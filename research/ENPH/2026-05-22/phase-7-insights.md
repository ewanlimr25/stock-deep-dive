# Phase 7 — UW Insights Confluence

**Ticker:** ENPH
**As-of date:** 2026-05-22
**Generated:** 2026-05-25T22:43:20Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-5-historical.md, phase-6-macro.md

## Summary

UW's composite instrumentation **confirms the bullish stack and resolves the
overwrite/hedge question in favor of genuine direction**: `conviction_matrix` =
**DIRECTIONAL_LONG** ("dark pool buying + aggressive call purchases — institutional
directional bet"), `institutional_accumulation` = **ACCUMULATION** (buy/sell 2.3×,
buy ratio 0.697), and `price_vs_flow` shows **no divergence** (flow bullish, price
+104%, aligned). This is, per the rubric, the strongest bullish category the skill's
tooling produces. **But two tempering facts keep it from a max read:** (1) ENPH is
**absent from the top-50 bullish `signal_confluence` list** — its score is only ~4/6
(bullish_flow + low_pcr + dp_accumulation + oi_building) and is **penalized on exactly
the two factors that mark a fresh entry: it is NOT cheap (no `low_iv_cheap_options`,
IV-rank 92) and NOT a fresh `volume_spike`** — i.e. UW's own composite agrees with
phase-5 that the setup is *confirmed-but-mature/rich*; (2) the only analyst anchor (GS
PT **$57**, phase-6) is **already below spot $64** — price has run past the bull case.
Baseline UW bias: **BULLISH / DIRECTIONAL_LONG, conviction 4/5**, with "mature & rich"
attached.

## Key signals

- `conviction_matrix` = **DIRECTIONAL_LONG** — institutional directional bet [INSIGHT:conviction_matrix]
- `institutional_accumulation` = **ACCUMULATION**, buy/sell 2.3×, buy ratio 0.697 [INSIGHT:institutional_accumulation]
- `price_vs_flow` = **no divergence**, price +104.11% (low $29.90 → $64.03) [INSIGHT:price_vs_flow]
- **ENPH absent from top-50 confluence** — score ~4/6, missing cheap-IV + volume-spike [INSIGHT:signal_confluence]
- Whole-tape aggregate: bullish $18.09M vs bearish $12.54M, **net +$5.55M, P/C 0.39** [INSIGHT:deep_dive]

## Detailed findings

### Deep-dive snapshot + directional aggregates

From `insights_deep_dive` (phase-0.5) — the whole-tape `uw_screener` block:

| Field | Value |
|-------|-------|
| call_premium / put_premium | $27.64M / $8.81M (**3.14:1**) |
| bullish_premium / bearish_premium | $18.09M / $12.54M |
| **net_flow** | **+$5,548,739** |
| put_call_ratio | 0.392 |
| iv_rank / iv30d | 92.06 / 101.3% |
| implied_move / implied_move_perc | 0.2957 / **0.46% (UNRELIABLE — use phase-4 ±16.5%/1wk, ±28%/27d for N4)** |
| total_open_interest | 457,179 |
| dark pool | $74.7M / 1.18M sh @ avg $63.38 |
| next earnings | 2026-07-28 (out of window) |

Reconciles cleanly with phase-1's aggregate and phase-0.5's `[CTX:]` rank (net_dir
99.5 pctile). **Phase-9 N4: do NOT use the 0.46% implied move — use the phase-4
term-structure-derived expected move.**

### Signal confluence (the tempering signal)

`direction=bullish, min_score=1, top_n=50`: **ENPH does NOT appear** in the top-50
(all displayed names score 5–6). ENPH's factor set is **bullish_flow ✓, low_pcr ✓
(0.39), dp_accumulation ✓ (0.70), oi_building ✓ (20 sessions)** = **score ≈ 4** — but it
**lacks `volume_spike`** (volume not a clean 2× — see phase-0.5) **and
`low_iv_cheap_options`** (IV-rank 92 = expensive). So UW's composite independently
reaches phase-5's conclusion: **the bullish factors are present, but the setup is mature
and the options are rich — not a fresh, cheap, exploding entry.** (Top-confluence
peers today: QSI/SKYT/TE score 6; ACHR/ASTS/F/HON score 5 — all *cheaper-IV* names.)

### Conviction matrix — DIRECTIONAL_LONG

`scenario: DIRECTIONAL_LONG`, dark_pool buy_ratio **0.697** (>0.6 bull), options_flow
call_ask 21,538 > call_bid 18,656 (calls bought) and put_bid 9,280 > put_ask 5,230
(puts sold) — **both legs bullish.** Explanation: "Dark pool buying + aggressive call
purchases — institutional directional bet." This **resolves the phase-1/3 open question**
(overwrite vs genuine long) → **genuine directional long.** (`confidence_pct` 23.3 is the
tool's internal calibration field, low in absolute terms — I read the *scenario label*,
the clearest bullish bucket, as the signal; the low confidence % is consistent with the
"mature/rich" caveat.)

### Price vs flow — aligned, no reversal

`divergence: false`, "Price and flow are aligned." `price_change_pct +104.11%`
($31.37 → $64.03; period low $29.90, high $64.94). **No leading-reversal divergence** —
but note this is "bullish flow confirming a doubled price," i.e. momentum confirmation,
not a fresh edge. Pair with phase-4's long-gamma pin: aligned ≠ more upside guaranteed.

### Analyst vs flow

UW returned **only the options_flow block (bullish)** — the **analyst/consensus block is
absent** (yfinance 401, same as phase-0.5's `yahoo_fundamentals` error). Substituting
phase-6's WebSearch: **Goldman Sachs PT = $57**, and **spot $64 is already above it.**
So the read is **flow bullish, but price has exceeded the marquee Street target** → a
*caution* (analysts now lag price), not a confirmation. Phase-7b will source full
fundamentals from Finnhub.

### Institutional accumulation — ACCUMULATION

`signal: ACCUMULATION`, `buy_sell_ratio 2.3`, buy 819,283 vs sell 355,977 sh,
vwap $63.56, avg $63.38. Top level **$64.03 ($22.7M, 354,749 sh, 9 trades)** = the EOD
blocks from phase-2. **Confirms phase-2 strongly** (phase-2 whole-day ~64% buy; this
0.697 buy ratio is consistent).

### Earnings play

**Skipped** — earnings 2026-07-28 is outside the 30-day window (phase-6 calendar).

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `insights_signal_confluence` | `{direction: bullish, min_score: 1, top_n: 50, date: 2026-05-22}` | ENPH absent (score ~4; missing cheap-IV + vol-spike) |
| `insights_conviction_matrix` | `{symbol: ENPH, date: 2026-05-22}` | **DIRECTIONAL_LONG**, DP buy 0.697 |
| `insights_price_vs_flow` | `{symbol: ENPH, lookback_days: 30, date: 2026-05-22}` | no divergence; +104.11% |
| `insights_analyst_vs_flow` | `{symbol: ENPH, date: 2026-05-22}` | flow bullish; analyst block absent (yfinance 401) |
| `insights_institutional_accumulation` | `{symbol: ENPH, date: 2026-05-22}` | **ACCUMULATION**, buy/sell 2.3× |
| `insights_deep_dive` | (reused from phase-0.5) | whole-tape aggregates surfaced above |

## Tool errors

- `insights_analyst_vs_flow` / `insights_deep_dive`: **yfinance analyst & fundamentals
  blocks unavailable (HTTP 401)** — non-fatal; fundamentals sourced in phase-7b (Finnhub),
  analyst target taken from phase-6 (GS $57 via WebSearch).

## Cross-check vs phases 1–5

| UW insight | Phase agreement? | Notes |
|------------|------------------|-------|
| signal_confluence (~4/6) | phases 1-3 **agree** (direction) | but caps score — missing cheap-IV + vol-spike = phase-5's "mature/rich" |
| conviction_matrix DIRECTIONAL_LONG | phases 2-3 **agree** | resolves overwrite/hedge → genuine long |
| institutional_accumulation ACCUMULATION | phase 2 **agrees** (buy 0.70 ≈ 64-95%) | strong confirmation |
| price_vs_flow no-divergence | phases 1,5 **agree** | momentum confirmation, not fresh edge |
| analyst_vs_flow | phase 6 **tempers** | spot $64 > GS PT $57 → price past bull case |

## Verdict for downstream phases

- **UW composite bias:** **BULLISH / DIRECTIONAL_LONG** — the clearest bullish scenario
  category, confirmed by accumulation + aligned price/flow. **Tag: confirmed-but-mature & rich.**
- **Conviction:** **4/5** (internally consistent bullish stack; held below 5 because the
  confluence score is only ~4 — expensive IV, no fresh volume spike — and spot is above
  the GS target).
- **Phase-9 baseline:** treat UW's read as **DIRECTIONAL_LONG baseline**; override only
  with specific contrary evidence (phase-4 negative-vanna/IV headwind, phase-5 extension,
  phase-6 rate headwind & price-past-target, the $2.5M LEAP put, and phases 7b/7c/8b).
- **Open questions:**
  - Fundamentals quality on a name riding an AI/product narrative over a "weak core" —
    does phase-7b veto or pass? (→ 7b)
  - Is the bullish positioning crowded/retail-driven (phase-4 COMPLACENT skew + phase-6
    "retail momentum")? (→ 7c)
