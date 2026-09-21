# Phase 9 — Trade Blueprint

**Ticker:** RDDT
**As-of date:** 2026-05-20 (data anchor 2026-05-18; next-session
2026-05-19 close $154.91 visible in `historical_trend`)
**PM voice:** desk PM running an institutional book
**Spot reference:** $158.89 (phase-4 GEX) at the 5/18 close;
$154.91 at the 5/19 close — current actionable spot is the lower
of the two for entry-level planning
**Upstream phases cited:** phase-1 through phase-8

> *For research and educational use only. Not financial advice.
> Sizing and structures are illustrative.*

## Thesis (≤3 sentences)

Real institutional accumulation is being built on RDDT around
**$154–$160** — block-tier dark-pool buy ratio **0.793 on $26.26M
single-session** [DP:block_stratified] with a **post-close +$1.36
over-mid** lift of >$2M [DP:dark_pool_extended_hours] anchored by a
5-day institutional shelf at $154.12 [DP:price_levels] — but
historical context says this **bullish-flow signature has had a 0%
5-day win rate** across MSFT/AAPL/QQQ/SMH/META/AVGO/UPS in the past
week [HIST:signal_backtest], confirmed by RDDT's own 5/19
**-2.64% next-day drop** and GEX regime flip POS→NEG
[HIST:gex_time_series]. With macro in **TRANSITIONAL regime + Comm
Services -$20.5M sector outflow** [MACRO:MarketRegime_2026-05-18]
and the desk panel splitting NEUTRAL-2 / LONG-1 / SHORT-1
[AGENT:risk-monitor, AGENT:contrarian-scanner], this is a
**buy-the-dip-only, defined-risk, half-size LONG**, not a chase.

## Bias + conviction + horizon

- **Directional bias:** LONG (buy-the-dip)
- **Conviction (M-01 bin):** **0.65** (moderate edge with real
  disconfirming evidence)
- **Time horizon:** **1-4w** (constructive window between current
  spot and the 2026-07-30 Q2 earnings catalyst)
- **Why this bin** (one sentence preview of phase-10 confluence):
  three strongly-positive phases (DP, STRUCT, INSIGHT) are partly
  offset by two strongly-negative phases (HIST, MACRO) and a split
  agent panel — confluence will land in the 55-65 band, which maps
  to the 0.65 bin per `rubrics/confluence-scoring.md`.

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| Primary    | **$154.00–$155.00** | Tag of the 5-day institutional DP shelf with intraday absorption (no impulsive break below $154) | [DP:price_levels] (5-day $154.12 = $9.02M / 58.5k shares cluster) |
| Aggressive | **$158.39 reclaim** | Spot reclaims chain ZGL AND GEX time-series re-flips to POSITIVE on next refresh | [STRUCT:gex] (ZGL 158.39, regime flipped POS→NEG on 5/19 per [HIST:gex_time_series]) |
| Fade       | **$160.50+** | Daily close > $160.50 on >1.5× 20D avg volume — chase only on confirmed gamma squeeze | [STRUCT:today_gamma_flip] (5/22 $160 wall +$602M; $160.50 was the 5/18 HOD with a $1.49M DP block printed AT it per [DP:largest]) |

**Do not initiate at current spot ($154.91)** without first seeing
absorption at the $154 shelf. If RDDT slides through $154 on volume
without bid response, the thesis is invalidated before entry.

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Primary support | **$154.12** | [DP:price_levels] (5-day densest cluster, $9.02M, 58,529 shares) |
| Secondary support | **$151.00–$152.50** | [DP:price_levels] (next two clusters, ~$5.85M combined) |
| Tertiary support | **$150.00** | [STRUCT:gex] (largest short-γ hole, -$77.3M); [DP:price_levels] $150 cluster $2.29M |
| Gamma flip (chain ZGL) | **$158.39** | [STRUCT:gex] |
| Today's ZGL (5/22 expiry) | **$158.03** | [STRUCT:today_gamma_flip] |
| ATM flip strike | **$157.50** | [STRUCT:today_gamma_flip] |
| Primary resistance / magnet | **$160.00** | [STRUCT:gex] (+$622.7M GEX = 49% of chain); [OI:biggest_increases] (5/22 OI 3,592, 6/18 OI 1,693) |
| Secondary resistance | **$165 / $167.50** | [STRUCT:gex] (165 +$178M, 167.5 +$121M GEX walls) |
| Major target if breakout | **$170.00** | [STRUCT:gex] (+$282M GEX wall, 2nd largest); [FLOW:options_flow_sweeps] (8/21 170C $356k ask-side bullish prints) |
| VWAP / institutional cost basis | **$158.47** | [INSIGHT:institutional_accumulation] |

## Invalidation

- **Price-based:**
  1. **Two consecutive daily closes below $154.00** (DP 5-day shelf
     fails) — HARD STOP, close 100%.
  2. **Intraday break of $150.00** with no immediate reclaim (enters
     phase-4 short-gamma hole at -$77M, opens path to $140 next
     [STRUCT:gex]) — HARD STOP triggered ahead of #1 if it fires first.
- **Signal-based:**
  1. **DP buy_ratio drops below 0.50 on the next available
     `dark_pool_block_stratified` refresh** (distribution flip from
     the current 0.793 [DP:block_stratified]).
  2. **`insights_conviction_matrix` flips from DIRECTIONAL_LONG to
     either HEDGED_LONG or MIXED** [INSIGHT:conviction_matrix].
  3. **Cumulative premium flow turns net-bearish for 3 consecutive
     sessions** from `historical_cumulative_premium_flow`
     [HIST:cumulative_premium_flow] (currently MIXED at +$5.5M over
     90d; tipping further negative kills the multi-week thesis).
- **Macro-based:**
  1. **UW `risk_market_regime` flips to RISK-OFF** or to TRANSITIONAL
     "Reduce size" guidance escalates [MACRO:MarketRegime_2026-05-18]
     — currently already TRANSITIONAL, so further deterioration means
     half size becomes zero.
  2. **June 16-17 FOMC** delivers a hawkish surprise (no cut in
     2026, or "extended hold" framing) [MACRO:FOMC_2026-04-29] —
     prepares to roll defined-risk into bear structures.
  3. **Sector rotation continues:** Comm Services net outflow > $50M
     for 2 consecutive sessions [MACRO:MarketRegime_2026-05-18].

**Exit method:** **HARD STOP** at $154 (close 100%, both legs of
either structure). Debit structures are not rolled — losses are
realized cleanly at the price level.

## Sizing (% of risk, NOT dollars)

**Kelly inputs:**
- p = **0.65** (conviction bin)
- Entry = **$155.00** (midpoint of primary entry zone)
- Stop = **$151.00** (just below secondary DP support shelf, above
  the tertiary $150 short-gamma cliff for stop-fire vs trigger
  separation)
- Target = **$170.00** (phase-4 secondary GEX wall, +$282M)
- b = (170 − 155) / (155 − 151) = **15 / 4 = 3.75**
- fraction = 0.25
- cap_pct = 5

**Raw Kelly:**
```
raw_kelly = (0.65 × 3.75 − 0.35) / 3.75
          = (2.4375 − 0.35) / 3.75
          = 2.0875 / 3.75
          = 0.5567  (55.67%)
suggested_size_pct = 0.5567 × 0.25 × 100 = 13.92%
capped at cap_pct (5%) = 5.00%
```

**Final size: 2.5% of book risk.**

**Deviation reason (downward, always allowed):** TRANSITIONAL regime
prescribes "half position sizes" [MACRO:MarketRegime_2026-05-18] AND
phase-5 `bullish_flow` 5d backtest win rate is 0.0% in the current
regime [HIST:signal_backtest] AND phase-8 risk-monitor recommended
"25-33% of normal" [AGENT:risk-monitor] — halving the 5% Kelly cap
to 2.5% is consistent with all three signals.

## Option structures

### Directional (primary) — 7/17 155/175 call debit spread

- **Structure:** Long-call debit vertical (long lower strike, short
  higher strike)
- **Strike(s) / expiry:** Long 1× **RDDT 2026-07-17 155C**, Short
  1× **RDDT 2026-07-17 175C**
- **Debit/credit:** Net **debit ~$8.00** per spread (long 155C ~$13,
  short 175C ~$5; estimates from phase-1 [FLOW:options_flow_sweeps]
  prints showing 7/17 170C @ $11.94 ask and 7/17 175C @ $9.40-$9.87
  range — interpolating for 7/17 155C ATM at ~$13 with IV 63.5%
  [STRUCT:iv_term_structure])
- **Breakeven:** $155 + $8 = **$163.00** at 7/17 expiration
- **Max loss:** $8.00 × 100 = **$800 per spread** (full debit)
- **Max gain:** ($175 − $155) − $8 = **$12.00 × 100 = $1,200 per
  spread** (if RDDT closes ≥ $175 at 7/17)
- **Payoff ratio:** 1.50 : 1 (gain : loss)
- **Sizing:** 2.5% of book risk ÷ $800 per spread = number of spreads
- **Why this structure:**
  - 7/17 expires **13 days BEFORE the 2026-07-30 Q2 earnings**
    [INSIGHT:deep_dive] — captures the entire 1-4w constructive
    window WITHOUT taking earnings IV-crush risk.
  - Long 155C strike sits at the chain VWAP $158.47
    [INSIGHT:institutional_accumulation] minus 2% — captures upside
    from a $155 entry through the $170 GEX wall [STRUCT:gex].
  - Short 175C strike caps premium outlay at the historical
    25-day-out 175C-ask level [FLOW:options_flow_sweeps] and matches
    the phase-1 8/21 175P bid-side "synthetic-long" institutional
    breakeven of ~$143.60.
  - IV is in the **11th percentile, regime LOW_IV** with VRP -2.6%
    FAIR [HIST:iv_percentile_zscore, HIST:vrp] — debit structures
    have better edge than credits here.
  - Defined risk = consistent with TRANSITIONAL regime guidance
    [MACRO:MarketRegime_2026-05-18].

### Defined-risk alternative — 6/18 150/145 put credit spread

- **Structure:** Bull put credit vertical (short higher strike, long
  lower strike)
- **Strike(s) / expiry:** Short 1× **RDDT 2026-06-18 150P**, Long
  1× **RDDT 2026-06-18 145P**
- **Debit/credit:** Net **credit ~$1.50** per spread (short 150P
  ~$3.50, long 145P ~$2.00; calibrated to phase-1 [FLOW:options_flow_sweeps]
  6/18 140P ask @ $4.20 and phase-3 [OI:smart_positioning] 6/18 95P
  bid-side @ $0.10 — interpolating with 6/18 IV 66% from
  [STRUCT:iv_term_structure])
- **Breakeven:** $150 − $1.50 = **$148.50** at 6/18 expiration
- **Max gain:** $1.50 × 100 = **$150 per spread**
- **Max loss:** ($150 − $145) − $1.50 = **$3.50 × 100 = $350 per
  spread**
- **Payoff ratio:** 0.43 : 1 (gain : loss) — credit spread; max win
  small, max loss bigger, but probability of profit ~75% if RDDT
  holds > $148.50
- **Sizing:** 2.5% of book risk ÷ $350 per spread = number of spreads
- **Why this structure:**
  - Strikes sit **inside the phase-4 short-gamma hole** ($150 = -$77M
    GEX, $145 = -$32M GEX [STRUCT:gex]) — short put is at the
    "resistance wall" in structural-flip terms; spot would have to
    break BOTH the $154 DP shelf AND the $150 gamma cliff to put
    short leg ITM.
  - 6/18 IV at 66% is **richer than the 7/17 IV at 63.5%**
    [STRUCT:iv_term_structure] (mild kink at 6/18 monthly opex from
    OPEX positioning) — gets paid slightly more in vol than a 7/17
    short put would.
  - Alternative income-style expression of the same bull thesis,
    appropriate when the directional debit feels too aggressive vs
    the TRANSITIONAL regime; pair with a tighter $151 stop on the
    underlying as the exit trigger.
  - Lower payoff ratio is acceptable because it's a hedged-alternative,
    not the primary expression.

## Macro overlay (cite phase-6)

**Tailwinds:**
- RDDT Q1 2026 beat: rev $663M +69% YoY, EBITDA margin 40%
  [MACRO:RDDT_Q1_2026-04-30]
- Shopify ecommerce integration ramping in March 2026 [MACRO:Shopify_2026-Q1]
- Needham $300 PT post-Q1 print (~89% implied upside) [MACRO:Needham_2026-04/05]
- SPY in 30D uptrend +3.5% [MACRO:MarketRegime_2026-05-18]
- April NFP beat +115K vs +55K consensus [MACRO:PAYEMS_2026-04]

**Headwinds:**
- Market regime **TRANSITIONAL** ("Reduce size, defined-risk")
  [MACRO:MarketRegime_2026-05-18]
- Comm Services net outflow **-$20.5M** on 2026-05-18
  [MACRO:MarketRegime_2026-05-18]
- Technology -$299.8M (sector spillover) [MACRO:MarketRegime_2026-05-18]
- Breadth bearish: 35.7% bullish-flow tickers
  [MACRO:MarketRegime_2026-05-18]
- April core CPI 2.8% YoY (sticky, above 2% target)
  [MACRO:CPILFESL_2026-04]
- Fed on hold at 3.50–3.75%, only 1 cut priced for 2026
  [MACRO:FOMC_2026-04-29]
- SPY MACD turning negative, highest-volume sell bar of the range on
  5/18 [MACRO:SPY_2026-05-18 WebSearch:tradingview.com]

**Net:** **net-headwind on regime/tape, net-tailwind on idiosyncratic
fundamentals.** This asymmetry is exactly why the trade is sized at
HALF Kelly cap (2.5%) and uses defined-risk structures rather than
naked long calls.

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|------|-------|------------------|
| 2026-05-22 (Fri) | Weekly OPEX + monthly OPEX; phase-4 $160 magnet operative | ? (pin most likely; consult [STRUCT:today_gamma_flip]) |
| 2026-05-28 (Thu) | FOMC April-29 minutes | ? (tape-driven) |
| Late May | April PCE release (typical last Friday) | ? (second look at inflation) |
| 2026-06-06 (Fri) | May NFP | systemic (?) |
| 2026-06-10 (Wed) | May CPI | systemic (?) |
| 2026-06-16/17 | **FOMC meeting + SEP/dot-plot** | **BINARY**; dovish surprise = + (tailwind for high-multiple growth); hawkish = − |
| 2026-06-18 (Thu) | Monthly OPEX (RDDT 6/18 chain) | structural; positions either pinned or unwound |
| ~late-July | **RDDT Q2 2026 earnings on 2026-07-30** [INSIGHT:deep_dive] | binary; 7/17 debit spread is INTENTIONALLY closed before this date |

## Post-trade monitoring checklist

- [ ] **Daily:** re-check phase-2 `dark_pool_block_stratified` for
      `block.buy_ratio` — invalidation if drops below 0.50.
- [ ] **Daily:** re-check phase-4 GEX regime label and ZGL —
      invalidation if regime stays NEGATIVE for 3 consecutive
      sessions with spot below 158.
- [ ] **Daily:** monitor sector flow via UW `risk_market_regime` —
      escalation trigger if Comm Services net flow < -$50M for 2 days.
- [ ] **End-of-day:** verify RDDT close vs $154 (primary stop level);
      execute HARD STOP if close < $154 for two consecutive sessions.
- [ ] **Weekly:** refresh `historical_signal_backtest(bullish_flow)`
      — if win rate stays at 0% for two more weeks, the trade-level
      conviction degrades and final size should be cut further.
- [ ] **Weekly:** check `insights_conviction_matrix` — if scenario
      flips from DIRECTIONAL_LONG to HEDGED_LONG, roll the debit
      spread into a bear structure or close.
- [ ] **Pre-6/17 FOMC:** preemptively cut size to 1.0% of book risk
      ahead of the binary; restore to 2.5% only on confirmed dovish
      print.
- [ ] **2026-07-25 (Mon):** preemptive close-or-roll of 7/17 debit
      spread before Q2 earnings IV pumps further. Do NOT carry into
      7/30.

## Citations summary (≥3 distinct upstream datapoints per M-04)

1. **[DP:block_stratified] — block-tier buy_ratio 0.793 on $26.26M
   premium, 14 trades, 2026-05-18** — phase-2-dark-pool.md §Tier
   breakdown.
2. **[STRUCT:gex] — total GEX +$1.261B, $160 strike +$622.7M (49%
   of chain), ZGL $158.39 vs spot $158.89** —
   phase-4-structure.md §GEX (DTE ≤ 45).
3. **[HIST:signal_backtest] — `bullish_flow` 5d backtest win rate
   0.0%, avg move -3.05%, n=7 across MSFT/AAPL/UPS/QQQ/SMH/META/AVGO**
   — phase-5-historical.md §Signal backtest (current regime).
4. **[MACRO:MarketRegime_2026-05-18] — UW regime TRANSITIONAL,
   breadth 35.7% bullish, Comm Services -$20.5M outflow, Tech
   -$299.8M outflow** — phase-6-macro.md §Market regime + §Sector
   rotation.
5. **[INSIGHT:conviction_matrix] — DIRECTIONAL_LONG scenario,
   confidence 22.25%, DP buy_ratio 0.642** —
   phase-7-insights.md §Conviction matrix.
6. **[AGENT:risk-monitor] — "Half size max (25-33% of normal),
   defined-risk only; cut on any close below 154"** —
   phase-8-agent-views.md §risk-monitor.
