# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** SNOW
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T15:10:00Z
**Upstream phases cited:** phase-0-intake.md

## Summary

SNOW's option tape is **unusual in *size* but not in *direction*.** Total premium
$42.2M sits at the **98th universe percentile** and volume is at the **94th
percentile vs its own 30-day average** — top-decile activity. But that activity is
**earnings-vol inflation, not a directional bet**: net-directional premium is
−$0.9M, the **2.3rd percentile** of the universe (i.e. near the most net-bearish
names by the ask−bid premium measure), and only the **33rd percentile of SNOW's
own 31-session history**. The driver is unambiguous — **earnings 2026-05-27
postmarket, 3 trading days out** — which also explains IV rank 86.76 (96th universe
percentile). SNOW is **outside the top-50** on net bullish *and* net bearish
directional premium. Sector context is a mild tailwind: the software/application
cohort is bid today while semis are sold. **Net read: a busy, expensive,
event-driven name without a clean directional tilt — treat as an earnings setup,
and cap phases 1–2 directional confluence at `+` (not `++`).**

## Universe ranking (single names, ETFs set aside)

- **Net bullish premium:** SNOW is **outside top-50** (leaders: AAPL +$81.4M,
  TSLA +$52.6M, DELL +$32.7M, IBM +$32.6M, ADBE +$23.4M) [CTX:screener_bullish_bearish].
- **Net bearish premium:** SNOW is **outside top-50** (most-sold: MSTR −$120.7M,
  NVDA −$97.0M, SNDK −$48.1M, GOOGL −$35.8M, SMH −$33.0M) [CTX:screener_bullish_bearish].
- **Volume-vs-average:** SNOW outside top-50 on the *ratio* leaderboard (which is
  dominated by micro-names), yet its **own** vol/avg30 is 94.2nd percentile of the
  universe [CTX:universe_pctile_vol_vs_avg DUCKDB] — high absolute turnover, just
  not a freak multiple like the micro-caps.
- **IV rank:** outside top-50 (top-50 is saturated with IV-rank=100 names), but
  SNOW's 86.76 is the **96.3rd universe percentile** [CTX:universe_pctile_iv_rank DUCKDB].

## Sector read

Today's directional tape splits clean: **software/application bid, semiconductors
sold.** Software net-bullish: ADBE +$23.4M, IGV (software ETF) +$16.2M, NOW
+$13.0M, PANW +$12.7M, INTU +$7.9M, SNPS/CDNS/PCOR all positive
[CTX:screener_bullish_bearish]. Semis net-bearish: NVDA −$97.0M, SNDK −$48.1M,
SMH −$33.0M, AMD −$8.8M, AVGO −$7.5M, AMAT −$2.7M. SNOW is in the in-favour
software cohort — a mild cross-sectional tailwind for phase-6 to weigh — **but
SNOW is not itself participating in the software bid** (outside top-50, net-dir
bottom-decile). Data-infra peer MDB was net-bearish −$2.6M; the cohort bid is
broad-software, not data-platform-specific.

## Self-history (DuckDB §C — local parquet present)

Today vs SNOW's own ≤31-session distribution (gap-aware N=31; the 2026-03-28→04-26
hole means this is 31 *available* sessions, not a contiguous window):

| Metric | Self-percentile | Read |
|--------|-----------------|------|
| Net-directional premium | **33.3** | below its own median — *not* a directionally bullish day |
| Total premium | **66.7** | above its own median — busier than typical |
| IV rank | **56.7** | only mid-for-SNOW — this name routinely runs high IV; 86.76 is normal-ish for it |

`sessions_in_window: 31` [CTX:self_pctile DUCKDB]. The IV-rank self-percentile (57)
is the tell: SNOW's IV rank looks extreme cross-sectionally (96th universe pctile)
but is ordinary *for SNOW* — so IV rank alone is not the edge; the earnings binary is.

## Source

MCP (`screener_bullish_bearish` ×2, `screener_volume_vs_average`,
`screener_iv_rank`, `insights_deep_dive`) **+ DuckDB §C** (exact universe &
self-history percentiles; local screener parquet present for 2026-05-22). Universe
N=4,532 optionable names. "Outside top-50" recorded for net-dir (both directions),
vol-ratio leaderboard, and IV-rank leaderboard.

## Verdict for downstream

```
universe_pctile_total_prem:  98.0
universe_pctile_net_dir:     2.3          # near most net-BEARISH by ask-bid premium
universe_rank_net_dir:       outside top-50 (both bullish & bearish boards)
sector_leadership:           Software/application LEADING today (semis lagging) — SNOW in-favour cohort but not a leader itself
iv_rank:                     86.76        # 96.3 universe pctile / 56.7 self pctile
implied_move_pct:            0.40 (screener implied_move_perc)  # ⚠ does NOT capture the 5/27 earnings jump — derive true expected move from phase-4 term structure / ATM straddle
self_pctile_net_dir:         33.3         # below own median
self_pctile_total:           66.7
sessions_in_window:          31           # gap-aware
unusual_verdict:             BUSY_NAME_NORMAL_DAY  (size-unusual, direction-neutral; EARNINGS-DRIVEN — 2026-05-27 postmarket)
```

### Three things later phases must remember
1. **This is an earnings setup (5/27 postmarket, 3 trading days out).** Every later
   phase must frame structures/levels around that binary. IV is rich (96th universe
   pctile); long-premium structures pay a steep event premium.
2. **Direction is unconfirmed by size.** Net-dir premium is bottom-decile (2.3
   universe / 33 self) despite top-decile gross premium. Big call premium ($34.6M
   call vs $7.6M put) is gross/lotto, not net-directional. → **phases 1–2 confluence
   capped at `+`.** Do not read the dollar size as bullish conviction.
3. **The screener `implied_move_perc` (0.40%) is unusable for the earnings move** —
   it understates a binary event. Phase 4 must compute the real expected move from
   the ATM straddle / front-week IV; phase 9's expected-move (N4) uses that, not this.

### Open questions
- Is the gross call buying (185C/200C 5/29 OI builds noted in phase-0) directional
  conviction or premium-selling/lotto? → phase-1 aggressor split + phase-3 OI resolve.
- Where is dealer gamma pinning price into the event? → phase-4 GEX/gamma-flip.
- Does SNOW's fundamental trajectory justify chasing an up-move into print? → phase-7b.
