# Phase A0 — Intake & Reuse Detection

**Ticker:** FSLR
**As-of date:** 2026-06-21 (US/Eastern)
**Version:** v1 (no prior `trade-plan.md` in `trade-plans/FSLR/2026-06-21/`)

> *For research and educational use only. Not financial advice. Sizing,
> structures, targets and dates are illustrative.*

## Inputs

- **Ticker:** FSLR — valid (`^[A-Z][A-Z0-9.]{0,5}$`), US-listed equity (First Solar).
- **As-of:** 2026-06-21 (default = today). All look-backs `<= as_of`.
- **Book-risk overrides:** none → defaults (fractional Kelly 0.25, cap 5%).

## Reuse detection — deep dive FOUND (but STALE)

- **Path:** `research/FSLR/2026-05-18/` (data anchor 2026-05-15).
- **decision.json:** **ABSENT** — this run uses the older phase-MD convention.
  Substrate reused from `phase-9-trade-plan.md` (the blueprint) + `phase-10-audit.md`
  (confluence 67/100, bias MATCH), plus phase-1…phase-8 MDs on demand.
- **Age:** 2026-05-18 → 2026-06-21 = **34 calendar days ≈ 23 trading days**.
  **> 10 trading days → STALE.** Flag set.
  - **Consequence (L-0003):** cut conviction one bin in A3; treat flow/positioning
    as **directional context, not a live edge**; A1 lists "refresh flow" as an
    `important` gap; recommend a fresh `/stock-deep-dive FSLR` before full size.
- **`flow_source` = `deep_dive` (stale).** Did NOT pull a fresh live `uw` snapshot
  at intake — A1 will decide which specific gaps justify a targeted live pull.

### Reused deep-dive blueprint (2026-05-18) — headline numbers

| Field | Value (as of 2026-05-15 anchor) |
|-------|--------------------------------|
| Bias / conviction | **LONG / 0.75** (confluence 67/100, band 65–79) |
| Spot then | $234.48 close 2026-05-15 [STRUCT:gex] |
| Dealer structure | Total GEX **+$452M POSITIVE**; ZGL **$121.35**; **$250 = +$228M** magnet; $240 = +$142M wall; DEX +$18.33B (dealers BUY underlying) [STRUCT:gex/dex] |
| Flow campaign | Two-tenor **$280C** build (Dec-2026 +434 OI; Mar-2027 280C $1.39M ask, vol/OI 10×, Δ0.48) [FLOW] |
| Dominant catalyst | **Section 232 polysilicon tariff** — presidential window "through ~late June 2026"; FSLR = largest US CdTe (non-poly) maker → near-pure tailwind [MACRO] |
| Support ladder | $219.95 (block floor) / $231.62 (largest DP cluster) / $234.5–235.8 (acceptance) [DP] |
| Resistance ladder | $237 / $240 / **$250 magnet** / **$280** LEAP ceiling [STRUCT/DP] |
| Invalidation | **2 consecutive closes < $230**; OR conviction-matrix → DIRECTIONAL_SHORT; OR Sec 232 NO-TARIFF (exit same-day) |
| Sizing then | Kelly p0.75 × b0.71 × 0.25 frac = 9.95% → cap 5% → **final 3.0%** (TRANSITIONAL regime half-size + 26.3% bullish-flow backtest) |

## Price action SINCE the deep dive (what changed) — chart-engine smoke read

- **Spot now: $257.70** vs $234.48 anchor → **+9.9%**. The deep dive's $250 gamma
  magnet has been **reached and exceeded** (intraday high region implied by
  sma20=$278.12 — price ran toward the $280 LEAP ceiling, then pulled back).
- **Short-term posture is a PULLBACK inside an uptrend:** price `< ema9 (266.3)`,
  `< ema21 (265.3)`, `< sma20 (278.1)` — but `> sma50 (236.7)` and `> sma200 (233.3)`.
  `ma_stack = mixed`. RSI14 48.5 (neutral). **MACD hist −5.99 (bearish)** — momentum
  rolled over off the highs. ATR% **6.77%** (high — wide stops needed).
- **Implication for the reused thesis:** the LONG was a *catalyst-anticipation*
  trade into Sec 232; price has since run ~+10% toward the $280 target zone and
  is now retracing. A1 must ask: **did the Section 232 decision land, and is the
  catalyst now spent / priced in?** This materially conditions whether the reused
  LONG is still a fresh entry or a finished move.

## Reasoning ledger — loaded, lessons threaded into A3/A4

`trade-plans/_eval/reasoning-ledger.md` loaded. Lessons matched to this setup:

| id | status | relevance to FSLR 2026-06-21 | applied where |
|----|--------|------------------------------|---------------|
| **L-0003** | ACTIVE | **Direct hit** — reused dive is 23 trading days stale → cut conviction one bin; flow = context not edge; recommend refresh. | A3 conviction, A1 gap |
| **L-0001** | ACTIVE | Likely relevant — chart shows a possible pullback/continuation pattern; if a CHART-LEADS break sets up, require close-beyond + >1.2× vol, size starter. | A3 entry style, A4 sizing |
| **L-0002** | ACTIVE | On watch — stale bullish flow vs a bearish-MACD pullback could read DIVERGENT; if so, default NEUTRAL/RANGE or defined-risk fade, not full directional. | A3 bias/conviction |
| L-0004 | CANDIDATE | Not directly applicable (FSLR is long-gamma, not short-gamma; no bearish-sweep campaign) but its "respect the catalyst + veto" logic informs A3. | A3 (informational) |

## Chart source probe

- `chart_engine.py --ticker FSLR --date 2026-06-21` → **`available: true`**,
  `source = yfinance` ("371 daily sessions"). Exit 0. **B1 not a gap.**

## Verdict for downstream

- `deep_dive_reused` = **true** (`research/FSLR/2026-05-18/`, phase-MD convention, no decision.json)
- `deep_dive_age_days` = **34 cal / ~23 trading → STALE**
- `flow_source` = **deep_dive (stale)**
- `chart_source` = **yfinance (available)**
- `ledger_lessons` = **L-0003 (apply), L-0001 (apply if break setup), L-0002 (apply if divergent), L-0004 (informational)**
- **Top question handed to A1:** has the Section 232 catalyst resolved, and has the
  +10% run already monetized the reused thesis? → drives whether this is a fresh
  LONG, a take-profit/neutral, or a new chart-led setup.
