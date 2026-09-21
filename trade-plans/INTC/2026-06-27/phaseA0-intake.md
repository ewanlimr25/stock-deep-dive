# Phase A0 — Intake & Reuse Detection — INTC

**Ticker:** INTC (US-listed equity, NASDAQ) · **As-of:** 2026-06-27 (US/Eastern) · **Version:** v1

## Inputs
- Ticker validated: `INTC` matches `^[A-Z][A-Z0-9.]{0,5}$`.
- As-of date: 2026-06-27 (default = today). All look-backs `<= as_of`.
- Book risk overrides: none → defaults (fraction 0.25, cap 5%).
- Output dir: `trade-plans/INTC/2026-06-27/` (newly created; no prior files → v1).

## Reused deep dive
- **Path:** `research/INTC/2026-06-26/` — has `decision.json` + full phase set (phase-0 … phase-10).
- **Age:** 1 calendar day (0 trading days) vs as_of → **NOT stale** (well within the 10-trading-day window). L-0003 staleness cut does **not** apply.
- **Also available (older):** `research/INTC/2026-06-15/` (superseded; not used).
- **flow_source = `deep_dive`.** Full flow / dark-pool / OI / dealer-structure / historical / macro / fundamentals / sentiment / debate substrate reused from 2026-06-26. No live re-pull needed.

### Deep-dive headline (from decision.json)
- **Bias:** SHORT · **conviction 0.55** · horizon 1–4w · spot_ref **$128.30**.
- **final_size_pct = 0.0** → bias is **watch-only**; expressed only as small defined-risk spreads, flat before Jul-23 earnings.
- **Thesis core:** +247.75% YTD parabola, only loss-maker in peer group, 29–33% above $102.70 analyst target; price-vs-flow bearish DIVERGENCE (+10.7% price / −$50.9M flow); 5/5-session bearish sweep campaign ($925.2M); ~73% bearish new OI led by Jul-17 $130 put +11,442 — into hawkish-Fed / tech-outflow macro.
- **But VETOED:** 4/4 earnings beats, insiders buying, long-gamma pin → `gates.fundamentals = VETO`, `crowd_state = CROWDED_LONG`.
- **Levels:** support 120, resistance 130, gamma_flip (ZGL) 27.26, largest_pin 125. Gamma pins +5.34M @120 / +4.16M @130.
- **IV rank 94.1**, expected move ±22% (±$28.2) to Jul-17. **VRP +5.95 → PREMIUM_SELLING** regime.
- **Catalysts:** June CPI ~Jul-15 · monthly OPEX Jul-17 · **INTC Q2 earnings Jul-23 AMC (DO NOT hold through)** · FOMC Jul-29.
- **Recommended structures (carry-only, max-loss ≤0.5% book):** (1) bear put debit 128/120 Jul-17 (debit ~$4, BE $124); (2) bear call credit 135/140 Jul-17 (credit ~$1.5, BE $136.5).

## Reasoning ledger (loaded `trade-plans/_eval/reasoning-ledger.md`)
- **L-0002 — DIVERGENT flow↔chart is not a directional trade** · status **ACTIVE** · scope `setup:divergent`. → **APPLIES.** Bearish flow vs. a raging bull chart stack is the textbook divergence; default NEUTRAL/RANGE or defined-risk fade only, never full directional size. Log divergence as top reason_against. Thread into A3 bias + conviction.
- **L-0004 — Bearish-sweep short in short-gamma + bullish catalyst + VETO = trap** · status **CANDIDATE** · scope `setup:divergent, setup:fundamentals-veto, signal:bearish-sweep, structure:short-gamma`. → **PARTIAL / related.** This INTC setup shares divergent + fundamentals-veto + bearish-sweep tags, **but structure is LONG-gamma (pin), not short-gamma** — so the "zero-gamma reclaim squeezes up" mechanic differs. Carry as a cautionary prior on A3/A4 (respect the VETO and the bear's strongest unrefuted point; don't carry bearish premium into the undated bullish catalyst = earnings), not as a binding rule.
- **L-0001 — don't size a breakout at full until the break holds** · ACTIVE · `pattern:triangle/flag`. → evaluate after A2 pattern read.
- **L-0003 — stale flow decays** · ACTIVE · `setup:reused-deep-dive`. → **does NOT apply** (deep dive is 1 day old).
- `ledger_lessons_applied` (to carry into A4): **L-0002**, **L-0004 (partial)**; L-0001 pending A2.

## Chart source probe (smoke test)
- `chart_engine.py --ticker INTC --date 2026-06-27` → **`available: true`**, **source = `yfinance`** (373 daily sessions).
- Spot $128.32 (chart) ≈ $128.30 (deep dive) — price unchanged day-over-day.
- Snapshot indicators: ma_stack **bullish_stack** (spot > sma20 119.42 > sma50 108.39 > sma200 58.23), RSI14 56.78 (neutral), MACD hist +0.481 (bullish), ATR14 9.97 (8.42%), BB 96.47–142.37. → chart is structurally bullish; B1 is **not** a gap.
- No tool errors.

## Verdict for downstream
- `deep_dive_reused`: **research/INTC/2026-06-26** (age **1 day**, fresh)
- `flow_source`: **deep_dive**
- `chart_source`: **yfinance** (373 sessions)
- `ledger_lessons`: **L-0002** (ACTIVE, apply), **L-0004** (CANDIDATE, partial/cautionary); L-0001 pending A2; L-0003 n/a
- Setup signature so far: **DIVERGENT (bearish flow ⟂ bullish chart) + fundamentals VETO + long-gamma pin + IV-rank-94 / PREMIUM_SELLING + hard earnings stop Jul-23.** Expect A1 → likely USABLE/USABLE_WITH_GAPS; A3 → NEUTRAL-to-bearish, low conviction, defined-risk only.
