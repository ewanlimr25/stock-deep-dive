# Phase 2 — Dark Pool & Block Prints

**Ticker:** BABA · **As-of:** 2026-07-23 · **Spot:** $114.99
**Generated:** 2026-07-24
**Upstream:** phase-1-flow.md (net_flow −$1.68M, 5-session bearish sweep persistence,
open question: "is DP confirming distribution?"). phase-0.5 BUSY_NAME_NORMAL_DAY.

## Summary

Off-exchange activity is **MIXED with a mild distribution lean.** The two active tiers
disagree: the **large tier is mildly accumulative (buy_ratio 0.581, $93.2M)** but the
**block tier is distributive (buy_ratio 0.356 → sell_ratio 0.644, $28.7M)**, and there
were **no mega-tier prints at all** (0 volume) — so there is no high-conviction
institutional footprint either way. The **single largest block — $7.45M, 64,416 sh at
$115.67 — printed pre-market (11:22 UTC) BELOW the NBBO mid (trade_vs_mid −1.05),
i.e. seller-initiated**, and **19 of the top-25 blocks printed below spot**. The 5-day
price-level map shows a heavy institutional transaction zone at **$115–118** now sitting
as **overhead supply** with a support shelf at **~$114.97**. This confirms phase-1's
mild-bearish read without escalating it.

## Key signals

- **Block-tier distribution:** buy_ratio **0.356** (sell 0.644) on $28.7M `[DP:block_stratified]`
- **Large-tier mild accumulation:** buy_ratio **0.581** on $93.2M — suggestive only
  (0.55–0.70 band) `[DP:block_stratified]`
- **No mega-tier prints** (buy/sell vol both 0) — no whale footprint today `[DP:block_stratified]`
- **Largest block seller-initiated & pre-market:** $7.45M @ $115.67, trade_vs_mid −1.05,
  11:22 UTC `[DP:largest]` / `[DP:extended_hours]`
- **Overhead supply $116.85–118.22** (5-day, ~$63M across the band) vs support shelf
  **$114.97** ($29.7M, 258k sh) `[DP:price_levels]`

## Detailed findings

### Largest blocks (top-25, total premium $39.4M) `[DP:largest]`

| Price | Size | Premium | Time (UTC) | vs spot | Note |
|-------|------|---------|-----------|---------|------|
| $115.67 | 64,416 | $7.45M | 11:22:05 | above | pre-mkt, trade_vs_mid −1.05 (seller) |
| $113.65 | 43,100 | $4.90M | 15:45:28 | below | |
| $113.55 | 22,394 | $2.54M | 17:14:50 | below | |
| $113.70 | 19,500 | $2.22M | 15:45:14 | below | |
| $113.70 | 14,400 | $1.64M | 15:45:21 | below | |
| $113.60 | 13,383 | $1.52M | 19:50:01 | below | |

**19 of 25 top blocks printed below spot** ($114.99); the intraday prints cluster tightly
at **$113.2–113.7**. Only the pre-market $115.67 cross is materially above — and it was
seller-side. Read: sellers working size into the $113–114 shelf.

### Tier breakdown `[DP:block_stratified]`

| Tier | buy_ratio | (derived sell_ratio) | buy_vol | sell_vol | premium | Read |
|------|-----------|----------------------|---------|----------|---------|------|
| large | 0.581 | 0.419 | 473,835 | 342,210 | $93.2M | mild accumulation (suggestive) |
| block | 0.356 | **0.644** | 89,462 | 162,008 | $28.7M | **distribution** |
| mega | 0.5 | 0.5 | 0 | 0 | $0 | no prints |
| retail | 0.5 | 0.5 | 0 | 0 | $0 | no prints |

Tiers disagree; no mega confirmation. Net = **balanced-to-mildly-distributive.** The
distributive block tier aligns with phase-1's marginally-bearish directional premium.

### Price levels (5-day, window ends 2026-07-23) `[DP:price_levels]`

| Level | Premium | Shares | vs spot $114.99 |
|-------|---------|--------|-----------------|
| $115.55 | $30.2M | 261,621 | just above |
| **$114.97** | **$29.7M** | **258,447** | **≈ spot (support shelf)** |
| $117.97 | $16.3M | 138,403 | overhead |
| $118.03 | $13.1M | 110,679 | overhead |
| $117.14 | $11.9M | 101,540 | overhead |
| $116.85 | $11.9M | 101,531 | overhead |
| $118.22 | $10.2M | 86,676 | overhead |
| $120.5–120.95 | $16.2M | — | upper cap |

Heavy institutional transaction band **$115–118** — spot at $114.99 is at the **low end**
of where size traded, so **$116.85–118.22 is overhead supply / resistance** and **$114.97
/ $113–114 is the support shelf** the intraday blocks defended. `--days 5` anchors to the
latest date (2026-07-23), covering ~2026-07-17→23 (all present locally per phase-0; no gap).

### Extended-hours activity `[DP:extended_hours]`

Top ext-hours print = the same **$7.45M pre-market cross @ $115.67** (11:22 UTC / 07:22 ET).
Remaining ext-hours prints are small ($0.5–0.6M) at $114–115.7. The pre-market size is a
single cross below mid — flagged as possible hedging/positioning, **de-rated** (not clean
directional accumulation). No overnight catalyst on record (cross-check phase-6).

## Tool calls (audit)

| Datapoint | Command | jq path |
|-----------|---------|---------|
| largest blocks | `uw dark-pool largest --symbol BABA --top-n 25 --sort-by premium --date 2026-07-23` | `.results[].{price,size,premium,trade_vs_mid,executed_at}` |
| tier buy/sell | `uw dark-pool block-stratified --symbol BABA --top-n 30 --min-tier large --date 2026-07-23` | `.results[0].{large,block,mega}.buy_ratio` (sell = 1−buy) |
| price levels | `uw dark-pool price-levels --symbol BABA --top-n 15 --days 5 --date 2026-07-23` | `.results[].{price_level,total_premium,total_shares}` |
| ext hours | `uw dark-pool extended-hours --symbol BABA --top-n 15 --date 2026-07-23` | `.results[].{price,size,premium,executed_at}` |
| rank check | `uw dark-pool ticker-summary --top-n 30 --date 2026-07-23` | `[.results[].ticker]\|index("BABA")` → outside top-30 |

## Tool errors

None. (`price-levels` field is `.price_level` not `.price`; `block-stratified` buy/sell is
nested per tier with no `sell_ratio` — derived per `[[deep-dive-json-field-traps]]`.)

## Verdict for downstream

- **Bias: MIXED, mild distribution.** Block tier selling (0.356), large tier only mildly
  accumulative (0.581), no mega footprint, largest block seller-initiated pre-market,
  19/25 blocks below spot.
- **Conviction: 2/5** — tiers disagree and there is no mega/whale confirmation; the
  distributive read is real but low-magnitude.
- **Largest block as % of float: n/a** (`fz` returns no `Shs Float` for this ADR —
  phase-0). Qualitatively, BABA's ADS float is multi-billion; a 64k-share block is a
  vanishingly small % of float — **size alone is NOT a conviction signal here.**
- **Three S/R levels for phase-9:**
  1. **Support $114.97** (258k-sh shelf, ≈ spot) → next **$113.2–113.7** (intraday block floor).
  2. **Resistance $116.85–118.22** (heavy 5-day overhead supply, ~$63M).
  3. **Upper cap $120.5–120.95.**
- **Open questions:** Does OI (phase-3) put a call wall in the $116–120 overhead zone,
  reinforcing it as resistance? Is the $114–115 shelf also a put wall (dealer support)?
