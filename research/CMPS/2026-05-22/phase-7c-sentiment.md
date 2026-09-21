# Phase 7c — Sentiment, Positioning & Short Interest

**Ticker:** CMPS
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T00:00:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-4-structure.md, phase-5-historical.md, phase-6-macro.md, phase-7b-fundamentals.md

## Summary

The crowd **confirms the bullish direction but is crowded-long** — the classic
late-stage configuration. Trailing-14d news is **euphoric** (Q1 beat 5/13, "two-year
high," *"keeps getting hotter; bypassed a profit-taking zone,"* a stack of price-target
raises to $14–$22); analyst-revision momentum is **accelerating bullish** (buy count
10→13 Mar→May, **18 buy/strongBuy vs 2 hold vs 0 sell** — near-unanimous, no bears left
to flip); retail is excited (the complacent call skew, phase-4). Crucially, the *smart
money side* is still **accumulating** (phase-2 DP buy_ratio 0.839, phase-7 ACCUMULATION),
so this is **not** retail-euphoria-into-distribution — it is everyone-leaning-the-same-way
*with* institutions confirming. Short interest is **8.9% of float, days-to-cover 7.4, and
rising fast (+23.9% recent / +127.8% YoY)** — shorts pressing the bull thesis into a +114%
run: moderate squeeze fuel on a Q3 data win, but persistent skeptic supply and sharp
downside if the NDA/Part-B disappoints. Options positioning is **not** at a statistical
extreme (P/C z −0.55, IV-rank 12.25). Net: **sentiment BULLISH, crowd CROWDED_LONG →
tier_adjustment = CAUTION** (cut one size step). VETO is *not* triggered because smart
money is accumulating, not exiting.

## Key signals

- **News euphoric (14d)**: Q1 beat 5/13 (EPS −0.30 vs −0.34, "accelerated FDA review"), "two-year high," PT raises Maxim $20 / RBC $22 / MS $17 / BTIG $14 `[SENT:company-news]`.
- **Analyst revisions accelerating bullish**: 18 buy/SB vs 2 hold vs **0 sell**; buy 10→13 Mar→May `[SENT:recommendation]`.
- **Short interest 8.9% float, DTC 7.4, +23.9% recent / +127.8% YoY** — rising into strength `[SENT:short_interest WebSearch:marketbeat.com]`.
- **Crowded-long stack**: euphoric news + unanimous analysts + complacent skew (phase-4) + at 52w high (phase-7b) `[SENT:positioning]`.
- **Smart money still accumulating** (phase-2 DP 0.839) → not distribution-into-strength; downgrades CAUTION from VETO `[SENT:retail_vs_inst]`.
- **No options-positioning extreme**: P/C z −0.55, IV-rank 12.25 (phase-5/0.5) — sentiment is hot qualitatively, not on the P/C gauge `[SENT:pc_zscore]`.

## Detailed findings

### News flow (14d tone; lead/lag) `[SENT:company-news]`

Window 2026-05-08→05-22 (look-ahead-guarded). Tone **strongly bullish/euphoric**:
- **5/13 Q1 2026 earnings**: EPS −$0.30 beat −$0.34; "shares surge," "accelerated FDA
  review progress," "took a trip to a two-year high."
- **PT raises**: Maxim $20 (5/15), RBC Capital Outperform **$22** (5/14), Morgan Stanley OW
  $17 (5/14), BTIG Buy $14 (5/13).
- **5/14 SeekingAlpha**: "Imminent Commercialization Should Provide Further Upside."
- **5/18 Yahoo**: *"This Psychedelics Stock Just Keeps Getting Hotter; Why Shares Bypassed
  A Profit-Taking Zone"* — a textbook euphoria/melt-up headline.
- **5/8 Reuters** (the lone macro item): officials near HHS Sec. Kennedy "explored ban of
  some widely used antidepressants" — ambiguous-to-**bullish** for psychedelics (SSRI
  scrutiny favours alternative mental-health therapies).

**Lead/lag:** price **led**, news **confirmed** — the run preceded; earnings + PT raises
piled on after. A confirming-but-late news tape = momentum is well-recognized (crowded),
not an early/under-the-radar signal.

### Analyst-revision momentum (direction) `[SENT:recommendation]`

| Period | StrongBuy | Buy | Hold | Sell | StrongSell |
|--------|-----------|-----|------|------|------------|
| 2026-02-01 | 5 | 10 | 2 | 0 | 0 |
| 2026-03-01 | 5 | 10 | 2 | 0 | 0 |
| 2026-04-01 | 5 | 11 | 2 | 0 | 0 |
| 2026-05-01 | 5 | **13** | 2 | 0 | 0 |

**Revision trend positive and accelerating** (buy 10→13), **zero sell/strongSell** across
4 months. Confirms the bullish direction — but **near-unanimity (18:2:0) is itself a
crowded-long marker**: the upside from further upgrades is largely exhausted, and any
single downgrade would be asymmetric news.

### Retail vs institutional `[SENT:retail_vs_inst]`

- **Institutional (phase-2 DP):** ACCUMULATION, buy_ratio 0.839 — smart money on the long side.
- **Retail (phase-4 skew + news):** complacent call skew (25Δ calls richer than puts) +
  euphoric retail-facing headlines ("keeps getting hotter") = retail chasing upside.
- **Lit tape (phase-1):** call *selling*/roll, not aggressive ask-side buying — so the lit
  options crowd isn't pressing fresh longs even amid euphoria (the phase-7 price_vs_flow
  divergence again).
- **Same side?** Institutions + retail + analysts all **long** → confirmation *and* crowding.
  The saving grace vs a fade-setup: institutions are **accumulating**, not distributing, so
  the lit-flow isn't obviously exit liquidity.

### Short interest & borrow `[SENT:short_interest WebSearch:marketbeat.com]`

- **% float short: 8.9%** (~11.0M shares) — moderate (not the >20% squeeze tier).
- **Days-to-cover: 7.4** — meaningful; ~1.5 weeks of volume to cover → real squeeze potential
  on a positive catalyst.
- **Trend: +23.9% from prior period, +127.8% over 12 months** — shorts have **added
  aggressively into the +114% rally**. The bear case (valuation at 52w high, binary NDA/Part-B
  risk) is actively expressed.
- **Borrow:** not explicitly HTB in the data; rising SI suggests tightening but no hard-to-borrow
  flag found. Note SI is exchange-reported and ~2 weeks lagged.
- **Two-sided read:** 8.9% + DTC 7.4 = modest **squeeze fuel** for the bull case on a Q3 data
  win, *and* a standing skeptic supply / accelerant if the binary disappoints.

### Positioning extremes `[SENT:pc_zscore]`

P/C z-score **−0.553 (NORMAL)**, IV-rank **12.25** (phase-0.5/5). **No statistical
options-positioning extreme** (no |z|>2 trigger). So the crowding is qualitative (news,
analysts, skew, price-at-high) rather than a quantitative P/C/IV extreme — which keeps this
a CAUTION, not a contrarian-fade VETO.

## Divergences

1. **Rising short interest (+23.9%) into a +114% rally** — shorts pressing the bull thesis;
   skeptic supply + squeeze fuel coexist.
2. **Lit call selling/roll (phase-1) vs euphoric retail call-skew sentiment** — the tape is
   not aggressively buying calls despite the euphoria (momentum-confirmation gap; same root
   as phase-7's price_vs_flow divergence).
3. **Unanimous analyst bullishness (0 sells) vs a stock at its 52w high** — the good news is
   in; the asymmetry now favours disappointment (downgrade/"sell-the-news") risk.

## Source calls (audit trail)

| Source | Status | Extract |
|--------|--------|---------|
| Finnhub `/company-news` (14d) | ok | ~25 items, euphoric tone, Q1 beat + PT raises |
| Finnhub `/stock/recommendation` | ok | 18 buy/SB : 2 hold : 0 sell, buy rising |
| WebSearch short interest | ok | 8.9% float, DTC 7.4, +23.9% recent (marketbeat) |
| phase-5 `historical_pc_ratio_zscore` (reuse) | ok | z −0.553, NORMAL |
| phase-0.5 IV rank (reuse) | ok | 12.25 (not extreme) |

## Source errors

_None._ Finnhub key present; news look-ahead-guarded to 2026-05-22 (no later items quoted).
Short-interest figure is exchange-reported (~2-week lag) — directionally current as of mid-May.

## Verdict for downstream

```
sentiment_signal:  BULLISH        # news euphoric, revisions accelerating, institutions accumulating
crowd_state:       CROWDED_LONG   # unanimous analysts (18:2:0), euphoric news, complacent skew, at 52w high
short_interest:    8.9% float, DTC 7.4, rising (+23.9% recent) ; borrow: EASY-to-tightening (no hard HTB flag)
tier_adjustment:   CAUTION        # crowded long into a bullish thesis → cut ONE size step (not VETO — smart money still accumulating)
divergences:       [ "Short interest +23.9% into a +114% rally (skeptic supply + squeeze fuel)",
                     "Lit call selling/roll vs euphoric retail call-skew (weak momentum confirmation)",
                     "Unanimous analysts (0 sells) at 52w high → asymmetric downgrade/sell-the-news risk" ]
key_risks:         [ "Chase risk: crowded-long + at 52w-high + euphoric news → vulnerable to profit-taking pullback; prefer pullback entries",
                     "DTC 7.4 + rising SI is two-sided — squeeze on Q3 data win, sharp gap down if NDA/Part-B disappoints",
                     "No upgrade headroom left (0 sells); downside surprise is the asymmetric tail" ]
```

- **Positioning gate result: CAUTION (cut one size step).** The crowd confirms the bullish
  direction, but the name is **crowded long** (euphoric, unanimous, at its high) — so chase
  risk and "sell-the-news" pullback risk are elevated. This **stacks** with phase-6's
  TRANSITIONAL/half-size guidance and phase-7b's "at 52w-high, defined-risk" → phase-9 should
  size conservatively and **favour pullback entries to the $11 gamma wall / $10.6–$11.5 DP
  shelves over chasing**. Not a VETO: institutions are accumulating (phase-2), not
  distributing, so the lit flow is not obviously exit liquidity; and SI/positioning are not
  at squeeze/contrarian extremes. The rising short base is a mild bull tailwind (squeeze fuel)
  that phase-9 may *note* but must not size up on (filters never add).
