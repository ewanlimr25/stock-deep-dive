# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** SHOP
**As-of date:** 2026-07-17
**Generated:** 2026-07-19 (run) · as-of 2026-07-17
**Upstream phases cited:** phase-0-intake.md

## Summary

SHOP is a **busy name having a mildly bearish normal day**, not a genuine flow
spike. It sits in the **top 2.3% of the universe by total option premium**
($17.44M, 97.7 pctile across 6,298 names) — a perennially active options name —
but its **net-directional premium is only at its own 32nd self-history
percentile** (−$1.08M today vs a 31-session distribution that has been net-bearish
7 of the last 8 sessions). Cross-sectionally that −$1.08M lands in the universe's
net-bearish tail (1.8 pctile), but that reflects a *persistent* bearish tilt for
the name rather than a one-day event. The stock traded **below average volume**
(5.67M vs 8.56M avg30 = 0.66×) and closed **−1.2%** (123.56 vs 125.06 prev). IV
rank is elevated at **85.6**. Verdict: `BUSY_NAME_NORMAL_DAY` → phases 1–2
confluence is capped at `+` (not `++`).

## Universe ranking

- **Total option premium:** $17.44M → **97.7 universe percentile** (top 2.3% of
  6,298 names). Very liquid/active options name. `[CTX]` [DUCKDB]
- **Net-directional premium (bull−bear):** −$1.08M → **1.8 universe percentile**
  (net-bearish tail). Absolute magnitude is modest; the low percentile reflects
  that most names cluster near zero while SHOP carries a steady bearish tilt.
  [DUCKDB]
- **Screener leader boards:** SHOP is **outside the top-60** on both the bullish
  net-premium list and the bearish net-premium list (by magnitude) — it is not one
  of the day's directional leaders. Bullish tape led by SPX / NDX / SPXW (indices),
  then **NVDA ($81.6M net), CDNS ($55.4M), SNDK ($42.7M), META ($35.1M)**.
  `[CTX:screener_bullish_bearish]`

## Sector read

- SHOP sector = **Technology / Software - Application** (per phase-0 `fz`).
- Today's bullish tape is **Technology / semis-led**: NVDA, CDNS, SNDK, META are
  the top single-name bullish-premium names. **Tech is in favour today.**
- **Yellow flag:** SHOP is bucking its own leading sector — net-bearish flow while
  Tech leads the bullish tape. Hand this to phase-6 to resolve (idiosyncratic
  weakness vs sector strength). `[CTX]`

## Self-history (parquet present — 31 sessions)

- Today net-directional −$1.08M → **32.3 self-percentile** (a normal, mildly
  bearish day for SHOP; not an extreme). [DUCKDB]
- Last 8 sessions net-directional ($M): −0.05, +0.84, −1.52, −1.22, −0.61, −1.40,
  −0.38, **−1.08** → net-bearish in 7 of 8. **Persistent, low-grade bearish flow
  regime** — the durable context signal, more than today's single print. [DUCKDB]
- Today total option volume 59,256 contracts; iv_rank 85.6 (elevated).

## Source

CLI (`uw screener bullish-bearish` ×2, `uw screener volume-vs-average`,
`uw insights deep-dive`) **+ DuckDB** escape hatch (`lib/duckdb-cuts.md §C`) for
exact universe + self-history percentiles on the local
`stock-screener-2026-07-17.parquet` (present). "Outside top-60" recorded on both
directional leader boards. SHOP absent from the vol-vs-average ≥2× top-80 list
(today's option volume not unusual vs its 30-day average).

## Verdict for downstream

```
universe_pctile_total_prem:  97.7
universe_rank_net_dir:       1.8 pctile (net-bearish tail); outside top-60 by magnitude
sector_leadership:           TECHNOLOGY leading (bullish) — SHOP bucking it (net-bearish); yellow flag
iv_rank:                     85.6
implied_move_pct:            0.49%   # implied_move_perc field; CROSS-CHECK in phase-4/9 (looks daily, low vs 75% IV)
self_pctile_net_dir:         32.3
unusual_verdict:             BUSY_NAME_NORMAL_DAY
```

**Three things later phases should remember:**
1. This is a top-2.3%-premium *liquid* name but today's directional flow is NOT a
   spike (self-pctile 32) — do not read raw premium magnitude as conviction. Cap
   phases 1–2 confluence at `+`.
2. SHOP has been **net-bearish 7 of the last 8 sessions** — the durable signal is
   a persistent low-grade bearish tilt, not today's single day.
3. **Sector divergence yellow flag:** Tech/semis lead the bullish tape while SHOP
   is net-bearish — phase-6 must resolve whether SHOP weakness is idiosyncratic.

**Open questions:** Is the persistent bearish premium dealer-hedging / put-buying
protection or genuine directional bearish conviction? (phases 1, 3, 4 resolve.)
Why is a 75%-IV name showing a 0.49% implied move — verify the field in phase-4.
