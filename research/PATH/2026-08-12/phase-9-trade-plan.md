# Phase 9 — Trade Blueprint

**Ticker:** PATH
**As-of date:** 2026-08-12
**PM voice:** desk PM running an institutional book
**Spot reference:** $15.26 (close, [FLOW:insights_deep_dive] / [HIST:trend])
**Upstream phases cited:** phase-0.5 through phase-8b

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

PATH sits at $15.26 after a +32.2% six-week rally built on a rare 29-of-30-
session OI-build streak inside an unbroken long-gamma dealer regime
[HIST:oi_trend][STRUCT:gex], but today's price-vs-flow reading shows an
outright divergence (price +32% vs. today's bearish flow)
[INSIGHT:price_vs_flow] right as phase-7b's fundamentals gate **vetoes** the
long on a fresh earnings miss and an insider-sentiment reading at its most
bearish level ahead of the 2026-09-03 print [FUND:insider_MSPR]. With
`market-regime`'s own guidance explicitly recommending "iron condors in
range" [MACRO:MarketRegime_2026-08-12] and phase-8's desk landing 4-of-5
NEUTRAL with zero LONG verdicts [AGENT:accumulation-hunter], the actionable
read here is defined-risk and range-bound, not a chase of either direction.

## Bias + conviction + horizon

- **Directional bias:** **RANGE** (mild bearish tilt if forced to pick a
  side — see Conviction deviation below)
- **Conviction (M-01 bin):** **0.55**
- **Time horizon:** 1-4w
- **Why this bin:** Phase-10's confluence score (pre-computed here, formally
  scored in phase-10) lands at **59/100** — the 50–64 band maps to a 0.65
  bin per `rubrics/confluence-scoring.md`, but phase-8b's debate-
  disconfirmation gate (`disconfirmed=true`) separately mandates a further
  one-step down-shift per `rubrics/sizing-rubric.md` §"Risk gates" #5 — see
  the deviation note.

## Conviction deviation

Phase-10's confluence-score band alone would place this at **0.65**. This
plan uses **0.55** instead, per the *sizing rubric's* explicit, separate
instruction that a `phase-8b disconfirmed=true` result "down-shift[s] the
conviction bin by one **and** cut one size step" — distinct from (and
compounding with) the −5-point penalty the confluence-score formula already
applies for the same fact. Both rubrics are followed literally rather than
treating the score-level penalty as already sufficient: bull_residual 0.65
vs. bear_residual 0.75 [DEBATE:bear_residual] means the adversarial pass did
not clear the trade, and the sizing rubric treats that as an independent,
compounding cut. This is not a discretionary deviation — it is the two
rubrics' rules applied as literally written.

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| Primary | Current ($15.26) | Sell the condor at spot — no better entry signal justifies waiting, given `BUSY_NAME_NORMAL_DAY` context (no unusual flow to time against) | [CTX:unusual_verdict, phase-0.5] |
| Aggressive | $15.75–$16.00 | Wait for a retest of the near-term call-wall zone to sell the call side at richer premium | [OI:oi_by_strike] `call_wall_resistance` $16.00 |
| Fade | Close above $16.50, 2 daily closes | Counter-trade: if the range breaks up through the condor's short call, cover that leg and consider a small structural-long call spread toward the $18.00 wall instead of fighting a confirmed breakout | [OI:oi_by_strike] $18.00 `call_wall_resistance` (largest near-term OI) |

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Support | $14.86–$14.87 (near); $13.89–$13.93 (hard) | [DP:price_levels] |
| Resistance | $16.00 (near); $16.50 (condor short-call strike) | [OI:oi_by_strike] `call_wall_resistance` |
| Gamma flip | $13.80 (nearest-expiry `today_zero_gamma`) | [STRUCT:today_gamma_flip] |
| Largest near-term pin/magnet | $11.00 (2026-08-21 max-pain, largest near-dated OI book, 98,917 contracts) | [STRUCT:max_pain] |
| Price context (advisory) | RSI(14)=70.94 (overbought); price −23.08% below the 52-week high, +65.87% above the 52-week low | [HIST:rsi fz][HIST:52w_proximity fz] |

RSI at 70.94 while price sits meaningfully below its own 52-week high is a
stretched-but-not-euphoric read — it colors the entry timing (don't chase a
pop toward $16 for a fresh long) but does not change sizing.

## Invalidation

- **Price-based:** Two consecutive daily closes below **$13.89** (breaks the
  hard dark-pool support and the level every phase-8 agent independently
  flagged as the accumulation-thesis floor) OR two consecutive daily closes
  above **$16.50** (breaks the condor's short-call strike and the near-term
  OI resistance ladder) [DP:price_levels][OI:oi_by_strike].
- **Signal-based:** The dealer book flips to `NEGATIVE` (short) gamma on a
  phase-4 daily refresh while spot holds inside the range — this would mean
  the long-gamma mean-reversion mechanic this whole plan leans on has broken
  [STRUCT:gex]. Secondary trigger: `institutional-accumulation` flips from
  `ACCUMULATION` to a clean distribution read on a fresh pull (not the
  artifact-affected one from this run) [INSIGHT:institutional_accumulation].
- **Macro-based:** A hawkish surprise at the September 15–16 FOMC (just
  outside the strict 30-day window but the nearest live macro event)
  [MACRO:FOMC_2026-07-29], or `market-regime` flips from `TRANSITIONAL` to a
  clean `RISK-OFF` read on refresh [MACRO:MarketRegime_2026-08-12].

**Exit on invalidation:** Credit structure (the iron condor) → **roll or
close the tested side first**, re-evaluate the untested side rather than
closing both legs on a single breach (per the invalidation rubric's
credit-structure guidance). The illustrative directional put spread, if ever
actually taken past its current watch-only sizing, uses a **hard stop** at
$16.50.

## Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** `p_raw` — phase-5's `signal_backtest_win_rate` is
  **null** (`dark_pool_accumulation` fired **0** historical times,
  `win_rate_n=0`) [HIST:signal_backtest] → **fallback to the conviction bin**
  (0.55), itself capped at ≤0.65 per the rubric (a proxy is never quoted
  ≥0.70) — 0.55 is already under that cap, so **p = 0.55**.
- **Kelly inputs (directional put-spread framing, target $13.90 / stop
  $16.50 / entry $15.26):** b = |15.26−13.90| / |16.50−15.26| = 1.36/1.24 =
  **1.097**, fraction = 0.25, cap_pct = 5.0
- **Raw Kelly:** (0.55×1.097 − 0.45)/1.097 = **13.95%** → ×0.25 = **3.49%**
  · **Win-rate map ceiling:** p=0.55 falls in the 0.50–0.70 band → **half**
  tier, ≤2.5% — take the smaller of (3.49%, 2.5%) = **2.5%** pre-gate.
- **Risk gates** (each can only cut; applied in order):
  1. **Fundamentals (phase-7b): `VETO`** → any *outright directional*
     structure is **watch-only / 0%**, regardless of Kelly. The put debit
     spread below is published for strike/level reference only, marked
     **fundamentals-vetoed, watch-only**. A defined-risk carry structure
     (the iron condor) remains permitted per the rubric's explicit
     carve-out.
  2. **Sentiment/crowd (phase-7c): `CAUTION`** (`crowd_state=BALANCED`) →
     cut the iron condor's pre-gate size one step: 2.5% (half) →
     **~1.25%** (starter).
  3. **Correlation cluster (phase-6/8):** none — PATH is the only blueprint
     dated 2026-08-12 → no-op.
  4. **Sector rotation (phase-6):** `neutral` (mixed — `sector-flow` level
     bullish, `market-regime` rotation-delta adverse; not cleanly aligned or
     adverse) → no-op (only fires on a clean `adverse` read).
  5. **Debate disconfirmation (phase-8b): `disconfirmed=true`**
     (bear_residual 0.75 ≥ bull_residual 0.65) → cut one more size step:
     ~1.25% → **1.0%** (sizing floor).
- **Context check (phase-0.5):** `unusual_verdict=BUSY_NAME_NORMAL_DAY`
  [CTX:unusual_verdict] → do not size at the top of the band — already
  satisfied; the gates independently drove size to the floor.
- **Final size:** **Iron condor: 1.0%** of book risk (max loss basis).
  **Directional put spread: 0% / watch-only** (fundamentals-vetoed).
- **Deviation reason:** none (final size is below, not above, the
  suggested size at every step — no upward deviation).

## Option structures

### Directional (illustrative only — 0% size, fundamentals-vetoed)

- **Structure:** Put debit spread
- **Strike(s) / expiry:** Buy $15P / Sell $13.50P, 2026-09-18 (37 DTE —
  deliberately spans the 2026-09-03 earnings date to express the specific
  catalyst-risk thesis phase-7b/7c raised, not a technical-only trade)
- **Debit/credit:** ~$0.75 illustrative debit (37-DTE avg IV ≈78.2%
  [STRUCT:iv_term_structure]; confirm against live markets before any actual
  fill)
- **Breakeven:** $14.25
- **Max loss:** $0.75/contract (the debit) — **but sized to 0% of book risk
  per the phase-7b VETO gate; this leg is not an active recommendation, it
  documents where a PM would express the bear case if the veto were later
  lifted (e.g., post-earnings, once the fundamental picture clears).**
- **Why this structure:** A debit put spread caps risk to the premium paid
  while targeting the well-corroborated $13.89–$13.93 support break every
  phase-8 agent flagged; spanning earnings deliberately tests the
  insider-selling/EPS-miss thesis rather than avoiding it, which is exactly
  why it's gated to zero size until the veto clears.

### Defined-risk alternative (primary recommendation — 1.0% size)

- **Structure:** Iron condor
- **Strike(s) / expiry:** Sell $16.50C / Buy $18.00C **and** Sell $14.50P /
  Buy $13.50P, 2026-08-28 (16 DTE — **expires before the 2026-09-03
  earnings date**, deliberately avoiding the binary-event gap risk phase-7b/
  7c flagged, per the phase-9 rule to avoid binary events the plan doesn't
  intend to trade)
- **Strike sourcing:** Short call $16.50 = phase-3's `call_wall_resistance`
  strike [OI:oi_by_strike]; long call $18.00 = the largest near-term OI
  cluster in the ≤30-DTE window [OI:oi_by_strike]; short put $14.50 sits
  just below phase-2's near support ($14.86–$14.87) [DP:price_levels]; long
  put $13.50 sits just below the hard support ($13.89–$13.93)
  [DP:price_levels].
- **Debit/credit:** Illustrative net credit ~$0.70–$0.90 (call spread width
  $1.50, put spread width $1.00; confirm against live markets — IV30d
  ≈82.1% [HIST:vrp] makes both sides reasonably rich to sell)
- **Breakeven:** approx. $15.65–$15.75 (upside) / approx. $13.75–$13.85
  (downside), depending on the actual credit received
- **Max loss:** width minus credit — capped and sized to **1.0% of book
  risk** on the wider ($1.50) call side
- **Why this structure:** Directly matches `market-regime`'s own trading
  guidance ("iron condors in range") [MACRO:MarketRegime_2026-08-12], sells
  into a `PREMIUM_SELLING` VRP regime (`vrp=+0.189`) [HIST:vrp], and
  monetizes the long-gamma mean-reversion mechanic [STRUCT:gex] without
  taking on the earnings-date gap risk the fundamentals/sentiment gates
  specifically flagged. At current IV (≈78–82% across the relevant tenors),
  a full 1-sigma 16-day move (~±$2.55) could test either short strike — the
  1.0% sizing (driven down by the 7c/8b gates) reflects that real
  assignment risk, not a mispriced "safe" trade.

## Macro overlay

- **Tailwinds:**
  - Technology `sector-flow` net_flow +$3.92B, 5/5-day inflow persistence
    [MACRO:sector_flow_persistence_2026-08-12]
  - Fed funds 3.63%, well below the prior-cycle peak (~5.5%) — an already-
    substantial cutting cycle [MACRO:DFF_2026-08-11]
  - ISM Manufacturing 55.6, strongest since May 2022
    [MACRO:ISM_Mfg_2026-07]
- **Headwinds:**
  - `market-regime=TRANSITIONAL`, explicit half-size guidance
    [MACRO:MarketRegime_2026-08-12]
  - Technology `market-regime` rotation-delta shows money flowing OUT
    (-$34.0M) today, and PATH's own peer set (PANW, PLTR) sat on the
    bearish side of today's tape [MACRO:MarketRegime_2026-08-12]
  - CPI YoY +3.30% / core +2.47%, PCE YoY +3.67% / core +3.29% — both above
    the Fed's target, with 3 hawkish FOMC dissents on 2026-07-29
    [MACRO:CPIAUCSL_2026-07][MACRO:FOMC_2026-07-29]
  - Payrolls -23K MoM (July) — softening labor momentum
    [MACRO:PAYEMS_2026-07]
- **Net:** Mixed — leaning cautious given the explicit market-regime sizing
  guidance and PATH's own adverse peer-group positioning within an otherwise
  bullish sector aggregate.

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|------|-------|------------------|
| 2026-09-03 (postmarket) | **PATH Q2 FY2027 earnings** (consensus rev. $397.77M, EPS $0.15) [MACRO:PATH_earnings_2026-09-03] | ? — binary; the iron condor deliberately expires (2026-08-28) before this date |
| 2026-09-15/16 | FOMC meeting (dot plot) | ? — just outside the strict 30-day window; proximate, watch for hawkish surprise risk bleeding into the condor's roll decision |

## Post-trade monitoring checklist

- [ ] Re-check `uw options-structure gex --symbol PATH` daily for a regime
      flip out of `POSITIVE` — the entire mean-reversion thesis behind the
      condor depends on this holding [STRUCT:gex]
- [ ] Re-check `uw dark-pool block-stratified --symbol PATH` daily —
      confirm the `large`-tier buy_ratio doesn't reverse toward sustained
      distribution (< 0.45) [DP:block_stratified]
- [ ] Watch for a fresh insider Form-4 filing or updated MSPR print before
      2026-09-03 — the July 2026 `-100` reading is the freshest available;
      any confirmation or reversal directly changes the phase-7b gate
      [FUND:insider_MSPR]
- [ ] Track short-interest updates (`fz` semi-monthly settlement) — does the
      31.10% figure start declining (covering) or keep rising into earnings?
      [SENT:short_float fz semi-monthly]
- [ ] Confirm the condor's short strikes ($14.50P/$16.50C) against live
      quotes before entry — the credit figures above are illustrative,
      derived from IV context, not a live chain snapshot
- [ ] If price closes twice above $16.50 or twice below $13.89, execute the
      invalidation exit per the rules above before the 2026-08-28 expiry

## Citations summary

1. `[HIST:oi_trend]` — 29 of 30 sessions net OI-building,
   `total_net_oi_change=+318,061` — phase-5-historical.md §OI trend
2. `[STRUCT:gex]` — dealer regime `POSITIVE` (long gamma), zero regime flips
   across the 30-session rally — phase-4-structure.md §GEX / phase-5-
   historical.md §GEX time series
3. `[FUND:insider_MSPR]` — insider MSPR at −100 (max bearish) in the most
   recent available month (July 2026), directly ahead of the 2026-09-03
   print — phase-7b-fundamentals.md §Insider signal
4. `[INSIGHT:price_vs_flow]` — "DIVERGENCE: Price is up 32.1% but options
   flow is bearish (net flow: $-44378)" — phase-7-insights.md §Price vs flow
5. `[MACRO:MarketRegime_2026-08-12]` — `TRANSITIONAL`, explicit "Half
   position sizes... Iron condors in range" guidance — phase-6-macro.md
   §Market regime
6. `[DEBATE:bear_residual]` — bear_residual 0.75 ≥ bull_residual 0.65,
   `disconfirmed=true` — phase-8b-debate.md §Disconfirmation verdict
