# Phase 9 — Trade Blueprint

**Ticker:** AAPL
**As-of date:** 2026-05-27
**PM voice:** desk PM running an institutional options-overlay book
**Spot reference:** 310.85 (phase-2 close / `fz`)
**Upstream phases cited:** phase-0.5 through phase-8b

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

AAPL's "bullish" tape is a busy-name mirage — net flow is only **+$17.4M** at a
0.53 call ask-fraction `[FLOW:insights_deep_dive]`, the marquee 7/2 310C printed
49.5/50.5 ask/bid (a spread, not a sweep), and the dark-pool buy skew is a
23-second closing-cross artifact `[DP:extended_hours]` — while dealers sit **long
gamma with a +$109M wall pinning spot at 310** `[STRUCT:gex]`. The stock is
**overbought (RSI 78.85) at its 52-week high after a +24% run** `[HIST:rsi fz]`
with **insiders selling (MSPR −100)** into a crowded-long, 0.95%-short-interest
tape, all inside a **TRANSITIONAL "reduce-size / iron-condors-in-range" regime**
`[MACRO:MarketRegime_2026-05-27]`. **This is not a directional long; it is a
range-to-fade-strength setup — harvest the 310 pin with defined risk, do not
chase.**

## Bias + conviction + horizon

- **Directional bias:** **RANGE** (unanimous 4/4 phase-8 desk; no LONG/SHORT vote)
- **Conviction (M-01 bin):** **0.55** (slight edge)
- **Time horizon:** **1-4w** (range-bound until the 7/30 earnings catalyst, which
  sits *outside* this window)
- **Why this bin:** bottom of the band — low confluence (conviction-matrix 17%,
  AAPL absent from bullish confluence top-50), two CAUTION gates, and the 8b debate
  disconfirmed (bear 0.85 ≥ bull 0.55) which down-shifts the bin by one. Matches
  phase-10's low confluence band.

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| Primary | ~310.85 (at pin) | Initiate the iron condor with spot within ±1% of the 310 gamma magnet (long-gamma pins it) | `[STRUCT:gex]` |
| Aggressive | 315–317.5 | Leg into the call side (short 317.5/322.5) on a tag of the 315 gamma wall that fails to break on vol_x >1.2 | `[STRUCT:gex]` |
| Fade (plan-B / counter) | 302–305 | If price pulls into the $304.99 DP support cluster and *holds*, the residual bullish flow + tech-sector inflow support a bounce-to-pin long — counter-trade | `[DP:price_levels]` |

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Support | **305** ($304.99 cluster, $3.02B); 2nd 302.25 | `[DP:price_levels]` |
| Resistance | **315** (gamma wall) → **320** (OI pin) | `[STRUCT:gex]` `[OI:pin_risk]` |
| Gamma flip (ZGL) | **~297** (below → dealers short gamma, downside accelerant) | `[STRUCT:today_gamma_flip]` |
| Largest pin / magnet | **310** (+$109M gamma wall = spot magnet) | `[STRUCT:gex]` |

**Price-context color (advisory):** entering at the **52-week high with RSI 78.85**
`[HIST:52w_proximity fz]` `[HIST:rsi fz]` — chase risk is acute. Prefer initiating
the range structure *at* the pin or fading a tag of 315; do not buy a breakout here.

## Invalidation

- **Price-based:** two daily closes **outside the 302–320 range** invalidates the
  range thesis (above 320 = breakout to re-underwrite; below 302 = heading for the
  ZGL). An **intraday break below ~297 (ZGL) with no reclaim** is a hard kill — it
  flips dealers short-gamma and turns this into a downside momentum tape.
- **Signal-based:** GEX regime flips **POSITIVE → NEGATIVE** on the phase-4 daily
  refresh (spot loses 297) `[STRUCT:gex]`; OR institutional-accumulation flips to
  **DISTRIBUTION** `[INSIGHT:institutional_accumulation]`. Either kills the
  pin-harvest premise.
- **Macro-based:** a **hawkish May-CPI print (~mid-June)** or **hawkish FOMC
  (~mid-June)** vs consensus `[MACRO:CPIAUCSL_2026-04]`, or a UW regime flip to
  **RISK-OFF** `[MACRO:MarketRegime_2026-05-27]` — any breaks the range with a
  gamma-unpinning gap.
- **Exit on invalidation:** **Roll/close** — close the threatened wing of the
  condor and keep the untested side; on a clean <297 break, close the whole
  structure (the range premise is dead).

## Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** p_raw = **0.857** (n=**7**, source=**backtest**,
  bullish_flow) → N-cap (n<10 → 0.75) → **capped p = 0.75** `[HIST:signal_backtest]`.
  *(Caveat: this win-rate is for the directional `bullish_flow` signal, which the
  desk is NOT primarily taking; it sizes the residual-long component only.)*
- **Kelly inputs:** b = **1.5** (target 320 / entry 311 / stop 305), fraction =
  0.25, cap_pct = 5.
- **Raw Kelly:** (0.75×1.5 − 0.25)/1.5 = **0.583** → suggested = min(0.583×0.25×100,
  5) = **5.0%** pre-gate. **Win-rate map ceiling:** p=0.75 ≥ 0.70 → full (≤5%).
- **Risk gates (each cuts; none adds):**
  - Fundamentals (phase-7b): **CAUTION** (rich valuation + insider MSPR −100) → cut
    one step (full → half, 5% → 2.5%).
  - Sentiment/crowd (phase-7c): **CAUTION**, crowd **CROWDED_LONG** → cut one step
    (half → starter, 2.5% → ~1.25%).
  - Correlation cluster (phase-6/8): **AAPL↔NVDA 0.736** (concurrent NVDA blueprint)
    → cut one step (~1.25% → ~0.6%).
  - Sector rotation (phase-6): **aligned** (Tech persistent inflow, persistence 1.0)
    → no cut (one-day directional wobble noted, not adverse).
  - Debate (phase-8b): **disconfirmed (bull 0.55 vs bear 0.85)** → down-shift bin by
    one (→ 0.55 floor) **and** cut one step (~0.6% → ~0.3%).
  - **Context (phase-0.5): BUSY_NAME_NORMAL_DAY** → no top-of-band sizing (enforced).
- **Final size:**
  - **Directional (residual long) component:** **~0.5%** of book risk — a token
    starter; **NOT the recommended trade** (bias is RANGE).
  - **Primary defined-risk (iron condor) allocation:** **~1.0%** of book max-loss —
    half-size-and-trimmed per the TRANSITIONAL regime + stacked gates. **Total name
    risk ≤ 1.0%.**
- **Deviation reason:** none (deviation is downward — always permitted; an upward
  deviation would be forbidden here because four gates fired).

## Option structures

### Directional (primary requirement — the fade-to-pin expression, small)

- **Structure:** **put debit spread** (fade the overbought tag back to the pin)
- **Strike(s) / expiry:** **312.5 / 305 put debit spread, 2026-06-12** (~16 DTE)
- **Debit/credit:** ~**$2.30** debit (illustrative, IV 6th %ile so cheap)
- **Breakeven:** ~**310.20**
- **Max loss:** ~**$2.30** (the debit) → sized to **~0.5%** of book
- **Why this structure:** expresses the desk's fade-strength lean (overbought RSI
  79 at 52W high, insiders selling) as a *defined-risk directional*, targeting the
  310 magnet / 305 DP support; 6/12 expiry harvests the move **before** the
  mid-June FOMC/CPI that could unpin the range. Cheap IV makes the long premium
  affordable. **Not** a high-conviction bet — a token starter.

### Defined-risk alternative (RECOMMENDED primary — pin harvest)

- **Structure:** **iron condor** (sell the 305–317.5 range around the 310 pin)
- **Strike(s) / expiry:** **short 305 put / long 300 put + short 317.5 call / long
  322.5 call, 2026-06-12** (~16 DTE)
- **Debit/credit:** ~**+$1.30** net credit (illustrative)
- **Breakeven:** ~**303.7** and ~**318.8**
- **Max loss:** $5 width − $1.30 credit = ~**$3.70** per condor → sized to **~1.0%**
  of book max-loss
- **Why this:** the long-gamma +$109M wall at 310 pins spot, the $302–305 DP support
  and 315–320 gamma walls bound the range, and the front expected move is only
  **±1.19% (±$3.69)** `[CTX:implied_move]` — well inside the 305–317.5 short strikes.
  This is the regime-sanctioned ("iron condors in range") trade. *Caveat: IV at the
  6th percentile means the credit is thin — this harvests the pin, not rich vol.*

**Expected-move check (N4):** front-expiry implied move ±1.19% / ±$3.69 → expected
near-term range ~307–315, comfortably inside both structures' short strikes. The
6/12 expiry deliberately **avoids** the 7/30 earnings binary and lands before the
mid-June macro cluster, so no single-catalyst gap of the expected-move magnitude
exceeds the defined max loss.

## Macro overlay (cite phase-6)

- **Tailwinds:**
  - **Technology sector persistent INFLOW** (persistence 1.0, $4.3B→$8.5B/5d)
    `[MACRO:sector_flow_persistence]`
  - SPY UPTREND +4.93% 30d, above 20/50 SMA `[MACRO:MarketRegime_2026-05-27]`
- **Headwinds:**
  - **TRANSITIONAL regime / weak breadth (37.1% bullish)** — "reduce size, defined-
    risk, range" `[MACRO:MarketRegime_2026-05-27]`
  - **CPI re-accelerating 3.78% YoY (+0.64% MoM)** + hawkish 8-4 Fed `[MACRO:CPIAUCSL_2026-04]`
  - 10y at 4.50% — mild duration drag on a 37.6x-PE name `[MACRO:DGS10_2026-05-26]`
- **Net:** **mixed** — the sector tailwind is real but the regime + inflation +
  breadth + the correlation cluster all argue size-down/range, not directional.

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|------|-------|------------------|
| ~2026-06-10 | May CPI release | ? (hot print = tech headwind, range-break risk) |
| ~2026-06-17 | FOMC (next meeting) | ? (hold likely; bias language = range-break risk) |
| 2026-07-30 | **AAPL Q3 earnings** | ? (**OUTSIDE this window/horizon** — structures expire 6/12, before it) |

## Post-trade monitoring checklist

- [ ] Re-check phase-4 **GEX regime daily** — if spot loses ~297 (ZGL), the
  long-gamma pin is gone; close the condor (range thesis dead).
- [ ] Watch phase-2 **dark-pool buy/sell daily** — a flip from the closing-cross
  buy skew to genuine intraday *distribution* confirms the bear/fade.
- [ ] Track **insider MSPR / any 8-K insider filings** — continued selling sustains
  the distribution-into-strength read.
- [ ] **Net the AAPL↔NVDA cluster** — if NVDA long is also on the book, treat the
  pair as one tech-beta line; cut the combined size, don't double it.
- [ ] Re-check **vol_x daily** — a close >315 on **vol_x >1.2** is the up-break
  signal that flips this from range to a real breakout (re-underwrite).

## Citations summary

1. `[FLOW:insights_deep_dive]` net flow **+$17.4M**, call ask-frac **0.53** —
   phase-1-flow.md §Whole-tape aggregate.
2. `[STRUCT:gex]` dealers **long gamma**, dominant wall **+$109M at 310**, ZGL ~297
   — phase-4-structure.md §GEX.
3. `[HIST:rsi fz]` **RSI 78.85**, −0.31% from 52W high, +24% window —
   phase-5-historical.md §Price context.
4. `[DP:extended_hours]` DP mega buy 0.867 is a **23-sec closing-cross artifact**,
   rank 14 — phase-2-dark-pool.md §Extended-hours.
5. `[MACRO:portfolio_correlation DUCKDB]` **AAPL↔NVDA 0.736** cluster —
   phase-6-macro.md §Cross-name correlation.
