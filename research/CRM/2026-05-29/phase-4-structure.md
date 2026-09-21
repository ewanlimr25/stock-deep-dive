# Phase 4 — Options Structure (GEX / Max-Pain / Skew / DEX)

## Summary

Dealer structure is **constructive-to-stabilizing, and it leans *against* phase-2's
distribution causing a cascade.** Four aligned reads:

- **GEX regime POSITIVE**: total GEX **+$50.4M**, zero-gamma level **$85.37** (far
  below spot $191.23) → **dealers are net long gamma**, which *dampens* volatility
  and promotes mean-reversion. The largest positive gamma node is **right at $190
  (+$25.9M)** — a stabilizing shelf at the close. (Contrast: a negative-gamma name
  would accelerate phase-2's selling; CRM does the opposite.)
- **Max-pain (6/18, the dominant OPEX) = $190**, only **−0.53%** from spot →
  **opex gravity is essentially AT the close.** Holder value at max pain $82.7M.
  The 0DTE/6-5 max pains are lower ($177.5) but those expiries are small; the
  weight is 6/18 at $190.
- **DEX net +$585.6M** (call_dex +$1.19B, put_dex −$0.60B): **public is net
  call-long → dealers are net short calls → dealer hedge is to BUY underlying.**
  This makes dealers *natural dip-buyers* near-term — a cushion under the price.
- **Skew COMPLACENT**: 25Δ put/call skew **−0.025** (ratio 0.948) — **puts are
  *cheaper* than calls.** No fear/tail premium bid; the market is not paying up for
  downside protection. IV term structure **CONTANGO** (normal, no event kink —
  consistent with earnings being *behind* us).

**Structural read: BULLISH-to-STABILIZING.** Positive dealer gamma + max-pain at
$190 + dealers-buy-dips DEX means the near-term path is more likely **pinned/grinding
around $190–$195 with dampened vol** than a sharp reversal. The $200 call wall
(phase-3) is the upside magnet; the $190 gamma node is the floor-ish pin. This
**partially neutralizes phase-2's distribution worry** — the institutions are
selling, but the dealer mechanics absorb rather than amplify it.

## GEX (`uw options-structure gex`) `[STRUCT:gex]`

| Field | Value |
|-------|-------|
| Regime | **POSITIVE** (dealers net long gamma) |
| Total GEX | **+$50.4M** |
| Zero-gamma level | **$85.37** (≈ −55% below spot — deeply positive zone) |
| Underlying | $191.23 |
| Description | "expect mean-reversion and reduced volatility" |

Net GEX by near-spot strike:

| Strike | Net GEX | Note |
|--------|---------|------|
| 185 | −$0.59M | small negative just below |
| 187.5 | +$1.96M | |
| **190** | **+$25.87M** | **dominant positive node — stabilizing pin** |
| 192.5 | +$2.05M | |
| 195 | +$7.81M | reinforces $195 wall |
| 200 | +$8.42M | reinforces $200 call wall |

- Positive gamma stacks at 190/195/200 → dealers sell rallies / buy dips across the
  $190–$200 zone, **capping** upside at the walls but also **buffering** downside.

## Max pain (`uw options-structure max-pain`) `[STRUCT:max-pain]`

| Expiry | DTE | Max-pain | Dist % | Total OI |
|--------|-----|----------|--------|----------|
| 2026-05-29 | 0 | $177.5 | −7.07 | 116,200 |
| 2026-06-05 | 7 | $177.5 | −7.07 | 29,457 |
| **2026-06-18** | 20 | **$190.0** | **−0.53** | **209,850** |

- The **dominant 6/18 expiry pins at $190** — right at the close. Opex gravity is
  neutral-to-supportive near current price, not pulling sharply lower (the $177.5
  near-dated pins carry far less OI).

## DEX (`uw options-structure dex`) `[STRUCT:dex]`

- net_dex **+$585.6M**; call_dex +$1.19B, put_dex −$0.60B.
- Interpretation: **public net call-long → dealers net short calls → dealer hedge =
  BUY underlying.** Dealers are mechanically biased to support price on weakness
  near-term. Reinforces the positive-gamma cushion.

## Skew & IV term (`term-skew`, `iv-term-structure`) `[STRUCT:term-skew]`

- 25Δ skew **−0.025**, ratio 0.948, interpretation **COMPLACENT** — put IV (45.2%)
  *below* call IV (47.7%). No downside fear premium; if anything the call side is
  bid. (Note: skew sampled at ~365 DTE; near-dated skew not separately surfaced, but
  the COMPLACENT label is the structural read.)
- IV term **CONTANGO** (19 expiries, no kink) — normal upward-sloping vol; the lack
  of a front-end kink confirms **no imminent binary event** (earnings already passed
  ~5/28). Front weekly avg IV ~52% vs deferred — elevated but not stressed.

## Tool calls

```bash
uw options-structure gex               --symbol CRM --date 2026-05-29 --json
uw options-structure max-pain          --symbol CRM --date 2026-05-29 --json
uw options-structure dex               --symbol CRM --date 2026-05-29 --json
uw options-structure term-skew         --symbol CRM --date 2026-05-29 --json
uw options-structure iv-term-structure --symbol CRM --date 2026-05-29 --json
```

## Tool errors

none

## Read-through

- **Phase-4 is the counterweight to phase-2.** The dark-pool tape said institutions
  distributed; the dealer-structure tape says the *mechanics* around $190 are
  stabilizing, not fragile. Positive gamma (+$50.4M, node at $190), max-pain pinned
  at $190, dealers hedging by buying dips (DEX +$586M), and **no downside fear bid**
  (complacent skew) together argue the +8.5% level is more likely to be **held/pinned
  near $190–$195** than to reverse violently in the very near term.
- **The synthesis tension is now sharp and well-defined:**
  - *Bull (flow + OI + structure):* call-buying targets $200, dealers buy dips, vol
    dampened, max-pain at $190 supports the close → grind toward $195/$200.
  - *Bear (dark pool):* the biggest holders sold ~$1.05B into the pop; supply
    overhang caps the move and bleeds it lower once dealer support fades past 6/18.
  - Phase-4 tilts the **near-term (into 6/18)** toward the bull/pin case; phase-2's
    distribution is more of a **medium-term** headwind. This horizon split is the key
    input for phase-9 structure/tenor selection.
- **Decision geometry for phase-9:**
  - **$190** = positive-gamma node + 6/18 max-pain = near-term pin/support.
  - **$185** = first OI support below (phase-3); below it an air pocket to $170/$160.
  - **$195 → $200** = call walls + positive-gamma caps = upside targets/resistance.
  - Complacent skew → **put protection is cheap** if a hedged-long structure is
    chosen (relevant to phase-9 given phase-2's overhang).

## Citations

- `[STRUCT:gex]` regime POSITIVE, total GEX +$50.4M, ZGL $85.37, +$25.9M node at $190 — `uw options-structure gex`
- `[STRUCT:max-pain]` 6/18 (dominant, 209,850 OI) max-pain $190, −0.53% from spot — `uw options-structure max-pain`
- `[STRUCT:dex]` net DEX +$585.6M → dealers short calls, hedge buys underlying — `uw options-structure dex`
- `[STRUCT:term-skew]` 25Δ skew −0.025 COMPLACENT (puts cheaper than calls); IV term CONTANGO — `uw options-structure term-skew` / `iv-term-structure`

## Upstream references

- phase-2-dark-pool.md §Read-through — "distribution into the pop, fade-risk high";
  phase-4 **partially offsets** it: positive dealer gamma + dip-buying DEX dampen,
  rather than amplify, near-term downside.
- phase-3-positioning.md §OI walls — "$200 call wall, support not until $185";
  phase-4 confirms positive-gamma caps at 195/200 and a stabilizing node at $190
  (above the $185 OI shelf).

## Next phase

- phase-5-historical.md (when CRM has had a call-heavy, IV-crush, post-pop day like
  this, what happened next? emits the empirical win-rate for Kelly sizing)
