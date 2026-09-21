# Phase 7 — UW Insights Confluence

**Ticker:** CRM
**As-of date:** 2026-06-05
**Generated:** 2026-06-06T16:50:00-04:00
**Upstream:** phase-1-flow.md (MIXED 2/5), phase-2-dark-pool.md (balanced today /
weekly distribution), phase-3-positioning.md (call-supply ceiling),
phase-4-structure.md (FULLY_NEGATIVE gamma), phase-5-historical.md
(premium-buying regime), phase-6-macro.md (HEADWIND 4/5)

## Summary

UW's own confluence machinery is **unanimously neutral on the single-day,
single-name axis**: conviction-matrix scenario `MIXED` at **3.7% confidence**
("Balanced dark pool activity — no clear bias"), CRM **absent from both** the
bullish and bearish signal-confluence top-20 even at `--min-score 1`,
price-vs-flow `divergence: false` ("Price and flow are aligned"), and
institutional-accumulation `NEUTRAL` (DP buy/sell 1.16). This **agrees with
phases 1–2's day-scoped reads** (flat tape, balanced DP) and confirms the run's
internal consistency — but the composite tools are day/30d-scoped and
structurally blind to the three things that ARE firing: the 5-session bearish
sweep campaign (phase-1), the dealer-gamma collapse into FULLY_NEGATIVE
(phase-4/5), and the sector-wide AVGO de-rating shock (phase-6). Baseline for
phase-9: **NEUTRAL day-tape, with the directional tilt carried entirely by
structure + macro, not by flow confluence.**

## Key signals

- **Conviction matrix: `MIXED`, confidence 3.7%** (thresholds bull 0.6 / bear
  0.4); DP buy_ratio 0.537 (717,472 buy vs 617,731 sell, 643 trades); options
  ask/bid: call_ask 20,205 vs call_bid 26,675 (calls net SOLD at bid — matches
  phase-1's `[FLOW:aggressor_ex0dte DUCKDB]` net call selling), put_ask 12,924
  vs put_bid 13,918 (puts net sold too). `[INSIGHT:conviction_matrix]`
- **Signal confluence: CRM scores below the board both ways** — absent from
  bullish AND bearish top-20 at min-score 1 (day's 6-factor names: TLRY/VXX/
  BITX bullish; MTUM/IRDM bearish). No stacked signal either direction.
  `[INSIGHT:signal_confluence]`
- **Price vs flow: NO divergence** — 30d lookback price +4.21% (178.16 →
  185.66, period range 164.33–211.34), flow_direction "bullish" (net +$1.28M);
  aligned, no reversal flag. `[INSIGHT:price_vs_flow]`
- **Institutional accumulation: `NEUTRAL — balanced dark pool activity`**;
  buy_sell_ratio 1.16, VWAP 186.49, avg trade 186.98, total DP $249.0M /
  1,335,203 sh (reconciles exactly with phase-2's 6/05 day figures); top level
  185.66 ($78.4M — the closing crosses phase-2 flagged).
  `[INSIGHT:institutional_accumulation]`
- **Analyst-vs-flow degraded to flow-only** (yahoo consensus block failed,
  §Tool errors): flow_sentiment "bullish", net_flow +$1,279,551 — the same
  derived bullish−bearish figure as phases 0.5/1. No analyst leg available
  here; phase-0's `fz` snapshot carries the sell-side view (target 247.46 ≈
  +33% vs spot). `[INSIGHT:analyst_vs_flow]`

## Detailed findings

### Deep dive snapshot

`uw_screener` directional aggregates (whole tape, reconciled with phase-1):
bullish_premium **$23,016,041** vs bearish_premium **$21,736,490** → derived
**net_flow = +$1,279,551** (deep-dive has no `net_flow` key); call_premium
$26.64M vs put_premium $21.02M; P/C ratio 0.57 (call vol 50,764 / put vol
28,811); iv_rank 60.0; iv30d 0.450; **implied_move $1.04 / 0.56%** (phase-9 N4
input); total OI 1,082,070; next earnings 2026-09-02. Matches phase-0.5's
`[CTX:]` block and phase-1's aggregate — consistent. `uw_dark_pool` block:
$249.0M / 1,335,203 sh / 643 trades, avg 186.98 (= phase-2). `uw_top_oi_changes`:
identical top-6 all-call build list as phase-3 (195C/200C 0DTE, 6/18
220C/210C, 7/17 220C). Yahoo fundamentals: **errored** (§Tool errors) — P/E
21.49 / fwd 11.95 / target 247.46 carried from phase-0 `fz` instead.
`[INSIGHT:deep_dive]`

### Signal confluence

CRM absent from bullish top-20 and bearish top-20 at `--min-score 1` (n=20
each; caveat: top-n truncation means "not in the day's top-20 stacked names"
— with max scores of 6 on both boards, CRM's score is ≤ the 20th name's, i.e.
no meaningful stack). `[INSIGHT:signal_confluence]`

### Conviction matrix

`scenario: MIXED`, `confidence_pct: 3.7`, explanation verbatim: "Balanced dark
pool activity — no clear bias." Inputs as §Key signals. The ask/bid splits are
the same income-tape signature phase-1's DuckDB cut found: both calls and puts
net traded at bid. `[INSIGHT:conviction_matrix]`

### Price vs flow

`divergence: false` — "Price and flow are aligned." 30d: price_start 178.16 →
price_end 185.66 (+4.21%), high 211.34 / low 164.33; flow bullish +$1.28M.
Note the 30d window nets out the round-trip (notably: the +19% spike and −11%
fade cancel) — alignment at window-scale, churn inside it. No reversal signal
fired. `[INSIGHT:price_vs_flow]`

### Analyst vs flow

Returned options_flow block only (flow_sentiment "bullish", net_flow
+$1,279,551, P/C 0.57); analyst consensus leg missing because the yfinance
call failed (§Tool errors) — agreement cannot be scored here. External
context: `fz` target 247.46 (+33%) and the 5-session options tape pressing
bearish = Wall Street constructive, aggressive flow skeptical — a
disagreement, but sourced from phase-0/1, not this tool.
`[INSIGHT:analyst_vs_flow]`

### Institutional accumulation

`signal: "NEUTRAL — balanced dark pool activity"`; buy 717,472 vs sell 617,731
(ratio 1.16); price_30d_change +4.21%; VWAP 186.49. Top price levels all
186±0.75 (today-scoped). Agrees with phase-2's day verdict; phase-2's *weekly*
distribution read (volume-at-highs decay) is outside this tool's scope.
`[INSIGHT:institutional_accumulation]`

### Earnings play

Skipped — next earnings 2026-09-02, outside the 30-day window (phase-6
calendar). Not a tool error.

## Tool calls

| Command | jq path | Status |
|---|---|---|
| `uw insights deep-dive --symbol CRM --date 2026-06-05 --json` | `.uw_screener` / `.uw_dark_pool` / `.uw_top_oi_changes[:5]` / `.yahoo_fundamentals` | ok except yahoo block (below) |
| `uw insights signal-confluence --direction bullish/bearish --min-score 1 --top-n 20 --date 2026-06-05 --json` | filter `.results[] ticker=="CRM"` | ok — absent both |
| `uw insights conviction-matrix --symbol CRM --date 2026-06-05 --json` | `.scenario/.confidence_pct/.dark_pool/.options_flow` | ok |
| `uw insights price-vs-flow --symbol CRM --lookback-days 30 --json` | `.divergence/.divergence_signal/.price_change_pct` | ok (trailing window anchors latest=as-of ✓) |
| `uw insights analyst-vs-flow --symbol CRM --json` | `.options_flow` (analyst leg absent) | degraded |
| `uw insights institutional-accumulation --symbol CRM --json` | `.signal/.buy_sell_ratio/.vwap` | ok |
| `uw insights earnings-play` | — | skipped (earnings 2026-09-02 > 30d) |

## Tool errors

- `uw insights deep-dive` → `.yahoo_fundamentals.error: "yahoo quoteSummary
  CRM: HTTP 401"` (verbatim). Yahoo auth/rate-limit; fundamentals carried from
  phase-0 `fz` snapshot instead and phase-7b will source Finnhub/fz directly.
- `uw insights analyst-vs-flow` returned no analyst-consensus block (same
  yfinance dependency) — scored as "degraded", flow leg only.

## Cross-check vs phases 1–5

| UW insight | Phase agreement? | Notes |
|---|---|---|
| signal_confluence (none either way) | **agrees** w/ phase-1 MIXED 2/5, phase-0.5 BUSY_NAME_NORMAL_DAY | no stack to trade off |
| conviction_matrix MIXED 3.7% | **agrees** w/ phase-1 (flat aggregate, calls+puts net sold) & phase-2 day-read | day-scope only |
| institutional_accumulation NEUTRAL | **agrees** w/ phase-2 today; **silent** on phase-2's weekly distribution (out of scope) | weekly read stands |
| price_vs_flow no-divergence | consistent w/ phase-5 (no sentiment extreme); window nets out the round-trip | not a contradiction, a resolution-scale artifact |
| analyst_vs_flow (degraded) | — | sell-side +33% target vs 5d bearish sweeps = phase-8 debate fodder |

**Where the composite is blind (carried by other phases):** bearish sweep
persistence 5/5 ($211M, phase-1), GEX collapse to FULLY_NEGATIVE (phase-4,
flip 6/04 per phase-5), AVGO sector shock + tech outflow −$807.6M (phase-6).

## Verdict for downstream

- **UW composite bias: NEUTRAL / MIXED** — every native confluence tool reads
  no-edge on the day tape.
- **Conviction: 2/5** (high internal consistency, low informational yield).
- **Phase-9 baseline instruction:** treat NEUTRAL as the baseline; the only
  legitimate overrides are the specific contrary evidence streams the
  composite can't see — (a) phase-4 dealer structure (FULLY_NEGATIVE gamma,
  vanna seller), (b) phase-1 sweep persistence (bearish 5/5), (c) phase-6
  macro headwind (AVGO shock + rotation OUT + regime "half size"), all of
  which point the same direction: **downside path risk exceeds upside until
  190–195 reclaims or the 6/18 OPEX cliff clears.**
- **Open questions:** Do fundamentals (7b) veto a short at 11.95× forward
  P/E with a $25B ASR bid? Does short interest 7.91% float (7c) make the
  downside crowded? What do the desk agents make of max-pain-above-spot vs
  short-gamma-below (phase-8)?
