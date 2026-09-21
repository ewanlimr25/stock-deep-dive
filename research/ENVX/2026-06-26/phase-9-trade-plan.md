# Phase 9 — Trade Blueprint

**Ticker:** ENVX
**As-of date:** 2026-06-26
**PM voice:** desk PM running an institutional book
**Spot reference:** $5.95 (phase-0 `fz` close; deep-dive underlying $5.88)
**Upstream phases cited:** phase-0.5 through phase-8b

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

A single ask-side campaign bought **$871,964 of $6-strike October calls (6,738 ct, 84% ask,
delta ~0.6)** `[FLOW:sweeps]` into a **26%-short-float, hard-to-borrow, actively-covering name**
`[SENT:short_float]` — genuine latent squeeze fuel — but the empirical edge is **negative**:
the matching `bullish_flow` backtest wins **20% (n=5)** `[HIST:signal_backtest]`, dealers are
**long-gamma for 30/30 sessions with July max-pain pinned at $6.00** `[STRUCT:gex, max_pain]`,
and the **desk went 0-for-4 directional** `[AGENT:phase-8]` while the bull/bear debate was
**disconfirmed (bear 0.75 ≥ bull 0.55)** `[DEBATE:residuals]`. **This is a watch, not a trade**:
the flow is real but counter-trend and pinned, with no catalyst until ~Aug-12 earnings — so the
PM passes on directional risk and holds a token, defined-risk squeeze option only as a carry.

## Bias + conviction + horizon

- **Directional bias:** RANGE (phase-8 plurality 3 RANGE / 1 NEUTRAL / 0 directional; structure pins $5.50↔$6.33)
- **Conviction (M-01 bin):** **0.55** (slight)
- **Time horizon:** 1-4w (range), with a separate ~1-3m option leg dated to the Aug-12 catalyst
- **Why this bin:** signals are mixed-leaning-negative for the long and the **debate disconfirmed
  the directional thesis**, forcing a one-bin down-shift; phase-10 confluence is expected mid-band
  (~mixed). Even the range read is only "slight" because the latent 26% squeeze + cheap VRP can
  break the range violently. (See `## Conviction note`.)

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| Primary | $5.95 | Hold of the $5.95 DP value area / $6 max-pain pin — enter the call-spread *carry* only | `[STRUCT:max_pain]` `[DP:price_levels]` |
| Aggressive | $5.50 | Tag-and-reclaim of the $5.50 put-wall / gamma-flip (buy the squeeze off support) | `[STRUCT:today_gamma_flip]` `[OI:oi_by_strike]` |
| Fade | $6.28–6.33 | Rejection at the DP supply shelf below the $7 wall — put-debit-spread counter-trade | `[DP:price_levels]` |

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Support | **$5.50** (put_wall_support); $5.85 minor | `[OI:oi_by_strike]` `[DP:price_levels]` |
| Resistance | **$6.28–6.33** (DP supply); **$7.00** (call wall, net +15,308) | `[DP:price_levels]` `[OI:oi_by_strike]` |
| Gamma flip | **~$5.07–5.50** (0DTE ZGL / atm_flip $5.50) | `[STRUCT:today_gamma_flip]` |
| Largest pin | **$6.00** (July-OPEX max-pain) | `[STRUCT:max_pain]` |

Price-context color: RSI 40.2, price **below all SMAs (20/50/200)**, −63.9% from the 52-week high
$16.49 but +28.9% above the 52-week low $4.61 `[HIST:rsi fz, 52w_proximity fz]` — entering a
counter-trend long in a confirmed downtrend; **prefer the fade/short leg or no trade over chasing
the bull.** (Narrative color only; does not alter `p` or size.)

## Invalidation

- **Price-based:** a decisive **two-daily-close break of either edge** — below **$5.50** (put
  wall + gamma flip → downtrend resumes toward the $4.61 52w-low, *kills any long*) **or** above
  **$6.33 on rising IV** (squeeze ignites → *kills any short/range, confirms the bull leg*).
- **Signal-based:** (a) tomorrow's OI does **not** confirm the $6-Oct build (the sweep was a
  one-off) → the bull premise is gone `[OI:biggest_increases]`; (b) `cumulative_premium_flow`
  turns net-bullish 3 consecutive sessions → upside confirmation, flip the bias `[HIST:cumulative_premium_flow]`;
  (c) `conviction_matrix` flips DIRECTIONAL_LONG → HEDGED_LONG → the call flow was hedging/
  distribution `[INSIGHT:conviction_matrix]`.
- **Macro-based:** SPY regime breaks further RISK-OFF (high-beta ENVX β2.31 drops with the tape)
  `[MACRO:MarketRegime]`, or a hawkish late-July CPI/FOMC lifts the 10y (duration hit), or
  Industrials outflow accelerates `[MACRO:sector_flow]`.

## Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** `p_raw = 0.20` (n=5, source=backtest) → N-cap (n<10 → 0.75) → **p = 0.20**
  `[HIST:signal_backtest]`. (No conviction-bin fallback — source is backtest.)
- **Kelly inputs:** b = **2.33** (target $7.00 / entry $5.95 / stop $5.50), fraction = 0.25, cap_pct = 5.
- **Raw Kelly:** (0.20×2.33 − 0.80)/2.33 = **−0.143 (NEGATIVE edge)** → suggested size floored at **0**.
  **Win-rate map ceiling:** p = 0.20 < 0.50 → **starter / skip** (SHORT-side floor enforced).
- **Risk gates:**
  - Fundamentals (7b): **CONFIRM** → no-op (business growing, not deteriorating).
  - Sentiment/crowd (7c): **CONFIRM**, crowd_state **CROWDED_SHORT** → no-op (short crowd = squeeze
    fuel *for* a long; not a cut).
  - Correlation cluster (6/8): ENVX/INTC **0.521** → below the 0.60 soft-watch → **no cut**.
  - Sector rotation (6): **ADVERSE**, persistence 1.0 → **cut half a step** (already at floor).
  - Debate (8b): bull 0.55 vs **bear 0.75 → disconfirmed** → **down-shift one bin + cut one step**.
- **Final size: 0.0% — directional WATCH-ONLY / SKIP.** Negative Kelly + p<0.50 floor + two gates
  fired (rotation, debate) → no Kelly-justified directional position. The structures below are
  published **carry-only / "if-forced"** at a **token ≤0.5% notional**, explicitly **not** a sized
  recommendation (upward deviation is forbidden — gates fired).
- **Deviation reason:** none (deviation upward forbidden — gates fired).

## Option structures

> All premiums illustrative; only the $6-Oct call (~$1.29) is anchored to a real phase-1 print.
> **The textbook range-fade (sell a $5.5/$6.5 strangle or iron condor) is CONTRAINDICATED:** VRP is
> **−0.17, PREMIUM_BUYING (realized 105% > implied 88%)** `[HIST:vrp]` — you'd be shorting *cheap*
> vol on a 26%-short-float name that can gap on Aug-12. The asymmetry is wrong; **own optionality,
> don't sell it.** Both legs below are debits (VRP-appropriate), defined-risk, dated past Aug-12.

### Directional (primary) — the squeeze option, carry-only

- **Structure:** $6 / $8 **call debit spread** (long $6, short $8)
- **Strikes / expiry:** 6 / 8, **2026-10-16** (the flow expiry; spans Aug-12 earnings)
- **Debit/credit:** ~**$0.80 debit** (long $6 ~$1.29 − short $8 ~$0.49, illustrative)
- **Breakeven:** ~$6.80 · **Max value:** $2.00 at ≥$8 · **Max loss:** ~$0.80 (= the position)
- **Why this structure:** debit (VRP says buy, not sell); the short $8 leg caps cost on a
  **negative-Kelly** bet and anchors to the **$8 call-OI wall** `[OI:oi_by_strike]`; targets the
  $7–8 resistance zone; **max loss = debit by construction**, so a single Aug-12 earnings gap of
  the expected magnitude cannot exceed it. **Token size only** — this is a squeeze lottery, not a position.

### Defined-risk alternative — the trend-continuation hedge

- **Structure:** $5.50 / $4.50 **put debit spread** (long $5.50, short $4.50)
- **Strikes / expiry:** 5.5 / 4.5, **2026-10-16** (or 2026-08-21 to cheapen)
- **Debit/credit:** ~**$0.40 debit** (illustrative)
- **Breakeven:** ~$5.10 · **Max value:** $1.00 at ≤$4.50 · **Max loss:** ~$0.40
- **Why:** plays the **break of the $5.50 gamma-flip** → downtrend resumes toward the $4.61 52w-low
  `[STRUCT:today_gamma_flip; HIST:52w_proximity fz]`; debit (VRP-appropriate), defined-risk. Pairs
  with the call spread as a **cheap long-optionality straddle on the eventual range break** — the
  honest expression of "pinned now, breaks later, direction unknown," skewed to neither side.

## Macro overlay (cite phase-6)

- **Tailwinds:** cheap vol — VRP −0.17 PREMIUM_BUYING `[HIST:vrp]` (favors the debit legs); soft
  labor (unemployment 4.3%, payrolls +172K) `[MACRO:UNRATE, PAYEMS]`; normal curve 2s10s +0.31 `[MACRO:T10Y2Y]`.
- **Headwinds:** regime **TRANSITIONAL/CHOPPY, breadth 38%, "half size"** `[MACRO:MarketRegime]`;
  **Industrials net −$61.6M out, persistence 1.0** (adverse rotation) `[MACRO:sector_flow]`; Tech
  −$638M; 10y **4.40%** `[MACRO:DGS10]`; sticky CPI ~4.3% YoY `[MACRO:CPIAUCSL]`.
- **Net:** **net headwind** — the only macro positive is that vol is cheap (a structure choice, not a tailwind to direction).

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|------|-------|------------------|
| 2026-07-17 | July monthly OPEX (max-pain $6 magnet) | ? (mechanical pin to $6) |
| ~2026-07 (mid) | June CPI release | − if hot (rates) |
| ~2026-07 (late) | FOMC (typical late-July; confirm date) | ? |
| **~2026-08-12** | **ENVX Q2 earnings** (the binary; UW's 07-30 likely stale) | ? (the squeeze trigger) |

## Post-trade monitoring checklist

- [ ] **Tomorrow's OI** (`uw oi biggest-increases`): did the $6-Oct sweep confirm as a real OI build, or was it a one-off? (Bull leg lives/dies here.)
- [ ] **Dark pool buy_ratio** daily (`uw dark-pool block-stratified`): does 0.629 climb toward ≥0.70 (real accumulation) or fade to distribution?
- [ ] **GEX/DEX regime** on daily refresh (`uw options-structure gex/dex`): a flip from long-gamma → short-gamma (ZGL crossing spot) signals the range is about to break.
- [ ] **Short interest** semi-monthly (`fz quote`): is the 49.12M short base still covering (bullish) or rebuilding (bearish)?
- [ ] **Confirm the Aug-12 earnings date** (IR) before any pre-earnings sizing — UW's 07-30 is likely stale.
- [ ] **SPY/regime** (`uw risk market-regime`): a further RISK-OFF break takes high-beta ENVX down regardless of flow.

## Conviction note

Bias is **RANGE** at **0.55** — the lowest non-zero bin. The directional long is **not taken**
(negative Kelly p=0.20, disconfirmed debate, adverse rotation). 0.55 (not higher) because even the
range view is fragile: the latent 26% squeeze and cheap VRP mean the $5.50↔$6.33 range can break
violently in either direction on the Aug-12 catalyst. This is deliberately a **watch with a token
defined-risk carry**, not a conviction trade.

## Citations summary (M-04 — phase-10 spot-checks these)

1. `[FLOW:sweeps]` — $6-Oct call ask-sweep **$871,964 / 6,738 ct / 84.2% ask** — phase-1-flow.md §Sweeps.
2. `[HIST:signal_backtest]` — `bullish_flow` **win_rate 0.20 (n=5)**, avg move −0.05% — phase-5-historical.md §Signal backtest.
3. `[STRUCT:max_pain]` — **July-OPEX max-pain $6.00** + long-gamma 30/30 — phase-4-structure.md §Max pain / phase-5 §GEX time series.
4. `[SENT:short_float]` — **26.00% SI, 49.12M, 7.45 DTC, HTB** — phase-7c-sentiment.md §Short interest.
5. `[DEBATE:residuals]` — **disconfirmed, bear 0.75 ≥ bull 0.55** — phase-8b-debate.md §Disconfirmation verdict.
