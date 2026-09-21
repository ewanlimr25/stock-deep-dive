# Phase 2 — Dark Pool & Block Prints

**Ticker:** CMPS
**As-of date:** 2026-06-18
**Generated:** 2026-06-20
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md, phase-1-flow.md

## Summary

Dark pool is **mixed, leaning mild distribution** — and notably does **not** confirm
aggressive selling under the bearish options skew. Total off-exchange premium was
$5.10M / 416,838 shares (**only 0.32% of the 128.74M float** — modest for this name).
The single biggest print was a **clean buy** (100,000 sh @ $12.10 = $1.21M, block
tier buy_ratio 1.0, lifted the ask), but the dominant **large tier** ($3.89M across
12 trades — most of the day's premium) is **net selling** (buy_ratio 0.398 →
sell_ratio 0.60). So the institution buying downside LEAP puts in phase-1 is *not*
sitting on top of one-way distribution; the common tape is two-sided with a sell
lean. The heaviest 5-day price cluster is **$12.10 ($3.025M)**, right at spot
($12.03) — the key reference level.

## Key signals

- Total DP $5.10M / 416,838 sh = **0.32% of float** — modest, not float-moving
  [DP:largest, DP:block_pct_float fz]
- Largest print a **buy**: 100K @ $12.10, $1.21M, block-tier buy_ratio **1.0** (lift)
  [DP:block_stratified]
- But **large tier net sell**: buy_ratio **0.398** (sell 0.60), $3.89M / 12 trades —
  the bulk of volume leans distribution [DP:block_stratified]
- Dominant 5-day price cluster **$12.10 = $3.025M**, magnet at spot; support shelf
  $11.84–11.90, lower level $11.54 [DP:price_levels]
- One extended-hours print: 50,102 @ $12.53 ($627,778) post-close (16:01 ET),
  above-mid buy [DP:extended_hours]
- CMPS **outside DP top-30** today — small relative to the tape [DP:ticker_summary]

## Detailed findings

### Largest blocks (`[DP:largest]`, spot $12.03; float 128.74M)

| Time (ET) | Price | Size | Premium | NBBO read | % float |
|-----------|-------|------|---------|-----------|---------|
| 10:42 | $12.10 | 100,000 | $1,210,000 | **LIFT / buy** (px=ask) | 0.078% |
| 16:01 | $12.53 | 50,102 | $627,778 | above mid (post-close) | 0.039% |
| 09:52 | $12.20 | 50,000 | $610,000 | below mid | 0.039% |
| 10:14 | $12.10 | 50,000 | $605,000 | at mid | 0.039% |
| 10:33 | $12.10 | 50,000 | $605,000 | LIFT / buy | 0.039% |
| 10:34 | $12.10 | 50,000 | $605,000 | below mid | 0.039% |
| 15:53 | $12.50 | 11,798 | $147,475 | HIT / sell | 0.009% |
| 15:53 | $12.50 | 11,798 | $147,474 | HIT / sell | 0.009% |

The 50K blocks at $12.10 cluster **10:14–10:34 ET — the same 30-min window the P10
LEAP puts were bought** (phase-1.md §Largest prints, 10:04–10:33 ET). Temporal
overlap supports a **collar/protective** read (someone long the common buying
downside) rather than pure directional distribution.

### Tier breakdown (`[DP:block_stratified]`)

| Tier | buy_ratio | sell_ratio | buy_vol | sell_vol | premium | trades |
|------|-----------|-----------|---------|----------|---------|--------|
| block | **1.00** | 0.00 | 100,000 | 0 | $1,210,000 | 1 |
| large | **0.398** | **0.602** | 126,142 | 190,696 | $3,885,278 | 12 |
| mega | — | — | 0 | 0 | $0 | 0 |
| retail | — | — | 0 | 0 | $0 | 0 |

`total_premium_all_tiers` = $5,095,278. The **large tier carries 76% of premium and
is 60% sell** — the net institutional lean is mildly distributive, but it sits in the
0.55–0.70 "suggestive only" band, muddied by the lone 100K block buy. No mega tier.

### Price levels (5-day clusters, `[DP:price_levels]`)

| Price | 5-day premium | Note |
|-------|---------------|------|
| **$12.10** | **$3,025,000** | dominant cluster, ≈ spot $12.03 — key reference |
| $12.20 | $867,493 | resistance shelf |
| $12.53 | $728,018 | upper (post-close print level) |
| $12.15 | $719,632 | resistance shelf |
| $11.54 | $688,938 | **lower support** |
| $11.84–11.90 | ~$776,000 combined | **near support shelf** |

(`--days 5` anchors to latest available date = 2026-06-18, contiguous with phase-0's
date list — no gap distortion.)

### Extended-hours activity

One print: 50,102 @ $12.53 = $627,778 at 16:01 ET (post-close), above mid → a
buy-ish facilitation/closing print. No pre-market activity. Cross-ref phase-6 for
any overnight news; absent a catalyst, reads as a closing cross, not directional.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|------------------|--------------------------|-----------|
| `uw dark-pool largest --symbol CMPS --sort-by premium` | top block 100K@$12.10=$1.21M ← `.results\|sort_by(-.premium)[0]`; total $5.10M / 416,838 sh ← `[.results[].premium\|size]\|add` | 13 |
| `uw dark-pool block-stratified --min-tier large` | large buy_ratio=0.398, sell=0.602 ← `.results[0].large.buy_ratio`; block buy_ratio=1.0 ← `.results[0].block.buy_ratio` | 1 |
| `uw dark-pool price-levels --days 5` | top cluster $12.10=$3.025M ← `.results\|sort_by(-.total_premium)[0]` | 15 |
| `uw dark-pool extended-hours` | 1 print 50,102@$12.53=$627,778 ← `.results[0]` | 1 |
| `uw dark-pool ticker-summary --top-n 30` | CMPS outside top-30 ← `select(.ticker=="CMPS")` empty | — |

## Tool errors

<none — all green>

## DATA NOTE / CORRECTION

- First-pass price-vs-mid sum read "roughly balanced" ($2.67M buy-ish vs $2.33M
  sell-ish). The authoritative **block-stratified** NBBO classification refines this:
  large tier (76% of premium) is **60% sell**; only the single 100K block-tier print
  is a clean buy. Verdict uses the block-stratified read (mild distribution), not the
  cruder price-vs-mid split.

## Verdict for downstream phases

- **Accumulation / Distribution / Mixed:** **MIXED — mild distribution.** Large tier
  60% sell, but the single largest print was a buy → not one-way selling.
- **Conviction:** **2 / 5** — total DP is only 0.32% of float, signals conflict
  (block buy vs large-tier sell), and no mega-tier participation. Low-confidence read.
- **Largest block as % of float:** 100K block = **0.078% of float** (total DP 0.32%).
  *Not* meaningful size for a 128.74M-float name — de-rate any DP-driven conviction.
  [DP:block_pct_float fz]
- **Three S/R levels for phase-9:**
  1. **$12.10** — dominant cluster / magnet ≈ spot (entry & pin reference).
  2. **$11.84–11.90** — near support shelf (first stop reference below).
  3. **$11.54** — lower support (deeper stop / where P10 puts gain).
- **Open questions:** Is the put buying a **collar** (common bought 10:14–10:34 ET
  alongside the puts) rather than a directional bear? Does phase-3 OI show the P10
  strike actually building? Any catalyst behind the post-close $12.53 buy (phase-6/7c)?
