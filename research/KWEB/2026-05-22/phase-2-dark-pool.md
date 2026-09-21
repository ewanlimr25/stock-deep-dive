# Phase 2 — Dark Pool & Block Prints

**Ticker:** KWEB
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T00:00:00Z
**Upstream phases cited:** phase-0.5-context.md, phase-1-flow.md

## Summary

Dark pool reads **net distribution at the institutional block level into a falling
price** — the opposite tilt to phase-1's bullish call campaign. The single mega
block ($13.8M, 514k shares) is **sell-classified (buy_ratio 0.0)** and the block
tier (≥$1M, 26 trades, $49.4M) is **sell-heavy (buy_ratio 0.306)**, while only the
smaller large tier ($100k–1M, $120.3M) is buy-heavy (0.622) — i.e. the *biggest*
prints sell, the *smaller* ones absorb. Pre-market prints walked price **down from
$27.31 (08:34) to $26.36 (08:35 ET)** before the regular-session blocks clustered at
$26.88–27.09. The 5-day volume node sits at **~$28.0** ($290M+ combined across
27.95–28.32), now **overhead supply** with spot at $26.91. **Heavy ETF caveat:**
KWEB is an ETF, so a large share of this $183.6M is creation/redemption / NAV
arbitrage, and most blocks printed within 1–4¢ of mid (low-confidence buy/sell) —
so this is a *suggestive distributive tilt*, not a high-confidence one.

## Key signals

- Mega tier: **1 print, $13.82M, 514,299 shares SOLD, buy_ratio 0.0** at $26.88
  (3.5¢ below mid) `[DP:block_stratified]` `[DP:largest]`.
- Block tier (≥$1M): **buy_ratio 0.306** (buy 561k vs sell 1,275k shares), $49.4M
  `[DP:block_stratified]` — distribution.
- Large tier ($100k–1M): **buy_ratio 0.622** (buy 2,788k vs sell 1,693k), $120.3M
  `[DP:block_stratified]` — the only accumulating tier.
- 5-day volume node **$27.95–28.32** (~$290M+; the single $28.09 level = $164.3M /
  5.85M sh) `[DP:price_levels]` — overhead supply ~+4% above spot.
- Pre-market distribution: prints walked **$27.31 → $26.36** before the open
  `[DP:extended_hours]`; a wide-spread $1.88M post-close print (20:00, NBBO
  26.8/27.6) is an ETF closing/NAV print — **non-directional, discount it**.

## Detailed findings

### Largest blocks `[DP:largest]` (spot $26.91)

| Time (UTC) | Price | Size | Premium | vs mid | Class |
|-----------|-------|------|---------|--------|-------|
| 15:36 | 26.88 | 514,299 | **$13.82M** | −3.5¢ | sell (mega) |
| 14:51 | 26.95 | 175,096 | $4.72M | −0.5¢ | ~mid (marginal sell) |
| 14:58 | 26.88 | 136,225 | $3.66M | −1.5¢ | sell |
| 14:38 | 27.03 | 130,906 | $3.54M | −1.5¢ | sell |
| 09:29* | 26.69 | 103,316 | $2.76M | **+4.5¢** | buy (pre-mkt) |
| 13:38 | 27.09 | 78,400 | $2.12M | +0.5¢ | buy |
| 20:00* | 26.91 | 69,695 | $1.88M | −29¢ | **ETF NAV print — ignore** |

Most blocks printed within ±1–4¢ of mid → buy/sell classification is **low
confidence** (pitfall: treat only >0.7 ratios as firm). The directional read is
carried by the *tier ratios*, not individual prints.

### Tier breakdown `[DP:block_stratified]` (boundaries: mega ≥$10M, block ≥$1M, large ≥$100k)

| Tier | Trades | Premium | Buy vol | Sell vol | buy_ratio | Read |
|------|--------|---------|---------|----------|-----------|------|
| **mega** | 1 | $13.8M | 0 | 514,299 | **0.00** | distribution |
| **block** | 26 | $49.4M | 561,386 | 1,274,591 | **0.306** | distribution |
| large | 574 | $120.3M | 2,788,284 | 1,692,865 | 0.622 | accumulation |
| retail | 0 | $0 | — | — | — | — |

Per the tool's own caveat, **mega/block is the smart-money tier** — and it is
**sell-tilted**. The large-tier buying is the absorbing counterparty (could be the
call-campaign hedger from phase-1 buying stock, or MM offset). Net: the heaviest
hands are **selling into the low**.

### Price levels (5-day clusters) `[DP:price_levels]`

| Level | 5-day premium | Position vs spot $26.91 | Role |
|-------|---------------|--------------------------|------|
| **$28.09** | $164.3M | +4.4% | **major overhead supply** |
| $28.06 / 28.10 / 28.16 / 28.31 / 28.32 | $71M / 55M / 14M / 16M / 14M | +4–5% | supply shelf |
| $27.95 | $26.5M | +3.9% | supply |
| $27.63 / 27.40 / 27.19 | $17M / 12M / 66M | +1–3% | intermediate pivots |
| **$26.88–26.95** | ~$57M (today) | ≈ spot | **near-term battleground/support** |

The dominant 5-day node is at **~$28**, where price traded 05-18→05-21 before
falling. With spot now below it, that shelf is **resistance/trapped supply**, not
support — confirming a distributive 5-day tape (consistent with phase-1's bearish
`sweep_persistence`).

### Extended-hours `[DP:extended_hours]`

All flagged prints are **pre-market** (08:34–13:25 UTC = 4:34–9:25 ET) or
post-close (20:00 UTC). Pre-market prints stepped **down** ($27.31 → $26.36),
signalling overnight selling pressure into the open. The 20:00 $1.88M print sits
29¢ from a wide NBBO mid → **ETF NAV/closing mechanic, not directional intent**.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `dark_pool_largest` | KWEB, top25, premium | mega 514k-sh sell $13.8M; blocks near mid |
| `dark_pool_block_stratified` | KWEB, top30, large | mega 0.0 / block 0.306 / large 0.622 |
| `dark_pool_extended_hours` | KWEB, top15 | pre-mkt walk-down 27.31→26.36; 20:00 NAV print |
| `dark_pool_price_levels` | KWEB, days5, top15 | 5-day node ~$28 (overhead); ~26.9 battleground |

## Tool errors

(none)

## Verdict for downstream phases

- **Institutional bias:** **MIXED, leaning DISTRIBUTION** — mega/block tier sells
  (buy_ratio 0.0 / 0.306) into a falling price; large tier absorbs (0.622); 5-day
  node at $28 is now overhead supply. **Does NOT confirm** phase-1's bullish calls.
- **Conviction:** **2.5/5** — directionally distributive, but de-rated hard for
  (a) KWEB being an **ETF** (creation/redemption noise), and (b) most blocks within
  ±1–4¢ of mid (low-confidence classification). The signal is the tier *tilt*, not
  any single print.
- **Three S/R levels for phase-9:**
  1. **$27.95–28.10** — major overhead supply (5-day $290M+ node); bull thesis
     needs to reclaim this; aligns with phase-1's 30–31 call strikes being *beyond* it.
  2. **$27.19–27.40** — intermediate resistance/pivot ($78M).
  3. **$26.88–26.95** — near-term support/battleground (today's $57M); a clean
     break below opens air toward the pre-market $26.36 low.
- **Open questions:**
  1. Is the mega/block selling **genuine distribution or ETF redemption**? (phase-6
     China-flows / fund-flow context may help.)
  2. Does dealer OI/positioning (phase-3) corroborate the bearish 5-day sweep +
     DP distribution, or the bullish phase-1 calls? **This is now the pivotal
     adjudication** — share tape (DP + sweeps) is heavy, options skew is bullish.
