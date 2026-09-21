# Phase 9 — Trade Blueprint

**Ticker:** BL (BlackLine, Inc.)
**As-of date:** 2026-05-19
**PM voice:** desk PM running a $5–50M options-overlay book
**Spot reference:** $30.03 close ([INSIGHT:insights_deep_dive] / [HIST:historical_trend])
**Upstream phases cited:** phase-1 through phase-8

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

Someone is rebuilding BlackLine's gamma structure in real time, on purpose,
into a known catalyst calendar — and the dealer book is *mechanically forced*
to chase: **+13,016 OI on BL Dec18 2026 $27.5 calls in one day with ask:bid
≈ 4.45×, $11.65M total premium, driving 99.3% of the name's $194,349,985
GEX** [OI:oi_biggest_increases][STRUCT:gex]; **dark pool buy ratio 0.915 with
both anchor blocks paying +$0.07 and +$0.14 above NBBO mid** [DP:largest][DP:block_stratified];
**UW `insights_conviction_matrix` returns DIRECTIONAL_LONG at 87.53%
confidence with ACCUMULATION buy/sell 10.77×** [INSIGHT:conviction_matrix]
[INSIGHT:institutional_accumulation], all on a 26% post-Q1-earnings flush
into the institutional floor at **$24.90–$25.81** [DP:price_levels] off
which spot has bounced 20% in 6 sessions [HIST:historical_trend]. The
operative bet: **buy what they're buying, sized to half-Kelly because the
market-wide bullish_flow backtest just printed 0/7 over 20 days and UW's
regime is TRANSITIONAL** [HIST:historical_signal_backtest][MACRO:MarketRegime_2026-05-19 UW][AGENT:risk-monitor].

## Bias + conviction + horizon

- **Directional bias:** **LONG**
- **Conviction (M-01 bin):** **0.75** (high edge — see deviation note below)
- **Time horizon:** **1-4w** primary; **1-3m** stretch
- **Why this bin (cite phase-10 confluence):** Phase-10's preliminary
  confluence score normalizes to **~84 (band 0.85)**, which would map to
  conviction 0.85 by the rubric. I am **deviating one bin down to 0.75**
  for the reasons below.

## Conviction deviation

Phase-10 score ~84 maps to the 0.85 bin. I'm setting **0.75** because:

1. **Market-wide bullish_flow backtest is 0/7 over 20 days (avg −3.05%)**
   [HIST:historical_signal_backtest]. While not BL-specific, this is the
   most recent regime read on follow-through for bullish-flow setups, and it
   is hostile.
2. **Phase-8 desk split was 2 LONG / 2 NEUTRAL.** Both NEUTRAL agents
   independently invoked the same countervailing evidence (0/7 backtest +
   Apr-17 $42.5C prior failure). They explicitly told the PM to size
   half-Kelly with defined risk [AGENT:risk-monitor][AGENT:contrarian-scanner].
3. **GEX sign-convention conflict** from phase 4 (UW labels "POSITIVE /
   dealers net long" while DEX direction implies dealers net short calls and
   buying the rally) was carried forward but never resolved
   [STRUCT:gex vs STRUCT:dex]. Phase-10 must audit.
4. **The same buyer profile lost in Apr 2026.** The Mar 23-24 build of 2,765
   contracts of Apr17 $42.5 calls expired worthless during the late-April
   drawdown [HIST:historical_oi_trend]. Today's structure resembles that
   playbook; phase-9 cannot assume "different this time" without
   acknowledging the prior cycle loss.

I am not reducing further to 0.65 because phases 1, 2, 3, 7 produced
emphatic, internally-consistent bullish reads, and the institutional
accumulation footprint is *materially* different from a typical retail
bullish-flow signal (DP buy/sell 10.77× plus +$0.07/+$0.14 above-mid blocks).
0.75 splits the difference between "phase-10 score says 0.85" and "phase-8
split says 0.65."

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| **Primary** | **$29.30 – $30.30** | Spot pulls back to or holds the institutional VWAP zone; intraday volume tape stays balanced | [INSIGHT:institutional_accumulation] VWAP $29.30; [DP:largest] today's 16 blocks clustered $28.91-30.31 |
| **Aggressive** | **$25.70 – $26.50** | Re-test of today's zero-gamma flip; defended by intraday buyers | [STRUCT:today_gamma_flip] today_zero_gamma 25.70; [DP:price_levels] $25.80-25.81 institutional cluster $7.7M |
| **Fade** | **$32.50** (only as a hedge, not as a primary entry) | If spot pierces $32.50 on weak volume and immediately rejects (dealer-cover exhaustion) | [STRUCT:today_gamma_flip] $986k support_wall at 32.50 = mechanical magnet; first take-profit, not entry |

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Hard support (lower) | **$24.90 – $25.81** | [DP:price_levels] 5-day institutional cluster $8.72M |
| Soft support (mid) | **$25.70** | [STRUCT:today_gamma_flip] today_zero_gamma; [HIST:historical_trend] May 13 low $24.96 |
| Soft support (upper) | **$28.91 – $29.43** | [DP:largest] today's biggest two block prints |
| VWAP / institution mark | **$29.30** | [INSIGHT:institutional_accumulation] |
| **First target / gamma magnet** | **$32.50** | [STRUCT:today_gamma_flip] $986k support_wall; [OI:oi_biggest_increases] OTM ladder seeded $30/$32.5/$35/$37.5 |
| Second target / implied move | **$33.98** | [INSIGHT:insights_deep_dive] implied_move 13.17% × spot $30.03 |
| Blue-sky / Mar high | **$40.00** | [HIST:historical_trend] 2026-03-23 close $40.02 |
| Largest pin (near OPEX) | **n/a** | [OI:pin_risk] BL absent from top 50 (lead expiry 213 DTE) |
| Gamma flip (today, intraday) | **$27.50 ATM flip / $25.70 ZGL** | [STRUCT:today_gamma_flip] |

## Invalidation

Apply [rubrics/invalidation-rubric.md] — all three categories with concrete,
falsifiable triggers:

- **Price-based:** **Two consecutive daily closes below $24.85.**
  This level (a) sits just below the 5-day institutional cluster
  [$24.90–25.81 DP:price_levels], (b) sits below today's zero-gamma
  [$25.70 STRUCT:today_gamma_flip], and (c) is below the May 13 panic low
  $24.96 [HIST:historical_trend]. Two closes (not intraday spike) prevents
  exiting on a single wash; if it breaks here, the dealer hedging flips
  from "buy the dip" to "sell into weakness" and the GEX structure can
  deflate as fast as it built (phase-5: built from −$1.55M to +$194M in 9
  sessions).
- **Signal-based:** **DEX flips negative on phase-4 daily refresh
  (drops below +$1B), OR `insights_conviction_matrix` flips from
  `DIRECTIONAL_LONG` to `HEDGED_LONG` / `MIXED`, OR cumulative premium flow
  turns net bearish for 3 consecutive sessions.** Today's net_dex
  +$6,337,156,590 [STRUCT:dex] can degrade quickly if the sponsor unwinds
  even half their position; daily monitoring is mandatory.
- **Macro-based:** **A hawkish FOMC surprise at the ~2026-06-17 meeting
  (anything raising terminal-rate expectations) OR a CPI/PCE print materially
  above consensus in the May/June window.** SaaS has high duration and
  re-prices fast on long-rate moves; with IGV already −21% YTD
  [MACRO:SaaS_Sector_2026 WebSearch:saastr.com], an upside inflation shock
  could push another 5–10% of sector multiple compression onto BL even with
  a clean BL story.

**Exit on invalidation:** **Hard stop, close 100%** if the price-based
trigger fires (two daily closes < $24.85). **Tranche exit (close 50%)** if
the signal-based trigger fires alone, hold the rest to the next daily
re-check. **Tranche exit (close 50%)** if the macro-based trigger fires
alone; reassess. **Close 100%** if any two of the three categories fire
within 3 sessions of each other.

## Sizing (% of risk, NOT dollars)

Using the [rubrics/sizing-rubric.md] Kelly framework with first target
$32.50 and stop $24.85, entry $30.00:

- **Kelly inputs (target = $33.98, the implied-move target — more
  representative of the trade's true objective than the first take-profit):**
  - `p = 0.75` (conviction bin)
  - `b = (33.98 − 30.00) / (30.00 − 24.85) = 3.98 / 5.15 = 0.773`
  - `raw_kelly = (0.75 × 0.773 − 0.25) / 0.773 = 0.330 / 0.773 = 0.427` → **42.7%**
- **Fractional Kelly:** `0.25 × 42.7% = 10.7%`
- **Capped at `cap_pct = 5%`:** `suggested_size_pct = 5%`
- **Final size: 2.5% of book risk** (half of cap)
- **Deviation reason for going BELOW suggested:** none required by rubric
  (always allowed to be smaller). Reason recorded for transparency: phase-8
  desk consensus was "half-Kelly" [AGENT:sweep-tracker][AGENT:risk-monitor],
  and the 0/7 bullish_flow backtest [HIST:historical_signal_backtest] is a
  real regime warning. 2.5% = half the 5% cap, consistent with that desk
  read.

For reference, sizing with the **first take-profit ($32.50)** as target
gives `b = 2.50 / 5.15 = 0.485`, `raw_kelly = (0.75 × 0.485 − 0.25) / 0.485
= 23.5%`, fractional Kelly 5.88%, also capped at 5%. Whichever target is
chosen, the answer caps and we then halve to 2.5%.

## Option structures

### Directional (primary)

**Mirror the institutional buyer's exact contract.**

- **Structure:** Long call (single leg)
- **Strike / expiry:** **BL 2026-12-18 $27.50 call** (lead OI contract)
- **Estimated debit:** ~$8.10 per contract ($810) — today's avg_price was
  `$7.80` with high prints to `$8.40` [FLOW:top_premium_trades]
- **Breakeven (at expiry):** $27.50 + $8.10 = **$35.60**
- **Max loss:** **$810 per contract** (full premium)
- **Delta / vega / theta:** ~0.67 / ~0.082 / ~−0.015 [FLOW:greek_screener]
- **Why this structure:**
  1. **VRP is negative (−0.0889, PREMIUM_BUYING regime)** [HIST:vrp] —
     debit structures are favored over credit.
  2. The contract is ITM with delta 0.67 — high probability of finishing
     in-the-money even if the catalyst doesn't fire; low gap-down vulnerability
     vs OTM options.
  3. **Expiry covers BOTH Q2 (2026-08-04) AND Q3 (~early Nov) earnings**
     [INSIGHT:insights_deep_dive `next_earnings_date=2026-08-04`] — two
     binary catalysts in one position.
  4. Vega 0.082 × ~5,200 contracts of *institutional* size = ~425
     vol-points per 1% IV move — the buyer wants vol *higher* as the catalyst
     approaches, which aligns with our long-vega exposure.
- **Sizing translation:** 2.5% of a $100k notional book = $2,500 → ~3
  contracts. For a $500k book → ~15 contracts. For a $5M book → ~150
  contracts. (Skill has no real account context — these are illustrative.)

### Defined-risk alternative

**Cheaper expression of the same view; sacrifices the blue-sky $40 target
but cuts capital outlay roughly in half.**

- **Structure:** **Call debit vertical** — long $27.5C / short $35C, same
  Dec 18 expiry
- **Strikes / expiry:**
  - Long BL 2026-12-18 $27.50 call @ ~$8.10
  - Short BL 2026-12-18 $35.00 call @ ~$4.00 (estimated; chain is thin away
    from $27.5 — actual quote could vary ±$0.50; verify before placing)
- **Net debit:** ~$4.10 per contract ($410)
- **Breakeven (at expiry):** $27.50 + $4.10 = **$31.60**
- **Max gain (at $35 or above at expiry):** $7.50 − $4.10 = **$340 per
  contract**
- **Max loss:** **$410 per contract**
- **R/R to max profit:** 0.83 : 1
- **Why this structure (when to choose it over the primary):** If the user
  prefers a **capital-efficient** expression, accepting that they cap at
  $35 (one cent above the deep-OTM ladder seeded in phase 3) and forgo the
  $40 stretch target. Better for users who want to size up contract count
  without taking more risk per leg.
- **Caveat — thin chain.** BL options away from $27.5 are illiquid. Quotes
  on the $35 call could be wide; consider working the spread as a single
  combo order, not legging in. If the spread cannot be filled inside $0.20
  of theoretical fair value, default to the primary structure.

## Macro overlay (cite phase-6)

- **Tailwinds:**
  - BL strategic pivot: *"trusted governance and control layer for CFOs
    deploying AI"* — on-trend for AI-narrative inflows
    [MACRO:BL_Q1_2026_2026-05-06 WebSearch:fool.com]
  - BL Q1 non-GAAP EPS beat $0.56 (+14% YoY), 20% FCF margin, ~$525M cash
    vs $667M debt after the March convertible payoff
    [MACRO:BL_Q1_2026_2026-05-06 WebSearch:benzinga.com]
  - Technology sector +$43,979,771 IN (top sector by money-IN today)
    [MACRO:SectorRotation_2026-05-19 UW]
  - SaaS multiples have ALREADY de-rated 21–30% from peak — less further-
    derating risk than names still at peak [MACRO:SaaS_Sector_2026 WebSearch:saastr.com]

- **Headwinds:**
  - Fed held at 3.50–3.75% with FOUR dissents (most since Oct 1992),
    inflation language hardened to "is elevated"
    [MACRO:FOMC_2026-04-29 WebSearch:federalreserve.gov]
  - April CPI sticky: +0.6% MoM, +3.8% YoY headline, +2.8% core YoY
    [MACRO:CPI_2026-04 WebSearch:bls.gov]
  - IGV (software ETF) −21% YTD, −30% from Sep 2025 peak; software now
    trades at-or-below S&P P/E for the first time
    [MACRO:SaaS_Sector_2026 WebSearch:saastr.com]
  - UW regime: **TRANSITIONAL** — "Half position sizes. Favor defined-risk
    strategies." [MACRO:MarketRegime_2026-05-19 UW]
  - Market breadth weak: only 34.7% bullish flow tickers
    [MACRO:MarketRegime_2026-05-19 UW]
  - SPY 9 of 10 recent sessions classified bearish-flow direction despite
    uptrend [MACRO:SPY_HistoricalTrend_2026-05-06_to_05-19 UW]

- **Net:** **mixed — idiosyncratic tailwind, broad headwind.** The trade is
  a bet on idiosyncratic > macro. This is precisely why the sizing is
  half-Kelly and the invalidation is sharp.

## Catalyst calendar (next 30d — and Q2 since the buyer chose Dec expiry)

| Date | Event | Impact direction |
|------|-------|------------------|
| ~2026-05-30 | April PCE Personal Income & Outlays (price index follow-up) | ? — Fed-path repricing |
| ~2026-06-11 | May CPI release | ? — duration-sensitive for SaaS |
| ~2026-06-17 | FOMC meeting (next after Apr) | ?? — 4-dissent context elevates volatility around this print |
| ~2026-07-15 | June CPI | ? |
| ~2026-07-29 | FOMC meeting | ? |
| **2026-08-04** | **BL Q2 2026 earnings (confirmed)** | **HIGH — primary catalyst inside the Dec expiry**; [INSIGHT:insights_deep_dive] implied_move 13.17% |
| ~late Oct / early Nov 2026 | BL Q3 2026 earnings | High — second binary catalyst inside expiry |
| **2026-12-18** | Lead contract expiry (Dec OPEX) | Position resolution |

Within the **next 30 days** (~through 2026-06-18), the highest-impact event
is the **2026-06-17 FOMC**, given the four-dissent FOMC dynamic and the
sticky-inflation tape. There is no BL-specific catalyst in the next 30
days; the Q2 print is 77 days out and inside the Dec expiry.

## Post-trade monitoring checklist

- [ ] **Daily:** re-pull [STRUCT:gex] and [STRUCT:dex] for BL. **Invalidation
      trigger:** total_gex collapses ≥50% in any single session OR net_dex
      drops below +$1B.
- [ ] **Daily:** re-pull [DP:block_stratified] for BL. **Invalidation
      trigger:** large-tier buy_ratio drops below 0.55 (today: 0.893) OR
      block-tier trades flip net-sell.
- [ ] **Daily:** re-pull [INSIGHT:insights_conviction_matrix]. **Invalidation
      trigger:** `scenario` flips from `DIRECTIONAL_LONG` to anything else,
      OR `confidence_pct` falls below 60 (today: 87.53).
- [ ] **Daily price check:** does BL hold above $25.70 intraday? Two
      consecutive daily closes below $24.85 = hard stop.
- [ ] **Every 3 sessions:** re-pull [HIST:historical_cumulative_premium_flow]
      with `days=10`. Trigger: trend flips to BEARISH for 3 consecutive
      sessions.
- [ ] **FOMC week (around 2026-06-17):** check pre-FOMC IV behavior; if IV
      rank spikes above 85, consider rolling the primary structure into the
      defined-risk vertical to lock partial gamma exposure at lower cost.
- [ ] **Watch for changes in the institutional sponsor:** if Dec $27.5C OI
      *declines* meaningfully (e.g. >2,000 contracts in a single day), the
      sponsor is unwinding — exit at least half immediately.

## Citations summary

Minimum 3 distinct upstream datapoints (M-04). For phase-10 audit:

1. **[OI:oi_biggest_increases]** `BL261218C00027500`: `last_oi=3162` →
   `curr_oi=16178`, `oi_diff_plain=13016`, `prev_total_premium=11,647,199`
   — phase-3-positioning.md §"Largest OI increases".
2. **[STRUCT:gex]** Net GEX at strike $27.5 = **$193,037,548.78** of
   `total_gex=$194,349,985` — phase-4-structure.md §"GEX (per strike, ZGL,
   total)".
3. **[DP:block_stratified]** block-tier `buy_ratio=1.00` ($1,048,103 single
   print), large-tier `buy_ratio=0.893` ($4,156,138 across 15 trades) —
   phase-2-dark-pool.md §"Tier breakdown".
4. **[INSIGHT:insights_conviction_matrix]** `scenario=DIRECTIONAL_LONG`,
   `confidence_pct=87.53`, `dark_pool.buy_ratio=0.915`,
   `options_flow.call_ask_volume=5323`, `call_bid_volume=220` —
   phase-7-insights.md §"Conviction matrix".
5. **[HIST:historical_vrp]** `vrp=-0.0889`, `iv30d=0.678`,
   `realised_vol=0.7668`, `regime=PREMIUM_BUYING` — phase-5-historical.md
   §"IV regime".
6. **[HIST:historical_signal_backtest]** `signal_type=bullish_flow`,
   `total_signals=7`, `win_rate=0.0%`, `avg_move_pct=-3.05` —
   phase-5-historical.md §"Signal backtest".
7. **[MACRO:MarketRegime_2026-05-19 UW]** `regime=TRANSITIONAL — Mixed
   signals, reduce position size, wait for clarity`; bullish breadth 34.7%
   — phase-6-macro.md §"Market regime".
8. **[AGENT:risk-monitor]** "Defined-risk only, half size, treat 87.5%
   conviction matrix as one input not gospel — regime says fade, history
   says this exact playbook just lost." — phase-8-agent-views.md
   §"risk-monitor".

(Eight citations exceed the M-04 minimum of three; phase-10 should be able
to spot-check any two and find the cited value at the cited section.)
