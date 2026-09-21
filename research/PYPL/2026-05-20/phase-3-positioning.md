# Phase 3 — Open Interest & Positioning

**Ticker:** PYPL
**As-of date:** 2026-05-19
**Generated:** 2026-05-20T00:25:00-04:00
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md

## Summary

OI positioning resolves phase 1's mixed signal: the dominant theme is
**call overwriting / premium-capture programs against the institutional
inventory we identified in phase 2**. Six of the seven largest OI builds in
calls are SOLD-to-bid (overwriters capping upside at $50, $52, $55 Jun-18 and
$75 LEAP). Put-selling dominates the OTM ($38–$40) buckets — bullish income.
The two unambiguous bearish OI builds are the **+1,831 contract Jul-17 $35P
ask-bought tail hedge** and the **+868 contract 3DTE 5/22 $44.5P ask-bought**
short-term hedge. **No pin risk and no OPEX concentration for PYPL** — the
chain is dispersed across expiries, so phase 4 dealer positioning will be
driven by gamma at the $50/$55 ceiling, not by an OPEX cliff. Net read:
mildly bullish (covered-call + put-write pattern = "own the stock, harvest
premium") with **clear upside cap near $50 for Jun expiry**.

## Key signals

- **PYPL 2026-06-18 $50C OI +1,352 → 23,713, prev bid_vol 2,287 vs ask 725
  (3.2:1 bid)** [OI:oi_biggest_increases / oi_smart_positioning] — largest
  OI add of the day is a CALL being SOLD = upside cap at $50 in 30 DTE.
- **PYPL 2026-07-17 $35P OI +1,831 → 6,923, prev ask_vol 2,347 vs bid 47
  (50:1 ask)** [OI:oi_smart_positioning] — biggest put OI build is BOUGHT
  far-OTM, classic tail hedge or strong directional bear bet.
- **Put-selling across $38–$40 OTM strikes (2,500 + 1,183 + 591 OI added
  net bid-side)** [OI:oi_biggest_increases:2026-05-19] — institutional
  premium harvesting consistent with the phase-2 accumulation thesis.
- **PYPL 2027-01-15 $75C OI +1,549 SOLD to bid** [OI:oi_biggest_increases] —
  LEAP call overwriting cap at $75; lengthens the program from phase 1's
  Dec-2028 $50C overwriter print.
- **No PYPL entry in `oi_pin_risk` top 50 (despite 3 DTE to 5/22 weekly
  OPEX)** [OI:oi_pin_risk] — OI not concentrated enough near spot for a
  mechanical pin; price action this week is *not* expected to be magnet-
  driven.
- **No PYPL entry in `oi_opex_concentration` top 100 (≥30% threshold)**
  [OI:oi_opex_concentration] — the chain is dispersed across expiries; no
  single-expiry cliff risk.
- **No same-day position rolls detected** [OI:oi_position_rolls] — today's
  flow is genuine new positioning, not roll-out activity.

## Detailed findings

### Largest OI increases — top 16

(`stock_price` field = $43.83 in all rows; this is the EOD reference used by
the OI service. Phase 2 spot of $43.88 is the late-session median. Use
$43.83 as the OI-anchor and $43.88 as the working spot.)

| Strike | Expiry | DTE | Type | OI Δ | Curr OI | Prev ask/bid | Inferred direction | Read |
|--------|--------|-----|------|------|---------|--------------|---------------------|------|
| 39   | 2026-05-29 | 10 | P | +2,500 | 2,506 | 505 / 1,681 | **bullish** | Put-sell premium harvest 11% OTM |
| 35   | 2026-07-17 | 59 | P | +1,831 | 6,923 | 2,347 / 47   | **bearish** | Tail-hedge put accumulation 20% OTM |
| 52   | 2026-06-05 | 17 | C | +1,551 | 1,748 | 1 / 1,554    | **bearish** (overwrite) | Call-overwrite 17DTE $52 cap |
| 75   | 2027-01-15 | 241 | C | +1,549 | 8,024 | 26 / 141     | **bearish** (overwrite) | LEAP $75 overwrite |
| **50**   | **2026-06-18** | **30** | **C** | **+1,352** | **23,713** | **725 / 2,287**  | **bearish** (overwrite) | **Jun $50 overwrite — KEY CAP** |
| 47   | 2026-05-22 | 3  | C | +1,337 | 6,476 | 1,182 / 1,283| mixed (slight bear) | 3DTE $47C, near-balanced |
| 38   | 2026-06-05 | 17 | P | +1,183 | 1,221 | 13 / 995     | bullish (put-sell) | Put-write 17DTE 13% OTM |
| 62.5 | 2026-07-17 | 59 | C | +992   | 1,832 | 1,001 / 40   | **bullish** | Jul $62.5C bought 42% OTM — speculative |
| 45   | 2026-05-22 | 3  | C | +932   | 1,628 | 858 / 550    | bullish | 3DTE $45C ATM bought |
| 44.5 | 2026-05-22 | 3  | P | +868   | 1,766 | 943 / 89     | **bearish** | 3DTE $44.5P ATM bought — strong short-term hedge |
| 55   | 2026-06-18 | 30 | C | +817   | 14,009 | 192 / 1,193  | bearish (overwrite) | Jun $55 overwrite |
| 45   | 2026-05-29 | 10 | C | +669   | 1,245 | 584 / 400    | bullish | 10DTE $45C ATM bought |
| 46   | 2026-05-22 | 3  | C | +667   | 6,455 | 671 / 588    | bullish | 3DTE $46C OTM bought |
| 40   | 2026-06-26 | 38 | P | +591   | 1,995 | 57 / 542     | bullish (put-sell) | Put-write 38DTE 9% OTM |
| 47.5 | 2026-09-18 | 122 | C | +590  | 5,396 | 747 / 20     | bullish | Sep $47.5C bought 8% OTM |
| 55   | 2026-07-17 | 59 | C | +544   | 5,229 | 63 / 752     | bearish (overwrite) | Jul $55 overwrite |

[OI:oi_biggest_increases:2026-05-19, OI:oi_smart_positioning:2026-05-19].

### Buckets by intent (sum of OI added)

| Bucket | Total OI added | Constituents |
|--------|----------------|--------------|
| Call overwriting (sold to bid) — **capping upside** | +6,150 | Jun-18 $50C, $55C; Jul-17 $55C; Jun-5 $52C; Jan-27 $75C |
| Put selling (sold to bid) — **bullish income** | +4,274 | May-29 $39P; Jun-5 $38P; Jun-26 $40P |
| Long calls bought (ask) — **bullish speculation** | +3,118 | May-22 $45C/$46C; May-29 $45C; Jul-17 $62.5C; Sep-18 $47.5C |
| Long puts bought (ask) — **bearish/hedge** | +2,699 | Jul-17 $35P (tail); May-22 $44.5P (ATM 3DTE) |

Net flow read:
- Bullish positioning (put-sell + long calls): **+7,392 OI**
- Bearish/cap positioning (call-overwrite + long puts): **+8,849 OI**

These are roughly balanced in raw OI count, but **the bearish/cap bucket is
dominated by overwriters (+6,150) — institutions willing to be called away
at $50–$75**. That's *neutral-to-bullish behavior* if you already own the
underlying (income harvest on a held position) but mechanically caps upside
in the underlying via positive dealer gamma above those strikes. The
long-put bucket (+2,699) is real but only the $44.5P short-dated leg is
high-conviction directional bearish.

### Closing / roll activity

Decreases are immaterial (largest: 2027-01-15 $135C −255 contracts, far
OTM far-DTE noise). [OI:oi_decrease_with_volume:2026-05-19].

`oi_position_rolls(threshold=500, near_dte_max=30)` returned **0 rolls
detected** [OI:oi_position_rolls:2026-05-19]. Today's flow is fresh
positioning, not a roll-out of expiring contracts. Confirms the new-
positions narrative.

### Pin risk

PYPL is NOT in `oi_pin_risk` top 50 with `dte_max=7, max_distance_pct=5`,
even though 5/22 weekly OPEX is 3 DTE away [OI:oi_pin_risk:2026-05-19].
The top market-wide pins on this date are: SPY @ $710 (3.2% from spot $733.44),
HYG @ $78, QQQ @ $680, IWM @ $270, TLT @ $86. PYPL's near-week OI is too
dispersed across $44–$48 strikes to create a magnet.

**Implication:** there is no mechanical pin pressure into Friday 5/22 from
PYPL's own OI structure. Price will move on flow + spy/sector beta, not on
gamma-induced pinning.

### OPEX concentration

PYPL is NOT in `oi_opex_concentration` top 100 at 30% threshold
[OI:oi_opex_concentration:2026-05-19]. The chain is dispersed across many
expiries (Jun-5, Jun-12, Jun-18, Jun-26, Jul-17, Sep-18, Jan-27, Jan-28,
Dec-28 all show meaningful OI). No single-expiry cliff risk on either
direction.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__oi_biggest_increases` | symbol=PYPL, top-n=25, min-oi-change=500, date=2026-05-19 | 16 contracts ≥500 OI added |
| `mcp__uw-pp__oi_decrease_with_volume` | symbol=PYPL, top-n=20, min-volume=100, date=2026-05-19 | 9 minor decreases, all <300 contracts |
| `mcp__uw-pp__oi_smart_positioning` | symbol=PYPL, top-n=25, min-oi-change=500, date=2026-05-19 | 16 entries with inferred direction |
| `mcp__uw-pp__oi_position_rolls` | symbol=PYPL, threshold=500, near-dte-max=30, date=2026-05-19 | 0 rolls detected |
| `mcp__uw-pp__oi_pin_risk` | top-n=50, dte-max=7, max-distance-pct=5, date=2026-05-19 | PYPL not in top 50 |
| `mcp__uw-pp__oi_opex_concentration` | top-n=100, min-concentration-pct=30, date=2026-05-19 | PYPL not in top 100 |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** **mildly bullish via accumulation-with-yield
  pattern, with explicit upside cap at $50 Jun-18 and a tail-hedge bid
  at $35 Jul-17**. The 3DTE $44.5P ATM buying is the only genuinely
  bearish short-term signal.
- **Conviction:** **3 / 5**. Overwriting + put-writing is a covered-call /
  buy-write pattern, which is structurally bullish-but-bounded. The tail
  put bid prevents a higher conviction call.
- **Three pin/cliff strikes for phase-9 entry/stop reference:**
  1. **$50 Jun-18 call wall** — 23,713 OI (+1,352 today), heavy overwriting.
     Dealer-positive gamma builds above $50 → suppresses upside; sustained
     close above $50 forces overwriter unwind = potential squeeze fuel.
  2. **$55 Jun-18 secondary cap** — 14,009 OI (+817 today). Second
     resistance band.
  3. **$35 Jul-17 put floor** — 6,923 OI (+1,831 today bought). Below $35
     dealers are short gamma → downside acceleration risk. Acts as both
     hedge cluster and a marker of where institutions think tail risk
     becomes real.
  4. (Bonus) **$44.5 May-22** — 3DTE ATM put pressure; if 5/22 closes
     below $44.5 those puts go ITM and dealers buy shares to delta-hedge
     into the close.
- **Open questions:**
  - Is the $50 Jun-18 call wall a true ceiling (positive gamma → mean-
    reversion) or a setup for a squeeze if a catalyst forces price
    through it? Phase 4 GEX/DEX and phase 5 historical GEX time-series
    will clarify.
  - The $35 Jul-17 put accumulation (+1,831 OI) — is this a single
    institution's structural hedge, or part of a broader bearish
    campaign? Phase 7 insights composite (institutional accumulation
    score) may help disambiguate.
  - Why is there no PYPL pin risk despite high recent options volume?
    Because OI is bimodal: heavy at $50 (call wall, +9.5% OTM) and at
    $35 (put bid, −20% OTM), with thin OI right at spot. Phase 9 should
    size with this gap in mind.
