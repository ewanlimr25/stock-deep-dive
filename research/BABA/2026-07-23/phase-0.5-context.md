# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** BABA · **As-of:** 2026-07-23 · **Generated:** 2026-07-24
**Upstream:** phase-0-intake.md (options confirmed active; local parquet present → DuckDB §C ran)

## Summary

BABA is a **busy name having a fairly normal day for itself.** On raw size it is
huge — **98.7th universe percentile on total option premium** and **96.0th on
volume-vs-average** — so absolute dollars are large. But against its **own** 72-session
history the day is unremarkable: total premium only **56.3rd self-percentile** and net
direction **43.7th self-percentile** — mid-pack. Cross-sectionally the net-directional
flow sits at the **bearish extreme of the universe (1.5th percentile on
net_call−net_put premium)**, and premium-weighted flow is marginally net **bearish**
(bullish $23.50M vs bearish $25.18M → net −$1.68M). BABA is **outside the top-50 on net
bullish, net bearish, AND volume-vs-average** — it is not one of today's directional
leaders. Per the skill's rule, self_pctile_net_dir 43.7 (< 80) with high absolute-but-mid
self premium ⇒ **BUSY_NAME_NORMAL_DAY** — phases 1–2 confluence is **capped at `+`, not
`++`** (`rubrics/confluence-scoring.md`). Context only; sets no directional bias.

## Universe ranking (as-of 2026-07-23)

- **Net bullish premium:** BABA **outside top-50.** Leaders (single names, ETFs aside):
  MU (+$103.8M), DELL (+$33.6M), IBM (+$26.3M) — semis/enterprise-tech lead the bullish tape.
- **Net bearish premium:** BABA **outside top-50.** Leaders: TSLA (−$247.3M), LULU
  (−$72.0M), GOOGL (−$59.6M), plus GLD/QQQ hedging — mega-cap + China-adjacent (GOOGL) selling.
- **Volume-vs-average (≥2×):** BABA **outside top-50** on the ratio screen, yet its own
  DuckDB vol-vs-avg percentile is **96.0** — i.e. active for itself, but not among the
  day's most-unusual-vs-average names.

## Sector read

BABA's UW `sector` field is null (known-broken for this ADR — see
`[[data-source-workarounds]]`; treat sector rank as n/a from the CLI). Read by proxy:
today's tape is led **bullishly by semis/enterprise tech** (MU, DELL, IBM) and pressured
**bearishly by mega-cap growth** (TSLA, GOOGL, GOOG) with index/gold hedging (QQQ, GLD).
China-ADR / consumer-discretionary is **absent from both leader lists** → the group is
**lagging / mid-pack**, not in favour. A GOOGL-led mega-cap-growth sell is a mild yellow
flag for the macro phase (phase-6) to resolve re: China-ADR risk appetite.

## Self-history (DuckDB §C, parquet present)

Window = **72 available sessions** (2026-03-13→2026-07-23; note the **2026-03-28→04-24
gap** — N is *available* sessions, not a contiguous 3.5-month calendar span).

| Metric | Today's self-percentile |
|--------|------------------------|
| net-directional premium | **43.7** (mid-pack — not unusually bull or bear for BABA) |
| total premium | **56.3** (slightly above its own median) |

Universe percentiles today (DuckDB §C): total_prem **98.7**, net_dir **1.5**
(bearish extreme), iv_rank **66.8**, vol_vs_avg **96.0**.

## Source

CLI + **DuckDB §C** (universe + self-history percentiles; local screener parquet for
2026-07-23 present). "Outside top-50" recorded on all three CLI screens (bullish,
bearish, volume-vs-average).

## Verdict for downstream — `[CTX:]`

```
universe_pctile_total_prem:  98.7
universe_rank_net_dir:       outside top-50 (universe pctile 1.5 — bearish extreme)
sector_leadership:           China-ADR / consumer-disc LAGGING (BABA outside top-50 both dirs; tape led by semis bullish, mega-cap-growth bearish); UW sector field null
iv_rank:                     61.16   # raw (universe pctile 66.8)
implied_move_pct:            1.56    # implied_move_perc 0.01557 → feeds phase-9 expected move (N4)
self_pctile_net_dir:         43.7    # N=72 available sessions
unusual_verdict:  BUSY_NAME_NORMAL_DAY
```

## Tool calls (audit)

| Datapoint | Command | jq/SQL path |
|-----------|---------|-------------|
| BABA outside bull/bear/vva top-50 | `uw screener bullish-bearish/volume-vs-average --top-n 50 --date 2026-07-23` | `[.results[].ticker] \| index("BABA")` → null |
| bullish/bearish premium, PCR, iv_rank, implied_move | `uw insights deep-dive --symbol BABA --date 2026-07-23` | `.uw_screener.{bullish_premium,bearish_premium,put_call_ratio,iv_rank,implied_move_perc}` |
| universe + self percentiles | DuckDB §C (`lib/duckdb-cuts.md`) | `PERCENT_RANK()` over screener parquet(s) |
