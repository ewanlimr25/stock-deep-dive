# Phase 9 — Trade Blueprint

**Ticker:** ENPH
**As-of date:** 2026-07-27
**PM voice:** desk PM running an institutional book
**Spot reference:** **$38.01** (`close`, `stock-screener-2026-07-27.parquet`; `phase-0.5-context.md`)
**Upstream phases cited:** phase-0.5 through phase-8b

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

ENPH goes into tomorrow's post-close print with a **bearish but trivially-sized
tape** — `net_flow = −$258,731` on a $4.84B company [FLOW:insights_deep_dive],
a 5-of-5 bearish sweep campaign worth just $1,335,255 [FLOW:sweep_persistence] —
sitting on top of a **structurally armed upside squeeze**: `net_dex = −$40.3M`
(0.83% of float) with `net_vanna = +913` [STRUCT:vanna_charm], short interest
**rising** to 17.55% of float [SENT:short_interest], and a **flat 25Δ skew**
(`skew_ratio = 1.001`, "COMPLACENT") [STRUCT:term_skew] — the exact configuration
that produced **+39%** on 2026-02-04 [AGENT:earnings-scout]. Both downside gates
fired independently — 7b `VETO` on a 4/4 beat rate into a −11.76pp gross-margin
collapse [FUND:earnings_surprises], 7c `VETO` on a crowded, rising short base —
and the 8b debate then broke the long-vol expression as well
(`bear_residual 0.65 ≥ bull_residual 0.65`) [DEBATE:disconfirmation]. **The honest
call is no directional position into the event**: a ±12.25% implied move
[CTX:implied_move_pct] over a surface with `zero_gamma_level = null`
[STRUCT:gex] and no pin means any pre-print stop is taken out by path, not by
being wrong [AGENT:risk-monitor].

## Bias + conviction + horizon

- **Directional bias:** **NEUTRAL** (plurality of phases 1–8: 4× NEUTRAL, 1× LONG,
  **0× SHORT** — every phase from 1–7 carried a bearish lean and the desk declined
  to express it)
- **Conviction (M-01 bin):** **0.55**
- **Time horizon:** **1-4w** (structures target the 2026-08-21 expiry, 25 DTE —
  past both binaries)
- **Why this bin:** the lowest bin is forced from three directions — phase-0.5
  `unusual_verdict = BUSY_NAME_NORMAL_DAY` with today's option volume at the
  **16.4th self-percentile** [CTX:self_pctile], **two independent `VETO` gates**
  (7b, 7c), and an **8b debate that disconfirmed** the surviving expression.
  Phase-10 should score this in the low band; if it scores higher, the gates still
  bind size.

## Entry zones

**All entries are CONDITIONAL and post-event. Nothing is entered before the
2026-07-28 postmarket print.**

| Entry type | Price | Trigger condition | Source |
|---|---|---|---|
| **Primary** | **$40.00** | Post-FOMC (after 2026-07-29 14:00 ET) daily **close above $40.00** — the modal max-pain magnet (8 of 15 expiries) and SMA200 ≈ $40.01 — with `call_ask_share > 0.50` confirming real demand | [STRUCT:max_pain], [HIST:sma200 fz], [FLOW:screener_ask_bid DUCKDB] |
| **Aggressive** | **$36.21 – $36.70** | Post-event flush into the dark-pool shelf that **holds** — $36.70 is the most-transacted DP level (9 trades, $2.48M) and $36.21 the 30-day low; requires a reclaim close, not just a tag | [DP:price_levels], [INSIGHT:price_vs_flow] |
| **Fade** | **$42.50** | Rejection at the six-method wall — counter-trade the squeeze if it exhausts there. This is plan B **only** if the primary long-side read plays out and stalls | [OI:oi_by_strike], [STRUCT:today_gamma_flip] |

## Levels to watch

| Type | Level | Source |
|---|---|---|
| **Support** | **$35.00** | `put_wall_support`, 4,217 puts vs **10** calls ≤30DTE (23,133 all-expiry); `net_gex −502,635` [OI:oi_by_strike], [STRUCT:gex] |
| Support (secondary) | **$36.21 – $36.70** | 30-day low $36.21 [INSIGHT:price_vs_flow]; most-transacted DP level $36.70, 9 trades [DP:price_levels] |
| **Resistance** | **$42.50** | **Six-method confluence**: only genuine near-term call wall (3,735 calls / **0** puts) [OI:oi_by_strike] + largest positive gamma **+703,006** [STRUCT:today_gamma_flip] + SMA20 ≈ $42.76 [HIST:sma20 fz] + **$42.00** median analyst target [FUND:targets] + vanna-squeeze ceiling [STRUCT:vanna_charm] + 4-of-5 agent consensus [AGENT:*] |
| Resistance (nearer) | **$40.00 – $40.67** | Modal max-pain strike, 8 of 15 expiries [STRUCT:max_pain]; DP supply cluster $40.55–40.67, 5 trades [DP:price_levels] |
| **Gamma flip** | **NONE — `zero_gamma_level = null`** | `regime = "FULLY_NEGATIVE"`, all 50 strikes negative; there is **no long-gamma zone within 45 DTE** [STRUCT:gex]. The only positive-gamma pocket is the 2026-07-31 expiry (`today_total_gex +1,047,168`, `today_zero_gamma 42.21`) and **it expires in 4 days** [STRUCT:today_gamma_flip] |
| **Largest pin / max pain** | **$41.00** (2026-07-31, +7.87%) | Native `max-pain`; modal strike across the curve is **$40.00** (8 of 15 expiries incl. the two heaviest). ⚠️ **Weak magnet** — earnings expiry holds only 6.98% of OI and ENPH is **absent from `pin-risk`** [STRUCT:max_pain], [OI:term_structure], [OI:pin_risk] |

**Price-context colour (advisory).** RSI **36.13** — weak but **not** oversold —
with price below SMA20/50/200 [HIST:rsi fz]. ENPH is **−48.45% from its 52-week
high ($73.74)** yet still **+47.47% above the 52-week low ($25.78)**
[HIST:52w_proximity fz]. There is room in both directions; this is not a
washed-out bottom, and it is not a chase. ATR **3.18 = 8.4% of spot** — the
±12.25% implied move is only **1.46× ATR**.

## Invalidation

- **Price-based:** **Two daily closes below $35.00** (the `put_wall_support`,
  4,217 puts vs 10 calls) — that confirms the crowded short was correctly
  positioned and kills the squeeze read outright. Symmetrically, a **daily close
  above $42.66** (the upper bound of the priced move) invalidates the
  range/neutral framing and hands the tape to short-gamma trend continuation.
- **Signal-based:** `net_vanna` flips **negative**, or `gex regime` exits
  `FULLY_NEGATIVE` [STRUCT:vanna_charm], [HIST:gex_time_series] — either removes
  the mechanical squeeze that is the entire reason not to be short. Also:
  `call_ask_share` remaining **below 0.50** for three sessions after the print
  (it has been <0.50 in **6 of 6** sessions) [FLOW:screener_ask_bid DUCKDB] means
  the tape never turned and the primary entry should not be taken.
- **Macro-based:** **Hawkish FOMC surprise 2026-07-29 14:00 ET** — the June SEP
  already lifted the median YE-2026 dot to **3.8%** from 3.4% with **9 of 18**
  officials projecting a hike [MACRO:FOMC_2026-06-17]; a statement confirming that
  path, or **`DGS10` extending materially above 4.69%** (already +28bp in 30 days)
  [MACRO:DGS10_2026-07-24], directly compresses residential-solar financing
  economics and overrides any positioning-driven bounce.

## Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** `p_raw = 0.556` (n = **9**, source = `backtest`,
  signal class `bearish_flow`) → N-cap for `n < 10` is 0.75 → **capped
  `p = 0.556`** [HIST:signal_backtest]
  - ⚠️ **Two caveats that matter more than the number.** (i) The tool is
    **market-wide** (constituents: TSLA, LULU, GOOGL, GLD, QQQ, SPY, META, MSFT) —
    this is a signal-class base rate, **not** ENPH's rate — and self-describes as
    *"In-sample backtest — not a robust live edge"*, with `avg_move_pct = 0.48`.
    At n=9, 55.6% is **5 wins in 9**; the 95% CI spans roughly 27–81% and does not
    exclude a coin flip. (ii) `p` was fetched for the **`bearish_flow`** class,
    but the blueprint's residual bias is **NEUTRAL with an upside skew** — so `p`
    does not correspond to the direction actually being expressed. **Moot, because
    directional size is 0%**, but recorded so phase-10 and the calibration loop
    are not misled.
- **Kelly inputs:** `b = 1.49` (target $42.50, entry $38.01, stop $35.00 →
  4.49 / 3.01), `fraction = 0.25`, `cap_pct = 5`
- **Raw Kelly:** `(0.556 × 1.49 − 0.444) / 1.49 = 0.258` → `0.258 × 0.25 × 100 =
  6.45%` → capped at `cap_pct` = **5.00%**
- **Win-rate map ceiling:** `p = 0.556` ∈ [0.50, 0.70] → **half** → ≤ 2.5%.
  Take the smaller: **2.50%** pre-gate.
- **Risk gates** (each can only cut; all five listed):
  1. **Fundamentals (phase-7b): `VETO`** — 2 of 3 axes contradict the bearish flow
     bias (4/4 beat rate, mean surprise +19.24%; recent MSPR +96.66 / +77.60) →
     **directional size = watch-only / 0%.** Defined-risk carry permitted, marked
     "fundamentals-vetoed".
  2. **Sentiment / crowd (phase-7c): `VETO`, `crowd_state = CROWDED_SHORT`** —
     17.55% of float short and **rising** (15.09M → 16.79M shares) into an armed
     vanna squeeze → **directional size = watch-only / 0%.** Marked
     "sentiment-vetoed".
  3. **Correlation cluster (phase-6/8): none.** ENPH is the only blueprint for
     2026-07-27; `portfolio-correlation` returned `tickers_analyzed = 1`,
     `high_correlations = null` (independently re-run by `risk-monitor`) →
     **no-op.**
  4. **Sector rotation (phase-6): `ADVERSE`** to the bearish read — Technology
     `persistence_score = 1`, `trend = "INFLOW"` 5/5 → would cut half a step.
     **Moot at 0%**, and heavily qualified (inflow decayed −85% to $367M and the
     sector still closed **−0.90%**).
  5. **Debate (phase-8b): `bull_residual 0.65` vs `bear_residual 0.65` →
     `disconfirmed = true`** → **down-shift the conviction bin by one** (applied:
     bin is 0.55) **and cut one size step.**
- **Context modifier (phase-0.5): `BUSY_NAME_NORMAL_DAY`** — do **not** size at
  the top of the band. Today's option volume is the **16.4th self-percentile**
  and premium the **31.5th**; the big cross-sectional numbers are ENPH's baseline,
  not a signal.
- **Final size: 0.00% directional (WATCH-ONLY).**
  Defined-risk carry allowance: **≤ 1.00% of book risk**, and only post-event.
- **Deviation reason:** none. **An upward deviation is forbidden here** — three
  gates fired (7b VETO, 7c VETO, 8b disconfirmed) and context is
  `BUSY_NAME_NORMAL_DAY`.

## Option structures

**Both structures below are CONDITIONAL on the post-event re-assessment. Neither
is entered before the 2026-07-28 print. Directional size is gated to 0% until
7b/7c conditions change; the carry structure is capped at ≤1.00% of book risk.**

All prices are **actual NBBO** from `bot-eod-report-2026-07-27.parquet`, not estimates.

### Directional (primary) — 2026-08-21 $40 / $45 call debit spread

- **Structure:** call debit spread (defined risk), **conditional long**
- **Strikes / expiry:** buy $40 call / sell $45 call, **2026-08-21** (25 DTE)
- **Actual quotes:** $40C bid 2.78 / **ask 3.18** (IV 0.997, Δ 0.458); $45C
  **bid 1.41** / ask 1.59 (IV 0.986, Δ 0.283)
- **Debit:** **≈ $1.55** per spread (mid-to-ask fill; $1.48 at mids, $1.77 at the
  worst side)
- **Breakeven:** **$41.55** (+9.3% from spot — **inside** the ±12.25% priced move)
- **Max loss:** **$1.55** ($155/contract) · **Max gain:** **$3.45** (2.23× risk)
- **Net delta:** 0.175 per spread
- **Why this structure:**
  - **It is the direct answer to phase-8b's winning attack.** The debate broke the
    naked front-week straddle because 170.1% IV requires **>12.25%** to break even
    and the April precedent (−9.1%) would have lost. This structure pays
    **~99% IV** on the 2026-08-21 expiry — **not** the 170.1% front week
    [STRUCT:iv_term_structure] — and its breakeven at +9.3% sits **inside** the
    priced move rather than beyond it.
  - **Expected-move check (N4):** spread width **$5.00 > expected move $4.65**, so
    it does not cap upside before the move completes; the $45 short strike is
    **+18.4% ≈ 1.5×** the priced move — at the richness boundary, accepted.
    Expiry is **past both binaries**, so no single-catalyst gap can exceed max
    loss (max loss = debit, by construction).
  - Strikes anchor to real structure: **$40** is the modal max-pain magnet (8 of
    15 expiries), the SMA200 ≈$40.01, and the `put_heavy` strike [OI:oi_by_strike];
    **$45** carries 1,744 calls / 3,111 puts at that expiry.
  - **It expresses the residual view honestly**: don't short, mild upside skew via
    the vanna squeeze, defined risk, no exposure to the event's IV crush.

### Defined-risk alternative — 2026-08-21 $35 / $30 put credit spread

- **Structure:** put credit spread — **"fundamentals-vetoed / sentiment-vetoed,
  carry only"**
- **Strikes / expiry:** sell $35 put / buy $30 put, **2026-08-21** (25 DTE)
- **Actual quotes:** $35P **bid 2.69** / ask 2.90 (IV 0.988, Δ −0.368);
  $30P bid 0.90 / **ask 1.06** (IV 0.986, Δ −0.172)
- **Credit:** **≈ $1.63** per spread
- **Breakeven:** **$33.37** — which is **$33.36**, the exact lower bound of the
  ±12.25% implied move [CTX:implied_move_pct]. The structure breaks even precisely
  at the bottom of the priced range.
- **Max loss:** **$3.37** ($337/contract) · **Return on risk:** 48.4%
- **Why this structure:**
  - **It sells the wing, not the event** — phase-5's explicit conclusion
    (`vrp = +0.2566`, `regime = "PREMIUM_SELLING"`, harvestable in the back
    months, **not** in the 170% front week) [HIST:vrp].
  - **It follows documented professional flow.** Phase-3 shows someone opened
    exactly this: **Aug-21 $35 puts, +473 OI on 655 volume with 582 on the bid**
    (sold), avg price $2.58 [OI:oi_changes DUCKDB]. Also C70, C75 and Oct $30 puts
    — the same desks are short both wings.
  - **$35 is the cleanest support in the chain** — 4,217 puts vs **10** calls at
    ≤30 DTE, 3,734 puts / 0 calls at this very expiry [OI:oi_by_strike].
  - **Historical sanity check:** the April precedent (**−9.1%**) would put ENPH at
    **$34.55 — above the $33.37 breakeven.** Only a print *worse* than April loses.
- ⚠️ **The honest risk.** This is **short the left tail into a deteriorating
  business**, and phase-8b's #1 unrefuted point is that **guidance, not the print,
  is the event** — ~29% of guided Q2 revenue (~$85M) is non-recurring safe-harbor
  [MACRO:ENPH_Q2-2026_preview]. A guide-down through $33.37 loses, and a −20% gap
  (to $30.41) is near max loss. Both vetoes apply to it. **Cap at ≤1.00% of book
  risk and only enter after the guide is known** — which removes most of its edge,
  and that is the correct trade-off here.

### Structures explicitly rejected

- **Naked front-week straddle/strangle (2026-07-31):** rejected by phase-8b —
  needs >12.25% to break even at 170.1% IV; 1 of 2 precedents loses.
- **Iron condor** (despite `market-regime` `trading_guidance` suggesting *"iron
  condors in range"*): rejected — no pin (ENPH absent from `pin-risk`),
  `zero_gamma_level = null`, and a documented ±39% / −9.1% reaction history.
  Short vol into this event is not a range trade.
- **Any directional short:** rejected by **both** gates and by **0 of 5** desk
  agents.
- **Far-OTM call credit spread (Sep-18 $60/$70):** examined and rejected on the
  actual quotes — $60C bid 0.63 vs $70C ask 0.33 gives a **$0.30 credit against
  $9.70 of risk (3.1%)**. The "dead wing" is correctly priced as dead; there is no
  premium to harvest there at retail scale.

## Macro overlay (cite phase-6)

- **Tailwinds:**
  - Technology sector flow `persistence_score = 1`, `trend = INFLOW`, 5/5 sessions
    [MACRO:sector_flow_persistence_2026-07-27] — ⚠️ decayed **−85%** to $367M and
    the sector still closed −0.90%
  - Utilities (solar's nearer neighbour) also `persistence 1.0 INFLOW`
    [MACRO:sector_flow_persistence_2026-07-27]
  - Core CPI **+2.57%** YoY, near target; headline CPI **−0.42% MoM**
    [MACRO:CPILFESL_2026-06]
  - Broad dollar **−0.58%** over 30 days — mild support for European revenue
    [MACRO:DTWEXBGS_2026-07-24]
- **Headwinds:**
  - **Section 25D repealed effective 2025-12-31**; FY installs guided **−22%**,
    Q2 interconnections **−25%+ YoY**; BNEF sees no recovery to 2023 levels within
    a decade [MACRO:25D_expiry_2025-12-31], [MACRO:OhmAnalytics_Q2-2026]
  - **`DGS10` +28bp in 30 days to 4.69%**; `DGS2` +22bp to 4.33%
    [MACRO:DGS10_2026-07-24]
  - **June dot plot median YE-2026 at 3.8%** (from 3.4%), **9 of 18** officials
    projecting a hike [MACRO:FOMC_2026-06-17]
  - **Core PCE +3.41% YoY** — the Fed's preferred gauge well above target
    [MACRO:PCEPILFE_2026-05]
  - Market regime **"TRANSITIONAL — reduce position size"**, `trend = CHOPPY`,
    breadth **35.2%**, SPY below both 20d and 50d SMA
    [MACRO:MarketRegime_2026-07-27]
  - Payroll growth halved (+129k → **+57k**) [MACRO:PAYEMS_2026-06]
- **Net: HEADWIND (strong).** 11 headwinds to 4 tailwinds; the headwinds are
  structural and legislated, the tailwinds technical and decaying.
- ⚠️ **Unmeasured:** ISM Services PMI and consumer confidence for July 2026 could
  not be retrieved — the **consumer channel is a blind spot**, and it is the most
  relevant soft indicator for residential-solar demand.

## Catalyst calendar (next 30d)

> **Front-expiry implied move: ±12.25% / ±$4.65 → $33.36 – $42.66**
> [CTX:implied_move_pct]. Every structure above is sized to this range.

| Date | Event | Impact direction |
|---|---|---|
| **2026-07-28, postmarket** | **ENPH Q2 2026 earnings** — consensus $292.2M (−19.6% YoY) / $0.46 (−33.3% YoY); guide $280–310M incl. **~$85M safe-harbor**; ~3pp tariff GM hit | **? — IS the ±12.25% move** |
| **2026-07-29, 14:00 ET** | **FOMC statement** (no dot plot); target 3.50–3.75% held since Dec 2025 | **?** — ENPH trades its gap into the Fed |
| 2026-07-31 | Front-week expiry — the **positive-gamma island expires** (`today_total_gex +1,047,168`); IV crush 170.1% → ~90% completes | + (vanna) / ? |
| ~2026-08-01 | ISM Manufacturing PMI (July) | ⚪ low relevance |
| ~2026-08-07 | Nonfarm payrolls (July) | ? consumer capacity |
| ~2026-08-12 | CPI release (July) | ? higher-for-longer |
| **2026-08-21** | **Monthly OPEX — 18.64% of total OI**; $40 put wall (7,888), $35 put wall (3,734). **Both structures expire here.** | ? |
| ~2026-08-26 | Ohm Analytics / SEIA Q3 install data | − confirms/refutes −22% FY |

## Post-trade monitoring checklist

- [ ] **Re-run `uw options-structure vanna-charm` and `gex` on 2026-07-29.** The
      entire non-short case rests on `net_vanna = +913` surviving the IV crush. If
      vanna flips negative or GEX exits `FULLY_NEGATIVE`, the squeeze read is dead
      and the primary entry is cancelled [STRUCT:vanna_charm], [HIST:gex_time_series].
- [ ] **Check `call_ask_share` daily for three sessions post-print.** It has been
      **below 0.50 in 6 of 6** sessions — calls persistently sold. The primary long
      entry requires it to cross **above 0.50** [FLOW:screener_ask_bid DUCKDB].
- [ ] **Re-check the Q3 guide against the ~$85M safe-harbor cliff**, not the Q2
      headline. Phase-8b's #1 unrefuted point: guidance is the event
      [MACRO:ENPH_Q2-2026_preview].
- [ ] **Re-pull short interest at the next semi-monthly settlement.** Shorts rose
      15.09M → 16.79M; if they keep adding through the print the squeeze fuel
      grows, if they cover the vanna case weakens [SENT:short_interest].
- [ ] **Re-run `uw oi biggest-increases` on 2026-07-28/29** to see whether the
      C70/C75/P35/P30 premium sellers are rolled, closed or added to — they are the
      professionals with a range view [OI:smart_positioning].
- [ ] **Watch $35.00 and $42.50 on a closing basis only.** Both sit inside the
      priced move and will be tagged intraday without meaning anything.
- [ ] **Re-run `uw risk market-regime`** — currently "TRANSITIONAL, half position
      sizes." A shift to a trending regime changes the sizing ceiling
      [MACRO:MarketRegime_2026-07-27].

## Conviction deviation

None. Conviction **0.55** is the bottom bin, consistent with two `VETO` gates, an
8b disconfirmation (which already down-shifted one bin), and
`BUSY_NAME_NORMAL_DAY` context. No upward deviation is taken or permitted.

## Citations summary

Minimum 3 distinct upstream datapoints (M-04). Listed for phase-10 spot-check:

1. **[FLOW:insights_deep_dive]** — derived `net_flow = bullish_premium −
   bearish_premium = 1,843,847 − 2,102,578 = **−$258,731**` —
   `phase-1-flow.md` §Whole-tape aggregate *(phases 1–4: today's tape)*
2. **[STRUCT:vanna_charm]** — `net_vanna = +913`, `put_vanna 1,208`,
   `call_vanna −294`; `net_dex = −$40,323,765` —
   `phase-4-structure.md` §Vanna + charm, §DEX *(phases 1–4: today's tape)*
3. **[HIST:signal_backtest]** — `bearish_flow win_rate = 55.6%`,
   `total_signals = 9`, `avg_move_pct = 0.48` —
   `phase-5-historical.md` §Signal backtest *(phase 5–7: historical)*
4. **[FUND:earnings_surprises]** — beat rate **4/4**, mean surprise **+19.24%**,
   estimate bar cut $0.634 → $0.419 — `phase-7b-fundamentals.md`
   §Earnings-surprise history *(phase 5–7)*
5. **[SENT:short_interest]** — short interest **15.09M → 16.79M shares = 17.55%
   of float**, days-to-cover 2.63 — `phase-7c-sentiment.md` §Short interest & borrow
6. **[MACRO:25D_expiry_2025-12-31]** — Section 25D repealed effective
   2025-12-31; FY installs guided **−22%** — `phase-6-macro.md` §Sector overlay
   *(phase 6 or 8: macro/agent)*
7. **[AGENT:earnings-scout]** — ENPH's last two earnings reactions **+39%
   (2026-02-04)** and **−9.1% (2026-04-28)** vs a 12.25% implied move —
   `phase-8-agent-views.md` §Verification *(phase 6 or 8)*
8. **[DEBATE:disconfirmation]** — `bull_residual 0.65`, `bear_residual 0.65`,
   `disconfirmed = true` — `phase-8b-debate.md` §Disconfirmation verdict
9. **[CTX:implied_move_pct]** — `implied_move_perc = 0.1224573` → **±12.25% /
   ±$4.65** — `phase-0.5-context.md` §Verdict `[CTX:]` block
