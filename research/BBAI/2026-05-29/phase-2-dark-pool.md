# Phase 2 — Dark Pool & Block Prints

**Ticker:** BBAI
**As-of date:** 2026-05-29
**Generated:** 2026-05-31 (re-verified against validated JSON)
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md, phase-1-flow.md

> **## DATA NOTE.** Figures below are from JSON-validated `uw dark-pool` output
> (`ticker-summary`/`largest`/`price-levels`/`block-stratified`/`extended-hours`)
> + the deep-dive `uw_dark_pool` aggregate. Earlier drafts mis-stated the tier mix
> (they said "retail"; it is in fact **large-tier**). This version is correct.

## Summary

BBAI's off-exchange flow is **large-tier and modestly buy-leaning — genuine
accumulation, not retail churn.** The day's dark-pool aggregate is **9,161,163
shares / $45,737,321 across 229 trades at avg $5.004** (**1.93% of the 473.71M
float**, ~10.5% of the 87.1M-share session). The tier breakdown: **`large`
$43,293,557 (94.7%) with buy_ratio 0.581** (buy_vol 5,041,000 vs sell_vol
3,635,289), one **`block` print of 484,874 sh / $2,443,765 that was a SELL** at the
highs, and **`mega $0`, `retail $0`**. So large accounts were **net buyers of
stock** (~58%) even as the options tape showed calls being **written** (phase-1) —
the combination reads like **accumulation-with-call-overwrite (a buy-write)**, with
one large block distributed into the pop. Net share-side bias: **mild
accumulation.**

## Key signals

- DP aggregate **9.16M sh / $45.7M / avg $5.004** = **1.93% of float** [DP:deep_dive_aggregate]
- **Large tier dominates & is buy-leaning**: `large $43.29M, buy_ratio 0.581`
  (buy 5,041,000 vs sell 3,635,289 sh) [DP:block-stratified]
- **One block print — a SELL**: 484,874 sh / $2,443,765 @ $5.04, below bid (NBBO
  5.05/5.06), 20:00 UTC = distribution into the highs [DP:largest]
- **No mega tier, no retail tier** ($0 each) → flow is institutional-scale
  large-tier, not retail [DP:block-stratified]
- 5-day price shelf: **$5.04 (954,045 sh), $4.94 (951,262 sh), $4.76 (594,507
  sh)**; today's prints span **$4.76–$5.12** [DP:price-levels]
- **Extended-hours active**: 15 prints, incl. two ~99k-sh blocks @ $5.08 at 21:30
  UTC (post-market) [DP:extended-hours]

## Detailed findings

### Tier breakdown (`uw dark-pool block-stratified`)

| tier | total premium | trades | buy_ratio | note |
|------|---------------|--------|-----------|------|
| large ($100k–$1M) | $43,293,557 (94.7%) | 228 | **0.581** | net buying |
| block ($1M–$10M) | $2,443,765 (5.3%) | 1 | **0.0** | single SELL (484,874 sh) |
| mega (≥$10M) | $0 | 0 | — | none |
| retail (<$100k) | $0 | 0 | — | none |
| **all tiers** | **$45,737,321** | 229 | — | overall ~55% buy by share |

→ Large-tier buy-lean (58.1%) = real accumulation; the lone block (a sell) and
the +6% day temper it. Overall share-weighted buy ≈ 55% (buy 5.04M vs sell 4.12M).

### Largest prints (`uw dark-pool largest`, top 10 of 25; top-25 = 2.59M sh / $12.9M)

| size (sh) | premium | price | NBBO | time (UTC) | read |
|-----------|---------|-------|------|------------|------|
| 484,874 | $2.44M | $5.04 | 5.05/5.06 | 20:00 | below bid → SELL (the block) |
| 114,338 | $547k | $4.78 | 4.78/4.79 | 14:18 | at bid |
| 109,758 | $536k | $4.88 | 4.88/4.89 | 13:34 | at bid |
| 104,600 | $526k | $5.03 | 5.02/5.03 | 18:54 | at ask → buy |
| 100,778 | $512k | $5.08 | 5.07/5.08 | 16:14 | at ask → buy |
| 99,588 | $506k | $5.0801 | 5.08/5.11 | 21:30 | post-mkt, near bid |
| 100,000 | $502k | $5.015 | 5.01/5.02 | 19:23 | mid/ask |
| 101,219 | $500k | $4.9399 | 4.93/4.94 | 15:22 | at bid |
| 96,382 | $493k | $5.12 | 5.11/5.12 | 16:22 | at ask → buy |

→ Two-sided but with afternoon at-ask buying in the $5.03–$5.12 zone; the single
biggest print is the $2.44M **block sell** at the close.

### Price levels (5-day, `uw dark-pool price-levels`; dates 5/29,28,27,26,22)

| level | shares (5d) | premium | trades |
|-------|-------------|---------|--------|
| $5.04 | 954,045 | $4.81M | 13 |
| $4.94 | 951,262 | $4.70M | 13 |
| $4.76 | 594,507 | $2.83M | — |

→ The institutional shelf spans **$4.76–$5.12**, heaviest at **$5.04 / $4.94**.
(`--days 5` anchors to latest available date per phase-0.)

## Tool calls (audit trail)

| Command | Result |
|---------|--------|
| `uw insights deep-dive --symbol BBAI --date 2026-05-29` (uw_dark_pool) | 9.16M sh / $45.7M / 229 trades / avg $5.004 |
| `uw dark-pool block-stratified --symbol BBAI --date 2026-05-29` | large $43.3M buy_ratio 0.581; block 1 sell; mega/retail $0 |
| `uw dark-pool largest --symbol BBAI --top-n 25 --sort-by premium --date 2026-05-29` | top = 484,874 sh $2.44M block SELL @ $5.04 |
| `uw dark-pool price-levels --symbol BBAI --top-n 15 --days 5 --date 2026-05-29` | shelf $4.76–$5.12; heaviest $5.04/$4.94 |
| `uw dark-pool extended-hours --symbol BBAI --top-n 15 --date 2026-05-29` | 15 prints (incl 21:30 post-mkt ~99k @ $5.08) |
| `uw dark-pool ticker-summary --top-n 60 --date 2026-05-29` | BBAI not in top-60 by total premium (universe rank not confirmed) |

## Tool errors

- First-draft leaves `uw dark-pool levels` / `ticker-prints` do not exist; corrected
  to real leaves above. An intermediate draft mis-labeled the tier mix as "retail"
  — corrected to large-tier from validated `block-stratified`.

## Verdict for downstream phases

- **Accumulation / Distribution / Mixed:** **Mild accumulation** (large-tier
  buy-lean 58%) with one block-sell offset.
- **Conviction:** 3/5 — large-tier (not retail), buy-leaning, but no mega prints
  and a $2.44M block distributed at the highs; share-side accumulation coexists
  with options-side call writing (phase-1) → consistent **buy-write** read.
- **Largest block as % of float:** 484,874 sh = **0.102%** (a SELL); total DP 1.93%
  of float — meaningful aggregate participation for the name.
- **Three S/R levels for phase-9:** **$5.04** (heaviest DP level + spot), **$4.94**
  (second shelf), **$4.76** (lower-tier support / day's low zone).
- **Open questions:** Is the large-tier buying short-covering (26% short float,
  phase-7c) or fresh longs? Does the buy-write read hold once phase-4 GEX shows
  whether dealers are long/short gamma at $5? Is the late block-sell + post-market
  prints a distribution start?
