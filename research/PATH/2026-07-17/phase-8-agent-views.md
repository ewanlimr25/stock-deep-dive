# Phase 8 — Multi-Agent Analyst Desk

**Ticker:** PATH · **As-of:** 2026-07-17 · **Version:** v1
Five specialist agents fanned out on the packed phase-1→7c context (one sanctioned
parallel batch). `earnings-scout` **skipped** — earnings 2026-09-03 is 48 days out
(>30d gate).

## Summary

The desk converges on a **low-conviction RANGE**, not a directional trade. Of the
four agents that ran: **1 LONG, 2 NEUTRAL, 1 RANGE** — plurality is *non-directional*
(NEUTRAL/RANGE, 3 of 4), average conviction **2.0/5**. Crucially, **all four agree on
the structure and levels even where the bias label differs**: unanimous **support
$11.88** (the phase-2 dark-pool demand shelf) and **resistance $13** (the phase-3/4
call wall + peak-GEX cap + analyst-PT cluster), with invalidation on a close below
~$11.50–$11.88. The lone bull (accumulation-hunter) itself qualifies the call —
"size for grind-to-cap, not breakout, until earnings forces the dealers' hand."
Contrarian sees nothing crowded to fade (and the short base too thin to squeeze);
sweep-tracker sees no fresh momentum trigger and would fade rallies into $13; and
risk-monitor flags the TRANSITIONAL "half-size" regime + COMPLACENT skew as a hidden
landmine on a rising-VIX tape. Net desk read: **a caged $11.88–$13 range with a real
but slow accumulation floor, low conviction, half-size, catalyst-dependent (Sep-3)
for any breakout.**

## Agent verdicts table

| Agent | bias | conviction | horizon | one_line_take |
|-------|------|-----------|---------|---------------|
| accumulation-hunter | **LONG** | 3 | 1-4w | Real quiet buying under a real gamma lid — size for grind-to-cap, not breakout, until earnings forces the dealers' hand. |
| contrarian-scanner | NEUTRAL | 1 | 1-4w | Nothing's crowded — book's balanced, no P/C extreme, no divergence, shorts too thin to squeeze; sit out, this isn't my setup. |
| sweep-tracker | NEUTRAL | 2 | 1-5d | Persistent bullish sweeps are real but the tape's gone quiet and dealers are capping $13 — no fresh trigger to chase, fade rallies into the wall. |
| risk-monitor | RANGE | 2 | 1-4w | Not tight-correlated to OKLO so no forced cluster cut, but half-size anyway — hawkish Fed, rising VIX, complacent skew all say the range could snap. |
| earnings-scout | — | — | — | MISSING/SKIPPED (earnings 48d out, >30d gate) |

## Per-agent details

### accumulation-hunter — LONG, conv 3, 1-4w
- support: $11.88–$12.01 (5-day DP demand shelf; break of $11.50 invalidates)
- resistance: $13.00 (dominant call wall, +6.03M peak GEX, analyst PT cluster)
- invalidation: close below $11.50, OR Nov'26 $16C OI unwinding on flat/negative flow
- top_signal: Convergence of dark pool ($267M, 65.7% buy-tier, absorbed an intraday
  fade), OI (11 consecutive days +337k net, Nov'26 $16C +4,255), and
  institutional-accumulation detector (buy/sell 1.96) — all while the unusual-volume
  scanner stays silent — the classic quiet-accumulation fingerprint.
- top_risk: Positive GEX pins price in a dealer-capped range under a hard $13
  wall/max-pain-$11.5 magnet, so accumulation may just fund a slow grind rather than a
  breakout absent the Sep-3 catalyst.

### contrarian-scanner — NEUTRAL, conv 1, 1-4w
- support: $11.88–$12.01 / $11 (max-pain, DEX support)
- resistance: $13 (dominant OI wall 19.7k, GEX peak — a cap, not squeeze fuel)
- invalidation: close below $11.88, OR close above $13 on rising volume
- top_signal: None of the 5 fade screens fire — P/C z only +0.20 (no extreme),
  price-vs-flow ALIGNED not divergent, OI BUILDING +337k/11d not unwinding — a quiet,
  non-crowded tape, not a fade candidate.
- top_risk: The one real crowd asymmetry — 28% short interest — is defanged by a
  2.6–3.6d cover ratio, so neither a squeeze-long nor a crowded-long fade has fuel;
  forcing a contrarian trade fights the tape.

### sweep-tracker — NEUTRAL, conv 2, 1-5d
- support: $11.88
- resistance: $13.00
- invalidation: close below $11.88 (bull case) OR close above $13 (cap thesis fails)
- top_signal: The 5-day sweep-persistence (5/5, consistency 1.0, $6.19M bullish) is
  the only genuine momentum tell, but today's tape is QUIET (outside top-60/80,
  net +$182k) and the biggest structure is a two-sided $13P roll, not a fresh sweep.
- top_risk: The positive-GEX $13 wall is a hard dealer-sell cap directly overhead, so
  even a real sweep-pop has almost no room before mean-reversion.

### risk-monitor — RANGE, conv 2, 1-4w
- support: $11.88 (DP demand shelf) / thin put support to $10
- resistance: $13.00 (OI wall 19.7k + GEX hard cap)
- invalidation: close below $11.88 on rising volume, OR a GEX flip to negative (the
  durable 30d positive regime breaking), OR VIX climbing through 20
- top_signal: GEX-positive/ZGL $6.78 with $13 a hard dealer cap = a range trade, not a
  breakout — but the TRANSITIONAL "half position sizes" regime overrides the bullish
  structure for sizing.
- top_risk: The COMPLACENT skew is a hidden landmine — cheap precisely because VIX
  just jumped +20% w/w off a low base; if realized vol catches up, downside is
  uncushioned (put support thin to $10) with no vanna buffer.

## Disagreements
- **accumulation-hunter (LONG) vs the other three (NEUTRAL/RANGE)** is the only bias
  split — and it is a *soft* one: the bull explicitly sizes "for grind-to-cap, not
  breakout" and shares the identical $11.88/$13 levels. Its distinguishing
  top_signal is the **quiet-accumulation fingerprint** (DP + 11-day OI build +
  accumulation detector firing *while* the unusual-volume scanner stays silent) — the
  one read that treats the range floor as an *entry* rather than a reason to sit out.
  No agent is bearish; no agent argues for a short.

## Tool errors
- `earnings-scout`: SKIPPED (earnings 2026-09-03, 48d out > 30d gate) — not a failure.
- No agent tool errors; none needed extra `uw` calls (context was sufficient).

## Verdict for downstream

- **Plurality bias: NEUTRAL/RANGE (3 of 4); 1 LONG.** Net desk = **non-directional
  range with an accumulation floor** — nobody bearish, nobody breakout-bullish.
- **Average conviction: 2.0 / 5** across the four non-skipped agents.
- **Three highest-quality signals across agents:**
  1. Quiet-accumulation fingerprint — DP $267M/65.7%-buy + OI 11-day +337k build +
     accumulation detector 1.96, *with unusual-volume silent* `[AGENT:accumulation-hunter]`
     (phase-2/3/5/7).
  2. $13 = hard dealer cap — peak GEX +6.03M + 19.7k call OI + analyst PTs coincide;
     a range, not a launchpad, absent a catalyst `[AGENT:sweep-tracker, risk-monitor]`
     (phase-3/4/6).
  3. TRANSITIONAL "half-size" regime + COMPLACENT skew on rising VIX = uncushioned
     downside; size down regardless of the bullish floor `[AGENT:risk-monitor]`
     (phase-4/6).
- **Open questions surfaced by agents:** (a) Does the accumulation ever break $13
  *without* the Sep-3 catalyst, or is any July/August long just range-grinding into a
  dealer wall? (b) Is the COMPLACENT skew cheap insurance to *buy* (define the long's
  risk) rather than a reason to avoid? (c) If VIX pushes through 20 and GEX flips, does
  the thin sub-$11.88 put support let the range break down fast (the risk-monitor
  landmine)? Phase-8b (debate) and phase-9 must resolve these before sizing.
