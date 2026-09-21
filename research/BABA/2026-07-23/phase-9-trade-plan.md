# Phase 9 — Trade Blueprint

**Ticker:** BABA
**As-of date:** 2026-07-23
**PM voice:** desk PM running an institutional options-overlay book
**Spot reference:** $114.99 (phase-1 top-premium block; GEX snapshot $113.52; OI $114.05)
**Upstream phases cited:** phase-0.5 through phase-8b

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

BABA is a **capped, deteriorating name the Street hasn't downgraded yet** — a **5-session bearish
sweep campaign (consistency 1.0, $76.5M) `[FLOW:sweep_persistence]`** and **net call *selling* in the
lit tape (call_bid 49,758 > call_ask 36,425) `[INSIGHT:conviction_matrix]`** into a **short-gamma
regime (spot ~$113.5 below ZGL $119.71) `[STRUCT:gex]`**, over a **0/4 earnings-miss streak
(latest −89.5%) `[FUND:earnings_surprise]`** the **43-buy-vs-1-sell Street `[SENT:recommendation]`**
is set up to be disappointed by. But the edge is **thin and reward-capped**: a **BUSY_NAME_NORMAL_DAY
`[CTX:unusual_verdict]`** with **+$625M standing bullish 90-day flow `[HIST:cumulative_premium_flow]`**,
a **max-pain pin at $114–115 `[STRUCT:max_pain]`**, and a **disconfirmed debate (bear_residual 0.65 ≥
bull_residual 0.65) `[DEBATE:disconfirmed]`**. Net: a **very small, defined-risk FADE of the $119–120
cap toward the $110–112 shelf** — not a directional short.

## Bias + conviction + horizon

- **Directional bias:** **SHORT / fade** (plurality of phases 1–8: 3 SHORT, 1 NEUTRAL, 1 RANGE, 0 LONG).
- **Conviction (M-01 bin):** **0.55** (slight edge).
- **Time horizon:** **1–4 weeks.**
- **Why this bin:** base moderate-edge (0.65) **down-shifted one bin by the phase-8b disconfirmation**
  (bear_residual ≥ bull_residual) — the direction survives but reward is capped and disconfirming
  evidence is real. Expect phase-10 confluence in the low band; if it scores higher, a
  `## Conviction deviation` note would be required (none used).

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| **Primary** | **$118–119** | rally/rejection into the ZGL + $120 call/gamma wall (the ideal short entry) | `[STRUCT:gex]` ZGL $119.71 / `[OI:oi_by_strike]` $120 wall |
| Aggressive | $115–115.7 | tag of the $115.55/$115.67 DP shelf + reject; smaller R, act only on a lower-high | `[DP:price_levels]` |
| Fade (plan B) | reclaim & hold **> $120** | if the cap breaks and dealers flip long-gamma, stand aside / flip to the $120/$125 call *debit* — counter-trade | `[STRUCT:gex]` ZGL |

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Support | **$114.97** (DP shelf) → **$113.2–113.7** (block floor) → **$112** (neg-gamma accelerant) → **$110** (put wall) | `[DP:price_levels]` / `[STRUCT:gex]` / `[OI:oi_by_strike]` |
| Resistance | **$116.85–118.22** (DP overhead) → **$119.71–$120** (ZGL + $8.56M gamma wall + OI call wall) | `[DP:price_levels]` / `[STRUCT:gex]` / `[OI:oi_by_strike]` |
| Gamma flip (ZGL) | **$119.71** (short-gamma below, long-gamma above) | `[STRUCT:gex]` |
| Largest pin | **$114 (0DTE) / $115 (2026-08-21 monthly)** — max-pain magnet | `[STRUCT:max_pain]` |

*Price-context color:* `fz` RSI/SMA/52W were **null for this ADR** (phase-5) — no independent
overbought/oversold cross-check; note only that BABA is **−40% off its $192.67 52-week high, lower
third of range** `[FUND:priceRel52wSP]` → mean-reversion risk against the fade (narrative only, not a
sizing input).

## Invalidation

- **Price-based:** **two daily closes above $120** (reclaim of ZGL + $120 gamma/OI wall → dealers flip
  long-gamma, the cap is gone) `[OI:oi_by_strike]` `[STRUCT:gex]`. Secondary: a **daily close back
  above $118** that holds → the fade is not working.
- **Signal-based:** **DEX/GEX flips POSITIVE on the phase-4 daily refresh** (spot reclaims ZGL → dealers
  buy dips, killing the amplification) `[STRUCT:gex]`; OR **cumulative premium flow turns net-bullish
  for 3 consecutive sessions** on top of the standing +$625M `[HIST:cumulative_premium_flow]`.
- **Macro-based:** **a risk-ON / dovish surprise at FOMC 2026-07-29** (6 days out) sparking a broad
  bounce the low-SI name has no forced-capitulation counter to `[MACRO:FOMC_2026-07-29]`; OR a
  **positive US-China tariff/AI-sanction de-escalation headline** `[MACRO:ChinaRisk]`.
- **Exit rule:** **hard stop** on the directional put spread (debit — close 100% on two closes > $120);
  **roll/close** the iron condor if either wing is breached and the breach holds.

## Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** p_raw = **0.875** (`bearish_flow` backtest, **n=8**, source=**backtest**)
  → N-cap (n<10 → 0.75) → **capped p = 0.75** `[HIST:signal_backtest]`. *(Caveat: market-wide base
  rate, NOT BABA-specific; conflicts with the bullish 90d flow — carried into the gates.)*
- **Kelly inputs:** b = **2.8** (primary entry $118, target $111, stop $120.5 → 7.0/2.5), fraction = 0.25, cap_pct = 5.
- **Raw Kelly:** (0.75×2.8 − 0.25)/2.8 = **0.66** → suggested = min(0.66×0.25×100, 5) = **5.0%**.
  **Win-rate map ceiling:** p 0.75 ≥ 0.70 → **full (≤ 5%)**.
- **Risk gates (each cuts; applied in order):**
  - **Fundamentals (phase-7b): CAUTION** → cut one step (full → half): **5% → 2.5%**.
  - **Sentiment / crowd (phase-7c): CAUTION, crowd_state CROWDED_LONG** → cut one step (half → starter):
    **2.5% → 1.25%**.
  - **Correlation cluster (phase-6/8): none** (BABA/GOOG < 0.70, no pair flagged) → no-op.
  - **Sector rotation (phase-6): ADVERSE for a long, but the trade is a SHORT/fade** → the −$3.04B
    Consumer-Cyclical outflow is **aligned** with the fade → **gate does not fire** (no cut).
  - **Debate (phase-8b): disconfirmed = TRUE** (bull_residual **0.65** vs bear_residual **0.65**) →
    down-shift the bin (→ 0.55) **and cut one step (starter → minimal): 1.25% → ~0.6%**.
- **Context modifier (phase-0.5): BUSY_NAME_NORMAL_DAY** → no top-of-band sizing (already far below).
- **Final size:** **≈ 0.6% of book risk** (minimal / sub-starter, **defined-risk only**). Three gates
  fired (7b, 7c, 8b) — an upward deviation is **forbidden**; none taken.
- **Deviation reason:** none.

## Option structures

Front-expiry implied move **±1.56% (~$1.78)** `[CTX:implied_move]` — small/near-term; the 1–4w
structures below span wider. **Both expiries set to 2026-08-14** to sidestep the **unverified earnings
date** (phase-6: UW says 2026-09-04 but BABA's June quarter historically prints mid-August). If earnings
verifies for Sep-04, extend to 2026-08-21 (heavier OI, PCR 0.42); if it verifies for mid-August, **stay
at/inside 08-14** to avoid the binary + IV crush.

### Directional (primary)

- **Structure:** **put debit spread** (long the fade, defined risk).
- **Strike(s) / expiry:** **long $115 put / short $110 put, 2026-08-14** (targets the $110 put wall
  `[OI:oi_by_strike]`).
- **Debit/credit:** ~**$1.70 debit** (est., IV ~47%).
- **Breakeven:** ~**$113.30**.
- **Max loss:** **$1.70** (the debit) — max profit $3.30 to $110.
- **Why this structure:** IV is **rich by level (84.5th pctile) but FAIR by risk-premium (VRP −0.011)
  `[HIST:vrp]`**, so a **debit** spread (not naked long puts) keeps vega small and defines the loss on a
  thin-edge fade; strikes hug the $114–115 pin (entry) and the $110 structural support (target) over a
  1–4w horizon.

### Defined-risk alternative

- **Structure:** **iron condor** (the CHOPPY-regime-endorsed range structure `[MACRO:MarketRegime]`).
- **Strike(s) / expiry:** **short $120 call / long $125 call + short $110 put / long $105 put, 2026-08-14.**
- **Debit/credit:** ~**$1.60 net credit** (est.).
- **Breakeven:** ~**$121.60 / $108.40**.
- **Max loss:** **~$3.40** (either $5 wing − credit).
- **Why this structure:** monetizes the **$112–$120 structural cage** (ZGL + $120 gamma/OI call wall
  above `[STRUCT:gex]` `[OI:oi_by_strike]`; $110 put wall below) and the **complacent call skew (calls
  richer, ratio 0.924) `[STRUCT:term_skew]`** by selling the rich $120 call, with the $114–115 max-pain
  pin `[STRUCT:max_pain]` as the theta magnet. Wings sit ~0.4σ out in the wide 47% IV — this is a
  **structure-over-implied-vol bet**; size tiny per the sizing block.

## Macro overlay (cite phase-6)

- **Tailwinds:** structural AI-cloud revenue **+40%** `[MACRO:ChinaRisk]` (long-term, not near-term);
  Fed funds easing to **3.63%** `[MACRO:DFF_2026-07-22]`.
- **Headwinds:** regime **TRANSITIONAL/CHOPPY — "half size, defined-risk, iron condors"**
  `[MACRO:MarketRegime_2026-07-23]`; **Consumer-Cyclical outflow −$3.04B today** `[MACRO:SectorFlow_2026-07-23]`;
  **US-China tariff + DoD-blacklist + outbound-reg overhang** `[MACRO:ChinaRisk]`; **10y at 4.67%**
  pressuring EM/growth `[MACRO:DGS10_2026-07-22]`; **bearish breadth 31.9%** `[MACRO:Breadth_2026-07-23]`.
- **Net:** **HEADWIND** (aligned with the fade; the AI tailwind is structural, not a 1–4w catalyst).

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|------|-------|------------------|
| **2026-07-29** | FOMC decision (no dot plot) | ? (bounce risk if dovish; can exceed ±1.56%) |
| **~mid-Aug (VERIFY vs UW 09-04)** | BABA FQ1-2027 earnings | − (0/4 miss streak) but binary; **structures dated to avoid it** |
| ongoing | US-China tariff / AI-sanction headlines | − (unscheduled tail; complacent skew under-prices) |

## Post-trade monitoring checklist

- [ ] **Daily: GEX/ZGL** — a reclaim of **$119.71** (spot > ZGL) flips dealers long-gamma → **exit** (phase-4 refresh).
- [ ] **Daily: dark-pool tier mix** — if the **block tier flips to accumulation (buy_ratio > 0.55)** or a **mega buy print** appears, the distribution read breaks (phase-2/7).
- [ ] **Each session: cumulative premium flow** — 3 consecutive net-bullish sessions on top of +$625M = thesis erosion (phase-5).
- [ ] **Analyst tape** — first **downgrade** off the 43-buy consensus = fade confirmation; a fresh **upgrade / price-target raise** = defended-name bounce risk (phase-7c).
- [ ] **Verify the earnings date** before 2026-08-08 — if mid-August confirms, do not roll structures past 08-14 (IV crush / binary).
- [ ] **FOMC 2026-07-29** — a dovish risk-on surprise is a same-week invalidation trigger (phase-6).

## Citations summary (≥3 distinct upstream datapoints — M-04)

1. `[FLOW:sweep_persistence]` — 5-session bearish sweep, consistency 1.0, $76.53M — phase-1-flow.md §Sweeps.
2. `[STRUCT:gex]` — short-gamma regime, ZGL $119.71, spot ~$113.5 below — phase-4-structure.md §GEX.
3. `[HIST:signal_backtest]` — `bearish_flow` win_rate 0.875 (n=8) → capped p 0.75 — phase-5-historical.md §Sizing handoff.
4. `[FUND:earnings_surprise]` — 0/4 beat-rate, latest −89.5% — phase-7b-fundamentals.md §Earnings.
5. `[SENT:recommendation]` — Street 43 buy vs 1 sell, improving — phase-7c-sentiment.md §Analyst.
6. `[DEBATE:disconfirmed]` — bear_residual 0.65 ≥ bull_residual 0.65 — phase-8b-debate.md §Verdict.
