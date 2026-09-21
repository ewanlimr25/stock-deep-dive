# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** ADBE
**As-of date:** 2026-05-29
**Generated:** 2026-05-30T19:50:00Z
**Upstream phases cited:** phase-0-intake.md

> **Within-run correction.** An earlier draft of this file recorded the DuckDB
> §C percentile cut as "transport-stalled → skipped" and set the verdict to
> `BUSY_NAME_NORMAL_DAY`. The DuckDB output had only been *buffered*; it
> subsequently returned and is now incorporated below. The corrected verdict is
> **GENUINELY_UNUSUAL (directional)**. No `-v2` was created because this is the
> same run and the prior content was provisional/incomplete, not a re-run.

## Summary

ADBE's tape on 2026-05-29 is **directionally unusual** — this is the **most
net-bullish session for ADBE in its entire available 35-session window**
(`self_pctile_net_dir` **100.0** [CTX:self_pctile DUCKDB]) and it sits in the
**99.6th percentile of the whole optionable universe on net-directional premium**
([CTX:universe_pctile DUCKDB], `net_flow` +$12.27M, rank **#23** of ~6,000
names). The one dimension that is *not* a blowout is **turnover**: ADBE sits at the
**96th universe percentile** on the option-activity-vs-average metric
[CTX:vol_vs_avg DUCKDB] yet is **outside the CLI volume-vs-average top-50** —
that board is dominated by mis-scaled microcap ratios (e.g. SCSC 2233×), so a
large optionable name rarely surfaces there; in absolute terms today's **81,787
option contracts** (55,718 calls / 26,069 puts) is a normal-to-elevated session,
not a turnover blow-off.
So the unusualness is in the **direction/conviction of the flow, not the raw
volume** — exactly the kind of signal phase-0.5 exists to confirm rather than a
"busy name having a normal day." IV rank is pinned at **100** (97.2 pctile),
the standard pre-earnings vol ramp (earnings **2026-06-11**). **Verdict:
GENUINELY_UNUSUAL** — no phase-1/2 confluence cap applies, but size is still
disciplined by the pre-earnings IV-100 backdrop and the modest turnover.

## Universe ranking

- **Net bullish premium:** ADBE **#23** of the full universe, `net_flow`
  **+$12,273,462** (`bullish_premium` $36.93M − `bearish_premium` $24.65M)
  [CTX:universe_rank_net_dir]; **99.6th percentile** across all optionable names
  [CTX:universe_pctile DUCKDB]. Among **single names** (excluding indices/ETFs),
  effective rank ~#18–19.
- **Exact universe percentiles (DuckDB §C, whole universe today):**
  total premium **98.2**, net-directional **99.6**, IV rank **97.2**,
  volume-vs-avg **96.0** [CTX:universe_pctile DUCKDB].
- **Bullish board leaders (single names):** MSFT (+$136.0M), DELL (+$122.0M),
  ORCL (+$59.8M), PLTR (+$56.7M), NOW (+$46.3M), CRWD (+$43.2M) — all Technology.
- **Bearish board:** index hedging — SPXW (−$1.94B), SPX (−$318M), SPY (−$126M),
  ASTS (−$55M), GOOG (−$41M). **ADBE outside the bearish top-50** (consistent
  with its net-bullish lean).
- **Turnover:** ADBE **outside** the CLI volume-vs-average top-50 but **96th
  universe percentile** on option-activity-vs-average (DuckDB §C)
  [CTX:vol_vs_avg DUCKDB]. The CLI board is dominated by mis-scaled microcap
  ratios; ADBE's **81,787 contracts** is conviction-rich but **not a volume
  event** — read the directional signal, not a turnover spike. (The screener's
  `avg30_volume` field is share-based, so an absolute option vol/avg multiple is
  not cleanly derivable from it — only the cross-sectional percentile is used.)
- **IV rank:** ADBE **#9 in the universe**, `iv_rank` **100.0** [CTX:iv_rank] —
  options at the richest of their trailing 1-year range, the standard
  pre-earnings IV ramp.

## Sector read

ADBE is **Technology**, and Technology/software **leads today's bullish
directional tape** — the entire single-name bullish top is software/app-infra
(MSFT, DELL, ORCL, PLTR, NOW, CRWD). **Favourable sector backdrop**, but ADBE is
a **follower within a leading sector**, not the name driving it. Mild
cross-sectional tailwind for a long, not a confirmation. Phase-6 should resolve
whether the software bid is durable (`sector-flow-persistence`) and whether ADBE
is being bought *with* the group.

## Self-history (DuckDB escape hatch §C — 35 sessions, gap-aware)

| Metric | Today's self-percentile |
|--------|-------------------------|
| net-directional premium | **100.0** [CTX:self_pctile DUCKDB] |
| total premium | **79.4** [CTX:self_pctile DUCKDB] |
| sessions in window | **35** (spans the 2026-03-28→04-24 gap; not contiguous) |

Today is **the single most net-bullish day for ADBE** in the available window —
the decisive evidence that this flow is genuinely unusual for the name, not its
baseline. Total premium is high (79th) but not a record; combined with the 1.22×
turnover, the message is **"unusually one-sided, normally-sized"** flow.

## Source

CLI (`uw screener bullish-bearish` ×2, `volume-vs-average`, `iv-rank`,
`uw insights deep-dive`) **+ DuckDB §C** (exact universe + 35-session
self-history percentiles; snapshot `stock-screener-2026-05-29.parquet` present).
"Outside top-N" recorded for: bearish premium, volume-vs-average.

## Verdict for downstream — `[CTX:]` block

```
universe_pctile_total_prem:  98.2            # DuckDB §C
universe_rank_net_dir:       23              # of full universe; 99.6 pctile; ~18-19 among single names
sector_leadership:           TECHNOLOGY/SOFTWARE is leading the bullish tape today
iv_rank:                     100             # pre-earnings extreme (97.2 universe pctile)
implied_move_pct:            0.295           # front-expiry (2026-06-05) implied move, $0.766 abs
self_pctile_net_dir:         100.0           # DuckDB §C — most net-bullish day in 35-session window
unusual_verdict:  GENUINELY_UNUSUAL
```

**Notes for later phases:**
1. `unusual_verdict = GENUINELY_UNUSUAL` (directional) → **no confluence cap** on
   phases 1–2. BUT the unusualness is in *direction*, not *turnover* (1.22×) —
   phase-9 should still avoid sizing at the very top of the band.
2. The front-expiry implied move (0.295% / $0.77) is **tiny** because the front
   weekly (2026-06-05) expires **before** the 2026-06-11 earnings — phase-6/9
   must price the *earnings* expiry (2026-06-12+) separately; the front-week
   number badly understates event risk.
3. IV rank 100 = **rich options into earnings** → phase-5 VRP / phase-9 structure
   choice should lean defined-risk / spreads over naked long premium.
