# Phase 8 — Multi-Agent Analyst Desk

**Ticker:** NVDA
**As-of date:** 2026-05-15
**Upstream phases cited:** phase-1 through phase-7
**Generated:** 2026-05-17T17:24Z

## Summary

**5 of 5 analysts returned NEUTRAL or RANGE** — zero LONG, zero SHORT.
Average conviction is **2.4/5**. All five agents independently picked the
same 1–5d horizon (binary 5/20 earnings dominates) and converged on the
same level set ($219–220 support, $235–236 resistance, $230 gamma wall).
Cleanest single recommendation came from **earnings-scout**:
> *"Sell the earnings vol crush, not direction — 240/250 call credit spread
> or 217.5/240 short iron condor on the 05-22 chain captures 22-pt IV
> collapse while phase-3's call-write wall caps upside risk."*

The unanimous "no directional conviction + binary-event in 5 sessions" read
strongly steers phase-9 toward a **defined-risk, vol-selling structure**
rather than directional debit / naked premium.

## Agent verdicts table

| Agent | Bias | Conviction | Horizon | One-line take |
|-------|------|-----------|---------|---------------|
| accumulation-hunter | NEUTRAL | 2 | 1-5d | Not accumulation — pre-earnings rebalancing with 3 flashy LEAP prints. Stand aside. |
| contrarian-scanner | RANGE (bearish skew) | 3 | 1-5d | Fade rips into $235; size half per TRANSITIONAL regime. Don't short the floor. |
| sweep-tracker | RANGE | 2 | 1-5d | $230 gamma wall pins; fade both extremes; don't pay up for premium. |
| earnings-scout | RANGE | 3 | 1-5d | Sell vol crush — 240/250 credit spread OR 217.5/240 iron condor on 05-22. |
| risk-monitor | NEUTRAL (lean RANGE) | 2 | 1-5d | Half size, defined-risk only, fade naked premium. No naked short premium. |

**Plurality bias:** RANGE (3 of 5) with the other 2 NEUTRAL — net interpretation
is RANGE-WITH-BINARY-EVENT.
**Average conviction:** 2.4/5.
**5 of 5 agents at the same horizon:** 1-5d.

## Per-agent details

### 1. accumulation-hunter

> Phase-7 `conviction_matrix` shows call BID volume (1.50M) exceeding call
> ASK volume (1.40M) today while phase-5 90d cumulative net flow is flat
> (+$200M on +36% rally) — that is the opposite of quiet accumulation,
> that is distribution dressed up as LEAP noise.

- **bias:** NEUTRAL
- **conviction:** 2
- **horizon:** 1-5d
- **support:** $225.83 (near) / $219.44 (major DP shelf, $2.25B 5d)
- **resistance:** $235.74 / $230 (gamma wall)
- **invalidation:** close < $218.30 (today ZGL → short-gamma) OR DP mega-tier
  buy_ratio re-flips > 0.60 with confirming +$200M+ daily net flow
- **top_risk:** "A clean Q1 FY27 beat + raised Blackwell guide on 2026-05-20
  AMC squeezes the 240/250 05-22 call wall and forces dealer-buying through
  $235.74 into the $250 institutional speculator target."

### 2. contrarian-scanner

> Crowd's chasing LEAPs and 250C lottos into IV pctile 100 with flow
> already quietly distributing — fade the rip into $235, don't short the
> floor.

- **bias:** RANGE (bearish skew)
- **conviction:** 3
- **horizon:** 1-5d
- **support:** $219.44 / $218.30 (today ZGL)
- **resistance:** $235.74 (5/14 intraday high was $234.45)
- **invalidation:** close > $236 on positive flow > +$150M, OR call bid/ask
  ratio flips back to ask-heavy with DP buy_ratio > 0.60
- **top_signal:** `insights_price_vs_flow` DIVERGENCE=TRUE (price +26.84% /
  30d vs net flow -$42.65M bearish today) + phase-5 90d cumulative net
  +$200M against a 36% rally + 20% bullish_flow win rate.
- **top_risk:** "Binary 5/20 print — a clean beat + raised Q2 Blackwell
  guide snaps spot through $235.74 resistance and the +$25.85T DEX
  structural bid overwhelms any fade."

### 3. sweep-tracker

> Sweep tape is loud but mixed — $230 gamma wall pins price into earnings,
> fade rips toward $235, fade flushes toward $220, don't pay up for premium.

- **bias:** RANGE
- **conviction:** 2
- **horizon:** 1-5d
- **support:** $219.44
- **resistance:** $235.74
- **invalidation:** close < $218.30 (ZGL flip) OR close > $236 with sweep
  flow ask-dominant
- **top_signal:** call BID volume 1.50M > call ASK volume 1.40M with
  price_vs_flow DIVERGENCE TRUE — distribution into strength
- **top_risk:** "Phase-4 backwardation (74% IV 05-22 vs 52% 30d) + phase-6
  5/20 AMC + COMPLACENT call-rich skew + IV pctile 100 = any miss
  accelerates a vanna-driven flush through $218.30 ZGL."

### 4. earnings-scout (highest-utility take)

> Sell the earnings vol crush, not direction — 240/250 call credit spread
> or 217.5/240 short iron condor on the 05-22 chain captures 22-pt IV
> collapse while phase-3's call-write wall caps upside risk.

- **bias:** RANGE
- **conviction:** 3
- **horizon:** 1-5d
- **support:** $219.44
- **resistance:** $235.74
- **invalidation:** close < $218.30 (ZGL flip) OR close > $238 (overruns
  the 237.5/240 call-write wall on volume)
- **top_signal:** Phase-4 05-22 IV 74% vs 32d IV 52.5% (backwardation 1.41)
  with COMPLACENT term skew → earnings stress fully priced AND upside more
  expensive than downside — textbook setup for post-print IV crush.
- **top_risk:** "Blowout Blackwell Q2 guide gaps NVDA through 237.5/240
  short-call wall → dealer gamma-squeeze toward $250."

### 5. risk-monitor

> Half size, defined-risk only, fade naked premium — IV 100th percentile
> into a binary print with bearish flow divergence and tech sector outflows
> is how books blow up.

- **bias:** NEUTRAL (lean RANGE)
- **conviction:** 2
- **horizon:** 1-5d
- **support:** $218.30 (today ZGL) / $219.44 (5d DP cluster)
- **resistance:** $235.74 / $237.5–$240 (call-write supply)
- **invalidation:** close < $218.30 on volume OR earnings gap >|10%|
  breaching either DP cluster
- **top_signal:** `insights_price_vs_flow` DIVERGENCE TRUE + phase-5
  bullish_flow 20% win rate
- **top_risk:** "Correlation cluster blowup — long NVDA, SMH, QQQ, any
  Mag7 single-name, or ADI all express the same AI-capex bet into a binary
  print with IV at 100th percentile."

Additional context from risk-monitor:
- **Correlation cluster** to constrain at portfolio level: NVDA, SMH, QQQ,
  ADI (5/20 same-day semis), Mag7 single-names. *Cap aggregate AI-beta
  exposure*; do not pair NVDA longs with SMH/QQQ longs.
- **Worst realistic loss sizing:** front-week IV implies ±10–12% earnings
  gap. Bad-print scenario: $200–$205 (-10 to -12%); tail $185 (-19%).
  Cap position at **0.5× normal premium-at-risk** per TRANSITIONAL guidance.

## Disagreements

No directional disagreements. The only modest split is conviction level
(2 vs 3) and bias label (NEUTRAL vs RANGE), but those are essentially
synonyms for "don't take a directional bet here, sell the vol crush".

## Tool errors

No agent reported MISSING — all 5 agent types were available and
responsive. No additional tool errors surfaced by any agent during their
runs.

## Verdict for downstream phases

- **Plurality bias:** **RANGE** (3 of 5) / **NEUTRAL** (2 of 5).
- **Average conviction:** 2.4/5.
- **Three highest-quality signals across all agents:**
  1. **Price-vs-flow DIVERGENCE TRUE** (cited by 3 of 5 agents) —
     `[INSIGHT:price_vs_flow]`
  2. **Term backwardation 1.41 + COMPLACENT skew + IV pctile 100** =
     textbook IV-crush setup (cited by 4 of 5 agents)
     `[STRUCT:front_end_iv_ratio]` `[STRUCT:term_skew]` `[HIST:iv_percentile_zscore]`
  3. **$230 gamma wall ($7.69T GEX)** = magnetic strike, expect pin
     behavior into earnings (cited by 3 of 5 agents)
     `[STRUCT:today_gamma_flip]`
- **Open questions surfaced by agents:**
  - Correlation/sizing constraint (risk-monitor) — phase-9 must mention.
  - Whether a Blackwell beat could overrun the call-write wall and
    convert this into a gamma-squeeze trade (all 5 agents flagged this
    as the top tail risk).
  - Specific structure: earnings-scout's iron condor on 05-22 chain is the
    most concrete recommendation — phase-9 should evaluate and either
    adopt or counter.
