# Trade Blueprint — NVDA 2026-05-29

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis

The live institutional tape is **distributing** — dark-pool mega-tier (≥$10M)
buy_ratio **0.003** (49.1M sold, $10.4B at the 211.14 close) [DP] and UW's
composite reads **DIRECTIONAL_SHORT / DISTRIBUTION** [INSIGHT] — yet the
underlying is **elite and peer-cheap** (rev +71%, EPS +110%, forward PE 17, the
lowest P/E in its AI peer group, strong-buy $307 target) [FUND], which **vetoes a
directional short** into a sector seeing durable, accelerating inflow (Tech flow
persistence 1/1, $11.6B) [MACRO]. With dealers **long gamma pinning 210–220**
[STRUCT], the bull/bear debate a 1-point toss-up [DEBATE], and all four desk
agents unanimous **NEUTRAL/RANGE** [AGENT], this is a **range-bound name with 210
as the single decisive level** — not a directional trade.

## Bias & Conviction

- **Bias:** RANGE (neutral; non-directional)
- **Conviction:** 0.55 (lowest bin — toss-up debate + BUSY_NAME_NORMAL_DAY +
  TRANSITIONAL regime all cap it)
- **Confluence score (from phase-10):** _(filled by phase-10)_

## Entry Zones

| Type | Trigger | Price zone | Notes |
|------|---------|-----------|-------|
| Primary (range) | Spot holding inside the positive-gamma band | **207–214** | Establish the defined-risk iron condor while price is pinned between the 210 put-side gamma and the 215–216 zero-gamma ceiling [STRUCT]. Best entry on a rip toward 214–216 (sell the ceiling) or a dip toward 207–208 (sell the floor). |
| Aggressive (fade strength) | Rejection at the 215–216 zero-gamma ceiling [STRUCT] where today's calls were written & faded [FLOW/OI] | **215–217** | Small defined-risk bear put spread *only* as a fade of a failed rally back into the dealer sell-zone; tight, quick. |
| Fade (plan B → directional) | **Sustained loss of 210** (negative-gamma trapdoor) [STRUCT] | **<210 on expanding volume** | If 210 breaks and holds, the distribution resolves into a trend — flip to the bear put spread (210/200) and abandon the condor's downside wing. Conversely a reclaim/hold of **216 with call OI building (not written)** flips to a 215/225 call-spread long. |

## Levels to Watch

| Level | Price | Source |
|-------|-------|--------|
| Resistance (call wall) | **220** (then 230) | phase-3 OI / phase-4 GEX ceiling |
| Zero-gamma / dealer sell-zone | **215–216** | phase-4 `gex` zero_gamma_level |
| Spot | 211.14 | phase-0 screener close |
| Support (gamma hinge) | **210** | phase-4 negative-gamma trapdoor |
| Support (put wall / neg-gamma) | **200** | phase-3 200P 49-DTE build / phase-4 negative-gamma (not max pain) |
| Price context (advisory) | RSI 49.4 (neutral), −10.7% from 52w high | [HIST:rsi fz] / [HIST:52w_proximity fz] |

## Invalidation

- **Price-based:** A **sustained close below 210** (negative-gamma trapdoor)
  invalidates the range/neutral thesis to the downside → flips to directional
  short (210/200 put spread). A **close above 220** (call wall) on rising call OI
  invalidates it to the upside → mean-reversion long confirmed.
- **Signal-based:** Dark-pool mega-tier buy_ratio flipping **>0.50 for 2 sessions**
  (distribution → accumulation) [DP], OR the 215–225 calls flipping from
  *written* to ask-side *bought* (net_ask_bid turning positive) [OI] — either
  breaks the "institutions selling" leg.
- **Macro-based:** UW market-regime leaving **TRANSITIONAL** for a clean
  RISK-ON/RISK-OFF [MACRO], or Tech sector-flow persistence dropping below 1
  (inflow stalling) — removes the mean-reversion floor.

## Sizing

**Step 1 — Kelly `p`** (from phase-5 sizing handoff, `win_rate_source = backtest`):
- `p_raw = 0.50` (bearish_flow backtest win_rate), `win_rate_n = 8`.
- N-conditional cap (n ∈ 3–9 → max |p−0.50| = 0.05): **p = 0.50** (unchanged).

**Step 2 — Payoff `b`:** primary structure = iron condor 195/200 – 220/225 Jun-18,
~$1.45 credit on $5 wing → `b = max_profit/max_loss = 1.45 / 3.55 ≈ 0.41`.

**Step 3 — Raw Kelly:** `raw_kelly = p − (1−p)/b = 0.50 − 0.50/0.41 = −0.72 → clip
to 0`. **At p = 0.50 there is no Kelly edge for any b < 1** → directional/Kelly
size = **0%**. (Confirmed numerically across b = 0.4–1.0.)

**Step 4 — Risk gates (all five + context):**

| Gate | Source | Fired? | Effect |
|------|--------|--------|--------|
| Fundamentals veto | 7b `VETO` | **YES** | directional short → **watch-only / 0%** |
| Sentiment / crowd | 7c `CONFIRM`, BALANCED | no | no cut |
| Correlation cluster | phase-6 (NVDA-PATH −0.38, NVDA-SNOW −0.10) | no | no cut |
| Sector rotation | phase-6 (aligned-to-long / adverse-to-bear) | n/a for neutral | no cut |
| Debate disconfirm | 8b toss-up (margin 1, directional read fails) | **YES** | −1 bin & −1 size step |
| Context | phase-0.5 `BUSY_NAME_NORMAL_DAY` | **YES** | **no top-of-band** size |

**Step 5 — Final size:** Kelly = **0%** at p=0.50 (no edge for any b<1). The
win-rate map would allow ≤2.5% (half of cap) *before* gates, but three gates
fired — fundamentals **VETO**, debate **disconfirmed**, context
**BUSY_NAME_NORMAL_DAY** — and upward deviation from Kelly is **forbidden when any
gate fires**. Therefore the **recommended deployed risk = 0.0% (watch-only)**.

**Final size = 0.0% — watch-only.** The iron condor below is documented as an
*optional* defined-risk carry the desk may elect at **≤1.0%** if it chooses to
express the gamma-pin range — but it is **not** a Kelly-sanctioned position and is
**not** part of the recommended deployment. The blueprint's instruction is: **do
nothing directional; watch 210.**

## Option Structures

Front-expiry implied move (1-day): **±0.45% / $0.95** [CTX:implied_move]. For the
**Jun-18 (20-DTE)** structures below the relevant expected move is IV-scaled:
IV30d 40.2% → **±9.4% / ±$19.8 → ~191–231 range**. Structures are sized to that.

### Directional (required; watch-only / conditional)

**Bear put spread — buy 210P / sell 200P, exp 2026-06-18.**
- Net debit ≈ **$3.20** (est.), max loss = $3.20, max gain = $6.80 (at ≤200),
  breakeven ≈ **206.80**, payoff b ≈ 2.1.
- **Trigger: only on a sustained loss of 210** (the negative-gamma trapdoor) — do
  NOT put on pre-emptively (the 7b fundamental VETO blocks an unconditional short).
  Strikes anchored to the 210 gamma hinge and the 200 put-build / negative-gamma
  level [STRUCT/OI] (200 is a put-wall + neg-gamma strike, not a max-pain figure).
- A single-day expected move ($0.95) does not threaten this; the spread is for the
  *post-210-break* trend, max loss capped at the debit.

### Defined-risk alternative (PRIMARY)

**Iron condor — sell 205P / buy 200P  +  sell 220C / buy 225C, exp 2026-06-18.**
- Net credit ≈ **$1.45**, max loss = $3.55, breakevens ≈ **203.55 / 221.45**,
  profit zone **205–220** (the positive-gamma pin band) [STRUCT].
- Wings (200/225) sit near the ±1σ expected-move edges (191–231) — the condor
  collects the dealer-pinned range while defining risk. This is the regime's
  prescribed structure ("iron condors in range," phase-6 [MACRO]).
- **Caveat:** VRP is FAIR [HIST] — no vol *edge* to selling premium, so this is a
  range *directional-neutral* bet on the gamma pin, not a vol-harvest. **Optional
  carry only, ≤1.0%** — the recommended deployment is 0.0% / watch-only (gates fired).

## Macro Overlay

- **Tailwinds:** Tech flow persistence 1/1, INFLOW $11.6B (5 sessions)
  [MACRO:SectorFlowPersistence_2026-05-29]; Core CPI 2.74% YoY
  [MACRO:CPILFESL_2026-04]; Fed easing 3.62% + un-inverted 2s10s +0.46
  [MACRO:DFF_2026-05-28 / T10Y2Y_2026-05-28]; SPY UPTREND [MACRO:MarketRegime].
- **Headwinds:** Regime **TRANSITIONAL**, breadth 36.3% bullish, "half-size,
  defined-risk" [MACRO:MarketRegime_2026-05-29]; payrolls softening +115k
  [MACRO:PAYEMS_2026-04]; NVDA beta 2.23 amplifies any SPY downdraft [FUND].

## Catalyst Calendar (next 30d)

| Date | Event | Impact |
|------|-------|--------|
| 2026-06-05 | Weekly OPEX (heavy 0DTE/weekly OI) | pin/gamma, neutral |
| 2026-06-18 | **June monthly OPEX** | OPEX/gamma pull toward 195–200 (neg-gamma/put-build, not max-pain); structure expiry |
| ~mid-June | CPI / FOMC (recurring) | rates re-rate; could break the range |
| 2026-08-26 | **NVDA earnings** | binary — **outside** all structures above |

## Post-Trade Monitoring

- **Daily: the 210 level.** A sustained close below it flips the plan to the bear
  put spread and drops the condor's upside-irrelevant wing — this is the trade.
- **Daily: dark-pool block-stratified buy_ratio** — a flip from 0.003 toward >0.50
  (distribution → accumulation) is the earliest "bottom-in" tell [DP].
- **Per session: 215–225 call OI net_ask_bid** — if written calls flip to
  ask-bought, the 215–216 ceiling is breaking → mean-reversion long [OI/STRUCT].
- **Weekly: Tech sector-flow persistence** — loss of the 1/1 inflow removes the
  fundamental/macro floor under the range [MACRO].
- **On any SPY ≥1% down day:** NVDA beta 2.23 → expect ~2.2× move; pre-plan the
  210-break action rather than reacting.

## Citations Summary

- [DP] Dark-pool mega-tier (≥$10M) **buy_ratio 0.003** (49.1M sold, $10.4B at the
  211.14 close) — phase-2-dark-pool.md §block-stratification.
- [FUND] Forward PE **17**, rev **+71%** / EPS **+110%** YoY, **cheapest P/E in
  AI peer group**, strong-buy $307 target — phase-7b-fundamentals.md §valuation;
  `tier_adjustment: VETO`.
- [MACRO] **Tech flow persistence 1/1, INFLOW $11.6B** — phase-6-macro.md
  §sector-rotation.
- [STRUCT] **Positive-gamma pin 215–230, 210 negative-gamma trapdoor, zero-gamma
  ~215–216** — phase-4-structure.md §gex.
- [DEBATE] Bull 17 / Bear 16, **1-point toss-up** → directional disconfirmed —
  phase-8b-debate.md §judge scorecard.
- [AGENT] 4/4 desk agents **NEUTRAL/RANGE, conviction 2** — phase-8-agent-views.md.
