# Phase 9 — Trade Blueprint

**Ticker:** KWEB
**As-of date:** 2026-05-22
**PM voice:** desk PM running an institutional options-overlay book
**Spot reference:** $26.91 (phase-1-flow.md / phase-7-insights.md)
**Upstream phases cited:** phase-0.5 through phase-8b

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

KWEB at $26.91 is a **low-conviction RANGE trade, not a directional long**: the
bullish lit call skew (net **+$2.65M**, P/C **0.25** `[FLOW:insights_deep_dive]`) is
**unconfirmed by the share tape** — institutions distributed the largest blocks
(mega buy_ratio **0.0**, block **0.306** `[DP:block_stratified]`) into a **−12%
downtrend** while the 30–31 calls were **written/closed** (Jun 31C OI **−13,668**
`[OI:decrease_with_volume]`). The one real edge is structural: **IV sits at the
3.33 percentile** `[HIST:iv_percentile_zscore]` with realized > implied (VRP
**−0.039** `[HIST:vrp]`), so vol is **mispriced cheap** into the late-May/early-June
China mega-cap earnings cluster and a fragile post-summit tariff thaw
`[MACRO:USChina_summit_2026-05-15]`. Play it as **cheap, defined-risk convexity with
a downside lean** — the 5-agent desk was unanimously non-directional (avg conviction
**2.6** `[AGENT:risk-monitor]`), capped at $28 and flipping long only above $29.

## Bias + conviction + horizon

- **Directional bias:** **RANGE** (downside lean; long-convexity expression)
- **Conviction (M-01 bin):** **0.55**
- **Time horizon:** **1-4w** (to June OPEX 06-18, capturing the China earnings cluster)
- **Why this bin** (one sentence): every UW composite reads MIXED
  (`conviction_matrix` MIXED, KWEB absent from bullish confluence `[INSIGHT:signal_confluence]`),
  both quality gates (7b/7c) are CAUTION, and the debate left the cautious range view
  standing — a slight-edge, non-directional bin (phase-10 confluence expected ~mixed/low-50s).

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| Primary | **$27.95–28.10** | rejection at the 5-day DP supply node / gamma-flip approach → put on the downside-lean structure | `[DP:price_levels]` `[STRUCT:gex]` |
| Aggressive | **< $26.88** | break-and-hold below today's battleground → short-gamma flush toward 25–26 | `[DP:price_levels]` `[STRUCT:gex]` |
| Fade (plan B) | **sustained close > $29** | dealer gamma flips long + vanna-squeeze → flip to the call side / chase 30–31 | `[STRUCT:gex]` `[OI:opex_concentration]` |

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Support | **$26.88–26.95** (today's node); then **$26.36** (pre-mkt low); then **$25–26** (Jul put floor) | `[DP:price_levels]` `[DP:extended_hours]` `[OI:biggest_increases]` |
| Resistance | **$27.95–28.10** (5-day node); then **$30–31** call walls | `[DP:price_levels]` `[OI:opex_concentration]` |
| Gamma flip | **~$28.5** (short→long gamma; 27 = −$41.5M GEX) | `[STRUCT:gex]` |
| Largest pin | **none in OPEX week** (KWEB absent from `pin_risk`); structural magnet = June 30–31 walls | `[OI:pin_risk]` `[OI:opex_concentration]` |

## Invalidation

- **Price-based:** two daily closes **above $28.10** (reclaims the DP supply node and
  approaches the gamma flip) → the range-high/fade is broken; a sustained close
  **>$29** flips the thesis outright long. `[DP:price_levels]` `[STRUCT:gex]`
- **Signal-based:** dealer regime flip — **DEX turns positive / GEX flips spot into
  long-gamma above $28.5** on the phase-4 daily refresh `[STRUCT:dex]` `[STRUCT:gex]`,
  **or** `insights_institutional_accumulation` flips NEUTRAL→**ACCUMULATION**
  `[INSIGHT:institutional_accumulation]`, **or** cumulative premium flow turns
  strongly bullish 3 consecutive sessions with price following `[HIST:cumulative_premium_flow]`.
- **Macro-based:** a **signed US-China tariff deal or large China stimulus headline**
  (the summit framework formalizes) → risk-on gap for China `[MACRO:USChina_summit_2026-05-15]`;
  conversely a **Taiwan escalation** `[MACRO:USChina_2026-05-22]` *confirms* the
  downside lean rather than invalidating it.
- **Exit rule:** defined-risk debits → **hard stop**: close the put-spread 100% on
  two closes > $28.10; the strangle is held to its capped max-loss (no stop needed).

## Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** p_raw = **1.00** (phase-5 `signal_backtest_win_rate`,
  n=**13**, source=**backtest**), N-cap (10≤n<20) → 0.85 `[HIST:signal_backtest]`.
  **BUT the backtested signal is directional `bullish_flow`, which does NOT match
  this trade's RANGE bias**, and phase-5 flagged it **market-wide / clustered / not
  KWEB** (effective independent N ≈ 1–2). Per the rubric I therefore **fall back to
  the conviction bin**: **p = 0.55** (proxy-capped at 0.65). This only *reduces* size.
- **Kelly inputs:** b = **1.5** (put-spread to the 25 short-strike), fraction = 0.25, cap_pct = 5.
- **Raw Kelly:** (0.55×1.5 − 0.45)/1.5 = **0.25** → ×0.25 = 6.25%. **Win-rate map
  ceiling:** p=0.55 ∈ [0.50,0.70] → **half ≤ 2.5%** (take the smaller → 2.5%).
- **Risk gates:**
  - **Fundamentals (7b): CAUTION** → cut one step (2.5% → ~1.25%). BABA 4 straight
    misses, latest −89.5% `[FUND:earnings_surprise]`.
  - **Sentiment/crowd (7c): CAUTION** (crowd_state BALANCED, de-risking) → cut one
    step (~1.25% → ~0.6%). 5-day outflows −$281.5M; KWEB laggard `[SENT:fund_flows]`.
  - **Correlation cluster (6/8): none** (KWEB orthogonal to ENPH/NTAP/PATH/SYM) → no-op.
  - **Sector rotation (6): NEUTRAL** (not adverse) → no-op.
  - **Debate (8b):** bull_residual **0.70** vs bear_residual **0.60** → **disconfirmed = false** → no-op.
  - **Context (0.5): GENUINELY_UNUSUAL** → no-op (but the "unusual" is *directional
    skew*; the trade isn't directional, reinforcing the small size).
  - **Macro regime: TRANSITIONAL** ("half size, defined-risk") → reinforces the above.
- **Final size:** **0.5% of book risk** (max-loss of the chosen debit structure ≤
  0.5% of book) — a **probe/starter** after two CAUTION cuts off a half ceiling.
- **Deviation reason:** none (size set *below* suggested — always permitted).

## Option structures

### Directional (primary) — downside-lean, defined-risk debit

- **Structure:** **Jun-18 27/24 put debit spread** (bearish lean)
- **Strike(s) / expiry:** buy 27P / sell 24P, **2026-06-18** (27 DTE; captures the
  China earnings cluster, before any July time premium)
- **Debit/credit:** ~**$0.80 debit** (27P ≈ $1.10, 24P ≈ $0.30; IV ~36–37%)
- **Breakeven:** ~**$26.20**
- **Max loss:** **$0.80** (the debit) — caps single-headline gap risk (N4 satisfied)
- **Why this structure:** expresses the distribution/downtrend lean toward the $25–26
  Jul put floor `[OI:biggest_increases]` while **buying** rather than selling vol
  (respects the premium-buying regime, IV 3.33 pctile `[HIST:vrp]`); width sits inside
  the ±8.5% monthly expected move so the 24 short strike is near the −1σ bound.

### Defined-risk alternative — direction-agnostic long convexity

- **Structure:** **Jun-18 25P / 29C long strangle** (own the move either way)
- **Strike(s) / expiry:** buy 25P + buy 29C, **2026-06-18**
- **Debit/credit:** ~**$1.05 debit** (25P ≈ $0.40, 29C ≈ $0.65)
- **Breakevens:** **~$23.95 / ~$30.05**
- **Max loss:** **$1.05** (total debit)
- **Why:** the earnings-scout's edge — front-end IV is **FLAT (1.037)** and June OPEX
  IV (36%) ≤ back-end `[STRUCT:front_end_iv_ratio]`, i.e. **~zero event premium** is
  priced into four China mega-cap prints while realized (33.8%) > implied (29.8%).
  Short-gamma at spot `[STRUCT:gex]` amplifies whichever way it breaks. Lean the
  strangle put-side (overweight 25P) to express the downside bias while keeping the
  upside-squeeze tail covered. (No premium *selling* — phase-5 forbids it here.)

## Macro overlay (cite phase-6)

- **Tailwinds:** May-15 Trump-Xi summit + $30B+ tariff-reduction framework
  `[MACRO:USChina_summit_2026-05-15]`; China consumer stimulus + 15th 5-Yr Plan
  (AI/digital) `[MACRO:China_policy_2026]`; cheap IV `[HIST:iv_percentile_zscore]`.
- **Headwinds:** firm/rising broad USD 119.3 `[MACRO:DTWEXBGS_2026-05-15]`; TRANSITIONAL
  US regime, 38.1% breadth `[MACRO:MarketRegime_2026-05-22]`; unresolved truce + Xi
  Taiwan warning `[MACRO:USChina_2026-05-22]`; KWEB −17% YTD laggard `[SENT:rel_performance]`.
- **Net:** **mixed, slight near-term headwind** with a real (fragile) bullish catalyst path.

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|------|-------|------------------|
| Late May–early Jun | China mega-cap earnings (PDD/Meituan/JD/NetEase) | **?** (high vol; BABA-style miss = downside) |
| Ongoing | US-China truce-extension / tariff-framework progress | + if signed / − if lapses |
| Tail | Taiwan escalation | **−** (gap risk) |
| 2026-06-18 | June OPEX (30/31 call walls) | gamma/pin mechanics |

## Post-trade monitoring checklist

- [ ] Phase-4 daily refresh: watch for **DEX→positive / GEX flip long >$28.5** (thesis flip).
- [ ] Dark-pool block `buy_ratio` daily: a flip from distribution (0.31) to **ACCUMULATION** invalidates the lean.
- [ ] Fund flows: 5-day outflow (−$281.5M) turning to **inflow** = demand returning.
- [ ] China earnings prints: a BABA-style miss **confirms** downside; a clean beat is the squeeze trigger.
- [ ] Levels: **$28.10** (stop the put-spread), **$26.88 / $26.36** (downside confirmation), **$29** (flip long).
- [ ] Broad USD (DTWEXBGS): a sharp USD reversal lower is a China/EM tailwind.

## Citations summary

1. `[FLOW:insights_deep_dive]` — net flow +$2.65M, P/C 0.25 — phase-1-flow.md §Whole-tape aggregate
2. `[DP:block_stratified]` — mega buy_ratio 0.0 / block 0.306 (distribution) — phase-2-dark-pool.md §Tier breakdown
3. `[OI:decrease_with_volume]` — Jun 31C OI −13,668 (calls written/closed) — phase-3-positioning.md §Closing
4. `[HIST:iv_percentile_zscore]` — IV 3.33 percentile (cheap) — phase-5-historical.md §IV regime
5. `[HIST:vrp]` — VRP −0.039 (premium-buying) — phase-5-historical.md §VRP
6. `[MACRO:USChina_summit_2026-05-15]` — summit + tariff framework — phase-6-macro.md §Sector overlay
7. `[AGENT:risk-monitor]` — 5/5 agents non-directional, avg conviction 2.6 — phase-8-agent-views.md
