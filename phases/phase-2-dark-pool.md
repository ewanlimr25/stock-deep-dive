# Phase 2 — Dark Pool & Block Prints

## Goal

Surface institutional off-exchange activity for `<SYMBOL>`: who's accumulating
or distributing, at what price levels, and during which sessions. Emit
`phase-2-dark-pool.md`.

## Tools

All take `--symbol` (the CLI unifies what the old MCP split between `symbol` and
`ticker`) and `--json`. Pass `--date <AS-OF>` if not today.

| Command | What it answers |
|---------|-----------------|
| `uw dark-pool largest --symbol <S> --top-n 25 --sort-by premium --json` | Biggest individual blocks |
| `uw dark-pool block-stratified --symbol <S> --top-n 30 --min-tier large --json` | Premium tier breakdown + buy/sell ratio |
| `uw dark-pool extended-hours --symbol <S> --top-n 15 --json` | Pre/post-market institutional moves |
| `uw dark-pool price-levels --symbol <S> --top-n 15 --days 5 --json` | Institutional S/R clusters |
| `uw dark-pool ticker-summary --top-n 30 --json` | Verify `<SYMBOL>` ranks in today's top |

## Composition guidance

- `uw dark-pool price-levels` is the only one that natively supports multi-day
  aggregation — use `--days 5` to find clusters not just today's prints.
  **Caveat:** `--days` anchors its window to the *latest available date*, not to
  `--date`; on a re-run after a new session lands the window slides. Cross-check
  the returned cluster premiums against phase-0's available-dates list.
- **`block-stratified` buy/sell lives nested per tier**, not as a row column: the
  buy fraction is `.results[].<tier>.buy_ratio` (e.g. `.results[0].mega.buy_ratio`),
  with `buy_volume`/`sell_volume`/`total_premium` alongside. **There is no
  `sell_ratio` field** — derive `sell_ratio = 1 − buy_ratio` (or
  `sell_volume/(buy_volume+sell_volume)`). Extract e.g.
  `… --json | jq '.results[] | {ticker, mega_buy: .mega.buy_ratio}'`.
- Cross-reference `uw dark-pool extended-hours` against any overnight news in
  phase-6 to attribute (or rule out) news-driven prints.
- **Float-normalize block size (D2, advisory).** If phase-0 captured `Shs Float`
  (`fz`, `lib/fz-recipes.md`), express the mega/block-tier print size as a **% of
  float** (`block_shares / Shs Float × 100`). Order size is meaningless in the
  abstract — a mega block is conviction in a 5M-float name and noise in a
  14.67B-float name. This is **advisory context for the verdict, not a new gate**
  and never raises conviction. Tag `[DP:block_pct_float fz]`. Skip if
  `fz_available=no`.

## Output sections

1. **Summary** — net institutional bias (accumulation / distribution /
   balanced) + premium magnitude.
2. **Key signals** — top-5 with `[DP:<tool>]` citations.
3. **Detailed findings**
   - ### Largest blocks (table: time, price, size, premium, NBBO context; add a
     **% of float** column for the top prints if `Shs Float` is available)
   - ### Tier breakdown (mega / block / large + buy/sell ratio per tier)
   - ### Price levels (sorted; flag clusters within 1% of spot)
   - ### Extended-hours activity (any unusual pre/post-market)
4. **Tool calls** — audit.
5. **Tool errors** — verbatim.
6. **Verdict for downstream**
   - Accumulation / Distribution / Mixed
   - Conviction 1–5 (size + tier + consistency)
   - Largest block as **% of float** (advisory; "n/a" if no `Shs Float`) — one
     line on whether the size is meaningful *for this name*
   - Three S/R levels for phase-9 to use as entry/stop reference
   - Open questions

## Interpretation heuristics

- **Accumulation:** mega-tier `buy_ratio` ≥ 0.55 (`.results[].mega.buy_ratio`) AND
  price levels cluster ABOVE current spot (institutions paying up).
- **Distribution:** mega-tier `buy_ratio` ≤ 0.45 (i.e. derived `sell_ratio` ≥ 0.55 —
  there is no `sell_ratio` field) AND clusters BELOW spot.
- **Pin formation:** multiple medium-tier prints at the same strike within
  OPEX week — cross-reference with phase-3 `oi_pin_risk`.
- **Hedging:** large block premium concentrated in pre/post-market right
  before catalyst date — distinct from directional accumulation.

## Common pitfalls

- Dark pool buy/sell classification is probabilistic (NBBO-based). Treat
  ratios > 0.7 as high-confidence, 0.55–0.7 as suggestive only. These thresholds
  are on `buy_ratio`; for a sell read use `1 − buy_ratio` symmetrically.
- Index ETFs and mega-caps print dark pool blocks all day every day — the
  signal is in CHANGE versus their ticker-summary baseline.
- Extended-hours prints can be index rebalancing or ETF creation/redemption,
  not directional intent. Flag and de-rate conviction if so.
