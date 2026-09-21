# Phase 3 — Open Interest & Positioning

**Ticker:** SNOW · **As-of:** 2026-05-29 · **Generated:** 2026-05-29
**Upstream:** phase-2-dark-pool.md (mega-tier distribution) · phase-1-flow.md
(ITM call closing + put hedging) · phase-0 (float 334.88M, spot $255.55)

## Summary

OI tells a **roll-up / repositioning** story that partly counterbalances the
phase-1/2 distribution read: traders are **closing the now-deep-ITM lower-strike
calls** ($185/$190/$200/$210/$225C — the pre-earnings positions that the gap-up
left ITM, the largest decreases) `[OI:decrease-with-volume]` and **opening fresh
OTM upside calls at $280–$350** (June-18 $300C +3,817 is the biggest structural
build, plus Jul $290/$280C, Jun-05 $350/$280C, Aug $300C) `[OI:biggest-increases]`.
So one cohort is booking the earnings gain (consistent with the dark-pool
distribution) while another is **betting on continuation higher**. Against the
bull build sits a downside hedge stack — Dec-2026 $220P (+1,881) and a cluster of
0DTE $200–$230 puts. Net: **mixed, with a genuine speculative bullish-continuation
build above $280** that the cautious phases 1–2 lacked. No pin risk and no
≥40% OI cliff (June OPEX >7d; mega-cap OI is distributed).

## Key signals

- **Fresh OTM upside calls $280–$350** — Jun-18 $300C **+3,817**, Jul-17 $290C
  +2,647, Jun-05 $350C +2,585, Aug-21 $300C +1,999 `[OI:biggest-increases]`.
  Real continuation bets, but speculative (spot $255 → $300C is +18% OTM).
- **ITM calls being CLOSED** — 0DTE $200C −3,399, $185C −2,894; Jun-18 $200C
  −2,837, $210C −2,734 `[OI:decrease-with-volume]`. Profit-taking on the
  pre-earnings positions the gap left ITM = the OI face of phase-2 distribution.
- **0DTE noise dominates raw** — $250C +4,075, $260C +2,654, plus 0DTE
  $220/$200/$230P `[OI:biggest-increases]`; discard for directional intent.
- **Downside hedge** — Dec-2026 $220P +1,881 (structural) `[OI:biggest-increases]`
  — a longer-dated insurance leg under the rally.
- **No pin / no cliff** — SNOW absent from `pin-risk` and `opex-concentration`
  `[OI:pin-risk][OI:opex-concentration]`; no single-strike gamma magnet this week.

## Detailed findings

### Largest OI increases (non-0DTE structural, decoded)
| Strike | Type | Expiry | OI Δ | Read |
|---|---|---|---|---|
| 300 | call | Jun-18 | +3,817 | biggest upside build |
| 290 | call | Jul-17 | +2,647 | continuation |
| 350 | call | Jun-05 | +2,585 | far-OTM upside |
| 300 | call | Aug-21 | +1,999 | longer upside |
| 220 | put | **Dec-2026** | +1,881 | structural downside hedge |
| 280 | call | Jul-17 | +1,790 | upside |
| 245 | call | Jun-05 | +1,470 | near-the-money upside |

### Closing / roll activity
| Strike | Type | Expiry | OI Δ | Read |
|---|---|---|---|---|
| 200 | call | 0DTE | −3,399 | ITM, closed |
| 185 | call | 0DTE | −2,894 | ITM, closed |
| 200 | call | Jun-18 | −2,837 | ITM, profit-taking |
| 210 | call | Jun-18 | −2,734 | ITM, profit-taking |
Clear **roll-up signature**: close ITM lower strikes, open OTM $280–$350.

### Smart positioning / pin / cliff
No pin-risk, no opex concentration ≥40%. Mega-cap OI is distributed across many
strikes; no mechanical pin to trade this week.

### Float normalization (advisory)
Largest structural build = Jun-18 $300C +3,817 ≈ 381,700 sh-equiv = **0.114% of
the 334.88M float** `[OI:oi_pct_float fz]` — immaterial as a footprint;
speculative option positioning, not stock-equivalent accumulation.

## Tool calls
| Tool | Args | Result |
|---|---|---|
| `oi biggest-increases` | `--min-oi-change 500 --top-n 18` | OTM $280-350 calls + Dec $220P |
| `oi decrease-with-volume` | `--min-volume 100 --top-n 8` | ITM calls closed (roll-up) |
| `oi pin-risk` | `--dte-max 7 --max-distance-pct 5` | SNOW absent |
| `oi opex-concentration` | `--min-concentration-pct 40` | SNOW absent |

## Tool errors
(none)

## Verdict for downstream

- **Positioning bias: MIXED — speculative bullish-continuation build above $280**
  (June $300C the largest) **vs ITM profit-taking + Dec $220P hedge.** This is the
  more constructive counterweight to the phase-1/2 distribution: a real cohort
  is positioning for further upside, just via OTM calls.
- **Conviction: 3 / 5.**
- **Largest structural build = 0.114% of float** (advisory) — immaterial.
- **Three strikes for phase-9:**
  1. **$280–$300** — upside call-OI magnet / continuation target band.
  2. **$255–$260** — near-the-money battleground (0DTE calls + phase-2 close).
  3. **$220–$230** — downside hedge strikes (Dec $220P + 0DTE puts); the
     protection floor.
- **Open questions:**
  - Does dealer gamma (phase-4) support a push toward the $280 call wall, or pin
    SNOW near $255 where phase-2 distribution is heaviest?
  - The roll-up (close ITM, open OTM) keeps net delta long but moves the strike
    higher — is that conviction or just "letting winners ride OTM"? Phase-8b debate.
