# Phase 2 — Dark Pool & Block Prints

**Ticker:** PATH
**As-of date:** 2026-07-13
**Generated:** 2026-07-13T20:20:00-04:00
**Upstream phases cited:** phase-0.5-context.md, phase-1-flow.md

## Summary

This is the anomaly of the whole workup. On **2026-07-09 afterhours** PATH printed
the **three largest darkpool blocks in its entire local history by ~15×** — a
**30.4M-share @ $11.80 = $358.7M** cross at 16:11 ET, a **19.4M @ $11.80 = $229.3M**
at 16:47 ET, and **4.8M @ $11.80 = $56.2M** at 16:00 ET. Block-stratified confirms
the mega tier was **100% buy (buy_ratio 1.0), 54.6M shares, $644.2M, zero sell**, and
the whole session lifted **$590M at/above ask vs just $3.6M sold**. Accumulation then
**continued into the as-of 07-13** (large tier buy_ratio 0.612, $337M) with price
holding/rising from $11.80 → ~$11.95–12.0. The $11.80 level is now a **$678.8M / 57.5M-share
institutional shelf**. This reads as **strong accumulation**, BUT the 54.6M mega block ≈
**~14% of float** printed at a flat $11.80 in seconds — the fingerprint of a *negotiated
block / secondary / index cross*, whose true nature (strategic buyer vs offering
placement vs Russell/ETF mechanics) **must be resolved by phase-6 news** before conviction is banked.

## Key signals

- **07-09 mega block: 30,399,031 sh @ $11.80 = $358.7M, printed at ask (lift/buy)** `[DP:largest]` — largest darkpool print in PATH's local history (15× the prior record).
- **Mega-tier buy_ratio = 1.000**, 3 prints, 54,595,203 buy shares, $644.2M, sell 0 `[DP:block_stratified]` — unambiguous accumulation at the mega tier.
- **07-09 whole-session aggressor: $590.1M lift/buy vs $3.6M hit/sell** (50.0M buy shares) `[DP:duckdb aggressor]` — one-directional demand.
- **Accumulation continued 07-13** (as-of): large tier buy_ratio **0.612**, $337.3M, 2,964 trades `[DP:block_stratified]` — not a one-day event.
- **$11.80 institutional shelf: $678.8M / 57,525,024 sh / 308 prints** over the 5-day window `[DP:price_levels]` — dominant support, 10× the next level.
- **Size ≈ ~14% of float** (54.6M / ~380M float) `[DP:block_pct_float]` — extraordinary single-session ownership transfer; block/secondary/index scale, not open-market drip.

## Detailed findings

### Largest blocks (07-09, the flagged event)

| Time (ET) | Size | Price | Premium | NBBO (bid/ask) | Aggressor | % float* |
|-----------|------|-------|---------|----------------|-----------|----------|
| 16:11:17 | 30,399,031 | $11.80 | $358.7M | 11.74 / 11.80 | lift/buy (at ask) | ~8.0% |
| 16:47:52 | 19,431,521 | $11.80 | $229.3M | 11.78 / 11.80 | lift/buy (at ask) | ~5.1% |
| 16:00:31 | 4,764,651 | $11.80 | $56.2M | 11.74 / 11.83 | abv_mid | ~1.3% |
| 15:45 (RTH) | 80,458 | $11.79 | $0.95M | 11.79 / 11.80 | blw_mid | — |

\*% of ~380M float (WebSearch; fz/uw float null). Combined mega = 54.6M ≈ **~14% of float**.
As-of 07-13 the largest blocks are normal-sized (~$500k, e.g. 42,190 sh @ $11.96) — the mega event is 07-09 only.

### Tier breakdown (buy_ratio; sell = 1 − buy_ratio)

| Date | Tier | buy_ratio | buy sh | sell sh | premium | trades |
|------|------|-----------|--------|---------|---------|--------|
| 07-09 | **mega** | **1.000** | 54,595,203 | 0 | $644.2M | 3 |
| 07-09 | large | 0.695 | 5,434,641 | 2,386,731 | $91.9M | 815 |
| 07-09 | *all tiers* | — | — | — | **$736.1M** | — |
| 07-13 (as-of) | large | 0.612 | 17,304,526 | 10,965,546 | $337.3M | 2,964 |

Both the mega event (100% buy) and the continuation (61% buy two sessions later) are net-accumulation. No offsetting sell tier.

### Price levels (5-session window) `[DP:price_levels]`

| Level | Premium | Shares | Prints |
|-------|---------|--------|--------|
| **$11.80** | **$678.8M** | 57,525,024 | 308 |
| $11.92 | $46.6M | 3,908,515 | 422 |
| $11.79 | $41.2M | 3,497,718 | 361 |
| $11.91 | $41.2M | 3,455,891 | 365 |
| $11.93 | $38.6M | 3,238,945 | 348 |

$11.80 dwarfs everything — the institutional cost-basis shelf and primary support. The $11.78–11.94 cluster is the current trading range where continuation buying sits.

### Extended-hours activity

The entire mega event is afterhours (16:00–16:47 ET on 07-09), all at $11.80. Uniform price + seconds-apart execution + 100% buy tier = a **pre-arranged block/cross**, not organic tape. Two additional AH prints (12,209 & 8,750 sh, also $11.80) tag along. This concentration is exactly what accompanies a secondary placement, a strategic stake, or an index/ETF reconstitution cross — **phase-6 must attribute it.**

## Tool calls (audit trail)

| Command | Key value(s) ← `jq` path | Rows |
|---------|--------------------------|------|
| `dark-pool largest --symbol PATH --date 2026-07-09 --sort-by premium` | 30.4M @ $11.80 = $358.7M ← `.results | sort_by(-.premium)[0]` | 25 |
| `dark-pool block-stratified --date 2026-07-09 --min-tier large` | mega buy_ratio 1.0, $644.2M ← `.results[0].mega.buy_ratio` | 1 |
| `dark-pool block-stratified --date 2026-07-13` | large buy_ratio 0.612 ← `.results[0].large.buy_ratio` | 1 |
| `dark-pool extended-hours --date 2026-07-09` | 30.4M/19.4M @ $11.80 AH ← `.results[].{size,price}` | 3 |
| `dark-pool price-levels --days 5` | $11.80 shelf $678.8M ← `sort_by(-.total_premium)[0]` | 15 |
| `dark-pool ticker-summary --date 2026-07-13` | PATH outside top-30 (07-13 normal) ← `select(.ticker=="PATH")` | 0 |
| DuckDB all-history (64 dp files) | 07-09 prints = local all-time top-3 by 15× ← `ORDER BY premium DESC` | — |
| DuckDB 07-09 aggressor split | lift/buy $590.1M vs hit/sell $3.6M ← `CASE price vs nbbo` | — |
| WebSearch float | ~366–392M float / ~535M shares out | — |

## Tool errors

- `dark-pool largest/extended-hours --date 2026-07-13` return only the single as-of day (normal-sized) — the flagged event is on 07-09, so re-queried with `--date 2026-07-09`. Not an error; a windowing property. All 07-09 numbers trace to the explicit 07-09 query.
- `insights deep-dive` / `fz quote` return null for float/shares_outstanding — used WebSearch fallback (float ~366–392M) per phase-0 `fz_available` note.

## DATA NOTE / CORRECTION

- price-levels field is `price_level`/`total_premium`/`total_shares`/`trade_count`
  (no `price`/`size`). First jq used wrong keys → empty; re-read against correct
  paths → shelf values above.

## Verdict for downstream

- **Institutional bias:** **ACCUMULATION** (mega buy_ratio 1.0; $590M lifted vs $3.6M sold; price held above the $11.80 shelf; buying continued 07-13 at 61% buy).
- **Conviction:** **4/5** on the accumulation read — but see the caveat: this is the single most important fact of the workup AND the single biggest attribution risk.
- **Largest block as % of float:** **~14%** of float in one afterhours session (54.6M / ~380M) `[DP:block_pct_float fz-fallback]` — **highly meaningful for this name**; only block/secondary/index-scale actors move this much. Precisely because it is so large, treat "buy at ask" cautiously: a negotiated cross's NBBO aggressor tag is weaker evidence of *directional intent* than an open-market lift.
- **Three S/R levels for phase-9:**
  1. **$11.80** — institutional cost-basis shelf / primary support ($678.8M, 57.5M sh). A close below it invalidates the accumulation thesis.
  2. **$11.78–11.85** — continuation accumulation band (07-13 large-tier buying).
  3. **~$12.15–12.17** — near-term overhead (07-13 blocks printed up to $12.145); first resistance.
- **Open questions (LOUD — for phase 6):** *What was the 07-09 block?* Strategic buyer / activist (bullish), secondary offering placement (a holder distributing, demand absorbing = neutral), or Russell/index reconstitution cross (mechanical, low directional signal — one source flags Russell rebalancing around this window)? The entire directional read hinges on this. Also: does phase-3 OI show a call/put wall at $12? Do phase-1's $12 LEAP puts hedge this exact long?
