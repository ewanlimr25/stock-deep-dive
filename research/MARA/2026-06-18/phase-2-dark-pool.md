# Phase 2 — Dark Pool & Block Prints

**Ticker:** MARA
**As-of date:** 2026-06-18
**Generated:** 2026-06-19
**Upstream phases cited:** phase-0-intake.md (`Shs Float` 372.36M), phase-0.5-context.md, phase-1-flow.md

## Summary

Dark-pool tape is **mild net accumulation** and — importantly — it **reconciles
phase-1's call selling into a buy-write, not a bearish short.** Full-day MARA dark
pool was **$106.5M / ~7.56M shares** (block-stratified), dollar-weighted **~57%
buy**: a single **1,245,887-share mega block @ $14.22 ($17.7M, classified 100% buy)**
anchors the day, the large tier (the bulk, $70.0M / 531 trades) is mildly buy-leaning
(buy_ratio 0.528), partly offset by block-tier *selling* (buy_ratio 0.312). Institutions
**buying shares at $14.22 while phase-1 shows the $14.5C being written against them =
classic covered overwrite / buy-write** — neutral-income, capped upside, *not* a
distribution. Two de-rates: MARA is **outside the top-30 DP names** today (modest
scale), and the conviction prints are **closing-cross / after-hours** (possible MOC /
index mechanics, not pure intraday intent).

## Key signals

- **1.25M-share mega block @ $14.22 = $17.7M, buy_ratio 1.0** (`mega.buy_ratio`),
  +$0.02 vs mid — single largest print, ~0.33% of float `[DP:block-stratified]`.
- Large tier (the bulk): **$70.0M, buy_ratio 0.528** (buy 2.64M / sell 2.35M sh) —
  mild accumulation `[DP:block-stratified]`.
- Block tier: **buy_ratio 0.312 (sell_ratio 0.688)**, $18.7M — *distribution* here,
  the one offsetting tier `[DP:block-stratified]`.
- Heavy 5-day institutional shelf at **$14.22** ($39.3M / 2.77M sh / 29 trades) —
  primary support/reference `[DP:price-levels]`.
- MARA **outside top-30 DP names** (SPY $33B, MRVL $24B, MU $21B lead) — accumulation
  is genuine but small vs the universe `[DP:ticker-summary]`.

## Detailed findings

### Largest blocks (`dark-pool largest`, top-25 = $44.1M / 3.11M sh)

| Time (UTC) | Price | Size | Premium | vs mid | % float |
|-----------|-------|------|---------|--------|---------|
| 21:48:02 | $14.22 | **1,245,887** | **$17.72M** | +0.02 | **0.335%** |
| 20:00:37 | $14.22 | 316,708 | $4.50M | −0.015 | 0.085% |
| 20:53:36 | $14.22 | 199,933 | $2.84M | +0.02 | 0.054% |
| 20:00:35 | $14.22 | 198,100 | $2.82M | −0.015 | 0.053% |
| 20:00:05 | $14.22 | 127,900 | $1.82M | −0.005 | 0.034% |
| 20:16:20 | $14.22 | 121,960 | $1.73M | +0.01 | 0.033% |
| 14:13:06 | $13.83 | 92,600 | $1.28M | −0.005 | 0.025% |

Most size prints **at $14.22** clustered around **20:00 UTC (4:00pm ET close) and the
21:48 after-hours cross** → closing-auction / after-hours concentration. A few clean
intraday prints lower ($13.83, $14.00–$14.03 mid-session) show real daytime two-way.

### Tier breakdown (`block-stratified`, single-day 2026-06-18, $106.5M total)

| Tier | buy_ratio | derived sell_ratio | buy / sell vol | Premium | Trades | Read |
|------|-----------|--------------------|----------------|---------|--------|------|
| **mega** | **1.000** | 0.000 | 1,245,887 / 0 | $17.72M | 1 | the one big buy block |
| **large** | **0.528** | 0.472 | 2,635,923 / 2,352,818 | $70.01M | 531 | mild accumulation (the bulk) |
| **block** | **0.312** | 0.688 | 411,422 / 908,888 | $18.74M | 9 | *distribution* (offsetting) |
| retail | — | — | 0 / 0 | $0 | 0 | empty |

Dollar-weighted buy fraction ≈ (17.72·1.0 + 70.01·0.528 + 18.74·0.312) / 106.47 ≈
**0.569 → ~57% buy = mild net accumulation.** Per the rubric, large-tier 0.528 is
only *suggestive* (0.55–0.7 band not even reached); the mega 1.0 is high-confidence
but a single after-hours print. Honest read: **balanced-to-mild-buy**, not strong.

### Price levels (`price-levels --days 5`, dates 06-12→06-18 — note 5-day window)

| Level | 5-day premium | Shares | Role vs spot $14.22 |
|-------|---------------|--------|---------------------|
| **$14.22** | **$39.35M** | 2,767,209 | **primary shelf = spot/support** |
| $14.00 / $14.08 / $13.99 | $11.33M / $10.91M / $6.94M (~$29M) | — | **support band below** |
| $14.42 / $14.49 | $15.95M / $6.61M | — | minor supply just above |
| **$14.85–$14.93** (7 prints) | ~$70M combined | — | **heavy zone above = resistance / prior accumulation** |

Price has rolled down from the $14.85–$14.93 shelf (last 5d) to the $14.22 shelf —
the upper band is now overhead supply. The **$14.5 short-call strike (phase-1) sits
between the $14.22 spot shelf and the $14.85+ DP resistance** → consistent with a
"capped near-term" / pin-below-$14.5 thesis.

### Extended-hours activity

15 ext-hours prints; the **1.25M block (21:48 UTC / 5:48pm ET)** and the cluster at
20:00 UTC (4pm ET close) dominate. This concentration in the **close + after-hours**
means a large share of the "accumulation" could be **MOC / index-rebalance / ETF
cross mechanics** rather than directional intraday intent — **de-rate conviction**
and flag for phase-6 to check for a 6/18 index event or overnight MARA news.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|------------------|--------------------------|-----------|
| `dark-pool largest --symbol MARA --top-n 25 --sort-by premium --date 2026-06-18` | 1.25M @ $14.22 $17.7M ← `.results[0]`; top-25 $44.1M | 25 |
| `dark-pool block-stratified --symbol MARA --min-tier large --date 2026-06-18` | mega buy_ratio 1.0 / large 0.528 / block 0.312 ← `.results[]\|select(.ticker=="MARA").<tier>.buy_ratio` | 1 |
| `dark-pool price-levels --symbol MARA --days 5 --date 2026-06-18` | $14.22 $39.35M cluster ← `.results[]`; dates 06-12→06-18 | 15 |
| `dark-pool extended-hours --symbol MARA --top-n 15 --date 2026-06-18` | 1.25M @ 21:48 UTC ← `.results[0]` | 15 |
| `dark-pool ticker-summary --top-n 30 --date 2026-06-18` | MARA outside top-30 ← `[.results[].ticker]\|index` | 30 |

## Tool errors

(none — all five reads returned valid JSON. `ticker-summary` "outside top-30" is
information, not an error.)

## Verdict for downstream phases

- **Net institutional bias:** **mild ACCUMULATION / balanced-buy** (~57% dollar-
  weighted buy). Reconciles phase-1 → the call-selling is a **buy-write (covered
  overwrite)**, neutral-income, *not* a bearish naked short.
- **Conviction:** **2.5/5** — buy lean is real but the large tier is only 0.528
  (sub-threshold), the conviction print is a single after-hours cross, and MARA is
  outside the top-30 DP names (modest scale, busy-name normal day per `[CTX:]`).
- **Largest block as % of float:** 1.25M sh = **0.335% of the 372.36M float** in one
  print (full-day DP ≈ 2.0% of float). Meaningful but not float-dominating —
  appropriate for a 372M-float name, not a conviction squeeze. `[DP:block_pct_float fz]`
- **Three S/R levels for phase-9:**
  1. **$14.22** — primary institutional shelf / pivot (huge $39M, 2.77M-sh cluster = spot).
  2. **~$14.00** ($13.99–$14.08 band, ~$29M) — first support below; thesis-support floor.
  3. **$14.85–$14.93** (~$70M 5-day band) — overhead supply / resistance; caps upside,
     consistent with the $14.5 short-call and the "capped" flow read.
- **Open questions:**
  - Is the 1.25M after-hours mega block **directional** or **index/ETF-rebalance**
    (5:48pm ET, exactly at close $14.22)? → phase-6 overnight-news / index check.
  - Does the $14.85–$14.93 shelf represent **trapped longs** (resistance) or a
    reload zone? Phase-3 OI walls / phase-4 max-pain should corroborate the $14.5 cap.
