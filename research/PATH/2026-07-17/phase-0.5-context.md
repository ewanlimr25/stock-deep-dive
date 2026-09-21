# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** PATH · **As-of:** 2026-07-17 · **Version:** v1
Cites: phase-0-intake.md (options+DP both anchor 2026-07-17).

## Summary

PATH's options tape on 2026-07-17 is **QUIET**, not unusual. On a market where
the directional premium is dominated by index/semis (SPX +$1.62B, NDX +$400M,
NVDA +$82M bullish; SPY −$162M, QQQ −$72M, SMH/SOXX/MU bearish), PATH does not
appear in the top-60 net-bullish **or** top-60 net-bearish list, and is outside
the top-80 on volume-vs-average. Its own book is near-balanced: bullish premium
$2.17M vs bearish $1.98M (net **+$0.18M**), with put premium ($2.53M) slightly
exceeding call premium ($2.35M) even though call *volume* (27.0k) is nearly 2×
put volume (14.9k) — small, cheap OTM call lottery tickets against a bit of
heavier put premium. IV rank is mid (44.5). The one thing that is **not** quiet
is the dark-pool footprint ($267M notional / 22.0M shares / 2,226 prints at
avg $12.14) and a concentrated Nov-16C open-interest build (+4,255) — both
flagged for phases 2 & 3 to size properly. Bottom line: treat single clean
prints with restraint; this is a low-tradeability options day for the name.

## Universe ranking (single names, ETFs set aside)

- **Net bullish premium:** PATH **outside top-60** (leaders: NVDA +$81.6M,
  CDNS +$55.4M, SNDK +$42.7M, META +$35.1M, BE +$20.7M — semis/AI-infra led).
- **Net bearish premium:** PATH **outside top-60** (leaders after ETFs:
  MU −$29.4M, NFLX −$20.0M, IONQ −$19.4M — semis two-sided, IONQ = the day's
  quantum/AI-adjacent sell).
- **Volume-vs-average:** PATH **outside top-80** (leaders are illiquid micro-caps
  REGL/SRL/PSK with 100–1200× spikes — noise, not comparable). PATH's option
  volume is *not* unusually elevated vs its own 30-day average.

## Sector read

PATH is **Technology / software-automation (AI/RPA)**. Today's directional tape
was led by **semiconductors & AI-infrastructure** (NVDA, CDNS, SNDK bullish;
MU, SMH, SOXX bearish — two-sided semis) and **index hedging** (SPY/QQQ puts).
Application/enterprise software — PATH's actual group — is **not** a leadership
sector today. So PATH is a lagging-group name on a day when capital is
concentrated up-cap in silicon, not down in software. Yellow flag for phase-6:
any PATH-specific strength would be swimming against its sector's non-leadership.

## Self-history

Not computed via DuckDB this pass (CLI-rank-only). Local screener parquet for
2026-07-17 IS present (phase-0), so a precise self-percentile is available if a
later phase needs it; the CLI ranking (outside top-60 net-dir, outside top-80
vol-vs-avg) already places today firmly mid/low for the name, so
`self_pctile_net_dir` is left null rather than asserted.

## Source

CLI-only (`uw screener bullish-bearish` ×2, `uw screener volume-vs-average`,
`uw insights deep-dive --symbol PATH`), all `--date 2026-07-17`. "Outside top-N"
recorded on net-bullish, net-bearish, and volume-vs-average — information, not
error. DuckDB self-history percentile skipped (additive only; verdict already
clear).

## Verdict for downstream

```
[CTX:]
universe_pctile_total_prem:  null            # CLI-rank-only; PATH outside top-60/80 on all ranked metrics
universe_rank_net_dir:       outside top-60  # both bullish and bearish lists
sector_leadership:           TECH/SOFTWARE is lagging today (semis + index lead the tape)
iv_rank:                     44.5
implied_move_pct:            1.13            # implied_move_perc 0.0113 (near-term); feeds phase-9 N4
self_pctile_net_dir:         null            # parquet present but not queried; CLI rank already mid/low
unusual_verdict:             QUIET
```

**Downstream effect:** per `rubrics/confluence-scoring.md`, a QUIET verdict keeps
options-flow conviction low regardless of how clean an individual print looks;
phases 1–2 confluence is capped (no `++` from a thin tape). The two exceptions to
watch and size in later phases are (a) the $267M dark-pool block [phase 2] and
(b) the Nov-16C OI build of +4,255 [phase 3] — genuine footprints on an otherwise
quiet options day. Earnings are 2026-09-03 (≈7 weeks out) — not in a short trade
window but inside a multi-week swing horizon; phase-7c/9 must treat any Aug/Sep
option as earnings-exposed.
