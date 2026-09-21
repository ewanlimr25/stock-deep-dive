# Phase 2 — Dark Pool & Block Prints

**Ticker:** IREN
**As-of date:** 2026-06-05
**Generated:** 2026-06-07T00:58Z
**Upstream phases cited:** phase-0-intake.md (float 324.15M), phase-0.5-context.md, phase-1-flow.md

## Summary

Off-exchange activity is **two-way institutional churn during a sharp
repricing, with a mild buy-side lean and no mega-tier conviction** — block-tier
buy_ratio 0.588 (suggestive band), large-tier 0.535 (≈balanced), mega tier
EMPTY (0 trades) [DP:block_stratified]. The 5-day price-level map reframes the
whole setup: a huge institutional shelf sits at **65.3–67.6** ($231.1M premium
at the 66.60 level alone) and at **61.0–61.9** ($43.6M at 61.86), while today's
prints walked down from 60–62 premarket to 53–55 by the close — IREN has
repriced ≈ −18% off its early-week institutional levels, and today itself
gapped/slid from ~60 premarket to a 51.57 low before V-recovering to 54.35
(consistent with the phase-1 underlying path, see phase-1-flow.md §Largest
premium prints). This is not clean distribution (buy ratios > 0.5) nor clean
accumulation (no mega prints; the big clusters are *above* spot because that's
where the stock traded, not because institutions are paying up).

## Key signals

- **Block-tier buy_ratio 0.588** (buy_volume 892,708 vs sell_volume 625,853;
  $83.7M, 41 trades) — suggestive-only dip-buying lean [DP:block_stratified];
  derived sell_ratio = 0.412. Large tier 0.535 on $404.6M / 2,056 trades.
- **Mega tier: zero trades** — no single-print institutional conviction either
  way [DP:block_stratified].
- **65.3–67.6 shelf**: 10 of the top-15 5-day price levels sit there, headed by
  66.60 = $231,138,154 / 3,470,543 sh / 31 trades — now MAJOR overhead supply
  [DP:price_levels].
- **Today's premarket prints at 60.30 / 59.90 / 61.86** (12:46Z, 12:56Z,
  11:44Z) vs a 54.35 close — institutions were active *before* the slide;
  extended-hours flow did not front-run the recovery [DP:extended_hours].
- **Largest single block = 0.042% of float** (136,648 sh @ 54.35 = $7.43M,
  20:46:31Z — at the closing price, benchmark/MOC-style) — individually
  meaningless for a 324.15M-float name [DP:block_pct_float fz]; the *aggregate*
  (8.94M sh stratified ≈ 2.76% of float) is the meaningful unit today.

## Detailed findings

### Largest blocks [DP:largest] (top-25, Σ$65.34M)

| Time (Z/ET) | Price | Size | Premium | NBBO context | % float |
|---|---|---|---|---|---|
| 20:46:31 / 16:46 | 54.35 | 136,648 | $7.43M | +0.495 vs mid (post-close, AT closing px) | 0.042% |
| 14:39:42 / 10:39 | 56.25 | 104,700 | $5.89M | −0.04 vs mid | 0.032% |
| 15:46:41 / 11:46 | 54.25 | 90,500 | $4.91M | −0.035 vs mid | 0.028% |
| 15:46:50 / 11:46 | 54.21 | 85,600 | $4.64M | +0.055 vs mid | 0.026% |
| 14:55:51 / 10:55 | 57.00 | 55,400 | $3.16M | **+1.07 above mid** (negotiated/late print) | 0.017% |
| 16:58:07 / 12:58 | 53.83 | 56,800 | $3.06M | +0.11 | 0.018% |
| 12:46:42 / 08:46 | 60.30 | 44,300 | $2.67M | premarket, at ask | 0.014% |
| 20:13:11 / 16:13 | 53.80 | 48,679 | $2.62M | post-close | 0.015% |

Pattern: sizes cluster 40–137k shares (all <0.05% float); pricing hugs mid —
crossing-network churn, not aggressive sweeps. The two 15:46Z prints (176k sh
combined within 9 seconds at 54.2x) coincide with the late-morning step down.

### Tier breakdown [DP:block_stratified] (jq: per-tier nested object; sell_ratio derived = 1 − buy_ratio)

| Tier | trades | buy_vol | sell_vol | buy_ratio | premium |
|---|---|---|---|---|---|
| mega | 0 | 0 | 0 | — | $0 |
| block | 41 | 892,708 | 625,853 | **0.588** | $83.72M |
| large | 2,056 | 3,969,690 | 3,456,375 | 0.535 | $404.56M |
| total | | | | | **$488.27M** |

0.588 sits in the 0.55–0.7 "suggestive only" band (heuristics); 0.535 is noise.
Stratified volume = 8.94M sh ≈ **2.76% of float** (324.15M, phase-0 fz
snapshot) — a heavy institutional hand-off day in aggregate.

### Price levels — 5-day window 06-01→06-05 [DP:price_levels]

| Level | Premium | Shares | Trades |
|---|---|---|---|
| **66.60** | **$231.14M** | 3,470,543 | 31 |
| 61.86 | $43.64M | 705,459 | 21 |
| 65.33 | $40.11M | 614,031 | 22 |
| 66.00 | $29.80M | 451,571 | 38 |
| 65.40–65.82 (4 levels) | $75.6M | 1.15M | 81 |
| 66.20 / 67.49 / 67.64 | $38.3M | 571k | 58 |
| 61.00 | $12.26M | 200,920 | 31 |
| 63.54 | $10.20M | 160,583 | 3 |
| 54.35 | $9.58M | 176,204 | 8 |

Read: the week's institutional volume lives at **65.3–67.6** (≈$450M total) —
overhead supply. Secondary shelf **61.0–61.9**. Today's spot (54.35) shows only
$9.6M — below 54 the 5-day map is uncharted. No cluster within 1% of spot
except today's own 54.35 prints. Window-anchor caveat checked: latest available
date = as-of (phase-0-intake.md), so the 5-day window is correct.

### Extended-hours activity [DP:extended_hours]

Premarket (11:44–13:17Z = 07:44–09:17 ET): prints at **61.86, 60.30, 59.90,
59.00, 58.90** ($0.7–2.7M each) — the stock was 59–62 before the regular
session; the whole −9% to the 51.57 low happened intraday. Post-close
(20:13–21:30Z): 53.80 / 54.35 prints including the day's largest ($7.43M at
exactly the 54.35 close — likely benchmark/closing-cross related, de-rated per
pitfalls). No catalyst-shaped pre-positioning visible; phase-6/7c should check
what news hit premarket (open question).

### Cross-sectional baseline [DP:ticker_summary]

IREN **outside top-30** dark-pool tickers today (leaders: QQQ $21.41B, SPY
$20.87B, MU $15.51B) — DP magnitude is elevated for the name but not
tape-leading.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw dark-pool largest --symbol IREN --top-n 25 --sort-by premium --date 2026-06-05 --json` | top block premium=$7,426,818.8, size=136,648 ← `.results[0].premium/.size`; Σ=$65,344,466 | top-25 |
| `uw dark-pool block-stratified --symbol IREN --top-n 30 --min-tier large --date 2026-06-05 --json` | block.buy_ratio=0.588, large.buy_ratio=0.535, mega.trade_count=0, total=$488,273,934.72 ← `.results[]\|select(.ticker=="IREN")` | 1 ticker row |
| `uw dark-pool extended-hours --symbol IREN --top-n 15 --date 2026-06-05 --json` | premarket 60.30/59.90/61.86 prints ← `.results[:8]` | top-15 |
| `uw dark-pool price-levels --symbol IREN --top-n 15 --days 5 --date 2026-06-05 --json` | 66.60 level: total_premium=$231,138,154.59, total_shares=3,470,543 ← `.results[0]` | 15 levels |
| `uw dark-pool ticker-summary --top-n 30 --date 2026-06-05 --json` | IREN outside top-30 ← ticker match on `.results[]` | top-30 |
| float normalization (fz snapshot, phase-0) | 136,648 / 324.15M = 0.042%; 8.94M / 324.15M = 2.76% | derived |

## Tool errors

(none)

## Verdict for downstream phases

- **Bias from this phase:** **Mixed — two-way churn with a mild (suggestive-only)
  buy lean** into the flush; NOT confirmation of phase-1's bearish tape, and
  NOT clean accumulation either (mega tier empty).
- **Conviction:** 2/5 (buy_ratio 0.588 is below the 0.7 high-confidence bar;
  aggregate size 2.76% float is real but direction-ambiguous).
- **Largest block as % of float:** 0.042% (136,648 sh / 324.15M float, fz) —
  individually NOT meaningful for this name; only the day's aggregate (≈2.76%
  of float) carries information [DP:block_pct_float fz].
- **Three S/R levels for phase-9:**
  1. **65.3–66.6** — $450M institutional shelf = major overhead resistance.
  2. **61.0–61.9** — secondary shelf ($43.6M + $12.3M) = first resistance band.
  3. **54.35 / 51.57** — today's heaviest sub-60 print level and the intraday
     V-low; below 54 the 5-day institutional map is empty (thin support).
- **Open questions:** What news hit premarket to take the stock from 66 →
  60-handle in days and 60 → 51.57 today? (phase-6/7c). Did the afternoon
  block-buy lean (0.588) coincide with the option-tape's LEAP-call selling —
  i.e. delta-hedged unwinds rather than directional dip-buying? (phase-3 OI
  changes will partially answer.)
