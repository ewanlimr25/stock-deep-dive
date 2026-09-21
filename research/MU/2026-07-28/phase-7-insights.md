# Phase 7 — UW Insights Confluence

**Ticker:** MU
**As-of date:** 2026-07-28
**Generated:** 2026-07-28T22:32:00-04:00
**Upstream phases cited:** `phase-0.5-context.md`, `phase-1-flow.md`, `phase-2-dark-pool.md`, `phase-3-positioning.md`, `phase-4-structure.md`, `phase-5-historical.md`, `phase-6-macro.md`

## Summary

**The UW composite layer reads MU as mildly BULLISH — and this phase's central finding is that
every one of its bullish inputs dissolves under the decompositions already performed in phases
1–4.** `signal-confluence` scores MU **3 of 6 bullish** on the factors
**`["bullish_flow","dp_accumulation","oi_building"]`**, and MU appears **nowhere in the 500-row
bearish list**. But phase-1 established that `bullish_flow` is UW's *ask-calls + bid-puts*
definition in which **bid-puts ($784.17M) is the larger half and calls were net SOLD (-$45.76M)**;
phase-2 established that `dp_accumulation` rests on a **`mega.buy_ratio` of 0.803 that collapses
to 0.227 (77% selling) once four post-close crosses at the $820.53 closing price are removed**;
and phase-3/5 established that `oi_building` is concentrated in **crash tails (55P +24,412 at
$0.01, 500P +11,767) and written puts**, not bullish positioning.

The composite's own top-level verdicts are far more equivocal than that 3/6 suggests, and they
corroborate the upstream work: **`conviction-matrix` returns `scenario = "MIXED"` at
`confidence_pct = 8.2`** — effectively no signal — and **`institutional-accumulation` returns
`"NEUTRAL — balanced dark pool activity"`.** `price-vs-flow` flags **`divergence = true`**
("Price is down 24.6% but options flow is bullish"), the classic reversal setup — but the
heuristic requires pairing it with the dealer regime, and phase-4's regime is **`FULLY_NEGATIVE`**,
which nullifies it.

**The most diagnostic result is cross-sectional:** MU's memory/semicap peers score **bearish** on
the same composite — **KLAC 6/6, WDC 4/6, AMAT 3/6, LRCX 3/6**, all carrying `dp_distribution`
and `oi_building_puts` — while MU alone is tagged `dp_accumulation`. **MU is the odd one out in
its own complex, and the reason is a single closing-auction print.**

## Key signals

- **`signal-confluence` bullish score = 3/6**, factors `bullish_flow`, `dp_accumulation`,
  `oi_building`; `volume_ratio = 0.84`; **absent from the bearish list (n=500)**.
  [INSIGHT:signal_confluence]
- **`conviction-matrix`: `scenario = "MIXED"`, `confidence_pct = 8.2`** — "Balanced dark pool
  activity — no clear bias." [INSIGHT:conviction_matrix]
- **`institutional-accumulation`: `"NEUTRAL — balanced dark pool activity"`**, `buy_sell_ratio`
  1.39, VWAP 819.11. [INSIGHT:institutional_accumulation]
- **`price-vs-flow`: `divergence = true`** — price -24.58% vs bullish net flow +$28,557,121.
  [INSIGHT:price_vs_flow]
- **Peers score bearish where MU does not: KLAC 6/6, WDC 4/6, AMAT 3/6, LRCX 3/6** — all with
  `dp_distribution`. [INSIGHT:signal_confluence]
- **`analyst-vs-flow` returned NO analyst consensus** — the yfinance leg is silently absent.
  [INSIGHT:analyst_vs_flow]

## Detailed findings

### Deep dive snapshot

From `uw insights deep-dive --symbol MU --date 2026-07-28` (the same call surfaced in
`phase-0.5-context.md`; reproduced here as the consolidation point):

**Directional aggregates (whole-tape):**

| field | value |
|---|---:|
| `bullish_premium` | $1,429,357,672 |
| `bearish_premium` | $1,400,800,551 |
| **derived `net_flow`** (bull − bear; **no `net_flow` key in this block**) | **+$28,557,121** |
| `call_premium` | $1,424,250,544 |
| `put_premium` | **$1,601,190,867** |
| `call_volume` / `put_volume` | 394,507 / 342,077 |
| `put_call_ratio` | 0.8671 |
| **`implied_move` / `implied_move_perc`** | **64.7944 / 7.904%** |
| `iv_rank` | 83.4835 |
| `iv30d` / `volatility` | 0.9604 / 1.2857 |
| `total_open_interest` | 3,326,277 |
| `next_earnings_date` | 2026-09-22 |

**Dark pool:** `total_premium` $12,931,901,814 · `total_shares` 15,787,788 · `trade_count`
31,598 · `avg_price` $817.22.

**Reconciliation against upstream — all three agree exactly:**
- Phase-1's DuckDB aggressor split reproduces `bullish_premium`/`bearish_premium` **to the
  dollar** (ask-calls 645.19 + bid-puts 784.17 = 1,429.36M ✓).
- Phase-0.5's `[CTX:]` rank (#8 universe-wide on net flow, 99.96th percentile on total premium)
  uses the same figures.
- Phase-2's dark-pool total reconciles to `block-stratified.total_premium_all_tiers`
  ($12,931,901,814 ✓).

**`implied_move_perc` = 7.904% is the figure phase-9 must size structures against (N4).**

**Fundamentals leg is unavailable:** `yahoo_fundamentals` returns
`{"error":"yahoo quoteSummary MU: HTTP 401"}` — so P/E, market cap and short % are **not**
available from this tool. They are sourced instead from `fz` in `phase-0-intake.md`
(Market Cap $926.70B, Sales $90.27B, Income $50.47B, Short Float 3.22%) and will be
authoritatively handled in phase-7b.

### Signal confluence

`uw insights signal-confluence --min-score 1 --top-n 500` (market-wide, filtered to MU):

**Bullish — MU present:**

| field | value |
|---|---|
| **`score`** | **3** (of 6) |
| **`factors`** | **`["bullish_flow","dp_accumulation","oi_building"]`** |
| `net_flow` | +$28,557,121 |
| `put_call_ratio` | 0.8671 |
| `iv_rank` | 83.4835 |
| **`volume_ratio`** | **0.84** |
| `close` / `sector` | 820.53 / Technology |

**Bearish — MU ABSENT from all 500 rows.**

*(An initial `--top-n 20` call showed MU in neither list; both were truncated at 20, so the query
was re-run at `--top-n 500` to establish MU's actual score. Per composition guidance,
`--min-score 1` was used throughout.)*

**Each of the three bullish factors is contradicted by an upstream decomposition of the same
underlying data:**

| factor | what the composite means | what phases 1–5 found |
|---|---|---|
| **`bullish_flow`** | `bullish_premium` > `bearish_premium` (+$28.6M) | **Definitional artifact.** `bullish_premium` = ask-calls + **bid-puts**, and bid-puts ($784.17M) is the larger half. **Calls were net SOLD -$45.76M; puts net sold -$74.32M; net customer delta ≈ -$41M ex-0DTE.** (phase-1) |
| **`dp_accumulation`** | `mega.buy_ratio` 0.803 | **Closing-auction artifact.** 88% of mega premium is post-close crosses at exactly $820.53 against a stale NBBO of 818.18/819.03. **Regular-hours mega buy_ratio = 0.227 (77% selling); every tier < 0.5.** (phase-2) |
| **`oi_building`** | OI rising, 30/30 build days | **True but mis-signed.** The build is **crash tails and written puts**: 55P Aug-07 +24,412 @ $0.01, 500P Jul-31 +11,767 @ $0.268 (ask-side), plus the 750/800 short-put campaign. Near-dated *protective* puts were closed (-24,600). (phase-3, phase-5) |

**Note `volume_ratio = 0.84` is itself a bearish/neutral input the score ignores** — it
reproduces phase-0.5's independent DuckDB calculation exactly and shows MU's option volume was
**below** its own 30-day average. The composite counts three "bullish" factors and does not
penalise the 0.84.

**Cross-sectional check (the most diagnostic result in this phase):**

| ticker | direction | score | factors |
|---|---|---:|---|
| **MU** | **bullish** | **3** | `bullish_flow`, **`dp_accumulation`**, `oi_building` |
| KLAC | bearish | **6** | `bearish_flow`, `high_pcr`, `volume_spike`, **`dp_distribution`**, `oi_building_puts`, `high_iv_sell_premium` |
| WDC | bearish | 4 | `bearish_flow`, `high_pcr`, `oi_building_puts`, `high_iv_sell_premium` |
| AMAT | bearish | 3 | **`dp_distribution`**, `oi_building_puts`, `high_iv_sell_premium` |
| LRCX | bearish | 3 | **`dp_distribution`**, `oi_building_puts`, `high_iv_sell_premium` |

**MU's four closest peers — every one of which fell 6–8% alongside it on the same CXMT
catalyst (phase-6) — score BEARISH with `dp_distribution`, while MU alone scores BULLISH with
`dp_accumulation`.** Given phase-2 demonstrated MU's accumulation tag is produced by a single
2.76M-share post-close cross, **the parsimonious reading is that MU belongs with its peers and
the composite is being misled by an auction print.**

### Conviction matrix

`uw insights conviction-matrix --symbol MU --date 2026-07-28`:

| field | value |
|---|---|
| **`scenario`** | **`MIXED`** |
| **`confidence_pct`** | **8.2** |
| `explanation` | "Balanced dark pool activity — no clear bias." |
| `thresholds` | bull 0.6 / bear 0.4 |
| `dark_pool.buy_ratio` | 0.582 |
| `dark_pool.buy_volume` / `sell_volume` | 9,193,327 / 6,594,461 |
| `options_flow.call_ask_volume` / `call_bid_volume` | 170,280 / **194,377** |
| `options_flow.put_ask_volume` / `put_bid_volume` | 148,856 / **167,982** |

- **`confidence_pct` of 8.2 is close to zero conviction.** The scenario is `MIXED` because the
  all-session dark-pool buy ratio (0.582) falls between the 0.4/0.6 thresholds.
- **The `options_flow` block is a direct, independent confirmation of phase-1's central
  finding:** `call_bid_volume` (194,377) **exceeds** `call_ask_volume` (170,280), and
  `put_bid_volume` (167,982) **exceeds** `put_ask_volume` (148,856). **More contracts were sold
  than bought on BOTH sides.** These counts match phase-1's DuckDB contract tallies (call ask
  170,280 ✓, put bid 167,982 ✓; call bid 193,977 and put ask 148,765 differ by <0.3%, a
  mid-print/cancel treatment difference). **The composite's own data says customers were net
  sellers of options — while its `signal-confluence` sibling tags MU `bullish_flow`.**
- The `dark_pool.buy_ratio` of 0.582 is the **all-session** figure. Phase-2's regular-hours cut
  is **0.464** overall and **0.227** at the mega tier. **Had the composite excluded the closing
  auction, this scenario would read bearish, not `MIXED`.**

### Price vs flow

`uw insights price-vs-flow --symbol MU --lookback-days 30`:

| field | value |
|---|---|
| **`divergence`** | **`true`** |
| **`divergence_signal`** | "DIVERGENCE: Price is down 24.6% but options flow is bullish (net flow: $28557121)" |
| `flow_direction` | `bullish` |
| `price_start` → `price_end` | 1087.99 → 820.53 (**-24.58%**) |
| `period_high` / `period_low` | 1255.00 / **789.09** |
| `net_premium_flow` | +$28,557,121 |
| `put_call_ratio` / `iv_rank` | 0.8671 / 83.4835 |

**This is the textbook bullish-reversal divergence — and it should not be sized on. Three
reasons:**

1. **The "bullish flow" leg is the same definitional artifact.** Net flow of +$28.6M is **+1.0%
   of $2.83B gross** (phase-1) and is majority put-selling. A divergence built on a 1% tilt is
   not a divergence.
2. **The heuristic explicitly requires pairing with the dealer regime before sizing.** Phase-4
   returned **`regime = FULLY_NEGATIVE`, `zero_gamma_level = null`** — dealers amplify moves
   rather than mean-revert them. In a short-gamma regime a price/flow divergence has no
   mechanical route to resolve upward.
3. **Phase-5 tested the generalised version of this claim and it failed.** Over 75 sessions,
   cumulative flow netted **+$320.7M on $200.8B gross (+0.16%)** with
   `trend_direction = "MIXED"`, and the 30-session `trend` shows **17 bullish days vs 13 bearish
   while price fell 24.6%.** **Flow direction has had no predictive relationship to MU's price.**

`period_low = 789.09` confirms today's intraday low (phase-3 screener `low`), and `period_high`
1255.00 is the 52-week high — MU has round-tripped from 1255 to 789 inside the window.

### Analyst vs flow

`uw insights analyst-vs-flow --symbol MU` returned **only the options-flow block**:

```json
{"symbol":"MU","options_flow":{"bullish_premium":1429357672,"bearish_premium":1400800551,
 "net_flow":28557121,"put_call_ratio":0.8670999500642574,"flow_sentiment":"bullish"}}
```

**There is no analyst consensus, price target, or recommendation field in the response** — the
yfinance leg is silently absent (consistent with the `yahoo quoteSummary MU: HTTP 401` error
seen in `deep-dive`). **No Wall Street vs options-trader comparison can be made from this tool.**
Recorded as a degradation, not fabricated around. **Phase-7b must source analyst data from
`fz`/Finnhub instead.**

*(Note `flow_sentiment: "bullish"` is derived from the same +$28.6M net — see the artifact
discussion above.)*

### Institutional accumulation

`uw insights institutional-accumulation --symbol MU`:

| field | value |
|---|---:|
| **`signal`** | **"NEUTRAL — balanced dark pool activity"** |
| `buy_sell_ratio` | 1.39 |
| `buy_side_volume` / `sell_side_volume` | 9,193,327 / 6,594,461 |
| `total_dp_premium` / `total_dp_volume` | $12,931,901,814 / 15,787,788 |
| `dark_pool_trades` | 31,598 |
| `vwap` / `avg_trade_price` | **819.11** / 817.22 |
| `price_30d_change_pct` | -24.58% |

**`top_price_levels` (today only):**

| price | shares | trades | premium |
|---:|---:|---:|---:|
| **820.53** | 4,059,410 | 74 | $3,330,867,686 |
| **900.20** | **224,669** | **2** | $202,247,033 |
| 834.00 | 72,028 | 23 | $60,071,352 |
| 827.41 | 57,560 | 5 | $47,625,724 |
| 830.00 | 48,621 | 59 | $40,355,433 |

- **The tool labels MU `NEUTRAL` despite a `buy_sell_ratio` of 1.39** — its own threshold logic
  evidently discounts the ratio, which is the correct call for the wrong stated reason.
- **The 900.20 row is decisive corroboration of phase-2:** 224,669 shares in only **2 trades**
  at the *previous* session's close. Phase-2 identified these as the 09:21:49 ET print of
  216,955 shares plus a 07:28:27 print of 7,714 — **216,955 + 7,714 = 224,669 exactly.** These
  are pre-market late-reported crosses struck 6% above the prevailing NBBO (848.00/848.36), not
  aggressive buying.
- Likewise the 820.53 row (4,059,410 shares in 74 trades) is the closing-auction cluster phase-2
  isolated (4,055,726 shares in 61 post-close prints at exactly $820.53).
- **VWAP 819.11 sits below the 820.53 close** — the average institutional print of the day was
  *below* where the stock settled.

### Earnings play

`uw insights earnings-play --days-until-earnings 30` returned 10 rows market-wide; **MU is not
among them.** This is correct and expected, not an error: per phase-6's calendar the reported
`next_earnings_date` is **2026-09-22 — 56 days out**, well outside the 30-day window.

**Out of window; no earnings-play commentary.** *(But note phase-3 flagged a 12.47%-of-OI
concentration at the Sep-18 expiry — four days BEFORE that date — and phase-4 flagged an IV hump
at Oct-16 (1.2188) consistent with an event between 9/18 and 10/16. **The earnings date needs
verification in phase-7b/7c.**)*

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|------------------|--------------------------|-----------|
| `uw insights deep-dive --symbol MU --date 2026-07-28 --json` | bullish=1,429,357,672; bearish=1,400,800,551; **derived net_flow=+28,557,121**; implied_move_perc=0.07904; iv_rank=83.4835; DP=$12.932B/15,787,788sh ← `.uw_screener.*`, `.uw_dark_pool.*` | whole-tape |
| `uw insights signal-confluence --direction bullish --min-score 1 --top-n 500 --date … --json` | **MU score=3**, factors=`["bullish_flow","dp_accumulation","oi_building"]`, **volume_ratio=0.84** ← `.results[]\|select(.ticker=="MU")` | 500 rows |
| `uw insights signal-confluence --direction bearish --min-score 1 --top-n 500 --date … --json` | **MU ABSENT**; KLAC=6, WDC=4, AMAT=3, LRCX=3 (all `dp_distribution`/`oi_building_puts`) | 500 rows |
| `uw insights conviction-matrix --symbol MU --date … --json` | **scenario=`MIXED`, confidence_pct=8.2**; dp buy_ratio=0.582; **call_bid 194,377 > call_ask 170,280; put_bid 167,982 > put_ask 148,856** | 1 row |
| `uw insights price-vs-flow --symbol MU --lookback-days 30 --json` | **divergence=true**; price -24.58% (1087.99→820.53); period_low=789.09; net_premium_flow=+28,557,121 | 30 sessions |
| `uw insights analyst-vs-flow --symbol MU --json` | **options_flow block ONLY — no analyst consensus returned** | 1 row |
| `uw insights institutional-accumulation --symbol MU --json` | **signal="NEUTRAL — balanced dark pool activity"**; buy_sell_ratio=1.39; vwap=819.11; top level 820.53 (4,059,410sh/74 trades), 900.20 (**224,669sh/2 trades**) | 1 row |
| `uw insights earnings-play --days-until-earnings 30 --json` | 10 rows; **MU absent** (earnings 2026-09-22 = 56 days out) | market-wide |

## Tool errors

1. **`uw insights deep-dive --symbol MU`** →
   `"yahoo_fundamentals":{"error":"yahoo quoteSummary MU: HTTP 401"}` (third consecutive
   occurrence this run — also in phases 0.5 and 1). **P/E, market cap and short % are therefore
   unavailable from the composite layer.** Non-blocking; sourced from `fz` and deferred to
   phase-7b per skill rule 4.
2. **`uw insights analyst-vs-flow --symbol MU`** returned **no analyst fields at all** — no
   consensus, target, or recommendation keys. Almost certainly the same yfinance
   unavailability. **This is a silent degradation, not an error message**, and would be easy to
   miss; recorded explicitly. **The "analyst vs flow" comparison this phase is supposed to
   produce could not be made.**
3. `uw insights signal-confluence` with the documented `--top-n 20` truncated MU out of both
   lists; re-run at `--top-n 500` to obtain the true score. Not an error — a query-design
   correction (see DATA NOTE).

## DATA NOTE / CORRECTION

1. **`signal-confluence` truncation.** The first call used `--top-n 20` and returned exactly 20
   rows in each direction with MU in neither — which could have been mis-recorded as "MU scores
   below min-score." Re-running at `--top-n 500` showed **MU scores 3 (bullish) and is genuinely
   absent from 500 bearish rows.** The distinction matters: "absent because truncated" and
   "absent because unscored" are different findings. **The reported score comes from the
   500-row query.**
2. **Two dark-pool buy ratios appear in this phase and both are quoted as returned:**
   `conviction-matrix.dark_pool.buy_ratio` = **0.582** and
   `institutional-accumulation.buy_sell_ratio` = **1.39** (= 9,193,327 / 6,594,461, i.e. a
   buy *fraction* of 0.582 — the same number expressed as a ratio). They are consistent with
   each other and **both are all-session figures** that include the closing auction. Phase-2's
   regular-hours figures (0.464 overall, 0.227 mega) are **not** a contradiction of these — they
   are a finer cut of the same data, and the difference is entirely the post-close crosses.
3. No value in this file was transcribed from an unparsed read; every figure round-tripped
   through `jq`.

## Cross-check vs phases 1–5

| UW insight | Value | Phase agreement? | Notes |
|---|---|---|---|
| **`signal_confluence` (bullish 3/6)** | `bullish_flow`, `dp_accumulation`, `oi_building` | **DISAGREES with phases 1, 2, 3** | All three factors are artifacts of aggregations that phases 1–3 decomposed: bullish_premium is majority put-selling; dp_accumulation is a closing-auction cross; oi_building is crash tails + written puts. |
| **`signal_confluence` `volume_ratio` 0.84** | 0.84 | **AGREES with phase-0.5** | Reproduces the DuckDB `optvol_x` exactly. Supports `BUSY_NAME_NORMAL_DAY`. |
| **`conviction_matrix` = `MIXED` @ 8.2%** | balanced | **AGREES with phase-1** | Near-zero confidence matches phase-1's "directionally inert" verdict. Its `options_flow` counts independently confirm **more contracts sold than bought on both sides**. |
| `conviction_matrix.dark_pool.buy_ratio` 0.582 | all-session | **PARTIALLY DISAGREES with phase-2** | Phase-2's regular-hours cut is 0.464 (mega 0.227). The composite includes the auction; phase-2 excludes it. **Phase-2 is the more precise read.** |
| **`institutional_accumulation` = `NEUTRAL`** | buy_sell 1.39 | **PARTIALLY AGREES with phase-2** | Both reject "accumulation." Phase-2 goes further to **DISTRIBUTION** on the regular-hours cut. Its `top_price_levels` **independently confirm** phase-2's auction (820.53 × 4.06M sh) and pre-market cross (900.20 × 224,669 sh in 2 trades). |
| **`price_vs_flow` divergence = true** | bullish flow, -24.6% price | **DISAGREES with phases 4 and 5** | Reversal signal is nullified by phase-4's `FULLY_NEGATIVE` gamma regime and refuted by phase-5's 75-session record (net +0.16%, `MIXED`; 17 bullish days vs 13 bearish while price fell 24.6%). |
| `deep_dive` aggregates | bullish/bearish premium, implied_move 7.904% | **AGREES exactly with phases 0.5 and 1** | Phase-1's DuckDB split reproduces both premium figures to the dollar. |
| `analyst_vs_flow` | no consensus returned | **CANNOT CROSS-CHECK** | yfinance leg absent → deferred to phase-7b. |
| `earnings_play` | MU absent (56 days out) | **AGREES with phase-6 calendar** | Correctly out of window. |
| **Peer confluence** | KLAC 6, WDC 4, AMAT 3, LRCX 3 — all bearish | **AGREES with phases 0.5 and 6** | Peers score bearish on the same instrumentation; MU's bullish tag is the outlier, and its differentiator is the auction print. |

## Verdict for downstream phases

- **UW composite bias: NOMINALLY MILD-BULLISH (3/6 confluence), SUBSTANTIVELY NEUTRAL-TO-BEARISH.**
  The composite's own headline verdicts are `MIXED` at **8.2% confidence** and `NEUTRAL` on
  accumulation. The only genuinely bullish output — the 3/6 confluence score — rests on three
  factors that phases 1–3 individually decomposed and reversed.
- **Conviction: 2 / 5 in the composite as a directional signal.** Not because the tools erred,
  but because MU is a case where **aggregate-level classifiers are systematically misled by two
  identifiable data artifacts**: (a) UW's `bullish_premium` definition treats put-selling as
  bullish, which on MU accounts for 54.9% of the bullish figure; (b) a single 2.76M-share
  post-close cross at the closing price flips the dark-pool tag from distribution to
  accumulation. **Both artifacts are documented with reconciling arithmetic upstream.**
- **Phase-9 guidance — this is the BASELINE, and it IS being overridden, with specific evidence:**
  The skill's convention is to treat phase-7 as the baseline and override only on specific
  contrary evidence from phases 1–8. **That override is warranted here and the evidence is
  named:**
  1. **Against `bullish_flow`:** phase-1's aggressor decomposition, which reconciles to UW's own
     `bullish_premium`/`bearish_premium` **to the dollar** and shows calls net sold -$45.76M,
     puts net sold -$74.32M, net customer delta **-$41M ex-0DTE** on a $926.7B cap. Confirmed
     independently by `conviction-matrix`'s own bid/ask volume counts.
  2. **Against `dp_accumulation`:** phase-2's session decomposition, which **reproduces UW's
     `mega.buy_ratio` of 0.803 exactly** and then shows it becomes **0.227** in regular hours,
     with every tier below 0.5 and after-hours prints down to $780.
  3. **Against `price_vs_flow`:** phase-4's `FULLY_NEGATIVE` regime (`zero_gamma_level = null`)
     and phase-5's 75-session finding that flow sign has no predictive relationship to MU price.
  **Where the composite and the decompositions conflict, the decompositions win — they are cuts
  of the same data at finer resolution, and they reconcile to the composite's own totals.**
- **What the composite genuinely adds (not overridden):** `volume_ratio = 0.84` (independent
  confirmation of `BUSY_NAME_NORMAL_DAY`); `confidence_pct = 8.2` (a quantified statement that
  there is almost no signal here); and the **peer cross-section (KLAC 6, WDC 4, AMAT 3, LRCX 3
  bearish)**, which is new information and points the same way as phases 2, 4 and 6.
- **Open questions:**
  - **Would the composite flip to bearish if the closing auction were excluded?** MU's peers all
    carry `dp_distribution`; MU's regular-hours mega ratio (0.227) is more extreme than several
    of them. **Strong likelihood the "MU is bullish, its peers are bearish" split is entirely an
    artifact — but the tool offers no session filter to prove it.** → phase-8b should treat
    MU as belonging with its peers unless the desk agents find a reason otherwise.
  - **Who is the 2.76M-share post-close counterparty?** Still unresolved from phase-2, and it is
    now clear that this single print is what separates MU's composite classification from its
    entire peer group. **It is the highest-value unknown in the run.**
  - **Analyst consensus is entirely missing** (yfinance 401). Phase-7b must supply it from `fz`
    or Finnhub, or the "Wall Street vs flow" dimension stays blank for this run.
  - **Earnings date (2026-09-22) remains unverified** while two independent structural hints
    (phase-3 Sep-18 OI, phase-4 Oct-16 IV hump) bracket it. → phase-7b/7c.
