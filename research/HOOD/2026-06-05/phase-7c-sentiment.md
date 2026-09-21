# Phase 7c — Sentiment, Positioning & Short Interest

**Ticker:** HOOD
**As-of date:** 2026-06-05
**Generated:** 2026-06-07T13:35:00-04:00
**Upstream phases cited:** phase-0.5-context.md, phase-1-flow.md, phase-2-dark-pool.md,
phase-5-historical.md, phase-6-macro.md, phase-7b-fundamentals.md

## Summary

The crowd is **bullishly inclined while the tape sells** — and the selling is
uniform across cohorts. The 14-day news flow (211 items, look-ahead filtered)
is dominated by bullish catalysts: SpaceX-IPO access ("Robinhood Is Opening
the SpaceX IPO to Everyday Investors", JPMorgan IPO event), the PDT-rule
elimination, and the publicly-reported **"Director Malka Buys $15.1 Million in
Shares"** (Jun-4) — yet price fell ~9% over the window's last week (90.73 →
82.47): the tape is leading (ignoring) the news, which favors the bearish
flow's information content. Street consensus drifts only marginally
(strongBuy 9→8, buy 19→18, hold 4→5 into June) and stays firmly Buy (fz Recom
1.69, target $101.87 — no vendor divergence). Positioning is **not crowded in
either direction**: short interest is just **4.96% of float, 1.29
days-to-cover** (no squeeze fuel, no HTB flags), institutional ownership 61%,
P/C z-score −0.016 (NORMAL), IV-rank 49.6 (58.5th pctile). The §A lit split
shows small-lot, mid, AND block traders all net-selling calls and net-buying
puts ex-0DTE — **no retail-vs-institution divergence; everyone de-risked
together**. Gate: one contrary axis (bullish catalyst proximity against the
short) → **CAUTION** (one size step cut). 

## Key signals

- News tone 14d: **bullish catalysts vs falling price** — SpaceX IPO access
  narrative across ≥6 headlines, PDT-rule change framed as structural win;
  Jun-5 itself "HOOD registers a bigger fall than the market" (beta day)
  [SENT:company_news Finnhub]
- Malka's buying hit the wires **Jun-4** ("Buys $15.1 Million in Shares",
  Yahoo) — the dip-buy of phase-7b is *public information*, partially priced
  [SENT:company_news Finnhub]
- Revisions: strongBuy 8 / buy 18 / hold 5 / sell 1 (Jun-1) vs 9/19/4/1
  (Apr–May) — **mild negative drift, level still solidly Buy**; fz cross
  Recom 1.69 / target $101.87, no divergence `[SENT:recom fz]`
  [SENT:recommendation Finnhub]
- **Short interest 4.96% / days-to-cover 1.29 / float 761.21M / Inst Own
  61.01% / Insider Own 15.54%** `[SENT:short_float fz semi-monthly]` — clean
  borrow, zero squeeze topology; borrow fee: n/a (no HTB flags found)
  [SENT:borrow WebSearch]
- Cohort alignment (§A ex-0DTE): calls net-sold by small-lot −$5.57M, mid
  −$3.34M, block −$2.32M; puts net-bought +$1.37M / +$0.84M / +$0.82M —
  **uniform de-risking, no crowd-vs-smart-money divergence**
  `[SENT:cohort_split DUCKDB]`

## Detailed findings

### News flow (2026-05-22 → 2026-06-05, n=211 items ≤ as-of)

Theme mix: (a) SpaceX IPO access/eligibility — strongly bullish for account
growth, JPM hosting the IPO event, Fidelity comparison pieces; (b) PDT rule
eliminated — "customers walked away because of a 25-year-old rule, now it's
final" (Benzinga); (c) crypto-adjacent caution (Baird bearish COIN, Q2 revenue
miss risk — read-across to HOOD's crypto leg); (d) Piper Sandler fintech
conference presentation (Jun-4); (e) the Malka purchase disclosure (Jun-4).
Net tone: **bullish**, and the tape fell through it — price *leads* the news
narrative downward, the classic signature of positioning unwind rather than
news-driven repricing.

### Analyst-revision momentum [SENT:recommendation Finnhub]

| Period | strongBuy | buy | hold | sell |
|---|---|---|---|---|
| 2026-06-01 | 8 | 18 | 5 | 1 |
| 2026-05-01 | 9 | 19 | 5 | 1 |
| 2026-04-01 | 9 | 19 | 4 | 1 |
| 2026-03-01 | 8 | 19 | 4 | 1 |

Direction: one strongBuy and one buy lost, one hold gained over two months —
consistent with phase-7b's −8.4% FY26 estimate cut: a *drift*, not a downgrade
cycle. No Finnhub-vs-fz divergence (both bullish-level). 

### Retail vs institutional `[SENT:cohort_split DUCKDB]` (lit, ex 0–1DTE)

| Cohort (trade size) | Call ask−bid | Put ask−bid | Read |
|---|---|---|---|
| small_lot (≤10) | −$5.57M | +$1.37M | retail selling calls, buying puts |
| mid (11–99) | −$3.34M | +$0.84M | same |
| block (≥100) | −$2.32M | +$0.82M | same |

All three cohorts share the bearish signature — phase-2's balanced dark pool
plus this says the de-risking is broad-based, plausibly profit-taking /
covered-call writing after May's +29% run rather than informed institutional
distribution alone. No fade-the-crowd divergence exists to exploit.

### Short interest & borrow

`[SENT:short_float fz semi-monthly]` (exchange settlement, ~2-week lag):
short_float **4.96%**, days_to_cover **1.29**, float 761.21M, Inst Own 61.01%,
Insider Own 15.54%. Borrow: **n/a** — WebSearch surfaced no HTB or elevated
borrow-fee flag for HOOD (June 2026); with 5% SI / 1.3 DTC the name is
mechanically easy to short and structurally hard to squeeze
[SENT:borrow WebSearch:fintel.io].

### Positioning extremes (reused upstream)

P/C ratio z-score **−0.016** = NORMAL (phase-5, 20d baseline 0.402); IV rank
49.59 / universe pctile 58.5 (phase-0.5); skew COMPLACENT with calls > puts
(phase-4). No |z|>2 contrarian trigger anywhere on the board.

## Divergences

1. **Bullish news catalysts (SpaceX IPO, PDT rule) vs persistent bearish tape**
   — the market is selling through good news; tape leads.
2. **Street Buy-consensus (26/32, target +23.5%) vs options flow fading it**
   (5/5-session bearish sweep campaign, phase-1).
3. **Publicly-disclosed director buying (Jun-4, $15.1M reported) vs
   sweep-selling into it** — informed insider vs informed flow, unresolved
   until 8b.

## Source calls

| Source | Status |
|---|---|
| Finnhub `/company-news` (05-22→06-05, look-ahead filtered) | ok, 211 items |
| Finnhub `/stock/recommendation` | ok, 4 months |
| `fz quote` SI/float/ownership | ok |
| DuckDB §A cohort split (ex 0–1DTE) | ok |
| WebSearch borrow fee / HTB | ran; no specific rate found → n/a |
| P/C z, IV-rank | reused phase-5 / phase-0.5 |

## Source errors

(none; borrow-fee specific datapoint unavailable from free sources — recorded
as n/a, not inferred)

## Verdict for downstream phases — the positioning gate

```
sentiment_signal:  BEARISH          # tape-leads-news; uniform cohort de-risking
crowd_state:       BALANCED         # SI 4.96%, P/C z −0.02, IV-rank 50 — nothing crowded
short_interest:    4.96% [fz, semi-monthly] ; days_to_cover: 1.29 ; borrow: n/a [WebSearch]
tier_adjustment:   CAUTION          # one contrary axis: imminent bullish catalyst
                                    # proximity (SpaceX IPO access + PDT tailwind +
                                    # public Malka buy) against the bearish thesis
divergences:
  - "bullish news catalysts vs falling tape (tape leads)"
  - "street Buy consensus / +23.5% targets vs 5-session bearish sweep campaign"
  - "disclosed $15.1M director buy (Jun-4) vs sweep-selling into it"
key_risks:
  - "SpaceX IPO access window = sharp gap-up event risk against any short (date fluid, June)"
  - "uniform call-selling may be covered-call income after +29% May — caps upside without forcing downside"
  - "low SI means no cover-bid under the market, but also no squeeze: bear case must work on its own flow, not positioning"
```

Phase-9 effect: **cut one size step** (stacked on phase-7b's VETO of the naked
directional short — defined-risk-only carry, one step smaller). Downside-only
rule respected: nothing here raises conviction.
