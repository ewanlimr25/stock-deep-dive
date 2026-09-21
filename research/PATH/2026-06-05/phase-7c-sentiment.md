# Phase 7c — Sentiment, Positioning & Short Interest

**Ticker:** PATH
**As-of date:** 2026-06-05
**Generated:** 2026-06-06T12:05:00-04:00
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md, phase-5-historical.md, phase-7-insights.md, phase-7b-fundamentals.md

## Summary

The crowd is **short, not long**: 31.15% of float short (fz; Fintel-family
sources show 115.09M sh / 31.49%, *rising* from 108.52M), days-to-cover 3.72,
yet borrow is **easy (0.29% fee, 10M shares available)** — shorts can press
cheaply and the failed 06-01 squeeze shows they are. Sentiment axes split:
news tone is fundamentally upbeat post-beat, but **revision momentum is
negative** (RBC $14→$12 on 06-02, BMO →$13 on 06-01, an SA downgrade, buy
count 8→7 / hold 17→18 in June) — the street is converging targets *toward*
spot rather than chasing the beat. Retail is *not* euphoric (small lots net
**sold** calls −$93.8k while blocks net bought +$334.1k). Against a
weak-bullish flow bias the gate scores **one contrary axis (adverse revision
trend) → CAUTION** — cut one size step.

## Key signals

- Short interest: **31.15% of float**, days-to-cover 3.72, float 412.34M,
  inst own 60.84%, insider own 20.77% [SENT:short_float fz semi-monthly];
  cross-source: 115.09M sh short = 31.49%, up from 108.52M prior period
  [SENT:si WebSearch:fintel.io]
- Borrow: **EASY** — fee 0.29% APR, ~10M shares available; not HTB
  [SENT:borrow WebSearch:companiesmarketcap.com]
- Revisions: Jun strongBuy 2 / buy 7 / hold 18 / sell 1 (from 2/8/17/1 in
  Mar–May) — drift toward hold; **two post-beat PT cuts** (RBC $12, BMO $13)
  [SENT:recommendation][SENT:news Benzinga 2026-06-01]
- Retail-vs-inst (lit tape, strike>8, ex-arb): block calls ask−bid
  **+$334.1k** vs small-lot **−$93.8k** — institutions buying, retail
  fading [SENT:retail_split DUCKDB]
- Positioning extremes: none — P/C z **−0.072 `NORMAL`** (phase-5), IV rank
  40.03 mid-range (phase-0.5) [SENT:pc_zscore]

## Detailed findings

### News flow (14d, 54 items ≤ as-of; look-ahead filtered)

Post-earnings coverage dominates: "UiPath (PATH) Is Up 19.9% After First
GAAP Profit And Higher 2027 Guidance" (06-02), "Is UiPath Stock a Buy as
Revenue Accelerates?" (06-03), "UiPath Just Delivered 2 Bullish Signals and
1 Warning Sign" (06-04) — *content* constructive, *framing* increasingly
interrogative as price faded. Negative-action items: SeekingAlpha "RPA and
Agentic AI… (Downgrade)" (06-01), BMO Market-Perform PT→$13 (06-01)
[Benzinga], RBC →$12 (06-02, phase-7b). Product/win flow positive (One NZ
benchmark 06-04, Dubai DESC cert 06-03, William Blair presentation 06-02).
**News lagged price on the pop (06-01) and led/echoed it on the fade** — the
PT cuts landed exactly as the squeeze unwound 06-02→06-05.

### Analyst-revision momentum

| period | strongBuy | buy | hold | sell |
|---|---|---|---|---|
| 2026-06-01 | 2 | **7** | **18** | 1 |
| 2026-05-01 | 2 | 8 | 17 | 1 |
| 2026-04-01 | 2 | 8 | 17 | 1 |
| 2026-03-01 | 2 | 7 | 18 | 1 |

Direction: mild deterioration into June [SENT:recommendation]. Cross-source:
fz Recom 2.65 / target $13.47 [SENT:recom fz] vs Finnhub hold-tilt and
WebSearch consensus ~$13.31–13.67 — **no vendor divergence**; everyone says
Hold with ~+20% targets they keep trimming.

### Retail vs institutional (lit small-lot vs blocks; `strike > 8` excludes
the deep-ITM arb family from phase-1)

| bucket | calls ask−bid prem | puts ask−bid prem |
|---|---:|---:|
| block (≥50) | **+$334.1k** | +$47.7k |
| mid (6–49) | +$96.4k | +$94.4k |
| small lot (≤5) | **−$93.8k** | +$2.5k |

[SENT:retail_split DUCKDB] Institutions are the net call buyers (the Sep
cluster); retail small lots are net call *sellers* — **no retail euphoria**,
the distribution-into-strength signature is absent on the lit tape. Blocks
also paid up modestly for puts (hedged buying, consistent with phase-1's
Aug $10P).

### Short interest & borrow

- fz (semi-monthly settlement, ~2wk lag): **Short Float 31.15%**, Short
  Ratio (days-to-cover) **3.72**, float 412.34M [SENT:short_float fz semi-monthly].
- WebSearch cross-check: 115.09M shares short, **31.49%** of float, rising
  from 108.52M [SENT:si WebSearch:fintel.io/marketbeat.com].
- Borrow: **0.29% APR, ~10M shares available — EASY**, not HTB
  [SENT:borrow WebSearch:companiesmarketcap.com].
- Implication for upstream reads: phase-1 hypothesized the deep-ITM 0DTE
  call structure as an HTB workaround — with borrow this cheap that
  hypothesis weakens; plain exercise/spread arb is the better label
  (correction below). For the thesis: 31% SI is squeeze *fuel* on any
  reclaim of the $12 wall, but easy borrow means **no forced covering** —
  shorts pressed the failed squeeze and won the week.

### Positioning extremes

P/C z-score −0.072 (`NORMAL`, 20d) [phase-5]; IV rank 40.03 / IV %ile 12.8
(1y) [phase-0.5/5] — no contrarian extreme on either axis.

## Divergences

1. **Street vs business:** two post-beat PT *cuts* and a ratings drift toward
   Hold against accelerating revenue + raised guidance (7b CONFIRM).
2. **Crowd vs smart money:** 31.5% of float short while blocks net-buy calls
   and DP prints a 0.64–0.65 buy ratio — the short crowd is leaning against
   the institutional tilt.
3. **Retail vs institutions:** small lots net-sell the calls blocks are
   buying — unusual (normally retail chases post-earnings pops); removes the
   classic euphoria-fade fuel from the bear case.

## Source calls

| Source | Status | Extract |
|---|---|---|
| finnhub `company-news` (05-22→06-05) | ok, 54 items | tone table above |
| finnhub `stock/recommendation` | ok | 4-month trend table |
| `fz quote` SI/ownership | ok | 31.15% / 3.72 / 412.34M |
| DuckDB §A small-lot split | ok | block +$334.1k vs small −$93.8k |
| WebSearch borrow/SI | ok | 0.29% fee, 115.09M sh, 31.49% |
| Positioning extremes | reused phase-5/0.5 | z −0.072; IVR 40 |

## Source errors

None — all sources returned. (No HTB/borrow API exists in the stack; borrow
figure is WebSearch-sourced and dated ~June 2026, treat as approximate.)

## DATA NOTE / CORRECTION

- **Phase-1 hypothesis revision:** the deep-ITM 0DTE/weekly call pairs were
  flagged "HTB/borrow-related structure" — borrow is in fact EASY (0.29%),
  so the better classification is exercise/dividend-style spread arb or
  buy-write mechanics. Either way still **non-directional**; phase-1's
  directional read (which already excluded these prints) is unaffected.

## Verdict for downstream phases

```
sentiment_signal:  NEUTRAL   # upbeat content vs negative revision actions
crowd_state:       CROWDED_SHORT   # 31.15–31.49% of float, rising
short_interest:    31.15% [fz, semi-monthly] ; days_to_cover: 3.72 ; borrow: EASY (0.29%) [WebSearch]
tier_adjustment:   CAUTION   # one contrary axis vs the weak-bullish flow bias:
                             # adverse analyst-revision momentum (post-beat PT cuts).
                             # Crowd itself is short (not crowded-long), so no VETO.
divergences:
  - "Street cuts targets into a raised guide (RBC $12, BMO $13 post-beat)"
  - "31.5% short float vs institutional block call buying + DP buy tilt"
  - "Retail small lots net-sell calls while blocks buy — no euphoria to fade"
key_risks:
  - "Easy borrow (0.29%) = shorts can press costlessly; failed 06-01 squeeze shows they're winning"
  - "Revision momentum negative — targets converging toward spot"
  - "Squeeze fuel (31% SI) is a two-sided hazard: violent up-moves on reclaim of $12, but no carry while waiting"
```

Downside-only note: the CROWDED_SHORT + block-buying combination *supports*
a long but per the gate rule it adds nothing — it is recorded as a tailwind
for phase-9 to weigh and a hazard flag for any short construction.
