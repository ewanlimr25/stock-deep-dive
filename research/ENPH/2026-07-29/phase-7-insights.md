# Phase 7 — UW Insights Confluence

**Ticker:** ENPH
**As-of date:** 2026-07-29
**Generated:** 2026-07-30T02:52:00Z
**Upstream phases cited:** `phase-0-intake.md`, `phase-0.5-context.md`, `phase-1-flow.md`, `phase-2-dark-pool.md`, `phase-3-positioning.md`, `phase-4-structure.md`, `phase-5-historical.md`, `phase-6-macro.md`

## Summary

**UW's composite instrumentation independently returns DIRECTIONAL_SHORT and reproduces
phases 1–3 to the contract, while simultaneously capping the conviction.**
`conviction-matrix` gives `scenario` **DIRECTIONAL_SHORT** with
`explanation` *"Dark pool selling + put buying — institutional bear bet"* — but
**`confidence_pct` only 24**. `institutional-accumulation` returns
`signal` **"DISTRIBUTION — dark pool sell volume significantly exceeds buy volume"**.
`price-vs-flow` returns `divergence` **false** / *"Price and flow are aligned"* with
`flow_direction` bearish and `price_change_pct` **−30.22%**. Three composites, one direction.

**The validation is unusually clean and worth stating plainly.**
`conviction-matrix`'s `options_flow` block returns **`call_ask_volume` 8,285 /
`call_bid_volume` 8,284 / `put_ask_volume` 7,236 / `put_bid_volume` 4,613** — **exactly** the
whole-tape figures I derived by hand in `phase-1-flow.md` §B via the DuckDB escape hatch.
`deep-dive`'s `uw_dark_pool` returns `total_shares` **1,088,795** and `total_premium`
**$39,492,789.05** across `trade_count` **190** — **exactly** my `phase-2-dark-pool.md` §B
derivation (350,361 + 547,468 + 53,300 + 137,666 shares; 188 large + 2 block trades).
`signal-confluence` returns `volume_ratio` **1.18**, matching my `vol_x` **1.178**. **Four
hand-built escape-hatch cuts are confirmed by the vendor's own composites.**

**And the composite explains, in its own factor list, exactly why conviction must stay
moderate.** `signal-confluence --direction bearish` scores ENPH **3 of 6**, with factors
**`["bearish_flow", "dp_distribution", "oi_building_puts"]`** — precisely phases 1, 2 and 3.
The three factors that did **not** fire are `high_pcr`, `volume_spike` and
`high_iv_sell_premium`, and each absence matches an upstream finding: P/C 0.726 is sub-1.0,
`volume_ratio` 1.18 is far below a spike, and `iv_rank` 47.05 sits at ENPH's 15.6th self
percentile. **ENPH required `--top-n 500` to surface at all**, and its score of 3 is the
**lowest bucket present — shared with 348 of 500 names**. By the spec's own heuristic
(*"confluence ≥ 5 is rare and high-conviction"*), ENPH is not a high-conviction setup. For
scale: XLK, the technology sector ETF, scores **5**, and ETN scores **6**.

**One refinement this phase adds that no prior phase could:** `institutional-accumulation`
returns the dark-pool **`vwap` 36.27**, and it supplies the `shares` that
`phase-2-dark-pool.md`'s `price-levels` leaf returned as `null`. The 36.15–36.30 band I
identified there as "the genuine institutional shelf" **is the day's dark-pool VWAP**. ENPH
closed at **35.07 — $1.20 (3.3%) below the level at which the bulk of institutional volume
cleared.** That is a cleaner and stronger statement than "distribution inventory": the
marginal seller pushed price *below* the day's institutional clearing price into the close.

**Two data legs are unavailable and both matter for phase 7b/7c.** `deep-dive`'s
`yahoo_fundamentals` returns **`{"error":"yahoo quoteSummary ENPH: HTTP 401"}`**, and
`analyst-vs-flow` consequently returns **only an options-flow block with no analyst side at
all** — so **no analyst-vs-flow agreement test is possible this run**. `earnings-play`
correctly excludes ENPH (earnings 2026-10-27, ~90 days out — out of window, not an error).

## Key signals

- **`conviction-matrix` `scenario` DIRECTIONAL_SHORT**, `explanation` *"Dark pool selling +
  put buying — institutional bear bet"*, **`confidence_pct` 24** [INSIGHT:conviction_matrix]
- **`institutional-accumulation` `signal` "DISTRIBUTION"** — `buy_side_volume` 403,661 vs
  `sell_side_volume` 685,134, `buy_sell_ratio` **0.59** [INSIGHT:institutional_accumulation]
- **`signal-confluence` score 3 / 6**, factors `bearish_flow` + `dp_distribution` +
  `oi_building_puts`; **lowest bucket present, shared by 348 of 500 names**
  [INSIGHT:signal_confluence]
- **`price-vs-flow` `divergence` false — "Price and flow are aligned"**, `flow_direction`
  bearish, `price_change_pct` **−30.22%**, `period_low` **34.96** (set today)
  [INSIGHT:price_vs_flow]
- **Dark-pool `vwap` 36.27 vs close 35.07 — price closed 3.3% BELOW the institutional
  clearing price** [INSIGHT:institutional_accumulation]
- **`uw_dark_pool`: `total_premium` $39,492,789, `total_shares` 1,088,795, `trade_count` 190**
  — exact match to my phase-2 hand derivation [INSIGHT:deep_dive]
- **`conviction-matrix.options_flow` = my phase-1 DuckDB ask/bid split exactly**
  (8,285 / 8,284 / 7,236 / 4,613) [INSIGHT:conviction_matrix]
- **`yahoo_fundamentals` HTTP 401** → no Yahoo fundamentals; **`analyst-vs-flow` returns no
  analyst leg** [INSIGHT:deep_dive / INSIGHT:analyst_vs_flow]
- **`uw_top_oi_changes` top row = `ENPH280121P00030000` +2,000 @ $8.97, `dte` 541** — the
  composite agrees the Jan-2028 P30 is the chain's dominant change [INSIGHT:deep_dive]
- **`earnings-play`: ENPH absent — out of window** (next earnings 2026-10-27)
  [INSIGHT:earnings_play]

## Detailed findings

### A — Deep-dive snapshot

`uw insights deep-dive --symbol ENPH --date 2026-07-29` returns four blocks:
`uw_screener`, `uw_dark_pool`, `uw_top_oi_changes`, `yahoo_fundamentals`.

**`uw_screener` — whole-tape directional aggregates** (the figures phase 9 sizes against):

| Field | Value |
|---|---|
| `call_premium` | $2,888,189 |
| `put_premium` | $2,370,262 |
| **Total premium** | **$5,258,451** |
| `bullish_premium` | $2,153,830 |
| `bearish_premium` | $2,633,643 |
| **`net_flow` (derived `bullish − bearish`)** | **−$479,813** |
| `call_volume` / `put_volume` | 18,150 / 13,176 |
| `put_call_ratio` | 0.7259 |
| `iv_rank` | 47.0523 |
| `iv30d` | 0.796977 |
| **`implied_move` / `implied_move_perc`** | **1.96197 / 5.5849%** |
| `total_open_interest` | 381,215 |
| `next_earnings_date` | **2026-10-27** |
| `volatility` | 1.11403 |

`net_flow` is **derived** — the block carries no `net_flow` key
(`lib/uw-json-paths.md` phantom-field trap). **Reconciliation:** identical to
`phase-1-flow.md` §A and `phase-0.5-context.md` to the dollar, and independently confirmed by
`price-vs-flow`'s own `net_premium_flow` **−479,813** and `signal-confluence`'s `net_flow`
**−479,813** (§B, §D). Four leaves, one value.

Against `phase-0.5-context.md`'s `[CTX:]` rank: total premium is the **93.8th universe
percentile** but the **26.6th self percentile**; `net_flow` is **outside the top-50 both
directions** (bearish rank-50 cutoff −$2,762,256). **`implied_move_perc` 5.5849%** is the
figure phase 9 must size structures to (N4) — down from ±12.25% pre-print.

**`uw_dark_pool`:**

| Field | Value |
|---|---|
| `total_premium` | **$39,492,789.05** |
| `total_shares` | **1,088,795** |
| `trade_count` | **190** |
| `avg_price` | 36.39 |

**Exact agreement with `phase-2-dark-pool.md` §B**, where I summed the four tiers by hand
(large 350,361 + 547,468; block 53,300 + 137,666 = 1,088,795 shares) and counted 188 + 2 =
190 trades. That derivation is now vendor-confirmed. Context: 1,088,795 shares = **12.6% of
the day's 8,670,939 share volume** and **0.852% of the 127.77M float**.

**`uw_top_oi_changes`** — the same five contracts as `phase-3-positioning.md` §C:

| `option_symbol` | Parsed | `dte` | `oi_diff_plain` | `avg_price` | Volume |
|---|---|---|---|---|---|
| **`ENPH280121P00030000`** | 2028-01-21 P30 | **541** | **+2,000** | **$8.97** | 3,162 |
| `ENPH260918C00070000` | 2026-09-18 C70 | 51 | +1,604 | $0.29 | 1,935 |
| `ENPH260918P00035000` | 2026-09-18 P35 | 51 | +885 | $4.13 | 1,048 |
| `ENPH260731C00045000` | 2026-07-31 C45 | 2 | +808 | $0.34 | 2,130 |
| `ENPH260731P00032000` | 2026-07-31 P32 | 2 | +598 | $0.65 | 735 |

The composite ranks the **Jan-2028 P30 first**, agreeing with phase 3 that this is the
chain's dominant positioning change.

**`yahoo_fundamentals`: `{"error":"yahoo quoteSummary ENPH: HTTP 401"}`** — surfaced verbatim
per orchestration rule 3. **No PE, market cap, short %, or fundamental ratios are available
from this leaf.** The spec's snapshot section asks for those; they must come from `fz` and
Finnhub in phase 7b instead. Substitutes already on file: `Market Cap` **$4.62B** / `Float`
127.77M / `Short Float` **17.94%** (`fz`, `phase-0-intake.md`), `marketcap`
**$4,799,493,615** (screener parquet, `phase-0.5-context.md`).

### B — Signal confluence

`uw insights signal-confluence --direction bearish --min-score 1 --top-n 20` → **ENPH
absent**. Per the spec's guidance I confirmed with `--min-score 1`; still absent. Widening to
**`--top-n 500`** surfaced it — the omission was a **ranking** cutoff, not a score cutoff:

| Field | Value |
|---|---|
| `ticker` | ENPH |
| **`score`** | **3** (of 6) |
| **`factors`** | **`["bearish_flow", "dp_distribution", "oi_building_puts"]`** |
| `close` | 35.07 |
| `net_flow` | −479,813 |
| `put_call_ratio` | 0.7259 |
| `iv_rank` | 47.0523 |
| **`volume_ratio`** | **1.18** |
| `sector` | Technology |

`uw insights signal-confluence --direction bullish --min-score 1 --top-n 20` → **ENPH
absent** (leaders: TEVA, BIPC, MBIN, ECHO, IAU, MMM, CZR, HYMC, TECH, SMTC, CRBG, SNN, ZGN,
LBRT, SSD, SHAZ, SOFI, ALLO, BKLN, CAG).

**Score distribution across the 500 returned bearish names:**

| Score | Count |
|---|---|
| **3** | **348** ← ENPH |
| 4 | 139 |
| 5 | 12 |
| 6 | 1 |

**This is the most useful calibration datapoint in the phase.** ENPH's score of 3 is the
**minimum score present in the entire returned set** and is shared with **348 of 500 names
(70%)**. The spec's heuristic — *"signal confluence ≥ 5 is rare and high-conviction"* — puts
ENPH firmly outside that. Only 13 of 500 names reached ≥5.

**The three factors that fired map one-to-one onto my upstream phases:**

| Factor | Upstream confirmation |
|---|---|
| `bearish_flow` | `phase-1-flow.md` — `net_flow` −$479,813; whole-tape puts bought 1.569× |
| `dp_distribution` | `phase-2-dark-pool.md` — large-tier `sell_ratio` 0.610 on 188 trades |
| `oi_building_puts` | `phase-3-positioning.md` — 5.4:1 premium-weighted bearish OI builds |

**The three that did NOT fire are equally informative, and each corroborates an upstream
caveat:**

| Missing factor | Why it didn't fire | Upstream agreement |
|---|---|---|
| `high_pcr` | `put_call_ratio` **0.7259** — below 1.0 | `phase-5-historical.md` §D: `pc-ratio-zscore` +0.482, `extreme` NORMAL |
| `volume_spike` | **`volume_ratio` 1.18** — nowhere near a spike | `phase-0.5-context.md`: `vol_x` **1.178**, BUSY_NAME_NORMAL_DAY |
| `high_iv_sell_premium` | `iv_rank` **47.05** — too low to sell premium | `phase-0.5-context.md`: iv_rank at ENPH's **15.6th self percentile** |

**Benchmark within the sector:** **XLK — the Technology sector ETF — scores 5** on bearish
confluence (`bearish_flow`, `high_pcr`, `dp_distribution`, `oi_building_puts`,
`high_iv_sell_premium`), as do ADP, ADI and BUD; **ETN scores 6**. So the *sector ETF* carries
a stronger bearish confluence signature than ENPH does. Read with `phase-6-macro.md` §H
(Technology sector *flow* is INFLOW at persistence 1.0 while Technology *price* fell −2.49%),
this is coherent: the mega-cap premium inflow and the sector-ETF bearish confluence are two
sides of the same narrow tape — index-level hedging alongside single-name mega-cap buying.

### C — Conviction matrix

`uw insights conviction-matrix --symbol ENPH --date 2026-07-29`:

| Field | Value |
|---|---|
| **`scenario`** | **DIRECTIONAL_SHORT** |
| **`confidence_pct`** | **24** |
| **`explanation`** | **"Dark pool selling + put buying — institutional bear bet."** |
| `thresholds` | `{"bear": 0.4, "bull": 0.6}` |
| `dark_pool.buy_ratio` | **0.371** |
| `dark_pool.buy_volume` / `sell_volume` | 403,661 / 685,134 |
| `dark_pool.trades` | 190 |
| `options_flow.call_ask_volume` / `call_bid_volume` | **8,285 / 8,284** |
| `options_flow.put_ask_volume` / `put_bid_volume` | **7,236 / 4,613** |

**The scenario is the most directly bearish label this instrumentation produces** — not
HEDGED_LONG (which per the spec would mean bullish flow + bearish dark pool, i.e. protection
buying), not MIXED, but **DIRECTIONAL_SHORT with an explicit "institutional bear bet"
explanation**. Both of its inputs cleared the `bear: 0.4` threshold: `dark_pool.buy_ratio`
0.371 < 0.40, and the put ask/bid ratio 7,236 / 4,613 = 1.569 against calls at 1.000.

**`confidence_pct` 24 is the essential counterweight and phase 9 must carry it.** The tool
identifies the direction with a low-confidence flag, which is exactly the shape of this entire
run: **direction well-corroborated across five lanes, magnitude trivial** (`net_flow`
−$479,813 = 5.8× below the day's bearish top-50 cutoff; `phase-2-dark-pool.md` absent from
the dark-pool top-30 against a $1.043B cutoff; `signal-confluence` 3/6 in the bottom bucket).

> **Two reconciliations, so phase 10 does not score these as contradictions:**
>
> 1. **`dark_pool.buy_ratio` 0.371 vs `phase-2-dark-pool.md`'s 0.390 (large tier) and 0.303
>    (auction-stripped).** The composite's 0.371 is the **all-tier aggregate and it INCLUDES
>    the closing-auction print**: 403,661 = 350,361 (large buy) + 53,300 (block buy);
>    685,134 = 547,468 (large sell) + 137,666 (**the 20:00:06 UTC auction cross**).
>    **The composite does not strip the auction artifact** flagged in
>    `memory/darkpool-closing-auction-artifact.md`. My phase-2 figures bracket it:
>    auction-stripped **0.303 buy** ≤ composite **0.371** ≤ large-tier **0.390**.
>    **All three are on the same side of the 0.40 bear threshold**, so the DIRECTIONAL_SHORT
>    classification survives the correction — but a caller quoting 0.371 as a clean
>    intraday institutional ratio would be quoting an artifact-inflated number.
> 2. **`options_flow` here = my `phase-1-flow.md` §B DuckDB cut, digit for digit**
>    (8,285 / 8,284 / 7,236 / 4,613). That cut was flagged there as an escape-hatch
>    derivation because the CLI exposes ask/bid only per-contract in `sweeps`. **It is now
>    vendor-confirmed** — the composite computes the same whole-tape split internally. This
>    materially raises confidence in phase 1's load-bearing evidence.

### D — Price vs flow

`uw insights price-vs-flow --symbol ENPH --lookback-days 30`:

| Field | Value |
|---|---|
| **`divergence`** | **false** |
| **`divergence_signal`** | **"Price and flow are aligned"** |
| `flow_direction` | **bearish** |
| `net_premium_flow` | −479,813 |
| `bullish_premium` / `bearish_premium` | 2,153,830 / 2,633,643 |
| `put_call_ratio` | 0.7259 |
| `iv_rank` | 47.0523 |
| `price_start` → `price_end` | **50.26 → 35.07** |
| **`price_change_pct`** | **−30.22%** |
| `period_high` / `period_low` | 55.19 / **34.96** |

**No divergence — and that is a trend-continuation reading, not a reversal one.** Per the
spec's heuristic, a divergence (bearish flow + *rising* price, or bullish flow + *falling*
price) is the leading reversal signal. **Neither is present:** flow is bearish and price is
down 30.22%. The reversal setup that would argue for a contrarian long **does not exist** in
this instrumentation.

Two details worth carrying:
- **`period_low` 34.96 was set today** (`phase-1-flow.md` §C session low). ENPH closed
  **$0.11 above the 30-day low**, with `period_high` 55.19 — the stock is at the bottom of its
  entire 30-session range.
- `price_change_pct` **−30.22%** matches `phase-5-historical.md`'s `trend` `price_change`
  (50.26 → 35.07, −30.2%) exactly, and `institutional-accumulation`'s
  `price_30d_change_pct` −30.22% (§E). Three leaves agree.

### E — Institutional accumulation

`uw insights institutional-accumulation --symbol ENPH`:

| Field | Value |
|---|---|
| **`signal`** | **"DISTRIBUTION — dark pool sell volume significantly exceeds buy volume"** |
| `buy_side_volume` | 403,661 |
| `sell_side_volume` | **685,134** |
| **`buy_sell_ratio`** | **0.59** |
| `dark_pool_trades` | 190 |
| `total_dp_premium` | $39,492,789.05 |
| `total_dp_volume` | 1,088,795 |
| **`vwap`** | **36.27** |
| `avg_trade_price` | 36.39 |
| `price_30d_change_pct` | −30.22% |

`top_price_levels`:

| Price | Shares | Premium | Trades |
|---|---|---|---|
| **35.07** | **168,497** | $5,909,197 | 6 |
| 37.48 | 57,800 | $2,166,344 | 2 |
| **36.27** | 31,263 | $1,133,834 | 6 |
| 36.70 | 30,100 | $1,104,535 | 2 |
| 36.07 | 26,835 | $967,938 | 1 |

**Verbatim DISTRIBUTION — the third composite pointing the same way**, and it agrees with
`phase-2-dark-pool.md`'s independent verdict.

> **Note `buy_sell_ratio` 0.59 is a RATIO, not a fraction** — 403,661 / 685,134 = 0.589. It is
> **not** comparable to `conviction-matrix`'s `dark_pool.buy_ratio` 0.371, which is
> buy / (buy + sell). Both describe the same underlying volumes. A phase quoting "0.59" as a
> buy *fraction* would materially understate the selling.

**Two genuinely new contributions:**

**(1) It supplies the `shares` that `price-levels` returned as `null`.**
`phase-2-dark-pool.md` §D flagged `total_shares` = `null` across all 15 rows of the
`price-levels` leaf, forcing interpretation onto premium and trade count alone. This leaf
fills the gap: **35.07 → 168,497 shares**, 37.48 → 57,800, 36.27 → 31,263, 36.70 → 30,100,
36.07 → 26,835. The 35.07 figure confirms the auction cluster's scale (phase 2 §C identified
151,595 shares crossing at 35.07 in the 20:00:01–20:00:15 UTC window; 168,497 total at that
level across 6 trades is consistent once the 20:07 print is included).

**(2) `vwap` 36.27 reframes phase 2's "institutional shelf" — this is the phase's best new
insight.** `phase-2-dark-pool.md` §D identified **36.15–36.30** as the genuine non-artifact
institutional cluster ($9,246,618 across 38 trades) and labelled it "distribution inventory,
now overhead supply." The dark-pool **`vwap` is 36.27 — dead centre of that band.**

**The band is not merely a cluster; it is where the day's institutional volume actually
cleared.** ENPH closed at **35.07, i.e. $1.20 / 3.3% BELOW its own dark-pool VWAP**, and
$1.32 below `avg_trade_price` 36.39. That is a stronger statement than phase 2 could make:
the marginal seller drove price below the level at which the bulk of institutional size
transacted, into the close, finishing $0.11 off the session low. Read with
`phase-2-dark-pool.md` §A — the gap was **bought** above mid at a VWAP of $37.56 in the first
eleven minutes, then 15 consecutive below-mid blocks laddered to 35.01 — the sequence is
unambiguous: **buyers early and high, sellers persistently and lower, close below everyone's
average.**

**Phase 9 implication:** **36.27 is a better-founded resistance reference than the 36.15–36.30
band midpoint guessed at in phase 2**, because it is a volume-weighted clearing price rather
than a premium-ranked cluster. It also sits just below the **36–37 gamma flip band**
(`phase-4-structure.md` §A/§G) and just below the **36 max-pain magnet** — three independent
methods converging on **36–36.3 as the pivot ENPH must reclaim.**

### F — Analyst vs flow

`uw insights analyst-vs-flow --symbol ENPH` returned **only an `options_flow` block**:

| Field | Value |
|---|---|
| `options_flow.flow_sentiment` | **bearish** |
| `options_flow.net_flow` | −479,813 |
| `options_flow.bullish_premium` / `bearish_premium` | 2,153,830 / 2,633,643 |
| `options_flow.put_call_ratio` | 0.7259 |
| **Analyst consensus block** | **ABSENT** |

**The tool's entire purpose — comparing Wall Street consensus against the options tape — could
not be served.** No `analyst_consensus`, `recommendation`, `target_price` or `agreement` field
was returned. The cause is almost certainly the same upstream failure as `deep-dive`'s
`yahoo_fundamentals` (**HTTP 401**): the spec notes this leaf's consensus is sourced from
yfinance, and yfinance is returning 401 for ENPH this run.

**Consequence: no analyst-vs-flow agreement test exists for this run.** Recorded in
`## Tool errors`. **Phase 7b must source analyst consensus and price targets from Finnhub**,
noting that `fz quote`'s `Recom` / `Target Price` fields are **also unavailable** because
`fz quote` is degraded to 14/84 fields (`phase-0-intake.md`). If Finnhub also fails, the
analyst leg is unmeasured for the run and phases 8/8b/9 must treat it as such rather than as
neutral.

### G — Earnings play

`uw insights earnings-play --days-until-earnings 30` returned **10 results; ENPH absent**
(null-safe select → `null`).

**Correctly out of window, not an error** — per the spec's pitfall note. `next_earnings_date`
is **2026-10-27** (§A), roughly **90 calendar days** out, well beyond the 30-day filter. ENPH
reported **2026-07-28** (`phase-6-macro.md` §G: revenue $291.9M beat, EPS $0.47 beat, Q3 guide
$290–320M).

**The structural consequence is one of the most important facts for phase 9:** ENPH has **no
company-specific catalyst for ~13 weeks**. This is why `iv-term-structure` is **flat at
82–87% beyond `dte` 23** (`phase-4-structure.md` §D), why `iv_rank` sits at the **15.6th self
percentile**, and why any thesis here must be carried by **rates and solar-sector beta
(ρ 0.846 to TAN, `phase-6-macro.md` §I)** rather than by anything ENPH can announce.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw insights deep-dive --symbol ENPH --date 2026-07-29 --json` | `uw_dark_pool.total_premium`=**39492789.0521**, `.total_shares`=**1088795**, `.trade_count`=**190**, `.avg_price`=36.3917; `uw_screener.bullish_premium`=2153830 / `.bearish_premium`=2633643 → `net_flow`=**−479813** (derived); `implied_move_perc`=0.055849; `next_earnings_date`=2026-10-27; `uw_top_oi_changes[0].option_symbol`=ENPH280121P00030000 / `oi_diff_plain`=2000 / `avg_price`=8.9744; **`yahoo_fundamentals.error`="yahoo quoteSummary ENPH: HTTP 401"** | 4 blocks |
| `uw insights signal-confluence --direction bearish --min-score 1 --top-n 20 --date 2026-07-29 --json` | ENPH **absent** ← `[.results[]\|select(.ticker=="ENPH")]\|.[0]//null` → `null`; leaders ETN score=6, ADP/XLK/ADI/BUD score=5 | top-20 |
| `uw insights signal-confluence --direction bearish --min-score 1 --top-n 500 --date 2026-07-29 --json` | ENPH `score`=**3**, `factors`=`["bearish_flow","dp_distribution","oi_building_puts"]`, `volume_ratio`=**1.18**, `close`=35.07 ← same select; distribution score3=**348** / score4=139 / score5=12 / score6=1 ← `[.results[].score]\|group_by(.)`; `min`=3 | top-500 |
| `uw insights signal-confluence --direction bullish --min-score 1 --top-n 20 --date 2026-07-29 --json` | ENPH **absent**; leaders TEVA, BIPC, MBIN, ECHO, IAU… | top-20 |
| `uw insights conviction-matrix --symbol ENPH --date 2026-07-29 --json` | `scenario`=**DIRECTIONAL_SHORT**, `confidence_pct`=**24**, `explanation`="Dark pool selling + put buying — institutional bear bet."; `dark_pool.buy_ratio`=**0.371** (buy 403661 / sell 685134); `options_flow`=**8285/8284/7236/4613**; `thresholds`={bear:0.4,bull:0.6} | 1 |
| `uw insights price-vs-flow --symbol ENPH --lookback-days 30 --json` | `divergence`=**false**, `divergence_signal`="Price and flow are aligned", `flow_direction`=bearish, `price_change_pct`=**−30.22**, `price_start`=50.26 → `price_end`=35.07, `period_high`=55.19, `period_low`=**34.96**, `net_premium_flow`=−479813 | 1 |
| `uw insights analyst-vs-flow --symbol ENPH --json` | `options_flow.flow_sentiment`=bearish, `net_flow`=−479813; **no analyst block returned** ← `keys` = `["options_flow","symbol"]` only | 1 (degraded) |
| `uw insights institutional-accumulation --symbol ENPH --json` | `signal`=**"DISTRIBUTION — dark pool sell volume significantly exceeds buy volume"**, `buy_sell_ratio`=**0.59**, `buy_side_volume`=403661, `sell_side_volume`=685134, **`vwap`=36.27**, `avg_trade_price`=36.39, `price_30d_change_pct`=−30.22; `top_price_levels[0]`={price:35.07, **shares:168497**, premium:5909197.29, trades:6} | 1 + 5 levels |
| `uw insights earnings-play --days-until-earnings 30 --json` | 10 results, ENPH **absent** ← null-safe select → `null` (out of window) | top-10 |

All nine `uw insights` reads were captured to a file before being queried and every value
round-tripped through `jq` on validated JSON; all market-wide leaves used the null-safe
`[…]|.[0]//null` form per `memory/batched-stdout-swallow.md`. One value is **derived**:
`net_flow` = `bullish_premium − bearish_premium` (§A), cross-validated against three other
leaves that return it directly (−479,813 in `price-vs-flow`, `signal-confluence`,
`analyst-vs-flow`).

## Tool errors

No invocation failures — all nine `uw insights` calls returned exit 0 with parseable JSON.
**Three degradations, two of them material:**

1. **`deep-dive` → `yahoo_fundamentals`: `{"error":"yahoo quoteSummary ENPH: HTTP 401"}`**
   (surfaced verbatim per orchestration rule 3). **No PE, market cap, short %, book value or
   fundamental ratios are available from this leaf**, so the spec's requested deep-dive
   snapshot is partial. Substitutes on file: `Market Cap` **$4.62B**, `Float` 127.77M,
   `Short Float` **17.94%** (`fz`, `phase-0-intake.md`); `marketcap` **$4,799,493,615**
   (screener parquet). Phase 7b must not rely on this leaf. Free-source failure, not a paid
   endpoint — no `tier_adjustment=NA` is warranted yet.
2. **`analyst-vs-flow` returned no analyst leg** — top-level keys are only
   `["options_flow","symbol"]`. **The tool's comparison purpose is unserved and no
   analyst-vs-flow agreement can be reported this run.** Same probable root cause as (1)
   (yfinance 401). Compounding constraint: `fz quote`'s `Recom` / `Target Price` are **also**
   unavailable (`fz quote` degraded to 14/84 fields, `phase-0-intake.md`). **Phase 7b must
   attempt Finnhub for consensus/targets; if that also fails, the analyst leg is UNMEASURED
   for this run** and must be reported as such, not as neutral.
3. **`signal-confluence` required `--top-n 500` to surface ENPH.** At `--top-n 20` with
   `--min-score 1` ENPH was absent, which the spec's guidance would read as "score below
   min-score." That inference would have been **wrong** — ENPH scores **3**, and the omission
   was purely a **ranking** cutoff. **Note for the phase spec (propose-only):** the
   `--min-score 1` confirmation step is insufficient on a 500+ name tape; `--top-n` must also
   be widened before concluding a symbol has no confluence score.

Not errors, recorded for completeness:
- **`earnings-play` correctly excludes ENPH** (earnings 90 days out) — the spec explicitly
  notes this is "out of window," not a failure.
- **`conviction-matrix`'s `dark_pool.buy_ratio` 0.371 includes the closing-auction print**
  and is therefore artifact-inflated (§C). The classification is unaffected.
- **`institutional-accumulation`'s `buy_sell_ratio` 0.59 is buy/sell, not
  buy/(buy+sell)** — not comparable to 0.371 (§E).

## Cross-check vs phases 1–6

| UW insight | Value | Phase agreement? | Notes |
|---|---|---|---|
| `signal_confluence` score/factors | **3/6** — `bearish_flow`, `dp_distribution`, `oi_building_puts` | **phases 1, 2, 3 AGREE — one-to-one** | Each fired factor maps to exactly one upstream phase verdict. The three *unfired* factors (`high_pcr`, `volume_spike`, `high_iv_sell_premium`) each match an upstream caveat: P/C 0.726, `vol_x` 1.178, `iv_rank` 47.05 at the 15.6th self pctile. **Score 3 = lowest bucket, 348/500 names** → confirms phase 0.5's BUSY_NAME_NORMAL_DAY cap |
| `conviction_matrix` scenario | **DIRECTIONAL_SHORT**, `confidence_pct` **24** | **phase 2 (DP) AGREES; phase 1 AGREES** | `options_flow` block = phase-1's DuckDB whole-tape split **digit for digit** (8,285/8,284/7,236/4,613) — vendor-confirms an escape-hatch cut. `dark_pool.buy_ratio` 0.371 includes the auction; phase-2's auction-stripped 0.303 and large-tier 0.390 bracket it, **all on the bear side of the 0.40 threshold** |
| `institutional_accumulation` | **DISTRIBUTION**, `buy_sell_ratio` 0.59, `vwap` **36.27** | **phase 2 (DP) AGREES** | Same verdict, reached independently. **Adds** the `shares` phase 2's `price-levels` returned as null, and reveals the 36.15–36.30 "shelf" **is the dark-pool VWAP (36.27)** — close 35.07 is **3.3% below** it |
| `price_vs_flow` | **`divergence` false** — aligned, bearish, −30.22% | **phase 5 AGREES** | `price_change_pct` −30.22% matches `trend`'s 50.26 → 35.07 exactly. **No reversal signal exists** → removes the contrarian-long case from this instrumentation |
| `deep_dive.uw_dark_pool` | $39,492,789 / 1,088,795 sh / 190 trades | **phase 2 AGREES exactly** | Vendor-confirms my hand-summed four-tier derivation |
| `deep_dive.uw_top_oi_changes` | Jan-2028 P30 +2,000 @ $8.97 ranked #1 | **phase 3 AGREES** | Same 5 contracts, same ordering |
| `deep_dive.uw_screener` | `net_flow` −$479,813; `implied_move_perc` 5.5849% | **phases 0.5 and 1 AGREE** | Four leaves now return −479,813 |
| `analyst_vs_flow` | **analyst leg ABSENT** | **cannot test** | yfinance 401. Unmeasured, not neutral → phase 7b |
| `earnings_play` | ENPH absent (out of window) | **phase 6 AGREES** | Earnings 2026-10-27, ~90d; explains the flat 82–87% vol curve |
| — | vs **phase 4** (structure) | **not directly tested** | The composites carry no gamma/dealer inputs. Phase 4's short-gamma read and phase 6's VIX finding are **independent of** and unchallenged by this phase |
| — | vs **phase 6** (macro) | **one genuine tension** | `phase-6-macro.md` §H: Technology sector *flow* is INFLOW, `persistence_score` **1.0** — the one adverse reading. Here **XLK itself scores 5/6 on bearish confluence**. Coherent rather than contradictory: index-level bearish hedging alongside mega-cap single-name buying, in a sector whose price fell −2.49% with 34.4% breadth |

**No internal contradiction found between this phase and phases 1–5.** The single tension in
the run remains phase 6's adverse sector-rotation gate, and phase 7's XLK datapoint arguably
softens even that. Two apparent discrepancies were traced to metric definitions rather than
disagreement (`buy_ratio` 0.371 vs 0.390/0.303 → auction inclusion; `buy_sell_ratio` 0.59 →
ratio not fraction) and are documented so phase 10 does not double-count them.

## Verdict for downstream phases

- **UW composite bias: BEARISH — `DIRECTIONAL_SHORT`, explicitly "institutional bear bet",
  at `confidence_pct` 24.** Three independent composites (`conviction-matrix`,
  `institutional-accumulation`, `price-vs-flow`) point the same way, with **no divergence
  signal** and therefore **no reversal setup** in this instrumentation.
- **Conviction: 3 / 5.** The direction is as well-corroborated as this skill's
  instrumentation can make it — and the *same instrumentation* caps the conviction three
  separate ways: **`confidence_pct` 24**; **`signal-confluence` 3 of 6**, the **lowest score
  bucket, shared with 348 of 500 names** and requiring `--top-n 500` to surface at all; and
  three of six bearish factors failing to fire (`high_pcr`, `volume_spike`,
  `high_iv_sell_premium`). Phases 1–2 remain **capped at `+`** per
  `phase-0.5-context.md`. The 3 is not a hedge — it is the composite's own arithmetic:
  **a clear direction on a name that clears no intensity threshold.**
- **Phase 9 should treat this as the BASELINE — a low-confidence directional short — and
  override only with specific contrary evidence.** The contrary evidence that actually exists
  and must be weighed, not waved past:
  1. **`phase-6-macro.md`'s adverse sector-rotation gate** — Technology `trend` INFLOW,
     `persistence_score` **1.0** (though decaying 71% and mega-cap concentrated).
  2. **`phase-4-structure.md`'s max-pain pull to 36** (08-07, +2.68%) and residual
     `net_vanna` **+1,327** — noting `phase-6-macro.md` established the vanna trigger
     (a VIX collapse) is **not met**, VIX having risen 13.5% to 20.66.
  3. **`phase-6-macro.md`'s Q2 beat** — revenue $291.9M and EPS $0.47 both beat, Q3 guide
     **above** the carried range, Europe +35%. The fundamentals were not the problem.
  4. **`phase-5-historical.md`'s `RSI` 31.60** and price **−30.49% below SMA50** — a fresh
     short is being initiated into an extended, near-oversold tape at the very bottom of the
     30-day range (`period_low` 34.96 set today).
- **Levels this phase contributes or sharpens:**
  - **36.27 — dark-pool `vwap`** and the true identity of phase 2's 36.15–36.30 "shelf".
    Close 35.07 is **3.3% below** it. Better-founded as resistance than the band midpoint,
    and it converges with phase 4's **36–37 gamma flip band** and **36 max-pain magnet** →
    **36–36.3 is the pivot ENPH must reclaim** to invalidate the bearish structure.
  - **37.48 — 57,800 shares / $2,166,344 across 2 trades** (`top_price_levels`), matching
    phase 2's trapped-buyer zone (76,300 shares bought above mid at a VWAP of $37.56).
  - **34.96 — `period_low`, set today**; close 35.07 is $0.11 above the 30-day low.
- **Open questions:**
  - **Can analyst consensus and price targets be sourced at all?** `analyst-vs-flow`'s
    analyst leg is absent (yfinance 401), `deep-dive`'s `yahoo_fundamentals` is 401, and
    `fz quote`'s `Recom`/`Target Price` are null (degraded leaf). **Finnhub is the last
    remaining route.** If it fails, phases 8/8b/9 must treat the analyst leg as
    **unmeasured, not neutral**. (→ 7b)
  - **Does `confidence_pct` 24 on a DIRECTIONAL_SHORT justify a position at all, or only a
    bias?** With `signal-confluence` at 3/6 in the bottom bucket, `phase-6-macro.md`'s
    `regime` guidance of *"Half position sizes. Favor defined-risk strategies"*, and the
    adverse rotation gate, the honest reading may be **defined-risk expression or no
    position** rather than a directional short. (→ 8b, 9)
  - **Why did the marginal seller push price 3.3% below the dark-pool VWAP of 36.27 into the
    close?** Forced liquidation, index/ETF-related selling (ρ 0.846 to TAN), or genuine
    conviction? A repeat below 35 on 07-30 would distinguish them. (→ 8, 9)
  - **XLK scores 5/6 bearish while Technology sector flow is a persistent INFLOW.** Is the
    index-level bearish confluence the hedge *against* the mega-cap longs, and does that
    make the sector-rotation gate less adverse than its `persistence_score` 1.0 implies?
    (→ 8b, 9)
