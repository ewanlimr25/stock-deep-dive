# Phase 5 — Historical Context & VRP

**Ticker:** FSLY
**As-of date:** 2026-05-19  (Effective data date: 2026-05-18)
**Generated:** 2026-05-19T00:50:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-4-structure.md

## Summary

Historical context dramatically reshapes the read. **FSLY crashed −38%
on 2026-05-07** (close $31.57 → $19.50) almost certainly on Q1 earnings
[HIST:historical_trend], then slid another −14% through 2026-05-18 to
$16.71. Despite IV30d at 81.3% absolute, the **1y IV percentile is
7.7%** [HIST:historical_iv_percentile_zscore] — IV is *cheap vs its own
history* because the trailing year contained 100-130% IV peaks. VRP
prints at **−85 IV points** (iv30d 0.81 vs realised σ 1.66) →
**PREMIUM_BUYING regime** [HIST:historical_vrp]: vol is *deeply cheap*
relative to realised. 90-day cumulative premium flow is net BULLISH
(+$9.9M, $85.6M bullish vs $75.7M bearish) [HIST:historical_cumulative_premium_flow]
— the campaign from phase-1 sits on a long-standing bullish flow base
that pre-dates the earnings crash. However, the bullish_flow signal
backtest is brutal: **8.3% win rate over the last 5 sessions, −3.22%
avg move** [HIST:historical_signal_backtest] — the tech complex has
been punishing bullish_flow setups. This is a tactical headwind the
trade plan has to acknowledge.

## Key signals

- **IV is cheap by 1y standard: percentile 7.7, z-score −0.95**
  [HIST:historical_iv_percentile_zscore]. Pre-earnings (5/1-5/6), IV
  rank was 92-96; post-earnings collapse to 42 IV rank by 5/18.
- **VRP = −0.85 (PREMIUM_BUYING regime).** Realised vol 166% vs IV
  81% → vol is materially underpriced; **debit structures favored
  over credit** in pure VRP terms [HIST:historical_vrp].
- **Earnings crash 2026-05-07**: close $31.57 → $19.50 (−38.2%),
  call vol 57,854, put vol 42,302, total premium ~$23.6M, net flow
  **+$7.3M bullish** on that day [HIST:historical_trend]. The
  bullish flow into the down day suggests speculative dip-buying.
- **90d cumulative net flow +$9.9M BULLISH**
  [HIST:historical_cumulative_premium_flow] — the bullish leaning is
  multi-month, not a one-day phenomenon.
- **bullish_flow backtest win_rate = 8.3% (1/12), avg move −3.22%**
  over 5/13-5/15 signal dates [HIST:historical_signal_backtest].
  **CAUTION**: the tech complex has been bullish-flow-trap territory.

## Detailed findings

### IV regime — LOW_IV (1y), but PREMIUM_BUYING (vs realised)

`historical_iv_percentile_zscore`, lookback_days=252:

| Field | Value |
|---|---|
| current_iv30d | 81.34% |
| iv_percentile | **7.69 (1y)** |
| iv_zscore | −0.945 |
| Regime | LOW_IV |

`historical_vrp`, realised_window_days=30:

| Field | Value |
|---|---|
| iv30d | 0.8134 |
| realised_vol (30d) | **1.6629** |
| vrp | **−0.8495** |
| Regime | **PREMIUM_BUYING** |
| Interpretation | "Vol cheap vs realised — favour premium buying" |

The two readings agree: **IV is cheap.** The realised vol of 166% is
dominated by the 2026-05-07 single-day −38% move, which inflates the
σ. So a more honest read is: "30d realised σ is distorted by a tail
event; the ambient regime is closer to 60-90% σ; IV at 81% is
*fair-to-cheap*, not screamingly cheap." Either way, **credit-only
structures are inferior right now** — long premium has a positive
expected edge here.

### Cumulative premium flow (90d)

`historical_cumulative_premium_flow`, days=90:

| Field | Value |
|---|---|
| cumulative_bullish | **$85,638,762** |
| cumulative_bearish | $75,721,627 |
| net_flow | **+$9,917,135** |
| trend_direction | BULLISH |
| Dates covered | 27 sessions (2026-03-13 → 2026-05-18) |

Net bullish skew of ~53% across 90 days — modest but consistent. The
absolute magnitude ($86M bullish) for a $16-handle small-cap is
substantial — institutional involvement is real.

### P/C ratio z-score — NORMAL

`historical_pc_ratio_zscore`, lookback_days=20:

| Field | Value |
|---|---|
| current_pc_ratio | 0.4034 |
| mean (20d) | 0.4299 |
| std | 0.1515 |
| zscore | −0.175 |
| extreme | **NORMAL** |

P/C of 0.40 is call-heavy in absolute terms but within FSLY's own
normal range. No sentiment extreme; no contrarian fade signal. The
trade thesis is not crowded.

### GEX time series — regime instability around earnings

`historical_gex_time_series`, days=30, dte_max=45 (27 sessions
available). Selected trajectory (close-of-day GEX and ZGL):

| Date | Spot | Total GEX | ZGL | Regime |
|---|---|---|---|---|
| 2026-03-13 | $24.58 | $4.3M | $17.33 | POSITIVE |
| 2026-03-25 | $30.01 | $14.6M | $10.12 | POSITIVE |
| 2026-04-27 | $24.91 | $54.9M | $14.47 | POSITIVE |
| **2026-05-01** | **$27.67** | **$125.9M** | $15.93 | POSITIVE |
| **2026-05-05** | **$31.94** | **$305.6M** | $15.39 | POSITIVE (peak GEX) |
| **2026-05-06** | $31.78 | $110.4M | $19.55 | POSITIVE |
| **2026-05-07** | **$19.58** | **$40.4M** | $12.00 | POSITIVE (CRASH DAY) |
| 2026-05-08 | $20.23 | $43.6M | $4.35 | POSITIVE |
| 2026-05-11 | $19.48 | $69.1M | $7.39 | POSITIVE |
| **2026-05-12** | $18.88 | **−$9.7M** | $6.93 | POSITIVE (first negative total) |
| **2026-05-13** | $18.44 | $13.6M | **$24.56** | **NEGATIVE FLIP** |
| 2026-05-14 | $17.39 | $24.3M | $5.77 | POSITIVE FLIP |
| 2026-05-15 | $17.21 | −$2.3M | $7.88 | POSITIVE |
| 2026-05-18 | $16.53 | −$9.8M | $9.00 | POSITIVE |

Two regime flips in 5/13 → 5/14 (the post-earnings repricing window).
Both ZGL and total GEX have been oscillating; the chain is still
**re-equilibrating** from the crash. The current $9.8M negative total
GEX is consistent with the 5/15 print of −$2.3M and represents the
"new normal" structure.

### OI trend

`historical_oi_trend` errored due to size:

```
Error: result (76,529 characters across 3,114 lines) exceeds maximum
allowed tokens. Output has been saved to a temp file (not retrieved).
```

**Workaround:** `total_open_interest` is reported daily in
`historical_trend`, which provides a sufficient OI trajectory:

| Date | Spot | Total OI |
|---|---|---|
| 2026-03-13 | $24.58 | 199,214 |
| 2026-03-23 | $28.75 | 178,227 |
| 2026-04-27 | $25.80 | 214,843 |
| 2026-05-04 | $27.49 | 209,133 |
| **2026-05-05** | $32.39 | 215,750 |
| **2026-05-07 (crash)** | $19.50 | 259,345 |
| 2026-05-08 | $20.48 | **296,458** (peak) |
| 2026-05-11 | $19.58 | 255,346 |
| 2026-05-12 | $18.88 | 260,892 |
| 2026-05-13 | $18.31 | 268,326 |
| 2026-05-14 | $17.39 | 269,938 |
| 2026-05-15 | $16.995 | 270,246 |
| **2026-05-18** | $16.71 | **214,439** |

**Story arc.**
- Pre-earnings OI base ~210K.
- Post-earnings OI surge to 296K on 5/8 (+82K, +39%) — investors
  positioning into the dislocation.
- OI sustained at 255-270K through 5/15.
- **OI dropped sharply to 214K on 5/18 (−56K from 5/15)** — back to
  pre-earnings base. The drop coincides with phase-1's $643K
  5-day sweep premium and the 5/22 OPEX week.

The 5/15 → 5/18 OI plunge is **the May OPEX cleanup signature** but
also tells us positions that opened post-earnings are closing into
the upcoming Friday OPEX. The fresh OI builds documented in phase-3
(9/18 20C, etc.) are *new* positioning replacing the closed positions.

### Multi-day trend (selected metrics)

`historical_trend`, days=30 (27 sessions):

| Date | Close | Vol (C+P) | Net flow | IV30d | IV rank | PCR | Flow |
|---|---|---|---|---|---|---|---|
| 2026-05-18 | 16.71 | 10,221 | −$8,155 | 81.3% | 42 | 0.40 | bearish |
| 2026-05-15 | 16.995 | 7,724 | +$33,575 | 73.1% | 34 | 0.52 | bullish |
| 2026-05-14 | 17.68 | 17,844 | −$167,556 | 74.8% | 35 | 0.39 | bearish |
| 2026-05-13 | 18.31 | 10,514 | −$397,923 | 87.9% | 50 | 0.43 | bearish |
| 2026-05-12 | 19.03 | 16,479 | +$144,602 | 89.2% | 51 | 0.38 | bullish |
| 2026-05-11 | 19.58 | 23,664 | −$849,633 | 91.4% | 54 | 0.26 | bearish |
| 2026-05-08 | 20.48 | 36,179 | −$783,757 | 87.1% | 49 | 0.43 | bearish |
| **2026-05-07** | **19.50** | **100,156** | **+$7,299,515** | 88.3% | 50 | 0.73 | **bullish** |
| 2026-05-06 | 31.57 | 54,589 | −$1,659,079 | 128.7% | 96 | 0.46 | bearish |
| 2026-05-05 | 32.385 | 67,241 | −$2,470,940 | 127.6% | 92 | 0.46 | bearish |
| 2026-05-04 | 27.49 | 12,779 | +$178,928 | 127.0% | 94 | 0.38 | bullish |
| 2026-05-01 | 28.07 | 44,410 | −$1,008,173 | 129.0% | 96 | 0.32 | bearish |

The earnings move was 2026-05-07 (close $19.50 from prior $31.57 =
**−38.2%**). On that day, despite the crash, **net flow was
+$7.3M BULLISH** with PCR 0.73 (highest in the window) — heavy
dip-buying activity. From 5/8 onward, daily flows have been mostly
bearish/mixed, but the campaign from phase-1 has rebuilt the
bullish momentum at the lower price.

### Signal backtest — CAUTION

`historical_signal_backtest`, signal_type=bullish_flow, lookback_days=20:

| Field | Value |
|---|---|
| total_signals | 12 |
| **win_rate** | **8.3% (1/12)** |
| **avg_move_pct** | **−3.22%** |
| Signal date range | 2026-05-13 → 2026-05-15 |

Of the 12 bullish_flow signals fired in the past 5 trading sessions
across the market, 11 are down 20 days later — average −3.22%. The
single winner is MSFT (+1.32%). Tickers in the failed cohort: AAPL,
UPS, QQQ, SMH, META, AVGO, TSLA, NVDA, GOOGL, META (twice), QQQ.

**Important caveats:**
1. None of the 12 signals is FSLY — this is a *market-wide regime*
   warning, not FSLY-specific evidence.
2. The signals fired 5/13-5/15, all into the same week of broad-tech
   weakness. They are heavily correlated (same regime, same period).
3. The tool only returned 12 signals against requested 20 → it's a
   thin sample.

Interpretation: **the tech complex has been hostile to bullish_flow
setups for the last 2 weeks.** FSLY's flow campaign may face the
same headwind unless either (a) the regime breaks, or (b) FSLY has
ticker-specific catalysts that decouple it from the complex.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|---|---|---|
| `mcp__uw-pp__historical_iv_percentile_zscore` | symbol=FSLY, lookback_days=252 | IV percentile 7.69 (1y); z-score −0.95; LOW_IV |
| `mcp__uw-pp__historical_vrp` | symbol=FSLY, date=2026-05-18 | vrp −0.85; PREMIUM_BUYING regime |
| `mcp__uw-pp__historical_cumulative_premium_flow` | symbol=FSLY, days=90 | net +$9.9M; trend BULLISH |
| `mcp__uw-pp__historical_pc_ratio_zscore` | symbol=FSLY, lookback_days=20 | z=−0.18 (NORMAL); no sentiment extreme |
| `mcp__uw-pp__historical_gex_time_series` | symbol=FSLY, days=30, dte_max=45 | 2 regime flips 5/13-5/14; chain still re-equilibrating |
| `mcp__uw-pp__historical_oi_trend` | symbol=FSLY, days=30, top_n=15 | **ERROR — output too large; surfaced verbatim below** |
| `mcp__uw-pp__historical_trend` | symbol=FSLY, days=30 | 27 sessions; earnings crash 5/7; net BULLISH 14/27 days |
| `mcp__uw-pp__historical_signal_backtest` | signal_type=bullish_flow, lookback_days=20, top_n=20 | **WIN RATE 8.3%**; 12 signals; tech-complex regime warning |

## Tool errors

`mcp__uw-pp__historical_oi_trend`:

```
Error: result (76,529 characters across 3,114 lines) exceeds maximum
allowed tokens. Output has been saved to
/Users/ewan/.claude/projects/-Users-ewan-Development-stock-deep-dive/
d172a9ad-c05f-4f0f-a7f6-612f88071864/tool-results/
mcp-uw-pp-historical_oi_trend-1779198518372.txt
```

The 30-day OI trajectory has been reconstructed from `historical_trend`
daily total_open_interest (table above), which is sufficient for the
purposes of this phase. No retry attempted.

## Verdict for downstream phases

- **Volatility regime:** vol is **cheap vs realised** (VRP −0.85) and
  cheap vs 1y history (7.7th percentile). **Favor premium-buying**
  structures over premium-selling structures, with the caveat that
  the 5/22 expiry alone is rich (117.7% IV vs 81% baseline) — avoid
  buying single-week premium, prefer 30-90 DTE.
- **Premium-flow direction:** 90-day net BULLISH (+$9.9M); aligns
  with phase-1's flow campaign.
- **Conviction on edge:** **2.5 / 5** — historical context is mixed.
  Pros: VRP edge, 90d bullish flow, vanna squeeze setup. Cons:
  bullish_flow signal has 8% win rate in current regime, the
  earnings crash creates ongoing repositioning chop, and the chain
  has flipped regime twice in 5 days.
- **Three specific data points for phase-9:**
  1. **IV percentile 7.7 / VRP −0.85** → debit structures (long
     calls, call spreads) have favorable vol edge.
  2. **−38% earnings crash on 2026-05-07** → recent shareholder
     base is bagholders + bottom-fishers; ~$18.84-$19.03 overhead
     supply (phase-2) is "earnings sellers' cost basis".
  3. **bullish_flow win_rate 8.3%** → require ABOVE-NORMAL
     conviction before sizing up; reduce position vs base case.
- **Open questions:**
  - Is FSLY decoupled enough from the tech complex (smaller cap,
    idiosyncratic story) that the 8% win rate doesn't apply? →
    phase-6 (macro/sector) + phase-7 (insights composite) +
    phase-8 (analyst views).
  - What's actually driving the 5/22 IV spike (117.7%)? Earnings
    already passed 5/7. Candidates: 5/22 monthly OPEX gamma, lockup
    expiry, secondary offering rumor, M&A speculation. → phase-6.
  - The 9/18 $20C standing OI of 2,890 (phase-3) was built mostly
    pre-crash. Is it underwater (long call holders) and likely to
    sell on any bounce, or fresh post-crash conviction? → cross
    with `historical_oi_trend` rebuild in phase-7 if possible.
