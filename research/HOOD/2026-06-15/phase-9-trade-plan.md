# Phase 9 — Trade Blueprint

**Ticker:** HOOD
**As-of date:** 2026-06-15
**PM voice:** desk PM running an institutional options-overlay book
**Spot reference:** $98.12 (phase-0.5 / screener close; structure tools ref $98.14–98.59)
**Upstream phases cited:** phase-0.5 through phase-8b

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

HOOD shows genuine but **late-cycle** institutional accumulation (dark-pool buy/sell
**1.7**, mega-tier buy_ratio **1.0** [DP:block_stratified]) sitting on a long-gamma
dealer-buy floor [STRUCT:gex] — but the same instrumentation **caps it**: a four-way
**$100 ceiling** (gamma wall +$18.17M [STRUCT:gex], call-wall OI +98,818
[OI:oi_by_strike], analyst target $102.91 [FUND:recom fz]) just +2% above spot, while
the matching **bullish_flow signal backtests only 28.6% (n=7)** [HIST:signal_backtest]
into a +28%/30-session, RSI-65 extended move. The desk is **3-of-4 RANGE**
[AGENT:phase-8] and the bull/bear debate **disconfirmed a fresh long** (bull 0.55 /
bear 0.65 [DEBATE]) — so this is a capped **$92–100 range, not a chase**: accumulate
only on a $92–93 pullback or a confirmed >$100.53 breakout, defined-risk, starter size.

## Bias + conviction + horizon

- **Directional bias:** **RANGE** (constructive-but-capped; long *lean* only on a
  pullback/breakout, no fresh directional position at spot).
- **Conviction (M-01 bin):** **0.55** (slight edge / mixed).
- **Time horizon:** 1-4w.
- **Why this bin:** phase-10 confluence ≈ **58** (50–64 band → recommended bin 0.65),
  conservatively **down-shifted one bin to 0.55** for the phase-8b disconfirmation +
  negative directional Kelly (p<0.50); the range read is moderately confident but the
  directional edge is slight and two-sided.

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| Primary    | $92–93 | tag of DP support / $95 gamma-wall hold → accumulate long (defined-risk) | [DP:price_levels][STRUCT:gex] |
| Aggressive | >$100.53 | confirmed daily close above on elevated volume (gamma flip above the wall → dealer chase) | [STRUCT:today_gamma_flip][OI:oi_by_strike] |
| Fade       | $99.7–100.5 | rejection at the $100 call/gamma wall → counter-trade the rip (sell $100, the range top) | [OI:oi_by_strike][DP:price_levels] |

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Support | $92–93 (then base $83.77–$86.36) | [DP:price_levels] |
| Resistance | $100 (then $105/$110) | [OI:oi_by_strike] call_wall_resistance / [STRUCT:gex] gamma wall |
| Gamma flip (ZGL) | ~$23–26 (far below → long-gamma all the way down) | [STRUCT:gex] |
| Pin magnet (6/18 max-pain) | $85 | [STRUCT:max_pain] |

Price-context color: RSI **65** and price **+17/21% above SMA20/50**, **−36% below the
52-week high $153.86** [HIST:rsi fz][HIST:52w_proximity fz] — extended near-term; this
is why the **primary entry is the $92–93 pullback, not the $98 chase** (narrative color
only; does not alter sizing).

## Invalidation

- **Price-based:** two daily closes **below $92** (loses the DP support shelf and breaks
  the accumulation structure) → range-floor broken, downside opens toward the $85
  max-pain. Symmetrically, two daily closes **above $100.53** flips the range to a
  breakout-long (not a bear invalidation, but it ends the range thesis).
- **Signal-based:** institutional_accumulation flips to **distribution** (phase-7
  buy/sell ratio < 1.0) OR **GEX flips negative** on the phase-4 daily refresh — the
  long-gamma dealer-buy floor disappears and downside accelerates (the regime has
  flipped 13× in 30d, so this is live) [STRUCT:gex][INSIGHT:institutional_accumulation].
- **Macro-based:** a **hawkish FOMC surprise on 6/17** (dots/presser more restrictive
  than the 99.6%-priced hold) OR a UW regime flip to **RISK-OFF** → the 2.34-beta name
  gaps toward $85 [MACRO:FOMC_2026-06-17][MACRO:MarketRegime_2026-06-15].

## Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** p_raw = **0.286** (n=**7**, source=**backtest**) → N-cap
  (n<10 → 0.75) → **p = 0.286** `[HIST:signal_backtest]`.
- **Kelly inputs:** b = **0.5** (illustrative long $98→$100 target, $94 stop),
  fraction = 0.25, cap_pct = 5.
- **Raw Kelly:** (0.286×0.5 − 0.714)/0.5 = **−1.14 → NEGATIVE edge.** Win-rate map: p
  0.286 **< 0.50 → starter/skip** (SHORT-side floor: directional must be starter or
  skip). A negative-Kelly directional long is **not a position**.
- **Risk gates:**
  - Fundamentals (phase-7b): **CAUTION** → cut one size step.
  - Sentiment/crowd (phase-7c): **CONFIRM** (BALANCED) → no-op.
  - Correlation cluster (phase-6/8): **none** (HOOD–INTC `high_correlations` null) → no-op.
  - Sector rotation (phase-6): **aligned** (Tech +$7.78B, persistence 1.0) → no-op.
  - Debate (phase-8b): bull_residual **0.55** vs bear_residual **0.65** → **disconfirmed
    = true** → down-shift bin one (→0.55) + cut one size step.
  - Context (phase-0.5): **GENUINELY_UNUSUAL** → no-op (edge already in p).
- **Final size:** **`final_size_pct = 0.0` — directional long SKIPPED** (negative Kelly
  −1.14, p<0.50, plus CAUTION + disconfirmation gates; the Kelly ceiling is 0). The
  Kelly-sized directional position is therefore **zero**. Any defined-risk RANGE
  structure below is **desk-discretion carry only, ≤1.0% of book max-loss** — it is
  *not* a Kelly-sized directional bet (its edge is the long-gamma pin, not bullish_flow).
  Preferred action: **WATCH** for the $92–93 pullback or the >$100.53 breakout before
  committing any directional risk.
- **Deviation reason:** none (no upward deviation; multiple gates fired).

## Option structures

**Front-expiry implied (expected) move: ±4.65% / ±$4.55** on $98.12 [CTX:implied_move_pct]
→ priced range ≈ **$93.6–$102.7**, which closely tracks the structural $92–$100/103 band.

### Directional (primary — conditional, enter on $92–93 pullback)

- **Structure:** call debit spread (bullish lean, cheap-vol-aligned).
- **Strikes / expiry:** long $95C / short $102C, **2026-07-17** (skips the 6/18
  FOMC+quad-witch binary; $95 = gamma support wall, $102 ≈ $100 wall + analyst target).
- **Debit/credit:** ~**$3.30 debit** (illustrative).
- **Breakeven:** ~$98.30.
- **Max loss:** $3.30 (the debit) — size so max-loss ≤ 1.0% of book.
- **Why this structure:** VRP −0.10 (IV 63% < realized 73%) favors **buying** premium,
  not selling [HIST:vrp]; the $7 width exceeds the ±$4.55 expected move (doesn't cap
  before the move completes); 7/17 avoids the 6/18 event. **Do not enter at $98** — the
  RR only works from the $92–93 pullback (most of $95→$100 is already captured at spot).

### Defined-risk alternative (range / pin expression)

- **Structure:** iron condor (profits from the $92–100 pin).
- **Strikes / expiry:** sell $100C / buy $104C **and** sell $92P / buy $88P,
  **2026-07-02** (prefer to leg in **after** the 6/18 quad-witch to capture the cleaner
  post-OPEX pin). Short strikes anchored to the $100 wall and the $92 DP support.
- **Debit/credit:** ~**$1.30 net credit** (illustrative).
- **Breakevens:** ~$90.70 / ~$101.30.
- **Max loss:** $4 − $1.30 = **$2.70** per side — size so max-loss ≤ 1.0% of book.
- **Caveat:** short premium into **high realized vol (73%)** + the FOMC/OPEX cluster — a
  full expected-move (±$4.55) gap breaches the call breakeven ($101.30 vs $102.7), so
  this is **starter-size, defined-risk, post-event-entry only**; the cap bounds the loss.

## Macro overlay (cite phase-6)

- **Tailwinds:** Technology sector inflow **+$7.78B, persistence 1.0**
  [MACRO:SectorFlow_2026-06-15]; steady labor (unemployment 4.3%, NFP +172k)
  [MACRO:PAYEMS_2026-05]; SpaceX-IPO demand driving record HOOD traffic [SENT:news]
  (event-driven, durability unproven).
- **Headwinds:** regime **TRANSITIONAL**, breadth 37.1% bullish ("reduce size")
  [MACRO:MarketRegime_2026-06-15]; sticky **CPI 4.3% YoY** [MACRO:CPIAUCSL_2026-05];
  **FOMC 6/17 + quad-witch OPEX 6/18** event cluster; high **beta 2.34** [FUND:metric].
- **Net:** **mixed/neutral** — sector tailwind offset by a cautious broad tape.

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|------|-------|------------------|
| 2026-06-17 | FOMC decision (99.6% no-change priced) | ? (presser/dots tail-risk; likely inside ±4.65%) |
| 2026-06-18 | June quad-witch OPEX (Juneteenth-shifted) | pin (gravity $98–100; max-pain $85) |
| 2026-08-05 | HOOD Q2 earnings | + (out of 30d window; noted, not traded near-term) |

## Post-trade monitoring checklist

- [ ] Re-check phase-2 dark-pool **buy/sell ratio daily** — a flip below 1.0 =
  distribution = signal invalidation.
- [ ] Watch **GEX/DEX** on the phase-4 daily refresh — GEX flip negative removes the
  long-gamma floor (13 flips/30d — unstable).
- [ ] Track **$100.53** (breakout trigger) and **$92** (range-floor break) on a closing
  basis; do not act intraday on either without a close.
- [ ] Reassess **after the 6/17 FOMC + 6/18 OPEX clear** — only then consider the
  post-event iron condor or a confirmed breakout long.
- [ ] Monitor **SpaceX-IPO traffic durability** — is the volume tailwind sustaining, or
  was it a one-off event spike?
- [ ] Watch **cumulative premium flow** — 3 consecutive net-bearish sessions = thesis
  weakening (it is already MIXED, −$16M/46 sessions).

## Citations summary

1. `[DP:block_stratified]` mega buy_ratio **1.0** / block **0.85** / large **0.581** —
   accumulation (phase-2-dark-pool.md §Tier breakdown).
2. `[STRUCT:gex]` **$100 gamma wall +$18.17M**, regime POSITIVE, ZGL ~$26
   (phase-4-structure.md §GEX).
3. `[HIST:signal_backtest]` bullish_flow **win_rate 0.286 (n=7)**
   (phase-5-historical.md §Signal backtest).
4. `[OI:oi_by_strike]` $100 call_wall_resistance **net_oi +98,818**
   (phase-3-positioning.md §OI walls).
5. `[DEBATE]` disconfirmed **true**, bull 0.55 / bear 0.65 (phase-8b-debate.md §Verdict).
