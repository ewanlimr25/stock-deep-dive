# Phase 9 — Trade Blueprint

**Ticker:** MU
**As-of date:** 2026-06-23
**PM voice:** desk PM running an institutional book
**Spot reference:** $1051.77 (phase-1 screener close; intraday tape $1053–1070)
**Upstream phases cited:** phase-0.5 through phase-8b

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

MU prints postmarket tomorrow (2026-06-24) as the market's **#1 net-bearish premium name**
[CTX:universe_rank_net_dir] yet on a **balanced two-sided tape** (net flow only −$145.2M, PCR
1.013 [FLOW:insights_deep_dive]) over **exceptional, accelerating fundamentals** (EPS +412% YoY,
100% beat rate, PEG 0.287 [FUND:earnings_surprise]) — so there is **no directional edge, only a
volatility event**. The dealer book **flipped to short gamma today** with the ZGL at 1495.2 far
above spot [STRUCT:gex], meaning the priced **±10.91% move** [CTX:implied_move_pct] will *trend,
not pin*, and **all five desk agents reject a side** [AGENT:phase-8]. The only trade I'll
underwrite is a **small, defined-risk expression of the certain post-print IV crush** — explicitly
not a long or a short.

## Bias + conviction + horizon

- **Directional bias:** **NEUTRAL / RANGE** (5-of-5 agents reject a side; conviction-matrix MIXED at 4.7% [INSIGHT:conviction_matrix])
- **Conviction (M-01 bin):** **0.55**
- **Time horizon:** **1–5d** (through the 2026-06-26 weekly OPEX; the event is tomorrow PM)
- **Why this bin:** confluence is near-mixed (signals roughly cancel — bullish fundamentals/DP-mega-buy vs bearish tape/divergence/semis-sold) and the **phase-8b debate disconfirmed** (bear residual 0.60 ≥ bull 0.60), which forces the bin to the floor; phase-10 will score this in the 30–49 band.

## Entry zones

| Entry type | Price | Trigger condition | Source |
|---|---|---|---|
| Primary | $1043–1058 | Establish the defined-risk condor into the close with price holding the max-pain pivot zone | [STRUCT:max_pain] $1050 / [DP:largest] $1058 block |
| Aggressive | $1020–1043 | If MU dips to the DP support shelf pre-print, leg the bullish call spread (dip-buy w/ fundamentals) | [DP:price_levels] $1043.19 / $1020.76 |
| Fade (plan B) | < $1000 **post-print only** | Break of the put-wall with short-gamma acceleration → momentum-short continuation toward $950 (NOT a pre-print short — 7b VETOes it) | [OI:oi_by_strike] put_wall $1000 / [STRUCT:gex] −GEX shelf $950 |

## Levels to watch

| Type | Level | Source |
|---|---|---|
| Support | **$1043.19**, then **$1020.76**, then **$1000** (put-wall) | [DP:price_levels] / [OI:oi_by_strike] |
| Resistance | **$1133.99** (5-day DP shelf, +7.8%), then **$1200** (call-wall) | [DP:price_levels] / [OI:oi_by_strike] |
| Gamma flip (ZGL) | **$1495.2** (≫ spot → short-gamma everywhere realistic) | [STRUCT:gex] |
| −GEX acceleration shelf | **$950–1000** (where a downside break is chased) | [STRUCT:gex] |
| Pin magnet (06-26) | **$1050** (max-pain, dead at spot) | [STRUCT:max_pain] |

**Price-context color (advisory):** RSI 57 (neutral — today's −12% cooled the parabola) and the
name sits **−13.3% off its $1213.56 52-week high** [HIST:rsi fz] [HIST:52w_proximity fz] — neither
an overbought-blowoff to short nor an oversold-washout to chase; consistent with NEUTRAL.

## Invalidation

- **Price-based:** post-print, MU gaps and **holds outside the ±10.91% band ($937–$1166)** → the
  range/condor thesis is broken (max loss). For the optional call spread, a gap-**down** that
  closes below **$1000** (put-wall) kills the bullish leg.
- **Signal-based:** post-print, the dark pool flips to genuine **intraday** mega-distribution
  (mega `buy_ratio < 0.40` [DP:block_stratified]) **or** GEX stays negative and DEX flips
  negative as price breaks $1000 [STRUCT:dex] → directional-down regime confirmed, range dead.
- **Macro-based:** a broad **semis/AI-capex risk-off acceleration** — Tech extends today's −3.94%
  [MACRO:group_valuation fz] while SPY breaks its 50-DMA ($732 [MACRO:MarketRegime]) → the whole
  complex de-risks regardless of MU's number.

## Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** p_raw = **0.889** (phase-5 `signal_backtest_win_rate`, signal_class
  **bearish_flow**, n=**9**, source=**backtest**) → N-cap (n<10 ⇒ 0.75) → **capped p = 0.75**
  [HIST:signal_backtest]. **Caveat:** this is the *directional-short* base rate, and it is
  **VETOed by phase-7b** (you do not short an underlying compounding EPS +412% with a 100% beat
  rate) — so it does **not** authorize a position; it is recorded for the calibration loop.
- **Kelly inputs (reference, directional call-spread b):** b ≈ 1.4 (target $1200 wall vs ~$1080
  entry / stop), fraction = 0.25, cap_pct = 5.
- **Raw Kelly (directional, if p=0.75 held):** ≈ (0.75·1.4 − 0.25)/1.4 ≈ **0.32** → suggested
  ≈ min(0.32·0.25·100, 5) = **5%**. **Win-rate map ceiling:** p 0.75 ⇒ "full." *But every gate
  below cuts this, and the bias is NEUTRAL, so no directional position is taken.*
- **Range-structure Kelly (the live trade):** p(range holds) ≈ **0.60** (phase-8b bull residual),
  condor payoff b ≈ 0.47 (credit/max-loss) → **raw_kelly ≈ (0.60·0.47 − 0.40)/0.47 ≈ −0.24
  (NEGATIVE)**. A short-premium structure with a fat short-gamma tail has **negative standalone
  Kelly** → publish defined-risk **as a starter "if-forced-to-play," not a sized conviction trade.**
- **Risk gates (each cuts only):**
  - **Fundamentals (7b): VETO** → directional **short = watch-only / 0%** (improving underlying, 2/3 axes bullish).
  - **Sentiment/crowd (7c): CAUTION**, crowd_state BALANCED → **cut one size step** (knife-catch/gap risk into a binary).
  - **Correlation cluster (6/8): none** (MU is the only 2026-06-23 blueprint) → no-op (but MU *is* the semis bearish tape — not diversifiable).
  - **Sector rotation (6): ADVERSE** near-term (Tech −3.94%, −$546.7M directional outflow), persistence 0.8 → **cut half a step**.
  - **Debate (8b): DISCONFIRMED** (bull 0.60 ≤ bear 0.60) → **down-shift bin one + cut one step**.
  - **Context (0.5): GENUINELY_UNUSUAL** → no-op on `p`, but the unusualness is *event-driven* → size for the binary, not the magnitude.
- **Final size: 0% — WATCH-ONLY / no sized position.** Negative range-Kelly (−0.24) means the
  Kelly ceiling is 0, and an upward deviation is *forbidden* because gates fired (sentiment
  CAUTION, sector adverse, debate disconfirmed) — so the disciplined call is **no sized bet into
  the binary.** Directional size is also 0% (NEUTRAL bias + 7b short-VETO).
  - **If forced to engage:** the defined-risk iron condor below is the only sanctioned expression,
    capped at **≤1.0% of book risk** (starter), explicitly marked "if-forced-to-play" — *not* a
    recommended position. The bull call spread is optional/illustrative only.
- **Deviation reason:** none (an upward deviation is forbidden — gates fired; final = 0% honors the negative Kelly).

## Option structures

### Directional (required by template; **OPTIONAL / small** — the fundamentals-aligned expression IF you must lean, on a *beat*)

- **Structure:** **bull call debit spread** (defined-risk; chosen over a naked call to blunt the post-print IV crush — net vega is long−short, far lower than a naked long)
- **Strike(s) / expiry:** **buy 1080C / sell 1200C, expiry 2026-07-17** (short leg = the $1200 call-wall [OI:oi_by_strike]; 07-17 monthly gives post-print follow-through time and lower relative crush than 06-26)
- **Debit/credit:** ~**$50 debit** (illustrative — no live quote; high pre-print IV keeps the spread rich)
- **Breakeven:** ~**$1130**
- **Max loss:** **~$50 (the debit)**; max gain ~$70 (width $120 − debit)
- **Why this structure:** expresses the bullish fundamental case (PEG 0.287, 100% beat rate, analyst strong-buy 1.35 [FUND]) on a beat while the short 1200 leg caps at resistance and finances IV; IV percentile is 100 [HIST:iv_percentile_zscore], so I will **not** buy a naked call into the crush. **Only if you choose to lean long — the base recommendation is NEUTRAL.**

### Defined-risk alternative (the **only sanctioned "if-forced-to-play" expression** — short the IV-100 crush, range-bound; ≤1% book risk, NOT a recommended position)

- **Structure:** **iron condor** centered on max-pain $1050, short strikes **outside** the ±10.91% band, long wings for defined risk (NO naked premium — disallowed by the sizing rubric)
- **Strike(s) / expiry:** **sell 935P / buy 905P** and **sell 1170C / buy 1200C, expiry 2026-06-26** (short 935/1170 just beyond the $937/$1166 expected-move edges; long 905/1200 define risk; 1200 = call-wall [OI:oi_by_strike]; 06-26 = the 19.4%-OI gravity expiry [OI:term_structure] to capture the crush)
- **Debit/credit:** ~**$11 credit** (illustrative)
- **Breakeven:** ~**$924 / ~$1181**
- **Max loss:** **~$19 per side** (width $30 − ~$11 credit; only one side can lose) — size so this max-loss ≤ ~1.0% of book risk
- **Why this structure:** harvests the **certain post-print IV crush** (IV30d 107% → far-lower realized on a clean beat) [STRUCT:front_end_iv_ratio] and the **$1050 max-pain pin** [STRUCT:max_pain]; defined wings cap the short-gamma breach the phase-8b bear flagged. **Half/starter size — the move can exceed ±10.9% (implied is a floor, not a ceiling).**

## Macro overlay (cite phase-6)

- **Tailwinds:** [MACRO:T10Y2Y] 2s10s +0.34 (normal, steepening — benign); [MACRO:CPILFESL] core CPI +2.82% YoY (toward target); [MACRO:sector_flow_persistence] Tech 5-day net **inflow** 0.8 (structural, not abandoned).
- **Headwinds:** [MACRO:MarketRegime] regime **TRANSITIONAL** ("half size, defined-risk, iron condors"); [MACRO:group_valuation fz] Tech **−3.94% today**; [MACRO:sector_flow] semis net directional **outflow −$546.7M**; [MACRO:DGS10] 10y 4.51% (valuation drag on a 49× / +268%-YTD name).
- **Net:** **mild-to-moderate headwind** — but the binary earnings event dominates; macro is a *size-down* argument, not a direction.

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|---|---|---|
| **2026-06-24 (postmarket)** | **MU fiscal-Q3 earnings** (THE catalyst, ±10.91% priced) | ? (binary) |
| 2026-06-26 | Post-earnings **weekly OPEX** (max-pain $1050, 19.4% of OI, PCR 2.13) | ? (gamma/pin resolution) |
| ~2026-07 (TBD) | Next FOMC / CPI (dates not confirmable on this as-of) | secondary to the print |

## Post-trade monitoring checklist

- [ ] **Tomorrow PM:** read the actual print + guidance vs the +27.3% last-surprise / 100% beat-rate base; mark the gap against the ±10.91% band ($937–$1166).
- [ ] **Post-print:** re-check GEX regime — does it stay NEGATIVE (trend-amplify) or flip back POSITIVE (pin)? [STRUCT:gex] daily refresh.
- [ ] **Daily:** re-pull dark-pool block-stratified — does mega-tier buying continue **intraday** (genuine accumulation) or was the $553M block a one-off post-close print? [DP:block_stratified]
- [ ] **Into 06-26:** watch the $1050 max-pain pin vs the $1000 put-wall / $1133 resistance — manage/close the condor before the OPEX gamma unwind if held.
- [ ] **Sector:** monitor semis (NVDA/AMD/AVGO) + SOXL — if the "AI-capex/memory-selloff" narrative [SENT:company_news] accelerates, the whole complex moves together (MU is not diversifiable here).

## Citations summary (M-04 — ≥3 distinct upstream datapoints, phase-10 spot-checks these)

1. `[FLOW:insights_deep_dive]` net flow −$145.2M, PCR 1.013 — phase-1-flow.md §Whole-tape aggregate
2. `[STRUCT:gex]` GEX NEGATIVE, ZGL 1495.2 ≫ spot $1053.58 — phase-4-structure.md §GEX
3. `[STRUCT:max_pain]` 06-26 max-pain $1050 (−0.13%) — phase-4-structure.md §Max pain
4. `[FUND:earnings_surprise]` 100% beat rate (4/4), EPS +412% YoY, PEG 0.287 — phase-7b-fundamentals.md
5. `[CTX:implied_move_pct]` ±10.91% expected move — phase-0.5-context.md §Verdict
6. `[HIST:signal_backtest]` bearish_flow win_rate 0.889 (n=9) — phase-5-historical.md §Sizing handoff
7. `[AGENT:phase-8]` 5-of-5 reject a direction; earnings-scout RANGE conv 4 (sell-vol) — phase-8-agent-views.md
