# Phase 9 — Trade Blueprint

**Ticker:** NVDA
**As-of date:** 2026-05-27
**PM voice:** desk PM running an institutional options-overlay book
**Spot reference:** $212.60 (phase-2 close / phase-5 trend)
**Upstream phases cited:** phase-0.5 through phase-8b

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

NVDA is in a **dealer-defined, institution-confirmed capped-upside regime**: the
conviction matrix labels it `COVERED_CALL` ("yield enhancement, capping upside")
[INSIGHT:conviction_matrix], a 5-session bearish sweep campaign ($4.55B, 5/5
consistency) is hitting calls on the bid [FLOW:sweep_persistence], and a
long-gamma GEX wall at $215/$217.5/$220 (+$146M combined) reinforced by fresh
call-writing OI caps the upside [STRUCT:gex]. Macro is a mild headwind —
Technology is today's single largest sector directional outflow at −$433.5M
[MACRO:sector_rotation_2026-05-27] and the regime is "TRANSITIONAL, half size"
[MACRO:MarketRegime_2026-05-27] — and the desk votes 3-of-4 RANGE. **But the
empirical edge is thin** (the `bearish_flow` signal wins only 37.5% historically
[HIST:signal_backtest]) and fundamentals are pristine (PEG 0.39, +43.8% analyst
target [FUND:peg fz][SENT:recom fz]), so this is a *small, defined-risk fade of
strength into the $215–$220 ceiling*, not an outright short.

## Bias + conviction + horizon

- **Directional bias:** **RANGE** (capped-upside with a bearish tilt — fade rips,
  do not press shorts)
- **Conviction (M-01 bin):** **0.65**
- **Time horizon:** 1–4 weeks
- **Why this bin** (phase-10 confluence): estimated confluence ≈ 64 (50–64 band →
  0.65). Moderate edge with real disconfirming evidence — the 37.5% backtest
  [HIST:signal_backtest] and bullish fundamentals [FUND:peg fz] are genuine
  headwinds against a clean directional read, offset by tight flow+structure
  confluence (phases 1/3/4).

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| Primary | ~$215 | Tag of the GEX/DP resistance shelf with rejection (fade the rip) | [STRUCT:gex] / [DP:price_levels] |
| Aggressive | $212.50 | Clean break below the $212.5 gamma pivot (−$85.7M GEX) with no reclaim | [STRUCT:today_gamma_flip] |
| Fade (plan B, counter-trade) | $220.50+ | Sustained close above the $220 wall — flip long to the +43.8% analyst target | [STRUCT:gex] / [SENT:recom fz] |

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Support | $207.50 (GEX acceleration) → $200 (put-hedge floor, OI 50,463) | [STRUCT:gex] / [OI:biggest_increases] |
| Pivot / gamma flip (0DTE) | **$212.50** (−$85.7M GEX) | [STRUCT:today_gamma_flip] |
| Resistance | **$215 / $217.5 / $220** (GEX walls +$146M) | [STRUCT:gex] |
| Largest pin | **$220** (pin_risk OI 81,598, 3.46% above spot) | [OI:pin_risk] |
| 45D ZGL (structural floor) | $138.94 (far below — long-gamma dip-buying caps downside) | [STRUCT:gex] |

**Price-context color (advisory):** NVDA RSI 51 (neutral), −10.1% from the 52-week
high of $236.54, still above SMA50/200 [HIST:rsi fz][HIST:52w_proximity fz] — the
pullback is mid-range, not oversold; there's room to drift to $207.5 without
hitting a technical floor, but also no capitulation to fade. (Narrative only —
not in the Kelly `p`.)

## Invalidation

- **Price-based:** **Two daily closes above $220.50** (above the $220 GEX wall +
  pin). This is the cleanest break — it flips the dealer ceiling into support and
  the vanna mechanics into a buy.
- **Signal-based:** Vanna flips positive on IV expansion (dealers shift from
  selling to buying) on phase-4 daily refresh, OR `conviction_matrix` flips from
  `COVERED_CALL` to `DIRECTIONAL_LONG` [INSIGHT:conviction_matrix], OR cumulative
  premium flow turns net-bullish 3 consecutive sessions [HIST:cumulative_premium_flow].
- **Macro-based:** A dovish / risk-on surprise at **May CPI (~2026-06-11)** or
  **FOMC (~2026-06-17)** that ignites a tech-multiple re-rate, OR UW regime flips
  from TRANSITIONAL to RISK-ON [MACRO:MarketRegime_2026-05-27]. This is the
  phase-8b `strongest_bear_point` — a vol re-pricing gaps NVDA *up* through the
  short-call zone.

**Exit on invalidation:** **Hard stop** on the directional put debit spread (close
100% on two closes > $220.50, or sooner if max-loss debit is at risk). The
defined-risk iron condor: **roll or close the tested side** if either wing is
breached.

## Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** `p_raw = 0.375` (n=8, source=backtest) → N-cap (n<10 →
  0.75) → **capped p = 0.375** [HIST:signal_backtest]. (No fallback — backtest
  data exists.)
- **Kelly inputs:** b = 1.94 (put debit spread: max-profit $6.60 / max-loss $3.40),
  fraction = 0.25, cap_pct = 5.
- **Raw Kelly:** (0.375 × 1.94 − 0.625) / 1.94 = **0.053** → suggested = 0.053 ×
  0.25 × 100 = **1.32%**. **Win-rate map ceiling: p < 0.50 → STARTER / skip**
  (SHORT-side floor enforced — a 37.5% signal is a starter at most).
- **Risk gates:**
  - **Fundamentals (phase-7b): `CAUTION`** (fundamental_signal BULLISH, 1
    contradiction) → **cut one size step** (the directional bearish read is cut;
    pristine business means the flow is yield-enhancement, not deterioration).
  - **Sentiment / crowd (phase-7c): `CONFIRM` / BALANCED** → no-op (no crowd to
    fade, SI 1.22% so no squeeze risk either way).
  - **Correlation cluster (phase-6): none** — NVDA is the only blueprint for
    2026-05-27, no concurrent position to cluster against → no-op.
  - **Sector rotation (phase-6): aligned** — Tech −$433.5M outflow is *with* the
    bearish tilt, not against it → no cut.
  - **Debate (phase-8b): bull_residual 0.75 vs bear_residual 0.65 →
    disconfirmed = false** → no-op.
- **Context modifier (phase-0.5): `BUSY_NAME_NORMAL_DAY`** → do not size at the top
  of the band (the magnitude is normal for this name).
- **Final size: 0.75% of book risk (STARTER).** Sized *below* the 1.32% Kelly
  suggestion because (a) p < 0.50 forces the SHORT-side floor to starter, (b)
  phase-7b CAUTION cuts a step, and (c) phase-0.5 BUSY_NAME caps off top-of-band.
- **Deviation reason:** none (sizing *down* from suggested — always permitted; an
  upward deviation would be forbidden here because a gate fired).

## Option structures

### Directional (primary) — bearish, defined-risk, debit (cheap-IV friendly)

- **Structure:** Put debit spread (bear put spread)
- **Strikes / expiry:** **Buy $210 put / Sell $200 put, 2026-06-18 (22 DTE)**
- **Debit/credit:** ~$3.40 debit (illustrative; IV30 ~40%, [HIST:vrp] VRP −0.86%
  so debit > credit is the right side — buy cheap premium)
- **Breakeven:** ~$206.60
- **Max loss:** $3.40 (the debit) per spread
- **Max profit:** $6.60 (if NVDA ≤ $200 at expiry — the put-hedge floor)
- **Why this structure:** IV is in the bottom quartile (pctile 25
  [HIST:iv_percentile_zscore]) so I want to *own* gamma cheaply, not sell it; the
  $200 short leg sits exactly on the phase-3 put-buildup floor (P200 OI 50,463
  [OI:biggest_increases]) and below the $207.5 GEX acceleration zone. **Sized to
  the expected move:** front-expiry implied move is ±1.94% / $4.12
  [CTX:implied_move_pct]; the $210→$200 target ($12.6 below spot, ~3× the
  single-period priced move) is reachable on the 1–4w horizon but rich for one
  session — hence the spread (not a naked put) and starter size. The expiry
  straddles CPI (6/11) + FOMC (6/17): a single-catalyst gap *up* of expected-move
  magnitude only loses the $3.40 debit (defined risk), so the catalyst straddle is
  acceptable for this structure.

### Defined-risk alternative — pure RANGE harvest

- **Structure:** Iron condor (sell the range, defined risk both sides)
- **Strikes / expiry:** **Sell $207.5 put / Buy $202.5 put** + **Sell $217.5 call /
  Buy $222.5 call**, 2026-06-12 (16 DTE — before CPI/FOMC vol risk crests)
- **Debit/credit:** ~$1.60 net credit (illustrative)
- **Breakevens:** ~$205.90 and ~$219.10
- **Max loss:** $3.40 (5-wide wing − $1.60 credit) per condor
- **Why:** Directly monetises the phase-8 RANGE plurality and the dealer ceiling
  ($217.5 short call sits above the $215/$217.5 GEX wall) + the $207.5 GEX support
  (short put). The 6/12 expiry deliberately closes *before* the FOMC (6/17) vol
  re-pricing risk the debate flagged. Thinner credit because IV is cheap — that is
  the cost of the cleaner range definition.

## Macro overlay (cite phase-6)

- **Tailwinds (for the underlying, against the trade):**
  - Fed funds 3.62%, cut from cycle peak [MACRO:DFF_2026-05-26 FRED] — structural
    support for long-duration tech multiples.
  - 2s10s +0.49% un-inverted, no recession signal [MACRO:DGS10_2026-05-26 FRED].
  - SPY uptrend +4.93% 30d, −0.22% from 90d high [MACRO:MarketRegime_2026-05-27].
- **Headwinds (for the underlying, with the trade):**
  - Technology −$433.5M largest sector directional outflow today
    [MACRO:sector_rotation_2026-05-27].
  - Breadth only 37.1% bullish — narrow leadership [MACRO:MarketRegime_2026-05-27].
  - CPI still +3.78% YoY (sticky → Fed pause) [MACRO:CPIAUCSL_2026-04 FRED];
    10y 4.50% elevated [MACRO:DGS10_2026-05-26 FRED].
- **Net:** **mixed-to-mild-headwind.** The macro is supportive of the *business*
  (rates, no recession) but the *flow* (sector outflow, weak breadth) aligns with
  the near-term capped/bearish tilt. This tension is exactly why the trade is
  small and defined-risk.

## Catalyst calendar (next 30d)

Front-expiry implied move: **±1.94% / $4.12** [CTX:implied_move_pct].

| Date | Event | Impact direction | vs ±1.94% |
|------|-------|------------------|-----------|
| 2026-05-29 | Weekly OPEX (pin $220) | $220 pin gravity | inside |
| ~2026-06-06 | May Nonfarm Payrolls | ? (broad) | typically inside |
| ~2026-06-11 | May CPI release | ? (tech-multiple sensitive — key) | could exceed if surprise |
| ~2026-06-17 | FOMC + dot plot | ? (rate path) | typically inside on a pause |
| 2026-08-26 | NVDA earnings | + binary (OUTSIDE 30d, not traded here) | n/a |

## Post-trade monitoring checklist

- [ ] Re-run `uw options-structure gex` + `vanna-charm` daily — exit if vanna
      flips positive on IV expansion (the regime-flip invalidation).
- [ ] Re-run `uw hot-chains sweep-persistence --symbol NVDA` daily — thesis
      weakens if `dominant_direction` flips to bullish or consistency_score drops.
- [ ] Watch the $212.50 gamma pivot and $220 wall — two closes > $220.50 = hard
      stop on the put spread; clean break < $212.5 = add to the aggressive entry.
- [ ] Track Tech sector flow (`uw options-flow sector-flow` directional read) —
      a reversal of the −$433.5M outflow removes the macro tailwind for the fade.
- [ ] Mark CPI (6/11) and FOMC (6/17) — close/roll the iron condor before FOMC;
      the put debit spread's defined risk survives the catalyst but cut if vol
      re-prices the chain higher (everyone is short premium — phase-7c).

## Citations summary

1. `[INSIGHT:conviction_matrix]` — scenario **COVERED_CALL**, "yield enhancement,
   capping upside" (phase-7-insights.md §Conviction matrix).
2. `[FLOW:sweep_persistence]` — `dominant_direction=bearish`, consistency_score 1,
   5/5 sessions, $4.55B (phase-1-flow.md §Key signals).
3. `[STRUCT:gex]` — long-gamma walls $215/$217.5/$220 = +$146M combined; K212.5 =
   −$85.7M flip; ZGL $138.94 (phase-4-structure.md §GEX).
4. `[HIST:signal_backtest]` — `bearish_flow` win_rate 0.375 (n=8) (phase-5 §Signal
   backtest) — the Kelly `p`.
5. `[MACRO:sector_rotation_2026-05-27]` — Technology −$433.5M, largest sector
   outflow (phase-6-macro.md §Market regime).
