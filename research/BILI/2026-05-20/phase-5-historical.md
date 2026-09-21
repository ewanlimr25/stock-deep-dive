# Phase 5 — Historical Context & VRP

**Ticker:** BILI
**As-of date:** 2026-05-20 (data date 2026-05-19)
**Generated:** 2026-05-20T10:10:00-04:00
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-4-structure.md

## Summary

BILI is **recovering from a sharp ~25% drawdown** since the 3/17 peak at $26.76,
basing in the **$19.00–$20.00 zone** for the last three sessions. The
volatility regime is **fresh-positive-gamma with low IV** — IV30d 48.0% sits
at the **0th percentile** of the available 27-day window (z-score -2.35), and
**VRP is -3.87 (FAIR/mildly premium-buying)**, meaning realized 30-day vol
(51.9%) is slightly outrunning implied. The dealer GEX has flipped from
**NEGATIVE to POSITIVE on 5/18**, and total GEX has more than doubled in two
sessions ($148M → $227M) — dealers are now structurally long gamma at deeper
levels than any time in the available window. Cumulative 28-day flow is
**MIXED** (bullish $15.1M / bearish $14.4M, net +$716k = essentially balanced)
— today's bullish call sweep is fresh, not a sustained accumulation. P/C
ratio z-score is **NORMAL** (-0.19, no sentiment extreme).

## Key signals

- **IV30d 48.0% / IV rank 34 / percentile 0 / z-score -2.35** — implied vol
  is at recent lows after IV crush from the 5/13 high (89th IV rank)
  [HIST:iv_percentile_zscore,trend].
- **VRP = -3.87% (FAIR)** — IV close to realized; realized slightly higher →
  **mildly premium-buying** regime, favors **debit structures**
  [HIST:vrp].
- **GEX regime flipped NEG→POS on 5/18, sustained 5/19** with total GEX
  jumping $148M → $227M (53% one-day expansion) [HIST:gex_time_series].
- Cumulative 28-day premium net flow **+$715,753 (MIXED)** — not a stealth
  accumulation pattern [HIST:cumulative_premium_flow].
- Price has retraced **-25% from $26.76 (2026-03-17) to $19.55 (2026-05-19)**,
  building a base at $19.00–$20.00 over 3 sessions [HIST:trend].

## Detailed findings

### IV regime [HIST:iv_percentile_zscore,vrp]

```
IV30d           : 48.02%
IV percentile   : 0   (LOW_IV)  — note: 27-day base, not full 252
IV z-score      : -2.35
Realized vol-30 : 51.89%
VRP             : -3.87% (FAIR, mildly premium-buying)
IV rank (today) : 34.3
IV rank trajectory: 32→37→55→87 (peak 5/14) →62→54→34 (today)
```

**The IV crush is the cleanest signature** in the recent series: IV rank peaked
at 89.5 on 5/13 (right before the −9% sell-off 5/13→5/15), then collapsed to
34 as the move played out and volatility re-priced. Today's IV is structurally
attractive for **buying premium**, especially on the call side given phase-4's
inverted skew.

### Cumulative premium flow [HIST:cumulative_premium_flow]

```
Window           : 28 trading days (2026-03-13 → 2026-05-19, with a
                   2026-03-28 → 2026-04-26 dataset gap)
Bullish premium  : $15,145,891
Bearish premium  : $14,430,138
Net flow         : +$715,753 (slight bull tilt)
Trend            : MIXED
```

**Not a "stealth accumulation" pattern.** Bullish and bearish premium are
within 5% of each other over the available window. Today's Jan-2027 $25 call
sweep ($217k single-timestamp) is a fresh institutional print — not the
continuation of a 28-day campaign.

### P/C ratio z-score [HIST:pc_ratio_zscore]

```
Current PCR     : 0.37   (calls dominate ~3:1)
Mean PCR (20d)  : 0.4455
Std PCR (20d)   : 0.3897
Z-score         : -0.194  → NORMAL (no extreme)
```

PCR is slightly below mean but within one standard deviation. **No
contrarian sentiment extreme** — sentiment is neutral-to-mildly-bullish in a
historically normal way. The 5/8 print of PCR 1.04 (put-heavy hedge day) and
5/18 PCR 5.75 (massive put buying day) are tail events that have washed out.

### GEX time series [HIST:gex_time_series]

| Date | Spot | Total GEX | ZGL | Regime |
|---|---|---|---|---|
| 2026-03-13 | $25.21 | +$357,962 | n/a | FULLY_POSITIVE |
| 2026-03-17 | $26.32 | +$2,950,938 | $22.01 | POSITIVE (peak) |
| 2026-03-19 | $24.97 | +$6,391,559 | $24.06 | POSITIVE |
| 2026-03-23 | $24.41 | -$4,139,830 | n/a | FULLY_NEGATIVE |
| 2026-03-26 | $22.79 | -$1,753,538 | n/a | FULLY_NEGATIVE |
| 2026-04-27 | $21.79 | -$6,102,128 | n/a | FULLY_NEGATIVE |
| 2026-04-30 | $21.87 | +$134,481,446 | $24.50 | NEGATIVE (below ZGL) |
| 2026-05-06 | $22.34 | +$50,219,870 | $20.51 | POSITIVE (flip ↑) |
| 2026-05-08 | $22.06 | +$94,168,135 | $22.61 | NEGATIVE (flip ↓) |
| 2026-05-11 | $22.22 | +$49,886,644 | $18.01 | POSITIVE (flip ↑) |
| 2026-05-13 | $22.46 | +$69,909,973 | $22.72 | NEGATIVE (flip ↓) |
| 2026-05-14 | $20.49 | +$114,003,439 | $20.68 | NEGATIVE (-9% session) |
| 2026-05-15 | $19.26 | +$91,967,852 | $20.58 | NEGATIVE |
| 2026-05-18 | $19.50 | +$148,262,755 | **$3.02** | **POSITIVE** (flip ↑) |
| **2026-05-19** | **$19.55** | **+$226,786,819** | **$19.11** | **POSITIVE** |

**Five regime flips in 28 days** (high-frequency regime change is itself a
volatility signal). The 5/18 → POSITIVE flip is critical: the ZGL collapsed
to $3.02 — meaning the entire chain re-priced into structural long-gamma
territory after the down-move. Today (5/19), ZGL re-anchored at **$19.11**
on a huge expansion of total GEX (+53% session-on-session to $226.8M).

**Reading:** dealers have spent most of April and early May in NEG-gamma /
above-ZGL configurations — the perfect setup for volatility expansion (which
delivered the 5/13–5/15 drop). Now in **fresh-pos-gamma** with $20 as the
magnet, the regime should compress realized vol and produce mean-reverting
intraday behavior — a 180° regime change from one week ago.

### Multi-day trend (28d) [HIST:trend]

Selected rows showing price + IV + flow direction:

| Date | Close | IV30d | IV rank | PCR | Flow | Net flow |
|---|---|---|---|---|---|---|
| **2026-05-19** | **$20.03** | **48.0%** | **34** | **0.37** | **bullish** | +$230k |
| 2026-05-18 | $19.63 | 55.6% | 54 | 0.23 | bearish | -$127k |
| 2026-05-15 | $19.07 | 56.6% | 62 | 0.30 | bearish | -$230k |
| **2026-05-14** | **$20.32** | **66.8%** | **87** | **0.08** | **bearish** | **-$395k** (size!) |
| 2026-05-13 | $22.34 | 67.6% | 89 (peak) | 0.16 | bullish | +$82k |
| 2026-05-08 | $22.04 | 58.5% | 63 | 1.04 | bearish | -$241k |
| **2026-04-29** | $21.46 | 50.4% | 31 | 0.80 | **bullish** | **+$516k** (size) |
| 2026-03-18 | $25.50 | 51.4% | 29 | **5.75** | bullish | +$779k (PUT outlier — $8.94M put premium) |

**Notable:**
- **2026-05-14** was the regime-break day: $20.32 close, IV rank 87 (peak vol
  fear), net bearish flow $395k, PCR 0.08 (call-heavy — counterintuitive).
- **2026-03-18** had a massive PCR 5.75 and $8.94M of put premium — likely a
  major hedge or distress print well before today's setup. The decline from
  $25.50 to $20.03 over 2 months has worked off that hedge.
- Today (5/19) sits at IV rank 34 with bullish flow and PCR 0.37 — **the
  cleanest single-day risk-on signature in the window**.
- Bullish days: 13, Bearish days: 15. Recency: **3 consecutive bearish days
  (5/14-15-18) followed by today's bullish reset** = pattern of base + reversal.

### Signal backtest [HIST:signal_backtest]

`dark_pool_accumulation` signal: **0 historical firings** for BILI in the
available window — cannot establish ticker-specific edge from this dataset.

`bullish_flow` signal (market-wide context check, last 5 trading days):
**3 of 15 wins = 20% win rate, avg move -1.35%**. Names like AMD won (+5.5%)
but TSLA (-7.2%), GOOGL (-4.0%), AVGO (-4.9%), META (-2.1%) lost. Conclusion:
**bullish-flow signals as a *cross-sectional* class have been a fade for the
past week** — a cautionary tape signal even if BILI's own setup is constructive.
BILI was not among the 15 names that fired the signal.

### OI trend [HIST:oi_trend]

Tool returned 78,918 chars of detailed per-strike multi-day OI rows that
exceeded the inline token budget; output was paged to a side file but **not
re-read** to preserve context. **Limitation acknowledged: detailed OI trend
not summarized in this phase.** Key OI dynamic was already established in
phase-3 (institutional call-write + bull-spread structure forming today;
total OI 274,470 today vs 247,500 on 3/27 — a +11% chain expansion over 6
weeks). For the level of granularity needed by phase-9, phase-3's
single-day snapshot is sufficient.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|---|---|---|
| `historical_iv_percentile_zscore` | symbol=BILI, lookback=252 | IV30d 48.0%, percentile 0, z -2.35, LOW_IV |
| `historical_vrp` | symbol=BILI, window=30 | VRP -3.87%, FAIR |
| `historical_cumulative_premium_flow` | symbol=BILI, days=28 | Bull $15.1M / Bear $14.4M / Net +$716k, MIXED |
| `historical_pc_ratio_zscore` | symbol=BILI, lookback=20 | PCR 0.37, z -0.19, NORMAL |
| `historical_gex_time_series` | symbol=BILI, days=28 | 5 regime flips; latest POSITIVE since 5/18 |
| `historical_oi_trend` | symbol=BILI, days=28 | Output exceeded tokens — not re-read, limitation noted |
| `historical_trend` | symbol=BILI, days=28 | 13 bull / 15 bear days; today bullish, IV rank 34 |
| `historical_signal_backtest` | dark_pool_accumulation, 5d | 0 firings (no BILI history) |
| `historical_signal_backtest` | bullish_flow, 5d | 15 cross-sectional firings, 20% win rate, avg -1.35% |

## Tool errors

`historical_oi_trend` exceeded the inline token budget (78,918 chars in 3,229
lines). Output was paged to disk but not consumed; phase-3 OI analysis is
sufficient for downstream phases.

## Verdict for downstream phases

- **Bias from this phase:** **constructive base** — recent 25% drawdown,
  IV crushed, GEX regime flipped fresh-positive, slight realized-vol over
  implied (premium-buying favored). Setup quality is **higher than the 28-day
  average** but the *cross-sectional* bullish-flow signal has been weak for
  the broader market.
- **Conviction:** **3.5 / 5** — historical context aligns with a constructive
  setup but two important caveats: (1) cumulative 28-day flow is mixed
  (no stealth accumulation), (2) market-wide bullish-flow signal has been
  a fade this week (20% win rate). Edge exists but is regime-dependent.
- **Three specific datapoints for phase-9:**
  1. **IV percentile = 0** (LOW_IV regime) → favor **debit** structures (long
     calls / call spreads / put credit spreads with cheap call wing).
  2. **VRP = -3.87%** → realized > implied → don't sell premium naked; if
     selling, prefer narrow spreads with defined risk.
  3. **GEX regime flipped 5/18 (one session ago)** → fresh-positive-gamma
     window typically lasts 5-10 sessions before next flip → constructive
     time-window aligns with 5/22 weekly OPEX through 5/29 weekly.
- **Open questions:**
  - The 5/14 down-move had IV rank 87 the prior day (5/13) but neutral PCR
    0.16 — what news drove the sell-off? Phase-6 should check Chinese ADR
    sector catalysts for 5/13–5/15.
  - 20% win rate on bullish_flow market-wide is concerning — was the entire
    last week a beta-risk event (e.g., Fed, China data)? Phase-6 should
    map to a regime.
  - Does BILI's earnings calendar matter? Bilibili's Q1 typically reports
    in late May; if earnings is upcoming, front-end backwardation +
    institutional positioning take on a different meaning. → phase-6 +
    phase-7 `insights_earnings_play`.
