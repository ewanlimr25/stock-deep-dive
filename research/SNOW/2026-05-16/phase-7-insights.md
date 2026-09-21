# Phase 7 — UW Insights Confluence

**Ticker:** SNOW
**As-of date:** 2026-05-16 (data date: 2026-05-15)
**Generated:** 2026-05-17T00:00:00Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-4-structure.md, phase-5-historical.md, phase-6-macro.md

## Summary

The UW composite insights stack labels SNOW **MIXED / NEUTRAL** at 1.82% confidence — a low-conviction read that **AGREES with phase-2's "balanced-to-distributive" dark pool** and the phase-3 short-strangle structure interpretation. **SNOW does NOT appear in the bullish_signal_confluence top 20 even at min_score=1**, because its IV rank 97 disqualifies it from the "low_iv_cheap_options" factor and its dark-pool buy_ratio of 0.482 is below the bullish threshold (0.6) — so the institutional-accumulation factor is also missing. The only confluence-positive signals are bullish options flow + low P/C ratio + OI building, which is exactly the pattern phase-5 backtested at a **20% win rate**. SNOW DOES appear prominently in `insights_earnings_play` (rank 14 of 15) with **12 days to Q1 FY27 earnings**, IV rank 97.08, and the largest absolute OI increase on the list (+16,771 contracts). **Bottom line: this is a high-IV earnings setup with internal flow inconsistency** — exactly the profile of a "sell the IV crush" / defined-risk play, not a directional debit long.

## Key signals

- **Conviction matrix: MIXED at 1.82% confidence** [INSIGHT:conviction_matrix]: dark_pool buy_ratio 0.482 (below 0.6 bull threshold), options flow tilted slightly call-side ask. UW's own classifier sees no clear bias.
- **SNOW absent from bullish_signal_confluence top 20** [INSIGHT:signal_confluence]: even with `min_score=1`, SNOW does not score. Top 20 are dominated by low-IV-rank names (avg IV rank ~30) — SNOW's IV rank 97 fails the "cheap options" factor.
- **price_vs_flow: ALIGNED, no divergence** [INSIGHT:price_vs_flow]: 30d price +5.42% ($149.38 → $157.47), net premium flow +$984k bullish → **flow and price agree**, NO reversal divergence flagged.
- **Institutional accumulation: NEUTRAL** [INSIGHT:institutional_accumulation]: DP buy_sell_ratio 0.93 (just below 1.0 = balanced), no accumulation signal. Reconciles with phase-2.
- **Earnings play setup live** [INSIGHT:earnings_play]: 12 days to 2026-05-27 earnings, IV rank 97.08, OI building (+16,771 contracts) — confirms phase-4 IV kink and phase-6 catalyst.

## Detailed findings

### Deep dive snapshot

[INSIGHT:deep_dive]:

```
SCREENER:
  iv30d:               86.83%
  iv_rank:             97.08
  put_call_ratio:      0.23
  call_premium:        $46,888,501
  put_premium:         $9,132,051
  bullish_premium:     $26,643,166
  bearish_premium:     $25,659,174     (near-parity)
  net_flow:            +$983,992
  call_volume:         78,227
  put_volume:          17,985
  total_open_interest: 608,469
  implied_move:        $0.51 (0.327% — daily, not earnings)
  next_earnings_date:  2026-05-27
  volatility:          8.00 (annualized %?)

DARK POOL:
  total_premium:  $108,211,049
  total_shares:   691,424
  trade_count:    403
  avg_price:      $156.79

TOP OI CHANGES (top 5):
  150P 5/22 (DTE 7):   +930 OI, $5.72 avg, 1,018 vol
  180C 6/18 (DTE 34):  +929 OI, $6.67 avg, 2,285 vol
  160C 5/29 (DTE 14):  +872 OI, $9.17 avg, 1,310 vol
  200C 6/18 (DTE 34):  +869 OI, $3.45 avg, 2,622 vol
  200C 5/29 (DTE 14):  +821 OI, $1.75 avg, 1,648 vol

YAHOO FUNDAMENTALS: error (HTTP 401) — Yahoo quoteSummary blocked.
```

The Yahoo quoteSummary 401 error means we have **no fundamentals (PE, market cap, short interest, EV/Sales)** from this tool. Phase 6 WebSearch partially compensated (we know YTD -28%, RBC PT cut, AI-Data-Cloud product progress) but precise valuation multiples are unavailable. **This is a known data gap** — phase 10 should flag for re-run if a fundamentals overlay is needed.

The screener data restates what phases 1-3 already established but with the critical add: **bullish vs bearish premium is near parity** ($26.6M vs $25.7M, +$984k net). This is **much weaker than the phase-1 narrative of "net bullish" suggested**. The bullish lean is real but extremely thin.

### Signal confluence

[INSIGHT:signal_confluence] (direction=bullish, min_score=1, top_n=20):

```
SNOW: NOT in top 20.
```

Top scoring tickers (score 6, then 5):

| Rank | Ticker | Sector | Score | IV rank | Factors |
|---|---|---|---|---|---|
| 1 | DXCM | Healthcare | 6 | 25.8 | bullish_flow, low_pcr, volume_spike, dp_accumulation, oi_building, low_iv_cheap_options |
| 2 | BOOT | Cons Cyclical | 6 | 11.8 | same |
| 3 | STAA | Healthcare | 6 | 29.4 | same |
| 4 | ENPH | Technology | 5 | 85.0 | (missing low_iv) |
| ... | ... | ... | ... | ... | ... |
| (none) | SNOW | Technology | — | 97.08 | misses low_iv (IV too rich); misses dp_accumulation (buy_ratio 0.48 < 0.6) |

**Analysis:** SNOW would need **dark-pool accumulation** (buy_ratio ≥ 0.6) AND/OR **low-IV/cheap-options** (it's IV rank 97 — premium is the opposite of cheap) to score ≥3. It has bullish_flow + low PCR + oi_building (probably 3 factors) but the missing two are what disqualify it. **This is a critical contrarian flag from UW's own composite layer**: SNOW's bullish flow today is happening in expensive-options/balanced-dark-pool context — historically a low-edge setup.

### Conviction matrix

[INSIGHT:conviction_matrix]:

```
scenario:        MIXED
confidence_pct:  1.82%
explanation:     "Balanced dark pool activity — no clear bias."

dark_pool:
  buy_ratio:    0.482
  buy_volume:   333,122
  sell_volume:  358,302
  trades:       403

options_flow:
  call_ask_volume: 37,281
  call_bid_volume: 33,772    (ask > bid by 10% on calls)
  put_ask_volume:  7,353
  put_bid_volume:  8,547     (bid > ask on puts = puts being sold = bullish lean)

thresholds: bull=0.6, bear=0.4
```

**MIXED** is the lowest-conviction scenario tag. The ask>bid imbalance on calls (+3,509 contracts ask-side) and bid>ask on puts (+1,194 contracts bid-side = put selling) net to a slight bullish lean, but dark-pool buy_ratio 0.482 (close to 50/50) prevents the model from upgrading to HEDGED_LONG or DIRECTIONAL_LONG.

### Price vs flow

[INSIGHT:price_vs_flow]:

```
period:           30 days
price_start:      $149.38
price_end:        $157.47
price_change_pct: +5.42%
period_high:      $159.83
period_low:       $118.30
flow_direction:   bullish
net_premium_flow: +$983,992
put_call_ratio:   0.23
divergence:       false
divergence_signal: "Price and flow are aligned"
```

**No divergence detected.** Flow and price agree at +5% over 30d. This removes one common reversal-warning signal (i.e., we don't have "bullish flow into a falling price" or "bearish flow into a rising price"). But the magnitude of net flow ($984k) relative to gross flow ($52M) is **only 1.9% net skew** — flow is essentially balanced.

The 30d range ($118.30 - $159.83 = $41.53 = 33% range on a $138 mid) confirms SNOW's been in a **high-volatility, wide-range regime** — consistent with the 92nd-percentile IV.

### Analyst vs flow

[INSIGHT:analyst_vs_flow]:

```
options_flow:
  flow_sentiment:    bullish
  bullish_premium:   $26,643,166
  bearish_premium:   $25,659,174
  net_flow:          +$983,992
  put_call_ratio:    0.23
```

The tool returned only the flow side — **Yahoo analyst data unavailable** (consistent with the deep_dive 401). Phase 6 supplements this: Wall Street is "cautious bullish" with avg PT implying +66-71% upside, but RBC cut PT to $220 from $245 on 5/15. So we have **partial alignment** (analysts moderately bullish PT-wise; flow slightly bullish today; price aligned with both). This is a generally "consensus bullish" setup — which is itself a contrarian flag if the consensus has been wrong (RBC just downgraded the target).

### Institutional accumulation

[INSIGHT:institutional_accumulation]:

```
signal:               NEUTRAL — balanced dark pool activity
buy_sell_ratio:       0.93
buy_side_volume:      333,122
sell_side_volume:     358,302
trades:               403
total_dp_premium:     $108,211,049
total_dp_volume:      691,424
avg_trade_price:      $156.79
vwap:                 $156.50
price_30d_change_pct: +5.42%

Top price levels (by premium):
  $157.72 — $4.32M, 27,400 sh, 5 trades
  $157.85 — $3.32M, 21,034 sh, 3 trades
  $158.99 — $3.02M, 19,000 sh, 1 trade
  $157.58 — $2.51M, 15,902 sh, 10 trades
  $150.46 — $2.03M, 13,500 sh, 1 trade
```

**Signal: NEUTRAL.** This **agrees with phase-2's read** (balanced LARGE tier, slightly-distributive BLOCK tier). Buy_sell_ratio 0.93 means slightly more sell than buy by share, which UW labels NEUTRAL because the threshold for ACCUMULATION is >1.5 and DISTRIBUTION is <0.7. The top single-block prints concentrate at $157-$159 (intraday rally zone) NOT at $150-$153 (the 5-day institutional support).

### Earnings play

[INSIGHT:earnings_play] (days_until_earnings=14, min_iv_rank=40, top_n=15):

SNOW appears as rank **14 of 15** in the universe:

| Rank | Ticker | DTE | Earnings date | IV rank | implied_move% | P/C | OI Δ |
|---|---|---|---|---|---|---|---|
| 1 | ZS | 11 | 2026-05-26 | 100 | 0.974% | 0.40 | +6,791 / -1,241 |
| 2 | TTWO | 6 | 2026-05-21 | 100 | 0.695% | 0.73 | +5,796 / -2,353 |
| 3 | WDAY | 6 | 2026-05-21 | 100 | 0.198% | 0.77 | +3,866 / -1,968 |
| 4 | OKTA | 13 | 2026-05-28 | 100 | 0.442% | 0.30 | +2,883 / -620 |
| 5 | DLTR | 13 | 2026-05-28 | 100 | 0.610% | 0.67 | +1,425 / -475 |
| ... | ... | ... | ... | ... | ... | ... | ... |
| 14 | **SNOW** | **12** | **2026-05-27** | **97.08** | **0.327%** | **0.23** | **+16,771 / -3,898** |
| 15 | URBN | 5 | 2026-05-20 | 96.41 | 1.203% | 3.34 | +6,043 / -63 |

**SNOW has by far the largest OI build (+16,771)** of any name on this list — even more than ZS (#1 by IV rank). Combined with the lowest P/C ratio (0.23 = most call-heavy) and highest absolute call concentration, this is a **textbook pre-earnings call-buildup setup**. The implied_move_perc field (0.327%) is the tool's daily implied move, not the event implied move; the actual event-implied move from the IV kink (107.6% on 5/29 vs 71.2% on 5/22) is around ±9-12%.

Cohort context: SNOW reports the same day as ZS (5/26-27) and one day before OKTA, DLTR (5/28). The whole "cloud/software" cohort is reporting in the same 6-day window (5/21 WDAY, 5/21 ZM, 5/21 TTWO, 5/26 ZS, 5/27 SNOW + HEI + BBWI, 5/28 OKTA + DLTR + BBY). **Cohort dynamics will matter** — phase 9 should consider whether SNOW trades on its own print or on cohort sympathy (especially ZS the day before).

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__insights_deep_dive` | symbol=SNOW | screener + DP + top OI; Yahoo fundamentals 401 |
| `mcp__uw-pp__insights_signal_confluence` | direction=bullish, min_score=1, top_n=20 | SNOW absent (IV-rank disqualifies) |
| `mcp__uw-pp__insights_conviction_matrix` | symbol=SNOW | MIXED, 1.82% confidence, DP buy_ratio 0.482 |
| `mcp__uw-pp__insights_price_vs_flow` | symbol=SNOW, lookback=30 | aligned, no divergence, +5.42% / +$984k |
| `mcp__uw-pp__insights_analyst_vs_flow` | symbol=SNOW | flow only (yfinance blocked) |
| `mcp__uw-pp__insights_institutional_accumulation` | symbol=SNOW | NEUTRAL, buy_sell_ratio 0.93 |
| `mcp__uw-pp__insights_earnings_play` | days=14, min_iv_rank=40, top_n=15 | SNOW #14, biggest OI build of cohort |

## Tool errors

- `insights_deep_dive` Yahoo fundamentals: `yahoo quoteSummary SNOW: HTTP 401`. No fundamentals (PE, market cap, short interest) available from this tool. Partially compensated by phase-6 WebSearch (YTD perf, PT, product news).
- `insights_analyst_vs_flow` returned only the flow side because of the same Yahoo block. Use phase-6 WebSearch coverage for analyst consensus.

## Cross-check vs phases 1–5

| UW insight | Phase 1 (flow) | Phase 2 (DP) | Phase 3 (OI) | Phase 4 (struct) | Phase 5 (hist) | Agreement |
|---|---|---|---|---|---|---|
| signal_confluence (SNOW absent) | bullish (4/5 conv) | mildly distributive | mixed strangle | positive GEX | bullish-flow 20% win rate | UW **AGREES** with phase-5's contrarian read; **PARTIALLY DISAGREES** with phase-1 |
| conviction_matrix (MIXED) | bullish | balanced | mixed | positive GEX | high IV | UW **AGREES** with phase-2, phase-3, phase-5; disagrees with phase-1 |
| price_vs_flow (no divergence) | bullish flow into rally | sellers on early prints | n/a | DEX call-heavy lifting tape | 30d up 5.4% | UW **AGREES** — flow and price both up, no reversal signal |
| institutional_accumulation (NEUTRAL) | n/a | balanced LARGE / distributive BLOCK | n/a | DEX +$113.8B (mechanical bid) | OI building 20d | UW **AGREES** with phase-2's NEUTRAL/balanced — but it averages over the BLOCK-tier distribution that phase-2 isolated |
| earnings_play (live) | n/a | n/a | OI building toward 5/29 | IV kink at 5/29 | high IV / VRP +13% | UW **AGREES** with phase-4 and phase-5 — earnings setup confirmed |

**The composite reads agree with the more skeptical phases (2, 3, 5) and disagree with phase 1's bullish-conviction-4/5 read.** Phase 9 must weight this carefully. UW's own composite tools are giving the same signal phase-5's backtest gave: this is NOT a clean bullish setup.

## Verdict for downstream phases

- **UW composite bias:** **MIXED → modestly bullish but low conviction.**
- **Conviction:** 2/5. The only strong signal is the earnings-play setup (large OI build into 5/27 with high IV), which is a VOL trade, not a directional trade.
- **Phase 9 should treat this as the BASELINE** — the directional bull thesis from phase 1 is **NOT** corroborated by UW's composite layer. Phase 9 must either:
  - (a) Demote the directional bull thesis and elevate the EARNINGS-VOL (premium-sell) thesis as primary, OR
  - (b) Construct a defined-risk bullish structure that profits from a positive earnings surprise without paying full IV-rich premium, OR
  - (c) Stand aside if no defined-risk structure has positive expected value.
- **Three datapoints phase-9 MUST carry forward:**
  1. **MIXED scenario at 1.82% confidence** — single most authoritative composite read.
  2. **SNOW absent from bullish_signal_confluence top 20 at min_score=1** — historically the worst setup pattern.
  3. **Largest OI build (+16,771) of any name in the earnings_play universe** — there IS something going on into 5/27, just not directional-clean.
- **Open questions:**
  - Cohort earnings sequencing (5/21 WDAY/TTWO/ZM, 5/26 ZS, 5/27 SNOW) — does SNOW IV de-grip on a ZS beat/miss the prior day?
  - With Yahoo fundamentals blocked, we cannot confirm SNOW's valuation multiple (P/Sales, EV/Sales). Phase 9 will rely on phase-6's YTD-down-28% as proxy for "deep oversold context."
