# Phase 8 — Multi-Agent Analyst Desk

**Ticker:** ENPH
**As-of date:** 2026-05-22
**Generated:** 2026-05-25T22:43:20Z
**Upstream phases cited:** phases 1–7c (full chain packed into each agent)

## Summary

Four specialist agents ran in parallel (earnings-scout skipped — earnings 7/28 is
out of the 30-day window). The desk is **genuinely split with no directional plurality
and low conviction**: **1 LONG (qualified), 1 SHORT, 1 NEUTRAL, 1 RANGE**, average
conviction **~2.5/5**, horizon **1-4w unanimous**. The unifying message across all four:
**rich, mature, crowded, range-bound — do NOT pay up for direction.** The lone LONG
(sweep-tracker) is explicitly "long the **$65 break only**, small, hard $60 stop"; the
SHORT (contrarian) is a **defined-risk fade**, not a naked short; the NEUTRAL and RANGE
agents both say half-size/defined-risk. **New datapoint:** risk-monitor re-ran correlation
against *real* solar names and found **ENPH/TAN 0.76, ENPH/SEDG 0.72, ENPH/FSLR 0.60** —
the phase-6 "no cluster" was an artifact of the placeholder SYM sibling; ENPH carries a
genuine **solar-sleeve cluster** (relevant if any other solar position is open).
Consensus map: **resistance $65 (gamma wall; squeeze trigger), support $62→$60.5,
disaster $53.15.**

## Agent verdicts table

| Agent | bias | conviction | horizon | one_line_take |
|-------|------|-----------|---------|---------------|
| accumulation-hunter | **NEUTRAL** | 2 | 1-4w | "Real blocks bought, but I'm not front-running a doubled, short-squeezed, fundamentally-broken name where retail is the marginal buyer — the quiet accumulation already happened at $30, not $64." |
| contrarian-scanner | **SHORT** | 3 | 1-4w | "Retail chasing a spent short-squeeze into a −18% QoQ revenue cliff at IV-rank 92; complacent skew = cheap puts, fade the euphoria with defined risk." |
| sweep-tracker | **LONG** | 3 | 1-4w | "Real persistent ask-side sweeps stacking June 65/70 calls, but it's mixed and retail-heavy on a spent squeeze — long the $65 break only, small, with a hard $60 stop." |
| risk-monitor | **RANGE** | 2 | 1-4w | "Rich, crowded, range-bound on dealer gamma — half size, defined-risk only; bullish flow and bearish fundamentals cancel out, so do not pay up for direction." |
| earnings-scout | — | — | — | **MISSING/SKIPPED** — earnings 2026-07-28 is >30d out (phase-6 calendar) |

**Tally:** LONG 1 · SHORT 1 · NEUTRAL 1 · RANGE 1 → **no plurality; MIXED.** Avg
conviction (4 agents) = **2.5/5**.

## Per-agent details

### accumulation-hunter — NEUTRAL (2)
- key_levels: support 62.34 (then 61.11; shelf 53.15); resistance 65.00 (then 70);
  invalidation: sustained break >$65 on volume → LONG toward $70; loss of $60 floor → SHORT toward $53.15.
- top_signal: Phase-2 block tier 95.3% buy ($27.2M) + Phase-3 June $70C OI +4,616 (ask 5,400 vs bid 275) = real institutional accumulation fingerprint, not overwrite.
- top_risk: Accumulation signal is **contaminated** — Phase-7c lit buying is retail-dominated ($14.5M vs $4.8M) into a 32.5% short float that already squeezed +100%, with Phase-7b bearish → **distribution-into-strength, not pre-move accumulation.**

### contrarian-scanner — SHORT (3)
- key_levels: support 60.00 (break = air pocket to 53.15); resistance 65.00 (close above on volume = fade fails); invalidation: sustained close >$65 OR renewed *block* (not retail) call accumulation.
- top_signal: [7c] 32.53% float short (4.5× peers) ⇒ the double was substantially a **spent short squeeze**; lit call buying retail-dominated ($14.5M vs $4.8M) — "crowd is long for the wrong reason."
- top_risk: Phase-2 ACCUMULATION + Phase-4 DEX +$508M squeeze fuel above $65 → a close >$65 ignites a **second squeeze leg** against the fade.
- Express as a defined-risk **put spread targeting $60→$53.15**; stand aside above $65.

### sweep-tracker — LONG (3)
- key_levels: support 62.34 ($60 GEX floor below); resistance 65.00 (break → $70 magnet); invalidation: close <$60.50, or sweep campaign flips put-dominant / OTM June call OI stops building.
- top_signal: Phase-1 sweep campaign 5/5 sessions, consistency 1.0 ($61.4M); cleanest leg June $65C lifted $1.55M/480 trades; Phase-3 +4,616 ask-driven $70C opening longs (60→70 roll).
- top_risk: dominant_direction MIXED (largest print $2.5M 2027 $60P) + retail-dominated buying on a spent squeeze → crowd chase, not fresh institutional conviction.
- (Called UW tools: confirmed ENPH absent from market-wide top sweep-ratio / smart-money tables — flow is real but mid-cap-sized.)

### risk-monitor — RANGE (2)
- key_levels: support 62.34 (then 61.11; shelf 53.15); resistance 65.00 (squeeze fuel above via DEX +$508M); invalidation: hourly close <$61.11 voids long-gamma pin; sustained break >$65 → squeeze-long re-rate.
- top_signal: Phase-4 long-gamma pin $60–65 ($65 wall, $60 floor) + Phase-2 ACCUMULATION → **dealers and institutions both defending a range, not chasing.**
- top_risk: 32.53% short + complacent skew + IV-rank 92 → a $65 break becomes a **reflexive squeeze in the same direction as crowded retail longs**; verified **solar cluster ENPH/TAN 0.76, ENPH/SEDG 0.72, ENPH/FSLR 0.60** — a single solar-sleeve bet that unwinds violently in either tail.
- (Called UW tools: re-ran correlation vs real solar names — overrides phase-6's placeholder "no cluster".)

## Disagreements

This is a **4-way split**, so every agent dissents from some other:
- **sweep-tracker (LONG)** vs **contrarian-scanner (SHORT)** are direct opposites. Sweep's case: "persistent 5/5 ask-side sweeps + $70C opening longs." Contrarian's case: "32.5% short = spent squeeze + retail-funded + −18% QoQ rev." **Both are right about different time-horizons/levels** — the reconciliation is *level-triggered*: long only above $65, short/fade only on loss of $60.
- **accumulation-hunter (NEUTRAL)** and **risk-monitor (RANGE)** both decline to pick a side → the modal desk view is **stand-aside / range / defined-risk**, not a directional commitment.

## Tool errors

- `earnings-scout`: **MISSING/SKIPPED** by design (earnings >30d out).
- risk-monitor's correlation re-run **supersedes phase-6's correlation verdict**: ENPH is
  NOT uncorrelated — it clusters with solar (TAN 0.76 / SEDG 0.72). Phase-6's "no cluster"
  held only because the sole sibling blueprint (SYM) is a placeholder. **Phase-9 note:** no
  *concurrent ENPH-correlated blueprint* is open today, so no live size-cut — but if a solar
  name is added, treat as one bet.

## Verdict for downstream phases

- **Plurality bias + count:** **NO PLURALITY — MIXED** (LONG 1 / SHORT 1 / NEUTRAL 1 /
  RANGE 1). Modal actionable stance = **range / defined-risk, level-triggered.**
- **Average conviction (4 agents):** **2.5/5** (low).
- **Three highest-quality signals across agents:**
  1. Long-gamma pin $60–65 + DP accumulation → dealers & institutions defending a range,
     squeeze fuel only on a $65 break (risk-monitor / [4]+[2]).
  2. 32.53% short float ⇒ the double was a largely-spent squeeze; lit buying retail-dominated
     ($14.5M vs $4.8M block) (contrarian / accumulation-hunter / [7c]).
  3. Persistent 5/5 ask-side sweep campaign + $70C opening longs = genuine upside
     positioning, but mixed (sweep-tracker / [1]+[3]).
- **Open questions surfaced:**
  - Is the $65 gamma wall the single binary that resolves this (break = squeeze-long, fail
    = fade-short)? → yes, the desk converges on $65 as the trigger. (→ phase 8b, phase 9)
  - Is the DP "accumulation" genuine demand or partly the $9.6M post-market portfolio
    print? → unresolved; accumulation-hunter doubts it's pre-move.
