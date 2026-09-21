# Phase 8b — Bull vs Bear Debate (disconfirmation)

**Ticker:** SWKS
**As-of date:** 2026-07-31
**Generated:** 2026-08-02
**Upstream phases cited:** `phase-1-flow.md` … `phase-7-insights.md`, `phase-7b-fundamentals.md`, `phase-7c-sentiment.md`, `phase-8-agent-views.md`

## Summary

**The attacker won on the numbers.** The defender closed at **0.55** and the
attacker at **0.65**, so **`disconfirmed = true`** and phase 9 must down-shift one
conviction bin and cut one size step on top of the two CAUTION gates already
standing. The defender's structural case survived intact — **five independent
instruments do name the $60–65 box**, and nobody in two rounds refuted that. What
did not survive was the **tradeable expression**. The attacker's decisive point,
which the defender conceded in round 2, is that **"cheap vol" is not supported by
the run's own data**: the trailing-10-session realized vol of **55.53%** sits
essentially *on* `iv30d` of **55.90%** `[HIST:realized_decomp DUCKDB]`, so paying
49 days of theta to own a straddle is a bet on **an undated binary resolving inside
the window** — against management's own formal guidance of **early calendar 2027**
`[MACRO:SWKS_QRVO_merger_2026-07-28]`. The defender's single unrefuted point is
that **the only opening position on the entire options board was 3,333 puts SOLD at
$52.50** `[FLOW:unusual_volume]`, 1.1% above the 52-week low — someone with size
underwrote the downside, and no bear argument explained it away.

## Setup

- **Thesis-defender ("bull"):** defends the phase-8 plurality — **RANGE/NEUTRAL:
  SWKS holds the $60–65 box over 1–4 weeks, and the box is tradeable with defined
  risk (owning optionality beats standing aside).** Phase 8 returned **3 NEUTRAL /
  2 RANGE, 0 LONG, 0 SHORT**, average conviction **2.0/5**, so the defended thesis
  is explicitly non-directional. The tradeable half of the thesis comes from the two
  agents that proposed action — `earnings-scout` (conviction 3, buy Sep-18 vol) and
  `risk-monitor` (half-size defined-risk inside $60–65).
- **Thesis-attacker ("bear"):** argues the box is **not tradeable** — it either
  breaks (short gamma + an undated binary) or the expression bleeds (theta, adverse
  rotation, no measured edge).
- **Rounds run: 2.** The 1-round shortcut requires phases 1–8 to be unanimous *and*
  phase 7b to be `CONFIRM`/`NA`. Phase 7b returned **`CAUTION`**, so two rounds are
  mandatory.

---

## Round 1

### Bull — round 1

Start with what is not in dispute, because it is the strongest thing on this board.
Five instruments drawn from three different data sources independently name the same
two prices. Phase 4's per-strike gamma surface flips sign between 62.5 and 65
`[STRUCT:gex]`; max pain for the 2026-08-21 expiry — which holds **61.87% of tracked
OI** `[OI:term_structure]` — computes to **$65.00** `[STRUCT:max_pain]`; phase 3's
`oi-by-strike` tags **65 as `call_wall_resistance`** (`net_oi` +435) and **60 as
`put_wall_support`** (`net_oi` −625) `[OI:oi_by_strike]`; and phase 2's five-day
dark-pool levels cluster support at **$60.25–61.22** across three single blocks
totalling ~277,000 shares `[DP:price_levels]`. That is not one model repeated four
times. It is an options-chain read, a dealer-hedging read and a share-tape read
arriving at the same box. All five phase-8 agents named **$60.00 / $65.00**
independently `[AGENT:all]`.

Now the part the bear will attack, so let me put it plainly. On 2026-07-29 — the
session SWKS fell **−5.40%** on a 15.3-million-share tape — the dark pool absorbed
**+341,637 net shares (+$21,160,930)** at a clean regular-session directional buy
ratio of **0.634**, and followed it with **+232,129 (+$14,211,575) at 0.751** the
next day `[DP:net_imbalance DUCKDB]`. The baseline for the five sessions before that
was **+12,614 to +24,390** `[DP:net_imbalance DUCKDB]`. That is a **15–25×
step-change**, **0.383% of the float** `[FUND:peer_pe fz]` taken down in two
sessions, and it survived the removal of **39.4% of the day's shares** carrying
`average_price_trade` / `prior_reference_price` codes plus the entire wide-NBBO
closing auction `[DP:trade_codes DUCKDB]`. Somebody bought the break.

The options tape says the same thing from a different instrument. The **only**
contract on the entire SWKS board that opened in size was the Aug-21 **52.5 put,
volume 3,333 against open interest 947 — a vol/OI ratio of 3.52** — and it traded
**on the bid**, $219,979 of premium, 3 of the 7 trades printing as a single
2,664-lot bid-side sweep `[FLOW:unusual_volume]` `[FLOW:sweeps]`. That is a **sold**
put at a strike **1.1% above the 52-week low of $51.93** `[CTX:52w]`. Someone took
in real money to be a buyer of SWKS at $52.50 through August. Below the box, the
$56.91–57.50 zone has now been tested three times — 2026-07-15, 2026-07-16 and the
2026-07-29 intraday low `[HIST:gex_time_series]` — and phase 2's accumulation shelf
at **$58.44–59.34** (176,487 shares, $10,373,555, twelve blocks, 67,200 of them
printed **pre-market before 08:38 ET**) sits between them `[DP:accumulation_shelf DUCKDB]`.
Three instruments, one floor.

On the expression: vol is cheap **for this name**. IV rank 52.90 is the **29.9th
percentile of SWKS's own 78-session history** `[CTX:self_pctile DUCKDB]`, `iv30d`
has collapsed from 0.741 to 0.559 across the event `[HIST:trend]`, and realized vol
over the trailing five sessions is **63.49% against implied of 55.90%**
`[HIST:realized_decomp DUCKDB]` — realized has crossed **above** implied. Meanwhile
the crowd is **supplying** that vol: `net_call_premium` **−$170,899** and
`net_put_premium` **−$214,781**, both negative, with call ask-share **0.175** and put
ask-share **0.088** `[FLOW:ask_bid_split DUCKDB]`. And the term structure is **FLAT
across all eight expiries, 57.2%–60.7%, `kink_expiry: null`** `[STRUCT:iv_term_structure]`
into an undated SAMR Phase III decision that phase 6 identifies as the only event
capable of exceeding the ±9.10% implied move `[MACRO:SWKS_QRVO_merger_2026-07-28]`.
A binary that big should kink a curve. It has not. Be on the other side of the
sellers.

Two more things the bear has to carry. There is **no crowd to fade** — retail sold
**79.2% of its own call contracts on the bid** (397 bid vs 104 ask)
`[SENT:retail_vs_inst DUCKDB]`, so the classic distribution-into-euphoria setup is
categorically absent. And the business is not broken: **4 of 4 quarters beat** with
an average surprise of **+11.26%** `[FUND:earnings_surprises]`, the balance sheet is
**net cash ~$417M with a 2.38 current ratio** `[FUND:financials_reported]`, free cash
flow ran **$306.9M in the last reported half** (~6.5% annualised yield), insider
MSPR has **no negative month in the trailing year** (+100.00, +42.06, 0, +33.69)
`[FUND:insider_MSPR]`, and forward P/E of **12.63** is roughly **half the 17-peer
median of ~25.9** `[FUND:peer_pe fz]`.

## Strongest opposing point I cannot refute

The one I cannot answer is phase 5's sizing block: **`signal_backtest_win_rate:
null`, `win_rate_n: 0`, `win_rate_source: null`** `[HIST:signal_backtest]`. The
`dark_pool_accumulation` backtest — the class that matches the single strongest
signal I just spent three paragraphs on — returned
`{"note":"no backtest results","total_signals":0}` on **two** consecutive runs. I am
asking a desk to act on a dark-pool absorption pattern that this instrumentation has
**never once measured succeeding**. Worse, phase 3 gives me zero corroboration from
the other direction: `biggest-increases --min-oi-change 500` returned **empty**, and
the largest OI change anywhere on the chain was **46 contracts**
`[OI:biggest_increases]`. If real institutions were building a position, I would
expect *some* footprint in open interest, and there is none. I can say the buying
happened — I cannot say it has ever predicted anything, and I cannot corroborate it
in the chain. That is a genuine hole in the middle of my case, not a technicality.

## Residual confidence
Residual confidence: 0.65

---

### Bear — round 1

The defender's five-instrument box is real and I am not going to waste a turn
pretending otherwise. I am going to attack the two things he actually needs: that
the box **holds**, and that owning vol **pays**.

Start with holding. Phase 4 does not say dealers defend the box — it says the
opposite. `gex.regime` is **`NEGATIVE`**, with the description printed verbatim in
the file: *"Dealers net short gamma — expect trend acceleration and increased
volatility"*, and spot closed at **62.28 sitting directly on the most negative
per-strike GEX on the entire board, 62.5 at −448,437** `[STRUCT:gex]`. That is not a
pin. That is a hair trigger: dealers **sell into weakness and buy into strength**, so
a move off $62.50 is **amplified**, not damped. Phase 5 makes it structural rather
than incidental — SWKS has been in a negative-gamma regime for **29 of the last 30
sessions**, with the only flip 27 sessions ago on 2026-06-22 at a spot of **76.26**
`[HIST:gex_time_series]`. And look at what that regime has actually produced: over
those same 30 sessions the stock went **72.45 → 62.28, −14.03%**
`[HIST:trend]`, with a low of **$56.91**. A −14% slide with a 25% peak-to-trough
drawdown from $76.26 is not the price history of a name that respects a $5 box. The
defender is quoting a box drawn on a chart that has been broken repeatedly.

Now the expression, which is where his case actually fails. He quotes the
**five-session** realized vol of 63.49% and skips the ten-session number in the same
table: **55.53% against `iv30d` of 55.90%** `[HIST:realized_decomp DUCKDB]`. Vol is
**fairly priced**, not cheap. And the tool-level 30-day VRP is **+0.0663 with
`regime: "PREMIUM_SELLING"`** `[HIST:vrp]` — his own phase 5 had to argue *against*
its instrument to get to "premium-buying," and it got there on a five-session
estimate with a wide standard error. Meanwhile his proposed structure — phase 8's
Sep-18 straddle at the 57.2% curve trough `[AGENT:earnings-scout]` — carries **49
days of theta** on a binary that management's **formal guidance places in early
calendar 2027** `[MACRO:SWKS_QRVO_merger_2026-07-28]`. "Optimistic about calendar
2026" is not a date. He is paying real carry for a timing bet the company itself has
not made.

He says the flat term structure means the binary is unpriced. The simpler reading is
that it is **correctly priced**: the market does not expect SAMR to rule inside 49
days. `kink_expiry: null` `[STRUCT:iv_term_structure]` is consistent with both
stories, and only one of them requires the entire options market to be wrong.

On the fundamentals he is selective. Yes, 4 of 4 beats. Read the **actual EPS**
column in the same table: **1.76 → 1.54 → 1.15 → 1.08**, four consecutive sequential
declines, **−38.6% peak to trough** `[FUND:earnings_surprises]`. The company beats a
bar that keeps being lowered. `epsGrowthTTMYoy` is **−6.00%** on
`revenueGrowthTTMYoy` of **+2.33%** — margin compression `[FUND:metric]` — with
**ROE at 6.30%** on a 1.51-beta stock, and Q4 gross margin guided **down** to 44–45%
`[FUND:financials_reported]` `[MACRO:SWKS_Q3FY26_2026-07-28]`. His "forward P/E of
12.63 is half the peer median" has an answer sitting in the same row of the same
table: **`EPS Next Y` is −2.20%**, and SWKS is one of only **two of seventeen** peers
with negative expected growth `[FUND:peer_pe fz]`. It is cheap **because** it is not
growing. That is the definition of a value trap, and phase 8's contrarian agent —
whose entire job was to find the contrarian long — reached the same conclusion
independently `[AGENT:contrarian-scanner]`.

And he did not mention the sell side once. On **2026-07-29, seven of eight firms cut
price targets**: Mizuho to **$52 at Underperform**, Citi $64, JPM $65, TD Cowen $65,
RBC $70, Stifel $70, Morgan Stanley $72, with UBS the sole raise
`[SENT:news_flow finnhub]`. Mean **$66.00**, median **$67.50** — versus a spot of
$62.28, so the *average* target implies **+5.97%**, less than the front-expiry
implied move of ±9.10% `[CTX:implied_move]`. Not one of eleven post-print firms
carries a Buy. Sells have gone **1 → 3 since April** while coverage shrank **33 →
31** `[SENT:recom finnhub]`. And the dividend — a **4.56% TTM yield on a 91.35%
payout** — was **eliminated outright** `[MACRO:SWKS_dividend_elimination_2026-07-28]`,
which means the holder base is now selling for **mandate reasons, price-insensitively**,
and a syndicated screen was **still listing SWKS as a high-yield tech name on
2026-07-30** `[SENT:news_flow finnhub]`. That supply is not finished.

Finally the macro. The regime engine's own words: **`TRANSITIONAL — Mixed signals,
reduce position size, wait for clarity`**, with **34.1% bullish breadth** (2,142 of
6,280) and `trading_guidance` reading *"Half position sizes. Favor defined-risk
strategies"* `[MACRO:MarketRegime_2026-07-31 UW]`. Technology was the **largest
net-sold sector of eleven on the as-of date, −$187,715,752** aggressor-adjusted, and
SWKS's own RF/analog cohort is **net −$12.51M across five sessions, negative on four
of five** `[MACRO:MarketRegime_2026-07-31 UW]`. He wants to be long optionality into
an adverse rotation, in a half-size regime, with **both** downstream gates already
reading **CAUTION** `[FUND:tier_adjustment]` `[SENT:tier_adjustment]`.

## Strongest opposing point I cannot refute

The 52.5 put block. **3,333 contracts opened at a vol/OI ratio of 3.52, sold on the
bid for $219,979** `[FLOW:unusual_volume]` `[FLOW:sweeps]`, at a strike **1.1% above
the 52-week low**. I have been arguing that nobody has a view here — that the short
interest is arb plumbing, the P/C extreme is a statistical artifact, and the dark-pool
absorption is hedging mechanics. But this trade does not fit that story. **An arb
desk hedging a stock leg does not sell 3,333 naked-looking puts 15.7% out of the
money.** Somebody accepted real, quantified downside risk at $52.50 through
2026-08-21, and did it in the **only** size trade on the entire board — phase 7c
found **zero** trades between 101 and 500 contracts and **no call blocks at all**
`[SENT:retail_vs_inst DUCKDB]`. My best rebuttal is that it is premium harvesting
into crushed vol rather than a directional view, which is what phase 8's sweep desk
concluded `[AGENT:sweep-tracker]` — but that is a rebuttal about *motive*, not about
*exposure*. Whatever the motive, the seller is short those puts and is long that
risk. And it is uncomfortably close to Mizuho's **$52 Underperform target**
`[SENT:news_flow finnhub]`: the most bearish house on the street and the largest
opening options position on the board are underwriting **the same price from
opposite sides**, and I cannot claim that is evidence for me.

## Residual confidence
Residual confidence: 0.65

---

## Round 2

### Bull — round 2

The bear's strongest blow landed and I will take it before anything else: he is
right that I quoted the five-session realized vol and not the ten-session one. The
honest table is **30d 49.26% → 10d 55.53% → 5d 63.49%** against `iv30d` **55.90%**
`[HIST:realized_decomp DUCKDB]`. The ten-session figure is **at parity**, not below.
So "vol is cheap" is **not** a claim I can make on realized-vs-implied. What I can
defend is narrower and I will restate it as such: vol is cheap **relative to this
name's own history** — IV rank at the **29.9th self-percentile**
`[CTX:self_pctile DUCKDB]` — and the **direction of travel** is realized rising while
implied falls. That is a weaker claim than the one I opened with, and it changes what
I can justify: a straddle paying 49 days of theta on fairly-priced vol is **not**
supported. A **defined-risk structure with a much smaller premium outlay** still is.

On his regime attack he overstates one thing. He says the box has "been broken
repeatedly," citing 72.45 → 62.28 over 30 sessions. But that decline **is how price
arrived in the box** — it is the path, not a test of the level. The box has existed
for four sessions, since the 2026-07-29 gap. Every instrument that defines it was
measured **on 2026-07-31** `[STRUCT:gex]` `[STRUCT:max_pain]` `[OI:oi_by_strike]`.
Quoting a pre-existence decline as evidence the level fails is a category error.

That said — and this is the concession that matters — his short-gamma point does
real damage to the *range* thesis specifically. Phase 4 is unambiguous: `regime:
"NEGATIVE"`, spot on the −448,437 GEX minimum `[STRUCT:gex]`, and phase 5 shows the
regime has held for **29 of 30 sessions** with the ZGL drifting *away* from spot
`[HIST:gex_time_series]`. A range thesis wants dealers **long** gamma so they lean
against moves. Here they lean **with** them. So the correct reading of my own
evidence is that the $60–65 box is a **map of where supply and demand sit**, not a
**mechanism that holds price there**. Those are different claims and I conflated them
in round 1.

Where I still think he is wrong is the value-trap charge, and specifically the claim
that the flat curve is "correctly priced." Both readings are consistent with
`kink_expiry: null`, he says, and only one requires the market to be wrong. But the
market is **also** the thing that left `signal_confluence` scoring SWKS **0 of 6
bullish and 2 of 6 bearish on factors that phase 7 itself showed are misclassified**
— `high_pcr` built from put *selling*, `dp_distribution` computed on a raw 0.428 that
collapses to **0.461** once VWAP and auction prints are removed
`[INSIGHT:signal_confluence]` `[DP:buy_ratio DUCKDB]`. And no UW composite references
the merger, the eliminated dividend, the $2B raise or SAMR **at all**
`[INSIGHT:conviction_matrix]`. A market whose own instrumentation is scoring the
pre-merger security is not obviously pricing the post-merger one correctly.

And he still has not dealt with the asymmetry phase 7c uncovered. The **21.93% short
float, ~32.85M shares, 5.77 days to cover** `[SENT:short_float fz semi-monthly]` does
**not** cover on a deal close — the arb delivers received shares. It only buys in the
open market on a **break**. So the bear's own preferred catalyst produces a
**dealer-amplified squeeze** in a negative-gamma book. His downside path has a
violent upward tail inside it, and he cannot size a short around it either.

## Strongest opposing point I cannot refute

The theta-versus-timing point, which he sharpened and I cannot escape. Management's
**formal guidance is early calendar 2027**; "optimistic about calendar 2026" is
management colour, not a date `[MACRO:SWKS_QRVO_merger_2026-07-28]`. SAMR Phase III
is **undated**. So any long-vol expression is a bet that an unscheduled regulatory
decision lands inside my expiry, and I have **no evidence at all** about that timing
— it does not appear in any phase of this run. Combined with the concession I already
made — that ten-session realized is **at** implied, not below — I am paying fair
premium for an event with an **unknown and possibly out-of-window** arrival time.
That is negative expected carry unless the tail is fat enough to compensate, and I
cannot demonstrate that it is, because phase 5 gives me **`win_rate_source: null`,
`win_rate_n: 0`** `[HIST:signal_backtest]` — there is no measured base rate for
anything here. I have a coherent story and no edge I can quantify.

## Residual confidence
Residual confidence: 0.55

---

### Bear — round 2

I will take the concession and then give one back, because he earned it.

He is right that I mis-framed the −14.03% decline as evidence the box fails. The box
was measured on 2026-07-31 and has existed for four sessions
`[STRUCT:gex]` `[OI:oi_by_strike]`; the slide from 76.26 is the path into it. That
was a category error and I withdraw it. My short-gamma point stands on its own
without it — and he has now conceded the substance, which is what I wanted: the box
is a **map of supply and demand, not a mechanism**. In a negative-gamma book with
spot on the −448,437 strike `[STRUCT:gex]`, nothing holds price inside $60–65 except
the willingness of the same participants who have already been selling.

He is also right about the squeeze asymmetry, and I will not pretend otherwise: a
deal **break** forces ~32.85M shares of open-market covering into short gamma
`[SENT:short_float fz semi-monthly]` `[STRUCT:gex]`. I cannot run a clean short here.
But note what that concession actually costs me — **nothing**, because I am not
arguing for a short. I am arguing the position is **not tradeable**, and "the bear
case also has a violent upward tail" is an argument *for* my conclusion, not against
it. A setup where both tails are fat, the direction is unknown, the timing is
unknown and the base rate is **unmeasured** is a setup you do not put on.

His rebuttal that the market's instrumentation is scoring the pre-merger security is
his best remaining line, and it is genuinely clever — the composites are blind to
SAMR, the dividend and the $2B raise `[INSIGHT:conviction_matrix]`. But it proves too
much. If the UW composites are blind to the merger, so is every historical
relationship this run measured: the **78-session self-history percentiles**
`[CTX:self_pctile DUCKDB]`, the **30-session realized-vol series**
`[HIST:realized_decomp DUCKDB]`, the **gamma regime** `[HIST:gex_time_series]` — all
estimated on a security that stopped existing on 2026-07-28. Phase 6 flagged exactly
this as a **regime-change** `[MACRO:SWKS_QRVO_merger_2026-07-28]`. He cannot use
"the models are stale" to discredit the bearish composites while relying on the same
stale window for his 29.9th-percentile IV rank and his three-times-tested floor.
**That argument cuts his case as deeply as mine.**

Which leaves the scoreboard. He has conceded that vol is fairly priced, that a
straddle is unsupported, that the box is a map rather than a mechanism, that the
timing of his catalyst is unknown and possibly out-of-window, and that there is **no
measured base rate for any signal in this run**. I have conceded that the 52.5 put
block is real risk-taking I cannot explain away, and that I cannot short this. The
residual, then, is not "SWKS goes down." It is: **there is no expression of this
thesis whose expected value I can demonstrate is positive**, and everything
downstream agrees — phase 7b **CAUTION**, phase 7c **CAUTION**, phase 6 **ADVERSE
rotation** with the regime engine printing *"Half position sizes"*, and a phase-8
desk that returned **0 LONG, 0 SHORT and an average conviction of 2.0**
`[AGENT:all]`. Five specialists looked at this and not one would take a side.

## Strongest opposing point I cannot refute

The 52.5 put seller, still, and he sharpened it by pairing it with the floor. **3,333
contracts opened at vol/OI 3.52, sold on the bid** `[FLOW:unusual_volume]`, at a
strike sitting **1.1% above the 52-week low**, directly beneath a **$58.44–59.34
shelf where 176,487 shares and $10,373,555 traded in twelve blocks on 2026-07-29 —
67,200 of them pre-market before 08:38 ET** `[DP:accumulation_shelf DUCKDB]`, and
beneath a **$56.91–57.50 zone tested three separate times**
`[HIST:gex_time_series]`. Three different instruments — options, dark-pool blocks and
price — independently mark the same floor, and one participant paid real money to be
short puts into it. My "it's premium harvesting" answer explains the *motive* and not
the *exposure*, and my broader thesis that nobody has a view here simply does not
cover this trade. If I am wrong about this name, **this is the datapoint that will
have been the tell**, and I would rather say so plainly than dress it down.

## Residual confidence
Residual confidence: 0.65

---

## Disconfirmation verdict

```
thesis_defender:  bull (RANGE/NEUTRAL — $60-65 box, tradeable with defined risk)
bull_residual:    0.55
bear_residual:    0.65
disconfirmed:     true
strongest_bear_point: "Vol is fairly priced, not cheap — trailing-10-session realized
  55.53% vs iv30d 55.90% [HIST:realized_decomp DUCKDB] — so any long-vol expression
  pays 49 days of theta on an UNDATED SAMR decision whose formal guidance is early
  calendar 2027 [MACRO:SWKS_QRVO_merger_2026-07-28], with no measured base rate to
  justify it (win_rate_source: null, win_rate_n: 0 [HIST:signal_backtest])."
```

**How the residuals moved.** Both sides opened at **0.65**. The defender **fell to
0.55** after conceding three things in round 2: that ten-session realized vol is *at*
implied rather than below it (killing the "cheap vol" premise for a straddle), that
the $60–65 box is a **map rather than a mechanism** in a negative-gamma book, and
that the catalyst's timing is **unknown and possibly outside any tradeable expiry**.
The attacker **held at 0.65**, having withdrawn one bad argument (the −14% decline as
evidence of box failure) and conceded two real points (the 52.5 put seller is
genuine risk-taking; a short is un-runnable because of the break-driven squeeze) —
neither of which damages a thesis whose conclusion is *"this is not tradeable"*
rather than *"this goes down."*

**`bear_residual (0.65) ≥ bull_residual (0.55)` ⇒ `disconfirmed = true`.**

**Phase-9 effect (per `rubrics/sizing-rubric.md` §"Risk gates"):** down-shift the
conviction bin by one **and** cut one size step, quoting both residuals. This stacks
on top of `phase-7b-fundamentals.md`'s **CAUTION** and `phase-7c-sentiment.md`'s
**CAUTION**, and on `phase-6-macro.md`'s **adverse rotation** and verbatim regime
guidance *"Half position sizes. Favor defined-risk strategies."* The debate can only
cut; the defender's surviving points are **not** grounds to size up.

**The `strongest_bear_point` must appear in phase-9's `key_risks` or invalidation.**

**Points that survived two rounds unrefuted — phase 9 should carry both:**

- **For the defender:** the **3,333-contract short-put block at $52.50** — the only
  opening position on the entire board, sold on the bid at vol/OI 3.52, 1.1% above
  the 52-week low, sitting beneath a three-times-tested $56.91–57.50 floor and phase
  2's $58.44–59.34 shelf. **The attacker conceded twice that he could not explain it
  away.** It is the best evidence in the run that the downside is spoken for.
- **For the attacker:** **no measured edge exists anywhere in this blueprint** —
  `win_rate_source: null`, `win_rate_n: 0`, `dark_pool_accumulation` backtest
  returning **0 signals on two runs**, phase 3 showing **zero** OI corroboration
  (largest chain-wide change: **46 contracts**), and a phase-8 desk returning **0
  LONG / 0 SHORT at 2.0 average conviction**. **The defender conceded this in round
  1 and never recovered it.**
