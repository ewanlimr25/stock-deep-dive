# Phase 2 — Dark Pool & Block Prints

**Ticker:** PATH · **As-of:** 2026-07-22 · **Underlying:** $10.53 · **Generated:** 2026-07-22
**Upstream:** phase-1-flow.md (net-bearish aggregate + 5-day bullish sweep campaign; near-term catalyst ~7/24), phase-0.5-context.md `[CTX:]` (total-prem 95th pctile)

## Summary

Dark-pool bias today is **mixed, tilting balanced-to-mildly-distributive**, wrapped
in a **bearish 5-day structure**. The broad large-tier tape is 57.2% buy ($110.4M,
960 trades — *suggestive* accumulation, not high-confidence), and a $9.13M block was
lifted **above the ask** at $10.88 (real paying-up). But the single largest print of
the day is a **1.5M-share, $16.06M SELL at $10.71** (below mid, mega tier 100% sell),
and — the biggest structural tell — the **5-day price-level clusters sit entirely at
$11.90–$12.50** (heaviest $11.94–11.99, ~$550M) while spot is **$10.53**. PATH has
fallen **~12% out of the week's institutional volume zone**, which now stands as
**overhead supply**. Net: institutions are transacting two-sided at $10.70–10.88 with
the seller marginally larger, beneath a wall of recently-printed stock at $12.

## Key signals

- **5-day DP volume clustered $11.90–$12.50, none near spot $10.53** — the $11.94–11.99 band alone is ~$550M / ~4,900 prints; now overhead supply after a ~12% weekly slide `[DP:price_levels]`.
- **Largest single print = 1.5M sh SELL, $16.06M @ $10.71** (trade_vs_mid −0.005, mega tier buy_ratio 0.0 → 100% sell) `[DP:largest]` `[DP:block_stratified]`.
- **$9.13M block BOUGHT above the ask @ $10.88** (840k sh, trade_vs_mid +0.025, block tier buy_ratio 1.0) — genuine institutional paying-up, offsetting most of the mega sell `[DP:largest]`.
- **Broad large-tier 57.2% buy** ($110.4M, 960 trades) — mild accumulation on the wide tape, but inside the 0.55–0.70 "suggestive-only" band `[DP:block_stratified]`.
- **Modest after-hours accumulation** — 118,805 sh bought @ $10.70 (+0.07 vs mid) plus small 10k lots at $10.60–10.73 `[DP:extended_hours]`.
- **PATH outside dark-pool ticker-summary top-30** — not an absolute top DP name, but the $16M+$9M prints are meaningful *for this $5.5B name* `[DP:ticker_summary]`.

## Detailed findings

### Largest blocks `[DP:largest]`

| time (Z) | price | size | premium | NBBO | trade_vs_mid | read |
|---|---|---|---|---|---|---|
| 15:00 | $10.7102 | 1,500,000 | **$16.06M** | 10.71–10.72 | −0.005 | **SELL** (mega) |
| 14:34 | $10.88 | 840,000 | $9.13M | 10.85–10.86 | +0.025 | **BUY** (above ask) |
| 21:16 (AH) | $10.70 | 118,805 | $1.27M | 10.60–10.66 | +0.070 | BUY (AH) |
| 15:27 | $10.725 | 87,598 | $0.93M | 10.72–10.73 | ~0 | neutral |
| 15:02 | $10.751 | 72,600 | $0.78M | 10.74–10.75 | +0.006 | slight buy |
| 15:10 | $10.685 | 61,873 | $0.66M | 10.69–10.70 | −0.010 | slight sell |
| 14:31 | $10.8601 | 56,480 | $0.61M | 10.86–10.87 | −0.005 | neutral |
| 23:52 (AH) | $10.63 | 49,674 | $0.52M | 10.60–10.67 | −0.005 | neutral |

**% of float (advisory, `[DP:block_pct_float]`):** exact float **n/a** (fz float field
absent this run — phase-0). Against ~526M shares outstanding (mktcap $5.54B ÷ $10.53),
the 1.5M-share mega block ≈ **0.28% of shares out** — a moderate, not dominant,
single print for a name this size. Exact %-of-float deferred to phase-7c WebSearch.

### Tier breakdown `[DP:block_stratified]`

| tier | buy_ratio | derived sell_ratio | buy vol | sell vol | premium | trades |
|---|---|---|---|---|---|---|
| mega | 0.00 | **1.00** | 0 | 1,500,000 | $16.07M | 1 |
| block | 1.00 | 0.00 | 958,805 | 0 | $10.41M | 2 |
| large | 0.572 | 0.428 | 5,912,981 | 4,421,028 | $110.45M | 960 |
| retail | — | — | 0 | 0 | $0 | 0 |
| **all tiers** | | | | | **$136.92M** | |

The extremes offset: the one mega print is all-sell; the two block prints are all-buy
(the $9.13M above-ask lift + the AH $1.27M buy). The mass of volume (large tier) is a
mild 57.2% buy. No `sell_ratio` field — derived as 1 − buy_ratio per skill rule.

### Price levels — 5-day clusters `[DP:price_levels]`

Every returned cluster is **above spot $10.53**; none near current price:

| price level | premium | prints |
|---|---|---|
| $11.95 | $111.34M | 1,000 |
| $11.94 | $107.36M | 974 |
| $11.97 | $86.38M | 778 |
| $11.96 | $84.46M | 764 |
| $11.99 | $84.25M | 755 |
| $11.98 | $82.52M | 734 |
| $12.48 | $81.33M | 709 |
| $11.93 | $75.00M | 685 |
| $12.49 | $68.61M | 596 |
| $12.47 | $66.02M | 573 |
| $12.00 | $63.55M | 561 |

Window anchors to latest date (2026-07-22) back 5 sessions; cross-checked against
phase-0 available dates (2026-07-16→07-22, contiguous — no gap distortion). Read:
the institutional volume-weighted zone for the week is **$11.90–$12.50**; spot at
$10.53 is **below it**, so those levels are **overhead resistance / trapped supply**,
and the stock is structurally weak (trading beneath where big money transacted).

### Extended-hours activity `[DP:extended_hours]`

Net **modest accumulation** post-close: 118,805 sh @ $10.70 (+0.07 vs mid, largest AH
print), then smaller 10–16k lots at $10.60–$10.73. No single AH block large enough to
signal a news-driven move; consistent with routine post-close positioning around
$10.6–10.7. Watch phase-6 for any 7/22 after-hours headline.

## Tool calls (audit)

| Datapoint | Command | jq path |
|---|---|---|
| largest blocks | `uw dark-pool largest --symbol PATH --top-n 25 --sort-by premium --date 2026-07-22 --json` | `.results[].{price,size,premium,nbbo_bid,nbbo_ask,trade_vs_mid}` |
| tiers | `uw dark-pool block-stratified --symbol PATH --top-n 30 --min-tier large --date 2026-07-22 --json` | `.results[0].{mega,block,large}.buy_ratio/buy_volume/sell_volume/total_premium` |
| ext hours | `uw dark-pool extended-hours --symbol PATH --top-n 15 --date 2026-07-22 --json` | `.results[].{executed_at,price,size,premium}` |
| price levels | `uw dark-pool price-levels --symbol PATH --top-n 15 --days 5 --json` | `.results[].{price_level,total_premium,total_shares,trade_count}` |
| rank | `uw dark-pool ticker-summary --top-n 30 --date 2026-07-22 --json` | `[.results[].ticker]|index("PATH")` → outside top-30 |

## Tool errors

<none>

## Verdict for downstream

- **Net institutional bias: MIXED / balanced-to-mildly-distributive today, inside a BEARISH 5-day structure.** Broad tape mild-buy (57.2%, suggestive only) and a real $9.1M above-ask lift, but offset by a larger $16M mega SELL and — decisively — spot trading ~12% BELOW the week's $11.90–12.50 institutional volume zone (overhead supply).
- **Conviction: 2/5.** The accumulation reads are all in the "suggestive" band; the structural overhead-supply picture caps any bullish DP interpretation. This does NOT confirm the 5-day bullish options sweep campaign at the tape/price level.
- **Largest block as % of float:** n/a exact (float absent); ≈0.28% of ~526M shares out — moderate, not a franchise-defining print.
- **Three S/R levels for phase-9:**
  1. **$11.90–$12.00** — major overhead resistance (heaviest 5-day DP cluster, ~$550M, now trapped supply). A reclaim of $12 would flip the structure.
  2. **$10.85–$10.88** — near battle zone (today's $9.1M above-ask buyer vs the $16M seller); first resistance on a bounce.
  3. **$10.50 → $10.00** — support shelf (spot + the near-ATM 10.5 / 10.0 puts bought in phase-1); loss of $10.00 opens the downside tail (8.5/9.0 crash puts).
- **Open questions:**
  - Did the ~12% weekly drop *precede* the bullish sweep campaign (dip-buying) or *follow* distribution at $12? → phase-5 historical price path.
  - Is the $12 cluster institutional distribution that led the slide, or trapped longs now capping rallies? → phase-3 OI change at those strikes.
  - Does the 7/22 after-hours tape tie to any headline? → phase-6.
