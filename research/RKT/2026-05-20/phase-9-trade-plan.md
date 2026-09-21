# Phase 9 — Trade Blueprint

**Ticker:** RKT (Rocket Companies)
**As-of date:** 2026-05-20 (data: 2026-05-19)
**PM voice:** desk PM running an institutional book
**Spot reference:** $12.65 (close $12.675 on 5/19 per phase-4-structure.md)
**Upstream phases cited:** phase-1 through phase-8
**Generated:** 2026-05-20T02:20:00Z

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

The desk does not buy a naked-directional RKT trade. The single cleanest
edge is the **18.3 vol-point term-structure dislocation** — 2026-05-22
weekly IV at 85.9% versus 2026-05-29 weekly at 67.6% with an unidentified
catalyst — sitting on top of a **short-gamma dealer book** ($13 carries
-$292M of 0DTE GEX) that creates mechanical asymmetric upside if the
event resolves bullish, while the 28-session OI build and 5/5 sweep
persistence point to structural institutional positioning ABOVE current
spot [STRUCT:iv_term_structure] [STRUCT:today_gamma_flip] [FLOW:sweep_persistence].
Counterweights are real and named: phase-2 dark pool mega-tier is 100%
SELL ($60.23M today) [DP:block_stratified], market regime is
TRANSITIONAL with Financial Services -$48.8M net outflow
[MACRO:MarketRegime_2026-05-19 UW], and bullish_flow signals are running
10% win rate over the last 20 days [HIST:signal_backtest]. We express
this as a **defined-risk, vol-relative, modestly-long-delta structure**
sized below half normal (per phase-8 risk-monitor) and exit fast on a
clean ZGL break.

## Bias + conviction + horizon

- **Directional bias:** **RANGE-with-long-skew** (modest long delta into
  vol-crush; not directional long)
- **Conviction (M-01 bin):** **0.55**
- **Time horizon:** 1-5 days primary (5/22 catalyst window); 1-4 weeks
  for the back-leg of any calendar/diagonal
- **Why this bin:** phase-8 desk is split (LONG×1, SHORT×1, NEUTRAL×2,
  RANGE×1) at avg conviction 2.8/5; expected phase-10 confluence score
  in the 40–55 band → rubric mandates 0.55 [AGENT:five-agent-split].

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| Primary    | $12.65 (current) | At-market open 2026-05-20; lay calendar/diagonal into the front-week vol spike BEFORE 5/22 catalyst | [STRUCT:iv_term_structure] (5/22 85.9% vs 5/29 67.6%) |
| Aggressive | $12.52 | Add a second tranche on touch of mega-print VWAP from 5/19 (institutional support, today's largest distribution level) | [DP:price_levels] ($12.52 with $35.5M premium / 2.84M shares) |
| Fade       | $13.10 | If RKT gaps through $13 wall on 5/20–5/21 BEFORE the catalyst, fade the breakout with a small short-call hedge — pre-event chasing into a -$292M gamma wall is poor entry | [STRUCT:today_gamma_flip] ($13 = -$292M 0DTE GEX wall) |

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Hard support (thesis-breaks) | **$10.52** | [STRUCT:gex] 45-DTE Zero Gamma Level |
| Near-term support (urgent) | **$11.51** | [STRUCT:today_gamma_flip] 0DTE ZGL — break = short-gamma waterfall |
| Distribution floor / pivot | **$12.52** | [DP:price_levels] today's mega-print level / 2.84M shares |
| Most-pinged consolidation | **$12.73** | [DP:price_levels] 19 trades / $7.28M |
| Primary resistance / pivot | **$13.00** | [STRUCT:today_gamma_flip] -$292M 0DTE GEX wall + [STRUCT:gex] -$374M 45-DTE wall |
| Positive-gamma magnet / target | **$14.00** | [STRUCT:gex] +$289M 45-DTE positive gamma + [OI:biggest_increases] Aug 14C OI Δ +3,610 |
| Multi-day overhead | **$14.25** | [DP:price_levels] 5-day distribution cluster $22.98M |

## Invalidation

(per `rubrics/invalidation-rubric.md`)

- **Price-based:** **Two daily closes below $11.51** (0DTE ZGL —
  short-gamma waterfall activates and the LEAPS bull book starts to
  bleed) [STRUCT:today_gamma_flip]. Alternatively, a single intraday
  break of $10.52 with no reclaim by next day's close [STRUCT:gex].
- **Signal-based:**
  - Dark pool mega/block tier buy_ratio remains BELOW 0.40 for 2
    additional sessions (today is 0.0/0.111 — confirms continued
    distribution) [DP:block_stratified, INSIGHT:institutional_accumulation].
  - GEX flips to net positive but ZGL rises above spot (regime
    becomes positive WITHOUT a spot rally) on the next phase-4 refresh
    — means dealers de-risked without us, no fuel left for the
    squeeze [STRUCT:gex].
  - Conviction matrix flips FROM `DIRECTIONAL_SHORT` TO `DIRECTIONAL_LONG`
    with confidence > 70% — paradoxically this WOULD trigger ADD, not
    invalidate; but if it flips and we are NOT in the trade, we have
    missed it. Note for monitor [INSIGHT:conviction_matrix].
- **Macro-based:**
  - 30Y mortgage rate prints above **6.75% intraday** — cancels any
    rate-cut optionality the LEAPS book was relying on
    [MACRO:Mortgage30Y_2026-05-20 WebSearch].
  - Brent crude > **$95** on Iran escalation headline — locks in CPI
    persistence and kills 2026 cut path [MACRO:GeopoliticalRisk WebSearch].
  - **Financial Services net flow** below -$50M for a SECOND consecutive
    session (today already -$48.79M) [MACRO:SectorRotation_2026-05-19 UW].

**Exit on invalidation:** **Hard stop** for the directional debit
structure (close 100% at the price level). For the diagonal, **roll**
the long-leg out one expiry IF only the short-leg is challenged and
back-end vol has not collapsed; otherwise hard-stop.

## Sizing (% of risk, NOT dollars)

(per `rubrics/sizing-rubric.md`)

**Calculation for the directional 6/18 call debit spread:**
- Entry net debit: ~$0.30 (long 6/18 $13C ≈ $0.50 − short 6/18 $14C ≈ $0.20)
- Target value at expiry if RKT closes at $14.00: $1.00 spread − $0.30
  debit = +$0.70 profit
- Stop: full debit lost = $0.30
- `b = 0.70 / 0.30 = 2.33`
- `p = 0.55` (per conviction bin)
- `raw_kelly = (0.55 × 2.33 − 0.45) / 2.33 = (1.2815 − 0.45) / 2.33 =
  0.357 = 35.7%`
- `fraction = 0.25, cap_pct = 5`
- `suggested_size_pct = min(0.357 × 0.25, 0.05) × 100 = 5.0% (capped)`

**Final size: 2.5% of book risk** (half the suggested cap, per phase-8
risk-monitor — TRANSITIONAL regime + 10% bullish_flow backtest +
Financial Services rotation → 0.5R sizing factor applied) [AGENT:risk-monitor].

- **Deviation reason:** sized DOWN from suggested 5.0% to 2.5%.
  Justification: agent risk-monitor mandates 0.5× factor for
  TRANSITIONAL regime; bullish_flow backtest at 10% win rate; net
  defined-risk debit. No further explanation required (downward
  deviation is always permitted by the rubric).

**Important:** subtract any existing book exposure to **UWMC, KBE, XLF,
mortgage REITs (NLY/AGNC/RITM), TLT longs, homebuilders** before sizing
this trade. RKT compounds those positions as a single "long mortgage
credit + long duration" bet [AGENT:risk-monitor].

## Option structures

### Directional (primary)

- **Structure:** Long call debit spread (vertical)
- **Strikes / expiry:** Long 2026-06-18 $13 CALL / Short 2026-06-18 $14 CALL
- **Estimated debit:** $0.30 per spread (long $0.50 − short $0.20; final
  fill subject to live quote)
- **Breakeven at expiry:** $13.30 (long strike + net debit)
- **Max profit at expiry:** $0.70 per spread if RKT ≥ $14.00 at June OPEX
- **Max loss:** $0.30 per spread (full debit, defined risk)
- **Why this structure:** Expiry 2026-06-18 captures both the 5/22
  catalyst window and the FOMC 6/10 decision (the only macro re-rating
  in window per phase-6). Strikes are anchored to phase-3's call-magnet
  zone ($14 = +6,892 OI Δ across multiple expiries; +$289M positive
  gamma) and phase-4's $13 gamma wall (-$374M in 45-DTE map). IV30 at
  60.1% / 33rd percentile [HIST:iv_percentile_zscore] keeps debit
  reasonable. The vertical caps payoff at $14, which is by design — the
  next overhead level ($14.25 [DP:price_levels]) is heavy distribution
  resistance, so paying for unbounded upside is uneconomic.

### Defined-risk alternative (vol-relative diagonal)

- **Structure:** Call diagonal — short front-week, long back-week
- **Strikes / expiry:** Short 2026-05-22 $14 CALL / Long 2026-07-17 $13 CALL
- **Estimated net debit:** $0.65 per spread (long ≈ $0.75 − short
  credit ≈ $0.10)
- **Max profit (estimated):** ~+$0.85 per spread if RKT trades to
  $14.00 by 2026-05-22 expiry (short 14C pins at $0 intrinsic, long 13C
  retains $1.00 intrinsic + ~$0.50 time value)
- **Max loss:** ~$0.55 per spread (if back-leg goes to $0.10 floor and
  short-leg expires worthless)
- **Breakeven at short-leg expiry:** approximately $12.85 (depends on
  back-leg IV)
- **Why this structure:** Sells the 85.9% IV 5/22 weekly anchor against
  the 61.1% IV 7/17 back-end — captures the 24.8 vol-point
  term-structure dislocation [STRUCT:iv_term_structure] while
  maintaining LONG delta exposure to a dealer-chase through $14
  [STRUCT:gex]. If the 5/22 catalyst is bullish and dealers cover into
  $14, this is the structure that pays multiples; if it's bearish, the
  long-leg holds residual value because IV30 is at the 33rd percentile
  and back-end vol has limited downside [HIST:iv_percentile_zscore].
  This is the **earnings-scout's prescribed structure**
  [AGENT:earnings-scout].

### What we are NOT doing and why

- **No naked long stock or naked long calls:** phase-5 bullish_flow
  signal win rate is 10% over the last 20 days [HIST:signal_backtest];
  naked delta is the wrong expression in this regime.
- **No put credit spreads:** phase-4 DEX is -$2.01B [STRUCT:dex]
  meaning dealers are already structurally short puts; selling more
  puts stacks the same exposure [AGENT:risk-monitor].
- **No naked short calls or strangles:** phase-4 vanna +178k + charm
  +1.74M with positive-gamma magnet at $14 [STRUCT:vanna_charm,
  STRUCT:gex] creates squeeze risk on short-vol trades that go wrong.

## Macro overlay

**Tailwinds:**
- IV30 at **33rd percentile** + VRP -4.05% (premium-buying regime)
  [HIST:iv_percentile_zscore, HIST:vrp]
- RKT Q1 2026 beat (5/7): $2.82B adj rev, $0.15 EPS, $738M EBITDA
  [MACRO:RKT_Q126_2026-05-07 WebSearch:SEC]
- Mr. Cooper deal: $2.1T UPB servicing book provides rate-insensitive
  revenue base [MACRO:RKT_MrCooper_2025-10-01 WebSearch:prnewswire]
- SPY in uptrend +4.94% in 30d [MACRO:SPY_2026-05-19 UW]

**Headwinds (major):**
- **30Y mortgage rate 6.58%** on 5/20, up materially since 5/12 CPI
  print [MACRO:Mortgage30Y_2026-05-20 WebSearch:money.com]
- **April CPI +3.8% YoY** (highest since May 2023) released 5/12
  [MACRO:CPI_2026-04 WebSearch:multiple]
- **Financial Services net flow -$48.79M** today [MACRO:SectorRotation_2026-05-19 UW]
- **TRANSITIONAL regime** with 34.7% bullish breadth and explicit
  "half position sizes; defined-risk" guidance
  [MACRO:MarketRegime_2026-05-19 UW]
- **Iran war** keeping oil/inflation elevated
  [MACRO:GeopoliticalRisk_2026-05 WebSearch:nora]

**Net:** **headwind-dominant**. Macro alone would push the trade
toward NEUTRAL/SHORT; the structure expresses LONG ONLY because the
gamma/vol-relative microstructure offers asymmetric event-vol payoff
within a defined-risk envelope.

## Catalyst calendar (next 30d)

| Date | Event | Impact direction | Source |
|------|-------|------------------|--------|
| **2026-05-22** | **Unknown catalyst at 85.9% weekly IV** (Conference Board LEI + State Employment 10am ET are the only known macro events; not enough to justify the spike) | **Binary (+/-)** — primary trade target | [STRUCT:iv_term_structure], phase-6 |
| 2026-06-09 | Existing-Home Sales (April release) | (-) Sector driver | phase-6 |
| **2026-06-10** | **FOMC decision + Powell presser + SEP update** | **Major** — only macro re-rating in window | phase-6 |
| 2026-06-(mid) | May 2026 CPI release | Major — does the April 3.8% repeat? | phase-6 |
| 2026-06-18 | June monthly OPEX (matches our directional spread expiry) | Neutral / liquidity | phase-3 |
| 2026-07-17 | July OPEX (matches diagonal long-leg expiry) | Neutral / liquidity | phase-1 |
| 2026-07-30 | RKT Q2 2026 earnings | High — but outside trade window | [INSIGHT:deep_dive] |

## Post-trade monitoring checklist

- [ ] **Daily:** Re-run `dark_pool_block_stratified` for RKT. Watch for
      mega-tier buy_ratio to flip above 0.55 (confirmation of seller
      exhaustion → ADD trigger). [DP:block_stratified]
- [ ] **Daily:** Re-run `options_structure_gex` for RKT. Watch for
      ZGL to drift toward spot from below (regime healing). If ZGL
      jumps above spot AGAIN without spot rallying, that's signal-based
      invalidation. [STRUCT:gex]
- [ ] **Daily:** Track the 30Y mortgage rate. **HARD STOP if > 6.75%**
      intraday. [MACRO:Mortgage30Y]
- [ ] **Daily:** Monitor Financial Services sector net flow via
      `risk_market_regime`. Two consecutive sessions below -$50M =
      macro invalidation. [MACRO:SectorRotation UW]
- [ ] **5/22 by close:** Identify and document the catalyst. If the
      catalyst is identified and is RKT-specific (e.g., refinancing,
      secondary, GSE/FHFA action), reassess sizing and consider
      adding the directional spread if confirmed bullish.
- [ ] **Daily:** Watch for Iran-war escalation headlines impacting
      Brent (HARD STOP if > $95) [MACRO:GeopoliticalRisk]
- [ ] **Post-5/22:** If diagonal pays out at $14, roll the long leg up
      and out (7/17 13C → 8/21 14C) to extend exposure into the FOMC
      6/10 window. [STRUCT:gex, $14 magnet]
- [ ] **Weekly:** Re-run sweep_persistence with days=5. If RKT drops
      out of the top sweep persistence list (stops being 5/5),
      downgrade conviction by one bin. [FLOW:sweep_persistence]

## Citations summary (M-04: ≥3 distinct upstream datapoints in thesis)

1. **[STRUCT:iv_term_structure]** — 2026-05-22 weekly IV at 85.9% vs
   2026-05-29 weekly at 67.6% — phase-4-structure.md §IV term structure
2. **[STRUCT:today_gamma_flip]** — $13 strike carries -$292M of 0DTE
   GEX; total 0DTE GEX = -$406M; ZGL 0DTE = $11.51 —
   phase-4-structure.md §Today's gamma flip
3. **[FLOW:sweep_persistence]** — RKT 5/5 sessions, consistency 1.0,
   dominant bullish, $5.02M cumulative — phase-1-flow.md §Sweep persistence
4. **[DP:block_stratified]** — mega tier 100% SELL ($60.23M); block
   tier 89% SELL — phase-2-dark-pool.md §Tier breakdown
5. **[MACRO:MarketRegime_2026-05-19 UW]** — regime TRANSITIONAL;
   Financial Services flow -$48.79M — phase-6-macro.md §Market regime
6. **[HIST:signal_backtest]** — bullish_flow signal 10% win rate /
   -1.57% avg over 20 days — phase-5-historical.md §Signal backtest
7. **[AGENT:earnings-scout]** + **[AGENT:risk-monitor]** — defined-risk
   diagonal sized at 0.5R, harvest the 18-point IV dislocation —
   phase-8-agent-views.md

Spot-check verification:
- Cite 1: phase-4-structure.md §IV term structure clearly lists
  `2026-05-22 | 85.9% | 1,209 contracts` and `2026-05-29 | 67.6% | 437
  contracts`. ✓
- Cite 4: phase-2-dark-pool.md §Tier breakdown lists
  `MEGA (≥$10M) | 2 | $60.23M | buy_ratio 0.000` and
  `BLOCK (≥$1M) | 9 | $21.90M | buy_ratio 0.111`. ✓
