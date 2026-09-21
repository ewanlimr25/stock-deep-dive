# Phase 6 — Macro Overlay

**Ticker:** OKLO
**As-of date:** 2026-07-17
**Generated:** 2026-07-18T00:00:00Z
**Upstream phases cited:** phase-0.5-context.md, phase-5-historical.md

## Summary

The macro backdrop is a **mild net headwind** that aligns with the bearish single-name
thesis. The market regime is **TRANSITIONAL** (SPY below its 20- and 50-SMA, −0.94% 30d,
IV rank rising 14→28), breadth is **negative (38.4% bullish; 3,878 bearish vs 2,420 bullish
names)**, and UW's own guidance is *"half position sizes, favor defined-risk, iron condors
in range."* Rates are an active headwind for a **pre-revenue, long-duration** name: **10y
4.57%**, Fed funds 3.63% (cutting cycle), curve normal (+0.37). OKLO's **Utilities sector
ranks 10th of 11** on net premium ($12M) and saw a **−$138M outflow on 07-16** (its
gap-down day). Most importantly, WebSearch confirms a **genuine fundamental de-rating**
behind the −42% YTD move: fading nuclear hype, slipping milestones, zero revenue, record
cash burn (−$154M FCF TTM), **dilutive equity raises**, DOE's $17.5B loan program tilting
to *large* reactors (not SMRs), and **Russell index deletions** in late June.

## Key signals

- **Regime TRANSITIONAL, breadth 38.4% bullish** — risk-off lean; guidance = half-size,
  defined-risk [MACRO:MarketRegime_2026-07-17 UW]
- **10y 4.57% / Fed funds 3.63% / 2s10s +0.37** — elevated long rates pressure a
  zero-cash-flow duration name [MACRO:DGS10_2026-07-16 FRED]
- **Utilities sector 10th of 11** on net premium ($12M), −$138M outflow on 07-16
  [MACRO:sector_flow_2026-07-17 UW]
- **Fundamental de-rating confirmed**: milestones slipping, record cash burn −$154M,
  dilution, Russell deletions, DOE tilt to large reactors [MACRO:OKLO_2026-07-16 WebSearch:247wallst.com]
- **Inflation moderate**: CPI 3.46% YoY, Core CPI 2.56% YoY — not the driver here
  [MACRO:CPIAUCSL_2026-06 FRED]

## Detailed findings

### Market regime — [MACRO:MarketRegime_2026-07-17 UW]

Label: **"TRANSITIONAL — Mixed signals, reduce position size, wait for clarity."** SPY
$743.29, **below** 20-SMA (745.02) and 50-SMA (744.38), −0.94% 30d, −2.25% from 90d high.
SPY 10d IV rank rose 14.4 → 27.8 (vol waking up). Breadth: **bullish_pct 38.4%** (3,878
bearish-flow / 2,420 bullish-flow tickers). Guidance verbatim: *"Half position sizes. Favor
defined-risk strategies. Iron condors in range."*

### Inflation — [MACRO:CPIAUCSL / CPILFESL_2026-06 FRED]

CPI index 332.568 (Jun) → **YoY +3.46%**; Core CPI **YoY +2.56%**. Moderate, disinflationary
trend; not a first-order driver for OKLO but keeps the Fed's cutting path measured.

### Labor — [MACRO:UNRATE_2026-06 FRED]

Unemployment **4.2%** (Jun), down from 4.3% (May/Apr). Labor stable — no recession signal,
no acute risk-off trigger.

### Rates — [MACRO:DGS10/DGS2/T10Y2Y/DFF FRED]

10y **4.57%** (07-16), 2y **4.16%**, 2s10s **+0.37** (normal, mildly flattening from +0.42),
Fed funds effective **3.63%** (mid-cutting-cycle). **Elevated long-end yields are a
structural headwind for a pre-revenue nuclear developer** whose value is entirely in
distant cash flows — the discount rate matters more here than for a profitable name.

### Activity / Consumer

Not separately pulled (single-name overlay; regime + rates + sector suffice). No known
imminent ISM/confidence print that changes the OKLO-specific read.

### Sector overlay + rotation — [MACRO:sector_flow / sector_flow_persistence UW]

Full sector net-premium ranking today:

| Rank | Sector | Net premium |
|---|---|---|
| 1 | Technology | $1,173M |
| 2 | Comm Services | $367M |
| 3 | Consumer Cyclical | $280M |
| … | … | … |
| 10 | **Utilities (OKLO)** | **$12M** |
| 11 | Industrials | −$384M |

Regime `money_flowing_in`: Technology (+$98.6M), Energy (+$30M), Comm Services (+$29.7M);
`out`: Financials (−$57M), Consumer Cyclical (−$45M). **Utilities is in neither** — mid/low
pack. 5-day persistence: Utilities `persistence_score 0.8`, nominal trend **INFLOW** by
sign-count, **but** the daily series is dominated by a **−$137.8M outflow on 07-16** (OKLO's
gap-down day): +14.6M / +36.7M / +14.9M / **−137.8M** / +12.1M.
- **Rotation verdict vs the (bearish) thesis: mildly ALIGNED / neutral** — OKLO's sector is
  a laggard bottom-ranked group that bled money on the break day; a weak sector supports a
  short, though the sign-persistence is technically positive so it is not a strong tailwind
  for the short. Recall phase-0.5: within the nuclear theme, flow favors **CCJ/GEV/BE**, not
  OKLO — relative weakness intact.

### Cross-name correlation — [MACRO:portfolio_correlation UW]

**No concurrent positions** — OKLO is the only blueprint for 2026-07-17
(`ls research/*/2026-07-17/` → OKLO only). Correlation gate **skipped**; no cluster risk to flag.

## Tailwind / Headwind table

| Datapoint | Latest | Release | Source | Impact on OKLO (Utilities/nuclear) |
|---|---|---|---|---|
| Market regime | TRANSITIONAL, 38.4% bullish | 2026-07-17 | UW | **headwind** (risk-off, half-size) |
| 10y yield | 4.57% | 2026-07-16 | FRED | **headwind** (duration/discount-rate) |
| Fed funds | 3.63% (cutting) | 2026-07-16 | FRED | mild tailwind (easing) — outweighed by 10y |
| 2s10s | +0.37 normal | 2026-07-17 | FRED | neutral |
| CPI YoY | 3.46% | 2026-06 | FRED | neutral |
| Core CPI YoY | 2.56% | 2026-06 | FRED | neutral |
| Unemployment | 4.2% | 2026-06 | FRED | neutral |
| Utilities sector flow | 10/11, $12M, −$138M on 07-16 | 2026-07-17 | UW | mild headwind for the name |
| Nuclear-theme fundamentals | de-rating (milestones, cash burn, dilution, Russell deletion) | 2026-07-16 | WebSearch | **headwind** |

## Catalyst calendar (next 30d)

**Front-expiry implied move:** `implied_move_perc` 0.00733 → **±0.73%** from the deep-dive
`uw_screener` block [CTX:implied_move] — **this near-dated figure is implausibly small for a
97% IV name and should NOT be used raw.** Phase-9 must reconcile: at IV30d ~97%, the
expected move to the **2026-08-10 earnings (~24 sessions out)** is ≈ 97% × √(24/365) ≈
**±25%**. Size structures to that, not to ±0.73%.

| Date | Event | Likely impact | vs expected move |
|---|---|---|---|
| 2026-08-10 | **OKLO earnings** (pre-revenue → guidance/milestone update) | HIGH — binary; short-squeeze risk if milestones reaffirmed | ~±25% priced (IV-derived) |
| late-Jul → Aug | Ongoing dilution / capital-raise headlines | headwind | inside |
| next FOMC (per cutting cycle) | rate path | 2nd-order | inside |

## Tool / source errors

None fatal. FRED key present and working (7 series pulled). `today-gamma-flip` /
ISM / consumer prints not separately queried (single-name overlay). `implied_move_perc`
flagged as a suspect near-dated value (see calendar).

## Verdict for downstream

- **Net macro bias for OKLO:** **HEADWIND** (mild-to-moderate). Risk-off regime + elevated
  long rates + a bottom-ranked sector + a confirmed fundamental de-rating all lean against
  the name — i.e. *aligned with the bearish thesis*.
- **Conviction:** 3 / 5 (macro is a supporting headwind, not the primary driver; the
  fundamental de-rating is the strongest macro-adjacent input).
- **Top 2 datapoints phase-9 must cite:** (1) Regime TRANSITIONAL / breadth 38.4% / "half
  size, defined-risk"; (2) 10y 4.57% as a duration headwind for a zero-cash-flow name.
- **Top 2 catalysts for the calendar:** (1) **2026-08-10 earnings** (~±25% IV-implied,
  binary, squeeze risk); (2) ongoing dilution / capital-raise headlines.
- **Sector-rotation verdict:** **mildly ALIGNED / neutral** with the bearish thesis
  (Utilities 10/11, −$138M on the break day; persistence 0.8 nominal-inflow). Phase-9: not a
  size booster, a mild confirm.
- **Correlation verdict:** **no concurrent positions** — gate skipped, no cluster.

Sources:
- [Oklo Just Dropped 28% in a Month — 247 Wall St](https://247wallst.com/investing/2026/07/16/oklo-just-dropped-28-in-a-month-is-it-time-to-abandon-nuclear-stocks-like-oklo-nuscale-and-uranium-energy-corp/)
- [Oklo Stock Is Down 41% in 2026 — Motley Fool](https://www.fool.com/investing/2026/07/15/oklo-stock-is-sliding-what-investors-need-to-under/)
- [Why Oklo Stock Sank 27% In The First Half of 2026 — Motley Fool](https://www.fool.com/investing/2026/07/11/why-oklo-stock-sank-27-in-the-first-half-of-2026/)
- [Oklo Stock Is Tumbling Today — Benzinga](https://www.benzinga.com/trading-ideas/movers/26/07/60507989/oklo-stock-is-tumbling-today-heres-what-the-chart-is-signaling)
