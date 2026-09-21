# Phase 7b — Deep Fundamentals & Quality Veto (FINNHUB)

**Ticker:** IREN
**As-of date:** 2026-06-05
**Generated:** 2026-06-07T01:45Z
**Upstream phases cited:** phase-0-intake.md (fz float/SI), phase-6-macro.md (BTC driver), phase-7-insights.md (flow bias baseline)

## Summary

The underlying business **partially contradicts the bearish flow bias** from
phases 1–7: revenue is growing **+97.3% TTM YoY** [FUND:revenueGrowthTTMYoy]
with a fortress current ratio (4.96) and a forward consensus that sees an EPS
inflection (FY27 ~$1.18 vs FY26 ~$0.32–0.40; consensus Buy, PT ~$80–84, +47–55%
above spot) — but the **near-term prints are deteriorating**: two consecutive
misses, the latest a **−283% surprise** (FQ3'26 actual −$0.74 vs est −$0.19)
on BTC-driven revenue softness, exactly the macro channel phase-6 identified.
Valuation is the vulnerability: P/S 25.9 (Finnhub) / 38.9 (fz) vs the real
miner cohort at 5.4–14.3 — IREN is priced as an AI-datacenter story, not a
miner. Insider axis is structurally unavailable (Australian FPI — no Form 4s;
Finnhub MSPR and transactions both empty, fz clusters empty). Net: **one clean
contradiction** (growth) against the bearish bias, one mixed axis (earnings),
one n/a (insider) → **tier_adjustment = CAUTION** — any bearish directional
trade cuts one size step; the flow is selling a business that is still growing
underneath.

## Key signals

- **Revenue growth +97.29% TTM YoY; Sales Q/Q +13.25%** [FUND:revenueGrowthTTMYoy,
  FUND:sales_qq fz] — vs the TipRanks-reported −22% *sequential* Q3 revenue
  decline (phase-6): growing YoY, inflecting down QoQ on BTC price.
- **Earnings recency broken: 2 straight misses** — FQ3'26 −$0.74 vs −$0.19 est
  (−283.0%), FQ2'26 −$0.15 vs −$0.11 (−35.5%); preceded by two huge beats
  (+561.8%, +319.8%) [FUND:earnings_surprises]. Beat-rate 2/4; direction down.
- **Forward consensus still firmly bullish**: FY26 rev ~$958M–1.04B, FY27 EPS
  ~$1.18; 10 buy / 3 hold / 2 sell, avg PT $79.8–81.1 (high 126 / low 41); fz
  cross-source Recom **1.94**, target **$84.15** [FUND:recom fz,
  WebSearch:stockanalysis.com/simplywall.st] — agreement between sources.
- **Valuation premium to cohort**: P/S 25.9–38.9 and Fwd P/E 133.1 vs MARA 5.41
  / RIOT 14.27 / CLSK 5.41 / APLD 31.85 P/S, none of which screen a positive
  P/E at all [FUND:peer_pe fz].
- **Balance sheet OK, margins noisy**: current ratio 4.96, LT-debt/equity 1.47,
  ROE 16.17%, ROA 8.6%, net margin +10.27% but operating margin TTM **−70.05%**
  (BTC fair-value/D&A accounting noise — flag, don't over-read)
  [FUND:key_metrics].

## Detailed findings

### Valuation [FUND:key_metrics, FUND:peer_pe fz]

peTTM 252.15 / peNormalized 223.08 / P/B 7.72 / P/S 25.90 (Finnhub; fz shows
P/E 187.16, Fwd P/E 133.14, P/S 38.86 — base differences, both rich), PEG n/a,
beta **4.28**, mcap $19.40B (Finnhub TTM-current; implies ~$56.9/sh vs 54.35
close — minor staleness flagged per pitfalls), 52W 8.82–76.87.

### Growth profile

Revenue +97.29% TTM YoY [FUND:revenueGrowthTTMYoy]; epsGrowthTTMYoy null
(sign-flip artifacts); fz EPS this Y −225.62% / **EPS next Y +185.51%** — the
consensus story is "FY26 trough, FY27 inflection" on AI-datacenter
contracts (cf. the 800MW deal coverage, phase-6). Sequential softness is
BTC-price-driven (mining segment), not demand-driven (ISM 54+, phase-6).

### Earnings-surprise history [FUND:earnings_surprises] (look-ahead filtered ≤2026-06-05; 4 quarters returned)

| Period | Actual EPS | Estimate | Surprise | Surprise % |
|--------|-----------:|---------:|---------:|-----------:|
| 2026-03-31 (FQ3'26) | −0.74 | −0.1932 | −0.5468 | **−283.0%** |
| 2025-12-31 (FQ2'26) | −0.15 | −0.1107 | −0.0393 | −35.5% |
| 2025-09-30 (FQ1'26) | +1.08 | +0.1632 | +0.9168 | +561.8% |
| 2025-06-30 (FQ4'25) | +0.66 | +0.1572 | +0.5028 | +319.8% |

Beat-rate 50% (2/4); recency strongly negative. Hyper-volatile EPS (beta-4
name with BTC fair-value swings through the P&L).

### Forward consensus (WebSearch fallback — Finnhub estimate endpoints paid)

FY2026: revenue ~$958.4M–1.04B, EPS ~$0.318–0.396. FY2027: EPS ~$1.18.
Consensus "Buy" (10/3/2 across 14–15 analysts), avg PT $79.84–81.07
[WebSearch:stockanalysis.com, simplywall.st, public.com]. Direction of
revisions intra-quarter: not retrievable free — flagged as a gap; the level
vs spot (+47–55%) is the usable datapoint.

### Balance-sheet health (statements limited — metric proxies)

`financials-reported` returned only n=2 quarterly filings (latest FQ2'26,
period 2025-12-31 — FPI 6-K lag); leaned on metrics per guidance: current
ratio **4.96** (highly liquid), LT-debt/equity **1.47** (real leverage from
the DC buildout, but term-funded), ROE 16.17 / ROA 8.6.

### Cash-flow quality

Direct FCF not free-tier. Proxy: operating margin TTM −70.05% vs net margin
+10.27% — the wedge is non-operating items (BTC fair-value gains, interest
cap). Capex intensity is structurally huge (AI-DC buildout). Treat reported
profitability as low-quality/noisy; the equity is a growth-capex claim, not a
cash-flow claim. [FUND:key_metrics proxies]

### Insider signal

- Finnhub MSPR: **empty (n=0)**; Finnhub insider-transactions 2026 YTD:
  **empty (n=0)** — IREN is an Australian-incorporated foreign private issuer
  (no Form 4 filings); absence here is a **structural data gap, not absence
  of conviction** — axis scored n/a, per "don't fabricate from missing data".
- fz insider-clusters (30d, ≥2 distinct, buy AND sell): no IREN row either
  side [FUND:insider_cluster fz]. Insider Own 9.17% / Inst Own 46.73% (fz).

### Peers — relative value [FUND:peer_pe fz]

Finnhub's peer list (TEAM, BRAI, WTC.AX, TNE.AX, IRE.AX, SDR.AX, CAT.AX,
OCL.AX) is a **mis-cohort** (Aussie-listed software comps from the
incorporation domicile) — replaced with the actual trading cohort (phase-0.5):

| Ticker | P/E | Fwd P/E | P/S | Short Float | Float | Perf YTD | Recom |
|--------|----:|--------:|----:|------------:|------:|---------:|------:|
| **IREN** | 187.2 | 133.1 | 38.9 | **15.71%** | 324.2M | +43.9% | 1.94 |
| MARA | – | – | 5.41 | 26.68% | 372.3M | +37.2% | 2.07 |
| RIOT | – | – | 14.27 | 18.52% | 348.4M | +94.6% | 1.38 |
| CLSK | – | – | 5.41 | 34.12% | 246.4M | +54.1% | 1.08 |
| APLD | – | – | 31.85 | 30.43% | 258.7M | +61.6% | 1.00 |

Placement: IREN is the cohort's **quality/AI-premium name** — only positive
earnings, lowest short float, richest sales multiple bar APLD. That premium is
the thing at risk when BTC leads the tape down.

## Red flags

1. **Serial recent misses** (2 straight, latest −283%) with BTC at $60k —
   FQ4'26 (Aug-27 print) estimate risk is live.
2. **Multiple compression risk**: P/S 26–39 vs cohort 5–14; −29% off the 52W
   high with beta 4.28.
3. **Low-quality earnings**: −70% operating margin vs +10% net margin wedge;
   profitability is accounting-sensitive to BTC marks.
4. (Gap, not flag): no insider visibility at all (FPI).

## Tool / source calls

| Source | Status | Key value |
|---|---|---|
| Finnhub `/stock/metric` | OK | P/S 25.90, rev growth +97.29%, beta 4.28 ← `.metric` |
| Finnhub `/stock/earnings` | OK (4 rows) | FQ3'26 surprise −283.0% ← `.[0].surprisePercent` |
| Finnhub `/stock/eps-estimate` | **403 paid, skipped** | → WebSearch fallback |
| Finnhub `/stock/revenue-estimate` | **403 paid, skipped** | → WebSearch fallback |
| Finnhub `/stock/peers` | OK (mis-cohort, replaced) | 8 tickers |
| Finnhub `/stock/insider-sentiment` | OK, **empty** (FPI) | n=0 |
| Finnhub `/stock/insider-transactions` (fallback) | OK, **empty** (FPI) | n=0 |
| Finnhub `/stock/financials-reported` | OK (n=2, lagged) | latest FQ2'26 |
| fz quote IREN (Recom/target/ratios) | OK | Recom 1.94, target 84.15 |
| fz insider-clusters buy/sell | OK, empty for IREN | [] |
| fz quote MARA/RIOT/CLSK/APLD | OK | peer table above |
| WebSearch forward consensus | OK | FY27 EPS ~1.18, PT ~80–81 |

## Tool / source errors

- `eps-estimate` / `revenue-estimate`: `{"error":"You don't have access to
  this resource."}` — paid tier, skipped (memory-consistent); WebSearch used.
- Look-ahead guard applied: earnings rows filtered `period <= 2026-06-05`
  (none dropped — latest row was FQ3'26, reported pre-as-of). Metric ratios
  are TTM-current; as-of = latest close, so contamination limited to the
  ~$56.9-implied mcap staleness noted above.

## Verdict for downstream phases

```
fundamental_signal:  NEUTRAL          # two-sided: growth+consensus up vs prints+valuation down
tier_adjustment:     CAUTION          # 1 clean contradiction vs the BEARISH flow bias
contradiction_count: 1                # growth/margins axis contradicts a short (rev +97% TTM, FY27 inflection);
                                      # earnings_trend axis MIXED (recency confirms short, fwd consensus contradicts) → not counted;
                                      # insider axis n/a (FPI structural gap) → not counted
insider_cluster:     {present: n, distinct_buyers: n/a, side: n/a}   # fz, D5 — no data (FPI)
key_risks:
  - "BTC transmission: FQ3'26 missed by −283% on BTC softness; BTC ~$60k keeps the mining P&L impaired into the 2026-08-27 print"
  - "Cohort-premium multiple (P/S 26–39 vs peers 5–14, beta 4.28) — fastest multiple to compress if AI-capex sentiment cracks"
  - "Analyst anchor (PT ~$80, Recom 1.94) set pre-crash — revision risk if BTC stays <$65k; no insider signal possible to cross-check"
```

**Phase-9 effect:** the flow bias is bearish; CAUTION cuts one size step from a
bearish directional. Symmetrically note: these fundamentals do NOT support a
fresh aggressive LONG either (misses + multiple risk) — they argue the name is
a growth business in a BTC air-pocket, i.e. **two-sided chop with a quality
floor**, consistent with phase-7's MIXED and phase-3's "protect the book, keep
the upside" positioning read.
