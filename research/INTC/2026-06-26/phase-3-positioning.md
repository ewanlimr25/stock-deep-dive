# Phase 3 — Open Interest & Positioning

**Ticker:** INTC
**As-of date:** 2026-06-26
**Generated:** 2026-06-27T10:01:55-0400
**Upstream phases cited:** phase-0.5-context.md, phase-1-flow.md, phase-2-dark-pool.md

## Summary

OI positioning is the **cleanest bearish signal in the dive so far** — and unlike
phase-1's premium, this is structural, not financing. Today's genuinely-new OI builds
are **~73% bearish by contract weight** (smart-positioning: 32,299 bearish OI_Δ vs
12,250 bullish), the **single largest new position is PUT 130 Jul-17 (+11,442 OI, ratio
4.11, inferred bearish)**, and the only clean new structural builds are puts (130/135
Jul-17, 140 Aug-21). Simultaneously, closing activity is a **call unwind** — 12 call
strikes shed −9,237 OI vs only −1,585 put OI, including deep-ITM C90 Jul-17 (−1,903),
corroborating phase-1's "calls = financing" read. So the day's positioning is a textbook
**rotation out of calls and into puts**, concentrated at the **July-17 OPEX gravity well
(21 DTE, 14.9% of all OI, P/C 0.90)**. The wall map: nearest resistance is the **$130
call wall (+1.8%)**, then $135/$140/$150; **put support is far below** ($110 −13.8%,
$100 −21.7%) — thin documented support between spot and $110.

## Key signals

- **PUT 130 Jul-17 +11,442 OI (ratio 4.11), inferred bearish** — day's #1 new build
  [OI:biggest_increases][OI:smart_positioning].
- **New OI ~73% bearish** (32,299 vs 12,250 OI_Δ); largest builds (≥1k) 74.5% bearish
  [OI:smart_positioning].
- **Call unwind**: −9,237 call OI closed across 12 strikes vs −1,585 put OI / 3 strikes;
  incl. deep-ITM C90 Jul-17 −1,903 [OI:decrease_with_volume].
- **Wall map (≤30 DTE):** $130 call wall (+1.8%, net_oi +14,942) nearest resistance;
  $150 the heaviest call wall (net_oi +72,422) but +17.5% away; put support only at
  $110/$100 [OI:oi_by_strike].
- **OPEX cliff = 2026-07-17** (dte 21): 14.9% of total OI, balanced P/C 0.90 — the
  gravity well where the put build sits [OI:term_structure].

## Detailed findings

### OI walls by strike (`oi-by-strike`, ≤30 DTE tradeable horizon; spot ref $127.67)

| Strike | call_oi | put_oi | net_oi | role | dist |
|---|---|---|---|---|---|
| 150 | 73,911 | 1,489 | **+72,422** | call_wall_resistance | +17.49% |
| 140 | 44,769 | 4,877 | +39,892 | call_wall_resistance | +9.66% |
| 160 | 39,815 | 95 | +39,720 | call_wall_resistance | +25.32% |
| 145 | 28,810 | 1,809 | +27,001 | call_wall_resistance | +13.57% |
| **130** | 36,600 | 21,658 | **+14,942** | **call_wall_resistance** | **+1.83%** |
| 135 | 22,499 | 10,669 | +11,830 | call_wall_resistance | +5.74% |
| 120 | 39,590 | 30,696 | +8,894 | call_heavy (battleground) | −6.01% |
| 110 | 9,044 | 21,301 | −12,257 | put_wall_support | −13.84% |
| 100 | 8,454 | 37,797 | −29,343 | put_wall_support | −21.67% |
| 80 | 5,285 | 35,016 | −29,731 | put_wall_support | −37.34% |

**Read:** the entire near-strike structure (130→160) is call-dominated resistance; the
$130 wall (+1.8%) is the immediate overhead lid and doubles as the strike where the big
new put build sits (battleground). $120 (−6%) is a two-sided `call_heavy` floor-ish
zone. There is **no put_wall_support until −13.8% ($110)** — limited structural cushion
just below spot. (All-expiry aggregate adds deep LEAP put walls at $100/$80/$30 — far,
ignore for the tradeable horizon.)

### OI term structure (OPEX cliffs)

| Expiry | DTE | call_oi | put_oi | P/C | % of total OI |
|---|---|---|---|---|---|
| **2026-07-17** | **21** | 281,951 | 252,766 | **0.90** | **14.91%** |
| 2026-12-18 | 175 | 272,989 | 234,631 | 0.86 | 14.15% |
| 2027-01-15 | 203 | 269,632 | 234,436 | 0.87 | 14.05% |
| 2026-09-18 | 84 | 236,924 | 159,437 | 0.67 | 11.05% |
| 2026-06-26 | 0 | 190,901 | 160,257 | 0.84 | 9.79% |
| 2026-08-21 | 56 | 184,836 | 130,870 | 0.71 | 8.80% |

Near-term gravity well = **July 17** (largest non-LEAP fraction, 14.9%). P/C 0.90 there
is balanced but the *new flow* into it is put-heavy (below). Cross-check vs phase-4
max-pain. The LEAP buckets (Dec/Jan) are large but slow.

### Largest OI increases (new positions today; OPRA-parsed)

| Side | Strike | Expiry | OI Δ | Ratio | Vol | Read |
|---|---|---|---|---|---|---|
| **P** | **130** | **2026-07-17** | **+11,442** | **4.11** | 13,185 | **New bearish core** |
| P | 135 | 2026-07-17 | +2,941 | 2.99 | 3,591 | New put (bearish) |
| P | 140 | 2026-08-21 | +2,177 | 1.64 | 3,202 | New put (bearish) |
| C | 130 | 2026-06-26 | +5,950 | 0.84 | 19,855 | 0DTE churn (<1 ratio) |
| C | 140 | 2026-06-26 | +4,363 | 0.28 | 21,482 | 0DTE churn |
| P | 120 | 2026-06-26 | +2,209 | 0.21 | 8,037 | 0DTE churn |

Only the three **ratio>1** rows are genuinely new structural OI — **all puts** (130/135
Jul-17, 140 Aug-21). The high-volume 0DTE call rows (ratio<1) are intraday/expiry churn,
not new positioning, consistent with phase-1's financing read.

### Closing / roll activity

Closes are **call-dominated**: C90 Jul-17 −1,903 (deep-ITM financing unwind), C180
Jul-02 −1,185, C125 0DTE −1,069, C130 Jul-02 −905, C150 Jul-17 −714, C160 Jul-17 −616.
Total call OI closed −9,237 across 12 strikes vs put OI closed −1,585 across 3.
`position-rolls` returned **rolls_detected: 0** (threshold 500, near-dte≤30) — no clean
near→far roll signature; the deep-ITM call activity is same-day churn, not a roll.

### Smart positioning (inferred direction)

| Direction | Σ OI_Δ | Positions | Of builds ≥1k |
|---|---|---|---|
| **bearish** | **32,299** | 12 | 27,721 (74.5%) |
| bullish | 12,250 | 8 | 9,507 |

~73% bearish by weight. Caveat (per phase doc): inference is OPRA-parse + ask/bid based
and **not perfectly clean** — e.g. P135 Jul-17 is tagged "bullish" (read as put-selling)
while P130 Jul-17 and P140 Aug-21 are "bearish" (put-buying); the dominant P130 build and
the aggregate both lean bearish.

### Pin risk / OPEX concentration

- `pin-risk` (dte≤7, ≤5% distance): **INTC outside top-25** — no near-dated pin
  candidate; the monthly OPEX (Jul-17) is 21 days out, beyond the 7-day window.
- `opex-concentration` (≥40%): **INTC outside top-20** — its largest single-expiry
  fraction is 14.9% (Jul-17), so OI is **well-distributed, no extreme single cliff**.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `oi oi-by-strike --symbol INTC --dte-max 30 --top-n 10` | $130 call wall net_oi +14,942 (+1.8%); $150 +72,422 ← `.results[].net_oi,.role,.distance_pct` | top-10 |
| `oi term-structure --symbol INTC` | Jul-17 14.91% / P/C 0.90 ← `.term_structure[]|max pct_of_total_oi` | 18 expiries |
| `oi biggest-increases --symbol INTC --min-oi-change 500` | P130 Jul-17 +11,442 ratio 4.11 ← OPRA-parse `.option_symbol` + `.oi_diff_plain,.oi_change` | top-20 |
| `oi smart-positioning --symbol INTC --min-oi-change 500` | bearish 32,299 vs bullish 12,250 ← `group_by(.inferred_direction)` | top-20 |
| `oi decrease-with-volume --symbol INTC --min-volume 100` | calls −9,237 OI vs puts −1,585 ← `.oi_diff_plain` by C/P | top-15 |
| `oi position-rolls --symbol INTC --threshold 500 --near-dte-max 30` | rolls_detected 0 ← `.results` empty | — |
| `oi pin-risk --dte-max 7 --max-distance-pct 5` | INTC absent (outside top-25) | top-25 |
| `oi opex-concentration --min-concentration-pct 40` | INTC absent (max 14.9% < 40%) | top-20 |

## Tool errors

None — all nine reads returned valid JSON on first call.

## DATA NOTE / CORRECTION

Spot reference differs by tool: `oi-by-strike.spot = $127.67` (OI snapshot, prior-close
reference) vs dark-pool avg_price $128.67 (phase-2) vs fz close $128.32 (phase-0). All
within ~0.8%; working spot ≈ **$128**. Distance_pct figures use the $127.67 OI reference.

## Verdict for downstream phases

- **Positioning bias:** **BEARISH** — new OI is ~73% bearish, the dominant new build is
  a Jul-17 $130 put (+11,442), and the call side is being *closed* (financing unwind).
  Net: rotation out of calls, into puts, at the July OPEX cliff.
- **Conviction:** **4 / 5** — the structural-OI shift is the dive's cleanest directional
  corroboration (it is positioning, not the phase-1 financing noise).
- **Largest OI build as % of float:** **0.027%** (11,442 ct × 100 sh / 4.25B float) —
  **not meaningful as %float** for a mega-cap, but it IS the day's dominant directional
  OI build. [OI:oi_pct_float fz]
- **Three pin/cliff strikes for phase-9** (sourced from roles + term-structure):
  1. **$130 — call_wall_resistance (+1.8%)**, the immediate overhead lid AND the strike
     of the new put build → battleground/pin into Jul-17.
  2. **$110 — put_wall_support (−13.8%)**, the nearest real downside structural shelf.
  3. **$150 — heaviest call_wall_resistance (net_oi +72,422, +17.5%)**, the hard
     overhead cap (aligns with phase-2's $140.94 supply zone region).
- **Open questions:**
  - Is the $150 call wall fresh bullish demand or static covered-call/financing OI? (The
    call *decreases* suggest static-to-shrinking, not fresh buying — phase-4 GEX will
    confirm dealer positioning.)
  - Where is the zero-gamma flip vs the $130 wall and the $128.32 dark-pool magnet
    (phase-4)? Does max-pain align with $130 into Jul-17?
