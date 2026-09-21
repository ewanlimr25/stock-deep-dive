# Phase 8 — Multi-Agent Analyst Desk

**Ticker:** PATH · **As-of:** 2026-07-22 · **Spot:** $10.53 · **Generated:** 2026-07-22
**Upstream:** phases 1–7c (full digest passed to each agent). `earnings-scout` SKIPPED (earnings ~Sep 3–8, >30d out per phase rule).

## Summary

**Unanimous no-edge.** Four independent desk agents converged: **3 NEUTRAL + 1 RANGE,
average conviction 2.0/5, zero directional dissent.** Every agent, from its own lens,
concluded the same thing — the LEAP OI build reads as **stale distribution from the
$12 zone, not accumulation at spot**; the crowded-short base and complacent skew are
**two crowds fighting into a binary 7/24 IV event**; and with **7b vetoing the long
and 7c vetoing the fresh short**, the only defensible expression is a **capped-risk
range trade, half-size, flat or hedged into 7/24.** Consensus band: support **$10.00**
(range floor $9.87), resistance **$11.00** near / **$11.90–12.50** ceiling;
invalidation on a **daily close outside $9.87–$12.55**.

## Agent verdicts table

| Agent | bias | conviction | horizon | one_line_take |
|-------|------|-----------|---------|---------------|
| accumulation-hunter | NEUTRAL | 2 | 1-5d | LEAP OI build looks like stale distribution from the $12 zone, not accumulation at spot; insider selling + $16M block dump = exit liquidity |
| contrarian-scanner | NEUTRAL | 2 | 1-5d | Two crowds fighting (crowded short vs complacent skew) into a binary 7/24 catalyst — no edge to fade; stand aside |
| sweep-tracker | NEUTRAL | 2 | 1-5d | Bullish campaign got run over by the OpenAI shock; today's tape is distribution not a shakeout — stand aside |
| risk-monitor | RANGE | 2 | intraday/1-5d | Fundamentals veto long, crowded-short vetoes short — trade the range, capped-risk, half-size, flat/hedged into 7/24 |
| earnings-scout | SKIPPED | — | — | earnings >30d out (~Sep 3–8) |

## Per-agent details

### accumulation-hunter — NEUTRAL, conv 2, 1-5d
- support $10.00 · resistance $11.90–12.50 · invalidation: close < $9.87 OR close > $12.50 (DP cluster reclaim)
- top_signal: 5-day DP clusters sit entirely at $11.90–12.50 (phase-2) — spot $10.53 is below the week's institutional zone, so last week's OI-building/sweeps happened *higher* and now look like distribution the tape fell out of, not fresh accumulation underneath.
- top_risk: the 14-day OI build is real and CROWDED_SHORT (~24–32% float) means stabilization above the $10.70 VWAP risks a mechanical squeeze that punishes a bearish read.

### contrarian-scanner — NEUTRAL, conv 2, 1-5d
- support 9.87 · resistance 11.90 · invalidation: close < 9.87 (fade-long dies) OR close > 12.50 (fade-short/squeeze dies)
- top_signal: crowded short (13–32% SI, DTC 2.6–4.3) + bearish-flow base rate only 10% (n=10) argue the crash is over-extended and squeeze-prone, **but** $550M of 5-day DP supply at $11.90–12.50 caps any squeeze well below prior highs.
- top_risk: complacent skew (0.919, calls richer) is itself crowded bullish optimism into 7/24 — if the IV crush resolves bearish (net-bearish flow, $276k ATM puts, insider selling/EPS miss), skew unwinds violently down.

### sweep-tracker — NEUTRAL, conv 2, 1-5d
- support 10.00 · resistance 11.00 · invalidation: close < 9.87 (range low) / < 9.50 negates shakeout
- top_signal: the 5-session bullish sweep campaign (consistency 1.0, $6.71M) is now offside post-crash, and today's flow flipped net-bearish (−$1.60M) with the largest print an $893k Dec-18 $12 call SOLD on bid — distribution, not accumulation.
- top_risk: OI shows the Dec-12 sweep matched existing OI (not fresh shorting) → position unwind/hedge-trim, so the momentum read could be premature either direction.

### risk-monitor — RANGE, conv 2, intraday/1-5d
- support $10.00 (floor $9.87) · resistance $11.00 / $12.00 · invalidation: daily close outside $9.87–$12.55 **OR any position held through 7/24 without a pre-defined risk cap**
- top_signal: dealer structure is positive-gamma/range-bound (ZGL $6.92, DEX +1.72M mechanical bid) but explicitly **event-contingent** — post-7/24 IV crush flips dealers to de-hedge/sell (vanna).
- top_risk: two-sided tail — post-7/24 vanna air-pocket lower vs 13–32% SI squeeze fuel higher; a directional bet into the event gets run over from either side.

## Disagreements

**None on direction.** All four decline a directional bias; the only nuance is RANGE
(risk-monitor, actively trade the band) vs NEUTRAL (the other three, lean stand-aside).
That is a structure nuance, not a directional split — it points at the same defined-risk,
non-directional expression.

## Tool errors

- `earnings-scout`: **SKIPPED** (not MISSING) — earnings ~Sep 3–8 is >30d out, per the phase's own skip rule. No agent type was unavailable.

## Verdict for downstream

- **Plurality bias: NEUTRAL/RANGE (4 of 4 non-directional; 3 NEUTRAL + 1 RANGE).**
- **Average conviction: 2.0/5** across the four agents.
- **Three highest-quality signals across all agents:**
  1. 5-day DP supply at $11.90–12.50 is **distribution the tape fell out of**, not accumulation at spot `[AGENT:accumulation-hunter]` (phase-2).
  2. Positive-gamma range is **event-contingent** — post-7/24 IV crush → dealer de-hedge → downside air-pocket `[AGENT:risk-monitor]` (phase-4 vanna).
  3. **Crowded short vs complacent skew** into a binary — no edge to fade until one side breaks `[AGENT:contrarian-scanner]` (phase-7c / phase-4).
- **Open questions surfaced by agents:**
  - Which way does the 7/24 IV crush resolve — squeeze (short covering) or skew-unwind lower?
  - Does $10.00 hold (squeeze support) or break to the $9.87/$9.50 air-pocket?
  - Is the $11.90–12.50 DP supply an impenetrable ceiling for any bounce?
- **Handoff to phase-8b/9:** the desk endorses a **defined-risk, range-bound** stance
  ($10 support ↔ $11.5–12 ceiling), half-size, with **no naked delta held through 7/24
  uncapped**. Phase-8b should stress the bull vs bear disconfirmation around exactly
  these two tails; phase-9 should build the plan as a defined-risk range/premium
  structure, not a directional bet.
