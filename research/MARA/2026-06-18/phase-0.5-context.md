# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** MARA
**As-of date:** 2026-06-18
**Generated:** 2026-06-19
**Upstream phases cited:** phase-0-intake.md

## Summary

MARA is a **busy name having a roughly normal day with a mild net-bearish lean** —
not a directional leader. Cross-sectionally its *total* option premium is rich
(96.4th universe percentile) and volume-vs-average is elevated (94.9th pctile), so
the tape is active — but by MARA's **own** history total premium is only 58th
percentile (a normal day), and the *net direction* is the tell: heavy call **volume**
(PCR 0.128) yet net aggressor flow is **bearish** — `bullish_premium − bearish_premium
= $5.72M − $7.32M = −$1.61M`, putting MARA in the **1.5th universe percentile on
net-directional premium** (i.e. among the most net-bearish names, in pctile terms,
though small in absolute dollars → outside top-50 either direction). Calls are being
**sold/overwritten**, not bought. Verdict: **BUSY_NAME_NORMAL_DAY** → phases 1–2
confluence is capped at `+` (not `++`) per `rubrics/confluence-scoring.md`.

## Universe ranking (today, 2026-06-18)

| Metric | MARA standing | Leaders |
|--------|---------------|---------|
| Net **bullish** premium | **outside top-50** | MU $522M, SNDK $110M, INTC $92M, MRVL $84M, AMD $26M (semis lead) |
| Net **bearish** premium | **outside top-50** | SPX −$396M, PLTR −$156M, **MSTR −$89M**, MSFT −$79M, NVDA −$31M |
| Volume-vs-average (≥2×) | outside top-50 (but 94.9th pctile across universe) | — |
| IV-rank (high) | outside top-50 | — |

- Exact universe percentiles `[CTX:universe_pctile DUCKDB]` (§C, all ~6.2k optionable names):
  total_prem **96.4** · net_dir **1.5** (net-bearish) · iv_rank **38.6** · vol_vs_avg **94.9**.
- Single-name leaders are semis (MU/SNDK/INTC/MRVL/AMD/AVGO/TSM/CRDO) — Technology
  owns today's bullish tape; ETFs (IBIT, SMH, SPY, SOXL, QQQ, GLD) set aside.

## Sector read (crypto-proxy complex is MIXED — yellow flag)

MARA's Finviz tag is **Financial / Capital Markets**, but functionally it's a
**bitcoin-beta proxy** (β = 5.35). The crypto complex is *not* uniformly bid today:
- **IBIT** (spot-BTC ETF) ranks **#4 on net bullish** (+$103M) — bullish on BTC itself.
- **MSTR** (BTC-treasury equity proxy) ranks **#3 on net bearish** (−$89M).
- **MARA** mildly net-bearish (−$1.6M).

So the **leveraged crypto-equity proxies (MSTR, MARA) are seeing net call-selling /
bearish aggressor flow while the underlying BTC ETF gets bought** — the equity proxies
are *lagging* the spot vehicle. This is a yellow flag for phase-6/phase-8 to resolve:
is the bid for BTC, but not for the miners' equity? Hand-off to macro.

## Self-history (49 sessions, gap-aware — local window has the 03-28→04-24 hole)

- `self_pctile_total = 58.3` — today's total option premium is **mid-pack for MARA**
  (a normal day, not an event spike). `[CTX:self_pctile DUCKDB]`
- `self_pctile_net_dir = 12.5` — today's net direction is in the **bottom ~12%** of
  MARA's own recent sessions (a modestly bearish day for itself, not extreme).
- Recent net_dir ($M): 06-18 **−1.61**, 06-17 −3.00, 06-16 +0.36, 06-15 +0.41,
  06-12 **+3.92**, 06-11 +1.51, 06-10 −0.63, 06-09 −1.11. → **choppy, no persistence**;
  two soft net-bearish days but well inside the ±$4M normal range.

## Price/trend context (advisory, `fz`)

- Spot **$14.22** · Perf YTD **+58.35%** · Perf Week +4.48% · RSI(14) **55.7** (neutral).
- Price is **+12.6% above SMA50 and +13.4% above SMA200** — a clean uptrend; the
  bearish *flow* lean is happening into an *up*-trending name (overwriting-against-gains
  is a plausible read). β = **5.35** (extreme crypto leverage). ` fz`

## Source

CLI rankings (`uw screener` ×4, `uw insights deep-dive`) **+ DuckDB §C** exact
universe & self-history percentiles (local parquet present for 2026-06-18). MARA is
"outside top-50" on bullish, bearish, volume-vs-avg, and iv-rank CLI lists — recorded,
not an error. Sector field from `fz` (UW sector field is known-broken).

## Verdict for downstream — `[CTX:]` block

```
universe_pctile_total_prem:  96.4          # rich absolute premium — but it's an always-active name
universe_rank_net_dir:       outside top-50 (both directions); universe net_dir pctile 1.5 (net-bearish)
sector_leadership:           crypto-equity proxies (MSTR/MARA) LAGGING — net-sold while BTC-ETF (IBIT) bid; semis lead the broad bullish tape
iv_rank:                     30.3          # from insights deep-dive (iv30d 79.7%)
implied_move_pct:            1.46          # implied_move_perc 0.01456 → feeds phase-9 expected-move (N4)
self_pctile_net_dir:         12.5          # DUCKDB; bottom ~12% of MARA's own sessions (mildly bearish for itself)
unusual_verdict:             BUSY_NAME_NORMAL_DAY
```

**Calibration note for phases 1–9:** treat the headline "$15M premium / 96th pctile"
with caution — it is normal magnitude *for MARA*, and the net lean is **mildly
bearish via call-selling**, not bullish despite the heavy call volume. Conviction
should track the *net-directional* read, not the gross call activity. Phase-1/2
confluence capped at `+`.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq`/SQL path | Rows used |
|------------------|------------------------------|-----------|
| `uw screener bullish-bearish --direction bullish --top-n 50 --date 2026-06-18 --json` | MARA outside top-50 ← `[.results[].ticker]\|index("MARA")` | top-50 |
| `uw screener bullish-bearish --direction bearish --top-n 50 --date 2026-06-18 --json` | MARA outside top-50; MSTR rank3 −$89.3M | top-50 |
| `uw screener volume-vs-average --min-volume-ratio 2 --top-n 50 ...` | MARA outside top-50 | top-50 |
| `uw screener iv-rank --mode high --top-n 50 ...` | MARA outside top-50 | top-50 |
| `uw insights deep-dive --symbol MARA --date 2026-06-18 --json` | bull 5,715,408 / bear 7,321,224 / call_prem 12,926,879 / put_prem 2,231,047 / pcr 0.1276 / iv_rank 30.30 / iv30d 0.7969 / implied_move_perc 0.01456 / next_earnings 2026-08-04 ← `.uw_screener.*` | 1 |
| DuckDB §C universe pctile (`stock-screener-2026-06-18.parquet`) | total 96.4 / net_dir 1.5 / iv 38.6 / vol 94.9; MARA close 14.22 ← `PERCENT_RANK()` | universe |
| DuckDB §C self-history (49 files) | self net_dir 12.5 / self total 58.3 / N=49 ← `PERCENT_RANK()` | 49 sessions |
| `fz quote MARA --agent` | sector Financial/Capital Markets, Perf YTD 58.35%, RSI 55.7, SMA50 +12.6%, SMA200 +13.4%, β 5.35 | 1 |

## Tool errors

(none — `uw insights deep-dive` `yahoo_fundamentals` block returned nulls for
price/sector/marketCap; substituted close=$14.22 from the local screener parquet and
sector from `fz`. Not an error, a thin sub-block.)
