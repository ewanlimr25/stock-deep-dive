# Phase 7b — Deep Fundamentals & Quality Veto

**Ticker:** SWKS
**As-of date:** 2026-07-31
**Generated:** 2026-08-02
**Upstream phases cited:** `phase-0-intake.md`, `phase-1-flow.md`, `phase-2-dark-pool.md`, `phase-5-historical.md`, `phase-6-macro.md`, `phase-7-insights.md`

## Summary

The underlying business is **decent quality but stalling** — not deteriorating
enough to veto, not improving enough to confirm. SWKS has beaten consensus in
**4 of 4 available quarters (100%, average surprise +11.3%)**, carries a
**fortress balance sheet** (cash **$1,413.3M** vs total debt **$996.6M** = net cash
~$417M; current ratio **2.38**; LT-debt/equity **0.086**), generates healthy free
cash flow (**$306.9M in the six months to 2026-04-03**, ~$614M annualised = a 6.5%
FCF yield), and shows **persistently positive insider sentiment** (MSPR +100,
+42.06, 0, +33.69 across the trailing year — **no negative month**). Against that:
**EPS is shrinking while revenue barely grows** (`epsGrowthTTMYoy` **−6.00%** on
`revenueGrowthTTMYoy` **+2.33%**), margins are thin and guided lower (operating
margin TTM **9.09%**, Q4 GM guided down to 44–45%), consensus expects **EPS Next Y
−2.20%**, and the sell side has moved to **Hold (1 Strong Buy / 4 Buy / 16 Hold /
3 Sell, avg PT $74.72)** with **KeyBanc cutting to Sector Weight on 2026-07-14**
explicitly on single-customer concentration into a contracting smartphone market.
**Exactly one of the three quality axes contradicts the flow bias ⇒
`tier_adjustment: CAUTION`.** This phase also recovers the data phase 0 could not:
**SWKS short float is 21.93% — by far the highest in its 17-name peer group** — a
finding that belongs to phase 7c and is flagged forward in the strongest terms.

## Key signals

- **100% beat rate.** 4 of 4 available quarters beat: +4.30%, +9.08%, +7.99%,
  +23.65% (avg **+11.26%**). `[FUND:earnings_surprises]`
- **But EPS is going backwards:** `epsGrowthTTMYoy` **−6.00%** against
  `revenueGrowthTTMYoy` **+2.33%** — revenue up, earnings down. `[FUND:metric]`
- **Fortress balance sheet, about to be levered.** Cash **$1,413.3M**, total debt
  **$996.6M**, equity **$5,765.7M**, current ratio **2.3756**,
  `longTermDebt/equityQuarterly` **0.0861**. `phase-6-macro.md` documents a
  **~$2B debt raise** in progress ⇒ pro-forma **~$1.6B net debt** from ~$417M net
  cash. `[FUND:financials_reported]`
- **Insider sentiment is positive and has never turned negative** in the trailing
  year: MSPR **+100.00** (2025-09), **+42.06** (2025-11), **0** (2026-02),
  **+33.69** (2026-05). Two months clear the |MSPR| > 30 strong-signal bar.
  **No insider sell-cluster** — `fz insider-clusters` returns SWKS on **neither**
  side. `[FUND:insider_MSPR]` `[FUND:insider_cluster fz]`
- **★ Short float 21.93%** (Short Ratio 5.77, Float **149.81M** ⇒ **~32.9M shares
  short**) — **2.7× the next-highest peer** (ALGM 10.05%) and **2.7× its own merger
  partner QRVO (8.02%)**. `[FUND:peer_pe fz]` → **hand off to phase 7c.**
- **Sell side is on Hold and cutting targets:** consensus **Hold**, avg PT
  **$74.72** (+20.0%); **1 Strong Buy / 4 Buy / 16 Hold / 3 Sell**; KeyBanc →
  Sector Weight (2026-07-14, no PT); Stifel PT → **$70** (2026-07-29).
  `[FUND:recom WebSearch:dailypolitical.com, gurufocus.com]`

## Detailed findings

### Valuation

`/stock/metric?metric=all` (Finnhub) plus the `fz` peer screen:

| Metric | Value |
|---|---|
| `peTTM` | **25.95** |
| `peNormalizedAnnual` | 19.64 |
| `pbAnnual` | 1.99 |
| `psTTM` | 2.32 |
| `pegTTM` | **null** (not returned) |
| `beta` | **1.506** |
| `52WeekHigh` / `52WeekLow` | 90.90 / 51.93 |

Cross-source (`fz`, EOD 2026-07-31): **P/E 32.26**, **Forward P/E 12.63**,
**PEG n/a**, **EPS Next Y −2.20%**.

**The two P/E figures disagree (25.95 vs 32.26) and both are reported.** They rest
on different EPS bases — 62.28 / 25.945 implies **$2.40** TTM EPS while
62.28 / 32.26 implies **$1.93**. The price input is identical (both reconcile to
the $62.28 as-of close), so the gap is definitional (GAAP vs adjusted, and which
four quarters are summed), not a price-date artifact. Neither is quoted as *the*
multiple. Per the phase's pitfall, Finnhub's `/stock/metric` ratios are TTM-current
rather than strictly point-in-time; the as-of date happens to be the latest
available session (`phase-0-intake.md`), which limits but does not eliminate that
contamination.

**Forward P/E of 12.63 against a trailing 25.95–32.26 is the headline valuation
fact** — the market is paying ~12.6× forward non-GAAP earnings (≈$4.93/share,
consistent with the $1.08 actual and $1.27 guided quarters). That is **cheap
against the peer group** (median forward P/E ~24.4) and cheap against the
Semiconductors industry aggregate (`phase-6-macro.md`: **Fwd P/E 28.75, PEG 0.56**).

**But cheapness alone is not CONFIRM** — the phase's own heuristic requires a
growth or insider co-signal, and **EPS Next Y is −2.20%**. This is the profile of a
**value trap candidate**, not a value opportunity, absent the merger.

### Growth profile

| Metric | Value |
|---|---|
| `revenueGrowthTTMYoy` | **+2.33%** |
| `epsGrowthTTMYoy` | **−6.00%** |
| `grossMarginTTM` | **41.07%** |
| `operatingMarginTTM` | **9.09%** |
| `netProfitMarginTTM` | **8.93%** |
| `roeTTM` | **6.30%** |
| `roaTTM` | **4.60%** |

Half-year income statement (period ended **2026-04-03**, the latest report at or
before the as-of date — the FQ3 10-Q was filed **2026-08-05**, *after* as-of, so it
is correctly excluded):

| Line | 6mo to 2026-04-03 |
|---|---|
| Net revenue | $1,979.1M |
| Cost of goods sold | $1,166.5M |
| **Gross profit** | **$812.6M (41.06% margin)** |
| R&D | $415.7M (21.0% of revenue) |
| SG&A | $228.0M |
| Restructuring, impairment & other | $22.5M |
| **Operating income** | **$145.9M (7.37% margin)** |
| Interest expense | $13.9M |
| Net income | **$114.8M** |
| Diluted EPS | **$0.76** |
| Diluted shares | **150.5M** |

**Revenue is growing 2.33% while EPS falls 6.00% — the definition of margin
compression.** GAAP operating margin of **7.37%** on the half and **9.09%** TTM is
thin for a semiconductor franchise, and R&D at **21.0% of revenue** is not
discretionary spend that can be cut without damaging the pipeline. Management
guided Q4 non-GAAP gross margin **down to 44–45%** from ~44.5–45.5% on mobile mix
and input-cost inflation (`phase-6-macro.md`).

**ROE of 6.30% is the number that most clearly says "stalled."** On a $5.77B equity
base with a 41% gross margin franchise, 6.3% is well below cost of equity for a
1.51-beta stock.

*(Note: the diluted share count of **150.5M** independently validates the
150,956,637 figure derived in `phase-2-dark-pool.md` from `marketcap / close`, and
sits right on the `fz` float of 149.81M — confirming the float-normalisation
denominators used in phases 2 and 3 were sound.)*

### Earnings-surprise history

`/stock/earnings?limit=8` returned **4 rows** (not 8). **Look-ahead guard applied:
every returned `period` is ≤ 2026-06-30 ≤ the 2026-07-31 as-of date — no future
period was returned and none was dropped.**

| Period | FY/Q | Actual EPS | Estimate | Surprise | Surprise % |
|---|---|---|---|---|---|
| 2026-06-30 | FY26 Q3 | **1.08** | 1.0355 | +0.0445 | **+4.30%** |
| 2026-03-31 | FY26 Q2 | **1.15** | 1.0543 | +0.0957 | **+9.08%** |
| 2025-12-31 | FY26 Q1 | **1.54** | 1.4260 | +0.1140 | **+7.99%** |
| 2025-09-30 | FY25 Q4 | **1.76** | 1.4234 | +0.3366 | **+23.65%** |

**Beat rate: 4 / 4 = 100%. Average surprise: +11.26%.**

**But read the actual EPS column, not just the surprise column: 1.76 → 1.54 → 1.15
→ 1.08.** Four consecutive sequential declines, a **−38.6% fall** peak to trough.
The company keeps beating a bar that keeps being lowered. This is the pattern the
BigGo headline referenced as *"Faces 38% Profit Drop Ahead of Earnings."*

Seasonality explains part of it — SWKS's fiscal year ends in September and the
December quarter is the seasonal iPhone-build peak — but not the direction:
`epsGrowthTTMYoy` at **−6.00%** is a like-for-like YoY measure and it is negative.

**Assessment of this axis: SPLIT, and therefore not counted as a contradiction.**
A 100% beat rate with an +11.26% average surprise is a genuinely strong execution
record; the phase's own guidance ("*a single bad quarter is not a trend*") argues
against counting a deteriorating *forward* view as a contradiction when the
*realised* record is spotless. Both halves are recorded so phase 8 can argue either.

### Forward consensus — **PAID TIER, UNAVAILABLE**

```
/stock/eps-estimate?symbol=SWKS&freq=quarterly
→ {"error":"You don't have access to this resource."}

/stock/revenue-estimate?symbol=SWKS&freq=quarterly
→ {"error":"You don't have access to this resource."}
```

Both endpoints are **paid tier on this key — marked "paid, skipped" per the phase
instruction, not retried, and no fabricated substitute used.**

Substituting only from sources already validated in this run:

| Forward datapoint | Value | Source |
|---|---|---|
| **Q4 FY26 revenue guide** | **$1.010–1.060B** | `phase-6-macro.md` (company, 2026-07-28) |
| **Q4 FY26 non-GAAP EPS guide** | **$1.27 mid vs $1.29 consensus — slight MISS** | `phase-6-macro.md` |
| Q4 FY26 gross margin guide | **44–45%**, down | `phase-6-macro.md` |
| **EPS Next Y (consensus growth)** | **−2.20%** | `fz` valuation screen |
| **Consensus rating** | **Hold** | WebSearch |
| **Average price target** | **$74.72** (+20.0% vs $62.28) | WebSearch |
| Rating distribution | 1 Strong Buy / 4 Buy / **16 Hold** / 3 Sell (24 analysts) | WebSearch |
| KeyBanc | **Overweight → Sector Weight, 2026-07-14, no PT** | WebSearch |
| Stifel | **PT lowered to $70.00, 2026-07-29** | WebSearch |
| Merger synergies (guided) | **$500M+** | `phase-6-macro.md` |

**Forward direction: DOWN.** Consensus EPS growth is negative, the Q4 guide came in
below consensus, gross margin is guided lower, and two named firms cut inside the
month. **This finally fills the analyst gap `phase-7-insights.md` could not** —
`uw insights analyst-vs-flow` returned no analyst block at all, and
`deep-dive.yahoo_fundamentals` was HTTP 401. The comparison the skill wanted is now
possible: **Wall Street is on Hold and cutting; the options tape is selling
premium on both legs.** Neither side is directional. **They agree — on apathy.**

### Balance-sheet health

Latest report at or before as-of (period ended **2026-04-03**):

| Line | Value |
|---|---|
| Cash and cash equivalents | **$1,413.3M** |
| Inventory | $885.6M |
| Goodwill | $2,176.7M |
| **Total assets** | **$7,896.0M** |
| Current portion of long-term debt | $499.9M |
| Long-term debt | $496.7M |
| **Total debt** | **$996.6M** |
| Total liabilities | $2,130.3M |
| **Total stockholders' equity** | **$5,765.7M** |

Ratios (Finnhub `/stock/metric`): `currentRatioQuarterly` **2.3756**,
`longTermDebt/equityQuarterly` **0.0861**, `totalDebt/totalEquityQuarterly`
**0.1728**.

**Today this is a fortress: ~$417M net cash, 2.38× current ratio, 17% total
debt/equity.** But it is about to change materially. `phase-6-macro.md` documents a
**~$2B debt raise** to fund the Qorvo cash consideration ($32.50/QRVO share).
Pro-forma, crudely:

```
Total debt      $996.6M  +  ~$2,000M   ≈  $3.0B
Net cash/(debt) +$417M   −  ~$2,000M   ≈  −$1.6B net debt
Debt / equity   0.173    →              ≈  0.52
```

That is **not distress** — ~$3.0B of debt against ~$614M annualised FCF and a
franchise gross margin — but it is a **real step-change in financial risk**, taken
into a 10-year yield that rose **+24bp** over the preceding month
(`phase-6-macro.md`). One caution: **goodwill is $2,176.7M, or 37.8% of equity**,
and a Qorvo combination will add substantially more. Impairment risk is a live
tail if the combined entity underperforms.

### Cash-flow quality

Six months to **2026-04-03**:

| Line | Value |
|---|---|
| Net cash provided by operating activities | **$445.8M** |
| Capital expenditures | $138.9M (+$32.2M accrued, not paid) |
| **Free cash flow (OCF − capex)** | **$306.9M** |
| **Dividends paid** | **$213.2M** |
| Buyback — repurchase program | **$7.5M** |
| Buyback — payroll-tax withholding on equity awards | $40.0M |

**The cash-flow statement explains the dividend elimination completely.**
Dividends of **$213.2M** consumed **69.5% of the $306.9M** of free cash flow
generated in the half, while the actual repurchase program spent **$7.5M** —
essentially nothing. Annualised, the dividend was a **~$426M/yr** claim on
~$614M/yr of FCF.

So the 2026-07-28 capital reallocation is **financially rational**: killing a
~$426M/yr dividend and authorising a **$2B buyback** (`phase-6-macro.md`) frees the
cash to service ~$2B of new merger debt. **The business logic is sound; the
shareholder-base consequence is severe** — `phase-0-intake.md` snapshotted the
prior yield at **4.56% TTM with a 91.35% payout ratio**, i.e. this was held
substantially by income mandates that are now **structurally misaligned and selling
for non-fundamental reasons.**

Capex intensity is a modest **7.0% of revenue** ($138.9M / $1,979.1M) — asset-light
for a semi, consistent with a fab-lite model, and it means FCF conversion should
hold up even as revenue stalls.

### Insider signal

`/stock/insider-sentiment?from=2025-07-31&to=2026-07-31`:

| Year-Month | `change` (net shares) | **MSPR** |
|---|---|---|
| 2025-02 * | +508,710 | **+99.38** |
| 2025-05 * | +46,985 | +56.38 |
| **2025-09** | +89,910 | **+100.00** |
| **2025-11** | +146,411 | **+42.06** |
| **2026-02** | 0 | **0.00** |
| **2026-05** | +22,749 | **+33.69** |

*\* Returned despite falling before the requested `from` date — Finnhub over-returned
the window, as the phase warns it can. Rows are shown for completeness but the
verdict uses only the four in-window months (2025-09 → 2026-05).*

**Every observation in the trailing year is ≥ 0. There is no negative MSPR month
anywhere in the series.** Two of the four in-window months clear the |MSPR| > 30
strong-signal threshold (+100.00 and +33.69), and the mean of the four is **+43.9**.

`fz insider-clusters --days 30 --min-buyers 2`: SWKS appears on **neither** the
`buy` side nor the `sell` side (the only buy-cluster returned market-wide was XAIR,
2 distinct owners). ⇒ `insider_cluster: {present: n, distinct_buyers: n/a, side: n/a}`.

**Three honest caveats:**
1. **There are no rows for 2026-06 or 2026-07** — precisely the pre-earnings window
   in which one syndicated headline alleged *"Insider Sales Rattle Investors"*
   (BigGo, pre-print). **Absence of data is not evidence of absence.** The most
   recent observation is 2026-05, two months stale.
2. MSPR is a blended ratio and does not distinguish open-market purchases from
   option exercises or grant vestings. A +100 reading on 89,910 shares is a small
   absolute number for a 149.81M-share float (**0.06%**).
3. The phase's own note applies: *absence of insider activity is itself a weak
   signal — note it, don't treat it as bullish.* Two of six months show negligible
   or zero activity.

**Assessment of this axis: CONFIRMS.** No insider selling, no sell cluster, and a
positive multi-month trend — but weakly, on small absolute size and stale data.

### Peers — relative-value comparison

Finnhub `/stock/peers` returned: **MTSI, LSCC, SITM, SMTC, RMBS, QRVO, ALGM, SLAB,
CRUS, MXL, RGTI, NVDA** (self dropped). That list omits SWKS's closest economic
comparables, so the group was **extended** with the RF/analog cohort used in
`phase-0.5-context.md` (QCOM, NXPI, MCHP, ADI, TXN, AVGO) and pulled via
`fz screen --tickers … --view valuation` + `--view ownership` (17 names returned of
17 requested; RGTI/NVDA dropped as non-comparable):

| Ticker | Price | P/E | Fwd P/E | PEG | EPS Next Y | **Short Float** | Short Ratio | Float | Inst Own |
|---|---|---|---|---|---|---|---|---|---|
| **SWKS** | **62.28** | **32.26** | **12.63** | — | **−2.20%** | **21.93%** | **5.77** | **149.81M** | 112.87% |
| **QRVO** *(merger partner)* | 90.57 | 21.02 | 11.36 | 1.26 | +6.63% | **8.02%** | 5.39 | 87.13M | 96.18% |
| QCOM | 147.61 | 17.08 | 14.27 | 4.85 | −2.64% | 3.45% | 1.66 | 1.05B | 81.15% |
| NXPI | 229.16 | 21.93 | 12.59 | 0.59 | +20.45% | 3.47% | 2.07 | 251.82M | 95.76% |
| MCHP | 74.29 | 344.09 | 17.81 | 0.44 | +31.03% | 6.61% | 2.93 | 533.14M | 95.94% |
| ADI | 367.41 | 54.60 | 24.35 | 0.80 | +21.59% | 2.15% | 2.18 | 485.74M | 89.82% |
| TXN | 275.74 | 41.95 | 26.98 | 0.89 | +20.54% | 1.73% | 1.80 | 910.89M | 89.27% |
| AVGO | 389.28 | 64.80 | 19.92 | 0.35 | +68.65% | 1.47% | 2.65 | 4.67B | 78.73% |
| MTSI | 251.44 | 109.02 | 36.27 | 1.05 | +37.87% | 2.97% | 1.20 | 68.97M | 97.80% |
| LSCC | 124.27 | 875.14 | 52.31 | 1.10 | +30.87% | 3.52% | 2.21 | 135.79M | 101.05% |
| SLAB | 217.50 | — | 49.07 | — | +55.28% | 9.10% | 6.82 | 32.23M | 91.74% |
| CRUS | 129.35 | 16.49 | 13.69 | — | +7.01% | 6.56% | 5.30 | 50.16M | 103.87% |
| MXL | 66.82 | — | 25.87 | 0.22 | +54.15% | 4.58% | 0.84 | 84.56M | 83.52% |
| SITM | 535.20 | — | 48.42 | 0.65 | +39.00% | 5.29% | 1.69 | 18.76M | 87.60% |
| SMTC | 117.82 | — | 30.64 | 0.59 | +44.63% | 7.03% | 1.84 | 92.65M | 107.26% |
| RMBS | 91.03 | 41.67 | 24.27 | 1.03 | +23.60% | 4.26% | 1.52 | 107.61M | 104.46% |
| ALGM | 41.50 | 552.60 | 27.68 | 0.49 | +45.53% | 10.05% | 4.18 | 124.99M | 75.38% |

**Where SWKS sits in the group — three findings:**

1. **Cheapest forward multiple in the cohort but one.** Fwd P/E **12.63** vs a
   group median of ~**25.9**; only QRVO (11.36) is cheaper — and QRVO's price is
   pinned to SWKS's by the exchange ratio, so that is not an independent
   observation.
2. **The only name in the group with NEGATIVE expected EPS growth alongside QCOM.**
   **EPS Next Y −2.20%** against a cohort where 13 of 17 names expect **+20% or
   better**. **SWKS is cheap because it is not growing.** This is the single
   clearest fundamental statement in the phase.
3. **★ Short float 21.93% — a massive outlier.** Next highest is ALGM at 10.05%,
   then SLAB 9.10%, then **QRVO at 8.02%**. SWKS is **2.2× the second-highest** and
   **~5× the cohort median (~4.3%)**. On a 149.81M float that is **≈32.9M shares
   short, 5.77 days to cover.**

**The short interest is almost certainly mechanical, not a bearish view.**
`phase-6-macro.md` established that the standard merger arb is **long QRVO / short
0.960 SWKS**. That structure produces exactly the observed pattern: a very large
SWKS short *and* an elevated QRVO short (8.02%, from the shorter leg of hedge
unwinds and the reverse trade), with both names' short ratios ~5.4–5.8 days while
the rest of the cohort sits at 1–3 days. **This is the quantification of the arb
overhang that phases 6 and 7 could only infer.** It is handed to phase 7c as its
primary input.

*(Note `Inst Own` of 112.87% for SWKS — above 100% — is itself a signature of
heavy shorting: shares lent and re-reported by both lender and borrower. Several
peers show the same, but SWKS is the highest.)*

## Red flags

1. **★ EPS declining on flat revenue.** `epsGrowthTTMYoy` **−6.00%** vs
   `revenueGrowthTTMYoy` **+2.33%**; actual quarterly EPS 1.76 → 1.54 → 1.15 →
   1.08. Operating margin **9.09% TTM / 7.37% in the latest half**. **ROE 6.30%.**
2. **★ Deteriorating forward view.** Consensus **EPS Next Y −2.20%** (only QCOM is
   also negative in a 17-name cohort where most expect >+20%); Q4 EPS guide **$1.27
   vs $1.29 consensus**; GM guided **down** to 44–45%; **KeyBanc → Sector Weight**
   (2026-07-14) and **Stifel PT → $70** (2026-07-29); consensus **Hold**
   (16 of 24 analysts).
3. **★ Leverage step-up + income-base eviction.** ~**$2B** new debt turns ~$417M
   net cash into ~**$1.6B net debt** (D/E 0.17 → ~0.52), into a 10-year that rose
   +24bp. The **dividend was eliminated outright** — a **4.56% TTM yield** with a
   **91.35% payout** — which consumed **69.5% of half-year FCF** and whose holders
   are now forced sellers on mandate, not on view.
4. **Customer concentration into a contracting end market.** KeyBanc's stated
   rationale: *"new content gains are likely to be offset by a contracting
   smartphone market"* and *"persistent reliance on a single large smartphone
   customer."* `phase-0.5-context.md` recorded that customer (AAPL) falling
   **−7.35%** on the as-of date.
5. **Goodwill at $2,176.7M = 37.8% of equity**, with more to be added by the Qorvo
   purchase accounting. Impairment is a live tail risk if the combination
   under-delivers on its **$500M+** guided synergies.
6. **Insider data is two months stale.** No MSPR rows for 2026-06 or 2026-07 —
   exactly the pre-print window in which a syndicated headline alleged insider
   sales. Not disproven; simply unobserved.

**Not red flags, and worth stating explicitly:** liquidity (current ratio 2.38),
FCF generation ($306.9M in a half, 6.5% annualised yield), the beat record (4/4),
capex discipline (7.0% of revenue), and insider sentiment (no negative month in
the trailing year).

## Tool / source calls (audit trail)

| # | Endpoint / command | Result ← path | Status |
|---|---|---|---|
| — | Preflight | `FINNHUB_API_KEY` **set** (from repo `.env`); `SWKS` **US, no dot suffix**; `fz --version` **ok** | pass |
| 1 | `curl .../stock/metric?symbol=SWKS&metric=all` | peTTM 25.9453, peNormalizedAnnual 19.6425, pbAnnual 1.9878, psTTM 2.3172, **pegTTM null**, currentRatioQuarterly 2.3756, longTermDebt/equityQuarterly 0.0861, totalDebt/totalEquityQuarterly 0.1728, roeTTM 6.3, roaTTM 4.6, grossMarginTTM 41.07, operatingMarginTTM 9.09, netProfitMarginTTM 8.93, **revenueGrowthTTMYoy 2.33**, **epsGrowthTTMYoy −6**, beta 1.5057, 52WeekHigh 90.9, 52WeekLow 51.93 ← `.metric.*` | **200** |
| 2 | `curl .../stock/earnings?symbol=SWKS&limit=8` | **4 rows** (not 8); all `period` ≤ 2026-06-30 ≤ as-of ⇒ **look-ahead guard: 0 rows dropped**. surprisePercent 4.2974 / 9.0771 / 7.9944 / 23.6476; actual 1.08 / 1.15 / 1.54 / 1.76 ← `.[].surprisePercent`, `.[].actual` | **200** |
| 3 | `curl .../stock/eps-estimate?symbol=SWKS&freq=quarterly` | **`{"error":"You don't have access to this resource."}`** | **paid, skipped** |
| 4 | `curl .../stock/revenue-estimate?symbol=SWKS&freq=quarterly` | **`{"error":"You don't have access to this resource."}`** | **paid, skipped** |
| 5 | `curl .../stock/peers?symbol=SWKS` | `["MTSI","LSCC","SITM","SMTC","RMBS","SWKS","QRVO","ALGM","SLAB","CRUS","MXL","RGTI","NVDA"]` — self dropped, RGTI/NVDA excluded as non-comparable | **200** |
| 5b | `fz screen --tickers SWKS,QRVO,QCOM,… --view valuation` / `--view ownership` | **17 of 17 rows each**. SWKS: P/E 32.26, Forward P/E **12.63**, EPS Next Y **−2.20%**, **Short Float 21.93%**, **Short Ratio 5.77**, **Float 149.81M**, Inst Own 112.87% ← `.[] \| {Ticker,…}` `[FUND:peer_pe fz]` | **ok** |
| 5b′ | `fz screen --filter ind_semiconductors --view valuation/ownership` | Returned only the **first 20 names alphabetically** (ADI…GSIT) — SWKS absent. **Abandoned in favour of the explicit `--tickers` form above.** | partial |
| 6 | `curl .../stock/insider-sentiment?symbol=SWKS&from=2025-07-31&to=2026-07-31` | 6 rows; in-window: 2025-09 mspr **100**, 2025-11 **42.06016**, 2026-02 **0**, 2026-05 **33.686752** ← `.data[].mspr`. **2 rows returned BEFORE the `from` date** (2025-02, 2025-05) — over-return noted, excluded from the verdict | **200** |
| 6b | `fz insider-clusters --days 30 --min-buyers 2 --side buy` / `--side sell` | SWKS **absent from both**. Only market-wide buy cluster: XAIR (`DistinctOwners` 2, `Transactions` 2) ⇒ `insider_cluster: {present:n}` `[FUND:insider_cluster fz]` | **ok** |
| 6c | `fz quote SWKS --json \| jq '{recom, target}'` | **`{"recom":null,"target":null}`** — the degraded 14/84-field quote (`phase-0-intake.md`). Cross-source **unavailable from `fz`** | **degraded** |
| 6c′ | WebSearch (fallback for 6c) | Consensus **Hold**, avg PT **$74.72**; 1 SB / 4 B / **16 H** / 3 S; KeyBanc → **Sector Weight** 2026-07-14; Stifel PT → **$70** 2026-07-29 `[FUND:recom WebSearch:dailypolitical.com, gurufocus.com, seekingalpha.com]` | **ok** |
| 7 | `curl .../stock/financials-reported?symbol=SWKS&freq=quarterly` | **200 — NOT paid-tier on this key.** 48 periods; latest ≤ as-of = **2026-04-03** (filed 2026-05-05). `bs`: Cash 1,413.3M, Inventory 885.6M, Goodwill 2,176.7M, Total assets 7,896.0M, current LTD 499.9M, LTD 496.7M, Total liabilities 2,130.3M, Equity 5,765.7M. `cf`: OCF 445.8M, capex 138.9M, dividends paid 213.2M, buyback 7.5M. `ic`: revenue 1,979.1M, GP 812.6M, R&D 415.7M, op income 145.9M, net income 114.8M, diluted EPS 0.76, diluted shares 150.5M ← `.data[0].report.{bs,cf,ic}[]` | **200** |

## Tool / source errors

- `/stock/eps-estimate` → **`{"error":"You don't have access to this resource."}`**
  (verbatim) — **paid tier, skipped.** Not retried; no substitute fabricated.
- `/stock/revenue-estimate` → **`{"error":"You don't have access to this
  resource."}`** (verbatim) — **paid tier, skipped.**
- `fz quote SWKS` → `Recom` and `Target Price` both **null** (the persistent 14/84
  field degradation from `phase-0-intake.md`). The D6 analyst cross-source could
  **not** be run from `fz`; WebSearch was used instead and is labelled as such.
- `fz screen --filter ind_semiconductors` → returned only the **first 20 tickers
  alphabetically**, so neither SWKS nor most of the intended cohort appeared.
  Not an error state, but the `--filter` form is **unusable for a named-peer
  comparison**; re-run with explicit `--tickers`, which returned all 17.
- `/stock/insider-sentiment` → returned **2 rows before the requested `from`
  date** (2025-02, 2025-05). Window over-return, matching the phase's warning.
  Rows are displayed but **excluded from the verdict**.
- `/stock/earnings` → returned **4 rows against `limit=8`**. Not an error; Finnhub
  simply holds 4 quarters for this symbol. The 8-quarter table the phase template
  requests **cannot be produced** and is presented as 4.
- No paid data was purchased. No endpoint was retried after a 403.

## DATA NOTE / CORRECTION

1. **★ `Shs Float` recovered — `phase-0-intake.md`'s "unavailable" is superseded.**
   Phase 0 recorded `Shs Float: n/a` because `fz quote` parses only 14 of 84
   fields. The **`fz screen --tickers … --view ownership`** path returns it
   cleanly: **Float 149.81M**, and the number is corroborated to within 0.5% by two
   independent sources already in this run — Finnhub's reported **diluted share
   count of 150.5M** (2026-04-03 10-Q) and the **150,956,637** derived in
   `phase-2-dark-pool.md` from `marketcap / close`. **Consequence: the
   float-normalised percentages in phases 2 and 3 stand essentially unchanged** —
   e.g. the two-session dark-pool absorption is **573,766 / 149.81M = 0.383%** (vs
   0.380% reported), and the largest OI build is **0.0031%** (vs 0.0030%). Nothing
   downstream needs revising, and the phase-2/3 caveat "true float % is higher" is
   now resolved as **negligible**.
2. **★ `Short Float` recovered — 21.93%.** Also previously recorded as unavailable
   in `phase-0-intake.md`. This is **phase 7c's input, surfaced here** because the
   D3 peer-breadth recipe is what recovered it. Flagged in the verdict block.
3. **Two P/E values are reported side by side and neither is adopted** (Finnhub
   25.95 vs `fz` 32.26). Both reconcile to the same $62.28 price, so the difference
   is an EPS-basis definition, not a stale-price artifact. Recorded rather than
   silently choosing one.
4. **The `fz` `Ticker` field is corrupted by a duplicated first character**
   (`SSWKS`, `AADI`, `QQRVO`). Detected in `phase-0-intake.md` and confirmed here
   across all 17 rows. Every row was re-keyed by stripping a doubled leading
   character and then **validated against an independent price** already in this
   run (e.g. `AADI` → ADI at 367.41 = the ADI close in `phase-0.5-context.md`;
   `SSWKS` → SWKS at 62.28). No row was matched on the ticker string alone.
5. **The 8-quarter surprise table is 4 quarters.** Reported as returned; the
   beat-rate is stated as **4/4**, not extrapolated.
6. **Look-ahead guard passed with nothing to drop.** All 4 earnings periods and the
   latest financial report (2026-04-03, filed 2026-05-05) precede the as-of date.
   The FQ3 10-Q — filed **2026-08-05**, after as-of — is **correctly absent** from
   the 48-period series. The FQ3 *results* quoted (revenue $935M, EPS $1.08) come
   from the **2026-07-28 press release**, which is at/before as-of and therefore
   legitimate.

## Verdict for downstream

```
fundamental_signal:  NEUTRAL
tier_adjustment:     CAUTION
contradiction_count: 1
insider_cluster:     {present: n, distinct_buyers: n/a, side: n/a}
key_risks:
  - "EPS shrinking on flat revenue: epsGrowthTTMYoy -6.00% vs revenueGrowthTTMYoy
     +2.33%; ROE 6.30%; op margin 9.09% TTM / 7.37% latest half; Q4 GM guided down
     to 44-45%. Consensus EPS Next Y -2.20% -- the only negative in a 17-peer
     cohort besides QCOM, where 13 of 17 expect >+20%."
  - "Leverage step-up + income-base eviction: ~$2B new debt turns ~$417M net cash
     into ~$1.6B net debt (D/E 0.17 -> ~0.52) into a 10y that rose +24bp; the 4.56%
     dividend (91.35% payout, 69.5% of half-year FCF) was ELIMINATED, making the
     income holder base forced sellers on mandate rather than on view."
  - "Single-customer concentration into a contracting smartphone market -- KeyBanc's
     explicit 2026-07-14 downgrade rationale; consensus now Hold (16 of 24), avg PT
     $74.72, Stifel cut to $70 on 2026-07-29."
```

**Contradiction accounting** — flow bias from phases 1–7 is **MIXED with a
constructive tilt** (phase 2's +573,766-share two-session absorption is the
strongest single signal; phases 1, 3, 5 and 7 are neutral-to-thin; phase 6 is a
headwind). Scored against the three quality axes:

| Axis | Reading | Contradicts flow bias? |
|---|---|---|
| **earnings_trend** | Beat rate **4/4 (100%)**, avg surprise **+11.26%** — but actual EPS 1.76→1.08, forward consensus **−2.20%**, Q4 guide below, two PT cuts | **NO — SPLIT.** The realised record is spotless; the phase's own guidance ("*a single bad quarter is not a trend*") argues against counting a forward *view* as a contradiction over a perfect *realised* record. Both halves recorded for phase 8b to contest. |
| **insider_MSPR** | +100.00, +42.06, 0, +33.69 — **no negative month in the trailing year**; **no sell cluster** | **NO — CONFIRMS** (weakly: small absolute size, 0.06% of float, and two months stale) |
| **growth/margins** | Revenue **+2.33%**, EPS **−6.00%**, ROE **6.30%**, op margin **9.09%**, GM guided **down** | **YES — CONTRADICTS** |

**⇒ `contradiction_count = 1` ⇒ `tier_adjustment: CAUTION` ⇒ phase 9 cuts one size
step.** A `VETO` requires ≥2 axes and is **not** warranted: the insider axis is
clean, the beat record is perfect, the balance sheet is strong today, and FCF
conversion is healthy. Equally, `CONFIRM` is **not** warranted: the phase's own
heuristic states a cheap multiple alone is not CONFIRM, and here the cheap forward
multiple (12.63×) is explicitly **explained by negative expected growth**.

**Explicitly noted per the phase's constraint — this gate can only cut, never
raise.** The genuinely positive findings (100% beat rate, net cash, positive
insider MSPR, 6.5% FCF yield, forward P/E half the peer median) are recorded but
**do not add conviction** to any long thesis.

**★ Two hand-offs that matter more than the gate itself:**

1. **To phase 7c — `Short Float 21.93%`, `Short Ratio 5.77`, `Float 149.81M`
   (≈32.9M shares short), `Inst Own 112.87%`.** This is **2.2× the second-highest
   peer** and **~5× the cohort median**, and it is almost certainly the **merger-arb
   short** (long QRVO / short 0.960 SWKS) that `phase-6-macro.md` inferred and
   `phase-7-insights.md` could only guess at — corroborated by QRVO's own elevated
   8.02% and by both names carrying ~5.4–5.8 days-to-cover against a cohort at 1–3.
   **This single number likely explains the dark-pool sell prints, the
   `dp_distribution` factor, and the flat tape on the day AAPL fell 7.35%.**
   Phase 7c must decide whether it is a **coiled spring** (deal approval ⇒ arbs
   cover ⇒ squeeze) or a **standing overhang**, and phase 8b must debate it.
2. **To phases 8/8b/9 — the analyst gap left open by `phase-7-insights.md` is now
   filled**, and the answer is that **Wall Street and the options tape agree on
   apathy**: consensus **Hold** (16 of 24 analysts) with an average target of
   **$74.72 (+20.0%)** and active downgrades, against an options tape that is
   **net short premium on both legs**. Nobody with a view is expressing it
   directionally. Any phase-9 thesis must therefore rest on **flow mechanics and
   the merger**, not on a fundamental re-rating — because no constituency is
   currently underwriting one.
