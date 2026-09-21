# Phase 7c — Sentiment, Positioning & Short Interest

**Ticker:** NOW
**As-of date:** 2026-06-05
**Generated:** 2026-06-06T13:20:00-04:00
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md, phase-1-flow.md, phase-2-dark-pool.md, phase-5-historical.md, phase-7b-fundamentals.md

## Summary

The crowd is **structurally long and marginally panicking**: the street is
static crowded-bullish (54 analysts, 89% buy-or-better, unchanged 4 months;
fz Recom 1.36 / target +25% — no vendor divergence), institutional ownership
86.4%, while the *marginal* options crowd just rushed to puts at a **+6.09σ
P/C extreme** (phase-5) — late bearishness into a name with only **5.67%
short float and 2.18 days-to-cover** (no squeeze powder keg, but a $50B
corporate bid underneath). The lot-size split shows **no retail call
euphoria to fade — every tier was a net premium *seller*** on the as-of day.
Versus the run's bearish flow lean this is **one contrary axis (the short
side is crowded at the margin) → `tier_adjustment = CAUTION`** (cut one size
step) — not VETO, because the SI/squeeze mismatch is soft.

## Key signals

- **Analyst revisions: static, crowded-long** — Finnhub monthly: 15 SB / 33
  B / 5 H / 1 S / 0 SS (Jun-1), vs 15/32/4/1/0 in March — direction flat
  (+1 buy, +1 hold over 4 months) [SENT:recommendation]; fz cross-source
  Recom 1.36, target 140.63 (+25.1%) [SENT:recom fz] — **no Finnhub-vs-fz
  divergence**; ratings lag the −26.6% YTD tape.
- **Short interest 5.67% of float, DTC 2.18** [SENT:short_float fz
  semi-monthly — exchange settlement, ~2-week lag] — moderate, not
  squeeze-critical; borrow fee not sourced (n/a), mega-cap liquidity implies
  easy borrow (advisory inference only).
- **P/C z-score +6.09 BEARISH_EXTREME + IV rank 79.2 (94.9th %ile)**
  [SENT:positioning ← phase-5 HIST:pc_ratio_zscore,
  HIST:iv_percentile_zscore] — both contrarian triggers fire; the put rush
  is paying top-decile vol for protection AFTER a −17% fade.
- **No retail euphoria**: lot split (ask vs bid) — retail(<10) calls
  $12.48M ask vs $19.04M bid, retail puts $6.11M vs $8.15M; block(≥100)
  puts $3.15M ask vs **$15.87M bid** [SENT:lot_split DUCKDB] — all three
  tiers net-sold premium on both wings; institutions did the biggest put
  selling (the 135P block, phase-1).
- **News tone: mixed-bullish recovery framing, lagging price** — as-of-day
  headlines: "SaaS-pocalypse fears" peak-framing with a high-profile buyer,
  "Rerating Just Beginning" (SeekingAlpha), Cognizant AI-governance
  partnership (6/4–6/5), vs "Plunges 30% in 6 Months: Hold Tight or Book
  Profits?" [SENT:company_news — 198 items / 14d, look-ahead filtered].

## Detailed findings

### News flow (14d, 2026-05-22 → 2026-06-05)

[SENT:company_news] 198 items (heavy churn — itself a volatility flag).
Recent tone sample (all ≤ as-of): bullish-leaning — Cognizant Neuro AI
Trust × ServiceNow AI-governance integration (Benzinga 6/4, Yahoo 6/5);
"The Purple Pill Of AI Software, With Rerating Just Beginning" (SA 6/5);
"Trump Loaded Up on ServiceNow Stock at the Peak of SaaS-pocalypse Fears"
(Yahoo 6/5); balanced/cautious — "Plunges 30% in 6 Months: Hold Tight or
Book Profits?" (6/5); "Can EmployeeWorks Become a Major Growth Driver?"
(6/4). **News lags the tape**: the melt-up/fade already happened
(phase-5); the window's coverage is digesting it, framing the dip as
opportunity — sentiment-recovery, not capitulation, journalism.

### Analyst-revision momentum

[SENT:recommendation] last 4 monthly snapshots (look-ahead filtered):

| Period | StrongBuy | Buy | Hold | Sell | StrongSell |
|---|---|---|---|---|---|
| 2026-06-01 | 15 | 33 | 5 | 1 | 0 |
| 2026-05-01 | 15 | 33 | 5 | 1 | 0 |
| 2026-04-01 | 15 | 32 | 4 | 1 | 0 |
| 2026-03-01 | 15 | 32 | 4 | 1 | 0 |

Direction: flat (one net add each to buy and hold). 48/54 = **88.9%
buy-or-better through an 18% Q1 drawdown and a −26.6% YTD** — ratings have
not capitulated. fz `Recom` 1.36 / target 140.63 agrees [SENT:recom fz]:
**no cross-vendor divergence**; both say the street is anchored above the
stock (downgrade-cascade risk if 100–110 breaks; pre-loaded fuel for any
stabilization).

### Retail vs institutional

[SENT:lot_split DUCKDB §A — ask/bid only, as-of tape]

| Lot tier | Call ask | Call bid | Put ask | Put bid | Net read |
|---|---:|---:|---:|---:|---|
| retail (<10) | 12.48 | 19.04 | 6.11 | 8.15 | net seller, both wings |
| mid (10–99) | 8.87 | 14.98 | 12.62 | 15.39 | net seller |
| block (≥100) | 1.73 | 4.81 | 3.15 | **15.87** | net seller; put-write block dominates |

($M premium.) Retail and institutions are on the **same side** (premium
supply) — there is no retail-euphoria-vs-DP-distribution divergence; the
classic distribution-into-strength signature does NOT fire. Cross-ref
phase-2: DP tiers 0.46–0.48 buy (balanced-sell-lean) — consistent.

### Short interest & borrow

[SENT:short_float fz semi-monthly] Short Float **5.67%**, Short Ratio
(days-to-cover) **2.18**, float 1.02B (phase-0 snapshot identical —
no drift). Borrow fee / HTB: WebSearch returned no specific figure
(Fintel/MarketBeat track it but values not surfaced) → **borrow: n/a**;
for a $116B NYSE mega-cap at 5.67% SI the borrow is liquid by inference
(advisory, unsourced). SI read: enough shorts to fuel a bounce, nowhere
near squeeze-mechanics territory.

### Positioning extremes

Reused per spec: P/C z-score **+6.093 BEARISH_EXTREME** (0.80 vs mean 0.33,
20d) [phase-5 HIST:pc_ratio_zscore]; IV rank **79.23** = 90.4th universe /
94.9th own-history percentile [phase-0.5 CTX, phase-5
HIST:iv_percentile_zscore]. Both fire the |z|>2 contrarian trigger: the
marginal bear is paying extreme relative premium, late.

## Divergences

1. **Street vs options crowd**: 88.9% buy-or-better static ratings vs a
   +6.09σ put rush — somebody is wrong; historically static-rich ratings
   break *after* price, so this cuts against shorts short-term (bounce) and
   against longs medium-term (downgrade fuel).
2. **News tone vs tape**: recovery/opportunity framing while the stock fell
   17% in 4 sessions — news lagging, not leading; no capitulation headline
   yet.
3. **No euphoric counterparty**: all lot tiers net-sold premium — the
   "fade the crowd" trade has no crowd to fade on the call side; the
   crowded side is the freshly-bearish put tape.

## Source calls

| Source | Status | Extract |
|---|---|---|
| Finnhub `company-news` (5/22→6/5) | ok, 198 items, look-ahead filtered | tone mixed-bullish |
| Finnhub `stock/recommendation` | ok | 15/33/5/1/0 static |
| `fz quote NOW` (SI/DTC/float, Recom/target) | ok | 5.67% / 2.18 / 1.02B; 1.36 / 140.63 |
| DuckDB §A lot split | ok | table above [SENT:lot_split DUCKDB] |
| WebSearch borrow fee / HTB | ran; no specific figure | borrow n/a |
| Positioning extremes | reused phases 0.5 / 5 | z +6.09; IV rank 79.2 |

## Source errors

- Borrow-fee leg: no sourced value (Fintel/MarketBeat pages not exposing
  the figure via search) — recorded **n/a**, easy-borrow inference labeled
  advisory. No other source errors.

## Verdict for downstream phases

```
sentiment_signal:  NEUTRAL     # bullish street + bullish-recovering news vs 6σ bearish marginal options crowd
crowd_state:       CROWDED_LONG   # structurally (88.9% buy ratings, 86.4% inst own);
                                  # marginal options crowd is freshly CROWDED-BEARISH (6σ)
short_interest:    5.67% [fz, semi-monthly] ; days_to_cover: 2.18 ; borrow: n/a [WebSearch — no figure; easy by liquidity inference]
tier_adjustment:   CAUTION     # vs the bearish flow lean: short side crowded at the margin
                               # (6σ P/C extreme + $50B buyback bid); squeeze mismatch soft
                               # (SI 5.67%) → one contrary axis, not VETO
divergences:
  - "static 89%-buy street vs +6.09σ put rush — ratings haven't capitulated"
  - "recovery-framing news vs −17% four-session tape — news lags, no capitulation print"
  - "no euphoric call crowd exists — every lot tier net-sold premium"
key_risks:
  - "shorting into a 6σ put extreme + $50B buyback = sharp-bounce risk even with easy borrow"
  - "if 100–110 breaks, the un-capitulated street is a downgrade cascade (gap risk both ways)"
  - "198 news items/14d — headline-gap risk inside any defined-risk structure's window"
```
