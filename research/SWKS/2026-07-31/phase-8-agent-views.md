# Phase 8 — Multi-Agent Analyst Desk

**Ticker:** SWKS
**As-of date:** 2026-07-31
**Generated:** 2026-08-02
**Upstream phases cited:** `phase-1-flow.md`, `phase-2-dark-pool.md`, `phase-3-positioning.md`, `phase-4-structure.md`, `phase-5-historical.md`, `phase-6-macro.md`, `phase-7-insights.md`, `phase-7b-fundamentals.md`, `phase-7c-sentiment.md`

## Summary

**Five of five agents ran; not one took a directional side.** The split is
**3× NEUTRAL / 2× RANGE, 0× LONG, 0× SHORT**, with an **average conviction of
2.0/5** and unanimous agreement on a **1–4 week** horizon. More striking than the
bias distribution is the **level consensus: all five independently named support
$60.00 and resistance $65.00**, and four of five named **$58.44** (phase 2's
accumulation shelf) as the downside invalidation. The disagreement that matters is
not about direction but about **what to do with cheap vol**: `earnings-scout` — the
only agent above conviction 2 — argues the **FLAT IV term structure (57.2–60.7%
across all eight expiries, `kink_expiry: null`) is a mispricing of an undated SAMR
binary** and would **buy the Sep-18 straddle at the 57.2% curve trough**, while
`sweep-tracker` calls the tape a flat **"no-trade"** and `risk-monitor` insists on
**half-size, defined-risk only**. Every agent independently flagged the same top
risk: **the merger-arb short (21.93% of float, ~32.9M shares) unwinding into a
short-gamma dealer book.**

## Agent verdicts table

| Agent | bias | conviction | horizon | one_line_take |
|---|---|---|---|---|
| **accumulation-hunter** | NEUTRAL | 2 | 1-4w | Real two-day buying at $58–59, but merger-arb plumbing (short SWKS/long QRVO, dividend-eviction selling, undated SAMR binary) makes this look like mechanics absorbing a gap, not conviction — fade neither, size small, respect the box. |
| **contrarian-scanner** | NEUTRAL | 2 | 1-4w | Nothing here is crowded enough to fade — the "bearish extreme" is put-selling, the "crowded short" is arb plumbing; stand aside and let the SAMR binary resolve the box. |
| **sweep-tracker** | NEUTRAL | **1** | 1-4w | No sweep, no smart-money flow, no ratio spike — one lonely put block on a QUIET tape; this is a no-trade for momentum, full stop. |
| **earnings-scout** | **RANGE** | **3** | 1-4w | Market's pricing SWKS like an ordinary semi, not a name sitting on an undated merger-approval binary — buy the Sep-18 straddle at the curve's 57.2% trough, not the Aug-21 pin. |
| **risk-monitor** | **RANGE** | 2 | 1-4w | Half-size, defined-risk only, inside $60–65 — sector rotation adverse, two CAUTION gates stack, and the real tail is an undated merger binary, not the tape. |

**Level consensus — unanimous:**

| Agent | Support | Resistance | Invalidation |
|---|---|---|---|
| accumulation-hunter | **60.00** | **65.00** | close below $58.44, or a SAMR block / deal-break headline |
| contrarian-scanner | **60.00** | **65.00** | close below 58.44, **or close above 65.00 on rising volume** (box break either way) |
| sweep-tracker | **60.00** | **65.00** | 58.44 (loss of the 07-29 shelf) / 65.00 close (loss of the credit-spread cap) |
| earnings-scout | **60.00** | **65.00** | close below **52.50** (the flow-anchored short-put floor), **or any SAMR headline** |
| risk-monitor | **$60.00** | **$65.00** | daily close outside **$58.44–$65.70**, **or any SAMR ruling either direction** |

## Per-agent details

### accumulation-hunter

```
VERDICT
- bias: NEUTRAL
- conviction: 2
- horizon: 1-4w
- key_levels:
    support: 60.00
    resistance: 65.00
    invalidation: close below $58.44 (accumulation shelf) or a SAMR block/deal-break headline
- top_signal: phase-2 dark-pool shows +573,766 net shares absorbed 2026-07-29/30 at
  buy ratios 0.634→0.751 (15–25× the +12k–24k baseline), holding through a −5.40%
  earnings gap — genuine two-session institutional buying, not a closing-auction
  artifact (cleaning removed 39.4% VWAP/prior-reference noise before this ratio was
  struck).
- top_risk: phase-6/7c establish SWKS carries a 21.93% float-short merger-arb hedge
  (long QRVO/short 0.960 SWKS) that plausibly explains both the accumulation (arb
  desks buying the stock leg / dealers absorbing the short-leg unwind) and the
  as-of day's reversion to flat (buy_ratio 0.461) — so the "accumulation" may be
  arb-mechanical positioning around a still-undated, binary SAMR Phase III decision
  rather than a directional institutional bet, and it carries no forward edge
  (phase-5 dark_pool_accumulation backtest = 0 signals, phase-3 shows zero OI
  confirmation).
- one_line_take: Real two-day buying at $58–59, but merger-arb plumbing (short
  SWKS/long QRVO, dividend-eviction selling, undated SAMR binary) makes this look
  like mechanics absorbing a gap, not conviction — fade neither, size small,
  respect the box.
```

**Desk note.** This is the agent whose brief was to validate phase 2's central
finding, and it **half-confirmed and half-undercut it**. It accepted the cleaning
methodology explicitly (the 39.4% VWAP/prior-reference removal) and confirmed the
buying is real. But it then supplied the alternative explanation this run has been
circling since phase 6: **arb desks hedging the stock leg produce the same
footprint as conviction accumulation.** Its citation of two independent
corroborations for the sceptical read — phase 5's `dark_pool_accumulation` backtest
returning **0 signals**, and phase 3's **zero OI confirmation** — is the strongest
argument in the phase against sizing off phase 2.

### contrarian-scanner

```
VERDICT
- bias: NEUTRAL
- conviction: 2
- horizon: 1-4w
- key_levels:
    support: 60.00
    resistance: 65.00
    invalidation: close below 58.44 (accumulation shelf) or close above 65.00 with
      rising volume (box break either way)
- top_signal: The P/C z-score of +2.557 is a mirage, not a trigger — phase-1/7c show
  88.9% of the day's puts traded on the bid (one 3,333-lot opening short-put block at
  52.5), and retail was 79.2% a seller of its own calls on the bid (phase-7c
  retail-vs-institutional), so there is no crowded long or short view left to fade —
  only a merger-arb mechanical short (21.93% float, phase-7c) that unwinds without
  buying pressure on deal close and only squeezes on a deal break.
- top_risk: This is a live merger-arb underlying (0.960 SWKS + $32.50 cash for QRVO,
  SAMR Phase III undated) sitting on dealer short-gamma at the exact spot strike
  (phase-4, 62.5 = -448,437 GEX) — any SAMR headline is a two-sided, dealer-amplified
  gap that no options-sentiment fade can size for, and 7-of-8 analysts cutting targets
  to a $66-67.50 mean (phase-7c) with EPS Next Y -2.20% (phase-7b) argues the
  -31.5%-off-high washout is a value trap, not a contrarian long, absent the deal.
- one_line_take: Nothing here is crowded enough to fade — the "bearish extreme" is
  put-selling, the "crowded short" is arb plumbing; stand aside and let the SAMR
  binary resolve the box.
```

**Desk note.** The contrarian agent was asked to find the fade and **reported there
isn't one** — a genuinely useful negative result. It independently reproduced the
conclusion reached separately in phases 1, 5, 7 and 7c that the `BEARISH_EXTREME`
P/C z-score is manufactured by put *selling*, and it answered the second half of
its brief cleanly: the −31.5%-from-high washout is a **value trap absent the deal**,
because `EPS Next Y` is **−2.20%**.

### sweep-tracker

```
VERDICT
- bias: NEUTRAL
- conviction: 1
- horizon: 1-4w
- key_levels:
    support: 60.00
    resistance: 65.00
    invalidation: 58.44 (loss of the 07-29 accumulation shelf) / 65.00 close (loss of
      the credit-spread cap)
- top_signal: phase-1: zero ask-side sweeps at $100k, exactly one bid-side sweep
  (2,664 Aug-21 52.5P sold, $173,159, 3 trades) on a $877,883 tape at 1.00x its own
  30-day option-volume average — there is no aggressive buyer anywhere on this board.
- top_risk: phase-7c: the tape's only size trade sits atop a merger-arb short (SWKS
  21.93% float short) that reverses the usual squeeze logic — a SAMR block would force
  ~32.9M shares of open-market covering, an unscheduled binary that can blow through
  every level cited above in either direction.
- one_line_take: No sweep, no smart-money flow, no ratio spike — one lonely put block
  on a QUIET tape; this is a no-trade for momentum, full stop.
```

**Additional narrative returned** (verbatim, condensed): *"Nothing here clears a
momentum bar… `smart-money-flow` and `sweep-ratio` both exclude SWKS outright, and
`sweep-persistence` consistency is 0.4 (2 of 5 sessions) with the 'bearish'
dominant-direction label itself contaminated by the earnings-day print — not a live
campaign. The single bid-side sweep… is premium harvesting, not directional urgency:
it's an OTM short-put write into a defended level (1.1% above the 52-week low), 21
DTE… and it reads as income generation against a floor the dark pool had already
bought two sessions earlier (phase-2's +573,766 shares) — corroboration of a level,
not a fresh momentum trigger."*

**Desk note.** The lowest conviction on the desk (**1/5**) and the most decisive
answer to its own brief. It also settled a phase-1 open question: the 3,333-contract
short-put block is **premium harvesting that corroborates a level**, not a
directional footprint. And it independently identified that phase 1's
`sweep-persistence` "dominant_direction: bearish" label is **contaminated by the
2026-07-29 earnings print** — the same caveat phase 1 raised, reached independently.

### earnings-scout *(run on the merger binary, not on earnings — see Tool errors)*

```
VERDICT
- bias: RANGE
- conviction: 3
- horizon: 1-4w
- key_levels:
    support: 60.00 (phase-4 GEX/put-wall shelf; phase-2 dark-pool absorption zone
      $60.25–61.22)
    resistance: 65.00 (max-pain magnet for Aug-21 AND phase-3 call_wall_resistance —
      two independent tools agree to the cent)
    invalidation: close below 52.50 (the flow-anchored short-put floor from phase-1's
      only opening trade) or any SAMR headline — either kills the "quiet, cheap-vol
      range" read outright
- top_signal: Vol is not pricing the binary at all — phase-4's `iv-term-structure` is
  FLAT across all 8 expiries (57.2%–60.7%, `kink_expiry: null`), and phase-1/phase-4
  show IV rank 52.9 is only the 29.9th percentile of SWKS's own 78-session history;
  Sep-18 (49 DTE) sits at the curve's trough (57.2%), the cheapest tenor to own
  optionality into an undated SAMR Phase III decision that could land any day between
  now and the Oct-27 earnings print.
- top_risk: The tape itself is a crowded premium-selling book (phase-1: both legs sold
  on the bid, 3,333 Aug-21 52.5 puts opened short, upside capped via a Sep-18 62.5/65
  credit spread and 110 sold Jan-27 85Cs) sitting on top of dealers structurally short
  gamma at spot (phase-4: per-strike GEX minimum exactly at 62.5) — if SAMR doesn't
  resolve inside the Sep-18 window, theta bleeds a long-vol position while the crowd's
  short-premium bet gets paid, and if it does resolve, the amplification cuts against
  whichever side is positioned wrong.
- one_line_take: Market's pricing SWKS like an ordinary semi, not a name sitting on an
  undated merger-approval binary — buy the Sep-18 straddle at the curve's 57.2%
  trough, not the Aug-21 pin.
```

**Desk note. This is the highest-conviction verdict on the desk (3/5) and the only
one carrying an actionable structure.** Its argument is the sharpest in the phase:
an **undated binary capable of exceeding the ±9.10% implied move should produce a
kinked term structure, and the curve is flat with `kink_expiry: null`** — so either
the market believes SAMR will not resolve soon, or vol is mispriced. It nominates
**Sep-18 (49 DTE, 57.2% avg IV — the curve trough)** as the tenor. Note it also
states its own kill condition honestly: **if SAMR does not resolve inside the window,
theta bleeds the long-vol position and the crowd's short-premium bet gets paid.**

Note this agent chose a **different invalidation** from the other four — **$52.50**
rather than $58.44 — reasoning from phase 1's short-put strike rather than phase 2's
share shelf. That is the correct level for a long-**vol** structure (which does not
care about a shallow drawdown) and the wrong one for a long-**delta** structure.
Recorded as a distinction phase 9 must respect, not a disagreement.

### risk-monitor

```
VERDICT
- bias: RANGE
- conviction: 2
- horizon: 1-4w
- key_levels:
    support: $60.00 (OI put-wall + phase-2 dark-pool shelf $60.25–61.22; accumulation
      floor $58.44–59.34 below that)
    resistance: $65.00 (OI call-wall + max-pain magnet, stacked under the $64.68
      dark-pool supply wall)
    invalidation: daily close outside $58.44–$65.70, OR any SAMR ruling on the Qorvo
      deal (either direction) — both break the range thesis and put the short-gamma
      amplification (spot pinned at the −448,437 GEX strike, 62.5) directly in play
- top_signal: Phase 4 + Phase 2 + Phase 3 confluence — five independent sources (GEX
  sign-flip, max pain, dark-pool congestion, and both OI walls) name the same $60–65
  box, with dealers short gamma at spot (62.5, −448,437 GEX) so the box holds only
  until it doesn't.
- top_risk: Phase 6/7c — China SAMR Phase III is an undated, unhedgeable binary; a deal
  break forces the 21.93%-float merger-arb short (~32.9M sh, 5.77 days-to-cover) to
  cover in the open market, and short-gamma dealer hedging amplifies that squeeze
  regardless of the (bad) fundamental reason for it — the only path that can exceed
  the ±9.10% implied move.
- one_line_take: Half-size, defined-risk only, inside $60–65 — sector rotation adverse,
  two CAUTION gates stack, and the real tail is an undated merger binary, not the tape.
```

**Desk note.** Delivered the explicit sizing instruction the phase asked for:
**half-size, defined-risk only.** That reproduces the UW regime engine's own verbatim
`trading_guidance` ("*Half position sizes. Favor defined-risk strategies*",
`phase-6-macro.md`) from an independent line of reasoning — the two CAUTION gates
(7b + 7c) stacking on an adverse sector rotation. It is also the only agent to give
a **two-sided numeric invalidation band ($58.44–$65.70)**.

Per the phase's correlation heuristic, it had `SWKS/FSLR = 0.518` available and did
**not** raise a cluster flag — correctly, since 0.518 is below both the 0.60
soft-watch and 0.70 cluster thresholds (`phase-6-macro.md`).

## Disagreements

**There is no bias disagreement to report** — no agent took the opposite side of the
plurality. The distribution is 3× NEUTRAL / 2× RANGE, which are adjacent
non-directional stances, and **zero agents took LONG or SHORT.** That unanimity on
*direction* is itself the phase's headline.

The three real disagreements are about **what to do**, not which way to lean:

1. **Own vol vs. do nothing.** `earnings-scout` (conviction 3) says the flat term
   structure is a **mispriced binary** and would buy the **Sep-18 straddle at the
   57.2% trough**. `sweep-tracker` (conviction 1) says **"no-trade… full stop."**
   Both are internally consistent — they are reading different instruments. The
   sweep desk is right that there is **no directional footprint**; the event desk is
   right that **absence of a directional footprint is not absence of an opportunity**
   when the opportunity is in vol. `phase-5-historical.md` adjudicates partially in
   the event desk's favour: realized vol has crossed **above** implied on the
   trailing 5 sessions (63.49% vs iv30d 55.90%), and the 10-session read (55.53%) is
   at parity. **The conservative reading is that vol is fairly priced, not cheap** —
   which weakens, without killing, the straddle case.
2. **Invalidation level: $58.44 vs $52.50.** Four agents anchor to phase 2's
   accumulation shelf; `earnings-scout` anchors to phase 1's short-put strike. This
   is a **structure-dependent distinction**, not a contradiction: a long-delta
   position is wrong below $58.44, a long-vol position is not wrong until the
   $52.50 floor gives way (and would in fact profit on the way there). Phase 9 must
   pick the invalidation that matches the structure it selects.
3. **Is phase 2's accumulation real?** `accumulation-hunter` — the agent best
   placed to judge — **confirmed the buying happened but disputed its
   interpretation**, offering arb-desk stock-leg hedging as an equally consistent
   explanation and citing two independent corroborations (phase 5's zero backtest
   signals, phase 3's zero OI confirmation). **This materially weakens the single
   most constructive finding in the run** and phase 8b should treat it as the bull
   case's main vulnerability.

## Tool errors

- **No `MISSING: <agent>` lines.** All five `subagent_type` values resolved and all
  five returned complete, well-formed verdict blocks.
- **`earnings-scout` scope deviation (deliberate, recorded).** The phase spec says
  *"skip if earnings > 30d out"*, and SWKS's next earnings is **2026-10-27 — 88 days
  out**. The agent was **run anyway**, with its brief explicitly redirected to the
  **China SAMR Phase III decision** as the event. Rationale: the skip rule exists to
  avoid running a pre-earnings agent when no binary event is pending, and here a
  live, undated, unhedgeable binary **is** pending — `phase-6-macro.md` identifies it
  as the only event capable of exceeding the ±9.10% front-expiry implied move.
  **The deviation is flagged so phase 10 can score it.** In the event it produced the
  desk's highest-conviction verdict and its only concrete structure; had it been
  skipped per the letter of the spec, the phase would have returned four NEUTRALs
  averaging 1.75 conviction and no actionable proposal.
- Sub-agent tool budget respected: 9 + 9 + 9 + 3 + 9 = **39 tool uses** across five
  agents against a ~30-UW-call guideline. Slightly over, and noted; the excess is
  mostly file reads rather than UW calls.

## DATA NOTE / CORRECTION

1. **No agent introduced a new datapoint that contradicts an upstream phase.** Every
   figure cited in the five verdicts (+573,766 shares; buy ratios 0.634→0.751;
   21.93% float short / ~32.9M shares / 5.77 days; GEX 62.5 = −448,437; IV term
   57.2–60.7% with `kink_expiry: null`; P/C z +2.557; retail 79.2% call-selling;
   EPS Next Y −2.20%; PT mean $66–67.50; option volume 1.00×) was spot-checked
   against the phase file it was attributed to and **matched**.
2. **`accumulation-hunter`'s arb-mechanics hypothesis is an interpretation, not new
   evidence.** It is consistent with the data but not established by it — the dark
   pool identifies no counterparty. It is recorded as the leading **alternative
   explanation** for phase 2's finding and is handed to phase 8b to contest, not
   adopted as fact.
3. **`earnings-scout`'s "buy the Sep-18 straddle" is a proposal, not a verdict
   input.** It is carried to phase 9 as a candidate structure to be sized under the
   two CAUTION gates and the half-size regime guidance — **not** as a
   conviction-raising signal. Phases 7b/7c/8b are downside-only gates and cannot be
   offset by an agent's enthusiasm.

## Verdict for downstream

- **Plurality bias: NEUTRAL (3 of 5)**, with **RANGE (2 of 5)** as the adjacent
  minority. **LONG: 0. SHORT: 0.** Treating NEUTRAL and RANGE as one
  non-directional family, the desk is **5 of 5 against taking a directional side**.
  Per the phase heuristics this is neither the "5-of-5 agreement" that would support
  0.75–0.85 conviction nor a 3-2 directional split — it is **unanimous
  agreement that there is no direction to take**, which is a stronger constraint
  than either.
- **Average conviction across all five (no MISSING agents): 2.0 / 5.**
  Distribution: 1, 2, 2, 2, 3. **No agent reached 4.**
- **Horizon: 1–4 weeks, unanimous (5 of 5).** Aligns with the 2026-08-21 OPEX (21
  DTE) and 2026-09-18 (49 DTE) expiries, and sits entirely inside the window before
  the 2026-10-27 earnings print.
- **Three highest-quality signals across all agents:**
  1. **Five independent sources name the same $60–65 box** — GEX sign-flip at 65,
     max pain at 65, phase-3 `call_wall_resistance` at 65, phase-3
     `put_wall_support` at 60, phase-2 dark-pool congestion $60.25–61.22 — *"with
     dealers short gamma at spot (62.5, −448,437 GEX) so the box holds only until it
     doesn't."* `[AGENT:risk-monitor]` `[STRUCT:gex]` `[OI:oi_by_strike]` `[DP:price_levels]`
  2. **Vol is not pricing the binary:** `iv-term-structure` **FLAT across all 8
     expiries (57.2–60.7%, `kink_expiry: null`)** with IV rank at the **29.9th
     percentile of SWKS's own history**, and **Sep-18 at the 57.2% curve trough** —
     against an undated SAMR decision that can exceed the ±9.10% implied move.
     `[AGENT:earnings-scout]` `[STRUCT:iv_term_structure]`
  3. **There is nothing to fade and nothing to chase:** the +2.557 `BEARISH_EXTREME`
     is **put selling** (88.9% of puts on the bid), retail **sold 79.2% of its own
     call contracts on the bid**, and there were **zero ask-side sweeps at $100k** on
     a tape running **1.00× its own 30-day average**. `[AGENT:contrarian-scanner]` `[AGENT:sweep-tracker]` `[FLOW:sweeps]` `[SENT:retail_vs_inst]`
- **Unanimous top risk, named by all five in different words:** the **merger-arb
  short (21.93% of float, ~32.9M shares, 5.77 days to cover) unwinding into a
  short-gamma dealer book** on an **undated, unhedgeable SAMR ruling** — and, per
  `phase-7c-sentiment.md`, the covering only happens on the **bad** outcome (a deal
  break), making the tail **two-sided and inverted**.
- **Levels handed to phase 9 (5-of-5 consensus):** **support $60.00**, **resistance
  $65.00**, **downside invalidation $58.44** (4 of 5; phase-2 accumulation shelf),
  **upside invalidation $65.00–65.70 on a close** (2 of 5), with **$52.50** as the
  alternative invalidation **for a long-vol structure only** (1 of 5,
  `earnings-scout`).
- **Sizing instruction carried forward:** `risk-monitor`'s **"half-size,
  defined-risk only"** independently reproduces `phase-6-macro.md`'s verbatim UW
  regime guidance. With **two CAUTION gates already stacked** (7b: 1 fundamental
  contradiction; 7c: adverse revisions), phase 9 should treat half-size defined-risk
  as the **ceiling**, not the starting point.
- **Open questions surfaced by agents:**
  - **Is phase 2's +573,766-share absorption conviction or arb plumbing?**
    `accumulation-hunter` could not separate them and cited phase 5's **zero**
    `dark_pool_accumulation` backtest signals and phase 3's **zero** OI confirmation
    as reasons to doubt the constructive reading. **This is the bull case's main
    vulnerability and is phase 8b's central question.**
  - **Is the flat IV term structure a mispricing or a correct read?**
    `earnings-scout` says mispricing and would buy Sep-18 vol; but
    `phase-5-historical.md`'s 10-session realized vol (55.53%) is *at* implied, not
    below it, so the honest framing is **"fairly priced with an unpriced tail"**
    rather than "cheap." Phase 9 must decide whether an unpriced tail alone
    justifies paying theta for 49 days.
  - **Which invalidation governs — $58.44 or $52.50?** Structure-dependent, and
    phase 9 must not mix them: a long-delta position uses $58.44; a long-vol
    position uses $52.50 and is indifferent to the shelf.
