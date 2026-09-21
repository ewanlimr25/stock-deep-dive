# Phase 0.5 — Cross-Sectional & Self-History Context

## Summary

Today's CRM tape is **genuinely unusual for the name on the call/directional axis,
but mid-pack cross-sectionally.** Against its own trailing 35 sessions, 2026-05-29
is CRM's **most call-heavy day in the window**: call premium and net-call premium
both **100th self-percentile**, share volume **100th percentile**, P/C ratio
**0th percentile** (i.e. the lowest / most call-skewed), total options premium
**88th percentile**. Yet IV rank sits at only the **35th self-percentile** — options
got *cheaper*, not more expensive, into the move (an IV-crush footprint).

Cross-sectionally, CRM ranks **#33 of the top-50 on net bullish premium**
(net_flow +$6.88M) — its sector leads the tape (Technology fills the top of the
board: NDX/MSFT/DELL/ORCL/PLTR/NOW), but **CRM is a laggard within its own leading
sector**. It is **outside the top-80** on both volume-vs-average and IV-rank.

Net read: **the flow is real and directional (call-heavy, fresh, name-unusual), but
CRM is not a market-leading flow name today** — it is a beaten-down sector laggard
(−27.86% YTD) having its single most call-heavy session of the window, on a +8.5%
price pop. **Verdict: GENUINELY_UNUSUAL** (self-axis), with a cross-sectional
"laggard-in-a-leading-sector" caveat that phase-6 must weigh. **Context only — no
directional bias set here.**

## Universe ranking (net bullish premium, top-50)

| Rank | Ticker | net_flow | Note |
|------|--------|----------|------|
| 1 | NDX | +$143.9M | index |
| 2 | MSFT | +$136.0M | software mega-cap |
| 3 | DELL | +$122.0M | |
| 4 | ORCL | +$59.8M | software |
| 5 | PLTR | +$56.7M | software |
| 6 | NOW | +$46.3M | software (direct CRM peer) |
| … | | | |
| **33** | **CRM** | **+$6.88M** | bullish $58.2M / bearish $51.3M |

- CRM **is** in the day's net-bullish leaders, but deep in the pack — its absolute
  net directional dollars are ~5% of MSFT's. `[CTX:universe_rank_net_dir]`

## Sector read

- **Technology leads today's directional tape** — software/large-cap tech occupy
  essentially the entire top of the net-bullish board (MSFT, ORCL, PLTR, NOW, plus
  DELL). CRM's sector is **in favour**.
- But **CRM lags its own sector**: direct software peers MSFT (#2), ORCL (#4),
  PLTR (#5), NOW (#6) all rank far ahead on net bullish flow. A name strong while
  its sector is bought is normally confirmation; here the **name is the laggard of
  a bought sector** — a yellow flag for phase-6 (is CRM a catch-up trade, or being
  left behind?). `[CTX:sector_leadership]`

## Self-history (DuckDB, 35 sessions 2026-03-13 → 2026-05-29) ` DUCKDB`

| Metric | Today | Self-percentile | Read |
|--------|-------|-----------------|------|
| Call premium | $94.5M | **100** | highest in window |
| Net call premium | +$6.51M | **100** | highest in window |
| Total premium | $119.5M | 88 | elevated |
| Share volume | 20.6M | **100** | highest in window |
| P/C ratio | 0.235 | **0** | most call-skewed in window |
| IV rank | 61.4 | 35 | **below**-median for the name (crushed) |

The self-history read is unambiguous: **the most aggressively call-tilted day CRM
has had in the visible window, on peak volume, with IV falling** — the signature of
a post-event directional repricing rather than a fear/hedging spike.
`[CTX:self_pctile_net_dir DUCKDB]`

## Composite (`uw insights deep-dive`)

- Dark pool (whole-day aggregate): **$1.45B premium, 7.62M shares, 1,891 trades,
  avg $190.15** — heavy institutional cash-tape participation right at the close
  level ($191.10). (Detail → phase-2.)
- Top OI changes skew to **fresh calls**: 190C 6/5 (+2,481 OI), 190C 7/17 (+1,069),
  180C 8/21 (+695) — but also a notable **160P 7/17 (+1,407 OI)** downside hedge.
  (Detail → phase-3.)
- `yahoo_fundamentals`: **HTTP 401** (unavailable; phase-7b will use `fz`/WebSearch).

## Source

CLI + DuckDB. `uw screener bullish-bearish / volume-vs-average / iv-rank`,
`uw insights deep-dive`, plus a DuckDB self-history percentile cut over the local
screener parquet (35 sessions; note the 03-27→04-27 gap inside the window). CRM is
**outside top-80** on volume-vs-average and IV-rank (recorded, not an error).

## Verdict for downstream `[CTX:]`

```
universe_pctile_total_prem:  88            # self-history proxy (cross-sec rank #33/50 net-dir)
universe_rank_net_dir:       33            # of top-50; sector leads, name lags
sector_leadership:           TECHNOLOGY leading the tape; CRM lagging within it
iv_rank:                     61.4          # 35th self-percentile — IV crushed into the move
implied_move_pct:            0.52%         # daily implied move (uw screener implied_move_perc)
self_pctile_net_dir:         100           # most call-heavy day in 35 sessions
unusual_verdict:             GENUINELY_UNUSUAL (self-axis; laggard-in-leading-sector caveat)
```

## Upstream references

- phase-0-intake.md §Summary — "$191.10, +8.47%, vol 20.6M (1.6× avg), P/C 0.235";
  phase-0.5 confirms those raw numbers are **self-history extremes** (100th-pctile
  call premium & volume), i.e. genuinely unusual for CRM, not a busy-name normal day.
- phase-0-intake.md §Finviz — "−27.86% YTD, short float 7.91%": the cross-sectional
  "laggard in a leading sector" finding is consistent with the beaten-down YTD print.

## Next phase

- phase-1-flow.md (options flow — sweeps, top-premium, smart-money: is the call-heavy
  flow aggressive/opening and on the ask, or passive? which strikes/expiries?)
