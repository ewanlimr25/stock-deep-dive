# Phase 9 — Trade Plan (PM Synthesis)

**Ticker:** CRM (Salesforce Inc) · **As-of:** 2026-05-29 · **Spot ref:** $191.10
**Bias:** LONG (tactical) · **Conviction bin:** 0.65 · **Horizon:** 1–4 weeks (into 6/18 OPEX)

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis

Buy the post-beat continuation in a cheap, beaten-down quality laggard — **small and
defined-risk**, because the institutional cash tape is on the other side. CRM printed
its **third straight accelerating earnings beat (+23.9%)** `[FUND:earnings_surprise]`
at **12.4× forward earnings / PEG 0.99** `[FUND:forwardPE fz]` after a −27.9% YTD
drawdown, and the options tape responded with **20-of-20 call sweeps, $26.3M, ~54%
ask-side, premium concentrated in the 6/18 & 7/17 monthlies targeting the $200
strike** `[FLOW:sweeps]` — which is the **heaviest call wall in the chain (net
+58,153 OI)** `[OI:oi-by-strike]`. Dealers are **net long gamma (+$50.4M, +$25.9M
node at $190) and short calls (DEX +$585.6M) → they buy dips into 6/18**
`[STRUCT:gex]` `[STRUCT:dex]`, and the trade rides the **single most persistent
sector inflow in the market (Technology, persistence 1.0, five sessions to +$11.6B)**
`[MACRO:sector_flow_persistence]` with **7.9% short interest as covering fuel**
`[SENT:short_float fz semi-monthly]`. Empirically, `bullish_flow` days ran **60% (5d)
/ 72.9% (10d), avg +5%** `[HIST:signal-backtest]`.

The disconfirming evidence is real and caps the trade: **$1.05B of mega/block
dark-pool premium sold ~90% one-sided into the pop, pinned at the $191.10 close**
`[DP:block-stratified]` (corroborated by `fz` Inst Trans −1.78% `[SENT:retail_vs_inst
fz]` and the engine's DISTRIBUTION verdict, 32.9% `[INSIGHT:conviction-matrix]`).
Phase-7b reframes that selling as **mechanical profit-taking, not informed
distribution** — there is no fundamental rot to front-run — but the phase-8b debate
forced the concession that it still **caps the advance's slope** toward a $190–$195
pin rather than a clean $200 run, on a **thin floor with no support between $191 and
$185**. Net: directional edge confirmed LONG (0 of 5 desk agents short; debate **not
disconfirmed**, bull 0.65 vs bear 0.55), but thin — a tactical, level-defined,
small-size long, expressed defined-risk to neutralize the trapdoor.

## Entries

| Type | Price | Trigger | Source |
|------|-------|---------|--------|
| **Primary** | **$190.0** | pullback into the +$25.9M positive-gamma node / 6/18 max-pain; dealer dip-buy zone | `[STRUCT:gex]` / `[STRUCT:max-pain]` |
| Aggressive | $187.5 | deeper fade toward the $185 OI shelf that holds (buy weakness dealers defend) | `[OI:oi-by-strike]` |
| Fade (counter) | $195.0 | rejection at the $195 call wall without a volume break → trim/avoid chasing | `[OI:oi-by-strike]` |

## Levels

| Level | Price | Role |
|-------|-------|------|
| Resistance (target) | **$200** | heaviest call wall (net +58,153 OI) + sweep magnet + positive-gamma cap |
| Intermediate | $195 | second call wall (net +24,417); debate base-case pin |
| Gamma node / pin | **$190** | +$25.9M GEX node + 6/18 max-pain |
| Support (first shelf) | $185 | first net-put OI shelf — **the line** |
| Air-pocket floor | $170 / $160 | put walls below the gap (no support 185→170) |

## Invalidation

- **Price:** a **sustained close below $185** (unanimous desk + debate) — loses the
  only near floor and opens the air pocket to $170. `[OI:oi-by-strike]`
- **Signal:** **GEX flips toward negative / DEX support fades**, or the **190C
  call-writing signature broadens** (dealers no longer dip-buying). `[STRUCT:dex]`
- **Macro/thesis-engine:** **Technology sector-flow persistence breaks its inflow
  streak** (the early-warning the laggard-catch-up engine has failed). `[MACRO:sector_flow_persistence]`

## Sizing

| Input | Value | Source / note |
|-------|-------|---------------|
| `p_raw` | 0.60 | phase-5 `bullish_flow` 5d win-rate (10d = 0.729) `[HIST:signal-backtest]` |
| `win_rate_n` | 70 | N≥20 → cap 0.90 |
| `p` (capped) | **0.60** | min(0.60, 0.90); **universe-pooled / in-sample → not haircut further but kept at the conservative 5d rate** |
| Payoff `b` | **1.5** | (target $200 − entry $191) / (entry $191 − stop $185) = 9/6 |
| `raw_kelly` | **0.333** | (0.60·1.5 − 0.40)/1.5 |
| fraction | 0.25 | fractional Kelly |
| suggested (pre-gate) | min(0.333·0.25·100, 5) = **5.0%** | Kelly × fraction, hit cap_pct |
| win-rate map ceiling | **2.5%** | p∈[0.50,0.70] → half of cap → take the smaller |
| **Gates applied** | all no-op / soft-watch | see below |
| **`final_size_pct`** | **1.5%** | deviation **downward** (always allowed): thin base-case R:R + half-size regime |

**Risk gates (each can only cut):**
1. **Fundamentals (7b): CONFIRM** → no-op.
2. **Sentiment/crowd (7c): NO-CUT, BALANCED** → no-op.
3. **Correlation cluster:** CRM/NOW 0.89, CRM/ADBE 0.88 — but **no *other* open
   research blueprint exists** to cluster against → **soft-watch, surfaced not cut.**
   (If a software peer long is open elsewhere, size CRM+peer as ONE line, one stop.)
4. **Sector rotation: ALIGNED** (Tech persistent inflow *supports* the long) → no-op.
5. **Debate disconfirmation: FALSE** (bull 0.65 ≥ bear 0.55) → no-op.

**Context modifier (0.5):** GENUINELY_UNUSUAL → no-op (edge already in `p`).

## Structures (sized so max-loss ≤ 1.5% of book risk)

| # | Kind | Type | Strikes | Expiry | Debit/Credit | Breakeven | Max loss | Note |
|---|------|------|---------|--------|--------------|-----------|----------|------|
| 1 | directional | **call debit spread** | **190/200** | 2026-06-18 | ~$3.6 debit | ~$193.6 | $3.6 (per spread) | anchored to the $190 gamma node and the $200 call wall; caps at the structural target, neutralizes the $185 trapdoor (loss is the debit, not the stock) |
| 2 | defined_risk | **put credit spread** | **180/175** | 2026-06-18 | ~$1.6 credit | ~$178.4 | $3.4 (width−credit) | sells the $185-floor/$180 shelf; finances the long, profits if the $190 pin holds; **complacent skew (puts cheap)** makes this less rich — use as a financing leg only `[STRUCT:term-skew]` |

- **Preferred expression:** the **190/200 call debit spread (6/18)** — defined-risk,
  rides PEAD-drift + short-covering toward the $200 wall, max-loss = debit. The put
  credit spread is an optional financing overlay for those comfortable with the
  $180/$175 short strikes (below the $185 invalidation).
- **Why defined-risk, not shares/outright calls:** the bear's unrefuted point (the
  $1.05B distribution + thin 191→185 floor) means an outright long carries gap risk
  to $170; the debit spread caps the loss at the premium and the regime guidance is
  explicitly "defined-risk." `[DP:block-stratified]` `[MACRO:market-regime]`

## Expected move

- Screener daily implied move **0.52%** (~$0.99) `[CTX:implied_move]`.
- Front-week (6/5, 7 DTE) expected move ≈ **±6.3%** (~±$12), and 6/18 (20 DTE) ≈
  **±10.7%** (computed from IV30d 0.458) — the $190/$200 spread width (~5%) sits
  inside the 6/18 expected move, i.e. the target is reachable within normal vol.

## Macro

- **Net: tailwind (qualified).**
- Tailwinds: `[MACRO:sector_flow_persistence]` Technology #1 inflow, persistence 1.0,
  5 sessions to +$11.6B; `[MACRO:market-regime]` SPY UPTREND, −0.21% from 90d high.
- Headwinds: `[MACRO:market-regime]` breadth only 36.3% bullish (narrow tape,
  "half-size"); `[MACRO:portfolio_correlation]` CRM β1.13, 0.88-correlated to the
  software cluster → no shelter if tech reverses.

## Catalysts

| Date | Event | Impact |
|------|-------|--------|
| 2026-06-18 | June monthly OPEX (dominant 24.86% of OI; max-pain $190) | ? |
| 2026-09-02 | Next earnings (beyond horizon; no event-vol into the trade) | ? |

## Key risks

1. **Institutional distribution is informed, not mechanical** — $1.05B mega/block
   ~90% sell into the close; if it continues, the thin 191→185 floor gaps to $170. `[DP:block-stratified]`
2. **Base-case R:R is thin** — a $190–$195 pin (debate concession) is sub-1:1 vs the
   $185 stop; the trade *needs* the $195-break / short-covering tail to pay. `[OI:oi-by-strike]`
3. **Correlation/breadth fragility** — 36.3%-breadth tape, CRM the highest-beta
   0.88-correlated laggard; a tech wobble hits it hardest with no diversification. `[MACRO:portfolio_correlation]`
4. **Call-writing under the surface** — 190C 6/5 prior-day bid>ask; part of the
   "bullish" call OI is supply, so the flow edge is thinner than the premium headline. `[OI:smart-positioning]`

## Citations (≥3 distinct upstream datapoints)

- `[FLOW:sweeps]` 20/20 call sweeps, $26.3M, ~54% ask, targeting $200
- `[OI:oi-by-strike]` $200 call wall net +58,153 OI; first support $185, gap to $170
- `[DP:block-stratified]` mega buy-ratio 0.017 / block 0.098 — $1.05B ~90% sell into the pop
- `[STRUCT:gex]` `[STRUCT:dex]` positive gamma +$50.4M (node $190) + DEX +$585.6M dealers buy dips
- `[FUND:earnings_surprise]` +23.9% beat, 3rd straight accelerating; fwd P/E 12.4
- `[HIST:signal-backtest]` bullish_flow 60% (5d) / 72.9% (10d), avg +5%
- `[MACRO:sector_flow_persistence]` Tech persistence 1.0, 5 sessions, +$11.6B
- `[SENT:short_float fz semi-monthly]` 7.91% SI, 4.71 DTC — covering fuel

## Upstream references

- phase-8b-debate.md §Disconfirmation — bull 0.65 vs bear 0.55, **not disconfirmed**;
  this plan inherits the "slope-capped, trapdoor-floored, small/defined-risk" verdict.
- phase-8-agent-views.md §Verdict — 3 LONG / 2 NEUTRAL-lean-long / 0 SHORT, avg conv
  2.4; plan = tactical long at conviction 0.65, half-size-then-deviated-down to 1.5%.
- phase-2 / phase-7b — the informed-vs-mechanical distribution question resolved
  mechanical-leaning, but carried as the #1 key risk and the $185 invalidation.

## Next phase

- decision.json (written alongside) → phase-10-audit.md (confluence score + contradiction sweep)
