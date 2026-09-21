# Phase 9 — Trade Blueprint

**Ticker:** PATH (UiPath Inc.)
**As-of date:** 2026-06-01
**PM voice:** desk PM running an institutional book
**Spot reference:** $13.11 (phase-4 GEX underlying_price; close $13.10)
**Upstream phases cited:** phase-0.5 through phase-8b

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

PATH gapped **+12% on a genuine Q1 earnings beat** into a dealer **long-gamma box** —
GEX +18.1M with a $13 pin and every near-expiry **max-pain at $11** [STRUCT:gex][STRUCT:max_pain]
— while the lit tape is two-sided (net only +$2.18M, the loudest single print a $2.31M
protective ATM put) [FLOW:unusual_volume] and the bullish-flow signal backtests
**edge-negative (44.4% win, −1.25% avg)** [HIST:signal_backtest]. Genuine dark-pool
accumulation (buy_ratio 0.634, **VWAP $12.89**) and a confirmed profitability inflection
[DP:block_stratified][FUND:operatingMarginTTM] underpin a floor, but the Street is cutting
targets to ≈spot and the bull/bear debate **disconfirmed the directional long (bull 0.55 <
bear 0.65)** [DEBATE]. Net: trade this as a **defined-risk, premium-selling RANGE ($12–$15,
pin $13) into the post-earnings IV crush — not a directional bet — at starter size**, with a
flip-long trigger only on a confirmed hold above $15.

## Bias + conviction + horizon

- **Directional bias:** **RANGE** (desk plurality: 2 RANGE / 2 NEUTRAL / 0 LONG / 0 SHORT)
- **Conviction (M-01 bin):** **0.55**
- **Time horizon:** **1-4w** (to the Jun-18 OPEX / FOMC node)
- **Why this bin:** phase-10 confluence ≈ **45** (band 30–49 → 0.55–0.65); the phase-8b
  disconfirmation (bear residual 0.65 ≥ bull 0.55) down-shifts one bin to **0.55**. The
  conviction is in the *range holding*, not a direction — any directional lean is
  explicitly disconfirmed.

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| Primary | ~$13.0–13.5 | Sell the condor near the **$13 gamma pin** as post-earnings IV crushes (theta + vega capture) | [STRUCT:gex] |
| Aggressive | $14.0 tag | Leg in the **call side into a squeeze spike** to the $14 first resistance (richer call premium) | [OI:oi_by_strike] |
| Fade (plan B) | >$15 hold | If price **breaks and holds >$15** (squeeze confirms), flip to the bullish call-debit tail; if it loses <$11.70, lean toward $11 max-pain | [OI:oi_by_strike] |

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Support | **$12.89** (DP VWAP), then $12.72 (block) / **$11.70** (deeper shelf) | [DP:price_levels][INSIGHT:institutional_accumulation] |
| Resistance | **$15.00** (call wall, 93k OI), $14 first | [OI:oi_by_strike] |
| Gamma flip (ZGL) | **$8.10** (far below — regime-flip / crash-only) | [STRUCT:gex] |
| Largest pin | **$11** (near-expiry max-pain, all of Jun-5/12/18); **$13** gamma magnet | [STRUCT:max_pain][STRUCT:gex] |

Price-context color (advisory): entering after a **+12% day with RSI 73.9, +21% above the
20-day SMA, pinned at the 200-day** [HIST:rsi fz][HIST:52w_proximity fz] — chase risk is
real; this is why the plan **sells premium into the move** rather than chasing it, and
prefers the aggressive (sell-into-strength) entry over a market entry.

## Invalidation

- **Price-based:** **Two daily closes >$15.00** (call wall breaks → squeeze confirmed; the
  range is wrong to the upside → close the call spread, flip to the bull tail) **OR two
  daily closes <$11.70** (loses the deep DP support shelf → max-pain $11 gravity takes over;
  range breaks down → close the put spread).
- **Signal-based:** **GEX regime flips NEGATIVE** on the phase-4 daily refresh (spot toward
  ZGL / vol-expansion regime — kills the mean-reversion premise) **OR** `insights
  institutional-accumulation` flips from ACCUMULATION to distribution (buy/sell ratio <1.0)
  [INSIGHT:institutional_accumulation] **OR** conviction-matrix flips DIRECTIONAL_LONG →
  HEDGED_LONG.
- **Macro-based:** **Hawkish/dovish FOMC surprise 2026-06-16/17** (dot plot) that gaps PATH
  beyond the ±6.32% expected move and breaches a short strike [MACRO:FOMC_2026-06-17]; or a
  UW `market-regime` flip TRANSITIONAL → RISK-OFF.

**Exit on invalidation:** credit structures → **roll or close** (not a hard stop): close the
breached spread at a 2× credit loss or on the second confirming daily close; leave the
untested side on to recoup.

## Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** p_raw = **0.444** (phase-5 `bullish_flow` win-rate, n=**9**,
  source=backtest) → N-cap (n<10 → 0.75) is non-binding → **capped p = 0.444**
  [HIST:signal_backtest].
- **Kelly inputs:** b = **1.67** (directional debit-spread payoff $1.25 gain / $0.75 risk),
  fraction = 0.25, cap_pct = 5.
- **Raw Kelly:** (0.444×1.67 − 0.556)/1.67 = **+0.111** (marginally positive *only* because
  b>1.5 offsets the sub-0.5 win-rate). **Win-rate map ceiling: p<0.50 → STARTER/SKIP**
  (SHORT-side floor: a sub-0.50 signal is not a directional position). Take the smaller →
  **starter**.
- **Risk gates (each cuts only):**
  - **Fundamentals (7b): CONFIRM** → no-op (quality supports; does not add).
  - **Sentiment/crowd (7c): CAUTION**, crowd_state CROWDED_SHORT → **cut one step**
    (adverse analyst-revision: targets cut to $13–15, $35M fund exit).
  - **Correlation (6/8): none** (PATH is the only blueprint for 2026-06-01) → no-op.
  - **Sector rotation (6): ALIGNED** (Tech #1 inflow, persistence 1) → no-op (no cut).
  - **Debate (8b): bull_residual 0.55 < bear_residual 0.65 → disconfirmed** → **down-shift
    bin (→0.55) + cut one step.**
  - **Context (0.5): GENUINELY_UNUSUAL** → no-op (edge already in p).
- **Final size:** **0.5% of book risk (starter)** — the multiple cuts (p<0.50 floor + 7c
  CAUTION + 8b disconfirm) drive an already-starter Kelly to the floor. The **directional
  debit spread is WATCH-ONLY/skip**; the only expression is the **defined-risk iron condor
  at 0.5%**.
- **Deviation reason:** none (upward deviation forbidden — multiple gates fired).

## Option structures

### Directional (primary) — *watch-only / squeeze-tail, NOT recommended at size*

- **Structure:** call debit spread (the bull's one durable point — the live upside tail)
- **Strike(s) / expiry:** **$13 / $15, 2026-07-17** (past FOMC + Jun-18 OPEX; 46 DTE)
- **Debit/credit:** ~**$0.75** debit (illustrative; IV ~79%)
- **Breakeven:** ~$13.75 · **Max gain:** ~$1.25 · **Max loss:** $0.75
- **Why this structure:** the 31% short float + Tech bid leave a real squeeze tail through
  the $15 wall [SENT:short_float][OI:oi_by_strike], but p=0.444 < 0.50 and the debate
  disconfirmed the long → **starter/skip only**; play it ONLY as the plan-B flip if price
  holds >$15. Do not initiate here against the edge-negative backtest.

### Defined-risk alternative — *RECOMMENDED, the actual expression*

- **Structure:** **iron condor** (sell the $12–$15 range into the IV crush)
- **Strike(s) / expiry:** **long $11 put / short $12 put + short $15 call / long $16 call,
  2026-06-18** (captures post-earnings IV crush + the OPEX/max-pain pin)
- **Debit/credit:** ~**$0.30 net credit** (illustrative; Jun-18 avg IV ~85%)
- **Breakeven:** ~**$11.70 / $15.30** · **Max loss:** ~**$0.70** (width $1.00 − credit $0.30)
- **Why this structure:** VRP **+0.139, PREMIUM_SELLING** [HIST:vrp] + long-gamma vol
  suppression + max-pain $11 + $15 call wall = a textbook sell-the-wings setup. Shorts ($12,
  $15) sit **beyond one expected move** (±6.32% = $12.28–$13.94) [CTX:implied_move_pct], so a
  single FOMC-day expected-move gap does not breach a short strike. Lower BE $11.70 = the
  deep DP support shelf. Size to **0.5% of book** (max-loss basis).

## Macro overlay (cite phase-6)

- **Tailwinds:** Technology **#1 net-inflow sector, persistence 1, accelerating**
  [MACRO:sector_flow_2026-06-01]; **Core CPI 2.74%** disinflating, supports the cutting cycle
  [MACRO:CPILFESL_2026-04]; **Fed funds 3.62%** (easing) [MACRO:DFF_2026-05-29].
- **Headwinds:** **10y 4.45%** pressures long-duration growth multiples [MACRO:DGS10_2026-05-29];
  **breadth 40% / regime TRANSITIONAL** → "half size, defined-risk, iron condors in range"
  [MACRO:MarketRegime_2026-06-01].
- **Net:** **mixed** — phase-6 graded the *name* a mild tailwind (sector bid), but for this
  *range* trade the narrow-breadth / half-size regime offsets it. The macro guidance itself
  prescribes the iron-condor structure chosen here.

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|------|-------|------------------|
| 2026-06-05 | Weekly OPEX (gamma pin $13) | ? |
| **2026-06-16/17** | **FOMC + dot plot/SEP** | ? |
| **2026-06-18** | **Monthly OPEX cliff** (max-pain $11, 110k OI) | ? |
| 2026-09-03 | Next earnings (Q2 FY27) — outside 30d window | ? |

Front-expiry **implied move ±6.32% / ≈$0.83** [CTX:implied_move_pct] — structures sized
beyond it. The FOMC-into-OPEX node (6/16–18) is the trade's primary risk window.

## Post-trade monitoring checklist

- [ ] **Daily: GEX regime + ZGL** (phase-4 refresh) — a flip to NEGATIVE kills the
  mean-reversion premise; close the condor.
- [ ] **Daily: dark-pool buy/sell ratio** (`insights institutional-accumulation`) — a flip
  below 1.0 = distribution starting; tighten the put side.
- [ ] **Each session: price vs $11.70 and $15** — the two range breaks (flip-long >$15,
  break-down <$11.70).
- [ ] **Into 6/16–18: IV / front-end term structure** — confirm the post-earnings crush is
  intact (the condor's edge); if front IV re-bids ahead of FOMC, consider closing early.
- [ ] **Analyst revisions** — a cluster of upgrades / target raises post-beat would revive
  the squeeze (re-weight toward the bull tail); more cuts confirm the fade.

## Citations summary

1. **[STRUCT:gex]** GEX +18.1M POSITIVE, ZGL $8.10, $13 pin — long-gamma mean-reversion
   box (phase-4-structure.md §GEX).
2. **[STRUCT:max_pain]** every near-expiry max-pain = **$11** (Jun-5/12/18) — downside
   gravity (phase-4-structure.md §Max pain).
3. **[HIST:signal_backtest]** `bullish_flow` win-rate **44.4%, n=9, avg −1.25%** — directional
   edge is negative (phase-5-historical.md §Signal backtest).
4. **[DP:block_stratified]** large-tier buy_ratio **0.634**, +4.6M sh accumulation, VWAP
   $12.89 (phase-2-dark-pool.md §Tier breakdown).
5. **[FUND:operatingMarginTTM]** first GAAP operating profit (op margin −22%→**+6%**), tier
   CONFIRM (phase-7b-fundamentals.md §Verdict).
6. **[MACRO:sector_flow_2026-06-01]** Technology **#1 inflow, persistence 1** (phase-6-macro.md
   §Sector rotation).
7. **[DEBATE]** bull_residual 0.55 < bear_residual 0.65 → disconfirmed (phase-8b-debate.md).
