# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** PDD
**As-of date:** 2026-05-26
**Generated:** 2026-05-26T20:18:00Z
**Upstream phases cited:** phase-0-intake.md

## Summary

PDD is a **big options name having an earnings-eve day, not a directional
standout.** Universe-wide it sits in the **top 2.5% by total option premium**
($31.27M today, 97.5th pctile of ~6,171 optionable names) — so it is always a
heavily-traded name; raw size is not a signal here. But on **net-directional
premium it is outside the top-50 leaders** (today's tape is led by semiconductors —
MU, AMD, SNDK, SMH — not China consumer). The elevation in PDD's own activity is
**earnings-driven, not conviction-driven**: PDD reports **tomorrow, 2026-05-27**
(`next_earnings_date`), IV rank is 76.5 (90th pctile of its own history), option
volume 130,284 is ~2–3× its recent daily (~45K) and 93rd pctile of its own
sessions, yet net-directional flow is only **+$1.12M bullish** (77th pctile self)
against $31M of total premium — a mild, inconsistent tilt. **Verdict:
BUSY_NAME_NORMAL_DAY** (earnings vol/volume ramp), which caps phase-1/2 confluence
at `+` not `++`. Treat this entire workup as a **binary earnings event study**, not
a clean accumulation setup.

## Universe ranking (today, 2026-05-26)

- **Net bullish premium (`screener_bullish_bearish` direction=bullish, top-50):**
  PDD does **not** appear. Lowest qualifying name is CVX at net_flow +$3.57M; PDD's
  bullish−bearish net is only +$1.12M [CTX:universe_rank_net_dir]. → outside top-50.
- **Net bearish premium (top-50):** PDD does **not** appear either (it is net
  *bullish*, just mildly). → not a bearish leader.
- **Volume-vs-average (top-50):** PDD does **not** appear; that list is dominated by
  illiquid micro-caps with absurd ratios (ARXS 293×, etc.) and is uninformative for
  a mega-ADR. Self-history (below) is the cleaner volume read.
- **Leaders today (single names):** MU (+$224.7M, iv_rank 100), SNDK (+$138M), META
  (+$77.6M), ASTS (+$63M), AMD (+$45.3M). **Semiconductors / memory dominate the
  bullish tape.** Bearish leaders: NVDA (−$100.2M — semis two-sided), GLD, GOOGL/GOOG,
  BE, MSFT.

## Sector read

- PDD is **Consumer Cyclical** (China e-commerce ADR — Pinduoduo domestic + Temu
  global). Its sector is **not** leading today's directional tape; **semiconductors
  lead** decisively. China/EM-adjacent proxies show a *mild* bid — EEM net +$8.94M,
  FUTU (China broker) net +$7.77M — so the China complex is modestly in favour, but
  PDD itself is mid-pack. This is a **yellow flag** the macro phase (phase-6) should
  resolve: name mildly bid, sector not a leader, broad tape risk-on in semis.

## Self-history (DuckDB §C — local parquet present, N=32 sessions)

Across PDD's own 32 available sessions (mind the §gap: 2026-03-28→04-24 absent):

| Metric | Today's value | Self-percentile |
|--------|---------------|-----------------|
| Total option premium | $31.27M | **83.9** [CTX:self_pctile DUCKDB] |
| Net-directional premium | +$1.12M | **77.4** [CTX:self_pctile DUCKDB] |
| Total option volume | 130,284 | **93.5** [CTX:self_pctile DUCKDB] |
| IV rank | 76.5 | **90.3** [CTX:self_pctile DUCKDB] |

Universe percentiles today [CTX:universe_pctile DUCKDB]: total premium 97.5, net-dir
97.5 (≈rank 150 of ~6,171 — high pctile but outside the top-50 *leaders* because the
universe tail is tiny), iv_rank 91.6.

**Recent tape (last 14 sessions):** spot ranged $94.52–$102.31; today $96.58 sits
**mid-range**. Net-directional flow has been **choppy and slightly net-bearish** over
two weeks (05-22 −1.55, 05-21 −1.64, 05-18 −2.73, 05-15 −4.33, 05-14 −2.31, 05-12
−3.24) with bullish pockets (05-20 +1.89, 05-19 +1.57, 05-06 +2.81). Today's +$1.12M
is a mild bullish nudge into the print, not the continuation of an accumulation
trend. IV rank has ramped from ~65 (05-22) to 76.5 — the classic pre-earnings vol
bid.

## Source

MCP (`insights_deep_dive`, `screener_bullish_bearish` ×2, `screener_volume_vs_average`)
+ DuckDB escape-hatch §C (universe + self-history percentiles; local snapshot present
for 2026-05-26). No metrics unavailable; the volume-vs-avg universe percentile from
§C (96.7) was discarded as misleading (denominator is *stock* avg volume, not
options) in favour of the self-history volume percentile (93.5).

## Verdict for downstream

```
universe_pctile_total_prem:  97.5
universe_rank_net_dir:       outside top-50 (≈rank 150 / 6,171 by net_call−net_put; +$1.12M bullish−bearish)
sector_leadership:           Consumer Cyclical / China-EM MID-PACK today (semis lead the tape; EEM/FUTU mildly bid)
iv_rank:                     76.5
implied_move_pct:            5.69        # straddle-implied move for the earnings event (feeds phase-9 N4)
self_pctile_net_dir:         77.4
unusual_verdict:             BUSY_NAME_NORMAL_DAY
```

- **Bias from this phase:** neutral (context only — sets no direction).
- **Conviction:** n/a (context phase).
- **Three things later phases must remember:**
  1. **EARNINGS TOMORROW (2026-05-27).** This dominates everything: phase-5 must pull
     historical earnings reactions, phase-9 must treat vol-crush + the 5.69% implied
     move as the core risk, and any structure must be earnings-aware (long premium
     bleeds into a known IV crush).
  2. **BUSY_NAME_NORMAL_DAY** → phase-1/2 confluence capped at `+`. The flow is a
     pre-earnings vol/volume ramp, not directional accumulation; net tilt is only
     mildly bullish and the two-week tape is choppy/net-bearish.
  3. Spot **$96.58**, mid of a $94–102 month range; IV rank 76.5 (90th pctile self);
     implied move ±5.69% (~±$5.50). Use these as the reference frame for every level.
- **Open questions for later phases:** Is the mild call tilt today genuine directional
  positioning or just earnings lottery-ticket/hedging (phase-1)? Does dark pool show
  accumulation under the print (phase-2)? How has PDD historically reacted to earnings
  and how does realized compare to the 5.69% implied (phase-5)?
