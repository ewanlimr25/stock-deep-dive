# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** ELF
**As-of date:** 2026-06-30
**Generated:** 2026-07-01T00:17:46Z
**Upstream phases cited:** phase-0-intake.md

## Summary

ELF's flow today is **genuinely unusual for the name**, even though it does not
crack the market's absolute leaderboard. On the CLI top-50 ranks ELF is *outside
top-50* on net-bullish, net-bearish, volume-vs-average, and IV-rank-high — those
lists are owned by mega-caps/ETFs (SNDK +$117M, AMD +$85M net). But the exact
DuckDB percentiles reframe it: ELF sits at the **96.8th universe percentile on
total option premium** and **97.9th on net-directional premium**, and against its
own 56-session history **today is its single largest premium day (100th self-pctile,
$14.53M)** and its 94.5th-percentile most net-bullish session. The one soft spot is
volume expansion — 1.51× the 30-day average (82nd pctile), short of the 2× textbook
bar. Net read: a real, name-specific bullish premium spike, not a busy name's normal
day — but ELF's sector (Consumer Defensive) is *not* the tape's favored sector today
(Technology/semis lead), a yellow flag for phase 6 to resolve.

## Universe ranking

- **Net-directional premium:** ELF net_flow = **+$1.22M** bullish
  (bull $5.97M − bear $4.75M). Outside CLI top-50 in absolute dollars, but
  **97.9th universe percentile** `[CTX:universe_pctile_net_dir DUCKDB]`. The absolute
  leaders are all mega-cap/tech: 1. SNDK +$117.4M, 2. AMD +$84.9M, 3. QQQ +$60.0M,
  4. SPCX +$41.9M, 5. TSM +$41.3M, 6. GEV +$32.9M, 7. CSCO +$32.2M.
- **Total option premium:** ELF = **$14.53M** → **96.8th universe percentile**
  `[CTX:universe_pctile_total_prem DUCKDB]`.
- **Volume vs 30-day average:** vol_x = **1.51×** (20,545 vs 13,604 avg contracts) →
  **81.9th universe percentile**. Elevated, but below the ≥2× "textbook unusual" bar.
- **IV rank:** 46.8 → 59.3rd universe percentile — mid-pack, not a vol-panic name.

## Sector read

- ELF sector = **Consumer Defensive** (Household & Personal Products / beauty).
- Today's bullish directional tape is **Technology/semis-led** — SNDK, AMD, TSM,
  CSCO, MRVL, DELL, AVGO fill the top ranks; no Consumer Defensive name appears in
  the top-12 net-bullish. So ELF is strong on *its own* flow while its **sector is
  lagging the day's favored rotation**. That name-strong / sector-not-favored split
  is the classic yellow flag phase-6 (macro/rotation) must resolve — is beauty /
  consumer staples catching a bid, or is ELF an idiosyncratic single-name move?

## Self-history (local parquet present — 56 sessions, 2026-03-13 → 06-30)

- **self_pctile_total_prem: 100.0** — $14.53M is ELF's **biggest option-premium day**
  in the entire 56-session window `[CTX:self_pctile DUCKDB]`. Next-highest recent was
  2026-06-16 at $9.51M; typical recent days ran $2–5M.
- **self_pctile_net_dir: 94.5** — +$1.22M net-bullish is near the top of ELF's own
  range; recent net-dir mostly oscillated ±$0.7M (prior high 06-22 at +$0.63M).
- **self_pctile_ivrank: 58.2** — IV rank 46.8 is only mid for ELF; the spike is in
  *premium/direction/volume*, not in implied vol. A flow event, not a vol event.
- **N caveat:** the 56 sessions are **non-contiguous** — a ~31-day April hole
  (2026-03-27 → 2026-04-27, per phase-0-intake.md). Percentiles are over 56
  *available* sessions, not a contiguous calendar window.

## Source

- CLI ranks: `uw screener bullish-bearish/volume-vs-average/iv-rank --top-n 50`
  (ELF outside top-50 on all — recorded, not an error).
- Absolute numbers: `uw insights deep-dive --symbol ELF` `uw_screener` block.
- Exact percentiles: **CLI + DuckDB** `lib/duckdb-cuts.md §C` on
  `stock-screener-2026-06-30.parquet` (+ 56-file self-history glob).

## Verdict for downstream

```
universe_pctile_total_prem:  96.8            # DUCKDB
universe_rank_net_dir:       outside top-50 absolute / 97.9th pctile (DUCKDB)
sector_leadership:           Consumer Defensive LAGGING (Technology/semis lead today)
iv_rank:                     46.8            # insights_deep_dive
implied_move_pct:            3.52%           # implied_move_perc 0.0352 → feeds phase-9 N4
self_pctile_net_dir:         94.5            # DUCKDB
unusual_verdict:  GENUINELY_UNUSUAL   (caveat: vol expansion only 1.51×, not ≥2×)
```

- **Bias from this phase:** neutral (context only — sets no directional bias).
- **Conviction:** n/a (context calibration).
- **Three things later phases should remember:**
  1. Today is ELF's **largest premium day in 56 sessions** and 97.9th-pctile
     net-bullish — the flow is genuinely name-unusual; do **not** discount phases 1–2
     as "busy-name noise." BUSY_NAME_NORMAL_DAY does **not** fire → no phase-1/2
     confluence cap.
  2. Unusualness is in **premium/direction/volume**, not IV (rank 46.8, 58th self-pctile)
     — this is a directional flow event, not a vol event; frame structures accordingly.
  3. ELF's sector (Consumer Defensive) is **lagging** the tech-led tape — phase-6 must
     resolve whether the sector is a headwind (name-strong / sector-weak yellow flag).
- **Open questions:** Is the volume expansion (only 1.51×) enough to sustain a move, or
  is this a one-day premium print? Phase-1 must check whether the $14.53M is sweep/ask-
  side (aggressive, new positioning) or spread/mid (positioning churn).
