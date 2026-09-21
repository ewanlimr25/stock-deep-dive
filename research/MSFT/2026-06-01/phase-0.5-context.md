# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** MSFT
**As-of date:** 2026-06-01
**Generated:** 2026-06-02T10:54:09Z
**Upstream phases cited:** phase-0-intake.md

## Summary

MSFT's flow today is **real but not anomalous — a strong day for a name that
trades like this routinely.** On *dollars* it is a top-5 directional name in the
whole market (net bullish +$81.2M, **99.9th universe percentile** on both total
and net-directional premium) and its sector — **Technology — is leading the
bullish tape** (the top-12 net-bullish names are almost entirely Tech). But the
two markers that separate a genuine anomaly from a busy mega-cap are *absent*:
option **volume is only the 74.9th universe percentile / not in the >2× pack**,
and today's net-directional flow is the **77.1st percentile of MSFT's own 36
recent sessions** — elevated, but below the 80th-pctile "unusual-for-the-name"
bar. Verdict: **BUSY_NAME_NORMAL_DAY** → phases 1–2 confluence is capped at `+`
(not `++`) per `rubrics/confluence-scoring.md`. The one genuinely notable feature
is the **call skew (P/C 0.256, call premium $1.39B vs put $265M)** — direction is
clean even if magnitude is normal.

## Universe ranking (today, 4,694 optionable names)

- **Net bullish premium rank: #5** — `net_flow` = **+$81,200,963**
  `[CTX:universe_rank_net_dir]`. Leaders ahead of MSFT (all Technology):
  | Rank | Ticker | Sector | net_flow |
  |------|--------|--------|----------|
  | 1 | NVDA | Technology | +$182.0M |
  | 2 | MU | Technology | +$149.9M |
  | 3 | SNDK | Technology | +$148.7M |
  | 4 | ADI | Technology | +$82.1M |
  | **5** | **MSFT** | **Technology** | **+$81.2M** |
  | 6 | NDX (index) | — | +$69.3M |
  | 7 | ORCL | Technology | +$60.1M |
- **Net bearish premium: outside top-50** — MSFT is *not* among the day's net
  sellers. The bearish tape is led by index hedges (SPX −$274.9M, SPXW −$64.7M,
  SPY −$45.2M) plus **TSLA −$107.2M, META −$98.7M, AAPL −$57.5M, TSM −$55.6M** —
  i.e. some mega-caps (AAPL/TSM/META) and Tesla are being sold while the
  semis + MSFT/ORCL/IBM cohort is bought.
- **Volume-vs-average (≥2×): outside top-50** — today's MSFT option volume is
  **not** a >2× anomaly; exact universe percentile **74.9** `[CTX:universe_pctile DUCKDB]`.
- **IV-rank (high mode): outside top-50**, yet MSFT's own `iv_rank` = **73.07**
  (87.3rd universe pctile `[CTX:universe_pctile DUCKDB]`) — elevated in absolute
  terms; just not in the top-50 most-elevated names of a 4,694 universe.

## Sector read

**Technology is leading today's directional (bullish) tape**, and within it the
semiconductor complex is the spearhead (NVDA, MU, SNDK, ADI, MRVL, ARM, LITE) with
software/large-cap Tech (MSFT, ORCL, IBM, DELL) riding alongside. MSFT is firmly
in the **in-favour** cohort. This is the strongest cross-sectional pattern: *name
strong while its sector leads the tape* — a green flag, not the name-strong/
sector-sold yellow flag. Hands phase-6 a head start: confirm whether the
semis-led Tech bid is a broad risk-on regime or a narrow AI-capex rotation, and
note the divergence where AAPL/TSM/META are being sold against the MSFT/semis bid.

## Self-history (parquet present — 36 sessions, **gap-aware**)

Today vs MSFT's own ≤36 *available* sessions (non-contiguous — the 2026-03-28→
04-24 hole means this is 36 available sessions, not a contiguous calendar window;
per `lib/duckdb-cuts.md §gap`):

| Metric | Self percentile | Read |
|--------|-----------------|------|
| net-directional premium | **77.1** `[CTX:self_pctile DUCKDB]` | elevated, **< 80** unusual-bar |
| total premium | 85.7 | elevated |
| iv_rank | 91.4 | high for the name |
| sessions_in_window | 36 | (gap-flagged) |

The 77.1 self-percentile on net direction is the decisive number: a genuine
anomaly would clear ~80; this is a busy-but-normal directional day for MSFT.

## Source

CLI (`uw screener` bullish/bearish/volume-vs-average/iv-rank, `uw insights
deep-dive`) **+ DuckDB §C** (exact universe + self-history percentiles, parquet
present for 2026-06-01). "Outside top-50" recorded for net-bearish, volume-vs-avg,
and high-IV-rank — information, not error.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq`/SQL path | Rows used |
|------------------|------------------------------|-----------|
| `uw screener bullish-bearish --direction bullish --top-n 50 --date 2026-06-01 --json` | rank #5, net_flow=+$81.2M ← `.results \| to_entries \| select(.value.ticker=="MSFT")` | top-50 |
| `uw screener bullish-bearish --direction bearish --top-n 50 --date 2026-06-01 --json` | MSFT outside top-50 ← `map(select(.ticker=="MSFT"))` | top-50 |
| `uw screener volume-vs-average --min-volume-ratio 2 --top-n 50 --date 2026-06-01 --json` | MSFT outside top-50 ← same | top-50 |
| `uw screener iv-rank --mode high --top-n 50 --date 2026-06-01 --json` | MSFT outside top-50 ← same | top-50 |
| `uw insights deep-dive --symbol MSFT --date 2026-06-01 --json` | iv_rank=73.07, implied_move_perc=0.0333, P/C=0.256, bull=$795.5M, bear=$714.3M ← `.uw_screener` | 1 |
| DuckDB §C universe | total/net-dir 99.9, iv 87.3, vol 74.9, N=4694 ← `PERCENT_RANK() … QUALIFY ticker='MSFT'` | universe |
| DuckDB §C self-history | net-dir 77.1, total 85.7, iv 91.4, N=36 ← self `PERCENT_RANK()` | 36 sessions |

## Tool errors

None. (First DuckDB attempt hit a Python nested-quote SyntaxError — fixed by
moving to a temp script with parameterized queries; the query itself never ran on
bad data, so no number is affected.)

## DATA NOTE / CORRECTION

None — all reported values round-tripped through `jq` (CLI) or returned from a
DuckDB DataFrame.

## Verdict for downstream — `[CTX:]` block (phases 1, 5, 9 read verbatim)

```
universe_pctile_total_prem:  99.9
universe_rank_net_dir:       5
sector_leadership:           Technology is LEADING the bullish tape today (semis-led)
iv_rank:                     73.07
implied_move_pct:            3.33
self_pctile_net_dir:         77.1
unusual_verdict:             BUSY_NAME_NORMAL_DAY
```

- **Bias from this phase:** neutral (context only — sets no directional bias).
- **Three things later phases should remember:**
  1. **BUSY_NAME_NORMAL_DAY** — dollars are top-decile (rank #5, 99.9 pctile) but
     volume is *not* anomalous (74.9 pctile) and self-net-dir is 77.1 (< 80).
     **Cap phase-1/2 confluence at `+`, not `++`.**
  2. **Direction is clean even though magnitude is normal**: P/C 0.256, call
     premium $1.39B vs put $265M, MSFT absent from the entire bearish top-50.
  3. **Sector tailwind is real**: Technology leads the tape (semis-led); MSFT is
     in-favour. But watch the AAPL/TSM/META-sold divergence for phase-6.
- **Open questions:** Is the Tech bid broad risk-on or a narrow AI-capex rotation
  (phase-6)? Is MSFT's $81M net-bullish concentrated in a few sweeps or broad tape
  (phase-1)? Is the elevated IV rank (73) a vol-buying setup or rich premium to
  fade (phase-4)?
