# Phase 7b — Deep Fundamentals & Quality Veto (FINNHUB)

**Ticker:** NVDA
**As-of date:** 2026-05-27
**Generated:** 2026-05-28T02:54:00Z
**Upstream phases cited:** phase-7-insights.md (flow bias: COVERED_CALL / mildly-bearish-flow)

## Summary

The **underlying business is exceptional** — operating margin 64%, ROE 112%,
revenue +70.7% YoY, EPS +110.3% YoY, and a 3/3 recent earnings-beat record
(filtered to ≤ as-of, the unfiltered Finnhub return contained one look-ahead
row). On any forward-looking valuation lens NVDA is **cheap among peers**: PEG
0.39, Forward P/E 17.19, against AVGO 23.25 / AMD 37.81 / ADI 28.17.
**Analyst recom 1.27 (strong buy) with $305.72 target = +43.8% upside.** These
fundamentals **reinforce, not contradict, the phase-7 COVERED_CALL framing** —
institutions write calls against premium-quality assets they want to *hold for
yield*, not against dogs they want to dump. They *do* contradict an outright
*directional short* thesis on the underlying business. Insider activity is
silent (no Finnhub MSPR, no `fz` cluster), so the insider axis is NEUTRAL (not
contradictory). Verdict: **`fundamental_signal: BULLISH`, `tier_adjustment:
CAUTION`** — flow says capped-upside / mild near-term bearish, fundamentals say
"the business is fine and probably mispriced cheap" → any **outright short** in
phase-9 must cut a size step; an **upside-capped defined-risk structure** is
unaffected (the fundamentals don't veto a near-term range trade).

## Key signals

- **Op margin 64.0%, ROE 111.66%, ROA 83.11%** [FUND:operatingMarginTTM]
  [FUND:roeTTM] — best-in-class profitability.
- **Revenue +70.68% YoY, EPS +110.34% YoY (TTM)** [FUND:revenueGrowthTTMYoy]
  [FUND:epsGrowthTTMYoy] — hyper-growth still intact.
- **PEG 0.39, Forward P/E 17.19** [FUND:peg fz] [FUND:forwardPE fz] — **cheap
  among hyperscale-AI peers** on growth-adjusted multiple.
- **Earnings beats 3/3 trailing (avg surprise ~+2.6%)** [FUND:earnings_surprises]
  — quality and consistency confirmed; magnitude modest.
- **Analyst recom 1.27 (strong-buy), target $305.72 (+43.8% upside)**
  [FUND:recom fz] — sell-side strongly bullish; conflicts with bearish flow.

## Detailed findings

### Valuation — [FUND:peTTM, peg fz, forwardPE fz]

| Metric | NVDA | Peer mid-range |
|--------|-----:|---------------:|
| P/E TTM | 32.56 | 25 (QCOM) – 82 (AVGO) |
| P/E TTM (Finnhub) | 32.12 | — |
| P/E Normalized Annual | 42.70 | — |
| **Forward P/E** | **17.19** | 23 (AVGO) – 38 (AMD) |
| **PEG TTM** | **0.39** (`fz`) / 1.03 (Finnhub) | 0.47 (AVGO) – 0.95 (ADI) |
| P/B | 26.23 | (high — quality premium) |
| EPS next Y growth | +39.39% | +20 (ADI) – +76 (AMD) |
| 52W High / Low | $236.54 / $129.16 | spot $212.60 → −10.1% from high |

The two PEG numbers disagree (Finnhub 1.03 vs `fz` 0.39) — Finnhub uses TTM EPS
growth while `fz` uses forward EPS growth, hence the divergence. Either way NVDA
prints as **cheap for its growth profile** relative to AVGO/AMD/ADI.

### Growth profile — [FUND:revenueGrowthTTMYoy, epsGrowthTTMYoy]

| Metric | TTM Value |
|--------|----------:|
| Revenue growth YoY | **+70.68%** |
| EPS growth YoY | **+110.34%** |
| Gross margin TTM | 74.15% |
| **Operating margin TTM** | **64.02%** |
| Net margin TTM | 62.97% |

Margin expansion has *not* compressed — NVDA is still in the rare regime of
growing >70% with 64% operating margins. There is **no evidence of business
deterioration**; the phase-1 bearish flow cannot be sourced from fundamentals.

### Earnings-surprise history (last 4, look-ahead filtered) — [FUND:earnings_surprises]

The raw Finnhub return contained 4 rows including one with `period=2026-06-30`
showing `actual=1.87` — a quarter **ending after the as-of 2026-05-27** that
*cannot* yet have an actual print. Dropped per the look-ahead guard.

| Period (≤ as-of) | Actual EPS | Estimate | Surprise | Surprise % |
|------------------|-----------:|---------:|---------:|-----------:|
| 2026-03-31 (Q4 FY26) | 1.62 | 1.5634 | +0.0566 | **+3.62%** |
| 2025-12-31 (Q3 FY26) | 1.30 | 1.2746 | +0.0254 | **+1.99%** |
| 2025-09-30 (Q2 FY26) | 1.05 | 1.0281 | +0.0219 | **+2.13%** |

**Beat-rate: 3/3 (100%); average surprise +2.58%**. The pattern is *consistent
small beats*, not big surprises — guidance-discipline + sandbagging. Healthy.

### Forward consensus — [FUND:eps_estimate, revenue_estimate]

Finnhub `/eps-estimate` and `/revenue-estimate` returned **empty `data` arrays**
on this free-tier key (the endpoints exist but appear gated for forward
consensus). `fz` surfaced `EPS next Q = 2.07` and `EPS next Y growth = +39.39%`
as a partial substitute. No analyst dispersion (high/low + count) available.

### Balance-sheet health — [FUND:currentRatioAnnual]

| Metric | Value |
|--------|------:|
| Current ratio | **3.91** (very strong liquidity) |
| Total debt / equity | (null — Finnhub did not return) |
| LT debt / equity | (null) |

`/stock/financials-reported` not pulled (free tier typically returns line items
inconsistently; deferred). Current ratio 3.91 indicates ample short-term
liquidity; absence of debt ratios is a known free-tier gap, not a red flag.

### Cash-flow quality

Statements skipped (paid-tier on this key). Margin proxies stand in: 74% gross,
64% op, 63% net → cash-flow conversion is implied high (no debt headwind from
current-ratio read). Buyback/dividend not pulled this run.

### Insider signal — [FUND:mspr, insider_cluster fz]

- Finnhub `/insider-sentiment` returned **empty `data` array** for NVDA in the
  trailing 365 days — known issue (memory `data-source-workarounds`: MSPR
  empty for many large caps via Finnhub).
- `fz insider-clusters --days 30 --side buy --min-buyers 2`: NVDA **not
  present** (the only buy cluster in the last 30d is WHF). `--side sell` top-N
  shows AMPX, AMZN, KALV, DIOD, LTH, … — **NVDA not in either cluster list**.

**Insider axis: NEUTRAL / silent.** Absence is not bullish or bearish — it
contradicts neither side of the flow read.

### Peers — relative-value comparison — [FUND:peer_pe fz]

Finnhub peer list: NVDA, AVGO, MU, AMD, INTC, TXN, QCOM, ADI, MRVL, MPWR,
CBRS, ALAB. Selected mega-cap comp (combining `fz quote --tickers` + the
`sec_technology,ind_semiconductors` screen — NVDA classified outside the strict
"Semiconductors" Finviz industry, hence absent from the screen rows):

| Ticker | P/E TTM | Forward P/E | PEG | EPS next Y |
|--------|--------:|------------:|----:|-----------:|
| **NVDA** | **32.56** | **17.19** | **0.39** | **+39.39%** |
| AVGO | 82.29 | 23.25 | 0.47 | +61.02% |
| AMD | 162.64 | 37.81 | 0.61 | +76.06% |
| ADI | 61.95 | 28.17 | 0.95 | +20.57% |
| MU | 43.83 | n/a | n/a | n/a |
| QCOM | 25.39 | n/a | n/a | n/a |
| TXN | 54.31 | n/a | n/a | n/a |
| MRVL | 64.28 | n/a | n/a | n/a |

NVDA prints the **lowest Forward P/E and PEG** in this peer set. Bear in mind
this is `fz` Finviz data — a deterministic EOD snapshot, not point-in-time
2026-05-27 — but consistent with Finnhub's PEG of 1.03 (TTM-based) being also
the lowest in the named peer list (AMD 1.21+ on the TTM lens).

NVDA-specific ownership (already from phase-0 `fz`): Float 23.27B, Short Float
1.22%, low short-interest cohort (named peers fall ADI 2.24% / AMD 2.23% /
AVGO 1.10% — NVDA in the middle-low band).

## Red flags

(none material identified from the data accessed). Caveats:
- Forward consensus data not returned by Finnhub on this key — analyst
  dispersion not visible.
- Insider MSPR empty (known issue) — insider axis is NEUTRAL by absence.

## Tool / source calls (audit trail)

| Endpoint | Result |
|----------|--------|
| `/stock/metric?metric=all` | ok — full ratios returned |
| `/stock/earnings?limit=8` | 4 rows returned (1 dropped via look-ahead guard) |
| `/stock/eps-estimate?freq=quarterly` | empty `data` |
| `/stock/revenue-estimate?freq=quarterly` | empty `data` |
| `/stock/peers` | full peer list returned |
| `/stock/insider-sentiment` | empty `data` |
| `fz quote NVDA` | recom 1.27, target $305.72, PEG 0.39, FwdPE 17.19 |
| `fz insider-clusters --days 30 --side buy/sell` | NVDA not present in either |
| `fz quote --tickers <peers>` | mega-cap peer overview returned |
| `fz screen --view valuation/ownership` | semiconductor screen (NVDA not in strict-Semis screen) |

## Tool / source errors

- Finnhub `/eps-estimate` and `/revenue-estimate` returned empty `data` for
  NVDA on this free-tier key — likely silently gated; not a transport error.
- Finnhub `/insider-sentiment` returned empty `data` — see memory
  `data-source-workarounds` ("MSPR empty"). Proxied with `fz`
  insider-clusters (also showed no NVDA activity).
- One earnings row (`period=2026-06-30`) dropped via look-ahead guard — Finnhub
  returned a future quarter in this run.

## Verdict for downstream — the quality gate

```
fundamental_signal:   BULLISH
tier_adjustment:      CAUTION
contradiction_count:  1
insider_cluster:      {present: no, distinct_buyers: n/a, side: n/a}
key_risks:
  - "Fundamentals contradict any *outright short* thesis — the bearish flow
     must be read as capped-upside/yield-enhancement, not deterioration."
  - "Forward-consensus visibility is limited (Finnhub free-tier empty) — phase-9
     cannot quote revision-trend or dispersion; sensitive to a surprise revision."
  - "MSPR data is silent (Finnhub) and the `fz` insider-cluster scan shows no
     NVDA activity in 30d — insider signal is genuinely absent, not negative."
```

**Phase-9 application:** any *outright bearish* directional structure (long puts,
naked short stock) gets **one size-step cut**. A *capped-upside defined-risk*
structure (short call spread at $215–$220, iron condor 200/215–220/230,
collar) is **unaffected** by this gate — the fundamentals don't argue against a
range/yield trade, and may in fact reinforce it (institutions write calls when
the underlying is strong but stretched).
