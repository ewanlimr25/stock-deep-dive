# Confluence Scoring (Phase 10)

Ported from `claude-trading-agents` (M-02 Risk Judge rubric) and adapted for a
single-ticker, signal-aggregation context. Output is a 0–100 confluence score
with directional sign and a per-phase contradiction log.

## Scoring axes

Score each of the seven phases (1–7) as one of:

| Symbol | Meaning | Points |
|--------|---------|--------|
| `++` | Strongly agrees with the dominant bias (large effect, high conviction) | +15 |
| `+`  | Mildly agrees | +7 |
| `0`  | Neutral / not enough data | 0 |
| `-`  | Mildly contradicts | -7 |
| `--` | Strongly contradicts | -15 |

Plus phase-8 (multi-agent desk):
- Each of the 5 sub-agents contributes ±2 based on whether its verdict aligns
  with the dominant bias.

**Score range:** -115 to +115. Normalize to 0–100 via:

```
confluence_score = round( (raw_score + 115) / 230 * 100 )
```

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
