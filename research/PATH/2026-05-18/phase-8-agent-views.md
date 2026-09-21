# Phase 8 — Multi-Agent Analyst Desk

**Ticker:** PATH
**As-of date:** 2026-05-18 (data: 2026-05-15)
**Generated:** 2026-05-18T02:00:00-04:00
**Upstream phases cited:** phase-1-flow.md → phase-7-insights.md (all 7 fed to each sub-agent)

## Summary

Five specialist sub-agents ran in parallel, each with the full
phase-1-through-7 packet. The desk is **split four ways**: 2 LONG / 1
SHORT (fade) / 1 RANGE (sell vol) / 1 NEUTRAL (lean long, defined-risk
only). Average conviction = **3.0/5**. Per the skill's interpretation
heuristics, a split this fractured maps to **MIXED → defined-risk
only, 0.55-0.65 sizing multiplier**. Critically, **4 of 5 agents
converge on three concrete operational rules**: (1) **NO naked long
calls into 2026-05-28**, (2) **the 2026-05-27 SNOW print is the
mandatory de-risk trigger**, and (3) **$9.40-$9.50 is the institutional
floor that defines downside invalidation**. The only outright LONG
takeaway with 4/5 conviction came from sweep-tracker, whose horizon is
1-4w but with explicit instruction to "ride the short-gamma fuse to
$11, exit before SNOW" — i.e. a tactical pre-earnings long, not a hold
through the event.

## Agent verdicts table

| Agent | Bias | Conviction | Horizon | One-line take |
|---|---|---|---|---|
| **accumulation-hunter** | LONG | **3** | 1-4w | "Institutions quietly built the floor at $9.40-$9.50 through the SaaSpocalypse selloff and are now front-running earnings — real accumulation, but it's catalyst ammo, not a stealth compounder." |
| **contrarian-scanner** | SHORT (fade) | **3** | 1-5d | "Everyone's long PATH calls into earnings while skew is inverted, IV's at 100th percentile, and every comparable bullish-flow signal lost 86% of the time over the past 20 days — that's not a thesis, that's a crowd." |
| **sweep-tracker** | LONG | **4** | 1-4w | "Five-day sweep stack into 2027 $12C plus 5,617-lot 0DTE+14 $11.5C urgency — ride the short-gamma fuse to $11, fade or roll before SNOW prints." |
| **earnings-scout** | RANGE (sell vol) | **3** | 1-4w | "IV is at the 100th percentile pricing a ~20% binary move into a crowded SaaS earnings night; sell the 5/29 vol via a short iron condor or 5/29-vs-6/18 call calendar at $12, not naked long calls." |
| **risk-monitor** | NEUTRAL (lean LONG defined-risk only) | **2** | 1-4w | "PATH-specific signal is real but you are buying a 100th-pct IV name into a SaaSpocalypse earnings stampede; half-size, defined-risk credit spreads or a call ratio that's short the 118% vega, never naked long calls." |

**Bias distribution:** LONG 2 / SHORT 1 / RANGE 1 / NEUTRAL 1
**Average conviction:** 15 / 5 = **3.0**

## Per-agent details

### accumulation-hunter [AGENT:accumulation-hunter]

VERDICT
- **bias:** LONG
- **conviction:** 3
- **horizon:** 1-4w
- **key_levels:**
    - support: $9.40
    - resistance: $10.71
    - invalidation: close below $9.40 on volume (breaks 5-day DP shelf) OR pre-earnings break of ZGL $7.53
- **top_signal:** phase-2 5-day price-level cluster $9.40-$9.50 = $22.81M / 2.40M sh / 80 trades, perfectly defended at the 2026-05-13 $9.46 low; confirmed by phase-5's 25 consecutive OI build days and phase-1's 5-of-5 sweep persistence ($7.77M cumulative).
- **top_risk:** Accumulation is real but tactical/event-driven — buyers are positioning for the 2026-05-28 binary, not stealth-compounding. A guide miss + vol crush + crowded inverted-skew calls = sharp give-back through $9.40.
- **one_line_take:** Institutions quietly built the floor at $9.40-$9.50 through the SaaSpocalypse selloff and are now front-running earnings — real accumulation, but it's catalyst ammo, not a stealth compounder.

### contrarian-scanner [AGENT:contrarian-scanner]

VERDICT
- **bias:** SHORT (fade the bullish crowd) — tactical pre-earnings fade, defined-risk only
- **conviction:** 3
- **horizon:** 1-5d (into 2026-05-28 earnings, exit before/at the event)
- **key_levels:**
    - support: $10.00 (round-number OI magnet) / $9.40-$9.50 (DP accumulation shelf — hard floor)
    - resistance: $10.65-$10.71 (phase-2 5-day shelf, $38.0M / 277 trades) / $11.00 (phase-4 GEX flip)
    - invalidation: sustained close above $10.71 on volume, OR SNOW print 2026-05-27 clean beat-and-raise
- **top_signal:** Phase-4 inverted skew (call 25Δ IV 97.6% > put 25Δ IV 89.6%, COMPLACENT) + phase-1 sweep persistence 5/5 ($7.77M) into phase-5's 14.3% market-wide bullish_flow win rate = textbook crowded one-way upside speculation right before the catalyst.
- **top_risk:** Phase-2 $9.40-$9.50 DP shelf is genuinely working, phase-4 net DEX +$2.16B forces mechanical dealer buying, and a Salesforce-Agentforce-style headline could squeeze the $13 +$627M GEX wall — fade gets run over on any beat-and-raise.
- **one_line_take:** Everyone's long PATH calls into earnings while skew is inverted, IV's at 100th percentile, and every comparable bullish-flow signal lost 86% of the time over the past 20 days — that's not a thesis, that's a crowd.
- **Preferred structure (vol-fade, not delta-short):** bear call spread $11.5/$13 on 2026-05-29 expiry, or 2026-05-29 / 2026-06-18 call calendar at $11 to harvest the 118%→96% IV crush.

### sweep-tracker [AGENT:sweep-tracker]

VERDICT
- **bias:** LONG
- **conviction:** 4
- **horizon:** 1-4w
- **key_levels:**
    - support: $10.00 (OI magnet) / $9.40-$9.50 (DP shelf)
    - resistance: $10.71 → $11.00 (GEX flip) → $13.00 (+$627M GEX wall)
    - invalidation: close below $9.40 DP floor, OR loss of bullish sweep persistence (drop out of top hot_chains_sweep_persistence ranking), OR SNOW 2026-05-27 print blowing up SaaS cohort
- **top_signal:** Phase 1 + Phase 5 — PATH logged sweep persistence 5-of-5 sessions bullish with $7.77M cumulative on a 25-consecutive-day OI build, and phase-4's negative-GEX zone $8-$10.5 means dealers must BUY underlying on any push toward $11 (net DEX +$2.16B).
- **top_risk:** Phase 5/6 — bullish_flow signal has 14.3% market-wide 20d win rate and tech sector saw -$151M outflow into a 100th-percentile IV print; a SNOW/OKTA miss on 2026-05-27 detonates the long-vega tail before PATH even reports.
- **one_line_take:** Five-day sweep stack into 2027 $12C plus 5,617-lot 0DTE+14 $11.5C urgency — ride the short-gamma fuse to $11, fade or roll before SNOW prints.

### earnings-scout [AGENT:earnings-scout]

VERDICT
- **bias:** RANGE (sell vol / fade the IV bulge)
- **conviction:** 3
- **horizon:** 1-4w (through 2026-05-29 expiry, post-earnings vol crush)
- **key_levels:**
    - support: $9.40-$9.50 (phase-2 5-day DP accumulation shelf)
    - resistance: $13.00 (phase-4 +$627M GEX + phase-3 2026-05-29 $13C 11,687 OI)
    - invalidation: close < $9.20 pre-earnings (breaks DP shelf + phase-7 30d low) OR > $11.10 on volume with IV still rising into 5/28 (real upside breakout — flip to long-delta call spread)
- **top_signal:** Phase 4 IV-term-structure kink — 2026-05-29 expiry IV 118.3% vs 75.8% at 5/22 and 96.3% at 6/18 — combined with phase-5 VRP +35.97 vol pts and IV30d 100th percentile makes the 19.8% implied move structurally rich vs PATH's last earnings realized path (+13.6% then full retrace).
- **top_risk:** Asymmetric upside surprise on agentic ARR re-rating: phase-4 negative-GEX cluster + net DEX +$2.16B means a beat triggers dealer-buy fuel from $10.30 → $11 (short-gamma amplification) before the $13 wall caps it — a short-vol structure that's also short upside delta gets run over.
- **one_line_take:** IV is at the 100th percentile pricing a ~20% binary move into a crowded SaaS earnings night; sell the 5/29 vol via a short iron condor or 5/29-vs-6/18 call calendar at $12, not naked long calls.
- **Preferred structure:** **Double calendar / call diagonal short the 2026-05-29 $12C and long the 2026-06-18 $12C** — harvests the 22-pt IV differential, defined-risk, vega-neutralish, small positive delta. Hard exit before SNOW 2026-05-27 AMC.

### risk-monitor [AGENT:risk-monitor]

VERDICT
- **bias:** NEUTRAL (lean LONG via defined-risk structures only; do NOT carry naked long delta through 2026-05-28 earnings)
- **conviction:** 2
- **horizon:** 1-4w (event-defined; trim or exit before 2026-05-27 SNOW AMC)
- **key_levels:**
    - support: $9.40-$9.50 (phase-2 DP shelf) / $10.00 (round-number magnet)
    - resistance: $10.65-$10.71 (phase-2 battle zone) / $11 (GEX flip) / hard wall $13
    - invalidation: close below $9.40 on volume = accumulation shelf broken, opens $8 floor; OR ZGL break below $7.53 = catastrophic dealer regime flip
- **top_signal:** phase-7 `insights_price_vs_flow` DIVERGENCE — price -4.06% / net flow +$1.13M bullish off the $9.46 low into the phase-2 $9.40-$9.50 DP shelf — the only UW composite tool giving a clean bullish read.
- **top_risk:** 2026-05-28 earnings is a guaranteed vol-crush event (IV 118% → 60-70%) into a TRANSITIONAL regime where bullish_flow signal wins only 14.3% of the time and the entire SaaS cohort reports the same week with no broadly bullish positioning — correlated cohort blowup risk is the dominant scenario.
- **one_line_take:** PATH-specific signal is real but you are buying a 100th-pct IV name into a SaaSpocalypse earnings stampede; half-size, defined-risk credit spreads or a call ratio that's short the 118% vega, never naked long calls.

**Risk-monitor's explicit kill switches (mandatory for phase 9):**
- SPY breadth drops below 30% bullish
- SNOW 2026-05-27 AMC reaction down >5%
- PATH closes below $9.40
- ZGL breaks below $7.53

**Sizing prescription:** 0.30-0.50× normal. Max single-name PATH risk
1.0-1.5% of book. **Mandatory exit decision BEFORE 2026-05-27 SNOW
AMC.**

## Disagreements

The 5-agent desk is split four ways. Each dissent is worth surfacing:

1. **Contrarian (SHORT 3/5) vs Sweep-tracker (LONG 4/5)** — the
   strongest opposition. Both cite the same phase-1 sweep persistence
   datapoint. Contrarian reads "5-of-5 = overcrowded one-way bet,"
   sweep-tracker reads "5-of-5 = unusually persistent = real conviction
   building." **Resolution:** The historical signal_backtest
   (14.3% win rate) supports the contrarian interpretation for cohort
   trades; the GEX/DEX dealer-flow mechanics support the sweep-tracker
   interpretation for PATH specifically. **Both can be partially right —
   PATH can run to $11 short-term then give back into earnings.** This is
   why earnings-scout's RANGE-and-sell-vol structure is the most
   informationally efficient: it works in both scenarios.

2. **Risk-monitor NEUTRAL 2/5 (lean long) vs Sweep-tracker LONG 4/5** —
   gap of 2 conviction points. Risk-monitor weights the macro/cohort
   correlation more heavily; sweep-tracker weights the ticker-specific
   sweep mechanics more heavily. **Resolution:** Both agree the trade
   must be SHORT-DURATION and exit before SNOW — they just describe the
   same trade with different baseline conviction.

3. **Earnings-scout RANGE vs accumulation-hunter LONG** — actually
   compatible: both endorse holding directional exposure (long delta)
   BUT earnings-scout's structure (call diagonal) achieves long-delta
   via short the front-month 118% IV + long the back-month 96% IV.
   Same direction, different vega.

## Tool errors

(no MISSING agents — all 5 agent types ran successfully)

## Verdict for downstream phases

- **Plurality bias:** Of the 5 agents, **4 are net-bullish-leaning** in
  some form (LONG, LONG, RANGE-with-positive-delta, NEUTRAL-leans-long)
  and **1 is short (contrarian fade)**. So a fair label is **DEFINED-RISK
  LONG WITH VOL-FADE OVERLAY**, NOT outright bullish.
- **Average conviction:** **3.0** — per the skill heuristic, "Split 3-2:
  target 0.55-0.65 conviction; defined-risk structure." Phase 9 should
  size at this level.
- **Three highest-quality signals across the desk (agreed by ≥3 agents
  each):**
  1. **Phase 1 sweep persistence 5/5 sessions, $7.77M cumulative bullish
     [AGENT:accumulation-hunter][AGENT:sweep-tracker][AGENT:contrarian-scanner]**
     — the same datapoint is the BULL setup for two agents and the
     CROWDING risk for one. Strongest single-signal cross-coverage.
  2. **Phase 4 inverted skew + IV 100th pct + VRP +35.97 vol pts =
     PREMIUM_SELLING regime
     [AGENT:contrarian-scanner][AGENT:earnings-scout][AGENT:risk-monitor]**
     — three agents converge on "long vol is the worst trade here."
  3. **Phase 5 bullish_flow signal market-wide 14.3% win rate +
     phase-7 SaaS earnings cohort 2026-05-27/28
     [AGENT:contrarian-scanner][AGENT:earnings-scout][AGENT:risk-monitor][AGENT:sweep-tracker]**
     — four agents flag the cohort/regime risk as the dominant scenario.
- **Open questions surfaced by agents (for phase 9 to resolve or
  acknowledge):**
  - Will SNOW 2026-05-27 AMC blow up the SaaS cohort? **Unanswerable in
    advance — the only mitigation is the mandatory pre-SNOW de-risk
    rule.**
  - Will PATH agentic ARR ($200M run-rate) get re-rated as a
    Salesforce-Agentforce ($800M ARR) winner on the print? Bimodal.
    **Phase 9 cannot bet on this binary — structure must work in both
    legs.**
  - What is PATH's average historical post-earnings 1-day realized
    move? **Implied 19.8% vs prior FQ4's 13.6% first-day move suggests
    vol is rich. Earnings-scout's call diagonal sells this richness.**
- **Mandatory rules for phase 9 (derived from agent consensus):**
  - **NO naked long calls into 2026-05-28** (5/5 agents agree)
  - **Mandatory de-risk decision before SNOW 2026-05-27 AMC** (4/5 agents)
  - **Hard invalidation: close below $9.40** (5/5 agents)
  - **Sizing: 0.30-0.50× normal** (risk-monitor + macro phase-6)
  - **Defined-risk only** (5/5 agents + macro TRANSITIONAL guidance)
