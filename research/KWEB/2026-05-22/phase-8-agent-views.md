# Phase 8 — Multi-Agent Analyst Desk

**Ticker:** KWEB
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T00:00:00Z
**Upstream phases cited:** phase-1 through phase-7c (full packed context)

## Summary

Five specialists, **zero clean directional longs**. Bias splits **3 NEUTRAL / 2
RANGE**, and the *leans* cluster bearish/non-directional: two lean SHORT/fade-into-$28
(contrarian, risk-monitor), one long-vol/short-delta (earnings-scout), one
neutral-distribution (accumulation-hunter), and only one conditional LONG — and only
on a >$27.95 reclaim (sweep-tracker). **Average conviction 2.6/5.** The desk
consensus: this is **not a directional long** — the lit bullish flow is unconfirmed
(or contradicted) by the share tape, so size small / defined-risk only. The single
most actionable original insight (earnings-scout): **IV is mispriced cheap into four
China mega-cap prints** (front-end FLAT 1.037, 06-18 OPEX IV 36% ≤ back-end, IV 3.33
pctile, realized 33.8% > implied 29.8%) → **own the move, not the direction**, with a
put-lean given distribution + downtrend.

## Agent verdicts table

| Agent | bias | conviction | horizon | one_line_take |
|-------|------|-----------|---------|---------------|
| accumulation-hunter | NEUTRAL (lean RANGE) | 2 | 1-4w | No accumulation — big blocks SELLING into the low while lit buyers chase OTM upside; distribution wearing a bullish mask. |
| contrarian-scanner | RANGE (lean SHORT into $28) | 3 | 1-4w | Dip-buyers paying up for 30-strike fantasies desks are writing; fade lottery tickets, sell rallies into $28. |
| sweep-tracker | NEUTRAL (lean LONG on reclaim) | 2 | 1-5d | Sweeps too conflicted; stand aside until $27.95 reclaims or $26.36 breaks. |
| earnings-scout | RANGE (long vol/convexity, short-delta lean) | 3 | 1-4w | Vol on the clearance rack into 4 China prints that keep cratering — buy the move, not the direction. |
| risk-monitor | NEUTRAL (lean SHORT/avoid-long) | 3 | 1-4w | Half-size or smaller, defined-risk only; short-gamma name with Taiwan tail under a rising USD; long lit-flow fights the tape. |

## Per-agent details

### accumulation-hunter — NEUTRAL/RANGE, conv 2, 1-4w
- support 26.88-26.95; resistance 27.95-28.10 (then 29-31 cap); invalidation: bull dead <26.36 on block-confirmed sell; range dead >28.10 on volume.
- top_signal: Phase-2 NET DISTRIBUTION at block level — mega $13.8M/514k buy_ratio 0.0, block 0.306 — opposite of accumulation.
- top_risk: bullish tape is upside calls (30-31, +12-15% OTM) being WRITTEN/capped (phase-3/4), so a bounce stalls into a wall while shares bleed.

### contrarian-scanner — RANGE (lean SHORT), conv 3, 1-4w
- support 26.41; resistance 28.00; invalidation: sustained close >29 on rising volume (fade is wrong → vanna-squeeze to 30-31).
- top_signal: Phase-3 the lit "bullish" 30-31 calls are being WRITTEN/CLOSED (Jun 31C OI −13,668, 30.5C −9,730 on 16k vol) while DP distributes and DEX −$334M — crowd buying lottery calls into supply.
- top_risk: a genuine China-earnings beat + fragile tariff tailwind could ignite the cheap-IV vanna-squeeze the bears are funding, forcing a breakout >29.

### sweep-tracker — NEUTRAL (lean LONG on reclaim), conv 2, 1-5d
- support 26.88 (loss → 26.36); resistance 27.95 (then 28.50 flip); invalidation: sustained close <26.36, or a fresh BID-side call sweep wave.
- top_signal: today's largest print is Jul 31P SOLD on the bid ($2.08M) stacked on ask-side 30-31 call sweeps → aggressive premium net-points modestly LONG **despite** the bearish persistence label (which is polluted by put-bid + deep-ITM-put-ask tallies).
- top_risk: DP distribution + normal volume = no momentum fuel; the "bearish $21M" persistence may be reading real put hedging the calls can't overpower.

### earnings-scout — RANGE (long vol/convexity, short-delta lean), conv 3, 1-4w
- support 26.88-26.95 (below → air to 25); resistance 27.95-28.10 (cap 29-31); invalidation: front-end IV inverts to BACKWARDATION (>1.05) → cheap-vol edge gone; OR sustained close >29 (flips to long).
- top_signal: 06-18 OPEX IV (36.0%) ≤ back-end LEAPS, front-end ratio FLAT 1.037, IV 3.33 pctile, realized 33.8% > implied 29.8% (VRP −0.04) → **~zero event premium priced into 4 mega-cap prints = mispriced cheap convexity**.
- top_risk: the call-skewed net +$2.65M could front-run a stimulus/summit pop, squeezing dealer short-gamma >28.5-29 and turning a put-leaning long-vol structure into a loser before earnings print.

### risk-monitor — NEUTRAL (lean SHORT/avoid-long), conv 3, 1-4w
- support 26.88-26.95 then ~25; resistance 27.95-28.10; invalidation: reclaim/hold >29 (flips bear thesis) OR clean <26.88 on volume (short-gamma flush).
- top_signal: Phase-4 SHORT-gamma at spot (27 = −$41.5M GEX), DEX −$334M overhang, GEX collapsed 672M→39M → moves trend/amplify, no pin.
- top_risk: Phase-6 Taiwan-warning gap risk + firm/rising USD (119.3) on a short-gamma structure = a single China-policy headline can gap it down with no dealer pin to absorb.

## Disagreements

- **sweep-tracker is the lone (conditional) bull**, reading the aggressive lit tape
  as net-long (Jul 31P *sold*, 30-31 calls bought) and the bearish 5-day
  `sweep_persistence` as a **tally artifact** (put-bid + deep-ITM-put-ask
  mislabeled bearish). This directly addresses phase-1's open conflict — the *lit
  aggression* points modestly up, but it is **conditional on a $27.95 reclaim** and
  it concedes there's no volume fuel. The other four weight the **share tape**
  (distribution, outflows, downtrend) over the lit options skew.
- earnings-scout reframes the whole trade as **vol, not direction** — the only agent
  to surface the cheap-convexity-into-catalyst edge, which both bull and bear leans
  can sit inside (long gamma, lean short delta).

## Tool errors

None. All five agents available and returned. (Several re-queried the local
parquet/OI tools to confirm — e.g. contrarian verified the 30-31 call OI *decreases*;
sweep-tracker confirmed KWEB absent from `volume_vs_average`.)

## Verdict for downstream

- **Plurality bias:** **NEUTRAL/RANGE (5 of 5 non-directional)** — leans tilt
  bearish/fade (2 short, 1 long-vol-short-delta, 1 neutral-distribution, 1
  conditional-long). **No agent endorses an outright directional long.**
- **Average conviction:** **2.6/5** (2, 3, 2, 3, 3).
- **Three highest-quality signals:**
  1. **Mispriced cheap convexity into the China earnings cluster** — front-end FLAT
     1.037, 06-18 OPEX IV 36% ≤ back-end, IV 3.33 pctile, realized 33.8% > implied
     29.8% `[STRUCT:front_end_iv_ratio]` `[HIST:vrp]` (earnings-scout).
  2. **Lit bullish flow is unconfirmed/exit liquidity** — DP block distribution
     (mega 0.0 / block 0.306) + the 30-31 calls being WRITTEN/CLOSED (Jun 31C OI
     −13,668) `[DP:block_stratified]` `[OI:decrease_with_volume]` (accumulation-hunter,
     contrarian).
  3. **Short-gamma trend-amplification + tail risk** — 27 = −$41.5M GEX, DEX −$334M,
     GEX collapsed 672M→39M, Taiwan/USD gap risk `[STRUCT:gex]` `[STRUCT:dex]`
     `[MACRO:DTWEXBGS]` (risk-monitor).
- **Open questions for phase-8b debate / phase-9:**
  1. Does the **cheap-IV vanna-squeeze fire** (summit/stimulus/earnings beat → close
     >28.5-29 → dealer flip → 30-31), or does **short-gamma + distribution + Taiwan
     flush it to 25**? This is the central bull/bear axis for the debate.
  2. Is the right expression **long convexity (strangle/backspread, put-lean)** that
     monetizes the cheap vol regardless of direction, vs a directional debit vertical?
