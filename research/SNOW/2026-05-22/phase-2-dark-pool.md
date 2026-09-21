# Phase 2 — Dark Pool & Block Prints

**Ticker:** SNOW
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T15:30:00Z
**Upstream phases cited:** phase-0.5-context.md, phase-1-flow.md

## Summary

Dark-pool activity is **balanced and largely mechanical** — it neither confirms nor
refutes phase-1's flat directional read. SNOW printed $151.5M / 881k shares / 343
trades today [DP:block_stratified], **not in the market's top-30 DP names** (#30 IBM
= $743M), consistent with "busy, not a leader." The genuine intraday tell is mildly
constructive — large-tier (≥$100k) buy_ratio **0.604** on $71.5M — but it is offset
by the single **mega print being a SELL** (90,600 sh / $15.6M at the 5:00pm ET
close, below mid) and block-tier buy_ratio 0.472. Crucially, most of today's biggest
blocks executed **20:00–21:05 UTC (4–5pm ET) at $172.20 — closing-auction /
post-market prints**, which carry low directional information (de-rated per the
extended-hours pitfall). The durable signal is in the 5-day price levels: a **strong
institutional accumulation shelf at $163.5–$167** built over the prior sessions,
with price now at $172.20. Net: **mildly constructive support structure, no
distribution, but today's tape is mechanical — conviction low.**

## Key signals

- **Large-tier buy-lean:** ≥$100k tier buy_ratio **0.604** ($71.5M, 320 trades) —
  the only clean directional tilt, buyers paying up [DP:block_stratified].
- **Mega print is a sell:** lone mega trade 90,600 sh / **$15.6M @ $172.20**,
  21:00:34 UTC (5pm ET close), `trade_vs_mid −0.30` [DP:largest] — but it's a
  closing-auction print, not conviction distribution.
- **5-day support shelf $163.5–$167:** stacked levels $164.24 ($16.7M), $166.97
  ($16.1M), $165.54 ($13.9M), $164.44 ($13.5M), $163.50 ($13.4M), $164.31 ($11.6M)
  → **~$85M accumulated 3–5% below spot** [DP:price_levels].
- **Spot node $172.20:** $37.8M / 219k sh over 5 days, but heavily weighted to
  today's closing prints [DP:price_levels] — a pivot, not proven support.
- **Thin resistance:** only $174.29 ($7.7M) above spot in the 5-day book — little
  overhead supply printed off-exchange [DP:price_levels].

## Detailed findings

### Largest blocks (today)

| time (UTC) | price | size | premium | vs mid | note |
|------------|-------|------|---------|--------|------|
| 21:00:34 | 172.20 | 90,600 | $15.60M | −0.30 | mega; 5pm ET close (mechanical) |
| 14:49:23 | 171.27 | 40,600 | $6.95M | +0.24 | intraday, above mid (buy-lean) |
| 21:05:59 | 172.20 | 34,831 | $6.00M | +0.085 | post-close |
| 16:01:48 | 171.70 | 33,232 | $5.71M | −0.11 | intraday |
| 20:16:34 | 172.20 | 28,599 | $4.92M | −0.35 | post-close |
| 18:13:04 | 171.76 | 24,800 | $4.26M | −0.005 | intraday, at mid |

The intraday prints (14:49 +0.24, the 15:39–15:47 $171.5 cluster at/above mid)
lean buy; the post-close $172.20 prints are auction-benchmarked. Phase-1's biggest
*options* conviction print (the 2027 155P) finds **no corroborating dark-pool
distribution** — there is no block selling pressure to confirm a downside lean.

### Tier breakdown [DP:block_stratified]

| tier | trades | premium | buy_ratio | read |
|------|--------|---------|-----------|------|
| mega (≥$10M) | 1 | $15.6M | 0.00 | single closing sell |
| block (≥$1M) | 22 | $64.4M | 0.472 | slight sell-lean |
| large (≥$100k) | 320 | $71.5M | **0.604** | buy-lean (genuine intraday) |
| retail | 0 | $0 | — | — |

Mixed, with the small/mid institutional tier (large) buying and the one whale print
selling at the close. No tier exceeds the 0.7 high-confidence threshold → treat all
ratios as suggestive only.

### Price levels (5-day institutional S/R) [DP:price_levels]

- **Resistance:** $174.29 ($7.7M) — thin; then open air to the $280 52w-high.
- **Pivot / spot node:** $172.20 ($37.8M, but mostly today's closing prints) ·
  $172.36 ($7.7M).
- **Near support shelf:** $171.76 ($11.9M) · $171.70 ($9.8M) · $170.94 ($10.2M) ·
  $170.84 ($8.4M) · $171.27 ($7.1M) → a dense $170.8–$171.8 floor.
- **Major support / accumulation zone:** $163.50–$166.97 (six levels, ~$85M total)
  — institutions built this shelf 3–5% under spot before the recent rise.

### Extended-hours activity [DP:extended_hours]

Dominated by `extended_hours_trade` at $172.20 between 20:00–21:05 UTC (4–5pm ET):
the $15.6M, $6.0M, $4.9M, $3.3M, $1.28M blocks all at $172.20. This is
closing-auction / post-market benchmarked size, not pre-positioning ahead of an
overnight catalyst (earnings is 5 days out, not tonight). One late print at 23:23
UTC (7:23pm ET) $0.64M @ $172.26. **Flagged as mechanical — conviction de-rated.**

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `dark_pool_largest` | symbol=SNOW, top_n=25, sort=premium | mega $15.6M sell @172.20 close; intraday prints buy-lean |
| `dark_pool_block_stratified` | symbol=SNOW, min_tier=large | mega 0.00 / block 0.472 / large 0.604 buy_ratio |
| `dark_pool_extended_hours` | symbol=SNOW, top_n=15 | all $172.20 closing/post-market — mechanical |
| `dark_pool_price_levels` | symbol=SNOW, days=5 | support shelf $163.5–$167; near-floor $170.8–$171.8; thin resist $174.29 |
| `dark_pool_ticker_summary` | top_n=30, date=2026-05-22 | SNOW NOT in top-30 (mid-tier DP name) |

## Tool errors

(none)

## Verdict for downstream phases

- **Institutional bias:** **MIXED / mildly constructive.** Large-tier buy-lean
  (0.604) + a multi-day $163.5–$167 accumulation shelf = constructive base; but the
  whale print is a closing sell and today's tape is auction-mechanical → no strong
  signal either way.
- **Conviction:** **2/5** (de-rated: biggest prints are closing-auction; no tier
  clears 0.7; not a top-30 DP name).
- **Three S/R levels for phase-9:**
  1. **Major support $163.5–$167** — the 5-day institutional accumulation shelf;
     natural stop-reference floor and the level a post-earnings flush would test
     [DP:price_levels].
  2. **Near support / pivot $170.8–$172.2** — dense near-floor + spot node; loss of
     $170.8 on volume would be the first crack [DP:price_levels].
  3. **Resistance $174.29** — thin overhead; little off-exchange supply above, so an
     up-move has room if earnings catalyzes it [DP:price_levels].
- **Open questions:**
  - Does dealer positioning (OI) show the $163–167 shelf or the $172 node as a pin?
    → phase-3 `oi_pin_risk`.
  - Is the 8–45DTE mild-bullish options footprint (phase-1) backed by *opening* OI
    builds? → phase-3.
  - Where does GEX flip relative to the $170.8 near-floor into earnings? → phase-4.
