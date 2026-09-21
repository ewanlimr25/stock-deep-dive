# Phase 2 — Dark Pool & Block Prints

**Ticker:** NOW
**As-of date:** 2026-07-17
**Generated:** 2026-07-19 (run) for as-of 2026-07-17
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md, phase-1-flow.md

## Summary

Dark-pool prints are **balanced with a mild genuine buy-lean, NOT conviction
accumulation.** The eye-catching **mega-tier buy_ratio = 1.00 ($121.9M all buy)** is
an artifact of **closing-cross / late facilitation prints** — the top four blocks
(803,594 sh $82.96M @ 20:10, 271,703 sh $28.05M @ 20:09, plus two 20:00 prints) all
executed at **exactly the $103.24 close**, i.e. auction/MOC facilitation, not
aggressive paying-up. Strip those and the picture is: **large tier (the biggest
bucket, $158.6M) buy_ratio 0.488 = balanced/slightly distributive**, while the
**block tier ($32.3M) buy_ratio 0.618 = mildly accumulative.** Price levels cluster
tightly around spot ($102.90–$104.85) with no directional displacement; a lighter
shelf sits at $111–112.5 above. **NOW is absent from the dark-pool ticker-summary
top-30** (leaders SPY/MU/QQQ/SNDK/NVDA) — consistent with phase-0.5's
BUSY_NAME_NORMAL_DAY. Net: **Mixed / balanced**, conviction 2/5.

## Key signals

- **Mega buy_ratio 1.00 is closing-cross, not accumulation:** top block 803,594 sh
  $82.96M @ 20:10 at the exact $103.24 close `[DP:largest]` `[DP:extended_hours]`.
- **Large tier (biggest, $158.6M) balanced-to-sell:** buy_ratio **0.488**
  `[DP:block_stratified .large.buy_ratio]`.
- **Block tier mildly accumulative:** buy_ratio **0.618**, $32.3M
  `[DP:block_stratified .block.buy_ratio]`.
- **Price footprint pinned to spot:** heaviest 5-day clusters $103.24 ($153.0M),
  $104.85 ($105.0M), $104.01 ($50.5M) — a shelf around current price `[DP:price_levels]`.
- **NOW absent from ticker-summary top-30** (not a dark-pool leader today) `[DP:ticker_summary]`.

## Detailed findings

### Largest blocks (top-6 of 25; $161.3M / 1.56M sh total)

| time | price | size (sh) | premium | note |
|---|---|---|---|---|
| 20:10 | 103.24 | 803,594 | $82.96M | closing-cross facilitation (= close) |
| 20:09 | 103.24 | 271,703 | $28.05M | closing-cross |
| 20:00 | 103.24 | 105,400 | $10.88M | late print @ close |
| 20:00 | 103.24 | 66,709 | $6.89M | late print @ close |
| 19:06 | 104.40 | 44,400 | $4.64M | **intraday** (only sizeable non-close block) |
| 20:48 | 103.24 | 33,590 | $3.47M | post-close @ close |

~$128M of the top-25 $161M prints at the exact $103.24 close between 20:00–20:48 →
facilitation/auction, de-rated as directional evidence. The genuine intraday
footprint (e.g. 19:06 @ $104.40) is small.

### Tier breakdown `[DP:block_stratified]`

| tier | buy_ratio | derived sell_ratio | buy_vol | sell_vol | premium |
|---|---|---|---|---|---|
| mega | **1.000** | 0.000 | 1,180,697 | 0 | $121.90M ← **closing-cross-dominated, de-rate** |
| large | **0.488** | 0.512 | 745,687 | 783,524 | $158.56M ← biggest bucket, balanced/slight sell |
| block | **0.618** | 0.382 | 192,552 | 119,118 | $32.26M ← mild genuine accumulation |
| retail | 0.500 | 0.500 | 0 | 0 | $0 |

Only the block tier (0.618) is a suggestive directional read (0.55–0.7 band =
"suggestive only" per rubric). Mega=1.0 fails the smell test (auction artifact);
large=0.488 is noise around balanced.

### Price levels (5-day; trailing window — see caveat) `[DP:price_levels]`

Spot = $103.24. Clusters by premium:
- **$103.24 — $153.0M** (spot / closing cross)
- **$104.85 — $105.0M** (just above spot; secondary shelf)
- **$104.01 — $50.5M** (prev_close)
- $104.73 — $23.7M
- **$112.5 — $21.1M** / **$111.26 — $13.2M** (upside shelf ~8% above spot)
- $104.40 — $7.5M · **$102.90 — $7.0M** (nearest support cluster below)

Read: institutional interest is concentrated $102.90–$104.85 (a tight band bracketing
spot) with a lighter magnetic shelf at $111–112.5. No cluster displacement that would
signal directional accumulation/distribution.

### Extended-hours activity `[DP:extended_hours]`

15 prints, $145.8M — but the top rows are the SAME 20:00–20:10 closing-cross prints
at $103.24 (803,594 & 271,703 sh). This *confirms* the mega-tier buy_ratio=1.0 is
close/after-hours facilitation, not fresh directional intent. No distinct
pre-market catalyst print. (Caveat noted per rubric: EH prints here are auction
facilitation, not index-rebalance news — attribute to the close, not a phase-6 event.)

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows |
|---|---|---|
| `uw dark-pool largest --symbol NOW --top-n 25 --sort-by premium` | $161.3M/1.56M sh; top 803,594 sh @103.24 20:10 ← `.results[]` | 25 |
| `uw dark-pool block-stratified --symbol NOW --min-tier large` | mega 1.00 / large 0.488 / block 0.618 ← `.results[0].<tier>.buy_ratio` | 1 |
| `uw dark-pool extended-hours --symbol NOW --top-n 15` | $145.8M; top = 20:00–20:10 @103.24 close prints ← `.results[]` | 15 |
| `uw dark-pool price-levels --symbol NOW --top-n 15 --days 5` | clusters 103.24 $153M, 104.85 $105M, 112.5 $21M ← `.results[].price_level/.total_premium` | 15 |
| `uw dark-pool ticker-summary --top-n 30` | NOW absent (leaders SPY/MU/QQQ/SNDK/NVDA) ← `[.results[].ticker]` | 30 |
| `fz quote NOW` (float retry) | still 14/84 fields, float n/a ← `.fundamentals` | 1 |

## Tool errors

None (all reads round-tripped through `jq`). `fz` float remained unavailable
(partial 14/84 snapshot, session-wide) — advisory-only lane, handled by estimate below.

## DATA NOTE / CORRECTION

None on the UW reads. `fz` %-of-float is an **estimate** (see verdict) because the
`fz` snapshot never returned `Shs Float` this session; flagged as estimate, not
transcribed as measured.

## Verdict for downstream

- **Bias:** **Mixed / balanced** (mild block-tier buy-lean; mega buy_ratio=1.0
  discounted as closing-cross facilitation; large tier balanced/slight sell). **Not**
  accumulation, **not** distribution.
- **Conviction:** **2 / 5** (size present but non-directional; dominated by auction
  prints; NOW not a DP leader).
- **Largest block as % of float (advisory, ESTIMATE):** `fz` float unavailable this
  session. Using an order-of-magnitude estimate of **~2.07B shares** (post-~10:1
  split; ServiceNow historically ~207M pre-split), the 803,594-sh top block ≈
  **~0.04% of float** and the entire top-25 (1.56M sh) ≈ **~0.075%** — **immaterial
  for a name this large.** Even the headline blocks carry no size-conviction here.
  `[DP:block_pct_float fz]` (estimate; verify float in phase-7b/7c).
- **Three S/R levels for phase-9:**
  1. **Support ~$102.90** (nearest DP cluster below spot) → stop reference.
  2. **Pivot/shelf $104.01–$104.85** (prev_close + heaviest above-spot cluster).
  3. **Upside magnet $111.26–$112.50** (secondary DP shelf ~8% above) → first target zone.
- **Open questions:** Do the phase-3 OI walls line up with the $111–112.5 DP shelf?
  Does phase-3 confirm the phase-1 Jan-2027 bid-side puts as OI *builds* (writes) —
  which would make the balanced DP + put-writing a coherent neutral-to-bullish
  income posture into earnings?
