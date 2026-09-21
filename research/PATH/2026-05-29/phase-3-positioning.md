# Phase 3 — Open Interest & Positioning

**Ticker:** PATH · **As-of:** 2026-05-29 · **Generated:** 2026-05-29
**Upstream:** phase-2-dark-pool.md (mild accumulation, $12 supply question,
"is the build speculative or covered?") · phase-1-flow.md (LEAP call lean) ·
phase-0-intake.md (Shs Float 412.34M)

## Summary

Open-interest builds confirm phase-1/2's read: **a mild, speculative bullish
call buildup in the near term, partly offset by downside put hedges, with 0DTE
dominating the raw numbers.** Stripping the same-day-expiry noise, the real
structural adds are **June-18 calls at $12/$13/$15** (oiΔ +3,620 / +4,023 /
+3,692) and a scatter of $14–$15 July calls — speculative upside positioning in
the $12–$15 band *above* spot ($11.72). Against that, fresh **put OI builds**
appear at July $10P, Sept $9P and a high-volume **Jan-2027 $8P** (oiΔ +1,452 on
vol 10,738) — tail/downside hedging. The largest *decrease* is the **Jan-2027
$30C closing** (oiΔ −3,170) — someone abandoning a deep-OTM upside bet, mildly
deflationary for the far-upside narrative. **No pin risk** (nearest monthly OPEX
June-18 is >7 days out) and **no single-strike OI cliff ≥40%** of chain.

## Key signals

- **June-18 call buildup, $12–$15** — 13C +4,023, 15C +3,692, 12C +3,620
  `[OI:biggest-increases]`. Real (non-0DTE), near-term speculative bullish — the
  structural footprint behind phase-1's call premium.
- **0DTE dominates and is noise** — the six largest raw builds are all
  same-day-expiry (13C +5,888, 12C +4,657, 12.5C +3,702, plus 0DTE 11P/12P/10P)
  `[OI:biggest-increases]`. Discard for directional intent (phase-0.5 / phase-1).
- **Downside hedges building** — July $10P +1,577, Sept $9P +1,745, **Jan-2027
  $8P +1,452 on vol 10,738** `[OI:biggest-increases]`. Tail protection / bearish
  insurance under spot — the offset to the call lean.
- **Far-upside bet abandoned** — Jan-2027 **$30C −3,170** is the single largest
  OI *decrease* `[OI:decrease-with-volume]` — a $30-by-2027 call being closed;
  trims the blue-sky tail, neutral-to-slightly-bearish for the long-dated story.
- **No pin / no cliff** — PATH absent from `pin-risk` (dte≤7, ≤5% dist) and
  `opex-concentration` (≥40%) `[OI:pin-risk][OI:opex-concentration]`. Gamma pin
  mechanics are not a factor this week.

## Detailed findings

### Largest OI increases (non-0DTE structural, decoded from OPRA symbols)
| Strike | Type | Expiry | OI Δ | Vol | Read |
|---|---|---|---|---|---|
| 13 | call | Jun-18 | +4,023 | 6,048 | speculative upside |
| 15 | call | Jun-18 | +3,692 | 7,713 | upside target band |
| 12 | call | Jun-18 | +3,620 | 6,664 | just-OTM upside |
| 15 | call | Jul-17 | +2,014 | 2,895 | upside |
| 14 | call | Jun-05 | +1,811 | 2,555 | upside |
| 11 | call | Sep-18 | +1,798 | 2,247 | longer upside |
| 9 | put | Sep-18 | +1,745 | 3,836 | downside hedge |
| 10 | put | Jul-17 | +1,577 | 1,923 | downside hedge |
| 8 | put | **Jan-2027** | +1,452 | **10,738** | tail hedge / bearish bet |

0DTE builds (13C/12C/12.5C/18C/14C/15C and 11P/12P/10P/9.5P) excluded as pin noise.

### Closing / roll activity
| Strike | Type | Expiry | OI Δ | Read |
|---|---|---|---|---|
| 30 | call | Jan-2027 | −3,170 | far-upside bet closed |
| 10 | call | Jun-18 | −1,650 | ITM call closed/rolled |
| 18 | call | Jun-18 | −956 | OTM call closed |
| 11 | call | 0DTE | −949 | expiring |

No clean near→far roll signature; the $30C close is an outright exit, not a roll.

### Smart positioning
`smart-positioning` returned the same strike list with null direction fields
(CLI did not populate `direction` for PATH) — directional inference falls back to
the symbol-decoded type above: net call-heavy in $12–$15 June, put-heavy below
$10 in longer tenors.

### Pin risk / OPEX concentration
None. June-18 monthly OPEX is 20 days out (>7-day pin window); no ≥40%
single-strike concentration. **No gamma-pin reference for phase-9 this week.**

### Float normalization (advisory)
Largest *structural* build = June-18 13C +4,023 contracts ≈ 402,300 share-equiv
= **0.098% of the 412M float** `[OI:oi_pct_float fz]`. Largest raw (0DTE 13C)
+5,888 ≈ 0.143%. Either way **immaterial as a structural footprint** — these are
speculative option bets, not float-moving positioning.

## Tool calls
| Tool | Args | Result |
|---|---|---|
| `oi biggest-increases` | `--symbol PATH --min-oi-change 500 --top-n 20` | Jun 12–15 calls + downside puts |
| `oi decrease-with-volume` | `--symbol PATH --min-volume 100 --top-n 15` | 2027 30C closed |
| `oi smart-positioning` | `--symbol PATH --min-oi-change 500` | null direction (used symbol decode) |
| `oi pin-risk` | `--dte-max 7 --max-distance-pct 5 --top-n 40` | PATH absent |
| `oi opex-concentration` | `--min-concentration-pct 40 --top-n 40` | PATH absent |

## Tool errors
(none — `smart-positioning` `direction` field null for PATH; worked around via
OPRA-symbol decode.)

## Verdict for downstream

- **Positioning bias: MILDLY BULLISH (speculative).** Near-term June $12–$15
  call buildup above spot, consistent with phase-1 call lean and phase-2
  accumulation — but speculative (small contracts, partly 0DTE) and offset by a
  genuine downside-put hedge stack (Jul $10P, Sep $9P, 2027 $8P). Not a covered
  or high-conviction structural bet.
- **Conviction: 3 / 5** — direction agrees with phases 1–2 but the magnitude is
  small and the hedges are real. Phase-0.5 `+` cap holds.
- **Largest structural OI build = 0.098% of float** (advisory) — immaterial;
  speculative option positioning, not institutional accumulation in the chain.
- **Three strikes for phase-9:**
  1. **$12–$13** — near-term call wall / upside magnet (June OI cluster + DP
     $12 supply). First resistance.
  2. **$15** — speculative upside target (June/July call OI). Stretch objective.
  3. **$9–$10** — downside hedge strikes (Jul/Sep puts) ≈ where protection sits;
     a break below the phase-2 $11.20 shelf opens air toward this band.
- **Open questions:**
  - Is the June $12–$15 call OI dealer-short (gamma squeeze fuel given 31% short
    float) or covered writing? Phase-4 structure / GEX must resolve.
  - Does the 2027 $8P + $30C-close combo signal a smart-money "range-bound, fade
    the squeeze" view? Carry to phase-8b debate.
