# Phase 9 — Trade Blueprint

**Ticker:** RKT
**As-of date:** 2026-06-05
**PM voice:** desk PM running an institutional book
**Spot reference:** $12.65 (screener close, phase-0.5-context.md §Sector read)
**Upstream phases cited:** phase-0.5 through phase-8b
**Generated:** 2026-06-06T18:50:00-04:00

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

RKT is a **fundamentals-vetoed tactical short into the June 30 unlock**: the
day's tape was distribution-shaped — calls net-sold 12,773 bid vs 8,042 ask and
puts net-bought 7,706 vs 3,119 ex-0DTE [FLOW:aggressor_ex0dte DUCKDB] — beneath
a price with **no dark-pool shelf below $12.65** [DP:price_levels] and a dealer
gamma cushion that has collapsed 97% in five sessions (47.6M → 1.33M)
[HIST:gex_time_series]. Macro is a 4/5 headwind for a mortgage originator —
30y at 6.59–6.69% and rising off the 6.09% low [MACRO:Mortgage30Y_2026-06-05]
— with a dated supply event (L-1 unlock 2026-06-30) standing over a stock
2.18% above its 52-week low [HIST:52w_proximity fz]. But the desk split 2-2
[AGENT], the business is improving (4/4 beats, VETO on naked shorts)
[FUND:earnings_surprises], and the debate did not clear the trade
(0.65 vs 0.65) [DEBATE:bear_residual] — so this is a **carry-size, defined-risk
put spread only**, not a conviction short.

## Bias + conviction + horizon

- **Directional bias:** SHORT (plurality of phases 1–8; gates cut, never set)
- **Conviction (M-01 bin):** **0.55**
- **Time horizon:** 1-4w (into and through the 06-30 unlock)
- **Why this bin:** anticipated phase-10 confluence ≈ 50 (band 50–64 → 0.65)
  down-shifted one bin by the phase-8b disconfirmation gate
  (bear_residual 0.65 ≥ bull_residual 0.65) — phase-10 to verify.

## Entry zones

| Entry type | Price | Trigger condition | Source |
|---|---|---|---|
| Primary | $12.85 | rejection inside the $12.94–12.96 DP supply band (~$135M transacted) on a dead-cat bounce | [DP:price_levels] |
| Aggressive | $12.62 | first hourly close below the $12.65 close-shelf (6.4M sh) confirming shelf failure — accepts chase risk at the 52w low | [DP:price_levels] [HIST:52w_proximity fz] |
| Fade (plan B, counter-trade) | $13.55 | reclaim-and-hold above $13.50 — GEX flips positive there; flip LONG for the vanna squeeze toward the $14/$14.5 max-pain magnets | [STRUCT:gex] [STRUCT:max_pain] [STRUCT:vanna_charm] |

Price-context color (advisory): RSI(14) 37.69 and spot **+2.18% off the 52-week
low** [HIST:rsi fz][HIST:52w_proximity fz] — this is a late-trend short; prefer
the primary (bounce-fade) entry over the aggressive one. Color only — does not
alter `p` or size.

## Levels to watch

| Type | Level | Source |
|---|---|---|
| Support (shelf) | $12.65 — today's close shelf, $81.0M / 6.4M sh; nothing documented beneath | [DP:price_levels] |
| Support (last) | $12.38 — 52-week low; below it is air (no put wall in top-10 strikes below spot) | [HIST:52w_proximity fz] [OI:oi_by_strike] |
| Resistance 1 | $12.94–12.96 — ~$135M DP band | [DP:price_levels] |
| Resistance 2 | $13.17–13.26 — ~$163M DP band (the week's heaviest supply) | [DP:price_levels] |
| Gamma flip (local) | $13.50 — first positive net_gex strike (+461,592); aggregate ZGL 7.71 is a coarse far-OTM crossing, not tradeable | [STRUCT:gex] |
| Pin magnet | $14.0 (Jun-12) / **$14.5 (Jun-18 OPEX, 23.77% of all OI)** — native max-pain values | [STRUCT:max_pain] [OI:term_structure] |
| Amplifier strike | $13.0 — largest \|GEX\| on the surface (net −4.59M): friction/acceleration, not support | [STRUCT:gex] |

## Invalidation

- **Price-based:** two consecutive daily closes above **$13.26** (top of the
  $163M DP band [DP:price_levels]); tighter early-warning: reclaim-and-hold of
  $13.50 (gamma flip [STRUCT:gex]) intraday without giving it back.
- **Signal-based:** cumulative premium flow turns **net bullish for 3
  consecutive sessions** [HIST:cumulative_premium_flow], or the ex-cross
  dark-pool buy ratio (block-stratified, closing crosses excluded) prints
  ≥ 0.55 two sessions running [DP:block_stratified] — the distribution leg of
  the thesis is then dead.
- **Macro-based:** dovish surprise at **FOMC 2026-06-16/17** or a soft May CPI
  (~06-10) that compresses VIX from 21.51 — falling IV arms the dealer vanna
  squeeze ("dealers short puts cover by BUYING underlying"
  [STRUCT:vanna_charm]) [MACRO:FOMC_2026-06-16].
- **Exit rule:** **hard stop** (debit structure): close 100% on the price-based
  trigger, or immediately on the macro trigger if $13.50 is reclaimed the same
  session.

## Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** p_raw = **0.875** (bearish_flow, n=**8**,
  source=backtest, market-wide base rate — not RKT-specific) → N-cap for n<10
  is 0.75 → **capped p = 0.75** [HIST:signal_backtest]
- **Kelly inputs:** entry 12.65 / stretch target 11.95 / stop 13.25 →
  b = |12.65−11.95| / |13.25−12.65| = 0.70/0.60 = **1.17**; fraction = 0.25;
  cap_pct = 5
- **Raw Kelly:** (0.75×1.17 − 0.25)/1.17 = **0.536** → suggested =
  min(0.536 × 0.25 × 100, 5) = **5.0%** · **Win-rate map ceiling:** p ≥ 0.70 →
  full (≤ cap_pct) — no conflict pre-gates
- **Risk gates (each cuts only; applied in order):**
  1. **Fundamentals (phase-7b): VETO** → naked directional short =
     **watch-only / 0%**; defined-risk carry structure allowed, marked
     "fundamentals-vetoed, carry only" [FUND:tier_adjustment]
  2. **Sentiment/crowd (phase-7c): CAUTION** (improving analyst revisions
     SB 4→6 vs the bear thesis; crowd_state BALANCED) → cut one size step:
     carry 5.0% → 2.5% [SENT:recommendation]
  3. **Correlation cluster (phase-6/8): none** — no RKT pair ≥ 0.70
     (CRM/NOW/PATH cluster excludes RKT) → no-op
     [MACRO:portfolio_correlation]
  4. **Sector rotation (phase-6): neutral** (conflicting lenses) → no-op
     [MACRO:sector_flow_persistence]
  5. **Debate (phase-8b): bull_residual 0.65 vs bear_residual 0.65 →
     disconfirmed = true** → conviction bin 0.65 → 0.55 AND cut one size step:
     2.5% → **1.0% (starter)** [DEBATE:bear_residual]
- **Context modifier (phase-0.5):** `BUSY_NAME_NORMAL_DAY` → top-of-band sizing
  forbidden — already at starter, consistent [CTX:unusual_verdict]
- **Final size: directional = 0% (watch-only — the 7b VETO zeroes the
  directional envelope; `decision.json` `final_size_pct = 0.0`).** The only
  permissible expression is the defined-risk put-spread **carry**, budgeted at
  max-loss ≤ **1.0% of book risk** (the post-gate starter step: 5.0 → 2.5 (7c)
  → 1.0 (8b)), marked "fundamentals-vetoed, carry only".
- **Deviation reason:** none (upward deviation forbidden — gates fired).

## Option structures

Expected-move anchor (N4): front-expiry implied move **±1.198% / $0.1514**
[CTX:implied_move_pct]. Scaled to the Jul-17 expiry (~6 weeks, √6 ≈ 2.45):
≈ ±2.9% ≈ ±$0.37. First target $12.38 (−2.1%) sits inside the priced move;
the stretch target $11.95 (−5.5%) is ~1.9× it — rich, which is another reason
this is carry-sized only. A single-catalyst gap of expected-move magnitude
(~±3%) does not exceed the stop (+4.7% away) and max loss is the debit —
catalyst-gap check passes.

### Directional (primary) — fundamentals-vetoed, carry only

- **Structure:** put debit spread (long put vertical)
- **Strike(s) / expiry:** long $12.5P / short $11P, **2026-07-17** (42 DTE —
  clears CPI 06-10, FOMC 06-16/17 and the 06-30 unlock; expires before the
  07-30 earnings, so no IV-crush exposure [MACRO:catalyst_calendar])
- **Debit/credit:** ≈ **$0.58 debit** (estimated off the as-of surface: Jun-18
  12.5P marked ~$0.56–0.60 at IV ≈ 0.61 [FLOW:greek_screener]; Jul-17 ATM IV
  0.5924 [STRUCT:iv_term_structure] — illustrative, not a quote)
- **Breakeven:** $11.92 at expiry
- **Max loss:** $0.58/spread — position sized so total debit ≤ **1.0%** of book risk
- **Max value:** $1.50 (payoff ≈ 1.6:1 at the stretch target)
- **Why this structure:** VRP −0.0852 says **buy** premium, not sell it
  [HIST:vrp], and IV is at its 15.4 percentile [HIST:iv_percentile_zscore] —
  debit structures are the cheap expression; the long 12.5 strike sits on the
  −0.82M GEX shelf where downside accelerates [STRUCT:gex], the short 11
  monetizes the post-12.38 air pocket without paying for the tail.

### Defined-risk alternative — the cap-harvest (no downside break required)

- **Structure:** call credit spread (bear call vertical) — sells the
  most-corroborated wall in the stack
- **Strike(s) / expiry:** short $14.5C / long $16C, **2026-07-17**
- **Debit/credit:** ≈ **$0.25 credit** (est.: Jul-10 14.5C printed $0.32
  [FLOW:top_premium_trades]; Jul-17 14.5C ≈ $0.40, 16C ≈ $0.15 — illustrative)
- **Breakeven:** $14.75 (+16.6% from spot)
- **Max loss:** $1.25/spread (width 1.50 − credit 0.25) — max-loss ≤ 1.0% of
  book risk if used instead of the put spread
- **Why:** $14.5 is Jun-18 max-pain + a +1.75M GEX wall + a 20,045-contract
  call wall + the day's fresh 3,460-lot institutional short-call line
  [STRUCT:max_pain][STRUCT:gex][OI:oi_by_strike][FLOW:top_premium_trades];
  this wins on down, flat, and mildly-up tapes. Honest tension: it sells
  premium into a negative-VRP regime [HIST:vrp] — the edge here is the wall
  structure, not the vol level; keep it small.

## Macro overlay (cite phase-6)

- **Tailwinds (for the short):** 30y mortgage 6.588–6.69% rising off the 6.09%
  2026 low [MACRO:Mortgage30Y_2026-06-05]; CPI +3.78% YoY re-accelerating
  [MACRO:CPIAUCSL_2026-04]; U-Mich record-low 44.8 [MACRO:UMich_2026-05-22];
  regime "TRANSITIONAL — reduce position size" with VIX 21.51 +40% d/d
  [MACRO:MarketRegime_2026-06-05 UW]; L-1 unlock 06-30
  [MACRO:RKT_L1_unlock_2026-06-30].
- **Headwinds (against the short):** Fed already at 3.62% with cut optionality
  [MACRO:DFF_2026-06-04 FRED]; solid labor (+172k) [MACRO:PAYEMS_2026-05 FRED];
  Financial sector cheap at 17.4×/14.1× fwd and resilient Friday (−0.39% vs
  Tech −6.11%) [MACRO:group_valuation fz EOD]; soft USD
  [MACRO:DTWEXBGS_2026-05-29 FRED].
- **Net:** **headwind for RKT** (= tailwind for this short), conviction 4/5
  per phase-6.

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|---|---|---|
| ~2026-06-10 | May CPI release | ? (hot = − for RKT; soft = squeeze risk) |
| 2026-06-16/17 | FOMC (Warsh) + SEP | ? (priced no-change; language binary) |
| 2026-06-18 | Monthly OPEX — 23.77% of RKT OI rolls; $14.5 max-pain | ? (pin/unwind) |
| ~2026-06-26 | May PCE | ? |
| 2026-06-30 | **Class L-1 transfer-restriction expiry (share unlock)** | − |
| late June | Russell reconstitution | ? (mechanical) |
| weekly Wed | MBA mortgage apps / 30y rate path | ? |

## Post-trade monitoring checklist

- [ ] **Monday OI confirm:** did Jul-10 $14.5C OI print ≈ +3,400 (confirming
  the opening short [FLOW:top_premium_trades]) and did Sep-18 $13C keep
  building [OI:biggest_increases]? A failure to confirm weakens the cap thesis.
- [ ] **Ex-cross DP buy ratio daily** [DP:block_stratified] — ≥0.55 two
  sessions = signal invalidation firing.
- [ ] **VIX vs 21.51 daily** — a slide toward 17–18 arms the vanna squeeze
  [STRUCT:vanna_charm]; tighten or exit the put spread before FOMC if VIX is
  already compressing.
- [ ] **GEX refresh on phase-4 dailies** — a reclaim of $13.5 flips the local
  surface positive [STRUCT:gex]; that is the fade-entry trigger, not a hold.
- [ ] **30y mortgage prints (daily) + MBA apps (Wed)** [MACRO:Mortgage30Y] —
  a drop back through ~6.3% guts the macro leg.
- [ ] **Unlock newsflow into 06-30** — any S-3/registration or RHI distribution
  detail changes the supply math [MACRO:RKT_L1_unlock_2026-06-30].

## Citations summary

1. `[FLOW:aggressor_ex0dte DUCKDB]` — calls 8,042 ask vs 12,773 bid; puts 7,706
   ask vs 3,119 bid (ex-0-1DTE) — phase-1-flow.md §DuckDB §A
2. `[DP:price_levels]` — no DP cluster below $12.65; $12.94–12.96 ≈ $135M and
   $13.17–13.26 ≈ $163M overhead — phase-2-dark-pool.md §Price levels
3. `[HIST:gex_time_series]` — total GEX 47,609,090 → 1,333,718 in 5 sessions
   (−97%) — phase-5-historical.md §GEX time series
4. `[MACRO:Mortgage30Y_2026-06-05]` — 30y 6.588%/6.69% rising from 6.09% low —
   phase-6-macro.md §Sector overlay
5. `[HIST:signal_backtest]` — bearish_flow win_rate 87.5% (n=8, market-wide) →
   capped p 0.75 — phase-5-historical.md §Signal backtest
6. `[FUND:earnings_surprises]` + `[DEBATE:bear_residual]` — 4/4 beats; debate
   0.65 vs 0.65 disconfirmed — phase-7b §Earnings-surprise / phase-8b §Verdict
