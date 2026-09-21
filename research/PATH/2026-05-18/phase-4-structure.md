# Phase 4 — Dealer Structure & Gamma

**Ticker:** PATH
**As-of date:** 2026-05-18 (data: 2026-05-15)
**Generated:** 2026-05-18T00:55:00-04:00
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-3-positioning.md

## Summary

PATH's dealer book has a textbook **"asymmetric squeeze pad" structure**:
overall GEX is positive (+$1.05B, ZGL $7.53), but at the per-strike level
**spot $10.29 sits inside a NEGATIVE-GEX cluster ($8-$10.50) with a
massive POSITIVE-GEX wall at $13 (+$627M)**
[STRUCT:gex]. Net DEX is **+$2.16B** — public is heavily call-long,
dealers are short calls, and the mechanical hedge is to **BUY
underlying** [STRUCT:dex]. The single most important finding is the
**term-structure CATALYST KINK: IV peaks at 118.3% on the 2026-05-29
expiry**, well above the 75.8% (4 DTE), 103.8% (18 DTE), or 96.3% (31
DTE) neighbors — implies the market is pricing a **binary event in the
2026-05-22 → 2026-05-29 window** (very likely UiPath earnings)
[STRUCT:iv_term_structure]. **30-DTE skew is INVERTED:** call_25Δ IV
97.6% vs put_25Δ IV 89.6% (skew_ratio 0.918) — the market is paying up
for **upside** vol, not crash hedges — a bullish speculative footprint
[STRUCT:term_skew].

## Key signals

- **Total GEX +$1.05B, ZGL $7.53, regime POSITIVE** —
  long-gamma overall [STRUCT:gex].
- **Per-strike: NEGATIVE GEX from $8 to $10.5 → POSITIVE GEX flip at $11
  → massive +$627M at $13** — spot $10.29 sits in the **short-gamma
  amplification zone**; any push above $11 enters dealer long-gamma
  damping zone [STRUCT:gex].
- **Net DEX +$2.16B → dealers BUY underlying as hedge** — mechanical bid
  flow [STRUCT:dex].
- **IV term structure: CATALYST KINK at 2026-05-29 = 118.3%**, vs 75.8%
  at 2026-05-22 and 96.3% at 2026-06-18. **Earnings-shaped kink
  ~11 DTE** [STRUCT:iv_term_structure].
- **30-DTE skew INVERTED (call_25Δ IV 97.6% > put_25Δ IV 89.6%, skew
  -8.05%)** — upside speculation rich, downside hedges relatively
  cheap [STRUCT:term_skew].

## Detailed findings

### GEX (DTE ≤ 45)

| Strike | Net GEX | Role |
|---|---|---|
| $8 | -$1.17M | Negative |
| $8.5 | -$16.85M | Negative |
| **$9** | **-$101.39M** | **Largest negative node** |
| $9.5 | -$25.32M | Negative |
| **$10** | **-$63.10M** | Spot-zone negative |
| $10.5 | -$57.27M | Negative |
| **$11** | **+$246.28M** | **GEX flip → positive** |
| $11.5 | +$94.41M | Positive |
| $12 | +$254.58M | Positive |
| **$13** | **+$627.11M** | **Dominant positive wall** |
| $14 | +$17.49M | Positive |
| $15 | +$49.59M | Positive |
| **Total** | **+$1,051,169,560** | Regime: POSITIVE |
| ZGL | **$7.53** | Spot $10.29 — above ZGL |

**Reading the structure:**

- **Below $11 (spot zone): dealer SHORT gamma cluster.** Moves get
  *amplified* — a rally from $10.30 toward $11 will trigger dealer
  buying which adds fuel.
- **Above $11: dealer LONG gamma cluster.** Moves get *damped* — once
  price clears $11, dealers will start selling rallies, with the
  heaviest pressure at $13.
- **$13 is the dominant resistance wall (+$627M)** — this aligns with
  phase-3's note that 2026-05-29 $13C OI = 11,687 and 2026-06-18 $13C
  OI = 6,808.

**Mechanically, this structure is the perfect setup for a sharp move
from $10.30 → $11.00 (short-gamma fuel), then a grinding push toward
$13 (long-gamma resistance, but call wall at the catalyst expiry strike
adds magnetism).**

### DEX

| Field | Value |
|---|---|
| call_dex | $3.85B |
| put_dex | -$1.69B |
| **net_dex** | **+$2.16B** |
| Interpretation | Public net call-long → dealer hedge = BUY underlying |

This is a **mechanical bullish bias** baked into dealer positioning.
Every incremental delta on the public's call book translates into
dealer buying. Combined with the negative GEX at spot, this is a
recipe for upward drift on quiet days.

### Vanna + Charm

| Field | Value |
|---|---|
| net_vanna | **-177,016** (call-heavy public book) |
| net_charm | +17,520,201 |
| call_vanna | -299,408 |
| put_vanna | +122,392 |

**Vanna read:** Because the book is call-heavy and dealers are short
calls:
- **Rising IV (e.g. into earnings) → call deltas grow → dealers add
  long underlying hedge → BUYING pressure** (supports drift into the
  catalyst).
- **Falling IV (post-earnings vol crush) → call deltas drop → dealers
  cut long underlying hedge → SELLING pressure** (textbook vanna decay
  risk after the event).

**This is the post-earnings vol-crush trap.** Even if the earnings beat
is good, if IV crushes from 118% to 60-70%, the vanna unwind alone
could pressure shares. Phase 9 must size for this.

### IV term structure (CATALYST KINK)

| Expiry | DTE | Avg IV | Read |
|---|---|---|---|
| 2026-05-15 | 0 | 29.4% | Expired (residual) |
| 2026-05-22 | 4 | 75.8% | Weekly, no event |
| **2026-05-29** | **11** | **118.3%** | **PEAK — catalyst expiry** |
| 2026-06-05 | 18 | 103.8% | Decaying post-event premium |
| 2026-06-12 | 25 | 98.0% | Decaying |
| 2026-06-18 | 31 | 96.3% | Monthly, still elevated |
| 2026-06-26 | 39 | 87.7% | Normalizing |
| 2026-07-17 | 60 | 83.3% | Back-month baseline |
| 2026-08-21 | 95 | 81.2% | Back-month baseline |
| 2027-01-15 | 245 | 80.2% | LEAP baseline |
| 2028-01-21 | 616 | 79.2% | LEAP baseline |

**Read:** The IV bulge at 2026-05-29 (118.3%) — **+42 pts above the
adjacent 2026-05-22 (75.8%) and +22 pts above 2026-06-05 (103.8%)** —
is a textbook earnings-event kink. Tool reports structure=CONTANGO and
kink_expiry=null (because the back-end smooth slope is contango), but
**a visual inspection makes the catalyst event unmistakable**.

**Inference: UiPath earnings are very likely between 2026-05-26 and
2026-05-29** (Tue-Fri of next week). Phase 6 must verify the calendar
date.

### Term skew (30 DTE)

| Field | Value |
|---|---|
| call_25Δ IV | **97.64%** |
| put_25Δ IV | 89.59% |
| skew (put-call) | **-8.05%** |
| skew_ratio | 0.918 |
| regime | "COMPLACENT" (default label) |

**The tool labels this COMPLACENT, but the real read is more nuanced:**
PATH's 25Δ-call IV > 25Δ-put IV. Negative skew (calls richer than
puts) is **the bullish-speculation signature**, not crash complacency.
It says **the market is paying up for upside vol** — confirming the
phase-1 flow signal that LEAPs are being bid and the phase-3 OI signal
that fresh OI is overwhelmingly call-side.

In a small-cap name into a catalyst, inverted skew with calls priced
above puts is a **call-buyer crowding signal**. Phase 10 should flag
this as a contrarian risk factor — if the catalyst is mildly bullish
but not blowout, vol crush + crowded longs = sharp give-back.

### Front-end IV ratio

| Field | Value |
|---|---|
| near (4 DTE) IV | 75.8% |
| far (31 DTE) IV | 96.3% |
| ratio | 0.787 |
| regime | CONTANGO |

Globally contango, but recall the **11-DTE kink at 118%** sits between
"near" and "far" — the tool's two-point ratio under-samples the event.
The contango reading is technically accurate but the catalyst peak is
the real story.

### Today's gamma flip (0DTE — Friday 2026-05-15, EXPIRED)

| Field | Value |
|---|---|
| today_expiry | 2026-05-15 (Friday OPEX) |
| today_total_GEX | +$6.28B |
| today_ZGL | $8.50 |
| ATM flip strike | $8 |
| Support walls | $10.5 (+$6.05B), $10 (+$199M), $12 (+$85M), $11 (+$38M) |
| Resistance walls | $9.5 (-$134M) |

**Note:** This snapshot is for 2026-05-15 EXPIRED options — useful as a
post-mortem of how PATH closed Friday (well above its 0DTE ZGL of $8.50
= bullish positive-gamma close) but **not actionable for Monday
2026-05-18 trading**. By Monday open the 0DTE chain rolls to 2026-05-22
weekly.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `options_structure_gex` | `{symbol: PATH, dte-max: 45, date: 2026-05-15}` | Total +$1.05B, ZGL $7.53, $13 wall +$627M |
| `options_structure_dex` | `{symbol: PATH, dte-max: 45, date: 2026-05-15}` | Net +$2.16B, dealers buy underlying |
| `options_structure_vanna_charm` | `{symbol: PATH, dte-max: 45, date: 2026-05-15}` | Vanna -177k (call-heavy), charm +17.5M |
| `options_structure_iv_term_structure` | `{symbol: PATH, date: 2026-05-15}` | 118.3% kink at 2026-05-29 |
| `options_structure_term_skew` | `{symbol: PATH, dte-target: 30, date: 2026-05-15}` | Inverted: call 97.6% > put 89.6% |
| `options_structure_front_end_iv_ratio` | `{symbol: PATH, near-dte: 7, far-dte: 30, date: 2026-05-15}` | 0.787 (contango), under-samples kink |
| `options_structure_today_gamma_flip` | `{symbol: PATH, date: 2026-05-15}` | Expired Friday OPEX, ZGL $8.50 — not actionable Monday |

## Tool errors

(none)

## Verdict for downstream phases

- **Bias from this phase:** **BULLISH STRUCTURALLY** — but with explicit
  **post-catalyst vanna unwind risk**.
- **Conviction:** **5/5** on the catalyst identification (IV kink is
  unmistakable). **4/5** on the directional dealer setup (short-gamma
  spot + dealer-buy hedging is high-conviction; resistance at $13 is
  also high-conviction).
- **Three structural levels for phase-9:**
  1. **ZGL $7.53** — long-term gamma flip floor. Spot below this turns
     dealers short gamma → trending sell. **Hard floor / catastrophic
     invalidation.**
  2. **$11 = per-strike GEX flip (negative → positive)** — once price
     clears $11, dealer hedging behavior reverses from amplifying to
     damping. **Primary breakout-confirmation level.** Below $11 =
     short-gamma fuel for the move; above $11 = headwind growing.
  3. **$13 = +$627M GEX wall** — single largest positive-GEX node.
     **Primary upside target and stiff resistance.** Phase-9 should
     either pin profit-take here or use $13C as a credit spread short
     leg.
- **Catalyst window:** **2026-05-26 to 2026-05-29** is the IV-implied
  binary event (likely UiPath FQ1 earnings). Phase 6 to verify.
- **Open questions for downstream:**
  - Confirm the 2026-05-29 IV kink IS UiPath earnings (phase 6).
  - Are there secondary catalysts (analyst day, product launch, ARR
    pre-announcement) that could front-run earnings? (phase 6)
  - **What is the historical post-earnings move for PATH? If realized
    moves average ±15-20%, the 118% IV pricing in roughly ±16-20%
    one-sigma weekly = market is pricing AT or slightly above historical
    norm. If history is ±10%, IV is rich.** (phase 5 historical IV
    percentile + earnings backtest)
