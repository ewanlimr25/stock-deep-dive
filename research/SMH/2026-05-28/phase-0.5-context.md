# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** SMH
**As-of date:** 2026-05-28
**Generated:** 2026-05-29T12:00:00Z
**Upstream phases cited:** phase-0-intake.md

## Summary

SMH (VanEck Semiconductor ETF, $68.3B AUM) is a perpetually-busy options name, so
its **size** today is unremarkable for itself — total option premium $218.3M sits
at the **51.5th self-percentile** (a normal-to-quiet dollar day for SMH, below its
recent $266–360M median) and option volume is only **1.6× its 30-day average**
(below the 2× "unusual" bar). What *is* genuinely unusual is the **direction**: net
directional premium ranks at the **0.1 universe percentile** (one of the most
bearish names in the entire ~6,000-name optionable universe today, #9 on net
bearish premium at −$21.0M) and the **bottom 12th self-percentile** for SMH, with a
put/call ratio of **7.26** sitting in the **top 6% of SMH's own history**
(93.9 self-pctile). All of this is happening with SMH pinned at **96.7% of its
52-week range** ($599.83 vs a $612.30 high). Read: *not a volume blow-out, but a
genuinely lopsided put/hedging skew into strength* — the basket is being insured
while single-name semis leaders are bid.

## Universe ranking (today, 2026-05-28)

| Metric | SMH value | Universe percentile | Read |
|--------|-----------|---------------------|------|
| Total option premium | $218.3M | **99.3** `[DUCKDB]` | SMH is a top-1% premium name *every* day (mega-ETF) — not informative alone |
| Net directional premium | −$21.0M | **0.1** `[DUCKDB]` | Near the single most bearish read in the universe; **#9 on net bearish premium** |
| IV rank | 84.6 | **94.5** `[DUCKDB]` | Vol is rich vs the universe and vs SMH's own range |
| Option vol ÷ 30d avg | **1.6×** | 81.8 `[DUCKDB]` | Elevated but **below the 2× unusual bar** — size is normal |
| Put/call ratio | 7.26 | — | Extreme put skew |

Bullish-premium leaders today (single names): TSLA, MSFT, MU (#4), STX (#9),
MRVL (#18), SNDK (#19), SOXL (#24), QCOM (#26), NVDA (#35), AVGO (#46), TSM (#47).
Bearish-premium leaders: SPX, ZS, META, AMD (#5), LITE (#6), **SMH (#9)**, ISRG,
plus the optical/equipment complex (ASML #23, CRDO #24, MTSI #25, AAOI #14, MXL #22).

## Sector read

Semis/Technology is **two-sided and leadership-narrow** today: the single-name
leaders (MU, STX, MRVL, SNDK, NVDA, AVGO, TSM) draw net **bullish** premium, while
the **basket itself (SMH) and the second-tier/equipment names** (AMD, ASML, the
optical complex LITE/AAOI/CRDO/MXL) draw net **bearish** premium. That divergence —
leaders bid, basket hedged — is the central cross-sectional fact and hands phase-6
a clean question: is this healthy rotation-into-leaders, or distribution masked by
a few mega-caps? SMH is *not* a name in disfavour; it is a name whose holders are
buying insurance near the highs.

## Self-history (SMH vs its own 34 local sessions)

| Metric | Today's self-percentile | Read |
|--------|-------------------------|------|
| Net directional premium | **12.1** `[DUCKDB]` | Bottom-12% — unusually bearish *for SMH* |
| Total premium | 51.5 `[DUCKDB]` | Median dollar day — **size is normal** |
| Put/call ratio | **93.9** `[DUCKDB]` | Top-6% put-heavy *for SMH* |
| IV rank | 78.8 `[DUCKDB]` | High end of SMH's own recent range |

Sessions in window: **34** (note: spans the 2026-03-28→04-26 local gap — the recent
contiguous run 2026-04-27→05-28 is clean). Recent price/flow path:

| Date | Close | net_dir $M | P/C | IV rank |
|------|-------|-----------|-----|---------|
| 05-28 | **599.83** | −20.4 | 7.26 | 84.6 |
| 05-27 | 595.50 | −19.5 | 7.28 | 87.4 |
| 05-26 | 602.29 | +30.9 | 5.15 | 92.3 |
| 05-22 | 576.32 | −27.4 | 9.29 | 77.3 |
| 05-20 | 564.66 | +9.4 | 2.76 | 80.8 |
| 05-19 | 543.67 | +2.3 | 3.27 | 81.3 |

SMH ran **+10% in ~7 sessions** ($543→$602) and is consolidating $595–602. Flow is
**persistently put-skewed even on up days** (P/C 5–9, net_dir negative on 4 of the
last 6 sessions) with IV rank stuck 77–92. That combination — new highs + relentless
put buying + sticky-high IV — is the textbook signature of **hedging into strength**,
not a directional crash bet.

## Source

CLI rankings (`uw screener bullish-bearish` / `volume-vs-average`) **+ DuckDB
escape hatch §C** for exact universe and self-history percentiles (`lib/duckdb-cuts.md`).
SMH was **outside the top-50 on volume-vs-average** (that list is dominated by tiny
illiquid names with 100×+ ratios; SMH's true 1.6× came from the DuckDB cut).
Yahoo fundamentals errored (HTTP 401) in `insights deep-dive` — irrelevant for an ETF.

## Verdict for downstream — `[CTX:]` block

```
universe_pctile_total_prem:  99.3            # mega-ETF; uninformative alone [DUCKDB]
universe_rank_net_dir:       9 (bearish; universe net_dir pctile 0.1) [DUCKDB]
sector_leadership:           SEMIS two-sided — single-name leaders bid, basket/equipment hedged
iv_rank:                     84.6
implied_move_pct:            1.71            # feeds phase-9 expected move (N4)
self_pctile_net_dir:         12.1            # bottom-12% = bearish extreme for SMH [DUCKDB]
self_pctile_total_prem:      51.5            # median $ day — SIZE IS NORMAL [DUCKDB]
self_pctile_put_call:        93.9            # top-6% put-heavy for SMH [DUCKDB]
unusual_verdict:             BUSY_NAME_NORMAL_DAY (size) + GENUINELY_UNUSUAL bearish/put skew
```

**Downstream calibration note (read by phases 1–2, 9):** Because total premium is
only median-for-SMH and vol is 1.6× (< 2×), the raw $131.5M put premium must **not**
on its own justify a `++` magnitude confluence in phases 1–2 — cap the *size* read
at `+` per `rubrics/confluence-scoring.md` (BUSY_NAME cap). However, the **directional
skew is a genuine signal** (0.1 universe net_dir pctile, P/C at 93.9 self-pctile) and
should carry through as a real — if hedging-flavoured — bearish/insurance lean. The
open question for phases 1–4: is the put flow **protective** (basket hedge by holders
long the bid single names, IV rank high) or **directional** (someone pressing semis
lower)? The narrow-leadership + new-highs context tilts toward *protective*, but the
530P 8DTE OI build (+50,795, see phase-3) needs resolution.

This phase sets **context only** — no directional bias is asserted; the bias is the
plurality of phases 1–8.
