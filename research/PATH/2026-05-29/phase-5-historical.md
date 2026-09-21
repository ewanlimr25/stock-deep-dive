# Phase 5 — Historical Context & VRP

**Ticker:** PATH · **As-of:** 2026-05-29 · **Generated:** 2026-05-29
**Upstream:** phase-4-structure.md (long-gamma, $12 cap) · phase-1-flow.md
(faint-bullish, conviction 2/5) · phase-0.5-context.md (BUSY_NAME_NORMAL_DAY)

> **Gap-aware caveat (MANDATORY):** the local window is non-contiguous — a
> 21-session hole (2026-03-28→04-24). Every "30-day"/"90-day" read below spans
> **~34 sessions actually present**, not the calendar span. Trailing tools
> (`iv-percentile-zscore`, `pc-ratio-zscore`, `cumulative-premium-flow`,
> `signal-backtest`) anchor to the latest available date (2026-05-29) — fine
> here since as-of == latest.

## Summary

History deflates the bullish lean rather than confirming it. **IV is cheap by
PATH's own 1-yr standard** — IV30d 64.6% sits at the **8.8th percentile**
(z −1.30, regime LOW_IV) — so optionality is *cheap to own*; but **VRP is
positive** (+15.8 vol pts, IV30 > realized) so carry favours *selling* premium.
The decisive read is the **bullish_flow signal backtest: 50.0% win rate over
n=8** — a coin flip, **no historical edge**, and `dark_pool_accumulation`
returned **no backtest results at all (n=0)**. Over the ~34-session window
cumulative premium flow is **balanced** (bullish $64.8M vs bearish $65.8M — net
*slightly bearish*), there is **no stealth institutional build**, and today's
call-heavy P/C (0.35) is **only −0.26σ from its 20-day mean — not an extreme,
just PATH's normal call-tilt**. Price is in a real recovery (RSI 63.5, +9–10%
above its 20/50-day SMAs) but still **−9.8% below the 200-day and −28% YTD** —
extended short-term, structurally downtrending. Net: today's signals are
**historically edge-neutral at best**; the only genuine tailwind is cheap IV.

## Key signals

- **bullish_flow win rate 50.0%, n=8** `[HIST:signal-backtest]` — no edge; this
  is the Kelly `p` and it is a coin flip on a tiny sample. **Caps sizing.**
- **`dark_pool_accumulation` backtest n=0 (no results)** `[HIST:signal-backtest]`
  — phase-2's signal class has no measurable historical edge for this name.
- **IV at 8.8th percentile / LOW_IV** (z −1.30) `[HIST:iv-percentile-zscore]` —
  cheap optionality; favours *owning* premium / debit structures.
- **VRP +15.8 pts, "favour premium selling"** `[HIST:vrp]` (RV30 48.8%) — carry
  tension with the cheap IV percentile → resolves to **spreads** (own cheap IV,
  sell some against the $12 gamma cap).
- **90d premium flow balanced** — bullish $64.8M vs bearish $65.8M
  `[HIST:cumulative-premium-flow]`; **no stealth build** behind today's tape.

## Detailed findings

### IV regime
IV30d **64.6%**, **8.8th percentile** (252d), z **−1.30**, regime **LOW_IV**
(dates_used 34). Absolutely high but historically cheap for PATH → directional
debit structures are not paying up for vol.

### VRP
IV30 > RV30 (RV30 **48.8%**); VRP **+15.8** vol pts → *"options pricing more vol
than realised — favour premium selling."* Tension with low IV percentile;
spread structures reconcile both.

### P/C ratio z-score
Today PCR **0.346**, z **−0.257** over 20d → **not a sentiment extreme**.
Daily PCR has run 0.19–0.43 most sessions (call-tilt is PATH's baseline), with
occasional spikes (5/19 = 1.14). Confirms phase-0.5 BUSY_NAME_NORMAL_DAY.

### GEX time series
`gex-time-series` did not populate regime-flip fields (tool returned only the
descriptive note). No multi-day regime-flip history available; phase-4's
single-day positive-GEX read stands un-cross-checked over time. **Data gap noted
in Tool errors.**

### OI trend
`oi-trend` returned null summary fields (no per-date series populated). Not
usable; defer to phase-3's single-day OI build.

### Multi-day trend (~34 sessions, 2026-03-20→05-29, spans the gap)
- **13 bullish days vs 17 bearish days** → net slightly bearish-tilted window.
- Price **$12.06 → $11.72** (−2.8% over window; recovering hard in the last ~2
  weeks per fz Perf Week +10.9%).
- IV rank **44.2 → 43.3** (flat). `flow_direction_latest`: bullish.

### Price context (`fz`, advisory)
- **RSI(14) 63.5** `[HIST:rsi fz]` — strong, not yet overbought (<70).
- **+9.8% above SMA20, +9.4% above SMA50** — extended short-term; chasing here
  carries mean-reversion risk into the phase-4 $12 cap.
- **−9.8% below SMA200** `[HIST:52w_proximity fz]` — still in a longer-term
  downtrend, approaching the 200-day from below (classic resistance zone, near
  the $12–$13 gamma wall).
- **Perf YTD −28.5%**, **−40.9% from 52w high ($19.84)**, **+27.4% off 52w low
  ($9.20)** — beaten-down recovery name, not a breakout leader.

### Signal backtest
| Signal | Win rate | N | Read |
|---|---|---|---|
| bullish_flow | **50.0%** | 8 | coin flip — no edge |
| dark_pool_accumulation | null | 0 | no results |

## Tool calls
| Tool | Args | Result |
|---|---|---|
| `historical iv-percentile-zscore` | `--lookback-days 252` | 8.8 pctile, LOW_IV |
| `historical vrp` | `--realised-window-days 30` | +15.8, sell-premium |
| `historical cumulative-premium-flow` | `--days 90` | balanced (slightly bearish) |
| `historical pc-ratio-zscore` | `--lookback-days 20` | z −0.26 (not extreme) |
| `historical trend` | `--days 30` | 13 bull / 17 bear days |
| `historical gex-time-series` | `--days 30 --dte-max 45` | regime fields null |
| `historical oi-trend` | `--days 30` | summary fields null |
| `historical signal-backtest` | `bullish_flow` / `dark_pool_accumulation` | 50% n=8 / n=0 |
| `fz quote` | `--agent` | RSI 63.5, +9-10% vs 20/50 SMA, −9.8% vs 200 |

## Tool errors
- `historical gex-time-series` returned only the descriptive `note` with null
  regime-flip / series fields — multi-day GEX regime stability **not verifiable**;
  treat phase-4's positive-GEX as a single-day reading.
- `historical oi-trend` returned null summary/series — OI buildup-over-time
  **not verifiable**; rely on phase-3 single-day OI.

## Verdict for downstream

- **Volatility regime: CHEAP (own premium) but positive carry (sell premium)** →
  the reconciling structure is a **debit spread** (long cheap IV, short the $12
  gamma-wall strike to fund and respect the cap). Not a naked long-vol or
  short-vol regime.
- **Premium environment:** balanced over 90d, no stealth directional build.
- **Conviction that today's signal is HISTORICALLY EDGE-POSITIVE: 1.5 / 5** —
  bullish_flow 50% win rate (n=8) is *not* edge-positive; the dark-pool signal
  has no backtest. The setup leans on cheap IV and structure, not on a proven
  flow edge.
- **Three datapoints:** IV percentile **8.8** · VRP **+15.8** · signal win rate
  **0.50 (n=8)**.
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:               bullish_flow
  signal_backtest_win_rate:   0.50
  win_rate_n:                 8
  win_rate_source:            backtest
  ```
  Kelly `p` = 0.50 on n=8 → apply the small-N cap (`rubrics/sizing-rubric.md`).
  An edge of 0.50 implies **near-zero Kelly fraction** → starter size at most.
- **Open questions:**
  - With no historical flow edge and price extended above short-term MAs into a
    $12 gamma cap, is the only attractive expression a *defined-risk* upside bet
    (debit call spread) rather than long stock? Carry to phase-9.
  - Does the 31% short float (phase-7c) provide a *non-flow* edge (squeeze) that
    the flow backtest can't capture?
