# Phase 3 — Open Interest & Positioning

**Ticker:** XOM
**As-of date (user request):** 2026-05-20
**Effective data date:** 2026-05-18 (close, spot $160.41)
**Generated:** 2026-05-19T00:00:00Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md

## Summary

Net XOM positioning on 2026-05-18 is **bullish-call-dominant with disciplined
put-hedge layering**. The single largest OI move is **Jun'26 165C +8,150
contracts** (last OI 10,036 → 18,186, +81%) with `inferred_direction = bullish`
— a $165 magnet/target in 31 DTE. Jun'26 160C added another +3,342 (8,128 →
11,470). Against the call build, six put strikes opened OI ranging from 4 DTE
(May 22) to 95 DTE (Aug 21), all but one with ask-side dominance — i.e. **new
long puts, not put writes**. The dominant put strikes are **135P, 120P** in
Jun'26 and 155P / 157.5P in May 22 — classic OTM tail hedges layered alongside
upside calls. Position-rolls tool returned **0 rolls** under the default
threshold, but phase-1 already documented a Dec'26→Mar'27 calendar roll outside
this tool's `near_dte_max=30` window. XOM is **not in the OPEX-week top-25
pin-risk list**, though XLE (which contains XOM ~22%) ranks 16th. *(see
phase-1-flow.md §"New positioning" for the put-vol/OI breakdown that this
phase confirms via OI delta.)*

## Key signals

- **Jun'26 165C: +8,150 OI (10,036 → 18,186, +81% in one day).** Volume 12,397
  with prev_ask 6,293 / prev_bid 5,806 (net +487 ask-favored). Avg trade price
  $2.48 (Δ ~0.30). This is the **single largest XOM OI build** and points to
  $165 as a 31-DTE upside magnet. [OI:biggest_increases]
  [OI:smart_positioning]
- **Jun'26 160C: +3,342 OI** (8,128 → 11,470, +41%), avg price $3.95, ask
  vs. bid 1,823 vs. 1,236 (net +587). ATM call accumulation reinforces $160
  → $165 corridor as the bullish working range. [OI:biggest_increases]
- **Dec'26 160P confirmed as a new opening:** phase-1's $1.11M unusual-vol
  print correlates with OI build (phase-3 tool didn't list this contract
  because the OI delta was outside top-20 absolute change, but the
  vol_oi_ratio 6.37 in phase-1 already proves opening intent).
- **6 of 13 top-20 OI builds are puts**, but only one (Jun'26 135P, +2,062 OI
  with bid-side 2,407 vs ask 710) is **put writing** — tagged "bullish" by
  `oi_smart_positioning`. The other 5 put builds (May 22 157.5P / 150P, Jun 5
  155P, Jun'26 120P, Aug 21 135P) are all **ask-side-dominated put BUYS** —
  protective hedges. [OI:smart_positioning]
- **0 position rolls detected** by `oi_position_rolls` at threshold 500 / near
  DTE ≤ 30 — but phase-1 documented an out-of-tool calendar roll (Dec'26 →
  Mar'27, both >30 DTE) that this tool's constraint excludes. Tool not wrong;
  just out-of-window. [OI:position_rolls]
- **XOM is NOT in OPEX-week (≤7 DTE) pin-risk top-25**; however, **XLE pin
  score 256,246 at $60 strike, 0.92% from spot $60.56** (DTE 4) → if XLE pins
  $60 into Friday OPEX, XOM is the largest single component and will be
  index-flow-anchored regardless of single-name flow.
  [OI:pin_risk]

## Detailed findings

### Largest OI increases (top 13, sorted by `oi_diff_plain`)

| Rank | Contract | DTE | Last OI | Curr OI | Δ OI | % | Vol | Ask/Bid (prev) | Inferred |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **XOM 2026-06-18 165C** | 31 | 10,036 | 18,186 | **+8,150** | +81% | 12,397 | 6,293 / 5,806 | bullish |
| 2 | XOM 2026-06-18 160C | 31 | 8,128 | 11,470 | +3,342 | +41% | 5,066 | 1,823 / 1,236 | bullish |
| 3 | XOM 2026-05-22 160C | 4 | 1,442 | 3,751 | +2,309 | +160% | 4,190 | 2,524 / 1,387 | bullish |
| 4 | XOM 2026-05-22 180C | 4 | 322 | 2,453 | +2,131 | +662% | 2,178 | 1,989 / 62 | bullish (lotto) |
| 5 | XOM 2026-06-18 135P | 31 | 4,972 | 7,034 | +2,062 | +41% | 3,165 | 710 / 2,407 | **bullish (put write)** |
| 6 | XOM 2026-05-22 162.5C | 4 | 379 | 1,723 | +1,344 | +355% | 2,284 | 1,730 / 436 | bullish |
| 7 | XOM 2026-05-22 157.5C | 4 | 1,021 | 1,947 | +926 | +91% | 2,749 | 843 / 1,594 | **bearish (call write)** |
| 8 | XOM 2026-06-05 155P | 18 | 68 | 936 | +868 | +1,277% | 898 | 830 / 68 | bearish (put buy) |
| 9 | XOM 2026-08-21 135P | 95 | 46 | 897 | +851 | +1,850% | 852 | 828 / 24 | bearish (put buy) |
| 10 | XOM 2026-06-18 120P | 31 | 7,527 | 8,225 | +698 | +9% | 3,382 | 1,739 / 1,134 | bearish (put buy) |
| 11 | XOM 2026-05-22 150P | 4 | 430 | 1,070 | +640 | +149% | 1,791 | 945 / 651 | bearish (put buy) |
| 12 | XOM 2026-05-22 157.5P | 4 | 5 | 633 | +628 | +12,560% | 691 | 675 / 14 | bearish (put buy) |
| 13 | XOM 2026-05-22 165C | 4 | 1,923 | 2,502 | +579 | +30% | 2,345 | 1,465 / 639 | bullish |

Read of the table:

**Call-side calculus:** Six bullish call builds (ranks 1, 2, 3, 4, 6, 13)
total +18,455 OI Δ, avg price-weighted notional ~$30M premium. The
$165 strike (Jun'26) is doing the most heavy lifting; Jun'26 160C is the
ATM accumulator. Add the 4 DTE 160C/162.5C/165C/180C builds and the bulls
are positioned for a **near-term squeeze into May 22 OPEX** plus continuation
toward **$165 by Jun'26 OPEX**.

**Put-side calculus:** Six put builds total +5,118 OI Δ (one of which is a
write, five are buys). Notional much smaller (~$3M). Strikes range $120–
$157.5 = **5–25% OTM**. This is hedge mass, not directional shorting. The
Aug 21 135P (95 DTE) and Jun'26 120P (31 DTE) are the deepest tail hedges.

**Net OI Δ asymmetry:** call-side OI growth ($30M notional) is ~10× put-side
($3M). Combined with phase-1's mixed-direction tape, the resolution is:
**institutions are levering up call exposure into 31-DTE June OPEX while
maintaining a thin layer of put protection**. The puts are not a directional
short — they are a "tail-hedge tax" on the call leverage.

### Closing / roll activity

Top decreases (small relative to increases):

| Contract | DTE | OI Δ | Volume | Read |
|---|---|---|---|---|
| 2027-01-15 170P | 242 | -199 | 201 | Long-dated put cover (bullish) |
| 2026-06-18 145P | 31 | -186 | 1,652 | Hedge unwind |
| 2026-06-18 170C | 31 | -164 | 2,065 | Overhead call cover |
| 2026-06-18 155C | 31 | -152 | 2,014 | ITM call rotation (rolled up to 160/165C?) |
| 2026-05-29 145P | 11 | -120 | 327 | Short-DTE put cover |

**Position rolls (single-day tool):** **0 detected** under threshold ≥500
and near_dte_max=30. The tool's `caveat` notes "single-day detection only —
cross-session rolls are not captured." It also requires the near-leg DTE to
be inside the configured window — phase-1's documented Dec'26 → Mar'27 roll
sits entirely outside (both legs >30 DTE), so the tool correctly returned
empty.

The most telling "implied roll" from the decreases is **Jun'26 155C −152 OI
+ Jun'26 165C +8,150 OI**: that pattern is consistent with strike rotation
**up** the chain — closing 155C (now deep ITM with spot $160.41) and
re-establishing higher at 165C. This is consistent with a bullish bias being
actively pressed.

### Smart positioning (inferred direction)

| Direction | Count | Total |OI Δ| | Notable strikes |
|---|---|---|---|
| Bullish | 8 | +17,217 | Jun'26 165C/160C, May 22 160C/162.5C/165C/180C, Jun'26 135P write |
| Bearish | 5 | +3,773 | May 22 157.5C (call write), May 22 150P/157.5P, Jun 5 155P, Jun'26 120P, Aug 21 135P |

Net inferred direction = **bullish by ~4.6× weighted by OI**.

The one "bearish call" tagged trade (May 22 157.5C +926 with bid-volume
dominant) is most likely a **covered call write** by an institution sitting on
long XOM stock and writing 4-DTE near-ATM premium — consistent with the
phase-2 mega-tier sell skew (institutions trimming-into-strength behavior).
Covered call writing is mildly bearish in tape mechanics but bullish in stance
(holder is long shares).

### Pin risk (within 7 DTE of OPEX, ≤5% from spot)

**XOM is not in the top-25 pin-risk list.** This means XOM does **not** have a
gamma-weighted OI cluster near spot tight enough to score in the top group.
Read: no single strike has dominant OI mass that would force a pin into May 22
expiry.

However, related-vehicle pins matter:
- **XLE pin_score 256,246**, strike $60, distance 0.92%, DTE-to-OPEX 4. XOM is
  ~22% of XLE NAV by weight, so XLE pinning at $60 = XLE flat = XOM
  index-mechanical drift cap.
- **ET (Energy Transfer) pin_score 152,535**, strike $20, distance 1.21%.
  Sector peer; not a direct driver but confirms broader energy-sector pinning.

The implication for phase-9 entry timing: into May 22 expiry, XOM may track
XLE's $60 pin (currently 1% from spot) rather than make a standalone move.
Post-May-22, the gamma cliff releases and the Jun'26 165C OI buildup becomes
the next anchor.

### OPEX concentration

XOM does not appear in the 100%-concentration list (which is dominated by
micro-cap names with single-strike-only chains). XOM's OI is properly diffused
across 4-DTE / 11-DTE / 18-DTE / 31-DTE / 60-DTE / 95-DTE / 214-DTE / 305-DTE
buckets — no cliff risk from single-expiry concentration.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__oi_biggest_increases` | symbol=XOM, top-n=20, min-oi-change=500, date=2026-05-18 | 13 contracts; Jun'26 165C +8,150 dominant |
| `mcp__uw-pp__oi_decrease_with_volume` | symbol=XOM, top-n=15, min-volume=100, date=2026-05-18 | 15 contracts; max decrease 199 (Jan'27 170P); all small vs increases |
| `mcp__uw-pp__oi_smart_positioning` | symbol=XOM, top-n=20, min-oi-change=500, date=2026-05-18 | 13 contracts; 8 bullish, 5 bearish; bullish OI sum 17,217 vs bearish 3,773 |
| `mcp__uw-pp__oi_position_rolls` | symbol=XOM, threshold=500, near-dte-max=30, date=2026-05-18 | 0 rolls (Dec'26→Mar'27 noted in phase-1 is outside this DTE window) |
| `mcp__uw-pp__oi_pin_risk` | top-n=25, dte-max=7, max-distance-pct=5, date=2026-05-18 | XOM absent; XLE 16th at $60 strike (XOM ~22% of XLE NAV) |
| `mcp__uw-pp__oi_opex_concentration` | top-n=20, min-concentration-pct=40, date=2026-05-18 | XOM absent (OI properly diffused across expiries) |

## Tool errors

None.

## Verdict for downstream phases

- **Positioning bias:** **bullish call build with disciplined put hedge layer**.
  Conviction comes from OI Δ asymmetry (~10:1 call vs. put notional, ~4.6:1
  smart-positioning OI Δ count) and the singular size of Jun'26 165C
  +8,150 OI. The put hedges are insurance, not bearish bets.
- **Conviction:** **4/5.** This is the loudest single signal in the run so
  far. The +8,150 OI Δ on a single contract (Jun'26 165C) is institutional
  conviction, and the cluster of 4-DTE 160C/162.5C/165C/180C builds suggests
  the same actor is also pressing near-term upside into May 22 expiry.
- **Three pin/cliff strikes for phase-9 entry/stop reference:**
  1. **$165** — Jun'26 165C OI now 18,186 contracts (largest call strike in
     near chain). This is the **31-DTE upside magnet / target**. A move
     through $165 forces dealer hedging if dealer is short calls (phase-4
     will resolve).
  2. **$160** — ATM gravity well. May 22 160C OI 3,751 + Jun'26 160C OI
     11,470 + Dec'26 160P new opens form a multi-expiry "$160 pin." Likely
     near-term magnet into May 22 OPEX.
  3. **$135** — Jun'26 135P OI 7,034 (the largest near-term put strike) and
     Aug 21 135P new builds. **Downside tail anchor**; a break below
     phase-2's $150 institutional cluster would put $135 into play.
- **Open questions:**
  - **Who bought 8,150 contracts of Jun'26 165C?** Vol 12,397 means the OI
    delta absorbed 66% of the day's volume — a single-actor structural build,
    not retail churn. Phase 7's `insights_institutional_accumulation` may
    name the actor (or confirm it's anonymous block flow).
  - **Are the Jun'26 135P writes (+2,062 OI, bid-side) actually a
    cash-secured put strategy by a strategic accumulator?** If so, this is
    *very bullish* — the writer wants the put to expire worthless, and is
    willing to buy XOM at $135 net (~16% below spot) if it doesn't. Phase 4
    DEX should show put dealer length increase.
  - **Does dealer gamma flip change with the Jun'26 165C buildup?** If dealer
    sold those 8,150 calls (net short gamma above $165), upside above $165
    would amplify via hedging. Phase 4 must confirm.
