# Phase 7 — UW Insights Confluence

**Ticker:** KWEB
**As-of date:** 2026-05-19
**Generated:** 2026-05-20T00:00:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-4-structure.md, phase-5-historical.md, phase-6-macro.md

## Summary

UW's composite tools confirm phases 1–6 with a single-word verdict:
**MIXED**. `insights_conviction_matrix` classifies KWEB as **MIXED at
8.28% confidence**, DP buy_ratio 0.417 (inside the 0.4–0.6 indecision
band) and options flow call_ask 24,148 vs **call_bid 77,729 (ratio
0.31 — bid-side dominant in calls, consistent with overwriting)**
[INSIGHT:conviction_matrix]. `insights_institutional_accumulation`
labels KWEB **NEUTRAL** with buy/sell ratio 0.72 and a single-day price
cluster at $28.31–28.32 [INSIGHT:institutional_accumulation]. KWEB is
**ABSENT from BOTH the bullish AND bearish `signal_confluence` top 50
even at min_score=1** [INSIGHT:signal_confluence] — meaning UW's
factor-count framework finds no directional confluence stack on KWEB
itself today. However, two **important cousin signals** are present:
- **YINN (3× China-bull ETF) scores 5 BULLISH factors** (bullish_flow,
  low_pcr, dp_accumulation, oi_building, low_iv_cheap_options) — a
  same-theme directional vote *for* China longs
  [INSIGHT:signal_confluence_bullish].
- **FUTU (score 5) and TIGR (score 5)**, both Chinese broker proxies,
  score BEARISH (high_pcr, oi_building_puts, high_iv_sell_premium)
  [INSIGHT:signal_confluence_bearish] — same-theme directional vote
  *against* China-internet finance specifically.

Price-vs-flow shows **NO divergence** (flow bearish, price down 2.82%
over 30d — aligned, not reversal-setup-ready)
[INSIGHT:price_vs_flow]. Analyst rating data unavailable (KWEB is an
ETF) [INSIGHT:analyst_vs_flow]. Deep-dive Yahoo fundamentals errored
HTTP 401 (also ETF-related, no fundamentals)
[INSIGHT:deep_dive].

## Key signals

- **Conviction scenario MIXED at 8.28% confidence**
  [INSIGHT:conviction_matrix] — UW's lowest-confidence verdict; nothing
  has clear edge.
- **Call ask/bid 24,148 / 77,729 (ratio 0.31)**
  [INSIGHT:conviction_matrix] — institutional **call OVERWRITING / long
  call liquidation** at scale; corroborates phase-1 bid-side call
  sweeps and phase-3 OI signature.
- **YINN scores 5 bullish factors** [INSIGHT:signal_confluence_bullish]
  — the directional China bet IS in the chain, just not in KWEB.
- **FUTU + TIGR score 5 bearish factors each**
  [INSIGHT:signal_confluence_bearish] — bearish theme is concentrated
  in China-broker / financial intermediary names, not in KWEB itself.
- **KWEB price-vs-flow ALIGNED (not divergent)**
  [INSIGHT:price_vs_flow] — no mean-reversion setup is signaled. The
  flow / price agreement removes one of the cleaner contrarian
  triggers from the table.

## Detailed findings

### Deep-dive snapshot [INSIGHT:deep_dive]

| Field | Value |
|-------|-------|
| Yahoo fundamentals | **HTTP 401** (ETF — none available) |
| UW dark pool total premium | $100,677,163 |
| UW dark pool total shares | 3,555,473 |
| UW dark pool avg price | $28.306 |
| UW dark pool trade count | 348 |
| Bullish premium | $3,538,314 |
| Bearish premium | $3,763,875 |
| Net flow | -$225,561 |
| Call premium | $7,592,679 |
| Put premium | $3,240,674 |
| Call volume | 143,389 |
| Put volume | 22,933 |
| PCR | **0.16** |
| IV30d | 30.24% |
| IV rank | 45.31 |
| Implied move | 0.5718 ($) / **2.02%** |
| Next earnings date | null (ETF) |
| Total OI | 3,864,160 |

Top OI changes block matches phase 3 exactly (28P May 29 +11,461;
30.5C May 29 +7,449; 15P Jan'27 +6,929; 29.5C May 29 +6,008; 29C Jun
+2,925).

### Signal confluence — bullish [INSIGHT:signal_confluence_bullish]

- KWEB is **NOT** in the bullish top 50 (min_score=1). 50 names listed
  with score ≥5 ahead of KWEB.
- **Notable China-thematic appearance: YINN (3× China-bull, score 5)**.
  Factors: `bullish_flow`, `low_pcr`, `dp_accumulation`, `oi_building`,
  `low_iv_cheap_options`. Net flow +$113K, IV rank 26.3, PCR 0.39.
  YINN scoring bullish is meaningful — it's the *most-leveraged China-
  long expression*, and if speculators were positioning for the tariff
  truce upside, this is exactly the vehicle they'd choose.

### Signal confluence — bearish [INSIGHT:signal_confluence_bearish]

- KWEB is **NOT** in the bearish top 50 either.
- **Two China-broker peers score 5 BEARISH:**
  - **FUTU (Futu Holdings)** — high_pcr 4.18, IV rank 91.0, net flow
    +$5.33M (note: positive but classified bearish on factor stack),
    volume ratio 3.17. Factors: high_pcr, volume_spike, dp_distribution,
    oi_building_puts, high_iv_sell_premium.
  - **TIGR (Tiger Brokers)** — high_pcr 26.15, IV rank 86.7, net flow
    -$350K. Factors: bearish_flow, high_pcr, volume_spike,
    oi_building_puts, high_iv_sell_premium.
- **PKX (POSCO, Korea steel — China demand exposure)** scores 4
  bearish at IV rank 78.5.

The cross-asset read: brokerage / finance / industrial-supply-chain
proxies skew bearish, while leveraged China-equity speculation
vehicles (YINN) skew bullish. KWEB itself sits in the middle —
explaining why the composite refuses to crown a side.

### Conviction matrix [INSIGHT:conviction_matrix]

| Field | Value |
|-------|-------|
| Scenario | **MIXED** |
| Confidence | **8.28%** |
| Explanation | "Balanced dark pool activity — no clear bias." |
| DP buy_ratio | 0.417 |
| DP buy_volume | 1,483,342 |
| DP sell_volume | 2,072,131 |
| Call ask volume | 24,148 |
| Call bid volume | **77,729** |
| Put ask volume | 8,446 |
| Put bid volume | 9,652 |
| Bull threshold | 0.6 |
| Bear threshold | 0.4 |

**The call ask/bid 24K vs 78K (ratio 0.31)** is the most informative
single number in this matrix: institutional desks are selling 3.2× as
many calls on the bid as they're buying on the ask. This is a **clean
call-overwriting / call-liquidation signature** — consistent with the
phase-1 bid-side sweeps in Jul 30C / Aug 35C / Sep 35C and the phase-3
OI signature in 29.5C / 30C / 32C / 35C / 50C bid-heavy openings.

Puts are *much* more balanced (8.4K ask vs 9.7K bid, ratio 0.87) — no
panic put buying. Confirms phase-3's read that the bearish tape is
overwhelmingly **call selling**, not put buying.

### Price vs flow [INSIGHT:price_vs_flow]

| Field | Value |
|-------|-------|
| Divergence | **false** |
| Divergence signal | "Price and flow are aligned" |
| Flow direction | bearish |
| Bullish premium | $3,538,314 |
| Bearish premium | $3,763,875 |
| Net premium flow | -$225,561 |
| Period (30d) high | $30.74 |
| Period (30d) low | $27.92 |
| Price start | $29.10 |
| Price end | $28.28 |
| 30d change | **-2.82%** |
| IV rank | 45.31 |
| PCR | 0.16 |

Price and flow are pointing the same direction — no reversal
configuration. The 30d range was tight (-7.8% peak-to-trough); the
+5% pop on 2026-05-13 followed by the 5-day fade fully fits inside
the broader 30d sideways range.

### Analyst vs flow [INSIGHT:analyst_vs_flow]

ETF — analyst recommendation data not available. Returned options-
flow block only:
- Flow sentiment: bearish
- Net flow: -$225,561
- Bullish premium: $3,538,314
- Bearish premium: $3,763,875
- PCR: 0.16

### Institutional accumulation [INSIGHT:institutional_accumulation]

| Field | Value |
|-------|-------|
| Signal | **NEUTRAL — balanced dark pool activity** |
| Avg trade price | $28.31 |
| VWAP | $28.32 |
| Buy/sell ratio | 0.72 (1.48M buy / 2.07M sell volume) |
| 30d price change | -2.82% |
| Total DP premium | $100,677,163 |
| Total DP volume | 3,555,473 |

Top intraday price-level clusters today:

| Price | Premium | Shares | Trades |
|-------|---------|--------|--------|
| $28.31 | $15,719,043 | 555,247 | 8 |
| $28.32 | $14,067,512 | 496,736 | 12 |
| $28.25 | $6,769,297 | 239,618 | 39 |
| $28.24 | $5,675,419 | 200,984 | 25 |
| $28.26 | $5,306,503 | 187,779 | 39 |

The single $15.7M premium at $28.31 (8 trades, avg ~70K shares each)
includes the large block prints from phase 2. The institutional
accumulation tool's NEUTRAL label disagrees with phase 2's
**Distribution at mega tier** read — UW's blended buy/sell ratio
(0.72) hides the tier-stratified asymmetry (mega 0.000 buy / large
0.536 buy). Phase 10 should flag this as a "composite-lost-the-
signal" caveat.

### Earnings play [INSIGHT:earnings_play]

Skipped — KWEB is an ETF; no earnings. Phase 6 calendar contains the
relevant binary catalysts (May 22 expiry, June FOMC, June 18 OPEX).

## Tool calls (audit trail)

| Tool | Args | Result |
|------|------|--------|
| `insights_deep_dive` | `{symbol: KWEB, date: 2026-05-19}` | Yahoo 401, UW data populated |
| `insights_signal_confluence` | `{direction: bullish, min-score: 1, top-n: 50, date: 2026-05-19}` | 50 names; KWEB absent; YINN at 5 |
| `insights_signal_confluence` | `{direction: bearish, min-score: 1, top-n: 50, date: 2026-05-19}` | 50 names; KWEB absent; FUTU/TIGR at 5 |
| `insights_conviction_matrix` | `{symbol: KWEB, date: 2026-05-19}` | MIXED, conf 8.28%, DP buy_ratio 0.417 |
| `insights_price_vs_flow` | `{symbol: KWEB, lookback-days: 30, date: 2026-05-19}` | divergence false, flow/price aligned |
| `insights_analyst_vs_flow` | `{symbol: KWEB, date: 2026-05-19}` | flow only (ETF) |
| `insights_institutional_accumulation` | `{symbol: KWEB, date: 2026-05-19}` | NEUTRAL, buy/sell 0.72 |

## Tool errors

- `insights_deep_dive` returned `yahoo quoteSummary KWEB: HTTP 401` —
  fundamentals not available because KWEB is an ETF (no quarterly
  reports, no PE). Non-blocking.

## Cross-check vs phases 1–6

| UW insight | Phase agreement? | Notes |
|------------|------------------|-------|
| `conviction_matrix` MIXED | **Agrees with phase 1 (mixed-leaning bearish), phase 3 (range), phase 5 (VRP edge muted)** | UW's MIXED is the same verdict reached upstream. |
| `conviction_matrix` call ask/bid 0.31 | **Strongly agrees with phase 1 (bid-side call sweeps) and phase 3 (call overwriting at 29.5/30/35)** | Cross-validates the call-overwriting thesis. |
| `institutional_accumulation` NEUTRAL | **Partially disagrees with phase 2 (mega-tier distribution)** | UW blends tiers; phase 2's stratified read (mega 0.000 buy) is hidden. Phase 10: flag composite loss-of-signal. |
| `price_vs_flow` no divergence | **Agrees with phase 5 (5-day fade after May 13 high)** | Price and flow rolling over together; no mean-reversion trigger. |
| `signal_confluence` KWEB absent | **Agrees with all phases** — nothing scored ≥3 for KWEB | Confluence framework finds no stack; consistent with our MIXED narrative. |
| `signal_confluence` YINN bullish | **NEW datapoint not derivable from phases 1-5** | Cross-asset bullish-China speculation is present in the chain via YINN. Phase 8 / 9 should reference this. |
| `signal_confluence` FUTU/TIGR bearish | **NEW datapoint, partially aligned with phase 1 5-day persistence** | Bearish China-finance peers strengthen the bearish lean, but specifically on intermediary names rather than constituent equities. |
| `deep_dive` implied move 2.02% | **Cross-references phase 4** — 30d IV 30% implies ~$0.57 daily move = aligns with the $28-29 corridor expectation from phase 4's $29 GEX wall and $28 short-gamma pocket | Useful sanity-check on phase 9 stop / target levels. |

## Verdict for downstream phases

- **UW composite bias:** **MIXED** at low confidence (8.28%). No
  directional verdict from UW alone.
- **Conviction:** 2 / 5. The composite tools are silent on direction.
  Higher-conviction reads have to come from the phase-1/2/3/4/6
  details that the composite blends away.
- **Phase 9 should treat MIXED as the BASELINE** and override ONLY on
  the following specific contrary evidence already documented:
  1. **Phase-2 mega-tier DP buy_ratio 0.000** (Distribution at scale)
     — the composite buried this. Bear conviction should carry it.
  2. **Phase-3 28P sold-to-open at $665K premium / OI +11,461 (5.4×)**
     — institutional floor defense at $28. Bull conviction at the $28
     entry should carry it.
  3. **Phase-6 2026-05-20 US-China tariff truce extension news** —
     post-close catalyst not yet in any UW dataset. Tactical bias
     +1 day.
  4. **Phase-4 May 22 IV at 52.6% / Phase-5 VRP -3.92% / 30 DTE skew
     COMPLACENT** — vol-rich front-week, vol-cheap mid-curve, calls
     richer than puts. Structural vol setup is asymmetric in favor of
     buying mid-DTE puts (cheap) and/or selling May 22 vol.
  5. **YINN scored 5 bullish** while KWEB scored absent — if a
     directional China-long is taken, the leveraged speculation is
     happening *next door*. Either treat as confirmation of the
     China-long thesis or treat as overcrowded-trade contrarian
     signal — phase 8 PM voice should weigh.
- **Open questions:**
  - Why does the composite `institutional_accumulation` say NEUTRAL
    when stratified phase 2 says mega-tier DISTRIBUTION? Composite
    tool blends across tiers and loses the asymmetry. Phase 10 must
    quote this as a *known divergence* in the audit.
  - The KWEB conviction matrix shows call ask/bid 0.31 — extreme call
    overwriting — yet the institutional_accumulation buy/sell ratio
    is 0.72 (close to even). If desks are selling calls heavily
    (bearish for stock pressure) but the DP isn't flooded with stock
    sells, where is the call premium coming from? Most likely
    **covered-call overlay programs by long-stock holders** — i.e.
    the call overwriting is *bullish-supportive structure*, not
    bearish-directional. This re-frames the entire 5-day sweep
    persistence flag.
