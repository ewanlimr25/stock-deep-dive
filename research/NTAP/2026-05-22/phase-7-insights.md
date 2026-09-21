# Phase 7 — UW Insights Confluence

**Ticker:** NTAP
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T00:00:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-4-structure.md, phase-5-historical.md, phase-6-macro.md, phase-0.5-context.md

## Summary

UW's composite tools are **unanimous and confirm every upstream phase**: the
scenario is **MIXED** (conviction confidence 7.3%), institutional footprint is
**NEUTRAL** (DP buy/sell 1.34, "balanced"), and there is a confirmed
**price-vs-flow DIVERGENCE — price +41.6% while options flow is bearish (net
−$48,537)**. NTAP is **absent from the top-50 bullish signal-confluence list** —
its bullish stack scores below the cut (wrong-signed flow, high not low IV, no OI
build, neutral DP). The earnings-play tool places NTAP 6 days from the 5/28 print
at **IV rank 100, implied move 10.64%**, but with a **trivial OI build (+349 vs
peer FUTU +30,789)** — no fresh pre-earnings positioning. The baseline phase-9 must
respect: **this is a high-IV pre-earnings EVENT name with a bearish flow divergence
and no directional conviction — a volatility trade, not a directional long.**

## Key signals

- **Conviction matrix: MIXED** (7.3% confidence) — call bid>ask & put bid>ask = net
  selling, balanced DP [INSIGHT:conviction_matrix]
- **Institutional accumulation: NEUTRAL** — buy/sell 1.34, "balanced dark pool",
  price +41.6% 30d [INSIGHT:institutional_accumulation]
- **Price-vs-flow DIVERGENCE = true** — "+41.6% price vs bearish flow" (reversal
  watch) [INSIGHT:price_vs_flow]
- **Absent from top-50 bullish confluence** — no bullish factor stack [INSIGHT:signal_confluence]
- **Earnings play: 6 days to 5/28, IV rank 100, implied move 10.64%, OI build +349
  (trivial)** [INSIGHT:earnings_play]

## Detailed findings

### Deep-dive snapshot + whole-tape directional aggregates — `[INSIGHT:deep_dive]`

| Metric | Value |
|--------|-------|
| Spot / VWAP | $139.36 / $136.82 |
| bullish_premium vs bearish_premium | $4,950,598 vs **$4,999,135** (net bearish) |
| net_flow | **−$48,537** |
| call_premium vs put_premium | $9,346,981 vs $1,488,717 |
| put_call_ratio | 0.178 |
| **implied_move / implied_move_perc** | **$14.82 / 10.64%** (phase-9 N4 sizes to this) |
| iv_rank / iv30d | **100** / 57.6% |
| total_open_interest | 29,220 |
| next_earnings_date | **2026-05-28** |
| DP total premium | $88.29M (645,259 sh, 278 trades) |
| Yahoo fundamentals | **error: HTTP 401** (unavailable — see phase-7b Finnhub) |

Whole-tape aggregates **reconcile exactly** with phase-1 (net-flat-to-bearish, call
volume not matched by net call premium) and phase-0.5 `[CTX:]` (bottom-decile
net-directional, top-5% magnitude).

### Signal confluence — `[INSIGHT:signal_confluence]`

NTAP is **not in the top-50 bullish list** (min_score=1). The list is dominated by
small/mid names scoring 5–6 (QSI, SKYT, ASTS, F, HON…) whose factors are
`bullish_flow / low_pcr / volume_spike / dp_accumulation / oi_building /
low_iv_cheap_options`. NTAP **fails the bullish stack**: its flow is bearish-signed,
IV is *high* (not the cheap-options factor), there's no OI build, and DP is neutral.
**No bullish confluence.**

### Conviction matrix — `[INSIGHT:conviction_matrix]`

- **scenario MIXED**, confidence 7.32%. DP buy_ratio 0.573 → "Balanced dark pool —
  no clear bias."
- Options flow: call_ask 7,306 vs **call_bid 7,649** (selling calls), put_ask 848 vs
  **put_bid 1,884** (selling puts). **Confirms phase-1's net-selling / premium-harvest
  read precisely.**

### Price vs flow — `[INSIGHT:price_vs_flow]`

- **divergence = true:** "Price is up 41.6% but options flow is bearish (net
  −$48,537)." Period high $141.75, low $95.06, end $139.36.
- Per the heuristic this is a **leading reversal signal, often early** — and the
  rubric says pair it with phase-4. Phase-4 = **long-gamma/mean-reversion** regime
  into the event → the divergence + pinning regime + above-target valuation
  (phase-6) all lean toward **caution on chasing the rally / a fade skew** post-print.

### Analyst vs flow — `[INSIGHT:analyst_vs_flow]`

- Tool returned **only the options-flow side** (flow_sentiment bearish, net −$48,537);
  the Yahoo analyst-consensus portion was unavailable (same HTTP 401 as deep_dive).
- **Substitute from phase-6 WebSearch:** Street is **split** — BofA PT $125 (raised),
  Morgan Stanley Underweight, BWG downgrade. Crucially the bull-case **$125 < spot
  $139.36**. So Wall Street consensus is *not* validating the post-spike price, while
  options flow is bearish-divergent — **analysts and flow broadly agree: skepticism
  into the print.**

### Institutional accumulation — `[INSIGHT:institutional_accumulation]`

- **signal NEUTRAL** — "balanced dark pool activity." buy_sell_ratio 1.34, buy vol
  369,892 vs sell 275,367, price_30d +41.63%. Top DP levels $134–138 (today's
  blocks). Agrees with phase-2 (mild/suggestive, not conviction) — UW's all-tier read
  lands at NEUTRAL vs my block-tier 0.653 "mild buy."

### Earnings play — `[INSIGHT:earnings_play]` (in-window: 6 days)

- NTAP: days_to_earnings **6**, earnings **2026-05-28**, **iv_rank 100**,
  **implied_move 10.64%**, PCR 0.178, **OI increase +349 / decrease −118**.
- Context vs the earnings cluster: peers **HPQ (5/27), HPE (6/1)** also at IV rank
  100 — the storage/hardware complex reports together. **NTAP's OI build (+349) is
  trivially small** vs FUTU (+30,789), TIGR (+59,039), PANW (+15,162) → confirms
  phase-3: **no fresh pre-earnings positioning** despite the huge premium churn.
- NTAP is also one of the few names in the list with **bearish > bullish premium**
  — more skeptically positioned than the typical earnings-play name.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__insights_conviction_matrix` | symbol=NTAP | **MIXED**, conf 7.3%, DP 0.573 |
| `mcp__uw-pp__insights_institutional_accumulation` | symbol=NTAP | **NEUTRAL**, buy/sell 1.34 |
| `mcp__uw-pp__insights_price_vs_flow` | symbol=NTAP, lookback=30 | **DIVERGENCE true** (+41.6% vs bearish) |
| `mcp__uw-pp__insights_analyst_vs_flow` | symbol=NTAP | flow bearish; analyst side unavailable (401) |
| `mcp__uw-pp__insights_earnings_play` | days=14, min_iv=40, top_n=20 | NTAP 6d, IV100, move 10.64%, OI+349 |
| `mcp__uw-pp__insights_signal_confluence` | bullish, min_score=1, top_n=50 | **NTAP absent** (no bullish stack) |

## Tool errors

- `insights_analyst_vs_flow` / `insights_deep_dive` Yahoo fundamentals: **HTTP 401**
  (Yahoo quoteSummary blocked). Not fatal — phase-7b pulls fundamentals from Finnhub
  and phase-6 supplied analyst ratings via WebSearch.

## Cross-check vs phases 1–6

| UW insight | Phase agreement? | Notes |
|------------|------------------|-------|
| signal_confluence (NTAP absent) | **agrees** phases 1,3,5 | no bullish stack — matches flat flow, static OI, bearish cumulative flow |
| conviction_matrix MIXED | **agrees** phase-1 | net call+put selling = premium harvest |
| institutional_accumulation NEUTRAL | **agrees** phase-2 | balanced DP (block 0.653 buy → all-tier NEUTRAL) |
| price_vs_flow DIVERGENCE | **agrees** phase-5 | +42% price vs net-bearish flow (the divergence) |
| earnings_play (IV100, OI+349) | **agrees** phases 3,4,5 | event name, no fresh OI, IV maxed |

**Zero internal contradictions.** Every composite confirms the upstream read.

## Verdict for downstream phases

- **UW composite bias:** **MIXED / NEUTRAL with a bearish flow divergence.** Not a
  directional long; not a clean short. A **high-IV pre-earnings VOLATILITY/EVENT
  setup** with a fade-skewed risk profile (divergence + above-target valuation +
  long-gamma pin).
- **Conviction:** **3/5** that this baseline is correct (the instrumentation is
  unanimous; the only bullish inputs — price momentum + AI catalyst — are not
  confirmed by flow/DP/OI/confluence).
- **Phase-9 guidance:** Treat **MIXED / event-vol / no-directional-edge** as the
  BASELINE. Override toward bullish only on specific contrary evidence (there is
  little); the consistent signal is *premium is rich and direction is unconfirmed* →
  favour **defined-risk, vol-aware** structures (phase-5 VRP +13.3, phase-4 crush).
- **Open questions for 7b/7c/8b:** Does fundamental quality (phase-7b) justify $139
  or flag overvaluation (bull-case target is $125)? Does sentiment/short-interest
  (phase-7c) confirm the bearish flow divergence is smart skepticism vs mechanical
  overwriting? In the debate (phase-8b), can the bull overcome (a) no bullish
  confluence, (b) price above bull-case target, (c) the negative-vanna post-earnings
  crush?
