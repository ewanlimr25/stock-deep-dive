# Phase 9 — Trade Blueprint

**Ticker:** USAR (USA Rare Earth, Inc., NASDAQ:USAR)
**As-of date:** 2026-05-20 (effective UW data date: 2026-05-19)
**PM voice:** desk PM running an institutional book
**Spot reference:** $19.97 close 2026-05-19 [HIST:historical_trend]; intraday range $19.46–$20.78 [DP:dark_pool_largest]
**Upstream phases cited:** phase-1 through phase-8

> *For research and educational use only. Not financial advice. Sizing and structures are illustrative.*

## Thesis (≤3 sentences)

USAR just took a -29% beating off the $28.16 peak [HIST:historical_trend]
into a **dealer book that is structurally pinned to $25** (the chain's
dominant +$383M GEX line, the Zero Gamma Level at $24.98 [STRUCT:gex],
and the $24.18–$25.95 5-day dark-pool supply band [DP:price_levels]),
while the EOD dark-pool tape printed 62.3% buy_ratio with the day's
biggest block ($505,960 at NBBO ask on $19.46 [DP:dark_pool_largest])
and the chain's single biggest dollar LEAP commitment was bullish (2028
$40P sold all-bid, $682k premium [OI:oi_smart_positioning]). With
**Cantor Fitzgerald reiterating Overweight and lifting PT to $35
[MACRO:CantorFitzgerald_PT35]**, VRP at -11.93% (vol cheap vs realized
110% — favor debit) [HIST:vrp], and the contrarian-scanner sub-agent
calling this "fade the panic, not the trend" [AGENT:contrarian-scanner],
the trade is a **defined-risk mean-reversion bounce to $25** with the
$19.46 dark-pool floor as the line in the sand.

## Bias + conviction + horizon

- **Directional bias:** **LONG**
- **Conviction (M-01 bin):** **0.65** (moderate edge — more likely than
  not, with real disconfirming evidence)
- **Time horizon:** **1–4 weeks** (target close BEFORE the 2026-06-17/18
  FOMC + USAR monthly OPEX collision; 6/18 expiry weekly only used for
  structure clarity, exit on or before 6/17)
- **Why this bin** (one sentence citing phase-10 expected confluence):
  Estimated phase-10 confluence ~70 (mid 65–79 band → bin 0.75), but
  deviating DOWN one bin to **0.65** per phase-8 risk-monitor's
  "trade unfit at normal size, 25-33% sleeve only" guidance, phase-7
  conviction_matrix confidence of only 14.1%, and phase-7
  signal_confluence ABSENT in both top-100 bullish AND top-100 bearish
  lists. Deviation reason documented in `## Conviction deviation`.

### Conviction deviation

Phase-9 deviates from confluence-rubric mapping by ONE bin DOWN
(0.75 → 0.65). Justification:

1. **Phase-7 conviction_matrix.confidence = 14.1%** — UW's own composite
   prints "low confidence" on this DIRECTIONAL_LONG call. That floor of
   confidence does not support 0.75 bin discipline.
2. **Phase-8 risk-monitor: "trade UNFIT at normal size; cap at 25-33%
   sleeve, defined-risk only, no naked premium short into negative-
   gamma FOMC-OPEX collision."** A sub-agent that explicitly mandates
   sub-normal sizing is incompatible with a 0.75 conviction bin's
   typical 3-5% allocation envelope.
3. **Phase-7 signal_confluence: USAR absent from top-100 in BOTH
   bullish and bearish directions** with min_score=1. The factor
   profile is genuinely too mixed for a "high conviction" bin label,
   even if the directional inference is reasonable.

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| Primary    | $19.90–$20.10 | Pullback to today's institutional accumulation cluster ($19.99 +$805k DP, $20.07 VWAP) | [DP:dark_pool_largest] + [INSIGHT:institutional_accumulation] |
| Aggressive | $19.46–$19.60 | Tag of the day's heaviest at-ask DP buy print ($505,960 @ $19.46) — accept worse spot for better R/R | [DP:dark_pool_largest] |
| Fade       | $21.05–$21.30 | Rejection at the dark-pool $21.27 near-overhead pivot + 5/22 positive-gamma support flip | [DP:price_levels] + [STRUCT:today_gamma_flip] |

**Avoid entries during 2026-05-21 → 2026-05-22 EOD** — 5/22 IV at 145%
will crush -32 vol points overnight per phase-4 term structure
[STRUCT:iv_term_structure]. Best to enter on 5/26 (Tuesday after
Memorial Day weekend) or after 5/22 close once IV deflates.

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| **Primary support** | **$19.46** | [DP:dark_pool_largest] ($505,960 NBBO-ask print) |
| Secondary support | $19.90–$20.07 (VWAP) | [INSIGHT:institutional_accumulation] |
| **Near-term resistance** | **$21.00–$21.27** | [DP:price_levels] ($21.27 = $1.34M, 8 trades) + [STRUCT:today_gamma_flip] ($21 positive-GEX support flip) |
| **Primary target / Major resistance** | **$24.98 ZGL / $25 GEX magnet / $24.18–$25.95 DP supply** | [STRUCT:gex] (+$383.5M GEX line) + [DP:price_levels] ($10.1M at $25.42) |
| Analyst-PT upside cap | $35 | [MACRO:CantorFitzgerald_PT35] |
| Put-wall floor | $17.50 (chain) / $16 (institutional bull put-write) | [OI:oi_biggest_increases] (5/22 $17.5P +1,300 OI; 6/18 $16P +277 OI bid>ask) |
| Gamma-flip / catastrophe floor | $13.50–$13.65 (today's ATM flip / today's ZGL) | [STRUCT:today_gamma_flip] |

## Invalidation

- **Price-based:** Two daily closes **below $19.46** (the at-ask DP
  print floor from [DP:dark_pool_largest]); OR one intraday print
  below **$18.00** (breach of phase-3 put-wall zone) without immediate
  reclaim within 60 minutes.
- **Signal-based:** [INSIGHT:institutional_accumulation] flips from
  ACCUMULATION to DISTRIBUTION (B/S ratio <1.0) on phase-2 daily
  refresh; OR phase-5 [HIST:historical_cumulative_premium_flow] turns
  net-bearish ≥3 consecutive sessions; OR phase-4 [STRUCT:dex] net
  DEX flips negative (currently +$411.6M — large buffer, would require
  major regime shift).
- **Macro-based:** 2026-06-17/18 FOMC hawkish surprise (≥25bp implied
  hike or ≥3 dots higher than current dot plot)
  [MACRO:FOMC_2026-04-29]; OR sector-specific catalyst — China
  formally REVOKES the critical-minerals export-ban suspension
  (currently runs through 2026-11-27) [MACRO:ChinaCritMin_2025-11-09],
  which would crater USAR's domestic-supply moat thesis.

**Exit on invalidation:** **Hard stop** on debit structures (close
100% of the call debit spread if $19.46 breaks on a close); **roll**
the put credit spread to a wider/lower strike if $17.50 is touched
intraday (defended by short-put wall — restructure rather than
close).

## Sizing (% of risk, NOT dollars)

- **Kelly inputs:**
  - p = **0.65** (conviction bin)
  - Entry (mid of primary zone) = **$20.00**
  - Target = **$25.00** (ZGL / $25 GEX magnet)
  - Stop = **$19.40** (slight buffer below $19.46 DP floor)
  - Move-to-target = $5.00; Move-to-stop = $0.60
  - **b = 5.00 / 0.60 = 8.33** (extreme R/R because stop is tight to
    the institutional floor)
- **Raw Kelly:** `(0.65 × 8.33 − 0.35) / 8.33` = `(5.415 − 0.35) / 8.33`
  = **0.608 = 60.8%**
- **Fractional Kelly (× 0.25):** **15.2%**
- **Cap-applied (cap_pct = 5%):** **5%**
- **Final size:** **1.5% of book risk** (≈ 30% of the 5% cap, matching
  phase-8 risk-monitor's 25-33%-of-normal-sleeve guidance and phase-6
  TRANSITIONAL-regime "half size" rule).
- **Deviation reason:** Downward deviation from suggested 5% does NOT
  require justification per rubric. Notating for the audit trail:
  reduced 70% from cap due to TRANSITIONAL regime
  [MACRO:MarketRegime_2026-05-19] + risk-monitor sleeve cap
  [AGENT:risk-monitor] + UW 14.1% confidence
  [INSIGHT:conviction_matrix].

For the chosen structures below, **1.5% of book risk** translates to:
- Call debit spread: **≤ 1.5% of book** as the spread's max-loss
  (i.e., spread debit × contracts ≤ 1.5% of book).
- Put credit spread: **≤ 1.5% of book** as (width − credit) × contracts.

## Option structures

### Directional (primary)

- **Structure:** **6/18 $20 / $25 call debit spread**
- **Strikes / expiry:** Long 1× USAR **2026-06-18 $20 CALL**; Short
  1× USAR **2026-06-18 $25 CALL**
- **Reference premiums (from chain estimates):**
  - 6/18 $20 C ≈ **$2.60** (interpolated from [OI:oi_biggest_increases]
    showing 4,563 OI at avg_price $2.60)
  - 6/18 $25 C ≈ **$1.30** (interpolated between 6/18 $20C $2.60 and
    6/18 $30C $0.70 [OI:oi_decrease_with_volume])
  - **Estimated net debit: ~$1.30** (verify at the screen — IV-crush
    after 5/22 EOD will bring this down further; ideal entry post-5/22)
- **Breakeven:** $20.00 + $1.30 = **$21.30**
- **Max loss:** debit paid (~$1.30 per spread) = **100% if expires
  ≤ $20**
- **Max gain:** $5.00 − $1.30 = **$3.70 per spread (≈ +285% on debit)
  if pinned at or above $25 at expiry**
- **Why this structure:**
  - VRP -11.93% [HIST:vrp] favors **debit structures** over short
    premium — the call debit spread pays you for being long vol with
    capped downside.
  - The structure pins max gain at $25 — the **exact** confluence of
    [STRUCT:gex] ($25 magnet), [DP:price_levels] ($25.42 cluster), and
    [STRUCT:gex] ZGL ($24.98). You're not paying for any move above
    $25 because the chain says you won't get one quickly.
  - **6/18 expiry chosen to capture the mean-reversion window** but
    **EXIT ON OR BEFORE 6/17** to avoid the FOMC + monthly OPEX
    collision (phase-6 catalyst calendar). Use 6/18 weekly for clean
    Greeks; treat 6/17 close as the operational expiry.
  - 30 DTE at entry matches phase-5 historical IV regime; we are
    BUYING the back-month at 104.5% IV (per [STRUCT:iv_term_structure])
    while the 5/22 IV-spike (145%) crushes on 5/22 close — using a
    post-5/22 entry monetizes that vol-crush.

### Defined-risk alternative

- **Structure:** **6/18 $17 / $14 put credit spread** (short the
  put-wall floor; income while expressing "stays above $16.50")
- **Strikes / expiry:** Short 1× USAR **2026-06-18 $17 PUT**; Long
  1× USAR **2026-06-18 $14 PUT**
- **Reference premiums (chain estimates):**
  - 6/18 $17 P ≈ **$0.68** ([OI:oi_biggest_increases] 3,404 OI at
    avg_price $0.68)
  - 6/18 $14 P ≈ **$0.20** (estimated by interpolation; 6/18 $16P
    avg $0.49 [OI:oi_biggest_increases], $14P further OTM)
  - **Estimated net credit: ~$0.48**
- **Breakeven:** $17.00 − $0.48 = **$16.52**
- **Max loss:** $3.00 width − $0.48 credit = **$2.52 per spread**
- **Max gain:** $0.48 per spread (credit kept) = **+19% on max risk
  if expires above $17 at 6/18**
- **Why this defined-risk alt:**
  - The bull put-write at 6/18 $16P (+277 OI, bid>ask) and the
    massive 6/18 $21P put wall (16,949 OI) [OI:oi_biggest_increases]
    create a **structural floor at $17–$21** which this spread monetizes.
  - For PMs who don't want to pay debit (and accept lower R/R), this
    structure pays you to be right about the floor. Note: this
    **slightly** conflicts with the phase-5 PREMIUM_BUYING rubric
    (which favors debit). Use only as a defined-risk overlay, not as
    the primary expression.
  - Exit / roll: if spot prints $17.50 intraday, roll the short put
    out and down to 7/17 $15 strike rather than close.

## Macro overlay (cite phase-6)

**Tailwinds:**

- **Cantor Fitzgerald Overweight, PT $35** (+72% upside from spot)
  [MACRO:CantorFitzgerald_PT35]
- **Q1 2026 EPS BEAT +42.9%** (released 2026-05-13 after-close, -$0.12
  vs -$0.21e) [MACRO:USAR_Q1_2026]
- **US gov't DPA / DoD critical-minerals priority spending** — USAR a
  named beneficiary; structural moat against China supply
  [MACRO:USAR_Q1_2026]
- **Sector flow today: Energy +$17M, Tech +$44M, Healthcare +$7M IN**
  (commodity-correlation positive) [MACRO:MarketRegime_2026-05-19]
- **CPI hot at 3.8% YoY** (energy +17.9%) — commodity-hedge bid intact
  [MACRO:CPIAUCSL_2026-04]
- **VRP -11.93% / IV percentile 22%** — vol cheap by both measures,
  ideal regime for debit-structure long thesis [HIST:vrp +
  HIST:iv_percentile_zscore]

**Headwinds:**

- **China critical-minerals export-ban suspension through 2026-11-27**
  — returning Chinese supply to global market = direct USAR pricing
  power headwind [MACRO:ChinaCritMin_2025-11-09]
- **Market regime TRANSITIONAL** — "Half position sizes. Favor
  defined-risk strategies." (UW guidance verbatim)
  [MACRO:MarketRegime_2026-05-19]
- **SPY breadth 34.7% bullish** (3,997 tickers bearish-flow vs 2,127
  bullish today) — broad institutional positioning still bearish
  underneath the SPY uptrend [MACRO:MarketRegime_2026-05-19]
- **Insider selling reports** at USAR per 5/15 Benzinga coverage
  [MACRO:USAR_5-18_Drop_2026-05-18]
- **6/17-6/18 FOMC + USAR monthly OPEX collision** — 16,949 OI 6/18
  $21P wall will dominate Greek dynamics that week [OI:oi_biggest_increases]

**Net:** **MIXED-tilted-tail** for USAR specifically; matches phase-6
verdict ("structural tailwinds outweigh the China-supply headwind once
the -29% drawdown is factored in").

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|------|-------|------------------|
| 2026-05-22 (Fri) | Weekly OPEX; concentrated USAR 5/22 OI; IV 145% → ~113% post-event | **+** for next-week entry timing (vol crush opens cheaper debit) |
| ~2026-05-?? | Q2 NFP release (typically first Friday of June; here mid-month if revised schedule) | ? — depends on print |
| ~2026-06-11/13 | May CPI release | + (if soft) / − (if hot) |
| **2026-06-17/18 (T/W)** | **FOMC + SEP/dot plot** | Critical — could spike or crush small-cap multiples |
| **2026-06-18 (Thu)** | **USAR monthly OPEX** (16,949 OI $21P wall) | Critical for pin dynamics — must exit BEFORE this |
| Q3 2026 | **USAR acquisition close** (Cantor-cited driver) | + (bullish trigger if smooth) |
| 2026-08-10 | USAR Q2 earnings | Outside 30-day window — set up phase-9 v2 for that |

## Post-trade monitoring checklist

- [ ] **Daily**: refresh `dark_pool_block_stratified` for USAR; watch
  for buy_ratio drop below 0.55 (signal-based invalidation).
- [ ] **Daily**: refresh `options_structure_dex` and `options_structure_gex`
  for USAR; watch for net DEX flip negative or ZGL drop below $20
  (signal-based invalidation).
- [ ] **Each session-close**: scan `historical_cumulative_premium_flow`
  trend over trailing 3 sessions; ≥3 consecutive bearish-net days =
  signal-based invalidation.
- [ ] **Pre-5/22 close**: confirm IV crush on 5/22→5/29 actually happens
  (expected -32 vol points); if it does NOT, treat as new event premium
  for an unrecognized catalyst → reduce position by 50%.
- [ ] **2026-06-12**: re-pull `risk_market_regime`. If regime flips
  from TRANSITIONAL to RISK-OFF, exit early (do not wait for invalidation
  price level).
- [ ] **2026-06-13** (post-CPI): re-pull `options_structure_iv_term_structure`
  + check 6/17-6/18 FOMC implied move from VIX/SPY. If front-end IV
  ratio spikes above 1.5 again, consider closing into the volatility
  expansion.
- [ ] **News monitoring**: watchlist alerts on USAR + USA Rare Earth +
  China rare earth export + Cantor Fitzgerald rating change.
- [ ] **2026-06-17 EOD**: HARD EXIT regardless of P&L unless thesis
  has accelerated bullish; do not hold through the FOMC + OPEX collision.

## Citations summary

Minimum 3 distinct upstream datapoints from the thesis. The thesis
above cites the following (one from phases 1–4, one from phases 5–7,
one from phases 6/8 — exceeding the minimum):

1. **[DP:dark_pool_largest]** — phase-2 large-tier $505,960 at NBBO
   ask on $19.46 (buy-side print). Resolves at
   `research/USAR/2026-05-20/phase-2-dark-pool.md` §Largest blocks.
2. **[STRUCT:gex]** — phase-4 $25 strike net_gex = +$383,535,631 (the
   chain's dominant gamma node), ZGL $24.98. Resolves at
   `research/USAR/2026-05-20/phase-4-structure.md` §GEX.
3. **[OI:oi_smart_positioning]** — phase-3 USAR 2028-01-21 $40P, +283
   OI all-bid, $682,030 premium (inferred bullish synthetic long
   LEAP). Resolves at `research/USAR/2026-05-20/phase-3-positioning.md`
   §Largest OI increases.
4. **[HIST:vrp]** — phase-5 VRP = -0.1193 / IV30d 98.95% / realised
   110.88% / regime PREMIUM_BUYING. Resolves at
   `research/USAR/2026-05-20/phase-5-historical.md` §VRP.
5. **[HIST:historical_trend]** — phase-5 price trajectory $28.16 peak
   (5/6) to $19.97 close (5/19) = -29.1%. Resolves at
   `research/USAR/2026-05-20/phase-5-historical.md` §Multi-day trend.
6. **[MACRO:CantorFitzgerald_PT35]** — phase-6 Cantor Overweight PT
   $35 raised from $30 (sourced via Benzinga WebSearch 2026-05).
   Resolves at `research/USAR/2026-05-20/phase-6-macro.md`
   §Tailwind/Headwind table.
7. **[AGENT:contrarian-scanner]** — phase-8 verdict LONG conviction 3,
   "fade the panic, not the trend". Resolves at
   `research/USAR/2026-05-20/phase-8-agent-views.md` §contrarian-scanner.
