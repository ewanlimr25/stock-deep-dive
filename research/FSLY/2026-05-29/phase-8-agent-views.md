# Phase 8 — Multi-Agent Analyst Desk

## Summary

Five specialist desk agents ran in parallel on the packed phases 1–7c context. The
net is **low-conviction and three-way-split, but uniformly non-bearish: 2 LONG / 2
NEUTRAL / 1 RANGE, zero SHORT, average conviction 2.0 / 5** — the lowest-conviction
desk the skill can return without an outright pass. Every agent independently reached
the **same one-line diagnosis: "armed but not triggered."** The bullish OI ladder +
cheap-vs-realized vol + mild accumulation are real; the absence of a volume/sweep
ignition + dampening positive gamma + low days-to-cover mean nothing has fired.

**Unanimous geometry (all five agents agree):**
- **Support $17.5** (gamma node + 6/18 max-pain + dark-pool shelf $17.49–$17.58).
- **Hard floor / invalidation: close below $16** (gamma flips negative −$1.6M node →
  downside accelerant; first OI put wall). **Every agent named $16 as the line.**
- **Resistance $20** (call wall, +12.9%) → **$22.5** (+27%).
- **The ignition trigger:** an aggressive-sweep + volume break through ~$18.5–$19
  flips the stand-aside agents LONG; until then, positive gamma pins $17.5.

**Desk verdict: small, defined-risk, cheap-optionality LONG — or wait for the volume
trigger.** Three agents (accumulation-hunter, earnings-scout, plus risk-monitor's
"defined-risk call spread at half-size") converge on **buy cheap upside convexity,
size small, stop on a $16 close**; two (sweep-tracker, contrarian) say **stand aside
until ignition**. No agent sees downside edge — the disagreement is LONG-now-small vs
WAIT, not LONG vs SHORT.

## Agent verdicts table

| Agent | bias | conv | horizon | one_line_take |
|-------|------|------|---------|---------------|
| accumulation-hunter | **LONG** | 2 | 1-4w | Genuine quiet accumulation (accelerating call-led OI build + inst adding) but a loaded gun with no finger on the trigger; buy cheap defined-risk upside, size small, wait for ignition. |
| contrarian-scanner | RANGE | 2 | 1-4w | No crowd to fade — pulled-back, Hold-heavy, P/C normal; a gamma-pinned $17.5 range with a $16 trapdoor and a $20 squeeze cap. |
| sweep-tracker | NEUTRAL | 2 | 1-4w | No sweeps, no ignition, dealers long gamma — armed but nobody's pulling the trigger; stand aside until aggressive flow and volume fire. |
| earnings-scout | **LONG** | 2 | 1-3m | Turnaround drift real but not kinetic — buy cheap-vs-realized convexity small (defined-risk 20/22.5 call spread, July), pre-positioning not catalyst. |
| risk-monitor | NEUTRAL | 2 | 1-4w | Correlation gate clean (idiosyncratic, beta 0.37, diversifier); only risk is the position itself — defined-risk call spread at half-size, hard stop on a $16 close. |

- **Tally:** LONG 2, NEUTRAL 2, RANGE 1, SHORT 0. Avg conviction **2.0**.

## Per-agent details

### accumulation-hunter — LONG, conv 2, 1-4w
- support $17.49 · resistance $20 → $22.5 · invalidation: close below $16.
- top_signal: accumulation is real and *accelerating* — 4 consecutive OI-build days
  ramping net +3,417 (5/28) → +6,062 (5/29), 138-up/37-down, entirely call-led
  (20C/30C 7/17), under choppy price = textbook quiet positioning; reinforced by Inst
  Trans +17.5% and DP large-tier buy_ratio 0.85.
- top_risk: armed not triggered — zero sweeps + positive gamma pinning $17.5 + 1.74
  days-to-cover (weak reflexivity); FSLY absent from top-200 DP names → accumulation
  is genuine but **sub-scale**.

### contrarian-scanner — RANGE, conv 2, 1-4w
- support $17.5 / hard floor $16 · resistance $20 → $22.5 · invalidation: close < $16
  (down) OR volume-sweep break > $18.5 (squeeze ignites — exit range, don't fade).
- top_signal: crowd_state BALANCED — RSI 42.3, −11.9%/−26.7% vs 20/50-SMA, analysts
  8-Hold/1-Sell, P/C z −0.76 NORMAL → **no sentiment extreme to fade either way**.
- top_risk: 14.6% SI + 20/22.5/25 call ladder is armed fuel — a single ignition flips
  range → breakout, blowing up any short-the-rally fade.
- Note: deliberately fails the contrarian bar (<3 fade signals align); only
  tradeable contrarian-adjacent read is mean-reversion *within* the $16–$20 range.

### sweep-tracker — NEUTRAL, conv 2, 1-4w
- support $17.5 / $16 · resistance $20 → $22.5 · invalidation: validates LONG only on
  an aggressive-sweep + volume ignition through $18.5–$19; thesis fails on close < $16.
- top_signal: ZERO sweeps on a +4.9% day, largest trade a $79k '28 LEAP on the mid;
  confirmed live — FSLY absent from the entire sweep-ratio scanner (owned by
  RIOT/NVDA/AXTI/AFRM). No momentum footprint.
- top_risk: the squeeze ignites without us — but positive GEX + 1.74 DTC make a
  dampened pin the more likely near-term path, so chasing pre-ignition bleeds high IV.

### earnings-scout — LONG, conv 2, 1-3m
- support $17.49 · resistance $20 → $22.5 · invalidation: close below $16.
- top_signal: VRP −0.566 (PREMIUM_BUYING, RV 144% >> IV 88%) + all-call fresh OI
  laddered 20/22.5/25 over 14.6% SI = cheap-vs-realized optionality on an armed
  squeeze with a 4/4 accelerating beat trajectory re-rating into the 8/05 print.
- top_risk: no near catalyst (earnings >2mo, no isolable event-vol expiry — 7/17→9/18
  gap, no kink), positive gamma pins $17.5, low DTC caps reflexivity → bleeds/chops
  without an external volume ignition.

### risk-monitor — NEUTRAL, conv 2, 1-4w
- support $17.5 / $16 · resistance $20 → $22.5 · invalidation: close below $16.
- top_signal: OI structurally call-skewed into a $20/$22.5/$25 ladder over 14.6% SI
  (P/C OI 0.53, all fresh OI calls) + VRP −0.566 makes the upside optionality
  cheap-vs-realized.
- top_risk: armed-but-unignited squeeze on an **unprofitable** small-cap (op margin
  −16%, no earnings floor), positive gamma pins $17.5, $16 trapdoor — if the catalyst
  never fires, you bleed high IV on a ±5–8% whipsaw name.
- **Risk overlay (carry to phase-9):** correlation gate **CLEAN** — idiosyncratic,
  beta 0.37, *negatively* correlated to DDOG (a diversifier, no cluster to stack).
  Only risk is the position itself → **defined-risk call spread at half-size, hard
  stop on a $16 close, no naked premium.**

## Disagreements

- **No directional dissent** (0 short, 0 high-conviction). The split is **LONG-small
  vs WAIT**, not a bias conflict: accumulation-hunter + earnings-scout + risk-monitor
  endorse a *small defined-risk long structure now*; sweep-tracker + contrarian say
  *stand aside until the volume/sweep ignition*. Both camps agree on the structure
  (defined-risk call spread), the levels ($17.5 / $16 / $20-22.5), and that **size
  must be small**. This is a uniform conviction-2 read → MIXED-constructive; phase-9
  targets the **floor of the band (0.55–0.65)** with a defined-risk structure.

## Tool errors

- None. All five agent types available and returned (the sanctioned parallel batch).
  Agents used ~58 uw calls total (mostly confirmations: sweeps empty, sweep-ratio
  scanner excludes FSLY, FSLY absent from top-200 DP names, no isolable 8/05 expiry).

## Verdict for downstream

- **Plurality bias: LONG/NEUTRAL tie (2 LONG / 2 NEUTRAL / 1 RANGE; 0 short).** Read
  as **tactical LONG-small or WAIT** — the constructive structure is real but
  un-triggered. Avg conviction **2.0** (lowest non-pass).
- **Three highest-quality signals across the desk:**
  1. `[AGENT:earnings-scout]` VRP −0.566 (RV 144% >> IV 88%) makes the upside
     optionality cheap-vs-realized — buy convexity, don't overpay. `[HIST:vrp]`
  2. `[AGENT:accumulation-hunter]` 4 consecutive OI-build days, accelerating to +6,062
     (138-up/37-down), all call-led — quiet positioning under choppy price. `[HIST:oi-trend]`
  3. `[AGENT:sweep-tracker]` ZERO sweeps, FSLY absent from sweep-ratio scanner — the
     squeeze is armed but **un-ignited**; no momentum to chase. `[FLOW:sweeps]`
- **Open questions for phase-8b debate:**
  - Is "buy cheap optionality now" worth the IV bleed, or does "wait for the $18.5–$19
    volume ignition" dominate given no near catalyst (earnings >2mo)?
  - Does the sub-scale accumulation (FSLY absent from top-200 DP names) + low
    days-to-cover (1.74) mean the squeeze fuel is too weak to rely on?
  - Defined-risk call spread (20/22.5 July) vs stand-aside — what's the honest
    reward:risk on a gamma-pinned name with a $16 trapdoor?

## Upstream references

- phase-7-insights.md §Summary — engine MIXED (4.7%); the desk concurs (avg conv 2.0,
  no directional edge) — the structure leans bullish but nothing has triggered.
- phase-4-structure.md / phase-1-flow.md — the "armed but not triggered" framing every
  agent independently reached is the explicit subject of phase-8b.

## Next phase

- phase-8b-debate.md (bull vs bear disconfirmation — adjudicate "buy small optionality
  now" vs "wait for ignition" before the PM synthesis)
