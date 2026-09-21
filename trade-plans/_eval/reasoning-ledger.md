# Reasoning Ledger

The learning loop for the trade-plan skills. `/trade-plan-eval` appends a lesson
here every time a taken plan is marked to market; `/trade-plan` reads it at
intake (phase A0) and applies ACTIVE lessons in A3/A4. This is how the
recommendations improve after real trades — the reasoning models get corrected
by outcomes, not just opinions.

## How to use

- **Generator (A0/A3/A4):** load this file, match lessons by `scope` tags
  (ticker / sector / setup / pattern / regime), apply every `ACTIVE` lesson, and
  list the applied ids in `sources.ledger_lessons_applied`.
- **Evaluator (E3):** append a new lesson with the next `L-####` id. Start new
  lessons as `CANDIDATE`; promote to `ACTIVE` once the same pattern has shown up
  in **≥2 marked trades** (cite both). Demote/retire a lesson if later trades
  contradict it (move to `## Retired` with the reason).

## Lesson format

```
### L-#### — <one-line title>
- status: CANDIDATE | ACTIVE | RETIRED
- scope: <tags, e.g. ticker:NVDA, sector:semis, setup:flow-leads, pattern:triangle, regime:transitional>
- lesson: <the actionable correction, imperative voice>
- evidence: <plan paths + outcomes that support it, e.g. trade-plans/NVDA/2026-06-18 (LOSS -1R)>
- applies_to: <which phase/rubric step it modifies: A3 conviction / A4 sizing / A2 pattern call / entry style>
- added: <YYYY-MM-DD by trade-plan-eval>
```

## Active & candidate lessons

### L-0001 — Don't size a triangle/flag breakout at full until the break holds
- status: ACTIVE
- scope: pattern:triangle, pattern:flag, setup:chart-leads
- lesson: On a CHART-LEADS setup (pattern clean but flow quiet), use a
  break-confirmation trigger (close beyond the level on >1.2x avg volume) and
  size at starter until two closes hold. Anticipatory full size on an unconfirmed
  break is the most common avoidable loss.
- evidence: seed lesson (textbook prior; confirm/retire after ≥2 marked trades).
  Supporting: trade-plans/PATH/2026-07-13 — the plan applied this lesson to its
  12.35 add trigger (volume-confirmed close, starter until two closes hold). The
  12.35 break came on the 2026-07-29 close at 12.59 *after* the 07-22/07-23
  flush; a confirmation-gated add would have re-entered there and captured
  +19.5% to 15.05, whereas an anticipatory add at the first 12.34 touch
  (07-15) would have been carried straight into the −15.6% air pocket.
- applies_to: A3 entry style + A4 sizing
- added: 2026-06-21 (seed); evidence added 2026-08-08 by trade-plan-eval

### L-0002 — A DIVERGENT flow↔chart read is not a directional trade
- status: ACTIVE
- scope: setup:divergent
- lesson: When flow and chart point opposite ways, default to NEUTRAL/RANGE or a
  defined-risk fade only — never a full directional size. Log the divergence as
  the top reason_against.
- evidence: seed lesson (mirrors stock-deep-dive price-vs-flow divergence gate).
  **First real marked trade supporting it:** trade-plans/PATH/2026-06-21
  (INCONCLUSIVE / no trade, 0R). DIVERGENT read (ask-side sweeps up vs H&S down);
  the plan sized 0% and required two consecutive closes < 10.00 to arm a short.
  That trigger never fired (one close at 9.93 in 33 sessions) and the
  reclaim-above-$11 kill-switch fired 2026-07-01. PATH then ran 10.27 → 15.05
  (+46.5%). Flow was right, chart was wrong; the stand-down was worth roughly a
  −1R stop plus a 41% adverse continuation avoided.
- applies_to: A3 bias + conviction
- added: 2026-06-21 (seed); evidence added 2026-08-08 by trade-plan-eval

### L-0003 — Stale flow decays; refresh before sizing up
- status: ACTIVE
- scope: setup:reused-deep-dive
- lesson: If the reused deep dive is > 10 trading days old, cut conviction one
  bin and treat the flow as directional context, not a live edge. Recommend a
  fresh `/stock-deep-dive` before committing full size.
- evidence: seed lesson
- applies_to: A0 staleness flag → A3 conviction
- added: 2026-06-21 (seed)

### L-0004 — Bearish-sweep short in a short-gamma name + bullish catalyst + VETO = trap
- status: CANDIDATE
- scope: setup:divergent, setup:fundamentals-veto, signal:bearish-sweep, structure:short-gamma
- lesson: A persistent bearish sweep campaign in a SHORT-GAMMA book with a live
  bullish catalyst (e.g. IPO access) and a fundamentals VETO is a trap — a
  zero-gamma-level *reclaim* squeezes UP. Respect the veto and the bear's
  strongest unrefuted point; do not even carry defined-risk bearish premium into
  an undated bullish catalyst.
- evidence: trade-plans/HOOD/2026-06-05 (LOSS −1R; HOOD reclaimed 87.45 ZGL and ran +31% to 108.15; the bear's named SpaceX-IPO risk fired). 21D-window re-mark 2026-07-18 confirms no vindication — faded to 99.96 but stayed ~+21% above the 82.47 entry, never threatened the 80/77.5 targets.
- applies_to: A3 conviction modifier + A4 sizing
- added: 2026-06-21 by trade-plan-eval (HOOD 2026-06-05 → 2026-06-18); reconfirmed 2026-07-18 (→ 21D window)
- note: still CANDIDATE — the 2026-07-18 re-mark is the SAME trade at a later window, not a distinct second trade. Promote to ACTIVE only after another name shows the pattern.

### L-0005 — In a >25% short-float name, express a dark-pool-shelf long as defined risk, not a stopped stock long
- status: CANDIDATE
- scope: setup:dark-pool-shelf, sentiment:crowded-short, regime:transitional, ticker:PATH
- lesson: When short interest exceeds ~25% of float, express a dark-pool-shelf
  long as **defined risk** (call debit spread / put credit spread), not as a
  stopped stock long. High-SI names resolve by violent two-way flushes that
  harvest stops before the thesis pays; a defined-risk structure has no stop to
  harvest and survives the round trip. If the desk insists on stock, the stop
  must sit below the full air pocket (see L-0006) and the size must fund that
  wider risk.
- evidence: trade-plans/PATH/2026-07-13 — identical thesis, opposite results by
  vehicle. Stock long 11.80 / stop 11.28 = **LOSS −1.00R**, stopped 2026-07-14 on
  a 10-cent wick (low 11.175) one session before T1 12.34 traded (07-15 high
  12.42). The 12/13 Aug-21 call debit spread reached **max value, +0.65 on a 0.35
  debit (+186%)**, beating its own modelled `est_payoff_at_target` of 0.78; the
  11/10 put credit spread held **full credit +0.31**. Both structures sat through
  the same 07-23 flush to 10.16. Underlying finished the window 11.85 → 15.05
  (+27.0%), both stock targets reached (T1 07-15, T2 08-03).
- applies_to: A4 vehicle selection + expression choice
- added: 2026-08-08 by trade-plan-eval (PATH 2026-07-13 → 2026-08-08)

### L-0006 — Never place a stock stop inside an air pocket you named in reasons_against
- status: CANDIDATE
- scope: risk:air-pocket, setup:dark-pool-shelf, gate:invalidation
- lesson: If a `reason_against` says "there is no support between X and Y", the
  stop may not be placed between X and Y. Put it below Y, or make the trade
  defined-risk. Add an explicit cross-check before publishing: every stop level
  is tested against the plan's own `reasons_against` and `key_risks` text.
- evidence: trade-plans/PATH/2026-07-13 (LOSS −1R) — reason_against #5 read
  "below 11.60/11.80 there is no OI support until $10 — 32% SI becomes an
  accelerant into 9.87-10 (−15%)". The plan then set entry 11.80 and hard stop
  11.28, inside that stated gap. Price did exactly the named thing: 12.04
  (07-21) → 10.16 (07-23), −15.6%, turning only at the $10 put wall the plan had
  itself identified as the real floor. The analysis found the right floor and
  entered 1.60 above it.
- applies_to: A3 level placement / A4 stop selection
- added: 2026-08-08 by trade-plan-eval (PATH 2026-07-13 → 2026-08-08)

### L-0007 — A debate `disconfirmed` cut is provisional while its steelman's own test is unfired
- status: CANDIDATE
- scope: gate:debate-disconfirmed, gate:sizing
- lesson: When the bear's residual rests on a claim carrying an explicit
  falsifiable test that has **not yet resolved**, mark the debate-disconfirmation
  size cut PROVISIONAL. Record the test and a `restore_condition` in the plan,
  and restore the size step once the test comes back clean — do not carry a cut
  premised on an unverified bear case for the life of the trade.
- evidence: trade-plans/PATH/2026-07-13 (LOSS −1R on stock, +186% on the call
  spread) — bear_residual 0.65 ≥ bull 0.65 → `disconfirmed` → one size-step cut
  to starter 1.0%. The steelman was "the $644M block is exit liquidity / an
  unannounced secondary", and it named two tests: a 13D/13G/S-3/424B filing, or
  large-tier dark-pool buy_ratio < 0.45. **Neither ever fired** — no filing
  appeared and large-tier buy_ratio was 0.672 on 2026-08-07 — while the name ran
  +27.0%. The gate cut size on a bear case that its own criteria falsified.
- applies_to: A4 sizing / debate-disconfirmation gate
- added: 2026-08-08 by trade-plan-eval (PATH 2026-07-13 → 2026-08-08)

### L-0008 — A mid-range dark-pool buy_ratio is "undecided", not "refuses to confirm"
- status: CANDIDATE
- scope: setup:divergent, lane:dark-pool, gate:confirmation
- lesson: Treat a large-tier dark-pool buy_ratio in [0.45, 0.55] as NEUTRAL for
  both sides, not as evidence against the bull lane of a DIVERGENT read. Hold it
  unresolved and set an explicit re-check date rather than letting it cut
  conviction — an institution mid-build prints near 0.50 right up until the day
  it does not.
- evidence: trade-plans/PATH/2026-06-21 (INCONCLUSIVE / no trade) — a 0.48
  large-tier buy_ratio was scored as "the dark pool won't confirm" the ask-side
  sweep campaign, reinforcing a bear tilt. Eighteen calendar days later the same
  lane printed a 54.6M sh / $644.2M block at buy_ratio **1.000**
  (trade-plans/PATH/2026-07-13), and the name ran 10.27 → 15.05 (+46.5%). The
  0.48 was an institution mid-build, not a refusal.
- applies_to: A3 flow-chart agreement + reason weighting
- added: 2026-08-08 by trade-plan-eval (PATH 2026-06-21 → 2026-08-08)

## Retired

(none yet)
