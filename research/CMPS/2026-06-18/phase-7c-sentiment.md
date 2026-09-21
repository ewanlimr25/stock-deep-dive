# Phase 7c — Sentiment, Positioning & Short Interest

**Ticker:** CMPS
**As-of date:** 2026-06-18
**Generated:** 2026-06-20
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-5-historical.md, phase-7-insights.md, phase-7b-fundamentals.md

## Summary

The crowd's positioning **contradicts the bearish flow** and flags the bear as the
*late, crowded* options trade — a **CAUTION**, not a clean short. Analyst-revision
momentum is **improving and uniformly bullish**: strongBuy count rose 5→7 over four
months with **zero sell ratings** across 22 analysts (Finnhub), matching fz Recom
**1.12 (strong-buy)** / target $21.72 — no vendor divergence. Short interest is
**moderate and unsqueezable** (5.69% of float, **1.80 days-to-cover**, 66% institutional
ownership, easy borrow) — so a fresh short has no squeeze tailwind, but the share base
isn't crowded short either. The one extreme is in *options*: the P/C z-score is **+3.83
(BEARISH_EXTREME**, phase-5) — but that is the single LEAP-put print, and |z|>2 is a
classic **contrarian fade trigger**, meaning the bearish positioning is already
stretched, not early. News was quiet (0 Finnhub items in the 14d window). Net: the
positioning gate trims the bear by one step.

## Key signals

- Analyst revisions **improving**: strongBuy 5→5→5→**7**, **zero sells**, 22 analysts —
  contradicts bear [SENT:recommendation]
- fz Recom **1.12 (strong-buy)**, target **$21.72 (+73%)** — no Finnhub-vs-fz divergence
  [SENT:recom fz]
- Short interest **5.69%**, **days-to-cover 1.80**, borrow **EASY** → no squeeze fuel
  for a short, share base not crowded [SENT:short_float fz semi-monthly]
- **P/C z-score +3.83 (BEARISH_EXTREME)** → options positioning stretched bearish =
  contrarian fade trigger [SENT:positioning]
- Institutional ownership **66.18%**, insider 4.58%, **no retail call euphoria** (the
  bear was an institutional LEAP put, phase-1) [SENT:retail_vs_inst]
- News quiet: **0 Finnhub items** 2026-06-04→06-18 → no catalyst behind the put visible
  [SENT:news]

## Detailed findings

### News flow (14d tone)

- Finnhub `company-news` returned **0 items** for 2026-06-04→06-18. The known
  catalysts (Phase-3 readouts) were Feb 2026; the next (COMP006 durability) is H2 2026
  (phase-6). Mid-June is a **news vacuum** → the bearish put was placed without a
  visible fresh headline → no news *lead* explains it (blind spot, not bullish/bearish).

### Analyst-revision momentum (direction, not level)

| Period | StrongBuy | Buy | Hold | Sell | StrongSell |
|--------|----------:|----:|-----:|-----:|-----------:|
| 2026-06-01 | **7** | 13 | 2 | 0 | 0 |
| 2026-05-01 | 5 | 13 | 2 | 0 | 0 |
| 2026-04-01 | 5 | 11 | 2 | 0 | 0 |
| 2026-03-01 | 5 | 10 | 2 | 0 | 0 |

**Improving** — strongBuy +2 and buy +3 over the window, **zero sell/strong-sell
throughout**. fz Recom **1.12** (strong-buy) + target **$21.72** corroborates; **no
Finnhub-vs-fz divergence**. This is a bullish revision cycle → **contradicts** a bear.
[SENT:recom fz]

### Retail vs institutional

- The bearish signal was an **institutional** LEAP put (phase-1: ~$647K ask-side,
  single player), not small-lot retail. Dark pool was balanced (phase-2). Institutions
  own **66.18%**; **no retail call-buying euphoria** present. So this is not a
  fade-the-retail-crowd setup — if anything one institution is hedging/betting against
  a heavily-institutionally-owned, analyst-loved name.

### Short interest & borrow

- `fz`: short_float **5.69%**, Short Ratio (days-to-cover) **1.80**, float 128.74M,
  inst_own 66.18% [SENT:short_float fz semi-monthly, ~2-week lag].
- Borrow: **EASY** (inferred from 5.69% SI + 1.80 dtc + 66% institutional liquid float;
  no HTB profile). Specific borrow-fee/APR not retrievable from free WebSearch
  (Fintel/Ortex paywalled) — flagged. [SENT:borrow WebSearch]
- Implication: a fresh **short has no squeeze hazard** (good for a bear mechanically),
  but the share base is **not crowded short** either, so the bear isn't a consensus
  position in the equity — the bearishness lives only in today's options print.

### Positioning extremes

- **P/C z-score +3.83 → BEARISH_EXTREME** (phase-5; today 1.36 vs 20-day mean 0.243).
  |z|>2 = genuine sentiment extreme → **contrarian trigger**: the bear is stretched,
  not early. IV rank **20.35** (low; phase-0.5) — not a fear-driven IV spike.

## Divergences

1. **Options P/C bearish extreme (z +3.83) vs improving analyst revisions** (sb 5→7,
   zero sells, target $21.72) — the loudest disagreement.
2. **Institutional bearish LEAP put vs 66% institutional ownership + balanced dark
   pool** — one player short-biased against the institutional base.
3. **Bearish flow vs +33% price uptrend** (price-vs-flow DIVERGENCE, phase-7) — the
   crowd (price + analysts + insiders) is bullish; the flow is the outlier.

## Source calls (audit)

| Source | Result |
|--------|--------|
| Finnhub `company-news` (14d) | ok — 0 items |
| Finnhub `recommendation` | ok — sb 5→7, zero sells |
| fz `quote` Recom/target | ok — 1.12 / $21.72 |
| fz `quote` SI/float/own | ok — 5.69% / 1.80 dtc / 66.18% inst |
| WebSearch borrow/HTB | no specific fee (paywalled); inferred EASY |

## Source errors

- Borrow-fee/HTB figure not available free (Fintel/Ortex paywalled) — never pay;
  borrow status inferred EASY from SI + days-to-cover. Marked, not fabricated.

## Verdict for downstream

```
sentiment_signal:  BULLISH        # analyst revisions improving, strong-buy, zero sells — contradicts the bear
crowd_state:       BALANCED       # share base: 5.69% SI, 66% inst, no retail euphoria; options P/C at a transient bearish extreme
short_interest:    5.69% [fz, semi-monthly] ; days_to_cover: 1.80 ; borrow: EASY [WebSearch inferred]
tier_adjustment:   CAUTION        # one contrary axis (improving revisions) + bear is the crowded/late options trade; low SI ⇒ not a squeeze VETO
divergences:       [P/C bearish-extreme vs improving strong-buy revisions,
                    institutional LEAP put vs 66% inst ownership + balanced DP,
                    bearish flow vs +33% uptrend]
key_risks:         [bear is the crowded/late options trade (P/C z +3.83) → contrarian fade risk,
                    improving revisions + $21.72 target can squeeze a short on any positive headline,
                    news blind spot (0 items 14d) — no visible catalyst behind the put]
```

- **Gate effect (downside-only):** trims the bearish thesis one step (**CAUTION**) on
  the positioning axis — stacks on phase-7b's VETO. The crowd (analysts, insiders,
  price) is bullish; the bear has no squeeze fuel but is the *late* options trade.
  7c cannot add long conviction — it only confirms that a fresh directional short is
  ill-supported by positioning.
