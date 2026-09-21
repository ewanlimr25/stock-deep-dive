# Phase 9 — Trade Blueprint

**Ticker:** RDDT
**As-of date:** 2026-05-22
**PM voice:** desk PM running an institutional book
**Spot reference:** $141.67 (phase-0.5 / phase-7 `uw_screener` close)
**Upstream phases cited:** phase-0.5 through phase-8b

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

RDDT printed its **most net-bearish flow day in 31 sessions** (net −$6.98M,
self-pctile 0.0 `[CTX:self_pctile]`) through **call-selling + put-buying**
(dated bullish $12.19M vs bearish $19.54M `[FLOW:aggressor_ex0dte]`) into a
**fully short-gamma dealer book** (GEX −$11.66M, no flip `[STRUCT:gex]`) that will
mechanically accelerate a break of 140 — **but** that bearish signal has only a
**30% historical win-rate** (`[HIST:signal_backtest]`, n=10), the underlying is
*accelerating* (revenue +70.6%, EPS +460%, 4/4 beats, PEG 0.095 `[FUND]`) which
**vetoes a conviction short**, and the analyst desk endorsed **zero shorts**
(`[AGENT]`, contrarian-scanner the lone directional call at LONG-fade). Net: a
genuinely **two-sided, low-edge, short-gamma whip** — the edge is at the *boundaries*
(140 break / 147–150 reclaim), not mid-range.

## Bias + conviction + horizon

- **Directional bias:** **NEUTRAL** (range-bound, boundary-traded; mild fade-long
  lean off 140 support, but disconfirmed — see phase-8b)
- **Conviction (M-01 bin):** **0.55**
- **Time horizon:** 1–5d tactical (boundary triggers); 1–4w if a boundary breaks
- **Why this bin:** the phase-8b debate ended in a tie (bull 0.65 / bear 0.65 →
  disconfirmed), the bear signal is negative-edge, and the desk took no clean side —
  this is "slight edge / coin-flip plus a sliver," the floor bin. (Phase-10 confluence
  band expected LOW; will confirm.)

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| Primary | $141.67 (spot) | **WATCH — no mid-range edge**; await a boundary | `[STRUCT:gex]` |
| Aggressive (bear) | < $140 | confirmed break + no reclaim → short-gamma accelerant toward ~$120 | `[STRUCT:gex]` `[HIST:gex_time_series]` |
| Fade (bull) | $141.5–142 | hold of the 141.67 block-buy shelf; vanna/squeeze coil fires up | `[DP:price_levels]` `[STRUCT:vanna_charm]` |
| Fade (counter, sell) | $146–147 | rejection at the $137M DP supply node | `[DP:price_levels]` |

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Support | $141.5–141.7 (then $140) | `[DP:price_levels]` (block buys) / `[STRUCT:gex]` (gamma cluster) |
| Resistance | $146–147 (then $150) | `[DP:price_levels]` ($137M node) / `[STRUCT:gex]` (first positive-GEX shelf) |
| Gamma flip | none in 45 DTE (fully short γ); 0DTE flip $103 | `[STRUCT:gex]` (ZGL null) / `[STRUCT:today_gamma_flip]` |
| Largest pin | none this expiry; soft 190 (call-writes) / 120 (standing put OI 5,678) | `[OI:pin_risk]` absent / `[OI:decrease_with_volume]` |

## Invalidation

- **Price-based:** for a **bear** boundary play — two daily closes back **above
  $147** (reclaims the DP supply node, voids the break) `[DP:price_levels]`. For a
  **bull/fade** play — two daily closes **below $140** (short-gamma accelerant arms
  the downside toward ~$120) `[STRUCT:gex]` `[HIST:gex_time_series]`.
- **Signal-based:** GEX flips to a **POSITIVE** regime / DEX turns positive on the
  daily refresh `[STRUCT:gex]` `[STRUCT:dex]` (short-gamma resolves → the whip
  thesis is gone); OR `insights_institutional_accumulation` flips to **DISTRIBUTION**
  `[INSIGHT:institutional_accumulation]`; OR cumulative premium flow turns one-way
  for 3 consecutive sessions `[HIST:cumulative_premium_flow]`.
- **Macro-based:** a **hawkish FOMC surprise 2026-06-16/17** `[MACRO:FOMC]`; OR a
  definitive **Meta "Forum" adoption headline** (either direction) that re-rates the
  competitive thesis `[MACRO:RDDT_news]`; OR a UW regime flip to **RISK-OFF**
  `[MACRO:MarketRegime]`.

## Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** p_raw = **0.30** (n=10, source=backtest, signal_class
  `bearish_flow`) `[HIST:signal_backtest]`. N-cap (10≤n<20) = 0.85 → **p = min(0.30,
  0.85) = 0.30**.
- **Kelly inputs:** b ≈ 1.7 (bear put-spread target/stop), fraction = 0.25, cap_pct = 5.
- **Raw Kelly:** (0.30×1.7 − 0.70)/1.7 = **−0.11 → NEGATIVE EDGE**. Per rubric, a
  negative-edge signal forces the directional action to **NEUTRAL or the opposite
  side** — the bearish short is a **SKIP**. **Win-rate map:** p=0.30 < 0.50 →
  starter/skip; **SHORT-side floor** → short is starter/skip regardless of Kelly.
- **Risk gates (each cuts, none adds):**
  - **Fundamentals (7b): VETO** → directional short = **watch-only / 0%** (business
    accelerating on ≥2 axes; flow read as profit-taking, not distribution).
  - **Sentiment/crowd (7c): CAUTION** (crowd_state BALANCED; **14.65% SI squeeze
    risk** + stable-bullish analysts + +2.77σ contrarian P/C) → cut one step.
  - **Correlation cluster (phase-6/8): none** — RDDT max pairwise corr 0.575 (SYM),
    < 0.60 soft-watch line (DuckDB-verified) → **no-op**.
  - **Sector rotation (phase-6/8): adverse but soft** — Comm Services net-directional
    outflow −$49.2M today, but 5-day gross persistence INFLOW → **cut half step**.
  - **Debate (phase-8b): DISCONFIRMED** — bull 0.65 vs bear 0.65 (tie) → **down-shift
    bin one + cut one step**. Quoted: no clean directional edge either way.
  - **Context (phase-0.5): GENUINELY_UNUSUAL** → no-op (edge already in p); but the
    edge is *negative*, so no top-of-band sizing.
- **Final size:** **0% directional core (WATCH).** A single boundary-triggered,
  **defined-risk debit structure** may be carried at **≤ 0.5% of book risk (starter)**
  — NOT both sides, NOT naked, only on a confirmed boundary trigger.
- **Deviation reason:** none (sized **down** from suggested — always permitted; an
  upward deviation is forbidden here, multiple gates fired).

## Option structures

Premium-buying regime (VRP −0.05, IV rank 18.7 `[HIST:vrp]`) → **debit structures
only**; do not sell vol. No earnings in window (7/30); both expiries clear the
6/16–17 FOMC with defined risk. Sized to the IV-derived expected move (see N4 below).

### Directional (primary) — the bear / Forum-break expression

- **Structure:** Put debit spread (long 140P / short 120P) — **bearish, carry only,
  fundamentals-VETOED + sentiment-CAUTIONED, trigger only on a confirmed close < 140**
- **Strikes / expiry:** **140 / 120 put spread, 2026-07-17** (56 DTE; past FOMC,
  before 7/30 earnings). Strikes anchored to the 140 gamma-cluster floor `[STRUCT:gex]`
  and the standing 120P OI (5,678) downside magnet `[OI:decrease_with_volume]`.
- **Debit/credit:** ≈ **$6.5 debit** (illustrative; 140P ~$11.5, 120P ~$5.0 at ~62% IV)
- **Breakeven:** ≈ **$133.5**
- **Max loss:** ≈ **$6.5** (the debit) · **Max gain:** ≈ $13.5 (width 20 − debit)
- **Why this structure:** cheap IV makes the long-put leg attractive (`[STRUCT:term_skew]`
  COMPLACENT — puts under-priced); the short 120P caps cost and sits at the standing
  put-OI floor; max loss = debit means even a FOMC/Forum gap cannot exceed the stop.
  **Only fires on a confirmed 140 break** — otherwise WATCH.

### Defined-risk alternative — the fade / squeeze expression

- **Structure:** Call debit spread (long 145C / short 160C) — **bullish/fade, if 140
  holds and the vanna/squeeze coil fires** `[STRUCT:vanna_charm]`
- **Strikes / expiry:** **145 / 160 call spread, 2026-07-17.** Long strike just above
  the 146–147 DP supply `[DP:price_levels]`; short strike at the 160 positive-GEX
  shelf `[STRUCT:gex]` / prior 5/29 call-build zone.
- **Debit/credit:** ≈ **$5.0 debit** (illustrative)
- **Breakeven:** ≈ **$150** · **Max gain:** ≈ $10 (width 15 − debit) · **Max loss:** ≈ $5.0
- **Why:** debit (premium-buying regime ✓), defined-risk; expresses the contrarian
  bounce (P/C +2.77σ extreme, 14.65% SI squeeze fuel, fundamentals strong) without
  selling cheap vol. Trigger: reclaim/hold of 142 with the 141.67 DP shelf intact.

**N4 expected-move check:** screener `implied_move_perc` 0.56% is a 1-day figure;
the IV30d-derived move is **±~8% (5/29 weekly), ±~17.8% (30d), ±~24% (to 7/17,
56DTE)** → range ≈ $108–176. Both spreads (140/120 and 145/160) sit **well inside**
the 56-DTE expected move, so neither caps the move before it can complete. A single
FOMC gap (beta 2.15) cannot exceed the defined-risk max loss. ✓

## Macro overlay (cite phase-6)

- **Tailwinds:** Fed funds 3.62% easing `[MACRO:DFF]`; soft-landing labor (UNRATE
  4.3%) supports ad demand `[MACRO:UNRATE]`; sell-side bullish (avg PT ~$225, +58%)
  `[MACRO:RDDT_analysts]`.
- **Headwinds:** **Meta "Forum" competitive launch** `[MACRO:RDDT_news]`; Comm
  Services biggest net-directional sector outflow −$49.2M `[MACRO:SectorRotation]`;
  TRANSITIONAL regime (half-size) `[MACRO:MarketRegime]`; sticky headline CPI +0.64%
  MoM `[MACRO:CPIAUCSL]`.
- **Net:** **mixed-to-headwind** (idiosyncratic Meta-Forum threat dominant; offset by
  easing Fed + bullish street).

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|------|-------|------------------|
| 2026-06-16/17 | FOMC + dot plot/SEP | ? (rates/risk-sentiment) |
| ~2026-06-10/11 | May CPI release | ? |
| 2026-06-19 | June OPEX / quad witching | mechanical (gamma reset) |
| ongoing | Meta "Forum" adoption headlines | ± (the live idiosyncratic driver) |
| 2026-07-30 | RDDT Q2 earnings | **outside window** (structures expire 7/17) |

## Post-trade monitoring checklist

- [ ] **Re-check GEX/DEX daily** `[STRUCT:gex/dex]` — a flip to POSITIVE regime kills
      the short-gamma whip thesis and the 140-break accelerant.
- [ ] **Watch the 140 / 147 boundaries** intraday — these are the only entry triggers;
      no mid-range adds.
- [ ] **Monitor Meta "Forum" adoption / Reddit DAU & ad-revenue headlines**
      `[MACRO:RDDT_news]` — the single fact that resolves the bull/bear tie.
- [ ] **Track short interest / borrow** `[SENT:short_interest]` — a rising SI + HTB
      tag escalates squeeze risk against any short; a falling SI relieves it.
- [ ] **Re-run dark-pool block tier daily** `[DP:block_stratified]` — a flip from the
      0.735 dip-buy to distribution invalidates the 141 support shelf.
- [ ] **FOMC 6/16–17** `[MACRO:FOMC]` — defined-risk caps the gap, but reassess regime
      after.

## Citations summary (M-04 — ≥3 distinct upstream datapoints)

1. `[FLOW:aggressor_ex0dte]` — ex-0DTE dated bullish $12.19M vs bearish $19.54M
   (genuine net-bearish flow: calls sold + puts bought) — phase-1-flow.md §Aggressor split.
2. `[STRUCT:gex]` — total GEX −$11,655,250, FULLY_NEGATIVE, no zero-gamma flip
   (short-gamma amplification, spot in 140–145 cluster) — phase-4-structure.md §GEX.
3. `[HIST:signal_backtest]` — `bearish_flow` win-rate **30%** (n=10) → negative Kelly
   edge — phase-5-historical.md §Signal backtest.
4. `[FUND]` — revenue +70.6% YoY, EPS +460% YoY, 4/4 beats, PEG 0.095 → 7b VETO of a
   short — phase-7b-fundamentals.md §Verdict.
5. `[AGENT]` / `[DEBATE]` — desk endorsed zero shorts; phase-8b disconfirmed
   (bull 0.65 = bear 0.65) — phase-8-agent-views.md, phase-8b-debate.md.
