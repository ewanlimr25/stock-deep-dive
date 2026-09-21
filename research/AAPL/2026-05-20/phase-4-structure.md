# Phase 4 — Dealer Structure & Gamma

**Ticker:** AAPL
**As-of date:** 2026-05-20
**Generated:** 2026-05-20T23:00:00Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md

## Summary

AAPL is in a **strong dealer-long-gamma regime** above $300. Total GEX
through 45 DTE = **$648.7B with regime POSITIVE** [STRUCT:gex], and the
gamma surface is dominated by a single mega-positive cluster at the
$297.5 / $300 / $302.5 strikes ($264.9B + $13.0B + $139.0B respectively).
0DTE-only flip level is **$287.86** [STRUCT:today_gamma_flip], with
$302.5 acting as a **$1.38T positive gamma support wall**. Net DEX
$+13.69T tells you the public is structurally call-long and dealers
must buy underlying on every up-move to maintain their hedge
[STRUCT:dex] — that's a mechanical bid as long as IV holds. Term
structure is **CONTANGO** (front-end ratio 0.863) with **complacent**
30-DTE skew (1.01 put/call ratio) [STRUCT:term_skew] — no event stress
priced in. The structural read: **buy-the-dip / sell-the-rip into
$300–$303 is the dealer-enforced path** for the next 5–10 sessions
unless spot breaks $295 (gamma flip zone) or IV expands materially
(vanna mechanics flip from selling to buying).

## Key signals

- **Regime: POSITIVE (long gamma)**, total GEX $648.7B
  [STRUCT:gex]. Dealers sell rallies, buy dips → mean-reversion.
- **Mega gamma support walls (0DTE):** $302.5 ($1,383B), $300 ($874B),
  $305 ($189B) [STRUCT:today_gamma_flip]. These match the phase-2 DP
  $302.25 clearing zone exactly — institutional buys + dealer long-gamma
  reinforces $300–$303 as the magnet band.
- **Net DEX $+13.69T** (public extreme call-long) → dealer hedge **buys
  underlying** [STRUCT:dex]. Combined with phase-2 DP buy-skew of 0.794
  in the mega tier, this is the **structural underpinning** of any
  intraday bid.
- **Net vanna NEGATIVE (−48.2M), net charm POSITIVE (+4.33B)**
  [STRUCT:vanna_charm]. Translation: if IV **falls** from here,
  dealers de-hedge by **selling** underlying (charm + vanna both
  bleed the mechanical bid). If IV **expands**, dealers buy. AAPL
  currently sits at low IV (23–27%) — modest room for a vanna
  squeeze higher if IV pops.
- **Term skew COMPLACENT** (put_25d_iv 24.1% vs call_25d_iv 23.85%,
  ratio 1.01) [STRUCT:term_skew]. No tail-hedge bid in 30-DTE puts —
  consistent with the LEAP buyer's view that downside is bounded but
  divergent from phase-1's 5-day bearish sweep persistence.
- **Front-end IV ratio 0.863 (CONTANGO)** with 7-DTE 23.23% vs
  29-DTE 26.93% [STRUCT:front_end_iv_ratio]. No near-term catalyst
  pricing in.

## Detailed findings

### GEX (per-strike, top concentrations within 45 DTE)

| Strike | net_gex | Role |
|--------|---------|------|
| **300** | **+264,889,004,599** | Largest positive — primary magnet |
| **302.5** | **+139,038,611,170** | Second positive — today's DP clearing zone |
| 297.5 | +12,993,778,210 | Positive, lower edge of long-gamma band |
| 280 | +1,155,785,393 | Far-OTM positive (LEAP land) |
| 275 | +224,061,988 | Far-OTM positive |
| 292.5 | **−1,741,269,157** | Biggest negative in the 280–295 zone |
| 285 | −601,083,593 | Negative |
| 295 | −505,424,312 | Negative |
| 290 | −376,304,772 | Negative |
| 287.5 | −344,993,144 | Negative |
| 270 | −112,810,303 | Negative |

**ZGL (45-DTE):** **$95.52** [STRUCT:gex]. This is an **artifact**:
the massive deep-ITM OI mass at $100 (legacy LEAP land) pulls the
algebraic zero unrealistically low. **Use the 0DTE ZGL of $287.86
instead** [STRUCT:today_gamma_flip] for near-term hedge mapping.

**Effective gamma flip zone:** $287.86–$295. Below $295 net gamma
turns negative and dealers must SELL into weakness (trend
amplification). Above $297.5 dealers are progressively longer gamma
all the way to $302.5+, which is the mean-reversion regime.

### DEX (dealer delta exposure)

| Field | Value |
|-------|-------|
| `call_dex` | +14,505,722,707,611 |
| `put_dex` | −818,130,366,333 |
| `net_dex` | **+13,687,592,341,278** |
| Interpretation | Public net call-long → dealer hedge = BUY underlying |

The number is dollar-delta. Dealers are short calls and need to be
long stock to hedge — that's the mechanical bid under spot. Sign and
magnitude consistent with phase-2's 0.794 mega-tier DP buy ratio.

### Vanna + charm

| Field | Value |
|-------|-------|
| `call_vanna` | −50,363,478 |
| `put_vanna` | +2,130,320 |
| `net_vanna` | **−48,233,158** |
| `net_charm` | **+4,327,640,413** |

**Mechanism (call-heavy book):** Vanna negative + charm positive means
that as the calendar advances and IV decays, dealer call hedges
(long-stock positions) become less needed → dealers **sell** underlying.
That's a gentle de-hedge bleed in low-vol drift days, partially
offsetting the long-gamma bid.

**Vanna squeeze setup?** Yes, but in reverse direction: a sudden IV
**rise** would force dealers to **buy** more stock (positive feedback
loop on the way up). Today's IV is low (28-day 26.9%) and skew is
complacent — a small spike could ignite that loop.

### IV term structure

Structure: **CONTANGO** (back > front) [STRUCT:iv_term_structure].

| Expiry | DTE | Avg IV |
|--------|-----|--------|
| 5/20 | 0 | 3.1% (expiration artifact) |
| **5/22** | **2** | **30.3%** (pin volatility) |
| 5/27 | 7 | 23.2% |
| 5/29 | 9 | 24.3% |
| 6/18 | 29 | 26.9% |
| 7/17 | 58 | 26.5% |
| 8/21 | 92 | 28.7% |
| 9/18 | 121 | 27.8% |
| 1/15/27 | 240 | 27.3% |
| **2/19/27** | **275** | **30.7%** (small kink — earnings?) |
| 1/21/28 | 612 | 29.1% (LEAP buyer's expiry) |

No earnings-binary kink in the front (no `kink_expiry` flagged).
5/22's 30.3% is elevated because of how IV is averaged across deep
OTM strikes near 0DTE — not a clean signal. The structure normalizes
cleanly above 5/27 — **AAPL has no acute event risk priced in for
the next ~9 days.**

### Term skew (30-DTE)

| Field | Value |
|-------|-------|
| `call_25d_iv` | 23.85% |
| `put_25d_iv` | 24.10% |
| `skew` | +0.0025 |
| `skew_ratio` | 1.01 |
| **interpretation** | **COMPLACENT** |

Puts are barely richer than calls — **no fear bid** in the 30-DTE
window. Cheap protection if you want hedges; risky as a contrarian
signal if you're already long (no margin for surprise).

### Front-end IV ratio (7/30)

| Field | Value |
|-------|-------|
| `near_iv` (7d) | 23.23% |
| `far_iv` (29d) | 26.93% |
| `ratio` | 0.863 |
| **regime** | **CONTANGO** |

Confirms term-structure read: no near-term stress. Normal
upward-sloping IV curve.

### Today gamma flip (0DTE walls)

| Strike | GEX | Role |
|--------|-----|------|
| **302.5** | **+1,383,658,924,735** | support_wall (largest) |
| 300 | +873,559,497,800 | support_wall |
| 305 | +188,738,601,892 | support_wall |
| 307.5 | +4,773,848,711 | support_wall (small) |
| 295 | −8,263,664,041 | "resistance_wall" — gamma flip trapdoor below |
| **0DTE ZGL** | **$287.86** | Net gamma = 0 line for today's expiry |

The 0DTE `regime` is POSITIVE, spot $300.52 sits **comfortably inside
the long-gamma corridor** ($300–$305) with a $1.38T support cushion at
$302.5. The trapdoor is at $295, which would require a 1.7% intraday
drop to hit.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__options_structure_gex` | `{symbol: AAPL, dte-max: 45, date: 2026-05-20}` | regime POSITIVE; total GEX $648.7B; ZGL $95.52 (artifact) |
| `mcp__uw-pp__options_structure_dex` | `{symbol: AAPL, dte-max: 45, date: 2026-05-20}` | net DEX +$13.69T (public call-long) |
| `mcp__uw-pp__options_structure_vanna_charm` | `{symbol: AAPL, dte-max: 45, date: 2026-05-20}` | vanna −48.2M, charm +4.33B |
| `mcp__uw-pp__options_structure_iv_term_structure` | `{symbol: AAPL, date: 2026-05-20}` | CONTANGO, no kink |
| `mcp__uw-pp__options_structure_term_skew` | `{symbol: AAPL, dte-target: 30, date: 2026-05-20}` | COMPLACENT, skew 1.01 |
| `mcp__uw-pp__options_structure_front_end_iv_ratio` | `{symbol: AAPL, near-dte: 7, far-dte: 30, date: 2026-05-20}` | CONTANGO, 0.863 |
| `mcp__uw-pp__options_structure_today_gamma_flip` | `{symbol: AAPL, date: 2026-05-20}` | 0DTE ZGL $287.86, $302.5 +$1.38T support |

## Tool errors

None. The 45-DTE ZGL of $95.52 is flagged as a computational
artifact, not a tool error.

## Verdict for downstream phases

- **Dealer regime:** **POSITIVE / long-gamma** above $295, transitioning
  to short-gamma below $287.86 (0DTE) / $295 (week-level).
- **Conviction:** 5 / 5. Multi-tool confluence: GEX positive +
  $13.69T DEX + walls + complacent skew all agree.
- **Three structural levels for phase-9:**
  1. **$302.5 / $300 — mega support walls + DP clearing zone.** Buy-
     the-dip cushion is here; any structured long should enter on
     pullbacks toward $300.
  2. **$295 — gamma flip trapdoor.** Hard stop on any directional long.
     Below $295 dealer flow reverses to selling.
  3. **$287.86 — 0DTE ZGL.** True regime switch level. A daily close
     below $287.86 invalidates the long-gamma mean-reversion thesis
     and turns AAPL into a trending/short-gamma name.
- **Open questions:**
  - Will the IV-low + complacent-skew combination persist? Phase 5
    historical IV percentile and VRP will resolve whether 27% 30-day
    IV is genuinely cheap (long vol) or middle-of-range (short vol).
  - Does the LEAP buyer's package (phase-1, $51.6M ask-side 2028 300C)
    add meaningfully to dealer short-call exposure tomorrow? Will pull
    GEX again on 2026-05-21 if running multi-day.
  - The 2/19/27 expiry has 30.7% IV — small kink suggesting potential
    catalyst around that window (Feb earnings?). Phase 6 macro should
    check AAPL's Q1 26 earnings date.
