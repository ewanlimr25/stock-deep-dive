# Phase 9 — Trade Blueprint

**Ticker:** IREN
**As-of date:** 2026-06-05
**PM voice:** desk PM running an institutional options-overlay book
**Spot reference:** 54.35 (phase-0.5 `[CTX:]` close)
**Generated:** 2026-06-07T02:25Z
**Upstream phases cited:** phase-0.5 through phase-8b

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

Friday's −12.1% flush printed IREN's most net-bearish tape in its 40-session
history (net flow −$18,832,787, self-history percentile 0.0
[CTX:self_pctile DUCKDB][FLOW:insights_deep_dive]) — but the bearishness is
rented, not structural: the dominant position event was a reactive 06/12 put
ladder bought at the ask at 130% front IV (50P +29,735 [OI:biggest_increases])
while block-size lots sold the 55/56 strangle both ways and far-LEAP 110C
builds confirmed opening [OI:biggest_increases], inside a still-5/5-bullish
$339.9M sweep campaign [FLOW:sweep_persistence]. With dealers short gamma
across 44–59 (total GEX −$64.8M [STRUCT:gex]), the June monthly magnet at 55
[STRUCT:max_pain], a BTC-transmitted macro headwind that single-name
mechanics cannot stop [MACRO:BTC_2026-06-05], and a unanimous NEUTRAL/RANGE
desk (avg conviction 2.25, identical 50/60 level map [AGENT:all-four]), the
only trade I'll book is the **50–60 box, defined-risk, tiny** — fade the
edges, don't live in the middle.

## Bias + conviction + horizon

- **Directional bias:** RANGE (50–60; tactical bearish tilt at the top of the
  box, per the bearish_flow class edge [HIST:signal_backtest])
- **Conviction (M-01 bin):** **0.55**
- **Time horizon:** 1-4w (to the 06/18 OPEX gravity date; tactical management 1-5d)
- **Why this bin:** expected phase-10 confluence lands in the 30–49 band
  (mixed phases, two gate penalties), and the phase-8b debate fired
  disconfirmed (0.65 vs 0.65 tie → attacker), forcing a one-bin down-shift
  from 0.65 [DEBATE:].

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| Primary | 59.50–60.50 | Stall-and-reject at the gamma flip / first positive-GEX strike + 60 call wall (27,719 OI ≤30DTE); short-delta only on rejection, not on touch | [STRUCT:gex] flip ~59.5–60; [OI:oi_by_strike] 60 call_wall_resistance |
| Aggressive | 50.00–50.50 | Tag of the 06/12 50-put wall (54,682 put OI, the +29,735 hedge strike) **with BTC ≥ $58k** — range-long side, defined risk only | [OI:oi_by_strike] 50 put_wall_support; [AGENT:contrarian-scanner] BTC condition |
| Fade (plan B) | 62.30 | Daily close > 62 — above the flip, the 61.86 DP shelf and the 06/12 max-pain 61 — range broken UP; flip long toward the 65.3–66.6 shelf | [DP:price_levels] 61.86 = $43.6M shelf; [STRUCT:max_pain] 06/12 = 61 |

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Support | 50 (then 45 / 40 — sub-50 DP map is UNCHARTED = air-pocket) | [OI:oi_by_strike dte≤30] 50: net_oi −45,730; [DP:price_levels] nothing <54 in 5d |
| Resistance | 60 (then 61.0–61.9 DP shelf, then 65.3–66.6 = $450M shelf) | [OI:oi_by_strike] 60 call wall; [DP:price_levels] 66.60 = $231.1M |
| Gamma flip | ~59.5–60 (per-strike sign change; tool ZGL 5.12 is a flagged artifact) | [STRUCT:gex] |
| Largest pin | **55** = 06/18 max-pain, distance +1.14%, 315,927 OI (native value) | [STRUCT:max_pain] |

Price-context color (advisory): RSI(14) 46.90 — the crash unwound overbought
but printed **no oversold signal**; price is −29.3% off the 76.87 52-week
high, still +9.0%/+16.2% above SMA50/200 [HIST:rsi fz][HIST:52w_proximity fz].
No knife-catch credit from the chart; respect the aggressive-entry BTC
condition.

## Invalidation

- **Price-based:** Two daily closes **< 50** (put wall + −$7.4M GEX shelf) →
  the box is dead, air-pocket to 45/40 opens — exit everything, no averaging.
  Symmetrically, a daily close **> 62** breaks the box UP (see Fade row —
  plan B, not a loss-exit if positioned per structure 2's call wing).
- **Signal-based:** Bid-side Jan-27+ LEAP call selling **recurs 06/08–06/09 at
  ≥$3M/day** (sweep-tracker's flip condition — Friday was a one-day $6.05M
  spike vs $1.4M on 06/04 [AGENT:sweep-tracker]); or cumulative premium flow
  prints net-bearish 3 consecutive sessions next week
  [HIST:cumulative_premium_flow]; or conviction-matrix flips MIXED →
  DIRECTIONAL_SHORT [INSIGHT:conviction_matrix].
- **Macro-based:** BTC daily close **< $56k** (validates the put ladder as
  trend — contrarian-scanner's hinge) or **> $65k** (force-unwinds the
  crowding upward through the call wall — risk-monitor's hinge)
  [MACRO:BTC_2026-06-05]; or May CPI (2026-06-10) core **> 0.4% MoM** =
  hawkish surprise into the hedges' own expiry week [MACRO:CPIAUCSL].
- **Exit mode:** Hard stop on the debit spread (close 100% on price-based
  trigger). Condor: close at 2× credit drawdown or on either box-break
  trigger; do not roll into the FOMC.

## Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** p_raw = **0.875** (bearish_flow, n = **8**, source
  = backtest [HIST:signal_backtest]) → N-conditional cap (n < 10 → 0.75) →
  **p = 0.75**. (Class base rate, market-wide, in-sample — not IREN-specific;
  phase-5 handoff quoted verbatim.)
- **Kelly inputs:** b = 2.0 (primary fade: entry 60 → target 55 = 5.0 vs stop
  62.5 = 2.5), fraction = 0.25, cap_pct = 5
- **Raw Kelly:** (0.75×2 − 0.25)/2 = **0.625** → 0.625 × 0.25 × 100 = 15.6% →
  capped at 5.0%. **Win-rate map ceiling:** p ≥ 0.70 → full permitted (≤5%).
- **Risk gates (in order; each can only cut):**
  1. Fundamentals (7b): **CAUTION** → cut one step: 5.0% → **2.5%**
  2. Sentiment/crowd (7c): **CAUTION** (crowd_state CROWDED_SHORT front-week;
     thesis-adjacent) → cut one step: 2.5% → **1.25%**
  3. Correlation (6/8): no pair ≥0.70; IREN/RKT 0.608 **soft-watch** →
     surfaced, no cut
  4. Sector rotation (6): phase-6 verdict **adverse** *to a bullish thesis*
     (cohort de-gross); our bias is RANGE with bearish tilt — not against the
     trade direction → no cut, surfaced
  5. Debate (8b): bull_residual **0.65** vs bear_residual **0.65** →
     **disconfirmed = true** → bin down-shift (0.65→0.55, applied above) +
     cut one step: 1.25% → **0.625%**
- **Context modifier (0.5):** GENUINELY_UNUSUAL → no-op (edge already in p).
- **Final size: 0.6% of book risk** (rounded from 0.625%; ≈ one-eighth of the
  5% cap). Regime guidance "half position sizes" [MACRO:MarketRegime] is
  independently satisfied.
- **Deviation reason:** none (upward deviation forbidden — three gates fired).

## Option structures

Expected move first (N4): the screener's `implied_move_perc` 0.96%
[CTX:implied_move] is a flagged artifact (phase-6/7) — sizing instead off the
IV surface: 06/12 avg IV 130.2% → ±1σ to Friday ≈ **±18.3% (±$9.97)**; 06/18
avg IV 121.3% → ±1σ ≈ **±22.9% (±$12.45)** [STRUCT:iv_term_structure]. Both
short strikes of the condor (−8.0%/+10.4%) sit well INSIDE one σ — this is a
walls-hold bet that realized vol finally undershoots, NOT a vol-edge bet
(VRP is −0.048 [HIST:vrp]); that is exactly why the size is 0.6% and the
wings are mandatory. Catalyst-gap check: an expected-move gap (±18%) would
blow through any stop on naked premium → only the wing-defined max-loss makes
either structure bookable; max loss per structure ≤ the 0.6% allocation.

### Directional (primary) — tactical bearish tilt at the box top

- **Structure:** put debit spread (long 55P / short 50P)
- **Strike(s) / expiry:** 55/50, **2026-06-26** (post-CPI, post-FOMC expiry —
  survives both binaries with theta runway; 21 DTE IV 113.5% vs 130% front =
  cheaper tenor [STRUCT:iv_term_structure])
- **Debit/credit:** ≈ $1.50 debit indicative at 06-05 marks (re-quote; target
  ≤ $1.10 if filled on the primary 60-rejection entry)
- **Breakeven:** ≈ 53.50 at 06-05 marks (55 − debit)
- **Max loss:** the debit (≈ $1.50/spread) — sized so total debit ≤ 0.6% of
  book risk
- **Why this structure:** strikes are the two heaviest near-term put levels —
  55 (51,891 OI battleground) and 50 (54,682 OI wall) [OI:oi_by_strike] — so
  the spread monetizes a top-of-box rejection into the wall without paying
  130% front vol; IV 76.9th pctile [HIST:iv_percentile_zscore] argues against
  naked long premium, and a spread caps the vega bleed when front-end
  backwardation normalizes [STRUCT:front_end_iv_ratio]. **Condition: only on
  the primary entry trigger (59.5–60.5 rejection). Not at spot — 54.35 sits
  in the −$30.7M gamma pit where the desk found "no edge either way"
  [AGENT:risk-monitor].**

### Defined-risk alternative — the actual range thesis

- **Structure:** iron condor (short 50P/60C, long 45P/65C)
- **Strike(s) / expiry:** 45/50/60/65, **2026-06-18** (the OPEX gravity date:
  16.55% of all OI, max-pain 55 [OI:term_structure][STRUCT:max_pain])
- **Debit/credit:** ≈ $1.80 credit indicative at 06-05 marks (re-quote at entry)
- **Breakeven:** ≈ 48.20 / 61.80
- **Max loss:** width − credit ≈ 5.00 − 1.80 = **$3.20/spread** — max-loss
  (not margin) ≤ 0.6% of book risk
- **Note:** all four strikes are native walls: 50 put wall, 60 call wall, 45
  put shelf (26,617 OI), 65 call wall (22,860 OI) + the 65.3 DP shelf
  [OI:oi_by_strike][DP:price_levels]. This is the UW regime engine's own
  guidance verbatim — "Half position sizes. Favor defined-risk strategies.
  Iron condors in range" [MACRO:MarketRegime_2026-06-05]. Manage: close at 2×
  credit drawdown, or harvest at 50% of credit; close the threatened side on
  either box-break invalidation; **no roll through FOMC 06/16-17.**

## Macro overlay (cite phase-6)

- **Tailwinds:** ISM Mfg 54.0 / Services 54.5 — AI-capex demand intact
  [MACRO:ISM_2026-06]; labor stable (NFP +172k, UNRATE 4.3% — no recession
  bid under puts) [MACRO:PAYEMS]; FOMC 98.7% priced hold [MACRO:FOMC_2026-06-17];
  equal-weight breadth −0.92% vs SPY −2.58% = orderly de-gross, not
  liquidation [MACRO:sector_breadth fz EOD].
- **Headwinds:** BTC ≈$60k, −18% w/w — the primary driver, trades through the
  weekend [MACRO:BTC_2026-06-05]; CPI re-accelerating (+3.78% YoY headline,
  hot MoM) [MACRO:CPIAUCSL_2026-04 FRED]; 2y +17bp m/m to 4.05%
  [MACRO:DGS2]; U-Mich record-low 44.8 [MACRO:UMICH_2026-05-22]; Tech option
  flow decelerating −71% over 4 sessions [MACRO:sector_flow]; US-Iran war
  ongoing.
- **Net:** headwind (4/5) — which is precisely why the bearish tilt sits at
  the TOP of the box and the long side only triggers at the 50 wall with a
  BTC floor condition.

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|------|-------|------------------|
| 2026-06-10 | May CPI 08:30 ET (war-month energy print) | ? (hawkish tail = −) |
| 2026-06-12 | Weekly OPEX — 50P/55P ladder + 55/56 strangle expire | ? (charm/unpin) |
| 2026-06-16/17 | FOMC + SEP (Warsh's first dots; 98.7% hold priced) | ? (dots = tail) |
| 2026-06-18 | June monthly OPEX (16.55% of OI; max-pain 55) | + (pin gravity IF ≥55) |
| continuous | BTC level / US-Iran headlines | − (current trajectory) |
| 2026-08-27 | Earnings (outside window — no position carried into it) | n/a |

## Post-trade monitoring checklist

- [ ] **Daily GEX refresh (phase-4):** does total_gex stay < 0 and spot < 59.5?
  A reclaim of ≥55 with front-IV crush switches the 55-pin magnet ON
  (condor-friendly); a fresh GEX low with spot < 52 = pre-break warning.
- [ ] **Monday/Tuesday sweeps (06/08–09):** bid-side Jan-27+ LEAP call selling
  ≥$3M/day = campaign reversal → kill the range thesis (signal invalidation).
- [ ] **Monday OI print:** did Jan-27 70C/100C/110C OI FALL (Friday's selling
  = closing/profit-taking, benign) or RISE (fresh overwriting, bearish)? —
  resolves phase-1's open question.
- [ ] **BTC twice daily:** < $56k or > $65k triggers the macro invalidation
  legs; weekend gap risk is THE risk (positions are Friday-EOD sized for it).
- [ ] **CPI morning (06/10):** if core > 0.4% MoM and spot < 52 pre-print,
  close the condor's put side into the print, keep wings.
- [ ] **Book check:** RKT correlation 0.608 soft-watch — if the book also
  carries CRM/NOW/PATH (0.76–0.86 cluster), total tech-complex defined-risk
  premium ≤ 2% of book.

## Citations summary

1. [OI:biggest_increases] 50P 06/12 OI +29,735 (1,601→31,336), 81% at ask,
   $2.60M — phase-3-positioning.md §Largest OI increases
2. [STRUCT:gex] total_gex −$64,788,860; all strikes 44–59 negative (54:
   −$30.7M); flip ~59.5–60 — phase-4-structure.md §GEX
3. [STRUCT:max_pain] 06/18 max_pain_strike 55, distance_pct +1.14, OI
   315,927 — phase-4-structure.md §Max pain
4. [FLOW:sweep_persistence] 5/5 sessions dominant-bullish,
   total_sweep_premium $339,924,997 — phase-1-flow.md §Key signals
5. [HIST:signal_backtest] bearish_flow win_rate 87.5%, n=8, avg −2.73%/5d →
   capped p 0.75 — phase-5-historical.md §Sizing handoff
6. [MACRO:BTC_2026-06-05] BTC ≈$60k, −18% w/w (US-Iran war) — phase-6-macro.md
   §Sector overlay
7. [AGENT:risk-monitor] "no sizeable directional bet survives this regime";
   no IREN pair ≥0.70 — phase-8-agent-views.md
8. [DEBATE:] bull_residual 0.65 vs bear_residual 0.65 → disconfirmed=true;
   strongest_bear_point = "pins require positive gamma and positive gamma
   starts at 60" — phase-8b-debate.md §Disconfirmation verdict
