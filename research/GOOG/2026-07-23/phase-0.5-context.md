# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** GOOG · **As-of:** 2026-07-23 · **Generated:** 2026-07-24T01:18:35Z
**Upstream:** phase-0-intake.md (UW reachable, as-of = latest date, no gap)

## Summary

GOOG's flow today is **genuinely unusual — and unusually bearish**. It is a busy
mega-cap (total option premium in the 99.8th universe percentile / 98.6th of its
own 72-session history — enormous engagement), but the *direction* is the story:
GOOG sits at the **0.0 universe percentile on net-directional premium** (the single
most net-bearish name in the ~6,000-name optionable universe today) and at the
**1.4 self-history percentile** — i.e. today is among the most net-bearish flow
days GOOG has printed in its available window. Both Alphabet share classes lead the
bearish tape: **GOOGL #3** (net −$59.6M) and **GOOG #6** (net −$49.4M) on net
bearish premium. This is not a big-numbers-normal-day; it is a real, cross-
sectionally-confirmed bearish skew. Context only — the directional call is the
plurality of phases 1–8; but downstream phases should treat the bearish flow as
signal, not noise, and phase-6 must resolve why Comm-Services/Alphabet is being sold.

## Universe ranking (as-of 2026-07-23)

- **Net bullish premium:** GOOG **outside top-50** (not a directional buy leader).
- **Net bearish premium:** GOOG **#6** (net_flow −$49.38M; bearish premium
  $308.0M) — GOOGL #3 (net −$59.62M). Bearish top-10 leaders: TSLA (−247M), LULU,
  GOOGL, GLD, QQQ, **GOOG**, MSTR, AMZN, SOXL, AMD.
- **Volume-vs-average (min ratio 2, top-60):** GOOG **outside the list** — its
  raw volume is not a 2× blow-off, though DuckDB puts its vol-vs-avg at the 97.3
  universe percentile (elevated, just short of the 2× screen).
- Net bullish leaders (setting ETFs SPX/SPXW/SPY/XSP aside): MU (+104M), DELL,
  IBM, SNDK, CVNA, NFLX — **semis + select tech lead the buy tape.**

## Sector read

- GOOG sector: **Communication Services**.
- Directional tape today: **Technology is mixed/two-sided** (13 of top-30 bought
  vs 12 of top-30 sold). **Communication Services skews to the sell side** (4 of
  top-30 bearish names vs 2 of top-30 bullish) — and Alphabet (both classes) *is*
  the Comm-Services bearish leadership. So GOOG's sector is mid-pack-to-lagging
  and GOOG is the name being sold within it. Hands phase-6 a clear question:
  is this Alphabet-specific or a Comm-Services rotation-out?

## Self-history (local parquet present — DuckDB §C)

Over **72 available sessions** (mind the non-contiguous window):
- `self_pctile_net_dir`: **1.4** — today ≈ GOOG's most net-bearish day in window.
- `self_pctile_total`: **98.6** — today's total premium near its own record high.
- Universe percentiles today: total_prem **99.8**, net_dir **0.0**, iv_rank
  **38.0**, vol_vs_avg **97.3**. `[CTX:universe_pctile DUCKDB]` `[CTX:self_pctile DUCKDB]`

## Source

CLI (`uw screener bullish-bearish` ×2, `volume-vs-average`, `insights deep-dive`)
**+ DuckDB §C** (local snapshot present for 2026-07-23). "Outside top-N" recorded
for bullish-premium and the 2×-volume screen.

## Verdict for downstream

```
universe_pctile_total_prem:  99.8
universe_rank_net_dir:       #6 net bearish (single most net-bearish pctile 0.0)
sector_leadership:           Communication Services lagging/sold today; GOOG is the sold name
iv_rank:                     38.3
implied_move_pct:            1.57      # from insights_deep_dive (implied_move_perc); feeds phase-9 N4
self_pctile_net_dir:         1.4       # 72-session window — near most-bearish
unusual_verdict:             GENUINELY_UNUSUAL   # unusually BEARISH — extreme net-dir + top-decile engagement
```

**Absolute numbers behind the rank (insights deep-dive):** bullish_premium
$258.7M, bearish_premium $308.0M (net −$49.4M); call_premium $215.9M, put_premium
$406.6M; call_volume 327,406, put_volume 233,311; put/call ratio 0.713 (by
volume); iv30d 0.324, iv_rank 38.3, implied_move 1.57% ($4.99); next earnings
2026-11-04. Note the **premium/volume divergence**: more call *contracts* trade
(cheap OTM call lottery), but put *premium* ($406.6M) dwarfs call premium
($215.9M) — the dollars lean bearish/protective. Phase-1 to resolve.

## Interpretation note

`unusual_verdict = GENUINELY_UNUSUAL` here fires on the **bearish** side: extreme
net-directional premium (universe pctile 0.0 / self pctile 1.4) plus top-decile
engagement. Phases 1–2 confluence is NOT capped at `+` (this is not a
busy-name-normal-day); the flow is real. Direction remains the job of the phase
plurality — but the prior is bearish, not bullish.
