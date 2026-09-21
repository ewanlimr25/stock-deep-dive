# Phase 7 — UW Insights Confluence

**Ticker:** PATH
**As-of date:** 2026-05-18 (data: 2026-05-15)
**Generated:** 2026-05-18T01:40:00-04:00
**Upstream phases cited:** phase-0-intake.md → phase-6-macro.md

## Summary

UW's composite insight tools give a **MORE CAUTIOUS read than phases
1-5 individually suggested.** `insights_conviction_matrix` labels PATH
**MIXED** with only **8.55% confidence** because the dark-pool buy
ratio 0.586 is just below the strict 0.60 bull threshold
[INSIGHT:conviction_matrix]. `insights_institutional_accumulation`
also returns **NEUTRAL** despite a 1.41 buy/sell volume ratio
[INSIGHT:institutional_accumulation]. PATH does **NOT** appear in the
top-50 `insights_signal_confluence` bullish list (min-score=1) —
because PATH lacks the "low_iv_cheap_options" factor (IV is at the
100th percentile, the opposite of cheap) [INSIGHT:signal_confluence].
But `insights_price_vs_flow` confirms a **bullish divergence
(price -4.06% over 30d while net premium flow +$1.13M bullish)** — a
reversal-leading signal [INSIGHT:price_vs_flow]. The composite verdict
is **bullish but lower conviction than the individual phases suggest**,
and validates the macro-driven decision to size down. Notably,
**PATH's options-implied earnings move ≈ 19.8% on the 2026-05-29
expiry** [INSIGHT:deep_dive] — a huge premium vol bet that puts PATH
in the same earnings-week cohort as **SNOW, MRVL, OKTA, MDB, ADSK, S,
HPQ, AMBA — all software/tech names reporting 2026-05-27/28
with iv_rank 91-100** [INSIGHT:earnings_play].

## Key signals

- **Conviction matrix: MIXED, confidence 8.55%** — dark-pool buy ratio
  0.586 just below 0.60 bull threshold; tool reads "balanced"
  [INSIGHT:conviction_matrix].
- **Price vs flow DIVERGENCE detected**: price -4.06% / net flow
  +$1.13M bullish → **reversal-leading signal**
  [INSIGHT:price_vs_flow].
- **Institutional accumulation: NEUTRAL** (signal) despite buy/sell
  ratio 1.41 — tool threshold not met
  [INSIGHT:institutional_accumulation].
- **PATH absent from top-50 signal_confluence** because high IV blocks
  the "cheap options" factor [INSIGHT:signal_confluence].
- **Implied earnings move ≈ 19.8% on 2026-05-29 expiry** —
  ~$2.04 either-side from spot $10.30
  [INSIGHT:deep_dive].

## Detailed findings

### Deep dive snapshot

| Field | Value | Source |
|---|---|---|
| Spot | ~$10.30 | UW screener |
| IV30d | 95.7% | UW |
| IV rank | 85.4 | UW |
| **Implied move (option-derived)** | **19.78% (~$2.04)** | UW |
| Implied-move percentile | 1.9% (low — atypical for a 100% IV setup) | UW |
| PCR | 0.26 | UW |
| Total OI | 935,851 | UW |
| Next earnings | **2026-05-28** | UW (confirmed phase-6) |
| Today bullish prem | $2.91M | UW |
| Today bearish prem | $1.77M | UW |
| Net flow | **+$1.13M** | UW |
| **Yahoo fundamentals** | **ERROR: HTTP 401** | Yahoo |

**Yahoo error:** The `insights_deep_dive` tool's yfinance fundamentals
call returned HTTP 401 — PE/market-cap/short% not retrievable from this
tool. Phase 6's WebSearch covered the FQ4 fundamentals; phase-9 should
not block on this.

### Signal confluence (market-wide)

PATH does NOT appear in the top-50 bullish signal_confluence list at
min-score=1. The reason is **PATH's IV is at the 100th percentile** —
that disqualifies the `low_iv_cheap_options` factor, capping PATH's
max possible score in this tool at 5 (out of 6) and pushing it below
other names with cheap IV.

**Notable comparable signal_confluence-5 tickers in tech:**

| Ticker | IV rank | Net flow | Factors | Sector |
|---|---|---|---|---|
| **GTLB** | **100** | $495,320 | bullish_flow, low_pcr, vol_spike, dp_accum, oi_building | Tech (closest cohort to PATH) |
| **UMC** | 80.8 | **$7.34M** | bullish_flow, low_pcr, vol_spike, dp_accum, oi_building | Tech |
| **ENPH** | 85.0 | $5.55M | bullish_flow, low_pcr, vol_spike, dp_accum, oi_building | Tech (solar) |
| **OUST** | 68.2 | $983k | bullish_flow, low_pcr, vol_spike, dp_accum, oi_building | Tech (lidar) |
| **QRVO** | 27.1 | $1.17M | bullish_flow, low_pcr, vol_spike, dp_accum, low_iv | Tech (semis) |

**Read:** PATH would qualify on **bullish_flow + low_pcr + oi_building**
(3 factors confirmed). `dp_accumulation` and `volume_spike` are
borderline. PATH's effective confluence score is **3-5** depending on
threshold choices — high but lower than the headline of "5/5
sweep persistence" from phase 1 might suggest in isolation.

### Conviction matrix

| Field | Value |
|---|---|
| Scenario | **MIXED** |
| Confidence | **8.55%** (very low) |
| DP buy_ratio | 0.586 |
| Bull threshold | 0.60 |
| Bear threshold | 0.40 |
| Call ask vol | 37,126 |
| Call bid vol | 22,257 |
| Put ask vol | 9,208 |
| Put bid vol | 7,310 |
| Tool explanation | "Balanced dark pool activity — no clear bias." |

**Disagreement with phase 2:** Phase 2 read this same data as
"suggestive accumulation (3/5)". UW's tool requires buy_ratio ≥ 0.60
for a directional label; 0.586 misses by **1.4 percentage points** and
gets binned as MIXED. **Phase 10 must flag this disagreement.** The
honest read: dark-pool data is on the boundary between accumulation
and neutral. Phase 9 should not lean too hard on dark pool alone.

The options-flow micro is more decisive:
- **Calls: ask 37,126 vs bid 22,257 → ask-to-bid ratio 1.67** = bullish
- **Puts: ask 9,208 vs bid 7,310 → ask-to-bid ratio 1.26** = mild
  hedging (paying for puts > selling puts), but only ~25% the size
  of the call ask activity.

### Price vs flow

| Field | Value |
|---|---|
| Period | 30 days |
| Price start | $10.95 |
| Period high | $11.37 |
| Period low | $9.20 |
| Price end | $10.51 |
| Price change % | **-4.06%** |
| Bullish premium | $2.91M |
| Bearish premium | $1.77M |
| Net premium flow | **+$1.13M** |
| **Divergence** | **TRUE** |
| Signal | "DIVERGENCE: Price is down 4.1% but options flow is bullish" |

**Read:** This is the textbook bullish-flow / bearish-price divergence
that often leads a reversal. **Combined with phase 5's confirmation
that the 2026-05-13 $9.46 low coincided with the $9.40-$9.50
dark-pool accumulation shelf**, this is a high-quality reversal
signature — institutional buyers stepped in at the bottom, paid up
through the bounce, and are positioning for upside.

### Analyst vs flow

| Field | Value |
|---|---|
| Options flow | bullish (net +$1.13M, PCR 0.26) |
| Analyst data | **(missing — yfinance 401)** |

The tool returned no analyst consensus due to the same Yahoo 401.
**Phase 8 sub-agents should fill this gap by pulling consensus via
WebSearch** (e.g. analyst price target range, recent rating changes,
short interest if available).

### Institutional accumulation

| Field | Value |
|---|---|
| Signal | **NEUTRAL** — balanced dark pool activity |
| Buy-side volume | 1,333,700 sh |
| Sell-side volume | 944,127 sh |
| **Buy/sell ratio** | **1.41** |
| Avg trade price | $10.22 |
| VWAP | $10.23 |
| Total DP premium | $23.30M |
| Trades | 122 |
| 30d price change | -4.06% |

**Top price levels for today (≠ multi-day from phase 2):**

| Price | Premium | Shares | Trades |
|---|---|---|---|
| $10.35 | $1.83M | 176,923 | 7 |
| $10.34 | $1.56M | 150,564 | 6 |
| $10.36 | $1.48M | 143,294 | 7 |
| $10.46 | $1.46M | 140,000 | 4 |
| $10.44 | $1.25M | 120,202 | 8 |

The cluster of 5 prints in the **$10.34-$10.46 band (= $7.59M premium,
730k shares)** today shows institutional activity concentrated in a
narrow 1.1% range right around close, consistent with the buy-write
program inferred in phase 3.

**Disagreement:** Tool says NEUTRAL but buy/sell ratio 1.41 (= 58.6%
buy share) is a directional tilt. This is the same threshold issue as
the conviction matrix. **Same flag for phase 10.**

### Earnings play

PATH NOT in the top 30 of `insights_earnings_play` despite having
earnings on 2026-05-28 — because PATH's iv_rank 85.4 is below the
98+ cutoff for the top 30. **Tools default to ranking by IV rank,
which discounts a name that's *only* at the 85th percentile.**

But the **PATH earnings week cohort** is huge. Software names reporting
the same Wednesday/Thursday:

| Ticker | Date | IV rank | Bull vs Bear premium | Implied move | Read |
|---|---|---|---|---|---|
| **SNOW** | 2026-05-27 | 97.1 | $26.6M / $25.7M | 0.3% | Mega cap SaaS comparable |
| **MRVL** | 2026-05-27 | 93.0 | $49.3M / $45.7M | 0.5% | Semis — different sub-sector |
| **HPQ** | 2026-05-27 | 93.3 | $814k / $518k | 0.8% | Mixed |
| **ANF** | 2026-05-27 | 95.2 | $821k / $764k | 1.5% | Retail (not relevant) |
| **HEI** | 2026-05-27 | 99.4 | $1.93M / $47k | 0.6% | Industrial — bullish skew |
| **BBWI** | 2026-05-27 | 100 | $165k / $234k | 2.0% | Retail |
| **OKTA** | **2026-05-28** | **100** | $925k / $928k | 0.4% | **Direct SaaS comparable** |
| **MDB** | **2026-05-28** | **93.7** | $16.6M / $17.1M | 0.4% | **Database SaaS comparable** |
| **ADSK** | **2026-05-28** | **91.9** | $278k / $320k | 0.9% | **Design SaaS comparable** |
| **AMBA** | **2026-05-28** | **99.0** | $286k / $420k | 1.2% | Semi |
| **DLTR** | 2026-05-28 | 100 | $2.0M / $3.4M | 0.6% | Retail (not relevant) |
| **BBY** | 2026-05-28 | 100 | $377k / $467k | 0.7% | Retail |
| **S** | **2026-05-28** | **91.8** | $1.6M / $3.1M | **1.3%** | **AI security — bearish skew** |

**Read:** PATH reports into an **extremely crowded earnings night for
software/tech**. The most-similar comparables are OKTA, MDB, ADSK, S.
Three of them (MDB neutral, OKTA neutral, S bearish skew) show NO
bullish flow advantage going in. **This is a regime warning:
institutional positioning into SaaS earnings night 2026-05-28 is
NOT broadly bullish.**

PATH stands out with PCR 0.26 (much lower than OKTA's 0.30, MDB's
0.43, S's 0.03 actually similar) — **so PATH's bullish skew is real
but it's not a unanimous sector view.**

The **2026-05-27 SNOW print** will set the tone for software earnings;
if SNOW tanks on guidance, PATH's IV could pop further (vol bid into
the catalyst grows) and the bullish positioning could de-risk.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `insights_deep_dive` | `{symbol: PATH, date: 2026-05-15}` | IV rank 85.4, implied move 19.8%, earn 2026-05-28; Yahoo 401 |
| `insights_signal_confluence` | `{direction: bullish, min-score: 1, top-n: 50, date: 2026-05-15}` | PATH not in top-50 (no `low_iv` factor) |
| `insights_conviction_matrix` | `{symbol: PATH, date: 2026-05-15}` | **MIXED, confidence 8.55%** |
| `insights_price_vs_flow` | `{symbol: PATH, lookback-days: 30, date: 2026-05-15}` | **DIVERGENCE: -4.06% price, +$1.13M flow** |
| `insights_analyst_vs_flow` | `{symbol: PATH, date: 2026-05-15}` | Flow bullish; **analyst data missing (401)** |
| `insights_institutional_accumulation` | `{symbol: PATH, date: 2026-05-15}` | **NEUTRAL signal, buy/sell 1.41** |
| `insights_earnings_play` | `{days-until-earnings: 14, min-iv-rank: 40, top-n: 30, date: 2026-05-15}` | PATH not in top-30; SNOW/MRVL/OKTA/MDB/ADSK/S in PATH's earnings cohort |

## Tool errors

- `insights_deep_dive` → `yahoo quoteSummary PATH: HTTP 401` (yfinance
  endpoint authentication issue; PE/market-cap/short% not available
  through this tool). Workaround: phase 6 web search covered FY26
  results; phase 8 sub-agents should fill the rest.
- `insights_analyst_vs_flow` returned options flow only; no analyst
  consensus due to the same Yahoo 401.

## Cross-check vs phases 1–5

| UW insight | Phase alignment | Notes |
|---|---|---|
| `signal_confluence` (PATH missing from top-50) | **PARTIAL MISMATCH** with phase-1 "BULLISH 4/5" | UW dings PATH for high IV; phase 1 weighted vol-persistence and flow-magnitude higher than IV richness. **Resolution: both true, just different lenses.** |
| `conviction_matrix` = MIXED | **MISMATCH** with phase-2 "ACCUMULATION 3/5" | Strict 0.60 threshold misses 0.586. Phase-2 read with 0.55 threshold + top-25 tilt 0.74 was more bullish. **Resolution: phase 9 should respect the conservative UW read and treat dark pool as INCONCLUSIVE, not confirmed bullish.** |
| `institutional_accumulation` = NEUTRAL | **MISMATCH** with phase-2 | Same threshold issue. |
| `price_vs_flow` = DIVERGENCE bullish | **ALIGNS** with phase-1/2 (reversal-from-low signal) | High-quality confirmation |
| `analyst_vs_flow` | Data missing; phase 8 to fill | n/a |
| `earnings_play` cohort | **CONFIRMS phase-6** (binary catalyst 2026-05-28) and adds **PEER WATCH** (SNOW Tue, OKTA/MDB/ADSK/S Thu) | Valuable |

## Verdict for downstream phases

- **UW composite bias for PATH:** **MIXED-LEANING-BULLISH** — the
  microstructure tools (price_vs_flow, deep dive) are bullish, but the
  threshold-based composite tools (conviction_matrix, institutional_accumulation)
  flag MIXED/NEUTRAL because PATH's dark-pool buy ratio is on the
  cusp.
- **Conviction:** **3/5** — UW won't sign off on a full directional
  bull call; the data is genuinely mixed at the dark-pool level even
  if options flow is clean bullish. This is a **down-grade from phase
  1/3's 4/5 reads.**
- **Phase 9 should:**
  - Treat **MIXED + 8.55% confidence** as the gate. Combined with
    macro TRANSITIONAL regime, this **forces defined-risk only**.
  - Use the **DIVERGENCE bullish (price down, flow up)** as the
    primary directional signal — it's the cleanest UW-validated
    bullish read.
  - Plan around the **2026-05-28 earnings binary** with an exit decision
    BEFORE the SNOW print (2026-05-27 AMC) so peer-cohort surprise
    doesn't bleed into PATH's setup.
- **Open questions:**
  - **What is the consensus analyst price target for PATH?** Phase 8
    must pull via WebSearch (yfinance 401 blocked the UW tool).
  - **What is PATH's average historical post-earnings 1-day move?** If
    historical avg is < 16-18%, the 19.8% implied-move pricing is rich.
    Phase 8 should backfill from earnings history.
  - **How did the 2026-03-12 FQ4 print react over the next 5 sessions?**
    Stock went from ~$11 to $12.45 by 2026-03-18 (+13.6%) then to
    $9.46 over 8 weeks. So the prior earnings gave a 5-day +13.6% move
    that completely retraced. **PATH has a recent track record of
    earnings beats not lasting.**
