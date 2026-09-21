# Phase 9 — Trade Blueprint

**Ticker:** CMPS
**As-of date:** 2026-06-18
**PM voice:** desk PM running an institutional book
**Spot reference:** $12.53 (phase-3 close; phases 1–2 intraday prints were $12.03–12.10)
**Upstream phases cited:** phase-0.5 through phase-8b

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

The entire bearish case on CMPS is **one** brand-new Jan-2028 $10 LEAP put bought
ask-side for ~$647K [FLOW:top_premium_trades] — non-persistent (consistency 0.2, 1
session [FLOW:sweep_persistence]), not yet in OI, and a +3.83σ P/C extreme that on a
normally call-heavy name reads as a *fade* trigger, not a trend [HIST:pc_ratio_zscore].
Everything that compounds points the other way: a FULLY_POSITIVE long-gamma dealer
pin at $12–13 [STRUCT:gex], insiders buying (MSPR +100 May'26 [FUND:insider_MSPR]) and
strong-buy revisions to a $21.72 target — which earned a phase-7b fundamental **VETO**
of any short [FUND:tier_adjustment] — and a desk that went **0 SHORT, 0 LONG, plurality
NEUTRAL** [AGENT:plurality]. **This is a no-directional-trade: watch the bear's
convexity, do not put on a short, and do not chase the +81.6%-YTD parabola long.**

## Bias + conviction + horizon

- **Directional bias:** **NEUTRAL** (latent bearish tilt from one print, fully faded by
  positioning, structure, fundamentals, and the desk).
- **Conviction (M-01 bin):** **0.55**
- **Time horizon:** 1–4w (the LEAP-put risk is a 2026–2027 story; nothing tradeable on
  this skill's near-term clock).
- **Why this bin:** estimated phase-10 confluence ≈ **31** (negative confluence — the
  bearish bias is *fought* by the data: 30–49 band → 0.55), and the bias is NEUTRAL, so
  0.55 reflects "slight edge, no directional trade," not a conviction short.

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| Primary | $11.54 | **No directional entry now** — re-engage the (currently vetoed) bear ONLY on two daily closes below $11.54 *with* P10/lower put OI building | [DP:price_levels] / [OI:term_structure] |
| Aggressive | $13.00 | Rejection at the $13 call wall / largest-GEX strike — short-bias scalp *within* the pin (defined-risk only) | [STRUCT:gex] |
| Fade | $11.84 | Hold of the $11.84–11.90 DP support shelf → put-credit-spread fade of the bear (the contrarian-scanner lean, down-weighted to neutral by the debate) | [DP:price_levels] |

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Support | $11.84 (shelf); $11.54 deeper; $10.00 LEAP put wall (−20%) | [DP:price_levels] / [OI:oi_by_strike] |
| Resistance | $13.00 (call wall + largest GEX) | [OI:oi_by_strike] / [STRUCT:gex] |
| Gamma flip | none — FULLY_POSITIVE GEX, no ZGL (spot deep in long-gamma) | [STRUCT:gex] |
| Largest pin | $12.00 (2026-07-17 max-pain magnet, −4.15%) | [STRUCT:max_pain] |

Price-context color: RSI(14) **58.68** (not overbought, no exhaustion cover for a fade)
[HIST:rsi fz]; spot **−15.1% below the 52-week high $14.76** [HIST:52w_proximity fz] —
room to the highs, momentum intact. (Narrative only; does not alter sizing.)

## Invalidation

- **Price-based:** two daily closes **below $11.54** (deep DP support) flips the read
  bearish-actionable; a daily close **above $13.00** (call wall) kills any short or
  range-short expression.
- **Signal-based:** **P10-or-lower put OI builds materially on 6/19+** (a campaign, not
  the one orphan print) **AND GEX flips negative** — that resurrects the directional
  short [OI:term_structure, STRUCT:gex]. Equally, the conviction-matrix flipping out of
  MIXED to DIRECTIONAL_SHORT [INSIGHT:conviction_matrix].
- **Macro-based:** a negative **COMP006 26-week durability / relapse** signal before the
  H2-2026 readout, or a macro shock that breaks the long-gamma pin [MACRO:CMPS_catalyst].

## Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** p_raw = **0.857** (bearish_flow, n=**7**, source=backtest)
  [HIST:signal_backtest] → N-cap (n<10) 0.75 → **capped p = 0.75**.
- **Kelly inputs:** b = (12.53−10.00)/(13.00−12.53) = **5.38**, fraction = 0.25, cap_pct = 5.
- **Raw Kelly:** (0.75×5.38 − 0.25)/5.38 = **0.704** → suggested = min(0.704×0.25×100, 5)
  = **5.0%** pre-gate. **Win-rate map ceiling:** p≥0.70 → full (pre-gate).
- **Risk gates (each can only cut):**
  - Fundamentals (phase-7b): **VETO** → **directional size = watch-only / 0%** (insiders
    buying + strong-buy + 2 Phase-3 wins contradict the short on ≥2 axes). **DECISIVE.**
  - Sentiment / crowd (phase-7c): **CAUTION**, crowd_state BALANCED → cut one step (moot
    after VETO; the bear is the late/crowded options trade with no squeeze fuel).
  - Correlation cluster (phase-6/8): **none** (CMPS/MARA/PATH unrelated, high_corr null) → no-op.
  - Sector rotation (phase-6): **adverse** (Healthcare INFLOW, persistence 0.8) → cut half
    step (moot after VETO).
  - Debate (phase-8b): bull_residual **0.75** vs bear_residual **0.65** → **disconfirmed =
    false** → no extra cut (the bear failed to overturn "don't short").
- **Context modifier (phase-0.5):** unusual_verdict = GENUINELY_UNUSUAL (bearish-skewed)
  → no-op on `p`, but the *small absolute $* keeps tradeability modest regardless.
- **Final size:** **0% directional (watch-only).** Any defined-risk premium-selling
  expression below is a **starter (≤1% book risk)**, separate from the vetoed direction.
- **Deviation reason:** none (no upward deviation; forbidden anyway — gates fired).

## Option structures

### Directional (primary) — *fundamentals-VETOED, carry/watch-only, 0% of book*

- **Structure:** Jan-2028 **$10/$7 put debit spread** (own the durability-binary convexity
  with defined risk; this is the bear's *own* instrument, not a desk short).
- **Strike(s) / expiry:** Buy $10 put @ $3.56, sell $7 put @ $2.39 — 2028-01-21.
- **Debit/credit:** **$1.17 debit**.
- **Breakeven:** $8.83. **Max loss:** $1.17 (defined). Max value $3.00 (profit $1.83).
- **Why this structure:** at IV30d ~86–95% a naked long put bleeds; the spread halves the
  premium and still pays on a durability miss into 2027. 582-DTE tenor spans COMP006 (H2
  2026) + NDA (Q4 2026) + FDA review. **Marked watch-only** — only sized >0 if the
  phase-7b VETO clears (insiders turn sellers / consensus cuts) AND OI confirms a campaign.

### Defined-risk alternative — *NEUTRAL/range, starter ≤1% only*

- **Structure:** 2026-07-17 **iron condor** (expires **before** 7/30 earnings — avoids that
  binary), expressing the long-gamma $12–13 pin + premium-selling VRP (+5.03 [HIST:vrp]).
- **Strike(s) / expiry:** Sell $10 put @ $0.46 / buy $8 put ≈ $0.20 (modeled, no print);
  sell $15 call @ $0.51 / buy $17 call @ $0.29 — 2026-07-17.
- **Debit/credit:** **≈ +$0.48 credit**.
- **Breakeven:** $9.52 / $15.48. **Max loss:** ≈ **$1.52** (width $2 − credit $0.48).
- **Caveat (N4):** 7/17 expected move ≈ **±$3.36 (±27%)** at IV ~95% — the $10/$15 short
  strikes (−20%/+20%) sit **inside** that move, so probability-of-profit is only ~coin-flip;
  the +VRP edge is thin against 94% absolute IV and binary risk. **Starter size only**, and
  the desk's honest answer is closer to **no trade** than to selling this condor.

## Macro overlay (cite phase-6)

- **Tailwinds (to the bear / pressure on the name):** hawkish FOMC 6/17 (dot to 3.8%, hike
  bias) [MACRO:FOMC_2026-06-17]; 10y **4.49%** rising — duration headwind on clinical
  biotech [MACRO:DGS10_2026-06-17]; sticky inflation (CPI +4.17% YoY) [MACRO:CPIAUCSL_2026-05].
- **Headwinds (to the bear / support for the name):** Healthcare **persistent INFLOW**,
  net +$219.6M, persistence 0.8 [MACRO:sector_flow_persistence]; both Phase-3 endpoints met
  [MACRO:CMPS_catalyst].
- **Net:** **mixed** — rate/Fed leg supports downside, sector flow + pipeline support the
  name; they roughly cancel, leaving the idiosyncratic durability binary as the swing.

## Catalyst calendar (next 30d+)

| Date | Event | Impact direction |
|------|-------|------------------|
| 2026-07-17 | OPEX cliff (31.21% of OI, call-heavy; max-pain $12) | ? (pin $12–13) |
| ~2026-07-28/29 | Next FOMC | ? |
| 2026-07-30 | CMPS earnings (verify) | ? |
| H2 2026 | **COMP006 26-week durability data** (the LEAP put's binary) | ? |
| Q4 2026 | **NDA submission to FDA** | ? |

## Post-trade monitoring checklist

- [ ] **6/19+ tape:** does the P10 (or lower-strike) put OI actually **build** (campaign) or
      stay a one-print orphan? — the single fact that flips the verdict [OI:biggest_increases].
- [ ] **GEX daily refresh:** any move toward a zero-gamma flip (negative GEX below spot) —
      currently FULLY_POSITIVE [STRUCT:gex].
- [ ] **Dark pool:** large-tier buy/sell ratio — does the 60%-sell large tier persist into
      genuine distribution, or revert [DP:block_stratified]?
- [ ] **Insider / consensus:** any reversal of MSPR to net-selling or a ratings cut — would
      begin to clear the phase-7b VETO [FUND:insider_MSPR].
- [ ] **Durability newsflow:** any COMP006 26-week / discontinuation signal before H2 2026.

## Citations summary

1. [FLOW:top_premium_trades] entire bearish skew = ONE Jan-2028 $10 LEAP put, ~$647K
   ask-side, delta −0.24 — phase-1-flow.md §Largest prints.
2. [HIST:pc_ratio_zscore] P/C z-score **+3.83 = BEARISH_EXTREME** (today 1.36 vs 20-day
   mean 0.243) — phase-5-historical.md §P/C z-score.
3. [FUND:tier_adjustment] phase-7b **VETO** — insiders buying (MSPR +100) + strong-buy
   (Recom 1.12, target $21.72) contradict the short — phase-7b-fundamentals.md §Verdict.
4. [STRUCT:gex] **FULLY_POSITIVE** GEX, no ZGL, pin $12–13 — phase-4-structure.md §GEX.
5. [INSIGHT:price_vs_flow] **DIVERGENCE: price +33.4% vs bearish flow** — phase-7-insights.md.
