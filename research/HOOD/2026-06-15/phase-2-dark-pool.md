# Phase 2 — Dark Pool & Block Prints

**Ticker:** HOOD
**As-of date:** 2026-06-15
**Generated:** 2026-06-16T11:58:00Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md, phase-1-flow.md

## Summary

Dark pool reads **net accumulation**, which reframes phase-1's large puts as likely
hedges rather than standalone bearish bets. Tier buy/sell ratios all lean buy —
**block-tier buy_ratio 0.85** ($68.7M), **mega-tier 1.0** (the single 132k-share
$12.95M closing block was a buy), **large-tier 0.581** ($415.7M, the bulk) — and the
top-25 individual blocks print **$71M above mid vs $11M below mid**. The catch: the
dominant large tier is only *suggestively* buy (0.58, mid-band), HOOD is **outside
the market's top-30** dark-pool names (SPY/MU/QQQ/NVDA lead), and every block is tiny
vs HOOD's **760.74M float** (mega block = 0.017% of float) — so this is *broad,
distributed* accumulation, not concentrated whale conviction. Multi-day price levels
show an institutional base at **$83.77–$86.36** (~$121M) and near support at
**$92–93** (~$57M), both below the $98.12 spot.

## Key signals

- Block-tier **buy_ratio 0.85** (buy 592,992 vs sell 104,925 sh, $68.7M) — high-conf
  accumulation `[DP:block_stratified]`.
- Mega-tier **buy_ratio 1.0** — the day's biggest block, **132,000 sh @ $98.12 =
  $12.95M**, was a buy `[DP:block_stratified][DP:largest]`.
- Large-tier (bulk) **buy_ratio 0.581** on $415.7M — suggestive buy, not decisive
  `[DP:block_stratified]`.
- Top-25 blocks aggressor lean **buy**: 17 above-mid ($71M) vs 7 below-mid ($11M)
  `[DP:largest]`.
- Institutional base at **$83.77 ($58.8M) / $86.36 ($62.3M)** and support **$92–93
  (~$57M)** — all below $98.12 spot `[DP:price_levels]`.

## Detailed findings

### Largest blocks `[DP:largest]` (all @ $98.12 close; spot $98.12)

| Time (UTC) | Price | Size (sh) | Premium | % of float |
|------------|-------|-----------|---------|-----------|
| 20:00:18 | $98.12 | 132,000 | $12.95M | 0.017% |
| 20:00:26 | $98.12 | 74,213 | $7.28M | 0.010% |
| 20:00:07 | $98.12 | 71,887 | $7.05M | 0.009% |
| 20:00:27 | $98.12 | 70,381 | $6.90M | 0.009% |
| 21:03:47 | $98.12 | 70,381 | $6.90M | 0.009% |
| 20:49:46 | $98.12 | 50,047 | $4.91M | 0.007% |

Top-25 total **$83M**. All print at the $98.12 close — these are **closing-auction /
MOC crosses** (20:00 UTC = 16:00 ET) plus one 17:03 ET after-hours print, not
intraday directional sweeps. `[DP:block_pct_float fz]` — even the mega block is only
**0.017% of the 760.74M float**; no single print is whale-sized for this name.

### Tier breakdown `[DP:block_stratified]` (sell_ratio = 1 − buy_ratio)

| Tier | buy_ratio | sell_ratio | buy_vol | sell_vol | total_premium |
|------|-----------|-----------|---------|----------|---------------|
| mega | **1.00** | 0.00 | 132,000 | 0 | $12.95M |
| block | **0.85** | 0.15 | 592,992 | 104,925 | $68.73M |
| large | **0.581** | 0.419 | 2,434,927 | 1,752,862 | $415.66M |
| retail | 0.50 | 0.50 | 0 | 0 | $0 |

All-tier premium ≈ **$497M**. Net buy volume ≈ +1.30M shares (≈0.17% of float).
Read: clear buy *lean* across all tiers, but the $415.7M that dominates sits at 0.581
(mid-band "suggestive only" per the rubric) — accumulation is broad and probabilistic,
not high-conviction. mega 1.0 / block 0.85 are stronger but carry far less premium.

### Price levels (5-day clusters) `[DP:price_levels]`

| Level | Premium | Shares | vs spot ($98.12) |
|-------|---------|--------|------------------|
| $98.12 | $70.8M | 721,626 | at spot (today's prints) |
| $86.36 | $62.27M | 721,158 | −12% (base) |
| $83.77 | $58.76M | 701,550 | −15% (base) |
| $92.23 | $43.6M | 472,793 | −6% (support) |
| $93.10–93.19 | ~$34M | ~369k | −5% (support) |
| $99.72 / $100.53 | $5.88M / $5.83M | ~117k | +2% (light supply) |

The heavy $83.77–$86.36 base (~$121M) aligns with phase-1's $85 strike (the $5.54M
LEAP put + $85C 7/17 ITM calls) — institutional cost basis there. Near support
$92–93 (~$57M). Thin supply just above at $99.72–$100.53 (≈ phase-1's $100 call wall).
⚠️ `--days 5` anchors to the latest date, so these clusters span 06-09→06-15 (matches
phase-0 available dates; no gap).

### Extended-hours `[DP:extended_hours]`

$64M total — but it is the **same closing-auction block set** (132k @ 20:00:18, etc.,
all $98.12) surfaced under the ext-hours view, plus the 21:03 ET print. No distinct
overnight news-driven distribution/accumulation; this is the close cross, already
counted. No de-rate beyond noting it isn't *separate* directional intent.

### Market context `[DP:ticker_summary]`

HOOD is **outside the dark-pool top-30** today. Leaders are index ETFs + MU
(SPY $17.2B, MU $14.6B, QQQ $12.3B, NVDA $9.0B, IVV $7.4B, VOO $7.0B). HOOD's ~$497M
all-tier DP premium is real but not a market-leading footprint.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|------------------|--------------------------|-----------|
| `uw dark-pool largest --symbol HOOD --top-n 25 --sort-by premium --date 2026-06-15` | 132k@$98.12 $12.95M largest; 17 above-mid $71M vs 7 below $11M ← `select(.trade_vs_mid>0).premium` | top-25 |
| `uw dark-pool block-stratified --symbol HOOD --top-n 30 --min-tier large --date 2026-06-15` | mega 1.0 / block 0.85 / large 0.581 ← `.results[0].<tier>.buy_ratio` | 1 (tiered) |
| `uw dark-pool price-levels --symbol HOOD --top-n 15 --days 5 --date 2026-06-15` | base $83.77/$86.36, support $92–93 ← `.results[].price_level` | top-15 |
| `uw dark-pool extended-hours --symbol HOOD --top-n 15 --date 2026-06-15` | $64M = same close cross | top-15 |
| `uw dark-pool ticker-summary --top-n 30 --date 2026-06-15` | HOOD outside top-30 ← `index("HOOD")==null` | top-30 |

## Tool errors

(none — all five reads returned valid JSON.)

## DATA NOTE / CORRECTION

- price-levels field is `price_level` (not `price`/`level`); initial jq used the wrong
  key and returned `px=null` — re-extracted with `.price_level`. No null transcribed.
- `block-stratified` has no `sell_ratio` (confirmed); derived `1 − buy_ratio` per rubric.

## Verdict for downstream phases

- **Net institutional bias:** **ACCUMULATION** (broad/distributed) — all tiers buy-lean,
  top blocks above mid. Reframes phase-1's large puts as **likely hedges on long stock**,
  not standalone bearish bets.
- **Conviction:** **3 / 5** — direction is clearly buy, but the dominant $415.7M large
  tier is only 0.581 (suggestive), HOOD is outside the DP top-30, and no block is large
  vs float.
- **Largest block as % of float:** **0.017%** (132k sh / 760.74M) — *not* meaningful in
  isolation for this large-float name; the signal is the consistent buy lean across many
  blocks, not concentrated size (advisory; de-rate single-print conviction).
- **Three S/R levels for phase-9:**
  1. **$92–93** — near support (~$57M DP, −5/6%) → stop-reference zone.
  2. **$83.77–$86.36** — institutional base (~$121M DP, −12/15%); aligns with $85 strike
     (phase-1 LEAP put + ITM calls) → deeper structural support.
  3. **$99.72–$100.53** — light supply just above spot; aligns with $100 call wall
     (phase-1) → first resistance / breakout trigger.
- **Open questions:** Does phase-3 OI show a $100 call wall (capping) and a $85/$90 put
  wall (matching the DP base)? Is the large-tier 0.581 buy lean improving or fading vs
  prior sessions (phase-5 historical)?
