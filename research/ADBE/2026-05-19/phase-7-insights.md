# Phase 7 — UW Insights Confluence

**Ticker:** ADBE
**As-of date:** 2026-05-19
**Generated:** 2026-05-19T22:30:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-4-structure.md, phase-5-historical.md, phase-6-macro.md

## Summary

UW's composite classifier puts ADBE squarely in the **COVERED_CALL
scenario**: dark-pool buying with call SELLING (yield enhancement,
upside capped) `[INSIGHT:conviction_matrix]` — the same conclusion this
phase chain reached by reconciling phase-2 (accumulation) with phase-3's
$265-call OI build (net_ask_bid −786). Independently, the
**institutional-accumulation classifier confirms ACCUMULATION** with a
**buy/sell ratio 1.60** on $173.8M total DP premium
`[INSIGHT:institutional_accumulation]`. **Signal-confluence found ADBE
in NEITHER the top-50 bullish nor the top-50 bearish lists** (even at
the loosest threshold `min_score=1`) — confirming the **MIXED
single-day tape** seen in phases 1, 3, and 5
`[INSIGHT:signal_confluence]`. **`insights_price_vs_flow` flags a
DIVERGENCE: price +6.55% over 30d vs net options flow −$642k bearish**
`[INSIGHT:price_vs_flow]` — a classic late-rally hedging signature
consistent with the COVERED_CALL scenario. ADBE's confirmed Q2 FY26
earnings date **2026-06-11** echoes from the screener
`[INSIGHT:deep_dive]`, matching phase-6's WebSearch finding. **Net
phase-7 baseline: long-stock institutional accumulation overlaid with
short-call yield enhancement and protective put activity into the
6/11 earnings event — a HEDGED LONG / yield-harvest profile, NOT a
clean directional long.**

## Key signals

- **Conviction matrix verdict: `COVERED_CALL`** with explanation "Dark
  pool buying + call selling — yield enhancement, capping upside"
  `[INSIGHT:conviction_matrix]` — reconciles phase-1 & phase-3.
- **Institutional accumulation signal: ACCUMULATION, buy/sell ratio
  1.60, $173.8M total DP premium, 597 trades**
  `[INSIGHT:institutional_accumulation]` — UW echoes phase-2.
- **Signal confluence: ADBE ABSENT from top-50 bullish AND top-50
  bearish lists at min_score=1** `[INSIGHT:signal_confluence]` —
  classifier sees no aligned directional factor stack.
- **Price-vs-flow divergence**: spot +6.55% (start $239.31 → end
  $254.99, period 30d) but net premium flow −$642k bearish; period
  range $224.13-$265.09 `[INSIGHT:price_vs_flow]`.
- **Deep-dive: implied move (near-term) $8.27 / 3.24%; IV rank 89.6;
  next earnings 2026-06-11; total OI 580,390**
  `[INSIGHT:deep_dive]` — short-term implied move is a 1-day vol read,
  NOT the earnings-event move (phase-4's ±9% across 6/12-6/18 is the
  event-specific calc).
- **Yahoo fundamentals returned HTTP 401** `[INSIGHT:deep_dive]` —
  fundamentals (P/E, market cap, short%) unavailable this run.
- **Top OI changes mirror phase-3 exactly**: 5/22 $265C +1,135, 5/22
  $275C +1,011, 5/22 $260P +845, 5/29 $255C +819, 5/22 $260C +771
  `[INSIGHT:deep_dive]`.

## Detailed findings

### Deep dive snapshot

| Metric | Value | Notes |
|--------|-------|-------|
| Symbol | ADBE | Tech / Software |
| Next earnings | **2026-06-11** | Matches phase-6 WebSearch |
| Implied move ($) | $8.27 | Near-term ATM straddle proxy |
| Implied move % | 3.24% | Short-dated; NOT the earnings move |
| IV30d | 0.5555 | Aligns with phase-5 |
| IV rank | **89.6** | High |
| P/C ratio | 0.59 | Slightly call-heavy |
| Call premium | $25.1M | |
| Put premium | $18.8M | |
| Total OI | 580,390 | |
| Volatility (proxy) | 0.5273 | |
| DP avg price | $258.48 | Aligns with phase-2 VWAP $258.73 |
| DP total premium | $173.8M | Aligns with phase-2 |
| DP trade count | 597 | Aligns with phase-2 |
| Yahoo fundamentals | **HTTP 401** | Not available |

### Signal confluence

```
mcp__uw-pp__insights_signal_confluence(direction=bullish, min_score=1, top_n=50)
  → ADBE absent
mcp__uw-pp__insights_signal_confluence(direction=bearish, min_score=1, top_n=50)
  → ADBE absent
```

**ADBE does not appear in EITHER the bullish OR bearish top-50 even at
`min_score=1`.** Interpretation: ADBE's factor stack (flow / pcr /
volume_spike / dp_accumulation / oi_building / iv_position) is too
balanced/mixed for the classifier to assign a directional confluence
score. The strongest bullish names today are SG and TE (both score 6
with all 6 factors aligned bullish at small-cap scale); the strongest
bearish is BNTX (score 6 bearish). ADBE sits in the middle without a
unified factor stack — consistent with the multi-axis tension this
phase chain has been mapping.

### Conviction matrix

| Field | Value |
|-------|------:|
| Scenario | **COVERED_CALL** |
| Confidence % | 13.45 |
| Dark-pool buy_ratio | **0.615** |
| Dark-pool buy_volume | 413,368 |
| Dark-pool sell_volume | 258,566 |
| Call ask_volume | 14,359 |
| Call bid_volume | **15,513** |
| Put ask_volume | 8,793 |
| Put bid_volume | 7,646 |
| Threshold bull | 0.6 |
| Threshold bear | 0.4 |

Explanation from the tool: *"Dark pool buying + call selling — yield
enhancement, capping upside."*

This is the **single most important reconciliation** of the phase chain:
- Phase-1 read the front-end ATM put-buying as "hedging".
- Phase-3 noted the $265 call line was net SOLD (calls written).
- Phase-2 confirmed dark-pool ACCUMULATION at +0.615 buy ratio.
- **Phase-7 puts the three together: institutions are LONG stock,
  WRITING calls above spot, BUYING puts as collar floors — a covered-
  call (or full collar) overlay.**

Confidence is only 13.45% — the classifier flags the read as
non-decisive, which is fair given the divergence and mixed signals.

### Price vs flow

| Field | Value |
|-------|------:|
| Period start price | $239.31 |
| Period end price | $254.99 |
| Period high | $265.09 |
| Period low | $224.13 |
| Price change % | **+6.55%** |
| Flow direction (today) | **bearish** |
| Net premium flow | **−$642,493** |
| Bullish premium | $19,780,045 |
| Bearish premium | $20,422,538 |
| **Divergence flag** | **TRUE** |

Tool signal: *"DIVERGENCE: Price is up 6.6% but options flow is
bearish."*

Reading: price made a 30-day round-trip ($224.13 → $265.09 → $254.99)
and recovered most of the drawdown, but the most recent day's tape
shows bearish net premium. This is a **classic late-rally hedging**
pattern — a holder who is long stock and rode the recovery is now
buying near-the-money puts (phase-1) and writing OTM calls (phase-3)
to lock in part of the gain into earnings. **NOT a reversal signal in
isolation**; it's the COVERED_CALL overlay manifesting in the tape.

### Analyst vs flow

```
mcp__uw-pp__insights_analyst_vs_flow(symbol=ADBE) →
  { options_flow: { sentiment: "bearish", net_flow: -642493, pcr: 0.59 } }
```

The tool returned **no analyst section** in the response — most likely
the yfinance recommendations side failed silently (consistent with the
Yahoo HTTP 401 in the deep-dive). Phase-9 should treat analyst
consensus as **unknown from UW**; phase-6 WebSearch surfaced
qualitative coverage suggesting "**Mixed Wall Street Sentiment**" and
"legal headwinds" alongside the bullish AI / Firefly / buyback story.
**Treat sell-side consensus as MIXED, not bullish, for sizing.**

### Institutional accumulation

| Field | Value |
|-------|------:|
| Signal | **ACCUMULATION** |
| Buy_sell ratio | **1.60** |
| Buy-side volume | 413,368 |
| Sell-side volume | 258,566 |
| Avg trade price | $258.48 |
| VWAP | $258.73 |
| Total DP premium | $173,847,335 |
| Total DP volume | 671,934 |
| 30d price change | +6.55% |
| Top 1 level | $261.86 — $24.1M / 92,057 sh / 1 trade (the mega buy) |
| Top 2 level | $263.20 — $4.7M / 18,040 sh / 4 trades |
| Top 3 level | $252.33 — $3.7M / 14,733 sh / 1 trade |
| Top 4 level | $264.28 — $3.4M / 12,840 sh / 2 trades |
| Top 5 level | $254.30 — $3.1M / 12,020 sh / 8 trades |

Tool signal: *"ACCUMULATION — dark pool buy volume significantly
exceeds sell volume."*

Read: confirms phase-2 verbatim. The $258.73 5-day VWAP is the
institutional anchor; spot at $255 sits below it, meaning the average
institutional buyer of the past 5 sessions is currently $3-4 underwater
on intraday close terms.

### Earnings play

```
mcp__uw-pp__insights_earnings_play(days_until_earnings=25, min_iv_rank=40,
  top_n=25) → ADBE absent
```

ADBE (earnings 6/11, 23 cal days / ~16 trading days away, IV rank
89.6) **does not appear in the top-25** earnings-play list. The top-25
ranking is driven by combinations of days-to-earnings + IV rank +
oi_buildup + premium, and ADBE evidently misses on at least one
ranking component (likely the IV rank vs other names — the list is
sorted by IV rank descending starting from 100, and at 89.6 ADBE falls
below the cutoff with this many higher-IV-rank names earnings in the
window).

Names worth noting in the window that ADBE will trade alongside / vs:
- **PANW** (Cisco-Cybersecurity adjacent) 6/02, IV rank 93.9, bullish
  flow $64M vs bearish $35M — software-sector tone-setter.
- **ADI** 5/20 — semis benchmark.
- **WDAY** 5/21 — software peer.
- **ZS** 5/26 — software peer.
- **CRM** is not in this list (likely already reported or post-window).

**ADBE earnings will land 9 trading days AFTER PANW** — phase-9 may
want to use PANW's reaction as a setup-quality signal for ADBE.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__insights_deep_dive` | symbol=ADBE, date=2026-05-19 | Earnings 6/11, IV rank 89.6, impl move 3.24%; Yahoo 401 |
| `mcp__uw-pp__insights_signal_confluence` | direction=bullish, min_score=1, top_n=50, date=2026-05-19 | ADBE absent |
| `mcp__uw-pp__insights_signal_confluence` | direction=bearish, min_score=1, top_n=50, date=2026-05-19 | ADBE absent |
| `mcp__uw-pp__insights_conviction_matrix` | symbol=ADBE, date=2026-05-19 | **COVERED_CALL**, 13.45% confidence |
| `mcp__uw-pp__insights_price_vs_flow` | symbol=ADBE, lookback-days=30, date=2026-05-19 | **DIVERGENCE TRUE** (+6.55% / bearish flow) |
| `mcp__uw-pp__insights_analyst_vs_flow` | symbol=ADBE, date=2026-05-19 | Analyst block missing (yfinance failure) |
| `mcp__uw-pp__insights_institutional_accumulation` | symbol=ADBE, date=2026-05-19 | **ACCUMULATION** (buy/sell 1.60) |
| `mcp__uw-pp__insights_earnings_play` | days=25, min_iv_rank=40, top_n=25, date=2026-05-19 | ADBE absent from top-25 |

## Tool errors

- `insights_deep_dive` → `yahoo_fundamentals.error: "yahoo
  quoteSummary ADBE: HTTP 401"` — fundamentals not available.
- `insights_analyst_vs_flow` → no analyst section in payload (probably
  same yfinance failure surfaced as a missing field rather than an
  error key).

## Cross-check vs phases 1–5

| UW insight | Phase agreement? | Notes |
|------------|------------------|-------|
| `signal_confluence` (ADBE absent both lists) | Agrees with phase-5 (MIXED 30d flow), phase-1 (mixed tape) | Tension with phase-3 which read net OI as bullish-skewed |
| `conviction_matrix` (COVERED_CALL) | **Agrees with phase-3** (call writing at $265 + put writing at $260) + phase-2 (DP accumulation) | Resolves the apparent phase-1 vs phase-3 contradiction |
| `institutional_accumulation` (ACCUMULATION 1.60) | **Agrees with phase-2** | Identical numerical breakdown |
| `price_vs_flow` (DIVERGENCE) | Agrees with phase-1 "ASK-side puts > ASK-side calls" | Today's net flow bearish even as 30d trend up |
| `analyst_vs_flow` (no analyst data) | Phase-6 supplies qualitative "MIXED" via WebSearch | Treat as MIXED |
| `earnings_play` (ADBE absent) | Phase-6 confirms 6/11 earnings; phase-4 confirms IV kink | ADBE IS in window but ranks below top-25 by combined IV-rank metric |
| `deep_dive` snapshot | Mirrors phase-1 (premium magnitudes) + phase-3 (top OI changes) | Internal consistency confirmed |

## Verdict for downstream phases

- **UW composite bias:** **HEDGED LONG / COVERED-CALL OVERLAY** —
  institutions accumulating shares while writing OTM upside and
  buying partial put floors into the 6/11 earnings event. Net
  short-term directional bias = NEUTRAL-with-upside-cap; net medium-
  term bias = constructive (accumulation + buyback + AI catalyst).
- **Conviction:** **3.5/5** — high agreement across multiple composite
  classifiers (conviction matrix, institutional accumulation,
  price-vs-flow), but signal-confluence's absence in both directional
  top-50s caps the conviction; classifier confidence only 13.45%.
- **Phase-9 should treat this as the BASELINE.** Specifically:
  - Default trade structure should be a **defined-risk credit
    structure that monetizes IV rank 90** (e.g., put-credit spread
    below $245, call-credit spread above $270, iron condor between
    them, or short strangle structured as a Jade Lizard).
  - **Outright long calls / outright long puts are NOT supported**
    by the UW composite read.
  - **Earnings 2026-06-11 is the single dominant catalyst** —
    structure expiry around it (5/22, 5/29, 6/05 for pre-event vol
    sell; 6/18 for full event capture).
- **Open questions:**
  - Why is signal_confluence ADBE-absent? Worth a re-run with
    explicit ADBE filter or by inspecting score components — out of
    scope here.
  - Yahoo fundamentals 401 means no P/E, market-cap, or short-interest
    verification — phase-9 must note this gap.
  - Analyst consensus per UW unavailable; phase-9 must use phase-6's
    qualitative read.
