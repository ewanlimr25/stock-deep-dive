# Phase 9 — Trade Blueprint

**Ticker:** HOOD
**As-of date:** 2026-06-05
**PM voice:** desk PM running an institutional options-overlay book
**Spot reference:** 82.47 (phase-1 `[FLOW:screener.close]`)
**Generated:** 2026-06-07T14:15:00-04:00
**Upstream phases cited:** phase-0.5 through phase-8b

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

HOOD has run a five-session bearish options campaign — top-sweeper 5/5 days,
dominant_direction bearish, consistency 1.0, $317.8M cumulative sweep premium
[FLOW:sweep_persistence] — into a dealer book that is short gamma with spot
6.5% below the 87.45 zero-gamma level and Jun-18 max-pain gravity at 80 on the
chain's biggest expiry (21.39% of all OI) [STRUCT:gex][STRUCT:max_pain]
[OI:term_structure]. The macro overlay pushes the same way: UW regime
TRANSITIONAL with 29.4% bullish breadth and "half position sizes" guidance,
VIX 15.4→21.5, and a hot-payrolls hike repricing into the June-17 FOMC
[MACRO:MarketRegime_2026-06-05 UW][MACRO:PAYEMS_2026-05 FRED], while the
bearish_flow signal class carries an 87.5% historical 5-day win rate (N=8,
market-wide) [HIST:signal_backtest]. I want the mechanical drift from ~82.5
into the 80 magnet over the nine trading days into Jun-18 OPEX — but the
fundamental gate (7b VETO: Malka's ~$36M open-market buy at 80.39–83.45 +
a franchise compounding at +41.5% revenue [FUND:insider_transactions]
[FUND:metric]) forbids a naked short; this is a **defined-risk carry trade
only**.

## Bias + conviction + horizon

- **Directional bias:** SHORT (plurality of phases 1–8; 7b/7c/8b cut size,
  never set bias)
- **Conviction (M-01 bin):** **0.65**
- **Time horizon:** 1-4w (nine trading days into 2026-06-18 OPEX)
- **Why this bin:** Provisional confluence ≈66 (band 65–79 → 0.75), but I am
  deviating DOWN one bin — see below.

### Conviction deviation (downward)

Phase-10's band points at 0.75; I'm taking 0.65. Reasons: (1) the desk split
2 SHORT / 2 NEUTRAL with uniform conviction 2.0 — the phase-8 heuristic for a
split desk targets 0.55–0.65 and defined-risk; (2) the 7b VETO means the
narrative confidence is in the *path*, not the destination — the structural
drift is well-supported but the underlying business actively fights the
thesis. Downward deviation needs no escape hatch (only upward does).

## Entry zones

| Entry type | Price | Trigger condition | Source |
|---|---|---|---|
| Primary | 82.50–83.00 | rejection at the Jun-12 max-pain 83 / fresh DP shelf 82.85 — short the failed retest | [STRUCT:max_pain][DP:price_levels] |
| Aggressive | 84.50–85.00 | fade a relief pop into the 85 call wall (≤30DTE net_oi +14,521) / DP 84.50 cluster | [OI:oi_by_strike][DP:price_levels] |
| Fade (plan B counter) | >87.45 on reclaim+hold | ZGL reclaim flips dealers long-gamma → counter-trade long toward the 90 wall | [STRUCT:gex][OI:oi_by_strike] |

## Levels to watch

| Type | Level | Source |
|---|---|---|
| Support | 80.00 (max-pain magnet + GEX +2.86M shelf); 79.78–80.60 block prints; then 75 put wall (net_oi −8,975 ≤30DTE) | [STRUCT:max_pain][DP:largest][OI:oi_by_strike] |
| Resistance | 85–86 call shelf; 88.16–88.33 DP overhead ($121M, earlier-week closes); 90 hard wall (net_oi +43,361, GEX +9.16M) | [OI:oi_by_strike][DP:price_levels][STRUCT:gex] |
| Gamma flip | 87.45 (±2% band; intraday tool n/a on an as-of run) | [STRUCT:gex] |
| Largest pin | Jun-12: 83 (+0.6%); **Jun-18: 80 (−3.0%)** — native max-pain values | [STRUCT:max_pain] |

Price-context color (advisory): RSI(14) 51.45 — neutral, no oversold excuse to
skip the entry; price is −46.4% from the 52-week high and +29.8% off the low,
above the 20/50 SMAs, below the 200 [HIST:rsi fz][HIST:52w_proximity fz]. Not
a stretched short at entry; never enters the sizing math.

## Invalidation

- **Price-based:** **two daily closes above 85.00** (the call-wall shelf
  [OI:oi_by_strike] and DP 84.50/86.24 cluster zone [DP:largest]) — OR a single
  intraday reclaim-and-hold of **87.45** (ZGL [STRUCT:gex]), whichever comes
  first. Exit: **hard stop, close 100%** (debit structure).
- **Signal-based:** daily net options flow prints bullish ≥ +$5M for 2
  consecutive sessions [HIST:cumulative_premium_flow], OR dark-pool block-tier
  buy_ratio ≥ 0.60 on any session [DP:block_stratified], OR conviction-matrix
  flips to DIRECTIONAL_LONG [INSIGHT:conviction_matrix].
- **Macro-based:** FOMC 2026-06-17 delivers a *dovish* surprise (hold +
  dovish guidance into the soft-landing tape) [MACRO:FOMC_2026-06-17], OR a
  confirmed SpaceX-IPO-access gap that opens HOOD above 85
  [SENT:company_news] — the strongest_bear_point of the debate
  [DEBATE:strongest_bear_point].

## Sizing (% of book risk, NOT dollars)

- **Kelly p (empirical):** p_raw = **0.875** (n=8, source=backtest,
  market-wide bearish_flow class — not HOOD-specific)
  [HIST:signal_backtest] → N-cap for n<10 is 0.75 → **capped p = 0.75**
- **Kelly inputs:** entry 82.50, target 80.00 (Jun-18 max-pain), stop 85.00 →
  b = |82.50−80.00| / |85.00−82.50| = 2.50/2.50 = **1.0**; fraction = 0.25;
  cap_pct = 5
- **Raw Kelly:** (0.75×1.0 − 0.25)/1.0 = **0.50** → suggested = min(0.50 ×
  0.25 × 100, 5) = **5.0%** · **Win-rate map ceiling:** p ≥ 0.70 → full
  (≤cap) — Kelly and map agree pre-gates
- **Risk gates (in order; cuts only):**
  1. **Fundamentals (7b): VETO** → naked directional short = **watch-only /
     0%**; defined-risk carry structure permitted, marked
     "fundamentals-vetoed, carry only", at ≤ half (2.5%)
  2. **Sentiment/crowd (7c): CAUTION** (crowd_state BALANCED; contrary axis =
     SpaceX/PDT catalyst proximity + disclosed insider buy) → cut one step:
     half → starter ⇒ **carry budget 1.25%**
  3. **Correlation cluster (6/8): none** — HOOD in no flagged pair (floor
     0.608; CRM/NOW/PATH cluster belongs to sibling blueprints) → no-op
  4. **Sector rotation (6): aligned** (Tech-cohort outflow −$807.6M,
     decelerating tilt) → no cut
  5. **Debate (8b): bull_residual 0.65 vs bear_residual 0.55 →
     disconfirmed=false** → no bin-shift, no cut
- **Context modifier (0.5):** GENUINELY_UNUSUAL (direction-only) → no-op on
  size; size-based confluence was never claimed
- **Final size: directional 0% (watch-only) — recorded as final_size_pct = 0
  per the VETO convention; the permitted defined-risk carry (max-loss ≤ 1.25%
  of book risk) is documented in the structure notes, not the directional
  size**
- **Deviation reason:** none (downward-only adjustments; upward forbidden —
  two gates fired)

## Option structures

Expected-move check (N4): front-expiry implied move ±0.727% / $0.60
[CTX:implied_move_pct] — but realized daily swings ran ±6% this week
[HIST:trend]; the implied print badly understates the regime, so structures
are sized to the *realized* band and the −3.0% target sits well inside one
realized daily move (no richness problem). Both expiries deliberately include
FOMC 6/17 (the thesis IS the OPEX/FOMC window); a gap of expected-move
magnitude cannot exceed the stop because both structures are max-loss-capped
by construction.

### Directional (primary) — "fundamentals-vetoed, carry only"

- **Structure:** bear put debit spread
- **Strike(s) / expiry:** long 84P / short 80P, 2026-06-18
- **Debit/credit:** ≈ $2.20 debit (indicative — modeled from the as-of chain's
  78.3% Jun-18 IV [STRUCT:iv_term_structure]; verify live)
- **Breakeven:** ≈ 81.80
- **Max loss:** $2.20/spread; premium at risk ≤ 1.25% of book
- **Max gain:** $1.80 at ≤80 (target = short wing = the max-pain magnet)
- **Why this structure:** VRP is −0.0858 — the tool's own regime is
  PREMIUM_BUYING ("vol cheap vs realised") [HIST:vrp], and the skew is
  COMPLACENT with 25Δ puts at 67.4% vs calls 71.7% [STRUCT:term_skew] — I am
  buying the cheapest side of a surface that under-prices delivered movement.
  Short wing at 80 harvests the pin rather than paying for a crash the flow
  never bought.

### Defined-risk alternative

- **Structure:** call credit spread (sells the invalidation shelf)
- **Strike(s) / expiry:** short 86C / long 90C, 2026-06-18
- **Debit/credit:** ≈ $1.40 credit (indicative; Jun-18 90C printed ~$2.09–2.21
  avg with spot 83–85 on the as-of tape [FLOW:sweeps])
- **Breakeven:** ≈ 87.40 — almost exactly the 87.45 ZGL [STRUCT:gex]
- **Max loss:** $2.60/spread (width 4 − credit); ≤ 1.25% of book if used
  instead of (not alongside) the put spread
- **Note:** short strike 86 = the 86 call wall (net_oi +16,953 ≤30DTE)
  [OI:oi_by_strike]; the structure profits if HOOD stays below the shelf —
  expresses "capped upside" without needing the 80 magnet to complete.

## Macro overlay (phase-6)

- **Tailwinds (to the short):** hike repricing off +172k payrolls vs ~80k est
  [MACRO:PAYEMS_2026-05 FRED]; VIX 21.51 regime stress [MACRO:VIX_2026-06-05
  UW]; Tech-cohort outflow −$807.6M with 5-session tilt deceleration −71%
  [MACRO:sector_flow UW]; sticky inflation (core PCE +3.29%)
  [MACRO:PCEPILFE_2026-04 FRED]; record-low UMich 44.8 pressures retail
  inflows [MACRO:UMich_2026-05 WebSearch].
- **Headwinds (to the short):** DB PT raise to $98 on the as-of day
  [MACRO:analyst WebSearch:marketbeat.com]; SpaceX-IPO-access catalyst window
  [SENT:company_news]; Financials sector flow mildly bid +$150.7M if HOOD
  re-couples [MACRO:sector_flow UW]; UW guidance itself says "wait for
  clarity" — TRANSITIONAL is not RISK-OFF [MACRO:MarketRegime UW].
- **Net:** headwind for HOOD (= tailwind for this short), conviction 4
  (phase-6 verdict).

## Catalyst calendar (next 30d)

| Date | Event | Impact direction (on this SHORT) |
|---|---|---|
| ~2026-06-10 | May CPI release | ? (hot = +, cool = −) |
| 2026-06-17 | FOMC + Warsh presser (T-1 to OPEX) | ? (hawkish = +, dovish = −) |
| 2026-06-18 | Jun OPEX — 21.39% of HOOD OI, max-pain 80 | + (structural gravity) |
| mid-June (date fluid) | SpaceX IPO access via HOOD | − (gap-up risk, the debate's strongest bear point) |
| 2026-07-29 | Q2 earnings | outside window (structures expire 6/18) |

## Post-trade monitoring checklist

- [ ] Daily: GEX/ZGL refresh — a reclaim of 87.45 or a regime flip to
      POSITIVE voids the drift mechanics (phase-4 re-run).
- [ ] Daily: net options flow sign — two consecutive bullish sessions ≥ +$5M
      triggers the signal invalidation (phase-5 cumulative flow).
- [ ] Daily: dark-pool block-tier buy_ratio — ≥ 0.60 on a session = informed
      accumulation against the short (phase-2 re-run).
- [ ] Headline watch: SpaceX IPO access dates + any HOOD-specific 8-K /
      insider Form 4 (a *second* distinct open-market buyer joining Malka
      upgrades the 7b contradiction into a cluster — exit).
- [ ] 2026-06-10 CPI + 2026-06-17 FOMC: re-assess the carry into each binary;
      the put spread may be closed into FOMC if it has captured >60% of max
      gain (majority of the decay realized).
- [ ] Jun-18 expiry: position dies at OPEX by construction; do not roll
      without a fresh full run.

## Citations summary (M-04; phase-10 spot-checks these)

1. [FLOW:sweep_persistence] — 5/5 sessions bearish-dominant, consistency 1.0,
   total_sweep_premium $317,794,122 — phase-1-flow.md §Key signals
2. [STRUCT:max_pain] — Jun-18 max_pain_strike 80, distance −3.0%, on
   total_oi 391,214 (21.39% of chain [OI:term_structure]) —
   phase-4-structure.md §Max pain
3. [HIST:signal_backtest] — bearish_flow win_rate 87.5%, total_signals 8,
   avg_move_pct −2.73 — phase-5-historical.md §Signal backtest
4. [MACRO:MarketRegime_2026-06-05 UW] — "TRANSITIONAL — Mixed signals, reduce
   position size"; breadth 29.4% bullish — phase-6-macro.md §Market regime
5. [FUND:insider_transactions] — Malka 249,000 sh @ 80.3944 (05-28) + 181,000
   @ 83.4467 (06-03) ≈ $36M — phase-7b-fundamentals.md §Insider signal
6. [DEBATE:strongest_bear_point] — disclosed insider buying in the profit
   zone + SpaceX gap risk — phase-8b-debate.md §Disconfirmation verdict
