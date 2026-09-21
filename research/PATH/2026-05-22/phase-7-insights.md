# Phase 7 — UW Insights Confluence

**Ticker:** PATH (UiPath Inc.)
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T00:00:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-4-structure.md, phase-5-historical.md, phase-6-macro.md

## Summary

UW's composite **baseline = low-conviction LONG-lean anchored on dark-pool accumulation,
with the bearish options premium as the dissent** — the same tension phases 1–4 mapped, now
confirmed by the instrumentation. `conviction_matrix` returns **DIRECTIONAL_LONG but at only
37.79% confidence**; `institutional_accumulation` is a firm **ACCUMULATION (buy/sell 6.11×)**;
and `price_vs_flow` explicitly flags **DIVERGENCE — price +8% over 30d while net options
flow is bearish (−$398,934)**. PATH is **absent from the top-50 bullish signal_confluence**
(it has `dp_accumulation` + `oi_building` + `low_pcr` but lacks `bullish_flow` and carries
*high*, not cheap, IV). Net: the UW composite agrees with phase-2/3/4 (accumulation +
call-skew + positive DEX lean) and treats phase-1's bearish sweeps as the overwriting
counterweight — but flags low confidence and an unresolved divergence into the binary
05-28 event. **Phase-9 baseline: neutral-to-mildly-long, expressed through defined-risk
given the rich IV.**

## Key signals

- **conviction_matrix = DIRECTIONAL_LONG**, confidence **37.79%**; "dark pool buying + aggressive call purchases — institutional directional bet" [INSIGHT:conviction_matrix]
- **institutional_accumulation = ACCUMULATION**, buy/sell ratio **6.11**, buy 2,041,093 / sell 334,020 sh, vwap $10.94 [INSIGHT:institutional_accumulation]
- **price_vs_flow = DIVERGENCE** — price +8.0% (10.12→10.93, range 9.2–11.3) vs net flow −$398,934 bearish [INSIGHT:price_vs_flow]
- **signal_confluence (bullish): PATH absent from top-50** (all ≥ score 5) — its bullish stack is incomplete (no bullish_flow, high IV) [INSIGHT:signal_confluence]
- **Whole-tape aggregates** (reconcile w/ phase-1): call_prem $3.42M vs put_prem $1.54M; bullish $1.65M vs bearish $2.05M; net_flow **−$398,934**; P/C 0.31; implied_move ~**11.8%**; iv_rank 84 [INSIGHT:deep_dive]

## Detailed findings

### Deep-dive snapshot (directional aggregates)

From phase-0.5/1 `insights_deep_dive.uw_screener` (whole tape):
`bullish_premium 1,649,236` < `bearish_premium 2,048,170` → **net_flow −$398,934**;
`call_premium 3,417,150` vs `put_premium 1,540,712`; P/C **0.31**; `iv_rank 84.0`;
`implied_move 0.118` (~11.8%); `next_earnings 2026-05-28`; DP avg $10.95; total OI 689,415.
Reconciles exactly with phase-1 — net-bearish premium, call-heavy volume (overwriting +
lottery), high IV. **Phase-9 N4 sizes structures to the ~11.8% implied move.**

### Signal confluence (bullish)

`min_score=1, top_n=50` returned 50 names **all scoring ≥5** — **PATH is not among them**.
Top scorers (QSI/SKYT/TE = 6) stack `bullish_flow + low_pcr + volume_spike + dp_accumulation
+ oi_building + low_iv_cheap_options`. PATH plausibly holds 3 of these (`low_pcr 0.31`,
`dp_accumulation`, `oi_building`) but **fails `bullish_flow` (net-bearish) and `low_iv`
(IV is rich, not cheap)** — so its bullish confluence is mid-low and below the top-50
cutoff. Consistent with phase-1 (not bullish flow) and phase-5 (no directional edge).

### Conviction matrix (scenario)

`scenario = DIRECTIONAL_LONG`, **confidence 37.79%**. Inputs: dark_pool buy_ratio **0.859**
(buy 2.04M / sell 0.33M); options_flow call_ask 25,240 vs call_bid 23,432 (marginally
ask-heavy calls), put_ask 5,835 vs put_bid 5,424. UW's weighting tips this to LONG on the
**DP buy dominance + slightly net-bought calls**, but the **low 37.8% confidence** reflects
the conflicting bearish premium. This is UW *overriding* phase-1's bearish tag toward long
via the accumulation weight — but weakly. Note it labels the calls "aggressive purchases,"
whereas phase-3 showed much of the larger call OI was *written*; the matrix reads net
ask/bid volume, not OI-opening side, so treat its "directional bet" framing as
**accumulation-driven, not call-buying-driven**.

### Price vs flow (divergence)

`divergence = true`: "Price is up 8.0% but options flow is bearish." Period 10.12→10.93,
high 11.3, low 9.2. Per the heuristic, bearish-flow-with-rising-price is a *potential*
early reversal signal — **but** phase-4's long-gamma + positive DEX + call-skew structure
*supports* the price side, and phase-3 shows the "bearish flow" is largely overwriting. So
the most coherent reading is **the rising price/accumulation is the real signal and the
bearish premium is hedging/overwriting noise**, not an imminent bearish reversal. The
divergence is the central ambiguity the 05-28 print will resolve.

### Analyst vs flow

`analyst_vs_flow` returned **only the options-flow block** (flow_sentiment bearish, net
−$398,934) — **no Wall Street consensus** (yfinance fundamentals 401'd, per phase-0.5). So
no analyst-vs-flow agreement read here; **phase-7c must source consensus via WebSearch/
Finnhub**.

### Institutional accumulation

`signal = ACCUMULATION` — buy/sell **6.11×**, buy 2,041,093 / sell 334,020 sh, total DP
premium $25.99M, vwap $10.94, price_30d +8%. Top levels: **$10.93 ($10.76M / 984,806 sh /
6 trades)**, $11 ($3.25M), $10.94 ($3.12M), $10.88 ($1.00M), $11.05 ($0.97M). Strongly
confirms phase-2 — **same caveat**: the $10.93 level is dominated by the 4:00 PM 900K close
block (possible benchmark/rebalance), and phase-4 showed part of the DP bid is dealer
delta-hedging (DEX +$28M). Real accumulation, partially mechanical.

### Earnings play

PATH is **outside the top-25 by iv_rank** (the list floors at iv_rank ~91; PATH = 84) but
**is a valid 6-day earnings setup**. The 05-27/05-28 tech-earnings cluster is heavy and
includes concurrent blueprint **NTAP** (05-28, implied move 10.6%, P/C 0.18, balanced
premium) plus DELL (05-28, +bullish), ADSK, OKTA, DLTR. Reinforces phase-6: a crowded
tech-earnings window; PATH's ~11.8% implied move is among the larger in the cohort.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__insights_signal_confluence` | `{direction: bullish, min_score: 1, top_n: 50}` | PATH absent from top-50 (all ≥5) |
| `mcp__uw-pp__insights_conviction_matrix` | `{symbol: PATH}` | DIRECTIONAL_LONG, conf 37.79%, DP buy_ratio 0.859 |
| `mcp__uw-pp__insights_price_vs_flow` | `{symbol: PATH, lookback: 30}` | DIVERGENCE: price +8% vs flow bearish |
| `mcp__uw-pp__insights_analyst_vs_flow` | `{symbol: PATH}` | Only flow (bearish); no analyst consensus |
| `mcp__uw-pp__insights_institutional_accumulation` | `{symbol: PATH}` | ACCUMULATION, 6.11× buy/sell |
| `mcp__uw-pp__insights_earnings_play` | `{days_until: 14, min_iv_rank: 40, top_n: 25}` | PATH outside top-25 by IV rank; 5/28 cluster (NTAP/DELL) |

## Tool errors

None fatal. `analyst_vs_flow` lacks consensus (yfinance auth) — handed to phase-7c.

## Cross-check vs phases 1–5

| UW insight | Phase agreement? | Notes |
|------------|------------------|-------|
| signal_confluence (bullish) | agrees phase-1/5 | PATH not a bullish-confluence name; no directional edge |
| conviction_matrix DIRECTIONAL_LONG (37.8%) | agrees phase-2/3/4, overrides phase-1 weakly | Accumulation-driven long-lean, low confidence |
| price_vs_flow DIVERGENCE | matches the phase-1↔2 tension | Structure (phase-4) supports price side → flow likely hedging |
| institutional_accumulation ACCUMULATION | strongly agrees phase-2 | 6.11×; close-block + dealer-hedge caveat carried |

## Verdict for downstream

- **UW composite bias:** **mildly LONG (DIRECTIONAL_LONG) at LOW confidence (37.79%)** —
  accumulation-anchored, with an unresolved price-up-vs-flow-bearish divergence.
- **Conviction:** **2.5/5** — the composite confirms accumulation but explicitly flags low
  confidence + divergence, and PATH is not a bullish-confluence name.
- **Phase-9 treatment:** Use this as the **BASELINE = neutral-to-mildly-long**, and only
  override with specific contrary evidence. Given rich IV (phase-5 VRP +43.7), the binary
  05-28 event, and TRANSITIONAL/half-size macro (phase-6), the natural expression is a
  **defined-risk structure**, not a leveraged directional bet. Do not read the matrix's
  "aggressive call purchases" as conviction call-buying — phase-3 showed the big call OI was
  largely *written*.
- **Open questions:**
  - Will the 05-28 print resolve the divergence in favor of the accumulation (up) or the
    bearish premium (down)? → phase-7b fundamentals + phase-7c sentiment + phase-8 debate.
  - How much of the ACCUMULATION is genuine vs close-block/dealer-hedging? → already
    de-rated; phase-9 should size cautiously.
  - What is Street consensus + revisions into the print (missing here)? → phase-7c.
