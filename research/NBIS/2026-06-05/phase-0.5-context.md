# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** NBIS
**As-of date:** 2026-06-05
**Generated:** 2026-06-06T19:40:00-0400
**Upstream phases cited:** phase-0-intake.md

## Summary

NBIS's options activity on 2026-06-05 is **genuinely unusual, with a bearish
cross-sectional tilt — but the tape is overwhelmingly two-way**. Total premium
($460.1M) sits at the **99.6th percentile of the whole optionable universe** and
the 92.3rd percentile of NBIS's own 40-session history, yet net direction is only
−$12.2M (net_call − net_put) — **0.8th universe percentile** (i.e., among the most
net-bearish names on the tape) and 10.3rd self-percentile. The name ranks **#44 on
the market-wide net-bearish screen** (net_flow −$9.6M, bullish−bearish premium)
and is outside the bullish top-50. Its sector (Communication Services per the
screener) is the second-most-sold sector today (−$137M) behind Technology
(−$890M) — a broadly risk-off single-name tape. IV rank ~90 with IV30d ~112%.
Headline: a battleground name on a heavy-volume, high-IV, mildly net-bearish day —
the gross-vs-net gap (net is only ~2.6% of gross premium) is the key context for
phase 1.

## Universe ranking

- Net **bullish** premium screen (top-50): **NBIS absent** — outside top-50.
  Leaders: SPX +$2,398M, NDXP +$73.8M, IWM +$55.2M, **STM +$53.4M**, NDX +$43.5M
  (only single name in the top 5 is STM).
- Net **bearish** premium screen (top-50): **NBIS rank #44**, net_flow
  **−$9,602,713**. Leaders: SPXW −$2,090M, QQQ −$116.9M, **SNDK −$114.3M,
  SOXL −$85.6M, NVDA −$81.4M** — AI/semis complex leading the sell side.
- Volume-vs-average screen (ratio ≥2, top-50): **NBIS absent** — outside top-50
  (cutoff was a 236× ratio dominated by micro-caps; informational only).
- IV-rank high screen (top-50): NBIS absent from top-50 (all at 100); NBIS's own
  iv_rank = 89.97 — elevated but below the pinned-at-100 cohort (MU, MRVL, SMH,
  SOXL...).
- Exact universe percentiles `[CTX:universe_pctile DUCKDB]`:
  **total premium 99.6 · net-directional 0.8 (extreme bearish tail) ·
  iv_rank 94.0 · vol-vs-avg 95.9** (vol-vs-avg metric is option-contracts ÷
  avg30 share volume — consistent cross-sectionally but not a clean ratio;
  treat the 95.9 as indicative).

## Sector read

Full-universe net-directional premium by sector `[CTX: DUCKDB]` (single names):

| Sector | Net dir ($M) |
|---|---|
| Consumer Defensive | **+13.3** (only positive) |
| … | … |
| Communication Services (NBIS's) | **−137.0** (2nd worst) |
| Technology | **−890.3** (worst) |

The directional tape is being **sold across tech/AI complex** (NVDA, SNDK, SOXL,
MU on the bearish leaders board). NBIS's sector is **lagging**, and NBIS's own
mild net-bearish tilt is **aligned with** its sector — no name-vs-sector
divergence to resolve, but phase-6 should note the risk-off tech tape.

## Self-history (40 sessions, non-contiguous)

`[CTX:self_pctile DUCKDB]` — N=40 local sessions (window 2026-03-13…2026-06-05
with the known 2026-03-28→04-24 hole; percentiles are over available sessions):

- `self_pctile_net_dir` = **10.3** — today is more net-bearish than ~90% of its
  own recent sessions.
- `self_pctile_total` = **92.3** — a genuinely busy day even by NBIS's own
  hyperactive standard.
- NBIS close 2026-06-05: **$227.81**; total premium $460.1M; net dir −$12.2M.

## Source

CLI (`uw screener` ×4, `uw insights deep-dive`) + DuckDB escape hatch §C
(universe percentile, self-history, sector aggregate). NBIS outside top-50 on:
bullish net flow, volume-vs-average, IV-rank-high screens (recorded, not errors).

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|------------------|--------------------------|-----------|
| `uw screener bullish-bearish --direction bullish --top-n 50 --date 2026-06-05 --json` | NBIS absent ← `map(.t) \| index("NBIS")` = null | top-50 |
| `uw screener bullish-bearish --direction bearish --top-n 50 --date 2026-06-05 --json` | rank #44, net_flow −9,602,713 ← `.results[] \| select(.ticker=="NBIS") \| .net_flow` | top-50 |
| `uw screener volume-vs-average --min-volume-ratio 2 --top-n 50 --date 2026-06-05 --json` | NBIS absent | top-50 |
| `uw screener iv-rank --mode high --top-n 50 --date 2026-06-05 --json` | NBIS absent; top names pinned at 100 | top-50 |
| `uw insights deep-dive --symbol NBIS --date 2026-06-05 --json` | bullish_premium 195,086,472; bearish_premium 204,689,185; put_call_ratio 0.97; iv_rank 89.9732; iv30d 1.117; implied_move 0.927; implied_move_perc 0.004068; total OI 1,117,357; next_earnings 2026-08-06 ← `.uw_screener.*` | whole-tape |
| DuckDB §C universe + self-history + sector agg | pctiles 99.6 / 0.8 / 94.0 / 95.9; self 10.3 / 92.3 (N=40); sector table | full universe |

## Tool errors

(none)

## DATA NOTE / CORRECTION

- `implied_move_perc` = 0.004068 (0.41%) is implausibly low against iv30d 1.117
  (≈7%/day at 112% annualized IV). Recorded verbatim; phase-9 should prefer an
  expected move derived from IV30d and flag this field as suspect.
- Two net-direction definitions coexist: bullish−bearish premium = −$9.6M
  (screener net_flow); net_call−net_put = −$12.2M (DuckDB). Same sign, similar
  magnitude; both quoted with their sources.

## Verdict for downstream phases

- **Bias from this phase:** none set (context-only) — cross-sectional tilt is
  mildly bearish, dwarfed by two-way gross flow.
- **Conviction:** n/a (context phase)

```
[CTX:]
universe_pctile_total_prem:  99.6                       # DUCKDB
universe_rank_net_dir:       #44 on net-BEARISH screen (outside bullish top-50); universe net-dir pctile 0.8
sector_leadership:           Communication Services is lagging today (−$137M, 2nd worst; Tech −$890M worst — AI/semis sold)
iv_rank:                     89.97
implied_move_pct:            0.41   # SUSPECT — see DATA NOTE; IV30d 111.7% implies ~7%/day
self_pctile_net_dir:         10.3   # DUCKDB, N=40 non-contiguous sessions
unusual_verdict:  GENUINELY_UNUSUAL   # bearish-tilted, but net is only ~2.6% of $460M gross — two-way battleground
```

- **Three things later phases should remember:**
  1. Gross flow is enormous ($460M, 99.6 pctile) but net direction is small
     (−$9.6M to −$12.2M) — do not mistake activity for conviction; read phase-1's
     aggressor/sweep detail before assigning direction.
  2. The whole AI/semis complex was sold today (NVDA/SNDK/SOXL/MU on the bearish
     board; Tech −$890M) — NBIS weakness may be beta, not idiosyncratic.
  3. IV rank ~90, IV30d ~112%, short float 22.43% (phase-0) — options are
     expensive and the name is heavily shorted; structure choice (phase 9) must
     respect rich vol, and phase-7c must gate on squeeze risk.
- **Open questions:** Is the −$9.6M net bearish tilt aggressive (sweeps at ask
  on puts) or passive/hedging (puts sold to open, collars)? Phase 1's aggressor
  split answers this. What news drove a 99.6-pctile premium day with no earnings
  until 2026-08-06? Phase 6/7c (WebSearch) should identify the catalyst.
```
