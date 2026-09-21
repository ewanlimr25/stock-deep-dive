# Phase 2 — Dark Pool & Block Prints

**Ticker:** HOOD
**As-of date:** 2026-06-05
**Generated:** 2026-06-07T12:28:00-04:00
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md, phase-1-flow.md

## Summary

The dark pool does **not** confirm the options tape's bearishness: HOOD printed
$376.4M across all tiers with block-tier `buy_ratio` 0.543 and large-tier 0.540
— squarely in the balanced zone (accumulation needs ≥0.55, distribution ≤0.45).
The one mega-tier print (429,184 sh @ $82.47 = $35.39M, `buy_ratio` 1.0) is an
after-hours print at exactly the closing price — an EOD/benchmark cross, not
directional intent, and its buy classification is de-rated accordingly. The
5-day price-level map shows the week's institutional volume concentrated at
**88.33–90.73 ($196M+), now 7–10% overhead** after the week's slide to 82.47 —
overhead supply, with a fresh near-spot shelf at 82.47–82.85 ($97.7M) and
intraday blocks printed down to 79.78–80.27. Net: institutions traded the down
day balanced-to-slightly-buy in the dark while options flow leaned bearish
(phase-1-flow.md) — a divergence, not a confirmation.

## Key signals

- Block-tier `buy_ratio` **0.543** (buy 255,461 / sell 214,594 sh, $38.8M, 23
  trades); large-tier **0.540** ($302.2M, 1,560 trades) → derived `sell_ratio`
  0.457/0.460 — **balanced, no distribution signature** [DP:block_stratified]
- Mega print: 429,184 sh @ 82.47, $35,394,804, 21:22:27Z (17:22 ET) at the
  close price with several sibling 82.47 prints after 20:00Z — **EOD cross,
  non-directional** [DP:largest, DP:extended_hours]
- 5-day clusters: **90.73 ($111.3M / 1.23M sh) and 88.33 ($84.7M)** sit above
  spot 82.47 — earlier-week volume now acting as overhead supply;
  near-spot shelf 82.85 ($52.9M) + 82.47 ($44.9M) [DP:price_levels]
- Intraday low-zone blocks: $2.39M @ 79.775 (18:44Z), $2.26M @ 80.265 (19:01Z),
  ~$1.0–1.3M each @ 80.00/80.48/80.49/80.60 — size showed up at 79.8–80.6
  [DP:largest]
- HOOD **absent from the day's dark-pool top-30** (leaders QQQ $21.4B, SPY
  $20.9B, MU $15.5B) — consistent with phase-0.5's "size is normal" verdict
  [DP:ticker_summary]

## Detailed findings

### Largest blocks [DP:largest]

| Time (UTC) | Price | Size | Premium | NBBO bid/ask | % of float |
|---|---|---|---|---|---|
| 21:22:27 | 82.47 | 429,184 | $35.39M | 82.30/82.50 | 0.0564% |
| 15:23:17 | 83.50 | 40,009 | $3.34M | 83.50/83.51 | 0.0053% |
| 13:52:46 | 84.17 | 30,733 | $2.59M | 84.14/84.16 | 0.0040% |
| 13:30:23 | 86.24 | 28,280 | $2.44M | 86.18/86.30 | 0.0037% |
| 18:44:44 | 79.775 | 30,000 | $2.39M | 79.77/79.78 | 0.0039% |
| 13:37:17 | 87.16 | 26,621 | $2.32M | 87.08/87.13 | 0.0035% |
| 19:01:24 | 80.265 | 28,180 | $2.26M | 80.33/80.34 (below bid) | 0.0037% |

Float = 761.21M sh (phase-0-intake.md, `fz`) → even the mega print is **0.056%
of float** `[DP:block_pct_float fz]` — advisory: block sizes here are routine
for a 761M-float name, not conviction prints. Block prices trace the day's
slide 87.16 → 79.78 → close 82.47. Duplicate feed rows noted (81.20 ×2,
80.00 ×2) — treated as single prints narratively.

### Tier breakdown [DP:block_stratified]

| Tier | buy_ratio | derived sell_ratio | buy_vol | sell_vol | Premium | Trades |
|---|---|---|---|---|---|---|
| mega (≥$10M) | 1.000 | 0.000 | 429,184 | 0 | $35.39M | 1 |
| block (≥$1M) | 0.543 | 0.457 | 255,461 | 214,594 | $38.81M | 23 |
| large (≥$100k) | 0.540 | 0.460 | 1,971,134 | 1,676,381 | $302.21M | 1,560 |
| retail | — | — | 0 | 0 | $0 | 0 |

`total_premium_all_tiers` $376,412,130. No `sell_ratio` field exists — derived
as 1−buy_ratio (phantom-field guard). Mega tier's 1.0 is one EOD cross —
classification is NBBO-probabilistic and meaningless on a closing print;
excluded from the verdict. Total DP shares ≈ 4.55M ≈ **0.60% of float**
`[DP:block_pct_float fz]`.

### Price levels — 5 sessions 2026-06-01→06-05 [DP:price_levels]

Window confirmed == phase-0 available dates (latest-anchored = as-of; no slide).

| Level | Premium | Shares | Trades | vs spot 82.47 |
|---|---|---|---|---|
| 90.73 | $111.31M | 1,226,787 | 32 | +10.0% overhead |
| 88.33 | $84.72M | 959,103 | 48 | +7.1% overhead |
| 82.85 | $52.87M | 638,100 | 33 | **+0.5% — at spot** |
| 82.47 | $44.86M | 543,903 | 18 | **0.0% — at spot** |
| 88.16 | $36.29M | 411,616 | 48 | +6.9% |
| 88.00 / 87.70 / 87.38 / 87.16 | $10.8M / $7.3M / $10.4M / $6.2M | — | 14–28 | +5.7–6.7% |
| 84.50 / 84.00 / 83.50 | $7.0M / $6.7M / $6.5M | — | 14–26 | +1.2–2.5% |
| 86.00 | $5.97M | 69,435 | 20 | +4.3% |

Read: the heavy 88–91 volume is *earlier-week* prints before the slide — in a
falling tape this is trapped/overhead supply, not "institutions paying up"
(the accumulation heuristic assumes static spot; here spot moved). The freshest
big clusters are at spot (82.47/82.85).

### Extended-hours activity [DP:extended_hours]

- Pre-market: 11:01Z (07:01 ET) 3,942 sh @ 87.35; 11:54Z 3,772 @ 87.10; 13:01Z
  (09:01 ET) 9,000 @ 86.30 — institutions printed at 86–87.4 *before* the
  regular-session slide; modest size.
- Post-close: the 429k mega @ 82.47 plus ≥9 more prints at/near 82.47
  (20:00–21:52Z) totalling ~$45M — all at the closing price, signature of
  MOC/benchmark crosses (possibly index-flow), **not directional**; flagged per
  the rebalancing pitfall and de-rated.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw dark-pool largest --symbol HOOD --top-n 25 --sort-by premium --date 2026-06-05 --json` | mega 429,184@82.47 ← `.results[] \| {executed_at, price, size, premium, nbbo_*}` | top-25 |
| `uw dark-pool block-stratified --symbol HOOD --top-n 30 --min-tier large --date 2026-06-05 --json` | buy_ratios 1.0/0.543/0.540 ← `.results[] \| select(.ticker=="HOOD") \| .mega/.block/.large.buy_ratio` | 1 row |
| `uw dark-pool extended-hours --symbol HOOD --top-n 15 --date 2026-06-05 --json` | post-close 82.47 cluster; pre-mkt 87s ← `.results[]` | 15 |
| `uw dark-pool price-levels --symbol HOOD --top-n 15 --days 5 --json` | 90.73=$111.3M etc ← `.results[] \| {price_level, total_premium}`; window ← `.dates_covered` | 15 |
| `uw dark-pool ticker-summary --top-n 30 --date 2026-06-05 --json` | HOOD absent ← `to_entries[] \| select(.value.ticker=="HOOD")` (empty) | top-30 |

## Tool errors

(none)

## DATA NOTE / CORRECTION

(none — duplicate feed rows in `largest` flagged inline, aggregates taken from
`block-stratified` which is unaffected)

## Verdict for downstream phases

- **Bias from this phase:** **Mixed / balanced** — no distribution signature in
  the dark despite bearish lit options flow (phase-1-flow.md); slight buy tilt
  (0.54) is below the 0.55 suggestive threshold and treated as noise.
- **Conviction:** 2
- **Largest block as % of float:** 0.056% (mega EOD cross) `[DP:block_pct_float
  fz]` — not meaningful for a 761M-float name; whole DP day ≈ 0.60% of float.
- **Three S/R levels for phase-9:**
  1. **82.47–82.85** — freshest at-spot institutional shelf ($97.7M, 5-day)
  2. **79.78–80.60** — where intraday size printed at the lows (~$8M of blocks)
  3. **88.16–88.33** (then 90.73) — overhead supply from earlier-week volume
- **Open questions:** Does OI confirm the 85–90 call ceiling phase-1 flagged
  (phase 3)? Were the post-close 82.47 crosses index-rebalance flow (phase 6
  news check)? If price reclaims 84.5–85, does the overhead-supply read flip?
