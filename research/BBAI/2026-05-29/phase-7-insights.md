# Phase 7 — UW Insights Confluence

**Ticker:** BBAI
**As-of date:** 2026-05-29
**Generated:** 2026-05-31
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-4-structure.md, phase-5-historical.md

## Summary

UW's composite tools **independently reproduce the deep-dive's central finding: a
price-up / flow-bearish divergence with no clear directional bias.** `price-vs-flow`
fires an explicit **DIVERGENCE** ("price is up 30.9% but options flow is bearish,
net flow −$756,295"); `conviction-matrix` returns **scenario MIXED at just 5%
confidence** ("balanced dark pool — no clear bias"); `institutional-accumulation`
reads **NEUTRAL** (buy/sell share ratio 1.22, "balanced"); and `analyst-vs-flow`
shows **bearish flow** (analyst consensus unavailable via this source). This is a
clean cross-validation of phases 1–5: **bearish options premium + a stretched price
+ only mildly-positive dark pool = MIXED, low-conviction, fade-the-extension** — to
be read against phase-4's long-gamma $5 pin.

## Key signals

- **price-vs-flow = DIVERGENCE**: "price up 30.9% but options flow bearish (net
  −$756,295)" — leading reversal warning [INSIGHT:price-vs-flow]
- **conviction-matrix = MIXED, confidence 5%** — "balanced dark pool, no clear
  bias" [INSIGHT:conviction-matrix]
- **institutional-accumulation = NEUTRAL** (buy/sell 1.22; buy 5,041,000 / sell
  4,120,163 sh; vwap $4.99; $45.7M DP) [INSIGHT:institutional-accumulation]
- **analyst-vs-flow = bearish flow** (net −$756,295, P/C 0.113; analyst consensus
  N/A) [INSIGHT:analyst-vs-flow]
- conviction-matrix options detail confirms **call selling**: call_bid_vol 123,453 >
  call_ask_vol 112,090 [INSIGHT:conviction-matrix]

## Detailed findings

### Deep-dive snapshot (whole-tape `uw_screener`)

| metric | value |
|--------|-------|
| market cap / spot | ~$1.64B / $5.04 |
| `bullish_premium` / `bearish_premium` | $5,310,344 / **$6,066,639** |
| `net_flow` | **−$756,295** |
| `call_premium` / `put_premium` | $11,866,705 / $1,082,369 |
| P/C ratio | 0.113 |
| `implied_move` / `implied_move_perc` | **6.79%** / 1.35% (phase-9 N4) |
| `iv_rank` | 34.39 |
| `total_open_interest` | 945,694 |
| dark pool | 9,161,163 sh / $45,737,321 / vwap $4.99 |
| next earnings | 2026-08-10 |

### Signal confluence

- `uw insights signal-confluence` is **market-wide** (`--direction`/`--min-score`,
  rejects `--symbol`) — not captured cleanly in this run (tool gap; see errors). The
  per-name composite is covered by conviction-matrix + price-vs-flow below.

### Conviction matrix (`uw insights conviction-matrix`)

- **scenario MIXED, confidence_pct 5** — "Balanced dark pool activity — no clear
  bias." `dark_pool.buy_ratio` 0.55 (buy 5,041,000 / sell 4,120,163). `options_flow`:
  **call_bid 123,453 > call_ask 112,090** (net call selling), put_bid 15,419 >
  put_ask 10,915. Thresholds bull ≥0.6 / bear ≤0.4 → 0.55 lands in the MIXED band.

### Price vs flow (`uw insights price-vs-flow`)

- **divergence = true**: "Price is up **30.9%** but options flow is **bearish**
  (net flow −$756,295)." period $3.85 → $5.04 (high $5.16, low $3.61), iv_rank 34.39.
  A textbook bearish divergence / reversal flag — tempered by phase-4's long-gamma
  pin (mean-reversion toward $5, not necessarily a hard reversal).

### Analyst vs flow (`uw insights analyst-vs-flow`)

- Only `options_flow` returned: **flow_sentiment bearish**, net −$756,295, P/C
  0.113. **Analyst consensus unavailable** (yfinance returned no rating block for
  BBAI) — the WebSearch read (phase-6) shows sell-side leaning constructive on the
  contract backlog, so the analyst-vs-flow tension is **constructive-analyst vs
  bearish-flow** (contradiction), to be weighed in phase-8.

### Institutional accumulation (`uw insights institutional-accumulation`)

- **signal NEUTRAL — "balanced dark pool activity"**; buy_sell_ratio 1.22 (buy
  5,041,000 / sell 4,120,163), 229 trades, vwap $4.99, total_dp_premium $45.7M.
  Top levels: $5.04 (888,585 sh), $5.08, $5.13, $4.76, $4.94 — the $5 shelf (phase-2).

### Earnings play

- Out of window (earnings 2026-08-10, >30d) — not run.

## Tool calls (audit trail)

| Command | Result |
|---------|--------|
| `uw insights conviction-matrix --symbol BBAI --date 2026-05-29` | MIXED, confidence 5% |
| `uw insights price-vs-flow --symbol BBAI --date 2026-05-29` | DIVERGENCE (price +30.9% / flow bearish) |
| `uw insights analyst-vs-flow --symbol BBAI --date 2026-05-29` | flow bearish; analyst N/A |
| `uw insights institutional-accumulation --symbol BBAI --date 2026-05-29` | NEUTRAL, buy/sell 1.22 |
| `uw insights deep-dive --symbol BBAI --date 2026-05-29` | net_flow −$756,295; impl move 6.79% |

## Tool errors

- `uw insights signal-confluence --symbol` → `unknown flag: --symbol` (market-wide
  leaf; needs `--direction`/`--min-score`). Per-name composite covered by the other
  insights; recorded as a tool gap, not fabricated.

## Cross-check vs phases 1–5

| UW insight | Phase agreement? | Notes |
|------------|------------------|-------|
| conviction_matrix MIXED (5%) | **agrees** | phase-1 bearish flow + phase-2 mild DP + phase-5 no edge |
| institutional_accumulation NEUTRAL | **agrees** | phase-2 mild large-tier buy (1.22), no blocks → NEUTRAL |
| price_vs_flow DIVERGENCE | **agrees (strongly)** | phase-1 divergence + phase-0.5 blow-off |
| analyst_vs_flow (flow bearish) | **agrees** | phase-1; analyst side N/A here, constructive per phase-6 |

→ Fully internally consistent. No phase is contradicted.

## Verdict for downstream

- **UW composite bias:** **MIXED with a bearish-divergence lean; very low
  conviction** (conviction-matrix confidence 5%).
- **Conviction:** 2/5 (the composite itself says "no clear bias").
- **Phase-9 baseline:** treat as **MIXED / fade-the-extension at the $5 pin** —
  override only with specific contrary evidence (e.g. phase-7c squeeze risk on 26%
  short float, or phase-6 contract-catalyst momentum).
- **Open questions:** Does the constructive analyst/contract narrative (phase-6) +
  26% short float (phase-7c) outweigh the bearish-flow divergence, or does the
  long-gamma pin + neutral DP cap the bounce? Phases 7c, 8, 8b decide.
