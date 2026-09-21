# Phase 8 — Multi-Agent Analyst Desk

**Ticker:** PDD
**As-of date:** 2026-05-26
**Generated:** 2026-05-26T21:14:00Z
**Upstream phases cited:** phase-1 → phase-7c (all packed into each agent)

## Summary

Five agents ran in parallel; **the desk is NEUTRAL/RANGE with a clear downside skew and
unanimous "defined-risk only."** Bias tally: **1 RANGE, 1 SHORT, 3 NEUTRAL** (of the
neutrals, 2 lean short / sell-vol, 1 leans mildly long). No agent is outright LONG; the
only long lean (sweep-tracker) explicitly caps itself. Average conviction **2.2/5** —
low, as every prior gate implied. **Every agent independently converged on the same
structural map:** sell the rich event vol with *defined* risk, treat **95 as the
short-gamma downside accelerant** and **104–110 as the cap**, and respect the binary
gap risk + the phase-7b fundamental VETO. The cleanest actionable expression came from
earnings-scout: a **put-skewed defined-risk iron condor** harvesting the 98% front-week
crush, wings outside the ±5.7% implied move.

## Agent verdicts table

| Agent | bias | conv | horizon | one_line_take |
|-------|------|------|---------|---------------|
| accumulation-hunter | RANGE | 2 | 1-5d | "Real blocks got bought, but they bought a collar, not a conviction long — into a fundamental VETO and binary print. Don't chase; respect 95." |
| contrarian-scanner | SHORT | 3 | 1-5d | "Crowd's chasing a cheap call lottery on a name missing earnings two quarters running; dealers aren't even hedging downside — fade the euphoria, half size, defined risk." |
| sweep-tracker | NEUTRAL (lean LONG) | 2 | 1-5d | "Sweeps lean long into the print but it's an earnings lottery, not conviction; short-gamma below 95 turns a miss into a cascade — size for a coin-flip, not a layup." |
| earnings-scout | NEUTRAL (sell-vol, put-skew) | 2 | 1-5d | "SELL VOL but defined-risk only — iron condor on the 98% 5/29 weekly, wings outside ±5.7%, put-skewed, to bank the crush while the VETO and 95-cascade cap upside and tail." |
| risk-monitor | NEUTRAL (lean SHORT on break) | 2 | 1-5d | "TRANSITIONAL + crowded-long + short-gamma-down into a binary = defined-risk only at quarter-size; if you hold any China-internet name you are NOT diversified (KWEB/PDD 0.81)." |

**Distribution:** bias — NEUTRAL/RANGE plurality (4/5), with the directional lean tilting
**short/down-skew** (3 of 5 see asymmetric downside; 1 mild long; 1 pure range). Conviction —
all 2 except contrarian-scanner at 3. Horizon — unanimous **1-5d** (the print is the event).

## Per-agent details

### accumulation-hunter — RANGE, conv 2, 1-5d
- support 94.52 → 92.57 (52w low); resistance 97.79 → 104-110; invalidation: sustained break
  <95 = short-gamma cascade (downside); reclaim/hold >104 = upside-trend flip.
- top_signal: Phase 2 block tier 100% BUY, 10 trades/$17.09M, sell_volume 0, $4.8M lift @ 97.35
  above mid late-day — one-sided institutional accumulation into the print.
- top_risk: Phase 3 OI shows the accumulated stock is likely **collared** (calls written, puts
  bought) and Phase 4 GEX is FULLY_NEGATIVE with −$8.63M at strike 95 — a break cascades, and the
  "accumulation" may be a hedged book, not a directional bet.

### contrarian-scanner — SHORT, conv 3, 1-5d
- support 92.57 (52w low; break = accelerant); resistance 104; invalidation: close >~102 post-ER
  OR a clean revenue re-accel / in-line+ print validating the 77% Street bull case → flip flat.
- top_signal: Phase 7b VETO (rev 49%→9.65% TTM, two double-digit misses −15.6%/−39%) collides with
  Phase 7c CROWDED_LONG (Street 77% buy and RISING, retail call lottery) — the crowd is buying
  decelerating earnings into a binary print.
- top_risk: Phase 2 DP blocks 100% BUY ($17.09M, $4.8M @ 97.35 above mid) is genuine accumulation,
  not a collar — if so, a beat triggers the Phase 4 vanna squeeze above 104.

### sweep-tracker — NEUTRAL (lean LONG on flow), conv 2, 1-5d
- support 94.52 (below → strike-95 −$8.63M accelerant); resistance 104-110 (gamma cap + OTM call
  sweep cluster 97-130); invalidation: close <95.00 flips fully SHORT; calls-written/puts-bought OI
  repeat post-print also kills the long.
- top_signal: Phase-1 + a fresh 3-day `hot_chains_sweep_persistence` shows PDD bullish, consistency
  1.0, $24.8M sweep premium, ask-side OTM call buying 97-130 — aggressive money positioning long
  into the print. (Note: the 5-session view was MIXED; the 3-session recent view leans bull.)
- top_risk: Phase-7b veto + China peers FUTU/TIGR −13/−14% post-ER → the short-gamma engine cuts
  violently DOWN on any miss.

### earnings-scout — NEUTRAL (sell-vol, put-skew), conv 2, 1-5d
- support 94.52 (below → 95 cascade); resistance 104-110 (call-write cap / vanna ceiling);
  invalidation: close >105 (squeeze fires, threatens short-vol) OR clean hold <94 (cascade DOWN,
  weak-Q1 + China-peer resolution confirmed).
- top_signal: IV rank 76.5, front 5/29 weekly IV **98.3% vs back ~42%** (severe backwardation) +
  VRP +0.072 PREMIUM_SELLING — vol is rich and the post-print crush is the edge.
- top_risk: Short-gamma −$12.8M with the 95 accelerant + weak-Q1 seasonality (both prior misses in
  Q1/Q4, −39% comparable quarter) makes a **naked** premium sale a tail-loss trap — must be defined.

### risk-monitor — NEUTRAL (lean SHORT on break), conv 2, 1-5d
- support 95.00 (heaviest neg-gamma −$8.63M); resistance 102.00 (down-drift origin / upper implied
  edge ~$102.08); invalidation: sustained reclaim/hold >102 on a beat OR hold of 95 with bullish
  post-print flow → NEUTRAL-constructive.
- top_signal: Phase 4 SHORT GAMMA / FULLY_NEGATIVE −$12.8M, heaviest neg-gamma at 95 (just below
  spot) + DEX −$347M → a sub-95 print triggers mechanical dealer selling into weakness; asymmetric
  downside on a binary event.
- top_risk: Binary print (±5.69%/±$5.50) into a non-pinned short-gamma book → gap risk dominates;
  7b deterioration + China peers FUTU/TIGR −13/−14% skew the gap **down**. Re-pull confirmed
  China-cluster KWEB/PDD 0.812 (and BABA/KWEB 0.898) — **treat the China-internet complex as ONE
  position**; do not add naked premium pre-print.

## Disagreements

- **sweep-tracker (lone long lean)** vs the desk's short/neutral skew. Its piece is the **fresh
  3-day sweep persistence flipping bullish** (consistency 1.0, $24.8M) — aggressive short-term money
  IS leaning long into the print. But it self-caps ("lottery, not conviction; <95 cascades"). This
  is the bull's strongest near-term tell and feeds phase-8b.
- **contrarian-scanner (SHORT 3)** vs the neutrals — the only conviction-3 call; it weights the
  7b VETO + 7c crowded-long over the DP accumulation, reading the lit flow as exit liquidity.
- The unresolved crux all five circle: **is the phase-2 block accumulation a directional bet or a
  collar hedge?** accumulation-hunter and contrarian both name it as the swing question → phase-8b.

## Tool errors

None. All five agent types available; no MISSING lines. (sweep-tracker, contrarian, risk-monitor
each made 3–4 confirmatory UW calls within budget; accumulation-hunter and earnings-scout reasoned
from the digest.)

## Verdict for downstream

- **Plurality bias:** **NEUTRAL/RANGE (4 of 5), directional lean SHORT/down-skew (3 of 5 see
  asymmetric downside; 1 mild long).** No clean directional consensus → phase-9 targets the
  MIXED/0.55–0.65 band and a **defined-risk structure** per the 3-2 heuristic.
- **Average conviction:** **2.2/5** across all five (none MISSING).
- **Three highest-quality signals across agents:**
  1. Phase 2 block tier **100% BUY $17.09M** (sell_vol 0, $4.8M lift @97.35 above mid)
     [DP:block_stratified] — the genuine bull tell, *qualified* by phase-3 as likely collared.
  2. Front 5/29 IV **98.3% vs back ~42%** backwardation + VRP **+0.072** [STRUCT:iv_term_structure /
     HIST:vrp] — vol is rich; the post-print crush is the highest-confidence edge (sell vol, defined).
  3. Short gamma **−$12.8M, −$8.63M at strike 95** [STRUCT:gex] + 7b deterioration + China peers
     **FUTU −13% / TIGR −14%** [HIST:signal_backtest] → downside gap is the dangerous tail; 95 is the line.
- **Open questions for phase-8b:** (1) Is the DP accumulation a directional long or a collar hedge?
  (2) Does the fresh 3-day bullish sweep persistence (sweep-tracker) override the 5-day MIXED read?
  (3) Can the bull case survive the 7b VETO + 7c crowded-long + China-consumption headwind, or is
  the bullish flow exit liquidity? The bull (DP accumulation + vanna-squeeze-if-it-holds) and bear
  (deteriorating fundamentals + short-gamma-down + China headwind) must be put head-to-head.
