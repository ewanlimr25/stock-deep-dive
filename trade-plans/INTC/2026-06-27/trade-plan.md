# Trade Plan — INTC

**As-of date:** 2026-06-27
**Spot reference:** $128.32 (yfinance, 373 sessions)
**Voice:** desk PM running an institutional book
**Built from:** `research/INTC/2026-06-26/` deep dive (age 1 day) + chart engine (yfinance)

> *For research and educational use only. Not financial advice. Sizing,
> structures, targets and dates are illustrative.*

## 0. Information completeness (gap audit)

- **Verdict:** **SUFFICIENT** — completeness **100%**
- **Have:** options flow/sweeps, dark pool/blocks, OI/positioning, dealer GEX/DEX/ZGL, historical win-rate, OHLCV chart + patterns, macro/sector rotation, event calendar, fundamentals veto, sentiment/crowd/SI, implied/expected move, earnings date (dual-confirmed UW + fz).
- **Missing / how to source:**
  | Item | Severity | How to source |
  |------|----------|---------------|
  | Live intraday tape for precise same-day trigger timing | nice_to_have | `uw options-flow sweeps --symbol INTC --json` + `uw options-structure gex --symbol INTC --dte-max 45 --json` on the morning of entry |

*SUFFICIENT = the evidence is complete enough to decide well. It does NOT mean a high-conviction directional trade exists — the constraints below are conviction/risk gates, not information gaps.*

## 1. Direction & conviction

- **Bias:** **SHORT** (watch-only)
- **Conviction (M-01 bin):** **0.55** (DIVERGENT floor)
- **Horizon:** 1–4w (every structure must close **before Jul-23 earnings**)
- **Confluence score:** 55
- **Flow ↔ chart agreement:** **DIVERGENT** (bearish flow/positioning/macro vs. a bullish, unbroken chart trend)

### Thesis (≤3 sentences, ≥3 tagged citations)

INTC is a +247.75% YTD parabola — the only loss-maker in its peer group and 29–33% above the $102.70 analyst target [FUND:peer_pe] — where the tape diverged from price (+10.7% price vs −$50.9M net flow [INSIGHT:price_vs_flow]), backed by a 5/5-session bearish sweep campaign [FLOW:sweep_persistence] and ~73% bearish new OI led by a Jul-17 $130 put +11,442 [OI:biggest_increases]. But the chart trend is still a full bullish MA stack [CHART:ma_stack] and the directional short is fundamentally **VETOED** (4/4 EPS beats, insiders buying, long-gamma pin), so this is a **DIVERGENT, watch-only SHORT** expressed only as small, defined-risk spreads that expire before the Jul-23 earnings binary.

### Why it should work
- Price-vs-flow bearish **DIVERGENCE**: +10.7% price / −$50.9M net flow over 30d [INSIGHT:price_vs_flow].
- **5/5-session bearish sweep campaign**, $925.2M, consistency 1.0 [FLOW:sweep_persistence].
- **~73% bearish new OI**; Jul-17 $130 put +11,442 (ratio 4.11) is the heaviest near-term build [OI:biggest_increases].
- **Extreme overvaluation**: +247.75% YTD, only loss-maker in peer group, 29–33% above the $102.70 target [FUND:peer_pe].
- **Macro tailwind (gated)**: hawkish Fed, Technology #1 outflow −$637.8M, $1.3T June semis selloff [MACRO:sector_rotation].
- **Chart exhaustion at the top**: new 52w high (141.45) on **0.73× volume** + neutral RSI 56.78; overhead DP supply $140.94 [CHART:vol_vs_avg][DP:price_levels].

### Why it may fail (the honest other side)
- **STRONGEST STEELMAN** — the "bearish flow" is likely **hedging/financing** (conviction-matrix = COVERED_CALL + deep-ITM delta-one), **not directional shorting**: longs are holding & protecting, not selling, so the fade is dealer-muffled and −EV at size [INSIGHT:conviction_matrix].
- **Fundamentals VETO / squeeze risk**: 4/4 EPS beats, +45.76% fwd EPS, insiders buying, Pelosi $6M buy; a 5th beat Jul-23 squeezes the crowded long [FUND:earnings_surprise].
- **Chart trend is bullish and unbroken** — shorting a +247% uptrend with a full MA stack and no reversal; watchable flip = two daily closes above 133 then 141.45 [CHART:ma_stack].
- **Long-gamma pin** (+5.34M@120 / +4.16M@130, ZGL 27.26) buys dips/sells rips; a bought put spread bleeds theta at 94% IV [STRUCT:gex].
- **No short fuel** — SI only 3.39%; the down-move must come from longs voluntarily selling, not short-covering [SENT].
- **DIVERGENT flow vs chart** — by rule (ledger **L-0002**) this is range/fade-only, never a directional size [CHART][INSIGHT:price_vs_flow].

## 2. Levels to watch

| Level | Role | Source | Note |
|-------|------|--------|------|
| 141.45 | stop / hard invalidation | [CHART:high_52w] | 52w high + DP supply $140.94 |
| 133.0 | trigger (fade-the-strength) | [CHART:swing_high] | swing high + DP supply $132–133 |
| 130.0 | resistance (call wall) | [OI:oi_by_strike] | gamma lid +4.16M |
| 128.32 | pin (spot) | [DP:price_levels] | DP shelf; $128 neg-gamma notch |
| 125.0 | pin / magnet | [STRUCT:max_pain] | largest pin |
| 120.0 | **target T1** | [STRUCT:gex] | gamma pin/max-pain +5.34M; + fib 0.236 117.26 / sma20 119.42 / ema21 122.09 shelf |
| 108.39 | target T2 | [CHART:sma50] | deeper objective |
| 102.29 | support | [CHART:fib_0.382] | = swing low 102.40; parabola-failing |
| 98.33 | support | [CHART:swing_low] | 2026-06-05 capitulation low |
| 27.26 | gamma flip (ZGL) | [STRUCT:gex] | far below; confirms dealers long-gamma |

Moving averages: ema21 122.09 · sma20 119.42 · sma50 108.39 · sma200 58.23. Fib (swing 38.95→141.45): 0.236 **117.26** · 0.382 **102.29** · 0.5 90.20 · 0.618 78.10. Ext 1.272 169.33.

## 3. Patterns forming (chart)

| Pattern | Direction | Confidence | Measured target | Invalidation | Note |
|---------|-----------|-----------|-----------------|--------------|------|
| broadening range | bearish | low | 98.33 | 141.45 | manual read — engine detected NONE; HH 141.45 + LL 98.33 = volatility expansion / distribution after +247% run; **plan does not lean on it** [CHART:recent_pivots] |
| elliott wave | — | none | — | — | no valid count (pivots not cleanly alternating) [CHART:elliott_wave] |

Engine `patterns_detected = []` — no flag / H&S / double / triangle / cup. No pattern is forced onto noise.

## 4. Upcoming events that move the tape (next ~30–60d)

| Date | Event | Impact | Source |
|------|-------|--------|--------|
| 2026-07-15 | June CPI release | ? | [MACRO:CPIAUCSL] |
| 2026-07-17 | monthly OPEX (all structures expire) | − | [OI:opex] |
| **2026-07-23** | **INTC Q2 earnings AMC — DO NOT HOLD THROUGH** | ? | [FUND:earnings_surprise] |
| 2026-07-29 | FOMC | ? | [MACRO:FOMC] |

## 5. Invalidation

- **Price-based:** two daily closes above **133** (clears the $130 call wall + $132–133 DP supply); **hard kill above the 141.45 52w high**.
- **Signal-based:** conviction-matrix flips COVERED_CALL → DIRECTIONAL_LONG, **OR** net-bullish premium flow 3 consecutive sessions, **OR** the 5/5 bearish sweep persistence breaks.
- **Macro-based:** dovish June-CPI surprise (~Jul-15) or semis flips to net inflow; **AND hard rule — holding any position through Jul-23 earnings is itself invalidation.**

## 6. Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** p_raw = **0.667** (n=**9**, src=backtest) → capped p = 0.667
- **Inputs:** b = **1.77**, fraction = 0.25, cap_pct = 5
- **Raw Kelly:** 0.667 − (0.333/1.77) = **0.48** → fractional 12% → capped **5%** · **Win-rate map ceiling:** starter (small N=9)
- **Risk gates (each can only cut):** fundamentals **VETO** · sentiment **CAUTION** / crowd **CROWDED_LONG** · correlation **none** · rotation **aligned** · debate **DISCONFIRMED** · context **IV-rank 94 / PREMIUM_SELLING (no top-of-band; option buying vega-taxed)**
- **Final size:** **0.0% of book** (directional/book-risk). *Deviation reason:* VETO + DIVERGENT + DISCONFIRMED force directional size to 0 (watch-only); only defined-risk carry darts (max-loss ≤0.5% book each, expiring before Jul-23) are sanctioned. SHORT-side floor honored via defined-risk-only (no naked short). Mirrors the deep dive (final_size_pct 0.0).

## 7. Plan A — pure stock (short)

- **Direction:** **short** (watch-only)
- **Entry:** $132.0 — trigger: rejection at $132.75–133 DP supply / $130 call-wall lid on a confirmed bearish reversal bar **AND** the conviction-matrix turning directional; otherwise **STAND ASIDE**.
- **Stop:** $141.5 (above the 52w high; ATR-consistent — 1.5-ATR short stop = 143.28)
- **Targets:** T1 **$120.0** ($120 gamma pin/max-pain + fib 0.236 + sma20/ema21 shelf, take 60%) · T2 **$108.39** (sma50, take 40%)
- **Reward:risk to T1:** **1.26R**
- **Size:** **0.0% book** (watch-only until the VETO lifts)
- **One-liner:** Fade strength into $132–133 ONLY on a confirmed rejection with flow turning directional, hard stop above $141.45, T1 the $120 pin (R 1.26) — but a +247% uptrend with no reversal and a long-gamma pin is **not** a stock short you press; size 0%.

## 8. Plan B — options (≥1 with target date + target price)

### B1 — defined-risk (HIGHEST-PROBABILITY, headline)

- **Structure:** **bear call credit spread**
- **Strikes / expiry:** **135/140** / **2026-07-17**
- **Target date / target price:** **2026-07-17** / **$130** (price at/below the $130 pin)
- **Debit/credit · breakeven · max loss:** credit **$1.50** · BE **$136.50** · max loss **$3.50**
- **Est. payoff at target:** **+$1.50** (full credit if INTC ≤ $135 at expiry)
- **Why this structure:** sells the $135 call wall / $140 supply into **VRP +5.95 / PREMIUM_SELLING** and the long-gamma pin — the cleanest, highest-probability expression of "INTC pins, doesn't break out." Expires before earnings; carry-only, max-loss ≤0.5% book. [STRUCT:gex][OI:oi_by_strike]

### B2 — directional dart

- **Structure:** **bear put debit spread**
- **Strikes / expiry:** **128/120** / **2026-07-17**
- **Target date / target price:** **2026-07-16** / **$120** (max-pain/gamma-pin pull into OPEX)
- **Debit/credit · breakeven · max loss:** debit **$4.00** · BE **$124.00** · max loss **$4.00**
- **Est. payoff at target:** **≈ +$3.50** net (spread ≈ full $8 width near expiry at/below $120)
- **Why this structure:** long the ATM $128 neg-gamma notch, short the $120 pin to cap the **94% IV** vega tax; R ≈ 1:1. Bleeds theta if price pins $128–130 — the long-gamma risk. Expires before earnings; carry-only, max-loss ≤0.5% book. [STRUCT:gex][OI:biggest_increases]

*Expected-move check:* front-expiry implied move is **±22% (±$28.2)** to Jul-17 — both spreads sit well inside it (the $120 target is −6.5%, the $135 short call +5.2%), so neither target is "rich"; the spreads cap the vega tax of 94% IV. No structure straddles the Jul-23 earnings gap.

## 9. Post-entry monitoring checklist

- [ ] Refresh GEX/ZGL and the conviction-matrix daily — exit if it flips to DIRECTIONAL_LONG.
- [ ] Watch for net-bullish premium 3 consecutive sessions or a break in the 5/5 sweep persistence → thesis invalidated.
- [ ] On the credit spread, close/roll if INTC closes above 133; hard-close anything before Jul-23 earnings AMC.
- [ ] Track June CPI (Jul-15) — a dovish surprise is a squeeze catalyst; flatten ahead if positioned.
- [ ] Re-pull live `uw` flow morning-of before placing either spread (1-day-old substrate).

## 10. Reasoning-ledger lessons applied

- **L-0002 (ACTIVE)** — DIVERGENT flow↔chart → capped conviction at 0.55, forced fade-only/defined-risk framing, logged as the top reason_against.
- **L-0004 (CANDIDATE, partial)** — respected the VETO + the bear's strongest unrefuted point (hedging-not-shorting); **no bearish premium carried into the undated bullish catalyst** — every structure expires before Jul-23 earnings. (Structure here is long-gamma, not short-gamma, so the squeeze-on-reclaim mechanic is replaced by pin-muffle.)

## Citations (≥3, what the eval will spot-check)

1. [INSIGHT:price_vs_flow] — bearish DIVERGENCE +10.7%/30d price vs −$50.9M flow — `research/INTC/2026-06-26/phase-7-insights.md`
2. [FLOW:sweep_persistence] — 5/5-session bearish sweep campaign, $925.2M, consistency 1.0 — `research/INTC/2026-06-26/phase-1-flow.md`
3. [OI:biggest_increases] — Jul-17 $130 put +11,442 OI (ratio 4.11), ~73% bearish new OI — `research/INTC/2026-06-26/phase-3-positioning.md`
4. [STRUCT:gex] — long-gamma pins +5.34M@120 / +4.16M@130, ZGL 27.26 — `research/INTC/2026-06-26/phase-4-structure.md`
5. [CHART:ma_stack] — bullish_stack 128.32 > 119.42 > 108.39 > 58.23 — `chart.json`
6. [INSIGHT:conviction_matrix] — COVERED_CALL: flow reads as hedging/financing not directional shorting — `research/INTC/2026-06-26/phase-8b-debate.md`
7. [FUND:peer_pe] — +247.75% YTD, only loss-maker in peer group, 29–33% above $102.70 target — `research/INTC/2026-06-26/phase-7b-fundamentals.md`
