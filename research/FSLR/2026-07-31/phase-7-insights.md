# Phase 7 — UW Insights Confluence

**Ticker:** FSLR
**As-of date:** 2026-07-31
**Generated:** 2026-07-31
**Upstream phases cited:** `phase-0.5-context.md`, `phase-1-flow.md`, `phase-2-dark-pool.md`, `phase-3-positioning.md`, `phase-4-structure.md`, `phase-5-historical.md`, `phase-6-macro.md`

## Summary

**UW's composite layer reads FSLR as mildly bearish and low-confidence — and
it does so using precisely the measures the earlier phases proved defective.**
`signal-confluence` scores FSLR **3 on the bearish side** (`bearish_flow`,
`oi_building_puts`, `high_iv_sell_premium`) and places it **outside the
top-300 bullish names**, where the score floor is 4. `conviction-matrix`
returns **MIXED at 8.8% confidence**. `institutional-accumulation` returns
**NEUTRAL**.

Deconstructing the three bearish factors is the useful work of this phase:
**one is a measurement artifact, one is protective hedging, and one is not
directional at all.** `bearish_flow` rests on `net_flow = −$2,374,671`, which
`phase-1-flow.md` showed **omits $2,545,750 (9.5% of the tape)** including a
$1.805M cross printed **at the offer**. `oi_building_puts` is real but phase 3
identified it as a **protective ladder** (support thickening 210 → 200 → 190)
against a far-dated book that is overwhelmingly **call**-side. And
`high_iv_sell_premium` is a **volatility** signal — phase 5's VRP +0.3587 —
which says sell premium, not sell stock.

The phase's strongest contribution is **validation**. `conviction-matrix`
returns `call_ask_volume 11,760 / call_bid 9,646 / put_ask 3,612 / put_bid
2,935` — **exactly** phase-1's independently computed DuckDB aggressor split,
and with the 1,900-contract cross again absent. Independently, the `251
trades / 488,393 shares` dark-pool figure exceeds phase-2's verified
`250 / 416,193` by **exactly 72,200 shares** — the cancelled duplicate. **Four
separate UW tools inherit that inflation.**

The one genuine disagreement is `institutional-accumulation = NEUTRAL` versus
phase-2's **ACCUMULATION**, and the cause is identifiable: this tool blends
all sessions and counts the cancelled print, while phase 2 decomposed by
session and found the regular session **73.1% buy** against a
classification-artifact **6.8%** at the close.

`uw insights deep-dive`'s fundamentals leg **failed outright** —
`{"error":"yahoo quoteSummary FSLR: HTTP 401"}` — which also emptied
`analyst-vs-flow` of its analyst side. Phase 7b must source fundamentals
elsewhere.

## Key signals

- **Bearish confluence score 3/6**: `bearish_flow`, `oi_building_puts`,
  `high_iv_sell_premium`; `volume_ratio` 1.86 `[INSIGHT:signal_confluence]`
- **Absent from the bullish list even at top-300** (bullish score floor is 4;
  distribution 4:267, 5:31, 6:2) `[INSIGHT:signal_confluence]`
- **`conviction-matrix` = MIXED at just 8.8% confidence**, *"Balanced dark
  pool activity — no clear bias"* `[INSIGHT:conviction_matrix]`
- **Options-flow volumes match phase-1's DuckDB split exactly** (11,760 /
  9,646 / 3,612 / 2,935) — and again exclude the 1,900 cross
  `[INSIGHT:conviction_matrix]`
- **`institutional-accumulation` = NEUTRAL**, `buy_sell_ratio` 1.43, but on
  **488,393 shares / 251 trades** — 72,200 more than phase-2's verified count
  `[INSIGHT:institutional_accumulation]`
- **`price-vs-flow`: no divergence** — price −18.11%, flow bearish, *"aligned"*
  `[INSIGHT:price_vs_flow]`
- **Yahoo fundamentals HTTP 401** — deep-dive fundamentals and the entire
  analyst leg unavailable `[INSIGHT:deep_dive]`
- **New: Jan-2027 $220 calls +349 OI on 1,029 volume** at $31.79 — far-dated
  call building below phase-3's ≥500 filter `[INSIGHT:deep_dive]`
- **`earnings-play`: FSLR correctly absent** — earnings 2026-10-29, ~90 days
  out `[INSIGHT:earnings_play]`

## Detailed findings

### Deep dive snapshot

**Directional aggregates** (`.uw_screener`, whole tape — reconciled against
phase-1 and phase-0.5):

| Field | Value |
|-------|------:|
| `call_premium` | $19,838,946 |
| `put_premium` | $6,825,911 |
| Total premium | $26,664,857 |
| `bullish_premium` | $10,872,218 |
| `bearish_premium` | $13,246,889 |
| **Derived `net_flow` = bullish − bearish** | **−$2,374,671** |
| `call_volume` / `put_volume` | 24,254 / 6,770 |
| `put_call_ratio` | 0.2791 |
| `iv_rank` | 81.9358 |
| `iv30d` | 0.7378 |
| **`implied_move` / `implied_move_perc`** | **$1.611 / 0.7625%** |
| `total_open_interest` | 577,414 |
| `next_earnings_date` | 2026-10-29 |

**Reconciliation: consistent across all three phases.** These match
`phase-0.5-context.md` and `phase-1-flow.md` exactly. The `net_flow` of
−$2,374,671 places FSLR in the **1.2 percentile of 4,499 names**
(`[CTX:universe_rank_net_dir]`) — and phase 1 established that adding back the
$1.805M cross that printed **at the offer** narrows it to roughly **−$0.57M**,
while net customer **delta** is **+$10.73M long**.

**`implied_move` $1.611 / 0.7625%** is the figure phase 9 must size structures
against (N4). Post-earnings, it carries **no event premium** — phase 4 found
`front-end-iv-ratio` **FLAT at 1.001**.

**Dark pool block** (`.uw_dark_pool`):

| Field | Value | Phase-2 verified | Δ |
|-------|------:|-----------------:|--:|
| `total_premium` | $103,647,999.45 | **$88,271,601** | +$15,376,398 |
| `total_shares` | 488,393 | **416,193** | **+72,200** |
| `trade_count` | 251 | **250** | **+1** |
| `avg_price` | 212.0376 | — | — |

**The deltas are exactly one cancelled 72,200-share print.** This is the
fourth UW tool to inherit it (after `block-stratified`, `price-levels` and
`institutional-accumulation`).

**Fundamentals block** (`.yahoo_fundamentals`):

```json
{"error":"yahoo quoteSummary FSLR: HTTP 401"}
```

**Hard failure.** No P/E, market cap, short interest, margins or analyst data
from this path. Substitutes already in hand: `fz screen` gives **P/E 13.01,
Market Cap 22.68B, Short Float 9.75%, Float 101.48M**
(`phase-0-intake.md`, `phase-0.5-context.md`), and `phase-6-macro.md` carries
the Q2 print (EPS $3.92 vs $2.86, EBITDA $644M, GM ~57%, backlog 45.1 GW).
**Phase 7b must not rely on this tool.**

**Top OI changes** (`.uw_top_oi_changes`) — one row phase 3's `--min-oi-change
500` filter excluded:

| `option_symbol` | Parsed | OI Δ | Volume | Avg px |
|---|---|-----:|-------:|-------:|
| `FSLR260918C00220000` | Sep-18 220 C, 49 DTE | +985 | 1,082 | $16.32 |
| `FSLR260731C00250000` | Jul-31 250 C, 0 DTE | +563 | 634 | $0.13 |
| `FSLR260731C00205000` | Jul-31 205 C, 0 DTE | +411 | 596 | $6.94 |
| **`FSLR270115C00220000`** | **Jan-15-2027 220 C, 168 DTE** | **+349** | **1,029** | **$31.79** |
| `FSLR260731P00167500` | Jul-31 167.5 P, 0 DTE | +295 | — | $0.10 |

**The Jan-2027 $220 call build (+349 on 1,029 volume ≈ $3.27M notional
premium) is new information.** Together with the Sep-18 $220 build (+985) it
means **$220 calls are being accumulated in both the 49-day and 168-day
tenors** — reinforcing phase-3's "hedged near-term, long far-term" structure
and phase-6's observation that Technology carries the lowest sector PEG. Two
of the five largest OI changes are 0DTE noise expiring today.

### Signal confluence

| Direction | FSLR | Score | Factors |
|-----------|------|------:|---------|
| Bullish | **absent from top-300** | **< 4** | — |
| **Bearish** | **present** | **3** | `bearish_flow`, `oi_building_puts`, `high_iv_sell_premium` |

FSLR's bearish row: `close 211.03`, `iv_rank 81.9358`, `net_flow −2,374,671`,
`put_call_ratio 0.2791`, **`volume_ratio 1.86`** (matching phase-0.5's
independently computed `opt_vol_x` of 1.86 exactly).

Top bullish name for scale: **DXCM, score 6/6** — all six factors
(`bullish_flow`, `low_pcr`, `volume_spike`, `dp_accumulation`, `oi_building`,
`low_iv_cheap_options`), `iv_rank` 19.5, `volume_ratio` 3.8. **That is what a
clean bullish stack looks like on this instrumentation, and FSLR is not close
to it.** Only 2 of 300 names scored 6.

**Deconstructing FSLR's three bearish factors — this is the phase's central
analytical point:**

| Factor | Verdict | Basis |
|--------|---------|-------|
| `bearish_flow` | **Artifact** | Rests on `net_flow` −$2.37M. `phase-1-flow.md` proved this measure **excludes $2,545,750 (9.5%)** of the tape as `mid`/`no_side`, including a **$1.805M cross at the offer** whose dealer hedge phase 2 independently identified (49s lag, 101.1% match). Corrected, net premium is ≈−$0.57M and net **delta** is **+$10.73M long**. |
| `oi_building_puts` | **Real, but mislabelled as directional** | Phase 3 confirms near-term put skew (Aug-21 P/C **1.166**, Aug-07 **1.503**) — but identifies it as a **protective ladder** thickening downward (210 net −432 → 200 net −1,811 → 190 net −3,040) beneath a far-dated book that is overwhelmingly call-side (Sep-18 P/C **0.382**; Jan-2028 **22,142 calls, zero puts**). Phase 4 adds that these puts are **cheap**: 25Δ put IV 0.7613 **below** 25Δ call IV 0.7652, `interpretation` **COMPLACENT**. **Legacy hedges, not fresh bearish demand.** |
| `high_iv_sell_premium` | **Real, but not directional** | Phase 5's VRP **+0.3587** (IV 0.7378 vs verified realized 0.3821) — the most robust finding in the run. But it argues for **selling premium**, not for being short the stock. Counting a volatility factor toward a directional bearish score conflates two different trades. |

**One of three bearish factors survives as directional evidence, and even it
describes hedging rather than conviction.**

**Caveat on the bullish absence:** the first call used `--top-n 20`; re-running
at **`--top-n 300`** confirmed FSLR is absent from a 300-name list whose
minimum score is **4**. So FSLR's bullish score is **≤ 3** — it is genuinely
not a bullish confluence name on this instrument, not merely crowded out.

### Conviction matrix

| Field | Value |
|-------|------:|
| **`scenario`** | **MIXED** |
| **`confidence_pct`** | **8.8** |
| `explanation` | *"Balanced dark pool activity — no clear bias."* |
| `thresholds` | bull ≥ 0.60, bear ≤ 0.40 |
| DP `buy_ratio` | **0.588** |
| DP buy / sell volume | 287,011 / 201,382 |
| DP trades | **251** |
| `call_ask_volume` | **11,760** |
| `call_bid_volume` | **9,646** |
| `put_ask_volume` | **3,612** |
| `put_bid_volume` | **2,935** |

**Two observations of unequal importance.**

First, **the four options-flow volumes reproduce phase-1's DuckDB aggressor
split contract-for-contract** (call ask 11,760 / call bid 9,646 / put ask
3,612 / put bid 2,935). That is strong mutual validation of both the escape-hatch
query and the tool. **And the 1,900-contract `no_side` cross is again
absent** — confirming a third time that UW's directional plumbing drops
crosses.

Second, **`buy_ratio` 0.588 misses the 0.60 bullish threshold by 0.012** — and
that margin is entirely artificial. Removing the cancelled 72,200-share print
from the buy side gives **214,811 / 201,382 = 0.516**, *further* from bullish.
But phase-2's session decomposition gives **73.1% buy in the regular session**
(63.2% excluding the delta hedge) against a **6.8%** closing-auction figure
that is a pure NBBO-classification artifact. **The tool's single blended ratio
is the wrong statistic**, and its 8.8% confidence is an honest admission that
it knows the read is weak.

### Price vs flow

| Field | Value |
|-------|------:|
| `divergence` | **false** |
| `divergence_signal` | *"Price and flow are aligned"* |
| `flow_direction` | bearish |
| `net_premium_flow` | −$2,374,671 |
| `price_start` → `price_end` | 257.70 → 211.03 |
| `price_change_pct` | **−18.11%** |
| `period_high` / `period_low` | 266.77 / 195.84 |
| `iv_rank` | 81.9358 |

No divergence: price fell and flow is bearish, so the two agree. **But both
inputs are compromised for a current-state read.**

The `flow_direction = "bearish"` label is the same artifact-laden measure
deconstructed above. And the **−18.11%** is stale as a description of the
present: `phase-5-historical.md` established the decline ran 2026-06-18 →
2026-07-16 (257.70 → 211.93), after which FSLR **based for twelve sessions
between 199.24 and 211.99 on close** and went nowhere (211.93 → 211.03).

**The absence of divergence is therefore correct about the last 30 days and
uninformative about the last two weeks.** Per the heuristic, divergence is a
leading reversal signal — its absence here is not evidence against a turn,
because the window that produced the −18.11% has already stopped operating.

### Analyst vs flow

```json
{"symbol":"FSLR",
 "options_flow":{"bullish_premium":10872218,"bearish_premium":13246889,
                 "net_flow":-2374671,"put_call_ratio":0.2791,
                 "flow_sentiment":"bearish"}}
```

**The analyst side is entirely missing** — the response contains only
`symbol` and `options_flow`. There is no consensus rating, no price target,
no analyst count. The cause is the same **Yahoo HTTP 401** that emptied
`deep-dive`'s fundamentals block, since this tool sources consensus from
yfinance.

**No agreement/disagreement assessment can be made.** The tool degraded to a
duplicate of the flow numbers already in hand. **Phase 7b/7c must source
analyst consensus and price targets independently** (WebSearch or `fz`).

### Institutional accumulation

| Field | Value |
|-------|------:|
| **`signal`** | **"NEUTRAL — balanced dark pool activity"** |
| `buy_sell_ratio` | 1.43 |
| `buy_side_volume` | 287,011 |
| `sell_side_volume` | 201,382 |
| `total_dp_volume` | **488,393** ⚠ |
| `total_dp_premium` | **$103,647,999.45** ⚠ |
| `dark_pool_trades` | **251** ⚠ |
| `vwap` | 212.22 |
| `avg_trade_price` | 212.04 |
| `price_30d_change_pct` | −18.11% |

`top_price_levels`:

| Price | Premium | Shares | Trades |
|------:|--------:|-------:|-------:|
| **212.97** | **$30,854,595** | **144,878** | **3** ⚠ |
| 211.03 | $26,294,971 | 124,603 | 29 |
| 214.00 | $6,395,390 | 29,885 | 4 |
| 212.00 | $2,459,624 | 11,602 | 1 |
| 214.39 | $1,071,950 | 5,000 | 1 |

⚠ The 212.97 row double-counts the cancelled print — **144,878 shares is
2 × 72,200 plus a 478-share tail**; the genuine figure is ~72,678 shares /
~$15.48M. Identical to the defect phase 2 found in `price-levels`.

**This tool's NEUTRAL verdict is the one genuine disagreement with an upstream
phase**, and the mechanism is fully diagnosable — see the cross-check below.

### Earnings play

`uw insights earnings-play --days-until-earnings 30` returned **10 tickers;
FSLR absent**. Correct: `next_earnings_date` is **2026-10-29**, ~90 days out.
**Out of window — no earnings-play commentary applies.** Consistent with
phase-4's `front-end-iv-ratio` **FLAT** (no event premium priced) and
phase-6's catalyst calendar (no company-specific catalyst inside 30 days).

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|------------------|--------------------------|-----------|
| `uw insights deep-dive --symbol FSLR --date 2026-07-31 --json` | `.yahoo_fundamentals` = `{"error":"yahoo quoteSummary FSLR: HTTP 401"}`; `.uw_dark_pool` total_shares=488393/trade_count=251/total_premium=103647999.45; `FSLR270115C00220000` oi_diff_plain=349, volume=1029 ← `.uw_top_oi_changes[3]` | 1 |
| `uw insights signal-confluence --direction bullish --min-score 1 --top-n 20 --date 2026-07-31 --json` | FSLR absent ← `[.results[].ticker]\|index("FSLR")`; DXCM score=6 ← `.results[0]` | 20 |
| `uw insights signal-confluence --direction bullish --min-score 1 --top-n 300 --date 2026-07-31 --json` | FSLR still absent; score distribution 4:267 / 5:31 / 6:2 ← `[.results[].score]\|group_by(.)` | 300 |
| `uw insights signal-confluence --direction bearish --min-score 1 --top-n 300 --date 2026-07-31 --json` | **FSLR score=3**, factors=["bearish_flow","oi_building_puts","high_iv_sell_premium"], volume_ratio=1.86 ← `[.results[]\|select(.ticker=="FSLR")]\|.[0]` | 300 |
| `uw insights conviction-matrix --symbol FSLR --date 2026-07-31 --json` | scenario="MIXED", confidence_pct=8.8, dark_pool.buy_ratio=0.588, options_flow.call_ask_volume=11760 ← `.` | 1 |
| `uw insights price-vs-flow --symbol FSLR --lookback-days 30 --json` | divergence=false, flow_direction="bearish", price_change_pct=−18.11, period_low=195.84 ← `.` | 30 |
| `uw insights analyst-vs-flow --symbol FSLR --json` | **only `.symbol` and `.options_flow` returned — no analyst keys** ← `keys` | 1 |
| `uw insights institutional-accumulation --symbol FSLR --json` | signal="NEUTRAL — balanced dark pool activity", buy_sell_ratio=1.43, total_dp_volume=488393, dark_pool_trades=251 ← `.`; 212.97 shares=144878/trades=3 ← `.top_price_levels[0]` | 1 |
| `uw insights earnings-play --days-until-earnings 30 --date 2026-07-31 --json` | 10 results, FSLR absent ← `[.results[]\|select(.ticker=="FSLR")]` | 10 |

## Tool errors

All nine commands exited 0. **One hard data failure and one systemic defect:**

1. **`uw insights deep-dive` — Yahoo fundamentals leg failed:**
   ```
   {"error":"yahoo quoteSummary FSLR: HTTP 401"}
   ```
   The command returns 0 and delivers its UW-sourced blocks (`uw_screener`,
   `uw_dark_pool`, `uw_top_oi_changes`), but **`.yahoo_fundamentals` is an
   error object**. HTTP 401 is authentication/rate-limiting at Yahoo, not a
   missing symbol. Beyond the documented "1–2 quarters stale" pitfall — there
   is **no fundamental data at all** on this path.

2. **`uw insights analyst-vs-flow` silently degraded** — returned only
   `symbol` and `options_flow`, with **no analyst consensus, target or
   rating**, and **no error field**. Same Yahoo root cause. A caller checking
   only the exit code would not notice. **The tool's entire stated purpose
   (Wall Street vs options-trader agreement) could not be evaluated.**

3. **Cancelled-trade inflation is systemic, not tool-local.** Four UW tools
   report FSLR's dark pool as **488,393 shares / 251 trades / $103,647,999**
   against phase-2's parquet-verified **416,193 / 250 / $88,271,601** — a
   difference of exactly the one 72,200-share `canceled = True` print:
   `deep-dive.uw_dark_pool`, `conviction-matrix.dark_pool`,
   `institutional-accumulation`, and (from phase 2) `block-stratified`,
   `largest` and `price-levels`. **Any UW dark-pool aggregate for FSLR today
   is overstated by 17.4% in premium.**

4. **`--top-n` masks absence.** The first `signal-confluence` call at
   `--top-n 20` made FSLR look unscored; re-running at 300 revealed a bearish
   score of 3 and a bullish score below the list's floor of 4. **"Absent" at
   small top-N is not evidence of a low score** — it must be re-run wide, as
   the phase-7 guidance requires.

## Cross-check vs phases 1–6

| UW insight | Value | Phase agreement? | Notes |
|------------|-------|------------------|-------|
| `signal_confluence` (bearish) | **3/6** | **Partial** | Of three factors: `bearish_flow` is the artifact phase 1 disproved; `oi_building_puts` is phase-3-confirmed but is a *protective ladder* under a call-heavy far book; `high_iv_sell_premium` is phase-5's VRP — a **volatility**, not directional, signal. **≤1 of 3 survives as directional evidence.** |
| `signal_confluence` (bullish) | **absent, score ≤3** | **Agrees** | Phase 1 rated its own bullish read only **2/5**; phase 5 found no historical edge. FSLR is genuinely not a clean bullish setup. |
| `conviction_matrix` | **MIXED, 8.8%** | **Agrees** | Matches phase-1 (2/5), phase-3 (2/5), phase-5 (2/5). The composite's low confidence is the honest read. |
| `conviction_matrix` options volumes | 11,760 / 9,646 / 3,612 / 2,935 | **Exact match** | Reproduces phase-1's DuckDB aggressor split **contract-for-contract** — mutual validation. Cross again excluded. |
| `institutional_accumulation` | **NEUTRAL**, ratio 1.43 | **DISAGREES with phase 2** | Phase 2 = **ACCUMULATION** (conviction 3/5). Two identifiable causes: (a) this tool blends all sessions, and phase 2 showed the regular session is **73.1% buy** while the close is a **6.8%** NBBO artifact; (b) it counts the **cancelled 72,200-share print**. **Phase 2's session-decomposed read is the more reliable.** |
| `price_vs_flow` | **no divergence** | **Partial** | Correct over 30 days; **stale for the last 12 sessions**, which phase 5 showed were flat (211.93 → 211.03). Both of its inputs — the −18.11% and the "bearish" label — describe a window that has stopped operating. |
| `analyst_vs_flow` | **degraded** | **n/a** | Analyst leg empty (Yahoo 401). Cannot be cross-checked. |
| `deep_dive` `uw_screener` | net_flow −$2,374,671 | **Agrees** | Matches phases 0.5 and 1 exactly. |
| `deep_dive` `uw_dark_pool` | 488,393 sh / $103.6M | **DISAGREES with phase 2** | Overstated by exactly the cancelled print (phase-2 verified 416,193 / $88.27M). |
| `earnings_play` | FSLR absent | **Agrees** | Consistent with phase-6 (earnings 2026-10-29) and phase-4 (`front-end-iv-ratio` FLAT). |

## Verdict for downstream phases

- **UW composite bias: MILDLY BEARISH / MIXED.** Taken at face value the
  instrumentation says: bearish confluence 3, bullish absent, conviction
  MIXED at 8.8%, accumulation NEUTRAL, no divergence. **Taken at face value it
  should be the baseline** — and phase 9 is instructed to treat it as such.
- **Conviction: 2 / 5.** Low, for reasons internal to the composite itself:
  `confidence_pct` is **8.8**; the fundamentals and analyst legs **failed
  outright** (Yahoo 401); every dark-pool aggregate is inflated **17.4%** by a
  cancelled print; and the bearish score's dominant factor is a measure
  phase 1 demonstrated omits 9.5% of the tape.
- **Guidance for phase 9 — the baseline and where to override it.** The
  phase-7 rule is to adopt this composite as the baseline and override *only*
  with specific contrary evidence. **That evidence exists and is documented**:
  1. **`bearish_flow` is measurement, not phenomenon.** `phase-1-flow.md`
     reconciles UW's own `bullish_premium`/`bearish_premium` to the cent from
     raw parquet and shows **$2,545,750 (9.5%)** is dropped as `mid`/`no_side`,
     including a **$1.805M cross at `nbbo_ask` exactly**
     (`pos_in_spread = 1.000`, OI 255, vol/OI 7.6×). Corrected: net premium
     ≈ **−$0.57M**, net customer **delta +$10.73M long**.
  2. **`phase-2-dark-pool.md` independently identified that cross's dealer
     hedge** — 72,200 shares, **49.0-second** lag, **101.1%** size match,
     `qualified_contingent_trade`, printed **above the ask**. The dealer bought
     stock to hedge a short call, so **the customer bought the calls**. Two
     independent datasets, one conclusion.
  3. **`institutional_accumulation = NEUTRAL` fails on session decomposition**
     — regular session **73.1% buy** (63.2% ex-hedge) versus a **6.8%**
     closing-auction figure that is mechanically produced by prints at 211.03
     against a stale NBBO of [210.00, 213.00]. The five-session trend
     (44.5 → 36.8 → **28.4** → 64.2 → **73.1**) flips exactly at the earnings
     date.
  **Phase 9 should override the composite's directional label while retaining
  its low conviction.** The correct synthesis is not "bearish" but
  **"balanced-to-mildly-constructive, with genuinely low confidence"** — and
  the composite's **`high_iv_sell_premium`** factor should be carried forward
  at full weight, because it is the one factor every phase corroborates.
- **Open questions:**
  - **Does the composite's `bearish_flow` factor ever correct for crosses?**
    If not, every FSLR confluence score is structurally biased on days with
    large block prints — a calibration item, not a trade input.
  - **What is the analyst consensus and price target?** The Yahoo 401 left
    this entirely unanswered, and it is a required input for phase-7c's
    revision-trend gate. **Phase 7c must source it via WebSearch or `fz`.**
  - **Is the $220 strike the market's chosen expression?** Two of the largest
    OI builds are $220 calls in different tenors (Sep-18 **+985**, Jan-2027
    **+349**), and $220 is where phase-4 finds a **negative** gamma pocket
    (net_gex −620,582) just above the +2.34M wall at 217.5. **A break above
    217.5 into a short-gamma pocket at 220 with call OI accumulating there is
    the most plausible upside-acceleration mechanism in this run** — phases
    8 and 9 should test it.
  - **Why does FSLR score `oi_building_puts` when its far book is
    22,142 calls to zero puts (Jan-2028)?** The factor appears to weight
    near-dated OI only, which for a name with FSLR's barbell structure
    inverts the true positioning read.
