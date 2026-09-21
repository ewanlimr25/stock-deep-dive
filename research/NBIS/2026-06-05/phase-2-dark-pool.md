# Phase 2 — Dark Pool & Block Prints

**Ticker:** NBIS
**As-of date:** 2026-06-05
**Generated:** 2026-06-06T20:05:00-0400
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md, phase-1-flow.md

## Summary

Dark-pool activity was **enormous ($814.5M all-tier premium, ~3.5M shares ≈ 1.8%
of float) but directionally balanced**: buy_ratio 0.518 (mega) / 0.523 (block) /
0.497 (large) — all inside the 0.45–0.55 dead zone, so no accumulation or
distribution call at any tier. The prints map a violent repricing day: premarket
blocks at $247–252, a seller-initiated 127k-share block at $230 (below bid) at
10:06 ET during the slide, midday volume 217–223, an official-close benchmark
cross of 136,487 sh at $227.81, and **after-hours prints drifting down to
~$220.7 by 19:49 ET** — the decline continued after the bell. The week's biggest
institutional volume sits far overhead at $249.5–251.7 ($367M across three
levels) — now supply, not support.

## Key signals

- All-tier premium $814,456,252; tier buy_ratios mega 0.518 / block 0.523 /
  large 0.497 → **balanced, no conviction read** (derived sell_ratios 0.482 /
  0.477 / 0.503) `[DP:block_stratified]`
- Largest block: 136,487 sh @ $227.81 = $31.09M at 17:22 ET, printed at the
  official close vs NBBO 225.10/226.28 — benchmark/closing cross, not aggression;
  = **0.068% of float** (201.04M, phase-0) `[DP:largest]` `[DP:block_pct_float fz]`
- 2nd largest: 127,255 sh @ $230.00 = $29.27M at 10:06 ET **below the bid**
  (NBBO 230.76/231.03) — seller-initiated during the morning slide `[DP:largest]`
- 5-day price-level clusters: $249.5 ($137.3M), $251.68 ($122.4M), $249.18
  ($108.0M), $264.51 ($99.3M) — all 9–16% **above** spot; today's level $227.81
  holds $41.1M `[DP:price_levels]`
- Extended hours: premarket prints $247–252 (04:19–08:56 ET); after-hours tape
  steps down 227.81 → 225.42 → 221.5 → **220.71 (19:49 ET, NBBO 221.65/222)** —
  post-close selling pressure `[DP:extended_hours]`
- NBIS **not in the top-30** dark-pool ticker summary (leaders QQQ, SPY, MU,
  NVDA, SNDK) — heavy day for the name, heavier day for the AI complex around it
  `[DP:ticker_summary]`

## Detailed findings

### Largest blocks `[DP:largest]`

| Time (ET) | Price | Size | Premium | NBBO (bid/ask) | Read | % float |
|---|---|---|---|---|---|---|
| 17:22:28 | 227.81 | 136,487 | $31.09M | 225.10/226.28 | closing-price cross (AH) | 0.068% |
| 10:06:45 | 230.00 | 127,255 | $29.27M | 230.76/231.03 | **below bid — sell** | 0.063% |
| 12:49:20 | 223.75 | 38,100 | $8.52M | 223.22/223.36 | above ask — buy-side | 0.019% |
| 16:20:00 | 227.81 | 30,395 | $6.92M | 220.67/221.00 | closing-price print (AH) | 0.015% |
| 09:56:18 | 236.56 | 20,892 | $4.94M | 236.44/236.50 | above ask | 0.010% |
| 09:51:28 | 235.00 | 19,100 | $4.49M | 234.41/235.00 | at ask | 0.010% |
| 12:46 ×2 | 223.50 | 19,000×2 | $4.25M×2 | ~223.2/223.5 | paired mid prints | — |

Morning blocks (09:45–10:30 ET) printed 230–239 as the stock fell; midday blocks
clustered 221–223.75 near the lows; the two largest "227.81" prints are
benchmark crosses at the official close executed after hours.

### Tier breakdown `[DP:block_stratified]` (no `sell_ratio` field; derived = 1 − buy_ratio)

| Tier | Trades | Buy vol | Sell vol | buy_ratio | Premium |
|---|---|---|---|---|---|
| mega | 2 | 136,487 | 127,255 | 0.518 | $60.36M |
| block | 64 | 290,954 | 265,188 | 0.523 | $127.63M |
| large | 3,029 | 1,352,899 | 1,369,962 | 0.497 | $626.46M |
| **all tiers** | | | | | **$814.46M** |

Every tier is within ±0.03 of 0.50 — classification-confidence rules
(`>0.7 high-confidence`) mean this is a firmly **balanced** tape. Aggregate DP
shares ≈ 3.54M ≈ **1.76% of float** `[DP:block_pct_float fz]` — large
participation, zero directional skew.

### Price levels (5-day window) `[DP:price_levels]`

Window note: `--days 5` anchors to the latest available date (= as-of
2026-06-05; sessions 06-01…06-05 per phase-0 available-dates) — as-of-correct
for this run.

| Level | Premium | Shares | vs spot ($227.81) |
|---|---|---|---|
| 249.50 / 249.18 / 249.75 | $137.3M / $108.0M / $29.5M | 1.10M | +9.4% overhead |
| 251.68 | $122.4M | 486k | +10.5% overhead |
| 264.51 / 265.51 | $99.3M / $61.1M | 606k | +16% overhead |
| 259.67 / 260.58 / 259.00 | $87.7M / $48.9M / $25.8M | 625k | +14% overhead |
| **227.81** | **$41.1M** | 181k | **at spot — today's shelf** |
| 230.00 | $30.1M | 131k | +1.0% |

The week's institutional cost basis is 249–266. Spot has cut through every
cluster: holders from Mon–Thu are underwater — **overhead supply** on any
bounce toward 249–252, and nothing institutional below 227.81 to lean on.

### Extended-hours activity `[DP:extended_hours]`

- Premarket (04:19–08:56 ET): $247.00–251.75 prints (sizes 1,9k–3.6k) — the name
  opened from a ~$248–252 overnight level before the −9.5% session (phase-1
  intraday path $240.29 → $217.40).
- After-hours (16:00–19:49 ET): step-down sequence 227.81 (16:00) → 225.42
  (16:02) → 221.5 (16:29) → 220.2 (16:38) → **220.71 at 19:49 with NBBO
  221.65/222.00** — the market kept selling after the close. This is consistent
  with a post-close news catalyst (phase-6/7c must attribute; phase-1 open
  question stands).
- Largest AH prints are closing-price benchmark crosses (227.81 vs live NBBO
  ~221–226) — index/EOD rebalance mechanics, de-rated per pitfalls; the
  *live-priced* AH tape (220–225) is the directional tell.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw dark-pool largest --symbol NBIS --top-n 25 --sort-by premium --date 2026-06-05 --json` | top block 136,487 sh @227.81 $31,093,103.47 ← `.results[0].{size,price,premium}` | top-25 |
| `uw dark-pool block-stratified --symbol NBIS --top-n 30 --min-tier large --date 2026-06-05 --json` | mega.buy_ratio 0.518; block 0.523; large 0.497; total $814,456,252.34 ← `.results[] \| select(.ticker=="NBIS")` | 1 row |
| `uw dark-pool extended-hours --symbol NBIS --top-n 15 --date 2026-06-05 --json` | AH path 227.81→220.71; premarket 247–252 ← `.results[].{executed_at,price}` | top-15 |
| `uw dark-pool price-levels --symbol NBIS --top-n 15 --days 5 --json` | 249.5 $137,316,316; 251.68 $122,439,551; 227.81 $41,149,542 ← `.results[].{price_level,total_premium}` | top-15 |
| `uw dark-pool ticker-summary --top-n 30 --date 2026-06-05 --json` | NBIS absent; top-5 QQQ/SPY/MU/NVDA/SNDK ← `.results[].ticker` | top-30 |

## Tool errors

(none)

## DATA NOTE / CORRECTION

- The two largest prints carry price $227.81 against NBBO several dollars lower —
  they are official-close benchmark crosses (timestamps 16:20/17:22 ET), so the
  mega-tier buy_ratio (0.518, 2 trades) is mechanically near-meaningless;
  rely on the block/large tiers (0.523/0.497, 3,093 trades) for the balance read.

## Verdict for downstream phases

- **Accumulation / Distribution / Mixed:** **Mixed (balanced)** — no tier
  exceeds 0.55 either way; heavy two-way repricing, not stealth accumulation.
- **Conviction:** 2/5 (size is huge but skew is absent)
- **Largest block as % of float:** 0.068% (136,487 / 201.04M `fz`) — *not*
  meaningful conviction size for this name; aggregate DP ≈1.76% of float is the
  more telling number (institutions actively repricing the whole position set).
- **Three S/R levels for phase-9:**
  1. **$220.7–221.0** — after-hours low prints; first support / breakdown trigger.
  2. **$227.8–230.0** — today's close shelf + $41M/$30M clusters; pivot zone.
  3. **$249.2–251.7** — $367M of trapped weekly volume; major overhead supply.
- **Open questions:** What post-close catalyst kept the AH tape offered (phase
  6/7c WebSearch)? Does Monday's OI confirm the Jun-26 285P write phase-1
  flagged (phase 3)? Is the 249–266 trapped supply visible in OI walls too
  (phase 3/4)?
