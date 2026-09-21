# Phase 8b — Bull vs Bear Debate (disconfirmation)

**Ticker:** RKT
**As-of date:** 2026-06-05
**Generated:** 2026-06-06T18:40:00-04:00
**Upstream phases cited:** phase-1 … phase-8 (all read); dominant bias defended: SHORT (phase-8 plurality, 2 SHORT / 2 NEUTRAL / 0 LONG)

## Summary

Two full rounds. The **defender (SHORT)** held the mechanical case — no shelf
below $12.65, local short-gamma, spent GEX cushion, rising mortgage rates, and
a dated supply event (06-30 L-1 unlock) — but could not refute the
entry-location asymmetry: shorting 2.18% above the 52-week low, against an
improving business (4/4 beats), improving revisions, and armed squeeze
mechanics. The **attacker** conceded the 1–5d path of least resistance is
genuinely down but established that the *edge statistics* behind the short
(win-rate N=8, market-wide) cannot carry a conviction bet. Final residuals:
**defender 0.65 vs attacker 0.65 → `disconfirmed = true`** (attacker ≥
defender) — phase-9 must down-shift one conviction bin and cut one size step.
The single most important unrefuted point on each side: (defender) *there is no
documented support between $12.65 and $12.38, and none below it* [DP:price_levels
+ OI:oi_by_strike]; (attacker) *the business is improving on every measurable
axis while the street raises ratings into the decline — shorts at the 52w low
are short a coiled spring with 7.48% SI and a +60% street target* [FUND + SENT].

## Setup

- **thesis_defender = bull (SHORT)** — defends the phase-8 plurality (bearish
  lean, 1–5d/1–4w blend).
- **attacker (bear of the short)** — argues the short is wrong / the long side.
- Rounds: 2 (mandatory — phases 1–8 not unanimous; phase-7b = VETO).

---

## Round 1

### Defender (SHORT) — turn 1

The short here isn't a valuation opinion, it's a mechanics trade with a date
attached. Start with what's under the price: nothing. The five-day dark-pool
map shows every major institutional band at or above spot — $12.94–12.96
(~$135M) and $13.17–13.26 (~$163M) overhead, $12.65 at the close, and **no
cluster below $12.65 in the top fifteen** [DP:price_levels]. The OI map agrees:
all ten heaviest strikes sit above spot; the nearest "structure" is an ITM put
pocket at $13, and there is **no put-wall support below $12.64**
[OI:oi_by_strike]. Dealer structure makes the floor worse, not better: spot
sits inside a $12–$14 negative-gamma pocket whose largest strike is $13 at
net_gex −4,587,931 [STRUCT:gex per_strike], and the stabilizing book has been
ground from 47.6M to 1.33M total GEX in five sessions — a 97% collapse
[HIST:gex_time_series]. The day's tape was distribution where it counts:
block-tier derived sell_ratio 0.883 high-confidence [DP:block_stratified],
calls net-sold 12,773 bid vs 8,042 ask and puts net-bought 7,706 ask vs 3,119
bid ex-0DTE [FLOW:aggressor_ex0dte DUCKDB], and the single largest print of the
session was an opening **sale** of 3,460 Jul-10 $14.5 calls [FLOW:
top_premium_trades]. Macro is pushing the same way — 30y mortgage 6.59–6.69%
rising off the 6.09% low [MACRO:Mortgage30Y_2026-06-05], U-Mich at a record-low
44.8 [MACRO:UMich_2026-05-22] — and there is a dated, name-specific supply
event 17 trading days out: the Class L-1 unlock on 2026-06-30
[MACRO:RKT_L1_unlock_2026-06-30], with zero insider open-market buys in six
months standing under it [FUND:insider_tx]. Path of least resistance: probe
$12.38, then air.

## Strongest opposing point I cannot refute

"4/4 earnings beats with accelerating actuals (0.04 → 0.15), Q1 net income
$297M and operating cash flow +$1.857B, forward P/E 11.61 with PEG 0.18, and a
street that *raised* strongBuy counts from 4 to 6 as the stock broke down"
[FUND:earnings_surprises + financials_reported; SENT:recommendation]. I cannot
refute that the underlying business is improving — my response ("the growth is
inorganic, margins are thin") is a quibble about quality, not a refutation of
direction. Phase-7b counted two of three axes against me and issued a VETO on
the naked short; if the improving-business signal is right, my bearish flow
read is mostly macro hedging and mechanical supply, which clears after 06-30 —
making my trade a timing scalp, not a thesis.

## Residual confidence
Residual confidence: 0.65

### Attacker — turn 1

The defender's map is accurate and beside the point: he is describing the last
2.2%. The short he proposes enters at $12.65 against a 52-week low of $12.38
[HIST:52w_proximity fz] — that is the *entire* documented runway before the
trade is hoping into unmeasured territory, while the squeeze fuel above is
measured and armed: 7.48% short float, 2.86 days-to-cover [SENT:short_float fz
semi-monthly], a dealer book that is "classic vanna-squeeze setup if VIX
collapses" by the tool's own interpretation [STRUCT:vanna_charm], and a VIX at
21.51 after a +40% one-day spike [MACRO:VIX_2026-06-05 UW] — vol mean-reversion
is the single most reliable mechanic in this whole file set, and when it comes,
dealers short puts buy stock. His statistical edge is a market-wide
bearish_flow win-rate of 87.5% on **eight** observations over five days
[HIST:signal_backtest] — N=8, not RKT-specific, flagged low-confidence by the
phase's own pitfall rule. Meanwhile the only multi-month positioning facts in
evidence lean the other way: OI has built thirty sessions straight (+540,341)
[HIST:oi_trend], all three qualifying OI builds were bullish ask-skewed calls
(Sep-18 $13C +2,971) [OI:smart_positioning], an institution paid $257,910 at
the ask for Jan-2027 $9.2 deep-ITM calls while $9.2 puts were closed −407 — a
synthetic long [FLOW:sweeps; OI:decrease_with_volume] — and max-pain gravity
into both June expiries sits *above* spot at $14/$14.5 [STRUCT:max_pain]. The
90-day cumulative net flow is −$4.18M on $118.7M total — trend "MIXED"
[HIST:cumulative_premium_flow] — there is no sustained distribution campaign
here, just one ugly mechanical week that the street answered with upgrades.

## Strongest opposing point I cannot refute

"The five-day dark-pool map shows every major institutional band at or above
spot … and **no cluster below $12.65 in the top fifteen** [DP:price_levels];
all ten heaviest strikes sit above spot … **no put-wall support below $12.64**
[OI:oi_by_strike]." I cannot refute the air pocket. If $12.38 gives way —
into the unlock, with dealers short-gamma below $12.5 and no documented bid —
the downside does not mean-revert, it accelerates. My squeeze case is
conditional on VIX compression that has not happened yet; his vacuum is
unconditional and already on the map.

## Residual confidence
Residual confidence: 0.55

---

## Round 2

### Defender (SHORT) — turn 2

The attacker's best material is real but lives on a different clock. The
synthetic long at Jan-2027 $9.2, the Sep-18 $13C build, the +60% street target
[FUND:recom fz] — all 6-to-12-month instruments. None of them bids for stock
between now and June 30. What bids for stock this month? Dealers hedging a
negative-gamma pocket (they sell as it falls) [STRUCT:gex], a retail crowd
already long puts (no marginal seller, granted — but no marginal buyer either,
~1.1 contracts/trade [FLOW:sweeps]), and an insider class that has bought
exactly zero shares in the open market in six months [FUND:insider_tx]. On his
squeeze: the vanna trigger is *falling IV*, and phase-6 checked it — "the
trigger is **not live** today" with VIX +40% d/d and CPI + FOMC still ahead
[MACRO + STRUCT:vanna_charm]. A squeeze needs a spark date after the binaries
clear; the unlock lands first. On my N=8: conceded, the backtest is thin — which
is why the desk's own risk-monitor capped this at quarter-size defined-risk
[AGENT:risk-monitor], and why I'm defending a debit-put-spread expression in a
premium-buying regime (VRP −0.0852 [HIST:vrp]), not a conviction short. Small,
dated, defined — the mechanics still point down into 06-30.

## Strongest opposing point I cannot refute

"His statistical edge is a market-wide bearish_flow win-rate of 87.5% on
**eight** observations over five days [HIST:signal_backtest] — N=8, not
RKT-specific, flagged low-confidence by the phase's own pitfall rule." That is
my Kelly `p`, and it is statistically almost worthless. Strip it out and my
"edge" is a directional read on mechanics that two of four desk agents
declined to trade at all [AGENT:accumulation-hunter; AGENT:contrarian-scanner].
I am pressing a setup whose quantified historical win-rate I cannot defend at
sample size eight; everything else is structure-reading, and structure can be
repriced by one CPI print.

## Residual confidence
Residual confidence: 0.65

### Attacker — turn 2

The defender has now conceded the two load-bearing walls: the business is
improving (round 1) and the win-rate statistic is nearly worthless (round 2).
What survives is "mechanics point down for three weeks" — and even that is
half-conceded, since he agrees the squeeze fires once IV compresses; we differ
only on whether the spark lands before or after 06-30. Note what the gates
already did to his trade: 7b VETO (naked short → 0%) [FUND:tier_adjustment],
7c CAUTION (cut a step — improving revisions) [SENT:tier_adjustment], regime
guidance "half position sizes" [MACRO:MarketRegime_2026-06-05 UW], desk average
conviction 2.25/5 [AGENT]. A thesis that exits the gauntlet as a quarter-size,
three-week put spread is not a thesis the desk believes in; it's a lottery
ticket on the unlock. And the unlock itself cuts both ways: phase-7c found the
tape *led* the news with the −10.8% week unmatched by headlines [SENT:
company_news] — mechanical pressure that is at least partially pre-positioned,
on a name where the 06-04 session bounced +2.2% the moment selling paused
[HIST:trend]. I will not claim the long is ready — RSI 37.7 is not oversold
[HIST:rsi fz], there's no divergence [INSIGHT:price_vs_flow], and his air
pocket below $12.38 stands. But "short small into binaries at the 52-week low
against an improving business with armed squeeze mechanics" is a negative-
expectancy entry the moment any one of CPI, FOMC, or the unlock surprises
dovish, and three chances to surprise is a lot of chances.

## Strongest opposing point I cannot refute

"What bids for stock this month? … the vanna trigger is *falling IV*, and
phase-6 checked it — 'the trigger is **not live** today'" [STRUCT:vanna_charm;
MACRO]. I cannot refute the timing gap: my squeeze mechanism is real but
unarmed until vol compresses, and the defender's supply mechanics (unlock,
no shelf, short gamma) are live *now*. For the next one to three weeks his
window is genuinely better than mine, and if $12.38 breaks inside that window
the acceleration he describes happens before my spark arrives.

## Residual confidence
Residual confidence: 0.65

---

## Disconfirmation verdict

```
thesis_defender:  bull (SHORT)
bull_residual:    0.65
bear_residual:    0.65
disconfirmed:     true        # bear_residual >= bull_residual
strongest_bear_point: The business is improving on every measured axis (4/4 beats, Q1 NI $297M / OCF $1.86B, fwd P/E 11.61, revisions SB 4→6, target +60%) while the short enters 2.18% above the 52-week low with 7.48% SI and an armed-but-unsparked vanna squeeze — the bearish flow is macro/mechanical, not informed distribution [FUND:earnings_surprises + SENT:recommendation + STRUCT:vanna_charm].
```

Per `rubrics/confluence-scoring.md` and `rubrics/sizing-rubric.md` §Risk gates:
phase-9 **down-shifts the conviction bin by one and cuts one size step**,
quoting both residuals. The debate can only cut — the defender's surviving
mechanical case is already reflected in phases 1–8 and adds nothing here.
