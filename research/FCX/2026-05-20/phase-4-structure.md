# Phase 4 — Dealer Structure & Gamma

**Ticker:** FCX
**As-of date:** 2026-05-20 (effective data 2026-05-19)
**Generated:** 2026-05-20T20:10:00-04:00
**Upstream phases cited:** `phase-0-intake.md`, `phase-1-flow.md`,
`phase-2-dark-pool.md`, `phase-3-positioning.md`

## Summary

This is the **decisive phase** for the FCX setup. The dealer-positioning
picture is unusually crisp and **resolves the phase-1 vs phase-3 contradiction
in favour of an asymmetric upside-skewed thesis**.

Spot $58.95 trades **BELOW the Zero Gamma Level $64.09** [STRUCT:gex] →
dealers are net SHORT GAMMA at current spot. Net GEX (45-DTE) sums to a
nominally positive +$2.22B, but that aggregate is dominated by the **$1.44B
of long gamma stacked at the 65 strike** [STRUCT:gex]. From $55 to $58
dealers carry $545M of *negative* GEX (the 55 strike alone is −$458M);
from $59 to $65 the picture flips and dealers are long $1.94B of gamma. The
implication: **moves UP toward $60–65 are mechanically braked** (dealers sell
rallies into long-gamma strikes — gravity well at $65); **moves DOWN through
$58 → $55 are mechanically amplified** (dealers sell into weakness — cascade
risk).

The IV term structure is in **clear backwardation** (front 9-DTE 64.2% vs
back 29-DTE 52.5%, ratio 1.22) [STRUCT:front_end_iv_ratio] — markets are
pricing an event-stress within the next 9 trading days. The 30-DTE 25Δ term
skew is **COMPLACENT** (call IV 52.3% > put IV 50.5%, skew −0.018)
[STRUCT:term_skew] — downside tail is underpriced, which is the inverse of
normal market psychology and consistent with the call-heavy DEX book.

DEX is +$16.8B net (call_dex +$27.9B vs put_dex −$11.1B) [STRUCT:dex] — the
public is heavily call-long, dealers are net short calls, **dealer hedge =
BUY underlying**. That's a structural bid. Vanna (−$460k net public) and
charm (+$14.4M net) [STRUCT:vanna_charm] add a second-order wrinkle: if
front-end IV mean-reverts down (likely once the May-29 catalyst passes),
dealers will need to *sell* some of that long-underlying hedge → modest
near-term overhead.

**Net dealer-structure read: bullish skew within a $58 floor / $65 magnet
band, with cascade risk if $55 breaks.** Conviction **4/5**.

## Key signals

- **Spot $58.95 < ZGL $64.09 → dealers SHORT GAMMA at spot** → trend-
  amplification regime [STRUCT:gex].
- **$65 strike net_gex = +$1,437.7M** — single largest dealer-long-gamma
  node anywhere in the chain. This **IS** the magnet/ceiling
  [STRUCT:gex].
- **$55 strike net_gex = −$458.2M** — the dominant short-gamma node below
  spot; below $55 dealers force-sell the cascade [STRUCT:gex].
- **DEX +$16.8B, dealers net short calls → BUY underlying as hedge**
  [STRUCT:dex] — structural bid corroborates phase-2 dark-pool +$11M
  accumulation.
- **Front-end IV backwardation 1.22 (9-DTE 64.2% vs 29-DTE 52.5%)**
  [STRUCT:front_end_iv_ratio] — event-stress flag inside 9 trading days;
  phase 6 must find the catalyst.
- **30-DTE skew: COMPLACENT** (call_25d 52.3% > put_25d 50.5%)
  [STRUCT:term_skew] — downside tail underpriced.
- **0DTE / May-22 weekly walls:** support at **$60** (+$80.5M GEX),
  resistance at **$58** (−$36M GEX) [STRUCT:today_gamma_flip] — short-term
  pin-toward-$60 dynamic into Friday.

## Detailed findings

### GEX — per-strike map (45-DTE) [STRUCT:gex]

| Strike | Net GEX ($) | Role | vs spot $58.95 |
|--------|-------------|------|----------------|
| 35 | −195,704 | minor short γ | −41% |
| 40 | −313,675 | minor short γ | −32% |
| **45** | **−8,871,179** | short γ shelf | −24% |
| 47 | −1,481,357 | minor | −20% |
| **50** | **−113,724,931** | major short γ wall | −15% |
| 51 | −688,687 | minor | −13% |
| 52 | +11,604,545 | small long γ | −12% |
| 53 | +14,661,258 | small long γ | −10% |
| 54 | −657,901 | flat | −8% |
| **55** | **−458,228,523** | **DOMINANT SHORT-GAMMA NODE** | **−7%** |
| 56 | −18,764,297 | short γ | −5% |
| 57 | −30,276,514 | short γ | −3% |
| 58 | −37,274,366 | short γ | −2% |
| **59** | **+166,852,156** | **GAMMA FLIP — first positive strike** | **+0.1%** |
| 60 | +299,166,129 | long γ wall | +2% |
| 61 | +5,484,844 | minor | +3% |
| 62 | +6,991,403 | minor | +5% |
| 63 | +9,052,533 | minor | +7% |
| 64 | +25,597,838 | long γ | +9% |
| **65** | **+1,437,659,056** | **DOMINANT LONG-GAMMA NODE — MAGNET** | **+10%** |
| 66 | +19,983,351 | long γ | +12% |
| 67 | +83,516,610 | long γ | +14% |
| 68 | +1,351,327 | minor | +15% |
| 70 | **+694,622,902** | secondary magnet | +19% |
| 75 | +106,344,850 | long γ ceiling | +27% |

**Totals:** net_gex +$2.22B, ZGL $64.09, regime label "NEGATIVE at spot".

**Reading the map:** there is a binary regime change between $58 and $59.
- Below $58: spot in short-gamma territory; dealer hedging amplifies moves.
- $59–$65: spot enters dealer long-gamma; rallies *into* this zone get
  faded, but the $65 node is so large it ALSO acts as a **gravitational
  pull** when spot trades within ~5% of it.
- $65+: extremely large long-gamma ceiling. Above $65, dealer selling is
  aggressive; a clean break of $65 against this much OI would be a
  significant institutional event.

### DEX — net dealer delta [STRUCT:dex]

| Component | Value | Read |
|-----------|-------|------|
| call_dex | +$27.86B | Public heavily long calls |
| put_dex | −$11.07B | Modest put length |
| **net_dex** | **+$16.80B** | Strongly call-heavy book |
| spot | $58.94 | reference |

**Interpretation:** "Public is net call-long → dealers net short calls →
dealer hedge is to BUY underlying." This is a **structural source of
demand for FCX equity from dealer rebalancing** — consistent with the
phase-2 dark-pool net accumulation of $11M.

### Vanna & charm [STRUCT:vanna_charm]

| Component | Value |
|-----------|-------|
| call_vanna | −$796,814 |
| put_vanna | +$337,226 |
| **net_vanna** | **−$459,588** |
| **net_charm** | **+$14,369,600** |

**Tool note (cited verbatim):** "Public net vanna negative (call-heavy
book). Falling IV → call delta drops → dealers (short calls) cut long-
underlying hedge → SELLING pressure. Rising IV reverses."

Charm interpretation: positive +$14.4M with call-heavy book → as time
passes, call deltas decay → dealers reduce long-underlying hedge → **modest
bearish drift over time** (a few cents per day, not directionally
decisive).

### IV term structure [STRUCT:iv_term_structure]

Regime: **BACKWARDATION**. No kink expiry detected. 15 expiries:

| Expiry | DTE | Avg IV | Read |
|--------|-----|--------|------|
| 2026-05-22 | 3 | **72.6%** | Weekly noise + real event premium |
| 2026-05-29 | 10 | **64.2%** | Front-end stress — pre-catalyst |
| 2026-06-05 | 17 | 55.8% | Normalising |
| 2026-06-12 | 24 | 54.4% | |
| 2026-06-18 | 30 | 52.5% | Standard monthly anchor |
| 2026-06-26 | 38 | 51.2% | |
| 2026-07-17 | 59 | 51.5% | Slight bulge (Jul earnings adjacent?) |
| 2026-08-21 | 94 | 51.3% | |
| 2026-09-18 | 122 | 51.8% | |
| 2026-11-20 | 213 | 51.1% | |
| 2026-12-18 | 241 | 51.1% | |
| 2027-01-15 | 270 | 51.8% | |
| 2027-03-19 | 333 | 50.8% | |
| 2027-06-17 | 423 | 49.8% | Lowest IV — true "fair vol" |
| 2028-01-21 | 611 | 51.2% | LEAP convergence |

The May-22 → May-29 → Jun-5 cliff (72.6 → 64.2 → 55.8%) tells us the
market prices a **specific event-stress window between today and ~Jun-5**.
Beyond that, IV settles into ~51% across all maturities — that is the
**true "FCX fair vol"** in this regime, and ~50% IV in LEAPs (vs ~35–40%
typical for large-cap miners) signals an elevated medium-term vol regime
(verify in phase 5 historical_iv_percentile_zscore).

### Term skew (25Δ, 30 DTE) [STRUCT:term_skew]

- call_25d_iv: 52.3%
- put_25d_iv: 50.5%
- **skew: −0.018**  (calls richer than puts)
- skew_ratio: 0.966
- **Label: COMPLACENT**

This is an **inverted skew** — calls trade richer than puts. Normal equity
behaviour is the opposite (puts richer, "smile" tilted left). FCX's
inverted skew reflects:
1. Genuine upside-call demand (consistent with the bullish call sweeps in
   phase-1 and the new 59C OI build in phase-3).
2. Insufficient downside-hedge demand at 25Δ.

**Contrarian interpretation:** if the bullish call positioning is wrong-
footed, the cheap puts will explode in IV on a downside move. **Vega is
asymmetric in our favour for a long-volatility / protective-put leg.**

### Front-end IV ratio [STRUCT:front_end_iv_ratio]

- near_iv (9 DTE): 64.2%
- far_iv (29 DTE): 52.5%
- **ratio: 1.223** → **BACKWARDATION** (threshold > 1.05)

Single-number confirmation of the term-structure cliff. Phase 6 should
identify the catalyst inside 9 trading days.

### Today's gamma flip (0DTE chain, May-22 weekly) [STRUCT:today_gamma_flip]

- spot: $58.94
- today_zero_gamma: $40.15 (computed from limited 0DTE OI; coarse)
- atm_flip_strike: 45
- today_total_gex: +$96.2M
- regime: POSITIVE (for the May-22 weekly chain only)

| Strike | GEX | Role |
|--------|-----|------|
| **60** | **+$80,518,410** | **support wall** — primary pin candidate |
| 65 | +$36,249,757 | upside support / magnet |
| 64 | +$26,610,379 | support |
| **58** | **−$35,950,527** | **resistance wall** |
| 57 | −$24,825,628 | resistance |

**Read for next 2 sessions (May-20 + May-21 → May-22 close):**
- $60 is the pin candidate for Friday weekly OPEX.
- $57–$58 acts as upside resistance from the gamma map.
- The 0DTE chain's positive regime (vs 45-DTE negative) means **for the
  weekly only**, dealers will fade extreme moves and pin toward $60.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `options_structure_gex` | symbol=FCX, dte_max=45, date=2026-05-19 | ZGL $64.09, total +$2.22B, regime "NEGATIVE at spot" |
| `options_structure_dex` | symbol=FCX, dte_max=45 | net_dex +$16.8B; dealer hedge = BUY underlying |
| `options_structure_vanna_charm` | symbol=FCX, dte_max=45 | vanna −$460k, charm +$14.4M |
| `options_structure_iv_term_structure` | symbol=FCX | BACKWARDATION, 15 expiries, no kink |
| `options_structure_term_skew` | symbol=FCX, dte_target=30 | COMPLACENT, skew −0.018 |
| `options_structure_front_end_iv_ratio` | symbol=FCX, near=7, far=30 | BACKWARDATION ratio 1.223 |
| `options_structure_today_gamma_flip` | symbol=FCX | $60 support, $58 resistance, today GEX +$96M |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** **bullish skew, mean-reverting toward the $65
  magnet**, conditional on holding the $55 floor. Asymmetric: upside is
  braked but pulled by gamma; downside is cascade-amplified.
- **Conviction:** **4/5** — the structural map is crisp and corroborates
  phase-2 (institutional levels at $65) and phase-3 (59C build = magnet
  reinforcement at strike).
- **Three structural levels for phase-9:**
  1. **$64.09 — Zero Gamma Level.** Above this, dealer hedging flips
     supportive; below, it's amplifying-down. **The primary line in the
     sand for a bull thesis.**
  2. **$65.00 — Dominant long-gamma node (+$1.44B GEX) AND $191M dark-
     pool concentration.** The natural target / magnet for any
     constructive scenario.
  3. **$55.00 — Dominant short-gamma node (−$458M GEX).** The cascade
     trigger. A breach of $55 forces dealer-selling acceleration and
     invalidates a long thesis.
- **Tactical level for the next 48 hours:** $60 weekly pin (May-22 OPEX);
  $57.50–$58 upside resistance from the 0DTE map.
- **Open questions:**
  - What specifically is driving the May-29 9-DTE backwardation? Earnings
    is unlikely (FCX usually reports late Apr/late Jul); **phase 6 must
    investigate** (FOMC date, copper-specific data, China data,
    contract/Indonesia mining news).
  - Is 50% LEAP IV historically elevated, in-line, or cheap for FCX?
    Phase-5 `historical_iv_percentile_zscore` decides whether the long-
    vol leg is attractive or expensive.
  - If the catalyst clears benignly, IV will mean-revert; that triggers
    dealer-vanna SELLING. Need to size around that, not despite it.
