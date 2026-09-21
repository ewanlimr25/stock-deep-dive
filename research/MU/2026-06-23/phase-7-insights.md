# Phase 7 — UW Insights Confluence

**Ticker:** MU
**As-of date:** 2026-06-23
**Generated:** 2026-06-23
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-5-historical.md, phase-6-macro.md

## Summary

UW's own composite engine agrees with the upstream read: **MIXED, a two-sided vol event
with a single clean directional tilt — a bearish price-vs-flow divergence.** The
`conviction-matrix` returns **MIXED at just 4.7% confidence** ("Balanced dark pool activity —
no clear bias"), MU is **absent from both the bullish and bearish signal-confluence top-30**
(no clean factor stack either way), and `institutional-accumulation` is **NEUTRAL**
(buy/sell ratio 1.21, balanced). The one composite signal that points somewhere:
`price-vs-flow` flags a **DIVERGENCE — "price up 32.2% but options flow is bearish
(−$145.2M)"**, the textbook leading reversal-down read after a parabolic run (and today's
−12% drop is that reversal beginning). `earnings-play` confirms the catalyst: **1 day to
earnings, IV rank 100, implied move 10.9%, OI building (+154k opened vs −28k closed).**
Net: the composite is a low-confidence MIXED with a mild bearish/reversal lean — phase-9's
baseline is a *vol event*, not a directional conviction trade.

## Key signals

- **Conviction-matrix MIXED, confidence 4.7%** — "balanced dark pool, no clear bias" `[INSIGHT:conviction_matrix]`
- MU **absent from both bullish & bearish signal-confluence** top-30 (no clean stack) `[INSIGHT:signal_confluence]`
- **Price-vs-flow DIVERGENCE (bearish)**: price +32.2% but flow −$145.2M → leading reversal-down `[INSIGHT:price_vs_flow]`
- **Institutional-accumulation NEUTRAL**: buy/sell 1.21, balanced book; 30d VWAP $1076.66 > $1051.77 close `[INSIGHT:institutional_accumulation]`
- **Earnings-play**: days_to_earnings **1**, IV rank 100, implied 10.9%, OI building (+154,442 / −27,999) `[INSIGHT:earnings_play]`

## Detailed findings

### Deep dive snapshot — `[INSIGHT:deep_dive]` (whole-tape `uw_screener`, from phase-1)

| Field | Value |
|---|---|
| bullish_premium / bearish_premium | $1.886B / $2.031B → **net_flow −$145.2M** |
| call_premium / put_premium | $2.646B / $1.490B |
| put_call_ratio | 1.013 |
| implied_move / implied_move_perc | $114.7 / **10.91%** (phase-9 N4 sizes to this) |
| iv_rank / iv30d | 100 / 1.072 |
| total_open_interest | 3,285,355 |
| dark-pool total_premium | $17.49B (#1 in market) |

Reconciles with phase-1 aggregate and phase-0.5 `[CTX]` (#1 net-bearish, 100th-pctile premium).

### Signal confluence — `[INSIGHT:signal_confluence]`

MU is **not in the bullish or the bearish list** even at `--min-score 1`. The standardized
6-factor stack (e.g. KBH scored 6 bearish: bearish_flow + high_pcr + volume_spike +
dp_distribution + oi_building_puts + high_iv_sell_premium) does **not** cleanly assemble for
MU in either direction — its factors are split (high IV + OI building, but balanced flow +
neutral DP). Confirms "no clean confluence," consistent with MIXED.

### Conviction matrix — `[INSIGHT:conviction_matrix]`

- `scenario` = **MIXED**, `confidence_pct` = **4.7%**; `explanation` = "Balanced dark pool
  activity — no clear bias."
- `options_flow` (whole-tape ask/bid volume): call_ask 132,462 vs **call_bid 163,156** (more
  calls *sold*), put_ask 149,199 vs put_bid 145,868 (slight put buying) → mild **bearish**
  aggressor read on the full tape (note: the *top-25 sweeps* in phase-1 leaned bullish — the
  whole-tape ask/bid leans the other way; the breadth of small flow is the bearish weight).
- `dark_pool` buy_ratio **0.547** (bull threshold 0.6 / bear 0.4 → neutral band).

### Price vs flow — `[INSIGHT:price_vs_flow]`

- `divergence` = **true**; `divergence_signal` = "DIVERGENCE: Price is up 32.2% but options
  flow is bearish (net flow: $−145,241,678)"; `flow_direction` = bearish.
- price_start 795.33 → price_end 1051.77 (+32.24%), period_high 1213.56, period_low 652.21.
- **The one clean directional tilt in the composite**: bearish flow against a big up-move =
  leading reversal-down (often early). Pair with phase-4 short-gamma (amplifies a break) and
  phase-5 (−12% reversal already underway, bearish_flow 88.9% backtest).

### Analyst vs flow — `[INSIGHT:analyst_vs_flow]`

Returned only `{options_flow, symbol}` — **no Yahoo analyst consensus/target** for MU on this
read (yfinance gap). Cannot score Wall-St-vs-flow agreement here; defer the analyst overlay to
phase-7b/7c (Finnhub revisions + `fz` cross-source).

### Institutional accumulation — `[INSIGHT:institutional_accumulation]`

- `signal` = **"NEUTRAL — balanced dark pool activity"**; `buy_sell_ratio` 1.21 (buy 8.89M /
  sell 7.36M sh), `total_dp_premium` $17.49B, `price_30d_change_pct` +32.24%, `vwap` **$1076.66**.
- **Refines phase-2**: the *overall* book is NEUTRAL (mild buy 1.21); phase-2's "accumulation"
  was driven by the **mega tier (85.9% buy)**, not the broad book. 30d VWAP $1076.66 sits
  **above** the $1051.77 close → after today's −12% drop, price is *below* the recent
  institutional average (constructive for dip-buyers, but the book is balanced, not loading).

### Earnings play (in-window) — `[INSIGHT:earnings_play]`

`days_to_earnings` **1** (2026-06-24), iv_rank 100, implied_move_perc 10.91%, PCR 1.013,
`total_oi_increase` **+154,442** vs `total_oi_decrease` −27,999 (net OI building into the
print), bullish $1.886B / bearish $2.031B. A maxed-IV, OI-building, two-sided pre-earnings setup.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Notes |
|---|---|---|
| `insights conviction-matrix --symbol MU` | MIXED, 4.7% ← `.scenario,.confidence_pct`; DP buy 0.547 | — |
| `insights signal-confluence --direction bullish/bearish --min-score 1 --top-n 30` | MU absent both ← `.results[]\|select(.ticker=="MU")` | market-wide |
| `insights price-vs-flow --symbol MU --lookback-days 30` | divergence true, bearish ← `.divergence,.divergence_signal` | +32.24% |
| `insights institutional-accumulation --symbol MU` | NEUTRAL, b/s 1.21 ← `.signal,.buy_sell_ratio`; vwap 1076.66 | — |
| `insights analyst-vs-flow --symbol MU` | no analyst data ← keys `[options_flow,symbol]` | yfinance gap |
| `insights earnings-play --days-until-earnings 30` | MU days_to_earnings 1 ← `.results[]\|select(.ticker=="MU")` | OI +154k/−28k |
| `insights deep-dive --symbol MU` (phase-1) | net_flow −$145.2M, implied 10.91% | whole-tape |

## Tool errors

(none. `analyst-vs-flow` returning no consensus is a yfinance data gap, not a tool error —
recorded; analyst overlay handled in 7b/7c.)

## Cross-check vs phases 1–5

| UW insight | Phase agreement? | Notes |
|---|---|---|
| signal_confluence (MU absent both) | **agrees** phases 1/3 (mixed) | no clean stack ↔ two-sided tape |
| conviction_matrix (MIXED 4.7%) | **agrees** phases 1/3/6 | low-confidence two-sided |
| institutional_accumulation (NEUTRAL) | **partly disagrees** phase-2 headline | overall book balanced; phase-2's accumulation was mega-tier-only (already flagged conviction 3/5) |
| price_vs_flow (bearish divergence) | **agrees** phase-5 (reversal, bearish_flow 88.9%) + phase-6 (semis sold) | the clean directional tilt |
| earnings_play (1d, IV 100) | **agrees** phases 0.5/1/4 | the dominant fact |

## Verdict for downstream phases

- **UW composite bias:** **MIXED (low-confidence), with a mild bearish/reversal tilt** — a
  two-sided vol event; the only clean directional signal is the bearish price-vs-flow divergence.
- **Conviction:** **2/5 directional** (composite confidence is literally 4.7%); **5/5 that
  this is a binary vol event** (earnings tomorrow, IV 100).
- **Phase-9 baseline:** treat the setup as a **defined-risk vol event with a slight downside
  lean**, NOT a directional conviction long or short. Override only with specific contrary
  evidence from phases 7b/7c/8/8b. The mega-tier DP buying (phase-2) and LEAP call buying
  (phase-1) are the bullish counterweights; the divergence + semis-sold + bearish backtest are
  the bearish weight — they roughly cancel on *direction*, leaving the **vol event** as the trade.
- **Open questions:** Do fundamentals (7b) justify the +268% YTD re-rate or impose a valuation
  veto into the print? Does sentiment/SI (7c) show crowding to fade? The composite gives no
  directional edge — 7b/7c/8b must supply the lean or confirm "trade the vol, not the side."
