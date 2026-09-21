# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** NOW
**As-of date:** 2026-06-05
**Generated:** 2026-06-06T11:59:00-04:00
**Upstream phases cited:** phase-0-intake.md

## Summary

NOW is a **busy name having a near-flat directional day with a put-premium
undertow**. It is a top-1% name by total options premium today
(universe pctile 99.0 [CTX:universe_pctile DUCKDB]) yet its net directional
flow is tiny: +$1.78M net bullish on $123.2M of two-way classified premium
(rank 47 of the top-50 bullish list), and it appears on **no** bearish,
volume-vs-average, or IV-rank top-50 list. However, on net call−put premium
the name sits at the **1.3rd percentile of the whole universe** and at the
**10.3rd percentile of its own 40-session history** — a put-skewed tape that
the flat bullish/bearish split conceals. IV rank 79.2 (90.4th universe
percentile) says vol is bid. Verdict: **BUSY_NAME_NORMAL_DAY** — phases 1–2
confluence is capped at `+` per `rubrics/confluence-scoring.md`, and phases
1–3 must resolve the put-skew tension.

## Universe ranking

| Metric | NOW result | Leaders (context) |
|---|---|---|
| Net bullish premium (top-50) | **rank 47**, `net_flow` +$1,783,036 | SPX +$2.40B, NDXP +$73.8M, IWM +$55.2M, **STM +$53.4M (1st single name, Tech)**, NDX +$43.5M |
| Net bearish premium (top-50) | outside top-50 | SPXW −$2.09B, QQQ −$116.9M, **SNDK −$114.3M (Tech)**, SOXL −$85.6M, **NVDA −$81.4M (Tech)** |
| Volume ≥2× 30-day avg (top-50) | outside top-50 (ratio <2 or unranked) | FCPT, IMCR, QVCAQ, FDIS, MNOV (small names) |
| IV-rank high (top-50) | outside top-50 | MU, AIS, MRVL |
| IV-rank low (top-50) | outside top-50 | XE, SACH, FDX1 |

NOW's own screener block [CTX: from `insights deep-dive .uw_screener`]:
bullish_premium $62,496,824 − bearish_premium $60,713,788 → derived
`net_flow` **+$1,783,036** (matches the screener row exactly; deep-dive has
no `net_flow` field — `lib/uw-json-paths.md`). call_premium $74,064,700 vs
put_premium $77,595,932; put_call_ratio 0.80 (volume: 126,878C / 101,468P);
iv_rank 79.23; iv30d 0.6693; close $112.45; total OI 1,603,623;
next_earnings_date 2026-07-22 (47 days beyond as-of — outside short trade
horizons).

## Sector read

Index/ETF hedging dominates both directional lists (SPX/SPXW/QQQ/IWM/NDX —
mentally set aside per the single-name convention). Among single names the
tape is **semis-led and two-sided within Technology**: STM leads the bullish
list (+$53.4M) while SNDK (−$114.3M), NVDA (−$81.4M) and SOXL lead the
bearish side — semiconductor distribution is the day's dominant
single-name story. NOW (Technology — software) is **mid-pack in a sector
whose hardware half is being sold**; software is neither leading nor the
target of the selling. No sector tailwind, no direct sector headwind —
phase 6 should resolve whether the semi selling is idiosyncratic or
regime-wide.

## Self-history (DuckDB §C, parquet present)

- `self_pctile_net_dir` (net_call−net_put prem vs own history): **10.3**
  [CTX:self_pctile DUCKDB] — today is in the most put-skewed decile of the
  name's own recent sessions.
- `self_pctile_total` (total premium vs own history): **79.5** — busier than
  ~4 of 5 recent sessions, but not an outlier for this name.
- `sessions_in_window` = **40** (true N; window is non-contiguous across the
  2026-03-30→04-24 snapshot gap flagged in phase-0-intake.md §Local data).

## Source

CLI (`uw screener` ×4, `uw insights deep-dive`) **+ DuckDB §C** (exact
universe + self-history percentiles; tagged ` DUCKDB`). Outside-top-50
metrics: bearish list, volume-vs-average (≥2× screen), iv-rank high, iv-rank
low.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw screener bullish-bearish --direction bullish --top-n 50 --date 2026-06-05 --json` | now rank 47 (idx 46) ← `.results \| map(.ticker) \| index("NOW")`; net_flow +1,783,036 ← `.results[] \| select(.ticker=="NOW") \| .net_flow` | top-50 |
| `uw screener bullish-bearish --direction bearish --top-n 50 --date 2026-06-05 --json` | NOW absent ← same `index` path → null | top-50 |
| `uw screener volume-vs-average --min-volume-ratio 2 --top-n 50 --date 2026-06-05 --json` | NOW absent ← `index` → null | top-50 |
| `uw screener iv-rank --mode high/--mode low --top-n 50 --date 2026-06-05 --json` | NOW absent in both ← `index` → null | top-50 ×2 |
| `uw insights deep-dive --symbol NOW --date 2026-06-05 --json` | bullish 62,496,824 / bearish 60,713,788 / iv_rank 79.2344 / implied_move_perc 0.00379519 / pcr 0.8 ← `.uw_screener.*` | per-name block |
| DuckDB §C (`lib/duckdb-cuts.md`) universe percentiles | 99.0 / 1.3 / 90.4 / 93.2 ← `pctile_total_prem, pctile_net_dir, pctile_iv_rank, pctile_vol_vs_avg` | full universe (call+put vol>0) |
| DuckDB §C self-history | 10.3 / 79.5 / N=40 ← `self_pctile_net_dir, self_pctile_total, sessions_in_window` | 40 local sessions |

## Tool errors

(none)

## DATA NOTE / CORRECTION

`implied_move_perc` = 0.00379519 (0.38%) looks inconsistent with iv30d 0.669
(a 67-vol name should move ~4.2%/day); the sibling field `volatility` = 4.3930
is the plausible daily-move figure. Both recorded verbatim — phase 9 (N4
expected-move) should sanity-check which unit it consumes rather than trust
0.38% blindly. No re-read was needed; values round-tripped `jq` cleanly.

## Verdict for downstream phases

- **Bias from this phase:** none by design — context only. (Tension to
  resolve: flat classified flow vs 1.3rd-pctile net call−put premium.)
- **Conviction:** n/a (context phase)
- **`[CTX:]` block (phases 1, 5, 9 read verbatim):**

```
universe_pctile_total_prem:  99.0            # DUCKDB
universe_rank_net_dir:       47 (of top-50 bullish; net_flow +$1.78M) — DUCKDB net_call−put pctile 1.3
sector_leadership:           Technology mixed — semis sold (SNDK/NVDA/SOXL lead bearish), STM leads bullish; software mid-pack
iv_rank:                     79.23
implied_move_pct:            0.38 (implied_move_perc verbatim; `volatility`=4.39 likely the true daily % — see DATA NOTE)
self_pctile_net_dir:         10.3            # DUCKDB, N=40 (gap-aware)
unusual_verdict:  BUSY_NAME_NORMAL_DAY
```

- **Three things later phases should remember:**
  1. Phases 1–2 confluence capped at `+` (BUSY_NAME_NORMAL_DAY).
  2. The put-premium skew (universe pctile 1.3, self pctile 10.3) is the
     single most unusual thing about today's tape — phases 1/3/4 must
     determine whether it is hedging, opening bearish bets, or vol selling.
  3. IV rank 79 with earnings 47 days out — vol is bid without an imminent
     catalyst; phase 4/5 should check VRP and term structure for why.
- **Open questions:** Is the put premium opening or closing? Aggressor side?
  Is the semi-led tech selling spilling into software (phase 6)?
