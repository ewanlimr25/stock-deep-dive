# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** CMPS
**As-of date:** 2026-06-18
**Generated:** 2026-06-20
**Upstream phases cited:** phase-0-intake.md

## Summary

CMPS is having a **genuinely unusual but BEARISH-skewed** options day. It is *not*
a leader on any of the day's directional premium leaderboards (outside top-50 on
net bullish, net bearish, and volume-vs-average screeners), but the exact universe
percentiles tell the real story: total premium sits at the **83.2nd** universe
percentile (an active day), while net-directional premium is at the **3.4th**
universe percentile — i.e. CMPS is a strong net-**bearish** outlier by skew. The
self-history cut is the sharpest signal: today's net-directional premium is the
**most bearish in the name's last 49 available sessions (0.0 self-percentile)**,
on elevated total premium (72.9 self-percentile). So the put-heavy tape (P/C 1.36,
net flow −$595K) is real and unusual *for this name* — but the absolute dollar
magnitude is small, so tradeability/size should stay modest. CMPS's sector
(Healthcare/biotech) is lagging — it leads neither side of today's tape.

## Universe ranking

- **Net bullish premium:** CMPS outside top-50. Leaders: MU, NDX, SNDK, IBIT, SMH
  (semis + crypto leading the bullish tape). [CTX:screener_bullish]
- **Net bearish premium:** CMPS outside top-50. Leaders: SPX, PLTR, MSTR, MSFT,
  SPCX (index + mega-cap momentum being sold). [CTX:screener_bearish]
- **Volume-vs-average (≥2× filter):** CMPS outside top-50 → today's option volume
  is **below 2× its own 30-day average** (elevated but not an explosion).
  [CTX:screener_volume_vs_average]
- **Exact universe percentiles (DuckDB §C, today):**
  total_prem **83.2** · net_dir **3.4** · iv_rank **21.2** · vol_vs_avg **71.4**.
  [CTX:universe_pctile DUCKDB]

## Sector read

CMPS sector = **Healthcare** (full_name: COMPASS PATHWAYS PLC). Today's tape is led
on the long side by semiconductors/crypto (MU, SNDK, SMH, IBIT) and sold on the
index/mega-cap-momentum side (SPX, PLTR, MSTR, MSFT). Healthcare/biotech appears on
neither leaderboard → **sector lagging / mid-pack, not in favour**. The name being
a net-bearish outlier while its sector is simply quiet (not being actively sold as
a group) is a single-name story, not a sector rotation — phase-6 to resolve whether
biotech-specific or macro risk-off is the driver.

## Self-history (DuckDB §C, parquet present)

- **sessions_in_window: 49** (note the known non-contiguous gap 2026-03-27→04-27;
  N is *available* sessions, not a contiguous calendar window).
- **self_pctile_net_dir: 0.0** — today is the **single most net-bearish day** for
  CMPS across those 49 sessions. [CTX:self_pctile DUCKDB]
- **self_pctile_total: 72.9** — total premium elevated for the name (top ~27%).
- Read: not big-numbers-on-a-busy-name; this is an outlier *bearish* premium day for
  CMPS specifically.

## Source

CLI (`uw screener` ×3 + `uw insights deep-dive`) **+ DuckDB §C** (universe &
self-history percentiles; local parquet present for 2026-06-18). "Outside top-50"
recorded on all three screener metrics (absolute-dollar leaderboards dominated by
indices/mega-caps); the DuckDB percentiles supply the exact cross-sectional read.

## Verdict for downstream

```
universe_pctile_total_prem:  83.2
universe_rank_net_dir:       outside top-50 (abs $); universe pctile_net_dir = 3.4 (extreme net-bearish)
sector_leadership:           HEALTHCARE lagging — leads neither side of tape today
iv_rank:                     20.35            # from insights_deep_dive (universe pctile 21.2)
implied_move_pct:            4.14%            # implied_move_perc 0.04145; feeds phase-9 expected-move (N4)
self_pctile_net_dir:         0.0              # most bearish in 49 available sessions
self_pctile_total:           72.9
unusual_verdict:             GENUINELY_UNUSUAL (bearish-skewed; small absolute $ → modest tradeability)
```

- **Bias from this phase:** context-only (no directional bias set), but the
  *unusualness* is on the bearish side — flag for phases 1–2.
- **Conviction:** n/a (context phase)
- **Three things later phases should remember:**
  1. Net-directional flow is the most bearish day for CMPS in 49 sessions
     (self_pctile_net_dir 0.0; universe pctile 3.4) — confluence should not be
     capped as "busy-name-normal-day"; the direction is genuinely unusual.
  2. Absolute net $ is small (−$595K) and vol-vs-avg < 2× → tradeability modest;
     keep size honest regardless of how clean the skew looks.
  3. IV rank is LOW (20.35 / 21.2 pctile) despite high absolute IV (iv30d 93.8%) —
     long-premium structures are not being penalised by elevated IV rank.
- **Open questions:** Is the bearish skew a directional bet or hedging/put-selling?
  (phase-1 aggressor split + phase-3 OI to resolve.) Single-name idiosyncratic vs
  biotech-group risk-off? (phase-6.)
