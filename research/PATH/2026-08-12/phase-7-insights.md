# Phase 7 — UW Insights Confluence

**Ticker:** PATH
**As-of date:** 2026-08-12
**Generated:** 2026-08-13T02:50:00Z
**Upstream phases cited:** phase-0.5-context.md, phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-4-structure.md, phase-5-historical.md

## Summary

UW's composite tools mostly agree with the phase-by-phase read rather than
adding a new signal: PATH is **absent from both bullish and bearish
`signal-confluence` top-20 lists** (no material composite score either way),
and `conviction-matrix` classifies today as **`COVERED_CALL`** (dark-pool
buying + call-selling, "yield enhancement, capping upside") at only **25%
confidence**. The most important new datapoint this phase surfaces is
`price-vs-flow`'s explicit **`DIVERGENCE: Price is up 32.1% but options flow
is bearish`** — a leading (if "often early," per the tool's own heuristic)
reversal signal that corroborates phase-4's long-gamma/mean-reversion regime
and phase-5's overbought-RSI/decelerating-OI-build read. `institutional-
accumulation` returns `ACCUMULATION` (`buy_sell_ratio=2.67`), but — flagged
explicitly here — it's built on the **same blended, after-hours-artifact-
inflated dark-pool ratio phase-2 already de-weighted** (0.727 blended vs.
phase-2's cleaner 0.678 large-tier-only read), so its confidence should not be
taken at face value. `analyst-vs-flow` has no analyst consensus (yfinance
401, a known limitation) — only the flow leg populated, matching phase-1
exactly. PATH does not appear in the market-wide `earnings-play` top-10
despite reporting on 2026-09-03 (phase-6) — other same-day reporters (SHOE,
SPWH) outrank it, so PATH isn't among today's most extreme earnings-IV setups.

## Key signals

- PATH absent from `signal-confluence` top-20 both directions (min-score 1) —
  no strong composite score [INSIGHT:signal_confluence]
- `conviction-matrix scenario=COVERED_CALL`, `confidence_pct=25` — low
  confidence [INSIGHT:conviction_matrix]
- `price-vs-flow divergence=true`: **"Price is up 32.1% but options flow is
  bearish (net flow: $-44,378)"** [INSIGHT:price_vs_flow]
- `institutional-accumulation signal=ACCUMULATION`, `buy_sell_ratio=2.67` —
  **built on the blended/artifact-affected DP ratio, not phase-2's cleaner
  ex-mega read** [INSIGHT:institutional_accumulation]
- `analyst-vs-flow`: no analyst consensus (yfinance 401); flow leg matches
  phase-1 exactly (`bearish`, `net_flow=-44378`) [INSIGHT:analyst_vs_flow]

## Detailed findings

### Deep dive snapshot

(Reused from phase-0.5/phase-1's `uw insights deep-dive --symbol PATH
--date 2026-08-12` call — same object, no re-fetch needed.)

- `uw_screener`: `bullish_premium=$1,440,177`, `bearish_premium=$1,484,555`,
  **derived `net_flow = -$44,378`**, `call_premium=$2,254,097`,
  `put_premium=$1,074,984`, `put_call_ratio=0.4748`, `implied_move=$0.50`,
  `implied_move_perc=3.29%`, `iv_rank=63.16` — all reconcile exactly with
  phase-0.5 and phase-1's whole-tape reads.
- `uw_dark_pool`: `total_premium=$306,421,986`, `total_shares=20,132,766`,
  `trade_count=2,015` — reconciles exactly with phase-2's
  `total_premium_all_tiers`.
- `uw_top_oi_changes`: top rows match phase-3's `biggest-increases` table.
- `yahoo_fundamentals`: **`{"error":"yahoo quoteSummary PATH: HTTP 401"}`** —
  known yfinance-blocked limitation; no PE/market-cap/short-% cross-check
  available from this leg this run (phase-7b's Finnhub/fz path is the
  fundamentals source of record).

### Signal confluence

`uw insights signal-confluence --direction bullish --min-score 1 --top-n 20`
and `--direction bearish` (same params): **PATH appears in neither the
bullish nor the bearish top-20**, even at the minimum score threshold of 1.
Since both returned lists are full at 20 rows (other tickers filled every
slot), this means PATH's composite factor score is low enough to be crowded
out in both directions — not a data gap, a genuine "no strong composite
signal" read. Consistent with phase-0.5's `BUSY_NAME_NORMAL_DAY`.

### Conviction matrix

`uw insights conviction-matrix --symbol PATH`: `scenario=COVERED_CALL`,
`confidence_pct=25`, `explanation="Dark pool buying + call selling — yield
enhancement, capping upside."` Inputs: `dark_pool.buy_ratio=0.727`
(`buy_volume=14,641,164` vs `sell_volume=5,491,602` — **this is the blended
mega+large figure**, not phase-2's cleaner ex-mega `large`-tier-only
`buy_ratio=0.678`); `options_flow.call_bid_volume=7,790` >
`call_ask_volume=7,108` (more call-selling-into-bid than call-buying-at-ask
today, consistent with phase-3's broad call-OI unwind). The scenario
classification is directionally reasonable (dark-pool buying paired with
call supply matches a covered-call/yield-enhancement read) but rests partly
on the artifact-affected DP number — treat the 25% confidence as, if
anything, generous.

### Price vs flow

`uw insights price-vs-flow --lookback-days 30`: `price_start=$11.55`,
`price_end=$15.26`, `price_change_pct=+32.12%`, `period_high=$16.04`,
`period_low=$10.16`, `flow_direction=bearish` (today), `divergence=true`,
**`divergence_signal="DIVERGENCE: Price is up 32.1% but options flow is
bearish (net flow: $-44378)"`**. This is the clearest new signal this phase
adds. Per the skill's own interpretation heuristic, price/flow divergence is
"a leading reversal signal but often early — pair with phase-4 dealer
regime before sizing on it": phase-4 found `POSITIVE` (long) gamma, which
mechanically favors mean-reversion, not trend continuation — the divergence
and the dealer regime **point the same way** (a reason for caution on chasing
further upside, not a reason to flip bearish outright). Spot ($15.26) sits
−4.9% below the 30-day high ($16.04) and +50.2% above the 30-day low
($10.16).

### Analyst vs flow

`uw insights analyst-vs-flow --symbol PATH`: only the `options_flow` block
populated (`bearish_premium=$1,484,555`, `bullish_premium=$1,440,177`,
`flow_sentiment=bearish`, `net_flow=-44378`) — identical to phase-1's
whole-tape read. **No analyst-consensus block returned** (the yfinance 401
affects this tool too, same root cause as the deep-dive snapshot's
`yahoo_fundamentals` error) — no Wall-Street-vs-options-trader agreement
read is possible from this tool this run; phase-7b/7c carry the analyst
consensus via Finnhub/fz instead.

### Institutional accumulation

`uw insights institutional-accumulation --symbol PATH`: `signal="ACCUMULATION
— dark pool buy volume significantly exceeds sell volume"`,
`buy_sell_ratio=2.67`, `buy_side_volume=14,641,164`,
`sell_side_volume=5,491,602`, `price_30d_change_pct=32.12%` (matches
price-vs-flow), `vwap=$15.22`. **Cross-check note:** `buy_side_volume`
(14,641,164) is exactly `phase-2's mega (3,096,277) + large (11,544,887) buy
volumes combined` — i.e. this signal is computed on the blended figure that
phase-2 explicitly flagged as artifact-inflated by the single after-hours
print. The underlying regular-session data still supports *some* accumulation
read (phase-2's clean `large`-tier `buy_ratio=0.678` is real and
"suggestive"), but the `2.67`/`ACCUMULATION` framing here overstates
conviction relative to phase-2's more careful decomposition. `top_price_
levels` cluster tightly $15.19–$15.26 — the near-spot congestion zone phase-2
already mapped.

### Earnings play

`uw insights earnings-play --days-until-earnings 30`: **PATH absent from the
top-10** market-wide results, even though other 2026-09-03 reporters (SHOE,
SPWH) appear — the tool is evidently ranking by something like `iv_rank`
extremity (both visible SHOE/SPWH rows show `iv_rank=100`) rather than simply
days-to-earnings, and PATH's `iv_rank=63.16` (phase-0.5) doesn't clear that
bar. Not an error — PATH's own earnings setup is already fully covered by
phase-0.5 (`iv_rank=63.16`, `implied_move_perc=3.29%`) and phase-6
(`earnings_date=2026-09-03`, cross-checked via WebSearch).

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw insights signal-confluence --direction bullish --min-score 1 --top-n 20 --date 2026-08-12 --json` | PATH absent ← `.results[]\|select(.ticker=="PATH")` | 20 |
| `uw insights signal-confluence --direction bearish --min-score 1 --top-n 20 --date 2026-08-12 --json` | PATH absent (same filter) | 20 |
| `uw insights conviction-matrix --symbol PATH --date 2026-08-12 --json` | `scenario=COVERED_CALL, confidence_pct=25` ← top-level | 1 |
| `uw insights price-vs-flow --symbol PATH --lookback-days 30 --date 2026-08-12 --json` | `divergence=true, price_change_pct=32.12` ← top-level | 1 |
| `uw insights analyst-vs-flow --symbol PATH --date 2026-08-12 --json` | `flow_sentiment=bearish` ← `.options_flow` | 1 |
| `uw insights institutional-accumulation --symbol PATH --date 2026-08-12 --json` | `signal=ACCUMULATION, buy_sell_ratio=2.67` ← top-level | 1 |
| `uw insights earnings-play --days-until-earnings 30 --date 2026-08-12 --json` | PATH absent ← `.results[]\|select(.ticker=="PATH")` | 10 |
| (reused) `uw insights deep-dive --symbol PATH --date 2026-08-12 --json` | `yahoo_fundamentals.error="HTTP 401"` ← `.yahoo_fundamentals` | 1 |

## Tool errors

- `yahoo_fundamentals` (nested inside `uw insights deep-dive`) and the
  analyst-consensus leg of `uw insights analyst-vs-flow` both return
  effectively empty due to a yfinance HTTP 401 — a known, standing limitation
  (not specific to this run). No fabricated substitute recorded; phase-7b/7c
  carry fundamentals/analyst data via Finnhub and `fz` instead.

## Cross-check vs phases 1–5

| UW insight | Phase agreement? | Notes |
|---|---|---|
| `signal_confluence` (absent both directions) | **Agrees** with phase-0.5 (`BUSY_NAME_NORMAL_DAY`) and phase-1 (mixed/neutral, 2/5 conviction) | No composite score in either direction |
| `conviction_matrix=COVERED_CALL` | **Partially agrees** with phase-2 (mild accumulation) and phase-3 (call OI unwind today) | Confidence only 25%; built partly on phase-2's flagged artifact-inflated DP ratio |
| `price_vs_flow` divergence | **Corroborates** phase-4 (`POSITIVE`/long-gamma → mean-reversion) and phase-5 (RSI 70.94 overbought, smallest OI-build day of the 29-day streak) | Three independent phases now converge on "rally due a pause" |
| `institutional_accumulation=ACCUMULATION` | **Overstates** phase-2's own more careful read | phase-2's clean ex-mega `large`-tier `buy_ratio=0.678` is real but "suggestive," not the 2.67 ratio's implied confidence |
| `analyst_vs_flow` (flow leg only) | **Agrees exactly** with phase-1's whole-tape `net_flow=-44378` | No new information; analyst leg unavailable (yfinance 401) |

## DATA NOTE / CORRECTION

<none — first read stood. The blended-vs-clean dark-pool ratio discrepancy
noted above is an interpretation caveat carried forward from phase-2, not a
mis-read here.>

## Verdict for downstream phases

- **UW composite bias:** Mixed, mildly structurally-constructive
  (`COVERED_CALL`/`ACCUMULATION`-flavored) but explicitly flagged low-
  confidence, with a real reversal-risk `DIVERGENCE` signal that phase-4 and
  phase-5 both independently corroborate.
- **Conviction:** 2/5 — no single UW composite tool clears its own
  high-confidence bar today (25% conviction-matrix confidence; absent from
  signal-confluence entirely; accumulation signal inherits phase-2's
  artifact caveat).
- **Phase 9 baseline:** Treat this phase's composite as **directionally
  neutral-to-cautiously-constructive**, with the price/flow divergence as the
  one point phase-9 should weight most (it's independently corroborated by
  phase-4 and phase-5, not a standalone read). Phase 9 should NOT treat
  `institutional_accumulation`'s 2.67 ratio as a clean override of phase-2's
  more careful 0.678 read.
- **Open questions:** Does phase-7b's fundamentals read (once the yfinance
  gap is filled via Finnhub) support the valuation implied by a +32% six-week
  rally, or does it argue the move has outrun the fundamentals? Does phase-8's
  multi-agent debate resolve the `COVERED_CALL` framing (bullish-neutral,
  capped upside) against the `DIVERGENCE` reversal-risk framing (caution)?
