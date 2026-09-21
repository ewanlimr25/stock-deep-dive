# Phase 9 — Trade Blueprint

**Ticker:** FSLR **As-of:** 2026-07-31 **Spot (official close):** 211.03
**Generated:** 2026-07-31
**Upstream:** `phase-0.5-context.md` → `phase-8b-debate.md`

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

---

## Thesis (≤3 sentences)

The flow is genuinely long — a 1,900-lot Aug-21 $230 call block printed at the
offer and its **72,200-share dealer delta hedge landed 49 seconds later at a
101.1% size match**, proving the customer bought it and putting reconstructed
net customer delta at **+$10.73M** rather than the screener's −$2.37M
`[DP:ts_confirm DUCKDB]` `[FLOW:delta_notional DUCKDB]` — but it has bought
nothing: **twelve sessions and $17.28M of sweep premium have moved the stock
211.93 → 211.03** with `dominant_direction: "mixed"` `[FLOW:sweep_persistence]`
`[HIST:trend]`. Today the market priced that stalemate exactly: the high of
**217.1274** stopped **0.17% short of the $217.50 gamma wall** (net_gex
+2,344,544, 78% of the summed surface) and gave back 6.10 points
`[STRUCT:gex]` `[HIST:intraday_range DUCKDB]`. Four independent agents returned
**RANGE ×3 / NEUTRAL ×1, zero LONG, zero SHORT, every one at conviction 2/5**,
converging unprompted on 205.83 support and 217.50 resistance
`[AGENT:accumulation-hunter]` `[AGENT:risk-monitor]`.

---

## Bias + conviction + horizon

| Field | Value |
|-------|-------|
| **Bias** | **RANGE** (plurality of phases 1–8: 3/4 agents RANGE, 1 NEUTRAL, 0 LONG, 0 SHORT) |
| **Conviction** | **0.55** — slight edge, coin-flip plus a sliver |
| **Horizon** | **1-4w** (to the 2026-08-21 OPEX), managed on 1-5d triggers |
| Directional lean within the range | **Mildly constructive** — the flow evidence is real, it is simply small and unconfirmed by price |

**How the conviction bin was reached.** The narrative base was **0.65** —
moderate edge with real disconfirming evidence, consistent with phase-7's
composite MIXED at 8.8% confidence and the desk's unanimous 2.0/5.
`phase-8b-debate.md` returned **`disconfirmed: true`** (bear residual **0.85**
≥ bull residual **0.55**), which per `rubrics/sizing-rubric.md` §"Risk gates"
**down-shifts the bin by one → 0.55**.

**No conviction deviation is claimed.** If phase-10's confluence band implies
something other than 0.55, phase 10 should override — this plan does not
argue for an exception.

**The bias deserves one sentence of defence.** Phases 1–3 read mildly bullish
and phase 2 read ACCUMULATION, so a LONG bias was available. It is not taken
because (a) the desk was unanimous that no directional trade exists, (b) the
debate disconfirmed the long, and (c) the one empirical test of the bull case
— the 217.50 tag — failed today. **RANGE is not a refusal to choose; it is the
conclusion the evidence supports.**

---

## Entry zones

| Zone | Price | Trigger | Source |
|------|------:|---------|--------|
| **Primary** | **205.83 – 207.50** | Tag of the dark-pool support shelf **without** a daily close below 205.83; the shelf is $90.6M across 48 prints at 205.83–206.01 and coincides with the 0/7/14/28-DTE max-pain cluster at 205–210 | `[DP:price_levels]` `[STRUCT:max_pain]` |
| **Aggressive** | **200.00 – 202.59** | Flush into the `put_wall_support` at 200 (net_oi −1,811, net_gex −465,782) and the 202.59 dark-pool level, **with an intraday reclaim of 205.83**. This is the short-gamma acceleration zone — only take it on a reclaim, never on the break | `[OI:oi_by_strike]` `[STRUCT:gex]` |
| **Fade (plan B)** | **214.00 – 217.50** | Rejection in the congestion band — short/roll-down the long side, or initiate the call-side credit. The band is triple-confirmed: phase-2's 28,000-share $214.00 block, phase-3's `call_wall_resistance` at 217.5 (net_oi +3,139), phase-4's net_gex +2,344,544 | `[DP:largest]` `[OI:oi_by_strike]` `[STRUCT:gex]` |

**Do not chase 211.03.** Spot sits mid-range with 6.47 points to resistance and
5.20 to support — the worst risk/reward on the board. **Every entry above is
below spot except the fade**, which is deliberate.

---

## Levels to watch

| Level | Price | Source |
|-------|------:|--------|
| **Resistance (primary)** | **217.50** | `oi-by-strike` `call_wall_resistance`, net_oi +3,139 (3,172 calls vs 33 puts), +3.07% `[OI:oi_by_strike]`; net_gex **+2,344,544** = 78% of summed gamma `[STRUCT:gex]`; 0DTE book independently tagged it `support_wall` at +2,339,132 `[STRUCT:today_gamma_flip]` |
| Resistance (first touch) | **214.00** | 28,000 shares / $5.99M bought above the offer at 14:13 ET, plus 5,000 @ 214.39 and 1,880 @ 214.55 `[DP:largest]` |
| **Gamma flip (ZGL)** | **215.03** | `zero_gamma_level`, spot 1.90% below; treat as a **±2% band (210.7–219.4)** per the low-liquidity caveat `[STRUCT:gex]` |
| **Support (primary)** | **205.83** | Dark-pool shelf $51.44M / 21 prints; with 206.01 ($39.16M / 27 prints) = $90.6M across 48 prints `[DP:price_levels]`. **All four agents named this independently** `[AGENT:sweep-tracker]` |
| Support (secondary) | **202.59** | Dark-pool level, $45.94M / 17 prints `[DP:price_levels]` |
| **Support (structural)** | **200.00** | `put_wall_support` net_oi −1,811 (2,588 puts ≤30d) `[OI:oi_by_strike]`; net_gex **−465,782** — below here dealer hedging accelerates downward `[STRUCT:gex]` |
| Support (deep) | **190.00** | `put_wall_support` net_oi −3,040; net_gex −583,415 `[OI:oi_by_strike]` |
| **Pin magnet (near expiry)** | **205 – 210** | `max-pain`: 0DTE **210**, 7d **205**, 14d **210**, 28d **205** — all *below* spot `[STRUCT:max_pain]` |
| Pin magnet (Aug-21) | **250 — DISREGARD** | `max-pain` returns 250 at +18.47%, roughly a **5σ** move in 21 days and computed on lagged, 38.9%-coverage OI. Explicitly excluded as untradeable `[STRUCT:max_pain]` |
| Negative-gamma pocket (up) | **220.00** | net_gex −620,582 — air above the wall; a clean break of 217.50 should travel fast `[STRUCT:gex]` |

**Price-context colour (advisory, does not affect sizing).** **RSI 43.00** —
neutral, so there is neither an oversold bounce edge nor exhaustion risk
`[HIST:rsi fz]`. Price is **−34.25% from the 52-week high (320.95)** and
**+22.70% off the low (171.99)** `[HIST:52w_proximity fz]`, below SMA20
(−1.49%), SMA50 (−13.93%) and SMA200 (−9.91%). **ATR 10.34 = 4.90% of spot** —
the 205.83–217.50 range is barely wider than one ATR, which is the single
strongest argument for defined-risk structures over a stop-based stock
position.

---

## Invalidation

**Price-based** — *the tightest of:*
- **Two daily closes below 205.83** (dark-pool shelf, `[DP:price_levels]`;
  unanimous agent invalidation). **Accelerated to a hard stop on any close
  below 200.00**, where net_gex turns −465,782 and dealer hedging amplifies
  the decline `[STRUCT:gex]`.
- **On the upside this is a range trade, so a confirmed close above 217.50 on
  above-average volume invalidates the *range*, not the constructive lean** —
  it converts the position to LONG per `[AGENT:sweep-tracker]`. Roll the
  call-side risk up; do not hold a short call through it.

**Signal-based** — *the most diagnostic:*
- **Regular-session dark-pool buy% falls back below 50% for two consecutive
  sessions.** The entire phase-2 case is the 28.4% → 64.2% → **73.1%** flip
  `[DP:session_split DUCKDB]`; if it reverts, the accumulation was
  post-earnings position-squaring, not initiation.
- **`FSLR260821C00230000` open interest fails to print near ~2,155 on the
  2026-08-03 snapshot.** Pre-trade OI was 255 `[OI:biggest_increases]`. If the
  1,900-lot block did not open, the bull's hardest evidence collapses and net
  customer delta swings from **+$10.73M to roughly −$4.5M** `[FLOW:delta_notional DUCKDB]`.
  **This is the single cheapest falsification test in the plan — check it first.**

**Macro-based** — *highest-probability event in the window:*
- **A hot core CPI print on ~2026-08-12.** Core PCE is already **+3.29% YoY**
  and **three FOMC members dissented in favour of a hike** on 2026-07-29
  `[MACRO:PCEPILFE_2026-06 FRED]` `[MACRO:FOMC_2026-07-29 WebSearch:federalreserve.gov]`.
  The 10-year has backed up **24bp to 4.68%** in a month `[MACRO:DGS10_2026-07-30 FRED]`;
  a further leg higher transmits directly to utility-scale solar project IRRs.
  **This is the only scheduled release in the window with a plausible move
  beyond the ±3.5% 21-day expected move.**

**Exit style: TRANCHE, not hard stop.** Close **50%** on the first close below
205.83 and the remaining **50%** on a close below 200.00 — or, for the credit
structure, **roll down and out rather than close**. Rationale: both structures
below are defined-risk with max loss already inside the position, and with
**ATR at 4.90% of spot** a hard stop at 205.83 (−2.46%) would be triggered by
half an average day's range.

---

## Sizing (% of risk, NOT dollars)

**Step 1 — Kelly `p` from the phase-5 empirical win-rate.**

```
win_rate_source:          backtest          (phase-5 sizing handoff block)
signal_class:             bullish_flow
p_raw:                    1.00              ("100.0%", reported as a string)
win_rate_n:               9
N-conditional cap:        n < 10  ->  0.75
p = min(1.00, 0.75)  =    0.75
```

**This `p` is not believable and I am recording why.** Phase 5 stated the raw
rate is **in-sample by the tool's own admission** (*"In-sample backtest — not a
robust live edge"*), **market-wide rather than FSLR-specific** (the command
takes no `--symbol`), and drawn from **9 firings over a 5-day window in which
the tape rallied**, with `avg_move_pct` 8.66 — close to measuring beta.
Phase 5's explicit recommendation was to fall back to the conviction bin.
The rubric is followed as written (`win_rate_source = backtest` → use the
capped rate), **but the choice is immaterial**: the conviction-bin fallback
would give `p = 0.55`, capped at 0.65, and **the gates below bind the final
size in either case**. Both paths are shown at Step 6.

Note also that `dark_pool_accumulation` — the class matching phase-2's
dominant signal — returned **`total_signals: 0` on two separate runs**
`[HIST:signal_backtest]`.

**Step 2 — payoff ratio.**

```
entry  = 211.03  (spot; the primary entry at 205.83-207.50 improves this)
target = 217.50  (gamma wall / unanimous agent resistance)
stop   = 205.83  (dark-pool shelf / unanimous agent invalidation)
b = |217.50 - 211.03| / |211.03 - 205.83| = 6.47 / 5.20 = 1.244
```

**Step 3 — raw Kelly.**

```
raw_kelly = (p x b - (1 - p)) / b
          = (0.75 x 1.244 - 0.25) / 1.244
          = (0.933 - 0.250) / 1.244
          = 0.549
```

**Step 4 — fractional Kelly, cap, and the win-rate sizing map.**

```
suggested_size_pct = min(0.549 x 0.25 x 100, cap_pct 5.0) = min(13.73, 5.0) = 5.00%
win-rate sizing map at p = 0.75 (>= 0.70)  ->  "full (up to cap_pct)" = 5.00%
take the smaller                            ->  5.00%
SHORT-side floor (p < 0.50)                 ->  not triggered
```

**Step 5 — risk gates. All five listed; three fired.**

| # | Gate | Value | Fired? | Effect | Running size |
|--:|------|-------|:------:|--------|-------------:|
| — | *(pre-gate)* | — | — | — | **5.000%** |
| 1 | **Fundamentals (7b)** | `CAUTION` — 1 contradiction (insider axis): five C-suite officers sold ~720,802 sh on 2026-07-29, MSPR negative 4 straight months, OCF −$214.9M `[FUND:insider_cluster fz]` | **YES** | cut one step (full → half) | **2.500%** |
| 2 | **Sentiment / crowd (7c)** | `CAUTION`, `crowd_state = BALANCED` — three price targets cut the day after a +37.1% beat `[SENT:revision_trend]` | **YES** | cut one step (half → starter) | **1.250%** |
| 3 | **Correlation cluster** | `null` — FSLR is the only blueprint for 2026-07-31; `portfolio-correlation` returned `tickers_analyzed: 1`, `high_correlations: null` `[MACRO:portfolio_correlation]` | no | no-op | 1.250% |
| 4 | **Sector rotation** | `aligned` — Technology 5-day net directional flow **+$839.5M**, positive 4 of 5 sessions `[MACRO:sector_flow_persistence DUCKDB]` | no | no-op | 1.250% |
| 5 | **Debate disconfirmation (8b)** | `disconfirmed: true` — **bear residual 0.85 ≥ bull residual 0.55** `[DEBATE:bear_residual]` | **YES** | down-shift bin (0.65→0.55) **and** cut one step | **0.625%** |

**Context modifier (phase-0.5, applied alongside).** `unusual_verdict` was set
**GENUINELY_UNUSUAL** but **revised by phase 1 to `BUSY_NAME_NORMAL_DAY`**
once the $2,545,750 (9.5%) of `mid`/`no_side` premium excluded from UW's
directional math was accounted for `[CTX:universe_rank_net_dir]`. Per the
rubric this means **do not size at the top of the band** — satisfied with
room to spare, and it independently forbids any upward deviation.

**Additional regime input (not a formal gate).** `uw risk market-regime`
returns **"TRANSITIONAL — Mixed signals, reduce position size"** with
`trading_guidance` **"Half position sizes. Favor defined-risk strategies. Iron
condors in range"** and breadth at **34.1% bullish** `[MACRO:MarketRegime_2026-07-31 UW]`.
**This is not applied as a fourth multiplicative cut** — doing so would take
size to 0.31% — but it is why the structures below are defined-risk and why no
stock position is proposed.

**Step 6 — final size.**

```
final_size_pct = 0.625%   of book risk
deviation_reason = null   (no upward deviation; forbidden — three gates fired
                           and context is BUSY_NAME_NORMAL_DAY)
```

**Sanity check against the alternative `p`.** With the conviction-bin fallback
(`p = 0.55`, capped 0.65): raw_kelly = (0.55×1.244 − 0.45)/1.244 = **0.188** →
0.188 × 0.25 × 100 = **4.70%**, and the win-rate map at 0.50–0.70 caps at
`cap_pct/2` = **2.50%** → take 2.50% → the same three gates give
**2.50 → 1.25 → 0.625 → 0.3125%**. **So the honest range is 0.31%–0.625%**;
this plan takes the upper end **0.625%** because it follows the rubric as
written, and notes that a PM preferring phase-5's own recommendation should
halve it again.

**Independent corroboration.** `phase-8-agent-views.md`'s risk-monitor computed
this separately as **0.5 (regime) × 0.75 (7b) × 0.75 (7c) ≈ 0.28**, discounted
to **"roughly 1/8–1/5 of a normal unit."** **0.625% is exactly 1/8 of the 5.0%
cap** `[AGENT:risk-monitor]`. Two different methods, the same answer.

---

## Option structures

**Expected move (N4).** Front-expiry `implied_move` **$1.611 / 0.7625%**
`[CTX:implied_move_pct]` — a **daily** figure, and **post-earnings it contains
no event premium** (`front-end-iv-ratio` **FLAT at 1.001** `[STRUCT:front_end_iv_ratio]`).
Scaled to the 2026-08-21 expiry: **√21 × 0.7625% ≈ 3.49% ≈ $7.37**, giving a
1σ band of **203.66 – 218.40**.

**Catalyst-gap check (mandatory).** A single expected-move gap **down** from
211.03 lands at **~203.66 — below the 205.83 stop.** The ~2026-08-12 CPI print
can therefore gap through the invalidation level in one session. Size is
already at 1/8 of cap and the expiry cannot avoid CPI without also abandoning
the OPEX anchor, so **the mitigation is structural: both positions below are
defined-risk, with max loss fixed at entry.** This is the explicit reason no
stock position is proposed.

> **All option prices below are last-observed NBBO midpoints from the
> 2026-07-31 tape.** They are snapshots taken at different times of day and are
> non-monotonic in places (e.g. the 225C mid prints above the 222.5C).
> **Re-price live before execution** — the strike selection, not the debit, is
> the deliverable.

### Directional (primary)

**Long Aug-21 2026 $215 / $230 call debit spread**

| Field | Value |
|-------|------:|
| Long leg | **Aug-21 $215 call** @ mid **15.10** (delta 0.524, IV 0.768) |
| Short leg | **Aug-21 $230 call** @ mid **8.57** (delta 0.362, IV 0.776) |
| **Net debit** | **≈ $6.53** |
| Width | $15.00 |
| **Max loss** | **$6.53** (= the debit) |
| **Max gain** | **$8.47** |
| **Breakeven** | **$221.53** (+4.98%) |
| Payoff ratio | 1.30 : 1 |
| Debit as % of width | 43.5% |
| DTE | 21 |

**Why these strikes.** **$215 is the zero-gamma level (215.03)** — the position
turns on precisely the flip the stock has been beneath all month
`[STRUCT:gex]`. **$230 is the strike the smart money actually bought** — the
1,900-lot block, whose dealer hedge phase 2 identified `[FLOW:unusual_volume]`
`[DP:ts_confirm DUCKDB]`. The $15 width is **2.0× the 21-day expected move
($7.37)**, so the structure does not cap upside before the move can complete.

**Why not something cheaper.** It cannot be. **VRP is +0.3587** — options price
**1.93×** the delivered vol `[HIST:vrp]` — so every debit structure starts with
a vol headwind, and the ATM call costs 7.2% of spot. **A 43.5%-of-width debit
is the price of expressing this view directionally, and it is why this is the
satellite and not the core.**

**Honest weakness:** the breakeven of **221.53 sits above the 217.50 wall**.
This structure **requires the breakout that failed today** — the sweep-tracker's
*"close above 217.50 with confirming volume"* condition `[AGENT:sweep-tracker]`.
**Consider it a contingent entry**: take it on the breakout confirmation
rather than now, or accept that ~half the debit is buying the option to be
right later.

### Defined-risk alternative (the one I would actually put on)

**Short Aug-21 2026 $200 / $190 put credit spread**

| Field | Value |
|-------|------:|
| Short leg | **Aug-21 $200 put** @ mid **9.23** (delta −0.329, IV 0.756) |
| Long leg | **Aug-21 $190 put** @ mid **5.98** (delta −0.241, IV 0.757) |
| **Net credit** | **≈ $3.25** |
| Width | $10.00 |
| **Max loss** | **$6.75** (width − credit) |
| **Max gain** | **$3.25** |
| **Breakeven** | **$196.75** (−6.77%) |
| Credit as % of width | 32.5% |
| DTE | 21 |

**Why these strikes.** **$200 is the `put_wall_support`** (net_oi −1,811, 2,588
puts ≤30 DTE) and the strike where net_gex turns **−465,782**; **$190 is the
next wall** (net_oi −3,040, net_gex −583,415) `[OI:oi_by_strike]` `[STRUCT:gex]`.
The short strike sits **below** the unanimous 205.83 invalidation and the
breakeven at **196.75 is beneath the 199.24 twelve-session base low**
`[HIST:trend]`.

**Why this is the core position.** Four independent lines converge on selling
premium rather than buying it: **VRP +0.3587 with realized vol falling**
(60d 0.5821 → 30d 0.3821 → 20d 0.3732) `[HIST:vrp]` `[HIST:realised_vol DUCKDB]`;
**`term-skew` COMPLACENT** — 25Δ puts at 0.7613 are *cheaper* than 25Δ calls at
0.7652, so this sells the richer wing relative to history `[STRUCT:term_skew]`;
**`front-end-iv-ratio` FLAT at 1.001**, no event premium to be crushed
`[STRUCT:front_end_iv_ratio]`; and the regime tool's own **"defined-risk
strategies, iron condors in range"** `[MACRO:MarketRegime_2026-07-31 UW]`.
It also aligns with the **max-pain cluster at 205–210** `[STRUCT:max_pain]` and
profits from exactly the outcome the desk expects — **nothing happening**.

**Extension (optional).** Adding a short **Aug-21 $230/$240 call** wing makes
this an iron condor and directly implements the regime guidance — but the
Aug-21 call-wing quotes are stale and compressed (230C 8.57 against 235C 7.60,
non-monotonic), so **the call side is not specified here**; price it live or
leave the structure one-sided.

**Sizing both structures.** Per `rubrics/sizing-rubric.md`: for the debit
spread, **max loss (the $6.53 debit) ≤ 0.625% of book risk**; for the credit
spread, **max loss (width − credit = $6.75) ≤ 0.625% of book risk — not margin
used**. If both are taken, the **combined** max loss must respect the 0.625%
budget, not 0.625% each.

---

## Macro overlay (cite phase-6)

**Tailwinds**
- **`[MACRO:45X_policy WebSearch:novoco.com]`** — Section 45X manufacturing
  credits preserved through **2032**; FSLR expects **$2.10–2.19B in 2026**,
  roughly **9% of a $22.68B market cap, annually**.
- **`[MACRO:sector_flow_persistence DUCKDB]`** — Technology 5-day net
  directional flow **+$839.5M**, positive 4 of 5 sessions. The sector gate is
  **aligned**; phase-0.5's "worst sector" reading was corrected in phase 6.
- **`[MACRO:group_valuation fz EOD]`** — Technology carries the **lowest PEG of
  all eleven sectors (0.88)**; FSLR itself is **P/E 13.01, forward 8.87, PEG
  0.33** `[FUND:peer_pe fz]`.
- **`[MACRO:PAYEMS_2026-06 FRED]`** — payroll growth halved to **+57k** from
  +129k, the main argument for the cuts that would relieve rate pressure.
- **`[MACRO:DTWEXBGS_2026-07-24 FRED]`** — broad USD softer (120.71, −0.6%/30d).

**Headwinds**
- **`[MACRO:DGS10_2026-07-30 FRED]`** — 10-year at **4.68%, +24bp in 30 days**;
  2s10s **+0.47** and steepening. **The binding constraint** on a
  levelized-cost business.
- **`[MACRO:FOMC_2026-07-29 WebSearch:federalreserve.gov]`** — held
  3.50–3.75% on a **9–3 vote with three dissents preferring a hike**.
- **`[MACRO:PCEPILFE_2026-06 FRED]`** — core PCE **+3.29% YoY**, 129bp above
  target.
- **`[MACRO:45Y48E_phaseout WebSearch:novoco.com]`** — 45Y/48E project credits
  in expedited phaseout for construction beginning after **2026-07-04**, a
  date **27 days past**. The subsidy moved from FSLR's *customers* to its
  *factories*.
- **`[MACRO:MarketRegime_2026-07-31 UW]`** — **TRANSITIONAL**, breadth
  **34.1% bullish** (2,142 vs 4,138), guidance **"half position sizes."**
- **`[MACRO:sector_breadth fz EOD]`** — S&P price breadth **43.94% green**,
  median change −0.24%, Technology group −0.49%: money is committing in
  options faster than in prices.

**Net: HEADWIND (moderate).** The macro does not veto the trade; it caps the
size and mandates defined risk.

---

## Catalyst calendar (next 30d)

Front-expiry expected move **±0.76% / $1.61 daily**, **≈±3.49% / $7.37 to the
Aug-21 expiry** `[CTX:implied_move_pct]`.

| Date | Event | Likely impact | vs expected move |
|------|-------|---------------|------------------|
| 2026-08-05 | ISM Services PMI (July) | Low — weak read-through to utility-scale solar | inside ±3.5% |
| ~2026-08-07 | **Nonfarm payrolls (July)** | Medium — a second sub-100k print revives cut pricing; **rate-sensitive positive** | inside ±3.5% |
| 2026-08-07 | Weekly OPEX — P/C OI **1.503**, 3,084 OI | Low; the most put-skewed near expiry | inside |
| **~2026-08-12** | **CPI (July)** | **Medium-high — the key risk.** Core drove three hawkish dissents; a hot print lifts the 10y and hits solar directly | **could exceed ±3.5%; can gap through the 205.83 stop** |
| **2026-08-21** | **Monthly OPEX** — 29,922 OI (13.34% of tracked), P/C 1.166, richest IV on the curve (79.6%) | **High (mechanical)** — where the 1,900-lot $230 block expires and the 72,200-share dealer hedge unwinds | **structural, not directional** |
| Late Aug | Jackson Hole | Medium — the venue for signalling after a 9–3 vote | could exceed ±3.5% |
| *(2026-09-16/17)* | *Next FOMC* | High — **outside the window** | n/a |
| *(2026-10-29)* | *FSLR Q3 earnings* | High — **outside the window** | n/a |

**The window is unusually clean of company-specific catalysts** — the dominant
scheduled event is **mechanical (the 2026-08-21 OPEX)**, which is precisely why
both structures are anchored to that expiry.

---

## Post-trade monitoring checklist

1. **`FSLR260821C00230000` open interest on the 2026-08-03 snapshot.** Pre-trade
   OI was **255**; if the 1,900-lot block opened it should print near **~2,155**
   `[OI:biggest_increases]`. **Highest-value check in the plan** — the entire
   bull case rests on this print having been an opening buy. Run:
   `uw oi biggest-increases --symbol FSLR --min-oi-change 500 --json`.
2. **Regular-session dark-pool buy%, daily.** The thesis rests on
   28.4% → 64.2% → **73.1%** `[DP:session_split DUCKDB]`. **Decompose by session
   every time** — the blended figure reads 0.588 and the closing-auction
   component is an NBBO artifact. Two consecutive sessions below 50% invalidates.
3. **The 217.50 gamma wall and the 215.03 ZGL, daily.** Re-run
   `uw options-structure gex --symbol FSLR --dte-max 45`. A **second failure at
   217.50** confirms resistance and argues for adding the call-side wing; a
   **close above on volume** flips the plan to LONG `[AGENT:sweep-tracker]`.
   Watch whether the ZGL holds near 215 or reverts toward the ~300 it printed
   all month `[HIST:gex_time_series]`.
4. **`iv30d` against today's 0.738.** The credit spread wants IV **flat or
   falling**; a spike compresses the VRP that underwrites it `[HIST:vrp]` and
   reverses the vanna mechanism from dealer-buying to dealer-selling
   `[STRUCT:vanna_charm]`. **Rising IV is an invalidation input, not just
   falling price.**
5. **Analyst revisions and any rating change.** Three targets were cut on
   2026-07-31 with **no rating changed** `[SENT:revision_trend]`. An actual
   *downgrade* — especially Wells Fargo off Overweight — is a materially
   different signal from a target trim.
6. **Insider filings.** Five C-suite officers sold on 2026-07-29
   `[FUND:insider_cluster fz]`. **Any insider buy** would be the single
   cleanest upgrade available to this thesis; further selling compounds the
   7b CAUTION.
7. **The 10-year.** Above ~4.85% the rate headwind becomes the dominant driver
   regardless of flow `[MACRO:DGS10_2026-07-30 FRED]`.

---

## Citations summary

The ≥3 distinct upstream datapoints underpinning the thesis, for phase-10
spot-check:

1. **`[DP:ts_confirm DUCKDB]`** — 72,200-share `qualified_contingent_trade` at
   212.9695 (above the 212.54 ask), **49.0 seconds** after the 1,900-lot Aug-21
   $230 call cross, **101.1% hedge match** (72,200 ÷ 190,000 = delta 0.3800 vs
   the option's 0.3760); the only non-cancelled QCT of the day.
   → `phase-2-dark-pool.md` §Cross-dataset confirmation.
2. **`[FLOW:delta_notional DUCKDB]`** — net customer delta notional
   **+$10.73M long**, versus the screener's `net_flow` of **−$2,374,671**;
   UW's directional math excludes **$2,545,750 (9.5% of the tape)** as
   `mid`/`no_side`. → `phase-1-flow.md` §The classification gap.
3. **`[STRUCT:gex]` + `[HIST:intraday_range DUCKDB]`** — $217.50 carries
   net_gex **+2,344,544** (78% of summed per-strike gamma) and today's high of
   **217.1274** stopped **0.17%** short before giving back 6.10 points.
   → `phase-4-structure.md` §GEX, `phase-5-historical.md` §The 217.50 test.
4. **`[FLOW:sweep_persistence]` + `[HIST:trend]`** — `consistency_score` 0.80,
   4 of 5 sessions in the top sweep names, `total_sweep_premium` **$17,278,108**,
   `dominant_direction: "mixed"`, while price went **211.93 → 211.03**.
   → `phase-1-flow.md` §Multi-day persistence.
5. **`[AGENT:accumulation-hunter]` / `[AGENT:risk-monitor]`** — four agents
   returned **RANGE ×3, NEUTRAL ×1, zero LONG, zero SHORT**, all at conviction
   **2/5**, converging unprompted on **205.83 / 217.50**.
   → `phase-8-agent-views.md` §Agent verdicts table.
6. **`[DEBATE:bear_residual]`** — bear **0.85** vs bull **0.55**,
   `disconfirmed: true`; strongest unrefuted bear point is the unanimous
   target-cut cluster into a beat. → `phase-8b-debate.md` §Disconfirmation verdict.

---

## Key risks

1. **The fundamental bear case is un-hedgeable by the flow layer.** Three firms
   cut targets the day after a +37.1% beat (WF $300, Truist $229, **Bernstein
   $197 — 6.7% below spot**) because **sales of $1.056B missed the $1.062B
   estimate** and **FY guidance of $4.900–5.200B was affirmed against a
   $5.118B consensus** `[SENT:revision_trend]` `[SENT:news_flow]`. The bull
   conceded in phase 8b that no options or dark-pool evidence reaches this.
2. **Cash is leaving while profits are recorded.** Operating cash flow was
   **−$214,866,000 in Q1 2026 against +$346.6M of net income**, and cash fell
   **$2.4B → $1.7B in six months** as 45X credits accrue ahead of monetization
   `[FUND:operating_cash_flow]`. **Five C-suite officers sold ~720,802 shares
   on 2026-07-29**, one day before the print, with MSPR negative four straight
   months and **zero insider buying** `[FUND:insider_cluster fz]`.
3. **The entire bullish delta conclusion rests on one print's interpretation.**
   Reversing the 1,900-lot cross swings net customer delta from **+$10.73M to
   roughly −$4.5M** `[FLOW:delta_notional DUCKDB]`. Phase 2's hedge evidence is
   strong but the OI confirmation is only available on 2026-08-03
   `[OI:oi_lag DUCKDB]`.
4. **Short gamma cuts both ways.** Below the 215.03 ZGL dealer hedging
   *amplifies*; the squeeze case above 217.50 has an exact mirror below **200**
   (net_gex −465,782), where **9.89M shares short at 4.09 days to cover** do
   not help `[STRUCT:gex]` `[SENT:short_float fz semi-monthly]`.
5. **A single expected-move CPI gap can clear the stop.** −3.49% from 211.03 is
   **203.66, below the 205.83 invalidation** — the reason both structures are
   defined-risk and no stock position is proposed.
6. **There is no measured historical edge.** 90-day cumulative premium flow is
   **+0.77% of gross (`MIXED`)**, the `dark_pool_accumulation` backtest returned
   **zero signals twice**, and the `bullish_flow` 100% win rate is in-sample on
   **n = 9**, market-wide `[HIST:cumulative_premium_flow]` `[HIST:signal_backtest]`.
