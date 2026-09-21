# Phase 2 — Dark Pool & Block Prints

**Ticker:** ENPH
**As-of date:** 2026-07-27
**Generated:** 2026-07-27T20:30:00-04:00
**Upstream phases cited:** `phase-0-intake.md`, `phase-0.5-context.md`, `phase-1-flow.md`

## Summary

**No institutional accumulation. The headline buy-ratio is an artifact, and the
one genuinely informative print is bearish.** `block-stratified` reports a
block-tier `buy_ratio = 0.817` that looks like conviction buying — but it rests on
**`trade_count = 2`**, and both prints are mechanical: a 129,000-share **closing
auction cross** and a 28,800-share **options delta hedge**. Strip them and the real
tape is the large tier at `buy_ratio = 0.555` (36 trades) — inside the rubric's
"suggestive only" band and barely above balanced. Whole-tape aggressor
classification tilts the other way: **20.3% of DP volume hit the bid vs 15.2%
lifting the ask**, with `hit% > lift%` in **4 of the last 6 sessions**. There is
**no mega tier at all** (`trade_count = 0`; the reported `buy_ratio = 0.5` is a
placeholder, not data), and ENPH is **outside the market-wide top-30** by DP premium.

The phase's real contribution is a **cross-dataset confirmation that resolves
phase-1's biggest open question**. Phase-1 flagged the day's largest option print —
800× 2026-11-20 $35 puts, $464,000, `side = "mid"` — as directionally
*unattributable*. A `§B` timestamp join finds **exactly one** dark-pool print
within ±5 minutes: **28,800 shares at 11:06:45.556 ET, classified `hit`**, against
an option print at **11:06:45 ET**. The put position's delta is
`800 × 100 × 0.3451 = 27,608` shares; the block is **28,800 shares — a 96% match**,
sold into the bid. That is the signature of a dealer hedging a **short put
position**, i.e. **the customer bought those puts.** The day's single largest
option print reclassifies from "unknown" to **downside demand**.

## Key signals

- **Block-tier `buy_ratio = 0.817` is an artifact of `trade_count = 2`** — one
  closing cross (129,000 sh) and one delta hedge (28,800 sh). **Neither is
  directional intent.** [DP:block_stratified]
- **Delta-hedge confirmation of the Nov-20 $35 put:** sole DP print in the ±5-min
  window is **28,800 shares `hit`** vs a **27,608-share** put delta — 96% match,
  sub-second aligned. Customer **bought** the puts. [DP:ts_confirm DUCKDB]
- **Real institutional tier is near-balanced:** large tier `buy_ratio = 0.555`
  (derived `sell_ratio = 0.445`) on 36 trades, $5,916,119. [DP:block_stratified]
- **Aggressor tilt is to the sell side:** `hit% 20.3` vs `lift% 15.2` today, and
  `hit% > lift%` in **4 of 6** sessions. [DP:aggressor_split DUCKDB]
- **No mega tier, and ENPH is outside the top-30** by DP premium (leaders MU
  $11.16B, SMH $10.48B, SPY $9.24B). [DP:block_stratified], [DP:ticker_summary]

## Detailed findings

### Largest blocks

`uw dark-pool largest --symbol ENPH --top-n 25 --sort-by premium`. Float =
**127.77M** (`phase-0-intake.md`), used for the `% float` column.

| Time (ET) | Price | Size | Premium | NBBO bid/ask | `trade_vs_mid` | **% float** | Read |
|---|---|---|---|---|---|---|---|
| **16:00:30** | 38.01 | **129,000** | **$4,903,290** | 37.79 / 38.09 | +0.070 | **0.101%** | **Closing auction cross** |
| **11:06:45** | 36.70 | **28,800** | **$1,056,960** | 37.18 / 37.26 | **−0.520** | **0.023%** | **Delta hedge (see below)** |
| 11:52:53 | 36.64 | 9,650 | $353,575 | 36.55 / 36.61 | +0.060 | 0.008% | above mid |
| 10:11:45 | 36.86 | 8,067 | $297,350 | 36.88 / 36.98 | −0.070 | 0.006% | below mid |
| 12:49:27 | 37.20 | 7,502 | $279,074 | 37.11 / 37.15 | +0.070 | 0.006% | above mid |
| 15:59:10 | 38.04 | 6,542 | $248,825 | 38.03 / 38.04 | 0.000 | 0.005% | at mid |
| 15:41:14 | 37.91 | 6,267 | $237,582 | 37.85 / 37.89 | +0.040 | 0.005% | above mid |
| 13:23:15 | 36.55 | 6,000 | $219,300 | 36.55 / 36.60 | −0.025 | 0.005% | below mid |
| 15:46:39 | 37.80 | 5,649 | $213,532 | 37.76 / 37.81 | +0.015 | 0.004% | above mid |
| 15:38:54 | 37.77 | 5,500 | $207,735 | 37.77 / 37.81 | −0.020 | 0.004% | below mid |

**Size is not meaningful for this name.** The largest block of the day is **0.101%
of float** and the entire day's dark-pool volume is **316,355 shares = 0.248% of
float**, or **10.2% of the 3,114,887-share session volume**. Below the third row
every print is under 0.01% of float. Per the phase-2 float-normalization guidance
this is **advisory and downside-only**: it cannot raise conviction, and here it
argues firmly for de-rating. Nothing on this tape is a position being built.

**The 28,800-share print — cross-dataset confirmation (`§B` escape hatch).**

```
DP prints within ±5 min of 11:06:45 ET, ENPH, canceled=false:
  executed_at                        size   prem_m  price  bid    ask    aggressor
  2026-07-27 11:06:45.556000-04:00  28800   1.057   36.70  37.18  37.26  hit
  (exactly one row)
```

| Leg | Value |
|---|---|
| Option print (`phase-1-flow.md`) | 2026-11-20 **P35**, size **800**, $464,000, `side="mid"`, `delta = −0.3451`, `underlying_price = 37.225`, **11:06:45 ET** |
| Implied hedge | `800 × 100 × 0.3451` = **27,608 shares** |
| Observed DP print | **28,800 shares**, `hit`, **11:06:45.556 ET** |
| **Match** | **96.0%** (Δ 1,192 shares), **sub-second** |

A dealer who **sells** puts to a customer is long delta and hedges by **selling
stock** — which is what a `hit` is. The alternative (customer sells puts → dealer
buys puts → dealer **buys** stock) would print a `lift`. It printed a `hit`.
**The customer was the put buyer.** This upgrades the day's largest option print
from unattributable to **genuine downside demand**, and it is the single most
useful fact this phase produces.

**Two honest caveats, neither of which overturns it:**

1. **The print is $0.48 *below* the NBBO bid** (36.70 vs bid 37.18) — far outside
   the quote for a normal aggressive sale. Note that **$36.70 is exactly the prior
   session's close** (`prev_close = 36.70`, `phase-0.5-context.md`). This is the
   signature of a **negotiated block priced at a reference (prior close)**, not a
   market sweep. The `hit` label is therefore partly a classification artifact of
   reference pricing. It still means stock was *supplied* at a below-market price,
   which is the direction the hedge interpretation requires — but the *aggression*
   implied by "hit" is overstated.
2. **Coincidence cannot be fully excluded.** One print, one window. The 96% size
   match and sub-second alignment make coincidence unlikely but not impossible.
   Confidence: **high, not certain.** Phase-3 can settle it — if 2026-07-28 OI on
   the Nov-20 $35 put rises by ~800, the position opened.

### Tier breakdown

`uw dark-pool block-stratified --symbol ENPH --min-tier large`.
Tier boundaries (from the tool's own `caveat`): mega ≥$10M, block ≥$1M,
large ≥$100k, retail <$100k. **`total_premium_all_tiers = $11,876,368.54`**,
`highest_tier = "block"`.

| Tier | `buy_ratio` | derived `sell_ratio` | Buy vol | Sell vol | Premium | `trade_count` | Verdict |
|---|---|---|---|---|---|---|---|
| **mega** | 0.500 | 0.500 | 0 | 0 | $0 | **0** | ⚠️ **placeholder — no data** |
| **block** | **0.817** | 0.183 | 129,000 | 28,800 | $5,960,250 | **2** | ⚠️ **artifact — see below** |
| **large** | **0.555** | **0.445** | 87,974 | 70,581 | $5,916,118.54 | **36** | weakly buy-tilted |
| retail | 0.500 | 0.500 | 0 | 0 | $0 | **0** | ⚠️ placeholder — no data |

> `sell_ratio` is **derived as `1 − buy_ratio`** — the field does not exist
> (`lib/uw-json-paths.md` phantom-field trap #2).

**Three readings this table invites and one that survives:**

- ❌ *"Mega tier is balanced at 0.500."* **Wrong** — there is no mega tier.
  `trade_count = 0` and `total_premium = 0`; `0.5` is a default for an empty
  bucket. **No print all day reached $10M.** Any downstream phase citing
  `mega.buy_ratio = 0.5` as evidence of anything is citing a null.
- ❌ *"Block tier shows 81.7% buying — institutions are accumulating."* **Wrong** —
  `trade_count = 2`, and the two prints are the exact pair itemised above:
  `buy_volume = 129,000` **is** the closing cross, `sell_volume = 28,800` **is**
  the delta hedge. A closing auction is a mechanical print of aggregate MOC
  imbalance, not a directional institution; a delta hedge is the dealer's
  obligation, not a view. **The 0.817 measures nothing about intent.** It clears
  the rubric's ≥0.55 accumulation threshold on a technicality and must be rejected.
- ✅ *"Large tier, 36 trades, `buy_ratio = 0.555`."* This is the only tier with
  enough prints to mean anything. 0.555 sits in the rubric's **0.55–0.70
  "suggestive only"** band — at its very bottom edge. Net buy skew of
  87,974 − 70,581 = **17,393 shares = 0.014% of float**. Honest label:
  **essentially balanced, with a whisper of a buy tilt.**

**Independent aggressor check (DuckDB, all prints, `canceled=false`):**

| Date | Prints | Shares | Premium | `lift%` | `hit%` | % float |
|---|---|---|---|---|---|---|
| **2026-07-27** | 38 | **316,355** | $11.88M | **15.2** | **20.3** | 0.248% |
| 2026-07-24 | 45 | 257,781 | $9.65M | 21.9 | 11.3 | 0.202% |
| 2026-07-23 | 42 | 307,879 | $11.90M | 14.1 | 19.0 | 0.241% |
| 2026-07-22 | 42 | 219,594 | $8.81M | 37.5 | 5.0 | 0.172% |
| 2026-07-21 | 58 | 261,423 | $10.50M | 9.2 | 13.3 | 0.205% |
| 2026-07-20 | 69 | 281,730 | $11.25M | 4.1 | 16.4 | 0.220% |

`hit% > lift%` in **4 of 6 sessions**, including today. This is computed over
**all 38 prints**, not two, and it points the **opposite way** to the block-tier
headline. Where the two disagree, the 38-print measure wins.

Note also the DP tape is **shrinking in count** (69 → 58 → 42 → 42 → 45 → 38) while
premium holds ~$9–12M — fewer, larger prints. Consistent with phase-0.5's
"positioning already established, not being established today".

### Price levels

`uw dark-pool price-levels --symbol ENPH --days 5`,
`dates_covered = [2026-07-27, 07-24, 07-23, 07-22, 07-21]` — **anchored to the
as-of date**, matching phase-0's available-dates list (the sliding-window caveat
does not bite here). Spot = **$38.01**.

| Level | Premium | Shares | Trades | vs spot | Note |
|---|---|---|---|---|---|
| **38.01** | $5,354,568 | 140,873 | 5 | **0.0%** | ⚠️ = 07-27 **close** |
| 38.89 | $4,188,807 | 107,711 | 5 | +2.3% | ⚠️ = 07-23 **close** |
| **36.70** | $2,476,553 | 67,481 | **9** | −3.4% | ⚠️ = 07-24 **close** |
| 39.95 | $1,678,001 | 42,000 | 1 | +5.1% | single print |
| 39.96 | $1,197,851 | 29,980 | 1 | +5.1% | single print |
| **37.96** | $1,088,313 | 28,670 | 2 | −0.1% | genuine intraday |
| **37.10** | $1,048,126 | 28,251 | 3 | −2.4% | genuine intraday |
| 40.55 | $880,603 | 21,718 | 3 | +6.7% | genuine intraday |
| 39.94 | $850,922 | 21,305 | 2 | +5.1% | ⚠️ ≈ 07-21 close (39.94) |
| **37.42** | $834,451 | 22,300 | 2 | −1.6% | genuine intraday |
| 40.67 | $776,869 | 19,100 | 2 | +7.0% | genuine intraday |
| 38.03 | $773,620 | 20,342 | 4 | +0.1% | near close |
| 38.30 | $760,156 | 19,850 | 1 | +0.8% | single print |
| 38.62 | $691,273 | 17,900 | 3 | +1.6% | genuine intraday |
| 38.51 | $612,309 | 15,900 | 1 | +1.6% | single print |

> **Do not read this table as institutional support/resistance without stripping
> the closes.** Four of the top five levels (38.01, 38.89, 36.70, 39.94/39.95/39.96)
> are the **daily closing prints** of 07-27, 07-23, 07-24 and 07-21 respectively
> (closes from `phase-0.5-context.md`: 38.01, 36.70, 38.89, 39.58, 39.94). Closing
> auction crosses aggregate every MOC order in the market and carry **no
> directional information**. Ranking price levels by premium therefore just ranks
> the recent closes. This is a real limitation of the tool on a name whose DP tape
> is closing-cross-dominated.

**Levels that survive the filter** (multi-trade, not a closing print):

- **$37.96 / $38.03** — 6 trades, $1.86M straddling spot. Genuine two-way interest
  *at* current price. This is where the stock is being traded, not defended.
- **$37.10 – $37.42** — 5 trades, $1.88M. The **nearest genuine demand shelf**,
  ~1.6–2.4% below spot.
- **$40.55 / $40.67** — 5 trades, $1.66M. **Overhead supply**, ~6.7–7.0% above spot.
- **$36.70** deserves separate mention: **9 trades — the highest `trade_count` of
  any level** and $2.48M. Even discounting the 07-24 closing cross, it was touched
  repeatedly. It is both the recent swing low close and the most-transacted level
  in the window. **The most defensible reference low on this tape.**

### Extended-hours activity

`uw dark-pool extended-hours --symbol ENPH --top-n 15` → **4 prints, all within
5 seconds of each other**:

| Time (UTC) | Time (ET) | Price | Size | Premium |
|---|---|---|---|---|
| 20:00:30 | 16:00:30 | 38.01 | 129,000 | $4,903,290 |
| 20:00:25 | 16:00:25 | 38.01 | 3,245 | $123,342 |
| 20:00:25 | 16:00:25 | 38.01 | 2,893 | $109,963 |
| 20:00:25 | 16:00:25 | 38.01 | 2,871 | $109,127 |
| **Total** | | **38.01** | **138,009** | **$5,245,722** |

**This is not extended-hours institutional activity — it is the closing auction.**
All four print at exactly **$38.01, the closing price**, within a 5-second window
immediately after the 16:00 ET close. They are the tape's normal reporting of the
closing cross.

Per the phase's own pitfall — *"extended-hours prints can be index rebalancing or
ETF creation/redemption, not directional intent. Flag and de-rate conviction"* —
**conviction is de-rated accordingly**. There is **zero genuine pre- or post-market
institutional positioning on the eve of earnings**, which is itself notable: no one
is moving size ahead of tomorrow's print.

Cross-reference to phase-6: no overnight news attribution is needed, because there
is no overnight print to attribute.

### Answering phase-1's question: is there an offsetting block buy behind the deep-ITM puts?

Phase-1 asked whether the **$210,004 of deep-ITM put buying** (Oct-16 P60 Δ−0.789,
Dec-18 P55 Δ−0.646, Oct-16 P55 ×2 Δ−0.769) was a synthetic short or the long leg
of a conversion/reversal — which would require a **paired stock purchase**.

Implied delta if opened: roughly `(34×0.789 + 34×0.646 + 30×0.769) × 100` ≈
**7,183 shares** of short delta. The three prints cluster at **11:00 and 13:11 ET**.
No block of that size appears near either timestamp in the top-25 (the nearest,
9,650 sh at 11:52:53, is 40+ minutes away and printed **above** mid). At ~7.2k
shares the required hedge is below the resolution of the block tape anyway —
**this question cannot be settled by dark-pool data.** Recorded as unresolved
rather than resolved in either direction; **phase-3 OI is the better instrument.**

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` / SQL path | Rows used |
|---|---|---|
| `uw dark-pool largest --symbol ENPH --top-n 25 --sort-by premium --date 2026-07-27 --json` | top print `size=129000 price=38.01 premium=4903290 executed_at=20:00:30Z trade_vs_mid=0.07`; 2nd `size=28800 price=36.7 premium=1056960 executed_at=15:06:45Z trade_vs_mid=-0.52` ← `.results[]` | 25 |
| `uw dark-pool block-stratified --symbol ENPH --top-n 30 --min-tier large --date 2026-07-27 --json` | `highest_tier="block"`, `total_premium_all_tiers=11876368.54`; `block.buy_ratio=0.817` `block.trade_count=2` `block.buy_volume=129000` `block.sell_volume=28800`; `large.buy_ratio=0.555` `large.trade_count=36` `large.total_premium=5916118.54`; `mega.trade_count=0`; **`sell_ratio` derived = 1−buy_ratio** ← `.results[0].<tier>.*` | 1 |
| `uw dark-pool extended-hours --symbol ENPH --top-n 15 --date 2026-07-27 --json` | 4 rows, all `price=38.01`, `executed_at` 20:00:25–20:00:30Z; Σ size **=138,009**, Σ premium **=$5,245,722** ← `.results[]` | 4 |
| `uw dark-pool price-levels --symbol ENPH --top-n 15 --days 5 --json` | `dates_covered=["2026-07-27","2026-07-24","2026-07-23","2026-07-22","2026-07-21"]`; `38.01→$5,354,568/140,873/5`, `36.70→$2,476,553/67,481/9`, `37.96→$1,088,313/28,670/2`, `37.10→$1,048,126/28,251/3` ← `.results[]` | 15 |
| `uw dark-pool ticker-summary --top-n 30 --date 2026-07-27 --json` | ENPH **absent** ← `[.results[].ticker]\|index("ENPH")` → `outside_top30`; leaders MU $11.16B, SMH $10.48B, SPY $9.24B, SNDK $6.92B, QQQ $6.27B | top-30 |
| DuckDB `§B` ts-join on `dp-eod-report-2026-07-27.parquet`, ±5 min of 11:06:45 ET | **exactly 1 row**: `size=28800`, `price=36.70`, `aggressor='hit'`, `executed_at=2026-07-27 11:06:45.556-04:00` ← `CASE WHEN price<=nbbo_bid THEN 'hit'` | 1 |
| DuckDB `§A` daily DP aggregate, 6 sessions | 2026-07-27 `n=38 shares=316,355 prem=$11.88M lift%=15.2 hit%=20.3`; `hit%>lift%` in 4 of 6 ← `SUM(CASE WHEN price>=nbbo_ask …)` / `SUM(size)` | 6 days |

> Note: `nbbo_mid` does **not** exist in the dark-pool parquet (columns are
> `nbbo_bid`, `nbbo_ask`, `nbbo_bid_quantity`, `nbbo_ask_quantity`). The `§B`
> recipe's mid column was replaced with explicit bid/ask. The **CLI's** `largest`
> output does expose a computed `nbbo_mid` — the two sources differ in shape and
> must not be conflated.

## Tool errors

One error, surfaced verbatim, resolved:

```
_duckdb.BinderException: Binder Error: Referenced column "nbbo_mid" not found in FROM clause!
Candidate bindings: "nbbo_bid", "nbbo_bid_quantity", "nbbo_ask", "nbbo_ask_quantity", "volume"
LINE 2:  ROUND(nbbo_mid,3) mid,
```

**Cause:** `lib/duckdb-cuts.md §B`'s recipe selects `nbbo_mid`, which exists in the
`uw dark-pool largest` **CLI** payload but **not** in the underlying
`dp-eod-report-*.parquet`. **Fix:** re-ran selecting `nbbo_bid` / `nbbo_ask`
directly; the `aggressor` CASE expression in the recipe already used only bid/ask
and was unaffected. **No value was taken from the failed call** — the query
errored at bind time and returned no rows.

*Recommendation for the skill (propose-only, not applied):* `lib/duckdb-cuts.md §B`
should drop `nbbo_mid` from its SELECT list, or compute it as
`(nbbo_bid+nbbo_ask)/2`.

All `uw` CLI commands exited 0 and round-tripped through `jq`.

## DATA NOTE / CORRECTION

- **`sell_ratio` derived, not read** (`1 − buy_ratio`) — block 0.183, large 0.445.
  Field does not exist by design.
- **`mega.buy_ratio = 0.5` and `retail.buy_ratio = 0.5` are placeholders on empty
  buckets** (`trade_count = 0`, `total_premium = 0`), not measurements. Flagged
  explicitly so no downstream phase reads "balanced mega tier" into a null.
- **`§B` recipe corrected before use** (see Tool errors). The published 28,800 /
  `hit` / 11:06:45.556 values come from the **successful** re-run.
- **No number written here was published and then retracted.** The block-tier
  `buy_ratio = 0.817` is reported *as returned* and then argued against on grounds
  of `trade_count = 2`; the figure itself is correct, its interpretation is what
  this phase rejects.

## Verdict for downstream phases

- **Institutional bias:** **MIXED, leaning DISTRIBUTION** — and materially weaker
  than the raw `block.buy_ratio = 0.817` suggests. The only statistically
  meaningful tier (large, n=36) is `0.555` — bottom edge of "suggestive"; the
  38-print aggressor split runs the other way (`hit 20.3%` vs `lift 15.2%`, and
  `hit > lift` in 4 of 6 sessions). **Explicitly NOT the "accumulation" signature**
  in the phase-2 heuristics: that requires mega-tier `buy_ratio ≥ 0.55` (there is
  no mega tier) **and** price clusters **above** spot (the genuine clusters at
  $37.10–37.42 sit **below** spot; the above-spot levels at $38.89/$39.9x are
  closing crosses).
- **Conviction:** **2 / 5.** No mega tier; block tier mechanical; large tier
  near-balanced; DP only 10.2% of session volume; ENPH outside the top-30 by DP
  premium. Low signal content. Combined with `[CTX:] BUSY_NAME_NORMAL_DAY`, this
  phase contributes at most **`+`** (and on the *bearish* side) to phase-10
  confluence — never `++`.
- **Largest block as % of float:** **0.101%** (129,000 sh ÷ 127.77M). Whole-day DP
  volume **0.248%** of float. **This size is not meaningful for this name** — and
  the single block that reaches 0.1% is a closing auction cross, which is the least
  informative print type on the tape. Advisory, de-rating only.
- **Three S/R levels for phase-9** (closing-cross levels deliberately excluded):
  1. **$37.10 – $37.42** — nearest genuine demand shelf, 5 trades / $1.88M,
     ~1.6–2.4% below spot. First reference support.
  2. **$36.70** — 9 trades / $2.48M, the **most-transacted level in the window**
     and the recent swing-low close. Primary reference low / stop anchor.
  3. **$40.55 – $40.67** — 5 trades / $1.66M, ~6.7–7.0% above spot. Overhead
     supply / first upside target reference.
  ⚠️ **All three are inside tomorrow's 12.25% implied move (±$4.65 → $33.36–$42.66).
  Every one of these levels can be gapped through overnight.** Phase-9 must not
  build a stop on them without pricing event risk.
- **Three things later phases must remember:**
  1. **The 800-lot Nov-20 $35 put was BOUGHT** — 28,800-share `hit` at 11:06:45.556
     ET vs 27,608 shares of implied delta (96% match, sub-second). The largest
     option print of the day is **downside demand**, not noise. Confidence high,
     not certain; the reference-priced block and the n=1 window are the caveats.
  2. **`block.buy_ratio = 0.817` must never be cited as accumulation.** `n = 2`,
     both prints mechanical. The honest institutional read is the **large tier at
     0.555 on 36 trades** — essentially balanced.
  3. **There was no pre/post-market positioning at all on earnings eve** — the four
     "extended-hours" prints are the closing cross at $38.01. Nobody moved size
     ahead of the print, which corroborates phase-0.5's 16.4th-percentile option
     volume: **the market is not leaning into this event.**
- **Open questions:**
  - Does 2026-07-28 OI on **2026-11-20 P35 rise by ~800**? That would convert the
    delta-hedge inference from high-confidence to confirmed, and settle whether the
    position is opening or closing. → **phase-3** (`oi biggest-increases`)
  - Are the deep-ITM put buys ($210,004, ~7,183 shares of short delta) synthetic
    short or a conversion leg? **Dark pool cannot resolve this** — the hedge is
    below block resolution. → **phase-3 OI**
  - The DP print count is falling (69 → 38 over six sessions) on flat premium.
    Is that consolidation into fewer institutional hands, or simply thinner
    participation into a binary? → **phase-3 / phase-7c**
  - `$36.70` is simultaneously the most-transacted DP level, the prior close, and
    the price of the delta-hedge block. Is it a real shelf or just the reference
    price everything was benchmarked to today? → **phase-4** (`max-pain`, GEX)
