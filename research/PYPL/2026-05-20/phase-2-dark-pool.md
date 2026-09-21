# Phase 2 — Dark Pool & Block Prints

**Ticker:** PYPL
**As-of date:** 2026-05-19
**Generated:** 2026-05-20T00:15:00-04:00
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md

## Summary

Dark pool tape is **clearly institutionally accumulative**, which breaks the
mixed-flow tie from phase 1. Two morning mega-prints totaling **$29.64M
($17.82M @ $44.00 and $11.82M @ $44.23, both at/above NBBO ask) hit within 8
minutes of the open with `buy_ratio = 1.0` in the mega tier** — every dollar
of mega-tier dark pool activity was on the bid-lift side. The block tier
($1–10M) showed mild distribution (`buy_ratio = 0.286`), but the larger
mega number dominates. Five-day institutional price clusters sit **above
spot** at $44.39 → $45.04 → $45.23, suggesting natural support pull from
existing institutional inventory. This is the first clean directional signal
in the chain and offsets phase 1's near-term put concentration.

## Key signals

- **Mega-tier (≥$10M) buy_ratio = 1.0 on $29.64M / 2 trades**
  [DP:dark_pool_block_stratified:2026-05-19] — 100% accumulation, no offsetting
  mega-sell.
- **$17.82M dark print at $44.00, 405,000 shares, 13:37:42Z (market open +7min),
  +$0.085 vs NBBO mid of $43.915** [DP:dark_pool_largest:2026-05-19] — printed
  ABOVE the offer, unambiguous institutional buy.
- **$11.82M dark print at $44.23, 267,233 shares, 13:45:38Z, +$0.005 vs mid
  ($44.225)** [DP:dark_pool_largest:2026-05-19] — at the ask, second leg of
  the same morning accumulation campaign.
- **5-day high-volume node = $44.39 ($37.1M / 836K shares / 15 trades)**
  [DP:dark_pool_price_levels:2026-05-13..19] — institutional gravity center
  sits $0.51 ABOVE spot $43.88 → natural support pull.
- **Block tier ($1–10M) buy_ratio = 0.286 (71% sell), $7.92M, 3 trades**
  [DP:dark_pool_block_stratified] — caveat to the bull story, mid-tier
  institutions are partially trimming.
- **PYPL absent from market-wide DP top 100 by total premium**
  [DP:dark_pool_ticker_summary] — $66M total is real but not exceptional; the
  signal is in the COMPOSITION (mega-tier one-sidedness) not the magnitude.

## Detailed findings

### Largest blocks (top 12)

| Time UTC | Size | Price | Premium | NBBO mid | vs mid | Read |
|----------|------|-------|---------|----------|--------|------|
| 13:37:42 | 405,000 | $44.00 | $17,820,000 | $43.915 | +$0.085 | **MEGA BUY** at/above offer |
| 13:45:38 | 267,233 | $44.23 | $11,819,716 | $44.225 | +$0.005 | **MEGA BUY** at ask |
| 15:04:30 | 78,576 | $44.45 | $3,492,703 | $44.455 | −$0.005 | Slight sell, near mid |
| 13:45:38 | 51,022 | $44.23 | $2,256,703 | $44.225 | +$0.005 | Block buy, same 13:45 cluster |
| 15:40:55 | 48,905 | $44.32 | $2,167,470 | $44.355 | −$0.035 | Sell, 3.5c below mid |
| 14:14:02 | 13,500 | $44.705 | $603,518 | $44.705 | $0     | Neutral, at mid |
| 14:47:29 | 11,613 | $44.66 | $518,637 | $44.665 | −$0.005 | Neutral |
| 14:12:28 | 11,074 | $44.68 | $494,786 | $44.675 | +$0.005 | Slight buy |
| 14:14:35 | 10,000 | $44.7499 | $447,499 | $44.735 | +$0.0149 | Mild buy |
| 18:33:30 | 10,000 | $44.1199 | $441,199 | $44.115 | +$0.0049 | Mild buy |
| 19:30:00 | 9,652  | $44.06   | $425,267 | $44.055 | +$0.005 | Mild buy late |
| 14:28:04 | 9,102  | $44.75   | $407,315 | $44.745 | +$0.005 | Mild buy |

[DP:dark_pool_largest:2026-05-19]. The two morning mega-prints account for
**$29.64M of the $66M total daily dark pool premium = 44.9% of the entire
day's institutional flow in a single 8-minute window, all on the buy side.**

### Tier breakdown (single-day stratification)

```
mega   (≥$10M):   2 trades   |  $29,639,716 | buy_ratio 1.000  |  100% BUY
block  ($1–10M):  3 trades   |  $7,916,876  | buy_ratio 0.286  |  71% sell
large  ($100K–1M):140 trades | $28,446,937  | buy_ratio 0.581  |  58% buy
retail (<$100K):  (excluded by min-tier=large)
TOTAL ALL TIERS:               $66,003,528
```

[DP:dark_pool_block_stratified:2026-05-19]. Dollar-weighted buy/sell:
- Mega + Block + Large buy dollars ≈ $29.64M + (0.286 × $7.92M) + (0.581 × $28.45M) = **$48.4M buy**
- Sell dollars ≈ 0 + (0.714 × $7.92M) + (0.419 × $28.45M) = **$17.6M sell**
- **Net institutional buy ≈ $30.8M (73%/27% split).**

The 3-trade block tier doing 71% sell is a meaningful caveat — possibly a
single institution distributing into the morning rally — but it is dwarfed
by the mega prints.

### Institutional price levels (5-day, top 15)

| Price | Total premium | Shares | Trades | Distance from spot ($43.88) |
|-------|---------------|--------|--------|------------------------------|
| **$44.39** | $37,107,657 | 836,038 | 15 | **+1.16%** (HVN) |
| $45.04 | $25,545,548 | 567,175 | 33 | +2.64% |
| $44.00 | $17,820,000 | 405,000 | 1  | +0.27% (single mega print) |
| $44.23 | $14,076,419 | 318,255 | 2  | +0.80% |
| $45.23 | $11,516,853 | 254,629 | 22 | +3.07% |
| $44.75 | $5,452,902  | 121,857 | 14 | +1.98% |
| $44.45 | $5,178,928  | 116,512 | 13 | +1.30% |
| $45.14 | $4,381,888  | 97,073  | 5  | +2.87% |
| $45.47 | $3,909,849  | 85,996  | 3  | +3.62% |
| $45.01 | $3,319,745  | 73,756  | 6  | +2.57% |
| $44.65 | $2,972,806  | 66,582  | 8  | +1.76% |
| $45.15 | $2,912,186  | 64,503  | 12 | +2.89% |
| $44.99 | $2,585,857  | 57,477  | 7  | +2.53% |
| $44.84 | $2,574,445  | 57,415  | 3  | +2.19% |
| $44.68 | $2,476,040  | 55,418  | 8  | +1.78% |

[DP:dark_pool_price_levels:2026-05-13..19, days=5]. **ALL 15 top institutional
price levels sit ABOVE current spot ($43.88).** The cluster band is $44.00–
$45.47 with the dominant gravity at **$44.39** and a secondary at **$45.04**.
Implication: institutions own size in this band; dips back into the cluster
will be defended; breaks above $45.04 will likely see absorption flip into
chasing.

### Extended-hours activity

One pre-market dark print only:

```
12:18:13Z  3,821 sh @ $44.474, premium $169,935
nbbo_bid $44.35 / nbbo_ask $44.70 → mid $44.525
trade vs mid: -$0.051 (slight sell, but at illiquid wide spread)
```

[DP:dark_pool_extended_hours:2026-05-19]. Immaterial size ($170K), inside
the spread, just one print. No overnight institutional positioning to flag.
Read: morning accumulation was NOT pre-positioned overnight — it hit at the
opening cross.

### Ticker-summary context

PYPL is NOT in the market-wide dark pool top 100 by premium (lowest entry in
top 100 is CVX at $212M; PYPL totaled ~$66M today). [DP:dark_pool_ticker_summary:2026-05-19].
The signal is **composition, not volume rank**. A $66M dark-pool day with a
$29.6M mega-buy block is structurally bullish even if PYPL is just a
mid-size dark-pool ticker.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__dark_pool_largest` | symbol=PYPL, top-n=25, sort-by=premium, date=2026-05-19 | 25 prints, top = $17.8M @ $44.00 |
| `mcp__uw-pp__dark_pool_block_stratified` | symbol=PYPL, top-n=30, min-tier=large, date=2026-05-19 | mega 100% buy, block 29% buy, large 58% buy |
| `mcp__uw-pp__dark_pool_extended_hours` | symbol=PYPL, top-n=15, date=2026-05-19 | 1 print premarket, $170K, slightly below mid |
| `mcp__uw-pp__dark_pool_price_levels` | symbol=PYPL, top-n=15, days=5, date=2026-05-19 | All 15 top levels above spot, peak $44.39 |
| `mcp__uw-pp__dark_pool_ticker_summary` | top-n=100, date=2026-05-19 | PYPL not in top 100; #100 = CVX $212M |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** **ACCUMULATION (bullish).** Mega-tier 100% buy,
  $29.6M morning campaign, all 5-day institutional clusters above spot. The
  71%-sell block tier is a caveat, not a reversal. Net institutional dollars
  ≈ $30.8M buy on the day.
- **Conviction:** **4 / 5**. The mega-tier signal is unusually clean; the
  block-tier offset and PYPL's mid-tier ranking prevent a perfect 5.
- **Three S/R levels for phase-9 to use:**
  1. **$44.39** — primary institutional support (HVN, $37.1M / 836K sh).
  2. **$45.04** — secondary cluster + likely first resistance band ceiling.
  3. **$45.23–$45.47** — upper cluster edge; sustained close above flips
     this zone from resistance to support.
  4. (Bonus) **$44.00** — anchor of today's mega-print; loss = bullish
     thesis weakens materially.
- **Open questions:**
  - Was the morning $29.6M an accumulation or an internal cross (e.g., a
    pension reallocation) that didn't constitute genuine new buy interest?
    Without trade-level prints we can't distinguish — phase 3 OI changes
    and phase 7 insights may help triangulate.
  - Why are mid-tier blocks (3 trades, $7.9M) net SELLERS while mega is
    100% buy? Is this institutional rebalancing or a single PM exiting?
  - Phase 4 dealer positioning at $44.39 / $45.04 will tell us whether
    gamma is positive (dealers buy dips → reinforces DP support) or
    negative (dealers sell dips → conflicts with DP support).
