# Phase 2 — Dark Pool & Block Prints

**Ticker:** MSTR
**As-of date:** 2026-05-19 (effective)
**Generated:** 2026-05-20T00:10:00Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md

## Summary

The MSTR dark-pool tape on 2026-05-19 shows **mid-tier-block accumulation at
current spot ($165–$167)** with a `block_tier buy_ratio = 0.754` on $14.95M of
block premium, while the much larger `large_tier` ($181.5M premium, 918 trades)
is statistically balanced at `buy_ratio = 0.519`. No mega-tier prints today.
The 5-session price-level map reveals a critical structural fact: **institutions
own a $250M+ cost-basis band at $174–$179, currently ~5–8% above spot**, with
the single largest cluster at **$166.63 ($243.6M / 1.46M shares / 40 trades)** —
i.e. spot is right on top of the heaviest institutional level. The picture is
"mild accumulation here, but a lot of underwater institutional inventory
overhead" — supportive in the short term, capped in the medium term unless
catalyst breaks the $174–$179 zone.

## Key signals

- Block-tier (mid-block, ≥ $1M) **buy_ratio = 0.754** on $14.95M premium — clearest institutional smart-money signal of the day [DP:block_stratified]
- Total MSTR DP premium **$196.44M** across all tiers; MSTR does NOT appear in the top-30 market-wide ticker summary (cutoff ~$600M today), so MSTR's flow is normal-but-active, not headline-level [DP:ticker_summary]
- Largest single print: **12,100 shares @ $165.16, $1.998M premium, +$0.155 above NBBO mid** — clean intraday accumulation print [DP:largest]
- Top-5 prints (RTH only) all printed AT or ABOVE mid → bias toward buyer-initiated
- Heaviest 5-day price level: **$166.63 / $243.6M / 1.46M shares / 40 trades** — institutional anchor exactly at spot [DP:price_levels]
- Secondary cluster: **$178.03 / $140.4M / 789k shares / 36 trades** — institutional cost basis 7.5% above current spot

## Detailed findings

### Largest blocks (RTH + extended-hours combined, top 12 by premium)

| Time (UTC) | Size (sh) | Price ($) | NBBO mid ($) | trade_vs_mid | Premium ($M) | Read |
|-----------:|----------:|----------:|-------------:|-------------:|-------------:|------|
| 14:25:53 | 12,100 | 165.16 | 165.005 | +0.155 | 1.998 | BUY |
| 14:03:50 | 10,000 | 166.78 | 166.730 | +0.050 | 1.668 | BUY |
| 15:13:41 | 8,900  | 166.63 | 165.170 | +1.460 | 1.483 | BUY (catch-up print, $1.46 above current mid) |
| 15:14:00 | 8,900  | 165.28 | 165.175 | +0.105 | 1.471 | BUY |
| 15:21:04 | 7,800  | 165.05 | 165.160 | -0.110 | 1.287 | SELL |
| 18:57:31 | 7,500  | 164.81 | 164.895 | -0.085 | 1.236 | SELL (post-close) |
| 15:14:57 | 7,300  | 165.59 | 165.535 | +0.055 | 1.209 | BUY |
| 15:14:18 | 7,300  | 165.40 | 165.325 | +0.075 | 1.207 | BUY |
| 13:40:33 | 7,159  | 166.13 | 166.055 | +0.074 | 1.189 | BUY (RTH-open) |
| 13:31:25 | 6,897  | 164.13 | 164.500 | -0.370 | 1.132 | SELL |
| 15:55:30 | 6,500  | 164.50 | 164.485 | +0.015 | 1.069 | mild BUY |
| 13:26:50 | 6,100  | 163.50 | 163.425 | +0.075 | 0.997 | BUY (pre-open) |

Of top-12: **8 BUY, 3 SELL, 1 neutral**. Above-mid:below-mid premium ratio in the top-25 = roughly **2:1 buyer-initiated**. Spot during these prints ranged $163.30 – $166.85 (~2.2% intraday range).

### Tier breakdown

| Tier (boundary) | Trade count | Buy vol | Sell vol | Buy ratio | Total premium ($) |
|---|---:|---:|---:|---:|---:|
| Mega (≥ $10M) | 0 | 0 | 0 | n/a | 0 |
| Block ($1M – $10M) | 11 | 68,159 | 22,197 | **0.754** | 14,950,503 |
| Large ($100k – $1M) | 918 | 567,311 | 526,507 | 0.519 | 181,491,959 |
| Retail (< $100k) | n/a — excluded from query | — | — | — | — |
| **Total reported** | 929 | 635,470 | 548,704 | 0.536 | **196,442,461** |

Read: The institutional smart-money signal lives in the **block tier (0.754
buy ratio)** — this is the most reliable directional cue today. The much
larger `large` tier is essentially balanced (0.519), which is the dominant
weight of $196M total premium. Net call: **mild accumulation, conviction
3/5**, not a stampede.

### Price levels (5-session aggregation, ranked by premium)

| Rank | Price ($) | Premium ($M) | Shares | Trades | Distance from spot ($165.5) |
|---:|---:|---:|---:|---:|---:|
| 1 | **166.63** | **243.6** | 1,462,094 | 40 | +0.7% — **primary cluster, at-spot** |
| 2 | **178.03** | **140.4** | 788,666 | 36 | **+7.6% — institutional cost basis above** |
| 3 | 174.55 | 43.7 | 250,625 | 3 | +5.5% (likely 1 mega block + 2 prints) |
| 4 | 186.97 | 43.1 | 230,479 | 26 | +13.0% |
| 5 | 174.38 | 36.5 | 209,200 | **1** | +5.4% (single block) |
| 6 | 189.89 | 12.0 | 62,975 | 4 | +14.7% |
| 7 | 165.19 | 10.1 | 61,049 | 15 | -0.2% |
| 8 | 165.00 | 7.9 | 47,584 | 31 | -0.3% |
| 9 | 179.62 | 7.8 | 43,237 | 11 | +8.5% |
| 10 | 175.00 | 7.6 | 43,179 | 21 | +5.7% |
| 11 | 178.00 | 7.5 | 42,148 | 17 | +7.6% |
| 12 | 174.60 | 7.3 | 42,078 | 4 | +5.5% |
| 13 | 179.60 | 7.0 | 39,162 | 11 | +8.5% |
| 14 | 187.00 | 6.8 | 36,443 | 3 | +13.0% |
| 15 | 165.28 | 6.7 | 40,323 | 20 | -0.1% |

Band-aggregated read:
- **$164.50–$166.65 band:** ~$268M total premium across 4 levels — current accumulation zone, BEHAVES AS SUPPORT.
- **$174–$179 band:** ~$250M+ across 7 levels — institutional cost-basis band currently UNDERWATER by 5–8%. **This is the dominant overhead supply.** Any rally into this zone faces dis-investment risk from break-even sellers.
- **$186–$190 band:** ~$62M institutional zone — secondary resistance.

The structural picture: **buyers anchored at $166.63 (largest cluster of the entire 5-session window) and supply piled at $174–$179**. A sustained rally above $179.62 (top of underwater band) would change the regime — until then, the stock is "negotiating with its own institutional cost basis".

### Extended-hours activity

Top extended-hours prints on 2026-05-19:
- Pre-open (08:00 UTC): 2,500 sh @ $166.66, NBBO ask $168 / bid $167.50 — pre-open ASK-side print, modest size
- Pre-open (11:05 UTC): 1,100 sh @ $166.50 and 900 sh @ $166.83 — light pre-open prints, near top of NBBO
- Pre-open (11:53 UTC): 1,000 sh @ $164.98, NBBO bid $164.60 — mild buyer-initiated
- Pre-open (13:26 UTC): 6,100 sh @ $163.50, NBBO mid $163.43 — **largest extended-hours print**, buyer-initiated
- Post-close (18:57 UTC): 7,500 sh @ $164.81 (from RTH+post: technically inside RTH 9:30–16:00 ET; UTC 18:57 = 14:57 ET, so this is **intraday**, miscategorized in screen).

No genuine post-close (after 20:00 UTC / 16:00 ET) institutional prints reported in the top-15 — so **no overnight catalyst-driven block activity**. The pre-open tape is mildly buyer-initiated and benign.

### Cross-reference to phase-1

Phase-1 flagged the Oct 2026 $245C bullish position-opening ($2.36M premium, vol/OI 16.3) and the wing-OTM put IV outliers as the contradicting forces. The dark pool tape gives the **directional tiebreaker**: mid-tier-block buy ratio of 0.754 favors the bullish-flow camp, but the cap is unambiguous — institutions are NOT willing to chase the rally; they are accumulating only at or below the $174–$179 cost-basis ceiling.

The bearish put tape of phase-1 (deep-ITM put synthetic shorts at $250/$340/$400 strikes) does NOT have an obvious dark-pool corroboration — there is no concentrated dark-pool selling consistent with a coordinated short-positioning campaign. Net: phase-1 puts look like hedge / synthetic shorts to insulate long stock, not aggressive new shorts.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__dark_pool_largest` | `{symbol:MSTR, date:2026-05-19, sort-by:premium, top-n:25}` | 25 prints, top $1.998M |
| `mcp__uw-pp__dark_pool_block_stratified` | `{symbol:MSTR, date:2026-05-19, min-tier:large, top-n:30}` | 1 row: MSTR — block buy_ratio 0.754, large 0.519 |
| `mcp__uw-pp__dark_pool_extended_hours` | `{symbol:MSTR, date:2026-05-19, top-n:15}` | 15 ext-hours prints, top $997k |
| `mcp__uw-pp__dark_pool_price_levels` | `{symbol:MSTR, date:2026-05-19, days:5, top-n:15}` | 15 levels, top $243.6M @ $166.63 |
| `mcp__uw-pp__dark_pool_ticker_summary` | `{date:2026-05-19, top-n:30}` | MSTR not in top-30 (cutoff $608M); MU/QQQ/SPY/NVDA dominate |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** **mild accumulation** (block-tier buy_ratio 0.754) anchored at $166.63 cluster, but with significant overhead institutional supply at $174–$179.
- **Conviction:** **3/5** — clean buy-skew in block tier; balanced in large tier; no mega prints. Not a "whale loading up" signal but supportive.
- **Three S/R levels phase-9 must use:**
  1. **Pivot / anchor:** **$166.63** — heaviest 5-session cluster; the institutional center-of-gravity.
  2. **Support:** **$163.30 – $164.50** — extended-hours bid zone + downside intraday range. Loss of $163 would invalidate the accumulation read.
  3. **Resistance band:** **$174 – $179.62** — institutional underwater cost-basis band, $250M+ premium. Until cleared on volume, any rally is selling-supply target.
  4. (Bonus) **Upper resistance:** **$186 – $190** — secondary institutional zone, $62M.
- **Open questions:**
  - The 36–40-trade clusters at $166.63 and $178.03 — were these accumulated this week or earlier in the 5-session window? (May change time-decay of supply.) Phase-5 (historical OI/flow trend) should triangulate.
  - The block-tier sell prints (3 of top 12) — was this single seller? If so, are they done? (No way to tell from tape alone; phase-3 OI changes may hint.)
  - No mega prints today. Is this normal for MSTR or a quiet day? Phase-5 historical context required.
