# Phase A4 — Trade Plans + Structured Envelope (goal #7 / #8)

## Goal

Turn the A3 thesis into concrete, falsifiable plans: **≥1 pure stock long/short
plan AND ≥1 options plan, each options plan with a target date and a target
price** (goal #8). Write the human-readable `trade-plan.md` and the
machine-readable `trade-plan.json`, then validate it.

## Inputs

- `phaseA1-gap-audit.md`, `phaseA2-chart.md`, `phaseA3-confluence.md`, `chart.json`
- `rubrics/direction-rubric.md` (Step 5 levels/targets), the deep-dive
  `sizing-rubric.md` (Kelly + gates) and `invalidation-rubric.md`
- `templates/trade-plan.md` and `templates/trade-plan.json`

## Steps

1. **Respect the gap-audit ceiling.** `INSUFFICIENT` → both plans are
   **watch-only / size 0%**, and the doc leads with the sourcing shortlist.
   `USABLE_WITH_GAPS` → proceed with caveats, one size step lower.

2. **Sizing (Kelly).** Apply `../../stock-deep-dive/rubrics/sizing-rubric.md`:
   pick `p` = the deep-dive's phase-5 `signal_backtest_win_rate` (capped by N);
   fall back to the conviction bin (≤0.65) only if `win_rate_source=null`. Pick
   `b` from your target/entry/stop. Compute raw Kelly; apply fraction 0.25,
   cap 5%; cross-check the win-rate map; enforce the SHORT-side floor. List every
   risk gate (fired or not). Show the math. This `sizing` block is authoritative
   and must match the JSON exactly.

3. **Plan A — pure stock (long/short).** Required (goal #8: "at least 1 pure
   long/short plan"):
   - `direction` (long/short, or `stand_aside` only if INSUFFICIENT),
   - `entry` + `entry_trigger` (use the A3 trigger level; for FLOW-LEADS use a
     break-confirmation trigger, not a market entry),
   - `stop` (chart invalidation or ATR×1.5, the tighter that clears noise),
   - `targets[]` (≥1; T1 with reward:risk ≥ 1.0, scale-out %), 
   - `r_multiple_to_t1`, `size_pct_book` (from sizing, translated to shares risk),
   - a one-line thesis.

4. **Plan B — options (≥1, each WITH target_date + target_price).** Required
   (goal #8: "at least 1 options plan with target date and price"):
   - At least one **directional** structure (long call/put, debit spread, risk
     reversal) AND ideally one **defined-risk** alternative (credit spread / iron
     condor / butterfly).
   - Each: `structure`, `strikes` (anchored to OI/gamma walls or chart levels),
     `expiry`, **`target_date`** (when you expect the target hit — before the
     expiry and clear of unwanted binary events), **`target_price`** (the
     underlying objective — usually a pattern measured-move / Fib / swing),
     `debit_credit`, `breakeven`, `est_payoff_at_target`, `max_loss`,
     `size_pct_book`.
   - **Size to the expected move:** state the front-expiry implied move; a target
     beyond ~1.5× the priced move is rich; a debit spread narrower than the move
     caps upside. If an expiry straddles a catalyst, confirm a single-gap of the
     expected-move size does not blow the stop — else move the expiry or cut size.

5. **Patterns + events into the envelope.** Carry the A2 patterns (type,
   direction, confidence, target, invalidation) and the A3 event calendar into
   the JSON `patterns[]` and `events[]`.

6. **Write the markdown** `trade-plans/<SYMBOL>/<DATE>/trade-plan.md` from
   `templates/trade-plan.md` (every section filled, disclaimer at top).

7. **Emit and validate the JSON.** Fill `templates/trade-plan.json` →
   `trade-plans/<SYMBOL>/<DATE>/trade-plan.json` (sizing + gates + gap_audit +
   sources authoritative; `confluence_score` from A3 or null). Then:
   ```bash
   python3 .claude/skills/trade-plan/schemas/validate_trade_plan.py \
       --file trade-plans/<SYMBOL>/<DATE>/trade-plan.json
   ```
   Fix and re-run until it prints `OK`. A broken envelope drops the plan out of
   the eval/learning loop.

## Validation checklist (before finishing)

- [ ] gap-audit verdict reflected in sizing (INSUFFICIENT ⇒ 0%).
- [ ] ≥2 reasons_for and ≥2 reasons_against, all tagged.
- [ ] ≥1 stock plan (direction + entry + stop + ≥1 target).
- [ ] ≥1 options plan, each with `target_date` AND `target_price`.
- [ ] Kelly math shown; all five gates listed; SHORT-side floor honored.
- [ ] Structures sized to the expected move; expiries clear unwanted catalysts.
- [ ] Levels & patterns carry sources; ≥3 distinct citations.
- [ ] `validate_trade_plan.py` prints `OK`.
- [ ] Disclaimer present.

## Surface to the user

Print: the path to `trade-plan.md`, the direction + conviction, the one-line
stock plan, the headline options plan (structure / target_price by target_date),
the gap-audit verdict, and a reminder to run `/trade-plan-eval <SYMBOL> <DATE>`
after taking the trade so the reasoning ledger learns from it.
