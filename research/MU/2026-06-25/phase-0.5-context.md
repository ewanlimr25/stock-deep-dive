# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** MU
**As-of date:** 2026-06-25
**Generated:** 2026-06-25
**Upstream phases cited:** phase-0-intake.md

## Summary

MU's flow today is **genuinely unusual on the directional/dollar axis**: it is the
**#1 single name in the entire optionable universe** on both total option premium
(100th pctile) and net-directional premium (100th pctile, +$279M net-bullish),
trailing only the SPX index itself. Versus its own history (N=53 available
sessions) today's net-bullish premium sits at the **98.1st percentile** — this is
one of MU's most bullish flow days on record. The one caveat: total option volume
is only **1.32× MU's 30-day average** (86.6th pctile universe-wide), so the
unusualness is driven by *directional conviction and dollars*, not by a raw volume
explosion — expected for a perpetually high-volume mega-cap. **Critically, the
IV-rank series (100→100→93→77 over 6-22→6-23→6-24→6-25) is a classic post-earnings
vol crush**, confirming MU reported ~June 23 and that `next_earnings_date
2026-09-22` is the *next* quarter (no imminent earnings binary). This is a
**post-earnings bullish-continuation** context, with flow having flipped from
−$145M net (6-23) to +$279M net (6-25).

## Universe ranking (today, 2026-06-25)

Net-bullish premium leaders (`screener bullish-bearish --direction bullish`):

| Rank | Ticker | net_flow (bull−bear premium) | Note |
|------|--------|------------------------------|------|
| 1 | SPX | +$696.6M | index (set aside) |
| **2** | **MU** | **+$279.0M** | **#1 single name** |
| 3 | SLV | +$126.7M | silver ETF |
| 4 | SNDK | +$95.2M | memory/storage peer |
| 5 | LULU | +$59.7M | consumer |
| 6 | RUT | +$54.5M | index |

- **MU net bearish premium:** outside top-60 (not being sold).
- **MU volume-vs-average:** outside top-60 on the CLI list (that list is dominated
  by micro-cap SPAC noise, e.g. RAM at 8847× — not meaningful for a mega-cap);
  exact `vol_x_today = 1.32` from DuckDB.
- Bearish-premium leaders for contrast: MSFT (−$179M), AAPL (−$150M), AMZN
  (−$87M), **INTC (−$78M)**, FXI, PLTR — megacap software + Intel being sold.

## Sector read

Today's tape splits **within** tech: **memory/storage semis are bid** (MU #1
single name, SNDK #4 on net-bullish premium) while **megacap software and Intel
are sold** (MSFT/AAPL/AMZN/INTC top the bearish list). So MU's specific
sub-sector (DRAM/HBM memory) is **leading**, even as broad large-cap software
lags. This is constructive rotation *into* MU's pocket — a head start for phase 6:
the bullish flow is corroborated by its closest peer (SNDK), not isolated, while
the funding source appears to be megacap software/Intel.

## Self-history (DuckDB §C, N=53 available sessions)

| Metric | Today's percentile vs MU's own history |
|--------|----------------------------------------|
| net-directional premium | **98.1** `[CTX:self_pctile DUCKDB]` |
| total premium | 98.1 |
| IV rank | 32.7 (today's IV is *low* for MU's recent range) |

Recent MU series (DuckDB):

| date | net_dir ($M) | tot_prem ($M) | P/C | iv_rank |
|------|-------------|---------------|-----|---------|
| 2026-06-25 | **+279.0** | **6935.3** | 1.026 | 77.1 |
| 2026-06-24 | +26.1 | 3795.3 | 1.040 | 93.0 |
| 2026-06-23 | −145.2 | 4136.1 | 1.013 | 100.0 |
| 2026-06-22 | +214.9 | 4972.5 | 0.930 | 100.0 |
| 2026-06-18 | +522.2 | 5623.8 | 1.124 | 94.2 |
| 2026-06-17 | +48.1 | 3119.6 | 0.920 | 95.9 |
| 2026-06-16 | −192.1 | 2979.7 | 0.944 | 96.9 |
| 2026-06-15 | +78.2 | 4705.3 | 0.921 | 100.0 |

Read: today's $6.94B total premium is the **highest in the window**; net-direction
swung sharply positive (+$279M) after the −$145M earnings-day (6-23) print. IV
rank collapsing 100→77 across the print = vol normalizing post-event.

## Source

CLI (`uw screener` bullish/bearish/vol-vs-avg/iv-rank, `uw insights deep-dive`)
**+ DuckDB §C** (exact universe + self-history percentiles; local parquet present
for 2026-06-25). N=53 self-history sessions span the 2026-03-28→04-24 gap — not a
contiguous calendar window. "Outside top-60" recorded for bearish & volume-ratio.

## Verdict for downstream

```
universe_pctile_total_prem:  100.0          # DuckDB; #1 of universe
universe_rank_net_dir:       1 (single names); 2 incl. SPX index; 100th pctile
sector_leadership:           SEMIS/MEMORY leading (MU #1, SNDK #4); megacap software lagging
iv_rank:                     77.07           # elevated absolute, but 32.7th pctile of MU's own range
implied_move_pct:            3.93%           # absolute implied_move 47.39 on ~$1,200 underlying
self_pctile_net_dir:         98.1            # DuckDB, N=53 sessions
unusual_verdict:             GENUINELY_UNUSUAL
```

**Verdict rationale:** GENUINELY_UNUSUAL on the directional/dollar axis — #1 single
name universe-wide on net-directional premium *and* 98th self-percentile. The
BUSY_NAME_NORMAL_DAY cap does **not** apply (rank is #1, not mid-pack; self_pctile
98, not <60). The single qualifier: volume-vs-average is a modest 1.32×, so phases
1–2 should read the signal as conviction/dollar-weighted, not a volume breakout.
**Context flag for all later phases:** this is a **post-earnings (≈June 23)
continuation** read with IV deflating — no imminent earnings binary; size off flow
+ structure, not an event.
