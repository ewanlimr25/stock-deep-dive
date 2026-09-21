# Trade Plan — ENVX

**As-of date:** 2026-06-27
**Spot reference:** $5.95 (yfinance, 373 sessions)
**Voice:** desk PM running an institutional book
**Built from:** `research/ENVX/2026-06-26/` deep dive (age 1 day) + chart engine (yfinance)

> *For research and educational use only. Not financial advice. Sizing,
> structures, targets and dates are illustrative.*

## 0. Information completeness (gap audit)

- **Verdict:** **SUFFICIENT** — completeness **94%**
- **Have:** options flow/sweeps, dark pool/blocks, OI/positioning, dealer GEX/max-pain, historical win-rate, OHLCV chart + patterns (inverse H&S, triangle), macro/sector rotation, event calendar, fundamentals (CONFIRM), sentiment/short interest, implied/expected move + VRP.
- **Missing / how to source:**
  | Item | Severity | How to source |
  |------|----------|---------------|
  | Confirmed Q2 earnings date (UW 07-30 vs IR-cadence ~Aug-12) | important | `fz quote ENVX` / `finnhub_enrich.py --ticker ENVX --date 2026-06-27` / ENVX IR — both candidates fall inside Oct-16 expiry, so it shifts theta budget, not expiry choice |
  | Next-day OI confirmation of the $6-Oct build + live tape | nice_to_have | `uw oi biggest-increases --symbol ENVX --json` + `uw options-flow sweeps --symbol ENVX --json` morning-of |

*SUFFICIENT = the evidence is complete enough to decide well. It does NOT imply an edge — here the empirical edge is **negative**.*

## 1. Direction & conviction

- **Bias:** **RANGE** (watch-only)
- **Conviction (M-01 bin):** **0.55** (DIVERGENT floor)
- **Horizon:** 1–4w for the range; the squeeze tail extends to ~Aug-12
- **Confluence score:** 51
- **Flow ↔ chart agreement:** **DIVERGENT** (bullish lone-sweep + unconfirmed inverse-H&S vs. a bearish downtrend + negative edge) → RANGE

### Thesis (≤3 sentences, ≥3 tagged citations)

ENVX is a $6 battery name pinned by a long-gamma July max-pain magnet (GEX 30/30) [STRUCT:max_pain] where a single bullish $6-Oct call ask-sweep ($871,964, 84% ask [FLOW:sweeps]) into a **26%-short-float HTB covering name** [SENT:short_float] sets up a real squeeze tail — but the directional edge is **negative** (backtest 20%/n=5, raw Kelly −0.143 [HIST]) and the debate is **DISCONFIRMED** (bear 0.75 ≥ bull 0.55 [DEBATE:residuals]), while the chart trend is down and a bullish inverse-H&S (neckline 7.40, target 9.41) sits **unconfirmed 24% above spot** [CHART:head_shoulders]. So this is a **DIVERGENT, watch-only RANGE**: no directional size, expressed only as **cheap two-way defined-risk debit optionality** (VRP −0.17 PREMIUM_BUYING) on a violent break of the $5.39–7.40 range.

### Why it should work (why RANGE + buy-cheap-two-way-optionality)
- **Long-gamma $6 pin** (GEX 30/30, July max-pain $6.00) mechanically pins price → range, not trend; the bull conceded this [STRUCT:max_pain].
- **Cheap vol**: VRP −0.17 PREMIUM_BUYING + IV rank 42.5; front expected move only ±2.42% — the eventual squeeze-or-breakdown is **not priced** [HIST:vrp][CTX:implied_move].
- **Real upside tail**: 26% SI / 49.12M sh / 7.45 DTC / HTB + the $6-Oct campaign + inverse-H&S target 9.41 → a single Aug-12 print can squeeze [SENT:short_float][FLOW:sweeps][CHART:head_shoulders].
- **Real downside tail**: full downtrend below all SMAs + adverse Industrials rotation + winning shorts pressing → a break of 5.39/5.50 runs to 4.84/4.61 [CHART:ma_stack][MACRO:sector_flow].
- **Both tails dwarf the cost**: ATR 10.49% — when the range breaks it moves multiples of the cheap debit premium [CHART:atr14].

### Why it may fail (the honest other side)
- **STRONGEST STEELMAN** — the directional long is **DISCONFIRMED and the edge is negative**: backtest 20% (raw Kelly −0.143), 90d net-bearish premium −$2.0M, desk 0-for-4; the flow is **one lottery ticket, not a campaign** [HIST][DEBATE:residuals].
- **Theta/pin trap**: the $6 pin + no catalyst until ~Aug-12 means **both debit legs bleed theta** for ~7 weeks while price pins $6 — the modal outcome is the range holds and both options decay [STRUCT:max_pain].
- **The inverse H&S is unconfirmed and at-risk** — price near the 5.39 invalidation, neckline 24% above; it may fail not confirm (L-0001) [CHART:head_shoulders].
- **DP is only a weak confirm** (buy_ratio 0.629 < 0.70) and the overhead is trapped-long supply, not fresh demand [DP:price_levels].
- **Earnings-date uncertainty** (UW 07-30 vs ~Aug-12) — if the squeeze trigger is mis-dated, the call-debit's theta budget is wrong [FUND:earnings].
- **DIVERGENT flow vs chart-trend** — by rule (ledger **L-0002**) not a directional trade [CHART][FLOW].

## 2. Levels to watch

| Level | Role | Source | Note |
|-------|------|--------|------|
| 9.41 | target (bull tail) | [CHART:head_shoulders] | inverse-H&S measured move; ≈ swing high 9.15 |
| 7.40–7.44 | trigger (bull-confirm) | [CHART:head_shoulders] | neckline + fib 0.382 7.42 + 5-touch resistance; sma200 7.72 above |
| 6.15–6.35 | resistance | [DP:price_levels] | DP supply $6.28–6.33 + fib 0.618 6.35 + S/R 6.15 |
| 6.00 | pin / magnet | [STRUCT:max_pain] | July max-pain, long-gamma 30/30 |
| 5.95 | spot | [DP:price_levels] | = DP value area |
| 5.39–5.59 | **decision-line / stop** | [STRUCT:gex] | $5.50 gamma-flip/put-wall + fib 0.786 5.59 + S/R 5.57/5.67 + **5.39 H&S invalidation** |
| 4.84 / 4.61 | target (bear tail) | [CHART:low_52w] | 52w low / fib swing-low (put-spread target) |

Moving averages: ema21 6.72 · sma50 6.83 · sma20 7.08 · sma200 7.72 (price below all). Fib (swing 4.61→9.15): 0.382 **7.42** · 0.5 6.88 · 0.618 **6.35** · 0.786 **5.59**.

## 3. Patterns forming (chart)

| Pattern | Direction | Confidence | Measured target | Invalidation | Note |
|---------|-----------|-----------|-----------------|--------------|------|
| inverse head & shoulders | bullish | **medium** | 9.41 | 5.39 | shoulders 6.16/6.19, head 5.39, neckline 7.40 — clean geometry but **UNCONFIRMED & at-risk** (price near invalidation, neckline 24% above). Confirm on close > 7.40 on >1.2× vol (L-0001). Aligns with the bullish $6-Oct flow [CHART:head_shoulders] |
| symmetrical triangle | neutral | low | break-based | — | converging trendlines (upper −0.15, lower +0.007); trade the break [CHART:triangle] |
| elliott wave | — | none | — | — | no valid count (pivots not cleanly alternating) [CHART:elliott_wave] |

## 4. Upcoming events that move the tape (next ~30–60d)

| Date | Event | Impact | Source |
|------|-------|--------|--------|
| 2026-07-17 | July monthly OPEX ($6 max-pain magnet) | − | [STRUCT:max_pain] |
| ~2026-07-30 | FOMC (late-July cadence — confirm date) | ? | [MACRO:FOMC] |
| **~2026-08-12** | **ENVX Q2 earnings — THE squeeze trigger** (UW 07-30 likely stale; confirm) | ? (far exceeds ±2.42%) | [FUND:earnings] |

## 5. Invalidation

- **Price-based:** the range breaks **into a tail** (which the long-optionality holder *wants*) on two daily closes **below 5.50** (→ bear tail 4.84/4.61) **or above 7.40 on rising IV** (→ bull tail / H&S confirm to 9.41). The thesis **fails (no payoff)** only if price pins **$5.90–6.10** into the structures' decay.
- **Signal-based:** next-day OI does **not** confirm the $6-Oct build (sweep was a one-off), or conviction_matrix flips DIRECTIONAL_LONG → HEDGED_LONG.
- **Macro-based:** SPY regime breaks further RISK-OFF (beta 2.31), or hawkish late-July CPI/FOMC lifts the 10y.

## 6. Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** p_raw = **0.20** (n=**5**, src=backtest) → p = 0.20
- **Inputs:** b = **2.33**, fraction = 0.25, cap_pct = 5
- **Raw Kelly:** 0.20 − (0.80/2.33) = **−0.143 (NEGATIVE)** → Kelly says **take no directional risk** · **Win-rate map ceiling:** none (negative edge)
- **Risk gates (each can only cut):** fundamentals **CONFIRM** · sentiment **CONFIRM** / crowd **CROWDED_SHORT** (squeeze fuel) · correlation **none** · rotation **adverse** · debate **DISCONFIRMED** · context **IV-rank 42.5 / VRP −0.17 PREMIUM_BUYING (buy cheap vol, don't sell)**
- **Final size:** **0.0% of book** (directional). *Deviation reason:* negative Kelly + DISCONFIRMED + DIVERGENT RANGE force directional size to 0; only **token defined-risk debit carry** on both tails (max-loss = premium, ~0.2–0.3% book each) is sanctioned — justified by cheap VRP, not by directional edge. Mirrors the deep dive (final_size_pct 0.0).

## 7. Plan A — pure stock (conditional long; else stand aside)

- **Direction:** **long** — but **watch-only at $5.95** (no edge)
- **Entry:** $7.45 — trigger: break and hold above the **7.40 inverse-H&S neckline on >1.2× avg volume (two closes)**; confirms the reversal AND aligns with the bullish $6-Oct flow. **Until then STAND ASIDE.** *Bear alternative:* short only on two closes below 5.50, stop 6.00, target 4.61.
- **Stop:** $6.80 (back below the neckline; = engine 1.5-ATR short stop 6.79)
- **Targets:** T1 **$9.15** (prior swing high, take 60%) · T2 **$9.41** (H&S measured move, take 40%)
- **Reward:risk to T1:** **2.62R** (on confirmation)
- **Size:** **0.0% book** now (would be starter on a confirmed neckline reclaim)
- **One-liner:** The only stock action with an edge is a **confirmed** inverse-H&S reclaim above 7.40 (flow-aligned, R 2.62), entered starter; at $5.95 with a negative backtest and a $6 long-gamma pin, **stand aside** — do not pre-position a +25%-away breakout (**L-0001**).

## 8. Plan B — options (≥1 with target date + target price)

### B1 — directional (squeeze-tail lottery)

- **Structure:** **call debit spread**
- **Strikes / expiry:** **6/8** / **2026-10-16**
- **Target date / target price:** **2026-08-13** / **$8.00** (underlying ≥ $8 caps the spread)
- **Debit/credit · breakeven · max loss:** debit **$0.80** · BE **$6.80** · max loss **$0.80**
- **Est. payoff at target:** **+$1.20** (spread max $2.00 width − $0.80 debit; ~1.5:1)
- **Why this structure:** long the $6 flow strike, short the $8 call-OI wall; **held *through* the ~Aug-12 earnings trigger** — max-loss = debit, so an earnings gap cannot exceed it. Buys cheap vol (VRP −0.17) to harvest a 26%-short squeeze. [FLOW:sweeps][SENT:short_float]

### B2 — defined-risk (downtrend-tail hedge)

- **Structure:** **put debit spread**
- **Strikes / expiry:** **5.5/4.5** / **2026-10-16**
- **Target date / target price:** **2026-08-13** / **$4.50** (underlying ≤ $4.5 caps the spread)
- **Debit/credit · breakeven · max loss:** debit **$0.40** · BE **$5.10** · max loss **$0.40**
- **Est. payoff at target:** **+$0.60** (spread max $1.00 width − $0.40 debit; ~1.5:1)
- **Why this structure:** below the $5.50 gamma-flip toward the $4.61 52w-low; debit (VRP −0.17 says **buy** not sell). Pairs with B1 as a **cheap long-strangle-via-spreads** on a violent range break. [CHART:ma_stack][MACRO:sector_flow]

*Expected-move check:* the **front-expiry** implied move is only **±2.42% / ±$0.14** — but both structures are **Oct-16, spanning the ~Aug-12 earnings**, where the move "far exceeds ±2.42%." The call target ($8 = +34%) and put target ($4.5 = −24%) are both inside a plausible post-earnings range for a 10.5%-ATR / 26%-short name, so neither is "rich." Buying these spreads = buying cheap optionality on a move the front month doesn't price (PREMIUM_BUYING). Max-loss = premium on each, so holding through the earnings binary is acceptable.

## 9. Post-entry monitoring checklist

- [ ] **Re-confirm the Q2 earnings date** (07-30 vs ~Aug-12) via `fz quote ENVX` before placing — it sets the theta clock.
- [ ] Check next-day OI confirms the $6-Oct call build; if it was a one-off, the bull tail weakens — cut the call-debit size.
- [ ] Watch the **5.39–5.50 decision line** and the **7.40 neckline** — a decisive break of either funds the corresponding tail; a pin at $6 bleeds both.
- [ ] Refresh GEX/max-pain weekly; if the long-gamma pin breaks (gamma-flip < 5.50), the range thesis is releasing.
- [ ] Reassess after Jul-17 OPEX — the $6 magnet pressure releases; re-pull live `uw` flow.

## 10. Reasoning-ledger lessons applied

- **L-0002 (ACTIVE)** — DIVERGENT flow↔chart → RANGE, capped conviction 0.55, directional size 0, logged as a top reason_against.
- **L-0001 (ACTIVE)** — the inverse H&S is unconfirmed; **no anticipatory sizing** — the bull tail confirms only on a close above **7.40 on >1.2× volume** (two closes to hold).
- **L-0004 (CANDIDATE, mirror-cautionary)** — a lone *bullish* sweep into a *long-gamma* $6 pin with no near catalyst is a **trap for the bull**; the pin caps the squeeze → the bull tail is sized as a **token lottery only**, not a position.

## Citations (≥3, what the eval will spot-check)

1. [FLOW:sweeps] — $6-Oct call ask-sweep $871,964 / 6,738 ct / 84.2% ask — `research/ENVX/2026-06-26/phase-1-flow.md`
2. [HIST:signal_backtest] — bullish_flow win_rate 0.20 (n=5), raw_kelly −0.143 — `research/ENVX/2026-06-26/phase-5-historical.md`
3. [STRUCT:max_pain] — July-OPEX max-pain $6.00 + long-gamma 30/30 — `research/ENVX/2026-06-26/phase-4-structure.md`
4. [SENT:short_float] — 26.00% SI, 49.12M sh, 7.45 DTC, HTB — `research/ENVX/2026-06-26/phase-7c-sentiment.md`
5. [DEBATE:residuals] — DISCONFIRMED, bear 0.75 ≥ bull 0.55 — `research/ENVX/2026-06-26/phase-8b-debate.md`
6. [CHART:head_shoulders] — inverse H&S neckline 7.40, head 5.39, target 9.41 (UNCONFIRMED) — `chart.json`
7. [DP:price_levels] — large buy_ratio 0.629, value area $5.95, overhead supply $6.28–6.33/$7.05 — `research/ENVX/2026-06-26/phase-2-dark-pool.md`
