# Phase 0 — Intake

**Ticker:** FSLY (Fastly Inc)
**As-of date:** 2026-05-29
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/FSLY/2026-05-29
**Version:** v1
**Generated:** 2026-05-31

## Summary

Ticker validated. **FSLY (Fastly Inc)**, Technology, Common Stock, **small-cap
~$2.65B**. Output directory created. `uw` CLI reachable; local parquet present for
the as-of date (lag 0). **PROCEED.**

The as-of day is a **modest up-day on light volume**: FSLY closed **$17.77, +4.87%**
vs prev close $16.94, on **5.1M shares — only ~0.48× the 30-day avg of 10.7M**. Flow
is call-tilted (P/C ratio **0.27**; call premium **$1.26M** vs put **$0.32M**), but
the dollar amounts are small (this is a $2.65B name, not a mega-cap). IV is **high**
(iv30d **0.88**, IV rank 46) — typical for a volatile small-cap.

The recent tape is **choppy and momentum-driven**, not trending cleanly: the last 12
sessions alternate sharp up and down days (+7.78% on 5/26, −4.72% on 5/27, +4.87% on
5/29). The structural backdrop is the headline: FSLY is **+74.5% YTD**, a heavily
**shorted (14.64% of float)**, **low-beta (0.37)** momentum/short-squeeze name
sitting mid-range ($17.77 vs 52-week $6.29–$34.82). Central question for the dive:
is the +4.9% call-tilted pop on light volume the next leg of a squeeze/momentum run,
or noise inside a volatile chop with a heavy short base that can cut both ways?

## UW availability

- `uw historical available-dates`: **ok** — all five data types present through 2026-05-29.
- Latest available options date: 2026-05-29
- Latest available darkpool date: 2026-05-29
- Local coverage: 2026-03-13 → 2026-05-29 (known 03-27 → 04-27 gap).

## Ticker sanity

- Options activity (`unusual-volume --symbol FSLY --top-n 1`): **FSLY 24C exp
  2026-06-26**, total_volume 156 vs OI 3 → vol/OI 52×, premium ~$4.3k, avg IV **0.91**.
  Confirms options trade but **thin** — a $2.65B small-cap, low absolute contract
  counts. Not abort-worthy (known equity, real chain), but flag **thin options
  activity** so later phases weight magnitude accordingly.

## Local data (escape hatch / gap-awareness)

- `local_data_available`: **yes** · `duckdb_available`: **yes** (DuckDB 1.5.2)
- `STOCKS_DIR`: ~/Documents/Stocks
- Available local screener dates: 2026-03-13..03-27, then 2026-04-27..2026-05-29
  (gap flagged: **yes** — non-contiguous 03-27 → 04-27).
- Note: the `uw` CLI is primary; DuckDB used directly here for the intake row and
  12-day trajectory, tagged ` DUCKDB`.

## Finviz augments (`fz`)

- `fz_available`: **yes**
- `Shs Float`: **145.24M** (Shs Outstand 156.37M) — carried to phases 2/3 for
  %-of-float normalization.
- Carried snapshot: **Short Float 14.64%** (HIGH), Short Ratio 1.74, Insider Own
  7.19%, Inst Own 88.69%, **Beta 0.37** (LOW), **Perf YTD +74.51%**, Recom 2.42,
  Target $25.20.

## Key intake datapoints (carried forward)

| Field | Value | Source |
|-------|-------|--------|
| Close / prev close | $17.77 / $16.94 | screener ` DUCKDB` |
| Day change | **+4.87%** | screener ` DUCKDB` |
| Volume / 30d avg | 5.1M / 10.7M (**0.48×** — light) | screener ` DUCKDB` |
| 52-week range | $6.29 – $34.82 | screener ` DUCKDB` |
| Market cap | $2.65B (small-cap) | screener ` DUCKDB` |
| IV rank / iv30d | 46.4 / 0.88 (high) | screener ` DUCKDB` |
| P/C ratio | 0.27 | screener ` DUCKDB` |
| Call / put premium | $1.26M / $0.32M | screener ` DUCKDB` |
| Total OI (call/put) | 229.6k (127.4k / 102.2k) | screener ` DUCKDB` |
| Next earnings | 2026-08-05 (>2mo out) | screener ` DUCKDB` |
| Short float / ratio | **14.64%** / 1.74 | ` fz` |
| Beta | 0.37 | ` fz` |
| Perf YTD | +74.5% | ` fz` |

## Tool calls

```bash
uw historical available-dates --json
uw options-flow unusual-volume --symbol FSLY --top-n 1 --json
fz quote FSLY --agent
# DuckDB intake row + 12-day trajectory from stock-screener-2026-05-29.parquet (+ trailing files)
```

## Prior versions

none (v1)

## Tool errors

none

## Next phase

- phase-0.5-context.md (cross-sectional + self-history context — is the +4.9%
  call-tilted pop genuinely unusual for FSLY, or noise on a light-volume day; where
  does a small-cap rank vs the universe/sector?)
