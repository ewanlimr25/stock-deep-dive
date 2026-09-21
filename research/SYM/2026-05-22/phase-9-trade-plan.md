# Phase 9 — Trade Blueprint

**Ticker:** SYM (Symbotic Inc., NASDAQ, Industrials)
**As-of date:** 2026-05-21 (effective; user requested 2026-05-22, no
data available — see phase-0-intake.md)
**PM voice:** desk PM running an institutional book
**Spot reference:** $50.50 (mid of 2026-05-21 dark-pool VWAP $50.47 +
NBBO close $50.95) — sources phase-2-dark-pool.md §Largest blocks,
phase-7-insights.md §Deep dive snapshot
**Upstream phases cited:** phase-1 through phase-8

> *For research and educational use only. Not financial advice. Sizing
> and structures are illustrative.*

## Thesis (≤3 sentences)

SYM is a post-event reset with **mid-tier institutional accumulation**
(dark-pool buy_ratio **0.672**, vwap $50.47, $4.04M multi-day base at
$46.40-$47.40 [DP:price_levels]) overlaid on a **fresh POSITIVE-GEX
regime that flipped today** ($51-$52 call wall $10.31M, today_ZGL
$44.53, 1-day-old regime flip from NEGATIVE
[STRUCT:gex, HIST:gex_time_series]). With **IV at the 10.34th
percentile** of the trailing 1y window [HIST:iv_percentile_zscore] and
4 agents converging on a $49.50–$52 range
([AGENT:accumulation-hunter], [AGENT:contrarian-scanner],
[AGENT:sweep-tracker], [AGENT:risk-monitor]), the high-probability
trade is a **defined-risk LONG into the $52 call wall on cheap
premium**, sized half because macro is a headwind (CPI 3.8% YoY
re-accelerating, Industrials sector outflow $-27M today)
[MACRO:CPI_2026-04 WebSearch:cnbc.com, MACRO:SectorRotation_2026-05-21 UW].

## Bias + conviction + horizon

- **Directional bias:** **LONG with a RANGE-respecting structure**
  (plurality of phases 1-8 is range-bound mild-long).
- **Conviction (M-01 bin):** **0.65** (moderate edge).
- **Time horizon:** **1-4 weeks** (matches majority agent horizon;
  expiry pushed past the June catalyst window for the directional
  structure).
- **Why this bin:** Phase-10 will compute a confluence score that
  lands in the 50-64 band (see anticipated breakdown in phase-10's
  audit). 0.65 captures "more likely than not, with real
  disconfirming evidence" — the bearish phase-1 LEAP-call premium
  signal and the macro headwinds prevent moving up to 0.75.

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| **Primary** | **$49.50–$50.00** | Pullback into the dealer-hedge boundary that all 4 agents flagged. Buy the *tag* of $49.50, NOT the break of it. | [STRUCT:gex] $49.5 wall +$340K GEX, [DP:price_levels] $49.96 shelf $2.02M |
| **Aggressive** | **$49.96–$50.20** | Intraday VWAP fade into the fresh same-week dark-pool shelf; size half. | [DP:price_levels] $49.96 $2.02M cluster, vwap $50.47 [INSIGHT:institutional_accumulation] |
| **Fade (Plan B)** | **$52.00–$52.10** | If price rejects at the $51-$52 call wall *without* a sustained ask-side sweep campaign (>$200K/session for ≥2 sessions per [AGENT:sweep-tracker] gate), short a defined-risk credit-call structure. | [STRUCT:gex] $51 +$5.67M / $52 +$4.64M call walls |

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| **Hard support** | **$49.50** | [STRUCT:gex] first negative-GEX strike below spot is $49 (−$356K); $49.5 (+$340K) is the boundary |
| **DP near support** | **$49.96** | [DP:price_levels] 5-day cluster $2.02M, 40,356 shares |
| **DP base support** | **$46.40–$47.40** | [DP:price_levels] multi-day $4.04M aggregate (9 sub-levels in the 100-bp band) |
| **First resistance** | **$51.00** | [STRUCT:gex] $5.67M (largest GEX strike in chain) |
| **Major resistance** | **$52.00** | [STRUCT:gex] $4.64M (combined with $51 = $10.31M wall) |
| **Secondary upside target** | **$55.00** | [STRUCT:gex] $1.19M, next call wall |
| **Gamma flip (45-DTE)** | **$35.19** | [STRUCT:gex] full structural invalidation |
| **Today gamma flip (0DTE)** | **$44.53** | [STRUCT:today_gamma_flip] *historical reference* — 2026-05-22 expiry has now passed |
| **Largest near-term OI cluster** | **$60 (Jun-18 C60 = 211 OI)** | [OI:biggest_increases] — too far OTM to act as a magnet but caps upside extension |

## Invalidation

- **Price-based:** **TWO daily closes below $49.50** (the unanimous
  agent boundary that maps to the [STRUCT:gex] dealer-hedge edge).
  Single-day prints below do NOT invalidate (rubric: "a single
  down-day on no volume" doesn't count). A *single* daily close
  below $47.00 — into the deep multi-day DP base — also invalidates
  the near-term thesis because it means the base itself is failing.
- **Signal-based:** [INSIGHT:institutional_accumulation] flips from
  ACCUMULATION to DISTRIBUTION on the next daily refresh OR the
  [HIST:gex_time_series] regime returns to NEGATIVE for 2 consecutive
  sessions (i.e., today's flip was a one-day artifact). Either fires
  → exit 100% of the directional leg.
- **Macro-based:** A **hawkish CPI surprise on ~2026-06-11** (May CPI
  release prints ≥4.0% headline YoY, accelerating from April's 3.8%)
  OR a hawkish FOMC dot-plot revision on ~2026-06-16/17 that removes
  the single 2026 cut from the SEP [MACRO:FOMC_2026-04-29
  WebSearch:federalreserve.gov]. Either fires → tranche-exit 50%
  *before* the print, 50% on confirmation.

## Sizing (% of risk, NOT dollars)

**Primary directional structure (call debit spread, see below):**

- **Kelly inputs:** p = 0.65, entry $2.25 debit, target $5.00 max value, stop = full debit (defined-risk).
- **Payoff ratio b** = ($5.00 − $2.25) / $2.25 = **$2.75 / $2.25 = 1.222**
- **Raw Kelly** = (0.65 × 1.222 − 0.35) / 1.222 = (0.7943 − 0.35) / 1.222 = 0.4443 / 1.222 = **0.3636 (36.36%)**
- **Fractional Kelly** = 0.3636 × 0.25 = 0.0909 = **9.09%**
- **Hard cap** = 5% (M-03 cap_pct)
- **Final size:** **5% of book risk** (capped).
- **Deviation reason:** none (cap binds; no upward deviation requested).

**Defined-risk alternative (short put credit spread, see below):**

- Max loss = (width − credit) = ($1.50 − $0.55) = **$0.95 per spread**.
- For the same 5% book-risk envelope: sizes to roughly **2× the
  contract count** of the directional debit spread, because the max
  loss per spread is smaller. Apply final cap accordingly.

## Option structures

### Directional (primary) — call debit spread

- **Structure:** Long **$50 call** / Short **$55 call**, **July 17,
  2026 expiry** (57 DTE).
- **Strike rationale:** $50 long leg is at the [STRUCT:gex] +$5.67M
  wall + [DP:price_levels] vwap $50.47 + [OI:biggest_increases] Jan-27
  C50 build (610 OI is institutional anchor at this strike). $55 short
  leg is at the next [STRUCT:gex] wall ($1.19M) and sits beyond the
  $51-$52 mega-wall — captures the full call-wall pin if SYM trades
  through.
- **Expiry rationale:** July 17 is **post-OPEX June 18, post-CPI
  ~Jun 11, post-FOMC ~Jun 16-17** [MACRO catalyst calendar from
  phase-6]. Captures the post-catalyst clearing rally if base case
  holds; also avoids being long premium *through* a hawkish CPI.
- **Debit/credit:** ~**$2.25 net debit** (estimate based on phase-4
  IV term structure 66.8% at 57 DTE and observed phase-1 mid-prices;
  finalize on execution).
- **Max gain:** ($55 − $50) − $2.25 = **$2.75 per contract** (if SYM
  ≥ $55 at expiry).
- **Breakeven:** $50 + $2.25 = **$52.25**.
- **Max loss:** $2.25 per contract (the debit). Total book risk
  capped at 5%.
- **Why this structure:** IV percentile at 10.34
  [HIST:iv_percentile_zscore] = **buying premium is cheap, selling
  premium has no edge** (VRP only +2.5 vol pts, FAIR per
  [HIST:vrp]). A debit spread expresses long delta with bounded
  loss. The short $55 wing also harvests phase-1's institutional
  call-write tape (institutions are selling LEAP calls; we follow
  that flow on the short leg).

### Defined-risk alternative — pre-catalyst put credit spread

- **Structure:** Short **$48 put** / Long **$45 put**, **June 5, 2026
  expiry** (15 DTE — **expires BEFORE the CPI release on ~Jun 11**).
- **Strike rationale:** Short $48 sits between the [STRUCT:gex]
  positive-GEX wall at $47 (+$220K) and the [DP:price_levels]
  $46.40–$47.40 deep institutional base $4.04M
  ([AGENT:accumulation-hunter]). Long $45 wing covers the deep
  negative-GEX strikes ($45 −$677K). This structure pays if SYM holds
  *above $48* through expiry — i.e., if the gamma floor holds.
- **Expiry rationale:** June 5 expiry sidesteps the entire June
  catalyst window. The trade resolves before CPI, FOMC, and OPEX.
- **Credit:** ~**$0.55** (estimate; finalize on execution).
- **Max gain:** $0.55 per spread (credit retained at expiry above $48).
- **Breakeven:** $48 − $0.55 = **$47.45**.
- **Max loss:** ($48 − $45) − $0.55 = **$2.45 per spread**.
- **Risk/reward:** $0.55 / $2.45 = poor headline (1:4.45) but **the
  probabilistic edge sits in the structure**: SYM closing below $48
  inside 15 sessions requires breaking the entire phase-2 DP base
  ($4.04M) AND the phase-4 $49.50 gamma boundary. Phase-5 GEX time
  series shows the deepest 15-session drawdown was on 2026-05-19
  ($45.17) — a repeat is non-trivial.
- **Why this defined-risk alt:** Phase-4 + phase-5 say IV is cheap
  AND positive gamma is fresh. Selling 15-DTE puts at the *outside*
  of the DP base lets us harvest theta while the primary debit
  spread waits for the post-catalyst rally. **Do NOT add the put
  credit spread if final size on the directional structure already
  reaches 5%** — this is a substitute, not a co-position, unless
  total max loss across both stays ≤ 5% of book risk.

## Macro overlay (cite phase-6)

**Tailwinds:**
- Walmart $5B+ backlog, "peak automation 2026" CEO commentary
  [MACRO:SYM_Walmart_2026-02-23 WebSearch:dtcdispatch.com,
  WebSearch:symbotic.com] — multi-quarter visibility.
- SYM Q2 FY26: first GAAP profit ($9M), revenue +23% to $676M, adj
  EBITDA $78M [MACRO:SYM_Q2FY26_2026-05-06 WebSearch:stocktitan.net]
  — fundamental inflection.
- SPY in UPTREND, +5.38% 30d, above 20/50 SMA
  [MACRO:MarketRegime_2026-05-21 UW] — broad beta tailwind.

**Headwinds:**
- CPI 3.8% YoY April 2026, accelerating from 3.3%
  [MACRO:CPI_2026-04 WebSearch:cnbc.com] — delays Fed cuts.
- Fed funds 3.50-3.75% with 8-4 dissent and SEP signaling only 1 cut
  for 2026 [MACRO:FOMC_2026-04-29 WebSearch:federalreserve.gov,
  WebSearch:finance.yahoo.com] — capex-financing headwind.
- Industrials sector flow **−$27.0M today**
  [MACRO:SectorRotation_2026-05-21 UW] — direct sector outflow.
- Market regime TRANSITIONAL, breadth 37.5%
  [MACRO:MarketRegime_2026-05-21 UW] — half-size guidance built into
  conviction.
- SYM Q3 FY26 guide ($650-670M) sequentially below Q2 actual
  ($676M) [MACRO:SYM_Q2FY26_2026-05-06 WebSearch:stocktitan.net] —
  the catalyst that drove the $58 → $45 drawdown; partially priced in
  the bounce to $51.

**Net:** **mixed-headwind, near-term**. Long-term tailwinds (Walmart
deal) are durable but not actionable inside a 1-4w horizon. The trade
relies on the *post-event reset* dynamic, not on macro re-acceleration.

## Catalyst calendar (next 30 days from 2026-05-21)

| Date | Event | Impact direction |
|------|-------|------------------|
| 2026-05-22 | 0DTE SYM expiry (already passed) | + Pin to $51-$52 wall area (already realized) |
| 2026-05-29 | Weekly OPEX | Neutral — small chain effect |
| **~2026-06-05** | **Defined-risk alt expiry** | n/a (own decision) |
| ~2026-06-10–12 | **May CPI release (BLS)** | **−** if accelerates above 3.8%; **+** if cools |
| ~2026-06-16–17 | **FOMC + SEP dot plot** | **−** if dots remove the 1-cut signal; **+** if any dove turns; rate-sensitive |
| 2026-06-18 | **Monthly OPEX** | + Pin effect supports $51-$52 mechanical drift |
| Late June 2026 | ISM Manufacturing PMI | Variable — direct read on industrial capex pulse |
| **2026-07-17** | **Primary directional expiry** | n/a (own decision) |
| ~2026-08 (early) | **SYM Q3 FY26 earnings** | Out of trade window; cited for sizing reasoning |

## Post-trade monitoring checklist

- [ ] **Daily re-check of [STRUCT:gex] regime** — invalidation if
      regime returns to NEGATIVE for 2 sessions, or if today_zero_gamma
      crosses back above spot.
- [ ] **Daily re-check of [DP:block_stratified] buy_ratio** — exit if
      buy_ratio falls below 0.50 for 2 consecutive sessions
      (accumulation thesis broken).
- [ ] **Daily re-check of [INSIGHT:institutional_accumulation]
      signal** — exit if it flips from ACCUMULATION to
      DISTRIBUTION or NEUTRAL with >$1M premium.
- [ ] **Weekly [HIST:cumulative_premium_flow] direction** — exit if
      net flow turns ≤ −$2M cumulative for the trade period
      (3 consecutive sessions of bearish premium).
- [ ] **Pre-CPI (~2026-06-09)** — reduce directional structure by
      33-50% if held; the May 6 earnings drawdown of −22% on a
      Q3-guidance miss is a baseline of how much SYM can move on a
      single event, and CPI is correlated to the Industrials sector.
- [ ] **Pre-FOMC (~2026-06-16)** — re-evaluate. If the dot plot
      removes the 2026 cut, exit primary structure entirely; the
      Walmart-backlog secular thesis is unchanged but doesn't help
      a 1-4w trade.

## Citations summary

Required ≥3 distinct upstream datapoints in the thesis. Phase-9 used
the following (all resolve to specific tables/lines in cited phase
MDs):

1. **[DP:price_levels]** dark-pool buy_ratio 0.672 + $4.04M
   multi-day base at $46.40–$47.40 + $2.02M fresh $49.96 shelf —
   phase-2-dark-pool.md §Price levels (multi-day, days=5) and
   §Tier breakdown.
2. **[STRUCT:gex]** total_gex +$11.22M, ZGL $35.19, $51 wall
   $5.67M, $52 wall $4.64M (combined $10.31M call wall),
   regime POSITIVE — phase-4-structure.md §GEX (45-DTE, near-term
   hedging window).
3. **[HIST:iv_percentile_zscore]** IV30d 0.6323, percentile 10.34,
   z-score −1.015, regime LOW_IV — phase-5-historical.md §IV regime.
4. **[HIST:gex_time_series]** regime flip on 2026-05-21 from
   NEGATIVE → POSITIVE, first flip in 30 sessions —
   phase-5-historical.md §GEX time series (30 days).
5. **[MACRO:CPI_2026-04 WebSearch:cnbc.com]** headline CPI 3.8% YoY,
   accelerating from 3.3% — phase-6-macro.md §Inflation (CPI).
6. **[MACRO:SectorRotation_2026-05-21 UW]** Industrials sector flow
   −$27.0M today — phase-6-macro.md §Sector rotation.
7. **[AGENT:accumulation-hunter]** LONG bias, conviction 3, top
   signal on the multi-day DP base — phase-8-agent-views.md
   §accumulation-hunter.
8. **[AGENT:risk-monitor]** RANGE bias, conviction 2, triple-catalyst
   window warning — phase-8-agent-views.md §risk-monitor.
9. **[INSIGHT:conviction_matrix]** DIRECTIONAL_LONG, confidence
   18.39%, dark-pool buy_ratio 0.672 — phase-7-insights.md
   §Conviction matrix.

(Thesis cites citations #1, #2, #3, #4, and #6 directly — ≥3
distinct datapoints requirement met.)
