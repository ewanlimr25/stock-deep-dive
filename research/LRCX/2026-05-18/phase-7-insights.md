# Phase 7 — UW Insights Confluence

**Ticker:** LRCX
**As-of date (requested):** 2026-05-18
**Effective as-of date (data):** 2026-05-15
**Generated:** 2026-05-18T00:00:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-4-structure.md, phase-5-historical.md, phase-6-macro.md

## Summary

UW's composite verdict is **MIXED scenario with confirmed price-flow
divergence**: the conviction matrix labels LRCX **MIXED at 2.57%
confidence**, signal_confluence does **not rank LRCX in either the top-50
bullish or top-50 bearish** (both at min_score=1, max top_n=50),
institutional_accumulation is **NEUTRAL** (buy/sell ratio 1.11, no
directional pressure), and **price_vs_flow flags an active DIVERGENCE
(price +29.0% over 30 days, options flow net -$2.2M bearish)** — a
textbook fade-the-rally / mean-reversion setup at IV rank 71.97. This
is the **highest single-signal confluence of the entire phase-7
sweep**. UW's institutional_accumulation top dark-pool price levels
($283.81, $282.93, $282.74, $282.99, $286.14) match phase-2's
intraday volume zone within $1. Earnings date 2026-07-29 confirms
phase-6.

## Key signals

- **Price-Flow DIVERGENCE: +29.0% price, -$2.2M net flow** (bearish)
  — IV rank 71.97 amplifies the mean-reversion edge
  [INSIGHT:price_vs_flow].
- **Conviction matrix MIXED at 2.57% confidence**: dark-pool buy_ratio
  0.526 (between 0.4/0.6 thresholds), call_bid/call_ask volume **18,924 /
  11,844 = 1.60** (call writing) [INSIGHT:conviction_matrix].
- **LRCX absent from top-50 bullish AND top-50 bearish signal_confluence
  lists** even at min_score=1 → no clean confluence; tape is genuinely
  two-sided [INSIGHT:signal_confluence].
- **Institutional accumulation NEUTRAL** (buy 279,592 vs sell 252,209,
  ratio 1.11) — balanced, no mega-tier [INSIGHT:institutional_accumulation].
- **Next earnings 2026-07-29 confirmed**; IV rank 71.97; implied move
  (intraday cross-strike) 1.13% — small, reflecting just 0DTE/5/22 ATM
  pricing [INSIGHT:deep_dive].

## Detailed findings

### Deep dive snapshot

| Field | Value |
|-------|-------|
| Symbol | LRCX |
| Sector | Technology |
| Spot (5/15 close) | $284.51 |
| **IV30d** | **64.21%** |
| **IV rank** | **71.97** |
| Put/Call ratio | 0.76 |
| Implied move (UW screener) | 1.13 / 0.40% — single-strike ATM-based |
| Bullish premium 5/15 | $21,797,567 |
| Bearish premium 5/15 | $24,041,565 |
| Net premium flow 5/15 | **-$2,243,998** |
| Volatility (close-to-close σ) | 8.95% |
| **Next earnings** | **2026-07-29** ✓ confirms phase-6 |
| Total OI | 600,399 |
| Call volume | 33,314 |
| Put volume | 25,369 |
| Yahoo fundamentals | **HTTP 401 error** (Yahoo blocked) |

Top OI changes (mirrors phase-3, included for audit):
- 8/21 400C +2007 OI, $13.00 avg → call write
- 8/21 310C +1503 OI, $38.34 avg → call write
- 8/21 320C +888 OI, $33.90 avg → long call
- 5/15 320C +800 OI, $0.86 avg → 0DTE
- 5/15 295P +439 OI, $3.85 avg → 0DTE put

### Signal confluence

Direction = **bullish**, min_score=1, top_n=50 → **LRCX not in top 50**.
The 50 ranked tickers max out at score 6 (DXCM, BOOT, STAA) and floor at
score 5. Tech-sector tickers in the bullish list: ENPH, SATL, GTLB, QRVO,
INOD, UMC, OUST, KLAR — but **not LRCX**.

Direction = **bearish**, min_score=1, top_n=50 → **LRCX not in top 50**.
The bearish top-50 has 50 tickers from score 4–6 including **SMH (score
5), ADI (score 5), SOXL (score 4), AEHR (score 4), VSH (score 4)** —
multiple semi peers, but **LRCX absent**.

**Interpretation:** UW's confluence scorer requires alignment across
≥4 of (bullish_flow, low_pcr, volume_spike, dp_accumulation, oi_building,
low_iv_cheap_options) or the bearish counterpart. LRCX has:
- ❌ bullish_flow (5/15 net flow was bearish)
- ✅ low_pcr (0.76)
- ❌ volume_spike (volume_ratio not flagged)
- ❌ dp_accumulation (buy_ratio 0.526 — neutral)
- ✅ oi_building (23 consecutive days from phase-5)
- ❌ low_iv_cheap_options (IV rank 72 is high, not low)

That's only **2 of 6 bullish factors → too few to rank**. And for the
bearish side LRCX has bearish_flow + oi_building_puts (partial) + high_iv
but lacks high_pcr (0.76 isn't high) and dp_distribution (buy_ratio
0.526 is neutral, not <0.4) — also doesn't clear the threshold.

This **absence-from-both-lists is itself the headline signal**: LRCX
is **mid-spectrum / no clean institutional consensus**, which is exactly
phases 1–6's read.

### Conviction matrix

| Metric | Value |
|--------|------:|
| Scenario | **MIXED** |
| Confidence | **2.57%** |
| Bull threshold | 0.6 |
| Bear threshold | 0.4 |
| DP buy_ratio | **0.526** (mid) |
| DP buy volume | 279,592 |
| DP sell volume | 252,209 |
| **Call bid volume** | **18,924** |
| **Call ask volume** | **11,844** |
| Call bid/ask ratio | **1.60** (call writing dominant) |
| Put bid volume | 11,671 |
| Put ask volume | 12,686 |
| Put bid/ask ratio | 0.92 (slight put buying) |

Explanation: *"Balanced dark pool activity — no clear bias."*

Call bid/ask 1.60 is the cleanest single-number capture of the
**call-write campaign** from phases 1 and 3. Put bid/ask 0.92 is a
slight tilt toward put buying (hedging/bearish), consistent with the
5/22 260P ask-side $519k and 5/22 287.5P ask-side $377k from phase-1.

### Price vs flow — THE divergence

| Metric | Value |
|--------|------:|
| Period | 30 days |
| Price start | $220.65 |
| Period high | $302.00 |
| Period low | $216.50 |
| Price end | $284.72 |
| **Price change** | **+29.04%** |
| Net premium flow | **-$2.2M** (bearish) |
| Flow direction | **bearish** |
| **IV rank** | **71.97** |
| Put/call ratio | 0.76 |
| **Divergence** | **TRUE** |
| Divergence signal | **"Price is up 29.0% but options flow is bearish"** |

This is the **single most actionable composite signal in phase 7**. The
combination of:
- A large up-move (+29% in 30 days)
- Bearish flow on the most recent session
- Elevated IV rank (72)
- Sector-wide bearish flow confirmed (phase-5 backtest)
- Identifiable catalyst (Samsung strike on 5/21 from phase-6)

…is the textbook **fade-the-rally setup**. Historical backtest from
phase-5 puts the n=7 semi-sector cohort at 100% bear-side resolution
with -4.4% avg in 20 days.

### Analyst vs flow

| Metric | Value |
|--------|------:|
| Flow sentiment | **bearish** |
| Net premium flow | -$2,243,998 |
| Put/call ratio | 0.76 |

The tool returned no analyst block (yfinance call likely failed
silently — Yahoo blocked from deep_dive too). Analyst data is sourced
from phase-6 WebSearch: **Moderate Buy consensus, $285.94 PT (5/2/26)**.
Stock is at $284.51 — **at the consensus PT**. Analysts effectively
neutral; options flow is bearish. Mild Wall Street vs flow divergence,
but the analyst PT is within $1 of spot so the disagreement is
inconsequential at current levels.

### Institutional accumulation

| Metric | Value |
|--------|------:|
| Signal | **NEUTRAL — balanced dark pool activity** |
| Buy/sell ratio | 1.11 |
| Buy-side volume | 279,592 |
| Sell-side volume | 252,209 |
| Total DP premium | $151,238,655 |
| VWAP | $284.39 |
| Avg trade price | $284.55 |
| 30d price change | +29.04% |

**Top dark-pool price levels (single-day, 5/15):**

| Price | Premium | Shares | Trades |
|------:|--------:|-------:|------:|
| **$283.81** | **$6.01M** | 21,181 | 2 |
| $282.93 | $4.44M | 15,685 | 4 |
| $282.74 | $3.82M | 13,517 | 8 |
| $282.99 | $3.41M | 12,047 | 3 |
| $286.14 | $3.06M | 10,704 | 3 |

Confirms phase-2's $283–$284 support cluster. The $283.81 level (where
the day's largest single block traded at the bid) is now also the
single-day premium concentration center.

### Earnings play

**Skipped** — LRCX next earnings 2026-07-29, ~72 days away, far outside
the 14-day `insights_earnings_play` window. The 8/21 OI campaign is
covered in phase-3 and called out in phase-6 as the post-earnings
positioning vehicle.

## Tool calls (audit trail)

| Tool | Args | Result |
|------|------|--------|
| `mcp__uw-pp__insights_deep_dive` | symbol=LRCX, date=2026-05-15 | OK, yahoo 401 |
| `mcp__uw-pp__insights_signal_confluence` | direction=bullish, min-score=1, top-n=50, date=2026-05-15 | LRCX absent |
| `mcp__uw-pp__insights_signal_confluence` | direction=bearish, min-score=1, top-n=50, date=2026-05-15 | LRCX absent |
| `mcp__uw-pp__insights_conviction_matrix` | symbol=LRCX, date=2026-05-15 | MIXED, 2.57% |
| `mcp__uw-pp__insights_price_vs_flow` | symbol=LRCX, lookback-days=30, date=2026-05-15 | **DIVERGENCE** |
| `mcp__uw-pp__insights_analyst_vs_flow` | symbol=LRCX, date=2026-05-15 | flow only |
| `mcp__uw-pp__insights_institutional_accumulation` | symbol=LRCX, date=2026-05-15 | NEUTRAL |

## Tool errors

- `mcp__uw-pp__insights_deep_dive` partial: `yahoo_fundamentals` returned
  `HTTP 401` (Yahoo quoteSummary auth-walled). All UW-native fields
  populated. Fundamentals already covered via phase-6 WebSearch.
- `mcp__uw-pp__insights_analyst_vs_flow`: no analyst block in response
  (Yahoo gate). Analyst consensus already covered in phase-6.

## Cross-check vs phases 1–6

| UW insight | Phase agreement? | Notes |
|------------|------------------|-------|
| `signal_confluence` (LRCX absent both directions) | **AGREES** phase-1 (mixed), phase-2 (balanced), phase-3 (write + buy split), phase-7 conviction MIXED | UW confirms no clean confluence |
| `conviction_matrix` MIXED 2.57% | **AGREES** phases 1–4 | Call bid/ask 1.60 is the single-number summary of the call-write campaign |
| `price_vs_flow` DIVERGENCE | **AGREES** phase-5 (5/15 flow flipped bearish after 4 bullish days; -5.1% reversal day) | This is the strongest single-signal anchor for the short thesis |
| `institutional_accumulation` NEUTRAL | **AGREES** phase-2 (mild distribution, no mega-tier) | DP buy/sell ratio 1.11 vs phase-2 large-tier buy_ratio 0.538 (consistent) |
| `deep_dive` next_earnings 2026-07-29 | **CONFIRMS** phase-6 | |
| `deep_dive` IV rank 71.97 | **AGREES** phase-5 | |
| Top DP price levels $283–$286 | **AGREES** phase-2 (S1 $283–$284) | |

**Zero contradictions** between UW composite tools and the phase 1–6
chain. The story is internally consistent.

## Verdict for downstream phases

- **UW composite bias:** **MIXED tape with high-conviction fade-the-rally
  setup**. The conviction_matrix says MIXED at 2.57%, but the
  price_vs_flow divergence is the cleanest standalone signal in the
  entire phase-7 sweep and points unambiguously to mean reversion.
  Combine with phase-5's bearish-flow signal backtest (100% win rate,
  semi peers) and phase-6's Samsung-strike catalyst (5/21) → phase-9's
  baseline should be **defined-risk short or fade-the-bounce structures
  with a vol-selling tilt** (VRP +8.9% supports credits).
- **Conviction in phase-7 verdict: 4/5.** Internally consistent across
  all six insight tools; the divergence signal is concrete and
  measurable; only downgrade comes from the inherent "MIXED" scenario
  label (UW does not see this as a high-conviction directional setup
  for either side, just for **mean reversion / time-decay capture**).
- **Phase 9 baseline:** Treat as a **rich-vol, ranging-to-mildly-bearish
  setup, sized as a fade-the-rally with a near-term catalyst (5/21
  strike) into 5/22 OPEX, NOT as an outright bearish directional bet.**
  Override only if phase-8 surfaces fundamentals/technicals invalidating
  this read.
- **Open questions for phase 8 agents:**
  1. Does the Samsung strike risk-off persist past 5/22 OPEX into 5/29,
     or does it fade fast (one-week vol spike pattern)?
  2. The UW signal_confluence absence is rare for a $35B+ name on a
     down-5% day; does the desk-PM panel see this as "no signal" or as
     "wait for the next data point"?
  3. If LRCX bounces to $290–$300 next week, do dealer support walls
     (phase-4) absorb the move or amplify it given the 8 GEX flips in
     26 sessions?
