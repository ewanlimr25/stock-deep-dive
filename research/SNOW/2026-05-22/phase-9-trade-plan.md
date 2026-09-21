# Phase 9 — Trade Blueprint

**Ticker:** SNOW
**As-of date:** 2026-05-22
**PM voice:** desk PM running an institutional options-overlay book
**Spot reference:** $172.16 ([STRUCT:gex] underlying_price; DP VWAP $171.89)
**Upstream phases cited:** phase-0.5 through phase-8b

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

SNOW is a **size-unusual but direction-neutral name pinned at the $172.5 gamma wall
into a 5/27 earnings binary** that the 5/29 ATM straddle prices at **±13.3% (~$149–$195)**
[STRUCT:gex DUCKDB] — and the smart-money tape refuses to confirm the +32% run-up:
net options flow is bearish despite the rally [INSIGHT:price_vs_flow], the
earnings-week signed delta is net −$15M [FLOW:delta_notional DUCKDB], and the only real
fresh positioning is a *capped* 5/29 185/200 bull call spread [OI:biggest_increases].
With the crowd one-sidedly long (86% analyst-buy, retail-funded calls) into a
priced-for-perfection name [SENT:revision_trend][FUND:psTTM] and a negative-vanna IV
crush that mechanically forces dealer selling on a miss [STRUCT:vanna_charm], this is a
**no-directional-edge, two-tailed, defined-risk event** — trade it small, define the
risk, and let the asymmetry (down) and the smart-money level (up = $185) frame the
structures.

## Bias + conviction + horizon

- **Directional bias:** **RANGE / NEUTRAL** (5-of-5 phase-8 agents; UW composite MIXED)
  with an **asymmetric-downside** tilt.
- **Conviction (M-01 bin):** **0.55** (slight edge).
- **Time horizon:** **1-5d** (event-anchored to the 2026-05-27 postmarket print; 5/29 expiry).
- **Why this bin:** phase-10 confluence is expected mid-40s (perfectly-mixed ~50 minus
  the phase-7c CAUTION penalty) → 30–49 band → 0.55; there is no directional edge to
  justify a higher bin, and two downside gates fired.

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| Primary | **$172.5** | Establish the structure while pinned at the gamma wall pre-print (best theta/skew entry on a spread) | [STRUCT:gex] $172.5 +$23.8M wall |
| Aggressive | **$174–175** | A pre-print pop into the thin DP resistance → cheaper put-spread / better condor credit | [DP:price_levels] $174.29 thin resistance |
| Fade (plan B) | **$185 reclaim** | If SNOW gaps and *holds* >$185 post-print, the downside thesis is dead — flip to the upside call-spread / stand with the breakout | [OI:biggest_increases] 185C magnet |

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Support (near) | **$170.8–171.8** | [DP:price_levels] dense near-floor |
| Support (major) | **$163.5–167** | [DP:price_levels] 5-day ~$85M accumulation shelf |
| Support (move floor) | **$150 ≈ −13%** | [STRUCT:gex DUCKDB] expected-move floor / 5/29 150P build |
| Resistance (near) | **$174.29** | [DP:price_levels] thin |
| Resistance (magnet) | **$185 ≈ +7.5%** | [OI:biggest_increases] 185C +5,046 OI / [STRUCT:gex] wall |
| Resistance (cap) | **$200 ≈ +16%** | [OI:smart_positioning] 200C writing / [STRUCT:gex] wall |
| Gamma flip (practical) | **$172.5** | [STRUCT:today_gamma_flip] support wall (ZGL $78.8 academic) |
| Largest pin | **n/a** | [OI:pin_risk] SNOW absent — earnings is the event, not an OPEX pin |

## Invalidation

- **Price-based:** *Downside thesis* — a post-print **gap-and-hold above $185** (the OI
  magnet / gamma wall) OR two daily closes back above **$174.29** pre-print → exit the
  put spread. *Range thesis* — a post-print close **outside the $149–$195 cone**.
- **Signal-based:** `insights_conviction_matrix` flips to **DIRECTIONAL_LONG**, OR
  dark-pool flips to clear **accumulation (buy_ratio >0.65)** [INSIGHT:institutional_accumulation],
  OR cumulative premium flow turns **net-bullish 3 consecutive sessions**
  [HIST:cumulative_premium_flow] — any of these kills the downside lean.
- **Macro-based:** a UW regime flip from **TRANSITIONAL → RISK-ON**
  [MACRO:MarketRegime_2026-05-22] lifts all software and undercuts the downside tilt.
  (No scheduled macro release between 5/22 and the 5/27 print — the binary is
  idiosyncratic.)
- **Exit style:** **Hard stop = the defined max loss** of each debit spread (let it
  resolve through the print; the spread *is* the stop). For the condor, **roll/close the
  tested side** if spot breaches a short strike intraday post-print.

## Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** p_raw = **0.923** from phase-5 `bullish_flow` backtest
  (n=13, source=backtest) [HIST:signal_backtest] — **REJECTED as the Kelly p**: it is
  universe-wide (not SNOW), tiny-N on a hot semis up-tape, and **not aligned with the
  RANGE/NEUTRAL bias** (there is no directional long thesis it sizes). Per phase-5's
  own recommendation, **fall back to the conviction bin** → fallback p = min(0.55,
  0.65 cap) = **0.55**. (The `high_iv_rank` vol-realisation 71.4% (n=14) is the
  regime-relevant read and argues *against* naked premium either way, reinforcing
  defined-risk.)
- **Kelly inputs:** b = **2.33** (primary put spread: profit $10.5 / risk $4.5),
  fraction = 0.25, cap_pct = 5.
- **Raw Kelly:** (0.55×2.33 − 0.45)/2.33 = **0.357** → suggested = min(0.357×0.25×100,
  5) = **5%**. **Win-rate map ceiling** at p=0.55 (0.50–0.70 band) = **half (≤2.5%)** →
  take the smaller = **2.5%**.
- **Risk gates:**
  - **Fundamentals (phase-7b): CAUTION** → cut one step (half → **starter**, ~1.25%).
  - **Sentiment/crowd (phase-7c): CAUTION, CROWDED_LONG** → cut one step (starter →
    **~1.0%**).
  - **Correlation (phase-6/8): SNOW/PATH 0.626** = soft-watch (0.60–0.70), **no cut**;
    size SNOW+PATH as ~1.3× one high-beta-software unit if both are live.
  - **Sector rotation (phase-6): aligned** (Tech inflow accelerating) → **no cut**.
  - **Debate (phase-8b): bull_residual 0.65 vs bear_residual 0.55 → NOT disconfirmed**
    → **no cut**.
  - **Context (phase-0.5): BUSY_NAME_NORMAL_DAY** → do not size at band top (honored).
- **Final size:** **~1.0% of book risk** (starter), split across the two structures.
- **Deviation reason:** none (sized *down*; deviation-up forbidden — two gates fired).

## Option structures

### Directional (primary) — downside-asymmetry tail, defined-risk

- **Structure:** 5/29 **put debit spread** (the thesis-aligned tail: profits if the
  crowded long unwinds / vanna gap-down).
- **Strike(s) / expiry:** **buy 165P / sell 150P, expiry 2026-05-29** (captures the
  5/27 print; 165 just under the $170.8 near-floor, 150 = the −13% move floor).
- **Debit/credit:** ≈ **$4.50 debit** (long 165P ~$7.5 / short 150P ~$3.0 at 5/29 IV
  ~123%; the spread neutralizes most of the IV-crush vega vs a naked put).
- **Breakeven:** ≈ **$160.5** (165 − 4.50).
- **Max loss:** **$4.50** / spread (the debit) — this *is* the hard stop.
- **Max value:** $15 (SNOW ≤ $150); payoff b ≈ 2.33.
- **Why this structure:** front IV is 123% [STRUCT:iv_term_structure] — a *spread* (not
  a naked long put) caps the IV-crush bleed while still paying off on the gap-down that
  phase-4 vanna + phase-7c crowded-long make the dominant drawdown vector. Sized to the
  ±13% move: the short 150 leg sits at the expected-move floor.

### Defined-risk alternative — neutral IV-crush harvest

- **Structure:** 5/29 **iron condor** (for the "vol is modestly rich, move stays in
  the cone" view — earnings-scout's expression).
- **Strike(s) / expiry:** **sell 150P / buy 140P** and **sell 195C / buy 205C, expiry
  2026-05-29.** Short strikes at the **±13% expected-move edges**, around the $172.5
  pin.
- **Debit/credit:** ≈ **$3.0 credit** (collect the rich front IV).
- **Breakeven:** ≈ **$147 / $198** (short strikes ± credit).
- **Max loss:** **$7.0** / side (width $10 − $3 credit), defined.
- **Caveat:** the `high_iv_rank` backtest shows **71.4% vol-realisation**
  [HIST:signal_backtest] — the move *often* reaches the edges, so this is a
  **lower-probability** premium harvest; keep it the smaller half of the ~1% budget and
  do not add to it. (Naked short straddles are disallowed; long straddles are gutted by
  the crush — both avoided.)

*Upside-tail alternative (for anyone leaning with the smart money):* a 5/29 **175/185
call debit spread** echoes the 185C magnet [OI:biggest_increases] — same defined-risk
logic, opposite tail; use only on a pre-print reclaim of $174.29.

## Macro overlay (cite phase-6)

- **Tailwinds:** Technology sector is the **largest + accelerating** options inflow
  ($6.19B, persistence 1.0) [MACRO:sector_flow_persistence]; **Fed easing** (funds
  3.62%) [MACRO:DFF_2026-05-21]; **core CPI +2.74% YoY** near target
  [MACRO:CPILFESL_2026-04].
- **Headwinds:** regime **TRANSITIONAL**, breadth only 38.1% → "half size, defined-risk"
  [MACRO:MarketRegime_2026-05-22]; **10y at 4.57%** caps multiple expansion
  [MACRO:DGS10_2026-05-21].
- **Net:** mixed / mildly-supportive sector backdrop offset by a cautious regime — the
  earnings binary dominates the outcome.

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|------|-------|------------------|
| **2026-05-27 (postmarket)** | **SNOW Q1 earnings** — ±13.3% expected move | ? (binary) |
| 2026-05-28 | **NTAP earnings** (data-infra peer, ~10.6% impl move) — read-through | ? |
| 2026-05-22 → 05-27 | No scheduled US macro release | neutral |

## Post-trade monitoring checklist

- [ ] **Daily:** re-check dark-pool buy_ratio (phase-2) — a flip >0.65 = accumulation =
  downside-thesis invalidation [INSIGHT:institutional_accumulation].
- [ ] **Daily:** watch spot vs the $172.5 gamma pin and the $174.29 / $170.8 band —
  a pre-print break of $174.29 on volume cuts the downside lean [STRUCT:gex][DP:price_levels].
- [ ] **Into the print (5/27 PM):** confirm the structure's max loss still ≤ the ~1%
  budget; do NOT add size into the event.
- [ ] **Post-print (5/28 AM):** if gap-and-hold >$185 → close the put spread (thesis
  dead); if gap-down through $160 → manage the put spread toward the $150 target; for
  the condor, roll/close any breached short side.
- [ ] **5/28:** read NTAP's print as a same-sector confirm/deny [INSIGHT:earnings_play].
- [ ] **Weekly:** re-run `historical_cumulative_premium_flow` — 3 net-bullish sessions
  invalidates the downside lean [HIST:cumulative_premium_flow].

## Citations summary

Minimum 3 distinct upstream datapoints (M-04), listed for phase-10 spot-check:

1. **[STRUCT:gex DUCKDB]** — 5/29 ATM straddle $23.35 → ±13.3% expected move
   (phase-4-structure.md §Summary / §GEX).
2. **[INSIGHT:price_vs_flow]** — "price up 31.7% but options flow is bearish (net
   −$902,406)" divergence (phase-7-insights.md §Price vs flow).
3. **[FLOW:delta_notional DUCKDB]** — earnings-week (2–7DTE) signed delta-notional
   **−$15M** (phase-1-flow.md §Aggressor & delta-notional).
4. **[OI:biggest_increases]** — 5/29 185C OI +5,046 ask-bought $2.17M, capped by 200C
   writing (phase-3-positioning.md §Largest OI increases).
5. **[STRUCT:vanna_charm]** — net vanna −2,294 → post-earnings IV crush forces dealer
   selling (phase-4-structure.md §Vanna + charm).
6. **[SENT:revision_trend]** — ~86% analyst buy (50/58), stable (phase-7c-sentiment.md
   §Analyst-revision momentum).
