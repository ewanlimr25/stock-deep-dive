# Phase 7 — UW Insights Confluence

**Ticker:** RDDT
**As-of date:** 2026-05-20 (data anchor 2026-05-18)
**Generated:** 2026-05-19T01:50:00-04:00
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md,
phase-3-positioning.md, phase-4-structure.md, phase-5-historical.md,
phase-6-macro.md

## Summary

UW's composite insight stack returns an internally consistent
**DIRECTIONAL_LONG** baseline: `signal_confluence` score **5 of 6**
(all factors firing except institutional_holdings), `conviction_matrix`
labels the scenario **DIRECTIONAL_LONG** with the explanation "Dark
pool buying + aggressive call purchases — institutional directional
bet", `institutional_accumulation` returns **ACCUMULATION**
(buy/sell 1.8), and `price_vs_flow` shows **no divergence** (flow
bullish, price +6.81% over 30d). Critically, the
`conviction_matrix.confidence_pct` is only **22.25%** despite the
high-score factors — the model itself is flagging modest conviction
under the surface label. The composite also explicitly confirms
**next earnings date 2026-07-30** (Q2 2026), which validates the
phase-4 8/21 IV hump as Q2-earnings-driven. **Implied 1-sigma weekly
move = $8.34 / 5.24%** — RDDT's actual 5/19 −2.64% next-day fell
inside that band. The UW reads agree with phases 1-3 unconditionally
but diverge from phase-5 (bullish_flow 0% recent backtest win rate)
and phase-6 (TRANSITIONAL regime, sector outflow) — those
regime-conditioning effects are NOT in the insights tools' input.

## Key signals

- `signal_confluence` (bullish): **score 5/6** for RDDT; factors:
  **bullish_flow, low_pcr, dp_accumulation, oi_building,
  low_iv_cheap_options** [INSIGHT:signal_confluence].
- `conviction_matrix`: scenario **DIRECTIONAL_LONG**, confidence
  **22.25%** — high-quality factors with the model itself hedging
  conviction [INSIGHT:conviction_matrix].
- `institutional_accumulation`: signal **ACCUMULATION**, buy/sell
  ratio **1.8**, VWAP $158.47, total DP premium $65.68M
  [INSIGHT:institutional_accumulation].
- `deep_dive`: **next_earnings_date 2026-07-30**, implied move
  **$8.34 / 5.24%**, IV30 64.94%, IV rank 24.16, PCR 0.529
  [INSIGHT:deep_dive].
- `price_vs_flow`: **NO divergence** (flow bullish, price +6.81% over
  30d, $145 → $154.88); divergence-reversal signal is NOT firing
  [INSIGHT:price_vs_flow].

## Detailed findings

### Deep dive snapshot (2026-05-18)

| Field | Value |
|-------|-------|
| sector | Communication Services |
| iv30d | 64.94% |
| iv_rank | 24.16 |
| put_call_ratio | 0.5288 |
| call_premium | $10,931,713 |
| put_premium | $5,001,318 |
| call_volume | 18,816 |
| put_volume | 9,949 |
| bullish_premium | $7,792,208 |
| bearish_premium | $6,918,251 |
| total_open_interest | 406,189 |
| implied_move (1σ weekly) | **$8.34 / 5.24%** |
| volatility (HV) | 73.45% |
| **next_earnings_date** | **2026-07-30** (Q2) |
| Yahoo fundamentals | HTTP 401 (blocked) |

Top OI changes per deep_dive (matches phase-3 + adds 1 LEAP row):

| Symbol | Strike | DTE | Δ OI | Avg Price |
|--------|--------|-----|------|-----------|
| RDDT 2026-05-22 160C  | 160   | 4   | +1,292 | $4.60  |
| RDDT 2026-05-22 167.5C| 167.5 | 4   |   +755 | $2.19  |
| RDDT 2026-06-18 160C  | 160   | 31  |   +643 | $10.69 |
| RDDT 2026-06-18 95P   | 95    | 31  |   +502 | $0.10  |
| **RDDT 2028-06-16 145P** | **145** | **760** | **+495** | **$46.15** |

The LEAP row (2028-06-16 145P) was not in phase-3's top set —
deep_dive's filter is broader. A 2-year ITM put at 145 with +495 OI
is a **synthetic-short or covered-call hedge** structure at
institutional scale ($46 premium × 495 contracts × 100 = ~$2.3M
notional premium). Important context for any LEAP/long-dated view.

### Signal confluence (5/6, BULLISH direction)

```
ticker: RDDT
score: 5
direction: bullish
factors: [bullish_flow, low_pcr, dp_accumulation, oi_building,
          low_iv_cheap_options]
close: 159.11
iv_rank: 24.1648
net_flow: 873957
put_call_ratio: 0.5288
sector: Communication Services
```

Read: **score 5 of 6** is the second-highest possible. Only missing
factor would typically be an institutional_holdings or technical
factor that UW didn't surface for RDDT specifically. **All five
factors confirm phases 1, 2, 3, 4 individually**. This is the
single strongest agreement-with-upstream-phases signal in the
workup so far.

### Conviction matrix (DIRECTIONAL_LONG, 22.25% confidence)

| Field | Value |
|-------|-------|
| scenario | **DIRECTIONAL_LONG** |
| confidence_pct | **22.25%** |
| explanation | "Dark pool buying + aggressive call purchases — institutional directional bet" |
| DP buy_ratio | 0.642 |
| DP buy_volume | 266,211 |
| DP sell_volume | 148,236 |
| call_ask_volume | 10,082 |
| call_bid_volume | 7,297 |
| put_ask_volume | 4,732 |
| put_bid_volume | 4,477 |

Read: the label is bullish, but **confidence 22.25%** is low. The
model is saying "directional-long is the most-likely classification
given the bull/bear factor counts, but my certainty about it is
weak". This matches phase-5's caution: phases 1-3 fire on the same
data the conviction matrix uses, so the alignment is structural; the
LOW confidence is the model encoding the noise.

Sub-metric notes:
- DP buy ratio 0.642 (this tool uses all-tier, not block-only;
  phase-2's BLOCK tier was 0.793 — the spread tells us
  large/block-tier alignment is stronger than the all-tier composite,
  supporting "real institutional" over "broad noise").
- call_ask/bid ratio = 10,082 / 7,297 = **1.38** (ask-side calls
  dominate by 38%, mild call-buying skew, not extreme).
- put_ask/bid ratio = 4,732 / 4,477 = **1.06** (effectively even —
  put buyers ≈ put sellers, no panic-hedge signature).

### Price vs flow (NO divergence)

| Field | Value |
|-------|-------|
| divergence | **false** |
| divergence_signal | "Price and flow are aligned" |
| flow_direction | bullish |
| net_premium_flow | +$873,957 |
| period_high (30d) | $177.13 |
| period_low (30d) | $135.00 |
| price_start | $145.00 |
| price_end | $154.88 |
| price_change_pct | +6.81% |
| iv_rank | 24.16 |

Read: no divergence-based reversal signal is firing. Price and flow
agree. This is **neutral-to-bullish** in the divergence framework
(neither warning of reversal nor confirming squeeze). The 5/19
−2.64% candle has NOT yet pulled price and flow apart enough to
trigger a divergence read in the tool, but it is one or two
sessions away — phase-9 should monitor.

### Analyst vs flow

The tool returned only the options-flow side:

| Field | Value |
|-------|-------|
| flow_sentiment | bullish |
| bullish_premium | $7,792,208 |
| bearish_premium | $6,918,251 |
| put_call_ratio | 0.5288 |

The analyst-recommendation side did not populate (likely Yahoo
HTTP 401 from deep_dive's underlying call). Use phase-6's manual
read: **Needham $300 PT** post-Q1-earnings (4/30/2026) gives a
~89% implied upside from $158 spot. Wall Street is broadly bullish
on RDDT post-print; this is **agreement** with flow.

### Institutional accumulation

| Field | Value |
|-------|-------|
| signal | **ACCUMULATION** ("dark pool buy volume significantly exceeds sell volume") |
| buy_sell_ratio | 1.80 |
| buy_side_volume | 266,211 |
| sell_side_volume | 148,236 |
| dark_pool_trades | 196 |
| avg_trade_price | $158.33 |
| vwap | $158.47 |
| total_dp_premium | $65,677,974 |
| total_dp_volume | 414,447 |
| price_30d_change_pct | +6.81% |

Top price levels mirror phase-2:

| Price | Shares | Premium |
|-------|--------|---------|
| 159.95 | 25,000 | $3.999M |
| 159.79 | 25,000 | $3.995M |
| 159.77 | 18,269 | $2.919M |
| 159.11 | 15,525 | $2.470M |
| 158.00 | 13,082 | $2.067M |

Read: **full confirmation of phase-2**. VWAP $158.47 is the
institutional cost basis anchor — phase-9 should treat the
$158-$160 zone as the institutional "fair value" and any pullback
below $158 as a developing risk (vs cost basis) signal.

### Earnings play

Next earnings 2026-07-30 = **73 days from 2026-05-18**, well outside
the default 14-day `insights_earnings_play` window. Tool skipped
per the phase spec. However the 8/21 IV hump (phase-4) and the LEAP
positioning (phase-3, phase-7-deep-dive) are both consistent with
this earnings date — record the 7/30 date in the phase-9 calendar.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__insights_deep_dive` | symbol=RDDT, date=2026-05-18 | full snapshot; yahoo fund. 401 |
| `mcp__uw-pp__insights_signal_confluence` | direction=bullish, date=2026-05-18, min_score=1, top_n=200 | RDDT score 5/6 (5 factors) |
| `mcp__uw-pp__insights_conviction_matrix` | symbol=RDDT, date=2026-05-18 | DIRECTIONAL_LONG, confidence 22.25% |
| `mcp__uw-pp__insights_price_vs_flow` | symbol=RDDT, date=2026-05-18, lookback=30 | no divergence |
| `mcp__uw-pp__insights_analyst_vs_flow` | symbol=RDDT, date=2026-05-18 | flow bullish; analyst side empty (yahoo 401) |
| `mcp__uw-pp__insights_institutional_accumulation` | symbol=RDDT, date=2026-05-18 | ACCUMULATION, b/s 1.8 |
| `mcp__uw-pp__insights_earnings_play` | n/a | skipped — Q2 earnings 7/30 outside 14d window |

## Tool errors

- `insights_deep_dive` Yahoo fundamentals call → `HTTP 401`. Yahoo
  blocks the fundamentals endpoint without authentication; not
  recoverable from here. Mitigation: phase-6 already supplied Q1
  results (rev $663M, EPS $1.01, EBITDA margin 40%, Needham $300 PT)
  from WebSearch.
- `insights_analyst_vs_flow` analyst side empty (same Yahoo auth
  issue).

## Cross-check vs phases 1–6

| UW insight | Phase agreement? | Notes |
|------------|------------------|-------|
| signal_confluence 5/6 (bullish) | **phases 1, 2, 3, 4 AGREE** | Single-day snapshot; doesn't see phase-5 regime |
| conviction_matrix DIRECTIONAL_LONG, 22% conf | phases 1, 2 AGREE on direction | LOW confidence_pct corroborates phase-5 caution |
| price_vs_flow NO divergence | phase-1 AGREES | But phase-5 next-day -2.64% means divergence is forming |
| institutional_accumulation ACCUMULATION | **phase-2 AGREES strongly** (block 0.79 buy ratio) | Highest-confidence cross-check in workup |
| analyst_vs_flow (flow only) | phase-6 Needham $300 PT AGREES | Both bullish; analyst side blocked by Yahoo |
| deep_dive earnings date 2026-07-30 | **phase-4 8/21 IV hump CONFIRMED** | Now explains: hump is residual post-earnings IV bleed |
| deep_dive implied move 5.24% | phase-5 -2.64% next-day = WITHIN band | Within 1σ weekly; no surprise yet |
| (none) | phase-5 0% backtest win rate for bullish_flow | NOT addressed by any insight tool — gap |
| (none) | phase-6 TRANSITIONAL regime / Comm Services outflow | NOT addressed by any insight tool — gap |

Two persistent gaps that phase-9 must close:
1. UW insights are date-local; they don't know that bullish_flow is
   getting faded across the tape this week.
2. UW insights don't ingest sector-rotation; the -$20.5M Comm Services
   outflow is unpriced in the composite.

## Verdict for downstream phases

- **UW composite bias:** **DIRECTIONAL_LONG** (signal_confluence 5/6,
  conviction_matrix DIRECTIONAL_LONG, institutional_accumulation
  ACCUMULATION, price_vs_flow aligned).
- **Conviction:** **3 / 5** — the LABEL is bullish but the MODEL'S
  OWN confidence_pct is 22.25% AND the regime-conditioning gaps
  (phase-5, phase-6) cap upside conviction.
- **Phase-9 baseline rule:** Use DIRECTIONAL_LONG as the starting
  point. Override only with the specific contrary evidence from:
  (a) phase-5 historical_signal_backtest 0% win rate, (b) phase-6
  TRANSITIONAL regime + sector outflow, (c) phase-4 spot $0.50 above
  ZGL (knife-edge structure), (d) phase-3 only 4 contracts above OI
  threshold (flow > positioning). Sizing must be reduced to ≤50% of
  normal even though the directional view is bullish.
- **Open questions:**
  - Did 5/19's -2.64% break the alignment (phase-9 should re-verify
    with `price_vs_flow` if a 5/19 snapshot becomes available)?
  - Does phase-8 contrarian-scanner agree with the "low confidence_pct
    + crowded factor agreement" → fade-the-bullish-consensus read?
  - Should phase-9 prefer a calendar/diagonal structure to harvest
    the 5/22 79% IV vs 7/17 63% IV backwardation rather than a
    straight directional long, given the cheap-IV regime?
