# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** KWEB
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T00:00:00Z
**Upstream phases cited:** phase-0-intake.md

## Summary

KWEB's flow today is **genuinely unusual on direction but ordinary on volume**.
Net-directional premium (+$2.65M call-over-put) sits at the **99.1 percentile of
the ~6,100-name optionable universe** `[CTX:universe_pctile DUCKDB]` and the
**83.3 percentile of KWEB's own 31 local sessions** `[CTX:self_pctile DUCKDB]` —
this is the **second consecutive bullish-skew day** after 05-21's +$11.41M net-dir
(the single largest bullish print in the local window), and it lands while price
grinds to the **bottom of its two-month range (~$26.91, down from ~$30 in
mid-March)**. Yet total option volume is a **normal day for the name** (vol_x not
elevated; KWEB absent from the universe volume-vs-average top-50; self total-premium
percentile only 60.0). Read: this looks like **quiet call accumulation into price
weakness**, not a loud crowded day — exactly the footprint that does *not* show up as
a volume spike. KWEB's own theme (China internet) is **not** in the US tape's
leadership today (index + semis/tech lead), so phase-6 must source direction from
China policy / ADR / FX, not US sector rotation.

## Universe ranking (2026-05-22)

| Metric | KWEB value | Universe percentile | Read |
|--------|-----------|---------------------|------|
| Total premium (call+put) | $16.33M | **96.6** | high vs universe |
| Net-directional premium (call−put) | **+$2.65M** | **99.1** | top 1% — but just *outside* MCP top-50 (index/mega-caps fill it) |
| IV rank | 38.9 | 55.7 | mid-pack; options not expensive |
| Volume vs 30d | (normal) | 94.0* | *pctile vs share-vol; option volume itself NOT in top-50 |

MCP `screener_bullish_bearish` (bullish, top-50) leaders are dominated by index/ETF
behemoths — **SPX** (net_flow $1.04B), **SPXW** ($296M), **AAPL** ($81M), **TSLA**
($53M), **DELL** ($33M), **IBM** ($33M), **GLD** ($31M). KWEB's +$2.65M net_flow
falls just under the 50th-place cutoff (RUTW $2.73M) — consistent with its 99.1
universe percentile (≈ rank 55 / 6,171). `[CTX:universe_rank_net_dir]`

## Sector read

The US directional tape today is led by **broad index (SPX/SPXW), large-cap tech
(AAPL, MSFT, DELL, IBM) and semis (MU, INTC, SOXL, QCOM, ARM, ALAB)**. KWEB's own
theme — **China internet** — is *not* a US leadership sector today. The only
China-complex names showing life are **Chinese brokers**: FUTU (26.7× its 30-day
option volume `[CTX:vol_vs_avg]`) and TIGR / UP Fintech (IV rank 100, in the bullish
net-flow top-50). That is a thin, broker-specific flicker — *not* a broad
China-internet bid. Net: KWEB is moving on its **own idiosyncratic call flow**, not
a sector wave. **Yellow flag for phase-6 to resolve**: name showing bullish skew
while its sector is not being chased on the US tape — the catalyst, if real, is
China-side (policy / stimulus / FX), so phase-6 must look there.

## Self-history (31 local sessions; mind the 03-28→04-24 gap, N=31 not contiguous)

KWEB net-directional premium ($M) and price, by session:

- **Recent bullish cluster:** 05-13 +8.65 ($30.59, IVR 88.8) → 05-14 +4.63 → … →
  **05-21 +11.41** ($27.63) → **05-22 +2.65** ($26.91). Two of the three largest
  bullish-skew days in the window are the **last two sessions**, and they print as
  price makes *new local lows*.
- **Bearish extremes** were all back in **March**: 03-23 −11.75, 03-26 −8.30.
- Total-premium percentile today (self) = 60.0 → a median-activity day in dollar
  terms; the signal is the **skew**, not the size. `[CTX:self_pctile DUCKDB]`
- IV rank fell from a mid-May peak of 88.8 (05-13) to **38.9** today — the call
  accumulation is happening into *cheaper*, not richer, vol.

## Source

MCP (`insights_deep_dive`, `screener_bullish_bearish`, `screener_volume_vs_average`)
**+ DuckDB escape hatch §C** (exact universe + self-history percentiles; local
snapshot present for 2026-05-22, DuckDB available). "Outside top-50" recorded for
net bullish premium (it is 99.1 universe pctile, just below the index-dominated
top-50 cutoff). vol_x raw ratio uses the screener's `avg30_volume` (underlying
share volume), so the 94.0 pctile is share-relative; KWEB option volume itself is a
normal day (absent from the option-volume-vs-average top-50).

## Verdict for downstream

```
universe_pctile_total_prem:  96.6
universe_rank_net_dir:       outside top-50 (99.1 universe pctile ≈ rank ~55/6171)
sector_leadership:           China-internet LAGGING US tape (index+semis/tech lead); only China-broker flickers (FUTU/TIGR)
iv_rank:                     38.9
implied_move_pct:            0.45            # daily (implied_move_perc); feeds phase-9 N4
self_pctile_net_dir:         83.3
unusual_verdict:             GENUINELY_UNUSUAL   # directional-skew driven (top-1% universe net-dir, 83rd self, 2nd consecutive bullish day into the low); volume is a NORMAL day — do NOT claim a volume surge
```

**Calibration note for phases 1–2 (per `rubrics/confluence-scoring.md`):** the
directional skew is genuinely unusual, so confluence is *not* capped to `+`. BUT
because total volume is normal (not a 2× surge) and the name's theme lags the US
tape, phases 1–2 should frame this as **quiet accumulation**, not a momentum
breakout — magnitude claims must rest on the *skew/persistence*, not on volume.

## Tool errors

`insights_deep_dive` → `yahoo_fundamentals: HTTP 401` (yfinance block; non-fatal,
fundamentals come from phase-7b/Finnhub). All UW screener + DuckDB cuts succeeded.
