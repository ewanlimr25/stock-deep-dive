# Phase 5 — Historical Context & VRP

**Ticker:** BABA
**As-of date:** 2026-05-27
**Generated:** 2026-05-28T03:35:00Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md, phase-1-flow.md, phase-4-structure.md

## Summary

History reframes today's read in two decisive ways. **(1) Vol is cheap:** IV30d
0.372 sits at the **0th percentile / z −1.61** of the available window and **VRP
is negative (−0.093)** — IV 37.2% vs realized 46.5% → a **PREMIUM-BUYING regime**
(buy options, don't sell them) `[HIST:vrp]` `[HIST:iv_percentile_zscore]`. **(2)
The bearish-flow signal that phase-1 leaned on has a poor recent track record:**
the market-wide `bearish_flow` backtest wins only **37.5% (n=8)** at 5d / 33.3%
(n=15) at 10d — **below the 0.45 edge threshold** `[HIST:signal_backtest]`. So the
tape's bearish lean is real but **historically unreliable right now** (the
environment has been mean-reverting/bouncing). The 30-session trend is genuinely
weak (**21 of 30 bearish-flow days**, price $134→$128, IV rank 32→21)
`[HIST:trend]`, fz confirms a clean multi-timeframe downtrend (below
SMA20/50/200, −33.7% off the 52w high, RSI 41.6 — **not yet oversold**)
`[HIST:rsi fz]`, **but** cumulative 90-day flow is net **bullish +$327M**
`[HIST:cumulative_premium_flow]` and the gamma regime is **unstable** (8 flips/30d,
NEGATIVE as recently as 05-26) — so phase-4's "long gamma" is **today-only,
low-confidence** `[HIST:gex_time_series]`. Net: a bearish backdrop, but the edge
to *act* on it is weak and the cheap-vol math says express any view with **long
premium, small size**.

## Key signals

- **VRP −0.093, PREMIUM_BUYING** (IV 0.372 < RV 0.465) → favor **debit/long-option**
  structures `[HIST:vrp]`.
- **IV 0th percentile, z −1.61, LOW_IV** over 32 available sessions — vol
  historically cheap `[HIST:iv_percentile_zscore]`.
- **`bearish_flow` backtest win_rate 37.5% (n=8) / 33.3% (n=15) — edge-NEGATIVE**
  `[HIST:signal_backtest]`.
- **Trend: 21/30 bearish-flow days, price $134.43→$127.76, IV rank 32→21**
  `[HIST:trend]`; cumulative 90d flow net **bullish +$327M** `[HIST:cumulative_premium_flow]`.
- **GEX regime UNSTABLE** — 8 flips/30d, NEGATIVE on 05-26 → POSITIVE on 05-27;
  ZGL swings $62→$149→$91 (single-name calc noisy) `[HIST:gex_time_series]`.

## Detailed findings

### IV regime (percentile + z-score + VRP) `[HIST:iv_percentile_zscore]` `[HIST:vrp]`

- `current_iv30d` 0.3724; `iv_percentile` **0**; `iv_zscore` **−1.611**; regime
  **LOW_IV**. **Gap caveat:** computed over **32 available sessions**, not a true
  252-day window (gap 03-28→04-24) — "0th percentile" means lowest of the 32, not
  a clean 1-year extreme, but z −1.61 confirms genuinely cheap.
- VRP **−0.0926**: IV30d 0.3724 < realized 0.465 → **PREMIUM_BUYING**. The crowd
  (phase-1: both legs net-sold) is **selling cheap vol** — the structural edge is
  to the **buyer** of premium. Reinforces phase-4's complacent skew (cheap puts).

### Cumulative premium flow (90d) `[HIST:cumulative_premium_flow]`

- cumulative_bullish **$1,435M** vs cumulative_bearish **$1,109M** → net
  **+$327M bullish** over the available window. Longer-horizon flow is net-buy
  even though the last 5 sessions and price action are bearish — consistent with
  the patient LEAP/dip buyers (phase-1 C210 Dec-2028, phase-2 block buys) layering
  in *against* the downtrend. (dates_covered span the gap — directional sign is
  robust, the dollar total is over available sessions only.)

### P/C ratio z-score (20d) `[HIST:pc_ratio_zscore]`

- current 0.3848, mean 0.3229, std 0.0748, **z 0.828 — NORMAL**. No sentiment
  extreme; today's call-heavy P/C is ordinary for BABA. No contrarian trigger.

### GEX time series (regime stability) `[HIST:gex_time_series]`

- **Trajectory is unstable: 8 regime flips in 30 sessions.** Recent: 05-22
  POSITIVE (ZGL 62.75), **05-26 NEGATIVE (ZGL 149.42 > spot 129.51)**, 05-27
  POSITIVE (ZGL 91.35). ZGL is wildly variable ($62→$149→$91) — the single-name
  GEX calc is noisy (tool caveat: "most meaningful for index products"). **Phase-4's
  long-gamma conclusion is a today-only snapshot, not a stable regime** — a flip
  back to negative (as on 05-26) would un-cap downside vol. Treat as low-confidence.

### OI trend (30d) `[HIST:oi_trend]`

- **27 consecutive build days**; today net_oi_change **+14,404** (438 contracts up
  vs 156 down). Sustained OI accumulation — positions are being *added*, not
  closed, across the window (consistent with both the LEAP build and the
  covered-call overwriting). Build is broad, not concentrated.

### Multi-day trend table (selected) `[HIST:trend]`

| date | close | net_flow $M | iv_rank | flow_dir |
|------|------:|-----------:|--------:|----------|
| 05-27 | 127.76 | −1.76 | 21.2 | bearish |
| 05-26 | 129.64 | −2.56 | 39.0 | bearish |
| (05-13 peak) | 145.81 | +14.23 | 83.0 | bullish |

- Summary: **bearish_days 21 / bullish_days 9** over 30 sessions (date_range
  2026-03-18→2026-05-27, gap-spanning); price_change $134.43→$127.76; iv_rank
  32.19→21.19; `flow_direction_latest = bearish`.

### Price context (fz, advisory) `[HIST:rsi fz]` `[HIST:52w_proximity fz]`

- RSI(14) **41.56** (bearish-leaning, **not oversold** — room to fall toward the
  $110–113 trapdoor before a reflex bounce). Below SMA20 (−5.21%), SMA50 (−2.83%),
  **SMA200 (−14.59%)** → downtrend on every timeframe. Perf YTD −12.84%, Perf
  Month −3.59%. **52W High $192.67 (−33.69% below); 52W Low $103.71 (+23.19%
  above)** — mid-to-lower of its annual range, decisively off the highs but with
  ~$24 (19%) of room down to the 52w low. Advisory only; not in Kelly `p`.

### Signal backtest (current signal's edge) `[HIST:signal_backtest]`

- **`bearish_flow`, 5d lookback: win_rate 37.5%, n=8, avg_move 1.84%.** 10d
  lookback: 33.3%, n=15. Of the 8 firings, only 3 fell (MSTR −3.6%, NVDA −1.3%,
  NVDA −3.2%); 5 *rose* (SNDK +7.5%, AMD +10.2%, IWM +2.8%, GOOGL +1.5%, SPY
  +0.7%). **Below the 0.45 edge floor → the bearish-flow signal is currently
  edge-negative.** Market-wide & in-sample (tool: "not a robust live edge") — treat
  as a weak prior, not a per-BABA stat.
- `dark_pool_accumulation`: `total_signals 0` (no firings) → not usable.

## Tool calls (audit trail)

| Command | Result summary |
|---------|----------------|
| `uw historical iv-percentile-zscore --symbol BABA --lookback-days 252` | iv pctile 0, z −1.61, LOW_IV (32 sessions) |
| `uw historical vrp --symbol BABA --realised-window-days 30` | VRP −0.093, PREMIUM_BUYING |
| `uw historical cumulative-premium-flow --symbol BABA --days 90` | net +$327M bullish |
| `uw historical pc-ratio-zscore --symbol BABA --lookback-days 20` | z 0.828, NORMAL |
| `uw historical gex-time-series --symbol BABA --days 30` | 8 flips, unstable, neg 05-26 |
| `uw historical oi-trend --symbol BABA --days 30` | 27 consecutive build days |
| `uw historical trend --symbol BABA --days 30` | 21/30 bearish days, $134→$128 |
| `uw historical signal-backtest --signal-type bearish_flow` | win_rate 37.5% (n=8) / 33.3% (n=15) |
| `uw historical signal-backtest --signal-type dark_pool_accumulation` | 0 signals |
| `fz quote BABA` | RSI 41.6, below all SMAs, −33.7% off 52w high |

## Tool errors

- Trailing-anchor caveat: `iv-percentile-zscore`, `pc-ratio-zscore`, `oi-trend`,
  `cumulative-premium-flow`, `signal-backtest`, and `vrp`'s realized leg anchor to
  the **latest available date (2026-05-27 = as-of here, so date-correct)**; a re-run
  after a new session would shift them.
- Gap (03-28→04-24): all `--days`/`--lookback` windows span the hole — counts are
  **available sessions**, not calendar days. No silent interpolation detected
  (date arrays show the gap explicitly).

## Verdict for downstream

- **Volatility regime:** **CHEAP** (IV 0th pctile, z −1.61) and **PREMIUM-BUYING**
  (VRP −0.093). Favor **debit / long-option** structures; fading the crowd's
  vol-selling is the structural edge.
- **Premium environment:** the tape is *selling* cheap vol → be the **buyer**.
- **Conviction that today's signal is HISTORICALLY EDGE-POSITIVE:** **LOW (2/5).**
  The bearish-flow signal class is currently **edge-negative (37.5%)**; the trend
  is real but the signal to trade it is unreliable, vol favors buyers, cumulative
  flow is net-bullish, and the gamma regime is unstable. Bears get a clean
  downtrend + room to $110–113; bulls get cheap vol + vanna-squeeze + net-bullish
  cumulative flow.
- **Three specific data points:** IV percentile **0** (z −1.61); VRP **−0.093**
  (premium-buying); `bearish_flow` win-rate **37.5% (n=8)**.
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:     bearish_flow
  signal_backtest_win_rate: 0.375
  win_rate_n:       8
  win_rate_source:  backtest
  ```
  (Market-wide, in-sample. 10d variant 0.333/n=15. Apply the N-conditional cap —
  n=8 is small AND p<0.45 → minimal-to-zero Kelly size on a bearish bet.)
- **Open questions:** What catalyst does the backwardation (phase-4) price into
  early June (no earnings until Sept)? — phase-6. Does the net-bullish cumulative
  flow + 27-day OI build mean institutions are bottom-fishing under the downtrend
  (phase-7b/8)? Is RSI 41.6 (not oversold) leaving room to the $110–113 trapdoor?
