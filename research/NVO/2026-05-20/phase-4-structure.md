# Phase 4 — Dealer Structure & Gamma

**Ticker:** NVO
**As-of date:** 2026-05-20
**Generated:** 2026-05-20T21:05:00-04:00
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md

## Summary

Dealer structure is **structurally bullish for an upside grind**:
NVO sits **deep in POSITIVE GEX** (total $2.10B, ZGL $27.44 vs spot
$44.90), with the two largest positive-gamma walls at **$45 ($776M GEX)
and $50 ($825M GEX)** — the same $45 line phase-1 LEAP buyer and phase-2
DP buyer anchored, and the $50 call-wall phase-3 flagged. DEX is **+$6.22B
net**, meaning the public is net-long calls and **dealers hedge by BUYING
the underlying** — the bid that absorbed today's flow. Skew is **COMPLACENT**
(25Δ put IV 38.27% vs call IV 38.35%, ratio 0.998) — no downside premium
priced; upside calls are cheap relative to puts. The structural risk is
below $44 where dealers flip into negative gamma ($93M short γ at $44,
$107M at $40); that is the level whose loss would change the regime.

## Key signals

- **Regime: POSITIVE GEX, total $2,099,855,377; ZGL = $27.44; spot $44.90** — dealers mean-revert / suppress vol [STRUCT:gex]
- **Top positive-GEX walls:** $50 = **+$825M**, $45 = **+$776M**, $47 = +$282M, $46 = +$239M [STRUCT:gex]
- **Top negative-GEX pockets:** $44 = **-$93M**, $40 = -$107M, $42.5 = -$15.8M, $43 = -$9M — the $44 line is the immediate destabilizer if lost [STRUCT:gex]
- **DEX = +$6,224,791,580** — public call-heavy, dealer hedge is **BUY underlying**; this is the mechanical bid that absorbed the $26.9M post-close DP block in phase 2 [STRUCT:dex]
- **Term skew 30 DTE: COMPLACENT** (put_25Δ 38.27% ≈ call_25Δ 38.35%; ratio 0.998) — **upside calls structurally cheap** [STRUCT:term_skew]
- **Term structure: front-end "backwardation" is a 2-DTE artifact** (5/22 IV 68% vs 5/29 IV 38.6%); 5/29 onward IVs are 38–46% in mild contango [STRUCT:iv_term_structure]
- **Front-end IV ratio = 0.957 = FLAT** — no event-stress vol bid [STRUCT:front_end_iv_ratio]
- **Today's 0DTE walls (5/22 expiry):** support stack at $47/$46/$45; **resistance at $44** (only negative-γ strike near spot) [STRUCT:today_gamma_flip]

## Detailed findings

### GEX — total + top per-strike

| Strike | Net GEX ($) | Role |
|-------:|------------:|------|
| **45** | **+776,572,748** | Largest near-money positive wall — phase-1/2/3 confluence |
| **50** | **+825,040,572** | Call wall (matches 32k OI $50C Jun phase-3) — first major resistance |
| 47 | +281,679,560 | Support stack |
| 46 | +238,732,873 | Support stack |
| 46.5 | +40,212,039 | (between walls) |
| 45.5 | +40,212,039 | Just above $45 |
| 48 | +39,409,434 | Mid-zone support |
| 49 | +25,228,873 | Light positive |
| 55 | +64,352,248 | Far-OTM call wall |
| 60 | +8,358,924 | Light far-OTM |
| **44** | **−93,089,846** | **Short-γ pocket — destabilizer if breached** |
| **42.5** | **−15,818,922** | Light short-γ pocket |
| 43 | −9,075,792 | Same negative cluster |
| 43.5 | −6,443,258 | Same |
| **40** | **−107,483,594** | Large short-γ pocket (downside trend-amplifier) |
| 35 | −12,320,079 | Smaller short-γ, far OTM |
| Total | **+2,099,855,377** | Positive regime |

**Read:** A continuous positive-gamma corridor sits from $45 → $50.
A negative-gamma "trap-door" sits at $44, then a much bigger one at $40.
The structure rewards staying above $45; it punishes losing $44.

### DEX

- `call_dex` = +$12,959,771,404 (public long calls)
- `put_dex` = −$6,734,979,824 (public long puts but smaller)
- `net_dex` = **+$6,224,791,580**

**Interpretation:** dealers are net short calls more than they are net short
puts → dealer hedge = **BUY underlying**. This is the regime-level
mechanical bid that explains why phase-2's $26.9M mega-block could clear at
NBBO mid without driving the tape down — dealers were net-buyers themselves.

### Vanna + charm

- `net_vanna` = −301,484; `call_vanna` = −592,415; `put_vanna` = +290,931
- `net_charm` = +14,518,176

**Vanna:** Public net-vanna is **negative** (call-heavy book). If IV falls,
call deltas drop → dealers (short calls) cut their long-stock hedge →
**SELLING pressure**. If IV rises, dealers cover → mechanical bid.
**Trading implication:** an **IV expansion** is the catalyst that turns
dealer hedging from neutral into a tailwind. With skew complacent and IVs
not stressed, a real catalyst (positive earnings beat, positive Phase 3
data, regulatory tailwind) could trigger this. Conversely, the regime is
fragile to an IV crush.

**Charm:** Positive net charm — dealers' long-stock hedge bleeds over time,
mild headwind into expiries. Manageable, not regime-defining.

### IV term structure

| Expiry | DTE | Avg IV | Contracts |
|--------|----:|-------:|----------:|
| 2026-05-22 | 2 | **68.0%** | 1,006 |
| 2026-05-29 | 9 | 38.6% | 600 |
| 2026-06-05 | 16 | 38.3% | 303 |
| 2026-06-18 | 29 | 40.4% | 833 |
| 2026-06-26 | 37 | 39.0% | 79 |
| 2026-07-17 | 58 | 40.1% | 674 |
| 2026-08-21 | 93 | 43.8% | 166 |
| 2026-09-18 | 121 | 43.4% | 287 |
| 2026-12-18 | 212 | 41.9% | 268 |
| 2027-01-15 | 240 | 44.7% | 285 |
| 2027-06-17 | 393 | 44.8% | 105 |
| 2028-01-21 | 611 | 45.2% | 229 |

The **5/22 = 68%** IV is a 2-DTE numeric artifact (very low time value
inflates the implied number) — discount it.
From **5/29 onward the curve is in mild contango** (38.6% → 45.2% across
9 → 611 DTE). No genuine event-stress signal. The Aug 21 / Sep 18 bumps
(43–44%) align with the next earnings cycle (Q2 reported mid-Aug 2026).

`kink_expiry: null` → no binary event embedded in pricing.

### Term skew (30 DTE)

- put_25Δ_iv = **0.3827** (38.27%)
- call_25Δ_iv = **0.3835** (38.35%)
- skew = **−0.0008**, ratio = **0.998**
- Label: **COMPLACENT**

This is unusually flat skew for a single name carrying obesity-drug
controversy risk. Two reads:
1. **Bullish:** market is no longer pricing tail risk — accumulation phase complete on the bear side.
2. **Risk:** complacency precedes vol shocks; a one-sided positioning unwind would expand realized vol.

For a long-biased structure, complacent skew is a **gift** — calls are
priced like puts; buying upside convexity is unusually cheap.

### Front-end IV ratio (event stress)

- near_iv (9 DTE) = 0.386, far_iv (29 DTE) = 0.4035
- ratio = **0.957 → FLAT**
- No imminent binary catalyst priced in.

### Today's gamma flip (2026-05-22 0DTE expiry view)

- Today total GEX (5/22 expiry only) = $544,854,170 positive
- ATM flip strike = $28 (deep below spot — irrelevant)
- 0DTE zero-gamma = $27.44 (same as the full-chain ZGL → all expiries align)
- **Key walls (intraday, 5/22):**
  - **Support stack:** $47 (+$221M), $46 (+$207M), $45 (+$129M), $46.5 (+$35M)
  - **Resistance:** **$44 (-$83M GEX = short-gamma resistance)** — if NVO falls toward $44, dealer hedging amplifies the move down
- Closing price $45.07 → above support wall, below upper walls → **inside the support stack**

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `options_structure_gex` | `{symbol: NVO, dte_max: 45, include_zero_gamma: true}` | POSITIVE regime, total +$2.10B, ZGL $27.44, top walls $45/$50 |
| `options_structure_dex` | `{symbol: NVO, dte_max: 45}` | net_dex +$6.22B, dealer hedge = BUY |
| `options_structure_vanna_charm` | `{symbol: NVO, dte_max: 45}` | net_vanna -301k (IV-rise = tailwind), charm +14.5M |
| `options_structure_iv_term_structure` | `{symbol: NVO}` | Backwardation tag, but artifact of 2-DTE; rest = mild contango |
| `options_structure_term_skew` | `{symbol: NVO, dte_target: 30}` | skew_ratio 0.998 → COMPLACENT |
| `options_structure_front_end_iv_ratio` | `{symbol: NVO, near_dte: 7, far_dte: 30}` | 0.957 = FLAT |
| `options_structure_today_gamma_flip` | `{symbol: NVO}` | Today expiry 5/22; support $47/$46/$45; resistance $44 |

## Tool errors

None.

## Verdict for downstream phases

- **Dealer regime:** **POSITIVE GAMMA (long-γ) above $44; flips to short-γ between $44 and $40.** Net DEX is dealer-buy. Vanna profile rewards IV expansion (mechanical bid).
- **Conviction:** **4.5/5** — the gamma map is dense enough on NVO that ZGL and per-strike walls are statistically meaningful. Half-point discount for vanna's two-sidedness (it's a tailwind only if IV rises — neutral-to-headwind if IV bleeds).
- **Three structural levels for phase-9:**
  1. **$45 — bullish anchor and largest near-money positive wall ($776M GEX).** Lose-and-hold below = regime change.
  2. **$50 — major call wall ($825M GEX) + 32k Jun OI ceiling.** First profit-take. Above $50, walls thin out → potential acceleration if it can absorb the call wall.
  3. **$44 (and the $40 pocket below) — short-gamma trap-door.** $44 is the binary regime line; $40 is the lower magnet if the trap-door opens.
- **Open questions:**
  - Phase 5 must answer: where does today's IV sit relative to 30/90/180-day history (percentile/rank)? The "complacent skew" call only matters in absolute IV context.
  - Is the $50 call wall organically distributed (covered-call writers) or concentrated (single dealer short)? OI by counterparty isn't visible — phase 5 historical OI trend at $50 will at least tell us if it's been growing fast.
  - The negative vanna means an **IV crush is the regime's main risk.** What macro catalysts in phase 6 could drive a vol-down event for healthcare ADRs?
