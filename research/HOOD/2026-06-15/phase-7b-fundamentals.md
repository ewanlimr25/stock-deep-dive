# Phase 7b — Deep Fundamentals & Quality Veto (FINNHUB)

**Ticker:** HOOD
**As-of date:** 2026-06-15
**Generated:** 2026-06-16T13:00:00Z
**Upstream phases cited:** phase-2-dark-pool.md, phase-6-macro.md, phase-7-insights.md

## Summary

The underlying business **quality supports** the accumulation thesis, with **one
caution**: HOOD is a high-growth, high-margin franchise (revenue +41.5% YoY, net margin
41.1%, operating margin 46.3%, ROE 21.6%, gross margin 95.2%) — consistent with phase-2
institutional buying — but it trades at a **premium multiple** (PE 46.6, PEG 2.48, P/S
19.2, ~2.6× the PE of broker peers SCHW/MS/GS) and its **earnings momentum is
decelerating** (surprise trend +31.8% → +12.0% → +3.2% → **−12.5% miss** in Q1'26).
Insider sentiment was net-selling across most of 2025/early-2026 but has **recently
flipped positive** (MSPR May +24.5, **Jun +32.8**), with no clustered insider buying.
Net: one of three quality axes (earnings_trend) contradicts the bullish flow →
**tier_adjustment = CAUTION** (cut one size step). The growth/margins axis strongly
confirms; insider axis is recently neutral-to-positive.

## Key signals

- High-quality growth: **rev +41.5% YoY, net margin 41.1%, ROE 21.6%** `[FUND:growth]`
  — confirms accumulation.
- **Premium valuation**: PE 46.6, PEG 2.48, P/S 19.2 vs SCHW 18 / MS 19.7 / GS 19.7
  `[FUND:peer_pe fz]` — priced for hypergrowth.
- **Decelerating earnings**: +31.8%→+12.0%→+3.2%→**−12.5% (Q1'26 miss)**
  `[FUND:earnings_surprise]` — the one contradiction.
- **Insider MSPR recently positive** (May +24.5, Jun +32.8) after a year of selling;
  **no insider cluster** `[FUND:mspr][FUND:insider_cluster fz]`.
- **Analyst recom 1.72 (buy), target $102.91** (+5%) — bullish but target sits **at
  the $100 ceiling** (phase-3/4) `[FUND:recom fz]`.

## Detailed findings

### Valuation `[FUND:metric][FUND:peer_pe fz]`

PE TTM **46.62** (normalized 46.97), P/B **11.13**, P/S **19.17**, **PEG 2.48** —
expensive even for the growth. Peer table:

| Ticker | P/E | Mkt Cap | Perf YTD | Note |
|--------|----:|--------:|---------:|------|
| **HOOD** | **47.45** | $88.4B | **−13.24%** | richest ex-AFRM; worst YTD |
| SCHW | 18.04 | $158.2B | −8.97% | retail-broker, cheap |
| IBKR | 39.88 | $41.3B | +44.24% | fintech-broker, leader |
| MS | 19.74 | $343.8B | +22.78% | IB |
| GS | 19.67 | $317.5B | +22.43% | IB |
| AFRM | 65.34 | $24.1B | −3.40% | fintech (≥5 confluence, phase-7) |

(`fz --tickers` overview lacks SI/float; HOOD short float **4.52%**, float 760.74M from
phase-0.) HOOD's multiple is justified *only* by its growth premium — it is the
group's **worst YTD performer** (−13.2%), now bouncing +28% off lows.

### Growth profile `[FUND:metric]`

Revenue growth TTM YoY **+41.5%**, EPS growth TTM YoY **+18.7%**, gross margin 95.2%,
operating margin 46.3%, net margin 41.1%, ROE 21.6%, ROA 4.73%, current ratio 1.26, no
material LT debt. **Excellent quality + growth** — this axis strongly *confirms* the
bullish flow and the dark-pool accumulation.

### Earnings-surprise history `[FUND:earnings_surprise]`

| Period | Actual EPS | Estimate | Surprise | Surprise % |
|--------|-----------:|---------:|---------:|-----------:|
| 2026-03-31 (Q1'26) | 0.38 | 0.4343 | −0.0543 | **−12.50%** |
| 2025-12-31 (Q4'25) | 0.66 | 0.6398 | +0.0202 | +3.16% |
| 2025-09-30 (Q3'25) | 0.61 | 0.5446 | +0.0654 | +12.01% |
| 2025-06-30 (Q2'25) | 0.42 | 0.3187 | +0.1013 | +31.79% |

Beat-rate 3/4 (75%) but the **surprise magnitude is monotonically deteriorating** and
the latest quarter is a **miss**. ⚠️ earnings_trend axis **contradicts** the strong
bullish thesis.

### Forward consensus

Finnhub `eps-estimate` / `revenue-estimate` → **403 "You don't have access"** (paid
tier). Proxy from management guidance (phase-6 WebSearch): **Q2'26 EPS $0.45 / rev
$1.234B, Q3'26 EPS $0.50** — sequentially *improving*. So forward direction is up per
guidance, partially offsetting the trailing deceleration; treat as soft (guidance, not
independent consensus).

### Balance-sheet & cash-flow

`financials-reported` not pulled (typically paid). Proxy from metrics: no material LT
debt, current ratio 1.26, net margin 41% + ROE 21.6% imply healthy cash generation.
Balance sheet is **not** a risk for this name.

### Insider signal `[FUND:mspr][FUND:insider_cluster fz]`

MSPR (recent 12 mo, ≤ as-of): 2025-7 −33.6, -8 −43.5, -9 −16.0, -10 −33.7, -11 −17.5,
-12 −33.3, 2026-1 −33.6, -2 **−55.9**, -3 +26.1, -4 −34.9, -5 **+24.5**, -6 **+32.8**.
Dominant pattern = **net selling through 2025/early-2026**, then a **recent flip
positive** (Mar, May, Jun all >+24; Jun +32.8 > 30 threshold). ⚠️ June is the partial
current month (as-of 6/15) — note look-ahead borderline; May +24.5 is clean.
`fz insider-clusters` (30d, ≥2 buyers): **HOOD not present in buy OR sell clusters** →
no clustered conviction; the recent MSPR uptick is not a multi-officer buy cluster.
Net read: insider axis is **neutral-to-recently-improving** — does *not* cleanly
contradict the bullish flow.

### Peers — relative value

Peer list (Finnhub): MS, GS, SCHW, IBKR, RJF, LPLA, EVR, JEF, SF, SNEX, HLI — all
**traditional brokers/IBs**, confirming HOOD's economic comp is **Financial Services**
(not UW's "Technology" tag). vs the retail-broker comps (SCHW PE 18, IBKR 40), HOOD at
47 is the expensive fast-grower; analyst target $102.91 implies the Street sees it
fairly valued into the $100–103 ceiling.

## Red flags

- Premium multiple (PE 47 / PEG 2.48) on a name that's the **worst YTD performer** in
  its peer group — vulnerable to multiple compression on any growth wobble.
- **Decelerating earnings momentum** → Q1'26 miss; next print Aug 5 (out of window).
- High **beta 2.34** — amplifies the TRANSITIONAL/weak-breadth market downside (phase-6).

## Tool / source calls (audit trail)

| Endpoint | Status | Key value(s) |
|----------|--------|--------------|
| `/stock/metric?metric=all` | ok | PE 46.6, PEG 2.48, rev_g +41.5%, ROE 21.6%, beta 2.34 |
| `/stock/earnings?limit=8` | ok (4 qtrs) | beat-rate 3/4; Q1'26 −12.5% miss |
| `/stock/eps-estimate` | **403 paid** | — (proxy: mgmt guide Q2 $0.45) |
| `/stock/revenue-estimate` | **403 paid** | — (proxy: mgmt guide $1.234B) |
| `/stock/peers` | ok (12) | broker/IB peer set |
| `/stock/insider-sentiment` | ok | MSPR May +24.5, Jun +32.8; net-selling 2025 |
| `fz quote --tickers …` | ok | peer PE: SCHW 18, IBKR 40, MS 19.7, GS 19.7, AFRM 65 |
| `fz insider-clusters buy/sell` | ok | HOOD absent both → no cluster |
| `fz quote HOOD .Recom/.Target` | ok | recom 1.72, target $102.91 |

## Tool / source errors

- Finnhub `eps-estimate` & `revenue-estimate` → 403 "You don't have access to this
  resource" (paid tier) — forward consensus unavailable; proxied with management
  guidance (phase-6). Not a blocker.

## DATA NOTE / CORRECTION

- June-2026 MSPR (+32.76) is the partial current month (as-of 6/15) — flagged
  look-ahead-borderline; the clean prior month (May +24.5) is also positive, so the
  "recent improvement" read holds either way.

## Verdict for downstream phases (QUALITY GATE)

```
fundamental_signal:  BULLISH        # high growth + margins + ROE confirm accumulation
tier_adjustment:     CAUTION        # 1 axis contradicts → cut one size step
contradiction_count: 1             # {earnings_trend} contradicts; growth/margins CONFIRMS; insider_MSPR NEUTRAL
insider_cluster:     {present: no, distinct_buyers: n/a, side: n/a}
key_risks:           ["Premium PE 46.6/PEG 2.48 — worst YTD performer in peer group, multiple-compression risk",
                      "Decelerating earnings: +32%->+12%->+3%->-12.5% (Q1'26 miss); next print Aug 5",
                      "Beta 2.34 amplifies TRANSITIONAL/weak-breadth market downside (phase-6)"]
```

- **Effect on phase-9:** **CAUTION → cut one size step.** The growth/quality is real and
  confirms the accumulation, but the decelerating earnings + premium multiple in a
  cautious tape argue against full size. Not a VETO (only 1 of 3 axes contradicts; the
  balance sheet and growth are strong).
- **Open questions:** Does phase-7c short-interest add a squeeze tailwind (SI 4.52% is
  modest) or a crowded-long warning? Is the Street target $102.91 (≈$100 wall) the right
  cap for phase-9's profit target?
