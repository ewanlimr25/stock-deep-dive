# Phase 7b — Deep Fundamentals & Quality Veto (FINNHUB)

**Ticker:** MARA
**As-of date:** 2026-06-18 (look-ahead guard applied: all periods filtered ≤ as-of)
**Generated:** 2026-06-19
**Upstream phases cited:** phase-6-macro.md (Q1 weakness, BTC-NAV), phase-7-insights.md (analyst-vs-flow split)

## Summary

The underlying business is **structurally weak, which CONFIRMS the capped/mild-bearish
flow thesis** (and would **VETO** any bullish directional long). MARA has **missed 3
straight quarters** (Q1'26 −50.7%, Q4'25 −3426%, Q3'25 −31.5%; only 1 beat in 4 =
**25% beat-rate**, and that beat was a BTC mark-to-market windfall), runs **ROE −52% /
net margin −235%** (GAAP losses dominated by BTC fair-value markdowns + heavy share
dilution), and shows **persistent insider net-selling (MSPR −100 in 13 of the last 16
months)**. Within the miner complex it is a **relative laggard** (YTD +58% vs RIOT
+122% / HUT +171% / WULF +152%) with the **deepest per-share loss (EPS −5.72)**. The
one bullish cross-source — Street **Recom 2.0 (Buy), target $17.70 (+24%)** — is a
longer-horizon BTC-bull view that the near-term flow, structure, and fundamentals all
contradict. Mitigants: **strong liquidity (current ratio 4.9)** and large **BTC-NAV
(₿36,303 ≈ $2.4B vs $5.4B mcap)** — not a solvency story, a BTC-beta story.

## Key signals

- **3 consecutive earnings misses**, 25% beat-rate (4q) `[FUND:earnings_surprise]`.
- **ROE −52.1%, net margin −234.8%** (BTC-markdown / dilution losses) `[FUND:roeTTM]`.
- **MSPR −100 in 13/16 months** — sustained insider net-selling `[FUND:mspr]`.
- **Relative miner laggard**: YTD +58.4% vs RIOT +121.8% / HUT +170.9%; worst EPS
  (−5.72) of the pure miners `[FUND:peer_pe fz]`.
- **Street Buy, target $17.70 (+24%)** — the lone bull, contradicted near-term
  `[FUND:recom fz]`.

## Detailed findings

### Valuation

- P/E **n/a** (loss-making), P/B **1.38**, P/S **6.22** (rich for a hardware-heavy
  miner), PEG n/a. Beta **5.41** (extreme — crypto leverage). 52wH $23.45 / 52wL $6.66.
- The whole miner complex is unprofitable (P/E "−" for RIOT/CLSK/HUT/CIFR/WULF/MSTR;
  only IREN positive at 206× P/E) → MARA's lack of earnings multiple is **sector-normal**,
  not idiosyncratic. P/S 6.2× is the relevant gauge → not cheap.

### Growth profile

- Revenue growth TTM YoY **+23.1%** (`metric`), BUT the **latest quarter decelerated**
  (Q1'26 rev $174.6M vs $213.9M YoY = **−18%**, phase-6) — top-line momentum is rolling
  over even as the trailing-twelve looks up. EPS growth n/a (negative). **Margins deeply
  negative** (net −234.8%, ROE −52.1%) — dominated by BTC fair-value markdowns, which
  swing with BTC price (a soft-BTC quarter → another markdown).

### Earnings-surprise history (look-ahead-filtered ≤ as-of)

| Period | Actual EPS | Estimate | Surprise % |
|--------|-----------:|---------:|-----------:|
| 2026-03-31 | −3.31 | −2.20 | **−50.7%** (miss) |
| 2025-12-31 | −4.52 | −0.13 | **−3425.7%** (huge miss) |
| 2025-09-30 | 0.31 | 0.45 | −31.5% (miss) |
| 2025-06-30 | 1.89 | 0.63 | +200.3% (beat — BTC mark-up) |

**Beat-rate 1/4 (25%); 3 consecutive misses.** The earnings_trend axis is clearly
**negative** — and 8/4 is a downside earnings binary (phase-6 calendar).

### Forward consensus

- Finnhub `eps-estimate` / `revenue-estimate` returned **no rows dated > as-of**
  (free-tier coverage gap for MARA) → forward consensus **unavailable** from Finnhub.
  Cross-source: `fz` Street **target $17.70**, Recom **2.0 (Buy)** — see Insider/Recom.

### Balance-sheet & cash-flow health

- `financials-reported` not pulled in depth (free-tier proxy via `metric`):
  **debt/equity 0.59** (moderate), **current ratio 4.94** (strong liquidity — large
  cash + BTC). **Not distressed.** The losses are non-cash BTC markdowns + dilution,
  not a liquidity crisis. BTC-NAV ₿36,303 ≈ $2.4B underpins ~44% of the $5.4B mcap.

### Insider signal (MSPR, trailing 12–16 months)

| Window | MSPR pattern |
|--------|--------------|
| 2025-04 → 2026-01 | **−100 every month** (net selling / no buying) |
| 2026-02 | **+81.2** (one anomalous buy month, +3.07M sh change) |
| 2026-03 → 2026-05 | **−100, −100, −100** (back to net selling) |

Dominant signal: **persistent insider net-selling (−100)**, the maximum bearish
reading, sustained → **no insider support** beneath the stock. `fz` insider-cluster
check: **no MARA buy-cluster AND no sell-cluster** in the last 30 days (≥2 distinct
officers) → nothing fresh to sharpen, MSPR stands alone. `[FUND:insider_cluster fz]`

### Peers — relative-value comparison (real miner complex; Finnhub list was miscategorized)

> Finnhub `/peers` returned SaaS names (DBX, PLTR, PEGA, APPF, PCOR…) — a
> mis-categorization (MARA's "Capital Markets" tag + AI-pivot). Used the actual
> bitcoin-miner / BTC-proxy complex via `fz` instead.

| Ticker | P/E | Mkt Cap | Perf YTD | EPS (ttm) |
|--------|----:|--------:|---------:|----------:|
| **MARA** | — | $5.42B | **+58.4%** | **−5.72** |
| RIOT | — | $10.63B | +121.8% | −2.46 |
| CLSK | — | $4.42B | +70.4% | −2.10 |
| HUT | — | $14.01B | +170.9% | −2.91 |
| CIFR | — | $11.94B | +97.7% | −2.23 |
| WULF | — | $14.36B | +152.2% | −2.51 |
| IREN | 206× | $21.40B | +58.8% | +0.29 |
| MSTR | — | $39.44B | −25.9% | −40.16 |

**MARA places mid-to-bottom of the miner pack** on YTD (only IREN comparable, MSTR
worse) with the **deepest per-share loss** of the pure miners. It is *not* the upside
leader of the complex — consistent with the capped flow read.

## Red flags

- **Serial earnings misses** (3 straight) + huge GAAP losses (BTC markdowns + dilution).
- **Persistent insider net-selling** (MSPR −100 most months).
- **Latest-quarter revenue −18% YoY** (top-line rolling over) despite +23% TTM.
- **Relative peer laggard** with the deepest per-share loss.
- (Mitigants: current ratio 4.9, BTC-NAV optionality, sector-normal losslessness.)

## Tool / source calls (audit trail)

| Endpoint / cmd | Key value(s) ← path | Status |
|----------------|---------------------|--------|
| `finnhub /stock/metric?metric=all` | ROE −52.1, netMargin −234.8, P/S 6.22, curr 4.94, β 5.41 ← `.metric` | ok |
| `finnhub /stock/earnings?limit=8` | 3 misses, 25% beat ← `.[].surprisePercent` | ok (4 rows) |
| `finnhub /stock/eps-estimate` / `revenue-estimate` | no rows > as-of ← `.data[]\|select(.period>asof)` | empty (coverage gap) |
| `finnhub /stock/peers` | SaaS list — miscategorized ← `.` | ok but unusable |
| `finnhub /stock/insider-sentiment` | MSPR −100 ×13/16 mo ← `.data[].mspr` | ok |
| `fz quote --tickers MARA,RIOT,CLSK,HUT,CIFR,WULF,IREN,MSTR` | MARA YTD +58% laggard ← `.[].Perf YTD` | ok |
| `fz quote MARA` recom/target | Recom 2.0, target $17.70 ← `.fundamentals.*` | ok |
| `fz insider-clusters --side buy\|sell` | no MARA cluster ← `select(.Ticker=="MARA")` | ok (none) |

## Tool / source errors

(none material — Finnhub key present, US ticker; forward-estimate endpoints returned
empty for MARA = free-tier coverage gap, not a 403. `financials-reported` not deep-pulled
— proxied from `metric` per the rubric.)

## Verdict for downstream — quality gate

```
fundamental_signal:  BEARISH        # serial misses, deep neg margins, insider-sold, peer laggard
tier_adjustment:     CONFIRM        # fundamentals AGREE with the capped/mild-bearish flow bias → no cut
contradiction_count: 0             # vs the (mild-bearish/capped) flow bias; 0 axes contradict it
                                    # ⚠ vs a BULLISH long thesis this would be VETO (all 3 axes contradict a long)
insider_cluster:     {present: n, distinct_buyers: n/a, side: n/a}   # fz; MSPR -100 stands alone
key_risks:
  - Serial earnings misses (3 straight) + 8/4 earnings is a downside BTC-markdown binary
  - Persistent insider net-selling (MSPR -100 most months) — no support under the stock
  - Relative miner laggard (YTD +58% vs RIOT +122%/HUT +171%); deepest per-share loss (mitigant: current ratio 4.9, BTC-NAV)
```

**Net:** the business quality **does not contradict** the capped/range/mild-bearish
read — it **reinforces** it (CONFIRM, no size cut) — while **explicitly vetoing any
bullish directional long** (the Street $17.70 target is unsupported by near-term flow,
structure, fundamentals, or insiders). Phase-9 should treat the upside as capped on
*fundamental* grounds too, and weight any range/credit structure toward the bearish
side of neutral.
