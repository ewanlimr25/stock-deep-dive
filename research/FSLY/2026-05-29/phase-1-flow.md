# Phase 1 — Options Flow

## Summary

The options tape is **call-tilted but tiny and low-conviction** — it confirms
phase-0.5's "quiet day" read rather than a directional signal. **Zero sweeps fired**
(no aggressive multi-exchange prints), and the largest *single* trade all day was a
**$79k 20C Jan-2028 LEAP on the mid** — lottery/long-dated, not urgent. Call premium
leads every expiry, but the magnitudes are small (top expiries $224k–$268k call
premium) and many of the larger single trades printed on the **bid** (17.5C 6/18
$38k bid, 35C '27 $18k bid, 17C 6/12 $15k bid) — i.e. as much passive/sold as bought.

There is a faint **squeeze-lottery flavour**: fresh interest in deep-OTM upside
(20C/30C 7/17, 45C 6/18, 30C '27) consistent with a 14.6%-short-float momentum name,
plus a couple of small ask-side call buys (18.5C 6/5, 20C 7/17, 16.5C 0DTE). DTE is
**BALANCED** (0DTE 0%, weeklies 21%, monthlies 26%, LEAPs 3.5%) — spread positioning,
not an intraday gamma event.

**Directional read: WEAK-BULLISH, conviction LOW.** The call-tilt is real but the
dollars are trivial for a $2.65B name and the buying is not aggressive (no sweeps,
mixed bid/ask). This is **not** flow you size off; it's a faint lean that the
positioning (phase-3) and squeeze structure must carry if there's a trade here.

## Sweeps (`uw options-flow sweeps`) `[FLOW:sweeps]`

- **0 sweep contracts.** No aggressive ask-hitting or bid-smacking multi-exchange
  prints on the day. Absence of sweeps on a +4.9% day = the move was not driven by
  urgent options demand. (Consistent with phase-0.5 volume 9th self-pctile.)

## Top-premium single trades (`uw options-flow top-premium-trades`) `[FLOW:top-premium-trades]`

| Strike | Type | Expiry | Side | Premium | Size |
|--------|------|--------|------|---------|------|
| 20 | call | 2028-01-21 | mid | $79k | 99 |
| 17.5 | call | 2026-06-18 | bid | $38k | 250 |
| 35 | call | 2027-07-16 | bid | $18k | 50 |
| 17 | call | 2026-06-12 | bid | $15k | 100 |
| 30 | call | 2026-12-18 | bid | $14k | 60 |
| 30 | put | 2026-06-18 | ask | $12k | 10 |
| 17.5 | call | 2026-07-17 | ask | $12k | 50 |
| 18.5 | call | 2026-06-05 | ask | $11k | 241 |
| 16.5 | call | 2026-05-29 | ask | $10k | 100 |
| 20 | call | 2026-07-17 | ask | $10k | 70 |

- **10 of 12 top bets are calls**, but the two largest (20C '28 mid, 17.5C 6/18 bid)
  are not aggressive buying. The genuine ask-side call buys (18.5C 6/5, 20C 7/17,
  17.5C 7/17, 16.5C 0DTE) are **$10–12k each** — small. The lone notable put is a
  **30C-distance 30P 6/18 ask** ($12k) — trivial. Net: call-leaning, low aggression.

## Expiry concentration (`uw options-flow expiry-heatmap`) `[FLOW:expiry-heatmap]`

| Expiry | Call prem | Put prem | Call/Put |
|--------|-----------|----------|----------|
| 2026-07-17 | $268k | $10k | 26.8 |
| 2026-06-18 | $224k | $56k | 4.0 |
| 2026-06-05 | $173k | $53k | 3.3 |
| 2026-05-29 (0DTE) | $181k | $27k | 6.7 |
| 2026-09-18 | $84k | $37k | 2.3 |
| 2028-01-21 (LEAP) | $101k | $4k | 25.3 |

- **Call premium leads every expiry**, heavily so in 7/17 (26.8×) and the '28 LEAP —
  but the absolute figures are small. The 7/17 monthly is the call-skew focal point
  (matches phase-0.5's fresh 20C/30C 7/17 OI builds).

## DTE regime (`uw options-flow dte-volume-share`) `[FLOW:dte-volume-share]`

- regime_hint **BALANCED** — 0DTE **0%**, weeklies 21%, monthlies 26%, LEAPs 3.5%.
  Spread positioning, no same-day gamma scramble.

## Tool calls

```bash
uw options-flow sweeps             --symbol FSLY --date 2026-05-29 --json   # 0 sweeps
uw options-flow top-premium-trades --symbol FSLY --date 2026-05-29 --top-n 12 --json
uw options-flow expiry-heatmap     --symbol FSLY --date 2026-05-29 --json
uw options-flow dte-volume-share   --symbol FSLY --date 2026-05-29 --json
```

## Tool errors

none (0 sweeps is an empty result, not an error — surfaced as a signal).

## Read-through

- Phase-1 **does not upgrade** phase-0.5's quiet read. The +4.9% close came with
  **no sweeps, trivial single-trade premium, and mixed bid/ask aggression** — the
  options market did not lead this move with conviction. The call-tilt (call premium
  leading every expiry, 7/17 26.8× skew) is genuine but small.
- The only forward-looking hook is **squeeze-lottery positioning**: fresh deep-OTM
  upside calls (20C/30C 7/17, 45C 6/18) on a 14.6%-short-float name. That is a
  *tail* bet — cheap optionality on another squeeze leg — not core directional flow.
- **Hands to phase-2/3:** with flow this thin, the dark-pool cash tape (phase-2) and
  the OI walls / squeeze positioning (phase-3) carry far more weight than usual in
  deciding whether there's any tradeable edge. Treat phase-1 as a faint
  weak-bullish prior, conviction LOW.

## Citations

- `[FLOW:sweeps]` 0 sweeps on a +4.9% day — `uw options-flow sweeps`
- `[FLOW:top-premium-trades]` largest single trade $79k 20C '28 LEAP (mid); 10/12 calls but mixed bid/ask — `uw options-flow top-premium-trades`
- `[FLOW:expiry-heatmap]` call premium leads every expiry (7/17 $268k vs $10k put) — `uw options-flow expiry-heatmap`
- `[FLOW:dte-volume-share]` BALANCED, 0DTE 0% — `uw options-flow dte-volume-share`

## Upstream references

- phase-0.5-context.md §Self-history — "volume 9th pctile, total premium 15th";
  phase-1 confirms the *mechanism*: zero sweeps, sub-$100k single trades — light tape.
- phase-0-intake.md §Finviz — "short float 14.64%"; the fresh deep-OTM call builds
  are the squeeze-lottery footprint this short base can produce.

## Next phase

- phase-2-dark-pool.md (does the $10.5M dark-pool tape show small-cap accumulation
  at ~$17.5, or is it as thin/neutral as the options flow?)
