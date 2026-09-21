# Phase 7b — Deep Fundamentals & Quality Veto (FINNHUB)

**Ticker:** ENPH
**As-of date:** 2026-07-27
**Generated:** 2026-07-27T21:55:00-04:00
**Upstream phases cited:** `phase-0-intake.md`, `phase-1-flow.md`, `phase-4-structure.md`, `phase-5-historical.md`, `phase-6-macro.md`, `phase-7-insights.md`

## Summary

**The business is deteriorating badly — and the fundamental gate still vetoes the
directional short.** Those two statements are both true, and reconciling them is
this phase's job.

The deterioration is not in dispute. The Q1'26 10-Q shows **net revenues $282.9M
vs $356.1M a year earlier (−20.6%)**, **gross margin collapsing from 47.25% to
35.49% (−11.8pp)**, and GAAP net income swinging from **+$29.7M to a −$7.4M
loss** — with management guiding a further **~3pp** of tariff margin damage for
Q2. Phase-6 supplied the cause: Section 25D was repealed effective 2025-12-31.

But the flow bias entering this gate is **bearish**, and the rubric asks how many
fundamental axes *contradict* it. Two do. **Earnings trend contradicts:** ENPH has
beaten consensus in **4 of 4** available quarters with a mean surprise of
**+19.2%**, and Wall Street has been **raising** targets into this print — Citi to
$43 from $31 (2026-07-22), JPMorgan to $40 from $35 (2026-07-21), Barclays to $33
from $29 — against a median target of **$42.00**. **Insider sentiment contradicts:**
the two most recent reported months are **MSPR +96.66 (2026-05)** and **+77.60
(2026-06)**, both well beyond the |30| threshold, on the buy side. Only
growth/margins confirms the bear case.

**2 of 3 axes contradict ⇒ `tier_adjustment = VETO`** — applied symmetrically, as
the rubric requires: *the flow says short into a business the market is being
told is beating.* Phase-9 must take the directional short to **watch-only**;
defined-risk carry structures remain permitted.

**That verdict deserves its caveats stated plainly, and they are severe.** The
beats are **non-GAAP against a bar cut 34%** (estimate fell $0.634 → $0.419 across
the four quarters). Insider MSPR is a *ratio* computed on trivial share counts —
net insider activity over twelve months is **−159,240 shares**. And ENPH is not
cheap: **37.41 trailing / 16.30 forward P/E against First Solar's 13.30 / 8.56**.
The veto blocks an aggressive short; it does **not** constitute a bull case.

## Key signals

- **Gross margin 47.25% → 35.49% YoY (−11.8pp); GAAP net income +$29.7M → −$7.4M;
  revenue −20.6%** — from the actual Q1'26 10-Q [FUND:financials_reported].
- **Beat rate 4/4 (100%), mean surprise +19.24%** — but the estimate bar fell from
  $0.634 to $0.419 (−33.9%) across those quarters [FUND:earnings_surprises].
- **MSPR +96.66 (2026-05) and +77.60 (2026-06)**, both > +30 — yet **net 12-month
  insider change is −159,240 shares** [FUND:insider_mspr].
- **Balance sheet is genuinely strong:** cash **$497.5M**, non-current debt
  **$572.5M** (net debt ~**$75M**), **current ratio 3.80**, Q1'26 **FCF $83.0M** vs
  $33.8M a year ago — and the **2026 notes were retired ($632.5M settled)**
  [FUND:financials_reported], [FUND:metric].
- **Not a value setup: P/E 37.41 / Fwd 16.30 vs FSLR 13.30 / 8.56** in a sector
  guided to −22% installs [FUND:peer_pe fz].
- **Analyst consensus "Hold"** (25 brokerages: 9 buy / 12 hold / 4 sell), **median
  target $42.00**, with three upgrades in the six days before the print
  [FUND:recom WebSearch:stockanalysis.com], [FUND:targets WebSearch:tipranks.com].

## Detailed findings

### Valuation

| Metric | ENPH | Source |
|---|---|---|
| P/E (TTM) | **35.83** / **37.41** | Finnhub `peTTM` / `fz` |
| P/E (normalized annual) | 28.10 | Finnhub |
| **Forward P/E** | **16.30** | `fz` |
| P/B (quarterly) | 4.52 | Finnhub |
| P/S (TTM) | 3.46 | Finnhub |
| PEG | **null** (no positive growth to divide by) | Finnhub / `fz` |
| P/FCF per share (TTM) | 33.34 | Finnhub |
| Book value/share | **$8.36** | Finnhub / `fz` (agree) |
| Revenue/share (TTM) | $10.66 | Finnhub |
| EPS incl. extra items (TTM) | **$0.9968** | Finnhub |
| Beta | 1.70 / 1.65 | Finnhub / `fz` |

**Peer relative value — real solar peers, not Finnhub's list.**
Finnhub's `/stock/peers` returned **`["ENTG","AMKR","ONTO","FORM","ACMR","ENPH",
"ACLS","UCTT","AXTI","VECO","ICHR","AEHR","AMAT"]`** — Entegris, Amkor, Onto,
FormFactor, ACM Research, Axcelis, Ultra Clean, AXT, Veeco, Ichor, Aehr and
Applied Materials. **Every one is semiconductor capital equipment. None is a solar
company.** ENPH makes residential solar microinverters; this peer set is
unusable and was **discarded**. Per the phase-7b §5b fallback, the industry was
screened directly with `fz screen --filter ind_solar`:

| Ticker | P/E | Fwd P/E | Short Float | Float | Market cap |
|---|---|---|---|---|---|
| **ENPH** | **37.41** | **16.30** | **17.94%** | 127.77M | $5.01B |
| FSLR | **13.30** | **8.56** | 9.74% | 101.57M | $22.12B |
| NXT | 27.05 | 18.18 | 4.82% | 149.36M | $15.73B |
| SEDG | — (loss) | 27.55 | **17.97%** | 59.76M | $2.62B |
| RUN | 4.67 | 21.37 | **28.65%** | 230.08M | $2.38B |
| SHLS | 47.11 | 18.07 | 8.83% | 164.42M | $1.57B |
| ARRY | — (loss) | **6.07** | 20.39% | 150.96M | $847.6M |
| CSIQ | — (loss) | 10.22 | **34.53%** | 47.58M | $936.3M |
| JKS | — (loss) | 13.50 | 6.81% | 50.26M | $766.5M |
| DQ | — (loss) | — | 7.11% | 67.28M | $815.4M |

**ENPH sits where a bear would want it: expensive.** It trades at **2.8× First
Solar's trailing multiple** and **1.9× its forward multiple**, despite being
−48.45% from its 52-week high. **Five of the ten solar names have no positive
earnings at all**, so the group's cheapness is concentrated in FSLR and ARRY —
and ENPH is at neither end. **There is no valuation floor under this stock.**
A 16.3× forward multiple prices continued profitability that Q1's GAAP loss and
the 25D repeal both call into question.

On short interest ENPH is **mid-pack** at 17.94% — essentially level with SEDG
(17.97%), well below RUN (28.65%), CSIQ (34.53%) and ARRY (20.39%), and well
above FSLR (9.74%) and NXT (4.82%). **ENPH is not the crowded short in solar**,
which materially weakens any squeeze thesis (phase-7c owns that).

### Growth profile

Finnhub TTM aggregates:

| Metric | Value |
|---|---|
| `revenueGrowthTTMYoy` | **−1.64%** |
| `epsGrowthTTMYoy` | **−3.77%** |
| `grossMarginTTM` | 45.34% |
| `operatingMarginTTM` | 6.86% |
| `netProfitMarginTTM` | 9.64% |
| `roeTTM` / `roaTTM` | 13.28 / 4.24 |

⚠️ **The TTM figures materially understate the deterioration and must not be
quoted as the current state.** Exactly the phase-7b pitfall about TTM-current
ratios. Compare three "gross margin" figures for the same company on the same day:

| Source | Gross margin | What it actually measures |
|---|---|---|
| `fz screen --view financial` | **54.66%** | Finviz TTM (stalest) |
| Finnhub `grossMarginTTM` | **45.34%** | Trailing twelve months |
| **Q1'26 10-Q (actual)** | **35.49%** | **The most recent quarter** |

A **19-point spread** between the stalest and the actual. **Use 35.49%.**

**Discrete quarterly progression from the filings** (note Finnhub returns
*cumulative* year-to-date figures for Q2/Q3 — discrete values derived below):

| Period | Net revenues | Gross margin | GAAP net income | OCF | Capex | **FCF** |
|---|---|---|---|---|---|---|
| 2025 Q1 | $356.084M | **47.25%** | **+$29.730M** | $48.414M | $14.608M | $33.806M |
| 2025 Q2 (YTD $719.237M) | *$363.153M* | 47.10% (YTD) | +$66.782M (YTD) | $75.043M | $22.867M | $52.176M |
| 2025 Q3 (YTD $1,129.664M) | *$410.427M* | 47.36% (YTD) | n/a | $88.961M | $30.899M | $58.062M |
| **2026 Q1** | **$282.900M** | **35.49%** | **−$7.406M** | **$102.871M** | $19.898M | **$82.973M** |
| **YoY Q1** | **−20.6%** | **−11.76pp** | **−$37.1M swing** | **+112%** | +36% | **+145%** |

Three readings, in order of importance:

1. **Margin compression is the story, not revenue.** A −20.6% revenue decline is
   painful but survivable; an 11.8-point gross-margin collapse is structural. It
   converts a 9%-net-margin business into a loss-maker, and management guides a
   **further ~3pp of tariff damage** in Q2 (`phase-6-macro.md`). Gross margin at
   ~32–33% would make GAAP losses the run-rate, not an aberration.
2. **GAAP is already negative while non-GAAP still "beats."** Q1'26 reported
   **−$7.406M** GAAP net income; the same quarter is recorded in the surprise
   table below as **+$0.47 actual EPS**. Both are accurate — one is GAAP, one is
   adjusted. **The 100% beat rate is an adjusted-EPS phenomenon sitting on top of
   a GAAP loss.** Any downstream phase citing "4/4 beats" without this is
   misrepresenting the company.
3. **Cash flow is the genuine bull point, and it is real.** OCF **more than
   doubled** YoY to $102.9M and FCF rose **145% to $83.0M** — in the quarter the
   company posted a GAAP loss. That is almost certainly working-capital release
   (inventory drawdown into falling demand) rather than earnings power, which
   makes it **partly non-repeatable**; but $83M of quarterly FCF against a $5.01B
   market cap is a solvency answer, not a growth answer.

### Earnings-surprise history

`/stock/earnings?limit=8` returned **4 quarters** (not 8). All periods
`≤ 2026-07-27` — **look-ahead guard satisfied, no future rows returned.**

| Period | Actual EPS | Estimate | Surprise | Surprise % |
|---|---:|---:|---:|---:|
| 2026-03-31 (Q1) | **0.47** | 0.4190 | +0.051 | **+12.17%** |
| 2025-12-31 (Q4) | **0.71** | 0.5933 | +0.1167 | **+19.67%** |
| 2025-09-30 (Q3) | **0.90** | 0.6604 | +0.2396 | **+36.28%** |
| 2025-06-30 (Q2) | **0.69** | 0.6340 | +0.056 | **+8.83%** |

- **Beat rate: 4 / 4 = 100%.** Mean surprise **+19.24%**; minimum beat +8.83%.
- **But look at the two trends underneath it.** Actual EPS fell
  **0.90 → 0.71 → 0.47** across three quarters (−48%), and the *estimate* fell
  **0.634 → 0.660 → 0.593 → 0.419** (−33.9% from the first to the last). **The
  company is clearing a bar that keeps being lowered.**
- **Q2'26 consensus is $0.46 vs $0.69 actual a year ago — −33.3% YoY**
  (`phase-6-macro.md`). Even a beat would leave EPS down a third.

**This is the axis that contradicts the bearish flow bias**, and it does so
legitimately: a company with a 100% beat rate and a 4-quarter track record of
clearing consensus is a genuinely hazardous short into a print. **But the beats
are adjusted-EPS beats against a collapsing bar, on a business that is now
GAAP-loss-making.** Both halves must travel downstream together.

⚠️ **This finally answers the question phases 4, 5, 6 and 7 all deferred — but
only partly.** The surprise *percentages* are available; the **earnings-day price
moves are not**. Finnhub's earnings endpoint carries no price reaction, the local
snapshot holds 74 sessions containing **no prior ENPH earnings date**, and the
estimate endpoints are paid. **How large ENPH's last four earnings-day gaps were
remains unmeasured** — so whether the 12.25% implied move is rich or cheap cannot
be settled from earnings history. Phase-9 must treat that as an open risk, not a
resolved one.

### Forward consensus

**Both Finnhub estimate endpoints are paid-tier.** Verbatim:

```json
{"error": "You don't have access to this resource."}
```

Returned by `/stock/eps-estimate` and `/stock/revenue-estimate` alike. Per the
phase-7b instruction these are marked **paid, skipped**, and the consensus is
sourced from WebSearch instead (`phase-6-macro.md`):

| Item | Value | Source |
|---|---|---|
| Q2'26 revenue consensus | **$292.2M (−19.6% YoY)** | Zacks via TradingView |
| Q2'26 EPS consensus | **$0.46 (−33.3% YoY)** | Zacks via TradingView |
| Company guidance | **$280–310M**, incl. **~$85M safe-harbor** | Company |
| Guided tariff GM impact | **≈ −3pp** | Company |

**Analyst ratings and targets** — recovered by WebSearch after **all three**
programmatic paths failed (`analyst-vs-flow` empty, `yahoo_fundamentals` HTTP 401,
`fz quote` `Recom`/`Target Price` null; no `fz screen` view carries them — five
views checked: overview / performance / financial / technical / custom):

| Item | Value |
|---|---|
| **Consensus rating** | **"Hold"** — 25 brokerages: **9 buy / 12 hold / 4 sell** |
| **Median price target** | **$42.00** (48 analysts) |
| Average target (S&P Global, 31 analysts) | $43.64 |
| Alternate consensus target (2026-07-21) | $47.11 |
| Target range | **$27.00 – $85.00** |
| **Citi** | raised to **$43** from $31 — **2026-07-22** |
| **JPMorgan** | raised to **$40** from $35 — **2026-07-21** |
| **Barclays** | raised to **$33** from $29 |

**Three upgrades in the week before the print, into a −15% slide.** That is a real
contradiction of the bearish tape and belongs on the record. Its force is limited
by three things: the consensus is **"Hold"** not "Buy"; the median target of
**$42.00 is only +10.5%** from $38.01 (and Barclays' raised target of **$33 is
13% *below* spot**); and the **$27–$85 range** is so wide it signals genuine
analyst disagreement rather than a view.

**Note the convergence:** the $42.00 median target sits essentially on the
**$42.50 call wall** (phase-3), the **largest positive-gamma strike** (+703,006,
phase-4) and the **SMA20 at ≈$42.76** (phase-5). **Five independent methods now
point at ~$42–42.76 as the upside pivot.**

### Balance-sheet health

**`/stock/financials-reported` is NOT paid on this key** — it returned the Q1'26
10-Q (`form: "10-Q"`, `endDate: 2026-03-31`, sections `["bs","cf","ic"]`).

| Item | Q1'26 | Read |
|---|---|---|
| Cash and cash equivalents | **$497.546M** | ~10% of market cap |
| Total assets | $2,723.923M | |
| Total liabilities | $1,621.571M | |
| Total stockholders' equity | **$1,102.352M** | |
| Debt, current | **$0** | no near-term maturity |
| Debt, non-current | **$572.510M** | |
| **Net debt** | **≈ $74.96M** | negligible |
| **Settlement of Notes due 2026** | **−$632.500M** | **retired in the quarter** |
| Current ratio | **3.799** | Finnhub |
| Quick ratio | 3.20 | `fz` |
| Debt / equity | **0.56** (LT 0.55) | `fz`; consistent with 572.5/1,102.4 = 0.52 |

**The balance sheet is not the risk here.** ENPH retired **$632.5M** of 2026
convertible notes during the quarter, carries **zero current debt**, holds
**$497.5M** of cash against **$572.5M** of non-current debt, and runs a current
ratio near **3.8×**. On a **$5.01B** market cap this is a company with time.

**This matters directly to trade construction.** There is no solvency
catalyst and no forced-deleveraging path — which caps how far a bear thesis can
reasonably run and argues against structures that need a collapse to pay. It is
also, alongside FCF, the most likely reason analysts are willing to raise targets
into deteriorating fundamentals.

### Cash-flow quality

| Metric | Q1'26 | Q1'25 | Δ |
|---|---|---|---|
| Operating cash flow | **$102.871M** | $48.414M | **+112%** |
| Capex | $19.898M | $14.608M | +36% |
| **Free cash flow** | **$82.973M** | $33.806M | **+145%** |
| Share repurchases | **$0** | — | buyback paused |
| Cash flow / share (TTM) | $4.42 | — | Finnhub |
| P/FCF per share (TTM) | 33.34 | — | Finnhub |
| Dividend | **none** (`Payout 0.00%`) | — | `fz` |

**FCF grew 145% in the quarter the company posted a GAAP loss.** Two readings and
both should travel:

- **Constructive:** $83M of quarterly FCF ≈ **$332M annualized** against a $5.01B
  cap (~6.6% FCF yield) funds the balance sheet indefinitely.
- **Cautionary:** cash generation rising while revenue falls 20.6% and margins
  collapse is the signature of **working-capital release** — inventory and
  receivables converting to cash as volumes shrink. That is a **one-time, finite**
  source. It cannot repeat once the balance sheet is right-sized, and it is not
  earnings power.

**`Repurchases of common stock: $0`** is a mild negative signal: with $497.5M of
cash and the stock 48% off its high, management is **not** buying. That is
consistent with prioritising the note settlement, but it is not the behaviour of
a board that believes the shares are mispriced.

### Insider signal

`/stock/insider-sentiment` for 2025-07-27 → 2026-07-27. **All rows ≤ as-of;
look-ahead guard satisfied** (latest month is 2026-06).

| Year-Month | MSPR | Net share change |
|---|---:|---:|
| 2025-01 | +100.00 | +99,000 |
| 2025-03 | −100.00 | −132,881 |
| 2025-04 | +100.00 | +4,000 |
| 2025-05 | +100.00 | +31,488 |
| 2025-06 | −100.00 | −1,319 |
| 2025-08 | +100.00 | +5,000 |
| 2025-09 | −100.00 | −1,319 |
| 2025-10 | +100.00 | +10,000 |
| 2025-11 | +100.00 | +5,000 |
| 2025-12 | **−100.00** | **−157,319** |
| 2026-01 | +100.00 | +135,960 |
| 2026-02 | +63.93 | +3,900 |
| **2026-03** | **−100.00** | **−206,089** |
| **2026-05** | **+96.66** | **+40,488** |
| **2026-06** | **+77.60** | **+4,851** |

**The two most recent reported months are strongly positive** — **+96.66** and
**+77.60**, both far beyond the |30| strong-signal threshold, on the buy side.
Taken at face value this is bullish and it **contradicts the bearish flow bias.**

**Three things temper it, and they should be read alongside:**

1. **MSPR is a ratio, and the share counts are trivial.** June's +77.60 rests on
   **4,851 shares** — roughly **$184,000** at $38. May's +96.66 covers 40,488
   shares (~$1.5M). Against a **127.77M float** these are rounding errors
   (0.004% and 0.03%).
2. **Net twelve-month insider activity is −159,240 shares** (sum of the `change`
   column). The **dollar-weighted** insider signal is **negative**, and the three
   largest single months are all sales: 2026-03 (−206,089), 2025-12 (−157,319),
   2025-03 (−132,881).
3. **It is a 2-month run, not the 3+ months** the phase-7b heuristic requires for
   its strongest CONFIRM stack — and **2026-04 and 2026-07 have no data at all**.

**`fz` insider clusters — unavailable.** Both `--side buy` and `--side sell`
returned:

```
No insider data in the local store yet. Run `finviz-pp-cli insider` first.
[]
```

The local Finviz insider store is unpopulated. The store-population command was
**not** run, as it writes to the user's local data store and is outside this
phase's read-only scope. **The distinct-buyer count that would discriminate
between "one officer exercising options" and "a genuine cluster" is therefore
unavailable** — which is precisely the discrimination the small share counts
above make necessary. Recorded as a real gap.

## Red flags

1. 🔴 **Gross margin −11.76pp YoY (47.25% → 35.49%)**, with **~3pp more** guided
   from tariffs. At ~32% gross margin GAAP losses become the run-rate.
2. 🔴 **GAAP net income swung +$29.7M → −$7.4M** while adjusted EPS still "beat" —
   a widening GAAP/non-GAAP gap is a classic late-cycle quality-of-earnings flag.
3. 🔴 **Revenue −20.6% YoY**, and **~29% of Q2 guided revenue (~$85M) is
   non-recurring safe-harbor pull-forward** (`phase-6-macro.md`) — the underlying
   run-rate is worse than the headline.
4. 🔴 **Structural demand destruction:** 25D repealed effective 2025-12-31;
   FY installs guided **−22%**; BNEF sees no recovery to 2023 levels within a
   decade. This is not cyclical.
5. 🔴 **Valuation offers no floor:** 37.41 trailing / 16.30 forward P/E vs FSLR's
   13.30 / 8.56. Being 48% off the high is not the same as being cheap.
6. 🟡 **Estimate bar cut 33.9%** ($0.634 → $0.419) — the beat streak is against a
   retreating target.
7. 🟡 **Net 12-month insider selling of 159,240 shares** despite two positive
   recent MSPR months; the three largest months are all sales.
8. 🟡 **Zero buybacks** with $497.5M cash and the stock down 48%.
9. 🟡 **FCF strength is likely working-capital release**, not earnings power —
   finite by construction.

**Genuine mitigants (recorded so the veto is not one-sided):** 100% beat rate over
4 quarters; three analyst target raises in the six days pre-print; net debt of only
~$75M after retiring $632.5M of notes; current ratio 3.80; $83.0M quarterly FCF
(+145% YoY); MSPR positive in the two most recent reported months.

## Tool / source calls (audit trail)

| Call | Result | Status |
|---|---|---|
| Preflight: `FINNHUB_API_KEY`, US ticker, `fz` | `key set` / `US ok` / `fz ok` | ✅ |
| `/stock/metric?symbol=ENPH&metric=all` | `peTTM=35.8304`, `peNormalizedAnnual=28.1003`, `pbQuarterly=4.5201`, `psTTM=3.4555`, `pegRatio=null`, `currentRatioQuarterly=3.799`, `roeTTM=13.28`, `roaTTM=4.24`, `grossMarginTTM=45.34`, `operatingMarginTTM=6.86`, `netProfitMarginTTM=9.64`, `revenueGrowthTTMYoy=-1.64`, `epsGrowthTTMYoy=-3.77`, `beta=1.6969`, `52WeekHigh=73.74`, `52WeekLow=25.775`, `epsInclExtraItemsTTM=0.9968`, `bookValuePerShareQuarterly=8.3648`, `cashFlowPerShareTTM=4.42261`, `pfcfShareTTM=33.3429`, `yearToDatePriceReturnDaily=14.5086` | ✅ |
| `/stock/earnings?limit=8` | **4 rows** (not 8), all `period ≤ 2026-07-27`; beat rate **4/4**, mean surprise **+19.24%** | ✅ partial |
| `/stock/eps-estimate?freq=quarterly` | `{"error": "You don't have access to this resource."}` | ⛔ **paid, skipped** |
| `/stock/revenue-estimate?freq=quarterly` | `{"error": "You don't have access to this resource."}` | ⛔ **paid, skipped** |
| `/stock/peers` | `["ENTG","AMKR","ONTO","FORM","ACMR","ENPH","ACLS","UCTT","AXTI","VECO","ICHR","AEHR","AMAT"]` — **all semiconductor equipment; discarded** | ⚠️ misclassified |
| `/stock/insider-sentiment?from=2025-07-27&to=2026-07-27` | **15 monthly rows**, latest 2026-06 (`mspr=77.603584`, `change=4851`); 2026-05 `mspr=96.65775`; Σ`change` = **−159,240** | ✅ |
| `/stock/financials-reported?freq=quarterly` | `data[0]` = `{year:2026, quarter:1, form:"10-Q", endDate:"2026-03-31"}`, sections `["bs","cf","ic"]`; `Net revenues=282900000`, `Gross profit=100393000`, `Net income (loss)=-7406000`, `Cash and cash equivalents=497546000`, `Total assets=2723923000`, `Total liabilities=1621571000`, `Total stockholders' equity=1102352000`, `Debt, current=0`, `Debt, non-current=572510000`, `Settlement of Notes due 2026=-632500000`, `Net cash provided by operating activities=102871000`, `Purchases of property and equipment=19898000`, `Repurchases of common stock=0` | ✅ **free on this key** |
| `fz screen --filter ind_solar --view ownership --agent` | 14 solar names incl. ENPH `Float=127.77M SI=17.94% SR=3.04`; FSLR `9.74%`; RUN `28.65%`; CSIQ `34.53%` | ✅ |
| `fz screen --filter ind_solar --view valuation --agent` | ENPH `P/E=37.41 Fwd P/E=16.30`; FSLR `13.30 / 8.56`; NXT `27.05 / 18.18`; SEDG `– / 27.55`; RUN `4.67 / 21.37` | ✅ |
| `fz screen --filter ind_solar --view financial --agent` | ENPH `Curr R=3.80`, `Quick R=3.20`, `Debt/Eq=0.56`, `LTDebt/Eq=0.55`, `Gross M=54.66%`, `Oper M=18.82%`, `ROE=14.11%`, `ROIC=7.91%`, **`Earnings="Jul 28/a"`** | ✅ |
| `fz screen --filter ind_solar --view performance --agent` | ENPH `Perf Month=-19.49%`, `Perf Quart=+6.26%`, `Perf Half=-3.67%`, `Perf YTD=+18.60%`, `Perf Year=+7.34%`, `Perf 3Y=-77.21%`, `Perf 5Y=-78.01%`, `Rel Volume=0.50` | ✅ |
| `fz insider-clusters --days 30 --min-buyers 2 --side buy\|sell --agent` | `"No insider data in the local store yet. Run finviz-pp-cli insider first."` → `[]` | ⛔ **unavailable** |
| `fz quote ENPH --agent` → `.fundamentals.Recom` / `."Target Price"` | **null** (degraded 14-field payload, carried from phase-0) | ⛔ |
| WebSearch — analyst consensus/targets | Consensus **"Hold"** (9/12/4 of 25); median target **$42.00** (48 analysts); Citi **$43** ← $31 (2026-07-22); JPM **$40** ← $35 (2026-07-21); Barclays **$33** ← $29; range **$27–$85** | ✅ fallback |

## Tool / source errors

1. **`/stock/eps-estimate` and `/stock/revenue-estimate` — paid-tier.** Verbatim:
   `{"error": "You don't have access to this resource."}` on both.
   **Marked "paid, skipped"; no subscription attempted.** Forward consensus
   sourced from WebSearch (Zacks) instead. *(Consistent with the known
   data-source constraint that Finnhub estimates are paid.)*
2. **`/stock/earnings?limit=8` returned only 4 quarters.** Not an error, but the
   beat-rate sample is **n=4**, not 8. Any "100% beat rate" claim carries that
   sample size.
3. **`/stock/peers` is misclassified.** ENPH returns a **semiconductor capital
   equipment** peer set (ENTG, AMKR, ONTO, FORM, ACMR, ACLS, UCTT, AXTI, VECO,
   ICHR, AEHR, AMAT) with **no solar company in it**. Discarded in favour of
   `fz screen --filter ind_solar`. *Propose-only note for the skill:*
   `phases/phase-7b-fundamentals.md` §5 should sanity-check the Finnhub peer list
   against the `fz` industry label before use, and prefer the `fz` industry screen
   on mismatch. (Note phase-6's search also found ENPH filed under
   "semiconductors" by a third-party site — the misclassification is not unique to
   Finnhub.)
4. **`fz insider-clusters` — local store empty.** Verbatim:
   `"No insider data in the local store yet. Run finviz-pp-cli insider first."`
   The population command was **not** run (it mutates the user's local data
   store, outside this phase's read-only scope). **`insider_cluster` is therefore
   `n/a`** — the distinct-buyer count that would validate or dismiss the two
   positive MSPR months is unavailable.
5. **Analyst fields unavailable from every programmatic source.** `fz quote`
   `Recom`/`Target Price` null (degraded payload); **five** `fz screen` views
   checked (overview, performance, financial, technical, custom) — none carries
   `Recom` or `Target Price`; `analyst-vs-flow` returned no analyst block and
   `yahoo_fundamentals` returned HTTP 401 (`phase-7-insights.md`). **Recovered via
   WebSearch and labelled as such** — not silently skipped, per phase-7's handoff.
6. **`fz` ticker strings are malformed** (`EENPH`, `FFSLR`, `SSEDG`, `RRUN`,
   `NNXT`, `SSHLS`, `AARRY`, `CCSIQ` — leading character duplicated). Cosmetic;
   identity confirmed by `Market Cap` and `Company` cross-match, as in phase-0.
   **No numeric impact**; malformed strings not propagated.

## DATA NOTE / CORRECTION

- **Q2/Q3 2025 revenue figures from `financials-reported` are cumulative
  year-to-date, not discrete quarters.** Discrete values ($363.153M for Q2'25,
  $410.427M for Q3'25) are **my subtraction** and are italicised in the table.
  The **Q1'26 vs Q1'25 comparison used for every YoY claim is discrete-vs-discrete**
  ($282.900M vs $356.084M) and is unaffected.
- **Gross margin 35.49% is derived** (`100.393 ÷ 282.900`), as is FCF
  (`OCF − capex`) and net debt (`572.510 − 497.546`). All from returned line items.
- **Beat rate and mean surprise are computed** from the four returned rows
  (4/4; mean of 12.1718, 19.6696, 36.281, 8.8328 = **+19.24%**).
- **Σ insider `change` = −159,240 shares** is my summation of the 15 returned rows.
- **Three different gross margins coexist** across sources (54.66% `fz` TTM /
  45.34% Finnhub TTM / **35.49% actual Q1'26**). The filing figure is used
  throughout; the discrepancy is reported rather than reconciled away.
- **YTD performance differs by source**: Finnhub `yearToDatePriceReturnDaily
  = 14.51%` vs `fz Perf YTD = 18.60%`. Both quoted; neither is load-bearing.
- **`fz` `Oper M = 18.82%` is irreconcilable with Finnhub's `operatingMarginTTM
  = 6.86%`** and with a GAAP-loss quarter. Flagged, **not used**.
- No value written in this phase was corrected after first read.

## Verdict for downstream

**Flow bias entering this gate: BEARISH** (plurality of phases 1–7: phase-1
bearish, phase-2 mixed-leaning-distribution, phase-4 short-gamma, phase-5 bearish
regime, phase-6 strong headwind, phase-7 weakly bearish).

**Axis-by-axis contradiction count:**

| Axis | Reading | vs bearish flow bias |
|---|---|---|
| **(a) earnings_trend** | Beat rate **4/4**, mean surprise **+19.24%**; 3 analyst target raises in 6 days pre-print; consensus "Hold", median target **$42.00** (+10.5%) | ❌ **CONTRADICTS** |
| **(b) insider_MSPR** | Two most recent months **+96.66** and **+77.60**, both > \|30\|, buy side | ❌ **CONTRADICTS** (weakly — see caveats) |
| **(c) growth/margins** | Revenue **−20.6%**, gross margin **−11.76pp**, GAAP **+$29.7M → −$7.4M**, ~3pp more tariff damage guided | ✅ **CONFIRMS** |

**2 of 3 contradict ⇒ `VETO`.**

```
fundamental_signal:  BEARISH
tier_adjustment:     VETO
contradiction_count: 2
insider_cluster:     {present: n/a, distinct_buyers: n/a, side: n/a}   # fz local store empty
key_risks:
  - "Gross margin 47.25% → 35.49% YoY with ~3pp more tariff damage guided; GAAP already a −$7.4M loss while non-GAAP still 'beats'."
  - "~29% of guided Q2 revenue (~$85M) is non-recurring safe-harbor pull-forward; 25D repeal removed the structural demand base (FY installs −22%)."
  - "No valuation floor: 37.41 trailing / 16.30 forward P/E vs FSLR 13.30 / 8.56 — 48% off the high is not cheap."
```

**Reading the verdict correctly — this is the part phase-9 must not garble.**

- `fundamental_signal = BEARISH` and `tier_adjustment = VETO` are **not**
  contradictory. The signal describes the *business*, which is deteriorating on
  every operating measure. The tier adjustment is a **downside-only gate applied
  to the trade**, and per the rubric's symmetric clause it fires when ≥2 axes
  contradict the flow bias — here, a directional **short** into a company with a
  100% beat rate, rising analyst targets, positive recent insider ratios, and a
  fortress balance sheet.
- **Phase-9 effect: the directional short goes to watch-only / 0% size.
  Defined-risk carry structures remain permitted.**
- **Phase-7b can only cut, never add.** Nothing here licenses a long. The three
  key risks above stand in full, and the fundamental picture remains bearish.

**Three things phase-8, 8b and 9 must carry:**

1. **The "4/4 beat, +19.24% average" and the "−$7.4M GAAP loss" are the same
   quarters.** Adjusted EPS beats a bar cut 33.9% ($0.634 → $0.419) while GAAP
   turns negative. **Never cite the beat rate without the bar cut and the GAAP
   loss**, and never cite the GAAP loss without the beat rate. Phase-8b should
   argue this directly — it is the sharpest bull/bear seam in the run.
2. **The balance sheet removes the tail.** Net debt ≈ **$75M**, current ratio
   **3.80**, **$0** current debt, **$632.5M** of 2026 notes already retired,
   **$83.0M** quarterly FCF. **There is no solvency catalyst** — which caps how far
   the bear case can travel and argues against structures needing a collapse.
   (Caveat: the FCF surge is likely finite working-capital release.)
3. **$42–42.76 is now a five-method confluence.** The **$42.00 median analyst
   target** joins the **$42.50 call wall** (phase-3), the **largest positive-gamma
   strike +703,006** (phase-4), **SMA20 ≈ $42.76** (phase-5) and phase-4's vanna
   pivot. Phase-9 should treat it as the primary upside reference.

**Open questions:**

- **ENPH's actual earnings-day price moves remain unmeasured** — Finnhub carries
  no price reaction, the local snapshot contains no prior ENPH earnings date, and
  estimates are paid. Whether the **12.25% implied move** is rich or cheap is
  therefore **unresolved after four phases of trying**. Phase-9 must carry it as
  an open risk. → **phase-9 (accept as unknown)**
- Insider MSPR is positive on **~$1.7M of buying** against **−159,240 shares** net
  over twelve months, and the `fz` cluster data that would resolve it is
  unavailable. Is the recent buying a genuine cluster or one officer? → **unresolved**
- ENPH's short float (**17.94%**) is **mid-pack** in solar — below RUN (28.65%),
  CSIQ (34.53%) and ARRY (20.39%). Does that leave enough fuel for a squeeze on a
  beat? → **phase-7c**
- **Zero buybacks** with $497.5M of cash and the stock 48% off its high. Signal or
  capital discipline after the note settlement? → **phase-8b**
