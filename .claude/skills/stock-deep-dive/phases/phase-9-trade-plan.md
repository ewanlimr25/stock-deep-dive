# Phase 9 — Synthesis & Trade Blueprint

## Goal

Speak as a desk PM running an institutional book. Translate phases 1 through 8b
(including the 7b fundamental veto and the 8b debate) into a single, actionable,
falsifiable trade blueprint. Emit `phase-9-trade-plan.md` following
`templates/trade-plan-template.md`, plus a structured `decision.json`.

## Inputs (read all)

- `phase-0.5-context.md` (the `[CTX:]` cross-sectional/self-history block — is the
  setup `GENUINELY_UNUSUAL`, `BUSY_NAME_NORMAL_DAY`, or `QUIET`?),
- `phase-1-flow.md` through `phase-8-agent-views.md` from the current run,
  **plus `phase-7b-fundamentals.md` (quality veto), `phase-7c-sentiment.md`
  (positioning/crowd gate), and `phase-8b-debate.md` (disconfirmation residuals).**
- `rubrics/confluence-scoring.md` (for the conviction bin choice)
- `rubrics/invalidation-rubric.md` (for the invalidation section)
- `rubrics/sizing-rubric.md` (for Kelly math + the risk gates)
- `rubrics/citation-conventions.md` (for every numeric claim)
- `templates/trade-plan-template.md` (the skeleton to fill)
- `templates/decision-template.json` (the structured envelope to emit alongside)

## Voice

You are a PM on a $5–50M options-overlay book. You speak plainly. You name
specific strikes. You do not hedge with "could / might / possibly" when the
data is clear. When it is ambiguous, you say so and choose a defined-risk
structure. You write for another PM to either accept, reject, or counter-edit.

Open the plan with:

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Required sections (from template)

Fill every section in `templates/trade-plan-template.md`. Below are the
specific rules per section.

### Thesis (≤3 sentences)

Must cite at least 3 distinct upstream datapoints with proper tags:
- 1 from phases 1–4 (today's tape)
- 1 from phase 5–7 (historical context or UW insight)
- 1 from phase 6 or 8 (macro or agent verdict)

### Bias + conviction

- Bias from the plurality of phases 1–8 (the 7b fundamental veto and the 8b
  debate can only cut conviction/size, never set the bias).
- Conviction MUST snap to one of {0.55, 0.65, 0.75, 0.85, 0.95}.
- Conviction must match the band given by phase-10's confluence score. If
  phase-9 wants to deviate (which is allowed but rare), write a
  `## Conviction deviation` note explaining why.

### Entry zones (primary, aggressive, fade)

- Primary: price + trigger; trigger should be a level cited from phase-2 or
  phase-4 (DP wall or gamma flip).
- Aggressive: a more opportunistic entry; explain the trigger.
- Fade: a counter-trade entry IF the primary thesis invalidates partially —
  this is your hedged plan B.

### Levels to watch

Source every level from a specific upstream phase. The minimum set:
- support (phase-2 price level, or phase-3 `oi-by-strike` `put_wall_support`)
- resistance (phase-2, or phase-3 `oi-by-strike` `call_wall_resistance`)
- gamma flip (phase-4 `today_gamma_flip` if available, else phase-4 ZGL)
- pin magnet (phase-4 `max-pain` near-expiry strike; or phase-3 `pin_risk` if
  within OPEX week). Use the native max-pain value — do NOT assert a pin level by
  eye (cf. the 2026-05-30 max-pain fabrication, `docs/audit/2026-05-30`).
- **price-context color (D8, advisory):** if phase-5 carried the `fz` read,
  mention RSI and **52-week proximity** in the levels/risks prose (e.g. "entering
  at the 52-week high with RSI 79 — chase risk; prefer the fade entry"). Tag
  `[HIST:rsi fz]` / `[HIST:52w_proximity fz]`. This is **narrative color only — it
  never alters the Kelly `p` or the final size.**

### Invalidation

Apply `rubrics/invalidation-rubric.md`: write all three categories
(price-based, signal-based, macro-based) with concrete, falsifiable triggers.

### Sizing (% of risk)

Apply `rubrics/sizing-rubric.md`:
1. Pick **p = the phase-5 `signal_backtest_win_rate`** (read the sizing
   handoff block in `phase-5-historical.md` §Verdict), then apply the
   N-conditional cap from the rubric using `win_rate_n`. Only if
   `win_rate_source` is `null`/insufficient do you fall back to the
   conviction bin. Show both `p_raw` and the capped `p`.
2. Pick b = payoff ratio from your chosen target/entry/stop.
3. Compute raw_kelly.
4. Apply fraction=0.25 and cap_pct=5; cross-check against the win-rate sizing
   map (take the smaller). Enforce the SHORT-side floor if `p < 0.50`.
5. **Apply the risk gates** — each can only cut size or down-shift the bin; list
   every gate and whether it fired (`rubrics/sizing-rubric.md` §"Risk gates"):
   1. fundamentals veto (phase-7b `tier_adjustment`),
   2. **sentiment/crowded gate (phase-7c `tier_adjustment` + `crowd_state`)** —
      CAUTION cuts one step, VETO → directional watch-only,
   3. correlation cluster (phase-6/8 `risk_portfolio_correlation`),
   4. sector-rotation (phase-6),
   5. debate disconfirmation (phase-8b).
   Also apply the **context check**: if phase-0.5 `unusual_verdict =
   BUSY_NAME_NORMAL_DAY`, do not size at the top of the band — the "big flow" is a
   normal day for this name; `QUIET` caps at starter regardless of Kelly.
6. Write Final size = …, with deviation_reason only if you deviated upward
   (forbidden if any gate fired, or if context is `BUSY_NAME_NORMAL_DAY`/`QUIET`).

### Option structures (≥1 directional + ≥1 defined-risk)

Required minimums:
- One **directional** structure (long call/put, debit spread, or risk reversal)
  with specific strike, expiry, debit/credit, breakeven, max loss.
- One **defined-risk alternative** (credit spread, iron condor, butterfly)
  with the same level of detail.
- Pick strikes by referencing phase-3 OI clusters or phase-4 gamma walls when
  possible.
- Pick expiries that match the time horizon AND avoid binary events you do
  not want to trade (use phase-6 catalyst calendar).
- **Size to the expected move (N4).** State the front-expiry implied move
  (`[CTX:implied_move_pct]` from phase-0.5 / phase-7's `uw_screener`) and choose
  structure width and target relative to it: a target beyond ~1.5× the priced move
  is rich, a debit spread narrower than the expected move caps upside before the
  move completes. For any structure whose expiry straddles a catalyst, confirm a
  single-catalyst gap of the expected-move magnitude does **not** exceed the stop —
  if it does, move the expiry or cut size. Record `expected_move` in `decision.json`.

### Macro overlay

Bullet tailwinds and headwinds, each tagged `[MACRO:<series>]` from phase-6.

### Catalyst calendar (next 30d)

Table with date / event / impact direction, all sourced from phase-6.

### Post-trade monitoring checklist

Concrete things to re-check daily / on each phase. At least 4 items.

### Citations summary

Final block listing the ≥3 distinct upstream datapoints from the thesis
(M-04). This is what phase-10 will spot-check.

## Emit the structured `decision.json` (MANDATORY)

After writing `phase-9-trade-plan.md`, write a machine-readable
`decision.json` in the SAME `research/<SYMBOL>/<DATE>/` directory, mirroring
the markdown. This is the envelope `/deep-dive-calibration` later marks to
market — the markdown alone is not machine-resolvable.

1. Fill `templates/decision-template.json` from the plan you just wrote. The
   numeric `sizing` block (`p_raw`, `p`, `win_rate_n`, `win_rate_source`,
   `payoff_b`, `raw_kelly`, `fraction`, `cap_pct`, `final_size_pct`,
   `deviation_reason`) and the `gates` block (`fundamentals`, **`sentiment`,
   `crowd_state`**, `correlation_cluster`, `sector_rotation`,
   `debate_disconfirmed`) are authoritative — they must match the markdown sizing
   section exactly. Also fill the **`context`** block (from phase-0.5 `[CTX:]`:
   `unusual_verdict`, `universe_rank_net_dir`, `iv_rank`, `self_pctile_net_dir`)
   and the **`expected_move`** block (`front_expiry_pct`, `front_expiry_abs`,
   `source`) used to size the structures (N1/N4).
2. Leave `confluence_score` and `recommended_bin` as `null`; phase-10 fills
   them after it scores.
3. **Validate before finishing:**
   ```bash
   python3 schemas/validate_decision.py --file research/<SYMBOL>/<DATE>/decision.json
   ```
   If it prints any error, FIX the JSON and re-run until it prints `OK`. Do
   not leave an invalid `decision.json` behind — a broken envelope silently
   drops the blueprint out of the calibration loop. (For a `-vK` re-run, name
   it `decision-vK.json`.)

## Validation before writing the file

- [ ] All template sections are non-empty.
- [ ] Conviction is in {0.55, 0.65, 0.75, 0.85, 0.95}.
- [ ] Kelly `p` came from the phase-5 win-rate (capped), or conviction-bin
      fallback only when `win_rate_source=null`.
- [ ] Sizing math shown explicitly, with **all five** risk gates listed (fired or
      not): fundamentals (7b), sentiment/crowd (7c), correlation, rotation, debate.
- [ ] Phase-0.5 `unusual_verdict` reflected in sizing (no top-of-band size on a
      `BUSY_NAME_NORMAL_DAY`; starter only on `QUIET`).
- [ ] Structures sized to the front-expiry expected move; `expected_move` in JSON.
- [ ] ≥3 distinct upstream citations in the thesis.
- [ ] ≥1 directional + ≥1 defined-risk structure.
- [ ] All citation tags resolve to actual content in the cited phase MD
      (spot-check 2 of them).
- [ ] Disclaimer line is present at the top.
- [ ] `decision.json` written AND `validate_decision.py` prints `OK`.

## Common pitfalls

- Writing the trade plan to fit a pre-existing bias instead of the data.
- Choosing strikes without referencing OI / gamma walls.
- Picking an expiry that straddles earnings without explicitly addressing IV
  crush.
- Saying "sized to conviction" without showing the Kelly math.
- Using vague invalidation ("if it breaks down") — must be a specific price
  or signal flip.
