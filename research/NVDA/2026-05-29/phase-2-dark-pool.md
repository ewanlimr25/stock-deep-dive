# Phase 2 — Dark Pool

**Ticker:** NVDA
**As-of date:** 2026-05-29
**Generated:** 2026-05-30T13:25Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md, phase-1-flow.md

## Summary

The dark-pool tape is **strongly distributive — institutions sold into the
close.** Block stratification is unambiguous: **mega-tier blocks (≥$10M) printed
a buy_ratio of 0.003** — i.e. **49.1M shares sold vs 135K bought ($10.4B
premium)**, essentially one-way institutional selling. The 25 largest individual
prints are **100% sell-side** (every one executed *below* the NBBO mid), totaling
**34.6M shares**, and all cleared at **211.14 — the closing price — in a cluster
at ~16:00 ET**, a textbook closing-cross liquidation. The block tier (≥$1M) was
also net-sell (buy_ratio 0.305); only the "large" tier ($100K–$1M) was mildly
net-buy (0.541). This **directly contradicts the weak phase-1 bull thread**: while
near-dated calls were being bought intraday at 215–217, the real institutional
size was *distributing stock* at the 211.14 close. Combined with the phase-0.5
downtrend, this is the most directionally informative signal so far. **Verdict:
BEARISH / distribution. Conviction 4/5.**

## Key signals

- [DP:block-stratified] **Mega tier (≥$10M): buy_ratio 0.003** — 135,457 buy vs
  **49,107,539 sell**, $10.40B premium, 122 trades. Near-total institutional
  selling. This is the dominant tier ($10.4B of the $18.2B all-tier total).
- [DP:block-stratified] **Block tier (≥$1M): buy_ratio 0.305** (2.18M buy /
  4.98M sell, $1.53B) — also net-sell. **Large tier ($100K–$1M): buy_ratio
  0.541** (mildly net-buy, $6.24B). Smart-money tiers (mega+block) = selling.
- [DP:largest] **Top-25 prints 100% sell-side** (all below NBBO mid): total
  **34,617,186 sh**, **0 buy / 34.6M sell by NBBO**. Largest: 3.40M @ 211.14
  (mid 211.76, −0.62), 3.03M @ 211.14 (mid 212.26, −1.12), 2.90M @ 211.14.
- [DP:largest] **All large prints cleared at 211.14 (the close) ~20:00 UTC
  (16:00 ET)** — a closing-cross distribution cluster, not intraday accumulation.
- [DP:price-levels] **49.7M shares ($10.5B) printed at the single 211.14 level**
  (the close); secondary activity at 216–217 (above spot, 0.15–0.32M each) —
  i.e. earlier prints higher, the giant block at the close.
- [DP:insights_deep_dive] Aggregate: **85.38M dark shares**, avg_price **215.47**
  (above the 211.14 close — bulk printed higher, then dumped at the close),
  $18.17B premium, 30,583 trades.

## Detailed findings

### Block stratification (the headline)

| tier (boundary) | buy_ratio | buy vol | sell vol | premium | read |
|-----------------|-----------|---------|----------|---------|------|
| **mega ≥$10M** | **0.003** | 135,457 | 49,107,539 | $10.40B | **one-way SELL** |
| block ≥$1M | 0.305 | 2,184,753 | 4,984,242 | $1.53B | net sell |
| large ≥$100K | 0.541 | 15,679,428 | 13,290,746 | $6.24B | mild net buy |
| retail <$100K | 0.500 | 0 | 0 | $0 | n/a |
| **all tiers** | — | — | — | **$18.17B** | smart-money = SELL |

The institutional smart-money tiers (mega + block, $11.9B combined) are
decisively net-sellers. The only net-buying is the "large" tier (0.541), which is
smaller money and barely above neutral. Per the tool's own caveat — "conviction in
mega/block tiers is the institutional smart-money signal; retail-tier moves are
noise" — **this is a distribution print.**

### Largest individual prints (top-12, all SELL vs NBBO mid)

| size | price | NBBO mid | vs mid | premium | time (UTC) | vs spot |
|------|-------|----------|--------|---------|-----------|---------|
| 3,403,663 | 211.14 | 211.76 | −0.62 | $718.6M | 20:00:09 | at close |
| 3,033,922 | 211.14 | 212.26 | −1.12 | $640.6M | 20:00:16 | at close |
| 2,901,663 | 211.14 | 212.26 | −1.12 | $612.7M | 20:03:13 | at close |
| 2,746,598 | 211.14 | 212.24 | −1.10 | $579.9M | 20:00:16 | at close |
| 2,368,097 | 211.14 | 212.49 | −1.35 | $500.0M | 20:58:40 | post |
| 2,062,115 | 211.14 | 212.62 | −1.48 | $435.4M | 20:15:24 | post |
| 1,740,392 | 211.14 | 211.98 | −0.84 | $367.5M | 20:00:07 | at close |
| 1,596,602 | 211.14 | 212.13 | −0.99 | $337.1M | 20:00:13 | at close |

Every print is below its prevailing NBBO mid (the seller crossed the spread down)
and stamped at the 211.14 close. This is liquidation/distribution at the bell, not
two-way value absorption.

### Price-level clustering

- **211.14 (close): 49.69M shares / $10.49B** — the mega sell block.
- 216.00–217.14: a band of smaller prints (0.16–0.31M each) earlier in the
  session, *above* spot — consistent with the avg_price 215.47.
- Read: stock changed hands higher through the day, then a wall of size hit the
  close at 211.14 on the sell side. The dark-pool center of gravity moved *down*
  into the close.

### % of float context

Mega sell tier 49.1M sh = **0.21% of the 23.27B float** (phase-0 `fz`); top-25
prints 34.6M = 0.15% of float. Individually small vs float, but the *consistency*
(100% sell, all at the close) is the signal, not the float share.

## Tool calls (audit trail)

| Command | Result |
|---------|--------|
| `uw dark-pool block-stratified --symbol NVDA --date 2026-05-29 --json` | mega buy_ratio 0.003 (one-way sell) |
| `uw dark-pool largest --symbol NVDA --date 2026-05-29 --top-n 25 --json` | 25 prints, 100% sell-side at 211.14 close |
| `uw dark-pool price-levels --symbol NVDA --date 2026-05-29 --top-n 15 --json` | 49.7M sh at 211.14; rest at 216–217 |
| `uw insights deep-dive … --json` (`uw_dark_pool`) | 85.4M sh, avg 215.47, $18.2B |

## Tool errors

```
$ uw dark-pool ticker-summary --symbol NVDA --date 2026-05-29 --json
Error: unknown flag: --symbol     # ticker-summary has no --symbol filter;
                                  # block-stratified + largest + price-levels covered the read.
```

## Verdict for downstream phases

- **Bias from this phase:** BEARISH (institutional distribution).
- **Conviction:** 4/5 — block-stratified mega tier (0.003 buy) + 100% sell-side
  top prints + closing-cross liquidation cluster all agree.
- **Three datapoints later phases must remember:**
  1. **Mega-block buy_ratio 0.003** — institutions sold ~49M shares one-way
     ($10.4B); this is the strongest directional signal in the run so far.
  2. **Top-25 dark prints are 100% sell-side at the 211.14 close** — distribution
     at the bell, the opposite of accumulation.
  3. This **refutes the phase-1 bull thread**: calls bought at 215–217 intraday,
     but the institutional stock flow *sold* into the 211.14 close — flow/price
     divergence resolves **bearish**.
- **Open questions:** Does dealer gamma (phase-4) reinforce downside (short gamma
  below flip)? Does the 216–217 earlier-session dark activity mark a supply shelf
  that now caps rallies?
