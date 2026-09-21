# Phase 3 — Open Interest & Positioning

**Ticker:** FSLR · **As-of:** 2026-07-20 · **Version:** v1 · **Generated:** 2026-07-20
**OI spot (prior close):** $205.23 · **Intraday underlying (phase-1/2):** $210.56
**Cites:** phase-1-flow.md (OTM call selling Sep 260/280/330; Aug 165P opening;
bearish net_flow); phase-2-dark-pool.md (support $205.31, pivot $211.99).

> **Data timing caveat:** OI updates after the close, so this feed's `spot` is the
> prior close ($205.23); intraday tape (phases 1–2) had FSLR at $210.56. Distance
> percentages below are vs $205.23 — shift ~2.5% for the live level.

## Summary

Positioning is **net bearish-to-neutral with a structural short-call ceiling
overhead.** Fresh OI is dominated by two bearish builds — **Aug-21 290C sold to
open (+3,254 OI, `inferred_direction=bearish`)** and **Aug-21 190P bought
(+1,362, bearish)** — versus one small bullish Jul-24 220C build (+554). The chain
carries a **wall of call OI stacked $250→$310** (all-expiry $300 call wall =
18,834 OI, the single heaviest strike), which is the other side of phase-1's OTM
call *selling* — dealers sit long those calls and will sell stock into rallies
toward them (upside-suppressive). Near-term (DTE≤30) the money is **put-heavy
around spot** ($200/$205 put walls, $210 put-heavy) = hedging into the 07-30
earnings. **No near-term pin** (outside pin-risk top-25) and **no single-expiry
cliff ≥40%** (outside opex-concentration top-20); OI gravity is the **2026-09-18
expiry (24.6% of total OI)** with the post-earnings **2026-08-21 monthly (15.1%)**
as the tradeable cliff.

## Key signals

- **[OI:smart_positioning]** Aug-21 **290C sold to open, +3,254 OI**
  (net_ask_bid −2,348, bid-vol 2,605 ≫ ask 257) → **bearish** overwriting; matches
  phase-1's Sep/Aug call selling.
- **[OI:smart_positioning]** Aug-21 **190P bought, +1,362 OI** (ask-side,
  net_ask_bid +1,338) → **bearish** protective/directional put build.
- **[OI:oi_by_strike]** All-expiry heaviest strike **$300 call wall, 18,834 call
  OI** (net +18,834); call OI stacked $250/$260/$270/$280/$290/$300/$310 =
  structural overhead supply / dealer-long ceiling.
- **[OI:oi_by_strike]** Near-term (DTE≤30) is **put-heavy at the money**: $200 put
  wall (1,549), $205 put wall (635, at spot), $210 put-heavy (1,427) = earnings
  hedging cluster.
- **[OI:term_structure]** OI gravity in **2026-09-18 (24.6%)**; post-earnings
  cliff **2026-08-21 (15.1%)**; the **07-31 weekly** (first after earnings) is
  **put-heavy, P/C 2.15** = concentrated earnings downside hedges.

## Detailed findings

### OI walls by strike — all-expiry aggregate `[OI:oi_by_strike]`
| Strike | Call OI | Put OI | Net OI | Role | Dist% (vs $205.23) |
|--------|---------|--------|--------|------|------|
| **300** | 18,834 | 0 | +18,834 | call_wall_resistance | +46.2% |
| 250 | 13,210 | 3,812 | +9,398 | call_wall_resistance | +21.8% |
| 280 | 12,841 | 0 | +12,841 | call_wall_resistance | +36.4% |
| 270 | 11,318 | 3 | +11,315 | call_wall_resistance | +31.6% |
| 260 | 10,271 | 355 | +9,916 | call_wall_resistance | +26.7% |
| 290 | 10,165 | 107 | +10,058 | call_wall_resistance | +41.3% |
| 310 | 9,758 | 1 | +9,757 | call_wall_resistance | +51.1% |
| **150** | 0 | 14,385 | −14,385 | put_wall_support | −26.9% |
| **180** | 226 | 10,974 | −10,748 | put_wall_support | −12.3% |
| 220 | 4,897 | 3,980 | +917 | call_heavy (two-sided) | +7.2% |

### OI walls — tradeable horizon (DTE≤30) `[OI:oi_by_strike --dte-max 30]`
| Strike | Call OI | Put OI | Net | Role | Dist% |
|--------|---------|--------|-----|------|-------|
| 240 | 2,311 | 25 | +2,286 | call_wall_resistance | +16.9% |
| 250 | 1,829 | 0 | +1,829 | call_wall_resistance | +21.8% |
| 200 | 11 | 1,549 | −1,538 | **put_wall_support** | −2.6% |
| 210 | 56 | 1,427 | −1,371 | put_heavy | +2.3% |
| 205 | 10 | 635 | −625 | **put_wall_support (at spot)** | −0.1% |
| 220 | 850 | 1,391 | −541 | put_heavy | +7.2% |
| 190 | 50 | 291 | −241 | put_wall_support | −7.4% |

Near-term: **first call wall $240**, support **$200/$205**. Puts dominate $190–220.

### OI term structure (OPEX cliffs) `[OI:term_structure]` — total OI 224,583
| Expiry | DTE | Call OI | Put OI | P/C | % of total OI |
|--------|-----|---------|--------|-----|---------------|
| 2026-07-24 | 4 | 6,034 | 2,332 | 0.39 | 3.7% |
| 2026-07-31 | 11 | 1,414 | 3,034 | **2.15** | 2.0% |
| **2026-08-21** | 32 | 19,770 | 14,184 | 0.72 | **15.1%** |
| **2026-09-18** | 60 | 43,302 | 12,019 | 0.28 | **24.6%** |
| 2026-12-18 | 151 | 19,976 | 4,131 | 0.21 | 10.7% |
| 2027-01-15 | 179 | 37,753 | 41,151 | 1.09 | 35.1% (LEAP) |

OPEX cliff for the trade horizon = **2026-09-18 (24.6%, call-heavy)**; the
earnings-relevant expiry is **2026-08-21 (15.1%)**. The **07-31 weekly** right
after earnings is put-heavy (P/C 2.15) → downside hedges. The 2027-01-15 LEAP
(35.1%) is structural, not tradeable.

### Largest OI increases (parsed from `option_symbol`) `[OI:biggest_increases]`
| Contract | Exp | Side | Strike | OI Δ | Vol | Inferred dir |
|----------|-----|------|--------|------|-----|--------------|
| FSLR260821C00290000 | 08-21 | Call | 290 | **+3,254** | 3,434 | **bearish** (sold) |
| FSLR260821P00190000 | 08-21 | Put | 190 | +1,362 | 1,408 | **bearish** (bought) |
| FSLR260724C00220000 | 07-24 | Call | 220 | +554 | 901 | bullish (small) |

### Closing / roll activity `[OI:decrease_with_volume]`
Negligible — all decreases < 100 OI (07-24 230C −77, 07-24 215P −52, 09-18 270C
−10). No meaningful closing or near→far rolling detected (`position-rolls`
threshold not met at the reported sizes).

### Smart positioning `[OI:smart_positioning]`
2 of 3 flagged **bearish** (Aug 290C overwrite, Aug 190P buy); 1 small bullish
(Jul-24 220C). Net inferred bias **bearish**, consistent with phase-1.

### Pin risk / OPEX concentration
- **Pin-risk (DTE≤7):** FSLR **outside the market-wide top-25** — the 07-24 weekly
  OI is thin (3.7%); no pin gravity into Friday. Skip pin commentary.
- **OPEX-concentration (≥40%):** FSLR **outside top-20** — OI is spread across
  expiries (no near-term single-expiry cliff ≥40%).

## Tool calls
| Tool | Args | Result |
|------|------|--------|
| oi oi-by-strike | FSLR, top 10 (all-expiry) | $300 call wall 18,834; $150/$180 put walls |
| oi oi-by-strike | FSLR, top 10, dte-max 30 | $240 call wall; $200/$205 put walls |
| oi term-structure | FSLR | 14 expiries; cliff 09-18 (24.6%), 08-21 (15.1%) |
| oi biggest-increases | FSLR, top 20, min-Δ 500 | 3 rows (2 bearish, 1 bullish) |
| oi decrease-with-volume | FSLR, top 15, min-vol 100 | 3 tiny decreases |
| oi smart-positioning | FSLR, top 20, min-Δ 500 | 2 bearish / 1 bullish |
| oi pin-risk | market, dte-max 7, dist 5% | FSLR outside top-25 |
| oi opex-concentration | market, min-conc 40% | FSLR outside top-20 |

## Tool errors
None. `biggest-increases` side/expiry parsed from `option_symbol` (OPRA), not
inferred. Term-structure ticker-scoped (no post-filter). All reads parsed via `jq`.

## Verdict for downstream

- **Positioning bias:** **BEARISH-to-NEUTRAL.** New OI = call overwriting (Aug
  290C −to-open) + put buying (Aug 190P), corroborating phase-1's short-vol/bearish
  tape. The overhead $250–310 call wall is a **dealer-long ceiling** (upside sold
  into), and near-term puts cluster at the money as earnings hedges.
- **Conviction: 3/5** — directionally consistent across new OI + smart-positioning,
  but sizes are modest and much is overwriting (income), not aggressive directional
  shorting. `[CTX:]` BUSY_NAME_NORMAL_DAY still caps phase-1–2 confluence at `+`.
- **Largest OI build as % of float:** **n/a** (no float this run). Absolute: the
  +3,254 Aug 290C build = ~325k share-equivalents — not structurally float-material.
- **Three cliff/wall strikes for phase-9:**
  1. **$240 → $250** — first near-term call-wall resistance (dealer-long ceiling
     begins here; the $300 wall is the structural cap).
  2. **$200 / $205** — near-term put-wall support (aligns with phase-2 $205.31 DP
     shelf → a real floor confluence).
  3. **OPEX cliff 2026-09-18 (24.6% of OI)**; earnings-anchored **2026-08-21
     (15.1%)** — size any options structure to these, and respect the 07-31
     put-heavy (P/C 2.15) earnings-hedge expiry.
- **Open questions:**
  - Is the $250–310 call OI covered-writing (income, capping upside) or dealers
    net-long gamma there? Phase-4 GEX/max-pain to resolve.
  - Does max-pain (phase-4) sit near the $205 put-wall / $211 DP pivot, implying a
    pin between phase-2's two shelves?
  - The put-wall support at $200/$205 vs the bearish new positioning — is $200 the
    line the bears must break for the thesis to pay?
