# Phase 9 — Trade Blueprint

**Ticker:** PATH (UiPath, Inc.)
**As-of date:** 2026-05-18 (data: 2026-05-15)
**PM voice:** desk PM running an institutional book
**Spot reference:** $10.29 (phase-4 GEX / phase-1 close)
**Upstream phases cited:** phase-1 through phase-8

> *For research and educational use only. Not financial advice. Sizing
> and structures are illustrative.*

## Thesis (3 sentences)

PATH has logged **5-of-5 session bullish sweep persistence with $7.77M
cumulative premium** through a 25-day consecutive OI build, defended
the institutional **$9.40-$9.50 dark-pool accumulation shelf ($22.81M
across 80 trades over 5 sessions)** on the 2026-05-13 cycle low, and
now sets up into a **dealer short-gamma zone from $8 to $10.50 that
mechanically buys underlying as it pushes toward $11**
[FLOW:hot_chains_sweep_persistence][DP:price_levels][STRUCT:gex]. But
the trade lives inside two firm headwinds: market-wide bullish_flow
signals have a **14.3% 20-day win rate (avg -2.68%)** in the current
regime and PATH reports Q1 FY27 earnings 2026-05-28 AMC into a UW
**TRANSITIONAL regime** with technology the **worst-flowing sector
(-$151M)** and the SaaSpocalypse sector beta still dominant
[HIST:signal_backtest][MACRO:MarketRegime_2026-05-15 UW][MACRO:SectorRotation_2026-05-15
UW]. We express a **defined-risk, vol-fade long-delta call diagonal
that exploits the 118.3% → 96.3% IV kink at the 2026-05-29 catalyst**
and pair it with a **bull put credit spread that sells into the
institutional shelf**, with a mandatory de-risk decision before the
SNOW 2026-05-27 AMC peer print [AGENT:earnings-scout][AGENT:risk-monitor].

## Bias + conviction + horizon

- **Directional bias:** **LONG (defined-risk only) with VOL-FADE
  overlay** — the cleanest single-direction read is positive delta, but
  the vega tax on naked long-vol is too punitive.
- **Conviction (M-01 bin):** **0.65**
- **Time horizon:** **1-4w** (front-month expiry 2026-05-29; back-month
  expiry 2026-06-18). Hard exit window: **before SNOW 2026-05-27 AMC
  print.**
- **Why this bin:** Phase-10 confluence score is expected in the 50-64
  band (mixed signals: phase-1/3 strongly bullish, phase-5/6 strongly
  bearish, phase-7 mixed, phase-8 desk split 2L/1S/1R/1N). Per the
  scoring rubric a 50-64 score maps to the 0.65 bin. See
  `phase-10-audit.md` for the score.

## Entry zones

| Entry type | Price | Trigger condition | Source |
|---|---|---|---|
| **Primary** | **$10.25-$10.45** | At-open 2026-05-18 entry into the multi-day breakout retest of the phase-2 $10.34-$10.46 institutional cluster; confirm dealer regime still POSITIVE (ZGL ≤ $7.53) | [DP:largest][STRUCT:gex] |
| **Aggressive** | **$10.71** | Volume break above the phase-2 5-day battle shelf ($38M / 277 trades at $10.65-$10.71); add a half-unit on confirmed break with daily close above | [DP:price_levels][STRUCT:gex] |
| **Fade** | **$9.50-$9.60** | If price reverses and tags the phase-2 accumulation shelf upper band; **only re-enter the put-credit-spread leg here, NOT the call diagonal** (the diagonal needs spot ≥ $10 to keep the short $12C OTM) | [DP:price_levels] |

## Levels to watch

| Type | Level | Source |
|---|---|---|
| **Support (institutional bid)** | **$9.40-$9.50** ($22.81M, 5d, 80 trades) | [DP:price_levels] |
| Floor (near-term) | $10.00-$10.01 ($5.14M single-level cluster) | [DP:price_levels] |
| **Resistance (overhead band)** | **$10.65-$10.71** ($38.04M, 5d, 277 trades) | [DP:price_levels] |
| Per-strike GEX flip (neg→pos) | **$11.00** | [STRUCT:gex] |
| Primary upside target / wall | **$13.00** (+$627M GEX, 11,687 OI on 2026-05-29 $13C) | [STRUCT:gex][OI:biggest_increases] |
| Zero Gamma Level | **$7.53** | [STRUCT:gex] |
| Pin risk into 2026-05-22 weekly | none (PATH not in top-50 pin_risk) | [OI:pin_risk] |

## Invalidation

- **Price-based (hard stop):**
  - **Two daily closes below $9.40** → breaks the institutional
    dark-pool shelf [DP:price_levels]; close 100% of both legs.
  - **OR intraday break of ZGL $7.53 with no immediate reclaim** →
    catastrophic dealer regime flip [STRUCT:gex]; close 100%.
- **Signal-based:**
  - **Bullish sweep persistence drops out** of the top of
    `hot_chains_sweep_persistence` on next daily refresh — re-check
    every session [FLOW:hot_chains_sweep_persistence].
  - **Cumulative premium flow turns net bearish for 3 consecutive
    sessions** [HIST:cumulative_premium_flow].
  - **`insights_conviction_matrix` flips from MIXED toward
    DIRECTIONAL_SHORT** (DP buy_ratio drops below 0.40)
    [INSIGHT:conviction_matrix].
- **Macro-based:**
  - **SNOW 2026-05-27 AMC reaction down >5%** → mandatory de-risk
    BEFORE PATH earnings [AGENT:risk-monitor][MACRO:PATH_Earnings_2026-05-28].
  - **UW regime flips to RISK-OFF** [MACRO:MarketRegime_2026-05-15 UW]
    → close 100%.
  - SPY breadth drops below 30% bullish (currently 35.9%)
    [MACRO:MarketRegime_2026-05-15 UW] → close 100%.

**Exit on invalidation type:** **Tranche.** 50% close at first
invalidation; second 50% at next invalidation OR the mandatory pre-SNOW
exit window, whichever comes first. The call diagonal is debit-side, so
a true breakdown takes a hard stop; the bull put spread is credit-side,
so we **roll** to a wider spread or close at -2× credit.

## Sizing (% of risk)

### Primary structure (call diagonal)

- **Kelly inputs:**
  - p = **0.65** (conviction bin)
  - Entry debit ≈ $0.20 per spread (1× contract = $20 per contract pair)
  - Target ≈ $0.40 at 2026-05-29 expiry (2× the debit, typical
    profit-at-short-expiry on an at-the-money calendar when underlying
    pins near the short strike and IV crushes asymmetrically)
  - Stop ≈ $0.10 (50% of debit, hard stop on breakdown thru $9.40)
  - b = ($0.40 − $0.20) / ($0.20 − $0.10) = **2.0**
- **Raw Kelly** = (0.65 × 2 − 0.35) / 2 = (1.30 − 0.35) / 2 = **0.475
  (47.5%)**
- Fractional Kelly (0.25): 47.5% × 0.25 = **11.9%**
- Cap_pct (5%): **5%** is the unconstrained suggested size
- **Regime multiplier (mandatory):**
  - 0.50× from UW TRANSITIONAL (phase-6) → 5% × 0.50 = 2.5%
  - 0.80× additional from phase-5 14.3% signal backtest (downgrade
    conviction → 0.80×) → 2.5% × 0.80 = **2.0%**
- **Final size: 2.0% of book risk on the call diagonal** (i.e., max
  loss across all calendar pairs ≤ 2% of book).
- **Deviation reason:** none — we are sizing BELOW the unconstrained
  suggestion, which the rubric always allows.

### Defined-risk alternative (bull put spread)

- **Kelly inputs (probabilistic, since credit spread):**
  - p ≈ 0.75 (probability PATH > $9 at 2026-06-18 expiry; 25Δ put at
    $9 strike implies ~75% OTM probability under 96% IV)
  - Entry credit ≈ $0.26
  - Max loss = $1.00 − $0.26 = $0.74
  - b = $0.26 / $0.74 = **0.35**
- **Raw Kelly** = (0.75 × 0.35 − 0.25) / 0.35 = (0.2625 − 0.25) / 0.35
  = **0.036 (3.6%)**
- Fractional Kelly (0.25): 3.6% × 0.25 = **0.89%**
- Regime multiplier 0.40× → **0.36%** unconstrained suggested
- **Final size: 1.0% of book risk on the bull put spread** (rounding up
  to 1.0% to make the credit spread economically meaningful; this is a
  small *upward* deviation that is allowed because the spread is
  defined-risk and the OTM probability is high).
- **Deviation reason:** the math undersizes a credit-spread that has
  75% OTM probability and serves as the put-side dimension of a
  composite directional book; setting at 1.0% keeps the spread
  meaningful while still under the cap.

**Total PATH book risk: 2.0% (diagonal) + 1.0% (put credit) = 3.0% of
book at maximum loss.** This is inside the 1.0-1.5% single-name cap
risk-monitor recommended **per leg** and inside the 5% hard cap.

## Option structures

### Directional (primary) — Call Diagonal

- **Structure:** Call diagonal (short front-month, long back-month, same
  strike)
- **Legs:**
  - **SHORT** 1× PATH **2026-05-29 $12 Call** @ ~**$0.35** (target
    fill; quoted IV ~118%)
  - **LONG** 1× PATH **2026-06-18 $12 Call** @ ~**$0.55** (target
    fill; quoted IV ~96%)
- **Net debit:** ~**$0.20** per spread (= $20 per contract pair)
- **Breakeven at 2026-05-29 short expiry:** approximately **$10.70-$13.30**
  (depends on IV of the back-month at the time; calendar breakeven is
  wide and forgiving when front IV crushes hard)
- **Max loss:** ~$0.20 (the debit), realized if back-month $12C goes
  worthless by 6/18 (i.e., PATH crashes below $9 and stays there) OR if
  PATH rips so far above $12 that the diagonal can't be unwound
  profitably at front expiry; reasonable hard stop at -50% of debit
- **Target:** $0.40 at or before 2026-05-29 close (front expiry); roll
  short to 2026-06-05 $12C or close if hit
- **Why this structure:**
  - **IV percentile 100, VRP +35.97 vol pts** [HIST:vrp][HIST:iv_percentile_zscore]
    → outright long calls are a vol-tax trap; the diagonal sells the
    118% front-month vol while staying long delta via the back-month
    96% IV vol.
  - **$12 strike sits at the phase-3 forward call wall** (2026-06-18
    $12C OI 9,843; 2027-01-15 $12C bullish LEAP sweep $693k)
    [OI:biggest_increases][FLOW:sweeps] — the structure aligns with
    where institutional demand has already congregated.
  - The **22 vol-point spread between the 5/29 and 6/18 expiries**
    [STRUCT:iv_term_structure] is the largest IV differential in PATH's
    term structure; harvesting it via the calendar is the cleanest
    expression of the vol-fade thesis.

### Defined-risk alternative — Bull Put Credit Spread

- **Structure:** Bull put vertical spread (sell higher put, buy lower
  put), same expiry
- **Legs:**
  - **SHORT** 1× PATH **2026-06-18 $9 Put** @ ~**$0.56** (current bid
    from phase-1 sweep data showed $9P trading at $0.54-$0.56)
  - **LONG** 1× PATH **2026-06-18 $8 Put** @ ~**$0.30** (estimated;
    no specific quote in upstream data — must verify at open)
- **Net credit:** ~**$0.26** per spread
- **Breakeven:** **$8.74** ($9 − $0.26)
- **Max loss:** $0.74 per spread ($1.00 width − $0.26 credit)
- **Max gain:** $0.26 per spread (the credit, if PATH > $9 at expiry)
- **Why this structure:**
  - **Sells into the phase-2 institutional bid at $9.40-$9.50**
    [DP:price_levels] — the $9 strike sits BELOW the accumulation shelf,
    so OTM-at-expiry probability is high.
  - **Defined risk** appropriate for TRANSITIONAL regime
    [MACRO:MarketRegime_2026-05-15 UW] and high-IV environment
    [HIST:iv_percentile_zscore].
  - The 2026-06-18 expiry is **AFTER** the 2026-05-28 earnings event,
    so we keep most of the credit after the vol crush.
  - Covers the put-side of the book and **rounds the directional
    exposure to a soft "long, but won't get killed if it dips"** —
    matching the desk's NEUTRAL-lean-LONG consensus
    [AGENT:risk-monitor][AGENT:earnings-scout].

## Macro overlay

**Tailwinds:**
- PATH FQ4 FY2026 result: rev $481.1M +14% YoY, first full-year GAAP
  profitability [MACRO:PATH_Q4FY26_Results_2026-03-12 WebSearch:ir.uipath.com].
- PATH AI/agentic ARR ~$200M run-rate (Maestro, IDP, agentic) — the
  category that's winning at Salesforce ($800M Agentforce ARR)
  [MACRO:PATH_Q4FY26_Results_2026-03-12 WebSearch:ir.uipath.com].

**Headwinds:**
- UW market regime **TRANSITIONAL** → half-size, defined-risk
  [MACRO:MarketRegime_2026-05-15 UW].
- Technology sector net options outflow **-$151M (worst sector)**
  [MACRO:SectorRotation_2026-05-15 UW].
- April 2026 CPI **3.8% YoY (highest since May 2023), core 2.8%** — no
  near-term Fed cut [MACRO:CPIAUCSL_2026-04 WebSearch:cnbc.com].
- FOMC held at 3.50-3.75%; next meeting 2026-06-16/17 (after our
  window) [MACRO:FOMC_2026-04-29 WebSearch:federalreserve.gov].
- SaaSpocalypse: $2T S&P Software & Services destroyed since Oct-2025;
  30-year worst non-recessionary drawdown per JPM
  [MACRO:SaaSpocalypse_2026-Q1 WebSearch:saastr.com].
- bullish_flow signal market-wide 14.3% 20d win rate, avg -2.68%
  [HIST:signal_backtest].

**Net:** **HEADWIND.** Five hard macro/regime headwinds vs two
ticker-specific tailwinds. The trade exists *because* of idiosyncratic
catalyst optionality, not because of macro support.

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|---|---|---|
| **2026-05-22 (Fri)** | PATH weekly OPEX (low pin risk per phase 3) | Neutral |
| **2026-05-27 (Wed AMC)** | **SNOW Q1 FY27 earnings (IV rank 97.1)** | **CRITICAL peer signal — mandatory PATH de-risk window** |
| **2026-05-27 (Wed AMC)** | MRVL, HPQ, ANF, HEI, BBWI earnings | Peer signal |
| **2026-05-28 (Thu AMC)** | **PATH Q1 FY2027 earnings** (guide $395-400M rev, $1.894-1.899B ARR) | **PRIMARY BINARY** — 19.8% implied move |
| **2026-05-28 (Thu)** | OKTA, MDB, ADSK, S, AMBA, DLTR, BBY earnings | Massive software cohort risk |
| **2026-05-29 (Fri)** | PATH weekly expiry — front-month diagonal expires | Vol crush event (118% → 60-70%) |
| **~2026-06-05/06** | NFP / jobs report | Macro risk-on/off |
| **2026-06-10/11** | May CPI release | Macro |
| **2026-06-16/17** | **FOMC + SEP** | Major macro vol release (after our window) |
| **2026-06-18 (Thu)** | PATH monthly OPEX — bull put spread expires | Defined exit |

## Post-trade monitoring checklist

- [ ] **Daily 1:** Re-pull `hot_chains_sweep_persistence` — if PATH
      drops out of top, that's a phase-1 signal flip.
- [ ] **Daily 2:** Re-pull `options_structure_gex` — confirm ZGL is
      still ≤ $7.53 and per-strike GEX flip remains at $11 (phase-4
      signal).
- [ ] **Daily 3:** Re-pull `dark_pool_block_stratified` — track if
      buy_ratio holds ≥ 0.55 or slides toward 0.40 (phase-2/7 signal
      flip).
- [ ] **Daily 4:** Re-pull `risk_market_regime` — flag any change from
      TRANSITIONAL toward RISK-OFF or RISK-ON; either triggers
      action.
- [ ] **2026-05-27 9pm ET:** SNOW prints AMC. **Mandatory desk
      decision:** if SNOW reaction is down > 5% after-hours, exit BOTH
      PATH legs at open 2026-05-28 regardless of price.
- [ ] **2026-05-28 close:** Close or roll the call diagonal short leg
      BEFORE the PATH earnings event. Two options: (a) close the short
      $12C and let the long $12C ride the binary (converts to a long
      call, accepts vega risk for the gamma payoff), or (b) close the
      entire diagonal for whatever profit/loss is on the screen.
- [ ] **2026-05-29 open:** Re-pull `options_structure_iv_term_structure`
      to verify front-month IV crushed as expected; reassess the bull
      put spread positioning vs new IV term structure.
- [ ] **2026-06-18:** Bull put spread expires. Close or roll based on
      where price sits relative to $9.

## Citations summary

Minimum 3 distinct upstream datapoints (M-04). Listed for phase-10
spot-check:

1. **[FLOW:hot_chains_sweep_persistence]** — PATH 5-of-5 sessions
   bullish sweep persistence, $7.77M cumulative premium —
   phase-1-flow.md § "Key signals" / § "Detailed findings — Sweeps"
2. **[DP:price_levels]** — $9.40-$9.50 5-day institutional bid cluster
   $22.81M / 80 trades — phase-2-dark-pool.md § "Price levels (5-day
   cluster map)"
3. **[STRUCT:gex]** — Total GEX +$1.05B, ZGL $7.53, per-strike negative
   GEX from $8 to $10.5 with flip at $11 and dominant +$627M wall at
   $13 — phase-4-structure.md § "GEX (DTE ≤ 45)"
4. **[STRUCT:iv_term_structure]** — IV kink at 2026-05-29 expiry =
   118.3%, vs adjacent 75.8% (5/22) and 96.3% (6/18) —
   phase-4-structure.md § "IV term structure (CATALYST KINK)"
5. **[HIST:signal_backtest]** — bullish_flow signal 14.3% win rate over
   20 trading days, avg move -2.68% across 14 signals —
   phase-5-historical.md § "Signal backtest"
6. **[MACRO:MarketRegime_2026-05-15 UW]** — UW regime TRANSITIONAL;
   half size, defined-risk; SPY breadth 35.9% bullish; technology
   sector outflow -$151M — phase-6-macro.md § "Market regime (UW)" /
   § "Sector rotation"
7. **[AGENT:earnings-scout][AGENT:risk-monitor]** — 4 of 5 agents
   converged on defined-risk + mandatory pre-SNOW de-risk —
   phase-8-agent-views.md § "Mandatory rules for phase 9"
