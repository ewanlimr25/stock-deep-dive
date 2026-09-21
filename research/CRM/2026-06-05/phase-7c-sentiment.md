# Phase 7c — Sentiment, Positioning & Short Interest

**Ticker:** CRM
**As-of date:** 2026-06-05 (look-ahead guard: all news/revisions filtered ≤ 2026-06-05)
**Generated:** 2026-06-06T17:10:00-04:00
**Upstream:** phase-7b-fundamentals.md (VETO on naked shorts; "does 7.91% SI
make the downside crowded?"), phase-1-flow.md (bearish sweeps 5/5),
phase-2-dark-pool.md (weekly distribution), phase-5-historical.md (P/C z −0.11)

## Summary

The crowd is **already leaning the same way as the flow tilt — bearish — and
the squeeze ledger is non-trivial**. The 14-day news tape (245 items) is
dominated by sector-panic framing ("Nasdaq worst day in more than a year",
"SaaS-pocalypse", "Bridgewater Just Sold Salesforce") with name-specific
positives underneath (RBC: core business holding steady, Agentforce adoption
building; 6/05 definitive agreement to acquire Contentful). Analyst revisions
are drifting down at the margin (strongBuy 14→13→12 over Mar→Jun; first sell
rating appeared in June) while the *level* stays constructive (Recom 1.64,
target 247.46 = +33%). Short interest is **7.91% of float / 4.46
days-to-cover** — 2–3× the quality-peer norm (ADBE 4.70%, ADSK 2.82%) with
EASY borrow; against it stands a $25B ASR executing daily. Retail shows **no
euphoria** (small lots are net premium *sellers*), and institutional lots
actually tilt bullish (net call buying + net put selling). Verdict vs the
bearish flow bias: **CAUTION** — the short side is moderately crowded and the
ASR is mechanical squeeze fuel; cut one size step on bearish expression.

## Key signals

- **SI 7.91% float / DTC 4.46** `[SENT:short_float fz semi-monthly]` (exchange
  settlement, ~2-week lag; float 792.65M) — highest in the quality-peer cohort
  (7b table); borrow **EASY** (no HTB flag on any tracker; mega-cap GC)
  `[SENT:borrow WebSearch:fintel.io]`. Squeeze hazard for fresh shorts when
  paired with the $25B ASR (7b) and a 100% beat-rate.
- **News tone (14d, n=245): NET BEARISH on sector framing, mixed on the name.**
  6/05 sample: "Nasdaq Suffers Worst Day in More Than a Year", "Tech Stocks
  Fall. Why Broadcom… Triggered Sell-Off", "Bridgewater Just Sold Salesforce",
  vs "Salesforce's Core Business Holding Steady as Agentforce Adoption Builds,
  RBC Says" and "Salesforce Signs Definitive Agreement to Acquire Contentful"
  (6/05, name-specific M&A). News *followed* price down (lagging, not
  leading). `[SENT:company_news finnhub]`
- **Revision momentum mildly negative:** strongBuy 14 (Mar/Apr) → 13 (May) →
  **12 (Jun)**; buy 30→31; sell 0→1; strongSell 1 steady (57 analysts). Level
  vs trend split: still a consensus buy, but the marginal analyst is moving
  down — agrees with the PT trims (7b). No Finnhub-vs-fz divergence (fz Recom
  1.64 / target 247.46 ≈ same read). `[SENT:recommendation finnhub]`
  `[SENT:recom fz]`
- **Retail is NOT euphoric — it's selling premium:** small-lot (1–5 ct,
  ex-0/1DTE) calls $3.65M ask vs $4.57M bid (net −$0.92M sellers), puts
  likewise net sold; institutional lots (>50 ct): calls **+$1.21M net bought**,
  puts **−$3.15M net SOLD** — the bullish-structure tilt (the Jan-27 RR
  signature). The lit crowd is income-harvesting, not chasing.
  `[SENT:retail_split DUCKDB]`
- **No positioning extreme to fade:** P/C z-score −0.113 (NORMAL, phase-5),
  IV rank 60.0 (phase-0.5) — mid-range on both. `[SENT:pc_zscore]`
  `[SENT:iv_rank]`

## Detailed findings

### News flow (14d tone; lead/lag)

Window 2026-05-22 → 2026-06-05, 245 items (heavy — earnings + sector shock).
Arc: pre-earnings preview chatter → 5/27-28 beat + $25B ASR coverage
(positive) → 6/01 record close + annual meeting (positive) → 6/03-05 AVGO
shock / SaaS-pocalypse / "worst day" coverage (negative, high volume),
including institutional-exit headlines ("Bridgewater Just Sold Salesforce" —
13F-derived, backward-looking). Name-specific 6/05: Contentful acquisition
(definitive agreement — strategic add, mildly cash-consuming), RBC
constructive note. **Tone: sector-bearish > name-bearish; news lagged price
on both legs.** `[SENT:company_news finnhub]`

### Analyst-revision momentum

| Period | strongBuy | buy | hold | sell | strongSell |
|---|---|---|---|---|---|
| 2026-06-01 | **12** | 31 | 13 | **1** | 1 |
| 2026-05-01 | 13 | 31 | 13 | 0 | 1 |
| 2026-04-01 | 14 | 30 | 13 | 0 | 1 |
| 2026-03-01 | 14 | 30 | 13 | 0 | 1 |

Direction: slow bleed out of strongBuy, first sell initiation post-earnings.
Cross-source: fz Recom 1.64 / target 247.46 — consistent level, no vendor
divergence (D6). `[SENT:recommendation finnhub]` `[SENT:recom fz]`

### Retail vs institutional

Lit small-lot vs block split (ex-0/1DTE, ask/bid only) `[SENT:retail_split DUCKDB]`:

| Bucket | Call ask | Call bid | Put ask | Put bid | Net read |
|---|---|---|---|---|---|
| retail (1–5) | $3.65M | $4.57M | $2.67M | $3.09M | net seller both types |
| mid (6–50) | $3.69M | $6.06M | $3.75M | $3.80M | call seller, put flat |
| inst (>50) | $3.56M | $2.35M | $1.01M | **$4.16M** | **call buyer + put seller (bullish tilt)** |

Cross-ref phase-2: DP blocks balanced today (buy_ratio 0.489–0.544), weekly
distribution at the highs. **Institutions: bullish in options, distributive in
stock during the spike — consistent with "sold the spike, re-risking via
defined structures lower."** Retail absent as a fade target.

### Short interest & borrow

7.91% of 792.65M float ≈ **62.7M shares short**; days-to-cover 4.46 (vs 14.06M
avg vol) `[SENT:short_float fz semi-monthly]` (settlement-lagged ~2wks — so
this is pre-/at-earnings positioning; the 5/29–6/01 +19% spike likely squeezed
some, the 4-day fade likely re-loaded some — next settlement will resolve).
Borrow: EASY (no HTB designation found; mega-cap general collateral)
`[SENT:borrow WebSearch:fintel.io]`. Phase-0 drift: Short Ratio 4.71 → 4.46.
Against the short book: $25B ASR executing (7b) + dividend ex-date 6/11.

### Positioning extremes

None. P/C 0.57 vs 20d mean 0.596, z −0.113 (phase-5); IV rank 60.0; skew
COMPLACENT (phase-4 — if anything, the *absence* of put-skew panic says the
crowd hasn't paid up for crash protection, so the fade is not yet a consensus
panic). `[SENT:pc_zscore]` `[SENT:iv_rank]`

## Divergences

1. **Institutional option lots bullish (call-buy/put-sell, +$4.4M tilt) vs the
   5-session bearish sweep campaign** — the aggressive tape and the
   block-structure tape disagree.
2. **Sell-side level (+33% target, Recom 1.64) vs price action and marginal
   revisions** — level constructive, momentum negative.
3. **Elevated SI (7.91%) + EASY borrow + $25B ASR** — the short crowd is
   populated while a mechanical buyer operates daily underneath.

## Source calls

| Source | Status |
|---|---|
| Finnhub `company-news` (5/22→6/05) | ok n=245, look-ahead-filtered |
| Finnhub `recommendation` | ok (4 periods ≤ as-of) |
| `fz quote` SI/DTC/float + Recom/target | ok |
| WebSearch borrow fee / HTB | ok — no specific fee found, no HTB flag (EASY inferred) |
| DuckDB §A small-lot split | ok |
| Phase-5 P/C z / phase-0.5 IV rank | reused |

## Source errors

None. (Borrow-fee numeric unavailable free — recorded as EASY/no-HTB rather
than a number; SI is semi-monthly-lagged, flagged inline.)

## Verdict for downstream

```
sentiment_signal:  BEARISH          # news tone + marginal revisions point down
crowd_state:       CROWDED_SHORT    # moderate — 7.91% float (2-3x peer norm),
                                    # 5/5 bearish sweeps, exit headlines; not
                                    # extreme (no HTB, no P/C extreme)
short_interest:    7.91% [fz, semi-monthly] ; days_to_cover: 4.46 ; borrow: EASY [WebSearch]
tier_adjustment:   CAUTION          # vs the bearish flow bias: crowd already
                                    # same-way + ASR/beat-rate squeeze fuel →
                                    # cut one size step on bearish expression
divergences:
  - "Institutional option lots bullish (call-buy + put-sell) vs 5d bearish sweep tape"
  - "Sell-side +33% target / Recom 1.64 vs negative revision momentum and tape"
  - "7.91% SI + EASY borrow + $25B ASR = mechanical squeeze ledger under any short"
key_risks:
  - "Short-side crowding: fresh shorts join a 62.7M-share book against a daily ASR bid"
  - "SI print is ~2wks stale; post-spike short reload unverifiable until next settlement"
  - "Complacent skew = cheap upside tails; a squeeze would find no call-supply brake until 195-200"
```

**Phase-9 effect:** bearish expression takes a one-step size cut (stacking
with 7b's VETO on *naked* shorts → only small, defined-risk bearish structures
survive the two gates). No effect on a long (the gate never adds conviction).
