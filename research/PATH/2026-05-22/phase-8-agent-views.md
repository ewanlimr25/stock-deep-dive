# Phase 8 — Multi-Agent Analyst Desk

**Ticker:** PATH (UiPath Inc.)
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T00:00:00Z
**Upstream phases cited:** phase-1 … phase-7c (all)

## Summary

Five specialist agents ran in parallel. **Plurality = 2 LONG + 3 NEUTRAL; conviction
average 2.6/5; NO agent is SHORT.** The desk is unanimous on three things: (1) the
persistent bearish options flow is **short-hedging / premium-selling, not directional
conviction** — do not chase the downside; (2) into a 6-day binary with ~30% short interest,
this is a **defined-risk, half-size** trade, not a leveraged directional bet; (3) the
operative levels are **support $10.50 (neg-GEX gate), resistance/pin $11.00, invalidation =
sustained close below $10.50**. The genuine split is **expression**: the
accumulation-hunter and contrarian-scanner favor a **long-biased squeeze lean** (smart-money
accumulation vs a 30%-short crowd), while the earnings-scout and risk-monitor favor
**selling the 140% 5/29 IV bubble** (defined-risk vol-harvest, VRP +43.7). The sweep-tracker
sits in between (neutral, lean-long, don't short). Phase-8b must resolve squeeze-lean vs
vol-harvest.

## Agent verdicts table

| Agent | bias | conv | horizon | one_line_take |
|-------|------|------|---------|---------------|
| accumulation-hunter | **LONG** | 3 | 1-4w | Institutions soaking up a crowded short into earnings; real accumulation but a defined-risk lottery — size half |
| contrarian-scanner | **LONG** | 3 | 1-4w | Fade the 30%-short crowd, not the small bearish-flow crowd; DP accumulating a squeezable float, $11 wall caps until earnings |
| sweep-tracker | NEUTRAL (lean long) | 2 | 1-5d | The "bearish campaign" is short-hedging + put-writing dressed as momentum; no volume confirm — don't chase downside |
| earnings-scout | NEUTRAL (range) | 3 | 1-5d | Sell the 140% weekly bubble, not the stock — defined-risk strangle/condor outside ±11.8%, size half |
| risk-monitor | NEUTRAL (vol-sell, mild up) | 2 | 1-5d | Rich vol on a beaten-down small-cap over a short-gamma trapdoor — harvest premium, half size, don't bet direction |

## Per-agent details

### accumulation-hunter — LONG, 3, 1-4w
- support $10.50 · resistance $11.00 · invalidation: close below $10.50 (enters neg-GEX
  pocket, voids accumulation thesis).
- top_signal: "Phase-2 block buy_ratio 1.0 ($13.95M, zero sells) + intraday at-ask $11 buys
  (~$2.3M), cross-confirmed by Phase-7 accumulation 6.11× — institutions absorbing supply on
  the $10.50–$10.65 shelf."
- top_risk: a guidance miss into 28–31% short interest cuts through $10.50 into the neg-GEX
  pocket before the squeeze fires.

### contrarian-scanner — LONG, 3, 1-4w
- support $10.50 · resistance $11.00 · invalidation: close below $10.50 on rising bearish-
  sweep volume, OR a post-earnings gap-down confirming a fundamental miss.
- top_signal: "Phase-2 ACCUMULATION (block 1.0, 6.11×) sits opposite a ~30% crowded short
  (5.2 DTC) — smart money absorbing the supply the crowd is pressing into a 6-day catalyst."
- top_risk: COMPLACENT skew + neg-GEX below $10.50 means downside is underpriced; a miss
  breaks support and proves the shorts right.
- (Verified via tools: oi_decrease shows downside hedges being *lifted* at the margin; P/C
  z-score NORMAL — no P/C extreme; regime range-bound enough to permit a fade.)

### sweep-tracker — NEUTRAL (lean LONG), 2, 1-5d
- support $10.50 (then $9.47 trough) · resistance $11.00/$12.00 · invalidation: sustained
  close < $10.50 on genuine ask-side put-sweep expansion + volume_ratio > 2×.
- top_signal: "sweep_persistence flags 5/5 bearish ($6.01M), but the largest print
  ($525,780 2027 $10P) is `no_side` long-dated and near-term 06-18 $11 puts are bid/mid
  (written) — premium collection + short-hedging, not aggressive buying." PATH not in
  volume_vs_average at 1.5× → no fresh volume surge confirming directional urgency.
- top_risk: a genuine fundamental miss lets price fall through the $10.50 neg-GEX shelf,
  validating the sweeps after the fact.

### earnings-scout — NEUTRAL (range), 3, 1-5d
- support $10.50 · resistance $11.00 · invalidation: sustained break < $10.50 (→ air pocket
  toward $8.50–$10 put wall) OR a gap-up beat igniting the short squeeze through $11.50–$12.
- top_signal: "Phase-4 — 5/29 IV 140% backwardated ~1.55× over 31-DTE LEAPs (~90%) with
  +$20–22M long gamma pinning $11; the weekly vol bubble is structurally overpriced, crush is
  mechanical (vanna negative → dealer selling on IV drop)."
- top_risk: 28–31% short float + agentic-AI revisions mean a beat-guide gaps PATH through the
  implied move and squeezes a short-vol structure past the $11 pin — and high-IV-rank
  realizes the move ~40–60% of the time (it doesn't always crush).

### risk-monitor — NEUTRAL (vol-sell, mild upside), 2, 1-5d
- support $10.50 · resistance $11.00 then $12–$13 cap · invalidation: close below $10.50
  pre-print, OR a defined-risk vol-seller breached beyond ±11.8% post-print.
- top_signal: "Phase-5 VRP +43.7 vol pts (IV 98.7 vs realized 55, IV %ile 100) + Phase-4
  5/29 140% bubble — the repeatable edge is structural premium-selling, not direction
  (bearish_flow backtest 28.6%, DP-accumulation null sample)."
- top_risk: "~11.8% implied move atop a neg-GEX air pocket below $10.50 → a bad print gaps
  through dealer short-gamma toward $8.5–$9; same-day NTAP earnings + a tech-saturated
  watchlist + TRANSITIONAL half-size regime make this a correlated, event-clustered bet, and
  the DEX +$28.2M bid reverses into selling on the IV crush." Correlation coefficients
  unusable (sectors "Unknown") — cluster inferred from watchlist (tech-heavy) + concurrent
  NTAP (same-day)/SYM (automation).

## Disagreements

No bias disagreement — **no agent is SHORT**, and all reject chasing the bearish flow. The
divergence is **expression**:
- **Directional-long-squeeze camp** (accumulation-hunter, contrarian-scanner): lean long to
  capture a beat-driven squeeze of the ~30% short float; horizon 1-4w.
- **Vol-harvest-neutral camp** (earnings-scout, risk-monitor): sell the structurally
  overpriced 140% 5/29 IV with a defined-risk neutral structure; horizon 1-5d (through the
  crush). sweep-tracker bridges (neutral/lean-long, don't short).
- The tension: a long-biased structure pays on a squeeze but loses on a miss-driven air
  pocket; a short-vol structure pays on the IV crush + pin but is exposed to the squeeze tail
  beyond ±11.8%. **8b must adjudicate.**

## Tool errors

None. No MISSING agents — all five subagent types available. risk-monitor noted
`risk_portfolio_correlation` returns unusable coefficients (sectors "Unknown") — cluster read
is inferred, not measured.

## Verdict for downstream

- **Plurality bias:** **NEUTRAL-to-LONG, NOT short** — 2 LONG + 3 NEUTRAL (all neutrals
  lean long / vol-sell), 0 SHORT.
- **Average conviction:** **2.6/5** across all five (non-MISSING).
- **Three highest-quality signals:**
  1. DP block buy_ratio 1.0 ($13.95M) + 6.11× accumulation **opposite a ~28–31% short float**
     → squeeze fuel `[DP:block_stratified]` × `[SENT:short_interest]`.
  2. The bearish flow **decoded as short-hedging/premium-selling**, not momentum: largest
     print `no_side` long-dated; near-term puts bid-side written; **no volume-vs-avg surge**
     `[FLOW:sweeps]` · `[FLOW:sweep_persistence]`.
  3. 5/29 IV **140% backwardated** vs ~90% at 31DTE + **VRP +43.7** + **$11 long-gamma pin**
     → structurally overpriced vol; sell-premium is the repeatable edge `[STRUCT:iv_term_structure]` · `[HIST:vrp]`.
- **Open questions for 8b/9:**
  - **Squeeze-lean vs vol-harvest** — the central expression question.
  - The **binary downside** ($10.50 neg-GEX gate → $8.5–$9 air pocket) if the 05-28 guide
    disappoints; how to cap it.
  - **Event clustering** (NTAP same-day 5/28; tech-crowded tape) under TRANSITIONAL half-size.
