# Phase 2 — Dark Pool & Block Prints

**Ticker:** ENVX
**As-of date:** 2026-06-26
**Generated:** 2026-06-27T14:47:39Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md

## Summary

Dark pool is **mildly accumulative but small and balanced — a weak confirm, not a
green light.** Large-tier `buy_ratio` is 0.629 (suggestive only, below the 0.70
high-confidence bar), on $3.36M total premium across just 16 "large"-tier prints —
**no mega/block-tier whale prints at all.** Sizing is negligible for this name: the
biggest block (106,747 sh, $635K) is **0.057% of the 188.93M float** (2.5% of ADV),
and the entire large-tier print set is 0.30% of float. The heaviest 5-day institutional
cluster sits **right at $5.95 = spot ($2.89M)** — a value-area battleground, not a
launch pad — with **overhead supply at $6.28–6.33 and $7.05** that directly threatens
the phase-1 $6-call thesis's upside. A morning print at $6.04 (buy-lean) shows some
willingness to pay above $6, but it's isolated. Net: dark pool **weakly supports** the
bullish flow at/near spot while **flagging resistance just above the $6 strike.**

## Key signals

- Large-tier **`buy_ratio 0.629`** (buy 355,098 / sell 209,478 sh), $3,359,349 premium,
  16 prints, `highest_tier "large"` — **no mega tier** `[DP:block_stratified]`.
- 5-day price-level clusters: **$5.95 $2.89M (= spot)**, then $6.33 $843K, $5.94 $781K,
  $6.28 $699K, $7.05 $619K `[DP:price_levels]` — value area at spot, supply above.
- Biggest block **106,747 sh @ $5.9499 = 0.057% of float** (buy-lean), at the 20:00 UTC
  close cross `[DP:largest]` — `[DP:block_pct_float fz]` advisory: **immaterial size**.
- ENVX **outside the dark-pool ticker-summary top-30** `[DP:ticker_summary]` — its
  $3.36M DP premium is not among the day's market-wide leaders (small-name consistent
  with phase-0.5 "outside top-50 by $").
- Extended-hours: one true post-market block (86,183 sh @ $5.95, 21:45 UTC); the rest
  are 20:00 UTC closing-auction prints, **not directional pre-positioning** `[DP:extended_hours]`.

## Detailed findings

### Largest blocks (buy/sell via price vs NBBO mid) — `[DP:largest]`

| Time (UTC) | Price | Size | Premium | % float | Lean |
|------------|-------|------|---------|---------|------|
| 20:00:08 | $5.9499 | 106,747 | $635,133 | 0.057% | BUY |
| 21:45:58 | $5.95 | 86,183 | $512,788 | 0.046% | MID |
| 13:59:42 | **$6.04** | 42,208 | $254,936 | 0.022% | **BUY (above spot)** |
| 20:13:14 | $5.95 | 37,152 | $221,054 | 0.020% | SELL |
| 20:26:11 | $5.95 | 35,020 | $208,369 | 0.019% | SELL |
| 16:11:38 | $5.85 | 18,668+17,444 | $211,254 | 0.019% | SELL |

Aggregate lean (price vs `nbbo_mid`): 7 buy prints $1.60M, 1 mid $0.51M, 8 sell prints
$1.24M — a mild buy tilt, consistent with the 0.629 volume buy_ratio. The buying clusters
at/around the close ($5.95) and the one morning $6.04 print; the selling is spread at
$5.95–5.975 and the $5.85 lows.

### Tier breakdown — `[DP:block_stratified]`

| Tier | buy_ratio | buy_vol | sell_vol | premium | trades |
|------|-----------|---------|----------|---------|--------|
| **large** | **0.629** | 355,098 | 209,478 | $3,359,349 | 16 |
| mega | — | 0 | 0 | 0 | 0 |
| block | — | 0 | 0 | 0 | 0 |
| retail | — | 0 | 0 | 0 | 0 |

`highest_tier = "large"`. **No mega/block prints** — there is no whale-conviction footprint,
just upper-mid institutional flow. `sell_ratio = 1 − 0.629 = 0.371`. By the rubric, 0.629
is **"suggestive accumulation only"** (high-confidence needs ≥ 0.70).

### Price levels (5-day clusters, gap-aware) — `[DP:price_levels]`

Heaviest → lightest: **$5.95 $2.89M (spot)**, $6.33 $843K, $5.94 $781K, $6.28 $699K,
$7.05 $619K, $6.05 $604K, $6.12 $578K, $6.11 $463K, $6.01 $281K, $6.04 $255K, $5.85 $211K.

Interpretation: the dominant value area is **$5.95** (current price). The clusters **above
spot ($6.28–6.33, $7.05)** are where ENVX traded earlier in the 5-day window *before* its
−20% slide — i.e. **overhead supply / trapped longs, not fresh paying-up.** $5.85 below is
light. Caveat: `--days 5` anchors to the latest date and spans the gap-free 06-22→06-26
window (phase-0), so these clusters are recent.

### Extended-hours — `[DP:extended_hours]`

13 prints, but 12 are at the 20:00 UTC (16:00 ET) **closing auction**; only the 21:45 UTC
86,183-sh @ $5.95 block is genuine post-market. No unusual overnight directional
positioning — treat as auction/rebalance mechanics, conviction-neutral.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|------------------|--------------------------|-----------|
| `uw dark-pool largest --symbol ENVX --top-n 25 --sort-by premium --date 2026-06-26` | biggest 106,747 sh $635K buy-lean ← `.results\|sort_by(-.premium)[0]`; lean ← `.price>.nbbo_mid` | 16 |
| `uw dark-pool block-stratified --symbol ENVX --top-n 30 --min-tier large --date 2026-06-26` | large buy_ratio 0.629 ← `.results[0].large.buy_ratio`; mega empty ← `.results[0].mega` | 1 |
| `uw dark-pool price-levels --symbol ENVX --top-n 15 --days 5` | $5.95 cluster $2.89M ← `.results\|sort_by(-.total_premium)` | 15 |
| `uw dark-pool extended-hours --symbol ENVX --top-n 15 --date 2026-06-26` | post-mkt 86,183@$5.95 ← `.results[]` | 13 |
| `uw dark-pool ticker-summary --top-n 30 --date 2026-06-26` | ENVX absent ← `select(.ticker=="ENVX")` empty | 0 (of 30) |

## Tool errors

<none — all reads round-tripped through jq>

## DATA NOTE / CORRECTION

<none — first reads stood>

## Verdict for downstream phases

- **Institutional bias:** **Mixed → mildly accumulative.** Buy_ratio 0.629 and a morning
  $6.04 buy print lean bullish; the absence of mega blocks, near-even buy/sell, and small
  size keep it weak. **Conviction 2/5.**
- **Largest block as % of float:** 0.057% (106,747 / 188.93M) — **immaterial for this name;**
  even the full large-tier set is 0.30% of float. Dark pool size adds *no* conviction here;
  the read is purely directional-lean, and that lean is only mild. `[DP:block_pct_float fz]`
- **Three S/R levels for phase-9:**
  1. **$5.95** — primary value area / heaviest 5d DP cluster ($2.89M) = the pivot/decision line.
  2. **$5.85** — minor support (today's low prints, light cluster).
  3. **$6.28–6.33** — first overhead supply cluster ($1.54M combined) = **resistance directly
     above the $6 call strike;** $7.05 is secondary resistance.
- **Open questions:** Does the $6 OI wall (phase-3) coincide with the $6.28–6.33 DP supply to
  create a hard ceiling? Is the mild buy lean genuine accumulation or short-seller covering at
  the value area (26% short float, phase-7c)? The dark pool does NOT independently confirm the
  phase-1 $6-call thesis — it's a weak tailwind with a supply headwind just above.
