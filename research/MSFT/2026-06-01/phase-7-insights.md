# Phase 7 — UW Insights Confluence

**Ticker:** MSFT
**As-of date:** 2026-06-01
**Generated:** 2026-06-02T11:18:20Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-5-historical.md

## Summary

UW's own composite engine **independently confirms the MIXED / low-conviction
read** the whole chain has been building. **`conviction-matrix` returns scenario
MIXED at just 3% confidence** ("balanced dark pool activity — no clear bias"), with
**call_ask_volume 594,991 ≈ call_bid_volume 580,116** — the cleanest single proof
that the call tape is two-way, not directional accumulation. **`signal-confluence`
does not list MSFT among bullish names even at `--min-score 1`** (zero confluence
factors stacking), and **`institutional-accumulation` reads NEUTRAL** (buy/sell
1.13, balanced). The lone positive: **`price-vs-flow` shows no divergence** —
price (+10.15%) and bullish flow are aligned. Net composite: **slight bullish
lean, but low-conviction and unconfirmed by confluence, accumulation, or
structure** — exactly consistent with phases 1–6. This is the BASELINE phase-9
should anchor to.

## Key signals

- **conviction-matrix: MIXED, confidence 3%** — "no clear bias" `[INSIGHT:conviction_matrix]`.
- **call_ask 594,991 ≈ call_bid 580,116** (and put_bid 150,775 > put_ask 141,151) →
  two-way call tape, mild put selling `[INSIGHT:conviction_matrix]`.
- **signal-confluence: MSFT absent from bullish top-20 (score <1)** — no factor
  stack `[INSIGHT:signal_confluence]`.
- **institutional-accumulation: NEUTRAL**, buy/sell 1.13, $6.09B DP `[INSIGHT:institutional_accumulation]`.
- **price-vs-flow: NO divergence, aligned bullish**, +10.15%, net flow +$81.2M
  `[INSIGHT:price_vs_flow]`.

## Detailed findings

### Deep-dive snapshot `[INSIGHT:deep_dive]`

`uw_screener` whole-tape directional aggregates (reconciled with phase-1):

| Field | Value |
|-------|-------|
| `bullish_premium` / `bearish_premium` | $795.5M / $714.3M |
| **derived `net_flow`** (bull − bear) | **+$81.2M** |
| `call_premium` / `put_premium` | $1,392.6M / $264.6M |
| `put_call_ratio` | 0.256 |
| `implied_move` / `implied_move_perc` | 15.36 / **3.33%** (phase-9 N4 sizes to this) |
| `iv_rank` | 73.07 |

`uw_dark_pool` summary: $6.09B premium, avg $461.69 (matches phase-2).
`uw_top_oi_changes`: 5 rows (call-led, per phase-3). **`yahoo_fundamentals`:
ERROR** (Yahoo block failed) → fundamentals sourced in phase-7b (Finnhub/fz/
WebSearch), analyst consensus from phase-6 (Buy, avg PT $565).

### Signal confluence `[INSIGHT:signal_confluence]`

MSFT is **not** in the bullish top-20 even at `--min-score 1` → its bullish
confluence score is **below 1**. Despite $1.39B call premium, the factors
(flow + DP + OI + price + structure aligned) do **not** stack. High-conviction
confluence (≥5) is absent; this is the opposite — near-zero.

### Conviction matrix `[INSIGHT:conviction_matrix]`

`scenario`: **MIXED**, `confidence_pct`: **3**, `explanation`: *"Balanced dark pool
activity — no clear bias."* Underlying:
- options_flow: call_ask **594,991** vs call_bid **580,116** (Δ +14,875, ~+1.3% — a
  whisker of net call buying on a two-way tape); put_ask 141,151 vs put_bid 150,775
  (net put *selling*).
- dark_pool: buy_ratio **0.53**, buy 6.99M / sell 6.21M sh — balanced.
Reads as **neither DIRECTIONAL_LONG nor COVERED_CALL — genuinely MIXED.**

### Price vs flow `[INSIGHT:price_vs_flow]`

`divergence`: **false** ("Price and flow are aligned"), `flow_direction`: bullish,
`net_premium_flow`: +$81.2M, `price_change_pct`: **+10.15%** (start 418.07 → end
460.52; period low 398.01 / high 466.32). No reversal signal — price and bullish
flow agree (both up). Mild positive, but note price is just off the period high
(460.5 vs 466.3) after a +10% leg.

### Analyst vs flow `[INSIGHT:analyst_vs_flow]`

Tool returned **only the flow side** (analyst/yfinance side unavailable, like the
yahoo block): flow_sentiment **bullish**, net_flow +$81.2M, P/C 0.256. Analyst
consensus comes from phase-6 WebSearch: **Buy, avg PT $565** (MS Overweight $650)
vs spot $460 — Wall Street and options flow **agree directionally bullish**, though
the flow magnitude is modest/two-way.

### Institutional accumulation `[INSIGHT:institutional_accumulation]`

`signal`: **"NEUTRAL — balanced dark pool activity"**, `buy_sell_ratio` **1.13**,
buy 6.99M / sell 6.21M sh, `total_dp_premium` $6.09B, `price_30d_change_pct`
+10.15%, `vwap` 460.8. **NOT accumulation** — confirms phase-2.

### Earnings play

**Out of window** — next earnings 2026-07-29 (>30d, phase-6). Skipped.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|------------------|--------------------------|-----------|
| `uw insights deep-dive --symbol MSFT --date 2026-06-01 --json` | net_flow +$81.2M, IV rank 73.07; yahoo ERROR ← `.uw_screener`, `.yahoo_fundamentals.error` | whole-tape |
| `uw insights signal-confluence --direction bullish --min-score 1 --top-n 20 --json` | MSFT absent (score<1) ← `map(select(.ticker=="MSFT"))` = [] | top-20 |
| `uw insights conviction-matrix --symbol MSFT --date 2026-06-01 --json` | MIXED, 3%, call_ask≈call_bid ← `.scenario,.confidence_pct,.options_flow` | 1 |
| `uw insights price-vs-flow --symbol MSFT --lookback-days 30 --json` | divergence false, +10.15% ← `.divergence,.price_change_pct` | 30d |
| `uw insights analyst-vs-flow --symbol MSFT --json` | flow bullish only (analyst side absent) ← `.options_flow` | 1 |
| `uw insights institutional-accumulation --symbol MSFT --json` | NEUTRAL, 1.13 ← `.signal,.buy_sell_ratio` | 1 |

## Tool errors

- `uw insights deep-dive` `.yahoo_fundamentals` → `{"error": …}` (Yahoo fetch
  failed). Non-fatal: PE/mcap/short% deferred to phase-7b; directional `uw_screener`
  block returned fine.
- `uw insights analyst-vs-flow` returned only `.options_flow` (no analyst-consensus
  block — yfinance analyst data unavailable). Analyst view taken from phase-6 instead.

## DATA NOTE / CORRECTION

None — all reported values round-tripped through `jq`.

## Cross-check vs phases 1–5

| UW insight | Phase agreement? | Notes |
|------------|------------------|-------|
| signal_confluence (absent, <1) | **agrees** w/ phases 1–3 | no factor stack — matches two-way tape |
| conviction_matrix (MIXED 3%) | **agrees** w/ phase 1 & 2 | call_ask≈call_bid confirms two-way; balanced DP |
| institutional_accumulation (NEUTRAL) | **agrees** w/ phase 2 | not accumulation — matches mixed DP |
| price_vs_flow (aligned bullish) | **agrees** w/ phase 5 | +10.15% price, bullish flow, no divergence |
| analyst (Buy $565, ph-6) vs flow (bullish) | **agree** directionally | both bullish; flow magnitude modest |

**Fully internally consistent** — no contradiction to flag for phase-10 here (the
flow-vs-structure tension lives in phase-4, not in this composite layer).

## Verdict for downstream phases

- **UW composite bias: MIXED with a slight bullish lean — LOW conviction.** The
  matrix is 3%-confident MIXED, confluence score <1, accumulation NEUTRAL; the only
  positive is bullish price/flow alignment (no divergence).
- **Conviction: 2/5.** The composite engine, which does its own confluence math,
  declines to call this a directional-long setup.
- **Phase-9 baseline:** treat this as a **MIXED / slight-bullish / low-conviction**
  situation; only override toward a strong directional long with *specific* contrary
  evidence (and phases 1–6 supply none — they reinforce mixed). The defensible bias
  is small/defined-risk, not conviction-long.
- **Open questions:** Does fundamentals (7b) add a quality tailwind or a valuation/
  capex veto? Does sentiment/positioning (7c) flag the complacent skew (phase-4) as
  a crowded-long fade? The debate (8b) should test bull (Tech rotation + Azure) vs
  bear (two-way flow + pinned structure + edge-negative backtest + transitional regime).
