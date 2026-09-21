# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** CMPS
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T00:00:00Z
**Upstream phases cited:** phase-0-intake.md

## Summary

CMPS is having a **genuinely unusual — but net-bearish-tilted — options day**, not
a quiet name and not a clean bullish accumulation. Total option premium ($1.427M)
sits in the **86.7th universe percentile** (top ~13% of 4,532 optionable names) and
the **86.7th percentile of the name's own 31-session history** — so activity is
elevated on both axes. *But the direction of that activity is the story:*
net-directional premium ranks in the **bottom 4.8% of the universe** and the
**bottom 3.3% of CMPS's own history** — i.e. CMPS is one of the most net-bearish
single names on the tape today. The headline July $13-call vol/OI of 12.8 (phase-0)
is **calls being net SOLD on the aggressor side** (`net_call_premium −$288.9k`), not
bought. IV rank is only **12.25** (bottom ~12% universe) — options are cheap for this
name, which argues against an imminent-catalyst vol bid. Sector context is a second
yellow flag: today's directional tape is led by Tech/semis + index, and Healthcare is
a laggard. Downstream phases should treat the high call *volume* skeptically and let
phases 1–2 resolve whether this is genuine bearish positioning or income/overwriting.

## Universe ranking (today, N = 4,532 optionable names) [CTX:universe_pctile DUCKDB]

| Metric | CMPS value | Universe percentile | Read |
|--------|-----------|---------------------|------|
| Total premium (call+put) | $1.427M | **86.7** | Elevated — active name today |
| Net-directional premium | **−$275.6k** | **4.8** | Bottom 5% — strongly net BEARISH aggressor flow |
| IV rank | 12.25 | **11.6** | Bottom ~12% — cheap vol for the name |
| Vol-vs-avg | (malformed*) | 83.7 | *Disregard — ratio mixes option contracts ÷ share avg vol |

- CMPS is **outside the top-50 on net bullish premium** (`screener_bullish_bearish`,
  direction=bullish) — the day's bullish-flow leaders are SPX/SPXW (index), AAPL
  (+$81M), TSLA (+$53M), DELL, IBM, GLD, ASTS, RKLB. CMPS does not appear.
- \*The `vol_vs_avg` field divides option contract volume by 30-day *share* average
  volume, so its raw value rounds to 0.0 and the 83.7 percentile is an artifact —
  **ignored**. Self-history vol_x (same units day-over-day) is the usable read below.

## Sector read

Today's directional leaderboard is dominated by **Technology / semiconductors**
(AAPL, DELL, IBM, MU, INTC, QCOM, ARM, SOXL, semis ETFs) plus index products.
**Healthcare is a laggard** — only LLY (#32, +$5.3M) and ABT (#40, +$4.0M) crack the
top-50, both modest. CMPS's sector is out of favour on the directional tape today.
This is a yellow flag for phase-6 to resolve: a name showing extreme *bearish* flow
inside a sector the market isn't bidding is internally consistent (no cross-current
to reconcile), but it also means there is no sector tailwind to lean on for any long.

## Self-history (CMPS own 31 available sessions) [CTX:self_pctile DUCKDB]

| Metric | Self percentile | Read |
|--------|-----------------|------|
| Net-directional premium | **3.3** | Today is among the most net-bearish days in the window |
| Total premium | **86.7** | Today's $ activity is high for the name |
| Vol-vs-avg (self) | 90.0 | Option volume elevated relative to the name's own recent days |

Recent series (note the **05-21 → 05-22 directional flip**):

| date | tot_prem ($M) | net_dir ($k) | iv_rank | close |
|------|--------------|-------------|---------|-------|
| 2026-05-22 | 1.427 | **−275.6** | 12.25 | 11.81 |
| 2026-05-21 | 2.532 | +552.8 | 15.10 | 11.59 |
| 2026-05-20 | 0.670 | +186.6 | 11.59 | 10.87 |
| 2026-05-19 | 0.492 | +53.0 | 9.78 | 10.07 |
| 2026-05-18 | 1.463 | +452.5 | 10.54 | 10.56 |
| 2026-05-15 | 0.373 | +22.4 | 9.39 | 10.36 |
| 2026-05-14 | 1.503 | +134.9 | 8.33 | 10.62 |
| 2026-05-13 | 1.071 | +327.0 | 9.25 | 10.96 |
| 2026-05-12 | 0.325 | −73.0 | 12.56 | 9.37 |

**Read:** the prior 9 sessions were predominantly **net-bullish** flow into a stock
that rallied from $9.37 (05-12) to $11.81 (05-22), +26% in eight sessions. Today is
the first sharp **net-bearish** print of the run, on the highest-percentile activity
day — i.e. a possible distribution / profit-taking flip at the top of a fast move,
**or** systematic call-overwriting after a +26% run. Phases 1–4 must distinguish.
(Gap note from phase-0: the 31-session window is non-contiguous — it skips
2026-03-28→04-24 — but the last 12 sessions shown are contiguous, so the run read is clean.)

## Source

MCP (`insights_deep_dive`, `screener_bullish_bearish`, `screener_volume_vs_average`)
+ **DuckDB escape hatch §C** (`lib/duckdb-cuts.md`) for exact universe & self-history
percentiles, since the MCP returns ranked top-N only and CMPS fell outside top-50 on
net direction. Local snapshot for 2026-05-22 present; percentiles over N=4,532 names
(universe) and N=31 sessions (self, non-contiguous).

## Verdict for downstream

```
universe_pctile_total_prem:  86.7
universe_rank_net_dir:       outside top-50 bullish (net_dir pctile 4.8 = bottom 5%, NET BEARISH)
sector_leadership:           Healthcare is LAGGING today (tape led by Tech/semis + index)
iv_rank:                     12.25
implied_move_pct:            13.95   # implied_move 1.65 on $11.81 close — feeds phase-9 N4
self_pctile_net_dir:         3.3
self_pctile_total:           86.7
unusual_verdict:             GENUINELY_UNUSUAL (bearish-tilted — elevated premium, extreme net-bearish direction, cheap IV)
```

- **Bias from this phase:** context-only (no directional bias set), but flagging that
  the *unusualness is bearish-direction* — high call volume is net-SOLD, not bought.
- **Conviction in the context read:** 4/5 (two independent percentile sources agree).
- **Three things later phases should remember:**
  1. Premium activity is genuinely elevated (top ~13% univ, 87th self) — this is a
     real signal day, not noise. **But the aggressor flow is net bearish** (bottom 5%
     univ / bottom 3% self). Do not read the July $13 vol/OI 12.8 as bullish.
  2. The stock just ran **+26% in 8 sessions** ($9.37→$11.81) on net-bullish flow;
     today is the first net-bearish flip at the high → test distribution-vs-overwrite.
  3. IV rank 12.25 (cheap) + Healthcare lagging the tape → no vol bid, no sector
     tailwind. Any long thesis must stand on the name alone; longs have negative carry
     working *for* them (cheap options) but no momentum confirmation today.
- **Open questions for phases 1–4:** Is today's net-bearish print (a) profit-taking /
  distribution after the run, (b) systematic call-overwriting (income, not a bet on
  downside), or (c) genuine bearish initiation? The aggressor split, sweep character,
  and OI changes (calls sold-to-open vs closed) resolve this.
```
