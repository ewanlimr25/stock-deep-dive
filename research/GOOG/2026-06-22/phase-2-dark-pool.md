# Phase 2 — Dark Pool & Block Prints

**Ticker:** GOOG
**As-of date:** 2026-06-22
**Generated:** 2026-06-22
**Upstream phases cited:** phase-0-intake.md (Shs Float 5.07B), phase-0.5-context.md, phase-1-flow.md

## Summary

Dark pool reads **mega-tier accumulation** today: the largest institutional blocks
(`mega` tier) printed a **buy_ratio of 0.764** ($274.2M, 14 trades) — high-confidence
buying (>0.70) — corroborated by a **buy-leaning trade-vs-mid on the biggest prints**
(top block +$1.13 vs mid). This **confirms phase-1's reframe**: under the
artifact-driven net-bearish *premium*, real institutional posture leans constructive
(mega blocks buying + call-heavy tape). Two qualifiers temper it: (1) the `block` and
`large` tiers are essentially **balanced** (0.552 / 0.525), so the accumulation is
concentrated in the very largest, fewest prints, not broad; and (2) the heaviest
**5-day price-level clusters sit at $362–371 — $13–22 ABOVE the $348.78 spot** — i.e.
GOOG has **pulled back ~5%** into today's level, leaving that zone as **overhead
supply/resistance** while today's mega blocks accumulate lower. Size is **float-trivial**
(total day's DP = 0.12% of the 5.07B float), so the signal is the **ratio and tier, not
magnitude** — GOOG ranks only **19/30** by DP premium. Net: **accumulation, conviction 3**.

## Key signals

- **Mega-tier buy_ratio 0.764** (buy_vol 600,669 vs sell 185,626; $274.2M; 14 trades)
  — high-confidence accumulation `[DP:block_stratified]`
- Largest block **239,933 sh / $83.7M @ $348.78, vs_mid +1.13 (buy lean)**, post-market
  18:01 ET `[DP:largest]`
- `block`/`large` tiers near-balanced — **0.552 / 0.525** — accumulation is narrow,
  not broad `[DP:block_stratified]`
- 5-day clusters **above spot**: $367.46 ($1.57B, n=161), $371.10, $362.10 — **overhead
  supply**; at-spot cluster $348.78 ($314M, n=86) `[DP:price_levels]`
- GOOG **rank 19/30** by DP premium ($2.055B, 5.91M sh) — mega-cap-normal; total DP =
  **0.12% of float** `[DP:ticker_summary]` `[DP:block_pct_float fz]`

## Detailed findings

### Largest blocks (buy/sell via trade_vs_mid) `[DP:largest]`

| Time (UTC) | Size | Premium | Price | vs_mid | %float | Lean |
|-----------|------|---------|-------|--------|--------|------|
| 22:01:03 | 239,933 | $83.68M | 348.78 | **+1.13** | 0.0047% | buy |
| 20:00:18 | 65,000 | $22.67M | 348.78 | +0.21 | 0.0013% | buy |
| 20:00:00 | 60,384 | $21.06M | 348.78 | −0.19 | 0.0012% | sell |
| 20:04:00 | 49,063 | $17.11M | 348.78 | −0.06 | 0.0010% | ~flat |
| 20:03:50 | 49,040 | $17.10M | 348.78 | +0.01 | 0.0010% | ~flat |
| 19:38:44 | 41,179 | $14.33M | 348.10 | −0.02 | 0.0008% | ~flat |
| 20:00:28 | 40,623 | $14.17M | 348.78 | +0.24 | 0.0008% | buy |
| 14:28:21 | 40,450 | $14.08M | 348.03 | +0.01 | 0.0008% | ~flat |

Most large prints cluster at the **20:00Z close auction** and the **22:01Z post-market**,
nearly all at the $348.78 closing print; the biggest (+1.13) and the majority of the
20:00 prints lean **buy** (+0.21/+0.24), a couple sell (−0.19). Sum of top-25 returned ≈
**$350.7M**. Net lean: **buy**, consistent with the mega-tier ratio.

### Tier breakdown (buy/sell per tier) `[DP:block_stratified]`

| Tier | buy_ratio | derived sell | buy_vol | sell_vol | total_prem | trades |
|------|-----------|--------------|---------|----------|-----------|--------|
| **mega** | **0.764** | 0.236 | 600,669 | 185,626 | $274.2M | 14 |
| block | 0.552 | 0.448 | 689,928 | 559,244 | $434.1M | 214 |
| large | 0.525 | 0.475 | 2,033,736 | 1,843,603 | $1,346.98M | 6,145 |
| retail | 0.500 | — | 0 | 0 | $0 | 0 |
| **all tiers** | — | — | — | — | **$2,055.27M** | — |
| highest_tier | mega | | | | | |

The **conviction is in the mega tier** (0.764, high-confidence). Block (0.552) is mildly
buy, large (0.525) is balanced — so this is *narrow* accumulation by the very biggest
prints, not a broad institutional bid. `sell_ratio` derived as `1 − buy_ratio` (no
`sell_ratio` field).

### Price levels (institutional S/R, 5-day) `[DP:price_levels]`

| Level | Premium | n | vs spot $348.78 |
|-------|---------|---|------------------|
| **367.46** | **$1,574M** | 161 | +5.4% (overhead) |
| 367.11 | $616M | 109 | +5.3% (overhead) |
| 362.10 | $363M | 90 | +3.8% (overhead) |
| 371.10 | $323M | 95 | +6.4% (overhead) |
| **348.78** | **$314M** | 86 | at spot (today) |
| 370.69 | $280M | 12 | +6.3% (overhead) |
| 348.03 / 348.10 | $17.5M / $16.6M | 11 / 11 | just below |

**Key structural read:** the dominant 5-day dark-pool transaction zone is **$362–371**,
now **$13–22 ABOVE spot** — GOOG has fallen back through it. That zone is **overhead
supply/resistance** (heaviest at **$367.46**). Today's at-spot cluster ($348.78, $314M)
is where the mega-tier accumulation is occurring. *(`--days 5` anchors to the latest
available date 2026-06-22, aligned with as-of; cross-checked vs phase-0 dates.)*

### Extended-hours activity `[DP:extended_hours]`

15 prints; the standouts are the **close-auction (20:00Z / 16:00 ET) and one
post-market (22:01Z / 18:01 ET 239,933-share $83.7M)** block — both at the $348.78
close. This is **closing-cross + late block** mechanics (MOC-related), buy-leaning, not
an overnight catalyst move (no extended-hours print away from the close price). Phase-6
should confirm no GOOG-specific overnight news; absent that, treat as positioning, not
news.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← path | Rows |
|------------------|--------------------|------|
| `uw dark-pool block-stratified --symbol GOOG --top-n 30 --min-tier large --date 2026-06-22 --json` | mega.buy_ratio=0.764, large.buy_ratio=0.525 ← `.results[0].mega.buy_ratio` | 1 |
| `uw dark-pool largest --symbol GOOG --top-n 25 --sort-by premium --date 2026-06-22 --json` | top block 239,933sh $83.68M vs_mid +1.13 ← `.results[0]` | 25 |
| `uw dark-pool price-levels --symbol GOOG --top-n 15 --days 5 --json` | $367.46 $1.57B (n=161) ← `.results[0].price_level` | 15 |
| `uw dark-pool extended-hours --symbol GOOG --top-n 15 --date 2026-06-22 --json` | 22:01Z 239,933sh $83.7M ← `.results[0]` | 15 |
| `uw dark-pool ticker-summary --top-n 30 --date 2026-06-22 --json` | GOOG rank 19/30, total $2.055B, 5.91M sh ← `select(.ticker=="GOOG")` | 30 |
| (float) phase-0 `fz` Shs Float = 5.07B | total DP 5.91M / 5.07B = 0.12% float | — |

## Tool errors

None. All five reads round-tripped through `jq`.

## DATA NOTE / CORRECTION

No mis-read. Interpretive note: the `price-levels --days 5` window spans sessions when
GOOG traded $362–371; those clusters are **historical transaction levels now overhead**,
not current bids. Verified the price pullback context belongs to phase-5 (historical) to
confirm the path; flagged here as resistance.

## Verdict for downstream phases

- **Bias from this phase:** **Accumulation (narrow, mega-tier).** Confirms phase-1 that
  the net-bearish *premium* was an artifact — institutional posture leans **constructive**.
- **Conviction:** **3 / 5.** Mega buy_ratio 0.764 is high-confidence, and the largest
  blocks lean buy — but it's only 14 trades / $274M, the broader block/large tiers are
  balanced, size is float-trivial (0.12% float), and GOOG is a mid-pack DP name (19/30).
- **Largest block as % of float:** 239,933 sh = **0.0047% of the 5.07B float** —
  *not* meaningful as size for this mega-cap; the signal is the **buy ratio**, not the
  block. (advisory, `[DP:block_pct_float fz]`)
- **Three S/R levels for phase-9:**
  1. **Resistance $367.46** (dominant 5-day cluster $1.57B; broader supply band
     **$362–371**, heaviest overhead).
  2. **Pivot/support $348.78** (today's close + at-spot accumulation cluster $314M;
     where mega blocks are buying).
  3. **Near support $348.0–348.1** (secondary clusters just below) → below it, the air
     pocket down toward prior-range support to be defined in phase-5.
- **Open questions:** Did GOOG genuinely sell off from $367 to $348.78 over the 5-day
  window (phase-5 to confirm the path and whether $362–371 was distribution or trapped
  longs)? Does OI (phase-3) show fresh call OI building at the 6/26 345–355 strikes to
  pair with today's call-heavy tape? Is the mega-tier bid a standalone accumulator or
  index/ETF-creation mechanics (no retail-tier prints argues against pure rebalancing)?
