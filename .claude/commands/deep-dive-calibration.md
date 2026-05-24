---
description: Retrospectively mark past stock-deep-dive blueprints to market. Uses the dated decision.json + phase-9/phase-10 artifacts under research/<TICKER>/<DATE>/ as the dataset and forward price action as the truth set. Resolves each blueprint to WIN/LOSS/INCONCLUSIVE on a horizon-matched, path-aware ±1R window (using each plan's own invalidation rule), Brier-scores by phase-10 confluence band, and attributes realised hit-rate to the phases and UW tools that fired. Seven phases, each a resumable checkpoint under research/_calibration/<YYYY-MM-DD>/. Frame every judgment from a desk perspective (buy-side PM, sell-side flow trader, market-maker quant). Propose-only — emits patch intentions, never auto-edits phase prompts or rubrics. Invoke when the user asks to calibrate the deep dive, backtest the blueprints, "are our deep-dive calls actually working," win-rate calibration, or types /deep-dive-calibration. Do NOT trigger for a new single-ticker deep dive (use /stock-deep-dive) or a one-off "did X work" (ad-hoc historical_trend).
model: opus
defaults:
  outcome_windows:
    intraday: same-day close vs entry
    "1-5d": 3D-and-10D
    "1-4w": 10D-and-21D
    "1-3m": 30D-and-63D
  min_dataset: 8
  disposition: propose-only
  cadence: on-demand
  win_threshold: ">=+1R in bias direction within window without -1R drawdown first"
  relax_threshold: false
---

# Deep-Dive Calibration

Audit the `stock-deep-dive` skill against its own historical output. Every
`research/<TICKER>/<DATE>/decision.json` (with its `phase-9-trade-plan.md` and
`phase-10-audit.md`) is one prior call; forward price action is the truth set.
The audit asks the only question phase-10 never does: **did the blueprint make
money, and is the confluence score → conviction-bin apparatus actually
predictive?** Without this loop the score is unfalsifiable — you cannot allocate
capital to a "score 85" blueprint you have never verified beats a "score 60" one.

The audit is **propose-only**. It emits patch intentions for the phase prompts
and rubrics — it never edits them. Every recommendation cites the phase and the
data point that justifies it. No vibes.

Ported and adapted from `uw-daily-analysis/.claude/commands/calibration-audit.md`
(the 7-phase outcome → calibration → attribution structure).

## When to invoke

- "Calibrate the deep dive" / "backtest the blueprints" / "are our calls real?"
- "Which phases actually predict?" / "tool tier list for the deep dive"
- Slash command `/deep-dive-calibration`

## When NOT to invoke

- A fresh single-ticker workup → `/stock-deep-dive <TICKER>`
- "Did NVDA work last week?" → ad-hoc `mcp__uw-pp__historical_trend`
- Editing a phase prompt directly (no outcome data needed) → `code-reviewer`

## Operating principle: outcome-driven, not opinion-driven

Every claim traces to a parseable datapoint: a field from a `decision.json`, a
forward-resolved outcome from `historical_trend`, a phase score from
`phase-10-audit.md`. Where data is thin, say so and downgrade the conclusion to
"structural / qualitative" — never silently extrapolate. The persona for every
phase is a composite **elite desk reviewer**: buy-side PM (does this generate
alpha?), sell-side flow trader (does this match how flow trades?), market-maker
quant (do the weights match realised marginal contribution?).

---

## Step 0 — Preflight

1. **Date** — `date +%F` → today's `YYYY-MM-DD`. Output dir:
   `research/_calibration/<YYYY-MM-DD>/`. `mkdir -p` it.
2. **Inventory** — `ls research/*/*/decision.json` (and `decision-v*.json`).
   Count the blueprints. Each (ticker, date) with a `decision.json` is one row;
   for `-vK` re-runs use the highest version.
3. **Threshold check** — default min 8 resolvable blueprints. If below:
   - `relax_threshold=false` (default): **abort** with:
     > "Insufficient calibration history: N=<X> resolvable blueprints. Below the
     > floor of 8. Calibration math is noise-dominated below this. Re-run after
     > more deep dives accumulate, or set `relax_threshold=true` to override
     > (results flagged DATASET-SIZE-RELAXED throughout)."
   - `relax_threshold=true`: proceed with a **DATASET-SIZE-RELAXED** banner on
     every checkpoint and at the top of `SUMMARY.md`.
4. **Resume detection** — if `research/_calibration/<DATE>/phase_<N>_*.md`
   exists, resume from the next phase. Each checkpoint is self-contained.
5. **Available-dates check** — `mcp__uw-pp__historical_available_dates`. Phase 2
   needs forward outcomes; if the latest UW data is < (most recent blueprint
   date + its shortest outcome window), some rows are unresolvable — tag those
   `INCONCLUSIVE(reason=window_not_elapsed)` rather than forcing a verdict.

---

## Phase 1 — Inventory & Parse

**Goal.** Normalize every blueprint into one machine-readable row.

`decision.json` is already structured, so parsing is mostly a read — prefer it
over re-parsing the markdown. For each blueprint capture:

```jsonc
{
  "ticker": "NVDA",
  "date": "2026-05-15",
  "bias": "LONG",                       // LONG|SHORT|NEUTRAL|RANGE
  "horizon": "1-4w",
  "conviction": 0.65,                   // M-01 bin
  "confluence_score": 71,               // from decision.json (phase-10 backfill) or phase-10-audit.md
  "recommended_bin": 0.75,
  "spot_reference": 132.4,
  "primary_entry": 130.5,
  "stop": 126.0,                        // from invalidation.price; else structure max_loss-implied
  "R_pct": null,                        // |entry-stop|/entry, or 0.5*ATR(14) fallback
  "signal_class": "bullish_flow",       // from sizing/citations (the phase-5 backtest class)
  "kelly_p": 0.58,                      // sizing.p (capped win-rate actually used)
  "win_rate_source": "backtest",        // backtest|fallback_bin|null
  "win_rate_n": 14,
  "final_size_pct": 1.85,
  "gates": {"fundamentals":"CONFIRM","correlation_cluster":null,
            "sector_rotation":"aligned","debate_disconfirmed":false},
  "phase_scores": {"1":"+","2":"++","3":"0","4":"+","5":"+",
                   "6":"-","7":"++","7b":"+","8":"+"},   // from phase-10-audit.md scorecard
  "structures": ["call debit spread 132/140 2026-06-19", "..."],
  "decision_valid": true,               // did validate_decision.py pass at write time?
  "blueprint_path": "research/NVDA/2026-05-15/"
}
```

Read `phase-10-audit.md` for the per-phase `++/+/0/-/--` scorecard and the
final confluence_score (if `decision.json.confluence_score` is null, fall back
to the markdown). If a blueprint has no `phase-10-audit.md`, tag
`audit_missing=true` and exclude it from phase/tool attribution (it can still be
outcome-resolved).

### Output
- `phase_1_inventory.md` — desk summary: N blueprints, breakdown by bias /
  horizon / conviction bin / confluence band; data-quality flags (missing
  audits, invalid decision.json, share-class confusion).
- `phase_1_inventory.jsonl` — one row per blueprint.

### Hard rules
- Never invent fields. Missing → `null`.
- One row per (ticker, date); `-vK` → highest version.
- Abort if a non-empty `decision.json` yields zero parseable fields — that's a
  schema/parser bug, surface the path.

---

## Phase 2 — Outcome Resolution

**Goal.** Resolve every row to WIN / LOSS / INCONCLUSIVE on a horizon-matched,
**path-aware** window.

### Horizon → window (frontmatter default; overridable)

| Horizon | Windows (both must agree; disagreement = INCONCLUSIVE unless the longer is decisive) |
|---|---|
| intraday | same-day close vs entry |
| 1-5d  | 3D AND 10D |
| 1-4w  | 10D AND 21D |
| 1-3m  | 30D AND 63D |

### Win threshold (path-aware — restate in checkpoint)

> ≥ +1R move in the **bias direction** within the window **without** a −1R
> drawdown first, where R = the blueprint's defined risk: `|entry − stop|`
> (stop from `invalidation.price`), or the structure `max_loss`-implied move,
> or `0.5 × ATR(14)` at entry when neither is available.

Path matters: a +2R gain that came only after a −1.2R drawdown is a LOSS — the
plan's own invalidation rule would have stopped it out first. For NEUTRAL/RANGE
blueprints, resolve against the defined-risk structure: WIN if spot stayed
inside the structure's profit zone through expiry (or the window end).

### Tool calls (cap: 1 `historical_trend` per row)

`mcp__uw-pp__historical_trend` — `ticker`, `start_date=blueprint_date`,
`lookback_days=longest_window`. Capture intra-window high/low,
drawdown-from-entry, and end-of-window close. Compute realised R-multiple and
max adverse excursion. If the call fails (delisted, no history) or the window
hasn't elapsed → `INCONCLUSIVE` with the reason; **never** tag as LOSS.

### Output
- `phase_2_outcomes.md` — WIN/LOSS/INCONCLUSIVE counts by bias, horizon, and
  confluence band, with the path-aware threshold reprinted verbatim.
- `phase_2_outcomes.jsonl` — Phase 1 rows + `outcome`, `outcome_window`,
  `realised_R`, `max_adverse_excursion_R`, `inconclusive_reason`.

INCONCLUSIVE rows are **excluded from win-rate denominators** downstream.

---

## Phase 3 — Calibration Audit

**Goal.** Is the confidence apparatus predictive? Compare claimed confidence to
realised outcomes.

### Calculations

1. **Confluence-band reliability.** Bucket by phase-10 confluence band
   (0–29 / 30–49 / 50–64 / 65–79 / 80–100). Realised win-rate per band MUST be
   monotone increasing. Flag inversions — a non-monotone score is a
   desk-quitting signal.
2. **Conviction-bin reliability.** Realised win-rate per conviction bin
   (0.55 / 0.65 / 0.75 / 0.85 / 0.95). The bin is a *probability* — bin 0.75
   should win ~75% of resolved calls. Report the gap.
3. **Brier score.** `Brier = (1/N) Σ (conviction − outcome)²`, outcome ∈ {0,1}.
   ≥ 0.25 = no better than coin-flip; ≤ 0.10 = professionally calibrated.
   Compute it **twice** — once using `conviction` and once using `kelly_p` (the
   phase-5 win-rate). **Which is better calibrated?** That answers AUDIT.md's
   open question of whether sizing on the empirical win-rate beats the bin.
4. **Sizing efficiency.** Σ(`final_size_pct` × `realised_R`) — did bigger sizes
   land on the winners? A negative size-weighted R with a positive unweighted R
   means the sizing is anti-predictive.

### Output
- `phase_3_calibration.md` — three reliability tables, two Brier numbers, a
  written verdict in three parts: (a) where the score is honest, (b) where it
  lies to itself, (c) bin/band inversions or HIGH-band overconfidence. Plus the
  explicit `conviction` vs `kelly_p` Brier comparison with a recommendation.
- `phase_3_calibration.jsonl` — per-band and per-bin numerics.

Desk commentary required per flagged divergence, in a sell-side flow trader's
voice — a desk note, not spreadsheet language.

---

## Phase 4 — Phase & Tool Attribution

**Goal.** Which phases and UW tools actually carry the signal?

### Per-phase contribution
For each phase (1, 2, 3, 4, 5, 6, 7, 7b, 8), using the `phase_scores` scorecard:
- `winrate | phase scored ++/+` vs `winrate | phase scored 0/-/--`.
- Marginal contribution = the difference, weighted by N. A phase whose `++`
  calls don't out-perform its `--` calls is decorative confluence.

### Per-tool contribution
For each UW tool family cited across blueprints (`top_premium_trades`,
`dark_pool_block_stratified`, `dex`, `gex`, `signal_backtest`, `sector_flow_persistence`,
`portfolio_correlation`, `insights_*`, …): `winrate_with` − `winrate_without`,
class-conditioned where possible. Use the tool tiers:

| Tier | Criterion | Action implied |
|---|---|---|
| LOAD-BEARING | ≥ +10pp marginal, fires on winners and losers | promote to required citation |
| SUPPORTIVE | +3 to +10pp | keep |
| CONFOUNDED | fires on ≥80% winners, ≤30% losers | demote — likely post-hoc lookup |
| NO-INFO | within ±2pp | deprecate from default citation |
| NEGATIVE | ≤ −5pp | investigate — likely misinterpreted |

### Output
- `phase_4_attribution.md` — phase-contribution table + tool tier list, both
  with market-maker-quant commentary.
- `phase_4_attribution.jsonl` — numerics.

### Hard rules
- Don't score a phase/tool cited < 5 times — mark `INSUFFICIENT_N`, exclude.
- A CONFOUNDED finding needs a manual sanity check before any demote
  recommendation (some tools genuinely fire only on high-conviction setups).

---

## Phase 5 — Gate-Efficacy Audit

**Goal.** Do the four risk gates (the additions from AUDIT.md §2) actually avoid
losers, or do they just shrink size on winners?

For each gate — fundamentals VETO/CAUTION (7b), correlation cluster (6/8),
adverse sector rotation (6), debate disconfirmation (8b):
1. **Cut-set win-rate.** Realised win-rate of blueprints where the gate FIRED
   vs where it did NOT. A gate earns its keep only if `winrate(fired)` <
   `winrate(not_fired)` — i.e. it is cutting genuinely worse trades.
2. **Over-cut check.** If the gate fired on trades that went on to WIN at a
   *higher* rate than the kept set, the gate is destroying alpha — flag it.
3. **Kelly-`p` sourcing efficacy.** Compare realised win-rate of
   `win_rate_source=backtest` rows vs `fallback_bin` rows. Confirms whether the
   empirical-`p` wiring (AUDIT.md §2 item 2) is paying off.

Holdout note: with small N, treat every gate finding as provisional and state
the N explicitly. Never propose loosening a gate on < 5 fired instances.

### Output
- `phase_5_gates.md` — per-gate cut-set table, over-cut flags, backtest-vs-bin
  sourcing comparison, verdict per gate (KEEP / TIGHTEN / LOOSEN / INSUFFICIENT_N).
- `phase_5_gates.jsonl` — numerics.

---

## Phase 6 — Process-Compliance Audit

**Goal.** Did phase-9 actually follow its own rubric on every blueprint?

Per row, mechanical checks:
1. **Kelly-`p` compliance.** Was `kelly_p` the phase-5 win-rate (capped per
   `win_rate_n`), or did it silently use the conviction bin while
   `win_rate_source=backtest` was available? A mismatch is a missed wiring.
2. **N-cap compliance.** Is `kelly_p ≤` the N-conditional cap for its
   `win_rate_n` (0.75 / 0.85 / 0.90)?
3. **Gate-application compliance.** Was every applicable gate evaluated (present
   in the sizing block), or silently skipped? A gate that should have fired
   (per the phase data) but is absent = **missed gate**.
4. **Schema compliance.** `decision_valid == true`? Count invalid envelopes.
5. **Bin-vs-band compliance.** Does `conviction` match the band
   `recommended_bin` from phase-10 (or carry a documented deviation)?

### Output
- `phase_6_compliance.md` — compliance rates, missed-gate ledger (call + the
  condition that should have triggered the gate), schema-failure count. Voice:
  buy-side PM doing a fund post-mortem — clinical, names the phase file.
- `phase_6_compliance.jsonl` — per-row flags.

If the missed-gate rate for any gate exceeds 20%, the phase-9 prompt and its
realised behavior have drifted — name the file to patch in Phase 7.

---

## Phase 7 — Recommendations (propose-only)

**Goal.** Prioritized patch intentions. Every recommendation cites the phase and
the datapoint.

Required deliverables:
1. **Phase-prompt edits** — file path + diff intent (NOT rewrites) for any phase
   flagged by Phase 6 drift or Phase 4 as decorative.
2. **Rubric edits** — `confluence-scoring.md` weight/band changes from Phase 3
   inversions; `sizing-rubric.md` N-cap or gate-threshold changes from Phase 5;
   each with its Phase-3/4/5 marginal-contribution justification.
3. **Tool tier movements** — promote LOAD-BEARING tools to required citations in
   the relevant phase prompt; deprecate NO-INFO; gate CONFOUNDED behind confluence.
4. **Process changes** — e.g. "phase-9 must hard-fail if `win_rate_source=backtest`
   but `kelly_p` ≠ capped win-rate" if Phase 6 shows the wiring is skipped.

Recommendation format — one heading + one paragraph with: **What**, **File**
(`phases/<f>.md` or `rubrics/<f>.md`), **Phase / Data** (`Phase 4: signal_backtest
marginal +14pp, n=11`), **Priority** (P0 calibration-breaking / P1 clear win /
P2 polish), **Risk** (what could go wrong, framed for the desk).

### Output
- `phase_7_recommendations.md` — prioritized list. Voice: chief of staff at a
  multi-strat fund.

### Hard rules
- **Propose-only.** Never `Edit`/`Write` outside `research/_calibration/<DATE>/`.
- Every recommendation cites the phase + datapoint. No vibe-driven items.
- A finding with no data behind it (thin run) → P2 with an explicit
  "low confidence, needs N≥<threshold>" note, not dropped silently.

---

## Step 8 — Executive Summary

Write `research/_calibration/<DATE>/SUMMARY.md` (≤400 words, desk-strategist
voice):

```markdown
# Deep-Dive Calibration — <date>

[DATASET-SIZE-RELAXED banner if applicable]

## Headline calibration
- N resolved: <X> · overall win-rate <Y>% · Brier(conviction) <A> vs Brier(kelly_p) <B>
- Is confluence monotone? <yes/no — band inversions if any>

## Top 3 attribution findings
1. <phase/tool> carries / is decorative. Phase 4 cite.
2. ...
3. ...

## Gate verdict
<one line per gate: KEEP / TIGHTEN / LOOSEN / INSUFFICIENT_N — Phase 5 cite>

## What we'd change before the next deep dive
<one paragraph, JPM-Friday-note voice — the single highest-P&L patch.>
```

---

## Failure modes & recovery

- **Phase 2 rate-limit mid-batch** — checkpoint partial outcomes; resume from the
  last completed ticker. Phase 2 is the only phase that may carry a `_partial` suffix.
- **`historical_available_dates` too stale for a recent blueprint** — resolve what
  has elapsed; tag the rest `INCONCLUSIVE(window_not_elapsed)`; never force LOSS.
- **A `decision.json` fails `validate_decision.py`** — include it in Phase 1 with
  `decision_valid=false`, resolve its outcome if possible, and count it in the
  Phase 6 schema-failure rate.
- **< 5 blueprints in any single signal_class / gate** — flag and exclude from
  per-class stats; never treat single-digit N as signal.

---

## Step 9 — Save and report

1. All seven phase checkpoints written under `research/_calibration/<DATE>/`.
2. `SUMMARY.md` written.
3. Print `SUMMARY.md` to chat. Nothing else — the user opens the folder for the rest.
