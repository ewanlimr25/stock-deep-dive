# Phase 4 — Dealer Structure & Gamma

**Ticker:** MARA
**As-of date:** 2026-05-19
**Generated:** 2026-05-20T00:35:00-04:00
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md

## Summary

Dealer positioning regime is **POSITIVE GAMMA** with total GEX $22.6B
across the DTE ≤ 45 chain — dealers are deeply net long gamma at current
spot ($12.08-$12.27). Zero Gamma Level (ZGL) sits at **$4.65** for the
full chain and **$7.85** for the 0DTE/May-22 expiry — both far below
spot. Per-strike GEX shows a **massive gamma wall at $13** (net GEX
$12.7B) and a **secondary wall at $12.5** ($8.0B), with negative GEX
beginning at $11 (-$1.16B) and accelerating below $10. DEX is +$26.2B
net call-long (public), which forces dealers to *buy* underlying as a
hedge for their net-short call book. Term structure is technically
"BACKWARDATION" but the slope is driven entirely by the OPEX-week
2026-05-22 bucket (134% IV vs back-month 88-92%); ex-OPEX, structure is
flat-to-slight-contango. **30-DTE term skew is COMPLACENT (call IV >
put IV, skew_ratio 0.88)** — unusual for a high-beta miner, signals
either crowded call positioning or low downside fear.

## Key signals

- Regime: **POSITIVE gamma**, ZGL $4.65 (full chain) / $7.85 (0DTE) →
  spot $12+ is firmly in long-gamma territory; mean-reversion regime
  [STRUCT:options_structure_gex]
- Largest gamma wall: **$13 strike, net GEX $12.7B** — strongest pin
  magnet in the entire chain [STRUCT:options_structure_gex]
- Secondary wall: **$12.5 strike, net GEX $8.0B** — pin pivot if Friday
  close <$13 [STRUCT:options_structure_gex / options_structure_today_gamma_flip]
- First negative-GEX flip: **$11 strike, net GEX -$1.16B** — the
  "trap door" below which the regime turns short-gamma and trend-amplifying
  [STRUCT:options_structure_gex]
- DEX net +$26.2B (call-heavy public) → dealers BUY underlying as hedge →
  structural systematic bid into rallies [STRUCT:options_structure_dex]
- Vanna NEGATIVE (-922K net) → if IV declines, dealers will SELL stock to
  cut hedges (vol crush = selling pressure) [STRUCT:options_structure_vanna_charm]
- Term skew COMPLACENT (skew_ratio 0.883, call IV 88.8% > put IV 78.4%
  at 25Δ / 30-DTE) — unusual; either crowded calls or no downside fear
  [STRUCT:options_structure_term_skew]
- Front/back IV ratio **1.016** (FLAT) — no event stress signal in the
  near term [STRUCT:options_structure_front_end_iv_ratio]

## Detailed findings

### GEX per strike (DTE ≤ 45)

| Strike | Net GEX (per-share gamma × OI × 100 × spot, $) | Role |
|--------|----------------------------------------------|------|
| 13.0 | **+$12,665,564,779** | Largest gamma wall (resistance + pin magnet) |
| 12.5 | +$8,001,892,329 | Secondary wall (pin pivot) |
| 14.0 | +$2,110,166,429 | Tertiary wall |
| 13.5 | +$1,587,951,616 | Support inside wall |
| 15.0 | +$849,140,416 | Upper resistance |
| 12.0 | +$515,748,191 | Lower pin |
| 16.0 | +$122,387,996 | OTM call wall |
| 17.0 | +$48,364,948 | Far OTM |
| 20.0 | +$57,789,475 | Upside speculation level (phase 3) |
| 11.5 | **-$1,153,515,509** | First negative — trap door begins |
| 11.0 | **-$1,761,150,004** | Heaviest single negative |
| 10.0 | -$415,940,270 | Deep negative |
| 9.5 | -$16,739,234 | Far below |

Total GEX: **+$22,605,177,693**. ZGL: **$4.65**. Spot $12.08-$12.27.

**Mechanical implications:**
- In the $11.50-$15 corridor, dealers are *short gamma below $11.5* and
  *long gamma above $11.5* with massive long-gamma concentration at
  $12.5-$14.
- Stock above $11.5 → dealers sell rallies, buy dips (mean-reversion).
- Stock below $11 → regime flips → dealers buy rallies, sell dips
  (trend-amplifying selloff). Confluence with phase-2 support at $11.75
  is interesting — first DP support exactly at the GEX flip threshold.
- The $13 wall is the single dominant feature: stock is *gravitationally*
  pulled toward $13 if Friday OPEX approaches and it stays close.

### Today's gamma flip (2026-05-22 0DTE bucket)

| Metric | Value |
|--------|-------|
| Total 0DTE GEX | +$20.5B |
| Regime | POSITIVE |
| 0DTE ZGL | $7.85 |
| ATM-flip strike | $7.50 |
| Spot at snapshot | $12.27 |

Key walls (0DTE):
- **$13 support_wall +$12.0B** (yes, the 0DTE GEX label "support" is
  perspective-dependent; in a long-gamma regime *above* the wall, it acts
  as resistance because dealers must sell stock to maintain hedge as gamma
  builds — *below* it acts as a magnet pulling price up)
- $12.5 support_wall +$7.7B
- $14 support_wall +$1.8B
- $13.5 support_wall +$1.5B
- **$11 RESISTANCE_wall -$1.6B** — negative GEX flips this to a true
  resistance for a downside move (vol-expanding floor; if price prints
  below, dealers accelerate the sale)

**Interpretation:** spot $12.27, walking into Friday OPEX, is positioned
*between* the $12.5 pivot and the $13 cap. Most-likely OPEX close band:
**$12.40-$13.00**, with the $13 wall a hard ceiling barring a catalyst.

### DEX (dealer delta exposure)

| Metric | Value |
|--------|-------|
| Call DEX | +$36.4B |
| Put DEX | -$10.2B |
| Net DEX | +$26.2B |
| Interpretation | Public net call-long → dealer is net SHORT calls → hedge by BUYING underlying |
| Spot at snapshot | $12.12 |

**Implication:** the public's $26.2B net call-long position requires
dealers to maintain a long-underlying hedge. As spot rises into the gamma
wall at $13, dealers must keep buying more delta until the gamma
inflection — at which point hedging dynamics flip to selling. This
mechanically creates the "magnet up to $13, ceiling at $13" behavior.

### Vanna & charm

| Metric | Value |
|--------|-------|
| Call vanna | -1,329,762 |
| Put vanna | +407,335 |
| Net vanna | **-922,427** |
| Net charm | +601,899,349 |

**Vanna interpretation (from tool):** Public net vanna negative
(call-heavy book). Falling IV → call delta drops → dealers (short calls)
cut long-underlying hedge → **SELLING pressure**. Rising IV reverses.

→ **This is the key vol/spot correlation:** if IV crushes (which is
typical post-OPEX or after a positive catalyst that releases pent-up
vol demand), dealers will systematically sell MARA underlying. Conversely,
an IV spike (e.g., BTC volatility event) would mechanically lift MARA.

**Charm:** +602M net positive → time decay favors continued dealer
delta accumulation over the next ~30 days. Mildly supportive into Jun
expiry.

### IV term structure

| Expiry | DTE | Avg IV | Contracts |
|--------|-----|--------|-----------|
| 2026-05-22 | 3 | **134.3%** | 6,989 (OPEX 0DTE bucket — inflated by short-DTE math) |
| 2026-05-29 | 10 | 92.0% | 1,789 |
| 2026-06-05 | 17 | 93.3% | 505 |
| 2026-06-12 | 24 | 96.2% | 279 |
| 2026-06-18 | 30 | 90.5% | 1,507 |
| 2026-06-26 | 38 | **111.5%** | 201 ← elevated — possible event-week |
| 2026-07-17 | 59 | 93.0% | 476 |
| 2026-08-21 | 94 | 93.8% | 243 |
| 2026-09-18 | 122 | 95.8% | 445 |
| 2026-12-18 | 213 | 92.2% | 122 |
| 2027-01-15 | 241 | 88.7% | 362 |
| 2027-06-17 | 394 | 91.3% | 63 |
| 2028-01-21 | 612 | 91.0% | 242 |

Structure label: **BACKWARDATION** — but only because of the 134% 5/22
bucket. Ignore that (it's structural OPEX-week math, not event signal)
and term structure is **flat near 90-95% across all back-months**, with
one anomaly: **2026-06-26 at 111.5%**. The 6/26 weekly bump (38-DTE)
suggests a market-implied event in the last week of June — possible
catalysts: MARA Q2 results (typically reported early-Aug, so not earnings),
**BTC-related event (FOMC meeting late June, or quarterly options
expiration)**, or simply low-liquidity weekly noise. Flag for phase 6
macro / catalog.

### Term skew (25Δ, 30-DTE)

| Metric | Value |
|--------|-------|
| 25Δ Put IV | 78.4% |
| 25Δ Call IV | 88.8% |
| Skew (put-call) | **-10.4%** |
| Skew ratio | 0.883 |
| Regime | **COMPLACENT** |

**Highly unusual for a 90% IV crypto-miner:** the 25Δ call is *more
expensive* than the 25Δ put. This means:
- Option market does NOT price elevated tail-risk down.
- Demand for upside calls is real (consistent with phase 1's 20C/22C
  speculation, phase 3's 12.5C/13.5C buildup).
- Crash hedges are cheap on a relative basis — anyone wanting protection
  can buy puts cheaply (a *contrarian* tell for a high-beta name).

The 6P/Jun-18 IV outlier flagged in phase 1 (134% IV, 1,503 contracts)
sits inside this complacent skew — somebody specifically targeting cheap
crash protection. Watch this print: if 6P or similar far-OTM put OI
keeps building, the smart-money read flips from "long-only collar" to
"long-protection accumulating before a known catalyst".

### Front-end IV ratio (7d vs 30d)

| Metric | Value |
|--------|-------|
| Near IV (9-DTE) | 92.0% |
| Far IV (29-DTE) | 90.5% |
| Ratio | **1.016** |
| Regime | **FLAT** |

No event stress in the 1-month window. The 5/22 0DTE bucket inflates the
3-day point, but past OPEX week, the curve is flat. **Confirms no
earnings catalyst between now and 2026-06-18.**

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__options_structure_gex` | `{symbol: MARA, date: 2026-05-19, dte_max: 45, include_zero_gamma: true}` | Total GEX +$22.6B, ZGL $4.65, POSITIVE regime |
| `mcp__uw-pp__options_structure_dex` | `{symbol: MARA, date: 2026-05-19, dte_max: 45}` | Net DEX +$26.2B (call-long public) |
| `mcp__uw-pp__options_structure_vanna_charm` | `{symbol: MARA, date: 2026-05-19, dte_max: 45}` | Net vanna -922K, charm +602M |
| `mcp__uw-pp__options_structure_iv_term_structure` | `{symbol: MARA, date: 2026-05-19}` | Backwardation (front-driven); 6/26 bump 111% |
| `mcp__uw-pp__options_structure_term_skew` | `{symbol: MARA, date: 2026-05-19, dte_target: 30}` | COMPLACENT, skew_ratio 0.883 |
| `mcp__uw-pp__options_structure_front_end_iv_ratio` | `{symbol: MARA, date: 2026-05-19, near_dte: 7, far_dte: 30}` | 1.016 FLAT |
| `mcp__uw-pp__options_structure_today_gamma_flip` | `{symbol: MARA, date: 2026-05-19}` | 0DTE ZGL $7.85, $13 wall +$12B |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** structurally constructive (long-gamma,
  call-heavy DEX → dealers buy dips, magnet to $12.5-$13 walls); but
  vanna is the *single most important risk* — IV crush would force
  dealer selling.
- **Conviction:** 5/5 — gamma mechanics are deterministic and the wall
  geometry is extreme (single strike GEX > $12B at $13 on a $12 stock is
  among the cleanest pin setups in the chain).
- **Three structural levels for phase 9:**
  1. **$13.00** — primary gamma wall, max-pain ceiling, GEX $12.7B
  2. **$12.50** — pin pivot, GEX $8.0B; expected Friday close median
  3. **$11.00** — first negative-GEX flip; below this, regime turns
     short-gamma and trend-amplifying (= invalidation level)
- **Open questions:**
  - What drives the 2026-06-26 IV bump to 111%? Phase 6 must check
    catalysts in that week (FOMC, BTC quarterly expiry, MARA-specific
    event, July OPEX cycle effects).
  - Phase 1 flagged a 6P/Jun-18 134% IV crash-hedge print (1,503 contracts)
    — sitting in a complacent skew regime, this is a contrarian flag.
    Phase 7 should test whether smart-money accumulation insights show
    a hidden distribution.
  - Phase 5 historical: where is current IV in its 1y rank? If 90-95% IV
    is *low* relative to MARA's 1y range, complacency is real and the
    tail hedges (Jan-27 LEAP put + 6P/Jun-18 crash hedge) become cheaper
    to load up.
