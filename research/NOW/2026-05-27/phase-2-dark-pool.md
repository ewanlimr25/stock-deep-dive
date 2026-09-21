# Phase 2 — Dark Pool & Block Prints

**Ticker:** NOW
**As-of date:** 2026-05-27
**Generated:** 2026-05-28T12:24:00Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md, phase-1-flow.md

## Summary

The dark pool is **MIXED, leaning balanced-to-soft — it does NOT confirm phase-1's
bullish options flow.** The headline "mega tier 100% sell ($135.9M)" is an
**after-hours artifact**: both mega blocks (1.07M sh / $108.8M and 265k sh /
$27.1M) printed at **20:00–20:15 at exactly $102.12, the official close, below the
NBBO bid** — the classic signature of a closing-cross / index-rebalance /
VWAP-referenced cross, not aggressive intraday distribution. Stripping those, the
intraday **large tier ($408M, 2,076 trades) is balanced (buy_ratio 0.492)** and
the block tier is mildly sell-tilted (0.326). There is **no accumulation footprint
under the call buying** — a yellow-flag divergence vs phase-1. In float terms even
the biggest block is only **0.10% of NOW's 1.02B float** — modest, not
needle-moving. `[DP:block_pct_float fz]`

## Key signals

- Mega tier (≥$10M): **buy_ratio 0.0** (2 blocks, $135.9M) — **but both are 20:00–20:15 closing-price prints → rebalance artifact, de-rated** `[DP:block_stratified]`
- Large tier (≥$100k, $408M, 2,076 trades): **buy_ratio 0.492 — balanced** (the real intraday read) `[DP:block_stratified]`
- Block tier (≥$1M, $51.7M, 34 trades): buy_ratio 0.326 — mildly sell-tilted intraday `[DP:block_stratified]`
- 5-day S/R: heavy supply at **$103.30 ($138M)**, support shelf **$101.0–$101.7**, major support **$99.69 ($79.6M)** `[DP:price_levels]`
- NOW **not in DP ticker-summary top-40** (MU $17.2bn, NVDA $10.8bn lead) — modest absolute DP day, consistent with phase-0.5 "no volume event" `[DP:ticker_summary]`

## Detailed findings

### Largest blocks `[DP:largest]`

| time (ET) | price | size (sh) | premium | NBBO | read |
|-----------|-------|-----------|---------|------|------|
| 20:15:05 | 102.12 | 1,065,605 | **$108.82M** | bid103.0/ask103.5 | AH, below bid — rebalance/cross |
| 20:00:36 | 102.12 | 265,500 | $27.11M | bid102.0/ask102.26 | AH at close — rebalance/cross |
| 20:45:26 | 102.12 | 50,500 | $5.16M | bid103.83/ask104.0 | AH at close |
| 21:06:38 | 102.12 | 43,288 | $4.42M | bid105.12/ask105.4 | AH at close |
| 18:02:08 | 102.49 | 21,800 | $2.23M | bid102.48/ask102.5 | intraday, at-ask |
| 14:38:34 | 105.00 | 20,500 | $2.15M | bid105.0/ask105.06 | intraday, at-bid |
| 13:10:34 | 98.81 | 21,660 | $2.14M | bid98.75/ask98.89 | intraday |

The top-4 prints are all after-hours at the $102.12 close (confirmed by
`extended-hours` below). The 1.07M-sh block = **0.10% of the 1.02B float**
`[DP:block_pct_float fz]` — large in dollars, immaterial in float terms.

### Tier breakdown `[DP:block_stratified]`

| tier | trades | buy_ratio | premium | shares (buy/sell) |
|------|--------|-----------|---------|-------------------|
| mega (≥$10M) | 2 | **0.000** | $135.9M | 0 / 1,331,105 |
| block (≥$1M) | 34 | 0.326 | $51.7M | 164k / 339k |
| large (≥$100k) | 2,076 | **0.492** | $408.0M | 1.95M / 2.01M |
| **all tiers** | — | — | **$595.6M** | — |

The $408M large tier is the bulk of the day and is **balanced**. Per the rubric,
mega buy_ratio 0.0 would be "high-confidence sell" — but the after-hours timing +
exact-close pricing flags it as mechanical, so it is de-rated to *not* a directional
distribution signal.

### Extended-hours `[DP:extended_hours]`

The five largest blocks ALL appear here, timestamped 20:00–21:11 at $102.12 /
$103.79 / $105.00 / $106.29. **This confirms the mega/largest prints are
after-hours, not intraday.** Per the phase pitfall ("extended-hours prints can be
index rebalancing… flag and de-rate") these are treated as rebalance/cross flow,
**not** directional intent. Phase-6 should check for a 2026-05-27 index/rebalance
event.

### Price levels (5-day institutional S/R) `[DP:price_levels]`

| price | premium | shares | role vs spot $102.12 |
|-------|---------|--------|----------------------|
| **103.30** | $138.3M | 1.34M | **overhead supply** (must clear to run) |
| 102.12 | $165.8M | 1.62M | at-spot pivot (rebalance-inflated) |
| 102.13 | $36.5M | 357k | at-spot |
| 101.0–101.7 | ~$10–13M each (6 levels) | — | **thick near-spot support shelf** |
| 100.00 | $9.1M | 91k | round-number support |
| **99.69** | $79.6M | 798k | **major support** below |
| 98.84 | $9.5M | 96k | secondary support |

Spot sits on its heaviest cluster ($102.12); the next real hurdle up is the
**$103.30 supply shelf**, and the floor is the **$101 band → $99.69**.

## Tool calls (audit trail)

| Command | Result summary |
|---------|----------------|
| `uw dark-pool largest --symbol NOW --sort-by premium` | top 4 are AH $102.12 closing prints |
| `uw dark-pool block-stratified --symbol NOW --min-tier large` | mega 0.0 buy / large 0.492 / block 0.326 |
| `uw dark-pool extended-hours --symbol NOW` | confirms 5 largest are 20:00–21:11 ET |
| `uw dark-pool price-levels --symbol NOW --days 5` | supply $103.30, support $101 band → $99.69 |
| `uw dark-pool ticker-summary --top-n 40` | NOW not in top-40 (MU/NVDA/SPY lead) |

## Tool errors

None.

## Verdict for downstream

- **Bias:** **MIXED / no-accumulation** (balanced large tier; soft-sell block tier;
  mega "sell" is a rebalance artifact). **Dark pool does NOT corroborate the
  bullish options flow** — divergence flag for phase-10.
- **Conviction:** **2/5** — weak signal, muddied by after-hours rebalance flow and
  a modest absolute DP day (NOW outside ticker-summary top-40).
- **Largest block as % of float:** **0.10%** (1.07M sh / 1.02B). Advisory: even the
  biggest print is immaterial to float — do not read it as a conviction
  accumulation/distribution event. `[DP:block_pct_float fz]`
- **Three S/R levels for phase-9:**
  1. **Support:** $101.0–$101.7 shelf (near-spot) → **$99.69 major support** (stop reference below ~$99.5).
  2. **Pivot:** $102.12 (spot, heaviest cluster — rebalance-inflated).
  3. **Resistance:** **$103.30 ($138M supply)** — must clear before the $105–110 call strikes (phase-1) can pay.
- **Open questions:**
  1. Were the 20:00–20:15 mega blocks an **index/MSCI rebalance** on 2026-05-27 (phase-6 to confirm)? If yes, fully discount them.
  2. Do the $90/$100 put strikes (phase-1's big blocks) show **growing OI with matching stock** (= collar against a long) in phase-3? That would reconcile bullish calls + soft DP + big puts as one hedged institutional structure.
