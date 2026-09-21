# Phase 9 — Trade Blueprint

**Ticker:** GOOG
**As-of date:** 2026-07-23
**PM voice:** desk PM running an institutional options-overlay book
**Spot reference:** $318.34 (phase-2/screener close)
**Upstream phases cited:** phase-0.5 through phase-8b

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

GOOG's −7% on 2026-07-23 is a **capex-timing overshoot, not a franchise break**: a
+24%-revenue / +82%-Cloud quarter re-rated on a $195–205B capex guide `[FUND:capex]`,
into a **2.2σ crowded-short** options tape (P/C z +2.21, BEARISH_EXTREME
`[HIST:pc_ratio_zscore]`) that phase-7b explicitly VETOed shorting `[FUND:tier_adjustment]`.
Dealers are **long-gamma** (ZGL 187.5 ≪ spot) with **max pain at 350** ~10% above spot
`[STRUCT:max_pain]`, and with the earnings binary now cleared the front-end
backwardation should crush and mechanically bid the underlying — so the desk's read
(4 agents, **zero SHORT**, avg conviction 2.25 `[AGENT:phase-8]`) is a **small,
defined-risk mean-reversion long / range play**, capped hard by $1.9B of overhead
dark-pool supply at 341–346 `[DP:price_levels]`.

## Bias + conviction + horizon

- **Directional bias:** LONG (mean-reversion) / RANGE — the tradeable expression of the
  phase-8 plurality; **no short** (7b VETO + 7c crowded-short + no bearish OI campaign).
- **Conviction (M-01 bin):** **0.55** (slight edge — coin-flip plus a sliver).
- **Time horizon:** 1–5d for the bounce; up to 1–4w for the range.
- **Why this bin:** UW composite is explicitly MIXED at 2.9% confidence
  `[INSIGHT:conviction_matrix]`, GOOG scores <1 on both bull/bear confluence, the
  debate held only 0.65 vs 0.55, and the backtested signal (bearish_flow) is the
  *opposite* direction to the trade — this is a low-confluence, tactical fade, not a
  conviction call. (Phase-10 to confirm the band; expected low.)

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| Primary | $315–318 | Hold above the 310 put-wall on a retest + first up-day / IV starting to crush | `[OI:oi_by_strike]` `[STRUCT:vanna_charm]` |
| Aggressive | $312–314 | Deeper flush into the 310 put-wall that long-gamma dealers defend (buy the dip) | `[STRUCT:gex]` `[OI:oi_by_strike]` |
| Fade (plan B) | close < $310 | Thesis partially breaks — stand aside or buy 300 puts toward the LEAP-put strike | `[DP:price_levels]` `[OI:oi_by_strike]` |

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Support | $310 (put_wall_support, net_oi −11,210) | `[OI:oi_by_strike]` |
| Support (hard floor) | $300 (put_wall_support / LEAP-put strike) | `[OI:oi_by_strike]` `[FLOW:top_premium_trades]` |
| Resistance | $341–346 (5-day DP supply, $1.9B) | `[DP:price_levels]` |
| Resistance | $350 (call_wall_resistance, all-exp OI 45,361) | `[OI:oi_by_strike]` |
| Gamma flip (ZGL) | $187.5 (far below → long-gamma; practical flip-watch = close < 310) | `[STRUCT:gex]` |
| Largest pin (max-pain) | $350 (07-24→08-14), $365 (08-21) — native, not eyeballed | `[STRUCT:max_pain]` |

*Price-context color:* `fz` RSI/52-week fields were null this run (mega-cap gap), so no
`[HIST:rsi fz]` overlay — but on UW data GOOG sits mid its 52w band ($187–409) ~22% off
the high, freshly broken down; treat the primary entry as knife-catch-adjacent and
prefer the aggressive dip-buy at the 310 wall.

## Invalidation

- **Price-based:** a daily **close below $310** (loses put-wall support); **hard stop at
  $300** (LEAP put wall). On the upside, a close above **$350** exits the range framing —
  take profits into the 341–346 supply, do not chase a breakout.
- **Signal-based:** **GEX flips NEGATIVE** (phase-5: 7 flips/30d instability) → dealers
  sell dips, the mean-reversion floor is gone; OR `sweep_persistence` flips from "mixed"
  to clean one-directional bearish `[FLOW:sweep_persistence]`; OR P/C z normalizes off
  +2.2 with no bounce (crowded-short thesis spent) `[HIST:pc_ratio_zscore]`.
- **Macro-based:** a **hawkish FOMC surprise 2026-07-29** (rate-hike signal) extends
  risk-off `[MACRO:FOMC_2026-07-29]`; OR a wave of post-guidance **analyst downgrades on
  capex** (phase-7c blind spot) validates the bears `[SENT:recommendation]`.

## Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** phase-5 `signal_backtest_win_rate` = 0.857 (n=7,
  source=backtest) — **but for `bearish_flow`, the OPPOSITE direction to this long**, so
  it is **not** a valid `p` for the trade. `win_rate_source` is inapplicable to the
  traded direction → **fall back to the conviction bin, capped at 0.65** → **p = 0.55**.
  `[HIST:signal_backtest]`
  - (The bearish_flow base rate is instead carried as a *risk*: the tape has historically
    continued down after bearish flow — a reason to keep the long tiny and defined-risk.)
- **Kelly inputs:** entry 318, target 340, stop 308 → b = 22/10 = **2.2**; fraction 0.25;
  cap_pct 5.
- **Raw Kelly:** (0.55×2.2 − 0.45)/2.2 = **0.345** → ×0.25×100 = 8.6% → capped at 5%.
  **Win-rate map ceiling:** p 0.55 ∈ [0.50,0.70] → **half** = ≤ 2.5%. Take the smaller →
  **2.5%**.
- **Risk gates:**
  - Fundamentals (phase-7b): tier_adjustment VETO — but of the *short*; for the LONG
    fundamental_signal is BULLISH → **CONFIRM-equivalent, no cut**.
  - Sentiment/crowd (phase-7c): CAUTION + crowd_state CROWDED_SHORT — crowd is offside to
    the long (supportive), but near-term news/macro is hostile and analyst revisions are a
    blind spot → **apply CAUTION, cut one step** (2.5% → starter ~1.25%).
  - Correlation cluster (phase-6): none (GOOG only 2026-07-23 blueprint) → **no-op**.
  - Sector rotation (phase-6): NEUTRAL (today's Comm-Services outflow is GOOG's own print;
    5-day trend INFLOW) → **no-op**.
  - Debate (phase-8b): bull_residual 0.65 vs bear_residual 0.55 → **not disconfirmed,
    no-op** (but narrow → keep size low).
  - Context (phase-0.5): GENUINELY_UNUSUAL → no-op (the unusualness was *bearish*; we fade
    it, so no top-of-band size).
- **Final size:** **1.25% of book risk** (starter). Capped at 5%; well under.
- **Deviation reason:** none (no upward deviation; a gate fired).

## Option structures

### Directional (primary)

- **Structure:** call debit spread (long premium — favored by phase-5 **VRP −0.073 /
  PREMIUM_BUYING**, vol cheap vs realized 39.7%).
- **Strike(s) / expiry:** **long 320C / short 340C, exp 2026-08-21** (29 DTE, past FOMC).
- **Debit/credit:** ~$7.0 debit (illustrative; IV ~33%).
- **Breakeven:** ~$327.
- **Max loss:** ~$7.0/contract (= the debit).
- **Why this structure:** 320 = spot/pivot and the 0DTE-scalp cluster `[OI:oi_by_strike]`;
  340 sits at the base of the 341–346 DP supply `[DP:price_levels]` / below the 350 call
  wall, so the target is *achievable* within the mean-reversion, not a breakout bet.
  Targets +6.8% ≈ 1.3× the ~4-week expected move (front-expiry 1.57% `[CTX:implied_move]`
  scaled) — reasonable, not rich.

### Defined-risk alternative

- **Structure:** put credit spread — **sells the 2.2σ-crowded, complacent-skew puts** at
  the dealer-defended wall.
- **Strike(s) / expiry:** **short 310P / long 300P, exp 2026-08-21**.
- **Debit/credit:** ~$3.0 **credit** (illustrative).
- **Breakeven:** ~$307.
- **Max loss:** ~$7.0/contract (width 10 − credit 3).
- Profits if GOOG holds above 310 (put_wall_support) into Aug-21; the long 300P caps risk
  exactly at the hard invalidation `[OI:oi_by_strike]`. A single-catalyst FOMC gap of the
  expected-move size (~±1.6–3%) does **not** breach the 300 stop.

*Both structures sized so aggregate max-loss ≤ 1.25% of book risk.*

## Macro overlay (cite phase-6)

- **Tailwinds:**
  - Earnings binary cleared → IV crush + vanna-buy mechanics `[MACRO:earnings_passed]` `[STRUCT:vanna_charm]`
  - Comm-Services 5-day trend still INFLOW; today's outflow is idiosyncratic `[MACRO:sector_flow_persistence]`
- **Headwinds:**
  - Regime TRANSITIONAL/risk-off, breadth 31.9% bullish, "half size, defined-risk" `[MACRO:MarketRegime_2026-07-23]`
  - 10y at 4.67% (rising) pressures long-duration multiples `[MACRO:DGS10_2026-07-22]`
  - FOMC 2026-07-29 inside the window `[MACRO:FOMC_2026-07-29]`
- **Net:** **mixed-to-mild-headwind** — macro is secondary; the trade is idiosyncratic
  mean-reversion, so size stays small and defined-risk.

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|------|-------|------------------|
| 2026-07-29 | FOMC (no SEP), hold 3.50–3.75% expected | ? (hawkish surprise = −) |
| 2026-08 (monthly) | CPI / PCE / NFP | ? (data-dependent) |
| 2026-11-04 | GOOG Q3 earnings | **outside window** (no single-name binary here) |

## Post-trade monitoring checklist

- [ ] Re-check phase-4 **GEX regime daily** — a flip to NEGATIVE kills the long-gamma
  floor and triggers signal-based invalidation.
- [ ] Watch the **310 put-wall** on every close — a daily close below = price invalidation.
- [ ] Re-run phase-1 **sweep_persistence** — a flip from "mixed" to clean bearish = bears
  organizing; exit.
- [ ] Track **post-guidance analyst revisions** (the phase-7c blind spot) — a downgrade
  wave on capex validates the bear.
- [ ] **FOMC 2026-07-29** — flatten or defend the spread into the print; do not carry a
  hawkish-surprise gap naked.
- [ ] Watch for **IV normalization** (backwardation → contango) confirming the vanna-buy
  tailwind; if IV stays elevated, the mean-reversion mechanic is not engaging.

## Citations summary

1. `[FUND:capex]` — 2026 capex guide $195–205B + first negative FCF = the −7% de-rate
   cause on a +24% rev / +82% Cloud quarter — phase-7b-fundamentals.md §Summary/Cash-flow.
2. `[HIST:pc_ratio_zscore]` — P/C z +2.21 (BEARISH_EXTREME; 0.71 vs 20d mean 0.46) —
   phase-5-historical.md §P/C ratio z-score.
3. `[STRUCT:max_pain]` — max pain 350 (07-24→08-14), 365 (08-21), ~10–15% above spot —
   phase-4-structure.md §Max pain.
4. `[DP:price_levels]` — 5-day overhead DP supply $1.14B @341.91 + $797M @346.19 —
   phase-2-dark-pool.md §Price levels.
5. `[AGENT:phase-8]` — 4 desk agents, zero SHORT, avg conviction 2.25 —
   phase-8-agent-views.md §Verdict.
