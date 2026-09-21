# Phase 8 — Multi-Agent Analyst Desk

**Ticker:** SNOW
**As-of date:** 2026-05-16 (data date: 2026-05-15)
**Generated:** 2026-05-17T00:00:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-4-structure.md, phase-5-historical.md, phase-6-macro.md, phase-7-insights.md

## Summary

5 specialist analysts ran in parallel against the same phases 1–7 context. **Plurality verdict is SELL-VOL / RANGE-TRADE / DEFINED-RISK** with the structure-of-choice being a 5/29 short strangle or iron condor around $150-$180. **4 of 5 agents (accumulation-hunter, contrarian-scanner, earnings-scout, risk-monitor) converge on a non-directional or short-bias premium-selling thesis**; only sweep-tracker votes LONG and even that vote carries an explicit "size half / exit before earnings" caveat. **Average conviction = 2.6/5** (deliberately moderate — high IV, fresh GEX regime, and 20% historical win rate of today's signal pattern force humility). Consensus levels: **support $151-$152.50** (5-day DP cluster), **hard invalidation $154.56** (ZGL), **resistance $160** ($2.31B GEX magnet), **secondary resistance $170-$180**.

## Agent verdicts table

| Agent | bias | conviction | horizon | one_line_take |
|---|---|---|---|---|
| accumulation-hunter | NEUTRAL (lean short-vol) | 2 | 1-4w | "This is not quiet accumulation — it is dressed-up distribution; institutions are selling stock to dealer hedgers while writing strangles to harvest 92nd-pctile IV." |
| contrarian-scanner | **SHORT** | 3 | 1-4w | "Consensus crowded long into rich 92nd-pctile IV with block-tier DP selling (0.304), UW MIXED 1.82%, and a backtest-failed bullish-flow signal — fade the euphoria, sell the IV crush." |
| sweep-tracker | **LONG** | 3 | 1-5d | "Aggressive 6/26 $145C ask sweep plus DEX +$113.8B mechanical dealer bid argues for a quick squeeze to the $160 gamma magnet, but size half and exit before 5/27 earnings IV crush." |
| earnings-scout | RANGE (short-vol tilt) | 3 | 1-4w | "Don't chase the 145C ask-side flow into IV-rank 97; sell the 5/29 earnings vol via a defined-risk iron condor 150P/200C, harvesting the +13.3% VRP and the $160 gamma magnet." |
| risk-monitor | RANGE (short bias > $160) | 2 | 1-5d | "Size HALF per UW TRANSITIONAL guidance; the bullish call tape is unconfirmed by dark pool, OI, composite, and historical backtest — sell IV via 5/22 or 5/29 iron condor $150/$165, never naked long debit into 5/27 earnings." |

**Tally:**
- LONG: 1 (sweep-tracker)
- SHORT: 1 (contrarian-scanner)
- NEUTRAL/lean-short-vol: 1 (accumulation-hunter)
- RANGE/short-vol: 2 (earnings-scout, risk-monitor)
- **Effective short-vol / fade alignment: 4 of 5** (accumulation, contrarian, earnings, risk all advocate selling premium or fading)
- **Average conviction: 2.6 / 5**

## Per-agent details

### accumulation-hunter [AGENT:accumulation-hunter]

```
VERDICT
- bias: NEUTRAL (lean SHORT-VOL / fade-the-debit-bull)
- conviction: 2
- horizon: 1-4w (through 5/27 earnings + IV crush)
- key_levels:
    support: $151-$152.50 (per phase-2-dark-pool.md, 5-day DP cluster
             absorbed ~$59M at $151.46-$152.94)
    resistance: $160 (per phase-4-structure.md, $2.31B net GEX wall)
    invalidation: close below $150.74 on volume (breaks both DP support
                  cluster AND 5/22 150P put-write floor) OR break above
                  $170 ($855M secondary GEX cap)
- top_signal: BLOCK-tier ($1M-$10M) buy_ratio = 0.304 on $16.7M premium —
              institutions were 2.3× net SELLERS on the largest individual
              prints while phase-1's call buyers paid ask; AND SNOW is
              ABSENT from bullish_signal_confluence top 20 (per phase-7).
- top_risk: A positive 5/27 earnings surprise combined with phase-4's
            +$113.8B call-heavy DEX would force violent dealer-buy hedging
            through the $160 wall toward $170 — being short here gets run
            over.
- one_line_take: This is not quiet accumulation — it is dressed-up
                 distribution; institutions are selling stock to dealer
                 hedgers while writing strangles ($150P/$180C/$200C per
                 phase-3) to harvest 92nd-percentile IV into earnings,
                 and the phase-5 bullish-flow backtest of 20% win rate
                 confirms the debit-call buyers are the patsy.
```

### contrarian-scanner [AGENT:contrarian-scanner]

```
VERDICT
- bias: SHORT (fade via premium-sell / defined-risk bear structure)
- conviction: 3
- horizon: 1-4w (through 5/27 earnings + 5/29 IV crush)
- key_levels:
    support: 154.56 (ZGL) / 151-152.50 (5-day DP absorption)
    resistance: 160 (primary $2.31B GEX magnet) / 170 (secondary)
    invalidation: spot reclaim and HOLD above 170 on volume OR DP block
                  buy_ratio flipping >0.6 with positive earnings reaction
- top_signal: Bullish_flow backtest 20% win rate / avg move -1.07%
              over last 5d (phase-5-historical.md) — the exact pattern
              firing on SNOW today has been a CONTRARIAN fade 8 of 10
              times.
- top_risk: Dealer DEX +$113.8B forces mechanical buying on any rally;
            positive 5/27 surprise could trigger vanna+dealer-hedge
            squeeze through $170 before the fade resolves.
- one_line_take: Consensus crowded long into rich 92nd-pctile IV with
                 block-tier DP selling (0.304), UW MIXED 1.82%, and a
                 backtest-failed bullish-flow signal — fade the
                 euphoria, sell the IV crush.

Aligned fade signals (4): (1) P/C z-score -1.59 + complacent skew 0.982;
(2) bullish_flow backtest 20% win rate; (3) SNOW absent from
bullish_signal_confluence top 20 at min_score=1; (4) BLOCK-tier DP
buy_ratio 0.304. Tech sector -$151M outflow + RBC PT $245→$220 add
macro/analyst pressure. Express via 5/29 short call spread or
earnings-vol short strangle, not naked short.
```

### sweep-tracker [AGENT:sweep-tracker]

```
VERDICT
- bias: LONG
- conviction: 3
- horizon: 1-5d
- key_levels:
    support: 154.56 (ZGL, hard invalidation); deeper 151-152.50 (5d DP
             absorption $59M)
    resistance: 160 (gamma magnet $2.31B GEX) then 170 (secondary $855M)
    invalidation: spot close < $154.56 on volume (regime flips
                  short-gamma)
- top_signal: The 15:10Z Jun-26 $145C ask block (467 ct @ $23.60, $1.10M,
              delta 0.67, vol/OI 314.67 on $2.10M aggregated strike
              premium) was paid up *into* the rally with same actor
              likely adding 6/26 $210C (+788 OI fresh) — a 145/210 call
              spread construction implying conviction SNOW > $160 in 1-4
              weeks.
- top_risk: Phase-5 bullish_flow backtest is 20% win rate / -1.07% avg
            move AND phase-2 BLOCK-tier DP buy_ratio 0.304 (institutions
            distributing into the rally) — the sweep cohort is being
            faded by share-level institutions.
- one_line_take: Aggressive 6/26 $145C ask sweep plus DEX +$113.8B
                 mechanical dealer bid argues for a quick squeeze to
                 the $160 gamma magnet, but size half and exit before
                 5/27 earnings IV crush.
```

### earnings-scout [AGENT:earnings-scout]

```
VERDICT
- bias: RANGE (with short-vol tilt)
- conviction: 3
- horizon: 1-4w (through 5/27 earnings + 5/29 IV crush)
- key_levels:
    support: $151-$152.50 (5-day DP cluster $59M absorbed; +$150 put-
             write OI)
    resistance: $180 (dealer headwind ceiling, +929 OI 6/18 180C bid-
                side); secondary $170 ($855M GEX)
    invalidation: spot < $154.56 ZGL on close — flips regime negative-
                  gamma, breaks short-vol thesis
- top_signal: 5/29 IV kink at 107.6% vs 5/22 71.2% and 6/18 84.9%
              combined with IV rank 97 and VRP +13.3% prices a binary
              earnings move that is structurally rich versus the 20%
              historical win-rate of the bullish-flow signature.
- top_risk: Long-gamma regime is only 2 sessions old (5/14 flip) and the
            prior 4/29→4/30 flip reverted next day — a cohort miss (ZS
            5/26) could blow out 5/29 IV further and squeeze short-vol
            structures before the crush.
- one_line_take: Don't chase the 145C ask-side flow into IV-rank 97;
                 sell the 5/29 earnings vol via a defined-risk iron
                 condor 150P/200C, harvesting the +13.3% VRP and the
                 $160 gamma magnet.

Suggested structure: SELL VOL — 5/29 iron condor short 150P / short 180C,
wings 145P / 195C; max risk capped, harvests IV crush + $160 GEX magnet.
Skip naked debit straddles (overpaying 92nd-pctile IV) and skip
directional debit calls (bullish-flow 20% win rate).
```

### risk-monitor [AGENT:risk-monitor]

```
VERDICT
- bias: RANGE (range-trade $150-$165 into earnings, with tactical short-
        bias overlay above $160)
- conviction: 2
- horizon: 1-5d
- key_levels:
    support: $154.56 (ZGL) / $151-$152.50 (5-day DP cluster $54M absorbed)
    resistance: $160 (gamma magnet $2.31B GEX) / $170 secondary
    invalidation: close < $154.56 on volume (regime flips short-gamma)
                  OR close > $162.50 cleanly (breaks dealer wall complex)
- top_signal: bullish_flow backtest = 20% win rate, avg move -1.07% over
              the last 5d — the exact pattern firing on SNOW today is a
              contrarian fade.
- top_risk: GEX regime is 2 sessions old and the only precedent
            (4/29→4/30) reverted next day; combined with Tech sector
            -$151M outflow and BLOCK-tier DP buy_ratio 0.304, a long
            here is fighting institutional supply on a fragile dealer
            regime into hot CPI / 4.59% 10y multiple compression.
- one_line_take: Size HALF per UW TRANSITIONAL guidance; the bullish
                 call tape is unconfirmed by dark pool, OI, composite
                 (MIXED 1.82%) and historical backtest — sell IV via
                 5/22 or 5/29 iron condor $150/$165, never naked long
                 debit into 5/27 earnings.
```

## Disagreements

The lone directional-long voter is **sweep-tracker** (LONG, conviction 3, 1-5d).

**sweep-tracker's top_signal:** "The 15:10Z Jun-26 $145C ask block (467 ct @ $23.60, $1.10M, delta 0.67, vol/OI 314.67 on $2.10M aggregated strike premium) was paid up *into* the rally with same actor likely adding 6/26 $210C (+788 OI fresh) — a 145/210 call spread construction implying conviction SNOW > $160 in 1-4 weeks."

This is the only agent that takes the directional bullish flow signal at face value. However:
- Sweep-tracker explicitly flags the 20% win rate and BLOCK-tier DP selling as their own top_risk.
- Their horizon is short (1-5d) and explicit guidance is "size half / exit before earnings."
- They target the **$160 GEX magnet**, the same resistance level all 5 agents agree on.

**Net interpretation:** sweep-tracker is voting for a short, defined exit "to the gamma magnet" trade, NOT a "ride through earnings" trade. When you stack their actual trade thesis (squeeze to $160 in 1-5 days, exit before earnings, half size) onto the other 4 agents' "sell IV through earnings" thesis, they are **not as contradictory as the bias labels suggest**. A trade that's long delta to $160 and then converts to short vol through earnings is consistent with both views.

## Tool errors

No MISSING agents. All 5 sub-agent types were available.

## Verdict for downstream phases

- **Plurality bias:** **RANGE / SHORT-VOL** (4 of 5 agents). One lone LONG with short horizon and explicit exit before earnings.
- **Average conviction:** 2.6 / 5 (moderate-low — appropriate given fresh GEX regime, 20% historical win rate, mixed UW composite).
- **Three highest-quality signals across all agents (cited by 3+ agents):**
  1. **`bullish_flow` backtest win rate = 20%, avg move -1.07% over 5d** [HIST:signal_backtest] — cited as top_signal or top_risk by 4 of 5 agents. This is the dominant historical-edge signal.
  2. **BLOCK-tier DP buy_ratio = 0.304** [DP:block_stratified] — cited by 4 of 5 agents. The clearest single-day institutional-distribution signature.
  3. **$160 = $2.31B GEX magnet** [STRUCT:gex] — cited by 5 of 5 as primary resistance / mean-revert target. Unanimous.
- **Top trade structures surfaced:**
  - **5/29 iron condor short 150P/180C, wings 145P/195C** (earnings-scout, refined by risk-monitor to $150/$165 width) — captures VRP +13.3%, harvests 92nd-pctile IV crush, defined-risk, primary "consensus trade" of phase 8.
  - **5/29 short call spread (e.g., short 170/180 or 180/200)** (contrarian-scanner) — pure short-side fade, defined-risk.
  - **Tactical long to $160 via 6/26 145/210 call spread** (sweep-tracker, conviction 3) — half size, take profit at $160, exit before 5/27 earnings.
- **Open questions surfaced by agents:**
  - Will ZS earnings 5/26 (day before SNOW) move SNOW IV up or down via cohort sympathy? (earnings-scout)
  - If GEX regime reverts on Monday 5/18 (the 4/29→4/30 precedent), what is the new ZGL and does the entire structural thesis change? (earnings-scout, risk-monitor)
  - Is the phase-1 $145C buyer the same actor as the phase-3 6/26 $210C buyer? (sweep-tracker speculated yes; unverifiable without trade-level identity data)
