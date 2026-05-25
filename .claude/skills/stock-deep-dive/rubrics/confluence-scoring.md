# Confluence Scoring (Phase 10)

Ported from `claude-trading-agents` (M-02 Risk Judge rubric) and adapted for a
single-ticker, signal-aggregation context. Output is a 0–100 confluence score
with directional sign and a per-phase contradiction log.

## Scoring axes

Score each of the eight signal phases (1, 2, 3, 4, 5, 6, 7, 7b) as one of:

| Symbol | Meaning | Points |
|--------|---------|--------|
| `++` | Strongly agrees with the dominant bias (large effect, high conviction) | +15 |
| `+`  | Mildly agrees | +7 |
| `0`  | Neutral / not enough data | 0 |
| `-`  | Mildly contradicts | -7 |
| `--` | Strongly contradicts | -15 |

Phase-7b (fundamentals) scores on the same scale, with one hard rule: a
`tier_adjustment = VETO` is at most `--` and the audit MUST note that the
directional thesis is fundamentally vetoed. `NA` (no data / ETF) scores `0`.

**Context modifier (phase-0.5).** When phase-0.5 `unusual_verdict =
BUSY_NAME_NORMAL_DAY`, the flow phases (1 and 2) are capped at `+` (cannot score
`++`): "big flow on a name that always has big flow" is weak confluence. `QUIET`
caps phases 1–2 at `0`. `GENUINELY_UNUSUAL` applies no cap. Phase-7c is **not** a
scored axis — it enters as a one-sided penalty (below), like phase-8b.

Plus phase-8 (multi-agent desk):
- Each of the 5 sub-agents contributes ±2 based on whether its verdict aligns
  with the dominant bias.

**Symmetric raw range:** the eight phases (±15 each = ±120) plus phase-8
(±10) give a raw range of **−130 to +130**. Normalize to 0–100 via:

```
base_score = round( (raw_score + 130) / 260 * 100 )
```

Then apply the **one-sided gate penalties** AFTER normalization (cuts only, so
they can never inflate the score and keep 50 = perfectly mixed):

```
confluence_score = base_score
                 − (5  if phase-8b disconfirmed else 0)      # debate
                 − (5  if phase-7c tier_adjustment == CAUTION else 0)  # sentiment
                 − (10 if phase-7c tier_adjustment == VETO    else 0)  # sentiment veto
```

`disconfirmed = true` (phase-8b) means the bear's residual ≥ the bull's residual —
the adversarial pass did not clear the trade. The **phase-7c** penalty fires when
the crowd/positioning read contradicts the thesis (CAUTION) or hard-vetoes it
(VETO — crowded-the-same-way + squeeze/borrow mismatch). All three are one-sided:
confirming sentiment or a strong defender residual is **not** allowed to add
confluence (filters never amplify). `NA`/`CONFIRM` subtract nothing.

A score of **50** means perfectly mixed signals. **>70** indicates strong
positive confluence; **<30** indicates strong negative confluence (the
dominant bias is being fought by the data).

## Confidence interpretation

| Score band | Phase-9 conviction bin should be |
|------------|----------------------------------|
| 0–29       | 0.55 (slight) — or revisit dominant bias entirely |
| 30–49      | 0.55–0.65 |
| 50–64      | 0.65 |
| 65–79      | 0.75 |
| 80–89      | 0.85 |
| 90–100     | 0.95 — only when binary catalyst + clean asymmetry |

## Contradiction log

For every phase scored `-` or `--`, write a one-line entry under phase-10's
`## Contradictions` section in the form:

```
- phase-N (<topic>): <one-sentence summary of the conflict> — <suggested resolution>
```

Suggested resolutions:
- **Downgrade conviction** to the next-lower bin
- **Tighten invalidation** so the trade exits earlier on the contradiction firing
- **Wait for confirmation** — note the specific datapoint that would resolve
  the conflict

## Forbidden moves

- Do NOT silently raise the confluence score by ignoring contradictions.
- Do NOT recompute upstream phases to make them agree.
- Do NOT skip phase-10 because phases 1–9 all agreed — write the audit anyway
  with the agreement noted.
