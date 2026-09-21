# Phase 7b — Deep Fundamentals & Quality Veto (FINNHUB)

**Ticker:** CMPS
**As-of date:** 2026-06-18
**Generated:** 2026-06-20
**Upstream phases cited:** phase-1-flow.md, phase-5-historical.md, phase-6-macro.md, phase-7-insights.md

## Summary

The underlying business quality **contradicts the bearish flow thesis** — this is a
symmetric **VETO of a fresh directional short**. CMPS is a pre-revenue clinical
biotech (no P/E, no revenue, ROE −48%, ~$2.58/sh annual cash burn), so the relevant
fundamentals are pipeline, consensus, insider, and balance sheet — and all four lean
*bullish/improving*: both Phase-3 trials met their primary endpoints (phase-6),
analyst consensus is **strong-buy (Recom 1.12)** with a **$21.72 target (+73% vs
$12.53)**, **insiders are net buyers including very recently** (MSPR +100 in May 2026
on +197,937 shares; +96 in Mar 2026 on +926,671), the balance sheet is healthy
(current ratio 3.32, LT-debt/equity 0.15), and CMPS is the **best YTD performer in its
peer group (+81.6%)**. Two of the three quality axes (forward-consensus, insider
sentiment) directly contradict a short; only the cash-burn/no-revenue axis gives a
bear anything to hold. **2 contradictions → VETO** the bearish directional trade. The
LEAP put reads as a hedge or a cheap convexity bet on the H2-2026 durability binary —
not a quality-backed short.

## Key signals

- Analyst consensus **STRONG-BUY (Recom 1.12)**, target **$21.72 (+73%)** — contradicts
  bear [FUND:recom fz]
- Insiders **net buyers**: MSPR **+100 (May'26, +197,937 sh)**, **+96 (Mar'26,
  +926,671 sh)** — contradicts bear [FUND:insider_MSPR]
- Both **Phase-3 trials met primary endpoints**; NDA Q4 2026 (phase-6) — improving
  forward [FUND:earnings_trend]
- Healthy balance sheet: **current ratio 3.32**, LT-debt/equity **0.15** [FUND:metric]
- Bear's only foothold: **pre-revenue, ROE −48%, CF/sh −2.58** (cash burn → dilution
  risk) [FUND:metric]
- Best peer-group YTD performer **+81.6%** (vs ROIV +44.8%, CNTA +60.0%, KNSA +33.6%)
  [FUND:peer_pe fz]

## Detailed findings

### Valuation

- **PE null / P/S null / PEG null** — pre-revenue, no earnings. P/B **2.18**. Beta
  **2.53** (high). EV ≈ $1.28B; mcap $1.69B (fz). Standard clinical-biotech profile:
  valuation is pipeline-NPV-driven, not multiple-driven. [FUND:metric]

### Growth profile

- revenuePerShareTTM **0**, revGrowth/epsGrowth **null** (no commercial revenue).
  ROE **−48.36%**, ROA **−55.39%** — deep losses funding R&D. Margins null. This is the
  one axis a bear can cite (no revenue, burning cash); it reflects clinical-stage
  structure, not deterioration of a going concern.

### Earnings-surprise history (8-quarter; EPS = losses, lumpy R&D spend)

| Period | Actual EPS | Estimate | Surprise | Surprise % |
|--------|-----------:|---------:|---------:|-----------:|
| 2026-03-31 | −0.30 | −0.386 | +0.086 | +22.2% |
| 2025-12-31 | −1.00 | −0.402 | −0.598 | −148.6% |
| 2025-09-30 | −1.44 | −0.398 | −1.042 | −262.0% |
| 2025-06-30 | −0.41 | −0.437 | +0.027 | +6.1% |

Beat-rate **2/4 (50%)**; misses were larger losses (trial-cost timing), beats
marginal. For pre-revenue biotech, EPS surprise is spend-timing noise, **not** a
demand signal — low weight on the earnings_trend axis; the *pipeline* (2 Phase-3
wins) is the real forward read.

### Forward consensus

- Finnhub `eps-estimate` / `revenue-estimate` returned **no `.data`** (free-tier /
  sparse coverage for this name). Forward read taken from **fz Recom 1.12
  (strong-buy)** + **target $21.72** and the phase-6 catalyst stack (NDA Q4 2026).
  Direction = **improving**. [FUND:recom fz]

### Balance-sheet health

- **current ratio 3.32** (healthy short-term liquidity), **LT-debt/equity 0.15** (low
  leverage). For a cash-burning biotech this is a *relatively* comfortable runway
  position — but with CF/sh −2.58 and no revenue, financing/dilution before
  commercialization remains the structural risk. `financials-reported` not separately
  pulled; metric proxies used. [FUND:metric]

### Cash-flow quality

- cashFlowPerShareTTM **−2.58** → negative operating cash flow (R&D + Phase-3 costs).
  No buyback/dividend (appropriate for clinical stage). Burn vs the 3.32 current ratio
  is the watch item — phase-9 carries dilution risk.

### Insider signal (MSPR, trailing ~12mo; `[FUND:insider_MSPR]`)

| Month | MSPR | Δ shares |
|-------|-----:|---------:|
| 2026-05 | **+100** | +197,937 |
| 2026-03 | **+95.99** | +926,671 |
| 2026-02 | −100 | −16,181 (small) |
| 2025-10 | +100 | +52,000 |
| 2025-08 | −100 | −6,366 (small) |
| 2025-07 | +100 | +52,000 |
| 2025-06 | +100 | +221,000 |

Dominant signal **strongly bullish** — the large positive months (Mar'26 +927K,
May'26 +198K, Jun'25 +221K) dwarf the small sell months. Most recent (May'26) is max
bullish. **|MSPR|>30 sustained → insiders confident.** `fz insider-clusters` shows
**no ≥2-distinct-owner cluster in the last 30d** (buy or sell) — the big buys predate
the 30d window. insider_cluster = none, but the MSPR trend is decisively positive.
[FUND:insider_cluster fz]

### Peers — relative value (`[FUND:peer_pe fz]`)

| Ticker | P/E | Mkt Cap | Perf YTD |
|--------|----:|--------:|---------:|
| **CMPS** | – | $1.69B | **+81.6%** |
| ROIV | – | $22.61B | +44.8% |
| CNTA | – | $6.19B | +60.0% |
| KNSA | 60.7 | $4.24B | +33.6% |
| IMCR | – | $1.45B | −17.6% |
| AUTL | – | $0.40B | −24.1% |

Most peers pre-earnings (P/E "–"). CMPS is the **top YTD performer** and mid-cap in
the group. Peer SI/float not retrievable via the `fz --tickers` overview (null);
CMPS's own short float = **5.69%** (phase-0). Peer-SI comparison thin — not material
to the veto.

## Red flags

- **Pre-revenue cash burn** (CF/sh −2.58, ROE −48%) → financing/dilution risk before
  commercialization — the one genuine bear foothold.
- **Durability binary**: COMP006 26-week data (H2 2026) — durability is the historical
  weak point of psychedelic antidepressants (phase-6).
- **High beta 2.53 + parabolic +81.6% YTD** → outsized drawdown if any catalyst slips.
- (NOT red flags: leverage is low, liquidity healthy, consensus strong-buy, insiders
  buying — these are why the short is vetoed.)

## Tool / source calls (audit trail)

| Endpoint | Result |
|----------|--------|
| Finnhub `/stock/metric` | ok — PE null, currentRatio 3.32, ROE −48.36, beta 2.53, CF/sh −2.58 |
| Finnhub `/stock/earnings` (8q) | ok — beat-rate 2/4, EPS losses |
| Finnhub `/stock/eps-estimate` | **no `.data`** (sparse coverage) |
| Finnhub `/stock/revenue-estimate` | **no `.data`** |
| Finnhub `/stock/peers` | ok — ROIV/CNTA/KNSA/IMCR/AUTL (+ non-US .L/OTC dropped) |
| Finnhub `/stock/insider-sentiment` (MSPR) | ok — net buyers, +100 May'26 |
| `fz quote --tickers` (peer overview) | ok — CMPS top YTD +81.6% |
| `fz insider-clusters` (buy/sell) | ok — no ≥2-owner cluster in 30d |
| `fz quote` Recom/target | ok — Recom 1.12, target $21.72 |

## Tool / source errors

- Finnhub `eps-estimate` / `revenue-estimate` returned empty `.data` (free-tier
  sparse coverage) — forward consensus taken from fz Recom/target + phase-6 calendar.
- `fz --tickers` overview returns no SI/float fields (null) — a `fz screen --view
  ownership` sector cut would be needed for peer SI; not material to the verdict, skipped.

## Verdict for downstream

```
fundamental_signal:  BULLISH
tier_adjustment:     VETO        # symmetric: SHORT thesis into an improving underlying
contradiction_count: 2          # {earnings/forward-consensus, insider_MSPR} contradict the bear;
                                #  growth/margins (cash burn) is the bear's only foothold (not counted)
insider_cluster:     {present: no, distinct_buyers: n/a, side: n/a}   # MSPR bullish, but no 2+-owner 30d cluster
key_risks:           [pre-revenue cash burn → dilution risk (CF/sh -2.58, current ratio 3.32),
                      COMP006 26-week durability data H2 2026 (binary),
                      high beta 2.53 on a parabolic +81.6% YTD name → drawdown risk]
```

- **Quality gate effect:** the bearish flow says "short," but the business is
  improving on ≥2 axes (consensus strong-buy + insider buying) → **read the bearish
  LEAP put as a hedge / cheap durability-binary convexity, NOT a quality-backed
  directional short.** Phase-9: directional short → watch-only / 0%; defined-risk
  carry (e.g. the existing put as a hedge) is the only structure this gate permits.
- This gate is **downside-only** — it cannot flip CMPS to a long; it only cuts the
  bear. The `key_risks` are the legitimate downside scenarios the LEAP put targets,
  carried forward for phase-9's risk framing.
