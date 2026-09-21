# Phase 3 — Open Interest & Positioning

**Ticker:** BABA
**As-of date:** 2026-05-27
**Generated:** 2026-05-28T03:18:00Z
**Upstream phases cited:** phase-0.5-context.md, phase-1-flow.md, phase-2-dark-pool.md

## Summary

OI changes are **light, diffuse, and mixed** — no structural conviction build.
Biggest single increase is only **+1,662 at C130 5/29 (2 DTE)** against 1.76M
total chain OI — incremental, not structural `[OI:biggest_increases]`. The
near-dated builds cluster at the 5/29 OPEX-week calls (C129/130/132/135), the one
notable longer-dated bullish build is **C140 7/17 (+1,103)**, and the one
notable bearish build is a **long-dated P110 Mar-2027 hedge (+1,001)**. Closures
are concentrated in **higher OTM calls ($145–180, led by C150 −1,115)** — the
upside bets from when BABA traded ~$145 are being abandoned as the stock sits at
$128 `[OI:decrease_with_volume]`. Read against phase-1 (calls net *sold*) and
phase-2 (block buying at $126.5), the 5/29 C130–135 build is most consistent with
**covered-call overwriting against accumulated stock**, not fresh speculation.
**No pin risk and no OPEX concentration cliff** flagged for BABA `[OI:pin_risk]`.

## Key signals

- **Top OI build C130 5/29 +1,662** (vol 3,287) — near-dated, OPEX-week, small
  `[OI:biggest_increases]`.
- **Bullish dated build C140 7/17 +1,103**; the closest thing to an upside target
  build `[OI:smart_positioning]`.
- **Bearish dated build P110 Mar-2027 +1,001** — long-dated downside hedge floor
  `[OI:smart_positioning]`.
- **Upside calls unwinding: C150 −1,115, C145 −310, C180/C160/C170/C165 down** —
  old $145-era longs capitulating `[OI:decrease_with_volume]`.
- **No pin risk / no OPEX cliff** for BABA (OI too diffuse vs universe)
  `[OI:pin_risk]`, `[OI:opex_concentration]`.

## Detailed findings

### Largest OI increases `[OI:biggest_increases]` / direction `[OI:smart_positioning]`

| strike/exp | DTE | OI Δ | vol | inferred dir |
|-----------|----:|-----:|----:|------|
| **C130 5/29** | 2 | +1,662 | 3,287 | bullish |
| **C140 7/17** | 51 | +1,103 | 1,667 | bullish |
| **P110 Mar-2027** | 296 | +1,001 | 1,005 | bearish (hedge) |
| C132 5/29 | 2 | +645 | 961 | bullish |
| C135 5/29 | 2 | +639 | 1,497 | bearish |
| C140 (9DTE) | 9 | +615 | 803 | bearish |
| C129 5/29 | 2 | +554 | 1,221 | bullish |
| C140 | — | +543 | 1,220 | bullish |

Near-dated (2 DTE / 5/29) builds dominate by count — C129/130/132/135 — exactly
the strikes where phase-1 showed **call premium being sold** ($533K C135, $353K
C130 on the bid). The overwriting interpretation is the parsimonious one.

### Closing / roll activity `[OI:decrease_with_volume]`

| strike | OI Δ | vol |
|--------|-----:|----:|
| C150 | −1,115 / −349 / −95 / −78 | 1,786 / 2,626 / … |
| C145 | −310 | 497 |
| C180 | −168 | 282 |
| C160 | −94 / −88 / −57 | 292 / 351 / 166 |
| C170 | −62 | 156 |
| C165 | −52 | 109 |

All closures are **higher OTM calls ($145–180)** — the upside positioning from
BABA's ~$145 high (05-13, see phase-0.5 trail) being unwound into the decline.
Mildly bearish: the bull case above $145 is being given up. **No position rolls
detected** today (`rolls_detected = 0`).

### Pin risk & OPEX concentration `[OI:pin_risk]` `[OI:opex_concentration]`

- **BABA not flagged for pin risk** despite 5/29 OPEX being 2 DTE — its near-spot
  OI is too small/diffuse to pin (cf. HYG topping the list with 511k OI at one
  strike). No pin trade.
- **BABA not in the ≥40%-concentration list** — no single-expiry OI cliff. The
  1.76M total OI is spread across many strikes/expiries.

## Tool calls (audit trail)

| Command | Result summary |
|---------|----------------|
| `uw oi biggest-increases --symbol BABA --min-oi-change 500` | top +1,662 C130 5/29; all small |
| `uw oi decrease-with-volume --symbol BABA --min-volume 100` | C145–180 calls unwinding |
| `uw oi smart-positioning --symbol BABA --min-oi-change 500` | mixed: bullish 129/130/132/140, bearish 110/135 |
| `uw oi position-rolls --symbol BABA --near-dte-max 30` | 0 rolls detected |
| `uw oi pin-risk --dte-max 7` | BABA absent |
| `uw oi opex-concentration --min-concentration-pct 40` | BABA absent |

## Tool errors

- `biggest-increases` / `decrease-with-volume` / `smart-positioning` return null
  `option_type` and `expiry` in the row body; strike+type+expiry reconstructed
  from `uw insights deep-dive`'s `uw_top_oi_changes` (OPRA symbols, e.g.
  `BABA260529C00130000` = C130 5/29) and the `smart_positioning` `direction` field.

## Verdict for downstream

- **Positioning bias:** **mixed/light, net mildly bearish at the margin.** Fresh
  builds are small and OPEX-week (likely covered-call overwriting); the structural
  tells are a long-dated **P110 Mar-2027 hedge build** and **upside-call
  capitulation ($145–180 closing)**. The lone clean bullish dated build is C140 7/17.
- **Conviction:** **2 / 5.** Diffuse, incremental, no pin/cliff, no rolls.
- **Largest OI build as % of float:** 1,662 × 100 / 2.40B = **0.007%** —
  negligible; not a structural bet for a 2.40B-float name `[OI:oi_pct_float fz]`.
- **Three reference strikes for phase-9:**
  1. **C130 5/29** — biggest near-dated build; the overwriting/pin-ish strike
     (price magnet into Friday, capped upside).
  2. **C140 7/17** — the upside target/reclaim build; bulls need $129–131 reclaim
     first (phase-2 supply node) to chase this.
  3. **P110 Mar-2027** — the structural downside-hedge floor reference.
- **Open questions:** Confirmed-covered overwriting vs speculation? (phase-4 GEX/
  dealer should show whether C130–135 is dealer-short = upside resistance.) Does the
  upside-call unwind plus P110 hedge mean institutions have flipped from the
  $145-era bull thesis to defensive? (phase-7b/8 to weigh.)
