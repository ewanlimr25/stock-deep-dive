# Phase 3 — Open Interest & Positioning

**Ticker:** INTC
**As-of date:** 2026-06-15
**Generated:** 2026-06-16T01:24:55Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md

## Summary

Positioning is **two-sided with a fresh bullish OTM call ladder built over an
existing call book that's being partly rolled/closed** — directionally constructive
but laced with financing and hedge structures, not a clean one-way bet. Fresh
upside call OI is building at **C130 (Jun18/Jun26), C140 (Jun18/Jun26), C150
(Aug21)** [OI:biggest_increases][OI:smart_positioning=bullish], while the single
largest build is a **deep-ITM Sep18 C97.5 (+63,781 contracts, $242.9M)** that
`smart-positioning` tags **bearish** (net bid-side) — reads as institutional
buy-write / financing, echoing phase-1's deep-ITM call *selling* and phase-2's
accumulation (institutions writing premium against stock) [OI:smart_positioning].
The wall map is clean: **$130 call wall (+1.7%, immediate resistance), $150 call
wall (+17.4%, upside magnet/cap)**, with **$120 call-heavy / $110 put-wall support**
below [OI:oi_by_strike]. The **06-18 expiry (3 DTE) holds 26.8% of all OI** —
this week's gravity well — but it is call-heavy (PCR 0.57) and INTC is **outside
the pin-risk top-25**, so no tight pin; if anything a mild upward OPEX drift bias.
Net positioning bias: **mildly bullish, conviction 3** — consistent with phases 1–2,
capped by the overhead call-wall supply.

## Key signals

- **$130 call wall, net_oi +37,683** (40,382 call vs 2,699 put OI, dte≤30), dist
  **+1.7%** — immediate overhead resistance just above spot [OI:oi_by_strike].
- **$150 call wall, net_oi +57,963** (58,242 call vs 279 put, dte≤30; 169k call OI
  all-expiry), dist **+17.4%** — the upside magnet *and* cap; OI actively building
  (Aug21 C150 +5,247) [OI:oi_by_strike][OI:biggest_increases].
- **Deep-ITM Sep18 C97.5 +63,781 OI** ($242.9M, avg $38.05), `smart-positioning`
  **bearish** (net_ask_bid −111) — buy-write/financing, overhead supply not a
  directional grab [OI:biggest_increases][OI:smart_positioning].
- **Fresh OTM call builds: C140 Jun26 +14,695, C140 Jun18 +4,467, C130 Jun18
  +3,200, C130 Jun26 +3,544** — all `smart-positioning` **bullish** [OI:smart_positioning].
- **06-18 OPEX cliff = 26.8% of all OI** (745,603 call / 425,199 put, PCR 0.57) —
  the heaviest expiry by far; call-heavy [OI:term_structure].
- **Calls being closed/rolled:** C90 Jul17 −4,525, C120 Jun18 −1,670, C120 Jul17
  −1,434, C150 Jun18 −788 — profit-taking on the existing book [OI:decrease_with_volume].

## Detailed findings

### OI walls by strike (`oi-by-strike`, dte ≤ 30 — tradeable map; spot $127.82)

| Strike | call_oi | put_oi | net_oi | role | dist |
|--------|---------|--------|--------|------|------|
| **150** | 58,242 | 279 | **+57,963** | call_wall_resistance | +17.4% |
| **130** | 40,382 | 2,699 | **+37,683** | call_wall_resistance | **+1.7%** |
| 120 | 41,553 | 11,145 | +30,408 | call_heavy | −6.1% |
| 110 | 18,190 | 26,706 | −8,516 | put_wall_support | −13.9% |
| 80 | 21,206 | 39,251 | −18,045 | put_wall_support | −37.4% |
| 70 | 41,469 | 47,770 | −6,301 | put_wall_support | −45.2% |
| 15 | 2,113 | 55,536 | −53,423 | put_wall_support | −88.3% (tail) |

All-expiry adds a huge legacy **$50 call_heavy (156k call OI)** and low-strike
clusters — relics of INTC's sub-$50 era, not tradeable levels. The near-term
picture: **spot pinned between the $130 call wall above and $120/$110 support
below**, with $150 the bigger upside cap.

### OI term structure (OPEX cliffs; total OI 4,363,446 across 18 expiries)

| Expiry | DTE | call_oi | put_oi | PCR | % of total OI |
|--------|-----|---------|--------|-----|---------------|
| **2026-06-18** | 3 | 745,603 | 425,199 | 0.57 | **26.8%** |
| 2026-12-18 | 186 | 337,517 | 241,325 | 0.72 | 13.3% |
| 2027-01-15 | 214 | 334,113 | 234,766 | 0.70 | 13.0% |
| 2026-07-17 | 32 | 244,271 | 197,825 | 0.81 | 10.1% |
| 2026-09-18 | 95 | 236,198 | 169,633 | 0.72 | 9.3% |

**06-18 is the gravity well** (>1 in 4 contracts), call-heavy. The next monthly
(07-17, PCR 0.81 — most put-heavy) is where phase-1's C90/C130/C150 flow concentrated.

### Largest OI increases (OPRA-parsed)

| Contract | Exp | Type/Strike | OI Δ | curr OI | vol | smart-dir |
|----------|-----|-------------|------|---------|-----|-----------|
| INTC260918C00097500 | Sep18 | C 97.5 (deep ITM) | **+63,781** | 63,935 | 63,836 | bearish (write/finance) |
| INTC260618P00070000 | Jun18 | P 70 (deep OTM) | +25,456 | 46,025 | 28,769 | bearish (tail) |
| INTC260626C00140000 | Jun26 | C 140 (OTM) | +14,695 | 16,320 | 20,314 | **bullish** |
| INTC260821C00150000 | Aug21 | C 150 (OTM) | +5,247 | 18,302 | 8,106 | **bullish** |
| INTC260618C00140000 | Jun18 | C 140 (OTM) | +4,467 | 15,456 | 18,784 | **bullish** |
| INTC260618C00130000 | Jun18 | C 130 (ATM+) | +3,200 | 26,547 | 22,908 | **bullish** |

Directional speculation (OTM calls) is bullish; the bearish-tagged builds are the
deep-ITM C97.5 write and deep-OTM put tails (P70, P62.5, Jan27 P100).

### Closing / roll activity

Calls closing across strikes: **C90 Jul17 −4,525** (heavy two-way vs phase-1's
ask buying — net churn), C120 Jun18 −1,670, C65 Jul17 −1,551, C120 Jul17 −1,434,
C125 Jun26 −1,074, C150 Jun18 −788. `position-rolls`: **0 detected** (single-day
detection only — cross-session rolls not captured) [OI:position_rolls]. The closing
is consistent with phase-1's "repositioning a bullish delta book," not fresh selling.

### Pin risk & OPEX concentration

- `pin-risk` (dte≤7, ≤5% from spot): **INTC not in top-25** (leaders AAPL/NVDA/
  TSLA/SPY/QQQ). 06-18 is call-heavy → no tight pin; mild upward drift bias if any [OI:pin_risk].
- `opex-concentration` (≥40% filter): **INTC absent** — its 06-18 concentration is
  26.8%, below the 40% threshold, so it doesn't qualify as a concentration cliff [OI:opex_concentration].

## Tool calls (audit trail)

| Command (`--symbol INTC --date 2026-06-15` where scoped) | Key value(s) ← path | Rows |
|------|------|------|
| `oi oi-by-strike --top-n 10 --dte-max 30` | $130 wall net_oi +37,683; $150 wall +57,963 ← `.results[]` | 10 |
| `oi oi-by-strike --top-n 10` (all-expiry) | $150 169k call OI; legacy $50 call-heavy | 10 |
| `oi term-structure` | 06-18 = 26.8% of OI ← `.term_structure` sort -pct | 18 |
| `oi biggest-increases --top-n 20 --min-oi-change 500` | Sep18 C97.5 +63,781 ← `.oi_diff_plain` | 20 |
| `oi decrease-with-volume --top-n 15 --min-volume 100` | C90 Jul17 −4,525 | 15 |
| `oi smart-positioning --top-n 20 --min-oi-change 500` | C97.5 bearish, C140/C150 bullish ← `.inferred_direction` | 20 |
| `oi position-rolls --threshold 500 --near-dte-max 30` | 0 rolls (single-day) | 0 |
| `oi pin-risk --top-n 25 --dte-max 7 --max-distance-pct 5` | INTC absent | 25 |
| `oi opex-concentration --top-n 20 --min-concentration-pct 40` | INTC absent | 20 |

## Tool errors

None — all nine reads returned valid JSON (all accepted `--date 2026-06-15`).

## DATA NOTE / CORRECTION

None. Spot reads $127.82 here (OI snapshot) vs $127.86 (phase-2 dark pool / fz) —
a 4-cent timestamp difference, not a discrepancy. OI is end-of-day; `option_symbol`
parsed from OPRA for side/expiry per the path map (no `side` column).

## Verdict for downstream phases

- **Positioning bias:** mildly **bullish** — fresh OTM call ladder (C130/C140/C150)
  built bullish, calls being rolled not dumped; tempered by deep-ITM call writing
  (C97.5) and protective put tails = overhead supply.
- **Conviction:** **3/5** — directional new positioning leans up, consistent with
  phases 1–2, but a large share is financing/hedging, and the $130/$150 call walls
  are overhead supply that caps the path.
- **Largest OI build as % of float:** **0.15%** (63,781 ct C97.5 ≈ 6.38M sh / 4.25B
  float `[OI:oi_pct_float fz]`); the genuine directional C140 build is ~0.035%.
  Modest for a 4.25B-float name — real positions, not float-dominating.
- **Three pin/cliff strikes for phase-9 (entry/stop reference):**
  1. **$130 — call_wall_resistance, +1.7%** (immediate overhead; the pivot to clear).
  2. **$150 — call_wall_resistance, +17.4%** (upside magnet *and* cap; target ceiling).
  3. **$110–120 support** — $120 call_heavy (−6.1%) / $110 put_wall (−13.9%); plus
     the **06-18 OPEX cliff** (26.8% of OI) as this week's gravity well.
- **Open questions:**
  - Is the deep-ITM C97.5 write + $130/$150 call walls enough overhead supply to cap
    the rally — i.e. what's the dealer gamma regime? → **phase-4 (GEX/max-pain)**.
  - Does max-pain sit near $127–130, reinforcing the 06-18 pin, or below? → **phase-4**.
  - Is the OTM call building speculative chase or hedged? → cross-ref **phase-5** trend, **phase-7c** positioning.
