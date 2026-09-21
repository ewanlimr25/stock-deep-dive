# Phase 9 — Trade Blueprint

**Ticker:** SHOP
**As-of date:** 2026-07-17
**PM voice:** desk PM running an institutional options-overlay book
**Spot reference:** 123.56 (phase-0.5 / DuckDB close; intraday underlying 123.5–124.1)
**Upstream phases cited:** phase-0.5 through phase-8b

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

SHOP is a crowded-long grinder pinned in a **short-gamma pocket** — dealers are net
short gamma with the largest strike a **−$12.8M GEX pole right at 123** and max-pain
magnets below spot at **117–121** `[STRUCT:gex][STRUCT:max_pain]` — while UW's composite
flags a **confirmed price-vs-flow divergence** (price +6.5% over 30d vs net-bearish flow
−$1.08M) `[INSIGHT:price_vs_flow]` and the block-tier dark pool is **74% sell**
`[DP:block_stratified]`. That sets up a **small, defined-risk tactical fade toward 117
— but only on a confirmed break of 123** — since the day itself was a
`BUSY_NAME_NORMAL_DAY` (self-pctile 32) `[CTX]` with no catalyst before the 7/24 expiry
and a **desk that split 3-2 at avg conviction 2.2** `[AGENT:desk]`. This is a scalp
against a still-bullish base, not a position short.

## Bias + conviction + horizon

- **Directional bias:** SHORT (tactical fade; plurality of phases 1–8, 3-of-5 desk)
- **Conviction (M-01 bin):** **0.55** (slight edge)
- **Time horizon:** 1-5d (into/through 2026-07-24 expiry; closed before Aug-5 earnings)
- **Why this bin:** the confluence is genuinely mixed (UW signal-confluence has SHOP
  absent both directions, conviction-matrix MIXED 8.8%) and the phase-8b debate
  **disconfirmed** the thesis (bear residual 0.65 ≥ bull 0.60), forcing a one-bin
  down-shift to the floor. (Phase-10 to confirm the band.)

## Entry zones

| Entry type | Price | Trigger condition | Source |
|---|---|---|---|
| Primary | **≤122.9** | **Confirmed break of the 123 GEX pivot** (below-123 acceptance / 15-min close) — short-gamma then presses toward 121→117 | `[STRUCT:gex]` |
| Aggressive | 124.7–125.0 | Rejection at the 125 call wall / DP cluster (fade the rally into resistance before the break) | `[DP:price_levels][OI:oi_by_strike]` |
| Fade (plan B) | 117.2 | If 117 max-pain fills and holds with block DP buy_ratio >0.55 — cover and reverse to a support-bounce lean | `[STRUCT:max_pain][DP:block_stratified]` |

## Levels to watch

| Type | Level | Source |
|---|---|---|
| Support | **117** (put wall net_oi −5,461; today's max-pain) | `[OI:oi_by_strike][STRUCT:max_pain]` |
| Support (magnet) | 121 (7/24 max-pain) · 120 (7/31 max-pain) | `[STRUCT:max_pain]` |
| Accelerant pivot | **123** (−$12.8M GEX — the trigger line) | `[STRUCT:gex]` |
| Resistance | **125 / 125.06** (call wall +4,687; heaviest 5-day DP cluster; +$4.87M GEX) | `[OI:oi_by_strike][DP:price_levels]` |
| Resistance (upper) | 130 (call wall net +7,377) | `[OI:oi_by_strike]` |
| Gamma flip | **134.98 (ZGL)** — above it dealers mean-revert; thesis dead | `[STRUCT:gex]` |

**Price-context color:** `fz` RSI/52w unavailable (partial quote), but phase-7b places
spot in the **lower third of its 52-week range** (94–182, −32% from the high) — the name
is *already well off its highs*, so downside room to a fresh low is limited and a bounce
is easy; this is color that reinforces "scalp, not swing," and never alters the size. `[HIST:52w_proximity fz]`

## Invalidation

- **Price-based:** a **daily close back above 125** (reclaims the call wall and the 123
  pivot) → short-gamma fade is dead; **hard stop 125.5**. Also: **failure to break 123
  within 2–3 sessions** = the trigger never fired → stand down (do not hold a decaying
  fade in the 116–121 stalemate).
- **Signal-based:** block-tier dark-pool **buy_ratio flips >0.55** (accumulation
  resumes) `[DP:block_stratified]`; **OR** sweep-persistence `dominant_direction` flips
  to a clean bullish read `[FLOW:sweep_persistence]`; **OR** the price-vs-flow divergence
  closes (flow turns net-bullish) `[INSIGHT:price_vs_flow]`.
- **Macro-based:** a broad **risk-ON leg** — VIX back below 15 and SPY reclaiming its
  20/50-day SMA `[MACRO:MarketRegime]` — lifts the durably-bid Tech sector and
  re-asserts the crowded long; **OR** any bullish SHOP upgrade/target-raise
  `[SENT:recommendation]`. The trade must be **flat before FOMC (7/29) and earnings
  (8/5)** regardless.

## Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** p_raw = **1.00** (bearish_flow backtest, n=**10**,
  source=backtest) → N-cap (10 ≤ n < 20 → 0.85) → **capped p = 0.85** `[HIST:signal_backtest]`.
  *Caveat: this backtest is market-wide + in-sample ("not a robust live edge," phase-5) —
  the gates below, not p, govern the real size.*
- **Kelly inputs:** entry 123.5 / target 117 / stop 125.5 → **b = 6.5/2.0 = 3.25**,
  fraction = 0.25, cap_pct = 5.
- **Raw Kelly:** (0.85×3.25 − 0.15)/3.25 = **0.804** → suggested = min(0.804×0.25×100, 5)
  = **5.0%** · **Win-rate map ceiling:** p≥0.70 → full (≤5%).
- **Risk gates (each cuts; order applied):**
  - **Fundamentals (7b): CAUTION** (rev +32% contradicts a short) → cut one step: 5% → **2.5%**.
  - **Sentiment/crowd (7c): CONFIRM** (CROWDED_LONG + low SI *supports* a fade) → no-op: **2.5%**.
  - **Correlation cluster (6/8): SHOP/PATH = 0.707** (concurrent blueprint) → cut one step: 2.5% → **1.25%**.
  - **Sector rotation (6): ADVERSE** (Tech #1 durable inflow, persistence 0.8) → cut half step (×0.75): 1.25% → **~0.94%**.
  - **Debate (8b): DISCONFIRMED** (bear 0.65 ≥ bull 0.60) → down-shift bin (→0.55) + cut one step (halve): 0.94% → **~0.47%**.
  - **Context (0.5): BUSY_NAME_NORMAL_DAY** → no top-of-band (already far below).
- **Final size:** **~0.5% of book risk** (starter/scalp — 4 of 5 gates fired).
- **Deviation reason:** none (upward deviation forbidden — multiple gates fired).

## Option structures

Front-expiry (7/24) **expected move ≈ ±6% (~$7.4)**, RV30-derived — the screener
`implied_move_perc` is unreliable `[STRUCT]`. Both structures expire **7/24, ahead of
FOMC (7/29) and earnings (8/5)** — no binary is straddled. In the **premium-selling**
regime (IV 98.5 %ile, VRP +0.31 `[HIST:vrp]`) the credit structure is the cleaner
expression; the debit spread is offered for a pure directional break.

### Directional (primary) — put debit spread

- **Structure:** SHOP **123 / 117 put debit spread** (buy 123 put, sell 117 put)
- **Strikes / expiry:** 123 / 117 · **2026-07-24**
- **Debit/credit:** ~**$2.20 debit** (est., rich front IV)
- **Breakeven:** ~120.80
- **Max loss:** $2.20/contract (= the debit); **max value $3.80** at ≤117
- **Why this structure:** strikes anchor to the 123 GEX pivot (entry trigger) and the
  117 put-wall/max-pain target `[STRUCT:gex][OI:oi_by_strike]`; a *spread* (not a naked
  long put) caps the cost of paying up for 98.5-percentile IV. Width $6 ≈ 1× the ±6%
  expected move — target inside the priced range, not a chase. Enter **only after the
  123 break**.

### Defined-risk alternative — bear call spread (premium-selling)

- **Structure:** SHOP **126 / 130 bear call spread** (sell 126 call, buy 130 call)
- **Strikes / expiry:** 126 / 130 · **2026-07-24**
- **Debit/credit:** ~**$1.10 credit**
- **Breakeven:** ~127.10
- **Max loss:** ~$2.90/contract (width 4 − credit)
- **Why this structure:** monetizes rich IV and the **125–130 call-wall / dealer-sell
  zone** `[OI:oi_by_strike][STRUCT:gex]` — profits if SHOP simply *fails to reclaim 126*,
  so it also pays in the 116–121 stalemate the debate flagged. Can be entered now
  (fades rallies into resistance) rather than waiting for the 123 break.

*Max loss on whichever structure is used must be ≤ ~0.5% of book risk.*

## Macro overlay (cite phase-6)

- **Tailwinds (for the underlying, i.e. headwinds for the short):**
  - Disinflation — headline CPI −0.42% MoM `[MACRO:CPIAUCSL_2026-06]`
  - Easing — Fed funds 3.63%, 2y falling to 4.16% `[MACRO:DGS2_2026-07-16]`
  - **Technology = #1 durable inflow sector** (+$98.6M, persistence 0.8) `[MACRO:sector_flow]`
- **Headwinds (support the short near-term):**
  - Regime TRANSITIONAL/CHOPPY, "half position sizes" `[MACRO:MarketRegime]`
  - VIX 15.6→18.8, breadth 38% bullish `[MACRO:MarketRegime]`
  - SHOP P/S ~13× vs sector 7.5× — compression risk on risk-off `[MACRO:group_valuation fz]`
- **Net:** **mixed** — medium-term tailwind vs near-term choppy; the durable sector
  inflow is the standing brake on how long the fade can be held.

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|---|---|---|
| 2026-07-29 | FOMC (no SEP) | ? (broad tech beta) — **after 7/24 expiry** |
| 2026-08-05 (BMO) | **SHOP Q2 earnings** | ? (major binary) — **be flat before this** |

## Post-trade monitoring checklist

- [ ] **123 pivot:** did it break (activate) or hold (stand down after 2–3 sessions)? `[STRUCT:gex]`
- [ ] **Block-tier DP buy_ratio** daily — a flip >0.55 = accumulation resumes, invalidation. `[DP:block_stratified]`
- [ ] **Price-vs-flow divergence** — recompute; a close of the divergence kills the edge. `[INSIGHT:price_vs_flow]`
- [ ] **125 line** — any daily close above = hard stop; **135 ZGL** = regime flip, dead. `[STRUCT:gex]`
- [ ] **SHOP/PATH combined exposure** — if PATH is also shorted, cap the pair as one name. `[MACRO:portfolio_corr]`
- [ ] **Calendar** — close/roll before FOMC 7/29 and unconditionally before earnings 8/5. `[MACRO:catalyst]`

## Citations summary

1. `[STRUCT:gex]` — dealers short gamma, **123 = −$12.8M GEX**, ZGL 134.98 — phase-4-structure.md §GEX
2. `[STRUCT:max_pain]` — near-term **max pain 117 (7/17) / 121 (7/24)** — phase-4-structure.md §Max pain
3. `[INSIGHT:price_vs_flow]` — **confirmed DIVERGENCE**, price +6.5% vs flow −$1.08M — phase-7-insights.md §Price vs flow
4. `[DP:block_stratified]` — block-tier **buy_ratio 0.257 (74% sell)** — phase-2-dark-pool.md §Tier breakdown
5. `[HIST:signal_backtest]` — bearish_flow **win_rate 1.00 (n=10, −5.22% avg)** — phase-5-historical.md §Signal backtest
6. `[MACRO:sector_flow]` — Tech **#1 inflow, persistence 0.8** (adverse) — phase-6-macro.md §Sector rotation
7. `[AGENT:desk]` — **3-of-5 SHORT, avg conviction 2.2** — phase-8-agent-views.md
8. `[DEBATE]` — **disconfirmed, bull 0.60 / bear 0.65** — phase-8b-debate.md
