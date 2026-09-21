# Phase 0.5 — Cross-Sectional & Self-History Context

## Summary

Today's FSLY tape is **NOT unusual — it is quieter than the name's own norm**, with
only a mild call-tilt. Against its trailing 35 sessions, 2026-05-29 sits at the
**9th self-percentile on share volume**, **15th on total options premium**, **26th
on call premium**, and **15th on P/C ratio** (call-tilted but not extreme). The only
metric above median is **net-call premium at the 62nd self-percentile** — a slight
directional lean, on a small-cap, on a light day. Cross-sectionally FSLY is
**outside the top-50 on net bullish premium and outside the top-100 on
volume-vs-average** — it is not a flow-leading name today.

The +4.87% price move is therefore **larger than the flow that accompanied it** —
a small-cap drifting up on light participation, not a conviction-flow breakout. The
one genuinely interesting structural fact (from intake) is that this is a **+74.5%
YTD, 14.6%-short-float momentum/squeeze name** — so even a quiet, light-volume
call-tilt can matter more than the raw dollars suggest *if* it marks the start of
another squeeze leg. But on the flow evidence alone, today is unremarkable.

**Verdict: BUSY_NAME_NORMAL_DAY → leaning QUIET** (volume 9th pctile is genuinely
thin). Downstream conviction should stay **low** and phases 1–2 confluence is
**capped** (the magnitude is below-normal for the name). Context only — no
directional bias.

## Universe ranking (net bullish premium) `[CTX:]`

- FSLY is **OUTSIDE the top-50** on net bullish premium today — not among the day's
  directional leaders (the board is led by mega-caps; a $2.65B name with $123k
  net-call premium does not rank). `[CTX:universe_rank_net_dir]`
- **OUTSIDE the top-100** on volume-vs-average — today's option volume is **not**
  unusual versus FSLY's 30-day average. This is the cross-sectional confirmation of
  the intake's "0.48× avg volume" light-tape read. `[CTX:volume_vs_average]`

## Sector read `[CTX:]`

- FSLY is Technology, the sector leading the broad tape (phase-6 will quantify), but
  **FSLY itself is not participating in size** — it's outside the directional and
  volume leaderboards. A small-cap laggard-by-magnitude inside a bid sector; the
  sector tailwind is generic, not FSLY-specific. `[CTX:sector_leadership]`

## Self-history (DuckDB, 35 sessions 2026-03-13 → 2026-05-29) ` DUCKDB`

| Metric | Today | Self-percentile | Read |
|--------|-------|-----------------|------|
| Share volume | 5.10M | **9** | very light — quietest decile |
| Total premium | $1.58M | 15 | below-normal |
| Call premium | $1.26M | 26 | below-normal |
| **Net call premium** | +$123k | **62** | mildly elevated (only above-median metric) |
| P/C ratio | 0.27 | 15 | call-tilted (low = call-heavy) |
| IV rank | 46.4 | 29 | below-median for the name |

The self-history is unambiguous: **a below-normal day on volume and premium, with a
modest call-directional lean.** Nothing here is a 90th-percentile signal.
`[CTX:self_pctile_net_dir DUCKDB]`

## Composite (`uw insights deep-dive`) `[CTX:]`

- Dark pool (whole-day aggregate): **$10.5M premium, 596.5k shares, 32 trades, avg
  $17.51** — small (consistent with the light tape). Detail → phase-2.
- Top OI changes are **fresh upside calls**: 20C 7/17 (+1,775 OI), 30C 7/17 (+1,233),
  17C 0DTE (+1,154), plus a lottery-ticket 45C 6/18 (+239). The 30C and 45C are
  deep-OTM (+69% / +153%) — squeeze-lottery positioning. Detail → phase-3.
- `yahoo_fundamentals`: **HTTP 401** (unavailable; phase-7b uses `fz`/WebSearch).

## Source

CLI + DuckDB. `uw screener bullish-bearish / volume-vs-average`,
`uw insights deep-dive`, plus a DuckDB self-history percentile cut (35 sessions; note
the 03-27→04-27 gap). FSLY **outside top-50 (net-dir)** and **outside top-100
(vol-vs-avg)** — recorded, not errors.

## Verdict for downstream `[CTX:]`

```
universe_pctile_total_prem:  15            # self-history (cross-sec: outside top-50 net-dir)
universe_rank_net_dir:       outside top-50
sector_leadership:           TECHNOLOGY leading tape; FSLY not participating in size
iv_rank:                     46.4          # 29th self-percentile
implied_move_pct:            2.46%         # daily implied move (uw screener implied_move_perc)
self_pctile_net_dir:         62            # mild call lean; everything else below-median
self_pctile_volume:          9             # very light tape
unusual_verdict:             BUSY_NAME_NORMAL_DAY (leaning QUIET — volume 9th pctile)
```

## Upstream references

- phase-0-intake.md §Summary — "$17.77, +4.87%, vol 5.1M (0.48× avg), P/C 0.27";
  phase-0.5 confirms those are **below-normal** for FSLY (volume 9th pctile, premium
  15th) → the price move outran the flow. NOT a genuine-unusual flow day.
- phase-0-intake.md §Finviz — "+74.5% YTD, short float 14.64%": the structural
  squeeze-name context that makes even a quiet call-tilt worth tracking, though the
  flow magnitude today does not confirm a new leg.

## Next phase

- phase-1-flow.md (options flow — are the sweeps/top-premium trades meaningfully
  call-directional, or is the thin tape just noise around a 4.9% drift?)
