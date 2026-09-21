# Phase 9 — Trade Blueprint

**Ticker:** FSLY
**As-of date:** 2026-05-19  (Effective data date: 2026-05-18)
**PM voice:** desk PM running an institutional options-overlay book
**Spot reference:** $16.71 (UW screener close 2026-05-18, [INSIGHT:deep_dive], phase-7)
**Upstream phases cited:** phase-1 through phase-8

> *For research and educational use only. Not financial advice.
> Sizing and structures are illustrative.*

## Thesis (≤3 sentences)

Institutions are quietly **accumulating FSLY at $16.48–$16.60 while
writing $20+ calls for yield** — the cleanest single read of the
day, captured by UW's `insights_conviction_matrix = COVERED_CALL`
with DP buy_ratio 0.692 and net call-bid > call-ask (3,534 vs
2,858) [INSIGHT:conviction_matrix]. The signal-stack is corroborated
by a 5-of-5 session sweep persistence on Sep'26 $17.5C (consistency
1.0, $642,945 in 5-day premium) [FLOW:hot_chains_sweep_persistence]
and a 30-DTE reverse skew (call IV 83.4% > put IV 79.9%,
COMPLACENT label) [STRUCT:term_skew]. But this is **not a moonshot**
— the tech sector took a **−$299.8M premium outflow on 5/18 alone**
[MACRO:MarketRegime_2026-05-18 UW] and the bullish_flow backtest is
**8.3% win rate over the last 5 sessions** [HIST:signal_backtest],
so the right play is a defined-risk LONG sized inside the cap with
explicit ceiling at $20.

## Bias + conviction + horizon

- **Directional bias:** **LONG (covered-call / wheel posture)**
- **Conviction (M-01 bin):** **0.65** (moderate edge — more likely
  than not, with real disconfirming evidence)
- **Time horizon:** **1-4w** (matches dominant phase-8 agent horizon
  3-of-4)
- **Why this bin** (one sentence citing phase-10 confluence
  estimate): Confluence score is in the 50-64 band (estimated 57,
  to be confirmed by phase-10), which maps to the 0.65 bin in the
  scoring rubric.

## Entry zones

| Entry type | Price | Trigger condition | Source |
|---|---|---|---|
| Primary | **$16.40 – $16.60** | Tag of institutional VWAP $16.57 with intraday DP buy print > 50K shares above mid | [DP:price_levels], [INSIGHT:institutional_accumulation] |
| Aggressive | **$17.50 break with hold** | Close above $17.50 on rising day-volume; the 5/22 gamma magnet flips into long-gamma terrain | [STRUCT:today_gamma_flip] |
| Fade | **$18.50 – $18.84** | Test of overhead DP supply ($22M zone) with rejection candle — *short-side fade only*, smaller risk allocation | [DP:price_levels] |

## Levels to watch

| Type | Level | Source |
|---|---|---|
| Support (primary) | **$16.48** | $3.49M / 211,800 shares 5d DP cluster [DP:price_levels] |
| Support (secondary) | $16.00 | 5/22 GEX resistance turning support post-pin [STRUCT:today_gamma_flip] |
| Resistance (primary) | **$17.50** | 5/22 SUPPORT wall $+12.57M GEX (acts as magnet then resistance) [STRUCT:today_gamma_flip] + biggest standing OI cluster at $17.5 across multiple expiries [OI:biggest_increases] |
| Resistance (next leg) | **$18.84** | Largest 5d DP cluster $5.65M, top of $22M supply wall $18.41-$19.03 [DP:price_levels] |
| Resistance (institutional ceiling) | **$20.00** | 5,454 standing OI (Jun + Sep $20C) [OI:biggest_increases]; institutional COVERED_CALL strike [INSIGHT:conviction_matrix] |
| Hard ceiling | $23.00 | 6/5 $23C +300 OI new bid-side write (18 DTE) [OI:smart_positioning] |
| Gamma flip (45-DTE) | $9.00 (ZGL) | Well below spot → constructive [STRUCT:gex] |
| Gamma flip (0-DTE / 5/22) | $10.58 | Far below spot → 5/22 is long-gamma regime [STRUCT:today_gamma_flip] |
| Largest pin | n/a | FSLY absent from `oi_pin_risk` top-50 (no meaningful 5/22 pin) [OI:pin_risk] |

## Invalidation

- **Price-based:** **Two consecutive daily closes below $15.50.**
  This level breaks the deepening negative-gamma pocket at $15
  (GEX −$8.2M) and violates the put-write floor (multiple bid-side
  put sells at 5/22/7/17/9/18 $15P). [STRUCT:gex] [OI:smart_positioning]
- **Signal-based:** Any ONE of:
  (a) `insights_institutional_accumulation` flips from
  ACCUMULATION (current 2.25× buy/sell) to DISTRIBUTION
  [INSIGHT:institutional_accumulation];
  (b) `insights_conviction_matrix` flips from COVERED_CALL to
  DIRECTIONAL_SHORT [INSIGHT:conviction_matrix];
  (c) Cumulative premium flow turns net BEARISH on a 3-session
  rolling basis (90d currently +$9.9M net BULLISH)
  [HIST:cumulative_premium_flow].
- **Macro-based:** Any ONE of:
  (a) **Tech sector premium outflow accelerates to ≤ −$500M for
  3 consecutive sessions** (current −$299.8M one day)
  [MACRO:MarketRegime_2026-05-18 UW];
  (b) **10y yield closes above 4.75%** (current 4.61%)
  [MACRO:DGS10_2026-05-18 WebSearch];
  (c) **June FOMC delivers a hawkish surprise** (rate path
  shifts up vs current 3.50-3.75% / dot plot tightens)
  [MACRO:FOMC_2026-04-29 WebSearch].

## Sizing (% of risk, NOT dollars)

- **Kelly inputs:** p = **0.65**, entry = **$16.55** (between
  primary low $16.40 and high $16.60), target = **$18.84**
  (resistance), stop = **$15.50** (invalidation).
- Long payoff distance: $18.84 − $16.55 = **$2.29**
- Long risk distance: $16.55 − $15.50 = **$1.05**
- **b = 2.29 / 1.05 = 2.18**
- **Raw Kelly** = (0.65 × 2.18 − 0.35) / 2.18 = (1.417 − 0.35) /
  2.18 = 1.067 / 2.18 = **0.489 (48.9%)**
- Fractional Kelly × 0.25 = **12.2%**
- Hard cap at 5% → suggested_size_pct = **5.0%**
- **Final size = 2.5% of book risk** (HALF the cap, no
  deviation_reason required because deviation is downward).
- **Why downward deviation:** phase-8 risk-monitor explicitly
  flagged "half size at most, defined-risk only" given the
  hostile tech regime and SMH bearish 5-confluence stack
  [AGENT:risk-monitor].

## Option structures

### Directional (primary)

- **Structure:** **Bull call debit spread**, 7/17 $17.5 / $22.5
- **Strike(s) / expiry:** Long 7/17/2026 $17.5C; Short 7/17/2026
  $22.5C
- **Why these strikes:**
  - Long $17.5 = the campaign strike + 5/22 gamma magnet
    + biggest near-DTE call OI [FLOW:options_flow_sweeps]
    [STRUCT:today_gamma_flip]
  - Short $22.5 = institutional cap zone (6/5 $23C bid write +300
    OI; 9/18 $22.5C +171 OI bear-write) [OI:smart_positioning]
  - 7/17 expiry sits AFTER the 5/22 IV-crush event and BEFORE the
    August earnings — clean window for the directional read to
    play out [STRUCT:iv_term_structure] [MACRO:FSLY_Q1_2026 WebSearch:fool.com]
- **Estimated debit:** ~$1.80 per spread (7/17 $17.5C ~$2.50 mid,
  7/17 $22.5C ~$0.70 mid — both extrapolated from phase-1 trade
  prints and phase-4 expiry-IV map; verify at execution)
- **Width:** $5.00; **Max profit:** ~$3.20; **Max loss:** ~$1.80
- **Breakeven:** ~$19.30
- **Payoff ratio (debit-spread):** 3.20 / 1.80 = **1.78**
- **Vol context:** IV percentile 7.7% (1y), VRP −0.85 →
  PREMIUM_BUYING regime favors debit structures
  [HIST:iv_percentile_zscore] [HIST:vrp]. Avoiding 5/22 specifically
  (117.7% IV is rich on the front week).
- **Sizing constraint:** ≤ 2.5% × book risk in net debit. (e.g., on
  a $100K book, ≤ $2,500 total debit ⇒ ~14 spreads at $1.80.)

### Defined-risk alternative

- **Structure:** **Bull put credit spread**, 7/17 $15 / $12.5
- **Strike(s) / expiry:** Short 7/17/2026 $15P; Long 7/17/2026
  $12.5P
- **Why these strikes:**
  - Short $15P sits on the institutional put-sell floor (5/22 $15P,
    6/12 $15P, 7/17 $15P all opened bid-side) [OI:smart_positioning]
    — "willing to own at $15" institutional behavior
  - Long $12.5P caps the downside and aligns with the −$2.27M GEX
    tail at $12.5 strike [STRUCT:gex]
- **Estimated credit:** ~$0.80 per spread (7/17 $15P bid ~$1.50
  mid from phase-1 sweep print; 7/17 $12.5P ~$0.70 mid)
- **Width:** $2.50; **Max profit:** $0.80 ($80); **Max loss:**
  $2.50 − $0.80 = **$1.70 ($170)**
- **Breakeven:** $14.20
- **Payoff (credit spread):** 0.80 / 1.70 = **0.47** (expected; this
  is a sell-premium structure — different geometry, takes time
  decay as edge)
- **When to prefer over the call spread:** if you want exposure to
  the COVERED_CALL "wheel" thesis without paying the front-week
  premium; sells the side institutions are SELLING (puts at $15).
- **Sizing constraint:** ≤ 2.5% × book risk in max_loss. (e.g., on
  a $100K book, ≤ $2,500 max loss ⇒ ~14 spreads at $170.)

## Macro overlay (cite phase-6)

**Tailwinds**

- AI-infra narrative: Compute segment +67% YoY in Q1 2026
  [MACRO:FSLY_Q1_2026 WebSearch:fool.com] — single
  ticker-specific bull.
- FMR LLC (Fidelity) 7.77M-share position at $29.06 cost basis
  [MACRO:FSLY_FMR_2026-03-31 WebSearch:gurufocus.com] —
  large institutional incentive to defend ~$16-17 area or
  average in.
- VRP −0.85, IV percentile 7.7% → premium-buying favorable
  [HIST:vrp] [HIST:iv_percentile_zscore].

**Headwinds**

- Technology sector premium outflow −$299.8M on 5/18 (30× next
  worst) [MACRO:MarketRegime_2026-05-18 UW] — **the binding
  constraint on sizing**.
- April CPI 3.8% YoY (highest since May 2023), Iran-shock-driven
  [MACRO:CPIAUCSL_2026-04 WebSearch:bls.gov] — re-acceleration
  removes near-term rate-cut tailwind.
- 10y yield 4.61% (highest since Feb 2025)
  [MACRO:DGS10_2026-05-18 WebSearch:advisorperspectives.com]
  — duration headwind for tech multiples.
- Market regime TRANSITIONAL, 35.7% breadth, UW guidance "half
  size, defined-risk" [MACRO:MarketRegime_2026-05-18 UW].
- bullish_flow signal backtest 8.3% win rate
  [HIST:signal_backtest] — regime is hostile to bullish_flow
  setups.

**Net:** **NET HEADWIND** (~6 head / 3 tail / 1 neutral). This is
why sizing is at half-cap (2.5%), not full-cap (5%), and why the
structure is defined-risk only.

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|---|---|---|
| 2026-05-22 (Fri) | **May monthly OPEX** | + for vanna squeeze if IV crushes; expected mechanical IV decay [MACRO:MarketRegime_2026-05-18 UW] [STRUCT:vanna_charm] |
| ~2026-06-11 (Wed est) | May CPI release | +/− binary — hot print = headwind, cool print = tailwind |
| ~2026-06-17/18 (Tue/Wed est) | June FOMC + SEP / dot plot | +/− major — primary near-term macro catalyst |
| ~2026-06-19 (Fri) | June quad-witching | Mechanical gamma event |
| Ongoing | Iran conflict + oil tape | − while elevated; resolution = +tail |

## Post-trade monitoring checklist

- [ ] **Re-run `dark_pool_block_stratified` and
  `dark_pool_largest` daily** — confirm block buy_ratio stays
  ≥ 0.55; flag if it drops below 0.40.
- [ ] **Watch `insights_institutional_accumulation` for the
  ACCUMULATION → NEUTRAL → DISTRIBUTION ladder** — first step
  down to NEUTRAL = trim size 50%; step to DISTRIBUTION = full
  exit per invalidation rubric.
- [ ] **Track `historical_cumulative_premium_flow` 5-day
  rolling** — currently +$9.9M (90d); if 5d rolling flips net
  bearish for 3 consecutive sessions, exit per
  signal-based invalidation.
- [ ] **Daily UW `risk_market_regime`** — current TRANSITIONAL;
  shift to RISK-OFF = exit; shift to RISK-ON = consider sizing up
  to 5% cap on next entry.
- [ ] **5/22 close** — verify 5/22 IV collapses (vanna squeeze
  fires) or doesn't (event was real). If IV stays > 90% on 5/29
  expiry post-OPEX, hidden catalyst is still live — investigate.
- [ ] **10y yield daily** — invalidation trigger at close > 4.75%.
- [ ] **Tech sector net flow daily** — invalidation trigger at
  ≤ −$500M for 3 sessions.

## Conviction deviation

None. Conviction bin (0.65) matches the estimated phase-10
confluence band (50-64). Final sizing deviated DOWNWARD from
suggested 5% to 2.5% per risk-monitor's regime warning — downward
deviation is always allowed without a `deviation_reason` field.

## Citations summary

Phase-9 thesis (M-04: ≥3 distinct upstream datapoints), spot-checkable
in phase MDs:

1. **[INSIGHT:conviction_matrix]** — "COVERED_CALL scenario,
   confidence 24.51%, DP buy_ratio 0.692, call_bid_volume 3,534 vs
   call_ask_volume 2,858" — phase-7-insights.md § "Conviction
   matrix — COVERED_CALL".
2. **[FLOW:hot_chains_sweep_persistence]** — "FSLY 5-of-5
   sessions, consistency_score 1.0, $642,945 5-day sweep premium"
   — phase-1-flow.md § "Multi-day persistence".
3. **[STRUCT:term_skew]** — "30 DTE 25Δ call IV 83.43% vs put IV
   79.92%; skew_ratio 0.958; interpretation COMPLACENT" —
   phase-4-structure.md § "Term skew — REVERSE / COMPLACENT".
4. **[MACRO:MarketRegime_2026-05-18 UW]** — "Technology sector
   net flow −$299,789,934; market regime TRANSITIONAL, bullish
   breadth 35.7%" — phase-6-macro.md § "Market regime (UW)".
5. **[HIST:signal_backtest]** — "bullish_flow signal_type,
   total_signals 12, win_rate 8.3%, avg_move_pct −3.22%" —
   phase-5-historical.md § "Signal backtest — CAUTION".
6. **[AGENT:risk-monitor]** — "Half-size at most, defined-risk
   only — this is a covered-call/wheel name in a hostile tech
   regime" — phase-8-agent-views.md § "Per-agent details /
   risk-monitor".
