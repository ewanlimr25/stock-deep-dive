# Phase A3 — Confluence: Direction, Reasons, Levels, Events — ENVX (2026-06-27)

Fuses the reused deep-dive layer (`research/ENVX/2026-06-26/`) with the A2 chart layer. Gap verdict = SUFFICIENT (94%, no size cut). Spot $5.95.

## Step 1 — directional vote tally
| Lane | Vote | Basis |
|------|------|-------|
| Flow (A1) | **bullish** (single shot) | $6-Oct call ask-sweep $871,964 / 84.2% ask — but one campaign, not persistent [FLOW:sweeps] |
| Dark pool (A2) | **NEUTRAL / weak-bull** | large buy_ratio 0.629 (< 0.70 green-light); overhead clusters $6.28/$7.05 are trapped longs from the −20% slide, not fresh demand [DP:price_levels] |
| Positioning (A3) | **bullish-ish** | $6-Oct build + $8 call-OI wall (the wall is also resistance) [OI] |
| Dealer (A4) | **NEUTRAL (pin)** | long-gamma 30/30 sessions, max-pain $6.00, gamma-flip $5.50 → suppresses direction [STRUCT:max_pain] |
| Historical (A5) | **bearish / no-edge** | bullish_flow backtest p=0.20 (n=5), avg −0.05%; 90d net-bearish premium −$2.0M [HIST] |
| Chart trend (B3) | **bearish** | spot below all SMAs, MACD bearish, descending highs [CHART:ma_stack] |
| Chart pattern (B4) | **bullish (unconfirmed)** | inverse H&S, neckline 7.40, target 9.41 — agrees with flow on the *upside tail* [CHART:head_shoulders] |
| Macro/sector (C1) | **bearish** | TRANSITIONAL/CHOPPY (breadth 38%), Industrials −$61.6M adverse, 10y 4.40%, beta 2.31 [MACRO] |

**Plurality = genuine 3-bull / 3-bear / 2-neutral split → RANGE.** The bullish votes are *tail/unconfirmed* (a lone sweep + an unconfirmed reversal pattern); the bearish votes are *trend + edge*. No directional plurality. Filters (cut-only): fundamentals **CONFIRM**, sentiment **CONFIRM** (squeeze fuel), debate **DISCONFIRMED** (bear 0.75 ≥ bull 0.55), rotation **adverse**.

## Step 2 — flow ↔ chart agreement: **DIVERGENT (→ RANGE)**
Bullish flow + the bullish (unconfirmed) inverse-H&S point **up**; trend + macro + the negative backtest point **down**. Per `direction-rubric.md`, DIVERGENT → **RANGE / defined-risk only, never a directional size** (ledger **L-0002**). The bullish tail has a **FLOW-LEADS** character — it is anticipatory and needs the **7.40 neckline break** to confirm (ledger **L-0001**); until then it is not a live long.

## Step 3 — conviction trail
1. Confluence band: score **51 → bin 0.55** (floor) [confluence-scoring].
2. Agreement modifier: **DIVERGENT → cap 0.55** (already at floor).
3. **Empirical edge is negative: raw_kelly = −0.143** (p=0.20, b=2.33) → Kelly says **take no directional risk** → directional size **0%**.
4. Risk gates: fundamentals CONFIRM (no cut), sentiment CONFIRM (no cut; squeeze fuel), **debate DISCONFIRMED** (directional long disconfirmed → 0%), rotation **adverse** (headwind).
5. Context: GENUINELY_UNUSUAL; **IV rank 42.5 / VRP −0.17 → PREMIUM_BUYING** — *buy* cheap vol (debits), don't sell. Front expected move only **±2.42% / ±$0.14** (the real move isn't priced).
6. Staleness: 1 day → no cut. Gap-audit: SUFFICIENT → no cut (C6 earnings-date is `important` but Oct expiry spans both candidates).

**→ bias RANGE · conviction 0.55 (DIVERGENT floor) · directional size 0% (negative edge + DISCONFIRMED) · horizon 1–4w for the range, with the squeeze tail extending to ~Aug-12.** The only sanctioned expression: **cheap, defined-risk debit optionality on BOTH tails** (long gamma of our own), exploiting the cheap VRP — explicitly **not** a directional bet. Mirrors the deep dive (RANGE, final_size_pct 0.0).

## Step 4 — reasons (two-sided, tagged, falsifiable)

### reasons_for (why RANGE + buy-cheap-two-way-optionality is the right posture)
1. **Long-gamma $6 pin** (GEX 30/30, July max-pain $6.00) mechanically pins price → range, not trend; the bull conceded this [STRUCT:max_pain].
2. **Cheap vol**: VRP −0.17 PREMIUM_BUYING + IV rank 42.5, and the front expected move is only ±2.42% [HIST:vrp][CTX:implied_move] — the eventual squeeze-or-breakdown is **not priced**, so optionality is underpriced.
3. **Real upside tail**: 26% SI / 49.12M sh / 7.45 DTC / HTB (~200K borrowable, declining short base) + the bullish $6-Oct campaign + an inverse-H&S target 9.41 → a single Aug-12 print can squeeze [SENT:short_float][FLOW:sweeps][CHART:head_shoulders].
4. **Real downside tail**: full downtrend below all SMAs + adverse rotation + winning shorts pressing absent a catalyst → a break of 5.39/5.50 runs to 4.84/4.61 [CHART:ma_stack][MACRO:sector_flow].
5. **Both tails dwarf the cost**: ATR 10.49% — when the range breaks it moves multiples of the cheap debit premium.

### reasons_against (steelman of "don't bother / it's a trap")
1. **[STRONGEST STEELMAN] The directional long is DISCONFIRMED and the edge is negative.** Backtest 20% (raw_kelly −0.143), 90d net-bearish premium −$2.0M, desk 0-for-4; the flow is **one lottery ticket, not a campaign** [HIST][DEBATE:residuals]. *Watchable flip:* next-day OI fails to confirm the $6-Oct build.
2. **Theta/pin trap**: the $6 pin + **no catalyst until ~Aug-12** means BOTH debit legs bleed theta for ~7 weeks while price pins $6 — the modal outcome is the range simply holds and both cheap options decay [STRUCT:max_pain].
3. **The inverse H&S is unconfirmed and at-risk** — price near the 5.39 invalidation, neckline 24% above; it may fail, not confirm (L-0001) [CHART:head_shoulders].
4. **DP is only a weak confirm** (buy_ratio 0.629 < 0.70) and the overhead is trapped-long supply, not fresh demand → thin fuel for the upside tail [DP:price_levels].
5. **Earnings-date uncertainty** (UW 07-30 vs IR-cadence ~Aug-12): if the squeeze trigger is mis-dated the call-debit's theta budget is wrong [FUND:C6].
6. **DIVERGENT flow↔chart-trend** — by rule (L-0002) not a directional trade [CHART][FLOW].

## Step 5 — level ladder (chart × dealer confluence)
| Role | Level | Sources |
|------|-------|---------|
| Bull-confirmation trigger / heavy resistance | **7.40–7.44** | inverse-H&S neckline [CHART:head_shoulders] + fib 0.382 7.42 [CHART:fib_0.382] + 5-touch 7.10 / 4-touch 7.23/7.44 [CHART:cluster]; sma200 7.72 above |
| Bull tail target | **9.41** | inverse-H&S measured target [CHART:head_shoulders]; ≈ swing high 9.15 [CHART:swing_high] |
| Near-term resistance lid | **6.15–6.35** | DP supply $6.28–6.33 [DP:price_levels] + fib 0.618 6.35 [CHART:fib_0.618] + S/R 6.15 [CHART:cluster] |
| Pin / magnet | **6.00** | July max-pain, long-gamma 30/30 [STRUCT:max_pain] |
| Spot | **5.95** | [CHART:spot] = DP value area [DP:price_levels] |
| **Decision-line support** | **5.39–5.59** | $5.50 gamma-flip/put-wall [STRUCT:today_gamma_flip] + fib 0.786 5.59 [CHART:fib_0.786] + S/R 5.57/5.67 [CHART:cluster] + **5.39 H&S invalidation/swing low** [CHART:swing_low] |
| Bear tail target | **4.84 / 4.61** | 52w low [CHART:low_52w] / fib swing-low (put-spread target) |
| Stops (ATR ref) | long 1.5-ATR **5.11**; short 1.5-ATR **6.79** | [CHART:stops] (ATR14 0.56) |

## Step 6 — event calendar (what moves this tape)
| Date | Event | Impact | Source |
|------|-------|--------|--------|
| 2026-07-17 | July monthly OPEX ($6 max-pain magnet) | **−** (pins, theta drag) | [STRUCT:max_pain] |
| ~2026-07-30 | FOMC (late-July cadence — confirm date) | ? | [MACRO:FOMC] |
| **~2026-08-12** | **ENVX Q2 earnings — THE squeeze trigger** (UW 07-30 likely stale; confirm) | ? (far exceeds ±2.42%) | [FUND:earnings] |

## Invalidation (carried to A4)
- **Price:** the range thesis breaks (into a *tail*, which the long-optionality holder wants) on two daily closes **below 5.50** (→ bear tail to 4.84/4.61) **or above 7.40 on rising IV** (→ bull tail/H&S confirm to 9.41). The thesis *fails* (no payoff) if price simply pins $5.90–6.10 into the structures' decay.
- **Signal:** next-day OI does **not** confirm the $6-Oct build (sweep was a one-off) [OI:biggest_increases], or conviction_matrix flips DIRECTIONAL_LONG → HEDGED_LONG [INSIGHT:conviction_matrix].
- **Macro:** SPY regime breaks further RISK-OFF (beta 2.31) [MACRO:MarketRegime], or hawkish late-July CPI/FOMC lifts the 10y.

## Ledger lessons applied
- **L-0002 (ACTIVE)** — DIVERGENT → RANGE, capped conviction 0.55, directional size 0, logged as reason_against #6. ✔
- **L-0001 (ACTIVE)** — the inverse H&S is unconfirmed; **no anticipatory sizing** — bull tail confirms only on a close above **7.40 on >1.2× volume** (two closes to hold). ✔
- **L-0004 (CANDIDATE, mirror-cautionary)** — a lone *bullish* sweep into a *long-gamma* $6 pin with no near catalyst is a **trap for the bull**; the pin caps the squeeze → size the bull tail as a **token lottery only**, not a position. ✔
- **L-0003** — n/a (deep dive fresh).

## Verdict for downstream (A4)
- `bias` **RANGE** · `conviction` **0.55** · `horizon` **1–4w** (squeeze tail to ~Aug-12) · directional size **0%**.
- Agreement label **DIVERGENT (FLOW-LEADS bull tail, unconfirmed)** → A4 = **cheap two-way defined-risk optionality**, trigger-based, token sizing only.
- Best-expression hierarchy for A4: (1) **call debit 6/8 Oct-16** = the squeeze-tail lottery (long the flow strike, capped by the $8 wall), held through ~Aug-12; (2) **put debit 5.5/4.5 Oct-16** = the downtrend-tail hedge below the gamma-flip; together a cheap long-strangle-via-spreads on a violent range break. Pure stock plan = **stand-aside / watch-only** (no directional edge; would only act on a confirmed 7.40 reclaim, starter, stop under 5.39).
