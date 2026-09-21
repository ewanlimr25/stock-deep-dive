# Phase 7 — UW Insights Confluence

**Ticker:** INTC
**As-of date:** 2026-06-15
**Generated:** 2026-06-16T01:24:55Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-4-structure.md, phase-5-historical.md, phase-6-macro.md

## Summary

UW's composite engine **consolidates to MIXED/NEUTRAL and explicitly flags a
price-vs-flow divergence** — it agrees with the phase-1→5 synthesis and tempers the
phase-6 narrative tailwind. The `conviction-matrix` returns **scenario MIXED at just
5.7% confidence** ("Balanced dark pool — no clear bias") [INSIGHT:conviction_matrix];
INTC is **absent from both the bullish *and* bearish `signal-confluence` top-20**
(no strong directional factor stack) [INSIGHT:signal_confluence];
`institutional-accumulation` reads **NEUTRAL** (buy/sell vol ratio 1.26, "balanced")
[INSIGHT:institutional_accumulation]; and most importantly `price-vs-flow` shows
**DIVERGENCE: price +33.5% but net options flow bearish (−$1.16M)**
[INSIGHT:price_vs_flow] — a leading reversal/mean-reversion caution that lines up
with phase-4's positive-gamma cap and phase-5's extension. The bull case therefore
rests on the *narrative* (phase-6 foundry catalyst + Tech sector flow), the *5-day
sweep persistence* (phase-1), and *mega-tier dark-pool buying* (phase-2) — **not** on
the composite flow signal, which is neutral-to-bearish and diverging. Treat MIXED as
the baseline; phase-9 should only lean long with defined risk and explicit respect
for the divergence. Conviction (that it is genuinely MIXED): 4/5.

## Key signals

- **Conviction matrix: MIXED, confidence 5.7%** — DP buy_ratio 0.557, options
  call_ask 188,912 < call_bid 205,924 (calls net *sold* on volume) [INSIGHT:conviction_matrix].
- **price-vs-flow DIVERGENCE** — "Price up 33.5% but options flow bearish (net
  −$1,162,844)"; period high $132.75 / low $95.6 [INSIGHT:price_vs_flow].
- **INTC absent from bullish AND bearish signal-confluence top-20** (leaders score 6;
  INTC below the factor threshold both ways) [INSIGHT:signal_confluence].
- **Institutional accumulation NEUTRAL** (buy_sell_ratio 1.26, buy 17.6M / sell 14.0M
  sh, DP $4.05B, vwap $128.13) [INSIGHT:institutional_accumulation].
- **Whole-tape aggregate (deep-dive):** call $425.4M / put $97.0M, bull $229.9M ≈
  bear $231.0M → net **−$1.16M**, PCR 0.605, IVR 82.0, implied move 6.17%, earnings
  2026-07-23 [INSIGHT:deep_dive].

## Detailed findings

### Deep-dive snapshot

- `uw_screener`: call_premium $425.4M, put_premium $97.0M, **bullish $229.9M vs
  bearish $231.0M → net_flow −$1.16M** (derived), PCR 0.605, iv_rank 82.0,
  implied_move_perc **6.17%**, next_earnings **2026-07-23**.
- `uw_dark_pool`: avg_price $128.66, total_premium $4.05B, 31.6M sh, 13,288 trades.
- `uw_top_oi_changes`: C97.5 Sep18 +63,781 · P70 Jun18 +25,456 · C140 Jun26 +14,695
  · C150 Aug21 +5,247 (matches phase-3).
- **`yahoo_fundamentals`: ERROR HTTP 401** — Yahoo fundamentals unavailable in the
  deep-dive; phase-7b sources fundamentals from Finnhub/`fz` instead (noted, not a
  blocker).

### Signal confluence

INTC **not in bullish top-20** (`--min-score 1`; leaders GEO/DOMO/SEZL/SPYI/ERII
score 6) and **not in bearish top-20**. INTC's directional factor count is below the
threshold *both* ways → no strong one-sided confluence; consistent with the two-sided
tape.

### Conviction matrix

**scenario MIXED, confidence 5.7%.** DP buy_ratio 0.557 (between bull 0.6 / bear 0.4
thresholds). Options *volume* is net sold both sides: call_ask 188,912 < call_bid
205,924; put_ask 98,140 < put_bid 133,366. "Balanced dark pool activity — no clear
bias." UW will not call this directional.

### Price vs flow

**divergence = true.** "Price is up 33.5% but options flow is bearish (net flow
−$1,162,844)." flow_direction bearish, price_change +33.49% ($95.78→$127.86),
period_high $132.75, period_low $95.6, iv_rank 82. This is the composite's clearest
warning: **the tape is not confirming the price.** Per the heuristic it is a leading
(often early) reversal signal — and phase-4's positive-gamma regime is exactly the
mechanism that would express it as chop/mean-reversion rather than a one-day reversal.

### Analyst vs flow

Flow side: **bearish** (net −$1.16M, PCR 0.605). The analyst block returned thin
(Yahoo 401), so the consensus comes from phases 5–6: **Finviz consensus target
$99.98 (−22%) vs BofA $135 (bull, June 11)**. Read: options traders are *not* leaning
bullish into the rip, and the analyst community is split (consensus lagging the run,
one marquee bull). No clean agreement either way.

### Institutional accumulation

**signal NEUTRAL — "balanced dark pool activity."** buy_sell_ratio 1.26 (buy 17.6M /
sell 14.0M sh), total DP $4.05B, vwap $128.13; top levels $127.86 ($1.03B), $124.57,
$128. Slightly softer than phase-2's "accumulation-leaning" — the composite averages
the whole tape (incl. phase-2's pre-market sell-lean) to neutral, while phase-2's
*mega-tier* (0.583) buy concentration is the nuance underneath. Reconcilable: mega
buys, broad tape balanced.

### Earnings play

**Out of window** — earnings 2026-07-23 is **38 days** out (> 30). `earnings-play`
not run; the setup will be a phase-7c / phase-9 consideration as the date approaches,
not a phase-7 signal now.

## Tool calls (audit trail)

| Command (`--symbol INTC` where scoped) | Key value(s) ← `jq` path | Rows |
|------|------|------|
| `insights deep-dive --date 2026-06-15` | net −$1.16M; yahoo_fundamentals 401 ← `.uw_screener`,`.yahoo_fundamentals` | 1 |
| `insights signal-confluence --direction bullish --min-score 1 --top-n 20` | INTC absent (rank null) | 20 |
| `insights signal-confluence --direction bearish --min-score 1 --top-n 20` | INTC absent | 20 |
| `insights conviction-matrix --date 2026-06-15` | MIXED, 5.7% ← `.scenario`,`.confidence_pct` | 1 |
| `insights price-vs-flow --lookback-days 30` | DIVERGENCE true ← `.divergence`,`.divergence_signal` | 1 |
| `insights analyst-vs-flow` | flow bearish; analyst thin (401) | 1 |
| `insights institutional-accumulation` | NEUTRAL, ratio 1.26 ← `.signal` | 1 |

## Tool errors

- `insights deep-dive` → `yahoo_fundamentals: {"error":"yahoo quoteSummary INTC:
  HTTP 401"}`. Yahoo fundamentals leg unavailable; the UW options/DP/OI blocks
  returned fine. Phase-7b uses Finnhub + `fz` for fundamentals (per skill rule 4).
- `analyst-vs-flow` analyst-consensus block thin (downstream of the same Yahoo 401) —
  flow side intact; consensus taken from phases 5–6 (`fz`/WebSearch).

## Cross-check vs phases 1–5

| UW insight | Phase agreement? | Notes |
|------------|------------------|-------|
| signal_confluence (absent both ways) | phases 1–3 **agree** | two-sided tape, no strong directional stack |
| conviction_matrix (MIXED 5.7%) | phase 1 (mixed-bullish) **agree** | composite even more neutral |
| institutional_accumulation (NEUTRAL) | phase 2 (accum-leaning) **mostly agree** | composite = whole-tape; phase-2 = mega-tier nuance |
| price_vs_flow (DIVERGENCE) | phase 4 (pos-gamma) + phase 5 (extended) **agree** | reversal/mean-reversion caution corroborated |

## Verdict for downstream phases

- **UW composite bias:** **MIXED / NEUTRAL with a downside price-vs-flow divergence
  flag.** Not a clean directional long on the instrumentation.
- **Conviction:** **4/5** that the read is genuinely MIXED (the tools agree
  decisively); directional conviction itself is *low* (matrix 5.7%).
- **Phase-9 baseline:** anchor to MIXED. The bull lean must come from *specific*
  contrary evidence — the phase-6 foundry catalyst + Tech sector flow (persistence
  1.0), phase-1's 5-day sweep persistence, phase-2's mega-tier accumulation — and
  must be expressed with **defined risk** that respects the divergence + positive-gamma
  cap. Do not override MIXED into a high-conviction long.
- **Open questions:**
  - Do the fundamentals justify $128 (foundry turnaround real in the numbers) or is
    this a momentum/narrative re-rate ahead of earnings? → **phase-7b**.
  - Is the crowd euphoric / short-squeeze-driven (complacent call-skew, SI)? →
    **phase-7c**.
  - The desk agents (phase-8) must weigh: real catalyst + sector flow vs neutral
    composite + divergence + extension.
