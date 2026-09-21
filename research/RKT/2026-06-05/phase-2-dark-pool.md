# Phase 2 — Dark Pool & Block Prints

**Ticker:** RKT
**As-of date:** 2026-06-05
**Generated:** 2026-06-06T17:05:00-04:00
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md, phase-1-flow.md

## Summary

RKT printed **$101.38M of off-exchange premium** on 2026-06-05, but the headline
is one print: a **5,821,043-share / $73.64M block at $12.65 executed 20:00:28Z**
(16:00:28 ET — at the closing bell, tagged `extended_hours_trade`), classified
buy-side (above mid). Stripped of that closing cross, the intraday tape leans
**distribution**: the block tier's derived sell_ratio is **0.883** (high-
confidence), prints tracked the stock down from ~$12.95 to ~$12.53, and the
5-day price-level map shows every major cluster **at or above** today's $12.65
close — no dark-pool support shelf below spot. This corroborates phase-1's
near-term bearish tilt (derived net_flow −$209,751, phase-1-flow.md §Whole-tape).
Confluence contribution capped at `+` per phase-0.5 `[CTX:]` BUSY_NAME_NORMAL_DAY.

## Key signals

- Mega-tier: 1 trade, `buy_ratio` 1.0, 5,821,043 sh / $73,636,193.95 @ $12.65 at
  20:00:28Z — a **closing-bell cross** (NBBO 12.59×12.68, trade_vs_mid +0.015);
  classification de-rated per pitfall (closing prints ≠ directional intent)
  [DP:block_stratified + largest]
- Block-tier derived sell_ratio **0.883** (buy_volume 82,717 vs sell_volume
  625,257; no `sell_ratio` field — derived 1−buy_ratio) — high-confidence
  intraday distribution [DP:block_stratified]
- Large-tier buy_ratio 0.561 (buy 823,122 / sell 643,691, 76 trades, $18.72M) —
  suggestive-only (0.55–0.7 band) [DP:block_stratified]
- 5-day price levels: $12.94 ($128.0M / 9.89M sh) and $13.23 ($123.9M / 9.37M sh)
  dominate — **both above spot**; nothing below $12.65 in the top-15
  [DP:price_levels]
- Mega block = **0.61% of float** (5,821,043 / 960.91M float, phase-0-intake.md
  §Finviz) — sizeable for one print but consistent with a benchmark/closing
  cross, not stealth accumulation [DP:block_pct_float fz]
- RKT **outside top-30** on the day's DP ticker board (QQQ/SPY/MU lead) —
  activity elevated for the name, not for the tape [DP:ticker_summary]

## Detailed findings

### Largest blocks (top 10 of 25, `--sort-by premium`)

| Time (UTC) | Price | Size | Premium | NBBO (bid×ask) | vs mid | % float |
|---|---|---|---|---|---|---|
| 20:00:28 | 12.65 | 5,821,043 | $73,636,194 | 12.59×12.68 | +0.015 | 0.606% |
| 20:06:01 | 12.65 | 405,557 | $5,130,296 | 12.66×12.68 | **−0.020** | 0.042% |
| 14:03:25 | 12.95 | 219,700 | $2,845,115 | 12.96×12.97 | **−0.015** | 0.023% |
| 20:00:38 | 12.65 | 82,717 | $1,046,370 | 12.59×12.68 | +0.015 | 0.009% |
| 13:56:11 | 12.875 | 77,500 | $997,813 | 12.87×12.88 | 0.000 | |
| 16:27:19 | 12.90 | 71,984 | $928,594 | 12.90×12.91 | −0.005 | |
| 13:49:55 | 12.955 | 68,972 | $893,532 | 12.95×12.96 | 0.000 | |
| 19:02:00 | 12.53 | 54,599 | $684,125 | 12.53×12.54 | −0.005 | |
| 19:38:59 | 12.54 | 52,991 | $664,507 | 12.54×12.55 | −0.005 | |
| 17:52:24 | 12.63 | 48,000 | $606,240 | 12.63×12.64 | −0.005 | |

Pattern: of the ten largest, **7 printed at or below mid** (sell-classified),
including the two largest non-closing prints (405k @ 20:06 below mid; 219.7k @
14:03 below mid). The below-mid prints walk down with the tape (12.95 → 12.53),
i.e. supply was being worked off-exchange during the slide phase-1 flagged
(underlying 12.98 → 12.505, phase-1-flow.md §Whole-tape).

### Tier breakdown (`block-stratified`; sell_ratio derived = 1 − buy_ratio)

| Tier | trades | buy_volume | sell_volume | buy_ratio | derived sell_ratio | total_premium |
|---|---|---|---|---|---|---|
| mega | 1 | 5,821,043 | 0 | 1.000 | 0.000 | $73,636,194 |
| block | 3 | 82,717 | 625,257 | 0.117 | **0.883** | $9,021,781 |
| large | 76 | 823,122 | 643,691 | 0.561 | 0.439 | $18,718,654 |
| retail | 0 | 0 | 0 | — | — | $0 |
| **all tiers** | | | | | | **$101,376,629** |

Confidence per pitfall thresholds: block-tier sell 0.883 = high-confidence;
large-tier buy 0.561 = suggestive only; mega-tier 1.0 rests on a single
closing-bell print — treated as **unclassifiable benchmark volume**, not a buy
signal.

### Price levels (5-day window — caveat: `--days` anchors to latest available
date = 2026-06-05 = as-of, so window is 2026-06-01→06-05, valid vs phase-0's
date list)

| Level | Premium | Shares | Trades | vs spot $12.65 |
|---|---|---|---|---|
| **12.94** | $127,989,857 | 9,891,043 | 14 | +2.3% overhead |
| **13.23** | $123,944,708 | 9,368,536 | 22 | +4.6% overhead |
| **12.65** | $80,966,009 | 6,400,475 | 8 | **at spot** (today's close shelf) |
| 13.17 | $27,156,829 | 2,061,370 | 5 | +4.1% |
| 14.03 | $9,513,276 | 678,062 | 9 | +10.9% |
| 13.22–13.26 (band w/ 13.23) | ~$136.1M combined | | 63 | +4.5–4.8% |
| 12.95–12.96 (band w/ 12.94) | ~$135.2M combined | | 30 | +2.3–2.5% |
| 13.40/13.41 | $7.5M combined | | 8 | +5.9% |
| 14.18/14.27 | $7.6M combined | | 20 | +12% |

Two heavy institutional bands overhead — **$12.94–12.96 (~$135M)** and
**$13.17–13.26 (~$163M)** — and **no cluster below $12.65** in the top 15. The
overhead bands are where the stock traded earlier in the week, i.e. trapped/
transacted supply above, thin documented support below.

### Extended-hours activity

10 prints; 8 are the 20:00:03–20:00:44Z cluster at $12.65 (closing-bell
mechanical tags) + one 20:06:01Z below-mid $5.13M sale. Genuine pre-market: one
print 12:33:57Z (08:33 ET), 10,000 sh @ $12.8601. **No catalyst-style
pre/post-market positioning detected**; the extended-hours premium is closing
volume. Phase-6 should still check for index-rebalance news (June MSCI/FTSE
windows) to attribute the closing cross.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw dark-pool largest --symbol RKT --top-n 25 --sort-by premium --date 2026-06-05 --json` | blocks ← `.results[]` | 25 |
| `uw dark-pool block-stratified --symbol RKT --top-n 30 --min-tier large --date 2026-06-05 --json` | tier ratios ← `.results[].mega.buy_ratio` etc.; sell_ratio derived 1−buy_ratio (no such field) | 1 ticker row |
| `uw dark-pool extended-hours --symbol RKT --top-n 15 --date 2026-06-05 --json` | 10 prints ← `.results[]` | 10 |
| `uw dark-pool price-levels --symbol RKT --top-n 15 --days 5 --date 2026-06-05 --json` | levels ← `.results[]` | 15 |
| `uw dark-pool ticker-summary --top-n 30 --date 2026-06-05 --json` | outside top-30 ← `.results \| map(.ticker) \| index("RKT")` = null | top-30 |

## Tool errors

None.

## DATA NOTE / CORRECTION

None — first read stood.

## Verdict for downstream phases

- **Accumulation / Distribution / Mixed:** **Mixed, leaning distribution
  intraday** — block tier sold 0.883 high-confidence, biggest non-closing prints
  below mid on a falling tape; the $73.6M "buy" mega print is a closing cross and
  doesn't offset that. No evidence of quiet accumulation below spot.
- **Conviction:** 2/5 (one-day read; capped at `+` by `[CTX:]` anyway)
- **Largest block as % of float:** 0.606% of 960.91M float
  [DP:block_pct_float fz] — meaningful size in the abstract, but its
  closing-bell timestamp and at-close price make it benchmark-flow-like, not a
  conviction print for this name.
- **Three S/R levels for phase 9:**
  1. **$12.65** — today's close shelf ($81.0M, 6.4M sh, incl. the mega cross);
     first reference; a close below it has no DP shelf beneath.
  2. **$12.94–12.96** — ~$135M transacted band, nearest overhead resistance.
  3. **$13.17–13.26** — ~$163M band, the week's heaviest supply zone.
- **Open questions:** Was the 4pm cross index/rebalance-driven (phase-6 news
  check)? Does OI structure put dealer support/pin anywhere near $12.5–12.65
  (phase 3)? Phase-1's $14.5 call-sale cap + DP overhead bands at $12.94/$13.23
  — does positioning agree the upside is capped (phase 3/4)?
