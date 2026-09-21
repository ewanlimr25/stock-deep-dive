# Phase 7 — UW Insights Confluence

**Ticker:** XOM
**As-of date (user request):** 2026-05-20
**Effective data date:** 2026-05-18
**Generated:** 2026-05-19T00:00:00Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-4-structure.md, phase-5-historical.md, phase-6-macro.md

## Summary

UW's composite tools deliver a **split verdict** that synthesizes the
phase-1–6 tension. On the options side, `insights_price_vs_flow` confirms
"Price and flow are aligned" (price +4.05% / 30d, flow bullish). On the
stock side, `insights_conviction_matrix` returns **DISTRIBUTION** (confidence
15.78%) with explanation "Dark pool selling with mixed options activity",
and `insights_institutional_accumulation` independently returns **DISTRIBUTION
— dark pool sell volume significantly exceeds buy volume** (1.06M buy vs 2.03M
sell, buy/sell ratio 0.52). Critically, **`insights_signal_confluence`
(bullish direction, min_score=1) returned 50 tickers and XOM is NOT in the
list** — meaning XOM's composite bullish score is below ~5 (the cutoff for
the top-50). The setup is **HEDGED_LONG / profit-taking / call-write
overlay**, NOT a clean DIRECTIONAL_LONG.

## Key signals

- **`insights_conviction_matrix` = DISTRIBUTION** (confidence 15.78%, dp
  buy_ratio 0.342 below 0.4 bear threshold). Call_ask 29,426 vs call_bid
  36,074 — aggregate call flow is **bid-side dominant**, the inverse of the
  ask-favored pattern phase-3 noted at the Jun'26 165C contract level.
  Interpretation: a substantial portion of today's call activity is call
  *writing* (bid-side), masking the few large ask-side OI builds.
  [INSIGHT:conviction_matrix]
- **`insights_institutional_accumulation` = DISTRIBUTION** (sell volume 1.92×
  buy volume; VWAP $159.41; 986 dark-pool trades). Confirms phase-2's
  mega-tier 95% sell skew but raises confidence by aggregating
  the entire DP tape. Top price level $159.44 ($80.4M, sell-classified
  block). [INSIGHT:institutional_accumulation]
- **`insights_signal_confluence` (bullish, min_score=1, top-n=50): XOM
  ABSENT.** The top-50 includes JBS, TE, CZR, KVUE, GAU, BROS, MNST (score
  6) and 43 names at score 5. XOM's composite likely scores 2–3 because it
  FAILS `dp_accumulation` and FAILS `low_iv_cheap_options` (IV rank 73 is
  high), only hitting `bullish_flow`, `low_pcr`, `oi_building`.
  [INSIGHT:signal_confluence]
- **`insights_price_vs_flow` = "Price and flow are aligned"; divergence: FALSE.**
  Bullish flow + rising price (+4.05% over 30d window). No reversal signal.
  But also no divergence-amplification. [INSIGHT:price_vs_flow]
- **`insights_deep_dive` confirms next earnings date 2026-08-07** — outside
  the 30-day window, so no earnings play. **Yahoo fundamentals returned
  HTTP 401 error**, so PE/short-interest/book-value not available; rely on
  phase-6 SEC-filing-derived earnings data. [INSIGHT:deep_dive]

## Detailed findings

### Deep dive snapshot

| Metric | Value | Source |
|--------|-------|--------|
| Total DP premium today | $492.2M | UW |
| Total DP shares | 3,087,793 | UW |
| Total DP trades | 986 | UW |
| Avg DP price | $159.49 | UW |
| Total options OI | 1,025,686 | UW |
| Call premium | $28.6M | UW |
| Put premium | $8.2M | UW |
| Net flow | +$306,031 | UW |
| Bullish premium | $17.0M | UW |
| Bearish premium | $16.7M | UW |
| P/C ratio | 0.3087 | UW |
| IV30d | 31.49% | UW |
| IV rank | 73.27 | UW |
| Implied move (next event) | $4.25 / 2.65% | UW |
| **Next earnings date** | **2026-08-07** | UW |
| Realized vol (60d window) | 37.36% | UW |
| Yahoo fundamentals | **HTTP 401 error** | UW (degraded) |

Top OI changes (already covered in phase-3, included here for confluence
check):
- Jun'26 165C +8,150 OI (DTE 31, $2.48 avg)
- Jun'26 160C +3,342 OI (DTE 31, $3.95 avg)
- May 22 160C +2,309 OI (DTE 4, $1.23 avg)
- May 22 180C +2,131 OI (DTE 4, $0.07 avg)
- Jun'26 135P +2,062 OI (DTE 31, $0.49 avg)

### Signal confluence (bullish direction)

**XOM is NOT in the top-50 bullish confluence list at min_score=1.** The
list (50 results, scores 6 and 5) is led by:

| Rank | Ticker | Sector | Score | Factors |
|------|--------|--------|-------|---------|
| 1 | JBS | Consumer Defensive | 6 | bullish_flow + low_pcr + volume_spike + dp_accumulation + oi_building + low_iv_cheap_options |
| 2 | TE | Industrials | 6 | (all 6 factors) |
| 3 | CZR | Consumer Cyclical | 6 | (all 6 factors) |
| 4 | KVUE | Consumer Defensive | 6 | (all 6 factors) |
| 5 | GAU | Basic Materials | 6 | (all 6 factors) |
| ... | (45 more at score 5) | | | |

**XOM's likely missing factors:**
- ✗ `dp_accumulation`: confirmed FAIL by conviction_matrix + institutional_accumulation
- ✗ `low_iv_cheap_options`: IV rank 73.27 ≫ low (typically <30)
- ✓ `bullish_flow`: net flow +$306k (marginal)
- ✓ `low_pcr`: 0.31
- ✓ `oi_building`: +34,856 net OI today (phase-5)
- ? `volume_spike`: not separately measured here, but historical_trend showed today's options volume 93,709 calls + 22,107 puts = 115,816 contracts on 1.03M OI = 11% of OI → modest, possibly below the threshold

So XOM's composite score is likely **3–4** — below the top-50 cutoff but
not zero. **It's a mildly bullish setup with two important failures (DP
distribution + expensive vol).**

### Conviction matrix (DISTRIBUTION)

```
scenario: DISTRIBUTION
confidence_pct: 15.78
dark_pool:
  buy_ratio: 0.342  (< 0.4 bear threshold)
  buy_volume:  1,056,593
  sell_volume: 2,031,200
  trades: 986
options_flow:
  call_ask_volume: 29,426
  call_bid_volume: 36,074  ← bid-dominant
  put_ask_volume:  10,159
  put_bid_volume:  10,221  ← roughly balanced
explanation: "Dark pool selling with mixed options activity."
```

**Critical insight:** the call bid-volume (36,074) exceeds the call ask-volume
(29,426) by 22.6%. In phase-3, the dominant Jun'26 165C contract showed
ask-favored 487 contracts net — that's marginal. The aggregate
across all contracts is **net bid-side for calls**. This means: while
specific large blocks (Jun'26 165C, Mar'27 155C ask) were bought aggressively,
the MAJORITY of call volume across the chain was hit on the bid (call
sellers). When combined with DP sell skew, this points to: institutions
holding existing long-stock positions are **selling stock + writing calls =
profit-taking + income overlay**, not exiting (since they wouldn't write
covered calls if exiting outright).

Confidence 15.78% is LOW — the tool itself flags this as a thin, conflicting
read.

### Price vs flow

| Metric | Value |
|--------|-------|
| Divergence | **FALSE** |
| Signal | "Price and flow are aligned" |
| Flow direction | bullish |
| Period start price (30d ago) | $156.22 |
| Period end price | $162.55 (intraday) / $160.49 (close) |
| 30d price change | +4.05% |
| Period high | $163.32 |
| Period low | $141.97 |
| IV rank | 73.27 |
| Bullish premium today | $17.00M |
| Bearish premium today | $16.70M |
| Net premium flow | +$306,031 |
| PCR | 0.3087 |

**No divergence** = no reversal signal. The flow is bullish and the price is
rising — this is the **trend-confirmation regime**, not a setup. The net
premium flow ($306k) is small relative to gross premium ($33.7M), so the
bullish tilt is mild.

### Analyst vs flow

The tool returned only the `options_flow` field for XOM (no
`analyst_recommendation` block). This is **consistent with the Yahoo HTTP
401 error** in `insights_deep_dive` — the tool relies on yfinance for the
analyst side and yfinance is degraded.

Phase 8's "Fundamental & Catalyst" analyst agent should pull WebSearch-based
analyst-target estimates as a fallback.

```
options_flow:
  flow_sentiment: bullish
  net_flow: 306031
  put_call_ratio: 0.3087
  bullish_premium: 17,001,679
  bearish_premium: 16,695,648
```

### Institutional accumulation

```
signal: "DISTRIBUTION — dark pool sell volume significantly exceeds buy volume"
avg_trade_price: 159.49
buy_sell_ratio: 0.52  (52% buy, 48% sell by share count … BUT)
buy_side_volume:  1,056,593
sell_side_volume: 2,031,200  (≈ 1.92x buy)
total_dp_premium: $492,233,782
total_dp_volume:  3,087,793
vwap: 159.41
price_30d_change_pct: +4.05%
dark_pool_trades: 986
```

The **buy_sell_ratio 0.52 figure is confusingly named** — the SHARE volumes
clearly show 1.92× more shares sell-classified than buy-classified. The
qualitative signal "DISTRIBUTION" reads the right way. Top price levels
mirror phase-2 exactly.

Note: this is a **single-day signal**. The price has STILL risen +4.05%
over the 30-day window despite distribution today. Institutions can
distribute into strength while spot still grinds higher — this is the
mid-cycle late-rally pattern.

### Earnings play

**Skipped** — next earnings 2026-08-07 is ~80 days out, well outside the
default 14-day window. No earnings play to evaluate.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__insights_deep_dive` | symbol=XOM, date=2026-05-18 | Full snapshot returned; Yahoo fundamentals HTTP 401 (degraded) |
| `mcp__uw-pp__insights_signal_confluence` | direction=bullish, min-score=1, top-n=50, date=2026-05-18 | 50 results; **XOM absent**; score cutoff ≥5 reached |
| `mcp__uw-pp__insights_conviction_matrix` | symbol=XOM, date=2026-05-18 | **DISTRIBUTION**, confidence 15.78%, dp buy_ratio 0.342, call_bid>call_ask |
| `mcp__uw-pp__insights_price_vs_flow` | symbol=XOM, lookback-days=30, date=2026-05-18 | No divergence; price +4.05%, flow bullish, aligned |
| `mcp__uw-pp__insights_analyst_vs_flow` | symbol=XOM, date=2026-05-18 | Only flow side returned; analyst side missing (Yahoo 401) |
| `mcp__uw-pp__insights_institutional_accumulation` | symbol=XOM, date=2026-05-18 | **DISTRIBUTION** signal; sell volume 1.92× buy volume; VWAP $159.41 |
| `mcp__uw-pp__insights_earnings_play` | (skipped — next earnings 2026-08-07 >14d) | n/a |

## Tool errors

- `insights_deep_dive.yahoo_fundamentals.error`: `"yahoo quoteSummary XOM:
  HTTP 401"` — Yahoo's quoteSummary endpoint authentication failed. This
  blocks PE / market cap / short interest / institutional ownership fields
  from being populated. Phase-9 should rely on phase-6 SEC-derived
  fundamentals (EPS $1.16, $9.2B Q1 distribution, $20B 2026 buyback).
- `insights_analyst_vs_flow` returned only the flow half, presumably for
  the same Yahoo auth reason. Wall Street consensus rating + price target
  not available from UW; phase-8 analyst agents should WebSearch.

## Cross-check vs phases 1–6

| UW insight | Aligns with phase? | Notes |
|------------|-------------------|-------|
| `signal_confluence` (XOM absent) | **Phase-5 win-rate caveat agrees**; phase-3/4/6 disagree | The composite penalizes XOM for the DP distribution AND high IV rank. Tactically consistent with phase-5's 2/5 historical conviction. |
| `conviction_matrix` = DISTRIBUTION | **Phase-2 agrees strongly** (mega tier 95% sell); phase-3 disagrees (call OI build); phase-6 indirectly agrees ("institutions trimming into strength" + Energy sector inflow) | The split itself is the truth: stock-side distribution + options-side mixed bullish. |
| `price_vs_flow` (aligned bullish, no divergence) | Phase-1 agrees | Modest net flow consistent with phase-1's "mixed-with-slight-bullish" verdict. |
| `analyst_vs_flow` (partial) | n/a | Yahoo 401 blocks comparison. Phase-8 must source analyst data via WebSearch. |
| `institutional_accumulation` = DISTRIBUTION | **Phase-2 agrees strongly** | Independent confirmation of mega-tier sell skew via different aggregation method. |

**Net cross-check verdict:** UW's composite **REINFORCES PHASE-2 and PHASE-5**'s
cautious signals, **TEMPERS PHASE-3 and PHASE-4**'s bullish read at the
options-positioning layer, and **DOES NOT INVALIDATE PHASE-6**'s macro
tailwind (because rotation-flow tailwind doesn't require single-day DP
accumulation).

## Verdict for downstream phases

- **UW composite bias:** **NEUTRAL-TO-CAUTIOUSLY-BULLISH**. The
  options-positioning bull case (phase-3 OI + phase-4 GEX) is partially
  offset by:
  (1) DP distribution at current price levels
  (2) call bid-volume dominance in aggregate (despite ask-side dominance at
      key contracts)
  (3) failure to appear in top-50 bullish confluence list
  Reframed: this is **HEDGED_LONG / income-overlay positioning by
  institutions trimming into the rally**, not a clean DIRECTIONAL_LONG
  setup.
- **Conviction:** **4/5 on the COMPOSITE** (the multi-tool agreement on
  DISTRIBUTION is robust). The bullish options-side is real but tempered
  by the stock-side distribution.
- **Phase 9 should treat this as the baseline:** **the right trade
  structure is not "buy calls" — it's a *defined-risk bullish-biased
  structure that takes advantage of complacent skew (call IV > put IV)
  while limiting downside exposure to the DP distribution risk.* Examples:
  put credit spread (sell the OTM put + buy further OTM, collect premium),
  bull call spread (limited debit), or covered-call overlay if already
  long shares.**
- **Open questions:**
  - **Why is the same actor (institutions) DP-selling while writing covered
    calls and also buying upside calls?** Most likely answer: large
    accumulated position taking profit on shares + writing income calls +
    holding a small new directional bull bet via Jun'26 165C. Phase 8's
    Institutional Strategist agent should test this hypothesis.
  - **Could the DP sell skew be largely VWAP / ETF rebalance flow (XOM is
    ~22% of XLE; XLE saw heavy ETF flows on the back of the rotation)?**
    Phase 8's Macro / Sector agent should weigh in.
  - **What is the consensus analyst price target for XOM?** Yahoo failed —
    phase 8 must WebSearch (e.g., "XOM analyst price target consensus
    May 2026"). This datapoint is needed for the sizing rubric.
