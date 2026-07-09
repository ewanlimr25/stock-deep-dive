"""OHLCV sourcing for the trade-plan skill.

The Unusual Whales substrate (``~/Documents/Stocks/*.parquet``) is options /
dark-pool / OI centric and carries NO clean price bars. Chart structure and
pattern detection need real OHLCV, so this module sources it with graceful
degradation:

    1. yfinance (primary)         -- full daily OHLCV history, many sessions.
    2. Stock Screener parquet     -- offline fallback. Has date/close/high/low/
       (DuckDB)                       prev_close/total_volume per ticker per day
                                      (no ``open`` -> synthesised from prev_close).

Like the ``uw-daily-analysis`` enrichment scripts, this NEVER raises for a
missing source: it returns a structured dict with an ``available`` flag and a
``source`` label so the caller can degrade instead of crashing.

Pure-ish: the public entry points return immutable dataclasses / plain dicts and
do not mutate their inputs.
"""

from __future__ import annotations

import glob
import os
from dataclasses import dataclass
from datetime import date as date_cls
from datetime import datetime, timedelta
from pathlib import Path

import numpy as np
import pandas as pd

STOCKS_DIR = Path(os.environ.get("STOCKS_DIR", str(Path.home() / "Documents" / "Stocks")))
SCREENER_GLOB = "Stock Screener/stock-screener-*.parquet"


@dataclass(frozen=True)
class OHLCResult:
    """Daily OHLCV frame plus provenance. ``df`` is indexed by date (ascending)."""

    ticker: str
    as_of: str
    source: str  # "yfinance" | "screener_parquet" | "none"
    available: bool
    df: pd.DataFrame  # columns: open, high, low, close, volume
    note: str = ""

    @property
    def sessions(self) -> int:
        return 0 if self.df is None else int(len(self.df))


def _empty_frame() -> pd.DataFrame:
    return pd.DataFrame(columns=["open", "high", "low", "close", "volume"])


def _from_yfinance(ticker: str, as_of: str, lookback_days: int) -> OHLCResult | None:
    """Daily bars up to and including ``as_of`` (look-ahead safe)."""
    try:
        import yfinance as yf  # local import: optional dependency
    except Exception:  # pragma: no cover - environment without yfinance
        return None

    try:
        end = datetime.strptime(as_of, "%Y-%m-%d").date() + timedelta(days=1)
        start = end - timedelta(days=lookback_days + 5)
        raw = yf.download(
            ticker,
            start=start.isoformat(),
            end=end.isoformat(),
            interval="1d",
            auto_adjust=False,
            progress=False,
            threads=False,
        )
    except Exception:
        return None

    if raw is None or len(raw) == 0:
        return None

    # yfinance may return a column MultiIndex when one ticker is requested.
    if isinstance(raw.columns, pd.MultiIndex):
        raw.columns = [c[0] for c in raw.columns]

    cols = {c.lower(): c for c in raw.columns}
    needed = ["open", "high", "low", "close"]
    if not all(n in cols for n in needed):
        return None

    df = pd.DataFrame(
        {
            "open": raw[cols["open"]].astype(float),
            "high": raw[cols["high"]].astype(float),
            "low": raw[cols["low"]].astype(float),
            "close": raw[cols["close"]].astype(float),
            "volume": raw[cols.get("volume", cols["close"])].astype(float)
            if "volume" in cols
            else np.nan,
        }
    )
    df.index = pd.to_datetime(df.index).date
    df = df[df.index <= datetime.strptime(as_of, "%Y-%m-%d").date()]
    df = df.dropna(subset=["close"]).sort_index()
    if len(df) < 5:
        return None
    return OHLCResult(ticker, as_of, "yfinance", True, df,
                      note=f"{len(df)} daily sessions via yfinance")


def _from_screener_parquet(ticker: str, as_of: str) -> OHLCResult | None:
    """Offline fallback: reconstruct H/L/C from the UW Stock Screener export.

    The screener parquet has one row per ticker per session with
    ``close/high/low/prev_close/total_volume`` (no ``open``). We synthesise
    ``open := prev_close`` -- adequate for swing S/R, MAs and pivots, not for
    candle-body patterns.
    """
    try:
        import duckdb
    except Exception:  # pragma: no cover
        return None

    files = sorted(glob.glob(str(STOCKS_DIR / SCREENER_GLOB)))
    files = [f for f in files if Path(f).stem.split("stock-screener-")[-1] <= as_of]
    if not files:
        return None

    file_list = ", ".join(f"'{f}'" for f in files)
    query = f"""
        SELECT date, prev_close, close, high, low, total_volume
        FROM read_parquet([{file_list}])
        WHERE ticker = ? AND date <= ?
        ORDER BY date
    """
    try:
        rows = duckdb.execute(query, [ticker.upper(), as_of]).fetchall()
    except Exception:
        return None
    if not rows or len(rows) < 5:
        return None

    df = pd.DataFrame(rows, columns=["date", "prev_close", "close", "high", "low", "volume"])
    df["open"] = df["prev_close"].fillna(df["close"])
    df.index = pd.to_datetime(df["date"]).dt.date
    df = df[["open", "high", "low", "close", "volume"]].astype(float).sort_index()
    return OHLCResult(ticker, as_of, "screener_parquet", True, df,
                      note=f"{len(df)} sessions via UW screener parquet (open=prev_close synth)")


def load_ohlc(ticker: str, as_of: str, lookback_days: int = 540) -> OHLCResult:
    """Load daily OHLCV up to ``as_of`` (inclusive). Never raises.

    Tries yfinance first, then the offline screener parquet. Returns an
    ``OHLCResult`` whose ``available`` flag is False (with an empty frame) only
    when both sources fail.
    """
    for loader in (
        lambda: _from_yfinance(ticker, as_of, lookback_days),
        lambda: _from_screener_parquet(ticker, as_of),
    ):
        res = loader()
        if res is not None and res.available:
            return res
    return OHLCResult(ticker, as_of, "none", False, _empty_frame(),
                      note="no OHLC source available (yfinance + parquet both failed)")
