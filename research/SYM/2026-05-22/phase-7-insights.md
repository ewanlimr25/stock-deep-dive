# Phase 7 — UW Insights Confluence

**Ticker:** SYM
**As-of date (effective):** 2026-05-21
**Generated:** 2026-05-22T15:21Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-5-historical.md

## Summary

UW composite tools call the SYM setup **DIRECTIONAL_LONG with LOW
confidence (18.39%)** [INSIGHT:conviction_matrix]. The matrix verdict
is driven by dark-pool buy_ratio 0.672 (phase-2 agreement) plus a
slight net call-ask volume excess (779 ask vs 743 bid). Independently,
`insights_institutional_accumulation` labels SYM **ACCUMULATION** with
buy/sell ratio **2.05** and notes "dark pool buy volume significantly
exceeds sell volume" [INSIGHT:institutional_accumulation]. The
`insights_price_vs_flow` tool reports **no divergence** — flow
direction is bearish today, price is flat-to-down over 30d, the two
are aligned [INSIGHT:price_vs_flow]. **SYM does NOT appear in
`insights_signal_confluence` top-100 in either bullish or bearish
direction** (min_score=1) — composite screens treat the name as
**neutral** because today's net premium is bearish (−$183K) which
knocks out the `bullish_flow` factor, but distribution-side factors
aren't strong enough to make the bearish list either.
`insights_analyst_vs_flow` returned **no analyst component** (yfinance
HTTP 401) — Wall Street agreement can't be tested. `insights_deep_dive`
also lost the yfinance fundamentals leg (HTTP 401) but confirmed UW
screener: **next earnings 2026-08-05** (75 days out, out of
earnings-play window), IV rank 5.79, implied move 3.20%, total OI
55,612, PCR 0.489. **Net composite: mildly bullish from accumulation
signals, neutral-to-mixed everywhere else. Confidence is genuinely
low — phase-9 should not lean on this as the sole anchor.**

## Key signals

- **Scenario = DIRECTIONAL_LONG**, confidence 18.39%, dark-pool
  buy_ratio 0.672, call ask/bid 779/743
  [INSIGHT:conviction_matrix].
- **Institutional ACCUMULATION**: buy/sell 2.05, total DP premium
  $1.82M, vwap $50.47, top price levels $50.82/$50.40/$50.06/$50.72/$51.00
  [INSIGHT:institutional_accumulation].
- **No price–flow divergence**: flow_direction bearish (today), 30d
  price change −1.22%, period high $67.08, period low $44.20
  [INSIGHT:price_vs_flow]. Aligned = no reversal warning.
- **SYM absent from bullish AND bearish signal_confluence top-100**
  [INSIGHT:signal_confluence] — composite-screen neutral.
- **Earnings out of window**: next earnings 2026-08-05, 75 DTE
  [INSIGHT:deep_dive] — no pre-earnings play setup.

## Detailed findings

### Deep dive snapshot

| Field | Value |
|-------|-------|
| symbol | SYM |
| next_earnings_date | **2026-08-05** (75 DTE) |
| iv30d | 0.6323 |
| iv_rank | **5.79** |
| volatility (realized) | 0.8998 |
| implied_move ($) | 1.63 |
| implied_move (%) | **3.20%** |
| put_call_ratio | 0.4889 |
| call_volume / put_volume | 1,628 / 796 |
| call_premium / put_premium | $703K / $231K |
| bullish_premium / bearish_premium | $326,928 / $510,233 |
| total_open_interest | 55,612 |
| dark_pool total_premium / shares / trades | $1.82M / 36,148 / 13 |
| Yahoo fundamentals | HTTP 401 (paid leg blocked) |

The IV rank of **5.79** is the most striking number in the snapshot —
SYM's IV is at the bottom of its 1-year band, consistent with
phase-5's IV percentile 10.34.

Top OI changes (mirrors phase-3 + adds the LEAP P42.5):

| Contract | DTE | Strike | OI Δ | Vol |
|----------|-----|--------|------|-----|
| SYM 2026-05-22 C53 | 1 | 53 | +404 | 431 |
| SYM 2026-05-22 C52 | 1 | 52 | +113 | 120 |
| SYM 2027-01-15 C50 | 239 | 50 | +110 | 114 |
| SYM 2027-01-15 P42.5 | 239 | 42.5 | +93 | 106 |
| SYM 2026-05-29 C52 | 8 | 52 | +87 | 169 |

### Signal confluence (bullish + bearish, min_score=1, top-100 each)

**SYM is not in either list.** Highest-conviction bullish names today
score 6/6 (ARRY, CGNX, WGS, SN, CMPS). Highest bearish names score 5
(GSG, EWG, SMTC, MDB, XOVR). The composite scorer requires multiple
factors firing simultaneously; SYM is missing `bullish_flow` (today's
net is bearish) and `volume_spike` (modest volume, total ~2,400
contracts on the day) — those gaps kept it off both lists. This is a
**fair characterization** of phases 1-5: real but mixed.

### Conviction matrix

| Field | Value |
|-------|-------|
| **scenario** | **DIRECTIONAL_LONG** |
| confidence_pct | **18.39** |
| dark_pool buy_ratio | 0.672 |
| dark_pool buy_volume | 24,294 |
| dark_pool sell_volume | 11,854 |
| dark_pool trades | 13 |
| call_ask_volume | 779 |
| call_bid_volume | 743 |
| put_ask_volume | 281 |
| put_bid_volume | 418 |
| explanation | *"Dark pool buying + aggressive call purchases — institutional directional bet."* |

Note: the call ask/bid count (779/743) reads net buying of calls by
**contract count**, but phase-1 showed that by **premium-weighted**,
calls were net bid-side (the $66K Jan-27 50C bid + $51K Jan-28 60C bid
dominated). The composite tool reconciles by contract count, which
gives a different read. **Phase-9 must hold both: contract-count flow
is mildly net-bought; premium-weighted flow is mildly net-sold.** The
puts side is unambiguous though — put_bid_volume (418) > put_ask_volume
(281), meaning **puts were net SOLD** today. Selling puts is a
bullish positioning by customers → dealers are short puts → dealer
hedge is to buy underlying. Combines with the DEX +$33.6M finding
in phase-4 [STRUCT:dex].

### Price vs flow

| Field | Value |
|-------|-------|
| flow_direction | bearish |
| divergence | **false** |
| divergence_signal | *"Price and flow are aligned"* |
| net_premium_flow | −$183,305 |
| price_change_pct | −1.22% |
| period_high | $67.08 |
| period_low | $44.20 |
| iv_rank | 5.79 |

No reversal warning. Both sides agree on a mildly negative bias
within a wide $44.20 → $67.08 range (lookback 30d, which crosses the
$45 capitulation low).

### Analyst vs flow

Returned only the flow side (yfinance HTTP 401 prevented analyst pull):

| Field | Value |
|-------|-------|
| options_flow.flow_sentiment | bearish |
| options_flow.bullish_premium | $326,928 |
| options_flow.bearish_premium | $510,233 |
| options_flow.net_flow | −$183,305 |
| options_flow.put_call_ratio | 0.489 |

**Analyst consensus could not be retrieved.** Phase-9 should fold in
the Walmart-backlog WebSearch findings from phase-6 as a proxy for
"the Street view" — even without yfinance, the qualitative analyst
narrative is: Q2 beat, but Q3 guide is sequentially down. That's
already in phase-6.

### Institutional accumulation

| Field | Value |
|-------|-------|
| **signal** | **ACCUMULATION** |
| explanation | *"dark pool buy volume significantly exceeds sell volume"* |
| buy/sell ratio | **2.05** |
| buy_side_volume | 24,294 |
| sell_side_volume | 11,854 |
| dark_pool trades | 13 |
| vwap | $50.47 |
| total_dp_premium | $1.82M |
| total_dp_volume | 36,148 |
| price_30d_change_pct | −1.22% |

Top price levels (single-day, mirrors phase-2):

| Level | Premium | Shares | Trades |
|-------|---------|--------|--------|
| $50.82 | $221,868 | 4,366 | 2 |
| $50.40 | $201,600 | 4,000 | 1 |
| $50.06 | $195,584 | 3,907 | 1 |
| $50.72 | $161,543 | 3,185 | 1 |
| $51.00 | $153,867 | 3,017 | 1 |

The single-day picture confirms phase-2: clusters at $50.40, $50.72,
$50.82, $51.00 are all *above* the day's VWAP — net buying happened at
prices above mid-VWAP, the strongest version of dark-pool buy-side
signal.

### Earnings play

**Not applicable.** `insights_earnings_play` was skipped because
next earnings is 75 days out (per `insights_deep_dive`
next_earnings_date=2026-08-05) — well outside the 14-day default
window of the earnings_play tool.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `insights_deep_dive` | symbol=SYM, date=2026-05-21 | next earnings 2026-08-05; yfinance fundamentals HTTP 401 |
| `insights_signal_confluence` | direction=bullish, min-score=1, top-n=100 | SYM not in top 100 |
| `insights_signal_confluence` | direction=bearish, min-score=1, top-n=100 | SYM not in top 100 |
| `insights_conviction_matrix` | symbol=SYM, date=2026-05-21 | DIRECTIONAL_LONG, confidence 18.39% |
| `insights_price_vs_flow` | symbol=SYM, lookback-days=30 | no divergence, flow bearish, price −1.22% |
| `insights_analyst_vs_flow` | symbol=SYM | flow side only, analyst missing |
| `insights_institutional_accumulation` | symbol=SYM, date=2026-05-21 | ACCUMULATION, buy/sell 2.05 |
| `insights_earnings_play` | (not called) | out of window (75 DTE) |

## Tool errors

- `insights_deep_dive` → yfinance `quoteSummary SYM: HTTP 401` —
  expected per skill rules (no paid data).
- `insights_analyst_vs_flow` returned only the options_flow leg; no
  analyst consensus surfaced (likely same yfinance restriction).

## Cross-check vs phases 1-5

| UW insight | Phase agreement? | Notes |
|------------|------------------|-------|
| `signal_confluence` (bullish/bearish, top-100) | **Agree** with phases 1-5 mixed read | SYM neutral in both directions = phases told a mixed-mild story |
| `conviction_matrix` = DIRECTIONAL_LONG | **Agree with phase-2**, **partial conflict with phase-1** | Phase-2 DP buy_ratio 0.672 → bullish. Phase-1 by premium was bid-side LEAP calls (slightly bearish); by contract count calls were net bought. Same data, different normalization. |
| `institutional_accumulation` = ACCUMULATION | **Strong agreement with phase-2** | Identical buy/sell numbers (24,294 / 11,854), same ratio (2.05 ≈ 0.672 buy_ratio) |
| `price_vs_flow` no divergence | **Agree** with phases 1-5 | No reversal warning; phases were not flagging one either |
| `earnings_play` | Out of window | Phase-6 confirmed earnings was 2026-05-06, ~75 days to next |

**Contradictions to surface to phase-10:**
1. Composite says DIRECTIONAL_LONG; phase-1 by *premium* says
   mild-bearish on LEAP calls.
2. Phase-3 inferred ONE bearish OI build (Jan-27 C50 bid-side
   net_ask_bid −25); composite call count says calls net bought 779 vs
   743 (+36). Different aggregation rules — both can be true.

## Verdict for downstream phases

- **UW composite bias:** **mild DIRECTIONAL_LONG via accumulation,
  capped by low confidence (18.39%) and absent signal confluence.**
- **Conviction:** 3/5. Composite tools are internally consistent
  (DP + accumulation agree). They mildly disagree with phase-1's
  premium-weighted LEAP-call reading — but phase-1 conviction was
  also only 2/5 there, so this isn't a hard collision.
- **Phase-9 baseline:** **mildly bullish on accumulation + low IV
  reset + positive gamma**, sized half because composite confidence
  is low and macro is a headwind. Override the composite "directional
  long" framing only with phase-4/5-specific evidence (positive GEX
  walls, regime flip, vol-crush context).
- **Open questions:**
  - The Yahoo / analyst consensus leg is dark. Phase-9 should fall
    back to the Walmart-deal qualitative narrative from phase-6 as
    the secular anchor, not from `insights_analyst_vs_flow`.
  - The composite's DIRECTIONAL_LONG label with 18.39% confidence is
    structurally below the bar for a high-conviction setup. Phase-9
    should default to **defined-risk / partial-size structures**.
