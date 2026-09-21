# Phase 8 — Multi-Agent Analyst Desk

**Ticker:** BILI
**As-of date:** 2026-05-20 (data date 2026-05-19)
**Generated:** 2026-05-20T10:45:00-04:00
**Upstream phases cited:** phase-1 through phase-7

## Summary

Five specialist sub-agents returned **a 3-way split bias** with one strong
LONG conviction and one strong SHORT conviction in opposition. Plurality by
**count** is LONG/RANGE/NEUTRAL tied 2-2 vs SHORT 1; plurality by
**conviction-weighted bias** is **LONG (sum 7)** vs SHORT (sum 4) vs
RANGE/NEUTRAL (sum 4). Average conviction across all five agents = **3.0 /
5**. **No agent recommends a naked aggressive long; ALL five agents
recommend defined-risk or wait-for-better-setup posture.** All five agree on
the structural levels (support $19.11 ZGL → $19.49-$19.65 DP cluster →
$18.82 lower base; resistance $20 magnet → $22.30 5-day overhead → $25
institutional ceiling) and on the **need to manage exposure across the 6/17
FOMC**.

## Agent verdicts table

| Agent | Bias | Conviction | Horizon | One-line take |
|---|---|---|---|---|
| accumulation-hunter | **LONG** | **4** | 1-4w | "Real institutions bought the earnings beat in size at $18.82-$19.65 and rolled long-dated upside; ride them to $22.50 with hard stop $18.82." |
| contrarian-scanner | **SHORT** | **4** | 1-4w | "Crowd bought the earnings beat; institutions sold them call premium with a $30 ceiling and rolled puts forward — fade the chase, short $20.50 against $22.50." |
| sweep-tracker | RANGE | 2 | 1-5d | "LEAP sweep is real but slow; near-tape is two-sided pin trade — fade $20.00-$20.30 to $19.55, no chase, wait for 6/18 OPEX reset." |
| earnings-scout | LONG | 3 | 1-3m | "Q1 beat got tape-shrugged, vol is bombed-out, institutions laddering Jan-27 $25/$30 — buy a Jul/Aug $20/$25 debit call spread to harvest IV crush now and ride into Q2 catalyst." |
| risk-monitor | NEUTRAL | 2 | 1-5d | "Half-size or skip — correlated China-ADR cluster, fragile gamma regime above thin ZGL cushion, 6/17 FOMC cliff make this defined-risk-only; max 0.25R, exit before 6/13." |

## Per-agent details

### accumulation-hunter [AGENT:accumulation-hunter]

- **bias:** LONG
- **conviction:** 4
- **horizon:** 1-4w
- **support:** $19.49-$19.65 (today's block-tier DP accumulation cluster)
- **resistance:** $22.30-$22.50 (5-day DP cluster + 22.5 put-roll strike +
  Jul-17 $30C short-call ceiling implies $22-25 cap)
- **invalidation:** close below $18.82 on volume, OR Comm Services sector
  outflow accelerates >$150M/day, OR negative-gamma flip back below $19.11
  ZGL.
- **top_signal:** "Phase-2 block-tier DP buy_ratio 1.00 with $5.91M /
  307,752 shares ALL at-or-above mid (125k @ $19.65 + 105k @ $18.82
  AT-ASK) is institutional fingerprint identity-matched to Phase-1's
  Jan-2027 $25C ask sweep and Phase-3's May-29 $25C → Jan-27 $25C OI roll
  — same desk, same thesis, multi-leg." [DP:largest, FLOW:options_flow_sweeps,
  OI:biggest_increases]
- **top_risk:** "Communication Services -$84.3M sector outflow + KWEB -16%
  YTD + 6/16-17 new-Fed-Chair FOMC could overwhelm single-name accumulation
  and force the $20 GEX magnet to break lower toward the $17.5 neg-gamma
  accelerant."

### contrarian-scanner [AGENT:contrarian-scanner]

- **bias:** SHORT
- **conviction:** 4
- **horizon:** 1-4w
- **support:** $19.11 (ZGL — below this is negative-GEX acceleration zone to
  $17)
- **resistance:** $20.00 (massive $117.6M GEX pin wall, 51.8% of total GEX;
  secondary $22 call-write wall)
- **invalidation:** sustained close >$22.50 on volume (breaks call-write
  wall; institutions forced to cover Jul $30 short calls).
- **top_signal:** "Phase-3 institutional CALL WRITING of 2,421 contracts
  ALL bid-side at Jul $30 + Phase-4 COMPLACENT inverted skew (-0.0192) +
  Phase-5 market-wide bullish-flow 20% win rate = smart money sold the
  post-earnings pop into a retail call-chase with capped upside."
  [OI:biggest_increases, STRUCT:term_skew, HIST:signal_backtest]
- **top_risk:** "Phase-2 block-tier dark pool buy_ratio 1.00 ($5.9M) could
  mark a genuine accumulation floor; if Comm Services flow reverses and
  $20 pin holds into June OPEX, gamma squeezes toward $22 stops out the
  short."

### sweep-tracker [AGENT:sweep-tracker]

- **bias:** RANGE
- **conviction:** 2
- **horizon:** 1-5d
- **support:** $19.49-$19.65 (DP cluster)
- **resistance:** $20.00 GEX magnet / $22.00 GEX wall
- **invalidation:** close < $19.07 (5/15 low) flips to SHORT; close > $20.63
  (1-σ upper) opens chase toward $22.
- **top_signal:** "Phase-4 GEX +$226.8M with $20 magnet (51.8% of total)
  plus Phase-1 near-dated sweeps two-sided ($19.5C 6/18 ask $18.3k vs bid
  $17.3k) = pinning, not momentum." [STRUCT:gex, FLOW:options_flow_sweeps]
- **top_risk:** "A second institutional buy program landing on top of the
  18:28:07Z Jan-27 $25C footprint could force dealer re-hedging and break
  the long-gamma cap upward through $20.63 toward $22."
- **Note:** Pulled additional UW data on June-18 sweeps — confirmed
  two-sided flow at $19.5C and $20P, dampening the near-term
  momentum-chase thesis.

### earnings-scout [AGENT:earnings-scout]

- **bias:** LONG
- **conviction:** 3
- **horizon:** 1-3m
- **support:** $19.11 (ZGL) / $18.30 recent low / $18.00 (Aug $18P hedge
  strike)
- **resistance:** $20.00 (gamma magnet $117.6M) → $22.50 → $25.00 (Jan-27
  long call strike)
- **invalidation:** daily close below $18.00 OR Comm Services sector
  outflow accelerates with BILI breaking VWAP $19.28.
- **top_signal:** "Phase-3 institutional Jan-27 $25/$30 bull call spread +
  Phase-4 inverted 'complacent' 25Δ skew (-0.0192) with IV z-score -2.35
  shows smart money laddering multi-quarter upside while retail/dealer
  hedges are absent — classic post-beat ignored setup."
  [OI:smart_positioning, STRUCT:term_skew, HIST:iv_percentile_zscore]
- **top_risk:** "8/21 $18 protective put ask-side OI build (94 DTE, lands
  in Q2 print window) signals smart money carries genuine downside tail —
  either China-ADR delisting headline or Q2 ad-growth deceleration could
  nuke the thesis before August."
- **Structure recommendation:** Jul/Aug $20/$25 debit call spread.

### risk-monitor [AGENT:risk-monitor]

- **bias:** NEUTRAL
- **conviction:** 2
- **horizon:** 1-5d
- **support:** $19.11 (ZGL); secondary $18.82-$18.98 DP shelf; cliff $17.50.
- **resistance:** $20.00 GEX wall; $22.30-$22.50 5-day overhead.
- **invalidation:** spot prints < $19.11 ZGL on close (gamma flip to NEG)
  OR KWEB/FXI break their 30d lows (sympathy cascade) OR BILI 4hr flow
  turns net seller while DP buy_ratio < 0.55.
- **top_signal:** "Phase 4 GEX +$227M positive but spot only +2.3% above
  ZGL with 5 regime flips in 28d (Phase 5) — the cushion is paper-thin
  and the regime is statistically unstable." [STRUCT:gex,
  HIST:gex_time_series]
- **top_risk:** "BILI 0.81 correlated to FXI and 0.82 to KWEB inside a
  100%-China-ADR concentration basket; one tariff/VIE headline before
  6/17 new-Fed-chair FOMC unwinds the entire cluster simultaneously."
- **Sizing rule:** max **0.25R**, exit before **6/13**.

## Disagreements

The desk is split **LONG vs SHORT** on a 4/4 conviction-equal axis. Both
sides correctly identify the same structural levels but disagree on which
flow signature dominates:

- **accumulation-hunter (LONG 4):** weights the **block-tier DP
  buy_ratio 1.00 + Jan-27 $25C ask sweep** as the dominant institutional
  fingerprint.
- **contrarian-scanner (SHORT 4):** weights the **Jul-17 $30C call writing
  (2,421 contracts) + inverted complacent skew + market-wide bullish-flow
  20% win rate** as the dominant retail-fade fingerprint.

Both agents acknowledge the *other side's signal as their own top_risk* —
which is the cleanest possible mark of a genuinely two-sided setup.
**Resolution: the truth is probably somewhere between** — institutional
desks ARE accumulating stock and long-dated calls (LONG-positive) WHILE
writing premium against that exposure at upside caps (SHORT-positive for
near-term capped upside). This is a **structured bull spread**, not a
naked directional play.

The sweep-tracker (RANGE 2) and risk-monitor (NEUTRAL 2) effectively endorse
**the structured view**: range-trade with capped upside ($25 ceiling),
defined-risk only, exit before FOMC.

## Tool errors / Missing agents

- None of the five specified agent types were unavailable.
- Each agent self-reported ≤3 additional tool calls; total tool budget
  consumed across all five was well under the 30-call phase budget.

## Verdict for downstream

- **Plurality bias (conviction-weighted):** **LONG (sum 7) > RANGE/NEUTRAL
  (sum 4) ≈ SHORT (sum 4).** No single side dominates; trade structure
  matters more than directional conviction.
- **Average conviction:** **3.0 / 5** — matches the phase-1 → phase-7
  composite reads (mostly 3-4).
- **Three highest-quality signals across agents:**
  1. **Block-tier DP buy_ratio 1.00 + matching Jan-27 $25C ask sweep + 5/29
     $25C OI close = identity-matched institutional bull-spread program.**
     [DP:largest, FLOW:options_flow_sweeps, OI:biggest_increases]
     (accumulation-hunter)
  2. **Jul-17 $30 call OI +2,421 ALL bid-side institutional call writing +
     inverted complacent skew + market-wide bullish-flow 20% recent
     win rate.** [OI:biggest_increases, STRUCT:term_skew,
     HIST:signal_backtest] (contrarian-scanner)
  3. **GEX +$227M positive but spot only +2.3% above ZGL with 5 regime
     flips in 28d — paper-thin cushion in unstable regime.**
     [STRUCT:gex, HIST:gex_time_series] (risk-monitor)
- **Open questions surfaced by agents:**
  - Is the Aug-21 $18 protective put the institutional bloc's signal that
    they themselves have genuine downside tail-risk for Q2 (Aug)
    earnings? (earnings-scout flagged this as their top_risk.)
  - At what spot level does the contrarian's short-call-write strategy
    actually become forced-cover (the "$22.50 sustained close" trigger)?
    (contrarian-scanner highlighted this is their structural cap.)
  - What's the actual BILI ↔ FXI / KWEB correlation in the LAST 5
    sessions vs the 90-day baseline? (risk-monitor estimated 0.81-0.82
    but used trailing window — recent moves might be tighter still.)

## Synthesis for phase-9

The desk consensus, when conviction-weighted, leans **LONG but capped**.
The two highest-conviction agents (accum 4 / contrarian 4) effectively
describe **two legs of the SAME institutional structure**: long stock +
long lower-strike calls + short upper-strike calls + short puts. **Phase-9
should NOT recommend a naked long call.** It should recommend a
**defined-risk debit call spread** that:

1. Captures the directional thesis from accumulation-hunter and
   earnings-scout (long Jul or Aug $20 call).
2. Acknowledges the contrarian's cap (short Jul or Aug $25 call —
   below the institutional Jan-2027 $30 short-write strike but above the
   $22 DP overhead supply).
3. Sizes at **half-or-less** of normal book per risk-monitor's TRANSITIONAL
   regime guidance and sub-threshold signal-confluence rating from phase-7.
4. Sets invalidation at the **$18.82 close** (DP support break) or the
   **$19.11 ZGL break** — agent consensus on these levels.
5. Closes or trims before the **6/17 FOMC** per risk-monitor's explicit
   guidance and the broader event-overhang.
