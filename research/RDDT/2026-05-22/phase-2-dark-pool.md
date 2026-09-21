# Phase 2 — Dark Pool & Block Prints

**Ticker:** RDDT
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T00:00:00Z
**Upstream phases cited:** phase-0.5-context.md, phase-1-flow.md

## Summary

Dark pool reads **mild accumulation / dip-buying — which contradicts phase-1's
bearish options tape.** Block-tier (≥$1M) prints show **buy_ratio 0.735** (high
confidence per the >0.7 heuristic) on $33.5M / 11 trades, and the two largest
blocks of the day ($9.86M @ 141.70 and $6.6M @ 141.67) both printed **above NBBO
mid** — institutions buying the dip into the close at 141–142. The countervailing
facts that keep this from being a clean accumulation call: the **mega tier
(≥$10M) is empty** (the biggest block was $9.86M, just under threshold — no single
whale), and the large tier ($131M, 657 trades) is **near-balanced at 0.526**.
The 5-day price-level map is dominated by a **$137M node at 146.72** (the 5/20
breakdown price) that now sits ~3.5% overhead as resistance/supply. Net: today's
off-exchange flow leans to the buy side at 141–142, **a genuine counterweight to
the bearish options flow** that the debate phase must resolve.

## Key signals

- **Block tier buy_ratio 0.735** ($33.5M, 11 trades) — high-confidence
  accumulation skew [DP:block_stratified]
- Two largest blocks **buy-side above mid**: 69,600 sh @ $141.70 (+$0.04 vs mid,
  $9.86M) and 46,700 sh @ $141.67 (+$0.025, $6.6M, at the close) [DP:largest]
- **Mega tier empty** — no ≥$10M single print; buying is distributed, not one
  whale [DP:block_stratified]
- 5-day DP supply node at **146.72 = $137M / 935k sh** (the 5/20 breakdown level),
  now overhead resistance [DP:price_levels]
- Today's accumulation building support at **141.67–141.70** ($25M combined)
  [DP:price_levels]

## Detailed findings

### Largest blocks — [DP:largest]

| Time (UTC) | Price | Size | Premium | vs mid | Read |
|------------|-------|------|---------|--------|------|
| 15:31 | 141.70 | 69,600 | $9.86M | +0.04 | **buy** (above mid) |
| 20:00 | 141.67 | 46,700 | $6.62M | +0.025 | **buy**, at close |
| 18:12 | 142.155 | 25,000 | $3.55M | −0.085 | sell (below mid) |
| 14:32 | 141.70 | 24,900 | $3.53M | +0.105 | **buy** |
| 19:12 | 141.21 | 11,275 | $1.59M | −0.075 | sell |
| 14:47 | 141.14 | 11,241 | $1.59M | +0.04 | buy |

A cluster of ~5,000-lot prints between 18:46–19:57 UTC printed at/just-above mid
around 141.5–141.9 — systematic afternoon buying into the close. The two biggest
blocks are buy-side; sells are smaller and scattered. Net **buy lean**, concentrated
late-session at 141–142.

### Tier breakdown — [DP:block_stratified]

| Tier | Premium | Trades | Buy ratio | Read |
|------|---------|--------|-----------|------|
| mega (≥$10M) | $0 | 0 | — | empty (no whale) |
| **block (≥$1M)** | **$33.47M** | 11 | **0.735** | **accumulation (high-conf)** |
| large (≥$100k) | $131.05M | 657 | 0.526 | near-balanced, slight buy |
| Total | $164.53M | — | — | mild net buy |

The accumulation signal lives entirely in the 11 block-tier trades; the much
larger "large" tier is essentially two-way. So this is *suggestive* accumulation,
not a saturating one — appropriate to de-rate to conviction 3.

### Price levels (5-day) — [DP:price_levels]

| Level | Premium | Shares | Note |
|-------|---------|--------|------|
| **146.72** | **$137.2M** | 935,034 | 5/20 breakdown price — **major overhead supply** |
| 146.08 | $56.2M | 384,703 | reinforces 146 supply shelf |
| 150.04 | $10.5M | 69,863 | 5/21 close — secondary resistance |
| 147.00 | $3.7M | 25,408 | within 146–147 supply zone |
| **141.70** | $14.6M | 103,000 | today — support being built |
| **141.67** | $10.5M | 73,954 | today's close — support |
| 158–160 | ~$13M | — | stale (early-window highs, far overhead) |

Current spot **141.67**. The dominant cluster (146–147, ~$200M combined) sits
~3.5–4% **above** spot — but it is *prior* transaction volume from the 5/20
down-day, i.e. **resistance/supply the stock fell through**, not fresh
above-market accumulation. Today's prints concentrate **at 141.67–141.70** =
nascent support. Read structurally, not as "paying up."

### Extended-hours activity — [DP:extended_hours]

The largest ext-hours prints are the **20:00 closing-cross-adjacent blocks at
141.67** ($6.6M / 46,700 sh, plus several smaller at the same 141.67 print) — these
are at the official close and read as liquidity/MOC rather than directional
overnight conviction. One genuine after-hours print: 22:38, 1,500 sh @ 141.23
(small). Morning pre-market prints (12:00–13:25) transacted at 145–150 when the
stock was higher pre-decline. **No directional overnight block** that would flag a
catalyst — de-rate ext-hours signal. Cross-ref phase-6 for any overnight news
(none expected; earnings not until 2026-07-30 per phase-0.5).

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `dark_pool_largest` | symbol=RDDT, top25, premium | top 2 blocks buy-side @141.67–141.70 |
| `dark_pool_block_stratified` | symbol=RDDT, min_tier=large | block 0.735 buy, large 0.526, mega empty |
| `dark_pool_price_levels` | symbol=RDDT, 5d, top15 | 146.72 $137M supply; 141.67 support |
| `dark_pool_extended_hours` | symbol=RDDT, top15 | closing-cross blocks @141.67, no overnight signal |

## Tool errors

None.

## Verdict for downstream

- **Bias:** Accumulation (mild) — block-tier dip-buying at 141–142. **Directly
  conflicts with phase-1's bearish options flow.**
- **Conviction:** 3/5 — block 0.735 is a real buy skew, but mega tier empty and
  large tier balanced (0.526) keep it from being decisive.
- **Three S/R levels for phase-9:**
  1. **Support 141.5–141.7** — today's block accumulation zone (entry/stop ref).
  2. **Resistance 146–147** — $200M 5-day supply node (the 5/20 breakdown); first
     major overhead target / where a bounce likely stalls.
  3. **Resistance 150** — 5/21 close, secondary cap.
- **Open questions:**
  - Is the block-tier dip-buying genuine directional accumulation, or just
    liquidity providers / index flow absorbing the options-driven selling? The
    near-balanced large tier suggests caution.
  - Does phase-3 OI confirm whether the 130P/115P put buildup (phase-1) and the
    bid-side LEAP call sales are *new* positions vs *closing* — and does dealer
    positioning explain the DP-vs-options divergence?
  - The **DP-accumulation-vs-options-bearish divergence is the central tension** of
    this dive — flag for phase-8b debate.
