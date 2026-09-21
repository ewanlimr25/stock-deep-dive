# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** NOW
**As-of date:** 2026-05-27
**Generated:** 2026-05-28T12:12:00Z
**Upstream phases cited:** phase-0-intake.md

## Summary

NOW's flow is **genuinely unusual on direction but not on volume.** Across the
full optionable universe (N=4,598 today) NOW sits in the **top 1% on
net-directional premium** (99.4th pctile — the absolute #29 name on net bullish
flow) and **84th pctile on IV rank**, while its option *volume* is only **0.9× its
own 30-day average** (universe 64.8th pctile; 87.5th vs its own thin history).
Net flow is decisively call-tilted (call premium $59.4M vs put $17.2M, ~3.4:1;
P/C 0.284). The read: **steady directional call accumulation, not a news-driven
volume blowout.** That is a *cleaner* signal for an accumulation thesis than a
one-day spike, but it means downstream phases must NOT claim a volume-confirmed
conviction event — the ≥2× volume prong of GENUINELY_UNUSUAL fails outright.

## Universe ranking (today, 2026-05-27)

**Net bullish premium leaderboard** (`screener bullish-bearish --direction bullish`):

| Rank | Ticker | net_flow ($) |
|------|--------|--------------|
| 1 | SPXW (index) | 111,416,860 |
| 2 | META | 61,658,704 |
| 3 | TSLA | 54,782,274 |
| 4 | ASTS | 32,514,573 |
| 5 | IREN | 30,774,398 |
| 6 | APP | 29,120,056 |
| **29** | **NOW** | **5,014,959** |

Read among *single names* (set SPXW aside): NOW is #28. On the top-50 leaderboard
it looks mid-pack, but **across all 4,598 names that is the 99.4th percentile** —
NOW is a genuine top-decile directional name, just dwarfed in absolute dollars by
the mega-cap leaders (META/TSLA at 10–12× NOW's net flow).

**Volume vs average:** NOW is **outside the top-50** and its raw ratio is **0.9×**
(`total_volume` 24.56M vs `avg30_volume` 27.36M). No volume expansion. The
vol-vs-avg top-50 is entirely micro-cap noise (PRA 1620×, MBC 1583×) — irrelevant.

## Sector read

The tape is led by the **index (SPXW)** then a stock-pickers' mix: mega-cap tech
(META), auto/AI (TSLA), space/telecom (ASTS), crypto-miners (IREN), ad-tech (APP).
There is **no single clean sector sweep** — enterprise-software/tech is
*participating* (META bid, NOW top-1%) but is not the singular leader. NOW's
strength is **name-specific**, not a sector wave lifting all software. Hand to
phase-6: confirm whether software/XLK breadth supports the single-name bid or
NOW is leading a sector that's otherwise flat (the latter = a yellow flag).

## Self-history (DuckDB §C, N=33 sessions — spans the 2026-03-28→04-26 gap)

| Metric | Today's self-percentile |
|--------|-------------------------|
| net-directional premium | **81.3** |
| total premium | 62.5 |
| volume ratio | 87.5 |

Today's net-bullish tilt is the 81st percentile of NOW's own ≤33 available
sessions — elevated for the name, not a record. `sessions_in_window=33` is the
true N; the lookback is **two non-contiguous blocks** (mid-March + late-Apr→May),
not a calendar month — never annualize across it.

## Source

CLI rankings (`uw screener`, `uw insights deep-dive`) **+ DuckDB §C** exact
percentiles (`lib/duckdb-cuts.md`, parquet present for as-of). Volume-vs-average:
NOW outside CLI top-50, exact ratio 0.9× from local parquet.

## Verdict for downstream — `[CTX:]` block

```
universe_pctile_total_prem:  98.8        [CTX:universe_pctile DUCKDB]
universe_pctile_net_dir:     99.4        [CTX:universe_pctile DUCKDB]   # = rank #29 / 4598
universe_rank_net_dir:       29          [CTX:rank]                     # #28 among single names
sector_leadership:           SOFTWARE/TECH participating, NOT sole leader (index-led tape)
iv_rank:                     63.07       [CTX:iv_rank]                  # 84th universe pctile
implied_move_pct:            4.07        [CTX:implied_move]             # $4.15 on ~$102 → feeds phase-9 N4
self_pctile_net_dir:         81.3        [CTX:self_pctile DUCKDB]
self_pctile_vol:             87.5        [CTX:self_pctile DUCKDB]
vol_vs_avg_ratio:            0.90        [CTX] # BELOW average — NO volume spike
vol_confirmed:               NO          # ≥2x prong of GENUINELY_UNUSUAL fails
unusual_verdict:  GENUINELY_UNUSUAL (DIRECTIONAL ONLY)
```

**Decision rule for downstream:** treat the *directional* signal as genuine
(top-1% net-bullish, 81st self-pctile, 3.4:1 call premium) — do NOT apply the
BUSY_NAME confluence cap to the *direction*. BUT because `vol_confirmed=NO`
(0.9× volume), phases 1–2 must NOT score this as a volume-confirmed blowout:
the volume dimension is neutral. Net effect — conviction can build on direction
+ structure, but a clean volume catalyst is absent (lower urgency / longer-fuse
setup). No earnings until 2026-07-22, so no near-term binary distorting the IV.
