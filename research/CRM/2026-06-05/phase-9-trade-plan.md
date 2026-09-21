# Phase 9 — Trade Blueprint

**Ticker:** CRM
**As-of date:** 2026-06-05
**PM voice:** desk PM running an institutional book
**Spot reference:** 185.66 (phase-0/2 close, screener parquet)
**Upstream phases cited:** phase-0.5 through phase-8b

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

CRM is a failed post-earnings breakout sitting on its own trapdoor: the
aggressive tape has pressed short five sessions running ($211.13M bearish
sweep persistence, consistency 1.0 `[FLOW:sweep_persistence]`) while dealer
gamma collapsed from +$50.4M to FULLY_NEGATIVE with the board's largest mass,
−$13.34M, parked exactly at the 185 strike `[STRUCT:gex]`
`[HIST:gex_time_series]`, and the sector is the day's single biggest
directional outflow (−$807.6M, regime TRANSITIONAL, AVGO shock unresolved
`[MACRO:MarketRegime_2026-06-05 UW]`). Below 185 there is almost no
transacted dark-pool volume until the 176.17 pre-earnings gap-fill — an air
pocket dealers are mechanically obliged to chase price through
`[DP:level_xcheck DUCKDB]`. But this is a *mechanics* short, not a
business short — fundamentals are improving on every axis (3/3 accelerating
beats, $25B ASR `[FUND:earnings_surprises]`), the short crowd is already
populated (7.91% float `[SENT:short_float fz]`), and the debate did not
clear the thesis (0.55 vs 0.55, disconfirmed) — so the directional position
is **watch-only** and the only book exposure is a trigger-conditional,
defined-risk carry at starter size.

## Bias + conviction + horizon

- **Directional bias:** SHORT (plurality of phases 1–8: phase-2 weekly
  distribution, phase-3 call-supply ceiling, phase-4 short gamma + dealer
  SELL, phase-5 bearish_flow edge, phase-6 headwind, phase-8 2-of-4 SHORT;
  gates cut size, not bias)
- **Conviction (M-01 bin):** **0.55** (base 0.65 "moderate edge" →
  down-shifted one bin by the phase-8b disconfirmation gate)
- **Time horizon:** 1-4w (the structure resolves through CPI ~6/10 → FOMC
  6/16-17 → OPEX 6/18)
- **Why this bin:** phases agree on geometry but split on direction (phase-8:
  2-1-1) and the debate ended 0.55/0.55 — slight edge, real disconfirming
  evidence; phase-10 will cross-check the band.

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| Primary | 184.50 | decisive break + hold below the 185 put-wall/gamma trigger (15-min close below 185 that does not reclaim within the hour) | `[OI:oi_by_strike]` `[STRUCT:gex]` |
| Aggressive | 189.50–190.00 | rejection at the 190 battleground / 6-18 max-pain magnet tag (failed reclaim on declining volume) | `[STRUCT:max_pain]` `[OI:oi_by_strike]` |
| Fade (plan B, counter-trade LONG) | 176.50 | tag of the 176.17 pre-earnings gap-fill at the air-pocket floor — play the ASR bid + squeeze ledger from support, stop below 174 | `[DP:price_path DUCKDB]` `[FUND:financials_reported]` |

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Support | 185 (put wall, net −9,580 ≤30DTE); then 183.70 (week's DP print low); then 176.17 (gap-fill) | `[OI:oi_by_strike]` `[DP:level_xcheck DUCKDB]` |
| Resistance | 190 (two-sided battleground) → 195 (call wall +8,928, dealer long-gamma +$3.9M) → 200–201 (wall +21,976, $415M DP shelf) | `[OI:oi_by_strike]` `[STRUCT:gex]` `[DP:price_levels]` |
| Gamma flip | no ZGL printed (FULLY_NEGATIVE); functional flip band **190–195** (per-strike sign crossover) | `[STRUCT:gex]` |
| Largest pin | **190** = 2026-06-18 max pain (+2.29% above spot); 192.5 = 6/12 max pain | `[STRUCT:max_pain]` |

Price-context color (advisory): RSI(14) 51.0 — neutral, not oversold; price
−15.66% below SMA200 and −32.93% from the 52-week high, +13.54% above the 52w
low `[HIST:rsi fz]` `[HIST:52w_proximity fz]` — a broken long-term trend
mid-retrace, which favors trigger-discipline over anticipation.

## Invalidation

- **Price-based:** **two daily closes above 190.00** (battleground + OPEX
  magnet) kills the short thesis; a **single close above 195** is squeeze
  confirmation (complacent skew = no brake to 200 `[STRUCT:term_skew]`) —
  hard-stop everything bearish immediately. On the downside-carry side, ATR
  ×1.5 ≈ $14.4 adverse (`ATR 9.60`, phase-0 drift) from entry without
  follow-through = stand aside.
- **Signal-based:** (a) any session flipping `sweep-persistence`
  dominant_direction off bearish (breaking the 5/5 streak)
  `[FLOW:sweep_persistence]`; (b) GEX regime returns POSITIVE with spot above
  the refreshed ZGL `[STRUCT:gex]`; (c) dark-pool buy_ratio steps up >0.60 on
  the 183–186 shelf (accumulation appearing where there is none today)
  `[DP:block_stratified]`.
- **Macro-based:** benign May CPI (~6/10) **plus** an as-expected/dovish FOMC
  (6/16-17) releases the max-pain magnet upward through the stop — treat the
  pair resolving benign as invalidation even without the 190 closes; regime
  flip back to uptrend per `uw risk market-regime` `[MACRO:MarketRegime UW]`.
- **Exit style:** hard stop (debit structure): close 100% on the price-based
  trigger. The 6/18 credit spread closes on the single-close->195 rule, no
  averaging.

## Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** p_raw = **0.875** (n=**8**, source=backtest,
  avg_move −2.73%) → N-conditional cap (n<10 → 0.75) → **capped p = 0.75**
  `[HIST:signal_backtest]`
- **Kelly inputs:** b = |entry − target| / |stop − entry| = (184.50 − 176.17)
  / (190.00 − 184.50) = 8.33 / 5.50 = **1.51**; fraction = 0.25; cap_pct = 5
- **Raw Kelly:** (0.75×1.51 − 0.25)/1.51 = **0.584** → suggested = min(0.584
  × 0.25 × 100, 5) = **5.0%** · **Win-rate map ceiling:** p 0.75 ≥ 0.70 →
  full (≤ cap) — pre-gates
- **Risk gates (each can only cut):**
  - Fundamentals (phase-7b): **VETO** (signal BULLISH, 2 contradictions vs
    the short) → **directional size = watch-only / 0%**; defined-risk carry
    only, marked "fundamentals-vetoed, carry only"
  - Sentiment/crowd (phase-7c): **CAUTION**, crowd_state CROWDED_SHORT → cut
    one size step on the carry
  - Correlation cluster (phase-6/8): **CLUSTER — CRM/NOW 0.863, CRM/PATH
    0.820** (concurrent same-date blueprints) → cut one size step; the three
    blueprints share ONE software risk budget
  - Sector rotation (phase-6): OUT of Technology = **aligned** with the short
    → no cut
  - Debate (phase-8b): bull_residual **0.55** vs bear_residual **0.55** →
    **disconfirmed = true** → conviction bin down-shifted (0.65→0.55) + cut
    one size step
- **Context modifier (phase-0.5):** `BUSY_NAME_NORMAL_DAY` → no top-of-band
  sizing permitted (moot — gates already bind).
- **Final size:** **0% — watch-only** (the 7b VETO zeroes the directional
  envelope regardless of Kelly; validator-enforced). The two structures below
  are published per the rubric as "fundamentals-vetoed, carry only" —
  illustrative candidates with an indicative budget of ≤0.5% of book max-loss
  (5.0% → VETO → CAUTION step → cluster step → debate step ⇒ starter),
  deployable ONLY if a re-run after the trigger fires clears the veto (e.g.,
  the flow bias flips or fundamentals deteriorate). Risk-monitor's "one-third
  of one position across the CRM/NOW/PATH cluster" applies on top: any
  deployed carry shares the NOW/PATH risk budget.
- **Deviation reason:** none (upward deviation forbidden — gates fired).

## Option structures

**Expected move (N4):** front-expiry implied move ±0.56% / $1.04
`[CTX:implied_move_pct]`; front-week (6/12) ATM IV 51.7% and 6/18 49.6%
`[STRUCT:iv_term_structure]` price a materially wider weekly range — the
structures below target the 176.17 air-pocket floor (−5.1%), well beyond the
daily priced move but reachable on the weekly IV; widths are set to NOT cap
the move before the gap-fill completes. All prices **indicative, derived from
6/05 observed prints** `[FLOW:top_premium_trades]`.

### Directional (primary — trigger-conditional, fundamentals-vetoed → carry only)

- **Structure:** put debit spread (bear put vertical)
- **Strike(s) / expiry:** long 180P / short 170P, **2026-07-17** (42 DTE;
  clears the 6/18 OPEX cliff; 7/17 holds 12.3% of chain OI — liquid
  `[OI:term_structure]`; strikes bracket the 176.17 gap-fill and sit on the
  180/170 put walls `[OI:oi_by_strike]`)
- **Debit/credit:** ≈ $3.71 debit (180P ≈ 7.63, 170P ≈ 3.92 observed 6/05)
- **Breakeven:** 176.29 — effectively the gap-fill level itself
- **Max loss:** $3.71/spread (= 100% of debit; book max-loss capped at the
  0.5% carry)
- **Why this structure:** VRP is negative (−0.0874, PREMIUM_BUYING regime —
  debit structures are the funded side `[HIST:vrp]`) and IV is only the
  30.8th percentile `[HIST:iv_percentile_zscore]`, so owning the spread does
  not fight rich vol; the short 170 leg sits on the −19,832 net-OI put wall
  where the move should stall. **Enter ONLY on the primary/aggressive
  trigger** — never inside the 185–190 box (the debate's core finding).
  Catalyst-gap check: a single benign-FOMC gap of the priced weekly move
  (~±2–3%) against the position loses less than the hard stop (max loss
  $3.71 ≈ 2% of spot) — defined risk holds through the binaries.

### Defined-risk alternative (the OPEX-harvest expression)

- **Structure:** call credit spread (bear call vertical)
- **Strike(s) / expiry:** short 195C / long 200C, **2026-06-18** (the OPEX
  cliff itself — sells the 195 call wall + dealer long-gamma pocket, buys the
  200 wall `[OI:oi_by_strike]` `[STRUCT:gex]`; harvests the decay of the
  stranded 190–220 call mass into 6/18 `[OI:term_structure]`)
- **Debit/credit:** ≈ $1.20 credit (indicative; 6/18 195C ≈ $1.75e from the
  49.6% expiry IV, 200C ≈ $0.55e)
- **Breakeven:** 196.20
- **Max loss:** $3.80/spread (width 5 − credit 1.20); book max-loss within
  the same 0.5% carry budget — this structure and the primary are
  either/or, not additive
- **Note:** short-premium into a negative-VRP tape conflicts with the
  phase-5 regime preference — accepted ONLY because it is the one expression
  that pays in both the chop and the breakdown scenarios and is fully
  defined-risk; it loses only on a >5% squeeze through both walls before
  6/18, which is exactly the invalidation (single close >195 = exit).

## Macro overlay (cite phase-6)

- **Tailwinds (for the name):** $25B ASR executing daily — a mechanical bid
  `[MACRO:CRM_Q1FY27_2026-05-28]`; ISM Mfg 54.0 / Services 54.5 — no
  recession bid under cyclicals `[MACRO:ISM_Mfg_2026-06-01]`.
- **Headwinds:** Technology −$807.6M, the day's biggest directional outflow;
  regime TRANSITIONAL, breadth 29.4% bullish, "half position sizes"
  `[MACRO:MarketRegime_2026-06-05 UW]`; AVGO AI-guide shock −$280B / Nasdaq
  −4%, contagion unresolved `[MACRO:AVGO_earnings_2026-06-03]`; CPI 3.78% YoY
  with hot MoM prints + 2y +12bp/30d — rate pressure on duration
  `[MACRO:CPIAUCSL_2026-04 FRED]` `[MACRO:DGS2 FRED]`; UMich 44.8 record low
  `[MACRO:UMich_2026-05-22]`.
- **Net:** **headwind** (4/5, phase-6) — aligned with the short, already
  reflected in the bias, not the size.

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|------|-------|------------------|
| ~2026-06-10 | May CPI release (hot-MoM streak) | − if hot / + if benign (releases magnet) |
| 2026-06-11 | CRM ex-dividend ($0.97e) | neutral/mechanical |
| 2026-06-16/17 | FOMC decision + presser (hold priced, divided committee) | binary; − if hawkish dissent grows |
| 2026-06-18 | CRM monthly OPEX — 25.13% of chain OI unwinds; max-pain 190 | structural; post-OPEX the magnet decays to 185–190 |
| 2026-06-26 / 07-02 | weekly opex tail | minor |
| ~2026-07-01 | ISM June prints | regime confirmation |

(Next earnings 2026-09-02 — outside the window; no event-vol crutch.)

## Post-trade monitoring checklist

- [ ] Daily: `uw hot-chains sweep-persistence` — does the bearish 5/5 streak
  extend or break? A flip is signal-invalidation #1.
- [ ] Daily: `uw options-structure gex` refresh — regime still
  FULLY_NEGATIVE? ZGL reappearing above spot? `[STRUCT:gex]`
- [ ] Daily: `uw dark-pool block-stratified` — buy_ratio >0.60 stepping up on
  the 183–186 shelf = accumulation appearing → exit short carry.
- [ ] 6/10 CPI + 6/17 FOMC: if BOTH resolve benign, exit per macro
  invalidation regardless of price.
- [ ] 6/18 OPEX: track the stranded 190–220 call unwind (dealer short-hedge
  buyback is an UP-flow — the debate's charm point); reassess all bearish
  carry post-expiry.
- [ ] Weekly: NOW/PATH co-movement (cluster 0.863/0.820) — combined software
  exposure stays within one position's risk budget.
- [ ] Next SI settlement: did shorts reload (>7.91%) or cover into the fade?
  `[SENT:short_float fz]`

## Citations summary

1. `[FLOW:sweep_persistence]` — bearish dominant 5/5 sessions, $211.13M,
   consistency 1.0 — phase-1-flow.md §Sweeps (today's tape, phases 1–4)
2. `[STRUCT:gex]` — regime FULLY_NEGATIVE, total −3,333,998, largest mass
   −$13.34M at strike 185 — phase-4-structure.md §GEX (phases 1–4)
3. `[HIST:signal_backtest]` — bearish_flow win_rate 87.5%, n=8, avg −2.73%
   (in-sample, market-wide) — phase-5-historical.md §Signal backtest (5–7)
4. `[MACRO:MarketRegime_2026-06-05 UW]` — Technology −$807.6M biggest sector
   outflow; regime TRANSITIONAL, "half position sizes" — phase-6-macro.md
   §Market regime (6/8)
5. `[DP:level_xcheck DUCKDB]` — genuine 5-session DP shelves 189/201/210
   ($415.9M/$415.3M/$413.7M) overhead; air pocket 186→176 — phase-2-dark-pool.md
   §Price levels
6. `[FUND:earnings_surprises]` + `[SENT:short_float fz]` — 3/3 accelerating
   beats; SI 7.91% / DTC 4.46 — the gate stack that takes the directional to
   watch-only — phase-7b/7c §Verdicts

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*
