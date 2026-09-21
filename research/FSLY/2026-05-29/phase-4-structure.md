# Phase 4 — Options Structure (GEX / Max-Pain / Skew / DEX)

## Summary

Dealer structure is **constructive in bias but vol-dampening in mechanics** — which
is the central nuance for FSLY: the squeeze ladder (phase-3) is *armed* but dealer
gamma currently **pins rather than accelerates**. Four reads:

- **GEX regime POSITIVE**: total GEX **+$4.49M**, zero-gamma level **$12.07** (well
  below spot $17.61) → dealers **net long gamma → mean-reversion, reduced vol.** The
  largest positive node is **$17.5 (+$2.24M)**, right at spot — a stabilizing pin.
  Note a **negative node at $16 (−$1.6M)**: just below spot gamma turns negative, so
  a break of ~$16 would *un*-dampen and accelerate downside.
- **Max-pain (6/18, dominant OPEX) = $17.5** (−1.24% from spot) → opex gravity sits
  essentially **at spot**, reinforcing a $17.5 pin into June OPEX.
- **DEX net +$1.63M** (call +$26.6M / put −$25.0M): public net call-long → **dealers
  short calls → hedge is to BUY underlying** — a mild dip-buy cushion (small, fitting
  the small-cap).
- **Skew COMPLACENT**: 25Δ skew **−0.076** (ratio 0.922) — **call IV (96.8%) > put IV
  (89.2%)**, i.e. the call side is bid (squeeze/upside-chasing demand), no downside
  fear premium. IV term **CONTANGO**, no kink (no binary event; earnings 8/05 is far).

**Structural read: BULLISH-bias / NEUTRAL-mechanics near-term.** Positive gamma +
$17.5 max-pain + dealers-buy-dips means the most likely near-term path is a
**dampened pin/grind around $17.5**, *not* an immediate squeeze. The $20/$22.5 call
ladder (phase-3) is real upside fuel but **needs an ignition (volume/sweeps) that
today's tape lacks** — until then dealer gamma caps it. The complacent, call-bid skew
confirms the market *leans* for upside, just not urgently. Conviction MODERATE on the
mechanics; the directional payoff is gated on a volume catalyst.

## GEX (`uw options-structure gex`) `[STRUCT:gex]`

| Field | Value |
|-------|-------|
| Regime | **POSITIVE** (dealers net long gamma) |
| Total GEX | **+$4.49M** |
| Zero-gamma level | **$12.07** (≈ −31% below spot) |
| Underlying | $17.61 |
| Description | "mean-reversion and reduced volatility" |

Near-spot net GEX:

| Strike | Net GEX | Note |
|--------|---------|------|
| **16** | **−$1.61M** | negative node — downside accelerant below $16 |
| 17 | +$0.68M | |
| **17.5** | **+$2.24M** | dominant positive node — the pin |
| 18 | +$1.62M | |
| 20 | +$0.35M | call wall, modest positive |
| 22.5 | +$0.22M | |

- Positive gamma concentrated **$17–$18** (pins spot); turns **negative below $16**
  (the trapdoor). Upside nodes at 20/22.5 are small → dealers don't strongly resist
  *or* fuel the ladder until price is there.

## Max pain (`uw options-structure max-pain`) `[STRUCT:max-pain]`

| Expiry | DTE | Max-pain | Dist % | Total OI |
|--------|-----|----------|--------|----------|
| 2026-05-29 | 0 | $17.0 | −4.06 | 14,829 |
| 2026-06-05 | 7 | $17.5 | −1.24 | 4,506 |
| **2026-06-18** | 20 | **$17.5** | **−1.24** | **39,345** |

- Dominant 6/18 pins at **$17.5** — neutral-to-spot gravity. No strong directional pull.

## DEX (`uw options-structure dex`) `[STRUCT:dex]`

- net_dex **+$1.63M** (call +$26.6M / put −$25.0M) → public net call-long, **dealers
  short calls, hedge buys underlying.** Mild dip-buy cushion; small in absolute terms.

## Skew & IV term (`term-skew`, `iv-term-structure`) `[STRUCT:term-skew]`

- 25Δ skew **−0.076**, ratio 0.922, **COMPLACENT** — call IV 96.8% > put IV 89.2%.
  The **call side is bid** (squeeze/upside demand), no downside-protection premium.
  (Sampled ~411 DTE; the directional label is the read.)
- IV term **CONTANGO**, 14 expiries, no kink — normal upward vol slope, no binary
  event into the horizon. Overall IV is **high** (iv30d 0.88, intake) — options are
  expensive, so long premium pays only on a real move.

## Tool calls

```bash
uw options-structure gex               --symbol FSLY --date 2026-05-29 --json
uw options-structure max-pain          --symbol FSLY --date 2026-05-29 --json
uw options-structure dex               --symbol FSLY --date 2026-05-29 --json
uw options-structure term-skew         --symbol FSLY --date 2026-05-29 --json
uw options-structure iv-term-structure --symbol FSLY --date 2026-05-29 --json
```

## Tool errors

none

## Read-through

- The structure **confirms the bullish *lean*** (call-bid complacent skew, dealers
  dip-buying, positive nodes up to $22.5) but **denies the near-term *trigger***:
  positive gamma + $17.5 max-pain = a dampened pin, so the $20 squeeze ladder is a
  wall that fires only on a volume/sweep ignition the current tape doesn't have.
- **The asymmetry to respect:** gamma flips **negative below $16** — so the same
  dealer mechanics that pin $17.5 would *accelerate* a break under $16. The structure
  is "pinned at $17.5, fuel above $20, trapdoor below $16."
- **High IV is the cost of admission:** iv30d 0.88 means any long-premium expression
  is expensive — you need the squeeze to actually move, not just drift. This argues
  for either patience (wait for the volume ignition) or a cheap, defined-risk,
  far-OTM call-spread expression that the squeeze ladder already prices.
- **For phase-9:** $17.5 = pin/max-pain/gamma node (entry anchor); **$16 = gamma
  trapdoor / invalidation zone**; **$20 → $22.5** = squeeze targets (call walls); IV
  high → defined-risk over outright long premium.

## Citations

- `[STRUCT:gex]` regime POSITIVE, total GEX +$4.49M, ZGL $12.07, +$2.24M node $17.5, −$1.6M node $16 — `uw options-structure gex`
- `[STRUCT:max-pain]` 6/18 max-pain $17.5 (−1.24%) — `uw options-structure max-pain`
- `[STRUCT:dex]` net DEX +$1.63M, dealers short calls buy dips — `uw options-structure dex`
- `[STRUCT:term-skew]` 25Δ skew −0.076 COMPLACENT (calls bid > puts); IV term CONTANGO — `uw options-structure term-skew`

## Upstream references

- phase-3-positioning.md §Summary — "$20→$22.5→$25 squeeze ladder"; phase-4 shows it's
  **armed but gamma-dampened** — positive GEX pins $17.5, the ladder needs a volume
  ignition to fire.
- phase-1-flow.md §Read-through — "no sweeps, light volume"; phase-4 explains why that
  matters: without ignition, positive dealer gamma keeps price pinned, not squeezing.

## Next phase

- phase-5-historical.md (when FSLY/this signal class has set up like this, what
  followed? emits the win-rate for sizing — and whether bullish_flow even fires on
  such a quiet day)
