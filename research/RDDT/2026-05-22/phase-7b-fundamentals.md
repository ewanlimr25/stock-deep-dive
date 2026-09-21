# Phase 7b — Deep Fundamentals & Quality Veto (FINNHUB)

**Ticker:** RDDT
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T00:00:00Z
**Upstream phases cited:** phase-1-flow.md, phase-5-historical.md, phase-6-macro.md,
phase-7-insights.md

## Summary

The underlying business **directly contradicts the bearish flow thesis** — this is
a textbook quality VETO on a conviction short. RDDT is a **hyper-growth, serially
beating, fortress-balance-sheet** name: revenue **+70.6% YoY**, EPS **+460% YoY**,
gross margin **91.4%**, operating margin **25.1%**, ROE **25.5%**, current ratio
**11.6**, **no long-term debt**, and **4 consecutive earnings beats** (avg surprise
≈ +72%, most recent Q1'26 actual $1.01 vs $0.589 est, +71.4%). On the rubric's three
axes vs the bearish flow bias, **two contradict** (earnings_trend ✓ improving,
growth/margins ✓ strong) and one does not (insider — CEO Huffman *selling* per
phase-6, MSPR endpoint empty) → **`tier_adjustment = VETO`** of a fresh directional
short. The crucial caveat: the bear case (phase-6 Meta "Forum" competition, ad-growth
deceleration, generative-AI disruption) is a **forward** risk that trailing TTM data
cannot see, and the forward-consensus endpoints are paid/unavailable (anecdotally,
Raymond James cut its PT $250→$225). So the VETO means: **do not short this business
with size on trailing quality this strong and a PEG of 0.095** — the heavy bearish
tape is far more likely **hedging / profit-taking on a high-flyer already −50% off
its 52-wk high ($283)** than a conviction bet on a deteriorating company. A small,
defined-risk, catalyst-aware bearish expression remains permissible (carry-only).

## Key signals

- **4/4 earnings beats**, avg surprise ≈ +72%; Q1'26 +71.4%, Q4'25 +29.2%, Q3'25
  +54.0%, Q2'25 +133.4% — serial beater [FUND:earnings_surprise]
- Revenue **+70.6% YoY**, EPS **+460% YoY** — explosive growth / profitability
  inflection [FUND:revenueGrowthTTMYoy] [FUND:epsGrowthTTMYoy]
- Gross margin **91.4%**, operating margin **25.1%**, ROE **25.5%**, ROA 23.1% —
  elite software-like economics [FUND:margins]
- **No LT debt**, current ratio **11.6** — fortress balance sheet (net cash)
  [FUND:currentRatioAnnual]
- **PEG 0.095** (PE 38.5 TTM / 51.5 normalized vs ~460% EPS growth) — cheap vs
  growth, though P/S 11.0 & P/B 14.9 are absolutely rich [FUND:pegRatio]

## Detailed findings

### Valuation (vs peers)

- peTTM **38.5**, peNormalizedAnnual **51.5**, P/S **11.0**, P/B **14.9**,
  **PEG 0.095**, beta **2.15** (2× market — high). 52-wk range **$95.23–$282.95**;
  spot $141.67 = **−49.9% off the high, +48.8% off the low.**
- Read: not a value name on absolute P/S/P/B, but the growth is so strong that PEG is
  near-zero. The high beta means it amplifies market moves (ties to phase-4 short
  gamma + phase-6 TRANSITIONAL regime — RDDT will move more than the tape).

### Growth profile

Revenue +70.6% YoY and EPS +460% YoY (profitability inflection). Margins elite and
expanding (GM 91.4%, OM 25.1%). This is a business in the steep part of its S-curve —
**the opposite of the deteriorating fundamentals the bearish flow would need to
validate a conviction short.**

### Earnings-surprise history (last 4 quarters available, ≤ as-of)

| Period | Actual EPS | Estimate | Surprise | Surprise % |
|--------|-----------:|---------:|---------:|-----------:|
| 2026-03-31 (Q1) | 1.01 | 0.589 | +0.421 | **+71.4%** |
| 2025-12-31 (Q4) | 1.24 | 0.960 | +0.280 | +29.2% |
| 2025-09-30 (Q3) | 0.80 | 0.520 | +0.280 | +54.0% |
| 2025-06-30 (Q2) | 0.45 | 0.193 | +0.257 | +133.4% |

**Beat-rate 4/4 (100%), avg surprise ≈ +72%.** A serial, large-magnitude beater.
(Finnhub returned only 4 quarters ≤ as-of; RDDT's short public history limits the
sample but the trend is unambiguous.)

### Forward consensus

**Not available** — `eps-estimate` / `revenue-estimate` are paid-tier on this key
(memory: Finnhub estimates paid). This is the **one axis that could capture the
ad-growth deceleration** the bear case rests on. Proxy from phase-6 WebSearch:
analysts remain "Buy" (avg PT ~$225) but **Raymond James cut its PT $250→$225** and
flagged slowing ad growth — i.e. forward consensus is *softening at the margin* even
as trailing beats. **Flag this blind spot for phase-9.**

### Balance-sheet & cash-flow health

`financials-reported` not pulled (typically paid); proxying from metrics: **no LT
debt, current ratio 11.6, ROA 23.1%, ROE 25.5%, 91% gross margin** → strongly cash
generative, no solvency risk. Cash-flow quality is high (proxy).

### Insider signal (MSPR)

Finnhub `insider-sentiment` returned **empty `[]`** for RDDT (as anticipated — memory
note). No MSPR series. **However, phase-6 WebSearch found CEO Steve Huffman insider
SELLING** in May 2026 — qualitatively a bearish-leaning insider signal that *supports*
the bearish flow (so this axis does **not** contradict the bearish thesis). Treat as
soft-bearish, not quantified.

### Peers

GOOGL, META, PINS, SNAP, MTCH, RUM, IAC, CARG, DJT, GRND. Social/ad/communication
cohort. Relative-value context: RDDT's 70% revenue growth dwarfs mature peers
(GOOGL/META), justifying a premium multiple — but it competes for ad budgets with
exactly those peers, and **META is now also a direct product competitor (Forum)**.

## Red flags

- **Forward ad-growth deceleration** from Meta "Forum" competition + generative-AI
  disruption — NOT visible in trailing TTM; the real bear thesis. ⚠️
- **CEO insider selling** (phase-6) — confidence flag.
- **Absolute multiples rich** (P/S 11.0, P/B 14.9) — high downside if growth derates;
  beta 2.15 amplifies. A multiple compression on a growth scare is the tail risk.

## Tool / source calls (audit trail)

| Endpoint | Status |
|----------|--------|
| `/stock/metric` (key metrics) | ✅ ok |
| `/stock/earnings` (surprises) | ✅ ok (4 qtrs ≤ as-of) |
| `/stock/peers` | ✅ ok |
| `/stock/insider-sentiment` (MSPR) | ⚠️ empty `[]` |
| `/stock/eps-estimate` / `/revenue-estimate` | ⛔ paid-tier — skipped (forward blind spot) |
| `/stock/financials-reported` | ⛔ not pulled (typically paid) — proxied from metrics |

## Tool / source errors

MSPR empty (known RDDT data gap — see [[data-source-workarounds]]); forward
EPS/revenue consensus paid-tier (substituted phase-6 WebSearch PT trend). Look-ahead
guard applied: earnings filtered to `period <= 2026-05-22`.

## Verdict for downstream — QUALITY GATE

```
fundamental_signal:  BULLISH        # business is strong & accelerating
tier_adjustment:     VETO           # vs the BEARISH flow bias — 2 axes contradict
contradiction_count: 2              # {earnings_trend, growth/margins} contradict bearish;
                                    #  insider (CEO selling) does NOT contradict
key_risks: [ "forward ad-growth deceleration from Meta Forum — invisible in TTM beats",
             "CEO insider selling (confidence flag)",
             "rich absolute multiples (P/S 11, P/B 15) + beta 2.15 → big derating risk if growth slows" ]
```

- **Effect on phase-9:** VETO a **fresh aggressive directional short** → reduce any
  bearish directional expression to **watch-only / carry-only defined-risk** (small
  put debit spread permissible, naked/large short not). Do NOT let this phase add
  bullish conviction — it only *cuts the short*.
- **Why VETO, stated plainly:** you do not short a 70%-revenue-growth, 91%-gross-
  margin, serial-beating, net-cash business with a 0.095 PEG on a heavy-tape day —
  especially one already −50% off its high. The bearish flow is most consistent with
  **hedging / profit-taking on a beaten-down high-flyer**, not distribution by a
  smart-money short. The *only* path that vindicates the bears is the **forward**
  Meta-Forum competitive derating, which trailing fundamentals can't price — so any
  bearish trade must be **explicitly a competitive-disruption bet, small and
  defined-risk**, not a "the flow is bearish" momentum short.
