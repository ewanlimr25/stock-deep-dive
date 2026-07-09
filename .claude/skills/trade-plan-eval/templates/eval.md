# Trade-Plan Eval — {{SYMBOL}} (plan {{PLAN_DATE}} → reviewed {{REVIEW_DATE}})

> *For research and educational use only. Not financial advice.*

**Plan:** {{trade-plans/<SYMBOL>/<PLAN_DATE>/trade-plan.md}}
**Trade taken:** {{vehicle}} {{direction}} @ {{entry}} on {{entry_date}} ({{structure}}), size {{%}}

## 1. Outcome (path-aware, ±1R)

- **Status:** {{WIN | LOSS | OPEN | INCONCLUSIVE}}
- **R achieved:** {{R}} · MFE {{mfe_R}}R · MAE {{mae_R}}R
- **First target hit:** {{date or —}} · **Stop hit:** {{date or —}} · **Invalidation price touched:** {{yes/no}}
- (from `mark_to_market.py`)

## 2. Reasoning review (process, not just result)

- **Direction call:** {{RIGHT/WRONG/UNRESOLVED}}
- **Flow↔chart agreement call:** {{RIGHT/WRONG/NA}}
- **Pattern call:** {{PLAYED_OUT/FAILED/UNCONFIRMED/NA}}
- **Level quality:** {{GOOD / STOP_TOO_TIGHT / TARGET_TOO_FAR / …}} (cite MFE/MAE)
- **Sizing review:** {{APPROPRIATE/OVERSIZED/UNDERSIZED}}

| Claim | Side | Verdict | Note |
|-------|------|---------|------|
| {{reason}} | for | {{RIGHT/WRONG}} | |
| {{reason}} | against | {{RIGHT/WRONG}} | |

## 3. Calibration

- Conviction {{bin}} · outcome_bit {{0/1}} · **Brier {{(bin−bit)²}}** · {{WELL_CALIBRATED / OVERCONFIDENT / UNDERCONFIDENT}}

## 4. Attribution — which lanes were decisive

| Lane | Effect | Note |
|------|--------|------|
| {{chart_pattern}} | {{decisive_right/decisive_wrong/minor}} | |
| {{dark_pool}} | {{...}} | |

## 5. Lessons → reasoning ledger

- {{L-####}} ({{CANDIDATE/ACTIVE/RETIRED}}, scope {{tags}}): {{lesson}}

## 6. Proposed rubric edits (propose-only — for the user to accept)

- **{{file}}** — {{old → new}} — {{rationale}}

## 7. One-paragraph takeaway

{{What this trade teaches the next plan on this name/setup.}}
