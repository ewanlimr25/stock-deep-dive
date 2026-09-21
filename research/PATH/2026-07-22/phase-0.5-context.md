# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** PATH · **As-of:** 2026-07-22 · **Generated:** 2026-07-22
**Upstream:** phase-0-intake.md (§Ticker sanity — PATH options live, iv30d 0.675)

## Summary

PATH is having a **genuinely unusual day — and the unusualness is bearish.** Total
option premium sits in the **95.3rd universe percentile** (top ~5% of 4,556
optionable names) and the **85.7th percentile of PATH's own 71-session history**, so
this is a heavy-activity session, not background noise. But the *direction* is the
opposite of the leaders': PATH's net-directional premium is in the **1.4th universe
percentile** and the **1.4th percentile of its own history** — i.e. among the most
net-bearish names on the tape and one of PATH's most bearish days on record. Option
volume is elevated (82.2nd pctile vs its own 30-day average). The tape's leadership
is **Technology / semis** (NVDA, SNDK, AVGO, MU dominate the net-bullish ranking) —
PATH's own sector is *in favour*, yet PATH is being **sold within a bought sector**,
the classic name-weak/sector-strong yellow flag for phase 6 to resolve.

## Universe ranking (as-of 2026-07-22, single names)

- **Net bullish premium:** PATH **outside top-50**. Leaders (ex-index): NVDA
  (+$67.0M), SNDK (+$25.6M), AVGO (+$22.7M), SMH (+$18.9M ETF), MU (+$16.8M),
  DELL (+$11.8M), TSLA (+$10.9M), SMCI (+$10.5M).
- **Net bearish premium:** PATH **outside top-50** on the CLI list, but the exact
  DuckDB cut puts its net-directional premium at the **1.4th percentile** (≈ rank
  ~64 of 4,556 — just outside the CLI top-50, consistent with a modest −$1.6M net vs
  the mega-caps' tens of millions).
- **Volume vs 30-day average:** PATH **outside top-50** on the ≥2× CLI list, but
  DuckDB exact percentile = **82.2nd** — genuinely elevated turnover, just not a
  top-50 extreme.

## Sector read

Technology **leads** today's directional tape: **22 of the 50** net-bullish names are
Technology, with the semiconductor complex (NVDA/SNDK/AVGO/MU/SMH/LRCX/TSM/STX) the
clear engine. PATH (Technology · Software — Infrastructure) is in a **leading
sector but is itself being net-sold** — sector tailwind exists but is not flowing
into this name. Hands phase 6 a specific question: is PATH-specific weakness or a
software-vs-semis rotation *within* Tech?

## Self-history (local parquet present, n=71 sessions, 2026-03-13 → 2026-07-22)

- **self_pctile_net_dir: 1.4** `[CTX:self_pctile DUCKDB]` — today is among PATH's own
  most net-BEARISH sessions in the window.
- **self_pctile_total: 85.7** `[CTX:self_pctile DUCKDB]` — today's total option
  premium is high for PATH (top ~14% of its own history).
- N caveat: the 71 sessions are **non-contiguous** (21-session hole 2026-03-28 →
  2026-04-24); percentile is over available sessions, not a calendar window.

## Note on the aggressor/premium divergence (for phase 1)

Gross **call premium $4.16M** dwarfs **put premium $1.29M**, yet both the
bullish/bearish premium split (bull $1.66M < bear $3.26M) and the net-directional
percentile (1.4) read **net bearish** — implying calls are being **net sold**
(hit-bid) while puts are net bought. Phase 1 must resolve whether this is bearish
initiation, call overwriting/covered-call supply, or hedging.

## Source

CLI (`uw screener bullish-bearish` ×2, `volume-vs-average`, `uw insights deep-dive`)
**+ DuckDB §C** exact universe & self-history percentiles (local snapshot present for
2026-07-22). "Outside top-50" recorded on all three CLI lists; exact percentiles
supplied by the escape hatch.

## Verdict for downstream

```
[CTX:]
universe_pctile_total_prem:  95.3
universe_rank_net_dir:       ~1.4th pctile (extreme bearish; ~rank 64, just outside CLI top-50)
sector_leadership:           Technology is LEADING today — but PATH is net-SOLD within it (name-weak/sector-strong)
iv_rank:                     45.58
implied_move_pct:            4.70
self_pctile_net_dir:         1.4   (extreme bearish for the name's own history)
self_pctile_total:           85.7
unusual_verdict:             GENUINELY_UNUSUAL (bearish tilt)
```

## Tool calls (audit)

| Datapoint | Command | jq/SQL path |
|---|---|---|
| bull leaders / PATH rank | `uw screener bullish-bearish --direction bullish --top-n 50 --date 2026-07-22 --json` | `.results[].ticker / .net_flow` |
| bear rank | `uw screener bullish-bearish --direction bearish --top-n 50 --date 2026-07-22 --json` | `[.results[].ticker]|index("PATH")` |
| vol-vs-avg rank | `uw screener volume-vs-average --min-volume-ratio 2 --top-n 50 --date 2026-07-22 --json` | `[.results[].ticker]|index("PATH")` |
| PATH abs numbers | `uw insights deep-dive --symbol PATH --date 2026-07-22 --json` | `.uw_screener.{bullish_premium,bearish_premium,iv_rank,implied_move_perc,put_call_ratio,next_earnings_date}` |
| universe pctiles | DuckDB §C on `stock-screener-2026-07-22.parquet` | `PERCENT_RANK() OVER(ORDER BY tot/net_dir/iv_rank/vol_x)` |
| self-history pctiles | DuckDB §C over 71 screener parquets | `PERCENT_RANK()` QUALIFY date=as-of |

## Tool errors

<none>
