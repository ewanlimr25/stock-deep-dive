# Phase 7 — UW Insights Confluence

**Ticker:** NBIS (Nebius Group NV)
**As-of date:** 2026-06-17
**Generated:** 2026-06-18T00:48:18Z
**Upstream phases cited:** phase-0.5-context.md, phase-1-flow.md, phase-2-dark-pool.md, phase-5-historical.md, phase-6-macro.md

## Summary

UW's own composite engine reads NBIS as a **MIXED, low-conviction setup with a mild bullish flow
tilt** — it does NOT corroborate a high-conviction directional trade, which is consistent with every
upstream phase. **NBIS is absent from the signal-confluence list in BOTH directions even at min-score
1** (confluence < 1 each way), the **conviction-matrix returns scenario MIXED at just 2.7% confidence**
(dark-pool buy_ratio 0.473, both call and put sides bought), and **institutional-accumulation = NEUTRAL**
(buy/sell 0.9, balanced). `price-vs-flow` shows no divergence ("aligned", bullish) but the alignment is
weak — net premium flow is only +$18.0M against a +43.99% 30-day price move, i.e. the flow never
confirmed the magnitude of the rally. `analyst-vs-flow` returns only the flow side (analyst block
empty — defer to fz target $255.29 < spot, and phase-7b). **Baseline for phase-9: MIXED / mild-bullish,
LOW conviction** — the composite says "lots of two-sided activity, no clean edge," which phase-9 should
treat as the anchor and only override with specific contrary evidence.

## Key signals

- **signal-confluence: NBIS not in bullish OR bearish list (score <1 both)** — no composite directional edge. [INSIGHT:signal_confluence]
- **conviction-matrix: MIXED, 2.7% confidence**; dark_pool 0.473 (balanced); call & put both net-bought. [INSIGHT:conviction_matrix]
- **institutional-accumulation: NEUTRAL** (buy/sell 0.9, vwap $283.42 > $280.91 close). [INSIGHT:institutional_accumulation]
- **price-vs-flow: aligned (no divergence), bullish — but flow +$18M vs +44% price (weak confirm).** [INSIGHT:price_vs_flow]
- **Deep-dive whole-tape: net_flow +$18.0M, call/put premium $514M/$189M, implied move ±4.86%, IV rank 91.3.** [INSIGHT:deep_dive]

## Detailed findings

### Deep dive snapshot (whole-tape aggregates) [INSIGHT:deep_dive]

| Metric | Value |
|--------|-------|
| bullish_premium / bearish_premium | $329.13M / $311.13M → **derived net_flow +$18.01M** |
| call_premium / put_premium | $514.13M / $189.44M (2.7×) |
| put_call_ratio | 0.846 |
| implied_move / implied_move_perc | 13.66 pts / **4.86%** (phase-9 N4 sizes to this) |
| iv_rank / iv30d | 91.3 / 113.1% |
| total_open_interest | 1,130,434 |
| next_earnings_date | 2026-08-06 (out of 30d window → earnings-play skipped) |

Reconciles exactly with phase-1 (net +$18.0M) and phase-0.5's [CTX:] rank (#20 net-dir, 99.7 pctile
total premium). Yahoo fundamentals block in deep-dive errored (HTTP 401, logged phase-0.5) — fundamentals via phase-7b/fz.

### Signal confluence [INSIGHT:signal_confluence]

Market-wide, `--min-score 1`, both directions: **NBIS appears in NEITHER list.** Its bullish AND
bearish confluence scores are both below 1 — the engine finds no stacked directional factor set. For a
name at the 99.7th premium percentile, the *absence* from the confluence list is itself the signal:
the activity is two-sided, not confluent. (Heuristic: confluence ≥5 is high-conviction; NBIS <1.)

### Conviction matrix [INSIGHT:conviction_matrix]

scenario **MIXED**, confidence_pct **2.7**, explanation "Balanced dark pool activity — no clear bias."
dark_pool buy_ratio 0.473 (thresholds bull 0.6 / bear 0.4 → middle = MIXED). options_flow: call_ask
70,194 vs call_bid 59,380 (net call buying); put_ask 61,003 vs put_bid 50,239 (net put buying) — **both
sides net-bought**, the textbook two-sided tape. NOT DIRECTIONAL_LONG, not HEDGED_LONG — genuinely MIXED.

### Price vs flow [INSIGHT:price_vs_flow]

divergence **false**, "Price and flow are aligned", flow_direction bullish. price_start 195.09 →
price_end 280.91 (**+43.99%**), period_high **297.93**, period_low 172.25, net_premium_flow +$18.0M.
Read: no reversal *signal*, but "aligned" is weak — a +44% price move on a +$18M net flow means flow
lagged price; the rally was momentum/index-driven, not flow-led (matches phase-6 inclusion catalyst).
**$297.93 is the recent intraday high** — a key resistance just under the $300 call wall (phase-3).

### Analyst vs flow [INSIGHT:analyst_vs_flow]

Returns flow only (flow_sentiment bullish, net +$18.0M); **analyst consensus block empty** (yfinance
thin, expected per tool docs). Defer to fz: **Target Price $255.29 < spot $280.91 — price is ABOVE
consensus target** (phase-0), and to phase-7b's analyst cross-source. The options tape is more bullish
than Wall Street's price target, which is *below* the market.

### Institutional accumulation [INSIGHT:institutional_accumulation]

signal **"NEUTRAL — balanced dark pool activity"**; buy_sell_ratio 0.9 (buy 2,354,496 / sell 2,626,604
→ buy fraction 0.473); vwap **$283.42**, avg_trade_price $284.02 (both above the $280.91 close); total
dp premium $1.412B. top_price_levels cluster $280.91→$286. Confirms phase-2: blended dark pool is
balanced; the mega-tier 0.064 sell skew (phase-2) is masked inside this all-tier 0.473 blend.

### Earnings play

**Skipped** — next earnings 2026-08-06 is >30d out (phase-6 calendar).

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← path | Rows |
|------------------|--------------------|------|
| `uw insights signal-confluence --direction bullish --min-score 1 --top-n 50` | NBIS absent ← `index("NBIS")` | 50 |
| `uw insights signal-confluence --direction bearish --min-score 1 --top-n 50` | NBIS absent ← `index("NBIS")` | 50 |
| `uw insights conviction-matrix --symbol NBIS --date 2026-06-17` | MIXED, conf 2.7%, dp 0.473 ← `.scenario/.confidence_pct` | 1 |
| `uw insights price-vs-flow --symbol NBIS --lookback-days 30` | divergence false, +43.99%, high 297.93 ← `.divergence/.period_high` | 1 |
| `uw insights analyst-vs-flow --symbol NBIS` | flow bullish +$18M; analyst block empty ← `.options_flow` | 1 |
| `uw insights institutional-accumulation --symbol NBIS` | NEUTRAL, buy/sell 0.9, vwap 283.42 ← `.signal/.buy_sell_ratio` | 1 |
| `uw insights deep-dive --symbol NBIS --date 2026-06-17` | net +$18.0M, impl move 4.86%, IV rank 91.3 ← `.uw_screener` | 1 |

## Tool errors

None (deep-dive `.yahoo_fundamentals` 401 already logged phase-0.5; analyst-vs-flow empty analyst block
is expected behavior, not an error).

## Cross-check vs phases 1–5

| UW insight | Phase agreement? | Notes |
|------------|------------------|-------|
| signal_confluence (absent both dirs) | **agrees** phases 1/5 | Confirms phase-1's *qualified* bullish (two-sided) and phase-5's edge-negative read; no clean edge. |
| conviction_matrix (MIXED 2.7%) | **agrees** phase 2 | Both see balanced; phase-2's mega-tier distribution is a finer cut inside the 0.473 blend. |
| institutional_accumulation (NEUTRAL) | **agrees** phase 2 | Blended dark pool balanced; phase-2 leaned mild-distribution at mega tier only. |
| price_vs_flow (aligned bullish) | **partial** vs phase 5 | "Aligned" but weak (flow lagged price); phase-5 says the bullish signal is edge-negative (37.5% win). |

## Verdict for downstream phases

- **UW composite bias:** **MIXED with a mild bullish flow tilt — LOW conviction.** The engine
  explicitly declines to flag NBIS as confluent in either direction (score <1) and rates the scenario
  MIXED at 2.7% confidence.
- **Conviction:** **2/5.** The composite's own confidence is 2.7%; institutional signal NEUTRAL; no
  divergence but weak alignment. This is a low-edge, two-sided name with an external (index) catalyst,
  not an instrument-confirmed directional setup.
- **Phase-9 guidance:** treat **MIXED / mild-bullish / low-conviction** as the BASELINE. Override toward
  bullish ONLY on the specific external catalyst (Nasdaq-100 inclusion, phase-6) and the persistent
  sweep campaign (phase-1) — and respect the contrary stack (phase-2 mega distribution, phase-5
  edge-negative + parabolic extension, phase-6 hawkish macro). Do not size as if confluence were high.
- **Open questions:** Does the external Jun-22 inclusion catalyst justify overriding a MIXED composite
  baseline (phase-8/8b)? Do fundamentals justify price > analyst target at P/E 93.7 (phase-7b)? Is the
  21.9% short float a squeeze fuel into inclusion or a smart fade (phase-7c)?
