# Phase 8 — Multi-Agent Analyst Desk

**Ticker:** RKT
**As-of date:** 2026-07-17
**Generated:** 2026-07-19T20:26:00-04:00
**Upstream phases cited:** phase-1 through phase-7c (all packed to each agent)

## Summary

Five specialist agents ran in parallel on the full phases 1–7c context. The desk is
**non-directional-constructive with zero shorts**: **2 LONG, 2 RANGE, 1 NEUTRAL**,
**average conviction 2.4 / 5**. No agent took the short side — the 7b/7c veto (4/4
EPS beats, +75% rev growth, MS $19 upgrade, 10.8% SI = squeeze fuel) was accepted
universally, and the "bearish" options tape was read across the board as
**call-overwriting/hedging, not conviction bearishness**. Every agent converged on
the same **$14.5–15.0 cage** with **$13.50 as the invalidation shelf** and **$15.00
as the call-wall cap**, and every agent flagged the **FOMC 07-29 → earnings 07-30
binary** as the fuse that breaks the range. The consistent structural recommendation
is **defined-risk / long-vol into the event** (call spread or skewed long straddle),
explicitly **not a naked directional bet** — reinforced by risk-monitor's "small,
defined-risk, or don't play the binary" given beta 2.21 in a TRANSITIONAL regime.

## Agent verdicts table

| Agent | bias | conviction | horizon | one_line_take |
|---|---|---|---|---|
| accumulation-hunter | **LONG** | 3 | 1-4w | Quiet money building a long under $14.5, collaring it with calls sold above / puts sold below — accumulation real but earnings is the fuse. |
| contrarian-scanner | **RANGE** | 2 | 1-4w | Nothing's crowded — P/C dead center, IV-rank 51.7; the only "divergence" is call-overwriting misread as bearishness. |
| sweep-tracker | **NEUTRAL** | 2 | 1-4w | No aggressive sweep momentum — thin tape, upside calls getting sold, straddle players betting on the print. |
| earnings-scout | **LONG** | 3 | 1-5d | Fundamentals+sentiment veto the short, gamma coiled at $14.5, but fairly-priced vol into a double-header argues for defined-risk, not a naked bet. |
| risk-monitor | **RANGE** | 2 | 1-4w | Uncorrelated on paper, but 2.2 beta into a hawkish-FOMC-then-earnings gauntlet during a "reduce size" tape means small/defined-risk or pass. |

## Per-agent details

### accumulation-hunter — LONG / 3 / 1-4w
- **key_levels:** support $14.30 (dark-pool shelf) / $13.50 (put wall); resistance
  $15.00 (call wall + positive-gamma pin); invalidation = daily close < $14.30 with
  large-tier dark-pool buy_ratio rolling under 0.55, or a break of $13.50.
- **top_signal:** Three lanes converge on *genuine* (not mechanical) accumulation —
  phase-2 large-tier buy_ratio 0.651 across 1,426 continuous prints, phase-3's
  call-writing + put-selling collar around a structural +45k Mar-27 $19C, and
  phase-4's DEX +$51.1M forcing dealers to buy the underlying.
- **top_risk:** The −$364,914 net-directional flow could be outright bearish rather
  than overwriting; the −$48.5M ATM short-gamma pocket means 07-30 breaks the cage
  either way.

### contrarian-scanner — RANGE / 2 / 1-4w
- **key_levels:** support $14.30 / $14.50 (put-wall + GEX pivot + 07-31 max-pain);
  resistance $15.00; invalidation = close < $13.50 on volume, or a break > $15.50–16
  not absorbed by call-writing.
- **top_signal:** phase-7 price-vs-flow DIVERGENCE (+9.9% price vs −$364,914 flow),
  with 7b/7c fundamentals+analysts disagreeing with the bearish tape — but a
  flow-vs-fundamentals gap, **not** a crowd-sentiment extreme.
- **top_risk:** There is no crowd to fade (P/C z +0.38, crowd_state BALANCED); a
  hawkish FOMC into an earnings miss on a beta-2.21 name would validate the bearish
  flow. **Only 2 of 5 fade signals fire → below the ≥3 bar → low-conviction range, not a sized fade.**

### sweep-tracker — NEUTRAL / 2 / 1-4w
- **key_levels:** support $14.00; resistance $15.00; invalidation = close < $13.50 or
  a reversal of the upside call-selling above $19–21.
- **top_signal:** The only clean aggressive reads are Oct $19C + Jan $21.2C **sold on
  the bid** ($125k + $115k) vs a single $18C bought ($145k) — a cap-the-upside
  signature, not bullish momentum.
- **top_risk:** The 983-lot Jul-24 ATM straddle + short dealer gamma at $14.5 means
  any earnings-adjacent move accelerates through the pivot regardless of the weak sweep signal.

### earnings-scout — LONG / 3 / 1-5d
- **key_levels:** support $14.50 (put-wall/GEX pivot); resistance $15.00 (call-wall,
  +$13.1M GEX); invalidation = close < $13.50, or a hawkish FOMC 07-29 breaking the
  cage before earnings.
- **top_signal:** phase-7b vetoes the bearish lane — 4/4 beats (+25–50%), EPS
  accelerating $0.04→$0.15, +75.3% rev — while 7c confirms (fresh MS OW/$19, 0 sells),
  turning 10.83% short float into squeeze fuel on a beat.
- **top_risk:** Vol is rich-by-percentile but only FAIRLY priced (VRP +0.003) into a
  genuine binary (FOMC hawkish-tail + earnings) with a −$48.5M ATM short-gamma pocket
  amplifying either break — **no cheap-vol edge** if the beat habit fails.

### risk-monitor — RANGE / 2 / 1-4w
- **key_levels:** support $14.00 (max-pain magnet); resistance $15.00; invalidation =
  close through $13.50 on volume, or hawkish FOMC pushing 30y mortgage decisively > 6.55%.
- **top_signal:** Fresh re-run of `uw risk portfolio-correlation --symbols
  RKT,OKLO,PATH,SHOP` confirms **RKT in zero high-correlation pair** (only PATH/SHOP
  at 0.707) → RKT genuinely diversifies today's book; no correlation size-cut.
- **top_risk:** Beta 2.21 on a back-to-back binary cluster (FOMC 07-29 + earnings
  07-30, ~±8–10% implied) inside a TRANSITIONAL, risk-off regime (SPY < 20/50-SMA,
  38.4% breadth) → large position/regime risk even with clean correlation.

## Disagreements

No directional disagreement — **not a single SHORT.** The only spread is
LONG (constructive) vs RANGE/NEUTRAL (non-directional):
- The two LONGs (accumulation-hunter, earnings-scout) lean on the *institutional
  accumulation + fundamental/sentiment veto* → a constructive bias.
- The three non-directional (contrarian, sweep, risk-monitor) stress *no crowd to
  fade, thin sweeps, and regime/beta risk* → range/wait.
- These are **compatible**, not contradictory: all agree the *underlying is
  constructive but the near-term is a coiled range whose direction the 07-30 binary
  resolves* — hence the shared defined-risk/long-vol conclusion.

## Tool errors

None. All five agents (`accumulation-hunter`, `contrarian-scanner`, `sweep-tracker`,
`earnings-scout`, `risk-monitor`) available and returned. risk-monitor independently
re-ran `uw risk portfolio-correlation` (confirming the no-cluster read).

## Verdict for downstream phases

- **Plurality bias:** **Non-directional-constructive** — 2 LONG / 2 RANGE / 1 NEUTRAL,
  **0 SHORT**. Read as **RANGE-with-constructive-lean** (the underlying favors up over
  down, but near-term is cage-bound pending the event).
- **Average conviction:** **2.4 / 5** (LONG 3, RANGE 2, NEUTRAL 2, LONG 3, RANGE 2).
  Per phase-8 heuristic (split → target 0.55–0.65 conviction, defined-risk structure).
- **Three highest-quality signals across agents:**
  1. Triple-lane accumulation — DP large-tier 0.651 + DEX +$51.1M + building OI/collar
     `[AGENT:accumulation-hunter → DP/STRUCT/OI]`.
  2. Fundamentals+sentiment veto the short — 4/4 beats + MS $19 upgrade + 10.8% SI
     squeeze fuel `[AGENT:earnings-scout → FUND/SENT]`.
  3. No crowd to fade + coiled dealer gamma at $14.5 → range until the event breaks it
     `[AGENT:contrarian-scanner / sweep-tracker → INSIGHT/STRUCT]`.
- **Open questions surfaced (for phase-8b debate):**
  - Is the −$364,914 bearish flow overwriting (bull case) or genuine directional
    bearishness (bear case)? The whole desk assumes overwriting — is that assumption robust?
  - Given fairly-priced vol (VRP ~0) into a real binary, is long-vol even worth
    paying for, or does the defined-risk *long* (call spread) leaning on the beat
    habit dominate? (bull vs bear structural debate for 8b/9.)
