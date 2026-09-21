# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** PATH (UiPath Inc.)
**As-of date:** 2026-06-01
**Generated:** 2026-06-01T20:09:00-04:00
**Upstream phases cited:** phase-0-intake.md

## Summary

The CLI top-50 boards make PATH look quiet — it is **outside the top-50** on net
bullish premium, net bearish premium, volume-vs-average, and high-IV-rank, drowned
out by a semis-led mega-cap tape (NVDA +$182M, MU +$150M, SNDK +$149M). But the
exact percentiles flip that read: across the ~6k-name optionable universe PATH sits
at the **98th percentile on net-directional premium** and **96th on total premium**,
and versus its own 36-session history today is its **single most net-bullish day
(100th self-percentile)** with total premium near its own high (97th). The
unusualness is real and directional — it is simply *small in absolute dollars*
(~$13 small-cap), which is why the mega-cap board hides it. Net call premium
+$2.18M, call-heavy (P/C 0.26), on a name carrying a 31% short float. Verdict:
**GENUINELY_UNUSUAL (directional)** — but tradeability/size must respect the modest
absolute liquidity, and the spike is in *direction/premium*, not a broad 2× option-
volume explosion (CLI volume screen did not flag it).

## Universe ranking (2026-06-01)

| Metric | PATH standing | Leaders (single names) |
|--------|---------------|------------------------|
| Net bullish premium (abs $) | **outside top-50** (net +$2.18M tiny vs board) | NVDA +$182M, MU +$150M, SNDK +$149M, ADI +$82M, MSFT +$81M |
| Net bearish premium (abs $) | outside top-50 | SPX −$275M, TSLA −$107M, META −$99M, AAPL −$58M, TSM −$56M |
| Volume-vs-average (≥2×) | outside top-50 | RJET1, TLTI, BLFS, DFNL, ANY1 (micro/illiquid) |
| IV-rank (high cohort) | outside top-50 | — (PATH iv_rank 53.3 = mid-pack) |

**Exact percentiles (DuckDB §C, whole universe):**
- `pctile_total_prem` = **96.2** [CTX:universe_pctile DUCKDB]
- `pctile_net_dir` = **98.0** [CTX:universe_pctile DUCKDB]
- `pctile_iv_rank` = **65.0** [CTX:universe_pctile DUCKDB]
- `pctile_vol_vs_avg` = 91.5 — **disregard** (the §C `vol_x` divides option contracts
  by average *share* volume → 0.0049; not a valid option-volume-vs-average ratio).
  Authoritative read: CLI option-volume screen left PATH outside the ≥2× top-50.

## Sector read

Today's directional tape is **Technology-led, specifically semiconductors** — the
entire bullish top-10 is Tech (NVDA/MU/SNDK/ADI/MSFT/ORCL/IBM/DELL/MRVL). PATH is
Technology too, but **application/automation software**, not the semis cohort that
is actually leading. So PATH rides a broadly-favoured sector while sitting *adjacent
to*, not inside, the day's leadership cohort. The bearish board is index/mega-cap
hedging (SPX, SPY, QQQ, TSLA, META, AAPL) — broad-market caution, not a PATH-
specific or software-specific sell. Hands phase-6 a head start: macro tape = "buy
semis / hedge index," a mixed backdrop for a small-cap software name.

## Self-history (DuckDB §C — 36 available sessions, GAP-aware)

- `self_pctile_net_dir` = **100.0** [CTX:self_pctile DUCKDB] — today is the most
  net-bullish directional day for PATH in the entire local window.
- `self_pctile_total` = **97.1** [CTX:self_pctile DUCKDB] — total premium near its
  own 36-session high.
- `sessions_in_window` = **36** (NOT a contiguous 36 calendar days — spans the
  2026-03-27→04-27 gap; two blocks).

## Raw anchors (DuckDB)

- close **$13.10**; total option premium **$17.55M**; net-directional **+$2.18M**;
  call_volume 151,351 vs put_volume 39,188 (P/C 0.259); iv_rank 53.3.
- From `insights deep-dive`: call_premium $14.0M, put_premium $3.54M; bullish
  $8.63M − bearish $6.45M = **+$2.18M** (matches); iv30d 72.3%; **implied_move 6.32%**
  ($0.83); total_OI 715,245; **next earnings 2026-09-03** (no near-term event).

## Source

CLI top-50 boards + `insights deep-dive` (PATH absolute) **+ DuckDB §C** (exact
universe + self-history percentiles; local 2026-06-01 parquet present). "Outside
top-50" recorded on all four CLI metrics — informational, mega-cap dominance, not
an error. The DuckDB percentiles are the authoritative cross-sectional read here.

## Verdict for downstream — `[CTX:]` block

```
universe_pctile_total_prem:  96.2                       # DUCKDB
universe_rank_net_dir:       outside top-50 abs$; 98.0 universe pctile [DUCKDB]
sector_leadership:           Technology LEADING (semis-led); PATH = software, adjacent not lead
iv_rank:                     53.3
implied_move_pct:            6.32
self_pctile_net_dir:         100.0                       # DUCKDB
unusual_verdict:             GENUINELY_UNUSUAL (directional; small absolute $)
```

**Calibration notes for later phases:**
1. The bullish flow is genuinely unusual *for PATH* (100th self-pctile net-dir) —
   do NOT cap phases 1–2 confluence at `+` as BUSY_NAME_NORMAL_DAY would require.
   BUT the absolute size is small and option volume is only modestly elevated
   (not a 2× spike), so phase-9 sizing must respect low absolute liquidity.
2. The unusualness is **directional/premium**, concentrated in call premium — phase-1
   must resolve whether this is real directional conviction vs short-dated lottery /
   squeeze-chasing, given the 31% short float.
3. Sector is favoured-but-adjacent (Tech up, but semis lead, not software) — phase-6
   to judge whether software/PATH actually participates or is left behind.
