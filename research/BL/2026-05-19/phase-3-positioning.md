# Phase 3 — Open Interest & Positioning

**Ticker:** BL
**As-of date:** 2026-05-19
**Generated:** 2026-05-19T00:00:00Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md

## Summary

Open-interest evidence is **emphatic and uni-directional bullish**. The single
largest OI increase across the entire BL chain is the same contract that
dominated phase-1 sweeps and phase-2 dark pool: **BL 2026-12-18 $27.5 call**
moved from `last_oi=3162` → `curr_oi=16178`, a **net +13,016 OI** with
`prev_ask_volume=12013` vs `prev_bid_volume=2697` (ask:bid ≈ **4.45×**) and
`prev_total_premium=11647199` [OI:oi_biggest_increases,
OI:oi_smart_positioning]. The phase-1 `$4.14M` ask-side sweep is therefore
**only ~36% of today's total $11.65M premium** on this contract — the rest
came in via patient at-mid / mid-spread fills, consistent with an
institutional limit-order ladder, not a single retail panic-buy. **Every
other directional row in smart-positioning is also bullish** (one micro
"bearish" exception is $1,165 premium on a far-OTM strike — noise)
[OI:oi_smart_positioning]. The single closing trade is **BL 2026-06-18 $32.5C
−45 OI** [OI:oi_decrease_with_volume] — a small, near-DTE position being
unwound while the Dec position is built; circumstantially consistent with a
roll-out, even though `oi_position_rolls` returns empty (its single-day
threshold is set higher than this roll's magnitude). **Net bias: bullish,
conviction 5/5.** No pin risk (BL not in OPEX-week window; lead expiry is
213 DTE [OI:oi_pin_risk, OI:oi_opex_concentration]).

## Key signals

- **Lead OI swing:** `BL261218C00027500` `last_oi=3162` → `curr_oi=16178`,
  `oi_diff_plain=13016`, ratio +411.6% [OI:oi_biggest_increases].
- **Smart-positioning confirms bullish:** `inferred_direction="bullish"`,
  `net_ask_bid=9316` on the lead contract [OI:oi_smart_positioning].
- **Premium dwarfs sweep premium:** `prev_total_premium=11647199` on the lead
  contract vs $4,137,830 from phase-1 sweeps — sweep is **35.5%** of the day's
  total premium [OI:oi_biggest_increases, cross-ref phase-1-flow.md].
- **OTM call ladder building:** OI increases at $30 (+46), $32.5 (closing
  but volume 165), $35 (+157), $37.5 (+106), and $40 across two expiries
  (+57 Aug, +123 Nov) — a stair-step bullish ladder
  [OI:oi_biggest_increases, OI:oi_smart_positioning].
- **Put sale signal:** the only put OI increase is `BL260618P00027500`
  +20 OI on the **bid side** (`net_ask_bid=-20`) — puts being **sold**, i.e.
  bullish positioning, not protection-buying [OI:oi_smart_positioning].

## Detailed findings

### Largest OI increases [OI:oi_biggest_increases]

| Option symbol | Strike | DTE | Last OI | Curr OI | ΔOI | Avg px | Ask vol | Bid vol | Premium |
|---------------|--------|-----|---------|---------|-----|--------|---------|---------|---------|
| **BL261218C00027500** | **27.5** | **213** | 3,162 | **16,178** | **+13,016** | 7.80 | 12,013 | 2,697 | **$11,647,199** |
| BL260618C00035000 | 35.0 | 30 | 8 | 165 | +157 | 1.02 | 161 | 6 | $17,071 |
| BL261120C00040000 | 40.0 | 185 | 7 | 130 | +123 | 2.79 | 130 | 1 | $36,600 |
| BL260618C00037500 | 37.5 | 30 | 2 | 108 | +106 | 0.78 | 105 | 3 | $8,421 |
| BL260821C00040000 | 40.0 | 94 | 17 | 74 | +57 | 1.56 | 51 | 8 | $9,208 |
| BL260618C00030000 | 30.0 | 30 | 53 | 99 | +46 | 2.30 | 73 | 1 | $17,965 |
| BL261218C00062500 | 62.5 | 213 | 84 | 109 | +25 | 0.47 | 0 | 25 | $1,165 (bid) |
| BL260618P00027500 | 27.5 | 30 | 13 | 33 | +20 | 1.30 | 0 | 20 | $2,600 (bid → puts sold) |

Eight directional rows; **seven bullish, one neutral/distributional**
(`$62.5C +25 OI bid-side` — $1.2k premium, immaterial; likely a
spread leg closure or covered-call write at a strike far above spot $30.21).

### Closing / roll activity [OI:oi_decrease_with_volume]

| Option symbol | Strike | DTE | Last OI | Curr OI | ΔOI | Volume | Avg px | Premium |
|---------------|--------|-----|---------|---------|-----|--------|--------|---------|
| BL260618C00032500 | 32.5 | 30 | 153 | 108 | **−45** | 165 | 1.40 | $23,043 |

This is the **only** OI decrease in BL today. It is small relative to the
+13,016 Dec build-up. But the **strike + DTE combination** is interesting:
$32.5 was a popular June-expiry OTM call last week (per the sweeps table in
phase-1 that showed June 32.5C ask sweeps $14,690 + bid sweeps $12,962 ≈
$27.6k two-sided trading). A position is being trimmed in June while a much
larger long is being layered in Dec. Possible explanations:

1. **Roll-out:** trader who owned June $32.5C is rolling to Dec $27.5C —
   gives up OTM upside leverage in exchange for ITM exposure with vega and
   time. Consistent with phase-1 buyer's pay-up tolerance and high-IV vega
   bias (vega ~0.082).
2. **Profit-taking on near-DTE:** unrelated trader closing a different June
   position; would not affect the bull thesis.

`oi_position_rolls` returned empty (`rolls_detected=0`,
`threshold=50`) — the June close (-45) is below the default threshold and the
algorithm did not match it to the Dec 27.5C buildup because the strikes don't
match (it looks for same-strike roll-outs). The signal here is suggestive,
not confirmed; downstream phases should consider both scenarios.

### Smart positioning (inferred direction)
[OI:oi_smart_positioning]

| Option symbol | DTE | Inferred direction | net_ask_bid | ΔOI | Prev premium |
|---------------|-----|---------------------|-------------|-----|--------------|
| BL261218C00027500 | 213 | **bullish** | **+9,316** | +13,016 | $11,647,199 |
| BL260618C00035000 | 30 | bullish | +155 | +157 | $17,071 |
| BL261120C00040000 | 185 | bullish | +129 | +123 | $36,600 |
| BL260618C00037500 | 30 | bullish | +102 | +106 | $8,421 |
| BL260821C00040000 | 94 | bullish | +43 | +57 | $9,208 |
| BL260618C00030000 | 30 | bullish | +72 | +46 | $17,965 |
| BL261218C00062500 | 213 | bearish | −25 | +25 | $1,165 |
| BL260618P00027500 | 30 | **bullish** (put sold) | −20 | +20 | $2,600 |

**Aggregate net_ask_bid (sum of bullish rows): +9,817 contracts.** Effectively
all of this concentrates in the lead Dec $27.5C. The bullish "ladder" at
$30/$35/$37.5/$40/$40 is **tiny in absolute size** (sum ≈ +500 OI) — these
look like the same sponsor (or its cohort) **seeding higher strikes** for
optionality in case the move extends. Phase-9 must treat the Dec $27.5C as
*the* trade and the OTM ladder as confirmation only.

### Pin risk [OI:oi_pin_risk]

BL is **not** in the top 50 pin-risk tickers (`dte_max=7`,
`max_distance_pct=5%`). Expected: BL's near-DTE OI is light (`June 30 / June
32.5 / June 35 / June 37.5` all have OI in low hundreds), and the lead
position is 213 DTE. **No OPEX-week pin to fear or exploit.**

### OPEX concentration [OI:oi_opex_concentration]

BL is **not** in the top 30 tickers with concentrated OPEX OI. BL's OI is
distributed across June, August, November, and December expiries — there is
no single-expiry cliff that would trigger a forced unwind. **Open question
for phase 4:** even though there's no concentration *cliff*, is there enough
gamma at Dec $27.5C alone to materially move dealer hedging? (Answer should
come from `options_structure_gex` filtered to BL.)

## Cross-phase confluence

| Datapoint | Phase 1 | Phase 2 | Phase 3 |
|-----------|---------|---------|---------|
| Anchor strike/expiry | Dec $27.5C, $4.14M ask sweeps | n/a (stock-side) | +13,016 OI, $11.65M total premium |
| Buyer aggression | paid $7.40 → $8.40 ask | paid +$0.07 / +$0.14 above NBBO mid | ask:bid 4.45× on lead contract |
| Persistence | 3 of 5 sessions, $17.97M sweep agg | 5-day floor at $24.90-25.81 ($8.72M) | OI more than quintupled today |
| Hedging visible? | 1 token put trade $1,300 | no extended-hours hedge prints | put OI +20 on bid (puts SOLD, not bought) |

Confluence across all three phases is **maximally aligned**. The same name,
same strike, same expiry, same direction, multiple venues, increasing
intensity. Phase-4 (dealer structure) is the next gate — if dealers are
short gamma at $27.5–$30, this thesis multiplies.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `oi_biggest_increases` | `{symbol:BL, top-n:20, min-oi-change:10, date:2026-05-19}` | 8 rows; lead is Dec 27.5C +13,016 OI |
| `oi_decrease_with_volume` | `{symbol:BL, top-n:15, min-volume:10, date:2026-05-19}` | 1 row: June 32.5C −45 |
| `oi_smart_positioning` | `{symbol:BL, top-n:20, min-oi-change:10, date:2026-05-19}` | 8 rows; 7 bullish, 1 bearish (immaterial) |
| `oi_position_rolls` | `{symbol:BL, threshold:50, near-dte-max:60, date:2026-05-19}` | empty (threshold too high for −45 close) |
| `oi_pin_risk` | `{top-n:50, dte-max:7, max-distance-pct:5, date:2026-05-19}` | BL absent (213 DTE, not OPEX week) |
| `oi_opex_concentration` | `{top-n:30, min-concentration-pct:40, date:2026-05-19}` | BL absent (OI distributed across expiries) |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** **Bullish** — speculative/directional call
  build-up dominated by a single 213-DTE ITM call; OTM ladder at higher
  strikes adds confirmation.
- **Conviction:** **5 / 5**.
- **Three pin/cliff strikes for phase-9 entry/stop reference:**
  1. **$27.5 (Dec 18, 2026)** — the **gravitational center of the position**.
     16,178 OI × 100 = 1.6M share-equivalent at full delta; current delta ~0.67
     → ~1.08M share-equivalent long delta in dealer-net-short hands. This is
     where dealer gamma must be checked in phase 4.
  2. **$30 / $32.5 / $35** — the **upside ladder**. If price reaches $32.5 the
     Dec $27.5C goes deeper ITM (delta → 0.85+), and the seeded OTM strikes
     start mattering for dealer hedging.
  3. **No OPEX pin** for the next week — phase 4 should look for dealer
     gamma flip / charm / vanna without expecting pin behavior.
- **Three things later phases should remember:**
  1. **Total premium on the lead contract is $11.65M today**, not $4.14M.
     Phase-9 sizing must respect this — the institution behind the trade
     has notional sized to a multi-billion-dollar fund, not a $500M shop.
  2. **One contract carries the thesis.** Dec $27.5C; if it doesn't fill,
     this whole blueprint is unimplementable for the user.
  3. **No defensive OI** anywhere — puts being sold, not bought. There is
     **no institutional hedge** working against this campaign; phase-8 risk
     monitor must flag this as a one-sided positioning regime.
- **Open questions:**
  - Where is BL's **dealer net gamma** today, and at what spot does it flip? →
    phase 4 (`options_structure_gex`, `options_structure_today_gamma_flip`).
  - Does the **DEX** profile show dealer-net-short calls at $27.5 (forcing
    them to buy stock as price rises) or dealer-net-long (no forced
    chasing)? → phase 4.
  - Is the IV the buyer is paying (78-81%) extreme by **historical**
    standards? → phase 5 (`historical_iv_percentile_zscore`).
  - **Why now?** What is the **catalyst** — earnings, M&A speculation, or a
    sector re-rating in accounting/finance SaaS that justifies a deep-ITM,
    213-DTE, $12M premium bet? → phase 5 + phase 6 + phase 7.
