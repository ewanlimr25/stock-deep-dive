# Phase 8 — Multi-Agent Analyst Desk

**Ticker:** SNOW
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T17:15:00Z
**Upstream phases cited:** phase-1 through phase-7c (full chain packed to each agent)

## Summary

**Five-of-five agreement on RANGE/NEUTRAL — there is no directional edge, and this
is a defined-risk event trade.** Three agents returned RANGE, two NEUTRAL (which here
is functionally the same "no clean direction" read). **Average conviction 2.4/5** —
deliberately low, reflecting a setup that is size-unusual but direction-neutral into a
±13.3% binary. No agent took an outright LONG or SHORT. The convergent thesis: a
**crowded long, priced for perfection, rallied +32% into the print, with net-bearish
smart-money flow underneath** — pinned at $172.5 by long gamma until the 5/27 catalyst,
after which the **vanna-driven IV crush makes the gap-DOWN the dominant drawdown
vector.** Every agent landed on defined-risk, half-size, event-anchored expression.

## Agent verdicts table

| Agent | bias | conviction | horizon | one_line_take |
|-------|------|-----------|---------|---------------|
| accumulation-hunter | NEUTRAL | 2 | 1-5d | "No stealth bid — DP balanced, OI build is a defined-risk 185/200 spread, fingerprints are retail longs + insiders selling. Stand aside." |
| contrarian-scanner | RANGE (fade post-pop into $185) | 3 | 1-5d | "Retail-funded, analyst-cheered melt-up with bearish smart-money flow underneath — fade the post-print pop into $185, not the pin." |
| sweep-tracker | RANGE | 2 | 1-5d | "Tape is loud but two-faced — 5 straight sweep sessions, zero net direction. No edge to chase; wait for the print to pick a side." |
| earnings-scout | RANGE | 3 | 1-5d | "Vol's a touch rich but the move usually lands — don't sell naked into a 71% realizer. Fade the wings with defined risk; crush does the work." |
| risk-monitor | NEUTRAL (asymmetric downside) | 2 | 1-5d | "Half-size, defined-risk into a 3-day binary; vanna-fueled downside is the dominant drawdown vector, and SNOW/PATH 0.627 means don't double the bet." |

## Per-agent details

### accumulation-hunter — NEUTRAL, 2/5
- **levels:** support 163.5 / resistance 185 (→200 cap) / invalidation: block-tier DP buy_ratio flips >0.65 on rising volume into 5/26 OR fresh downside put build; sustained closes <163 kill the thesis.
- **top_signal:** Phase-2 genuine tell is mild not stealth — large-tier $71.5M @ 0.604 + the $163.5–167 ~$85M shelf are constructive but SNOW is not a top-30 DP name and the mega print is a mechanical closing SELL → balanced, not quiet accumulation.
- **top_risk:** The visible buildup is the crowd not smart money (7c CROWDED_LONG, 7b 38M insider sells/0 buys, 7 divergence) → disappointing print snaps back with no institutional bid underneath.
- Convergence scorecard: <1 of the 4 accumulation triggers fire → fails the 3+ bar.

### contrarian-scanner — RANGE (fade tilt), 3/5
- **levels:** support 167 / resistance 185 ($200 hard cap) / invalidation: sustained close >$185 on a clean beat-and-raise OR a decisive net-bullish smart-money flip pre-print.
- **top_signal:** Phase-7 price_vs_flow DIVERGENCE (+31.7% price vs bearish flow) corroborated by Phase-1 net earnings-week flow −$15M and the $1.07M ask 2027 155P, while retail carries the long tape.
- **top_risk:** Long-gamma $172.5 pin holds price up into the print, and a 4/4-beat name gaps through the $185 wall on a guide-raise, squeezing the fade before IV crush helps.
- Key nuance: **fade the post-print pop, not the pre-event pin** (the pin holds until the catalyst).

### sweep-tracker — RANGE, 2/5
- **levels:** support 170.8 (deeper 163.5–167) / resistance 174.29 (thin)→185 / invalidation: a fresh single-direction sweep cluster (consistency 1.0 + dominant_direction flips to one-sided) OR spot holding outside 170.8–174.29 on elevated volume.
- **top_signal:** Phase-1 sweep_persistence 5/5 sessions at consistency 1.0 but dominant_direction MIXED ($89.7M), and the two largest sweeps offset (bid 5/29 160C $1.6M call-selling vs ask 5/29 175C $1.2M) — high activity, no net direction.
- **top_risk:** Long-gamma pin coils spot into the print, so any pre-earnings directional sweep play decays into the catalyst.
- Honest call: **no clean momentum edge.**

### earnings-scout — RANGE, 3/5
- **levels:** support 163.5 (then $150 ≈ −13% floor) / resistance 185 ($200 short-strike cap) / invalidation: post-print close outside the $149–$195 cone, OR clean break/hold >$185 on volume → LONG-directional.
- **top_signal:** Phase-5 VRP +0.303 (IV 83% vs RV 53%) flags rich premium, but the same phase's high-IV-rank backtest shows 71.4% vol-realisation → the ±13.3% move is only *modestly* rich, not a free premium-sale.
- **top_risk:** A 5th straight beat against a +32% priced-for-perfection run could gap SNOW through $185 toward the $200 cap, running over short-vol/range structures.
- **Structure guidance:** short the *wings* not the body — iron condor ~150/160–190/200 around the $172.5 pin to harvest crush while capping gap risk; or, for an upside lean, the existing 175/185 call spread financed by a 150 put sale. Avoid long straddles (crush) and naked short straddles (71% realizer + gap risk).

### risk-monitor — NEUTRAL (asymmetric downside), 2/5
- Fresh reads (date 2026-05-22): **SNOW/PATH 0.627 MODERATE** (single pair, no ≥0.70 cluster); **Tech sector flow accelerating $4.98B→$6.19B, persistence 1.0** → no adverse rotation away from SNOW's sector.
- **levels:** support 170.8 (deeper 163.5–167) / resistance 174.29→185→200 / invalidation: gap-and-hold >185 → LONG continuation; sustained loss of 163.5 → downside vanna unwind confirmed.
- **top_signal:** Phase-4 vanna −2,294 + backwardation → post-earnings IV crush mechanically forces dealer SELLING into any down-move; Phase-5 VRP/71.4% realisation says the ~13% move is likely paid out.
- **top_risk:** A CROWDED_LONG, priced-for-perfection name printing into net-bearish 2–7DTE flow is the classic asymmetric-downside binary — the gap-down is the move that hurts.
- **Sizing guidance:** half-size, strictly defined-risk; treat SNOW+PATH as ~1.3× a single high-beta-software unit if both are live; define max loss at entry (gaps jump stops); NTAP (5/28) is a next-day correlation watch.

## Disagreements

**None on bias** — all five are RANGE/NEUTRAL. The only gradient is in *expression*:
contrarian-scanner has the most explicit fade-the-pop (mild short) lean into $185;
earnings-scout is neutral-condor (harvest crush both wings); risk-monitor weights the
*downside* tail heaviest. No agent is bullish-directional; no agent argues to chase.

## Tool errors

(none. All five agent types available; risk-monitor made 3 UW calls for fresh
correlation + sector-persistence reads, others reasoned from the packed context.)

## Verdict for downstream phases

- **Plurality bias:** **RANGE / NEUTRAL — 5 of 5** (no directional edge). Pre-print:
  pinned ~$172.5. Through-print: ±13.3% binary with asymmetric DOWNSIDE risk.
- **Average conviction:** **2.4/5** across all five agents.
- **Three highest-quality signals across agents:**
  1. **price_vs_flow DIVERGENCE** (+31.7% price vs bearish flow) [INSIGHT:price_vs_flow],
     corroborated by net earnings-week delta −$15M [FLOW:delta_notional DUCKDB] — the
     crowd is long, the smart-money flow isn't.
  2. **VRP +0.303 rich but 71.4% vol-realisation** [HIST:vrp][HIST:signal_backtest] —
     vol modestly rich, the move usually lands → defined-risk, not naked premium either way.
  3. **Vanna −2,294 + backwardation → mechanical post-earnings dealer SELLING**
     [STRUCT:vanna_charm] — makes the gap-down the dominant drawdown vector.
- **Open questions surfaced by agents:**
  - Does the 5/27 print beat-and-raise (gap >$185, flip LONG) or disappoint
    (gap-down, vanna unwind to $150)? — unknowable; structure for both tails.
  - Should the desk express this as a crush-harvesting condor, a defined-risk bull
    call spread (echoing the smart-money 185/200), or a downside-tail put spread?
    → phase-9 strategy selection, weighed against the downside-asymmetry flag.
  - SNOW/PATH 0.627 — does the desk hold both? If so, size as one ~1.3× unit.
