# Phase 7b — Deep Fundamentals & Quality Veto (FINNHUB)

**Ticker:** ENPH · **Sector:** Technology / **Industry:** Solar
**As-of date:** 2026-07-29
**Generated:** 2026-07-30T03:08:00Z
**Upstream phases cited:** `phase-0-intake.md`, `phase-0.5-context.md`, `phase-1-flow.md`, `phase-3-positioning.md`, `phase-5-historical.md`, `phase-6-macro.md`, `phase-7-insights.md`

## Summary

**The business is deteriorating on the axes that matter for a bearish thesis, and the gate
still lands on CAUTION rather than CONFIRM — for one specific, weak reason.**

Two of three fundamental axes **confirm** the phases 1–7 bearish bias.
**Growth is collapsing:** `revenueGrowthQuarterlyYoy` **−20.55%**, `pegTTM` **−5.45**
(negative because earnings are shrinking), `operatingMarginTTM` only **6.86%**, and ENPH's own
guidance calls for a **−22%** decline in 2026 US residential additions
(`phase-6-macro.md` §G). **The earnings trend has broken:** EPS ran **0.90 → 0.71 → 0.47 →
0.46** across the last four reported quarters — **−49%** — and the beat magnitude decayed
monotonically **+36.28% → +19.67% → +12.17% → −1.67%**, i.e. **Q2 2026 was the first MISS in
four quarters** on Finnhub's own actual-vs-estimate basis.

**The one contradiction is insider sentiment, and it is thin.** MSPR's two most recent months
are **+96.66 (2026-05)** and **+77.60 (2026-06)**, both above the spec's |MSPR| > 30
strong-signal threshold, with a 6-month mean of **+23.03**. Mechanically that contradicts a
bearish thesis → **contradiction_count = 1 → `tier_adjustment` CAUTION** (cut one size step).
But the ratio is blind to size: over those same six months insiders were **net sellers of
178,209 shares**, because one −100 month (**2026-03, −206,089 shares**) dwarfs every buy
month combined — June's "bullish" +77.60 rests on **4,851 shares (~$170k)**. And `fz`
`insider-clusters` finds **no ENPH cluster on either side**. The contradiction is real by the
rubric and weak in substance; §D states both.

**This is a genuine, data-driven downgrade of the veto from the prior run.** The 07-27
blueprint recorded `fundamentals: VETO` built on *"a 4/4 beat rate into a −11.76pp
gross-margin collapse"* — a beat streak contradicting a bearish tape. **That streak has now
broken.** With Q2 a −1.67% miss, the earnings axis flipped from *contradicting* the bearish
thesis to *confirming* it, moving the gate **VETO → CAUTION**.

**The honest counterweight to the short — and it is substantial.** The balance sheet is
strong: `currentRatioQuarterly` **3.799**, **$930.6M** of cash plus marketable securities
against **$481.8M** current liabilities, and Q1 2026 free cash flow of **$83.0M**
(OCF $102.9M − capex $19.9M) — roughly a **7.2% annualized FCF yield** on the $4.62B cap.
`Forward P/E` is **15.82**. A shrinking business with a fortress balance sheet and a
high-single-digit FCF yield is a poor short at the bottom of its 30-day range.

**But the valuation is a premium one inside a de-rated group:** ENPH trades at **P/E 34.75**
— second-highest of 18 solar names and **2.7× FSLR's 12.87** — on **P/S 3.48**, near the top
of the industry, while shrinking 20% YoY. And **buybacks are halted: `Repurchases of common
stock` = $0** in Q1 2026, against **−$651.2M** of financing outflows. The historical corporate
bid under this stock is gone.

**Two data gaps must be carried forward, not glossed.** Finnhub's `eps-estimate`,
`revenue-estimate` and `price-target` all return *"You don't have access to this resource"*
(paid tier), and `recommendation-trends` **404s**. Combined with `phase-7-insights.md`'s Yahoo
**HTTP 401** and `fz quote`'s degraded `Recom`/`Target Price` (both `null`), **all four
analyst routes are exhausted — the analyst leg is UNMEASURED for this run**, not neutral.
Separately, **Finnhub's peer list for ENPH is wrong** — it returns semiconductor-equipment
names (MKSI, ENTG, ONTO, AMKR, AMAT…) — so the peer comparison in §H was rebuilt from an
`fz` Solar-industry screen.

## Key signals

- **`revenueGrowthQuarterlyYoy` −20.55%** (TTM −1.64%), `pegTTM` **−5.45**,
  `operatingMarginTTM` **6.86%** [FUND:metric]
- **EPS 0.90 → 0.71 → 0.47 → 0.46 (−49% over 4 quarters); Q2 2026 a −1.67% MISS** — the
  first in four, with beat magnitude decaying +36.28% → +19.67% → +12.17% → −1.67%
  [FUND:earnings_surprises]
- **MSPR 2026-05 +96.66 / 2026-06 +77.60, 6-month mean +23.03 — but net −178,209 shares
  sold** over the same window [FUND:insider_sentiment]
- **`currentRatioQuarterly` 3.799; $497.5M cash + $433.1M securities = $930.6M liquid**
  vs $481.8M current liabilities [FUND:financials_reported]
- **Q1 2026 FCF $83.0M** (OCF $102.9M − capex $19.9M) ≈ **7.2% annualized yield** on a
  $4.62B cap [FUND:financials_reported]
- **`Repurchases of common stock` = $0**; `Net cash used in financing` **−$651.2M**
  [FUND:financials_reported]
- **P/E 34.75 — 2nd highest of 18 solar names, 2.7× FSLR's 12.87**; P/S 3.48;
  Forward P/E 15.82 [FUND:peer_pe fz]
- **Short Float 17.94% — 5th of 18 in the industry, and essentially identical to SEDG's
  17.97%**; `Short Ratio` only **3.05 days** [FUND:peer_si fz]
- **`fz insider-clusters`: no ENPH cluster either side** (buy n=0 market-wide, sell n=4
  clusters without ENPH) [FUND:insider_cluster fz]
- **All four analyst routes dead** — Finnhub estimates/target paid, `recommendation-trends`
  404, Yahoo 401, `fz` `Recom` null → **analyst leg UNMEASURED** [FUND:analyst_unavailable]
- **Finnhub `peers` returns semiconductor-equipment names for ENPH** — peer set rebuilt from
  `fz --filter ind_solar` [FUND:peers]

## Detailed findings

### A — Valuation

`curl .../stock/metric?symbol=ENPH&metric=all` → `.metric` (129 fields returned):

| Metric | Value |
|---|---|
| `peTTM` | **35.4594** |
| `peNormalizedAnnual` | 27.8094 |
| `pbAnnual` | 3.8583 |
| `psTTM` | 3.4197 |
| **`pegTTM`** | **−5.44534** |
| `beta` | 1.6940817 |
| `52WeekHigh` / `52WeekLow` | 73.74 / 25.775 |

> **Point-in-time caveat (spec pitfall).** Finnhub `/stock/metric` ratios are **TTM-current**,
> not strictly point-in-time. Cross-referenced against the as-of price: spot **35.07**
> (verified two ways, `phase-0-intake.md`), and `fz`'s independent trailing **P/E 34.75**
> (§H) sits within 2% of Finnhub's 35.4594 — so the multiple is not materially contaminated at
> this as-of date. `52WeekHigh` 73.74 / `52WeekLow` 25.775 match the screener parquet exactly
> (`phase-0.5-context.md`), a useful consistency check.

**`pegTTM` −5.45 is the single most informative valuation number here.** A negative PEG means
the growth denominator is negative — earnings are **shrinking**, so the PEG framework does not
apply and the trailing P/E of 35.46 has no growth to amortise it. Against that, `Forward P/E`
**15.82** (§H) implies the market expects EPS to roughly double off the trailing base, which
is a demanding assumption for a business guiding **−22%** volume (`phase-6-macro.md` §G).

`pbAnnual` 3.86 cross-checks against the balance sheet: market cap $4.62B ÷ `Total
stockholders' equity` $1,102.4M = **4.19** (§E). The gap is a timing artifact (equity is as of
2026-03-31, price as of 2026-07-29); both indicate ENPH trades at ~4× book.

`beta` **1.694** corroborates `fz`'s 1.65 (`phase-5-historical.md` §G) — a high-beta name into
`phase-6-macro.md`'s TRANSITIONAL/CHOPPY regime.

### B — Growth profile

| Metric | Value |
|---|---|
| **`revenueGrowthQuarterlyYoy`** | **−20.55%** |
| `revenueGrowthTTMYoy` | −1.64% |
| `epsGrowthTTMYoy` | −3.77% |
| `epsGrowthQuarterlyYoy` | **null** |
| `grossMarginTTM` | 45.34% |
| **`operatingMarginTTM`** | **6.86%** |
| `netProfitMarginTTM` | 9.64% |
| `roeTTM` | 13.28% |
| `roaTTM` | 4.24% |

**The TTM-versus-quarterly gap is the whole story.** Revenue is down only **−1.64% on a TTM
basis** but **−20.55% in the latest quarter year-over-year** — the deterioration is recent,
steep, and accelerating, so the TTM figure flatters it badly. My independent derivation in
`phase-6-macro.md` §G (revenue $291.9M against a carried consensus basis of −19.6% YoY) gives
≈**−19.7%**, corroborating the −20.55% from a different source.

**Margins are thinner than the headline suggests.** `grossMarginTTM` 45.34% is respectable and
close to the reported Q2 non-GAAP 46.8% (`phase-6-macro.md` §G, different basis), but
`operatingMarginTTM` is only **6.86%** — so operating leverage is minimal, and a 20% revenue
decline flows almost directly to operating income.

**`netProfitMarginTTM` 9.64% EXCEEDS `operatingMarginTTM` 6.86%** — a 2.78pp gap that means
**material non-operating income**. The balance sheet explains it: **$930.6M** of cash and
marketable securities (§E) at prevailing short rates (`SOFR` 3.65%, `phase-6-macro.md` §D)
generates roughly **$34M/yr** of interest income. **A meaningful share of ENPH's reported
profitability is interest on its cash pile, not operations.** That matters two ways: it makes
the earnings base more durable than the operating trend implies (a genuine floor under the
short), and it means the *operating* business is closer to break-even than a 9.64% net margin
suggests.

**Q3 guidance** (`phase-6-macro.md` §G): revenue **$290–320M** — *above* the $280–310M the
07-27 run carried — with non-GAAP GM **44–47%** versus Q2's 46.8% actual, i.e. **revenue guide
up, margin guide flat-to-down.**

### C — Earnings-surprise history

`curl .../stock/earnings?symbol=ENPH&limit=8` returned **4 quarters**, not 8. **Look-ahead
guard applied and clean:** all four `period` values are ≤ the 2026-07-29 as-of date; zero rows
were dropped.

| Period | Actual EPS | Estimate | Surprise | Surprise % |
|---|---:|---:|---:|---:|
| **2026-06-30** | **0.46** | **0.4678** | **−0.0078** | **−1.67%** |
| 2026-03-31 | 0.47 | 0.4190 | +0.0510 | +12.17% |
| 2025-12-31 | 0.71 | 0.5933 | +0.1167 | +19.67% |
| 2025-09-30 | 0.90 | 0.6604 | +0.2396 | +36.28% |

**Beat-rate: 3 of 4 (75%) — but the trajectory is what matters, and it is unambiguous.**

1. **EPS fell 0.90 → 0.71 → 0.47 → 0.46: −49% across four quarters**, declining every single
   quarter without exception.
2. **Beat magnitude decayed monotonically: +36.28% → +19.67% → +12.17% → −1.67%.** This is
   the textbook signature of estimates finally catching down to a deteriorating business, and
   then overshooting it.
3. **Q2 2026 is the first MISS in the available history.**

> **An important discrepancy I must surface rather than resolve silently.** Finnhub reports Q2
> `actual` **0.46** against `estimate` **0.4678** — a **−1.67% miss**. The press coverage in
> `phase-6-macro.md` §G reports *"adjusted earnings of 47 cents per share, beating estimates
> of 46 cents."* **Both are accurate on their own basis**; they differ on the adjusted-EPS
> definition and the consensus vintage. **Neither is "the" answer, and the direction of the
> gate does not hinge on it** — a +1c beat and a −0.8c miss are both a *flat quarter against
> expectations*, and the four-quarter −49% EPS trend is identical under either basis. Phase 8
> agents and phase 8b must not treat "ENPH beat" or "ENPH missed" as a settled fact; the
> settled fact is **EPS roughly halved in a year and the beat cushion is gone.**

### D — Insider signal

`curl .../stock/insider-sentiment?symbol=ENPH&from=2025-07-29&to=2026-07-29` → `.data`.
**Look-ahead guard applied: 0 rows dated after 2026-07** (verified by filtering
`(.year*100+.month) > 202607` → length 0).

| Month | MSPR | Share change |
|---|---:|---:|
| 2025-08 | +100.00 | +5,000 |
| 2025-09 | −100.00 | −1,319 |
| 2025-10 | +100.00 | +10,000 |
| 2025-11 | +100.00 | +5,000 |
| 2025-12 | −100.00 | **−157,319** |
| 2026-01 | +100.00 | +135,960 |
| 2026-02 | +63.93 | +3,900 |
| **2026-03** | **−100.00** | **−206,089** |
| 2026-04 | *(no data)* | — |
| **2026-05** | **+96.66** | +40,488 |
| **2026-06** | **+77.60** | +4,851 |
| **Last 6 available** | **mean +23.03** | **net −178,209** |

(Earlier rows in the returned window: 2025-01 +100 / +99,000; 2025-03 −100 / −132,881;
2025-04 +100 / +4,000; 2025-05 +100 / +31,488; 2025-06 −100 / −1,319.)

**This axis is the sole contradiction to the bearish thesis, and it is weak. Both facts
belong on the record:**

- **By MSPR, the signal is bullish.** The two most recent months — **+96.66** and **+77.60** —
  are both well beyond the spec's |MSPR| > 30 strong-signal threshold, and the 6-month mean is
  **+23.03**. Per the rubric this **contradicts** a bearish flow bias.
- **By share count, insiders were net sellers of 178,209 shares** over the same six months.
  MSPR is a *ratio* and is blind to size: the single **2026-03** month at **−206,089 shares**
  (roughly $9M at then-prevailing prices) outweighs every buy month combined, and the
  "strongly bullish" **2026-06 +77.60 rests on 4,851 shares — about $170k**, which for a
  company with 2,872 employees and $4.62B of market cap is immaterial.
- **MSPR is also extremely bimodal** — 11 of 15 months print exactly ±100, which is what
  happens when a month contains a single transaction. This is a low-information series for
  ENPH, not a smooth sentiment gauge.

**`fz` insider clusters (D5):** `fz insider-clusters --days 30 --min-buyers 2 --side buy`
returned **0 rows market-wide**; `--side sell` returned **4 clusters, none of them ENPH**
(null-safe select → `null`). So there is **no clustered insider conviction in either
direction** — no buy cluster to sharpen a CONFIRM, and no sell cluster to sharpen a VETO. Per
the spec, the absence of insider activity is *itself a weak signal* and must not be read as
bullish.

**Net assessment: counted as 1 contradiction (the conservative direction, since 7b is
downside-only and a bullish insider read cuts the short's size), while flagging that the
underlying evidence is a bimodal ratio built on a handful of tiny transactions against a
six-month net sale.**

### E — Balance-sheet health

`curl .../stock/financials-reported?symbol=ENPH&freq=quarterly` **succeeded — not paid-tier
on this key.** Latest filing at or before the as-of date: **2026 Q1, form 10-Q, period
2026-01-01 → 2026-03-31, filed 2026-04-28.**

> **Look-ahead and staleness note.** The **Q2 (period ending 2026-06-30) 10-Q is not yet in
> the dataset** — the Q2 earnings release was 2026-07-28 and the filing follows. So the
> balance sheet and cash flow below are as of **2026-03-31, roughly four months stale**, and
> predate the quarter just reported. That is the correct as-of-safe choice (no look-ahead), but
> phase 9 must know these figures do not reflect the Q2 print.

| Line item | 2026-03-31 |
|---|---:|
| Cash and cash equivalents | **$497,546,000** |
| Marketable securities | **$433,095,000** |
| **Total liquid** | **$930,641,000** |
| Inventory | $290,701,000 |
| Total current assets | $1,830,271,000 |
| Total assets | $2,723,923,000 |
| Total current liabilities | **$481,783,000** |
| Total liabilities | $1,621,571,000 |
| **Total stockholders' equity** | **$1,102,352,000** |

**Derived:**

- **Current ratio = 1,830,271 / 481,783 = 3.80** — matches Finnhub's
  `currentRatioQuarterly` **3.799** exactly. Independent confirmation.
- **Liquid assets ($930.6M) cover current liabilities 1.93×** on cash and securities alone.
- **Non-current liabilities = 1,621,571 − 481,783 = $1,139,788,000.** Predominantly
  convertible notes. Against $930.6M liquid, that is roughly **−$209M net debt** — close to
  net-cash-neutral.
- Liabilities/equity = 1,621.6 / 1,102.4 = **1.47** (total liabilities, not debt-only —
  Finnhub returned `longTermDebt_equityQuarterly` and `totalDebt_totalEquityQuarterly` as
  **null**, so a clean debt/equity is unavailable from either source).
- Market cap $4.62B ÷ equity $1,102.4M = **P/B 4.19**.

**Verdict: the balance sheet is genuinely strong and is the most important argument AGAINST a
short.** A 3.80 current ratio, $930.6M of liquidity, and approximate net-cash-neutrality mean
there is **no solvency or financing pressure** — ENPH can absorb a multi-year demand trough
without a capital raise. Any bearish thesis must be a **multiple-compression and
demand-erosion** thesis, explicitly **not** a distress thesis.

### F — Cash-flow quality

From the same 2026 Q1 10-Q (`.data[0].report.cf`):

| Line item | Q1 2026 (3 months) |
|---|---:|
| Net cash provided by operating activities | **$102,871,000** |
| Purchases of property and equipment | $19,898,000 |
| **Free cash flow (OCF − capex)** | **$82,973,000** |
| Net cash provided by investing activities | +$576,383,000 |
| **Net cash used in financing activities** | **−$651,186,000** |
| **Repurchases of common stock** | **$0** |
| Purchases of PP&E through tenant improvement allowance | $0 |
| Purchases of PP&E included in accounts payable | $12,044,000 |

**Three findings, pulling in different directions:**

1. **FCF is solidly positive: $83.0M in one quarter.** Crudely annualized (**×4 — a rough
   proxy from a single quarter, and residential solar is seasonal, so treat as indicative**)
   that is ~**$332M**, a **7.2% FCF yield** on the $4.62B market cap. **Capex intensity is
   low** — $19.9M against $102.9M of OCF is **19%** — consistent with a fabless
   microinverter model. **A 7.2% FCF yield is a hard floor argument against shorting**, and it
   is the strongest fundamental counterweight in this phase.
2. **Buybacks are halted: `Repurchases of common stock` = $0.** ENPH has historically
   repurchased stock; a zero print removes the corporate bid. Read with
   `phase-2-dark-pool.md`'s distribution (`sell_ratio` 0.610) and
   `phase-3-positioning.md`'s zero `position-rolls`, **the marginal buyer of ENPH stock is
   absent from every lane measured in this run — including the company itself.**
3. **−$651.2M of financing outflow funded by +$576.4M of investing inflow.** ENPH liquidated
   marketable securities to meet a large financing obligation — almost certainly convertible
   note repayment/settlement. **Prudent deleveraging, but it consumed the securities balance**
   and is why cash and securities must be read together (§E). It also explains why the buyback
   is zero: cash went to debt, not to shares.

No dividend (`Payout` 0.00%, `Dividend TTM` "-" — `fz`, `phase-0-intake.md`).

### G — Forward consensus

**Unavailable from Finnhub — paid tier.**

| Endpoint | Response |
|---|---|
| `/stock/eps-estimate?symbol=ENPH&freq=quarterly` | `{"error":"You don't have access to this resource."}` |
| `/stock/revenue-estimate?symbol=ENPH&freq=quarterly` | `{"error":"You don't have access to this resource."}` |
| `/stock/price-target?symbol=ENPH` | `{"error":"You don't have access to this resource."}` |
| `/stock/recommendation-trends?symbol=ENPH` | **404 not found** |

Consistent with `memory/data-source-workarounds.md` ("Finnhub estimates are paid — use
WebSearch"). Per orchestration rule 4, no abort — these are marked **paid, skipped** and the
gap is labelled.

**Substituted from company guidance via WebSearch** (`phase-6-macro.md` §G):

| Forward datapoint | Value | Direction |
|---|---|---|
| Q3 2026 revenue guide | **$290–320M** (midpoint $305M) | **UP** vs $280–310M carried; +4.5% QoQ on the midpoint |
| Q3 2026 non-GAAP GM guide | **44–47%** | **flat-to-DOWN** vs 46.8% Q2 actual |
| Q3 IQ Battery shipments | 130–150 MWh | UP vs 113.8 MWh |
| 2026 US resi additions (company) | **−22%** | **DOWN** |

**Forward direction is mixed and I will not force it either way:** the near-term revenue and
battery guides are *up sequentially* and above the previously carried range, while the margin
guide is flat-to-down and the company's own multi-quarter volume outlook is **−22%**. The
sequential improvement is real; it is improvement off a base that fell 20% YoY.

**The analyst leg is UNMEASURED.** All four routes are exhausted: Finnhub estimates and
price-target are paid, `recommendation-trends` 404s, `phase-7-insights.md`'s
`analyst-vs-flow` returned **no analyst block** (Yahoo **HTTP 401**), and `fz quote`'s
`Recom`/`Target Price` are **`null`** (leaf degraded to 14/84 fields,
`phase-0-intake.md`). **Phases 8, 8b and 9 must treat analyst consensus as a blind spot, not
as neutral** — there is no consensus rating, no price target, and therefore no
analyst-vs-flow divergence test available for this run.

### H — Peers: relative-value comparison

> **Finnhub's peer list for ENPH is wrong and was discarded.**
> `/stock/peers?symbol=ENPH` returned
> `["MKSI","ENTG","ONTO","AMKR","FORM","ENPH","ACMR","ACLS","UCTT","VECO","AXTI","ICHR","AMAT"]`
> — **semiconductor capital-equipment names** (MKS Instruments, Entegris, Onto, Amkor, Applied
> Materials…). Not one is a solar company. Finnhub appears to be classifying ENPH by a
> semiconductor SIC code rather than by its actual end market. **Using this list would have
> produced a meaningless relative-value read.** Per the spec's §5b fallback, the peer set was
> rebuilt with a sector/industry screen: `fz screen --filter ind_solar`.

**Solar industry — valuation** (`fz screen --filter ind_solar --view valuation --agent`):

| Ticker | P/E | Fwd P/E | PEG | P/S |
|---|---:|---:|---:|---:|
| SHLS | **39.86** | 15.29 | 0.82 | 2.49 |
| **ENPH** | **34.75** | **15.82** | — | **3.48** |
| NXT | 24.17 | 16.24 | 1.07 | 3.95 |
| **FSLR** | **12.87** | **8.29** | **0.30** | 3.95 |
| RUN | 4.43 | 20.27 | — | 0.71 |
| SEDG | — | 24.96 | — | 1.86 |
| JKS | — | 12.90 | — | 0.08 |
| CSIQ | — | 10.17 | — | 0.17 |
| ARRY | — | 5.30 | 0.34 | 0.61 |
| SPWR | — | 1.06 | — | 0.20 |
| DQ / BEEM / FTCI / SMXT / SPRU / SUNE / ASTI / PN | — | — | — | 0.13–248.98 |

**Solar industry — ownership / short interest** (`--view ownership`):

| Ticker | Float | **Short Float** | Short Ratio | Inst Own | Insider Own | Price |
|---|---|---:|---:|---:|---:|---:|
| CSIQ | 47.58M | **34.53%** | 5.65 | 58.35% | 29.92% | 13.72 |
| RUN | 230.08M | **28.65%** | 6.57 | 108.24% | 3.55% | 9.47 |
| ARRY | 150.96M | 20.39% | 5.04 | 133.75% | 1.86% | 4.81 |
| **SEDG** | 59.76M | **17.97%** | 3.13 | 101.59% | 1.75% | 39.04 |
| **ENPH** | **127.77M** | **17.94%** | **3.05** | **101.05%** | **3.06%** | **35.07** |
| ASTI | 9.78M | 12.67% | 0.84 | 17.02% | 0.37% | 2.79 |
| SUNE | 3.45M | 12.14% | 0.05 | 35.09% | 16.44% | 2.16 |
| BEEM | 21.22M | 11.10% | 1.54 | 11.58% | 4.43% | 0.98 |
| FSLR | 101.48M | 9.75% | 4.06 | 92.85% | 5.55% | 199.24 |
| FTCI | 11.23M | 9.43% | 6.30 | 9.88% | 29.82% | 2.60 |
| SHLS | 164.42M | 8.83% | 2.53 | 109.89% | 2.00% | 7.94 |
| SPWR | 118.85M | 8.15% | 2.51 | 16.25% | 35.07% | 0.30 |
| DQ | 67.28M | 7.11% | 5.02 | 44.41% | 0.57% | 11.97 |
| JKS | 50.26M | 6.81% | 4.42 | 32.18% | 0.01% | 14.58 |
| SPRU | 13.09M | 6.45% | 20.18 | 18.70% | 28.74% | 1.99 |
| NXT | 149.36M | 4.82% | 2.40 | 107.72% | 1.51% | 92.67 |
| SMXT | 41.89M | 1.36% | 0.60 | 3.55% | 26.40% | 0.36 |

*(`fz` returns the `Ticker` field with its first character duplicated — `EENPH`, `FFSLR` —
a cosmetic bug documented in `phase-0-intake.md`. Values are correctly aligned; labels are
corrected above.)*

**Placing ENPH in the group — three conclusions:**

1. **ENPH carries a premium multiple in a de-rated industry while shrinking fastest.** Its
   **P/E 34.75 is second-highest of the 18 names** (only SHLS at 39.86 is higher) and
   **2.7× FSLR's 12.87**; **P/S 3.48** sits at the top of the group alongside FSLR and NXT
   (3.95). Forward P/E 15.82 is mid-pack — but that forward multiple *requires* the EPS
   recovery that §B/§C give little support to, and FSLR offers a comparable business at
   **Fwd P/E 8.29 with PEG 0.30**. **A relative-value investor has cheaper ways to own solar.**
2. **ENPH's short interest is NOT an outlier — it is a sector condition.** At **17.94%**,
   ENPH is 5th of 18 and **effectively tied with SEDG's 17.97%**, well below CSIQ (34.53%),
   RUN (28.65%) and ARRY (20.39%). **This materially tempers any "crowded short = squeeze
   fuel" argument** and phase 7c must weigh it: being shorted like your closest comparable
   is not a distinguishing setup. Reinforcing that, **ENPH's `Short Ratio` is only 3.05
   days** — the shorts can exit in three sessions, versus RUN 6.57, CSIQ 5.65 and ARRY 5.04.
   **A 3-day short base is cheap to cover and therefore weak squeeze fuel.**
3. **Institutional ownership at 101.05% is normal for the group** (RUN 108.24%, SHLS 109.89%,
   NXT 107.72%, SEDG 101.59% — figures above 100% reflect securities lending double-counting).
   `Insider Own` **3.06%** is low but not anomalous. Nothing here distinguishes ENPH.

## Red flags

1. **Revenue −20.55% YoY in the latest quarter**, with the company guiding **−22%** US
   residential additions for 2026 and a **permanent 30% ITC sunset** already in effect
   (`phase-6-macro.md` §G). The decline is **structural and company-confirmed**, not cyclical.
2. **EPS −49% over four quarters (0.90 → 0.46) with the beat cushion exhausted** — beat
   magnitude decayed +36.28% → +19.67% → +12.17% → **−1.67%** (first miss).
3. **Premium valuation into that decline** — P/E 34.75 (2nd of 18, 2.7× FSLR), P/S 3.48,
   `pegTTM` **−5.45**. Multiple-compression risk if the trajectory persists.
4. **Buyback halted — `Repurchases of common stock` = $0** with **−$651.2M** of financing
   outflows. The corporate bid is gone, at the same time as
   `phase-2-dark-pool.md` distribution and zero `position-rolls`.
5. **Thin operating leverage** — `operatingMarginTTM` **6.86%**, and `netProfitMarginTTM`
   9.64% is *flattered by ~$34M/yr of interest income* on the cash pile (§B). The operating
   business is nearer break-even than headline profitability implies.
6. **Insiders net −178,209 shares over six months** despite a positive MSPR mean, with the
   single largest transaction a **−206,089-share sale in 2026-03** and no buy cluster (§D).
7. **Analyst leg entirely unmeasured** (§G) — four independent routes dead. A genuine blind
   spot, not a neutral reading.
8. **`Short Ratio` 3.05 days** — the short base is small relative to volume, which **cuts
   against** any squeeze thesis built on 17.94% short float.

**Not red flags — stated for balance:** current ratio **3.80**, **$930.6M** liquid, roughly
net-cash-neutral, **FCF $83.0M/quarter (~7.2% annualized yield)**, capex intensity only 19% of
OCF, `roeTTM` 13.28%, `Forward P/E` 15.82, Europe revenue **+35%**, and Q3 revenue guided
**above** the prior range. **There is no distress here.**

## Tool / source calls (audit trail)

| # | Source / command | Result | Key value(s) ← path |
|---|---|---|---|
| 0 | Preflight: `test -n "$FINNHUB_API_KEY"`; ticker pattern; `fz --version` | **key set · US ok · fz ok** | `.env`-sourced key |
| 1 | `curl .../stock/metric?symbol=ENPH&metric=all` | **OK** (129 fields) | `peTTM`=35.4594, `pegTTM`=**−5.44534**, `psTTM`=3.4197, `pbAnnual`=3.8583, `currentRatioQuarterly`=**3.799**, `roeTTM`=13.28, `grossMarginTTM`=45.34, `operatingMarginTTM`=**6.86**, `netProfitMarginTTM`=9.64, `revenueGrowthQuarterlyYoy`=**−20.55**, `revenueGrowthTTMYoy`=−1.64, `epsGrowthTTMYoy`=−3.77, `beta`=1.6941, `52WeekHigh`=73.74, `52WeekLow`=25.775; `longTermDebt_equityQuarterly`/`totalDebt_totalEquityQuarterly`=**null** ← `.metric` |
| 2 | `curl .../stock/earnings?symbol=ENPH&limit=8` | **OK** (4 of 8 rows) | 2026-06-30 `actual`=**0.46** / `estimate`=0.4678 / `surprisePercent`=**−1.6674**; 2026-03-31 +12.1718; 2025-12-31 +19.6696; 2025-09-30 +36.281 ← `.[]`. Look-ahead: 0 rows > as-of |
| 3 | `curl .../stock/eps-estimate?symbol=ENPH&freq=quarterly` | **PAID, SKIPPED** | `{"error":"You don't have access to this resource."}` |
| 4 | `curl .../stock/revenue-estimate?symbol=ENPH&freq=quarterly` | **PAID, SKIPPED** | same error |
| 4b | `curl .../stock/price-target?symbol=ENPH` | **PAID, SKIPPED** | same error |
| 4c | `curl .../stock/recommendation-trends?symbol=ENPH` | **404** | `404 not found` |
| 5 | `curl .../stock/peers?symbol=ENPH` | **OK but WRONG SET** | `["MKSI","ENTG","ONTO","AMKR","FORM","ENPH","ACMR","ACLS","UCTT","VECO","AXTI","ICHR","AMAT"]` — semiconductor equipment, **discarded** |
| 5b | `fz screen --filter ind_solar --view valuation --agent` | **OK** (18 rows) | ENPH `P/E`=**34.75** / `Forward P/E`=15.82 / `P/S`=3.48; FSLR 12.87 / 8.29 / PEG 0.30; SHLS 39.86 ← `.[]` |
| 5c | `fz screen --filter ind_solar --view ownership --agent` | **OK** (18 rows) | ENPH `Short Float`=**17.94%** / `Short Ratio`=**3.05** / `Float`=127.77M / `Inst Own`=101.05%; SEDG 17.97%/3.13; CSIQ 34.53%; RUN 28.65% ← `.[]` |
| 6 | `curl .../stock/insider-sentiment?symbol=ENPH&from=2025-07-29&to=2026-07-29` | **OK** (15 months) | 2026-06 `mspr`=**+77.604** / `change`=+4,851; 2026-05 +96.658 / +40,488; 2026-03 **−100** / **−206,089**; last-6 mean **+23.03**, Σ`change`=**−178,209** ← `.data[]` filtered `(.year*100+.month) <= 202607`. Look-ahead: 0 rows > as-of |
| 6b | `fz insider-clusters --days 30 --min-buyers 2 --side buy --agent` | **OK, 0 rows** | ENPH absent ← `[.[]?\|select(.Ticker=="ENPH")]\|.[0]//null` → `null` |
| 6b | `fz insider-clusters --days 30 --min-buyers 2 --side sell --agent` | **OK, 4 rows** | ENPH **absent** ← same null-safe select → `null` |
| 6c | `fz quote ENPH --agent` → `Recom` / `Target Price` | **DEGRADED** | both **`null`** (leaf returns 14/84 fields, `phase-0-intake.md`) |
| 7 | `curl .../stock/financials-reported?symbol=ENPH&freq=quarterly` | **OK — not paid on this key** | 2026Q1 10-Q (2026-01-01→2026-03-31, filed 2026-04-28): `Cash and cash equivalents`=497,546,000; `Marketable securities`=433,095,000; `Total current assets`=1,830,271,000; `Total current liabilities`=481,783,000; `Total liabilities`=1,621,571,000; `Total stockholders' equity`=1,102,352,000; `Net cash provided by operating activities`=**102,871,000**; `Purchases of property and equipment`=19,898,000; **`Repurchases of common stock`=0**; `Net cash used in financing activities`=**−651,186,000** ← `.data[0].report.bs[]` / `.cf[]` |

Every Finnhub and `fz` read was captured to a file before being queried and every value
round-tripped through `jq` on validated JSON; both `insider-clusters` selects used the
null-safe `[…]|.[0]//null` form. **Look-ahead guard applied to both dated series** (earnings
`period`, insider `year`/`month`) and verified to have dropped nothing — and the
`financials-reported` selection deliberately used the **2026Q1** filing because the Q2 10-Q
post-dates the as-of date. Derived values, stated inline: current ratio (§E), total liquid,
non-current liabilities, net debt, P/B, FCF and its annualization, capex intensity, interest-
income estimate, and the MSPR 6-month mean and net share change (§D).

## Tool / source errors

No fatal errors. The Finnhub key was present (repo-root `.env`) and ENPH is a US ticker, so
**no graceful-skip line is required and `tier_adjustment` is NOT `NA`.**

1. **`/stock/eps-estimate`, `/stock/revenue-estimate`, `/stock/price-target` → paid, skipped**
   — all three returned `{"error":"You don't have access to this resource."}`. Consistent with
   `memory/data-source-workarounds.md`. Substituted with company guidance via WebSearch (§G)
   per orchestration rule 4. **No abort.**
2. **`/stock/recommendation-trends` → `404 not found`** (returned an HTML `<a href="/">Found</a>`
   redirect body, not JSON). Not a paid-tier message — the endpoint path appears unavailable.
3. **Analyst leg fully unavailable — four independent routes dead.** Finnhub estimates/target
   (paid), `recommendation-trends` (404), Yahoo via `analyst-vs-flow` (**HTTP 401**,
   `phase-7-insights.md` §F), `fz quote` `Recom`/`Target Price` (**null**, leaf degraded).
   **Recorded as UNMEASURED for phases 8/8b/9 — explicitly not neutral.**
4. **`/stock/peers` returns a wrong peer set for ENPH** — 12 semiconductor-equipment names,
   zero solar. A silent correctness failure (exit 0, valid JSON, plausible-looking tickers)
   that would have produced a meaningless relative-value table. Rebuilt via
   `fz screen --filter ind_solar`. **Candidate note for the phase spec / `lib/fz-recipes.md`
   (propose-only): always sanity-check Finnhub's peer list against the known industry before
   using it.**
5. **`/stock/earnings?limit=8` returned only 4 quarters.** Not an error, but the beat-rate is
   computed on **N=4**, which is a small sample; the spec's own caution that *"a single bad
   quarter is not a trend"* is why §C leans on the four-quarter EPS *trajectory* and the
   monotonic beat-magnitude decay rather than on the single miss.
6. **`financials-reported` latest filing is 2026Q1 (2026-03-31), ~4 months stale**, because
   the Q2 10-Q had not been filed as of the as-of date. Correct as-of-safe behaviour; §E/§F
   figures do **not** reflect the just-reported quarter.
7. **`longTermDebt_equityQuarterly` and `totalDebt_totalEquityQuarterly` both `null`** in
   `/stock/metric`, and the balance-sheet extract surfaced no explicit long-term-debt line —
   so a clean debt/equity ratio is unavailable from either source. §E uses total liabilities
   and a derived non-current-liabilities figure, labelled as such.
8. **`fz` `Ticker` field first-character duplication** persists (`EENPH`, `FFSLR`) — cosmetic;
   labels corrected in §H, values correctly aligned. Do not join on that field.

## Verdict for downstream

```
fundamental_signal:  BEARISH
tier_adjustment:     CAUTION
contradiction_count: 1        # insider_MSPR only; earnings_trend and growth/margins CONFIRM
insider_cluster:     {present: n, distinct_buyers: n/a, side: n/a}
key_risks:
  - "Revenue −20.55% YoY with company-guided −22% 2026 US resi additions and a permanent 30% ITC sunset — structural, not cyclical demand erosion"
  - "Premium multiple in a de-rated group: P/E 34.75 (2nd of 18 solar names, 2.7x FSLR's 12.87), P/S 3.48, pegTTM −5.45 — multiple-compression risk"
  - "SHORT-SIDE RISK: fortress balance sheet (current ratio 3.80, $930.6M liquid, ~net-cash-neutral) plus ~7.2% annualized FCF yield and Fwd P/E 15.82 — a poor short at the bottom of its 30-day range"
```

**Axis-by-axis derivation of `contradiction_count`** (flow bias = **BEARISH**, the plurality
of phases 1–7; `phase-7-insights.md` returns `scenario` DIRECTIONAL_SHORT):

| Axis | Evidence | vs bearish flow bias |
|---|---|---|
| **earnings_trend** | EPS 0.90 → 0.71 → 0.47 → **0.46** (−49% / 4 quarters); beat magnitude +36.28% → +19.67% → +12.17% → **−1.67%** (first miss); Q3 revenue guide *up*, GM guide flat-to-down | **CONFIRMS** |
| **insider_MSPR** | Last two months **+96.66 / +77.60** (both > +30), 6-month mean **+23.03** — *but* net **−178,209 shares**, bimodal ±100 series, no cluster either side | **CONTRADICTS** (weakly) |
| **growth/margins** | `revenueGrowthQuarterlyYoy` **−20.55%**, `pegTTM` **−5.45**, `operatingMarginTTM` **6.86%**, net margin flattered by ~$34M/yr interest income, company guides −22% volume | **CONFIRMS** |

**1 contradiction → `CAUTION` → phase 9 cuts one size step.**

**Why this is a downgrade from the prior run's VETO, and why that is correct.** The
2026-07-27 `decision.json` recorded `fundamentals: VETO`, reasoned on *"a 4/4 beat rate into a
−11.76pp gross-margin collapse"* — a beat streak that **contradicted** the bearish tape. **That
streak broke on 2026-07-28**: Q2 printed a −1.67% miss on Finnhub's basis, and the beat
magnitude has decayed monotonically for four quarters. The earnings axis therefore flipped
from *contradicting* to *confirming* the bearish thesis, taking the count from ≥2 to 1 and the
gate from **VETO → CAUTION**. This is a data-driven change, not a re-interpretation.

**Reminder of this gate's direction (spec rule):** phase 7b is **downside-only — it can only
confirm or cut, never raise conviction.** CAUTION cuts one size step off whatever phases 1–7
and the sizing rubric would otherwise support. It does **not** license a larger short because
two axes confirm.

**What phase 9 must carry beyond the gate:**

- **This is a multiple-compression / demand-erosion thesis, NOT a distress thesis.** Current
  ratio **3.80**, **$930.6M** liquid, approximately net-cash-neutral, **FCF ~$83M/quarter
  (7.2% annualized yield)**, capex only 19% of OCF. **ENPH can fund a multi-year trough
  without a raise.** Any bearish framing that implies balance-sheet risk is wrong and phase 8b
  should attack it.
- **The squeeze-fuel argument is weaker than the 17.94% short float suggests.** ENPH is 5th of
  18 in the industry and **statistically tied with SEDG (17.97%)** — a sector condition, not a
  distinguishing setup — and its **`Short Ratio` is only 3.05 days**, versus RUN 6.57, CSIQ
  5.65, ARRY 5.04. **A 3-day short base is cheap to cover.** Phase 7c must weigh this against
  its crowd-state call.
- **The corporate bid is gone.** `Repurchases of common stock` = **$0** with **−$651.2M** of
  financing outflows, alongside `phase-2-dark-pool.md` distribution and
  `phase-3-positioning.md`'s zero `position-rolls`. **No lane measured in this run shows a
  marginal buyer — including the company.**
- **Two blind spots to state in `decision.json`, not paper over:** (1) the **analyst leg is
  UNMEASURED** — no consensus rating, no price target, no analyst-vs-flow test, after four
  dead routes; (2) the balance sheet and cash flow are as of **2026-03-31 (~4 months stale)**
  and do not reflect the just-reported quarter.
- **The EPS beat/miss basis is genuinely ambiguous** — Finnhub says a −1.67% miss (0.46 vs
  0.4678), the press says a +1c beat ($0.47 vs $0.46). **Phase 8 agents must not assert either
  as settled.** The settled fact is that **EPS roughly halved year-over-year and the beat
  cushion is exhausted.**
