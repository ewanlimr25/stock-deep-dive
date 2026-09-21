# Phase 8 — Multi-Agent Analyst Desk

**Ticker:** NTAP
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T00:00:00Z
**Upstream phases cited:** phase-1 through phase-7c (packed context to all 5 agents)

## Summary

Five specialist agents ran in parallel. **None is LONG** — the desk unanimously
rejects chasing the +12.4% rally into the print. Bias distribution: **2 NEUTRAL, 2
SHORT, 1 RANGE**; average conviction **3.0/5**. The consensus structure is
**defined-risk, vol-aware, half-size**, with a shared timing insight: *pre-earnings*
the long-gamma pin + IV rank 100 makes a naked fade expensive, so **the cleaner fade
is post-earnings** (vol crush + negative-vanna de-hedge + valuation air-pocket).
Levels converge tightly: **resistance 145** (gamma wall + overwrite strike),
**support 125 / 134**, then the **$119–124 shelf / ZGL $115.41**.

## Agent verdicts table

| Agent | bias | conviction | horizon | one_line_take |
|-------|------|-----------|---------|---------------|
| accumulation-hunter | **NEUTRAL** | 2 | 1-5d | "Base built at $119-124 last week, not today; today chased $139. Event-vol, no net OI — dealers hedging + crowding, not accumulation. Stand aside into earnings." |
| contrarian-scanner | **SHORT** | 3 | 1-4w | "Retail buying lotto calls into a print priced 18% above where every analyst says it belongs — fade the euphoria, size for the gap, play the post-earnings vol crush." |
| sweep-tracker | **RANGE** | 3 | 1-5d | "Momentum's gassed — sellers writing the 145 ceiling, dealers pinning it. Fade the chase, play 134–145, don't short strength outright." |
| earnings-scout | **SHORT** | 3 | 1-5d | "Sell the rich IV but defined-risk only — iron condor / short call spread around 125–145; priced for perfection above every target, cap the downside." |
| risk-monitor | **NEUTRAL** | 4 | 1-5d | "Event gap stacked on a valuation air-pocket — TRANSITIONAL regime + binary print = half-size max, defined-risk only, no naked short premium; do not chase long." |

## Per-agent details

### accumulation-hunter — NEUTRAL, conv 2, 1-5d
- support 134.00 · resistance 141.32 → 145C wall · invalidation: reclaim/hold >145 on
  rising net-call-buying + fresh OI build = LONG; close <134 with no DP defense = SHORT.
- **top_signal:** Phase-3 OI is STATIC despite a 31-session-high $10.84M premium day —
  `oi_biggest_increases` EMPTY, zero rolls, 145C OI fell 1,642→1,597 on 6,231 vol
  (pure overwrite) → **no net new institutional position built today**.
- **top_risk:** DP buy_ratio is contaminated by dealer call-hedging + price-chasing;
  a long here is fading distribution.

### contrarian-scanner — SHORT, conv 3, 1-4w
- support 124.00 (shelf/wall 125) · resistance 145.00 · invalidation: sustained close
  >145 on real call-buying, or a 5/28 beat that holds the AI narrative above the
  ±10.6% move.
- **top_signal:** Distribution-into-strength — spot $139.36 ABOVE every analyst target
  (avg $115–118, high $137, JPM Neutral $110) while cumulative flow is net BEARISH
  −$1.75M across 21/30 bearish-flow days during a 37% rally.
- **top_risk:** The genuine Google Cloud AI catalyst can gap NTAP through 145 before
  the vol crush lets the fade work. **Timing note: express post-print, not pre.**

### sweep-tracker — RANGE, conv 3, 1-5d
- support 134.00 · resistance 141.75 · invalidation: close >142 on expanding volume
  (momentum re-ignites) OR close <134 (pin fails).
- **top_signal:** Dealers LONG GAMMA, spot far above ZGL $115.41, and the **145 wall
  (+392K) is the exact strike being overwritten** ($2.86M 145C sold-on-bid) → 145 is
  a pinning cap into 5/28.
- **top_risk:** Bullish weekly sweeps (3/5, $5.08M) + DP chasing $134→$139 could carry
  through 145 on a beat before crush.

### earnings-scout — SHORT, conv 3, 1-5d
- support 125 (wall +488K) · resistance 145 (wall +392K) · invalidation: settle >145
  or <124.5 on the print (clean break of the implied range).
- **top_signal:** The largest print (145C 6/18 sold-on-bid $2.86M) into IV rank 100 /
  VRP +13.3 = **smart money harvesting rich premium, not chasing**.
- **top_risk:** 60% vol-realisation (N=10) + negative vanna (−817) means a real ±10.6%
  move materialises more often than not, and complacent skew leaves downside cheap/
  unprotected if the crowded long unwinds. **Structure: iron condor / short call
  spread, defined-risk.**

### risk-monitor — NEUTRAL, conv 4, 1-5d
- support 115.41 (ZGL / consensus-target cluster) · resistance 137.00 (highest target —
  already below spot) · invalidation: close >137 holding into print = fade invalid;
  close <115.41 = short-gamma vol-expansion downside confirmed.
- **top_signal:** Price $139.36 ABOVE all analyst targets, CROWDED_LONG with
  price_vs_flow DIVERGENCE=true and institutional distribution-into-strength.
- **top_risk:** Binary 5/28 (±10.6%/±$15) + IV rank 100; negative vanna → post-print
  crush = dealer de-hedge selling; a break of ZGL $115.41 flips dealers short-gamma
  into a vol-expansion air-pocket. **Half-size max, defined-risk, no naked short premium.**

## Disagreements

No agent took the **opposite** (LONG) bias — the disagreement is purely **expression/
timing**, not direction:
- **sweep-tracker (RANGE)** is the lone non-SHORT/non-NEUTRAL: it argues the
  long-gamma pin makes a *range* (134–145) the trade pre-print, vs the contrarian's
  *directional fade*. Its top_signal (145 overwrite + pin) is actually the mechanism
  the others rely on — a confirmation, not a true dissent.
- **accumulation-hunter & risk-monitor (NEUTRAL)** prefer *stand-aside/half-size*
  over the contrarian/earnings-scout *active short* — a risk-appetite difference. All
  agree: **no long, defined-risk, fade-leaning.**

## Tool errors

None. All 5 agents available; all returned valid verdicts with zero extra tool calls
(context was sufficient).

## Verdict for downstream

- **Plurality bias:** **NON-BULLISH / FADE-LEANING** — 2 NEUTRAL + 2 SHORT + 1 RANGE,
  **0 LONG**. Treating NEUTRAL+RANGE+SHORT as "do not be long," the desk is **5/5
  against a long**, with a 2-SHORT lean toward an active fade and a strong
  defined-risk/vol-selling consensus.
- **Average conviction:** **3.0/5** across all five (none MISSING).
- **Three highest-quality signals:**
  1. **OI static — no net build** despite a 31-session premium high; 145C OI *fell* on
     6,231 vol = overwrite [OI:biggest_increases]/[OI:decrease_with_volume] (accum-hunter).
  2. **Spot $139.36 above ALL analyst targets** (high $137, consensus $115–118) +
     price_vs_flow DIVERGENCE + distribution-into-strength [SENT:analyst_targets]/[INSIGHT:price_vs_flow] (contrarian/risk-monitor).
  3. **145C 6/18 sold-on-bid $2.86M into IV rank 100 / VRP +13.3** = premium harvest,
     not accumulation [FLOW:sweeps]/[HIST:vrp] (earnings-scout).
- **Open questions for phase-8b/9:**
  1. **Timing** — is the trade the *pre-earnings range/pin* (134–145) or the
     *post-earnings fade* (vol crush toward $115–125)? (sweep-tracker vs contrarian)
  2. Can a genuine **5/28 beat re-arm momentum through 145** before the crush — the
     gap risk that caps every agent's conviction at 3?
  3. **Structure & size** — iron condor vs short call spread vs stand-aside, at
     half-size, given the binary and IV rank 100?
