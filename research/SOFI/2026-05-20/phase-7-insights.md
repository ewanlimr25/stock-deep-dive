# Phase 7 — UW Insights Confluence

**Ticker:** SOFI
**As-of date (requested):** 2026-05-20
**Effective data date:** 2026-05-19
**Generated:** 2026-05-20T00:00:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-4-structure.md, phase-5-historical.md, phase-6-macro.md

## Summary

UW's composite-insight stack delivers a **meaningful pushback** against the
constructive read built up across phases 1-3. Three independent UW
classifiers all converge on **MIXED / NEUTRAL**: the **conviction matrix
labels SOFI as MIXED with only 9.57% confidence**, citing a dark-pool
buy_ratio of 0.596 just below the 0.60 bullish threshold
[INSIGHT:conviction_matrix]; **institutional_accumulation flags NEUTRAL —
"balanced dark pool activity"** despite a 1.47 buy/sell ratio
[INSIGHT:institutional_accumulation]; and **SOFI is absent from BOTH the
top-50 bullish AND top-50 bearish signal_confluence tables** at min_score
1, meaning the cross-factor alignment isn't strong enough to register on
either side [INSIGHT:signal_confluence]. **insights_price_vs_flow shows
NO divergence — price and flow are aligned bearish** ($-2.5M net flow,
-7.64% price over 30d) [INSIGHT:price_vs_flow]. This is the
reconciliation moment for the run: phases 1-2 over-weighted the bullish
flow narrative; phases 4-6 (dealer structure, historical, macro) already
called for caution; phase 7's composite agrees with phases 4-6 and
recalibrates phases 1-2 downward. **Net composite read: MIXED with mild
mean-reversion tilt at $15-$16**.

## Key signals

- **Conviction matrix: MIXED, confidence 9.57%**, dark-pool buy_ratio
  0.596 (below 0.60 bull threshold). Call ask/bid 89,595/108,863 = ask
  dominant on calls; put ask/bid 36,181/33,327 = balanced.
  [INSIGHT:conviction_matrix]
- **Institutional accumulation: NEUTRAL — "balanced dark pool activity"**,
  buy/sell ratio 1.47, VWAP $15.20, 1,108 trades, $187.7M premium.
  [INSIGHT:institutional_accumulation]
- **SOFI absent from top-50 bullish_flow signal_confluence** at min_score 1
  → SOFI's bullish factor count is < 1 of 6 possible (the 6 factors are:
  bullish_flow, low_pcr, volume_spike, dp_accumulation, oi_building,
  low_iv_cheap_options). [INSIGHT:signal_confluence]
- **SOFI absent from top-50 bearish_flow signal_confluence** as well —
  meaning no clear bearish stack either. Net read: genuinely mixed.
  [INSIGHT:signal_confluence]
- **Price vs flow: ALIGNED bearish, NO divergence** over 30d.
  Period: $20.13 high → $14.92 low → $15.23 end. Flow $-2.5M net.
  [INSIGHT:price_vs_flow]
- **No earnings play in window**: next earnings per UW screener
  **2026-08-04** (~77 days out). Out of phase-7 14-day window — skipped.
  [INSIGHT:deep_dive] Note minor calendar discrepancy with phase-6
  WebSearch which had 2026-07-28; UW screener date is more authoritative.

## Detailed findings

### Deep dive snapshot

| Metric | Value | Source |
|---|---|---|
| UW dark pool total premium | $187.72M | UW |
| UW dark pool shares | 12,347,503 | UW |
| UW dark pool avg price | $15.221 | UW |
| UW dark pool trade count | 1,108 | UW |
| Screener IV30d | 53.81% | UW |
| Screener IV rank | 18.77 | UW |
| Screener implied move | $0.59 / 3.89% | UW |
| Screener PCR | 0.38 | UW |
| Screener call vol | 221,091 | UW |
| Screener put vol | 84,505 | UW |
| Screener call premium | $21.60M | UW |
| Screener put premium | $8.89M | UW |
| Screener bullish premium | $11.11M | UW |
| Screener bearish premium | $13.62M | UW |
| Screener total OI | 4,218,292 | UW |
| **Next earnings (UW)** | **2026-08-04** | UW screener |
| Yahoo fundamentals | **error: HTTP 401** | failed |

**Note:** Yahoo fundamentals errored with HTTP 401, so we have no
fundamentals snapshot (PE, market cap, short %, etc.) in this run. Phase 6
SEC source confirms Q1 metrics (revenue $1.1B, net income $167M, EPS
$0.12, members 14.7M) [MACRO:SOFI_Q1_2026 WebSearch:sec.gov].

### Signal confluence (cross-ticker, min_score = 1)

**Bullish confluence (50 tickers ranked):** SOFI **absent**. Top scorers
include SG (score 6, Consumer Cyclical), TE (score 6, Industrials), DPST
(score 5), WULF (score 5, Financial Services), HRL (score 5, IV rank 100,
Consumer Defensive). Of the 50 bullish-confluence tickers, six are
Financial Services (WULF, ARX, HIVE, PURR, CIFR plus AFL) — but SOFI does
not make the cut. **Implication:** SOFI's bullish factor count (out of 6)
is below 1 — possibly only "low_pcr" fires (PCR 0.38 is low) but none of
the other five (bullish_flow, volume_spike, dp_accumulation, oi_building,
low_iv_cheap_options) clear UW's thresholds on a market-wide-comparable
basis.

**Bearish confluence (50 tickers ranked):** SOFI **absent**. Top scorers
include BNTX (score 6, IV rank 87, Healthcare), EIX (score 5, Utilities),
FLEX (score 5, Technology), TOL (score 5, Consumer Cyclical), DG (score 5,
Consumer Defensive). Of the 50 bearish-confluence tickers, six are
Financial Services (PSEC, TIGR, FUTU plus FHI). SOFI does not make the
cut.

**Net read:** SOFI is genuinely **in the middle** — not confluence-bullish,
not confluence-bearish. This is a strong meta-signal that the run's
confluence score will land in the 30-50/100 range in phase 10.

### Conviction matrix

| Field | Value |
|---|---|
| Scenario | **MIXED** |
| Confidence | **9.57%** |
| Dark pool buy_ratio | 0.596 |
| Bull threshold | 0.60 |
| Bear threshold | 0.40 |
| Dark pool buy volume | 7,354,984 |
| Dark pool sell volume | 4,992,519 |
| Dark pool trades | 1,108 |
| Options call ask vol | 89,595 |
| Options call bid vol | 108,863 |
| Options put ask vol | 36,181 |
| Options put bid vol | 33,327 |
| Explanation | "Balanced dark pool activity — no clear bias." |

**Calibration disagreement:** Phase 2 weighted the 0.339 (block-tier) and
0.616 (large-tier) buy ratios to **0.596 net** and labeled it ACCUMULATION
4/5. UW's matrix uses a **strict 0.60 bullish threshold** and labels 0.596
MIXED. The 0.004-point gap matters: my phase-2 read was at the very edge
of bullish, not solidly inside it. **Recalibrate phase-2 verdict downward
to NEUTRAL-LEANING-BULLISH 3/5 max for the audit.**

**Options-flow micro-context within the matrix:** call ask 89,595 vs call
bid 108,863 — **CALLS WERE BID-HEAVY ON NET TODAY**, not ask-heavy. This
is the smoking gun for the phase-3 interpretation: today's dominant
call-side activity was SELLING (bid-hits), not BUYING. The institutional
covered-call-write thesis from phase 3 is reinforced by this matrix-level
ask/bid breakdown. Put ask 36,181 vs put bid 33,327 — slightly ask-heavy
on puts → mild downside protection demand.

### Price vs flow

| Field | Value |
|---|---|
| Divergence | **FALSE — price and flow are aligned** |
| Flow direction | bearish |
| Bullish premium (30d) | $11,109,142 |
| Bearish premium (30d) | $13,615,364 |
| Net premium flow | -$2,506,222 |
| Period high (30d) | $20.13 |
| Period low (30d) | $14.92 |
| Price start (30d ago) | $16.49 |
| Price end | $15.23 |
| Price 30d change | -7.64% |
| IV rank | 18.77 |
| PCR | 0.38 |

No reversal divergence. Confirms phase-5 read: bearish flow + falling
price = trend-aligned, no contrarian setup.

### Analyst vs flow

The tool returned only options-flow data — no Wall Street analyst
consensus block. Likely caused by the same Yahoo 401 error that disabled
the deep_dive fundamentals. **Cannot cross-check Wall St rating drift
against the tape in this run.** Flagged as open question.

### Institutional accumulation

| Field | Value |
|---|---|
| Signal | **NEUTRAL — "balanced dark pool activity"** |
| Buy/sell ratio | 1.47 |
| Buy-side volume | 7,354,984 |
| Sell-side volume | 4,992,519 |
| Dark pool trades | 1,108 |
| VWAP | $15.20 |
| Total DP premium | $187,719,852 |
| Avg trade price | $15.22 |
| Price 30d change | -7.64% |

**Top 5 price levels (today only, DP-aggregated):**

| Price | Premium | Shares | Trades |
|---|---|---|---|
| $15.29 | $12.55M | 820,673 | 75 |
| $15.33 | $11.97M | 781,039 | 88 |
| $15.30 | $9.95M | 650,473 | 75 |
| $15.06 | $8.61M | 571,712 | 22 |
| $15.32 | $8.72M | 569,364 | 61 |

**Calibration:** UW's institutional_accumulation labels SOFI NEUTRAL despite
a 1.47 buy/sell ratio (which sounds bullish). The reason: the tool weighs
volume-traded vs total tape, and a 1.47 ratio in a ticker that just fell
-7.64% over 30d is **not enough divergence from price action to register
as smart-money accumulation**. UW is essentially saying: institutions are
nibbling, but not loading the boat.

### Earnings play

**Skipped — next earnings 2026-08-04 (UW screener) is ~77 calendar days
out, far outside the 14-day window for the `insights_earnings_play` tool.**
The Sep-18 IV kink at 87.2% from phase 4 [STRUCT:iv_term_structure] is
therefore NOT an earnings event (Q2 2026 reports in August, not September).
Possibility: the Sep-18 IV is elevated because of Q3 guide expectations or
a known investor day in September. WebSearch did not surface a specific
event. Flag as open question.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|---|---|---|
| `insights_deep_dive` | symbol=SOFI, date=2026-05-19 | DP $187.7M, screener IV rank 18.77, next earnings 2026-08-04, Yahoo 401 |
| `insights_signal_confluence` | direction=bullish, min-score=1, top-n=50, date=2026-05-19 | SOFI absent from top-50 |
| `insights_signal_confluence` | direction=bearish, min-score=1, top-n=50, date=2026-05-19 | SOFI absent from top-50 |
| `insights_conviction_matrix` | symbol=SOFI, date=2026-05-19 | MIXED, confidence 9.57%, DP buy_ratio 0.596 (below 0.60) |
| `insights_price_vs_flow` | symbol=SOFI, lookback-days=30, date=2026-05-19 | No divergence; flow & price both bearish; -7.64% / 30d |
| `insights_analyst_vs_flow` | symbol=SOFI, date=2026-05-19 | Analyst consensus block missing (Yahoo 401 cascade) |
| `insights_institutional_accumulation` | symbol=SOFI, date=2026-05-19 | NEUTRAL — buy/sell 1.47, VWAP $15.20 |

## Tool errors

- `insights_deep_dive` → `yahoo_fundamentals.error: "yahoo quoteSummary
  SOFI: HTTP 401"`. Yahoo Finance authentication failed; fundamentals
  block empty. This cascades into the missing analyst block in
  `insights_analyst_vs_flow`. Not a UW tool error per se but an upstream
  data dependency.

## Cross-check vs phases 1-5

| UW insight | Phase agreement? | Notes |
|---|---|---|
| `signal_confluence` (bullish, SOFI absent) | **DISAGREES** with phase-1 mixed-bullish lean; **AGREES** with phase-5 bullish_flow 0% win rate fade-warning |
| `signal_confluence` (bearish, SOFI absent) | AGREES with phase-1 mixed verdict (genuine middle) |
| `conviction_matrix` MIXED 9.57% confidence | **SOFT-DISAGREES** with phase-2 ACCUMULATION 4/5; recalibrates dark pool read to NEUTRAL-LEANING-BULLISH at best |
| `institutional_accumulation` NEUTRAL | **SOFT-DISAGREES** with phase-2 ACCUMULATION 4/5; both look at the same DP data, UW labels NEUTRAL not ACCUMULATION |
| `price_vs_flow` no divergence (both bearish) | AGREES with phase-5's net-bearish premium tally; partially CONTRADICTS phase-3's bullish call buildup (but the call buildup was bid-heavy on net per matrix, i.e. call-WRITING — internally consistent) |
| Call ask/bid 89,595/108,863 | **DIRECTLY CONFIRMS** phase-3 [OI:smart_positioning] read that net call activity today was bid-heavy (writing-dominant) at 17/17.5/18/19/20/25 strikes |
| Put ask/bid 36,181/33,327 | Mild ask-skew on puts → mild protection demand, consistent with phase-4 COMPLACENT skew (downside hedging is cheap and being mildly bought) |

## Verdict for downstream phases

- **UW composite bias:** **MIXED**, leaning very slightly NEUTRAL-bullish
  (DP buy_ratio 0.596 just below threshold).
- **Conviction:** **2 / 5** — UW's strict thresholds are explicit that
  SOFI doesn't qualify as confluence-bullish or confluence-bearish on
  this tape.
- **Phase 9 should treat this as the BASELINE** and only override with
  specific contrary evidence. Specifically, phase 9 should:
  1. Recalibrate phase-2's ACCUMULATION 4/5 verdict down to NEUTRAL-LEANING-
     BULLISH 3/5 to reflect the UW threshold pushback.
  2. Recalibrate phase-1's mixed-bullish lean to **mixed-neutral with
     near-term covered-call dominance**, because the matrix-level
     ask/bid (call ask 89,595 vs bid 108,863) directly shows today's
     call activity was net WRITING, not buying.
  3. Maintain phase-3's pin/structure read ($15 pin, $16 ceiling, $17
     covered-call wall) and phase-4's positive multi-week / short-gamma
     intraday read.
  4. Maintain phase-5's PREMIUM_BUYING regime (VRP -9.47%) — premium
     remains cheap regardless of direction.
  5. Maintain phase-6's HEADWIND macro overlay.
- **Open questions:**
  - Yahoo 401 prevented Wall St consensus comparison — would have been
    useful to see if analysts are upgrading vs downgrading SOFI post-Q1.
  - What event drives the Sep-18 IV kink at 87.2%? Not Q2 earnings (Aug 4).
    Possible: Investor Day, Fed-cut expectations clustering, or just
    chain-imbalance noise. Phase 9 should not rely on Sep IV signal until
    sourced.
