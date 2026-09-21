# Phase 4 — Dealer Structure & Gamma

**Ticker:** RKT
**As-of date:** 2026-06-05
**Generated:** 2026-06-06T17:18:00-04:00
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md

## Summary

The tool labels RKT's ≤45DTE dealer book **`regime: POSITIVE` — "Dealers net
long gamma — expect mean-reversion and reduced volatility"** with
`zero_gamma_level` **7.71** (far below spot 12.59), but the per-strike
cross-check shows that headline is carried by the call walls above: the strikes
**around spot are a negative-gamma pocket** ($13 net_gex **−4.59M** — the
largest absolute strike on the surface; $12/-1.13M, $12.5/−0.82M, $14/−0.70M),
flipping positive only at $13.5 and decisively at $14.5–$17 (+1.75M to +2.07M).
DEX says the public is net put-long and the **dealer hedge is to SELL
underlying** (net_dex −39.9M). Vanna is the offset: a put-heavy book primed for
a **vanna squeeze if IV falls**. Near-expiry max pain sits **above** spot
(Jun-12 → $14, Jun-18 → $14.5), agreeing with phase-3's wall map that the chain's
gravity is upward into mid-June OPEX even as flow (phase-1) leans bearish.

## Key signals

- `regime: "POSITIVE"`, `regime_description: "Dealers net long gamma — expect
  mean-reversion and reduced volatility"`, `total_gex` 1,333,718,
  `zero_gamma_level` 7.71, spot 12.59 [STRUCT:gex]
- Per-strike cross-check: $13 net_gex **−4,587,931** (largest |GEX| strike);
  negative band $12–$14; positive wall band $14.5 (+1,748,609), $15
  (+1,778,090), $16 (+2,073,555) [STRUCT:gex per_strike]
- `net_dex` **−39,893,544** (put_dex −59,835,418 / call_dex +19,941,875);
  interpretation verbatim: *"Public is net put-long → dealers net short puts →
  dealer hedge is to SELL underlying."* [STRUCT:dex]
- `net_vanna` +1,711, `net_charm` +87,243; verbatim: *"Classic vanna-squeeze
  setup if VIX collapses"* (falling IV → dealers short puts buy back underlying)
  [STRUCT:vanna_charm]
- Term skew `interpretation: "COMPLACENT"` — 25Δ **calls richer than puts**
  (call_25d_iv 0.6063 vs put_25d_iv 0.5811, skew_ratio 0.958): speculative call
  demand, zero put fear [STRUCT:term_skew]
- Max pain: Jun-12 → **$14** (+10.76%), Jun-18 → **$14.5** (+14.72%, total_oi
  113,579), Jun-26 → $13.5, Jul-02 → $12.5 [STRUCT:max_pain]

## Detailed findings

### GEX

| Field | Value |
|---|---|
| regime / description | POSITIVE — "Dealers net long gamma — expect mean-reversion and reduced volatility" |
| total_gex | 1,333,718 |
| zero_gamma_level | 7.71 (coarse on a $12.59 name — treat as a far-OTM aggregate crossing, ±2% band per pitfall; not a tradeable level) |
| underlying_price | 12.59 |

Top strikes by |net_gex|:

| Strike | net_gex | Side of spot |
|---|---|---|
| **13** | **−4,587,931** | +3.3% |
| 16 | +2,073,555 | +27% |
| 15 | +1,778,090 | +19% |
| 14.5 | +1,748,609 | +15% |
| 12 | −1,125,296 | −4.7% |
| 17 | +1,018,548 | +35% |
| 12.5 | −823,000 | −0.7% |
| 14 | −700,818 | +11% |
| 15.5 | +590,667 | +23% |
| 13.5 | +461,592 | +7% |

Read (cross-check, not re-derivation): the tool's aggregate label is POSITIVE,
but spot sits inside a **local short-gamma pocket ($12–$14)** — moves inside
this band get amplified by dealer hedging, while the $14.5–$16 positive-gamma
wall acts as a brake/ceiling. This matches phase-3's call-wall staircase
(oi-by-strike: 14.5/15/16 call_wall_resistance) and phase-2's $12.94–13.26
overhead DP supply.

### DEX

call_dex +19,941,875; put_dex −59,835,418; **net_dex −39,893,544**.
Tool interpretation verbatim: *"Public is net put-long → dealers net short puts
→ dealer hedge is to SELL underlying."* Mechanical dealer supply pressures
rallies until the put book decays or IV drops.

### Vanna + charm

net_vanna +1,711 (call_vanna −1,526 / put_vanna +3,237), net_charm +87,243.
Verbatim: *"Public net vanna positive (put-heavy book). Falling IV → |put delta|
drops → dealers (short puts) cover by BUYING underlying. Classic vanna-squeeze
setup if VIX collapses."* Positive charm points the same way into expiry: as
ITM/ATM put deltas bleed, dealer short-put hedges unwind via buying. **The
squeeze trigger is falling IV** — phase-6's regime read decides whether that's
live.

### IV term structure

`structure: "BACKWARDATION"` (tool label). Rows (`avg_iv` by expiry):
0DTE 4.3803 (expiry-day artifact, dte_approx −1 — distorts the label),
Jun-12 0.6516, Jun-18 0.6328, Jun-26 0.5932, Jul-02 0.6089, Jul-10 0.6439
(52-OI noise), Jul-17 0.5924, Jul-24 0.6025, **Aug-21 0.6697, Sep-18 0.7016**,
Dec-18 0.6488, Jan-27 0.6518. Shape ex-0DTE: mild front backwardation
(Jun-12 > Jun-26 trough 0.5932) then **upward kink into Aug/Sep** — consistent
with the 2026-07-30 earnings (phase-0.5 `.uw_screener.next_earnings_date`)
sitting between Jul-24 and Aug-21 expiries. Not post-earnings normalization
(earnings 55 days away) — the front-end stress is mild and positional.

### Term skew (dte_target 30, actual 26)

call_25d_iv 0.6063 > put_25d_iv 0.5811; skew −0.0252; skew_ratio 0.958;
`interpretation: "COMPLACENT"`. Inverted (call-rich) skew on a Financial
Services name = upside-chase pricing, no tail-hedge demand — unusual given
phase-1's put-buying tilt; the put buying is ITM/short-dated, not OTM crash
protection.

### Front-end IV ratio (near 6d / far 26d)

near_iv 0.6516 / far_iv 0.6089 → `ratio` **1.07**, `regime: "BACKWARDATION"`.
Mild front-end stress with **no earnings inside the window** (next 2026-07-30) —
likely macro-week premium (phase-6 to attribute) rather than a name catalyst.

### Today's gamma flip

Skipped — 0DTE-intraday tool; this is an after-hours/as-of run (per phase
guidance, only meaningful during the session).

### Max pain (`--dte-max 30`; static-OI caveat — softer the further the expiry)

| Expiry | DTE | max_pain_strike | distance_pct | put_call_oi_ratio | total_oi |
|---|---|---|---|---|---|
| 2026-06-05 | 0 | 14.0 | +10.76 | 0.224 | 47,104 (expired) |
| **2026-06-12** | 7 | **14.0** | +10.76 | 0.817 | 20,716 |
| **2026-06-18** | 13 | **14.5** | +14.72 | 0.364 | 113,579 |
| 2026-06-26 | 21 | 13.5 | +6.80 | 0.844 | 4,723 |
| 2026-07-02 | 27 | 12.5 | −1.11 | 0.360 | 552 |

Near-expiry magnets sit **above spot**: $14 into Jun-12 and $14.5 into the
Jun-18 OPEX that holds 23.77% of all OI (phase-3 term-structure cliff). Max pain
agreeing with the $14.5 call wall (phase-3) and the phase-1 short-call line at
$14.5 makes $14.5 the single most-corroborated level in the structure stack.
Caveat: with spot in a negative-gamma pocket, max-pain pull is weaker than the
label suggests — static-OI estimate.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw options-structure gex --symbol RKT --dte-max 45 --date 2026-06-05 --json` | regime/ZGL ← `.regime`/`.zero_gamma_level`; pocket ← `.per_strike[]` sorted by \|net_gex\| | full surface |
| `uw options-structure dex --symbol RKT --dte-max 45 --date 2026-06-05 --json` | −39,893,544 ← `.net_dex`; `.interpretation` verbatim | aggregate |
| `uw options-structure vanna-charm --symbol RKT --dte-max 45 --date 2026-06-05 --json` | +1,711/+87,243 ← `.net_vanna`/`.net_charm`; `.vanna_interpretation` verbatim | aggregate |
| `uw options-structure iv-term-structure --symbol RKT --date 2026-06-05 --json` | BACKWARDATION ← `.structure`; rows ← `.term_structure[].avg_iv` | 15 expiries |
| `uw options-structure term-skew --symbol RKT --dte-target 30 --date 2026-06-05 --json` | COMPLACENT ← `.interpretation`; 0.958 ← `.skew_ratio` | 1 |
| `uw options-structure front-end-iv-ratio --symbol RKT --near-dte 7 --far-dte 30 --date 2026-06-05 --json` | 1.07 ← `.ratio`; `.regime` | 1 |
| `uw options-structure max-pain --symbol RKT --dte-max 30 --date 2026-06-05 --json` | strikes ← `.results[].max_pain_strike` | 5 expiries |
| `today-gamma-flip` | skipped — intraday-only tool, after-hours run | — |

## Tool errors

None. (First `jq` draft read `.term_structure[].atm_iv`/`.dte` which don't exist
— nulls returned, nothing transcribed; corrected to `.avg_iv`/`.dte_approx` after
inspecting row keys.)

## DATA NOTE / CORRECTION

IV-TS row fields corrected pre-write (`atm_iv`→`avg_iv`, `dte`→`dte_approx`);
all quoted values come from the validated second read.

## Verdict for downstream phases

- **Dealer regime:** **Transitional** — headline long-gamma (`POSITIVE`, ZGL
  7.71 ≪ spot) but spot sits in a local $12–$14 short-gamma pocket; true
  positive-gamma stabilization only kicks in at $13.5/$14.5+. Net dealer delta
  hedge is a seller (net_dex −39.9M); offset by a live vanna-squeeze setup **if
  IV falls**.
- **Conviction:** 3/5 (signals internally consistent; ZGL coarse per pitfall;
  GEX on a mid-cap is directionally useful, not precise)
- **Structural levels for phase 9:**
  1. **$13.0** — largest |GEX| strike (−4.59M, amplifier not wall) + Jun-26 max
     pain at 13.5 right above; the friction/acceleration zone.
  2. **$14.5** — Jun-18 max-pain magnet + +1.75M GEX wall + phase-3 call wall +
     phase-1 fresh short-call line: the most corroborated cap in the stack.
  3. **$12.0–$12.5** — negative-GEX shelf below spot (−1.13M/−0.82M): in the
     local short-gamma pocket a break of $12.5 accelerates (no dealer bid, no DP
     shelf per phase-2).
  - Near-expiry max-pain pin: **$14 (Jun-12) / $14.5 (Jun-18)** — upward OI
    gravity into OPEX.
- **Open questions:** Does the macro regime (phase-6) support the IV-decline
  trigger for the vanna squeeze? Is the front-end 1.07 backwardation macro-week
  premium or name-specific? Does historical behavior (phase-5) show RKT
  respecting max-pain pulls into monthly OPEX?
