# Phase 2 — Dark Pool & Block Prints

**Ticker:** CRM
**As-of date:** 2026-06-05
**Generated:** 2026-06-06T16:05:00-04:00
**Upstream:** phase-0-intake.md (`Shs Float` 792.65M `fz`), phase-0.5-context.md
(`[CTX:] BUSY_NAME_NORMAL_DAY` — phase capped at `+`), phase-1-flow.md (open
question: "is dark pool accumulating or distributing under the flat options tape?")

## Summary

The 5-session dark-pool tape reads **distribution-into-strength followed by
participation collapse**. Price context (verified from screener closes, see
§Price path): CRM ran +19% in two sessions post-earnings (176.17 → 209.60 by
6/01) then faded four straight sessions to 185.66. DP dollar volume peaked
exactly at the highs — $931.9M (4.49M sh) on 6/01 at prints of 197–211 — and
shrank monotonically to $249.0M (1.34M sh) on 6/05 as price fell. Today's tape
is balanced (large-tier buy_ratio 0.489 across 613 trades); the headline
mega-tier buy_ratio 0.693 is just n=2 closing-cross prints at 185.66 and carries
no directional confidence. Size is immaterial vs float (largest block = 0.020%
of float). Net: **mixed today, distribution on the week**; answers phase-1's
open question — dark pool is NOT confirming the Jan-2027 bullish risk reversal.

## Price path (cross-check, DuckDB)

`[DP:price_path DUCKDB]` screener closes: 5/28 176.17 → 5/29 191.10 (+8.47%,
earnings) → 6/01 **209.60** (+9.68%) → 6/02 200.84 (−4.18%) → 6/03 190.61
(−5.09%) → 6/04 188.75 (−0.98%) → 6/05 **185.66** (−1.64%). The fz drift in
phase-0 (191.10→185.66) silently spanned this +19%/−11.4% round trip — later
phases must use this path, not a smooth decline.

## Key signals

- **DP participation collapsed as price fell:** 6/01 $931.9M / 4.49M sh (prints
  197.10–211.30) → 6/02 $841.4M → 6/03 $333.6M → 6/04 $573.4M → 6/05 **$249.0M /
  1.34M sh** (prints 183.70–192.38). Institutions transacted heaviest at the
  top; appetite at 185 is the week's lowest. `[DP:price_path DUCKDB]`
- **Largest genuine 5-session clusters sit OVERHEAD:** ~189 ($415.9M), ~201
  ($415.3M), ~210 ($413.7M, 1,149 trades) — ~$830M of DP volume transacted at
  200–211, now trapped supply above spot. `[DP:price_levels]` cross-checked
  `[DP:level_xcheck DUCKDB]`
- **Today balanced, not accumulating:** large-tier buy_ratio 0.489 (613 trades,
  $145.5M), block-tier 0.544 (28 trades, $61.2M) — both inside the 0.45–0.55
  dead zone. `[DP:block_stratified]`
- **Mega-tier 0.693 buy_ratio is a 2-print artifact:** buy leg = 157,569 sh @
  185.66 20:58:07Z (printed above the 185.01/185.45 NBBO — after-hours
  closing-benchmark cross, $29.25M), sell leg = 69,900 sh @ 185.66 20:00:11Z (at
  the bell). Probabilistic classification of benchmark crosses — discard as
  directional signal. `[DP:largest]` `[DP:block_stratified]`
- **CRM absent from DP ticker-summary top-30** (leaders QQQ $21.4B, SPY $20.9B,
  MU $15.5B) — consistent with `[CTX:] BUSY_NAME_NORMAL_DAY`. `[DP:ticker_summary]`

## Detailed findings

### Largest blocks (2026-06-05)

| Time (UTC) | Price | Size | Premium | % float | NBBO context |
|---|---|---|---|---|---|
| 20:58:07 | 185.66 | 157,569 | $29.25M | 0.020% | above ask (185.01/185.45) — AH benchmark cross |
| 20:00:11 | 185.66 | 69,900 | $12.98M | 0.009% | inside (185.50/187.50) — closing cross |
| 20:00:16 | 185.66 | 42,233 | $7.84M | 0.005% | closing cross |
| 19:29:54 | 186.00 | 36,700 | $6.83M | 0.005% | at mid (185.97/186.03) — intraday block |
| 19:49:19 | 186.36 | 24,420 | $4.55M | 0.003% | inside — intraday block |
| 21:06:41 | 185.66 | 19,921 | $3.70M | 0.003% | AH cross |

`[DP:largest]` `[DP:block_pct_float fz]` All ≤0.020% of the 792.65M float —
size is noise *for this name*; no single print carries conviction.

### Tier breakdown (block-stratified, min-tier large)

| Tier | buy_ratio | derived sell_ratio | Buy vol | Sell vol | Premium | Trades |
|---|---|---|---|---|---|---|
| mega | 0.693 | 0.307 | 157,569 | 69,900 | $42.23M | **2** (closing crosses — discard) |
| block | 0.544 | 0.456 | 178,953 | 149,957 | $61.23M | 28 |
| large | 0.489 | 0.511 | 380,950 | 397,874 | $145.54M | 613 |

`[DP:block_stratified .results[].<tier>.buy_ratio]` (no `sell_ratio` field;
derived = 1 − buy_ratio). All tiers inside or near the 0.45–0.55 indeterminate
band once the 2-print mega tier is discarded → **balanced day**.

### Price levels (5-day window, --days anchors to latest = 2026-06-05 ✓)

Top reported levels `[DP:price_levels]`: 188.75 ($349.5M), 200.84 ($312.0M),
190.61 ($135.6M), 209.60 ($112.3M), 199.75 ($84.5M), 185.66 ($78.4M).
**Caveat applied:** 188.75 / 200.84 / 190.61 / 209.60 / 185.66 are *exactly* the
6/04, 6/02, 6/03, 6/01, 6/05 closes — these "levels" are closing-cross
aggregations, benchmark activity, not chosen institutional levels.
DuckDB re-cut on the same 5 sessions (rounded to $1) gives the genuine volume
shelf map: **~189 $415.9M · ~201 $415.3M · ~210 $413.7M · ~191 $241.1M · ~186
$161.3M** `[DP:level_xcheck DUCKDB]`. Two-thirds of the week's DP dollar volume
sits 200–211, far above spot 185.66 — overhead supply, not support. Nearest
real shelf below spot: thin (~186 is current price; next meaningful prints
183.70 = week's low).

### Extended-hours activity

All large AH prints (20:58, 21:06 UTC) are at exactly 185.66 = the 4pm closing
price → benchmark/MOC-style crosses, NOT directional overnight positioning.
Per the pitfall rule these are flagged and de-rated; no genuine pre-market
prints surfaced. `[DP:extended_hours]`

## Tool calls

| Command | jq path | Status |
|---|---|---|
| `uw dark-pool largest --symbol CRM --top-n 25 --sort-by premium --date 2026-06-05 --json` | `.results[] {executed_at,price,size,premium,nbbo_bid,nbbo_ask}` | ok n=25 |
| `uw dark-pool block-stratified --symbol CRM --top-n 30 --min-tier large --date 2026-06-05 --json` | `.results[].{mega,block,large,retail}.buy_ratio` | ok |
| `uw dark-pool extended-hours --symbol CRM --top-n 15 --date 2026-06-05 --json` | `.results[]` | ok n=15 |
| `uw dark-pool price-levels --symbol CRM --top-n 15 --days 5 --json` | `.results[] {price_level,total_premium,total_shares}` | ok n=15 (window anchors latest=as-of ✓) |
| `uw dark-pool ticker-summary --top-n 30 --date 2026-06-05 --json` | filter ticker==CRM | ok — CRM absent |
| DuckDB: per-day DP range/premium + 5-session level re-cut + close series | (verification cuts) | ok |

## Tool errors

None. (price-levels returned valid JSON; its closing-cross composition is an
interpretation caveat, not a tool error.)

## Verdict for downstream

- **Bias: MIXED today / DISTRIBUTION on the 5-session window** — heaviest DP
  at the 200–211 top, participation collapsing into the fade, no buy-side
  step-up at 185–186.
- **Conviction: 3/5** on the weekly distribution read (volume-at-price is
  classification-independent); 2/5 on today's balanced tape.
- **Largest block as % of float: 0.020%** (157.6k sh / 792.65M `fz`) — not a
  meaningful size for this name; the week's entire DP tape ≈ 1.9% of float.
- **Three S/R levels for phase-9:**
  1. **~189–191 resistance** (189 shelf $415.9M + 191 shelf $241.1M + 5/29
     earnings close 191.10) — first supply band above spot.
  2. **~200–201 heavy resistance** ($415.3M shelf at 201, 6/02 close 200.84).
  3. **~183.70–176 support zone** — 183.70 is the week's DP print low; 176.17
     pre-earnings close is the gap-fill magnet; almost no DP volume transacted
     between 176 and 186 (air pocket).
- **Open questions:** Did OI build at 190/195/200 calls confirm the trapped
  supply read (phase 3)? Was the 6/01 +9.7% second-leg surge news-driven and
  has that news decayed (phase 6)? Is the four-day fade a normal post-earnings
  retrace by historical analog or a failed breakout (phase 5)?
