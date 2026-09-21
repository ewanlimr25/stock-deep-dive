# Phase 9 — Trade Blueprint

**Ticker:** NOW (ServiceNow Inc)
**As-of date:** 2026-07-17
**PM voice:** desk PM running an institutional options-overlay book
**Spot reference:** $103.24 (phase-0 screener close)
**Upstream phases cited:** phase-0.5 through phase-8b

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

There is **no directional edge to own here into the 7/22 print**: the firing bullish
flow has a **14.3% historical win-rate (n=7, avg −7.38%)** `[HIST:signal_backtest]`,
the tape is **delta-neutral (−$89k)** with the largest prints being **Jan-2027 puts
sold at the bid** `[FLOW:greek_screener]` `[FLOW:top_premium_trades]`, and UW's own
composite reads **COVERED_CALL — "dark pool buying + call selling, capping upside"**
`[INSIGHT:conviction_matrix]`. What IS real is a **short-vol edge** (IV percentile
98.5, VRP +18.9 `[HIST:vrp]`) into an event with an **~±11% implied move**
`[STRUCT:iv_term_structure]` — but with **decelerating earnings into a miss** (+13.4→
−0.3%) `[FUND:earnings_surprise]`, an **89%-Buy crowded consensus** on a name **−51%
off its high** `[SENT:recommendation]`, and a **debate that disconfirmed the range
thesis (bear 0.70 ≥ bull 0.60)** `[DEBATE:disconfirmed]`, the honest call is
**stand aside on direction; if engaging, a minimal defined-risk structure that sells
the overpriced tails while OWNING the cheap downside.**

## Bias + conviction + horizon

- **Directional bias:** **NEUTRAL / RANGE** (with a downside tilt; **zero** phase-8
  agents were bullish, plurality NEUTRAL, 1 SHORT).
- **Conviction (M-01 bin):** **0.55** (floor — slight edge is short-vol only; the
  debate down-shift and four fired gates pin it here).
- **Time horizon:** **1-4w** (8/21 expiry — captures the 7/22 event AND the
  post-earnings IV crush; avoids naked 0DTE/event-week gamma).
- **Why this bin:** phase-10 will score low confluence — the flow is mixed on a
  BUSY_NAME_NORMAL_DAY `[CTX:unusual_verdict]`, NOW is absent from both
  bullish and bearish signal-confluence `[INSIGHT:signal_confluence]`, and the debate
  disconfirmed the thesis; 0.55 is the correct floor.

## Entry zones

| Entry type | Price | Trigger condition | Source |
|---|---|---|---|
| Primary | **$104–105** | Sell into a tag of the **negative-gamma pocket / max-pain** — vol is richest and upside is capped by the $110 wall | `[STRUCT:gex per_strike]` `[STRUCT:max_pain]` |
| Aggressive | **$110–111** | Rejection at the **$110 call wall** (heaviest near-term, net +12,587) → put-side / short-vol entry on a failed rally | `[OI:oi_by_strike dte<=30]` |
| Fade (plan B) | **$95–96** | If NOW breaks the $100 pin and tags **$95 put support**, fade the flush (oversold −51%, insiders bought dips) with a small long — counter to the downside tilt | `[OI:oi_by_strike]` `[FUND:insider_MSPR]` |

## Levels to watch

| Type | Level | Source |
|---|---|---|
| Support | **$102.90** (DP cluster) → **$101.21** (ZGL) → **$100** (put wall) → **$95** | `[DP:price_levels]` `[STRUCT:gex]` `[OI:oi_by_strike]` |
| Resistance | **$104–105** (neg-gamma pocket) → **$110** (call wall) → **$120** | `[STRUCT:gex per_strike]` `[OI:oi_by_strike dte<=30]` |
| Gamma flip (ZGL) | **$101.21** — below it, dealers flip short-gamma and drawdowns accelerate | `[STRUCT:gex]` |
| Largest pin | **$104** (7/24 max-pain ≈ spot); **8/21 monthly** is the OI anchor (17.4%) | `[STRUCT:max_pain]` `[OI:term_structure]` |

Price-context color: `fz` RSI / 52-week proximity **unavailable this run** (degraded
snapshot); the Finnhub read stands — NOW is **~51% below its 52w high ($210)**, lower
third of range `[FUND:52wHigh]` → not a breakout, a wounded name; prefer the fade
entry over chasing strength. (Narrative only; does not alter size.)

## Invalidation

- **Price-based:** two daily closes **above $105** (breaks the range up through the
  negative-gamma pocket toward $110 — kills the short-vol/neutral thesis) OR two daily
  closes **below $100** (loses the positive-GEX pin; short-gamma below $101.21
  accelerates down — the condor's downside is threatened, the put spread confirmed).
- **Signal-based:** **GEX flips FULLY_NEGATIVE on the phase-4 daily refresh** (as it
  did at the June $92 lows `[HIST:gex_time_series]`) — dealer hedging stops damping and
  starts amplifying; OR institutional-accumulation reverses to distribution
  `[INSIGHT:institutional_accumulation]`.
- **Macro-based:** the **2026-07-22 earnings print itself** is the binary — a
  beat-and-raise gap **>+11%** invalidates the downside tilt (squeeze up to $110+); a
  guide-down gap **>−11%** confirms it but may exceed the condor's $87.46 breakeven.
  Secondary: a risk-off regime flip on `uw risk market-regime` `[MACRO:MarketRegime]`.

## Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** p_raw = **0.143** (bullish_flow, **n=7**, source=backtest)
  → N-cap for n<10 is 0.75 (non-binding) → capped **p = 0.143** `[HIST:signal_backtest]`.
- **Kelly inputs:** b = **1.58** (put debit spread reward/risk = 6.12/3.88);
  fraction = 0.25; cap_pct = 5.
- **Raw Kelly:** (0.143×1.58 − 0.857)/1.58 = **−0.40 → NEGATIVE**. **Win-rate map:
  p 0.143 < 0.50 → starter/skip; SHORT-side floor forces directional to starter/skip.**
  The bullish signal is edge-negative; a directional LONG is **skipped**. No validated
  positive-edge `p` exists for the bearish/neutral expression (bearish_flow 100% is
  n=10 and NOT the firing signal — deliberately NOT sized on), so the trade is capped
  at **STARTER** and gated down.
- **Risk gates (all five, in order):**
  - Fundamentals (7b): **CAUTION** (decelerating earnings) → cut one step.
  - Sentiment/crowd (7c): **CAUTION + CROWDED_LONG** (89% Buy on −51% name) → cut one step.
  - Correlation cluster (6): **CLUSTER — NOW/PATH 0.798** → cut one step (size NOW+PATH
    as ONE position).
  - Sector rotation (6): **NEUTRAL** (tech inflow but NOW lagging; not adverse-against
    direction) → no cut.
  - Debate (8b): **bull 0.60 vs bear 0.70 → disconfirmed=true** → down-shift bin +
    cut one step.
  - Context: **BUSY_NAME_NORMAL_DAY** `[CTX:unusual_verdict]` → no top-of-band.
- **Final size:** **0.0% — WATCH-ONLY / stand aside.** Raw Kelly is negative
  (edge-negative bullish signal), the debate disconfirmed the thesis, and four gates
  fired (7b, 7c, correlation, debate) on a BUSY_NAME_NORMAL_DAY — there is no
  size to put on. The option structures below are **illustrative only**; if a desk
  overrides to engage the short-vol edge, cap the defined-risk structure's max-loss at
  **≤0.5% of book risk** (starter) and treat NOW+PATH as one position.
- **Deviation reason:** none (final < suggested — always permitted; upward deviation
  forbidden here anyway, gates fired).

## Option structures

### Directional (primary) — bearish, leans into the downside asymmetry

- **Structure:** **8/21 100/90 put debit spread** (buy 100P, sell 90P).
- **Strike(s) / expiry:** 100/90 puts, **2026-08-21** (spans 7/22, captures follow-through).
- **Debit/credit:** **−$3.88 debit** (BS @ IV 72%; verify live).
- **Breakeven:** **$96.12**; max value $10 (< $90), **max profit $6.12**.
- **Max loss:** **$3.88** (the debit).
- **Why this structure:** owns the cheap **COMPLACENT downside skew** (`[STRUCT:term_skew]`
  — put25Δ ≈ call25Δ) that the market isn't pricing for a **decelerating-earnings miss**
  `[FUND:earnings_surprise]`; the spread caps vega so the post-earnings **IV crush**
  doesn't sink it, and a downgrade-cascade gap prints it deep ITM. Sized at ≤0.5% book.

### Defined-risk alternative — short-vol / range (harvest the crush)

- **Structure:** **8/21 iron condor** — short 90P / short 115C, long 85P / long 120C.
- **Strike(s) / expiry:** 85/90 put wing + 115/120 call wing, **2026-08-21**.
- **Debit/credit:** **+$2.54 credit** (BS @ IV 72%).
- **Breakeven:** **$87.46 / $117.54** (both **outside** the ~±11% implied move —
  this is the VRP edge: options overpricing realized `[HIST:vrp]`).
- **Max loss:** **$2.46** (width $5 − credit $2.54).
- **Why:** short strikes sit beyond the priced ±11% earnings move, so it monetizes the
  **IV rank 98.5 crush** post-7/22 `[HIST:iv_percentile_zscore]` with defined risk —
  exactly the **"iron condors in range, defined-risk, half size"** the macro regime
  prescribes `[MACRO:MarketRegime_2026-07-17]`. Loses only on a >±13% gap.

## Macro overlay (cite phase-6)

- **Tailwinds:** Technology sector **INFLOW +$1.17B, persistence 0.80**
  `[MACRO:sector_flow_persistence]` (sector-level only — NOT reaching NOW);
  Core CPI easing to **2.5%** `[MACRO:CPILFESL_2026-06]`.
- **Headwinds:** Regime **TRANSITIONAL/CHOPPY, "half size, defined-risk"**
  `[MACRO:MarketRegime_2026-07-17]`; breadth **bearish 38.4%**; **10y 4.57%** pressuring
  the 60× multiple `[MACRO:DGS10_2026-07-16]`; **NOW/PATH 0.798 cluster**
  `[MACRO:portfolio_correlation]`.
- **Net:** **net headwind** for a directional long; supportive of a defined-risk
  short-vol posture.

## Catalyst calendar (next 30d)

Front-expiry (7/24) implied move **~±11% / ~$11.4** — every structure is sized to this.

| Date | Event | Impact direction |
|---|---|---|
| **2026-07-22** | **ServiceNow Q2 FY26 earnings (AMC)** — the binary | **? (±11% priced; downside tail under-hedged)** |
| ~2026-07-28 | FOMC (approx) | ? (post-earnings, second-order) |
| ~2026-08-12 | July CPI (approx) | ? (market-level) |

## Post-trade monitoring checklist

- [ ] **7/22 AMC earnings** — the trade IS this event; have the condor/put-spread on
      BEFORE the close 7/22 or not at all (do not chase the gap).
- [ ] **GEX regime on daily refresh** — a flip to FULLY_NEGATIVE `[HIST:gex_time_series]`
      = accelerant; tighten or exit the condor's downside.
- [ ] **NOW/PATH combined exposure** — if PATH is held, treat as one position; cut a
      leg before the print `[MACRO:portfolio_correlation]`.
- [ ] **Analyst revisions post-print** — a downgrade wave off the 89%-Buy wall
      `[SENT:recommendation]` confirms the put spread; watch the tape/DP for
      distribution.
- [ ] **IV rank post-earnings** — the condor's edge is the crush; if IV rank stays
      elevated (no crush), the short-vol thesis failed — close.

## Citations summary (≥3 distinct upstream datapoints)

1. `[HIST:signal_backtest]` bullish_flow win-rate **0.143 (n=7, avg −7.38%)** — phase-5 §Signal backtest.
2. `[STRUCT:iv_term_structure]` / `[HIST:vrp]` earnings implied **~±11%**, VRP **+18.9**, IV pctile **98.5** — phase-4/5.
3. `[INSIGHT:conviction_matrix]` **COVERED_CALL** "DP buying + call selling, capping upside" — phase-7.
4. `[SENT:recommendation]` **89% Buy (48/54)** on a name **−51% off high** — phase-7c/7b.
5. `[DEBATE:disconfirmed]` bull 0.60 vs **bear 0.70 → disconfirmed** — phase-8b.
6. `[MACRO:portfolio_correlation]` **NOW/PATH 0.798 cluster** — phase-6.
