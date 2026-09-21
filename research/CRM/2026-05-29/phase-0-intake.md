# Phase 0 — Intake

**Ticker:** CRM
**As-of date:** 2026-05-29
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/CRM/2026-05-29
**Version:** v1
**Generated:** 2026-05-31

## Summary

Ticker validated. **CRM (Salesforce Inc)**, Technology, Common Stock, mega-cap
~$144.3B. Output directory created. `uw` CLI reachable; local parquet present for
the as-of date (lag 0). **PROCEED.**

The as-of day is a **large up-day**: CRM closed **$191.10, +8.47%** vs prev close
$176.17, on **20.6M shares (~1.6× the 30-day avg of 12.8M)**. Flow is sharply
call-heavy (P/C ratio **0.235**; call premium **$94.5M** vs put premium **$24.9M**).
IV rank fell **96 → 55 → 61** across 5/27→5/29 — an IV-crush footprint. Next
earnings is dated **2026-09-02**, and the IV collapse + volume spike on 5/28–5/29
is consistent with **a catalyst/earnings reaction around 5/28–5/29** (treated as a
working hypothesis for later phases to confirm, not an asserted fact).

This is a **post-breakout, beaten-down-laggard** setup: CRM is **−27.86% YTD** and
sits at $191 vs a 52-week range $163.52–$276.80 (just ~17% off the low, ~31% below
the high), with a notable **7.91% short float**. The central question for the dive:
is the +8.5% pop the start of a durable reversal (short-driven / institutional
re-entry) or a one-day relief spike into an established downtrend?

## UW availability

- `uw historical available-dates`: **ok** — all five data types present through 2026-05-29.
- Latest available options date: 2026-05-29
- Latest available darkpool date: 2026-05-29
- Local coverage: 2026-03-13 → 2026-05-29 (with the known 03-27 → 04-27 gap).

## Ticker sanity

- Options activity (`unusual-volume --symbol CRM --top-n 1`): **CRM 270C exp
  2026-07-17**, total_volume 21,425 vs OI 157 → **vol/OI 136×**, total premium
  ~$1.70M, avg IV 0.54. Confirms live, heavy, *opening* call activity. Not thin.

## Local data (escape hatch / gap-awareness)

- `local_data_available`: **yes** · `duckdb_available`: **yes** (DuckDB 1.5.2)
- `STOCKS_DIR`: ~/Documents/Stocks
- Available local screener dates: 2026-03-13..03-27, then 2026-04-27..2026-05-29
  (gap flagged: **yes** — non-contiguous 03-27 → 04-27; ~60 trading-day self-history
  window 04-27→05-29 is contiguous and usable).
- Note: the `uw` CLI is primary; DuckDB used directly here for the intake row and
  trajectory (a custom cut the CLI doesn't expose as a single call), tagged ` DUCKDB`.

## Finviz augments (`fz`)

- `fz_available`: **yes**
- `Shs Float`: **792.87M** (Shs Outstand 819.00M) — carried to phases 2/3 for
  %-of-float normalization.
- Carried snapshot: Short Float **7.91%**, Short Ratio **4.71**, Insider Own 3.19%,
  Inst Own 93.39%, Beta **1.13**, Perf YTD **−27.86%**.

## Key intake datapoints (carried forward)

| Field | Value | Source |
|-------|-------|--------|
| Close / prev close | $191.10 / $176.17 | screener ` DUCKDB` |
| Day change | **+8.47%** | screener ` DUCKDB` |
| Volume / 30d avg | 20.6M / 12.8M (1.6×) | screener ` DUCKDB` |
| 52-week range | $163.52 – $276.80 | screener ` DUCKDB` |
| Market cap | $144.3B | screener ` DUCKDB` |
| IV rank (5/29) | 61.4 (was 96 on 5/27) | screener ` DUCKDB` |
| P/C ratio | 0.235 | screener ` DUCKDB` |
| Call / put premium | $94.5M / $24.9M | screener ` DUCKDB` |
| Net call premium | +$6.51M | screener ` DUCKDB` |
| Total OI (call/put) | 1.005M (568.8k / 436.3k) | screener ` DUCKDB` |
| Next earnings | 2026-09-02 | screener ` DUCKDB` |
| Short float / ratio | 7.91% / 4.71 | ` fz` |
| Beta | 1.13 | ` fz` |

## Tool calls

```bash
uw historical available-dates --json
uw options-flow unusual-volume --symbol CRM --top-n 1 --json
fz quote CRM --agent      # float / short / beta snapshot
# DuckDB intake row + 12-day trajectory from stock-screener-2026-05-29.parquet (and trailing files)
```

## Prior versions

none (v1)

## Tool errors

none

## Next phase

- phase-0.5-context.md (cross-sectional + self-history context — is this +8.5% / call-heavy day genuinely unusual, and how does CRM rank vs the universe/sector?)
