# Sizing Rubric (Phase 9)

Ported from `claude-trading-agents` (M-03: Kelly with `sizing_deviation_reason`
escape hatch) and `uw-daily-analysis/signal-confluence-quant` (the win-rate
sizing map + N-conditional cap). This is the **canonical** sizing document for
the three-repo set — `uw-daily` and `claude-trading-agents` should copy it.

## Conviction bins (M-01)

Phase-9 MUST snap conviction to one of:

| Bin   | Meaning |
|-------|---------|
| 0.55  | Slight edge — coin-flip plus a sliver. |
| 0.65  | Moderate edge — more likely than not, with real disconfirming evidence. |
| 0.75  | High edge — standard high-conviction trade after debate. |
| 0.85  | Very high edge — opposition failed to materially dent the thesis. |
| 0.95  | Near-certain — binary catalyst with clean asymmetry. Use sparingly. |

The conviction bin is the **narrative confidence** read off phase-10's
confluence band. It is NOT, by default, the Kelly `p` — see the next section.

## Choosing the Kelly `p` (M-07: empirical win-rate, not the bin)

**Use the realised signal win-rate that phase-5 already fetched as `p`,** not
the conviction bin. Phase 5 runs `historical_signal_backtest` for the firing
signal class and emits `signal_backtest_win_rate`, `win_rate_n`, and
`win_rate_source` in its verdict (see `phases/phase-5-historical.md`). That
empirical edge — the rate at which this exact signal has actually paid off —
is the calibration-trainable input. The conviction bin describes *how sure the
narrative is*; the backtest win-rate describes *how often the tape has been
right*. Kelly sizes on the latter.

### Step 1 — pick the raw win-rate

| `win_rate_source` (from phase-5) | `p_raw` |
|---|---|
| `backtest` (signal had ≥1 historical firing) | the reported `win_rate` |
| `null` / empty / `INSUFFICIENT_N` (no usable history) | fall back to the conviction bin |

### Step 2 — apply the N-conditional cap (uw-daily 2026-05-15 calibration)

Small-N backtests routinely print 100% in a trending tape; cap the *quoted*
`p` by the sample size `win_rate_n`. Show both the raw and capped value.

| `win_rate_n` | Cap on `p` |
|---|---|
| `n < 10`        | 0.75 |
| `10 ≤ n < 20`   | 0.85 |
| `n ≥ 20`        | 0.90 |

`p = min(p_raw, cap)`. If `p_raw` came from the conviction-bin fallback, the
fallback is itself capped at **0.65** (a proxy is never quoted ≥ 0.70).

### Step 3 — win-rate sizing map (sanity gate on the Kelly output)

The Kelly math below produces a number; this map is the independent gate it
must not exceed. Cross-check the two — if they disagree, take the smaller.

| `p` (capped win-rate) | Pre-gate size ceiling |
|---|---|
| `≥ 0.70`       | full (up to `cap_pct`) |
| `0.50 – 0.70`  | half (≤ `cap_pct` / 2) |
| `< 0.50`       | starter / skip |
| `null`         | starter |

**SHORT-side floor.** If `p < 0.50`, the directional size MUST be starter or
skip — never half or full — regardless of what raw Kelly returns. A
negative-edge signal is not a position.

## Kelly formula

```
raw_kelly = (p × b − (1 − p)) / b

p = capped signal-backtest win-rate from phase-5 (Steps 1–2 above);
    conviction bin only when win_rate_source is null/insufficient
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

## Risk gates (apply AFTER raw Kelly, BEFORE final size)

Each gate can only **cut** size (or down-shift the conviction bin); none can
add. Apply them in order and show each in the sizing block. Mirrors
`uw-daily-analysis/risk-monitor`.

1. **Fundamentals veto (phase-7b).** Read the `tier_adjustment` from
   `phase-7b-fundamentals.md`:
   - `CONFIRM` / `NA` → no-op.
   - `CAUTION` → cut one size step (full→half, half→starter).
   - `VETO` → directional size is **watch-only / 0%**, regardless of Kelly.
     A `VETO` means the flow contradicts the underlying on ≥2 of
     {earnings_trend, insider MSPR, growth/margins} — treat the bullish flow
     as smart-money distribution, not a tradeable long. You may still publish
     a defined-risk structure marked "fundamentals-vetoed, carry only".
2. **Correlation cluster gate (phase-6 / phase-8 `risk_portfolio_correlation`).**
   If this name is pairwise-correlated ≥ 0.70 with another open research blueprint
   (same `research/<other>/<date>/`), cut one size step and name the cluster.
   `0.60–0.70` is a soft-watch — surface it, do not cut.
3. **Adverse sector-rotation gate (phase-6 `options_flow_sector_flow_persistence`).**
   If smart money is persistently rotating *out* of this name's sector against
   the trade direction, cut half a size step.
4. **Debate-disconfirmation gate (phase-8b).** If the bear's residual
   confidence ≥ the bull's residual confidence, the disconfirmation step did
   NOT clear the trade: down-shift the conviction bin by one and cut one size
   step. Quote both residuals. The debate can only cut, never add.

## Deviation escape hatch

Phase-9 may set `final_size_pct < suggested_size_pct` without explanation
(always allowed to be smaller). Phase-9 may set
`final_size_pct > suggested_size_pct` only if it supplies a
`sizing_deviation_reason` field with one specific, falsifiable justification
(e.g., "phase-10 confluence is 92, hard catalyst on +3d, IV percentile <20").
A deviation upward is forbidden when any gate above fired.

## Forbidden

- Sizing in dollars (skill has no account context).
- Sizing more than `cap_pct` × any deviation factor > 2.
- Recommending naked short calls on a stock without phase-6 confirmation that
  the risk profile is acceptable.
