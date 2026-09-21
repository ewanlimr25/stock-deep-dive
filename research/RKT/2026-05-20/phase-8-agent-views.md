# Phase 8 — Multi-Agent Analyst Desk

**Ticker:** RKT
**As-of date:** 2026-05-20 (data: 2026-05-19)
**Generated:** 2026-05-20T02:00:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-4-structure.md, phase-5-historical.md, phase-6-macro.md, phase-7-insights.md

## Summary

Five specialist sub-agents returned independent verdicts. The bias
distribution is **split with no majority direction**: LONG×1, SHORT×1,
NEUTRAL×2, RANGE×1. Average conviction is **2.8/5** — desk is undecided
on direction. However, the structural recommendation **converges sharply
across 4 of 5 agents: express the trade as a defined-risk, event-vol
structure built around the 2026-05-22 weekly IV anomaly**, NOT as naked
delta. The sweep-tracker (the only LONG agent) explicitly targets the
$14 positive-gamma magnet via a debit structure, which is compatible with
the earnings-scout's "sell 5/22 weekly vs long 6/18 or 7/17 call
calendar" prescription and the risk-monitor's "max 0.5R defined-risk
debit." The accumulation-hunter is the lone SHORT and grounds its call in
the synchronized 14:10 options-then-distribute sequence, which the desk
cannot dismiss — phase-9 must respect this as the bear scenario.

## Agent verdicts table

| Agent | Bias | Conviction | Horizon | One-line take |
|-------|------|-----------|---------|---------------|
| accumulation-hunter | **SHORT** | 3 | 1-5d | Stock holder monetizing into LEAPS calls — distribution dressed as accumulation; lean short to $12.73 [AGENT:accumulation-hunter] |
| contrarian-scanner | **NEUTRAL** | 2 | 1-5d | P/C extreme is hedge-driven not crowded-short; defined-risk 5/22 lottery, not contrarian long in cash [AGENT:contrarian-scanner] |
| sweep-tracker | **LONG** | 4 | 1-5d | Persistent bullish sweeps + complacent skew + short-gamma coil under $13 = breakout fuse; long above $12.80, target $14 [AGENT:sweep-tracker] |
| earnings-scout | **RANGE** | 3 | 1-5d | Sell rich 5/22 weekly vol vs long 6/18 or 7/17 calls; harvest the 18-point term-structure dislocation [AGENT:earnings-scout] |
| risk-monitor | **NEUTRAL** | 2 | 1-5d | Max 0.5R defined-risk debit, sized AFTER netting any UWMC/COOP/KBE/XLF/mREIT exposure; cut on $11.51 break [AGENT:risk-monitor] |

**Bias distribution:** LONG=1, SHORT=1, NEUTRAL=2, RANGE=1. **No plurality direction.**
**Average conviction:** (3+2+4+3+2)/5 = **2.8/5**.

## Per-agent details

### accumulation-hunter — SHORT 3 / 1-5d

```
key_levels:
  support: 12.52
  resistance: 13.20
  invalidation: Dark-pool mega/block tier buy_ratio flips above 0.55
                within 2 sessions AND spot reclaims $13.20 on close
top_signal: Phase-2 14:10→14:17 sequence — options package
            (Jul 12C + Dec 10P) executed 7 minutes before
            1.998M-share mega print at -$0.105 vs mid, then
            2.8M-share at-bid mega at 15:51; mega tier 100% SELL
            ($60.23M) — textbook "hedge then distribute" not
            stealth accumulation [DP:largest, DP:block_stratified,
            FLOW:top_premium_trades].
top_risk: Jan-28 10P STO + Aug 14C BTO + 28-day OI build implies
          a credible structural buyer is positioned below; if the
          seller exhausts inside 5/22 catalyst window, a 5-8%
          short-cover snap toward $13.20-$14.00 is plausible and
          would invalidate the short quickly.
```

The accumulation-hunter's decisive point is the **7-minute sequence**:
options-structuring at 14:10 immediately preceded the 14:17 mega
distribution print. A clean accumulator does NOT need to liquidate 2M
shares at a -10.5¢ discount to mid right after laying on the structured
long. The pattern is "monetize stock, retain optional upside" — a
distribution program with synthetic-upside retention, not new
accumulation. The Jan-27 12.2C + Jan-27 16.2P (deep-ITM put SOLD = wide
risk-reversal) is mechanically a synthetic long ABOVE $16.20 — only
economically rational for a holder unwinding direct exposure.

### contrarian-scanner — NEUTRAL 2 / 1-5d

```
key_levels:
  support: 12.38 (28-day low / DP VWAP 12.63 floor)
  resistance: 13.00 (-$292M 0DTE / -$374M 45-DTE gamma wall)
  invalidation: close below $11.51 (0DTE ZGL); alternatively,
                a 4th consecutive day where bullish_flow signals
                fail market-wide
top_signal: phase-5 P/C z-score +3.21 BEARISH_EXTREME (0.98 vs
            20d mean 0.42) coincides with phase-4 COMPLACENT
            25Δ skew -0.0212 — the put VOLUME is hedge-driven
            (collar legs), not speculative shorts, so it is NOT
            a crowded-short reading.
top_risk: phase-5 bullish_flow backtest 10% win rate / -1.57%
          avg move (9 of 10 large-caps failed last 20d) — the
          regime is actively rejecting bull setups regardless
          of structural quality.
```

Contrarian's most important call: **the P/C +3.2σ extreme is NOT a
crowded-short signal** because the put volume is hedge-driven (collar
legs) — confirmed by phase-4's COMPLACENT skew (calls richer than puts at
30Δ). A true crowded-short would have skew steepening into puts. It
isn't. So no fade-the-shorts trade. Edge migrates to **volatility**, not
direction.

### sweep-tracker — LONG 4 / 1-5d

```
key_levels:
  support: $11.51 (0DTE ZGL — break = short-gamma waterfall toward $10.52)
  resistance: $13.00 (-$292M 0DTE / -$374M 45-DTE gamma wall)
  invalidation: close below $11.51 on 5/22 catalyst, OR
                Dec 10P/13P put-side volume swamps next-day call
                sweep (collar flips to outright short)
top_signal: Phase-1 sweep_persistence: RKT alone at 5/5 sessions,
            consistency 1.0, $5.02M bullish-dominant premium, with
            synchronized 14:10 BTO of Jul-17 $12C + Dec-18 $10P —
            package trade, not bearish.
top_risk: The $817k Dec 13P ASK is a real hedge layer — if 5/22
          disappoints, dealers in -gamma at $13 amplify a flush
          through ZGL $11.51 toward $10.52; Dec puts pay before
          calls do.
```

Sweep-tracker is the most aggressive vote: highest conviction (4/5)
because the persistence signal is unambiguously strong and the
gamma-coil geometry under $13 is mechanically asymmetric. Even so, the
agent EXPLICITLY says "long above $12.80, target $14" — entry is on
breakout confirmation, not at-market.

### earnings-scout — RANGE 3 / 1-5d

```
key_levels:
  support: 11.51 (0DTE ZGL); hard invalidation 10.52 (45-DTE ZGL)
  resistance: 13.00 (gamma wall); breakout magnet 14.00 (+$289M)
  invalidation: weekly close <$10.52 (gamma waterfall) OR
                clean breakout/close >$13.10 on volume
                (dealer chase to $14)
top_signal: Phase-4 IV term: 5/22 weekly 85.9% vs 5/29 67.6%
            — 18.3 vol-point unexplained event spike, while
            phase-5 IV30 33rd %ile and VRP -4.05%. Front-week
            rich into unknown catalyst, back-end vol cheap —
            textbook calendar/diagonal setup.
top_risk: 5/22 catalyst is UNIDENTIFIED; macro outright hostile.
          If unknown event is rate/policy negative, the
          short-gamma $13→$11.5 corridor unwinds violently
          through the LEAPS book.
```

Earnings-scout's clean call is the **18 vol-point term-structure
dislocation** as the cleanest single edge — sell front-week 5/22 vol,
buy back-end (6/18 or 7/17) call. This decouples the trade from
direction while harvesting the event-vol mispricing.

### risk-monitor — NEUTRAL 2 / 1-5d

```
key_levels:
  support: $12.52 (today's distribution floor / mega VWAP)
  resistance: $13.00 (0DTE -$292M / 45-DTE -$374M wall)
  invalidation: close below $11.51 (0DTE ZGL) OR 30Y mortgage
                rate above 6.75% OR Brent above $95 on Iran
                escalation OR Financial Services sector flow
                extending another session below -$50M
top_signal: phase-5 bullish_flow backtest = 10% win rate /
            -1.57% avg over last 20d combined with phase-6
            Financial Services net flow -$48.79M — regime is
            actively rejecting longs in this sector.
top_risk: dealer DEX -$2.01B with 0DTE ZGL at $11.51 means a
          break below $12.52 cascades into short-gamma
          waterfall toward $11-$11.50; RKT compounds with any
          UWMC/COOP/KBE/XLF/mREIT longs in the book as a
          single "long mortgage credit + duration" bet.
```

Risk-monitor adds two essential constraints for phase-9:
- **Max 0.5R defined-risk debit only**, sized AFTER netting any
  UWMC/COOP/KBE/XLF/mREIT exposure.
- No naked stock, no naked calls, NO put-credit spreads (DEX -$2.01B
  says dealers already short puts — adding put credit would stack the
  same dealer-hedge exposure).

## Disagreements

The split is real:

- **sweep-tracker (LONG/4) vs accumulation-hunter (SHORT/3)** is the
  central disagreement.
  - Sweep-tracker emphasizes phase-1 sweep_persistence + phase-4 gamma
    geometry as the dominant signal: $5.02M cumulative bullish premium
    over 5/5 sessions is too clean to dismiss.
  - Accumulation-hunter emphasizes the phase-2 dark-pool 7-minute
    sequence + UW composite DIRECTIONAL_SHORT as the dominant signal:
    $60M mega-distribution after structured-long execution is too
    explicit to dismiss.
- **contrarian-scanner (NEUTRAL/2) and risk-monitor (NEUTRAL/2)** broker
  the disagreement by pivoting the trade to **volatility-relative
  structures** (defined-risk debit calendars / verticals) instead of
  picking a direction.
- **earnings-scout (RANGE/3)** explicitly proposes the synthesizing
  structure: SHORT 5/22 weekly vol vs LONG 6/18 or 7/17 calls (calendar
  or diagonal).

## Tool errors

None. All 5 agents completed; none returned MISSING.

## Verdict for downstream phases

- **Plurality bias:** NEUTRAL (2/5), with the structurally-converging
  recommendation being **event-vol-relative, defined-risk, sized at half
  or less**.
- **Average conviction:** 2.8/5.
- **Three highest-quality cross-agent signals:**
  1. **18-point IV term-structure dislocation at 5/22** (earnings-scout,
     reinforced by sweep-tracker): the cleanest edge of any kind in this
     stack [STRUCT:iv_term_structure, AGENT:earnings-scout].
  2. **The 14:10→14:17 sequence = "monetize-then-distribute"**
     (accumulation-hunter) — interprets the central phase-1/phase-2
     contradiction in a way no other agent disputes
     [AGENT:accumulation-hunter, DP:largest].
  3. **bullish_flow signal 10% win rate in this regime**
     (risk-monitor, contrarian, accumulation-hunter all cite) — the
     macro tape is hostile to naked bull bets across the board
     [HIST:signal_backtest, MACRO:SectorRotation].
- **Open questions / things phase-9 must resolve:**
  - **What is the 5/22 catalyst?** Still unidentified after agent
    review. Phase-9 will plan around it as a binary event and define
    invalidation accordingly.
  - **How to size the trade given correlation risk** with
    UWMC/COOP/KBE/XLF/mREIT positions? Phase-9 must note this in sizing
    instructions but cannot verify the user's book.
  - **Direction conditional on the 5/22 outcome?** Bullish if dealer
    gamma flips clean positive AND spot reclaims $13.20; bearish if
    sub-$11.51. The trade should be structured to survive both
    outcomes (defined risk).
