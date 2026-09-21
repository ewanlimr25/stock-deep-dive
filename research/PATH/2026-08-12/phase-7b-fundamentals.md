# Phase 7b — Deep Fundamentals & Quality Veto (FINNHUB)

**Ticker:** PATH
**As-of date:** 2026-08-12
**Generated:** 2026-08-13T03:05:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-5-historical.md, phase-7-insights.md

## Summary

This phase finds a **genuine quality veto**. The flow bias building across
phases 1–7 was mildly bullish on the multi-week structural dimension (29-day
OI build, +32% rally, moderate dark-pool accumulation), but two of the three
fundamental axes contradict it: (1) the **most recent quarter broke a 3-quarter
beat streak with a −7.86% EPS miss**, and (2) **insider MSPR has been
persistently negative for 11 of the last 15 available months, including the
most recent one (July 2026, `mspr=-100`, the maximum-bearish reading)**.
Growth/margins (15.24% TTM revenue growth, 83% gross margin, no debt, positive
operating cash flow) do not contradict the flow bias — but **2 of 3 axes do**,
which trips the rubric's `VETO` threshold. Separately, the peer comparison
surfaces the single most striking datapoint of this whole deep dive: **PATH's
short float is 31.10% of float — 2.3× to 13× every one of its 11 named
peers** (range 2.37%–13.26%). This isn't one of the three formal veto axes,
but it's the loudest quality/positioning signal in the fundamentals layer and
must be carried forward as a `key_risk`.

## Key signals

- **Earnings: 3 of last 4 quarters beat, but the most recent (period
  2026-06-30) MISSED by −7.86%** [FUND:earnings_surprise]
- **Insider MSPR: 11 of 15 available months negative; most recent (July 2026)
  = −100 (max bearish)** [FUND:insider_MSPR]
- **Short float 31.10%** — 2.3×–13× every named peer (next-highest: GTLB
  13.26%; most peers 2–11%) [FUND:short_float fz]
- Revenue growth TTM YoY **+15.24%**, gross margin **83.02%**, no long-term
  debt on the balance sheet, current ratio **2.48** [FUND:key_metrics]
- Peer valuation: PATH's forward P/E (**16.93**) is the 2nd-cheapest of 11
  named peers; PEG (**1.26**) is mid-pack [FUND:peer_pe fz]

## Detailed findings

### Valuation (PE / fwd PE / PEG / P/B / P/S vs named peers)

Finnhub `/stock/metric`: `peTTM=24.67`, `peNormalizedAnnual=28.61`,
`P/B=3.22`, `P/S=4.83`, `PEG=null` (Finnhub doesn't compute it). Peer table
below (fz) fills the PEG gap.

### Growth profile

`revenueGrowthTTMYoy=+15.24%`, `epsGrowthTTMYoy=null` (Finnhub). `grossMarginTTM
=83.02%`, `operatingMarginTTM=6.05%`, `netProfitMarginTTM=19.58%`. **Quality
flag:** net margin (19.58%) is over 3× operating margin (6.05%) — the
company's TTM net income is being lifted well above core operating
profitability, almost certainly by a non-operating item (e.g. a tax benefit
or gain) in a quarter other than the one directly inspected below. The single
quarter examined in the statements pull (period ending 2026-04-30) shows
`OperatingIncomeLoss=$27.99M` (6.69% of that quarter's $418.4M revenue) vs.
`NetIncomeLoss=$22.53M` (5.38% margin) — i.e. for *this specific quarter*, net
margin is actually *below* operating margin, the opposite of the TTM
relationship. This means the TTM net-margin lift is concentrated in a
different quarter — treat the TTM net margin as **lower-quality earnings**,
not a clean read on run-rate profitability.

### Earnings-surprise history (Finnhub returned 4 of the requested 8 quarters)

| Period | Actual EPS | Estimate | Surprise | Surprise % |
|---|---:|---:|---:|---:|
| 2025-09-30 | $0.15 | $0.0817 | +$0.0683 | **+83.60%** |
| 2025-12-31 | $0.16 | $0.149 | +$0.011 | +7.38% |
| 2026-03-31 | $0.30 | $0.2597 | +$0.0403 | +15.52% |
| **2026-06-30** | **$0.15** | **$0.1628** | **−$0.0128** | **−7.86%** |

**Beat-rate: 3/4 (75%)**, but **the most recent quarter broke the streak with
a miss** — recency matters more than the trailing average for a flow-timing
veto. (Look-ahead guard: all 4 periods are ≤ the 2026-08-12 as-of date; no
future-period contamination.)

### Forward consensus

`/stock/eps-estimate` and `/stock/revenue-estimate` both **403'd** ("You
don't have access to this resource" — paid tier, per the known Finnhub
free/paid map). Substitute (WebSearch, phase-6): **Q2 FY2027 (reporting
2026-09-03) consensus revenue $397.77M, consensus EPS $0.15** — a single
forward data point, not a multi-quarter trend; no forward EPS/revenue
*trajectory* is available this run.

### Balance-sheet health

Finnhub `/stock/financials-reported` (quarterly 10-Q, period ending
2026-04-30, filed 2026-06-04 — the latest one available, ~3.5 months stale
relative to the as-of date, normal filing lag): `CashAndCashEquivalents=
$632.2M`, `Assets=$2,904.7M`, `Liabilities=$1,001.7M` (`LiabilitiesCurrent=
$831.7M`), `StockholdersEquity=$1,903.0M`. **No long-term-debt line item found
anywhere in the balance-sheet report** — consistent with Finnhub's
`longTermDebt2TotalCapitalAnnual=null` (no debt to report, not a data gap).
`currentRatio=2.48` — healthy liquidity.

### Cash-flow quality

Same 10-Q: `NetCashProvidedByOperatingActivities=+$131.9M` (healthy, positive)
for the quarter; `NetCashUsedInInvestingActivities=-$112.8M` (includes a
$149.4M acquisition — active M&A); `NetCashUsedInFinancingActivities=
-$252.2M` (large net outflow — with no debt to service, this is most likely
capital return / buyback activity, though the specific buyback line item
wasn't isolated from the raw `cf` tags pulled). `PaymentsToAcquire
PropertyPlantAndEquipment=$2.7M` — very light capex intensity, consistent
with a software business.

### Insider signal (MSPR, last ≤12 months + fz cluster)

Finnhub `/stock/insider-sentiment` (from 2025-08-12 to 2026-08-12):

| Month | MSPR | Month | MSPR |
|---|---:|---|---:|
| 2025-01 | −100 | 2025-10 | −89.47 |
| 2025-02 | −100 | 2025-11 | −100 |
| 2025-03 | +5.01 | 2025-12 | −4.17 |
| 2025-04 | −100 | 2026-01 | −100 |
| 2025-05 | −100 | 2026-02 | **+100** |
| 2025-06 | −77.79 | 2026-03 | −33.33 |
| 2025-07 | −100 | 2026-04 | +59.03 |
| 2025-09 | −7.33 | **2026-07** | **−100** |

(2025-08 and 2026-05/06 have no rows — no reported insider transaction volume
those months, not zero-filled.) **11 of the 15 available months are negative**,
5 of those at the −100 floor. The most recent available month (July 2026) is
**−100**, the maximum-bearish reading, right ahead of the 2026-09-03 earnings
date. Per the MSPR scale, `|MSPR|>30` is a strong signal and this series has
been persistently in strong-negative territory. **`fz insider-clusters
--days 30 --min-buyers 2`**: PATH appears in **neither** the buy-cluster (5
names) nor the sell-cluster (23 names) list — no ≥2-distinct-officer cluster
event in the trailing 30 days either way. `insider_cluster: {present: false,
distinct_buyers: n/a, side: n/a}` — the MSPR read stands alone, un-sharpened
either direction by the cluster lens.

**Analyst cross-source (Finnhub `/stock/recommendation`, free):** unchanged
for 3 straight months (Jun/Jul/Aug 2026): `strongBuy=2, buy=7, hold=18, sell=1,
strongSell=0` (28 analysts) — a moderate-buy-leaning but hold-dominated
consensus with zero revision momentum. (`fz`'s `Recom`/`Target Price` fields
were unavailable — same known `fz quote` degradation flagged in phase-0;
Finnhub's free recommendation-trends endpoint substitutes cleanly.)

### Peers — relative-value comparison

Finnhub `/stock/peers` (self dropped): FTNT, ZS, RBRK, GEN, FROG, S, GTLB,
QLYS, NTSK, CVLT, MSFT. `fz screen --tickers ... --view valuation` /
`--view ownership` (ticker prefix doubled in display — a known cosmetic
quirk, values correct):

| Ticker | P/E | Fwd P/E | PEG | EPS next Y | Short Float | Float |
|---|---:|---:|---:|---:|---:|---:|
| **PATH** | 25.18 | **16.93** | 1.26 | 15.17% | **31.10%** | 390.80M |
| CVLT | 90.40 | 22.80 | 1.12 | 14.02% | 7.84% | 40.89M |
| FROG | — | 75.17 | 3.63 | 16.76% | 8.66% | 108.46M |
| FTNT | 56.67 | 42.79 | 2.72 | 9.45% | 2.37% | 607.31M |
| GEN | 16.63 | 8.67 | 0.71 | 12.82% | 5.57% | 539.07M |
| GTLB | — | 40.12 | 6.04 | 25.20% | 13.26% | 144.35M |
| NTSK | — | 700.14 | — | 111.94% | 6.42% | 236.45M |
| QLYS | 32.42 | 22.13 | 2.73 | 8.19% | 10.90% | 34.22M |
| RBRK | — | 151.11 | — | 106.23% | 8.31% | 153.67M |
| S | — | 44.68 | 0.84 | 43.02% | 5.91% | 319.29M |
| ZS | — | 38.72 | 2.15 | 11.24% | 7.08% | 104.84M |

PATH sits near the **cheap end** of the peer group on forward P/E (only GEN's
8.67 is cheaper) and mid-pack on PEG (GEN 0.71 and S 0.84 are cheaper on a
growth-adjusted basis; most others are far more expensive, up to GTLB's 6.04).
**But PATH's short float dwarfs every peer** — the next-highest is GTLB at
13.26%, less than half of PATH's 31.10%; most peers sit in single digits.
Market participants are structurally more bearish/hedged on PATH than on any
name in its own comp set, despite (or possibly contributing to) reasonable
relative valuation and the recent rally. `fz quote --tickers` (the shallow
overview call) returned `P/E`/`Perf YTD` as null for every ticker including
PATH — the `--view` screen route was used instead for real numbers, per the
already-memoried `fz quote` degradation.

## Red flags

- **Most recent quarter (2026-06-30) missed EPS by −7.86%**, breaking a
  3-quarter beat streak, right ahead of the next print (2026-09-03).
- **Insider MSPR persistently negative** (11/15 months, 5 at the −100 floor)
  with the **freshest available read at the maximum-bearish extreme**
  (July 2026, −100).
- **Short float 31.10%** — far outside the peer range (2.37%–13.26%), the
  standout positioning red flag of the whole fundamentals layer.
- Net margin (19.58% TTM) diverges sharply from operating margin (6.05% TTM,
  and the single-quarter net margin of 5.38% is actually *below* that
  quarter's operating margin) — a lower-quality-earnings flag, not a clean
  profitability read.
- No forward EPS/revenue *trend* available (paid-tier); only a single-point
  Q2 FY2027 consensus via WebSearch.

## Tool / source calls

| Command | Status |
|---|---|
| `curl .../stock/metric?symbol=PATH&metric=all` | 200 OK |
| `curl .../stock/earnings?symbol=PATH&limit=8` | 200 OK, 4 of 8 rows returned |
| `curl .../stock/eps-estimate?symbol=PATH&freq=quarterly` | **403 paid, skipped** |
| `curl .../stock/revenue-estimate?symbol=PATH&freq=quarterly` | **403 paid, skipped** |
| `curl .../stock/peers?symbol=PATH` | 200 OK, 12 tickers (11 peers + self) |
| `curl .../stock/insider-sentiment?symbol=PATH&from=2025-08-12&to=2026-08-12` | 200 OK, 15 monthly rows |
| `curl .../stock/financials-reported?symbol=PATH&freq=quarterly` | 200 OK, 19 quarters, `bs`/`cf`/`ic` all populated (not paid-tier-blocked this run) |
| `curl .../stock/recommendation?symbol=PATH` | 200 OK, 4 monthly rows |
| `fz quote --tickers PATH,<11 peers> --agent` | 200 OK but `P/E`/`Perf YTD` null (known degradation) |
| `fz screen --tickers PATH,<10 peers> --view valuation --agent` | 200 OK, full data |
| `fz screen --tickers PATH,<10 peers> --view ownership --agent` | 200 OK, full data |
| `fz insider-clusters --days 30 --min-buyers 2 --side buy/sell --agent` | 200 OK, PATH absent both lists |
| `fz quote PATH --agent` (Recom/Target) | 200 OK but null (known `fz quote` degradation) |

## Tool / source errors

- `eps-estimate`/`revenue-estimate`: HTTP 403 "You don't have access to this
  resource" — confirmed paid-tier per the standing Finnhub free/paid map;
  substituted with a single WebSearch consensus point (phase-6), no forward
  trend available.
- `fz quote --tickers` and `fz quote PATH` (Recom/Target leg): return null for
  the affected fields — the same standing `fz quote` degradation logged in
  phase-0/memory; worked around via `fz screen --view` for valuation/ownership
  and Finnhub `/stock/recommendation` for the analyst cross-source.

## Verdict for downstream phases

```
fundamental_signal:  BEARISH
tier_adjustment:     VETO
contradiction_count: 2   # earnings_trend (recent miss breaks beat streak),
                          # insider_MSPR (persistently + currently extreme negative)
                          # growth/margins does NOT contradict (solid revenue growth,
                          # strong gross margin, no debt, positive OCF)
insider_cluster:     {present: false, distinct_buyers: n/a, side: n/a}
key_risks:
  - Insider MSPR at the maximum-bearish reading (-100) in the most recent
    available month, directly ahead of the 2026-09-03 earnings date.
  - Most recent quarter missed EPS estimates (-7.86%), breaking a 3-quarter
    beat streak — recency-weighted caution into the next print.
  - Short float (31.10%) is 2.3x-13x every named peer — the market is
    structurally far more bearish/hedged on PATH than on any comparable name,
    a positioning risk independent of the two formal veto axes above.
```

**Per the tier-adjustment rubric, 2 contradictions trips `VETO`**: a
directional long thesis built on the phases 1–7 flow read should be sized as
**watch-only / 0%** on outright direction; only carry-defined-risk structures
(e.g. credit spreads, collars) should be considered by phase-9, not a naked
directional long. This does not flip the thesis bearish outright (growth/
margins/balance-sheet remain solid, and analyst consensus hasn't moved
negative) — but it firmly vetoes chasing the bullish flow/structural read from
phases 2/4/5 with a full-size directional long. Phase-9 must carry this
verdict forward verbatim; per this phase's own rule, a quality gate can only
cut conviction, never raise it.

**Open questions for phase-8/8b:** Does the bull case have a specific
rebuttal for the insider-selling pattern (e.g., pre-set 10b5-1 selling plans
unrelated to sentiment, common for post-IPO-vintage tech names) worth
weighing against the raw MSPR reading? Is the extreme short float a
short-squeeze tailwind (helping explain the +32% rally) or confirmation that
smart money remains structurally bearish through the rally?
