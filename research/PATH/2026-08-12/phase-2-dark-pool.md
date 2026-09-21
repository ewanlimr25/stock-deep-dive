# Phase 2 — Dark Pool & Block Prints

**Ticker:** PATH
**As-of date:** 2026-08-12
**Generated:** 2026-08-13T01:45:00Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md, phase-1-flow.md

## Summary

Total dark-pool premium for PATH today is $306.42M — two orders of magnitude
below the market's dark-pool leaders (MU $8.62B, SPY $8.25B; PATH is absent
from the ticker-summary top-30), consistent with phase-0.5's
`BUSY_NAME_NORMAL_DAY` read. The `mega` tier (100% buy_ratio) is a **single
3.10M-share, $47.25M after-hours print** tagged `extended_hours_trade` at
21:03 UTC amid a cluster of same-price ($15.26), wide-NBBO-spread prints right
at and after the close — the known **closing/extended-hours print artifact**
pattern (`[[darkpool-closing-auction-artifact]]` memory) — and is de-weighted
per that precedent. **Stripped of the mega print, the `large` tier alone
(2,014 trades, $259.17M premium) still shows a moderate buy-side tilt
(`buy_ratio=0.678`)** — "suggestive," not high-confidence, per this phase's own
threshold rubric. 5-day price-level clustering shows dark-pool premium
concentrated near and just above current spot with a rising trend from ~$13.9
to ~$15.5 over the window. Net read: **mild accumulation**, low-to-moderate
conviction.

## Key signals

- `mega` tier: 1 trade, 3,096,277 shares, $47.25M premium, `buy_ratio=1.0` —
  **flagged as extended-hours print artifact, de-weighted** [DP:block_stratified]
- `large` tier ex-mega: 2,014 trades, $259.17M premium, `buy_ratio=0.678`
  (buy_volume 11.54M vs sell_volume 5.49M) — moderate, suggestive-tier
  accumulation signal [DP:block_stratified]
- Mega print = **0.79% of float** ($3,096,277 / 390.80M shares); large-tier buy
  volume alone = **2.96% of float** [DP:block_pct_float fz]
- 5-day price levels cluster in three bands: near-spot $15.19–15.54 (bulk of
  premium), a mid support $14.86–14.87, and a lower support $13.89–13.93 —
  price has trended up through the window [DP:price_levels]
- PATH absent from market-wide `ticker-summary` top-30 (PATH total $306M vs.
  MU's $8.62B leader) — not a dark-pool-active name today [DP:ticker_summary]

## Detailed findings

### Largest blocks

`uw dark-pool largest --top-n 25 --sort-by premium` (top 6 of 25):

| Time (UTC) | Price | Size | Premium | trade_vs_mid | % of float |
|---|---|---|---|---|---|
| 21:03:32 | $15.26 | 3,096,277 | $47,249,187 | +0.085 (wide AH NBBO) | 0.79% |
| 14:05:15 | $15.08 | 58,791 | $886,568 | -0.005 | 0.015% |
| 18:58:41 | $15.2699 | 49,009 | $748,363 | -0.005 | 0.013% |
| 19:51:02 | $15.385 | 34,449 | $529,998 | ~0.00 | 0.009% |
| 17:43:55 | $15.221 | 24,854 | $378,303 | -0.004 | 0.006% |
| 14:14:42 | $15.26 | 20,100 | $306,726 | +0.005 | 0.005% |

The 21:03:32 print dwarfs everything else by ~53×. `nbbo_bid/ask` at that
timestamp (15.15/15.20, spread $0.05) is roughly 5× the regular-session spread
seen on the other prints (~$0.01), and it lands inside a cluster of five other
prints at 20:00:02–20:00:25 UTC — literally seconds after the 16:00 ET close —
all printed at the identical $15.26 with similarly wide NBBO. This is the same
signature the `HOOD` re-mark flagged: a delayed/negotiated block reported
against a stale, wide after-hours quote, not a real-time aggressive buy.
`trade_vs_mid` buy classification on a wide, post-close NBBO is low-confidence
per this phase's own pitfalls rubric.

### Tier breakdown

`uw dark-pool block-stratified --min-tier large` (`.results[]`, no `sell_ratio`
field — derived `1 − buy_ratio`):

| Tier | Trades | Buy vol | Sell vol | Buy ratio | Derived sell ratio | Premium |
|---|---|---|---|---|---|---|
| mega | 1 | 3,096,277 | 0 | 1.000 | 0.000 | $47,249,187 |
| large | 2,014 | 11,544,887 | 5,491,602 | 0.678 | 0.322 | $259,172,799 |
| block | 0 | 0 | 0 | 0.500 (no data) | — | $0 |
| retail | 0 | 0 | 0 | 0.500 (no data) | — | $0 |

`total_premium_all_tiers = $306,421,986` = mega + large exactly.

**Session-decomposed read (per memory precedent — never call accumulation off
a raw mega-tier ratio without checking session):** excluding the single
after-hours mega print, the `large` tier's `buy_ratio=0.678` across 2,014
regular-session trades is the reliable number — solidly in the "suggestive"
0.55–0.7 band, not the "high-confidence" >0.7 band. If the mega print is
included at face value, the blended buy_ratio rises to 0.727 (14,641,164 /
20,132,766) — but that overstates confidence given the artifact flag above.

### Price levels (5-day, `--days 5`, dates covered 2026-08-06→08-12)

Top clusters by premium:

| Price level | Total premium | Shares | Trades | vs. spot ($15.26) |
|---|---|---|---|---|
| $15.26 | $67.23M | 4,406,064 | 156 | at spot (includes the mega print) |
| $15.51 | $33.31M | 2,147,967 | 252 | +1.6% |
| $15.52 | $29.47M | 1,899,289 | 223 | +1.7% |
| $15.54 | $24.03M | 1,546,604 | 180 | +1.8% |
| $15.50 | $23.92M | 1,543,650 | 184 | +1.6% |
| $15.19–15.21 | ~$65.77M combined | ~4.33M combined | ~528 | -0.3% to -0.5% |
| $13.89–13.93 | ~$62.37M combined | ~4.48M combined | ~508 | -8.9% to -9.0% |
| $14.86–14.87 | ~$40.38M combined | ~2.72M combined | ~313 | -2.6% |

Three bands: **near-spot congestion** ($15.19–15.54, the bulk of 5-day
premium), a **mid support shelf** ($14.86–14.87, -2.6%), and a **lower support
shelf** ($13.89–13.93, -8.9%) — the latter marking where price traded before
the run-up into the current $15.19–15.54 congestion zone. Read: price has
trended up through the window and institutional dark-pool activity followed it
up rather than fading it, consistent with (not proof of) accumulation into
strength.

### Extended-hours activity

`uw dark-pool extended-hours --top-n 15`: 9 rows, all tagged
`extended_hours_trade`. Besides the mega print already covered, a cluster of
5 prints at 20:00:02–20:00:25 UTC (i.e., seconds after the close) all print at
$15.26 with abnormally wide NBBO (bid/ask spreads of $0.25–$0.85 vs. ~$0.01
intraday) — textbook closing/settlement-cross reporting artifacts, not fresh
institutional intent. A smaller pair of prints at 11:09–11:10 UTC (07:09–07:10
ET, pre-market) at $15.51/$15.55 (7,775–10,000 shares each, $120K–$155K
premium) look more like genuine pre-market institutional orders, but are
small.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw dark-pool largest --symbol PATH --top-n 25 --sort-by premium --date 2026-08-12 --json` | top block $47.25M ← `.results[0]` | 25 |
| `uw dark-pool block-stratified --symbol PATH --top-n 30 --min-tier large --date 2026-08-12 --json` | `mega.buy_ratio=1, large.buy_ratio=0.678` ← `.results[0].{mega,large}.buy_ratio` | 1 |
| `uw dark-pool extended-hours --symbol PATH --top-n 15 --date 2026-08-12 --json` | 9 rows, mega print confirmed `ext_hour_sold_codes=extended_hours_trade` ← `.results[]` | 9 |
| `uw dark-pool price-levels --symbol PATH --top-n 15 --days 5 --date 2026-08-12 --json` | 15 price-level rows ← `.results[]` | 15 |
| `uw dark-pool ticker-summary --top-n 30 --date 2026-08-12 --json` | PATH absent ← `.results[].ticker` | 30 |
| (phase-0 carry) `fz screen --tickers PATH --view ownership` | `Float=390.80M` | 1 |

## Tool errors

<none>

## DATA NOTE / CORRECTION

<none — first read stood>

## Verdict for downstream phases

- **Accumulation / Distribution / Mixed:** **Mild accumulation** (large-tier
  buy_ratio=0.678, suggestive not high-confidence; price-level trend rising
  into a near-spot congestion zone). The raw mega-tier 100% buy read is
  explicitly discounted as an after-hours reporting artifact.
- **Conviction:** 2/5 (large-tier ratio is only "suggestive"; PATH is not a
  dark-pool-active name today per ticker-summary; capped further by
  phase-0.5's `BUSY_NAME_NORMAL_DAY`)
- **Largest block as % of float:** 0.79% (mega print, artifact-flagged) / 2.96%
  (large-tier buy volume alone) — meaningful size for a 390.8M-float name, but
  the largest single print's provenance is the weakest part of today's read.
- **Three S/R levels for phase-9:**
  1. Near-spot congestion / pivot: **$15.19–15.54** (current trading zone)
  2. First support below: **$14.86–14.87** (-2.6%)
  3. Second support below: **$13.89–13.93** (-8.9%, prior base before the
     run-up)
- **Open questions:** Does phase-3 OI-by-strike show open interest building at
  strikes near the $15.50 resistance cluster (would corroborate the dark-pool
  read)? Is the after-hours mega print attributable to a known
  index/ETF-rebalance event (phase-6 should check the macro calendar for
  8/12 close)?
