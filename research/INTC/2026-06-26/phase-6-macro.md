# Phase 6 — Macro Overlay

**Ticker:** INTC
**As-of date:** 2026-06-26
**Generated:** 2026-06-27T10:13:43-0400
**Upstream phases cited:** phase-0.5-context.md, phase-1-flow.md, phase-5-historical.md

## Summary

The macro backdrop is a **clear, multi-source HEADWIND for INTC and aligns with the
bearish single-name thesis.** The Fed just delivered a **hawkish pivot** (Jun-16/17 FOMC,
new Chair Warsh: rates held 3.5–3.75%, easing bias removed, 2026 median dot raised to
3.8% — signaling a *hike* possibly by October) into **sticky 4%+ inflation** (headline
CPI +4.27% YoY, core PCE +3.41%) and a **4.40% 10-year** — a textbook valuation headwind
for high-multiple tech. The UW regime is **TRANSITIONAL / CHOPPY** ("half position sizes,
favor defined-risk, iron condors"), SPY is below its 20- and 50-day SMAs (−2.86% 30d), and
broad flow is bearish (38.2% bullish). **Technology is the #1 sector with money flowing
OUT (−$637.8M directional)** even though raw call-premium looks positive (the same
financing-inflation artifact seen in INTC itself). The web confirms a **structural semis
stress** — a $1.3T June-2026 chip selloff (Broadcom guide miss), a memory-chip crisis, and
an IDC smartphone forecast of −13% (worst on record); **INTC crashed to $99 on Jun-5 and
V-bounced to ~$128**, now trading **29–33% ABOVE the average analyst target ($102.70)**.
The only genuine offsets are the intact **AI secular boom** (Deloitte +26%/$975B 2026) and
INTC's own Q1 recovery + a Q2 guide that beat lowered expectations — both of which feed the
**squeeze/binary risk** into **Jul-23 earnings**. Net: macro is a headwind; the fade is
macro-supported but the AI narrative is the live bull tail.

## Key signals

- **Hawkish Fed pivot**: FOMC Jun-17 held 3.5–3.75%, dropped cut bias, dots → 3.8%, hike
  bias [MACRO:FOMC_2026-06-17 WebSearch:cnbc.com][MACRO:DFF_2026-06-25 FRED].
- **Sticky inflation**: CPI +4.27% YoY, core CPI +2.96%, core PCE +3.41% (May 2026)
  [MACRO:CPIAUCSL_2026-05 FRED][MACRO:PCEPILFE_2026-05 FRED].
- **Regime TRANSITIONAL/CHOPPY** — half size, defined-risk; SPY <20/50 SMA, breadth 38.2%
  bullish [MACRO:MarketRegime_2026-06-26 UW].
- **Tech = #1 directional outflow sector (−$637.8M)** despite +$3.2B raw premium (financing
  artifact) [MACRO:sector_rotation UW].
- **INTC 29–33% above analyst targets** ($102.70 avg / $100 median vs ~$128 spot); semis
  in a $1.3T June selloff [MACRO:INTC_targets WebSearch:cnn.com][MACRO:semis_selloff WebSearch:cnbc.com].

## Detailed findings

### Market regime (UW: SPY + breadth + rotation)

`regime = "TRANSITIONAL — Mixed signals, reduce position size, wait for clarity"`,
`trend = CHOPPY`, `trading_guidance = "Half position sizes. Favor defined-risk strategies.
Iron condors in range."` SPY $728.99: `above_20sma false`, `above_50sma false`,
`change_30d −2.86%`, `pct_from_90d_high −4.13%`. Breadth: 3,854 bearish-flow vs 2,385
bullish-flow tickers (**38.2% bullish**). SPY 10d: $741.75 → $728.99, **7 bearish / 3
bullish days**, latest bearish. **Mild broad risk-off.**

### Inflation (FRED, May 2026 prints)

| Series | Latest | YoY | Read |
|---|---|---|---|
| CPIAUCSL (headline CPI) | 333.979 (May) | **+4.27%** | Elevated/re-accelerating — headwind |
| CPILFESL (core CPI) | 336.121 | +2.96% | Above target |
| PCEPILFE (core PCE) | 130.082 | +3.41% | Above Fed 2% target |

### Labor (FRED)

NFP `PAYEMS` 159,001k (May), MoM **+172k** (prior +179k) — solid. `UNRATE` **4.3%** (flat
Mar/Apr/May). Labor gives the Fed room to stay hawkish; no recession signal.

### Rates (FRED + FOMC)

`DFF` **3.63%** (06-25); `DGS10` **4.40%**, `DGS2` **4.09%**, `T10Y2Y` **+0.31** (curve
normalized/dis-inverted, no inversion-recession flag); `DTWEXBGS` 120.40. **FOMC Jun-16/17
(Chair Warsh, unanimous 12-0):** held 3.5–3.75%, removed easing-bias language, 2026 median
dot **3.4% → 3.8%** ("at least one hike"), "the recent past need not be prologue." Traders
price a possible **October hike**. A 4.40% 10y + hawkish Fed + 4%+ CPI = **pressure on
long-duration / high-P/E tech**.

### Sector overlay (semiconductors — WebSearch)

- **$1.3T June-2026 semis/AI selloff** (Jun-4/5): Broadcom Q3 AI guide $16B vs $17.2B est,
  no FY raise → "sell-the-news"; **Intel hit hardest, −11.28% to $99.17 on Jun-5**; AMD
  −10.86%, AVGO −14%, MU ~−7% [MACRO:semis_selloff WebSearch:cnbc.com].
- **Structural stress**: memory-chip crisis + IDC global smartphone −13% in 2026 (worst on
  record). Jun-23: "tech rout intensifies" (Mag7/Samsung/SK Hynix) [MACRO:tech_rout_2026-06-23 WebSearch:cnbc.com].
- **Offset (bull tail)**: AI boom intact — Deloitte 2026 outlook $975B sales, +26% growth.
- **INTC-specific**: Q1-2026 recovery (Data Center/AI), Q2 guide ($13.8–14.8B rev, $0.20
  EPS) beat lowered expectations → fueled the rally; now **29–33% above analyst targets**
  (avg $102.70 / median $100). Earnings **Jul-23** confirmed (matches UW; resolves the
  memory note's stale-date risk).

### Sector rotation (UW flow)

`sector-flow` raw net (premium): Technology **+$3,210.4M** (largest) — but this is
call_premium $8,434M − put_premium $5,223M, **inflated by deep-ITM financing** (same
artifact as INTC). The regime's **directional** `sector_rotation` is the truer read:
**Technology −$637.8M (money flowing OUT, the largest outflow)**, vs inflows to Consumer
Cyclical (+$114.2M), Healthcare (+$34.1M), Comm Services (+$27.0M). **`sector-flow-
persistence` returned uniform placeholder values** (every sector net_flow $0M /
persistence 1 / INFLOW) → **not usable**; the rotation read rests on the regime
directional field + web sector stress + phase-0.5's semis-distribution leaderboard.
**Verdict: ADVERSE for an INTC long / ALIGNED with the bearish thesis.**

- **`fz` breadth cross-check (advisory, EOD 06-27):** whole-market advancers 324 /
  decliners 178, `pct_green` 64.41%, but **worst mover = ON Semiconductor −23.66%** — a
  semis name leading the downside corroborates sector stress. Tech group `Change −0.96%`,
  `P/E 36.81` / `Fwd P/E 25.68` / `PEG 0.98` — rich-ish multiple
  [MACRO:sector_breadth fz EOD][MACRO:group_valuation fz EOD].

### Cross-name correlation (UW)

Run with INTC,MU,TSM,NVDA,AMD (no concurrent blueprints — INTC is the only as-of-date
research dir, so **no sizing-gate cut applies**). Coefficients (valid; sector field broken
= "Unknown", per known UW behavior):

| Pair | ρ | Flag |
|---|---|---|
| **INTC/MU** | **0.954** | HIGH |
| TSM/NVDA | 0.861 | HIGH |
| TSM/AMD | 0.694 | MODERATE |
| NVDA/AMD | 0.576 | MODERATE |

**INTC ≈ MU at 0.954** — an INTC bearish trade is effectively a **semis-complex / memory
bet**, and MU (the tightest correlate) is the **#2 most net-bearish name in the entire
market today** (phase-0.5: −$408.7M). Context, not a gate, but it means the trade is *not*
idiosyncratic — it rides the memory-crisis tape.

## Tailwind / Headwind table

| Datapoint | Latest value | Release | Source | Impact on Tech/Semis |
|---|---|---|---|---|
| FOMC stance | Held 3.5–3.75%, hike bias, dots→3.8% | 2026-06-17 | WebSearch:cnbc.com | **Headwind (strong)** |
| Headline CPI YoY | +4.27% | 2026-05 | FRED | **Headwind** |
| Core PCE YoY | +3.41% | 2026-05 | FRED | Headwind |
| 10y yield | 4.40% | 2026-06-25 | FRED | Headwind (valuation) |
| Market regime | TRANSITIONAL/CHOPPY | 2026-06-26 | UW | Headwind |
| Tech directional flow | −$637.8M (out) | 2026-06-26 | UW | **Headwind (aligned)** |
| Semis sector | $1.3T June selloff, memory crisis | 2026-06 | WebSearch:cnbc.com | **Headwind (strong)** |
| INTC vs analyst targets | +29–33% above $102.70 | 2026-06 | WebSearch:cnn.com | **Headwind (valuation)** |
| 2s10s spread | +0.31 (normal) | 2026-06-26 | FRED | Neutral |
| Labor (UNRATE/NFP) | 4.3% / +159k | 2026-05 | FRED | Neutral (supports hawkish Fed) |
| AI secular demand | $975B / +26% (Deloitte) | 2026 | WebSearch | **Tailwind (bull tail)** |
| INTC Q2 guide / Q1 recovery | $13.8–14.8B, $0.20 EPS, beat | 2026 | WebSearch | **Tailwind (binary)** |

## Catalyst calendar (next 30d)

**Front-expiry expected (implied) move (IV-derived, NOT the 0DTE residual):** at ATM IV
~94% (phase-4/5), 1σ ≈ **±12% to Jul-02 (6d)** and **±22% to Jul-17 OPEX (21d)**. Phase-9
sizes structures to this priced range.

| Date | Event | Likely impact | vs expected move |
|---|---|---|---|
| ~Jul-14/15 | June CPI release | Hot print → reinforces hawkish Fed, tech headwind | macro, sector-wide |
| **2026-07-17** | **Monthly OPEX** (the OI gravity well; $130 put build) | Pin/de-gamma; bearish put position expires | within ±22% band |
| **2026-07-23** | **INTC Q2 earnings** | **Primary binary** — beat could squeeze; miss/guide-cut confirms fade | high-vol; IV 94% prices a large move |
| ~Jul-28/29 | Next FOMC | Hawkish-hold/hike risk → tech headwind | macro |

Note: the **Jul-17 put build expires BEFORE the Jul-23 earnings** — it is a *near-term
pullback* bet, not an earnings play. The earnings binary sits just outside the dominant
OPEX cliff.

## Tool / source errors

- `sector-flow-persistence` returned uniform placeholder data (all sectors net_flow $0M,
  persistence 1, trend INFLOW) — **not usable**; substituted the regime directional
  `sector_rotation` field + web sector evidence. Not a crash; degraded output surfaced.
- FRED ran via Path A (key present, len 32) — no skip. All 10 series returned valid JSON.
- WebSearch is real-world data and is **consistent with the as-of substrate** (INTC
  52W-range $18.97–$141.45, ~$132.87 recent print, Jul-23 earnings all match UW/fz).

## Verdict for downstream phases

- **Net macro bias for INTC:** **HEADWIND** — hawkish Fed + sticky inflation + 4.4% 10y +
  choppy risk-off tape + tech-sector outflow + structural semis/memory stress + price
  29–33% above analyst targets. The AI boom + Jul-23 earnings are the live bull tails.
- **Conviction:** **4 / 5.**
- **Top 2 datapoints phase-9 must cite:** (1) Tech is the #1 directional outflow sector
  −$637.8M [MACRO:sector_rotation UW]; (2) hawkish FOMC Jun-17 + CPI +4.27% YoY
  [MACRO:FOMC_2026-06-17 WebSearch][MACRO:CPIAUCSL_2026-05 FRED].
- **Top 2 catalysts for phase-9 calendar:** (1) **Jul-23 INTC earnings** (primary binary);
  (2) **Jul-17 monthly OPEX** (OI gravity well, where the $130 put build expires).
- **Sector-rotation verdict:** **ADVERSE (aligned with the bearish thesis)** — tech
  directional outflow −$637.8M; persistence score *unavailable* (placeholder tool output),
  but corroborated by regime + web + phase-0.5 semis leaderboard. Phase-9 sizing: macro
  does NOT cut the bearish thesis (it supports it) but the TRANSITIONAL regime caps gross
  size to "half / defined-risk."
- **Correlation verdict:** **No concurrent positions** (INTC is the only blueprint for
  2026-06-26) → no cluster sizing-cut. Context flag: **INTC/MU ρ=0.954** — the trade is a
  semis-complex/memory bet, not idiosyncratic.
