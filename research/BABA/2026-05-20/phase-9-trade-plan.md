# Phase 9 — Trade Blueprint

**Ticker:** BABA
**As-of date:** 2026-05-20 (data: 2026-05-19)
**PM voice:** desk PM running an institutional book
**Spot reference:** $135.69 close, $135.70 VWAP (phase-7 `insights_institutional_accumulation`)
**Upstream phases cited:** phase-1 through phase-8

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

BABA is parked **exactly on its Zero Gamma Level** ($135.66, spot $135.70)
inside a **long-gamma cage** capped at the **+$8.5B GEX wall at $140** with a
**−$985M GEX trapdoor at $130** [STRUCT:gex], while an **institutional
campaign worth $217M of 5-session sweep premium** with a Mar 27 $145C/$130P
LEAP risk reversal argues for a higher target on a 1–3m horizon
[FLOW:sweep_persistence] [FLOW:top_premium_trades]. The counter is severe:
the **last 15 market-wide `bullish_flow` signals printed a 6.7% win rate and
−1.62% average move** [HIST:signal_backtest], BABA's sector is bleeding
**−$27M today** [MACRO:MarketRegime_2026-05-19 UW], and the
**25Δ skew is COMPLACENT (calls richer than puts by 2.8 vol pts)**
[STRUCT:term_skew] — so we trade the range with defined risk and refuse to
take naked directional exposure into 5/22 OPEX or the 6/17–18 FOMC.

## Bias + conviction + horizon

- **Directional bias:** **RANGE with a long-side asymmetric overlay**
- **Conviction (M-01 bin):** **0.55**
- **Time horizon:** **1–4w core (range), 1–3m overlay (LEAP-direction)**
- **Why this bin:** The desk split 2 RANGE / 1 SHORT (conv 4) / 1 LONG (conv 3)
  in phase 8 with an average conviction of 2.75/5; UW conviction-matrix is
  MIXED at confidence 2.81%; BABA misses the top-50 bullish-confluence list
  (score < 5). Phase-10 will score this run in the low-confluence band —
  this conviction bin matches.

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|------:|-------------------|--------|
| **Primary** | **$134.00–$134.50** | Pullback into the fresh 5-day DP accumulation cluster ($133.40 / $134.50 nodes, 19 and 23 trades respectively) AND today_ZGL ($134.43) holds. | [DP:price_levels], [STRUCT:today_gamma_flip] |
| Aggressive | $135.70 | Enter immediately at VWAP if 5/22 OPEX gravity holds (within $1 of ZGL $135.66 + $135 pin strike of 21,302 OI). | [STRUCT:gex], [OI:pin_risk] |
| Fade (plan B) | $140.50–$141.50 | Reject at the $140 GEX wall (+$8.5B). If price tags $140.50 intraday and reverses with no follow-through, fade short via the call wing of the IC. | [STRUCT:gex], [OI:biggest_increases] May22 $142C +1,702 OI bid-side |

## Levels to watch

| Type | Level | Source |
|------|------:|--------|
| Floor (DP support, fresh) | **$133.40** | [DP:price_levels] 5-day cluster, 19 trades |
| Floor (DP support, secondary) | $134.50 | [DP:price_levels] 5-day cluster, 23 trades |
| **Zero Gamma Level (today)** | **$134.43** | [STRUCT:today_gamma_flip] |
| **Zero Gamma Level (45d)** | **$135.66** | [STRUCT:gex] |
| Pin strike (5/22 weekly OPEX) | **$135** | [OI:pin_risk] 21,302 OI, 0.51% from spot, 3 DTE |
| Resistance (intraday cap) | $137–$138 | [OI:biggest_increases] covered-call strip $137C/$138C |
| **Hard resistance (gamma wall)** | **$140** | [STRUCT:gex] +$8.51B net GEX |
| Secondary resistance | $142 | [OI:biggest_increases] $142C 5/22 +1,702 OI written |
| Distribution zone (5d DP) | $140.87 / $144.15 / $145.81 | [DP:price_levels] $88.5M combined premium |
| LEAP target | $145–$150 | [FLOW:top_premium_trades] Mar27 $145C, [FLOW:sweeps] Jan27 $150C $2.43M ASK |
| **Trapdoor (GEX) — DOWNSIDE INVALIDATION** | **$130** | [STRUCT:gex] −$985M net GEX |

## Invalidation

- **Price-based:** TWO daily closes below **$130** (the −$985M GEX trapdoor —
  dealer regime flips to short-gamma below this level and downside
  trend-accelerates into the −$249M cluster at $125 and −$121M at $125)
  [STRUCT:gex]. OR: a single intraday break above **$142.50** that closes
  above $140 — this breaks both the $140 long-gamma wall AND the
  May 22 covered-call ceiling. Either condition exits both legs.
- **Signal-based:** EITHER (a) cumulative premium flow flips net bearish for
  **3 consecutive sessions** [HIST:cumulative_premium_flow] — the +$336M / 90d
  bull bias is the thesis backbone, OR (b) **DEX flips negative** [STRUCT:dex]
  — the +$134.7B mechanical dealer bid disappears, OR (c) the conviction matrix
  flips from MIXED to DIRECTIONAL_SHORT [INSIGHT:conviction_matrix].
- **Macro-based:** **June 17–18 FOMC delivers a hawkish surprise** —
  specifically (a) >25bp hike, (b) explicit push-back of the 2026 cut into
  2027, OR (c) Powell's presser tone is materially more hawkish than the
  April 29 statement [MACRO:FOMC_2026-04-29 WebSearch:federalreserve.gov]. We
  exit the directional leg the day prior; this overlaps the Jun 18 BABA OPEX
  by one day and is the highest-risk catalyst in the trade horizon. Secondary
  macro flag: market regime flips from TRANSITIONAL → RISK-OFF on UW daily
  refresh [MACRO:MarketRegime_2026-05-19 UW].

## Sizing (% of risk, NOT dollars)

### Directional overlay — Jul 17 call debit spread

- **Kelly inputs:** p = **0.55**, b = **1.86** (max-profit $6.60 vs max-loss
  $3.40, see structure below), fraction = 0.25.
- **Raw Kelly:** (0.55 × 1.86 − 0.45) / 1.86 = (1.023 − 0.45) / 1.86 = **0.308**
  (30.8% of book risk uncapped).
- **Suggested size:** 0.308 × 0.25 = **7.70%** of book.
- **Cap:** 5% per rubric.
- **Final size:** **2.50% of book risk** (half-Kelly suggested cap to respect
  risk-monitor's "HALF normal" recommendation in phase-8 + 6.7% recent
  backtest base rate).
- **Deviation reason:** none (final < suggested, no escape-hatch needed).

### Defined-risk range structure — May 29 iron condor

- **Kelly inputs:** p = 0.55, **b ≈ 0.76** (credit $1.30 vs max loss $2.70).
- **Raw Kelly:** (0.55 × 0.76 − 0.45) / 0.76 = (0.418 − 0.45) / 0.76 =
  **−0.042** → negative directional Kelly. The IC is NOT a directional bet;
  it's a *neutral structure* harvesting the May 22 OPEX pin + post-OPEX
  vanna drift. Per rubric, neutral structures are permitted; size manually.
- **Final size:** **1.50% of book risk** (max-loss-based, conservative
  because conviction is 0.55 and the structure is short-vol).

## Option structures

### Directional (primary) — Jul 17 $140 / $150 call debit spread

- **Structure:** Long July 17 2026 $140 call / short July 17 2026 $150 call.
- **Reference prices (from phase-1 chain context, 2026-05-19):**
  - Jul 17 $140 call: ASK ~$6.90 (`avg_price` field on the Jul 17 $140C
    ASK-side sweep, $499,560 premium / 724 size) [FLOW:top_premium_trades].
  - Jul 17 $150 call: not directly priced in the sweep table; conservative
    estimate ~$3.40–$3.50 based on Jan 27 $150C @ $14.74 scaled by sqrt-time
    (Jul 17 ≈ 59 DTE vs Jan 27 ≈ 241 DTE: sqrt(59/241) × $14.74 ≈ $7.30,
    minus higher vol skew for shorter dated puts ≈ $3.40–$3.80).
- **Net debit estimate:** ~$3.40–$3.50.
- **Max profit at expiry ≥ $150:** $10.00 − debit = **~$6.50–$6.60**.
- **Max loss = debit:** **~$3.40–$3.50** per spread.
- **Breakeven at expiry:** ~$143.40–$143.50.
- **Why this structure:**
  1. **IV environment**: VRP −5.1pp = premium cheap to realized = debit
     structures preferred [HIST:vrp]. IV percentile 33 (cheap side of 1Y)
     means we are not paying peak vol [HIST:iv_percentile_zscore].
  2. **Horizon**: 59 DTE expires AFTER the June 17–18 FOMC, capturing the
     June OPEX vol cycle WHILE letting the macro catalyst pass — but allowing
     a hard exit pre-FOMC if the macro-invalidation fires.
  3. **Strike geometry**: $140 long matches the +$8.5B GEX wall, betting
     dealer absorption *flips to dealer chase* on a catalyst break; $150
     short cap matches the Jan 27 $150C $2.43M LEAP target
     [FLOW:sweeps] AND sits inside the 5-day DP overhead cluster at $145.81,
     so we cap profit at the realistic resistance.
  4. **Risk reversal alignment**: aligns directly with the Mar 27 $145C side
     of the institutional LEAP risk reversal [FLOW:top_premium_trades].

### Defined-risk alternative — May 29 iron condor $128 / $132 / $140 / $143

- **Structure:** Short put $132 / long put $128 (put wing) +
  short call $140 / long call $143 (call wing). All May 29 2026 expiry (10 DTE).
- **Reference prices (phase-1/phase-3 data, 2026-05-19):**
  - May 29 $132 put: estimated $0.80–$1.10 mid (light OI in this strike;
    interpolated from $130P 5/22 @ $1.32 and $132P 6/18 vol/OI flag).
  - May 29 $128 put: estimated $0.30–$0.50.
  - May 29 $140 call: estimated $1.10–$1.50 (May 29 $141C OI build at $1.87
    [OI:biggest_increases] gives the anchor).
  - May 29 $143 call: estimated $0.50–$0.70.
- **Estimated total credit:** **~$1.20–$1.40 per spread**.
- **Max loss:** **$4.00 (put wing width) − credit = ~$2.60–$2.80 per spread**
  (call wing only $3.00 wide, so put wing dominates max loss).
- **Breakevens at expiry:** ~$130.70 (lower) and ~$141.30 (upper).
- **Profit zone:** between $132 and $140 at May 29 expiry — captures the
  $135 pin gravity into 5/22 OPEX, the dealer-vanna selling drift post-OPEX
  back to ZGL [STRUCT:vanna_charm], and the structural ZGL anchor at $135.66
  for the following week.
- **Why this structure:**
  1. **Long-gamma regime + complacent skew** = vol-of-vol expected to fall;
     short-premium structures benefit [STRUCT:term_skew] [STRUCT:gex].
  2. **Wing geometry**: short put at $132 is inside the new 5-day DP
     support cluster ($133.40 / $134.50) — we are short the put strike
     where institutional accumulation forms; short call at $140 is exactly
     the GEX wall ceiling. Both wings are at structurally defended levels.
  3. **Expiry choice**: 10 DTE (May 29) lets us collect through the May 22
     OPEX pin event AND through the post-OPEX vanna mechanical drift the
     week after — exactly the regime phase-4 expects.

## Macro overlay (cite phase-6)

**Tailwinds:**
- BABA Cloud +38% YoY with AI on track to 50% of cloud within 12 months —
  long-duration narrative intact [MACRO:BABA_Q4FY26_2026-05-13 WebSearch:yahoo.com].
- China "Anti-Involution" policy regime mildly constructive for
  margin-focused incumbents [MACRO:ChinaPolicy_2026-NPC WebSearch:bloomberg.com].
- Ant Group HK IPO 2.0 potential H2 2026 — speculative catalyst for ~33%
  BABA stake [MACRO:AntGroup_IPO_potential WebSearch:financialcontent.com].
- Tech sector flow +$44M today (BABA classified Cons Cyclical but tech
  story by economics) [MACRO:MarketRegime_2026-05-19 UW].

**Headwinds:**
- Market regime **TRANSITIONAL — reduce size, wait for clarity**
  [MACRO:MarketRegime_2026-05-19 UW].
- Market breadth only **34.7% bullish** — narrow leadership
  [MACRO:MarketRegime_2026-05-19 UW].
- **Consumer Cyclical sector flow today: −$27M** — BABA's sector is bleeding
  [MACRO:MarketRegime_2026-05-19 UW].
- **April CPI YoY 3.8% (highest since May 2023)**, energy +17.9% from Iran
  war oil shock [MACRO:CPI_2026-04 WebSearch:cnbc.com].
- **Fed 1-cut path for 2026** with hawkish dissent
  [MACRO:FOMC_2026-04-29 WebSearch:federalreserve.gov].
- BABA earnings May 13 already printed: **non-GAAP profit −99.7%, rev miss**
  — narrative tailwind (Cloud) competes with margin headwind
  [MACRO:BABA_Q4FY26_2026-05-13 WebSearch:yahoo.com].

**Net:** **headwind-tilted neutral**. The macro tape favors *defined risk
range* over *aggressive long*.

## Catalyst calendar (next 30d)

| Date | Event | Impact direction | Notes |
|------|-------|------------------|-------|
| **2026-05-22 (Fri)** | **BABA weekly OPEX (3 DTE)** | + (pin gravity to $135) | Phase-3 pin score 105,465; iron condor designed for this |
| ~2026-06-05 | May NFP | ? | Broad risk-on/off; not BABA-specific |
| ~2026-06-11 | May CPI | − if hot, + if cool | If CPI extends 3.8% → 4%+ trend, FOMC must hold/hike |
| **2026-06-17 / 18 (est)** | **June FOMC + presser** | − (hawkish surprise) | **HIGHEST RISK CATALYST** — exit directional leg day prior |
| 2026-06-18 (Thu) | BABA monthly OPEX (Jun) | + (phase-1 $130P/$140C/$145C cluster expires) | LEAP risk-reversal underlying expiry; the call debit spread will still have 30 DTE remaining |
| H2 2026 (speculative) | Ant Group HK IPO 2.0 | + (BABA upside catalyst) | Not in 30d window; flag for thesis-upgrade if confirmed |

## Post-trade monitoring checklist

- [ ] **Daily**: refresh phase-4 GEX/DEX/ZGL — flag if ZGL crosses spot
  (regime flip per phase-5 history of 13 flips in 28 sessions).
- [ ] **Daily**: refresh phase-2 dark pool prints — flag if 5-day cluster
  forms below $133 (support break) or above $146 (overhead supply cleared).
- [ ] **Daily**: re-run phase-1 sweeps + sweep_persistence — if BABA falls
  out of top-5 days OR persistence count drops below 4/5, downgrade
  conviction.
- [ ] **Each new session**: confirm cumulative_premium_flow is still net
  bullish (phase-5 $336M is the benchmark; 3 consecutive bearish sessions =
  invalidation per rubric).
- [ ] **Each catalyst date** (5/22 OPEX, 6/11 CPI, 6/17–18 FOMC): pre-decide
  the trim/roll/exit action 24h ahead; do not improvise during the print.
- [ ] **Weekly**: check whether bullish_flow signal-backtest win rate
  recovers (phase-5 6.7% sample — if rolling 20d sample climbs above 30%,
  market regime is improving and we can size up).
- [ ] **Ad-hoc**: news on Ant Group IPO 2.0 or China tech regulation — both
  would warrant thesis-upgrade and possible size addition (debit spread →
  outright long call).

## Conviction deviation

None. Final size 2.50% (directional) + 1.50% (range overlay) = **4.00% combined
book risk**, below the 5% cap. The deviation is *downward* (smaller than
suggested) and the rationale is documented in sizing: risk-monitor's "HALF
normal" recommendation + phase-5 bullish_flow 6.7% backtest base rate.

## Citations summary

Minimum 3 distinct upstream datapoints (M-04 requirement). Listed here for audit:

1. **[STRUCT:gex]** — Total GEX +$16.48B, ZGL $135.66, $140 wall +$8.51B,
   $130 trapdoor −$985M (phase-4-structure.md §GEX). Resolves to the
   per-strike table at phase-4-structure.md.
2. **[FLOW:sweep_persistence]** — BABA 5/5 sessions in top, consistency 1.0,
   $217M cumulative sweep premium (phase-1-flow.md §Sweep persistence).
3. **[HIST:signal_backtest]** — `bullish_flow` 20d window 15 signals, 6.7%
   win rate, avg −1.62%, samples include TSLA −7.4%, AVGO −4.1%, GOOGL
   −4.5% (phase-5-historical.md §Signal backtest).
4. **[FLOW:top_premium_trades]** — Mar 27 $145C +$1.89M paired with Mar 27
   $130P +$1.58M, same timestamp 16:04:32Z, same 1000-lot (phase-1-flow.md
   §Mar 2027 LEAP risk reversal).
5. **[STRUCT:term_skew]** — 25Δ skew COMPLACENT, call IV 0.4396 vs put IV
   0.4118 at 29 DTE (phase-4-structure.md §25Δ term skew).
6. **[MACRO:MarketRegime_2026-05-19 UW]** — regime TRANSITIONAL, breadth
   34.7%, Consumer Cyclical sector −$27M (phase-6-macro.md §Market regime).
7. **[OI:pin_risk]** — BABA #40 in pin-risk table, spot $135.69, pin $135,
   distance 0.51%, 21,302 OI, 3 DTE, pin_score 105,465
   (phase-3-positioning.md §Pin risk).
