# Phase 2 — Dark Pool & Block Prints

**Ticker:** INTC
**As-of date:** 2026-06-15
**Generated:** 2026-06-16T01:24:55Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md, phase-1-flow.md

## Summary

Dark pool **confirms phase-1's mildly-bullish thread but does not amplify it** —
the answer to phase-1's open question ("is dark pool confirming this premium, or is
the underlying being distributed?") is *accumulation-leaning, suggestive not
decisive*. The mega tier (≥$10M prints) runs **buy_ratio 0.583** (derived sell_ratio
0.417) — above the 0.55 accumulation line but inside the suggestive band, not
high-confidence [DP:block_stratified]. It is driven by a single **$500.0M block at
the 5:03pm-ET print, $127.86, +$1.99 above the NBBO mid** (buyer paying up)
[DP:largest], while large/block tiers are near-balanced (0.547 / 0.525) and the
pre-market saw ~$250M print *below* mid at $124.57 (sell-lean). INTC is **#10 in
the dark-pool universe today ($4.05B total)** — a top-10 name but behind MU ($14.6B)
and NVDA ($9.0B), echoing phase-0.5's "semis lead, INTC lags" [DP:ticker_summary].
Net: **accumulation-leaning, conviction 3** — real institutional buying underneath
the call tape, but modest as a fraction of INTC's 4.25B float.

## Key signals

- **Mega-tier buy_ratio 0.583** (buy 5.71M sh vs sell 4.08M sh, $1.24B, 16 trades) —
  biggest prints lean buy; derived sell_ratio 0.417 [DP:block_stratified].
- **$500.0M single block @ $127.86, +$1.99 above mid, 5:03pm ET** — 3,910,527 sh;
  the day's accumulation signature [DP:largest].
- **Ascending 5-day level stack:** $116.96 ($800M) → $124.57 ($852M) → **$127.86
  ($1.03B, largest cluster, = spot)** — institutions building UP into the rally
  [DP:price_levels].
- **Pre-market sell-lean:** ~$250M printed at $124.57, −$3.9 to −$4.2 below mid
  (8:32–9:04am ET) — the one distribution-flavored window [DP:largest][DP:extended_hours].
- **INTC #10 in dark-pool universe ($4.05B, 31.6M sh, 13,288 trades)** — top-10 but
  trailing MU/NVDA; large-tier 0.547 / block-tier 0.525 ≈ balanced [DP:ticker_summary].

## Detailed findings

### Largest blocks (NBBO context + % of float)

Float = 4.25B (phase-0). `[DP:block_pct_float fz]`

| Time (ET) | Price | Size (sh) | Premium | vs mid | % float | Read |
|-----------|-------|-----------|---------|--------|---------|------|
| 17:03 (AH) | 127.86 | 3,910,527 | **$500.0M** | **+$1.99** | 0.092% | buyer paying up — accumulation |
| 16:00 (close) | 127.86 | 939,667 | $120.1M | +0.005 | 0.022% | closing cross (at mid) |
| 08:32 (pre) | 124.57 | 737,512 | $91.9M | −$3.92 | 0.017% | below mid — sell-lean |
| 08:32 (pre) | 124.57 | 483,691 | $60.3M | −$3.92 | 0.011% | below mid — sell-lean |
| 16:00 (close) | 127.86 | 467,338 | $59.8M | +0.01 | 0.011% | closing cross |
| 09:04 (pre) | 124.57 | 401,379 | $50.0M | −$4.19 | 0.009% | below mid — sell-lean |

The **buy-side prints concentrate at the close/after-hours at $127.86** (the $500M
block +$1.99 above mid is the standout); the **sell-lean prints are pre-market at
$124.57**. Day nets to mega buy_ratio 0.583 because the closing/AH buy block
dominates. Even so, the $500M block is only **0.092% of the 4.25B float** — large in
dollars, structurally small for this name.

### Tier breakdown (buy/sell ratio per tier) — `[DP:block_stratified]`

| Tier (boundary) | buy_ratio | derived sell_ratio | premium | trades |
|-----------------|-----------|--------------------|---------|--------|
| **mega** (≥$10M) | **0.583** | 0.417 | $1,242.9M | 16 |
| large (≥$100k) | 0.547 | 0.453 | $2,511.7M | 13,117 |
| block (≥$1M) | 0.525 | 0.475 | $296.4M | 155 |

Accumulation concentrated in the *mega* tier; the broad large tier (the bulk of
$ volume) is only marginally buy-tilted. Confidence: **suggestive (0.55–0.70 band),
not high-confidence (>0.70)**.

### Price levels (5-day clusters, 2026-06-09 → 06-15)

| Level | 5d premium | shares | flag |
|-------|-----------|--------|------|
| **$127.86** | $1,026.5M | 8.03M | = spot; largest shelf / battleground (within 1%) |
| **$124.57** | $851.9M | 6.84M | support, −2.6% |
| **$116.96** | $799.6M | 6.84M | support, −8.5% |
| $107.92 | $254.7M | 2.36M | deeper support −15.6% |
| $107.04 | $108.9M | 1.02M | deeper support −16.3% |

The **ascending shelf stack ($107 → $117 → $124.57 → $127.86)** shows institutions
accumulating *into* a rising tape — constructive, and it tells phase-5 the 5-day
trend is strongly up. Spot sits on the heaviest shelf ($127.86).

### Extended-hours activity

The two largest prints of the day are extended-hours: **$500.0M @ 17:03 ET (AH,
above mid)** and **$120.1M @ 16:00 (closing cross)**, plus the pre-market $124.57
sell-lean cluster. The AH $500M buy block is the single most important print —
attribute against phase-6 for any overnight semi/INTC headline; if none, it reads
as a genuine institutional accumulation cross rather than news reaction.

## Tool calls (audit trail)

| Command (`--symbol INTC --date 2026-06-15`) | Key value(s) ← `jq` path | Rows |
|------|------|------|
| `dark-pool block-stratified --top-n 30 --min-tier large` | mega.buy_ratio 0.583 ← `.results[0].mega.buy_ratio`; sell:=1−0.583 | 1 |
| `dark-pool largest --top-n 25 --sort-by premium` | $500M @127.86 +1.99 mid ← `.results[0]` | 25 |
| `dark-pool price-levels --top-n 15 --days 5` | $127.86 $1.03B top shelf ← `.results` sort -prem | 15 |
| `dark-pool extended-hours --top-n 15` | AH $500M @17:03 ← `.results[0]` | 15 |
| `dark-pool ticker-summary --top-n 30` | INTC rank #10, $4.05B ← `index("INTC")` | 30 |

## Tool errors

None — all five reads returned valid JSON.

## DATA NOTE / CORRECTION

None. (`--days 5` window `dates_covered` = 2026-06-09→06-15, all June, clear of the
March/April local gap — cluster premiums are clean. All reads file-captured then
`jq`'d.)

## Verdict for downstream phases

- **Institutional bias:** **Accumulation-leaning** (mega buy_ratio 0.583 + $500M
  above-mid AH block), tempered by balanced large-tier and a pre-market sell-lean window.
- **Conviction:** **3/5** — suggestive band, not high-confidence; consistent with
  (not stronger than) phase-1. BUSY_NAME_NORMAL_DAY cap respected.
- **Largest block as % of float:** **0.092%** ($500M / 4.25B float) — meaningful in
  dollars, structurally modest for a 4.25B-float name; do not over-weight raw size.
- **Three S/R levels for phase-9 (entry/stop reference):**
  1. **$127.86** — spot & heaviest 5-day shelf ($1.03B); the battleground / pivot.
  2. **$124.57** — first support (−2.6%, $852M shelf); also the pre-market print level.
  3. **$116.96** — major support (−8.5%, $800M shelf); logical swing-stop reference.
- **Open questions:**
  - Was the $500M AH block news-driven or a clean accumulation cross? → **phase-6** (overnight catalyst check).
  - Does dealer OI positioning (walls/GEX) corroborate $127.86 as a pin/pivot and define the upside path? → **phases 3–4**.
  - Is the 5-day ascending accumulation a fresh institutional build or late-cycle chase? → **phase-5** trend + **phase-7b** valuation.
