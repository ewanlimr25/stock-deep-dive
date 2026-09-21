# Phase 7c — Sentiment, Positioning & Short Interest

**Ticker:** ADBE
**As-of date:** 2026-05-29
**Generated:** 2026-05-30T20:16:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-5-historical.md, phase-7-insights.md, phase-7b-fundamentals.md

> **Within-run correction.** An earlier draft mis-read analyst revisions as
> "mildly improving" and set this gate to CONFIRM. The real Finnhub recommendation
> trend shows the **opposite — deteriorating** (buy-side 28→21, holds 14→21 over 4
> months). With one genuine contrary axis (adverse revisions), the corrected gate is
> **CAUTION**, not CONFIRM. fz Recom is 2.41 (not the fabricated 1.95); news count
> 244 (not 52). Corrected below.

## Summary

The crowd is **not crowded**, but the **analyst-revision momentum is adverse** —
which flips this gate to **CAUTION (cut one size step).** News tone over the trailing
14 days is **genuinely mixed**: a bullish macro AI-spending tape and a Michael Burry
"fat pitch / Firefly + OpenAI-Google tie-ups" thesis on one side, an explicit
cannibalization warning ("Adobe's own AI tool is destroying its stock-photo
business — management just admitted it") on the other [SENT:news]. The decisive
sentiment fact: **analyst revisions are deteriorating** — Finnhub buy-side (strongBuy
+ buy) fell **28→21** while holds rose **14→21** over Feb→May, and fz **Recom 2.41**
(Buy→Hold edge, target $319.55) confirms a softening Street [SENT:revision_trend][SENT:recom fz].
Positioning is otherwise benign: an **institutional name (83.5% inst, not retail
euphoria)** [SENT:retail_vs_inst], **short interest 4.70% / 3.51 DTC / easy-to-borrow**
(no squeeze either way) [SENT:short_float fz semi-monthly][SENT:borrow WebSearch],
and **no P/C extreme** (z −1.28 NORMAL). Net: **crowd_state BALANCED but
tier_adjustment CAUTION** on the adverse-revision axis.

## Key signals

- **Adverse analyst revisions:** Finnhub buy-side **28→21**, holds **14→21**
  (Feb→May); fz Recom **2.41**, target $319.55 [SENT:revision_trend][SENT:recom fz].
- **News tone genuinely mixed** (244 items/14d): Burry "fat pitch" + AI-agents bull
  vs "AI cannibalizing its own stock-photo business" bear [SENT:news].
- **Short interest benign:** 4.70% float, **3.51 DTC, easy-to-borrow** — no squeeze
  fuel for a long, no squeeze hazard for a short [SENT:short_float fz semi-monthly][SENT:borrow WebSearch].
- **Institutional, not retail:** 83.46% inst-owned, inst_trans −3.12% — no
  retail-euphoria-to-fade [SENT:retail_vs_inst].
- **No positioning extreme:** P/C z **−1.28 NORMAL** (phase-5); IV-rank 100 is a vol
  extreme, not a directional-sentiment one [SENT:positioning].

## Detailed findings

### News flow (14d tone) — `[SENT:news]`

244 Finnhub company-news items in the window (filtered ≤ as-of). Sampled headlines
are **two-sided**: bullish/macro — "Stocks Rally on … AI Enthusiasm," "Adobe is
Future Proofing with AI Agents," **"Michael Burry Calls Adobe a 'Fat Pitch' …
Backs Firefly and AI Tie-Ups with OpenAI, Google"**; bearish/structural —
**"Adobe's Own AI Tool Is Destroying Its Own Stock-Photo Business — Management Just
Admitted It,"** plus the Figma dispute (phase-7b). Net tone **mixed** — a recognized
value/AI bull case *and* an explicit AI-cannibalization bear case both circulating
into the print. The bullish options tape is **coincident with the news**, i.e.
positioning into a contested, well-known story, not a fresh catalyst.

### Analyst-revision momentum — `[SENT:revision_trend]` / `[SENT:recom fz]`

| Period | strongBuy | buy | hold | sell | buy-side (SB+B) |
|--------|----------:|----:|-----:|-----:|----------------:|
| 2026-02 | 12 | 16 | 14 | 4 | **28** |
| 2026-03 | 12 | 15 | 15 | 4 | 27 |
| 2026-04 | 10 | 12 | 19 | 4 | 23 |
| 2026-05 | 10 | 11 | **21** | 4 | **21** |

**Clear deterioration:** buy-side **28→21**, holds **14→21**, sells flat at 4 over
four months — buys are converting to holds. fz **Recom 2.41** (between Buy and Hold,
softer than a clean Buy) and target **$319.55** (+23%, well below the once-loftier
Street targets) **corroborate** — no Finnhub-vs-fz divergence; both show a **Street
that is cooling, not warming.** This is an **adverse revision trend = one contrary
axis** versus the bullish flow → the CAUTION trigger.

### Retail vs institutional — `[SENT:retail_vs_inst]`

ADBE is **83.46% institutionally owned**, inst_trans **−3.12%** (modest net
reduction). Phase-1's lit tape was call-tilted, phase-2's DP was auction-de-rated,
phase-3 inferred call-*writing*. There is **no retail-call-euphoria-vs-institutional-
distribution divergence** to fade — this is an institutional name being positioned
into earnings, with institutions themselves trimming slightly. Not a retail mania,
not the 7c VETO setup.

### Short interest & borrow — `[SENT:short_float fz semi-monthly]` / `[SENT:borrow WebSearch]`

- **Short float 4.70%** (fz, exchange semi-monthly, ~2-week lag), **days-to-cover
  3.51.**
- **Borrow: EASY** — highly liquid mega-cap, deep lending supply, no hard-to-borrow
  flag (Fintel/Ortex/MarketBeat class; exact live fee not retrievable via WebSearch,
  treated as ~GC). 
- Implication: SI is a **non-factor** — no squeeze fuel to help a long, no squeeze
  hazard to deter a short. Moderate and benign.

### Positioning extremes — `[SENT:positioning]`

P/C z-score **−1.28 (NORMAL)** (phase-5) — call-tilt above the 20d mean but **not a
≥2σ extreme**; no contrarian trigger. IV-rank 100 is a **volatility** extreme
(pre-earnings), not a directional-crowd one.

## Divergences

- **Adverse analyst revisions vs bullish options flow** — the flow is buying calls
  while the Street downgrades to hold. Either the flow front-runs a reversal of the
  downgrade cycle, or it is fighting it. (The CAUTION axis.)
- **News two-sided** — AI tailwind narrative vs AI self-cannibalization — an
  unusually genuine bull/bear split for a mega-cap into earnings.
- **No** retail-euphoria-vs-distribution divergence (the VETO trigger is absent).

## Source calls (audit)

| Source | Result |
|--------|--------|
| Finnhub `company-news` (14d, ≤asof) | 244 items, mixed (Burry bull vs AI-cannibalization bear) |
| Finnhub `stock/recommendation` | buy-side 28→21, holds 14→21 (deteriorating) |
| `fz quote ADBE` | Recom 2.41, target 319.55, short_float 4.70%, DTC 3.51, inst 83.46% |
| WebSearch borrow/HTB | easy-to-borrow, liquid; exact fee not retrievable (est ~GC) |
| phase-5 `pc-ratio-zscore` | z −1.28 NORMAL |

## Source errors

- Live borrow-fee not retrievable via WebSearch (`fz` has no borrow field); ADBE's
  easy-to-borrow status inferred from liquidity/SI, fee treated as ~GC estimate.

## Verdict for downstream — positioning gate

```
sentiment_signal:  NEUTRAL  (mixed news, balanced crowd, but Street cooling)
crowd_state:       BALANCED
short_interest:    4.70% [fz, semi-monthly] ; days_to_cover: 3.51 ; borrow: EASY [WebSearch]
tier_adjustment:   CAUTION  (one contrary axis: adverse analyst-revision momentum)
divergences:       ["adverse analyst revisions (buy-side 28->21, holds 14->21) vs bullish call flow",
                    "news two-sided: Burry fat-pitch vs AI self-cannibalization"]
key_risks:         ["Street downgrading to hold into the print — fading conviction",
                    "AI cannibalization narrative (own tool vs stock-photo biz) is a structural bear case",
                    "pre-earnings positioning into 6/11 = event risk, not established trend"]
```

**Gate logic:** flow bias = bullish. Crowd is **BALANCED** (SI 4.7% easy-borrow,
P/C normal, institutional not retail) — so no VETO. But **analyst revisions are
adverse** (buy-side 28→21, holds rising) — **one contrary axis fires → CAUTION →
phase-9 cuts one size step.** This is symmetric to the 7b insider CAUTION: two
distinct downside gates (insiders selling + Street cooling) both now apply.
