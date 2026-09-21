# Phase 2 — Dark Pool & Block Prints

**Ticker:** NVDA
**As-of date:** 2026-05-27
**Generated:** 2026-05-28T02:24:00Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md, phase-1-flow.md

## Summary

The dark-pool tape **superficially contradicts** the bearish options flow
(phase-1): mega-tier `buy_ratio = 0.964` ($3.63B, 16.45M buy vs 0.61M sell). But
the contradiction largely dissolves on inspection — **every mega-block driving that
ratio is an after-hours print (20:00–21:41 UTC ≈ 16:00–17:41 ET) clustered at the
$212.60 close** ($712M, $680M, $680M, $500M, $300M), the classic
closing-auction / MOC / index-rebalance signature rather than aggressive
intraday directional accumulation. The *intraday* block and large tiers are
near-balanced (buy_ratio 0.537 / 0.515). In %-of-float terms each block is
negligible (≤0.014% of NVDA's 23.27B float). Net read: **MIXED / mechanical** —
not high-conviction accumulation, and not enough to override the persistent
bearish options campaign.

## Key signals

- **Mega buy_ratio 0.964** ($3.63B, 25 trades) — eye-catching, but [DP:largest]
  shows it is after-hours closing prints, not intraday lifts.
- **Largest block:** 3,350,463 sh @ $212.60 = $712.3M at 20:00:07 UTC
  [DP:largest] — 0.0144% of float [DP:block_pct_float fz], negligible for a
  23.27B-float megacap.
- **Intraday tiers near-balanced:** block 0.537, large 0.515 [DP:block_stratified]
  — no directional conviction once the closing prints are set aside.
- **5-day price clusters span spot→above:** $212.6 ($3.49B), $215.33 ($2.43B),
  $223.47 ($1.52B), $219.51 ($894M) [DP:price_levels].
- **NVDA #2 in universe DP premium** ($10.76B) behind MU ($17.24B); SNDK #4,
  AMD #8 [DP:ticker_summary] — semi-complex dominates dark pool too (phase-0.5).

## Detailed findings

### Largest blocks — [DP:largest]

| Time (UTC) | Price | Size (sh) | Premium | % float |
|------------|------:|----------:|--------:|--------:|
| 20:00:07 | 212.60 | 3,350,463 | $712.3M | 0.0144% |
| 20:03:44 | 212.60 | 3,198,100 | $679.9M | 0.0137% |
| 20:03:51 | 212.60 | 3,198,100 | $679.9M | 0.0137% |
| 21:06:37 | 212.60 | 2,351,834 | $500.0M | 0.0101% |
| 21:41:40 | 212.60 | 1,411,100 | $300.0M | 0.0061% |
| 18:35:25 | 213.20 |   750,000 | $159.9M | 0.0032% |
| 21:18:47 | 212.36 |   559,466 | $118.8M | 0.0024% |

The five biggest prints all execute **after 20:00 UTC at exactly $212.60** — the
closing price. This timestamp+single-price clustering is the MOC/closing-auction /
index-flow fingerprint (common pitfall #3); treat the 0.964 mega buy_ratio as
**de-rated**, not a clean accumulation signal.

### Tier breakdown — [DP:block_stratified]

| Tier (≥) | buy_ratio | buy_vol | sell_vol | premium |
|----------|----------:|--------:|---------:|--------:|
| mega ($10M) | **0.964** | 16,452,703 | 610,406 | $3.63B |
| block ($1M) | 0.537 | 3,056,429 | 2,636,780 | $1.20B |
| large ($100k) | 0.515 | 14,455,206 | 13,603,037 | $5.93B |

The conviction is *entirely* in the mega tier, which is *entirely* after-hours
closing prints. Strip those and the institutional intraday tape (block/large) is a
coin-flip — consistent with phase-1's net-bearish read, not opposed to it.

### Price levels (5-day, anchored to latest=2026-05-27) — [DP:price_levels]

Support / resistance clusters: **$212.6 (spot, $3.49B — heaviest)**, $215.33
($2.43B), $219.51/$219.21 (~$1.42B combined), **$223.47 ($1.52B)**. The shelf at
$212.6 is the day's battleground (= the 0DTE option pin from phase-1); $215.3 and
$223.5 are overhead supply.

### Extended-hours — [DP:extended_hours]

All 15 extended-hours prints are the same after-hours $212.60 cluster catalogued
above. No pre-market accumulation; this is closing-side flow.

## Tool calls (audit trail)

| Command | Result summary |
|---------|----------------|
| `uw dark-pool largest --symbol NVDA --sort-by premium` | 25 blocks, top $712M @ $212.60 AH |
| `uw dark-pool block-stratified --min-tier large` | mega 0.964 / block 0.537 / large 0.515 |
| `uw dark-pool price-levels --days 5` | clusters $212.6 / $215.3 / $223.5 |
| `uw dark-pool extended-hours` | 15 prints, all AH $212.60 |
| `uw dark-pool ticker-summary` | NVDA #2 ($10.76B) behind MU |

## Tool errors

(none)

## Verdict for downstream

- **Net institutional bias:** **MIXED / mechanical** — headline mega buy_ratio
  0.964 is real but after-hours closing-auction flow; intraday tiers balanced. Does
  *not* confirm accumulation and does *not* refute phase-1's bearish campaign.
- **Conviction:** **2/5** (size is large in $ but mechanical in character and
  negligible in %-of-float; probabilistic NBBO classification).
- **Largest block as % of float:** 0.0144% [DP:block_pct_float fz] — immaterial
  for a 23.27B-float megacap; do not read the dollar size as conviction.
- **Three S/R levels for phase-9:**
  1. **$212.6** — pivot/support, heaviest DP shelf + 0DTE option pin (phase-1).
  2. **$215.3** — first overhead supply ($2.43B cluster).
  3. **$223.5** — major overhead resistance ($1.52B cluster).
- **Open questions:**
  - Were the $212.60 after-hours blocks index rebalance / MOC, or a real buyer
    stepping in at the close? Phase-6 should check for any 2026-05-27 rebalance/news.
  - Phase-3 OI-change must resolve whether the bid-side LEAP calls (phase-1) are
    long closes or short-call opens at the $210/$212.6 shelf.
