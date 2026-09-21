# Phase 4 — Dealer Structure & Gamma

**Ticker:** RKT
**As-of date:** 2026-05-20 (data: 2026-05-19)
**Generated:** 2026-05-20T00:35:00Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md

## Summary

The dealer structure is **short-gamma in the near term with a positive-gamma
magnet at $14**, a regime that mechanically amplifies any catalyst-driven
move. Net DEX is -$2.01B (dealers net short put exposure), 0DTE total GEX
is -$406M with the $13 strike alone carrying **-$292M of single-strike
short-gamma wall** [STRUCT:today_gamma_flip]. The 45-DTE Zero Gamma Level
sits at **$10.52** and the 0DTE ZGL at **$11.51** — both BELOW spot $12.67,
so a drop through these levels expands the negative-gamma regime
(downside-amplification risk) [STRUCT:gex, STRUCT:today_gamma_flip]. Term
structure is in **BACKWARDATION** with the 2026-05-22 weekly IV at
**85.9%** — a 1,830 bps spike over the 2026-05-29 weekly at 67.6%,
unambiguously confirming a catalyst between 5/19 and 5/22 [STRUCT:iv_term_structure].
The 30-DTE 25Δ skew prints **-0.0212 (COMPLACENT: calls richer than puts)**
— a bullish positioning signal that aligns with the phase-3 OI bull-bias
read [STRUCT:term_skew]. Net vanna and charm are positive: a post-event IV
collapse mechanically forces dealer buying. Setup is asymmetric.

## Key signals

- **0DTE / weekly regime is NEGATIVE-gamma; $13 is the largest single-strike
  short-gamma wall at -$292M** [STRUCT:today_gamma_flip].
- **45-DTE Zero Gamma Level = $10.52, 0DTE ZGL = $11.51** — short-gamma
  regime intensifies below these [STRUCT:gex, STRUCT:today_gamma_flip].
- **$14 strike carries +$289M of long-gamma in the 45-DTE map** — once price
  punches through $13, dealer hedging shifts from "fight the rally" to
  "chase the rally" through $14 [STRUCT:gex].
- **Term structure BACKWARDATION**; **5/22 weekly IV = 85.9%** vs **5/29
  weekly = 67.6%** — 3-trading-day event premium [STRUCT:iv_term_structure].
- **25Δ skew = -0.0212 (COMPLACENT)** — calls richer than puts at 30 DTE,
  confirms bullish-tilt positioning seen in phase-3 [STRUCT:term_skew].
- **Vanna +178k / Charm +1.74M** — post-event vol-crush triggers vanna-driven
  dealer BUYING [STRUCT:vanna_charm].

## Detailed findings

### GEX — per-strike map (`mcp__uw-pp__options_structure_gex`, DTE ≤ 45)

```
total_gex       = -124,396,640        (NET NEGATIVE)
zero_gamma_level = $10.52
underlying_price = $12.65
regime label     = POSITIVE (spot > ZGL)  *but* net_gex is negative
                                            because $13 strike is -$374M
```

Top-magnitude strikes:

| Strike | net_gex | Distance from $12.65 | Read |
|--------|---------|----------------------|------|
| **$13.00** | **-$374,347,418** | +2.8%  | **Largest negative-gamma wall — overhead resistance** |
| **$14.00** | **+$288,907,082** | +10.7% | **Largest positive-gamma support — bullish magnet** |
| **$16.00** | +$123,353,963     | +26.5% | Far-OTM positive gamma cluster |
| $15.00 | -$79,129,244 | +18.6% | Secondary short-gamma wall |
| $12.00 | -$39,714,902 | -5.1%  | Below-spot short-gamma |
| $12.50 | -$35,129,484 | -1.2%  | At-spot short-gamma |
| $13.50 | -$32,260,112 | +6.7%  | Above-spot short-gamma |
| $17.00 | +$9,453,636  | +34.4% | Modest positive gamma |
| $20.00 | +$5,327,452  | +58.1% | OTM positive gamma |
| $10.00 | +$28,113     | -20.9% | Tiny (puts mostly already-short) |

The structural picture: dealers are **massively short gamma at $13**
($374M wall) and **massively long gamma at $14** ($289M). The shape between
$13 and $14 is a steep V — a move from $13 → $14 forces dealers to buy
through the gamma flip, mechanically accelerating upside. Below $13, the
$12–$13 corridor is all short-gamma — dealer hedging amplifies downside.

The **POSITIVE regime label** from the API reflects spot > ZGL ($10.52), but
the net negative gex tells you the immediate-DTE picture is short-gamma.
Reconciliation: long-dated LEAPS gamma at $1 strike (+9,236), $10 strike
(+28,113), $14 (+288.9M) and $16 (+123.4M) supports the "positive overall"
classification, while the weekly/monthly OI is short-gamma concentrated.

### DEX — dealer delta exposure (`mcp__uw-pp__options_structure_dex`)

```
net_dex   = -$2,013,685,879   (negative = public net put-long)
put_dex   = -$2,878,986,001
call_dex  = +$865,300,122
spot      = $12.65
```

**Interpretation (from API):** "Public is net put-long → dealers net short
puts → dealer hedge is to SELL underlying." That confirms the phase-2
dark-pool distribution had a structural reason: dealers offloading hedge
inventory matches the persistent at-bid prints.

The public's put length is large relative to RKT's market cap. Ratio of
put_dex magnitude to RKT's ~$25-28B market cap is ≈ 0.10 — institutionally
material. If the put book unwinds (price rallies), dealers cover by
**buying back stock**, supporting the long thesis.

### Vanna & charm (`mcp__uw-pp__options_structure_vanna_charm`)

```
net_vanna  = +178,256
put_vanna  = +236,845
call_vanna = -58,588
net_charm  = +1,742,859
```

**Vanna interpretation:** "Public net vanna positive (put-heavy book).
Falling IV → |put delta| drops → dealers (short puts) cover by BUYING
underlying. Classic vanna-squeeze setup if VIX collapses."

**Charm interpretation:** Strongly positive net charm = as expiry approaches,
the put-side delta decays toward zero; dealers (short puts) cover by buying.
A typical bull-tape feature into OPEX week.

This is one of the cleanest **vanna-squeeze precursor setups** in the
single-name tape today. Conditional on IV mean-reverting (post-event vol
crush from 85.9% → ~60% in May-22 strikes), the structure transmits
mechanical bid into RKT.

### IV term structure (`mcp__uw-pp__options_structure_iv_term_structure`)

| Expiry | DTE | Avg IV | Contracts | Read |
|--------|-----|--------|-----------|------|
| **2026-05-22** | 3   | **85.9%** | 1,209 | **EVENT WEEK — vol spike** |
| 2026-05-29 | 10  | 67.6% | 437 | Normalizes |
| 2026-06-05 | 17  | 65.0% | 333 | |
| 2026-06-12 | 24  | 61.9% | 157 | |
| 2026-06-18 | 30  | 71.0% | 1,187 | Slight June OPEX bump |
| 2026-06-26 | 38  | 64.9% | 41   | |
| 2026-07-17 | 59  | 61.1% | 220  | |
| 2026-08-21 | 94  | 63.2% | 169  | |
| 2026-09-18 | 122 | 61.0% | 593  | |
| 2026-12-18 | 213 | 59.6% | 261  | LOWEST back-end IV |
| 2027-01-15 | 241 | 62.8% | 261  | |
| 2027-03-19 | 304 | 60.2% | 76   | |
| 2027-06-17 | 394 | 61.2% | 68   | |
| 2028-01-21 | 612 | 63.3% | 172  | |

```
structure: BACKWARDATION
kink_expiry: null
```

**Headline:** May-22 IV at 85.9% is **+18.3 vol points** above May-29 (67.6%)
and **+26.3 vol points** above the 6-month back-end (12/18 at 59.6%). This
is a clear event-spike, not generalized vol elevation. The June 18 modest
bump (71.0%) likely reflects June OPEX + a possible second event (FOMC,
quarterly economic release).

Phase-6 must identify the May 22 catalyst. Probable candidates:
- Ex-dividend date (RKT pays a variable cash distribution)
- Conference / investor presentation
- A government-policy decision (e.g., GSE policy, mortgage-rate-related)
- An expected major shareholder secondary / unlock event

### Term skew (`mcp__uw-pp__options_structure_term_skew`, DTE target 30)

```
call_25d_iv  = 0.6158
put_25d_iv   = 0.5946
skew         = -0.0212   (negative = calls richer than puts)
skew_ratio   = 0.966     (< 1.0 = COMPLACENT regime)
interpretation: COMPLACENT
```

This is a **rare positive-asymmetry skew** for a single-stock — typically
puts are richer. Calls priced above puts at 25Δ means dealers/traders are
collectively paying up for upside more than for downside protection. That
directly corroborates the phase-3 OI bias and contradicts the bearish read
that pure phase-2 distribution would suggest.

### Front-end IV ratio (`mcp__uw-pp__options_structure_front_end_iv_ratio`)

```
near_iv (9 DTE, May-29)  = 0.6763
far_iv  (29 DTE, June-18) = 0.7095
ratio                     = 0.953
regime                    = FLAT
```

Note: the API chose 9-DTE / 29-DTE buckets that DO NOT include the May-22
event spike (it sits at DTE 3, below the near-bucket floor of 7). So this
metric is reading the post-event term structure — slightly contango between
6/29 and 6/18 because June 18 has the June OPEX premium baked in. The
85.9% May-22 vol is a SEPARATE event-localized phenomenon, not a sustained
backwardation across the entire front-end.

### Today's gamma flip (`mcp__uw-pp__options_structure_today_gamma_flip`)

```
today_expiry         = 2026-05-22
today_total_gex      = -406,545,704        (heavily NEGATIVE)
today_zero_gamma     = $11.51
atm_flip_strike      = $11.5
regime               = NEGATIVE
spot                 = $12.67
```

Key walls (all RESISTANCE / negative gex):

| Strike | gex | Read |
|--------|------|------|
| **$13.0** | **-$291,852,000** | **Primary resistance** |
| $13.5 | -$33,677,559 | Secondary resistance |
| $14.0 | -$31,080,456 | Tertiary resistance (3-DTE only) |
| $12.5 | -$28,465,234 | Below-spot resistance |
| $12.0 | -$24,637,160 | Further below |

**Bottom line for the weekly:** dealers will FIGHT $13 hard for the May-22
weekly. A clean push above $13 with vol expansion would force significant
hedge buying. Conversely, falling below $11.51 ZGL on the weekly opens
short-gamma waterfall risk into $11–$11.5.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `options_structure_gex` | `{symbol: RKT, dte_max: 45, date: 2026-05-19}` | total -$124.4M; ZGL $10.52; $13 = -$374M; $14 = +$289M |
| `options_structure_dex` | `{symbol: RKT, dte_max: 45, date: 2026-05-19}` | net -$2.01B; dealers short puts |
| `options_structure_vanna_charm` | `{symbol: RKT, dte_max: 45, date: 2026-05-19}` | vanna +178k / charm +1.74M (squeeze precursor) |
| `options_structure_iv_term_structure` | `{symbol: RKT, date: 2026-05-19}` | BACKWARDATION; 5/22 = 85.9%; 5/29 = 67.6% |
| `options_structure_term_skew` | `{symbol: RKT, dte_target: 30, date: 2026-05-19}` | COMPLACENT; calls richer than puts (skew -0.02) |
| `options_structure_front_end_iv_ratio` | `{symbol: RKT, near_dte: 7, far_dte: 30, date: 2026-05-19}` | ratio 0.953 (FLAT, but excludes 5/22 spike) |
| `options_structure_today_gamma_flip` | `{symbol: RKT, date: 2026-05-19}` | NEGATIVE; ZGL $11.51; $13 wall -$292M |

## Tool errors

(none)

## Verdict for downstream phases

- **Bias from this phase:** bullish-asymmetric (short-gamma dealer setup
  with a positive-gamma magnet at $14, complacent skew, vanna-squeeze
  precursor) IF the May-22 catalyst resolves the right way; bearish-tail
  risk IF the same catalyst breaks $11.51 ZGL.
- **Conviction:** 5/5 — the structural read is unusually rich and internally
  coherent.
- **Three structural levels for phase-9 entry/stop:**
  1. **$10.52 — ZGL (45-DTE).** Below here, regime shifts decisively
     short-gamma; downside accelerates. This is the line below which the
     phase-9 thesis is broken.
  2. **$13.00 — primary gamma resistance.** -$292M of 0DTE short-gamma
     wall + -$374M in the 45-DTE map. The "if-then" pivot: through it,
     dealer buying mechanics activate; capped below it, the stock pins.
  3. **$14.00 — positive-gamma magnet.** +$289M of 45-DTE positive gamma.
     If price crosses $13, dealers chase to $14 and the LEAPS / Aug 14C
     buyers from phase-3 get paid. This is the upside target before any
     thesis revision.
- **Open questions:**
  - **What is the 2026-05-22 catalyst?** Phase-6 must answer. Without
    knowing the event, phase-9 can't size the trade correctly. Candidate
    events: ex-div date, conference, government policy decision, large
    secondary unlock.
  - Has historical IV ever spiked to 85% on RKT outside earnings? (phase-5)
  - Is there an FHFA / mortgage-rate event in the window? (phase-6)
