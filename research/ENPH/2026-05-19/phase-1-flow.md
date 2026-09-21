# Phase 1 — Options Flow

**Ticker:** ENPH
**As-of date:** 2026-05-19 (effective UW date 2026-05-15)
**Generated:** 2026-05-19T00:00:00-04:00
**Upstream phases cited:** phase-0-intake.md

## Summary

The ENPH 2026-05-15 tape is **decisively bullish with one large structural
caveat**. Aggregate ask-side / ask-favored call premium in near and
intermediate expiries (May → Sept 2026) blows out **$8M+** with persistent
sweep activity, and a single late-session, paired **Jun-2027 $70 call /
$45 put trade** (~12,300×each, ~$14.8M premium each, simultaneous fill) prints
a clear **long-dated bullish risk-reversal-style combo** (call delta +0.53,
put delta −0.28 → net long ~+0.80Δ even if held as a strangle, more
bullish if the $45 put leg is short). Sweep persistence flags ENPH as
**5-of-5 sessions in the top of the bullish sweep board with $55.8M
cumulative sweep premium** — the single strongest persistence print on the
board. The caveat: deep-ITM **Jan-2027 $100 puts sold on the bid for ~$3.2M
aggregate premium** (a synthetic-long signal but also a profile that suggests
a holder rolling out covered puts).

Spot reference (from largest top-premium trade prints): **$52.11 intraday,
~$53.19 by 17:56Z, ~$53.31 by 18:44Z** — call this **~$52.50 close**.

## Key signals

- **5-of-5 bullish sweep persistence, $55.8M cumulative premium**
  [FLOW:hot_chains_sweep_persistence] — strongest signal on the board.
- **Jun-2027 $70 call + $45 put combo, 12,300 contracts each, ~$29.5M
  combined premium, simultaneous 17:13:03Z fill, "no_side"**
  [FLOW:options_flow_sweeps][FLOW:top_premium_trades] — long-dated bullish
  combo (likely risk reversal sell-put/buy-call).
- **Jan-2027 $100 puts SOLD on bid (16 trades, 606 contracts, $3.23M
  aggregate)** [FLOW:options_flow_sweeps] — synthetic long via deep-ITM put
  monetization; could also be position roll.
- **Ask-side June $50 / $55 / $65 call sweeps totaling ~$5M premium** at
  flow_iv ~0.93–0.95 (in-line with current IV regime), executed near intraday
  highs [FLOW:options_flow_sweeps].
- **Short-dated 5/15 expiring-day IV outliers (call IVs 5–29, max_iv
  29.71)** are mechanical end-of-life noise [FLOW:options_flow_iv_outliers]
  — discount.

## Detailed findings

### Sweeps — ask vs bid, premium, persistence

Top sweep aggregations (date=2026-05-15, min_premium=$100k):

| Expiry | Type | Strike | Side | Premium | Size | Trades | Avg Price | Note |
|---|---|---|---|---|---|---|---|---|
| 2027-06-17 | call | 70 | no_side | $14.82M | 12,300 | 1 | $12.05 | Combo leg A |
| 2027-06-17 | put | 45 | no_side | $14.64M | 12,300 | 1 | $11.90 | Combo leg B |
| 2027-01-15 | put | 100 | **bid** | $3.23M | 606 | 16 | $53.46 | Deep ITM puts SOLD (synthetic long / roll) |
| 2026-06-18 | call | 50 | **ask** | $2.30M | 3,665 | 415 | $6.39 | Bullish |
| 2026-06-18 | call | 50 | bid | $1.52M | 2,482 | 275 | $6.27 | Mixed — likely some net-sell |
| 2026-06-18 | call | 55 | bid | $1.23M | 2,699 | 417 | $4.35 | Mixed |
| 2026-09-18 | call | 65 | **ask** | $1.13M | 2,343 | 160 | $5.44 | Bullish |
| 2026-05-29 | call | 52 | bid | $1.06M | 2,796 | 32 | $4.39 | ATM near-term — direction ambiguous |
| 2026-06-18 | call | 55 | **ask** | $0.92M | 2,128 | 395 | $4.32 | Bullish |
| 2026-06-18 | call | 60 | bid | $0.87M | 2,589 | 245 | $3.36 | Mixed |
| 2026-07-17 | call | 45 | bid | $0.74M | 633 | 47 | $10.58 | Deep ITM call bid — possibly closing |

**Ask-side bullish premium (calls only, ask-tagged): ≈ $7.4M** across
June/Sept/Aug expiries.
**Bid-side neutral/bearish on calls: ≈ $5.7M** but most are near-ATM and
likely 2-way market-maker noise rather than directional selling.
**Net directional read: bullish, ~$7M of clean ask-side conviction +
$3.2M of synthetic long from put-selling.**

### Sweep persistence (5-day)

`hot_chains_sweep_persistence` (days=5, symbol=ENPH):

| Field | Value |
|---|---|
| sessions_in_top | **5 of 5** |
| consistency_score | **1.00** |
| dominant_direction | **bullish** |
| total_sweep_premium (5d) | **$55,813,662** |

This is a maximum-persistence print. Smart-money sweeping ENPH calls every
single session over the past week.

### New positioning (unusual vol, vol/OI ratio)

`options_flow_unusual_volume` (min_vol_oi_ratio=3):

The most striking entries:

| Expiry | Type | Strike | OI | Volume | Vol/OI | Premium | Avg IV |
|---|---|---|---|---|---|---|---|
| 2027-06-17 | **put** | 45 | 71 | 12,308 | **173.4** | $14.65M | 0.759 |
| 2026-06-05 | put | 51 | 1 | 148 | 148 | $58.8k | 0.950 |
| 2026-05-22 | put | 31.5 | 4 | 356 | 89 | $3.4k | 1.808 |
| 2026-06-12 | put | 50 | 6 | 384 | 64 | $154k | 0.924 |
| 2026-05-29 | put | 47 | 4 | 136 | 34 | $37.7k | 0.925 |
| 2026-05-22 | put | 32.5 | 36 | 1,004 | 27.9 | $3.5k | 1.471 |
| 2026-05-22 | put | 46 | 12 | 236 | 19.7 | $33k | 1.016 |
| 2026-05-22 | call | 55 | 436 | 4,492 | 10.3 | **$863k** | 1.097 |
| 2026-07-17 | put | 45 | 194 | 2,077 | 10.7 | $826k | 0.853 |
| 2026-07-17 | call | 55 | 214 | 1,779 | 8.3 | $951k | 0.898 |
| 2026-09-18 | call | 65 | 489 | 3,254 | 6.65 | **$1.66M** | 0.883 |

Notes:
- The **2027 $45 put** is the same line as the combo leg above; vol/OI of
  173 confirms this is brand-new opening, not roll. Pairs with the $70 call
  leg.
- Cluster of **deep-OTM short-dated puts (strikes 30–35 for 5/22 expiry)**
  is **small-dollar tail-hedge tape** — premiums $400–$3,500 each. Likely
  retail or volatility-sweep machine; **do NOT read as directional bearish**.
- **Sep-2026 $65 calls with $1.66M premium and vol/OI 6.65** is the
  cleanest new-money upside speculation of the day.

### Largest premium prints

`options_flow_top_premium_trades` (top 10):

| Time (Z) | Expiry | Type | Strike | Side | Premium | Size | Spot | IV | Δ |
|---|---|---|---|---|---|---|---|---|---|
| 17:13:03 | 2027-06-17 | call | 70 | no_side | $14.82M | 12,300 | 52.11 | 0.80 | +0.53 |
| 17:13:03 | 2027-06-17 | put | 45 | no_side | $14.64M | 12,300 | 52.11 | 0.78 | −0.28 |
| 13:48:35 | 2027-01-15 | put | 100 | **bid** | $1.08M | 200 | 47.10 | 0.67 | −0.86 |
| 15:11:59 | 2026-06-18 | call | 50 | bid | $0.62M | 1,000 | 50.82 | 0.94 | +0.58 |
| 15:12:25 | 2026-06-18 | call | 50 | ask | $0.62M | 1,000 | 50.78 | 0.95 | +0.58 |
| 16:16:57 | 2026-05-29 | call | 52 | bid | $0.60M | 1,770 | 50.74 | 1.00 | +0.49 |
| 17:56:35 | 2026-08-21 | call | 50 | **ask** | $0.55M | 477 | 53.19 | 0.93 | +0.64 |
| 15:18:06 | 2027-01-15 | put | 100 | **bid** | $0.52M | 100 | 50.82 | 0.74 | −0.79 |
| 15:04:46 | 2027-01-15 | put | 100 | **bid** | $0.51M | 100 | 50.93 | 0.72 | −0.80 |
| 14:12:35 | 2026-09-18 | call | 50 | ask | $0.35M | 380 | 48.55 | 0.86 | +0.58 |

**Interpretation of the headline $29.5M combo (17:13:03Z, Jun-2027 70C +
45P, same size, no_side):**
- Same timestamp / same size / opposite legs / similar premiums
  ≈ **block-printed combo**.
- Mid-IV (~0.78–0.80 on both legs, in-line with surface) suggests neither
  leg was traded at an aggressive premium — consistent with a single
  negotiated trade routed to floor.
- Net delta if held as **strangle (long both)**: +0.53 − 0.28 = **+0.25Δ
  bullish**.
- Net delta if held as **risk reversal (long call / short put)**: +0.53 +
  0.28 = **+0.80Δ bullish**.
- Either way, the bias is **long stock equivalent on a 2-year horizon**.
- The institutional read: a fund putting on a **multi-year long ENPH
  expression** financed in part by selling the $45 put (the buyer collects
  ~$11.90 if short the put — implying willingness to be long stock at an
  effective $33 cost basis vs current ~$52.50).

**Jan-2027 $100 puts sold on bid (×3 prints totaling $2.1M premium):**
- Deep ITM (50%+ ITM with spot $50). Selling a $100 put for ~$53 ≈ buying
  stock at ($100 − $53) = $47 net.
- Net effect: **bullish (synthetic long, cost ~$47 basis)**.
- Could alternatively be **closing of a prior short put position**, but
  there is no offsetting decrease in OI for that strike in the OI tools
  yet — phase 3 will confirm.

### IV outliers + Greeks

`options_flow_iv_outliers` (min_iv=1.0):
- Top entries are **all 5/15 expiring-day calls** with IVs 5–29. This is
  end-of-life pricing noise — discount entirely.
- Cleaner outliers: **5/22 OTM puts (strikes 27.5–35)** carry IV
  1.4–2.5 — a fat tail-hedge skew on the **short-dated put side**, but the
  size is tiny ($400–$3,500 each), so this is retail/MM noise, not
  institutional positioning.

`options_flow_greek_screener` (sort_by=premium): mirrors the top-premium
table above. The 2027 combo dominates vega: each leg ~0.18–0.22 vega per
contract × 12,300 contracts ≈ **$2.5M+ vega exposure per 1 vol point per
leg** — this is a significant volatility position regardless of direction.

### Smart money flow (market-wide, ENPH filtered)

- `hot_chains_smart_money_flow direction=bullish, min_volume=500, top_n=25`:
  ENPH **does not appear** in the top-25 bullish smart-money list
  (dominated by TLT, F, NU, INTC, PEP, QQQ index plays).
- `hot_chains_smart_money_flow direction=bearish`: ENPH **does not appear**
  in the bearish list either.
- Interpretation: ENPH's bullishness shows up in **persistence + sweep
  ratio**, not in raw same-day ask/bid volume imbalance — typical of a
  high-IV name where market makers actively two-side every print.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|---|---|---|
| `mcp__uw-pp__options_flow_sweeps` | symbol=ENPH, date=2026-05-15, min_premium=100000, top_n=25 | 25 rows; $7M+ ask-side bullish premium |
| `mcp__uw-pp__options_flow_unusual_volume` | symbol=ENPH, date=2026-05-15, min_vol_oi_ratio=3, top_n=25 | 23 rows; top entry vol/OI 173 |
| `mcp__uw-pp__options_flow_top_premium_trades` | symbol=ENPH, date=2026-05-15, top_n=25 | 25 rows; #1 $14.82M Jun-2027 70C |
| `mcp__uw-pp__options_flow_iv_outliers` | symbol=ENPH, date=2026-05-15, top_n=15 | 15 rows; mostly expiring-day noise |
| `mcp__uw-pp__options_flow_greek_screener` | symbol=ENPH, date=2026-05-15, top_n=15, sort_by=premium | 15 rows; vega-heavy 2027 combo on top |
| `mcp__uw-pp__hot_chains_smart_money_flow` | direction=bullish, date=2026-05-15, top_n=25, min_volume=500 | ENPH absent from top-25 |
| `mcp__uw-pp__hot_chains_smart_money_flow` | direction=bearish, date=2026-05-15, top_n=25, min_volume=500 | ENPH absent from top-25 |
| `mcp__uw-pp__hot_chains_sweep_persistence` | symbol=ENPH, days=5, top_n=20 | 5/5 sessions, $55.8M, bullish |
| `mcp__uw-pp__hot_chains_sweep_ratio` | date=2026-05-15, top_n=25, min_volume=500, min_sweep_ratio=0.3 | ENPH absent (filtered by vol≥500 mechanically); covered via sweep_persistence |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** **bullish** (with one ambiguous LEAP-combo leg
  that could be defensive).
- **Conviction:** **4 / 5** — driven by 5/5 sweep persistence and the
  $14.8M Jun-2027 $70 call leg.
- **Three things later phases should remember:**
  1. **Spot reference is $52.11–$53.31** intraday — call it **$52.50
     close** for phase-9 entry levels.
  2. **$14.8M Jun-2027 $70 call + $14.6M Jun-2027 $45 put combo** at
     17:13:03Z is the dominant institutional fingerprint. Phase 3 must
     confirm both legs created new OI (they should, given vol/OI of 173 on
     the put leg).
  3. **Persistent ask-side call sweeps in June/Sept 2026 expiries**
     ($45–$65 strikes) total ~$7M+ premium and have run for 5 consecutive
     sessions.
- **Open questions:**
  - Is the Jun-2027 combo a **risk reversal (bullish)** or a **strangle
     (vol bet)**? Phase-2 dark pool and phase-3 OI behavior tomorrow will
     clarify; for now we read it as risk reversal (more probable given
     bullish persistence context).
  - Is the **Jan-2027 $100 put bid-side selling** new (= synthetic long)
     or a roll out of a prior position? Phase-3 `oi_decrease_with_volume`
     should confirm.
  - **Is dark pool confirming this premium?** — Phase 2 must answer.
