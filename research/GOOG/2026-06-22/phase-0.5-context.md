# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** GOOG
**As-of date:** 2026-06-22
**Generated:** 2026-06-22
**Upstream phases cited:** phase-0-intake.md

## Summary

GOOG is having a **high-activity, directionally-bearish day** — not a quiet name
and not a clean "unusual-volume" event either. Total option premium sits in the
**99.7th universe percentile** and the **95.9th percentile of GOOG's own 50-session
history** [CTX:self_pctile DUCKDB], so the tape is genuinely busy. But the tilt is
**net bearish**: net-directional premium (bullish − bearish) is **−$23.0M**, which
ranks GOOG **#13 on the day's net-bearish leaderboard** and lands in the **0.2nd
universe percentile** and **10.2nd self percentile** [CTX:net_dir] — i.e. one of
GOOG's more bearish-leaning days both cross-sectionally and for itself. Crucially
this is a *directional-premium* unusualness, **not** a volume or vol event: option
volume is only **1.62×** the 30-day average (below the 2× unusual-volume bar; GOOG
is outside the CLI's top-50 vol-vs-avg list), stock volume 1.14×, and IV rank is a
middling **39.8** (51st universe pctile). Both Alphabet share classes — GOOG and
the voting GOOGL (#5 bearish, −$57.4M) — plus META and NFLX are net-sold today, so
the **Communication Services mega-cap complex is lagging** while semis lead the
bullish tape.

## Key signals

- Net-directional premium **−$23.04M** (bull $182.2M − bear $205.2M) → **#13
  net-bearish** in the universe; **outside top-50 bullish** [CTX:net_dir]
- Total premium **99.7th universe pctile** / **95.9th self pctile** — busy day
  [CTX:total_prem DUCKDB]
- Net-dir **0.2nd universe pctile** / **10.2nd self pctile** — bearish extreme for
  the name [CTX:self_pctile DUCKDB]
- Option volume **1.62× 30-day avg** (stock 1.14×) — elevated but **< 2× bar**;
  IV rank **39.8** (51st pctile) → not a vol/IV event
- Sector: **Communication Services lagging** — GOOG, GOOGL, META, NFLX all net
  bearish; semis (MU/SNDK/INTC/SOXL) lead the bullish tape

## Universe ranking (as-of 2026-06-22)

| Metric | GOOG value | Rank / percentile |
|--------|-----------|-------------------|
| Net bullish premium | −$23.0M | **outside top-50** |
| Net bearish premium | −$23.0M | **#13** |
| Total premium (call+put) | $419.3M | **99.7th pctile** [DUCKDB] |
| Net-directional premium | −$23.0M | **0.2nd pctile** [DUCKDB] |
| IV rank | 39.78 | **51.3rd pctile** [DUCKDB] |
| Option vol vs 30d avg | 1.62× | **96.6th pctile** [DUCKDB] (but < 2× absolute) |

**Bullish-tape leaders (single names, ETFs aside):** MU (+$214.9M), SNDK (+$56.9M),
TSLA (+$38.9M), INTC (+$23.1M), LITE (+$18.2M) — **semiconductors lead**.
**Bearish-tape leaders:** CDNS (−$110.8M), SPCX (−$100.4M), GOOGL (−$57.4M, #5),
AMZN (−$54.4M), MSFT (−$45.9M), NVDA (−$44.0M), GOOG (#13, −$23.0M).

## Sector read

GOOG's sector is **Communication Services**, and today it is being **sold**: every
Comm-Services name in the bearish top-50 — GOOGL (−$57.4M), GOOG (−$23.0M),
META (−$15.4M), NFLX (−$14.1M) — is net bearish, with no Comm-Services name in the
bullish leaders. The directional tape is led on the long side by **semiconductors**
(MU, SNDK, INTC, SOXL, DRAM, LITE) and on the short side by EDA/design (CDNS) and
mega-cap tech/comm. **A name being sold while its whole sector is being sold is a
consistent (not divergent) bearish read** — no yellow flag for phase 6 to resolve;
the macro phase should check whether mega-cap Comm/Tech rotation-out is broad.

## Self-history (local parquet present, DuckDB)

- **N = 50 sessions** (GOOG's available local window; **spans the 2026-03-27 →
  04-27 gap** — not a contiguous calendar window, per phase-0).
- `self_pctile_net_dir` = **10.2** → today's net-direction is in the **bottom
  decile** of GOOG's own 50 sessions (a bearish-extreme day for the name).
- `self_pctile_total` = **95.9** → today's total premium is in the **top ~4%** of
  GOOG's own window (a high-conviction-activity day).
- Read together: heavy money is moving in GOOG today, and it is leaning short.

## Source

CLI (`uw screener` ×4 + `uw insights deep-dive`) **+ DuckDB §C** (exact universe &
self-history percentiles; local screener parquet present for 2026-06-22). "Outside
top-50" recorded for bullish-premium, vol-vs-average, and iv-rank-high screens.

## Verdict for downstream

```
universe_pctile_total_prem:  99.7
universe_rank_net_dir:       #13 net-BEARISH (outside top-50 bullish)
sector_leadership:           Communication Services LAGGING today (mega-cap comm/tech net sold; semis lead)
iv_rank:                     39.78
implied_move_pct:            2.63%        # $9.18 on $348.78 close (next earnings 2026-07-22, ~1mo out)
self_pctile_net_dir:         10.2         # bottom-decile = bearish extreme for the name
unusual_verdict:             GENUINELY_UNUSUAL   # on NET-DIRECTIONAL (bearish) premium + total premium; NOT a volume (1.62x) or IV (40) event
```

**Interpretation for phases 1–9:** the flow IS genuinely unusual — but in
*direction and dollar-weight*, leaning **bearish**, on a busy day — **not** in
volume-ratio or implied vol. Phases 1–2 should test whether the −$23M net-bearish
premium is real institutional positioning (sweeps/blocks, put buying vs call
selling) or mechanical (the put_call_ratio is 0.39, call-heavy by volume, so the
bearish *premium* may come from call-side selling / OTM put bids rather than
outright put accumulation — resolve there). Because volume is only 1.62× and IV is
mid, do **not** treat this as a top-tier conviction setup on magnitude alone; the
edge, if any, is the directional consistency with a sector-wide Comm/Tech sell.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq`/SQL path | Rows used |
|------------------|------------------------------|-----------|
| `uw screener bullish-bearish --direction bullish --top-n 50 --date 2026-06-22 --json` | GOOG outside top-50 ← `index("GOOG")==null` | top-50 |
| `uw screener bullish-bearish --direction bearish --top-n 50 --date 2026-06-22 --json` | GOOG #13, net_flow=−23040858, sector="Communication Services" ← `.results[]` | top-50 |
| `uw screener volume-vs-average --min-volume-ratio 2 --top-n 50 --date 2026-06-22 --json` | GOOG outside top-50 | top-50 |
| `uw screener iv-rank --mode high --top-n 50 --date 2026-06-22 --json` | GOOG outside top-50 | top-50 |
| `uw insights deep-dive --symbol GOOG --date 2026-06-22 --json` | iv_rank=39.78, implied_move_perc=0.02632, put_call_ratio=0.388, next_earnings=2026-07-22 ← `.uw_screener` | 1 |
| DuckDB §C universe pctile (`stock-screener-2026-06-22.parquet`) | total 99.7 / net_dir 0.2 / iv 51.3 / vol_x 96.6 ← `PERCENT_RANK()` | universe |
| DuckDB §C self-history (50 screener parquets) | self_net_dir 10.2 / self_total 95.9 / N=50 ← `PERCENT_RANK()` | 50 sessions |
| DuckDB raw vol ratio | opt_vol_x=1.62, stk_vol_x=1.14 | 1 |

## Tool errors

None. All five CLI reads round-tripped through `jq`; both DuckDB cuts returned.

## Verdict for downstream phases

- **Bias from this phase:** neutral (context only — no directional bias set here),
  but flags a **bearish-leaning, high-premium, low-vol-expansion** backdrop.
- **Conviction:** n/a (context phase).
- **Three things later phases should remember:**
  1. Net-directional premium is a **bearish extreme** for GOOG (0.2 univ / 10.2
     self pctile) on a **top-decile total-premium** day — the dollars are real and
     leaning short.
  2. It is **not** a volume (1.62×) or IV (40 / 51st pctile) event — temper
     conviction; magnitude alone is mega-cap-normal.
  3. The **whole Communication Services mega-cap complex** (GOOGL, GOOG, META,
     NFLX) is net-sold today while **semis lead** — consistent sector context, a
     job for phase 6 to size as rotation vs noise.
- **Open questions:** is the −$23M net-bearish premium genuine put accumulation or
  call-side selling (put_call_ratio 0.39 is call-heavy by volume)? Phase 1 resolves.
