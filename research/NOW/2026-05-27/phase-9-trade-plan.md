# Phase 9 — Trade Blueprint

**Ticker:** NOW
**As-of date:** 2026-05-27
**PM voice:** desk PM running an institutional options-overlay book
**Spot reference:** $102.12 (phase-2 close / fz quote)
**Upstream phases cited:** phase-0.5 through phase-8b

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

NOW is a high-quality SaaS compounder (gross margin 76.6%, +21.7% revenue growth,
forward PEG ≈1.0, Street strong-buy with a $140.63 target) `[FUND:metric]` that has
been de-rated 51% off its high and is now coiled in a short-gamma squeeze geometry —
spot $102.75 below ZGL $104.62 with dealers net-short calls forced to buy on
strength `[STRUCT:gex]`, and a 3.4:1 bullish call tape (net delta-notional +$0.36bn)
`[FLOW:delta_notional DUCKDB]`. But the spring has **no fuse**: the desk debate was
disconfirmed `[DEBATE]`, the dark pool shows **no accumulation** `[DP:block_stratified]`,
and Technology is the day's largest net-directional outflow (−$433.5M, persistence
1.0) `[MACRO:sector_rotation]` — so this is a small, **trigger-contingent** long on a
$103.30 break toward the $110 gamma wall, not a conviction position here.

## Bias + conviction + horizon

- **Directional bias:** **LONG (trigger-contingent)**
- **Conviction (M-01 bin):** **0.55**
- **Time horizon:** **1–4w** (catalyst/break-contingent; the underlying mean-reversion case extends 1–3m)
- **Why this bin:** phase-10 confluence ≈ **53** (band 50–64 → 0.65), **down-shifted one bin to 0.55** by the phase-8b debate-disconfirmation gate (bull_residual 0.65 = bear_residual 0.65). See `## Conviction note`.

## Conviction note

Confluence ≈53 maps to 0.65, but the phase-8b debate was **disconfirmed**
(bear_residual 0.65 ≥ bull_residual 0.65), and the sizing rubric mandates a
one-bin down-shift on disconfirmation → **0.55**. This is not a discretionary
deviation; it is the gate firing. 0.55 ("slight edge — coin-flip plus a sliver")
honestly captures a real-but-untriggered setup the desk would only pre-position
small.

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| **Primary** | $103.50 | Break + hold of the **$103.30 DP supply** on a volume expansion (the missing catalyst), targeting the $104.62 ZGL flip | `[DP:price_levels]` `[STRUCT:gex]` |
| **Aggressive** | $100.75–$101.00 | Pullback into the **$101.0–$101.7 DP support shelf** that holds (buy the V-bottom retest, tighter stop) | `[DP:price_levels]` |
| **Fade** | $109.50–$110.00 | Rejection at the **$110 gamma wall (+7.4M)** — take profit / counter-trade the squeeze exhaustion | `[STRUCT:gex]` `[OI:biggest_increases]` |

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Support (shelf) | $101.0–$101.7 | `[DP:price_levels]` |
| Support (major) | **$99.69** | `[DP:price_levels]` |
| Resistance (near) | **$103.30** ($138M supply) | `[DP:price_levels]` |
| Gamma flip (ZGL) | **$104.62** | `[STRUCT:gex]` |
| Upside target / wall | **$110** (+7.4M GEX, OI cluster) | `[STRUCT:gex]` `[OI:biggest_increases]` |
| Near-term OI magnet | $106 (106C 6/05 +5,436) | `[OI:biggest_increases]` |

**Price-context color (advisory):** RSI 57 — neutral, not overbought, room to run
`[HIST:rsi fz]`; but NOW is **−51.7% from its 52-week high and below its 200-day
SMA** `[HIST:52w_proximity fz]` — this is a counter-trend bounce, not a breakout, so
prefer the **trigger-contingent primary** or the **aggressive dip** over chasing.

## Invalidation

- **Price-based (hard stop):** two daily closes **below $99.69** (loses the major DP
  support shelf + the 2026-05-13 V-bottom structure) `[DP:price_levels]` `[HIST:trend]`.
- **Signal-based:** the bullish tape reverses — net call premium falls below put
  premium (flow sign flips) for **2+ consecutive sessions**, OR cumulative premium
  flow turns net-bearish 3 sessions `[HIST:cumulative_premium_flow]`, OR IV bleeds
  with no catalyst and vanna-driven dealer selling accelerates (the phase-4 negative-
  vanna trap fires) `[STRUCT:vanna_charm]`.
- **Macro-based:** hawkish **June FOMC (~6/16)** surprise, OR the Technology net
  outflow accelerates / SPY regime flips RISK-OFF `[MACRO:sector_rotation]` `[MACRO:MarketRegime]`.

## Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** p_raw = **0.857** (n=**7**, source=backtest) → N-cap (n<10 ⇒ 0.75) → **capped p = 0.75** `[HIST:signal_backtest]`.
- **Kelly inputs:** b = **1.625** (target $110 / entry $103.50 / stop $99.50), fraction = 0.25, cap_pct = 5.
- **Raw Kelly:** (0.75×1.625 − 0.25)/1.625 = **0.596** → ×0.25×100 = 14.9%, **capped at 5.0%**. Win-rate map (p=0.75 ≥0.70): **full** (≤ cap_pct). Pre-gate ceiling = **5.0%**.
- **Risk gates (each cuts only):**
  - Fundamentals (7b): **CONFIRM** → no-op.
  - Sentiment/crowd (7c): **CONFIRM / BALANCED** → no-op.
  - Correlation cluster (6/8): **none** (NOW neg-correlated to AAPL/NVDA/BABA → diversifier) → no-op (no credit; gates can't add).
  - **Sector rotation (6): ADVERSE** (Tech −$433.5M, persistence 1.0) → **−½ size step**.
  - **Debate (8b): DISCONFIRMED** (bull 0.65 / bear 0.65) → **−1 size step + bin down-shift**.
- **Context modifier (0.5):** `GENUINELY_UNUSUAL (directional only)` → no-op on p, **but vol_confirmed=NO** → do not size at top of band (already deeply cut).
- **Step math:** full 5.0% → (debate −1 step) 2.5% → (sector −½ step) **≈1.9%**.
- **Final size:** **1.9% of book risk** (well below the 5% cap; defined-risk max-loss basis).
- **Deviation reason:** none (no upward deviation; forbidden anyway — two gates fired).

## Option structures

### Directional (primary) — 105/110 call debit spread

- **Structure:** long 105C / short 110C (call debit spread)
- **Strike(s) / expiry:** **105 / 110, exp 2026-07-17** (51 DTE — captures June FOMC + CPI and the bounce window; **expires BEFORE the 7/22 earnings binary**, so no earnings IV crush)
- **Debit/credit:** ≈ **$2.00 debit** (illustrative; IV ~56%)
- **Breakeven:** ≈ **$107.00**
- **Max loss:** **$2.00** (the debit) — size so total debit ≤ 1.9% of book risk
- **Why this structure:** VRP −0.165 says options are **cheap vs realized → buy premium (debit)**, not sell it `[HIST:vrp]`; the spread is **anchored to the $110 gamma wall** `[STRUCT:gex]` which caps natural upside and cheapens the structure vs an outright call. Target $110 (+7.7%) is ~1.45× the 51-DTE expected move (≈±5.3%, scaled from the front ±4.07% `[CTX:implied_move]`) — at the rich edge, so **take 50% at the $106 OI magnet** (within ~1× expected move) and let the rest run to $110.

### Defined-risk alternative — 100/95 put credit spread

- **Structure:** short 100P / long 95P (put credit spread — sells the V-bottom floor)
- **Strike(s) / expiry:** **100 / 95, exp 2026-07-17**
- **Debit/credit:** ≈ **$1.70 credit** (illustrative)
- **Breakeven:** ≈ **$98.30**
- **Max loss:** **$3.30** (width $5 − credit $1.70) — size so max-loss ≤ 1.9% of book risk
- **Note:** expresses "NOW holds the $99.69–$100 floor" — the better structure if you
  believe the **RANGE** (contrarian-scanner) over the break. Sells the exact shelf
  that is the price-invalidation, so the trade and the stop coincide. Caveat: selling
  premium runs *against* the premium-buying VRP — use only as the range/hold-the-floor
  expression, not the primary.

## Macro overlay (cite phase-6)

- **Tailwinds:** Fed funds **3.62%, easing cycle** — supports de-rated growth duration `[MACRO:DFF_2026-05-26 FRED]`; 2s10s **+0.48 normalized** (no recession signal) `[MACRO:T10Y2Y_2026-05-27 FRED]`; SPY uptrend near highs `[MACRO:MarketRegime_2026-05-27 UW]`; NOW a **diversifier** (neg-correlated to AAPL/NVDA/BABA) `[MACRO:correlation DUCKDB]`.
- **Headwinds:** **Technology net outflow −$433.5M, persistence 1.0** `[MACRO:sector_rotation UW]`; regime **TRANSITIONAL** "reduce size, defined-risk", 37% breadth `[MACRO:MarketRegime UW]`; **sticky core CPI +0.38% MoM** caps the easing pace `[MACRO:CPILFESL_2026-04 FRED]`.
- **Net:** **mixed → mild headwind** (sector rotation + regime offset the rate tailwind; the diversification credit is the bright spot).

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|------|-------|------------------|
| ~2026-06-10 | May CPI release | ? (hot core = headwind, rates up) |
| ~2026-06-16/17 | **June FOMC** | ? (dovish = tailwind; the key macro binary) |
| 2026-06-18 | Monthly OPEX | gamma/pin mechanics |
| 2026-07-22 | NOW earnings | **outside window** (51 DTE) — structures expire 7/17, before it |

## Post-trade monitoring checklist

- [ ] **Daily: does the bullish flow sign hold?** Net call premium > put premium; watch for the risk-monitor's "Tech rotation drags NOW's flow negative" — the trade's core tension (`[FLOW]` vs `[MACRO]`).
- [ ] **Daily: GEX/ZGL refresh** — has spot reclaimed $104.62 (squeeze armed, add) or is ZGL drifting up away from spot? `[STRUCT:gex]`
- [ ] **Daily: dark pool** — does laddered *buying* finally appear below market (accumulation confirms), or stay a $102.12 pin? `[DP:price_levels]`
- [ ] **IV watch:** is IV bleeding with no catalyst (the negative-vanna trap)? If IV rank rolls off below ~50 with price flat, the debit thesis is decaying — cut. `[STRUCT:vanna_charm]` `[HIST:iv_percentile_zscore]`
- [ ] **Time stop:** if no $103.30 break with volume by ~6/12 (post-CPI) and still range-bound, close the debit spread (the 6/05 near-term build will have decayed; the spring never sprung).
- [ ] **June FOMC (~6/16):** size is defined-risk through it; reassess regime after.

## Citations summary (M-04 — phase-10 spot-checks these)

1. `[STRUCT:gex]` — ZGL $104.62 vs spot $102.75, regime NEGATIVE, $110 wall +7.4M GEX — phase-4-structure.md §GEX.
2. `[FUND:metric]` — forward PE 20.2 / forward PEG ≈1.0, strong-buy recom 1.35, target $140.63 — phase-7b-fundamentals.md §Valuation.
3. `[MACRO:sector_rotation UW]` — Technology net-directional outflow −$433.5M, persistence 1.0 — phase-6-macro.md §Sector rotation.
4. `[HIST:signal_backtest]` — bullish_flow win_rate 0.857 (n=7) → capped p 0.75 — phase-5-historical.md §Verdict.
5. `[DEBATE]` — phase-8b disconfirmed, bull_residual 0.65 = bear_residual 0.65 — phase-8b-debate.md §Disconfirmation verdict.
