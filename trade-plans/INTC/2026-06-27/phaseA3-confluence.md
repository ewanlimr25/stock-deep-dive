# Phase A3 — Confluence: Direction, Reasons, Levels, Events — INTC (2026-06-27)

Fuses the reused deep-dive flow/positioning/structure/macro/fundamentals layer (`research/INTC/2026-06-26/`) with the A2 chart layer. Gap verdict = SUFFICIENT (no size cut from data). Spot $128.32.

## Step 1 — directional vote tally
| Lane | Vote | Basis |
|------|------|-------|
| Flow (A1) | **SHORT** (qualified) | 5/5 bearish sweep campaign $925.2M, net flow −$50.9M [FLOW:sweep_persistence] — *but* conviction-matrix = COVERED_CALL (may be hedging, see reason_against #1) |
| Dark pool (A2) | **NEUTRAL** | 51.9% buy / 48.1% sell — "neither confirms nor refutes"; MEGA 1.0 is rebalance flow. Structural: overhead supply $140.94, pin shelf $128.32 [DP:price_levels] |
| Positioning (A3) | **SHORT** (qualified) | ~73% bearish new OI; Jul-17 $130 put +11,442 (ratio 4.11) [OI:biggest_increases] — could be protective puts on longs |
| Dealer (A4) | **NEUTRAL (pin)** | Long-gamma pins +5.34M@120 / +4.16M@130; ZGL 27.26 far below → dealers buy dips/sell rips, muffles direction [STRUCT:gex] |
| Historical (A5) | **SHORT** | Firing-class backtest p=0.667, n=9, payoff 1.77 [HIST] |
| Chart trend (B3) | **LONG** | Full bullish MA stack, +120% over sma200, uptrend unbroken [CHART:ma_stack] |
| Chart pattern (B4) | **NEUTRAL** | No pattern detected; broadening range low-conf only [CHART:patterns] |
| Macro/sector (C1) | **SHORT** | Hawkish Fed, Tech #1 outflow −$637.8M, $1.3T semis selloff [MACRO:sector_rotation] |

**Plurality = SHORT** (4 short / 1 long / 3 neutral). Filters (cut-only): fundamentals **VETO** [FUND], sentiment **CAUTION / CROWDED_LONG** [SENT], debate **DISCONFIRMED** (bull 0.65 = bear 0.65) [phase-8b].

## Step 2 — flow ↔ chart agreement: **DIVERGENT**
Flow / positioning / macro point **down**; the chart trend points **up** and is unbroken. Per `direction-rubric.md` Step 2, a DIVERGENT read → **NEUTRAL/RANGE by default, or a defined-risk fade only — never a full directional size.** This is the core constraint of the plan and the top reason_against. (Ledger **L-0002**.)

## Step 3 — conviction trail
1. Confluence band: score **55 → bin 0.65** [confluence-scoring].
2. Agreement modifier: **DIVERGENT → cap 0.55**.
3. Risk gates: fundamentals **VETO → directional size 0%**; sentiment CAUTION + debate DISCONFIRMED → reinforce watch-only; rotation *aligned* (supports short, no cut); CROWDED_LONG (cuts conviction in chasing the long, supports the fade thesis but adds two-way squeeze risk).
4. Phase-0.5 context: GENUINELY_UNUSUAL, **IV rank 94.1 → PREMIUM_SELLING / VRP +5.95**; no top-of-band; option *buying* is vega-taxed.
5. Staleness: deep dive 1 day old → **no cut**.
6. Gap-audit: SUFFICIENT → **no cut**.

**→ bias SHORT · conviction 0.55 (DIVERGENT floor) · directional size 0% (VETO) · horizon 1–4w, hard-capped to expire before Jul-23.** The only sanctioned expression is a **small, defined-risk fade of strength toward the $120 pin** (or selling the upside VRP) — not a naked directional short. This matches the deep dive (conviction 0.55, final_size_pct 0.0).

## Step 4 — reasons (two-sided, tagged, falsifiable)

### reasons_for (the short / downside fade)
1. **Price-vs-flow bearish DIVERGENCE** — +10.7% price / −$50.9M net flow over 30d [INSIGHT:price_vs_flow].
2. **5/5-session bearish sweep campaign**, $925.2M, consistency 1.0 [FLOW:sweep_persistence].
3. **~73% bearish new OI**, Jul-17 $130 put +11,442 (ratio 4.11) — heaviest near-term build is a put [OI:biggest_increases].
4. **Extreme overvaluation** — +247.75% YTD, only loss-maker in peer group, 29–33% above the $102.70 analyst target [FUND:peer_pe].
5. **Macro tailwind (gated)** — hawkish Fed, Technology #1 directional outflow −$637.8M, $1.3T June semis selloff [MACRO:sector_rotation].
6. **Chart exhaustion at the top** — new 52w high (141.45) on **0.73× volume** + neutral RSI 56.78; overhead DP supply $140.94 [CHART:vol_vs_avg][DP:price_levels].

### reasons_against (steelman of the long / no-trade)
1. **[STRONGEST STEELMAN] The "bearish flow" is likely hedging/financing, not directional shorting.** Conviction-matrix reads **COVERED_CALL** + deep-ITM delta-one — longs are holding & protecting, not selling. If true, the entire bear premise is a misread of the tape and the fade is −EV at size [INSIGHT:conviction_matrix]. *Watchable flip:* matrix → DIRECTIONAL_LONG, or net-bullish premium 3 sessions.
2. **Fundamentals VETO / squeeze risk** — 4/4 EPS beats, +45.76% fwd EPS, insiders buying, Pelosi $6M buy, AI headlines; a 5th beat Jul-23 squeezes the crowded long [FUND:earnings_surprise]. *Watchable:* any pre-earnings upgrade/AI catalyst.
3. **Chart trend is bullish and unbroken** — shorting a +247% uptrend with a full MA stack and no reversal signal [CHART:ma_stack]. *Watchable trigger (→ invalidation):* two daily closes above 133, then 141.45.
4. **Long-gamma pin muffles the downside** — dealers buy dips/sell rips around $120/$130; a bought put spread bleeds theta at 94% IV [STRUCT:gex].
5. **No short fuel** — SI only 3.39%; the down-move must come from longs voluntarily selling, not short-covering → slow grind, not a cascade [SENT].
6. **DIVERGENT flow↔chart** — by rule (L-0002) this is range/fade-only, never a directional size [CHART][INSIGHT:price_vs_flow].

## Step 5 — level ladder (chart × dealer confluence)
| Role | Level | Sources |
|------|-------|---------|
| Hard ceiling / bear invalidation | **141.45** | [CHART:high_52w] + DP supply $140.94 [DP:price_levels] |
| Resistance / fade-the-strength trigger | **132.75–133** | [CHART:swing_high] + DP supply band $132–133 [DP:price_levels]; $130 call-wall/gamma lid just beneath [OI] |
| Call wall / gamma lid | **130** | [OI:oi_by_strike] + gamma pin +4.16M [STRUCT:gex] |
| Spot / pin shelf | **128.32** | [CHART:spot] + DP shelf [DP:price_levels]; $128 neg-gamma notch [STRUCT:gex] |
| Largest pin / magnet | **125** | [OI] / max-pain region |
| **Key support shelf (downside target)** | **117–122** | fib 0.236 117.26 [CHART:fib_0.236] + sma20 119.42 [CHART:sma20] + ema21 122.09 [CHART:ema21] + **$120 gamma pin / max-pain** +5.34M [STRUCT:gex][OI] |
| Deeper support | **108.39 → 102** | sma50 [CHART:sma50]; fib 0.382 102.29 ≈ swing low 102.40 [CHART:fib_0.382][CHART:swing_low] |
| Capitulation support | **98.33** | swing low 2026-06-05 [CHART:swing_low] |
| Gamma flip (ZGL) | **27.26** | [STRUCT:gex] — far below; confirms dealers long-gamma (context, not a tradeable level) |
| Stops (ATR ref) | short 1.5-ATR **143.28**; long 1.5-ATR **113.36** | [CHART:stops] (ATR14 9.97) |

## Step 6 — event calendar (what moves this tape)
| Date | Event | Impact | Source |
|------|-------|--------|--------|
| 2026-07-15 | June CPI release | **?** (dovish → squeeze risk; hawkish → supports short) | [MACRO:CPIAUCSL] |
| 2026-07-17 | Monthly OPEX (all structures expire here) | **−** (gamma roll-off; pin pressure releases after) | [OI:opex] |
| **2026-07-23** | **INTC Q2 earnings AMC** | **? PRIMARY BINARY — DO NOT HOLD THROUGH** (beat squeezes, miss confirms) | [FUND:earnings_surprise] |
| 2026-07-29 | FOMC | ? (after structures expire) | [MACRO:FOMC] |

## Invalidation (carried to A4)
- **Price:** two daily closes above **133** (clears $130 call wall + $132–133 DP supply); hard kill above **141.45**.
- **Signal:** conviction-matrix flips COVERED_CALL → DIRECTIONAL_LONG, **OR** net-bullish premium flow 3 consecutive sessions, **OR** the 5/5 bearish sweep persistence breaks [INSIGHT:conviction_matrix][HIST].
- **Macro / hard rule:** dovish June-CPI surprise OR semis flips to net inflow; **AND holding any position through Jul-23 earnings is itself invalidation** [FUND:earnings_surprise].

## Ledger lessons applied
- **L-0002 (ACTIVE)** — DIVERGENT capped conviction at 0.55, forced fade-only / defined-risk framing, logged as top reason_against #6. ✔
- **L-0004 (CANDIDATE, partial)** — respected the VETO + the bear's strongest unrefuted point (hedging-not-shorting); **no bearish premium carried into the undated bullish catalyst** — every structure expires before Jul-23. ✔ (Structure is long-gamma here, not short-gamma, so the squeeze-on-reclaim mechanic is replaced by pin-muffle; noted.)
- **L-0001 / L-0003** — not applicable (no pattern detected; deep dive fresh).

## Verdict for downstream (A4)
- `bias` **SHORT** · `conviction` **0.55** · `horizon` **1–4w (must close before Jul-23)** · directional size **0%**.
- Agreement label **DIVERGENT** → A4 entry style = **fade-of-strength / defined-risk only**, trigger-based, starter sizing at most.
- Best-expression hierarchy for A4: (1) **sell the upside VRP** (bear call credit, aligns with PREMIUM_SELLING + long-gamma pin) as the highest-probability; (2) a **small bear put debit toward the $120 pin** as the directional dart (theta-aware, capped). Pure stock plan = **watch-only short**, starter only on a confirmed rejection at 132–133, hard stop above 141.45.
