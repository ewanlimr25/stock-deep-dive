# Phase 9 — Trade Blueprint

**Ticker:** NOW
**As-of date:** 2026-06-05
**PM voice:** desk PM running an institutional book
**Spot reference:** 112.45 close ([CTX:] phase-0.5 / [HIST:trend] phase-5)
**Upstream phases cited:** phase-0.5 through phase-8b

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

NOW closed a −17% unwind week pinned between a trapdoor and a ceiling: spot
sits 2.5% above the dealers' zero-gamma level at 109.7 with **no put wall
until 100/90** [STRUCT:gex][OI:oi_by_strike], underneath ~$200M of trapped
dark-pool supply at 117.90–119.36 [DP:price_levels] and a 5-session bearish
sweep campaign of $377.9M [FLOW:sweep_persistence]. But the marginal bear
is 6σ late (P/C z +6.093 [HIST:pc_ratio_zscore]), the day's largest
"bearish" print was a $20.7M **sold** put [FLOW:sweeps], fundamentals just
beat-and-raised with a $50B buyback [FUND:guidance], and the desk returned
zero LONGs with a non-directional plurality [AGENT:phase-8] inside a
TRANSITIONAL half-size macro regime [MACRO:MarketRegime_2026-06-05]. So we
trade the **edges of 109.7–120 only, defined-risk only**: stand watch, short
the *break* of 109.7 toward the 6/18 OPEX magnet at 108 and the 100 shelf
[STRUCT:max_pain], fade nothing in the middle.

## Bias + conviction + horizon

- **Directional bias:** **RANGE** (109.7–120; bearish skew on a confirmed
  break of the floor). Bias set by the plurality of phases 1–8 (phase-7
  MIXED baseline; phase-8 NEUTRAL×2/RANGE/SHORT, zero LONG); the 7b VETO,
  7c CAUTION, and 8b disconfirmation cut size/conviction but do not set bias.
- **Conviction (M-01 bin):** **0.55**
- **Time horizon:** 1–4w (CPI ≈6/10 → FOMC 6/16-17 → OPEX 6/18 → early July)
- **Why this bin:** estimated confluence sits in the 50–64 band (→0.65),
  and the phase-8b debate gate (`disconfirmed=true`, 0.65 vs 0.65) mandates
  a one-bin down-shift → 0.55. Phase-10 to verify the band.

## Conviction deviation

None upward. The 0.65-band estimate is down-shifted to 0.55 by the debate
gate per `rubrics/sizing-rubric.md` §Risk gates #5 — recorded here so
phase-10 can reconcile band vs bin.

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| Primary | ~109.50 | Daily close below ZGL 109.7 with no same-session reclaim → enter the bear put spread (trapdoor opens: dealers flip short-gamma, no OI support until 100) | [STRUCT:gex] [OI:oi_by_strike] |
| Aggressive | 117.50–119.50 | Rejected bounce into the DP supply shelf (failed retest, intraday reversal off the $148M 119.36 cluster) — same vetoed-carry constraints, better level | [DP:price_levels] |
| Fade (plan B) | >120.00 | Two closes reclaiming the 120 call wall + 6/12 max-pain → flip to a call debit spread toward the 125/130 GEX shelves (sweep-tracker's two-sided line) | [OI:oi_by_strike] [STRUCT:max_pain] [AGENT:sweep-tracker] |

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Support (first) | 110 — two-sided 110 strike + GEX shelf +$3.51M | [OI:oi_by_strike] [STRUCT:gex] |
| Support (structural) | 100, then 90 — first true put walls (−11.0% / −19.9%) | [OI:oi_by_strike] |
| Resistance | 117.90–119.36 (~$190M DP prints), then 120 call wall (net +19,858) | [DP:price_levels] [OI:oi_by_strike] |
| Gamma flip | **109.7** (ZGL; treat as ±2% band 107.5–112) | [STRUCT:gex] |
| Pin magnet | 120 into 6/12 weekly; **108 into the 6/18 cliff (20.9% of OI)** | [STRUCT:max_pain] [OI:term_structure] |

Price-context color (advisory): RSI 54.5 — the fade only unwound the
overbought melt-up; price is −46.8% below the 52W high and +38.4% above the
52W low, still +6.9%/+13.5% above the rising 20/50-SMAs [HIST:rsi fz]
[HIST:52w_proximity fz] — this is the middle of a violent rebound, not a
fresh breakdown; another reason to demand the trigger before shorting.

## Invalidation

- **Price-based:** for the RANGE read — two daily closes above **120.00**
  (call wall + weekly max-pain reclaimed [OI:oi_by_strike]
  [STRUCT:max_pain]) → flip to plan-B fade. For the triggered put spread —
  hard stop on a daily close back above **113.00** (reclaims the −$5.3M
  short-gamma battleground at 112–113 [STRUCT:gex per_strike]).
- **Signal-based (most diagnostic first):** (1) next OI snapshot shows the
  Jul-17 135P line down ≥8,000 contracts → the $20.7M block was a CLOSE
  (hedge monetization = bears cashing out; bearish-skew thesis weakens
  materially) [FLOW:sweeps][OI:term_structure]; (2)
  institutional-accumulation flips to ACCUMULATION with buy/sell >1.0 and
  absorption above VWAP 110–112 [INSIGHT:institutional_accumulation]
  [AGENT:accumulation-hunter]; (3) cumulative premium flow net-bullish 3
  consecutive sessions [HIST:cumulative_premium_flow].
- **Macro-based:** cool May CPI (≈6/10) **and** dovish June FOMC (6/16-17)
  → Dec-hike odds collapse from 43% [MACRO:FedWatch_2026-06-05] and the
  multiple-compression headwind lifts; or UW regime flips back to RISK-ON
  [MACRO:MarketRegime].
- **Exit rule:** debit spread = **hard stop** (close 100% on the price
  invalidation); condor = close at 2× credit drawdown or roll the tested
  wing; no averaging.

## Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** p_raw = **0.875** (bearish_flow, n=**8**,
  source=backtest) → N-conditional cap (n<10 → 0.75) → **p = 0.75**
  [HIST:signal_backtest]. Note: market-wide class base rate, not
  NOW-specific.
- **Kelly inputs:** b = |entry−target| / |stop−entry| = |109.5−100| /
  |113−109.5| = 9.5/3.5 = **2.71**; fraction = 0.25; cap_pct = 5
- **Raw Kelly:** (0.75×2.71 − 0.25)/2.71 = **0.658** → ×0.25 = 16.4% →
  capped at **5.0%** suggested. **Win-rate map ceiling:** p 0.75 ≥ 0.70 →
  full (pre-gates).
- **Risk gates (each cut-only, applied in order):**
  - Fundamentals (phase-7b): **VETO** (contradictions 2: beat-and-raise +
    growth/margins) → directional standing size **0% / watch-only**; any
    triggered directional expression must be defined-risk, marked
    **"fundamentals-vetoed, carry only"**, starter at most.
  - Sentiment/crowd (phase-7c): **CAUTION** (short side crowded at the
    margin — 6σ P/C extreme + $50B buyback; crowd_state CROWDED_LONG
    structurally) → cut one size step.
  - Correlation cluster (phase-6/8): **FIRED — NOW/PATH 0.759 ≥ 0.70**,
    live PATH blueprint same date (RANGE 0.65) → cut one size step; do not
    run both books at full carry.
  - Sector rotation (phase-6): aligned-for-shorts / adverse-for-longs,
    INFLOW persistence 1.0 decelerating −71% → **not fired** for the
    bearish-skew structures (would fire on the plan-B long).
  - Debate (phase-8b): bull_residual **0.65** vs bear_residual **0.65** →
    `disconfirmed=true` → conviction bin 0.65→**0.55** + cut one size step.
- **Context modifier (phase-0.5):** `BUSY_NAME_NORMAL_DAY` → no
  top-of-band sizing (already moot post-gates).
- **Final size:** standing **0%** (watch). On trigger:
  **max-loss ≤ 0.5% of book risk** on the engaged structure (5% suggested →
  starter via VETO → halved again via CAUTION + cluster + debate stacking;
  regime guidance "half position sizes" [MACRO:MarketRegime] concurs).
  Never both structures beyond 0.75% aggregate max-loss.
- **Deviation reason:** none (downward only — always allowed).

## Option structures

Expected-move check (N4): screener `implied_move_perc` 0.38% is
**unit-suspect** (phase-0.5 DATA NOTE) — rejected. Derived front-expiry
(6/12, 7d) expected move = 74.8% IV × √(7/365) ≈ **±10.4% ≈ ±$11.65**
[STRUCT:iv_term_structure]; daily ±1σ ≈ 4.4% (`volatility` field). The
spread's 110→100 target (−8.7% from trigger) is **inside** one front-expiry
σ — not a rich target; both structures are debit/defined wings, so no
single-catalyst gap can exceed the stated max loss (CPI/FOMC/OPEX all sit
inside the expiry on purpose: they are the resolution mechanism, not a
hazard to a defined-risk book).

### Directional (primary — TRIGGER-CONDITIONAL, fundamentals-vetoed carry only)

- **Structure:** bear put debit spread (enter ONLY on the 109.7 trigger)
- **Strike(s) / expiry:** long 110P / short 100P, **2026-07-17** (42 DTE;
  strikes = the two-sided 110 strike and the 100 put wall
  [OI:oi_by_strike]; expiry clears the 6/18 OPEX magnet at 108 and the
  FOMC, expires before 7/22 earnings [MACRO:calendar])
- **Debit/credit:** ≈ $4.00 debit (illustrative off the as-of surface —
  Aug 110P printed $11.92 [FLOW:top_premium_trades]; reprice at trigger)
- **Breakeven:** 106.00 · **Max loss:** $4.00/spread (≤0.5% book risk)
- **Why this structure:** VRP −0.106 says own premium, don't sell it
  [HIST:vrp], and IV's 35-DTE trough (66.5% at 7/10 [STRUCT:iv_term_structure])
  makes mid-July the cheapest tenor that still contains the OPEX-gravity
  window; the debit cap honors the 7b VETO (carry-only, defined loss).

### Defined-risk alternative (the RANGE expression, no-trigger carry)

- **Structure:** iron condor (sell the edges the walls defend)
- **Strike(s) / expiry:** short 100P / long 95P + short 125C / long 130C,
  **2026-07-17** (short strikes = the 100 put wall and the 125 call wall /
  +$2.4M GEX shelf [OI:oi_by_strike][STRUCT:gex])
- **Debit/credit:** ≈ $2.70 credit (illustrative; reprice)
- **Breakeven:** 97.30 / 127.70 · **Max loss:** $2.30/condor (≤0.5% book)
- **Caveat:** this is short premium against a PREMIUM_BUYING VRP regime
  [HIST:vrp] — acceptable only because both wings sit outside walls and
  size is starter; skip it entirely if front IV re-rates above ~80%.

## Macro overlay (cite phase-6)

- **Tailwinds (for the name):** $50B buyback authorization 5/29
  [MACRO:NOW_catalysts]; Huang agentic-AI endorsement underpinning the
  sector narrative [MACRO:NOW_catalysts]; ISM Services 54.5 = healthy
  enterprise demand [MACRO:ISM_Svcs_2026-05].
- **Headwinds:** Dec-hike odds 43% (from 26%) + CPI +3.78% YoY
  [MACRO:FedWatch_2026-06-05][MACRO:CPIAUCSL_2026-04]; VIX 21.51 (+40%)
  with regime TRANSITIONAL, "half position sizes"
  [MACRO:MarketRegime_2026-06-05]; 10y 4.47% vs a 66.9× GAAP multiple
  [MACRO:DGS10][FUND:metric]; tech inflow decelerating −71%/5 sessions
  [MACRO:sector_flow_persistence]; U-Mich 44.8 record low
  [MACRO:UMich_2026-05].
- **Net:** headwind — which is exactly why the plan demands the trigger
  rather than positioning in the middle of the range.

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|------|-------|------------------|
| ≈2026-06-10 | May CPI release | hot → trapdoor risk (−); cool → bounce (+) [MACRO:calendar] |
| 2026-06-12 | Weekly OPEX, max-pain 120 | mild upward pin (+) [STRUCT:max_pain] |
| 2026-06-16/17 | FOMC (~98.7% hold; tone) | ? — statement/dots decide the hike narrative [MACRO:FOMC] |
| 2026-06-18 | NOW monthly OPEX — 20.9% of OI rolls; max-pain 108 | downward gravity into it; gamma/charm reset after (−/?) [OI:term_structure][STRUCT:max_pain] |
| 2026-07-22 | Earnings (outside 30d; structures expire 7/17) | n/a by design [MACRO:calendar] |

## Post-trade monitoring checklist

- [ ] **Daily OI refresh on the Jul-17 135P line** — −8,000 = block was a
  close (hedge monetization; bearish skew weakens); +8,000 = opened
  put-write (vol supply; range thesis strengthens) [OI:biggest_increases].
- [ ] **Daily ZGL/GEX refresh** — cushion was 6.9M and falling
  [HIST:gex_time_series]; a negative print = regime flip = trigger
  imminent; also watch the 110 GEX shelf.
- [ ] **DP buy/sell ratio + price levels daily** — accumulation flip
  (b/s >1.0, absorption above VWAP 110–112) is the accumulation-hunter's
  invalidation [INSIGHT:institutional_accumulation].
- [ ] **Cumulative premium flow sign** — 3 consecutive net-bullish sessions
  invalidates the bearish skew [HIST:cumulative_premium_flow].
- [ ] **Tech sector-flow persistence** — did the −71% deceleration cross
  into outright OUTFLOW (accelerant), or re-accelerate (stand down)
  [MACRO:sector_flow_persistence]?
- [ ] **PATH blueprint status** — correlation cluster 0.759; if the PATH
  RANGE position is engaged, cap NOW aggregate risk accordingly
  [MACRO:portfolio_correlation].
- [ ] **Pre-CPI / pre-FOMC risk check** — no new entries inside 24h of
  either print; defined-risk only through 6/18 OPEX.

## Citations summary

1. [STRUCT:gex] — ZGL 109.7, total_gex +6,878,457, regime POSITIVE; 112
   strike −$5,325,467 — phase-4-structure.md §GEX
2. [OI:oi_by_strike] — 120 call wall net +19,858; no put wall until 100
   (−11.0%) / 90 (−19.9%) — phase-3-positioning.md §Walls
3. [DP:price_levels] — 119.36 cluster $148,352,419 (5-day) —
   phase-2-dark-pool.md §Price levels
4. [HIST:pc_ratio_zscore] — z +6.093, BEARISH_EXTREME (0.80 vs mean 0.33)
   — phase-5-historical.md §P/C ratio z-score
5. [FLOW:sweep_persistence] — bearish 5/5 sessions, $377,864,816,
   consistency 1.0 — phase-1-flow.md §Key signals
6. [MACRO:MarketRegime_2026-06-05] — "TRANSITIONAL — Mixed signals, reduce
   position size"; "Half position sizes" — phase-6-macro.md §Market regime
7. [FUND:guidance] — FY26 subscription guide raised to $15,735–15,775M;
   [FUND:verdict] tier_adjustment VETO — phase-7b-fundamentals.md
8. [DEBATE:bear_residual] — 0.65 vs bull 0.65 → disconfirmed=true —
   phase-8b-debate.md §Disconfirmation verdict
