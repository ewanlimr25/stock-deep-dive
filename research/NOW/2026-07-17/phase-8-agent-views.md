# Phase 8 — Multi-Agent Analyst Desk

**Ticker:** NOW
**As-of date:** 2026-07-17
**Generated:** 2026-07-19 (run) for as-of 2026-07-17
**Upstream phases cited:** phase-1 through phase-7c (all packed into each agent)

## Summary

Five specialists fanned out on the same phase-1→7c context. **Plurality =
NEUTRAL/RANGE with a distinct downside tilt** — 3 NEUTRAL (accumulation-hunter,
sweep-tracker, risk-monitor), 1 SHORT conv-4 (contrarian-scanner), 1 directionally-
neutral short-vol-with-tail-hedge (earnings-scout). **Average conviction ≈ 2.6.**
There is **strong unanimity on the *structure*, not just direction**: every agent
independently converged on **no naked directional long, size down / defined-risk,
sell the rich vol but buy the cheap downside tail, and resolve the NOW/PATH cluster
before the print.** No agent was bullish. The lone high-conviction call
(contrarian, SHORT 4) is a *fade-the-crowd* thesis (89% analyst buy on a −51% name
into a decelerating-earnings binary), which the others treat as the primary risk
rather than a base case. Consensus levels: support **$101.21 (ZGL) / $100 / $95**,
resistance **$104–105 (neg-gamma pocket) → $110–120 walls**, invalidation on a close
**>$105** (range breaks up) or **<$100/$101.21** (pin breaks down).

## Agent verdicts table

| Agent | bias | conv | horizon | one_line_take |
|---|---|---|---|---|
| accumulation-hunter | **NEUTRAL** | 2 | 1-5d | "Accumulation is closing-print noise + Jan-27 put-selling for yield, not smart money loading up — not buying this dip." |
| contrarian-scanner | **SHORT** | 4 | 1-5d | "89% Buy on a stock −51% with decelerating growth is a downgrade cascade waiting on a beat that isn't showing up — fade the consensus." |
| sweep-tracker | **NEUTRAL** | 2 | 1-5d | "Sweeps loud but directionless — delta-neutral tape, no smart-money confirm, a coin-flip parked at the gamma flip into earnings." |
| earnings-scout | **NEUTRAL** (short-vol + tail hedge) | 3 | 1-5d | "Sell the ±10–12% move via defined-risk condor/strangle-with-wings — the IV-96.9/VRP+18.9 crush is real edge, cheap complacent puts are the hedge." |
| risk-monitor | **NEUTRAL** | 2 | 1-5d | "Same bet twice under one roof (NOW/PATH), half-sized regime, naked skew into earnings — trim the cluster or hedge with defined-risk before the print." |

## Per-agent details

### accumulation-hunter — NEUTRAL, conv 2, 1-5d
- key_levels: support $102.90 · resistance $104.85 → $111–112.5 · invalidation close <$100 (loses positive-GEX pin + insider-buy floor) or >$105 (neg-gamma accelerates).
- top_signal: Phase-2 mega-tier buy_ratio 1.0 is closing-cross facilitation ($82.96M at the exact $103.24 close), not conviction accumulation — large tier balanced (0.488), NOW absent DP top-30.
- top_risk: Earnings in 5 days, decelerating surprises + 89%-Buy crowd on a −51% drawdown = real downgrade-cascade gap risk no put-writing premium offsets.

### contrarian-scanner — SHORT, conv 4, 1-5d
- key_levels: support 100 · resistance 105 · invalidation close >$105 with call-side OI building, or IV crush post-earnings without a downside break.
- top_signal: Phase-7c CROWDED_LONG (89% Buy, 48/54, unchanged) on a −51% name with decelerating earnings (7b: +13.4→−0.3%), while Phase-5 bullish_flow backtest resolves negative (14.3%, n7) vs bearish_flow 100% (n10) — the crowd's bullish positioning is the fade.
- top_risk: Complacent skew + short-gamma/backwardation into earnings means a violent beat-driven gap-up squeezes the short before any downgrade cascade — covered-call sellers get run over.

### sweep-tracker — NEUTRAL, conv 2, 1-5d
- key_levels: support $101.21 (ZGL) · resistance $104–105 · invalidation close <$101 (loses long-gamma anchor) or <$95.
- top_signal: Phase-1 sweep-persistence 5/5 sessions $106M but dominant_direction="mixed"; ask-side calls ($6.2M fragmented) offset by larger bid-side put-selling ($8.97M), netting delta-neutral (−$89k) — vol/skew positioning, not a directional campaign.
- top_risk: A push through $104–105 neg-gamma pocket pre-earnings accelerates the move to $110 fast either way; conviction-chasing gets run over by the 7/22 gap.

### earnings-scout — short-vol + tail-hedge (directionally NEUTRAL), conv 3, 1-5d
- key_levels: support $95 / long-gamma floor $101.21 (decays into print) · resistance $105/$104 (max-pain/battleground) · invalidation close beyond ±12% of $103.24 (<$91 or >$116) post-print — outside the implied move breaks the crush thesis.
- top_signal: Phase-4 backwardation (7/24=114.2% vs 8/21=74%) + VRP +18.9 (5) = textbook post-earnings crush setup, but complacent skew (put25Δ 71.9%≈call25Δ 72.7%) means the crowd isn't paying for the downside tail that 7b's decelerating surprise trend makes plausible.
- top_risk: The 89%-Buy base on a −51% name sets up a downgrade cascade if a fourth straight miss posts — short-vol gets run over by a real gap, not just a crush.

### risk-monitor — NEUTRAL, conv 2, 1-5d
- key_levels: support $101.21 → $95 · resistance $105 / $110–120 · invalidation close <$101.21 with GEX flipping negative, or portfolio: NOW+PATH combined loss >1R.
- top_signal: Phase-6 NOW/PATH 0.798 (30d) is a genuine cluster, not diversification — PATH already −38%, NOW −51%, both the same decelerating-enterprise-automation bet.
- top_risk: Complacent skew into a binary + GEX going fully negative on prior drawdowns (June $92 lows) means a repeat miss gets amplified by dealer short-gamma selling, not cushioned.
- **Explicit action items:** (1) Treat NOW+PATH as ONE position for sizing (cut a leg or cap combined delta to a single-position limit). (2) NOW/SHOP 0.58 soft-watch — don't stack a third correlated leg. (3) Regime "half size, defined-risk, iron condors" is the correct frame; NOW diverging from tech's +$1.17B inflow argues against adding on strength.

## Disagreements

- **contrarian-scanner (SHORT 4)** is the lone directional dissent from the NEUTRAL
  plurality. Its top_signal (fade the 89%-Buy consensus into decelerating earnings +
  bullish_flow-14% backtest) is not contradicted by the others — they **agree it is
  the dominant risk**, but decline to size it as a base case because of the beat-gap
  squeeze risk and the complacent-but-cheap downside optionality (i.e. better
  expressed as *long the cheap tail* than *naked short stock*). Read as
  **confirmation of a downside skew, expressed with defined risk**, not a true split.

## Tool errors

None. All five agent types available; none needed extra `uw` calls (0 tool uses each).

## Verdict for downstream

- **Plurality bias:** **NEUTRAL/RANGE with downside tilt** — 3 NEUTRAL + 1 short-vol-
  neutral + 1 SHORT(4). **Zero bullish.** Count: Neutral 4, Short 1.
- **Average conviction:** **≈ 2.6 / 5** (non-MISSING agents).
- **Three highest-quality signals across agents:**
  1. **NOW/PATH 0.798 cluster** — same-bet concentration; resolve before the print
     `[AGENT:risk-monitor]` `[MACRO:portfolio_correlation]`.
  2. **Crowded 89%-Buy on a −51% name + decelerating earnings + bullish_flow backtest
     14.3%** — asymmetric downgrade-cascade risk `[AGENT:contrarian-scanner]`
     `[SENT:recommendation]` `[HIST:signal_backtest]`.
  3. **Backwardation 114%/VRP +18.9 + COMPLACENT skew** — short-vol edge, but the
     cheap downside tail is the required hedge `[AGENT:earnings-scout]`
     `[STRUCT:iv_term_structure]` `[STRUCT:term_skew]`.
- **Open questions surfaced by agents:** Should the trade be a **defined-risk short-vol
  structure with downside wings** (iron condor / strangle-with-wings), not a
  directional bet (earnings-scout)? Must phase-9 explicitly **size NOW+PATH as one
  position** (risk-monitor)? Does the $104–105 negative-gamma pocket make pre-earnings
  direction a coin flip that only earnings resolves (sweep-tracker)?
