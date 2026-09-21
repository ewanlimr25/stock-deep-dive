# Phase 7 — UW Insights Confluence

**Ticker:** CMPS
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T00:00:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-4-structure.md, phase-6-macro.md

## Summary

UW's composite tools crystallize the central tension of this name in one place: the
**surface options tape reads bearish-tagged, while the underlying structure reads
constructive-accumulation.** `conviction_matrix` classifies CMPS as **COVERED_CALL**
("Dark pool buying + call selling — yield enhancement, capping upside") and
`institutional_accumulation` returns **ACCUMULATION** (buy/sell ratio 5.22) — both
squarely confirming phases 1–3. But `price_vs_flow` flags a **DIVERGENCE** (price
+114% while net flow is −$276k) and CMPS is **absent from the bullish `signal_confluence`
top-100** because its negative aggregate net_flow disqualifies the `bullish_flow`
factor — even though it carries dp_accumulation + low_pcr + oi_building + cheap_iv.
These two "cautions" are the **same aggressor-tape artifact** phases 1 and 3 already
dissected: the negative net_flow is the *closing leg of a bullish roll-up-and-out* plus
the $13-call intraday churn, not genuine distribution. The composite is therefore best
read as **constructive-but-capped with an accumulation core and a flow-confirmation
caveat**; and because UW's model has no knowledge of the de-risked Phase 3 data (phase-6),
it structurally *under-rates* the bullish case. Baseline for phase-9: **mildly bullish /
range-accumulation, not distribution.**

## Key signals

- **conviction_matrix = COVERED_CALL** (conf 52.03%): DP buy_ratio 0.839 + call bid 3,398 > ask 1,591 → "yield enhancement, capping upside" `[INSIGHT:conviction_matrix]`.
- **institutional_accumulation = ACCUMULATION**: buy/sell 5.22, buy 120,058 vs sell 23,000, vwap $11.98 `[INSIGHT:institutional_accumulation]`.
- **price_vs_flow = DIVERGENCE**: "+114.3% price vs bearish flow (net −$275,581)" — reversal flag, but the artifact phases 1/3 explained `[INSIGHT:price_vs_flow]`.
- **signal_confluence: CMPS absent from bullish top-100** — negative net_flow kills the `bullish_flow` factor despite 4 supporting factors present `[INSIGHT:signal_confluence]`.
- **analyst_vs_flow**: yfinance consensus unavailable (HTTP 401); flow-side bearish-tagged. Phase-6 WebSearch fills the gap — Street targets **$14–$18** (bullish) `[INSIGHT:analyst_vs_flow]` `[MACRO:CMPS_2026 WebSearch]`.

## Detailed findings

### Deep-dive snapshot + `uw_screener` directional aggregates `[INSIGHT:insights_deep_dive]`

(From the deep_dive pulled in phases 0.5/1 — same as-of data; not re-called.)

| Field | Value |
|-------|-------|
| Spot / vwap | $11.81 close / $11.98 DP vwap |
| Market cap | $1.56B (Healthcare) |
| IV rank | 12.25 (cheap); iv30d 75.0% |
| **bullish_premium / bearish_premium** | **$330,105 / $605,686** |
| **net_flow** | **−$275,581** (bearish-tagged) |
| call_premium / put_premium | $1,326,507 / $100,519 |
| **implied_move / implied_move_perc** | **$1.65 / 13.95%** (phase-9 N4 sizes to ±14%) |
| put_call_ratio | 0.129 |
| total_open_interest | 89,658 |
| next_earnings | 2026-07-30 (outside 30d → earnings_play skipped) |
| Yahoo fundamentals | error HTTP 401 (use phase-6/7b for fundamentals) |

Reconciles with phase-1's whole-tape aggregate exactly (same screener block). The
directional aggregate is negative, but call premium is 13× put premium — the negativity
is an *aggressor-side* effect (calls sold/rolled), not a put-buying panic.

### Signal confluence `[INSIGHT:signal_confluence]`

CMPS does **not** appear in the bullish list (min_score=1, top_n=100; 100 names returned,
all score ≥4). CMPS's qualifying factors present: `low_pcr` (0.129), `dp_accumulation`
(0.839), `oi_building` (Jul $12 +1,962), `low_iv_cheap_options` (rank 12.25) — but
**`bullish_flow` fails** (net_flow −$276k), so CMPS scores below the top-100 cut. The
model is flow-direction-gated and penalizes exactly the artifact this deep-dive has
already explained. Healthcare names that *did* clear (positive flow): QSI (6), AXSM,
NVO, TEM, DXCM, IMMX, TWST. **Takeaway:** on a naïve same-day flow screen CMPS would be
skipped — the bullish case here requires the OI-structure + fundamental layers UW's
confluence does not see.

### Conviction matrix `[INSIGHT:conviction_matrix]`

`scenario COVERED_CALL · confidence 52.03% · DP buy_ratio 0.839 · call bid 3,398 / ask 1,591`.
"Dark pool buying + call selling — yield enhancement, capping upside." This **agrees with
phases 1+2's surface reconciliation** (buy stock, sell calls). **Nuance vs phase-3:** the
matrix sees static "call selling," but phase-3's OI showed the selling is the *closing leg
of a roll-up-and-out* (Jun $11 → Jul $12 calls bought) — a **more bullish** posture than a
plain covered call. So COVERED_CALL is the floor interpretation; the truth is "covered-call-
*plus-upside-roll*." Either way: **not bearish.**

### Price vs flow `[INSIGHT:price_vs_flow]`

`divergence true · price +114.26% (start $5.75 → end $12.32, 30-session window spanning the
gap) · flow bearish · net −$275,581 · iv_rank 12.25`. Face value: bearish-flow-into-strength
= leading reversal warning. **Discount heavily:** (1) the +114% spans the data gap (the WH-EO
re-rating, phase-6), not a frothy melt-up; (2) the "bearish flow" is the roll/churn artifact;
(3) phase-2 DP is *accumulating*, not distributing; (4) phase-4 dealers are **long gamma**
(mean-reversion, not reversal-acceleration). Net: a **weak momentum-confirmation caution**
(after +114%, fresh ask-side call buying is NOT confirming) — argues for *consolidation*, not
a violent reversal. Carry as a yellow flag into phase-8/8b.

### Analyst vs flow `[INSIGHT:analyst_vs_flow]`

UW returned only the flow side (bearish-tagged, net −$276k); the yfinance analyst block is
**unavailable (HTTP 401)** — same Yahoo failure as deep_dive. Substituting phase-6 WebSearch:
**Stifel $14 (Buy), Morgan Stanley $16 (OW), Canaccord $18 (Buy), Wolfe initiated Outperform**
— consensus clearly **bullish, +19% to +52% above $11.81**. So analyst-vs-flow is a
**divergence**: Street bullish, same-day aggressor flow bearish-tagged. Given the flow
artifact + de-risked fundamentals, side with the analysts here.

### Institutional accumulation `[INSIGHT:institutional_accumulation]`

`signal ACCUMULATION · buy/sell 5.22 · buy 120,058 / sell 23,000 · 11 trades · vwap $11.98 ·
price_30d +114.26%`. Top levels: $12.07 ($413k), $11.76 ($208k), $12.20 ($159k), $11.94, $11.99.
**Strong, unambiguous accumulation read** — fully confirms phase-2. The buying is at $11.8–$12.2,
extending the base above the $10.56–$11.45 shelves.

### Earnings play

**Skipped** — next earnings 2026-07-30 is >30d from the 2026-05-22 as-of (phase-6 calendar).
Not an in-window earnings setup.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `insights_conviction_matrix` | symbol=CMPS | COVERED_CALL, conf 52.03%, buy_ratio 0.839 |
| `insights_price_vs_flow` | symbol=CMPS, lookback=30 | DIVERGENCE: +114% price vs bearish flow |
| `insights_analyst_vs_flow` | symbol=CMPS | flow bearish; analyst side unavailable (401) |
| `insights_institutional_accumulation` | symbol=CMPS | ACCUMULATION, buy/sell 5.22, vwap $11.98 |
| `insights_signal_confluence` | bullish, min_score=1, top_n=100 | CMPS absent (neg net_flow disqualifies bullish_flow) |
| `insights_deep_dive` | (reused from phase-0.5/1) | net_flow −$276k, implied move ±14%, IV rank 12.25 |

## Tool errors

- `insights_analyst_vs_flow` / `insights_deep_dive` Yahoo fundamentals: **HTTP 401** (yfinance
  blocked). Analyst consensus + fundamentals sourced from phase-6 WebSearch and phase-7b (Finnhub)
  instead. Not fatal.

## Cross-check vs phases 1–6

| UW insight | Phase agreement? | Notes |
|------------|------------------|-------|
| conviction_matrix = COVERED_CALL | **Agrees** w/ phases 1+2; phase-3 upgrades to "covered-call + bullish roll" | Floor read; truth is more constructive |
| institutional_accumulation = ACCUMULATION | **Agrees** w/ phase-2 (buy_ratio 0.839) | Strong, consistent |
| price_vs_flow = DIVERGENCE (bearish) | **Apparent conflict**, resolved by phases 1/3/4 | Roll/churn artifact + long-gamma → consolidation, not reversal |
| signal_confluence (CMPS absent) | **Apparent conflict**, same artifact | Flow-gated model can't see OI-roll or fundamentals |
| analyst_vs_flow | **Agrees** w/ phase-6 (Street $14–18 bullish) | Flow-bearish tag is the artifact |

## Verdict for downstream phases

- **UW composite bias:** **CONSTRUCTIVE-BUT-CAPPED / accumulation core** — COVERED_CALL +
  ACCUMULATION dominate; the DIVERGENCE and confluence-absence are the explained
  aggressor-tape artifact, not new bearish evidence. Net: **mildly bullish / range-accumulation.**
- **Conviction: 3/5.** The two "agree" signals (accumulation, COVERED_CALL) are clean and
  match phases 1–3; the two "caution" signals (divergence, confluence-miss) are real but
  artifact-driven and already explained — they cap conviction rather than reverse it. UW's
  model under-rates CMPS because it cannot see the phase-6 clinical de-risking.
- **Phase 9 should treat this as the BASELINE:** range-accumulation, constructive into the
  Q3 catalyst, with upside capped near-term by the $12 gamma wall / overwrite strikes and
  the weak same-day momentum confirmation. Override only with specific contrary evidence
  from phases 7b/7c/8/8b.
- **Open questions for 7b/7c/8b:**
  - Does phase-7b confirm the **runway-to-2028 / share count** (UW/Yahoo fundamentals failed)
    so the bull case rests on funded execution, not a financing overhang?
  - Is sentiment/positioning already **crowded long** into the Q3 data (phase-7c short
    interest, retail-vs-inst) given +114% off the low and the COMPLACENT skew (phase-4)?
  - Does the **price_vs_flow divergence** deserve weight as a near-term consolidation/pullback
    signal the bull case should buy *into* (vs chase) — i.e. wait for the $11 gamma-wall retest?
