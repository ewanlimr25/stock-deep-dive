# Phase 8b — Bull vs Bear Debate (disconfirmation)

**Ticker:** MU
**As-of date:** 2026-07-28
**Generated:** 2026-07-28T23:34:00-04:00
**Upstream phases cited:** `phase-1-flow.md` … `phase-7c-sentiment.md`, `phase-8-agent-views.md`

## Summary

**The short thesis survived on the facts and failed on the execution — and that is enough to
disconfirm it.** The thesis-defender's core claim held up under two rounds of attack and was
never refuted: **regular-hours dark-pool selling of 0.227 at the mega tier with the heaviest
selling at the *lowest* prices** is a realised fact about today's tape, not a forecast, and the
attacker conceded it explicitly in both rounds. But the attacker landed three blows the defender
could not answer: **the business is compounding at +166.98% revenue growth with 4/4 beats and a
5.1% debt/equity ratio while the entire bear case is a 2027–28 forecast** (`[FUND:]`); **realised
vol of 109.12% exceeds implied of 96.04%, so the short is being asked to pay for protection that
is cheap precisely because the market has not panicked** (`[HIST:vrp]`); and **a
capital-committed counterparty has been opening short puts at 750/800 for six consecutive
sessions, accelerating as price falls** (`[OI:]`) — someone with real money is underwriting the
exact zone the short must travel through.

Both sides finished at **0.65**. Since `bear_residual >= bull_residual`, **`disconfirmed = true`**
— phase-9 must **down-shift the conviction bin by one and cut one size step.**

**The single most important unrefuted point on each side:**
- **Defender (short):** the dark-pool distribution is *observed*, corroborated by the after-hours
  slide to $780, and sits inside a `FULLY_NEGATIVE` gamma regime with `zero_gamma_level = null`
  — there is no mechanical brake below.
- **Attacker (long/no-short):** you are being asked to short a company earning a 72.57% gross
  margin at 5.31× forward earnings, into a binary FOMC, in a regime where a 10.1% ATR makes any
  survivable stop wider than the move you are trying to capture.

## Setup

- **Dominant bias from phase-8:** **SHORT** — the plurality directional vote (SHORT 2 /
  NEUTRAL 2 / LONG 0 / RANGE 0, average conviction 2.5).
- **Thesis-defender = "bull" = defends the SHORT.**
- **Thesis-attacker = "bear" = argues against the short (i.e. long or stand-aside).**
- **Rounds run: 2.** One round is permitted only when phases 1–8 are unanimous *and* phase-7b is
  `CONFIRM`/`NA`. Neither holds: phase-8 split 2-2, and **phase-7b returned `VETO`**.
- Run inline as two voices, each turn seeing the prior transcript.

---

## Round 1

### Bull turn (defending the SHORT)

The case for being short MU does not rest on the headline flow, and I want to concede that at the
outset so we argue about the right thing. MU's net directional premium was **+$28,557,121 on
$2.83B of gross two-way flow — a 1.0% tilt** `[FLOW:insights_deep_dive]`, and the net customer
delta across the entire tape was **-$41M ex-0DTE against a $926.7B market cap**
`[FLOW:delta_notional DUCKDB]`. That is nothing. Anyone arguing MU from the options tape is
reading noise, in either direction.

The case rests on what institutions actually *did with stock*. MU was the **single largest
dark-pool name in the entire market today — $12,931,901,814 across 15,787,788 shares, 1.41% of
the 1.12B float, ahead of both SPY and QQQ** `[DP:ticker_summary]`. The composite tools read that
as accumulation because the mega-tier `buy_ratio` printed **0.803** `[DP:block_stratified]`. It
is not accumulation. Eighty-eight percent of that mega-tier premium is **post-close crosses
struck at exactly the $820.53 closing price against a stale NBBO of 818.18/819.03** — and when
you restrict to regular hours the same classifier, reproduced to three decimals, gives
**0.227: nine mega sells against three mega buys, 196,620 shares sold versus 57,902 bought**
`[DP:block_stratified]`. Every tier is a net seller in regular hours — mega 0.227, block 0.423,
large 0.481. And the gradient is the part that matters: the buy ratio is **lowest at the lowest
prices — 0.411 in the $790s and 0.419 in the $800s, against 0.497 in the $820s** `[DP:price_bins
DUCKDB]`. Institutions did not absorb the dip. They fed it. The after-hours tape then carried the
same message without the auction contamination: stripping the 61 prints at the closing price,
post-close trading VWAP'd at **$809.02**, and the last prints of the evening were at
**$780.00–789.00, roughly 5% below the close** `[DP:extended_hours]`.

Now put that on top of the dealer structure, because this is where a distribution day becomes a
trend. MU's gamma regime is **`FULLY_NEGATIVE` — `total_gex` -45,676,510 with
`zero_gamma_level = null`** `[STRUCT:gex]`. That null is not a missing value; it is the finding.
**There is no price anywhere on the 45-DTE surface at which dealers flip to long gamma.** They
buy rallies and sell dips at every level, and `net_dex` of **-$9,116,110,160** means the standing
hedge is to **sell underlying** `[STRUCT:dex]`. We have a live, dated demonstration that this
matters: the historical series flags a **regime flip on 2026-07-23**, after which MU printed
**-6.99%, -2.25%, -8.85% — -17.1% in three sessions** `[HIST:gex_time_series]`. The regime has
now been `FULLY_NEGATIVE` for three consecutive sessions.

And the four lenses converge on one number. The **largest negative-gamma strike in the entire
chain is $800 at -6,527,065** `[STRUCT:gex]`; **$800 is also the dominant put wall — 84,213
contracts of OI, net -32,711, sitting 2.39% below spot** `[OI:oi_by_strike]`; **$800 is where the
dark-pool selling was heaviest**; and **$800 is the strike the closing put-strip sale was written
at** `[FLOW:top_premium_trades]`. Four independent instruments, one level, and price closed
$20.53 above it having already traded to **$789.09** intraday `[HIST:screener_low]`.

Finally, there is no floor nearby. **RSI is 40.29 — not oversold** — and MU remains **+61.28%
above its 200-day moving average** while trading -13.44% below its 20-DMA and -14.37% below its
50-DMA `[HIST:rsi fz]` `[HIST:sma fz]`. The stock is **+187.49% YTD and +637.56% over one year**
`[HIST:perf fz]`. A -32.4% drawdown has retraced a fraction of a parabola whose local base was a
**355.46 close on 2026-03-26** `[CTX:self_history DUCKDB]`. There is no valuation support, no
technical support, and no oversold condition between here and a very long way down.

## Strongest opposing point I cannot refute

The point I cannot answer is phase-7b's, and I will quote it as written rather than soften it:
**"Revenue is +166.98% TTM YoY, EPS +700.71%, gross margin 72.57% TTM (76.6% on the nine-month
10-Q), operating margin 65.63%, net margin 55.91%, ROE 70.55%... and 4 of 4 earnings beats with
EPS ramping $3.03 → $4.78 → $12.20 → $25.11 in four quarters"**, with **long-term debt of $5.14B
against ~$100.7B of equity — 5.1%** `[FUND:financials_reported]`, and operating cash flow of
**$45.70B on net income of $47.27B, a 96.7% conversion ratio** `[FUND:cash_flow]`. Phase-7b
returned **`tier_adjustment = VETO`** against precisely the thesis I am defending, on the
grounds that two of the three fundamental axes contradict it.

My rebuttal is weak and I know why. I want to say "those are peak-cycle earnings" — and the
`peNormalizedAnnual` of **108.93 against a `peTTM` of 18.43** `[FUND:peNormalizedAnnual]` does
support me. But that is a *forecast* about mean reversion, and the thing I am forecasting has
not started. Phase-6 establishes that DRAM is currently in **shortage, not oversupply**, with
**contract prices up 93–98% QoQ in Q1 2026**, HBM at a **5–8× ASP premium**, and **CXMT's HBM3E
mass production not targeted until 2027** `[MACRO:DRAM_pricing_Q1-2026]`. I am short a business
whose realised financials are improving on every observable axis, on the strength of a
competitive threat that is eighteen months from mattering. If the cycle rolls over later than I
think — and I have no dated evidence that it rolls over at all in 2026 — I am simply wrong and
the fundamentals will grind me out.

## Residual confidence
Residual confidence: 0.65

---

### Bear turn (attacking the SHORT)

I accept the defender's dark-pool work. I am not going to pretend the 0.227 does not exist —
it does, the decomposition reproduces UW's own 0.803 to three decimals before inverting it, and
the price-bin gradient showing heaviest selling at the lows is genuinely damning `[DP:price_bins
DUCKDB]`. If the question were "did institutions distribute MU today," the answer is yes. But
that is not the question. The question is whether *you should be short MU tomorrow morning*, and
on that the defender has not made a case — he has made an observation.

Start with the instrument problem, because it is fatal before we get to direction. Phase-5
returns **`vrp = -0.1308` with `regime = "PREMIUM_BUYING"`: 30-day realised volatility of 109.12%
against IV30 of 96.04%** `[HIST:vrp]`, and the tool's own language is *"Vol cheap vs realised —
favour premium buying."* So: you cannot express this short by selling calls or call spreads,
because you would be selling volatility that is already 13 points too cheap. You can buy puts —
but note that the market agrees with you on nothing, because **25-delta skew is `NORMAL` at a
ratio of 1.053** `[STRUCT:term_skew]`, meaning after an 8.85% collapse there is *no crash premium
whatsoever* in the surface. And you cannot short the stock with a sensible stop, because
**ATR is 83.13 — 10.1% of spot** — with weekly and monthly realised volatility of 6.75% and 6.91%
`[HIST:atr fz]`. The defender's own `FULLY_NEGATIVE` gamma argument cuts against him here: a
regime that amplifies moves in **both** directions is a regime that runs your stop before it pays
you. Phase-8's risk-monitor said it plainly — **"any stop tighter than ~8-10% sits inside a
single day's noise"** `[AGENT:risk-monitor]`.

Second, the defender skipped the one genuinely capital-committed footprint in the entire run, so
I will supply it. Someone has been **opening** — not closing — **short puts at the 750 and 800
strikes across Sep-26, Oct-26, Dec-26, Jan-27, Feb-27, Mar-27 and Jun-27 for six consecutive
sessions, with open interest rising on bid-dominated volume: 7/23 +324 and +167, 7/27 +360 and
+550, 7/28 +216 and +200, every one of them lopsided to the bid (465/12, 302/0, 551/1, 455/99,
217/1, 201/2)** `[OI:biggest_increases DUCKDB]`. And the campaign **accelerated as price fell** —
+554 contracts on 7/23, +975 on 7/27, +416 on 7/28. That is a desk being paid $50–$191 a contract
to own MU at 750–800 out to eleven months. It is the only participant in this entire deep dive
who has taken a dated, directional, capital-at-risk position, and they are on the other side of
the defender's trade, in size, at exactly the level he wants to break. Note also who *else* is
paying attention: phase-8's **accumulation-hunter — the agent whose sole function is to find
institutional buying, and which voted SHORT — nominated this campaign as its own `top_risk`**,
conceding it is "a genuine... constructive structural footprint that could be the leading edge of
real accumulation" `[AGENT:accumulation-hunter]`.

Third, the structural gravity runs against him. **Max pain is 930 on the 7/31 expiry (+13.47%)
and 940 on 8/21 (+14.69%)**, with the 7/31 expiry alone holding **18.38% of MU's entire open
interest at a put/call OI ratio of 2.592 — 291,008 puts against 112,250 calls** `[STRUCT:max_pain]`
`[OI:term_structure]`. That is an enormous, deeply in-the-money put book that decays toward the
defender's counterparties, not his. And phase-4 identifies the mechanism by which it unwinds
violently: **`net_vanna` +5,467 on a put-heavy book, with the tool's own note reading "Classic
vanna-squeeze setup if VIX collapses"** `[STRUCT:vanna_charm]`. Dealers are short those puts. If
implied vol falls, their hedges force them to **buy** stock.

And there is a dated trigger for exactly that, tomorrow. **The FOMC decides at 2026-07-29 14:00
ET with no SEP and a Warsh press conference at 14:30** `[MACRO:FOMC_2026-07-29]`, into a setup
where **June CPI came in at 3.5% headline with a -0.4% monthly print — the largest since April
2020 — core at 2.6%, both below consensus, and June payrolls missed at +57k against 115k
expected** `[MACRO:CPI_2026-06]` `[MACRO:PAYEMS_2026-06]`. The macro data argues dovish. A dovish
Fed collapses front-end implied vol — which is running at **151–152% on the 7/29 and 7/31
expiries** `[STRUCT:iv_term_structure]` — and fires the vanna squeeze into a market whose
own max-pain magnet sits 13% higher. The defender is short into that binary with no gamma brake
in his favour either.

Finally, the historical record refuses to validate him. **`bearish_flow` backtests at an 80% win
rate — but on n=10, market-wide, with the tool self-disclaiming "In-sample backtest — not a
robust live edge"** — and phase-1's actual flow verdict was **MIXED, not bearish**, so the class
does not even match `[HIST:signal_backtest]`. Over 75 sessions MU's cumulative premium flow nets
**+$320,661,260 on $200.8B gross — +0.16% — with `trend_direction = "MIXED"`**, and the 30-session
window records **17 bullish days against 13 bearish while price fell 24.6%** `[HIST:trend]`.
Flow sign has had no predictive relationship to MU's price. Neither, then, does today's.

## Strongest opposing point I cannot refute

The claim I cannot get around is the defender's price-gradient finding, quoted exactly:
**"the buy ratio is lowest at the lowest prices — 0.411 in the $790s and 0.419 in the $800s,
against 0.497 in the $820s"** `[DP:price_bins DUCKDB]`, corroborated by an after-hours VWAP of
**$809.02** and closing prints at **$780.00–789.00** `[DP:extended_hours]`.

I have been arguing that MU is oversold into a structural bid, and this is the direct refutation.
If institutions were accumulating a dislocation, the buy ratio would *rise* as price fell —
that is what absorption looks like. Instead it falls monotonically. My best rebuttal is that
NBBO-based classification is probabilistic and that a single session is not a campaign, but that
is genuinely weak: the effect is monotonic across five price bins, it holds across every size
tier, and it is independently corroborated by an after-hours tape that kept sinking to $780 with
no auction artifact available to explain it away. I also cannot explain why, if my 750/800
put-writer is so committed, they were not visibly bidding for stock at $790 today. The honest
answer is that selling a put eleven months out and buying stock at the lows are very different
levels of commitment, and only the cheaper one was in evidence.

## Residual confidence
Residual confidence: 0.60

---

## Round 2

### Bull turn (defending the SHORT)

The attacker's strongest move was to shift the argument from *direction* to *execution*, and I
have to meet him there because he is largely right about it. But I want to first collect what he
conceded, because it is the whole ballgame: he accepts the 0.227, he accepts the monotonic price
gradient, and he admits he "cannot explain why, if my 750/800 put-writer is so committed, they
were not visibly bidding for stock at $790 today." That concession is more damaging to his case
than he allows. **Writing a put at 750 eleven months out is not a bid for stock at 790.** It is a
yield trade with a strike 8.6% below the market and time value that pays you to be patient. The
total campaign is **+2,370 contracts — 237,000 share-equivalents, 0.021% of the 1.12B float**
`[OI:oi_pct_float fz]`. Against 15.79M shares of dark-pool volume — **1.41% of float** — on the
distribution side `[DP:ticker_summary]`, his marginal buyer is outweighed roughly seventy to one.
He has built a thesis on the smallest real position in the run.

On max pain: he is quoting a static-OI construct against a live gamma regime. The tool's own
caveat reads **"Single-day OI snapshot. Max pain assumes settlement at each candidate strike with
current open interest unchanged to expiry"** `[STRUCT:max_pain]`. That 930 magnet exists because
MU's open interest was built when the stock was $900–1,200; it is a description of where the
chain *used* to be struck, not a force. Phase-4 states the priority directly — in a
`FULLY_NEGATIVE` regime gamma beats max-pain gravity, and at 13–15% distance the magnet has no
mechanism. MU is not even a pin candidate: **`pin-risk` returned 25 rows market-wide and zero for
MU**, and **`opex-concentration` returned 20 rows and zero for MU** `[OI:pin_risk]`
`[OI:opex_concentration]`.

On the vanna squeeze, I think he has the physics right and the fuel wrong. A vanna squeeze needs
implied vol to **fall**. But phase-5 measured **realised at 109.12% against implied at 96.04%**
`[HIST:vrp]` — the attacker cited this himself. **Implied vol is already below realised. There is
no compression premium left to release.** For his squeeze to fire, the market must reprice
implied vol *below* a realised vol that the last three sessions of -6.99%, -2.25% and -8.85% are
actively pushing higher. He is relying on the two bullish structural arguments simultaneously,
and they are mutually exclusive: **you cannot have both "vol is cheap, so buy premium" and
"vol will collapse and squeeze dealers."** Phase-5 flagged exactly this tension as an open
question, and he has not resolved it.

And his crowd argument runs my way, not his. **Analysts are 91.1% buy-or-better — 51 of 56, one
sell, zero strong sells — and coverage *grew* from 52 to 56 with not a single downgrade while the
stock fell 32%** `[SENT:recommendation]`. Retail is publicly anchored on a **"$1,000 rebound"**
with the stock at $820.53 `[SENT:company_news]`. Meanwhile insiders sold: **MSPR printed -100 in
November 2025, February, April and May 2026**, and the two largest sale months (-71,726 and
-89,601 shares) came immediately before the June peak `[FUND:MSPR]`. That is the classic
configuration — the sell side and the retail bid are long, the people who run the company and the
desks that move blocks are not.

## Strongest opposing point I cannot refute

The attacker's execution argument, which I will state in his terms: **"you cannot short the stock
with a sensible stop, because ATR is 83.13 — 10.1% of spot"**, and the `FULLY_NEGATIVE` regime
I rely on for my downside "is a regime that runs your stop before it pays you" `[HIST:atr fz]`
`[STRUCT:gex]`.

I cannot refute this and it is not a detail — it is the trade. My thesis says MU travels from 820
to the 750 shelf, roughly **-8.6%**. The daily average true range is **10.1%**, the front-expiry
implied move is **±7.90%** `[CTX:implied_move]`, and phase-0.5 documents recent sessions of
+12.17%, -8.02% and -8.85%. **The move I am forecasting is smaller than one day's noise.** Any
stop I can survive is wider than my target, which means my risk-reward is inverted before I
account for the FOMC binary landing tomorrow at 14:00 ET into a book with no gamma brake
`[MACRO:FOMC_2026-07-29]`. And I have to concede the compounding problem: phase-7b `VETO`s this
short on fundamentals, phase-7c returns `CAUTION`, phase-6's `market-regime` instructs **"Half
position sizes. Favor defined-risk strategies"** `[MACRO:MarketRegime_2026-07-28]`, and phase-8
produced **zero** agents willing to be long but also **two of four unwilling to be short**. Even
if I am right about direction, the position I am permitted to take is too small and too
wide-stopped to be worth the capital. **I am defending a view, not a trade.**

## Residual confidence
Residual confidence: 0.65

---

### Bear turn (attacking the SHORT)

The defender has just conceded the case. Not on direction — I will grant him direction, and I
have granted it twice — but on the only question that pays: **"I am defending a view, not a
trade."** That is the correct conclusion and it is mine, not his.

He is right that I over-reached on the vanna squeeze, and I withdraw it as an active thesis. His
point is exact: with **implied at 96.04% below realised at 109.12%** `[HIST:vrp]`, there is no
compression premium to release, and I cannot simultaneously argue that vol is too cheap to sell
and that it is about to collapse. I will keep only the weaker version — that a dovish FOMC
removes a specific event premium from the **151–152% front-week strikes**
`[STRUCT:iv_term_structure]` — and note that this is a two-day effect, not a thesis.

He is also right on scale: my put-writer is **0.021% of float against 1.41% of float in
dark-pool volume** `[OI:oi_pct_float fz]` `[DP:ticker_summary]`. I over-weighted them. What I
will not give up is what they signify. **They are the only participant in this entire nine-phase
deep dive who took a dated, capital-at-risk directional position**, they did it **six sessions
running**, and they **added into the decline** — +554 contracts on 7/23, +975 on 7/27, +416 on
7/28 `[OI:biggest_increases DUCKDB]`. Everyone else — the composite tools, the analysts, the
retail commentary — is expressing an opinion. Small and committed beats large and mechanical as
*information*, even when it loses on notional.

But the reason I win this exchange is simpler than any of that, and it is the defender's own
arithmetic. His target is the 750 shelf: **-8.6% from spot.** The daily ATR is **10.1%**
`[HIST:atr fz]`. The implied move is **±7.90%** `[CTX:implied_move]`. **His entire thesis fits
inside one average session of noise**, in a `FULLY_NEGATIVE` gamma regime that he correctly
identifies as amplifying moves *in both directions*, with a binary FOMC tomorrow at 14:00 ET, and
with **phase-7b explicitly `VETO`ing this exact trade** because revenue is compounding at
**+166.98%** with **4 of 4 beats**, a **72.57% gross margin** and **5.1% debt/equity**
`[FUND:*]`. He needs the cycle to roll; phase-6 documents DRAM in **shortage** with contract
prices **+93–98% QoQ** and CXMT's HBM3E **not shipping until 2027** `[MACRO:DRAM_pricing_Q1-2026]`.
He is short a compounding business, at the wrong instrument, with an inverted risk-reward, into a
binary, against a fundamental veto.

One last observation he cannot dismiss, because it is his own skill's record. **This exact
workflow ran MU on 2026-06-25, correctly identified the top at 1213.56, and still could not
convert it into a trade** — it proposed buying "the $1,134 absorbed shelf," which broke within
four sessions, with formal invalidation triggering on 2026-07-01 `[CTX:self_history]`. **Being
right about direction on MU and wrong about the level has already cost this desk once.** The
defender is now asking to do the mirror image: right about distribution, wrong about whether an
8.6% target is reachable through a 10.1% daily range.

## Strongest opposing point I cannot refute

Unchanged from round 1, and the defender sharpened it rather than weakening it: **the buy ratio
falls monotonically as price falls — 0.411 in the $790s, 0.419 in the $800s, 0.497 in the $820s**
— across every size tier, corroborated by an after-hours VWAP of **$809.02** and final prints at
**$780.00–789.00** `[DP:price_bins DUCKDB]` `[DP:extended_hours]`.

I cannot refute it, and his round-2 sharpening made it worse for me. He is correct that **writing
a 750 put eleven months out is not a bid for stock at 790**, and that my "structural bid" is
therefore not a bid at all — it is a limit order eight percent lower with a year of patience
attached. If MU opens lower tomorrow there is nothing in the observed data that steps in front of
it: no absorption gradient, no positive gamma until **870** `[STRUCT:today_gamma_flip]`, no
oversold reading (**RSI 40.29**), and no valuation floor within **61.28% of the 200-DMA**
`[HIST:rsi fz]`. My position is that you should not be *short*; it is emphatically **not** that
you should be long, and I have no evidence that would support one.

## Residual confidence
Residual confidence: 0.65

---

## Disconfirmation verdict

```
thesis_defender:  bull (SHORT)
bull_residual:    0.65
bear_residual:    0.65
disconfirmed:     true
strongest_bear_point: "The short's target (750 shelf, -8.6%) is smaller than one average daily
  range (ATR 83.13 = 10.1% of spot; implied move +/-7.90%), so any survivable stop is wider than
  the objective — an inverted risk-reward into a binary FOMC, against a phase-7b VETO grounded in
  +166.98% revenue growth and 4/4 earnings beats." [HIST:atr fz] [CTX:implied_move] [FUND:VETO]
```

**`disconfirmed = true`** because `bear_residual (0.65) >= bull_residual (0.65)`.

**Per `rubrics/sizing-rubric.md` §"Risk gates", phase-9 MUST down-shift the conviction bin by one
and cut one size step, quoting both residuals.** The debate is a gate, not an input — the
defender's 0.65 is **not** a reason to size up.

**What the debate settled:**
- **The distribution finding is real and unrefuted.** Both sides accept regular-hours mega
  `buy_ratio` 0.227 and the monotonic price gradient. Nothing in this run contradicts it.
- **The vanna-squeeze bull argument is withdrawn.** The attacker conceded it is incompatible with
  `vrp = -0.1308`. **Phase-9 should not carry a vanna-squeeze upside case**, only the narrower
  two-day event-premium release around the FOMC.
- **The put-writing campaign is real but small — 0.021% of float versus 1.41% on the
  distribution side.** It is *information*, not *support*. Phase-9 should treat 750–800 as a zone
  where a patient seller of puts exists, **not** as a defended floor.
- **The short is directionally supported and operationally unviable at this spot.** The
  defender's own closing concession — *"I am defending a view, not a trade"* — is the honest
  synthesis, and it converges with phase-8's risk-monitor, phase-7b's `VETO`, phase-7c's
  `CAUTION` and phase-6's "half position sizes."
- **Neither side produced a long case.** The attacker states explicitly: *"My position is that
  you should not be short; it is emphatically not that you should be long, and I have no evidence
  that would support one."*

**For phase-9's `key_risks` / invalidation** (per the phase contract, `strongest_bear_point` must
appear there): the inverted risk-reward — an 8.6% objective inside a 10.1% daily range — is the
binding constraint on any directional expression, and the FOMC at 2026-07-29 14:00 ET is the
dated trigger that resolves it in one direction or the other.
