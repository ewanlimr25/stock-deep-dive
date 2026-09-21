# Phase 9 — Trade Blueprint

**Ticker:** GRAB
**As-of date:** 2026-05-21
**PM voice:** desk PM running an institutional $5–50M options-overlay book
**Spot reference:** $3.555 (last DP print 21:34Z, NBBO mid; see phase-2)
**Upstream phases cited:** phase-1 through phase-8

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

A single institution accumulated **$2.91M (817,675 sh) at NBBO mid post-bell
plus 2.91× DP buy/sell ratio for the day** [DP:largest],
[INSIGHT:institutional_accumulation], anchoring a long-gamma dealer book
($245M LEAP GEX at the $4 strike, ZGL $2.63) [STRUCT:gex] — the structural
bid is real and the upside magnet is well-defined. But the 90-day premium
tape has been net bearish **-$6.28M with price -10% from $3.91 to $3.55**
[HIST:cumulative_premium_flow, HIST:historical_trend], and accumulation-
hunter conviction is capped at 3/5 "pending a second session of
confirmation" [AGENT:accumulation-hunter] — so we express the
constructive view with a **defined-risk, premium-selling structure that
collects the +14% VRP** [HIST:vrp] rather than chasing directionally
into a TRANSITIONAL regime + binary June FOMC [MACRO:MarketRegime_2026-05-21
UW].

## Bias + conviction + horizon

- **Directional bias:** LONG (modest)
- **Conviction (M-01 bin):** **0.55**
- **Time horizon:** **1–4 weeks** (3 of 4 agents picked this window)
- **Why this bin** (one sentence): phase-8 agent average is 2.25/5 with
  3-of-4 voting RANGE/NEUTRAL and only 1 voting LONG-3; phase-10 confluence
  will likely land in the 50–64 band → 0.55 bin per rubric.

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| Primary    | **$3.50–$3.52** | tag of the 5-day DP support cluster ($3.51 = $8.8M premium, $3.50 = $5.4M); enter on hold of $3.50 | [DP:price_levels] |
| Aggressive | **$3.40–$3.42** | flush to the 30d pivot low ($3.47–$3.40); add tranche only if vol contracts (IV30d holds <50%) | [HIST:historical_trend], [DP:price_levels] |
| Fade       | **$4.00 → $3.90** | rejection at the $4 LEAP gamma magnet; fade with a long-put/short-call kicker only if today's accumulation is reversed by a new $1M+ DP sell block | [STRUCT:gex], [DP:largest] |

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Support (primary) | **$3.50** | [DP:price_levels] — 5-day $5.4M premium / 1.53M sh |
| Support (secondary) | **$3.47** | [HIST:historical_trend] — 30d low and the agent-consensus invalidation |
| Resistance | **$4.00** | [STRUCT:gex] — $245M LEAP GEX magnet, also major OI wall [OI:biggest_increases] |
| Gamma flip (regime) | **$2.63** | [STRUCT:gex] — 365-DTE ZGL; break would flip to short-gamma |
| 0DTE support shelf (tomorrow's session) | **$3.50** | [STRUCT:today_gamma_flip] — $39.6M GEX wall |
| Largest pin | **n/a** — GRAB not in pin_risk top 48 | [OI:pin_risk] |
| Distribution / heavy 5d zone | **$3.54** | [DP:price_levels] — $30.7M / 8.7M sh / 33 trades (true center of fair value) |

## Invalidation

- **Price-based:** Two daily closes below **$3.47** (phase-5 30d low and the
  agent-unanimous invalidation level). Tight version: intraday break of the
  $3.50 0DTE gamma support shelf [STRUCT:today_gamma_flip] with no reclaim
  by close.
- **Signal-based:** (a) `institutional_accumulation` flips from ACCUMULATION
  to DISTRIBUTION or NEUTRAL on the phase-7 daily refresh
  [INSIGHT:institutional_accumulation]; OR (b) `cumulative_premium_flow`
  (3-day) turns net bearish > $200K for 3 consecutive sessions
  [HIST:cumulative_premium_flow]; OR (c) `conviction_matrix` flips from
  DIRECTIONAL_LONG to HEDGED_LONG / MIXED [INSIGHT:conviction_matrix].
- **Macro-based:** Hawkish hold or hawkish dot-plot surprise at the
  **2026-06-16/17 FOMC** [MACRO:FOMC_2026-06-17 WebSearch:federalreserve.gov]
  → 4-dissenter dovish narrative defeated, EM-tech correlated sell-off
  expected per [AGENT:risk-monitor]; **OR** UW Market Regime flips from
  TRANSITIONAL to RISK-OFF [MACRO:MarketRegime_2026-05-21 UW].

**Exit on invalidation:** TRANCHE EXIT — close 50% on first invalidation
firing (signal- or price-based), close remaining 50% on confirmation
(close below $3.40 or a second consecutive invalidating signal). For the
credit structure: ROLL down strikes one strike if invalidation fires
before 7 DTE; otherwise CLOSE.

## Sizing (% of risk, NOT dollars)

- **Kelly inputs:** p = **0.55** (conviction bin), b = **1.50** (credit
  structure payoff ratio — see "Defined-risk" below: max gain $0.30 / max
  loss $0.20), fraction = 0.25
- **Raw Kelly:** (0.55 × 1.50 − 0.45) / 1.50 = (0.825 − 0.45) / 1.50 =
  **0.250 (25.0%)**
- **Suggested size:** 0.250 × 0.25 × 100 = **6.25%**
- **Final size:** **5.0% of book risk** (hard cap per `cap_pct = 5`
  rubric) → no `sizing_deviation_reason` invoked (the rubric cap is
  honored).
- **Deviation reason:** none (the natural Kelly would suggest 6.25% but
  we are capped to 5%).
- **Half-size override:** UW Market Regime is TRANSITIONAL, which
  recommends "half position sizes." Apply this BEFORE the cap:
  - Pre-cap target: 6.25% → halved for TRANSITIONAL regime = **3.13%**
  - Post-cap = 3.13% (below the 5% ceiling, so cap is moot)
- **FINAL DEPLOYED SIZE: 3.0% of book risk** (rounded; respects both the
  TRANSITIONAL-regime half-size guidance from phase-6 and the 5% Kelly
  cap from the rubric).

## Option structures

### Directional (primary) — Call debit spread, July expiry

- **Structure:** **+$3.50C / -$4.00C** call debit spread
- **Strike(s) / expiry:** $3.50 / $4.00, 2026-07-17 (57 DTE, past
  2026-06-16/17 FOMC, before 2026-07-30 earnings — clean window)
- **Indicative pricing** (derived from phase-1 flow tape; closing
  references):
  - Long $3.50C: ~$0.25–$0.30 (slightly OTM, IV ~48–50%, delta ~0.55)
  - Short $4.00C: ~$0.10–$0.15 (delta ~0.25)
  - **Net debit: ~$0.15 per spread = $15 per contract**
- **Breakeven:** **$3.65** ($3.50 + $0.15 debit)
- **Max gain:** **$35 per contract** at $4.00 or above
- **Max loss:** **$15 per contract** (debit paid)
- **Payoff ratio:** 35/15 = **2.33×**
- **Why this structure:** IV is NORMAL at 38th %ile but VRP is +14%
  [HIST:iv_percentile_zscore, HIST:vrp] — debit is acceptable because
  the call wing benefits from the COMPLACENT skew making calls relatively
  expensive but the magnet at $4 [STRUCT:gex] gives a high-probability
  target. The 7/17 expiry threads between the FOMC and earnings.
- **Sizing translation:** 3.0% of book × debit $15/contract → number of
  contracts = (book × 0.030) / $15. (e.g., $5M book → $150K risk → 10,000
  contracts; $20M book → $600K risk → 40,000 contracts. Adjust to
  available liquidity — GRAB July $3.50/$4 likely caps at <1,000
  contracts per side without slippage.)

### Defined-risk alternative — Put credit spread, July expiry

- **Structure:** **-$3.50P / +$3.00P** put credit spread
- **Strike(s) / expiry:** $3.50 / $3.00, 2026-07-17 (57 DTE)
- **Indicative pricing:**
  - Short $3.50P: ~$0.45–$0.50 (close to ATM; IV ~47–50%)
  - Long $3.00P: ~$0.18–$0.22 (further OTM; IV ~45–48%)
  - **Net credit: ~$0.30 per spread = $30 per contract**
- **Breakeven:** **$3.20** ($3.50 − $0.30 credit)
- **Max gain:** **$30 per contract** at $3.50 or above
- **Max loss:** **$20 per contract** (width $0.50 − credit $0.30)
- **Payoff ratio:** 30/20 = **1.5×**
- **Why this is the preferred structure for sizing:** the **PREMIUM_SELLING
  regime (VRP +14%) [HIST:vrp] + long-gamma magnet at $4 [STRUCT:gex] +
  $3.50 DP support cluster [DP:price_levels]** all reward selling the
  $3.50 put. The Kelly math above is computed for THIS structure
  (b=1.5×). Use this as the primary deployment; the debit spread is the
  symmetric upside-leverage alternative for a sub-allocation.

### Why NOT to use other structures here

- **Naked long call:** debit + VRP headwind + thin underlying = bad
  R/R; rejected.
- **Long straddle / strangle:** the LEAP $4 straddle is already being
  bought by another desk [FLOW:top_premium_trades]; phase-4 vanna is
  mildly negative meaning a vol crush could hit; rejected.
- **Risk reversal (short put + long call):** unlimited downside in a
  TRANSITIONAL regime + binary FOMC = unacceptable risk per
  [AGENT:risk-monitor]; rejected.

## Macro overlay (cite phase-6)

- **Tailwinds:**
  - **Tech sector inflow $297M** today [MACRO:SectorRotation_2026-05-21 UW]
  - **Financial Services sector inflow $15.3M** today
    [MACRO:SectorRotation_2026-05-21 UW]
  - **VIX 16.76 + IV rank 14.2 (complacent)** [MACRO:VIX_2026-05-21 UW] —
    low macro vol cost
  - **4 dissenters at the April 29 FOMC** (most since 1992)
    [MACRO:FOMC_2026-04-29 WebSearch:federalreserve.gov] — rising cut
    probability is EM consumer-tech bullish
  - **GRAB Q1 2026 print: rev +24% YoY, EBITDA +46% YoY**
    [MACRO:GRAB_Q1_2026_2026-05-05 WebSearch:sec.gov]
- **Headwinds:**
  - **UW regime = TRANSITIONAL** [MACRO:MarketRegime_2026-05-21 UW] →
    half size required
  - **Core CPI +2.8% YoY (above target)** [MACRO:CPI_2026-04
    WebSearch:bls.gov] — delays Fed cuts
  - **Breadth weak: 37.5% bullish_pct** [MACRO:MarketRegime_2026-05-21 UW]
  - **Post-earnings fade**: GRAB ran $3.62 → $3.79 then back to $3.55
    (-6.3% from post-print high) [HIST:historical_trend] — bullish
    fundamentals not getting paid
- **Net:** **MIXED with mild tailwind** — sufficient to support a
  conviction-0.55 directional trade but not a 0.75+ size.

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|------|-------|------------------|
| 2026-05-22 (Fri) | Weekly OPEX — no GRAB pin [OI:pin_risk] | neutral |
| 2026-06-05 (Fri) | **NFP May release** | ?  (sets FOMC tone — softer = bull) |
| 2026-06-10 (Wed) | **CPI May release** | ?  (softer = bull EM-tech) |
| **2026-06-16/17** | **FOMC + new SEP / dot plot** | **dominant** — dovish = bull, hawkish = bear |
| 2026-06-18 (Thu) | June monthly OPEX (GRAB $4 wall) | mild positive (pin) |
| 2026-06-26 (Fri) | Phase-4 IV kink (catalyst TBD — NOT earnings) | uncertain — possibly sector/analyst |
| 2026-07-17 (Fri) | July monthly OPEX (our spread expiry) | trade exit point |
| 2026-07-30 (Thu, after-close approx) | **Q2 2026 earnings** [INSIGHT:deep_dive] | exit BEFORE — outside our window |

## Post-trade monitoring checklist

- [ ] **Daily:** re-run `insights_institutional_accumulation` and confirm
  buy/sell ratio stays >1.5×; flip to <1.0 = signal-based invalidation
  fired [INSIGHT:institutional_accumulation].
- [ ] **Daily:** re-run `historical_cumulative_premium_flow` (3-day) and
  watch for sustained <-$200K net premium [HIST:cumulative_premium_flow].
- [ ] **Daily:** check GEX regime is still POSITIVE and ZGL > $2.50; a
  flip to NEGATIVE = structural invalidation [STRUCT:gex],
  [HIST:gex_time_series].
- [ ] **At each phase refresh:** check that `conviction_matrix` remains
  DIRECTIONAL_LONG; flip to HEDGED_LONG / MIXED / DIRECTIONAL_SHORT =
  signal-based invalidation [INSIGHT:conviction_matrix].
- [ ] **Pre-FOMC (2026-06-16):** size DOWN to 50% of current deployment
  ahead of binary 2026-06-17 risk per [AGENT:risk-monitor] guidance; do
  NOT add into the catalyst.
- [ ] **Watch SE-Asia EM proxies** (EWY, EEM, SE) for correlated
  divergence — if those break down while GRAB holds, it's a signal of
  GRAB-specific bid; if GRAB breaks down with them, it's correlated
  drawdown risk firing [AGENT:risk-monitor].

## Citations summary

Minimum 3 distinct upstream datapoints (M-04 requirement). Listed here
for audit:

1. **[DP:largest]** — "$2.91M block executed at 21:02Z, 817,675 shares at
   $3.56 NBBO-mid" — phase-2-dark-pool.md §Largest blocks (table row 1).
2. **[STRUCT:gex]** — "$245,418,226 net GEX at the $4 strike (365 DTE) +
   ZGL $2.63 POSITIVE long-gamma regime" — phase-4-structure.md §GEX —
   365 DTE.
3. **[HIST:cumulative_premium_flow]** — "Net 90d flow -$6,283,288
   BEARISH (bullish $10.3M vs bearish $16.6M)" — phase-5-historical.md
   §Cumulative premium flow.
4. **[HIST:vrp]** — "IV30d 44.04% vs realised 29.9% → VRP +14.1%,
   PREMIUM_SELLING regime" — phase-5-historical.md §IV regime.
5. **[MACRO:MarketRegime_2026-05-21 UW]** — "TRANSITIONAL — Mixed
   signals, reduce position size, wait for clarity; bullish_pct 37.5%"
   — phase-6-macro.md §Market regime.
6. **[INSIGHT:conviction_matrix]** — "DIRECTIONAL_LONG, confidence
   26.81%, DP buy_ratio 0.745, explanation 'institutional directional
   bet'" — phase-7-insights.md §Conviction matrix.
7. **[AGENT:risk-monitor]** — "Triple-correlated trade — long EM beta +
   long EM-consumer-tech + short USD — into a TRANSITIONAL US regime
   with 37.5% breadth and a binary 6/17 FOMC" — phase-8-agent-views.md
   §risk-monitor.
