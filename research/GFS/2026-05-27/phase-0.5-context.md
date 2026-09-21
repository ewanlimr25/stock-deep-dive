# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** GFS
**As-of date:** 2026-05-27
**Generated:** 2026-05-28T00:00:00Z
**Upstream phases cited:** phase-0-intake.md

## Summary

GFS is a **busy, high-IV name on the first big red day of a parabolic run**, not a
clean directional flow signal. It ran **+35% in five sessions** ($66.75 on 05-19 →
$89.83 peak on 05-26) then dropped **−9.7% to $81.11** on the as-of date (05-27).
Today's **total option premium is top-5% of the entire optionable universe**
(95.5 pctile) and 84th-pctile for GFS itself — so the *magnitude* of activity is
genuinely elevated — but the **net direction is bearish-leaning** (universe net-dir
5.6 pctile; GFS self net-dir 21.9 pctile). It is outside the top-50 on both net
bullish and net bearish premium, and below 2× volume-vs-average. Critically, its
**sector (semiconductors) is leading the BEARISH tape today** — MU, AMD, NVDA, SNDK,
ARM occupy 5 of the top-6 net-bearish slots. Verdict: **BUSY_NAME_NORMAL_DAY** for
directional purposes (caps phases 1–2 confluence at `+`, not `++`), with the
overriding context that this is a **post-parabolic reversal-risk regime**.

## Universe ranking (today, 2026-05-27)

- **Net bullish premium rank:** outside top-50 `[CTX:universe_rank_net_dir]`.
  Leaders (single names): META +$61.7M, TSLA +$54.8M, ASTS +$32.5M, IREN +$30.8M,
  APP +$29.1M, AXTI +$25.3M (SPXW +$111M leads overall).
- **Net bearish premium rank:** outside top-50. Leaders: **MU −$124.3M, AMD
  −$85.5M, NVDA −$66.3M, SNDK −$62.3M, ARM −$40.9M** (SPX index aside).
- **Volume-vs-average:** below 2× (outside the ≥2× top-80 list), but **87.2 pctile**
  of the universe on vol/avg30 — elevated, just not extreme `[CTX:universe_pctile_vol DUCKDB]`.
- **Exact universe percentiles** `[CTX:universe_pctile DUCKDB]` (N=all optionable):
  - total premium: **95.5 pctile** (top 5% — busy)
  - net-directional premium: **5.6 pctile** (bottom 6% — bearish lean)
  - IV rank: **92.5 pctile** (top 8% — richly priced vol)
  - vol-vs-avg: **87.2 pctile**
  - sector: Technology · close $81.11 · mcap $50.01B

## Sector read

GFS's sector (semiconductors / Technology) is **leading the day's net-bearish
tape**: MU, AMD, NVDA, SNDK, ARM are 5 of the 6 most-sold names. Semis are being
distributed today, not accumulated. This is a **yellow flag** for phase-6 to
resolve — a single semi name showing balanced/slightly-bearish flow while its whole
sector is sold is *not* swimming with a tailwind. Hands the macro phase a clear
starting question: is this a semi-wide de-risk or GFS-specific?

## Self-history (parquet present, N=33 sessions; gap 03-27→04-27 noted)

- **self_pctile_net_dir: 21.9** — today is one of GFS's more bearish directional
  days `[CTX:self_pctile DUCKDB]`.
- **self_pctile_total: 84.4** — but total premium is high for GFS (run-driven).
- **self_pctile_ivrank: 81.3** — IV rank elevated for the name.

Recent series (the parabola + first red day):

| date | net_dir ($M) | tot_prem ($M) | iv_rank | close |
|------|-------------:|--------------:|--------:|------:|
| 2026-05-27 | **−0.30** | 10.31 | 79.1 | **81.11** |
| 2026-05-26 | +3.09 | 14.00 | 90.2 | **89.83** ← peak |
| 2026-05-22 | +1.52 | 13.55 | 74.2 | 85.64 |
| 2026-05-21 | +2.09 | 14.31 | 64.6 | 81.35 |
| 2026-05-20 | −0.35 | 2.23 | 55.6 | 70.79 |
| 2026-05-19 | +4.32 | 11.20 | 50.4 | **66.75** ← base |

The run was call-premium-led (net_dir positive through the rip); the as-of day is
the **first session the net flow turned negative as price broke down −9.7%**.

## Implied move / vol context (from `uw insights deep-dive`)

- **IV30d 82.3%**, **iv_rank 79.1** (deep-dive block) / 92.5 universe pctile.
- **implied_move 11.03 pts (13.6%)** `[CTX:implied_move_pct]` — feeds phase-9
  expected-move sizing.
- **Next earnings 2026-08-04** — ~10 weeks out. The rich IV is **NOT** an earnings
  event premium; it is the parabola's realized-vol bleed-through. That matters: vol
  can mean-revert lower without a catalyst date defending it.
- put_call_ratio 0.33 (call-heavy by volume), call_premium $8.37M vs put_premium
  $1.93M.

## Source

CLI (`uw screener` + `uw insights deep-dive`) **+ DuckDB §C** (exact universe &
self-history percentiles; parquet present for 2026-05-27). "Outside top-50" recorded
for both net-bullish and net-bearish premium; "below 2×" recorded for vol-vs-avg.

## Verdict for downstream

```
universe_pctile_total_prem:  95.5
universe_rank_net_dir:       outside top-50 (net ≈ flat / slight bear; 5.6 pctile)
sector_leadership:           SEMICONDUCTORS leading the BEARISH tape today (lagging/sold)
iv_rank:                     79.1   (92.5 universe pctile)
implied_move_pct:            13.6
self_pctile_net_dir:         21.9
unusual_verdict:             BUSY_NAME_NORMAL_DAY  (directional); regime = POST-PARABOLIC REVERSAL RISK
```

- **Bias from this phase:** neutral (context only — no directional bias set here).
- **Three things later phases must remember:**
  1. **Post-parabolic first red day.** +35% in a week → −9.7% on the as-of date.
     Treat any bullish flow as potential late-chase; treat bearish flow as
     potential top-distribution. Phases 1–2 confluence **capped at `+`**.
  2. **Sector is being sold.** Semis lead the bearish tape (MU/AMD/NVDA/SNDK/ARM).
     GFS is not riding a sector tailwind today.
  3. **Vol is rich without a catalyst.** IV rank 79 / 92.5 universe pctile, implied
     move 13.6%, earnings 10 weeks out → premium-selling structures favored over
     premium-buying, all else equal. Carry implied_move 13.6% to phase-9.
- **Open questions:** Is the −9.7% drop a one-day shakeout in an uptrend or the
  start of a distribution? (phases 1, 2, 5, 8b must resolve.) What drove the +35%
  run — fundamental catalyst or squeeze? (phase-7b/7c, given 7.08% short float.)
