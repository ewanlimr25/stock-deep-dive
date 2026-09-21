# Phase 5 — Historical Context & VRP

**Ticker:** ENPH
**As-of date:** 2026-07-27
**Generated:** 2026-07-27T21:08:00-04:00
**Upstream phases cited:** `phase-0-intake.md`, `phase-0.5-context.md`, `phase-1-flow.md`, `phase-3-positioning.md`, `phase-4-structure.md`

## Summary

**The short-gamma regime has a birthday and a body count.** `gex-time-series`
identifies exactly **one regime flip in 30 sessions — 2026-06-22, POSITIVE →
NEGATIVE at spot $53.40** — and ENPH has printed `FULLY_NEGATIVE` on essentially
every session since. Over that window the stock went **$53.40 → $38.01, −28.8%**.
The tool's own note (*"Empirically precedes realised-vol expansion"*) was
correct here, and it validates phase-4's regime read with 24 sessions of
out-of-sample evidence rather than one snapshot.

Vol is **rich but not extreme**: `vrp = +0.2566` (`iv30d 0.922` vs
`realised_vol 0.6655`), `regime = PREMIUM_SELLING` — yet `iv-percentile-zscore`
returns `iv_percentile = 54.79`, `iv_zscore = 0.352`, `regime = "NORMAL"`. Both
are true and the reconciliation is the point: **ENPH's implied vol is ordinary
for ENPH, and the premium over realized is the earnings event.**
`pc-ratio-zscore` finds `zscore = −0.037`, `extreme = "NORMAL"` — **no sentiment
extreme in either direction**, which independently kills any contrarian read.

The one genuine surprise is the **90-day cumulative premium flow: net
+$28,650,420 bullish** (`cumulative_bullish 435,331,447` vs `cumulative_bearish
406,681,027`, `trend_direction = "MIXED"`). Over the full window the tape has been
*net bullish* even as the stock halved — a direct counterpoint to phase-1's
five-session bearish campaign, and a warning that the recent bearish tilt is a
**three-week phenomenon, not a quarter-long one.**

Technically the name is broken but not yet washed out: `RSI = 36.13`, price below
**all three** moving averages (SMA20 −11.10%, SMA50 −25.53%, SMA200 −5.00%),
**−48.45% from the 52-week high** yet still **+47.47% above the 52-week low**.

**Sizing input: `bearish_flow` backtest `win_rate = 55.6%` on `total_signals = 9`
— below the 10-firing confidence floor, market-wide rather than ENPH-specific,
and self-described as *"In-sample backtest — not a robust live edge."***

## Key signals

- **Regime flip 2026-06-22 at $53.40; `FULLY_NEGATIVE` ever since; −28.8% over the
  span.** One flip in 30 sessions — a stable, not transitional, short-gamma
  regime [HIST:gex_time_series].
- **`vrp = +0.2566`, `regime = PREMIUM_SELLING`** (IV 92.2% vs RV 66.55%) — but
  `iv_percentile = 54.79`, `regime = "NORMAL"`, `dates_used = 73`
  [HIST:vrp], [HIST:iv_percentile_zscore].
- **90-day cumulative premium flow is net +$28.65M BULLISH**,
  `trend_direction = "MIXED"` — contradicts the 5-session bearish campaign
  [HIST:cumulative_premium_flow].
- **OI `overall_trend = "BUILDING"`, `consecutive_build_days = 6`,
  `total_net_oi_change = +187,280`** over 30 sessions [HIST:oi_trend].
- **`bearish_flow win_rate = 55.6%` on `n = 9`, `avg_move_pct = 0.48`** — thin
  edge, sub-threshold sample, in-sample [HIST:signal_backtest].
- **RSI 36.13; below SMA20/50/200; −48.45% from 52W high, +47.47% off 52W low;
  ATR 3.18 (8.4% of spot)** [HIST:rsi fz], [HIST:52w_proximity fz].

## Detailed findings

### IV regime (percentile + z-score + VRP)

`uw historical iv-percentile-zscore --symbol ENPH --lookback-days 252`:

| Field | Value |
|---|---|
| `current_iv30d` | 0.922 |
| `iv_percentile` | **54.79** |
| `iv_zscore` | 0.352 |
| **`dates_used`** | **73** |
| `lookback_days` (requested) | 252 |
| `regime` | **NORMAL** |

⚠️ **Gap-aware N (mandatory).** The requested 252-day lookback returned
`dates_used = 73`, not 252 — the local snapshot holds only 74 sessions total
(`phase-0-intake.md`) spanning **2026-03-13 → 2026-07-27 with a 21-session hole
at 2026-03-28 → 2026-04-24**. **This is a ~4.5-month percentile, not a 1-year
one.** The phase-5 pitfall about 1-year IV percentiles being misleading applies
with extra force: this window covers *only* the period during which ENPH
squeezed to $64 and then collapsed to $38, so the "median" it measures is drawn
entirely from an unusually violent stretch.

`iv_percentile = 54.79` reconciles exactly with phase-0.5's independent DuckDB
`self_pctile_iv30d = 54.8` — **two different code paths, same answer**, which is
a useful validation of both.

`uw historical vrp --symbol ENPH --realised-window-days 30`:

| Field | Value |
|---|---|
| `iv30d` | 0.9220 |
| `realised_vol` | 0.6655 |
| **`vrp`** | **+0.2566** |
| `regime` | **PREMIUM_SELLING** |
| `interpretation` | *"Options pricing more vol than realised — favour premium selling."* |

**The two tools appear to disagree and do not.** IV is at its *own* median
(54.79th percentile) while carrying a **+25.7 vol-point premium to realized**.
Both hold because ENPH's realized vol (66.55%) is running *below* its structural
implied level (~86–92%, `phase-4-structure.md`). The VRP is not a mispricing to
harvest — **it is the earnings event, and it is 24 hours away.**

**Do not act on `PREMIUM_SELLING` naively.** The heuristic (*IV rich + VRP > 0 →
favour credit structures*) is the correct general rule and the **wrong** rule
here: selling premium into a confirmed binary with a **12.25% implied move** and
a `FULLY_NEGATIVE` gamma surface is selling a lottery ticket the day before the
draw. The VRP is compensation for event risk, not excess. Phase-3 already showed
who is taking that trade — the C70/C75/P35/P30 sellers — and they are selling the
**wings at 116 and 53 DTE**, not the front week. That distinction is the whole
craft: **the +0.2566 VRP is harvestable in the back months, not in 2026-07-31.**

**Is the 12.25% implied move rich or cheap?** (phase-4's handoff question)

| Reference | Value |
|---|---|
| Implied one-day move | **12.25%** (±$4.65) |
| ATR (14) | **3.18** = **8.4%** of $38.01 |
| Implied move ÷ ATR | **1.46×** |
| RV30 (annualized) | 66.55% → **4.19%** daily-equivalent |
| Implied move ÷ daily RV | **2.92×** |
| Recent realized daily moves | −6.74%, −5.63%, −5.08%, +4.47%, +4.35%, +3.95%, +3.57% |

A 12.25% expectation is **~1.5× the stock's average true range** and **~2.9× its
recent daily realized move**. On a name that routinely prints 5–7% *without* a
catalyst, that is a **modest** event premium. Preliminary verdict:
**fairly priced to slightly cheap — certainly not the giveaway that "170% IV"
suggests at first glance.** The 170.1% front-week number is what a 12.25% move
over 4 DTE *has* to annualize to; it is arithmetic, not richness.

### Cumulative premium flow

`uw historical cumulative-premium-flow --symbol ENPH --days 90`:

| Field | Value |
|---|---|
| `cumulative_bullish` | $435,331,447 |
| `cumulative_bearish` | $406,681,027 |
| **`net_flow`** | **+$28,650,420** |
| `trend_direction` | **MIXED** |
| `days` (requested) | 90 |
| **`dates_covered` length** | **74** |

⚠️ **Gap caveat:** `--days 90` returned **74 sessions**, spanning
**2026-03-13 → 2026-07-27** — i.e. the *entire* local snapshot, **including the
21-session hole**. This is a 74-session read across ~4.5 calendar months, not a
90-session read. Do not annualize it.

**This is the most important counter-signal in the phase.** Across 74 sessions the
options tape has been **net bullish by $28.7M** — while the stock fell from the
$46–64 range to $38.01. Three honest readings:

1. **Most of that bullish premium was accumulated during the May squeeze**, when
   ENPH ran $46.83 → $64.03 in three sessions (`phase-0.5-context.md`). It is
   history, and it was *wrong*.
2. **`trend_direction = "MIXED"` is the tool's own verdict** — it explicitly
   declines to call this a directional build. Per the phase-5 heuristic, a stealth
   institutional build requires *"cumulative premium flow + and persistent ≥ 60d"*;
   **`MIXED` fails the persistence test**, so this does **not** qualify as a
   bullish confirmation.
3. **Net +$28.7M on $842M of gross two-way premium is a 3.4% tilt** — statistically
   near-balanced.

**Correct use downstream:** this does *not* argue bullish. It argues that
phase-1's five-session bearish campaign is **recent and narrow**, and that anyone
sizing off "the flow has been bearish" should know the quarter-long tape is
essentially flat. It caps bearish conviction; it does not create bullish conviction.

### P/C ratio z-score

`uw historical pc-ratio-zscore --symbol ENPH --lookback-days 20`:

| Field | Value |
|---|---|
| `current_pc_ratio` | 0.5474 |
| `mean_pc_ratio` | 0.5602 |
| `std_pc_ratio` | 0.3485 |
| **`zscore`** | **−0.037** |
| `extreme` | **NORMAL** |

**Today's P/C ratio is 0.04 standard deviations from its own 20-day mean** — as
close to unremarkable as a reading can be. The phase-5 contrarian heuristic
(`|z| > 2`) is nowhere near satisfied.

This independently confirms phase-1's warning that `put_call_ratio = 0.547` is a
**bull trap**: not only does the ask/bid split show those calls being *sold*, the
ratio itself is **exactly average for ENPH** (0.5474 vs a 0.5602 mean). There is
no information in it at all. Note also `std = 0.3485` on a `mean = 0.5602` — a 62%
coefficient of variation, so ENPH's P/C is intrinsically noisy and **z-scores on
it will rarely be significant.** Treat this tool as uninformative for this name.

### GEX time series

`uw historical gex-time-series --symbol ENPH --days 30 --dte-max 45`
(`days_analyzed = 30`, `note`: *"Regime flips identify dates where spot crossed
the zero-gamma level. Empirically precedes realised-vol expansion."*):

**`regime_flip_dates` — exactly one in 30 sessions:**

| Date | From | To | Spot | ZGL | `zgl_delta` |
|---|---|---|---|---|---|
| **2026-06-22** | POSITIVE | **NEGATIVE** | **53.40** | 74.39 | 54.39 |

**Trajectory (recent sessions):**

| Date | Regime | Spot | ZGL | `total_gex` |
|---|---|---|---|---|
| 2026-06-12 | POSITIVE | 54.25 | 29.02 | +7,755,175 |
| 2026-07-08 | FULLY_NEGATIVE | 42.34 | null | −2,637,888 |
| 2026-07-09 | FULLY_NEGATIVE | 45.06 | null | −1,863,384 |
| 2026-07-10 | FULLY_NEGATIVE | 45.14 | null | −687,297 |
| 2026-07-13 | FULLY_NEGATIVE | 42.93 | null | −2,182,459 |
| 2026-07-14 | FULLY_NEGATIVE | 44.84 | null | −875,738 |
| 2026-07-15 | ⚠️ POSITIVE | 43.72 | 20.04 | **−1,216,059** |
| **2026-07-16** | FULLY_NEGATIVE | 41.29 | null | **−4,361,654** |
| 2026-07-17 | FULLY_NEGATIVE | 41.63 | null | −2,613,239 |
| 2026-07-20 | FULLY_NEGATIVE | 39.73 | null | −763,473 |
| 2026-07-21 | FULLY_NEGATIVE | 40.11 | null | −483,746 |
| 2026-07-22 | FULLY_NEGATIVE | 40.07 | null | −817,890 |
| 2026-07-23 | FULLY_NEGATIVE | 38.48 | null | −1,622,027 |
| 2026-07-24 | FULLY_NEGATIVE | 37.05 | null | −2,199,041 |
| **2026-07-27** | FULLY_NEGATIVE | 37.52 | null | **−566,158** |

**Three findings:**

1. **The regime is stable, not transitional.** One flip in 30 sessions, 24
   sessions ago. The phase-5 heuristic (*"GEX regime flip in last 5d → dealer
   hedging in transition"*) **does not fire** — this is a settled short-gamma
   regime, which makes phase-4's read more reliable, not less.
2. **The flip preceded the decline, exactly as the tool's note predicts.** Spot
   was **$53.40** on the flip date and is **$38.01** today: **−28.8% in 24
   sessions** under continuous negative gamma. The worst single GEX print
   (**−4,361,654** on 2026-07-16) coincides with the worst single day in
   phase-0.5's table (**−6.74%**, P/C 1.537, net flow −$4.43M). **Gamma
   amplification is not a theory in this name; it is the observed mechanism.**
3. **Today is the *least* negative print in a fortnight** (−566,158 vs −2,199,041
   yesterday and −4,361,654 on 07-16). Consistent with phase-4's finding that the
   2026-07-31 expiry is a positive-gamma island (`today_total_gex = +1,047,168`)
   partially offsetting the put-heavy book. **That cushion expires in 4 days.**

⚠️ The **2026-07-15** row is internally inconsistent — `regime = "POSITIVE"` with
`total_gex = −1,216,059` and a ZGL of 20.04 far below spot 43.72. This is the same
class of labeling defect phase-4 flagged in `today-gamma-flip`. Treated as a
mislabel, not a genuine one-day regime change; it does not appear in
`regime_flip_dates`, which supports that reading.

### OI trend

`uw historical oi-trend --symbol ENPH --days 30 --top-n 10`:

| Field | Value |
|---|---|
| `overall_trend` | **BUILDING** |
| `consecutive_build_days` | **6** |
| `total_net_oi_change` | **+187,280** |
| `days_analyzed` | 30 |

**Daily detail:**

| Date | `net_oi_change` | Increases | Decreases |
|---|---|---|---|
| 2026-07-27 | +6,341 | 279 | 65 |
| 2026-07-24 | +1,153 | 268 | 119 |
| 2026-07-23 | +2,114 | 191 | 79 |
| 2026-07-22 | +2,687 | 227 | 68 |
| 2026-07-21 | +8,315 | 315 | 83 |
| 2026-07-20 | **+12,748** | 238 | 69 |
| 2026-07-17 | −2,771 | 212 | 125 |
| 2026-07-16 | +575 | 200 | 94 |
| 2026-07-15 | +3,868 | 229 | 75 |
| 2026-07-14 | +5,091 | 252 | 82 |
| 2026-07-13 | +4,647 | 172 | 84 |
| 2026-07-10 | +288 | 210 | 130 |

**This is the phase's second major finding and it resolves a phase-0.5 question.**
Phase-0.5 asked why option volume sat at the 16.4th self-percentile on earnings
eve — genuine disinterest, or positioning already established? **`oi-trend`
answers: already established.** OI has risen on **6 consecutive sessions** and by
**+187,280 contracts over 30 days** — against a `term-structure` total of
241,974 (`phase-3-positioning.md`), i.e. the book has roughly **doubled in a
month**. Today alone, **279 contracts gained OI vs 65 that lost**.

So the correct characterisation is **not** "nobody cares about this event". It is
**"the book was built over the last month, and today was just the quiet last day
before it pays off or doesn't."** That materially changes the read on phase-1's
thin tape: low volume on earnings eve is the *absence of late repositioning*, not
the absence of positioning.

⚠️ **Note the tension with phase-3**, which found only **2** contracts moving OI by
≥500 today. Both are true: today's build was **broad and shallow** (279 contracts
up, net +6,341, average ~+23 contracts each) rather than concentrated. Phase-3's
≥500 threshold is simply blind to a diffuse build. **Neither phase is wrong; the
threshold is doing the work.** Phase-10 should not log this as a contradiction.

### Multi-day trend

`uw historical trend --symbol ENPH --days 30`:

| Field | Value |
|---|---|
| `days_analyzed` | **30** |
| `date_range` | **2026-06-12 to 2026-07-27** |
| `bullish_days` | 11 |
| `bearish_days` | **19** |
| `price_change` | **54.59 → 38.01** (**−30.4%**) |
| `iv_rank_change` | 55.27 → 69.81 |
| `flow_direction_latest` | **bearish** |

✅ **Gap check passed:** the window 2026-06-12 → 2026-07-27 is **entirely after**
the 2026-03-28 → 2026-04-24 hole, and `days_analyzed = 30` matches the 30 trading
sessions in that range. **This is a genuinely contiguous 30-session read** — the
only major lookback in this phase that is gap-free, and therefore the one to
trust most.

**19 bearish days vs 11 bullish (63% bearish) with a −30.4% price change.** Note
`iv_rank` *rose* (55.27 → 69.81) as price fell — the standard spot-down/vol-up
relationship, and further evidence that the flat 25Δ skew phase-4 found
(`skew_ratio = 1.001`) is anomalous: vol responded to the decline, but **skew did
not.**

### Price context (`fz`, advisory)

`fz screen --view technical --tickers ENPH --agent` — used because
`fz quote --agent` is degraded to 14 fields on this ticker (`phase-0-intake.md`
§Tool errors) and returns no RSI/SMA/52W data:

| Field | Value | Implied level |
|---|---|---|
| Price | 38.01 | — |
| **RSI (14)** | **36.13** | not yet oversold (<30) |
| **SMA20** | **−11.10%** | ≈ **$42.76** |
| **SMA50** | **−25.53%** | ≈ **$51.04** |
| **SMA200** | **−5.00%** | ≈ **$40.01** |
| 52W High | **−48.45%** | $73.74 |
| 52W Low | **+47.47%** | $25.78 |
| ATR | **3.18** | **8.4%** of spot |
| Beta | 1.65 | — |
| Change | +3.57% | — |
| Gap | +2.57% | — |
| Change from Open | +0.97% | — |

**Two observations worth carrying forward.**

**1. The moving averages land on the option levels.** SMA200 ≈ **$40.01** sits
essentially *on* the $40 strike that phase-3 identified as `put_heavy` (8,444
puts), phase-4 identified as the **most negative GEX strike** (−1,112,908), and
`max-pain` identified as the **modal magnet across 8 of 15 expiries**. SMA20 ≈
**$42.76** sits essentially *on* the **$42.50 call wall** (3,735 calls / zero
puts; largest positive gamma at +703,006). **Four independent methods — moving
averages, OI walls, gamma, and max pain — agree on the same two levels.** That is
the strongest confluence produced anywhere in this run, and phase-9 should build
its levels on it.

**2. Today's +3.57% was a gap that merely held.** `Gap = +2.57%` and
`Change from Open = +0.97%` — roughly **72% of the day's gain was the opening
gap**, with only modest follow-through, on **0.59× average share volume**
(`phase-0.5-context.md`). This corroborates phase-1's refusal to score the green
candle as demand.

RSI **36.13** with price below all three SMAs is an unambiguous downtrend, but
**not** an oversold-bounce setup — 36 is weak, not washed out. Per the phase
guidance this is **advisory only**: it enters no Kelly `p` and no sizing block.

### Signal backtest

Run with `--signal-type bearish_flow`, matching phase-1's verdict
(`Bias from this phase: bearish`) and phase-2's *"MIXED, leaning DISTRIBUTION"*:

`uw historical signal-backtest --signal-type bearish_flow --lookback-days 5 --top-n 20`:

| Field | Value |
|---|---|
| `signal_type` | bearish_flow |
| **`win_rate`** | **"55.6%"** (returned as a **string**) |
| **`total_signals`** | **9** |
| `truncated_signals` | 9 |
| `avg_move_pct` | **0.48** |
| `lookback_days` | 5 |
| `methodology_notes` | *"win_rate = fraction of signals where forward move agrees with the signal's direction. Lookback is in TRADING days; selection is positional within the yfinance bar series. **In-sample backtest — not a robust live edge.**"* |

Constituent tickers: TSLA, LULU, GOOGL, GLD, QQQ, SPY, META, MSFT (+1).

**Four disqualifiers on this number, all of which phase-9 must respect:**

1. **`total_signals = 9` is below the phase-5 confidence floor** (*"treat <10
   historical firings as low-confidence"*). At n=9, 55.6% means **5 wins out of
   9**. The 95% confidence interval on 5/9 spans roughly **27%–81%** — it does not
   exclude a coin flip, or a losing signal.
2. **It is market-wide, not ENPH-specific.** The tool takes no `--symbol`, and the
   constituents are mega-caps and index ETFs. **`p` is the base rate of the
   `bearish_flow` signal class across the tape, not ENPH's rate.**
3. **`avg_move_pct = 0.48`** — even when the signal "wins," the average forward
   move is **0.48%**. Against ENPH's **8.4% ATR** and a **12.25% implied move**,
   this edge is economically invisible.
4. **The tool disowns itself**: *"In-sample backtest — not a robust live edge."*

Per the composition guidance, a **single re-run** was not required — the result is
populated, not the `{"note":"no backtest results","total_signals":0}` stub — so
`win_rate_source = backtest` is recorded, with the caveats above attached.

**Phase-5 heuristic check:** *"win_rate < 0.45 → downgrade conviction."* At 0.556
this does **not** trigger a downgrade — but neither does it earn an upgrade. The
honest reading is **no measurable edge either way**, and phase-9 should lean on
the N-conditional cap in `rubrics/sizing-rubric.md` rather than the raw 0.556.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows / N |
|---|---|---|
| `uw historical iv-percentile-zscore --symbol ENPH --lookback-days 252 --json` | `iv_percentile=54.79`, `iv_zscore=0.352`, `current_iv30d=0.922`, **`dates_used=73`**, `regime="NORMAL"` | N=73 (≠252) |
| `uw historical vrp --symbol ENPH --realised-window-days 30 --json` | `vrp=0.2566`, `iv30d=0.922`, `realised_vol=0.6655`, `regime="PREMIUM_SELLING"`, `interpretation="Options pricing more vol than realised…"` | 1 |
| `uw historical pc-ratio-zscore --symbol ENPH --lookback-days 20 --json` | `zscore=-0.037`, `extreme="NORMAL"`, `current_pc_ratio=0.5474`, `mean_pc_ratio=0.5602`, `std_pc_ratio=0.3485` | N=20 |
| `uw historical cumulative-premium-flow --symbol ENPH --days 90 --json` | `cumulative_bullish=435331447`, `cumulative_bearish=406681027`, `net_flow=28650420`, `trend_direction="MIXED"`, **`dates_covered\|length=74`** (≠90) | N=74 |
| `uw historical gex-time-series --symbol ENPH --days 30 --dte-max 45 --json` | `regime_flip_dates=[{date:"2026-06-22", from_regime:"POSITIVE", to_regime:"NEGATIVE", spot:53.4, zero_gamma_level:74.39, zgl_delta:54.39}]` (**exactly 1**); `trajectory[-1]={date:"2026-07-27", regime:"FULLY_NEGATIVE", spot:37.52, total_gex:-566158, zero_gamma_level:null}`; min `total_gex=-4361654` @ 2026-07-16 | N=30 |
| `uw historical oi-trend --symbol ENPH --days 30 --top-n 10 --json` | `overall_trend="BUILDING"`, `consecutive_build_days=6`, `total_net_oi_change=187280`, `days_analyzed=30`; 2026-07-27 `net_oi_change=6341 contracts_with_increases=279 contracts_with_decreases=65` ← `.daily_data[]` | N=30 |
| `uw historical trend --symbol ENPH --days 30 --json` | `days_analyzed=30`, `date_range="2026-06-12 to 2026-07-27"`, `bullish_days=11`, `bearish_days=19`, `price_change="54.59 -> 38.01"`, `iv_rank_change="55.2711 -> 69.8119"`, `flow_direction_latest="bearish"` | N=30 |
| `uw historical signal-backtest --signal-type bearish_flow --lookback-days 5 --top-n 20 --json` | **`win_rate="55.6%"`**, **`total_signals=9`**, `truncated_signals=9`, `avg_move_pct=0.48`, `methodology_notes="…In-sample backtest — not a robust live edge."` | N=9 (market-wide) |
| `fz screen --view technical --tickers ENPH --agent` | `RSI="36.13"`, `SMA20="-11.10%"`, `SMA50="-25.53%"`, `SMA200="-5.00%"`, `"52W High"="-48.45%"`, `"52W Low"="47.47%"`, `ATR="3.18"`, `Beta="1.65"`, `Gap="2.57%"`, `"Change from Open"="0.97%"` ← `.[0]` | 1 |

## Tool errors

No command errored; all exited 0 and round-tripped through `jq`. **Five
data-quality items** surfaced:

1. **`fz quote ENPH --agent` remains degraded** (14 of 84 fields; carried from
   `phase-0-intake.md`), so the phase-5 D8 recipe — which reads
   `.fundamentals."RSI (14)"`, `.SMA50`, `.SMA200`, `"Perf YTD"`, `"52W High/Low"`
   — **returns all-null on this ticker.** *Recovery:* `fz screen --view technical
   --tickers ENPH --agent` supplies RSI/SMA20/SMA50/SMA200/52W/ATR/Beta intact.
   *Propose-only note for the skill:* `phases/phase-5-historical.md` §D8 should
   fall back to the technical screen view when `fz quote` returns a partial payload.
   Note the screen view expresses SMAs as **% distance**, not price levels — the
   implied levels in the table above are my arithmetic, flagged as derived.
2. **`--lookback-days 252` silently returned `dates_used = 73`.** Not an error —
   the tool correctly reports its true N — but **any consumer reading "252-day IV
   percentile" would be wrong by 3.5×.** Quoted as a 73-session percentile
   throughout.
3. **`--days 90` on `cumulative-premium-flow` returned 74 sessions spanning the
   21-session hole.** The returned `dates_covered` array was inspected explicitly
   rather than trusting the `days: 90` echo. The series **does** span the gap, so
   per the mandatory gap rule it is **not** annualized and is quoted as a
   74-session total.
4. **`gex-time-series` 2026-07-15 row mislabels `regime = "POSITIVE"` with
   `total_gex = −1,216,059`.** Same defect class as phase-4's `today-gamma-flip`
   inconsistency. Not counted as a regime change (it is absent from
   `regime_flip_dates`). Flagged for phase-10 as a recurring tool-labeling issue.
5. **`signal-backtest` returns `win_rate` as a string (`"55.6%"`), not a float.**
   Converted to `0.556` for the sizing block; the raw string is preserved in the
   audit row above. Phase-9 must not attempt arithmetic on the raw field.

**Latest-anchor caveat (mandatory).** Every tool in this phase except `trend`'s
date range takes **no `--date`** and anchors to the **latest available date**,
which for this run is **2026-07-27 — identical to the as-of date**, so no
stale-window substitution occurred. **However, ENPH reports tomorrow after the
close.** A re-run on or after 2026-07-29 will shift *every* trailing read here —
`iv30d`, `vrp`, `iv_percentile`, `realised_vol`, GEX trajectory, OI build days and
the win-rate — because a ±12.25% gap will enter each window. **These figures are
reproducible only against a 2026-07-27 anchor.**

## DATA NOTE / CORRECTION

- **`win_rate` converted from `"55.6%"` → `0.556`** for the sizing handoff. Raw
  string preserved above.
- **SMA price levels are derived, not returned.** `fz` gives % distance; the
  levels ($42.76 / $51.04 / $40.01) are computed as `38.01 ÷ (1 + pct)`. The
  **percentages** are the datapoints; the levels are my arithmetic and are
  approximate (Finviz rounds to 2dp).
- **`iv_percentile = 54.79` cross-validates phase-0.5's DuckDB
  `self_pctile_iv30d = 54.8`** — two independent paths, matching to 0.01. No
  correction needed; recorded as a positive validation.
- **The phase-3 tension is explained, not corrected.** Phase-3's "only 2 OI builds
  ≥500" and phase-5's "+187,280 over 30 days / 279 contracts up today" are both
  accurate; the `--min-oi-change 500` filter cannot see a broad shallow build.
  Recorded so phase-10 does not log a false contradiction.
- **No value written in this phase was corrected after first read.**

## Verdict for downstream phases

- **Volatility regime:** **RICH vs realized, NORMAL vs its own history — and the
  richness is entirely the event.** `vrp = +0.2566` with `regime = PREMIUM_SELLING`,
  but `iv_percentile = 54.79` / `regime = "NORMAL"` (N=73). The 12.25% implied move
  is only **1.46× ATR** and **2.9× daily realized** on a stock that prints 5–7%
  days unprompted: **fairly priced, arguably slightly cheap.**
- **Premium environment:** **SELL THE WINGS, NOT THE EVENT.** The +25.7-point VRP
  is harvestable in the ~86% back months (which is exactly what phase-3's C70/C75/
  P35/P30 sellers are doing), and is **not** harvestable in the 2026-07-31 expiry,
  where 170.1% IV is the fair price of a binary under a `FULLY_NEGATIVE` gamma
  surface. Combined with phase-4's **`skew_ratio = 1.001` / COMPLACENT**, the
  structuring conclusion is specific: **buy front-week convexity outright if you
  want direction; sell back-month wings if you want carry; never the reverse.**
- **Conviction that today's signal is HISTORICALLY EDGE-POSITIVE: 2 / 5.**
  The `bearish_flow` backtest is **55.6% on n=9** (below the 10-firing floor,
  market-wide, in-sample, `avg_move_pct` 0.48%) — it neither confirms nor refutes.
  What *does* carry real weight is the **regime evidence**: 24 sessions of
  continuous `FULLY_NEGATIVE` gamma delivering **−28.8%** since the 2026-06-22
  flip, and **19 of 30 sessions bearish**. That is a persistent, mechanical,
  observed edge — but it is a *regime* fact, not a *signal-backtest* fact, and it
  must not be laundered into the Kelly `p`. Held to 2/5 because the 74-session
  cumulative flow is **net +$28.7M bullish / `MIXED`**, which directly caps how
  much the three-week bearish tape can be extrapolated.
- **Three specific datapoints:**
  1. **IV percentile: `54.79`** (`iv_zscore 0.352`, `regime "NORMAL"`, **N=73 not 252**)
  2. **VRP: `+0.2566`** (`iv30d 0.922` − `realised_vol 0.6655`, `regime "PREMIUM_SELLING"`)
  3. **Signal win rate: `55.6%` on `n=9`** (`avg_move_pct 0.48`, market-wide, in-sample)
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:              bearish_flow
  signal_backtest_win_rate:  0.556
  win_rate_n:                9
  win_rate_source:           backtest
  ```
  ⚠️ **`win_rate_n = 9 < 10`** — below the phase-5 low-confidence floor. The rate is
  a **market-wide base rate for the `bearish_flow` signal class**, NOT an
  ENPH-specific rate (the tool takes no `--symbol`), and the tool self-describes as
  *"In-sample backtest — not a robust live edge."* Phase-9 **must** apply the
  N-conditional cap in `rubrics/sizing-rubric.md` §"Choosing the Kelly `p`" and
  should treat 0.556 as indistinguishable from 0.50.
- **Three things later phases must remember:**
  1. **The short-gamma regime began 2026-06-22 at $53.40 and has delivered −28.8%
     over 24 sessions with only one flip in 30.** This is the single best-evidenced
     mechanism in the entire run — phase-4's snapshot regime is confirmed
     longitudinally. It also means the regime is **stable, not transitional**: no
     flip in the last 5 days, so expect continued trend amplification rather than
     a hedging-dynamics change.
  2. **Positioning was built over the past month, not today.** `overall_trend =
     "BUILDING"`, **6 consecutive build days**, **+187,280 contracts in 30 sessions**
     (~doubling the book), **279 contracts up vs 65 down today**. Phase-0.5's
     16.4th-percentile option volume means *no late repositioning*, **not** market
     indifference to the event. Correct any downstream phase that reads the quiet
     tape as apathy.
  3. **Four independent methods agree on two levels: $40 and $42.50.**
     SMA200 ≈ **$40.01** = the `put_heavy` strike (8,444 puts) = the most negative
     GEX strike (−1,112,908) = the modal max-pain magnet (8 of 15 expiries).
     SMA20 ≈ **$42.76** ≈ the **$42.50** call wall (3,735 calls / 0 puts) = the
     largest positive gamma (+703,006). **Phase-9 should anchor its levels here.**
     Counterweight to remember: **74-session cumulative premium flow is net
     +$28.65M BULLISH with `trend_direction = "MIXED"`** — the bearish tape is
     three weeks old, not three months.
- **Open questions:**
  - **How large were ENPH's actual last four earnings-day moves?** Phase-4 asked and
    phase-5 cannot answer: the local snapshot is 74 sessions and contains **no prior
    ENPH earnings date**. If historical gaps exceed 12.25%, the front week is cheap.
    → **phase-7b** (Finnhub surprise history / WebSearch)
  - The 74-session tape is net **+$28.7M bullish** while the last 5 sessions are
    firmly bearish. Which window should phase-9 weight — and does the
    2026-06-22 gamma flip mark the regime break that makes the older data
    irrelevant? → **phase-8b**
  - `vrp = +0.2566` says sell premium; `FULLY_NEGATIVE` gamma + a 12.25% binary says
    do not. Is there a structure that is long the front-week convexity and short the
    back-month wings? → **phase-9**
  - RSI 36.13 is weak but **not** oversold, and price is **+47.47% above the 52-week
    low**. How much downside remains before value buyers appear? → **phase-7b**
