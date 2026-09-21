# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** DOCN
**As-of date:** 2026-07-17
**Generated:** 2026-07-20T01:05:00Z
**Upstream phases cited:** phase-0-intake.md

## Summary

DOCN is a heavily-optioned name in absolute terms (94.6th-pctile total option
premium across the ~universe, 96.3rd-pctile IV rank) but **today is a normal-to-
quiet day *for DOCN itself*** — self-history total premium sits at only the 31.3rd
pctile and net-directional flow at the 52.2nd pctile over its own 68 available
sessions. It is **outside the top-50** on every cross-sectional CLI leaderboard
(net-bullish, net-bearish, vol-vs-average, IV-rank-high). The one genuinely
extreme reading is **IV rank 99.12** — DOCN's implied vol is pinned near the top
of its range ahead of **earnings on 2026-08-04** (~18 days out). Verdict:
**BUSY_NAME_NORMAL_DAY** — this is a pre-earnings vol story, not an unusual
directional-flow day. Per `rubrics/confluence-scoring.md`, phases 1–2 confluence
is capped at `+` (not `++`).

## Universe ranking

- **Net bullish premium:** DOCN **outside top-50** (CLI list). Leaders (single
  names, ETFs aside): NVDA +$81.6M, CDNS +$55.4M, SNDK +$42.7M, META +$35.1M.
  Index/ETF top: SPX +$1.62B, NDX +$400M, SPXW +$178M, GLD +$44.7M.
- **Net bearish premium:** DOCN **outside top-50**. Leaders: SPY −$161.5M,
  QQQ −$72.1M, SMH −$54.7M, SLV −$32.9M, MU −$29.4M.
- **Volume-vs-average:** DOCN **outside top-50** (leaders are illiquid micro-caps
  REGL/SRL/PSK — not comparable). DuckDB says DOCN vol-vs-avg is 79.4th-pctile —
  elevated but not extreme.
- **DuckDB exact universe percentiles** `[CTX:universe_pctile DUCKDB]`:
  total_prem **94.6** · net_dir **91.9** · iv_rank **96.3** · vol_vs_avg **79.4**.
  High absolute standing (busy, well-optioned name) — but see self-history.

## Sector read

Today's directional tape is led by **index + semis/EDA** on the bull side
(NVDA, CDNS) and **broad-index + semis hedging** on the bear side (SPY, QQQ,
SMH, MU). DOCN (cloud-infrastructure / application software) is **not a
directional leader either way** — its sub-sector is mid-pack. Net: no
cross-sectional tailwind or headwind from sector rotation today; phase-6 to
resolve whether software is in or out of favour on the swing horizon.

## Self-history (parquet present — 68 available sessions, gap-aware)

`[CTX:self_pctile DUCKDB]` — over DOCN's own ≤68 available screener sessions
(non-contiguous; 2026-03-28→04-24 hole per phase-0):
- **self_pctile_net_dir: 52.2** — today's net direction is dead-median for DOCN.
- **self_pctile_total: 31.3** — today's total option premium is *below* DOCN's
  own median (a quieter-than-usual tape for the name).
- Interpretation: nothing about *today's* flow is unusual for DOCN. The elevated
  absolute standing is DOCN's baseline as a well-optioned name, amplified only by
  the pre-earnings IV spike.

## Own uw_screener block (absolute numbers behind the rank)

- bullish_premium $2.886M vs bearish_premium $2.732M → **net +$154K** (≈53%
  bullish; essentially balanced) `[CTX:insights_deep_dive]`
- call_premium $3.006M vs put_premium $2.998M (balanced); call_vol 2,957 /
  put_vol 2,555 → **put_call_ratio 0.864** (mild call lean)
- **iv_rank 99.12**, iv30d 1.146 (≈114% — very high), volatility 17.40
- **implied_move 2.14 / implied_move_perc 1.80%** (near-dated expected move)
- total_open_interest 147,920 · **next_earnings_date 2026-08-04**
- Top OI *builds* today skew upside/longer-dated: **Aug-21 $145C +206**,
  7/24 $100C +59, 7/24 $105P +48, Aug-21 $130P +31, Aug-7 $150C +28.

## Source

CLI (`uw screener` ×4 + `uw insights deep-dive`) **+ DuckDB §C** (exact universe
& self-history percentiles; parquet present for as-of). "Outside top-50" recorded
on all four CLI leaderboards. `yahoo_fundamentals` errored (HTTP 401) inside the
deep-dive payload — non-blocking, fundamentals come from phase-7b.

## Verdict for downstream

```
universe_pctile_total_prem:  94.6
universe_rank_net_dir:       outside top-50 (91.9 pctile via DuckDB)
sector_leadership:           software/cloud mid-pack today (index+semis lead; SMH/MU sold)
iv_rank:                     99.12
implied_move_pct:            1.80        # near-dated; earnings move will be larger
self_pctile_net_dir:         52.2
unusual_verdict:             BUSY_NAME_NORMAL_DAY
```

- **Bias from this phase:** neutral (context only — sets no direction)
- **Conviction:** n/a (context modifier)
- **Three things later phases should remember:**
  1. **BUSY_NAME_NORMAL_DAY** → cap phases 1–2 confluence at `+`; do not read raw
     absolute premium as an unusual-flow signal for DOCN.
  2. The real anomaly is **IV rank 99 into Aug-4 earnings** — this is a
     volatility/event setup; phase-4/7c/9 must treat elevated IV as the headline.
  3. Directional flow is **balanced** (net +$154K, P/C 0.86, self net-dir 52nd
     pctile) — no conviction directional edge from the tape alone yet.
- **Open questions:** Does phase-1's intraday sweep/tape detail reveal directional
  intent that the balanced EOD screener hides? Is the Aug-21 $145C OI build new
  positioning or a roll? (phase-1/phase-3 to resolve.)
