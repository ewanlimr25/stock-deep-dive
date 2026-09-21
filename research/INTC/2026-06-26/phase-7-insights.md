# Phase 7 — UW Insights Confluence

**Ticker:** INTC
**As-of date:** 2026-06-26
**Generated:** 2026-06-27T10:16:50-0400
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-5-historical.md, phase-6-macro.md

## Summary

UW's composite tools **corroborate the bearish-fade thesis** with one important false
positive to discard. The headline composite signal is **price-vs-flow DIVERGENCE: price
+10.7% over 30d but options flow bearish (net −$50.9M)** — a classic reversal/fade flag —
and the **conviction-matrix classifies INTC as COVERED_CALL** ("dark pool buying + call
selling — yield enhancement, capping upside"; calls sold [bid>ask], puts bought
[ask>bid]). That is the topping/distribution posture phases 1–5 built. The **false
positive: `institutional-accumulation` returns "ACCUMULATION" (buy_sell 1.62)** — but that
buy-skew is the **quarter-end/Russell rebalance artifact phase-2 already dissected** (its
own top price level is $128.32, the after-hours close); the genuine continuous tape is
balanced (phase-2 LARGE tier 51.9% buy), so this tag is **discarded**. INTC sits **outside
both the bearish and bullish `signal-confluence` top-20** (min-score 1) — the direction is
real but it is **not a clean multi-factor confluence stack**, so conviction is capped at
moderate. `analyst-vs-flow`'s UW analyst block is null, but phase-6's web read (targets
$100–103 vs ~$128 spot) means **Wall Street and options flow AGREE — both skeptical of the
price.** Net composite: **mildly-to-moderately BEARISH / topping**, consistent with the
upstream chain.

## Key signals

- **price-vs-flow DIVERGENCE** — "Price up 10.7% but options flow bearish (net −$50.9M)";
  period_low $98.33 → high $141.45 → $128.32 [INSIGHT:price_vs_flow].
- **conviction-matrix = COVERED_CALL** (confidence 13.1%) — cap upside + hedge downside
  [INSIGHT:conviction_matrix].
- **institutional-accumulation "ACCUMULATION" = FALSE POSITIVE** (rebalance artifact;
  phase-2 corrects to balanced) [INSIGHT:institutional_accumulation].
- **Outside top-20 signal-confluence both directions** — real direction, not a clean
  multi-factor stack [INSIGHT:signal_confluence].
- **Whole-tape aggregate (deep-dive)**: net_flow −$50.9M, call $494.5M / put $71.6M (call
  side = financing), P/C 0.582, iv_rank 94.1 [INSIGHT:deep_dive].

## Detailed findings

### Deep-dive snapshot (`insights deep-dive`, as-of 2026-06-26)

| Field | Value | Note |
|---|---|---|
| `call_premium` / `put_premium` | $494.5M / $71.6M | Call side = deep-ITM financing (phase-1) |
| `bullish_premium` / `bearish_premium` | $183.4M / $234.3M | — |
| **derived `net_flow`** | **−$50.9M** | bullish − bearish; bearish |
| `put_call_ratio` | 0.582 | More calls than puts (financing-driven) |
| `iv_rank` / `iv30d` | 94.1 / 0.923 | High-vol regime (phase-4/5) |
| `implied_move_perc` | 0.0065 | **0DTE EOD residual — NOT a multi-day move** (phase-4 corrected; real ~94% IV → ±22% to Jul-17) |
| `total_open_interest` | 4.96M | OI building 30d (phase-5) |
| `next_earnings_date` | 2026-07-23 | Confirmed by web (phase-6) |
| dark-pool premium / avg_price | $2.8B / $128.67 | Rebalance-heavy (phase-2) |

Yahoo fundamentals errored (HTTP 401) — valuation deferred to phase-7b (`fz`/Finnhub).

### Signal confluence

INTC is **not in the bearish top-20 nor the bullish top-20** at `--min-score 1`. Its
composite multi-factor score is below threshold — the bearish direction is genuine
(phases 1/3/6) but does not stack 5+ confirming factors in UW's composite. **Reading: a
real but not overwhelming directional signal → moderate, not maximal, conviction.**

### Conviction matrix

`scenario = COVERED_CALL`, `confidence_pct = 13.1`, `explanation = "Dark pool buying +
call selling — yield enhancement, capping upside."` Underlying: dark-pool buy_ratio 0.618;
options `call_bid_volume 161,655 > call_ask_volume 153,028` (calls **sold**) and
`put_ask_volume 121,195 > put_bid_volume 79,391` (puts **bought**). This is a **collar /
cap-and-hedge** posture — institutions writing calls and buying puts against a name that
has run up. Bearish-leaning (upside capped, downside hedged); the low 13.1% confidence
reflects the mixed dark-pool/flow inputs, not a strong directional short.

### Price vs flow

`divergence = true`, `divergence_signal = "DIVERGENCE: Price is up 10.7% but options flow
is bearish (net flow −$50.9M)"`, `flow_direction = bearish`, `price_change_pct +10.69`,
`period_low 98.33`, `period_high 141.45`, `price_end 128.32`, iv_rank 94.1. **The core
composite reversal signal** — the rally is being faded by flow. Per the heuristic this is
a *leading* reversal that is **often early**; phase-4's long-gamma regime says it resolves
slowly (grind, not cascade), so size/timing accordingly.

### Analyst vs flow

UW `analyst` block = **null** (yfinance thin — known). `options_flow.flow_sentiment =
bearish` (net −$50.9M). Cross-filled from phase-6 web: analyst **avg target $102.70 /
median $100** vs ~$128 spot (price **29–33% above** targets). **So analysts and options
flow AGREE — both skeptical of the current price.** No bull/bear disagreement to exploit;
both lanes lean against the valuation.

### Institutional accumulation — FALSE POSITIVE (discarded)

`signal = "ACCUMULATION — dark pool buy volume significantly exceeds sell volume"`,
`buy_sell_ratio 1.62`, buy 13.5M / sell 8.3M, `top_price_levels` led by **$128.32 ($621M,
4.84M sh, 122 trades)**. **This conflicts with phase-2 and phase-2 wins:** the buy skew is
the **Russell-reconstitution / quarter-end after-hours close-cross** (phase-2: 96.6% of
the largest blocks printed ≥20:00 at $128.32), not directional accumulation; the genuine
continuous LARGE tier is balanced (51.9% buy). **Tag discarded** — do not let phase-9 read
"institutional accumulation" as a bullish offset.

### Earnings play

`earnings-play --days-until-earnings 30` surfaced **ABT (Abbott, Jul-16, 20d)** as its top
setup, **not INTC**. INTC's Jul-23 earnings (28d, within window) is a known binary
(phase-6) but did **not** register as a top pre-earnings IV/OI-ramp setup here — plausibly
because INTC IV is already maxed (iv_rank 94) so there's no fresh ramp to flag. No
additional earnings-vol signal for INTC from this tool.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows |
|---|---|---|
| `insights deep-dive --symbol INTC --date 2026-06-26` | net_flow −$50.9M, iv_rank 94.1 ← `.uw_screener` | whole-tape |
| `insights signal-confluence --direction bearish/bullish --min-score 1` | INTC absent both ← `map(select(.ticker=="INTC"))` | top-20 ×2 |
| `insights conviction-matrix --symbol INTC` | COVERED_CALL, 13.1% ← `.scenario,.confidence_pct` | 1 |
| `insights price-vs-flow --symbol INTC --lookback-days 30` | divergence true, bearish, +10.7% ← `.divergence,.divergence_signal` | 30d |
| `insights analyst-vs-flow --symbol INTC` | analyst null; flow bearish ← `.analyst,.options_flow.flow_sentiment` | 1 |
| `insights institutional-accumulation --symbol INTC` | ACCUMULATION 1.62 (rebalance FP) ← `.signal,.buy_sell_ratio,.top_price_levels` | 1 |
| `insights earnings-play --days-until-earnings 30` | top = ABT, not INTC ← `.results[0]` | top-N |

## Tool errors

- `insights deep-dive .yahoo_fundamentals` → `{"error":"yahoo quoteSummary INTC: HTTP
  401"}` — paid/blocked; valuation handled in phase-7b via `fz`/Finnhub (rule 4).
- No other errors; all reads valid JSON.

## Cross-check vs phases 1–5

| UW insight | Phase agreement? | Notes |
|---|---|---|
| `signal_confluence` (outside top-20) | partial | Phases 1/3 found real bearish direction; UW composite agrees it's not a *clean multi-factor stack* (caps conviction). |
| `conviction_matrix` = COVERED_CALL | **agree** | Coheres with phase-1 (call premium = financing/calls sold), phase-3 (puts bought), phase-2 (mild DP) → cap-and-hedge. |
| `price_vs_flow` = DIVERGENCE bearish | **agree (strong)** | Confirms phases 1/3 (bearish flow) + phase-5 (extended/rallied price) — the reversal/fade. |
| `institutional_accumulation` = ACCUMULATION | **DISAGREE → phase-2 wins** | Rebalance false positive; phase-2 LARGE tier balanced. Discarded. |
| `analyst_vs_flow` | agree | Analysts (web $100–103) + flow both skeptical of $128. |

## Verdict for downstream phases

- **UW composite bias:** **mildly-to-moderately BEARISH / topping** — driven by the
  price-vs-flow bearish divergence and the COVERED_CALL conviction-matrix; the lone bullish
  tag (institutional-accumulation) is a rebalance false positive and is discarded.
- **Conviction:** **3.5 / 5** — coherent bearish stack, but composite confluence is below
  the top-20 threshold (not an extreme multi-factor case) and the divergence is a *leading*
  (early) signal in a long-gamma (slow) regime.
- **Phase-9 baseline:** treat this composite as the BASELINE = **bearish fade of an
  extended rally, expressed defensively** (regime is TRANSITIONAL, divergence is early,
  long-gamma resists fast moves). Override only with specific contrary evidence from
  phases 7b/7c/8/8b.
- **Open questions:**
  - Does fundamentals (phase-7b) justify the 248% re-rate, or confirm the price is ahead
    of itself (analysts say $100–103)? **Pivotal for the fade's durability.**
  - Does sentiment/short-interest (phase-7c) show the bearish positioning is a hedge
    (complacent skew, normal P/C) vs a conviction short — and is there squeeze fuel?
  - Is the bearish divergence going to resolve before Jul-17 OPEX (the put-build expiry),
    or does the long-gamma regime stall it past earnings?
