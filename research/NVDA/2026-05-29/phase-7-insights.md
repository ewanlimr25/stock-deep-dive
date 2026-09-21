# Phase 7 — UW Insights Confluence

**Ticker:** NVDA
**As-of date:** 2026-05-29
**Generated:** 2026-05-30T14:45Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-6-macro.md

## Summary

UW's composite tools **independently confirm the bearish/distribution read** that
emerged in phases 2–4 and override the superficially-bullish options headline.
The **conviction-matrix classifies NVDA DIRECTIONAL_SHORT** ("Dark pool selling +
put buying — institutional bear bet", confidence 32.3%), and
**institutional-accumulation returns DISTRIBUTION** (dark-pool buy/sell ratio
**0.27**, sell 67.4M vs buy 18.0M shares). Both are driven by the same
closing-cross sell block phase-2 found (49.7M sh at 211.14). The one bullish
crosscurrent is `price-vs-flow`, which reports **no divergence** with a *bullish*
30-day flow label — but that is a month-scale read (period +4.69%) and reflects
the near-balanced net premium (+$17.3M), not conviction. NVDA appears in
**neither** the bullish nor bearish market-wide signal-confluence top lists
(n=80/50), consistent with phase-0.5's **BUSY_NAME_NORMAL_DAY** — it is not a
standout in either direction today. **UW composite bias: DIRECTIONAL_SHORT /
distribution, low confidence (32%). Conviction 3/5.** This becomes phase-9's
baseline: a low-conviction bearish/distribution tape inside a constructive sector.

## Key signals

- [INSIGHT:conviction-matrix] **Scenario DIRECTIONAL_SHORT**, confidence **32.3%**
  — "Dark pool selling + put buying — institutional bear bet." Dark-pool buy_ratio
  **0.211** (18.0M buy / 67.4M sell).
- [INSIGHT:institutional-accumulation] **Signal DISTRIBUTION** — buy/sell ratio
  **0.27**, sell 67.4M vs buy 18.0M; VWAP 212.83, avg trade 215.47 (both > 211.14
  close — sold into the close). Top level: **49.7M sh / $10.49B at 211.14**.
- [INSIGHT:price-vs-flow] **divergence FALSE** ("price and flow aligned"),
  flow_direction *bullish*, net_premium +$17.3M, 30d price +4.69% — month-scale,
  reflects balanced premium, **not** a strong bull signal.
- [INSIGHT:signal-confluence] NVDA in **neither** bullish (n=80) nor bearish
  (n=50) top lists → not a directional standout; corroborates BUSY_NAME_NORMAL_DAY.
- [INSIGHT:deep-dive uw_screener] Whole-tape: bullish_premium **$596M** vs
  bearish **$579M** (net +$17.3M), call_premium $1.04B vs put $277M, P/C 0.424,
  IV rank 40.65, implied_move **±0.45% / $0.95**.

## Detailed findings

### Deep-dive snapshot (whole-tape aggregates)

| metric | value |
|--------|-------|
| close | 211.14 (−1.45% day) |
| bullish_premium / bearish_premium | $596.1M / $578.7M (**net +$17.3M**) |
| call_premium / put_premium | $1,043.3M / $277.0M |
| put_call_ratio | 0.424 |
| iv_rank | 40.65 |
| implied_move / perc | $0.95 / ±0.45% (front-expiry) |
| dark-pool total | 85.4M sh, $18.17B, VWAP 212.83 |
| dark-pool buy/sell | **0.27 ratio (DISTRIBUTION)** |

The options aggregate is mildly bullish (+$17.3M, capped at `+` per phase-0.5);
the dark-pool aggregate is decisively distributive. UW's composites weight the
dark-pool tape and land DIRECTIONAL_SHORT.

### Signal confluence

NVDA is absent from both directional top lists at min-score 1. It is neither a
top bullish nor a top bearish confluence name — a middling, two-sided tape. No
high-conviction stack (≥5) on either side.

### Conviction matrix

- **DIRECTIONAL_SHORT, confidence 32.3%** (below the bull 0.6 / above-bear-0.4
  framing — it sits in the bearish zone but at low confidence). Driver: dark-pool
  sell + put buying. This is the single most decisive composite read and it
  **agrees with phase-2 (distribution) and phase-3 (written calls / put builds)**.

### Price vs flow

- **No divergence** over 30 days; flow labeled bullish, price +4.69% for the
  window. Note this is a *monthly* lookback that starts at 201.68 (post-gap low
  area) and ends 211.14 — it does **not** capture the recent 10-session −10.4%
  leg or today's intraday fade. Treat as "no month-scale reversal flag," not as a
  bull signal. The phase-2 intraday flow/price divergence (calls bid at 215–217,
  stock sold to 211.14 close) is a finer-grained, more current read.

### Analyst vs flow

- Tool returned only the options-flow block (flow_sentiment bullish, net +$17.3M);
  **no analyst consensus block populated** (yfinance side empty in this pull) — so
  no Wall-Street-vs-traders agreement read. Deferred to phase-7b (fundamentals)
  for the analyst cross-source.

### Earnings play

- Out of window — earnings 2026-08-26 (>30d). Not run.

## Tool calls (audit trail)

| Command | Result |
|---------|--------|
| `uw insights conviction-matrix --symbol NVDA --date 2026-05-29 --json` | DIRECTIONAL_SHORT, conf 32.3% |
| `uw insights institutional-accumulation --symbol NVDA --json` | DISTRIBUTION, buy/sell 0.27 |
| `uw insights price-vs-flow --symbol NVDA --lookback-days 30 --json` | no divergence (30d), flow bullish |
| `uw insights analyst-vs-flow --symbol NVDA --json` | flow bullish; analyst block empty |
| `uw insights signal-confluence --direction bullish/bearish --min-score 1 --json` | NVDA in neither top list |
| `uw insights deep-dive --symbol NVDA --date 2026-05-29 --json` | whole-tape aggregates (above) |

## Tool errors

```
# analyst-vs-flow: analyst/consensus block not populated (yfinance side empty);
#   only options-flow returned. Analyst cross-source deferred to phase-7b.
# signal-confluence is market-wide; NVDA absent from top-80 bullish / top-50
#   bearish at min-score 1 (not an error — means no strong directional stack).
```

## Cross-check vs phases 1–5

| UW insight | Phase agreement? | Notes |
|------------|------------------|-------|
| conviction_matrix = DIRECTIONAL_SHORT | **agrees** phase-2/3/4 | dark-pool sell + written calls + put builds |
| institutional_accumulation = DISTRIBUTION | **agrees** phase-2 | same 49.7M sell block, buy/sell 0.27 |
| price_vs_flow = no divergence (bullish, 30d) | partial tension w/ phase-1 | month-scale; misses intraday fade & recent −10% leg |
| signal_confluence: NVDA in neither list | **agrees** phase-0.5 | BUSY_NAME_NORMAL_DAY, not a standout |
| deep-dive net_flow +$17.3M | **agrees** phase-1 | mildly bullish options, capped at `+` |

## Verdict for downstream phases

- **UW composite bias:** **DIRECTIONAL_SHORT / DISTRIBUTION**, low confidence (32.3%).
- **Conviction:** 3/5 (two independent composites agree on distribution; offset by
  the constructive sector macro and the still-bullish 30d price-vs-flow label).
- **Phase 9 baseline:** treat this as a **low-conviction bearish/distribution
  tape**. The bullish options headline is a head-fake (balanced net premium +
  written calls); the institutional stock flow is selling. Override only with
  specific contrary evidence — the main contrary force on file is phase-6's
  durable Tech sector inflow (tailwind) and the intact longer uptrend (phase-5 fz).
- **Open questions for 7b/7c/8b:** Do fundamentals justify distribution at these
  levels (valuation veto, 7b)? Is sentiment/positioning crowded or is the near-
  dated put/tail-hedge build a rising-fear signal (7c)? Can the bull case survive
  the bear's strongest point — institutional distribution into a sector that's
  being bought (8b)?
