# Phase 9 — Trade Blueprint

**Ticker:** CMPS
**As-of date:** 2026-05-22
**PM voice:** desk PM running an institutional options-overlay book
**Spot reference:** $11.81 (phase-5 close; DP vwap $11.98)
**Upstream phases cited:** phase-0.5 through phase-8b

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

CMPS is a **fundamentally de-risked psychedelics biotech** — two positive Phase 3 TRD
readouts, a White House EO, FDA priority voucher, NDA Q4, and runway to 2028
`[MACRO:CMPS_COMP006_2026-02-17]` — that institutions are still **accumulating** in the
dark pool (`buy_ratio 0.839`, buy/sell 5.22) `[DP:block_stratified]` while rolling their
calls **up-and-out** (far-call OI +3,820, Jul $12 bought) `[OI:position_rolls]`, with
options priced cheap (VRP −0.71, IV 75% vs realized 146%) `[HIST:vrp]`. But the move is
**already priced and crowded** — price at its 52-week high after +114%, analysts 18/2/0,
today's tape net-*selling* `[INSIGHT:price_vs_flow]`, and dealers **long-gamma-pinned at
$11–$12** `[STRUCT:gex]` — so the desk is unanimous RANGE near-term `[AGENT:*]`. The trade
is therefore **not a chase**: own a small, defined-risk, *cheap-optionality long into the
Q3 Part-B/NDA catalyst*, entered on a pullback to the $11 wall, not here.

## Bias + conviction + horizon

- **Directional bias:** **RANGE** (near-term), with a bullish lean expressed as
  defined-risk long-the-catalyst optionality. (Plurality of phase-8: 3 RANGE / 1 constrained-LONG / 0 bearish.)
- **Conviction (M-01 bin):** **0.65**
- **Time horizon:** **1-4w** to position; the payoff catalyst is **early Q3** (Part-B data).
- **Why this bin:** phase-10 confluence ≈ **65** (bottom of the 65–79 / 0.75 band), then the
  **phase-8b debate disconfirmation** (bear_residual 0.65 ≥ bull_residual 0.65) **down-shifts
  one bin → 0.65** `[DEBATE:]`. Moderate edge with real, unrefuted disconfirming evidence.

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| Primary | **$11.00–$11.45** | Pullback/retest of the $11 gamma wall + nearest DP shelf; buy weakness, don't chase the high | `[STRUCT:gex]` `[DP:price_levels]` |
| Aggressive | **$10.56–$10.86** | Deeper flush into the heaviest 5-day DP accumulation base (still above the $10 hedge/ZGL) | `[DP:price_levels]` |
| Fade (counter) | **$12.20** | Rejection at the DP supply / 52-week-high zone → fade back toward $11 if long isn't yet on | `[DP:largest]` `[FUND:52WeekHigh]` |

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Support | **$11.45** (then $10.56–$10.86 base) | `[DP:price_levels]` |
| Resistance | **$12.00–$12.24** (gamma wall + DP supply + 52w high) | `[STRUCT:gex]` `[DP:largest]` |
| Gamma flip (ZGL) | **$9.02** (regime flip → short-gamma trapdoor) | `[STRUCT:gex]` |
| Largest pin | **$11** gamma wall (+1.37M GEX = 84% of total; Jun $11 call OI 10,553) | `[STRUCT:gex]` `[OI:biggest_increases]` |

## Invalidation

- **Price-based:** **Two daily closes below $10.00** — breaks the $10.56–$11.45 DP base, the
  $10 put-hedge strike, and loses the $11 gamma wall → opens the trapdoor to ZGL $9.02. `[DP:price_levels]` `[STRUCT:gex]`
- **Signal-based:** GEX **flips NEGATIVE / spot closes below ZGL $9.02** `[STRUCT:gex]`, **OR**
  dark-pool **ACCUMULATION reverses to DISTRIBUTION** (institutional buy_ratio < 0.40)
  `[INSIGHT:institutional_accumulation]`, **OR** cumulative premium flow turns net-bearish 3
  consecutive sessions `[HIST:cumulative_premium_flow]`.
- **Macro-based:** A **negative COMP006 Part-B/durability signal or NDA setback** (the binary
  this name lives on) `[MACRO:catalyst_calendar]`, **OR** UW regime flips to RISK-OFF with
  breadth deteriorating below the current 38.1% `[MACRO:MarketRegime_2026-05-22]`.
- **Exit on invalidation:** **Hard stop** (close the structure) on the price or
  clinical/NDA-headline trigger — these are debit structures, max loss is pre-paid; do not
  average down on a binary miss. Absent a trigger, hold the defined-risk premium to the Q3 catalyst.

## Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** p_raw = **0.875** (phase-5 `bullish_flow` backtest, n=16,
  source=backtest) → N-cap (10≤n<20 → 0.85) → **capped p = 0.85** `[HIST:signal_backtest]`.
  - ⚠️ **Contamination caveat:** phase-5 flagged this win-rate is **market-wide and
    regime-contaminated** (semis-momentum tape), **not CMPS-specific** — the CMPS-specific
    `dark_pool_accumulation` backtest was **n=0**. The 0.85 is carried for mechanical fidelity,
    but the three gates below (which fire hard) are what set the real, conservative size.
- **Kelly inputs:** b = **2.3** (Aug $12/$16 call-debit-spread payoff = max_gain/max_loss),
  fraction = 0.25, cap_pct = 5.
- **Raw Kelly:** (0.85×2.3 − 0.15)/2.3 = **0.785** → suggested = min(0.785×0.25×100, 5) = **5.0%**
  (hits cap). · **Win-rate map ceiling:** p≥0.70 → full (≤5%).
- **Risk gates (each cuts; three fired):**
  - Fundamentals (phase-7b): **CONFIRM** → no-op (funded, current ratio 3.32, runway 2028).
  - **Sentiment/crowd (phase-7c): CAUTION + CROWDED_LONG** → **cut one step** (5% → 2.5%).
  - **Correlation cluster (phase-6): CMPS/RDDT 0.746 (≥0.70)** → **cut one step** (2.5% → 1.25%).
  - Sector rotation (phase-6): **neutral** (Healthcare inflow persistence 0.80, not adverse) → no-op.
  - **Debate (phase-8b): bull_residual 0.65 vs bear_residual 0.65 → DISCONFIRMED** → down-shift
    bin (done: 0.75→0.65) **+ cut one step** (1.25% → ~0.6%).
  - Context (phase-0.5): `GENUINELY_UNUSUAL` → no-op on size (edge already in p); broad regime
    TRANSITIONAL reinforces the small size.
- **Final size:** **≈0.6% of book risk** (three gates fired from a 5% ceiling), **defined-risk
  only.** Matches the risk-monitor's "quarter-size-or-less, debit-only" read `[AGENT:risk-monitor]`.
- **Deviation reason:** none (no upward deviation — forbidden here, three gates fired).

## Option structures

Both are **long premium** (debit) — deliberately, to harvest the cheap-vol/VRP edge
(`[HIST:vrp]`) rather than sell mispriced-low optionality, and both cap loss at the pre-paid
debit so a binary Q3 gap-down cannot exceed the stop. Expiry **Aug 21 (≈91 DTE)** straddles
the **early-Q3 Part-B** catalyst.

### Directional (primary)

- **Structure:** Long **Aug $12 call** (outright).
- **Strike(s) / expiry:** $12 / 2026-08-21 — the secondary gamma wall + the institutionally-
  accumulated Jul/Aug $12 strike `[STRUCT:gex]` `[OI:smart_positioning]`.
- **Debit/credit:** ~**$2.10 debit** (est. at IV ~108%, phase-4 Aug term).
- **Breakeven:** ~**$14.10**.
- **Max loss:** the **$2.10 debit** (pre-paid; ≤ final_size_pct of book).
- **Why this structure:** cleanest expression of *long cheap vol into the Q3 catalyst* — VRP
  −0.71 means realized (146%) dwarfs implied (75%), so owning the call is buying the move at a
  discount; uncapped to Street $14–$18 and the 8.9%/DTC-7.4 short squeeze `[SENT:short_interest]`,
  with max loss the premium if the pin holds / Part-B disappoints.

### Defined-risk alternative

- **Structure:** **Aug $12/$16 call debit spread** (the cheaper, capped-gain version).
- **Strike(s) / expiry:** buy $12 / sell $16, 2026-08-21 — long strike at the $12 wall, short
  strike at the Aug $16 OI build (+307, phase-3) and the top of the Street target range `[OI:biggest_increases]`.
- **Debit/credit:** ~**$1.20 debit** (width $4).
- **Breakeven:** ~**$13.20**.
- **Max loss:** the **$1.20 debit**.
- **Note:** caps gain at $16 (+35%, the rich end of the ±14% front-move ×~2.5; see Expected-move
  note) but halves the cost/theta — preferred if the move is expected to be gradual into Q3
  rather than a single gap.

**Expected-move check (N4):** front-expiry implied move **±13.95% / ±$1.65** `[CTX:implied_move]`.
The Aug structures intentionally target beyond the *front* move because their expiry sits
**after** the Q3 Part-B binary (which is priced larger, per the Nov-IV bump, phase-4); the $14
breakeven (≈+19%) is the realistic Street-median base case, the $16 cap (+35%) is the rich tail.
Both are **defined-risk**, so a single-catalyst gap of any magnitude cannot exceed the pre-paid
debit — satisfying the "gap ≤ stop" requirement for a catalyst-straddling expiry.

## Macro overlay (cite phase-6)

- **Tailwinds:**
  - Two positive Phase 3 TRD trials + WH EO + FDA priority voucher + NDA Q4 + runway 2028 `[MACRO:CMPS_2026]`.
  - Fed funds 3.62% (easing) + 10y 4.57% falling + 2s10s +0.43 un-inverted → mild support for long-duration biotech `[MACRO:DGS10_2026-05-21]` `[MACRO:T10Y2Y_2026-05-22]`.
  - Healthcare sector net flow +$494M, 5-day persistence 0.80 (inflow) `[MACRO:SectorFlowPersistence_5d]`.
- **Headwinds:**
  - Regime **TRANSITIONAL**, SPY breadth only 38.1% bullish → "half-size, defined-risk" `[MACRO:MarketRegime_2026-05-22]`.
  - **CMPS/RDDT correlation 0.746** — concurrent blueprints overlap as one beta-2.46 bet `[MACRO:corr_2026-05-22]`.
- **Net:** **mixed** — strong idiosyncratic (clinical) tailwind, fragile broad-market regime.

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|------|-------|------------------|
| Next 30d (to ~Jun 22) | No scheduled binary — catalyst-light (supports the pin / cheap Jun IV) | ? |
| Early Q3 2026 (~Jul–Aug) | **COMP006 26-wk Part-B durability data** (the next real binary) | ? (high-magnitude) |
| 2026-07-30 | Q2 earnings (cash/runway/NDA update) | ? |

## Post-trade monitoring checklist

- [ ] **Daily:** re-check dark-pool buy_ratio (phase-2) — a flip below 0.40 (distribution) is signal-invalidation.
- [ ] **Daily:** track spot vs the **$11 gamma wall** and **ZGL $9.02** (phase-4 daily GEX refresh) — a close below $10 is price-invalidation.
- [ ] **Weekly:** watch for the **COMP006 Part-B / NDA** headline (phase-6) — the structures are built to be held into it; size up only on a confirmed *positive* break >$12.20 on volume >2× (per the desk upside trigger).
- [ ] **Weekly:** re-run **CMPS/RDDT correlation** (phase-6) — if RDDT position is added/sized up, cut CMPS further (cluster).
- [ ] **On any move:** confirm cumulative premium flow hasn't turned net-bearish 3 sessions (phase-5), and that analyst revisions haven't started rolling over (phase-7c, the 0-sell base is the asymmetric risk).

## Citations summary

1. `[DP:block_stratified]` — dark-pool large-tier **buy_ratio 0.839** (buy/sell 5.22) — phase-2-dark-pool.md §Tier breakdown.
2. `[OI:position_rolls]` — call **roll-up-and-out, far-call OI +3,820** (Jul $12 bought, Jun $11 closed) — phase-3-positioning.md §Closing/roll.
3. `[HIST:vrp]` — **VRP −0.7132** (IV 75% vs realized 146%), premium-buying regime — phase-5-historical.md §IV regime.
4. `[MACRO:CMPS_COMP006_2026-02-17]` — two positive Phase 3 TRD trials + NDA Q4 + runway 2028 — phase-6-macro.md §Sector overlay.
5. `[INSIGHT:price_vs_flow]` — DIVERGENCE: price +114% vs net flow −$275.6k — phase-7-insights.md §Price vs flow.
6. `[DEBATE:]` — bull_residual 0.65 = bear_residual 0.65 → disconfirmed — phase-8b-debate.md §Verdict.
