# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** SNOW · **As-of:** 2026-05-29 · **Generated:** 2026-05-29
**Upstream:** phase-0-intake.md (price $255.55 +6.84%, earnings 2026-05-27 beat,
short float 5.81%, post-earnings day)

## Summary

Unlike a busy-name-normal-day, SNOW's options tape on 2026-05-29 is **genuinely
unusual** — it's the post-earnings (T+2) blowout after a 5/27 beat. SNOW sits at
the **99.3rd universe percentile on total option premium** and **96.0th on
volume-vs-average** `[CTX:universe_pctile DUCKDB]`, and the **94.1st percentile
of its own 35-session history** for total premium. But the **direction is split**:
gross flow is hugely call-tilted (call premium **$232.6M** vs put **$28.3M**,
P/C 0.40), yet on the bull/bear classification SNOW is *net slightly bearish*
(bullish $113.8M vs bearish $118.2M) and shows up at **rank 38 on the net-bearish
premium board**, NOT on the bullish board — while the order-book net-directional
metric (net_call − net_put premium) ranks **98.8th**. That divergence — record
call buying alongside enough call-selling/hedging to tilt the bull/bear net
bearish — is the central question phases 1–4 must resolve: **is this post-earnings
continuation buying, or profit-taking / call-writing into the +6.84% rip?**
Sector is the strongest possible backdrop: software/AI mega-caps lead the entire
tape, and SNOW (earnings beat + "AI winner" narrative) is squarely in the leading
theme — name-strong-into-strong-sector.

## Universe ranking

- Net-bullish premium board (top-60 single names): SNOW **absent**.
- Net-bearish premium board: SNOW **present, rank 38** — net-flow (bull−bear
  premium) is *slightly negative* despite the huge call premium.
- Leaders (bullish board): NDX, MSFT, DELL, ORCL, PLTR, NOW, CRWD — a
  **software/AI-led tape**, SNOW's cohort.
- Exact universe percentiles `[CTX:universe_pctile DUCKDB]`: total premium
  **99.3**, net-directional (net_call−net_put) **98.8**, IV-rank **71.9**,
  vol-vs-avg **96.0**.

## Sector read

Software/AI is **leading and in favour** (MSFT/ORCL/NOW/CRWD/PLTR top of the
bullish board). SNOW just beat on AI-driven growth (phase-0 news: "Roars Back To
Life On AI Growth," HSBC upgrade, "Back In The AI Winner Camp") — so unlike a
laggard, SNOW is a **credible participant in the leading theme**. This is the
favourable cross-sectional configuration; hands phase-6 a sector-in-favour prior.

## Self-history

`[CTX:self_pctile DUCKDB]` over **35 available sessions** (non-contiguous —
2026-03-28→04-26 gap): net-directional premium **79.4th** percentile, total
premium **94.1st**. Read: a top-of-window activity day with *elevated but not
extreme* net direction — consistent with a big post-earnings day where buyers and
sellers are both very active.

## Source

`uw insights deep-dive` + `uw screener bullish-bearish` (both directions) + DuckDB
§C exact percentiles (universe + 35-session self-history). SNOW "absent from
bullish top-60 / present rank 38 bearish" recorded as information.

## Verdict for downstream

```
universe_pctile_total_prem:  99.3
universe_rank_net_dir:       absent from bullish top-60; rank 38 on bearish board (but net_call−net_put pctile 98.8)
sector_leadership:           Software/AI is LEADING today (in favour); SNOW a credible participant
iv_rank:                     51.5 (insights) / 71.9 universe-pctile
implied_move_pct:            0.55% (daily implied move, post-earnings IV crush)
self_pctile_net_dir:         79.4  (35-session window)
unusual_verdict:             GENUINELY_UNUSUAL
```

**Why GENUINELY_UNUSUAL (no confluence cap on phases 1–2):** activity clears the
bar decisively (99.3 universe / 94.1 self total premium, 96.0 vol-vs-avg) and the
context is a real catalyst (post-earnings beat). Self net-directional 79.4 is a
whisker under the 80 threshold, so the *magnitude* is unusual but the *direction*
is not yet clean — the bull/bear net being slightly bearish while call premium is
huge means phases 1–4 must adjudicate continuation-vs-fade. Downstream should size
on the genuine edge (it's in the data, not capped), but treat the **directional
sign as unresolved** until the flow/structure phases settle it.
