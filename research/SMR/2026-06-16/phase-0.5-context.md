# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** SMR
**As-of date:** 2026-06-16
**Generated:** 2026-06-17T11:48:05Z
**Upstream phases cited:** phase-0-intake.md

## Summary

SMR is a **busy name having a normal day, not a genuinely unusual one.** It sits
in the **top ~6.5% of the universe by total option premium** today
(`universe_pctile_total_prem=93.5` DUCKDB) — structurally a high-activity options
name — but its **net-directional premium is near the bottom of the universe**
(`pctile_net_dir=8.1` DUCKDB; net flow −$0.16M, slightly *bearish*), it is
**outside the top-50 on every screener leaderboard** (net-bullish, net-bearish,
volume-vs-average, IV-rank-high), its IV rank is below the universe median
(26.7, `pctile_iv_rank=31.8`), and **today is below its own median premium day**
(`self_pctile_total=37.0`, `self_pctile_net_dir=45.7` over 47 available
sessions). Stock volume is **0.78× its 30-day average** — quiet. Verdict:
**BUSY_NAME_NORMAL_DAY** → phases 1–2 confluence is capped at `+` (not `++`).

## Universe ranking (today, ~all optionable names)

| Metric | SMR read | Where it ranks |
|--------|----------|----------------|
| Total option premium | $4.69M | **93.5th pctile** (top ~6.5%) — busy name |
| Net-directional premium | **−$0.159M** (bull 1.826M − bear 1.985M) | **8.1th pctile** — leans net-bearish vs universe |
| IV rank | 26.68 | 31.8th pctile — below median |
| Option vol-vs-avg | n/a (outside top-50) | 84.3th pctile by recipe ratio, but stock vol **0.78×** avg |
| Net-bullish leaderboard | **outside top-50** | not a directional leader |
| Net-bearish leaderboard | **outside top-50** | not among heaviest sells either |

- Today's **net-bullish tape leaders** (single names, ETFs aside): LRCX
  (+$106.4M), CRM (+$89.3M), CRWV (+$42.4M), META (+$31.7M) — **semis / software /
  AI-cloud lead**.
- Today's **net-bearish leaders**: MU (−$192M), MSFT (−$84M), TSLA (−$63M), SNDK
  (−$52M), **BE (−$51M)**, INTC (−$48M).

## Sector read

SMR is classified **Industrials / Specialty Industrial Machinery** (Finviz), a
small-cap **nuclear / clean-power** name (Index = RUT, Russell 2000). Its
adjacent power / clean-energy complex is being **net sold** today:

- **BE** (Bloom Energy, fuel cells) — net flow **−$51.0M** (bull 93.2M / bear
  144.2M), #7 on the net-bearish leaderboard.
- **GEV** (GE Vernova, power) — also in the net-bearish list.

So SMR's neighbourhood is **lagging / being faded**, while tape leadership is
tech/semis/AI. A name that is itself net-bearish-leaning *and* sits in a sector
being sold is a **yellow flag** — phase-6 (macro/rotation) must resolve whether
this is broad de-risking of the small-cap power theme or name-specific. This is
context, **not** a directional call.

## Self-history (DuckDB, SMR's own sessions)

- `self_pctile_net_dir = 45.7` — middle of SMR's own net-directional range; a
  **normal directional day** for the name.
- `self_pctile_total = 37.0` — **below** its own median premium day (a quieter
  options day than SMR usually has).
- `sessions_in_window = 47` available sessions — **non-contiguous** (spans the
  2026-03-27→04-27 gap noted in phase-0). Not a contiguous 47-calendar-day window.

## Source

CLI screener rankings (`uw screener` ×4) **plus** the DuckDB §C escape hatch
(`lib/duckdb-cuts.md`) for exact universe + self-history percentiles (local
parquet for 2026-06-16 present). Outside-top-50 recorded on all four CLI
leaderboards. Sector/industry from `fz quote` (UW sector field unreliable per
project memory).

## Verdict for downstream

```
universe_pctile_total_prem:  93.5            # DUCKDB — busy name (top 6.5% premium)
universe_rank_net_dir:       outside top-50  # DUCKDB pctile 8.1 → net-bearish-leaning
sector_leadership:           Industrials/nuclear-power LAGGING (peers BE,GEV net-bearish; tape led by semis/AI)
iv_rank:                     26.68
implied_move_pct:            5.68            # feeds phase-9 expected-move
self_pctile_net_dir:         45.7            # DUCKDB, N=47 sessions (non-contiguous)
unusual_verdict:             BUSY_NAME_NORMAL_DAY
```

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq`/SQL path | Rows used |
|------------------|------------------------------|-----------|
| `uw screener bullish-bearish --direction bullish --top-n 50 --date 2026-06-16` | SMR `index([.results[].ticker])` = null → outside top-50; leaders LRCX/CRM/CRWV | top-50 |
| `uw screener bullish-bearish --direction bearish --top-n 50 --date 2026-06-16` | SMR outside top-50; BE `net_flow=-51,023,686` (#7) | top-50 |
| `uw screener volume-vs-average --min-volume-ratio 2 --top-n 50 --date 2026-06-16` | SMR outside top-50 | top-50 |
| `uw screener iv-rank --mode high --top-n 50 --date 2026-06-16` | SMR outside top-50 | top-50 |
| `uw insights deep-dive --symbol SMR --date 2026-06-16` | `iv_rank=26.6757`, `implied_move_perc=0.05679`, `put_call_ratio=0.2626`, bull 1.826M / bear 1.985M | uw_screener block |
| DuckDB §C universe pctile (`stock-screener-2026-06-16.parquet`) | `pctile_total_prem=93.5`, `pctile_net_dir=8.1`, `pctile_iv_rank=31.8` | full universe |
| DuckDB §C self-history (47 screener parquets) | `self_pctile_net_dir=45.7`, `self_pctile_total=37.0`, `sessions=47` | SMR rows |

## Tool errors

(none — all reads jq/SQL-parsed. Note: `yahoo_fundamentals` inside the deep-dive
returned HTTP 401, but that sub-field is unused here; UW screener block intact.)

## DATA NOTE / CORRECTION

The screener net-directional field is **`net_flow`** (= bullish_premium −
bearish_premium), **not** `net_premium` (which is `null` in these rows). Confirmed
against BE: `net_flow=-51,023,686` == 93,181,705 − 144,205,391. All net-direction
reads above use `net_flow` / the DuckDB `net_call_premium−net_put_premium`
equivalent. (Consistent with the project's "deep-dive has no net_flow; derive it"
trap — here the *screener* row carries `net_flow` directly while `net_premium` is
null.)

## Verdict for downstream phases

- **Bias from this phase:** neutral (context only — sets no directional bias)
- **Conviction:** n/a
- **Three things later phases should remember:**
  1. **BUSY_NAME_NORMAL_DAY** — high absolute premium (93.5 pctile) but a normal
     day for SMR (self total 37 pctile, net-dir 45.7 pctile, stock vol 0.78×).
     Phases 1–2 confluence **capped at `+`**.
  2. Net-directional flow **leans bearish** vs the universe (8.1 pctile); not a
     bullish-flow name today despite call-heavy gross volume.
  3. SMR's **power/clean-energy sector is being faded** (BE, GEV net-bearish);
     name + sector both un-bid → yellow flag for phase-6.
- **Open questions:** Is the sector fade macro/rotation-driven (phase-6) or
  name-specific? Does the call-heavy gross volume (call_prem 2× put_prem) reflect
  upside speculation or call *selling* against the short base? (phases 1, 3)
