# Phase 9 — Trade Blueprint

**Ticker:** NBIS
**As-of date:** 2026-06-05
**PM voice:** desk PM running an institutional book
**Spot reference:** $227.81 (screener close, phase-0.5; Friday range $216.69–250.75, phase-6)
**Upstream phases cited:** phase-0.5 through phase-8b

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

NBIS printed a 99.6th-percentile gross-premium day that netted to **−$9.6M and
a delta-flat ex-0DTE tape** [FLOW:insights_deep_dive] [FLOW:delta_notional
DUCKDB] while every dark-pool tier sat balanced (0.497–0.523)
[DP:block_stratified] — there is no directional edge to own here, only a
violently repriced range. The week's one persistent signal is bearish
(5/5-session sweep dominance, $643.6M [FLOW:sweep_persistence]; price-vs-flow
divergence resolving [INSIGHT:price_vs_flow]) but it is **double-vetoed**: the
business is improving on 2 of 3 quality axes (4/4 beats, ARR +54% QoQ
[FUND:earnings_surprises]) and the short is crowded into squeeze-shaped
microstructure (22.43% short float [SENT:short_float fz semi-monthly], inverted
skew [STRUCT:term_skew], FULLY_NEGATIVE gamma [STRUCT:gex]). With macro a
4/5-conviction headwind (AVGO guide-down + hike-risk repricing
[MACRO:AVGO_guidance_2026-06-03] [MACRO:DGS2_2026-06-04 FRED]) and all four desk
agents at conviction-2 stand-aside [AGENT:all], the book trades the
**205–250 box defined-risk only** and rents out the backwardated front of the
vol curve rather than picking a side.

## Bias + conviction + horizon

- **Directional bias:** **RANGE** (205–250 box; bearish tilt acknowledged but
  vetoed as a position)
- **Conviction (M-01 bin):** **0.55**
- **Time horizon:** **1-4w** (through the Jun-10 CPI → Jun-16/17 FOMC → Jun-18
  OPEX gauntlet)
- **Why this bin:** estimated phase-10 confluence ≈ 41 (band 30–49 → 0.55–0.65);
  the 7b VETO scores `--` by hard rule and the 7c VETO subtracts 10 one-sided —
  with two gates fired, the bottom of the band is the honest bin.

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| Primary | $226–230 | spot stabilizes above the AH low shelf (no new low > 30 min) → put on the Jun-12/Jul-17 220 calendar at the 227.81/$41M + 230/$30M pivot cluster | [DP:price_levels] |
| Aggressive | $221.0 | tag of the 220.7–221.0 AH-low prints + 220 put wall with immediate reclaim (no 15-min close below) | [DP:extended_hours] [OI:oi_by_strike] |
| Fade | $249.5 | rejection at the 249.2–251.7 trapped-supply cluster (= 250 call wall, net +21,723) — counter-trade short-delta there | [DP:price_levels] [OI:oi_by_strike] |

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Support | $220.7 (then 200–205 shelf, 31.4k puts ≤30 DTE) | [DP:extended_hours] [OI:oi_by_strike --dte-max 30] |
| Resistance | $250 (= $249.2–251.7 DP cluster, $367M trapped) | [OI:oi_by_strike] [DP:price_levels] |
| Gamma flip | none — ZGL null, book FULLY_NEGATIVE at every strike; biggest node AT spot ($227.5, −$2.93M) | [STRUCT:gex] |
| Largest pin | $235 (Jun-12 max-pain, +3.2%); Jun-26 at $230 | [STRUCT:max_pain] |

Price-context color (advisory): RSI(14) 56.1 — neutral, no oversold edge at the
lows [HIST:rsi fz]; spot is −18.3% from the 52-week high ($278.84) but still
+94% above its SMA200 [HIST:52w_proximity fz] — a "dip" only by last week's
prices. Color only; does not enter sizing.

## Invalidation (of the RANGE thesis)

- **Price-based:** two daily closes **below $205** (the 200–205 put shelf +
  descending GEX nodes [OI:oi_by_strike] [STRUCT:gex]) → bear break; or two
  daily closes **above $250** (call wall + trapped supply [DP:price_levels]) →
  squeeze break. Single-day reference: a close beyond ±1.5× the ~7%/day ATR
  band (≈±$24 [HIST:vrp realized 120%]) ends the range read same-day.
- **Signal-based:** `sweep-persistence` extends to 6+/6 bearish with strike
  concentration shifting to ≤200 [FLOW:sweep_persistence]; or cumulative
  premium flow turns net bearish 3 consecutive sessions
  [HIST:cumulative_premium_flow]; or any DP tier exits the 0.45–0.55 band
  [DP:block_stratified]; or conviction-matrix flips MIXED → directional
  [INSIGHT:conviction_matrix].
- **Macro-based:** hawkish surprise at the Jun-10 CPI or Jun-16/17 FOMC (hike
  signaled / dots up) [MACRO:FOMC_calendar] — bear break becomes primary; OR a
  major AI-capex *positive* surprise (mega-cap capex raise reversing the AVGO
  read [MACRO:AVGO_guidance_2026-06-03]) — squeeze becomes primary. Either
  direction kills RANGE.
- **Exit on invalidation:** **hard stop** — close the calendar/condor 100% on
  the second qualifying close (debit structures, no roll); the armed
  directional plan below replaces it only after gates re-evaluate.

## Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** p_raw = **0.875** (n=**8**, source=backtest)
  → N-cap (n<10 → 0.75) → **capped p = 0.75** [HIST:signal_backtest]
- **Kelly inputs:** b = 1.67 (vetoed directional spread: 12.5 gain / 7.5 risk),
  fraction = 0.25, cap_pct = 5
- **Raw Kelly:** (0.75×1.67 − 0.25)/1.67 = **0.600** → suggested = min(0.600 ×
  0.25 × 100, 5) = **5.0%** · **Win-rate map ceiling:** p ≥ 0.70 → full (≤ cap)
- **Risk gates (all five, in order):**
  - Fundamentals (phase-7b): **VETO** (2 of 3 axes contradict the bear flow) →
    **directional size = watch-only / 0%**
  - Sentiment/crowd (phase-7c): **VETO** (CROWDED_SHORT, 22.43% SI + squeeze
    microstructure) → **directional size = watch-only / 0%** (reinforces)
  - Correlation cluster (phase-6/8): **none** (NBIS max pairwise ρ = 0.222 vs
    CRM/NOW/PATH/RKT) → no cut
  - Sector rotation (phase-6): **adverse** (CommSvc −$130M day; gross tilt
    −51%/5d) → cut half step on whatever survives
  - Debate (phase-8b): bull_residual 0.65 vs bear_residual 0.55 →
    **disconfirmed = false** → no cut
- **Context check (phase-0.5):** `GENUINELY_UNUSUAL` → no cap (no-op).
- **Final size: 0.0% directional** (double-vetoed, Kelly notwithstanding).
  **Defined-risk carry only, max-loss budget ≤ 1.0% of book risk combined**
  (starter: market-regime "half position sizes" [MACRO:MarketRegime UW] +
  adverse-rotation half-step cut applied to the carry sleeve).
- **Deviation reason:** none (upward deviation forbidden — gates fired).

## Option structures

(Sized to the expected move, N4: front-expiry (Jun-12) expected move ≈
**±15.7% / ±$35.8** — derived from IV30d 1.117 × √(5/252); the screener
`implied_move_perc` (0.41%) is flagged SUSPECT upstream [CTX:implied_move_pct,
phase-0.5 DATA NOTE]. Front IV 132.1% vs 34d 111.3% = backwardation 1.187
[STRUCT:front_end_iv_ratio]. All prices indicative off 2026-06-05 marks —
reprice at entry.)

### Defined-risk carry (primary) — rent out the event hump

- **Structure:** put calendar (sell front event-vol, own back month)
- **Strike(s) / expiry:** short Jun-12 220P / long Jul-17 220P (strike = the
  220 put wall [OI:oi_by_strike] / AH-low shelf [DP:extended_hours])
- **Debit/credit:** ≈ $14.0 debit (anchors: Jun-12 215P traded ~$9.6–10.3
  vol-weighted; Jul-17 220P ~$29.0 vol-weighted [FLOW:sweeps]; OTM-adjusted)
- **Breakeven:** path-dependent — max value with spot ≈ 220 at Jun-12 expiry;
  indicative profit zone ≈ $205–240 at front expiry
- **Max loss:** the $14.0 debit (≤1.0% book risk → sleeve sizing)
- **Why this structure:** VRP is negative (−0.0841, PREMIUM_BUYING — naked
  short vol disallowed [HIST:vrp]) but the front/back ratio of 1.187 with the
  hump at Jun-18 (143.6%) [STRUCT:iv_term_structure] lets us be net-long vol
  while *selling only the over-priced CPI/FOMC window*; the short leg expires
  before FOMC, the long leg owns July at 111% on a name realizing 120%.

### Directional (watch-only — double-vetoed; activates ONLY on trigger + gate re-check)

- **Structure:** put debit spread — **armed, not live**: requires a daily close
  < $220 with `sweep-persistence` extending bearish [FLOW:sweep_persistence],
  then a fresh 7b/7c re-read
- **Strike(s) / expiry:** long Jun-26 220P / short Jun-26 200P (target = the
  200–205 shelf [OI:oi_by_strike]; expiry holds the Jun-26 max-pain 230 — exits
  before quarter-end LEAP noise, accepts the FOMC binary deliberately)
- **Debit/credit:** ≈ $7.5 debit (indicative) · **Breakeven:** ≈ $212.5
- **Max loss:** $7.5 · max gain $12.5 → b ≈ 1.67 (the Kelly b above)
- **Marked: fundamentals-vetoed + sentiment-vetoed — 0% until triggers fire.**

### Defined-risk alternative (conventional, NOT preferred)

- **Structure:** iron condor (box-edges per the level map)
- **Strike(s) / expiry:** Jun-26 — short 200P / long 190P + short 250C / long
  260C (sells the put shelf and the call wall [OI:oi_by_strike])
- **Debit/credit:** ≈ $5.0 credit (indicative; 130%-IV chains pay fat edges)
- **Breakeven:** ≈ $195 / $255
- **Max loss:** $5.0 (width 10 − credit 5)
- **Warning:** the 200–250 body (±11%) is *narrower than the ±15.7% weekly
  expected move* and VRP is negative — statistically the realized tape has been
  beating implied [HIST:vrp]. Published as the conventional range expression;
  the calendar is the better-priced trade. If used: half the carry sleeve, roll
  or close at first short-strike touch.

**Catalyst-gap check (N4):** the calendar's short leg expires Jun-12 — before
FOMC; a CPI-day gap of one expected move (±7%) moves the calendar against us
< its max loss (debit-capped) ✓. The condor straddles BOTH binaries — a single
FOMC gap of the weekly expected move (±15.7%) breaches the body; that is why it
is flagged not-preferred and half-sleeve ✓ (max loss still capped).

## Macro overlay (cite phase-6)

- **Tailwinds:**
  - ISM Mfg 54.0 / Services 54.5 — real activity strong; AI demand (Q1 ARR
    +54% QoQ) is not a demand-side problem [MACRO:ISM_2026-06-01/03]
  - France/SoftBank AI commitments $61.7bn with Nebius named (Jun-2) — the
    sector's spend narrative is not dead [SENT:company_news 2026-06-02]
- **Headwinds:**
  - AVGO AI guide-down ($16bn vs $17.2bn) → complex-wide derate; NBIS −12.27%
    was beta with no company news [MACRO:AVGO_guidance_2026-06-03]
  - Hike-risk repricing: DGS2 4.05% (+17bp/30d) vs DFF 3.62% on +172k NFP
    [MACRO:DGS2_2026-06-04 FRED] [MACRO:PAYEMS_2026-05 FRED] — direct threat to
    a $16–20bn-capex funding story [FUND:capex]
  - CPI +3.78% YoY / core PCE +3.29% into the Jun-10 print [MACRO:CPIAUCSL_2026-04 FRED]
  - Regime TRANSITIONAL, breadth 29.4% bullish, VIX 16.7→21.5 [MACRO:MarketRegime UW]
  - Sector rotation adverse: CommSvc −$130M day, gross tilt −51%/5d
    [MACRO:sector_flow_persistence UW]
- **Net:** **headwind**

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|------|-------|------------------|
| 2026-06-10 | May CPI 8:30 ET | − (hot print → hike pricing) / ? |
| 2026-06-12 | Weekly OPEX — max-pain 235 above spot, P/C OI 3.0 | + (mild magnet) |
| 2026-06-16/17 | **FOMC + SEP** (the Jun-18 IV-hump event) | ? (binary) |
| 2026-06-18 | Monthly OPEX — 20.9% of total OI rolls off | ? (positioning reset) |
| 2026-06-26 | Jun-26 expiry (max-pain 230); U-Mich June final | ? |
| ongoing | AI-capex newsflow post-AVGO (peer guides) | ± episodic |
| 2026-08-06 | NBIS earnings (outside 30d — anchor only) | ? |

## Post-trade monitoring checklist

- [ ] Daily: `uw hot-chains sweep-persistence --symbol NBIS` — a 6th/7th
  consecutive bearish session or strike-shift ≤200 = signal invalidation arm
- [ ] Daily: `uw dark-pool block-stratified` — any tier leaving 0.45–0.55
  ends the "balanced institutions" leg of the thesis
- [ ] Mon 06-08: did the Jun-26 285P write print in OI (chain-oi-changes
  06-08 file)? Confirms/denies the phase-1 financing-structure read
- [ ] Daily: `uw options-structure gex` — total_gex recrossing positive (ZGL
  reappearing) restores mean-reversion and *improves* the condor/calendar
- [ ] 06-10 CPI + 06-16/17 FOMC: re-run phase-6 verdict same day; hawkish
  surprise = exit carry, evaluate armed put spread (with fresh 7b/7c)
- [ ] Next SI settlement: did the 45.10M short interest cover into the flush?
  Squeeze-fuel re-read for the fade entry
- [ ] Front/back IV ratio (`front-end-iv-ratio`): hump decay after FOMC is the
  calendar's profit engine — track 1.187 → <1.0

## Citations summary

Minimum 3 distinct upstream datapoints (M-04), spot-checkable:

1. [FLOW:delta_notional DUCKDB] — ex-0/1DTE customer delta-notional ≈ +$0.000bn
   (+0.265 −0.365 −0.195 +0.295) — phase-1-flow.md §Aggressor split
2. [DP:block_stratified] — tier buy_ratios mega 0.518 / block 0.523 / large
   0.497 on $814.46M — phase-2-dark-pool.md §Tier breakdown
3. [FLOW:sweep_persistence] — 5/5 sessions bearish-dominant, consistency 1.0,
   $643,611,015 — phase-1-flow.md §Key signals
4. [FUND:earnings_surprises] — 4/4 beats, surprise% +20.2→+59.1 —
   phase-7b-fundamentals.md §Earnings-surprise history
5. [SENT:short_float fz semi-monthly] — 22.43% short float / 45.10M shares /
   DTC 2.54 — phase-7c-sentiment.md §Short interest
6. [STRUCT:gex] — regime FULLY_NEGATIVE, total_gex −$12,546,295, ZGL null —
   phase-4-structure.md §GEX
7. [MACRO:AVGO_guidance_2026-06-03] — AVGO Q3 AI guide $16bn vs $17.2bn est →
   sector derate — phase-6-macro.md §Sector overlay
8. [HIST:signal_backtest] — bearish_flow win_rate 87.5% (n=8, in-sample) →
   capped p 0.75 — phase-5-historical.md §Sizing handoff
