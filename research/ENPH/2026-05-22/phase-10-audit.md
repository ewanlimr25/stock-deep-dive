# Phase 10 — Audit & Confidence Score

**Ticker:** ENPH
**As-of date:** 2026-05-22
**Generated:** 2026-05-25T22:43:20Z
**Dominant bias audited:** LONG (conditional/token), phase-9

## Summary

**Confluence score: 35/100** → recommended conviction bin **0.55** (band 30–49). Phase-9's
actual bin is **0.55 — MATCH.** The run is **internally consistent**: the signal phases
(1,2,3,7) genuinely lean bullish, but four phases actively fight a directional long
(phase-4 long-gamma pin + negative vanna, phase-5 doubled/extended at IV-%ile 100, phase-6
rate headwind, phase-7b BEARISH fundamentals), the phase-8 desk is split 4 ways, and the
phase-8b debate disconfirmed the unconditional long. **4 contradictions logged**; all 3
spot-checked citations resolve; `decision.json` validates `OK`. A score of 35 correctly
says "the dominant bias is being fought by the data" — phase-9's response (token 0.5%
size, $65-trigger-gated, defined-risk only, symmetric fade) is the appropriate expression.

## Confluence scorecard

| Phase | Score | Justification (datapoint) |
|-------|-------|---------------------------|
| 1 — flow | **+** | Call/put premium 3.1:1, net +$5.55M `[FLOW]`, but `dominant_direction MIXED` + $2.5M LEAP put → mild, not strong, agreement |
| 2 — dark pool | **+** | Block tier **95.3% buy** `[DP:block_stratified]` (strong) — dialed from `++` because the largest print is a $9.6M post-market block that may be a portfolio trade |
| 3 — OI | **+** | June **$70C OI +4,616 ask-driven opening longs** `[OI:biggest_increases]`; offset by long-dated put hedges |
| 4 — structure | **−** | Long-gamma **pin $60–65** + **negative vanna at IV-rank 92 → falling IV = dealer SELLING** `[STRUCT:vanna_charm]` — structure fights a clean directional long |
| 5 — historical | **−** | **Doubled $30.77→$63.93**, IV %ile **100**, VRP FAIR `[HIST]` — the move is banked; mildly contradicts a fresh long |
| 6 — macro | **−** | CPI +3.78% YoY / 10y 4.57% solar headwind, **TRANSITIONAL** regime, spot above GS $57 target `[MACRO]` |
| 7 — insights | **+** | UW `conviction_matrix` **DIRECTIONAL_LONG** + ACCUMULATION `[INSIGHT]`, but absent top-50 confluence (mature/rich) |
| 7b — fundamentals | **−−** | **BEARISH / CAUTION (near-VETO)**: Q1'26 rev **−18% QoQ**, GAAP loss, beat aided by one-time rev `[FUND]` — 2 axes contradict |
| 8 — agents | **−4 (1/4 align)** | sweep-tracker LONG (+2); contrarian SHORT, accumulation NEUTRAL, risk-monitor RANGE (−2 each); earnings-scout MISSING |

**Raw score (symmetric):** (+7+7+7−7−7−7+7−15) = **−8** (phases) + **−4** (phase-8) = **−12**
**Base score:** round((−12 + 130)/260 × 100) = **45**/100
**Debate penalty (phase-8b):** **−5** (disconfirmed — bull_residual 0.55 < bear_residual 0.70)
**Sentiment penalty (phase-7c):** **−5** (tier_adjustment CAUTION); VETO penalty n/a
**Confluence_score:** 45 − 5 − 5 = **35**/100
**Recommended bin:** **0.55** (band 30–49 → 0.55–0.65; 8b disconfirmation pins the floor)
**Phase-9 actual bin:** **0.55** — **MATCH**

Context modifier check: phase-0.5 `unusual_verdict = GENUINELY_UNUSUAL` → no cap applied to
phases 1–2 (they kept `+`, not forced down). Correctly handled.

## Contradictions

- **phase-4 (structure):** long-gamma pin $60–65 + negative vanna means a directional long
  bleeds below $65 as IV mean-reverts. — *Resolution: tighten invalidation* — phase-9 already
  gates entry to a confirmed $65 break and uses a debit **spread** (not naked call) to cap
  the vega/vanna bleed. ✓ addressed.
- **phase-5 (historical):** the stock already doubled at IV-%ile 100 / VRP-fair; the easy,
  asymmetric money is banked. — *Resolution: downgrade conviction* — phase-9 at 0.55 (floor)
  and token 0.5% size. ✓ addressed.
- **phase-6 (macro):** sticky inflation + 10y 4.57% + TRANSITIONAL regime + price above the
  GS $57 target are a net headwind for rate-sensitive solar. — *Resolution: wait for
  confirmation* — phase-9 makes the long conditional on a $65 break and flags FOMC June 17 /
  CPI June 11 as trim/stand-aside windows. ✓ addressed.
- **phase-7b (fundamentals, −−):** core business deteriorating (rev −18% QoQ, GAAP loss,
  low-quality beat) while flow is bullish → distribution-into-strength risk. — *Resolution:
  downgrade conviction + tighten invalidation* — phase-9 applied the 7b CAUTION size cut and
  put the distribution-into-strength risk in key_risks. ✓ addressed. *(Note: formal Finnhub
  veto instrument was NA — no key; the BEARISH read is WebSearch-sourced and rounds to a
  CAUTION→VETO boundary. The audit flags this as a data-quality limitation, not a clean veto.)*

## Citation failures

None — all 3 spot-checked phase-9 thesis citations resolve:
1. `[DP:block_stratified]` "95.3% buy" → phase-2 §Tier breakdown: block `buy_ratio 0.953`. ✓
2. `[OI:biggest_increases]` "$70C +4,616 (ask 5,400 vs bid 275)" → phase-3 §Largest OI
   increases: `oi_diff_plain 4616`, prev ask 5,400 / bid 275. ✓
3. `[SENT:short_interest]` "32.53% float short" → phase-7c §Short interest: 32.53%, 4.63
   d-to-cover, peers 7.24%. ✓

## Sanity checks

- ✓ All `phase-*.md` present (0, 0.5, 1, 2, 3, 4, 5, 6, 7, 7b, 7c, 8, 8b, 9) + this audit.
- ✓ Phase-9 thesis cites ≥3 distinct upstream datapoints (7 listed; mix of phases 1–4, 5–7, 6/8).
- ✓ Conviction bin 0.55 ∈ {0.55, 0.65, 0.75, 0.85, 0.95}.
- ✓ ≥1 directional (65/72.5 call debit spread) + ≥1 defined-risk (60/52.5 put debit spread).
- ✓ Sizing math shown; Kelly `p` = phase-5 win-rate 1.00 → N-capped 0.75 (n=8), with the
  unreliability caveat surfaced; not a bin fallback.
- ✓ All five risk gates evaluated in phase-9: fundamentals (CAUTION), sentiment/crowd
  (CAUTION/CROWDED_LONG), correlation (none live), sector rotation (neutral), debate
  (disconfirmed). Phase-0.5 `unusual_verdict` (GENUINELY_UNUSUAL) reflected — no top-of-band cap needed; size driven to token by the gate cascade.
- ✓ Structures sized to the front-expiry expected move; `expected_move` (±28% / ±$18 to
  6/18) in `decision.json`; both target strikes inside the priced range.
- ✓ `decision.json` exists and passes `validate_decision.py` (`OK`), incl. `context`,
  `expected_move`, `gates.sentiment`/`crowd_state`; `confluence_score` 35 and
  `recommended_bin` 0.55 backfilled.
- ✓ Disclaimer present at top of phase-9.

## Final auditor note

The run is **internally consistent and ready for action as written** — phase-9's
conviction (0.55) and recommended bin (0.55) match the confluence score (35), and the
token, trigger-gated, defined-risk structure is the honest expression of a bullish tape
that the fundamentals (7b −−), structure (4 −), extension (5 −), macro (6 −), and the
disconfirming debate all fight. **No revision required.** The single most important
caveat the desk must carry forward: the bullish flow is real but the $30→$64 double was
substantially a **spent short squeeze on a deteriorating core** — so this is a binary
**$65-break** trade, not a trend, and below $60 the symmetric defined-risk fade is the live
plan. Secondary limitation: the fundamental gate ran on WebSearch (no Finnhub key) and the
balance-sheet/FCF/insider axes are blind spots.
