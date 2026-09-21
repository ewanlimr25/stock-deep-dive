# Phase 9 — Trade Blueprint

**Ticker:** GOOG
**As-of date:** 2026-06-22
**PM voice:** desk PM running an institutional book
**Spot reference:** $348.78 (phase-2 close; gex intraday $348.31)
**Upstream phases cited:** phase-0.5 through phase-8b

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

GOOG just printed a **fresh 30-day low** (−12% from $397) and **flipped out of 21
straight sessions of long-gamma into a short-gamma, vol-expansion regime** (total_gex
**−3.84M**, ZGL null) `[STRUCT:gex]` `[HIST:gex_time_series]` — precisely where the only
constructive micro-signals (a **hollow** mega-tier dark-pool buy of 0.764 inside a
**0.562-NEUTRAL** whole book `[DP:block_stratified]`, and near-money call OI building
straight **into the $362–371 overhead supply shelf** `[DP:price_levels]`) lack the edge to
fight an idiosyncratic catalyst cluster (Gemini AI co-lead to OpenAI, capex/FCF −47%,
antitrust) into a hawkish-Fed tape `[MACRO:Alphabet_2026-06-22]`. The desk returned **zero
LONG votes**, the bull/bear debate **disconfirmed** (bear 0.75 vs bull 0.55)
`[DEBATE:disconfirmed]`, and the bullish_flow backtest is a **coin flip (50%, n=8)**
`[HIST:signal_backtest]` — so there is **no directional edge to size into**. Net:
**WATCH-ONLY by default**; if expressed at all, a **defined-risk RANGE trade ($340–365)
with the downside as the fatter tail**, sized to a tactical **starter** after four risk
gates fired.

## Bias + conviction + horizon

- **Directional bias:** **RANGE** (downside-fatter tail). *Plurality of phases 1–8 was
  non-directional — 3 NEUTRAL + 1 RANGE + 1 SHORT, **0 LONG**; RANGE is the tradeable
  form of that consensus, with the $340–365 boundaries the desk drew and the downside as
  the fatter tail.*
- **Conviction (M-01 bin):** **0.55** (slight/no edge — the floor; debate disconfirmation
  down-shifted it here and it cannot go lower).
- **Time horizon:** **1-4w** (to the 7/17 OPEX; deliberately *before* the 7/22 earnings
  binary).
- **Why this bin:** UW composite is MIXED at 6.2% confidence `[INSIGHT:conviction_matrix]`
  and the empirical win-rate is 0.50 — this is the lowest narrative-confidence band, and I
  expect phase-10 confluence in the low band to match.

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| Primary | **break & hold < $340** | loss of the put wall / worst −GEX strike (−5.79M) → downside continuation; enter the put debit spread | `[OI:oi_by_strike]` `[STRUCT:gex]` |
| Aggressive | **rally into $362–365** | rejection at the DP supply shelf / 7/17 max-pain → fade the bounce (put spread or call credit spread) | `[DP:price_levels]` `[STRUCT:max_pain]` |
| Fade (plan B) | **two closes > $362 on volume** | overhead supply RECLAIMED — thesis flips; cover bears, small tactical long toward $370 only with a whole-book DP buy_ratio >0.62 | `[DP:price_levels]` |

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Support | **$340** (put wall, net −13,215) → **$330** (strongest, net −30,223) | `[OI:oi_by_strike]` |
| Resistance | **$362–371** DP supply shelf (heaviest **$367.46**, $1.57B) | `[DP:price_levels]` |
| Gamma flip | **null** (net short-gamma throughout 45 DTE); functional − → + transition ~**$362–365** | `[STRUCT:gex]` |
| Largest pin | **$360** (7/17 max-pain) / **$365** (6/26 max-pain) — pull ABOVE spot | `[STRUCT:max_pain]` |

*Price-context color (advisory):* RSI **39.99** — weak but **not** oversold (<30), so no
mean-reversion trigger is armed; GOOG sits **−13.8% off the 52-wk high $404.47** but
**+12% above the 200-DMA** `[HIST:rsi fz]` `[HIST:52w_proximity fz]`. Don't treat the dip
as a bottom; it is a pullback without a momentum floor yet.

## Invalidation

- **Price-based:** for the downside-lean — **two daily closes above $362** (DP supply
  shelf reclaimed `[DP:price_levels]`) negates the range-cap and the bearish tilt. For the
  range itself — **two daily closes outside $335–367**.
- **Signal-based:** **GEX flips back POSITIVE** (long-gamma re-flip) on the phase-4 daily
  refresh while spot holds `[STRUCT:gex]` — kills the vol-expansion/downside thesis; OR
  **institutional-accumulation turns to a clear ACCUMULATION** (whole-book DP buy_ratio
  >0.62 for 2 sessions) `[INSIGHT:institutional_accumulation]` — the hollow-buy thesis
  breaks.
- **Macro-based:** a **dovish CPI (~07-15)** or an **AI-narrative reversal** (talent-exit
  walk-back / capex reframe) that re-rates the growth multiple up `[MACRO:CPIAUCSL_2026-05]`
  `[MACRO:Alphabet_2026-06-22]` — invalidates the downside lean.

**Exit on invalidation:** **Hard stop** on the debit structures (close 100% on a two-close
$362 reclaim or a GEX re-flip positive). The condor (if used) is a **roll/close** at a
short-strike breach.

## Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** p_raw = **0.50** (phase-5 `bullish_flow` backtest, **n=8**,
  source=**backtest**) → N-cap (n<10) = 0.75, not binding → **capped p = 0.50**
  `[HIST:signal_backtest]`. *(No bearish/`dark_pool_accumulation` backtest existed —
  empty — so the bullish base rate is the only empirical p; at 0.50 it reads as "no edge
  either direction.")*
- **Kelly inputs:** b = **2.5** (put debit spread 345/330: max-profit ~$10.8 / max-loss
  ~$4.2), fraction = 0.25, cap_pct = 5.
- **Raw Kelly:** (0.50×2.5 − 0.50)/2.5 = **0.30** → suggested = min(0.30×0.25×100, 5) =
  5.0%, but the **win-rate map ceiling at p=0.50 is HALF = 2.5%** → **pre-gate size 2.5%**.
- **Risk gates** (each cuts; order applied):
  1. **Fundamentals (phase-7b): CAUTION** → cut one step (half → starter). *Forward
     EPS decel + FCF −47% despite strong trailing quality.*
  2. **Sentiment/crowd (phase-7c): CAUTION**, crowd_state **CROWDED_LONG** → cut one step.
     *Bearish news momentum + crowded-long analysts (0 sells) with downgrade risk.*
  3. **Correlation cluster (phase-6): none** (GOOG is the only blueprint today) → no-op.
  4. **Sector rotation (phase-6): ADVERSE** (Comm Services #1 net outflow −$118M) → cut
     half a step.
  5. **Debate (phase-8b): DISCONFIRMED** — bull_residual **0.55** vs bear_residual
     **0.75** → down-shift the bin one (already at floor 0.55) **and** cut one step.
- **Context modifier (phase-0.5):** `unusual_verdict = GENUINELY_UNUSUAL` → no-op (but it
  was *directional-premium* unusualness, not a clean tradeable edge — do not size up).
- **Final size:** **0.6% of book risk (deep STARTER)** — four gates collapsed the 2.5%
  half-ceiling. **The honest default is WATCH-ONLY / 0% directional**; 0.6% is the
  absolute-max tactical starter, **defined-risk only**, if the desk insists on a position.
- **Deviation reason:** none (no upward deviation — forbidden anyway, four gates fired).

## Option structures

### Directional (primary) — the downside-tail expression

- **Structure:** **Put debit spread** (long vol, defined risk).
- **Strikes / expiry:** **Buy GOOG 2026-07-17 $345 Put / Sell 2026-07-17 $330 Put**
  (strikes anchored to the $340/$330 put walls `[OI:oi_by_strike]`; 7/17 = the 19.94%-OI
  gravity well and **expires 5 days BEFORE the 7/22 earnings** → no earnings IV crush /
  binary gap risk).
- **Debit/credit:** ~**$4.20 debit** (illustrative; IV30 ~33%, 25 DTE).
- **Breakeven:** ~**$340.80**.
- **Max loss:** **$4.20** (the debit; ≤ starter size of book risk).
- **Max profit:** ~$10.80 (if ≤ $330 at expiry).
- **Why:** in a freshly **short-gamma, vol-expansion** regime `[STRUCT:gex]` you want to
  **own gamma, not sell it**; this plays the $340 break toward the $330 wall with capped,
  defined risk, sized to the ~$9.18 front-expiry move `[CTX:implied_move]` (the $345→$330
  target is ~1.6× a 25-day implied move — reasonable, not rich).

### Defined-risk alternative — the range scenario

- **Structure:** **Iron condor** (defined risk). **CAVEAT: this is short-vol into a
  vol-expansion regime** — the risk-monitor explicitly flagged short-premium as
  regime-inappropriate here, and VRP is FAIR (+0.0107, **no premium edge**) `[HIST:vrp]`.
  Use **only** for the explicit chop scenario ($340 holds, vol contracts), sized minimal;
  **the put debit spread or WATCH-ONLY is preferred.**
- **Strikes / expiry:** **Sell 7/17 $335 Put / Buy $325 Put** and **Sell 7/17 $365 Call /
  Buy $375 Call** (short strikes at the put wall floor $335 and the max-pain/supply ceiling
  $365 `[STRUCT:max_pain]` `[DP:price_levels]`).
- **Debit/credit:** ~**$3.00 net credit**.
- **Breakevens:** ~**$332** and ~**$368**.
- **Max loss:** ~**$7.00** (one side; $10 width − $3 credit).

*(Alternative defined-risk bearish expression if you only want one wing: a **call credit
spread $365/$375 7/17** — sells the overhead supply directly; ~$2.50 credit, max loss
~$7.50, breakeven ~$367.5.)*

## Macro overlay (cite phase-6)

- **Tailwinds:**
  - No broad risk-off — **SPY near highs (744, above 50-sma), VIX 17.28 falling**
    `[MACRO:SPY_2026-06-22]`; **10y eased 4.57→4.46** `[MACRO:DGS10_2026-06-18]`.
  - GOOG is the **relative-strength / quality leader** of a de-rated cohort (+11% YTD vs
    peers −15% to −43%) `[FUND:peer_pe fz]`; strong-buy target **$433.76 (+24%)** is a
    longer-horizon floor argument.
- **Headwinds:**
  - **Idiosyncratic catalyst cluster** — AI-talent exodus, **capex $180–190B / FCF −47%**,
    antitrust remedy phases `[MACRO:Alphabet_2026-06-22]`.
  - **FOMC dot plot flipped to a HIKE** (Warsh), **sticky inflation CPI ~4.2%**
    `[MACRO:FOMC_2026-06-17]` `[MACRO:CPIAUCSL_2026-05]`.
  - **Comm Services #1 net-directional sector OUTFLOW −$118M** `[MACRO:sector_flow_2026-06-22]`.
- **Net:** **HEADWIND.**

## Catalyst calendar (next 30d)

Front-expiry implied move **±2.63% / ±$9.18** `[CTX:implied_move]` — read each binary
against it.

| Date | Event | Impact direction |
|------|-------|------------------|
| ~2026-07-15 | CPI (June) release | ? (sticky-inflation risk; market-level) |
| 2026-07-17 | July monthly OPEX (19.94% OI cliff, call-heavy) | ? (pin toward $360 max-pain) |
| **2026-07-22** | **Alphabet Q2 earnings** | **−** (negative-skew binary: capex/FCF/AI-moat in focus; far exceeds ±2.63%) |
| ~2026-07-28 | next FOMC | ? (hawkish-hold risk) |

## Post-trade monitoring checklist

- [ ] **Re-run phase-4 GEX daily** — a flip back to POSITIVE (long-gamma) at spot
  invalidates the vol-expansion/downside thesis (`uw options-structure gex`).
- [ ] **Watch the $340 put wall** — a break & hold below it is the entry/continuation
  trigger; a firm hold + reclaim of $350 weakens the bearish lean.
- [ ] **Re-check dark-pool block-stratified daily** — whole-book buy_ratio sustaining
  >0.62 across block+large tiers would turn "hollow" accumulation into a real base
  (`uw dark-pool block-stratified`).
- [ ] **Track analyst revisions into 7/22** — the first downgrades (0 sells today) confirm
  the crowded-long capitulation risk (`finnhub stock/recommendation`).
- [ ] **Flatten/roll before 2026-07-22** — these structures are designed to be closed by
  7/17; do **not** carry naked directional risk into the earnings binary.

## Citations summary

1. `[STRUCT:gex]` — short-gamma `FULLY_NEGATIVE`, total_gex **−3.84M**, ZGL null —
   phase-4-structure.md §GEX.
2. `[HIST:gex_time_series]` — **first long→short-gamma flip in 21 sessions at a fresh
   30-day low** ($397→$348.78) — phase-5-historical.md §GEX time series.
3. `[DP:block_stratified]` — mega buy_ratio **0.764** but **whole-book 0.562 NEUTRAL** (14
   trades) — phase-2-dark-pool.md §Tier breakdown.
4. `[MACRO:Alphabet_2026-06-22]` — AI-talent exodus + **capex $180–190B / FCF −47%** +
   antitrust; −5% worst day in >1yr — phase-6-macro.md §Sector overlay.
5. `[HIST:signal_backtest]` — bullish_flow win_rate **0.50 (n=8)** — phase-5-historical.md
   §Sizing handoff.
6. `[DEBATE:disconfirmed]` — bear 0.75 vs bull 0.55, disconfirmed=true — phase-8b-debate.md.
