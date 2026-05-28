# Phase 3 — Open Interest & Positioning

## Goal

Map where positions are being built, rolled, or closed across the option
chain. Identify pin risk and OPEX cliffs. Emit `phase-3-positioning.md`.

## Tools

All take `--json`; ticker-scoped ones take `--symbol <S>` and `--date <AS-OF>` if
not today. `biggest-increases` reports the absolute delta in `oi_diff_plain` (the
fractional `oi_change` field is the ratio, not the delta).

| Command | What it answers |
|---------|-----------------|
| `uw oi biggest-increases --symbol <S> --top-n 20 --min-oi-change 500 --json` | Largest new positions opened |
| `uw oi decrease-with-volume --symbol <S> --top-n 15 --min-volume 100 --json` | Closing or roll activity |
| `uw oi smart-positioning --symbol <S> --top-n 20 --min-oi-change 500 --json` | Inferred directional positioning (omit `--direction` for both) |
| `uw oi position-rolls --symbol <S> --threshold 500 --near-dte-max 30 --json` | Near→far expiry rolls |
| `uw oi pin-risk --top-n 25 --dte-max 7 --max-distance-pct 5 --json` | OPEX-week pin candidates |
| `uw oi opex-concentration --top-n 20 --min-concentration-pct 40 --json` | Per-ticker OI cliffs |

## Composition guidance

- `uw oi pin-risk` and `uw oi opex-concentration` are MARKET-WIDE; filter to
  `<SYMBOL>` after.
- If today is > 7 calendar days from OPEX, `uw oi pin-risk` will likely return
  empty — record that and skip pin commentary.
- **Float-normalize the OI build (D2, advisory).** If phase-0 captured `Shs Float`
  (`fz`, `lib/fz-recipes.md`), express the largest OI increase as a **% of float**
  in share-equivalent terms (`OI_Δ × 100 / Shs Float × 100`). A 50k-contract build
  is a structural bet in a small-float name and a rounding error in a mega-float
  one. **Advisory context, not a new gate**; never raises conviction. Tag
  `[OI:oi_pct_float fz]`. Skip if `fz_available=no`.

## Output sections

1. **Summary** — net positioning: who's building, who's closing, what side.
2. **Key signals** — top-5 with `[OI:<tool>]` citations.
3. **Detailed findings**
   - ### Largest OI increases (table: strike, expiry, side, OI Δ, vol)
   - ### Closing / roll activity (decreases + position rolls)
   - ### Smart positioning (inferred direction)
   - ### Pin risk (if within OPEX week)
   - ### OPEX concentration (cliff strikes within 5% of spot)
4. **Tool calls** — audit.
5. **Tool errors** — verbatim.
6. **Verdict for downstream**
   - Positioning bias (calls being built / puts being built / hedges /
     rolling out)
   - Conviction 1–5
   - Largest OI build as **% of float** (share-equivalent; advisory, "n/a" if no
     `Shs Float`) — one line on whether the build is structural for this name
   - Three pin/cliff strikes for phase-9 entry/stop reference
   - Open questions (e.g., "is the call buildup speculative or covered?")

## Interpretation heuristics

- **Speculative call buildup:** OI Δ concentrated in near-DTE, OTM strikes
  with high vol/OI ratio (cross-ref phase-1).
- **Covered-call writing:** OI Δ in near-DTE, slightly OTM calls coinciding
  with phase-2 institutional accumulation = institutions writing premium
  against stock holdings.
- **Hedging:** OI Δ in puts with strikes ~10% OTM and DTE matching upcoming
  catalysts (phase-6 calendar).
- **Roll signature:** decreases in near-DTE strike X coinciding with
  increases in far-DTE same strike = position rolling.

## Common pitfalls

- OI updates daily after close; intraday calls will see prior-day OI.
- `uw oi smart-positioning` infers direction from OPRA symbol parsing — for
  unusual ticker symbols (e.g. dual-class shares), verify by spot-checking
  one contract manually.
- A single 50,000-contract OI increase in a far-DTE strike can be a hedge
  fund's structural position, not a directional bet — flag and contextualize.
