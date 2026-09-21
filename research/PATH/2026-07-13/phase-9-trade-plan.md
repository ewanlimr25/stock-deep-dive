# Phase 9 — Trade Blueprint

**Ticker:** PATH (UiPath Inc.)
**As-of date:** 2026-07-13
**PM voice:** desk PM running an institutional book
**Spot reference:** $11.87 (phase-4 GEX / phase-7 institutional-accumulation VWAP $11.93)
**Upstream phases cited:** phase-0.5 through phase-8b

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

An unattributed institution lifted **54.6M shares / $644M at the ask, buy_ratio 1.000,
zero sell — the largest darkpool print in PATH's history by ~15×** `[DP:block_stratified]`
on 2026-07-09, and kept buying into the as-of tape (large tier 61.2% buy, $337M)
`[DP:block_stratified]`, building a **$678.8M institutional shelf at $11.80**
`[DP:price_levels]` under a name that is **28–32% of float short** `[SENT:short_float]` —
a squeeze-loaded floor. But the print **moved price zero over 30 days** `[HIST:trend]`
while **insiders sold 9.6M shares** `[FUND:insider_MSPR]`, the desk split **2 LONG / 2
RANGE, 0 SHORT** `[AGENT:desk]`, and the bear disconfirmation held `[DEBATE:disconfirmed]`.
Net: a **low-conviction, starter-size long biased off the $11.80 shelf**, expressed
defined-risk, that nobody should short and nobody should press until the block attributes
or price clears $13.

## Bias + conviction + horizon

- **Directional bias:** LONG (lean) — plurality of phases 1–8 (2 LONG / 2 RANGE / 0 SHORT; darkpool accumulation is the dominant signal). Not a press; a toe-in against a defined floor.
- **Conviction (M-01 bin):** **0.55** (slight edge).
- **Time horizon:** 1-4w.
- **Why this bin:** the raw accumulation + squeeze topology would merit ~0.65, but the phase-8b bear disconfirmation (bear_residual 0.65 ≥ bull_residual 0.65) down-shifts one bin to **0.55**, matching the low confluence band (BUSY_NAME_NORMAL_DAY, two CAUTION gates, n=0 backtest, inert price).

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| Primary | $11.80–$11.90 | Hold of the $11.80 darkpool shelf with continued large-tier buy_ratio > 0.55 | `[DP:price_levels]` |
| Aggressive | $11.60–$11.70 | Dip toward the shelf that does NOT close below $11.60, with DP buy continuation | `[DP:block_stratified]` |
| Fade (plan B) | $12.90–$13.00 | Rejection at the $13 gamma wall — counter-trade the box top / take profit / avoid new longs | `[STRUCT:gex]` |

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Support | **$11.80** (institutional shelf) | `[DP:price_levels]` |
| Support (secondary) | $10 put wall (−15.7%) | `[OI:oi_by_strike]` |
| Resistance | **$13.00** (gamma wall + call wall + covered-call cap) | `[STRUCT:gex]` / `[OI:oi_by_strike]` |
| Gamma flip (ZGL) | $5.70 (far below — firmly long-gamma) | `[STRUCT:gex]` |
| Largest pin | $11.00 (Jul-17 max-pain) → $12 (Jul-31) | `[STRUCT:max_pain]` |

## Invalidation

- **Price-based:** a **daily close below $11.60** (the $11.80 shelf fails). With **32% short interest and no OI support until $9–$10** `[OI:oi_by_strike]`, a shelf break is a short-cascade tail, not a slow bleed — exit, do not average.
- **Signal-based:** the darkpool bid **withdraws** — a subsequent session prints large-tier buy_ratio < 0.45 (net selling) `[DP:block_stratified]` — OR the 07-09 block **attributes as supply**: a secondary-offering / 13D-distribution filing confirms the print was a holder distributing, not accumulating (`[DEBATE:strongest_bear_point]` — the block was exit liquidity).
- **Macro-based:** a hawkish FOMC / 10y spike above ~4.8% compressing software multiples `[MACRO:DGS10]`, or breadth deteriorating below the already-weak 33.8% into a risk-off regime `[MACRO:MarketRegime_2026-07-13]`.

## Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** p_raw = **null** (signal-backtest `dark_pool_accumulation` returned n=0, source=null `[HIST:signal_backtest]`) → **fall back to conviction bin 0.55**, itself capped at 0.65. **p = 0.55.**
- **Kelly inputs:** b = |13.00 − 11.85| / |11.85 − 11.50| = 1.15 / 0.35 = **3.29**; fraction = 0.25; cap_pct = 5.
- **Raw Kelly:** (0.55 × 3.29 − 0.45) / 3.29 = **0.413** → suggested = min(0.413 × 0.25 × 100, 5) = **5.0%**. **Win-rate map ceiling:** p 0.55 ∈ [0.50, 0.70] → **half** (≤ 2.5%). Take the smaller → **2.5% pre-gate.**
- **Risk gates:**
  - Fundamentals (phase-7b): **CAUTION** (insider selling contradicts flow) → **cut one step: half → starter (~1.25%)**.
  - Sentiment/crowd (phase-7c): **CAUTION**, crowd_state CROWDED_SHORT (lukewarm analyst consensus, PT $12) → **cut one step (~0.6%)**. (High SI is squeeze-supportive but cannot add.)
  - Correlation cluster (phase-6): **none** (PATH only blueprint for the date) → no-op.
  - Sector rotation (phase-6): **aligned** (tech persistence score 1) → no-op (not adverse).
  - Debate (phase-8b): bull_residual **0.65** vs bear_residual **0.65** → **disconfirmed = true → down-shift bin (done: 0.65→0.55) AND cut one step**.
- **Context modifier (phase-0.5):** `unusual_verdict = BUSY_NAME_NORMAL_DAY` → **do not size at top of band.**
- **Final size:** **1.0% of book risk** (starter/toe-in). Three gates fired on a 2.5% half-ceiling; the honest range is 0.5–1.0% or watch-only until the block attributes. **No upward deviation (forbidden — gates fired).**

## Option structures

Front-expiry implied move **±5.3% / ≈±$0.63** `[CTX:implied_move]`. Both structures use
**Aug-21 (39 DTE)** — past Jul-17 OPEX, clean of the 2026-09-03 earnings binary, matching
the 1-4w horizon. Max-loss per structure is small, so 1.0% book risk = a modest number of spreads.

### Directional (primary)

- **Structure:** $12 / $13 **call debit spread** (bullish, defined risk)
- **Strike(s) / expiry:** Buy $12 call / Sell $13 call, **2026-08-21**
- **Debit/credit:** ~**$0.35 debit** (buy $12 ≈ $1.00, sell $13 ≈ $0.65) `[prices: local Aug-21 chain]`
- **Breakeven:** **$12.35**
- **Max loss:** **$0.35** (the debit); max profit $0.65 (2:1 R/R) at/above $13
- **Why this structure:** VRP is **premium-selling (+0.084, IV > RV)** `[HIST:vrp]`, so a *spread* (sell the $13 wall to fund the $12 long) beats a naked call that fights carry; the short $13 leg sits exactly on the gamma wall / covered-call cap `[STRUCT:gex]` where upside stalls anyway. Targets the box-top squeeze, not open-ended upside.

### Defined-risk alternative

- **Structure:** $11 / $10 **bull put credit spread** ("get paid to defend the shelf")
- **Strike(s) / expiry:** Sell $11 put / Buy $10 put, **2026-08-21**
- **Debit/credit:** ~**$0.31 credit** (sell $11 ≈ $0.57, buy $10 ≈ $0.26) `[prices: local Aug-21 chain]`
- **Breakeven:** **$10.69**
- **Max loss:** **$0.69** ($1.00 width − $0.31 credit)
- **Why:** monetizes the premium-selling regime `[HIST:vrp]` + the $11.80 accumulation floor `[DP:price_levels]` + long-gamma range `[STRUCT:gex]`; the short $11 strike sits above the $10 put wall `[OI:oi_by_strike]`, the long $10 caps the short-cascade tail. Highest-probability expression if the range simply holds. **Preferred if you want a single position** — it aligns with the premium-selling VRP and does not need a breakout.

## Macro overlay (cite phase-6)

- **Tailwinds:** Fed easing, funds 3.62% — duration support for software `[MACRO:DFF]`; Tech sector-flow-persistence INFLOW score 1 `[MACRO:SectorPersistence_2026-07-13]`; Maestro Case AI catalyst, +3.33% on 07-09 `[MACRO:UiPath_2026-07-09]`; no offering/13D filed against the block `[MACRO:UiPath_2026-07-09]`.
- **Headwinds:** Regime TRANSITIONAL, breadth 33.8% bullish, "half position sizes" `[MACRO:MarketRegime_2026-07-13]`; HOLD-heavy consensus, UBS PT cut to $12 `[SENT:recommendation]`; today's defensive rotation (Tech −$516M) `[MACRO:MarketRegime_2026-07-13]`.
- **Net:** mixed / mild-tailwind — helps a hold, does not force a breakout.

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|------|-------|------------------|
| ~mid-late Jul 2026 | CPI (June) print | ? (market-level, indirect) |
| ~late Jul 2026 | FOMC (approx.) | ? (easing-path signal, indirect) |
| (passed 07-10) | Short-seller report in focus | watch for follow-on `[SENT:news]` |
| **2026-09-03** | **PATH earnings — OUTSIDE 30d** | binary; Aug-21 structures avoid it |

**No PATH binary inside the horizon** — this is a flow/shelf swing, not an earnings play.

## Post-trade monitoring checklist

- [ ] **Daily: re-pull `uw dark-pool block-stratified --symbol PATH`** — is the bid still there (buy_ratio > 0.55) or did it withdraw (< 0.45 = invalidation)?
- [ ] **Watch SEC filings / news for block attribution** — a secondary/13D confirming distribution flips the thesis (strongest bear point).
- [ ] **$11.80 shelf integrity** — any daily close below $11.60 = exit (short-cascade tail with 32% SI).
- [ ] **$13 gamma wall** — a clean break above $13 on volume/sweep upgrades the long (take-profit on the call spread; the RANGE case breaks bullish).
- [ ] **IV / vanna** — if IV falls, the dealer DEX bid flips to selling `[STRUCT:vanna_charm]`; watch for the mechanical unwind pressuring the shelf.
- [ ] **Insider filings** — continued heavy selling (MSPR) deepens the fundamental CAUTION.

## Citations summary

1. `[DP:block_stratified]` — 07-09 mega tier **buy_ratio 1.000, 54.6M sh, $644.2M, zero sell** — phase-2-dark-pool.md §Tier breakdown.
2. `[HIST:trend]` — price **$11.72 → $11.85 over 30d** (block moved price zero) — phase-5-historical.md §Multi-day trend.
3. `[SENT:short_float]` — **~28–32% of float short, ~5 days to cover** — phase-7c-sentiment.md §Short interest.
4. `[DEBATE:disconfirmed]` — bull_residual 0.65 / bear_residual 0.65 → disconfirmed true — phase-8b-debate.md §Disconfirmation verdict.
5. `[STRUCT:gex]` — gamma wall **$13**, ZGL $5.70, long-gamma — phase-4-structure.md §GEX.
