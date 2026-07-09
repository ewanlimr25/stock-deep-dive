# Direction & Conviction Rubric (Phase A3)

How to fuse the flow/positioning layer (from the deep-dive) with the new chart
layer into ONE direction, a conviction bin, and an honest two-sided case. This
reuses the canonical stock-deep-dive machinery — do not reinvent it:

- conviction bins, Kelly `p`, the N-cap, and the five risk gates →
  `../../stock-deep-dive/rubrics/sizing-rubric.md` (or the copy you loaded)
- 0–100 confluence → `../../stock-deep-dive/rubrics/confluence-scoring.md`
- citation tags → `../../stock-deep-dive/rubrics/citation-conventions.md`
  (plus the new `[CHART:<detector>]` tag for chart-engine datapoints)

## Step 1 — collect directional votes

Tally a bias from each available lane. Each lane votes LONG / SHORT / NEUTRAL.

| Lane | Bullish read | Bearish read |
|------|--------------|--------------|
| Flow (A1) | net call premium, ask-side sweeps | net put premium, bid-side |
| Dark pool (A2) | block buy-ratio > 0.55 accumulation | sell-ratio distribution |
| Positioning (A3) | call walls building above, put support | call OI as resistance, put builds below |
| Dealer (A4) | positive DEX / long-gamma above ZGL | negative DEX / short-gamma |
| Historical (A5) | cum-premium-flow accreting, win-rate ≥ 0.55 | flow decaying / negative |
| **Chart trend (B3)** | uptrend HH-HL, price > rising 50/200 | downtrend LH-LL, price < falling MAs |
| **Chart pattern (B4)** | bull flag / inv-H&S / asc-triangle / double-bottom | bear flag / H&S / desc-triangle / double-top |
| Macro/sector (C1) | regime risk-on, sector inflow | risk-off, sector outflow |

**Bias = plurality of lanes.** The fundamentals veto (C3), sentiment gate (C4)
and debate can only *cut*, never set the bias (mirrors the deep-dive: filters
don't amplify).

## Step 2 — flow ↔ chart agreement is the key signal

The edge of this skill is fusing two independent views. Classify the agreement:

- **CONFLUENT** — flow and chart agree on direction → take conviction from the
  confluence band normally.
- **FLOW-LEADS** — flow is directional but the chart hasn't confirmed (e.g.
  accumulation under resistance, base not yet broken) → **anticipatory**: use a
  *trigger* entry (break of the level) and cut conviction one bin until the
  chart confirms. This is the highest-value setup when it later confirms.
- **CHART-LEADS** — clean pattern but flow is quiet/mixed → treat the pattern as
  the primary, size at starter, demand a volume-confirmed break.
- **DIVERGENT** — flow and chart point opposite ways → NEUTRAL/RANGE by default,
  or fade only with a defined-risk structure; never a full directional size.
  Record the divergence as a top `reason_against`.

## Step 3 — conviction bin

Snap to {0.55, 0.65, 0.75, 0.85, 0.95} from the confluence-scoring band, then
apply, in order (each can only lower):

1. agreement modifier (FLOW-LEADS / CHART-LEADS → −1 bin; DIVERGENT → cap 0.55)
2. the five deep-dive risk gates (fundamentals, sentiment, correlation, rotation, debate)
3. the phase-0.5 context modifier (BUSY_NAME_NORMAL_DAY → no top-of-band; QUIET → starter)
4. data-staleness: deep-dive reused > 10 sessions old → cut one bin and flag it
5. gap-audit verdict: USABLE_WITH_GAPS → cut one step; INSUFFICIENT → watch-only

## Step 4 — reasons for / against (goal #3)

Write **≥2 reasons_for** and **≥2 reasons_against**, every line tagged and
falsifiable. Rules:

- The strongest `reason_against` MUST be the single best argument the *other*
  side would make (steelman). If you can't articulate it, you don't understand
  the trade.
- At least one `reason_against` must be a concrete, watchable trigger that would
  flip the thesis (it should reappear in the invalidation block).
- A DIVERGENT flow/chart read is always a `reason_against`.

## Step 5 — levels & targets

- **Entry trigger / support / resistance:** prefer a level confirmed by *both* a
  chart pivot/cluster (`[CHART:…]`) and a dealer/OI level (`[DP:…]`/`[OI:…]`/`[STRUCT:…]`).
  A level two independent methods agree on is the one to trade.
- **Stop:** the chart invalidation (swing pivot / pattern neckline) OR an
  ATR×1.5 distance — take the tighter that still sits beyond noise.
- **Targets:** pattern measured-move, Fib extension, prior swing, or the nearest
  significant opposing wall — whichever is nearest and named. T1 should give a
  reward:risk ≥ 1.0; if it can't, cut size or stand aside.

## Forbidden

- Setting bias from the chart pattern alone when flow flatly contradicts it.
- Quoting a pattern as `high` confidence off the heuristic engine — the engine
  caps at `medium`; only raise to `high` with an explicit, cited manual read.
- Inventing a level not present in `chart.json` or a deep-dive phase MD.
