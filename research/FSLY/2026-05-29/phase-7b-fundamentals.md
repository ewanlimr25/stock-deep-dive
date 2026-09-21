# Phase 7b — Deep Fundamentals & Quality Veto

## Summary

Fastly is an **unprofitable-but-sharply-improving turnaround** — the fundamentals do
**not veto** the (small, optionality-style) long, but they do flag a real quality
caveat that caps conviction. The business is still loss-making (**TTM EPS −0.69,
operating margin −16.0%, ROE −10.7%, no trailing P/E**), yet every *trend* axis is
improving fast: **Sales Q/Q +19.8%, EPS Q/Q +51.1%**, EPS-next-Y +21.5%, and the
**earnings-surprise trajectory is sharply positive** — last four quarters −0.03 →
0.07 → 0.12 (beat **+112%**) → **0.13 (beat +58%)**, i.e. **crossing into
profitability** on accelerating beats. Gross margin is healthy at **56.9%** (the
software unit economics are fine; the losses are opex/scale). Valuation is a growth
re-rating: **forward P/E 45, PEG 0.84, P/S 4.26**, analyst Recom **2.42 (Buy-ish),
target $25.20 (+42%)**.

This is the **mirror-image of CRM's profile**: CRM was cheap+profitable+beating;
FSLY is **expensive+unprofitable+improving**. Neither is a veto, but FSLY's quality
is *lower* — the long depends on the turnaround/squeeze narrative continuing, and a
−16% operating margin means there's no earnings floor under the stock if momentum
fails. Per the rubric this is **CONFIRM (0 hard contradictions — earnings_trend and
growth both improving)**, but I'm flagging the unprofitability + rich forward
multiple as the carried quality risk, which argues against sizing at the top of any
band.

## Key signals

1. `[FUND:earnings_surprise]` Surprise trajectory −0.03 → +0.07 → +0.12 (+112%) →
   **+0.13 (+58%)** — crossing into profitability, accelerating beats. (CONFIRMS flow.)
2. `[FUND:growth fz]` **Sales Q/Q +19.8%, EPS Q/Q +51.1%**, EPS-next-Y +21.5% —
   growth re-accelerating. (CONFIRMS flow.)
3. `[FUND:operatingMargin fz]` **Operating margin −16.0%, ROE −10.7%, TTM EPS −0.69**
   — still unprofitable: the quality caveat.
4. `[FUND:grossMargin fz]` **Gross margin 56.9%** — software unit economics intact;
   losses are scale/opex, not a broken model.
5. `[FUND:forwardPE fz]` **Fwd P/E 45, PEG 0.84, target $25.20 (+42%)** — growth-
   priced; rich on near-zero earnings but PEG <1 on the growth rate.

## Detailed findings

### Valuation (vs CDN/infra peers)

| Ticker | P/E | Perf YTD | Note |
|--------|----:|---------:|------|
| ESTC | 18.5 | −14.2% | profitable, cheap |
| AKAM | 50.4 | +71.4% | profitable incumbent |
| **FSLY** | **— (neg)** | **+74.5%** | **unprofitable, best YTD** |
| NET | — (neg) | +22.7% | unprofitable growth |
| DDOG | 660 | +81.9% | profitable, extreme multiple |

- FSLY sits with the **unprofitable growth-CDN cohort** (NET) on losses but leads on
  YTD momentum (+74.5%). Forward P/E 45 / PEG 0.84 prices a turnaround that the
  beat-trajectory supports but does not guarantee.

### Growth profile

- Sales Q/Q **+19.8%**, EPS Q/Q **+51.1%**, EPS-next-Y +21.5%, EPS-next-5Y +53.6%,
  TTM revenue **$652.6M**. Gross margin 56.9%. Growth is **re-accelerating** — the
  core of the bull/turnaround case.

### Earnings-surprise history `[FUND:earnings_surprise]`

| Period (FQ end) | Actual EPS | Estimate | Surprise % |
|-----------------|-----------:|---------:|-----------:|
| 2025-06-30 | −0.03 | −0.050 | +40.2% |
| 2025-09-30 | 0.07 | 0.00 | (n/a) |
| 2025-12-31 | 0.12 | 0.057 | **+111.6%** |
| 2026-03-31 | 0.13 | 0.082 | **+58.3%** |

- **4/4 beats, crossing from loss into profit, accelerating** — the strongest
  fundamental support for the long. (All periods ≤ as-of; no look-ahead.)

### Balance-sheet health

- **Debt/Equity 0.41** (low — clean balance sheet, no leverage risk), P/B 2.84.
  Current ratio not returned by `fz`. For a cash-burning small-cap, the low leverage
  is a genuine positive (runway risk is lower than the −16% margin alone suggests).

### Cash-flow quality

- Not directly pulled; with −16% operating margin and −15.8% net margin, FCF is
  likely still negative-to-breakeven, improving with the EPS trajectory. No proxy for
  a *deteriorating* trend — the direction is toward profitability.

### Insider signal

- **MSPR: empty** (Finnhub returned 0 rows). Per rubric, absence = weak/neutral, not
  bullish. No insider-buy confirmation; no `fz` cluster run.

### Peers — relative value

- Unprofitable cohort (FSLY, NET) trades on P/S and growth, not P/E. FSLY's +74.5%
  YTD is the cohort's best — it has *already* re-rated hard, so the "cheap" case is
  weaker than CRM's; this is a momentum/turnaround long, not a value long.

## Tool / source calls

```bash
fz quote FSLY --agent
fz quote --tickers FSLY,NET,AKAM,DDOG,ESTC --agent
curl .../stock/earnings?symbol=FSLY&limit=8          # surprise history (<= as-of)
curl .../stock/insider-sentiment?symbol=FSLY&...     # MSPR — empty
```

## Tool / source errors

- Finnhub `insider-sentiment` returned **no data** (MSPR axis unavailable → neutral).
- `fz --tickers` flat view: P/S returned None for the cohort (overview limitation);
  P/E + Perf YTD usable. Not blocking.

## Verdict for downstream

```
fundamental_signal:  BULLISH (improving turnaround) — but lower-quality than a profitable name
tier_adjustment:     CONFIRM         # 0 hard contradictions: earnings_trend + growth both improving
contradiction_count: 0
insider_cluster:     {present: n, distinct_buyers: n/a, side: n/a}   # MSPR empty
key_risks: [
  "Still unprofitable: -16% operating margin, ROE -10.7%, no earnings floor if momentum fails",
  "Already re-rated +74.5% YTD on fwd P/E 45 - the cheap/value case is weak; this is momentum/turnaround",
  "Insider MSPR empty - no insider-buy confirmation of the bullish OI"
]
```

## Tier-adjustment rubric application

- **earnings_trend** (4/4 beats, crossing into profit, accelerating) → **CONFIRMS**.
- **growth/margins** (Sales/EPS growth re-accelerating, gross margin 56.9%) →
  **CONFIRMS** (margins still negative but *improving* — direction confirms).
- **insider_MSPR** (empty) → neutral/NA.
- Contradictions = **0** → `CONFIRM`. The gate does not cut, **but** the
  unprofitability + rich forward multiple is logged as a conviction-capping caveat
  (it prevents sizing at the top of the band; it does not trigger a step-cut).

## Read-through

- Fundamentals **clear the veto and mildly support** the long: a clean balance sheet
  (D/E 0.41), 56.9% gross margins, and a 4-quarter beat streak crossing into profit
  mean this is a *credible turnaround*, not a value-trap-into-distribution. There's no
  deteriorating business to front-run — so, like CRM, the bullish OI/flow isn't smart-
  money distribution.
- **But the quality is genuinely lower than a profitable compounder:** −16% operating
  margin = no earnings floor, and +74.5% YTD on fwd P/E 45 means the easy re-rating is
  done. This is a **momentum/turnaround/squeeze long, not a value long** — its payoff
  depends on the narrative and the short base (phase-3), not a valuation cushion.
- **Net:** CONFIRM, but the caveats reinforce phases 4/5/7's "small, defined-risk,
  optionality" framing — the fundamentals justify *participating* in the squeeze
  structure, not *sizing up* into an unprofitable name that's already run.

## Citations

- `[FUND:earnings_surprise]` 4/4 beats crossing into profit: 0.12 (+112%), 0.13 (+58%) — Finnhub `/stock/earnings`
- `[FUND:growth fz]` Sales Q/Q +19.8%, EPS Q/Q +51.1%, gross margin 56.9% — `fz quote FSLY`
- `[FUND:operatingMargin fz]` operating margin −16.0%, ROE −10.7%, TTM EPS −0.69 (unprofitable) — `fz quote FSLY`
- `[FUND:forwardPE fz]` fwd P/E 45, PEG 0.84, D/E 0.41, target $25.20 (+42%) — `fz quote FSLY`

## Upstream references

- phase-3-positioning.md §Summary — "squeeze ladder + 14.6% short float"; phase-7b
  confirms there's a *real improving business* under the squeeze (4 beats, 56.9% GM),
  so the bullish OI isn't distribution — but the −16% margin caps conviction.
- phase-5-historical.md §VRP — "cheap vol, premium-buying"; phase-7b's turnaround +
  clean balance sheet support expressing that via defined-risk upside, sized small.

## Next phase

- phase-7c-sentiment.md (positioning gate: the 14.6% short float / borrow, news tone,
  analyst revisions — is the short base squeeze fuel or a warning, and is the crowd
  euphoric on a +74.5% YTD name?)
