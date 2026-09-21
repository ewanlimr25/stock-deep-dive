# Phase 4 — Dealer Structure & Gamma

**Ticker:** KWEB
**As-of date:** 2026-05-19
**Generated:** 2026-05-20T00:00:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md

## Summary

Dealer regime is **POSITIVE GAMMA** (long-gamma) with total GEX
**$30.55B** at spot $28.34 and Zero Gamma Level (ZGL) **$23.81** — i.e.
spot trades ~16% above the flip [STRUCT:gex]. Above $28, the gamma
profile is range-suppressing with two dominant positive walls:
**$29 (+$17.79B)** and **$30 (+$10.75B)** [STRUCT:gex]. Net DEX is
**+$70.74B** (call-heavy public, dealer hedge = systematically LONG
underlying) [STRUCT:dex] — a structural bid. IV term structure is
labelled **BACKWARDATION** but the entire backwardation is driven by
the 3-DTE May 22 expiry at **52.6% IV** vs ~34% across the rest of the
curve [STRUCT:iv_term_structure] — this is **localised front-week event
premium**, not a full vol-stress regime (front-end / 30-DTE ratio is
**0.952 = FLAT** when the 3-DTE outlier is excluded
[STRUCT:front_end_iv_ratio]). Term skew at 30 DTE is **COMPLACENT**
(calls 33.74% > puts 30.71%, ratio 0.91)
[STRUCT:term_skew] — **calls are richer than puts**, an unusual
configuration that implies downside protection is *under-priced*
relative to the 5-day bearish sweep persistence flagged in phase 1.

## Key signals

- **POSITIVE GEX regime**, total $30.55B, ZGL $23.81, spot $28.34
  [STRUCT:gex] — long-gamma until spot loses ~16% from here.
- **$29 strike GEX = $17.79B (largest single)** [STRUCT:gex] and 0DTE
  support wall confirms it: $29 → $2.35B for the May 22 expiry alone
  [STRUCT:today_gamma_flip]. Strongest dealer magnet above spot.
- **$30 strike GEX = $10.75B** — the second positive ceiling
  [STRUCT:gex]. Cross-validates phase-3's $30 call-write activity
  [OI:smart_positioning].
- **$27 strike GEX = -$7.10B** [STRUCT:gex] — single largest NEGATIVE
  strike. A break below $27 swings the regime sharply toward short-
  gamma trend-acceleration. This is the most important downside
  trigger.
- **Term skew COMPLACENT, ratio 0.91, calls > puts** [STRUCT:term_skew]
  — KWEB downside is structurally cheap; long-puts / put-spreads have a
  vol-discount tailwind for any bearish hedge.
- **May 22 expiry IV 52.6%** [STRUCT:iv_term_structure] — 19 pts above
  next-week's 33.3% (May 29). High likelihood of a known event in the
  3-day window. Phase 6 macro will check the calendar.

## Detailed findings

### GEX — per-strike profile (DTE ≤ 45) [STRUCT:gex]

| Strike | Net GEX | Role |
|--------|---------|------|
| $20 | +$84K | minor |
| $23.5 | -$1,822 | ATM flip strike per 0DTE (today_gamma_flip) |
| $24 | -$135K | minor |
| **$25** | **-$14.68M** | growing negative below ZGL |
| $25.5 | -$2.30M | |
| **$26** | **-$90.43M** | accelerating |
| $26.5 | -$255K | |
| **$27** | **-$7,098.54M ($-7.10B)** | **biggest negative — short-gamma acceleration zone** |
| $27.5 | -$444.54M | |
| **$28** | **-$588.60M** | small negative below spot |
| **$28.5** | **+$104.24M** | first positive — gamma transition |
| **$29** | **+$17,793.65M ($17.79B)** | **dominant positive wall** |
| **$29.5** | **+$1,228.57M** | secondary positive |
| **$30** | **+$10,752.64M ($10.75B)** | **secondary call-wall ceiling** |
| $30.5 | +$95.77M | small |
| $31 | +$2,606.05M | major |
| $31.5 | +$328.64M | |
| $32 | +$2,336.27M | major |
| $33 | +$734.38M | (post-35K-OI close from phase 3 — still positive) |
| $34 | +$92.09M | |
| **$35** | **+$2,683.63M** | LEAP/LEAP-adjacent ceiling |
| $40 | +$12.37M | tail |
| $50 | +$4.10M | tail |

- **Regime:** POSITIVE — dealers net long gamma, suppress realized vol,
  mean-reversion tape.
- **Zero Gamma Level:** **$23.81** (4.53 = 16% below spot). Wide
  positive-gamma envelope.
- **Underlying price (per tool):** $28.34.

### DEX — dealer delta hedge [STRUCT:dex]

| Field | Value |
|-------|-------|
| Net DEX | **+$70,739,550,285** |
| Call DEX | +$84,480,983,691 |
| Put DEX | -$13,741,433,406 |
| Spot | $28.34 |

Interpretation: **Public is net call-long → dealers net short calls →
dealer hedge = BUY underlying.** This is a systematic structural bid
for KWEB shares: every unit of new call OI requires dealers to add
spot exposure. It also helps explain the *mild accumulation* observed
in phase-2's block / large tiers (buy_ratio 0.677 / 0.536) — those buy
tickets are likely partially dealer-delta hedging absorbing the new
call OI from phase 3.

### Vanna + Charm [STRUCT:vanna_charm]

| Field | Value |
|-------|-------|
| Net Vanna | -7,006,572 |
| Net Charm | +115,712,572 |
| Call Vanna | -8,228,277 |
| Put Vanna | +1,221,705 |

Tool interpretation: **"Public net vanna negative (call-heavy book).
Falling IV → call delta drops → dealers (short calls) cut long-
underlying hedge → SELLING pressure. Rising IV reverses."**

Trading implication: **IV is the steering wheel here.** If realized
vol decays from current 33–35% toward the 2025-Q4 base regime, dealers
will mechanically unwind their long-spot hedge → small downside
mechanical pressure. If IV rises (catalyst, macro shock), dealers
re-add hedge → mechanical bid. Charm flow is +$115.7M — positive time
decay flow biases dealer hedge UPWARD over the next 1–2 weeks
*ceteris paribus*.

### IV term structure [STRUCT:iv_term_structure]

| Expiry | DTE | Avg IV | Note |
|--------|-----|--------|------|
| 2026-05-22 | 3 | **52.6%** | front-week event premium spike |
| 2026-05-29 | 10 | 33.3% | floor of curve |
| 2026-06-05 | 17 | 39.2% | mild bump |
| 2026-06-12 | 24 | 34.5% | |
| 2026-06-18 | 30 | 34.9% | OPEX |
| 2026-06-26 | 38 | 34.0% | |
| 2026-07-17 | 59 | 34.7% | |
| 2026-08-21 | 94 | 34.7% | |
| 2026-09-18 | 122 | 34.4% | |
| 2026-11-20 | 185 | 34.1% | |
| 2026-12-18 | 213 | 37.2% | small Dec bump |
| 2027-01-15 | 241 | 36.9% | LEAP-equivalent |
| 2027-06-17 | 394 | 39.7% | LEAP |
| 2028-01-21 | 612 | 38.9% | far LEAP |

Tool label: **BACKWARDATION**. Reality: **localised front-week stress**
at the May 22 expiry. The rest of the curve sits in a tight 33–37%
band — call this a **kinked term structure** in practice, not a true
event-stress backwardation.

### Term skew (30-DTE) [STRUCT:term_skew]

| Field | Value |
|-------|-------|
| Call 25Δ IV | 33.74% |
| Put 25Δ IV | 30.71% |
| Skew | -0.0303 |
| Skew Ratio | 0.91 |
| Interpretation | **COMPLACENT** |

Calls are **richer than puts** at 25Δ — a reversed (or "reverse-skew")
configuration. For a sector that has been in a 5-day bearish sweep
persistence + mega-tier DP distribution, this means the **vol market is
under-pricing tail downside**. Two implications:
- Cheap downside puts are an asymmetric structure if the bearish thesis
  prevails.
- Conversely, the complacent skew aligns with the OI evidence that
  institutions are *selling* 28-strike puts (phase 3) — they're
  pocketing premium that they believe is fairly priced *because* the
  $28-$30 zone is well-defended structurally.

### Front-end IV ratio [STRUCT:front_end_iv_ratio]

| Field | Value |
|-------|-------|
| Near DTE actual | 9 |
| Near IV | 33.27% |
| Far DTE actual | 29 |
| Far IV | 34.93% |
| Ratio | 0.952 |
| Regime | **FLAT** |

The single-number front-end ratio sits in the FLAT band when the 3-DTE
outlier is excluded. The market is pricing a tactical week-ahead event
(May 22 expiry) but does NOT see a broader vol regime change beyond
that. **Sell the 3-DTE IV spike, buy nothing else on vol**.

### Today's gamma flip — 0DTE for May 22 expiry [STRUCT:today_gamma_flip]

| Field | Value |
|-------|-------|
| Spot | $28.33 |
| Today's ZGL | $23.08 |
| ATM flip strike | $23.5 |
| Today's total GEX | $2.996B |

Key walls (May 22 expiry only):

| Strike | Role | GEX |
|--------|------|-----|
| $29 | support_wall | +$2,354,402,524 |
| $30 | support_wall | +$477,524,518 |
| $29.5 | support_wall | +$94,625,042 |
| $31 | support_wall | +$88,085,401 |
| $28 | resistance_wall | -$48,047,033 |

Read: **for the May 22 expiry the dealer-hedged path of least
resistance is $29**. Above $29 strong dealer-sell pressure; below $28
small dealer-acceleration. The $28-$29 corridor is the most likely
print zone into Friday, with $29 as the upper magnet.

## Tool calls (audit trail)

| Tool | Args | Result |
|------|------|--------|
| `options_structure_gex` | `{symbol: KWEB, dte-max: 45, date: 2026-05-19}` | regime POSITIVE, ZGL 23.81, total $30.55B |
| `options_structure_dex` | `{symbol: KWEB, dte-max: 45, date: 2026-05-19}` | net DEX +$70.74B |
| `options_structure_vanna_charm` | `{symbol: KWEB, dte-max: 45, date: 2026-05-19}` | vanna -7.0M, charm +115.7M |
| `options_structure_iv_term_structure` | `{symbol: KWEB, date: 2026-05-19}` | BACKWARDATION (front-only) |
| `options_structure_term_skew` | `{symbol: KWEB, dte-target: 30, date: 2026-05-19}` | COMPLACENT, ratio 0.91 |
| `options_structure_front_end_iv_ratio` | `{symbol: KWEB, near-dte: 7, far-dte: 30, date: 2026-05-19}` | FLAT, ratio 0.952 |
| `options_structure_today_gamma_flip` | `{symbol: KWEB, date: 2026-05-19}` | spot $28.33, key wall $29 (+$2.35B) |

## Tool errors

None.

## Verdict for downstream phases

- **Dealer regime:** **POSITIVE GAMMA / long-gamma** at spot $28.34;
  ZGL $23.81. Mean-reverting tape above $24, sharp short-gamma
  acceleration if $27 breaks.
- **Conviction:** 4 / 5 — the GEX is dominant and one-sided positive
  above $28; only deduction is that the IV term structure has a
  localised 3-DTE event that needs phase-6 calendar resolution.
- **Three structural levels for phase 9:**
  1. **$29** — primary positive gamma magnet (45-DTE GEX +$17.79B; May
     22 GEX +$2.35B). Best long entry on dips toward $28; profitable
     target / call-strike for premium harvest.
  2. **$30** — secondary call-wall ceiling (+$10.75B). Phase-3
     overwriting confirmation. Sell calls at or above this strike.
  3. **$27** — large negative-gamma break level (-$7.10B). Hard
     invalidation for any long thesis; clean-trigger entry for any
     short thesis with $26 / ZGL ($23.81) targets.
- **Open questions:**
  - **May 22 IV at 52.6%** is anomalous. What is the catalyst in the
    next 3 days? Phase 6 macro calendar must identify it (China data
    print, Fed minutes, US tariff window, US-China sanctions
    announcement, sector earnings — TCEHY/JD/BABA/PDD calendar?).
    Without a catalyst this is short-vol opportunity; with one it's
    a setup risk for the put-write structure from phase 3.
  - The **complacent skew + bearish 5-day sweep persistence** is the
    key contradiction the audit (phase 10) must hold front-of-mind.
    Either flow tape lies or the vol market is mispriced — phase 7
    insights composite should help decide.
  - **DEX +$70.74B implies a substantial dealer long-stock hedge.** If
    a wave of long-call OI gets closed (similar to today's 33C
    −35,485), dealers will need to UNWIND ~$70B of long exposure
    proportionally — i.e. the upside chain is a *spring-loaded* short.
    Phase 7 / 8 / 9 should weight this risk explicitly.
