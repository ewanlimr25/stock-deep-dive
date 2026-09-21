# Phase 3 — Open Interest & Positioning

**Ticker:** FSLR
**As-of date:** 2026-05-18 (data anchor: 2026-05-15)
**Generated:** 2026-05-18T00:25:00Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md

## Summary

The OI delta snapshot for 2026-05-15 is structurally muted because **2026-05-15
is May OPEX**: today's same-day opening trades (e.g. the Mar-2027 280C
480-lot ASK print from phase-1) will appear as OI increases in the *next*
snapshot, while today's deltas are dominated by May-15 0DTE closing of
small-OI strikes. As a result, `oi_biggest_increases` returned **empty** at
the 500-contract threshold and `oi_smart_positioning` returned **empty**.
`oi_position_rolls` detected **0 rolls** at threshold 500. FSLR is **not**
on the market-wide pin-risk board for the May OPEX cycle, nor in the
opex_concentration list — chain is dispersed across expiries. The only
substantive standing position uncovered in the decrease scan is a
**Jan-2027 $380 call with 9,037 contracts of OI ($10.56 avg price ≈ $9.5M of
prior call premium)** — pre-existing institutional bullish bet on FSLR back
to $380 by Jan 2027. Net read: **inconclusive from delta data alone, but
existing positioning leans bullish-leverage to upside via deep-OTM LEAPs**,
conviction 2/5.

## Key signals

- `oi_biggest_increases` (symbol=FSLR, min-oi-change=500): **0 rows** —
  today's new positions (from phase-1 sweeps) have not yet rolled into the
  OI snapshot because 2026-05-15 is OPEX day; expect Mar-2027 280C,
  May-22 230P, May-29 220P, Jun-18 250C to appear in tomorrow's data
  [OI:oi_biggest_increases].
- `oi_decrease_with_volume`: 8 small decreases, all near-zero relative to
  chain size. Top: 240C May-15 −60 OI on 399 vol (0DTE close); 240C Jun-18
  −53 OI on 101 vol; **380C Jan-2027 −30 OI on 102 vol (avg price $10.56,
  curr_oi = 9,037)** [OI:oi_decrease_with_volume].
- `oi_smart_positioning`: **0 rows** at min-oi-change=500 (same OPEX-day
  cause as above) [OI:oi_smart_positioning].
- `oi_position_rolls` (near_dte_max=21, threshold=500): **rolls_detected=0**
  — no detectable institutional rolls today [OI:oi_position_rolls].
- `oi_pin_risk` (dte_max=7, max_distance_pct=5): FSLR **not present** in top
  25; OPEX-week pin board is dominated by HYG@79, SPY@710, QQQ@700, TLT@86,
  IWM@270, XLF@51. FSLR-specific pin risk is not a tradeable factor this
  week [OI:oi_pin_risk].
- `oi_opex_concentration` (min-concentration-pct=40): FSLR **not present** —
  no single expiry holds ≥40% of FSLR's total OI; chain is dispersed,
  consistent with a liquid actively-traded large-cap [OI:oi_opex_concentration].

## Detailed findings

### Largest OI increases

**Empty result.** With min-oi-change=500 and date=2026-05-15, no FSLR
contracts showed a ≥500-contract OI build. This is materially explained by:

1. **OPEX day timing.** OI snapshots update from prior close to today's
   close; same-day fresh opens are not yet "OI" in the conventional sense.
   Tomorrow's (2026-05-18) snapshot will show:
   - 2027-03-19 280C OI Δ ≈ **+480** (from phase-1 unusual vol; prior OI=48)
   - 2026-05-22 230P OI Δ ≈ multi-hundred
   - 2026-05-29 220P OI Δ ≈ **+1,500-ish** (from phase-1 vol 1,513)
   - 2026-06-18 250C OI Δ TBD (was already a $1.6M ASK + $1.6M BID
     two-sided print so net Δ may be modest).

2. **No legacy directional builds today.** Beyond the same-day-print
   limitation, no other FSLR strike had a clean ≥500 contract OI build,
   suggesting positioning activity is concentrated in the new options-flow
   tape rather than slow-burn accumulation in standing OI.

### Closing / roll activity

`oi_decrease_with_volume` (min-volume=100):

| Strike | Type | Expiry | DTE | OI Δ | Curr OI | Vol | Avg px | Read |
|--------|------|--------|-----|------|---------|-----|--------|------|
| 240 | C | 2026-05-15 | 0 | −60 | 2,586 | 399 | $1.14 | 0DTE expiry-day churn |
| 240 | C | 2026-06-18 | 34 | −53 | 3,845 | 101 | $12.87 | Minor close of Jun call |
| 245 | C | 2026-05-15 | 0 | −43 | 132 | 149 | $0.44 | 0DTE small unwind |
| 380 | C | 2027-01-15 | 245 | −30 | **9,037** | 102 | **$10.56** | **Trim of large Jan-27 LEAP position** |
| 230 | C | 2026-05-15 | 0 | −10 | 1,231 | 108 | $3.40 | 0DTE ITM close |
| 370 | C | 2027-01-15 | 245 | −7 | 99 | 104 | $11.54 | Minor sibling LEAP trim |
| 215 | P | 2026-05-15 | 0 | −4 | 352 | 102 | $0.15 | 0DTE put close |
| 217.5 | P | 2026-05-15 | 0 | −3 | 357 | 106 | $0.42 | 0DTE put close |

**The standing institutional bullish bet** worth flagging is the
**Jan-2027 $380 call** — current OI **9,037 contracts** at $10.56 avg
implies ~**$9.5M of LEAP premium** stacked at a strike 60% above spot. The
−30 OI decrease today is a rounding-error trim, not distribution. This is
strong evidence that institutions had ALREADY been bullish on FSLR back to
$380+ by Jan 2027 before today's tape.

No `oi_position_rolls` were detected; the data does not show a near→far
roll signature today.

### Smart positioning

`oi_smart_positioning` (min-oi-change=500): **empty**. Same OPEX-day cause
as the increases tool. Cannot infer direction from this tool's output today.

### Pin risk (OPEX week)

FSLR **not present** in the top-25 pin-risk list for the 2026-05-15 OPEX.
Market-wide top pins are index/macro-tier names:

| Ticker | Spot | Pin strike | Pin distance | Pin score |
|--------|------|------------|--------------|-----------|
| HYG | 79.50 | 79 | 0.62% | 2,362,988 |
| SPY | 739.11 | 710 | 3.94% | 1,901,451 |
| QQQ | 708.86 | 700 | 1.25% | 1,090,776 |
| TLT | 83.64 | 86 | 2.83% | 1,043,379 |
| IWM | 277.57 | 270 | 2.73% | 1,032,448 |
| XLF | 51.11 | 51 | 0.21% | 825,279 |

Implication for FSLR: today's intraday tape (rallying to $236.5) is
**not** being shaped by 2026-05-15 OPEX pin gravity. The price discovery
on 2026-05-15 was driven by **flow and dark-pool absorption** rather than
gamma pinning — that is a clean signal.

### OPEX concentration

FSLR **not in the top-30 opex_concentration list** at min-concentration-pct=40.
The list is dominated by micro-caps and biotech (SKYE, EHTH, DLNG, CURB,
DOUG, IART, CATO, etc.) whose OI clusters in a single expiry — a sign of
event-driven retail-style positioning. FSLR's dispersed expiry structure
is consistent with a liquid mid/large-cap with active options market
makers rolling positions across the chain — no single OPEX cliff risk.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__oi_biggest_increases` | `{symbol: FSLR, top-n: 25, min-oi-change: 500, date: 2026-05-15}` | **Empty** (OPEX-day artifact) |
| `mcp__uw-pp__oi_decrease_with_volume` | `{symbol: FSLR, top-n: 20, min-volume: 100, date: 2026-05-15}` | 8 rows, all small; largest standing OI = 380C Jan-27 = 9,037 |
| `mcp__uw-pp__oi_smart_positioning` | `{symbol: FSLR, top-n: 25, min-oi-change: 500, date: 2026-05-15}` | **Empty** (same cause) |
| `mcp__uw-pp__oi_position_rolls` | `{symbol: FSLR, threshold: 500, near-dte-max: 21, date: 2026-05-15}` | rolls_detected=0 |
| `mcp__uw-pp__oi_pin_risk` | `{top-n: 25, dte-max: 7, max-distance-pct: 5, date: 2026-05-15}` | FSLR not in top 25 |
| `mcp__uw-pp__oi_opex_concentration` | `{top-n: 30, min-concentration-pct: 40, date: 2026-05-15}` | FSLR not in top 30 |

## Tool errors

None. Empty result sets are valid data — they signal the absence of
qualifying activity, attributed to the May-OPEX timing.

## Verdict for downstream phases

- **Bias from this phase:** **inconclusive on delta data; mildly bullish on
  standing positioning.** The pre-existing Jan-2027 $380C 9,037-contract
  OI base is a sizeable structural call leverage to upside that has not
  been distributed.
- **Conviction:** 2/5. Most tools returned empty due to OPEX timing — the
  signal here is the *absence* of distribution + the size of the existing
  LEAP base, both weak-form bullish.
- **Three pin/cliff strikes for phase-9 reference:**
  1. **$380 (Jan-2027)** — psychological/leverage anchor for the standing
     bullish OI base; relevant for upside target framing, not entry/stop.
  2. **$240 / $250 (May-22 / Jun-18 calls)** — densest near-term call
     strike clusters with persistent activity (240C Jun-18 OI=3,845;
     240C May-15 OI=2,586). $240 is the **first call-wall** above spot
     for short-term resistance.
  3. **$220–230 puts (May-22, May-29)** — fresh hedge layer being built in
     phase-1; these strikes become the **realistic worst-case retracement
     anchors** for a 1–3 week horizon.
- **Open questions for downstream:**
  - Tomorrow's OI snapshot is needed to confirm the Mar-2027 280C
    480-contract opening rolls into +480 OI; phase-7 insights tools may
    capture this if they run on intraday data.
  - Is the standing $380 LEAP held by one or many accounts? Out of scope;
    not knowable from OPRA alone.
  - Where is dealer gamma vs $240 (call wall) and $230 (put wall)?
    (→ phase-4 structure)
