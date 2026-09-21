# Phase 7 — UW Insights Confluence

**Ticker:** USAR (USA Rare Earth, Inc.)
**As-of date:** 2026-05-20 (effective UW data date: 2026-05-19)
**Generated:** 2026-05-20T11:15:00-04:00
**Upstream phases cited:** phase-0, phase-1, phase-2, phase-3, phase-4, phase-5, phase-6

## Summary

UW's composite tools produce a **soft DIRECTIONAL_LONG verdict at 14.1%
confidence** — agreeing with the dark-pool accumulation thesis but
flagging multiple cross-currents that keep conviction modest. The most
important new fact: **`insights_deep_dive` reports next earnings
2026-08-10**, confirming 5/22's IV backwardation is **NOT an event
window** but rather residual realized-vol pricing from the -29%
drawdown. **`insights_price_vs_flow` raises a DIVERGENCE flag** (price
+31.5% over 30d while flow net-bearish -$814k) — that divergence has
**already played out** in the 5/15→5/19 crash; the question phase 9
must answer is whether *this* divergence (DP buying / call buyers paying
ask, while puts also bid up) is the analog setup at the bottom rather
than the top. **Signal confluence: USAR makes neither the top-100
bullish nor the top-100 bearish list** — its mixed factor profile is
exactly that: mixed. The composite reads as "moderate-confidence
contrarian long" — best executed with defined risk per the phase-6
TRANSITIONAL regime guidance.

## Key signals

- **Conviction matrix: DIRECTIONAL_LONG, confidence 14.1%, explanation
  "Dark pool buying + aggressive call purchases — institutional
  directional bet"** [INSIGHT:conviction_matrix]
- **Institutional accumulation: ACCUMULATION, buy/sell ratio 1.65** —
  "dark pool buy volume significantly exceeds sell volume"; VWAP $20.07
  [INSIGHT:institutional_accumulation]
- **Next earnings 2026-08-10** (per `insights_deep_dive` screener) →
  5/22 backwardation is NOT earnings stress. 81 days out from earnings.
  [INSIGHT:deep_dive]
- **Price vs flow DIVERGENCE**: price +31.5% over 30d ($16.72 → $21.98
  reading, but actually closed $19.97 today), flow net -$813,975
  bearish. [INSIGHT:price_vs_flow]
- **Signal confluence: USAR NOT in top-100 bullish (min_score=1)** nor
  in **top-100 bearish (min_score=1)** — confirms mixed factor profile
  [INSIGHT:signal_confluence]
- **Implied 30-day move: 7.25% / $1.45** — far below recent realized
  swings; market pricing post-crash mean-reversion, not continued
  trending. [INSIGHT:deep_dive screener]
- **Call ask/bid: 10,331 / 9,618** (call buyers winning); **Put ask/bid:
  7,400 / 4,178 (put buyers winning 64%)** — both sides aggressive
  [INSIGHT:conviction_matrix]
- **Yahoo fundamentals: HTTP 401** — yfinance access failed, no
  cap/PE/short% in deep_dive output [INSIGHT:deep_dive tool_error]

## Detailed findings

### Deep dive snapshot

```
Symbol             USAR
Sector            (yfinance unavailable; phase-6 confirms Materials/Critical Minerals)
Next earnings     2026-08-10  ← 81 days away
PE / mkt cap      N/A (yfinance HTTP 401)
IV30d             98.95%
IV Rank           15.25  ← LOW (matches phase-5)
Implied 30d move  $1.45 (7.25%)
Volatility (realised) 117.79%
P/C ratio         0.67
Total OI          483,387
Call premium      $3,017,909
Put premium       $2,829,686
Bullish premium   $2,001,224
Bearish premium   $2,815,199
DP total premium  $18,618,110 (118 trades, 927,653 shares)
```

The IV vs realized vol mismatch is again striking: IV30d 98.95% vs
realized 117.79% — a **-18.8% volatility risk premium** in 30d window
terms (phase-5 reported -11.93% on a slightly different basis). Either
way: **vol is cheap, debit structures favored**.

### Signal confluence

- `direction=bullish, min_score=1, top_n=100`: **USAR NOT in result**.
- `direction=bearish, min_score=1, top_n=100`: **USAR NOT in result**.

USAR's factor profile (`bullish_flow`? no — net bearish -$814k.
`low_pcr`? PCR 0.67 not <0.50. `dp_accumulation`? yes (0.623).
`oi_building`? yes (both sides). `low_iv_cheap_options`? yes (IV rank
15). `high_iv_sell_premium`? no.) — gives it **3 bullish factors and
~2 bearish factors mid-strength**, net 0–1 score either direction. The
tool's lowest score cutoff is 1 and even that doesn't include USAR —
the **factor count truly is balanced**.

For sector context, the bullish-confluence top-100 contains several
adjacent names:
- **USAS** (related symbol — possibly US Antimony Mining or similar
  small-cap mining; score 5 with low_pcr 0.01, dp_accumulation,
  oi_building, low_iv).
- **NB** (Basic Materials, score 5).
- **PPTA** (Basic Materials, score 5).
- **APD** (Basic Materials Air Products, score 4).
- **NG** (Basic Materials Novagold, score 4).

→ The Basic Materials cohort has some bullish-leaning names today; USAR
is **not** the leader of its sector for institutional bullish flow on
this date.

### Conviction matrix

```
Scenario:   DIRECTIONAL_LONG
Confidence: 14.1%
Explanation:"Dark pool buying + aggressive call purchases —
             institutional directional bet."

Dark pool:
  buy_ratio = 0.623   (above 0.6 bull threshold)
  buy_vol   = 578,055
  sell_vol  = 349,598

Options flow:
  call_ask = 10,331   |  put_ask = 7,400
  call_bid =  9,618   |  put_bid = 4,178
  call_aggressor_ratio = 0.518  (mild call-buy)
  put_aggressor_ratio  = 0.639  (PUT BUYERS DOMINANT)
```

**Critical nuance**: while the matrix labels this DIRECTIONAL_LONG, the
**put_aggressor_ratio of 0.639 is HIGHER than the call_aggressor_ratio
of 0.518**. Put buyers are *more aggressive* than call buyers, even
though the absolute call-ask volume is larger. Reads as **both sides
paying up** — high-conviction two-way tape. The "directional long" label
is driven primarily by the dark-pool buy_ratio.

### Price vs flow — DIVERGENCE FLAG

```
period_low       $15.47
period_high      $28.69
price_start      $16.72  (30 sessions ago)
price_end        $21.98  (calc-window close)
price_change_pct +31.46%
flow_direction   bearish  (net -$813,975, PCR 0.67)
divergence       TRUE
divergence_signal "Price is up 31.5% but options flow is bearish"
```

The divergence tool measures **net price** over the lookback (which
ended ~5/15-ish given the $21.98 endpoint) vs current flow direction.
The **divergence already manifested** — the bearish flow that built
during the +31% ramp predicted (and is now mid-realizing) the
correction. The relevant question now is whether **today's combined
DP-bullish / flow-bearish split is the bottom-divergence analog**, but
that's not what this tool tests directly. Phase 9 must apply that
inference itself.

### Analyst vs flow

`insights_analyst_vs_flow` returned only the flow side (no Wall Street
consensus block; yfinance auth presumed). Flow side:
- Sentiment: **bearish** (net flow -$813k, bullish $2.0M vs bearish
  $2.8M premium).
- PCR 0.67.

**Phase-6 manual analyst sourcing** filled this gap: **Cantor Fitzgerald
OVERWEIGHT, PT $35 (raised from $30)**. So the proper analyst-vs-flow
read is:

> Wall Street: BULLISH ($35 PT, +75% from spot)
> Options tape: BEARISH (-$814k net)
> Verdict: ANALYST AND FLOW DISAGREE — flow is the contrarian leading
>          indicator after a -29% drawdown.

That misalignment is consistent with phase-1's "MIXED with bearish lean"
verdict and reinforces the contrarian-long reading at current spot.

### Institutional accumulation

```
Signal:           ACCUMULATION — dark pool buy volume significantly
                  exceeds sell volume
Buy/sell ratio:   1.65
Buy-side volume:  578,055
Sell-side volume: 349,598
Total premium:    $18,618,110
VWAP:             $20.07
Avg trade price:  $20.11
Price 30d Δ:      +31.46%

Top accumulation levels today:
  $19.99 — $805k premium (5 trades)
  $19.91 — $614k (4 trades)
  $19.90 — $586k (3 trades)
  $19.95 — $584k (3 trades)
  $20.32 — $542k (3 trades)
```

The institutional accumulation is **concentrated $19.90–$20.32**, not
spread across the day. This is consistent with phase 2's per-print
table (top buys at $19.46, $19.48, $19.95) and confirms: the floor
buyers stepped in around the $19.90–$20.00 zone. **$19.90 emerges as
the most defensible support level in this run** — five different prints
at or very near this price.

### Earnings play

**Not run.** `insights_deep_dive` confirmed earnings on 2026-08-10, 81
days away — far outside the 14-day `days_until_earnings` default. There
is no near-term earnings setup to evaluate.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `insights_deep_dive` | symbol=USAR, date=2026-05-19 | Earnings 2026-08-10; IV rank 15.3; implied move 7.25%; yfinance HTTP 401 |
| `insights_signal_confluence` | dir=bullish, min-score=1, top-n=100 | **USAR absent** from top-100 bullish |
| `insights_signal_confluence` | dir=bearish, min-score=1, top-n=100 | **USAR absent** from top-100 bearish |
| `insights_conviction_matrix` | symbol=USAR, date=2026-05-19 | **DIRECTIONAL_LONG, confidence 14.1%** |
| `insights_price_vs_flow` | symbol=USAR, lookback=30, date=2026-05-19 | **DIVERGENCE TRUE**: price +31.5% / flow -$814k |
| `insights_analyst_vs_flow` | symbol=USAR, date=2026-05-19 | Flow only (yfinance gap); bearish net |
| `insights_institutional_accumulation` | symbol=USAR, date=2026-05-19 | **ACCUMULATION**, B/S 1.65, VWAP $20.07 |

## Tool errors

- `insights_deep_dive`.yahoo_fundamentals: **HTTP 401** (yfinance auth
  block). Fundamentals (market cap, PE, short%, float) unavailable from
  this path. Phase-6 manual WebSearch partially covered.
- `insights_analyst_vs_flow`: silently omitted analyst block (likely
  same yfinance auth issue). Phase-6 Cantor Fitzgerald PT $35 was
  sourced manually.

## Cross-check vs phases 1–6

| UW insight | Phase agreement? | Notes |
|------------|------------------|-------|
| `conviction_matrix = DIRECTIONAL_LONG` | Phase 2 ✓, Phase 4 ✓ | Aligned with DP accumulation + dealer DEX +$411M buy hedging |
| `institutional_accumulation = ACCUMULATION` | Phase 2 ✓ | Identical underlying tape, slightly different aggregation |
| `price_vs_flow = DIVERGENCE` | Phase 1 ✓, Phase 5 ✓ | Bearish flow led the -29% crash; "divergence" now represents bottom-finding tension |
| `signal_confluence = USAR absent (both sides)` | Phase 1 ✓ | Mixed flow profile confirmed — neither side dominant enough to surface |
| `deep_dive.next_earnings = 2026-08-10` | Phase 4 ✓ | Confirms 5/22 backwardation is residual realized-vol, NOT earnings premium |
| Conviction confidence 14.1% | Phase 5 ✓ | Matches "no historical signal backtest" / small-N caveat |
| Analyst-vs-flow tool incomplete | Phase 6 manually filled | Cantor PT $35 vs options bearish flow = bottom-divergence candidate |

**No contradictions between UW composites and phases 1–6.** All
upstream phases were directionally consistent; the composite tools
sharpen the read but do not overturn any prior verdict.

## Verdict for downstream phases

- **UW composite bias:** **DIRECTIONAL_LONG (low confidence 14.1%) with
  bottom-divergence characteristics**. The matrix says long, the
  accumulation says long, the price-vs-flow says "bearish flow led the
  fall" (and is now exhausted at the floor), and signal-confluence says
  "mixed — don't size for asymmetric directional".
- **Conviction:** **3/5** — UW composites concur with the contrarian-
  long thesis but cap conviction by reporting low confidence and
  mixed-factor profile.
- **Phase 9 BASELINE recommendation from this phase**: long-bias
  defined-risk structure, sized at half the normal allocation per phase
  6 regime, with a put-spread or call-debit-spread structure to express
  it (matches phase 5's premium-buying VRP read).
- **Open questions:**
  - Is the dark-pool $19.90–$20.32 accumulation cluster the FLOOR or a
    BEAR TRAP before a leg lower? With confidence at 14.1% the answer
    is "don't bet the farm".
  - Does the **put_aggressor_ratio of 0.64** (puts more aggressive
    than calls) imply the institutions are accumulating stock AND
    buying protective puts (collar) — i.e., they don't trust the
    bounce either?
  - **Why is USAS (a different small-cap Basic Materials name) on the
    bullish signal_confluence list at score 5 today, while USAR isn't?**
    Sector-rotation signal worth tracking separately.
