# Phase 9 — Trade Blueprint: PATH (UiPath) as-of 2026-07-22

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

**Ticker:** PATH · **Spot:** $10.53 · **As-of:** 2026-07-22 · **PM voice**

## Thesis (≤3 sentences)

PATH gapped ~13% today on the OpenAI "Presence" competitive shock `[MACRO:OpenAI_Presence]`,
and the tape is a genuine stalemate: today's aggressor is net-bearish (net −$1.60M,
calls net-sold `[FLOW:insights_deep_dive]`) into a **long-gamma, range-bound dealer
regime** (ZGL $6.92, mechanical DEX bid `[STRUCT:dex]`) with max-pain gravity up at
$11–11.5 `[STRUCT:max_pain]`. The fundamental gate **vetoes any bounce-as-accumulation
long** (sustained insider selling, MSPR ≈ −100, −9.6M sh Mar-26 `[FUND:MSPR]`) while the
positioning gate **vetoes a fresh short** (crowded ~13–32%-of-float short, squeeze fuel
`[SENT:short_float]`), and all four desk agents returned **NEUTRAL/RANGE** `[AGENT:risk-monitor]`.
Net: **no directional edge — trade the $10–$12 range with defined risk, or stand flat.**

## Bias + conviction

- **Bias: NEUTRAL / RANGE** (plurality of phases 1–8: 3 NEUTRAL + 1 RANGE).
- **Conviction: 0.55** (slight edge — the "edge" is the range holding, not a direction).
  Base narrative was ~0.60–0.65 (mixed); the phase-8b disconfirmation (`disconfirmed=true`,
  bull 0.65 = bear 0.65) **down-shifts one bin to 0.55**. Phase-10 confluence will confirm
  the band; no upward deviation is claimed.

## Entry zones

- **Primary:** initiate the defined-risk **iron condor** with spot in the **$10.40–$10.70**
  zone (near DP VWAP $10.70 `[INSIGHT:institutional_accumulation]`), trigger = spot holding
  **above the $10 put wall** `[OI:oi_by_strike]`. This is the "range confirmed" entry.
- **Aggressive:** sell the condor into a **bounce toward $11.00–$11.50** (the max-pain pin
  `[STRUCT:max_pain]` / two-sided $11 battleground `[OI:oi_by_strike]`) — premium is richer
  and you are selling nearer the $12 ceiling.
- **Fade (plan B / counter-trade):** if the range breaks **down** (two closes < $9.87),
  flip to the bear put spread below (down-tail). If it breaks **up** (two closes > $12.00,
  reclaiming the DP supply `[DP:price_levels]`), **do NOT fade — that is the squeeze; stand
  aside.**

## Levels to watch

- **Support:** **$10.00** put wall `[OI:oi_by_strike]` → range floor **$9.87** (30d low
  `[INSIGHT:price_vs_flow]`) → deeper put walls $9 / $8.5.
- **Resistance:** **$11.00** battleground/pin → **$11.90–$12.00** hard ceiling (call wall
  `[OI:oi_by_strike]` + $550M 5-day DP supply `[DP:price_levels]` + $12 analyst PT
  `[MACRO:UBS_PT]`).
- **Gamma flip (ZGL):** **$6.92** `[STRUCT:gex]` — far below; regime stays long-gamma
  unless a catastrophic break. Not a near trigger; it is the "vol-expansion" floor.
- **Pin magnet:** **$11.00** (8/21 max-pain, the heavy 16.2%-OI cliff) / $11.50 (near
  expiries) `[STRUCT:max_pain]` — native max-pain, not eyeballed.
- Price-context color: `fz` RSI/52-wk read was unavailable (reduced payload, phase-5);
  from Finnhub, spot sits near the **52-week low $9.20** (high $19.84) `[FUND:52w]` — a
  value zone, not a chase, which is *why* the crowded short is squeeze-prone.

## Invalidation (all three categories)

- **Price-based:** two daily closes **below $9.87** (range floor / below the $10 put wall)
  → range broken to the downside, close the condor and let the bear put spread run; **or**
  two daily closes **above $12.00** (reclaim of the DP supply + call wall) → squeeze
  underway, close the condor's call side.
- **Signal-based:** post-7/24 **DEX/GEX weakens** and cumulative premium flow turns
  net-bearish **3 consecutive sessions** `[HIST:cumulative_premium_flow]`, **or**
  institutional-accumulation flips NEUTRAL→distribution `[INSIGHT:institutional_accumulation]`
  — confirms the phase-8b **vanna air-pocket** `[STRUCT:vanna_charm]` and voids the range.
- **Macro-based:** a **fresh OpenAI-competition headline** or a **second analyst PT cut
  below $10** `[MACRO:UBS_PT]` (secular de-rate confirmation), **or** a market regime flip
  to RISK-OFF as breadth deteriorates from the current 33.8% `[MACRO:MarketRegime]`.

**Exit on invalidation:** the condor is a **credit** structure → **close or roll** at the
first invalidation (do not hold for max loss). The bear put spread is a **debit** → let its
**defined max loss** run (no separate stop needed).

## Sizing (% of book risk)

**Kelly input (phase-5 handoff):** signal_class **bearish_flow** (today's dominant flow /
the phase-8b down-tail), `win_rate_source = backtest`.
- `p_raw = 0.10` (bearish_flow win-rate, n=10).
- N-conditional cap (10 ≤ n < 20 → 0.85): `p = min(0.10, 0.85) = 0.10`.
- **Win-rate sizing map:** `p < 0.50` → **starter / skip**; **SHORT-side floor** applies.
- Payoff `b` (bear put spread $10/$9, debit ~$0.35, max profit $0.65) = **1.86**.
- `raw_kelly = (0.10 × 1.86 − 0.90) / 1.86 = −0.38` → **NEGATIVE edge** → directional short
  is NOT a position on its own merit.

**Risk gates (each cuts only; all five listed):**
1. **Fundamentals veto (7b): VETO** → directional **LONG = 0% / watch-only** (insider selling + EPS miss).
2. **Sentiment/crowd (7c): VETO**, crowd_state **CROWDED_SHORT** → fresh directional **SHORT = 0% / watch-only** (squeeze risk).
3. **Correlation cluster: none** (PATH is the only 2026-07-22 blueprint) → no-op.
4. **Sector-rotation (6): ADVERSE** (Tech inflow, PATH diverges) → cut half a size step.
5. **Debate disconfirmation (8b): disconfirmed = true** (bear 0.65 ≥ bull 0.65) → down-shift bin one (→0.55) + cut one size step.

**Context modifier (0.5):** `GENUINELY_UNUSUAL` → no-op (edge already in `p`).

**Result:** negative Kelly on the bear side + a **long-veto AND a short-veto** = **no
directional position.** The Kelly-sized risk budget is therefore **`final_size_pct = 0.0%`**
(negative edge; no upward deviation permitted with gates fired).
- **Directional final size: 0% (watch-only).**
- **Optional defined-risk range carry (iron condor):** if the desk still wants exposure,
  a **STARTER ~1% book max-loss** condor is the only un-vetoed expression — but this sits
  **outside the Kelly-sized budget** (it is carry-only, permitted under veto). Selling
  premium into the 7/24 shock-residual carries gap risk, so **flat/watch is fully
  defensible and is the PM's honest default here.**

## Option structures

Front-expiry **implied move ±4.70% ≈ ±$0.50** `[CTX:implied_move]`. Structures sized to it;
a single 7/24 gap of ~1× the priced move ($10.53 → ~$10.03) stays **inside** the condor's
short strikes, and a 2× gap is capped by the long wings.

### 1) Defined-risk (PRIMARY) — Iron condor, expiry **2026-08-21**
- **Sell $9.5 put / Buy $8.5 put** (downside cushion below the $9.87 floor to the $8.5 put wall) **+ Sell $12 call / Buy $13 call** (upside capped at the $12 wall/DP-supply/PT ceiling).
- Net **credit ~$0.35** (illustrative); **max loss = $1.00 − credit ≈ $0.65 per side**, fully defined.
- **Profits if PATH holds ~$9.5–$12 into 8/21** — the range every layer agrees on — and benefits from **post-7/24 front-IV decay** (VRP +0.18 premium-selling `[HIST:vrp]`).
- Put-skewed strikes (short put at $9.5, not $10) deliberately give the **heavier down-tail** room per phase-8b. **Size: starter (~1% book max loss).**

### 2) Directional (REQUIRED, gated) — Bear put spread, expiry **2026-08-21**
- **Buy $10 put / Sell $9 put.** Debit **~$0.35**; **max loss $0.35** (defined — no squeeze blow-up, which is *why* a spread and not short stock); breakeven **$9.65**; max profit **$0.65** if PATH < $9 by 8/21.
- This is the **phase-8b down-tail expression** (post-7/24 vanna air-pocket + secular OpenAI de-rate). **Explicitly marked watch-only / STARTER:** the bearish base rate is 10% (negative Kelly) and 7c vetoes fresh shorts — hold only as a small defined-risk hedge into the range, not a conviction bet.

## Macro overlay

- **Headwinds:** OpenAI "Presence" secular competitive shock `[MACRO:OpenAI_Presence]`;
  analyst PTs cut to $12 `[MACRO:UBS_PT]`; regime TRANSITIONAL, breadth 33.8%, "half-size"
  `[MACRO:MarketRegime]`; 10y 4.63% rising `[MACRO:DGS10]` (mild duration headwind).
- **Tailwinds (partial):** Technology durable sector inflow, persistence 0.80
  `[MACRO:SectorFlowPersistence]` (but PATH diverges — does not reach the name); Fed easing
  (funds 3.63%) `[MACRO:DFF]`; value/net-cash floor `[FUND:valuation]`.
- **Net: HEADWIND** — the sector tailwind bypasses the name.

## Catalyst calendar (next 30d)

| Date | Event | Impact |
|---|---|---|
| ongoing (7/23+) | OpenAI Presence rollout / follow-on headlines | HEADWIND, can exceed ±4.7% priced move |
| ~2026-07-24 | **NOT a scheduled event** — front IV is shock residual | IV decay (fade long-vol; helps the condor) |
| ~2026-09-03/08 | Q2 FY2027 earnings (outside 30d; drives Sep/Jan LEAP) | binary — beyond these structures' 8/21 expiry |

## Post-trade monitoring checklist

1. **Daily $10 put wall + $12 ceiling** — two closes outside $9.87–$12.00 voids the range (close condor).
2. **Post-7/24 vanna/DEX refresh** — if the dealer bid flips to net selling and premium flow goes net-bearish 3 sessions, exit (air-pocket confirmed).
3. **Short-interest / borrow tape** — a squeeze through $11.5→$12 means close the call side; do not fight it.
4. **OpenAI-competition & analyst headlines** — a second PT cut < $10 shifts the plan to the down-tail (let the bear put spread run).
5. **Front-IV / VRP** — confirm the 7/24 IV actually decays (thesis for the condor); if front IV stays elevated, a real second catalyst is being priced — re-underwrite.

## Citations summary (phase-10 spot-check)

1. `[MACRO:OpenAI_Presence]` — OpenAI "Presence" launch 2026-07-22 drove the −13% (phase-6).
2. `[FUND:MSPR]` — sustained insider selling, MSPR ≈ −100 most months, −9.6M sh Mar-2026 (phase-7b).
3. `[SENT:short_float]` — crowded short ~13–32% of float, DTC 2.6–4.3 (phase-7c).
4. `[STRUCT:dex]` / `[STRUCT:max_pain]` — long-gamma DEX bid + max-pain $11–11.5 range gravity (phase-4).
5. `[HIST:signal_backtest]` — bearish_flow win-rate 0.10 (n=10) → negative Kelly (phase-5).
