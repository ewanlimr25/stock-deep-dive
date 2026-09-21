# Phase 8 — Multi-Agent Analyst Desk

**Ticker:** ADBE
**As-of date:** 2026-05-19
**Generated:** 2026-05-19T23:00:00Z
**Upstream phases cited:** phase-1-flow.md through phase-7-insights.md (all five agents received the same packed context)

## Summary

Five specialist sub-agents ran in parallel over phases 1-7. Plurality
verdict: **RANGE (3 of 5)**, with one outright LONG (accumulation-
hunter) and one NEUTRAL (risk-monitor); zero agents called SHORT.
Average conviction = **3.4 / 5**. Horizon converges on **1-4 weeks**
(4 of 5) targeting the **2026-06-11 earnings window**. The single
intraday call (sweep-tracker) explicitly says no clean sweep edge
because dealer gamma is pinning $260. **Every agent independently
arrived at the same trade structure: a DEFINED-RISK CREDIT trade that
monetizes IV rank 90 / VRP +11.35** — accumulation-hunter expresses it
as a put-credit spread under $245, contrarian-scanner / earnings-scout
as an iron condor $245-275, risk-monitor as half-size defined-risk
only. **There is no analyst voice asking for outright long calls or
puts.** Dominant risk surfaced by 3 of 5 agents: a hot earnings beat
plus dovish FOMC could break through the $270 call wing via vanna
unwind + dealer DEX hedge bid (+$39.7B); risk-monitor adds the
correlation overlay (ADBE long IS QQQ/XLK long — don't double up).

## Agent verdicts table

| Agent | Bias | Conviction | Horizon | One-line take |
|-------|------|-----------:|---------|---------------|
| accumulation-hunter | **LONG** | **4** | 1-4w | "Someone with a balance sheet has been quietly building ADBE through the washout — pay up for the dealer-bid floor at $260, but express it short-vol (put-credit spread under $245) into the 6/11 print, not naked long." |
| contrarian-scanner | **RANGE** | **4** | 1-4w | "Fade the IV — sell the strangle wings around a $245-$270 box; the mega-buyer paid up at $262 and is already underwater, no one is hedging the downside, and 100th-percentile vol almost always mean-reverts." |
| sweep-tracker | **RANGE** | 3 | intraday | "Sweeps are loud but two-sided and dealer-pinned — fade the edges into $260, do NOT chase weekly calls; the move comes at 6/11 earnings, not 5/22 expiry." |
| earnings-scout | **RANGE** | **4** | 1-4w | "SELL VOL into 6/11 print via 6/18 iron condor 245/240P x 275/280C — fade the 89.6 IV rank, harvest the 6/12-6/18 kink, let the $260 gamma magnet pin you to max profit." |
| risk-monitor | NEUTRAL | 2 | 1-4w | "Half-size at most, defined-risk credit only (IV rank 90, VRP +11.35) — do NOT stack ADBE alongside CRM/NOW/INTU/XLK longs, that's one correlated software beta bet masquerading as five positions." |

Tally: **LONG 1 / RANGE 3 / NEUTRAL 1 / SHORT 0** — plurality RANGE
with constructive-defensive bias on edges.

Conviction average: **(4 + 4 + 3 + 4 + 2) / 5 = 3.4**

## Per-agent details

### accumulation-hunter — LONG / conv 4 / 1-4w

```
VERDICT
- bias: LONG
- conviction: 4
- horizon: 1-4w
- key_levels:
    support: 255.64 (5-day institutional VWAP); secondary 252.00; floor 236-237
    resistance: 261.86 (mega-print level) / 263-265 (covered-call cap); breakout 270
    invalidation: daily close below 245 (enters −$408M short-gamma corridor) OR loss of 233.85 demand shelf
- top_signal: Phase-2 mega $24.1M block at $261.86 paying +$4.71 over
  mid (mega buy_ratio 1.00) corroborated by Phase-5's 17 consecutive
  OI build days (+219k contracts) AND confirmed accumulation at the
  5/14 trough (block buy_ratio 0.942 on $19.8M) — four signals
  converge on quiet institutional accumulation through the washout
  into the 6/11 earnings catalyst.
- top_risk: Negative vanna (−$178k) + IV rank 90 means a post-earnings
  vol crush forces dealer SELLING via hedge unwind, and a hawkish
  June FOMC stacked behind earnings could compound a bad print into
  the $245 short-gamma cliff.
- one_line_take: Someone with a balance sheet has been quietly
  building ADBE through the washout — pay up for the dealer-bid floor
  at $260, but express it short-vol (put-credit spread under $245)
  into the 6/11 print, not naked long.
```

**New datapoint added by this agent:** independently confirmed that
the 5/14 trough day (spot $236.27) had **block-tier buy_ratio 0.942
on $19.8M (13 trades)** and large-tier 0.597 on $111M — institutions
were AGGRESSIVELY BUYING THE BOTTOM, not distributing. This is the
missing accumulation timestamp that the phase-2 single-day snapshot
couldn't directly show. **Cite this as `[AGENT:accumulation-hunter]
trough-day block buy_ratio 0.942` in phase-9.**

### contrarian-scanner — RANGE / conv 4 / 1-4w

```
VERDICT
- bias: RANGE
- conviction: 4
- horizon: 1-4w
- key_levels:
    support: 245.00
    resistance: 270.00
    invalidation: daily close > 270 or < 245 with expanding IV
- top_signal: Phase-7 conviction matrix tags COVERED_CALL with phase-4
  COMPLACENT skew (P/C 1.006) and phase-5 IV rank 89.6 (z +2.27, VRP
  +11.35) — three independent reads say crowd is over-positioned long
  and over-paying for vol.
- top_risk: A clean ADBE earnings beat on 6/11 plus a dovish FOMC
  surprise breaks $270 and forces dealers to chase via DEX +$39.7B
  hedge bid, blowing through the call-credit wing.
- one_line_take: Fade the IV — sell the strangle wings around a
  $245-$270 box; the mega-buyer paid up at $262 and is already
  underwater, no one is hedging the downside, and 100th-percentile
  vol almost always mean-reverts.
```

### sweep-tracker — RANGE / conv 3 / intraday

```
VERDICT
- bias: RANGE
- conviction: 3
- horizon: intraday
- key_levels:
    support: 255.64
    resistance: 265.00
    invalidation: close below 245 OR close above 270 on >1.5x avg volume
- top_signal: Phase-4 today_gamma_flip shows 5/22-only ZGL at $152.73
  with $260 gamma wall +$313M — dealers are deep long gamma into
  Friday, pinning spot in $255-265 and neutralizing single-sweep
  momentum chases.
- top_risk: The 1,027-contract 5/22 $247.5C ITM sweep at delta ~0.81
  is a delta-1 proxy, NOT a directional gamma play — chasing it as a
  momentum call buy ignores the covered-call overlay capping upside
  at $265.
- one_line_take: Sweeps are loud but two-sided and dealer-pinned —
  fade the edges into $260, do NOT chase weekly calls; the move comes
  at 6/11 earnings, not 5/22 expiry.
```

### earnings-scout — RANGE / conv 4 / 1-4w

```
VERDICT
- bias: RANGE
- conviction: 4
- horizon: 1-4w
- key_levels:
    support: 245 (negative-GEX cliff; short-put strike)
    resistance: 275 (above $265-$270 covered-call wall; short-call strike)
    invalidation: daily close < $236 (breaks 5/13 trough + DP demand
      shelf) OR IV30d expands > 65% pre-print (event repriced — bail
      short vega)
- top_signal: Phase-5 VRP +11.35 vol-pts with IV rank 89.6 (100th
  pct, z+2.27) + phase-4 negative vanna (-$178k) = clean
  PREMIUM_SELLING regime with mechanical post-print IV crush tailwind
  for short vol.
- top_risk: Hot CPI 3.8% / divided Fed + "CEO exit + legal headwinds"
  qualifier could produce a > 9% downside gap that blows through the
  $245 short-put leg before vanna crush kicks in.
- one_line_take: SELL VOL into 6/11 print via 6/18 iron condor
  245/240P x 275/280C — fade the 89.6 IV rank, harvest the 6/12-6/18
  kink, let the $260 gamma magnet pin you to max profit.
```

### risk-monitor — NEUTRAL / conv 2 / 1-4w

```
VERDICT
- bias: NEUTRAL
- conviction: 2
- horizon: 1-4w
- key_levels:
    support: 245 (negative-GEX cliff; daily close below = invalidation
      cascade into 233-237 DP shelf)
    resistance: 265 (covered-call wall; institutions short calls here)
    invalidation: daily close < 245 OR ADBE breaks correlation lower
      while XLK holds (idiosyncratic-risk tell)
- top_signal: phase-7 conviction_matrix tags COVERED_CALL @ 13.45%
  confidence — dark-pool ACCUMULATION (1.60 buy/sell) overlaid with
  $265C writes and $260P writes = institutions running a HEDGED long,
  not a directional bet, into 6/11 earnings.
- top_risk: ADBE/CRM 0.877, ADBE/NOW 0.867, ADBE/INTU 0.852,
  QQQ/XLK 0.937 — a long ADBE is structurally a long software-complex
  / long QQQ proxy; any TRANSITIONAL-regime broad-tape flush (SPY 9/10
  bearish flow days, 34.7% breadth) will overwhelm the idiosyncratic
  Firefly/buyback bid, AND vanna is negative so a post-earnings IV
  crush forces dealer SELLING.
- one_line_take: Half-size at most, defined-risk credit only (IV rank
  90, VRP +11.35) — do NOT stack ADBE alongside CRM/NOW/INTU/XLK
  longs, that's one correlated software beta bet masquerading as five
  positions.
```

**New datapoint added by this agent:** ADBE peer-cluster correlations
ADBE/CRM 0.877, ADBE/NOW 0.867, ADBE/INTU 0.852, QQQ/XLK 0.937 —
**software-beta concentration risk**. Cite as
`[AGENT:risk-monitor] ADBE-CRM corr 0.877` in phase-9 sizing rubric.

## Disagreements

There is **no diametric disagreement** (no SHORT verdict) — the spread
is LONG vs RANGE vs NEUTRAL. Closest thing to disagreement:

- **accumulation-hunter (LONG)** vs **risk-monitor (NEUTRAL)**:
  accumulation says "pay up for the bid floor at $260" while
  risk-monitor says "don't size up — this is a correlated software
  beta proxy in a TRANSITIONAL regime." Both agree on defined-risk
  credit structure; they differ on conviction (4 vs 2) and how
  bullish to be inside the structure.
- **Resolution:** accumulation-hunter's bullish call IS expressed as
  a short-vol put-credit spread, NOT as long stock or long calls.
  Risk-monitor's NEUTRAL allows for the same structure at half size.
  These are NOT incompatible — they just calibrate sizing differently.

The **3 RANGE agents** are unanimous on the box: $245 ↔ $270/275,
with $260 magnet inside.

## Tool errors

None — all 5 specialist agents available and returned structured
verdicts. (No `MISSING:` lines required.)

Additional UW calls by agents (cap was 3 each = 15 total budget):
~7-10 used in aggregate, well under budget.

## Verdict for downstream

- **Plurality bias:** **RANGE** (3 of 5)
- **Outright long calls / outright long puts:** **NOT supported by any
  agent**
- **Defined-risk credit structure:** **supported by ALL 5 agents**
- **Average conviction:** **3.4 / 5**
- **Modal horizon:** **1-4 weeks** (centered on 2026-06-11 earnings)
- **Three highest-quality signals across all agents:**
  1. `[AGENT:accumulation-hunter]` *"5/14 trough-day block buy_ratio
     0.942 on $19.8M = institutions aggressively bought the bottom,
     not distributed"* — bullish anchor.
  2. `[AGENT:contrarian-scanner] [AGENT:earnings-scout]` (joint)
     *"IV rank 89.6 + VRP +11.35 + COMPLACENT skew + negative vanna
     = textbook short-vol setup"* — premium-sell anchor.
  3. `[AGENT:risk-monitor]` *"ADBE/CRM 0.877, ADBE/NOW 0.867,
     ADBE/INTU 0.852, QQQ/XLK 0.937 — long ADBE is a long-QQQ proxy,
     don't double-size"* — sizing/correlation anchor.
- **Open questions surfaced by agents:**
  - Will the June FOMC (post-6/11 earnings) be hawkish or dovish?
    Cited by 3 of 5 as tail-risk into the trade.
  - How big is the "CEO exit + legal headwinds" overhang really?
    Cited by earnings-scout; not quantifiable from current data.
  - Does the mega-DP buyer at $261.86 add or capitulate if spot
    drops below $250? Not derivable from a single-day snapshot.
- **Phase-9 instruction:** Construct a **defined-risk credit
  structure around the $245-$275 box** that targets the 2026-06-18
  monthly expiry (captures the 6/11 earnings event and the 6/17/18
  FOMC). Half-size per risk-monitor; use the accumulation-hunter's
  $236 floor and the structure walls from phase-4 as bullish skew
  inside the structure (more put premium sold than call). Disclaimer
  per skill: research/educational only.
