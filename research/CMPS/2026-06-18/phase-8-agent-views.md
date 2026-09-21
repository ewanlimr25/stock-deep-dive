# Phase 8 — Multi-Agent Analyst Desk

**Ticker:** CMPS
**As-of date:** 2026-06-18
**Generated:** 2026-06-20
**Upstream phases cited:** phase-1 through phase-7c (all packed into each agent)

## Summary

Four specialist agents ran in parallel (earnings-scout skipped — earnings 2026-07-30
is 42d out, beyond the 30d window). **Plurality NEUTRAL (3 of 4)**; the contrarian-
scanner returned **RANGE with a fade-the-bear lean**. **No agent took SHORT and none
took LONG** — the desk unanimously declines to trade the bearish LEAP put as a
directional short, and equally declines a fresh long into a parabolic name in a
half-size regime. Average conviction **2.25 / 5** (low). The consensus structure:
watch-only or defined-risk convexity at most, with a clear invalidation — a P10 LEAP
put **OI build on 6/19+** would resurrect the short; a close **above $13** kills it.

## Agent verdicts table

| Agent | bias | conviction | horizon | one_line_take |
|-------|------|-----------|---------|---------------|
| accumulation-hunter | NEUTRAL | 2 | 1-4w | No accumulation fingerprint — DP thin & net-sell, detector NEUTRAL, only fresh print is a bearish hedge; nothing to chase. |
| contrarian-scanner | RANGE | 3 | 1-4w | One lonely LEAP put screaming bear into a +33% tape & strong-buy analysts — a crowd of one; fade the panic, respect the pin. |
| sweep-tracker | NEUTRAL | 2 | 1-5d | One stale LEAP put, zero persistence, no bid-side urgency — deep-OTM long-dated convexity is not a short signal. |
| risk-monitor | NEUTRAL | 2 | 1-4w | No clean edge + hard short-veto stack (7b VETO + 7c CAUTION); half-size regime → watch-only or defined-risk convexity, never a fresh short. |
| earnings-scout | — | — | — | **SKIPPED** — earnings 2026-07-30 (42d out) > 30d window. |

## Per-agent details

### accumulation-hunter — NEUTRAL (2), 1-4w
- key_levels: support 11.84–11.90 / 11.54 / 12.10 (DP magnet ≈ spot); resistance 13.00;
  invalidation: a settled OI build at $12–13 calls or a ≥mega-tier DP buy through $13 on
  >2× vol = pre-breakout accumulation read; a P10 LEAP put OI build below $12 = distribution.
- top_signal: the detector itself is the tell — phase-7 institutional-accumulation = NEUTRAL
  (buy/sell 1.19) and phase-2 large DP tier 60% SELL on 0.32% of float with biggest-OI-
  increases EMPTY → 3 of 4 accumulation signals fail; only the lone 100K block buy leans accumulation.
- top_risk: the constructive backdrop (4-day call-OI build +61,955, +33% trend, MSPR +100,
  strong-buy revisions) means a real stealth campaign could begin 6/19+ and be caught a session late.

### contrarian-scanner — RANGE (3), 1-4w  *(lone non-NEUTRAL)*
- key_levels: support 11.84–11.90 / 11.54; resistance 13.00; invalidation: P10 LEAP put OI
  BUILDS 6/19+ (campaign) OR daily close < $11.54 (gamma flips) — either kills the fade.
- top_signal: phase-5 P/C z-score **+3.83 = BEARISH_EXTREME** (today 1.36 vs 20-day mean
  0.243) on a normally call-heavy name + the entire skew is ONE brand-new Jan-2028 $10 LEAP
  put (~$647K), absent from confluence both sides → the classic crowded/late single-factor
  trade to fade.
- top_risk: the +3.8σ put could be a smart-money **front-run of the COMP006 26-week durability
  binary (H2 2026)** — a real catalyst the divergence is leading, in which case fading early is wrong.

### sweep-tracker — NEUTRAL (2), 1-5d
- key_levels: support 11.84–11.90 / 11.54; resistance 13.00; invalidation: bearish-actionable
  only if P10/lower-strike put OI settles & BUILDS 6/19+ AND GEX flips negative; flips against
  any short on a close above 13.00.
- top_signal: the only aggressive sweep was ONE ask-side Jan-2028 $10 LEAP put (~$667,944,
  delta −0.24, 582 DTE, vol/OI 13.97), sweep-persistence consistency 0.2 / sessions_in_top 1,
  no smart-money rows — an isolated one-day event, not a momentum campaign.
- top_risk: the lone print is a deep-OTM 582-DTE LEAP most consistent with a tail hedge /
  durability convexity, fighting long-gamma pinning + a +33% uptrend → no near-term follow-through.

### risk-monitor — NEUTRAL (2), 1-4w
- key_levels: support 11.84–11.90 / 11.54 / 10.00 (LEAP put strike, −20%); resistance 13.00 /
  15.00; invalidation: P10 put OI builds materially 6/19+ OR daily close < 11.54 on rising put
  OI flips GEX negative → resurrects the short.
- top_signal: macro is genuinely two-sided — FOMC 6/17 hawkish dot to 3.8% + 10y 4.49% is a real
  duration headwind aligned with the bear, but Healthcare is a persistent sector INFLOW (+$219.6M,
  persistence 0.8) adverse to a short; the two roughly cancel.
- top_risk: beta 2.53 on a parabolic +81.6%-YTD name into the COMP006 durability binary + NDA Q4
  means a single adverse readout produces an outsized idiosyncratic drawdown no index hedge protects.
- desk notes: NO correlation cluster (CMPS/MARA/PATH unrelated, high_correlations null; broken-
  sector warning disregarded); NO high-confluence setup (CMPS absent both confluence lists);
  regime caps any expression at half-size, defined-risk.

## Disagreements

- **contrarian-scanner (RANGE/fade-the-bear)** is the only non-NEUTRAL, but it is **not opposite**
  the majority — a fade of the bear aligns with the desk's unanimous "this is not a short." Its
  added nuance is the standout caveat: the +3.8σ P/C extreme *could* be a smart-money front-run
  of the H2-2026 durability binary rather than a fade-able outlier. **No agent is bearish; no true
  dissent.**

## Tool errors

- `MISSING/SKIPPED: earnings-scout` — earnings 2026-07-30 is 42d out (> 30d window), per phase
  rule. The relevant binary (COMP006 durability, H2 2026) is captured by contrarian-scanner and
  risk-monitor.

## Verdict for downstream

- **Plurality bias:** **NEUTRAL (3 of 4)**; contrarian-scanner RANGE/fade-the-bear. **0 LONG,
  0 SHORT.** Net desk read: **MIXED/NEUTRAL — not a tradeable directional short; a possible
  shallow fade of the bear, capped by regime.**
- **Average conviction (non-skipped):** **2.25 / 5** (low).
- **Three highest-quality signals across agents:**
  1. P/C z-score **+3.83 BEARISH_EXTREME** on a normally call-heavy name — contrarian fade
     trigger [SENT/HIST:pc_ratio_zscore] (contrarian-scanner).
  2. Only aggressive sweep = ONE Jan-2028 P10 LEAP put, **consistency 0.2, 1 session** — event,
     not campaign [FLOW:sweep_persistence] (sweep-tracker).
  3. Macro two-sided & cancelling: hawkish FOMC duration headwind vs Healthcare **INFLOW
     persistence 0.8** [MACRO:sector_flow_persistence] (risk-monitor).
- **Open questions surfaced:** (1) Does the P10 LEAP put OI **build on 6/19+** (campaign →
  short resurrects) or stay a one-print orphan (fade)? (2) Is the +3.8σ put a **front-run of the
  COMP006 durability readout** or a fade-able outlier? — the single fact that most changes the
  verdict.
