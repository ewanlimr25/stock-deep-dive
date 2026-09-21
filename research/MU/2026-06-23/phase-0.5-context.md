# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** MU
**As-of date:** 2026-06-23
**Generated:** 2026-06-23
**Upstream phases cited:** phase-0-intake.md

## Summary

MU's flow today is **genuinely unusual on every axis that matters** — and the
single most important fact in the whole dive surfaces here: **MU reports earnings
tomorrow, 2026-06-24 postmarket** (`next_earnings_date`, `er_time=postmarket`,
confirmed in both `insights deep-dive` and the screener parquet). Against the full
4,615-name optionable universe, MU sits at the **100th percentile of total option
premium** (the single largest premium name on the tape) and the **0th percentile of
net-directional premium** — i.e. it is the **#1 net-*bearish* name market-wide**
(net_flow = **−$145.2M**). IV rank is pinned at **100** (97th universe percentile),
IV30d = **107%**, and the implied move into the print is **±10.91%** (±$114.7 on a
$1051.77 close). Versus its own 51-session history this is MU's **most net-bearish
day on record (0th self-percentile)** with total premium in its **78th** self-
percentile and volume in the **96.7th** universe percentile — elevated, not a normal
day. The entire semiconductor complex is being sold today (NVDA, SOXL, AMD, INTC,
MRVL, SNDK, AVGO all in the bearish top-12), so MU's bearish lean is sector-wide —
but **MU leads it**. Caveat for downstream: net-aggressor flow leans bearish, yet
this is a *two-sided* pre-earnings book ($2.03B bearish vs $1.89B bullish premium,
PCR 1.01) — phase 1 must separate genuine directional conviction from event hedging.

## Universe ranking (single names, ETFs set aside)

| Metric | MU standing | Source |
|--------|-------------|--------|
| Net **bearish** premium | **#1 in the market** (net_flow −$145.2M, PCR 1.01) | `screener bullish-bearish --direction bearish` rank 1 |
| Net **bullish** premium | outside top-60 | `screener bullish-bearish --direction bullish` |
| Total option premium | **100.0th pctile** of 4,615 names (largest on tape) | §C DuckDB |
| Net-directional premium | **0.0th pctile** (most bearish in universe) | §C DuckDB |
| IV rank | **97.0th pctile** universe (raw iv_rank=100) | §C DuckDB / `iv-rank` rank 21 |
| Volume vs 30d avg | **96.7th pctile** universe (elevated) | §C DuckDB |

**Bearish-tape leaders (single names):** MU (−$145.2M) › NVDA (−$105.8M) › SOXL
(−$93.4M) › TSLA (−$66.2M) › AMD (−$44.5M) › INTC (−$31.2M) › MRVL (−$30.3M) ›
SNDK (−$27.7M) › AVGO (−$25.3M). Semis own the bottom of the directional tape.

## Sector read

**Technology / Semiconductors is LEADING the bearish tape today.** Of the top-12
net-bearish single names, eight are semis (MU, NVDA, SOXL[3x semi ETF], AMD, INTC,
MRVL, SNDK, AVGO). This is a **sector-wide de-risk**, not an MU-idiosyncratic move —
hands phase-6 a clear head start: the macro question is whether semis are being sold
ahead of MU's print as the bellwether, or as part of a broader risk-off rotation.
Note SMH (semi ETF) is actually #3 on the *bullish* tape (+$50.1M net) with IV rank
100 — so there is two-sided semi positioning, consistent with hedging into a
catalyst rather than outright capitulation.

## Self-history (parquet present — 51 sessions, gap-aware)

| Metric | MU self-percentile | Note |
|--------|--------------------|------|
| Net-directional premium | **0.0** | Most net-bearish day in MU's own 51-session window |
| Total premium | **78.0** | Elevated vs its own history (event-driven) |
| Sessions in window | 51 | Non-contiguous (2026-03 gap); true N stated per `§ gap` |

The 0th self-percentile on net-direction confirms the bearish lean is unusual *for
MU itself*, not just cross-sectionally — but it coincides with the highest-premium,
max-IV pre-earnings session, so "bearish" here is inseparable from event positioning.

## Source

CLI (`uw screener` ×4 + `uw insights deep-dive`) **plus** DuckDB escape hatch §C
(`lib/duckdb-cuts.md`) for exact universe + self-history percentiles. "Outside
top-60" recorded for bullish net premium and the volume-ratio≥2 leaderboard (the
latter resolved by the 96.7th-pctile DuckDB read — MU's volume *is* elevated; it
simply isn't among the 60 highest *ratios*). No tool errors.

## Verdict for downstream

```
universe_pctile_total_prem:  100.0
universe_rank_net_dir:       #1 most bearish (0.0 percentile)   # net_flow -$145.2M
sector_leadership:           SEMIS leading the bearish tape today (Tech sold)
iv_rank:                     100        # 97th universe pctile; IV30d 107%
implied_move_pct:            10.91%     # ±$114.7 on $1051.77 — feeds phase-9 N4
self_pctile_net_dir:         0.0        # most bearish day in MU's own 51-session history  [CTX:self_pctile DUCKDB]
unusual_verdict:             GENUINELY_UNUSUAL
```

**Calibration note for phases 1–9:** `unusual_verdict=GENUINELY_UNUSUAL` (top-decile
net-directional AND elevated volume AND maxed IV), so the phase-1/2 confluence cap
for "busy-name-normal-day" does **not** apply. BUT the unusualness is **event-driven**
(earnings tomorrow postmarket) — treat the directional read as *positioning into a
binary*, not a clean trend signal. Any phase-9 trade must price the ±10.91% gap and
the post-print IV crush. This phase sets **context only** — no directional bias is
asserted here; the bias is the plurality of phases 1–8.

## Tool errors

(none)

## DATA NOTE / CORRECTION

(none — all values round-tripped through `jq`/DuckDB on first read)
