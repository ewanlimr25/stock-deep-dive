# Phase 9 — Trade Blueprint

**Ticker:** {{SYMBOL}}
**As-of date:** {{YYYY-MM-DD}}
**PM voice:** desk PM running an institutional book
**Spot reference:** {{price}} ({{source phase}})
**Upstream phases cited:** phase-1 through phase-8

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

{{Lead with the why. Reference the dominant signal.}}

## Bias + conviction + horizon

- **Directional bias:** {{LONG / SHORT / NEUTRAL / RANGE}}
- **Conviction (M-01 bin):** {{0.55 | 0.65 | 0.75 | 0.85 | 0.95}}
- **Time horizon:** {{intraday / 1-5d / 1-4w / 1-3m}}
- **Why this bin** (one sentence citing phase-10 confluence): {{...}}

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| Primary    | {{$}} | {{e.g. "tag of gamma flip"}} | {{[STRUCT:gamma_flip]}} |
| Aggressive | {{$}} | {{e.g. "intraday VWAP fade"}} | {{...}} |
| Fade       | {{$}} | {{e.g. "rejection at DP wall"}} | {{[DP:price_levels]}} |

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Support | {{$}} | {{[DP:price_levels]}} |
| Resistance | {{$}} | {{[OI:opex_concentration]}} |
| Gamma flip | {{$}} | {{[STRUCT:today_gamma_flip]}} |
| Largest pin | {{$}} | {{[OI:pin_risk]}} |

## Invalidation

- **Price-based:** {{e.g. "two daily closes below $X"}}
- **Signal-based:** {{e.g. "DEX flips positive while spot rallies"}}
- **Macro-based:** {{e.g. "FOMC delivers a hawkish surprise on <date>"}}

## Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** p_raw = {{phase-5 signal_backtest_win_rate}} (n={{win_rate_n}}, source={{backtest|null}}) → capped p = {{min(p_raw, N-cap)}} `[HIST:signal_backtest]`
  - (fallback to conviction bin {{0.55…0.95}} only if win_rate_source=null)
- **Kelly inputs:** b = {{payoff ratio}}, fraction = 0.25, cap_pct = {{5}}
- **Raw Kelly:** {{%}} · **Win-rate map ceiling:** {{full/half/starter}}
- **Risk gates:**
  - Fundamentals (phase-7b): {{CONFIRM/CAUTION/VETO/NA}} → {{effect}}
  - Correlation cluster (phase-6/8): {{none / cluster <name> @ corr X.XX}} → {{effect}}
  - Sector rotation (phase-6): {{aligned / adverse}} → {{effect}}
  - Debate (phase-8b): bull_residual {{0.xx}} vs bear_residual {{0.xx}} → {{effect}}
- **Final size:** {{%}} (capped at {{cap%}} of book risk)
- **Deviation reason (if any):** {{leave blank if none; forbidden if a gate fired}}

## Option structures

### Directional (primary)

- **Structure:** {{e.g. "long call", "call debit spread"}}
- **Strike(s) / expiry:** {{...}}
- **Debit/credit:** {{$}}
- **Breakeven:** {{$}}
- **Max loss:** {{$}}
- **Why this structure:** {{2 sentences referencing IV percentile + horizon}}

### Defined-risk alternative

- **Structure:** {{e.g. "put credit spread", "iron condor"}}
- **Strike(s) / expiry:** {{...}}
- **Debit/credit:** {{$}}
- **Breakeven:** {{$}}
- **Max loss:** {{$}}

## Macro overlay (cite phase-6)

- **Tailwinds:** {{bulleted from phase-6, each with [MACRO:<series>] tag}}
- **Headwinds:** {{...}}
- **Net:** {{net tail / net head / mixed}}

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|------|-------|------------------|
| {{...}} | {{e.g. "earnings", "FOMC"}} | {{+/-/?}} |

## Post-trade monitoring checklist

- [ ] {{e.g. "watch for DEX flip on phase-4 daily refresh"}}
- [ ] {{e.g. "re-check phase-2 dark pool prints daily"}}
- [ ] {{...}}

## Citations summary

Minimum 3 distinct upstream datapoints (M-04 requirement). Listed here for audit:

1. {{[TAG:source] - exact value - phase-N.md §section}}
2. {{...}}
3. {{...}}
