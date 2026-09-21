# Phase 8 — Multi-Agent Analyst Desk

**Ticker:** ENPH
**As-of date:** 2026-05-19 (effective UW data 2026-05-15)
**Generated:** 2026-05-19T00:00:00-04:00
**Upstream phases cited:** phase-1-flow.md through phase-7-insights.md (full packed context delivered to all five agents)

## Summary

The desk is **genuinely split 2-2-1**. Two agents (`accumulation-hunter`,
`sweep-tracker`) call **LONG with conviction 4**. Two agents
(`contrarian-scanner`, `earnings-scout`) call **SHORT with conviction 4** —
crucially, both SHORTs are **fade-vol / IV-crush / mean-revert thesis,
not directional outright shorts of the stock**. One agent (`risk-monitor`)
calls **NEUTRAL with conviction 2**, advocating half-size defined-risk
discipline. **There is no plurality direction.** Average conviction
across all five non-MISSING agents is **3.6**. **Three agents independently
flag the same phase-5 cohort backtest (14.3% win rate) and the same
$50 / $48 / $45 level cluster as the structural pivot.** The aggregated
desk view is therefore: **the setup is real but extended; the dominant
near-term edge is IV CRUSH, not direction**; use **defined-risk structures
sized for half-book conviction** with **$45–$48 as the hard invalidation
floor** and **$53.50–$55 as the immediate ceiling**.

## Agent verdicts table

| Agent | bias | conviction | horizon | one_line_take |
|---|---|---|---|---|
| `accumulation-hunter` | **LONG** | 4 | 1-4w | "Quiet size is loud here — 549 large dark prints buying the $48-$51 shelf while $50C OI explodes; accumulation is real, just don't pay the top tick." |
| `contrarian-scanner` | **SHORT** | 4 | 1-4w | "The +69.8% V-chase is done — earnings beat priced, IV at 121% with no catalyst until 7/28, Tech sector bleeding $151M, and the cohort that bought this flow lost money 86% of the time." |
| `sweep-tracker` | **LONG** | 4 | 1-5d | "Sweepers slamming Jun/Sep $50-$65 calls ask-side into a $50 wall magnet with no upside resistance — momentum lives near-term but get paid fast." |
| `earnings-scout` | **SHORT** | 4 | 1-4w | "Catalyst spent, IV rank 85 with no event in 30d window — sell July strangles or iron condors around $48/$55, fade the residual vol-of-vol." |
| `risk-monitor` | **NEUTRAL** | 2 | 1-5d | "Crowded score-5 long on a 1-day-old GEX regime after +69.8% — half size or less, defined-risk only, cut on $45 loss; this is a fade-the-late-comer setup, not a swing-long." |

**Bias distribution:** 2 LONG / 2 SHORT / 1 NEUTRAL.
**Conviction distribution:** four 4s and one 2.
**Average conviction (non-MISSING):** **3.6**.
**Plurality direction:** **NONE** — tied 2-2-1.

## Per-agent details

### `accumulation-hunter` — LONG, 4

```
VERDICT
- bias: LONG
- conviction: 4
- horizon: 1-4w
- key_levels:
    support: 48.01
    resistance: 53.50
    invalidation: close below 48.00 on expanding dark-pool sell-ratio (<0.45)
- top_signal: Phase 7 institutional_accumulation buy/sell ratio 1.71x converges
    with Phase 2 large-tier dark-pool buy_ratio 0.634 ($100M premium) and Phase 3
    Jun-26 $50C +4,985 OI roll-up — three independent accumulation fingerprints
    aligning.
- top_risk: Phase 5 bullish-flow backtest cohort posted 14.3% win-rate / −2.18%
    avg move after +69.8% 12-day rally, signaling chase-risk and mean-reversion
    exhaustion.
- one_line_take: Quiet size is loud here — 549 large dark prints buying the
    $48-$51 shelf while $50C OI explodes; accumulation is real, just don't pay
    the top tick.
```

### `contrarian-scanner` — SHORT, 4

```
VERDICT
- bias: SHORT
- conviction: 4
- horizon: 1-4w
- key_levels:
    support: 48.01
    resistance: 53.50
    invalidation: close > 55.00 on volume with skew normalizing (puts re-bid above calls)
- top_signal: Phase-5 historical_signal_backtest shows bullish_flow cohort
    14.3% win rate / −2.18% avg move over 20d in this exact regime, while
    Phase-4 inverted skew (−0.10, calls richer than puts) confirms crowd has
    piled into the same side.
- top_risk: Phase-4 positive GEX + $50 wall (+$2.78B) means dealers mechanically
    buy dips and pin spot, blunting any mean-reversion lower until $50 fails.
- one_line_take: The +69.8% V-chase is done — earnings beat priced, IV at
    121% with no catalyst until 7/28, Tech sector bleeding $151M, and the
    cohort that bought this flow lost money 86% of the time.
```

### `sweep-tracker` — LONG, 4

```
VERDICT
- bias: LONG
- conviction: 4
- horizon: 1-5d
- key_levels:
    support: 51.14
    resistance: 55.00
    invalidation: close below 50.00 with sweep flow flipping to bid-side puts
- top_signal: Phase 1 sweep_persistence prints 5/5 bullish with $55.8M total
    premium and 1.00 consistency score, plus $7M+ clean ask-side Jun/Sep call
    sweeps stacked into a long-gamma POSITIVE GEX regime (Phase 4).
- top_risk: Phase 5 cohort backtest shows only 14.3% win rate / −2.18% avg
    for bullish_flow at this 30d +69.8% extreme — sweep chasers are buying
    the top of a parabolic move.
- one_line_take: Sweepers slamming Jun/Sep $50-$65 calls ask-side into a $50
    wall magnet with no upside resistance — momentum lives near-term but get
    paid fast.
```

### `earnings-scout` — SHORT (= sell vol), 4

```
VERDICT
- bias: SHORT
- conviction: 4
- horizon: 1-4w
- key_levels:
    support: 48
    resistance: 55
    invalidation: IV30d re-expands above 105% or spot breaks $55 on >$80M
        dark pool buy-tier
- top_signal: Phase-5 IV rank 84.97 with VRP +0.115 immediately after Q1 +
    IQ9S-3P catalyst already printed = textbook post-event vol crush setup
    with realized lagging implied.
- top_risk: Jun-2027 $70C LEAP buyer plus 5/5 bullish sweep persistence
    ($55.8M) signals real upside chase that could pin gamma higher and
    squeeze short premium.
- one_line_take: Catalyst spent, IV rank 85 with no event in 30d window —
    sell July strangles or iron condors around $48/$55, fade the residual
    vol-of-vol.
```

### `risk-monitor` — NEUTRAL, 2

```
VERDICT
- bias: NEUTRAL
- conviction: 2
- horizon: 1-5d
- key_levels:
    support: 45.00
    resistance: 50.00
    invalidation: daily close < 45 (re-arms $40 short-gamma trap, GEX likely
        flips back negative)
- top_signal: Phase 4 dealer structure — $50 wall +$2.78B GEX concentration
    over a 1-day-old positive regime (Phase 5: flipped 5/14) makes pin/fragile
    both ways.
- top_risk: Triple-correlated exposure (Tech sector −$151M outflow + small/mid
    solar + policy-sensitive) into 6/17 FOMC with 4 dissents and only 18.4%
    UW confidence on a 14.3% cohort win rate.
- one_line_take: Crowded score-5 long on a 1-day-old GEX regime after +69.8%
    — half size or less, defined-risk only, cut on $45 loss; this is a
    fade-the-late-comer setup, not a swing-long.
```

## Disagreements

The desk is **fully split**, not just dissenting:

- **2 LONG (`accumulation-hunter`, `sweep-tracker`)** — confirm phases 1, 2, 3, 4,
  7 and lean on the strength of clean accumulation + ask-side sweep persistence.
  Both acknowledge the cohort backtest red flag and accordingly choose **shorter
  horizons (1-4w / 1-5d)** with **specific invalidation levels at $48 and $50**.

- **2 SHORT (`contrarian-scanner`, `earnings-scout`)** — read the same data
  through phase-5's cohort backtest and phase-6's catalyst-already-priced
  lens. **Critically, NEITHER advocates a directional short of ENPH stock**;
  both are calling **fade-vol / short-premium / mean-reversion** trades. The
  "SHORT" bias in their verdicts means "short vol via short straddles /
  strangles / iron condors" plus moderate directional fade.

  > **Quote (earnings-scout):** "sell July strangles or iron condors around
  > $48/$55, fade the residual vol-of-vol."

- **1 NEUTRAL (`risk-monitor`)** — declines to take a directional view and
  insists on **half-size or less, defined-risk only**, with **invalidation
  on a daily close < $45** (the level at which the short-gamma trap re-arms
  per phase-4).

**Reading:** the two LONG votes and the two SHORT votes are NOT mirror
images. They agree on the same data and the same level structure
(invalidation $45–$48, ceiling $53.50–$55); they disagree on **whether to
play direction or vol**. **A structure that monetizes IV CRUSH while
keeping a small directional bias bounded** is the synthesis — i.e., a
**defined-risk credit structure (iron condor / put-credit spread)** or
a **call spread that gives up extreme upside in exchange for cheaper
debit**.

## Tool errors

None. All five sub-agents returned valid VERDICT blocks. No `MISSING:`
declarations.

## Verdict for downstream phases

- **Plurality bias:** **NONE — tied 2 LONG / 2 SHORT / 1 NEUTRAL.** Phase-9
  must treat this as a **MIXED setup** per the rubric, target conviction
  band **0.55–0.65**, and use defined-risk structures.
- **Average conviction (non-MISSING):** **3.6 / 5**.
- **Three highest-quality signals across all agents:**
  1. **Phase-2 DP buy_ratio 0.634 + phase-7 institutional_accumulation
     1.71× + phase-3 Jun-26 $50C +4,985 OI = three independent accumulation
     fingerprints** [AGENT:accumulation-hunter].
  2. **Phase-5 cohort backtest 14.3% win rate / −2.18% avg + phase-4
     inverted skew −0.10 (calls richer) = crowd-on-same-side**
     [AGENT:contrarian-scanner].
  3. **Phase-5 IV rank 84.97 + VRP +0.115 immediately after Q1 + IQ9S-3P
     spent = textbook IV-crush setup with no event in 30d window**
     [AGENT:earnings-scout].
- **Open questions surfaced by agents:**
  - **`accumulation-hunter`**: are the same buyers ALSO showing up on
    Monday's tape? Phase-9 monitoring checklist must include daily DP
    buy_ratio re-pull.
  - **`risk-monitor`**: triple-correlated exposure into 6/17 FOMC — phase-9
    structure must NOT straddle the FOMC date without explicit acknowledgment.
  - **`sweep-tracker`**: "get paid fast" — argues for short-dated debit
    structures (1–5d), but phase-4 says 5/22 IV is 121% (debit too expensive).
    The implication is **no clean debit-call answer this week**.
  - **`earnings-scout`**: prefers a 7/17 expiry (between current and 7/28
    earnings) — captures pre-earnings vol re-expansion as the IV-rank
    decay plays out.
