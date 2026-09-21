# Phase 7 — UW Insights Confluence

**Ticker:** HOOD
**As-of date:** 2026-06-15
**Generated:** 2026-06-16T12:50:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-4-structure.md, phase-5-historical.md

## Summary

UW's composite layer paints the **full qualitative bullish stack — but at low
confidence**. The conviction matrix returns **DIRECTIONAL_LONG** ("Dark pool buying +
aggressive call purchases — institutional directional bet"), institutional-accumulation
returns **ACCUMULATION** (buy/sell ratio 1.7, $497.3M DP premium), and price-vs-flow
shows **no divergence** (price +28.2%, flow bullish, aligned) — per this skill's
heuristic, that triad is "the strongest possible bullish stack on this instrumentation."
**However** the conviction-matrix confidence is only **14%**, and HOOD is **outside the
top-20 bullish signal-confluence names** (all scoring 5–6 — HOOD scores <5; fintech
peer AFRM makes the cut, HOOD does not). So the *direction* is unambiguously bullish-long
and accumulation is real, but the *magnitude/confidence* is weak — exactly consistent
with phase-5's poor backtest (28.6%) and the two-sided, modest-net tape.

## Key signals

- Conviction matrix **DIRECTIONAL_LONG**, confidence **14%** — bullish but low-conf
  `[INSIGHT:conviction_matrix]`.
- Institutional-accumulation **ACCUMULATION**, buy/sell **1.7** (buy 3.16M vs sell
  1.86M sh, $497.3M DP, VWAP $99.12) — confirms phase-2 `[INSIGHT:institutional_accumulation]`.
- Price-vs-flow **no divergence**: +28.18% price, bullish flow, aligned; period range
  $73.18–$100.87 `[INSIGHT:price_vs_flow]`.
- HOOD **outside top-20 bullish confluence** (cut is score ≥5; HOOD <5) — sub-elite
  composite `[INSIGHT:signal_confluence]`.
- Whole-tape directional aggregates: bullish $106.4M vs bearish $97.8M → **net_flow
  +$8.68M**; call $197.9M vs put $35.2M; PCR 0.346; implied move ±4.65%
  `[INSIGHT:deep_dive]`.

## Detailed findings

### Deep-dive snapshot `[INSIGHT:deep_dive]`

- **uw_screener directional aggregates:** bullish_premium $106,433,035 vs
  bearish_premium $97,757,295 → **net_flow +$8,675,740** (derived); call_premium
  $197.9M vs put_premium $35.2M; **put_call_ratio 0.346**; iv_rank 32.4;
  **implied_move $4.55 / 4.65%** (phase-9 N4 range). Reconciles exactly with phase-1
  aggregate and phase-0.5 `[CTX:]`.
- **uw_dark_pool:** avg_price **$99.35**, total_premium **$497.3M**, total_shares
  5,017,706, 2,119 trades — matches institutional-accumulation below and phase-2.
- ⚠️ **yahoo_fundamentals: error "HTTP 401"** — yfinance blocked, so PE / market cap /
  short% are unavailable here. Deferred to **phase-7b** (Finnhub) and **phase-7c/0**
  (`fz`: float 760.74M, short float 4.52%).

### Signal confluence `[INSIGHT:signal_confluence]`

Market-wide bullish list (min-score 1, top-20) is fully populated by names scoring
**5–6**; HOOD is **not present** → HOOD's bullish confluence score is **<5**. Top-20:
GEO, DOMO, SEZL, SPYI, ERII, LYFT, PEP, FNCL, UUP, OTLK, KLAR, AMBP, IBIT, STUB, TMC,
XLF, SLV, **AFRM**, ASR, AAPL. (Note: fintech peer **AFRM** clears ≥5; HOOD does not —
HOOD's flow is bullish but not elite-confluent.) HOOD also **absent from the bearish**
top-20 → not a strong bearish either.

### Conviction matrix `[INSIGHT:conviction_matrix]`

scenario **DIRECTIONAL_LONG**, confidence_pct **14**, explanation "Dark pool buying +
aggressive call purchases — institutional directional bet." options_flow: call_ask
159,825 / call_bid 153,374 (slight call-ask lean = bought), put_ask 49,230 / put_bid
53,772 (slight put-bid lean). dark_pool buy_ratio **0.63** (buy 3.16M vs sell 1.86M,
2,119 trades). Read: classified a directional long, but **14% confidence is low** —
the setup type is bullish, the strength is not.

### Price vs flow `[INSIGHT:price_vs_flow]`

divergence **false** — "Price and flow are aligned." flow_direction bullish,
net_premium_flow +$8.68M, price_change **+28.18%** ($76.55→$98.12), period_high
**$100.87**, period_low $73.18, PCR 0.346, iv_rank 32.4. No reversal signal; the recent
$100.87 high coincides with the phase-3 $100 wall / phase-4 gamma pin (overhead).

### Analyst vs flow `[INSIGHT:analyst_vs_flow]`

Tool returned **only the options_flow side** (bullish, net +$8.68M, PCR 0.346) — **no
analyst consensus** (the yfinance analyst leg is empty, consistent with the deep-dive
401). Analyst/Street view deferred to **phase-7b/7c** (Finnhub recommendations + `fz`).

### Institutional accumulation `[INSIGHT:institutional_accumulation]`

signal **"ACCUMULATION — dark pool buy volume significantly exceeds sell volume"**,
buy_sell_ratio **1.7**, buy_side 3,159,919 vs sell_side 1,857,787, total_dp_premium
**$497.3M**, total_dp_volume 5,017,706, price_30d **+28.18%**, **VWAP $99.12**,
avg_trade_price $99.35, 2,119 trades. VWAP/avg-trade *above* spot $98.12 → institutions
paid up. Strong confirmation of phase-2.

### Earnings play

Skipped — HOOD earnings **Aug 5** (phase-6), outside the 30-day window.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows |
|------------------|--------------------------|------|
| `uw insights deep-dive --symbol HOOD --date 2026-06-15` | net_flow +$8.68M; DP $497.3M; yahoo 401 ← `.uw_screener/.uw_dark_pool/.yahoo_fundamentals.error` | 1 |
| `uw insights signal-confluence --direction bullish --min-score 1 --top-n 20` | HOOD absent; cut ≥5 ← `[.results[].ticker]` | top-20 |
| `uw insights signal-confluence --direction bearish --min-score 1 --top-n 20` | HOOD absent | top-20 |
| `uw insights conviction-matrix --symbol HOOD --date 2026-06-15` | DIRECTIONAL_LONG, conf 14% ← `.scenario/.confidence_pct` | 1 |
| `uw insights price-vs-flow --symbol HOOD --lookback-days 30` | divergence false; +28.18% ← `.divergence/.price_change_pct` | 1 |
| `uw insights analyst-vs-flow --symbol HOOD` | flow bullish; no analyst leg ← `.options_flow` only | 1 |
| `uw insights institutional-accumulation --symbol HOOD` | ACCUMULATION, buy/sell 1.7 ← `.signal/.buy_sell_ratio` | 1 |

## Tool errors

- `uw insights deep-dive` → `yahoo_fundamentals: "yahoo quoteSummary HOOD: HTTP 401"`
  (yfinance blocked). uw_screener / dark_pool / oi blocks intact; fundamentals deferred
  to phase-7b/7c. `analyst-vs-flow` returned no analyst consensus (same yfinance gap).

## Cross-check vs phases 1–5

| UW insight | Phase agreement? | Notes |
|------------|------------------|-------|
| signal_confluence (<5, sub-elite) | **agrees** phase-5 | matches poor backtest (28.6%) + modest net; not elite |
| conviction_matrix (DIRECTIONAL_LONG, 14%) | **agrees** phases 1-2 | bullish-long type confirmed; low conf matches two-sided tape |
| institutional_accumulation (ACCUMULATION 1.7) | **agrees** phase-2 | $497.3M DP, VWAP $99.12 paid-up — direct confirmation |
| price_vs_flow (no divergence) | **agrees** phase-5 | price up + flow bullish aligned; period high $100.87 ≈ $100 wall |

No contradictions. The composite is internally consistent with phases 1–6: a real but
modest, capped, low-confidence bullish-long with confirmed accumulation.

## Verdict for downstream phases

- **UW composite bias:** **BULLISH / DIRECTIONAL_LONG** with **confirmed accumulation**
  and **no price-flow divergence** — qualitatively the full bullish stack — but at
  **LOW confidence** (conviction 14%, sub-5 confluence).
- **Conviction:** **3 / 5** — direction is clean and triple-confirmed; magnitude/edge is
  weak (backtest 28.6%, modest net +$8.68M, capped at $100).
- **Phase-9 baseline:** treat as a **bullish-long, small-size** baseline (cheap-vol →
  debit expression per phase-5), ceiling $100 (phase-3/4). Override only with specific
  contrary evidence from phases 7b/7c/8/8b. Do **not** upsize on the qualitative stack
  alone — the confidence layer is explicitly low.
- **Open questions:** Do phase-7b fundamentals (Finnhub) justify the accumulation
  (quality), or veto it? Does phase-7c short-interest/positioning add a squeeze angle or
  a crowded-long warning? Why does fintech peer AFRM clear ≥5 confluence while HOOD does
  not — is HOOD the laggard or the safer expression?
