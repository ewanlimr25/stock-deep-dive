# Phase 9 — Trade Blueprint

**Ticker:** SWKS
**As-of date:** 2026-07-31
**PM voice:** desk PM running an institutional book
**Spot reference:** **$62.28** (screener close, `phase-0.5-context.md`)
**Upstream phases cited:** phase-0.5 through phase-8b

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

SWKS is a **$60–65 box with a defended floor and no directional edge**: five
instruments across three data sources name the same two prices — `put_wall_support`
at **$60.00** (`net_oi` −625) and `call_wall_resistance` at **$65.00** (`net_oi`
+435, and the identical **max-pain strike for the 2026-08-21 expiry that holds
61.87% of tracked OI**) `[OI:oi_by_strike]` `[STRUCT:max_pain]` — while the only
opening position on the entire options board was **3,333 Aug-21 52.5 puts SOLD on
the bid at a vol/OI ratio of 3.52**, 1.1% above the 52-week low
`[FLOW:unusual_volume]`. Against that, there is **no measurable edge anywhere in
this blueprint** — the matching signal backtest returned `total_signals: 0` on two
runs (`win_rate_source: null`) `[HIST:signal_backtest]` — and the desk was
unanimous: **five specialist agents returned 0 LONG, 0 SHORT and an average
conviction of 2.0/5** `[AGENT:all]`. **The honest recommendation is NO TRADE at
spot**; raw Kelly is **negative (−0.085)** entering at $62.28 and only turns
positive at a tag of $60.00, so everything below is conditional on that entry.

## Bias + conviction + horizon

- **Directional bias:** **NEUTRAL** (plurality of phases 1–8: 3× NEUTRAL / 2× RANGE
  / 0× LONG / 0× SHORT). The tradeable sub-form is **RANGE**, bounded $60–65.
- **Conviction (M-01 bin):** **0.55**
- **Time horizon:** **1–4 weeks** (unanimous across all five phase-8 agents; aligns
  with the 2026-08-21 OPEX at 21 DTE and sits entirely before the 2026-10-27
  earnings print)
- **Why this bin:** the base evidence supports at most 0.65 (moderate edge with real
  disconfirming evidence), and `phase-8b-debate.md` returned
  **`disconfirmed: true` (bear 0.65 ≥ bull 0.55)**, which mandates a one-bin
  down-shift ⇒ **0.55**. Phase 10 will score confluence independently; if its band
  disagrees, phase 10 flags it.

## Entry zones

| Entry type | Price | Trigger condition | Source |
|---|---|---|---|
| **Primary** | **$60.00** | Tag of the ≤30-DTE `put_wall_support` (1,139 puts vs 514 calls) inside the dark-pool shelf $60.25–61.22 (~277,000 shares across three blocks), **then a daily close back above $60.25** | `[OI:oi_by_strike]` + `[DP:price_levels]` |
| **Aggressive** | **$58.44–59.34** | Tap of the 2026-07-29 accumulation shelf — **176,487 shares / $10,373,555 in twelve blocks**, 67,200 of them printed **pre-market before 08:38 ET** | `[DP:accumulation_shelf DUCKDB]` |
| **Fade** | **$64.68–65.00** | Rejection at the stacked supply wall: **607,453 shares / $39,290,060** at the 2026-07-28 pre-earnings close of $64.68, immediately beneath the $65.00 call wall and max-pain strike. Counter-trade the box top. | `[DP:price_levels]` + `[STRUCT:max_pain]` |

**Do not chase at $62.28.** At spot the payoff ratio to the $65.00 target against
the $58.44 stop is **b = 0.708**, which makes raw Kelly **negative** (see Sizing).
The primary entry exists precisely because it is the only price at which the
geometry works.

## Levels to watch

| Type | Level | Source |
|---|---|---|
| **Support** | **$60.00** | `[OI:oi_by_strike]` `put_wall_support`, `net_oi` −625, `distance_pct` −3.78 — confirmed by `[DP:price_levels]` shelf $60.25–61.22 |
| **Deep support** | **$58.44–59.34** | `[DP:accumulation_shelf DUCKDB]` — 176,487 sh / $10.37M, all 2026-07-29 |
| **Floor (flow-anchored)** | **$52.50** | `[FLOW:unusual_volume]` — 3,333 puts sold, vol/OI 3.52; 1.1% above the 52-week low of $51.93 |
| **Resistance** | **$65.00** | `[OI:oi_by_strike]` `call_wall_resistance`, `net_oi` +435, `distance_pct` +4.23 |
| **Supply wall** | **$64.68** | `[DP:price_levels]` — 607,453 sh / $39,290,060, the largest 5-day level; 2026-07-28 pre-earnings close |
| **Gamma flip** | **$62.50** | `[STRUCT:today_gamma_flip]` `atm_flip_strike` = 62.5, which is also the per-strike GEX **minimum** (−448,437) `[STRUCT:gex]` |
| **Largest pin** | **$65.00** | `[STRUCT:max_pain]` — 2026-08-21, `distance_pct` +4.23, `holder_value_at_max_pain` $603,250 |

**⚠ The reported `zero_gamma_level` of 77.61 is explicitly NOT a level and must not
be used.** `phase-4-structure.md` disqualified it: the positive-gamma mass creating
it is the **11,927-contract legacy Aug-21 80 call trading at a $0.24 last fill with
OI flat since 2026-07-14**. Use the **$62.50 sign-flip**.

**Price-context colour (advisory, `[HIST:52w_proximity]`):** spot sits at **26.5%
of the 52-week range** ($51.93–$90.90), **−31.5% from the high** and **+19.9% off
the low**, after a **−14.03% month** (72.45 → 62.28). This is a **washout, not a
breakout** — there is no chase risk on the long side. The `fz` RSI/SMA cross-check
was **unavailable** (all fields null, `phase-5-historical.md`), so no momentum
overlay is available to confirm or temper this. **Narrative colour only; it does not
touch the Kelly `p` or the size.**

## Invalidation

Per `rubrics/invalidation-rubric.md`, all three categories, each falsifiable:

- **Price-based (two-sided):**
  - **Downside — two consecutive daily closes below $58.44.** That is the base of
    the 2026-07-29 accumulation shelf; below it the institutions who took
    **+573,766 net shares** across 07-29/30 `[DP:net_imbalance DUCKDB]` are
    underwater and the entire floor thesis is dead. **Thesis void, not reduced.**
  - **Upside — one daily close above $65.70.** Clears the stacked $64.68 supply
    wall and the $65.00 call wall/max-pain magnet together; the RANGE read is wrong
    and the box has broken up.
- **Signal-based:**
  - **Dark-pool regime flip:** the phase-2 cleaned metric (regular-session,
    directional-only, VWAP and `prior_reference_price` prints excluded) printing a
    **buy ratio below 0.45 on two consecutive sessions with >300,000 directional
    shares**. That reverses the single most constructive finding in the run.
  - **The floor never formed:** the **2026-08-03 OI file failing to show a material
    rise in Aug-21 52.5-strike put open interest** from its current 947. The OI
    dataset is **lagged one session** (`last_date` 2026-07-30 / `curr_date`
    2026-07-31), so the 3,333 contracts traded on the as-of day are **unconfirmed as
    open interest** `[OI:lag DUCKDB]`. If they were intraday-offset, the
    "flow-anchored $52.50 floor" was never real and every level below $58.44 loses
    its options anchor.
- **Macro-based:**
  - **Any China SAMR ruling on the Qorvo combination, in either direction.**
    `[MACRO:SWKS_QRVO_merger_2026-07-28]` — the review is in **Phase III (final)**
    and is the only event that can exceed the **±9.10%** front-expiry implied move.
    **The thesis is void on the headline, not on the price.** Close on the news.
  - Secondary: a hot CPI print driving **DGS10 through ~4.85%** (from 4.68%, already
    **+24bp month-over-month**) `[MACRO:DGS10_2026-07-30 FRED]` — it compresses a
    34.3× P/E sector and directly raises the cost of the **~$2B debt raise** SWKS is
    executing.

## Sizing (% of risk, NOT dollars)

**Kelly `p`:**
- `phase-5-historical.md` §Verdict handoff: **`signal_backtest_win_rate: null`,
  `win_rate_n: 0`, `win_rate_source: null`** — the `dark_pool_accumulation` backtest
  returned `{"note":"no backtest results","total_signals":0}` on **two** runs
  `[HIST:signal_backtest]`.
- ⇒ **Fall back to the conviction bin.** `p_raw = 0.55` (the M-01 bin). The
  fallback is itself capped at **0.65**, so **`p = min(0.55, 0.65) = 0.55`**.
- *(The populated market-wide classes were rejected as `p`: `bullish_flow`
  win_rate 100.0% on **n = 9** with SWKS **absent from the sample** — SNDK/SPY/
  ASML/GOOGL/MSFT/QQQ/NBIS/NDX — and the tool self-labels "In-sample backtest — not
  a robust live edge.")*

**Kelly inputs and the entry-dependence that decides this trade:**

| Entry | `b` = \|target − entry\| / \|entry − stop\| | `raw_kelly` = (p·b − (1−p))/b |
|---|---|---|
| **At spot $62.28** | (65.00 − 62.28)/(62.28 − 58.44) = **0.708** | **−0.0853 ← NEGATIVE** |
| **At primary $60.00** | (65.00 − 60.00)/(60.00 − 58.44) = **3.205** | **+0.4096** |

**Per `rubrics/sizing-rubric.md`: `raw_kelly < 0` ⇒ the directional action MUST be
NEUTRAL or the opposite side.** At spot there is no trade — that is the arithmetic,
not an opinion, and it is why the bias is NEUTRAL. All sizing below is computed off
the **primary $60.00 entry only** and is void at any other entry.

- **Raw Kelly (primary entry): 0.4096** · fraction **0.25** · cap_pct **5.0**
- `suggested_size_pct = min(0.4096 × 0.25 × 100, 5.0) = min(10.24, 5.0) =` **5.00%**
- **Win-rate map ceiling:** `p = 0.55` falls in the **0.50–0.70** band ⇒ **half**
  ⇒ ceiling **2.50%**. Take the smaller ⇒ **2.50%**.

**Risk gates — all five listed, fired or not:**

| # | Gate | Reading | Effect | Running size |
|---|---|---|---|---|
| 1 | **Fundamentals (7b)** | **`CAUTION`**, `contradiction_count: 1` (growth/margins: `epsGrowthTTMYoy` −6.00% on `revenueGrowthTTMYoy` +2.33%) | **FIRED** — cut one step | 2.50% → **1.25%** |
| 2 | **Sentiment / crowd (7c)** | **`CAUTION`**, `crowd_state: CROWDED_SHORT` (adverse revisions: **7 of 8 firms cut targets 2026-07-29**) | **FIRED** — cut one step | 1.25% → **0.63%** |
| 3 | **Correlation cluster** | `SWKS/FSLR = 0.518` — below the 0.60 soft-watch and 0.70 cluster thresholds | **not fired** — no-op | **0.63%** |
| 4 | **Sector rotation (6)** | **`ADVERSE`** — Technology aggressor-adjusted **−$187,715,752**, largest outflow of 11 sectors; RF/analog cohort −$12.51M, negative 4 of 5 sessions | **FIRED** — cut half a step (×0.75) | 0.63% → **0.47%** |
| 5 | **Debate (8b)** | **`disconfirmed: true`** — bull_residual **0.55** vs bear_residual **0.65** | **FIRED** — bin 0.65→0.55 *(already applied)* + cut one step | 0.47% → **0.23%** |

**Context modifier (phase-0.5):** `unusual_verdict = **QUIET**` — total premium
**$877,883**, option volume **1.00×** its own 30-day average, rank **565/4,499** on
net direction. **QUIET caps directional size at starter regardless of Kelly.**
0.23% is already at or below starter, so no further cut is applied.

- **Final size: 0.25% of book risk** (rounded from 0.234%; expressed as **max loss
  on the chosen structure ≤ 0.25% of book risk**).
- **Deviation reason:** none. **An upward deviation is forbidden here** — four of
  five gates fired and the context verdict is `QUIET`.

**PM read on that number.** 0.25% of book risk after a 5.00% raw Kelly is a **95%
haircut**, and it is the correct answer. At that size the position does not move the
book and does not repay the operational attention. **Treat this blueprint as
WATCH-ONLY with a defined trigger at $60.00.** The structures below exist so that
the desk has a pre-agreed expression if the trigger prints — not because the trade
should be initiated today.

## Option structures

**Expected-move budget (N4):** front-expiry `implied_move` **$5.6749**,
`implied_move_perc` **9.098%** `[CTX:implied_move]` ⇒ a one-move band of
**$56.61 – $67.95**. Every structure below is checked against it.

### Directional (primary)

- **Structure:** **Call debit spread**
- **Strikes / expiry:** **Long 60 call / short 65 call, 2026-08-21 (21 DTE)**
- **Debit:** **$2.60** (mid-to-mid $2.49; paying the ask and hitting the bid
  $2.80 — 60C NBBO 4.60/4.96, 65C NBBO 2.16/2.42, all 2026-07-31 quotes)
- **Breakeven:** **$62.60** (+0.51% from spot)
- **Max loss:** **$2.60** (at or below $60.00)
- **Max gain:** **$2.40** (at or above $65.00) — payoff **0.92 : 1**
- **Why this structure:** both legs sit on **observed** OI (60C = 514, 65C = 874),
  and the strikes are not chosen by eye — **$60.00 is phase-3's `put_wall_support`
  and $65.00 is simultaneously `call_wall_resistance`, phase-4's max-pain strike,
  and the level where the desk observed a Sep-18 62.5/65 credit call spread being
  sold** `[OI:oi_by_strike]` `[STRUCT:max_pain]` `[FLOW:top_premium_trades]`.
  IV is **57.6% at the 65 strike** against an IV rank of 52.9 that is only the
  **29.9th percentile of SWKS's own history** — you are not overpaying for vol, but
  `phase-5-historical.md` showed trailing-10-session realized (55.53%) is **at**
  implied (55.90%), so there is **no vol edge in either direction**.
- **N4 check:** target $65.00 = **+4.37% = 0.48× the priced move** — comfortably
  inside, so the target is **not rich**. ⚠ **But the $5.00 spread width is narrower
  than the $5.67 expected move** — the rubric's explicit caution. That is
  **deliberate**: $64.68–65.00 is a genuine stacked wall (607,453 shares of trapped
  supply plus the call wall), so capping there is intentional. The cost is real —
  **this structure cannot benefit from a SAMR-driven gap** and will be capped while
  the underlying runs past it.
- **Honest weakness:** the payoff is **sub-1:1**. Entered at spot it is a losing
  proposition (raw Kelly −0.085). It only works from the $60.00 trigger, where the
  same spread would cost materially less and the geometry inverts.

### Defined-risk alternative

- **Structure:** **Put credit spread**
- **Strikes / expiry:** **Short 55 put / long 50 put, 2026-08-21 (21 DTE)**
- **Credit:** **$0.43** (55P bid 0.89, 50P ask 0.46 — 2026-07-31 quotes)
- **Breakeven:** **$54.57**
- **Max loss:** **$4.57** (width $5.00 − credit $0.43), at or below $50.00
- **Why this structure:** it sells the zone **directly beneath phase-2's
  $58.44–59.34 accumulation shelf and directly above phase-1's $52.50
  flow-anchored floor** — the same directional side as the only opening position on
  the board, but with **defined** risk. The block seller took undefined risk at
  $52.50; this does not. Both legs have observed OI (55P = 686, 50P = 1,307).
- **N4 check — PASSES.** The short strike at **$55.00 is −11.7% from spot**, below
  the **$56.61** one-expected-move floor. A single expected-move gap does **not**
  breach the short strike. ✓
- **Honest weakness:** **$0.43 of credit against $4.57 of risk is a 9.4% return on
  risk for 21 days.** That is thin compensation, and the thinness is itself
  evidence: **the market is not paying you to underwrite this floor.** A SAMR
  headline can gap straight through both strikes, in which case max loss is realised
  in one print — sized within the 0.25% cap, but realised.

### ✗ Rejected structure — the desk's own highest-conviction proposal

`phase-8-agent-views.md`'s `earnings-scout` (the only agent above conviction 2)
proposed **buying the Sep-18 straddle at the 57.2% curve trough**. Priced on
2026-07-31 quotes: **Sep-18 62.5 call ask $5.24 + 62.5 put ask $5.20 = $10.44
debit**, breakevens **$52.06 / $72.94** — a required move of **±16.76%**, which is
**1.84× the front-expiry priced move**. `rubrics/sizing-rubric.md`'s N4 guidance
treats a target beyond **~1.5×** the priced move as rich. **Rejected on the
rubric's own arithmetic**, and independently by `phase-8b-debate.md`, where the
defender conceded that ten-session realized vol (55.53%) sits **at** implied
(55.90%) so the "cheap vol" premise does not hold, and that the SAMR catalyst's
timing is **undated with formal guidance of early calendar 2027** — i.e. 49 days of
theta on a bet that an unscheduled ruling lands inside the expiry.

*(A short-put risk reversal — selling the 52.5 put alongside a long 65 call — was
also considered and **ruled out**: `rubrics/sizing-rubric.md` disallows naked short
premium at this skill's level.)*

## Macro overlay (cite phase-6)

**Tailwinds:**
- **$2B buyback authorised** alongside the dividend elimination — a partial,
  price-sensitive offset to the arb supply `[MACRO:SWKS_QRVO_merger_2026-07-28]`
- **Broad dollar −0.6% month-over-month** (120.71 from 121.41) — SWKS books the
  large majority of revenue overseas `[MACRO:DTWEXBGS_2026-07-24 FRED]`
- **Payrolls decelerating to +57k** (from +129k) — caps the hawkish-dissent hike
  risk without signalling a break `[MACRO:PAYEMS_2026-06 FRED]`
- **Q3 beat both lines** — revenue $935M and non-GAAP EPS $1.08 vs a $1.03 guided
  midpoint `[MACRO:SWKS_Q3FY26_2026-07-28]`
- **Semis are cheap on growth-adjusted multiples** — industry PEG **0.56**, and the
  group closed **+0.25%** while being net-sold `[MACRO:group_valuation fz EOD]`

**Headwinds:**
- **Dividend ELIMINATED** — a **4.56% TTM yield at a 91.35% payout**, consuming
  69.5% of half-year FCF. The income holder base is now a **price-insensitive,
  mandate-driven seller**, and syndicated screens were **still listing SWKS as a
  high-yield tech name on 2026-07-30**
  `[MACRO:SWKS_dividend_elimination_2026-07-28]`
- **~$2B debt raise** (Goldman bridge commitment up to $3.05B) turns ~$417M net
  cash into ~$1.6B net debt, D/E 0.17 → ~0.52, into a rising long end
  `[MACRO:SWKS_QRVO_merger_2026-07-28]`
- **Market regime `TRANSITIONAL`**, breadth **34.1% bullish** (2,142 of 6,280),
  engine guidance verbatim *"Half position sizes. Favor defined-risk strategies."*
  `[MACRO:MarketRegime_2026-07-31 UW]`
- **Technology was the largest net-SOLD sector of eleven, −$187,715,752**
  aggressor-adjusted `[MACRO:MarketRegime_2026-07-31 UW]`
- **FOMC held 3.50–3.75% on a 9–3 vote with all three dissenters wanting a HIKE**;
  core PCE **+3.29% YoY** `[MACRO:FOMC_2026-07-29 WebSearch:federalreserve.gov]`
  `[MACRO:PCEPILFE_2026-06 FRED]`
- **10-year at 4.68%, +24bp month-over-month** — multiple compression *and* a direct
  increase in the deal's financing cost `[MACRO:DGS10_2026-07-30 FRED]`
- **Conference Board Present Situation 114.9, third consecutive monthly decline** —
  handset demand is labour-sensitive `[MACRO:ConfBoard_2026-07-28 WebSearch:advisorperspectives.com]`

**Net: HEADWIND.** Eight headwinds (two severe and company-specific) against five
tailwinds (one material). `phase-6-macro.md` conviction **4/5**.

## Catalyst calendar (next 30d)

Front-expiry implied move **±9.10% / ±$5.67** ⇒ band **$56.61 – $67.95**.

| Date | Event | Impact direction | vs expected move |
|---|---|---|---|
| **2026-08-03** (Mon) | ISM Manufacturing PMI (July) — 1st business day | ? | Inside |
| **2026-08-05** (Wed) | ISM Services PMI (July) — 3rd business day | ? | Inside |
| ~**2026-08-07** *(date not independently verified)* | July employment report | ? | Inside |
| ~**mid-August** *(date not independently verified)* | July CPI | − if hot | Inside unless a large upside surprise |
| **UNDATED — any day** | **★ China SAMR Phase III decision on the Qorvo merger** | **? BINARY, two-sided** | **★ CAN EXCEED ±9.10% — the only event that can** |
| **UNDATED — "near term"** | ~$2B debt raise pricing | − | Inside, re-rate risk |
| **2026-08-21** (Fri) | **OPEX** — 61.87% of tracked OI; max pain **$65.00** | + toward $65 (weak) | Well inside |
| 2026-09-16/17 *(outside 30d)* | FOMC — end-2026 dots span 3.6–4.1% | ? | — |
| 2026-10-27 *(outside 30d)* | **SWKS FQ4 earnings — verified, not stale** | — | **No earnings risk inside the horizon** |

## Post-trade monitoring checklist

- [ ] **Daily — SAMR headline watch.** Any ruling on the Qorvo combination voids the
      thesis **on the headline, not on the price**. Close, do not wait for a level.
- [ ] **Daily — phase-2 dark-pool method, cleaned.** Recompute the regular-session
      directional buy ratio with `average_price_trade` / `prior_reference_price`
      prints and the 16:00 auction cluster **excluded**. Two consecutive sessions
      below **0.45** on >300k directional shares = signal invalidation. *(Raw
      `block-stratified` ratios are NOT a substitute — they read 0.395/0.478 on the
      as-of day versus 0.461 cleaned.)*
- [ ] **2026-08-03 — check the Aug-21 52.5-strike put OI.** The OI dataset is lagged
      one session, so the 3,333 contracts sold on 2026-07-31 are **unconfirmed**.
      If OI has not risen materially from **947**, the $52.50 flow-anchored floor
      never formed and every level below $58.44 loses its options anchor.
- [ ] **Daily — gamma pivot at $62.50.** Watch `gex` `per_strike`: the −448,437
      minimum at 62.5 means moves off that strike are **amplified**. A shift of the
      minimum away from spot would mean the amplification risk has moved.
- [ ] **Weekly — short interest.** The 21.93% figure is the **semi-monthly exchange
      settlement, ~2 weeks lagged**, and predates the print, the dividend cut and
      the SAMR disclosure. A **fall** would signal arbs unwinding ahead of a ruling.
- [ ] **On each analyst action — track the $66.00/$67.50 anchor.** Eight firms
      re-marked on 2026-07-29; a **rating** change (not just a target cut) from any
      of the 16 Holds is the first sign the consensus is moving off the fence.
- [ ] **Do not initiate at spot.** The trigger is **$60.00 with a close back above
      $60.25**. At $62.28 raw Kelly is negative.

## Conviction deviation

None. Conviction is set at **0.55**, the floor of the M-01 bin set, after the
mandatory one-bin down-shift from `phase-8b-debate.md`'s `disconfirmed: true`.
No upward deviation is claimed, and none would be permitted — **four of the five
risk gates fired** and phase-0.5's context verdict is **`QUIET`**.

## Citations summary

Minimum 3 distinct upstream datapoints (M-04). Spot-checkable by phase 10:

1. **`[OI:oi_by_strike]` — `put_wall_support` $60.00 (`net_oi` −625, 1,139 puts vs
   514 calls, `distance_pct` −3.78) and `call_wall_resistance` $65.00 (`net_oi`
   +435, 874 calls vs 439 puts, `distance_pct` +4.23), ≤30 DTE** —
   `phase-3-positioning.md` §OI walls by strike. *(phases 1–4)*
2. **`[FLOW:unusual_volume]` — Aug-21 52.5 put, `total_volume` 3,333 vs
   `open_interest` 947, `vol_oi_ratio` **3.5195**, `total_premium` $219,979, sold on
   the bid** — `phase-1-flow.md` §New positioning. *(phases 1–4)*
3. **`[HIST:signal_backtest]` — `dark_pool_accumulation` returned
   `{"note":"no backtest results","total_signals":0}` on two runs ⇒
   `win_rate_source: null`, `win_rate_n: 0`** — `phase-5-historical.md` §Signal
   backtest. *(phases 5–7)*
4. **`[STRUCT:max_pain]` — 2026-08-21 `max_pain_strike` **65**, `distance_pct`
   4.23, `holder_value_at_max_pain` $603,250, on the expiry holding **61.87%** of
   tracked OI** — `phase-4-structure.md` §Max pain. *(phases 1–4)*
5. **`[MACRO:MarketRegime_2026-07-31 UW]` — regime `TRANSITIONAL`,
   `bullish_pct` 34.1, `trading_guidance` "Half position sizes. Favor defined-risk
   strategies."; Technology `sector_rotation` **−$187,715,752**, largest outflow of
   11** — `phase-6-macro.md` §Market regime, §Sector rotation. *(phase 6)*
6. **`[AGENT:all]` — five specialist agents returned 3× NEUTRAL / 2× RANGE,
   **0 LONG, 0 SHORT**, average conviction **2.0/5**, unanimous on support $60.00 /
   resistance $65.00** — `phase-8-agent-views.md` §Agent verdicts table. *(phase 8)*
7. **`[DEBATE:residuals]` — bull_residual **0.55** vs bear_residual **0.65** ⇒
   `disconfirmed: true`** — `phase-8b-debate.md` §Disconfirmation verdict.
