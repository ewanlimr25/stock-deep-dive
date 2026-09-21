# Phase 7 — UW Insights Confluence

**Ticker:** RKT
**As-of date:** 2026-05-20 (data: 2026-05-19)
**Generated:** 2026-05-20T01:20:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-5-historical.md, phase-6-macro.md

## Summary

UW's composite insight stack delivers a **bearish-leaning verdict that
directly contradicts the phase-3 options-OI read**. The Conviction Matrix
scores RKT as **DIRECTIONAL_SHORT at 49.36% confidence**, citing dark pool
buy_ratio of 0.243 (well below the 0.40 bear threshold) and put-ask volume
(16,500) exceeding call-ask volume (13,616) [INSIGHT:conviction_matrix].
The Institutional Accumulation tool returns **DISTRIBUTION** (buy/sell
ratio 0.32; price down 12.28% over 30 days) [INSIGHT:institutional_accumulation].
Signal Confluence scores RKT BELOW 1 on BOTH the bullish and bearish lists
(RKT does not appear in the top 30 of either direction at min_score=1) —
meaning UW's composite does not see a clean directional confluence even
after factoring options + DP + OI [INSIGHT:signal_confluence]. Price-vs-Flow
shows **no divergence** ("price and flow are aligned" both bearish over
30 days) [INSIGHT:price_vs_flow]. Net read: the simple, machine-readable
view is "**bearish-distribution name** with mixed-signal confluence." The
sophisticated option-positioning bull thesis from phase-1 and phase-3 is
real but does not dominate the composite tape.

## Key signals

- **Conviction Matrix: DIRECTIONAL_SHORT at 49.36% confidence** —
  DP buy_ratio 0.243; put-ask vol > call-ask vol
  [INSIGHT:conviction_matrix].
- **Institutional Accumulation: DISTRIBUTION** — buy/sell ratio 0.32;
  3.1× more sell volume than buy volume; price -12.28% in 30d
  [INSIGHT:institutional_accumulation].
- **Signal Confluence: RKT not in top 30 bullish OR bearish at min_score=1**
  — composite score is < 1 on both sides; the signal stack is mixed/neutral
  [INSIGHT:signal_confluence].
- **Price vs Flow: no divergence, both bearish** — flow_direction
  "bearish", price -12.28%, period high $17.36 → close $13.18
  [INSIGHT:price_vs_flow].
- **Yahoo fundamentals unavailable** (`HTTP 401`) — no PE/short interest/
  market cap context this run [INSIGHT:deep_dive Tool errors].
- **Next earnings: 2026-07-30** (Q2; ~70 days out — outside near-term
  trade window) [INSIGHT:deep_dive].

## Detailed findings

### Deep dive snapshot (`insights_deep_dive`)

```
yahoo_fundamentals     : ERROR — HTTP 401
next_earnings_date     : 2026-07-30
iv30d                  : 0.6014  (60.1%)
iv_rank                : 34.26
implied_move (1d?)     : 0.544 ($) ≈ 4.30%
volatility (30d)       : 0.690 (69.0%)
put_call_ratio (today) : 0.98
total_open_interest    : 620,927
call_premium / put_premium : $2.87M / $3.16M (PUT-skewed)
bullish_premium / bearish_premium : $2.79M / $2.96M
darkpool total premium : $132.67M / 10.51M shares / 268 trades / avg $12.69
```

Top OI changes consistent with phase-3: Aug 14C +3,610, May-29 14C +2,643,
May-22 13P +1,368, Jan-28 10P +1,237, May-22 14C +978.

### Signal Confluence (`insights_signal_confluence`)

**Bullish direction (min_score=1, top_n=30):**

RKT is **NOT in the top 30** bullish names. Top names by score=5–6 include
SG, TE, DPST, WULF, WBD, USAS, HRL, AFL, CMBT, LQDA, SFM, YPF, MKC, SNXX,
RVMD. (Notable Financial Services bullish-confluence names: WULF and AFL —
not mortgage-related.)

**Bearish direction (min_score=1, top_n=30):**

RKT is also **NOT in the top 30** bearish names. Top bear names: BNTX,
EIX, FLEX, TOL, PSEC, DG, TIGR, HACK, TJX, FUTU, IPO, SMH (the chip ETF
SMH itself), ADM, NOW, ADI.

**Implication:** RKT's directional signal stack does not meet the score≥1
floor in either direction. This is **independent corroboration** of the
phase-5 finding that single-name signals in this regime are noisy — the
machinery cannot find a clean RKT direction call.

### Conviction matrix (`insights_conviction_matrix`)

```
symbol         : RKT
scenario       : DIRECTIONAL_SHORT
confidence_pct : 49.36
explanation    : "Dark pool selling + put buying — institutional bear bet."

dark_pool:
  buy_ratio    : 0.243        (below 0.40 bear threshold)
  buy_volume   : 2,553,087
  sell_volume  : 7,955,000
  trades       : 268

options_flow:
  call_ask_volume : 13,616
  call_bid_volume :  8,396
  put_ask_volume  : 16,500    (HIGHER than call_ask)
  put_bid_volume  :  5,900
```

The matrix reads:
- DP buy_ratio 0.243 < 0.40 → bearish DP
- put_ask > call_ask → bearish options flow
- Combination → DIRECTIONAL_SHORT

**Key caveat:** confidence is only 49.36% — barely above coin-flip. The
classifier is not high-conviction on either side. The phase-3 nuance
(put-ask volume INCLUDES protective collar legs, not just bearish bets) is
NOT captured by this composite.

### Price vs flow (`insights_price_vs_flow`)

```
period_high   : $17.36
period_low    : $12.38
price_start   : $15.02   (30d ago)
price_end     : $13.18   (yesterday — note: doesn't match 5/19 close of $12.675; uses Yahoo dated lag)
price_change_pct : -12.28%

flow_direction       : bearish (today)
net_premium_flow     : -$170,758
divergence           : false
divergence_signal    : "Price and flow are aligned"
```

**No divergence.** Both price and flow are pointing the same direction
(bearish). This removes the reversal-signal optionality that
divergence-based traders look for. The mechanical takeaway: do NOT
contrarian-buy this name purely on signal — the tape and price are
aligned.

### Analyst vs flow (`insights_analyst_vs_flow`)

```
options_flow:
  flow_sentiment : bearish
  net_flow       : -$170,758
  put_call_ratio : 0.98
  bullish_premium / bearish_premium : $2.79M / $2.96M
```

The analyst side returned no Yahoo data (consistent with the 401 error on
`deep_dive`). Phase-6 already covered: analyst sentiment is broadly
constructive (Overweight ratings, undervaluation thesis). The flow today
contradicts analyst consensus (analysts say "buy"; tape says "bearish").

### Institutional accumulation (`insights_institutional_accumulation`)

```
signal                    : DISTRIBUTION — dark pool sell volume
                             significantly exceeds buy volume
buy_sell_ratio            : 0.32
buy_side_volume           : 2,553,087
sell_side_volume          : 7,955,000
price_30d_change_pct      : -12.28%
vwap                      : $12.63
total_dp_volume           : 10,508,087 shares
total_dp_premium          : $132.67M

top_price_levels:
  $12.52 — $35.50M / 2.84M shares / 5 trades  (today's largest distribution)
  $12.60 — $25.28M / 2.01M shares / 2 trades  (today's secondary)
  $12.73 — $ 7.28M / 0.57M shares / 19 trades (most-pinged level)
  $12.55 — $ 6.60M / 0.53M shares / 4 trades
  $12.62 — $ 5.24M / 0.42M shares / 7 trades
```

The composite tool agrees with phase-2's verdict: this is DISTRIBUTION,
not accumulation. The 30-day decline of 12.28% accompanies a buy/sell
ratio of 0.32 — institutions are persistently lightening exposure.

### Earnings play

Skipped — next earnings 2026-07-30 is ~70 DTE, outside the standard
14-day window.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `insights_deep_dive` | `{symbol: RKT, date: 2026-05-19}` | OK (Yahoo fundamentals failed 401) |
| `insights_signal_confluence` | `{direction: bullish, top_n: 30, min_score: 1, date: 2026-05-19}` | RKT not in top 30 |
| `insights_signal_confluence` | `{direction: bearish, top_n: 30, min_score: 1, date: 2026-05-19}` | RKT not in top 30 |
| `insights_conviction_matrix` | `{symbol: RKT, date: 2026-05-19}` | DIRECTIONAL_SHORT @ 49.36% conf |
| `insights_price_vs_flow` | `{symbol: RKT, lookback_days: 30, date: 2026-05-19}` | no divergence; both bearish |
| `insights_analyst_vs_flow` | `{symbol: RKT, date: 2026-05-19}` | flow bearish; analyst side missing |
| `insights_institutional_accumulation` | `{symbol: RKT, date: 2026-05-19}` | DISTRIBUTION; b/s ratio 0.32 |

## Tool errors

- `insights_deep_dive.yahoo_fundamentals`: `HTTP 401` — Yahoo
  quoteSummary API rejection. Falls back gracefully to UW-native data
  (screener + DP + OI), which is sufficient for this run. Phase-6 covered
  the fundamentals (Q1 results, Mr. Cooper deal).
- `insights_analyst_vs_flow.analyst_recommendations`: missing — Yahoo
  401 cascades here. Phase-6 already captured analyst stance as
  "Overweight / undervalued" via WebSearch.

## Cross-check vs phases 1–6

| UW insight | Phase agreement? | Notes |
|------------|------------------|-------|
| `signal_confluence` bullish | **DISAGREE w/ phase 1** | Phase 1 read tape as bullish-tilt (sweep persistence 5/5). UW composite scores RKT < 1 (out of top 30). The discrepancy comes from the UW composite weighting DP buy_ratio (0.24) heavily. |
| `signal_confluence` bearish | DISAGREE w/ phase 2 narrowly | Phase 2 was distribution-clear, but the composite doesn't put RKT in the top 30 bears either. Mixed reading. |
| `conviction_matrix` DIRECTIONAL_SHORT | **AGREE w/ phase 2** (DP), **DISAGREE w/ phase 3** (OI) | UW privileges DP over the options-OI structural bull case. |
| `institutional_accumulation` DISTRIBUTION | **STRONG AGREE w/ phase 2** | Same data, same conclusion. |
| `price_vs_flow` no divergence | AGREE w/ phase 5 trend | 19 bearish vs 9 bullish days corroborates aligned-bearish stance. |
| `analyst_vs_flow` | Inconclusive (no Yahoo) | Phase 6 captured the analyst-flow contradiction separately. |

**Composite gap:** UW's machine read of the tape sees DISTRIBUTION +
DIRECTIONAL_SHORT. The deep human read (phases 1+3) sees stock-to-LEAPS
conversion. Both can be simultaneously true — the same desk(s) may be
liquidating stock while building optional upside. But the dominant cash
flow direction TODAY is bearish on stock, period.

## Verdict for downstream phases

- **UW composite bias:** **bearish (DIRECTIONAL_SHORT)** at 49% confidence
  + **distribution-confirmed**.
- **Conviction:** 3/5 on direction — high agreement with phases 2, 5, 6,
  but low absolute confidence in the matrix output (49%).
- **Phase-9 must reconcile the contradiction:** the options-positioning
  bull thesis (phase 1, 3) versus the UW composite + dark pool + price
  trend bearish thesis (phase 2, 5, 6, 7). Two valid resolutions:
  1. **"Sell the stock, monetize the options":** the marginal flow is
     selling-driven; near-term price grinds lower. The options book is
     someone else's structural bet, not the current driver.
  2. **"Distribution exhausts itself":** after $132M of one-day DP
     volume and 28 days of grind-lower, the seller may be near done. The
     phase-1 LEAPS + Aug 14C buyer is positioned for the post-seller
     bounce.

  **Phase 9 should NOT pick a single side; instead, structure for the
  binary outcome around the 5/22 catalyst window with defined risk.**
- **Open questions:**
  - Does dealer GEX flip back to clean positive on 5/20 — i.e., is the
    short-gamma phase over? (would have to be re-run live)
  - Is the 5/22 catalyst resolved upward (LEAPS bull thesis pays out) or
    downward (distribution accelerates)?
  - Are there any short-interest / borrow-cost signals to suggest a
    forced-cover candidate? (out of scope for this run)
