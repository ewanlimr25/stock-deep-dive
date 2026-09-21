# Phase 10 — Audit & Confidence Score

## Summary

**Confluence score: 61 / 100** (positive-of-mixed) → raw-signal recommended bin
**0.65**; **phase-9 deliberately set 0.55** — a **downward override** by the binding
debate-disconfirmation gate + the phase-0.5 QUIET context cap. This is a **MISMATCH in
the conservative direction**, which the sizing rubric explicitly permits (gates can
only cut, never add). The run is **internally consistent**: the signal *structure*
leans bullish (OI ladder, cheap vol, mild accumulation), but the *timing/conviction
overlay* (no ignition, QUIET tape, disconfirmed debate) correctly pulls the actionable
read down to a **starter-only 0.55**. **1 explicit contradiction** (phase-8b
disconfirmed), already the binding driver of the size cut. No citation failures.

## Confluence scorecard

| Phase | Score | Justification (diagnostic datapoint) |
|-------|-------|--------------------------------------|
| 1 — flow | **0** | 0 sweeps, largest trade a $79k '28 LEAP on the mid, premium trivial `[FLOW:sweeps]` — call-tilt too thin to score; QUIET context caps phases 1–2 anyway. |
| 2 — dark pool | **+** | Large-tier buy_ratio 0.85 ($6.74M) mild accumulation `[DP:block-stratified]`; capped at `+` (not `++`) by QUIET context + one $3.78M sell block. |
| 3 — OI | **++** | Call ladder $20/$22.5/$25, P/C OI 0.53, **all** fresh OI calls, 4-day build `[OI:oi-by-strike]` — the strongest bullish phase. |
| 4 — structure | **+** | Call-bid complacent skew + dealers buy dips (DEX +$1.63M) `[STRUCT:dex]`; held to `+` by the vol-**dampening** positive-gamma pin. |
| 5 — historical | **+** | VRP −0.566 cheap-vs-realized + 4-day OI build `[HIST:vrp]`/`[HIST:oi-trend]`; `+` not `++` due to choppy 4/4 flow + universe-pooled p. |
| 6 — macro | **0** | Idiosyncratic (beta 0.37, neg-corr to DDOG); generic sector tailwind FSLY doesn't capture `[MACRO:portfolio_correlation]` — genuinely neutral. |
| 7 — insights | **0** | Composite MIXED, confidence 4.7%, balanced DP `[INSIGHT:conviction-matrix]` — no bias. |
| 7b — fundamentals | **+** | CONFIRM, improving turnaround (4/4 beats crossing into profit) `[FUND:earnings_surprise]`; `+` not `++` — still unprofitable (−16% op margin). |
| 8 — agents | **− (net)** | 2 LONG (+2 ea) / 2 NEUTRAL (−2) / 1 RANGE (−2) → **−2**; uniformly conv 2, no short. |

**Raw score (symmetric):** +41 (phases +43, desk −2)
**Context modifier (phase-0.5):** QUIET → phases 1–2 capped at `+` (applied: phase-1
scored 0 on merit, phase-2 capped at `+`).
**Base score:** round((41+130)/260×100) = **66 / 100**
**Debate penalty (phase-8b):** **−5** (disconfirmed; bull 0.55 = bear 0.55)
**Sentiment penalty (phase-7c):** −0 (NO-CUT / BALANCED)
**Confluence_score:** **61 / 100**
**Recommended bin (raw signal):** **0.65** (band 50–64… 61→0.65)
**Phase-9 actual bin:** **0.55** — ⚠️ **MISMATCH (intentional, conservative)**

### Why the mismatch is correct

The confluence score measures **raw signal confluence** (the structure is genuinely
bullish → 61/0.65). Phase-9's bin is set **after the binding downside gates**, which
the confluence formula only partially captures (it applies the −5 debate penalty but
not the *bin down-shift* or the QUIET *starter cap*). Two gates pull phase-9 below the
raw band:
1. **Debate disconfirmed (8b, 0.55/0.55)** → rubric mandates a one-bin down-shift +
   size-step cut. 0.65 → 0.55.
2. **Phase-0.5 QUIET** (volume 9th self-pctile) → caps directional size at **starter**.
Both are downside-only; an override *downward* is always legal. Phase-9 at 0.55/starter
is the correct actionable read; the 0.65 confluence is the (accurate) statement that
the *underlying structure* is better than the *tradeable conviction* — exactly the
"armed but not triggered" thesis. **Not an error; flagged for transparency.**

## Contradictions

- **phase-8 / phase-8b (debate disconfirmed):** the desk split LONG-small vs WAIT and
  the debate tied at 0.55 (bull = bear) → the adversarial pass did **not** clear the
  trade to size. **Resolution: applied** — phase-9 down-shifted to 0.55 and cut size to
  a **starter (0.5%)**, with the real position deferred to the **$18.5–$19 ignition**.
  *Wait-for-confirmation datapoint:* a volume/sweep break through $18.5–$19.
- (No phase scored `--`. The phase-8 net `−` reflects the 2-NEUTRAL/1-RANGE
  stand-aside majority, not a bearish signal — there were 0 shorts. Logged as the
  conviction drag, already priced into the starter sizing.)

## Citation failures

Spot-checked 3 phase-9 thesis citations:
1. `[HIST:vrp]` "VRP −0.566, RV 144% >> IV 88%" → resolves: phase-5 VRP table,
   PREMIUM_BUYING regime. ✅
2. `[OI:oi-by-strike]` "$20 call wall net +14,840, ladder 20/22.5/25" → resolves:
   phase-3 OI walls table. ✅
3. `[FLOW:sweeps]` "0 sweeps on a +4.9% day" → resolves: phase-1 sweeps section
   (0 contracts). ✅

**No citation failures.**

## Sanity checks

- ✅ All phase files present: 0, 0.5, 1, 2, 3, 4, 5, 6, 7, 7b, 7c, 8, 8b, 9, 10 + decision.json.
- ✅ Phase-9 cites ≥3 distinct upstream datapoints (7 distinct tags).
- ✅ Conviction bin ∈ {0.55, 0.65, 0.75, 0.85, 0.95} → 0.55.
- ✅ ≥1 directional (20/22.5 call debit spread) + ≥1 defined-risk (17.5/15 put credit spread) structure.
- ✅ Sizing math shown; Kelly `p` = phase-5 backtest win-rate (0.60, source=backtest, N=70), not the bin.
- ✅ All five risk gates evaluated (fundamentals CONFIRM / sentiment NO-CUT /
  correlation CLEAN / rotation neutral / **debate disconfirmed→cut**) + phase-0.5
  QUIET reflected (starter cap — binding).
- ✅ `decision.json` exists and passes `validate_decision.py` (OK), incl. context /
  expected_move / gates.sentiment fields. `gates.debate_disconfirmed = true` correctly set.
- ⚠️ `expected_move` field carries the **daily** implied move (2.46%); the structure
  is sized to the **July expected move (~±32%)** per phase-9 §Expected move. Same
  field-convention nuance noted in the CRM audit — non-blocking.
- ✅ Confluence/bin **mismatch is intentional and explained** (gates cut below the raw band).

## Final auditor note

The run is **internally consistent and ready for action as a starter-size,
defined-risk, ignition-triggered optionality long**: the bullish *structure* scores 61
(0.65 band), but the binding debate-disconfirmation + QUIET-context gates correctly
pull the *actionable* conviction to 0.55 / starter — the deliberate, conservative
mismatch is the whole "armed but not triggered" thesis expressed in the sizing. No
revision required; the only watch-item is the `expected_move` daily-vs-front-expiry
field convention (cosmetic).
