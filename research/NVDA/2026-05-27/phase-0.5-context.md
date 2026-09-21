# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** NVDA
**As-of date:** 2026-05-27
**Generated:** 2026-05-28T02:16:00Z
**Upstream phases cited:** phase-0-intake.md

## Summary

NVDA is the **busiest options name in the universe today** (total option premium
99.9th percentile) but the flow is **not bullish** — on a net-directional basis
NVDA sits at the **0.1 percentile** (the single most net-*sold* megacap), ranking
**#4 on net bearish premium** behind only SPX, MU and AMD. The entire semiconductor
complex is leading the *bearish* tape today (MU/AMD/NVDA/SNDK/ARM/MRVL/SMH occupy
bearish ranks #2–#8). Relative volume is only mid-pack (58.7 pctile, not ≥2× avg),
and today's net-direction sits in the bottom quartile of NVDA's own 33-session
history — so this is a **busy name on an elevated (not anomalous) day with a
persistent, sector-wide net-bearish directional skew**. Verdict:
`BUSY_NAME_NORMAL_DAY` (confluence on phases 1–2 capped at `+`, not `++`), with the
real cross-sectional signal being the *bearish* net-direction, not bullish.

## Universe ranking (single names; ETFs set aside)

- **Net bearish premium: NVDA ranks #4** — `net_flow = -$66.25M`
  [CTX:universe_rank_net_dir]. Leaders: SPX −$6.06B, MU −$124.3M, AMD −$85.5M,
  NVDA −$66.3M, SNDK −$62.3M, ARM −$40.9M, MRVL −$37.2M, SMH −$34.8M.
- **Net bullish premium: NVDA outside top-50** — despite $1.482B gross call
  premium, NVDA does not appear among the day's net-bullish leaders (META #2,
  TSLA #3, ASTS #4, AAPL #9 lead the single-name bullish tape).
- **Volume-vs-average: NVDA outside top-50** (`vol_x` only 58.7 pctile) — today's
  option volume is *not* unusual relative to NVDA's 30-day average.

## Sector read

Semiconductors are **leading the bearish directional tape** today: MU, AMD, NVDA,
SNDK, ARM, MRVL and the SMH ETF cluster at the top of the net-bearish ranking. The
sector is decisively **out of favour on today's flow** — a bearish sector backdrop
that phase-6 (macro) must resolve. A name being net-sold *while its whole sector is
net-sold* is the bearish analogue of the strongest cross-sectional confirmation —
NVDA is not an idiosyncratic story today, it is moving with a semi-complex de-risk.

## Self-history (local parquet, DuckDB §C — N=33 available sessions, gap-aware)

| Metric | Today's percentile vs own history |
|--------|-----------------------------------|
| net-directional premium | **25.0** (bottom quartile — among NVDA's more bearish days) [CTX:self_pctile DUCKDB] |
| total premium | 78.1 (elevated but not extreme for the name) [CTX:self_pctile DUCKDB] |

Recent net-direction series ($M, DuckDB) shows **sustained net selling + collapsing
IV** over the last ~7 sessions:

| date | net_dir $M | total $M | iv_rank |
|------|-----------:|---------:|--------:|
| 2026-05-27 | −66.3 | 1824.9 | 30.5 |
| 2026-05-26 | −100.2 | 1444.1 | 34.2 |
| 2026-05-22 | −97.0 | 1369.9 | 27.3 |
| 2026-05-21 | −189.7 | 2405.2 | 34.2 |
| 2026-05-20 | +24.1 | 1716.0 | 61.0 |
| 2026-05-15 | −42.6 | 2184.0 | 76.7 |
| 2026-05-11 | +282.3 | 2662.2 | 62.9 |

IV rank has more than halved (≈76 → 30.5) over two weeks while net flow stayed
negative — vol is being sold *and* direction is bearish. The last decisively
bullish session was 2026-05-11.

## Source

CLI (`uw screener` bullish/bearish/volume-vs-average + `uw insights deep-dive`)
**+ DuckDB escape hatch §C** for exact universe + self-history percentiles. Local
snapshot present for 2026-05-27. Gap-aware: self-history N=33 *available* sessions
across the non-contiguous local window (2026-03-13→03-27, 2026-04-27→05-27), not a
contiguous 33 calendar days. "Outside top-50" recorded for net-bullish and
volume-vs-average (information, not error).

## Verdict for downstream

```
universe_pctile_total_prem:  99.9        # busiest name in the universe
universe_rank_net_dir:       #4 bearish (net_flow -$66.25M; net-dir pctile 0.1)
sector_leadership:           SEMIS leading the BEARISH tape today (out of favour)
iv_rank:                     30.5        # mid/low — IV collapsed from ~76 in mid-May
implied_move_pct:            1.94        # (implied_move_perc 0.0194; abs $4.12)
self_pctile_net_dir:         25.0        # bottom quartile of own 33-session history
unusual_verdict:             BUSY_NAME_NORMAL_DAY
```

**Notes for later phases:**
1. Phases 1–2 confluence **capped at `+`** (busy-name rule) — but note the cap
   guards against over-reading *bullish* magnitude; the genuine cross-sectional
   signal here is *bearish* net-direction, which phase 1 must investigate directly.
2. Huge gross call premium ($1.48B) coexists with the most-bearish net-direction in
   the universe → phase 1 must separate gross call *volume* from net *aggressor
   direction* (calls may be sold, not bought). This is the central question.
3. No earnings catalyst near-term — next earnings 2026-08-26 (~3 months out); IV
   rank 30.5 means options are not richly priced. Persistent vol-selling backdrop.
4. Sector context is bearish (semis net-sold); phase-6 must decide if this is a
   one-day de-risk or a regime shift.
