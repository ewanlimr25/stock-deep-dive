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
- evidence: seed lesson (textbook prior; confirm/retire after ≥2 marked trades)
- applies_to: A3 entry style + A4 sizing
- added: 2026-06-21 (seed)

### L-0002 — A DIVERGENT flow↔chart read is not a directional trade
- status: ACTIVE
- scope: setup:divergent
- lesson: When flow and chart point opposite ways, default to NEUTRAL/RANGE or a
  defined-risk fade only — never a full directional size. Log the divergence as
  the top reason_against.
- evidence: seed lesson (mirrors stock-deep-dive price-vs-flow divergence gate)
- applies_to: A3 bias + conviction
- added: 2026-06-21 (seed)

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

## Retired

(none yet)
