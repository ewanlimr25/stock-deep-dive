# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** OKLO
**As-of date:** 2026-07-17
**Generated:** 2026-07-18T00:00:00Z
**Upstream phases cited:** phase-0-intake.md

## Summary

OKLO's tape today is **not genuinely unusual** — it is a normal-to-quiet directional
day for the name. Net directional premium is a modest +$397,772 (bullish − bearish),
ranking **213 of 250** in the universe net-bullish screen and absent from the bearish,
volume-vs-average (≥2×) and iv-rank-high top-100 lists. Against its own 68-session
history the day is mildly bullish (net-dir 64th self-percentile) but **below-median on
total premium (42nd pctile, $19.75M vs $23.1M median)** and running at only **0.89× its
30-day average volume**. The nuclear/power theme it belongs to IS bid today — Cameco
(CCJ, +$15.4M net, rank 16), GE Vernova (GEV, +$15.2M, rank 17) and Bloom Energy (BE,
+$20.7M, rank 12) are all top-20 single names — but **OKLO itself is not the vehicle**
the flow is choosing. Context cap: phases 1–2 confluence held to `+`, not `++`.

## Universe ranking (as-of 2026-07-17)

- **Net bullish premium:** OKLO rank **213 / 250**, net_flow **+$397,772**
  (`bullish_premium 8,702,389 − bearish_premium 8,304,617`). Mid-to-low pack.
- **Net bearish premium:** OKLO **outside top-250** — not a net-bearish leader either.
- **Volume-vs-average (min 2× filter):** OKLO **outside top-100** — today's option
  volume is NOT ≥2× its 30-day average (DuckDB confirms 0.89×, i.e. below average).
- **IV-rank (high mode):** OKLO **outside top-100** — IV rank 32.7 is not universe-high.
- Universe leaders (indices aside): NVDA (+$81.6M), CDNS (+$55.4M), SNDK (+$42.7M),
  META (+$35.1M).

## Sector read

- OKLO is tagged **Utilities** in the screener (its advanced-nuclear/SMR theme sits in
  the power/utility complex).
- The **nuclear/power theme is in favour today**: BE rank 12 (+$20.7M), CCJ rank 16
  (+$15.4M), GEV rank 17 (+$15.2M) are all top-20 single names on net bullish premium.
- **Yellow flag for phase-6/phase-8:** the theme is bid but the flow is concentrated in
  the *larger, revenue-generating* nuclear names (Cameco = uranium miner; GE Vernova =
  power equipment), not the pre-revenue SMR story (OKLO). OKLO is a theme *laggard* on
  today's directional tape — relative-strength divergence to resolve downstream.

## Self-history (DuckDB escape hatch — 68 local sessions, `lib/duckdb-cuts.md §C`)

| Metric (today) | Value | Self-percentile | Read |
|---|---|---|---|
| Net-directional premium | +$397,772 | **64.2** | mildly bullish (own median is −$38.7K) |
| Total premium (call+put) | $19,752,534 | **41.8** | below own median $23.1M — quieter day |
| Volume / 30-day avg | 0.89× | 73.1 | ratio-pctile high but absolute <1 = below avg |
| IV rank | 32.7 | 76.1 | elevated vs own recent history, mid absolute |

Read: net-direction is above OKLO's own median (mildly bullish) but total premium and
absolute volume are below normal. Not a self-history outlier — falls short of the
`self_pctile_net_dir ≥ 80` "genuinely unusual" bar.

## Source

CLI ranks (`uw screener bullish-bearish / volume-vs-average / iv-rank`, `uw insights
deep-dive`) **+ DuckDB self-history** on `stock-screener-*.parquet` (68 sessions).
Metrics recorded "outside top-N": bearish (>250), volume-vs-average (>100 at 2× floor),
iv-rank-high (>100).

## Verdict for downstream

```
[CTX:]
universe_pctile_total_prem:  ~42        # self-history proxy; universe rank 213/250 net-dir
universe_rank_net_dir:       213 of 250
sector_leadership:           Utilities/nuclear theme LEADING today, but OKLO LAGS it
iv_rank:                     32.7
implied_move_pct:            0.73        # implied_move_perc 0.00733 from deep-dive; near-dated —
                                         #   phase-9 must reconcile vs IV30d ~97% & 2026-08-10 earnings
self_pctile_net_dir:         64.2
unusual_verdict:  BUSY_NAME_NORMAL_DAY   # leans quiet: mid-pack rank, below-median premium, <1x vol
```

- **Bias from this phase:** neutral (context only — no directional bias set here).
- **Three things later phases should remember:**
  1. Flow is **unremarkable** — cap phases 1–2 confluence at `+`; do not read the raw
     dollar figures as a strong signal.
  2. OKLO's **theme is bid but OKLO lags its peers** (CCJ/GEV/BE lead) — a relative-
     weakness tell the bull case must answer.
  3. IV rank 32.7 (mid) with IV30d ~97% and earnings **2026-08-10** — vol is
     structurally high but not rank-extreme; premium is expensive for buyers.
- **Open questions:** why is OKLO lagging its power-complex peers on flow — distribution,
  rotation, or just a quiet day? Resolve in phases 1–2 (is there hidden accumulation) and
  phase-6 (theme rotation).
