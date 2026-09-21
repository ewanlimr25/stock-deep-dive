# Phase 5 — Historical Context & VRP

**Ticker:** NTAP
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T00:00:00Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-3-positioning.md, phase-4-structure.md, phase-0.5-context.md

## Summary

The historical context **rewrites the read of today's tape**: NTAP **gapped +12.4%
on 5/22** (close $123.95 → $139.36), the last leg of a **~37% rally off ~$102 (mid-
March)** straight into the **5/28 earnings**. So the 145C "overwrite" (phase-1) is
profit-taking/call-writing after a violent run, the fresh 130P/135P are hedges on
the spike, and the DP blocks (phase-2) chased price up. Vol is **rich**: IV
percentile **100**, z **+2.56**, VRP **+13.3 vol pts → PREMIUM_SELLING regime**.
Strikingly, options **premium flow has been net-bearish for 21 of 30 sessions and
cumulatively −$1.75M** *during* that price rally — a **price/flow divergence**
(persistent call-overwriting / skepticism into strength). The matching signal
backtest (`high_iv_rank`) shows a **60% vol-realisation rate (N=10, borderline-low)**
— the implied move usually shows up, which argues for **defined-risk** premium
selling over naked short vol.

## Key signals

- **+12.4% single-day move on 5/22** into 5/28 earnings; ~37% off the mid-March base [HIST:trend]
- **IV percentile 100, z +2.56, regime HIGH_IV** (over 30 available sessions, not a true 1y) [HIST:iv_percentile_zscore]
- **VRP +0.1332** (IV30 57.6% − realised 44.2%) → **PREMIUM_SELLING** edge [HIST:vrp]
- **Cumulative 31-session flow net BEARISH −$1.75M; 21/30 days bearish** despite the rally → **price/flow divergence** [HIST:cumulative_premium_flow], [HIST:trend]
- **OI in a 27-session consecutive build** (12.7K → 29.2K) — slow pre-earnings accumulation [HIST:oi_trend]
- **GEX stably POSITIVE; ZGL risen $103→$115 tracking spot; no flip in 5d** [HIST:gex_time_series]
- **Signal backtest `high_iv_rank`: vol-realisation 60%, N=10** (Kelly `p`, low-confidence) [HIST:signal_backtest]

## Detailed findings

### IV regime — `[HIST:iv_percentile_zscore]`, `[HIST:vrp]`

- current IV30d **57.6%**, **iv_percentile 100**, **iv_zscore +2.564**, regime
  HIGH_IV. **Gap caveat:** `dates_used = 30` — the "252-day" lookback had only **30
  sessions** present (snapshot window, gap 03-28→04-24 excluded), so this is "highest
  IV in the available 30 sessions," not a true 1-year percentile. Directionally
  unambiguous (IV is richly bid), but don't over-read the "100/252."
- **VRP +0.1332** (IV30 0.5755 − realised σ30 0.4423) → **PREMIUM_SELLING**. Options
  price ~13 vol points more than the stock has realised. Note realised σ is itself
  high (44%) because of the +12.4% gap — the spread still favours selling premium.

### Cumulative premium flow (90d requested → 31 sessions present) — `[HIST:cumulative_premium_flow]`

- cumulative_bullish $11.93M vs **cumulative_bearish $13.68M**, **net_flow −$1.75M,
  trend_direction BEARISH**. **Gap caveat:** `dates_covered` jumps 04-27 ← 03-27, so
  "90 days" = **31 actual sessions**. The net-bearish premium accretion *during a
  +37% price rally* is the headline divergence — consistent with sustained call
  overwriting / hedging into strength, not bullish accumulation.

### P/C ratio z-score — `[HIST:pc_ratio_zscore]`

- current PCR **0.178**, mean 0.388, std 0.793, **zscore −0.265 → NORMAL**. No
  sentiment extreme; today's call-heavy ratio is within range (the high std reflects
  the 5/19 put-spike day, PCR 3.52). **No contrarian signal.**

### GEX time series (30 sessions, gap-aware) — `[HIST:gex_time_series]`

- Regime **POSITIVE almost throughout**; brief NEGATIVE flips only in March at
  ~$102 spot (3/23, 3/27). Since 4/27, continuously POSITIVE. **No flip in the last
  5 sessions.**
- total_GEX peaked $8.6M (5/15), now ~$1.57M; **ZGL climbed $103 (Mar) → $115.41
  (now)** tracking spot up. The +12.4% move on 5/22 happened *inside* positive gamma
  — strong enough to overpower dealer long gamma → **news/momentum-driven**, not a
  gamma squeeze. A post-earnings break below **~$115 (ZGL)** would flip to short
  gamma (vol expansion) — roughly one implied-move down.

### OI trend — `[HIST:oi_trend]`

- **consecutive_build_days 27** — total OI ~12.7K (3/23) → 17.4K (4/27) → 21.6K
  (5/11) → **29,220 (5/22)**, roughly doubling. A **slow, sustained pre-earnings OI
  build** across the chain — *but* today's single-day net build was trivial (+231,
  phase-3). So: multi-week accumulation of positioning into the event, with no
  single-day conviction spike.

### Multi-day trend (selected) — `[HIST:trend]`

| Date | Close | IV rank | PCR | net_flow | flow_dir |
|------|-------|---------|-----|----------|----------|
| 05-22 | **139.36** | 100 | 0.18 | −48,537 | bearish |
| 05-21 | 123.945 | 87.4 | 0.15 | +40,458 | bullish |
| 05-20 | 118.97 | 98.0 | 0.35 | +127,332 | bullish |
| 05-19 | 120.63 | 89.4 | 3.52 | +73,126 | bullish (put-spike day) |
| 05-13 | 118.58 | 92.4 | 0.03 | −873,112 | bearish |
| 04-27 | 108.44 | 50.3 | 0.23 | −22,672 | bearish |
| 03-16 | 102.24 | 40.7 | 0.22 | −201,383 | bearish |

**bearish_days 21 / bullish_days 9** over 30 sessions; `flow_direction_latest
bearish`. Price climbed ~37% while options premium flow stayed predominantly
bearish — the divergence to carry into phase-8/9.

### Signal backtest — `[HIST:signal_backtest]`

| Signal | Rate | N | Note |
|--------|------|---|------|
| **high_iv_rank** (primary) | **vol-realisation 60.0%** | **10** | avg move 3.7%; mixed (RDW +18/+26%, CBRS −15%, ADI −4%) |
| volume_spike | 22.2% | 9 | avg +0.54%; sample is micro-ETFs (GIF/BLCN/PDLB) — **not comparable**, disregard |
| dark_pool_accumulation | **no results** | **0** | win_rate_source = null for the DP signal |

The `high_iv_rank` 60% is a **vol-realisation** rate (did the move show up), not a
directional win rate. It sits in **tension with the VRP premium-selling edge**: the
implied move materialises 60% of the time, so *naked* short premium is exposed — the
edge is in **defined-risk** premium selling (cap the tail, harvest the crush). N=10
is borderline-low → phase-9 must apply the N-conditional Kelly cap.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__historical_iv_percentile_zscore` | symbol=NTAP, lookback=252 | pctile 100, z+2.56 (30 sessions present) |
| `mcp__uw-pp__historical_vrp` | symbol=NTAP, realised=30 | VRP +0.1332, PREMIUM_SELLING |
| `mcp__uw-pp__historical_cumulative_premium_flow` | symbol=NTAP, days=90 | net −$1.75M BEARISH (31 sessions) |
| `mcp__uw-pp__historical_pc_ratio_zscore` | symbol=NTAP, lookback=20 | z −0.265, NORMAL |
| `mcp__uw-pp__historical_gex_time_series` | symbol=NTAP, days=30, dte_max=45 | stably POSITIVE, ZGL→115.41 |
| `mcp__uw-pp__historical_oi_trend` | symbol=NTAP, days=30, top_n=10 | 27 consecutive build days |
| `mcp__uw-pp__historical_trend` | symbol=NTAP, days=30 | +12.4% on 5/22; 21/30 bearish flow days |
| `mcp__uw-pp__historical_signal_backtest` | high_iv_rank / volume_spike / dark_pool_accumulation | 60% N10 / 22% N9 / null |

## Tool errors

None. **Gap-data caveats (not errors):** `iv_percentile_zscore` used 30 sessions for
a "252d" request; `cumulative_premium_flow` summed 31 sessions for a "90d" request;
`historical_trend` "30 days" spans 2026-03-16→05-22 with the 03-28→04-24 hole
excluded. All windows reported on **sessions actually present**, never annualised
across the gap (phase-0 §Local data).

## Verdict for downstream phases

- **Volatility regime:** **RICH** — IV percentile 100, VRP +13.3 → **premium-selling**
  environment. Favour credit / defined-risk short-vol structures over debit longs.
- **Environment:** **premium-SELLING**, but with a 60% vol-realisation rate → the
  earnings move usually shows up → **defined-risk only** (no naked short vol).
- **Conviction that today's signal is HISTORICALLY EDGE-POSITIVE:** **3/5 on the VOL
  thesis** (rich IV + premium-selling, tempered by 60% realisation and N=10);
  **2/5 on any DIRECTIONAL thesis** (net-bearish flow divergence, no OI conviction,
  no sentiment extreme).
- **Three specific data points:** IV percentile **100** (z +2.56); VRP **+0.1332**
  (PREMIUM_SELLING); `high_iv_rank` **vol-realisation 60%, N=10**.
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:     high_iv_rank        # event/vol is the real signal; directional flow = bearish-divergent (no edge)
  signal_backtest_win_rate: 0.60        # vol_realisation_rate (NOT directional) — interpret as "move materialises"
  win_rate_n:       10                  # borderline-low → apply N-conditional Kelly cap
  win_rate_source:  backtest
  ```
- **Open questions:** What drove the +12.4% 5/22 gap — upgrade, M&A chatter, or
  DELL/storage sympathy (phase-6/7c must resolve)? Does NTAP historically *fade*
  post-earnings despite beats (the phase-4 negative-vanna crush risk)? Is the
  net-bearish flow divergence smart skepticism or just mechanical overwriting
  against the rally? With earnings *inside* any 6/18 structure, is the trade a
  vol/event trade rather than a directional swing (phase-9)?
