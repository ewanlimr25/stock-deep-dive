# Phase 8 — Multi-Agent Analyst Desk

**Ticker:** FSLR
**As-of date:** 2026-07-31
**Generated:** 2026-07-31
**Upstream phases cited:** `phase-1-flow.md`, `phase-2-dark-pool.md`, `phase-3-positioning.md`, `phase-4-structure.md`, `phase-5-historical.md`, `phase-6-macro.md`, `phase-7-insights.md`, `phase-7b-fundamentals.md`, `phase-7c-sentiment.md`

## Summary

**Four agents, four independent mandates, and near-total convergence: no one
wants to be directionally long or short FSLR here.** Three of four returned
**RANGE**, one returned **NEUTRAL**. **Zero LONG. Zero SHORT.** Average
conviction is **2.0 / 5** — every agent independently landed on 2.

The agreement on levels is tighter than the agreement on bias:
**all four named 205.83 as support and 217.50 as resistance**, and all four
named **a close below 205.83** as the invalidation. That is four different
analytical lenses — accumulation detection, crowd-fade, momentum, and
portfolio risk — converging on the same two prices without coordination.

Their reasoning diverges usefully even where their conclusions agree.
The **accumulation-hunter** confirmed the buying is real but reframed it as
*"selective repositioning at the top of a base, not a stealth accumulation
campaign"* — and made the sharpest observation of the phase: **this is two
different institutional cohorts on opposite sides, not one accumulating
story.** The **contrarian-scanner** did the most valuable negative work,
refusing to manufacture a fade: *"No crowd, no fade"* — and then relocated the
real tension to **analysts versus price**, not longs versus shorts. The
**sweep-tracker** accepted the block as a genuine opening buy on phase-2's
hedge evidence yet declined to call it momentum: *"one real block plus a
wall-test rejection is a level to watch, not a trend to chase."* The
**risk-monitor** did the arithmetic the desk actually needs, and concluded the
three size cuts are **genuinely independent and multiplicative** — roughly
**1/8 to 1/5 of a normal unit, defined-risk only.**

`earnings-scout` was **skipped by specification** — earnings are 2026-10-29,
about 90 days out, well beyond the 30-day trigger.

## Agent verdicts table

| Agent | bias | conviction | horizon | one_line_take |
|-------|------|-----------:|---------|---------------|
| accumulation-hunter | **RANGE** | 2 | 1-5d | Real but modest regular-session buying (0.05% of float, ex-hedge) into a name where the LEAP holder trimmed, the C-suite sold, and analysts cut targets the same day — selective repositioning at the top of a base, not a stealth accumulation campaign; fade rallies into 214-217.5, respect the base at 205.83. |
| contrarian-scanner | **NEUTRAL** | 2 | 1-5d | No crowd, no fade — sentiment gauges sit at NORMAL across the board, so the real tension here is analysts vs. price, not longs vs. shorts; stand aside. |
| sweep-tracker | **RANGE** | 2 | 1-5d | One real block plus a wall-test rejection is a level to watch, not a trend to chase — mixed persistence says fade the pop into 214-217.5, don't buy the break until it actually clears. |
| risk-monitor | **RANGE** | 2 | 1-4w | Three independent, multiplicative cuts (macro half-size × insider CAUTION × analyst-revision CAUTION) cap this at ~1/8-1/5 unit, defined-risk only, invalidated on a 205.83 close. |
| earnings-scout | **SKIPPED** | — | — | Out of window — earnings 2026-10-29 (~90d), spec triggers only within 30d. |

**Distribution:** RANGE 3 · NEUTRAL 1 · LONG 0 · SHORT 0.
**Conviction:** 2, 2, 2, 2 → **mean 2.0, zero dispersion.**
**Level consensus:** support **205.83** (4/4) · resistance **217.50** (4/4) ·
invalidation **close below 205.83** (4/4).

## Per-agent details

### accumulation-hunter

```
VERDICT
- bias: RANGE
- conviction: 2
- horizon: 1-5d
- key_levels:
    support: 205.83
    resistance: 217.50
    invalidation: close below 205.83 (breaks the post-earnings base) or a
                  confirmed close above 217.50 on rising IV
- top_signal: Phase-2's session-decomposed dark pool shows regular-session
  buying flipping exactly at the earnings date (28.4%→64.2%→73.1%), with
  genuine ex-hedge accumulation of +51,936 shares (63.2% buy) plus a real
  28,000-share buy at $214.00 above the offer — corroborated by phase-3's OI
  BUILDING +184,105/10 straight days and phase-4's triple-confirmed $217.50
  gamma wall that capped today's 217.13 high exactly as predicted.
- top_risk: The 72,200-share "mega print" is a QCT dealer delta hedge, not
  conviction buying, and the largest options blocks (>500 lots, ask/bid 0.69)
  plus five C-suite officers selling pre-earnings and three analyst target
  cuts the same day are a distribution/de-risking signal running concurrently
  with the mid-size institutional buying — this is two different institutional
  cohorts on opposite sides, not one accumulating story.
- one_line_take: Real but modest regular-session buying (0.05% of float,
  ex-hedge) into a name where the LEAP holder trimmed, the C-suite sold, and
  analysts cut targets the same day — call it selective repositioning at the
  top of a base, not a stealth accumulation campaign; fade rallies into
  214-217.5, respect the base at 205.83.
```

**Assessment:** answered all three questions it was asked. It **confirmed** the
dark-pool regime flip is real (citing the 28.4 → 64.2 → 73.1 sequence and the
28,000-share $214.00 buy above the offer as evidence independent of the
hedge), **agreed** the 72,200-share QCT must be excluded from the accumulation
count, and **rejected** the unifying narrative — the LEAP trim and C-suite
selling are a *different* story from the block buying, not the same one. Its
size framing (**0.05% of float**) matches phase-2's computed +51,936 shares =
0.0512% of the 101.48M float exactly.

### contrarian-scanner

```
VERDICT
- bias: NEUTRAL
- conviction: 2
- horizon: 1-5d
- key_levels:
    support: 205.83
    resistance: 217.50
    invalidation: close above 217.50 (gamma wall clears) or close below
                  205.83 (base breaks)
- top_signal: phase-5's own admission — P/C z-score −0.825 is "extreme: NORMAL"
  and IV rank 81.94 is only the 39.4th self-percentile (phase-0.5/7c) — there
  is no crowd to fade; phase-7c confirms retail bought puts harder than calls
  (1.43 vs 1.12), ruling out the euphoria-into-distribution setup that would
  justify a bearish fade.
- top_risk: the trade this desk actually wants to fade is analyst opinion, not
  the options crowd — phase-7c shows three firms (WF/Truist/Bernstein) cut
  targets in unison after a beat, with Bernstein's $197 sitting 6.7% below
  spot and revenue/guidance both missing consensus — that's a real bear case
  resting on fundamentals, not a positioning extreme, so no options-flow fade
  thesis touches it.
- one_line_take: No crowd, no fade — sentiment gauges sit at NORMAL across the
  board, so the real tension here is analysts vs. price, not longs vs. shorts;
  stand aside.
```

**Assessment:** the most disciplined response of the four. Explicitly asked
whether the absence of a sentiment extreme means there is no contrarian trade,
it **said so plainly instead of manufacturing one** — the failure mode the
prompt was designed to test for. Its second contribution matters for phase 9:
it identifies that the genuine bear case (Bernstein $197, revenue miss,
guidance below consensus) is **fundamental, not positional**, and therefore
**cannot be neutralised by any options-flow argument.** That is a real
limitation on how far phases 1–2 can carry the thesis.

### sweep-tracker

```
VERDICT
- bias: RANGE
- conviction: 2
- horizon: 1-5d
- key_levels:
    support: 205.83 (dark-pool close/max-pain shelf, phase-2/phase-4);
             secondary 200 (put wall, net_gex −465,782)
    resistance: 217.50 (triple-confirmed gamma wall, net_gex +2,344,544 =
                78% of summed gamma, phase-4) — 214.00–217.50 is the
                congestion band
    invalidation: close below 205.83 (breaks the 12-session base) reopens the
                  downtrend; close above 217.50 with confirming volume flips
                  this to LONG
- top_signal: The 1,900-lot Aug-21 $230 call cross ($1.805M at the offer,
  vol/OI 7.6x) is a genuine opening buy — phase-2's dark pool independently
  confirms it via a 49-second-lag, 101.1%-match QCT delta hedge (dealer paid
  above ask, proving dealer is short calls / customer is long) — but
  sweep_persistence.dominant_direction is "mixed" across 4 of 5 sessions with
  $17.28M of premium producing zero price progress (211.93→211.03 over twelve
  sessions), and today's high stopped 0.17% short of the 217.50 wall before
  giving back 6.10 points.
- top_risk: A single cross print carries the entire bullish-delta conclusion
  (net customer delta swings from +$10.73M to roughly −$4.5M if reversed), and
  the 13:1 new-call skew sits atop a dealer short-gamma regime below 215.03
  where a failed breakout accelerates downside just as readily as a successful
  one accelerates upside.
- one_line_take: One real block plus a wall-test rejection is a level to watch,
  not a trend to chase — mixed persistence says fade the pop into 214-217.5,
  don't buy the break until it actually clears.
```

**Assessment:** the momentum specialist declined to call momentum, which is the
most informative possible answer from this seat. It accepted the block as
genuine on phase-2's hedge evidence but weighed **"mixed" persistence across
$17.28M and twelve flat sessions** as the stronger fact. It supplied the one
condition phase 9 most needs: **a close above 217.50 with confirming volume
flips this to LONG.** It also independently reproduced phase-1's own stated
fragility (the ±$15M delta swing on a single print's interpretation).

### risk-monitor

```
VERDICT
- bias: RANGE
- conviction: 2
- horizon: 1-4w
- key_levels:
    support: 205.83
    resistance: 217.50
    invalidation: Daily close below 205.83 (breaks the 12-session base +
                  phase-2/3 dark-pool/OI support shelf); confirmed/accelerated
                  on a close below 200 where dealer gamma turns decisively
                  negative (net_gex −465,762)
- top_signal: The three cuts are genuinely independent, not double-counting —
  7b's insider/cash-flow axis predates and is uninformed by 7c's post-print
  analyst-revision axis (insiders sold 07-29, before the 07-30 AMC revenue
  miss that drove the 07-31 target cuts), and the regime "half size" is a
  market-wide breadth/Fed input orthogonal to both — so they compound
  multiplicatively on an already-low base conviction (2-3/5 across phases 1-4,
  composite MIXED at 8.8%): 0.5 (regime) × ~0.75 (7b CAUTION) × ~0.75 (7c
  CAUTION) ≈ 0.28, further discounted for the sub-2.5/5 base conviction to
  roughly 1/8–1/5 of a normal unit — and dealers are short gamma below 215.03
  with cash burning (−$214.9M OCF, $2.4B→$1.7B in 6mo), so any size beyond
  that is unjustified without a defined-risk wrapper (credit spread/iron
  condor per phases 4-6's convergent premium-selling read).
- top_risk: [merged into top_signal above by the agent]
- one_line_take: Three independent, multiplicative cuts (macro half-size ×
  insider CAUTION × analyst-revision CAUTION) cap this at ~1/8-1/5 unit,
  defined-risk only, invalidated on a 205.83 close.
```

**Assessment:** answered the gate-stacking question decisively and with a
**temporal argument phase 7c did not make**: insiders sold on **2026-07-29**,
*before* the 07-30 AMC revenue miss that drove the 07-31 target cuts — so the
two CAUTIONs cannot be the same information reaching the market twice. The
regime cut is market-wide breadth and Fed policy, orthogonal to both. Its
multiplicative arithmetic (**0.5 × 0.75 × 0.75 ≈ 0.28**, discounted to
**1/8–1/5 unit**) is the most concrete sizing input produced anywhere in this
run and phase 9 should adopt it. *(Note: it transcribed net_gex at 200 as
−605,762/−465,762 in one field; phase-4's value is **−465,782**. Immaterial to
the conclusion.)*

## Disagreements

**There is no directional disagreement to report** — no agent took a bias
opposite the plurality. RANGE and NEUTRAL are adjacent readings, not opposed
ones: both decline a directional position, differing only on whether the
205.83–217.50 boundaries are tradeable (RANGE) or whether the right action is
to stand aside entirely (NEUTRAL).

Three second-order divergences are worth carrying forward:

1. **Is there a tradeable range, or nothing at all?** Three agents would
   trade the boundaries (fade 214–217.5, respect 205.83); the
   contrarian-scanner says *"stand aside."* Since RANGE with 1/8–1/5 sizing
   and NEUTRAL are nearly the same position in practice, this is a distinction
   phase 9 can resolve by structure choice rather than by direction.
2. **Horizon.** Three agents say **1-5d**; risk-monitor says **1-4w**. The
   short-horizon agents are anchored on the 217.50 rejection and the OPEX
   mechanics; risk-monitor is anchored on the 2026-08-21 expiry and the macro
   calendar. **Phase 9 should size to 1-4w and manage on 1-5d triggers.**
3. **What breaks the trade upward.** Only the sweep-tracker specified an
   *upside* flip condition — *"close above 217.50 with confirming volume flips
   this to LONG."* The accumulation-hunter treats a close above 217.50 **on
   rising IV** as an *invalidation* of the range rather than a long trigger.
   These are compatible but differently framed, and phase 9 should state which
   it means.

## Tool errors

**`MISSING: earnings-scout` — not a failure; skipped by specification.** The
phase-8 agent table directs *"skip if earnings > 30d out."* FSLR's
`next_earnings_date` is **2026-10-29** (~90 days out, confirmed in
`phase-0.5-context.md` from the screener-parquet earnings-date flip, in
`phase-6-macro.md`'s catalyst calendar, and independently by
`fz screen --view financial` reporting `Earnings: "Jul 30/a"` for the *prior*
event). `uw insights earnings-play --days-until-earnings 30` independently
returned 10 tickers with **FSLR absent**, confirming it is out of window. The
remaining four agents ran as specified.

No agent errored. All four returned complete, well-formed verdict blocks and
stayed within budget (9 tool uses each).

One transcription slip, recorded for completeness: risk-monitor quoted the
net_gex at strike 200 as −465,762 (and −605,762 in one place) against
phase-4's **−465,782**. The sign, magnitude and conclusion are unaffected.

## Verdict for downstream

- **Plurality bias: RANGE — 3 of 4** (accumulation-hunter, sweep-tracker,
  risk-monitor), with **NEUTRAL 1 of 4** (contrarian-scanner).
  **LONG 0, SHORT 0.** Read together, the desk's position is: *no directional
  edge; a defined 205.83–217.50 band; act only at the boundaries.*
- **Average conviction: 2.0 / 5** across four non-MISSING agents — **every
  agent independently returned exactly 2**, with zero dispersion. Per the
  phase-8 heuristics this is not the 3-2 split that maps to 0.55–0.65
  conviction; it is **unanimous low conviction**, which is a stronger and
  cleaner signal than a split would have been. Phase 9 should treat 2.0/5 as
  a hard ceiling, not a midpoint.
- **Three highest-quality signals across all agents:**
  1. **`[AGENT:accumulation-hunter]`** — *"regular-session buying flipping
     exactly at the earnings date (28.4%→64.2%→73.1%), with genuine ex-hedge
     accumulation of +51,936 shares (63.2% buy) plus a real 28,000-share buy
     at $214.00 above the offer."* The accumulation is **real but small
     (0.0512% of float)** and independently corroborated by phase-3's OI
     BUILDING (+184,105 over 10 straight days). Cites `[DP:session_split
     DUCKDB]` and `[OI:oi_trend]`.
  2. **`[AGENT:sweep-tracker]`** — *"the 1,900-lot Aug-21 $230 call cross is a
     genuine opening buy — confirmed via a 49-second-lag, 101.1%-match QCT
     delta hedge — but `sweep_persistence.dominant_direction` is "mixed"
     across 4 of 5 sessions with $17.28M of premium producing zero price
     progress."* **Both halves matter**: the block is real *and* it has not
     moved the stock. Cites `[FLOW:unusual_volume]`, `[DP:ts_confirm DUCKDB]`,
     `[FLOW:sweep_persistence]`.
  3. **`[AGENT:risk-monitor]`** — *"insiders sold 07-29, before the 07-30 AMC
     revenue miss that drove the 07-31 target cuts,"* therefore the phase-7b
     and phase-7c CAUTIONs are **temporally independent** and compound:
     **0.5 × 0.75 × 0.75 ≈ 0.28 → 1/8–1/5 of a normal unit, defined-risk
     only.** Cites `[FUND:insider_cluster fz]`, `[SENT:revision_trend]`,
     `[MACRO:MarketRegime_2026-07-31 UW]`.
- **Consensus levels for phase 9** (4/4 agreement, unprompted):
  - **Support 205.83** — dark-pool shelf (`phase-2`), max-pain cluster
    (`phase-4`), base low. **Secondary 200** (put wall, net_gex −465,782)
    where, per risk-monitor, dealer gamma turns decisively negative.
  - **Resistance 217.50** — the triple-confirmed gamma wall, with
    **214.00–217.50** as the congestion band.
  - **Invalidation: a daily close below 205.83.** Unanimous. Accelerated
    below 200.
  - **Upside flip: a close above 217.50 with confirming volume** →
    sweep-tracker converts to LONG.
- **Open questions surfaced by agents:**
  - **Are two institutional cohorts genuinely on opposite sides?**
    (accumulation-hunter) Mid-size 101–500 lot flow ran ask/bid **3.22**
    while >500-lot blocks ran **0.69**, and the LEAP holder trimmed $1.374M of
    credit while regular-session dark pool bought. **If so, no single
    "institutional" verdict is available and phase 9 should stop seeking
    one.**
  - **Can any options-flow argument address the fundamental bear case?**
    (contrarian-scanner) Bernstein's **$197** target, the **$1.056B revenue
    miss** and the **below-consensus guide** are fundamental, not positional —
    **so no flow-based thesis neutralises them.** Phase 9 must carry this as
    an un-hedgeable residual.
  - **Does the 217.50 rejection kill or merely delay the momentum case?**
    (sweep-tracker) Answer given: **delay** — but confirmation requires an
    actual close above 217.50 on volume, which has not happened.
  - **Is a 1-5d or 1-4w horizon correct?** Unresolved 3-1. Phase 9 should
    size to the longer horizon (2026-08-21 OPEX) and manage on the shorter.
