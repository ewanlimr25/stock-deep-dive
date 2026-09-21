# Phase 2 — Dark Pool & Block Prints

**Ticker:** INTC
**As-of date:** 2026-06-26
**Generated:** 2026-06-27T09:58:20-0400
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md, phase-1-flow.md

## Summary

Net institutional dark-pool bias is **BALANCED / MECHANICAL — not directional.** The
genuine continuous-session tape (LARGE tier, **$2,083.6M across 11,191 trades**) is
essentially even at **51.9% buy / 48.1% sell**. The eye-catching "MEGA tier buy_ratio
**1.0**, $505.1M all-buy" is a **rebalance/closing-cross artifact**: 2026-06-26 is the
last Friday of June (Russell reconstitution + quarter-end), and **96.6% of the largest
blocks ($566.5M of $586.4M) printed after-hours (≥20:00) at the exact close $128.32** —
index-fund buying into the cross, classified "buy" against stale after-hours NBBO, not
conviction accumulation. **The dark pool therefore neither confirms nor refutes phase-1's
bearish options read** — it is mechanically neutral. No block is meaningful as a % of
INTC's 4.25B float (largest 1.28M sh = 0.03%). The actionable output is the 5-day price
structure: heavy overhead supply at **$140.94** (where INTC traded before this ~9%
pullback) and a pin/support shelf at **$128.32**.

## Key signals

- **LARGE-tier (continuous tape) is balanced**: buy_ratio **0.519**, $2,083.6M, 11,191
  trades — the real institutional read is two-sided [DP:block_stratified].
- **MEGA buy_ratio 1.0 ($505.1M, 11 trades) is rebalance flow** — 22/25 largest blocks
  printed ≥20:00 at $128.32 (close); discount as directional [DP:largest][DP:extended_hours].
- **Overhead supply at $140.94**: heaviest 5-day cluster, $707.6M / 5.02M sh, **+9.5%**
  above spot — the level INTC sold off from [DP:price_levels].
- **Pin/support at $128.32**: $624M / 4.86M sh cluster, −0.27% from spot — today's
  closing magnet [DP:price_levels].
- **INTC dark-pool premium rank #23** of top-30 ($2.8B total) — present but not a leader;
  MU leads the complex at $32.4B [DP:ticker_summary].

## Detailed findings

### Largest blocks (top by premium)

| Price | Size | Premium | vs spot | % float | Time (ET) |
|---|---|---|---|---|---|
| $128.32 | 1,277,294 | $163.9M | −0.35 | 0.030% | 20:00:17 |
| $128.32 | 1,015,845 | $130.4M | −0.35 | 0.024% | 21:25:30 |
| $128.32 | 447,511 | $57.4M | −0.35 | 0.011% | 20:00:09 |
| $128.32 | 270,047 | $34.7M | −0.35 | 0.006% | 20:01:47 |
| $128.32 | 238,119 | $30.6M | −0.35 | 0.006% | 20:00:27 |
| $132.87 | 79,879 | $10.6M | +4.20 | 0.002% | 12:31:42 (intraday) |

22 of 25 (96.6% of premium) printed ≥20:00 at $128.32. `trade_vs_mid` is positive on
these but the after-hours NBBO is stale (e.g. the 21:25 print shows NBBO [127.01–127.13]
with a $128.32 trade → vsmid +1.25), so the "above-mid → buy" inference is unreliable.
**Read as mechanical closing/rebalance prints, not directional accumulation.**

### Tier breakdown (buy/sell; `sell_ratio` derived = 1 − buy_ratio)

| Tier | buy_ratio | sell_ratio | buy_vol | sell_vol | Premium | Trades | Read |
|---|---|---|---|---|---|---|---|
| MEGA | **1.000** | 0.000 | 3,933,639 | 0 | $505.1M | 11 | Rebalance artifact (after-hrs) |
| LARGE | **0.519** | 0.481 | 8,404,456 | 7,790,973 | **$2,083.6M** | **11,191** | **Balanced (the real tape)** |
| BLOCK | 0.675 | 0.325 | 1,137,644 | 548,549 | $216.5M | 100 | Modest buy skew (suggestive only) |
| RETAIL | — | — | 0 | 0 | $0 | 0 | empty |

Total all tiers $2,805.2M (matches phase-0.5 DP block). The dominant, statistically
meaningful tier (LARGE, 11k trades) is a coin-flip; the only clean "buy" tier (MEGA) is
the contaminated one. Net: **no directional edge from the buy/sell split.**

### Price levels (5-day clusters; latest-anchored window)

| Price | Premium | Shares | vs spot | Note |
|---|---|---|---|---|
| **$140.94** | $707.6M | 5,020,607 | **+9.54%** | **Heaviest cluster = overhead supply/resistance** |
| **$128.32** | $624.0M | 4,863,101 | −0.27% | **Pin/support (at spot)** |
| $132.28 | $423.2M | 3,199,568 | +2.81% | Resistance |
| $131.65 | $347.1M | 2,636,910 | +2.32% | Resistance |
| $132.87 | $311.8M | 2,346,772 | +3.26% | Resistance |
| $130 / $129 | $41.3M / $35.8M | — | +1.0% / +0.3% | Minor shelves near spot |

The 5-day structure shows INTC distributed down from the ~$141 supply shelf into the
$128–133 zone; clusters are concentrated **at and above spot**, with thin institutional
print volume below $128 — i.e. **little dark-pool support documented under the current
price.** Caveat: `--days 5` anchors to the latest date (= as-of 2026-06-26), clean here.

### Extended-hours activity

15 extended-hours prints, all at $128.32 in the 20:00–21:25 window (`ext_hour_sold_codes`
present) — the same closing-cross/rebalance blocks as the "largest" set. Classic
quarter-end/Russell mechanical flow; **de-rate conviction, treat as non-directional.**

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `dark-pool largest --symbol INTC --sort-by premium --top-n 25` | top $163.9M @ $128.32 @20:00; 22/25 after-hours ← `.results[]` | top-25 |
| `dark-pool block-stratified --symbol INTC --min-tier large` | LARGE buy_ratio 0.519 ($2,083.6M/11,191); MEGA 1.0 ← `.results[]|select(.ticker=="INTC")|.<tier>.buy_ratio` | INTC row |
| `dark-pool price-levels --symbol INTC --days 5` | $140.94 $707.6M (+9.5%); $128.32 $624M ← `.results[].price_level,.total_premium` | top-15 |
| `dark-pool extended-hours --symbol INTC --top-n 15` | 15 prints @ $128.32 20:00–21:25 ← `.results[]` | top-15 |
| `dark-pool ticker-summary --top-n 30` | INTC rank #23; MU leads $32.4B ← `index("INTC")` | top-30 |

## Tool errors

None — all five reads returned valid JSON on first call.

## DATA NOTE / CORRECTION

None.

## Verdict for downstream phases

- **Bias from this phase:** **MIXED / NEUTRAL (mechanical).** Continuous tape balanced;
  the bullish-looking MEGA all-buy is rebalance noise. Does **not** confirm phase-1
  bearish; does **not** refute it either. Flag the divergence (flow bearish, DP neutral).
- **Conviction:** **2 / 5** — low directional information content.
- **Largest block as % of float:** **0.030%** (1.28M sh / 4.25B) — **not meaningful for
  this name**; INTC's 4.25B float swamps any single print. [DP:block_pct_float fz]
- **Three S/R levels for phase-9:**
  1. **$140.94** — major overhead supply/resistance (heaviest 5-day cluster, +9.5%).
  2. **$132–133** — near resistance band ($131.65 / $132.28 / $132.87 clusters).
  3. **$128.32** — pin/support shelf at spot (today's $624M closing cluster); thin
     documented dark-pool support below it.
- **Open questions:**
  - Does the phase-3 OI structure put a gamma/pin wall at $128–130 to corroborate the
    $128.32 dark-pool magnet? Where are the OI walls vs the $140.94 supply?
  - Is there any genuine intraday (continuous-session) distribution hidden under the
    rebalance prints? (LARGE tier says no — balanced.)
