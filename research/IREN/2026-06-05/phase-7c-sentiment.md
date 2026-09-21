# Phase 7c — Sentiment, Positioning & Short Interest

**Ticker:** IREN
**As-of date:** 2026-06-05
**Generated:** 2026-06-07T01:52Z
**Upstream phases cited:** phase-0-intake.md (SI pre-flag), phase-0.5-context.md, phase-1-flow.md, phase-2-dark-pool.md, phase-5-historical.md (P/C z), phase-7b-fundamentals.md (peer SI)

## Summary

The crowd is **split down the middle, and the split is the signal**: Wall
Street turned MORE bullish into the crash (B. Riley raised its PT to **$96**
on 06-04, Canaccord to **$79** on 06-03, both *during* the −18% slide; news
flow carried the bullish 800MW South-Australia transmission agreement on
06-03) [SENT:news, SENT:recom], while the trader crowd flipped freshly bearish
TODAY — retail small-lots bought puts (+$2.7M net) and sold calls (−$7.7M
net), the front week is the most put-skewed expiry on the board (P/C OI 3.43,
phase-3), and the 20d P/C z-score is +1.47 [SENT:pc_z]. Block-size lots did
neither: they sold premium on BOTH sides (calls −$12.0M, puts −$13.9M at bid)
— institutions are harvesting the 130% front-end vol, not taking direction
[SENT:retail_vs_inst DUCKDB]. Short interest is **15.71% of float but
cohort-LOW** (peers 18.5–34.1%), days-to-cover just **1.20**, borrow **EASY**
(0.28% fee, 10M shares available) [SENT:short_float fz semi-monthly,
WebSearch:fintel.io] — squeeze fuel exists but isn't trapped. For the bearish
flow bias this is **CAUTION**: the short/hedge side just got crowded *after*
the move, and analyst momentum points the other way — but no hard
squeeze/borrow mismatch, so no VETO.

## Key signals

- **PT raises INTO the crash**: B. Riley Buy, PT → $96 (2026-06-04); Canaccord
  Buy, PT → $79 (2026-06-03) — the Street re-anchored bullish while price fell
  −18% [SENT:news Finnhub, look-ahead filtered ≤06-05].
- **Recommendation counts just started softening at the margin**: Jun-01 6
  strongBuy / 9 buy / 5 hold / 1 sell vs May-01 6/11/5/1 (−2 buys, +0 hold
  net) — first deterioration in 4 months, still overwhelmingly positive;
  consistent with fz Recom 1.94 / target 84.15 (no vendor divergence)
  [SENT:recom, SENT:recom fz].
- **Retail bearish / blocks vol-selling**: small-lot (≤10) net: calls −$7.65M
  (sold), puts +$2.69M (bought); block (≥100) net: calls −$11.99M AND puts
  −$13.86M (both SOLD at bid — the phase-1 55/56 strangle signature)
  [SENT:retail_vs_inst DUCKDB §A].
- **SI 15.71% / DTC 1.20 / borrow EASY (0.28%, 10M avail)** — elevated vs
  market, lowest in cohort (MARA 26.7 / RIOT 18.5 / CLSK 34.1 / APLD 30.4,
  phase-7b table); FINRA-settlement basis, semi-monthly lag flagged
  [SENT:short_float fz semi-monthly, WebSearch:fintel.io].
- **Positioning extremes not extreme**: P/C z +1.47 (< |2| contrarian bar),
  IV rank 48.2 mid-range [SENT:pc_z phase-5, CTX phase-0.5] — stressed, not
  capitulated.

## Detailed findings

### News flow (14d, Finnhub company-news, n=30, all items ≤ as-of)

Tone: **bullish-to-mixed coverage against a falling tape** — price LED the
news down. Highlights: 06-05 "IREN Limited: An AI Powerhouse In Play" (SA);
06-04 "Why Is IREN Stock Falling On Thursday?" (Benzinga) alongside the B.
Riley PT raise; 06-03 "IREN Stock Rises After Securing Transmission Connection
For Planned 800MW Data Center Campus" + Canaccord raise; cohort noise (MARA
$1.5B acquisition, CLSK "fundamentals keep getting uglier", CoreWeave/Nebius
comparisons). No company-specific negative item in the window — confirms
phase-6: the decline is macro/BTC-transmitted, not news-driven.

### Analyst-revision momentum

| Period | strongBuy | buy | hold | sell |
|---|---|---|---|---|
| 2026-06-01 | 6 | **9** | **5** | 1 |
| 2026-05-01 | 6 | 11 | 5 | 1 |
| 2026-04-01 | 6 | 11 | 4 | 1 |
| 2026-03-01 | 6 | 11 | 4 | 1 |

Direction: flat for 3 months, **first softening in June** (buy 11→9). Yet PT
momentum is UP (two raises this week). Read: coverage is consolidating around
"buy the AI story, trim the conviction" — a late-cycle rating pattern. No
Finnhub-vs-fz divergence (both ≈ buy/strong-buy with PT $79–96 band).

### Retail vs institutional [SENT:retail_vs_inst DUCKDB §A] (lit tape, ask/bid only, full day)

| Lot size | Calls net (ask−bid) | Puts net (ask−bid) | Read |
|---|---|---|---|
| small ≤10 | −$7.65M (sold) | +$2.69M (bought) | **bearish/hedging** |
| mid 11–99 | −$4.80M (sold) | +$5.57M (bought) | bearish |
| block ≥100 | −$11.99M (sold) | **−$13.86M (sold)** | **vol-selling, non-directional** |

Retail+mid chased the move down (put buying into 130% front IV — paying up
for protection after the fact); blocks faded the vol on both sides.
Divergence: the crowd is directional-bearish, the size is short-vol-neutral.

### Short interest & borrow

- fz (point-in-time, FINRA semi-monthly settlement basis): short_float
  **15.71%**, short_interest 50.94M sh, days_to_cover **1.20**, float 324.15M
  [SENT:short_float fz semi-monthly].
- Borrow (WebSearch, fintel.io): fee **0.28%**, **10M shares available** —
  **EASY**, not HTB. (Fintel's own SI vintage cited Jan-30 41M/12.47% — older
  than the fz figure; fz used as primary per recipe.)
- Verdict: real short base, zero mechanical trap. A BTC bounce squeezes
  sentiment, not borrow.

### Positioning extremes

P/C z-score **+1.47** (20d; phase-5) — elevated, below the |z|>2 contrarian
trigger. IV rank **48.2** (phase-0.5) — mid-range; the vol surface is
stressed in shape (backwardation, phase-4) not in level. Front-week P/C OI
**3.431** (phase-3) is the crowding locus: the hedge ladder all sits in 06/12.

## Divergences (crowd vs flow)

1. **Street vs tape**: two PT raises ($96, $79) + bullish 800MW news during a
   −18% three-session crash — analysts bullish, flow bearish.
2. **Retail vs blocks**: small-lots directional-bearish (bought puts at 130%
   IV) while block-size sold premium both ways — the size is fading the move
   the crowd is chasing.
3. **Options crowd vs stock borrow**: front-week puts crowded (P/C OI 3.43)
   yet equity borrow EASY / DTC 1.2 — the bearishness is rented (one-week
   options), not structural (stock short).

## Source calls

| Source | Status | Key value |
|---|---|---|
| Finnhub company-news 05-22→06-05 | OK (n=30, look-ahead filtered) | PT raises 06-03/06-04; 800MW deal |
| Finnhub /stock/recommendation | OK (4 periods ≤ as-of) | Jun buy 9 (−2 m/m) |
| fz quote (SI block) | OK | 15.71% / DTC 1.20 / 50.94M sh |
| WebSearch borrow fee | OK | 0.28%, 10M avail → EASY [fintel.io] |
| DuckDB §A small-lot split | OK | table above |
| Phase-5 P/C z / phase-0.5 IV rank | reused | +1.47 / 48.2 |

## Source errors

(none — all legs returned; SI semi-monthly lag and Fintel's older SI vintage
flagged inline.)

## Verdict for downstream phases

```
sentiment_signal:  NEUTRAL            # Street bullish vs trader-crowd freshly bearish — offsetting
crowd_state:       CROWDED_SHORT      # front-week options only (P/C OI 3.43, fresh 2-day put ladder);
                                      # equity short base cohort-LOW with EASY borrow — not a structural crowd
short_interest:    15.71% [fz, semi-monthly] ; days_to_cover: 1.20 ; borrow: EASY (0.28%, 10M avail) [WebSearch:fintel.io]
tier_adjustment:   CAUTION            # for the BEARISH flow bias: crowd already leaning the thesis's way
                                      # (fresh put crowding) + contrary analyst-revision momentum (PT raises);
                                      # no HTB/squeeze mismatch → not VETO
divergences:
  - "Street raised PTs ($96/$79) into the −18% slide — analysts vs tape"
  - "Retail bought puts at 130% IV while blocks sold premium both ways"
  - "Front-week put crowding vs easy stock borrow — bearishness is rented, not structural"
key_risks:
  - "Crowded-short unwind: any BTC bounce >$65k forces the 06/12 put ladder + retail hedges to unwind into a beta-4.28 name"
  - "Downgrade-cycle fuel: PT anchors $79–96 vs spot 54.35 — if BTC stays <$65k, cuts begin and the bullish Street pillar flips"
  - "Whipsaw window: CPI 06/10 + FOMC 06/16-17 land exactly on the crowd's 06/12 hedge expiry and 06/18 OPEX magnet"
```
