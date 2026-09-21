# Phase 7 — UW Insights Confluence

**Ticker:** AAPL
**As-of date:** 2026-05-27
**Generated:** 2026-05-28T03:30:00Z
**Upstream phases cited:** phase-0.5-context.md, phase-1-flow.md, phase-2-dark-pool.md, phase-5-historical.md

## Summary

UW's composite tools **agree with the upstream read and confirm it is
low-conviction**. The conviction-matrix labels AAPL **DIRECTIONAL_LONG but at only
17% confidence**; institutional-accumulation flags **ACCUMULATION** (DP buy/sell
1.77); price-vs-flow shows **no divergence** (bullish flow aligned with a +16.67%
30d move). The single most telling composite result: **AAPL does not appear in the
bullish signal-confluence top-50 even at min-score 1** — the factor it is missing
is `volume_spike` (volume is *below* average), exactly phase-0.5's
BUSY_NAME_NORMAL_DAY finding. The high-confluence names today (IOVA/TE/GGAL score
6, AMZN score 5) carry the full bullish stack; **AAPL is a mild lean, not a
high-confluence setup.** This is the BASELINE phase-9 should default to: *mildly
bullish, low confidence, range-bound* — overridden only by specific contrary evidence.

## Key signals

- conviction-matrix: **DIRECTIONAL_LONG, confidence 17%** — directional label,
  low confidence `[INSIGHT:conviction_matrix]`
- **AAPL absent from bullish signal-confluence top-50** (min-score 1); missing
  `volume_spike` → composite confluence unremarkable `[INSIGHT:signal_confluence]`
- institutional-accumulation: **ACCUMULATION**, buy/sell **1.77** (buy 4.41M /
  sell 2.49M sh), VWAP 311.11 `[INSIGHT:institutional_accumulation]`
- price-vs-flow: **no divergence** ("price and flow aligned"), flow bullish, but
  price already +16.67% over 30d (coincident, not leading) `[INSIGHT:price_vs_flow]`
- analyst-vs-flow returned **no data** (Yahoo) → defer analyst read to phase-7c `[INSIGHT:analyst_vs_flow]`

## Detailed findings

### Deep-dive snapshot (whole-tape `uw_screener`)

| Field | Value |
|-------|-------|
| call_premium / put_premium | $741.9M / $64.8M |
| **bullish_premium / bearish_premium** | **$197.95M / $180.54M** |
| **net_flow (bull−bear)** | **+$17.42M** |
| put_call_ratio | 0.373 |
| iv_rank / iv30d | 32.05 / 22.4% |
| **implied_move / implied_move_perc** | **$3.69 / 1.19%** (phase-9 N4 sizes to this) |
| total_open_interest | 4,871,089 |
| DP premium / shares | $2.146B / 6.90M sh |
| next_earnings | 2026-07-30 (>30d) |

Reconciles exactly with phase-1's aggregate (+$17.4M net) and phase-0.5's `[CTX:]`
(rank 9, implied move 1.19%). No new directional information — the whole-tape read
is stable across phases.

### Signal confluence

- **AAPL not in the bullish top-50** at `--min-score 1` → its bullish confluence
  score is below the cut. Today's leaders: **IOVA / TE / GGAL (score 6)** with the
  full stack [bullish_flow, low_pcr, volume_spike, dp_accumulation, oi_building,
  low_iv_cheap_options]; **AMZN / RDW (score 5)**.
- AAPL *has* several of those factors (low_pcr 0.373, oi_building 30d, low_iv 6th
  %ile, mild dp_accumulation) but **lacks `volume_spike`** (vol_x 0.82, below
  average) and its bullish_flow is weak (+$17.4M). → composite confluence is
  **mid/unremarkable**, not a standout. Confirms phase-0.5.

### Conviction matrix

- scenario **DIRECTIONAL_LONG**, **confidence_pct 17**. explanation: "Dark pool
  buying + aggressive call purchases — institutional directional bet." DP buy_ratio
  0.639; options call_ask 369,050 vs call_bid 326,709 (53% ask); put_ask 134,946 /
  put_bid 152,167. Thresholds bull 0.6 / bear 0.4. → **directional-long label, but
  the 17% confidence is the operative number** — the engine is not convinced.

### Price vs flow

- **divergence FALSE** — "Price and flow are aligned." flow bullish, net +$17.4M,
  **price_change +16.67%** (266.43→310.85, period 257.81–313.26). No reversal
  signal, but the bullish flow is **coincident with a stretched move**, not leading
  a fresh one — corroborates phase-5's overbought/extended flag.

### Analyst vs flow

- Returned only `{symbol: AAPL}` — **no consensus/analyst payload** (yfinance, same
  Yahoo 401 seen in deep-dive). Not usable; phase-7c will source analyst
  revisions/PTs from Finnhub/`fz`/WebSearch.

### Institutional accumulation

- signal **ACCUMULATION** — "dark pool buy volume significantly exceeds sell
  volume." buy_sell_ratio **1.77** (buy 4.41M / sell 2.49M sh), total DP $2.146B,
  VWAP 311.11, price_30d +16.67%. **Caveat:** this uses all-day buy/sell and does
  *not* capture phase-2's qualifiers (the buy skew is closing-cross-concentrated,
  AAPL ranks only 14th in DP, blocks are trivial % of float). **Phase-2's qualified
  read is more decision-relevant than this clean label.**

### Earnings play

Out of window — AAPL earnings 2026-07-30 (>30d); AAPL absent from the 30-day
earnings-play list (expected). Skipped.

## Tool calls (audit trail)

| Command | Result summary |
|---------|----------------|
| `uw insights deep-dive --symbol AAPL` | whole-tape aggregate (net +$17.4M); Yahoo fundamentals 401 |
| `uw insights conviction-matrix --symbol AAPL` | DIRECTIONAL_LONG, confidence 17% |
| `uw insights signal-confluence --direction bullish --min-score 1` | **AAPL absent from top-50** |
| `uw insights price-vs-flow --lookback 30` | no divergence, flow bullish, +16.67% |
| `uw insights analyst-vs-flow --symbol AAPL` | **no data (Yahoo)** |
| `uw insights institutional-accumulation --symbol AAPL` | ACCUMULATION, buy/sell 1.77 |
| `uw insights earnings-play --days-until-earnings 30` | AAPL out of window (earnings 7/30) |

## Tool errors

- `uw insights analyst-vs-flow --symbol AAPL` → empty payload (`{symbol: AAPL}`),
  Yahoo-sourced consensus unavailable (HTTP 401 seen in deep-dive). Not fatal —
  analyst data deferred to phase-7c (Finnhub/`fz`/WebSearch).

## Cross-check vs phases 1–5

| UW insight | Phase agreement? | Notes |
|------------|------------------|-------|
| signal_confluence (AAPL absent) | **AGREE** w/ phases 0.5, 1, 3 | low/mid confluence; missing volume_spike = BUSY_NAME_NORMAL_DAY |
| conviction_matrix (DIR_LONG @17%) | **AGREE** w/ phase-1 | direction matches, 17% confidence = low conviction |
| institutional_accumulation (ACCUM) | **partial** w/ phase-2 | sign agrees; composite omits phase-2's closing-cross/rank-14/float caveats |
| price_vs_flow (no divergence) | **AGREE** w/ phase-5 | aligned but stretched (+16.67%) — coincident not leading |

## Verdict for downstream

- **UW composite bias:** **mildly bullish / DIRECTIONAL_LONG at LOW confidence
  (17%)** — and explicitly *not* a high-confluence name (absent from bull top-50).
- **Conviction:** **2/5.**
- **Phase-9 baseline:** treat this as *mildly bullish, low confidence, range-bound*
  and override only with specific contrary evidence. The composite is internally
  consistent with phases 0.5–6 — the run is coherent, not conflicted, and the
  coherent message is **"weak signal."**
- **Open questions:**
  - Does fundamentals (phase-7b) justify the +24% run, or is it momentum on cheap
    vol (which would make the extension more fragile)?
  - Does sentiment/positioning (phase-7c) confirm the crowd is already long
    (overbought + complacent skew) → fade risk?
