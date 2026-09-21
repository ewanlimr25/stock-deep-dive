# Phase 7 — UW Insights Confluence

**Ticker:** ADBE
**As-of date:** 2026-05-29
**Generated:** 2026-05-30T20:14:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-4-structure.md, phase-0.5-context.md

> **Within-run correction.** An earlier draft of this file mis-stated the
> conviction-matrix as "MIXED/LOW" and institutional-accumulation as "NEUTRAL."
> The flushed tool output shows the engine actually returned **DIRECTIONAL_LONG
> (confidence 41.3%)** and **ACCUMULATION (buy/sell 5.88)**. Corrected below. The
> important nuance — that the engine's bullishness rests on the same dark-pool
> buy_ratio phase-2 de-rated as closing-auction mechanical — is now the headline
> cross-check.

## Summary

UW's composite engine reads ADBE **bullish but at low confidence, and on data
phase-2 already discounted.** Conviction-matrix = **DIRECTIONAL_LONG** but
confidence only **41.3%** (the bull/bear thresholds are 0.6/0.4 and the inputs
straddle them) [INSIGHT:conviction_matrix]; institutional-accumulation =
**ACCUMULATION** with buy/sell **5.88** [INSIGHT:institutional_accumulation];
price-vs-flow shows **no divergence** (flow bullish, price +6% aligned)
[INSIGHT:price_vs_flow]; market-wide signal-confluence scores ADBE **3 of 6**
[INSIGHT:signal_confluence]. **The critical cross-check:** both the matrix and the
accumulation call lean on the **dark-pool buy_ratio (0.855)** — and phase-2 showed
that buy-skew is **~37% closing-auction/month-end crosses at the 259.21 close**, not
discretionary accumulation. So the UW composite is **mechanically bullish on
contaminated DP plus the call-tilted tape**, while phase-3 (call-writing) and phase-4
(long-gamma pin to 245-250) point the other way. Net: a **genuine but low-confidence
bullish composite that overstates the case** — phase-9 should treat the bullish lean
as real but discount the engine's confidence given the auction contamination.

## Key signals

- **Conviction-matrix DIRECTIONAL_LONG, confidence 41.3%** — flow + DP buy both
  above the 0.6 bull threshold, but confidence is sub-50% [INSIGHT:conviction_matrix].
- **Institutional-accumulation ACCUMULATION, buy/sell 5.88** — but the top price
  levels are 259.19–259.22 (the closing cross), confirming phase-2's auction read
  [INSIGHT:institutional_accumulation].
- **No price-vs-flow divergence** — flow bullish, price +6.04% over the lookback,
  aligned (not a reversal setup) [INSIGHT:price_vs_flow].
- **Signal-confluence 3/6** for ADBE — middling; the 5–6 leaders (GS, CRCL, UHAL)
  have the full stack ADBE lacks (volume_spike, dp_accumulation, oi_building)
  [INSIGHT:signal_confluence].
- **Earnings-play in-window:** days_to_earnings 13 (6/11), iv_rank 100, OI increase
  +13,776 vs decrease −2,719 [INSIGHT:earnings_play].

## Detailed findings

### Deep dive snapshot — `[INSIGHT:deep_dive]`

From phase-0.5/1's `uw_screener` block: net_flow **+$12.27M**, call_premium $46.62M
vs put_premium $20.43M, **P/C 0.468**, **iv_rank 100**, iv30d 0.596, implied_move
0.766/0.295% (front weekly), total_OI 637,730, next_earnings 2026-06-11. Yahoo
fundamentals 401'd → phase-7b (Finnhub/fz). DP aggregate $657.8M/2.55M sh/avg
$255.14 (phase-2).

### Signal confluence — `[INSIGHT:signal_confluence]`

ADBE **score 3/6**. The day's leaders (GS 6; CRCL, UHAL 5) carry
bullish_flow + low_pcr + dp_accumulation + oi_building + low_iv_cheap_options. ADBE
has the **bullish_flow + low_pcr** legs but **misses oi_building (it's writing, ph3),
clean dp_accumulation (auction-contaminated, ph2), and low_iv (IV rank is 100 — the
*opposite* of cheap)**. The 3/6 is a fair "real but partial" score.

### Conviction matrix — `[INSIGHT:conviction_matrix]`

Scenario **DIRECTIONAL_LONG**, **confidence_pct 41.3**. Inputs: dark_pool buy_ratio
**0.855** (>0.6 bull threshold), options_flow call_ask 28,288 vs call_bid 22,392 and
put_ask 9,229 vs put_bid 14,463 (net call-ask, put-bid = bullish). Explanation:
"Dark pool buying + aggressive call purchases — institutional directional bet."
**Caveat (phase-2):** the 0.855 DP buy_ratio is inflated by closing-auction crosses;
strip those and the discretionary large-tier buy_ratio was 0.64. The engine's
label is technically DIRECTIONAL_LONG but its **41.3% confidence** is the honest
signal — barely above coin-flip.

### Price vs flow — `[INSIGHT:price_vs_flow]`

`divergence: false`, "Price and flow are aligned." Flow bullish; price +6.04% over
the window (start 244.45 → end 259.21; period high 265.09, low 231.74). No reversal
divergence — the flow confirms the up-move rather than fighting it. Constructive,
but it also means **the easy +6% is already in the price** (today's 259.21 is near
the period high 265).

### Analyst vs flow — `[INSIGHT:analyst_vs_flow]`

Returned options_flow only (flow_sentiment bullish, net +$12.27M); the analyst leg
was empty from this tool (yfinance gap). Analyst cross-check deferred to phase-7c
(Finnhub recommendation trend + fz Recom 2.41) — which shows **deteriorating**
revisions, a contradiction the flow-only view here misses.

### Institutional accumulation — `[INSIGHT:institutional_accumulation]`

Signal **ACCUMULATION** — "dark pool buy volume significantly exceeds sell volume,"
buy/sell **5.88** (buy 2,180,326 vs sell 370,658), avg trade $255.14. **But the
top price levels it cites are 259.21 ($300M/122 trades), 259.19, 259.20, 259.22 —
i.e. the closing cross.** This is the same data phase-2 flagged as auction
mechanical. The tool cannot tell auction from discretionary; phase-2's de-rating
stands and this ACCUMULATION label is **overstated**.

### Earnings play — `[INSIGHT:earnings_play]`

ADBE in-window: days_to_earnings **13** (6/11), iv_rank **100**, implied_move_perc
0.295% (front weekly, pre-print — understates), OI increase +13,776 vs −2,719. The
elevated-IV pre-earnings setup is confirmed; not a top-of-scan name (PANW etc. rank
higher on fresher buildup).

## Tool calls (audit trail)

| Command | Result summary |
|---------|----------------|
| `uw insights conviction-matrix --symbol ADBE --date 2026-05-29` | DIRECTIONAL_LONG, confidence 41.3%, DP buy 0.855 |
| `uw insights institutional-accumulation --symbol ADBE` | ACCUMULATION, buy/sell 5.88 — top levels = closing cross |
| `uw insights price-vs-flow --symbol ADBE --lookback-days 30` | divergence false; flow bull, price +6.04% aligned |
| `uw insights analyst-vs-flow --symbol ADBE` | flow bullish; analyst leg empty (→ 7c) |
| `uw insights signal-confluence --direction bullish --min-score 1 --top-n 50 --date 2026-05-29` | ADBE 3/6 |
| `uw insights earnings-play --days-until-earnings 30` | ADBE 6/11, iv_rank 100, OI +13,776 |

## Tool errors

- `uw insights deep-dive` Yahoo fundamentals = HTTP 401 (phase-0.5) → 7b Finnhub/fz.
- `uw insights analyst-vs-flow` analyst leg empty (yfinance) → 7c Finnhub/fz.

## Cross-check vs phases 1–5

| UW insight | Phase agreement? | Notes |
|------------|------------------|-------|
| conviction_matrix DIRECTIONAL_LONG (41%) | **partial** — agrees with ph1 flow; **conflicts** with ph3 OI (call-writing) & ph4 (pin-down) | low confidence is the tell |
| institutional_accumulation ACCUMULATION 5.88 | **conflicts with phase-2's de-rating** | tool counts auction crosses as buys; phase-2 strips them |
| price_vs_flow no divergence | agrees with ph1/ph5 | flow confirms +6% up-move; move largely already made |
| signal_confluence 3/6 | agrees | "real but partial" — missing oi_building, clean dp, low_iv |

## Verdict for downstream

- **UW composite bias: BULLISH, LOW confidence (41.3%), partly on contaminated DP.**
  The engine labels DIRECTIONAL_LONG / ACCUMULATION, but both lean on the
  closing-auction DP buy-skew phase-2 discounted, and confidence is sub-50%.
- **Conviction:** 2 / 5 (the composite is bullish but weak and overstated).
- **Phase-9 should treat this as a WEAK bullish baseline** — real flow lean,
  confirmed by no-divergence and ACCUMULATION-on-paper, but **discount the engine's
  confidence** for the auction contamination and reconcile against phase-3/4's
  cautionary structure. Do NOT read DIRECTIONAL_LONG as a green light.
- **Open questions:** Do fundamentals (7b) justify paying up at IV-100 into the
  print, or is the cheap multiple a value trap with insiders selling? Does the
  positioning/crowd (7c) confirm or fade — especially the analyst-revision trend the
  analyst-vs-flow tool couldn't supply?
