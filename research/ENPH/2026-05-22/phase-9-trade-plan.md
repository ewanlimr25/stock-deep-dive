# Phase 9 — Trade Blueprint

**Ticker:** ENPH
**As-of date:** 2026-05-22
**PM voice:** desk PM running an institutional options-overlay book
**Spot reference:** $64.03 (phase-2 close; intraday $63.93 phase-4)
**Upstream phases cited:** phase-0.5 through phase-8b

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

The ENPH tape is genuinely bullish — dark-pool block accumulation at **95.3% buy**
`[DP:block_stratified]` plus **+4,616 ask-driven June $70C opening longs**
`[OI:biggest_increases]` on a 5/5-session sweep campaign — but the move is a
**largely-spent short squeeze** (32.53% float short, 4.5× peers `[SENT:short_interest]`)
on a **deteriorating core** (Q1'26 revenue −18% QoQ, GAAP loss `[FUND]`) that has already
**doubled to above the GS $57 target** into a TRANSITIONAL macro regime
`[MACRO:MarketRegime_2026-05-22]`. Dealers **pin $60–65** (long-gamma; $65 = 3.5M-GEX wall
`[STRUCT:gex]`) with a **+$508M DEX squeeze coil** that only fires above $65 — so this is a
**binary level trade, not a trend**, and the bear **disconfirmed** the unconditional long
(residual 0.70 vs 0.55 `[DEBATE]`). Net: a **token, trigger-gated long above $65,
defined-risk only**, with a symmetric defined-risk fade below $60.

## Bias + conviction + horizon

- **Directional bias:** **LONG** — *conditional/token* (plurality of signal phases 1,2,3,7
  is bullish; the gates cut size, not bias). Practically a **stand-aside with a $65 trigger**.
- **Conviction (M-01 bin):** **0.55** (slight edge).
- **Time horizon:** **1-4w** (unanimous across the phase-8 desk).
- **Why this bin:** anticipated phase-10 confluence ≈ low-30s (signal phases bullish but
  fought by phase-4 pin, phase-5 extension, phase-6 headwind, phase-7b BEARISH), then
  −5 (8b disconfirmed) −5 (7c CAUTION) → **band 30–49 → 0.55**, with the 8b down-shift
  pinning it to the floor.

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| Primary (long) | **$65.00+** | **Confirmed break AND hold above the $65 gamma wall on volume** (flips local gamma short → dealer chase) | `[STRUCT:gex]` $65 wall 3.5M / `[STRUCT:dex]` +$508M |
| Aggressive (long) | **$62.34** | Pullback into the recent DP support shelf that holds intraday | `[DP:price_levels]` $62.34 cluster |
| Fade (plan-B, short) | **$60.00** | Loss of the $60 gamma/OI floor → flip to put-debit-spread toward $53.15 | `[STRUCT:gex]` $60 floor / `[DP:price_levels]` $53.15 shelf |

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Resistance | **$65.00** (then $70 magnet) | `[STRUCT:gex]` 3.5M-GEX wall / `[OI:biggest_increases]` 70C +4,616 |
| Support | **$62.34** (then $61.11, $60 floor) | `[DP:price_levels]` / `[STRUCT:gex]` $60 |
| Gamma flip | ZGL **$17.59 — NOT usable** (deep-ITM artifact); effective pivot = $65 wall / $60 floor | `[STRUCT:gex]` |
| Largest pin | **None in OPEX week** (next monthly 6/18 = 27 DTE); deep structural OI at $50 | `[OI:pin_risk]` (ENPH absent) |
| Disaster shelf | **$53.15** ($48.4M DP cluster) | `[DP:price_levels]` |

## Invalidation

- **Price-based:** **Two daily closes below $60** (gamma/OI floor) → long invalid; or a
  break above $65 that **fails to hold/reclaim** within the session → exit the trigger long.
- **Signal-based:** dark-pool **ACCUMULATION reverses to DISTRIBUTION**
  (`insights_institutional_accumulation` flips, phase-7), OR the conviction matrix flips
  **DIRECTIONAL_LONG → HEDGED_LONG** `[INSIGHT:conviction_matrix]`, OR cumulative premium
  flow turns net-bearish 3 consecutive sessions `[HIST:cumulative_premium_flow]`.
- **Macro-based:** **hawkish FOMC dot-plot surprise (June 16-17)** or a **hot May CPI
  (~June 10-11)** `[MACRO:FOMC_2026-06-17]` — either intensifies the rate-sensitive solar
  headwind; or UW regime flips to **RISK-OFF** `[MACRO:MarketRegime]`.

## Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** p_raw = **1.00** (n=**8**, source=**backtest**) → N-cap (n<10 →
  0.75) → **p = 0.75** `[HIST:signal_backtest]`.
  - *Caveat (phase-5):* the backtest is **market-wide, not ENPH-specific, and a
    bull-regime artifact** — quoted per rubric, but treated as unreliable; the gates below,
    not this p, govern the result.
- **Kelly inputs:** b = **1.6** (call debit spread max-profit/max-loss), fraction = 0.25,
  cap_pct = 5.
- **Raw Kelly:** (0.75×1.6 − 0.25)/1.6 = **0.59** → ×0.25×100 = 14.8% → **capped at 5%**.
  **Win-rate map** (p=0.75 ≥0.70 → full) ceiling = **5%**. Pre-gate = **5%**.
- **Risk gates** (each cuts; none adds):
  - **Fundamentals (7b): CAUTION** → cut one step (full→half): 5% → **2.5%**.
  - **Sentiment/crowd (7c): CAUTION, CROWDED_LONG** → cut one step (half→starter): 2.5% → **1.25%**.
  - **Correlation cluster: none live** — only sibling SYM is a placeholder (no concurrent
    correlated blueprint) → no-op. *(Latent solar cluster ENPH/TAN 0.76, ENPH/SEDG 0.72
    flagged by phase-8 risk-monitor — applies only if a solar name is added.)*
  - **Sector rotation: NEUTRAL** — UW tags ENPH "Technology" (persistent INFLOW), so the
    out-rotation gate does **not** fire (the true-solar-peer adversity is already in the
    thesis) → no-op.
  - **Debate (8b): DISCONFIRMED** (bull_residual 0.55 < bear_residual 0.70) → down-shift
    bin (already 0.55) + cut one step: 1.25% → **~0.6%**.
- **Context modifier (phase-0.5):** `GENUINELY_UNUSUAL` → no-op (edge already in p; no
  top-of-band penalty needed — moot here given the cascade).
- **Final size:** **0.5% of book risk** (token starter; rounded down from ~0.6%). This is
  a **near-watch-only** directional allocation — appropriate when the flow is bullish but
  two quality gates fired and the debate disconfirmed.
- **Deviation reason:** none (deviated **down**, always allowed; an upward deviation is
  forbidden because gates fired).

## Option structures

### Directional (primary) — LONG, trigger-gated

- **Structure:** **$65/$72.5 call debit spread** (bull call spread).
- **Strike(s) / expiry:** Buy $65C / Sell $72.5C, **2026-06-18** (27 DTE).
- **Debit/credit:** ~**$2.90 debit** per spread.
- **Breakeven:** ~**$67.90**.
- **Max loss:** **$2.90** (the debit) — this is the sized risk.
- **Max profit:** ~$4.60 (width $7.50 − debit) at ≥$72.5.
- **Why this structure:** IV-rank is **100 / VRP FAIR** `[HIST:vrp]` and **net vanna is
  negative** `[STRUCT:vanna_charm]`, so a **naked call would bleed** as IV mean-reverts;
  the **spread caps the vol cost** and the short $72.5 leg funds it. Strikes anchor to the
  **$65 gamma wall (entry trigger)** and the **$70 bull magnet / $72.5** — both **inside
  the ±28% 27-DTE expected move** (range $46–82) so the target is not rich. **Enter only on
  a confirmed break and hold above $65** (below it, the long-gamma pin makes this a bleed).

### Defined-risk alternative — the fade / plan-B (SHORT), trigger-gated

- **Structure:** **$60/$52.5 put debit spread** (bear put spread).
- **Strike(s) / expiry:** Buy $60P / Sell $52.5P, **2026-06-18**.
- **Debit/credit:** ~**$2.40 debit**.
- **Breakeven:** ~**$57.60**.
- **Max loss:** **$2.40**.
- **Max profit:** ~$5.10 at ≤$52.5 (targets the **$53.15 DP shelf** `[DP:price_levels]`).
- **Why:** the contrarian/risk-monitor case — if **$60 breaks**, the spent squeeze unwinds
  into the air pocket below the floor; complacent skew `[STRUCT:term_skew]` makes puts
  relatively cheap. Symmetric, defined-risk, **trigger-gated on loss of $60.** *(No iron
  condor: the ±28% expected move would breach any condor wings inside $46–82.)*

## Macro overlay (cite phase-6)

- **Tailwinds:** idiosyncratic catalyst (IQ9S-3P launch + AI-data-center narrative)
  `[MACRO:ENPH_2026-05-14]`; **32.5% short interest = squeeze fuel above $65**
  `[SENT:short_interest]` (tactical, can't size up on it).
- **Headwinds:** **CPI +3.78% YoY / 10y 4.57%** → rate-sensitive solar headwind
  `[MACRO:DGS10]`; **regime TRANSITIONAL, breadth 38%** `[MACRO:MarketRegime_2026-05-22]`;
  **spot $64 above GS $57 target**; true solar peers (FSLR/BE) being sold `[CTX]`.
- **Net:** **net headwind** (idiosyncratic catalyst is the only offset; it is already in
  the price after a double).

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|------|-------|------------------|
| ~2026-06-10/11 | May CPI release | − / ? (sticky-inflation risk for solar/rates) |
| 2026-06-16/17 | **FOMC + dot plot** | − / ? (hawkish dots = solar headwind) |
| 2026-06-18 | Monthly OPEX | structural (70/85/95C wall + dealer hedge) |
| 2026-07-28 | ENPH earnings | outside window / outside any <60-DTE structure |

## Post-trade monitoring checklist

- [ ] **Daily:** is spot holding above $65 (long live) or losing $60 (flip to fade)? No
  position in the $60–65 pin zone.
- [ ] **Daily:** re-check dark-pool buy ratio (`dark_pool_block_stratified`) — accumulation
  → distribution flip is a hard invalidation `[DP]`.
- [ ] **On phase-4 refresh:** DEX/GEX — does the $65 wall persist, and does the squeeze coil
  (+$508M DEX) hold or unwind? `[STRUCT]`.
- [ ] **Each session:** does the sweep campaign stay call-led or flip put-dominant
  (`hot_chains_sweep_persistence`)? `[FLOW]`.
- [ ] **Around June 10-17:** trim/stand-aside into May CPI + FOMC dot plot; do not carry
  the directional debit through a hawkish surprise `[MACRO]`.
- [ ] **Watch IV:** if IV-rank stays pinned at 100 and the move stalls, the long debit
  bleeds via negative vanna — exit on time decay, don't hope `[STRUCT:vanna_charm]`.

## Citations summary

1. `[DP:block_stratified]` — dark-pool block tier **95.3% buy** ($27.2M) — phase-2-dark-pool.md §Tier breakdown
2. `[OI:biggest_increases]` — June **$70C OI +4,616** (ask 5,400 vs bid 275, opening longs) — phase-3-positioning.md §Largest OI increases
3. `[STRUCT:gex]`/`[STRUCT:dex]` — **$65 gamma wall 3.5M GEX**, **DEX +$508M** squeeze coil — phase-4-structure.md §GEX/§DEX
4. `[SENT:short_interest]` — **32.53% float short, 4.5× peers** (squeeze, largely spent) — phase-7c-sentiment.md §Short interest
5. `[FUND]` — **Q1'26 revenue −18% QoQ, GAAP loss** — phase-7b-fundamentals.md §Growth profile
6. `[HIST:signal_backtest]` — bullish_flow win-rate **1.00 (n=8, capped 0.75, unreliable)** — phase-5-historical.md §Sizing handoff
7. `[DEBATE]` — bear_residual **0.70** ≥ bull_residual **0.55** → disconfirmed — phase-8b-debate.md
