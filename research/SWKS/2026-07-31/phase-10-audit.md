# Phase 10 — Audit & Confidence Score

**Ticker:** SWKS
**As-of date:** 2026-07-31
**Generated:** 2026-08-02
**Dominant bias audited:** **NEUTRAL** (phase-9; RANGE sub-form, $60–65)

## Summary

**Confluence score: 49 / 100.** Recommended conviction bin **0.55–0.65**;
phase-9's actual bin is **0.55** — **MATCH**, at the bottom of the band, which is
the correct place to sit given that **four of five risk gates fired**. The run is
**internally consistent**: nine of eleven phases either agree with the NEUTRAL
read or are genuinely thin, and the two that contradict it (**phase 2's dark-pool
accumulation** and **phase 6's macro headwind**) do so from opposite directions,
which is itself evidence for a neutral resolution rather than against it. All
three spot-checked citations resolved. **Six corrections were made across the run
and every one was logged in the emitting phase's `## DATA NOTE / CORRECTION`
block** — including two that overturned earlier phases' conclusions (phase 6
correcting phase 0.5's sector verdict; phase 7c correcting phase 7b's price
target). `decision.json` validates **OK** after backfill.

## Confluence scorecard

Scored against the dominant bias **NEUTRAL**: a phase that finds *no direction*
**agrees**; a phase that finds a *directional signal* **contradicts**.

| Phase | Score | Justification (diagnostic datapoint) |
|---|---|---|
| **1 — flow** | **0** | Content strongly agrees with NEUTRAL — `net_call_premium` **−$170,899** and `net_put_premium` **−$214,781**, both negative; call ask-share **0.175**, put ask-share **0.088**; **zero** ask-side sweeps at $100k. **But the phase-0.5 `QUIET` context modifier caps phases 1–2 at `0`**, so the agreement cannot be scored up. `[FLOW:ask_bid_split DUCKDB]` |
| **2 — dark pool** | **−7** | **The one phase whose headline finding argues against NEUTRAL:** **+341,637 net shares (+$21,160,930) at buy ratio 0.634 on 2026-07-29 and +232,129 (+$14,211,575) at 0.751 on 2026-07-30** — 15–25× the +12,614/+24,390 baseline, 0.383% of float. Directional absorption, not balance. Mitigated (not reversed) by the as-of session itself printing **net −6,697 shares at 0.461**. `[DP:net_imbalance DUCKDB]` |
| **3 — OI** | **+7** | Agrees decisively: *"the option chain is inert."* `biggest-increases --min-oi-change 500` → **empty**; `position-rolls --threshold 500` → **empty**; `smart-positioning --min-oi-change 500` → **empty**; largest change anywhere on the chain = **46 contracts**. Scored `+` not `++` because the phase's own conviction is **1/5**. `[OI:biggest_increases]` |
| **4 — structure** | **+7** | Agrees on direction while supplying the map: `net_dex` **+$3,674,783 = 58,844 share-equivalents = 1.18% of daily volume**, `net_vanna` **+25**, `term-skew` **NORMAL** (1.042), `iv-term-structure` **FLAT** (`kink_expiry: null`). No directional force anywhere. ⚠ Its short-gamma finding (spot on the **−448,437** GEX minimum at 62.5) cuts against the *range mechanism* — logged below, but it does not flip the directional sign. `[STRUCT:dex]` `[STRUCT:gex]` |
| **5 — historical** | **+7** | Agrees: *"no measurable edge."* `signal_backtest` → **`total_signals: 0`** on two runs ⇒ `win_rate_source: null`; 90-day cumulative premium flow **`MIXED`** (+$6.71M net on $178.6M two-way = a 3.8% tilt). `[HIST:signal_backtest]` `[HIST:cumulative_premium_flow]` |
| **6 — macro** | **−7** | Contradicts: **net HEADWIND at conviction 4/5**. Technology was the **largest net-SOLD sector of eleven at −$187,715,752** aggressor-adjusted; FOMC held **9–3 with all three dissenters wanting a HIKE**; DGS10 **+24bp m/m**; dividend **eliminated**. Also establishes that the name is **binary-driven, not range-driven** — an undated SAMR ruling is the only event that can exceed the ±9.10% implied move. `[MACRO:MarketRegime_2026-07-31 UW]` |
| **7 — insights** | **+7** | Agrees: `conviction-matrix` returns **`scenario: "MIXED"` at `confidence_pct: 7.2`**; `institutional-accumulation` = **`NEUTRAL`**; `signal-confluence` = **0 of 6 bullish**. The mild bearish lean (2/6 bearish) is discounted because both its factors were shown misclassified. `[INSIGHT:conviction_matrix]` |
| **7b — fundamentals** | **0** | `fundamental_signal: **NEUTRAL**`, `tier_adjustment: **CAUTION**`, `contradiction_count: 1`. Genuinely two-sided: **4/4 earnings beats (avg +11.26%)**, net cash ~$417M, positive insider MSPR every month — against **`epsGrowthTTMYoy` −6.00%** on `revenueGrowthTTMYoy` +2.33% and **ROE 6.30%**. Neither confirms nor contradicts a NEUTRAL bias. `[FUND:metric]` |
| **8 — agents** | **+10** | **5 of 5 aligned.** 3× NEUTRAL / 2× RANGE / **0 LONG / 0 SHORT**, average conviction **2.0/5**, unanimous on support **$60.00** and resistance **$65.00**. Every agent contributes +2. `[AGENT:all]` |

**Raw score (symmetric, −130 … +130):**
`0 + (−7) + 7 + 7 + 7 + (−7) + 7 + 0 + 10 = ` **+24**

**Base score:** `round((24 + 130) / 260 × 100) = round(59.23) = ` **59 / 100**

**Gate penalties (one-sided, applied after normalization):**
- **Debate (phase-8b): −5** — `disconfirmed: true` (bull_residual **0.55** vs
  bear_residual **0.65**)
- **Sentiment (phase-7c): −5** — `tier_adjustment: CAUTION`
- Sentiment VETO: not applicable (0)

**Confluence_score: 59 − 5 − 5 = 49 / 100**

**Recommended bin (band 30–49): 0.55–0.65**
**Phase-9 actual bin: 0.55 — MATCH** (bottom of the band, consistent with four of
five gates firing and a `QUIET` context verdict)

A score of **49** sits one point below "perfectly mixed." That is the right answer
for a run in which the desk returned zero directional votes, the signal backtest
returned zero firings, and the two contradicting phases pull in opposite
directions.

## Contradictions

- **phase-2 (dark pool): −7.** Its headline finding — **+573,766 net shares
  absorbed across 2026-07-29/30** at buy ratios of 0.634 and 0.751, a 15–25×
  step-change over baseline — is a **directional** signal inside a NEUTRAL thesis.
  If real institutional accumulation is under way, the plan's NEUTRAL bias
  understates the upside. **Resolution: wait for confirmation.** The specific
  datapoint that resolves it is already in phase-9's monitoring checklist — the
  **cleaned regular-session directional buy ratio** (VWAP / `prior_reference_price`
  prints and the 16:00 auction excluded). Two more sessions above ~0.60 on >300k
  directional shares would justify upgrading the bias; two below 0.45 voids it.
  Note the contradiction is **partially self-limiting**: phase 2 itself records the
  as-of session as **neutral (0.461, net −6,697 shares)**, and phase 8's
  `accumulation-hunter` — the agent best placed to judge — **could not distinguish
  the absorption from merger-arb stock-leg hedging**, citing phase 5's zero backtest
  signals and phase 3's zero OI corroboration.

- **phase-6 (macro): −7.** Net **HEADWIND at conviction 4/5**, and more
  importantly it establishes that SWKS is a **binary-driven security, not a
  range-bound one**: a live Qorvo merger (0.960 SWKS + $32.50 cash, **China SAMR in
  Phase III**), an **eliminated 4.56% dividend**, a **~$2B debt raise**, and a
  **21.93% arb short**. A $60–65 range thesis is the wrong frame if an undated
  ruling can gap the stock beyond ±9.10%. **Resolution: tighten invalidation** —
  and phase 9 already did, correctly, by making **any SAMR ruling in either
  direction a macro invalidation that voids the thesis on the headline rather than
  on the price.** No further action needed; the contradiction is already priced into
  the plan's exit rule and into the 0.25% size.

**Constructive tension, not a contradiction (logged for completeness):**
`phase-4-structure.md` scores **+7** on direction but its **short-gamma** finding
(`gex.regime: NEGATIVE`, spot sitting on the **−448,437** per-strike minimum at
62.5) argues that the $60–65 box is a **map of supply and demand rather than a
mechanism that holds price**. Phase 8b's defender **conceded this point in round 2**
and phase 9 carried it verbatim into `key_risks`. Correctly handled upstream;
recorded here so it is not lost.

## Citation failures

**None.** Three citations from phase-9's thesis were spot-checked against the
cited source file and all three resolved exactly:

| # | Citation | Claimed value | Verified in |
|---|---|---|---|
| 1 | `[OI:oi_by_strike]` | `put_wall_support` **$60.00**, `net_oi` **−625** (514 calls / 1,139 puts), `distance_pct` **−3.78%** | `phase-3-positioning.md` — row found verbatim: `\| **60** \| 514 \| **1,139** \| **−625** \| **put_wall_support** \| **−3.78%** \|` ✓ |
| 2 | `[FLOW:unusual_volume]` | Aug-21 52.5 put, `vol_oi_ratio` **3.5195** | `phase-1-flow.md` — string `3.5195` present (2 occurrences: §Key signals and §Tool calls) ✓ |
| 3 | `[HIST:signal_backtest]` | `dark_pool_accumulation` → `total_signals: 0` | `phase-5-historical.md` — string `total_signals":0` present (2 occurrences: §Signal backtest and §Tool calls) ✓ |

Two further citations were checked opportunistically and also resolved:
`[STRUCT:max_pain]` `holder_value_at_max_pain` **$603,250** in
`phase-4-structure.md` ✓, and `[AGENT:all]` **"LONG: 0. SHORT: 0."** in
`phase-8-agent-views.md` ✓.

## Sanity checks

| Check | Result |
|---|---|
| All `phase-*.md` present, **including `phase-0.5`, `phase-7b`, `phase-7c`, `phase-8b`** | ✓ — 14 phase files + `decision.json` on disk |
| Phase-9 cites ≥3 distinct upstream datapoints | ✓ — **7** listed in §Citations summary, spanning phases 1, 3, 4, 5, 6, 8, 8b |
| Thesis draws from phases 1–4 / 5–7 / 6-or-8 as required | ✓ — `[OI:oi_by_strike]` + `[FLOW:unusual_volume]` (1–4); `[HIST:signal_backtest]` (5–7); `[AGENT:all]` (8) |
| Conviction bin ∈ {0.55, 0.65, 0.75, 0.85, 0.95} | ✓ — **0.55** |
| ≥1 directional + ≥1 defined-risk structure | ✓ — Aug-21 **60/65 call debit spread** (directional) and Aug-21 **55/50 put credit spread** (defined-risk); plus a **third, explicitly rejected** structure (Sep-18 62.5 straddle) with the rejection arithmetic shown |
| Strikes referenced to OI / gamma walls | ✓ — 60 = `put_wall_support` (OI 514/1,139); 65 = `call_wall_resistance` (OI 874/439) **and** max-pain; 55P OI 686, 50P OI 1,307. **All from observed OI, none picked by eye** |
| Sizing math shown explicitly | ✓ — `b`, `raw_kelly`, `fraction`, `cap_pct`, the win-rate-map cross-check, and every gate step with a running size |
| Kelly `p` = phase-5 win-rate, or justified bin fallback | ✓ — `win_rate_source: null` / `win_rate_n: 0` ⇒ **bin fallback, capped at 0.65** ⇒ `p = 0.55`. The populated market-wide classes were **explicitly rejected** (SWKS absent from the `bullish_flow` sample; tool self-labels in-sample; n=9) |
| **All five** risk gates evaluated (fired or not) | ✓ — 7b **CAUTION (fired)**, 7c **CAUTION (fired)**, correlation **0.518 (not fired)**, rotation **ADVERSE (fired)**, debate **disconfirmed (fired)** |
| Phase-0.5 `unusual_verdict` reflected in sizing | ✓ — **`QUIET`** applied as a starter cap; phase 9 states 0.234% is already at/below starter so no further cut |
| Structures sized to the front-expiry expected move; `expected_move` in JSON | ✓ — band **$56.61–$67.95** stated; call spread target at **0.48×** the priced move; put spread short strike **below** the one-move floor (**N4 PASSES**); straddle **rejected at 1.84×** |
| No upward size deviation | ✓ — `deviation_reason: null`; would be forbidden anyway (four gates fired + `QUIET`) |
| Disclaimer present at top of phase-9 | ✓ |
| `decision.json` exists and passes `validate_decision.py` | ✓ — **`OK: … is a valid DeepDiveDecision`**, re-validated after the phase-10 backfill |
| `confluence_score` / `recommended_bin` backfilled | ✓ — **49** and **0.55** written; `paths.audit` set to `phase-10-audit.md` |
| `context` / `expected_move` / `gates.sentiment` fields present | ✓ — `context` {`QUIET`, rank 565, iv_rank 52.8977, self_pctile 66.2}; `expected_move` {9.098%, $5.6749}; `gates.sentiment` **CAUTION**, `gates.crowd_state` **CROWDED_SHORT** |
| Immutability (no phase MD overwritten) | ✓ — v1 run; directory was empty at intake |

**One deviation from spec, disclosed and scored:** `phase-8-agent-views.md` ran
**`earnings-scout` despite earnings being 88 days out**, redirecting its brief to
the undated SAMR binary. The phase file flags this explicitly under `## Tool
errors` with its rationale. **The audit accepts it**: the skip rule exists to avoid
running a pre-earnings agent when no binary is pending, and one **was** pending. It
materially improved the phase — it produced the desk's only concrete structure
proposal, which phase 9 then evaluated and **rejected on the rubric's own N4
arithmetic**. Had it been skipped, phase 8 would have returned four NEUTRALs at 1.75
average conviction and no proposal to test. **No score adjustment.**

## Cross-phase correction log

Six corrections were made during the run. Each was logged in the emitting phase's
`## DATA NOTE / CORRECTION` block rather than silently applied. Recorded here
because two of them **overturned an earlier phase's stated conclusion** — exactly
the class of drift this audit exists to catch:

| # | Correcting phase | Corrected | Substance |
|---|---|---|---|
| 1 | phase-1 | **phase-0** | `unusual-volume` was recorded "empty" at the tool's **default** vol/OI threshold; at the phase-prescribed `--min-vol-oi-ratio 3` it returns the **3,333-lot 52.5P**. Phase-0's inference ("thin new-position activity") superseded; the 52.5P block is now the plan's central datapoint. |
| 2 | phase-0.5 | **phase-0** | `fz` prices tagged "live 2026-08-02, advisory only" — but 2026-08-02 is a **Sunday**, so `fz`'s 62.28 / −0.32% **reconcile exactly** with the as-of close. Timing caveat withdrawn. |
| 3 | phase-4 | **phase-3** | Phase 3 predicted max pain would be dragged to $75–80 by dead call OI. The returned `pain_curve` shows those strikes generate the **largest** holder value ($5.30M at 80; $40.96M at 100), pushing the minimum **down** to **$65**. Caution **withdrawn**; the $65 magnet is genuine. |
| 4 | **phase-6** | **phase-0.5** | Phase 0.5 reported *"Technology is LEADING the tape (+$2.78B)"* from `sector-flow`'s **call−put** metric. On the **aggressor-adjusted** metric Technology was the **largest net-SOLD sector of eleven (−$187,715,752)**. Both metrics re-derived from the parquet and the aggressor-adjusted column **reproduces `market-regime` exactly across all eleven sectors**. Material correction — it flipped the sector verdict from tailwind to **ADVERSE** and fired a sizing gate. |
| 5 | **phase-7c** | **phase-7b** | Phase 7b carried a consensus price target of **$74.72**; the Finnhub news feed shows that predates the **2026-07-29 revision cluster in which 7 of 8 firms cut**. Corrected anchor: **mean $66.00 / median $67.50** — a ~12% reduction in implied upside (+20.0% → +5.97%). |
| 6 | phase-7b | **phase-0** | `Shs Float` (recorded "unavailable" from the degraded `fz quote`) **recovered as 149.81M** via `fz screen --view ownership`, corroborated to within 0.5% by Finnhub's 150.5M diluted share count and the 150,956,637 derived in phase 2. The phase-2/3 float caveats resolve as **negligible**. The same call recovered **`Short Float` 21.93%**, which became phase 7c's primary input. |

**Assessment:** the correction chain is healthy — later phases caught and reversed
earlier ones **with re-derived evidence**, not assertion, and in every case the
superseded value was retained in the record. Corrections #4 and #5 both moved the
plan **against** the constructive read, and were made anyway.

## Unresolved blind spots

Recorded so the calibration loop can weight this blueprint correctly:

1. **No empirical edge measurement exists.** `win_rate_source: null`,
   `win_rate_n: 0`. The confluence score and the Kelly `p` both rest on the
   conviction bin, not on a measured base rate. **This blueprint should be scored
   by `/deep-dive-calibration` without a win-rate leg, and phase 5 says so
   explicitly.**
2. **The phase-1 short-put floor is unconfirmed.** The OI dataset is **lagged one
   session** (`last_date` 2026-07-30 / `curr_date` 2026-07-31), so the 3,333
   contracts sold on the as-of day can only appear in the **2026-08-03** file —
   beyond this snapshot. The plan's most-cited datapoint is therefore
   **provisional**, and phase 9 correctly made it a signal invalidation rather than
   an assumption.
3. **The analyst-consensus lane is dead in the UW layer.**
   `uw insights analyst-vs-flow` returned **no analyst block** and
   `deep-dive.yahoo_fundamentals` returned **HTTP 401** throughout. The gap was
   filled from Finnhub `/stock/recommendation` and primary reporting, and is
   labelled as such — but the tool-native comparison the skill wanted was
   **not performed**.
4. **Borrow / hard-to-borrow status is unknown.** No fee or HTB tag was
   recoverable for a name with **21.93% of float short**. Recorded as `n/a`, **not**
   inferred as EASY.
5. **`fz quote` is degraded run-wide** (14 of 84 fields), which killed the D6
   analyst cross-source and the D8 RSI/moving-average price-context check. The
   `fz screen` and `fz breadth`/`groups` leaves worked normally.
6. **Two catalyst dates are approximate and flagged as unverified** (July
   employment ~2026-08-07, July CPI ~mid-August), inferred from release cadence
   rather than confirmed against a primary calendar.

## Final auditor note

**The run is internally consistent and ready for action as written — where "as
written" means WATCH-ONLY with a defined $60.00 trigger, not an initiation
today.** Phase 9's conviction bin (0.55) matches the recommended band, its Kelly
`p` correctly falls back to the bin because no empirical win-rate exists, all five
risk gates are evaluated with four firing, both structures are anchored to observed
OI and pass or explicitly fail the expected-move test, and the negative raw Kelly
at spot (**−0.085**) is surfaced rather than buried — which is what turns a
low-conviction range read into an honest "do not chase."

**No revision of phase 9 is required.** The single thing that would change the
blueprint is the phase-2 contradiction resolving: two further sessions of cleaned
dark-pool buy ratio above ~0.60 on >300k directional shares would justify
upgrading the bias off NEUTRAL — and until then, the **undated SAMR ruling makes
any directional size unjustifiable regardless of what the tape does.**
