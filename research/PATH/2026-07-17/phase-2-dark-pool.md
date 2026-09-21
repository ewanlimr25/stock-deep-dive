# Phase 2 — Dark Pool & Block Prints

**Ticker:** PATH · **As-of:** 2026-07-17 · **Version:** v1
Cites: phase-1-flow.md (open question: "is the $267M DP block confirming the slow
bullish bid?"); phase-0.5-context.md (flagged $267M / 22M-share footprint).

## Summary

Net institutional bias is **mild accumulation**. PATH's off-exchange tape on
2026-07-17 totals **~$267M / 22.0M shares / 2,226 prints** (phase-0.5), and the
tier breakdown is **buy-leaning across the board**: the large tier (the bulk —
$258M, 2,222 prints) is **65.7% buy** (13.95M buy vs 7.30M sell shares) and the
block tier (4 big trades, $9.19M) is **82.1% buy**; the mega tier is empty. Just
as important, institutions bought **into an intraday fade** — morning prints hit
$12.30–$12.36, faded to a $12.11–$12.15 close, yet the buy-ratio held above 0.55
and extended-hours buyers stepped **up** to $12.15 after the $12.11 close. The
5-day dark-pool volume builds a thick support shelf at **$11.88–$12.01** (heaviest
at $11.99/$12.00), with spot (~$12.12) sitting just above it. This directly
**confirms phase-1's slow bullish bid** (the 5-day sweep-persistence campaign) —
the options accumulation and the dark-pool accumulation point the same way. It is
mild, not aggressive: PATH is outside the top-40 of today's DP tape and there is
no mega-tier print.

## Key signals

- **Large tier 65.7% buy** — $258.0M premium, 2,222 prints, buy 13.95M vs sell
  7.30M shares → net institutional **accumulation** `[DP:block_stratified]`.
- **Block tier 82.1% buy** — 4 trades, $9.19M, buy 622.5k vs sell 135.3k sh — the
  concentrated big blocks are decisively buy-side `[DP:block_stratified]`.
- **Largest block: 357,000 sh @ $12.115 = $4.33M** at 15:33 ET, printed exactly
  at NBBO mid `[DP:largest]` — big but mid-market (not an aggressive lift).
- **Extended-hours buyers step UP to $12.15** — the two biggest post-close prints
  (135.3k + 129.9k sh, both @ $12.15) land *above* the $12.11 regular close;
  8 EH prints, all $12.11–$12.15 `[DP:extended_hours]`. Late-day conviction, not
  distribution.
- **5-day support shelf $11.88–$12.01** — top clusters $11.99 (5.63M sh/$67.5M),
  $12.00 (5.60M/$67.2M), $11.94 (5.54M/$66.1M) `[DP:price_levels]`. Spot rests on
  the shelf's upper edge.

## Detailed findings

### Largest blocks `[DP:largest]`
| Time (ET) | Size (sh) | Price | Premium | NBBO | vs mid |
|---|---|---|---|---|---|
| 15:33 | 357,000 | $12.115 | $4.33M | 12.11/12.12 | ~mid |
| 15:47 | 135,657 | $12.125 | $1.64M | 12.12/12.13 | mid |
| 16:48* | 135,292 | $12.150 | $1.64M | 12.13/12.18 | −0.005 (post-close) |
| 16:06* | 129,871 | $12.150 | $1.58M | 12.06/12.18 | **+0.03 (buy)** |
| 09:53 | 43,762 | $12.300 | $0.54M | 12.30/12.31 | mid |
| 10:20 | 38,713 | $12.360 | $0.48M | 12.36/12.37 | mid |
*post-16:00 ET = extended hours. `trade_vs_mid` on individual prints is near-zero
(all within ±½¢ of mid) — per-print NBBO classification is neutral; the directional
read comes from the **aggregate tier buy-ratios**, which are the robust signal.

### Tier breakdown `[DP:block_stratified]`
| Tier | buy_ratio | buy sh | sell sh | premium | trades |
|---|---|---|---|---|---|
| mega | — (empty) | 0 | 0 | $0 | 0 |
| block | **0.821** | 622,528 | 135,292 | $9.19M | 4 |
| large | **0.657** | 13,948,807 | 7,296,044 | $258.0M | 2,222 |
Both populated tiers clear the 0.55 accumulation threshold. No mega prints →
this is broad institutional buying, not one whale. (`sell_ratio` derived as
1 − buy_ratio: large 0.343, block 0.179.)

### Price levels (5-day clusters) `[DP:price_levels]`
Heaviest institutional volume concentrates **$11.87–$12.09**, peaking at:
$11.99 (5.63M sh), $12.00 (5.60M), $11.94 (5.54M), $11.88 (5.40M), $11.95 (5.23M).
This is a **dense demand shelf just below spot** — the clusters sit *below*
$12.12, and price is now on the shelf's top edge = institutions accumulated the
$11.9–$12.0 band and price has lifted marginally above it (accumulation heuristic:
buy-ratio ≥0.55 AND clusters near/below spot with price holding above).

### Extended-hours `[DP:extended_hours]`
8 prints, all $12.11–$12.15. The two largest (135.3k + 129.9k sh @ $12.15) are the
day's 3rd/4th biggest blocks and land **above** the $12.11 close — post-close
buyers paying up, not liquidating. No pre-market prints flagged. No overnight
catalyst to attribute to (phase-6 to confirm); reads as directional late add, not
news hedging.

## Tool calls
| Tool | Args | Result |
|---|---|---|
| dark-pool largest | --symbol PATH --sort-by premium --date 2026-07-17 | 357k @12.115 top; $16.4M in top-25 |
| dark-pool block-stratified | --symbol PATH --min-tier large --date 2026-07-17 | large 0.657 buy, block 0.821 buy |
| dark-pool extended-hours | --symbol PATH --date 2026-07-17 | 8 prints, all $12.11–12.15 |
| dark-pool price-levels | --symbol PATH --days 5 (trailing→2026-07-17) | shelf $11.88–$12.01 |
| dark-pool ticker-summary | --top-n 40 --date 2026-07-17 | PATH outside top-40 (SPY/MU/QQQ lead) |
| fz screener/quote (float) | --tickers PATH | float field absent → block_pct_float n/a |

## Tool errors
- None. `fz` float retry (screener + quote) again returned an absent `Shs Float`
  field (phase-0 truncation persists) — handled as advisory n/a, not an error.

## Verdict for downstream

- **Accumulation** (mild-to-moderate) — buy-ratios 0.66 (large) / 0.82 (block),
  EH buyers stepping up, 5-day demand shelf holding under spot.
- **Conviction: 3 / 5** — size and buy-ratio consistency are genuine and confirm
  phase-1's slow bullish bid, but PATH is outside the DP top-40, the mega tier is
  empty, and per-print `trade_vs_mid` is neutral, so this is patient accumulation,
  not an aggressive institutional lift.
- **Largest block as % of float: n/a** — `fz` float unresolved this run. Raw sizes
  (357k largest block) are modest for a large-float software name; the meaningful
  figure is the **$267M / 22M-share daily aggregate**, a genuine footprint for a
  ~$12 stock even if not float-dominant. Do not treat any single block as
  float-moving.
- **Three S/R levels for phase-9:**
  1. **Support shelf $11.88–$12.01** (5-day DP demand core; heaviest $11.99/$12.00)
     — natural stop reference sits just below, ~$11.85.
  2. **Spot / pivot ~$12.12–$12.15** (regular close $12.11, EH prints $12.15) —
     the accumulation is defending this.
  3. **Intraday supply ~$12.30–$12.36** (morning blocks faded from here) — first
     overhead resistance.
- **Open questions:** Does phase-3 OI show call walls above $12.15 that cap the
  accumulation, or open air? Is the Nov-16C OI build (phase-0.5) the LEAP buyer
  from phase-1 laddering up? Does the buy-into-the-fade pattern persist over the
  5-day window, or was 2026-07-17 a one-off (phase-5 to check)?
