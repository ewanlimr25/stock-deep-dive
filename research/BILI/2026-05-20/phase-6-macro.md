# Phase 6 — Macro Overlay

**Ticker:** BILI
**As-of date:** 2026-05-20 (data date 2026-05-19)
**Generated:** 2026-05-20T10:20:00-04:00
**Upstream phases cited:** phase-1-flow.md, phase-3-positioning.md, phase-5-historical.md

## Summary

**The single most important macro fact discovered in this phase is that BILI
reported Q1 2026 earnings on 2026-05-19 (the same day as our data snapshot)
— and the print was a beat:** revenue +7% YoY to RMB 7.47B, adjusted net
profit +62% YoY, advertising +30% YoY, DAUs +8% to 115.2M. **This reframes
everything we've seen in phases 1–5: the 5/13–5/15 sell-off was pre-print
de-risking, the IV crush from rank 89→34 is post-earnings vol collapse, and
the Jan-2027 $25 call sweep + DP block buying are textbook post-print
institutional accumulation.**

The broader macro layer is **mixed-with-headwinds**: market regime UW-tagged
**TRANSITIONAL** (uptrend SPY +5.16% 30d, but breadth weak at 34.7% bullish
pct), **Communication Services is the largest outflow sector today at
-$84.3M** (direct headwind for BILI's sector), April CPI YoY printed at
**3.8% — sticky inflation aggravated by an Iran-war oil spike**, China ADR
sentiment remains weak (KWEB -16% YTD), and the **June 16-17 FOMC carries
extra event risk** because it is the **first meeting under a new Fed chair**
(Powell's term ended 2026-05-15). Net macro tilt: **single-name tailwind
into a sector + geopolitical headwind**.

## Key signals

- **BILI Q1 2026 EARNINGS BEAT (2026-05-19)** — first meaningfully profitable
  quarter; revenue +7% YoY, adj profit +62% YoY, advertising +30%
  [MACRO:BILI_Q1_2026_2026-05-19 WebSearch:sec.gov].
- **Market regime: TRANSITIONAL** — SPY $740.39 (uptrend), but breadth weak
  (34.7% bullish pct). Guidance: half position size, defined-risk
  [MACRO:MarketRegime_2026-05-19 UW].
- **Sector rotation headwind: Communication Services -$84.3M** (largest
  sector outflow today) [MACRO:SectorRotation_2026-05-19 UW].
- **April 2026 CPI +3.8% YoY / +0.6% MoM** — sticky, Iran-war oil spike
  pushing energy +3.8% MoM [MACRO:CPIAUCSL_2026-04 WebSearch:bls.gov].
- **June 16-17 FOMC under NEW Fed chair** — first dot plot under new
  leadership = elevated rate uncertainty
  [MACRO:FOMC_2026-06-17 WebSearch:federalreserve.gov].
- **China ADR sentiment weak — KWEB -16% YTD**, ongoing US-China tariff
  escalation [MACRO:KWEB_YTD_2026 WebSearch:aol.com].

## Detailed findings

### Market regime [MACRO:MarketRegime_2026-05-19 UW]

```
Trend                 : UPTREND
Regime label          : TRANSITIONAL ("Mixed signals, reduce size, defined risk")
SPY                   : $740.39
SPY 20-SMA            : $728.24  → above
SPY 50-SMA            : $693.74  → above
SPY 30d change        : +5.16%
SPY pct from 90d high : -1.22%
Breadth (bullish pct) : 34.7%   ⚠ (weak)
Bullish-flow tickers  : 2,127
Bearish-flow tickers  : 3,997
```

Surface index strong (SPY in uptrend, close to high) but underlying breadth
**concerning** — only 34.7% of tickers showing bullish flow. UW guidance for
TRANSITIONAL = **half-size, defined-risk** — directly applies to the BILI
sizing decision in phase-9.

### Sector rotation [MACRO:SectorRotation_2026-05-19 UW]

| Sector | Today's net options flow |
|---|---|
| Technology | **+$43.98M** (largest inflow) |
| Energy | +$16.95M |
| Healthcare | +$7.25M |
| Financial Services | -$48.79M |
| Consumer Cyclical | -$26.99M |
| **Communication Services** | **-$84.33M** (largest outflow) |

**BILI is in Communication Services — the sector with the worst flow today.**
This is a direct macro headwind. The flow tape suggests China ADRs and other
Comm-Services names are being net-sold while Technology and Energy receive
flows.

### Inflation [MACRO:CPIAUCSL_2026-04 WebSearch:bls.gov]

| Metric | Value | MoM | YoY |
|---|---|---|---|
| Headline CPI (April 2026) | — | **+0.6%** SA | **+3.8%** NSA |
| Core CPI ex food & energy | — | +0.4% SA | **+2.8%** NSA |
| Energy index | — | +3.8% MoM | (40%+ of all-items rise) |
| Shelter index | — | +0.6% MoM | — |

**Sticky inflation with energy-driven re-acceleration.** The article notes
the **Iran war caused oil prices to spike**, pushing gasoline, airfare, and
food prices up. This is a **risk-off macro backdrop**: higher inflation
prints make rate cuts less likely, geopolitics adds tail risk.

### Rates & Fed [MACRO:FOMC_2026-06-17 WebSearch:federalreserve.gov]

- **No FOMC meeting in May 2026.** Last decision: 2026-04-29 (not pulled in
  this run; user can WebFetch the statement if needed).
- **Next FOMC: 2026-06-16/17** — first meeting under **new Fed chair**
  (Powell's term ended 2026-05-15). Dot plot release scheduled.
- **2026 median dot (December 2025 SEP):** ~3.4% terminal — implies ~1 cut.
  Range from 2.25% (most dovish) to 3.75% (most hawkish).
- FRED series not pulled (no `FRED_API_KEY` env var — see tool errors).

**Implication:** the June 17 FOMC is a **risk event** for risk assets generally
and high-beta names like BILI specifically. Any direction-of-policy surprise
under new leadership amplifies vol. **Position into / out of June 18 OPEX
needs to budget for FOMC overhang.**

### China-specific overlay [MACRO:KWEB_YTD_2026 WebSearch:aol.com]

- **KWEB -16% YTD** — China internet/platform sector beaten down.
- ADR structural risks persist: variable-interest-entity (VIE) structure,
  potential delisting overhang, regulatory mood from CSRC.
- US Section-301 tariff escalation has hammered Chinese equities broadly
  in 2026.
- Some analyst constructive case: "platform economy is the part of China
  most mispriced after the regulatory reset" — supports BILI's bull thesis
  IF China policy normalizes.
- CSRC tightening on speculative leverage may compress China-A volatility
  but indirectly support more orderly capital flow.

### Consumer / activity

Not pulled in this run (would require WebSearch for ISM PMI + U-Mich) —
**limitation noted**. Given the TRANSITIONAL market regime and 3.8% CPI
print, the consumer is presumed neutral-to-soft.

### Tailwind / Headwind table

| Datapoint | Latest value | Release date | Source | Impact on BILI (Comm Services / China ADR) |
|---|---|---|---|---|
| **BILI Q1 2026 EPS** | RMB 202M profit (vs RMB -10.7M LY) | 2026-05-19 | SEC 6-K | **TAILWIND (strong)** |
| BILI Q1 2026 revenue YoY | +7% (RMB 7.47B) | 2026-05-19 | SEC 6-K | TAILWIND |
| BILI Q1 2026 advertising YoY | +30% | 2026-05-19 | SEC 6-K | TAILWIND |
| Comm Services net flow today | -$84.33M | 2026-05-19 | UW | **HEADWIND** |
| Market regime label | TRANSITIONAL | 2026-05-19 | UW | HEADWIND (size constraint) |
| SPY 30d change | +5.16% | 2026-05-19 | UW | mild tailwind (beta) |
| Market breadth (bullish pct) | 34.7% | 2026-05-19 | UW | HEADWIND |
| April CPI YoY | +3.8% | 2026-05-12 | BLS | HEADWIND (sticky inflation) |
| Iran-war oil spike | (oil up driving CPI) | ongoing 2026-05 | BLS/news | HEADWIND (risk-off) |
| KWEB YTD performance | -16% | 2026 YTD | sector ETF | HEADWIND (sector) |
| US-China tariffs (Section 301) | escalating | ongoing 2026 | china-briefing.com | HEADWIND |
| New Fed chair June FOMC | unknown chair, June 16-17 | upcoming | federalreserve.gov | HEADWIND (event risk) |

### Catalyst calendar (next 30 days)

| Date | Event | Likely impact on BILI |
|---|---|---|
| 2026-05-22 (Fri, 2d) | Weekly OPEX | Pin to $20 magnet expected (phase-4); low-impact |
| 2026-05-25 (Mon) | US Memorial Day holiday | Volume light; spread risk |
| ~2026-05-29 (Fri) | Weekly OPEX | Less concentration than 5/22 |
| ~2026-06-04 (Wed) | Likely ISM Services PMI release | Macro risk |
| ~2026-06-06 (Fri) | Likely NFP release | Macro risk |
| ~2026-06-10 (Wed) | Likely May CPI release | Macro risk |
| **2026-06-16/17 (Tue-Wed)** | **FOMC + new chair's first dot plot** | **HIGH event risk** |
| 2026-06-18 (Thu) | Monthly OPEX | Phase-4 GEX shows $20 dominant strike |
| Late-Aug 2026 (target) | BILI Q2 2026 earnings | Major single-name catalyst; matches 8/21 put OI build [OI:biggest_increases] |

## Tool / source errors

- `FRED_API_KEY` not set in the shell environment, so we did **not** pull
  the 12 FRED series listed in the phase-6 prompt (CPIAUCSL, PCEPI,
  PAYEMS, UNRATE, DFF, DGS10, DGS2, T10Y2Y, DTWEXBGS, SOFR). For automated
  production-grade macro pulls, the user can register a free FRED key at
  https://fred.stlouisfed.org/docs/api/api_key.html and `export
  FRED_API_KEY=…` in `~/.zshrc`.
- ISM PMI and U-Mich Consumer Sentiment **not pulled** in this run
  (limitation noted — would require additional WebSearch).
- April-2026 FOMC statement (2026-04-29) **not fetched verbatim** —
  WebSearch returned the URL only.

## Verdict for downstream phases

- **Net macro bias for BILI:** **MIXED — single-name tailwind, sector +
  geopolitical headwind.** The earnings beat is the dominant positive
  catalyst and explains the post-print flow we analyzed in phases 1-3.
  But sector flow is the worst in the market today, geopolitics (Iran war
  + tariff escalation) keep risk-off bias, and the new-chair June FOMC is
  a hard event-overhang.
- **Conviction:** **3 / 5** — the BILI-specific tailwind is strong and
  fresh, but the macro overlay forces phase-9 to apply **TRANSITIONAL-regime
  sizing rules (half-size, defined-risk)** and **fully encapsulates the
  6/17 FOMC** in any structure that crosses that date.
- **Top 2 datapoints phase-9 MUST cite:**
  1. **BILI Q1 2026 earnings beat (2026-05-19)** — primary
     fundamental driver.
  2. **Sector rotation: Comm Services -$84.3M** — confirms
     phase-9 should NOT size for outright long-stock thesis; defined-risk
     options structures are mandated by both regime and sector.
- **Top 2 catalysts phase-9 MUST put in the calendar:**
  1. **2026-06-16/17 FOMC** (first under new chair) — manage exposure
     across this date.
  2. **Late-August 2026 BILI Q2 earnings** — the institutional 8/21 $18
     put-buy + Jan-27 call spread is sized for **this catalyst**, not just
     Q1. Anyone holding past 6/18 OPEX is implicitly long-vol into Q2.

## Sources

- [Bilibili Q1 2026 6-K filing](https://www.sec.gov/Archives/edgar/data/0001723690/000119312526229680/d157629dex991.htm)
- [CNBC: CPI inflation April 2026](https://www.cnbc.com/2026/05/12/cpi-inflation-april-2026-.html)
- [BLS: CPI April 2026 release](https://www.bls.gov/news.release/cpi.nr0.htm)
- [Fed: FOMC calendar](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm)
- [Fed: March 2026 SEP / dot plot](https://www.federalreserve.gov/monetarypolicy/files/fomcprojtabl20260318.pdf)
- [Why MCHI, KWEB, FXI for China recovery](https://www.aol.com/finance/why-mchi-kweb-fxi-could-192029996.html)
- [China 2026 tariff schedule](https://www.china-briefing.com/news/chinas-2026-tariff-schedule/)
