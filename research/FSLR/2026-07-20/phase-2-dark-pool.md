# Phase 2 — Dark Pool & Block Prints

**Ticker:** FSLR · **As-of:** 2026-07-20 · **Underlying:** $210.56 · **Version:** v1
**Generated:** 2026-07-20
**Cites:** phase-1-flow.md (net_flow −$3.8M bearish, 5-session bearish sweep
campaign); phase-0.5-context.md (BUSY_NAME_NORMAL_DAY → confluence capped at `+`).

## Summary

Off-exchange activity is **mildly accumulative and in tension with the bearish
options tape.** The dominant large-tier ($100k–$1M) prints — $17.9M across 81
trades — are **63.9% buy** (net accumulation), outweighing the only two block-tier
($1M+) prints, which were **100% sell** ($2.0M). There are **no mega-tier
($10M+) blocks.** Five-day institutional price-levels cluster mostly **above spot**
($220–230 zone) with the single biggest, highest-conviction shelf at **$211.99
(27 trades, $9.42M)** just above spot and a heavy **support shelf at $205.31**
(25 trades intraday + a 15-print, $5.0M post-market cluster all at $205.31). Net:
institutions look to be **quietly buying shares up into $205–212 while the options
desk sells vol / hedges** — a divergence to flag, not a clean directional signal.
Buy-ratio 0.639 is in the "suggestive only" band, so conviction stays moderate.

## Key signals

- **[DP:block_stratified]** Large tier **64% buy** ($17.9M / 81 trades) — net
  accumulation; but block tier ($2.0M / 2 trades) **100% sell** → mixed, volume
  favours accumulation.
- **[DP:price_levels]** Biggest 5-day cluster **$211.99 — $9.42M, 44,428 sh, 27
  trades**, within 1% of spot → primary institutional pivot/resistance shelf.
- **[DP:extended_hours]** **All 15** post-market prints at **exactly $205.31**,
  24,448 sh / **$5.0M** — a coordinated close/after-hours block defining a support
  shelf ~2.5% under spot.
- **[DP:largest]** 25 blocks, $11.6M / 56,046 sh today; largest single = 4,896 sh
  / $1.00M at $204.66 (below spot). No block ≥ $10M → no whale-tier conviction.
- **[DP:price_levels]** Upside clusters stacked $220.58 → $230 ($2.7M–$8.1M each,
  mostly 1–10 trades) → prior institutional transaction zone overhead.

## Detailed findings

### Largest blocks (top 6 by premium; % of float advisory)
| Time (UTC) | Price | Size | Premium | vs spot | % float |
|-----------|-------|------|---------|---------|---------|
| 19:08 | $204.66 | 4,896 | $1.00M | −2.8% | n/a |
| 15:53 | $208.43 | 4,800 | $1.00M | −1.0% | n/a |
| 13:30 | $214.85 | 3,988 | $0.86M | +2.0% | n/a |
| 20:00 | $205.31 | 3,475 | $0.71M | −2.5% | n/a |
| 19:44 | $205.03 | 3,078 | $0.63M | −2.6% | n/a |
| 20:00 | $205.31 | 2,800 | $0.57M | −2.5% | n/a |

`% of float` = **n/a** — `fz`/Yahoo float unavailable this run (phase-0). In
absolute terms every block is ≤ ~4,900 sh and total 5-day DP is modest, so no
single print is float-material; treat size as advisory only.

### Tier breakdown — `[DP:block_stratified]`
| Tier | Trades | Premium | buy_ratio | derived sell_ratio | Read |
|------|--------|---------|-----------|--------------------|------|
| mega (≥$10M) | 0 | $0 | — | — | none |
| block (≥$1M) | 2 | $2.00M | **0.00** | **1.00** | 100% sell |
| large (≥$100k) | 81 | **$17.91M** | **0.639** | 0.361 | net **buy** |
| retail (<$100k) | — | — | — | — | noise |

Volume-weighted the accumulation (large tier, $17.9M) dominates the two block
sells ($2.0M). 0.639 is *suggestive*, not high-confidence (>0.7).

### Price levels (5-day clusters; spot $210.56) — `[DP:price_levels]`
| Level | Premium | Shares | Trades | vs spot |
|-------|---------|--------|--------|---------|
| **$211.99** | **$9.42M** | 44,428 | **27** | +0.7% (within 1%) |
| $223.82 | $8.12M | 36,299 | 10 | +6.3% |
| $224.50 | $7.03M | 31,300 | 2 | +6.6% |
| **$205.31** | $6.21M | 30,226 | **25** | −2.5% |
| $211.93 | $3.68M | 17,349 | 16 | +0.7% (within 1%) |
| $220.58 | $2.99M | 13,562 | 10 | +4.8% |

High-conviction (high trade-count) shelves: **$211.99 / $211.93** (pivot at spot)
and **$205.31** (support). The $220–230 clusters are largely single big blocks
(prior transaction memory, thinner conviction). Window = 2026-07-14 → 07-20
(`--days` anchors to latest date = as-of ✓, matches phase-0 available-dates).

### Extended-hours activity — `[DP:extended_hours]`
All 15 EH prints at **$205.31**, 24,448 sh / **$5.0M** (largest 3,475 sh). A
single tight post-market cluster — either a closing-cross/rebalance print or a
deliberate institutional block at $205.31. De-rate directional weight (could be
mechanical) but it firmly marks $205.31 as an institutional reference.

## Tool calls
| Tool | Args | Result |
|------|------|--------|
| dark-pool largest | FSLR, top 25, sort premium, date 07-20 | 25 blocks, $11.6M |
| dark-pool block-stratified | FSLR, top 30, min-tier large | large 64% buy / block 100% sell; no mega |
| dark-pool extended-hours | FSLR, top 15 | 15 prints, all $205.31, $5.0M |
| dark-pool price-levels | FSLR, top 15, days 5 | 15 clusters (07-14→07-20) |
| dark-pool ticker-summary | top 30, date 07-20 | **FSLR outside top-30** |

## Tool errors
None. All reads round-tripped through `jq`. `block-stratified` buy/sell read from
nested `.results[0].<tier>.buy_ratio` (no `sell_ratio` field — derived as
`1−buy_ratio`, per `lib/uw-json-paths.md`).

## Verdict for downstream

- **Net institutional bias:** **MILD ACCUMULATION** (large tier 64% buy, $17.9M),
  **in tension with the bearish options tape (phase-1).** Read as smart money
  accumulating shares into $205–212 while the options desk harvests premium /
  hedges — a divergence phase-8/8b must resolve.
- **Conviction: 2.5/5** — buy-ratio 0.639 is only *suggestive*; no mega blocks;
  FSLR outside the DP ticker-summary top-30 (not a standout DP name today); and
  `[CTX:]` BUSY_NAME_NORMAL_DAY caps phase-1–2 confluence at `+`.
- **Largest block as % of float:** **n/a** (no float this run) — but absolute
  sizes (≤ ~4.9k sh) are not float-material; size is advisory, not conviction.
- **Three S/R levels for phase-9:**
  1. **$205.31** — support shelf (25 intraday + $5.0M post-market prints). Natural
     stop reference for a long / target for a short.
  2. **$211.99 / $211.93** — pivot at spot (43 combined trades). Acceptance above =
     bullish; rejection = the bears' level.
  3. **$220–224** — overhead supply (prior institutional transaction zone); first
     meaningful resistance on any squeeze.
- **Open questions:**
  - Does phase-3/4 OI place the max-pain / dealer wall near $211 or $205,
    corroborating a pin between the two DP shelves?
  - Is the $205.31 post-market cluster mechanical (rebalance) or a real position?
    Phase-6 to check for overnight news.
  - Can mild share accumulation coexist with a 5-day bearish sweep campaign — i.e.
    delta-neutral vol selling against a long book? Phase-8b to adjudicate.
