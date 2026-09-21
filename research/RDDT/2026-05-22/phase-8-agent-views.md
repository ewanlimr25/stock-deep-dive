# Phase 8 — Multi-Agent Analyst Desk

**Ticker:** RDDT
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T00:00:00Z
**Upstream phases cited:** phase-1 through phase-7c (packed into each agent)

## Summary

The desk **refuses to press a directional short** despite the bearish tape — the
defining outcome. Of four agents (earnings-scout skipped, earnings 7/30 > 30d out):
**1 LONG** (contrarian fade, conviction 3), **2 NEUTRAL** (accumulation-hunter
lean-long; sweep-tracker lean-short), **1 RANGE** (risk-monitor). **Zero clean
shorts.** Average conviction **2.25 (low)**. The consensus that emerges is a
**defined-risk RANGE / fade-the-extreme** posture, with a mild *long/fade-off-
support* tilt: buy/fade weakness near the 140–142 block-buy shelf, sell/fade strength
into 146–150, and respect the short-gamma break of 140 as the one real downside
accelerant (magnet toward $121). Every agent independently lands on **"do not size
up"** — TRANSITIONAL regime + fully short gamma + beta 2.15 + 14.65% short interest =
maximum whip. Correlation gate independently re-verified clean (RDDT uncorrelated to
the concurrent book).

## Agent verdicts table

| Agent | bias | conv | horizon | one_line_take |
|-------|------|------|---------|---------------|
| accumulation-hunter | NEUTRAL (lean LONG) | 2 | 1-5d | "Block buyers showed up at 141.70 but the broad tape is flat and the mega whale never printed — absorption, not a campaign; real support, not yet a bid." |
| contrarian-scanner | **LONG (fade)** | **3** | 1-5d | "Crowd's max-bearish on a one-day flip — 2.8σ P/C extreme, 30% bear win-rate, blocks buying the 141 dip, vanna coiled to squeeze. Fade it long off 140, dead below." |
| sweep-tracker | NEUTRAL (lean SHORT) | 2 | 1-5d | "The bullish 'campaign' was call writers cashing out, not buyers reloading — flow tilts down but no sweep urgency to chase the 140 break; fade rallies, don't press shorts." |
| risk-monitor | RANGE (lean short-of-range) | 2 | 1-5d | "Do not size up. TRANSITIONAL + short-gamma + 2.15 beta + 14.65% SI = max whip; half-size, defined-risk only. Correlation gate clean." |
| earnings-scout | MISSING (out of window) | — | — | earnings 2026-07-30 > 30d — skipped per phase rule |

## Per-agent details

### accumulation-hunter — NEUTRAL (lean LONG), conv 2, 1-5d
- key_levels: support 141.5–141.7 / resistance 146–147 then 150 / invalidation close <140 (loses gamma+DP floor, opens 120P air-pocket).
- top_signal: "Phase-2 block-tier buy_ratio 0.735 on $33.5M with the two largest blocks above NBBO mid into the close shows real dip-buying at 141–142."
- top_risk: "institutional_accumulation returns NEUTRAL (1.32), large tier 0.526, mega empty — the 'accumulation' is liquidity absorbing today's call-selling at the cross, not conviction; RDDT absent from any accumulation/confluence top-30."
- **Verdict nuance:** block dip-buying is *partly real but not standalone accumulation* — builds a credible 141.5–141.7 support shelf, not a long trigger.

### contrarian-scanner — LONG (fade), conv 3, 1-5d  ← highest conviction
- key_levels: support 140–142 (fade trigger) / resistance 146–147 then 150 / invalidation decisive close <140 (short-gamma accel + vanna flips to fuel, fade dead).
- top_signal: "Phase-5 P/C z +2.768 BEARISH_EXTREME (live-confirmed, 0.92 vs 0.47) atop a 30% bearish_flow win-rate and MIXED 90d flow (net −$5.8M of ~$800M) — crowd extreme-bearish on a single-day flip with no campaign behind it."
- top_risk: "Record short gamma (−$11.66M, DEX −$209M) means a clean break of 140 self-reinforces, and Meta-Forum could be genuine regime change not noise."
- **Verdict nuance:** 4 of 5 contrarian lenses align for a fade (P/C extreme, price-vs-flow, bull/bear disconnect, regime); "fade FROM support, not in the air."

### sweep-tracker — NEUTRAL (lean SHORT), conv 2, 1-5d
- key_levels: support 140–142 / resistance 146–147 then 150 / invalidation: reclaim+hold >147 on ask-side call sweeps voids distribution; clean break/hold <140 is the short trigger.
- top_signal: "The five largest 5/22 sweeps are bid-side call SALES across tenors (100C Sep $0.97M, LEAPs, 120C Jun) while RDDT is entirely absent from the sweep_ratio leaderboard — the '5/5 bullish' persistence tag is LEAP call-premium being monetized, not aggressive buying."
- top_risk: "Bearish replacement flow is small (~$7M net, no put-OI build, IV 18.7) = distribution not a sweep-backed short; SI 14.65% means any 147 reclaim squeezes violently."
- **Verdict nuance:** killed the "bullish campaign reasserting" thesis — it was call writers cashing out; today's flip is unwind/distribution, no urgency to chase down.

### risk-monitor — RANGE (lean short-of-range), conv 2, 1-5d
- key_levels: support 140–142 / resistance 146–147 then 150 / invalidation close <140 (accel toward 121) OR reclaim 150 (bull flip).
- top_signal: "Phase-4 FULLY SHORT GAMMA −$11.66M with beta 2.15 and Phase-5 GEX most-negative-in-window (prior prints drifted to $121) — dealers amplify any move, path violent both ways."
- top_risk: "14.65% SI + short-gamma + vanna +961 coil = a single up-catalyst (Forum) triggers a reflexive squeeze through 150 that whipsaws any short — directional sizing either way gets stopped on noise."
- **Fresh re-checks:** (1) correlation re-run — only PATH/SNOW 0.622, RDDT in no high pair → **gate clean, no size cut**; (2) regime TRANSITIONAL confirmed (half size); (3) **flagged Comm Services 5-day persistence as INFLOW 1.0 → downgraded the phase-6 single-day adverse-rotation warning to LOW** (see Disagreements).

## Disagreements

- **contrarian-scanner (LONG) vs sweep-tracker (lean SHORT):** both low conviction
  and they actually *converge on a RANGE* — fade weakness near 140, fade strength
  near 147–150. The disagreement is direction-of-lean within a range, not a genuine
  long-vs-short conflict.
- **risk-monitor vs phase-6 on sector rotation:** risk-monitor notes Comm Services
  `sector_flow_persistence` = INFLOW persistence 1.0 ($741M, 5/5), so it calls the
  phase-6 −$49.2M *net-directional* outflow a "one-day blip" and downgrades the
  warning. **Reconciliation:** the persistence tool measures *gross* premium activity
  (positive for every sector — non-directional), while phase-6's −$49.2M is the
  *net-directional* (bullish−bearish) read; they are not the same metric. The honest
  read: RDDT's sector is being net-*sold* directionally today but is not seeing a
  multi-day collapse in gross interest. Net: **mild adverse, not severe** — closer to
  risk-monitor's LOW than phase-6's headline. Phase-9 should treat sector rotation as
  a **soft** headwind.

## Tool errors

`MISSING: earnings-scout` — skipped, earnings 2026-07-30 is > 30 days out (phase rule).

## Verdict for downstream

- **Plurality bias:** **NEUTRAL / RANGE** (3 of 4 non-directional; 1 LONG-fade, 0
  clean SHORT). Directional lean = mild **fade/long off the 140–142 support shelf**,
  capped at 146–150. **No agent endorses a directional short** — strong corroboration
  of the phase-7b VETO.
- **Average conviction:** **2.25 / 5** (low — defined-risk, half-size mandate).
- **Three highest-quality signals across agents:**
  1. P/C z **+2.768 BEARISH_EXTREME** + 30% bearish_flow win-rate + MIXED 90d flow →
     crowd extreme-bearish on a one-day flip, no campaign [SENT/HIST] (contrarian).
  2. The 5 largest 5/22 sweeps are **bid-side call SALES** + RDDT absent from the
     sweep_ratio board → the "bullish campaign" was call-writing being monetized;
     today's bearish flip is distribution, not a sweep-backed short [FLOW] (sweep).
  3. **FULLY SHORT GAMMA −$11.66M + beta 2.15**, prior such prints drifted to $121 →
     dealers amplify; break of 140 self-reinforces down (the one real bear support)
     [STRUCT/HIST] (risk-monitor + accumulation).
- **Open questions surfaced by agents (for phase-8b debate):**
  - Is the Meta-Forum catalyst a **genuine regime change** (vindicating a small
    competitive short / break of 140) or **positioning noise into an oversold,
    squeezable, fundamentally-accelerating name** (favoring the fade)?
  - Does the short-gamma 140-break risk outweigh the contrarian-extreme + squeeze
    fuel that argue for a bounce? (The crux — RANGE resolves it either way at the
    boundaries.)
