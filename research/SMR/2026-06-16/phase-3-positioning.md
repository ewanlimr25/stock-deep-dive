# Phase 3 — Open Interest & Positioning

**Ticker:** SMR
**As-of date:** 2026-06-16
**Generated:** 2026-06-17T11:56:18Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md

## Summary

Positioning is **mixed but modestly bearish-tilted**, and **structurally caps
upside.** Today's OI builds are short-dated OTM 06-18 calls (strikes $11–$12.5)
that `smart-positioning` infers **6 bearish vs 4 bullish** (ΔOI 7,829 bearish vs
5,374 bullish) — i.e. a blend of speculative call-buying *and* call-writing, not
clean accumulation. The at-the-money **$10 strike is put-heavy** (net_oi −8,116 in
<30 DTE; put 11,526 vs call 3,410) and new **ATM put** OI is building (P10 +631,
P10.5 +519). Overhead is a stack of **call-wall resistance at $12 / $15**. The
nearest **OPEX cliff is 06-18 (2 DTE) holding 28.24% of all OI**, but SMR is in
**no pin-risk or opex-concentration top list** — gravity is modest. This
corroborates phases 1–2 (net-bearish flow + distribution).

## Key signals

- **At-money $10 is put-heavy:** <30-DTE `net_oi = −8,116` (put 11,526 / call
  3,410), `role=put_heavy`, 1.21% from spot — puts dominate right at spot
  [OI:oi_by_strike].
- **Call-wall resistance overhead:** $12 (`net_oi +8,842`, 21.5% OTM) and the big
  $15 wall (`net_oi +21,424`, 51.8% OTM) cap upside [OI:oi_by_strike].
- **OI builds lean bearish:** of the 10 largest, `inferred_direction` is **6
  bearish / 4 bullish**; the one clean bullish build is C12 06-18 (net_ask_bid
  +2,859, ask-side buy); C14 07-10 & C15 07-17 are sold (net_ask_bid −793 / −775)
  [OI:smart_positioning].
- **OPEX cliff 06-18 = 28.24% of OI** (call 114,404 / put 49,536); LEAP 2027-01-15
  = 20.79% (call 108,748 / put 11,910, far-OTM call stack) [OI:term_structure].
- **No pin / no cliff cross-sectionally:** SMR absent from `pin-risk` top-25 and
  `opex-concentration` top-20 (max single-expiry 28.24% < 40% threshold); **0
  position rolls** detected [OI:pin_risk][OI:opex_concentration][OI:position_rolls].

## Detailed findings

### OI walls by strike (tradeable horizon, `--dte-max 30`; spot $9.88) — [OI:oi_by_strike]

| Strike | call_oi | put_oi | net_oi | role | dist% |
|--------|---------|--------|--------|------|-------|
| $10 | 3,410 | 11,526 | **−8,116** | put_heavy | +1.21 |
| $10.5 | 4,126 | 3,942 | +184 | (balanced) | +6.28 |
| $11 | 7,862 | 7,214 | +648 | (balanced) | +11.34 |
| $11.5 | 6,257 | 4,953 | +1,304 | call_wall | +16.4 |
| $12 | 16,124 | 7,282 | **+8,842** | call_wall_resistance | +21.46 |
| $13 | 6,748 | 3,127 | +3,621 | call_wall | +31.58 |
| $14 | 6,729 | 1,531 | +5,198 | call_wall | +41.7 |
| $15 | 22,430 | 1,006 | **+21,424** | call_wall_resistance | +51.82 |

All-expiry view adds **put-wall support below**: $9 (`net_oi −14,941`), $8
(`net_oi −20,460`). Read: near-spot is a put-heavy $10 magnet, with OTM call OI
forming overhead resistance (the role-tagged "call walls" at $12/$15 are far OTM —
treat as caps, not near-term pivots).

### OI term structure (OPEX cliffs) — [OI:term_structure]

| Expiry | DTE | call_oi | put_oi | % of total OI |
|--------|-----|---------|--------|---------------|
| **2026-06-18** | 2 | 114,404 | 49,536 | **28.24%** ← nearest cliff |
| 2027-01-15 | LEAP | 108,748 | 11,910 | 20.79% (OTM call stack) |
| 2026-07-17 | 31 | 65,237 | 22,887 | 15.18% |
| 2026-08-21 | 66 | 47,710 | 34,512 | 14.17% |
| 2028-01-21 | LEAP | 37,739 | 12,177 | 8.60% |
| 2026-11-20 | — | 18,040 | 13,636 | 5.46% |

Total OI 580,445 across 11 expiries. The 06-18 cliff is call-skewed (P/C OI ≈
0.43) but no expiry crosses the 40% concentration that would flag a hard pin.

### Largest OI increases (parsed from `option_symbol`) — [OI:biggest_increases]

| Contract | Side | Expiry | ΔOI | Vol | smart-pos infer |
|----------|------|--------|-----|-----|-----------------|
| C11.5 | call | 06-18 | +3,127 | 5,089 | bearish (bid) |
| C12 | call | 06-18 | +2,354 | 6,349 | **bullish (ask +2,859)** |
| C12.5 | call | 06-18 | +2,313 | 4,149 | bearish (bid) |
| C11 | call | 06-18 | +1,677 | 6,778 | bullish (mild) |
| C15 | call | 07-17 | +657 | 2,659 | bearish (sold) |
| C14 | call | 07-10 | +638 | 820 | bearish (sold, bid 802/ask 9) |
| **P10** | put | 06-18 | +631 | 2,822 | bullish (put sold on bid) |
| **P10.5** | put | 06-18 | +519 | 1,419 | bearish (put bought on ask) |

The OTM-call builds are **not uniformly bullish** — only C12/C11 show ask-side
buying; C11.5/C12.5/C14/C15 are bid-side (written). This is the "speculative vs
covered/written" ambiguity, resolved as **mixed, bearish-tilted** — consistent
with phase-1's overwrite read.

### Closing / roll activity — [OI:decrease_with_volume][OI:position_rolls]

Minor decreases only (C10 06-18 −332, P11 06-18 −277, C10 08-21 −268).
`position-rolls` = **0 detected** (single-day detector; cross-session rolls not
captured).

### Pin risk / OPEX concentration — [OI:pin_risk][OI:opex_concentration]

SMR in **neither** top list. Despite 2 DTE to the 06-18 expiry, its pin/cliff
gravity is below the cross-sectional cut (pin top-25 = AAPL/NVDA/SPY/TSLA…;
opex-conc top-20 = small illiquid names with ≥40% single-expiry concentration).
The $10 strike is the *internal* magnet but not a market-flagged pin.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|------------------|--------------------------|-----------|
| `uw oi oi-by-strike --symbol SMR --dte-max 30 --top-n 10 --date 2026-06-16` | $10 net_oi=−8,116 put_heavy ← `.results[]` | top-10 |
| `uw oi oi-by-strike --symbol SMR --top-n 10 --date …` (all-expiry) | $15 net_oi +63,705 wall; $8/$9 put walls | top-10 |
| `uw oi term-structure --symbol SMR --date …` | 06-18 pct_of_total_oi=28.24 ← `.term_structure[]` | 11 expiries |
| `uw oi biggest-increases --symbol SMR --top-n 20 --min-oi-change 500 --date …` | C11.5 06-18 +3,127 ← `.results[].oi_diff_plain` + `option_symbol` | 10 |
| `uw oi smart-positioning --symbol SMR --top-n 20 --min-oi-change 500 --date …` | 6 bearish/4 bullish ← `.results[].inferred_direction` + `net_ask_bid` | 10 |
| `uw oi decrease-with-volume --symbol SMR --top-n 15 --min-volume 100 --date …` | C10 06-18 −332 ← `.results[].oi_diff_plain` | top |
| `uw oi position-rolls --symbol SMR --threshold 500 --near-dte-max 30 --date …` | `rolls_detected=0` | 0 |
| `uw oi pin-risk --top-n 25 --dte-max 7 --max-distance-pct 5 --date …` | SMR absent ← filter | top-25 |
| `uw oi opex-concentration --top-n 20 --min-concentration-pct 40 --date …` | SMR absent ← filter | top-20 |

## Tool errors

(none — all reads jq-validated. `term-structure` rows are nested under
`.term_structure[]`, not `.results[]` — adjusted path. `smart-positioning`
direction field is `inferred_direction` (not `direction`) — adjusted.)

## DATA NOTE / CORRECTION

`biggest-increases`/`smart-positioning` carry no `side`/`expiry` columns — both
parsed from `option_symbol` (OPRA) per the trap. `oi_diff_plain` used for the ΔOI
(not the fractional `oi_change`). No value transcribed from an unparsed buffer.

## Verdict for downstream phases

- **Bias from this phase:** **Mixed, modestly bearish** — put-heavy at-money $10,
  bearish-tilted OI builds (6:4), call-wall caps overhead at $12/$15.
- **Conviction:** **2/5** — two-sided builds, modest gravity, no flagged pin.
- **Largest OI build as % of float:** C11.5 06-18 +3,127 ct ≈ **0.093%** of float
  (share-equiv); aggregate 06-18 call OI 114,404 ct ≈ **3.41%** of float
  [OI:oi_pct_float fz]. Single builds are small; the **aggregate 06-18 call OI is
  structurally meaningful** as overhead but is spread/partly written, not one bet.
- **Three pin/cliff strikes for phase-9:**
  1. **$10 — at-money put-heavy magnet** (net_oi −8,116; nearest strike, 1.2%) →
     pivot/support reference.
  2. **$12 — call-wall resistance** (net_oi +8,842) → first upside cap;
     **$15** the harder cap (net_oi +21,424).
  3. **$9 / $8 — put-wall support** (all-expiry net_oi −14,941 / −20,460) →
     downside structural support, aligns with phase-2 $9.79/$9.57/$9.48.
  - **OPEX cliff: 06-18 (28.24% of OI)** — cross-check phase-4 max-pain.
- **Open questions:** Is the at-money $10 put-heaviness hedging or directional
  bearish bets? Does max-pain (phase-4) and GEX confirm a $10 pin into 06-18? Is
  the far OTM call stack ($15/2027 LEAP) old covered-call inventory vs the short
  base (phase-7c)?
