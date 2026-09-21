# Phase 9 — Trade Blueprint

**Ticker:** MSFT
**As-of date:** 2026-06-01
**PM voice:** desk PM running an institutional book
**Spot reference:** $459.77 (close $460.52) (phase-1 `top_premium_trades`)
**Upstream phases cited:** phase-0.5 through phase-8b
**Generated:** 2026-06-02T11:34:36Z

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

MSFT's bullish call tape is real but two-way and normal-magnitude — net flow only
**+$81.2M on $1.39B gross call premium** [FLOW:insights_deep_dive] — and it runs
straight into a **long-gamma dealer pin (GEX +$268.7M centered at 460, max pain
417.5 across every near-term expiry)** that caps upside and pulls toward OPEX
[STRUCT:gex] [STRUCT:max_pain]. The `bullish_flow` signal class is **edge-negative
here (44.4% win, −1.25% avg, n=9)** [HIST:signal_backtest] and the whole desk
returned **RANGE 4-of-4** [AGENT:risk-monitor] into a **TRANSITIONAL,
"half-size / iron-condors-in-range"** regime [MACRO:MarketRegime]. Net: there is no
directional edge to buy — **fade the crowded, capped upside with a small
defined-risk call credit spread, not a long.**

## Bias + conviction + horizon

- **Directional bias:** **RANGE** (plurality of phases 1–8: phase-8 unanimous RANGE;
  phase-4 long-gamma pin; phase-7 MIXED). The bullish flow (phase-1) and bullish
  fundamentals (phase-7b) are the noted contradictions to the range, not a
  directional green light.
- **Conviction (M-01 bin):** **0.65** (moderate edge — in the *range* thesis, with
  real disconfirming evidence on both sides).
- **Time horizon:** **1-4w** (through June OPEX 06-18).
- **Why this bin:** phase-10 confluence is expected mid-band (~60) — the data
  confluences well on "pinned/range-bound" (phase-4 ++, phase-8 4/4) but is fought
  by the bullish flow/fundamentals; the phase-7c CAUTION penalty caps it. 0.65 is
  conviction in the *range holding*, NOT in a directional move.

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| Primary | **$470–480** | Sell the call spread on a tag/rejection of the 470–480 call-wall / GEX cap (fade the rip) | [STRUCT:gex] / [OI:oi_by_strike] |
| Aggressive | **$460 (spot)** | Initiate the call credit spread now — IV still bid pre-NFP, harvest elevated event premium into the long-gamma pin | [STRUCT:front_end_iv_ratio] |
| Fade (plan B) | **>$480** | Two daily closes above 480 on expanding (non-0DTE) volume → pin broke UP, cover the short calls & stand down (longs validated) | [AGENT:accumulation-hunter] |

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Support | **$450** (then 427, then 417.5) | [DP:price_levels] $450 shelf / [STRUCT:max_pain] 417.5 / [OI:oi_by_strike] |
| Resistance | **$480** (then 500) | [OI:oi_by_strike] call_wall_resistance / [STRUCT:gex] cap |
| Gamma pin (range center) | **$460** | [STRUCT:gex] +$57.6M GEX strike (native) |
| Pin magnet (OPEX gravity) | **$417.5** (06-18 max pain, −9.3%) | [STRUCT:max_pain] (native) |
| Short-gamma flip (downside) | **~$410** | [STRUCT:gex] (ZGL 206.8 is degenerate; net_gex turns negative ≈410) |

*Price-context color:* entering with **RSI 72.9 (overbought)**, +12.9% on the
month, but still **−17% below the 52-week high** [HIST:rsi fz] [HIST:52w_proximity fz]
— chase risk is real; this favors the fade entry over the aggressive, narrative
color only (does not alter size).

## Invalidation

- **Price-based:** **Two daily closes above $480** (call-wall / GEX cap breached →
  range broke UP, longs validated, the short-call structure is wrong) [OI:oi_by_strike].
  Secondary: two daily closes **below $410** (short-gamma flip → range breaks DOWN
  and amplifies toward the 417–430 max-pain zone) [STRUCT:gex].
- **Signal-based:** **GEX flips POSITIVE→NEGATIVE on the phase-4 daily refresh** (the
  long-gamma pin that anchors the whole range thesis is gone → trend regime)
  [STRUCT:gex]; or conviction-matrix flips MIXED→DIRECTIONAL_LONG with rising
  confluence [INSIGHT:conviction_matrix].
- **Macro-based:** **Dovish FOMC/CPI surprise (06-10 / 06-16-17)** that rips MSFT
  through 480, OR a **hawkish surprise** that triggers the negative-vanna vol-crush
  and the unhedged air-pocket to 417-430 [MACRO:FOMC] [STRUCT:vanna_charm].
- **Exit on invalidation:** credit structure → **tranche/roll**. Close 50% of the
  call credit spread if MSFT closes >$475 (approaching the short strike); close the
  remainder or roll up-and-out on a confirmed second close >$480.

## Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** p_raw = **0.444** (phase-5 `bullish_flow`
  win_rate, n=9, source=backtest) → N-cap (n<10 → 0.75) → **capped p = 0.444**
  [HIST:signal_backtest].
- **Kelly inputs:** b = **1.5** (reference long-call debit spread 460/480: max
  profit $12 / max loss $8), fraction = 0.25, cap_pct = 5.
- **Raw Kelly:** (0.444×1.5 − 0.556)/1.5 = **+0.073** → suggested 1.83%. **BUT the
  win-rate map fires first:** p = 0.444 **< 0.50 → directional ceiling = STARTER /
  SKIP** (SHORT-side floor: a sub-0.50 signal is not a directional position). **The
  directional LONG is therefore SKIPPED (0%)** — negative edge.
- **The recommended expression is the FADE side** (sell the crowded, capped upside).
  The bullish signal failing ~55.6% of the time is the call-credit-spread's edge
  (≈ half bucket), then cut by the gates below.
- **Risk gates:**
  - Fundamentals (phase-7b): **CONFIRM** (0 contradictions) → no-op (does not cut;
    cannot add).
  - Sentiment / crowd (phase-7c): **CAUTION, CROWDED_LONG** → **cut one size step**
    (half → starter).
  - Correlation (phase-6/8): **MSFT/PATH 0.637 — soft-watch (0.60–0.70)** → surface,
    **no cut**; size MSFT+PATH as ~1.5 names, not 2.
  - Sector rotation (phase-6): **aligned** (Tech inflow, persistence 1.0) → no cut.
  - Debate (phase-8b): bull_residual **0.65** vs bear_residual **0.55** →
    **disconfirmed = false** → no cut (but carry the downside-tail risk).
  - **Context (phase-0.5): BUSY_NAME_NORMAL_DAY** → do **not** size at top of band.
- **Final size:** **1.0% of book risk** (defined-risk max-loss ≤ 1% — starter),
  on the recommended call credit spread. **Directional long = 0% (skipped).**
- **Deviation reason:** none (final is *below* suggested, always permitted; no upward
  deviation — forbidden here anyway since the 7c gate fired and context is
  BUSY_NAME_NORMAL_DAY).

## Option structures

### Directional (presented per template — NOT recommended)

- **Structure:** Long call debit spread (the bull expression)
- **Strike(s) / expiry:** 460C / 480C, **2026-06-18**
- **Debit/credit:** ~$8.00 debit
- **Breakeven:** ~$468.0
- **Max loss:** $8.00 (per spread)
- **Why / why NOT:** strikes anchored to spot and the 480 call wall. **Not
  recommended:** the `bullish_flow` edge is negative (44.4%, −1.25%) [HIST:signal_backtest],
  the crowd is already long [SENT:recommendation], upside is gamma-capped at 480
  [STRUCT:gex], and the expiry straddles **NFP/CPI/FOMC** → IV-crush risk into the pin.

### Defined-risk (RECOMMENDED)

- **Structure:** **Bear call credit spread** (fade the capped, over-priced upside)
- **Strike(s) / expiry:** **Sell 480C / Buy 490C, 2026-06-18**
- **Debit/credit:** ~**+$2.50 credit**
- **Breakeven:** ~$482.5
- **Max loss:** $10 − $2.50 = **$7.50** (per spread); size so total max-loss ≤ **1%**
  of book
- **Why this structure:** sells the **rich COMPLACENT call skew** (calls richer than
  puts, skew_ratio 0.902) [STRUCT:term_skew] at the **480 call wall / GEX cap**
  [STRUCT:gex]; the 480 short sits just beyond the ±3.33% expected move (475)
  [CTX:implied_move]. Profits if MSFT stays ≤480 (high probability in a long-gamma
  pin) **and profits fully if the phase-8b downside tail fires** — it does not take
  the under-hedged downside risk. This is the thesis-consistent expression.

### Defined-risk alternative (second choice)

- **Structure:** Iron condor (pure-pin / range)
- **Strike(s) / expiry:** Sell 430P / Buy 415P + Sell 480C / Buy 490C, **2026-06-18**
- **Debit/credit:** ~+$3.00 net credit
- **Breakeven:** ~$427 / ~$483
- **Max loss:** ~$7.00 (wider side); ≤1% of book
- **Note:** **Inferior to the call credit spread here** — the 430 short put *takes*
  the exact phase-8b downside-tail risk (the negative-vanna air-pocket to the
  417–430 max-pain zone). Use only if you hold a pure symmetric-pin view and accept
  the put-side tail; the short put is set below the 417.5 magnet and above the 400
  put wall [STRUCT:max_pain] [OI:oi_by_strike].

## Macro overlay (cite phase-6)

- **Tailwinds:** Technology **#1 sector inflow +$13.1B, persistence 1.0, accelerating
  5 sessions** [MACRO:SectorFlowPersistence]; **ISM Mfg 54.0** (growth accelerating)
  [MACRO:ISM_Mfg]; easing cycle, **normal 2s10s +0.42** [MACRO:T10Y2Y].
- **Headwinds:** **Regime TRANSITIONAL — "half size, defined-risk, iron condors"**
  [MACRO:MarketRegime]; **breadth weak 40%** (narrow market) [MACRO:MarketRegime];
  **CPI 3.8% sticky, Fed on hold 3.50–3.75%, 10y 4.45%** [MACRO:CPIAUCSL]
  [MACRO:DGS10].
- **Net:** **mixed** (a durable Tech tailwind under a risk-managed, narrow,
  event-heavy tape).

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|------|-------|------------------|
| 2026-06-05 | May NFP / jobs report (front-end IV event) | ? |
| 2026-06-10 | CPI | ? |
| 2026-06-16/17 | FOMC (Powell's last; consensus hold) | ? |
| 2026-06-18 | June OPEX (OI cliff 17.78%, max pain 417.5) | ? |
| 2026-06-25 | BEA block (GDP/PCE) | ? |

Each binary is read against the **front-expiry expected move ±3.33% / ±$15.3**
[CTX:implied_move]; the 480 short call sits just beyond a single-event expected move.

## Post-trade monitoring checklist

- [ ] **GEX regime on phase-4 daily refresh** — if it flips POSITIVE→NEGATIVE, the
  pin is gone; the range thesis breaks and the short-call structure is at risk.
- [ ] **Dark-pool tape daily** — RTH (not after-hours) prints lifting offers >$462
  with mega/large buy_ratio >0.7 = genuine accumulation invalidating the range up
  [DP:block_stratified].
- [ ] **IV / front-end term structure around 06-05 NFP and 06-10 CPI** — a post-event
  vol crush is the negative-vanna dealer-selling trigger (downside tail).
- [ ] **480 call wall / 410 short-gamma flip** — the two range boundaries; a
  confirmed close beyond either is the invalidation.
- [ ] **MSFT vs PATH** — both are the same AI/Tech bet (0.637); don't let combined
  exposure exceed ~1.5 names.

## Citations summary

1. [FLOW:insights_deep_dive] net_flow **+$81.2M** on $1.39B gross call premium —
   phase-1-flow.md §Whole-tape aggregate.
2. [STRUCT:gex] **POSITIVE GEX +$268.7M, pin 460**, long-gamma "mean-reversion /
   reduced vol" — phase-4-structure.md §GEX.
3. [STRUCT:max_pain] **06-18 OPEX max pain 417.5 (−9.3%)**, every near-term expiry
   7–9% below spot — phase-4-structure.md §Max pain.
4. [HIST:signal_backtest] **bullish_flow win_rate 0.444, avg −1.25%, n=9** —
   phase-5-historical.md §Signal backtest.
5. [AGENT:risk-monitor] **desk 4/4 RANGE, avg conviction 2.25** — phase-8-agent-views.md.
6. [MACRO:MarketRegime] **TRANSITIONAL — "half size, defined-risk, iron condors"** —
   phase-6-macro.md §Market regime.
