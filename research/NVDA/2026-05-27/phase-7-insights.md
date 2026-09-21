# Phase 7 — UW Insights Confluence

**Ticker:** NVDA
**As-of date:** 2026-05-27
**Generated:** 2026-05-28T02:50:00Z
**Upstream phases cited:** phase-0.5-context.md, phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-4-structure.md

## Summary

UW's composite tools converge on a **single, internally-consistent label** that
ties phases 1-4 together: **`scenario = COVERED_CALL` — "Dark pool buying + call
selling — yield enhancement, capping upside"** [INSIGHT:conviction_matrix].
Mechanically: institutional longs are *held* (DP buy_ratio 0.668, buy_sell_ratio
2.02, signal `ACCUMULATION`) but **upside is being mechanically capped** by call
writing at $215–$220 (matching the GEX walls and OI builds in phases 3-4). The
options tape is `flow_sentiment: bearish` (net_flow −$66.25M, P/C 0.396) and
`price_vs_flow` shows **DIVERGENCE** (price +6.9% over 30d but flow bearish) —
the classic reversal antechamber. Crucially NVDA is **absent from
`signal-confluence`** at min-score 1 in **both directions** — the composite
scoring tool finds no clean directional stack, again consistent with a
yield-enhancement (not directional) regime. Confidence on the COVERED_CALL
scenario itself is **only 19.9%**, meaning UW classifies the *fit* but warns
the pattern is fragile.

## Key signals

- **Scenario = COVERED_CALL, confidence 19.9%, explanation: "yield enhancement,
  capping upside"** [INSIGHT:conviction_matrix] — defines the whole trade.
- **`price_vs_flow` DIVERGENCE = true** (price +6.9% over 30d, flow bearish,
  net_flow −$66.25M) [INSIGHT:price_vs_flow] — reversal antechamber.
- **`institutional_accumulation` signal = ACCUMULATION** (buy_sell_ratio 2.02,
  buy 33.96M / sell 16.85M) [INSIGHT:institutional_accumulation] — but
  the top price level is **$212.60 with 16.3M shares** (the after-hours close
  cluster from phase-2), so the "accumulation" is heavily MOC-weighted.
- **NVDA NOT in signal-confluence (either direction) at min-score 1**
  [INSIGHT:signal_confluence] — no clean directional confluence; mixed signal.
- **`analyst_vs_flow` flow_sentiment = bearish** (net_flow −$66M); analyst
  consensus not returned by yfinance this run [INSIGHT:analyst_vs_flow].

## Detailed findings

### Deep-dive snapshot (`uw insights deep-dive`) — [INSIGHT:deep_dive]

Already surfaced in phase-0.5. Whole-tape directional aggregates (re-cited here
for the reconciliation):

| Field | Value |
|-------|------:|
| call_premium | $1,482,343,454 |
| put_premium | $342,603,767 |
| bullish_premium | $575,068,095 |
| bearish_premium | $641,319,214 |
| **net_flow (bull−bear)** | **−$66,251,119** |
| put_call_ratio | 0.396 |
| implied_move | $4.12 (1.94%) |
| iv_rank | 30.5 / iv30d 0.375 |
| total_open_interest | 15,940,062 |
| next_earnings_date | 2026-08-26 |
| dark_pool total_premium | $10.76B (50.81M shares; avg $211.40) |

### Signal confluence — [INSIGHT:signal_confluence]

| Direction | NVDA in top-50? | Score |
|-----------|-----------------|------:|
| bullish (min-score 1) | **No** | <1 |
| bearish (min-score 1) | **No** | <1 |

The composite confluence tool does not find a clean directional stack for NVDA
today. This is *consistent* with the COVERED_CALL label — a yield-enhancement
pattern is *not* a directional confluence trade.

### Conviction matrix — [INSIGHT:conviction_matrix]

| Field | Value |
|-------|------:|
| **scenario** | **COVERED_CALL** |
| confidence_pct | 19.9% |
| **explanation** | **"Dark pool buying + call selling — yield enhancement, capping upside."** |
| dark_pool.buy_ratio | 0.668 |
| dark_pool.buy_volume | 33,964,338 |
| dark_pool.sell_volume | 16,850,223 |
| options_flow.call_ask_vol | 1,075,106 |
| options_flow.call_bid_vol | **1,214,465** (calls being *hit*) |
| options_flow.put_ask_vol | 454,818 |
| options_flow.put_bid_vol | 462,019 |
| thresholds | bear 0.40, bull 0.60 |

The dark-pool buy_ratio (0.668) is in "bull" zone, but the options call_bid >
call_ask is the call-selling signature, so the matrix labels the combination
COVERED_CALL rather than DIRECTIONAL_LONG. Confidence is *low* (19.9%) — UW is
telling us the pattern fits the rules but is not a high-conviction read.

### Price vs flow — [INSIGHT:price_vs_flow]

| Field | Value |
|-------|------:|
| price_start (30d ago) | $198.87 |
| price_end | $212.60 |
| **price_change_pct** | **+6.9%** |
| period_high | $236.54 |
| period_low | $194.74 |
| flow_direction | **bearish** |
| net_premium_flow | −$66.25M |
| **divergence** | **true** |
| divergence_signal | "Price is up 6.9% but options flow is bearish (net flow: $-66.25M)" |

The 30-day window net is +6.9%, hiding a peak-to-now drawdown of −9.8% from
$235.74 (phase-5). Smart money has been selling premium into the rally; price
is now rolling over.

### Analyst vs flow — [INSIGHT:analyst_vs_flow]

| Field | Value |
|-------|------:|
| flow_sentiment | **bearish** |
| net_flow | −$66.25M |
| P/C ratio | 0.396 |
| analyst consensus | (not returned; yfinance) |

Without analyst consensus this is just a re-statement of phase-1's flow read.
Phase-7c will pull analyst revision data via Finnhub/`fz`.

### Institutional accumulation — [INSIGHT:institutional_accumulation]

| Field | Value |
|-------|------:|
| signal | **ACCUMULATION** — "dark pool buy volume significantly exceeds sell volume" |
| buy_sell_ratio | 2.02 |
| buy_side_volume | 33,964,338 |
| sell_side_volume | 16,850,223 |
| avg_trade_price | $211.40 |
| top_price_levels | $212.6 ($3.47B, 16.34M sh), $213.2, $212.36, $210.70, $210.15 |

The top price level alone (`$212.60 / 16.3M sh / $3.47B`) accounts for ~70% of
mega-tier premium (phase-2: mega $3.63B). The accumulation signal is real but
heavily concentrated in the after-hours close cluster — a *mechanical* (MOC) tilt,
not 30 days of clean accumulation. Read: held, not bought aggressively.

### Earnings play

Next earnings 2026-08-26 — **outside the 30-day catalyst window**; tool skipped.

## Tool calls (audit trail)

| Command | Result summary |
|---------|----------------|
| `uw insights deep-dive --symbol NVDA --date 2026-05-27` | full snapshot (cited above) |
| `uw insights signal-confluence --direction bearish --min-score 1` | NVDA not in top-50 |
| `uw insights signal-confluence --direction bullish --min-score 1` | NVDA not in top-50 |
| `uw insights conviction-matrix --symbol NVDA` | **COVERED_CALL, conf 19.9%** |
| `uw insights price-vs-flow --lookback-days 30` | DIVERGENCE true (+6.9% price / bearish flow) |
| `uw insights analyst-vs-flow --symbol NVDA` | flow bearish; analyst portion empty |
| `uw insights institutional-accumulation --symbol NVDA` | ACCUMULATION (buy_sell_ratio 2.02) |
| `uw insights earnings-play` | skipped — earnings 2026-08-26 outside 30d |

## Tool errors

- `uw insights analyst-vs-flow` returned only options_flow fields; no analyst
  consensus block (yfinance pull empty). Phase-7c will source analyst
  consensus/revisions via Finnhub.

## Cross-check vs phases 1-5

| UW insight | Phase agreement? | Notes |
|------------|------------------|-------|
| `conviction_matrix` = COVERED_CALL | **Agrees** with phases 1+3+4 | Explains the seeming bearish-flow vs DP-buying contradiction as one mechanical structure (yield enhancement, capping upside at $215-220). |
| `price_vs_flow` DIVERGENCE | **Agrees** with phase-1 (bearish net_flow despite NVDA still well above 50/200 SMA per phase-5 `fz`) | Reversal antechamber confirmed by the 13-session rollover from $235 → $212. |
| `institutional_accumulation` = ACCUMULATION | **Partially agrees** with phase-2 | The ratio is real, but the 70% concentration in $212.60 MOC prints means phase-2's "mechanical" caveat stands — re-rate as held-not-bought. |
| `signal_confluence` absent both directions | **Agrees** with phase-5 (weak edge) | The composite is correctly cautious — no clean directional stack supports an outright long or short. |
| `analyst_vs_flow` flow_sentiment bearish | Agrees with phase-1 | Awaiting phase-7c for the analyst leg. |

## Verdict for downstream

- **UW composite bias:** **CAPPED-UPSIDE / NEUTRAL-TO-MILDLY-BEARISH** — the
  composite is best characterised as a *covered-call regime* (held, not bought
  or sold aggressively) with a confirmed price/flow divergence pointing to
  near-term downside risk.
- **Conviction:** **3/5** — the COVERED_CALL label is internally coherent and
  agrees with phases 1-4, but UW's own confidence on it is 19.9% and
  signal-confluence is empty. Treat as the baseline.
- **Phase 9 should treat this as BASELINE** and only override with specific
  contrary evidence: it should size for a defined-risk *upside-capped* /
  *mild-bearish* trade rather than an outright directional long or short.
- **Open questions:**
  - Does Finnhub analyst sentiment (phase-7c) reinforce or contradict the
    "long-but-capped" institutional posture?
  - Are the call-writers' strikes (215/217.5/220) the right *short call legs*
    for a phase-9 call-spread short, or is implied move (±$4.12) too tight for
    the short call to be worth the credit?
