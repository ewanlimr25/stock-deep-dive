# Phase 7b — Deep Fundamentals & Quality Veto (FINNHUB)

**Ticker:** NOW
**As-of date:** 2026-05-27
**Generated:** 2026-05-28T13:06:00Z
**Upstream phases cited:** phase-5-historical.md, phase-6-macro.md, phase-7-insights.md

## Summary

**The underlying business is high-quality and growing — fundamentals CONFIRM,
not contradict, the bullish flow.** NOW carries **76.6% gross margin, +21.7% YoY
revenue growth, +14.2% EPS growth, very low leverage (D/E 0.115), ROE 15%** — a
premium SaaS compounder. The −51% drawdown (phase-5) is a **multiple de-rating of
a still-growing business**, not fundamental deterioration: trailing PE 61 / PEG 4.2
looks rich, but **forward PE is ~20 with +21.8% expected EPS growth → forward PEG
≈1.0**, and the **Street is at strong-buy (recom 1.35) with a $140.63 target
(+37.7%)**. Beat-rate is 75% (3/4) though **surprise magnitude is decelerating**
(+13.4%→+11.8%→+3.2%→−0.3% latest). NOW is the **worst YTD performer of its
software peer group** — a quality laggard, i.e. a mean-reversion candidate.
Contradictions vs the bullish bias: **0 → tier_adjustment CONFIRM** (no-op; no size
cut). Insider data is absent (neutral, not bullish).

## Key signals

- **Quality intact:** gross margin **76.6%**, rev growth **+21.7%**, EPS growth +14.2%, D/E 0.115 `[FUND:margins]` `[FUND:growth]`
- **Forward valuation reasonable:** fwd PE **20.2**, EPS next-Y **+21.8%** → fwd PEG ≈1.0 (vs trailing PEG 4.2) `[FUND:fwd_pe fz]`
- **Street strong-buy:** recom **1.35**, target **$140.63 (+37.7%)**, inst-own 86.4% `[FUND:recom fz]`
- **Beat-rate 75%** but **decelerating** (+13.4→+11.8→+3.2→−0.3%); latest Q a thin miss `[FUND:earnings]`
- **Worst-in-group YTD** (−33% vs MSFT −15%, PANW +35%, FTNT +61%) — quality laggard `[FUND:peer_pe fz]`

## Detailed findings

### Valuation `[FUND:metric]` `[FUND:fwd_pe fz]`

| metric | NOW | read |
|--------|-----|------|
| PE (TTM / norm) | 61.0 / 61.3 | rich trailing |
| **Forward PE** | **20.2** (fz) | reasonable for a 21% grower |
| PEG (TTM / fwd) | 4.21 / **~1.0** | forward-fair |
| P/B · P/S | 12.3 · 7.7 | premium |
| beta | 0.84 | below-market |

The trailing-vs-forward gap is the crux: the de-rating has pulled the **forward**
multiple to a level (PEG ~1) that is *not* expensive for the growth. Value-trap
risk is low (business is growing); residual risk is further multiple compression
if rates stay high (phase-6 sticky core CPI).

### Growth & margins `[FUND:growth]` `[FUND:margins]`

Revenue +21.7% YoY, EPS +14.2% YoY, gross margin 76.6%, operating margin 13.4%,
net margin 12.6%, ROE 15.0%, ROA 7.5%. **Strong, durable SaaS economics — this
axis CONFIRMS the bullish thesis.**

### Earnings-surprise history (≤ as-of, look-ahead filtered) `[FUND:earnings]`

| Period | Actual EPS | Estimate | Surprise % |
|--------|-----------:|---------:|-----------:|
| 2026-03-31 | 0.97 | 0.973 | **−0.34%** (miss) |
| 2025-12-31 | 0.92 | 0.892 | +3.17% |
| 2025-09-30 | 0.964 | 0.862 | +11.85% |
| 2025-06-30 | 0.818 | 0.721 | +13.44% |

Beat-rate **75% (3/4)**, but the **surprise magnitude is clearly decelerating**
and the latest quarter (Q1-26) was an in-line/thin miss. This is the single
fundamental caution — and a plausible *cause* of the multiple de-rating. EPS levels
still grinding higher. Net: the axis **confirms** (forward consensus strong) with a
deceleration flag carried as a key risk.

### Forward consensus `[FUND:fwd_pe fz]` `[FUND:recom fz]`

- Finnhub `eps-estimate` / `revenue-estimate` returned **null** (paid-tier on this
  key) → used `fz` forward fields instead: **EPS next-Y +21.8%, EPS next-5Y +20.9%**,
  forward PE 20.2, **recom 1.35 (strong-buy)**, target **$140.63** (+37.7% vs $102.12).
- Direction: **firmly positive** — confirms.

### Balance sheet / cash flow

- `financials-reported` not pulled (commonly paid-tier); proxied from metrics:
  **D/E 0.115** (very low leverage), current ratio 1.00 (adequate), ROE 15% — a
  clean balance sheet. No liquidity/solvency red flag.

### Insider signal `[FUND:insider_cluster fz]`

- Finnhub MSPR: **empty** (no data on this key — consistent with the known
  MSPR-empty limitation).
- `fz insider-clusters` (30d, ≥2): **no buy-cluster AND no sell-cluster** for NOW.
- → **Insider axis = no activity (neutral).** Per rubric, absence is a weak
  signal — *not* treated as bullish, *not* a contradiction.

### Peers — relative value `[FUND:peer_pe fz]`

| Ticker | P/E | Perf YTD |
|--------|----:|---------:|
| **NOW** | **60.8** | **−33.3%** |
| MSFT | 24.6 | −14.7% |
| ORCL | 34.3 | −2.0% |
| FTNT | 49.4 | +61.1% |
| PANW | 137.5 | +34.9% |
| CRWD | NM | +37.7% |
| ZS | NM | −43.8% |
| S | NM | +19.7% |

(`fz --tickers` returns the flat 9-field overview only — fwd PE / SI / float not
available in this view; peer list from Finnhub `/peers`.) NOW's PE sits mid-pack
(above MSFT/ORCL, below PANW), but its **−33% YTD is second-worst in the group** —
a clear **quality laggard**. Two reads: relative weakness (bear) vs catch-up /
mean-reversion candidate (bull). Neither is a fundamental contradiction.

## Red flags

1. **Decelerating earnings-surprise magnitude** + latest thin miss — beat cadence fading.
2. **Rich trailing multiple** (PE 61) — vulnerable to further compression if rates/growth disappoint.
3. **Worst-in-class YTD** — relative-strength laggard; sector outflow (phase-6) could keep pressure on.

## Tool / source calls (audit)

| Endpoint | Result |
|----------|--------|
| `/stock/metric` | ok — full metrics |
| `/stock/earnings` (limit 8) | ok — 4 quarters returned, all ≤ as-of |
| `/stock/eps-estimate` · `/revenue-estimate` | **null (paid-tier)** → fz forward used |
| `/stock/peers` | ok — 10 peers |
| `/stock/insider-sentiment` (MSPR) | **empty** |
| `fz insider-clusters` (buy & sell) | ok — no NOW cluster |
| `fz quote` (recom/target/fwd) · `fz --tickers` (peers) | ok |

## Tool / source errors

- Finnhub `eps-estimate` & `revenue-estimate`: returned `null` data (paid-tier on
  this key) — substituted `fz` forward EPS/growth/target. Not fatal.
- Finnhub MSPR: empty (known limitation). Insider read via `fz` clusters (also none).

## Verdict for downstream — quality gate

```
fundamental_signal:  BULLISH
tier_adjustment:     CONFIRM
contradiction_count: 0      # earnings_trend=confirm, insider=neutral/no-data, growth/margins=confirm
insider_cluster:     {present: n, distinct_buyers: n/a, side: n/a}
key_risks:
  - Decelerating earnings-surprise magnitude (+13.4→+11.8→+3.2→−0.3%); latest Q a thin miss.
  - Rich trailing multiple (PE 61) → further multiple-compression risk if rates stay high.
  - Worst-in-class YTD (−33%) → quality laggard; sector outflow (phase-6) may persist.
```

**Gate effect:** CONFIRM = **no-op** (no size cut). Fundamentals support reading the
bullish flow as **genuine positioning in a de-rated quality compounder**, not
distribution into a deteriorating business. Note: phase-7b can only confirm or
cut — it does **not** raise conviction; the upside is already partly in the flow.
The forward-fair valuation + strong-buy Street view simply *remove* the
fundamental veto that a deteriorating name would have triggered.
