# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** RDDT
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T00:00:00Z
**Upstream phases cited:** phase-0-intake.md

## Summary

RDDT's flow today is **genuinely unusual — on the bearish axis.** The name is a
busy options name (total option premium in the **97.8th universe percentile**,
80th self-percentile), but the directional tilt is the standout: net-directional
premium (bullish−bearish) of **−$6.98M** puts RDDT in the **0.5 universe
percentile** (among the most net-bearish of 4,532 optionable names) and the
**0.0 self-percentile** — i.e. **today is the single most net-bearish flow day
in RDDT's entire 31-session local window.** Volume is elevated (88th universe /
90th self pctile) and the put/call ratio jumped to 0.92 (vs ~0.4–0.5 typical
recently). This is happening into a multi-week downtrend: RDDT peaked ~$172 on
2026-05-05 and has bled to **$141.67** (−18%). The one anomaly: IV rank is only
**18.7** — options stayed cheap through the entire decline. Context for
downstream: this is *not* a busy name having a normal day; the bearish flow is
real and cross-sectionally extreme, but the absolute dollars are modest and the
cheap IV says the market is not pricing panic. Phases 1–4 must confirm whether
the bearish net-premium is genuine directional selling or hedging/skew noise.

## Universe ranking (today, 2026-05-22)

- **Net bearish premium:** RDDT `net_flow −$6,975,679` ranks **~22nd of the full
  universe** on `screener_bullish_bearish direction=bearish`, behind SPY, MSTR,
  NVDA, SNDK, GOOGL, SMH, META, IWM, COIN, GOOG, IREN, MOD, QQQ, FUTU, EEM, VSAT,
  HOOD, DIA, AMD, TLT, AVGO. Stripping the 7 ETFs/indices above it (SPY, SMH,
  IWM, QQQ, EEM, DIA, TLT), RDDT is **~15th among single names** on net bearish
  flow. [CTX] [SENT precursor]
- **Exact universe percentiles** (DuckDB §C, N=4,532 optionable names):
  - total premium: **97.8th** (very busy)
  - net-directional premium: **0.5th** (near the most-bearish in the universe)
  - IV rank: **19.6th** (cheap vol)
  - volume-vs-avg: **88.3rd** (elevated)
  `[CTX:universe_pctile DUCKDB]`
- **Leaders today (single names):** the day's directional tape is led on the
  bearish side by mega-cap tech and semis — NVDA (−$97M), MSTR (−$121M), SNDK
  (−$48M), GOOGL (−$36M), AMD, AVGO, META; on the bullish side by AAPL (+$81M),
  TSLA (+$53M), DELL, IBM, GLD, ASTS, RKLB. RDDT is not a directional *leader* in
  dollars, but it is firmly in the **net-sold** cohort.

## Sector read

RDDT is **Communication Services**. The sector is **split-to-lagging** today:
its mega-cap peers GOOGL/GOOG (−$36M / −$17M), META (−$23M), NFLX, SPOT all sit
in the bearish top-50; only smaller names (ASTS, TTWO, RBLX) are bid. The broad
tape is risk-off — SPY net −$168M, QQQ −$13M, and the strongest selling is in
semis (SMH −$33M, NVDA, AMD, AVGO, SNDK). RDDT is being sold *with* its large-cap
comms peers and *with* the broad risk-off tape — there is no single-name
idiosyncratic bid fighting the macro here. Hands phase-6 a head start: this is a
broad-market de-risking day, not a clean RDDT-specific story. **Yellow flag for
phase-6 to resolve only if** a later phase finds RDDT-specific bullish positioning
fighting the tape (none seen yet).

## Self-history (DuckDB §C — N=31 sessions, gap-aware)

Today vs RDDT's own ≤31-session distribution (note: April 2026 absent — window is
2026-03-13→03-27 then 04-27→05-22):

| Metric | Today (5/22) | Self-percentile |
|--------|-------------|-----------------|
| net-directional premium | −$6.98M | **0.0** (most bearish in window) |
| total option premium | $38.07M | 80.0 (busy) |
| total volume | 7,429,085 | 90.0 (elevated) |

`[CTX:self_pctile DUCKDB]`

Self-history series confirms the regime change: RDDT ran from ~$132 (3/13) to a
**$172 peak on 5/05** (the 5/01 session printed +$19.04M net-bull premium on
$114.8M total premium and 13.2M volume — the biggest bullish day in the window),
then rolled over: 5/06 −$2.9M, 5/08 −$5.3M, 5/12 −$3.8M, 5/20 −$6.6M (px $146.72),
and now 5/22 −$6.98M (px $141.67). **Four of the last five sessions are net-bearish
and the magnitude is accelerating.** IV rank collapsed from ~67 (late Apr) to 18.7
now — the down-move came with *falling* IV, classic orderly distribution rather
than a vol-driven panic.

## Source

MCP (`insights_deep_dive`, `screener_bullish_bearish` ×2, `screener_volume_vs_average`)
+ DuckDB escape hatch §C for exact universe/self percentiles. RDDT was **outside
the top-50 on `screener_volume_vs_average`** (that list is dominated by tiny
illiquid names with 100×+ ratios) — the precise 88th-percentile vol-vs-avg comes
from the DuckDB cut, which is the trustworthy read for a liquid large-cap.

## Verdict for downstream

```
universe_pctile_total_prem:  97.8
universe_rank_net_dir:       ~22nd universe / ~15th single-name (net BEARISH); universe net-dir pctile 0.5
sector_leadership:           Communication Services lagging; broad tape risk-off (SPY net -$168M, semis sold)
iv_rank:                     18.7
implied_move_pct:            0.56%   # 1-day; iv30d 62.0%
self_pctile_net_dir:         0.0     # most bearish net-directional day in 31-session window
unusual_verdict:             GENUINELY_UNUSUAL (bearish)
```

- **Bias from this phase:** neutral by mandate (context only) — but the context
  is *unusually bearish*, not benign. Confluence is NOT capped at `+` here (the
  BUSY_NAME_NORMAL_DAY cap does not apply); the flow is genuinely unusual.
- **Conviction (that the flow is unusual):** 4/5
- **Three things later phases should remember:**
  1. Today is RDDT's **most net-bearish flow day** in the 31-session window
     (self-pctile 0.0, universe 0.5) — phases 1–2 should expect to *find* the
     bearish footprint, and flag loudly if they instead find bullish flow.
  2. The down-move from $172→$142 came with **collapsing IV (rank 18.7)** — cheap
     options. Phase-4 (structure) and phase-9 (sizing) should note long premium is
     *cheap* here; debit structures are favoured over credit.
  3. RDDT is being sold **with** its comms peers and the broad risk-off tape — no
     idiosyncratic bid is fighting the macro (phase-6 input).
- **Open questions:** Is the −$6.98M net-bearish premium genuine directional put
  buying / call selling, or skew/hedging artifact? Is the 5/01 $172 bullish blow-off
  being unwound (position rolls)? → phases 1, 3, 4.
