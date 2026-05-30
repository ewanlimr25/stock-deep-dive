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
| `uw oi oi-by-strike --symbol <S> --top-n 10 --json` | **Heaviest strikes ranked by total OI, with role tagging** (`call_wall_resistance` / `put_wall_support` / `call_heavy` / `put_heavy`) + `distance_pct` from spot. The native call/put-wall map — use this instead of hand-reconstructing walls from the raw chain. Add `--dte-max 30` or `--expiry <D>` to narrow from the all-expiry aggregate. |
| `uw oi term-structure --symbol <S> --json` | **OI distribution across all expiries** — per-expiry call/put OI, P/C ratio, and `pct_of_total_oi`. Spot OPEX cliffs at a glance (the expiry holding the largest OI fraction). Ticker-scoped; no market-wide filter needed. |

## Composition guidance

- `uw oi pin-risk` and `uw oi opex-concentration` are MARKET-WIDE; filter to
  `<SYMBOL>` after. `uw oi oi-by-strike` and `uw oi term-structure` are
  **ticker-scoped** (`--symbol`) — no post-filter needed.
- **`uw oi oi-by-strike` is the canonical wall map** — prefer it over deriving
  walls from `greeks`/`biggest-increases` by hand (manual reconstruction is where
  strike/type parsing errors creep in). Trust its `role` tag and `distance_pct`,
  but read `net_oi` (call_oi − put_oi) to judge whether a "heavy" strike is a true
  resistance/support wall vs a two-sided `call_heavy`/`put_heavy` battleground.
- **`uw oi term-structure` is the OPEX-cliff lens** — the expiry with the largest
  `pct_of_total_oi` is the gravity well; cross-check it against phase-4 max-pain
  and phase-6's catalyst calendar.
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
   - ### OI walls by strike (`oi-by-strike` table: strike, call_oi, put_oi,
     net_oi, role, distance_pct — the resistance/support map for phase-9 levels)
   - ### OI term structure (`term-structure`: per-expiry P/C + pct_of_total_oi;
     name the OPEX cliff = largest pct_of_total_oi expiry)
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
   - Three pin/cliff strikes for phase-9 entry/stop reference — source them from
     `oi-by-strike` roles (call_wall_resistance / put_wall_support) and the
     `term-structure` OPEX cliff, not hand-picked levels
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
- `oi-by-strike` `role` is a heuristic from the call/put split at the strike — a
  `call_heavy` strike (e.g. a 200 with large call AND put OI) is a two-sided
  battleground, not a clean wall; quote `net_oi` alongside the role so phase-9
  doesn't mislabel it as pure support/resistance.
- `oi-by-strike` defaults to the **all-expiry aggregate** — a wall there may be a
  far-dated LEAP strike, not a near-term level. Use `--dte-max 30` (or `--expiry`)
  for the tradeable-horizon wall map that phase-9 actually sizes against.
