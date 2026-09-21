# Phase 6 — Macro Overlay

**Ticker:** NVDA
**As-of date:** 2026-05-27
**Generated:** 2026-05-28T02:45:00Z
**Upstream phases cited:** phase-0.5-context.md, phase-1-flow.md, phase-3-positioning.md, phase-5-historical.md

## Summary

Macro is a **net mild headwind** for the NVDA setup, not a hammer. The UW market
regime is **"TRANSITIONAL — reduce position size, defined-risk strategies"** with
SPY in a structural uptrend (+4.93% 30d, above SMA20/50, only −0.22% from 90d
high) but only **37.1% bullish breadth** internally — narrow leadership, broad
weakness. Most importantly for NVDA: **Technology was today's largest sector
directional outflow at −$433.5M** in the regime tool's screener-based read,
contradicting the gross call-premium-heavy sector-flow tool that shows Tech with
$8.5B "INFLOW" (this is calls-minus-puts, *not* net directional — the same trap
the single-name flow exhibited). NVDA is **0.93 correlated to SMH** and 0.90+ to
AMD/AVGO/MRVL/TSM over 32 sessions — a pure semi-complex beta. FRED prints a
mid-cycle regime: **CPI +3.78% YoY, Core CPI +2.74%, Fed funds 3.62%, 10y 4.50%,
2s10s +0.49% (un-inverted), UNRATE 4.3%** — Fed has cut from the prior peak,
curve is normal, no recession signal, but inflation is still above target so
Fed has limited room to cut further. Long-duration growth (Tech) gets a
structural rate tailwind but a near-term sector-flow headwind. Verdict:
**adverse sector rotation, neutral-to-mild macro.**

## Key signals

- **UW market regime: TRANSITIONAL — guidance "Half position sizes. Favor
  defined-risk."** [MACRO:MarketRegime_2026-05-27 UW].
- **SPY +4.93% 30d, above SMA20/50, only −0.22% from 90d high; breadth 37.1%
  bullish** [MACRO:MarketRegime_2026-05-27 UW] — uptrend with weak internals.
- **Technology sector −$433.5M directional outflow today (largest of any
  sector)** [MACRO:sector_rotation_2026-05-27 UW] — adverse for NVDA.
- **CPI 3.78% YoY Apr / Core CPI 2.74% YoY Apr; Fed funds 3.62%, 10y 4.50%,
  2s10s +0.49%** [MACRO:CPIAUCSL_2026-04 FRED] [MACRO:DGS10_2026-05-26 FRED] —
  mid-cycle, curve normal, no rate-cycle break.
- **NVDA / SMH 30d correlation = 0.93** [MACRO:correlation DUCKDB] — pure
  semi-complex beta; bench- ed against today's semi-complex selloff.

## Detailed findings

### Market regime — [MACRO:MarketRegime_2026-05-27 UW]

| Field | Value |
|-------|------:|
| regime | **TRANSITIONAL — Mixed signals, reduce position size, wait for clarity** |
| trading_guidance | "Half position sizes. Favor defined-risk strategies. Iron condors in range." |
| trend | UPTREND |
| SPY current | $750.46; +4.93% 30d; above SMA20 ($735.29) + SMA50 ($700.07); −0.22% from 90d high |
| breadth | bullish 2,291 vs bearish 3,881 (37.1% bullish) |
| money flowing in | Comm Services +$84M, Consumer Cyclical +$49M, Financial Services +$35M |
| **money flowing out** | **Technology −$433.5M (largest)**, Healthcare −$15M, Cons Defensive −$7M |

### Inflation (FRED) — [MACRO:CPIAUCSL_2026-04 FRED, CPILFESL_2026-04 FRED]

| Series | Latest (Apr-2026) | Prior (Mar-2026) | YoY (Apr-25→Apr-26) |
|--------|------------------:|-----------------:|--------------------:|
| CPI (CPIAUCSL) | 332.407 | 330.293 | **+3.78%** |
| Core CPI (CPILFESL) | 335.423 | 334.165 | **+2.74%** |
| PCE (PCEPI, Mar) | 130.344 | 129.484 | — |
| Core PCE (PCEPILFE, Mar) | 129.279 | 128.901 | — |

Headline still ~1.8pp above 2% target; core within shouting distance. Inflation
is normalizing but not done.

### Labor — [MACRO:PAYEMS_2026-04 FRED, UNRATE_2026-04 FRED]

| Series | Latest (Apr-2026) | Δ MoM |
|--------|------------------:|-------|
| Nonfarm payrolls (PAYEMS) | 158,736k | +115k vs Mar (+185k Mar→prior) |
| Unemployment rate (UNRATE) | 4.3% | flat |

Soft-but-positive labor — consistent with the "no recession, mild slowing"
regime read.

### Rates (FRED) — [MACRO:DFF_2026-05-26 FRED, DGS10_2026-05-26 FRED]

| Series | Latest |
|--------|-------:|
| Fed funds (DFF) | 3.62% |
| 2y Treasury (DGS2) | 4.01% |
| 10y Treasury (DGS10) | 4.50% |
| 10y − 2y spread (T10Y2Y) | **+0.49% (un-inverted)** |
| SOFR | 3.63% |
| Broad USD index (DTWEXBGS) | 119.29 (2026-05-22) |

Curve is normal, real rates moderate. Fed has cut materially from the prior cycle
peak (5.25–5.50%). Lower rates structurally support long-duration growth/Tech
multiples but are not actively easing further given sticky 3.78% CPI.

### Activity / Consumer

WebSearch fallback **skipped this run** — as-of 2026-05-27 is forward of the
operator's reliable web index for this session, and the FRED+UW picture is
sufficient for the single-ticker macro overlay. Flag for the next calibration
pass.

### Sector rotation — [MACRO:sector_flow_2026-05-27 UW, sector_flow_persistence UW]

**Two reads of "Tech sector flow" — they disagree:**

| Tool | Tech sector | Interpretation |
|------|-------------|----------------|
| `uw risk market-regime` `.sector_rotation.money_flowing_out` | **−$433.5M (largest outflow)** | screener bullish−bearish premium (directional) |
| `uw options-flow sector-flow` `.net_flow` | +$8.50B (calls $13.95B vs puts $5.45B) | call-premium minus put-premium (gross) |
| `uw options-flow sector-flow-persistence --days 5` | INFLOW, score 1 | persistent gross-call dominance |

The same trap as NVDA's single-name flow (phase-1): **gross calls > puts does
not equal *buying* calls** — the persistent Tech sector-flow "INFLOW" reflects
high call-volume mechanics, while the bullish-bearish directional read shows
the **biggest sector OUTFLOW** today. The directional read agrees with phase-1
and phase-0.5's semi-complex bearish ranking.

**`fz` breadth cross-check (advisory)** — sector-wide breadth pct_green 46.92%
(advancers 236 / decliners 263 / unchanged 4); Technology group Change −0.42%
today [MACRO:sector_breadth fz EOD] [MACRO:group_valuation fz EOD]. Tech is
red on breadth too — consistent with the directional outflow, not the
gross-call inflow. Tech P/E 39.39, Fwd P/E 28.21, PEG 1.18 — premium valuation
but not bubble.

### Cross-name correlation — [MACRO:correlation DUCKDB]

`uw risk portfolio-correlation` flagged "Unknown" sectors and no
high_correlations (known issue, see memory `data-source-workarounds`). Computed
locally from the screener parquet close series over 32 available sessions:

```
ticker   AMD   ARM  AVGO  MRVL    MU  NVDA   SMH  SNDK   TSM
NVDA    0.91  0.81  0.91  0.90  0.79  1.00  0.93  0.83  0.92
```

**Only NVDA has a blueprint for 2026-05-27** (no concurrent positions to
correlate against). For the next deep dive added on this date, anything from
{SMH, AMD, AVGO, MRVL, TSM, ARM, SNDK, MU} would trigger a **CLUSTER (≥0.70)**
gate per the macro rubric; phase-9 sizing would have to cut size.

## Tailwind / Headwind table

| Datapoint | Latest value | Release date | Source | Impact on NVDA / Semis |
|-----------|--------------|--------------|--------|------------------------|
| CPI YoY | +3.78% | Apr-2026 | FRED | mild headwind (sticky → Fed pause) |
| Core CPI YoY | +2.74% | Apr-2026 | FRED | neutral (normalizing) |
| Fed funds | 3.62% | 2026-05-26 | FRED | tailwind structurally (cut from 5.25%+) |
| 10y yield | 4.50% | 2026-05-26 | FRED | mild headwind (still elevated) |
| 2s10s | +0.49% | 2026-05-26 | FRED | tailwind (curve normal, no recession) |
| UNRATE | 4.3% | Apr-2026 | FRED | neutral |
| Payrolls | +115k | Apr-2026 | FRED | neutral (soft-positive) |
| SPY trend | +4.93% 30d | 2026-05-27 | UW | tailwind |
| Breadth bullish | 37.1% | 2026-05-27 | UW | **headwind** (narrow leadership) |
| Sector rotation | Tech −$433.5M (largest outflow) | 2026-05-27 | UW | **headwind (adverse)** |
| Sector breadth | Tech −0.42%, mkt pct_green 46.9% | 2026-05-28 EOD | `fz` | mild headwind |

## Catalyst calendar (next 30d)

Front-expiry implied move (from phase-0.5): **±1.94% / $4.12** [CTX:implied_move].
Each binary below should be read against this band.

| Date | Event | Likely impact | vs ±1.94% expected move |
|------|-------|---------------|-------------------------|
| ~2026-06-11 | May CPI release (typical) | Tech-multiple sensitive | could exceed if surprise |
| ~2026-06-17 | FOMC meeting (typical mid-June) | Rate path + dot plot | typically inside on rate-pause day |
| ~2026-06-06 | May Nonfarm Payrolls (typical 1st-Fri) | broad market | typically inside |
| 2026-08-26 | **NVDA earnings (next)** | Massive — outside 30d window | binary; not in this scope |

No NVDA-specific catalyst in the 30-day window. The trade has to stand on flow
+ structure + macro — no event lift expected. WebSearch confirmation of exact
release dates skipped (forward-of-cutoff caveat).

## Tool / source errors

- `uw risk portfolio-correlation` returned `sector=Unknown` for both NVDA and
  LRCX with no `high_correlations` — known issue (see memory
  `data-source-workarounds`). Worked around with local DuckDB compute on the
  screener parquet close series (32 sessions).
- WebSearch for FOMC / ISM / consumer skipped (as-of 2026-05-27 is at/beyond the
  operator's session web index reliability; FRED + UW sufficient for the macro
  overlay this run).

## Verdict for downstream

- **Net macro bias for NVDA:** **mild HEADWIND** (Tech sector rotation adverse;
  breadth narrow; rates still elevated; nothing actively bullish for semis).
- **Conviction:** **3/5** (regime + FRED prints are mid-cycle; sector rotation
  is *today's* read and could mean-revert by Friday).
- **Top 2 datapoints phase-9 must cite in macro overlay:**
  1. UW market regime **TRANSITIONAL** + breadth 37.1% bullish (guidance:
     half size, defined-risk).
  2. Tech sector −$433.5M directional outflow today (NVDA correlation to SMH
     0.93 means the name *is* this sector).
- **Top 2 catalysts phase-9 must put in the calendar:**
  1. May CPI release (~2026-06-11) — directly tests the "Fed pause vs cut" lean.
  2. FOMC meeting (~2026-06-17) — first dot plot since last cut.
- **Sector-rotation verdict:** **ADVERSE** for any bullish NVDA thesis;
  **ALIGNED** for a bearish thesis (5/5 sector-flow persistence on the gross
  call-heavy metric is misleading — the directional read is bearish).
  Persistence: today's directional outflow is a single-day snapshot; the
  5-session persistence tool only measures the gross-call metric (known
  definitional mismatch — note in audit).
- **Correlation verdict:** **No concurrent positions** for 2026-05-27 (only
  NVDA blueprint for the date). If any of {SMH/AMD/AVGO/MRVL/TSM/ARM/SNDK/MU}
  is added on this date, that pair is a **CLUSTER (≥0.79)** and phase-9
  sizing must cut.
