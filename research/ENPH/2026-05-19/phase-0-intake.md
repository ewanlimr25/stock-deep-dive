# Phase 0 — Intake

**Ticker:** ENPH
**As-of date:** 2026-05-19 (requested) → **2026-05-15 effective** (latest UW data)
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/ENPH/2026-05-19
**Version:** v1
**Generated:** 2026-05-19T00:00:00-04:00

## Summary

Ticker validated (ENPH, Enphase Energy, US-listed residential-solar
microinverter manufacturer). Output directory created fresh; no prior versions.
UW MCP reachable; latest available data across all five subsystems is
**2026-05-15 (Friday)**. Requested as-of is 2026-05-19 (Tuesday) but UW
parquet snapshots through that date are not yet on disk, so all downstream
phases will pass `date=2026-05-15` to UW tools and treat the effective lens
as Friday's close. Initial sanity probe found a single-trade unusual-volume
signal of **$14.6M premium in ENPH June-2027 $45 puts** (vol 12,308 vs OI 71,
vol/OI 173x) — flagged as the dominant flow datapoint to chase in phase-1.

## UW availability

- `historical_available_dates`: ok
- Latest available options date: **2026-05-15**
- Latest available darkpool date: **2026-05-15**
- Latest available OI date: **2026-05-15**
- Latest available hotchains date: **2026-05-15**
- Latest available screener date: **2026-05-15**

(Note the gap in the snapshot list between 2026-04-27 and 2026-03-27 — data
exists for the May window we care about; the multi-week gap is in March/April
and does not affect 30-day historical tools for this run.)

## Ticker sanity

- Options activity (`options_flow_unusual_volume` top 1, date=2026-05-15):
  **ENPH 2027-06-17 $45 PUT** — premium $14,646,017, volume 12,308, OI 71,
  vol/OI ratio 173.4, avg_iv 0.7585.
- Active and deeply liquid; no abort needed. Activity is not "thin".

## Effective date convention for this run

Every UW MCP call in phases 1–7 will pass `date="2026-05-15"`. Macro phase
(phase-6) will use real-time WebSearch and FRED (if key set) for prints
through 2026-05-19. Phase-8 sub-agents will be told the effective tape is
Friday's close.

## Prior versions

None (v1).

## Tool errors

None. Both smoke tests returned successfully.
