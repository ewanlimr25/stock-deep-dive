# Phase 7 — UW Insights Confluence

**Ticker:** SWKS
**As-of date:** 2026-07-31
**Generated:** 2026-08-02
**Upstream phases cited:** `phase-0.5-context.md`, `phase-1-flow.md`, `phase-2-dark-pool.md`, `phase-3-positioning.md`, `phase-4-structure.md`, `phase-5-historical.md`, `phase-6-macro.md`

## Summary

UW's composite layer returns **MIXED with near-zero confidence**, and it leans
**mildly bearish** where it leans at all. `conviction-matrix` returns
`scenario: "MIXED"` with **`confidence_pct: 7.2`** and the explanation *"Balanced
dark pool activity — no clear bias."* `institutional-accumulation` returns
**`NEUTRAL — balanced dark pool activity`**. `signal-confluence` does **not** rank
SWKS anywhere in the top-2,000 bullish rows, but **does** place it in the bearish
list with a score of **2 of 6** on the factors **`high_pcr`** and
**`dp_distribution`**. The one genuinely informative composite is `price-vs-flow`,
which flags **`divergence: true` — *"Price is down 14.0% but options flow is
bullish (net flow: $43,882)."*** That divergence is real but, as phases 1 and 5
established, the "bullish" leg is **put selling misclassified as bullish premium**,
so the divergence is far weaker than the label implies. **This phase largely
agrees with phases 1–5 (thin, mixed, low-conviction) and disagrees with phase 2 on
one point — the dark-pool sign — where phase 2's session- and trade-code-cleaned
read is the better evidence.** Two composites are degraded: `analyst-vs-flow`
returned **no analyst data at all**, and `deep-dive`'s `yahoo_fundamentals` block is
**`HTTP 401`**.

## Key signals

- **`conviction-matrix`: `scenario: "MIXED"`, `confidence_pct: 7.2`** —
  *"Balanced dark pool activity — no clear bias."* Thresholds `bear: 0.4`,
  `bull: 0.6`; observed dark-pool `buy_ratio` **0.428**, i.e. just inside the
  neutral band. `[INSIGHT:conviction_matrix]`
- **`signal-confluence`: SWKS is absent from the bullish list across 2,000 rows**
  (cutoff score 2) but **present in the bearish list at score 2/6**, factors
  **`["high_pcr","dp_distribution"]`**. The bullish leader on the day scored **6/6**
  (DXCM). `[INSIGHT:signal_confluence]`
- **`price-vs-flow`: `divergence: true`** — price **−14.04%** over 30 sessions
  (72.45 → 62.28, `period_high` 79.20, `period_low` 55.43) against `flow_direction:
  "bullish"` (`net_premium_flow` **+$43,882**). `[INSIGHT:price_vs_flow]`
- **`institutional-accumulation`: `NEUTRAL — balanced dark pool activity`**,
  `buy_sell_ratio` **0.75**, `vwap` **61.79**, `avg_trade_price` **61.90**,
  `total_dp_premium` **$16,263,573** on 263,187 shares / 56 trades.
  `[INSIGHT:institutional_accumulation]`
- **`analyst-vs-flow` returned NO analyst consensus** — the response contains only
  `symbol` and an `options_flow` echo. The Wall-Street-vs-options comparison the
  tool exists to make **could not be performed**. `[INSIGHT:analyst_vs_flow]`
- **`earnings-play`: SWKS absent** from the 10 returned rows — correct, since next
  earnings is **2026-10-27**, **88 days out** and far outside the 30-day window
  (`phase-6-macro.md §Catalyst calendar`). `[INSIGHT:earnings_play]`

## Detailed findings

### Deep-dive snapshot

`uw insights deep-dive --symbol SWKS --date 2026-07-31`. Four sub-blocks returned;
one errored.

**`uw_screener` — whole-tape directional aggregates:**

| Field | Value |
|---|---|
| `bullish_premium` | **$376,945** |
| `bearish_premium` | **$333,063** |
| **derived `net_flow` = bullish − bearish** | **+$43,882** |
| `call_premium` | $380,703 |
| `put_premium` | $497,180 |
| `call_volume` / `put_volume` | 1,080 / 4,384 |
| `put_call_ratio` | **4.0593** |
| **`implied_move` / `implied_move_perc`** | **$5.6749 / 9.098%** |
| `iv_rank` | 52.8977 |
| `iv30d` / `volatility` | 0.559032 |
| `total_open_interest` | 118,470 |
| `next_earnings_date` | **2026-10-27** |

**Reconciliation — clean.** Every figure matches `phase-1-flow.md §Whole-tape
aggregate` exactly, and `net_flow` was **derived** (`bullish_premium −
bearish_premium`) because this block has **no `net_flow` key**. Cross-checked a
third time against `phase-0.5-context.md`'s independent parquet derivation
(`net_call_premium − net_put_premium` = −170,899 − (−214,781) = **+43,882**). Three
independent paths, one number.

The **implied move of ±9.098% / ±$5.67** is the figure phase 9 sizes structures to
(N4), and it is carried forward unchanged from `[CTX:implied_move_pct]`.

**`uw_dark_pool`:**

| Field | Value |
|---|---|
| `total_premium` | $16,263,573.10 |
| `total_shares` | 263,187 |
| `trade_count` | 56 |
| `avg_price` | $61.9005 |

Matches `phase-2-dark-pool.md` exactly (56 prints, $16,263,573).

**`uw_top_oi_changes`** — the five largest OI moves on the chain:

| `option_symbol` | Strike | DTE | `oi_diff_plain` | `volume` | `avg_price` |
|---|---|---|---|---|---|
| SWKS260918P00052500 | 52.5 P | 49 | **+46** | 55 | $1.691 |
| SWKS260918P00057500 | 57.5 P | 49 | +29 | 34 | $3.129 |
| SWKS261120P00042500 | 42.5 P | 112 | +24 | 24 | $1.279 |
| SWKS260821C00065000 | 65 C | 21 | +15 | 31 | $2.239 |
| SWKS260821P00060000 | 60 P | 21 | +15 | 41 | $2.908 |

Identical to `phase-3-positioning.md §Largest OI increases`. **The largest OI change
on the entire SWKS chain is 46 contracts**, and the three largest are all puts —
the composite layer independently reproduces phase 3's "the chain is inert" finding.

**`yahoo_fundamentals`: `{"error":"yahoo quoteSummary SWKS: HTTP 401"}`** — so **no
P/E, no market cap, no short %, no float** from this tool. Substituting only
already-validated values from elsewhere in this run: market cap **$9,401,539,419**
and 52-week range **$51.93–$90.90** (screener parquet, `phase-0.5-context.md`);
**P/E 32.26**, EV **$9.25B**, Sales **$4.01B**, Income **$290.10M** (`fz`,
`phase-0-intake.md`). Short interest is **still unavailable** —
`phase-0-intake.md` recorded `Short Float` as unparseable — and is deferred to
phase 7c.

### Signal confluence

`uw insights signal-confluence --min-score 1 --top-n 2000 --date 2026-07-31`, run
in both directions:

| Direction | Rows returned | Lowest score in list | **SWKS present?** |
|---|---|---|---|
| bullish | 2,000 | 2 | **NO** |
| bearish | 2,000 | 1 | **YES** |

SWKS's bearish row:

```json
{"ticker":"SWKS","score":2,"factors":["high_pcr","dp_distribution"],
 "close":62.28,"iv_rank":52.8977,"net_flow":43882,
 "put_call_ratio":4.059259259259259,"sector":"Technology","volume_ratio":1}
```

For contrast, the day's top bullish row scored **6 of 6**:

```json
{"ticker":"DXCM","score":6,"factors":["bullish_flow","low_pcr","volume_spike",
 "dp_accumulation","oi_building","low_iv_cheap_options"],
 "iv_rank":19.5148,"net_flow":1446649,"volume_ratio":3.8}
```

**SWKS scores 2 of 6 bearish and 0 of 6 bullish.** Per the phase heuristic
(≥5 is rare and high-conviction), **2 is weak**. Note `volume_ratio: 1` in the SWKS
row — a fourth independent confirmation of `phase-0.5-context.md`'s finding that
option volume was exactly **1.00×** its own 30-day average.

Both contributing factors deserve scrutiny:

- **`high_pcr`** — true as a number (4.0593, a **+2.557 z-score** per
  `phase-5-historical.md`), but `phase-1-flow.md` showed **88.9% of those puts
  traded on the bid** and 3,333 of them were a single **opening short-put block**.
  A high P/C built from put *selling* is not a bearish factor. **The factor is
  arithmetically correct and directionally misleading.**
- **`dp_distribution`** — this is the one place the composite layer materially
  disagrees with an upstream phase. See the cross-check table below.

### Conviction matrix

`uw insights conviction-matrix --symbol SWKS --date 2026-07-31`:

| Field | Value |
|---|---|
| **`scenario`** | **`MIXED`** |
| **`confidence_pct`** | **7.2** |
| `explanation` | *"Balanced dark pool activity — no clear bias."* |
| `thresholds` | `bear: 0.4`, `bull: 0.6` |
| `dark_pool.buy_ratio` | **0.428** |
| `dark_pool.buy_volume` / `sell_volume` / `trades` | 112,594 / 150,593 / 56 |
| `options_flow.call_ask_volume` / `call_bid_volume` | **172 / 811** |
| `options_flow.put_ask_volume` / `put_bid_volume` | **312 / 3,245** |

**`confidence_pct` of 7.2 is the single most honest number in this phase.** The
engine is saying it has almost no information. None of the five scenario labels
(DIRECTIONAL_LONG / HEDGED_LONG / COVERED_CALL / DIRECTIONAL_SHORT / MIXED)
applies with conviction, and `MIXED` is the residual.

**The `options_flow` sub-block reconciles exactly with `phase-1-flow.md`'s
ask/bid split** (call ask 172 / bid 811 ⇒ call ask-share **0.175**; put ask 312 /
bid 3,245 ⇒ put ask-share **0.088**). This is a valuable independent confirmation
that phase 1's central finding — **both legs sold on the bid** — came from the same
underlying data the composite layer sees, not from a DuckDB artifact.

**But note what the matrix does *not* do with it.** It reads a `buy_ratio` of 0.428
from the dark pool and calls the day balanced, while the *options* sub-block it
prints in the same response shows a **19:1 put-bid-to-put-ask imbalance**. The
engine does not appear to weight aggressor side in its scenario logic. Its
`MIXED`/7.2% output is nonetheless the right answer for the wrong reason.

### Price vs flow

`uw insights price-vs-flow --symbol SWKS --lookback-days 30`:

| Field | Value |
|---|---|
| **`divergence`** | **true** |
| **`divergence_signal`** | *"DIVERGENCE: Price is down 14.0% but options flow is bullish (net flow: $43882)"* |
| `flow_direction` | `bullish` |
| `price_start` → `price_end` | **72.45 → 62.28** |
| `price_change_pct` | **−14.04%** |
| `period_high` / `period_low` | **79.20 / 55.43** |
| `net_premium_flow` | +$43,882 |
| `put_call_ratio` | 4.0593 |
| `iv_rank` | 52.8977 |

The price leg reconciles exactly with `phase-5-historical.md §Multi-day trend table`
(`price_change: "72.45 -> 62.28"`, `days_analyzed: 30`, range 2026-06-18 →
2026-07-31, contiguous, no gap crossing). `period_high` 79.20 and `period_low`
**55.43** extend slightly beyond the closing-price series phase 5 used
(intraday extremes vs closes), consistent with phase 5's **$56.91–57.50 triple
bottom** on a closing basis.

**Assessment: the divergence is real in form and weak in substance.** The phase
heuristic treats *bullish flow + falling price* as a leading reversal signal — but
the "bullish" leg here is **+$43,882 on a $877,883 tape**, i.e. a **5.0% tilt**,
and it is manufactured by put selling. `phase-5-historical.md` independently found
the 90-day cumulative premium flow to be **`MIXED`** (+$6.71M net on $178.6M
two-way, a 3.8% tilt) — so there is **no persistent bullish flow** behind the
divergence either. Per the heuristic's own instruction, pairing it with the phase-4
dealer regime: `phase-4-structure.md` has dealers **short gamma at spot**, which
**amplifies** rather than mean-reverts — the mechanical backdrop does **not**
support fading the 14% decline on this signal alone.

### Analyst vs flow — **DEGRADED, no analyst data**

`uw insights analyst-vs-flow --symbol SWKS --json` returned only two top-level
keys:

```json
{"symbol":"SWKS",
 "options_flow":{"bullish_premium":376945,"bearish_premium":333063,
                 "net_flow":43882,"put_call_ratio":4.059259259259259,
                 "flow_sentiment":"bullish"}}
```

**There is no analyst block** — no consensus rating, no price target, no
recommendation count. The tool's stated purpose ("Wall Street vs options-trader
agreement") **cannot be fulfilled**. This is consistent with the
`yahoo quoteSummary SWKS: HTTP 401` seen in `deep-dive` and first recorded in
`phase-2-dark-pool.md §Tool errors` — the yfinance-backed analyst lane is
unavailable across the whole run.

**Consequence:** the analyst-consensus leg of this phase is **missing**, and
`phase-7b-fundamentals.md` / `phase-7c-sentiment.md` must source analyst views from
`fz` or WebSearch instead. Recorded here rather than papered over. `phase-6-macro.md`
did surface one relevant datapoint from primary reporting — *"analysts remain on
the sidelines until the Qorvo deal closes"* (Seeking Alpha, 2026-07-29) — which is
a **qualitative** stand-in, not a consensus figure, and is not treated as one.

The `flow_sentiment: "bullish"` label restates the same +$43,882 already
disqualified above.

### Institutional accumulation

`uw insights institutional-accumulation --symbol SWKS --json`:

| Field | Value |
|---|---|
| **`signal`** | **`NEUTRAL — balanced dark pool activity`** |
| `buy_sell_ratio` | **0.75** |
| `buy_side_volume` / `sell_side_volume` | 112,594 / 150,593 |
| `dark_pool_trades` | 56 |
| `total_dp_volume` / `total_dp_premium` | 263,187 / $16,263,573.10 |
| `vwap` | **$61.79** |
| `avg_trade_price` | $61.90 |
| `price_30d_change_pct` | −14.04% |

`top_price_levels`:

| Price | Shares | Premium | Trades |
|---|---|---|---|
| **$62.28** | 105,758 | $6,586,608 | 17 |
| **$60.74** | 54,485 | $3,309,565 | **2** |
| $62.50 | 7,500 | $468,750 | 2 |
| $61.60 | 6,282 | $386,971 | 1 |
| $62.09 | 6,212 | $385,672 | 1 |

**Note `buy_sell_ratio: 0.75` is a buy-to-sell RATIO, not a buy fraction**
(112,594 / 150,593 = 0.7477). The equivalent buy *fraction* is
112,594 / 263,187 = **0.428**, matching `conviction-matrix` exactly.

**Reconciliation with phase 2 — the numbers agree, the labels do not.** Phase 2's
independent decomposition produced all-session buy **103,822**, sell **150,593**,
flat **8,772**. UW's `buy_side_volume` of **112,594 = 103,822 + 8,772**, i.e. the
engine classifies prints at exactly the NBBO mid as **buys**. Sell volume matches to
the share. **The raw data is identical; the difference is entirely in treatment.**

Phase 2 then applied two cleanings the composite does not:
1. Removed the **16 prints (103,612 shares, 39.4% of the day)** carrying
   `average_price_trade` / `prior_reference_price` codes — VWAP fills and late
   reports whose price carries no aggressor information.
2. Removed the **16:00 auction/late cluster**, whose classifications are artifacts
   of a wide post-close 61.93/62.96 NBBO.

The **$60.74 level UW ranks second (54,485 shares, exactly 2 trades)** is precisely
the pair of VWAP prints phase 2 disqualified. **A "top institutional price level"
built from two average-price prints is not a level.**

After cleaning, phase 2's as-of-day regular-session directional buy ratio is
**0.461** — still balanced, so **on the as-of day UW's `NEUTRAL` label and phase 2
agree**. The disagreement is about the **prior two sessions**, which this tool does
not look at: 2026-07-29 **+341,637 net shares at buy_ratio 0.634**, 2026-07-30
**+232,129 at 0.751**.

### Earnings play — out of window

`uw insights earnings-play --days-until-earnings 30 --date 2026-07-31` returned
**10 rows; SWKS is not among them.** Correct and expected: SWKS's next earnings
date is **2026-10-27**, i.e. **88 calendar days out**, verified in
`phase-0.5-context.md` by reading the field's own 12-snapshot history (it rolled
from `2026-07-28 postmarket` to `2026-10-27` between the 07-28 and 07-29
snapshots). Per the phase's pitfall note this is **"out of window," not an error**.

**No earnings setup exists**, and — as `phase-6-macro.md` emphasises — **there is
no scheduled SWKS earnings risk inside a 1–8 week trade horizon.**

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw insights deep-dive --symbol SWKS --date 2026-07-31 --json` | `uw_screener`: bullish_premium 376945, bearish_premium 333063 ⇒ **derived net_flow +43882**; call_premium 380703, put_premium 497180, put_call_ratio 4.059259, **implied_move 5.674921 / implied_move_perc 0.0909807**, iv_rank 52.8977, total_open_interest 118470, next_earnings_date 2026-10-27. `uw_dark_pool`: total_premium 16263573.1003, total_shares 263187, trade_count 56, avg_price 61.90052. `uw_top_oi_changes[0]`: SWKS260918P00052500, oi_diff_plain **46**. **`yahoo_fundamentals` = `{"error":"yahoo quoteSummary SWKS: HTTP 401"}`** | 4 blocks |
| `uw insights conviction-matrix --symbol SWKS --date 2026-07-31 --json` | **`scenario`="MIXED"**, **`confidence_pct`=7.2**, `explanation`="Balanced dark pool activity — no clear bias.", `dark_pool.buy_ratio`=0.428 (buy 112594 / sell 150593 / 56 trades), `options_flow`={call_ask 172, call_bid 811, put_ask 312, put_bid 3245}, thresholds {bear 0.4, bull 0.6} ← `.scenario`, `.confidence_pct` | 1 |
| `uw insights signal-confluence --direction bullish --min-score 1 --top-n 100 --date 2026-07-31 --json` | 100 rows; SWKS **absent** ← `[.results[]\|select(.ticker=="SWKS")]\|.[0]//null` = null; top row DXCM score **6**, factors 6 | top-100 |
| `uw insights signal-confluence --direction bullish --min-score 1 --top-n 2000 --date 2026-07-31 --json` | 2,000 rows, lowest score **2**; SWKS still **absent** | top-2000 |
| `uw insights signal-confluence --direction bearish --min-score 1 --top-n 100 --date 2026-07-31 --json` | 100 rows; SWKS **absent** | top-100 |
| `uw insights signal-confluence --direction bearish --min-score 1 --top-n 2000 --date 2026-07-31 --json` | 2,000 rows, lowest score 1; **SWKS present: `score` 2, `factors` ["high_pcr","dp_distribution"], close 62.28, iv_rank 52.8977, net_flow 43882, put_call_ratio 4.059259, `volume_ratio` 1** ← `[.results[]\|select(.ticker=="SWKS")]\|.[0]` | top-2000 |
| `uw insights price-vs-flow --symbol SWKS --lookback-days 30 --json` | **`divergence`=true**, `divergence_signal`="DIVERGENCE: Price is down 14.0% but options flow is bullish (net flow: $43882)", `flow_direction`="bullish", `price_start`=72.45, `price_end`=62.28, `price_change_pct`=**−14.04**, `period_high`=79.20, `period_low`=**55.43**, `net_premium_flow`=43882 ← `.divergence`, `.divergence_signal` | 30 sessions |
| `uw insights analyst-vs-flow --symbol SWKS --json` | **Only 2 keys returned** ← `keys` = `["options_flow","symbol"]`. **No analyst consensus block.** `options_flow.flow_sentiment`="bullish", net_flow 43882 | **degraded** |
| `uw insights institutional-accumulation --symbol SWKS --json` | **`signal`="NEUTRAL — balanced dark pool activity"**, `buy_sell_ratio`=**0.75**, buy_side_volume 112594, sell_side_volume 150593, `vwap`=**61.79**, avg_trade_price 61.90, total_dp_premium 16263573.1003, price_30d_change_pct −14.04; `top_price_levels[0]` = 62.28/105758sh/17 trades, `[1]` = **60.74/54485sh/2 trades** ← `.signal`, `.top_price_levels[]` | 1 + 5 levels |
| `uw insights earnings-play --days-until-earnings 30 --date 2026-07-31 --json` | 10 rows; SWKS **absent** ← `[.results[]\|select(.ticker=="SWKS")]\|.[0]//null` = null (next earnings 2026-10-27 = 88d out) | top-10 |

## Tool errors

- `uw insights deep-dive` → sub-block
  **`"yahoo_fundamentals": {"error":"yahoo quoteSummary SWKS: HTTP 401"}`**
  (verbatim). No P/E, market cap, short %, or float from this tool. First observed
  and recorded in `phase-2-dark-pool.md`; **now confirmed as persistent across the
  run.** Substituted only with values already validated from the screener parquet
  and `fz`; **no fundamental figure was taken from this tool.**
- `uw insights analyst-vs-flow` → returned **without any analyst block** (keys:
  `["options_flow","symbol"]` only). Not an exception — a **silently degraded
  response**, almost certainly the same yfinance 401. **The tool's core function
  could not be performed.** No consensus rating or price target is reported
  anywhere in this phase.
- `uw insights earnings-play` → SWKS absent. **Not an error** — "out of window" per
  the phase's own pitfall note (earnings 88 days out).
- `uw insights signal-confluence` (bullish) → SWKS absent at `--top-n 100` **and**
  at `--top-n 2000`. **Not an error** — the name genuinely scores 0 bullish factors.
  Re-called at wider `--top-n` per the composition guidance before recording the
  absence.

## Cross-check vs phases 1–5

| UW insight | Value | Phase agreement? | Notes |
|---|---|---|---|
| `conviction_matrix.scenario` | **MIXED** (7.2% conf.) | **AGREES** with phases 1, 3, 5 | Phase 1 verdict was "MIXED, tilted neutral-constructive" at conviction 2/5; phase 3 found the chain inert (conviction 1/5); phase 5 found no measurable edge (1/5). A 7.2% confidence score is the composite layer saying the same thing. |
| `conviction_matrix.options_flow` (ask/bid) | call 172/811, put 312/3,245 | **AGREES EXACTLY** with phase 1 | Independently confirms call ask-share **0.175** and put ask-share **0.088** from the engine's own data, not DuckDB. Phase 1's central finding is corroborated at source. |
| `signal_confluence` bearish `high_pcr` | P/C 4.0593 | **AGREES on the number, DISAGREES on the sign** | Phase 1 and phase 5 both show the high P/C is built from put **selling** (88.9% on the bid; one 3,333-contract opening short block). The factor is arithmetically right and directionally misleading. |
| **`signal_confluence` bearish `dp_distribution`** | — | **DISAGREES with phase 2** | **The one material conflict in this phase.** UW reads distribution from a raw all-session `buy_ratio` of 0.428. Phase 2, after removing 39.4% of shares carrying `average_price_trade`/`prior_reference_price` codes and the wide-NBBO closing auction, gets **0.461 for the as-of day (balanced)** and **0.634 / 0.751 for 2026-07-29 / 07-30 (accumulation, +573,766 net shares)**. **Phase 2's read is preferred** — it is the same source data with documented contaminants removed, and the raw and cleaned share counts reconcile exactly. |
| `institutional_accumulation.signal` | **NEUTRAL** | **AGREES on the as-of day, INCOMPLETE overall** | Phase 2 also calls the as-of session neutral (net −6,697 shares). But this tool looks only at the as-of day and therefore **cannot see** the two-session accumulation that is phase 2's actual finding. Not a contradiction — a narrower window. |
| `institutional_accumulation.top_price_levels[1]` | $60.74, 54,485 sh, 2 trades | **DISAGREES with phase 2** | Those two prints are the disqualified VWAP `average_price_trade` / `derivative_priced` blocks. Phase 2 excludes $60.74 as a level; it should not be used by phase 9. |
| `price_vs_flow.divergence` | **true** | **AGREES with phase 5 on the price leg, DISAGREES on flow significance** | Price −14.04% matches `historical trend` exactly. But phase 5's 90-day cumulative flow is **`MIXED`** (+3.8% tilt) — there is no persistent bullish flow behind the divergence, and phase 4's short-gamma regime argues against fading the decline on it. |
| `deep_dive.uw_top_oi_changes` | max +46 contracts | **AGREES EXACTLY** with phase 3 | Same five contracts, same magnitudes. Independent confirmation the chain is inert. |
| `signal_confluence` `volume_ratio` | **1** | **AGREES EXACTLY** with phase 0.5 | Fourth independent confirmation of option volume at **1.00×** its own 30-day average. |
| `earnings_play` | SWKS absent | **AGREES** with phases 0.5 and 6 | Earnings 2026-10-27, 88 days out. No event inside the trade horizon. |
| `analyst_vs_flow` | **no analyst data** | **cannot cross-check** | Degraded; deferred to phases 7b/7c. |
| **Merger context** | **absent from every composite** | **BLIND SPOT** | No UW composite references the Qorvo combination, the eliminated dividend, the ~$2B debt raise, or the SAMR Phase III review (`phase-6-macro.md`). The composite layer is scoring SWKS as an ordinary single-name semi. **It is not one.** |

## DATA NOTE / CORRECTION

1. **`buy_sell_ratio: 0.75` is a ratio, not a fraction.** 112,594 / 150,593 =
   0.7477. The comparable buy *fraction* is 112,594 / 263,187 = **0.428**, which is
   what `conviction-matrix` reports. Both are quoted so neither is mistaken for the
   other.
2. **UW classifies mid-priced prints as buys.** `buy_side_volume` 112,594 equals
   phase 2's buy 103,822 **plus** flat 8,772. Verified by arithmetic against the
   independently computed phase-2 figures; `sell_side_volume` matches to the share.
   This is a **classification difference, not a data discrepancy**, and it accounts
   for part of the 0.428-vs-0.461 gap.
3. **`net_flow` derived, not read** — the `uw_screener` block has no `net_flow` key
   (`lib/uw-json-paths.md` phantom-field trap #1). Value **+$43,882** derived and
   cross-checked against two independent paths already validated in this run.
4. **Nothing was substituted for the missing Yahoo/analyst data.** Where the tools
   returned nothing, this phase reports nothing. Market cap, P/E and 52-week range
   are quoted only from sources already validated elsewhere in the run, and are
   labelled with those sources.
5. **`signal-confluence` was re-called at `--top-n 2000`** before recording SWKS's
   bullish absence, per the composition guidance ("if `<SYMBOL>` is not in the
   result … re-call"). The absence is genuine at a bullish-list floor of score 2.

## Verdict for downstream phases

- **UW composite bias: MIXED, leaning mildly BEARISH.** `conviction-matrix` =
  `MIXED` at **7.2% confidence**; `institutional-accumulation` = `NEUTRAL`;
  `signal-confluence` = **0/6 bullish, 2/6 bearish** (`high_pcr`,
  `dp_distribution`). The only bullish-flavoured composite (`price-vs-flow`
  divergence) rests on a **+$43,882 net on an $877,883 tape** that phases 1 and 5
  have shown is put-selling misclassified as bullish premium.
- **Conviction: 2 / 5.** The composite layer is internally consistent with phases
  1, 3 and 5 and independently reproduces four of their key numbers (ask/bid split,
  max OI change of 46, volume ratio 1.00×, price −14.04%) — which is genuine
  corroboration. But it is held low because: (a) the engine itself reports **7.2%
  confidence**; (b) **two of seven tools are degraded** (`analyst-vs-flow` returned
  no analyst data; `deep-dive`'s Yahoo block is HTTP 401); (c) its one directional
  factor pair is **arithmetically right and directionally wrong** on `high_pcr` and
  **contaminated** on `dp_distribution`; and (d) **it is blind to the single most
  important fact about this security.**
- **Phase 9 should treat this as the BASELINE — with two named overrides.** The
  baseline is *"mixed, low-confidence, mildly bearish-tilted, no edge."* Phase 9
  should depart from it **only** on these two specific pieces of contrary evidence,
  both already documented upstream:
  1. **`dp_distribution` is overridden by `phase-2-dark-pool.md`.** Same source
     data, contaminants removed and reconciled: **+573,766 net shares absorbed
     across 2026-07-29/30 (0.380% of shares outstanding) at buy ratios of 0.634 and
     0.751**, versus a +12k–+24k daily baseline. The composite's raw 0.428 does not
     survive the cleaning.
  2. **The entire composite layer is blind to the merger** (`phase-6-macro.md`):
     Qorvo combination at **0.960 SWKS + $32.50 cash**, **China SAMR in Phase III**,
     **dividend eliminated**, **~$2B debt raise**, **$2B buyback**, arb spread
     **1.86%**. None of the seven tools references any of it. **A composite score
     computed on the pre-merger security cannot be the baseline for the
     post-merger one**, and phase 9 must weight `phase-6-macro.md` accordingly.
- **Open questions:**
  - **Does the `price-vs-flow` divergence mean anything without persistent flow
    behind it?** The signal fires on a 5.0% single-day premium tilt while phase 5's
    90-day cumulative flow is `MIXED` at a 3.8% tilt. Phase 8's bull case must
    either find persistence the tools missed or drop the divergence as an argument.
  - **How much of the "bearish" composite is just the merger arb?**
    `phase-6-macro.md` established that the standard arb is long QRVO / **short
    0.960 SWKS** — a structural, price-insensitive SWKS supply. That would produce
    exactly the observed signature: dark-pool sell prints, a `dp_distribution`
    factor, and a flat tape on the day AAPL fell 7.35%. **Phases 7c and 8b must
    determine whether the bearish read is a view or a mechanic** — the two have
    opposite trading implications.
  - **Can any analyst view be sourced at all?** The `analyst-vs-flow` lane is dead
    for this run. `phase-7b-fundamentals.md` (peers, `fz` analyst cross-source) and
    `phase-7c-sentiment.md` (revisions) must fill it, or the "Wall Street vs
    options" comparison is simply absent from this blueprint and phase 10 should
    score it as a missing input rather than a neutral one.
