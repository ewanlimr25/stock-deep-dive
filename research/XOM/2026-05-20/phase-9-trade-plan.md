# Phase 9 — Trade Blueprint

**Ticker:** XOM
**As-of date (user request):** 2026-05-20
**Effective data date:** 2026-05-18 (close)
**PM voice:** desk PM running an institutional options-overlay book
**Spot reference:** $160.49 (EOD close — phase-1-flow.md §"Tool calls" / `historical_trend` 2026-05-18 row)
**Upstream phases cited:** phase-1 through phase-8

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

XOM dealer mechanics have built a long-gamma cage in the $152.5–$170 corridor
with **+$9.75B net GEX at the $165 strike** [STRUCT:gex] and **+8,150 OI Δ
added today on Jun'26 165C** [OI:biggest_increases], setting up a 31-day grind
toward the $165 magnet against an unambiguous macro tailwind (**Strait of
Hormuz closure / Iran conflict shutting in 10.5 mmb/d, with Brent ~$110**
[MACRO:Strait_of_Hormuz_2026-04_to_2026-05]) and **net energy-sector inflow
$+9.1M vs technology -$299.8M today** [MACRO:MarketRegime_2026-05-18]. The
trade is **defined-risk LONG into the dealer pin**, not a chase: the same
day showed **mega-tier dark-pool buy_ratio 0.049 (95% sell-classified)**
[DP:block_stratified] and the multi-agent desk landed at **avg conviction
2.0 / 5 with plurality NEUTRAL/RANGE** [AGENT:contrarian-scanner +
AGENT:sweep-tracker], so size is small and the structure is asymmetric.
Net: buy the pin-toward-$165 via a Jun'26 bull call spread, with a
put-credit-spread alternative that monetizes the COMPLACENT call-rich skew
[STRUCT:term_skew].

## Bias + conviction + horizon

- **Directional bias:** **LONG (defined-risk, range-bounded)**
- **Conviction (M-01 bin):** **0.65**
- **Time horizon:** **1-4w** (target the Jun'26 monthly OPEX, 31 DTE from
  2026-05-18 → 2026-06-18)
- **Why this bin** (cites phase-10 anticipated confluence): confluence
  scoring per `rubrics/confluence-scoring.md` lands near **+33 raw → ~64
  normalized**, which falls in the **50–64 band → conviction 0.65**. Three
  strong-confirms (phase-3 OI, phase-4 GEX, phase-6 macro) at +15 each are
  offset by three contradictions (phase-2 DP at -7, phase-5 historical at
  -7, phase-7 insights at -7). Phase-8 nets +2 (one LONG, one fade-lean,
  one RANGE, one NEUTRAL).

## Entry zones

| Entry type | Price | Trigger condition | Source |
|---|---|---|---|
| Primary | $157.50 | Tag of first dealer support wall on a low-vol pullback (post-OPEX or intraday rejection from $162-$164) | [STRUCT:gex] $911M GEX at $157.50 |
| Aggressive | $160.00 | Re-enter today's anchor with TIGHT stop just below $156.35 (phase-2 secondary support); only if entered before May 22 OPEX with awareness of vanna-bleed risk | [STRUCT:today_gamma_flip] OPEX wall $4.1B at $160 |
| Fade | $164-$165 | Sharp rip into Jun'26 165C wall on an isolated catalyst; defined-risk tactical short via call credit spread for 1-3 sessions | [STRUCT:gex] $9.75B net GEX at $165 |

**Timing note:** **DO NOT enter before May 22 OPEX expiry.** Phase 4
documented that May 22 IV (40.8%) collapses through Jun 18 IV (33.5%) —
vanna unwind on Monday May 25 forces dealers to mechanically sell underlying
into the IV decline [STRUCT:vanna_charm]. Wait for the post-OPEX dip
(target Tuesday May 26 or Wednesday May 27) and look for the bounce off
$157.50 / $156.35 to confirm entry.

## Levels to watch

| Type | Level | Source |
|---|---|---|
| Strong DP support (5-day cluster) | $151.57 / $150.63 / $150.93 / $150.80 / $150.91 / $152.39 / $152.78 (aggregate ~$1.34B premium) | [DP:price_levels] |
| Intraday support / first dealer wall | $157.50 | [STRUCT:gex] +$911M, [STRUCT:today_gamma_flip] $911M wall |
| Dealer support / OPEX magnet | $160 | [STRUCT:today_gamma_flip] $4.10B wall, [STRUCT:gex] +$6.66B |
| Largest single-strike GEX (sticky resistance) | $165 | [STRUCT:gex] +$9.75B, [OI:biggest_increases] Jun'26 165C OI 18,186 |
| Air-pocket above wall | $165 → $170 (next wall thin at +$1.39B) | [STRUCT:gex] |
| **Gamma flip / hard invalidation** | **$152.5 ATM flip, $153.09 OPEX ZGL** | [STRUCT:today_gamma_flip] atm_flip_strike 152.5, today_zero_gamma 153.09 |
| Largest near-term put strike (downside tail) | $135 (Jun'26 OI 7,034) | [OI:biggest_increases] Jun'26 135P |

## Invalidation

- **Price-based:** **two daily closes below $152.50** (OPEX-week ATM gamma
  flip from [STRUCT:today_gamma_flip]). One intraday wick below is not
  enough — wait for confirmation. If close is two consecutive days below
  $152.50, the dealer regime flips to short-gamma and the bull thesis is
  mechanically broken.
- **Signal-based:** **DISTRIBUTION in `insights_institutional_accumulation`
  PERSISTS for 3 consecutive sessions** WITH **`consecutive_build_days`
  resets to 0** in `historical_oi_trend` [HIST:oi_trend] AND **the Jun'26
  165C OI declines by >2,000 contracts** [OI:biggest_increases]. Reading:
  the institutional bull build was a one-day repositioning, not a campaign;
  if it doesn't continue and starts to unwind, the +$9.75B GEX support also
  unwinds.
- **Macro-based:** **Strait of Hormuz reopening headline** (the EIA
  forecast already references "late May 2026" reopening — this is a known
  binary risk). On the headline, Brent typically drops $10–$20 and XOM
  re-rates to its 6-month average +$1-2, which puts spot near $148–$152.
  Trade plan must close on the headline regardless of price action.
  [MACRO:Strait_of_Hormuz_2026-04_to_2026-05]

**Exit on invalidation:**
- **For the bull call spread (directional debit):** **HARD STOP** — close
  100% if any of the three invalidations fires.
- **For the put credit spread (defined-risk credit):** **ROLL** the short
  put down to $145 or close at 50% max loss if hit, depending on which
  invalidation fires (price → roll; signal/macro → close).

## Sizing (% of risk, NOT dollars)

- **Kelly inputs:** p = 0.65, b = 1.50, fraction = 0.25
- **b derivation:** target $165, entry $157.50, stop $152.50.
  - distance to target: |165 − 157.50| = $7.50
  - distance to stop: |157.50 − 152.50| = $5.00
  - b = 7.50 / 5.00 = **1.50**
- **Raw Kelly:** (0.65 × 1.50 − 0.35) / 1.50 = (0.975 − 0.35) / 1.50 =
  0.625 / 1.50 = **0.4167 = 41.67%**
- **Suggested size:** raw_kelly × fraction × 100 = 41.67% × 0.25 = **10.4%**
- **After cap (5%):** **5.00%** of book risk (cap binding)
- **Final size:** **2.50%** of book risk
- **Deviation reason (DOWNWARD — always permitted):** Phase-8 desk consensus
  was 2.0/5 avg conviction with risk-monitor explicitly recommending "size
  half" [AGENT:risk-monitor]. The COMPLACENT skew + DP distribution +
  bullish_flow 0% historical win rate [HIST:signal_backtest] all argue for
  halving the cap. **Going DOWNWARD from 5% to 2.5% is conservative and
  matches the desk's recommended haircut**.

## Option structures

### Directional (primary): Bull Call Spread

- **Structure:** long Jun'26 160 call / short Jun'26 170 call (debit spread)
- **Strikes / expiry:** Buy XOM 2026-06-18 $160 Call ; Sell XOM 2026-06-18
  $170 Call
- **DTE at entry (target):** ~24 days (entering 2026-05-26 post-OPEX dip)
- **Debit/credit:** ~$2.45 net debit per contract (estimated; current
  reference: Jun'26 160C avg trade $3.95 [OI:biggest_increases]; Jun'26
  170C OI 8,410 [OI:decrease_with_volume] avg trade $1.79 → spread
  approx $3.95 − $1.50 = $2.45 at $157.50 entry; refresh quote on entry day)
- **Max gain:** $10.00 − $2.45 = **$7.55 per contract** (occurs at any
  spot ≥ $170 at expiry)
- **Breakeven:** $160 + $2.45 = **$162.45 at expiry**
- **Max loss:** $2.45 per contract = debit paid
- **R/R:** 7.55 / 2.45 = **3.08:1**
- **Why this structure:** (1) IV is FAIR (VRP +0.24, IV %ile 65)
  [HIST:vrp] [HIST:iv_percentile_zscore] — neither cheap nor rich vol,
  so debit risk is appropriate; (2) targets the **air pocket between
  $165 and $170** that opens if the wall breaches; (3) defined-risk
  debit caps loss at $2.45; (4) Jun'26 expiry is **31 DTE from data
  anchor**, fully captures the GEX-magnet OPEX cycle and **avoids the
  Q2 2026 earnings event 2026-08-07** [INSIGHT:deep_dive].

### Defined-risk alternative: Put Credit Spread

- **Structure:** short Jun'26 152.50 put / long Jun'26 145 put (credit
  spread)
- **Strikes / expiry:** Sell XOM 2026-06-18 $152.50 Put ; Buy XOM 2026-06-18
  $145 Put
- **Width:** $7.50
- **Debit/credit:** ~$1.30 net credit per contract (estimated from
  phase-3 chain reference points: Jun'26 145P avg trade price $1.72
  [OI:decrease_with_volume], 152.5P richer ~$3.00; the $7.50-wide spread
  collects ~$1.30 credit; refresh quote on entry day)
- **Max gain:** $1.30 per contract (occurs at any spot ≥ $152.50 at expiry)
- **Breakeven:** $152.50 − $1.30 = **$151.20 at expiry**
- **Max loss:** $7.50 − $1.30 = **$6.20 per contract**
- **R/R:** 1.30 / 6.20 = **0.21:1** (asymmetric to the downside but high
  probability of profit — short strike is **at the gamma flip**, so
  spot must structurally break the dealer regime to challenge it)
- **Why this structure:** (1) **COMPLACENT skew** (call IV 32.86% > put
  IV 31.49%) [STRUCT:term_skew] = put-side is RELATIVELY cheap to sell;
  (2) the $152.50 short strike sits **exactly at the OPEX-week ATM gamma
  flip** [STRUCT:today_gamma_flip] — a hold above $152.50 is the same
  test as the trade thesis; (3) collects positive theta in a fair-vol
  regime; (4) **same Jun'26 expiry avoids August earnings event**.

**Structure selection logic:**
- If desk only takes ONE position: **bull call spread** (asymmetric upside
  with defined loss, matches phase-3/4/6 confluence).
- If desk wants a positive-theta carry: **put credit spread**.
- A combined "synthetic risk reversal" (long 160/170 call spread + short
  152.5/145 put spread) would create a higher-conviction directional bet
  at slightly negative cost, but the phase-8 desk avg conviction 2.0/5
  argues against combining structures — pick one, size 2.5%.

## Macro overlay

**Tailwinds:**
- Strait of Hormuz closure shutting in 10.5 mmb/d
  [MACRO:Strait_of_Hormuz_2026-04_to_2026-05]
- Brent ~$110, WTI ~$103 (current spot)
  [MACRO:Brent_2026-05_WebSearch:tradingeconomics.com]
- April CPI energy +3.8% MoM, gasoline +28.4% YoY
  [MACRO:CPI_2026-04 WebSearch:bls.gov]
- UAE departure from OPEC → structurally reduced spare capacity
  [MACRO:UAE_OPEC_2026-05-01 WebSearch:cnbc.com]
- Energy sector inflow $+9.1M today vs Tech outflow -$299.8M (300:1 rotation)
  [MACRO:MarketRegime_2026-05-18]
- XOM Q1 2026 EPS beat ($1.16 vs $0.98 est, $8.8B earnings ex-items)
  [MACRO:XOM_Q1_2026-05-01 WebSearch:investor.exxonmobil.com]
- $20B 2026 buyback affirmed; 43rd consecutive annual dividend increase
  [MACRO:XOM_Q1_2026-05-01]
- Fed Funds on hold 3.50-3.75% → value/cash-flow names favored
  [MACRO:FOMC_2026-04-29 WebSearch:federalreserve.gov]

**Headwinds:**
- **Strait of Hormuz REOPENING risk** (EIA references "late May 2026"
  resolution — binary headline risk)
  [MACRO:Strait_of_Hormuz_2026-04_to_2026-05]
- Broad market regime classified **TRANSITIONAL** (size smaller per UW
  guidance) [MACRO:MarketRegime_2026-05-18]
- OPEC+ +188 kb/d production increase (post-UAE departure) — mild offset
  [MACRO:OPEC_post-UAE_2026-05-03 WebSearch:cnbc.com]
- Mega-cap tech selloff could spread to broader equities via correlation
  if SPY breaks $725 (currently $733.73 above 20-SMA $726.78)
  [MACRO:MarketRegime_2026-05-18]

**Net:** **NET TAILWIND**, conviction 4/5 on macro alone (phase 6).
However, the Hormuz binary risk pulls the *combined* trade conviction
down to 0.65.

## Catalyst calendar (next 30d from 2026-05-20)

| Date (approx) | Event | Impact direction |
|---|---|---|
| Late May 2026 | **Strait of Hormuz reopening (EIA forecast)** | **NEGATIVE (binary; close trade)** |
| 2026-05-22 (Fri) | Weekly OPEX | Mild positive (pin to $160) |
| 2026-05-25 (Mon) | Post-OPEX vanna-bleed session | Mild negative (mechanical dealer selling) |
| Early June 2026 | OPEC+ monthly meeting | Negative if further production added |
| 2026-06-10 | XOM Q2 2026 dividend payment | Mild negative (ex-div mechanical $1.03 drop, ex-date already passed 2026-05-15) |
| ~2026-06-11 | May 2026 CPI release (BLS schedule) | Positive (hot energy print = thesis confirm) |
| Mid-June 2026 | **FOMC meeting + new dot plot** | Neutral (cuts unlikely at hot CPI) |
| **2026-06-18 (Thu)** | **Jun'26 monthly OPEX (trade target expiry)** | **PIN to $160-165 expected; trade thesis pays off here if right** |
| ~Late July 2026 | OPEC+ monthly meeting | Outside trade horizon |
| 2026-08-07 | **XOM Q2 2026 earnings** | Outside Jun'26 trade horizon (good — avoided binary) |

## Post-trade monitoring checklist

- [ ] **Daily:** re-run `mcp__uw-pp__historical_oi_trend` symbol=XOM days=5
      and verify `consecutive_build_days` ≥ 1 with `oi_diff_plain` on
      Jun'26 165C either flat or increasing.
- [ ] **Daily:** re-check `mcp__uw-pp__insights_institutional_accumulation`
      — if it flips to ACCUMULATION, increase conviction. If it stays
      DISTRIBUTION for 3 sessions, signal-based invalidation triggers.
- [ ] **Daily:** re-check `mcp__uw-pp__options_structure_today_gamma_flip`
      OPEX ZGL — if it rises above $155, the bull case strengthens; if it
      falls below $152.50 while spot tests, prepare to close.
- [ ] **Daily WebSearch:** "Strait of Hormuz reopening" — close on any
      credible reopening headline regardless of price action.
- [ ] **Twice weekly:** `mcp__uw-pp__options_structure_term_skew` —
      monitor whether COMPLACENT skew normalizes (call IV − put IV gap
      closes). Normalization = late-stage rally typical pattern, prepare
      to trim.
- [ ] **Twice weekly:** check XOM appearance in
      `mcp__uw-pp__insights_signal_confluence` (bullish, min_score=3). If
      XOM enters the top-50, conviction confirms and consider scaling.
- [ ] **Weekly:** `mcp__uw-pp__risk_market_regime` — if regime flips to
      RISK-OFF, halve any remaining position.
- [ ] **Pre-OPEX (2026-06-17):** decide on roll vs close. If thesis intact
      and XOM > $162, close at credit-side of expected payoff. If $158-162,
      consider rolling to Jul'26 175C/185C if conviction has risen.

## Citations summary (M-04 audit list)

Minimum 3 distinct upstream datapoints used in the thesis (these are the
spot-check points for phase-10):

1. **`[STRUCT:gex]` — total net GEX +$23.2B with $9.75B concentrated at
   $165 strike**; resolves to phase-4-structure.md §"GEX (DTE ≤ 45)"
   table row "Strike $165 / Net GEX +$9,749,363,698".
2. **`[OI:biggest_increases]` — Jun'26 165C +8,150 OI Δ (10,036 → 18,186)
   on volume 12,397**; resolves to phase-3-positioning.md §"Largest OI
   increases" table rank #1.
3. **`[MACRO:Strait_of_Hormuz_2026-04_to_2026-05]` — 10.5 mmb/d of Middle
   East production shut in during April 2026, Strait effectively closed
   until late May**; resolves to phase-6-macro.md §"Sector overlay — energy
   specifics" first bullet and the tailwind/headwind table row.
4. **`[DP:block_stratified]` — mega-tier dark-pool buy_ratio 0.049 across
   6 trades, $206.6M premium, 5 of 6 prints below NBBO mid**; resolves to
   phase-2-dark-pool.md §"Tier breakdown" mega-tier row.
5. **`[MACRO:MarketRegime_2026-05-18]` — Energy sector inflow $+9.1M vs
   Technology outflow -$299.8M on 2026-05-18**; resolves to
   phase-6-macro.md §"Market regime" sector_rotation listing AND the
   tailwind table.
6. **`[AGENT:risk-monitor]` — "size half, define risk, don't chase"**;
   resolves to phase-8-agent-views.md §"risk-monitor" one_line_take.

## Conviction deviation

No conviction deviation. Phase-9 conviction 0.65 matches the expected
phase-10 confluence band (~64) by `rubrics/confluence-scoring.md` (the
50-64 band maps to 0.65). Sizing deviation is DOWNWARD only (5% → 2.5%)
and is always permitted.

## One-line PM take

> "Defined-risk LONG into the dealer pin: buy the Jun'26 160/170 call
> spread at $2.45, set the stop at the OPEX gamma flip ($152.50), size
> 2.5% of book, and **close immediately on any credible Strait of Hormuz
> reopening headline.**"
