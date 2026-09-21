# Phase 6 — Macro Overlay

**Ticker:** BBAI
**As-of date:** 2026-05-29
**Generated:** 2026-05-31
**Upstream phases cited:** phase-0.5-context.md, phase-1-flow.md, phase-5-historical.md

## Summary

The macro backdrop is a **net headwind for a speculative high-beta long, partly
offset by a real idiosyncratic catalyst.** The UW market-regime read is
**`TRANSITIONAL — Mixed signals, reduce position size, wait for clarity`** with
**weak breadth (36.3% of 6,187 optionable names bullish; 3,940 bearish vs 2,247
bullish)**. The macro tape is **late-cycle**: the S&P 500 is at a record (>7,300, a
6-week win streak) but stretched; **rate cuts are off the table for 2026**,
inflation is sticky (~April CPI +3.7% YoY headline / +2.7% core), and a **hawkish
Fed-chair transition** is underway (Powell's term ended May 15, 2026). The lone
clear positive: **Technology is the dominant sector inflow today (+$533.3M net)**,
and BBAI has a **genuine fundamental tailwind** — a defense-AI contract backlog of
**$281.9M (+14% QoQ)** including a **$53M classified sole-source award**, a Q1
revenue beat ($34.4M vs $33.6M), and the bounce off $3 is news-driven. Net: macro =
**headwind/caution** for chasing; **supportive of the phase-1/4/5 fade-the-extension
lean**, with the contract catalyst the main two-sided risk.

## Key signals

- **Regime TRANSITIONAL — "reduce position size, wait for clarity"**; breadth
  bullish_pct **36.3%** (3,940 bearish vs 2,247 bullish tickers) [MACRO:MarketRegime_2026-05-29 UW]
- **Technology = dominant sector inflow +$533.3M** (vs Energy $0.5M, Utilities
  $2.5M) → sector tailwind for an AI name [MACRO:sector_rotation_2026-05-29 UW]
- **Rate cuts off the table 2026; sticky ~3% inflation; hawkish Fed-chair
  transition** (Powell term ended 2026-05-15) [MACRO:Fed_2026-05 WebSearch:ishares.com]
- **April CPI +3.7% YoY headline / +2.7% core** (released ~May 12) [MACRO:CPI_2026-04 WebSearch:heygotrade.com]
- **BBAI catalyst: defense backlog $281.9M (+14% QoQ), $53M classified award, Q1
  beat** — the real driver of the +32%/mo bounce [MACRO:BBAI_news_2026-05 WebSearch:foreignpolicyjournal.com]
- **Front-expiry implied move ≈ ±6.8%** (screener `implied_move` 0.0679) — phase-9
  sizes structures to this [CTX:implied_move]

## Detailed findings

### Market regime (`uw risk market-regime`)

- `regime`: **TRANSITIONAL — Mixed signals, reduce position size, wait for clarity**.
- `market_breadth`: 6,187 optionable tickers; **bullish_pct 36.3%** (bullish_flow
  2,247 vs bearish_flow 3,940) → **breadth skewed bearish** market-wide.
- `sector_rotation.money_flowing_in`: **Technology +$533,349,600** (dominant),
  Utilities +$2,509,698, Energy +$472,501.
- Read: a "reduce size / wait" regime with bearish breadth is a **headwind** for a
  speculative small-cap; the Tech inflow is a partial offset, but it is concentrated
  in mega-cap software/index (phase-0.5), not small-cap AI.

### Macro backdrop (WebSearch)

- **Rates/Fed:** 2026 rate cuts "off the table"; new Fed chair labeled a hawk;
  Powell's term expired 2026-05-15 — leadership-transition uncertainty is live.
- **Inflation:** April CPI +0.6% MoM / **+3.7% YoY** headline, +0.3% MoM / **+2.7%
  YoY** core; inflation "sticky near 3%, above target."
- **Equities:** S&P 500 at a record (>7,300), longest 6-week streak since 2024, but
  flagged stretched/correction-prone. Headwinds: slowing jobs, sticky inflation,
  tariff aftermath, Fed uncertainty.
- **Net:** late-cycle, risk-on-but-fragile — historically unkind to unprofitable
  high-beta speculative names on a pullback.

### Sector rotation

- UW: **Technology is the day's top net inflow (+$533M)** → sector tailwind. But
  phase-0.5 showed the directional leaders are mega-cap software/index (MSFT, NDX,
  DELL, ORCL, PLTR), not small-cap AI; BBAI rides the theme, doesn't lead it.
- `sector-flow-persistence` (5-day persistence) **not captured** — the leaf
  rejected `--date`; recorded as a tool gap (see errors). Rotation verdict from the
  single-day regime read: **aligned-but-shallow** (Tech in favor, BBAI peripheral).
- `fz` sector-breadth overlay **skipped** (the `group-performance` leaf returned
  empty in this run) — advisory only, no impact on the verdict.

### BBAI-specific catalyst (WebSearch)

- Backlog **$281.9M, +14% QoQ**, incl a **$53M classified sole-source** military
  award (12–24mo revenue conversion). Q1: EPS −$0.12 (narrowed from −$0.25), revenue
  **$34.4M beat $33.6M**; ~$75M new wins; acquisitions Ask Sage + CargoSeer. Guidance
  25–35% backlog-to-revenue → ~$70–100M 2026 revenue adds. Stock ran ~$4.20 (5/22) →
  $5.04 (5/29) on this momentum. **Next earnings 2026-08-10** (outside 30d).

### Cross-name correlation

- `uw risk portfolio-correlation` errored (`unknown flag: --symbol`; the leaf needs
  `--symbols` and is flagged unreliable in project notes). **No concurrent
  2026-05-29 blueprint** was confirmed in `research/*/2026-05-29/` → **no concurrent
  positions to correlate against**; correlation gate skipped.

## Tailwind / Headwind table

| Datapoint | Latest value | Release/asof | Source | Impact on BBAI (small-cap AI/defense) |
|-----------|--------------|--------------|--------|----------------------------------------|
| Market regime | TRANSITIONAL / reduce size | 2026-05-29 | UW | **headwind** |
| Breadth | 36.3% bullish | 2026-05-29 | UW | **headwind** |
| Fed / rates | no 2026 cuts, hawkish transition | 2026-05 | WebSearch | **headwind** |
| CPI YoY | +3.7% headline / +2.7% core | 2026-04 | WebSearch | **headwind** (sticky) |
| Tech sector flow | +$533M inflow | 2026-05-29 | UW | **tailwind** (sector) |
| S&P 500 | record >7,300, stretched | 2026-05 | WebSearch | mixed |
| BBAI backlog/contracts | $281.9M (+14% QoQ), $53M classified | 2026-05 | WebSearch | **tailwind** (idiosyncratic) |

## Catalyst calendar (next 30d)

Front-expiry implied (expected) move: **≈ ±6.8%** (`implied_move` 0.0679; phase-9
sizes to this — N4).

| Date | Event | Likely impact | vs expected move |
|------|-------|---------------|------------------|
| 2026-06-05 | Weekly OPEX | gamma/pin mechanics (phase-4) | inside ±6.8% |
| ~2026-06-10/12 | May CPI release | rate-path repricing | could exceed if hot |
| ~2026-06-17 | FOMC meeting | hawkish-hold risk | could exceed |
| 2026-06-18 | Monthly OPEX (OI cliff, phase-3) | $5 pin / unwind | pivot |
| 2026-08-10 | BBAI Q2 earnings | binary (outside 30d) | n/a this window |

## Tool / source errors

- `uw options-flow sector-flow-persistence --date` → `unknown flag: --date`
  (persistence not captured; single-day rotation used instead).
- `uw risk portfolio-correlation --symbol` → `unknown flag: --symbol` (needs
  `--symbols`; leaf unreliable per project notes) — correlation gate skipped (no
  concurrent blueprint anyway).
- `fz group-performance` returned empty (advisory breadth overlay skipped).
- FRED not queried (no key configured); macro sourced via WebSearch per skill rule 4.

## Verdict for downstream

- **Net macro bias for BBAI:** **headwind / caution** (TRANSITIONAL regime +
  weak breadth + hawkish-Fed/sticky-inflation late cycle), partly offset by Tech
  sector inflows and BBAI's genuine contract catalyst.
- **Conviction:** 3/5.
- **Top 2 datapoints for phase-9 macro overlay:** regime **TRANSITIONAL/reduce-size
  (breadth 36.3%)**; **no 2026 rate cuts + sticky CPI +3.7%**.
- **Top 2 catalysts for the calendar:** **6/18 monthly OPEX** (OI cliff / $5 pin);
  **June FOMC + May CPI** (macro repricing).
- **Sector-rotation verdict:** **aligned-but-shallow** (Tech inflow tailwind; BBAI
  peripheral) — persistence score unavailable (tool gap).
- **Correlation verdict:** **no concurrent positions** for 2026-05-29 → no cluster.
