# Phase 10 — Audit & Confidence Score

**Ticker:** MU
**As-of date:** 2026-07-28
**Generated:** 2026-07-29T04:05:00Z
**Dominant bias audited:** **NEUTRAL** (phase-9), conviction bin **0.55**, final directional size **0.00%**

## Summary

**Confluence score: 51 / 100** (base 61, less a −5 debate-disconfirmation penalty and a −5
phase-7c `CAUTION` penalty). That maps to a **recommended conviction bin of 0.65**; phase-9
chose **0.55**, a **one-bin conservative MISMATCH** which is permitted and explained below.

**A 51 is the correct-looking number for this run: it means the evidence is very nearly perfectly
mixed, which is exactly what phase-9 concluded.** The run is internally consistent. Every number
in the chain reconciles — most notably phase-1's DuckDB aggressor split reproduces UW's
`bullish_premium`/`bearish_premium` **to the dollar**, phase-2's classifier replication reproduces
UW's `mega.buy_ratio` of **0.803 to three decimals** before inverting it to 0.227 on the
regular-hours cut, and phase-5's `total_gex` of **-45,676,585** matches phase-4's independent
**-45,676,510** to within 0.0002%.

**Two contradictions logged** (phase-2 at `-`, phase-7b at `--`). Both are genuine, both were
correctly incorporated by phase-9 rather than ignored, and neither is an error. **All four
citation spot-checks resolved.** All fifteen expected artifacts are present and `decision.json`
validates.

## Confluence scorecard

| Phase | Score | Justification (quoting the most diagnostic datapoint) |
|---|:---:|---|
| **1 — flow** | **`+`** | Agrees with NEUTRAL: **net customer delta -$41M ex-0DTE on a $926.7B cap** and net flow **+1.0% of $2.83B gross**, with `sweep-persistence` `dominant_direction = "mixed"` (5/5 sessions) and **zero MU rows in `smart-money-flow`**. `[FLOW:delta_notional DUCKDB]` **Capped at `+` (cannot score `++`) by the phase-0.5 `BUSY_NAME_NORMAL_DAY` context modifier** — option volume was **0.84×** its own 30-day average. |
| **2 — dark pool** | **`-`** | **Contradicts NEUTRAL** by supplying the run's strongest directional signal: regular-hours **`mega.buy_ratio` 0.227 (77% selling)**, every tier <0.5, buy ratio *lowest at the lowest prices* (0.411 in the $790s), after-hours to **$780**. `[DP:block_stratified]` Conviction 4/5. Argues a short is available; phase-9 declined it on executability, not on evidence. |
| **3 — OI** | **`+`** | Agrees with NEUTRAL: genuinely two-sided. Put/call OI runs **2.592 at 3 DTE → 0.635 in the 2027 LEAPs** (near-term fear, long-term optimism), near-dated protective puts closed (**-24,600 contracts**) while a **six-session 750/800 short-put campaign opens** (+2,370 contracts). `[OI:term_structure]` `[OI:biggest_increases DUCKDB]` |
| **4 — structure** | **`+`** | Agrees with NEUTRAL on net: **`FULLY_NEGATIVE` gamma with `zero_gamma_level = null`** is bearish-amplifying, but **max pain sits 13–15% ABOVE spot (930/940)**, `net_vanna` **+5,467** flags a squeeze setup, and skew is **`NORMAL` at 1.053**. `[STRUCT:gex]` `[STRUCT:max_pain]` The regime is also the direct reason a directional stop is unworkable at a 10.1% ATR — which supports flat. |
| **5 — historical** | **`++`** | **Strongly agrees:** phase-5's own verdict is *"conviction that today's signal is HISTORICALLY EDGE-POSITIVE: 2/5 (low)"*. Over 30 sessions, **17 bullish days vs 13 bearish while price fell 24.6%**; over 75 sessions cumulative flow nets **+0.16% of $200.8B gross** with `trend_direction = MIXED`; and `bullish_flow` backtests at a **66.7% win rate with `avg_move_pct` -2.69** — positive hit rate, negative expectancy. `[HIST:trend]` `[HIST:cumulative_premium_flow]` |
| **6 — macro** | **`0`** | Genuinely offsetting. The **CXMT / SK Hynix catalyst is a dated bearish industry signal** (conviction 4), but it is squarely contradicted by **DRAM contract prices +93–98% QoQ, HBM at a 5–8× premium, CXMT HBM3E only in 2027**, and the `market-regime` guidance (*"Half position sizes. Favor defined-risk strategies"*) directly supports the flat call. `[MACRO:CXMT_2026-07-28]` `[MACRO:MarketRegime_2026-07-28]` |
| **7 — insights** | **`++`** | **Strongly agrees:** UW's own composite returns **`conviction_matrix` = `MIXED` at `confidence_pct` 8.2** and **`institutional_accumulation` = `"NEUTRAL — balanced dark pool activity"`**. Its `conviction_matrix` bid/ask counts independently confirm **more contracts sold than bought on both sides** (call_bid 194,377 > call_ask 170,280; put_bid 167,982 > put_ask 148,856). `[INSIGHT:conviction_matrix]` |
| **7b — fundamentals** | **`--`** | **`tier_adjustment = VETO`** (`contradiction_count` = 2). Per the rubric's hard rule a VETO scores at most `--` and **the audit must state that the directional thesis is fundamentally vetoed** — here the veto is against the **SHORT**, on revenue **+166.98% TTM YoY**, EPS **+700.71%**, gross margin **72.57%**, **4/4 earnings beats** and LT debt/equity of **5.1%**. `[FUND:revenueGrowthTTMYoy]` **See the Contradictions note — the mechanical `--` penalises a run that correctly obeyed the veto.** |
| **8 — agents** | **`0` (net)** | 4 non-MISSING agents. **2 NEUTRAL align with the dominant bias (+2 each = +4); 2 SHORT do not (−2 each = −4) → net 0.** No agent voted LONG or RANGE. Average conviction **2.5/5**. `earnings-scout` correctly `MISSING` (earnings 56 days out). `[AGENT:phase-8]` |

**Raw score (symmetric):** 7 − 7 + 7 + 7 + 15 + 0 + 15 − 15 + 0 = **+29** (range −130…+130)
**Base score:** round((29 + 130) / 260 × 100) = **61 / 100**
**Debate penalty (phase-8b):** **−5** — `disconfirmed = true` (bull_residual **0.65** vs bear_residual **0.65**)
**Sentiment penalty (phase-7c):** **−5** — `tier_adjustment = CAUTION` (`crowd_state = CROWDED_LONG`)
**Confluence_score: 51 / 100**
**Recommended bin:** **0.65** (band 50–64)
**Phase-9 actual bin:** **0.55** — **MISMATCH (one bin, conservative)**

### Note on the bin mismatch (not an error)

Phase-9 landed at 0.55 because it applied the phase-8b disconfirmation as a **bin down-shift**
(0.65 → 0.55) per `rubrics/sizing-rubric.md` §"Risk gates", while this audit applies the same
disconfirmation as a **−5 score penalty** per `rubrics/confluence-scoring.md`. **The
disconfirmation is therefore counted twice across the two rubrics.** Absent the phase-9
down-shift, both routes agree on **0.65**.

**No correction is required.** A conviction bin *below* the recommended band is always permitted
(deviations only need justification when they go *upward*), the direction of the discrepancy is
conservative, and with `final_size_pct = 0.00%` the bin has no effect on the position. Recorded
here so `/deep-dive-calibration` can attribute the difference to double-counting rather than to
phase-9 misreading the band. **Suggested rubric fix (propose-only, not applied): the two rubrics
should reference a single disconfirmation adjustment rather than each applying their own.**

## Contradictions

- **phase-2 (dark pool):** The strongest, best-evidenced directional signal in the run —
  regular-hours `mega.buy_ratio` **0.227** with selling heaviest at the lowest prices and an
  after-hours slide to **$780** — argues that a tradeable short exists, which conflicts with
  phase-9's NEUTRAL bias and 0% size. **Suggested resolution: WAIT FOR CONFIRMATION.** The
  specific datapoint that resolves it is already named in phase-9's invalidation — **two daily
  closes below $800** would convert the distribution read into an executable path toward $750;
  **two sessions of regular-hours `mega.buy_ratio` >0.55** would kill it. Phase-9 did not ignore
  this phase; it declined the trade on an executability argument (an 8.6% objective inside a
  10.1% ATR), which the phase-8b debate independently upheld.
- **phase-7b (fundamentals):** `tier_adjustment = VETO` scores `--` under the rubric's hard rule
  and costs the run 15 raw points. **The conflict is with the rubric, not with the analysis.**
  The rule was written for the common case (a bullish flow thesis vetoed by deteriorating
  fundamentals = distribution into strength). Here the veto runs **against a short**, and
  phase-9 **obeyed it** by setting directional size to 0%. **Suggested resolution: DOWNGRADE
  CONVICTION — already done** (phase-9 is at 0.55, below the recommended 0.65). **Propose-only
  rubric observation:** the `VETO → at most --` rule should arguably be sign-aware, since a run
  that correctly honours a veto is currently penalised identically to one that ignores it.

*(No other phase scored `-` or `--`.)*

## Citation failures

**None.** Four of phase-9's thesis citations were spot-checked by grep against the cited file:

| # | Citation | Claimed value | Resolves in | Result |
|---|---|---|---|---|
| 1 | `[DP:block_stratified]` | regular-hours mega `buy_ratio` **0.227** | `phase-2-dark-pool.md` (11 occurrences) | **✓ PASS** |
| 2 | `[FLOW:delta_notional DUCKDB]` | net customer delta **-$41M** ex-0DTE | `phase-1-flow.md` (5 occurrences) | **✓ PASS** |
| 3 | `[HIST:vrp]` | `vrp` **-0.1308** | `phase-5-historical.md` (6 occurrences) | **✓ PASS** |
| 4 | `[STRUCT:gex]` | `total_gex` **-45,676,510** | `phase-4-structure.md` (4 occurrences) | **✓ PASS** |
| 5 | `[FUND:revenueGrowthTTMYoy]` | revenue **+166.98%** TTM YoY | `phase-7b-fundamentals.md` (5 occurrences) | **✓ PASS** |
| 6 | `[DEBATE:residuals]` | `bear_residual: 0.65` | `phase-8b-debate.md` (1 occurrence) | **✓ PASS** |

## Sanity checks

- ✓ **All phase files present** — 14 markdown artifacts plus `decision.json`, including
  `phase-0.5-context.md`, `phase-7b-fundamentals.md`, `phase-7c-sentiment.md` and
  `phase-8b-debate.md`.
- ✓ **Phase-9 cites ≥3 distinct upstream datapoints** — **8** listed in its Citations summary,
  spanning phases 1–4 (tape), 5–7b (historical/insight/fundamental) and 6/8 (macro/agent), which
  satisfies the per-band requirement.
- ✓ **Conviction bin ∈ {0.55, 0.65, 0.75, 0.85, 0.95}** — 0.55.
- ✓ **≥1 directional + ≥1 defined-risk structure** — put debit spread 900/800 Oct-16 (directional,
  explicitly **VETOED / 0%**) and put credit spread 900/800 Oct-16 (defined-risk, carry-only).
  **Both legs are prices actually observed on today's tape** ($196.45 / $122.25), not model
  estimates — a notably stronger standard than the template requires.
- ✓ **Sizing math shown, and Kelly `p` is the phase-5 win-rate** — `p_raw` 0.80 from
  `signal_backtest_win_rate` (`bearish_flow`, `win_rate_n` 10, `win_rate_source` `backtest`),
  N-conditional cap 0.85 → capped **p = 0.80**; b = 1.4257; raw_kelly = **0.6597**; suggested
  **5.00%**. No bin fallback used. Phase-9 also carried forward all four of phase-5's qualifiers
  (market-wide, in-sample, n at the floor, imperfect class-match).
- ✓ **All five risk gates evaluated in phase-9's sizing block** — fundamentals `VETO`,
  sentiment/crowd `CAUTION`/`CROWDED_LONG`, correlation cluster **none active** (with the
  MU/SNDK 0.904 standing constraint recorded), sector rotation `neutral`, debate
  `disconfirmed = true`. Each is shown with its effect.
- ✓ **Phase-0.5 `unusual_verdict` reflected in sizing** — `BUSY_NAME_NORMAL_DAY` is named as the
  context modifier and top-of-band sizing is explicitly forbidden; it also correctly capped
  phases 1–2 at `+` in this scorecard.
- ✓ **Structures sized to the front-expiry expected move** — `expected_move` present in
  `decision.json` (`front_expiry_pct` 7.904, `front_expiry_abs` 64.7944, source
  `[CTX:implied_move]`). The $100-wide spread = **12.2% of spot = 1.54× the priced move**, and
  the catalyst-gap check (±$64.79 → $755.74 / $885.32) confirms a single-catalyst gap **cannot**
  exceed the defined max loss.
- ✓ **`decision.json` exists and passes `validate_decision.py`** — including the `context`,
  `expected_move` and `gates.sentiment` fields. Re-validated after backfill (below).
- ✓ **Disclaimer present** at the top of `phase-9-trade-plan.md`.
- ✓ **Immutability respected** — this is v1; no pre-existing `phase-*.md` was overwritten in
  `research/MU/2026-07-28/`.
- ⚠ **Data-availability caveats carried, not hidden** (each surfaced in its phase's
  `## Tool errors`): Finnhub `eps-estimate` / `revenue-estimate` / `price-target` are **paid-tier**
  (forward consensus is a genuine blind spot); **FRED unavailable** (no `FRED_API_KEY` — rates,
  2s10s and core PCE are absent, macro sourced via WebSearch with verified release dates);
  `fz quote` **degraded to 14 of 84 fields** (float/SI/analyst re-sourced from `fz screen` views);
  `uw insights analyst-vs-flow` returned **no analyst consensus** (yfinance HTTP 401); Finnhub
  `company-news` delivered a **6-day window instead of 14**; and **today's OI is unobservable**
  (the OI file window is 7/27→7/28, so today's $28.4M put-strip sale settles tomorrow).
- ⚠ **Bin mismatch (one bin, conservative)** — documented above as double-counting of the
  phase-8b disconfirmation across two rubrics. Not an error; no revision required.

## `decision.json` backfill

`confluence_score` **51** and `recommended_bin` **0.65** written into the envelope phase-9 left as
`null`, and `paths.audit` set to `phase-10-audit.md`. Re-validated:

```
python3 .claude/skills/stock-deep-dive/schemas/validate_decision.py --file research/MU/2026-07-28/decision.json
→ OK: research/MU/2026-07-28/decision.json is a valid DeepDiveDecision
```

## Final auditor note

**The run is internally consistent and ready for action, and the action it recommends is to take
no position.** Its central claims survive adversarial scrutiny because they were derived by
decomposing UW's own aggregates rather than by asserting against them — the `bullish_premium`
identity reconciles to the dollar, the `mega.buy_ratio` replication reproduces 0.803 before
inverting it to 0.227, and the two composite tools that could have been read as bullish
(`signal-confluence` 3/6, `price-vs-flow` divergence) were each traced to a specific, named
artifact rather than dismissed.

**The one thing a reader should not conclude from a score of 51 is that the analysis was
inconclusive.** It was conclusive: MU's options tape carries no directional information
(net customer delta ≈ −$41M on a $926.7B cap), the dark pool distributed, the fundamentals
forbid pressing that as a short, realised volatility exceeds implied so every downside structure
costs more than the move it targets, and the bearish objective sits inside a single day's range —
with a binary FOMC landing tomorrow into a book with no gamma brake. **The correct output of a
good process on this evidence is a well-documented zero.**
