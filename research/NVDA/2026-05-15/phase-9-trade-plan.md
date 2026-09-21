# Phase 9 — Trade Blueprint

**Ticker:** NVDA
**As-of date:** 2026-05-15
**PM voice:** desk PM running a $5–50M options-overlay book
**Spot reference:** $228.93 (late-day per phase-1 underlying_price);
DP-VWAP $227.84
**Upstream phases cited:** phase-1 through phase-8
**Generated:** 2026-05-17T17:28Z

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

NVDA prints earnings Wed 2026-05-20 AMC with **05-22 IV at 74% vs 30d IV at
52.5% (backwardation 1.41)** `[STRUCT:front_end_iv_ratio]` and **IV30d at
the 100th percentile of the trailing 252-day window**
`[HIST:iv_percentile_zscore]` — the IV-crush carry is the cleanest edge in
the file. The directional signal stack is **mixed-to-bearish**
(`insights_price_vs_flow` flags DIVERGENCE TRUE with price +26.84% / 30d
vs net flow -$42.65M today `[INSIGHT:price_vs_flow]`, 5-of-5 sub-agents
returned NEUTRAL or RANGE `[AGENT:contrarian-scanner]` `[AGENT:earnings-scout]`),
which kills the case for naked directional debit and leaves a **range /
short-vol blueprint** as the highest-edge expression. Macro is mildly
HEADWIND (UW regime TRANSITIONAL, Technology -$151M sector outflow today,
hot CPI 3.8%) `[MACRO:MarketRegime_2026-05-15 UW]` `[MACRO:CPIAUCSL_2026-04 WebSearch:bls.gov]`.

## Bias + conviction + horizon

- **Directional bias:** **RANGE** (with a mild bearish tilt — would prefer
  to pay more credit on the call side than the put side)
- **Conviction (M-01 bin):** **0.55** (slight edge)
- **Time horizon:** **1-5d** (through earnings; structure expires post-event
  on 2026-05-22)
- **Why this bin:** phase-10 confluence is expected to land in the 50–64
  band → bin 0.65 by the rubric. I'm down-binning by one because phase-5's
  `historical_signal_backtest` shows bullish_flow at 20% recent win rate
  AND phase-7's `insights_price_vs_flow` is a true DIVERGENCE flag. When
  both my structural carry edge (IV crush) and my mean-reversion stat
  (bullish-flow under-performance) point the same way but the binary event
  can override everything, I cap conviction at 0.55. Phase-10 should flag
  this deviation if it disagrees.

## Entry zones

| Entry type | Price level | Trigger condition | Source tag |
|------------|-------------|-------------------|------------|
| Primary    | NVDA $227–$230 spot zone | Open the iron condor when spot is within $2 of the $230 gamma wall on a normal-volume session | `[STRUCT:today_gamma_flip]` |
| Aggressive | NVDA $234–$236 | Sell extra call-side credit on a rip into the $235.74 DP cluster (lean the structure short-call-heavy) | `[DP:price_levels]` |
| Fade       | NVDA $219–$220 | Roll up the put credit spread strike on a flush to the DP support shelf (lean structure short-put-heavy) | `[DP:price_levels]` |

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Primary support | **$219.44** | `[DP:price_levels]` ($2.25B 5d cluster) |
| Secondary support | $225.83 | `[DP:price_levels]` |
| Today ZGL (regime flip) | **$218.30** | `[STRUCT:today_gamma_flip]` |
| Primary resistance | **$235.74** | `[DP:price_levels]` ($1.36B 5d) |
| Gamma wall (magnet) | **$230** | `[STRUCT:today_gamma_flip]` ($7.69T GEX) |
| Call-write wall (5/22) | **$237.5 – $240** | `[OI:smart_positioning]` (+51k contracts bid-sold) |
| Upside-buyer target (5/22) | $250 | `[OI:biggest_increases]` (+45,567 OI bullish) |

## Invalidation

- **Price-based:** two consecutive 1H closes BELOW **$218.30** (today ZGL)
  flips dealer regime to short-gamma — close 100% of the put-side credit
  spread immediately; the trade thesis (positive-gamma pin) is broken.
- **Signal-based:** post-event `insights_conviction_matrix` flips to
  DIRECTIONAL_LONG with `insights_institutional_accumulation` to ACCUMULATION
  *and* a daily net flow > +$200M — close the call-side credit spread.
- **Macro-based:** intra-week FOMC speaker hawkish surprise (none scheduled
  through 5/22 but a SOMA speech is possible) or oil/USD spike that takes
  SPY -2%+ on the day — defensive close of full structure.

## Sizing (% of risk, not dollars)

Kelly math (transparent, M-03):
- p = 0.55 (conviction bin)
- Define "win" as the structure expires within both wings (i.e. spot in
  $220–$240 on 05-22 close). Front-end IV implies ±10% move (~$23), so
  the ±$10 strike-distance gives roughly 50–60% breach probability →
  win probability ~45–50% for full max credit but the **expected value
  is positive due to credit > expected loss conditional on breach** when
  IV crushes 74% → 52%.
- b (payoff) for a 5-wide iron condor at typical credit ~$1.50:
  b = credit / (width − credit) = 1.50 / 3.50 = **0.43**
- raw_kelly = (0.55 × 0.43 − 0.45) / 0.43 = **−0.50** → **negative Kelly**
- This is a slight-edge premium-sell where the textbook Kelly fails but
  the structural carry edge (22-pt IV crush) is meaningful. Honest read:
  **the trade DOES NOT pass strict Kelly at p=0.55**. To proceed, either:
  - revise p upward (only justifiable to p≥0.75 if phase-10 confluence
    confirms ≥65/100, OR
  - **size very small** (≤0.5% of book risk; treat as a discretionary
    "earn the carry" position, not a full Kelly bet), OR
  - **skip the trade** and wait for post-earnings clarity.

**Final size:** **0.5% of book risk** (DISCRETIONARY UNDER-SIZED). This is
below the TRANSITIONAL regime ceiling of 2.5% (half of 5%) and reflects
the negative-Kelly + binary-event reality.

**Sizing deviation reason:** none (sizing DOWN from cap is always allowed).

## Option structures

### Defined-risk PRIMARY — 220/215 – 240/245 iron condor on 05-22 chain

- **Structure:** short 5-wide put credit spread + short 5-wide call credit
  spread on the same 2026-05-22 expiry
- **Legs:**
  - SHORT NVDA 220P 2026-05-22, LONG NVDA 215P 2026-05-22
  - SHORT NVDA 240C 2026-05-22, LONG NVDA 245C 2026-05-22
- **Expected credit:** ~$1.50 ($75–$80 per spread mid; refresh at execution)
- **Max loss per condor:** width − credit ≈ $5.00 − $1.50 = **$3.50 / $350**
- **Max profit per condor:** **$1.50 / $150**
- **Breakevens:** $218.50 / $241.50
- **Why this structure:** Strikes are anchored to phase-2's institutional
  S/R ($219.44, $235.74) and phase-3's call-write wall ($237.5–$240)
  `[DP:price_levels]` `[OI:smart_positioning]`. The 220P short sits ABOVE
  the today ZGL ($218.30) so a regime flip provides an early invalidation
  signal. The 240C short rides phase-3's institutional call-write supply,
  giving structural confluence beyond just IV pricing.

### Directional ALTERNATIVE — 235/250 call debit spread on 2026-06-18 chain

For PMs who want a directional bullish bet despite the consensus RANGE
view (e.g., believes Blackwell guide will be a beat). Skips earnings IV
crush by going to June monthly OPEX.

- **Structure:** long call debit spread
- **Legs:**
  - LONG NVDA 235C 2026-06-18
  - SHORT NVDA 250C 2026-06-18
- **Expected debit:** ~$4.50 mid (refresh)
- **Max loss:** **debit $4.50 / $450** per spread
- **Max profit:** width − debit = $15 − $4.50 = **$10.50 / $1,050**
- **Breakeven:** $239.50
- **Why this structure:** 235 long-strike sits AT the phase-2 institutional
  resistance — buying the call gives upside above the level. 250 short-strike
  matches phase-3's `oi_biggest_increases` +45,567 OI BULLISH at 250C 05-22
  `[OI:biggest_increases]` — institutional speculators have already named
  $250 as their target. Selling that strike captures their bid. June expiry
  avoids the IV crush penalty and lets the position breathe through any
  immediate post-print whipsaw.

## Macro overlay (cite phase-6)

**Tailwinds:**
- SPY trend UPTREND, +5.35% 30d, above 20/50 SMA `[MACRO:MarketRegime_2026-05-15 UW]`
- China H200 export approved (Dec 2025, 25% tariff) `[MACRO:ChinaChipExports_2026-05 WebSearch:bis.gov]`

**Headwinds:**
- UW market regime **TRANSITIONAL** — explicit guidance "half size, defined-risk"
  `[MACRO:MarketRegime_2026-05-15 UW]`
- Technology sector flow today **-$151M** (worst sector) `[MACRO:SectorFlow_2026-05-15 UW]`
- CPI April **+3.8% YoY** (highest since May 2023) — tech multiple compression
  pressure `[MACRO:CPIAUCSL_2026-04 WebSearch:bls.gov]`
- China H200 deliveries **ZERO so far** as of mid-May; Beijing blacklisted H20
  `[MACRO:ChinaChipExports_2026-05 WebSearch:scmp.com]`

**Net:** mildly HEADWIND, reinforces the no-naked-direction stance.

## Catalyst calendar (next 30d)

| Date | Event | Likely impact |
|------|-------|---------------|
| **2026-05-20 AMC** | **NVDA Q1 FY2027 earnings + Q2 guide** | **BINARY — primary catalyst** |
| 2026-05-20 AMC | ADI earnings (semis adjacency, same day) | + correlation amplifier |
| 2026-05-21 AMC | TTWO, WDAY, ZM, DE | indirect (software/tech sentiment) |
| 2026-05-30 | PCE April release | + if cool, - if hot |
| 2026-06-05 | NFP May release | indirect (rate path) |
| 2026-06-11 | CPI May release | + if cool, - if hot |
| 2026-06-17/18 | FOMC | dot-plot revision after hot CPI |

## Post-trade monitoring checklist

- [ ] Daily: re-pull `mcp__uw-pp__options_structure_today_gamma_flip` —
      flag if today ZGL crosses $228 (means the gamma wall has migrated).
- [ ] Daily: re-pull `mcp__uw-pp__insights_conviction_matrix` — flag if
      scenario shifts away from MIXED (DIRECTIONAL_LONG → close call
      credit; DIRECTIONAL_SHORT → close put credit).
- [ ] Daily: monitor SPY for risk-on / risk-off regime flip (UW
      `risk_market_regime`) — close full structure if regime flips to
      RISK-OFF.
- [ ] **Wed 5/20 EOD (pre-print):** decide whether to hold full structure
      through the event or take any tier off. If front-end IV has rallied
      further (e.g. ratio >1.5), let it ride — IV crush will be larger.
      If front-end IV has decayed pre-event, consider taking 50% off.
- [ ] **Thu 5/21 09:30 ET:** check post-print spot vs $220 / $240 strikes;
      if both wings intact, hold to expiry; if breached, close immediately
      (do not "hope" for mean reversion on the breached side).
- [ ] Post-event: log realized P&L vs Kelly-expected P&L for calibration.

## Citations summary (M-04: ≥3 distinct upstream datapoints)

1. `[STRUCT:front_end_iv_ratio]` — Front-end IV ratio **1.41**, near-IV
   **74.0%** (05-22) vs far-IV **52.5%** (30d) → phase-4-structure.md §IV
   term structure. Source of the IV-crush thesis.
2. `[INSIGHT:price_vs_flow]` — DIVERGENCE TRUE: price +26.84% / 30d vs net
   flow today -$42.65M → phase-7-insights.md §Price vs flow. Source of the
   no-naked-direction constraint.
3. `[MACRO:MarketRegime_2026-05-15 UW]` — TRANSITIONAL regime with
   explicit "Half position sizes. Favor defined-risk strategies."
   → phase-6-macro.md §Market regime. Source of the half-size constraint.
4. `[DP:price_levels]` — $219.44 ($2.25B 5d) and $235.74 ($1.36B 5d) cluster
   → phase-2-dark-pool.md §Price levels. Source of the iron-condor strike
   choice.
5. `[AGENT:earnings-scout]` — "Sell the earnings vol crush, not direction
   — 240/250 credit spread or 217.5/240 iron condor on 05-22 chain"
   → phase-8-agent-views.md §earnings-scout. Source of the primary
   structure recommendation (modified to 220/215 + 240/245 for tighter risk).
