# Phase 6 — Macro Overlay

**Ticker:** DOCN
**As-of date:** 2026-07-17
**Generated:** 2026-07-20T02:05:00Z
**Upstream phases cited:** phase-0.5-context.md, phase-4-structure.md, phase-5-historical.md

## Summary

The macro tape is **TRANSITIONAL / CHOPPY** — SPY below its 20- & 50-day SMAs,
market breadth negative (UW 38.4% bullish; fz 29% green), UW guidance literally
"half position sizes, favor defined-risk, iron condors in range." DOCN's sector
(**Technology**) is paradoxically the **#1 options-flow inflow sector (+$1.17B, 5-day
persistence 0.8)** yet was **−1.09% on price today** — flow rotating into a soft
tape. Rates are a mild headwind for long-duration software: **10y 4.57% (rising),
inflation sticky ~3.5%, and the 7/29 FOMC carries a ~25% *hike* risk (no cut
priced).** Critically, WebSearch resolves DOCN's −34% crash as **mostly technical +
capital-structure**: a **Russell 2000→1000 rebalance "sell-the-news," a $500M
convertible-note repurchase funded by a dilutive equity offering, and fundamental
worries** (hyperscaler pressure, SMB net-retention, AI capex). Net macro bias:
**neutral-to-mild-headwind**; the sector-flow tailwind is undercut by DOCN being
the sector *laggard* and by rates/breadth.

## Key signals

- Regime **TRANSITIONAL/CHOPPY**, SPY 743.29 (−0.94% 30d, below 20/50 SMA),
  breadth **38.4% bullish** `[MACRO:MarketRegime_2026-07-17 UW]` — half size,
  defined-risk (aligns with phase-5's premium-selling read).
- **Technology = #1 inflow sector +$1.17B, persistence 0.8** `[MACRO:sector_flow UW]`
  `[MACRO:sector_flow_persistence UW]` — durable rotation IN → sector tailwind…
- …but Technology **−1.09% price today**, PEG 0.91, Fwd P/E 25.9
  `[MACRO:group_valuation fz EOD]` and DOCN is −34% in 30d → **DOCN is the sector
  laggard; the weakness is idiosyncratic, not sector-wide.**
- **DOCN crash cause = Russell 1000 rebalance sell-the-news + $500M convert
  repurchase via dilutive equity offering + competitive/SMB/AI-capex concerns**
  `[MACRO:DOCN_2026-07 WebSearch:marketbeat.com/trefis.com]`.
- Rates headwind: **10y 4.57%** (up from 4.44 30d ago), **2s10s +0.37 (normal)**,
  **7/29 FOMC** hold-expected but **~25% hike odds, no cut** `[MACRO:DGS10_2026-07-16
  FRED]` `[MACRO:FOMC_2026-07-29 WebSearch:federalreserve.gov]`.

## Detailed findings

### Market regime (UW) `[MACRO:MarketRegime_2026-07-17 UW]`

- regime: **TRANSITIONAL — Mixed signals, reduce position size, wait for clarity**;
  trend **CHOPPY**; trading_guidance: "Half position sizes. Favor defined-risk
  strategies. Iron condors in range."
- SPY 743.29 · above_20sma **false** · above_50sma **false** · 30d −0.94% ·
  −2.25% from 90d high.
- breadth: **38.4% bullish** (2,420 bullish vs 3,878 bearish of 6,298 optionable).
- sector_rotation (regime tool): IN → Technology +$98.6M, Energy +$30M, Comm Svcs
  +$29.7M; OUT → Financial Services −$57.2M, Consumer Cyclical −$45.3M.

### Inflation (FRED) `[MACRO:CPIAUCSL_2026-06 FRED]`

| Series | Latest (date) | YoY | Note |
|--------|---------------|-----|------|
| CPI (CPIAUCSL) | 332.568 (Jun) | **+3.46%** | MoM −0.4% (May 333.979) — cooling |
| Core CPI (CPILFESL) | 336.065 (Jun) | **+2.57%** | flat MoM |
| Core PCE (PCEPILFE) | 130.082 (May) | **+3.41%** | still above target |

Inflation moderating but **sticky ~2.6–3.5%** → keeps the Fed on a hold/hike bias,
not a cutting path. Mild headwind for rate-sensitive growth.

### Labor (FRED) `[MACRO:UNRATE_2026-06 FRED]`

- Unemployment **4.2%** (Jun, down from 4.3% May). Nonfarm payrolls 158,984k,
  **+57k MoM**. Labor solid → no recession signal, but no dovish trigger either.

### Rates (FRED + FOMC) `[MACRO:DFF_2026-07-16 FRED]`

- Fed funds effective **3.63%** (target 3.50–3.75%, held at June 16-17 FOMC).
- **10y 4.57%** (up from 4.44% 30d ago), 2y 4.16%, **2s10s +0.37 (normal/steepening)**.
- USD (DTWEXBGS) 120.50, softening from 121.41 (mild risk-supportive).
- **Next FOMC 7/29** (decision 7/29 2pm ET): consensus **hold**; fixed-income prices
  ~**25% hike** odds by July, higher by Sep/Dec. **No cut priced.** Rising 10y +
  hike-tail is a **valuation headwind** for long-duration software like DOCN.

### Activity / Consumer

- Not separately pulled (single-ticker overlay); the negative breadth + CHOPPY
  regime already capture the risk tone. Marked neutral.

### Sector overlay (Technology / cloud-infra software)

- UW sector-flow: **Technology net +$1.17B (rank #1)**; regime tool: +$98.6M net
  (different net-of-noise measure) — both #1 inflow.
- fz Technology group: P/E 35.19, **Fwd P/E 25.94, PEG 0.91**, EPS-next-5Y 38.83%,
  **Change −1.09% today** `[MACRO:group_valuation fz EOD]`.
- fz breadth (whole market): advancers 147 / decliners 356, **pct_green 29.2%**
  `[MACRO:sector_breadth fz EOD]` — corroborates UW's weak breadth.

### Sector rotation `[MACRO:sector_flow_persistence UW]`

- Technology **persistence 0.8** (high 5-session sign-consistency) → the inflow is
  **durable, not a one-day blip.**
- **Verdict vs thesis:** sector flow is **ALIGNED** for a long/recovery thesis
  (money durably entering tech) — **BUT DOCN is the sector laggard** (−34% while the
  sector's flow is positive), so the sector tailwind does **not** rescue DOCN; the
  problem is company-specific (Russell/convert/competition). Treat as **neutral for
  DOCN specifically** despite the aligned sector flow.

### Cross-name correlation `[MACRO:portfolio_correlation UW]`

- Correlated against concurrent 2026-07-17 blueprints: **NOW, OKLO, PATH, RKT, SHOP**
  (6 symbols incl. DOCN), 30d lookback.
- High-correlation pairs (≥0.58): **NOW/PATH 0.798, PATH/SHOP 0.707, NOW/SHOP 0.58**
  — **DOCN appears in NONE of them.** DOCN is uncorrelated with the other positions
  over the window (it de-coupled during its idiosyncratic crash).
- (Sector field returns "Unknown" — the known-broken UW sector field; the
  coefficients themselves are valid per prior audit.)
- **Correlation verdict: NO cluster, NO soft-watch for DOCN.** No size cut from
  correlation. (The NOW/PATH/SHOP cluster is a concern for *those* blueprints, not
  DOCN.)

## Tailwind / Headwind table

| Datapoint | Latest | Release | Source | Impact on DOCN (tech/cloud) |
|-----------|--------|---------|--------|------------------------------|
| Tech sector flow | +$1.17B #1, persist 0.8 | 2026-07-17 | UW | **tailwind (sector)** |
| DOCN vs sector | −34% 30d vs sector inflow | 2026-07-17 | UW/WebSearch | **headwind (idiosyncratic)** |
| Market breadth | 38.4% bull / 29% green | 2026-07-17 | UW/fz | headwind |
| 10y yield | 4.57% (rising) | 2026-07-16 | FRED | headwind (duration) |
| FOMC 7/29 | hold, ~25% hike, no cut | 2026-07-29 | WebSearch | headwind/neutral |
| Core CPI YoY | 2.57% | 2026-06 | FRED | neutral |
| Unemployment | 4.2% | 2026-06 | FRED | neutral |
| USD | 120.5 (softening) | 2026-07-10 | FRED | mild tailwind |
| Russell rebalance | 2000→1000 sell-news | 2026-07 | WebSearch | headwind (fading?) |
| $500M convert repurchase | dilutive equity offer | 2026-07 | WebSearch | headwind |

## Catalyst calendar (next 30d)

**Front-expiry implied move: ±1.80% / $2.14** `[CTX:implied_move_pct]` (near-dated;
the 8/7 earnings expiry prices a far larger move — IV 117.9%, phase-4).

| Date | Event | Likely impact | vs expected move |
|------|-------|---------------|------------------|
| **2026-07-29** | **FOMC decision** | hold likely; ~25% hike tail = risk-off for duration tech | can exceed ±1.8% front move |
| **2026-08-04** | **DOCN Q2 earnings** | dominant binary; post −34% crash, high-stakes; guidance Q2 EPS 0.20–0.23 / FY 1.10–1.20 | **far exceeds** front ±1.8%; IV hump 117.9% at 8/7 prices a large gap |
| ongoing | Russell rebalance flow / convert-offer overhang | forced-selling may be exhausting → potential base | — |

## Tool / source errors

- FRED: **key present** (repo `.env`); all 10 series returned valid JSON. No skip.
- `fz groups` first jq path (`.rows`) failed — the payload is a top-level **array**;
  re-read against `.[]` (Technology row extracted correctly). Recorded as a
  path-correction, not a tool failure.
- WebSearch returned dataset-consistent DOCN 2026 coverage ($119.65 on 7/15, ~$15B
  cap, Russell 1000 add) — used for the crash-cause attribution and FOMC calendar.

## Verdict for downstream phases

- **Net macro bias for DOCN:** **NEUTRAL-to-mild-HEADWIND.** Durable tech-sector
  inflow (tailwind) is offset by weak breadth, rising 10y + FOMC hike-tail, and —
  decisively — DOCN's idiosyncratic drivers (Russell sell-news, dilutive convert,
  competitive/SMB/AI-capex concerns). The sector is bid; DOCN is the laggard.
- **Conviction:** **3/5** (regime + rates + crash-cause are well-sourced).
- **Top 2 datapoints phase-9 must cite:** (1) Regime TRANSITIONAL → half size /
  defined-risk / iron-condor-in-range guidance; (2) Tech sector +$1.17B inflow
  persistence 0.8 vs DOCN −34% (aligned sector, idiosyncratic laggard).
- **Top 2 catalysts for phase-9 calendar:** (1) **8/4 earnings** (dominant binary,
  large priced move); (2) **7/29 FOMC** (hike-tail duration risk).
- **Sector-rotation verdict:** **ALIGNED (sector) / NEUTRAL (DOCN)** — persistence
  0.8; sector tailwind does not transfer to the laggard. Not a size *adder*.
- **Correlation verdict:** **No concurrent-position cluster for DOCN** (absent from
  all ≥0.58 pairs; NOW/PATH 0.80 & PATH/SHOP 0.71 are among the *other* blueprints).
  No correlation size cut.
