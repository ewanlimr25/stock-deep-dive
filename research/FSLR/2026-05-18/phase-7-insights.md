# Phase 7 — UW Insights Confluence

**Ticker:** FSLR
**As-of date:** 2026-05-18 (data anchor: 2026-05-15)
**Generated:** 2026-05-18T01:20:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-4-structure.md, phase-5-historical.md

## Summary

UW's composite tools return a deliberately **cautious MIXED read** on FSLR
that *aligns* with phases 1–5 rather than override them. The conviction
matrix tags **scenario = MIXED** with confidence only **1.66%**
(dark-pool buy ratio 0.483 sits between the 0.40 bear and 0.60 bull
thresholds; options flow has balanced call ask/bid but **put_ask_volume
4,025 vs put_bid_volume 1,752 = 2.3× — net put buying**). The
institutional accumulation signal is **NEUTRAL** ("balanced dark pool
activity"; buy_sell_ratio 0.94). The price-vs-flow divergence check is
**clean — no divergence**: spot +19.58% over 30d and flow direction
"bullish", consistent. Crucially, FSLR appears in **neither** the top-100
bullish nor top-100 bearish signal-confluence lists at min_score=1 — i.e.,
the screener-based factor stack does not light up in either direction for
this name today. Yahoo fundamentals failed with HTTP 401 (recorded as a
tool error). Next earnings is **2026-07-30** (~73 days out — outside the
30d window, so earnings_play deferred). Composite verdict: **MIXED with
bullish-aligned tape but no factor-stack confluence**, conviction 2.5/5.
This is a setup for **defined-risk structures around a binary catalyst**,
not a high-confluence directional thesis.

## Key signals

- **Conviction matrix scenario = MIXED, confidence 1.66%**; DP buy_ratio
  0.483 (between 0.40 bear and 0.60 bull thresholds); explanation:
  "Balanced dark pool activity — no clear bias." [INSIGHT:conviction_matrix]
- **FSLR absent from top-100 bullish signal_confluence list AND absent
  from top-100 bearish list at min_score=1** — no factor-stack signal in
  either direction; the factors (low_pcr, dp_accumulation, oi_building,
  low_iv_cheap_options, volume_spike, bullish_flow) **did not align** today
  [INSIGHT:signal_confluence].
- **Institutional accumulation signal: NEUTRAL** — buy_sell_ratio 0.94,
  signal text "balanced dark pool activity" [INSIGHT:institutional_accumulation].
- **Price vs flow: no divergence** — 30d spot +19.58% ($192.31 → $229.97,
  period high $240.84 / low $185.13), flow direction bullish, net flow
  +$648K, PCR 0.41 [INSIGHT:price_vs_flow].
- **Solar peer ENPH (Enphase) score 5 bullish confluence** (iv_rank 84.97,
  net_flow $5.5M); peer **SEDG score 4 bearish confluence** (iv_rank 87.3,
  net_flow −$833K). The solar sector is *bifurcated*, with FSLR sitting
  between the two — consistent with the binary tariff thesis from phase-6
  [INSIGHT:signal_confluence].
- **Next earnings date: 2026-07-30** — 73 days out; earnings_play tool
  skipped per skill rule [INSIGHT:deep_dive].

## Detailed findings

### Deep dive snapshot

| Field | Value |
|-------|-------|
| Symbol | FSLR |
| Dark pool avg price (today) | **$231.42** |
| Total DP premium | $71,228,946 (matches phase-2) |
| Total DP shares | 307,200 |
| DP trades | 383 |
| Bullish premium (screener) | $8,305,599 |
| Bearish premium (screener) | $7,657,600 |
| Call premium | $13,746,615 |
| Put premium | $3,258,593 |
| Call volume | 14,571 |
| Put volume | 5,957 |
| **PCR** | **0.41** (call-heavy) |
| Net flow | +$647,999 |
| IV30d | 52.81% |
| **IV rank** | **37.83** (mid-range) |
| Implied move | $1.61 (0.69%) |
| Volatility | 14.79 |
| Total OI | 574,424 |
| **Next earnings** | **2026-07-30** (out of 30d window) |

Top OI changes (insights view):

| Strike | Type | Expiry | DTE | OI Δ | Vol | Avg px |
|--------|------|--------|-----|------|-----|--------|
| 280 | Call | 2026-12-18 | 217 | +434 | 526 | $24.72 |
| 250 | Call | 2026-05-15 | 0 | +194 | 779 | $0.21 |
| 247.5 | Call | 2026-05-15 | 0 | +150 | 173 | $0.48 |
| 270 | Call | 2026-05-22 | 7 | +125 | 125 | $0.50 |
| 250 | Call | 2026-05-22 | 7 | +117 | 154 | $2.53 |

Notable new datapoint: a **Dec-2026 280C build (+434 OI, $24.72 avg
price, 526 vol)** — institutional positioning at the SAME $280 strike
but a near-term expiry, layered behind the phase-1 Mar-2027 280C
single-print. Two-tenor 280-strike call build is a meaningful tell that
$280 is the institutional **directional target**, not a one-off LEAP
flyer. Yahoo fundamentals path is broken (HTTP 401) so PE/short% are not
available; macro overlay (phase-6) covers the analyst consensus.

### Signal confluence (BULLISH direction, min_score=1, top-100)

**FSLR is NOT in the top-100 bullish confluence list.** That means:
- FSLR didn't earn ≥1 factor from {bullish_flow, low_pcr, volume_spike,
  dp_accumulation, oi_building, low_iv_cheap_options} that ranked it into
  the top 100 — OR it earned only the disqualifying combinations.
- Notable peers in the list:
  - **ENPH (Enphase Energy)** score **5**: bullish_flow + low_pcr +
    volume_spike + dp_accumulation + oi_building. iv_rank 84.97
    (elevated). Same sector — solar — but ENPH is positioned for upside
    while FSLR is positioned MIXED.

### Signal confluence (BEARISH direction, min_score=1, top-100)

**FSLR is NOT in the top-100 bearish confluence list either.**
- **SEDG (SolarEdge)** score **4** bearish: bearish_flow + volume_spike +
  oi_building_puts + high_iv_sell_premium. iv_rank 87.32. SEDG has been
  the **bearish-bookend solar peer** for some time.
- Heaviest market bearish concentrations are semiconductors: HPE (6),
  ADI (5), SMH (5), SOXL (4), SOXX (4) — directly explains the Tech
  sector −$151M flow in phase-6.

**Implication of FSLR's absence from both lists:** the screener factors
read FSLR as genuinely neutral *today*. This is consistent with all
upstream phases — phase 1 was mixed-bullish 3/5, phase 2 mixed-accum 3/5,
phase 3 inconclusive 2/5, phase 4 structurally bullish 4/5, phase 5
historically inconclusive 2.5/5. The composite simply confirms there is
no single-day factor stack confluence to trade on.

### Conviction matrix (scenario classifier)

| Field | Value |
|-------|-------|
| Scenario | **MIXED** |
| Confidence | **1.66%** |
| DP buy ratio | **0.483** (between bear 0.40 and bull 0.60) |
| DP buy volume | 148,488 |
| DP sell volume | 158,712 |
| Call ask volume | 6,676 |
| Call bid volume | 6,777 |
| Put ask volume | **4,025** |
| Put bid volume | **1,752** |
| Explanation | "Balanced dark pool activity — no clear bias." |

Key cross-read: **call ask ≈ call bid (balanced)** but **put ask is 2.3×
put bid → net put buying is real**. Aligns with phase-1's put hedge
layer interpretation.

### Price vs flow (divergence detector)

| Field | Value |
|-------|-------|
| Period | 30 days |
| Price start (~2026-04-15) | $192.31 |
| Price end (2026-05-15) | $229.97 |
| Period high | $240.84 |
| Period low | $185.13 |
| **Price change %** | **+19.58%** |
| Flow direction | bullish |
| Bullish premium (period) | $8,305,599 |
| Bearish premium (period) | $7,657,600 |
| Net premium flow | +$647,999 |
| IV rank | 37.83 |
| **Divergence** | **false** |
| Signal | "Price and flow are aligned" |

This is the cleanest single-line vindication of the upstream phases:
**price has moved with the flow, not against it**. No reversal trigger.

### Analyst vs flow

The tool's `analyst_recommendations` field is **absent from this run**
(only `options_flow` returned). Likely cause: Yahoo Finance auth failure
seen in `insights_deep_dive` (HTTP 401) blocks yfinance recommendations.
Macro phase covered the manual web-research analyst consensus
(30 Buy / 5 Hold / 1 Sell, median PT $277).

### Institutional accumulation

| Field | Value |
|-------|-------|
| **Signal** | **NEUTRAL — balanced dark pool activity** |
| Buy_sell_ratio | **0.94** |
| Buy_side_volume | 148,488 |
| Sell_side_volume | 158,712 |
| Total DP premium | $71,228,946 |
| Total DP volume | 307,200 |
| VWAP | $231.87 |
| 30d price change | +19.58% |

Top price levels (today only):

| Level | Premium | Shares | Trades |
|-------|---------|--------|--------|
| 231.03 | $2.69M | 11,655 | 1 (the seller block) |
| 235.87 | $2.05M | 8,704 | 2 (buyer above ask) |
| 236.55 | $1.80M | 7,600 | 1 |
| 232.01 | $1.44M | 6,220 | 2 |
| 236.96 | $1.42M | 5,990 | 1 |

Same data as phase-2 — composite tool reads it more cautiously
(NEUTRAL) than phase-2 (mild accumulation) because the buy_sell_ratio is
below 1.0 in absolute terms. This is **a real disagreement with phase-2**:
the composite tool is treating "above-1.0 ratio = accumulation"; phase-2
applied additional context (the 11,655-share sell was a single block
distortion; the 0.535 large-tier buy ratio was the underlying signal).
**Phase-9 should weight phase-2's nuance OVER the composite's binary
classification** because the composite collapses tier-level information.

### Earnings play (out-of-window — skipped)

Per skill rule: only run `insights_earnings_play` if earnings within 30
days. FSLR Q2 reports **2026-07-30 (~73 days out)**, so deferred. This
becomes relevant for a phase-9 trade with horizon ≥ 60 days.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__insights_deep_dive` | `{symbol: FSLR, date: 2026-05-15}` | DP $71M, IV30 52.8%, IV rank 37.8, next earnings 2026-07-30 |
| `mcp__uw-pp__insights_signal_confluence` | `{direction: bullish, min-score: 1, top-n: 100, date: 2026-05-15}` | FSLR absent from top 100; ENPH score 5 |
| `mcp__uw-pp__insights_signal_confluence` | `{direction: bearish, min-score: 1, top-n: 100, date: 2026-05-15}` | FSLR absent from top 100; SEDG score 4 |
| `mcp__uw-pp__insights_conviction_matrix` | `{symbol: FSLR, date: 2026-05-15}` | MIXED, confidence 1.66%, DP ratio 0.483 |
| `mcp__uw-pp__insights_price_vs_flow` | `{symbol: FSLR, lookback-days: 30, date: 2026-05-15}` | No divergence; aligned bullish; +19.58% price |
| `mcp__uw-pp__insights_analyst_vs_flow` | `{symbol: FSLR, date: 2026-05-15}` | Only flow side returned (yfinance auth issue) |
| `mcp__uw-pp__insights_institutional_accumulation` | `{symbol: FSLR, date: 2026-05-15}` | NEUTRAL; buy_sell_ratio 0.94; VWAP $231.87 |
| `mcp__uw-pp__insights_earnings_play` | NOT CALLED — earnings 73d out | — |

## Tool errors

- `mcp__uw-pp__insights_deep_dive` `yahoo_fundamentals` field returned
  `{"error": "yahoo quoteSummary FSLR: HTTP 401"}` — Yahoo Finance auth
  rejected the request. Mitigation: phase-6 macro web-searched analyst
  consensus and Q1 earnings results manually; no downstream impact.
- `mcp__uw-pp__insights_analyst_vs_flow` did not return an
  `analyst_recommendations` block (same upstream cause). Mitigation: same
  as above.

## Cross-check vs phases 1–5

| UW insight | Phase | Agreement? | Notes |
|------------|-------|------------|-------|
| `signal_confluence` absence | phase 1 (mixed-bullish 3/5) | **AGREE** — confluence math says no factor stack, phase 1 said "mixed" |
| `signal_confluence` absence | phase 4 (bullish structure 4/5) | **PARTIAL DISAGREE** — phase 4 is the strongest bull read; confluence tool doesn't weight dealer-structure inputs |
| `conviction_matrix` MIXED | phase 1 | AGREE |
| `conviction_matrix` MIXED | phase 2 (mild accum 3/5) | PARTIAL — phase 2 was more positive on tier-level data |
| `conviction_matrix` MIXED | phase 4 | DISAGREE — phase 4 was bullish on dealer structure; conviction matrix uses only DP and screener flow |
| `institutional_accumulation` NEUTRAL | phase 2 | PARTIAL — phase 2 explained the 11,655-sh distortion; composite is binary |
| `price_vs_flow` no divergence | phase 5 (17 bull / 9 bear days, +19% trend) | **AGREE** |
| `price_vs_flow` no divergence | phase 1 | AGREE |

**Net cross-check:** the composite tools UNDER-WEIGHT phase-4's dealer
structure signals and phase-6's binary catalyst overlay (Section 232).
This is by design — the composites read screener / DP / OI surface
data, not GEX/DEX/macro context. **Phase-9 should anchor on phase-4
structure + phase-6 catalyst, and treat phase-7's "MIXED" as the
*single-day surface read* it really is.**

## Verdict for downstream phases

- **UW composite bias:** **MIXED** with bullish-aligned tape direction;
  no factor-stack confluence.
- **Conviction:** **2.5/5.** Cannot be higher because the composite tools
  did not light up; cannot be lower because price-vs-flow is aligned and
  the put-hedge layer is a known phase-1 datapoint that the composite is
  correctly reflecting.
- **Phase-9 baseline treatment:** Phase-9 should treat phase-7 as the
  *surface-level reality check* — confirmation that no broad-confluence
  trade is on. The directional edge in this deep dive comes from
  **phase-4 (dealer structure) + phase-6 (Section 232 binary catalyst)**,
  which the composite tools do not measure. Defined-risk structures
  through the catalyst window are the indicated playbook.
- **Open questions for downstream phases:**
  - Phase-8 sub-agents should be asked to RECONCILE the MIXED composite
    read with the LONG-GAMMA structural read — is the trade idea
    direction-neutral premium-selling, or directional defined-risk?
  - Where does the next-OI-snapshot Mar-2027 280C +480 contracts and
    Dec-2026 280C +434 already-built two-strike build fit into the
    composite read? Likely it lifts FSLR onto the bullish board *tomorrow*.
  - Is the put hedge layer (visible in phase-1, partial in phase-7) a
    SIZE-CAP signal for the trade structure? (→ phase-9 sizing rubric)
