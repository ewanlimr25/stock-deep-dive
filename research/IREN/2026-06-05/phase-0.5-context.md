# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** IREN
**As-of date:** 2026-06-05
**Generated:** 2026-06-07T00:46Z
**Upstream:** phase-0-intake.md (UW ok, local snapshot 40 dates, fz float 324.15M)

## Summary

IREN's tape today is **genuinely unusual — on the bearish side**. Absolute
activity is near the top of the universe (total premium 99.1 pctile) but the
*direction* is the signal: net-directional premium sits at the **0.4 universe
percentile** (among the most net-bearish optionable names in the whole market)
and at the **0.0 self-history percentile** — the single most net-bearish
session for IREN in the 40 local sessions on disk. Both directional legs agree:
net call premium **−$23.14M** (calls being sold) and net put premium **+$1.14M**
(puts being bought). IREN ranks **#28 on the market-wide net-bearish-premium
screener** (net flow −$18.83M; bearish $91.2M vs bullish $72.4M) while being
**outside the top-50 bullish** list. The one leg that does NOT confirm is raw
volume-vs-average: IREN is outside the top-50 on the ≥2× screener — the
unusualness is directional, not volumetric (this is a perpetually busy options
name: 518k contracts, 2.46M total OI). Downstream phases should read bullish
prints skeptically against this backdrop.

## Universe ranking

- **Net bullish premium:** outside top-50. Leaders: SPX (+$2.40B), NDXP
  (+$73.8M), IWM (+$55.2M), STM (+$53.4M), NDX (+$43.5M), UTHR (+$18.8M).
- **Net bearish premium:** **IREN rank #28** — net_flow **−$18,832,787**
  (bearish_premium $91,205,132 vs bullish_premium $72,372,345; jq
  `.results[] | select(.ticker=="IREN")`). Leaders: SPXW (−$2.09B), QQQ
  (−$116.9M), SNDK (−$114.3M), SOXL (−$85.6M), NVDA (−$81.4M), TSLA (−$81.1M).
- **Volume-vs-average (≥2× screener):** outside top-50 (leaders are
  illiquid-name spikes: FCPT 5309×, IMCR 732×, …).
- **IV rank (high mode):** outside top-50 (leaders pinned at 100: MU, AIS,
  MRVL, SMH, SOXL). IREN iv_rank = 48.17 — mid-range.

## Sector read

UW's official label for IREN is **Financial Services** (legacy crypto-miner
classification; the name trades with the AI-datacenter/bitcoin-miner cohort,
i.e. semis-adjacent). Today's single-name bearish leader board is **dominated
by AI-hardware/semis being sold**: SNDK −$114M, SOXL −$85.6M, NVDA −$81.4M,
TSLA −$81.1M — and IREN at #28 sits inside that same sell-the-AI-complex tape.
Bullish single-name leaders (STM, UTHR) are scattered. Read: **IREN's trading
cohort is leading the bearish tape today** — the name is being sold *with* its
group, not idiosyncratically. Phase-6 should resolve whether this is a one-day
rotation or regime pressure.

## Self-history (DuckDB §C, 40 sessions, gap-aware)

- `self_pctile_net_dir` = **0.0** — today is the most net-bearish IREN session
  in the 40-session local window [CTX:self_pctile DUCKDB].
- `self_pctile_total` = **82.1** — busier than typical for the name, not extreme.
- `sessions_in_window` = 40 (window is non-contiguous: 2026-03-13…03-27 +
  2026-04-27…06-05; the 03-28→04-26 hole means this is 40 *available* sessions,
  not a calendar quarter).
- Components (screener parquet, jq/SQL): net_call_premium **−$23.14M**,
  net_put_premium **+$1.14M** → net_dir **−$24.28M** [CTX:universe_pctile DUCKDB].
- Caveat: §C `vol_x` (0.01; 94.2 pctile) divides options contracts by the
  *stock* avg30_volume — units quirk; treat as cross-sectional intensity rank
  only. The authoritative volume-vs-average read is the CLI screener (outside
  top-50).

## Source

CLI (`uw screener` ×4 + `uw insights deep-dive`) **+ DuckDB §C** (exact
universe + self-history percentiles). Outside-top-N metrics: bullish premium,
volume-vs-average ≥2×, IV-rank-high — all recorded above.

## Verdict for downstream

```
[CTX:]
universe_pctile_total_prem:  99.1          # DUCKDB §C
universe_rank_net_dir:       #28 on BEARISH screener; outside top-50 bullish
sector_leadership:           AI-datacenter/semis cohort is leading the BEARISH tape; IREN selling WITH its group (official label: Financial Services)
iv_rank:                     48.2          # insights deep-dive .uw_screener.iv_rank
implied_move_pct:            0.96%         # .uw_screener.implied_move_perc = 0.00963
self_pctile_net_dir:         0.0           # most bearish of 40 sessions; DUCKDB
unusual_verdict:  GENUINELY_UNUSUAL        # bearish direction — NOT volumetric
```

**Nuance for phases 1–2:** the GENUINELY_UNUSUAL verdict is *directional*
(net-dir 0.4 universe pctile + 0.0 self pctile, mirror of the ≥80 bullish bar);
the volume-vs-average ≥2× leg is NOT met. The unusualness is *which way* the
premium leans, not how much of it there is. A bullish thesis from later phases
must overcome this cross-sectional bearish skew; a bearish thesis is
flow-confirmed but crowded-trade checks (phase 7c) matter more than usual.
Close $54.35; next earnings 2026-08-27 (far — no earnings gravity in the
2-week window).

## Tool calls

| Command | jq/SQL path | Result |
|---|---|---|
| `uw screener bullish-bearish --direction bullish --top-n 50 --date 2026-06-05 --json` | `.results[] ticker match` | IREN outside top-50 |
| `uw screener bullish-bearish --direction bearish --top-n 50 --date 2026-06-05 --json` | `.results[27]` | rank #28, net_flow −18,832,787 |
| `uw screener volume-vs-average --min-volume-ratio 2 --top-n 50 --date 2026-06-05 --json` | ticker match | outside top-50 |
| `uw screener iv-rank --mode high --top-n 50 --date 2026-06-05 --json` | ticker match | outside top-50 |
| `uw insights deep-dive --symbol IREN --date 2026-06-05 --json` | `.uw_screener` | P/C 0.91, iv_rank 48.17, implied_move_perc 0.00963, tot OI 2,459,547 |
| DuckDB §C universe percentile | PERCENT_RANK over screener parquet | tot 99.1 / net_dir 0.4 / ivr 55.9 / vol_x 94.2 |
| DuckDB §C self-history | PERCENT_RANK over 40 sessions | net_dir 0.0 / total 82.1 / N=40 |
| DuckDB IREN row detail | screener parquet | net_call −23.14M, net_put +1.14M, close 54.35 |

## Tool errors

(none)
