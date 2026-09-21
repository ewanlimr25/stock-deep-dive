# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** RKT
**As-of date:** 2026-06-05
**Generated:** 2026-06-06T16:52:00-04:00
**Upstream phases cited:** phase-0-intake.md

## Summary

RKT's options tape on 2026-06-05 is **busy but not unusual**. The name sits at the
90.1 percentile of the optionable universe on total premium and 82.5 on
volume-vs-30d-average, yet it is **outside the top-50 on every leadership board**
(net bullish, net bearish, volume-vs-average, IV-rank high and low), and its own
40-session self-history puts today at only the **38.5 percentile on net direction**
and 46.2 on total premium — i.e., a completely normal day for a name that always
trades this much. Net flow is marginally bearish (−$209,751 derived). Its sector
(Financial Services) is lagging on a broadly risk-off tape where only Consumer
Defensive printed net-positive directional premium.

## Key signals

- Derived net flow = bullish_premium 1,256,315 − bearish_premium 1,466,066 =
  **−$209,751** [CTX: `uw insights deep-dive .uw_screener`, derived per
  `lib/uw-json-paths.md` — no `net_flow` field in this block]
- Universe exact percentiles (6k+ optionable names): total_prem **90.1**,
  net_dir **11.0** (bottom-decile = relatively bearish), iv_rank 24.4,
  vol_vs_avg **82.5** [CTX:universe_pctile DUCKDB]
- Self-history (N=40 sessions, gap-aware): net_dir **38.5 pctile**, total
  **46.2 pctile** — mid-pack, not a flow event [CTX:self_pctile DUCKDB]
- Outside top-50 on ALL five `uw screener` leadership boards [CTX:]
- IV rank **29.9622**, iv30d 0.5719, implied_move_perc **0.0119843** (≈1.20%),
  next_earnings_date 2026-07-30 [CTX: `.uw_screener`]

## Detailed findings

### Universe ranking (uw screener, --date 2026-06-05)

| Board | RKT rank | Leaders (top 3–5) |
|---|---|---|
| bullish-bearish --direction bullish | outside top-50 | SPX (+$2.398B), NDXP (+$73.8M), IWM (+$55.2M), STM (+$53.4M), NDX (+$43.5M) |
| bullish-bearish --direction bearish | outside top-50 | SPXW (−$2.090B), QQQ (−$116.9M), SNDK (−$114.3M), SOXL (−$85.6M), NVDA (−$81.4M) |
| volume-vs-average (≥2x) | outside top-50 | FCPT, IMCR, QVCAQ, FDIS, MNOV |
| iv-rank --mode high | outside top-50 | MU, AIS, MRVL |
| iv-rank --mode low | outside top-50 | — |

Setting index/ETF tickers aside (SPX/SPXW/NDXP/NDX/IWM/QQQ/SOXL), the single-name
leadership today is semis-centric: STM on the bullish side; SNDK and NVDA leading
the bearish board. RKT is not a directional leader in either direction.

### RKT's own screener block (`uw insights deep-dive .uw_screener`)

| Field | Value |
|---|---|
| bullish_premium | 1,256,315 |
| bearish_premium | 1,466,066 |
| call_premium / put_premium | 1,912,369 / 1,332,438 |
| call_volume / put_volume | 32,206 / 14,951 |
| put_call_ratio | 0.46 |
| iv_rank | 29.9622 |
| iv30d | 0.571872595676123 |
| implied_move / implied_move_perc | 0.1514222090151781 ($) / 0.0119843457867177 |
| total_open_interest | 756,321 |
| next_earnings_date | 2026-07-30 |

P/C of 0.46 says volume skews to calls 2:1, but premium-aggressor split nets
slightly bearish — calls being sold / puts bought at premium parity. Phase 1
resolves this with the aggressor tape.

### Exact percentiles (DuckDB §C — escape hatch, snapshot present)

Universe (2026-06-05, `call_volume+put_volume>0` filter):

| pctile_total_prem | pctile_net_dir | pctile_iv_rank | pctile_vol_vs_avg |
|---|---|---|---|
| 90.1 | 11.0 | 24.4 | 82.5 |

Self-history (all 40 local sessions; **non-contiguous** — 21-session hole
2026-03-28→04-24 per phase-0-intake.md §Local data — N stated per `§ gap`):

| self_pctile_net_dir | self_pctile_total | sessions_in_window |
|---|---|---|
| 38.5 | 46.2 | 40 |

### Sector read (DuckDB on same snapshot, sum net_dir by sector)

| Sector | Σ net_dir ($M) |
|---|---|
| Consumer Defensive | **+13.3** (only green sector) |
| Real Estate | −1.8 |
| Healthcare | −7.3 |
| Utilities | −8.4 |
| Energy | −12.0 |
| Basic Materials | −23.5 |
| **Financial Services (RKT)** | **−55.8** (7th of 11) |
| Industrials | −102.7 |
| Consumer Cyclical | −114.5 |
| Communication Services | −137.0 |
| Technology | −890.3 |

Broad risk-off directional tape; RKT's sector is lagging/mid-pack, not in favour.
RKT close (screener): **$12.65**.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw screener bullish-bearish --direction bullish --top-n 50 --date 2026-06-05 --json` | RKT ← `.results \| map(.ticker) \| index("RKT")` = null → outside top-50; leaders ← `.results[:5] \| {ticker,net_flow}` | top-50 |
| `uw screener bullish-bearish --direction bearish --top-n 50 --date 2026-06-05 --json` | same — outside top-50 | top-50 |
| `uw screener volume-vs-average --min-volume-ratio 2 --top-n 50 --date 2026-06-05 --json` | outside top-50 | top-50 |
| `uw screener iv-rank --mode high/--mode low --top-n 50 --date 2026-06-05 --json` | outside top-50 both | top-50 ×2 |
| `uw insights deep-dive --symbol RKT --date 2026-06-05 --json` | all §block values ← `.uw_screener.*`; net flow derived `bullish_premium - bearish_premium` | whole-tape |
| DuckDB §C (`lib/duckdb-cuts.md`) on `stock-screener-2026-06-05.parquet` + 40-file glob | universe + self pctiles; sector Σ net_dir | full universe / 40 sessions |

## Tool errors

None.

## DATA NOTE / CORRECTION

None — first read stood.

## Verdict for downstream phases

- **Bias from this phase:** neutral (context only — no directional bias by design)
- **Conviction:** n/a (context phase)
- **Three things later phases should remember:**
  1. `unusual_verdict = BUSY_NAME_NORMAL_DAY` → **phases 1–2 confluence capped at
     `+` (not `++`)** per `rubrics/confluence-scoring.md`.
  2. RKT's sector is being net-sold on a risk-off tape (Fin Svcs −$55.8M, Tech
     −$890M); name-strong/sector-weak is a yellow flag phase-6 must resolve.
  3. P/C 0.46 (call-heavy volume) vs net premium −$210k (slightly bearish):
     volume and aggressor premium disagree — phase 1 must resolve with the tape.
- **Open questions:** Is the call volume opening or closing? Is the slight bearish
  premium tilt concentrated in one print or distributed?

### `[CTX:]` block (phases 1, 5, 9 read verbatim)

```
universe_pctile_total_prem:  90.1            # DUCKDB exact
universe_rank_net_dir:       outside top-50 (both directions)
sector_leadership:           Financial Services is lagging today (−$55.8M, 7/11; tape risk-off, only Consumer Defensive green)
iv_rank:                     29.9622
implied_move_pct:            1.198%
self_pctile_net_dir:         38.5            # DUCKDB, N=40 non-contiguous sessions
unusual_verdict:  BUSY_NAME_NORMAL_DAY
```
