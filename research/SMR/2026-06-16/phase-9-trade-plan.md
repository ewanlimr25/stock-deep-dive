# Phase 9 — Trade Blueprint

**Ticker:** SMR
**As-of date:** 2026-06-16
**PM voice:** desk PM running an institutional book
**Spot reference:** $9.89 ([CTX]/phase-0; intraday $9.9–10.0)
**Upstream phases cited:** phase-0.5 through phase-8b

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

SMR is a genuinely bearish tape — dark-pool **DISTRIBUTION** (`buy_ratio 0.384`,
$4.63M sells vs $1.72M buys [DP:block_stratified]) under a **net-bearish whole-tape**
(net_flow −$159,229 [FLOW:insights_deep_dive]) and a −16.8% 30-day downtrend
[HIST:trend], with UW's composite calling it DIRECTIONAL_SHORT [INSIGHT:conviction_matrix]
— but it is **not a tradeable short here.** The directional bearish signal
backtests **28.6% (N=7)** [HIST:signal_backtest], the short is **crowded** (18.12%
float [SENT:short_float fz]) into an **FOMC binary one day out** [MACRO:FOMC_2026-06-17]
and a live **Japan $25B SMR squeeze catalyst** [MACRO:Japan_SMR_pledge] on a funded
balance sheet, and the phase-8b debate **disconfirmed** the short (bear 0.65 ≥ bull
0.55). Net: **RANGE / fade-the-rip, watch-only at spot** — the only edge is selling
strength into the $10.64–$10.95 supply, not chasing the dip.

## Bias + conviction + horizon

- **Directional bias:** **RANGE** (bearish-lean, but the directional short is
  negative-edge → expressed as fade-the-rip; long-gamma range $9.5–$10.95).
- **Conviction (M-01 bin):** **0.55**
- **Time horizon:** **1-5d** (through the 06-17 FOMC; re-assess after)
- **Why this bin:** estimated phase-10 confluence ≈ low-50s (mildly mixed, slight
  bearish lean), then the phase-8b disconfirmation gate **down-shifts one bin** →
  floor **0.55**. (Phase-10 finalizes.)

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| Primary    | **WATCH (no entry)** | Stand aside through FOMC 06-17 — negative-edge short (p=0.286), crowded, binary one day out | [HIST:signal_backtest] |
| Aggressive | **$10.64–$10.95** | **Fade the rip:** rejection at the DP supply band post-FOMC, no fresh ask-side call sweeps | [DP:price_levels] |
| Fade (plan B) | **>$10.95** | Counter: two closes above $10.95 on **ask-side call sweeps** = squeeze real, bearish lean dead → stand aside / small momentum-long | [STRUCT:term_skew] |

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Support | **$9.48** (band $9.79/$9.57/$9.48; put walls $9/$8; 52W low $8.85) | [DP:price_levels] / [OI:oi_by_strike] |
| Resistance | **$10.64** (supply $10.64–$10.95) | [DP:price_levels] |
| Gamma flip | **$7.50** (front 06-18; broad ZGL $4.40) — but the live **$10 gamma resistance wall** is the operative pivot | [STRUCT:today_gamma_flip] |
| Largest pin | **$12.00** (06-18 max-pain, 21% OTM — unreachable, calls bleed) | [STRUCT:max_pain] |

**Price-context color (advisory):** RSI(14) 42.25 [HIST:rsi fz] — *not* oversold;
price is **−82.78% from the 52W high and +11.75% off the 52W low $8.85**
[HIST:52w_proximity fz] → a falling knife in its bounce zone. This reinforces
"watch-only / fade rips," not "press the short into support."

## Invalidation

- **Price-based:** Two daily closes **above $10.95** (top of the DP supply band)
  [DP:price_levels], OR any reclaim-and-hold of the **$10 gamma wall** on rising
  volume [STRUCT:today_gamma_flip] — the bearish lean is then dead.
- **Signal-based:** Dark-pool DISTRIBUTION reverses to accumulation (`buy_ratio
  > 0.55`) [INSIGHT:institutional_accumulation], OR fresh **ask-side call sweeps**
  appear (there were none on the as-of tape) [FLOW:sweeps].
- **Macro-based:** A **dovish FOMC surprise on 06-17** or a **Japan $25B SMR-pledge
  follow-through gap** beyond the ±5.68% implied move
  [MACRO:FOMC_2026-06-17][MACRO:Japan_SMR_pledge].
- **Exit on invalidation:** **Hard stop** (debit structures) — close 100% on a
  daily close back above the $10 gamma wall.

## Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** `p_raw = 0.286` (n=7, source=backtest)
  [HIST:signal_backtest] → N-cap (n<10 → 0.75) → **capped p = 0.286** (cap not
  binding). p **< 0.50**.
- **Kelly inputs:** b = **1.85** (target $8.50 / entry $9.89 / stop $10.64),
  fraction = 0.25, cap_pct = 5.
- **Raw Kelly:** **−0.099** (negative edge) → suggested size = `min(−2.50, 5)` →
  **clamped to 0**. **Win-rate map:** p<0.50 → **starter/skip; SHORT-side floor
  enforced.**
- **Risk gates:**
  - Fundamentals (7b): **CONFIRM** → no-op (business deteriorating, confirms bearish).
  - Sentiment/crowd (7c): **CAUTION**, crowd_state **CROWDED_SHORT** → cut one step.
  - Correlation (6/8): **none** (SMR is the only blueprint for 2026-06-16) → no-op.
  - Sector rotation (6): **neutral** (Industrials options outflow supports the
    bearish direction, but sector was +1.14% on price) → no-op.
  - Debate (8b): bull_residual **0.55** vs bear_residual **0.65** → **disconfirmed
    → down-shift bin one + cut one step.**
- **Context (0.5):** `BUSY_NAME_NORMAL_DAY` → not top-of-band (already at floor).
- **Final size:** **0.0% — WATCH-ONLY.** Negative raw Kelly + gates fired forbid
  any upward deviation; a starter defined-risk debit (≤0.75% max-loss) is permitted
  **only if** the fade-the-rip trigger ($10.64–$10.95 rejection, post-FOMC) fires.
- **Deviation reason:** none (sizing down — always allowed; upward deviation
  forbidden because gates fired).

## Option structures

> **Structure governance (premium-buying regime).** VRP **−2.15** — realized vol
> **307%** vs implied 92%, IV at the **0th percentile** [HIST:vrp] — means **BUY
> options, do not sell them.** The "range" read's natural structure (an iron condor
> / call-credit fade) is **REJECTED**: selling premium on a 307%-realized-vol,
> beta-2.27 name into the Japan/FOMC catalysts gets run over. Both structures below
> are **debit** (long vol), expiry **2026-07-17** to clear the 06-18 FOMC/OPEX chaos.
> Debits are **illustrative** (IV30d ≈ 92%), per the disclaimer.

### Directional (primary)

- **Structure:** long put (convexity expression of the bearish lean / fade-the-rip)
- **Strike(s) / expiry:** **$10 put, 2026-07-17** (31 DTE)
- **Debit/credit:** ≈ **$1.05** debit (illustrative)
- **Breakeven:** ≈ **$8.95**
- **Max loss:** the debit (≈ $1.05/contract)
- **Why this structure:** IV is at its 0th percentile and realized vol is 3× implied
  [HIST:vrp] — long premium is cheap and convex into a 307%-realized-vol tail; the
  07-17 expiry sidesteps the 06-18 FOMC/OPEX pin. **Deploy only on a rip into
  $10.64–$10.95** (better entry), not at spot.

### Defined-risk alternative

- **Structure:** bear put debit spread (caps cost; tighter defined risk)
- **Strike(s) / expiry:** **$10 / $8 put spread, 2026-07-17**
- **Debit/credit:** ≈ **$0.70** debit (illustrative)
- **Breakeven:** ≈ **$9.30**
- **Max loss:** ≈ **$0.70/contract** (max gain ≈ $1.30 toward the 52W-low zone)
- **Why this structure:** cheaper expression that floors max-loss while still
  long-vol; targets the $9 put-wall / $8.85 52W-low zone [OI:oi_by_strike]. Sized
  starter (≤0.75% max-loss) **only on the fade-the-rip trigger.**

## Macro overlay (cite phase-6)

- **Tailwinds (to the bearish lean):**
  - Sticky inflation keeps rates high → pressures pre-revenue small-cap
    [MACRO:CPIAUCSL_2026-05 FRED] (CPI 4.17% YoY).
  - Industrials options **OUTFLOW −$318M** today [MACRO:MarketRegime_2026-06-16 UW].
  - TRANSITIONAL regime, "half size / defined-risk" [MACRO:MarketRegime_2026-06-16 UW].
- **Headwinds (to the bearish lean / risks):**
  - **FOMC 06-17 binary** [MACRO:FOMC_2026-06-17] — dovish surprise = squeeze.
  - **Japan $25B US-SMR pledge** [MACRO:Japan_SMR_pledge] — live squeeze fuel.
  - Sector green on price +1.14% [MACRO:group_valuation fz EOD]; bullish-Street
    target $15.64.
- **Net:** **mixed** — directionally headwind for SMR, but the binary + catalyst
  make it a two-way event, not a clean short.

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|------|-------|------------------|
| **2026-06-17 (2pm ET)** | **FOMC decision + dot plot** (Warsh's 1st) | ? (hawkish=−, dovish=+) |
| ongoing | Japan $25B US-SMR pledge follow-through | + (squeeze fuel) |
| ~2026-08-06 | Q2 2026 earnings (est., unconfirmed) | ? (outside 30d) |

## Post-trade monitoring checklist

- [ ] **FOMC 06-17 2pm ET** — do not hold directional exposure into it; re-assess
      the tape *after* the dot plot.
- [ ] Re-check dark-pool `buy_ratio` daily — a flip >0.55 (accumulation) invalidates
      the distribution thesis [DP:block_stratified].
- [ ] Watch for **fresh ask-side call sweeps** (absent on as-of) — first sign of a
      squeeze/short-cover [FLOW:sweeps].
- [ ] Track the $10 gamma wall + $10.64–$10.95 supply — fade-the-rip entry zone;
      a hold above $10.95 kills the bearish lean [DP:price_levels].
- [ ] Monitor SMR/nuclear-sector headlines (Japan pledge, contracts) — beta 2.27 /
      307% realized vol means gap risk on any print [SENT:news_tone].

## Citations summary

1. [DP:block_stratified] dark-pool `buy_ratio 0.384` (sell 0.616), $4.63M sells vs
   $1.72M buys — phase-2 §Tier breakdown.
2. [HIST:signal_backtest] `bearish_flow win_rate 28.6%` (n=7) — phase-5 §Signal
   backtest / sizing handoff.
3. [MACRO:FOMC_2026-06-17] FOMC decision one day after as-of; hawkish dot-plot risk
   — phase-6 §Catalyst calendar.
4. [INSIGHT:conviction_matrix] DIRECTIONAL_SHORT at 13.7% confidence — phase-7
   §Conviction matrix.
5. [SENT:short_float fz] 18.12% float short, days-to-cover 1.85, borrow EASY (0.42%)
   — phase-7c §Short interest.
