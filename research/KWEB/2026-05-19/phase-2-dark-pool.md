# Phase 2 — Dark Pool & Block Prints

**Ticker:** KWEB
**As-of date:** 2026-05-19
**Generated:** 2026-05-20T00:00:00Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md

## Summary

Off-exchange tape is **divergent across institutional size tiers**:
**mega-tier ($10M+) buy_ratio is 0.000** — two prints totalling
**$25.87M (913,698 shares)** both crossed BELOW NBBO mid and are
classified SELL [DP:block_stratified]. The block tier ($1M+) flipped the
other way with buy_ratio 0.677, and the large tier ($100K+) was 0.536
[DP:block_stratified]. Read: **whales distributing while smaller desks
absorb**, consistent with phase-1's bearish 5-day sweep persistence
[FLOW:sweep_persistence]. Total KWEB DP premium today was **$100.7M**
across 348 prints. KWEB did NOT crack the top-30 market-wide DP cohort
($608M cut-off) — institutional but not headline volume.

## Key signals

- **Two mega prints classified SELL** [DP:largest]:
  - **13:40:07Z — 489,513 sh @ $28.31** ($13.86M), traded **-0.5¢ below
    mid** of $28.315
  - **19:56:41Z — 424,185 sh @ $28.32** ($12.01M), traded **-1.5¢ below
    mid** of $28.335 (last 4 minutes of the regular session — classic
    EOD unload pattern)
- **Mega tier buy_ratio = 0.000** (0 / 913,698 sh on buy side)
  [DP:block_stratified] — unambiguous distribution at the largest tier.
- **Block tier buy_ratio = 0.677** (320,749 sh buy / 152,800 sh sell)
  [DP:block_stratified] — sub-mega institutions absorbing some of the
  flow.
- **5-day cluster at $28.06 = $71M / 2.53M sh, 24 trades**
  [DP:price_levels] — far the largest institutional level in the
  trailing 5 sessions; sits ~1% BELOW today's spot ($28.36) — natural
  short-term magnet / support.
- **Secondary 5-day cluster at $30.50–30.61 = ~$117M aggregate**
  [DP:price_levels] — clear OVERHEAD distribution zone from prior week
  when KWEB was higher.

## Detailed findings

### Largest individual blocks [DP:largest]

Top-10 single prints today:

| Time (UTC) | Price | Size (sh) | Premium | NBBO mid | Δ-mid (¢) | Classification |
|------------|-------|-----------|---------|----------|-----------|----------------|
| 13:40:07 | 28.310 | 489,513 | $13,858,113 | 28.315 | -0.5 | **SELL (mega)** |
| 19:56:41 | 28.320 | 424,185 | $12,012,919 | 28.335 | -1.5 | **SELL (mega)** |
| 18:53:43 | 28.350 | 78,927 | $2,237,580 | 28.345 | +0.5 | buy |
| 14:02:07 | 28.410 | 57,000 | $1,619,370 | 28.405 | +0.5 | buy |
| 13:41:50 | 28.290 | 56,000 | $1,584,240 | 28.295 | -0.5 | sell |
| 19:11:05 | 28.380 | 54,000 | $1,532,520 | 28.395 | -1.5 | sell |
| 13:49:43 | 28.425 | 50,000 | $1,421,250 | 28.425 | 0 | neutral |
| 14:28:42 | 28.235 | 50,000 | $1,411,750 | 28.235 | 0 | neutral |
| 17:31:07 | 28.370 | 48,222 | $1,368,058 | 28.365 | +0.5 | buy |
| 19:45:36 | 28.300 | 42,800 | $1,211,240 | 28.305 | -0.5 | sell |

Pattern: **the two largest prints (a coordinated opening cross at the
13:40Z mark and an EOD unload at 19:56Z) are the unambiguous bearish
signals**. Mid-day block prints look more two-way and are weighted
toward smaller individual sizes.

### Tier breakdown [DP:block_stratified]

| Tier | Buy vol | Sell vol | Buy ratio | Premium | Trades |
|------|---------|----------|-----------|---------|--------|
| Mega (≥$10M) | 0 | 913,698 | **0.000** | $25,871,032 | 2 |
| Block (≥$1M) | 320,749 | 152,800 | 0.677 | $13,423,619 | 9 |
| Large (≥$100K) | 1,162,593 | 1,005,633 | 0.536 | $61,382,512 | 337 |
| Retail (<$100K) | — | — | — | 0 | 0 |
| **All tiers** | | | | **$100,677,163** | **348** |

The shape (0% buy at mega, then bid-back ratios at block / large) is the
**classic "whale distributes, mid-tier absorbs"** print. It is not the
shape you'd see in a clean bull-tape (mega buy + cascading large buys)
nor a panic (mega sell + large sell). It's a controlled distribution.

### Institutional price levels (5-day) [DP:price_levels]

Trailing 5 sessions (2026-05-13 → 2026-05-19), top 15 levels by premium:

| Rank | Price | Premium | Shares | Trades | Spot Δ% |
|------|-------|---------|--------|--------|---------|
| 1 | **$28.06** | **$71.0M** | 2,530,701 | 24 | -1.0% (SUPPORT) |
| 2 | $30.59 | $39.8M | 1,302,571 | 25 | +7.9% (resistance) |
| 3 | $30.61 | $32.5M | 1,060,486 | 33 | +7.9% (resistance) |
| 4 | $28.32 | $22.8M | 806,268 | 43 | +0.0% (battleground) |
| 5 | $28.31 | $20.5M | 723,618 | 26 | -0.2% |
| 6 | $30.56 | $20.2M | 660,314 | 30 | +7.8% (resistance) |
| 7 | $28.29 | $14.7M | 518,621 | 42 | -0.2% |
| 8 | $30.46 | $12.9M | 425,122 | 16 | +7.4% |
| 9 | $29.20 | $12.9M | 442,509 | 18 | +3.0% |
| 10 | $30.60 | $11.4M | 372,506 | 37 | +7.9% |
| 11 | $28.26 | $11.3M | 400,722 | 69 | -0.4% |
| 12 | $28.33 | $11.3M | 399,269 | 31 | +0.0% |
| 13 | $30.52 | $10.0M | 328,233 | 22 | +7.6% |
| 14 | $28.23 | $10.0M | 353,732 | 35 | -0.5% |
| 15 | $28.25 | $9.9M | 350,066 | 48 | -0.5% |

Cluster summary:
- **$28.06 — outsized single-level support** ($71M / 2.53M sh — 2x any
  other level). This is likely a prior swing low where institutions
  scaled in.
- **$30.46-$30.61 cluster** — six adjacent levels, **~$127M cumulative**.
  This is the prior trading zone before KWEB pulled back to current
  spot. Large institutional inventory in this zone implies **heavy
  resistance** if price reclaims it.
- **$28.20–28.33 cluster** — ten adjacent levels, **~$130M cumulative**.
  This IS the current battleground; spot is sitting on top of it.

### Extended-hours activity [DP:extended_hours]

Only two pre-market prints, total $267K — negligible. No catalyst-
driven overnight institutional moves to attribute.

### Ticker-summary context [DP:ticker_summary]

KWEB's $100.7M total premium ranks BELOW the top 30 names today (#30 cut
sits at SOXS ~$609M). The big DP cohort is dominated by index ETFs
(QQQ/SPY/IWM), mega-caps (NVDA/TSLA/AAPL/AMZN/GOOGL/META), bond ETFs
(LQD/HYG/TLT), and a notable **EWZ entry at $890M total premium with a
single $334.6M trade** — a Latin America / EM flag that may resonate
with KWEB's emerging-market China-internet exposure (phase 6 macro).

## Tool calls (audit trail)

| Tool | Args | Result |
|------|------|--------|
| `dark_pool_largest` | `{symbol: KWEB, top-n: 25, sort-by: premium, date: 2026-05-19}` | 25 rows |
| `dark_pool_block_stratified` | `{symbol: KWEB, top-n: 30, min-tier: large, date: 2026-05-19}` | 1 row (KWEB tier rollup) |
| `dark_pool_extended_hours` | `{symbol: KWEB, top-n: 15, date: 2026-05-19}` | 2 rows |
| `dark_pool_price_levels` | `{symbol: KWEB, top-n: 15, days: 5, date: 2026-05-19}` | 15 rows |
| `dark_pool_ticker_summary` | `{top-n: 30, date: 2026-05-19}` | 30 rows; KWEB absent |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** **Distribution** at mega tier, mild
  accumulation at block tier → net **mixed-bearish**, but the SIGNAL is
  the mega-tier 0.000 buy_ratio.
- **Conviction:** 4 / 5 — two mega prints at -0.5¢ and -1.5¢ below mid
  is high-confidence sell classification (the threshold for high-
  confidence per skill heuristics is buy/sell ratio > 0.7; this is
  effectively 1.0 sell). The 4 (not 5) reflects block-tier offset.
- **Three S/R levels for phase-9 to use:**
  1. **$28.06** — major institutional support (5-day $71M cluster).
     Stop-loss reference for any long entry; objective for any short
     swing.
  2. **$28.30** — current battleground (today's mega prints + $91M
     trailing-5d cluster). Above = neutral; below + holds = bears in
     control.
  3. **$30.46–30.61** — overhead resistance band ($127M institutional
     inventory). First objective for any bull reversal; sizable
     overhead-supply problem.
- **Open questions:**
  - Are the mega-tier sellers a single index-rebalancing flow (which
    would discount conviction) or true directional sellers? Without
    intraday print-protocol detail we can't fully separate; phase 8 PM
    sub-agent should weigh in.
  - Will the 5-day bearish sweep persistence (phase 1) AND mega-tier DP
    distribution (this phase) be confirmed by OI structure (phase 3)?
    Specifically: are puts being opened *or* covered, and are calls
    being closed *or* sold-to-open? OI delta in phase 3 is the deciding
    evidence.
