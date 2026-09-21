# Phase 6 — Macro & Market Regime

## Summary

The macro backdrop is a **net tailwind for a tactical CRM long, with one breadth
caveat.** Three reads:

- **Market regime TRANSITIONAL but trend UPTREND.** SPY $756.48 is above its 20-
  and 50-day SMAs (739 / 704), **+6.31% over 30 days**, only **−0.21% from its
  90-day high.** The "TRANSITIONAL" tag comes from **weak breadth** — just **36.3%
  of 6,187 optionable tickers show bullish flow** (2,247 bull vs 3,940 bear). So:
  index strong, participation narrow. The regime engine advises **half size,
  defined-risk** — which dovetails exactly with phases 2/5.
- **CRM's sector is THE money-magnet.** Sector rotation shows **Technology +$533.3M
  inflow today — the single largest of any sector** (vs outflows in Comm Services
  −$104M, Consumer Cyclical −$50M, Basic Materials −$20M). And it's **persistent**:
  Technology sector-flow **persistence score 1.0 (perfect), trend INFLOW**, five
  consecutive sessions of positive net flow ($6.2B→$8.7B→$8.5B→$7.1B→**$11.6B** on
  5/29). The narrow-breadth tape is concentrating *into tech* — and CRM is tech.
- **CRM is a high-beta software-basket name (β 1.13).** 30-day correlations:
  **CRM/NOW 0.89, CRM/ADBE 0.88, CRM/MSFT 0.74** — CRM moves with the software
  complex that is leading the inflow. The sector tailwind transmits *directly* to
  CRM; but the same correlation means **if tech rolls over, CRM has no idiosyncratic
  shelter** (and it's the highest-beta laggard of the group).

**Macro verdict: MODEST-TO-GOOD TAILWIND.** Uptrending index + the strongest,
most-persistent sector inflow in the market, transmitted to CRM via 0.88+ software
correlation. The offsets — narrow breadth (36% bullish) and the regime's explicit
"half-size / defined-risk" guidance — argue for **participating, but small and
hedged**, not pressing. This *supports* the phase-1 flow case more than it tempers it.

## Market regime (`uw risk market-regime`) `[MACRO:market-regime]`

| Field | Value |
|-------|-------|
| Regime | **TRANSITIONAL** — "reduce size, wait for clarity" |
| Trend | **UPTREND** |
| SPY | $756.48 (above 20sma 739 / 50sma 704) |
| SPY 30d change | **+6.31%** |
| SPY vs 90d high | **−0.21%** (at the highs) |
| Market breadth | **36.3% bullish** (2,247 bull / 3,940 bear of 6,187) |
| Guidance | **Half position sizes; favor defined-risk** |

## Sector rotation (`uw risk market-regime` + `sector-flow`) `[MACRO:sector_rotation]`

| Direction | Sectors |
|-----------|---------|
| **In** | **Technology +$533.3M**, Utilities +$2.5M, Energy +$0.5M |
| Out | Comm Services −$104.3M, Consumer Cyclical −$49.8M, Basic Materials −$20.4M |

- Sector-flow sentiment (whole tape): **Technology net flow +$11.6B**, call premium
  **$16.0B vs put $4.3B** — overwhelmingly bullish at the sector level.

## Sector persistence (`uw options-flow sector-flow-persistence`, 5d) `[MACRO:sector_flow_persistence]`

| Session | Tech net flow |
|---------|---------------|
| 2026-05-22 | +$6.19B |
| 2026-05-26 | +$8.72B |
| 2026-05-27 | +$8.50B |
| 2026-05-28 | +$7.14B |
| **2026-05-29** | **+$11.62B** |

- **persistence_score 1.0 (perfect), trend INFLOW.** Five straight up-sessions,
  accelerating into 5/29. This is the strongest, cleanest sector signal in the dive.

## Correlation (`uw risk portfolio-correlation`, 30d) `[MACRO:portfolio_correlation]`

| Pair | Corr | Flag |
|------|------|------|
| CRM / NOW | **0.89** | HIGH |
| CRM / ADBE | **0.88** | HIGH |
| CRM / MSFT | 0.74 | MODERATE |

- CRM trades as part of the software complex (β 1.13). Sector tailwind transmits
  directly; correlation also = no diversification/shelter if tech reverses.
- (`sector_breakdown` returned "Unknown" — the correlation tool doesn't tag GICS
  here; sector identity taken from screener/phase-0. Cosmetic, not blocking.)

## Tool calls

```bash
uw risk market-regime                       --date 2026-05-29 --json
uw options-flow sector-flow                 --date 2026-05-29 --json
uw options-flow sector-flow-persistence     --days 5 --json
uw risk portfolio-correlation --symbols CRM,MSFT,ORCL,NOW,ADBE --lookback-days 30 --json
```

## Tool errors

- `sector-flow-persistence` takes no `--sector`/`--date` (returns all sectors at
  latest; filtered to Technology in post). `portfolio-correlation` takes no `--date`
  (uses trailing 30d to latest). Both anchor to the latest available date = the
  as-of date here, so as-of-correct. Noted, not blocking.

## Read-through

- Macro **reinforces the bull side of the central divergence.** The single most
  persistent flow signal in the entire market right now is **money pouring into
  Technology** (perfect persistence, 5 sessions, accelerating), and CRM is a 0.88-
  correlated software name. A beaten-down (−27.86% YTD) laggard catching a bid while
  its sector is the market's money-magnet is a coherent **catch-up/rotation-long**
  setup — and it's the cross-sectional question phase-0.5 flagged ("laggard in a
  leading sector"), now answered: **the sector leadership is real and persistent**,
  which favors the laggard closing the gap.
- **The caveats keep it disciplined:** (1) breadth is narrow (36% bullish) — this is
  a concentrated, top-heavy tape, the kind that can unwind quickly; (2) the regime
  engine itself says **half-size, defined-risk**; (3) CRM's 0.88 software correlation
  means a tech reversal hits it with no shelter, and as the group's highest-beta
  laggard it would likely fall hardest. These align with phase-2 (distribution) and
  phase-5 (no accumulation backing) → **size small, define risk, prefer hedged
  structure.**
- **Net:** macro is a *tailwind that argues for taking the long*, while every risk
  overlay (breadth, regime guidance, correlation) argues for *taking it small and
  defined-risk*. That is the shape phase-9 should build.

## Citations

- `[MACRO:market-regime]` TRANSITIONAL/UPTREND, SPY −0.21% from 90d high, breadth 36.3% bullish, "half-size" — `uw risk market-regime`
- `[MACRO:sector_rotation]` Technology +$533.3M = largest sector inflow; sector net flow +$11.6B — `uw risk market-regime` / `sector-flow`
- `[MACRO:sector_flow_persistence]` Tech persistence 1.0, INFLOW, 5 straight sessions to +$11.6B — `uw options-flow sector-flow-persistence`
- `[MACRO:portfolio_correlation]` CRM/NOW 0.89, CRM/ADBE 0.88, CRM/MSFT 0.74 — `uw risk portfolio-correlation`

## Upstream references

- phase-0.5-context.md §Sector read — "Technology leading the tape; CRM lagging
  within it"; phase-6 confirms the leadership is **persistent (score 1.0, 5
  sessions)** and frames CRM as a catch-up-long candidate.
- phase-5-historical.md §Sizing — "keep Kelly fractional"; phase-6's narrow breadth +
  "half-size" regime guidance independently corroborates fractional sizing.

## Next phase

- phase-7-insights.md (does the composite synthesis — conviction matrix, signal
  confluence, analyst-vs-flow, price-vs-flow — line up the bull-flow/bear-darkpool
  divergence into a single scenario classification?)
