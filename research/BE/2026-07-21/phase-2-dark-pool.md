# Phase 2 — Dark Pool & Block Prints

**Ticker:** BE
**As-of date:** 2026-07-21
**Generated:** 2026-07-22T08:10:00Z
**Upstream phases cited:** phase-1-flow.md, phase-0.5-context.md, phase-0-intake.md

## Summary

Dark-pool tape is **MIXED, not the confirming accumulation the options lean would
want.** The bulk large-tier tape ($385.5M) is *mildly bought* (buy_ratio 0.561)
and the one genuine intraday whale print (162,500 sh @ 229.22) lifted **above mid
(+$1.51) → bought**, but the mega tier reads 88.6% *sold* — driven entirely by
**three post-close crossing prints at the exact closing price 226.26** ($165.2M +
$76.5M + $45.3M), where NBBO-based buy/sell tagging is unreliable and the print is
more likely a closing-cross / portfolio transition than directional distribution.
The durable, usable output is the **institutional S/R map — 197 / 215 / 226 / 243
— which lines up precisely with phase-1's put-write floor (197.5–215) and spot.**
BE is outside today's DP top-30 (MU/SPY/QQQ/SNDK/NVDA/AMD dominate), matching
phase-0.5: heavy in absolute dollars, not a universe turnover leader.

## Key signals

- **Large tier (the bulk, $385.5M): buy_ratio 0.561** → mild accumulation `[DP:block_stratified]`
- **Mega tier: buy_ratio 0.114 (sell 0.886, $324.2M, 4 trades)** — but 3 of 4 are
  **post-close crosses at 226.26**, de-rated as non-directional `[DP:largest / extended_hours]`
- **Real intraday whale: 162,500 sh @ 229.22, $37.2M, +$1.51 above mid → bought** `[DP:largest]`
- **S/R clusters (5-day): 226.26 $311.6M · 197.06 $214.9M · 214.96 $82.6M · 243.4
  $51.1M** — 197/215 match phase-1 put-write strikes `[DP:price_levels]`
- BE **outside DP ticker-summary top-30** — large absolute ($794.9M) but not a
  turnover leader `[DP:ticker_summary]`

## Detailed findings

### Largest blocks `[DP:largest]`

| Size (sh) | Price | Premium | Exec (UTC) | vs_mid | Read |
|-----------|-------|---------|-----------|--------|------|
| 730,013 | 226.26 | $165.2M | 20:34 (post-close) | −0.99 | closing cross — non-directional |
| 338,305 | 226.26 | $76.5M | 20:49 (post-close) | −1.09 | closing cross — non-directional |
| 200,000 | 226.26 | $45.3M | 20:00 (post-close) | −0.17 | closing cross — non-directional |
| **162,500** | **229.22** | **$37.2M** | 18:37 (2:37pm ET) | **+1.51** | **intraday, bought above mid** |
| 42,100 | 225.42 | $9.5M | 19:16 | — | intraday |

The three 226.26 prints are extended-hours (per `extended_hours`, all after the
4pm close) at the fixed closing price — the "sold below mid" tag reflects a stale
post-close NBBO, not aggressor intent (pitfall: de-rate extended-hours prints).
The genuine directional whale is the 229.22 accumulation.

### Tier breakdown `[DP:block_stratified]`

| Tier | Premium | buy_ratio | derived sell_ratio | Read |
|------|---------|-----------|--------------------|------|
| large | $385.5M | **0.561** | 0.439 | mild accumulation (the bulk) |
| block | $85.1M | 0.432 | 0.568 | mild distribution |
| mega | $324.2M | **0.114** | 0.886 | *post-close cross-driven — de-rated* |
| **all tiers** | **$794.9M** | — | — | net **MIXED** |

Ex the post-close mega crosses, the tradeable intraday tape (large + the 229.22
whale) tilts mildly accumulative; the whale-tier is not confirming aggressive
buying and the closing crosses hint a large holder may be *reducing* — a genuine
yellow flag against the bullish options lean.

### Price levels — institutional S/R (5-day) `[DP:price_levels]`

| Level | 5-day premium | Role vs spot 226.26 |
|-------|---------------|---------------------|
| **226.26** | $311.6M | spot / heaviest (today's crosses) |
| **197.06** | $214.9M | **major support** — = phase-1 197.5 put-write floor |
| 214.96 | $82.6M | support — = phase-1 215 put-write strike |
| **243.40** | $51.1M | **first resistance above** |
| 206.5 | $46.1M | intermediate support |

This S/R map is the phase's highest-value output — it independently corroborates
the phase-1 options structure (puts written at 197.5/215, spot 226, upside toward
243/300).

### Extended-hours `[DP:extended_hours]`

All top ext-hours prints are the 226.26 closing crosses (20:00–20:50 UTC). No
pre-market news-driven accumulation; nothing that changes the directional read.
Flagged as post-close/non-directional.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|------------------|--------------------------|-----------|
| `dark-pool largest --symbol BE --sort-by premium` | 162,500@229.22 vs_mid +1.51 ← `.results[]｜.trade_vs_mid`; top block 730k@226.26 $165.2M | top-25 |
| `dark-pool block-stratified --symbol BE --min-tier large` | large buy 0.561, mega buy 0.114 ← `.results[0].large.buy_ratio / .mega.buy_ratio`; sell = 1−buy | 1 (tiered) |
| `dark-pool extended-hours --symbol BE` | 3× 226.26 post-close crosses ← `.results｜sort_by(-.premium)` | 15 |
| `dark-pool price-levels --symbol BE --days 5` | 197.06 $214.9M ← `.results[]｜.price_level/.total_premium` | 15 |
| `dark-pool ticker-summary` | BE not in top-30 ← `select(.ticker=="BE")` empty | 30 |

## Tool errors

<none — all four BE-scoped reads + ticker-summary returned valid JSON>

## DATA NOTE / CORRECTION

- `price-levels` field is `price_level` + `total_premium`/`total_shares` (not
  `price`/`premium`); `total_shares` returned null in the aggregated view — used
  `total_premium` for cluster ranking, which is the intended sort key.
- `block-stratified` buy/sell is nested per tier with **no `sell_ratio` field**;
  derived `sell_ratio = 1 − buy_ratio` per the phase spec (deep-dive-json-field-traps).

## Verdict for downstream phases

- **Institutional bias:** **MIXED** (large-tier mild-buy 0.561 vs mega post-close
  crosses; one intraday whale bought at 229.22). Not confirming accumulation.
- **Conviction:** **2.5 / 5** — the cleanest signal (S/R map) is high-value, but
  the directional buy/sell read is muddied by post-close crossing prints; whale
  tier is a yellow flag, not a green light.
- **Largest block as % of float:** **n/a** — phase-0 captured no `Shs Float`
  (`fz` degraded); cannot normalize the 730k-share cross to float. Advisory only.
  (Context: BE ~230M shares out per phase-7b to confirm; 730k ≈ ~0.3% — a
  meaningful single cross but not a float-dominating print.)
- **Three S/R levels for phase-9:** **support 197 (put-write floor, $214.9M DP) /
  215**, **spot pivot 226**, **first resistance 243**.
- **Open questions:** Is the mega closing-cross a large holder exiting (bearish
  overhang) or benign portfolio transition? Do the phase-3 OI walls sit at
  197/215/230 (put) and 243/300 (call) to confirm the S/R map? Does max-pain
  (phase-4) gravitate toward 226/230 into the 7/25 & 8/21 OPEX?
