# Phase 9 — Trade Blueprint

**Ticker:** MARA
**As-of date:** 2026-06-18
**PM voice:** desk PM running an institutional options-overlay book
**Spot reference:** $14.22 (phase-0.5 / local screener close)
**Upstream phases cited:** phase-0.5 through phase-8b

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

MARA is a gamma-pinned, range-bound BTC proxy: dealers have been net long gamma every
session for 30 days (`regime_flip_dates: null`, ZGL $5.26) with peak gamma **+$36.4M at
$14.5** `[STRUCT:gex]`, max-pain $14 for 6/26, while today's loud "$13M call premium"
was actually **sold** (net_flow −$1.61M, and the $14.5C 6/26 churned 63k contracts for
only **+514 OI** `[OI:biggest-increases]`). The macro frame reinforces the cap — BTC is
**below its 50d/200d MAs** into a **hawkish 6/17 FOMC** (2026 dot → 3.8%, hike bias)
and the UW regime literally prescribes *"iron condors in range"* `[MACRO:MarketRegime]`
— and all four desk agents returned **RANGE** `[AGENT:desk]`. The trade is to **sell
the $14.5–$15 upside, defined-risk**, around a $14 pin — small, because the edge is
thin (a busy name's normal day) and a 26.5% short float makes the up-break violent.

## Bias + conviction + horizon

- **Directional bias:** **RANGE** (capped-upside, mild-bearish tilt — sell premium)
- **Conviction (M-01 bin):** **0.65**
- **Time horizon:** **1-5d** (to 6/26 weekly OPEX, where the pin + max-pain resolve)
- **Why this bin:** confluence is strong on the *range classification* (≈0.75 band —
  long-gamma pin + calm vol + unanimous agents), but I hold **one bin lower (0.65)**
  because the *tradeable edge* is thin: `[CTX:] = BUSY_NAME_NORMAL_DAY`, IV at the 4.17th
  percentile (poor level to sell despite +VRP carry), phase-7c **CAUTION** (squeeze
  risk), and the desk averaged only 2.5/5. See `## Conviction deviation`.

## Conviction deviation

Phase-10 confluence is expected to land ~73–78 (→ 0.75 band). I deliberately set
**0.65 (one bin down)**: the phases agree strongly that MARA is *range-bound*, but they
agree just as strongly that it is a **low-edge** range — a normal day for a busy name,
IV cheap (4.17 pctile), and a CAUTION squeeze gate. High confidence in the
*classification* ≠ high confidence in the *trade*. Conservative down-deviation only.

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| Primary | **$14.50** | sell the upside on a tag/rejection of the $14.5 gamma + call wall | `[STRUCT:gex]` / `[OI:oi-by-strike]` |
| Aggressive | **$14.80–$14.90** | fade into the $14.85–14.93 dark-pool supply band (richer call premium to sell) | `[DP:price_levels]` |
| Fade (plan B, counter-trade) | **> $15.00** | if BTC reclaims $65.2k and MARA closes > $15, **abandon the short-call / flip to a small squeeze-chase long** above the $15.5 long leg | `[SENT:short_float]` / `[MACRO:BTC]` |

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Support | **$14.00** (then put-wall $12.00) | `[DP:price_levels]` / `[OI:oi-by-strike]` put_wall_support |
| Resistance | **$14.50** (immediate) → **$15.00** (dominant wall) | `[OI:oi-by-strike]` call_wall_resistance / `[STRUCT:gex]` |
| Gamma flip (ZGL) | **$5.26** (far below — deep long-gamma; break not a near-term risk) | `[STRUCT:gex]` |
| Largest pin (6/26 max-pain) | **$14.00** | `[STRUCT:max-pain]` |

Price-context color: RSI(14) 55.7 (neutral), spot −39% below the 52w high $23.45 and
+113% above the 52w low — **mid-range, not extended either way** `[HIST:rsi fz]`
`[HIST:52w_proximity fz]`; no chase risk, but no oversold bounce setup either
(narrative only — does not alter sizing).

## Invalidation

- **Price-based:** **two daily closes above $15.00** (the dominant call/GEX wall) →
  the range cap is broken and dealer gamma flips to a chase; exit the call side. (Down-
  side: a close below **$13.83** voids the $14 shelf — manage the put side.)
- **Signal-based:** GEX/DEX flips toward **short-gamma above $15** on the phase-4 daily
  refresh, **or** `institutional-accumulation` flips to distribution, **or** cumulative
  premium flow turns **net-bullish for 3 consecutive sessions** (a real standing call-OI
  build above the wall, not churn) `[INSIGHT:institutional-accumulation]` `[HIST:cumulative-premium-flow]`.
- **Macro-based:** **BTC reclaims its $65.2k 50d MA / breaks $66k resistance** (the
  squeeze trigger) `[MACRO:BTC]`; conversely a BTC break below **$60k** triggers a
  β-5.35 down-cascade. Either resolves the range.

## Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** p_raw = **0.857** (phase-5 `bearish_flow` backtest, **n=7**,
  source=backtest) → **N-cap (n<10) = 0.75** → **p = 0.75** `[HIST:signal_backtest]`.
  - ⚠ `bearish_flow` is a **loose proxy** for a range/credit trade (phase-5 flagged
    this) — treat p as soft.
- **Kelly inputs:** b = **0.43** (iron-condor max-profit/max-loss ≈ $0.30/$0.70),
  fraction = 0.25, cap_pct = 5.
- **Raw Kelly:** (0.75·0.43 − 0.25)/0.43 = **+0.169** → suggested = 0.169·0.25·100 =
  **4.2%**. **Win-rate map** (p=0.75 ≥ 0.70 → "full" ≤ 5%) → ceiling 4.2%. Take smaller → **4.2%**.
- **Risk gates:**
  - Fundamentals (7b): **CONFIRM** → no-op (weak business *supports* the cap; would VETO a long).
  - Sentiment/crowd (7c): **CAUTION** (CROWDED_SHORT 26.49%) → **cut one step (full→half): 4.2% → 2.1%.**
  - Correlation cluster (6/8): **none** (no concurrent blueprint; BTC-complex corr 0.72–0.82 is advisory) → no-op.
  - Sector rotation (6): **neutral** → no-op.
  - Debate (8b): bull_residual **0.75** vs bear_residual **0.65** → **not disconfirmed** → no-op.
  - **Context (0.5): BUSY_NAME_NORMAL_DAY** → do not size top-of-band → discretionary cut from 2.1% toward starter.
- **Final size: 1.5% of book risk** (structure max-loss ≤ 1.5% of book). Down-deviation
  from 2.1% for the busy-name normal day + thin/loose-proxy edge (no justification
  required for a *downward* move).
- **Deviation reason:** none (downward only).

## Option structures

### Directional (the mild-bearish / capped lean) — Bear call (credit) spread

- **Structure:** sell $14.5 call / buy $15.5 call (mirrors the smart-money trade; the
  $15.5 long leg **caps the squeeze tail** per phase-8b).
- **Strikes / expiry:** **14.5 / 15.5, 2026-06-26** (8 DTE).
- **Credit:** ≈ **+$0.23** (est. $14.5C $0.42 − $15.5C $0.19).
- **Breakeven:** **$14.73.**
- **Max loss:** **$0.77** (width $1.00 − credit $0.23).
- **Why:** profits if MARA ≤ $14.5 at 6/26 — the flow-defined cap + peak gamma wall +
  6/26 max-pain $14. IV at the 4th percentile makes the *level* a poor place to sell, so
  the long $15.5 leg is mandatory (defined risk); the short strike sits at ~+1σ(8d) of
  the ±4.1% expected move, so the upside is the tested side.

### Defined-risk (primary recommended) — Iron condor

- **Structure:** sell $15 call / buy $16 call **and** sell $13 put / buy $12 put — both
  short strikes **outside** the ±4.1% 8-day expected move, bracketing the $14 pin.
- **Strikes / expiry:** **13/12 put wing + 15/16 call wing, 2026-06-26.**
- **Credit:** ≈ **+$0.30** (call wing ~$0.20 at the $15 gamma wall + put wing ~$0.10).
- **Breakevens:** ≈ **$12.70 / $15.30.**
- **Max loss:** **≈ $0.70** (wider wing $1.00 − credit $0.30) → **this is the 1.5%-of-book
  sizing anchor**.
- **Why:** the regime-prescribed "iron condor in range"; short strikes at the $15 call
  wall and $13 put-support band, profit zone $13–$15 brackets the pin and the ±4.1%
  expected move. Roll/close the tested side on invalidation.

## Macro overlay (cite phase-6)

- **Tailwinds:** VIX 16.4 falling → calm vol supports the pin `[MACRO:VIX]`; UW regime
  guidance *"half size, defined-risk, iron condors in range"* `[MACRO:MarketRegime]`;
  VRP +6.3% premium-selling carry `[HIST:vrp]`.
- **Headwinds:** hawkish FOMC 6/17 (2026 dot 3.8%, hike bias) `[MACRO:FOMC]`; BTC below
  50d/200d MAs `[MACRO:BTC]`; sticky CPI +4.16% `[MACRO:CPIAUCSL]`; 26.5% short float =
  up-squeeze tail `[SENT:short_float]`.
- **Net:** **headwind-neutral** — caps the upside and supports the short-premium range;
  the only thing that breaks it is a BTC move (either direction).

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|------|-------|------------------|
| 2026-06-26 | weekly OPEX (the structures' expiry; pin/max-pain $14) | ? |
| ongoing | **BTC test of $65.2k 50d MA / $66k resistance** (the real trigger) | ? |
| ~2026-07-15 | June CPI release | − (sticky-inflation / rate-path risk) |
| ~2026-07-28/29 | next FOMC (hike bias live) | − |
| 2026-08-04 | MARA Q2 earnings (outside the 6/26 expiry — not traded) | ? |

Front-expiry implied move **±1.46% / ±$0.21** `[CTX:implied_move]`; the 8-day (6/26)
expected move ≈ **±4.1% / ±$0.58** → both structures' short strikes are placed at/outside
that boundary. A single-catalyst gap of the expected-move magnitude does **not** exceed
the defined-risk max-loss (structures are capped), so the 6/26 expiry is safe to hold.

## Post-trade monitoring checklist

- [ ] **BTC vs its $65.2k 50d MA, daily** — a reclaim is the squeeze trigger AND the macro invalidation.
- [ ] **GEX regime / ZGL on the phase-4 daily refresh** — a flip toward short-gamma above $15 breaks the pin.
- [ ] **$14.5/$15 call OI for a real standing build** (phase-3 `biggest-increases`, not churn) — positioning for an up-break.
- [ ] **Dark-pool tone** — a flip from accumulation to distribution, or a fresh large buy block at $14 (phase-2/7).
- [ ] **Short interest / borrow** — an SI spike or HTB shift changes the squeeze math (phase-7c).

## Citations summary

1. `[STRUCT:gex]` peak net_gex **+$36.4M at $14.5** / ZGL $5.26 (long-gamma pin) — phase-4-structure.md §GEX.
2. `[OI:biggest-increases]` $14.5C 6/26 OI **+514** vs 63,005 volume (selling was churn, not a standing short) — phase-3-positioning.md §New OI.
3. `[HIST:gex-time-series]` **30d zero regime flips** (stable long-gamma) + `[HIST:signal_backtest]` bearish_flow win **0.857 (n=7)** — phase-5-historical.md.
4. `[MACRO:FOMC]` hawkish 6/17 (2026 dot → 3.8%) + `[MACRO:BTC]` BTC below 50d/200d MAs — phase-6-macro.md.
