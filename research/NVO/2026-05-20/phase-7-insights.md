# Phase 7 — UW Insights Confluence

**Ticker:** NVO
**As-of date:** 2026-05-20
**Generated:** 2026-05-20T21:55:00-04:00
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-4-structure.md, phase-5-historical.md, phase-6-macro.md

## Summary

UW's composite reads agree with phases 1–5: **DIRECTIONAL_LONG** scenario
on the conviction matrix, **ACCUMULATION** on institutional flow (DP buy
ratio 0.687, buy/sell 2.19×), and **no divergence** between flow and the
+20.4% 30-day price action ($37.44 → $45.07). The single dissenting
datapoint is that **NVO did NOT appear in the bullish signal-confluence
top 50 today (min_score=1)** — most likely because volume was not a
"spike" relative to NVO's already-active baseline and the absolute
net-premium ($1.75M) is small for a name this size. Phase 9 should treat
the composite verdict as **moderate-conviction bullish** and discount
for the missed confluence tag.

Note: `yahoo quoteSummary` returned HTTP 401, so insights_deep_dive's
fundamentals block (PE, market cap, short %) is unavailable; quantitative
flow + DP fields are intact and form the actionable signal.

## Key signals

- **Conviction matrix: DIRECTIONAL_LONG** (DP buy_ratio 0.687 > 0.60 bull threshold; aggressive call ask-side buying); confidence 23.98% [INSIGHT:conviction_matrix]
- **Institutional accumulation: ACCUMULATION** — buy/sell 2.19×; buy_volume 1,277,980 vs sell_volume 583,277 shares; 30d price +20.38% [INSIGHT:institutional_accumulation]
- **Price vs flow: NO DIVERGENCE** — 30d range $36.82 → $47.79, bullish flow aligned with +20.4% rise [INSIGHT:price_vs_flow]
- **Deep dive snapshot:** IV30 = 0.3766, IV rank = 12.32, PCR = 0.331, next earnings = **2026-08-05**, total OI = 1,389,734 [INSIGHT:deep_dive]
- **Bullish signal confluence: NVO not in top 50 (min_score=1)** — top scorers FLR, TE, PPLT, XIFR (score 6); peers in healthcare bullish list = GILD, DXCM, VKTX, RLAY, IMNM, TLRY, PRCT, PGNY — NVO absent [INSIGHT:signal_confluence]

## Detailed findings

### Deep dive snapshot

| Field | Value |
|-------|------:|
| Symbol | NVO |
| Sector | Healthcare |
| IV30d | 37.66% |
| IV rank | **12.32** (very low) |
| PCR | 0.331 (call-heavy) |
| Total OI | 1,389,734 |
| Call premium | $4,933,340 |
| Put premium | $1,424,100 |
| Bullish premium | $3,622,732 |
| Bearish premium | $1,870,445 |
| Implied move (1d) | 0.99 / 2.19% |
| Next earnings | **2026-08-05** (Q2 2026; 77 days out) |
| DP avg price | $44.86 |
| DP total premium | $83,636,790 |
| DP total shares | 1,861,257 |
| DP trade count | 221 |
| Yahoo fundamentals | **error: HTTP 401** (PE, market cap, short interest unavailable) |

Top OI changes today (already analyzed in phase-3):
- 2026-06-18 $42.5P +1,093 (put-sale floor)
- 2026-05-29 $45C +699 (bid-side, mild bear / income)
- 2026-05-29 $45P +642 (put-sale)
- 2026-06-18 $40.5P +474 (put-buy, hedge)
- 2027-06-17 $35P +417 (LEAP put-sale)

### Signal confluence (market-wide bullish, min_score=1, top 50)

**NVO does NOT appear in the top 50 bullish-confluence list.** That list is
dominated by:
- Score 6: FLR (Industrials), TE (Industrials), PPLT (ETF), XIFR (Utilities)
- Score 5: GILD ($130.69, Healthcare), DXCM ($71.44, Healthcare), VKTX ($29.44, Healthcare), META ($605.06), TOL ($136.31), IOT ($30.63), W ($64.72), RIVN ($13.73), AMBA ($83), LOW ($221.05), HSBC ($91.99), and ~30 others

Why NVO might be missing despite 5/6 factor presence:
1. **No "volume_spike"** — NVO's daily volume isn't extreme vs trailing average; it is structurally a heavily-traded ADR.
2. **Net flow $1.75M is small in absolute dollars** for a $50B+ market-cap name (most score-5 tickers had net flow >$200k on much smaller floats — the relative magnitude is lower for NVO).
3. **PCR 0.33** is "low_pcr" but borderline; the screener may use a stricter cutoff (e.g. <0.25) for the factor flag.

This is a **caveat, not a contradiction**: the composite scoring system
didn't fire NVO above the standard threshold, even though qualitatively
the picture (DP accumulation, OI build, bullish flow, low IV) is the same.
Phase 9 should treat this as: **the conviction matrix is reliable; the
absence from the broad confluence list moderates conviction by ~1 point.**

### Conviction matrix

| Field | Value |
|-------|------:|
| Scenario | **DIRECTIONAL_LONG** |
| Confidence | **23.98%** |
| DP buy_ratio | 0.687 (> 0.60 bull threshold) |
| DP buy_volume | 1,277,980 shares |
| DP sell_volume | 583,277 shares |
| Call ask volume | 12,569 |
| Call bid volume | 10,152 |
| Put ask volume | 2,814 |
| Put bid volume | 2,197 |
| Explanation | "Dark pool buying + aggressive call purchases — institutional directional bet" |

The confidence of 23.98% is modest — the matrix tags the scenario
confidently but assigns it limited statistical edge. Reading: **direction
is clear, magnitude is undecided.**

### Price vs flow

| Field | Value |
|-------|------:|
| Divergence | **No** |
| Signal | "Price and flow are aligned" |
| Flow direction | bullish |
| Net premium flow | +$1,752,287 |
| Period (30d) high | $47.79 |
| Period (30d) low | $36.82 |
| Price change | **+20.38%** |
| Price start | $37.44 |
| Price end | $45.07 |
| IV rank | 12.32 |

Confirms phase 5's read that NVO has been a strongly trending up name
with options-flow validation. No reversal warning.

### Analyst vs flow

The tool returned only `options_flow` data (sentiment = bullish, net flow
+$1.75M, PCR 0.33). The `analyst` block is absent — likely due to the
same yfinance auth issue that returned 401 on the fundamentals. **Analyst
consensus is not verified by this tool today** — phase 9 should not rely
on it without the phase-8 analyst-perspective agent's external check.

### Institutional accumulation

| Field | Value |
|-------|------:|
| Signal | **ACCUMULATION** ("dark pool buy volume significantly exceeds sell volume") |
| Buy/sell ratio | **2.19×** |
| Buy-side volume | 1,277,980 |
| Sell-side volume | 583,277 |
| Avg trade price | $44.86 |
| VWAP | $44.94 |
| 30d price change | +20.38% |
| Total DP premium | $83,636,790 |
| Total DP volume | 1,861,257 shares |
| Top price level | $45.07 — $35.24M premium, 782k shares, 12 trades |

Confirms phase 2's reading verbatim — the same 781k-share cluster at
$45.07 (mostly the post-close mega print) is the top-line institutional
buying mark.

### Earnings play

`insights_earnings_play` not run — next earnings 2026-08-05 is **77 days
out**, well outside the 14-day window. Skipped per phase-7 composition
guidance.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `insights_deep_dive` | `{symbol: NVO, date: 2026-05-20}` | Full snapshot; Yahoo fundamentals 401 |
| `insights_signal_confluence` | `{date: 2026-05-20, direction: bullish, min_score: 1, top_n: 50}` | NVO not in top 50 |
| `insights_conviction_matrix` | `{symbol: NVO, date: 2026-05-20}` | DIRECTIONAL_LONG, confidence 23.98% |
| `insights_price_vs_flow` | `{symbol: NVO, date: 2026-05-20, lookback_days: 30}` | No divergence, +20.4% / bullish flow aligned |
| `insights_analyst_vs_flow` | `{symbol: NVO, date: 2026-05-20}` | options_flow only; analyst block absent |
| `insights_institutional_accumulation` | `{symbol: NVO, date: 2026-05-20}` | ACCUMULATION, 2.19× buy/sell |

## Tool errors

- `insights_deep_dive` returned `yahoo_fundamentals.error: "yahoo quoteSummary NVO: HTTP 401"` — PE, market cap, short interest, dividend info **not available** via this tool today. Phase 8 agents may use WebSearch to fetch.
- `insights_analyst_vs_flow` did NOT include an analyst block (likely same 401 underneath). No consensus rating captured.

## Cross-check vs phases 1–6

| UW insight | Phase agreement? | Notes |
|------------|------------------|-------|
| conviction_matrix = DIRECTIONAL_LONG | **Agrees with phases 1, 2, 3, 4, 5** | All upstream verdicts converge on long bias |
| institutional_accumulation = ACCUMULATION | **Agrees with phase 2** | Same $45.07 / 782k-share cluster |
| price_vs_flow = no divergence | **Agrees with phase 5** | +20.4% 30d up-trend + bullish flow |
| signal_confluence: NVO not in top 50 | **DISAGREES with phases 1–5** | Caveat: NVO doesn't tick "volume_spike" and net-flow magnitude is small relative to mkt cap. Soft red flag — moderates conviction. |
| Deep dive next earnings 2026-08-05 | Agrees with phase 6 | 77 days out — outside 30d catalyst window but worth noting for LEAP timeline |
| IV rank 12.32 | Agrees with phase 5 (IV %ile 7.14) | Same regime, different normalization |

## Verdict for downstream phases

- **UW composite bias: BULLISH (DIRECTIONAL_LONG + ACCUMULATION + no divergence)**, **moderated** by absence from the bullish signal-confluence top 50.
- **Conviction: 3.5/5** — would be 4.5 if NVO had also scored ≥5 on the confluence factor table. The "missing" confluence is the single most important caveat in this phase.
- **Phase 9 baseline treatment:** The conviction matrix is the load-bearing UW finding; the institutional_accumulation tag is the corroborating finding. Phase 9 should treat NVO as a **moderate-conviction long with sizing under the full Kelly allocation** to respect the missing confluence flag.
- **Open questions:**
  1. Does phase 8's analyst-perspective sub-agent corroborate the LEAP buyer's thesis with sell-side data (revised price targets post-ER) — this is the missing piece left by the 401 errors.
  2. Why did the bullish_flow factor for NVO not trip the screener? Is the threshold tuned for mid-caps and NVO's $50B+ market cap is suppressing the relative magnitude?
  3. Does the next earnings on 2026-08-05 (77 DTE) explain the rising Aug 21 IV bumps in phase 4's term structure?
