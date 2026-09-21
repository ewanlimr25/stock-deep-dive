# Phase 7 — UW Insights Confluence

**Ticker:** RKT
**As-of date:** 2026-07-17
**Generated:** 2026-07-19T20:02:00-04:00
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-5-historical.md, phase-6-macro.md

## Summary

UW's own composite instrumentation independently lands on **MIXED / low-conviction**,
confirming the synthesized read from phases 1–6. `conviction-matrix` returns
**MIXED (confidence 9.3%)** — "balanced dark pool activity, no clear bias." The
sharpest composite signal is `price-vs-flow`, which flags a **formal DIVERGENCE:
"Price is up 9.9% but options flow is bearish (net flow −$364,914)"** — the exact
tension phase-5 surfaced. `institutional-accumulation` is *labeled* NEUTRAL yet
carries a **buy/sell ratio of 1.46** (buy 9.67M vs sell 6.62M sh) — a mild
accumulation lean underneath the neutral tag, matching phase-2. RKT appears in
**neither** the bullish nor bearish `signal-confluence` top-50 → it is not a
high-confluence directional name in either direction. Net: the UW baseline is a
range-bound / capped name with bearish flow diverging from a risen price — treat as
**MIXED baseline**; directional risk requires specific edge phases 1–6 did not supply.

## Key signals

- **conviction-matrix MIXED, confidence 9.3%** — "balanced, no clear bias" `[INSIGHT:conviction-matrix]`
- **price-vs-flow DIVERGENCE = TRUE:** price +9.9% vs bearish net flow −$364,914 → reversal-watch / flow-is-hedging `[INSIGHT:price-vs-flow]`
- **institutional-accumulation buy/sell ratio 1.46** (buy 9.67M / sell 6.62M sh), labeled NEUTRAL → mild accumulation underneath `[INSIGHT:institutional-accumulation]`
- **RKT absent from both bullish & bearish signal-confluence top-50** → no strong directional confluence either way `[INSIGHT:signal-confluence]`
- **analyst-vs-flow: flow-only (no analyst consensus returned)** — flow_sentiment bearish, net −$364,914; Wall-Street side unavailable `[INSIGHT:analyst-vs-flow]`

## Detailed findings

### Deep-dive snapshot (whole-tape aggregates) `[INSIGHT:deep-dive]`

From the `uw_screener` block (same as phase-0.5/phase-1):
- bullish_premium **$758,711** vs bearish_premium **$1,123,625** → **net_flow (derived)
  −$364,914** (bearish).
- call_premium $1,563,016 vs put_premium $605,907; **put_call_ratio 0.502**.
- **iv_rank 51.7**, iv30d 0.694, **implied_move_perc 0.63%** (1-day; phase-9 N4 sizes
  the *earnings-tenor* ±8–10% from phase-6, not this figure).
- next_earnings_date **2026-07-30**.
- dark_pool (composite) buy_ratio **0.593** / 1,429 trades — accumulation lean.

Reconciles cleanly with phase-1 (net −$364,914 identical) and phase-0.5 `[CTX:]`.

### Signal confluence `[INSIGHT:signal-confluence]`

- **RKT not in bearish top-50 nor bullish top-50** (both lists full at 50, RKT absent
  from each). Its directional confluence score is below the cutoff on both sides →
  **no strong stacked signal either direction.** Agrees with the MIXED read.

### Conviction matrix `[INSIGHT:conviction-matrix]`

- **Scenario: MIXED**, confidence **9.3%**. Explanation: "Balanced dark pool activity
  — no clear bias."
- options_flow detail: call_ask 9,079 / call_bid 11,756 (**calls net sold**), put_ask
  7,562 / put_bid 2,501 (**puts net bought**) → the same bearish-delta / overwrite
  signature from phase-1.
- dark_pool detail: buy_ratio **0.593** (buy 9.67M / sell 6.62M, 1,429 trades) →
  accumulation lean, echoing phase-2's large-tier 0.651.
- Not a clean COVERED_CALL/HEDGED_LONG label from the tool, but the *components*
  (calls sold + puts bought + dark-pool buying) = the hedged/overwritten-long picture.

### Price vs flow `[INSIGHT:price-vs-flow]`

- **DIVERGENCE = TRUE.** Signal: *"Price is up 9.9% but options flow is bearish (net
  flow −$364,914)."* price_start $13.23 → price_end $14.54.
- Reading (paired with phase-4 dealer regime, per heuristic): in a **long-gamma /
  range** regime this divergence is more "**flow is hedging/overwriting a risen,
  accumulated stock**" than an imminent reversal — but it is a genuine
  **reversal-watch** flag and caps upside conviction. Phase-8b should stress it.

### Analyst vs flow `[INSIGHT:analyst-vs-flow]`

- Returned **flow-only**: flow_sentiment bearish, net_flow −$364,914, PCR 0.502.
- **No analyst consensus / price target surfaced** (yfinance side unavailable — cf.
  the deep-dive Yahoo 401 in phase-0.5). Wall-Street-vs-flow agreement **cannot be
  scored here** → defer analyst read to phase-7b/7c (Finnhub/fz/WebSearch).

### Institutional accumulation `[INSIGHT:institutional-accumulation]`

- **Signal label: NEUTRAL** — "balanced dark pool activity." But **buy_sell_ratio
  1.46** (buy_side 9,665,188 / sell_side 6,620,756 sh), total_dp_premium $238.3M,
  vwap $14.63, price_30d +9.9%.
- top_price_levels: **$14.54 (3.88M sh, $56.5M)** heaviest, then $14.76/$14.77/$14.53/
  $14.51 — same $14.5 cluster as phase-2. The 1.46 buy ratio **leans accumulation**
  despite the NEUTRAL tag → consistent with phase-2's "mild accumulation."

### Earnings play

- `earnings-play --days-until-earnings 30` returned **no RKT row** (RKT not among the
  tool's top-ranked IV/OI-buildup earnings setups). Not an error — earnings *is*
  07-30 (13 days out, in-window), but RKT's setup didn't rank as a standout play.
  Phase-7c/earnings context carries the event read.

## Tool calls (audit trail)

| Command | Key value(s) ← `jq` path | Rows |
|---|---|---|
| `uw insights conviction-matrix --symbol RKT --date 2026-07-17` | MIXED, conf 9.3%, dp buy_ratio 0.593 ← `.scenario`/`.confidence_pct`/`.dark_pool.buy_ratio` | 1 |
| `uw insights price-vs-flow --symbol RKT --lookback-days 30` | DIVERGENCE true, "+9.9% vs bearish −$364,914" ← `.divergence`/`.divergence_signal` | 1 |
| `uw insights institutional-accumulation --symbol RKT` | NEUTRAL, buy_sell_ratio 1.46 ← `.signal`/`.buy_sell_ratio` | 1 |
| `uw insights analyst-vs-flow --symbol RKT` | flow-only, bearish; no analyst data ← `.options_flow` | 1 |
| `uw insights signal-confluence --direction bearish/bullish --min-score 1 --top-n 50` | RKT absent from both | 50+50 |
| `uw insights earnings-play --days-until-earnings 30` | no RKT row | — |

## Tool errors

None. `analyst-vs-flow` omitting the analyst side (yfinance unavailable) and RKT's
absence from `signal-confluence`/`earnings-play` are **findings**, not errors.

## Cross-check vs phases 1–5

| UW insight | Phase agreement? | Notes |
|---|---|---|
| signal_confluence (RKT absent both) | **agrees** phases 1–4 | no strong directional confluence — matches the MIXED synthesis |
| conviction_matrix = MIXED | **agrees** phase 1 (bearish flow) + phase 2/3 (accum/range) | components = overwritten/hedged long |
| institutional_accumulation (1.46 buy) | **agrees** phase 2 | mild accumulation under a NEUTRAL label |
| price_vs_flow = DIVERGENCE | **agrees** phase 5 | confirms bearish-flow-into-rising-price; reversal-watch |

Internally consistent — UW's composite reproduces the multi-phase read with no
contradiction. No upstream phase needs override on the basis of phase-7.

## Verdict for downstream phases

- **UW composite bias: MIXED / low-conviction (9.3%)** — range-bound, capped,
  bearish flow diverging from a +9.9% risen & mildly-accumulated stock.
- **Conviction: 3 / 5** — high *consistency* (every composite tool agrees), but the
  composite verdict itself is explicitly MIXED, so it constrains rather than directs.
- **Phase 9 should treat MIXED as the BASELINE** and only take a directional lean with
  specific contrary edge from phases 8/8b — which the evidence so far does **not**
  supply. The natural expression is **non-directional / defined-risk around the 07-30
  event**, not a clean long or short.
- **Open questions:** does fundamentals (7b) resolve the divergence — is the +9.9% run
  fundamentally justified (integration accretive) so bearish flow is just hedging, or
  is it extended (bearish flow front-running a disappointment)? Does 7c show short
  interest building that would make the divergence a squeeze/838 setup?
