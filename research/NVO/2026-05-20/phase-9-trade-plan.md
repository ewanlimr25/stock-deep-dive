# Phase 9 — Trade Blueprint

**Ticker:** NVO (Novo Nordisk ADR, NYSE)
**As-of date:** 2026-05-20
**PM voice:** desk PM running an institutional options-overlay book
**Spot reference:** $45.07 (phase-2 mega DP print level; close)
**Upstream phases cited:** phase-1 through phase-8

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

A real institutional buyer stepped in on NVO today: a $1.0M ask-side LEAP
sweep on the Jan 2028 $45 calls (30 trades, δ 0.62) with the matched put
sold on the bid [FLOW:sweeps], a $26.94M dark-pool mega-print at $45.07
with mega-tier buy_ratio 1.0 [DP:largest, DP:block_stratified], and the
biggest single-day gamma regime reset in the trailing 29 sessions — ZGL
dropped −$17.30 to flip back into POSITIVE gamma [HIST:gex_time_series]
— all on the day a 5-session bearish-sweep streak finally broke. Three
of four sub-agents return LONG with the same support ($44.15),
invalidation ($44 close), and an extension target stack at $45.80 → $50
[AGENT:accumulation-hunter, AGENT:sweep-tracker]. With IV30 in the 7th
percentile, complacent skew, and management's Q1 guidance raise on the
Wegovy-pill surprise [MACRO:NVO_Q1_2026], the right trade is to **buy
cheap upside convexity sized to the structural $50 target, with a hard
stop at $44 to respect the contrarian's complacency caveat and the LLY
Medicare Bridge competitive cliff on July 1**.

## Bias + conviction + horizon

- **Directional bias:** LONG
- **Conviction (M-01 bin):** **0.85**
- **Time horizon:** 1-4w (with optional LEAP follow-on tranche on confirmation)
- **Why this bin (confluence-driven):** phase-10 preview score ≈ 87
  (rubric band 80–89 → 0.85). Phases 1, 2, 4, 5 all "++"; phases 3, 6, 7
  "+"; phase 8 = 3-of-4 LONG aligned. Single material caveat: NVO missing
  from bullish_confluence top 50 (phase-7) → confluence is at the lower
  end of the 0.85 band, not the upper end.

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|------:|-------------------|--------|
| **Primary** | **$45.10 – $45.25** | Hold-and-go above today's $45.07 pivot; intraday close ≥ $45.10 confirms the LEAP buyer's level is now support | [DP:largest] post-close $26.94M @ $45.07; [STRUCT:gex] $45 strike +$776M positive wall |
| **Aggressive** | **$44.40 – $44.70** | Tag of pre-market accumulation zone OR retest of $44.65/$44.68 5-day DP clusters with stable tape | [DP:price_levels] 5-day $44.65 = $5.54M / 124k shares; $44.68 = $4.60M / 103k shares |
| **Fade (Plan B)** | **rejection at $45.80 with >1.5× volume** | If price tags $45.80 institutional ceiling and reverses on volume, take a small mean-revert short to $44.50 | [DP:price_levels] $45.80 = $36.95M / 807k shares = 5-day buyer ceiling |

## Levels to watch

| Type | Level | Source |
|------|------:|--------|
| **Support (hard)** | **$44.15** | [DP:price_levels] 5-day cluster $25.75M / 583k / only 2 trades (block-defended) |
| Support (soft) | $44.65 – $44.73 | [DP:price_levels] secondary daily DP clusters |
| **Pivot** | **$45.07** | [DP:largest] today's mega-print; also Jan 2028 $45 LEAP synthetic anchor |
| Resistance 1 | **$45.80** | [DP:price_levels] institutional 5-day ceiling, $36.95M |
| **Resistance 2 / structural** | **$50.00** | [STRUCT:gex] +$825M call wall; [OI:biggest_increases] June $50C OI = 32,113 |
| Gamma flip (chain-wide) | $27.44 (ZGL) | [STRUCT:gex] — far below spot, irrelevant for active trading |
| Local short-γ trap | **$44 → $40** | [STRUCT:gex] $44 = −$93M, $40 = −$107M (regime change zone if breached) |
| Pin risk this week | n/a | [OI:pin_risk] — NVO not in 7-DTE OPEX window |

## Invalidation

- **Price-based:** Two consecutive daily closes below **$44.00**, OR a single intraday print below **$43.50** without immediate reclaim by close. Reason: $44 is the boundary between phase-4's POSITIVE gamma regime and the $-93M short-gamma pocket; losing $44 unrolls the supporting dealer hedge and opens a path toward the $40 −$107M trap-door [STRUCT:gex, STRUCT:today_gamma_flip].
- **Signal-based:** Any ONE of (a) DEX flips from +$6.22B to net-short on phase-4 daily refresh; (b) UW conviction matrix flips from `DIRECTIONAL_LONG` to `HEDGED_LONG` or `MIXED` [INSIGHT:conviction_matrix]; (c) `historical_cumulative_premium_flow` 3-day net flow turns ≤ −$5M [HIST:cumulative_premium_flow]; (d) institutional_accumulation tag flips from ACCUMULATION to DISTRIBUTION [INSIGHT:institutional_accumulation].
- **Macro-based:** (a) FOMC June 16–17 SEP/dot-plot revises 2026 median dot **higher** by ≥25bp vs current path [MACRO:FOMC_2026-04-29]; (b) July 1 LLY Medicare Bridge launches with **NVO explicitly excluded** AND no NVO Medicare counter-deal announced by July 15 [MACRO:Medicare_GLP1_Bridge]; (c) UW risk_market_regime flips from TRANSITIONAL into RISK-OFF [MACRO:MarketRegime_2026-05-20].

**Exit on invalidation:** **Hard stop** on debit structures (close 100% if price-based fires); **roll/close** on credit structures. On the signal-based or macro-based fire, **close 50% immediately and re-evaluate the remaining 50% within one session**.

## Sizing (% of risk, NOT dollars)

Using the structural $50 target (the dominant payoff path):
- entry = $45.20 (midpoint of primary entry zone)
- target T2 = $50.00
- stop = $43.95 (just below $44 invalidation)
- b = (50.00 − 45.20) / (45.20 − 43.95) = **4.80 / 1.25 = 3.84**

- **Kelly inputs:** p = **0.85**, b = **3.84**, fraction = 0.25
- **Raw Kelly:** (0.85 × 3.84 − 0.15) / 3.84 = (3.264 − 0.15) / 3.84 = 3.114 / 3.84 = **0.811 = 81.1%**
- **Fractional:** 0.811 × 0.25 = **20.3%**
- **Capped:** min(20.3%, **5%**) = **5.00%**
- **Final size:** **5.00% of book risk** (capped — the structural Kelly far exceeds the hard ceiling)
- **Deviation reason:** none; sizing is AT the cap, not above it. The cap is binding because the asymmetry is large and conviction is high, but the rubric's 5% hard ceiling governs.

For T1 ($45.80) the b≈0.48, raw_kelly ≈ 0.54, fractional 13.5%, also capped at 5%. **Both paths size to the cap.**

## Option structures

### Directional (primary) — Long Call

- **Structure:** Long 1× NVO 2026-07-17 **$45 Call**
- **Strike / expiry:** $45 strike, 2026-07-17 (58 DTE)
- **Debit (estimated from today's tape):** **$2.90** per contract ([FLOW:sweeps] 7/17 $45C avg fill = $2.93)
- **Breakeven:** $45.00 + $2.90 = **$47.90**
- **Max loss:** **$290** per contract (if NVO < $45 at 7/17 expiry)
- **Profit at T1 $45.80:** ~+$0 (option still mostly extrinsic; capture via T2 path)
- **Profit at T2 $50.00:** intrinsic = $5.00, less debit $2.90 = **+$210/contract (+72%)**
- **Why this structure:** IV30 is in the 7th percentile [HIST:iv_percentile_zscore], so paying premium is carry-favorable. 58 DTE spans the **July 1 LLY Medicare Bridge** event ([MACRO:Medicare_GLP1_Bridge]) and finishes before the August 5 NVO Q2 ER [INSIGHT:deep_dive], so no earnings IV crush is embedded. Delta ~0.55 → directly tracks the structural move to $50.

**Sizing note:** Premium spent per contract = $290. To size to 5% of book
risk: contracts = (book risk × 0.05) / $290. (Book size left to the
operator since this skill has no account context per
[rubrics/sizing-rubric.md].)

### Defined-risk alternative — Call Debit Spread

- **Structure:** Long NVO 2026-07-17 **$45 / $50 Call Debit Spread**
- **Strikes / expiry:** Buy 1× $45C @ ~$2.90 / Sell 1× $50C @ ~$0.70
- **Net debit:** **$2.20** per spread
- **Breakeven:** $45.00 + $2.20 = **$47.20**
- **Max profit at $50:** $5.00 − $2.20 = **+$280/contract (+127%)**
- **Max loss:** **$220** per contract (24% less premium than naked long)
- **Why this structure:** Caps upside at the $50 [STRUCT:gex] +$825M call wall — the structural ceiling the data identifies anyway. Better risk-adjusted return than the naked long (R:R 1.27 vs 0.72) at the cost of forgoing any tail to $55+. Preferred sizing vehicle when book risk is the binding constraint or when the operator wants a tighter loss tail.

## Macro overlay (cite phase-6)

**Tailwinds:**
- NVO Q1 2026 ER beat + raised 2026 guidance (Wegovy pill 1.3M Q1 scripts ≈ 2× consensus) [MACRO:NVO_Q1_2026]
- Wegovy pill 80% GLP-1-naive users → market expansion, not cannibalization [MACRO:NVO_Q1_2026]
- Wegovy HD approvals (~21% weight loss) [MACRO:NVO_Q1_2026]
- Fed retains easing bias despite 3 hawkish dissents → asymmetric rate risk skewed dovish [MACRO:FOMC_2026-04-29]
- SPY +5.28% 30d in UPTREND despite TRANSITIONAL regime label [MACRO:MarketRegime_2026-05-20]

**Headwinds:**
- LLY Medicare GLP-1 Bridge live 7/1/2026 — NVO not in package (the principal medium-term risk) [MACRO:Medicare_GLP1_Bridge]
- April CPI +3.8% YoY (hottest since May 2023) [MACRO:CPIAUCSL_2026-04]
- Market breadth weak: 39.5% bullish tickers [MACRO:MarketRegime_2026-05-20]
- Sector rotation neutral for Healthcare (not in flow-in or flow-out buckets) [MACRO:SectorRotation_2026-05-20]
- LLY oral pill 2Q 2026 launch (competitive entrant) [MACRO:GLP1_market_2026]

**Net:** mildly positive (tailwind) on company-specific Q1 + product
momentum, partially offset by the known LLY Medicare-Bridge competitive
cliff at +6 weeks.

## Catalyst calendar (next 30d)

| Date | Event | Source | Impact direction |
|------|-------|--------|------------------|
| 2026-05-22 (Fri) | Weekly OPEX (5/22 NVO 0DTE) | [STRUCT:iv_term_structure] | Neutral / mild ($50 gamma intact next week) |
| 2026-05-29 (Fri) | Weekly OPEX (5/29) | [OI:biggest_increases] | Neutral (700-contract $45C bid-side OI build today expires) |
| 2026-06-13 (Sat est) | May 2026 CPI release (estimated) | [MACRO:CPIAUCSL_2026-04] precedent | If ≥ +0.5% MoM = hawkish (−); ≤ +0.3% = dovish (+) |
| **2026-06-16–17 (Tue/Wed)** | **FOMC + SEP/dot plot** | [MACRO:FOMC_2026-04-29] | **MATERIAL — re-rate event for sector multiples** |
| **2026-06-18 (Thu)** | **June 2026 OPEX (NVO)** | [OI:biggest_increases] | $50C wall (32k OI), $45C (23k OI), $42.5P (1.1k OI) all roll off |

(The 7/1 LLY Medicare go-live is just outside the 30-day window but is
the dominant catalyst within the trade horizon — it has been flagged in
invalidation.)

## Post-trade monitoring checklist

- [ ] **Daily:** Re-check phase-2 dark pool prints — look for continued buy-side accumulation at $45.07 / $45.80 OR a flip to distribution.
- [ ] **Daily:** Re-check phase-4 DEX sign; we need DEX to remain net dealer-buy. A flip is one of the named signal invalidations.
- [ ] **Daily:** Re-check phase-1 sweep tape — does the LEAP buyer's footprint persist or expand? Look specifically at 2028-01 $45 strike OI for follow-on adds.
- [ ] **Daily:** Watch the $44.00 line. Any intraday print below $43.50 → flag the desk; two consecutive closes below $44 → close 100%.
- [ ] **Weekly:** Re-check phase-7 conviction matrix and institutional_accumulation tags — both must remain in `DIRECTIONAL_LONG` and `ACCUMULATION`.
- [ ] **Weekly:** Re-check phase-5 IV percentile — IV expansion to >25th percentile is fine (vanna tailwind kicks in); IV crush to <3rd percentile + price stall = take profits early.
- [ ] **Event-day:** Pre-FOMC 6/16, halve the position into the print regardless of bias (TRANSITIONAL macro regime → no naked long through binary macro events).
- [ ] **Event-day:** Monitor LLY Medicare Bridge launch coverage 7/1/2026 — if NVO announces own deal within 30 days, conviction upgrade; if explicitly excluded > 30d, downgrade.

## Citations summary (≥3 distinct upstream datapoints)

1. **[FLOW:sweeps]** — $1,007,176 ask-side sweep on NVO 2028-01-21 $45C, 30 trades, avg fill $10.64, δ 0.62 (phase-1-flow.md §Sweeps).
2. **[DP:largest]** — $26,943,297 mega print at $45.07, 597,810 shares, NBBO mid (phase-2-dark-pool.md §Largest individual blocks).
3. **[DP:block_stratified]** — Mega-tier buy_ratio 1.000; block-tier 0.893 (phase-2-dark-pool.md §Tier breakdown).
4. **[STRUCT:gex]** — Total GEX +$2,099,855,377; $45 strike +$776,572,748; $50 strike +$825,040,572 (phase-4-structure.md §GEX).
5. **[HIST:gex_time_series]** — Today's ZGL drop = −$17.30 (from $44.74 to $27.44) — biggest 1-day shift in the 29-session series; April 28 analog ran +8% in 5d (phase-5-historical.md §GEX time series).
6. **[HIST:iv_percentile_zscore]** — IV percentile 7.14, z-score −1.36 (phase-5-historical.md §IV regime).
7. **[INSIGHT:conviction_matrix]** — DIRECTIONAL_LONG, DP buy_ratio 0.687 (phase-7-insights.md §Conviction matrix).
8. **[MACRO:NVO_Q1_2026]** — Wegovy pill 1.3M Q1 scripts, DKK 2.26B revenue (~2× consensus); 2026 guidance raised (phase-6-macro.md §Sector overlay).
9. **[MACRO:Medicare_GLP1_Bridge]** — LLY Zepbound live 2026-07-01; NVO not in package (phase-6-macro.md §Sector overlay).
10. **[AGENT:accumulation-hunter, AGENT:sweep-tracker, AGENT:risk-monitor]** — 3-of-4 LONG verdicts; universal $44.15 support / $44 invalidation (phase-8-agent-views.md §Agent verdicts table).
