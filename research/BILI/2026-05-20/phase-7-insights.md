# Phase 7 — UW Insights Confluence

**Ticker:** BILI
**As-of date:** 2026-05-20 (data date 2026-05-19)
**Generated:** 2026-05-20T10:30:00-04:00
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-5-historical.md, phase-6-macro.md

## Summary

UW's composite engines converge on **DIRECTIONAL_LONG with low confidence
(22.09%)** — dark pool buy/sell ratio 1.67 (640k buy vs 383k sell) and
aggressive call purchases dominate, but the magnitude and bullish_flow factor
count are below the threshold for top-tier confluence (BILI is **absent from
the top-50 score≥1 confluence list**, while sector peers PSKY and WBD score
5). The most actionable composite finding is the **constructive
price-vs-flow divergence**: 30-day price down 22.7% while net flow is bullish
(+$230,522) — a textbook flow-leading-price-reversal signature, exactly what
the institutional accumulation pattern in phase-2 would predict. Confirms
the **earnings beat reaction** thesis from phase-6.

## Key signals

- **Conviction matrix scenario: DIRECTIONAL_LONG** — confidence 22.09%; DP
  buy_ratio 0.626, call ask_volume 4,632 vs bid 3,151
  [INSIGHT:conviction_matrix].
- **Institutional accumulation: ACCUMULATION** — buy/sell ratio 1.67, VWAP
  $19.28 on 30-day price down -22.7% [INSIGHT:institutional_accumulation].
- **Price vs flow: DIVERGENCE TRUE (constructive)** — price -22.7% / flow
  +$230k bullish, IV rank 34 [INSIGHT:price_vs_flow].
- **Confluence score sub-threshold** — BILI not in top-50 with min_score=1
  while same-sector PSKY and WBD score 5 [INSIGHT:signal_confluence].
- **Implied move ±3.45% ($0.69)** for the front-month — modest
  post-earnings vol pricing [INSIGHT:deep_dive].

## Detailed findings

### Deep dive snapshot [INSIGHT:deep_dive]

```
Spot proxy           : avg_trade_price $19.33 (DP VWAP)
Total DP premium     : $19,728,031
DP trade count       : 80
DP shares            : 1,023,241
IV30d                : 48.02%
IV rank              : 34.32
Implied move (1mo)   : ±$0.69 (±3.45%)
PCR                  : 0.37
Call premium         : $729,962
Put premium          : $272,003
Total OI             : 274,470
next_earnings_date   : 2026-05-19 (PAST — just reported)
Yahoo fundamentals   : HTTP 401 (Yahoo gated)
```

Yahoo fundamentals errored; phase-6 captured the actual Q1 2026 earnings
content from SEC 6-K directly. **Confirmed: BILI just reported.**

### Signal confluence (market-wide ranking) [INSIGHT:signal_confluence]

BILI **does NOT appear** in the top-50 bullish-confluence list with min_score
lowered to 1. The 50 names that did clear (mostly score 5 — bullish_flow +
low_pcr + dp_accumulation + oi_building + low_iv_cheap_options) are all
**better-aligned than BILI** on at least one factor.

Specifically, the breakdown of BILI's factors that ARE firing:
- low_pcr ✓ (0.37 vs typical threshold 0.7)
- dp_accumulation ✓ (buy_sell ratio 1.67 — phase-2)
- low_iv_cheap_options ✓ (IV rank 34, percentile 0 — phase-5)

And factors NOT firing strongly enough:
- bullish_flow ✗/weak: net flow $230k is bullish-tilted but small absolute size
- volume_spike ✗: ratio not extreme (today's 8,714 calls / 3,193 puts is
  active but not a spike)
- oi_building ✗/weak: total OI 274k vs 247k 6 weeks ago (+11%) — building
  but spread across many strikes, not a single concentration

**Same-sector reference rows (also Communication Services / Comm-adjacent):**
- WBD (Comm Services): score 5, IV rank 8, net flow $1.51M, PCR 0.68
- PSKY (Comm Services): score 5, IV rank 19, net flow $501k, PCR 0.41

Conclusion: BILI's setup is **constructive but below the confluence floor**.
This is a real downgrade vs. naively bullish reads of phase-1.

### Conviction matrix [INSIGHT:conviction_matrix]

```
Scenario     : DIRECTIONAL_LONG
Confidence   : 22.09%  (LOW)
DP buy_ratio : 0.626   (above bull threshold 0.60)
Call ask vol : 4,632
Call bid vol : 3,151   (call ask/bid 1.47x)
Put ask vol  : 1,264
Put bid vol  : 1,443   (put bid/ask 1.14x — puts being SOLD net)
Explanation  : "Dark pool buying + aggressive call purchases — 
                institutional directional bet."
```

**This is the cleanest single composite verdict.** Two-axis classification:
- Dark-pool axis: BUY (ratio 0.626 > 0.6 threshold)
- Options-flow axis: CALL_BUY (call ask/bid > 1; put ask/bid < 1)
- → DIRECTIONAL_LONG quadrant

The 22.09% confidence number reflects the **magnitude weakness** — DP buy
ratio is only barely past the 0.6 threshold, and the call ask/bid 1.47x is
moderate, not extreme.

### Price vs flow [INSIGHT:price_vs_flow]

```
Period high       : $25.63
Period low        : $18.30
Price start (30d) : $23.77
Price end (30d)   : $18.38
Price change      : -22.7%
Flow direction    : bullish
Net flow          : +$230,522
PCR               : 0.37
IV rank           : 34.3
Divergence        : TRUE
Signal text       : "Price is down 22.7% but options flow is bullish"
```

**This is a CONSTRUCTIVE divergence (flow leading reversal):** price has
sold off hard, flow has turned bullish. Classically precedes reversal —
**confirmed by phase-2 institutional block buying (1.00 buy_ratio) at the
lows of the move**. Important caveat: divergence signals are early — pair
with phase-4 dealer regime (which is fresh-positive-gamma → mean-reversion
into $20 magnet) for timing.

### Analyst vs flow [INSIGHT:analyst_vs_flow]

```
Flow sentiment : bullish
Bullish prem   : $583,912
Bearish prem   : $353,390
Net flow       : +$230,522
PCR            : 0.37
Analyst data   : (not returned — likely Yahoo gating, as with deep_dive)
```

**Analyst consensus could not be retrieved** in this run. Phase-6 noted
broader sentiment on China ADRs has been negative (KWEB -16% YTD); for an
analyst-vs-flow read, a manual ratings pull (e.g., from WSJ / Bloomberg /
yfinance with fresh auth) would be needed. **Limitation noted.**

### Institutional accumulation [INSIGHT:institutional_accumulation]

```
Signal         : ACCUMULATION
Buy_sell_ratio : 1.67
Buy_side_vol   : 640,331
Sell_side_vol  : 382,910
Trades         : 80
VWAP           : $19.28
30d price chg  : -22.7%
Total DP prem  : $19,728,031
Total DP vol   : 1,023,241

Top price levels (today):
  $19.65 — 189,972 sh / $3.73M / 8 trades
  $18.82 — 124,530 sh / $2.34M / 3 trades
  $18.98 —  76,800 sh / $1.46M / 1 trade
  $19.55 —  52,500 sh / $1.03M / 6 trades
  $19.20 —  49,199 sh / $945k  / 1 trade
```

**Unambiguous ACCUMULATION signal** — perfectly aligned with phase-2's
block-tier buy_ratio 1.00 finding. The 1.67 buy/sell ratio is the
**all-tier composite** (vs phase-2's per-tier breakdown), giving the same
directional answer at lower magnitude.

### Earnings play [INSIGHT:earnings_play]

BILI **does NOT** appear in the 120-day forward earnings_play universe (top
30 names with IV rank ≥20). The screener only returns pre-earnings setups
with **rising** OI and IV rank. Confirmation:
- BILI just reported on 2026-05-19 → no upcoming earnings within the
  120-day window that the screener captured (the next BILI earnings is
  likely Q2 in **late-August 2026**, which is ~93 days out — at the edge
  of the window — but BILI's IV rank 34 is well below the IV-rich threshold
  the screener favors).
- The pattern is consistent with **post-earnings IV crush** — phase-5's
  IV rank trajectory 89 → 34 over 6 sessions.

The 8/21 $18 PROTECTIVE PUT OI build flagged in phase-3 [OI:biggest_increases]
aligns with **someone hedging into the Q2 print** roughly 93 days out — i.e.,
the institutional bloc has positioned for the next earnings, not this one.

## Cross-check vs phases 1–6

| UW insight | Upstream agreement | Notes |
|---|---|---|
| `conviction_matrix`: DIRECTIONAL_LONG, 22% conf | Phase 1: mixed-bullish 3/5; Phase 2: accumulation 4/5; Phase 3: range-bull-skew 3/5 | **AGREES** — composite slightly upgrades phase-1 mixed-bullish to a confident-direction label, but the low 22% confidence number aligns with phase-1's 3/5 conviction. |
| `signal_confluence`: BILI absent | Phase 5: cumulative 28d flow MIXED; Phase 6: sector outflow $-84M | **AGREES** — cross-sectional confluence floor not cleared, sector headwind matters. |
| `price_vs_flow`: DIVERGENCE bullish | Phase 5: -25% drawdown + bullish flip today | **AGREES strongly** — phase-5 narrative confirmed independently. |
| `institutional_accumulation`: ACCUMULATION | Phase 2: block-tier buy_ratio 1.00, large-tier 0.465 | **AGREES** — composite ratio 1.67 sits between block-tier and large-tier reads. |
| `earnings_play`: BILI absent | Phase 6: earnings on 2026-05-19 (PAST) | **AGREES** — confirms post-earnings status, no fresh pre-event setup. |
| `analyst_vs_flow`: no analyst data | Phase 6: KWEB sector weak | **Limitation** — analyst data not retrieved. Phase-8 sub-agents can fill if needed. |

**No contradictions detected.** Phase-7 is the cleanest internal
consistency check the run could provide; everything that loaded points the
same direction: a **constructive but not high-conviction post-earnings
bullish setup** with institutional dark-pool accumulation at the lows.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|---|---|---|
| `insights_deep_dive` | symbol=BILI, date=2026-05-19 | DP $19.73M, IV rank 34, next earn 5/19 PAST, Yahoo HTTP 401 |
| `insights_signal_confluence` | direction=bullish, min-score=1, top-n=50 | BILI absent; WBD/PSKY same-sector at score 5 |
| `insights_conviction_matrix` | symbol=BILI | DIRECTIONAL_LONG, conf 22.09%, DP ratio 0.626 |
| `insights_price_vs_flow` | symbol=BILI, lookback=30 | DIVERGENCE TRUE: -22.7% price / +$230k bullish flow |
| `insights_analyst_vs_flow` | symbol=BILI | Flow bullish, no analyst data returned |
| `insights_institutional_accumulation` | symbol=BILI | ACCUMULATION, ratio 1.67, VWAP $19.28 |
| `insights_earnings_play` | days=120, min-iv-rank=20, top-n=30 | BILI absent — post-earnings, IV rank 34 below event-rich threshold |

## Tool errors

- `insights_deep_dive` → yahoo_fundamentals "yahoo quoteSummary BILI: HTTP
  401". Not a blocker (phase-6 supplied fundamentals from SEC 6-K directly).
- `insights_analyst_vs_flow` returned no analyst consensus (silently empty
  — same Yahoo limitation suspected).

## Verdict for downstream phases

- **UW composite bias:** **DIRECTIONAL_LONG with low confidence (22%)** +
  **ACCUMULATION** signal + **constructive price-vs-flow divergence**.
  This is the baseline for phase-9.
- **Conviction:** **3 / 5** — composite engine result is strong directionally
  but low-magnitude. The sub-confluence-threshold ranking is the most
  honest restraint indicator: BILI is not a top-tier conviction name today,
  it is a constructive single-name idea in a mixed market.
- **Phase 9 should treat as BASELINE**, and only override with specific
  contrary evidence from phases 1–8:
  - **No contrary evidence detected.** All phases align with
    constructive-but-not-maximal positioning.
- **Open questions:**
  - Why is BILI's confluence score sub-threshold while WBD and PSKY (same
    sector) score 5? Could be relative DP-volume scale — phase-9 should
    treat BILI sizing as **smaller** than the comparable WBD/PSKY allocation
    a trader would use.
  - Are there pending analyst rating actions post-Q1 print? Phase-8
    `accumulation-hunter` and `earnings-scout` sub-agents may add color
    from broader web sources.
