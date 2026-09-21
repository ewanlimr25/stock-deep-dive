# Phase 0 — Intake

**Ticker:** PATH
**As-of date:** 2026-08-12
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/PATH/2026-08-12
**Version:** v1
**Generated:** 2026-08-13T01:13:43Z

## Summary

Ticker validated (PATH = UiPath Inc, NYSE, Technology / Software-Infrastructure).
Output directory created fresh (no prior run on this date). UW CLI reachable and
fully current through the as-of date (options/darkpool/oi/hotchains/screener all
have a 2026-08-12 partition). Options activity confirmed present. Local parquet
snapshot is current through 2026-08-12 with DuckDB available as the escape hatch.
`fz quote` is hitting its known, previously-memoried degraded-output mode
(14-field subset, SI/float null) — recovered in full via `fz screen --tickers
PATH --view {ownership,technical,valuation}`, which surfaced a notably
elevated `Short Float=31.10%`. Proceeding to phase 0.5.

## UW availability

- `uw historical available-dates --json`: ok
- Latest available options date: 2026-08-12
- Latest available darkpool date: 2026-08-12
- Latest available oi date: 2026-08-12
- Latest available hotchains date: 2026-08-12
- Latest available screener date: 2026-08-12

## Ticker sanity

- Options activity (unusual_volume top 1, `--date 2026-08-12`): PATH 2026-08-28
  $14.5 put, `total_volume`=418, `open_interest`=24, `vol_oi_ratio`=17.42,
  `total_premium`=$18,475, `avg_iv`=0.6013 (source:
  `bot-eod-report-2026-08-12.parquet`)

## Local data (escape hatch / gap-awareness)

- `local_data_available`: yes · `duckdb_available`: yes
- `STOCKS_DIR`: /Users/ewan/Documents/Stocks
- Available local dates: continuous 2026-03-13→2026-03-27, **gap**
  2026-03-27→2026-04-27, then continuous 2026-04-27→2026-08-12 (through today's
  as-of date). Gap flagged: yes (known non-contiguous gap, pre-dates this run's
  window — no impact on phase 5/self-history lookback from 2026-08-12).
- Note: the `uw` CLI is primary; local DuckDB is opt-in for cuts the CLI can't
  express (`lib/duckdb-cuts.md`).

## Finviz augments (`fz`)

- `fz_available`: yes (binary reachable, `fz doctor --agent` → api "reachable",
  auth "not required", config "ok")
- `Shs Float`: **390.80M** — recovered via the `fz screen --view` route (see
  below), not the plain `fz quote` path.
  `fz quote PATH --agent` (and `--json --no-color --yes --no-cache` without
  `--compact`) returns only the known-degraded 14-field fundamentals subset
  (Book/sh, Cash/sh, Dividend*, Employees, Enterprise Value, IPO, Income,
  Index, Market Cap, Payout, Sales) instead of the documented 84-field grid —
  `Short Float`/`Shs Float`/`Shs Outstand`/`Short Ratio` all `null`. Verified
  not PATH-specific (`fz quote MSFT`/`AAPL` return the identical 14-key
  subset). This is a **known, recurring, already-memoried** `fz quote`
  degradation (prior recurrences: SHOP 2026-07-17, RKT 2026-07-17, MU
  2026-07-28 — see project memory `data-source-workarounds`), not a fresh
  fault.
  **Recovery used:** `fz screen --tickers PATH --view {ownership,technical,valuation} --agent`
  returns the full grid (ticker displays as `PPATH` — cosmetic doubling quirk,
  values correct):
  - ownership: `Float=390.80M`, `Outstanding=455.76M`, `Short Float=31.10%`,
    `Short Ratio=1.95`, `Inst Own=64.50%`, `Inst Trans=-6.43%`,
    `Insider Own=24.57%`, `Insider Trans=0.00%`, `Price=15.26`
  - technical: `RSI=70.94`, `SMA20=18.18%`, `SMA50=29.17%`, `SMA200=19.83%`,
    `Beta=1.00`, `ATR=0.79`, `52W High=-23.08%`, `52W Low=65.87%`
  - valuation: `P/E=25.18`, `Forward P/E=16.93`, `PEG=1.26`, `P/S=4.73`,
    `P/B=4.17`, `P/FCF=21.07`, `EPS Next Y=15.17%`, `EPS Next 5Y=13.43%`
- Note: `fz` supplements SI/float/peer/breadth only (`lib/fz-recipes.md`).
  Because the `screen --view` recovery worked cleanly, phase-2/3 CAN
  %-of-float normalize this run (`Short Float=31.10%` is a live, elevated read
  worth flagging into phase-7c), and phase-7b/7c should prefer this recovered
  `fz` data over WebSearch/Finnhub fallback where it overlaps.

## Prior versions

<empty for v1>

## Tool errors

- `fz quote PATH --agent | jq '.fundamentals'` — no hard error (exit 0), but
  output is a reduced 14-field object where the documented recipe
  (`lib/fz-recipes.md §1`) expects an 84-field grid including `Short Float`,
  `Shs Float`, `Shs Outstand`, `Short Ratio`, `Recom`, `Target Price`, `RSI (14)`,
  `SMA50/200`, `52W High/Low`. Reproduced across PATH/MSFT/AAPL with and without
  `--compact`/`--no-cache`. This matches the recurring `fz quote` degradation
  already logged in project memory (SHOP/RKT/MU) — treated as a known
  condition, not a fresh regression. **Resolved for this run** via the
  `fz screen --tickers <T> --view {ownership,technical,valuation}` recovery
  path (see Finviz augments section above); no data loss.
