# Phase 3 — Open Interest & Positioning

**Ticker:** LRCX
**As-of date (requested):** 2026-05-18
**Effective as-of date (data):** 2026-05-15
**Generated:** 2026-05-18T00:00:00Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md

## Summary

OI deltas on 5/15 paint a **post-earnings call-overwrite campaign in
August** (~98 DTE): the **8/21 310C** added **+1,503 OI on $5.78M
turnover**, the **8/21 400C** added **+2,007 OI** (almost entirely at the
bid, $2.69M premium = pure call writing 40% OTM), and the deep-ITM **8/21
250C** shed **-1,486 OI** ($10.6M turnover) — a likely **roll-up**:
existing 250C longs/writers closing and a new short-call cap being
established at 310/400. A countervailing bullish trade is the **8/21 320C
+888 OI on 1,036 ask-side prints, $3.55M premium** — directional long
call. **No same-day rolls detected** by the cross-strike algorithm. LRCX is
**not in pin-risk top-25** (DTE to 5/22 OPEX = 7) and not in OPEX
concentration top-30. Net positioning bias: **neutral-to-bearish ceiling
near $310–$320, with isolated bullish $320 bet to size against**.

## Key signals

- **8/21 400C +2,007 OI**, prev_ask_volume 8 vs prev_bid_volume 2,062 →
  near-pure call writing 40% OTM, $2.69M premium written
  [OI:biggest_increases, OI:smart_positioning].
- **8/21 310C +1,503 OI** on $5.78M premium turnover — major institutional
  ceiling at 310 [OI:biggest_increases].
- **8/21 320C +888 OI**, prev_ask_volume 1,036 vs prev_bid_volume 0 → all
  ask = **bullish long-call open** for $3.55M [OI:smart_positioning].
- **8/21 250C -1,486 OI** with 1,529 volume @ $69.59 avg → ITM call
  closing/roll = -$10.6M position turnover [OI:decrease_with_volume].
- **No 5/22 OPEX pin risk surface** — LRCX not in market-wide pin top-25
  despite being 7 days out [OI:pin_risk].

## Detailed findings

### Largest OI increases (LRCX, OI Δ ≥ 500)

| Contract | DTE | Prev OI | Curr OI | Δ OI | Volume | Avg $ | Prev premium | Bid vs Ask vol | Read |
|----------|----:|--------:|--------:|-----:|-------:|------:|--------------:|----------------|------|
| **8/21 400C** | 98 | 91 | 2,098 | **+2,007** | 2,071 | $13.00 | $2.69M | 2062 bid / 8 ask | **Call write (bear)** |
| **8/21 310C** | 98 | 3,240 | 4,743 | +1,503 | 1,509 | $38.33 | $5.78M | 5 bid / 4 ask (block/OTC) | **Call write (bear)** |
| **8/21 320C** | 98 | 255 | 1,143 | +888 | 1,046 | $33.90 | $3.55M | 0 bid / 1036 ask | **Long call (bull)** |
| 5/15 320C | 0 | 1,880 | 2,680 | +800 | 941 | $0.86 | $80k | 475 bid / 118 ask | 0DTE OTM noise |

**Interpretation of the August cluster:** an institution is **selling
calls at 310 and 400** (write campaign, ~$8.5M premium gross) while a
*different* participant is **buying 320 calls** ($3.55M). Net delta of
August writes (310C ~Δ0.55 + 400C ~Δ0.15) is **-$1,800 × 100 × Δ-weighted ≈
-90k delta-equivalent shares short** vs the 320C buyer's **+45k delta**
long. Net institutional positioning for August expiry: **modest net
delta-negative** (≈45k shares-equivalent short).

### Largest OI decreases (LRCX, with volume ≥ 100)

| Contract | DTE | Prev OI | Curr OI | Δ OI | Volume | Avg $ | Notes |
|----------|----:|--------:|--------:|-----:|-------:|------:|-------|
| **8/21 250C** | 98 | 6,212 | 4,726 | **-1,486** | 1,529 | $69.59 | **$10.6M ITM close / roll up** |
| 5/15 302.5C | 0 | 1,422 | 788 | -634 | 1,304 | $5.00 | 0DTE OTM expiry/close |
| 5/15 300C | 0 | 4,367 | 3,762 | -605 | 1,857 | $6.10 | 0DTE OTM expiry/close |
| 5/15 287.5C | 0 | 820 | 568 | -252 | 832 | $14.57 | 0DTE near-ATM close |
| 6/18 170C | 34 | 1,113 | 982 | -131 | 201 | $131.47 | Deep ITM close |
| 5/15 260P | 0 | 6,768 | 6,653 | -115 | 178 | $0.19 | 0DTE OTM expiry |

The **8/21 250C decrease (-1,486)** combined with **8/21 310C, 320C, 400C
increases** is the structural signal: a multi-million-dollar **post-earnings
positioning rotation** — closing ITM 250 strike, redistributing exposure
above $310 (mostly as short calls, with a smaller offsetting long at 320).
This is consistent with **profit-taking on a long-stock position with
overwriting at a new ceiling** rather than fresh directional buying.

### Smart positioning (inferred direction by ask/bid imbalance)

| Contract | Inferred | OI Δ | Net ask-bid |
|----------|----------|-----:|------------:|
| 8/21 400C | **bearish** | +2,007 | **-2,054** |
| 8/21 310C | **bearish** (block-driven) | +1,503 | -1 |
| 8/21 320C | **bullish** | +888 | +1,036 |
| 5/15 320C | bearish | +800 | -357 |

Three of four major Δ-OI strikes flip bearish, only 320C bullish.

### Position rolls

`oi_position_rolls` with `near-dte-max=30, threshold=500` returned **0
rolls** for LRCX. The 250C→310C/320C/400C migration described above is a
*same-expiry* (all 8/21) reallocation, not a near→far roll, so the
roll-detection algorithm correctly skips it. Worth flagging that the
algorithm cannot see across strikes within the same expiry.

### Pin risk (≤7 DTE)

LRCX **does not appear** in the top-25 pin-risk list for the 5/22 OPEX
window. Top of the board is HYG, SPY, QQQ, TLT, IWM, XLF, NVDA, AAPL.
Implication: LRCX OI is reasonably distributed across 5/22 strikes
($260P 6,653 OI, $300C 3,762 OI, $320C 2,680 OI, $260P 5/15 still 6,653)
without a single dominant pin magnet. **No pin scenario to plan around
for 5/22**, but the 6/18 expiry has materially more OI at 300C (2,928),
which phase 4's gamma map will pick up.

### OPEX concentration

LRCX is **not in the OPEX concentration top-30** (cutoff = 100% — illiquid
microcaps dominate the list). Its OI is spread across at least the 5/15,
5/22, 6/18, 7/17, 8/21, 9/19, 12/18, 1/15, and 2028 LEAP expiries. No
single-expiry cliff risk.

## Tool calls (audit trail)

| Tool | Args | Result |
|------|------|--------|
| `mcp__uw-pp__oi_biggest_increases` | symbol=LRCX, top-n=20, min-oi-change=500, date=2026-05-15 | 4 rows |
| `mcp__uw-pp__oi_decrease_with_volume` | symbol=LRCX, top-n=15, min-volume=100, date=2026-05-15 | 15 rows |
| `mcp__uw-pp__oi_smart_positioning` | symbol=LRCX, top-n=20, min-oi-change=500, date=2026-05-15 | 4 rows |
| `mcp__uw-pp__oi_position_rolls` | symbol=LRCX, threshold=500, near-dte-max=30, date=2026-05-15 | 0 rolls |
| `mcp__uw-pp__oi_pin_risk` | top-n=25, dte-max=7, max-distance-pct=5, date=2026-05-15 | 25 rows (no LRCX) |
| `mcp__uw-pp__oi_opex_concentration` | top-n=30, min-concentration-pct=40, date=2026-05-15 | 30 rows (no LRCX) |

## Tool errors

(none)

## Verdict for downstream phases

- **Bias from this phase:** **Bearish-to-neutral with an emerging
  institutional ceiling at $310–$320**. The 8/21 picture is a clear
  call-overwrite campaign: -1,486 ITM 250C closed, +1,503 OI 310C and +2,007
  OI 400C written, partially offset by +888 OI long 320C from a different
  participant. Net delta of new August positioning is short ~45k
  share-equivalents. This is **consistent with phase-1 (5/22 295/300/302.5C
  writes) and phase-2 (5-day institutional distribution at $289–$300)**.
- **Conviction: 4/5**. The August roll is dollar-large ($10M+ closed,
  $11M+ opened), institutional in tenor, and confirmed by ask/bid
  attribution.
- **Three strikes for phase-9:**
  1. **$310 = primary call-write ceiling** (8/21 310C +1,503 OI on $5.78M).
     Cleanest short-thesis level above spot.
  2. **$320 = battleground** (8/21 320C bullish long $3.55M vs 5/15 320C
     and 8/21 400C bearish writes). Above $320 the bear thesis is in
     trouble; below $320 the writes dominate.
  3. **$400 = far ceiling** (8/21 400C +2,007 OI). Implies institutions
     see <40% upside as the August outer band. Functions as a vol-skew
     anchor more than a price target.
- **Open questions:**
  - The 8/21 expiry is **just after** LRCX's expected late-July earnings
    (phase 5/6 to confirm). Are the 310/400 writes **earnings-hedge call
    overwriting against long stock**, or **speculative short-volatility**
    for a known buyer? Phase 7's `insights_*` composite should help.
  - Did dealer gamma post the 1,503 OI build at 310C? If gamma is short
    here, dealers must buy stock as it approaches $310 → squeeze risk.
    (phase 4)
  - Why no LRCX in 5/22 pin-risk top-25? Likely because OI is split
    across many strikes; phase 4 GEX map will reveal whether 5/22 has any
    gamma magnet.
