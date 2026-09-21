# Phase 2 — Dark Pool & Block Prints

**Ticker:** MSFT
**As-of date:** 2026-06-01
**Generated:** 2026-06-02T11:00:41Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md, phase-1-flow.md

## Summary

The dark-pool tape is **large in dollars but low in directional conviction.** MSFT
is a top-4 market dark-pool name today ($6.09B total premium, 13.2M shares, avg
print $461.69 — *above* spot $459.77), but **$2.31B of it is a single cluster of
after-hours blocks (20:00–21:00 ET) all printed at exactly $460.52** — the
textbook signature of **index/basket rebalancing or a closing cross, not
directional accumulation** (phase-2 pitfalls: de-rate extended-hours basket
flow). Tier buy-ratios are *mildly* accumulative at the top (mega `buy_ratio`
0.552, large 0.532) but distributive at block tier (0.438 → derived sell 0.562),
and **all sit in the 0.44–0.55 "suggestive-only" band — none above the 0.7
high-confidence line.** As a fraction of MSFT's **7.31B float**, even the $565M
top block is **0.017%** — immaterial for this name. Net: dark pool **does not
cleanly confirm phase-1's bullish call tilt**; it is mixed/rebalance-dominated.

## Key signals

- **$2.31B in after-hours blocks at a single price ($460.52), 20:00–21:00 ET** —
  almost certainly basket/rebalance/closing-cross flow, **de-rated as directional**
  `[DP:extended_hours]`.
- **Mega-tier `buy_ratio` 0.552** (buy 3.14M vs sell 2.54M sh, $2.61B) — *marginal*
  accumulation, **suggestive only (< 0.7)**, and contaminated by the AH cluster
  `[DP:block_stratified]`.
- **Block-tier `buy_ratio` 0.438** (derived sell_ratio 0.562, $717M) — small-block
  tier is net **distributive** `[DP:block_stratified]`.
- 5-day institutional price shelves: **$450 (−2.1%, $4.43B), $427 (−7.1%, $3.04B),
  $412–418 (−9 to −10%)** — support map well *below* spot `[DP:price_levels]`.
- Largest block = **0.017% of float**; whole-day DP = 0.18% of float — size is
  **not** a conviction signal for a 7.31B-float mega-cap `[DP:block_pct_float fz]`.

## Detailed findings

### Largest blocks (top 8) `[DP:largest]`

Spot $459.77; `vs_spot` and `% float` (÷ 7.31B) shown. Note the **7 largest are all
after-hours @ $460.52**:

| Time(ET) | Price | Size (sh) | Premium | % float | vs_mid | vs_spot |
|----------|-------|-----------|---------|---------|--------|---------|
| 20:00:18 | 460.52 | 1,227,000 | **$565.1M** | 0.017% | −0.07 | +0.16% |
| 20:05:21 | 460.52 | 950,000 | $437.5M | 0.013% | +0.32 | +0.16% |
| 20:05:31 | 460.52 | 949,981 | $437.5M | 0.013% | +0.45 | +0.16% |
| 21:00:28 | 460.52 | 524,147 | $241.4M | 0.007% | +4.42 | +0.16% |
| 20:00:25 | 460.52 | 292,480 | $134.7M | 0.004% | −0.07 | +0.16% |
| 20:00:08 | 460.52 | 228,968 | $105.4M | 0.003% | −0.24 | +0.16% |
| 20:25:05 | 460.52 | 141,865 | $65.3M | 0.002% | +1.12 | +0.16% |
| 12:11:39 | 450.24 | 111,050 | $50.0M | 0.002% | −16.9 | −2.07% |

The uniform $460.52 price + 20:00–21:00 ET window across seven prints is the tell:
this is a **coordinated after-hours basket/rebalance/cross**, not seven independent
accumulation decisions. `vs_mid` is mixed (some above, some at/below) — consistent
with a cross, not a directional sweep. Only the 12:11 RTH print ($50M @ $450.24,
−16.9 vs mid → sell-side) is a clean intraday directional block, and it is a *sell*
near the $450 shelf.

### Tier breakdown `[DP:block_stratified]` (whole day, RTH+AH combined)

| Tier | `buy_ratio` | derived sell | buy / sell vol (sh) | total_premium | trades |
|------|-------------|--------------|----------------------|---------------|--------|
| mega | **0.552** | 0.448 | 3,137,341 / 2,544,960 | $2,611.9M | 32 |
| large | 0.532 | 0.468 | 3,177,131 / 2,792,961 | $2,756.4M | 12,353 |
| block | **0.438** | **0.562** | 680,579 / 873,756 | $717.3M | 355 |
| retail | 0.500 | — | 0 / 0 | $0 | 0 |
| **all tiers** | — | — | — | **$6,085.7M** | — |

`highest_tier = mega`. Top two tiers lean *mildly* buy (0.55/0.53), block tier
leans sell (0.44). But the mega tier's 32 trades are essentially the AH cluster
above, so its 0.552 is **rebalance-contaminated and suggestive-only** — not a
high-confidence accumulation read.

### Price levels (5-day clusters) `[DP:price_levels]`

`dates_covered`: 2026-06-01, 05-29, 05-28, 05-27, 05-26 (contiguous — no data-gap
contamination). Sorted by premium; distance to spot $459.77:

| Level | 5-day premium | shares | dist to spot |
|-------|---------------|--------|--------------|
| **$450.24** | $4,434.9M | 9.85M | −2.07% ← nearest major shelf |
| **$426.99** | $3,039.2M | 7.12M | −7.13% |
| $460.52 | $2,359.6M | 5.12M | +0.16% (today's AH cluster) |
| **$412.67** | $1,728.4M | 4.19M | −10.24% |
| $416.03 / $415.22 / $418.57 / $414.83 | $0.3–0.6B ea | — | −9 to −10% |
| $450.23 / $450.25 | $0.7B / $0.1B | — | −2.07% |

Institutional transaction shelves cluster at **$450 (heavy, −2%)**, **$427 (−7%)**,
and a deep **$412–418 (−10%)** zone. All major shelves are *below* spot — these are
support/accumulation zones from the recent run-up, useful as phase-9 stop/entry
references, but they sit beneath current price (institutions are not paying *up*
through spot in size during RTH).

### Extended-hours activity `[DP:extended_hours]`

**$2,311.4M across 15 prints**, all coded `extended_hours_trade`, concentrated
20:00–21:00 ET at $460.52 (the same blocks as the "largest" table). This is **~38%
of the entire day's dark-pool premium executed after hours at one price** → flagged
as **likely index/basket/rebalance or closing-cross flow, de-rated as directional
intent**. No near-term catalyst (earnings 2026-07-29, phase-0.5) to explain it as
event hedging; 2026-06-01 is the first trading day of June — consistent with
start-of-month/index allocation flow. Phase-6 to cross-check for any overnight news.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|------------------|--------------------------|-----------|
| `uw dark-pool largest --symbol MSFT --top-n 25 --sort-by premium --date 2026-06-01 --json` | top block $565.1M @ $460.52, 0.017% float ← `.results\|sort_by(.premium)\|reverse` | top-25 |
| `uw dark-pool block-stratified --symbol MSFT --top-n 30 --min-tier large --date 2026-06-01 --json` | mega buy_ratio 0.552; block 0.438 ← `.results[0].mega.buy_ratio`, `.block.buy_ratio` | 1 (MSFT) |
| `uw dark-pool extended-hours --symbol MSFT --top-n 15 --date 2026-06-01 --json` | AH total $2,311.4M @ $460.52 ← `map(.premium)\|add` | 15 |
| `uw dark-pool price-levels --symbol MSFT --top-n 15 --days 5 --date 2026-06-01 --json` | shelves $450/$427/$412–418 ← `.results\|sort_by(.total_premium)`; `.dates_covered` | top-15, 5d |
| `uw dark-pool ticker-summary --top-n 30 --date 2026-06-01 --json` | MSFT #4, $6.09B, avg $461.69, max trade $565M ← `.results\|map(select(.ticker=="MSFT"))` | top-30 |

## Tool errors

None — all five commands returned valid JSON that round-tripped through `jq`.

## DATA NOTE / CORRECTION

None — all values round-tripped through `jq`. (`buy_ratio` read from the nested
per-tier object `.results[0].<tier>.buy_ratio`, not a flat column; `sell_ratio`
derived as `1 − buy_ratio` per the field-path map — there is no `sell_ratio` key.)

## Verdict for downstream phases

- **Net institutional bias: MIXED / rebalance-dominated.** Mega+large tiers lean
  *marginally* buy (0.552 / 0.532, suggestive-only), block tier distributes (0.438),
  and the dominant $2.31B is after-hours basket-like flow at a single price → **low
  directional conviction. Does NOT confirm phase-1's bullish call tilt.**
- **Conviction: 2/5.** Large dollars, but (a) buy-ratios below high-confidence 0.7,
  (b) biggest prints are likely non-directional rebalance, (c) immaterial as % of float.
- **Largest block as % of float: 0.017%** (whole-day DP 0.18%) — size is **not**
  meaningful for a 7.31B-float name; do not let raw dollars inflate conviction.
- **Three S/R levels for phase-9:**
  1. **$450** — nearest heavy institutional shelf (−2.1%, $4.43B 5-day) → first
     support / logical stop reference.
  2. **$427** — major secondary shelf (−7.1%, $3.04B).
  3. **$412–418** — deep accumulation zone (−10%); $460.52 marks today's near-spot
     transaction price (mild resistance/pivot).
- **Open questions:** Can phase-6 attribute the $2.31B AH @ $460.52 to a specific
  index/basket event (confirming it as non-directional)? Does phase-3 OI show walls
  at the same 450/460/500 strikes phase-1 flagged, and does the $450 DP shelf line
  up with a put wall (support confluence)?
