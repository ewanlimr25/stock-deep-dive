# Phase 9 — Trade Blueprint

**Ticker:** PATH (UiPath Inc.)
**As-of date:** 2026-06-18
**PM voice:** desk PM running an institutional book
**Spot reference:** $10.27 (phase-0/phase-7 `uw_screener`)
**Upstream phases cited:** phase-0.5 through phase-8b

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

PATH is a **no-edge, counter-trend setup — I'm passing.** The one signal firing
(bullish_flow) backtests at just **37.5%** (n=8, avg move −0.51%) [HIST:signal_backtest]
and the dark pool **refuses to confirm it** (dominant large-tier buy_ratio **0.48**)
[DP:block_stratified], while the FOMC's **6/17 hawkish flip** [MACRO:FOMC_2026-06-17] and the
desk's **NEUTRAL/RANGE plurality** [AGENT:desk] argue against fresh directional risk; the lone
bull pillar (5-session sweep persistence, consistency **1.0** [FLOW:sweep_persistence]) plus
**31.78% short-float** squeeze fuel [SENT:short_float fz] keep this from being a *short*, not
from being a *pass*. **Recommendation: WATCH-ONLY — no directional position.**

## Bias + conviction + horizon

- **Directional bias:** **NEUTRAL** (lean RANGE) — plurality of phases 1–8 (3 NEUTRAL/RANGE vs 1 LONG, 0 SHORT)
- **Conviction (M-01 bin):** **0.55** (floored)
- **Time horizon:** 1-4w (re-evaluate at next FOMC / CPI)
- **Why this bin:** phase-10 confluence ≈ **33** (band 30–49 → 0.55–0.65); the disconfirmed
  debate (phase-8b) floors it at **0.55** — the data is *fighting* the bullish lean, not backing it.

## Entry zones

This is a watch-list, not an active entry. Prices below are **conditions that would change the
stance**, not orders to work today.

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| Primary (to consider a long) | $11.00 | **Reclaim & hold >$11** (max-pain/call-wall) AND DP buy_ratio >0.60 — wait for confirmation the flow is finally validated | [STRUCT:max_pain] / [DP:block_stratified] |
| Aggressive | $10.23 | Bounce off the $10.23 DP support **while $10 holds**, with a fresh ask-side sweep reload | [DP:price_levels] / [FLOW:sweep_persistence] |
| Fade (counter, defined-risk) | $10.79 | Rejection at the $10.79 DP supply cluster → range-fade toward $10 | [DP:price_levels] |

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Support (near) | $10.23 | [DP:price_levels] (also today's 262k buy block) |
| Support (critical line) | **$10.00** | [OI:oi_by_strike] put-wall + [STRUCT:today_gamma_flip] −8.69M resistance_wall |
| Resistance (supply) | $10.79 | [DP:price_levels] heaviest 5-day cluster ($16.4M) |
| Resistance (call wall) | $11.00 → $12.00 | [OI:oi_by_strike] call walls (+7% / +16.7%) |
| Gamma flip (effective) | ~$10.00 | [STRUCT:gex] (tool ZGL 2.34 is a low-price artifact; near-spot gamma turns negative at $10) |
| Largest pin (magnet) | $11.00 | [STRUCT:max_pain] (all expiries, +7%) |

**Price-context color (advisory):** RSI 41.7, price below SMA20/50/200, **−48% from the 52-week
high** and only +11.6% off the 52-week low $9.20 [HIST:rsi fz][HIST:52w_proximity fz] — any long
is bottom-fishing a downtrend, not chasing strength. (Does not alter sizing.)

## Invalidation

- **Price-based:** two daily closes **below $10.00** (put-wall + short-gamma line) → confirms
  breakdown toward the $9.20 52-week low; hard exit for any long.
- **Signal-based:** dark pool shifts to distribution (large-tier buy_ratio <0.45)
  [INSIGHT:institutional_accumulation], **OR** the 5-session bullish sweep persistence breaks
  (consistency drops < ~0.6) [FLOW:sweep_persistence], **OR** cumulative premium flow stays net
  bearish 3 consecutive sessions (already −$3.3M MIXED) [HIST:cumulative_premium_flow].
- **Macro-based:** hawkish surprise at **June CPI ~7/15** or the **~7/28 FOMC** relative to
  consensus [MACRO:FOMC_2026-06-17], or a RISK-OFF regime flip on Iran/energy
  [MACRO:MarketRegime_2026-06-18].

## Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** p_raw = **0.375** (n=8, source=backtest) → N-cap (n<10 → 0.75) →
  capped **p = 0.375** [HIST:signal_backtest].
- **Kelly inputs:** b = **2.70** (target $11 / entry $10.27 / stop $10.00), fraction = 0.25, cap_pct = 5.
- **Raw Kelly:** 0.144 → suggested 3.6%. **Win-rate map ceiling: starter/skip** (p **< 0.50** →
  SHORT-side floor forces starter regardless of Kelly). **Take the smaller → starter (~1%).**
- **Risk gates (each can only cut):**
  - Fundamentals (phase-7b): **CAUTION** (insider MSPR sell-dominated) → cut one step (starter → ½-starter).
  - Sentiment/crowd (phase-7c): **CAUTION** (crowded bullish narrative unconfirmed; crowd_state CROWDED_SHORT) → cut one step → **0**.
  - Correlation cluster (phase-6/8): **none** (PATH~MARA 0.079) → no-op.
  - Sector rotation (phase-6): **neutral for PATH** (tech inflow is semis-led; PATH not participating) → no-op.
  - Debate (phase-8b): bull_residual **0.55** vs bear_residual **0.65** → **disconfirmed** → down-shift bin (floored 0.55) + cut one step.
- **Context modifier (phase-0.5):** `BUSY_NAME_NORMAL_DAY` → no top-of-band sizing (moot at 0).
- **Final size: 0% — WATCH-ONLY.** Negative empirical edge + two CAUTION gates + a disconfirmed
  debate = no directional book risk. The structures below are **illustrative only**.
- **Deviation reason:** none (upward deviation forbidden — multiple gates fired).

## Option structures

Both are **illustrative / "if forced to express a view"** — the desk recommendation is no
position. IV percentile is **0** (cheap) [HIST:iv_percentile_zscore], so any expression should be
**debit (long premium)**, never credit.

### Directional (primary, illustrative — WATCH-ONLY)

- **Structure:** call debit spread (bullish, if forced)
- **Strike(s) / expiry:** **+$10 call / −$12 call, exp 2026-07-17** (29 DTE; clears the Sept-08 earnings/IV-crush)
- **Debit/credit:** ~**$0.60 debit** (est. from phase-1 marks: $10C ~$0.75, $12C ~$0.15)
- **Breakeven:** ~$10.60
- **Max loss:** ~$0.60 / spread (defined)
- **Why this structure:** long leg sits at the $10 put-wall/gamma line, short leg at the $12 call
  wall [OI:oi_by_strike]; cheap IV (pctile 0) favors a debit; the $11 max-pain magnet is the
  realistic target. Only deploy if price reclaims and holds >$11 with DP confirmation.

### Defined-risk alternative (vol / two-sided, illustrative)

- **Structure:** long strangle (non-directional — owns the two-sided tail)
- **Strike(s) / expiry:** **+$9.50 put / +$11 call, exp 2026-07-17**
- **Debit/credit:** ~**$0.70 debit** (est.)
- **Breakeven:** ~$8.80 / ~$11.70
- **Max loss:** ~$0.70 (defined)
- **Why this structure:** the cleanest expression of the NEUTRAL bias — cheap IV (pctile 0) +
  degrading dealer gamma (ZGL collapsed 7.65→2.34) [HIST:gex_time_series] + a binary $10 line
  with **two-sided tails** (32% SI squeeze through $10.79 *or* short-gamma break to $9.20). **Caveat:**
  breakevens are far outside the 2.06% implied move and there's **no catalyst until ~Sept** —
  pure theta bleed near-term; keep it tiny or stand aside.

## Macro overlay (cite phase-6)

- **Tailwinds:** Technology sector inflow +$9.36B, persistence 0.8 [MACRO:sector_flow_persistence]
  (but semis-led, PATH not participating); VIX 16.4 and falling [MACRO:VIX] (aids a vanna-bid if it holds).
- **Headwinds:** FOMC **hawkish flip** 6/17 — ≥1 hike penciled 2026 [MACRO:FOMC_2026-06-17];
  regime **TRANSITIONAL** "half position sizes" [MACRO:MarketRegime_2026-06-18]; breadth 38.6%
  bullish; CPI 4.3% YoY [MACRO:CPIAUCSL_2026-05].
- **Net:** **headwind** for a duration-sensitive, beaten-down software name.

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|------|-------|------------------|
| ~2026-07-15 | June CPI release | ? |
| ~2026-07-28/29 | FOMC meeting (hike risk live) | ? |
| ongoing | Iran / Middle-East energy risk-off | − |
| 2026-09-08 | UiPath Q2 FY2027 earnings (**outside 30d**) | ? |

Front-expiry implied move **±2.06% / ±$0.21** [CTX:implied_move] — structures are tiny-move-priced;
no near-term binary to trade.

## Post-trade monitoring checklist

- [ ] Watch the **$10.00 line daily** — a confirmed break (2 closes) flips the read short-side (short gamma → $9.20).
- [ ] Re-check **dark-pool buy_ratio** daily — a shift >0.60 with sub-spot clusters would be the missing accumulation confirmation.
- [ ] Track **sweep-persistence consistency** — if it stays 1.0 and PATH enters the smart-money/sweep-ratio leaders, the bull pillar strengthens.
- [ ] Re-run **GEX/ZGL** on the phase-4 daily refresh — ZGL has collapsed 7.65→2.34; watch for total_gex sign and a real flip.
- [ ] Monitor **VIX / IV percentile** — a VIX collapse triggers the vanna-bid (long); an IV spike on Iran flips to short-gamma vol expansion.
- [ ] Watch **CPI 7/15 & FOMC 7/28** — the macro headwind is the dominant near-term driver absent earnings.

## Citations summary

1. [HIST:signal_backtest] bullish_flow win_rate **0.375** (n=8, avg −0.51%) — phase-5-historical.md §Signal backtest
2. [DP:block_stratified] dominant large-tier **buy_ratio 0.48** (DP non-confirmation) — phase-2-dark-pool.md §Tier breakdown
3. [FLOW:sweep_persistence] bullish campaign **consistency 1.0, 5/5 sessions, $2.27M** — phase-1-flow.md §Sweeps
4. [STRUCT:gex] near-spot **short gamma**, $10 strike gex −8.69M — phase-4-structure.md §GEX / today_gamma_flip
5. [MACRO:FOMC_2026-06-17] hawkish dot-plot flip (≥1 hike 2026) — phase-6-macro.md §Rates
6. [SENT:short_float fz] **31.78%** short float, DTC 3.78 — phase-7c-sentiment.md §Short interest
