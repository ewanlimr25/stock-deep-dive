# Phase 8 — Multi-Agent Analyst Desk

## Summary

Five specialist desk agents ran in parallel on the packed phases 1–7c context. The
net is a **cautious-constructive consensus: 3 LONG / 2 NEUTRAL, zero SHORT, average
conviction 2.4 / 5.** Critically, **no agent took the short side** — even the
contrarian-scanner, whose explicit job is to find the fade, concluded the fade
**does not qualify** (the two cleanest contrarian gates fail to fire). The two
NEUTRALs are both **lean-long-tactical** (accumulation-hunter and risk-monitor),
not bearish — they withhold from LONG only because their specific lens (quiet
accumulation / clean risk) isn't satisfied, not because they see downside edge.

**Every agent converges on the same geometry and the same risk:**
- **Support $190** (positive-gamma node + 6/18 max-pain) → **$185** first OI shelf →
  air pocket to **$170/$160**.
- **Resistance $195 → $200** (stacked call walls, net +24.4k / +58.2k OI; the $200
  sweep magnet).
- **Invalidation: sustained close below $185** (unanimous — loses the only near
  floor, opens the air pocket; risk-monitor adds "or Tech sector-flow persistence
  breaking its inflow streak").
- **The one shared top-risk:** phase-2 institutional distribution (mega buy-ratio
  0.017, ~$1.05B sold into the pop, corroborated by `fz` Inst Trans −1.78%) on a
  thin floor in a narrow-breadth tape.

**Desk verdict: tactical LONG, small, defined-risk, $185 the line.** The bull case
(call sweeps → $200, +23.9% beat / cheap fwd P/E, Tech sector inflow, positive
gamma, short-covering fuel) is real but thin-edged; the bear case is a single (if
high-quality) signal — institutional selling — that 7b reframes as likely mechanical.

## Agent verdicts table

| Agent | bias | conv | horizon | one_line_take |
|-------|------|------|---------|---------------|
| accumulation-hunter | NEUTRAL (lean-long) | 2 | 1-5d | No quiet accumulation — big holders sold $1.05B into the pop; the long is a sector-rotation catch-up bet, not my signal. |
| contrarian-scanner | NEUTRAL | 2 | 1-5d | No table-pounding fade — thin-edge post-beat pop, not crowded euphoria; the one short-tell lacks P/C/IV/RSI/squeeze confirmation. |
| sweep-tracker | **LONG** | 3 | 1-4w | One-way call sweeps into a cheap post-beat laggard with squeeze fuel + sector inflow; swing toward $200 by 6/18-7/17, size small. |
| earnings-scout | **LONG** | 3 | 1-4w | Cheap laggard, accelerating beats, IV crushed cheap — buy the post-beat drift small/defined-risk; institutions selling, don't press. |
| risk-monitor | **LONG** (tactical, hedged) | 2 | 1-5d | Smart money handed retail stock into the pop in a 36%-breadth tape; take it small, half-size, respect $185 as the trapdoor. |

- **Tally:** LONG 3, NEUTRAL 2, SHORT 0. Avg conviction **2.4**. Horizons split
  1-5d (3) / 1-4w (2).

## Per-agent details

### accumulation-hunter — NEUTRAL (lean-long), conv 2, 1-5d
- support $190 / $185 · resistance $195 → $200 · invalidation: close below $185 on
  rising DP sell volume, or a $190 break that fails to find dealer dip-buying.
- top_signal: cash tape is DISTRIBUTION not accumulation — mega DP buy-ratio 0.017,
  block 0.098 ($1.05B ~90% sold, pinned at $191.10), and phase-5
  `dark_pool_accumulation` backtest = 0 signals → the accumulation thesis is
  structurally absent.
- top_risk: the selling is *informed* distribution not mechanical, and with no put
  support 191→185 the overhang bleeds the pop lower once positive gamma fades past
  6/18.
- Note: confirmed the 190C 6/5 build had prior-day bid>ask (call-writing signature);
  #2 OI build (160P) is genuine new put buying → two-way under a call surface.

### contrarian-scanner — NEUTRAL, conv 2, 1-5d
- support $190 / $185 · resistance $195 → $200 · invalidation: break+hold above $195
  kills the fade; daily close below $185 confirms a distribution-led fade.
- top_signal: the fade **doesn't qualify** — `price-vs-flow` divergence:false (price
  & flow aligned, net premium only +$6.88M), P/C z −1.92 labeled NORMAL → the two
  cleanest contrarian gates fail.
- Walked all 5 fade gates: P/C-extreme FAIL, price-flow-divergence FAIL,
  OI-unwind FAIL (OI being built), screener-disconnect points to "thin edge" not
  "crowd wrong," regime says don't fade strong inflow. **1 bearish signal (DP
  distribution) is a stand-aside, not a fade.**

### sweep-tracker — LONG, conv 3, 1-4w
- support $190 (gamma node + max-pain) · resistance $200 (sweep magnet = heaviest
  call wall) · invalidation: sustained close below $185.
- top_signal: 20/20 call sweeps, $26.3M, 54% ask, premium concentrated in 6/18+7/17
  ($16M) targeting $200 = the exact heaviest call wall (+58,153 OI), into the #1
  persistent sector inflow.
- Confirmed premium lives in the 6/18→7/17 monthlies (term-structure positioning,
  not a 0DTE chase) → horizon 1-4w.

### earnings-scout — LONG, conv 3, 1-4w
- support $190 → $185 · resistance $195 → $200 · invalidation: sustained close below
  $185 (voids PEAD-drift thesis).
- top_signal: accelerating beat streak (+3.7→+12.6→+23.9%) on fwd P/E 12.4 / PEG
  0.99 = textbook cheap-laggard PEAD-continuation, with bullish_flow backtest 60%
  (5d) / 72.9% (10d), avg +5–5.6%.
- top_risk: phase-2 distribution can cap the drift once dealer dip-buying fades past
  6/18 opex.

### risk-monitor — LONG (tactical, hedged) / lean-neutral, conv 2, 1-5d
- support $190 / $185 · resistance $195 → $200 · invalidation: close below $185, OR
  Tech sector-flow persistence breaking its +$11.6B inflow streak.
- top_signal: Technology is the single largest, most-persistent sector inflow
  (+$533.3M today, persistence 1.0, 5 sessions to +$11.6B); CRM the 0.88-correlated
  cheap laggard positioned to catch up.
- top_risk: institutional distribution on a thin floor (no support 191→185) in a
  36%-breadth regime where CRM's 0.88+ software correlation = zero shelter if tech
  reverses.
- **Risk overlay (carry to phase-9):** CRM/NOW/ADBE are effectively ONE bet
  (0.89/0.88/0.87 internal) — don't stack on an existing software long; size the
  cluster as one line, one stop. Fractional Kelly only (p≈0.60 is universe-pooled/
  in-sample — haircut it). DP distribution is **review/hedge, not cut**; cut trigger
  = close below $185. Watch the Tech persistence streak as the thesis engine.

## Disagreements

- **No agent dissents on direction** (0 short, 0 high-conviction anything). The only
  "disagreement" is LONG-vs-NEUTRAL, and it is a **conviction split, not a bias
  split**: the two NEUTRALs (accumulation-hunter, risk-monitor) are lean-long and
  withhold a LONG label only because their lens (accumulation / clean risk) isn't
  met. This is a 3-2 conviction split → MIXED-constructive, phase-9 targets ~0.55–0.65
  conviction with a defined-risk structure (per the phase-8 heuristic).

## Tool errors

- None. All five agent types available and returned. ~54 uw calls total across
  agents (each stayed near budget; mostly confirmations of existing phase data).

## Verdict for downstream

- **Plurality bias: LONG (3 of 5; 0 short).** Avg conviction across 5 agents **2.4**.
- **Three highest-quality signals across the desk:**
  1. `[AGENT:sweep-tracker]` 20/20 call sweeps, $26.3M, premium in 6/18+7/17 targeting
     $200 = the heaviest call wall (+58,153 OI) — directional positioning with a clear
     target. `[FLOW:sweeps]`/`[OI:oi-by-strike]`
  2. `[AGENT:earnings-scout]` accelerating beats (+3.7→+12.6→+23.9%) + fwd P/E 12.4 +
     bullish_flow backtest 60/73% = cheap-laggard PEAD-continuation. `[FUND:earnings_surprise]`/`[HIST:signal-backtest]`
  3. `[AGENT:risk-monitor]` Tech = #1 persistent sector inflow (persistence 1.0, 5
     sessions, +$11.6B); CRM 0.88-correlated catch-up candidate. `[MACRO:sector_flow_persistence]`
- **Open questions surfaced by agents (for phase-8b debate):**
  - Is the phase-2 dark-pool distribution **informed** (bearish) or **mechanical
    profit-taking into the beat** (benign)? — the single hinge of the whole dive.
  - Does the **call-writing signature** (190C prior-day bid>ask) plus 52%-volume-ask
    mean the bullish flow is thinner than the premium headline?
  - If LONG: outright vs defined-risk (call spread / collar) given the thin
    191→185 floor and the cheap complacent-skew puts?

## Upstream references

- phase-7-insights.md §Summary — engine voted DISTRIBUTION (32.9%); the desk
  **does not override it into a short** but reads the distribution as the top *risk*
  to a tactical long, not a thesis — consistent with phase-7b's reframing.
- phase-2-dark-pool.md / phase-7b-fundamentals.md — the "informed vs mechanical
  distribution" question every agent flagged is the explicit subject of phase-8b.

## Next phase

- phase-8b-debate.md (bull vs bear disconfirmation — adjudicate the informed-vs-
  mechanical distribution question head-on before the PM synthesis)
