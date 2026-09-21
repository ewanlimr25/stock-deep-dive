# Phase 2 — Dark Pool & Block Prints

**Ticker:** NOW
**As-of date:** 2026-06-05
**Generated:** 2026-06-06T12:10:00-04:00
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md, phase-1-flow.md

## Summary

NOW printed **$473.2M of off-exchange premium** on the as-of day, but the
institutional read is **balanced-with-a-sell-lean, not conviction
distribution**: large-tier buy_ratio 0.461 and block-tier 0.477 (derived
sell_ratio 0.539 / 0.523 — suggestive band only, below the 0.55-buy /
≥0.55-sell confidence thresholds). The 5-day price-level map is a
**descending trail of the week's ~−17% collapse (≈136 → 112.45)**, not an
accumulation zone — confirming phase-1-flow.md's bearish-leaning tape rather
than contradicting it. The one mega-tier print ($13.86M @ 118.24, buy-classified)
is N=1 and was immediately run over by a further ~5% decline. Per phase-0.5's
`[CTX:] BUSY_NAME_NORMAL_DAY`, this phase's confluence is **capped at `+`**.

## Key signals

- **Tier ratios lean sell, low confidence**: large tier buy_ratio **0.461**
  ($379.1M, 1,974 prints), block tier **0.477** ($80.2M, 39 prints) — derived
  sell_ratios 0.539/0.523, inside the 0.45–0.55 "suggestive" band
  [DP:block_stratified].
- **Single mega print**: 117,240 sh @ $118.24 = **$13,862,458** at 13:39:06
  UTC, vs_mid +0.08 (buy-classified, buy_ratio 1.0 but N=1)
  [DP:largest, DP:block_stratified] — 0.0115% of float; buyer underwater by
  the close (112.45).
- **5-day levels are a markdown trail, not S/R clusters**: 119.36 ($148.4M),
  135.86 ($105.8M), 127.65 ($68.7M), 117.90 ($41.3M), 112.45 ($32.7M)
  [DP:price_levels --days 5] — the stock traversed 137→112 this week; supply
  sits overhead at 117.9–120 ($206M combined within +5–7% of spot).
- **Premarket institutional selling prints**: $5.76M at 119.36–119.81 by
  12:21 UTC (8:21am ET) before the −6% session [DP:extended_hours].
- **NOW outside top-30 DP tickers** market-wide (leaders QQQ $21.4B, SPY
  $20.9B, MU $15.5B, NVDA $10.7B, SNDK $5.8B) [DP:ticker_summary] — heavy
  for NOW, unremarkable for the tape; consistent with `[CTX:]`
  BUSY_NAME_NORMAL_DAY.

## Detailed findings

### Largest blocks

Top-25 by premium: **$77,188,346 / 669,837 sh** (≈0.066% of float 1.02B,
phase-0-intake.md §Finviz) [DP:largest]. Times UTC:

| Time | Price | Size | Premium | vs mid | % float |
|---|---|---|---|---|---|
| 13:39:06 | 118.24 | 117,240 | $13,862,458 | +0.080 | 0.0115% |
| 16:27:52 | 113.69 | 60,000 | $6,821,400 | −0.005 | 0.0059% |
| 21:22:28 | 112.45 | 51,341 | $5,773,295 | +0.655 (above ask 111.98) | 0.0050% |
| 20:00:19 | 112.45 | 47,146 | $5,301,568 | +0.090 | 0.0046% |
| 14:06:36 | 114.86 | 39,600 | $4,548,456 | +0.015 | 0.0039% |
| 12:21:23 | 119.36 | 36,575 | $4,365,592 | −0.590 (below mid, premarket) | 0.0036% |

The block sequence tracks the decline (118 → 115 → 113 → 112.45); ~$17.7M of
the top-25 premium printed at exactly 112.45 between 20:00:19–21:22:28 UTC —
4pm-close/late crosses at the closing price (mechanical, not directional).
[DP:block_pct_float fz] Largest block = **0.0115% of float — order size is
noise for a 1.02B-float name**; advisory only.

### Tier breakdown

[DP:block_stratified] `total_premium_all_tiers` = **$473,177,699**;
`highest_tier` = mega. Tier boundaries per tool caveat: mega ≥$10M, block
≥$1M, large ≥$100k.

| Tier | buy_ratio | derived sell_ratio | buy vol | sell vol | Premium | Prints |
|---|---|---|---|---|---|---|
| mega | 1.000 | 0.000 | 117,240 | 0 | $13,862,458 | 1 |
| block | 0.477 | 0.523 | 334,483 | 367,165 | $80,225,754 | 39 |
| large | 0.461 | 0.539 | 1,528,292 | 1,786,444 | $379,089,487 | 1,974 |

(No `sell_ratio` field exists — derived as `1 − buy_ratio`,
`lib/uw-json-paths.md`.) Total classified DP volume ≈ 4.13M sh ≈ 0.41% of
float. The weight of evidence (large+block, 2,013 prints) leans sell at
0.46–0.48 buy — **inside the suggestive band, not high-confidence
distribution** (heuristic needs ≤0.45).

### Price levels (5 days: 2026-06-01 → 2026-06-05)

[DP:price_levels --days 5 — window verified to end at as-of:
`dates_covered = [2026-06-05 … 2026-06-01]`, matches phase-0 available-dates]

| Level | Premium | Shares | Prints | vs spot 112.45 |
|---|---|---|---|---|
| 119.36 | $148,352,419 | 1,242,899 | 49 | +6.1% |
| 135.86 | $105,756,570 | 778,423 | 61 | +20.8% |
| 127.65 | $68,740,796 | 538,510 | 68 | +13.5% |
| 117.90 | $41,266,855 | 350,016 | 48 | +4.8% |
| **112.45** | $32,733,859 | 291,097 | 48 | **at spot** |
| 137.00 | $20,724,392 | 151,273 | 107 | +21.8% |
| 127.24/127.12/127.00 | $44.9M comb. | 353,510 | 50 | +13% |
| 120.00 | $9,815,056 | 81,792 | 25 | +6.7% |

Read: a week-long markdown 137 → 127 → 119 → 112. Every big cluster sits
ABOVE spot because that's where price *was* — overhead supply, not
institutional bids. Nearest meaningful shelf: **117.9–120 (~$200M printed)**;
at-spot cluster 112.45 is largely the close-cross mechanics noted above.

### Extended-hours activity

[DP:extended_hours] All 15 rows code `extended_hours_trade`:
- **Premarket** (12:16–12:21 UTC = 8:16–8:21 ET): $1.40M @ 119.81 + $4.37M @
  119.36 (below mid −0.59) — institutions moving size before the regular
  session; price never saw 119 again.
- **Close-cross cluster** (20:00:04–20:00:36 UTC): ~$14.2M across 9 prints,
  all at exactly 112.45 — closing-price crosses, mechanical.
- **Post-close** (21:06–21:22 UTC): $1.22M + $5.77M at 112.45, the latter
  printed above the prevailing NBBO ask (111.98, vs_mid +0.655) — a late
  benchmark cross; NBBO mid had drifted to ~111.8 after hours (mild further
  weakness post-close).

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw dark-pool largest --symbol NOW --top-n 25 --sort-by premium --date 2026-06-05 --json` | $13,862,458 @118.24 ← `.results[0].premium/.price`; top-25 tot $77,188,346 ← `map(.premium)\|add` | top-25 |
| `uw dark-pool block-stratified --symbol NOW --top-n 30 --min-tier large --date 2026-06-05 --json` | mega br 1.0 / block 0.477 / large 0.461; tot $473,177,699 ← `.results[]\|select(.ticker=="NOW")\|.<tier>.buy_ratio, .total_premium_all_tiers` | NOW row |
| `uw dark-pool extended-hours --symbol NOW --top-n 15 --date 2026-06-05 --json` | premarket $4,365,592 @119.36 ← `.results[].premium` | 15 rows |
| `uw dark-pool price-levels --symbol NOW --top-n 15 --days 5 --date 2026-06-05 --json` | 119.36 → $148,352,419 ← `.results[0]`; window ← `.dates_covered` | top-15 levels |
| `uw dark-pool ticker-summary --top-n 30 --date 2026-06-05 --json` | NOW absent ← `map(.ticker)\|index("NOW")` → null | top-30 |

## Tool errors

(none)

## DATA NOTE / CORRECTION

First ticker-summary extraction used `{now:(.results[]\|select(...))}` which
yields an empty stream (not null) when the row is absent, printing nothing.
Re-extracted from the saved JSON with `[.results[]\|select(...)]\|first` →
confirmed `now=null`, `n=30`. No numeric value changed.

## Verdict for downstream phases

- **Accumulation / Distribution / Mixed:** **Mixed, sell-leaning** — tier
  ratios 0.46–0.48 buy are below balance but above the 0.45
  distribution-confidence line; the price-level map confirms a markdown week,
  with no visible accumulation shelf below spot.
- **Conviction:** 2 / 5 (capped at `+` by `[CTX:]`, phase-0.5-context.md;
  classification is probabilistic and the lean is inside the suggestive band)
- **Largest block as % of float:** 0.0115% ($13.9M / 117,240 sh vs 1.02B
  float) [DP:block_pct_float fz] — **not meaningful sizing for this name**;
  nothing on the DP tape forces a directional read by size alone.
- **Three S/R levels for phase-9:**
  1. **112.45** — at-spot close-cross cluster ($32.7M, 5-day); first
     reference, weak support.
  2. **117.90–119.36** — $190M+ printed this week; primary overhead supply /
     resistance on any bounce (+4.8% to +6.1%).
  3. **127.0–127.65** — $113M mid-week shelf; second resistance band (+13%).
- **Open questions:** Did OI build at the put strikes phase-1 flagged
  (110/135) — i.e., is the options campaign backed by fresh positioning
  (phase 3)? What event drove the −17% week (phase 6/7c news scan)? Is the
  morning mega-buy at 118.24 a one-off knife-catch or the start of a
  laddered bid (needs next sessions — out of scope for as-of)?
