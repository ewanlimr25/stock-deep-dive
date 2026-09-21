# Phase 5 — Historical Context & VRP

**Ticker:** SNOW
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T16:08:00Z
**Upstream phases cited:** phase-0-intake.md, phase-3-positioning.md, phase-4-structure.md, phase-0.5-context.md

> **Gap-aware window:** all "30-day" tools here run over the **31 sessions actually
> present** (2026-03-13…03-27 then 2026-04-27…05-22); the **21-session hole
> 2026-03-28→04-26** is excluded (phase-0). No metric is annualized across the hole.
> True N is small — confidence is correspondingly capped.

## Summary

Today's setup is a **high-IV name that has rallied hard into a binary**, with rich
vol that history says usually gets realized — *not* a clean directional edge. IV30d
0.833 is the **80th percentile** (z +0.888) over the available window, regime
HIGH_IV [HIST:iv_percentile_zscore], and VRP is **+0.303** (IV 83% vs realized 53%)
→ nominally PREMIUM_SELLING [HIST:vrp]. **But that VRP is pre-earnings:** the rich
front IV prices the 5/27 binary the trailing realized hasn't seen, and the
`high_iv_rank` backtest shows a **71.4% vol-realisation rate** [HIST:signal_backtest]
— the move tends to materialize, so premium-selling here is not a free lunch. Price
has **rallied ~+26% from $136 (4/30) to $172 (5/22) into the print**
[HIST:gex_time_series], OI is in a **25-session consecutive build**
[HIST:oi_trend], dealer gamma flipped POSITIVE on 5/13 and **spiked to +40.7M on
5/22** [HIST:gex_time_series]. Premium flow over the window is net +$57.8M but
**MIXED** [HIST:cumulative_premium_flow]; P/C z −0.65 = NORMAL, no sentiment extreme
[HIST:pc_ratio_zscore]. **The directional `bullish_flow` backtest (92.3%) is
universe-wide, N=13, on a hot up-tape — NOT a SNOW edge; treat as unreliable.**

## Key signals

- **VRP +0.303 (IV 83% / RV 53%) → PREMIUM_SELLING regime** [HIST:vrp] — but pre-event
  and offset by 71.4% vol-realisation; the edge is conditional on historical earnings
  moves vs the priced ±13% (phase-7b).
- **IV 80th pctile, z +0.888, HIGH_IV** [HIST:iv_percentile_zscore] — elevated but not
  extreme; SNOW structurally runs high IV (echoes phase-0.5 self-IV-rank 57th pctile).
- **Rallied +26% into earnings** ($136 4/30 → $172 5/22) [HIST:gex_time_series] —
  priced for good news; raises the bar for a positive reaction, increases downside
  asymmetry on a miss.
- **OI 25-session consecutive build, +16,717 on 5/22** (368 up / 171 down)
  [HIST:oi_trend] — sustained positioning into the catalyst, not a one-day spike.
- **Signal backtests are universe-wide & tiny-N:** `bullish_flow` 92.3% (n=13) on a
  semis-ripping tape, `high_iv_rank` vol-realisation 71.4% (n=14)
  [HIST:signal_backtest] — neither is SNOW-specific; low confidence for sizing.

## Detailed findings

### IV regime & VRP [HIST:iv_percentile_zscore][HIST:vrp]

current_iv30d 0.8327 · iv_percentile **80** · z **+0.888** · regime HIGH_IV (30
dates used). VRP = IV30d 0.8327 − realized 0.5298 = **+0.3029**, regime
PREMIUM_SELLING ("options pricing more vol than realised"). **Reconciliation:** the
30-day realized (53%) predates the earnings jump; the 5/29 IV (122.9%, phase-4)
prices a discrete event. So VRP overstates the "sell premium" case — pair it with the
historical *earnings* move (phase-7b), not the calm-period realized, before fading vol.

### Cumulative premium flow (31 sessions) [HIST:cumulative_premium_flow]

cumulative_bullish $685.2M vs cumulative_bearish $627.5M → net **+$57.8M**,
trend_direction **MIXED**. A slight bullish net over the window but no persistent
stealth accumulation — consistent with phases 1–3's two-sided read.

### P/C ratio z-score [HIST:pc_ratio_zscore]

current 0.369 vs 20d mean 0.563 (std 0.298) → z **−0.651**, **NORMAL**. Today is more
call-heavy than its recent norm but nowhere near a |z|>2 extreme → no contrarian
sentiment signal.

### GEX time series (regime stability) [HIST:gex_time_series]

Choppy negative/positive flips through late-Apr/early-May around $136–153, then
**POSITIVE and stable since 2026-05-13** (5 logged flips, last on 5/13). Total GEX
trajectory: 5/15 +31.2M → 5/21 +14.3M → **5/22 +40.7M** (the earnings-week 172.5
wall, phase-4). Spot path: 4/30 $136.4 → 5/15 $157.8 → 5/19 $169.6 → 5/22 $172.2.
**Net: +26% rally into the print under a hardening long-gamma regime.**

### OI trend [HIST:oi_trend]

`consecutive_build_days` **25** — OI built every available session. 5/22:
net_oi_change +16,717, 368 contracts increasing vs 171 decreasing; top builds are the
5/29 185C (+5,046) and 200C (+3,413) from phase-3, plus a LEAP 2028-01 180C (+487)
and 6/18 170C (+422). **Sustained structural buildup into earnings**, not spike/decay.

### Multi-day trend (selected) [HIST:trend]

bullish_days 15 / bearish_days 15 over 30 = perfectly split (MIXED); flow_direction
latest **bearish** (net_flow −$0.9M, the phase-1 number). IV rank ran 80–100
throughout the post-4/27 window (earnings vol). The 3/16–3/19 cluster shows huge put
premium ($75–324M, P/C 2–8) — large hedging/roll days at lower IV rank (~40), pre-
the run-up; not relevant to the current earnings setup but noted.

### Signal backtest (current signal's edge) [HIST:signal_backtest]

⚠ **Both are MARKET-WIDE** (the tool takes no symbol) over 2026-05-19→21, a tiny
window where semis ripped (MU +14–26%, SNDK, AMD up):
- `high_iv_rank`: **vol_realisation_rate 71.4%**, n=14, avg move 6.11% — the move
  usually shows up after a high-IV-rank flag.
- `bullish_flow`: **win_rate 92.3%**, n=13, avg move 8.7% — but inflated by the hot
  up-tape and not SNOW-specific.

**Neither is a reliable SNOW Kelly `p`.** N is tiny and the sample is universe-wide
on a one-directional tape. Phase-9 must apply the N-conditional cap
(`rubrics/sizing-rubric.md`) and effectively lean on the conviction bin, not 0.92.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `historical_iv_percentile_zscore` | symbol=SNOW, lookback=252 | IV 80th pctile, z +0.888, HIGH_IV (30 dates) |
| `historical_vrp` | symbol=SNOW, rv_window=30 | VRP +0.303, PREMIUM_SELLING (pre-event caveat) |
| `historical_cumulative_premium_flow` | symbol=SNOW, days=90 | net +$57.8M, MIXED (31 sessions) |
| `historical_pc_ratio_zscore` | symbol=SNOW, lookback=20 | z −0.651, NORMAL |
| `historical_gex_time_series` | symbol=SNOW, days=30 | POSITIVE since 5/13; +40.7M on 5/22; +26% rally |
| `historical_oi_trend` | symbol=SNOW, days=30 | 25 consecutive build days; 185C/200C lead |
| `historical_trend` | symbol=SNOW, days=30 | 15 bull / 15 bear = MIXED; latest bearish |
| `historical_signal_backtest` | high_iv_rank / bullish_flow, lookback=5 | 71.4% vol-real (n=14) / 92.3% win (n=13) — universe-wide |

## Tool errors

(none. Data-quality note: the historical series correctly skip the 03-28→04-26 hole —
the `dates_covered` lists jump 2026-03-27 → 2026-04-27, so no silent interpolation.)

## Verdict for downstream phases

- **Volatility regime:** **RICH** (IV 80th pctile, VRP +0.30) — *but* event-driven;
  the rich front IV prices the 5/27 binary and history (71.4% vol-realisation) says
  the move tends to come. Not a clean premium-sell.
- **Environment:** nominally **premium-selling**, with the strong qualifier that the
  earnings move is likely realized → favor **defined-risk** structures over naked
  premium-selling or naked premium-buying. The IV crush (phase-4) punishes long
  premium; the move-realization punishes naked short premium. Defined-risk spreads
  thread it.
- **Conviction that today's signal is HISTORICALLY EDGE-POSITIVE:** **2/5.** The
  directional backtest is unreliable; the genuine character is a wide ±13% event cone
  after a +26% run-up, with mixed flow.
- **Three datapoints:** IV percentile **80** (z +0.888); VRP **+0.303** (IV 83% / RV
  53%); `high_iv_rank` vol-realisation **71.4%** (n=14).
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:               bullish_flow (phase-3 capped-bull structure); regime = high_iv_rank
  signal_backtest_win_rate:   0.923          # bullish_flow — UNIVERSE-WIDE, NOT SNOW
  win_rate_n:                 13
  win_rate_source:            backtest (LOW CONFIDENCE — universe-wide, tiny-N, hot-tape-biased)
  alt_vol_realisation_rate:   0.714          # high_iv_rank, n=14 — the move usually materializes
  recommended_p_handling:     apply N-conditional cap; do NOT size on 0.92 — fall back to conviction bin
  ```
- **Open questions:**
  - Does SNOW's *own* earnings-move history run above or below the priced ±13%?
    (decides whether to be net-long or net-short vol) → phase-7b.
  - After a +26% run-in, is the fundamental story strong enough to clear a high bar,
    or is it priced for perfection? → phase-7b/7c.
  - Is the macro/sector regime calm enough to keep the long-gamma pin intact into the
    event? → phase-6.
