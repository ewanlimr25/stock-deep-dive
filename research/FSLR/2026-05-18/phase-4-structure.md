# Phase 4 — Dealer Structure & Gamma

**Ticker:** FSLR
**As-of date:** 2026-05-18 (data anchor: 2026-05-15)
**Generated:** 2026-05-18T00:35:00Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md

## Summary

FSLR sits in a **structurally long-gamma, long-dealer-delta** regime that
materially favors the upside path of least resistance. **Total GEX = +$452M
with ZGL at $121.35 (spot $234.48)** — spot is $113 above zero gamma; it
would take a 48% crash to flip the regime. **Net DEX = +$18.33B (call_dex
+$20.64B vs put_dex −$2.30B)** — public is overwhelmingly call-long, so
dealers are short calls and hedge by **BUYING underlying** as price rises.
The single largest gamma cluster is the **$250 strike at +$228M GEX**, with
secondary positive walls at $240 (+$142M) and $270 (+$38M); the lone
negative-GEX wall near spot is **$230 (−$46.5M)** — a put-heavy strike that
would amplify a downside break. **Term skew is COMPLACENT** (25Δ call IV
56.0% > 25Δ put IV 53.4%; skew_ratio 0.954) and **front-end IV ratio is
FLAT at 1.044** (just below 1.05 backwardation threshold) — a hint of
near-term event stress but no crisis pricing. **Term structure is CONTANGO
overall** but visibly *kinked* at May-22 (58.2% IV vs Jun-5's 55.6%) and
Mar-2027 (62.9% IV) — a one-week-out event premium and an early-2027
catalyst (likely earnings) are priced in. Net read: **dealer regime
strongly bullish-biased, conviction 4/5**.

## Key signals

- Total dealer GEX (DTE≤45) = **+$452M**; regime tag = **POSITIVE**;
  **ZGL = $121.35** vs spot $234.48 → spot is deeply inside long-gamma
  territory (mean-reverting / vol-suppressed) [STRUCT:options_structure_gex].
- Net DEX = **+$18.33B**; public net call-long; **dealer hedge buys
  underlying** as price rises [STRUCT:options_structure_dex].
- **$250 = the gamma magnet**: net_gex = **+$228,076,645** — single largest
  positive cluster in the chain and ~$15 above spot — primary upside target
  in this regime [STRUCT:options_structure_gex].
- **$230 = the resistance wall in 0DTE map**: 0DTE total GEX +$592.9M
  but $230 strike is **−$29.9M GEX (put-heavy)** — breaks below $230 lose
  the gamma cushion and invite amplification [STRUCT:options_structure_today_gamma_flip].
- Term skew = **COMPLACENT** at DTE=30 (call IV 56.0% > put IV 53.4%,
  skew_ratio 0.954) — no tail-hedge premium in 30-day vol; the put hedges
  in phase-1 are buying *cheap* protection [STRUCT:options_structure_term_skew].
- IV term structure is CONTANGO with a kink at May-22 (58.2%) and Mar-2027
  (62.9%) — **one-week event premium + Mar-2027 catalyst priced**
  [STRUCT:options_structure_iv_term_structure].
- Net vanna **−152,638** (call-heavy book) — falling IV would force dealers
  to sell underlying; **rising IV would force a mechanical bid**
  [STRUCT:options_structure_vanna_charm].

## Detailed findings

### GEX (DTE ≤ 45)

- Total GEX: **+$452,282,889**
- Regime: **POSITIVE** — "Dealers net long gamma — expect mean-reversion and
  reduced volatility"
- Underlying ref: $234.48
- Zero Gamma Level: **$121.35** (49% below spot)

Top-10 positive GEX strikes (gamma magnets / upside resistance shelves):

| Strike | Net GEX | Distance vs spot | Role |
|--------|---------|------------------|------|
| **250** | **+$228,076,645** | +6.6% | **Primary upside magnet** |
| **240** | **+$142,045,456** | +2.4% | Secondary call wall |
| **270** | **+$38,096,817** | +15.1% | Outer upside cluster |
| **300** | +$16,412,658 | +27.9% | Round-number LEAP echo |
| **260** | +$16,375,046 | +10.9% | Bridge between 250 and 270 |
| **280** | +$11,977,246 | +19.4% | **Mar-2027 280C strike** (from phase-1) |
| **235** | +$44,315,357 | +0.2% | Near-ATM positive shelf |
| **237.5** | +$2,869,551 | +1.3% | Minor |
| **245** | +$2,268,659 | +4.5% | Minor |
| **290** | +$1,724,293 | +23.7% | Minor |

Negative-GEX strikes (put-heavy / amplification zones below spot):

| Strike | Net GEX | Distance vs spot | Role |
|--------|---------|------------------|------|
| **230** | **−$46,459,956** | −1.9% | **Primary downside friction; if lost, gamma cushion breaks** |
| 210 | −$9,590,383 | −10.4% | Mid-tier put wall |
| 215 | −$2,842,244 | −8.3% | Put cluster |
| 200 | −$2,657,711 | −14.7% | Tail hedge zone |
| 190 | −$1,434,727 | −18.9% | Far OTM put cluster |
| 180 | −$1,368,637 | −23.2% | LEAP put cluster |

**Spatial story:** Spot $234.48 sits in a strong positive-gamma corridor
between the small −$46M at $230 (put wall just below) and the massive
+$142M / +$228M at $240 / $250 above. Long-gamma + this strike layout
implies dealers will **buy dips toward $230 and sell rallies near $250**.
That's a built-in $20-wide mean-reversion range with bullish drift bias
(because the magnet above is much larger than the wall below).

### DEX (DTE ≤ 45)

- Net DEX: **+$18,333,477,793**
- Call DEX: +$20,635,654,970
- Put DEX: −$2,302,177,177
- Interpretation (verbatim): *"Public is net call-long → dealers net short
  calls → dealer hedge is to BUY underlying."*

The public call book is **~9× the put book in delta-dollar terms**. This is
extreme and consistent with a name where institutional sentiment skews
bullish through 45 DTE.

### Vanna + charm (DTE ≤ 45)

- Net vanna: −152,638 (call vanna −167,433; put vanna +14,794)
- Net charm: +1,896,226

Interpretation (verbatim): *"Public net vanna negative (call-heavy book).
Falling IV → call delta drops → dealers (short calls) cut long-underlying
hedge → SELLING pressure. Rising IV reverses."*

Trade-relevant implication: an **IV expansion event** (catalyst, surprise,
fast move higher) creates a **mechanical bid** as dealers re-hedge.
Conversely, a slow grind with IV bleed creates incremental selling
pressure from delta-hedging — i.e. the up-leg needs vol expansion to
break out cleanly; a quiet drift higher will encounter dealer-hedge
selling near $250.

### IV term structure

- Structure: **CONTANGO** (no algo-flagged kink)
- 16 expiries (avg IV %):

| Expiry | DTE | Avg IV | Note |
|--------|-----|--------|------|
| 2026-05-15 | 0 | 15.2% | OPEX-day collapse, intrinsic-only contracts |
| 2026-05-22 | 7 | **58.2%** | **Elevated vs 6/5 neighbor — event stress** |
| 2026-05-29 | 14 | 54.1% | |
| 2026-06-05 | 21 | 55.6% | |
| 2026-06-12 | 28 | 55.0% | |
| 2026-06-18 | 34 | 55.8% | June OPEX |
| 2026-06-26 | 42 | 55.5% | |
| 2026-07-17 | 63 | 55.2% | |
| 2026-08-21 | 98 | 58.3% | **Slight bump** |
| 2026-09-18 | 126 | 56.7% | |
| 2026-12-18 | 217 | 56.8% | |
| 2027-01-15 | 245 | 59.7% | **Steepens** |
| 2027-03-19 | 308 | **62.9%** | **Catalyst priced — matches phase-1 280C IV** |
| 2027-06-17 | 398 | 61.8% | |
| 2028-01-21 | 616 | 57.8% | LEAP normalize |
| 2028-06-16 | 762 | 56.1% | |

**Manual kink callouts:**
1. **May-22** at 58.2% is +260bp above May-29 — this is a single-week
   event premium. With phase-1's $1.27M put hedge layer at May-22/29
   strikes 220–230, this is consistent with hedge funds paying up for
   one-week downside cover around an unseen catalyst.
2. **Mar-2027** at 62.9% — the peak in the term structure. Aligns with
   the phase-1 280C ASK print at 57.5% IV (slightly below the chain
   average — buyer got a small IV discount on size). This is the
   institutional bet's vol footprint.

### Term skew (DTE 30)

- 25Δ Call IV: **56.04%**
- 25Δ Put IV: **53.44%**
- Skew: −0.026 (calls > puts)
- Skew ratio: **0.954**
- Interpretation: **COMPLACENT**

Normal equity skew has puts richer than calls (insurance premium). FSLR's
inverted skew means the market is paying *more* for upside than downside.
This implies:
- The put hedges seen in phase-1 are being bought into **cheap**
  protection — a discount.
- Calls are richly bid — consistent with the institutional 280C buyer
  paying 57.5% IV (in line with chain average for 1Y LEAP).

### Front-end IV ratio (near 7 vs far 30)

- Near IV (4 DTE actual): 58.23%
- Far IV (31 DTE actual): 55.78%
- Ratio: **1.044**
- Regime: **FLAT** (threshold for backwardation = 1.05)

Just below the formal backwardation cutoff. Implication: **mild near-term
event stress** consistent with a one-week-out catalyst, but not a full
risk-off backwardation. The market is hesitating, not panicking.

### Today's gamma flip (0DTE map, 2026-05-15)

- Today's spot: $232.95
- Today's total GEX: **+$592,913,961**
- Today's ZGL: **$166.4**
- ATM flip strike: $180
- Regime: **POSITIVE**

Key intraday walls (as labeled by tool):

| Strike | Today GEX | Role (per tool) | My read |
|--------|-----------|-----------------|---------|
| 240 | +$293,241,817 | support_wall | Largest 0DTE gamma cluster — magnet from below |
| 235 | +$166,265,131 | support_wall | Near-spot positive cluster |
| 220 | +$119,031,907 | support_wall | Downside positive shelf |
| 237.5 | +$37,784,923 | support_wall | Minor |
| **230** | **−$29,855,390** | **resistance_wall** | **Negative-GEX strike — break = amplification** |

The tool's labeling is consistent with treating positive-GEX strikes as
"support" magnets and negative-GEX strikes as resistance to be broken.
**Key takeaway: the $230 strike is the line in the sand**.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__options_structure_gex` | `{symbol: FSLR, dte-max: 45, date: 2026-05-15}` | Total +$452M, regime POSITIVE, ZGL $121.35 |
| `mcp__uw-pp__options_structure_dex` | `{symbol: FSLR, dte-max: 45, date: 2026-05-15}` | Net DEX +$18.33B; dealer hedge buys |
| `mcp__uw-pp__options_structure_vanna_charm` | `{symbol: FSLR, dte-max: 45, date: 2026-05-15}` | Vanna −152K, charm +1.9M |
| `mcp__uw-pp__options_structure_iv_term_structure` | `{symbol: FSLR, date: 2026-05-15}` | CONTANGO, 16 expiries, kinks at May-22 + Mar-27 |
| `mcp__uw-pp__options_structure_term_skew` | `{symbol: FSLR, dte-target: 30, date: 2026-05-15}` | COMPLACENT, skew −0.026 |
| `mcp__uw-pp__options_structure_front_end_iv_ratio` | `{symbol: FSLR, near-dte: 7, far-dte: 30, date: 2026-05-15}` | Ratio 1.044, regime FLAT |
| `mcp__uw-pp__options_structure_today_gamma_flip` | `{symbol: FSLR, date: 2026-05-15}` | 0DTE total +$593M, support walls 240/235/220, resistance 230 |

## Tool errors

None.

## Verdict for downstream phases

- **Dealer regime:** **LONG GAMMA / LONG DELTA** — vol-suppressed,
  mean-reverting, with built-in dealer-hedge bid as price grinds higher.
- **Conviction:** **4/5.** Clean structure: ZGL is 49% below spot, total
  GEX is large and positive, DEX call_dex 9× put_dex, skew complacent.
  Half-point taken for the slight FLAT/backwardation tension at the
  one-week tenor (May-22 58% IV) — signals a near-term catalyst that could
  swing the structure either way over the next few sessions.
- **Three structural levels for phase-9:**
  1. **$250 — primary gamma magnet** (+$228M GEX cluster). In a long-gamma
     regime, dealers cap rallies into this strike; this is the **first
     bullish target / partial-take area**.
  2. **$240 — secondary gamma wall** (+$142M GEX, 0DTE +$293M). First
     break-up confirmation level; close above on volume opens path to $250.
  3. **$230 — must-hold line** (−$46.5M GEX 45D, −$30M 0DTE). Loss of $230
     forfeits the long-gamma cushion and pulls structure toward the
     phase-2 dark-pool floor at $231.62, then $224–228.
  4. **$121 ZGL** — structural disaster floor, not a tradeable level but a
     reminder that the regime is *very* far from flipping short-gamma.
- **Open questions:**
  - What catalyst is priced into May-22 IV (one week out)? Earnings?
    Capacity announcement? Tariff/IRA-related news? (→ phase-6 macro)
  - Has FSLR's IV rank historically run at this 55–60% level, or is this
    elevated vs the 1Y distribution? (→ phase-5 historical)
  - Will composite tools (insights_*) confirm the bullish dealer regime
    with cross-signal confluence? (→ phase-7)
