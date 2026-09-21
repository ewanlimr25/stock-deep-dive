# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** NTAP
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T00:00:00Z
**Upstream phases cited:** phase-0-intake.md

## Summary

NTAP's options activity is **genuinely unusual in magnitude and volatility, but
flat in direction.** Today's total option premium ($10.84M) sits in the **95.6th
percentile of the 4,532-name optionable universe** and is a **31-session high for
the name itself (100th self-percentile)**; IV rank is **100** (97.8th universe,
100th self) and volume is **2.76× its 30-day average** (94.6th universe, 100th
self). Yet **net-directional premium is bottom-decile — 11.0th universe percentile,
37th self-percentile** — net flat to slightly *negative* (−$0.05M). The headline
call-heavy volume (P/C 0.178) is **not matched by net call premium direction**,
which is the signature of two-sided pre-earnings vol positioning (call buying *and*
overwriting), not one-way accumulation. Earnings land **2026-05-28** (6 sessions
out) with a **10.6% implied move**. NTAP is therefore in a pre-earnings vol coil:
the desk should read the flow as event-charged, **not** as directional conviction.

## Universe ranking (today, N=4,532 optionable names — DUCKDB §C)

| Metric | NTAP value | Universe percentile | Read |
|--------|-----------|---------------------|------|
| Total option premium | $10.84M | **95.6** | Top 5% — the volume is real |
| Net-directional prem (net_call−net_put) | −$0.05M | **11.0** | **Bottom decile — flat/negative** |
| Net bull−bear premium | −$48.5K | **11.0** | Bottom decile — confirms no directional edge |
| IV rank | 100 | **97.8** | Top 2–3% — vol is richly bid |
| Volume vs 30-day avg | 2.76× | **94.6** | Top 5–6% — activity spike is real |

**Directional leaderboard (`screener_bullish_bearish`, top-50):** NTAP is
**outside the top-50 on net bullish premium** (the 50th name, RUTW, has
net_flow +$2.73M; NTAP is −$0.05M). The day's directional leaders are index
products (SPX +$1.04B net, SPXW +$296M) then single names **AAPL (+$81M), TSLA
(+$53M), DELL (+$33M), IBM (+$33M), ADBE (+$23M)**, with a deep semis bench (MU,
QCOM, ARM, INTC, SOXL, TSM, CRDO, ALAB). NTAP is a top-of-tape name by
*magnitude* but a non-participant by *direction*.

## Sector read

NTAP is **Technology**, and Tech is broadly **in favour** on today's directional
tape — AAPL, DELL, IBM, ADBE, NOW, PANW, QCOM, MSFT, ARM all rank in the top-30
net-bullish. **Most relevant peer: DELL ranks #7 (net +$32.7M, IV rank 92.2)** — a
direct storage/server-hardware comparable that also reports in late May. So the
storage/server complex is bid, **but NTAP itself is not following directionally**
(outside top-50, bottom-decile net-dir). **Yellow flag for phase-6:** sector bid +
name flat = NTAP is coiled on its own catalyst, not riding the sector tape. Macro
phase should confirm whether the Tech/storage bid is a tailwind or noise into the
5/28 print.

## Self-history (NTAP vs its own 31-session local window — DUCKDB §C)

| Metric | Self-percentile | Note |
|--------|-----------------|------|
| Total premium | **100.0** | Highest premium in the 31-session window |
| IV rank | **100.0** | Highest IV rank in window |
| Volume vs avg | **100.0** | Highest vol-vs-avg in window (2.76×) |
| Net-directional prem | **36.7** | **Below its own median** — net flat/bearish |

Recent net-directional trail (net_call−net_put, $M): 05-13 **−0.87**, 05-14 −0.17,
05-15 −0.11, 05-18 −0.01, 05-19 +0.07, 05-20 +0.13, 05-21 +0.04, **05-22 −0.05**.
Net-directional premium has been **persistently flat-to-negative** for two weeks;
the only thing that spiked today is *magnitude* and *IV*, not *direction*.
**Mind the gap:** sessions_in_window = 31 *available* sessions, non-contiguous
(03-28 → 04-24 missing) — not a contiguous calendar window (phase-0 §Local data).

## Source

MCP (`insights_deep_dive`, `screener_bullish_bearish`, `screener_volume_vs_average`)
**+ DuckDB escape hatch §C** (exact universe + self-history percentiles — a cut the
MCP cannot express). NTAP was **outside top-50** on the bullish screener and not
present on the volume-vs-average top-50 (that list is dominated by illiquid
micro-names with huge ratios; NTAP's 2.76× is meaningful for a liquid name and is
captured precisely by the §C percentile instead).

## Verdict for downstream

```
universe_pctile_total_prem:  95.6           # DUCKDB §C — top 5%
universe_rank_net_dir:       outside top-50 # 11.0th pctile — bottom decile
sector_leadership:           TECHNOLOGY leading today; NTAP a non-participant directionally (peer DELL #7)
iv_rank:                     100            # insights_deep_dive uw_screener
implied_move_pct:            10.64%         # feeds phase-9 expected-move (N4)
self_pctile_net_dir:         36.7           # DUCKDB §C — below own median
unusual_verdict:  GENUINELY_UNUSUAL (EVENT/VOL — NOT DIRECTIONAL)
```

**[CTX:] guidance phases 1–9 must honour:**
1. The unusualness is **event/volatility**, not direction. Net-directional premium
   is **bottom-decile (11.0 universe / 36.7 self)**. **Phases 1–2 bullish directional
   confluence is capped at `+` (not `++`)** — heavy call volume here is NOT
   accumulation (`rubrics/confluence-scoring.md`).
2. **Earnings 2026-05-28 (6 sessions out), implied move 10.6%, IV rank 100.** Any
   structure spanning the print is a long-vol-into-event / short-vol-into-event
   decision, not a clean directional swing. Phase-9 expected-move math uses 10.64%.
3. **Sector (Tech/storage) is bid (peer DELL #7), NTAP is not following** — phase-6
   must resolve whether that is tailwind or a divergence yellow flag.
