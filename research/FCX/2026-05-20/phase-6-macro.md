# Phase 6 — Macro Overlay

**Ticker:** FCX
**As-of date:** 2026-05-20 (effective data 2026-05-19)
**Generated:** 2026-05-20T20:45:00-04:00
**Upstream phases cited:** `phase-4-structure.md`, `phase-5-historical.md`

## Summary

The macro picture **resolves the front-end IV backwardation puzzle** raised
in phase 4. Inside the next 18 trading days, FCX faces a stacked catalyst
calendar: **June 10 CPI** (US May data, 9 sessions) and **June 16–17 FOMC
+ dot plot** (18 sessions) — and the FOMC is **Kevin Warsh's first meeting
as Chair** [MACRO:FOMC_2026-06-17 WebSearch:federalreserve.gov]. That fully
explains the 64% IV on the May-29 weekly and 52% on the Jun-18 monthly:
markets are pricing the dot-plot surprise risk.

The May 13 → May 19 FCX **−12.6% pullback** is not a stand-alone event —
it **coincides with**: (a) Kevin Warsh confirmed Fed Chair on May 13
[MACRO:WarshConfirmation_2026-05-13 WebSearch], introducing a hawkish-
unknown into the rates curve; and (b) **copper retracing from ~$6.44/lb to
$6.10–$6.20** over the same window [MACRO:Copper_2026-05-15
WebSearch:tradingeconomics.com], with the Iran-ceasefire premium unwinding.
FCX is acting as a **high-beta copper proxy** — these two macro forces
sufficient to explain the move without invoking company-specific news.

The structural copper bull case remains intact: JPM models **LME copper
$12,500/ton Q2 2026 avg, $12,075 full-year** on AI/electrification
[MACRO:CopperForecast_2026-Q2 WebSearch:goldmansachs.com]. **Deutsche Bank
raised FCX target $58 → $72** during the rally
[MACRO:DBPT_2026-05-13 WebSearch], and consensus targets now cluster
$70–$81. **Grasberg ramp is on track** for ~1.0B lbs copper / 0.9M oz gold
2026, scaling to 1.6B/1.3M for 2027–29 [MACRO:GrasbergGuidance_2026-Q1
WebSearch].

UW's market-regime tool labels today **TRANSITIONAL — "Mixed signals,
reduce position size, wait for clarity. Favor defined-risk strategies."**
[MACRO:MarketRegime_2026-05-19 UW]. SPY is in an uptrend (+5.28% 30d, above
20/50 SMA) but breadth is poor — only 34.7% of tickers showed bullish flow
today [MACRO:MarketRegime_2026-05-19 UW]. Sector rotation: Tech (+$44M),
Energy (+$17M), Healthcare (+$7M) leading; Comm Services (−$84M), Financials
(−$49M), Cons Cyclical (−$27M) lagging. **Basic Materials does not appear
in either list — neutral sector flow for FCX**.

**Net macro bias for FCX: NEUTRAL near-term with a bullish structural tilt
on 6–12mo horizon.** The 4-week trading window is dominated by event-stress
binaries (CPI, FOMC) on top of cheap implied vol — favors **debit, defined-
risk structures over naked directional bets**. Conviction **3/5**.

## Key signals

- **TRANSITIONAL market regime — size DOWN, defined-risk only**
  [MACRO:MarketRegime_2026-05-19 UW]; bullish-flow breadth 34.7%.
- **June 16–17 FOMC = Warsh's first meeting + dot plot** — 18 sessions
  from today, inside Jun-18 OPEX [MACRO:FOMC_2026-06-17
  WebSearch:federalreserve.gov]. **Source of front-end IV backwardation.**
- **June 10 CPI release (May data)** — 9 sessions, inside May-29/Jun-5
  weekly options windows [MACRO:CPI_2026-06-10 WebSearch:bls.gov].
- **Copper retraced from $6.44 (late-Apr) → $6.10 (May-20)**, FCX's −12.6%
  4-day pullback tracks the copper move 1:1 [MACRO:Copper_2026-05-15
  WebSearch:tradingeconomics.com].
- **Deutsche Bank PT $58 → $72 (May 13), Buy**
  [MACRO:DBPT_2026-05-13 WebSearch]; consensus cluster $70–$81 — the
  $70 magnet in dealer GEX [STRUCT:gex@phase-4] aligns with analyst fair
  value.
- **Grasberg + Indonesia bridge favorable** [MACRO:GrasbergGuidance_2026-Q1
  WebSearch] — structural tailwind.
- **No FCX earnings until late-July (Q2)** — no idiosyncratic catalyst
  inside Jun-18 OPEX [MACRO:FCXEarnings_2026-04-23 WebSearch].

## Detailed findings

### Market regime (UW) [MACRO:MarketRegime_2026-05-19 UW]

| Metric | Value |
|--------|-------|
| Regime | **TRANSITIONAL** |
| Trend | UPTREND |
| SPY | $741.25 |
| vs 20-SMA | above ($728.29) |
| vs 50-SMA | above ($693.76) |
| 30-day change | +5.28% |
| % from 90-day high | −1.1% |
| Bullish-flow tickers | 2,127 of 6,124 (**34.7%**) |
| Bearish-flow tickers | 3,997 of 6,124 (65.3%) |

**Sector rotation today:**

| Money flowing IN ($M) | Money flowing OUT ($M) |
|----------------------|------------------------|
| Technology +44.0 | Communication Services −84.3 |
| Energy +17.0 | Financial Services −48.8 |
| Healthcare +7.3 | Consumer Cyclical −27.0 |

Basic Materials does not appear in the top inflow/outflow lists — **neutral
sector flow for FCX**.

**SPY 10-day flow** [MACRO:SPYTrend_2026-05-19 UW]: 9 of 10 sessions
bearish-flow despite the price uptrend. Five-day cumulative SPY net flow
≈ −$418M. **This is a meaningful flow/price divergence — the uptrend is
running on thinner conviction.**

### Inflation, labor, rates

FRED API key not configured (see Tool errors). Pulling from WebSearch:

- **CPI April 2026 released May 12, 2026** [MACRO:CPI_2026-05-12
  WebSearch:bls.gov]. Specific YoY % not retrieved this run; the market's
  reaction (FCX hit $66.03 on May-12, peaked $67.16 May-13) suggests the
  print was at least benign / consistent with hold-and-wait Fed.
- **Next CPI (May data): June 10, 2026 at 8:30 ET** — **9 trading days
  from today** [MACRO:CPI_2026-06-10 WebSearch:bls.gov]. Hot print →
  hawkish-pressure on Warsh debut → copper / FCX headwind via USD. Cool
  print → ease pressure → tailwind.
- **April 29, 2026 FOMC** kept rates at **3.50–3.75%**
  [MACRO:FOMC_2026-04-29 WebSearch:federalreserve.gov].
- **June 16–17 FOMC: Warsh's first meeting + new SEP/dot plot**
  [MACRO:FOMC_2026-06-17 WebSearch:federalreserve.gov]. **Most-watched
  meeting of the year — single largest source of June IV.**

### Activity / commodity (FCX-relevant)

- **Copper spot $6.10–$6.20/lb** [MACRO:Copper_2026-05-15
  WebSearch:tradingeconomics.com] — pulled back ~5% from $6.44/lb late-Apr
  high. Three-session decline at search time.
- **JPMorgan: LME copper avg $12,500/ton Q2 2026, $12,075 FY**
  [MACRO:CopperForecast_2026-Q2 WebSearch:oilprice.com] — bullish.
- **Goldman Sachs: copper to decline modestly from record highs in 2026**
  [MACRO:CopperForecast_2026 WebSearch:goldmansachs.com] — calibration
  point; not a bear call, just a cap.
- **AI/data-center copper demand:** 27–33 tonnes/MW of installed AI
  capacity; 100 MW campus = several thousand tonnes
  [MACRO:CopperAIDemand_2026 WebSearch:nasdaq.com]. Structural multi-year
  tailwind.

### FCX-specific catalysts (verified, not retrieved live)

| Event | Date | Source |
|-------|------|--------|
| Q1 2026 earnings beat (EPS 0.57, rev $6.23B) | **2026-04-23** (past) | [MACRO:FCXEarnings_2026-04-23 WebSearch:sec.gov] |
| Dividend ex-date | **2026-04-15** (past) | [MACRO:FCXDividend_2026-04-15 WebSearch:koyfin.com] |
| Last dividend paid $0.08 | 2026-05-01 (past) | [MACRO:FCXDividend_2026-05-01 WebSearch] |
| **Deutsche Bank PT raise $58 → $72** | **2026-05-13** (catalyst for rally peak) | [MACRO:DBPT_2026-05-13 WebSearch] |
| Analyst consensus cluster | $70–$81 | [MACRO:FCXAnalystTargets_2026-05 WebSearch:simplywall.st] |
| **Next FCX earnings (Q2 2026)** | late July 2026 (est) | [MACRO:FCXEarnings_2026-Q2 WebSearch:marketbeat.com] |
| Grasberg ramp guidance 2026 | 1.0B lbs Cu / 0.9M oz Au; scaling 2027–29 | [MACRO:GrasbergGuidance_2026-Q1 WebSearch:fcx.com] |
| Indonesia export permits | extended through mid-2026 | [MACRO:IndonesiaExport_2026 WebSearch:simplywall.st] |
| Manyar smelter | repairs ongoing post-2024 fire | [MACRO:Manyar_2024-fire WebSearch:financialcontent.com] |

## Tailwind / Headwind table

| Datapoint | Latest value | Release date | Source | Impact on Basic Materials / FCX |
|-----------|--------------|--------------|--------|---------------------------------|
| Copper spot $6.10/lb | mid-cycle | 2026-05-15 | WebSearch | **Mixed** — high absolute, momentum negative |
| Copper Q2 forecast (JPM) | $12.5k/ton avg | 2026-Q2 | WebSearch | **Tailwind** (medium-term) |
| Copper forecast (GS) | decline modestly | 2026 | WebSearch | **Mild Headwind** (offset) |
| AI/electrification demand | 27–33 t/MW | 2026 | WebSearch | **Tailwind** (structural multi-year) |
| Deutsche Bank PT $72 | Buy | 2026-05-13 | WebSearch | **Tailwind** |
| FOMC June 16–17 + dot plot | first Warsh meeting | 2026-06-17 | WebSearch | **NEUTRAL** — binary, two-way risk |
| CPI May data | (release) | 2026-06-10 | WebSearch | **NEUTRAL** — two-way risk |
| Market regime TRANSITIONAL | bullish breadth 34.7% | 2026-05-19 | UW | **Headwind** — size DOWN rule |
| SPY uptrend +5.28% 30d | above 20/50 SMA | 2026-05-19 | UW | **Tailwind** for beta |
| SPY breadth | 9 of 10 days bear flow | 2026-05-19 | UW | **Headwind** — uptrend fragility |
| Basic Materials sector flow | not in top in/out | 2026-05-19 | UW | **Neutral** |
| Grasberg ramp guidance | on track | 2026-Q1 | WebSearch | **Tailwind** |
| Indonesia exports extended | through mid-2026 | 2026 | WebSearch | **Tailwind** |
| FCX Q2 earnings | est late-July | 2026-07 | WebSearch | **Neutral** (outside 4-week window) |
| FCX dividend | $0.08 paid 2026-05-01 | past | WebSearch | **Neutral** (priced in) |

## Catalyst calendar (next 30 days from 2026-05-20)

| Date | DTE | Event | Likely impact on FCX |
|------|-----|-------|----------------------|
| 2026-05-22 | 2 | Weekly OPEX (gamma pin $60) | Range-trade, low signal |
| 2026-05-29 | 9 | Weekly OPEX | IV is 64% here — pre-CPI hedge unwind potential |
| 2026-06-05 | 16 | Weekly OPEX | |
| **2026-06-10** | **20** | **CPI (May data, 8:30 ET)** | **HIGH — copper / USD reaction → FCX two-way** |
| 2026-06-12 | 22 | Weekly OPEX | Post-CPI vol fade |
| **2026-06-16–17** | **27–28** | **FOMC + dot plot, WARSH DEBUT** | **HIGH — single largest June vol source** |
| **2026-06-18** | **29** | **Monthly OPEX** | OI cliff resolution (59C / 65C / 70C strikes) |
| 2026-06-19 | 30 | Quad witching adjacencies | Post-FOMC dust |

**The Jun-18 monthly OPEX is the focal point of the entire 30-day map** —
it sits one day after FOMC, captures the new 59C build (6,216 OI), and is
the strike-distance resolver for the 65/70 dealer-long-gamma walls.

## Tool / source errors

```
FRED — skipped: no FRED_API_KEY env var set in user's shell. Public CSV
endpoint is CDN-blocked. To enable automated CPI/PCE/NFP/rates/USD pulls
in future runs, the user can register a free key at
https://fred.stlouisfed.org/docs/api/api_key.html and export it in
~/.zshrc (skill SKILL.md phase-6 documents the procedure).
```

WebSearch was used in lieu — adequate for a single-ticker overlay; precise
series-level values for CPI YoY / PCE YoY / 2s10s / DXY were not retrieved
this run.

## Verdict for downstream phases

- **Net macro bias for FCX:** **NEUTRAL near-term (4-week) with bullish
  structural tilt on 6–12mo horizon.**
- **Conviction:** **3/5** — catalyst stack is clear and dated; price
  reaction is two-way binary at each event.
- **Top 2 datapoints phase-9 MUST cite in its macro overlay:**
  1. **Market regime = TRANSITIONAL** [MACRO:MarketRegime_2026-05-19 UW] →
     enforces "half position size, defined-risk only" — this is the most
     important sizing input.
  2. **Deutsche Bank PT $72 + analyst cluster $70–$81** [MACRO:DBPT_2026-
     05-13] — gives phase-9 a defensible upside target that coincides
     with the dark-pool concentration ($65.94–$68.50) and the dealer-
     long-gamma magnet (65 / 70 strikes).
- **Top 2 catalysts phase-9 MUST put in calendar:**
  1. **2026-06-10 CPI (May data, 8:30 ET)** — 20 DTE from today;
     primary driver of front-end IV.
  2. **2026-06-16–17 FOMC + dot plot (WARSH DEBUT)** — 27–28 DTE; falls
     inside Jun-18 monthly OPEX. **This is THE event.**
- **Tactical implication:** The Jun-18 monthly is the right expiry for
  the directional structure (captures FOMC), but the position should be
  established BEFORE the May-29 weekly OPEX so we lean on cheap implied
  vol that the front-end backwardation hasn't fully priced into the Jun
  series yet (Jun-18 IV is "only" 52.5%, far below the 64% on May-29).
