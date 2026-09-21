# Phase 7 — UW Insights Confluence

**Ticker:** FSLY
**As-of date:** 2026-05-19  (Effective data date: 2026-05-18)
**Generated:** 2026-05-19T01:10:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-5-historical.md

## Summary

UW's composite engine produces a **strongly cohesive but unambitiously
bullish** picture. The headline call is the conviction matrix's
**COVERED_CALL** scenario [INSIGHT:conviction_matrix]: dark-pool BUY
volume of 628K shares vs SELL 279K (ratio 2.25) PAIRED with options-flow
showing **call_bid_vol (3,534) > call_ask_vol (2,858)** — institutions
are accumulating stock AND simultaneously writing calls for yield. That
single classification reconciles every apparent tension in phases 1-3
(why is bid-side call activity so large alongside ask-side calls and DP
block buys?). `insights_institutional_accumulation` independently
confirms ACCUMULATION on the equity side
[INSIGHT:institutional_accumulation]. However, FSLY does **NOT appear in
either side of the market-wide signal confluence list (min_score=1,
top_n=50)** [INSIGHT:signal_confluence] — meaning per UW's standard
threshold (score ≥ 4), FSLY's signal stack doesn't aggregate to "stand-
out conviction" in either direction. The result: a clean, lower-tempo
"covered_call / wheel" thesis rather than a screaming directional long.

## Key signals

- **Conviction matrix = COVERED_CALL** with confidence 24.51%
  [INSIGHT:conviction_matrix]. Plain-English read from the tool: "Dark
  pool buying + call selling — yield enhancement, capping upside."
  This is the cleanest single label of the day.
- **Institutional accumulation signal = ACCUMULATION** (2.25× buy/sell
  ratio, VWAP $16.57) [INSIGHT:institutional_accumulation] — confirms
  phase-2 block-buy read.
- **FSLY absent from the bullish AND bearish top-50 confluence lists**
  at min_score=1 [INSIGHT:signal_confluence] — the per-axis signals
  don't combine to ≥4 in UW's framework. This is itself a "mixed
  composite" finding.
- **Price vs flow: NO divergence.** 30d price change −49.24%; current
  flow direction bearish (−$8K net premium 5/18)
  [INSIGHT:price_vs_flow]. No reversal trigger from this lens.
- **Confirmed Q2 2026 earnings date: 2026-08-05** [INSIGHT:deep_dive
  screener.next_earnings_date] — 78 days out, outside the standard
  pre-earnings window (skipping `insights_earnings_play`).
- **Yahoo fundamentals call failed** (HTTP 401)
  [INSIGHT:deep_dive yahoo_fundamentals.error] — surfaced verbatim
  under tool errors; phase-8 sub-agents may have to fill in
  PE/cash/debt manually.

## Detailed findings

### Deep-dive snapshot

`insights_deep_dive`, symbol=FSLY, date=2026-05-18:

| Section | Field | Value |
|---|---|---|
| UW dark pool | total_premium | $15,042,199 |
| | total_shares | 907,902 |
| | avg_price | $16.61 |
| | trade_count | 37 |
| UW screener | iv30d | 81.3% |
| | iv_rank | 42.35 |
| | total_open_interest | 214,439 |
| | put_call_ratio | 0.4034 |
| | implied_move ($) | $1.20 |
| | implied_move_pct | 7.18% |
| | next_earnings_date | **2026-08-05** |
| | volatility | 1.012 (front-week IV) |
| | call_premium | $1,019,296 |
| | put_premium | $408,206 |
| | bullish_premium | $620,656 |
| | bearish_premium | $628,811 |
| Top OI changes | (5 rows — already in phase-3) | — |
| Yahoo fundamentals | error | **HTTP 401** |

The 5/22 implied move of $1.20 (7.2%) brackets the 117.7% IV print
from phase-4. Over 4 sessions, ~$1.20 absolute is a wide expected
range. **A 1× implied move down = $15.43** (matches phase-3's $15
put-selling line). **A 1× implied move up = $17.83** (just under
phase-4's $17.50 magnet, between magnet and the next resistance).

### Signal confluence — FSLY absent both lists

`insights_signal_confluence`, direction=bullish, min_score=1, top_n=50:
**FSLY absent.** 50 tickers returned, lowest score = 5. JBS, TE, CZR,
KVUE, GAU, BROS, MNST scored 6 (perfect bullish stack). DUOL, PLTR,
QRVO, CTSH are the top tech names that DID make the list.

`insights_signal_confluence`, direction=bearish, min_score=1, top_n=50:
**FSLY absent.** 50 tickers returned, lowest score = 4. Bearish tech
standouts: SMH (5), CIEN, ZM, P, ADI, ON, FLEX, KEYS, GFS (all 4).

**Interpretation.** FSLY's individual axes (bullish flow, low PCR, DP
accumulation, OI building, low IV) score MIXED. Some are bullish
(low_pcr, dp_accumulation, oi_building), some are neutral (iv_rank
mid-range), and some show two-sided activity (the call-writing on
the bid offsets the bullish_flow). The composite doesn't cleanly
aggregate into either list — exactly the "mixed" reading the
covered-call scenario implies.

### Conviction matrix — **COVERED_CALL**

`insights_conviction_matrix`, symbol=FSLY:

| Field | Value |
|---|---|
| **scenario** | **COVERED_CALL** |
| confidence_pct | 24.51% |
| explanation | "Dark pool buying + call selling — yield enhancement, capping upside" |
| DP buy_ratio | 0.692 |
| DP buy_volume | 628,463 |
| DP sell_volume | 279,439 |
| call_ask_volume | 2,858 |
| **call_bid_volume** | **3,534** |
| put_ask_volume | 1,043 |
| put_bid_volume | 1,398 |
| thresholds | bull 0.6 / bear 0.4 |

**The single most important table in phase 7.** Three facts reconcile
into one institutional posture:

1. DP is BUYING (ratio 0.692, above 0.6 bull threshold).
2. Options-flow is **NET CALL-SELLING** (3,534 bid vs 2,858 ask).
3. Options-flow is also **NET PUT-SELLING** (1,398 bid vs 1,043 ask).

That trifecta = "buy the stock, sell premium against it (both sides)."
This is institutional **wheel / covered-call yield-enhancement
strategy** at $16.50 area. It is bullish-leaning (the stock leg is
long), but the upside is *intentionally* capped via short calls,
which is why phase-3 surfaced new bid-side $20 / $22.5 / $23 / $45
call write OI.

Confidence is LOW (24.51%) because the front-week vol is rich (117%)
and the broader regime is hostile (phase-6). A pro desk doing this
trade would size accordingly.

### Price vs flow — no divergence

`insights_price_vs_flow`, lookback_days=30:

| Field | Value |
|---|---|
| **divergence** | **false** |
| divergence_signal | "Price and flow are aligned" |
| price_start (30d ago) | $32.75 |
| price_end | $16.63 |
| **price_change_pct (30d)** | **−49.24%** |
| period_high | $34.82 |
| period_low | $16.35 |
| flow_direction (latest) | bearish |
| net_premium_flow (latest) | −$8,155 |

Price is down −49% and flow is mildly bearish today. **No divergence**
= no contrarian reversal trigger from this lens. Note that today's
−$8K net flow is *tiny* — effectively neutral. The 30d picture has
already played out (the −38% earnings crash); current flow is the
mop-up phase.

### Analyst vs flow

`insights_analyst_vs_flow`, symbol=FSLY:

| Field | Value |
|---|---|
| flow_sentiment | bearish |
| net_flow | −$8,155 |
| put_call_ratio | 0.4034 |
| analyst recommendations | **NOT RETURNED by tool** |

The tool returned only the options-flow side and omitted the analyst
recommendation block — consistent with the Yahoo HTTP 401 error from
`insights_deep_dive`. Wall Street consensus will need to come from
phase-8 sub-agents using WebSearch or other sources.

### Institutional accumulation — **ACCUMULATION**

`insights_institutional_accumulation`, symbol=FSLY:

| Field | Value |
|---|---|
| **signal** | **ACCUMULATION — dark pool buy volume significantly exceeds sell volume** |
| buy_sell_ratio | **2.25** |
| buy_side_volume | 628,463 |
| sell_side_volume | 279,439 |
| total_dp_premium | $15,042,199 |
| total_dp_volume | 907,902 |
| vwap | $16.57 |
| price_30d_change_pct | −49.24% |

| Price level | Premium | Shares | Trades |
|---|---|---|---|
| $16.48 | $3,490,464 | 211,800 | 3 |
| $16.53 | $3,066,315 | 185,500 | 1 |
| $16.52 | $1,486,619 | 89,982 | 6 |
| $16.55 | $1,405,095 | 84,900 | 6 |
| $16.60 | $1,113,370 | 67,062 | 1 |

The price-level clustering at $16.48-$16.60 is precisely where the
DP accumulation is occurring. **VWAP $16.57** is the institutional
"fair fill" right now — anything below that is a discount to the
recent institutional cost basis.

### Earnings play

Skipped — next earnings 2026-08-05 (78 days out, outside the 14-day
default window for `insights_earnings_play`).

## Tool calls (audit trail)

| Tool | Args | Result summary |
|---|---|---|
| `mcp__uw-pp__insights_deep_dive` | symbol=FSLY, date=2026-05-18 | $15M DP; 81.3% IV; Q2 earn 8/5; **Yahoo fundamentals 401** |
| `mcp__uw-pp__insights_signal_confluence` | direction=bullish, min_score=1, top_n=50, date=2026-05-18 | FSLY ABSENT from top-50 |
| `mcp__uw-pp__insights_signal_confluence` | direction=bearish, min_score=1, top_n=50, date=2026-05-18 | FSLY ABSENT from top-50 |
| `mcp__uw-pp__insights_conviction_matrix` | symbol=FSLY, date=2026-05-18 | **COVERED_CALL** scenario, 24.5% confidence |
| `mcp__uw-pp__insights_price_vs_flow` | symbol=FSLY, lookback_days=30, date=2026-05-18 | No divergence; 30d −49.24% |
| `mcp__uw-pp__insights_analyst_vs_flow` | symbol=FSLY, date=2026-05-18 | Flow only; no analyst block returned |
| `mcp__uw-pp__insights_institutional_accumulation` | symbol=FSLY, date=2026-05-18 | **ACCUMULATION**, 2.25× buy/sell |
| `mcp__uw-pp__insights_earnings_play` | (not called — earnings 78d out) | skipped |

## Tool errors

`insights_deep_dive` returned `yahoo_fundamentals.error = "yahoo
quoteSummary FSLY: HTTP 401"`. Yahoo's quoteSummary endpoint requires
either auth or rate-limit handling we can't apply from here. Impact:
no PE, market cap, balance sheet, or short interest in this phase.
Phase-8 sub-agents will need to source these from WebSearch /
filings if any analyst-view requires them.

`insights_analyst_vs_flow` returned only the flow block, omitting
analyst consensus — consistent with the same Yahoo auth issue.
**Wall Street view is unavailable through UW today.**

## Cross-check vs phases 1-5

| UW insight | This phase says | Upstream agreement | Notes |
|---|---|---|---|
| signal_confluence (bullish) | FSLY absent (score < 4) | Mild **DISAGREE** with phase-1 verdict "bullish conviction 3.5/5" | UW's threshold for "stand-out" is higher than individual axis bullishness |
| signal_confluence (bearish) | FSLY absent (score < 4) | AGREE with phase-3 "bullish skew on new positioning" | FSLY is not bear-flagged either |
| **conviction_matrix = COVERED_CALL** | Yield enhancement, capping upside | **STRONG AGREE** with phase-1 (bid-side call writes at $20, $22.5, $23) + phase-2 (DP block buys) + phase-3 (+300 OI new write at 5/29 $23) | Best single label of the run |
| price_vs_flow = no divergence | Aligned | AGREE with phase-5 (90d net flow +$9.9M but recent days mixed) | No reversal trigger |
| analyst_vs_flow | Yahoo missing | n/a — gap | Phase-8 fills |
| **institutional_accumulation = ACCUMULATION** | 2.25× buy/sell | **STRONG AGREE** with phase-2 (block buy_ratio 0.847; 371K shares accumulation at 15:12) | Same DP data viewed two ways |

The most important finding here: **the COVERED_CALL classification
explicitly resolves the apparent contradiction in phase-1** between
ask-side call buying and bid-side call writing. They are the same
players doing both legs of a single thesis — long stock, short calls.

## Verdict for downstream phases

- **UW composite bias:** mildly bullish (COVERED_CALL is a long-stock
  scenario by definition, just income-skewed). Not a directional rip
  case.
- **Conviction:** 3.5 / 5 — the cross-tool agreement is strong, but
  the overall confidence_pct of 24.51 and the absence from market-
  wide confluence lists tempers it.
- **Treatment for phase 9:**
  - Use COVERED_CALL as the **baseline trade thesis**: own the
    underlying (or risk-equivalent), sell calls into the campaign
    target strikes ($20 / $22.5).
  - Override only if phase-8 sub-agents surface (a) a credible
    near-term catalyst that would re-rate, (b) institutional
    accumulation that breaks the 2.25× ratio markedly higher,
    or (c) macro flip from "tech outflow" to "tech inflow."
- **Open questions for phase 8:**
  - What is Wall Street consensus and PT distribution? (Yahoo
    failed.)
  - Is the FMR LLC 7.77M-share position (phase-6) still in 13F
    as of latest filing, or has it been pared?
  - Are there sell-side notes referencing $20 as a target (which
    would corroborate the call-write strike choice)?
  - Has any analyst recommended a wheel / collar on FSLY publicly?
