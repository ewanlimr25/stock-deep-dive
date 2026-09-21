# Trade Plan — FSLR

**As-of date:** 2026-06-21
**Spot reference:** $257.70 (yfinance close; $257.13 on the 2026-06-18 options parquet)
**Voice:** desk PM running an institutional options-overlay book
**Built from:** `research/FSLR/2026-05-18/` deep dive (STALE, ~23 trading days) + **live 2026-06-18 GEX/DEX/IV/max-pain refresh** + chart engine (yfinance, 371 sessions)

> *For research and educational use only. Not financial advice. Sizing,
> structures, targets and dates are illustrative.*

## 0. Information completeness (gap audit)

- **Verdict:** **USABLE_WITH_GAPS** — completeness ~65%
- **Have:** dealer structure (GEX/DEX/ZGL, **fresh 6/18**), OI/positioning (max-pain, P/C OI, **fresh**), implied move/IV term (**fresh**), OHLCV+patterns, fundamentals (no veto), event calendar; reused (stale) flow campaign, dark pool, historical backtest, macro.
- **Missing / how to source:**
  | Item | Severity | How to source |
  |------|----------|---------------|
  | Section 232 resolution (binary, imminent) | important | WebSearch / regulations.gov / pv-tech.org daily through end-June |
  | Today's live sweep tape | important | `uw options-flow sweeps --symbol FSLR`; `uw insights deep-dive --symbol FSLR` |
  | Macro regime refresh | important | `uw risk market-regime` |
  | Dark-pool / backtest / short-interest refresh | nice_to_have | `uw dark-pool block-stratified`; `uw historical signal-backtest`; `fz quote FSLR` |

## 1. Direction & conviction

- **Bias:** **LONG (low conviction) — tactically RANGE**
- **Conviction (M-01 bin):** **0.55** (bottom bin)
- **Horizon:** **1–4 weeks** (carry through the Section 232 window; out before ~7/30 earnings)
- **Confluence score:** ~58/100 (the new chart layer drags the stale 67/100 down)
- **Flow↔chart agreement:** **FLOW-LEADS** (bullish positioning, chart unconfirmed) → anticipatory, trigger entry, starter size.

### Thesis (≤3 sentences)

FSLR's dealer book is still mechanically supportive — POSITIVE GEX regime, ZGL
**$70.31** far below spot, DEX **+$666M** (dealers BUY), and the **$250 gamma magnet
(+$4.33M)** sits exactly on a chart confluence floor (swing low $248.66 + fib 0.500
$251.97) [STRUCT:gex + CHART:fib_0.5] — while bullish positioning is intact 23 days
on (max-pain pins **$260**, P/C OI 5→19 call-heavy) ahead of the still-**pending,
binary Section 232 polysilicon decision** that disproportionately benefits FSLR
[OI:max_pain + MACRO:Sec232]. But the easy money is already made — the name **blew
off +73% to $320.95 then dumped 22%** and now trades **below its 9/21 EMAs with
bearish MACD** in a `range_or_transition`, so the chart has *not* confirmed the flow
[CHART:swing_high/macd]; with the market-wide `bullish_flow` edge a poor **26.3%**
[HIST:signal_backtest] and front-end IV at **82.7%**, this is a **starter-size,
defined-risk lean off the floor — harvest the vol, don't pay it**, not a conviction
chase.

### Why it should work

- **Dealer structure supports the floor (fresh 6/18):** POSITIVE GEX, ZGL $70.31, DEX +$666M; the **$250 magnet (+$4.33M)** is the largest cluster and sits on the chart floor [STRUCT:gex/dex + CHART:fib_0.5]. *Falsifiable:* GEX flips NEGATIVE / ZGL crosses up through ~$200.
- **Bullish positioning is intact, not unwound:** max-pain $260 across 7/02–7/31, P/C OI 5.06→19.1, the two-tenor $280C build still standing [OI:max_pain + FLOW]. *Falsifiable:* P/C OI < 1 / call OI bleeds.
- **Live idiosyncratic binary:** Section 232 decision "by end of month"; FSLR (CdTe, non-poly) near-pure beneficiary; 82.7% front IV prices a real event [MACRO:Sec232 + STRUCT:iv_term]. *Falsifiable:* "no tariff" headline.
- **Primary trend still up:** spot > sma50 $236.68 > sma200 $233.30 (+79% off 52w low) [CHART:sma200].

### Why it may fail (the honest other side)

- **★ Post-parabolic exhaustion + FLOW↔CHART divergence (steelman):** +73% to $320.95 then −22%; now below ema9/21/sma20, MACD bearish, `range_or_transition`. The chart hasn't confirmed the bullish flow and the deep-dive LONG *already captured* the catalyst move — buying here is buying a stalled, extended name on stale flow (L-0002) [CHART:trend/macd]. *Trigger:* rejection at $260/$266 or 2 closes < $248.
- **Crowded long + a fresh credible bear:** P/C OI to 19, sell-side PTs chased to $300–330, and **Bernstein initiated Underperform 6/16** right here [SENT WebSearch:marketbeat] — crowded + extended = violent-unwind risk. *Falsifiable:* heavy-volume break of $248.
- **Binary + brutal vega:** front IV 82.7% → long premium overpays and gets vol-crushed on resolution even if direction is right; "no tariff" removes the asymmetry → same-day exit [STRUCT:iv_term + MACRO].
- **Poor calibrated edge + regime headwind:** bullish_flow 26.3% win / −1.26% avg-20d; macro TRANSITIONAL [HIST + MACRO] → size tiny.

## 2. Levels to watch

| Level | Role | Source | Note |
|-------|------|--------|------|
| **$320.95** | extension | [CHART:swing_high] | parabolic 52w high; fib 1.272 $358.48 beyond |
| **$278–$288** | resistance | [CHART:sma20] + [STRUCT:gex] | ceiling band: sma20 278.12 + Jun-12 high 279.18 + S/R 280.41 + $280 gamma + fib 0.236 288.39 |
| **$265–$268** | trigger | [CHART:ema9] | reclaim line — close >$266 on >1.2× vol = momentum-long confirm; fib 0.382 268.25 |
| **$260** | pin | [STRUCT:max_pain] + [CHART:cluster] | $260 gamma +$3.38M + max-pain pin |
| **$257.70** | spot | — | sits on the $257.5 neg-gamma chop strike (−$1.04M) |
| **$248–$252** | support | [STRUCT:gex] + [CHART:fib_0.5] | **★ make-or-break floor:** $250 gamma +$4.33M + swing low 248.66 + fib 0.5 251.97 + S/R 248.24/251.62 + 7/10 max-pain 250 |
| **$241** | stop | [CHART:stops] | 1-ATR 241.36 + S/R 241.86; 2 closes < $248 = exit |
| **$234–$236** | support | [CHART:fib_0.618] + [STRUCT:gex] | deep shelf: fib 0.618 235.69 + sma50 236.68 + S/R 234.07 + old $230 put wall |
| **$70.31** | gamma flip | [STRUCT:gex] | ZGL — disaster floor / regime flip |

Moving averages: sma50 $236.68 · sma200 $233.30 · ema21 $265.25. Fib (swing $182.99→$320.95): 0.382 $268.25 · 0.5 $251.97 · 0.618 $235.69.

## 3. Patterns forming (chart)

| Pattern | Direction | Confidence | Measured target | Invalidation | Note |
|---------|-----------|-----------|-----------------|--------------|------|
| flag / H&S / double / triangle / cup | — | **none** | — | — | **all `detected:false`** — no classical pattern; post-blow-off range not yet resolved |
| Elliott working count | bearish | **none** (1/3 rules) | $259.96 | $279.18 | impulse-down wave-5 pending; **NOT tradeable**; weakly hints downside exhaustion at the $250–$260 floor; *yields* to the flow/structure long lean |

## 4. Upcoming events that move the tape (next ~30–60d)

| Date | Event | Impact | Source |
|------|-------|--------|--------|
| ~2026-06-26 | Weekly expiry carrying **82.7% event IV** — implied catalyst timing | ? | [STRUCT:iv_term] |
| ~2026-06-30 | **Section 232 polysilicon decision** window edge (binary, asymmetric +) | + | [MACRO:Sec232 WebSearch:pv-tech.org] |
| 2026-07-04 | FEOC deadline for 10% bonus ITC (FSLR FEOC-clean) | + | [MACRO:FEOC] |
| 2026-07-17 | July monthly OPEX | ? | third Friday |
| ~2026-07-30 | FSLR Q2-2026 earnings (corroborated by 7/31 IV bump 76.9%) — **exit before** | ? | [FUND + STRUCT:iv_term] |

## 5. Invalidation

- **Price-based:** **2 consecutive daily closes < $248** — breaks the gamma magnet + swing low + fib 0.5 floor; opens $234/$230 (trend damage) [CHART:support + STRUCT:gex].
- **Signal-based:** GEX flips **NEGATIVE** or ZGL crosses up through **~$200**; OR dark-pool accumulation → distribution; OR P/C OI collapses **< 1** [STRUCT:gex + OI:max_pain].
- **Macro-based:** Section 232 "**no tariff / no action**" → **exit same-day** (asymmetry gone); OR regime → RISK-OFF [MACRO:Sec232].

## 6. Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** p_raw = **0.263** (phase-5 `bullish_flow` win-rate, n=19, src=backtest); N-cap (10≤n<20 → 0.85) non-binding → **p = 0.263**.
- **Inputs:** b = **3.11** (entry $250 → objective $278, stop $241), fraction = 0.25, cap_pct = 5.
- **Raw Kelly:** **+2.61%** (barely positive — the trade survives *only* on 3:1 asymmetry, not on hit-rate). Fractional → **0.65% ceiling**.
- **Win-rate map:** p < 0.50 → **STARTER / skip ceiling** (SHORT-side floor binds — never half/full at this win-rate).
- **Risk gates (each can only cut):** fundamentals **CONFIRM** (no-op) · sentiment/crowd **CAUTION** (crowded, Bernstein UP) · correlation **CUT** (Tech+solar+Sec232 triple-stack) · rotation **CUT** (TRANSITIONAL) · debate **CUT** (divergence unrefuted) · context **CUT** (stale + USABLE_WITH_GAPS).
- **Final size:** **0.5% of book risk** (directional starter). Defined-risk vol-harvest leg (Plan B2) carries an additional ~1.0%; **combined deployment ≤ ~1.5%**, far under the 5% cap. No deviation reason (sizing *below* ceiling).

## 7. Plan A — pure stock (long)

- **Direction:** **long** (starter)
- **Entry:** **$248–$252** floor (use $250) — trigger: buy a **tag that holds** (closes back > $250); **do NOT chase**. Add only on a **close > $266 on >1.2× avg volume** (EMA reclaim, L-0001).
- **Stop:** **$241** (below 1-ATR $241.36 / S/R $241.86; equivalently 2 closes < $248).
- **Targets:** T1 **$260** (gamma pin/max-pain, take **50%**) · T2 **$278** (ceiling band / measured retest, take 50%, trail the rest toward $321).
- **Reward:risk to T1:** **1.11R** (to T2: ~3.1R).
- **Size:** **0.5% book** (starter; poor empirical edge + every gate cutting).
- **One-liner:** Small long off the $250 dealer-magnet floor with a $241 stop; scale only on a $266 reclaim — asymmetry, not conviction.

## 8. Plan B — options (≥1 with target date + target price)

> IV is **very elevated** (front 82.7%) — structures are chosen to **mitigate/harvest vega**, not pay it. Front-expiry implied move ≈ **±$30 (±11.6%) for 6/26**, ±$51 for 7/17.

### B1 — directional (upside-break expression)

- **Structure:** **call debit spread** (vega-mitigated by the short leg)
- **Strikes / expiry:** **Long $260C / Short $280C** / **2026-07-17** (26 DTE; after the Sec 232 window, before ~7/30 earnings → no crush)
- **Target date / target price:** **2026-07-10** / **$278** (ceiling band on a Sec 232 bullish resolution)
- **Debit · breakeven · max loss:** ~**$7.00** · **$267.00** · **$7.00** (width $20, max profit $13)
- **Est. payoff at target:** ~**$10** (interim, ~7 DTE left at $278)
- **Why:** brackets the $260 pin → $280 magnet; the short $280 leg cuts ~40% of the premium and caps vega at the old LEAP target. Size **0.5% book**. *If Sec 232 prints "no tariff," close same day.*

### B2 — defined-risk (core: vol-harvest + bullish-floor)

- **Structure:** **put credit spread** (bull put — sells the elevated event vol, leans on the dealer floor)
- **Strikes / expiry:** **Short $245P / Long $235P** / **2026-07-17** (26 DTE)
- **Target date / target price:** **2026-07-17** / **$250** (objective = FSLR holds ≥ $245 → full credit)
- **Credit · breakeven · max loss:** ~**$4.30** · **$240.70** · **$5.70** (width $10, max profit $4.30)
- **Why:** strikes sit **below** the $248–$252 make-or-break floor and the $245 neg-gamma; breakeven $240.70 aligns with the $241 stop / sma50. Harvests the 82.7% IV with defined risk; positive theta. Size **1.0% book**. **Binary gap risk:** a Sec 232 "no tariff" gap toward $235 ≈ max loss — close on the headline. *Neutral variant:* add a $280/$290 call credit spread to form an iron condor if you read this as pure range.

## 9. Post-entry monitoring checklist

- [ ] Daily: re-check GEX regime + ZGL — exit-half if regime flips NEGATIVE or ZGL crosses up through ~$200 [STRUCT:gex].
- [ ] Daily: scan for any Section 232 / FEOC headline (regulations.gov, BIS, Commerce, pv-tech.org) — "no tariff" = same-day exit [MACRO:Sec232].
- [ ] Re-check P/C OI + max-pain — thesis weakens if P/C OI < 1 or max-pain rolls below $250 [OI:max_pain].
- [ ] After T1 ($260): trail the stock stop to breakeven ($250).
- [ ] Watch the $266 reclaim (>1.2× vol) for the scale-in trigger; watch $248 (2 closes) for invalidation.
- [ ] **Refresh the flow** — the reused narrative is ~23 trading days stale; run `/stock-deep-dive FSLR` before sizing above starter [L-0003].

## 10. Reasoning-ledger lessons applied

- **L-0003** (stale flow decays): reused dive ~23 td old → conviction cut, flow = context, refresh recommended before full size.
- **L-0001** (don't size a break at full until it holds): anticipatory starter only; scale requires a **>$266 reclaim close on >1.2× vol**.
- **L-0002** (divergent → defined-risk/temper): the FLOW↔CHART divergence is the **top reason_against**; expression is starter + defined-risk, never full directional.

## Citations (≥3, what the eval will spot-check)

1. **[STRUCT:gex]** $250 net_gex **+$4,331,683** (largest magnet); ZGL **$70.31**; regime POSITIVE — live 2026-06-18 (`_live/gex.json`).
2. **[OI:max_pain]** max-pain pins **$260** (7/02/7/17/7/31); P/C OI **5.06→19.1** call-heavy — live 2026-06-18 (`_live/maxpain.json`).
3. **[CHART:swing_high]** parabolic blow-off **$320.95 on 2026-06-03** then −22% to **$248.66** (2026-06-10) — `chart.json`.
4. **[HIST:signal_backtest]** `bullish_flow` win-rate **26.3%** / −1.26% avg-20d, n=19 — `research/FSLR/2026-05-18/phase-5-historical.md`.
5. **[STRUCT:iv_term]** front-end IV **82.7%** (6/26) decaying to ~66% LEAPs — binary event premium — live 2026-06-18 (`_live/ivterm.json`).
6. **[MACRO:Sec232]** Section 232 polysilicon decision pending "by end of month"; FSLR CdTe near-pure beneficiary — WebSearch:pv-tech.org.

---
*Run `/trade-plan-eval FSLR 2026-06-21` after taking the trade so the reasoning ledger learns from the outcome.*
