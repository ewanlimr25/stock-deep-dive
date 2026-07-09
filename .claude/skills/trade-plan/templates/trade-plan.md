# Trade Plan — {{SYMBOL}}

**As-of date:** {{YYYY-MM-DD}}
**Spot reference:** {{price}} ({{source}})
**Voice:** desk PM running an institutional book
**Built from:** {{deep-dive reused path | "live snapshot"}} + chart engine ({{chart_source}})

> *For research and educational use only. Not financial advice. Sizing,
> structures, targets and dates are illustrative.*

## 0. Information completeness (gap audit)

- **Verdict:** {{SUFFICIENT | USABLE_WITH_GAPS | INSUFFICIENT}} — completeness {{NN}}%
- **Have:** {{flow, dark pool, OI, dealer structure, historical, macro, fundamentals, chart/patterns, events}}
- **Missing / how to source:**
  | Item | Severity | How to source |
  |------|----------|---------------|
  | {{item}} | {{critical/important/nice}} | {{command / feed}} |

## 1. Direction & conviction

- **Bias:** {{LONG / SHORT / NEUTRAL / RANGE}}
- **Conviction (M-01 bin):** {{0.55 | 0.65 | 0.75 | 0.85 | 0.95}}
- **Horizon:** {{intraday / 1-5d / 1-4w / 1-3m / 3-12m}}
- **Confluence score (if scored):** {{0–100}}

### Thesis (≤3 sentences, ≥3 tagged citations)

{{Lead with the why; fuse flow + structure + chart.}}

### Why it should work

- {{tagged reason}}
- {{tagged reason}}

### Why it may fail (the honest other side)

- {{tagged reason}}
- {{tagged reason}}

## 2. Levels to watch

| Level | Role | Source | Note |
|-------|------|--------|------|
| {{$}} | trigger | {{[CHART:swing_high]}} | |
| {{$}} | support | {{[DP:price_levels]}} | |
| {{$}} | resistance | {{[OI:oi_by_strike]}} | |
| {{$}} | gamma flip | {{[STRUCT:gex]}} | |
| {{$}} | pin | {{[STRUCT:max_pain]}} | |

Moving averages: {{sma50 / sma200 / ema21}}. Fib: {{retracement cluster}}.

## 3. Patterns forming (chart)

| Pattern | Direction | Confidence | Measured target | Invalidation | Note |
|---------|-----------|-----------|-----------------|--------------|------|
| {{ascending_triangle}} | {{bullish}} | {{low}} | {{$}} | {{$}} | |
| {{elliott working count}} | {{...}} | {{low}} | {{$}} | {{$}} | rules {{x/3}} |

## 4. Upcoming events that move the tape (next ~30–60d)

| Date | Event | Impact | Source |
|------|-------|--------|--------|
| {{...}} | {{earnings / FOMC / CPI / OPEX}} | {{+/-/?}} | {{[FUND:next_earnings] / [MACRO:event]}} |

## 5. Invalidation

- **Price-based:** {{two daily closes below $X}}
- **Signal-based:** {{DEX/GEX flip, cum-flow against thesis 3 sessions}}
- **Macro-based:** {{FOMC/CPI surprise, regime flip}}

## 6. Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** p_raw = {{phase-5 win-rate}} (n={{N}}, src={{backtest|bin}}) → capped p = {{p}}
- **Inputs:** b = {{payoff}}, fraction = 0.25, cap_pct = 5
- **Raw Kelly:** {{%}} · **Win-rate map ceiling:** {{full/half/starter}}
- **Risk gates (each can only cut):** fundamentals {{..}} · sentiment/crowd {{..}} · correlation {{..}} · rotation {{..}} · debate {{..}} · context {{..}}
- **Final size:** {{%}} of book risk {{(deviation reason if any)}}

## 7. Plan A — pure stock (long/short)

- **Direction:** {{long / short}}
- **Entry:** {{$ / zone}} — trigger: {{...}}
- **Stop:** {{$}}
- **Targets:** T1 {{$}} ({{rationale}}, take {{%}}) · T2 {{$}} ({{rationale}})
- **Reward:risk to T1:** {{R}}
- **Size:** {{% book}}
- **One-liner:** {{...}}

## 8. Plan B — options (≥1 with target date + target price)

### B1 — directional

- **Structure:** {{call/put debit spread / long call}}
- **Strikes / expiry:** {{...}} / {{YYYY-MM-DD}}
- **Target date / target price:** {{YYYY-MM-DD}} / {{$}}
- **Debit/credit · breakeven · max loss:** {{$}} · {{$}} · {{$}}
- **Est. payoff at target:** {{$}}
- **Why this structure:** {{IV percentile + horizon + expected move}}

### B2 — defined-risk alternative

- **Structure:** {{credit spread / iron condor}}
- **Strikes / expiry:** {{...}} / {{YYYY-MM-DD}}
- **Target date / target price:** {{YYYY-MM-DD}} / {{$}}
- **Debit/credit · breakeven · max loss:** {{$}} · {{$}} · {{$}}

## 9. Post-entry monitoring checklist

- [ ] {{re-check DEX/GEX flip on daily refresh}}
- [ ] {{trail stop to breakeven after T1}}
- [ ] {{watch event-risk dates}}
- [ ] {{refresh deep-dive flow if > N days stale}}

## 10. Reasoning-ledger lessons applied

- {{L-XXXX: lesson from a prior marked trade}}

## Citations (≥3, what the eval will spot-check)

1. {{[TAG:source] — value — file §section}}
2. {{...}}
3. {{...}}
