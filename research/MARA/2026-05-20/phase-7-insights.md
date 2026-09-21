# Phase 7 — UW Insights Confluence

**Ticker:** MARA
**As-of date:** 2026-05-19
**Generated:** 2026-05-20T01:20:00-04:00
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-4-structure.md, phase-5-historical.md, phase-6-macro.md

## Summary

UW composite verdict on MARA is **MIXED with confidence 0.13** (very
low). MARA does **NOT appear** in either the top-100 bullish or top-100
bearish `signal_confluence` lists at min_score=1 — the standardized
factor template lights up zero factors for MARA today, because each
individual factor (PCR, IV rank, dp ratio, net flow magnitude) sits
just below its cutoff. Conviction Matrix returns `MIXED`,
Institutional Accumulation returns `NEUTRAL`, Price-vs-Flow says **no
divergence** (price +33% over 30d with bullish flow direction — aligned
trend, not a reversal candidate). The deep-dive snapshot confirms next
earnings is **2026-08-04** (well outside 30-day window) — no earnings
play to construct. **The single biggest UW composite finding:** all five
insight tools converge on the same answer as phases 1-5 — **MARA is in
a balanced, range-bound consolidation with no edge in either direction**.
This is not a "no setup" answer; it is an active vote for **non-directional
spread structures over directional bets**.

## Key signals

- Conviction Matrix: **MIXED**, confidence **0.13** (very low edge in
  either direction) [INSIGHT:conviction_matrix]
- Institutional Accumulation: **NEUTRAL** — buy/sell ratio **0.99**,
  dark-pool VWAP $12.09 [INSIGHT:institutional_accumulation]
- Price vs Flow: **NO DIVERGENCE** — 30-day price +33.35%, flow bullish,
  aligned (no reversal signal) [INSIGHT:price_vs_flow]
- Signal confluence: **MARA absent from top-100 bullish AND bearish**
  lists at min_score=1 → standardized confluence factors are all just
  below threshold; the strength of MARA's setup is in *sub-categorical*
  features (sweep persistence, gamma walls, OI buildup) that the
  confluence template doesn't score [INSIGHT:signal_confluence]
- Deep-dive: total OI **1.80M contracts**, IV30 84.2%, IV rank 35.9,
  next earnings **2026-08-04** (no in-window earnings play)
  [INSIGHT:deep_dive]
- Top dark-pool price levels (single-day, 5/19): $12.40 ($3.7M), $12.10
  ($3.55M), **$11.75 ($3.1M / 265K shares / 6 trades)** —
  confirms phase-2 dip-buy at $11.75
  [INSIGHT:institutional_accumulation]
- Yahoo fundamentals: **errored (HTTP 401)** — no Yahoo-sourced P/E, market
  cap, or analyst data available for this run [INSIGHT:deep_dive]

## Detailed findings

### Deep-dive snapshot

| Field | Value | Source |
|-------|-------|--------|
| Total dark pool premium | $53,712,734 | UW dark pool |
| Dark pool VWAP | $12.11 | UW |
| Dark pool trade count | 274 | UW |
| Total open interest | 1,804,691 contracts | UW screener |
| Call premium today | $3,796,678 | UW |
| Put premium today | $1,771,651 | UW |
| Net flow today | +$320K | UW |
| Volume (calls/puts) | 61,241 / 36,171 | UW |
| Put/call ratio | 0.59 | UW |
| IV30d | 84.19% | UW |
| IV rank | **35.9** | UW |
| Implied move (next earnings) | $0.744 / **5.98%** | UW |
| Next earnings date | **2026-08-04** | UW screener |
| Volatility (yfinance) | 96.9% | yfinance |
| Yahoo fundamentals | **error HTTP 401** | yfinance |

Top OI changes recap (already covered in phase 3, but UW deep-dive
confirms): 12.5C 5/22 (+3,920), 10P 1/27 LEAP (+2,780), 12.5C 5/29
(+2,430), 13C 5/29 (+2,305), 12P 5/22 (+2,207).

### Signal confluence

| Direction | MARA in top-100? | Score | Factors |
|-----------|------------------|-------|---------|
| Bullish (min_score=1) | **NO** | 0 (below threshold) | none of: bullish_flow, low_pcr, volume_spike, dp_accumulation, oi_building, low_iv_cheap_options |
| Bearish (min_score=1) | **NO** | 0 (below threshold) | none of: bearish_flow, high_pcr, volume_spike, dp_distribution, oi_building_puts, high_iv_sell_premium |

**Why this matters:** The confluence factor template counts standardized
buckets. MARA is below cutoff on each: PCR 0.59 (not "low_pcr" at <0.4,
not "high_pcr" at >1.5), IV rank 35.9 (not "low_iv_cheap_options" at
<30, not "high_iv_sell_premium" at >70), dp_ratio 0.499 (neither
accumulation nor distribution), net flow $320K (small for a stock of
this OI). **The features that DID light up in phases 1-4 are not in the
confluence template** (sweep persistence, single-strike gamma wall,
OI structure, vanna sign). So the absence here is not contradictory;
it's a template-coverage limitation.

**For sector context, peers WITH high confluence scores today:**
- WULF (Financial Services / crypto-miner): score **5** bullish factors
  (bullish_flow, low_pcr, dp_accumulation, oi_building, low_iv) — same
  peer that appeared in phase-1 hot_chains as the largest miner-sector
  bullish flow.
- CIFR (Financial Services / crypto-miner): score **5** bullish
- HIVE (Financial Services / crypto-miner): score **5** bullish (PCR
  0.37, net flow +$528K)
- CORZ (Technology): score **4** bullish (net flow +$1.9M)
- **CLSK (Technology / crypto-miner): score 4 bullish (net flow +$1.48M)**

→ **Crypto miner peers WULF, CIFR, HIVE, CORZ, CLSK all score 4-5
bullish confluence today, but MARA does not.** This is a meaningful
*relative* signal: the sector cohort is showing standardized bullish
features (low PCR, ask-side flow, dp accumulation, OI building) but
MARA does not. MARA is the *laggard* in the miner cohort today.

**Counterpoint:** MARA had the heaviest pre-earnings buildup of any
miner (phase 5: +1.72M OI over 28 days) and now sits in post-earnings
digestion while peers haven't reported yet. The cohort divergence may
reflect MARA *trailing* the rally because it already ran (+67% from
3/27 low) and then disappointed on Q1.

### Conviction matrix

```
Scenario: MIXED
Confidence: 0.13
Dark pool buy_ratio: 0.499
Options:
  call_ask_volume: 25,825
  call_bid_volume: 28,859
  put_ask_volume: 12,258
  put_bid_volume: 19,824
Thresholds: bull≥0.6, bear≤0.4
```

**Reading:** dp ratio 0.499 is centered. The options sub-breakdown is
slightly bearish on calls (28,859 bid vs 25,825 ask = 53% bid-side =
mild call writing — confirms phase 3's $13 wall write) and modestly
bullish on puts (19,824 bid vs 12,258 ask = 62% bid-side = put
writing — confirms phase 3's $10/11/12 put writing). Combined: **collared
long-stock structure with no fresh directional initiation**.

### Institutional accumulation

```
Signal: NEUTRAL — balanced dark pool activity
Buy-side volume: 2,215,117 shares
Sell-side volume: 2,227,017 shares
Buy/sell ratio: 0.99
Total dark-pool trades: 274
Total dark-pool premium: $53,712,734
VWAP: $12.09
30-day price change: +33.3%
```

**Top single-day price clusters (5/19):**

| Price | Premium | Shares | Trades |
|-------|---------|--------|--------|
| $12.40 | $3,729,791 | 300,790 | 11 |
| $12.10 | $3,551,991 | 293,552 | 4 |
| **$11.75** | **$3,118,450** | **265,400** | **6** |
| $12.33 | $2,203,097 | 178,681 | 11 |
| $11.82 | $1,766,740 | 149,475 | 7 |

→ The $11.75 cluster (265K shares / 6 trades) is the same buy block
identified in phase 2's largest-print analysis. The $12.40 cluster
(300K shares / 11 trades) and $12.10 (293K / 4 trades) confirm
balanced two-way action. **VWAP $12.09 is below today's $12.30-$12.44
close** — institutions transacted *below* the closing print, which is
mildly bullish (institutions paid up into the close).

### Price vs flow

```
Divergence: false
Divergence signal: "Price and flow are aligned"
Period: 30d
Price start: $9.67
Price end: $12.90
Price change: +33.35%
Period high/low: $13.80 / $9.18
Flow direction: bullish
Net premium flow: +$320K
IV rank: 35.9
PCR: 0.59
```

**Reading:** the 30-day rally aligned with bullish flow — no reversal
divergence. Note the period high $13.80 is slightly above phase-2's
$13.20-$13.29 dark-pool cluster, confirming intraday spikes above the
institutional-distribution band. The current $12.30-$12.44 close is
*below* both metrics.

### Analyst vs flow

Tool returned options-flow side only:
- flow_sentiment: **bullish**
- net_flow: +$320K
- PCR: 0.59

**Analyst consensus side did not return** (yfinance 401 error in
deep_dive likely cascading). No Wall Street analyst data for this run.
Treat as inconclusive on the agreement axis. **Open question:** the
phase-3 LEAP put buying ($662K of Jan-27 10P bid) is consistent with
institutions hedging a *consensus-bullish* analyst rating. If consensus
is bullish, then the put-buying is protection on a long thesis; if
consensus is bearish, the put-buying is fresh-shorts. Phase 8 sub-agents
should attempt to pull current analyst consensus via WebSearch.

### Earnings play

**Skipped** — next earnings is **2026-08-04**, well outside the 14-day
default. Confirmed by `insights_deep_dive.next_earnings_date`. No
earnings-vol setup applies; MARA Q1 earnings (5/11) already digested
per phase-6.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__insights_deep_dive` | `{symbol: MARA, date: 2026-05-19}` | OI 1.80M, IV rank 36, Aug 4 earnings; Yahoo 401 |
| `mcp__uw-pp__insights_signal_confluence` | `{date: 2026-05-19, direction: bullish, min_score: 1, top_n: 100}` | **MARA absent** from top-100 |
| `mcp__uw-pp__insights_signal_confluence` | `{date: 2026-05-19, direction: bearish, min_score: 1, top_n: 100}` | **MARA absent** from top-100 |
| `mcp__uw-pp__insights_conviction_matrix` | `{symbol: MARA, date: 2026-05-19}` | MIXED, confidence 0.13 |
| `mcp__uw-pp__insights_price_vs_flow` | `{symbol: MARA, date: 2026-05-19, lookback_days: 30}` | No divergence, aligned bullish |
| `mcp__uw-pp__insights_analyst_vs_flow` | `{symbol: MARA, date: 2026-05-19}` | Flow side only; analyst absent |
| `mcp__uw-pp__insights_institutional_accumulation` | `{symbol: MARA, date: 2026-05-19}` | NEUTRAL, buy/sell 0.99, VWAP $12.09 |

## Tool errors

- `insights_deep_dive`: `yahoo_fundamentals` field returned
  `{"error":"yahoo quoteSummary MARA: HTTP 401"}`. Yahoo Finance
  fundamentals (P/E, market cap, analyst ratings, EPS estimates) are
  unavailable for this run. Phase 8 sub-agents should source from
  WebSearch (Stockanalysis.com, Seeking Alpha, etc.) if needed.

## Cross-check vs phases 1-5

| UW insight | Phase agreement? | Notes |
|------------|------------------|-------|
| signal_confluence (MARA absent both lists) | partial AGREE w/ phase-5 caveat | Phase 5's signal_backtest warning that bullish_flow is being faded across the market is consistent with the confluence template not lighting MARA up. Phase 1's "5/5 sweep persistence" is a stronger signal not captured by the standardized factors. |
| conviction_matrix MIXED | **AGREE** phase 1, 2, 3 | Phase 1 verdict: "modestly bullish, mixed near-term"; phase 2: "mixed-to-mildly bullish (balanced raw split)"; phase 3: "mixed-bullish, near-term capped, mid-term bullish". All three converge with MIXED. |
| institutional_accumulation NEUTRAL | **AGREE** phase 2 | Phase 2 reported buy_ratio 0.512 (block) / 0.497 (large) = balanced. UW's 0.99 buy/sell ratio (using shares not tier) confirms. |
| price_vs_flow aligned | **AGREE** phase 5 | Phase 5 showed +67% rally from 3/27 to 5/11 high with bullish flow on rally days. No divergence today. |
| top price levels include $11.75 | **AGREE** phase 2 | The 265K-share/6-trade cluster at $11.75 is the dip-buy block identified in phase 2 (210K + 30K + 31K matches). |
| Yahoo fundamentals error | no impact | Phase 8 to source independently if needed. |

**No internal contradictions** between phase 7's UW composite and the
phase 1-5 chain. Strong convergence on the **MIXED / range-bound** read.

## Verdict for downstream phases

- **UW composite bias:** **MIXED** (confidence 0.13 — very low directional
  edge)
- **Conviction:** 3/5 — UW agrees with the range read but contributes no
  independent edge; the strength is in *confirmation* of phases 1-5,
  not in new information.
- **Phase 9 baseline:** treat the trade as **range / spread structure**,
  not directional. The MIXED label combined with phase-4's mechanical
  gamma magnet at $12.5-$13 strongly favors a **defined-risk vol-neutral
  to vol-positive structure** rather than a long-stock or long-call bet.
- **Three things phase 9 must remember from this phase:**
  1. UW Conviction Matrix = MIXED, confidence 0.13 → "no edge in either
     direction" → trade the range, not direction.
  2. VWAP $12.09 below close $12.30-$12.44 → institutions paid up at
     close (small bullish tilt) but flat for the day.
  3. Crypto-miner peers (WULF, CIFR, HIVE, CORZ, CLSK) show stronger
     standardized confluence than MARA → if the trade is sector-cohort
     long crypto miners, MARA is the **fade leg / pair-trade short**
     candidate; if MARA is the *outright* trade, prefer a structure
     that doesn't require directional move.
- **Open questions for phase 8:**
  - Get current analyst consensus / price target (yfinance failed; use
    WebSearch on stockanalysis.com or Seeking Alpha)
  - Quantify the institutional/insider-ownership picture (large
    institutional buyers vs sellers in 13F-recent)
  - Cross-asset: how does MARA's structure compare with WULF/CIFR/HIVE
    options structure today (5 bullish vs MARA's mixed) — pair-trade
    candidate?
