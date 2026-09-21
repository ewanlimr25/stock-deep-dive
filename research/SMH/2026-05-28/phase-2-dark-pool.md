# Phase 2 — Dark Pool & Block Prints

**Ticker:** SMH
**As-of date:** 2026-05-28
**Generated:** 2026-05-29T12:20:00Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md, phase-1-flow.md

## Summary

Dark-pool tape is **mildly distributive but low-conviction**, and the distribution
signal is largely an **ETF-mechanics artifact**: the mega-tier (the 7 biggest
blocks, $133.4M) prints **buy_ratio 0.314** (net selling) `[DP:block_stratified]`,
but those mega sells are **three after-hours prints executed at exactly the close
$599.83** (45,081 + 26,302 + 17,578 sh ≈ $53M, all 20:55–22:22 UTC) — the signature
of ETF redemption / NAV crosses, not directional distribution. The large tier (the
bulk, $571.9M, 69% of premium) is mild-sell (0.461) and the block tier mild-buy
(0.583). Total dark-pool premium $826.3M ranks SMH **outside the top-10** today —
dwarfed by the single-name semis it holds (MU $13.68bn, NVDA $9.69bn, SNDK $5.37bn,
AMD $4.62bn) `[DP:ticker_summary]`, reinforcing phase-0.5's read that **the action is
in the single names and SMH is the hedge/basket vehicle**. The actionable output is
the **5-day institutional support shelf at $567.88 ($198.7M)** `[DP:price_levels]`.

## Key signals

- **Mega-tier net selling** but it's AH-at-close ETF mechanics: buy_ratio 0.314,
  buy 69,581 / sell 152,293, $133.4M, 7 trades `[DP:block_stratified]`.
- **Three AH blocks at the close $599.83** (≈$53M total, 20:55/21:08/22:22 UTC) =
  redemption/NAV crosses — de-rated, not directional `[DP:extended_hours]`.
- **Major support shelf $567.88** — $198.7M / 349,932 sh over 5 days, the single
  heaviest institutional level, ~5.3% below spot `[DP:price_levels]`.
- **SMH outside DP top-10** ($826M) vs MU $13.68bn / NVDA $9.69bn — basket is the
  hedge, single names are where institutions actually transact `[DP:ticker_summary]`.
- Intraday RTH prints two-way around $601–604 (LIFT and HIT mixed); no clean
  one-sided accumulation or distribution within the session `[DP:largest]`.

## Detailed findings

### Largest blocks (UTC times; RTH = 13:30–20:00 UTC)

| Time (UTC) | Price | Size | Prem | NBBO | Note |
|-----------|-------|------|------|------|------|
| 20:55:32 | 599.83 | 45,081 | $27.04M | HIT | **AH at close — redemption?** |
| 19:05:04 | 601.00 | 42,000 | $25.24M | LIFT | RTH buy |
| 16:22:28 | 602.01 | 35,758 | $21.53M | HIT | RTH sell |
| 17:15:23 | 603.51 | 27,574 | $16.64M | HIT | RTH sell |
| 17:27:33 | 602.16 | 27,581 | $16.61M | LIFT | RTH buy |
| 22:22:48 | 599.83 | 26,302 | $15.78M | HIT | **AH at close** |
| 21:08:03 | 599.83 | 17,578 | $10.54M | HIT | **AH at close** |
| 19:17:43 | 599.85 | 13,614 | $8.17M | LIFT | RTH buy |
| 17:00:34 | 604.74 | 10,129 | $6.13M | LIFT | RTH buy |

Intraday is genuinely two-way (LIFT/HIT alternating, $601–604). The one-sided
signal is the AH $599.83 cluster — and that price = the exact official close, the
hallmark of NAV/redemption activity for an ETF.

### Tier breakdown (single-day)

| Tier | buy_ratio | buy_vol | sell_vol | premium | trades | read |
|------|-----------|---------|----------|---------|--------|------|
| mega (≥$10M) | **0.314** | 69,581 | 152,293 | $133.4M | 7 | net sell — but AH-at-close (ETF mechanics) |
| block ($1–10M) | 0.583 | 117,822 | 84,185 | $121.0M | 64 | mild buy |
| large ($100k–1M) | 0.461 | 440,481 | 515,254 | $571.9M | 2,645 | mild sell |
| retail | — | 0 | 0 | $0 | 0 | n/a |

Premium-weighted, the tape leans mild-sell (large tier is 69% of premium at 0.461),
but no tier is a high-confidence (>0.7) signal. **Treat as balanced-to-mildly
distributive, low conviction.**

### Price levels (5-day clusters, 2026-05-21 → 05-28)

| Price | Premium | Shares | Trades | vs spot ($599.83) |
|-------|---------|--------|--------|-------------------|
| **567.88** | **$198.7M** | 349,932 | 9 | −5.3% (major support) |
| 577.39 | $62.0M | 107,424 | 4 | −3.7% |
| **599.83** | $59.2M | 98,683 | 12 | spot (today's prints) |
| 576.32 | $52.9M | 91,869 | 19 | −3.9% |
| 596.10 | $36.7M | 61,490 | 6 | −0.6% |
| 595.50 | $33.1M | 55,630 | 13 | −0.7% |
| 601.00 | $27.2M | 45,330 | 14 | +0.2% |

Institutional price memory: **heavy support $567–577**, a mid-shelf $595–596, and
spot $599–601. The $567.88 shelf is by far the largest and aligns with the 05-21
swing low — a natural downside magnet/support if the June put hedges pay off.

### Extended-hours activity

Concentrated entirely at $599.83 (the close): $27.04M + $15.78M + $10.54M + $3.00M
+ $1.36M ≈ **$57M AH at the exact close price**. For an ETF this is overwhelmingly
likely creation/redemption or NAV-based crossing, **not** directional intent — flag
and de-rate per the phase pitfall. One small AH LIFT at $602.49 (1,000 sh).

## Tool calls (audit trail)

| Command | Result summary |
|---------|----------------|
| `uw dark-pool largest --symbol SMH --sort-by premium` | two-way RTH $601–604; AH cluster $599.83 |
| `uw dark-pool block-stratified --symbol SMH --min-tier large` | mega 0.314 / large 0.461 / block 0.583 |
| `uw dark-pool price-levels --symbol SMH --days 5` | major shelf $567.88 ($198.7M) |
| `uw dark-pool extended-hours --symbol SMH` | ~$57M AH at close $599.83 (redemption) |
| `uw dark-pool ticker-summary` | SMH outside top-10; MU $13.68bn, NVDA $9.69bn lead |

## Tool errors

(none)

## Verdict for downstream

- **Institutional bias:** **Mixed / mildly distributive — LOW conviction.** The
  mega-tier sell is an AH-at-close ETF-mechanics artifact; intraday is two-way. No
  clean accumulation or distribution. This neither confirms nor contradicts the
  phase-1 hedging read — it is consistent with a basket being held/rolled, not
  dumped.
- **Conviction:** **2/5** (low — ETF redemption mechanics dominate the one-sided tier).
- **Largest block as % of float:** **n/a** — SMH is an ETF; `fz` returns no float
  (`Shs Float` null, phase-0). Size is best read vs SMH's own $826M DP baseline,
  where today is unremarkable and ranks outside the DP top-10.
- **Three S/R levels for phase-9:**
  1. **$567.88** — major institutional support shelf ($198.7M, 5-day) and the
     downside target the June puts protect toward.
  2. **$576–577** — secondary support cluster ($62M + $53M).
  3. **$595–601** — current consolidation / spot shelf ($36.7M + $33.1M + $59.2M
     + $27.2M); $601 is near-term overhead, $612.30 is the 52-week high.
- **Open questions:** Do the AH $599.83 prints reflect net creation (bullish basket
  demand) or net redemption (basket being unwound)? The buy/sell tilt says
  redemption-leaning but ETF NBBO classification at the close is unreliable. Does
  phase-3 OI show the June puts *opening* against this support shelf (hedge build to
  $568), confirming $567.88 as the consensus downside line?
