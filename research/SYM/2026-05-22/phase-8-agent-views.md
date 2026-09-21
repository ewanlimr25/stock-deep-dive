# Phase 8 — Multi-Agent Analyst Desk

**Ticker:** SYM
**As-of date (effective):** 2026-05-21
**Generated:** 2026-05-22T15:30Z
**Upstream phases cited:** phase-1 through phase-7

## Summary

Four specialist sub-agents returned verdicts in parallel
(earnings-scout skipped — earnings 2026-08-05 is 75 DTE, well outside
the 30-day pre-earnings window). The desk **leans RANGE / mildly LONG
with low conviction (avg 2.25/5)** — 2 votes RANGE, 1 vote LONG,
1 vote NEUTRAL-leaning-LONG. **Unanimous level agreement**: every
agent puts **support at $49.50, resistance at $52.00, invalidation on
a daily close below $49.50**. This convergence is the single most
important phase-8 finding — it gives phase-9 hard mechanical
boundaries regardless of which directional bias is correct.

The bullish dissent (accumulation-hunter, conviction 3) leans on the
$4.04M multi-day DP base + fresh $2.02M $49.96 shelf as a "start of
build," not exit. The two RANGE votes (contrarian-scanner,
risk-monitor) both emphasize: fresh gamma flip, low IV %ile, thin
liquidity, hostile macro, and the June catalyst window. The
sweep-tracker takes a middle ground (NEUTRAL with tactical long
into resistance) and explicitly downgrades the bullish sweep
persistence as "featherweight."

## Agent verdicts table

| Agent | Bias | Conv | Horizon | One-line take |
|-------|------|------|---------|---------------|
| accumulation-hunter | LONG | 3 | 1-4w | Mid-tier funds quietly built a $4M shelf at $46-$47 and added $2M at $49.96 while dealers flipped long-gamma today — the floor is being laid, not the exit. |
| contrarian-scanner | RANGE | 2 | 1-4w | Crowd called the bottom on DP prints while institutions sold LEAP calls and bought Jan-27 P42.5 hedges — fade both extremes, sell the $52 wall and the $49.50 floor. |
| sweep-tracker | NEUTRAL (lean LONG tactical) | 2 | 1-5d | Sweep persistence is real but featherweight — $710K over 5 sessions, premium bid-side on LEAPs, no smart_money_flow hit; this is mean-reversion chop into $52, not a chase. |
| risk-monitor | RANGE | 2 | 1-5d | Range-trade the $49.50-$52 corridor with defined-risk half-size only; fresh, low-confluence gamma flip on a thin name walking into a triple-catalyst window with sector flow against it — do not size up, and cut on a daily close under $49.50. |
| earnings-scout | **MISSING** (out of window — 75 DTE) | — | — | — |

## Per-agent details

### accumulation-hunter

```
VERDICT
- bias: LONG
- conviction: 3
- horizon: 1-4w
- key_levels:
    support: 49.50 (dealer-hedge boundary; sub-support $49.96 DP shelf, then $46.40-$47.40 base)
    resistance: 51-52 (combined $10.31M positive GEX call wall; secondary $55)
    invalidation: daily close below $49.50 flips dealer regime to
                  negative-gamma air pocket and breaks the fresh $49.96 shelf
- top_signal: Phase-2 multi-day dark-pool accumulation of $4.04M at
  $46.40-$47.40 plus a same-week $2.02M shelf at $49.96, corroborated
  by phase-7 institutional_accumulation buy/sell 2.05 and phase-5's
  30 consecutive OI build days — the base is the START of a build,
  with today's positive-gamma regime flip
  ([HIST:gex_time_series], NEG→POS on 2026-05-21) providing the
  mechanical bid to lean against it.
- top_risk: The accumulation is mid-tier only ($1.82M today, no
  mega/block prints, IV %ile 10.34 means hedges are cheap to add) and
  macro is hostile (CPI 3.8%, Industrials sector outflow, Q3 guide
  sequentially lower) — a CPI/FOMC shock in mid-June could reopen
  the negative-GEX air pocket toward the $46.40 base before the
  long thesis pays.
- one_line_take: Mid-tier funds quietly built a $4M shelf at $46-$47
  and added $2M at $49.96 while dealers flipped long-gamma today —
  the floor is being laid, not the exit.
```

### contrarian-scanner

```
VERDICT
- bias: RANGE
- conviction: 2
- horizon: 1-4w
- key_levels:
    support: 49.50
    resistance: 52.00
    invalidation: daily close < $49.50 (loses positive-gamma shelf
                  into the $47.5/$45/$42.5 negative-GEX air pocket)
                  OR daily close > $52.00 with follow-through (breaks
                  the $51-$52 call-wall ladder)
- top_signal: Phase-4 $51+$52 call walls hold $10.31M combined GEX
  directly overhead while Phase-5 shows the GEX regime flipped
  POSITIVE only today after a fresh negative-gamma drawdown — the
  dealer hedging that just snapped the $45→$51 bounce is the same
  machinery that now caps the upside, not a launchpad.
- top_risk: Phase-2 dark-pool accumulation ($4.04M base $46.40-$47.40
  + fresh $49.96 shelf) + Phase-4 +$33.6M net DEX bid could ignite a
  vanna squeeze if low IV (10th %ile) mean-reverts upward, melting
  through $52 before the fade triggers.
- one_line_take: Crowd called the bottom on dark-pool prints while
  institutions sold LEAP calls and bought Jan-27 P42.5 hedges — fade
  both extremes, sell the $52 wall and the $49.50 floor.
```

### sweep-tracker

```
VERDICT
- bias: NEUTRAL (lean LONG tactical, fade above $52)
- conviction: 2
- horizon: 1-5d
- key_levels:
    support: $49.50 (dealer-hedge boundary; $46.40-$47.40 deeper DP
             accumulation base)
    resistance: $52.00 (combined $51-$52 call wall = $10.31M GEX);
                secondary $55
    invalidation: daily close below $49.50 (flips back to negative-gamma
                  air pocket) OR sustained ask-side sweep campaign
                  >$200K premium per session to validate bullish
- top_signal: Phase-3 0DTE C53 ask/bid 420:4 (+404 OI) plus C52
  ask-side build sit ON TOP of Phase-4's +$10.31M GEX call wall at
  $51-$52 — retail lottery into mechanical resistance, not a
  sustained sweep campaign.
- top_risk: Phase-5 GEX regime flipped POSITIVE only TODAY after a
  3-week FULLY_NEGATIVE run; fresh flips empirically precede vol
  expansion, and Phase-6 Industrials sector outflow −$27M + CPI 3.8%
  can crack the $49.50 floor fast.
- one_line_take: Sweep persistence is real but featherweight — $710K
  over 5 sessions, premium bid-side on LEAPs, no smart_money_flow
  hit; this is mean-reversion chop into $52, not a chase.
```

### risk-monitor

```
VERDICT
- bias: RANGE
- conviction: 2
- horizon: 1-5d
- key_levels:
    support: 49.50 (dealer-hedge boundary; below = negative-GEX air
             pocket per Phase-4)
    resistance: 52.00 (combined $51-$52 GEX wall = $10.31M per Phase-4)
    invalidation: daily close < $49.50 (regime flip back to negative
                  gamma) OR daily close > $52.10 with volume (breaks
                  call-wall ladder)
- top_signal: Phase-5 confirms GEX regime flipped NEG→POS today for
  the first time in 30 sessions with IV at 10.34th percentile (1y
  low) — tool note flags this empirically precedes realized-vol
  expansion, not suppression.
- top_risk: Fresh 1-day gamma flip is fragile and sits directly
  above a negative-GEX air pocket ($49→$42.5 cumulative −$3.2M GEX);
  if the $49.50 boundary breaks into the back-to-back June CPI
  (~Jun 11) + FOMC (~Jun 16-17) + OPEX (Jun 18) catalyst window,
  dealer hedging amplifies down through a thin chain (top-25
  premium only $390K, dark-pool only $1.82M) — Industrials sector is
  already bleeding $27M/day while Tech absorbs $297M, so any
  drawdown will not get a sector-rotation bid.
- one_line_take: Range-trade the $49.50-$52 corridor with
  defined-risk half-size only; this is a fresh, low-confluence
  gamma flip on a thin name walking into a triple-catalyst window
  with sector flow against it — do not size up, and cut on a daily
  close under $49.50.
```

### earnings-scout

```
MISSING: earnings-scout intentionally skipped — next earnings is
2026-08-05, 75 days out, outside the standard 30-day pre-earnings
window. Per phase-8 protocol, agent skipped (not a tool failure).
```

## Disagreements

Single bullish dissent: **accumulation-hunter** (LONG conv 3) vs.
three votes for RANGE / NEUTRAL.

The accumulation-hunter's top_signal:
> *"Phase-2 multi-day dark-pool accumulation of $4.04M at $46.40-$47.40
> plus a same-week $2.02M shelf at $49.96 ... the base is the START
> of a build."*

This is the strongest single bullish argument in the desk and is not
refuted by the RANGE votes — they simply weight it less than the
gamma-fragility and macro-headwind signals. **Both views are
defensible.** Phase-9 should adopt a *defined-risk LONG* skew that
respects the RANGE consensus on levels.

## Tool errors / agent misses

- earnings-scout: MISSING (out of window — 75 DTE; intentional skip).

## Verdict for downstream

- **Plurality bias:** **RANGE (2)** > LONG (1) > NEUTRAL-lean-LONG (1).
  Read as **range-bound with a bullish skew on accumulation but
  capped by gamma walls and macro fragility**.
- **Average conviction:** **2.25 / 5** across the four returning
  agents. Below the 3.0 threshold typically considered actionable.
- **Three highest-quality signals across agents:**
  1. **[AGENT:accumulation-hunter]** *"Phase-2 multi-day dark-pool
     accumulation of $4.04M at $46.40-$47.40 plus a same-week $2.02M
     shelf at $49.96 ... corroborated by phase-7
     institutional_accumulation buy/sell 2.05 and phase-5's 30
     consecutive OI build days."* — the structural long signal.
  2. **[AGENT:contrarian-scanner]** *"Phase-4 $51+$52 call walls hold
     $10.31M combined GEX directly overhead ... the dealer hedging
     that just snapped the $45→$51 bounce is the same machinery that
     now caps the upside, not a launchpad."* — the structural cap
     signal.
  3. **[AGENT:risk-monitor]** *"GEX regime flipped NEG→POS today for
     the first time in 30 sessions with IV at 10.34th percentile (1y
     low) — tool note flags this empirically precedes realized-vol
     expansion, not suppression."* — the regime-fragility signal.
- **Open questions surfaced by agents:**
  - All four agents converge on $49.50 as the hard invalidation. If
    that floor holds through the June catalyst window, the
    accumulation-hunter's "floor being laid" thesis activates.
    Phase-9 should use $49.50 as the SINGLE binary decision boundary.
  - Three agents flagged the **June 11 (CPI) + June 16-17 (FOMC) +
    June 18 (OPEX)** triple-catalyst window. Phase-9 must explicitly
    sequence the position around this — *do not hold size through it
    without a hedge*.
  - The bullish dissent + sweep-tracker's caveat about "no
    sustained sweep campaign" point to phase-9 sizing the position
    half-on now, half-on contingent on a sustained ask-side sweep
    campaign (>$200K/session) confirming the build.
