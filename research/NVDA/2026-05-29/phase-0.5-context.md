# Phase 0.5 — Cross-Sectional & Self-History Context (CTX)

**Ticker:** NVDA
**As-of date:** 2026-05-29
**Generated:** 2026-05-30T11:55Z
**Upstream phases cited:** phase-0-intake.md

## Summary

NVDA's *absolute* footprint is, as always, at the very top of the universe
(total option premium 99.91st pctile, net-directional premium 99.74th, stock
volume 99.93rd of 5,782 names). But the cross-sectional and self-history reads
both say **this is a busy mega-cap having a normal-to-quiet day, not a genuinely
unusual-flow day.** Today's net-directional premium is **+$17.3M** — mildly
bullish, but only the **60th percentile of NVDA's own last 35 sessions** and it
ranks **15th among single names** (18th incl. indices). Critically, the *context
is a downtrend*: NVDA has fallen **−10.4% over 10 sessions** (235.74 → 211.14)
and the prior week of flow was heavily *negative* (May 21 −$190M, May 22 −$97M,
May 26 −$100M net-dir). Today's small positive print reads as a **bounce-day
blip inside a corrective leg**, not the start of fresh accumulation. Technology
overwhelmingly leads the tape (+$533M net-dir vs every other sector flat/red),
so NVDA is a mid-pack participant in a strongly-bid sector. IV rank 40.65 is
**middling** (not cheap, not rich). **Verdict: BUSY_NAME_NORMAL_DAY.**

## Universe ranking

- [CTX:] NVDA universe percentiles (n=5,782; 4,455 optionable) [DUCKDB]:
  total premium **99.91**, net-directional premium **99.74**, stock volume
  **99.93**, IV rank **60.87**, volume-vs-avg ratio **64.42**.
- [CTX:] **Net-directional premium rank: 15th among single names** / 18th incl.
  indices (`uw screener bullish-bearish`). Leaders: MSFT +$136M, DELL +$122M,
  ORCL +$60M, PLTR +$57M, NOW +$46M, CRWD +$43M, AVGO +$26M, ARM +$23M,
  AMD +$23M — **all Technology**; NVDA +$17.3M sits behind the whole semis/
  software complex.
- [CTX:] NVDA exact flow today: net-dir **+$17.35M**, net_call_premium **+$16.0M**,
  **put/call ratio 0.424** (call-skewed, structural for NVDA), vol_ratio **0.921**
  (below its 30-day average volume — a quiet down day).

## Sector read

- [CTX:] **Technology leads decisively**: +$533.3M net-directional premium across
  557 single names — the *only* sector meaningfully bid. Every other sector is
  flat-to-negative (Comm Svcs −$104M, Cons Cyclical −$50M, Materials −$20M).
- Read for phase-6: the bid is concentrated in Tech/semis-software, but **NVDA is
  not leading its own sector** — it ranks ~15th within the very group that's
  leading. Name strong-ish, sector strong, but name lagging the sector's leaders.

## Self-history (parquet present — 35 sessions) [DUCKDB]

| date | close | net-dir $M | net-call $M | P/C | IV rank |
|------|-------|-----------|------------|-----|---------|
| 05-21 | 219.51 | **−189.7** | −213.8 | 0.432 | 34.2 |
| 05-22 | 215.33 | −97.0 | −94.4 | 0.470 | 27.3 |
| 05-26 | 214.66 | −100.2 | −79.8 | 0.420 | 34.2 |
| 05-27 | 212.60 | −66.3 | −55.9 | 0.396 | 30.5 |
| 05-28 | 214.25 | +8.6 | −2.4 | 0.342 | 31.3 |
| **05-29** | **211.14** | **+17.3** | **+16.0** | **0.424** | **40.6** |

- [CTX:] **self_pctile_net_dir ≈ 60** (today's +$17.3M vs own 35-session dist).
- [CTX:] Price trend: **−10.4% over 10 sessions** (235.74 → 211.14); 20-session
  range 167.52 – 235.74. NVDA is **mid-correction**, today closing −1.45% on the
  day despite the mildly positive net flow (flow/price divergence — bears still
  in control of price; small bid building in options).
- [CTX:] IV rank 40.6 = 45.7th self-percentile — middling vol, no panic, no
  complacency.

## Source

CLI (`uw screener bullish-bearish`, `uw options-flow unusual-volume`) + DuckDB
escape hatch (`lib/duckdb-cuts.md §C`) for exact universe + self-history
percentiles. All as-of 2026-05-29. No "outside top-N" gaps. Data gap
2026-03-28 → 04-26 limits the trailing window to 35 sessions.

## [CTX:] Context block (inherited verbatim by phases 1, 5, 9)

```
universe_pctile_total_prem:  99.91
universe_rank_net_dir:       15 (single names; 18 incl. indices)
sector_leadership:           Technology is LEADING the tape (+$533M); NVDA mid-pack within it
iv_rank:                     40.65
implied_move_pct:            0.45      # 1-day implied move ~$0.95 on 211.14
self_pctile_net_dir:         60
price_trend:                 DOWNTREND -10.4% over 10 sessions (235.74 -> 211.14); today -1.45%
unusual_verdict:             BUSY_NAME_NORMAL_DAY
```

**Calibration note for downstream phases:** This caps phases 1–2 confluence at
`+` (not `++`) per `rubrics/confluence-scoring.md`. Any "bullish flow" read must
be weighed against (a) the active downtrend, (b) the prior week of heavily
*negative* flow, and (c) NVDA lagging its own leading sector. A flow/price
**divergence** is the key tension: options turned mildly net-bullish over the
last two sessions while price kept falling. Phases 1–4 must decide whether that
is early accumulation into weakness or a dead-cat bounce being faded.

## Verdict for downstream phases

- **Bias from this phase:** neutral (context only — no directional vote)
- **Conviction:** n/a (context phase)
- **Three things later phases must remember:**
  1. NVDA is **mid-correction (−10.4%/10d)** and closed red today — price trend is down.
  2. Today's +$17.3M net-dir flow is **mild and only 60th self-pctile**; prior
     week was heavily negative — verdict **BUSY_NAME_NORMAL_DAY**, confluence capped at `+`.
  3. **Tech leads the tape (+$533M) but NVDA ranks ~15th within it** — sector tailwind exists, name is not the leader.
- **Open questions:** Is the 2-day positive flow turn genuine accumulation into
  the dip, or a fade-able bounce? (phases 1–4). Where is dealer gamma vs the
  211 spot and the recent 219–225 supply? (phase 4).

## Handoff to next phase

Phase 1 (flow): re-derive net premium and aggressor side strictly from as-of
2026-05-29 data; benchmark against NVDA's high baseline and the prior week's
*negative* flow, not absolute $. Resolve the flow/price divergence: are calls
being bought into the downtrend (accumulation) or is this short-dated noise?
Carry forward: downtrend context, IV rank 40.65 (middling), P/C 0.424.
