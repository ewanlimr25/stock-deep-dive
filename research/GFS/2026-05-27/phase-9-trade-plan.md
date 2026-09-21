# Phase 9 — Trade Blueprint

**Ticker:** GFS
**As-of date:** 2026-05-27
**PM voice:** desk PM running an institutional options-overlay book
**Spot reference:** $81.11 (phase-2-dark-pool.md close / phase-0.5 self-history)
**Upstream phases cited:** phase-0.5 through phase-8b

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

GFS's 76%-owner Mubadala is distributing a **$1.91B / 22M-share block (~16.6% of
float), marketed $86.30–86.80 and settling 05-28** `[SENT:insider_block WebSearch:bloomberg.com]`,
into a name that ran **+87.5% above its 200-DMA / +132% YTD** `[HIST:52w_proximity fz]`
and just printed its first −9.7% red day — with dealers **short gamma below ZGL
$86.37** `[STRUCT:gex]` and **Technology the day's largest net outflow at −$433.5M**
`[MACRO:sector_rotation_2026-05-27 UW]`. This is a textbook post-parabolic fade with a
**hard, quadruple-stacked ceiling at $86–87** (block price ≈ ZGL ≈ gamma wall ≈ 52-wk
high) — but because the *business* is high-quality (4/4 earnings beats, fortress
balance sheet, fresh dividend/buyback) `[FUND:earnings_surprise]`, the play is **not a
naked short**: it is a small, defined-risk fade that **sells the complacent, rich call
premium into the overhang**, with a near-term horizon because the block-settlement
clears the acute supply.

## Bias + conviction + horizon

- **Directional bias:** **SHORT (fade)** — expressed defined-risk only (plurality of
  phases 1–8: 2 SHORT + 2 NEUTRAL-fade, **0 long**).
- **Conviction (M-01 bin):** **0.65**
- **Time horizon:** **1-5d** (the trade is the block-settlement window; bounce risk
  rises after 05-28).
- **Why this bin:** phase-10 confluence lands ~65 — the bearish stack (structure
  `++`, macro/flow/DP `+`) is dragged toward the boundary by the phase-7b fundamentals
  `--` veto; I take the **lower** of the boundary bins because the fundamental VETO of
  a naked short, the BUSY_NAME_NORMAL_DAY context cap, and the unrefuted post-settlement
  bounce risk all argue against pressing it.

### Conviction deviation

Confluence (~65) sits at the 0.65/0.75 boundary; I deviate **down** to 0.65 (allowed —
downward is always conservative). Reason: phase-7b `tier_adjustment = VETO` of the
naked directional short + phase-0.5 `BUSY_NAME_NORMAL_DAY` (don't size top-of-band) +
phase-8b `strongest_bear_point` (05-28 clearing → bounce, DTC 1.94 = no squeeze fuel).

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| Primary | **$84.5–86.5** | Rally into the stacked ceiling **fails** (rejection at block price ≈ ZGL) — best R:R | `[STRUCT:gex]` ZGL $86.37 / `[SENT:insider_block]` block $86.30–86.80 |
| Aggressive | **$80.0** | Break & hold below today's $80.72 mega-print value area (momentum continuation) | `[DP:price_levels]` |
| Fade (plan B counter) | **>$87.5** | Reclaim/hold above the ceiling → cover & flip to buy-the-dip on the quality floor | invalidation / `[FUND:target fz]` |

The aggressive short-from-spot has poor R:R (phase-8b bear point) — **prefer the
primary fade into $84–86**; that is where the payoff ratio works.

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Support | **$78.77**, then **$70.79** (pre-breakout base; $65 negative-GEX accelerant below) | `[DP:price_levels]`, `[STRUCT:gex]` |
| Resistance | **$86.37 (ZGL) / $86.30–86.80 (block)**, then **$91–92** ($83M DP supply / $92.55 52-wk high) | `[STRUCT:gex]`, `[SENT:insider_block]`, `[DP:price_levels]` |
| Gamma flip (ZGL) | **$86.37** (±2% → $84.7–88.1) | `[STRUCT:gex]` |
| Largest pin | **none** — no pin/OPEX cliff within the week (June OPEX 22d out) | `[OI:pin_risk]` |

**Price-context color (advisory):** RSI 62.8 — the −9.7% drop already relieved the
overbought peak, so this is *extended + first crack*, not an RSI-85 blow-off; entering
short at spot ($81, 12% below the $92.55 high) is mid-range — **prefer the fade entry
into $84–86**, not a chase of the breakdown `[HIST:rsi fz]`, `[HIST:52w_proximity fz]`.

## Invalidation

- **Price-based:** **two daily closes above $87** (clears the block/ZGL/gamma ceiling),
  OR an intraday reclaim of **$86.37 (ZGL)** that holds into the close — flips dealers
  long-gamma and the fade is dead `[STRUCT:gex]`, `[DP:price_levels]`.
- **Signal-based:** GEX regime flips to **POSITIVE / spot above ZGL** on the phase-4
  daily refresh, OR dark-pool buy_ratio turns strongly accumulative (**>0.65**)
  post-settlement, OR price-vs-flow **divergence resolves** (flow turns net bullish)
  `[INSIGHT:price_vs_flow]`, `[STRUCT:gex]`.
- **Macro-based:** **dovish FOMC surprise (~Jun 16–17)** or **cool May CPI (~Jun 10–11)**
  that reverses the tech rotation / re-risks semis, OR regime flips
  TRANSITIONAL → RISK-ON with tech net **inflows** `[MACRO:FOMCminutes_2026-05-20 WebSearch:cnbc.com]`,
  `[MACRO:sector_rotation_2026-05-27 UW]`.

**Exit on invalidation:** defined-risk structures → **hold to defined max-loss** (no
discretionary stop needed; loss is capped by construction). For the credit spread,
**close/roll** if spot closes above the $85 short strike with momentum (don't wait for
the long wing).

## Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** p_raw = **0.583** (n=**12**, source=**backtest**, signal
  class `bearish_flow`) → N-cap (10≤n<20 → 0.85) → **capped p = 0.583** `[HIST:signal_backtest]`.
- **Kelly inputs:** b = **2.0** (fade entry ~$84 → target ~$77, stop ~$87.5:
  7.0/3.5), fraction = 0.25, cap_pct = 5.
- **Raw Kelly:** (0.583×2.0 − 0.417)/2.0 = **0.375** → ×0.25×100 = 9.4% → Kelly-cap 5%.
  **Win-rate map ceiling:** p∈0.50–0.70 → **half (≤2.5%)** → take the smaller = **2.5%**.
- **Risk gates:**
  - **Fundamentals (phase-7b): VETO** → **naked directional short = 0%**; defined-risk
    carry-only permitted, marked "fundamentals-vetoed."
  - **Sentiment/crowd (phase-7c): CONFIRM** (crowd confirms the fade; DTC 1.94 = no
    squeeze) → **no-op** (no cut).
  - **Correlation cluster (phase-6): FIRED** — GFS↔NVDA **0.76**, GFS↔AAPL **0.73**
    (≥0.70) → **cut one size step** (half → starter).
  - **Sector rotation (phase-6): aligned** (tech outflow is *with* the short) → no cut.
  - **Debate (phase-8b):** bull_residual **0.75** vs bear_residual **0.65** →
    `disconfirmed=false` → **no-op**.
  - **Context (phase-0.5): BUSY_NAME_NORMAL_DAY** → do not size top-of-band (already
    at starter).
- **Final size (directional):** **0% — watch-only (fundamentals-VETOED).** The naked
  directional short is off per phase-7b. The two defined-risk structures below are
  **"carry-only"**: a PM electing to carry them should cap **max-loss ≤ ~1.0% of book
  risk** (the post-gate starter level: half from the win-rate map → starter from the
  correlation-cluster cut), but the blueprint's *directional* size is **0**.
- **Deviation reason:** none (no upward deviation; gates fired).

## Option structures

Front-expiry **implied move ±13.6% / ±$11.03** `[CTX:implied_move_pct]`. Targets
($77 = −5%, $74 = −8.8%) and the stop ($87.5 = +7.9%) all sit **inside** the priced
move, so a single expected-move gap can blow through a hard stop — which is *why* both
expressions are **defined-risk** (capped loss survives a 13.6% gap). Both use the
**June-18 expiry** (captures the 05-28 settlement + May CPI + FOMC; no earnings until
Aug-4, so no earnings IV-crush trap).

### Directional (primary expression)

- **Structure:** **put debit spread** (bearish, defined-risk)
- **Strike(s) / expiry:** **buy $80 put / sell $74 put, 2026-06-18**
- **Debit/credit:** ~**$2.30 debit** (est. at ~90% June IV)
- **Breakeven:** ~**$77.70**
- **Max loss:** **$2.30** (the debit) — sized so max-loss ≤ 1.0% of book
- **Why this structure:** captures the gap-fill toward the $74 deeper-support target
  with capped risk through the FOMC/CPI gap window; $74 short strike anchors the
  phase-2 support shelf. **Caveat (phase-8b):** long premium bleeds theta if the fade
  chops sideways post-settlement — hence it is the *secondary*-preferred vs the credit.

### Defined-risk alternative (desk-preferred per phase-8b)

- **Structure:** **bear call credit spread** (sells the rich/complacent call skew)
- **Strike(s) / expiry:** **sell $85 call / buy $90 call, 2026-06-18**
- **Debit/credit:** ~**$1.50 credit** (est.)
- **Breakeven:** ~**$86.50** (right at the block price / ZGL stacked ceiling)
- **Max loss:** **$3.50** (width $5 − credit $1.50) — sized so max-loss ≤ 1.0% of book
- **Why:** harvests **IV rank 79 / backwardation** `[STRUCT:iv_term_structure]` and
  the **COMPLACENT reverse skew** (25Δ calls richer than puts) `[STRUCT:term_skew]`;
  profits as long as GFS stays **below $85** (below the entire $86–87 wall) — theta
  works *for* you, and it's wrong only if the ceiling breaks (= the invalidation). This
  is the structure both debate sides converged on.

## Macro overlay (cite phase-6)

- **Tailwinds (for GFS = headwinds for the fade):** CHIPS $375M quantum award
  `[MACRO:GFS_catalyst_2026-05 WebSearch:fool.com]`; fed funds 3.62% off peak / curve
  normalized `[MACRO:DFF_2026-05-26 FRED]`; serial earnings beats `[FUND:earnings_surprise]`.
- **Headwinds (for GFS = tailwinds for the fade):** Technology net outflow **−$433.5M**
  `[MACRO:sector_rotation_2026-05-27 UW]`; hawkish FOMC hike-risk
  `[MACRO:FOMCminutes_2026-05-20 WebSearch:cnbc.com]`; warm headline CPI +0.64% MoM
  `[MACRO:CPIAUCSL_2026-04 FRED]`; Mubadala block overhang `[SENT:insider_block]`.
- **Net:** **near-term headwind** (supports the fade) over a **structural tailwind**
  (caps the downside — no air-pocket; quality + dividend floor + $79.95 mean target).

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|------|-------|------------------|
| 2026-05-28 | **Mubadala $1.91B block settlement** | ? (acute supply clears → then bounce risk) |
| ~2026-06-10/11 | May CPI release | − (hawkish-repricing risk if hot) |
| ~2026-06-16/17 | **FOMC** (next meeting) | − (hike-risk tilt → growth headwind) |
| 2026-06-18 | June OPEX | ? (written-$120-call / GEX-wall mechanics) |
| 2026-08-04 | GFS Q2 earnings | (outside 30d) |

## Post-trade monitoring checklist

- [ ] **Watch the 05-28 block settlement** — if GFS bounces hard off settlement back
      toward $86, the fade window is closing; take credit-spread profit / tighten.
- [ ] **Re-check GEX/ZGL daily (phase-4 refresh)** — a reclaim of $86.37 (long-gamma
      flip) is the structural invalidation.
- [ ] **Re-check dark-pool buy_ratio (phase-2)** — a post-settlement flip to >0.65
      accumulation signals the overhang is absorbed.
- [ ] **Watch the NVDA/AAPL cluster (corr 0.76 / 0.73)** — if those blueprints turn
      and the tech tape re-risks, the fade is fighting the cluster; cut.
- [ ] **CPI (Jun 10/11) + FOMC (Jun 16/17)** — a dovish surprise re-risks semis →
      macro invalidation.

## Citations summary

1. `[SENT:insider_block WebSearch:bloomberg.com]` — Mubadala $1.91B / 22M-share block,
   marketed $86.30–86.80, settles 05-28 — phase-7c-sentiment.md §News flow / Verdict.
2. `[STRUCT:gex]` — dealers short gamma, ZGL $86.37 > spot $81.04; walls $85/$90/$100 —
   phase-4-structure.md §GEX.
3. `[MACRO:sector_rotation_2026-05-27 UW]` — Technology net outflow −$433.5M (largest
   sector) — phase-6-macro.md §Sector rotation.
4. `[HIST:52w_proximity fz]` — +87.5% above 200-DMA, +132.7% YTD, 12.2% below $92.55
   high — phase-5-historical.md §Price context.
5. `[HIST:signal_backtest]` — bearish_flow win_rate 0.583 (n=12) — phase-5 §Sizing
   handoff (the Kelly p).
