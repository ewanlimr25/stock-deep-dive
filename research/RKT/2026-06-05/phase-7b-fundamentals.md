# Phase 7b — Deep Fundamentals & Quality Veto (FINNHUB)

**Ticker:** RKT
**As-of date:** 2026-06-05
**Generated:** 2026-06-06T18:05:00-04:00
**Upstream phases cited:** phase-0-intake.md, phase-5-historical.md, phase-6-macro.md, phase-7-insights.md

## Summary

The underlying business is **improving, not deteriorating** — which cuts
*against* the weak-bear flow baseline from phase-7. RKT has beaten EPS
consensus in **4 of 4** available quarters (surprises +25.6% to +50.5%),
TTM revenue is +75.31% YoY and EPS +266.46% (heavily inorganic — Redfin and
Mr. Cooper deals), Q1-2026 printed $2.941B revenue / $297M net income / $1.86B
operating cash flow, and the forward multiple (11.61×) implies ~48% forward EPS
growth with a consensus Buy (Recom 1.94) and $20.27 target (+60% vs $12.65).
Quality caveats are real — TTM net margin 2.69%, ROE 1.53%, zero insider
open-market buying at the 52-week low — but on the rubric's three axes,
**two contradict the bearish flow bias → `tier_adjustment = VETO`** for any
naked directional short. This is a downside-only gate on the short thesis:
defined-risk expressions only.

## Key signals

- Earnings-surprise history **4/4 beats**: +25.63%, +25.71%, +50.54%, +46.52%
  (no misses in the available window) [FUND:earnings_surprises]
- `revenueGrowthTTMYoy` **+75.31**, `epsGrowthTTMYoy` **+266.46** — but
  acquisition-driven (Redfin Jul-2025, Mr. Cooper Oct-2025); organic split not
  disclosed in free tier [FUND:metric]
- Q1-2026 (2026-03-31): revenue **$2,941,000,000**, net income **$297,000,000**,
  operating cash flow **+$1,857,000,000**, capex $43M [FUND:financials_reported]
- Valuation split personality: peTTM 149.5 (fz: 214.4 — different EPS bases)
  vs **Forward P/E 11.61, PEG 0.18**; peers UWMC 5.03 / PFSI 5.61 fwd — RKT at
  ~2× its direct comps [FUND:metric][FUND:peer_pe fz]
- Insider tape: **0 open-market purchases (code P)** in 6 months; 25 S-code
  sales (−62,500 sh), 19 F-code tax-vest dispositions (−1.72M sh, mechanical),
  10 A-code awards (+3.0M sh). No fz buy- or sell-cluster
  [FUND:insider_tx][FUND:insider_cluster fz]
- Analyst cross-source: `Recom` **1.94** (buy), `Target Price` **$20.27**
  (+60.2% vs spot) [FUND:recom fz]

## Detailed findings

### Valuation (vs named peers)

| Metric | RKT | Note |
|---|---|---|
| P/E (TTM) | 149.52 Finnhub / 214.41 fz | epsTTM $0.059 — optically meaningless |
| Forward P/E | **11.61** | implies fwd EPS ≈ $1.09 |
| PEG | 0.18 | cheap on expected growth |
| P/B | 1.54 | |
| P/S (TTM) | 4.02–4.30 | rich vs originator peers |
| Market cap | $35.79B | |
| Beta | 2.24 | high-beta in a risk-off tape (phase-6) |

### Growth profile

TTM YoY: revenue +75.31%, EPS +266.46% — **flagged: inorganic**, the Redfin
(2025-07) and Mr. Cooper (2025-10) closings dominate the comp. Margins:
operating 20.81% TTM, **net 2.69% TTM** (Q1-2026 standalone ≈10.1% —
improving), ROE 1.53%, ROA 0.52%. Profitability is thin at the TTM level;
the Q1 print shows the merged entity scaling.

### Earnings-surprise history (all available; look-ahead filter `period <= 2026-06-05` applied — 4 rows returned by the API)

| Period | Actual EPS | Estimate | Surprise | Surprise % |
|---|---:|---:|---:|---:|
| 2026-03-31 | 0.15 | 0.1194 | +0.0306 | **+25.63%** |
| 2025-12-31 | 0.11 | 0.0875 | +0.0225 | +25.71% |
| 2025-09-30 | 0.07 | 0.0465 | +0.0235 | +50.54% |
| 2025-06-30 | 0.04 | 0.0273 | +0.0127 | +46.52% |

Beat-rate **4/4 (100%)** with accelerating actuals (0.04 → 0.15).

### Forward consensus

Finnhub `eps-estimate` / `revenue-estimate`: **403 — "You don't have access to
this resource." (paid tier, skipped)**. Proxy from fz (labeled): EPS next Y
growth **+48.19%**, Forward P/E 11.61, Recom 1.94, Target $20.27
[FUND:recom fz]. Direction of recent *revisions* is phase-7c's news lane.

### Balance-sheet health

Free-tier metric proxies: LT-debt/equity **0.449**, current ratio 0.17
(typical originator structure — warehouse funding; not a distress read),
totalDebt/equity n/a. Statements (free on this key, 21 quarters) show nothing
alarming at the top lines; full leverage walk not built (line-item parse out of
scope).

### Cash-flow quality

Q1-2026 OCF **+$1.857B** vs capex $43M — asset-light, strongly cash-generative
this quarter. Caveat: originator OCF swings with origination volume/MSR
moves; one quarter ≠ run-rate.

### Insider signal (MSPR fallback)

`insider-sentiment` (MSPR): **empty `data: []`** (known gap — fell back to
`insider-transactions` by code, per documented workaround). 6-month window
(2025-12-05 → 2026-06-05), 59 transactions:

| Code | Meaning | n | Net shares |
|---|---|---|---|
| P | open-market buy | **0** | 0 |
| S | open-market sell | 25 | −62,500 |
| F | tax-withhold on vest | 19 | −1,717,115 (mechanical) |
| A | award/grant | 10 | +3,003,314 |
| G/J/M | gift/other/exercise | 5 | −107,856 |

**No insider has bought stock in the open market in six months** — including
through the slide to the 52-week low. Recent prints are all F-code (e.g.
Malhotra 2026-05-06 −52,484 @ $14.09). fz clusters: RKT in **neither** the
buy-cluster (2 market-wide) nor sell-cluster (28) lists
[FUND:insider_cluster fz].

### Peers — relative value (fz `ind_mortgagefinance` screen; Finnhub peer list: FNMA, ACT, MTG, UWMC, RDN, PFSI, FMCC, NMIH, MBIN, AGM)

| Ticker | P/E | Fwd P/E | EPS Next Y | Short Float | Float |
|---|---:|---:|---:|---:|---:|
| **RKT** | 214.41 | **11.61** | +48.19% | 7.48% | 960.91M |
| UWMC | 9.63 | 5.03 | +29.87% | 13.14% | 328.70M |
| PFSI | 8.63 | 5.61 | +34.39% | 5.89% | 34.22M |
| WD | 25.37 | 11.05 | +29.18% | 3.47% | 32.95M |
| VEL | 6.32 | 5.11 | +21.82% | 4.46% | 24.59M |
| LDI | — | 5.83 | +1720% (base effect) | 15.82% | 110.38M |
| BETR | — | 131.38 | +103.33% | **30.82%** | 7.21M |

RKT carries ~2× the forward multiple of its closest comps (UWMC/PFSI) — the
market already pays up for the platform/scale story; SI 7.48% is mid-pack (no
squeeze-fuel standout vs UWMC 13.1% or LDI 15.8%). Inst own 29.58%, insider own
66.04% (Gilbert/RHI — the L-1 overhang class, phase-6).

## Red flags

1. **Zero insider open-market buying at 52-week lows** + steady S/F-code supply
   — nobody inside is defending the price; pairs badly with the 06-30 L-1
   unlock (phase-6-macro.md §Catalysts).
2. **Thin TTM profitability** (net 2.69%, ROE 1.53%) — little cushion if
   mortgage rates stay 6.6%+ (phase-6 headwind).
3. **Growth optics are inorganic** — the +75%/+266% TTM comps embed two
   mergers; integration risk and the 2× peer forward multiple leave room for
   de-rating if the cycle doesn't turn.

## Tool / source calls

| Source | Status |
|---|---|
| Finnhub `/stock/metric` | ok |
| Finnhub `/stock/earnings` (limit 8, look-ahead filtered) | ok — 4 rows |
| Finnhub `/stock/eps-estimate` | **403 paid, skipped** |
| Finnhub `/stock/revenue-estimate` | **403 paid, skipped** |
| Finnhub `/stock/peers` | ok |
| Finnhub `/stock/insider-sentiment` (MSPR) | empty `[]` → fallback |
| Finnhub `/stock/insider-transactions` (6mo, by code) | ok — 59 rows |
| Finnhub `/stock/financials-reported` | ok (free) — Q1-26 IC/CF lines |
| `fz insider-clusters --days 30 --min-buyers 2 --side buy/sell` | ok — no RKT |
| `fz screen --filter ind_mortgagefinance --view ownership/valuation` | ok — 13 names |
| `fz quote RKT` (Recom/Target) | ok |
| `fz quote --tickers <peers>` | **HTTP 404 (quote.ashx)** — superseded by the industry screen |

## Tool / source errors

- `eps-estimate` / `revenue-estimate`: `{"error":"You don't have access to this
  resource."}` — paid tier; forward consensus proxied from fz (labeled).
- `insider-sentiment`: `{"data":[],"symbol":"RKT"}` — empty; fell back to
  insider-transactions by code (documented workaround).
- `fz quote --tickers …`: `Error: GET /quote.ashx returned HTTP 404` — Finviz
  multi-ticker endpoint failure; peer table built from `fz screen` instead.
- Point-in-time caveat: `/stock/metric` ratios are TTM-current (pulled
  2026-06-06, one session after as-of) — drift risk negligible at this gap.

## DATA NOTE / CORRECTION

None — values from validated reads; failed endpoints recorded above, nothing
transcribed from them.

## Verdict for downstream

Flow bias being gated (plurality of phases 1–7): **weak-bear / capped-upside**.

| Axis | Read | vs bear flow bias |
|---|---|---|
| (a) earnings_trend | 4/4 beats, accelerating actuals, fwd +48% (fz proxy) | **contradicts** |
| (b) insider | MSPR n/a; 0 open-market buys, mild S-code selling, no clusters | does not contradict (mildly confirms) |
| (c) growth/margins | rev +75%/EPS +266% (inorganic), Q1 NI $297M & OCF $1.86B improving; margins thin | **contradicts** (improving, not deteriorating) |

```
fundamental_signal:  BULLISH
tier_adjustment:     VETO        # ≥2 axes contradict the SHORT thesis →
                                 # naked directional short = watch-only/0%;
                                 # carry-only defined-risk expressions allowed
contradiction_count: 2           # earnings_trend, growth/margins
insider_cluster:     {present: n, distinct_buyers: n/a, side: n/a}
key_risks:
  - Growth is acquisition-driven (Redfin/Mr. Cooper) — TTM optics overstate organic momentum; 2× peer fwd multiple = de-rating room
  - Thin profitability (net 2.69% TTM, ROE 1.53%) — no cushion if 30y stays >6.5% (phase-6)
  - Zero insider open-market buying at 52w low + 2026-06-30 L-1 unlock = supply with no inside bid
```

Note the symmetry clause: this VETO blocks the *naked short* (improving
underlying → bearish flow may be hedging/macro, not informed distribution). It
does **not** make the long case — the gate never raises conviction
(phase-7b is downside-only), and the red flags above carry to phase-9 against
any long expression too.
