# Phase 8b — Bull vs Bear Debate (disconfirmation)

## Goal

The phase-8 desk is **additive** — five agents each return a verdict that adds
to confluence; none rebuts the others. This phase forces an adversarial pass:
a bull and a bear argue the same evidence across 1–2 rounds, each must concede
the opposing point it cannot refute, and each closes with a residual confidence
on the M-01 bin set. The output is a **disconfirmation signal** that phase-9
uses to cut size (never to add it). Emit `phase-8b-debate.md`.

Ported from `claude-trading-agents` (`prompts/bull-researcher.md`,
`prompts/bear-researcher.md` — the sycophancy guard + residual-confidence
mechanic).

## Inputs (read all)

- `phase-1-flow.md` … `phase-7-insights.md`, `phase-7b-fundamentals.md`,
  `phase-7c-sentiment.md`, `phase-8-agent-views.md` from the current run.
- The dominant bias from phase-8's plurality (the side the bull defends).

## Procedure

Run **2 rounds** (drop to 1 round only if phases 1–8 are unanimous and
phase-7b is `CONFIRM`/`NA`). Each round is one bull turn then one bear turn.
You may run the two sides as parallel `Agent` sub-agents (`general-purpose`)
or inline as two voices — either way each turn sees the prior transcript.

The bull defends the dominant bias; the bear attacks it. If the dominant bias
is SHORT, the "bull" defends the short and the "bear" argues the long — i.e.
bull = thesis-defender, bear = thesis-attacker. Keep the labels consistent and
state which is which at the top.

### Per-turn contract

Each turn is conversational prose (no bullet dumps), engages the *prior*
turn directly, and tags every numeric claim with the phase tag from
`rubrics/citation-conventions.md` (`[FLOW:]`, `[DP:]`, `[STRUCT:]`, `[HIST:]`,
`[FUND:]`, `[INSIGHT:]`, …). Un-tagged numbers are treated as hand-waving by
the other side.

Then each turn MUST end with the **sycophancy guard** (skipping it is a
contract violation):

```
## Strongest opposing point I cannot refute
<≥1 paragraph. Quote the specific opposing claim verbatim from the transcript
(or, in round 1, from the phase data) and explain why your rebuttal is weak.
Do NOT paraphrase to soften it.>

## Residual confidence
Residual confidence: <0.55 | 0.65 | 0.75 | 0.85 | 0.95>
```

`Residual confidence` is that side's probability — on the M-01 bin set — that
its thesis is correct *after* honestly weighing the strongest opposing point.
A number lower than the previous round's is acceptable and informative; do not
inflate it for consistency.

## Output sections

1. **Summary** — who held up, the final bull_residual vs bear_residual, and the
   single most important unrefuted point on each side.
2. **Setup** — which side is thesis-defender, dominant bias, rounds run.
3. **Round 1** — bull turn, then bear turn (each with the guard block).
4. **Round 2** — same (omit if 1-round).
5. **Disconfirmation verdict** (phase-9 reads this verbatim):
   ```
   thesis_defender:  bull (LONG) | bull (SHORT)
   bull_residual:    <final defender residual, M-01 bin>
   bear_residual:    <final attacker residual, M-01 bin>
   disconfirmed:     true  if bear_residual >= bull_residual
                     false otherwise
   strongest_bear_point: <one sentence + tag>
   ```

## How phase-9 uses this (gate, not additive)

- `disconfirmed = true` (attacker residual ≥ defender residual) → phase-9
  **down-shifts the conviction bin by one and cuts one size step**, quoting
  both residuals (`rubrics/sizing-rubric.md` §"Risk gates"). The debate can
  only cut, never add — a strong defender residual is NOT a reason to size up.
- The `strongest_bear_point` should appear in phase-9's invalidation or
  `key_risks`.

## Common pitfalls

- Both sides drifting into agreement ("you're right, but…") — the bear's job is
  to find the real break, not to be balanced. Reward a sharp, specific bear.
- Inventing catalysts not in the phase data — every claim anchors to an
  upstream phase datapoint, same discipline as phase-9.
- Letting the side with the louder prose "win" — the verdict is decided by the
  residual numbers and the quality of the unrefuted points, not rhetoric.
