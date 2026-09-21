# Phase 8 — Multi-Agent Analyst Desk

**Ticker:** CMPS
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T00:00:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-4-structure.md, phase-6-macro.md, phase-7-insights.md, phase-7c-sentiment.md

## Summary

Four desk agents ran in parallel (earnings-scout skipped — earnings 2026-07-30 is
>30d out). The desk is **strongly aligned on RANGE: 3 of 4 vote RANGE, the fourth votes
constrained-LONG (quarter-size, defined-risk)** — i.e. *no one is bearish, no one wants
to chase*. Average conviction **3.25/5**; horizon **unanimously 1–4w**. The shared thesis:
CMPS is a **fundamentally de-risked bull story that is already priced, crowded, and
dealer-pinned $11–$12** — so the near-term trade is range/defined-risk, and the
asymmetric upside is owning cheap optionality into the **Q3 Part-B / Q4 NDA catalyst**
that could break the $12 gamma wall on a volume spike. Every agent put **support $11.00–
$11.45, resistance $12.00–$12.24, and the $10→$9.02 ZGL as the downside trapdoor / hard
invalidation.** The risk-monitor's distinct contribution: the **CMPS/RDDT 0.746 cluster**
makes concurrent CMPS+RDDT+SYM "one beta-2.46 risk-on bet sized as three" → size down.

## Agent verdicts table

| Agent | bias | conviction | horizon | one_line_take |
|-------|------|-----------|---------|---------------|
| accumulation-hunter | RANGE | 3 | 1-4w | Real institutional bid, but accumulating at the *top* of the range, not under it — footprint says defend $11–12, not chase a breakout. |
| contrarian-scanner | RANGE | 3 | 1-4w | Crowd's euphoric and flow's quietly selling the rip, but P/C isn't a real extreme and dealers are pinning, not distributing — fade resistance, don't short the catalyst. |
| sweep-tracker | RANGE | 4 | 1-4w | No momentum trigger; flow is selling into strength under a positive-gamma pin — stand aside or fade $12, wait for the Q3 catalyst + volume spike to chase a breakout. |
| risk-monitor | LONG (constrained: ¼-size, defined-risk) | 3 | 1-4w | Right direction, dangerous concentration — cluster-and-crowd to quarter-size, debit-only; $10 is the line, below it this and RDDT fall as one. |
| earnings-scout | — | — | — | SKIPPED (earnings 2026-07-30, >30d out per phase rule). |

**Distribution:** RANGE 3 · LONG(constrained) 1 · SHORT 0 · NEUTRAL 0. Mean conviction 3.25.

## Per-agent details

### accumulation-hunter — RANGE, 3, 1-4w
- support 11.45 (5-day DP shelf; deeper base 10.56–10.86) · resistance 12.20–12.24 (supply + 52wk high) · invalidation: close >12.25 on fresh net-bullish/ask-side OI build → flips LONG; close <11.00 (below $11 wall) → flips SHORT.
- top_signal: "DP buy/sell ratio 5.22 (120k vs 23k shares, VWAP $11.98, 11 prints all at-or-above mid) is genuine institutional accumulation."
- top_risk: "Accumulation is buying INTO supply $12.0–12.2 at a 52-week high while IV rank is 12.25 and positioning is crowded-long — the move it front-ran (Phase 3 data + EO) is **already priced**; this is late/mature accumulation, not pre-move."

### contrarian-scanner — RANGE, 3, 1-4w
- support 11.45 · resistance 12.20 · invalidation: close >12.48 on expanding volume (gamma squeeze + short-cover) voids the fade; or flow flips decisively bullish.
- top_signal: "price_vs_flow DIVERGENCE — price +114.96% while flow bearish ($605.7k bearish vs $330.1k bullish), and the Jun $11 wall call is being UNWOUND (OI −753 on 2,761 vol) = crowd longs ringing the register at resistance."
- top_risk: "8.9% short interest / DTC 7.4 rising into a positive-gamma pin (84% GEX at $11) with Q3 Part-B + Q4 NDA — a single beat detonates a squeeze through $12.20."
- Note: the contrarian explicitly *checked itself* — P/C z-score −0.553 is NORMAL, **not** a euphoria extreme, so it downgraded from a directional short to a tactical fade-the-resistance.

### sweep-tracker — RANGE, 4, 1-4w
- support 11.00 · resistance 12.00 · invalidation: sustained close >12.20 on volume_ratio >2× (flips COVERED_CALL read into breakout demand), or close <11.00 breaking the GEX pin.
- top_signal: "Marquee Jul $13 call traded 1,632 sold on the bid vs 629 bought on the ask (2.6:1) + a 1,000-lot mid block — premium harvesting/overwriting, not aggressive upside accumulation."
- top_risk: "A surprise Q3 headline gaps it through the $12 wall before the +1.37M GEX $11 pin can mean-revert it, stranding short-vol/range positions."
- Adds: $13 is only a +87k GEX wall — dealers defend mild upside but there's *no fuel above $12* to self-sustain a breakout absent a catalyst.

### risk-monitor — LONG (constrained), 3, 1-4w
- support 11.00 / 10.56–11.45 · resistance 12.00–12.20 · invalidation: daily close <10.00 → ZGL 9.02 (short-gamma trapdoor).
- top_signal: "Healthcare net flow +$494M with 0.80 5-day persistence and no rotation out — CMPS sits in a sector being bought, not unwound."
- top_risk: "CMPS/RDDT 0.746 (+CMPS/SYM 0.651): holding all three is one beta-2.46 risk-on bet sized as three — they blow up together in a drawdown."
- **Explicit sizing math:** half-size (TRANSITIONAL regime) × one-step cut (phase-7c CROWDED_LONG) on beta-2.46/realized-146% = **quarter-size, defined-risk, debit-structured.** Confirmed UW corr tool false-negatived again (sectors Unknown); DuckDB matrix is authoritative.

## Disagreements

No bias *opposition* — the split is RANGE (3) vs constrained-LONG (1), both bullish-leaning,
neither bearish. The risk-monitor's LONG is **direction-only**; on *sizing* it is the most
conservative of the four (quarter-size), so it functionally agrees with the RANGE camp that
this is not a chase-the-breakout setup now. The genuine tension is **timing, not direction**:
own-it-now-small (risk-monitor) vs wait-for-the-Q3-trigger/fade-$12-meanwhile (sweep-tracker,
contrarian, accumulation-hunter). All four converge on defined-risk + the $11–12 range + the
$10/$9.02 invalidation.

## Tool errors

- `earnings-scout`: **SKIPPED** (not MISSING) — earnings 2026-07-30 >30d from as-of, per phase rule.
- risk-monitor re-confirmed UW `risk_portfolio_correlation` returns sectors "Unknown" and
  misses the CMPS cluster (known broken tool) — DuckDB phase-6 matrix used instead.

## Verdict for downstream phases

- **Plurality bias: RANGE (3 of 4)**, with the dissent a *constrained-LONG* (same direction,
  most conservative sizing) → net desk read **range-bound now, bullish-biased into the Q3
  catalyst, defined-risk, sub-half size.** No bear in the room.
- **Average conviction across the 4 non-skipped agents: 3.25/5.** Per phase-8 heuristics, a
  3–2-style split → MIXED → phase-9 targets ~0.55–0.65 conviction and a **defined-risk
  structure** (here it's 3-RANGE/1-LONG, even more cohesive on "defined-risk").
- **Three highest-quality signals across agents:**
  1. *(sweep-tracker, phase-1)* Jul $13 call **1,632 sold / 629 bought (2.6:1) + 1,000-lot mid
     block** = premium harvesting/overwriting, not upside accumulation `[FLOW:sweeps]` `[AGENT:sweep-tracker]`.
  2. *(risk-monitor, phase-6)* **CMPS/RDDT 0.746 cluster** (+SYM 0.651) — concurrent blueprints
     are not independent; size down `[MACRO:corr DUCKDB]` `[AGENT:risk-monitor]`.
  3. *(accumulation-hunter, phase-2)* DP **buying into supply $12.0–12.2 at the 52-week high** —
     mature/late accumulation, the front-run move is already priced `[DP:largest]` `[AGENT:accumulation-hunter]`.
- **Open questions surfaced by agents (for phase-8b/9):**
  - Is the right expression **own-small-now** (risk-monitor) or **wait-for-the-Q3-trigger /
    buy-the-$11-retest** (the three RANGE agents)? → phase-9 entry timing.
  - The **upside trigger is explicit**: a sustained close >$12.20 on volume_ratio >2× (a Q3
    Part-B/NDA headline) flips RANGE→LONG and squeezes the 8.9%/DTC-7.4 short base through the
    thin >$12 gamma. The **downside trigger** is a close <$10 → $9.02 ZGL (short-gamma trapdoor).
  - Can the cheap IV (rank 12, VRP −0.71) be *owned* (long calls/call-spread into Q3) rather
    than the range *sold* — i.e. structure the trade to be long the catalyst optionality while
    respecting the pin? → phase-9 structure choice.
