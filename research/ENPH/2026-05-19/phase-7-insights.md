# Phase 7 — UW Insights Confluence

**Ticker:** ENPH
**As-of date:** 2026-05-19 (effective UW date 2026-05-15)
**Generated:** 2026-05-19T00:00:00-04:00
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-4-structure.md, phase-5-historical.md, phase-6-macro.md

## Summary

UW's composite insight tools deliver a **strongly bullish baseline that
matches phases 1–4 / 7 but is silent on the historical cohort-backtest red
flag from phase-5**. ENPH lands on `insights_signal_confluence` with a
**score of 5/6 bullish factors** (bullish_flow, low_pcr, volume_spike,
dp_accumulation, oi_building) — only failing the **`low_iv_cheap_options`
box because IV rank is 84.97 (rich, not cheap)**
[INSIGHT:signal_confluence]. `insights_conviction_matrix` classifies the
scenario as **DIRECTIONAL_LONG** with dark-pool buy_ratio **0.631 (above
the 0.6 bullish threshold)** and explicit reasoning "Dark pool buying +
aggressive call purchases — institutional directional bet"
[INSIGHT:conviction_matrix]. `insights_institutional_accumulation` returns
**"ACCUMULATION" with buy/sell ratio 1.71×** [INSIGHT:institutional_accumulation].
`insights_price_vs_flow` reports **no divergence — price and flow aligned**
[INSIGHT:price_vs_flow]. **Next earnings date confirmed 2026-07-28**
[INSIGHT:deep_dive] which is outside the 30-day phase-9 window, so
`insights_earnings_play` is skipped as out-of-window. **Two notable tool
gaps**: `insights_deep_dive` returned "yahoo quoteSummary ENPH: HTTP 401"
on the fundamentals block (no PE, market cap, short %), and
`insights_analyst_vs_flow` returned **only the flow side** (analyst
consensus block empty, likely the same yfinance 401) — analyst-vs-flow
agreement cannot be verified in this run.

## Key signals

- **Signal confluence score: 5 of 6 — bullish_flow + low_pcr +
  volume_spike + dp_accumulation + oi_building** [INSIGHT:signal_confluence].
  Only `low_iv_cheap_options` is missing (IV rank 84.97 = expensive).
- **Conviction matrix: DIRECTIONAL_LONG — DP buy_ratio 0.631; call
  ask-vol 53,515 vs bid-vol 43,179 (net +10,336 ask); put ask-vol 6,617
  vs bid-vol 10,231 (net −3,614 = puts SOLD on bid)**
  [INSIGHT:conviction_matrix].
- **Institutional accumulation: buy/sell ratio 1.71×, signal
  "ACCUMULATION"** [INSIGHT:institutional_accumulation].
- **Price vs flow: NO divergence; price +55.09% over 30d, flow bullish,
  net +$5.55M** [INSIGHT:price_vs_flow].
- **Volume ratio 4.59×** (today's volume vs 30-day average), confirming
  the late-week volume spike that accompanied the rally
  [INSIGHT:signal_confluence].

## Detailed findings

### Deep dive snapshot

`insights_deep_dive`:

| Block | Field | Value |
|---|---|---|
| uw_dark_pool | total_premium | $105,923,117 |
| uw_dark_pool | total_shares | 2,052,741 |
| uw_dark_pool | avg_price (VWAP-style) | $51.79 |
| uw_dark_pool | trade_count | 554 |
| uw_screener | iv30d | 0.9537 (95.4%) |
| uw_screener | iv_rank | **84.97** |
| uw_screener | implied_move ($) | $1.83 |
| uw_screener | implied_move_perc | 3.47% |
| uw_screener | call_premium | $57,450,366 |
| uw_screener | put_premium | $22,913,827 |
| uw_screener | call_volume | 117,404 |
| uw_screener | put_volume | 31,519 |
| uw_screener | put_call_ratio | **0.27** |
| uw_screener | total_open_interest | 414,369 |
| uw_screener | volatility (rolling) | 38.71% |
| uw_screener | **next_earnings_date** | **2026-07-28** (Q2 2026) |
| uw_top_oi_changes | #1 | Jun-26 $50C +4,985 OI |
| uw_top_oi_changes | #2 | Jun-26 $55C +3,714 OI |
| uw_top_oi_changes | #3 | 5/15 $50C +2,197 OI (0DTE) |
| uw_top_oi_changes | #4 | Jun-26 $50P +1,508 OI (puts sold) |
| uw_top_oi_changes | #5 | Jan-27 $70C +1,310 OI |
| yahoo_fundamentals | error | **"yahoo quoteSummary ENPH: HTTP 401"** |

**Implied move:** the market is pricing only **$1.83 (3.47%)** of single-
day move on average — this is the *normalized* implied move and looks
modest relative to the 5/22 expiry IV of 121%. The implied move on the
5/22 expiry alone is much larger (a 121% IV with 7 DTE implies roughly
±5.5% on the day). Phase-9 should anchor on the **5/22 expected move
≈ ±5–6%**, not on the 3.47% normalized figure.

### Signal confluence (where ENPH ranks)

`insights_signal_confluence` (direction=bullish, min_score=1, top_n=50):

| Rank | Ticker | Score | Sector | Factors |
|---|---|---|---|---|
| 1 | DXCM | 6/6 | Healthcare | all six bullish boxes |
| 2 | BOOT | 6/6 | Consumer Cyclical | all six |
| 3 | STAA | 6/6 | Healthcare | all six |
| **4** | **ENPH** | **5/6** | **Technology** | bullish_flow, low_pcr, volume_spike, dp_accumulation, oi_building |
| 5+ | FWRD, SEI, E, PURR, OMER, PZZA, HRL, ... (43 more) | 5/6 | various | various |

ENPH is **tied for the 4th-highest confluence score on the entire UW
universe** for 2026-05-15 (50 tickers returned at score ≥5).

The single missing factor is **`low_iv_cheap_options`** because IV rank
84.97 means premium is rich — this is consistent with phase-5's finding
that IV30d is at the 100th percentile of the available window. **Phase-9
should treat the high-IV factor as a constraint on structure choice, not
as a contradiction of the directional thesis.**

Notable observation: **only 4 of 50 tickers at score ≥5 are in the
Technology sector** (ENPH, SATL, GTLB, QRVO, INOD, KLAR, UMC, OUST — 8
actually). Combined with phase-6's **−$151M Technology outflow**, the
tech-sector confluence list is doing real work but pushing against a
sector-flow headwind.

### Conviction matrix (scenario classification)

`insights_conviction_matrix` (symbol=ENPH):

| Field | Value |
|---|---|
| **scenario** | **DIRECTIONAL_LONG** |
| confidence_pct | **18.4%** |
| dark_pool.buy_ratio | 0.631 (above 0.6 bull threshold) |
| dark_pool.buy_volume | 1,294,309 |
| dark_pool.sell_volume | 758,432 |
| dark_pool.trades | 554 |
| options_flow.call_ask_volume | 53,515 |
| options_flow.call_bid_volume | 43,179 |
| options_flow.put_ask_volume | 6,617 |
| options_flow.put_bid_volume | 10,231 |
| explanation | "Dark pool buying + aggressive call purchases — institutional directional bet." |

**Reading:**
- The **scenario label is the strongest bullish classification UW
  produces** (DIRECTIONAL_LONG > HEDGED_LONG > COVERED_CALL > MIXED >
  DIRECTIONAL_SHORT).
- **call ask-vol 53,515 vs bid-vol 43,179**: net +10,336 ask-side call
  buying. **Bullish, but the bid-side calls are also large — there is
  active two-sided flow.** Not a one-way bullish stampede.
- **put bid-vol 10,231 vs ask-vol 6,617**: net +3,614 bid-side put
  selling = synthetic long signature.
- **confidence_pct 18.4% is modest** — UW's own confidence metric does
  not call this a slam-dunk. Phase-9 should respect this.

### Price vs flow (divergence)

`insights_price_vs_flow` (lookback_days=30):

| Field | Value |
|---|---|
| **divergence** | **false** |
| divergence_signal | "Price and flow are aligned" |
| flow_direction | bullish |
| price_change_pct | **+55.09%** (30d) |
| price_start (30d) | $32.04 |
| price_end (30d) | $49.69 |
| period_high | $53.89 |
| period_low | $29.90 |
| iv_rank | 84.97 |
| put_call_ratio | 0.27 |
| net_premium_flow | +$5,548,943 |

**Reading:** no reversal signal. Both flow and price are pulling in the
same direction. **However** the price has run +55% in 30 days, which is
itself a counter-signal: aligned-bullish-flow + already-huge-move is a
late-stage rally pattern. **Phase-9 should worry about chasing.**

### Analyst vs flow (consensus vs options trader)

`insights_analyst_vs_flow` (symbol=ENPH):

| Field | Value |
|---|---|
| options_flow.flow_sentiment | bullish |
| options_flow.net_flow | +$5,548,943 |
| options_flow.put_call_ratio | 0.27 |
| **analyst block** | **absent (likely yfinance 401)** |

**Cannot verify** Wall Street analyst consensus vs options-trader signal.
Phase-9 must not claim "analyst agreement" or "analyst disagreement"
based on this run; the UW deep_dive's yahoo fundamentals failed with HTTP
401, suggesting the analyst data source is the same that's unavailable.

### Institutional accumulation

`insights_institutional_accumulation` (symbol=ENPH):

| Field | Value |
|---|---|
| **signal** | **ACCUMULATION — dark pool buy volume significantly exceeds sell volume** |
| buy_sell_ratio | **1.71×** |
| buy_side_volume | 1,294,309 |
| sell_side_volume | 758,432 |
| price_30d_change_pct | +55.09% |
| total_dp_premium | $105,923,117 |
| total_dp_volume | 2,052,741 shares |
| vwap | $51.60 |
| dark_pool_trades | 554 |

Top price levels (confirming phase-2):

| Price | Premium | Shares | Trades |
|---|---|---|---|
| $51.46 | $1,867,998 | 36,300 | 3 |
| $50.81 | $1,488,733 | 29,300 | 3 |
| $51.25 | $1,429,865 | 27,900 | 4 |
| $53.19 | $1,474,747 | 27,726 | 2 |
| $51.14 | $1,406,237 | 27,500 | 4 |

**Reading:** confirms phase-2 — clean buy-side accumulation, concentrated
in the $51–$53 zone, with VWAP $51.60 sitting just above phase-4's $50
gamma wall.

### Earnings play

**SKIPPED** — `insights_earnings_play` only runs for earnings within ~14
days. Next ENPH earnings is **2026-07-28** (70+ days out), per
`insights_deep_dive.uw_screener.next_earnings_date`. Phase-9 must NOT
size on an earnings event; the catalyst pricing in the 5/22 IV term
structure is **vol-of-vol from the 5/13 IQ9S-3P announcement and Q1
beat**, not a forward earnings binary.

## Cross-check vs phases 1–5

| UW insight | Phase agreement? | Notes |
|---|---|---|
| signal_confluence score 5/6 | Phases 1–4 **agree** | Missing factor is the IV-rank one (phase-5 confirms IV is rich); the 5 bullish factors all match upstream conclusions. |
| conviction_matrix DIRECTIONAL_LONG | Phase 2 (DP) **agrees** | DP buy_ratio 0.631 matches phase-2's 0.634 large-tier reading. |
| conviction_matrix confidence 18.4% | **Modest** — disagrees with raw signal strength | UW's own confidence is low. Phase-5 backtest 14.3% win rate explains why. |
| price_vs_flow no divergence | Phase 1, 3 **agree** | But this is the "single-day" snapshot — phase-5's longer-window backtest is what should temper conviction. |
| institutional_accumulation 1.71× | Phase 2 **agrees** | Same data source; consistent. |
| analyst_vs_flow agreement | **Unverified** | yfinance 401; phase-9 cannot claim either way. |
| Yahoo fundamentals | **Tool error** | HTTP 401; no PE/market-cap snapshot. |

## Tool calls (audit trail)

| Tool | Args | Result summary |
|---|---|---|
| `mcp__uw-pp__insights_deep_dive` | symbol=ENPH, date=2026-05-15 | DP $105.9M, IV rank 84.97, next earnings 2026-07-28, yfinance 401 |
| `mcp__uw-pp__insights_signal_confluence` | direction=bullish, date=2026-05-15, min_score=1, top_n=50 | ENPH score 5/6 (tied for #4) |
| `mcp__uw-pp__insights_conviction_matrix` | symbol=ENPH, date=2026-05-15 | DIRECTIONAL_LONG, confidence 18.4%, buy_ratio 0.631 |
| `mcp__uw-pp__insights_price_vs_flow` | symbol=ENPH, date=2026-05-15, lookback_days=30 | divergence: false, +55.09% / +$5.55M aligned |
| `mcp__uw-pp__insights_analyst_vs_flow` | symbol=ENPH, date=2026-05-15 | flow side only; analyst block absent (yfinance 401) |
| `mcp__uw-pp__insights_institutional_accumulation` | symbol=ENPH, date=2026-05-15 | ACCUMULATION, buy/sell 1.71× |
| `mcp__uw-pp__insights_earnings_play` | — | **Skipped** (next earnings 70d out, outside the 14d window) |

## Tool errors

- `insights_deep_dive.yahoo_fundamentals`: **"yahoo quoteSummary ENPH:
  HTTP 401"** — yfinance auth/rate-limit failure. PE, market cap, short
  interest, dividend, fundamentals all unavailable from this source.
- `insights_analyst_vs_flow`: analyst recommendation block absent in the
  return (presumably same yfinance 401 cause); analyst consensus cannot
  be cited.

## Verdict for downstream phases

- **UW composite bias:** **BULLISH — DIRECTIONAL_LONG scenario, score
  5/6 confluence, ACCUMULATION signal.**
- **Conviction:** **4 / 5** on the directional signal stack; **3/5** when
  the modest confidence_pct (18.4%) and the IV-rich constraint are
  factored in.
- **Phase-9 baseline:** **treat DIRECTIONAL_LONG + ACCUMULATION as the
  default thesis.** Override only with the explicit phase-5 backtest red
  flag (14.3% win rate cohort) and phase-6 sector-rotation headwind, which
  argue for **defined-risk sizing rather than thesis flip**.
- **Open questions:**
  - **Analyst consensus** is unknown from this run. Phase-9 sub-agent
    `accumulation-hunter` may have alternative analyst data; otherwise
    leave analyst overlay out.
  - **UW confidence_pct 18.4%** is the most diagnostic dampening signal
    in phase-7 — phase-10 should treat this as a partial contradiction
    that supports a 0.65–0.75 conviction rather than 0.85+.
