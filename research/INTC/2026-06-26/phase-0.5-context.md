# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** INTC
**As-of date:** 2026-06-26
**Generated:** 2026-06-27T09:51:45-0400
**Upstream phases cited:** phase-0-intake.md

## Summary

INTC's options tape today is **genuinely unusual — and it is unusual to the bearish
side.** Total option premium ($566.1M) sits in the **99.8th percentile of the entire
4,589-name optionable universe** [CTX:universe_pctile DUCKDB], yet net-directional
premium is **−$50.4M, the 0.1th percentile** — i.e. INTC is one of the most net-bearish
names in the whole market (ranked **#5 on the net-bearish leaderboard**, behind only
SPX, MU, SPY, SNDK). Against its own 54-session history this is the **7.5th percentile
on net-direction** — among INTC's most bearish days on record [CTX:self_pctile DUCKDB].
The one axis that is *not* extreme is raw volume-vs-average: INTC is outside the top-50
on `screener volume-vs-average ≥2` — the classic busy-mega-cap signature (it always
trades a lot, today's contract count is not a surge). **So the signal here is in the
directional/premium skew and the elevated IV, not in a volume spike.** Critically, INTC
is not alone: the entire single-name semiconductor complex is under distribution today
(MU #2, SNDK #4, INTC #5, TSM #7 on net-bearish), even as the SMH ETF shows bullish
premium — a dispersion/hedging divergence phase-6 must resolve. As-of spot anchored at
**$128.67** (dark-pool avg_price) — INTC has clearly re-rated far above its historical
$20–40 range. **This phase sets context only; it asserts no directional bias.**

## Universe ranking (market-wide, as-of 2026-06-26)

| Metric | INTC standing | Source |
|--------|---------------|--------|
| Total option premium | **99.8th pctile** ($566.1M) of 4,589 names | §C DUCKDB |
| Net-directional premium | **0.1th pctile** (−$50.4M); **#5 most-bearish name** | §C DUCKDB + `screener bullish-bearish --direction bearish` |
| Net **bullish** premium | **outside top-50** | `screener bullish-bearish --direction bullish` |
| IV rank | **97.0th pctile** universe (own iv_rank 94.1) | §C DUCKDB + `insights deep-dive` |
| Volume-vs-average (option vol vs 30d) | **outside top-50** (NOT a volume surge) | `screener volume-vs-average` |

**Net-bullish leaders today** (set ETFs aside): SPXW (+$119.8M), **SMH (+$78.0M)**,
IGV (+$76.1M), TSLA (+$70.3M), LULU (+$68.0M), LLY (+$37.5M). INTC absent.
**Net-bearish leaders today:** SPX (−$1,713M), **MU (−$408.7M)**, SPY (−$95.5M),
**SNDK (−$61.6M)**, **INTC (−$50.9M)**, GLD (−$49.6M), **TSM (−$47.9M)**, SOXL (−$42.3M).

## Sector read

**Semiconductors lead the BEARISH tape today.** Four of the seven most net-bearish
single names are semis (MU, SNDK, INTC, TSM), plus the 3× semis bull ETF SOXL showing
net-bearish flow (i.e. SOXL puts / unwinds). This is a sector-wide distribution read,
not an INTC-idiosyncratic one. **Divergence flag:** the broad semis ETF **SMH is the
#2 net-bullish name** (+$78.0M) — index-level call demand against single-name selling.
That pattern (buy the basket, sell the components) often reads as hedging or dispersion
positioning rather than clean directional conviction; **phase-6 must resolve whether
semis are in genuine rotation-out or merely being basket-hedged.** Separately, the IV
backdrop is hot across the complex: 12 Technology names sit at IV-rank 100 (AMAT, ADI,
TXN, TER, …) — a high-vol regime, with INTC's 94.1 elevated but mid-pack in that cohort.

## Self-history (INTC vs its own 54 available sessions)

| Self-percentile (ascending) | Value | Read |
|---|---|---|
| `self_pctile_net_dir` | **7.5** | Among INTC's **most bearish** net-direction days |
| `self_pctile_total` | 73.6 | Premium elevated for the name, not a record |
| `self_pctile_iv_rank` | 79.2 | IV elevated vs own recent history |
| `sessions_in_window` | **54** | True N (note the 2026-03-27→04-27 gap — not contiguous) |

The premium being only 73.6th self-pctile while net-direction is 7.5th confirms the
read: this is not "more flow than usual," it is **directionally more bearish than
usual** at a roughly normal-for-INTC activity level.

## Anchor datapoints carried forward

- **As-of spot ≈ $128.67** (dark-pool `avg_price`, `insights deep-dive .uw_dark_pool`).
  Dark pool today: $2,805M premium / 21.8M shares / 11,302 trades — heavy DP activity
  (detail deferred to phase-2).
- **Top OI builds (carry to phase-3):** PUT 130 Jul-17 (+11,442 OI, 21 DTE, avg $11.05)
  and PUT 135 Jul-17 (+2,941) — net put accumulation just above spot; the rest is 0DTE
  churn (C130/C140/P120 all dte=0). `insights deep-dive .uw_top_oi_changes`.
- **IV/implied-move tension (flag for phase-4):** `iv_rank=94.1`, `iv30d=0.923` (≈92%
  annualized) but `implied_move_perc=0.0065` (0.65%) and `implied_move=0.83` — the
  near-dated implied move looks far too small for a 92% IV30d. Phase-4 must reconcile
  (likely the implied_move field is a 1-day move while iv30d is annualized, or a
  scaling artifact). Do NOT propagate 0.65% as a multi-day expected move unchecked.
- **Next earnings:** 2026-07-23 (`.uw_screener.next_earnings_date`) — ~4 weeks out;
  cross-check in phase-7b (UW earnings dates can be stale).

## Source

CLI (`uw screener` ×4 + `uw insights deep-dive`) **+ DuckDB escape hatch §C** (exact
universe + self-history percentiles; local screener parquet for 2026-06-26 present).
"Outside top-50" recorded for net-bullish, volume-vs-average, and IV-rank-high
(the last because 50+ names are pegged at IV-rank 100).

## Verdict for downstream

```
universe_pctile_total_prem:  99.8                 # [CTX:universe_pctile DUCKDB]
universe_rank_net_dir:       #5 most-bearish (0.1 pctile); outside top-50 bullish
sector_leadership:           SEMICONDUCTORS leading the BEARISH tape (single names
                             MU/SNDK/INTC/TSM distributed); SMH ETF bullish = divergence
iv_rank:                     94.1                 # universe 97th pctile
implied_move_pct:            0.65%                # FLAG: reconcile vs iv30d 92% in phase-4
self_pctile_net_dir:         7.5                  # [CTX:self_pctile DUCKDB] — bearish extreme
unusual_verdict:             GENUINELY_UNUSUAL    # bearish-skewed; volume-vs-avg NOT elevated
```

**Interpretation note for phases 1–2:** the BUSY_NAME_NORMAL_DAY confluence cap is
*not* triggered (universe net-dir rank is extreme #5, self net-dir pctile is an extreme
7.5 — neither is "mid-pack"). But because the unusualness is in **direction/premium/IV,
not volume**, treat the bearish read as the high-confidence axis and avoid reading the
raw contract count as an independent surge signal.
