# Phase 6 — Macro & Market Regime

## Summary

The macro backdrop is a **mild, generic tailwind that FSLY barely participates in —
but its idiosyncrasy is the real story.** Three reads:

- **Regime TRANSITIONAL / trend UPTREND.** SPY $756.48 is above 20/50-SMA, **+6.31%
  30d, −0.21% from the 90-day high**, but **breadth is narrow — 36.3% bullish** (2,247
  of 6,187). The regime engine advises **"reduce size, defined-risk."** `[MACRO:market-regime]`
- **Technology is the #1 sector inflow** (+$533.3M today; persistence **1.0, trend
  INFLOW**) `[MACRO:sector_flow_persistence]` — but FSLY is a **$2.65B small-cap that
  doesn't participate in size** (phase-0.5: outside top-50 net-dir, outside top-100
  volume). The sector tailwind is generic, not FSLY-specific.
- **FSLY is idiosyncratic / low-beta — and that cuts *for* it here.** Beta **0.37**
  (intake), and its only flagged 30d correlation is **NEGATIVE: FSLY/DDOG −0.634**;
  it is **not** highly correlated with CDN/infra peers (NET, AKAM, ESTC).
  `[MACRO:portfolio_correlation]` Unlike a high-beta cluster name, FSLY trades on its
  **own short-squeeze/momentum dynamics**, not tech beta. That means: (a) the narrow-
  breadth tech tape is neither a strong help nor a strong threat, and (b) it offers
  genuine **diversification** — a tech-risk-off wouldn't drag it the way it would a
  0.88-correlated mega-cap.

**Macro verdict: NEUTRAL-to-mild-TAILWIND.** Risk-on uptrend is a faint positive, but
FSLY's edge (if any) is **idiosyncratic** — the 14.6% short base + call-OI ladder
(phases 3) — not macro/sector beta. The narrow-breadth "half-size" regime guidance
applies; the low beta / negative peer correlation means the trade lives or dies on
FSLY-specific catalysts, not the tape.

## Market regime (`uw risk market-regime`) `[MACRO:market-regime]`

| Field | Value |
|-------|-------|
| Regime | **TRANSITIONAL** — "reduce size, wait for clarity" |
| Trend | **UPTREND** |
| SPY | $756.48 (above 20/50-SMA) |
| SPY 30d / vs 90d-high | **+6.31% / −0.21%** |
| Breadth | **36.3% bullish** (2,247 / 6,187) |
| Guidance | **Half size; defined-risk** |

## Sector rotation & persistence `[MACRO:sector_flow_persistence]`

- Inflow: **Technology +$533.3M** (largest), Utilities +$2.5M, Energy +$0.5M.
  Outflow: Comm Services −$104.3M, Consumer Cyclical −$49.8M, Basic Materials −$20.4M.
- Technology **persistence 1.0, trend INFLOW** — strongest sector signal. But FSLY's
  non-participation (phase-0.5) means it captures this only as a **generic** backdrop.

## Correlation (`uw risk portfolio-correlation`, 30d) `[MACRO:portfolio_correlation]`

| Pair | Corr | Flag |
|------|------|------|
| **FSLY / DDOG** | **−0.634** | MODERATE (negative) |
| NET / AKAM | −0.548 | (peer pair) |
| FSLY / NET, AKAM, ESTC | not high-corr | — |

- FSLY's **only** flagged correlation is **negative** (vs DDOG). It is **not**
  clustered with its CDN/infra-software peers → **idiosyncratic, low-beta (0.37)**.
  *Diversification positive*: a tech-led drawdown would not mechanically drag FSLY the
  way it would a high-beta cluster name (contrast CRM's 0.88 software cluster).

## Tool calls

```bash
uw risk market-regime                   --date 2026-05-29 --json
uw options-flow sector-flow-persistence --days 5 --json
uw risk portfolio-correlation --symbols FSLY,NET,AKAM,DDOG,ESTC --lookback-days 30 --json
```

## Tool errors

none (correlation/persistence anchor to latest available = as-of date; sector
breakdown returns "Unknown" GICS — cosmetic, sector taken from screener/phase-0).

## Read-through

- Macro is **not the engine of this trade.** The risk-on uptrend and Tech inflow are
  faint positives, but FSLY's near-zero/negative peer correlation and 0.37 beta mean
  the tape barely moves it. The thesis must stand on **FSLY-specific** structure: the
  14.6% short float + the $20/$22.5 call-OI ladder + cheap-vs-realized vol (phase-5).
- The **silver lining vs CRM:** where CRM was a 0.88-correlated highest-beta laggard
  (no shelter if tech reversed), FSLY is **uncorrelated/low-beta** — so a macro wobble
  is a *smaller* risk here. The flip side: there's no sector tailwind *pushing* it
  either; it needs its own ignition.
- **For phase-9:** treat macro as **neutral/mild-tailwind, non-decisive**; the
  narrow-breadth "half-size" guidance still applies to sizing, but the correlation
  gate is **clean** (no ≥0.70 cluster to cut against — in fact negatively correlated).

## Citations

- `[MACRO:market-regime]` TRANSITIONAL/UPTREND, breadth 36.3% bullish, "half-size" — `uw risk market-regime`
- `[MACRO:sector_flow_persistence]` Tech #1 inflow +$533.3M, persistence 1.0 — `uw risk market-regime` / `sector-flow-persistence`
- `[MACRO:portfolio_correlation]` FSLY/DDOG −0.634; not clustered with CDN peers; beta 0.37 → idiosyncratic — `uw risk portfolio-correlation`

## Upstream references

- phase-0.5-context.md §Sector read — "Technology leading; FSLY not participating in
  size"; phase-6 confirms the sector tailwind is generic and FSLY's edge is
  idiosyncratic (low beta, negative peer correlation).
- phase-3-positioning.md §Summary — "squeeze ladder + 14.6% short float"; phase-6
  reinforces that this FSLY-specific structure, not macro beta, is the thesis engine.

## Next phase

- phase-7-insights.md (does the composite synthesis line up the quiet-flow / bullish-
  OI / cheap-vol / squeeze-structure reads into a single scenario?)
