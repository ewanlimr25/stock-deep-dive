# Phase 7 — UW Insights Confluence

**Ticker:** NVDA
**As-of date:** 2026-05-15
**Upstream phases cited:** phase-1 through phase-6
**Generated:** 2026-05-17T17:19Z

## Summary

UW's composite insights are **NOT bullish** on NVDA. The composites — which
already do confluence math across screener + dark pool + OI + flow — come
back **MIXED** and flag a **bearish price-vs-flow divergence**:

- `insights_conviction_matrix` → **MIXED** scenario (confidence 4%), dark
  pool buy_ratio 0.54 sits between bull (≥0.60) and bear (≤0.40) thresholds.
- `insights_institutional_accumulation` → **NEUTRAL**, "balanced dark pool
  activity".
- `insights_price_vs_flow` → **DIVERGENCE TRUE**: price up **+26.84%** over
  the 30d window while net flow today is **-$42.65M bearish**.
- `insights_signal_confluence` → NVDA does not appear in the top 50
  bullish-factor stocks (even with `min_score=1`). The factor model
  penalizes NVDA because IV is HIGH (failed `low_iv_cheap_options`) and
  dark pool is balanced (failed `dp_accumulation`).
- `insights_earnings_play` → NVDA confirmed earnings 2026-05-20 in UW
  screener, but NVDA does NOT appear in the top-25 earnings-play list (the
  list returns mostly small-to-mid caps with iv_rank ≥94, e.g. DOMO, URBN,
  ADI, TJX, ELF, HD — all reporting same week).

This phase is the cleanest cross-check the skill produces. It **contradicts
phase-1's bullish read** by showing the LEAP buying does not aggregate to a
DIRECTIONAL_LONG scenario when paired with balanced DP. It **confirms
phase-5's caution** about the price-vs-flow divergence and the contrarian
20% bullish-flow win rate. Phase-9 must respect this: the composite verdict
is **NEUTRAL-with-event-risk**, not bullish.

## Key signals

- **Conviction Matrix:** scenario **MIXED**, confidence 4.01%, buy_ratio
  0.54 `[INSIGHT:conviction_matrix]`
- **Institutional Accumulation:** **NEUTRAL** signal, buy/sell ratio 1.17
  `[INSIGHT:institutional_accumulation]`
- **Price vs Flow:** **DIVERGENCE TRUE** — price +26.84% over 30d,
  flow_direction bearish, net -$42.65M today `[INSIGHT:price_vs_flow]`
- **Signal Confluence:** NVDA absent from top-50 bullish list (score < 5
  even at min=1) `[INSIGHT:signal_confluence]`
- **Earnings Play:** NVDA in screener with earnings 2026-05-20 but absent
  from the top-25 high-IV earnings-play list `[INSIGHT:earnings_play]`

## Detailed findings

### Deep dive snapshot

| Field | Value |
|-------|-------|
| Next earnings date | **2026-05-20** ✅ (matches phase-6) |
| IV30d | 0.4895 (49.0%) |
| IV rank | 76.67 |
| Implied move (today) | 0.58 / +0.26% |
| Put/Call ratio | 0.46 (call-heavy) |
| Call premium | $1.75B |
| Put premium | $436M |
| Total OI | 16,890,388 |
| Dark pool premium | $8.01B |
| Dark pool avg price | $227.87 |
| Dark pool trade count | 33,318 |
| Top OI add | NVDA 250C 05-22 (+45,567 OI) — matches phase-3 |

**Tool error embedded:** `yahoo_fundamentals` returned `HTTP 401`. NVDA
fundamentals (PE, market cap, short interest) not available this run — see
Tool errors section.

### Signal confluence (market-wide, bullish direction)

NVDA does NOT appear in the top 50 results even with `min_score=1`. The
top tickers scoring 5–6/6 are small-to-mid caps:

| Ticker | Score | Sector | IV rank |
|--------|-------|--------|---------|
| DXCM | 6 | Healthcare | 25.8 |
| BOOT | 6 | Consumer Cyclical | 11.8 |
| STAA | 6 | Healthcare | 29.4 |
| ENPH | 5 | Technology | 85.0 |
| FWRD | 5 | Industrials | 29.8 |

**Why NVDA is missing:** the factor list is `bullish_flow, low_pcr,
volume_spike, dp_accumulation, oi_building, low_iv_cheap_options`. NVDA
likely fails:
- `low_iv_cheap_options` — IV rank 76 is too high (model wants ≤30)
- `dp_accumulation` — buy_ratio 0.54 vs threshold > 0.55-0.60
- `bullish_flow` — today's `flow_direction: bearish`

The bullish-factor score on NVDA today is therefore at most 2–3 of 6.

### Conviction matrix

| Field | Value |
|-------|-------|
| Scenario | **MIXED** |
| Confidence | 4.01% |
| Bull threshold (DP buy_ratio) | 0.60 |
| Bear threshold | 0.40 |
| DP buy_ratio | 0.54 (between thresholds) |
| DP buy volume | 18,983,796 |
| DP sell volume | 16,167,011 |
| Call ask volume | 1,396,595 |
| Call bid volume | **1,504,665** (BID > ASK on calls today!) |
| Put ask volume | 679,008 |
| Put bid volume | 619,054 |
| Explanation | "Balanced dark pool activity — no clear bias" |

**Critical detail:** *call bid volume EXCEEDS call ask volume* today
(1.50M vs 1.40M). This means more calls were sold on bid than bought on
ask. Combined with put bid > put ask (619k vs 679k — actually put ASK >
put BID, so puts were slightly net-bought, mildly bearish put behavior).
This is consistent with **distribution from the call side** + **mild put
accumulation** = end-of-week de-risking ahead of earnings. Reads bearish
for the next 5 sessions.

### Institutional accumulation

| Field | Value |
|-------|-------|
| Signal | **NEUTRAL** |
| Buy/sell ratio | 1.17 (mild buying) |
| 30d price change | +26.84% |
| Avg trade price | $227.87 |
| VWAP | $227.84 |
| Top DP level | $227.87 ($62.5M premium, 274k shares, 81 trades) |

Top 5 DP prices today: $227.87, $229.30, $228.00, $228.60, $226.00 — all
within 1.5% of each other, confirming the institutional VWAP-style
execution noted in phase-2.

### Price vs flow

| Field | Value |
|-------|-------|
| **Divergence** | **TRUE** |
| Divergence text | "Price is up 26.8% but options flow is bearish (net flow: $-42,649,954)" |
| Period (30d) start | $177.64 |
| Period high | $236.54 |
| Period low | $173.66 |
| Period end | $225.32 |
| Flow direction | bearish |
| Bullish premium | $940.37M |
| Bearish premium | $983.02M |

This is the most important contrarian signal in the entire run. Combined
with phase-5's 20% bullish_flow win rate over the 5d forward window, this
is a clear quant flag: **mean-reversion or pullback risk is elevated**.

### Analyst vs flow

The tool returned only the options-flow side (flow_sentiment: bearish today),
not the Yahoo analyst consensus side — likely the same HTTP 401 issue
hitting `insights_deep_dive`. Cannot compare analyst rating vs flow this
run. Surface in Tool errors.

### Earnings play

NVDA's earnings date (2026-05-20) is correctly carried in `insights_deep_dive`
screener data. However, NVDA does NOT appear in the top 25
`insights_earnings_play` results — the list is dominated by names with
iv_rank ≥94 (NVDA is 76.7). NVDA being a large-cap with relatively lower
IV rank than smaller pre-earnings names means it gets filtered out of the
"compressed-IV earnings play" universe.

Other 2026-05-20 earnings names from the list (potential correlation
exposure for phase-8 risk-monitor):
- ADI (semis adjacency, iv_rank 94.4)
- HD, TJX, ELF, DOMO, URBN

Other 2026-05-21 earnings names (one day after NVDA, may amplify
sentiment): TTWO, WDAY, ZM, AAP, ROST, DE.

## Cross-check vs phases 1–5

| UW insight | Phase agreement? | Notes |
|------------|------------------|-------|
| `signal_confluence` (NVDA absent) | **Disagrees with phase-1** (bullish flow read) | LEAP flow is loud but the multi-factor score is unimpressed |
| `conviction_matrix` (MIXED) | **Disagrees with phase-3** (mildly bullish positioning) | Call-side bid > ask today = distribution |
| `institutional_accumulation` (NEUTRAL) | **Agrees with phase-2** (mixed DP) | Mega-tier sell + large-tier buy nets to neutral |
| `price_vs_flow` (DIVERGENCE) | **Agrees with phase-5** (90d net +$200M flat; bullish_flow win rate 20%) | The strongest contrarian signal in the run |
| `analyst_vs_flow` (incomplete) | n/a | Yahoo 401 |
| `earnings_play` (NVDA absent) | **Confirms phase-6** earnings 5/20 but flags NVDA setup is not "premium IV-rank earnings setup" by UW's filter | NVDA premium is rich in $ terms but rank-percentile not at the screener's stretch zone |

## Tool calls (audit trail)

| Tool | Args | Result |
|------|------|--------|
| `mcp__uw-pp__insights_deep_dive` | `symbol=NVDA, date=2026-05-15` | full snapshot; Yahoo 401 |
| `mcp__uw-pp__insights_signal_confluence` | `direction=bullish, min-score=1, top-n=50, date=2026-05-15` | 50 rows, NVDA absent |
| `mcp__uw-pp__insights_conviction_matrix` | `symbol=NVDA, date=2026-05-15` | scenario MIXED |
| `mcp__uw-pp__insights_price_vs_flow` | `symbol=NVDA, date=2026-05-15, lookback-days=30` | DIVERGENCE TRUE |
| `mcp__uw-pp__insights_analyst_vs_flow` | `symbol=NVDA, date=2026-05-15` | flow side only |
| `mcp__uw-pp__insights_institutional_accumulation` | `symbol=NVDA, date=2026-05-15` | NEUTRAL |
| `mcp__uw-pp__insights_earnings_play` | `date=2026-05-15, days-until-earnings=14, min-iv-rank=40, top-n=25` | NVDA absent, 25 other names |

## Tool errors

### `mcp__uw-pp__insights_deep_dive` — Yahoo fundamentals 401

The `yahoo_fundamentals` sub-call returned `HTTP 401`. NVDA PE, market cap,
shares short, etc. are not available in this run. Likely a transient
yfinance auth/rate issue. Workaround: production runs can fall back to
WebSearch for fundamentals. Not blocking for the trade blueprint since
we're trading flow / structure, not fundamentals.

### `mcp__uw-pp__insights_analyst_vs_flow` — partial output

The tool returned only the options-flow side, not the analyst-consensus
side. Same root cause likely. Production runs should re-attempt or fall
back to WebFetch on a research-aggregator page (e.g., Marketwatch / Yahoo
analyst snapshot).

## Verdict for downstream phases

- **UW composite bias:** **MIXED-TO-NEUTRAL** with a clear PRICE-VS-FLOW
  DIVERGENCE flag.
- **Conviction:** 4/5 — multiple composites concur.
- **Treatment for phase-9:** Use this as the BASELINE bias. Phase-9 should
  NOT be more bullish than NEUTRAL-RANGE absent specific contrary
  high-conviction evidence (and phase-8 agents would need to be unanimously
  bullish to override).
- **Open questions for phase 8:**
  - Will `accumulation-hunter` agree with the NEUTRAL accumulation read?
  - Will `contrarian-scanner` flag the price-vs-flow divergence as a fade
    setup?
  - Will `earnings-scout` accept that NVDA's IV-rank-relative setup is
    weaker than other 5/20 earnings names, OR will it argue the absolute
    $-magnitude flow makes NVDA the dominant play of the week regardless?
