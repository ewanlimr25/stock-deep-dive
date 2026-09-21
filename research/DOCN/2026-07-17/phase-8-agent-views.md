# Phase 8 — Multi-Agent Analyst Desk

**Ticker:** DOCN
**As-of date:** 2026-07-17
**Generated:** 2026-07-20T03:00:00Z
**Upstream phases cited:** phase-1 through phase-7c (all packed into each agent)

## Summary

Five specialists, **zero directional votes.** Plurality is **RANGE (3)** with
**NEUTRAL (2)** — not a single LONG or SHORT. Average conviction **2.2/5**. The
desk is unanimous that DOCN is a **range / premium-selling setup into 8/4
earnings**, not a directional trade: the "bullish divergence" is forced-technical
selling (Russell + dilution) absorbed by a long-gamma, pinned tape — no
institutional accumulation, no sweep conviction, and a max-bullish Street that is
*unwinding* (the $985K 180C print closed OI) while insiders sell. Both event-aware
agents (earnings-scout, risk-monitor) add the crucial caveat: **sell the rich vol,
but size for an 8/4 gap, not just a fade** (guidance-cut downgrade risk + vanna
vol-crush). Levels are tightly agreed: **support $115, resistance $128, pin $120.**

## Agent verdicts table

| Agent | bias | conviction | horizon | one_line_take |
|-------|------|-----------|---------|---------------|
| accumulation-hunter | NEUTRAL | 2 | 1-4w | "Every lane that should light up on real accumulation stayed dark; long-gamma range, not a stealth base." |
| contrarian-scanner | RANGE | 3 | 1-4w | "Everybody's bullish on paper and nobody's actually buying — sell the edges, not the direction." |
| sweep-tracker | NEUTRAL | 1 | intraday | "Biggest print's bullish but it's a single ticket buried in hedges; fade the noise, wait for earnings." |
| earnings-scout | RANGE | 3 | 1-4w | "Rich vol, pinned tape, priced-in crush — sell premium into 8/4, but size for a gap, not just a fade." |
| risk-monitor | RANGE | 2 | 1-4w | "No cluster risk, but two vol bombs (FOMC 7/29, earnings 8/4) argue small, defined-risk premium-selling only." |

## Per-agent details

### accumulation-hunter — NEUTRAL, conv 2, 1-4w
- key_levels: support $117 (DP 5d cluster $38.07M) / $115 (put wall 918 OI); resistance $123.3 / $126.3 (DP supply) / $128 (call wall); invalidation daily close < $115, or a fresh mega-tier DP buy + ≥500-ct OI build (neither exists).
- top_signal: "No lane confirms accumulation — DP large-tier sell-leaning (buy 0.468), biggest OI change only +206, the $985K 180C print OI-reducing −430, insiders selling (MSPR −98.9/−77.8) — three lanes independently say NOT accumulation."
- top_risk: "Russell rebalance + $500M dilutive offering create technical non-informational selling that *could* mask accumulation — but no mega-tier DP prints / structural OI build support that."

### contrarian-scanner — RANGE, conv 3, 1-4w
- key_levels: support $115 (put wall); resistance $128 (call wall / 7/17 max-pain); invalidation daily close beyond $115 or $128 on volume, or an 8/4 gap that overwhelms long-gamma.
- top_signal: "Street max-bullish (0 sells, buy 10→11, PTs $155–185) while insiders dump (MSPR −98.9/−77.8) and the $985K 180C was buy-to-close (−430 OI) — the crowd's bullish bet is unwinding, not building."
- top_risk: "No clean capitulation either way — P/C z +0.11 NORMAL (not panic), ~15% SI with easy borrow (not a squeeze); the range fade bets on dealer gamma holding, which 8/4 mechanically breaks."

### sweep-tracker — NEUTRAL, conv 1, intraday
- key_levels: support $115; resistance $128; invalidation close outside $115–128 on volume, or a repeat multi-session directional skew (currently "mixed" 4/5).
- top_signal: "The lone big $180C Nov sweep is offset same-instant (16:58:10) by $175P Oct + $100P Sep buying, and DOCN is on zero smart-money/sweep-ratio leaderboards — no directional cluster to trade."
- top_risk: "Chasing the 180C as 'smart money' ignores it's one ticket buried in hedges (123C/115P writing) inside a long-gamma pinned regime — not urgency."

### earnings-scout — RANGE, conv 3, 1-4w
- key_levels: support $115 (implied-move floor); resistance $120–122 (max-pain pin / IM ceiling); invalidation IV rank < 50 pre-print (thesis dead) OR spot > $130 pre-earnings (pin fails).
- top_signal: "IV rank 99 / VRP +0.434 (IV 114.6% vs realized 71.2%) + term hump peaking 8/7 (117.9%) — options price a crush that hasn't happened; long-gamma call-heavy book near $120 sets up vanna selling once IV mean-reverts post-print."
- top_risk: "FY26 guidance already implies ~50% H2 EPS deceleration while analysts stay uniformly bullish (0 sells, $155–185 PTs) — an 8/4 confirmation triggers a downgrade cascade that overwhelms the vol-crush edge with a directional gap."

### risk-monitor — RANGE, conv 2, 1-4w
- key_levels: support $115 (put wall); resistance $128 (call wall / max-pain); invalidation close < $110 (below period low $111.13) or close > $130 with rising IV.
- top_signal: "Regime TRANSITIONAL/CHOPPY, UW guidance 'half size, defined-risk, iron condors in range,' reinforced by DOCN's own long-gamma pin to $120 into 8/4."
- top_risk: "Call-heavy book at IV rank 99 (vanna −260) → post-8/4 vol-crush vanna selling, compounding the earnings binary and 7/29 FOMC hike-tail — long-vol/long-delta must be sized for the gap, not the ±1.8% front move."
- **Correlation confirm:** re-ran `uw risk portfolio-correlation` — **DOCN absent from all high-corr pairs** (NOW/PATH 0.798, PATH/SHOP 0.707, NOW/SHOP 0.58). **No cluster for DOCN.**

## Disagreements

- **No directional dissent** — no agent voted LONG or SHORT. The only spread is
  NEUTRAL (accumulation-hunter, sweep-tracker) vs RANGE (contrarian, earnings-scout,
  risk-monitor), which are both non-directional and mutually consistent (NEUTRAL =
  "nothing to trade"; RANGE = "trade the $115–128 edges / sell vol").
- **sweep-tracker is the most cautious** (conv 1, intraday, "wait for earnings") —
  its dissent is on *tradeability now*, not direction; it wants to wait for 8/4.

## Tool errors

- None. All five agent types available and returned structured verdicts. (Agents
  made 0–6 supporting `uw` calls each; risk-monitor re-confirmed correlation.)

## Verdict for downstream

- **Plurality bias:** **RANGE (3) / NEUTRAL (2)** — **0 LONG, 0 SHORT.** Treat as a
  strong non-directional consensus; per phase-8 heuristics a 3-2 split → MIXED,
  defined-risk structure, phase-9 conviction ~0.55–0.65 band **but here both sides
  of the split are non-directional**, so the real read is "no directional edge —
  premium-selling/range only."
- **Average conviction:** **2.2/5** across all five (none MISSING).
- **Three highest-quality signals:**
  1. The $985K 180C Nov print was **OI-reducing (−430) = buy-to-close**, not fresh
     bullish conviction `[AGENT:accumulation-hunter → phase-3]` — the one bullish
     standout is falsified.
  2. **Street max-bullish (0 sells, PTs $155–185) while insiders dump (MSPR
     −98.9/−77.8)** — bullish positioning unwinding `[AGENT:contrarian-scanner → phase-7b/7c]`.
  3. **IV rank 99 / VRP +0.434 / term hump 8/7 117.9%** = priced-in crush → sell
     premium, but **size for the 8/4 gap** `[AGENT:earnings-scout → phase-4/5]`.
- **Open questions surfaced:**
  - The dominant tension: sell rich vol into 8/4 **vs** protect against a
    guidance-cut directional gap (downgrade cascade off a max-bullish Street).
    Phase-9 must resolve structure choice around this (defined-risk, not naked).
  - Does dealer long-gamma hold the $115–128 range until 8/4, or does the 7/29 FOMC
    hike-tail break it early? (both event-aware agents flag it).
