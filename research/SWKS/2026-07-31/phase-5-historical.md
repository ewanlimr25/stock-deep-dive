# Phase 5 — Historical Context & VRP

**Ticker:** SWKS
**As-of date:** 2026-07-31
**Generated:** 2026-08-02
**Upstream phases cited:** `phase-0-intake.md`, `phase-0.5-context.md`, `phase-1-flow.md`, `phase-2-dark-pool.md`, `phase-3-positioning.md`, `phase-4-structure.md`

## Summary

SWKS options are **cheap in level terms and getting cheaper against what the stock
is actually doing**. `iv-percentile-zscore` returns `iv_percentile` **40.26** with
`iv_zscore` **−0.219** (`regime: "NORMAL"`), and `phase-0.5-context.md` put the same
IV rank at the **29.9th percentile of the name's own history**. The tool-level VRP
reads **+0.0663 (`regime: "PREMIUM_SELLING"`)** — IV30 55.90% vs 30-day realized
49.27% — **but that 30-day window is stale**, and the phase's own pitfall
("*read the trailing-5d trend, not just today*") resolves it decisively: realized
vol over the trailing 10 sessions is **55.53%** and over the trailing 5 sessions is
**63.49%**, i.e. **realized has crossed above implied** and the true near-term VRP
is roughly **−7.6 vol points — a premium-BUYING regime.** Dealers have been
**short gamma for 29 of the last 30 sessions** (single regime flip 2026-06-22 at
spot 76.26), and price has fallen **−14.0% over those 30 sessions (72.45 → 62.28)**
with a tested floor at **$56.91–57.50** hit three separate times. The one sentiment
extreme is `pc-ratio-zscore` at **z = +2.557, `extreme: "BEARISH_EXTREME"`**.
**Crucially, the sizing handoff is null:** the `dark_pool_accumulation` backtest —
the signal class matching phase 2's dominant finding — returns
`{"note":"no backtest results","total_signals":0}` on **two** runs, so phase 9 must
fall back to the conviction bin rather than an empirical Kelly `p`.

## Key signals

- **VRP flips sign on the tradeable horizon.** Tool: `vrp = +0.0663`,
  `regime: "PREMIUM_SELLING"` (IV30 0.559 vs realized-30d 0.4927). Recomputed on
  the same closes: realized **30d 49.26% → 10d 55.53% → 5d 63.49%**, against a
  falling `iv30d` (0.741 → 0.559). **Near-term VRP ≈ −7.6 points.** `[HIST:vrp]` `[HIST:realized_decomp DUCKDB]`
- **IV is genuinely cheap:** `iv_percentile` **40.26**, `iv_zscore` **−0.219**,
  `regime` **NORMAL**, `current_iv30d` 0.559 (`dates_used` **77**, not 252).
  `[HIST:iv_percentile_zscore]`
- **P/C ratio at a 2.6-sigma extreme:** `current_pc_ratio` **4.0593** vs
  `mean_pc_ratio` 1.0798, `std_pc_ratio` 1.1652 ⇒ **`zscore` +2.557**,
  `extreme: "BEARISH_EXTREME"`. `[HIST:pc_ratio_zscore]`
- **Short gamma is the persistent regime, not today's condition:** `gex-time-series`
  shows **NEGATIVE or FULLY_NEGATIVE on 29 of 30 sessions**, with exactly **one
  `regime_flip_date` — 2026-06-22, POSITIVE → NEGATIVE at spot 76.26**. `[HIST:gex_time_series]`
- **OI is `BUILDING` on paper but the build is stale:** `overall_trend: "BUILDING"`,
  `consecutive_build_days` **11**, `total_net_oi_change` **+51,001** over 30 days —
  yet **+26,690 of it landed on a single day (2026-06-23)** and the as-of day added
  only **+199**. `[HIST:oi_trend]`
- **Sizing input is unavailable.** `signal-backtest --signal-type
  dark_pool_accumulation` → `total_signals: 0` (twice). The populated alternatives
  are market-wide and unusable: `bullish_flow` **win_rate "100.0%" on N=9** (rows
  are SNDK/SPY/ASML/GOOGL/MSFT/QQQ/NBIS/NDX — **no SWKS**), `bearish_flow`
  **"14.3%" on N=7**, both flagged in-sample by the tool itself. `[HIST:signal_backtest]`

## Detailed findings

### IV regime — percentile, z-score, VRP

`uw historical iv-percentile-zscore --symbol SWKS --lookback-days 252`:

| Field | Value |
|---|---|
| `current_iv30d` | **0.559** |
| `iv_percentile` | **40.26** |
| `iv_zscore` | **−0.219** |
| `regime` | **`NORMAL`** |
| `lookback_days` (requested) | 252 |
| **`dates_used` (actual)** | **77** |

**Gap caveat (mandatory):** the requested 252-day lookback resolved to **77 actual
sessions**. Per `phase-0-intake.md §Local data`, those 77 sessions span
**2026-03-13 → 2026-07-31 and cross the ~4-week hole 2026-03-30 → 2026-04-24**.
So `iv_percentile = 40.26` is a percentile against **77 available sessions
(~4.5 calendar months), not one year**. It is not a true 1-year percentile, and the
phase's pitfall about structurally-low-vol years cannot even be assessed on this
window. Quoting the tool's own `dates_used` rather than the calendar span, as the
gap rule requires.

`uw historical vrp --symbol SWKS --realised-window-days 30`:

| Field | Value |
|---|---|
| `iv30d` | 0.559 |
| `realised_vol` | **0.4927** |
| `realised_window_days` | 30 |
| **`vrp`** | **+0.0663** |
| `regime` | **`PREMIUM_SELLING`** |
| `interpretation` | *"Options pricing more vol than realised — favour premium selling."* |

**This is the single most consequential reading in the phase, and taken at face
value it contradicts phases 1 and 4.** Phase 1 concluded the crowd is *supplying*
already-cheap vol and that owning optionality is structurally favoured; phase 4
concluded dealers are short gamma at spot so realized vol should *exceed* what a
flat 57–60% surface implies. VRP `PREMIUM_SELLING` says the opposite.

The phase's own pitfall — *"VRP can flip on a single catalyst day — read the
trailing-5d trend, not just today"* — instructs the check, so it was performed on
the same closes the tool uses (annualized log-return σ × √252, over the contiguous
2026-06-18 → 2026-07-31 block — **no gap crossing**, N = 30):

| Window | Realized vol | vs `iv30d` 55.90% |
|---|---|---|
| 30 sessions (matches tool: 0.4926 ≈ 0.4927 ✓) | **49.26%** | **+6.6 pts ⇒ sell premium** |
| 30 sessions **excluding 2026-07-29** (the −5.40% earnings day) | 47.56% | +8.3 pts |
| **10 sessions** | **55.53%** | **+0.4 pts ⇒ flat** |
| **5 sessions** | **63.49%** | **−7.6 pts ⇒ BUY premium** |
| 3 sessions | 61.95% | −6.1 pts |
| Largest / smallest daily move in window | **+5.23% / −5.55%** | |

Two conclusions follow, and both matter:

1. **The +6.63 VRP is not an earnings artifact.** Removing the −5.40% earnings day
   moves 30-day realized only 49.26% → 47.56%. SWKS is *structurally* a ~48–50 vol
   name over the month; the gap did not manufacture the number.
2. **But the 30-day window is stale.** Realized vol is **rising monotonically as
   the window shortens** (49.3 → 55.5 → 63.5) while `iv30d` has been **falling**
   (0.741 on 2026-07-28 → 0.559 now, `phase-0.5-context.md`). The two lines have
   **crossed**. On any horizon a 21-DTE or 49-DTE option actually cares about, the
   market is now pricing **less** vol than the stock is delivering.

**Adjudication: the VRP `PREMIUM_SELLING` label is accepted as a correct 30-day
measurement but rejected as the tradeable regime.** The near-term regime is
**premium-buying**, which restores consistency with phase 1 (crowd short premium
into 29.9th-percentile-cheap vol) and phase 4 (dealers short gamma at spot). Stated
with its limitation: a 5-session realized-vol estimate has a wide standard error,
which is why the 10-session reading (55.53%, essentially *at* implied) is quoted
alongside it as the conservative anchor. The honest summary is **"VRP has closed
from +6.6 to roughly zero-to-negative,"** not "vol is outright cheap to realized."

### Cumulative premium flow (90d)

`uw historical cumulative-premium-flow --symbol SWKS --days 90`:

| Field | Value |
|---|---|
| `cumulative_bullish` | **$92,675,789** |
| `cumulative_bearish` | **$85,963,860** |
| **`net_flow`** | **+$6,711,929** |
| **`trend_direction`** | **`MIXED`** |
| `days` (requested) | 90 |
| **`dates_covered` (actual)** | **78 sessions, 2026-03-13 → 2026-07-31** |

**Gap caveat:** the 90-day request returned **78 sessions spanning 4.6 calendar
months and crossing the 2026-03-30 → 2026-04-24 hole**. This is a cumulative sum
over available sessions, not a contiguous 90-day accretion, and it must not be
annualized or read as a rate.

Net **+$6.71M bullish over 78 sessions** is a **3.8% tilt** on $178.6M of
two-way premium — the tool's own `MIXED` label is right. The phase's
"stealth institutional build" heuristic (*cumulative flow positive and persistent
≥60d*) requires **persistence**, and `MIXED` explicitly denies it. **No stealth
build is present.**

For scale, that entire 78-session net of +$6.71M is dwarfed by what phase 2 found
in **two** sessions in the *share* tape: **+$35.4M net dark-pool absorption on
2026-07-29/30**. Consistent with `phase-3-positioning.md §Verdict` — the SWKS story
lives in the share tape, not the option chain.

### P/C ratio z-score — the one genuine extreme

`uw historical pc-ratio-zscore --symbol SWKS --lookback-days 20`:

| Field | Value |
|---|---|
| `current_pc_ratio` | **4.0593** |
| `mean_pc_ratio` | 1.0798 |
| `std_pc_ratio` | 1.1652 |
| **`zscore`** | **+2.557** |
| **`extreme`** | **`BEARISH_EXTREME`** |

**|z| > 2 ⇒ the phase's contrarian-setup condition fires.** This is the third
independent confirmation of the same fact: `phase-0.5-context.md` put the same P/C
at the **97.4th percentile of SWKS's own 78-session history**, and this z-score
puts it at **2.6 sigma over a 20-session window**.

But `phase-1-flow.md` already established **what** produced it, and the mechanism
inverts the label. The 4,384 puts were not bought — **88.9% of them traded on the
bid** (put ask-share **0.088**), and 3,333 of them were a single **opening short-put
block at the 52.5 strike** (vol/OI 3.52×, $219,979, sold). A `BEARISH_EXTREME`
manufactured by **put selling** is not bearish sentiment; it is the opposite. The
tool classifies by volume ratio and is blind to aggressor side.

**Handling: the z-score is recorded as a genuine statistical extreme and its
`BEARISH_EXTREME` label is explicitly not adopted as a sentiment read.** The
contrarian setup the heuristic points to is **already the position on the tape**,
not a fade of it.

### GEX time series — regime stability

`uw historical gex-time-series --symbol SWKS --days 30 --dte-max 45`
(`days_analyzed` 30, trajectory length **30** — **2026-06-18 → 2026-07-31, fully
contiguous, no gap crossing**):

`regime_flip_dates` — **exactly one**:

```
date=2026-06-22  from_regime=POSITIVE  to_regime=NEGATIVE
spot=76.26  zero_gamma_level=79.11  zgl_delta=8.4
```

| Date | Regime | Spot | `total_gex` | ZGL |
|---|---|---|---|---|
| 2026-06-18 | **POSITIVE** | 71.82 | 5,674,308 | 70.71 |
| 2026-06-22 | **NEGATIVE** ← flip | 76.26 | 847,489 | 79.11 |
| 2026-06-24 | NEGATIVE | 70.06 | 333,741 | 83.01 |
| 2026-06-29 | NEGATIVE | 66.93 | 92,429 | 89.12 |
| 2026-07-02 | **FULLY_NEGATIVE** | 62.53 | −65,765 | — |
| 2026-07-06 | **FULLY_NEGATIVE** | 62.31 | −300,814 | — |
| 2026-07-08 | NEGATIVE | 58.65 | 635,953 | 90.23 |
| 2026-07-14 | NEGATIVE | 57.48 | 98,234 | 94.55 |
| 2026-07-15 | **FULLY_NEGATIVE** | **57.00** | −855,130 | — |
| 2026-07-16 | **FULLY_NEGATIVE** | **56.91** | −314,699 | — |
| 2026-07-17 | **FULLY_NEGATIVE** | 58.98 | −1,083,507 | — |
| 2026-07-21 | NEGATIVE | 62.98 | 2,501,048 | 77.59 |
| 2026-07-24 | NEGATIVE | 60.42 | 695,671 | 74.69 |
| 2026-07-28 | NEGATIVE | 65.12 | 2,744,326 | 74.97 |
| 2026-07-29 | NEGATIVE | 62.08 | 1,017,558 | 78.82 |
| 2026-07-30 | NEGATIVE | 61.67 | 590,328 | 78.38 |
| **2026-07-31** | **NEGATIVE** | **62.45** | 1,191,030 | **77.61** |

*(Selected rows; all 30 read and audited.)*

**The phase's "GEX regime flip in last 5d ⇒ transition" heuristic does NOT fire** —
the only flip was **27 sessions ago**. Short gamma is SWKS's *settled* condition,
which strengthens phase 4's read: this is not a transient hedging quirk but a
six-week structural state.

Two further observations:

- **The ZGL has been drifting away from spot the whole time** (70.71 → 79.11 →
  89.12 → 94.55 → 77.61) while spot fell from 71.82 to 62.45. As phase 4 showed,
  that drift is the legacy 75/80/95-strike call OI decaying, not a real level
  moving. The `zgl_delta` of **8.4** on the flip date is itself a warning about the
  measure's coarseness on this name.
- **`FULLY_NEGATIVE` clusters mark the bottoms.** The five FULLY_NEGATIVE sessions
  are 07-02, 07-06 and **07-15/16/17 — the exact 3 sessions containing the
  window's low of $56.91**. When total GEX went outright negative, price was at its
  extreme. Today's `total_gex` is **+1,191,030**, i.e. *not* in that capitulation
  state.

**Price context from the same series: 71.82 → 62.45 over 30 sessions (−13.0%),
with a floor at $56.91–57.50 tested on 2026-07-15, 2026-07-16 and again on
2026-07-29** (that day's low, `phase-2-dark-pool.md §Price levels`). That is a
**triple bottom**, and it sits directly beneath phase 2's $58.44–59.34 accumulation
shelf.

### OI trend

`uw historical oi-trend --symbol SWKS --days 30 --top-n 10` (`days_analyzed` 30,
`daily_data` length **30**, 2026-06-18 → 2026-07-31, contiguous):

| Field | Value |
|---|---|
| `overall_trend` | **`BUILDING`** |
| `consecutive_build_days` | **11** |
| `total_net_oi_change` | **+51,001** |

Daily `net_oi_change` (selected; all 30 read):

| Date | Net OI Δ | Increases | Decreases |
|---|---|---|---|
| 2026-06-18 | +769 | 36 | 30 |
| **2026-06-23** | **+26,690** | 98 | 17 |
| **2026-06-24** | **−18,345** | 71 | 24 |
| **2026-06-30** | **+10,625** | 62 | 17 |
| 2026-07-02 | −3,853 | 54 | 25 |
| 2026-07-07 | +3,845 | 58 | 17 |
| 2026-07-08 | +2,507 | 77 | 27 |
| 2026-07-16 | −167 | 58 | 26 |
| 2026-07-20 | +1,665 | 61 | 13 |
| 2026-07-29 | +957 | 52 | 19 |
| **2026-07-30** | **+5,975** | 149 | 40 |
| **2026-07-31 (as-of)** | **+199** | 44 | 16 |

**The `BUILDING` label is technically true and practically misleading.** Of the
+51,001 net change, **+26,690 (52%) landed on one day, 2026-06-23**, and **−18,345
came straight back off the next session** — that pair is a roll/expiry mechanic, not
accumulation. Excluding those two days the 28-session net is **+42,656**, still
dominated by the single +10,625 on 2026-06-30.

Against that, the **as-of day added +199 contracts across 44 increases and 16
decreases** — which is exactly what `phase-3-positioning.md` found from the other
direction (largest single OI change on the entire chain: **46 contracts**;
`biggest-increases --min-oi-change 500` → **empty**). **The two phases agree: there
is no current OI build.** The `consecutive_build_days: 11` counts *sign*, not size.

This is a **spike-then-decay** profile, not the "sustained buildup" the phase's
heuristics reward.

### Multi-day trend table

`uw historical trend --symbol SWKS --days 30`:

| Field | Value |
|---|---|
| `date_range` | **2026-06-18 to 2026-07-31** |
| `days_analyzed` | **30** (contiguous — no gap crossing) |
| `price_change` | **72.45 → 62.28 (−14.03%)** |
| `iv_rank_change` | **65.1457 → 52.8977** |
| `bullish_days` / `bearish_days` | **13 / 17** |
| `flow_direction_latest` | `bullish` |

Last 12 sessions:

| Date | Close | Call prem | Put prem | P/C | IV rank | `net_flow` | Dir |
|---|---|---|---|---|---|---|---|
| 2026-07-16 | 57.63 | $216,419 | **$1,722,365** | 3.089 | 95.8 | −$60,261 | bearish |
| 2026-07-17 | 59.35 | $622,617 | $396,441 | 0.494 | 99.3 | −$360,223 | bearish |
| 2026-07-20 | 59.80 | $268,462 | $671,155 | 1.011 | 100.0 | −$505,597 | bearish |
| 2026-07-21 | 62.95 | $497,483 | $176,579 | 0.547 | 100.0 | −$96,068 | bearish |
| 2026-07-22 | 63.16 | $350,847 | $129,998 | 0.528 | 99.1 | +$129,930 | bullish |
| 2026-07-23 | 60.47 | $726,047 | $100,929 | **0.011** | 100.0 | −$33,902 | bearish |
| 2026-07-24 | 60.21 | $582,693 | $1,027,781 | 0.701 | 96.5 | +$493,813 | bullish |
| 2026-07-27 | 63.44 | $223,493 | $198,322 | 0.409 | 88.7 | −$29,309 | bearish |
| 2026-07-28 *(earnings PM)* | 64.68 | $604,615 | $549,951 | 0.627 | **91.2** | +$35,514 | bullish |
| **2026-07-29** | **61.19** | **$11,092,659** | $3,828,390 | 0.657 | 62.6 | **−$4,809,634** | bearish |
| 2026-07-30 | 62.48 | $131,188 | $142,381 | 1.091 | 56.8 | −$67,463 | bearish |
| **2026-07-31** | **62.28** | $380,703 | $497,180 | **4.059** | **52.9** | +$43,882 | bullish |

**IV rank sat at 88.7–100.0 for the eleven sessions to 2026-07-28 and has collapsed
to 52.9 in three sessions.** That is the whole vol story in one column, and it is
why the level-based readings (40th universe percentile, 29.9th self-percentile) look
cheap while the 30-day VRP still looks rich.

`flow_direction_latest = "bullish"` restates the +$43,882 net that
`phase-1-flow.md` showed is an artifact of classifying **sold** puts as bullish
premium. Not adopted as a directional read.

### Price context (`fz` cross-check) — **UNAVAILABLE**

Attempted per the phase's D8 advisory step:

```
fz quote SWKS --json | jq -c '{rsi, sma50, sma200, perf_ytd, high52, low52}'
→ {"rsi":null,"sma50":null,"sma200":null,"perf_ytd":null,"high52":null,"low52":null}
```

**All six fields are null.** This is the same degradation `phase-0-intake.md`
recorded (`fz quote` parses **14 of 84** fundamental fields). The independent EOD
cross-check on the UW IV/trend read **cannot be performed**; no RSI, no moving
averages, no 52-week proximity from `fz`.

Substituting the equivalent context from the already-validated screener parquet
(**not** `fz`, and therefore **not** tagged `[HIST:rsi fz]`):

| Metric | Value |
|---|---|
| Close (2026-07-31) | **$62.28** |
| `week_52_high` | **$90.90** → **−31.5%** below |
| `week_52_low` | **$51.93** → **+19.9%** above |
| Position in 52w range | **26.5%** (lower third) |
| 30-session change | **−14.03%** (72.45 → 62.28) |
| Window low (30 sessions) | **$56.91** (2026-07-16); intraday low $57.50 on 2026-07-29 |

The advisory conclusion the `fz` check was meant to support — *"an overbought RSI at
the 52-week high tempers a fresh-breakout thesis"* — is **inapplicable in the
opposite direction**: SWKS sits in the **lower third of its annual range, 31.5%
off the high**, after a −14% month. Nothing here tempers a long thesis on
overbought grounds; the risk is the reverse (falling knife), which phase 7b's
quality veto must adjudicate.

### Signal backtest — **the sizing input is null**

Phase 2's dominant signal is dark-pool accumulation, so the matching class was run
first:

```
uw historical signal-backtest --signal-type dark_pool_accumulation --lookback-days 5 --top-n 20
→ {"note":"no backtest results","signal_type":"dark_pool_accumulation","total_signals":0}
```

**Re-run once per the composition guidance — identical empty stub.**
⇒ `win_rate_source = null`.

The two populated classes, recorded as context only:

| `signal_type` | `win_rate` | `total_signals` | `avg_move_pct` |
|---|---|---|---|
| `bullish_flow` | **100.0%** | **9** | 8.73 |
| `bearish_flow` | **14.3%** | **7** | 6.07 |

**Neither may be used as the Kelly `p`, for four independent reasons:**

1. **The tool is market-wide.** Inspecting `.results[]` for `bullish_flow` returns
   **SNDK, SPY, ASML, GOOGL, MSFT, SNDK, QQQ, NBIS, NDX** — **SWKS does not
   appear**. This is a base rate for mega-caps and indices over the last five
   trading days, not a SWKS rate.
2. **The tool disclaims itself.** `methodology_notes`: *"In-sample backtest — not a
   robust live edge."*
3. **N is below the phase's own confidence floor.** 9 and 7 respectively; the
   pitfall sets **<10 firings = low confidence**.
4. **A 100.0% win rate on N=9 is a red flag, not an edge** — and its mirror
   (`bearish_flow` at 14.3%) shows both numbers are measuring the same thing: the
   **five-session tape to 2026-07-31 rewarded longs and punished shorts across the
   market**. That is a regime observation for phase 6, not a signal edge for SWKS.

Note also the **latest-anchor caveat**: `signal-backtest` takes no `--date` and
anchors to the latest available session. `phase-0-intake.md` confirms that is
**2026-07-31**, so the window is as-of-consistent on this run — but a re-run after
a new session lands will move these numbers.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows / N used |
|---|---|---|
| `uw historical iv-percentile-zscore --symbol SWKS --lookback-days 252 --json` | `current_iv30d`=0.559, **`iv_percentile`=40.26**, `iv_zscore`=−0.219, `regime`=NORMAL, **`dates_used`=77** (vs 252 requested) ← `.iv_percentile`, `.dates_used` | **77 sessions (gap-crossing)** |
| `uw historical vrp --symbol SWKS --realised-window-days 30 --json` | `iv30d`=0.559, `realised_vol`=**0.4927**, **`vrp`=+0.0663**, `regime`=**PREMIUM_SELLING**, `interpretation`="Options pricing more vol than realised…" ← `.vrp`, `.regime` | 30 |
| `uw historical cumulative-premium-flow --symbol SWKS --days 90 --json` | `cumulative_bullish`=92675789, `cumulative_bearish`=85963860, **`net_flow`=+6711929**, **`trend_direction`=MIXED**, `dates_covered` length=**78** (2026-03-13→2026-07-31) ← `.net_flow`, `.trend_direction`, `.dates_covered\|length` | **78 sessions (gap-crossing)** |
| `uw historical pc-ratio-zscore --symbol SWKS --lookback-days 20 --json` | `current_pc_ratio`=4.0593, `mean_pc_ratio`=1.0798, `std_pc_ratio`=1.1652, **`zscore`=+2.557**, **`extreme`=BEARISH_EXTREME** ← `.zscore`, `.extreme` | 20 |
| `uw historical gex-time-series --symbol SWKS --days 30 --dte-max 45 --json` | `days_analyzed`=30, `trajectory` length=**30**; **`regime_flip_dates`** = single entry {date 2026-06-22, POSITIVE→NEGATIVE, spot 76.26, zgl 79.11, zgl_delta 8.4} ← `.regime_flip_dates[]`, `.trajectory[]`; 5 `FULLY_NEGATIVE` days (07-02, 07-06, 07-15, 07-16, 07-17) | 30 (contiguous) |
| `uw historical oi-trend --symbol SWKS --days 30 --top-n 10 --json` | **`overall_trend`=BUILDING**, `consecutive_build_days`=**11**, `total_net_oi_change`=**+51001**, `days_analyzed`=30, `daily_data` length=30; 2026-06-23 net_oi_change **+26690**, 2026-06-24 **−18345**, as-of **+199** ← `.daily_data[].net_oi_change` | 30 (contiguous) |
| `uw historical trend --symbol SWKS --days 30 --json` | `date_range`="2026-06-18 to 2026-07-31", `days_analyzed`=**30**, `price_change`="72.45 -> 62.28", `iv_rank_change`="65.1457 -> 52.8977", `bullish_days`=13, `bearish_days`=17, `flow_direction_latest`=bullish ← top-level; per-day close/premium/pcr/iv_rank ← `.daily_data[]` | 30 (contiguous) |
| `uw historical signal-backtest --signal-type dark_pool_accumulation --lookback-days 5 --top-n 20 --json` **(×2)** | `{"note":"no backtest results","total_signals":0}` **both runs** ← `.total_signals` | 0 |
| `uw historical signal-backtest --signal-type bullish_flow --lookback-days 5 --top-n 20 --json` | **`win_rate`="100.0%"**, **`total_signals`=9**, `avg_move_pct`=8.73, `methodology_notes`="In-sample backtest — not a robust live edge." ← top-level; `.results[]` tickers = SNDK/SPY/ASML/GOOGL/MSFT/SNDK/QQQ/NBIS/NDX — **no SWKS** | 9 (market-wide) |
| `uw historical signal-backtest --signal-type bearish_flow --lookback-days 5 --top-n 20 --json` | `win_rate`="14.3%", `total_signals`=7, `avg_move_pct`=6.07 | 7 (market-wide) |
| `fz quote SWKS --json --no-color` | rsi/sma50/sma200/perf_ytd/high52/low52 **all null** ← `.fundamentals."RSI (14)"` etc. — D8 cross-check **unavailable** | — |
| DuckDB `stock-screener-*.parquet`, SWKS, date ≥ 2026-06-18 | realized σ×√252: 30d **0.4926** (reconciles tool's 0.4927), excl-07-29 **0.4756**, 10d **0.5553**, 5d **0.6349**, 3d **0.6195**; max/min daily log-return +5.23% / −5.55% `[HIST:realized_decomp DUCKDB]` | 30 (contiguous) |
| DuckDB — 52-week context | `week_52_high`=90.90, `week_52_low`=51.93, close=62.28 ⇒ −31.5% from high, +19.9% off low, 26.5% of range | 1 |

## Tool errors

No `uw historical` command errored.

**Non-error conditions recorded per orchestration rule 3:**
- `signal-backtest --signal-type dark_pool_accumulation` → empty stub
  `{"note":"no backtest results","total_signals":0}` on **two** consecutive runs.
  Per the composition guidance this is now recorded as `win_rate_source = null`,
  not treated as a failure.
- `fz quote` → all six D8 price-context fields **null** (same 14/84-field
  degradation as `phase-0-intake.md`). The advisory cross-check was skipped and
  substituted with parquet-sourced 52-week context, explicitly **not** tagged as
  `fz`.
- **Gap crossings surfaced as data-quality caveats** (per the gap rule, which
  directs these into this section):
  - `iv-percentile-zscore` requested 252 days, `dates_used = 77` spanning
    2026-03-13 → 2026-07-31 — **crosses the 2026-03-30 → 2026-04-24 hole**.
    `iv_percentile = 40.26` is a 77-session percentile, **not** a 1-year one.
  - `cumulative-premium-flow` requested 90 days, `dates_covered` = **78 sessions**
    over the same span — **crosses the hole**. The cumulative sum is over available
    sessions only and must not be read as a 90-day rate.
  - `gex-time-series`, `oi-trend` and `trend` all returned **30 sessions spanning
    2026-06-18 → 2026-07-31, entirely inside the contiguous post-2026-04-27 block**
    — **no gap crossing**, series verified against `phase-0-intake.md`'s date list.
    No suspicious smoothing detected in any of them.
- **Latest-anchor caveat:** `iv-percentile-zscore`, `pc-ratio-zscore`, `oi-trend`,
  `cumulative-premium-flow`, `gex-time-series`, `trend`, `signal-backtest` and
  `vrp`'s realized leg take no `--date` and anchor to the **latest available
  session**. `phase-0-intake.md` confirms that is **2026-07-31 = the as-of date**,
  so every trailing read above is as-of-consistent on this run. A re-run after a new
  session lands will shift all of them.

## DATA NOTE / CORRECTION

1. **The tool's `PREMIUM_SELLING` VRP label is reported verbatim but not adopted as
   the tradeable regime.** The recomputation (30d 49.26% → 10d 55.53% → 5d 63.49%
   against a falling `iv30d` of 55.90%) is a **term-structure decomposition of the
   same input the tool uses**, performed because the phase's pitfall explicitly
   requires the trailing-5d check — not a re-derivation to overrule the tool. The
   30-day figure reconciles to four decimals (0.4926 vs the tool's 0.4927), which
   validates the method before the shorter windows are read. Both readings are
   carried forward: `vrp_30d = +0.0663 (PREMIUM_SELLING)` and
   `vrp_5d ≈ −0.076 (premium-buying)`.
2. **`BEARISH_EXTREME` is recorded as a statistical fact and rejected as a sentiment
   label**, on evidence already validated in `phase-1-flow.md` (put ask-share
   **0.088**; the 3,333-contract 52.5-strike block traded on the **bid** with
   vol/OI 3.52×). The z-score tool classifies on the volume ratio and has no
   aggressor-side input.
3. **`BUILDING` OI trend is recorded and qualified.** `total_net_oi_change` +51,001
   is real, but 52% of it is one session (2026-06-23, +26,690) largely reversed the
   next (−18,345). The as-of day's +199 is consistent with
   `phase-3-positioning.md`'s independent finding of a 46-contract maximum change.
   No contradiction between the phases — the labels differ, the data agrees.
4. **`win_rate` is NOT SWKS-specific and is NOT used.** Verified by reading
   `.results[]` and confirming SWKS is absent from the `bullish_flow` sample.
   Recorded so phase 9 does not mistake "100.0%" for a SWKS edge.
5. All gap-crossing windows quote the tool's **own** session count
   (`dates_used`, `dates_covered`, series length) rather than the requested
   calendar span, as the gap rule requires.

## Verdict for downstream phases

- **Volatility regime:** **CHEAP in level, FAIR-to-CHEAP versus near-term realized.**
  `iv_percentile` **40.26** (over 77 sessions, not 252), `iv_zscore` **−0.219**,
  `regime` **NORMAL**, and the **29.9th self-percentile** from
  `phase-0.5-context.md`. The 30-day VRP of **+0.0663** says rich; the 10-session
  VRP is **≈ 0** and the 5-session VRP is **≈ −0.076**. **The honest statement is
  that VRP has closed from +6.6 points to roughly zero-or-negative as IV crushed and
  realized rose — not that vol is outright cheap to realized.**
- **Premium environment:** **PREMIUM-BUYING on a 1–8 week horizon.** Three
  independent supports: (a) realized vol has crossed above implied on the trailing
  5–10 sessions; (b) dealers have been short gamma for **29 of 30 sessions** with
  no flip in 27 sessions (`phase-4-structure.md` puts spot on the most negative
  per-strike GEX, 62.5 = −448,437), so realized should keep exceeding a flat 57–60%
  surface; (c) `phase-1-flow.md` shows the crowd **supplying** that vol
  (`net_call_premium` −$170,899 and `net_put_premium` −$214,781, both negative).
  **Favour debit structures; be on the other side of the seller.** This
  **overrides** the tool's 30-day `PREMIUM_SELLING` label, with the reasoning and
  both numbers recorded above.
- **Conviction that today's signal is HISTORICALLY EDGE-POSITIVE: 1 / 5.**
  There is **no usable historical edge measurement for this setup**. The matching
  backtest class returns `total_signals: 0` twice; the populated classes exclude
  SWKS, disclaim themselves as in-sample, and carry N = 9 and 7. Separately, the
  90-day cumulative premium flow is **`MIXED`** (+$6.71M on $178.6M two-way, a 3.8%
  tilt), so the "stealth build ⇒ high-confidence directional" heuristic **does not
  fire**. This phase supplies **regime context, not edge**, and phase 9 must size
  accordingly.
- **Three specific datapoints:**
  1. **IV percentile 40.26** (`iv_zscore` −0.219, `regime` NORMAL, `dates_used` 77 —
     a 4.5-month percentile, not a 1-year one).
  2. **VRP +0.0663 at 30 days (`PREMIUM_SELLING`) → ≈ 0 at 10 days → ≈ −0.076 at 5
     days.** The regime has flipped on the tradeable horizon.
  3. **Signal win rate: NONE AVAILABLE.** `dark_pool_accumulation` → 0 signals
     (×2). Market-wide `bullish_flow` 100.0% / N=9 and `bearish_flow` 14.3% / N=7
     are recorded as tape-regime context and are **not** SWKS edge.
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:             dark_pool_accumulation
  signal_backtest_win_rate: null
  win_rate_n:               0
  win_rate_source:          null
  ```
  **Phase 9 must fall back to the conviction bin** per
  `rubrics/sizing-rubric.md` §"Choosing the Kelly `p`". For the record, had a
  populated class been substituted it would still be unusable: the backtest is
  **market-wide** (SWKS absent from the sample), so it is a base rate of a signal
  class across the tape, never a SWKS-specific rate.
- **Additional levels this phase contributes:**
  - **$56.91–57.50 — a triple bottom.** Lows on 2026-07-15 ($57.00), 2026-07-16
    ($56.91) and 2026-07-29 intraday ($57.50). All three coincide with
    `FULLY_NEGATIVE` total GEX or the earnings gap. This sits **directly beneath**
    phase 2's $58.44–59.34 accumulation shelf and **above** phase 1's sold 52.5 put
    strike — three instruments, one floor zone.
  - **52-week range $51.93–$90.90**, close $62.28 = **26.5% of range, −31.5% from
    the high**. Any long thesis here is a **falling-knife/washout** thesis, not a
    breakout thesis. `fz`'s RSI/SMA cross-check was **unavailable** to temper or
    confirm this.
- **Open questions:**
  - **Will realized vol keep exceeding implied, or was the 5-session 63.5% an
    echo of the earnings gap that decays?** The 30-day figure excluding 2026-07-29
    (47.56%) shows the gap is *not* what drives realized — but the 5-session window
    still contains that day's neighbours. Phase 9's structure choice (debit vs
    credit) hinges on this; the conservative anchor is the **10-session 55.53% ≈
    implied**, i.e. treat vol as **fairly priced**, not a giveaway.
  - **Why has no backtestable dark-pool-accumulation signal ever fired?** Either
    the engine's threshold is not met by SWKS-scale prints ($16.3M/day, absent from
    the top-30 dark-pool tickers per `phase-2-dark-pool.md`), or the class is
    unpopulated market-wide. Either way phase 10 should score this run's confluence
    **without** an empirical win-rate leg and say so explicitly.
  - **Does the $56.91–57.50 triple bottom hold in a short-gamma regime?** Phase 4
    warns dealer hedging **amplifies** breaks. The three prior tests all occurred
    with `total_gex` at or below zero (`FULLY_NEGATIVE`); today's +1,191,030 is not
    in that state. Phase 8's bear case must argue the fourth test, and phase 9 must
    not place a stop inside $58–60 where dealer selling accelerates.
