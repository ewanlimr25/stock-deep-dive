# Phase 9 — Trade Blueprint

**Ticker:** NTAP
**As-of date:** 2026-05-22
**PM voice:** desk PM running an institutional options-overlay book
**Spot reference:** $139.36 (phase-2 dark-pool close / phase-4 underlying)
**Upstream phases cited:** phase-0.5 through phase-8b

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

NetApp ripped **+12.4% on 5/22** on a genuine Google-Cloud-AI / Red-Hat / Iterate.ai
catalyst into its **5/28 earnings**, but the options tape is **selling the rally, not
buying it** — the marquee print is the **145C 6/18 sold on the bid for $2.86M**
[FLOW:sweeps], net call *and* put premium are negative [FLOW:aggressor_ex0dte DUCKDB],
OI is static [OI:biggest_increases], and the whole-tape flow has stayed **net-bearish
(−$1.75M, 21/30 days) through a +41.6% rally** [INSIGHT:price_vs_flow], [HIST:cumulative_premium_flow].
With **IV rank 100 / VRP +13.3** [HIST:vrp] and the stock **above the entire analyst
target range ($88–137, consensus $115–118)** [SENT:analyst_targets], the edge is
**selling rich premium with a downside skew, defined-risk**, not a directional bet —
the cleaner fade is *post-print*, because a beat can gap it through the 145 dealer wall
first ([DEBATE:bear_residual] strongest unrefuted point).

## Bias + conviction + horizon

- **Directional bias:** **NEUTRAL** (vol-sell / range with a downside fade skew; the
  desk is 0/5 for a long, 2 SHORT / 2 NEUTRAL / 1 RANGE — no directional conviction
  into the binary).
- **Conviction (M-01 bin):** **0.65** (moderate edge with real disconfirming evidence —
  the genuine AI catalyst + sector inflow + 60% vol-realisation cap a higher bin).
- **Time horizon:** **1-4w** (structures to 6/18; thesis resolves at/after the 5/28 print).
- **Why this bin:** the instrumentation is unanimous that there is *no directional
  long* and the premium is rich, but the binary gap risk + aligned Tech inflow keep
  conviction moderate, not high — matched to phase-10's confluence band (see phase-10).

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| Primary | $139–143 | Sell defined-risk premium at/below the **145 gamma-wall cap**; richer credit if it tags 143–145 | [STRUCT:gex] |
| Aggressive | $145 | Tag of the **145 wall / overwrite strike** — sell the call side into strength | [FLOW:sweeps], [STRUCT:gex] |
| Fade (plan B) | >$145 sustained | If NTAP closes >145 twice on **rising net-call-buying + fresh OI**, stand down the fade; the only bull tell ($1.51M LEAP calls) is in control | [FLOW:delta_notional DUCKDB] |

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Support | **$125** (gamma wall +488K; top of the $119–124 DP shelf) | [STRUCT:gex], [DP:price_levels] |
| Support (pivot) | **$134** (today's DP blocks ~$13M) | [DP:price_levels] |
| Resistance | **$145** (gamma wall +392K, 145C overwrite, > all analyst targets) | [STRUCT:gex], [FLOW:sweeps] |
| Gamma flip (ZGL) | **$115.41** (below = short-gamma vol expansion) | [STRUCT:gex] |
| De-facto pin/cap | **$145** (largest fresh-traded strike; no OPEX-week pin) | [OI:decrease_with_volume] |

## Invalidation

- **Price-based:** **Two daily closes above $145** (the gamma wall + above the highest
  analyst target $137) → the fade/neutral thesis is broken and the AI-breakout is in
  control. [STRUCT:gex], [SENT:analyst_targets]
- **Signal-based:** **Cumulative premium flow turns net-bullish for 3 consecutive
  sessions** (reversing the −$1.75M / 21-of-30-day bearish divergence), OR
  `insights_conviction_matrix` flips to DIRECTIONAL_LONG with a real OI build. [HIST:cumulative_premium_flow], [INSIGHT:conviction_matrix]
- **Macro-based:** **A clean 5/28 earnings beat that holds NTAP above the +10.6%
  implied move (~$154) and validates the AI narrative** — the [DEBATE:bear_residual]
  point; this is the single event that turns the fade into a chase. [MACRO:NTAP_earnings]

## Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** p_raw = **0.60** (phase-5 `high_iv_rank` **vol-realisation**
  rate, n=**10**, source=**backtest**) → N-cap (10≤n<20)=0.85 → **capped p = 0.60**
  `[HIST:signal_backtest]`.
  - **Critical interpretation:** 0.60 is a *vol-realisation* rate ("the move shows up"),
    **not** a directional win-rate. For the **range/vol-sell** structure the effective
    win-rate is ~**0.40** (the move materialises against a pinned condor 60% of the
    time) → this lands in the **win-rate-map "starter/skip" zone** and triggers the
    `p<0.50` caution. For the **directional fade** skew, 0.60 "move happens" + price
    above all targets tilts the realised move down but remains a binary gamble.
- **Kelly inputs:** b = **0.85** (iron-condor credit $2.3 / max-loss $2.7), fraction = 0.25, cap_pct = 5.
- **Raw Kelly:** at nominal p=0.60, b=0.85 → (0.60×0.85 − 0.40)/0.85 = **0.135** →
  suggested = 0.135×0.25×100 = **3.4%**; **win-rate-map ceiling (p 0.50–0.70) = half =
  2.5%** → take the smaller = **2.5%**. The effective-0.40 range-sell read pulls the
  honest pre-gate ceiling to **starter (~1.5%)**.
- **Risk gates (each can only cut):**
  - **Fundamentals (7b): NA** (no Finnhub key) → no-op; carry the FCF −20% / above-target risks.
  - **Sentiment/crowd (7c): CAUTION** + crowd_state CROWDED_LONG → **cut one step** (half→starter).
  - **Correlation (6/8): none** (tool returned no usable coefficients; ENPH/SYM different industries) → no-op.
  - **Sector rotation (6): ADVERSE to this fade** — Tech net flow +$6.19B persistence 1.0 is *aligned to a long*, therefore *adverse to a fade* → **cut half a step**. [MACRO:sector_flow_persistence]
  - **Debate (8b): bull_residual 0.65 vs bear_residual 0.55 → disconfirmed = FALSE** → no-op.
  - **Context (0.5): GENUINELY_UNUSUAL (event/vol)** → no-op on the modifier.
- **Final size:** **~1.0% of book risk (STARTER, defined-risk max-loss only).** Deviated
  *down* from the 2.5% map ceiling via the effective-p reinterpretation + sentiment +
  sector gates (downward deviation needs no reason).
- **Deviation reason (if any):** none (downward only).

## Option structures

### Directional (fade skew) — Bear call spread

- **Structure:** Bear call spread (sell 145C / buy 155C) — defined-risk credit, bearish.
- **Strike(s) / expiry:** **145C / 155C, 2026-06-18** (145 = gamma wall + overwrite
  strike + above all analyst targets; 155 ≈ top of the implied-move range).
- **Debit/credit:** **credit ≈ $3.2** (illustrative; 145C ~$6.0 / 155C ~$2.8).
- **Breakeven:** **$148.2** (145 + 3.2).
- **Max loss:** **$6.8** (width 10 − credit 3.2).
- **Why this structure:** Sells the exact strike institutions are overwriting into IV
  rank 100 [FLOW:sweeps]; a credit (not debit) structure so the post-earnings vol crush
  works *for* you [STRUCT:vanna_charm]. Wins on a pin/fade below 145; defined-risk caps
  the up-gap to the strongest_bear_point scenario.

### Defined-risk alternative (primary recommendation) — Iron condor

- **Structure:** Iron condor — sell 150C / buy 155C **and** sell 125P / buy 120P.
- **Strike(s) / expiry:** **120/125P – 150/155C, 2026-06-18** (short strikes ≈ the
  ±10.6% implied-move edges; long wings at the gamma walls 125/ and beyond 150).
- **Debit/credit:** **credit ≈ $2.3** (illustrative).
- **Breakeven:** **~$122.7 and ~$152.3** (short put − credit / short call + credit).
- **Max loss:** **~$2.7 per side** (width 5 − credit 2.3).
- **Why this structure:** The dealer **long-gamma pin** [STRUCT:gex] + **VRP +13.3 /
  IV rank 100** [HIST:vrp] reward selling both wings into the crush; profits if NTAP
  settles in the **$122.7–$152.3** band (i.e. the move stays *inside* the priced
  ±10.6%). **Caveat: the 60% vol-realisation [HIST:signal_backtest] means this is
  breached more often than not — hence STARTER size and defined wings only.**

**Expected-move check (N4):** front-expiry implied move **±10.64% / ±$14.82** (~$124.5–
$154.2) [CTX:implied_move_pct]. Both structures are sized so a single-catalyst gap of
the full expected move = the *defined* max loss (≤1% of book) — the gap cannot exceed
the stop because the risk is capped by construction. **Preferred execution: wait for
the 5/28 print and fade the vol crush / mean-reversion toward $115–125, rather than
carrying naked exposure through the binary** (contrarian + risk-monitor, phase-8).

## Macro overlay (cite phase-6)

- **Tailwinds (to the name, adverse to the fade):** Tech sector net flow **+$6.19B,
  persistence 1.0** [MACRO:sector_flow_persistence]; genuine AI/cloud capex catalyst
  [MACRO:NTAP_news_2026-05-22].
- **Headwinds (support the fade):** spot **$139.36 > bull-case $125 / all targets**,
  **JPMorgan downgrade → Neutral $110** [MACRO:NTAP_analysts_2026-05-22]; **TRANSITIONAL
  regime — half size, defined-risk** [MACRO:MarketRegime_2026-05-22]; macro neutral
  (core CPI +2.74%, 10y 4.57%) [MACRO:CPILFESL_2026-04 FRED].
- **Net:** **mixed** — a real continuation tailwind sits against a valuation-overshoot /
  distribution headwind; resolves on 5/28.

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|------|-------|------------------|
| **2026-05-28 (AMC)** | **NTAP fiscal Q4 earnings** (Street EPS $2.27, guide rev $1.87B) | **?** (binary, ±10.6% priced) |
| 2026-05-27 / 06-01 | Storage peers HPQ / HPE report | ? (sector read-through) |
| ongoing | AI/cloud capex narrative | + (sector tailwind) |

## Post-trade monitoring checklist

- [ ] **Daily: cumulative premium flow** — does it flip net-bullish 3 sessions (invalidation)? [HIST:cumulative_premium_flow]
- [ ] **Daily: 145 level** — two closes above = fade broken; re-check 145C OI for a real build vs overwrite. [STRUCT:gex], [OI:decrease_with_volume]
- [ ] **Phase-4 refresh: DEX/GEX + ZGL** — a break of ZGL $115.41 flips to short-gamma (vol expansion downside). [STRUCT:gex]
- [ ] **5/28 AMC: trade the crush, not the gap** — let IV collapse, then assess mean-reversion toward $115–125; negative vanna = dealer de-hedge selling. [STRUCT:vanna_charm]
- [ ] **Dark pool: $119–124 shelf** — does institutional bid defend on a pullback, or distribute? [DP:price_levels]

## Citations summary (M-04 — phase-10 spot-checks these)

1. **[FLOW:sweeps]** — 145C 6/18 sold on the bid **$2,858,466 / 4,851 ctr** (phase-1-flow.md §Sweeps) — *today's tape, premium harvest not accumulation.*
2. **[SENT:analyst_targets]** — spot **$139.36 above the entire target range $88–137**, consensus $115–118, JPM Neutral $110 (phase-7c-sentiment.md §Analyst-revision) — *positioning/valuation.*
3. **[HIST:vrp]** — **VRP +0.1332** (IV30 57.6% vs realised 44.2%), PREMIUM_SELLING; IV rank 100 (phase-5-historical.md §IV regime) — *historical/vol context.*
4. **[STRUCT:vanna_charm]** — net vanna **−817** → post-earnings crush forces dealer de-hedge selling (phase-4-structure.md §Vanna) — *dealer structure.*
5. **[INSIGHT:price_vs_flow]** — DIVERGENCE: price **+41.6%** vs net-bearish flow (phase-7-insights.md §Price vs flow) — *UW composite.*
