# Phase 5 — Historical Context & VRP

**Ticker:** CRM
**As-of date:** 2026-06-05 (latest available date = 2026-06-05, so all trailing
windows anchor exactly to as-of — reproducible this run)
**Generated:** 2026-06-06T16:25:00-04:00
**Upstream:** phase-4-structure.md (FULLY_NEGATIVE GEX on 6/05; "is the
magnet or the amplification the historical winner?"), phase-2-dark-pool.md
(price path 176→209.60→185.66), phase-0.5-context.md (iv_rank 60)

## Summary

History frames 6/05 as **the day dealer support finished evaporating after a
failed earnings breakout, in a premium-BUYING vol regime with no sentiment
extreme**. IV30d 0.4503 is only the 30.8th 1y percentile (z −0.70, regime
NORMAL, N=39 true sessions) yet realized vol ran 0.5377 → **VRP −0.0874,
PREMIUM_BUYING** ("Vol cheap vs realised"). The 30-session GEX series shows
support decaying monotonically through the fade — +$50.4M (5/29) → +$29.0M →
+$36.7M → +$18.8M → NEGATIVE flip 6/04 → **FULLY_NEGATIVE −$3.3M on 6/05** —
an unstable book that has flipped regimes 8 times in 30 sessions. 90-day
cumulative premium flow is dead-flat (net −$4.13M on $2.33B two-sided, MIXED);
P/C z-score −0.11 (NORMAL). The matching market-wide signal backtest
(`bearish_flow`, 5-day lookback) returns **win_rate 87.5% on N=8** with avg
forward move −2.73% — edge-positive but small-N and explicitly in-sample.

## Key signals

- **GEX regime flipped NEGATIVE on 6/04 and FULLY_NEGATIVE on 6/05** — flip
  inside the last 5 days → expect larger intraday ranges (heuristic). Dealer
  gamma through the fade: 5/29 +50.4M (spot 191.23) → 6/01 +29.0M (209.83) →
  6/02 +36.7M (200.65) → 6/03 +18.8M (190.93) → 6/04 +12.1M but spot below ZGL
  203.14 (NEGATIVE) → 6/05 **−3.3M, ZGL null**. `[HIST:gex_time_series]`
- **VRP −0.0874 → PREMIUM_BUYING** (IV30d 0.4503 vs realized30 0.5377; tool:
  "Vol cheap vs realised — favour premium buying"). Caveat: realized30 includes
  the +8.5%/+9.7% earnings legs — trailing-window inflation, but four fade
  sessions keep realizing ≥ implied (ATR 8.27→9.60, phase-0). `[HIST:vrp]`
- **IV is NOT rich: 30.77th 1y percentile, z −0.702, regime NORMAL** (N=39
  `dates_used` of the 252 requested — gap-aware true N). Long-premium
  structures are not fighting rich vol. `[HIST:iv_percentile_zscore]`
- **bearish_flow backtest: win_rate 87.5%, N=8, avg_move −2.73%** (market-wide
  base rate, not CRM-specific; methodology verbatim: "In-sample backtest — not
  a robust live edge"). `[HIST:signal_backtest]`
- **No sentiment extreme to fade:** P/C 0.57 vs 20d mean 0.5958, z −0.113
  (NORMAL) — the fade has NOT produced put-panic; complements phase-4's
  COMPLACENT skew. `[HIST:pc_ratio_zscore]`

## Detailed findings

### IV regime

IV30d 0.4503; 1y percentile 30.77; z-score −0.702; regime NORMAL (N=39).
VRP = 0.4503 − 0.5377 = **−0.0874 → PREMIUM_BUYING**. IV is cheap-to-fair
while the tape realizes 9%+ post-event days — debit structures are funded
fairly; credit selling is NOT being paid for the realized risk.
`[HIST:iv_percentile_zscore]` `[HIST:vrp]`

### Cumulative premium flow (90d window → 40 true sessions, gap-aware)

cumulative_bullish $1,161.7M vs cumulative_bearish $1,165.9M → **net −$4.13M,
trend MIXED** across the 40 sessions present (dates_covered spans 2026-03-13 →
2026-06-05 including the 03-28→04-26 hole). No stealth institutional build in
either direction — the $2.3B two-sided tape nets to noise.
`[HIST:cumulative_premium_flow]`

### P/C ratio z-score

current 0.57, 20d mean 0.5958, σ 0.2285, **z −0.113, extreme: NORMAL**. No
contrarian setup from sentiment. `[HIST:pc_ratio_zscore]`

### GEX time series (30 sessions, dte≤45)

Eight regime flips in 30 sessions (4/29, 4/30, 5/01, 5/06, 5/22, 5/27, 5/28,
6/04) — chronically unstable hedging book; ZGL estimates swing 85↔218 (coarse,
treat as bands). The operative sequence: post-earnings POSITIVE-gamma plateau
(5/29–6/03, +50M→+19M) decayed into the 6/04 NEGATIVE flip at spot 189.21 (ZGL
203.14) and 6/05's FULLY_NEGATIVE −3.3M. **Phase-4's open question answered in
part: the magnet (max-pain 190–192.5) has lost its dealer-gamma enforcement —
in the last two sessions the amplification side has been winning (closes 188.75
→ 185.66 through the put floor).** `[HIST:gex_time_series]`

### OI trend (30 sessions)

`overall_trend: BUILDING`, **21 consecutive build days**, total net OI change
**+640,594 contracts** — the chain has been accreting positions continuously
since late April (through earnings). Read with phase-3: the recent builds are
call-supply above spot; total chain OI 1,082,070 (phase-1 deep-dive) means the
last 30 sessions built more than half of today's standing OI. Note 6/05's own
biggest single-day jump: total_open_interest 1,071,134 (6/04) → 1,082,070
(6/05) = +10,936. `[HIST:oi_trend]` `[HIST:trend .daily_data]`

### Multi-day trend (30 sessions present, range 2026-03-27 → 2026-06-05 — crosses the gap)

bullish_days 12 vs bearish_days 18; flow_direction_latest "bullish" (the
+$1.28M 6/05 net); iv_rank 56.23 → 59.99 over the window; price 179.31 →
185.66. Recent dailies `[HIST:trend]`:

| Date | Close | Net flow | P/C | IV rank | Flow dir |
|---|---|---|---|---|---|
| 2026-06-05 | 185.66 | +$1.28M | 0.57 | 60.0 | bullish |
| 2026-06-04 | 188.75 | −$4.42M | 0.46 | 56.8 | bearish |
| 2026-06-03 | 190.61 | −$3.86M | 0.50 | 62.6 | bearish |
| 2026-06-02 | 200.84 | +$0.46M | 0.41 | 68.6 | bullish |
| 2026-06-01 | 209.60 | +$17.2M (101M bull vs 83M bear) | — | — | bullish |

The fade sessions (6/03–6/04) ran net-bearish flow; 6/05's "+$1.28M bullish" is
flat-noise, not a reversal print.

### Price context (`fz`, advisory)

RSI(14) **51.02** (neutral — momentum reset, not oversold `[HIST:rsi fz]`);
price +2.23% vs SMA20, +2.40% vs SMA50, **−15.66% vs SMA200**; Perf YTD
−29.92%; 52W: −32.93% from high (276.80), +13.54% above low (163.52)
`[HIST:52w_proximity fz]`. Structurally a broken long-term trend with a
mean-reverted short-term bounce — neither oversold-washout nor breakout.

### Signal backtest

`--signal-type bearish_flow --lookback-days 5`: **win_rate 87.5%,
total_signals 8, avg_move_pct −2.73%**. Methodology verbatim: "win_rate =
fraction of signals where forward move agrees with the signal's direction.
Lookback is in TRADING days; selection is positional within the yfinance bar
series. In-sample backtest — not a robust live edge." Market-wide (no
`--symbol`) → this is the base rate of the signal class, not CRM-specific.
N=8 < 10 → low-confidence per pitfall rule; phase-9 must apply the
N-conditional cap. `[HIST:signal_backtest]`

## Tool calls

| Command | jq path | Status |
|---|---|---|
| `uw historical iv-percentile-zscore --symbol CRM --lookback-days 252 --json` | `.iv_percentile/.iv_zscore/.regime/.dates_used` | ok N=39 |
| `uw historical vrp --symbol CRM --realised-window-days 30 --json` | `.vrp/.regime/.iv30d/.realised_vol` | ok |
| `uw historical cumulative-premium-flow --symbol CRM --days 90 --json` | `.net_flow/.trend_direction/.dates_covered` | ok (40 sessions) |
| `uw historical pc-ratio-zscore --symbol CRM --lookback-days 20 --json` | `.zscore/.extreme/.mean_pc_ratio` | ok |
| `uw historical gex-time-series --symbol CRM --days 30 --dte-max 45 --json` | `.regime_flip_dates/.trajectory[]` (first pass mis-pathed `.series` → empty; rows live in `.trajectory`) | ok n=30 |
| `uw historical oi-trend --symbol CRM --days 30 --top-n 10 --json` | `.overall_trend/.consecutive_build_days/.total_net_oi_change/.daily_data` (same re-path) | ok n=30 |
| `uw historical trend --symbol CRM --days 30 --json` | `.bullish_days/.bearish_days/.daily_data[:6]` (newest-first ordering; `[-5:]` first grabbed oldest) | ok n=30 |
| `uw historical signal-backtest --signal-type bearish_flow --lookback-days 5 --top-n 20 --json` | `.win_rate/.total_signals/.avg_move_pct/.methodology_notes` | ok |
| `fz quote CRM --agent` | `.fundamentals.{RSI,SMA*,Perf YTD,52W*}` | ok (advisory) |

## Tool errors

None. Data-quality caveats (not errors): (1) `trend` `date_range` 2026-03-27 →
2026-06-05 spans the 21-session local hole — `days_analyzed: 30` is the true N
and was used; (2) `iv-percentile-zscore` used 39 of 252 requested days
(`dates_used: 39`) — the 1y percentile is really a ~2-month percentile; (3)
trailing tools anchored to latest=2026-06-05 which equals as-of, so no
latest-anchor drift this run; (4) realized-vol window includes two ±9% earnings
legs — VRP partially event-inflated.

## Verdict for downstream

- **Volatility regime: CHEAP-TO-FAIR** (30.8th %ile — really ~2-month basis —
  z −0.70) with **VRP negative → PREMIUM-BUYING environment**: favor debit
  structures, avoid naked credit.
- **Premium flow:** 90d dead-flat (MIXED); no stealth build to lean on.
- **Conviction signal is HISTORICALLY EDGE-POSITIVE: 3/5.** The bearish_flow
  class wins 87.5% over 5 days (avg −2.73%) and the GEX-decay sequence has
  already been resolving downward — but N=8, in-sample, market-wide.
- **Three datapoints:** IV %ile **30.77** (N=39); VRP **−0.0874**
  (PREMIUM_BUYING); bearish_flow win_rate **87.5% / N=8 / avg −2.73%**.
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:     bearish_flow
  signal_backtest_win_rate: 0.875
  win_rate_n:       8
  win_rate_source:  backtest
  ```
- **Open questions:** Does the macro regime (phase 6) support pressing a
  short-gamma fade, or is the index tape in a dip-buying regime that rescues
  the 190–192.5 max-pain magnet? Is there a sector-rotation bid under
  software (phase 6 sector-flow-persistence)? Do the fundamentals (7b) veto
  shorting a name at 11.95× forward P/E (phase-0 drift)?
