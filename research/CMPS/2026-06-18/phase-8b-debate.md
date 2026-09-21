# Phase 8b — Bull vs Bear Debate (disconfirmation)

**Ticker:** CMPS
**As-of date:** 2026-06-18
**Generated:** 2026-06-20
**Upstream phases cited:** phase-1 … phase-8 (all)

## Summary

The defender (the **fade-the-bear / don't-short** case — phase-8's dominant bias)
held up. After two rounds, **bull_residual 0.75** vs **bear_residual 0.65** →
**disconfirmed = false**. The defender's strongest unrefuted plank is that the entire
bearish thesis is a *single, non-persistent, unsettled* LEAP-put print
(`consistency 0.2, 1 session` [FLOW:sweep_persistence]) against improving
fundamentals (insiders buying [FUND:insider_MSPR], strong-buy revisions
[SENT:recommendation]) and a long-gamma pin [STRUCT:gex]. The bear's strongest
unrefuted plank — which keeps it at a respectable 0.65 — is that a deep-OTM 582-DTE
put bought *aggressively on the ask* is the rational way to pre-position for the
**COMP006 26-week durability binary (H2 2026)** [MACRO:CMPS_catalyst], a real event
neither side can resolve today. Net: the desk's "no directional short" conclusion
survives; the debate adds **no extra size cut**, but the durability binary is logged
as the live risk to any expression.

## Setup

- **Thesis-defender (the "bull"):** defends phase-8's dominant bias — **do NOT short
  CMPS; fade/neutral with a mild long-lean.**
- **Thesis-attacker (the "bear"):** argues the **bearish flow is informed smart money
  → short / own downside.**
- **Dominant bias defended:** NEUTRAL / fade-the-bear (phase-8: 3 NEUTRAL + 1 RANGE,
  0 SHORT, 0 LONG).
- **Rounds run:** 2 (phases not unanimous; phase-7b = VETO, so the 1-round shortcut
  does not apply).

## Round 1

### Bull (defender) — round 1

The bear has exactly one bullet, and it has already missed. The entire short thesis
rests on a *single* Jan-2028 $10 put bought ask-side for ~$647K [FLOW:top_premium_trades]
— and the desk's own tooling says it is not a campaign: `consistency 0.2`,
`sessions_in_top 1`, no smart-money-flow rows [FLOW:sweep_persistence]. It is not even
in the book yet — the 2028 expiry shows `put_oi = 0` and `biggest-increases` is EMPTY
[OI:term_structure, OI:biggest_increases]. One orphan print is not a position. Meanwhile
*everything that compounds* points the other way: insiders are net buyers into this
(MSPR **+100** in May'26 on +197,937 shares [FUND:insider_MSPR]), analysts are raising
estimates (strongBuy **5→7**, zero sells [SENT:recommendation]) with a **$21.72 target,
+73%** [FUND:recom fz], both Phase-3 trials hit their endpoints [MACRO:CMPS_catalyst],
and the dealer is **long-gamma, FULLY_POSITIVE GEX**, pinning $12–13 and *buying* dips
[STRUCT:gex, STRUCT:dex]. Phase-7b stamped a fundamental **VETO** on the short
[FUND:tier_adjustment]. You do not short a +81.6%-YTD name [HIST:perf_ytd fz] that
insiders are buying and the dealer is defending, on the strength of one hedge.

## Strongest opposing point I cannot refute
The bear will say the put was **bought on the ask, aggressively, paying up** — net
delta-notional −$411K [FLOW:delta_notional] — and that *someone with size chose deep-OTM
582-DTE convexity right before the COMP006 26-week durability readout* [MACRO:CMPS_catalyst].
I cannot refute that the timing is rational for an informed bear: durability *is* the
historical failure mode of psychedelic antidepressants, the data is H2 2026, and a LEAP
put is precisely how you express that without theta bleeding you out. My "it's just a
hedge" reframe is an assumption, not a proof — I genuinely do not know who printed it or why.

## Residual confidence
Residual confidence: 0.75

### Bear (attacker) — round 1

"One orphan print" is the defender's tell — it is *anchoring on persistence when the
instrument is designed to be a single print.* You do not *campaign* a 582-DTE LEAP; you
buy your convexity once and wait [FLOW:unusual_volume, vol/OI 13.97 = brand-new]. The
absence of follow-through is not absence of conviction — it is the correct execution of a
binary-event bet. And look at *what* it costs: deep-OTM, delta −0.24, ~$647K paid on the
**ask** [FLOW:sweeps] on the *single most net-bearish day in 49 sessions*
(`self_pctile_net_dir 0.0` [CTX:self_pctile]) and a P/C z-score of **+3.83**
[HIST:pc_ratio_zscore]. That is not random. The defender leans on insider buying and
strong-buy ratings, but those are the *consensus that a clinical binary exists to be wrong
about* — analysts were strong-buy on every psychedelic name that later failed durability.
Phase-7 itself flags the **price-vs-flow DIVERGENCE** — "+33.4% but flow bearish"
[INSIGHT:price_vs_flow] — a documented *leading* reversal. And the macro tape just turned:
hawkish FOMC, dot to 3.8%, 10y 4.49% [MACRO:DGS10] is a duration headwind on a beta-2.53
[FUND:metric] parabola. The smart money is pre-positioning; the crowd is long and late.

## Strongest opposing point I cannot refute
The defender's hardest point is the **dealer structure**: FULLY_POSITIVE GEX, no
zero-gamma level, dealers *buying* dips [STRUCT:gex, STRUCT:dex], with the heaviest OI a
*call* wall at $13 [OI:oi_by_strike]. I cannot refute that *near-term* this mechanically
suppresses exactly the downside my put needs — the pin is real, and until OI builds below
spot the gamma does not flip. My thesis is a 2026-2027 durability/FDA bet wearing a today's-
flow costume; on a 1–4 week horizon the defender is probably right that nothing breaks, and
my put can bleed (even at low theta) while the pin holds and the uptrend grinds.

## Residual confidence
Residual confidence: 0.65

## Round 2

### Bull (defender) — round 2

The bear just conceded the whole near-term — "on a 1–4 week horizon the defender is
probably right that nothing breaks" — and that is the only horizon this skill sizes. Grant
the bear *everything* about H2 2026: durability is a real binary, and a LEAP put is the
right vehicle. That still is not a **short the desk can put on today**, because (a) phase-4
long-gamma + the $13 call wall [STRUCT:gex, OI:oi_by_strike] cap the move, (b) the bear has
*no edge on the binary's outcome* — both trials already hit primary endpoints
[MACRO:CMPS_catalyst], so the prior is success, not failure, and (c) the cost of being wrong
is brutal: beta 2.53 [FUND:metric] + strong-buy revisions + a $21.72 target mean a positive
durability print or an NDA-acceptance headline squeezes a short violently — and SI is only
5.69%, days-to-cover 1.80 [SENT:short_float fz], so there is no crowded-short fuel working
*for* me either; it just means the equity isn't pricing the bear. The honest synthesis is
NEUTRAL: don't short, don't chase the parabola long. If anyone trades it, it is the bear's
*own* instrument — defined-risk long-dated convexity — not a directional equity short.

## Strongest opposing point I cannot refute
Unchanged and unrefuted: **the put may be informed front-running of the COMP006 durability
readout** [MACRO:CMPS_catalyst]. I have argued the *prior* is success (two endpoints met),
but I cannot prove the 26-week durability holds, and I cannot prove the printer is not
someone with a better read on the discontinuation/relapse curve than the sell-side. If that
put is informed, "fade the bear" is the wrong side and my mild long-lean is exactly the
exit liquidity the bear wants. I down-weight my long-lean to *neutral* because of this.

## Residual confidence
Residual confidence: 0.75

### Bear (attacker) — round 2

I will not inflate. The defender is right that I have no edge on the binary's *outcome* and
that near-term the pin holds — so I cannot claim a tradeable short on this skill's 1–4 week
clock, and I won't pretend the +33% tape and insider buying aren't real headwinds to my
entry [HIST:trend, FUND:insider_MSPR]. My residual stays at 0.65, not higher: my thesis is
*correct as a risk*, not as a *trade-now*. The one thing I hold that the defender keeps
having to concede is that the smartest-dollar print on the tape this session was bearish and
deliberate, and it is aimed at a real H2-2026 event — so "neutral, watch it" is the ceiling
for the bull, not "fade." If the desk does anything, it owns the bear's convexity, not the
bull's dip.

## Strongest opposing point I cannot refute
The defender's "**the prior is success — both Phase-3 trials met their primary endpoints**"
[MACRO:CMPS_catalyst] is the point I cannot break. Primary-endpoint wins materially lower
the base rate of a durability/FDA disaster; my put is fighting a de-risked pipeline, not a
coin flip. Combined with the long-gamma pin, that means my downside thesis needs a *new*
negative catalyst that does not yet exist in the data — and inventing one would violate the
phase-data discipline. So my edge is convexity and asymmetry, not probability.

## Residual confidence
Residual confidence: 0.65

## Disconfirmation verdict

```
thesis_defender:  bull (NEUTRAL/fade — defends NOT-SHORT, mild long-lean down-weighted to neutral)
bull_residual:    0.75
bear_residual:    0.65
disconfirmed:     false        # bear_residual (0.65) < bull_residual (0.75)
strongest_bear_point: The session's largest, most deliberate print was an aggressive ask-side 582-DTE LEAP put — the rational vehicle to pre-position for the real COMP006 26-week durability binary in H2 2026 [MACRO:CMPS_catalyst, FLOW:sweeps], a risk no amount of current strong-buy consensus can rule out.
```

### How phase-9 should use this
- `disconfirmed = false` → **no extra size cut from the debate.** The fade/neutral thesis
  survived; but note the defender *voluntarily down-weighted its long-lean to neutral* in
  round 2 — phase-9 should read the surviving thesis as **NEUTRAL ("no directional trade"),
  not "fade-long."**
- Carry `strongest_bear_point` into phase-9 `key_risks` / invalidation: a P10-or-lower put
  **OI build on 6/19+**, or any negative durability/relapse signal before the H2-2026 readout,
  is the event that flips this from "watch" to "own the bear's convexity."
