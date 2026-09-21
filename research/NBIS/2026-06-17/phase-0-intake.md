# Phase 0 — Intake

**Ticker:** NBIS (Nebius Group NV)
**As-of date:** 2026-06-17
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/NBIS/2026-06-17
**Version:** v1 (first run for this date; prior dated run exists at research/NBIS/2026-06-05/)
**Generated:** 2026-06-18T00:19:32Z

## Summary

Ticker validated (NBIS = Nebius Group NV, Technology / Software-Infrastructure). Output
directory created, empty → v1. UW CLI reachable; all five datasets (options, darkpool, oi,
screener, hotchains) carry data through the as-of date 2026-06-17. NBIS has heavy options
activity. **Headline from the intake drift vs the 2026-06-05 prior run: the stock has ripped
+23% in 12 sessions ($227.81 → $280.91) and now trades ABOVE its $255.29 consensus analyst
target, +126.7% above its 200-day MA, RSI 68.6, P/E 93.7, on a 21.9% short float.** This is a
crowded, momentum-extended, heavily-shorted AI-infra name — every later phase should read the
flow against that "already-run, above-target, high-short" backdrop. Proceeding to phase 0.5.

## UW availability

- `uw historical available-dates`: ok (keys: darkpool, hotchains, oi, options, screener)
- Latest available options date: 2026-06-17 (as-of present ✓)
- Latest available darkpool date: 2026-06-17 (as-of present ✓)
- Latest available oi date: 2026-06-17 ✓ · Latest screener date: 2026-06-17 ✓

## Ticker sanity

- Options activity (unusual_volume top 1): NBIS 2026-08-21 $400 PUT — total_premium $12,679,719,
  total_volume 933, open_interest 4, vol_oi_ratio 233.25, avg_iv ≈ 115.2%.
  → Options are highly active and IV is very rich; thin-options note NOT triggered.

## Local data (escape hatch / gap-awareness)

- `local_data_available`: yes · `duckdb_available`: yes
- `STOCKS_DIR`: /Users/ewan/Documents/Stocks
- Available local dates: 2026-03-13 → 2026-03-27, then **GAP**, 2026-04-27 → 2026-06-17
  (contiguous trading days within each block). Gap flagged: **yes** (2026-03-27 → 2026-04-27,
  ~1 month missing). As-of date 2026-06-17 IS present locally.
- Note: the `uw` CLI is primary; local DuckDB is opt-in for cuts the CLI can't express
  (lib/duckdb-cuts.md). The gap matters only for long self-history percentiles (phase-0.5/5).

## Finviz augments (`fz`)

- `fz_available`: yes
- `Shs Float`: **202.00M** (Shs Outstand 220.41M; Short Float **21.93%**) — carried to
  phase-2/3 for %-of-float normalization and to phase-7c as the SI gate input.
- Note: `fz` supplements SI/float/peer/breadth only (lib/fz-recipes.md); downside-only/advisory.

## Prior versions

No prior version for **this date** (2026-06-17 dir was empty → v1). A full prior dated run
exists at `research/NBIS/2026-06-05/` (12 days earlier). `fz quote-drift --since 2026-06-05`
returned 40 moved fields; the material ones:

| Field | 2026-06-05 | 2026-06-17 | Δ | Read |
|-------|-----------|-----------|---|------|
| Price | 227.81 | **280.91** | +53.10 (+23.3%) | parabolic 12-day rip |
| Perf YTD | 172.16% | **235.60%** | +63.4pp | extreme momentum |
| 52W High dist | −18.30% | **+0.74%** | — | at/above 52W high |
| SMA200 dist | +94.45% | **+126.65%** | +32.2pp | extreme extension |
| RSI (14) | 56.12 | **68.57** | +12.45 | nearing overbought |
| P/E | 76.01 | **93.72** | +17.71 | multiple expansion |
| Target Price | 252.43 | 255.29 | +2.86 | **price now ABOVE target** |
| Short Float | 22.43% | 21.93% | −0.50pp | marginal cover into the rip |
| Short Ratio | 2.54 | 2.49 | −0.05 | still a crowded short |
| Beta | 4.34 | 4.28 | −0.06 | very high beta |
| ATR(14) | 22.26 | 24.29 | +2.03 | widening range |

This drift is context for phases 0.5 / 5 / 7c / 8b: the easy money may already be made; the
flow now has to be read against a name that has overrun consensus on a heavy short base.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|------------------|--------------------------|-----------|
| `uw historical available-dates --json` | keys=[darkpool,hotchains,oi,options,screener]; latest options/dp/oi/screener = 2026-06-17 ← `.options[]\|sort\|tail` | all |
| `uw options-flow unusual-volume --symbol NBIS --top-n 1 --date 2026-06-17 --json` | $400P prem=$12.68M, vol_oi=233.25, avg_iv=1.152 ← `.results[0]` | top-1 |
| `ls "$STOCKS_DIR/Stock Screener/"` | 48 local dates, gap 03-27→04-27 ← filename parse | all |
| `fz quote NBIS --agent` | float=202.00M, short_float=21.93%, price=280.91 ← `.fundamentals` | 1 |
| `fz quote-drift NBIS --since 2026-06-05 --agent` | 40 fields moved; price +23.3%, now > target ← `.[]` | all |

## Tool errors

None — all green.

## DATA NOTE / CORRECTION

None — first reads stood and round-tripped through `jq`.

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake sets context, no bias — but flags an extreme-momentum / above-target / high-short backdrop).
- **Conviction:** n/a (intake).
- **Three things later phases should remember:**
  1. Price $280.91 is **above** the $255.29 consensus target and **+126.7%** over the 200-day — mean-reversion / exhaustion risk is structurally elevated; the contrarian and debate phases must weigh this.
  2. **21.9% short float / 2.49 short ratio** — squeeze fuel is real but partly spent; any bearish flow must be read as possible short-driven, any bullish flow as possible squeeze chase.
  3. Very high IV (avg ~115% on the front $400P) and beta 4.28 → option premium is expensive; structures (phase 4/9) should prefer defined-risk / spreads over naked long premium.
- **Open questions:** Is the current flow fresh institutional positioning or momentum/squeeze chase? (phases 1–4) Has the fundamental story re-rated enough to justify P/E 93.7? (phase 7b) How crowded is sentiment vs the 21.9% short? (phase 7c)
