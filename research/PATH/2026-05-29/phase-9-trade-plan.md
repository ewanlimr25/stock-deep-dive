# Phase 9 — Trade Blueprint

**Ticker:** PATH (UiPath Inc.)
**As-of date:** 2026-05-29
**PM voice:** desk PM running an institutional options-overlay book
**Spot reference:** $11.72 (phase-0 / fz close; intraday recovered from ~$10.4)
**Upstream phases cited:** phase-0.5 through phase-8b

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

PATH is a cheap, **profitable, net-cash software laggard** (fwd PE 13.1, 83%
gross margin, net cash $2.51/sh `[FUND:peer_pe fz]`) that just **raised FY
guidance and printed its first GAAP profit** on 2026-05-28 and is being
**accumulated by institutions at the floor** — dark-pool block-tier prints are
100% buy at/above spot `[DP:block-stratified]` — but its upside is **hard-capped
at $12–$13** by the largest gamma wall (+$11.4M GEX) `[STRUCT:gex]` sitting
exactly where consensus fair-value $13.47 lives. With a **50% / n=8 flow
backtest (no historical edge)** `[HIST:signal-backtest]`, a `BUSY_NAME_NORMAL_DAY`
tape, and a debate that **disconfirmed** the bullish lean (bear 0.62 ≥ bull 0.60)
`[DEBATE:]`, the honest trade is a **small, defined-risk $11–$13 range skewed
slightly long**, with the 31% short float + dealer-short-call DEX `[STRUCT:dex]`
as a cheap convex option *if* $13 breaks — not a conviction directional bet.

## Bias + conviction + horizon

- **Directional bias:** RANGE (with a slight long lean to the upper edge)
- **Conviction (M-01 bin):** **0.55**
- **Time horizon:** 1–4w (June-18 expiry; post-earnings, next catalyst is the
  post-IV-crush drift — no PATH event in window)
- **Why this bin:** phase-10 confluence ≈ 58 maps to the 0.65 band, but the
  **phase-8b disconfirmation gate down-shifts the bin one step to 0.55** (and
  `BUSY_NAME_NORMAL_DAY` forbids sizing at the top of any band).

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| Primary | $11.65–$11.80 | hold of the dark-pool value shelf where block money paid up | `[DP:largest]` |
| Aggressive | $11.00–$11.20 | tag of the gamma pivot / lower DP shelf and *reclaim* (don't catch it falling through) | `[STRUCT:gex]` `[DP:largest]` |
| Fade (counter) | $12.90–$13.10 | rejection at the $13 wall / consensus target — sell the rip (this is the iron-condor short-call zone) | `[STRUCT:gex]` `[SENT:recom fz]` |

Price-context color: RSI 63.5 and price **+9–10% above its 20/50-day SMA**
`[HIST:rsi fz]` — entering long is *chasing* a short-term-extended bounce into a
wall; prefer the primary shelf or the aggressive reclaim, not market-buying here.

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Support (value shelf) | $11.65–$11.80 | `[DP:largest]` |
| Support (lower / pivot) | $11.00–$11.30 | `[STRUCT:gex]` (gamma flips negative <$11) / `[DP:largest]` |
| Resistance (gamma wall / cap) | $12.00 (largest), then $13.00 | `[STRUCT:gex]` |
| Consensus fair-value / IC breakeven | $13.47 | `[SENT:recom fz]` |
| Largest pin | none (no pin-risk; June-18 OPEX >7d, no ≥40% cliff) | `[OI:pin-risk]` |
| Downside cascade target if $11 breaks | $9.00–$10.00 | `[OI:biggest-increases]` (put shelf) |

## Invalidation

- **Price-based:** *Range long invalidated* by two daily closes **below $11.00**
  (flips dealers to negative gamma → short-gamma acceleration toward $9–$10).
  *Range itself invalidated* (upside) by a sustained close **above $13.00** —
  that is no longer "range," it's the squeeze breaking out; roll to the
  momentum-long expression.
- **Signal-based:** DEX flips so dealers are **no longer net short calls**
  `[STRUCT:dex]` (squeeze fuel gone), OR dark-pool block tier turns **net seller**
  `[DP:block-stratified]` (accumulation thesis broken), OR short float collapses
  toward ~15% (the over-shorted convexity is spent).
- **Macro-based:** regime flips from TRANSITIONAL to **RISK_OFF**
  `[MACRO:MarketRegime_2026-05-29 UW]`, or the **10y breaks above ~4.70%**
  `[MACRO:DGS10_2026-05-28 FRED]` (discount-rate hit to long-duration software).

## Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** p_raw = **0.50** (n=**8**, source=`backtest`,
  bullish_flow) → n<10 cap is 0.75, so capped **p = 0.50** `[HIST:signal-backtest]`.
- **Kelly inputs:** b = |13.00 − 11.72| / |11.72 − 11.00| = 1.28/0.72 = **1.78**;
  fraction = 0.25; cap_pct = 5.
- **Raw Kelly:** (0.50×1.78 − 0.50)/1.78 = **0.219** → ×0.25×100 = 5.48% → capped
  at cap_pct **5.0%**. **Win-rate map ceiling:** p=0.50 → "0.50–0.70 = half"
  ⇒ ≤ **2.5%**. Take the smaller: **2.5%**.
- **Risk gates:**
  - Fundamentals (7b): **CONFIRM** → no-op (profitable, cheap, net cash; *not* a veto).
  - Sentiment/crowd (7c): **CONFIRM**, crowd_state **CROWDED_SHORT** → no-op
    (shorts are fuel for a long, not a crowded-long fade; squeeze is a *noted*
    tailwind, **not** added to size).
  - Correlation cluster (6/8): **none** (PATH is the only blueprint for the date) → no-op.
  - Sector rotation (6): **aligned** (Tech persistence 1/1) → no-op.
  - Debate (8b): bull_residual **0.60** vs bear_residual **0.62** → **disconfirmed**
    → **cut one size step (half → starter)** + bin down-shift (already applied).
  - **Context (0.5): `BUSY_NAME_NORMAL_DAY`** → do not size at top of band (reinforces).
- **Final size:** **1.25% of book risk** (starter — the debate gate cut half→starter).
- **Deviation reason:** none (no upward deviation; all moves were cuts).

## Option structures

> Front-expiry implied move **1.63%/day ≈ $0.19** `[CTX:implied_move]`; the ~20-day
> June-18 1σ move ≈ 7% ≈ **±$0.85** (→ ~$10.87–$12.57). Earnings are **behind us**
> (2026-05-28), so there is **no IV-crush risk** inside this window — but IV has
> already crushed to the 8.8th percentile `[HIST:iv-percentile-zscore]`, so the
> long legs are cheap and the short legs (June IV still ~80–100%) collect well.

### Directional (primary — the cheap convex upper-edge bet)

- **Structure:** call debit spread, **$12 / $14, June-18-2026**
- **Strikes / expiry:** long $12C, short $14C (both June-18 OI clusters: $12 OI
  13,235; $14 OI 2,952; $12 = largest gamma wall) `[OI:biggest-increases]` `[STRUCT:gex]`
- **Debit:** ≈ $0.36 (0.58 − 0.22)
- **Breakeven:** $12.36
- **Max loss:** $0.36 (the debit) · **Max value:** $2.00
- **Why this structure:** owns the **squeeze-break tail >$13** cheaply (4.5:1
  asymmetry) while the cheap-IV (8.8th pctile) long $12 leg costs little; the
  short $14 caps cost and accepts the consensus ceiling. Defined risk; expires
  worthless in the base-case range (acceptable, it's the "free option" on the
  31% short squeeze).

### Defined-risk alternative (the desk-consensus core — sell the range)

- **Structure:** **iron condor, short $11P / short $13C, long $10P / long $14C,
  June-18-2026**
- **Strikes / expiry:** short $11P ($0.56) + long $10P ($0.22) = +$0.34; short
  $13C ($0.35) + long $14C ($0.22) = +$0.13 → strikes anchored to the $11 gamma
  pivot, $13 wall, and the $9–$10 / $15 OI shelves `[STRUCT:gex]` `[OI:biggest-increases]`
- **Net credit:** ≈ **$0.47**
- **Breakevens:** **$10.53** and **$13.47** (the upper BE = the consensus target
  exactly `[SENT:recom fz]`)
- **Max loss:** $1.00 width − $0.47 credit = **$0.53**
- **Why:** this is the **regime-prescribed expression** ("iron condors in range,"
  `[MACRO:MarketRegime_2026-05-29 UW]`), monetizes the VRP +15.8 premium-selling
  carry `[HIST:vrp]`, and profits across the entire $10.5–$13.5 box the whole
  desk and the debate converged on. **Size so max loss ≤ 1.25% of book.**

## Macro overlay (cite phase-6)

- **Tailwinds:** easing cycle, fed funds 3.62% + un-inverted 2s10s +0.46
  `[MACRO:DFF_2026-05-28 FRED]` `[MACRO:T10Y2Y_2026-05-28 FRED]` (duration support);
  Tech sector flow leadership, persistence 1/1 `[MACRO:SectorFlowPersistence_2026-05-29 UW]`.
- **Headwinds:** regime **TRANSITIONAL "half size, defined-risk"** + weak breadth
  36% bullish `[MACRO:MarketRegime_2026-05-29 UW]`; core PCE 3.29% + 10y 4.45%
  cap the duration tailwind `[MACRO:PCEPILFE_2026-04 FRED]`; the Tech bid is
  **mega-cap concentrated**, not small-cap.
- **Net:** **mixed** — sector tailwind offset by a cautionary, narrow-breadth regime.

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|------|-------|------------------|
| 2026-05-28 (PASSED) | Q1 FY2027 earnings — EPS miss, **guidance raised**, first GAAP profit | + (already in the tape) |
| ~mid-Jun | May CPI release | ? (sector rate beta) |
| ~early-Jun | May NFP | ? (sector rate beta) |
| ~mid-Jun | FOMC (if scheduled) | ? (easing-path signal) |
| 2026-09-03 | next PATH earnings (**outside window**) | n/a |

No idiosyncratic PATH catalyst in the window — the thesis is technical/structural
post-earnings drift, not event-driven.

## Post-trade monitoring checklist

- [ ] Re-check **dark-pool block buy_ratio** daily — if the block tier flips to
      net seller, the floor thesis is broken (exit the long lean).
- [ ] Re-check **DEX / GEX** on the phase-4 daily refresh — a flip to dealers no
      longer short calls, or spot losing the $11 gamma pivot, invalidates the box.
- [ ] Watch **$11.00 and $13.00** as the binary range edges — a sustained close
      beyond either flips the trade (down→exit/cascade, up→roll to momentum long).
- [ ] Track **short interest / borrow fee** at the next semi-monthly print — a
      collapse in SI (or borrow tightening into a real squeeze) changes the convex
      tail's value.
- [ ] Monitor **10y yield (4.45%)** and the **regime label** — a break >4.70% or
      a RISK_OFF flip is the macro invalidation.

## Citations summary

1. `[DP:block-stratified]` — dark-pool block tier **100% buy** (buy_ratio 1.0,
   769K sh / $8.96M), pay-up at/above spot — phase-2-dark-pool.md §Tier breakdown.
2. `[STRUCT:gex]` — **+$28.6M positive GEX, largest wall $12 (+$11.4M), $11
   pivot** — phase-4-structure.md §GEX.
3. `[HIST:signal-backtest]` — **bullish_flow win rate 0.50, n=8** (no edge) —
   phase-5-historical.md §Signal backtest.
4. `[FUND:peer_pe fz]` — **fwd PE 13.1, only profitable name vs FROG/GTLB/S/ZS** —
   phase-7b-fundamentals.md §Valuation.
5. `[DEBATE:]` — **disconfirmed, bull 0.60 / bear 0.62** — phase-8b-debate.md.
