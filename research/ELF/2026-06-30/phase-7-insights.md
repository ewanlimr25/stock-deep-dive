# Phase 7 — UW Insights Confluence

**Ticker:** ELF
**As-of date:** 2026-06-30
**Generated:** 2026-07-01T00:39:05Z
**Upstream phases cited:** phase-0.5-context.md, phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-4-structure.md, phase-5-historical.md

## Summary

The UW composite reads **bullish but weak/borderline — and it overstates the dark-pool
conviction.** `conviction-matrix` labels ELF **DIRECTIONAL_LONG** but at only **49.9%
confidence** (dead-center between the 0.40 bear / 0.60 bull thresholds). `price-vs-flow`
finds **no divergence** (price and flow aligned bullish, +34.9%/30d). But the two tools
that scream "accumulation" — `conviction-matrix`'s DP leg (buy_ratio 0.948) and
`institutional-accumulation` (ACCUMULATION, buy/sell 18.26) — are **both inflated by the
single $241M quarter-end rebalance cross** (3.24M sh = 87% of the day's DP volume) that
phase-2 correctly de-rated to non-directional. The honest DP read is phase-2's stripped
**large-tier buy_ratio 0.61**. Meanwhile ELF is **absent from `signal-confluence` in both
directions even at min-score 1** — it is not a market-leading confluence name (consistent
with phase-0.5's "outside top-50 absolute"). So the composite baseline is a **mild
DIRECTIONAL_LONG that must be discounted for the rebalance-cross artifact** — squarely in
line with the phases-1–5 stack: real bullish tilt, but extended, churny, and
mean-reverting.

## Key signals

- **conviction-matrix = DIRECTIONAL_LONG, confidence 49.9%** (borderline; bull thresh 0.60) [INSIGHT:conviction-matrix]
- **institutional-accumulation = ACCUMULATION but buy/sell 18.26 is a rebalance-cross artifact** ($241M/3.24M-sh single print = 87% of DP vol) [INSIGHT:institutional-accumulation]
- **price-vs-flow: NO divergence** — aligned bullish, +34.89%/30d (low $48.82 = 52-wk low, high $74.49) [INSIGHT:price-vs-flow]
- **ELF absent from signal-confluence (both directions, min-score 1)** — not a top composite-score name [INSIGHT:signal-confluence]
- **deep-dive: net_flow +$1.22M, P/C 0.184, IV rank 46.8, implied move ±3.52%** [INSIGHT:deep-dive]

## Detailed findings

### Deep-dive snapshot `[INSIGHT:deep-dive]` (`uw_screener` whole-tape block)

| Field | Value |
|---|---|
| bullish_premium / bearish_premium | $5,972,371 / $4,752,027 |
| **net_flow (derived)** | **+$1,220,344** bullish |
| call_premium / put_premium | $13,319,462 / $1,210,166 |
| put_call_ratio | 0.184 |
| implied_move / implied_move_perc | 2.606 / **3.52%** (phase-9 N4) |
| iv_rank | 46.83 |
| total_open_interest | 92,758 |
| next_earnings_date | **2026-08-05** |

Reconciles exactly with phase-1's aggregate and phase-0.5's `[CTX:]` (net +$1.22M,
96.8/97.9 universe pctile). Yahoo fundamentals block returned null (sector/price/mktcap
null) this run — company financials deferred to phase-7b (mkt cap ~$4.40B, close $74,
P/E ~26 from `fz`).

### Signal confluence `[INSIGHT:signal-confluence]`

- **ELF absent from the bullish list AND the bearish list at `--min-score 1`.** Its
  composite factor score does not clear the market-wide top-20 threshold in either
  direction. Read: not a high-confluence name — the bullish signal is real but not
  stacked across the maximum number of independent factors (a "≥5 confluence" name it is
  not). Consistent with phase-0.5 (outside top-50 absolute).

### Conviction matrix `[INSIGHT:conviction-matrix]`

- `scenario` = **DIRECTIONAL_LONG**; `confidence_pct` = **49.9%** (thresholds bull 0.60 /
  bear 0.40 → this is *borderline*, not a conviction long).
- `explanation` = "Dark pool buying + aggressive call purchases — institutional
  directional bet."
- `dark_pool`: buy_ratio **0.948** (buy 3,537,067 / sell 193,708, 119 trades) — **inflated
  by the $241M rebalance cross; treat as phase-2's 0.61, not 0.948.**
- `options_flow`: call_ask 7,207 vs call_bid 5,874 (net +1,333 ask → mild bullish); put_ask
  1,078 vs put_bid 1,742 (net −664 → puts sold, bullish). Options leg mildly bullish,
  matches phase-1.

### Price vs flow `[INSIGHT:price-vs-flow]`

- `divergence` = **false** ("Price and flow are aligned"), `flow_direction` = bullish,
  `net_premium_flow` +$1,220,344.
- `price_change_pct` **+34.89%** (start $54.86 → end $74.00; `period_low` **$48.82** =
  52-wk low, `period_high` $74.49). No reversal signal — but "aligned + extended" is a
  *confirming*, not a *leading*, read: the flow rode the move, it isn't front-running one.

### Analyst vs flow `[INSIGHT:analyst-vs-flow]`

- Returned only the `options_flow` leg (flow_sentiment **bullish**, net_flow +$1.22M);
  the analyst-consensus leg came back empty this run (yfinance ratings not returned).
  Cross-fill from phase-6 WebSearch: **Raymond James Strong Buy, $85 PT** → analyst and
  flow are **aligned bullish** (agreement). The $85 PT ≈ the phase-1/3 $80/$85 call
  strikes.

### Institutional accumulation `[INSIGHT:institutional-accumulation]`

- `signal` = **ACCUMULATION** ("dark pool buy volume significantly exceeds sell volume"),
  `buy_sell_ratio` **18.26**, buy 3,537,067 / sell 193,708, `price_30d_change_pct` +34.89,
  vwap $74.20, avg_trade_price $72.71.
- **CAVEAT (decisive):** `top_price_levels[0]` = **3,242,478 sh / $241.2M @ $74.39 in 1
  trade** = the quarter-end close cross. It is **87% of `total_dp_volume` (3,730,775)**,
  so the 18.26 buy/sell ratio is essentially that one print. **Strip it → phase-2's
  large-tier 0.61 (mild accumulation).** This tool is fooled by the rebalance cross;
  phase-2 is the honest reference.

### Earnings play `[INSIGHT:earnings-play]`

- **ELF not flagged** (`--days-until-earnings 40`): earnings 2026-08-05 is ~36 days out
  and ELF's IV/OI buildup does not register as an earnings-play setup. Out-of-window /
  not-flagged — not a tool error. (The phase-1 Aug-21 call buying may still be
  earnings-anticipation; the composite just doesn't classify it as one yet.)

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows |
|---|---|---|
| `uw insights deep-dive --symbol ELF --date 2026-06-30` (reused from 0.5) | net_flow +$1.22M ← `.uw_screener.bullish_premium − .bearish_premium` | whole-tape |
| `uw insights signal-confluence --direction bullish/bearish --min-score 1 --top-n 20` | ELF absent both ← `index("ELF")==null` | 0 |
| `uw insights conviction-matrix --symbol ELF --date 2026-06-30` | DIRECTIONAL_LONG 49.9% ← `.scenario`,`.confidence_pct` | 1 |
| `uw insights price-vs-flow --symbol ELF --lookback-days 30` | divergence false, +34.89% ← `.divergence`,`.price_change_pct` | 30d |
| `uw insights analyst-vs-flow --symbol ELF --date 2026-06-30` | flow bullish; analyst leg empty ← `.options_flow.flow_sentiment` | 1 |
| `uw insights institutional-accumulation --symbol ELF --date 2026-06-30` | ACCUMULATION 18.26 (cross-inflated) ← `.signal`,`.buy_sell_ratio`,`.top_price_levels[0]` | 119 trades |
| `uw insights earnings-play --days-until-earnings 40 --date 2026-06-30` | ELF absent ← `index("ELF")==null` | 0 |

## Tool errors

_None — all seven reads returned exit 0 and valid JSON. `analyst-vs-flow`'s empty
analyst leg and `earnings-play`'s non-listing are data conditions, not errors._

## Cross-check vs phases 1–5

| UW insight | Phase agreement? | Notes |
|---|---|---|
| signal_confluence (ELF absent) | **agrees** (0.5, 1, 3) | Not a top-tier signal — matches "outside top-50 absolute" + churny OI |
| conviction_matrix DIRECTIONAL_LONG 49.9% | **agrees** (1 bullish, 3/4 tempered) | Borderline confidence mirrors phase-3 churn + phase-4 mean-reversion |
| price_vs_flow (no divergence) | **agrees** (1, 5) | Aligned bullish; but "aligned + extended" ≠ fresh entry |
| institutional_accumulation ACCUMULATION | **direction agrees / magnitude DISAGREES** (2) | Composite inflated by the $241M rebalance cross; phase-2's 0.61 is honest |
| analyst_vs_flow bullish | **agrees** (6) | RJ Strong Buy $85 + bullish flow aligned |

## Verdict for downstream phases

- **UW composite bias:** **MILD BULLISH / borderline DIRECTIONAL_LONG** — with an explicit
  discount: the "strong accumulation" composite reads are a **rebalance-cross artifact**;
  the true DP signal is mild (phase-2 0.61), confidence is only 49.9%, and ELF is not a
  top-confluence name.
- **Conviction:** **3 / 5** — genuinely bullish-tilted and internally consistent with
  phases 1–5, but weak in magnitude and inflated by one print. Not a high-conviction stack.
- **Baseline for phase 9:** treat this as a **weak DIRECTIONAL_LONG baseline**. The
  downside gates (7b fundamentals, 7c sentiment/SI, 8b debate) can only *cut* from here.
  Phase 9 should override the composite's apparent strength **only** where it already has:
  the DP accumulation magnitude is overstated (use phase-2), and the setup is extended
  (phases 4/5) — so size for consolidation/defined-risk, not breakout.
- **Open questions:**
  - Does phase-7b confirm the **fundamental turnaround** (Rhode +80%, Q4 beat) is
    durable, or is the +35% run pricing it fully at P/E ~26 / PEG 2.89 (phase-6)?
  - Does phase-7c show **short interest / crowding** — is the recovery partly a squeeze
    (would cap upside once covered), and how rich is positioning?
  - The composite is fooled by the rebalance cross — phase-8/9 must not double-count it as
    conviction.
