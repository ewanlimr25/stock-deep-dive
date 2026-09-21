# Phase 2 — Dark Pool & Block Prints

**Ticker:** GOOG · **As-of:** 2026-07-23 · **Spot:** $318.34
**Generated:** 2026-07-24T01:18:35Z
**Upstream:** phase-1-flow.md (net bearish −$49.4M, top-25 prints 100% puts, deep-ITM
put deltas −0.84 to −0.96; open Q: "is dark pool confirming distribution?")

## Summary

Today's dark-pool tier ratios are **balanced, not distributive**: mega-tier
buy_ratio 0.522, large-tier 0.542, block-tier 0.497 — none crosses the 0.55
accumulation / 0.45 distribution lines. Total DP premium $3.07B (7,163 trades,
avg $319.49), GOOG ranked #10 of 30 names today — heavy but baseline for the
name. The **signal is in the price structure, not the buy/sell split**: the 5-day
DP volume is stacked *above* spot — $1.14B at $341.91, $797M at $346.19, $488M at
$346.12, $201M at $351.37 — meaning GOOG has **fallen ~8–9% from the low-$340s/
$350s into $318.34**, and that overhead volume is now trapped supply / resistance.
So dark pool does not *confirm* today's put-buying with active selling, but the
tape structure (a name that just broke down, overhead supply, thin support) is
fully consistent with phase-1's bearish premium skew.

## Key signals

- **Tier ratios balanced:** mega buy_ratio **0.522** (buy 1.78M / sell 1.63M sh,
  $1.12B), large **0.542**, block **0.497**. No accumulation, no distribution.
  `[DP:block_stratified]`
- **Overhead supply cluster:** 5-day DP volume peaks at **$341.91 ($1.14B)** and
  **$346.19 ($797M)**, both ~7–9% ABOVE spot — GOOG recently traded there and
  fell. `[DP:price_levels]`
- **Largest single print $500M** — 1,570,648 sh at the $318.34 close (20:49 ET
  closing cross), trade_vs_mid −0.735 (slight sell-lean). A benchmark/cross, not
  clean directional intent. `[DP:largest]`
- **$3.07B total DP premium, rank #10/30** — engaged but not an outlier day for a
  mega-cap. `[DP:ticker_summary]`
- **Anomalous $341.91 prints today** (7× ~$50M at 11:55 UTC, NBBO $325.7, tvm
  +16) — a fixed-reference/basis-program artifact, not spot-level buying; excluded
  from the directional read but consistent with the overhead $341.91 shelf. `[DP:largest]`

## Detailed findings

### Largest blocks (top, near-spot genuine prints) — `[DP:largest]`
| Price | Size | $Prem | trade_vs_mid | Time (ET) | Note |
|---|---|---|---|---|---|
| 318.34 | 1,570,648 | $500.0M | −0.735 | 20:49 | closing cross, slight sell |
| 318.34 | 191,750 | $61.0M | +0.07 | 20:00 | post-close, ~mid |
| 318.34 | 87,277 | $27.8M | +0.07 | 20:00 | post-close, ~mid |
| 341.91 | 146,236 ×7 | ~$50M ea | +16.1 | 11:55 | above-NBBO artifact/basis |

Premium-weighted buy-vs-sell over top-25: buy $602M vs sell $542M — marginal buy
lean, driven partly by the $341.91 artifact prints; strip those and the genuine
near-spot flow is ~balanced with the biggest print (the $500M cross) sell-leaning.

### Tier breakdown — `[DP:block_stratified]`
| Tier | buy_ratio | derived sell_ratio | total_premium | trades |
|---|---|---|---|---|
| mega | 0.522 | 0.478 | $1,115M | 21 |
| large | 0.542 | 0.458 | $1,557M | 6,919 |
| block | 0.497 | 0.503 | $402M | 223 |
All within the neutral 0.45–0.55 band → **BALANCED**.

### Price levels (5-day clusters; spot $318.34) — `[DP:price_levels]`
| Level | $Prem (5d) | Shares | vs spot |
|---|---|---|---|
| 341.91 | $1,135.7M | 3.32M | **+7.4% (resistance)** |
| 346.19 | $796.6M | 2.30M | **+8.7% (resistance)** |
| 318.34 | $720.1M | 2.26M | **at spot (pivot)** |
| 346.12 | $488.3M | 1.41M | +8.7% |
| 351.37 | $201.4M | 0.57M | +10.4% |
| 344.87 | $93.4M | 0.27M | +8.3% |
| 317.91 | $19.4M | 0.06M | −0.1% (thin near support) |
Overhead $341–351 shelf dwarfs anything below spot → recent breakdown, trapped
supply above, **thin visible support below 318**.

### Extended-hours activity — `[DP:extended_hours]`
The three biggest prints are extended-hours: the $500M close cross (20:49 ET) and
$61M + $27.8M post-close (20:00 ET) at 318.34, plus the pre-market 341.91 artifact
cluster (11:55 UTC). Post-close crosses at the closing price are benchmark/rebal
flow — de-rate as directional intent.

## Tool calls
| Tool | Args | Rows | jq path |
|---|---|---|---|
| dark-pool largest | --symbol GOOG --top-n 25 --sort-by premium | 25 | `.results[].{price,size,premium,trade_vs_mid,executed_at,nbbo_*}` |
| dark-pool block-stratified | --symbol GOOG --top-n 30 --min-tier large | 1 | `.results[0].{mega,large,block}.buy_ratio` |
| dark-pool price-levels | --symbol GOOG --top-n 15 --days 5 | 15 | `.results[].{price_level,total_premium,total_shares,trade_count}` |
| dark-pool ticker-summary | --top-n 30 | 30 | `.results[]│select(.ticker=="GOOG")` (rank 10) |
| dark-pool extended-hours | --symbol GOOG --top-n 15 | 15 | `.results[].{price,size,premium,executed_at}` |

## Tool errors
<none — all five parsed clean>

## Verdict for downstream

- **Net institutional bias: BALANCED / MIXED** (mega 0.522, large 0.542 — a whisper
  of buy-lean, nothing that qualifies as accumulation or distribution). Dark pool
  does **not** actively confirm today's bearish option premium, but neither does it
  contradict it — the structure (post-breakdown, overhead supply) is bearish-context.
- **Conviction: 2 / 5** on the buy/sell signal (genuinely balanced), but the
  price-level map is high-value for the trade plan.
- **Largest block as % of float:** GOOG Class-C float ≈ 5.8B sh (fz snapshot n/a;
  approximate) — the $500M / 1.57M-sh block is ≈0.03% of float. **Not meaningful
  for this name**; mega-block size carries no conviction here (pitfall: mega-caps
  print blocks all day). `[DP:block_pct_float]` (advisory only, no fz float).
- **Three S/R levels for phase-9:**
  1. **Resistance $341–346** — dominant 5-day DP supply ($1.9B combined), trapped
     longs from the pre-drop; a rally into here should sell.
  2. **Pivot / spot $318.34** — today's $720M cluster, the current battleground.
  3. **Support thin below $318** — next visible DP shelf ≈$317.9; a break opens air
     toward the phase-1 put strikes (300 LEAP put, 315 zone).
- **Open questions:**
  - Was the overhead $341–351 shelf distribution into the drop, or accumulation
    now trapped? → phase-3 OI change, phase-5 historical price confirms the fall.
  - What drove the ~8–9% breakdown into $318? → phase-6 macro/news (earnings are
    2026-11-04, so not earnings — a sector or single-name catalyst).
