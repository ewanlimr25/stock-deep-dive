# Phase 9 — Trade Blueprint

**Ticker:** DOCN
**As-of date:** 2026-07-17
**PM voice:** desk PM running an institutional book
**Spot reference:** $118.91 (phase-5 close, 2026-07-17)
**Upstream phases cited:** phase-0.5 through phase-8b

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

DOCN is a −34% fallen name (`$180.50 → $118.91` [HIST:trend]) whose crash was
**technical** — Russell 2000→1000 rebalance forced selling + a 7/15 dilutive $500M
convert-repurchase equity offering [MACRO:DOCN_2026-07 WebSearch] — now pinned in a
**long-gamma range** (ZGL $70.14 ≪ spot, max-pain magnet $120 [STRUCT:max_pain])
with **IV rank 99 / VRP +0.434** [HIST:vrp] making optionality expensive to own and
attractive to sell. The desk returned **zero directional votes** (3 RANGE / 2
NEUTRAL [AGENT]), the one "bullish" print ($985K 180C) was OI-reducing
[OI:decrease_with_volume], and phase-7b **VETO'd** any directional long (insiders
selling, forward EPS guided ~50% lower, PE 58.7). **Net: no directional trade —
harvest the rich, downside-skewed vol with a small, defined-risk, bearish-lean
premium-selling structure that side-steps the 8/4 earnings binary.**

## Bias + conviction + horizon

- **Directional bias:** **RANGE** (bearish-leaning; per phase-8b the distribution is
  downside-skewed, so this is *sell-upside*, not a symmetric condor)
- **Conviction (M-01 bin):** **0.55** (slight edge — the edge is *vol/range*, not
  direction; VETO + CAUTION + BUSY_NAME_NORMAL_DAY hold it at the floor)
- **Time horizon:** **1-4w** (pre-8/4; the primary structure expires 7/31, before earnings)
- **Why this bin:** non-directional consensus with a fundamental VETO and a
  positioning CAUTION → lowest conviction band; phase-10 confluence expected low
  (backfilled there).

## Conviction deviation

Phase-10 confluence scores **68 → recommended bin 0.75**, but this plan holds
**0.55** — a deliberate **downward** deviation (always permitted; the conservative
direction). The high confluence measures *agreement that DOCN is a rich-vol,
long-gamma, no-directional-edge RANGE* — which is real and near-unanimous — **not**
confidence in a sizeable tradeable edge. With the directional expression **VETO'd
to 0%** (phase-7b), a negative bullish Kelly (p 0.143), a positioning **CAUTION**,
and `BUSY_NAME_NORMAL_DAY` context, the honest conviction on the *actionable*
(discretionary defined-risk carry) trade is the floor. "Everyone agrees it's a
range" is not "size this up."

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| Primary    | $123–126 | Sell the bear call spread INTO a rally toward the DP supply shelf ($123.3 / $126.3) — better credit, closer to the $128 wall | [DP:price_levels] |
| Aggressive | ~$119 (now) | Put the spread on at spot to start harvesting the rich IV / long-gamma decay immediately | [STRUCT:gex] |
| Fade (plan B) | >$128 reclaim | If DOCN reclaims the $128 call wall on volume, the bearish-lean is wrong — close the call spread; do NOT flip long (7b veto) | [OI:oi_by_strike call_wall_resistance] |

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Support | **$115** (put wall 918 OI), then $110 / period-low $111.13 | [OI:oi_by_strike put_wall_support] / [INSIGHT:price_vs_flow] |
| Resistance | **$128** (call wall 2,156 OI; 7/17 max-pain), then $123.3 / $126.3 DP supply | [OI:oi_by_strike call_wall_resistance] / [DP:price_levels] |
| Gamma flip (ZGL) | **$70.14** (far below spot — confirms deep long-gamma; not a tradeable trigger) | [STRUCT:gex] |
| Largest pin | **$120** (max-pain magnet, 7/24 & 8/7 expiries) | [STRUCT:max_pain] |

*Price-context color:* `fz` RSI/52-week-proximity were **null** for DOCN (sparse-fz,
phase-5) → no independent overbought/oversold cross-check; the UW trend (−34%,
basing at the low end of the $111–187 range) stands on its own. Narrative only.

## Invalidation

- **Price-based:** two daily closes **above $128** (call wall break → range-up /
  squeeze; the bear call spread's tested side) OR two daily closes **below $115**
  (breakdown toward $110/air). Either voids the $115–128 range premise.
- **Signal-based:** **GEX regime flips NEGATIVE** on the phase-4 daily refresh
  (long-gamma range → trend-amplification; the pin that anchors this trade is gone)
  [STRUCT:gex], OR cumulative premium flow turns decisively net-bullish 3 straight
  sessions (a squeeze building against the call spread) [HIST:cumulative_premium_flow].
- **Macro-based:** **7/29 FOMC hawkish/hike surprise** → risk-off gap for
  duration tech that breaks the range [MACRO:FOMC_2026-07-29]. (The **8/4 earnings**
  binary is *avoided by construction* — the primary structure expires 7/31.)

## Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** p_raw = **0.143** (bullish_flow, n=**7**, source=backtest)
  → N-cap (n<10) = 0.75 → capped **p = 0.143** [HIST:signal_backtest]. The bullish
  signal has a **14.3% historical win-rate** — it *confirms* not going long and
  invert-supports the bearish lean.
- **Kelly inputs:** b = **0.35** (recommended bear call spread: credit $1.30 / max
  loss $3.70), fraction = 0.25, cap_pct = 5.
- **Raw Kelly:** (0.143×0.35 − 0.857)/0.35 = **−2.31 (NEGATIVE)** → for any
  *directional-long* expression the edge is negative → **0%**. **Win-rate map:**
  p 0.143 < 0.50 → **starter / skip** (SHORT-side floor applies).
- **Risk gates:**
  - **Fundamentals (7b): VETO** → **directional size = watch-only / 0%**; defined-risk
    carry only.
  - **Sentiment/crowd (7c): CAUTION** (crowd_state BALANCED; Street one-sidedly
    bullish into a crashed name) → cut one size step.
  - **Correlation (phase-6/8): none** → no-op (DOCN absent from all ≥0.58 pairs).
  - **Sector rotation (phase-6): neutral** (tech inflow is *aligned* for the sector
    but DOCN is the idiosyncratic laggard; not adverse) → no cut.
  - **Debate (phase-8b):** bull_residual **0.72** vs bear_residual **0.62** →
    **disconfirmed = false** → no bin down-shift (but low-conviction survival).
- **Context modifier (phase-0.5):** `BUSY_NAME_NORMAL_DAY` → **no top-of-band sizing.**
- **Final size (Kelly-sized):** **0%** — raw Kelly is negative (bullish p 0.143) and
  the 7b VETO makes any directional allocation watch-only. The recommended bear call
  spread is a **discretionary defined-risk carry only** ("fundamentals-vetoed, carry
  only", 7b): if the desk elects to express the rich-vol/range view, cap its
  **max-loss at ≤ 1% of book** (starter) — this is *not* a Kelly-sized position and
  is not counted in `final_size_pct`.
- **Deviation reason:** none (upward deviation forbidden — gates fired; VETO holds
  the Kelly-sized allocation at 0%).

## Option structures

### Directional (primary) — WATCH-ONLY / 0% (fundamentals-vetoed)

- **Structure:** put debit spread (bearish) — **carry only if the 7b veto lifts on a
  confirmed 8/4 miss**; not for entry now.
- **Strike(s) / expiry:** buy $115P / sell $105P, **2026-08-21** (post-earnings)
- **Debit/credit:** ~$3.66 debit (115P ~$13.90 − 105P ~$10.24; rich IV)
- **Breakeven:** ~$111.34
- **Max loss:** $3.66 (defined — survives any 8/4 gap by construction)
- **Why this structure:** captures a guidance-gap-down through the 8/4 binary with
  capped risk; the spread (vs a naked put) mutes the post-earnings IV crush on the
  long leg. **Watch-only until a fundamental catalyst clears the VETO.**

### Defined-risk alternative — RECOMMENDED CARRY

- **Structure:** **bear call spread** (sell-upside, downside-skew-aware per phase-8b)
- **Strike(s) / expiry:** **sell $128C / buy $133C, 2026-07-31** (expires BEFORE 8/4
  earnings — no binary exposure)
- **Debit/credit:** ~**$1.30 credit** (est.; sell the rich 7/31 IV ~106%)
- **Breakeven:** ~$129.30
- **Max loss:** ~$3.70 (width $5 − credit $1.30) → size so this ≤ 1% of book
- **Why this structure:** sells the phase-3 **$128 call wall** (2,156 OI) and phase-4
  range top into a **long-gamma pin toward $120**; harvests IV rank 99 / VRP +0.434;
  bearish-lean matches the 8b downside skew; **avoids the 8/4 gap by expiring 7/31.**

## Macro overlay (cite phase-6)

- **Tailwinds:** [MACRO:sector_flow_persistence] Technology #1 inflow +$1.17B,
  persistence 0.8 (durable) — *but does not transfer to the DOCN laggard*;
  [MACRO:DTWEXBGS] USD softening (mild risk-support).
- **Headwinds:** [MACRO:DGS10] 10y 4.57% rising → duration/multiple pressure;
  [MACRO:FOMC_2026-07-29] hold-expected but ~25% hike-tail, no cut; [MACRO:MarketRegime]
  TRANSITIONAL/CHOPPY, breadth 38.4% bull → "half size, defined-risk, iron condors."
- **Net:** **mixed** (sector tailwind offset by rates/breadth + DOCN idiosyncratic weakness).

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|------|-------|------------------|
| 2026-07-29 | FOMC decision (hold likely, ~25% hike tail, no cut) | ? (hike = − for duration tech) |
| 2026-08-04 | **DOCN Q2 earnings** (guidance Q2 EPS 0.20–0.23 / FY 1.10–1.20) | ? (dominant binary; downside-skewed) |

Front-expiry implied move **±1.80% / $2.14** [CTX:implied_move]; the 8/4 earnings
move is far larger (8/7 IV 117.9%). The recommended 7/31 structure is deliberately
inside the pre-earnings window; the watch-only put spread is sized to survive the gap.

## Post-trade monitoring checklist

- [ ] Re-check **GEX regime** daily (phase-4) — a flip to NEGATIVE kills the range/pin premise.
- [ ] Watch **$128 call wall** — two closes above = invalidation (close the call spread).
- [ ] Track **cumulative premium flow** (phase-5) — 3 sessions net-bullish = squeeze risk building.
- [ ] Re-pull **insider MSPR / analyst revisions** (7b/7c) — any downgrade or fresh insider print reshapes the 8/4 setup.
- [ ] **Close/roll the 7/31 bear call spread before 8/4 earnings** — do NOT let it run into the binary.
- [ ] Monitor **7/29 FOMC** — a hike breaks the regime; reassess.

## Citations summary

1. [HIST:trend] DOCN −34% (`$180.50 → $118.91`), 30d — phase-5-historical.md §Price trajectory
2. [STRUCT:max_pain] near-expiry max-pain magnet **$120** (7/24 & 8/7) — phase-4-structure.md §Max pain
3. [HIST:signal_backtest] bullish_flow **win-rate 0.143 (n=7)** — phase-5-historical.md §Signal backtest
4. [OI:decrease_with_volume] 180C Nov **OI −430** (the "$985K bullish" print closed) — phase-3-positioning.md
5. [FUND:tier_adjustment] fundamentals **VETO** (2 contradictions) — phase-7b-fundamentals.md §Verdict
6. [AGENT] desk **0 directional votes** (3 RANGE / 2 NEUTRAL) — phase-8-agent-views.md
