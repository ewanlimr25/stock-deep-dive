# Phase 10 — Audit & Confidence Score

**Ticker:** ENPH
**As-of date:** 2026-07-27
**Generated:** 2026-07-28T03:05:00Z
**Dominant bias audited:** **NEUTRAL** (from `phase-9-trade-plan.md`)

## Summary

**Confluence score: 29 / 100. Recommended bin: 0.55. Phase-9 actual bin: 0.55 —
MATCH.** Four phases contradict the dominant NEUTRAL bias (1, 6, 7, 7b); three
support it (3, 4, 8); two are genuinely neutral (2, 5). All three citations
spot-checked resolve. All 15 expected artifacts are present, `decision.json`
validates, and every one of the five risk gates was evaluated in phase-9's sizing
block.

**One scoring artifact must be flagged up front, because it drives a third of the
negative score.** The confluence rubric was designed for a *directional* thesis
and mandates that a phase-7b `tier_adjustment = VETO` scores **at most `--`**. But
in this run the 7b veto fires **against a short**, which *supports* the neutral
stance phase-9 adopted. Applying the rule as written costs −15 points for a phase
that in substance agrees with the thesis. **The rule is applied as written** (it
is a hard rule and I will not silently reinterpret it), and the sensitivity is
shown below: scoring 7b on its actual effect would lift the score to 37, which
lands in the 30–49 band and still recommends **0.55**. **The conclusion is robust
to the artifact.**

The run is internally consistent. The three genuine mid-run corrections
(phase-2's put-buyer inference withdrawn by phase-3; the `institutional-accumulation`
label refuted by phase-7; phase-3's "filtered feed" characterisation revised by
phase-7c) were each surfaced by a later phase and carried forward correctly rather
than being buried.

## Confluence scorecard

| Phase | Score | Justification (diagnostic datapoint) |
|---|---|---|
| **1 — flow** | **`-`** (−7) | Verdict is *"bearish, conviction 3/5"* — directionally against NEUTRAL, though it disqualifies itself on magnitude: derived `net_flow = −$258,731` on a $4.84B cap, and `sweep-persistence total_sweep_premium = $1,335,255` [FLOW:sweep_persistence]. Context cap (`+` max) does not bind on a negative score. |
| **2 — dark pool** | **`0`** (0) | Own headline verdict is *"MIXED, leaning DISTRIBUTION"*, conviction 2/5; the only statistically meaningful tier is `large.buy_ratio = 0.555` on n=36 — essentially balanced [DP:block_stratified]. Genuinely neutral. |
| **3 — OI** | **`+`** (+7) | *"PREMIUM SELLING / SHORT VOL … Not a directional book"* — C70 −1,407 `net_ask_bid` and P30/P35 both **sold**, implying a range view of roughly $30–$50 [OI:smart_positioning]. Directly supports NEUTRAL. |
| **4 — structure** | **`++`** (+15) | *"the same book that amplifies a breakdown also mechanically buys a relief rally"* — `regime = FULLY_NEGATIVE`, `net_dex = −$40,323,765`, yet `net_vanna = +913` [STRUCT:vanna_charm], [STRUCT:gex]. Explicitly two-sided and path-dependent at conviction 4/5 — the strongest support for a non-directional stance. |
| **5 — historical** | **`0`** (0) | Cuts both ways and says so: 24 sessions of `FULLY_NEGATIVE` gamma delivering **−28.8%** since the 2026-06-22 flip, against a 74-session `cumulative_premium_flow` of **+$28,650,420** with `trend_direction = "MIXED"`; concluded *"no measurable edge either way"* [HIST:gex_time_series], [HIST:cumulative_premium_flow]. |
| **6 — macro** | **`--`** (−15) | *"HEADWIND (strong)"*, conviction 4/5, 11 headwinds to 4 tailwinds — Section 25D repealed effective 2025-12-31, FY installs guided **−22%**, `DGS10` **+28bp** in 30 days to 4.69% [MACRO:25D_expiry_2025-12-31], [MACRO:DGS10_2026-07-24]. Strongly directional-bearish; contradicts a neutral stance. |
| **7 — insights** | **`-`** (−7) | *"WEAKLY BEARISH, LOW CONFIDENCE"*, conviction 2/5; `price-vs-flow divergence = false` / *"Price and flow are aligned"* bearish, and `conviction-matrix confidence_pct = 21.1` [INSIGHT:price_vs_flow], [INSIGHT:conviction_matrix]. |
| **7b — fundamentals** | **`--`** (−15) ⚠️ | **`tier_adjustment = VETO` — capped at `--` by rubric hard rule; the directional thesis is fundamentally vetoed.** 2 of 3 axes contradict the flow bias: beat rate **4/4** with mean surprise **+19.24%** [FUND:earnings_surprises] and MSPR **+96.66 / +77.60** in the two most recent months [FUND:insider_mspr]. **⚠️ See §Scoring artifact — this veto substantively *supports* the audited NEUTRAL bias.** |
| **8 — agents** | **`+`** (+6) | **4 of 5 align** with NEUTRAL (accumulation-hunter, sweep-tracker, earnings-scout, risk-monitor); 1 dissents LONG (contrarian-scanner). `4 × (+2) + 1 × (−2) = +6`. Avg conviction 2.2/5; **0 of 5 SHORT** [AGENT:*]. |

**Raw score (symmetric, range −130…+130):**
`(−7) + 0 + (+7) + (+15) + 0 + (−15) + (−7) + (−15) + (+6)` = **−16**

**Base score:** `round((−16 + 130) / 260 × 100)` = `round(43.85)` = **44 / 100**

**One-sided gate penalties (applied after normalization, cuts only):**

| Penalty | Fires? | Effect |
|---|---|---|
| Debate (phase-8b `disconfirmed`) | **YES** — `bull_residual 0.65` vs `bear_residual 0.65` | **−5** |
| Sentiment `CAUTION` (phase-7c) | no | 0 |
| **Sentiment `VETO` (phase-7c)** | **YES** — `crowd_state = CROWDED_SHORT` | **−10** |

**Confluence score: 44 − 5 − 10 = 29 / 100**

**Recommended bin (band 0–29): 0.55** — *"slight — or revisit dominant bias entirely"*
**Phase-9 actual bin: 0.55 → ✅ MATCH**

**Context modifier check (phase-0.5).** `unusual_verdict = BUSY_NAME_NORMAL_DAY`
caps phases 1–2 at `+`. Phase-1 scored `-` and phase-2 scored `0`, so **the cap
was not binding** — but it *was* correctly applied upstream (phase-1 explicitly
capped its own downstream contribution at `+`, and phase-9 declined to size at the
top of the band on the same grounds). ✅

### ⚠️ Scoring artifact and sensitivity (mandatory disclosure)

The rubric's phase-7b rule (*"a `tier_adjustment = VETO` is at most `--`"*)
assumes the audited bias is directional and the veto opposes it. **Here the veto
opposes a short while the audited bias is NEUTRAL — so the veto and the thesis
agree, yet the rule forces −15.**

| Scenario | 7b score | Raw | Base | After −15 penalties | Band | Recommended bin |
|---|---|---|---|---|---|---|
| **As-written (used)** | `--` (−15) | −16 | 44 | **29** | 0–29 | **0.55** |
| Sensitivity: 7b on actual effect | `+` (+7) | +6 | 52 | 37 | 30–49 | 0.55–0.65 |

**Both paths recommend 0.55**, which is phase-9's actual bin. The as-written score
of **29** is reported as the official figure; the artifact is disclosed so the
calibration loop does not read it as nine phases fighting the thesis when in fact
one of the four "contradictions" is a rubric-mechanics result.

*Propose-only note for the skill (not applied):* `rubrics/confluence-scoring.md`
should state how phases are scored when the dominant bias is `NEUTRAL`/`RANGE` —
specifically whether a downside gate that *supports* non-participation still
takes the `--` cap.

## Contradictions

- **phase-1 (options flow):** Verdict is bearish (conviction 3/5) against phase-9's
  NEUTRAL, resting on a 5-of-5 bearish sweep campaign — but the campaign is
  **$1,335,255 = 0.027% of market cap** and today's option volume is the **16.4th
  self-percentile**. — **Resolution: wait for confirmation.** The specific
  resolving datapoint is `call_ask_share` crossing **above 0.50** (it has been
  below in **6 of 6** sessions); phase-9 already encodes this as both the primary
  entry trigger and a signal invalidation.
- **phase-6 (macro):** Strong structural headwind (25D repeal, −22% FY installs,
  `DGS10` +28bp) argues the stock should fall, contradicting a neutral stance. —
  **Resolution: tighten invalidation.** Phase-9's macro invalidation (hawkish FOMC
  2026-07-29 / `DGS10` above 4.69%) is correct but the deeper risk is the **Q3
  guide against the ~$85M safe-harbor cliff** — already carried as `key_risks[0]`.
  No further action; the contradiction is acknowledged rather than resolved,
  because macro pessimism is precisely what the positioning gates say is already
  crowded.
- **phase-7 (UW insights):** *"WEAKLY BEARISH"* with `divergence = false`
  contradicts NEUTRAL. — **Resolution: downgrade conviction** — already at the
  floor bin (0.55), so no further downgrade is available. Note the phase's own
  conviction is 2/5 and `conviction-matrix confidence_pct = 21.1`, so the
  contradiction is weak by construction.
- **phase-7b (fundamentals):** `VETO`, capped at `--`. Business deteriorating on
  every operating measure (revenue **−20.6%**, gross margin **−11.76pp**, GAAP
  **+$29.7M → −$7.4M**) while the gate blocks the short. — **Resolution: no action
  — this is the scoring artifact above.** The veto *supports* phase-9's decision
  not to be short; it does not fight the thesis. **Substantively there are three
  genuine contradictions, not four.**

## Citation failures

**None.** Three thesis citations spot-checked by direct grep against the cited
files; all resolve to real datapoints:

| # | Citation | Claimed value | Verified in | Result |
|---|---|---|---|---|
| 1 | `[FLOW:insights_deep_dive]` | `net_flow = −$258,731` (derived `bullish − bearish`) | `phase-1-flow.md` — 6 occurrences | ✅ resolves |
| 2 | `[STRUCT:vanna_charm]` | `net_vanna = +913` | `phase-4-structure.md` — 6 occurrences | ✅ resolves |
| 3 | `[SENT:short_interest]` | short interest `15.09M → 16.79M = 17.55%` of float | `phase-7c-sentiment.md` — 10 occurrences | ✅ resolves |

Three additional spot-checks passed: `[FUND:earnings_surprises]` mean surprise
**+19.24%** (phase-7b, 6 hits); `[AGENT:earnings-scout]` **+39%** earnings move
(phase-8, 12 hits); `[DEBATE:disconfirmation]` `bull_residual 0.65`
(phase-8b, 1 hit). **6 of 6 verified.**

## Sanity checks

| Check | Result |
|---|---|
| All `phase-*.md` present incl. 0.5, 7b, 7c, 8b | ✅ **15 artifacts** — phase-0, 0.5, 1, 2, 3, 4, 5, 6, 7, 7b, 7c, 8, 8b, 9, 10 + `decision.json` |
| Phase-9 cites ≥3 distinct upstream datapoints | ✅ **9 citations** spanning phases 0.5, 1, 4, 5, 6, 7b, 7c, 8, 8b — satisfies the 1-from-phases-1-4 / 1-from-5-7 / 1-from-6-or-8 rule |
| Conviction bin ∈ {0.55, 0.65, 0.75, 0.85, 0.95} | ✅ **0.55** |
| ≥1 directional + ≥1 defined-risk structure | ✅ Aug-21 **$40/$45 call debit spread** (directional) + Aug-21 **$35/$30 put credit spread** (defined-risk carry) |
| Sizing math shown; Kelly `p` = phase-5 win-rate | ✅ `p_raw = 0.556` (n=9, `backtest`) → N-cap 0.75 → `p = 0.556`; `b = 1.49`; `raw_kelly = 0.258`; win-rate map ceiling **half (2.5%)**; **final 0.00%** |
| All five risk gates evaluated | ✅ fundamentals **VETO** · sentiment **VETO** (`CROWDED_SHORT`) · correlation **none** · rotation **adverse** · debate **disconfirmed** |
| Phase-0.5 `unusual_verdict` reflected in sizing | ✅ `BUSY_NAME_NORMAL_DAY` explicitly cited as forbidding top-of-band sizing and any upward deviation |
| Structures sized to front-expiry expected move | ✅ width $5.00 > expected move $4.65; call-spread breakeven **+9.3%** inside ±12.25%; put-spread breakeven **$33.37** ≈ the exact lower bound $33.36; `expected_move` present in JSON |
| `decision.json` exists and validates | ✅ `OK: … is a valid DeepDiveDecision` (validated pre- and post-backfill) |
| Option prices are real, not estimated | ✅ all four legs quoted from actual NBBO in `bot-eod-report-2026-07-27.parquet` |
| No fabricated max-pain / invented commands | ✅ max pain **$41** (2026-07-31) and modal **$40** read natively from `uw options-structure max-pain` |
| Structures avoid unwanted binary exposure | ✅ both expire **2026-08-21**, past earnings (07-28) and FOMC (07-29); entries are **conditional and post-event** |
| Look-ahead guard on as-of run | ✅ phase-7b (earnings/MSPR) and phase-7c (news) both confirmed all records ≤ 2026-07-27 |

**All checks pass.**

### Unresolved data conflicts carried from upstream (recorded, not resolved)

These were surfaced verbatim by their phases and none is decision-relevant, but
the calibration loop should see them:

1. **`gex`: `total_gex = −566,158` vs Σ`per_strike = −916,496`** — 62% gap inside
   one payload (phase-4). Sign/regime unaffected; no conclusion depends on the
   magnitude.
2. **`term-structure total_oi = 241,974` vs `deep-dive total_open_interest =
   355,935`** — 32% gap between two UW surfaces (phase-3). All wall/cliff
   percentages computed on one denominator consistently.
3. **Contract-level volume disagreement between `bot-eod-report` and
   `chain-oi-changes`** (Nov-20 P35: 811 vs 6; Nov-20 C70: 3 vs 1,418) — phases 3
   and 7c. **Both files agree on the OI levels that actually matter**
   (P35 407→412, C70 359→1,683), and `bot-eod-report` totals to the exact screener
   premium ($4,764,749) and volume (14,999).
4. **Jun-2027 P40/P45 sweeps have no OI footprint** — 258 contracts reported
   traded against total Jun-2027 put OI of 52 (phase-1 vs phase-3). Likely the
   same floor/negotiated print class as the P35 cross; unproven.
5. **Two different `net_flow` definitions in the CLI** — `sector-flow`
   (call−put premium, Tech +$366.8M) vs `market-regime`/screener
   (bullish−bearish, Tech +$21.0M), a 17× gap (phase-6). Never compared.
6. **Recurring regime-label defects** — `today-gamma-flip` `regime = POSITIVE`
   with spot below `today_zero_gamma`; `gex-time-series` 2026-07-15 labelled
   POSITIVE with `total_gex = −1,216,059`. Both quoted verbatim, neither
   interpreted.
7. **Finnhub `/stock/peers` misclassifies ENPH as semiconductor equipment**
   (phase-7b) — discarded in favour of `fz screen --filter ind_solar`.

### Corrections chain (each caught by a later phase and propagated)

| Correction | Raised by | Status |
|---|---|---|
| Phase-2's *"customer bought the 800-lot Nov-$35 puts → downside demand"* | **phase-3** (OI moved only 407→412; `{futures_floor}`/`slft`) | **Withdrawn**; never reached phases 8/8b/9 |
| `institutional-accumulation` = *"ACCUMULATION, buy_sell_ratio 2.18"* | **phase-7** (excluding the 129k closing cross, `buy_ratio` 0.679 → **0.450**) | **Refuted**; independently re-verified by `accumulation-hunter` |
| Phase-3's *"`bot-eod-report` is a filtered notable-print feed"* | **phase-7c** (its ENPH totals match the screener **exactly**) | **Revised**; no number changed |
| Phase-0.5's *"~45% of the short base has covered"* framing | **phase-7c** (shorts **added** 15.09M → 16.79M in the latest period) | **Reframed**; both true at different horizons |

**This is the audit's most positive finding.** Four separate over-reads were each
caught downstream and none survived into the trade plan.

## Backfill of `decision.json`

`confluence_score` and `recommended_bin` written into the fields phase-9 left
`null`; re-validated after the edit — see §Sanity checks. Both pre- and
post-backfill validation printed `OK`.

## Final auditor note

**The run is internally consistent and the blueprint is ready for action as
written — where "action" is explicitly `final_size_pct = 0.00%`, watch-only, with
two conditional post-event structures.** The confluence score of **29** and the
matched **0.55** bin correctly encode a setup where the directional evidence
(bearish flow, bearish macro, deteriorating fundamentals) is real but is
neutralised by two independent positioning vetoes, an armed vanna squeeze, and a
±12.25% binary over a surface with no gamma brake and no pin.

**No revision to phase-9 is required.** The one thing a reviewer should weigh
independently is the **n=2** evidence base behind the "implied move is cheap"
finding (+39% / −9.1%) — it is the single most consequential new fact in the run,
it was independently re-verified, and it is still two observations.
