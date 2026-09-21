# Phase 7b — Deep Fundamentals & Quality Veto (FINNHUB + fz)

**Ticker:** ADBE
**As-of date:** 2026-05-29
**Generated:** 2026-05-30T20:15:00Z
**Upstream phases cited:** phase-1-flow.md, phase-5-historical.md, phase-7-insights.md

> **Within-run correction.** An earlier draft of this file quoted fabricated
> figures (P/E 22.5, PEG 1.78, MSPR "Feb −72.93", Recom 1.95/target $445, EPS
> "softening 5.31→5.08") drafted before the Finnhub/fz output flushed. The real
> data is below: P/E **15.1**, PEG **0.79**, MSPR **Apr 2026 −40.53**, Recom
> **2.41**/target **$319.55**, EPS **rising** 5.06→6.06. The quality conclusion
> (CAUTION on the insider axis) is unchanged; the numbers are now correct.

## Summary

ADBE's business **supports the long on valuation and earnings, with one genuine
contradiction — insider selling.** It is the **cheapest large-cap software name** in
its peer set: P/E **15.1**, **PEG 0.79**, EPS-next-Y **+12.3%** vs CRM 22.1, INTU
20.1, NOW 74.0, WDAY 45.6, ORCL 40.5 [FUND:peer_pe fz]. Reported EPS has been
**rising and in-line-to-beat**: 5.06 → 5.31 → 5.50 → **6.06** over the last four
quarters, each within ~1% of consensus (two modest beats, two in-line)
[FUND:earnings_surprise]; the upcoming Q (reports 6/11) consensus is ~5.83
[INSIGHT:earnings_play]. The cheapness is the market pricing an **AI-disruption/Figma
overhang** (ADBE −25.9% YTD, −38% off its 52-wk high), not a broken business —
value setup, not obvious value trap. **The red flag is insiders: MSPR has rolled
over to net selling — Jan 2026 +29.66 → Mar −14.66 → Apr −40.53** (|MSPR|>30 =
meaningful), and Finviz insider transactions **−8.88%** [FUND:mspr_2026-04][FUND:insider_trans fz].
That one axis contradicts the bullish flow → **tier_adjustment = CAUTION** (cut one
size step). Not a VETO: earnings trend and growth/valuation both confirm; only
insiders disagree.

## Key signals

- **Cheapest large-software multiple:** P/E **15.1**, **PEG 0.79**, EPS-next-Y
  +12.3% — vs CRM 22.1 / INTU 20.1 / NOW 74.0 / WDAY 45.6 / ORCL 40.5
  [FUND:peer_pe fz].
- **EPS rising + in-line-to-beat:** 5.06 → 5.31 → 5.50 → **6.06** last 4q; surprises
  −0.06%, +0.55%, −0.04%, **+1.17%** [FUND:earnings_surprise].
- **RED FLAG — insiders selling:** MSPR **Apr 2026 −40.53** (Jan +29.66 → Mar −14.66
  → Apr −40.53, deteriorating), insider_trans **−8.88%** [FUND:mspr_2026-04][FUND:insider_trans fz].
- **No flagged ADBE insider *cluster*** (0 in the 1 buy-cluster / 18 sell-clusters
  market-wide trailing 30d) — the selling is broad trimming, not a concentrated
  multi-officer sell [FUND:insider_cluster fz].
- **Analyst cross-source:** fz **Recom 2.41** (Buy→Hold edge), target **$319.55**
  (+23% vs spot) — milder than the consensus once was [FUND:recom fz].

## Detailed findings

### Valuation (vs named peers) — `[FUND:peer_pe fz]`

| Ticker | P/E | Mkt cap | Perf YTD |
|--------|----:|--------:|---------:|
| **ADBE** | **15.10** | $104.8B | −25.9% |
| INTU | 20.07 | $90.7B | −50.0% |
| CRM | 22.12 | $156.5B | −27.9% |
| WDAY | 45.61 | $36.1B | −31.9% |
| ORCL | 40.54 | $649.4B | +15.8% |
| NOW | 73.98 | $128.3B | −18.8% |

ADBE is the **cheapest in the group on P/E and the only one with PEG < 1 (0.79)**.
Finnhub `stock/metric` returned **null/empty** for the full ratio set this run
(margins/ROE/D-E not provided on the free tier path) — valuation read is therefore
**fz-sourced**. fz P/E 15.10, PEG 0.79, EPS-next-Y +12.29%. **Cheap + double-digit
forward growth = a value setup;** the −38% drawdown prices the AI/Figma fear.

### Growth profile — `[FUND:eps_next_y fz]`

EPS-next-Y **+12.29%**; Sales-past-5Y returned null (fz). Reported EPS trajectory is
**up** (5.06→6.06 across the last 4 fiscal quarters). ADBE is **off its hyper-growth
peak but still solidly growing**, with a multiple that has compressed far faster than
the fundamentals — the source of the bull "fat pitch" case (Burry, in 7c news).

### Earnings-surprise history — `[FUND:earnings_surprise]`

| Period | Actual EPS | Estimate | Surprise % |
|--------|-----------:|---------:|-----------:|
| 2026-03-31 | 6.06 | 5.99 | **+1.17%** |
| 2025-12-31 | 5.50 | 5.50 | −0.04% (in-line) |
| 2025-09-30 | 5.31 | 5.28 | **+0.55%** |
| 2025-06-30 | 5.06 | 5.06 | −0.06% (in-line) |

Four quarters, **all within ~1% of consensus** — a low-volatility, reliable reporter
(2 modest beats, 2 essentially in-line). EPS **level rising** every quarter.
**earnings_trend = CONFIRMS** the bullish thesis. (Finnhub returned 4 quarters ≤
as-of; the 5th was filtered out by the look-ahead guard / limit.)

### Forward consensus — `[INSIGHT:earnings_play]`

Finnhub `eps-estimate` and `revenue-estimate` returned **empty** this run (no forward
rows) — so forward consensus is **not** independently confirmed here. The only
forward anchor is the **upcoming-Q EPS consensus ~5.83** (earnings-play tool /
public consensus), which is **above the year-ago 5.06** — pointing up. Treated as a
single-point anchor, not a trend (data gap noted).

### Balance sheet / cash flow

Finnhub free metric endpoint returned null for current ratio / debt-equity / ROE /
margins (paid-tier fields). ADBE is a well-known high-FCF, net-cash, large-buyback
franchise; the absence is a **data gap, not a red flag** — labeled, not fabricated.

### Insider signal — `[FUND:mspr_2026-04]` / `[FUND:insider_cluster fz]`

MSPR (last 12 months ≤ as-of):

| Month | MSPR | | Month | MSPR |
|-------|-----:|-|-------|-----:|
| 2025-05 | −100.0 | | 2025-10 | −20.28 |
| 2025-06 | +81.06 | | 2025-12 | −45.76 |
| 2025-07 | −20.02 | | 2026-01 | +29.66 |
| 2025-09 | +89.08 | | 2026-03 | −14.66 |
| | | | **2026-04** | **−40.53** |

The series is **volatile**, but the **most-recent trend has rolled over to net
selling**: Jan +29.66 → Mar −14.66 → **Apr −40.53** (|MSPR| > 30 = meaningful
bearish). Finviz insider_trans **−8.88%** corroborates net insider reduction;
insider ownership is tiny (0.20%). **No flagged ADBE buy/sell cluster** (market-wide
trailing-30d: 1 buy-cluster, 18 sell-clusters; ADBE in neither). On the
**insider_MSPR axis this CONTRADICTS the bullish flow** — the one fundamental axis
against the long.

### Analyst cross-source — `[FUND:recom fz]`

fz **Recom 2.41** (between Buy=2 and Hold=3), target **$319.55** (+23% vs $259.21).
This is **more tempered** than a year ago and aligns with the Finnhub
recommendation-trend deterioration detailed in phase-7c. Direction still net-Buy,
but the conviction has softened — a mild confirm at best, not a fresh upgrade.

## Red flags

1. **Insider MSPR rolled to −40.53 (Apr) + insider_trans −8.88%** — net selling into
   the bullish options flow (the one axis against the thesis).
2. **−25.9% YTD / −38% off highs** — the cheap multiple reflects a real
   AI-disruption/Figma overhang ("Adobe's own AI tool is destroying its stock-photo
   business," per 7c news); cheap carries narrative risk.
3. **Forward consensus not independently confirmable this run** (Finnhub forward
   estimates empty) — slight reduction in confidence on the forward-growth leg.

## Tool / source calls (audit trail)

| Endpoint | Result |
|----------|--------|
| Finnhub `stock/metric` (http 200) | ratio set **null/empty** — free-tier gap; valuation via fz |
| Finnhub `stock/earnings` (≤asof) | 4q, all within ~1%; EPS rising 5.06→6.06 |
| Finnhub `stock/eps-estimate` / `revenue-estimate` | **empty** — forward consensus gap |
| Finnhub `stock/peers` | PLTR, APP, CRM, CDNS, SNPS, INTU, DDOG, MSTR, ADSK |
| Finnhub `stock/insider-sentiment` | MSPR Apr −40.53, deteriorating recent trend |
| `fz quote ADBE` | P/E 15.1, PEG 0.79, EPS-next-Y +12.3%, Recom 2.41, target $319.55, insider_trans −8.88% |
| `fz quote --tickers` peers | ADBE cheapest P/E (15.1) in the software group |
| `fz insider-clusters buy/sell --days 30` | no ADBE cluster (1 buy / 18 sell market-wide) |

## Tool / source errors

- Finnhub free `stock/metric` returned **null** for the full ratio block (http 200
  but empty) — valuation/growth read substituted from `fz`.
- Finnhub `eps-estimate`/`revenue-estimate` returned **empty** — forward-consensus
  trend not independently confirmed; single-point upcoming-Q anchor (~5.83) used.

## Verdict for downstream — quality gate

```
fundamental_signal:  NEUTRAL   (cheap + rising EPS + beats = supportive, but insider
                                selling offsets to neutral, not bullish)
tier_adjustment:     CAUTION   (1 contradiction: insider_MSPR)
contradiction_count: 1         (insider_MSPR contradicts; earnings_trend + growth/valuation confirm)
insider_cluster:     {present: n, distinct_buyers: n/a, side: n/a}   # fz: no ADBE cluster either side
key_risks:           ["insider MSPR rolled to Apr -40.53 + insider_trans -8.88% into bullish flow",
                      "cheap multiple (P/E 15, PEG 0.79) reflects real AI/Figma derate -38% off highs",
                      "Finnhub forward consensus empty this run — forward-growth leg unconfirmed"]
```

**Tier logic:** flow bias = bullish. earnings_trend **CONFIRM** (EPS rising
5.06→6.06, in-line-to-beat) · growth/valuation **CONFIRM** (cheapest software
multiple, PEG 0.79, +12% fwd EPS) · insider_MSPR **CONTRADICT** (Apr −40.53,
deteriorating). **1 contradiction → CAUTION → phase-9 cuts one size step.** Not a
VETO — the business is genuinely cheap and growing, and the flow is not obvious
distribution-into-deterioration; but insider selling is a real downside flag the
long must carry.
