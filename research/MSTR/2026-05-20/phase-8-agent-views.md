# Phase 8 — Multi-Agent Analyst Desk

**Ticker:** MSTR
**As-of date:** 2026-05-19 (effective)
**Generated:** 2026-05-20T01:00:00Z
**Agents launched:** accumulation-hunter, contrarian-scanner, sweep-tracker, risk-monitor
**Agents skipped:** earnings-scout (next earnings 2026-07-30 is > 30 DTE — outside skill window)

## Summary

**4-of-4 NEUTRAL verdict with average conviction 2/5.** The desk is unanimous: there
is no directional edge in MSTR at the day-of close on 2026-05-19. The agents do
not disagree with each other but each surface a different reason for the same
conclusion. The unifying themes:

1. **$174.79 (45-DTE ZGL = institutional cost-basis ceiling) is the gate**: cited
   as resistance by 3 of 4 agents; flipping above it converts dealer regime to
   long-gamma AND clears the $174–$179 institutional supply zone (phase-2).
2. **$160 is the breakdown trigger**: cited by 3 of 4 agents (resistance_wall
   in phase-4 + dark-pool floor at $163 in phase-2).
3. **The June 18 FOMC binary is the only "real edge" location** — agents see no
   reason to commit conviction outside event-vol structures.
4. **The contrarian fade is NOT yet justified**: contrarian-scanner confirmed
   on its own follow-up that the P/C z-score collapses from +1.45σ (20-day) to
   only **+0.64σ on a 60-day window** — sentiment is not washed-out.
5. **Risk-monitor pulled a fresh correlation read: IBIT/MSTR 0.864, COIN/MSTR
   0.803** — MSTR is functionally one position within a 4-name BTC-proxy
   cluster, requiring portfolio-aware sizing.

The verdict for phase-9: **build the trade plan around the June 18 binary
event**, not the day's flow. Size at **0.5x normal**, use **debit (long-premium)
structures** per VRP -4.3% and IV33rd-percentile, and respect the
$160 / $174.79 corridor for entry/stop logic.

## Agent verdicts table

| Agent | bias | conviction | horizon | one_line_take |
|---|---|---:|---|---|
| accumulation-hunter | NEUTRAL | 2/5 | 1-5d | Blocks are nibbling at $166 but the whales aren't here yet — accumulation footprint, not a stampede; wait for mega-tier confirmation or a $178 reclaim. |
| contrarian-scanner | NEUTRAL | 2/5 | 1-4w | Tail-puts panic but ATM stays complacent and P/C z-score halves on longer lookback — crowd isn't extreme enough to fade; stand down. |
| sweep-tracker | NEUTRAL | 2/5 | 1-5d | Tape is loud but two-sided — $465M of mixed sweeps, LEAP roll not new bull, ATM call magnet vs $180 wall, stand down until break of $174.79 or $160. |
| risk-monitor | NEUTRAL (lean RANGE) | 2/5 | 1-4w | TRANSITIONAL + MIXED + 0.86 BTC-proxy correlation = cap MSTR at 0.5x normal size, hard 1% portfolio max-loss, defined-risk debit structures only. |

**Plurality bias: NEUTRAL — 4 of 4 agents (100%)**
**Average conviction: 2.0 / 5** — the desk explicitly recommends caution.

## Per-agent details

### accumulation-hunter

```
VERDICT
- bias: NEUTRAL
- conviction: 2
- horizon: 1-5d
- key_levels:
    support: 164.74
    resistance: 178.03
    invalidation: close below 162.50 on block-tier buy_ratio flipping <0.50
- top_signal: Phase 2 block-tier (≥$1M) buy_ratio 0.754 on $14.95M premium
  with a $243.6M dark-pool cluster pinned at $166.63 — institutions
  absorbing at-spot, not chasing.
- top_risk: $178.03 cluster ($140.4M premium) sits underwater as overhead
  supply, large-tier buy_ratio only 0.519, no mega prints, and
  conviction_matrix flags MIXED at 3.66% — classic falling-knife trap
  risk after a -15.9% six-day flush on a fundamental (Saylor BTC-sale)
  catalyst.
- one_line_take: Blocks are nibbling at $166 but the whales aren't here
  yet — accumulation footprint, not a stampede; wait for mega-tier
  confirmation or a $178 reclaim.
```

### contrarian-scanner

```
VERDICT
- bias: NEUTRAL
- conviction: 2
- horizon: 1-4w
- key_levels:
    support: 163.30 (phase-2 DP support; loss = mechanical acceleration)
    resistance: 174.79 (phase-4 45-DTE ZGL = phase-2 institutional
                        cost-basis ceiling)
    invalidation:
      short-fade thesis: spot < $160 close (phase-4 negative-gamma
                          wall + phase-2 DP support break)
      long-fade thesis: spot > $179.62 reclaim
- top_signal: Phase-5 P/C z-score +1.45σ on 20-day window collapses to
  +0.64σ on 60-day window (just-confirmed) AND phase-4 25Δ term skew =
  COMPLACENT (0.974) — crowd is NOT actually washed out; panic is
  confined to 5–10Δ wings, not full-curve, so the contrarian-long fade
  lacks the sentiment extreme required.
- top_risk: Phase-6 Saylor 2026-05-05 sell-admission is a STRUCTURAL
  re-rating (not noise) and the phase-4 June 18 FOMC binary at 143% IV
  is a real 28-day-away catalyst — any contrarian fade gets steamrolled
  if BTC breaks $76k or FOMC prints hawkish.
- one_line_take: Tail-puts panic but ATM stays complacent and P/C z-score
  halves on longer lookback — crowd isn't extreme enough to fade; stand
  down, wait for spot to reclaim $174.79 or wash to <+2σ P/C.
```

**New data this agent surfaced**: 60-day P/C z-score = +0.64σ (vs the +1.45σ
20-day reading in phase-5). This is a critical refinement — the "approaching
extreme" framing in phase-5 was a 20-day artifact, not a real sentiment extreme.

### sweep-tracker

```
VERDICT
- bias: NEUTRAL
- conviction: 2
- horizon: 1-5d
- key_levels:
    support: $160 (5/22 resistance_wall flips to break-trigger; $150
             put-build wall below)
    resistance: $174.79 (45-DTE ZGL) → $180 (call wall, 34.5k OI)
    invalidation:
      Decisive close >$174.79 flips bias LONG (gamma regime + $170C magnet)
      Decisive close <$160 flips SHORT (resistance_wall break, negative-gamma
                                          cascade toward $150)
- top_signal: Phase 1 — 5-session sweep persistence of $465.79M with
  consistency_score 1.0 and dominant_direction = MIXED; today's top sweep
  ($120C LEAP bid $2.32M paired with $135C LEAP ask $2.18M) reads as a
  diagonal up-roll, not fresh directional initiation.
- top_risk: Phase 3 — $170 5/22 call OI +8,654 (the day's hottest strike)
  is a near-term magnet that could trap shorts into Friday OPEX if
  BTC/IBIT firms, while the simultaneous $245C Oct ask-side sweep ($1.43M)
  and ITM put SALES ($1.33M bid on 5/22 $182.5P) mean a violent reflex
  bounce is live.
- one_line_take: Tape is loud but two-sided — $465M of mixed sweeps, LEAP
  roll not new bull, ATM call magnet vs $180 wall, stand down until break
  of $174.79 or $160.
```

### risk-monitor

```
VERDICT
- bias: NEUTRAL (lean SHORT-vol-of-direction, tilt RANGE through 5/22;
                 defined-risk only)
- conviction: 2
- horizon: 1-4w (to June 18 FOMC + OPEX)
- key_levels:
    support: $160 (phase-4 resistance_wall + phase-2 $163 supply floor;
              break = mechanical acceleration zone)
    resistance: $174.79 (phase-4 45-DTE ZGL = phase-2 institutional
                          cost-basis ceiling; single highest-leverage level)
    invalidation:
      spot < $160 on close OR Saylor BTC-sale announcement OR June FOMC
      hawkish hold = thesis-resetting gap;
      spot > $174.79 on volume flips dealer regime long-gamma and
      invalidates the bearish tilt
- top_signal: Phase-4 IV term structure prices 143% on the June 18 expiry
  vs 75-78% neighbors — the FOMC binary (Phase-6: 65% hold / 33% cut, hot
  3.8% CPI) is the only place real edge lives; everything else is MIXED
  (Phase-7 conviction_matrix 3.66% confidence, MSTR absent from both
  bullish and bearish signal_confluence top-50).
- top_risk: Correlated blowup — IBIT/MSTR corr 0.864, COIN/MSTR 0.803
  (fresh risk_portfolio_correlation pull), so any BTC-proxy book is one
  bet; combine with Phase-4 short-gamma (ZGL -5.5% above spot), 8 GEX
  flips in 28 sessions, post-5/22 vanna-charm SELL pressure, and a -20%
  gap-risk envelope on hawkish FOMC = sizing must assume a single -20%
  MSTR move wipes the entire cluster simultaneously.
- one_line_take: TRANSITIONAL regime + MIXED conviction + 0.86 BTC-proxy
  correlation = cap MSTR at 0.5x normal size, hard 1% portfolio max-loss
  per trade, defined-risk debit structures only (long premium per VRP
  -4.3%), and treat MSTR+IBIT+COIN+MARA as ONE position not four.
```

**New data this agent surfaced**: fresh `risk_portfolio_correlation` pull —
IBIT/MSTR = 0.864, COIN/MSTR = 0.803. MSTR is a BTC-proxy cluster member, not
an independent name for risk-budgeting purposes.

## Disagreements

**None.** All four agents converged on NEUTRAL with conviction 2/5. The
unanimity is itself notable — when multiple specialist lenses all decline to
take a directional side, that IS the read.

The closest thing to disagreement is the *time horizon*:
- accumulation-hunter, sweep-tracker: **1-5 day** focus (OPEX week mechanical)
- contrarian-scanner, risk-monitor: **1-4 week** focus (June 18 FOMC binary)

This is not actually a disagreement — it reflects two complementary trade
windows that the desk can play sequentially: the OPEX-pin trade through 5/22,
then a reset for the FOMC vol trade into 6/18.

## Tool errors

- No `MISSING:` agents — all 4 launched agents returned structured verdicts.
- earnings-scout intentionally skipped (next earnings 2026-07-30, outside 30d window).

## Verdict for downstream phases

- **Plurality bias:** **NEUTRAL — 4 of 4 (100%)**
- **Average conviction:** **2.0 / 5** (LOW — the desk says explicitly: no directional edge today)
- **Three highest-quality signals across agents (verbatim citations):**
  1. *(risk-monitor)* "Phase-4 IV term structure prices 143% on the June 18 expiry vs 75-78% neighbors — the FOMC binary is the only place real edge lives." → **the central trade thesis**.
  2. *(contrarian-scanner)* "P/C z-score +1.45σ on 20-day window collapses to +0.64σ on 60-day window AND phase-4 25Δ term skew = COMPLACENT (0.974) — crowd is NOT actually washed out." → **invalidates the contrarian-long fade**.
  3. *(accumulation-hunter)* "Block-tier ≥$1M buy_ratio 0.754 on $14.95M premium with a $243.6M dark-pool cluster pinned at $166.63 — institutions absorbing at-spot, not chasing." → **defines the support floor at $166**.

- **Open questions surfaced by agents (phase-9 must answer or acknowledge):**
  1. Has a **mega-tier ($10M+) dark pool print** arrived in the next session, confirming whale accumulation? (accumulation-hunter — "wait for mega-tier confirmation")
  2. Does **BTC/IBIT firm into the OPEX-week pin or break $76k**? (sweep-tracker, contrarian-scanner)
  3. **Portfolio correlation budget**: if the user already holds IBIT or COIN, MSTR adds < diversification value than the gross exposure suggests. (risk-monitor)
  4. **Vanna-charm post-OPEX risk**: the week of 2026-05-26 carries mechanical dealer-sell pressure as 5/22 IV crushes — what's the planned entry/exit timing? (risk-monitor)

- **Phase-9 directives:**
  - Build the **primary trade around the June 18 FOMC binary event**, NOT the day-of flow.
  - Use **debit/long-premium structures** (IV 33rd percentile + VRP -4.3% = mathematically favored).
  - **Size at 0.5x normal**, hard cap 1% portfolio max-loss.
  - Define entry around the $160 → $174.79 corridor.
  - Treat invalidation as: (a) spot close < $160 = thesis-resetting break, (b) spot close > $174.79 on volume = bear tilt invalidated, (c) Saylor BTC-sale announcement = -20% gap risk, escape immediately.
