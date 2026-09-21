# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** NOW
**As-of date:** 2026-07-17
**Generated:** 2026-07-19 (run) for as-of 2026-07-17
**Upstream phases cited:** phase-0-intake.md

## Summary

NOW is a **big-premium name having a quiet, high-IV pre-earnings day** — the flow
is **not genuinely unusual**. Its *absolute* option premium is top-of-universe
(98.6th pctile total premium, 99.0th pctile net-directional across 6,298 names),
which is normal for a mega-cap that always trades size — but its **volume is below
average** (vol/avg30 = **0.59**, 40.9th pctile universe / 25.0th pctile self) and
total premium sits at only the **17.6th pctile of NOW's own recent history**. The
one dominant fact is **IV rank 96.9** with **earnings on 2026-07-22 (5 calendar
days out)** — this is an event-vol build, not a directional-flow surge. Net premium
is mildly bullish (+$2.21M) but mid-pack for the name (64.7th self pctile).
**unusual_verdict = BUSY_NAME_NORMAL_DAY.** Phases 1–2 confluence capped at `+`.

## Universe ranking (as-of 2026-07-17)

- **Net bullish premium:** NOW = **+$2.21M** → **outside CLI top-50** (leaders below),
  but **99.0th universe pctile** (rank ≈ 63 of 6,298 — most names cluster near zero).
- **Total premium:** **$40.7M** → **98.6th universe pctile** (genuinely a large
  premium name in absolute terms).
- **Volume vs 30-day average:** **0.59×** → **40.9th universe pctile** — NOT a volume
  spike; below the median name. (`uw screener volume-vs-average --min-ratio 2` did
  not list NOW → outside that top-60.)
- **Bearish premium:** NOW outside CLI top-50.

**Today's directional leaders (single names, net bullish premium):** NVDA $81.6M,
CDNS $55.4M, SNDK $42.7M, META $35.1M, DRAM $24.1M, BE $20.7M (index ETFs SPX
$1.62B / NDX $400M / SPXW $178M set aside per pitfall). **Semis + AI-infra lead the
tape; NOW is not among the day's directional leaders.**

## Sector read

Technology leads today's directional tape, but the leadership is concentrated in
**semiconductors / AI-infra** (NVDA, CDNS, SNDK, DRAM) and **META** — not
application software. NOW (Software - Application) is **in-sector-favour by label
but out of the leadership pocket**. Yellow flag handed to phase-6: is application
software lagging the AI-infra bid, and does that cap NOW's beta into a market rally?

## Self-history (DuckDB escape hatch, 68 local sessions)

- **Net-directional premium:** 64.7th self pctile — above its own median but not
  extreme.
- **Total premium:** **17.6th self pctile** — LOW for NOW; it has had far bigger
  premium days. `[… DUCKDB]`
- **Volume vs avg30:** 25.0th self pctile (0.59×) — a quiet-volume day for the name.
  `[… DUCKDB]`
- Net read: not a standout session on any self-referential axis; the elevated IV
  rank is doing all the work.

## Source

CLI (`uw screener bullish-bearish` × 2, `volume-vs-average`, `insights deep-dive`)
**+ DuckDB** universe & self-history percentiles (local parquet present for
2026-07-17; 68-session self window with the flagged 03-27→04-27 gap). `yahoo_fundamentals`
block in `insights deep-dive` returned null sector/price (non-blocking; price came
from phase-0 screener parquet = $103.24).

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` / SQL path | Rows used |
|------------------|--------------------------------|-----------|
| `uw screener bullish-bearish --direction bullish --top-n 50 --date 2026-07-17` | NOW outside top-50; leaders NVDA $81.6M… ← `.results[].net_flow` | top-50 |
| `uw screener bullish-bearish --direction bearish --top-n 50 …` | NOW outside top-50 ← `.results[]` | top-50 |
| `uw screener volume-vs-average --min-volume-ratio 2 --top-n 60 …` | NOW absent → vratio<2 ← `.results[]` | top-60 |
| `uw insights deep-dive --symbol NOW --date 2026-07-17` | iv_rank=96.90, put_call_ratio=0.632, bullish=$18.75M, bearish=$16.54M, total_oi=1,514,177, next_earnings=2026-07-22 ← `.uw_screener.*` | 1 |
| duckdb universe pctiles (6,298 names) | tot_prem 98.6th, net_dir 99.0th, vratio 40.9th ← percentile SQL | universe |
| duckdb self-history (68 sessions) | self net_dir 64.7th, tot_prem 17.6th, vratio 25.0th ← percentile SQL | 68 |

## Tool errors

None (all reads round-tripped through `jq`/DuckDB).

## DATA NOTE / CORRECTION

Apparent contradiction reconciled, not an error: CLI showed NOW "outside top-50" on
net bullish premium while DuckDB shows 99.0th universe pctile. Both true — the
universe (6,298 names) is heavily zero-clustered, so the 99th pctile lands at rank
≈ 63, just past the CLI's top-50 cut. Recorded as-is.

## Verdict for downstream — `[CTX:]` block

```
universe_pctile_total_prem:  98.6
universe_rank_net_dir:       ~63 of 6298 (99.0th pctile; outside CLI top-50)
sector_leadership:           TECH leading tape BUT via semis/AI-infra; app-software NOW lagging pocket
iv_rank:                     96.9
implied_move_pct:            0.49%   # DAILY straddle-implied (insights implied_move_perc); earnings-window move is larger — phase-9 must recompute the event straddle
self_pctile_net_dir:         64.7
unusual_verdict:             BUSY_NAME_NORMAL_DAY
```

**Three things later phases must remember:**
1. **EARNINGS 2026-07-22 (5 days out); IV rank 96.9.** This dominates. Every phase
   is really reading a *pre-earnings* tape. Cross-check the earnings date (phase-7b/7c)
   — UW's `next_earnings_date` can be stale.
2. **Flow is a busy-name normal day, not unusual** — cap phases 1–2 confluence at `+`;
   volume is *below* average (0.59×). Don't over-read single prints.
3. **NOW is outside the day's directional-leader pocket** (semis/AI-infra lead) —
   phase-6 must resolve whether app-software lag caps NOW's upside beta.
