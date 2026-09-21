# Phase 9 — Trade Blueprint

**Ticker:** INTC
**As-of date:** 2026-06-26
**PM voice:** desk PM running an institutional options-overlay book
**Spot reference:** $128.3 (phase-2 DP avg $128.67 / fz close $128.32 / OI ref $127.67)
**Upstream phases cited:** phase-0.5 through phase-8b

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

INTC is a +247.75% YTD parabola — the **only loss-maker in its peer group, trading 29–33%
above the $102.70 analyst target** `[FUND:peer_pe fz]` — where the options tape has turned
against the price: a **price-vs-flow bearish DIVERGENCE (+10.7% price / −$50.9M flow)**
`[INSIGHT:price_vs_flow]`, a **5-of-5-session bearish sweep campaign** ($925.2M, consistency
1.0) `[FLOW:sweep_persistence]`, and **~73% bearish new OI led by a Jul-17 $130 put build
(+11,442, ratio 4.11)** `[OI:biggest_increases]` into a **hawkish-Fed / tech-outflow macro**
`[MACRO:sector_rotation]`. But the directional short is **fundamentally VETOED** — four
straight earnings beats, insiders net-buying, and a long-gamma dealer pin make a naked fade a
widow-maker `[FUND:earnings_surprise]` — so this resolves to a **watch-only directional bias**,
expressed (if at all) only as a **small, defined-risk spread toward the $120 pin that expires
before the Jul-23 print.**

## Bias + conviction + horizon

- **Directional bias:** SHORT (tactical range-fade, not a directional short)
- **Conviction (M-01 bin):** **0.55**
- **Time horizon:** 1-4w (work to Jul-17 OPEX; flat before Jul-23 earnings)
- **Why this bin:** estimated phase-10 confluence ≈ **55** (band → 0.65), but the **phase-8b
  disconfirmation gate down-shifts one bin → 0.55**; the bearish lane is real but gated by a
  7b VETO + 7c CAUTION + a tied debate. (Phase-10 will formalize; this is a downward move, no
  upward-deviation note required.)

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| Primary    | $130–132 | **Rejection at the $130 call wall / gamma lid** (sell into strength) | `[OI:oi_by_strike]` / `[STRUCT:gex]` |
| Aggressive | $127.5 | Break/close below the $128 local **negative-gamma notch** + loss of the $128.32 DP shelf with momentum | `[STRUCT:gex]` / `[DP:price_levels]` |
| Fade (plan B) | $133+ | **Reclaim of $133** (thesis partial-invalidation) → counter-trade small toward the $140.94 supply | `[DP:price_levels]` |

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Support (target) | **$120** (gamma pin +5.34M + Jul-02 max-pain + call_heavy floor); nearer **$125** (pin + 0DTE max-pain) | `[STRUCT:gex]` / `[STRUCT:max_pain]` / `[OI:oi_by_strike]` |
| Resistance (lid) | **$130** (call wall +14,942 net_oi + gamma pin +4.16M); then **$132–133** band, **$140.94** supply / **$141.45** 52W high | `[OI:oi_by_strike]` / `[DP:price_levels]` |
| Gamma flip (ZGL) | **$27.26** (far below — no near-term flip; spot deeply long-gamma); 0DTE ZGL $55.06 | `[STRUCT:gex]` |
| Pin magnet | **$125 → $120** (near-expiry max-pain pull) | `[STRUCT:max_pain]` |

**Price-context color (advisory):** entering near the 52-week high ($141.45, −9.3%) with
**RSI 56.8 (neutral, not overbought)** `[HIST:rsi fz]` after a +29% V-bounce off $99 — the
chase risk is real and argues for the *primary (sell-into-$130-strength)* entry over the
aggressive break-down entry. Color only; does not change `p` or size.

## Invalidation

- **Price-based:** **two daily closes above $133** (clears the $130 call wall / gamma lid AND
  the $132–133 dark-pool supply band) → fade negated `[DP:price_levels][OI:oi_by_strike]`.
- **Signal-based:** **conviction-matrix flips COVERED_CALL → DIRECTIONAL_LONG**
  `[INSIGHT:conviction_matrix]`, OR **cumulative premium flow turns net-bullish 3 consecutive
  sessions** `[HIST:cumulative_premium_flow]` (it is already MIXED/balanced — a clean bullish
  flip kills the divergence), OR the **5/5 bearish sweep persistence breaks** below consistency
  `[FLOW:sweep_persistence]`.
- **Macro-based:** a **dovish June-CPI surprise (~Jul-14/15)** that relieves the hawkish-Fed
  tech pressure `[MACRO:CPIAUCSL_2026-05]`, OR **semis sector flips to net inflow**
  `[MACRO:sector_rotation]`, OR a positive AI-capex/sector catalyst.
- **Structural (hard):** **holding through Jul-23 earnings is itself invalidation** — the 4/4
  beat streak + +45.76% fwd EPS make the binary un-shortable `[FUND:earnings_surprise]`.
  **Exit/expire before Jul-23.**
- **Exit rule:** **hard stop** on the directional debit spread (close 100% on a daily close
  > $133); the credit spread is **rolled or closed** at $133, never held into earnings.

## Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** `p_raw = 0.667` (phase-5 `bearish_flow` win-rate, n=**9**,
  source=**backtest**) → N-cap (n<10 → 0.75) → **capped p = 0.667** `[HIST:signal_backtest]`.
  (Market-wide base rate, in-sample, "not a robust live edge" — treat as soft.)
- **Kelly inputs:** entry $128.3, target $120, stop $133 → **b = 8.3/4.7 = 1.77**, fraction
  0.25, cap_pct 5.
- **Raw Kelly:** (0.667·1.77 − 0.333)/1.77 = **0.48** → suggested = min(0.48·0.25·100, 5) =
  **5.0%**. **Win-rate map ceiling:** p 0.667 ∈ [0.50, 0.70] → **half (≤2.5%)** → take the
  smaller = **2.5% pre-gate**.
- **Risk gates (each cuts only):**
  - **Fundamentals (7b): `VETO`** → **directional naked size = 0% / WATCH-ONLY**; defined-risk
    structures permitted "carry only, fundamentals-vetoed."
  - **Sentiment/crowd (7c): `CAUTION`** (crowd_state CROWDED_LONG, no squeeze base) → **cut one
    step** (half → starter).
  - **Correlation (6/8): none** — INTC is the only blueprint for the date; INTC/MU ρ0.954 is a
    soft-watch context flag, **no concurrent-position cut**.
  - **Sector rotation (6): ALIGNED with the short** (tech −$637.8M outflow is *with* the bearish
    direction) → **no cut** (persistence score itself was an unusable placeholder).
  - **Debate (8b): DISCONFIRMED** — bull_residual **0.65** vs bear_residual **0.65** (tie ⇒
    attacker ≥ defender) → **down-shift bin one (0.65→0.55) + cut one step**.
  - **Context (0.5):** `unusual_verdict = GENUINELY_UNUSUAL` → no-op (edge already in `p`); but
    the unusualness is *direction/premium*, not volume — do not size on magnitude.
- **Final size:** **directional (naked) = 0% — WATCH-ONLY** (7b VETO). **Defined-risk carry
  structures: max-loss ≤ 0.5% of book risk** (2.5% half → starter via 7c CAUTION → starter-of-
  starter via 8b disconfirm). 
- **Deviation reason:** none (no upward deviation; forbidden anyway — three gates fired).

## Option structures

Both are **defined-risk** (the 7b VETO disallows naked directional), both **expire Jul-17,
six days before the Jul-23 earnings**, and both sit **inside** the priced expected move
(±~22% to Jul-17), so neither is rich and neither carries the earnings gap. Carry only,
max-loss ≤ 0.5% of book.

### Directional (primary) — bear put **debit** spread

- **Structure:** buy Jul-17 **$128 put** / sell Jul-17 **$120 put** (long the ATM neg-gamma
  notch, short the $120 gamma-pin/max-pain target).
- **Strikes / expiry:** 128 / 120, **2026-07-17**.
- **Debit:** ≈ **$4.00** (est.; Jul-17 $130 put traded ~$11.05 `[OI:biggest_increases]`, so the
  $128/$120 spread ≈ $4 at 94% IV).
- **Breakeven:** ≈ **$124.00**.
- **Max loss:** **$4.00** (the debit; ≤0.5% of book in contract count).
- **Max value:** $8.00 at ≤$120 → ~1:1 payoff (the **IV tax** — high 94% IV makes even the
  spread pay modestly; that is *why* it is a spread, not a long put).
- **Why this structure:** at iv_rank 94 / IV ~94% a naked put is a vega trap `[HIST:iv_percentile_zscore]`;
  the spread sells the $120 put (the gamma-pin magnet) to fund the ATM put and caps the cost,
  targeting the exact `[STRUCT:max_pain]` / `[STRUCT:gex]` downside pin over the 1-4w horizon.

### Defined-risk alternative — bear **call credit** spread (premium-selling)

- **Structure:** sell Jul-17 **$135 call** / buy Jul-17 **$140 call** (sell the $135 call wall,
  cap at the $140 supply).
- **Strikes / expiry:** 135 / 140, **2026-07-17**.
- **Credit:** ≈ **$1.50** (est. at 94% IV).
- **Breakeven:** ≈ **$136.50**.
- **Max loss:** **$3.50** (width $5 − credit $1.5; ≤0.5% of book in contract count).
- **Why:** the **VRP +5.95 PREMIUM_SELLING** regime `[HIST:vrp]` rewards *selling* the rich IV;
  this monetizes the $135/$140 call walls `[OI:oi_by_strike]` (resistance the fade expects to
  hold) and profits on time + a drift/pin below $135 — the highest-probability expression given
  the long-gamma pin, without paying the IV tax.

## Macro overlay (cite phase-6)

- **Tailwinds (for the SHORT):**
  - `[MACRO:sector_rotation]` Technology = #1 directional outflow, −$637.8M.
  - `[MACRO:FOMC_2026-06-17]` hawkish Fed pivot (Warsh, dots → 3.8%, hike bias).
  - `[MACRO:CPIAUCSL_2026-05]` CPI +4.27% YoY — sticky inflation pressures high-multiple tech.
  - `[MACRO:semis_selloff]` $1.3T June semis selloff, memory crisis, smartphone −13%.
- **Headwinds (against the SHORT):**
  - `[MACRO:AI_demand]` AI secular boom intact (Deloitte +26% / $975B 2026).
  - `[MACRO:INTC_guide]` Q1 recovery + Q2 guide beat; `[FUND:earnings_surprise]` 4/4 beats.
- **Net:** macro is a **net tailwind for the short**, but it is sector-wide (the trade rides the
  semis/memory tape, ρ0.954 with MU) and is **gated by the fundamental/sentiment offsets** — the
  macro supports the *direction*, the gates cap the *size*.

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|------|-------|------------------|
| ~2026-07-14/15 | June CPI release | hot → short tailwind / soft → invalidation |
| **2026-07-17** | **Monthly OPEX** (structure expiry; $130 put build expires) | pin/de-gamma |
| **2026-07-23** | **INTC Q2 earnings** | **? — DO NOT hold through (4/4 beat squeeze risk)** |
| ~2026-07-28/29 | FOMC | hawkish-hold/hike → short tailwind |

## Post-trade monitoring checklist

- [ ] **Re-check the conviction-matrix daily** — a flip COVERED_CALL → DIRECTIONAL_LONG is the
  fastest signal-based invalidation `[INSIGHT:conviction_matrix]`.
- [ ] **Watch the $130 / $133 line** — two daily closes > $133 = hard stop on the debit spread,
  roll/close the credit spread `[OI:oi_by_strike]`.
- [ ] **Track cumulative premium flow** (phase-5) — net-bullish 3 sessions running = the
  divergence has resolved against the fade `[HIST:cumulative_premium_flow]`.
- [ ] **Monitor MU + the semis tape** (ρ0.954) — INTC is a semis-complex bet; a memory/AI
  re-rate up drags INTC with it `[MACRO:sector_rotation]`.
- [ ] **Hard calendar gate:** close/expire ALL structures **before 2026-07-23 earnings**.
- [ ] **Watch for fresh insider buys / new Pelosi-style headlines** — squeeze fuel `[SENT:news_2026-06-26]`.

## Citations summary

1. `[INSIGHT:price_vs_flow]` — bearish DIVERGENCE, price +10.7%/30d vs net flow −$50.9M (phase-7-insights.md §Price vs flow).
2. `[OI:biggest_increases]` — Jul-17 $130 put +11,442 OI (ratio 4.11); ~73% bearish new OI (phase-3-positioning.md §Largest OI increases / Smart positioning).
3. `[MACRO:sector_rotation]` — Technology #1 directional outflow −$637.8M (phase-6-macro.md §Sector rotation).
4. `[FUND:peer_pe fz]` — only loss-maker in peer group, +247.75% YTD, 29–33% above analyst targets (phase-7b-fundamentals.md §Valuation).
5. `[FLOW:sweep_persistence]` — 5/5-session bearish sweep campaign, $925.2M, consistency 1.0 (phase-1-flow.md §Key signals).
