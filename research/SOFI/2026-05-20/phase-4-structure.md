# Phase 4 — Dealer Structure & Gamma

**Ticker:** SOFI
**As-of date (requested):** 2026-05-20
**Effective data date:** 2026-05-19
**Generated:** 2026-05-20T00:00:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md

## Summary

SOFI dealer structure shows **two regimes overlapping**. The multi-week
(DTE ≤ 45) frame is labeled **POSITIVE / long-gamma** by UW with ZGL at $11.65
— meaning spot at $15.16 sits comfortably above the multi-week flip and
dealers will fade rallies / support dips in calm conditions. However the
intraday May-22 OPEX-week book is short-gamma: today's total GEX -$3.66B,
today's ZGL $13.15, and the dominant strike is **$15 with NET GEX of
-$47.27B** — a massive negative-gamma node from the put-write demand
documented in phase-3 [OI:smart_positioning]. Above $15, the chain flips
sharply positive: **$16 holds +$25.18B GEX (largest positive wall)**,
**$16.5 holds +$11.57B**, $17 holds +$5.44B. Mechanically: a break of $15
unleashes accelerated downside (negative-gamma trapdoor); a push above
$15.50 hits dealer-sell hedges that cap the move at $16. **DEX is -$24.87B
(public net long puts → dealers net short puts → dealer hedge is to SELL
underlying** on the bid). **Term skew is COMPLACENT (-5.1%, calls richer
than puts at 30 DTE)** — downside protection is unusually cheap.
**Term structure is BACKWARDATION** driven by lottery-IV May-22 lottery
contracts; the 9/30-day ratio is in CONTANGO (0.94) → no event stress
within the next month. Net read: **mean-reversion within $15-$16 with a
sharp trapdoor below $15 and a strong magnet at $16 — favorable for
range-bound or short-gamma strategies; downside hedging is cheap because
of complacent skew**.

## Key signals

- **Multi-week regime: POSITIVE / long-gamma; ZGL = $11.65; spot $15.16**.
  Mean-reversion / vol-suppression structurally for the next 6+ weeks.
  [STRUCT:gex]
- **Intraday (May-22) regime: NEGATIVE / short-gamma; today's ZGL = $13.15;
  today's total GEX -$3.66B**. Trend amplification through Friday.
  [STRUCT:today_gamma_flip]
- **Single largest negative-gamma node: $15 strike, net GEX -$47.27B** —
  derived from 80,486 OI at the pin [OI:pin_risk]. Volatility amplifier on
  break of $15. [STRUCT:gex]
- **Single largest positive-gamma node: $16 strike, net GEX +$25.18B** —
  hard mean-reversion ceiling. [STRUCT:gex]
- **DEX -$24.87B (call_dex +$72.21B, put_dex -$97.08B)** — dealers net short
  puts; hedging direction: SELL on rallies. [STRUCT:dex]
- **Term skew COMPLACENT** (put 25Δ IV 54.3% vs call 25Δ IV 59.4%, skew
  -5.1%) — downside protection is cheap. [STRUCT:term_skew]
- **Vanna-squeeze setup armed**: net vanna +$1.85M, put vanna +$5.33M.
  Falling IV → dealers cover short puts by BUYING stock. [STRUCT:vanna_charm]

## Detailed findings

### GEX (multi-week, DTE ≤ 45)

- **Total GEX:** -$4,609,650,391
- **Regime:** POSITIVE (label) / spot 15.16 above ZGL 11.65
- **ZGL:** $11.65 (well below spot — would require -23.2% move to flip
  multi-week regime to short-gamma)

Top per-strike GEX (DTE ≤ 45):

| Strike | Net GEX | Role |
|---|---|---|
| 13 | -$141.9M | Minor negative node |
| 13.5 | -$64.2M | Minor negative node |
| 14 | -$1.74B | Negative-gamma support shelf |
| 14.5 | -$6.20B | Negative-gamma shelf |
| **15** | **-$47.27B** | **Dominant pin / trapdoor** |
| 15.5 | +$3.87B | Positive support wall |
| **16** | **+$25.18B** | **Largest positive wall — ceiling** |
| 16.5 | +$11.57B | Strong positive resistance |
| 17 | +$5.44B | Positive |
| 17.5 | +$699M | Positive |
| 18 | +$1.93B | Positive |
| 19 | +$243M | Positive |
| 20 | +$1.49B | Positive (LEAP-driven) |
| 22 | +$82.1M | Positive |
| 25 | +$75.0M | Positive (LEAP) |
| 30 | +$20.9M | Positive (LEAP) |

The chart is asymmetric: ENORMOUS negative GEX concentrated at $15 (a single
strike that dwarfs the rest of the negative side combined), with the entire
positive side stacked from $15.50-$20 with the peak at $16. This is a
**"mean-reversion bracket" structure** — price wants to stay between $15
(trapdoor) and $16-$16.50 (ceiling). The next clean range *above* this is
$16.50-$18 (positive but lighter gamma).

### DEX (net dealer delta hedge)

- **Net DEX:** -$24,867,575,774
- **Call DEX:** +$72,212,460,318 (public net long calls → dealers short calls →
  dealer hedge BUYS underlying)
- **Put DEX:** -$97,080,036,093 (public net long puts → dealers short puts →
  dealer hedge SELLS underlying)
- **Net direction:** put exposure dominates; aggregate dealer hedge SELLS into
  rallies. This is consistent with phase-3 finding that institutions sold
  May-22 $15P (32k OI) and $14.5P — leaving dealers long those puts (or short
  the offsetting position with the public).

Note: this contradicts phase-3 interpretation that put-write at $15 was
institutional. The reconciliation is that the *flow* on 2026-05-19 added new
put-write OI at $15 (bid-heavy), but the *stock* of legacy OI (much of which
is public long-put / dealer-short-put from prior weeks) still dominates the
DEX calc.

### Vanna + charm

- **Net vanna:** +$1,850,917 (put-heavy book)
- **Net charm:** +$322,699,529 (positive — strong dealer time-decay collection)
- **Put vanna:** +$5,334,646
- **Call vanna:** -$3,483,729
- **Interpretation:** classic vanna-squeeze setup — if IV collapses (e.g.
  post-OPEX vol crush after Friday May-22), dealers are forced to BUY
  underlying to cover their short-put delta (since |put delta| drops as IV
  falls). Mechanical bullish vector if IV decays.

### IV term structure

**Regime: BACKWARDATION** (front-end IV much higher than back-end), driven
almost entirely by lottery-IV May-22 contracts.

| Expiry | Avg IV | Contracts |
|---|---|---|
| **2026-05-22** | **101.8%** | 13,845 (lottery-IV bias) |
| 2026-05-29 | 63.9% | 5,168 |
| 2026-06-05 | 78.7% | 3,100 |
| 2026-06-12 | 67.8% | 1,237 |
| 2026-06-18 | 68.0% | 4,492 |
| 2026-06-26 | 61.9% | 2,544 |
| 2026-07-17 | 70.4% | 2,073 |
| 2026-08-21 | 68.5% | 1,994 |
| **2026-09-18** | **87.2%** | 1,714 (**kink — likely earnings**) |
| 2026-10-16 | 64.3% | 835 |
| 2026-11-20 | 67.0% | 489 |
| 2026-12-18 | 68.2% | 1,317 |
| 2027-01-15 | 67.7% | 2,132 |
| 2027-03-19 | 69.8% | 473 |
| 2027-06-17 | 69.6% | 624 |
| 2027-12-17 | 70.9% | 295 |
| 2028-01-21 | 70.8% | 980 |
| 2028-06-16 | 69.7% | 2,048 |

**Two key observations:**
1. May-22's 101.8% IV is artificial — driven by deep-ITM 1C/2C/3C with mechanical
   IVs of 1000%+ (see phase-1 [FLOW:iv_outliers]). The "true" front-month IV
   is May-29's **63.9%**.
2. **Sep-18 expiry IV 87.2%** sits as a clear kink relative to surrounding
   Aug-21 (68.5%) and Oct-16 (64.3%) — strongly suggests **earnings event
   priced into the Sep-18 monthly expiry**. Phase 6 calendar must confirm
   (likely SOFI Q2 earnings late July / early Aug missed Aug-21 expiry, or
   Q3 guide / investor day).

### Term skew (25Δ at 30 DTE)

- **Put 25Δ IV:** 54.3%
- **Call 25Δ IV:** 59.4%
- **Skew:** -5.1% (NEGATIVE = call skew, calls richer than puts)
- **Skew ratio:** 0.914
- **Regime label:** **COMPLACENT**

**This is meaningful.** Most US single-name equities trade with put-skew
(puts ~5-15% richer than calls) — reflecting market-wide demand for tail
hedges. SOFI inverting to call-skew means **the marginal options buyer is
chasing UPSIDE, not hedging DOWNSIDE**. This is consistent with phase-1
[FLOW:sweeps] showing aggressive ATM call buying. The trade implication:
**downside puts are cheap relative to upside calls** — for a multi-week
position, a long put or put-spread is asymmetrically attractive as a hedge.

### Front-end IV ratio (event stress, 9 DTE vs 29 DTE)

- **Near IV (9 DTE / May-29):** 63.9%
- **Far IV (29 DTE / Jun-18):** 68.0%
- **Ratio:** 0.94 → **CONTANGO**

No event-stress signal in the next 7-30 days. Combined with the COMPLACENT
skew, this confirms that **no near-term catalyst is being priced in** —
consistent with the lack of OPEX concentration in phase 3.

### Today's gamma flip (May-22 expiry, 3 DTE)

- **Today's ZGL:** $13.15
- **Today's total GEX:** -$3,661,604,121 → **NEGATIVE (short-gamma intraday)**
- **ATM flip strike:** $12

| Wall | Strike | Net GEX | Role label |
|---|---|---|---|
| Resistance | **$15** | **-$39,836,459,348** | Dominant pin / floor |
| Support | **$16** | **+$23,219,084,087** | Largest positive ceiling |
| Support | $16.5 | +$10,854,172,954 | Secondary ceiling |
| Resistance | $14.5 | -$4,387,655,195 | Lower support |
| Support | $15.5 | +$4,019,832,345 | Pivot |

UW's "resistance" / "support" labels reflect dealer hedge mechanics rather
than chart vocabulary:
- **Negative-GEX "resistance" walls** at $15 and $14.5 = volatility amplifiers
  where dealers fight price (or pin). Break of $15 = "trapdoor" toward $14.5.
- **Positive-GEX "support" walls** at $15.5 / $16 / $16.5 = mean-reversion
  magnets where dealers sell rallies (capping upside).

**For 0DTE through May-22:** SOFI is gravitationally bound to $15-$16 with
maximum dealer-pin pressure at $15. Expect either a Friday close near
$15.00-$15.50 or, if volatility expands, a break of $15 toward $14.50.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|---|---|---|
| `options_structure_gex` | symbol=SOFI, dte-max=45, include-zero-gamma=true, date=2026-05-19 | ZGL $11.65; total GEX -$4.61B; regime POSITIVE; peaks $15(-$47B) / $16(+$25B) |
| `options_structure_dex` | symbol=SOFI, dte-max=45, date=2026-05-19 | Net DEX -$24.87B; dealer hedge SELLS underlying |
| `options_structure_vanna_charm` | symbol=SOFI, dte-max=45, date=2026-05-19 | Net vanna +$1.85M (put-heavy); net charm +$322.7M; vanna-squeeze armed |
| `options_structure_iv_term_structure` | symbol=SOFI, date=2026-05-19 | BACKWARDATION (artifact from May-22 lottery IV); Sep-18 KINK at 87.2% |
| `options_structure_term_skew` | symbol=SOFI, dte-target=30, date=2026-05-19 | Skew -5.1% (calls richer than puts) → COMPLACENT |
| `options_structure_front_end_iv_ratio` | symbol=SOFI, near-dte=7, far-dte=30, date=2026-05-19 | Ratio 0.94 → CONTANGO; no event stress in next 30d |
| `options_structure_today_gamma_flip` | symbol=SOFI, date=2026-05-19 | Today expiry May-22; ZGL $13.15; total GEX -$3.66B NEGATIVE; pin $15 |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** **structural range-bound mean-reversion with a
  short-gamma intraday tilt through Friday, complacent downside skew, and a
  vanna-squeeze setup if IV crushes post-OPEX**.
- **Conviction:** **4 / 5** — internally consistent structural picture across
  GEX / DEX / vanna / skew / term structure; the only friction is the
  POSITIVE multi-week regime label vs. NEGATIVE intraday total — and that
  contradiction resolves naturally (multi-week regime is set by far-out OI
  at $20-$25 strikes; intraday is set by May-22 short-dated put-write OI at
  $15).
- **Three structural levels for phase 9:**
  1. **$15.00 — gamma trapdoor / pin.** -$47.27B GEX. Break of $15 =
     volatility expansion to $14.50. Use as primary stop on long entries.
  2. **$16.00 — dealer ceiling.** +$25.18B GEX (largest positive wall).
     Use as primary profit target for any long-side trade; expect heavy
     dealer-sell hedging here.
  3. **$13.15 / $11.65 — intraday ZGL / multi-week ZGL.** If $15.00 breaks,
     next dealer-support zones. Use as **catastrophic stop** for any LEAP
     long.
- **Open questions:**
  - Is the Sep-18 IV kink (87.2%) driven by an earnings event? Phase 6 must
    confirm.
  - Does dark pool accumulation persist intraday on 2026-05-20 (RTH not
    yet available)? Phase 5 historical trend check.
  - Given complacent skew + vanna-squeeze setup, does Phase 7
    [INSIGHTS:institutional_accumulation / insights_deep_dive] flag the
    same vol-collapse-into-rally setup?
  - Reconciliation: phase-3 said put-write at $15 was institutional
    BULLISH; phase-4 DEX -$24.87B says aggregate dealers are SHORT puts
    (hedging by SELLING stock). Both can be true if 2026-05-19's flow was
    incremental bullish on top of a legacy bearish/protective book. Phase
    10 audit must flag this for confluence scoring.
