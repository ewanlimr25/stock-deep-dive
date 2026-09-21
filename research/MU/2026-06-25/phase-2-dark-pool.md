# Phase 2 — Dark Pool & Block Prints

**Ticker:** MU
**As-of date:** 2026-06-25
**Generated:** 2026-06-25
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md, phase-1-flow.md

## Summary

MU is the **#1 dark-pool name in the entire market today by premium ($29.31B)** —
printing *above* every index ETF (IVV $16.2B, VOO $15.1B, SPY $11.3B) with peer
SNDK #5 ($8.96B). Institutional engagement is enormous. **But the directional read
is balanced, not accumulation:** tier buy_ratios are mega **0.47**, block **0.504**,
large **0.511** — none breach the 0.55 (accumulation) or 0.45 (distribution) lines,
and the largest tier (mega) is a slight *sell* lean. So despite phase-1's bullish
call premium and a strong **+4% up day** (intraday ~$1,165 → close ~$1,213),
institutions transacted **two-way into the rally** rather than accumulating —
a yellow flag the dark pool does not independently confirm the bullish flow. The
constructive offset: a heavy 5-session accumulation shelf sits at **~$1,134** with
secondary support **~$1,050-1,059**, while recent prints cluster as supply at the
**~$1,211-1,214** highs.

## Key signals

- **#1 DP name market-wide, $29.31B**, above all index ETFs `[DP:ticker_summary]`
- Tier buy/sell **balanced**: mega 0.47 / block 0.504 / large 0.511 — no accumulation tilt `[DP:block_stratified]`
- Heaviest 5-day price shelf **$1,134** ($5.14B, 4.53M sh, 223 prints) — support below spot `[DP:price_levels]`
- Largest block **$694M / 572,240 sh @ $1,213.56**, after-hours closing cross, below NBBO bid — likely mechanical `[DP:largest / extended_hours]`
- Largest block = **0.05% of 1.12B float**; full-day DP = ~2.18% of float `[DP:block_pct_float fz]`

## Detailed findings

### Largest blocks `[DP:largest]`

| Price | Size | Premium | Time (UTC) | NBBO | % float |
|-------|------|---------|------------|------|---------|
| 1213.56 | 572,240 | **$694.4M** | 20:05:54 (post-close) | bid 1215 / ask 1216 (below bid) | 0.051% |
| 1213.56 | 50,580 | $61.4M | 20:00:17 | — | 0.005% |
| 1213.56 | 42,960 | $52.1M | 20:00:06 | — | 0.004% |
| 1213.56 | 42,000 | $51.0M | 20:00:24 | — | 0.004% |
| 1206.63 | 40,998 | $49.5M | 20:07:56 | — | 0.004% |

The blocks concentrate at **20:00–20:07 UTC (the 4 pm ET close / after-hours)** at
~$1,213.56 — i.e. **closing-cross prints**, not intraday directional accumulation.
The $694M top block is explicitly flagged `ext_hour_sold_codes:
extended_hours_trade` and printed **below the NBBO bid** (trade_vs_mid −1.94) — read
as a **facilitated/benchmark closing print, likely mechanical** (index/portfolio
rebalance), de-rated for directional intent.

### Tier breakdown `[DP:block_stratified]`

| Tier | buy_ratio | derived sell_ratio | total_premium | trades |
|------|-----------|--------------------|--------------:|-------:|
| mega | **0.47** | 0.53 | $1.61B | 44 |
| block | 0.504 | 0.496 | $5.41B | 3,004 |
| large | 0.511 | 0.489 | $22.30B | 114,344 |
| **all tiers** | — | — | **$29.31B** | — |

Every tier sits inside the 0.45–0.55 **balanced band**. Per the heuristic this is
neither accumulation (≥0.55) nor distribution (≤0.45); the mega tier's 0.47 is a
mild sell lean on the largest blocks. **Verdict: BALANCED** — the dark pool is not
corroborating phase-1's bullish premium with a buy tilt today.

### Price levels (5-session clusters, 2026-06-18 → 06-25) `[DP:price_levels]`

| Level | Premium | Shares | Prints | vs spot (~$1,213 close) |
|-------|---------|--------|--------|--------------------------|
| **$1,133.99** | **$5,142M** | 4,534,311 | 223 | **major support shelf, below** |
| $1,211.38 | $2,975M | 2,455,532 | 136 | at the highs (recent supply) |
| $1,213.56 | $1,617M | 1,332,595 | 176 | today's close level |
| $1,051.77 | $1,061M | 1,008,536 | 72 | lower support shelf |
| $1,048.51 | $1,041M | 992,779 | 46 | lower support shelf |
| $1,058.88 | $558M | 526,567 | 26 | lower support shelf |
| $1,190 / $1,200 / $1,110 | $170M / $142M / $137M | — | 451 / 358 / 154 | round-number pin magnets |

The dominant absorbed shelf is **~$1,134** (heaviest cluster by far, below current
price after the rally) — a strong support reference. A secondary shelf sits at
**~$1,050-1,059**. Recent prints stacking at **~$1,211-1,214** mark where today's
supply met the rally. Round numbers 1190/1200/1110 carry high print *counts* (pin
behaviour) — cross-reference phase-3 OI walls / phase-4 max-pain.

### Extended-hours activity `[DP:extended_hours]`

Dominated by the same **post-close prints at $1,213.56** (the $694M block + the
20:00 cluster). All flagged `extended_hours_trade`. Consistent with a closing
benchmark cross rather than informed overnight directional positioning — de-rate
conviction; cross-check phase-6 for any overnight news.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows |
|------------------|--------------------------|------|
| `dark-pool ticker-summary --top-n 30` | MU #1 market-wide $29.31B ← `.results[]\|select(.ticker=="MU")` | top-30 |
| `dark-pool largest --symbol MU --top-n 25 --sort-by premium` | $694.4M / 572,240 sh @ 1213.56 ← `.results[0]` | top-25 |
| `dark-pool block-stratified --symbol MU --min-tier large` | mega 0.47 / block 0.504 / large 0.511 ← `.results[0].<tier>.buy_ratio` | tiers |
| `dark-pool price-levels --symbol MU --days 5` | shelf $1,134 $5.14B ← `.results[].price_level` | 5 sess (6-18→6-25) |
| `dark-pool extended-hours --symbol MU --top-n 15` | post-close $694M cross ← `.results[0]` | top-15 |

## Tool errors

None — all five DP commands returned valid JSON.

## DATA NOTE / CORRECTION

`block-stratified` exposes buy fraction nested per tier (`.results[].<tier>.buy_ratio`);
there is no `sell_ratio` field — `sell_ratio` derived as `1 − buy_ratio`.
`price-levels --days 5` window confirmed = [06-25, 06-24, 06-23, 06-22, 06-18]
(matches phase-0 available dates; no gap contamination).

## Verdict for downstream phases

- **Institutional bias:** **BALANCED / MIXED** — massive volume (#1 DP name
  market-wide) but no directional tilt (all tiers 0.47–0.51). The dark pool does
  **not** confirm phase-1's bullish call premium with accumulation; institutions
  transacted two-way into the +4% day.
- **Conviction:** **2 / 5** on direction (engagement is 5/5, directional clarity is
  low). This is the first material cross-check *against* the bullish flow read.
- **Largest block as % of float:** **0.05%** (572,240 / 1.12B) — *not* meaningful by
  size for a 1.12B-float mega-cap; and it's a likely-mechanical closing cross. The
  durable signal is the **price-level shelves**, not block size. `[DP:block_pct_float fz]`
- **Three S/R levels for phase-9:**
  1. **Support ~$1,134** (heaviest 5-day absorbed shelf) → stop reference below.
  2. **Support ~$1,050-1,059** (secondary shelf) → deeper invalidation.
  3. **Supply/resistance ~$1,211-1,214** (recent prints at the highs / today's close).
- **Open questions:** Do phase-3 OI walls reinforce the $1,190-1,214 supply and the
  round-number pins (1190/1200/1110)? Is the balanced DP a sign the rally is
  *distribution into strength* (bearish) or healthy two-way digestion (neutral)?
  Phase-3/4 dealer positioning should arbitrate.
