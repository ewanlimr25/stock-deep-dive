# Phase 9 — Trade Blueprint

**Ticker:** OKLO
**As-of date:** 2026-07-17
**PM voice:** desk PM running an institutional book
**Spot reference:** $41.11 (phase-0.5 close / phase-2 vwap $41.09)
**Upstream phases cited:** phase-0.5 through phase-8b

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

OKLO is in a mechanically-reinforced downtrend: a 5-session bearish sweep campaign
($41,004,637, consistency_score 1) [FLOW:sweep_persistence] sits on top of a −37% / 30-session
price collapse with `bearish_flow` backtesting 100% (n=10, avg −5.22%) [HIST:signal_backtest]
and a confirmed fundamental de-rating — 3 of 4 quarters missed EPS, insiders selling 11/12
months (MSPR −90.4) [FUND:mspr] — into a TRANSITIONAL, "half-size / defined-risk" regime
[MACRO:MarketRegime]. Dealer structure is FULLY_NEGATIVE gamma with dealers net-short-puts
selling underlying to hedge [STRUCT:dex], so any break lower is amplified. **But this is a
crowded 19.3%-float short on a cash-rich company at its 52-week low with still-bullish analysts
and a primed positive-vanna up-squeeze into 08-10 earnings** [SENT:short_float] — so the trade
is a *defined-risk, half-size, exit-before-earnings* short, not a naked one.

## Bias + conviction + horizon

- **Directional bias:** SHORT (plurality of phases 1–8: 5-of-5 desk agents SHORT)
- **Conviction (M-01 bin):** **0.65**
- **Time horizon:** 1-4w (exit/hedge before 2026-08-10 earnings)
- **Why this bin:** phase-10 confluence estimated ~68 (0.75 band), but I deliberately down-bin
  to 0.65 — see `## Conviction deviation`.

## Conviction deviation

Raw confluence lands ~68 (0.75 band per `rubrics/confluence-scoring.md`), but I set conviction
at **0.65 (downward)**. Justification (downward deviation is always permitted, and warranted
here): phase-8 desk average conviction was **2.2/5**; the phase-8b debate residuals were
**close (bull-short 0.65 vs bear 0.55)**; phase-7c is **CROWDED_SHORT + CAUTION**; and
phase-0.5 tagged the day **BUSY_NAME_NORMAL_DAY**. Narrative confidence is moderate, not high.

## Entry zones

| Entry type | Price | Trigger condition | Source |
|---|---|---|---|
| **Primary** | **$44–$46** | sell strength — rejection at the 5-day DP supply shelf / max-pain approach (better R/R than chasing the low) | [DP:price_levels] $45.5–$46.2 |
| **Aggressive** | **< $40** | daily close below the $40 put_wall_support → continuation into the $35 magnet (chases; worse fill, higher squeeze-recovery risk) | [OI:oi_by_strike] |
| **Fade (plan B)** | **> $46.20 close** | if the DP shelf is reclaimed and/or IV30d crushes < ~75% firing the vanna squeeze → flip to a small long/call-spread targeting the $47–50 max-pain magnet | [STRUCT:vanna_charm], [STRUCT:max_pain] |

## Levels to watch

| Type | Level | Source |
|---|---|---|
| Support (near) | **$40** (put_wall_support, −2.7%) | [OI:oi_by_strike] |
| Support (magnet) | **$35** (heaviest put wall 12,227 OI + most-negative GEX −851K) → then 52w low **$39.53** | [OI:oi_by_strike], [STRUCT:gex], [FUND:52w] |
| Resistance (near) | **$45.5–$46.2** (5-day DP supply shelf, ~$40M) | [DP:price_levels] |
| Resistance (ceiling) | **$47–$50** (max-pain 07-24/07-31 + $50 call wall) | [STRUCT:max_pain], [OI:oi_by_strike] |
| Gamma flip | **ZGL null** → spot in a wholly short-gamma zone (no dampening cushion) | [STRUCT:gex] |
| Largest pin (upside magnet) | **$47** (07-24) / $48 (07-17) — above spot | [STRUCT:max_pain] |

## Invalidation

- **Price-based:** two daily closes **above $46.20** (reclaims the 07-16 gap-down / DP supply
  shelf) → thesis broken; hard-stop the directional structures. [DP:price_levels]
- **Signal-based:** **GEX flips out of FULLY_NEGATIVE / DEX turns net-positive** on the phase-4
  daily refresh **while spot rallies** (dealers stop selling → amplification reverses up); OR
  sweep-persistence flips from bearish to bullish (consistency drops). [STRUCT:gex], [FLOW:sweep_persistence]
- **Macro-based:** a **milestone/regulatory/DOE-loan reaffirmation** for OKLO, or a nuclear-theme
  risk-on rotation *back into OKLO* (sector flow flips OKLO to a leader) — either can fire the
  squeeze; also the **2026-08-10 earnings** binary (be flat/hedged before it). [MACRO:OKLO], [SENT:recom]

## Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** p_raw = **1.00** (`bearish_flow` win_rate, n=10, source=backtest)
  → N-cap (10≤n<20) = 0.85 → **p = 0.85** [HIST:signal_backtest]
- **Kelly inputs:** b = **1.20** (short: entry $41.11 / target $35 / stop $46.20 →
  |41.11−35|/|46.20−41.11| = 6.11/5.09), fraction = 0.25, cap_pct = 5
- **Raw Kelly:** (0.85×1.20 − 0.15)/1.20 = **0.725** → suggested = min(0.725×0.25×100, 5) = **5%**
  · **Win-rate map ceiling:** p 0.85 ≥ 0.70 → **full** (≤ cap_pct)
- **Risk gates:**
  - Fundamentals (phase-7b): **CONFIRM** (fundamentals confirm the short) → **no-op**
  - **Sentiment/crowd (phase-7c): CAUTION + CROWDED_SHORT (19.3% float) → cut one step (full → half = 2.5%)**
  - Correlation cluster (phase-6/8): **none** (only OKLO blueprinted 2026-07-17) → no-op
  - Sector rotation (phase-6): Utilities weak/laggard = *aligned* with the short (not adverse) → no-op
  - Debate (phase-8b): bull_residual **0.65** vs bear_residual **0.55** → **not disconfirmed** → no-op
  - **Context modifier (phase-0.5): BUSY_NAME_NORMAL_DAY** → do not size at top of band → trim below 2.5%
- **Final size:** **2.0%** of book risk (defined-risk max-loss), i.e. the half-step (2.5%)
  trimmed for the BUSY_NAME_NORMAL_DAY context and the qualitative squeeze caution.
- **Deviation reason:** none (final < suggested — always permitted; no upward deviation).

## Option structures

> IV30d ~97.5%, IV rank 76th pctile, **VRP +0.28 (PREMIUM_SELLING — long naked premium
> overpays ~28 vol points)** [HIST:vrp]. IV-implied move to 08-10 earnings ≈ **±23–25%**
> (the screener implied_move_perc ±0.73% is a near-dated artifact — not used). Both structures
> **expire 2026-08-07, before the 08-10 earnings** — deliberately out of the binary gap +
> post-earnings IV crush. Debit/credit are **illustrative estimates at ~97% IV**, to be
> confirmed against the live chain.

### Directional (primary)

- **Structure:** put **debit** spread (defined-risk; avoids the rich-IV overpay of a naked put)
- **Strike(s) / expiry:** **buy $40 put / sell $34 put, exp 2026-08-07**
- **Debit/credit:** ~**$2.30 debit** per spread (est.)
- **Breakeven:** ~**$37.70**
- **Max loss:** ~**$2.30** (the debit) per spread; sized so aggregate max-loss ≤ 2.0% of book
- **Why this structure:** long strike at the $40 put_wall_support, short strike straddling the
  heavy $35 wall / fresh $33 put — captures the move into the OI magnet within the ±23% priced
  move; a *spread* (not a naked put) because VRP +0.28 makes long premium expensive and caps the
  19%-float squeeze loss. At target $35 the spread is ~$5 value → ~+$2.70 vs $2.30 risk (b≈1.17).

### Defined-risk alternative

- **Structure:** bear **call credit** spread (monetizes the rich IV / PREMIUM_SELLING regime)
- **Strike(s) / expiry:** **sell $47 call / buy $52 call, exp 2026-08-07**
- **Debit/credit:** ~**$1.00 credit** per spread (est.)
- **Breakeven:** ~**$48.00**
- **Max loss:** ~**$4.00** (width $5 − credit $1) per spread; profits if OKLO stays below $47
- **Note:** short strike above the $45.5–46.2 DP shelf and below the $47–50 max-pain ceiling;
  collects premium on a name that can't easily reclaim $47 pre-earnings. **Caveat:** FULLY_NEGATIVE
  GEX amplifies an up-squeeze — the $52 long cap is the protection; size to max-loss ≤ 2.0% of book.

## Macro overlay (cite phase-6)

- **Tailwinds (for the short):** [MACRO:MarketRegime] TRANSITIONAL, breadth 38.4% bullish,
  "half-size/defined-risk"; [MACRO:DGS10] 10y 4.57% pressures a zero-cash-flow duration name;
  [MACRO:sector_flow] Utilities 10/11, −$138M outflow on the 07-16 break day.
- **Headwinds (against the short):** [MACRO:DFF] Fed cutting (3.63%) = mild risk-on support;
  nuclear-theme bullish headlines (ARK) can rotate back to OKLO.
- **Net:** net headwind for OKLO = **tailwind for the short** (mild-to-moderate).

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|---|---|---|
| 2026-08-10 | **OKLO earnings** (pre-revenue; milestone/guidance) | ? (binary; ~±25% priced; **squeeze risk** — be flat/hedged before) |
| late-Jul → Aug | dilution / capital-raise headlines | − (headwind, aligned with short) |
| post-OPEX (this week) | IV crush | ? (could fire the vanna squeeze up — watch IV30d vs ~75%) |

## Post-trade monitoring checklist

- [ ] Re-run `uw options-structure gex/dex` daily — **exit if GEX leaves FULLY_NEGATIVE or DEX
      turns net-positive while spot rallies** (amplification reversing up).
- [ ] Re-check `uw hot-chains sweep-persistence` — thesis anchor; exit if it flips bullish.
- [ ] Watch **IV30d vs ~75%** — a post-OPEX crush below it fires the positive-vanna dealer buy-back → squeeze.
- [ ] Track the **$46.20** line (two daily closes above = hard stop) and the next semi-monthly
      **short-interest print** (a fresh SI build = escalating squeeze risk).
- [ ] Be **flat or fully hedged before 2026-08-10 earnings** — do not hold naked directional risk into the print.

## Citations summary

1. [FLOW:sweep_persistence] OKLO bearish-dominant 5/5 sessions, consistency_score 1, $41,004,637 — phase-1-flow.md §Sweep persistence
2. [HIST:signal_backtest] bearish_flow win_rate 1.00 (n=10, avg −5.22%) — phase-5-historical.md §Signal backtest
3. [FUND:mspr] insider MSPR negative 11/12 months, −90.4 latest — phase-7b-fundamentals.md §Insider signal
4. [STRUCT:dex] net DEX −167M, "dealers net short puts → hedge is to SELL underlying" — phase-4-structure.md §DEX
5. [SENT:short_float] 19.29% of float short (2026-06-15), DTC 2.6 — phase-7c-sentiment.md §Short interest
