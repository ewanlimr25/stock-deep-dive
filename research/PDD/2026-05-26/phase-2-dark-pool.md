# Phase 2 — Dark Pool & Block Prints

**Ticker:** PDD
**As-of date:** 2026-05-26
**Generated:** 2026-05-26T20:26:00Z
**Upstream phases cited:** phase-0.5-context.md, phase-1-flow.md

## Summary

Dark pool is the **first genuinely one-sided signal in this workup: mild-to-moderate
accumulation into the print.** The block tier (≥$1M trades) is **100% buy** — 10
trades, $17.09M, buy_volume 175,998 vs sell_volume **0** (buy_ratio 1.0)
[DP:block_stratified]. The day's largest block, a $4.8M / 49,300-share print, executed
**above NBBO mid (+$0.075)** late session at $97.35 [DP:largest], and most large blocks
printed at-or-above mid in the $96.9–$97.5 zone while the stock closed lower at $96.58
— institutions paying up, not hitting bids. The 5-day institutional center of gravity
is a **$92.6M shelf at $97.79** just above spot, with a support shelf at **$94.52**
[DP:price_levels]. Caveats keep conviction moderate: classification is NBBO-probabilistic,
the broader large tier is only weakly buy (0.552), and this is accumulation *into a
binary earnings event* — it could be hedged against the phase-1 puts. Still, this is the
cleanest directional tilt so far and **partially offsets the mixed options tape**.

## Key signals

- **Block tier 100% buy:** $17.09M across 10 trades, sell_volume 0, buy_ratio **1.0**
  [DP:block_stratified]. (mega tier empty; large tier 0.552 buy on $42.7M / 186 trades.)
- **Largest block bought above mid:** $4.8M, 49,300 sh @ $97.35 vs mid $97.275 (+$0.075),
  15:17 ET [DP:largest] — biggest single print of the day is a lift, not a hit.
- **Institutional pivot $97.79:** $92.6M / 946,841 sh over 5 sessions — the dominant
  level, just above the $96.58 close [DP:price_levels].
- **Support shelf $94.52:** $37.5M / 396,863 sh (5-day) — the floor institutions defended
  [DP:price_levels]; deeper shelf at $92.00 ($3.1M).
- **No alarming overnight block:** extended-hours prints are modest ($150K–$878K) at
  $95.3–$95.7, no single mega pre-market block to suggest a news leak [DP:extended_hours].

## Detailed findings

### Largest blocks — `[DP:largest]`

| Time (ET) | Price | Size | Premium | NBBO mid | vs mid | Read |
|-----------|-------|------|---------|----------|--------|------|
| 15:17 | 97.35 | 49,300 | $4.80M | 97.275 | **+0.075** | buy (biggest, late) |
| 12:25 | 97.51 | 21,051 | $2.05M | 97.49 | +0.02 | buy |
| 09:30 | 94.83 | 18,284 | $1.73M | 94.68 | **+0.15** | buy (open) |
| 12:26 | 97.49 | 17,631 | $1.72M | 97.43 | +0.06 | buy |
| 10:27 | 97.18 | 13,210 | $1.28M | 97.175 | +0.005 | at mid |
| 12:27/12:28 | 97.50/97.45 | 12,072/11,850 | $1.18/1.15M | — | +0.03/+0.01 | buy |
| 13:51 | 97.50 | 11,500 | $1.12M | 97.30 | **+0.20** | strong lift |

The vast majority print **above mid** → buy-classified. Only a handful at/below mid
(96.93 −0.015, 97.46 0.00, 97.34 −0.005, 96.30 −0.02). The directional skew is buy.

### Tier breakdown — `[DP:block_stratified]`

| Tier (boundary) | Trades | Premium | Buy vol | Sell vol | Buy ratio |
|-----------------|--------|---------|---------|----------|-----------|
| mega (≥$10M) | 0 | $0 | 0 | 0 | n/a |
| **block (≥$1M)** | **10** | **$17.09M** | **175,998** | **0** | **1.000** |
| large (≥$100k) | 186 | $42.71M | 243,602 | 197,369 | 0.552 |
| Total all tiers | — | $59.80M | — | — | — |

The **block tier is unambiguously buy** (the cleaner institutional signal per the tool's
own caveat). The large tier's 0.552 is only "suggestive" (heuristic: 0.55–0.70 =
suggestive, >0.70 = high-confidence) — so the strong read rests on the 10 block trades.
No mega-tier prints today.

### Price levels (5-day clusters) — `[DP:price_levels]`

| Level | 5-day premium | Shares | Position vs spot ($96.58) |
|-------|---------------|--------|---------------------------|
| **97.79** | **$92.6M** | 946,841 | +1.3% — institutional center of gravity |
| 98.15 | $28.95M | 294,965 | +1.6% — resistance shelf |
| 97.35 / 97.2 / 97.5 / 97.45 | $9.2/6.2/3.8/3.4M | — | the day's accumulation band |
| **94.52** | **$37.5M** | 396,863 | −2.1% — primary support shelf |
| 94.37 / 92.00 | $5.8M / $3.1M | — | deeper support |

Heavy two-sided shelving: a thick band at **97.2–98.2** (accumulation + resistance) and a
defended floor at **94.5** with a backstop at **92**. Spot sits just under the 97.79 magnet.

### Extended-hours — `[DP:extended_hours]`

Pre-market prints are modest: largest $878K (9,207 sh @ 95.39, 06:11 ET), rest
$138K–$286K at $95.3–$95.7. No outsized overnight block → no evidence of a news-driven
leak ahead of the 5/27 print. Early prints (~95.4) are *below* the regular-session
accumulation band (~97.3), consistent with steady intraday buying lifting the level.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `dark_pool_largest` | symbol=PDD, top25, by premium | $4.8M top block @97.35 above mid; most prints buy-side |
| `dark_pool_block_stratified` | symbol=PDD, top30, min=large | block 100% buy ($17.09M); large 0.552; no mega |
| `dark_pool_price_levels` | symbol=PDD, top15, days5 | $92.6M @97.79 pivot; $37.5M @94.52 support |
| `dark_pool_extended_hours` | symbol=PDD, top15 | modest pre-mkt $95.3–95.7; no leak block |
| (`ticker_summary` value via phase-0.5 `insights_deep_dive`) | — | PDD DP $59.8M / 616,969 sh / 196 trades, avg $96.93 |

## Tool errors

None.

## Verdict for downstream phases

- **Institutional bias:** **ACCUMULATION (mild-to-moderate).** The one one-sided read in
  the workup — block tier 100% buy, biggest block lifted above mid late-day.
- **Conviction:** **3/5.** Block-tier buy is notable; tempered because (a) it rests on 10
  trades, (b) large tier is only weakly buy (0.552), (c) it's accumulation *into* a binary
  event and may be paired with the phase-1 downside hedges. Phase-0.5 caps phases 1–2
  confluence at `+` [CTX:unusual_verdict].
- **Three S/R levels for phase-9:**
  1. **Support $94.52** — $37.5M institutional shelf; below it, $92.00 backstop. Natural
     stop reference / downside-print magnet.
  2. **Pivot $97.79** — $92.6M 5-day center of gravity, +1.3% above spot; reclaiming and
     holding it post-earnings = bullish confirmation.
  3. **Resistance $98.15** — $29M shelf; first overhead supply on an up-move.
- **Open questions:** Does dealer gamma (phase-4) pin spot to the 97.79/98 shelf or leave
  it free post-print? Is the block buying genuine directional accumulation or the long leg
  of a hedged structure against the 95/90 puts (phase-1)? Phase-7c short interest will
  help arbitrate accumulation-vs-squeeze-setup.
