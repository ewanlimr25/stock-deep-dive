# Phase 7 — UW Insights Confluence

**Ticker:** PATH
**As-of date:** 2026-06-05
**Generated:** 2026-06-06T11:30:00-04:00
**Upstream phases cited:** phase-0.5-context.md, phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-5-historical.md

## Summary

UW's composite stack reads PATH as a **low-confidence directional long**:
conviction-matrix scenario `DIRECTIONAL_LONG` but with **confidence_pct just
21.4**, institutional-accumulation fires `ACCUMULATION` (DP buy/sell ratio
1.84), and price-vs-flow shows **no divergence** ("Price and flow are
aligned", 30d price +8.39% with bullish net flow). But PATH does **not
appear in the market-wide signal-confluence top-20 in either direction even
at `--min-score 1`** — the name has no high-stack confluence today. The
composite is a weak-bullish baseline consistent with phases 1–2 (mild,
capped) and with phase-5's warning that the broader regime is eating bullish
flow.

## Key signals

- Conviction matrix: **`DIRECTIONAL_LONG`, confidence 21.4%** — explanation
  verbatim: "Dark pool buying + aggressive call purchases — institutional
  directional bet."; call ask vol 22,539 > bid 17,248; put ask 7,309 < bid
  8,633 [INSIGHT:conviction_matrix]
- Institutional accumulation: signal verbatim **"ACCUMULATION — dark pool
  buy volume significantly exceeds sell volume"**; buy 3,295,389 vs sell
  1,791,352 (ratio **1.84**), VWAP 11.22, total DP $57,098,217 / 5,086,741 sh
  [INSIGHT:institutional_accumulation]
- Price-vs-flow: **divergence false** — price_start 10.37 → price_end 11.24
  (+8.39%/30d), flow_direction bullish, net_premium_flow +$55,591
  [INSIGHT:price_vs_flow]
- Signal confluence: **PATH absent from top-20 both directions at min-score
  1** (bullish leaders: TLRY/VXX/BITX at score 6) [INSIGHT:signal_confluence]
- Whole-tape aggregates re-confirmed: bullish $2,131,707 vs bearish
  $2,076,116 → derived net_flow +$55,591; P/C 0.39; implied_move_perc 2.238%;
  iv_rank 40.03 [INSIGHT:deep_dive]

## Detailed findings

### Deep dive snapshot

- `uw_screener` (whole tape, reconciles exactly with phase-1 §aggregate and
  phase-0.5): call_premium $3,816,349 / put_premium $899,432;
  bullish_premium $2,131,707 / bearish_premium $2,076,116 → **derived
  net_flow +$55,591** (no `net_flow` key in this block); call_volume 45,372 /
  put_volume 17,735; P/C 0.39; iv30d 0.6474; iv_rank 40.03; implied_move
  $0.2521 / **2.238%**; total OI 815,535; next earnings 2026-09-03.
- `uw_dark_pool`: 485 trades, 5,086,741 sh, $57,098,217, avg price 11.2185 —
  matches phase-2 (block-stratified large 484 + 1 block-tier print).
- `uw_top_oi_changes` top-5: Aug $12C +3,379; Jan-27 $20C +1,603; 0DTE $12C
  +886; Jun-12 $13.5C +601; **Jul-17 $11P +492** (a fifth row phase-3's
  ≥500 cut excluded) — consistent with phase-3.
- `yahoo_fundamentals`: **errored** (`{"error":"yahoo quoteSummary PATH:
  HTTP 401"}`) — no PE/short%/target data from this path; phase-7b owns
  fundamentals via Finnhub/fz.

### Signal confluence (market-wide)

Not present in bullish top-20 (n=20 returned; leaders TLRY/VXX/BITX score 6)
nor bearish top-20 at `--min-score 1`. Absence from a full top-20 list at
min-score 1 means PATH is at best below the 20th-ranked name on score —
either way, **no standout factor stack** on either side. Agrees with
phase-0.5 `BUSY_NAME_NORMAL_DAY`.

### Conviction matrix

`DIRECTIONAL_LONG` @ **21.4%** confidence (thresholds bull 0.6 / bear 0.4;
DP buy_ratio input 0.648). The scenario label matches phase-1/2 direction;
the 21.4% confidence matches their *capped* conviction — UW's own math says
this is the weakest tier of directional-long.

### Price vs flow

No divergence over 30d: price +8.39% (10.37 → 11.24; period range 9.20–13.20)
with bullish cumulative flow. Note this is a *trailing-30d* alignment; the
*last four sessions* (06-02→06-05: −7.0%, −4.2%, 0.0%, −3.7% with three
bearish flow days, phase-5/6) are the live tension the tool's window blurs.

### Analyst vs flow

Tool returned **only** the options_flow block (flow_sentiment "bullish",
net_flow +55,591, P/C 0.39) — **no analyst consensus fields** (yfinance leg
hit the same Yahoo 401). Wall-Street-vs-flow agreement **cannot be assessed
here**; phase-7b/7c to cover analyst posture via WebSearch/Finnhub.

### Institutional accumulation

`ACCUMULATION` — buy 3,295,389 / sell 1,791,352 (1.84), 485 trades, VWAP
11.22. Top single-day price levels all in the **11.11–11.14 flush zone**
(~$15.2M across four ticks) + 11.30 ($3.0M) — i.e. the heaviest off-exchange
absorption happened *at the lows*, which is the accumulation-friendly read
of the same prints phase-2's NBBO classification scored as mixed-to-sell.
Tension noted in the cross-check below.

### Earnings play

Skipped — next earnings 2026-09-03, outside the 30-day window (phase-6
calendar).

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw insights deep-dive --symbol PATH --date 2026-06-05 --json` | net_flow +55,591 ← `.uw_screener.bullish_premium − .bearish_premium` (derived); DP $57,098,217 ← `.uw_dark_pool.total_premium`; yahoo error ← `.yahoo_fundamentals.error` | whole-tape |
| `uw insights signal-confluence --direction bullish --min-score 1 --top-n 20 --date 2026-06-05 --json` | PATH absent ← ticker filter; TLRY 6 ← `.results[:3]` | top-20 |
| `… --direction bearish …` | PATH absent ← same | top-20 |
| `uw insights conviction-matrix --symbol PATH --date 2026-06-05 --json` | DIRECTIONAL_LONG / 21.4 ← `.scenario/.confidence_pct` | aggregate |
| `uw insights price-vs-flow --symbol PATH --lookback-days 30 --json` | divergence false; +8.39% ← `.divergence/.price_change_pct` | 30d |
| `uw insights analyst-vs-flow --symbol PATH --json` | options_flow only; no analyst block ← full output | aggregate |
| `uw insights institutional-accumulation --symbol PATH --json` | ACCUMULATION, 1.84 ← `.signal/.buy_sell_ratio` | 485 trades |

## Tool errors

- `uw insights deep-dive` → `.yahoo_fundamentals` = `{"error":"yahoo
  quoteSummary PATH: HTTP 401"}` (verbatim). Fundamentals snapshot
  unavailable from Yahoo path; phase-7b covers via Finnhub/fz/WebSearch.
- `uw insights analyst-vs-flow` returned no analyst consensus block (same
  Yahoo dependency) — agreement column recorded as not-assessable.

## DATA NOTE / CORRECTION

None — first reads stood (conviction-matrix DP volumes reconcile with
phase-2: 3,160,389 large + 135,000 block = 3,295,389 buy; 484+1 = 485 trades).

## Cross-check vs phases 1–5

| UW insight | Phase agreement? | Notes |
|---|---|---|
| signal_confluence (absent both top-20s) | **agrees** w/ 0.5, 1 | no factor stack — matches BUSY_NAME_NORMAL_DAY + mixed sweeps |
| conviction_matrix (DIRECTIONAL_LONG, 21.4%) | **agrees w/ caveat** w/ 1, 2 | direction matches; 21.4% ≈ their capped 2/5 conviction |
| institutional_accumulation (ACCUMULATION 1.84) | **partial** w/ 2 | phase-2 scored the same prints "mixed, mild accumulation tilt" — NBBO mid-prints at the 11.11–11.14 lows are buy-classified here, sell/mixed there; composite is the more bullish read of identical data |
| price_vs_flow (aligned, +8.39%/30d) | **agrees** w/ 5 | but blurs the 4-session post-squeeze fade phase-5/6 flag |
| analyst_vs_flow | n/a | Yahoo 401 — not assessable |
| (no earnings-play) | agrees w/ 6 | earnings 09-03 out of window |

No upstream phase is contradicted outright; the composite sits at the
bullish end of the same weak-bullish band phases 1–2 establish.

## Verdict for downstream phases

- **UW composite bias:** weak bullish (`DIRECTIONAL_LONG` @ 21.4% +
  `ACCUMULATION` + no divergence; no confluence-stack presence)
- **Conviction:** 2/5
- **Phase 9 baseline:** treat *weak-bullish-with-low-confidence* as the
  baseline; override only with specific contrary evidence from phases 1–8
  (phase-5's 0/8 backtest and phase-6's adverse rotation are exactly such
  evidence on the sizing side)
- **Open questions:** Analyst posture (Yahoo down — 7b/7c must fill); is the
  11.11–11.14 absorption accumulation or distribution-into-liquidity
  (phase-8 desk views should argue both)?
