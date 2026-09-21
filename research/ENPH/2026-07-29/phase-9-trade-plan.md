# Phase 9 — Trade Blueprint (PM voice)

**Ticker:** ENPH · **Sector:** Technology / Industry: Solar
**As-of date:** 2026-07-29 · **Spot reference: 35.07**
**Generated:** 2026-07-30T04:12:00Z
**Upstream phases cited:** all — `phase-0-intake.md` through `phase-8b-debate.md`

---

## The call

**Directionally short. Zero size today. This is a watch, not a position.**

I have five independent lanes telling me the same thing about direction and one telling me
loudly that I should not act on it here. The direction is bearish and I am comfortable saying so:
dealers are short gamma at **every strike from 25 through 36.5** with spot below the **36–37**
flip band [STRUCT:gex]; `net_dex` is **−$65,123,664 = 1.41% of float**, and the tool's own words
are *"dealer hedge is to SELL underlying"* [STRUCT:dex]; `total_gex` has now been negative for
**26 consecutive sessions**, over which ENPH fell **−24.7%** [HIST:gex_time_series]; the large
dark-pool tier printed `sell_ratio` **0.610** across 188 trades [DP:block_stratified]; and UW's own
composite returns **DIRECTIONAL_SHORT** with the explanation *"Dark pool selling + put buying —
institutional bear bet"* [INSIGHT:conviction_matrix]. The phase-8b thesis-attacker **conceded
direction outright in both rounds.**

**And I am still not putting size on, for four reasons that are each independently sufficient.**

**One — the crowd is already here and still filling up.** `Short Float` is **17.94% of float**
(~22.9M shares) and it **rose from 17.55%** through the print rather than covering
[SENT:short_float fz semi-monthly]. Seven brokers cut targets on 07-29 and **every one maintained
its rating**: mean **$43.07**, median **$45** — **+22.8% / +28.3% above spot** — with **zero
strongSell** across four months [SENT:company_news][SENT:recommendation]. Phase 7c returned
`tier_adjustment` **VETO**, and the rubric is unambiguous: a fresh directional short into a
heavily-shorted name is **watch-only / 0%**.

**Two — there is no survivable stop.** `ATR` is **3.24 — 9.2% of a 35.07 stock**
[HIST:rsi fz] — against a front-expiry implied move of only **5.58%** [CTX:implied_move]. My
invalidation sits at a close above **37**, which is **5.5% away — inside a single average day's
range.** Any stop tight enough to size normally gets taken out by path; any stop wide enough to
survive has already sized me down to a fraction. This is why I will not touch short stock.

**Three — nobody with size is pressing this.** `net_flow` is **−$479,813**, which is **5.8× below
the day's bearish top-50 cutoff** of −$2,762,256 [FLOW:insights_deep_dive]
[CTX:screener_bullish_bearish]. `signal-confluence` scores ENPH **3 of 6 — the minimum in a
500-name set, shared with 348 others** — and `conviction-matrix` puts `confidence_pct` at **24**
[INSIGHT:signal_confluence][INSIGHT:conviction_matrix]. Six separate conviction screens fail to
find ENPH at all. Worse for me, the *self-relative* measures that size cannot excuse say the same:
`total_premium` at the **26.6th percentile of its own 65 sessions** and `vol_x` **1.178 — on the
session after a binary event** [CTX:self_pctile DUCKDB].

**Four — the entry is the worst tick in the range and the desk was unanimous about it.**
`period_low` **34.96 was set today** and the close is **$0.11 above it**
[INSIGHT:price_vs_flow]; `RSI` **31.60**, price **−30.49% below SMA50** [HIST:rsi fz]. Five
specialist agents returned **zero LONG votes and not one conviction above 2** — the desk did not
fail to find a bull case, it found **no trade worth sizing** [AGENT:accumulation-hunter]
[AGENT:contrarian-scanner][AGENT:sweep-tracker][AGENT:earnings-scout][AGENT:risk-monitor].

**What would change my mind and put me in.** A **confirmed break and hold below 34.96** on volume
turns this from a watch into a trade — because *below* 34.96 there is nothing: phase 2 found **no
institutional dark-pool shelf beneath spot in the 5-day window**, the nearest genuine level being
**36.00, 2.7% above** [DP:price_levels]. Spot would be falling through a uniformly negative-gamma
field with dealers mechanically selling. **That is the trade. It is not available at 35.07.**

**One honest note on what this is not.** ENPH is not distressed. Current ratio **3.799**,
**$930.6M** of cash and securities, roughly net-cash-neutral, **$83.0M of free cash flow in a
single quarter** (~**7.2% annualized yield**), `Forward P/E` **15.82**
[FUND:financials_reported][FUND:peer_pe fz]. This is a multiple-compression and demand-erosion
thesis on a company that can fund a multi-year trough without a raise. Anyone framing it as a
solvency short is wrong.

---

## Levels

| Level | Price | Why it matters |
|---|---|---|
| **Resistance — primary** | **36.27** | **Triple convergence**: dark-pool **VWAP 36.27** [INSIGHT:institutional_accumulation] = the 36.15–36.30 distribution shelf ($9,246,618 / 38 trades) [DP:price_levels] = **36 max-pain** (08-07, +2.68%) [STRUCT:max_pain]. All five phase-8 agents named it independently. **Close is 3.3% BELOW it** — the marginal seller drove price under the level institutional size actually cleared. |
| **Gamma flip band** | **36 – 37** | `atm_flip_strike` **36** [STRUCT:today_gamma_flip]; observed `net_gex` sign change between 36.5 (−1,033) and 37 (+108,762) [STRUCT:gex]. Treat as ±2% (coarse on this liquidity). **Spot below it = short gamma.** |
| **Resistance — supply** | **37.48 – 38.25** | Trapped-buyer zone: **76,300 shares bought ABOVE mid at a $37.66 VWAP in the first 11 minutes**, now **−6.9%** [DP:largest]. Also brackets BMO's $37 target. |
| **Resistance — gap high** | **39.60** | Session high; the failed gap [FLOW:ohlc DUCKDB]. |
| **Support / trigger** | **34.96** | **30-day low, set today**; close $0.11 above [INSIGHT:price_vs_flow]. **An untested edge, NOT defended support** — no dark-pool cluster below spot [DP:price_levels]. Post-close probe to **34.90** [DP:extended_hours]. |
| **Objective** | **30.00** | `put_wall_support`, **22,446 puts** all-expiry / 2,963 at 08-21, `net_gex` **−471,049** [OI:oi_by_strike]. **Where the institutional money actually went** — the **$2,837,716 Jan-2028 P30** at 92% ask-side [OI:biggest_increases]. |

**Do not treat 35 as support.** `today-gamma-flip` tags the 35 strike a **`resistance_wall`** at
`gex` **−323,628**, alongside 36, 33 and 32; the only `support_wall` is 42.5 (+427,794), which is
**21% away and made of junk calls expiring Friday** [STRUCT:today_gamma_flip]. ENPH is **absent
from `pin-risk` top-25** — there is **no Friday pin** [OI:pin_risk].

---

## Entries

| Entry | Price | Trigger | Source |
|---|---|---|---|
| **Primary (the only one I'd act on)** | **34.90** | **Confirmed break and hold below 34.96** on above-average volume — a daily close beneath it, not an intraday wick. Below this there is no institutional shelf and dealer gamma amplifies. | [DP:price_levels][INSIGHT:price_vs_flow][STRUCT:gex] |
| **Fade / better price** | **36.27 – 36.50** | Rally into the dark-pool VWAP / 36–37 flip band that **fails**. Better risk-reward than chasing the low, and it is where supply sits. | [INSIGHT:institutional_accumulation][STRUCT:today_gamma_flip] |
| **Aggressive (not recommended)** | 35.07 | At-market today. **Explicitly discouraged** — bottom tick of a 30-day range, RSI 31.60, into a 7c VETO. | — |

**No entry is live today.** Both actionable entries are conditional. This blueprint's action is
**wait**.

---

## Sizing

```
signal_class:               bearish_flow
signal_backtest_win_rate:   1.00   (as reported by phase-5)
win_rate_n:                 9
win_rate_source:            backtest  →  OVERRIDDEN to conviction-bin fallback (see below)

conviction bin (pre-gate):  0.65
conviction bin (post-8b):   0.55        # gate 5 down-shifted one bin
p_raw:                      1.00
p (operative):              0.55
payoff_b:                   2.333       # (34.90 − 30.00) / (37.00 − 34.90) = 4.90 / 2.10
raw_kelly:                  0.3571      # (0.55 × 2.333 − 0.45) / 2.333
fraction:                   0.25
cap_pct:                    5.0
suggested (Kelly):          5.0%        # min(0.3571 × 0.25 × 100, 5.0) = min(8.93, 5.0)
sizing-map ceiling:          2.5%        # p 0.55 ∈ [0.50,0.70] → half of cap_pct
→ pre-gate size:            2.5%        # smaller of the two, per rubric §Step 3
final_size_pct:             0.0
deviation_reason:           null
```

**Why `p` is 0.55 and not 0.75.** Mechanically the rubric would take `p_raw` = the reported
`win_rate` **1.00**, then apply the `n < 10` cap of **0.75**. **I am not using that number**, and
both phase 5 and phase 8 told me not to. The backtest is unusable on four cumulative grounds:
the tool self-describes as *"In-sample backtest — not a robust live edge"*; **N = 9 is below the
spec's own 10-firing confidence floor**; the leaf is **market-wide and ENPH does not appear in the
9-signal sample** (TSLA, WOLF, AMD, GLD, MU, SNDK, SOXL, BE); and all nine signals originate on
**just two dates (07-24, 07-27)**, so they are ~2 correlated market events, not 9 observations
[HIST:signal_backtest]. `phase-8-agent-views.md`'s risk-monitor ruled on it directly: *"not a
usable Kelly p — phase 9 must discard it and size off the conviction bin, not the backtest"*
[AGENT:risk-monitor]. Calibration note: the 07-27 run recorded `p_raw` **0.556** on the **same**
`win_rate_n` of 9 — a 0.556 → 1.000 swing in two sessions at unchanged N is metric instability,
not an edge change. So I treat `win_rate_source` as effectively INSUFFICIENT_N, fall back to the
conviction bin per rubric Step 1, and the bin (0.55) sits below the 0.65 fallback cap.

**Gates, applied in order — every one either cut or was neutral, none added:**

| # | Gate | State | Effect |
|---|---|---|---|
| — | Pre-gate (Kelly ∧ sizing map) | p 0.55, b 2.333 | **2.5%** |
| 1 | **Fundamentals (7b)** | **CAUTION** — 1 contradiction (insider MSPR); earnings_trend and growth/margins both CONFIRM | cut one step: half → **starter ≈ 1.25%** |
| 2 | **Sentiment / crowded trade (7c)** | **VETO** — `crowd_state` CROWDED_SHORT, 17.94% and rising, analyst level +22.8% | **directional → 0.0%**, defined-risk carry only |
| 3 | Correlation cluster | **none** — ENPH is the only blueprint for 2026-07-29 | no-op *(advisory: ENPH/TAN ρ **0.846**, ENPH/SEDG 0.819, Beta 1.65–1.69 — this is a leveraged solar-beta bet, not an idiosyncratic one)* |
| 4 | **Adverse sector rotation (6)** | **adverse** — Technology `trend` INFLOW, `persistence_score` **1.0** (5/5) | cut half a step → already 0 |
| 5 | **Debate disconfirmation (8b)** | **`disconfirmed = true`** — `bear_residual` **0.75** ≥ `bull_residual` **0.65** | **bin 0.65 → 0.55** *(applied above)* + cut one step → already 0 |
| — | **Context modifier (0.5)** | **BUSY_NAME_NORMAL_DAY** | do not size at the top of the band |

**`final_size_pct = 0.0`. Directional exposure is watch-only.** Defined-risk structures below are
published **carry-only and sentiment-vetoed**, per the rubric's explicit allowance — they are the
"if I were forced to express this" answer, not a recommendation to open today.

> This is the second consecutive ENPH blueprint at **0.0%**, but for materially different reasons.
> The 07-27 run zeroed on fundamentals **VETO** + sentiment **VETO** + debate disconfirmed. Here
> fundamentals **improved to CAUTION** (the beat streak broke, so the earnings axis flipped from
> contradicting the bearish thesis to confirming it), and the zero now comes from **sentiment
> VETO + adverse rotation + debate disconfirmation**. The reasons rotated; the answer did not.

---

## Structures (defined-risk, carry-only, sentiment-vetoed)

All legs priced off **actual end-of-day NBBO** from
`bot-eod-report-2026-07-29.parquet` — bid/ask/mid/IV/delta are real, not modelled. **Mid-fill
assumed; worst-case fill shown.**

### A — PRIMARY: Aug-21 35/30 put debit spread

| | Buy P35 | Sell P30 |
|---|---|---|
| Bid / Ask | 2.55 / **2.87** | **0.80** / 0.90 |
| Mid | 2.71 | 0.85 |
| IV | 0.795 | 0.832 |
| Delta | −0.454 | −0.196 |
| Open interest | **4,031** | **2,963** |

- **Net debit: $1.86 (mid) · $2.07 (worst fill)** · width $5.00
- **Max loss = the debit** ($1.86) · **Max profit $3.14** · **reward:risk 1.69 : 1**
- **Breakeven $33.14** (−5.5% from spot — inside the ±5.58% front implied move)
- Net delta **−0.258** per spread · `dte` **23**

**Why this one.** Both legs sit on **real** OI walls (4,031 puts at 35; 2,963 at 30) so it is the
most liquid downside structure available. It **expires exactly at the 2026-08-21 OPEX cliff** —
`pct_of_total_oi` **15.69%**, 46,288 contracts, the one structural date inside the horizon
[OI:term_structure][MACRO:catalyst_calendar]. Its short strike is **30**, precisely where the
$2,837,716 Jan-2028 P30 buyer is aiming [OI:biggest_increases]. And critically, **it expires
BEFORE the 09-18 mechanical bid** that phase 8b identified — the 8,970 written Sept-18 P35 puts
(0.70% of float) that become assignment purchases at that expiry [OI:oi_by_strike]
[DEBATE:disconfirmation]. **A spread, not an outright put, because `vrp` is +0.1267** — `iv30d`
0.797 vs `realised_vol` 0.6703, `regime` **PREMIUM_SELLING** — so I want to be short some vol
against the long leg rather than pay 80% implied outright [HIST:vrp].

### B — ALTERNATIVE: Aug-21 37/40 bear call spread (credit)

| | Sell C37 | Buy C40 |
|---|---|---|
| Bid / Ask | **2.64** / 2.90 | 1.26 / **1.31** |
| Mid | 2.77 | 1.29 |
| Delta | 0.519 | 0.303 |
| Open interest | **49** ⚠ | 866 |

- **Net credit $1.33 (bid/ask) · $1.48 (mid)** · width $3.00
- **Max loss $1.67** (width − credit) · **reward:risk 0.80 : 1**
- **Breakeven $38.33** · net delta **−0.216** · `dte` 23

**Why consider it.** It **profits from nothing happening**, which is what the evidence actually
predicts: **no company catalyst until 2026-10-27** and a vol curve **flat at 82–87% beyond
`dte` 23** [INSIGHT:earnings_play][STRUCT:iv_term_structure]. It sells the **37** invalidation
level, and its **$38.33 breakeven sits above the entire 37.48–38.25 trapped-buyer supply zone**
[DP:largest]. With `vrp` **+0.1267** favouring premium sale, the credit side is the
better-aligned expression of a flat-to-lower view.
**⚠ Liquidity caveat: the C37 leg has only 49 open interest** and a 26-cent spread — assume
worse-than-mid fills and size accordingly. This is why it is the alternative, not the primary.

### C — NOT recommended, stated for completeness

- **Short stock: rejected.** `ATR` 3.24 = **9.2% of spot** vs a 5.58% front implied move — no
  survivable stop [HIST:rsi fz]. Both phase-8 bears refused it independently
  [AGENT:earnings-scout][AGENT:risk-monitor].
- **Outright long puts: rejected in favour of A.** `skew_ratio` **0.994** means downside carries
  no skew premium [STRUCT:term_skew] and the 10-16 expiry is the curve's cheapest vol at
  **82.2%** — but at **79 DTE** you pay ~2.6 months of theta on a thesis with no scheduled
  resolution, and `vrp` **+0.1267** says options are rich to realised. The Oct-16 35/30 spread
  prices at **$2.38 mid** for the same $5 width — a **1.10:1** reward:risk versus Aug-21's
  **1.69:1**. Aug-21 is strictly better.
- **Naked short premium: disallowed** at this skill's level.

---

## Invalidation

Per `rubrics/invalidation-rubric.md` — all three categories, concrete and falsifiable. Because
`final_size_pct` is 0, these are the conditions that either **activate** the thesis or **retire**
it.

### Price-based
**Thesis retired: two consecutive daily closes above 37.00.** That reclaims `atm_flip_strike` 36
and the observed 36.5→37 gamma sign change, flipping the dealer regime to long gamma and removing
the mechanical core of the case [STRUCT:gex][STRUCT:today_gamma_flip]. It also clears the 36.27
dark-pool VWAP and coincides with the 07-31 max-pain strike (37) and BMO's $37 target. Unanimous
across all five phase-8 agents.
**Secondary (also retires it): a close above 38.25** — reclaiming the trapped-buyer zone on volume
would mean that supply has been absorbed [DP:largest].
**Thesis ACTIVATED: a daily close below 34.96 on above-average volume** — below the 30-day low,
with no institutional shelf beneath and negative gamma through 32–36.

### Signal-based
Most diagnostic here, in priority order:
1. **`conviction-matrix` flips off DIRECTIONAL_SHORT** (to MIXED or HEDGED_LONG) on daily refresh
   [INSIGHT:conviction_matrix] — the composite that anchors this call.
2. **`total_gex` turns positive**, ending the 26-session negative run, or `atm_flip_strike` falls
   below spot [STRUCT:gex][HIST:gex_time_series].
3. **`institutional-accumulation` flips from DISTRIBUTION to accumulation**, or the large-tier
   `buy_ratio` rises above **0.55** (from 0.390) — auction-stripped
   [INSIGHT:institutional_accumulation][DP:block_stratified].
4. **Cumulative premium flow turns net positive for 3 consecutive sessions**
   [HIST:cumulative_premium_flow] — noting phase 5's warning that ENPH's big *bullish* prints have
   been put-**selling** and were **3-for-3 wrong**, so require three sessions, not one spike.

### Macro-based
**Highest-probability event in the next 30d: nonfarm payrolls, ~2026-08-07.** June printed
**+57k** against +129k prior [MACRO:PAYEMS_2026-06 FRED]; a second weak print is the most
plausible route to a dovish repricing, which would relieve the **`DGS10` 4.61% (+23bp/30d)** bear
steepener that is the most direct headwind to financed residential solar
[MACRO:DGS10_2026-07-28 FRED]. Secondary: **CPI ~2026-08-12** (core 2.81%, headline 3.73%).
**A dovish surprise on either retires the macro leg of this thesis.**
**Plus one non-price condition no single lane owns:** **a VIX reversal toward collapse re-arms the
vanna bid** (`net_vanna` **+1,327**), which is a thesis-killer independent of ENPH's price
[STRUCT:vanna_charm][MACRO:VIX_2026-07-29 UW][AGENT:risk-monitor].

### Exit on invalidation
**Hard stop** — both structures are defined-risk with max loss known at entry, so on any
price-based invalidation I close 100% rather than roll. Structure A's max loss is the $1.86 debit;
Structure B's is $1.67. **No tranching**, because `ATR` 3.24 means a partial exit at a level 5.5%
away is not meaningfully different from a full one within a single session's range.

---

## Catalyst calendar (next 30d)

**Front-expiry implied move: ±5.58% / ±$1.96** [CTX:implied_move] — down from **±12.25%**
pre-print. Every event below is read against that range, and both structures are sized to it.

| Date | Event | Likely impact | vs ±5.58% |
|---|---|---|---|
| **2026-07-31** | Front-week expiry (`dte` 2). 26,693 OI, but **11,177 of its 19,447 calls sit 21–57% OTM** and worthless; `today_total_gex` has **inverted to −406,622**; **no pin** (absent from `pin-risk`) | **Low** — removes almost no gamma near the money. **Do not expect expiry support at 35** | inside |
| 2026-08-01 | ISM Manufacturing PMI (July) | Low, indirect via rates | inside |
| **~2026-08-07** | **Nonfarm payrolls (July)** — June **+57k** vs +129k prior | **Medium-high** — the most plausible dovish trigger; **the macro invalidation** | inside unless a large miss |
| ~2026-08-12 | CPI (July) — core 2.81% / headline 3.73% | Medium — a hot print entrenches the hawkish 9–3 hold | inside |
| **2026-08-21** | **Monthly OPEX — the tradeable cliff.** `pct_of_total_oi` **15.69%** (46,288 contracts). Put-dominated near the money: **40 → 7,839 puts, 35 → 4,031, 30 → 2,963**. **Structure A expires here** | **High — the key structural date** | **exceeds** if 35 breaks (negative gamma 25→36.5) |
| ~2026-08-28 | PCE (July) — core 3.41% | Medium, indirect | inside |
| *2026-09-15/16* | Next FOMC (first chance to break a 5-meeting hold; SEP dot plot due) | High, **outside 30d** | — |
| *2026-09-18* | **The 8,970 written P35 puts become assignment purchases** — a mechanical bid, 0.70% of float. **Structure A deliberately expires before this** | Medium, **outside 30d** | — |
| *2026-10-27* | **ENPH Q3 earnings — the next company catalyst, ~13 weeks out** | High, **outside 30d** | — |

**The calendar's most important feature is the void.** No company-specific catalyst for ~13 weeks
is why `iv_rank` sits at ENPH's **15.6th self percentile**, why the curve is **flat at 82–87%
beyond `dte` 23**, and why a long-dated debit structure would be paying theta into silence. In the
interim ENPH trades as **solar-sector beta (ρ 0.846 to TAN) at 1.65× market beta**.

---

## Macro overlay

**Net: HEADWIND.** 13 headwinds (4 structural and already in force) vs 6 tailwinds, of which only
one is a live counterweight.

**Two datapoints phase 6 required me to carry:**
1. **VIX 20.66, +13.5% on the day and +23.5% over ten sessions** — this **invalidates phase 4's
   vanna-squeeze trigger** (*"if VIX collapses"*), leaving negative gamma and $65.1M of dealer
   selling as the **unopposed** mechanics [MACRO:VIX_2026-07-29 UW][STRUCT:vanna_charm].
2. **`DGS10` 4.61% (+23bp/30d) with the FOMC on a fifth consecutive hold at 3.50–3.75%, 9–3 with
   three hawkish dissents** [MACRO:DGS10_2026-07-28 FRED]
   [MACRO:FOMC_2026-07-29 WebSearch:federalreserve.gov]. Residential solar is a financed
   $20,000+ purchase; rising long rates plus the **sunset 30% ITC** is a compounding shock — and
   **ENPH itself guides −22%** US residential additions for 2026.

**The one genuine tailwind, stated fairly:** Technology sector flow is a **persistent INFLOW,
`persistence_score` 1.0** (5/5 sessions) — adverse to my short and applied as gate 4. Qualified:
it is **decaying 71%** (767M → 223M), mega-cap concentrated, contradicted by Technology price
**−2.49%** and **36.18%** market breadth, and **ENPH ranks 477th of 538** in that very sector
[MACRO:SectorFlowPersistence_2026-07-29 UW].

**Regime:** **TRANSITIONAL — *"Mixed signals, reduce position size, wait for clarity"***,
`trend` CHOPPY, `bullish_pct` **32.5%**, SPY below both 20d and 50d SMAs. The tool's own guidance
is *"Half position sizes. Favor defined-risk strategies."* [MACRO:MarketRegime_2026-07-29 UW]

---

## Key risks

1. **The 8,970 written Sept-18 P35 puts (0.70% of float) become a mechanical bid at the 09-18
   expiry.** Raised by accumulation-hunter as a squeeze that needs *no* accumulation, no good news
   and no fundamental change [AGENT:accumulation-hunter]. Resolved in phase 8b: delta-hedged short
   puts **sell** on the way down (now) and **buy** at assignment (September) — so the accelerant
   expires into a bid inside the horizon [DEBATE:disconfirmation]. **Structure A is chosen to
   expire before it.**
2. **Shorting into consensus upside on a crowded, growing short base.** 17.94% of float (~22.9M
   shares), **up from 17.55%**; seven targets averaging **$43.07** with every rating maintained and
   **zero strongSell**; and **borrow cost UNMEASURED** so the true carry and fragility of a short
   cannot be priced [SENT:short_float fz semi-monthly][SENT:company_news].
3. **No survivable stop:** `ATR` **3.24 = 9.2% of spot** exceeds the **5.58%** front implied move —
   the mechanical reason a share expression fails regardless of direction [HIST:rsi fz].
4. **Cost without catalyst.** Paying **80–85% implied** against **67% realised** (`vrp` **+0.1267**,
   `regime` PREMIUM_SELLING) on a flat curve with **no company catalyst for ~13 weeks**
   [HIST:vrp][STRUCT:iv_term_structure].
5. **This is a leveraged solar-beta bet, not an idiosyncratic one.** **ENPH/TAN ρ 0.846**,
   ENPH/SEDG 0.819, Beta **1.65–1.69** — any ENPH-specific thesis must clear the 0.846 hurdle
   [MACRO:PortfolioCorrelation_2026-07-29 UW].
6. **A VIX reversal alone rescues the bull case**, independent of ENPH news, by re-arming the
   +1,327 vanna bid [AGENT:risk-monitor].
7. **Oversold does not mean-revert in a short-gamma regime — cuts both ways.** RSI 31.60 is not a
   buy signal (the two deepest negative-GEX readings, 07-02 and 07-16, were each followed by
   further declines), *and* it warns against an over-tight short stop [HIST:gex_time_series]
   [DEBATE:disconfirmation].
8. **Two known blind spots:** borrow fee / HTB **not obtainable**, and the balance sheet is as of
   **2026-03-31 (~4 months stale)** — the Q2 10-Q post-dates the as-of date
   [FUND:financials_reported].

---

## Citations (the three datapoints this plan turns on)

- **[STRUCT:gex]** `net_gex` negative at **every strike 25→36.5** (40: −1,165,778 · 35: −977,948 ·
  30: −471,049); `atm_flip_strike` **36**; spot **35.07 below** the flip band → dealers sell into
  weakness with no dampening near the money. Corroborated by **26 consecutive** negative-`total_gex`
  sessions through a **−24.7%** decline [HIST:gex_time_series].
- **[SENT:short_float fz semi-monthly]** **17.94% of float short, UP from 17.55%** through the
  print — with seven analyst targets averaging **$43.07 (+22.8%)**, every rating maintained, zero
  strongSell → `tier_adjustment` **VETO**, the gate that zeroes directional size.
- **[DEBATE:disconfirmation]** `bear_residual` **0.75** ≥ `bull_residual` **0.65** →
  `disconfirmed = true` → conviction bin down-shifted **0.65 → 0.55** and one size step cut.
  `strongest_bear_point`: six conviction screens fail to find ENPH and `signal-confluence` scores
  it **3/6 — the minimum in a 500-name set, shared with 348 others** — while its own self-relative
  measures (`total_premium` **26.6th** self percentile, `vol_x` **1.178**) say almost no
  repositioning occurred the session after a binary event.

Supporting: **[DP:block_stratified]** large-tier `sell_ratio` **0.610** / 188 trades ·
**[INSIGHT:conviction_matrix]** **DIRECTIONAL_SHORT**, `confidence_pct` **24** ·
**[OI:biggest_increases]** **$2,837,716** Jan-2028 P30 at **92% ask-side**, opened pre-print ·
**[INSIGHT:institutional_accumulation]** close **3.3% below** the 36.27 dark-pool VWAP ·
**[FLOW:ask_bid_split DUCKDB]** whole-tape puts bought **1.569×**, calls **1.000** ·
**[SENT:company_news]** Q2 EPS **$0.46 IN LINE** after a published CORRECTION; six PT cuts, zero
raises · **[MACRO:VIX_2026-07-29 UW]** VIX **+23.5%/10d** kills the vanna trigger.

---

## Bottom line

**SHORT bias · conviction 0.55 · horizon 1-4w · size 0.0% · WATCH.**

The structure is bearish and I would rather be short ENPH than long it. But at **35.07** — the
bottom tick of a 30-day range, $0.11 off a low set today, with 17.94% of the float already short
and growing, a median Street target 28% higher, no survivable stop, six conviction screens finding
nothing, and two gates plus a lost debate all firing — **there is no trade here worth sizing.**

**I am watching two prices.** A daily close **below 34.96** on volume activates the short via
Structure A. Two daily closes **above 37.00** retire the thesis entirely. Between them I do
nothing, and I am comfortable with that: five specialist agents read the same nine files and
returned **zero LONG votes and not one conviction above 2**.

---

*For research and educational use only. Not financial advice. Sizing and structures are
illustrative.*
