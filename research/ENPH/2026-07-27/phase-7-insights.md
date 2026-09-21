# Phase 7 — UW Insights Confluence

**Ticker:** ENPH
**As-of date:** 2026-07-27
**Generated:** 2026-07-27T21:38:00-04:00
**Upstream phases cited:** `phase-0.5-context.md`, `phase-1-flow.md`, `phase-2-dark-pool.md`, `phase-3-positioning.md`, `phase-4-structure.md`, `phase-5-historical.md`, `phase-6-macro.md`

## Summary

**The UW composites split, and the split is diagnostic rather than confusing.**
`price-vs-flow` returns `divergence = false` — *"Price and flow are aligned"* —
with `flow_direction = "bearish"` and `price_change_pct = −30.37%`: no reversal
signal, just a stock and its tape going the same way. `conviction-matrix` returns
`scenario = "COVERED_CALL"` at only **`confidence_pct = 21.1`**, explaining
*"Dark pool buying + call selling — yield enhancement, capping upside."*
`institutional-accumulation` goes further and returns
**`signal = "ACCUMULATION — dark pool buy volume significantly exceeds sell
volume"`, `buy_sell_ratio = 2.18`.**

**That accumulation signal is an artifact, and this phase disproves it.** The
`buy_ratio = 0.686` derives from `buy_volume = 216,974` vs `sell_volume = 99,381`
— and **129,000 of those 216,974 "buy" shares are the single closing-auction
cross** identified in `phase-2-dark-pool.md`. Re-running the identical
above/below-mid classifier over the same 38 prints with that one cross excluded
drops the buy ratio to **0.45** — i.e. **55% sell**. Two of the three UW composites
that lean bullish rest entirely on one mechanical print.

What survives is consistent with phases 1–6: **calls are being sold**
(`call_ask_volume 4,196` vs `call_bid_volume 4,635`), **puts are being bought**
(`put_ask 2,410` vs `put_bid 1,719`), flow and price are aligned bearish, and
ENPH is **absent from `signal-confluence` in both directions** and **absent from
`earnings-play`** — the latter because every qualifying name carries
`iv_rank = 100` while ENPH sits at 69.81.

**Composite verdict: weakly bearish, low confidence — and notably weaker than the
raw tool labels suggest.** Phase-9 should take this as the baseline and note that
the strongest-sounding UW label in the entire run ("ACCUMULATION") does not
survive inspection.

## Key signals

- **`institutional-accumulation` = "ACCUMULATION", `buy_sell_ratio = 2.18` —
  REFUTED.** Excluding the 129,000-share closing cross, `buy_ratio` falls
  **0.679 → 0.45** [INSIGHT:institutional_accumulation],
  [INSIGHT:dp_reclassified DUCKDB].
- **`conviction-matrix` = `COVERED_CALL`, `confidence_pct = 21.1`** — *"Dark pool
  buying + call selling."* The call-selling half is confirmed; the DP-buying half
  is not [INSIGHT:conviction_matrix].
- **`price-vs-flow`: `divergence = false`, "Price and flow are aligned",
  `flow_direction = "bearish"`, `price_change_pct = −30.37%`** — **no reversal
  signal** [INSIGHT:price_vs_flow].
- **ENPH absent from `signal-confluence` at `--min-score 1`, both directions**
  (returned top-20 saturated at scores 4–5; ENPH scores below 4)
  [INSIGHT:signal_confluence].
- **ENPH absent from `earnings-play` despite reporting in 1 day** — all 10
  qualifying names have `iv_rank = 100` vs ENPH's **69.81**
  [INSIGHT:earnings_play].
- **`analyst-vs-flow` returns no analyst block at all** — only the options-flow
  sub-object. No Wall Street consensus available [INSIGHT:analyst_vs_flow].

## Detailed findings

### Deep-dive snapshot

`uw insights deep-dive --symbol ENPH --date 2026-07-27` — four blocks returned.

**`uw_screener` (whole-tape directional aggregates):**

| Field | Value |
|---|---|
| `bullish_premium` | $1,843,847 |
| `bearish_premium` | **$2,102,578** |
| **derived `net_flow`** (`bullish − bearish`) | **−$258,731** |
| `call_premium` | $2,171,125 |
| `put_premium` | **$2,593,624** |
| `call_volume` / `put_volume` | 9,693 / 5,306 |
| `put_call_ratio` | 0.5474 |
| **`implied_move` / `implied_move_perc`** | **$4.65 / 12.25%** |
| `iv_rank` / `iv30d` | 69.81 / 0.9220 |
| `volatility` | 1.7258 |
| `total_open_interest` | 355,935 |
| `next_earnings_date` | **2026-07-28** |

✅ **Reconciles exactly** with `phase-1-flow.md`'s whole-tape aggregate and
`phase-0.5-context.md`'s `[CTX:]` block. `net_flow` **derived**, not read — the
block has no such key (`lib/uw-json-paths.md` trap #1) — and independently
confirmed against the screener parquet's `net_call_premium − net_put_premium` =
−$258,731 (exact match).

**`uw_dark_pool`:**

| Field | Value |
|---|---|
| `total_premium` | $11,876,368.54 |
| `total_shares` | 316,355 |
| `trade_count` | 38 |
| `avg_price` | $37.3489 |

✅ **Matches `phase-2-dark-pool.md`'s independent DuckDB aggregate to the cent**
(316,355 shares / $11.88M / 38 prints). Note `avg_price = $37.35` is **$0.66 below
the $38.01 close** — the day's dark-pool business was transacted materially below
where the stock finished.

**`uw_top_oi_changes`** — identical to `phase-3-positioning.md`:
`ENPH261120C00070000` +1,324 (vol 1,418, avg $1.4493),
`ENPH261016P00030000` +542 (vol 624, avg $2.5227),
`ENPH260821P00035000` +473 (vol 655, avg $2.5825),
`ENPH260918C00075000` +383 (vol 697, avg $0.2526),
`ENPH261120P00022500` +210 (avg $1.14).

**`yahoo_fundamentals`:**

```json
{"error":"yahoo quoteSummary ENPH: HTTP 401"}
```

⚠️ **Failed.** No P/E, market cap, short %, margins or balance-sheet data from
this path. Substitutes already in hand from other sources: market cap
**$4.837B** (screener parquet) / **$5.01B** (`fz`), **Short Float 17.94%**,
`Shs Float` **127.77M**, `Book/sh` **8.36**, `Cash/sh` **7.06**,
`Enterprise Value` **4.69B**, `Sales` **1.40B**, `Income` **135.00M**
(`phase-0-intake.md`). **Phase-7b must not rely on the deep-dive fundamentals
path** — it is unavailable for this ticker on this date.

### Signal confluence

`uw insights signal-confluence --direction bearish|bullish --min-score 1 --top-n 20`:

- **ENPH: absent from both directions.**
- Returned lists contain 20 rows each with `score` ranging **min 4, max 5** — the
  top-20 is saturated well above the requested `--min-score 1`, so **ENPH's
  confluence score is below 4** and it is crowded out of the ranking.
- Representative qualifying row (bearish): `AIQ` — `score = 5`,
  `factors = ["bearish_flow","high_pcr","volume_spike","dp_distribution",
  "high_iv_sell_premium"]`, `put_call_ratio = 8.71`, `iv_rank = 85.12`,
  `volume_ratio = 4.02`.

**This is a genuine and useful negative.** Per the phase-7 heuristic, *"signal
confluence ≥ 5 is rare and high-conviction"* — ENPH is not merely below that, it
fails to make a list that ENPH-adjacent bearish names populate. Compare AIQ's
profile with ENPH's: `put_call_ratio` 8.71 vs **0.55**, `volume_ratio` 4.02 vs
**0.57×** its own option average (`phase-0.5-context.md`). **ENPH's tape does not
exhibit the co-firing factors that constitute a real confluence signal.**

✅ Fully consistent with phase-0.5 (`outside top-50` on all five screener metrics),
phase-1 (`smart-money-flow` and `sweep-ratio` both empty for ENPH) and phase-2
(`ticker-summary` outside top-30). **Six independent rankings, six absences.**

### Conviction matrix

`uw insights conviction-matrix --symbol ENPH --date 2026-07-27`:

| Field | Value |
|---|---|
| **`scenario`** | **COVERED_CALL** |
| **`confidence_pct`** | **21.1** |
| `explanation` | *"Dark pool buying + call selling — yield enhancement, capping upside."* |
| `dark_pool.buy_ratio` | **0.686** |
| `dark_pool.buy_volume` / `sell_volume` | 216,974 / 99,381 |
| `dark_pool.trades` | 38 |
| `options_flow.call_ask_volume` / `call_bid_volume` | **4,196 / 4,635** |
| `options_flow.put_ask_volume` / `put_bid_volume` | **2,410 / 1,719** |
| `thresholds` | `bear 0.4`, `bull 0.6` |

**The scenario is half right, and the wrong half is the bullish half.**

- ✅ **"Call selling" — confirmed.** `call_ask 4,196` vs `call_bid 4,635` gives
  `call_ask_share = 0.475`, exactly the figure `phase-1-flow.md` derived
  independently from the screener parquet. Calls are net sold. Phase-3
  corroborates with the C70 build (`net_ask_bid = −1,407`, 99.5% bid-side) and the
  C75 build.
- ❌ **"Dark pool buying" — does not survive the closing cross.** See below.
- ⚠️ **Note what the explanation omits: puts are being bought.**
  `put_ask 2,410` vs `put_bid 1,719` → `put_ask_share = 0.584`. The `COVERED_CALL`
  label describes call selling but is silent on aggressive put buying. **Call
  selling + put buying is not "yield enhancement" — it is a collar or an outright
  bearish tilt.**

**`confidence_pct = 21.1` is the tool's own verdict on itself.** At 21% confidence
this classification should carry very little weight downstream regardless of the
critique above.

### Price vs flow

`uw insights price-vs-flow --symbol ENPH --lookback-days 30`:

| Field | Value |
|---|---|
| **`divergence`** | **false** |
| `divergence_signal` | **"Price and flow are aligned"** |
| `flow_direction` | **bearish** |
| `net_premium_flow` | −$258,731 |
| `bullish_premium` / `bearish_premium` | 1,843,847 / 2,102,578 |
| `price_start` → `price_end` | **54.59 → 38.01** |
| `price_change_pct` | **−30.37%** |
| `period_high` / `period_low` | **56.62 / 36.21** |
| `put_call_ratio` | 0.5474 |
| `iv_rank` | 69.81 |

**No divergence — and that is the more informative outcome.** The phase-7
heuristic treats divergence as a leading reversal signal; its **absence** means
there is no mean-reversion tell here. Bearish flow has accompanied a −30.37%
decline. Nothing is stretched; nothing is snapping back on positioning alone.

✅ `price_start 54.59 → price_end 38.01` and `−30.37%` reconcile exactly with
`phase-5-historical.md`'s `trend` output (`price_change: "54.59 -> 38.01"`, 30
sessions, 2026-06-12 → 2026-07-27).

**New datapoints not available upstream:** `period_high = 56.62` and
`period_low = 36.21`. The 30-day low of **$36.21** is a useful phase-9 reference —
it sits just below phase-2's most-transacted dark-pool level (**$36.70**, 9 trades)
and just above the $35 put wall. **The $35–36.70 zone is where three independent
methods place the floor.**

### Analyst vs flow

`uw insights analyst-vs-flow --symbol ENPH`:

```json
{"symbol":"ENPH",
 "options_flow":{"bullish_premium":1843847,"bearish_premium":2102578,
                 "net_flow":-258731,"put_call_ratio":0.5474...,
                 "flow_sentiment":"bearish"}}
```

⚠️ **The analyst block is entirely absent** — the payload contains only
`symbol` and `options_flow`. This matches the documented behaviour in
`lib/uw-json-paths.md` (*"analyst block can be empty/thin"*) and the phase-7
pitfall that consensus comes from yfinance — the same source that returned
**HTTP 401** for `yahoo_fundamentals` in the deep-dive above. **Both yfinance-backed
paths failed on this ticker today.**

**Consequence:** the Wall-Street-vs-options-traders comparison **cannot be made**
in this phase. `flow_sentiment = "bearish"` is simply phase-1's aggregate restated.
Note also that `fz`'s `Recom` and `Target Price` fields were **null** in the
degraded `fz quote` payload (`phase-0-intake.md`). **Analyst positioning is
unmeasured across all three available sources** — phase-7b must source it
independently or mark it `n/a`.

### Institutional accumulation — and its refutation

`uw insights institutional-accumulation --symbol ENPH`:

| Field | Value |
|---|---|
| **`signal`** | **"ACCUMULATION — dark pool buy volume significantly exceeds sell volume"** |
| **`buy_sell_ratio`** | **2.18** |
| `buy_side_volume` / `sell_side_volume` | **216,974 / 99,381** |
| `total_dp_volume` | 316,355 |
| `total_dp_premium` | $11,876,368.54 |
| `dark_pool_trades` | 38 |
| `vwap` | $37.54 |
| `avg_trade_price` | $37.35 |
| `price_30d_change_pct` | −30.37% |

**This is the single most bullish-sounding output produced anywhere in this run,
and it does not survive verification.**

Reproducing the classifier over the same 38 prints
(`dp-eod-report-2026-07-27.parquet`, `canceled = false`, above/below-mid):

| Basis | Buy vol | Sell vol | At mid | **`buy_ratio`** |
|---|---|---|---|---|
| All 38 prints, at-mid excluded from denominator | 210,432 | 99,381 | 6,542 | **0.679** |
| All 38 prints, **at-mid counted as buy** (UW's method) | **216,974** | **99,381** | — | **0.686** ✅ |
| **Excluding the 129,000-share closing cross** | — | — | — | **0.450** |

The middle row reproduces UW's `buy_volume = 216,974` and `sell_volume = 99,381`
**exactly** — 210,432 + 6,542 at-mid = 216,974 — so the method is confirmed and
the tool is doing what it says.

**But 129,000 of those 216,974 "buy" shares — 59.5% — are one print:** the
16:00:30 ET closing auction cross at $38.01 (`phase-2-dark-pool.md`). Remove that
single mechanical print and the buy ratio falls to **0.450**, i.e. **55% sell**,
flipping the signal from ACCUMULATION to mild **distribution**.

**Why the exclusion is the right call, not a convenient one:**

1. A closing auction cross aggregates every market-on-close order in the name. It
   is a **settlement mechanism**, not a directional institution expressing a view.
2. Its `trade_vs_mid = +0.07` is a mechanical consequence of printing at the
   official close, not evidence of a buyer paying up.
3. The same conclusion follows from an **entirely different classifier**:
   `phase-2-dark-pool.md`'s NBBO-based aggressor split gives **`hit% 20.3` vs
   `lift% 15.2`** today, with `hit% > lift%` in **4 of the last 6 sessions**.
4. Phase-2's `block-stratified` tier read reached it too: the only tier with a
   meaningful sample (large, **n = 36**) is `buy_ratio = 0.555` — barely above
   balanced — while the block tier's headline 0.817 rests on `trade_count = 2`.

**Four independent routes, one answer: there is no institutional accumulation in
ENPH today.** The `buy_sell_ratio = 2.18` should not be carried into phases 8, 8b
or 9.

Two genuine caveats in the tool's favour, recorded for fairness: `vwap = $37.54`
and `avg_trade_price = $37.35` both sit **below** the $38.01 close, so dark-pool
participants did transact at better-than-closing prices; and the tool correctly
reports `price_30d_change_pct = −30.37%` alongside its signal, so it is not
claiming the accumulation has worked.

### Earnings play

`uw insights earnings-play --days-until-earnings 30 --date 2026-07-27`:
**ENPH absent** (0 occurrences of the string in the payload). 10 results returned,
`days_to_earnings` ranging **2 to 23**.

| Ticker | `days_to_earnings` | `iv_rank` | `implied_move_perc` |
|---|---|---|---|
| SPCX | 8 | **100** | 7.95% |
| ECHO | 11 | **100** | 5.29% |
| KHC | 9 | **100** | 2.36% |
| QXO | 17 | **100** | 5.12% |
| TTMI | 9 | **100** | 20.79% |

**Not a tool error — an informative exclusion, for two reasons.** ENPH's
`days_to_earnings = 1` falls below the minimum of 2 in the returned set, and —
more tellingly — **every qualifying name carries `iv_rank = 100` while ENPH sits
at 69.81.**

✅ **This independently confirms the run's most counter-intuitive finding.** ENPH
reports tomorrow with a **12.25% implied move**, yet its IV rank is not extreme —
because, as `phase-0.5-context.md` established, `iv30d = 0.922` is only the
**54.8th percentile of ENPH's own distribution**. The name simply lives at ~90%
vol. UW's own earnings-play screen agrees: **on an IV-rank basis this is not a
notable earnings setup**, even though the event itself is large.

Note TTMI clears at a **20.79%** implied move — so a 12.25% implied move is not
extraordinary among earnings names, reinforcing phase-5's conclusion that ENPH's
event is **fairly priced rather than rich**.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw insights deep-dive --symbol ENPH --date 2026-07-27 --json` | `.uw_screener`: `bullish_premium=1843847`, `bearish_premium=2102578` (**derived `net_flow`=−258731**), `implied_move=4.65215`, `implied_move_perc=0.1224573`, `put_call_ratio=0.5474053`, `iv_rank=69.8119`, `total_open_interest=355935`, `next_earnings_date=2026-07-28`; `.uw_dark_pool`: `total_premium=11876368.539`, `total_shares=316355`, `trade_count=38`, `avg_price=37.3489`; `.yahoo_fundamentals`: **`{"error":"yahoo quoteSummary ENPH: HTTP 401"}`** | 1 |
| `uw insights signal-confluence --direction bearish --min-score 1 --top-n 20 --date 2026-07-27 --json` | ENPH **absent** ← `[.results[]\|select(.ticker=="ENPH")]` → `[]`; `[.results[].score]` → `min=4 max=5`, n=20 | top-20 |
| `uw insights signal-confluence --direction bullish --min-score 1 --top-n 20 --date 2026-07-27 --json` | ENPH **absent** ← same path → `[]` | top-20 |
| `uw insights conviction-matrix --symbol ENPH --date 2026-07-27 --json` | `scenario="COVERED_CALL"`, `confidence_pct=21.1`, `explanation="Dark pool buying + call selling — yield enhancement, capping upside."`, `dark_pool.buy_ratio=0.686`, `options_flow.call_ask_volume=4196`, `call_bid_volume=4635`, `put_ask_volume=2410`, `put_bid_volume=1719`, `thresholds={bear:0.4,bull:0.6}` | 1 |
| `uw insights price-vs-flow --symbol ENPH --lookback-days 30 --json` | `divergence=false`, `divergence_signal="Price and flow are aligned"`, `flow_direction="bearish"`, `net_premium_flow=-258731`, `price_start=54.59`, `price_end=38.0099983`, `price_change_pct=-30.37`, `period_high=56.62`, `period_low=36.21` | 1 |
| `uw insights analyst-vs-flow --symbol ENPH --json` | keys = `[symbol, options_flow]` only — **no analyst block**; `options_flow.flow_sentiment="bearish"` | 1 |
| `uw insights institutional-accumulation --symbol ENPH --json` | `signal="ACCUMULATION — dark pool buy volume significantly exceeds sell volume"`, `buy_sell_ratio=2.18`, `buy_side_volume=216974`, `sell_side_volume=99381`, `total_dp_volume=316355`, `vwap=37.54`, `avg_trade_price=37.35`, `price_30d_change_pct=-30.37` | 1 |
| `uw insights earnings-play --days-until-earnings 30 --date 2026-07-27 --json` | ENPH **absent** (`grep -c ENPH` → 0); n=10, `days_to_earnings` min=2 max=23, all `iv_rank=100`; TTMI `implied_move_perc=0.2079` | 10 |
| DuckDB reclassification, `dp-eod-report-2026-07-27.parquet` (ENPH, `canceled=false`) | above-mid `210,432` + at-mid `6,542` = **216,974** (reproduces UW exactly), below-mid `99,381`, `buy_ratio=0.679`; **excluding `size=129000`: `buy_ratio=0.450`** | 38 → 37 |

## Tool errors

Every `uw` command exited 0 and round-tripped through `jq`. **Three failures /
absences** recorded:

1. **`deep-dive.yahoo_fundamentals` → `{"error":"yahoo quoteSummary ENPH: HTTP 401"}`.**
   Verbatim. Yahoo's `quoteSummary` endpoint rejected the request (401 =
   unauthorized, the well-known yfinance cookie/crumb failure mode, not a
   paid-source gate). **No fundamentals available from this path.** Substitutes
   sourced from the screener parquet and `fz` (see Deep-dive snapshot).
   **Phase-7b must not depend on this path.**
2. **`analyst-vs-flow` returned no analyst block** — payload is `{symbol,
   options_flow}` only. Consistent with the documented thin/empty behaviour and
   with failure #1 (same yfinance backend). Combined with `fz quote`'s null
   `Recom` / `Target Price`, **analyst consensus is unavailable from all three
   sources this run.** Not fabricated; marked `n/a` and escalated to phase-7b.
3. **ENPH absent from `signal-confluence` (both directions) and `earnings-play`.**
   **Not errors** — genuine exclusions. Confluence: the top-20 saturates at scores
   4–5 and ENPH scores below 4. Earnings-play: ENPH's `days_to_earnings = 1` is
   below the returned minimum of 2, and all qualifying names carry `iv_rank = 100`
   vs ENPH's 69.81. Recorded as findings, per the phase-7 pitfall that an
   out-of-window `earnings-play` result is not a true error.

## Cross-check vs phases 1–6

| UW insight | Phase agreement? | Notes |
|---|---|---|
| **`signal_confluence`** (ENPH absent, both directions) | ✅ **agrees** with 0.5, 1, 2 | Sixth independent ranking to exclude ENPH (screener ×5, `smart-money-flow`, `sweep-ratio`, `ticker-summary`, `pin-risk`, `opex-concentration`). Confirms `[CTX:] BUSY_NAME_NORMAL_DAY`. |
| **`conviction_matrix`** = COVERED_CALL @ 21.1% | ⚠️ **half-agrees** | Call-selling leg ✅ matches phase-1 (`call_ask_share = 0.475`) and phase-3 (C70 `net_ask_bid = −1,407`). DP-buying leg ❌ refuted below. Label also omits the put buying (`put_ask_share = 0.584`). |
| **`institutional_accumulation`** = ACCUMULATION, ratio 2.18 | ❌ **DISAGREES with phase-2** | **Resolved against the tool.** Excluding the 129k closing cross, `buy_ratio` 0.679 → **0.450**. Phase-2's NBBO aggressor split (`hit 20.3%` > `lift 15.2%`) and `block-stratified` large tier (0.555, n=36) both agree with the corrected figure. |
| **`price_vs_flow`** = aligned bearish, −30.37% | ✅ **agrees** with 1, 5 | `price_start/end` and `price_change_pct` reproduce phase-5's `trend` exactly. No reversal signal. |
| **`deep_dive.uw_screener`** aggregates | ✅ **agrees** with 0.5, 1 | Every field matches phase-1's whole-tape table; derived `net_flow` = −258,731 confirmed against the parquet. |
| **`deep_dive.uw_dark_pool`** | ✅ **agrees** with 2 | 316,355 sh / $11.88M / 38 prints — identical to phase-2's DuckDB aggregate. |
| **`deep_dive.uw_top_oi_changes`** | ✅ **agrees** with 3 | Same five contracts, same `oi_diff_plain` values. |
| **`earnings_play`** (ENPH absent) | ✅ **agrees** with 0.5, 4, 5 | Confirms IV is not extreme *for this name* (`iv_rank 69.81` vs qualifying 100), matching the 54.8th self-percentile finding. |
| **`analyst_vs_flow`** (no analyst block) | ⚪ **n/a** | Cannot be cross-checked; escalated to phase-7b. |

**One material disagreement (`institutional_accumulation`), and it has been
adjudicated with primary data rather than left open.** Per the phase-7 goal
statement — this phase should agree with 1–5 and *"DISAGREE only when one of the
upstream phases was thin or wrong"* — here the disagreement runs the other way:
**the upstream phase was right and the composite is misled by a single mechanical
print.**

## DATA NOTE / CORRECTION

- **`net_flow` derived, not read** (`bullish_premium − bearish_premium` =
  −$258,731); `deep-dive .uw_screener` has no such key.
- **The DuckDB reclassification is a verification, not a new measurement.** It
  reproduces UW's own `buy_volume`/`sell_volume` **exactly** (216,974 / 99,381)
  before removing one print, so the 0.450 figure is directly comparable to the
  tool's 0.686 — same classifier, same data, one exclusion.
- **`price-vs-flow` `price_end = 38.0099983215332`** is float32 noise for $38.01;
  quoted as $38.01, consistent with the screener `close`.
- **Phase-2's verdict is *reinforced*, not corrected, by this phase.** Phase-2
  concluded "MIXED, leaning DISTRIBUTION"; the UW composite's contrary
  "ACCUMULATION" label has been traced to the closing cross that phase-2 had
  already isolated and flagged as mechanical. No prior number changes.
- **Standing correction from phase-3 remains in force:** phase-2's inference that
  the 800-lot Nov-20 $35 put was *bought* by a customer is **withdrawn**
  (OI moved 407 → 412). Nothing in phase-7 reinstates it.
- No value written in this phase was corrected after first read.

## Verdict for downstream phases

- **UW composite bias: WEAKLY BEARISH, LOW CONFIDENCE.** After removing the
  closing-cross artifact, the composites align with phases 1–6: calls sold, puts
  bought, price and flow aligned bearish, no divergence, no reversal signal, and
  ENPH excluded from every ranked screen. The two bullish-sounding labels
  (`COVERED_CALL`'s "dark pool buying", `ACCUMULATION`) reduce to **one mechanical
  print**.
- **Conviction: 2 / 5.** The direction is consistent across every surviving
  composite, but the magnitudes are small, `conviction-matrix` self-reports
  **21.1%** confidence, ENPH fails to score 4 on `signal-confluence`, and the two
  yfinance-backed tools returned nothing. **Low-information phase** — its main
  value is negative (what ENPH is *not*) and corrective (what the ACCUMULATION
  label is *not*).
- **Phase-9 should treat this as the BASELINE** — weakly bearish, low confidence —
  **and override only on specific contrary evidence.** The two items in this run
  that legitimately do so are **phase-4's armed vanna squeeze** (positive
  `net_vanna` + imminent 170% → ~90% IV crush) and **phase-6's Technology sector
  `persistence_score = 1` INFLOW**. Neither appears in any phase-7 composite,
  because none of these tools measures dealer-hedging mechanics or sector rotation.
- **Three things later phases must remember:**
  1. **`institutional-accumulation`'s "ACCUMULATION / 2.18" is refuted** —
     `buy_ratio` 0.679 → **0.450** once the 129,000-share closing cross is
     excluded, and three independent phase-2 measures agree. **Do not cite it as
     bullish evidence in phase-8, 8b or 9.**
  2. **ENPH is absent from *nine* separate ranked screens across the run**
     (5× `screener`, `smart-money-flow`, `sweep-ratio`, `ticker-summary`,
     `pin-risk`, `opex-concentration`, `signal-confluence` ×2, `earnings-play`).
     Whatever the direction, **the magnitude is not there** — this is the
     empirical backbone of the `BUSY_NAME_NORMAL_DAY` cap.
  3. **Analyst consensus is unavailable from all three sources**
     (`analyst-vs-flow` empty, `yahoo_fundamentals` HTTP 401, `fz quote` `Recom`
     and `Target Price` null). **Phase-7b must source it independently (WebSearch)
     or explicitly mark it `n/a`** — it must not be silently skipped, since
     analyst positioning into a binary is a real input.
- **Open questions:**
  - With `yahoo_fundamentals` returning HTTP 401 and `fz quote` degraded, can
    Finnhub supply the statements/surprise history — and specifically **ENPH's last
    four earnings-day moves**, still unanswered from phases 4, 5 and 6? → **phase-7b**
  - `conviction-matrix` labels the setup `COVERED_CALL` but ignores
    `put_ask_share = 0.584`. Is the real structure a **collar** (long stock +
    short calls + long puts), which would imply holders hedging rather than
    exiting? → **phase-7c / phase-8b**
  - `vwap = $37.54` and `avg_trade_price = $37.35` both sit below the $38.01
    close. Did institutions sell the close, or simply transact through a lower
    session range? → unresolved; low materiality
  - The 30-day low is **$36.21** and the most-transacted DP level **$36.70**, just
    above the **$35** put wall. Is $35–36.70 a real floor or merely where the
    stock has spent time on the way down? → **phase-8 / phase-9**
