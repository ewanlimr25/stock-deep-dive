# Phase 2 — Dark Pool & Block Prints

## Goal

Surface institutional off-exchange activity for `<SYMBOL>`: who's accumulating
or distributing, at what price levels, and during which sessions. Emit
`phase-2-dark-pool.md`.

## Tools

All ticker-scoped; some require `ticker=<SYMBOL>` (singular, not `symbol`).

| Tool | Args | What it answers |
|------|------|-----------------|
| `mcp__uw-pp__dark_pool_largest` | symbol, top_n=25, sort_by=premium | Biggest individual blocks |
| `mcp__uw-pp__dark_pool_block_stratified` | symbol, top_n=30, min_tier=large | Premium tier breakdown + buy/sell ratio |
| `mcp__uw-pp__dark_pool_extended_hours` | symbol, top_n=15 | Pre/post-market institutional moves |
| `mcp__uw-pp__dark_pool_price_levels` | ticker=<SYMBOL>, top_n=15, days=5 | Institutional S/R clusters |
| `mcp__uw-pp__dark_pool_ticker_summary` | top_n=30 | Verify `<SYMBOL>` ranks in today's top |

## Composition guidance

- `dark_pool_price_levels` is the only one that natively supports multi-day
  aggregation — use `days=5` to find clusters not just today's prints.
- Cross-reference `dark_pool_extended_hours` against any overnight news in
  phase-6 to attribute (or rule out) news-driven prints.

## Output sections

1. **Summary** — net institutional bias (accumulation / distribution /
   balanced) + premium magnitude.
2. **Key signals** — top-5 with `[DP:<tool>]` citations.
3. **Detailed findings**
   - ### Largest blocks (table: time, price, size, premium, NBBO context)
   - ### Tier breakdown (mega / block / large + buy/sell ratio per tier)
   - ### Price levels (sorted; flag clusters within 1% of spot)
   - ### Extended-hours activity (any unusual pre/post-market)
4. **Tool calls** — audit.
5. **Tool errors** — verbatim.
6. **Verdict for downstream**
   - Accumulation / Distribution / Mixed
   - Conviction 1–5 (size + tier + consistency)
   - Three S/R levels for phase-9 to use as entry/stop reference
   - Open questions

## Interpretation heuristics

- **Accumulation:** mega-tier buy_ratio ≥ 0.55 AND price levels cluster ABOVE
  current spot (institutions paying up).
- **Distribution:** mega-tier sell_ratio ≥ 0.55 AND clusters BELOW spot.
- **Pin formation:** multiple medium-tier prints at the same strike within
  OPEX week — cross-reference with phase-3 `oi_pin_risk`.
- **Hedging:** large block premium concentrated in pre/post-market right
  before catalyst date — distinct from directional accumulation.

## Common pitfalls

- Dark pool buy/sell classification is probabilistic (NBBO-based). Treat
  ratios > 0.7 as high-confidence, 0.55–0.7 as suggestive only.
- Index ETFs and mega-caps print dark pool blocks all day every day — the
  signal is in CHANGE versus their ticker-summary baseline.
- Extended-hours prints can be index rebalancing or ETF creation/redemption,
  not directional intent. Flag and de-rate conviction if so.
