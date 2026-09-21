# Phase A0 — Intake & Reuse Detection — MU — 2026-06-26

## Inputs
- **Ticker:** MU (valid, `^[A-Z][A-Z0-9.]{0,5}$`)
- **As-of:** 2026-06-26 (US/Eastern, default = today)
- **Version:** base (no prior `trade-plan.md` in `trade-plans/MU/2026-06-26/`)
- **Book risk overrides:** none (defaults: fraction 0.25, cap 5%)

## Output directory
- `trade-plans/MU/2026-06-26/` created. Immutability check passed — no existing
  `trade-plan.md`, so this is the **base** version.

## Reused deep dive
- **Path:** `research/MU/2026-06-25/` ✅ (has `decision.json` + full phase set
  `phase-0`…`phase-10`)
- **Age:** **1 calendar day** (1 trading session) vs as_of 2026-06-26 → **FRESH,
  not stale** (well within the 10-trading-day window). No staleness conviction
  cut. **L-0003 does NOT fire.**
- **Also available (older):** `research/MU/2026-06-23/` — superseded, ignored.
- **flow_source = `deep_dive`** (no live `uw` re-pull needed; A1 may name targeted
  gap-fills only).

### Deep-dive decision.json — headline substrate (do NOT re-pull)
- **bias = LONG, conviction = 0.55, horizon 1-3m**, spot_reference **1213.56**
- **Thesis (one line):** fundamentally cheap-on-forward (fwd P/E 8.4, 4/4 beats)
  leader of a confirmed memory supercycle and the **#1 single-name net-bullish
  premium in the universe (+$279M, calls 2.79x)** with price-and-flow aligned —
  **but the entry is wrong**: spot at the 1211-1213 double-top after a +15.8%
  earnings gap on a +325%-YTD parabola; dark pool balanced/distributive (mega
  buy_ratio 0.47); dealer long-gamma, max-pain pulling to 1040. **Structural
  long, but only on a pullback to the $1,134 absorbed shelf — token at spot.**
- **Levels:** support **1134**, resistance **1213**, largest_pin **1040**,
  gamma_flip null.
- **Entries:** primary **1134** (pullback to heaviest 5-session DP shelf);
  aggressive **1255** (decisive daily close above intraday high on rising IV);
  fade **1213** (rejection at 1211-1255 double-top → put-debit counter-trade).
- **Invalidation:** two daily closes below **1052** (6-23 pivot low / shelf
  failure); or DP tiers flip distributive (mega buy_ratio ≤0.45) / premium net-
  bearish 3 sessions; macro = DRAM/HBM rollover or hawkish FOMC ~Jul 28-29.
- **Sizing:** p 0.60, payoff_b 1.5, raw_kelly 0.333, fraction 0.25, cap 5% →
  **final_size_pct 0.3%** (token).
- **Gates:** fundamentals CAUTION, sentiment CAUTION, crowd_state **CROWDED_LONG**,
  sector_rotation aligned, debate_disconfirmed true.
- **Context:** unusual_verdict GENUINELY_UNUSUAL, universe_rank_net_dir **#1**,
  iv_rank 77.07, self_pctile_net_dir 98.1.
- **Expected move (front expiry):** ±3.93% (±47.39 abs).
- **Catalysts:** 2026-07-15 June CPI · 2026-07-17 July OPEX (17.27% of OI,
  put-heavy) · 2026-07-29 FOMC · 2026-09-22 MU earnings.

## Reasoning ledger (loaded)
`trade-plans/_eval/reasoning-ledger.md` read. Lessons matched to this setup:
- **L-0003 (stale flow)** — *not applicable* (deep dive is 1 day old).
- **L-0001 (don't full-size an unconfirmed breakout)** — *watch*: the aggressive
  1255 breakout entry must use a close-confirmation trigger + starter size.
- **L-0002 (divergent flow↔chart → neutral/fade only)** — *watch*: re-check after
  A2/A3. Flow is bullish (#1 net premium) but DP is distributive and price is at
  a double-top; if A2's chart read opposes the long, default to range/fade-only.
- **L-0004 (crowded directional + veto = trap)** — *partial*: this is a CROWDED_LONG
  with fundamentals/sentiment CAUTION; respect the crowd-state and the bear's
  strongest point (distribution-into-strength). Don't manufacture full-size
  conviction at the ATH.

`sources.ledger_lessons_applied` (carry to A3/A4): **L-0001, L-0002, L-0004**.

## Chart source probe (smoke test, not analysis)
- `chart_engine.py --ticker MU --date 2026-06-26` → **`available: true`**,
  **source = yfinance** (372 daily sessions). spot 1213.56 (matches deep dive).
  ma_stack bullish_stack, RSI14 64.5 (neutral), ATR% 8.53. **B1 is NOT a gap.**

## Tool errors
- None. All probes returned clean.

## Verdict for downstream
- `deep_dive_reused = research/MU/2026-06-25/` · `deep_dive_age_days = 1` (FRESH)
- `flow_source = deep_dive`
- `chart_source = yfinance` (available)
- `ledger_lessons = [L-0001, L-0002, L-0004]` → thread into A3/A4
- Headline tension to resolve downstream: **bullish flow (#1 universe) vs
  distributive dark pool + double-top price + long-gamma/max-pain-1040 cap** →
  the deep dive's own answer is *structural long on a $1,134 pullback, token at
  spot*. A1 grades gaps; A2 reads the chart; A3 fuses; A4 writes the two-sided plan.
