# Phase 0 — Intake

**Ticker:** SNOW (Snowflake Inc.)
**As-of date:** 2026-05-29
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/SNOW/2026-05-29
**Version:** v1
**Generated:** 2026-05-29

## Summary

Ticker validated (SNOW = Snowflake Inc., NYSE mega-cap, ~$88B). Output dir
created. UW CLI reachable; latest date 2026-05-29 == as-of (reproducible run).
SNOW carries deep options activity. `fz` available.

**⚠️ Earnings cross-check applied upfront (lesson from the PATH run):** SNOW
**reported earnings 2026-05-27 AMC** (fz `Earnings = "May 27 AMC"`; confirmed by
Finnhub news "Earnings Beat", "Roars Back To Life On AI Growth", HSBC upgrade).
UW `next_earnings_date = 2026-08-26` is the *next* print — consistent. So **this
2026-05-29 tape is the post-earnings reaction day** (T+2), and the stock is
**+6.84%** — a strong positive earnings response. Every later phase must read the
flow as post-earnings continuation, not a quiet pre-catalyst session.

**Headline intake signals (color only):**
- Price **$255.55, +6.84%** on the day — strong post-earnings rally.
- **Short float ≈ 5.81%** — modest; this is NOT a short-squeeze setup (contrast
  with PATH's 31%).
- Float 334.88M / shs out 346.6M (~$88B cap).
- Whole-tape: call premium **$232.6M** vs put **$28.3M** (P/C 0.40) — heavily
  call-tilted gross, but bull/bear premium near-balanced ($113.8M vs $118.2M).
- Dark pool **$1.10B** / 4.39M shares (large, befitting a mega-cap).

## UW availability

- `uw historical available-dates`: ok
- Latest darkpool / hotchains date: 2026-05-29 == as-of (reproducible)

## Ticker sanity

- Options activity (unusual_volume top 1): SNOW Jun-05 252.5P, vol/OI 275.5 —
  deep, liquid options surface (post-earnings repositioning).

## Local data (escape hatch / gap-awareness)

- `local_data_available`: yes · `duckdb_available`: yes
- `STOCKS_DIR`: /Users/ewan/Documents/Stocks
- Available local dates: 2026-03-13→03-27, **GAP**, 2026-04-27→05-29 (gap flagged
  yes; ~1mo missing 2026-03-28→04-26). Phase-5 lookbacks are non-contiguous.

## Finviz augments (`fz`)

- `fz_available`: yes
- `Shs Float`: **334.88M** (carried to phase-2/3 for %-of-float normalization)
- Shs Outstand 346.6M · Short Float 5.81% · Price $255.55 · Earnings 2026-05-27.

## Concurrent blueprints (for phase-6 correlation gate)

- **PATH/2026-05-29 exists** — phase-6 MUST run `uw risk portfolio-correlation`
  on SNOW vs PATH (prior memory noted SNOW/PATH ≈ 0.626). Correlation gate is
  **active** this run.

## Prior versions
(none — v1)

## Tool errors
(none)
