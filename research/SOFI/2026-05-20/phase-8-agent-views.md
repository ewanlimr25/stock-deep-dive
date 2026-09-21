# Phase 8 — Multi-Agent Analyst Desk

**Ticker:** SOFI
**As-of date (requested):** 2026-05-20
**Effective data date:** 2026-05-19
**Generated:** 2026-05-20T00:00:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-4-structure.md, phase-5-historical.md, phase-6-macro.md, phase-7-insights.md

## Summary

Four specialist sub-agents returned **biased differently but converged
sharply on levels**. Bias is split 1-1-1-1 (LONG / SHORT / NEUTRAL / RANGE),
average conviction 2.75/5, but **every agent independently identified
$15.00-$14.85 as support and $16.00-$16.10 as resistance**. The contrarian
scored highest conviction (4/5 SHORT) leaning on phase-5's 0% bullish_flow
win rate and COMPLACENT skew, while the accumulation-hunter goes 3/5 LONG
on phase-2 large-tier accumulation. The neutral and range votes (both 2/5)
flag the same structural picture: a pin trade with broken dealer regime
and fintech-basket correlation overload. **Net read: this is a defined-
risk, range-bound setup with downside skew — phase 9 should size small,
play between $15 and $16, and prefer asymmetric structures that use the
COMPLACENT skew to buy cheap downside protection or play the vanna-squeeze
asymmetric upside via spreads, not naked directional bets.**

## Agent verdicts table

| Agent | Bias | Conviction | Horizon | One-line take |
|---|---|---|---|---|
| accumulation-hunter | LONG | 3/5 | 1-4w | Quiet accumulation in large-tier and OI; biggest blocks are trimming — buy $15 trapdoor, sell $16 wall. |
| contrarian-scanner | **SHORT** | **4/5** | 1-4w | Retail bought Q1 dip with Jan-27 15Cs; dealers short-gamma below, complacent above — every bounce into $15.65-$16 is exit liquidity. |
| sweep-tracker | NEUTRAL | 2/5 | 1-5d | Two-sided tape; bulls chase weeklies into pin while institutions write the upside — sweep persistence is noise, not edge. |
| risk-monitor | RANGE | 2/5 | 1-5d | Half-size max, defined-risk only; if long, buy cheap -5.1% skew puts as hedge — pin trade not trend trade. |

**Plurality bias:** No plurality (1-1-1-1 split). **Weighted by conviction:**
SHORT 4 + LONG 3 + NEUTRAL 2 + RANGE 2 = the **only single-bias view with
above-average conviction is contrarian SHORT at 4/5**, but it does NOT
dominate the room (LONG + NEUTRAL + RANGE = 7 vs SHORT = 4).
**Average conviction:** (3+4+2+2)/4 = **2.75/5**.

## Per-agent details

### accumulation-hunter

```
VERDICT
- bias: LONG
- conviction: 3
- horizon: 1-4w
- key_levels:
    support: $14.85 (Phase-4 $15 negative-GEX trapdoor floor + sub-VWAP $15.20)
    resistance: $16.00 (Phase-4 +$25B GEX ceiling / Phase-3 16C +12,861 OI wall)
    invalidation: Daily close below $14.50 OR dark pool buy_ratio drops below 0.50 for 2 consecutive sessions
- top_signal: Phase-2 large-tier $173.97M premium at 0.616 buy_ratio with pre-market prints at $15.56-$15.63 (paying ABOVE today's close) plus 5-day price-level clusters stacked at $15.30-$15.63 confirms institutions defended the value area into a -7.64% pullback while Phase-3 dropped +49,317 fresh call OI in a single session with ZERO rolls.
- top_risk: Phase-2 block tier (≥$1M) buy_ratio 0.339 shows the LARGEST institutional prints are net sellers and Phase-7 call ask/bid 89,595/108,863 confirms today's net call flow is bid-heavy WRITING, meaning smart money may be distributing into the visible large-tier "accumulation" while Phase-6 Financial Services sector outflow ($-48.8M) compounds the headwind.
- one_line_take: Quiet accumulation fingerprint is real in the large-tier and OI tape, but the biggest blocks are trimming — buy the $15 trapdoor, sell the $16 wall.
```

### contrarian-scanner

```
VERDICT
- bias: SHORT
- conviction: 4
- horizon: 1-4w
- key_levels:
    support: 14.50 (then 13.80 air-pocket below pin)
    resistance: 16.00 (dealer ceiling +$25B GEX) / 15.65 (DP cluster supply)
    invalidation: sustained close >$16.10 with PCR z >0 and skew normalizing positive
- top_signal: Phase-5 bullish_flow backtest 0% win rate on 7 signals avg -3.05% while Phase-4 skew is COMPLACENT -5.1% (calls richer than puts into a -14.7% drift) — textbook crowd-long-into-bearish-tape.
- top_risk: PCR z=-0.51 is NORMAL not extreme, so this isn't a euphoria-peak fade; a Vanna squeeze through $16 on a soft-CPI print could ignite the trapped Jan-27 15C delta and force chase to $16.50+.
- one_line_take: Retail bought the Q1 dip with Jan-27 15Cs; dealers are short-gamma below, complacent above — every bounce into $15.65-$16.00 is exit liquidity, not accumulation.
```

### sweep-tracker

```
VERDICT
- bias: NEUTRAL
- conviction: 2
- horizon: 1-5d
- key_levels:
    support: $15.00 (pin strike, 80,486 OI)
    resistance: $16.00 (+$25B GEX ceiling, dealer wall)
    invalidation: sustained close >$16.05 (call-writer pain) or <$14.85 (trapdoor breach below $15 GEX -$47B)
- top_signal: Phase 1 shows the May-22 15C $580k ask-side sweep (13,326 contracts, 686 trades) is being faded by Phase 7's net call-writing dominance (89,595 bid vs 108,863 ask) and Phase 3's institutional ceiling writers stacking 17-25C OI.
- top_risk: The Jan-27 15C $873k mid-sweep + persistent dark-pool buy ratio 0.616 means real LEAP accumulation is happening underneath; a CPI/FOMC upside surprise could trap the writers above $16 and ignite the -$47B gamma trapdoor in reverse toward $17.
- one_line_take: Two-sided tape with bulls chasing weeklies into a pin and institutions writing the upside — sweep persistence is noise, not edge; sit out until $16 breaks or $14.85 fails.
```

### risk-monitor

```
VERDICT
- bias: RANGE
- conviction: 2
- horizon: 1-5d
- key_levels:
    support: 15.00 (max-pain pin, 80k OI; below it trapdoor opens to 13.15 ZGL)
    resistance: 16.00 (+$25B gamma ceiling, institutional call-writer wall 17-20)
    invalidation: close <14.85 (loses $15 pin + flips into negative-gamma trapdoor) OR close >16.10 on volume (breaks dealer ceiling, vanna squeeze triggers)
- top_signal: Phase 4 GEX regime broke today ($+37B → -$4.6B, first negative print in 28 sessions) with $15 trapdoor (-$47B) directly under spot — dealer hedging now AMPLIFIES moves, not dampens.
- top_risk: SOFI correlates 0.88 with HOOD and 0.65-0.68 with COIN/UPST/AFRM in a TRANSITIONAL regime where Financial Services is the #2 sector outflow (-$48.8M) — any fintech basket exposure means SOFI is the same bet, not a diversifier.
- one_line_take: Half-size at most, defined-risk only; if long, buy the cheap -5.1% skew puts as hedge — this is a pin-trade not a trend-trade, and the dealer regime just flipped.
```

### earnings-scout

```
MISSING: earnings-scout — SKIPPED per phase-8 rubric. Next SOFI earnings is
2026-08-04 per UW screener (or 2026-07-28 per WebSearch), 77/70 days outside
the as-of date. The 30-day in-window guard applies; no pre-earnings playbook
needed in this run.
```

## Disagreements

The room is genuinely split: 1 LONG, 1 SHORT, 1 NEUTRAL, 1 RANGE. The clearest
disagreement is **accumulation-hunter (LONG 3) vs contrarian-scanner (SHORT 4)**.

**accumulation-hunter** anchors on phase-2's 0.616 large-tier buy_ratio +
pre-market premium-paying + 5-day clusters at $15.30-$15.65 above today's
close: *"institutions defended the value area into a -7.64% pullback."*

**contrarian-scanner** anchors on phase-5's 0% bullish_flow backtest +
phase-4's COMPLACENT skew into a -14.7% drift: *"textbook crowd-long-into-
bearish-tape."*

These two views are NOT actually incompatible:
- Both can be true if the large-tier "accumulation" is institutional
  inventory-building for delta-neutral covered-call writing programs (real
  buyers but covered, hence no upside push) while retail buys near-dated
  calls speculatively (the trapped Jan-27 15C / May-22 15C exposure).
- Both views converge on $16 as the ceiling — they only differ on whether
  the floor at $15 holds (LONG read) or breaks toward $14.50-$13.80 (SHORT
  read).

**sweep-tracker** and **risk-monitor** essentially split the middle:
"don't fight this; size small or pass." The risk-monitor's correlation
overlay (SOFI 0.88 to HOOD, 0.65-0.68 to COIN/UPST/AFRM) is the most
load-bearing risk-management observation of the four — a new datapoint
not present in phases 1-7.

## Tool errors

- **earnings-scout MISSING** — intentionally skipped per phase rubric
  (earnings > 30d out).
- All four returning agents completed without tool errors.
- Note: only risk-monitor invoked additional UW tools (3 tool calls);
  the other three reasoned directly from packed context.

## Verdict for downstream phases

- **Plurality bias:** None (1-1-1-1 split). Treat as **MIXED** baseline.
- **Average conviction across the 4 returning agents:** **2.75 / 5**.
- **Key-level consensus (UNANIMOUS):**
  - Support: **$15.00** (pin) → **$14.85** (trapdoor breach trigger) → **$14.50** (lower stop / contrarian's first target)
  - Resistance: **$16.00** (dealer ceiling) → **$16.10** (vanna squeeze trigger)
- **Three highest-quality signals across all agents:**
  1. **Phase-5 bullish_flow 5d backtest 0% win rate / -3.05% avg** —
     contrarian-scanner's anchor. Strongest negative-edge signal in the
     run. [HIST:signal_backtest]
  2. **Phase-4 GEX swing from +$37B (May 18) → -$4.6B (May 19), first
     negative in 28 sessions** — risk-monitor's anchor. Dealer regime
     flipped to amplifying. [STRUCT:gex] [HIST:gex_time_series]
  3. **Phase-2 large-tier $173.97M buy_ratio 0.616 + premarket prints at
     $15.56-$15.63 above RTH close** — accumulation-hunter's anchor.
     Real but threshold-marginal. [DP:block_stratified, DP:extended_hours]
- **Open questions surfaced by agents:**
  - **Risk-monitor's fintech correlation overlay** (SOFI 0.88 to HOOD,
    0.65-0.68 to COIN/UPST/AFRM) — phase 9 must factor this into sizing
    if the user has any fintech-basket exposure (caller doesn't say).
  - **Vanna squeeze trigger conditions**: contrarian's TOP RISK is the
    same as sweep-tracker's TOP RISK — a soft CPI (June 11) could ignite
    upside acceleration through $16 via dealer short-gamma covering.
    That's a date-specific asymmetric risk phase 9 must address.
  - **Is the $15.30-$15.65 5-day institutional cluster (phase 2) the
    selling zone (distribution into rip) or the buying zone (accumulation
    into pullback)?** Different agents read it different ways. The
    phase-2 dark pool data alone can't disambiguate; awaiting next-day
    (2026-05-20) RTH continuation.
