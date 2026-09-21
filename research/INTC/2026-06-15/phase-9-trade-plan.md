# Phase 9 — Trade Blueprint

**Ticker:** INTC
**As-of date:** 2026-06-15
**PM voice:** desk PM running an institutional book
**Spot reference:** $127.86 (phase-2 dark pool / `fz` close)
**Upstream phases cited:** phase-0.5 through phase-8b

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

INTC is a euphoric **+246.5%-YTD** foundry-turnaround re-rate [HIST:perf fz] whose
options tape has **stopped confirming the price** — net flow is flat at **−$1.16M**
despite the run [FLOW:insights_deep_dive] and the composite flags an outright
**price-vs-flow DIVERGENCE** [INSIGHT:price_vs_flow]. The dealer structure is
**positive-gamma and mean-reverting, pinned under a +$15.3M gamma wall at $130**
[STRUCT:gex], so this is a **RANGE** ($124.57 dip-bid → $130 cap), not a breakout —
the unanimous desk read (3 RANGE + 1 NEUTRAL) [AGENT:desk]. Trade it **tiny and
defined-risk**: a real foundry catalyst + 5-day bullish sweep persistence
[FLOW:sweep_persistence] keep me from shorting, but two CAUTION gates and a
disconfirmed bull/bear debate keep me from chasing — the highest-EV action is to let
**FOMC (6/17)** resolve the $130 break.

## Bias + conviction + horizon

- **Directional bias:** RANGE (fade rips into $130 / buy dips to ~$124.57; no clean
  long or short — plurality of phases 1–8)
- **Conviction (M-01 bin):** **0.55** (narrative range-confidence ~0.65, down-shifted
  one bin by the phase-8b debate disconfirmation)
- **Time horizon:** 1-5d (to FOMC + OPEX; re-underwrite after 6/17)
- **Why this bin:** lowest band — a heavily-gated, non-directional setup on a
  BUSY_NAME_NORMAL_DAY with a price-vs-flow divergence; phase-10 confluence expected
  in the low band (see `## Conviction deviation` if it diverges).

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| Primary | **$124.57** | tag of the dark-pool dip-bid shelf + dealer (DEX) buying on weakness; buy the dip | [DP:price_levels] / [STRUCT:dex] |
| Aggressive | **$120.00–116.96** | flush into the lower DP shelf / put-wall (only if it gets there without a flow flip) | [DP:price_levels] / [OI:oi_by_strike] |
| Fade | **$129–130** | rejection at the $130 gamma pin / call wall — counter-trade the rip | [STRUCT:gex] / [OI:oi_by_strike] |

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Support | **$124.57** (then $116.96, then $110–112) | [DP:price_levels] / [STRUCT:max_pain] |
| Resistance | **$130** (then $150) | [OI:oi_by_strike call_wall_resistance] / [STRUCT:gex] |
| Gamma flip (ZGL) | $13.44 — **legacy-OI artifact; regime is POSITIVE, spot far above, no real flip near spot** | [STRUCT:gex] |
| Largest pin / magnet | **$110–112** (near-expiry max-pain; 06-18 reads $60 = legacy artifact) | [STRUCT:max_pain] |

**Price-context color (advisory):** entering near the **52-week high ($132.75,
−3.7%)** with **RSI 64** [HIST:rsi fz][HIST:52w_proximity fz] — not yet textbook
overbought (the 6/5 dip to $100 reset it), but +137% above the 200-SMA — *chase risk
is real; prefer the fade or a confirmed dip, never a market-order at $128.*

## Invalidation

- **Price-based:** two daily closes **below $120** (loses the $124.57→$120 shelf,
  opens the $116.96 / $110–112 air pocket) → the buy-the-dip is wrong. For the range
  itself: two daily closes **above $132** on expanding volume (clears the $130 gamma
  cap → momentum long, range broken upward).
- **Signal-based:** **GEX/DEX flips from POSITIVE to short-gamma** on the phase-4
  daily refresh (mean-reversion → trend amplification) [STRUCT:gex]; OR dark-pool
  **mega buy_ratio reverses below 0.45** (accumulation → distribution) [DP:block_stratified];
  OR the **price-vs-flow divergence resolves with net flow turning decisively bullish**
  (would upgrade to a real long) [INSIGHT:price_vs_flow].
- **Macro-based:** **FOMC 6/17 surprise** — hawkish → high-multiple semi de-rate
  (the euphoric MU/MRVL/AMD cohort unwinds together) [MACRO:FOMC]; dovish → breaks
  $130 and the range flips to a momentum long. Both tails are live → keep size minimal
  until resolved.
- **Exit on invalidation:** **Hard stop = the defined-risk premium** — because a
  single FOMC gap of the ±6.17% implied move ($124.57 ∓ $7.87 → ~$116.7 / ~$132.4)
  *exceeds* the $120 price stop, the directional expression is a debit spread whose
  max loss is the premium, not a stop-loss order. Close the structure on a confirmed
  signal-based flip; otherwise let defined risk run to expiry.

## Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** p_raw = **1.00** (n=**7**, source=**backtest**;
  bullish_flow, **market-wide** base rate) → N-cap (n<10 → 0.75) → **p = 0.75**
  [HIST:signal_backtest]. *(N=7 + market-wide, not INTC-specific — the cap is doing
  real work here.)*
- **Kelly inputs:** b = **1.2** (target $130 cap / entry $124.57 / stop $120),
  fraction = 0.25, cap_pct = 5.
- **Raw Kelly:** (0.75×1.2 − 0.25)/1.2 = **0.542** → ×0.25×100 = 13.5%, **capped at
  5.0%** (full). **Win-rate map ceiling:** p=0.75 ≥ 0.70 → full (≤5%). Pre-gate = **5.0%**.
- **Risk gates (each cuts only):**
  - Fundamentals (phase-7b): **CAUTION** → cut one step (full → half) → **2.5%**.
  - Sentiment/crowd (phase-7c): **CAUTION**, crowd_state **CROWDED_LONG** → cut one
    step (half → starter) → **1.25%**.
  - Correlation cluster (phase-6/8): **none** (INTC sole blueprint for 2026-06-15) → no-op.
  - Sector rotation (phase-6): **aligned** (Tech inflow +$7.78B, persistence 1.0) → no-op.
  - Debate (phase-8b): **disconfirmed = true** (bull_residual 0.55 < bear_residual
    0.65) → down-shift conviction bin one (0.65→0.55) **and** cut one step (starter →
    ~half-starter) → **~0.6%**.
  - Context (phase-0.5): **BUSY_NAME_NORMAL_DAY** → do not size at top of band (already minimal).
- **Final size:** **0.6% of book risk** (defined-risk max-loss basis; ≪ cap 5%).
- **Deviation reason:** none (no upward deviation; forbidden here — three gates fired).

**PM call:** 0.6% is a *toe*, not a position. The honest recommendation is
**watch-/wait-for-FOMC**: a minimal defined-risk dip-buy is permissible, but the
edge-positive move is to let 6/17 resolve the $130 break and trade the resolution
with a clean structure.

## Option structures

### Directional (primary) — buy-the-dip, long premium

- **Structure:** call debit spread (long premium = VRP-aligned; VRP −0.085,
  PREMIUM_BUYING [HIST:vrp]).
- **Strikes / expiry:** **C125 / C135, 2026-07-17** (32 DTE) — **avoids the 2026-07-23
  earnings IV crush**; $125 anchors the $124.57 DP shelf, $135 = the BofA target between
  the $130 cap and the $150 magnet [OI:oi_by_strike].
- **Debit/credit:** ~**$5.00 debit** (width $10).
- **Breakeven:** ~**$130.00**.
- **Max loss:** **$5.00 / contract** (the debit) — sized so total debit ≤ 0.6% of book.
- **Why this structure:** entered ONLY on a dip to ~$124.57, it buys cheap-vs-realized
  premium (VRP-aligned) with capped risk that survives a FOMC gap beyond the $120 stop;
  it plays the dealer dip-bid into the $130 cap and the upside if FOMC breaks it.

### Defined-risk alternative — fade the rip

- **Structure:** call credit spread (the desk's preferred range expression — fade the
  $130 gamma cap).
- **Strikes / expiry:** **C132 / C140, 2026-07-17** (sold on a rip into $129–130).
- **Debit/credit:** ~**+$2.30 credit** (width $8).
- **Breakeven:** ~**$134.30**.
- **Max loss:** **$5.70 / contract** (width − credit) — sized ≤ 0.6% of book.
- **Note:** sells the $130/$150 call-wall supply into a positive-gamma cap. **VRP
  tension:** VRP-negative says premium is cheap, so keep it tight/small — a clean,
  volume-backed break of $130 (dovish FOMC) runs it; close on a daily close >$132.

## Macro overlay (cite phase-6)

- **Tailwinds:**
  - [MACRO:sector_flow] Technology = #1 sector inflow **+$7.78B**, persistence **1.0**/5d.
  - [MACRO:INTC_BofA] BofA upgrade → **$135** + Google-TPU/Nvidia backup-foundry wins (real catalyst).
- **Headwinds:**
  - [MACRO:MarketRegime] regime **TRANSITIONAL — "half position sizes, defined-risk"**, breadth 37% bullish.
  - [MACRO:DGS10] 10y **4.48%** pressures the ~83× fwd-P/E multiple [FUND:fwd_pe fz].
  - [MACRO:FOMC] **FOMC 6/17 inside OPEX** — a 2-way binary.
- **Net:** **mixed** (genuine sector + idiosyncratic tailwind vs. cautious regime + event risk + stretched valuation).

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|------|-------|------------------|
| 2026-06-16/17 | FOMC (stmt 6/17 2pm ET) | ? |
| 2026-06-18/19 | Monthly OPEX (26.8% of INTC OI) | ? |
| 2026-07-23 | INTC Q2 earnings | ? |

## Post-trade monitoring checklist

- [ ] Re-run phase-4 `gex`/`dex` daily — **any POSITIVE→short-gamma flip invalidates the range** (trend amplification).
- [ ] Re-check phase-2 dark pool daily — mega `buy_ratio` holding ≥0.55 = accumulation intact; **<0.45 = distribution → exit**.
- [ ] Watch the **$124.57 shelf and $130 gamma cap** — two daily closes outside ($<120 or $>132) breaks the range thesis.
- [ ] **FOMC 6/17**: trade the *resolution*, not the *anticipation* — keep size ≤0.6% into it; re-underwrite the whole blueprint 6/18.
- [ ] Track the semi cohort (MU/MRVL/AMD) — a correlated cohort unwind takes INTC down with it [FUND:peer_pe fz].
- [ ] Watch `pc-ratio-zscore` / call-skew — a move to a P/C extreme (|z|>2) would upgrade the fade to a real contrarian short.

## Citations summary (M-04 — ≥3 distinct upstream datapoints)

1. [FLOW:insights_deep_dive] net_flow **−$1.16M** flat (bullish $229.9M ≈ bearish $231.0M) — phase-1-flow.md §Whole-tape.
2. [STRUCT:gex] regime **POSITIVE**, largest gamma pin **$130 (+$15.3M)** — phase-4-structure.md §GEX.
3. [INSIGHT:price_vs_flow] **DIVERGENCE** — price +33.5% but net flow bearish — phase-7-insights.md §Price vs flow.
4. [HIST:perf fz] **+246.5% YTD**, analyst target **$99.98 (−22%)** — phase-5-historical.md §Price context.
5. [AGENT:desk] phase-8 unanimous **3 RANGE + 1 NEUTRAL**, avg conviction 2.75 — phase-8-agent-views.md.
6. [DEBATE] disconfirmed — bull_residual 0.55 vs bear_residual 0.65 — phase-8b-debate.md.

## Conviction deviation

None pre-emptively. If phase-10 scores the confluence band materially above the 0.55
floor, the override is *still* the floor — three risk gates fired (7b, 7c, 8b) and the
context is BUSY_NAME_NORMAL_DAY, so an upward deviation is forbidden by the sizing
rubric regardless of the confluence number. If phase-10 scores it *lower*, take the lower.
