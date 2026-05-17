# Sizing Rubric (Phase 9)

Ported from `claude-trading-agents` (M-03: Kelly with `sizing_deviation_reason`
escape hatch).

## Conviction bins (M-01)

Phase-9 MUST snap conviction to one of:

| Bin   | Meaning |
|-------|---------|
| 0.55  | Slight edge — coin-flip plus a sliver. |
| 0.65  | Moderate edge — more likely than not, with real disconfirming evidence. |
| 0.75  | High edge — standard high-conviction trade after debate. |
| 0.85  | Very high edge — opposition failed to materially dent the thesis. |
| 0.95  | Near-certain — binary catalyst with clean asymmetry. Use sparingly. |

## Kelly formula

```
raw_kelly = (p × b − (1 − p)) / b

p = conviction bin (0.55..0.95)
b = payoff ratio = |target − entry| / |entry − stop|     (long)
                 = |entry − target| / |stop − entry|     (short)

fraction = 0.25                  # fractional Kelly (Thorp/MacLean default)
cap_pct  = 5                     # hard ceiling on book risk
```

Then:
```
suggested_size_pct = min(raw_kelly × fraction × 100, cap_pct)
final_size_pct     = suggested_size_pct           # unless deviation_reason supplied
```

If `raw_kelly < 0` (negative edge), the directional action MUST be either
NEUTRAL or the opposite side. Phase-9 may still publish a defined-risk
structure as an "if I were forced to play" alternative, but mark it clearly.

## Sizing in option structures, not shares

Translate `final_size_pct` to:
- **Long calls / puts:** premium debit ≤ final_size_pct of book risk.
- **Debit spreads:** max-loss ≤ final_size_pct of book risk.
- **Credit spreads:** max-loss (width − credit) ≤ final_size_pct of book risk,
  NOT margin used.
- **Naked short premium:** disallowed at this skill's level — escalate to user.

## Deviation escape hatch

Phase-9 may set `final_size_pct < suggested_size_pct` without explanation
(always allowed to be smaller). Phase-9 may set
`final_size_pct > suggested_size_pct` only if it supplies a
`sizing_deviation_reason` field with one specific, falsifiable justification
(e.g., "phase-10 confluence is 92, hard catalyst on +3d, IV percentile <20").

## Forbidden

- Sizing in dollars (skill has no account context).
- Sizing more than `cap_pct` × any deviation factor > 2.
- Recommending naked short calls on a stock without phase-6 confirmation that
  the risk profile is acceptable.
