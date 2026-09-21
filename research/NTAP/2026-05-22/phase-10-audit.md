# Phase 10 — Audit & Confidence Score

**Ticker:** NTAP
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T00:00:00Z
**Dominant bias audited:** NEUTRAL (vol-sell / fade-skew, no directional long) — phase-9

## Summary

**Confluence score: 66/100** → recommended conviction bin **0.75**; phase-9 chose
**0.65** — a **MISMATCH (one bin conservative)**, which is a *permitted downward
deviation* given the binary 5/28 gap risk and the 60% vol-realisation eroding the
vol-sell edge. The run is **internally consistent**: every phase supports the
"no-long / rich-premium / fade-skew" thesis, with the lone contradiction being
**macro (phase-6)** — the persistent Tech-sector inflow is a continuation tailwind
that genuinely fights the fade. **1 contradiction** logged; **0 citation failures**;
all sanity checks pass. The key tension the auditor flags: signal *agreement* is high
(score 66) while position *conviction* is rightly moderate (0.65) — a legitimate
divergence for fading a binary.

## Confluence scorecard

| Phase | Score | Justification (quote a datapoint) |
|-------|-------|-----------------------------------|
| 1 — flow | **+** | Net call SELLING −$0.356M + put SELLING −$0.308M; 145C 6/18 sold-on-bid $2.86M [FLOW:aggressor_ex0dte DUCKDB] — supports no-long/sell-premium |
| 2 — dark pool | **0** | Block buy 0.653 but large-tier 0.523, UW NEUTRAL [DP:block_stratified] — mild buy lean is a soft headwind to the fade, net balanced |
| 3 — OI | **+** | `oi_biggest_increases` EMPTY, 145C OI fell on 6,231 vol [OI:decrease_with_volume] — static, no directional positioning |
| 4 — structure | **++** | Long-gamma pin (ZGL $115.41 vs spot $139.37) + negative vanna −817 [STRUCT:gex],[STRUCT:vanna_charm] — strongest support for pin/vol-sell/post-crush fade |
| 5 — historical | **+** | VRP +0.1332 PREMIUM_SELLING, IV pctile 100, price/flow divergence [HIST:vrp] — supports sell-premium (momentum/60%-realisation a partial counter) |
| 6 — macro | **−** | Tech net flow +$6.19B, persistence 1.0 ALIGNED to a long [MACRO:sector_flow_persistence] — a continuation tailwind that contradicts the fade |
| 7 — insights | **++** | conviction_matrix MIXED, price_vs_flow DIVERGENCE=true, NTAP absent from bullish confluence [INSIGHT:price_vs_flow] — unanimous no-long |
| 7b — fundamentals | **0** | `tier_adjustment = NA` (no Finnhub key) — quality veto unavailable, scores neutral |
| 8 — agents | **+ (5/5 align, +10)** | 0 LONG: 2 NEUTRAL + 2 SHORT + 1 RANGE — all align with no-long/neutral-fade |

**Context modifier (phase-0.5):** `unusual_verdict = GENUINELY_UNUSUAL` → **no cap**
applied to phases 1–2 (cap only fires on BUSY_NAME_NORMAL_DAY / QUIET).

**Raw score (symmetric):** +7 +0 +7 +15 +7 −7 +15 +0 +10 = **+54**
**Base score:** round((54 + 130) / 260 × 100) = **71/100**
**Debate penalty (phase-8b):** **0** (disconfirmed = false; bull_residual 0.65 > bear_residual 0.55)
**Sentiment penalty (phase-7c):** **−5** (tier_adjustment = CAUTION)
**Confluence_score:** **66/100**
**Recommended bin:** **0.75** (band 65–79)
**Phase-9 actual bin:** **0.65** → **MISMATCH — phase-9 is one bin conservative (permitted downward deviation)**

## Conviction deviation (phase-9 0.65 vs recommended 0.75)

Permitted and justified — downward deviation is always allowed:
1. **Binary gap risk** — every phase-8 agent capped conviction at 3/5; a 5/28 beat
   can gap NTAP through 145 before the fade works ([DEBATE:bear_residual]).
2. **60% vol-realisation (N=10)** makes the vol-sell's *effective* edge marginal
   (range-sell win-rate ~0.40) — high signal-agreement ≠ high trade edge.
3. **Score sits at the 65/66 band boundary** — 66→0.75 vs 64→0.65 is within noise;
   0.65 is the prudent side for a fade into a binary.

## Contradictions

- **phase-6 (macro): −** Persistent Tech-sector options inflow (+$6.19B, persistence
  1.0) plus the genuine Google-Cloud-AI catalyst is a **continuation tailwind that
  fights the fade** [MACRO:sector_flow_persistence], [MACRO:NTAP_news_2026-05-22].
  **Resolution:** already encoded — (a) **tighten invalidation** (two closes >145 =
  thesis broken), (b) **defer the directional fade to post-earnings** (don't carry a
  naked short through the print), (c) size at **starter (~1%) defined-risk** so the
  tailwind can't inflict more than the capped loss. *Soft watch (phase-2, scored 0):*
  the block-tier 0.653 buy lean is a mild bid under price — re-check if it strengthens.

## Citation failures

None — all 3 spot-checked thesis citations resolve:
1. **[FLOW:sweeps]** "145C 6/18 sold-on-bid $2.86M / 4,851 ctr" → ✓ resolves to
   phase-1-flow.md §Sweeps (`total_premium 2,858,466`, `total_size 4,851`, side bid).
2. **[SENT:analyst_targets]** "spot $139.36 above target range $88–137; consensus
   $115–118" → ✓ resolves to phase-7c-sentiment.md §Analyst-revision momentum.
3. **[HIST:vrp]** "VRP +0.1332, PREMIUM_SELLING, IV rank 100" → ✓ resolves to
   phase-5-historical.md §IV regime.

## Sanity checks

- ✓ All phase files present: 0, 0.5, 1, 2, 3, 4, 5, 6, 7, **7b**, **7c**, 8, **8b**, 9, + this audit + `decision.json`.
- ✓ Phase-9 cites ≥3 distinct upstream datapoints (5 in citations summary).
- ✓ Conviction bin ∈ {0.55, 0.65, 0.75, 0.85, 0.95} → 0.65.
- ✓ ≥1 directional (bear call spread 145/155) + ≥1 defined-risk (iron condor 120/125P–150/155C).
- ✓ Sizing math shown; Kelly **p = 0.60** is the phase-5 `high_iv_rank` backtest win-rate
  (n=10, capped 0.85), not the bin.
- ✓ All five risk gates evaluated: fundamentals **NA**, sentiment **CAUTION**,
  correlation **none**, rotation **adverse**, debate **not disconfirmed**.
- ✓ Phase-0.5 `unusual_verdict = GENUINELY_UNUSUAL` reflected in sizing (no-op modifier;
  no top-of-band sizing applied — final is starter ~1%).
- ✓ Structures sized to the front-expiry expected move (`expected_move` 10.64% / $14.82
  in `decision.json`; defined-risk max-loss = the expected-move gap, ≤ size).
- ✓ `decision.json` exists, backfilled (confluence 66, recommended_bin 0.75), and
  passes `validate_decision.py` (incl. `context` / `expected_move` / `gates.sentiment`).

## Final auditor note

The run is **internally consistent and ready for action as written**: ten-plus
phases unanimously reject a directional long and converge on a defined-risk,
fade-skewed vol-sell into a name trading above every analyst target with IV rank 100.
The one honest caveat the auditor underlines is that **confluence (signal agreement,
66) is high while conviction (0.65) is deliberately moderate** — correct, because the
edge is being fought by a real AI-catalyst/sector-inflow tailwind and a binary 5/28
print, so the blueprint's insistence on **starter size, defined-risk wings, and a
post-earnings expression** is the right risk posture, not a hedge to soften.
