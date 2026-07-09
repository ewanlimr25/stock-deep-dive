# Pattern Rubric (Phase A2/A3) — calling chart patterns honestly

`chart_engine.py` proposes patterns from deterministic geometry. This rubric
says how to *report* them: with a confidence the geometry earns, a measured
target, and an explicit invalidation. Patterns are **context, not signals** —
they sharpen entries/targets/stops; they do not by themselves set the bias
(see `direction-rubric.md` Step 2).

## Confidence ladder

| Confidence | When |
|------------|------|
| `high` | textbook geometry **and** volume confirmation **and** flow agrees — only assignable by an explicit manual read, never auto from the engine |
| `medium` | the engine detected it and the structure is clean (clear pivots, matching shoulders/rims) |
| `low` | engine detected with loose tolerances, or pattern still forming / unconfirmed |
| `none` | not present — say so; do not force a pattern onto noise |

The engine emits at most `medium`. Promotion to `high` requires a written,
cited justification (volume + flow + level confluence).

## Per-pattern reporting

For every detected pattern report: **type · direction · confidence · measured
target · invalidation · confirmation trigger**.

- **Flag / pennant** — needs a real pole (≥ ~3 ATR). Target = breakout ± pole
  height. Invalidation = opposite side of the consolidation. Continuation only.
- **Head & shoulders / inverse** — three pivots, head the extreme, shoulders
  within ~5%. Confirms on a *close* through the neckline. Target = head→neckline
  height projected from the break. Invalidation = back through the head.
- **Double top / bottom** — two equal extremes (±3%) with an intervening
  pivot (the neckline). Confirms on a close beyond the neckline; target = depth
  projected. Invalidation = beyond the extreme.
- **Triangles** — ascending (flat highs, rising lows → bullish bias),
  descending (flat lows, falling highs → bearish), symmetrical (neutral, trade
  the break). Always volume-confirm the break; apothem/height as the target.
- **Cup & handle** — rounded base (12–50% deep), matching rims, shallow handle
  near the rim. Bullish continuation on a close above the rim.

## Elliott wave — special handling (low confidence by construction)

The engine's count is a **hypothesis**, never an assertion. Report:

- the interpretation (impulse up/down, wave-5 pending; or corrective ABC),
- the three hard rules and which pass (`rules_passed: x/3`): (1) wave 2 does not
  retrace beyond wave 1's origin, (2) wave 3 is not the shortest impulse leg,
  (3) wave 4 does not overlap wave 1's price territory,
- the wave-5 / next-leg projection as a *target zone*, not a price promise,
- the invalidation (the pivot whose breach kills the count).

Rules of use:
- If `rules_passed < 3`, cap at `low` and label "working count — unconfirmed".
- Never let an Elliott count *override* the flow+structure bias; it may shape
  targets and where to expect exhaustion.
- If the count and the flow agree on direction, say so as a *supporting* point;
  if they conflict, the count yields.

## Fibonacci

- Report the dominant-swing retracement cluster (0.382 / 0.5 / 0.618) and
  extensions (1.272 / 1.618). A retracement level that coincides with a pivot
  cluster or a dealer level is a high-value entry/target — call out the
  confluence explicitly.

## Forbidden

- Reporting a pattern with no measured target and no invalidation.
- Upgrading engine `low`/`medium` to `high` without a cited manual reason.
- Building the entire thesis on a single low-confidence pattern.
