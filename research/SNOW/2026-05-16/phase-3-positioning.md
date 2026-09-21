# Phase 3 — Open Interest & Positioning

**Ticker:** SNOW
**As-of date:** 2026-05-16 (data date: 2026-05-15)
**Generated:** 2026-05-17T00:00:00Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md

## Summary

SNOW's same-day OI changes paint a **range-bound short-strangle structure** ($150-$200) layered on top of two clear directional bets. Institutions were net **selling 6/18 180C (+930 OI)** and **6/18 200C (+869 OI)** — both bid-side weighted, classic covered-call income at strikes 14%/27% above spot — while simultaneously **selling 5/22 150P (+930 OI)** at 5% below spot. This strangle is a "range" trade: stay between $150 and $180-$200 and earn premium. On top of it sit two clear bullish directional opens: **5/29 160C (+872 OI ask-side, $1.2M premium)** and **6/26 210C (+788 OI fresh, was 1 OI)**. No position rolls detected on 5/15. SNOW is NOT in the OPEX-week pin-risk top 25, so pinning dynamics are absent. The puts-sold support at $150 is **confluent with phase-2 dark-pool absorption at $150-$153**.

## Key signals

- **$150 put-write build** [OI:biggest_increases]: 5/22 150P OI +930 to 1,162, prev_total_premium $581,983, net_ask_bid -114 (bid-lean = SELLING puts) — classic bullish put-write at institutional support [DP:price_levels].
- **6/18 180C write** [OI:biggest_increases]: OI +929 to 4,886, prev_ask_vol 526 vs bid_vol 1,684, net_ask_bid **-1,158** (deeply bid-side) — covered-call write at $180 = 14% above spot. Cap on near-term upside.
- **5/29 160C buy** [OI:smart_positioning]: OI +872 to 1,610, net_ask_bid **+412** (ask-side), $1.2M prev_total_premium — short-dated bullish directional bet $2 OTM.
- **6/26 210C fresh open** [OI:biggest_increases]: OI 1 → 789 (+788) in one day, ask-side dominant (net_ask_bid +376), 794 volume — pure new-money speculative OTM call buying 33% above spot, expiring 6 wks out.
- **No position rolls and no pin risk** [OI:position_rolls, OI:pin_risk]: SNOW absent from both signals; positioning is fresh, not roll-driven, and not OPEX-week pinned.

## Detailed findings

### Largest OI increases (top 7)

[OI:biggest_increases] at spot $157.66:

| Contract | DTE | OI Δ | Curr OI | Vol | Avg Price | Prev ask vol | Prev bid vol | Prev premium | Inferred dir |
|---|---|---|---|---|---|---|---|---|---|
| SNOW 5/22 150P | 7 | +930 | 1,162 | 1,018 | $5.72 | 447 | 561 | $581,983 | **bullish** (put SELL) |
| SNOW 6/18 180C | 34 | +929 | 4,886 | 2,285 | $6.67 | 526 | 1,684 | $1,525,208 | **bearish** (call SELL) |
| SNOW 5/29 160C | 14 | +872 | 1,610 | 1,310 | $9.17 | 824 | 412 | $1,200,676 | **bullish** (call BUY) |
| SNOW 6/18 200C | 34 | +869 | 4,404 | 2,622 | $3.45 | 422 | 2,136 | $904,107 | **bearish** (call SELL) |
| SNOW 5/29 200C | 14 | +821 | 4,635 | 1,648 | $1.75 | 401 | 1,091 | $288,336 | **bearish** (call SELL) |
| SNOW 6/26 210C | 42 | +788 | 789 | 794 | $3.08 | 396 | 20 | $244,512 | **bullish** (call BUY) |
| SNOW 6/18 320C | 34 | +784 | 1,015 | 921 | $0.07 | 502 | 331 | $6,884 | **bullish** (tail-lottery BUY) |

**Direction tally:**
- Bullish OI opens: 150P SOLD + 160C BOUGHT + 210C BOUGHT + 320C BOUGHT = 4 contracts, ~3,378 OI added
- Bearish OI opens: 180C SOLD + 200C SOLD (5/29) + 200C SOLD (6/18) = 3 contracts, ~2,619 OI added

Counts and OI volumes are roughly balanced, but the **structure** is the message:
- Bullish opens cluster at strikes RANGING from $160 to $320 (some near-term directional, some tail-lottery).
- Bearish opens cluster at strikes $180 and $200 — these are **call writes against the rally**, i.e. someone holding SNOW shares (or having other long delta) is selling premium against further upside, presumably collecting income.
- Put writing at $150 + call writing at $180 (mostly) and $200 = an institutional **short strangle for income** that defines an expected near-term range of **$150-$180** (with hedged tail above to $200).

### Smart positioning (inferred direction)

[OI:smart_positioning] sorted by OI Δ:

| Contract | Inferred dir | net_ask_bid | DTE | Strike vs spot |
|---|---|---|---|---|
| 5/22 150P | **bullish** | -114 | 7 | -4.9% |
| 6/18 180C | **bearish** | -1,158 | 34 | +14.2% |
| 5/29 160C | **bullish** | +412 | 14 | +1.5% |
| 6/18 200C | **bearish** | -1,714 | 34 | +26.9% |
| 5/29 200C | **bearish** | -690 | 14 | +26.9% |
| 6/26 210C | **bullish** | +376 | 42 | +33.2% |
| 6/18 320C | **bullish** | +171 | 34 | +103% |

The two most aggressively bid-side (institutionally SOLD) calls are the $180 and $200 strikes, with combined net_ask_bid = -3,562 contracts. This is the meatiest covered-call write of the day on SNOW. The dealer is the buyer of these calls, meaning dealer is long calls / short stock to delta hedge — as spot approaches $180-$200, dealer hedging is a **headwind to upside**, especially around $180 (the closer strike with bigger volume bid-side).

The $145 strike directional buys from phase-1 (Jun-26-26 $145C, $2.10M premium, vol/OI 314.67) do not appear in the OI top-7 list. The OI at that strike was only 3 before this trade — after Friday's volume of 944, OI should be near 944. Cross-checking: it does not appear because the OI-changes tool ranks by absolute delta; +941 would have been #1. The fact it doesn't appear suggests the trade closed against existing OI rather than building net new OI — OR — these were sweep prints that happened to clear without creating new OI (e.g., assigned or exercised same-day). Worth investigating; for now treat the 145C buy as confirmed directional flow (phase 1) but **note that it did not produce a corresponding OI buildup** in the chain. **This is a phase-10 contradiction flag.** [OI:biggest_increases vs FLOW:unusual_volume]

### Closing / roll activity

[OI:decrease_with_volume] — all small; biggest closure was 5/15 175P -369 OI on OPEX day (routine), no meaningful roll signature. Top decreases:

| Contract | OI Δ | Vol | DTE |
|---|---|---|---|
| 5/15 175P | -369 | 151 | 0 (OPEX) |
| 6/18 250C | -119 | 231 | 34 |
| 5/15 150C | -84 | 433 | 0 |
| 5/22 180C | -81 | 453 | 7 |
| 6/18 210C | -62 | 114 | 34 |

[OI:position_rolls] returned **rolls_detected = 0** with threshold=500, near_dte_max=30. **No near→far rolls today.** Institutional positions are being initiated or unwound at expiry, not rolled. This argues against a "kicking the can" story — the current positioning is fresh conviction.

### Pin risk

[OI:pin_risk] with dte_max=7, max_distance_pct=5%: SNOW does **not** appear in the top 25. The 5/15 OPEX pin candidates are HYG (pin $79, score 2.36M), SPY ($710, 1.90M), QQQ ($700, 1.09M), TLT ($86, 1.04M), IWM ($270, 1.03M), NVDA ($220, 0.72M), AAPL ($300, 0.66M), etc. The chain-wide 5/15 SNOW OI is distributed across $150/$155/$157.5/$160 without a dominant strike, so pinning was unlikely (and the 5/15 close near $158 confirms — no pin discipline visible).

### OPEX concentration

[OI:opex_concentration] SNOW does **not** appear in the top 20 OPEX-concentration list either; the list is dominated by micro-caps like EHTH, MAX, YQ. SNOW's OI is diversified across 5/22, 5/29, 6/12, 6/18, 6/26, 8/21, 9/18, 2027-03, 2028-01, 2028-12 — no single expiry holds >40% of total OI. **No OPEX cliff to worry about.**

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__oi_biggest_increases` | symbol=SNOW, top_n=20, min_oi_change=500 | 7 contracts; balanced bullish/bearish OI builds |
| `mcp__uw-pp__oi_decrease_with_volume` | symbol=SNOW, top_n=15, min_volume=100 | 15 contracts; only OPEX-day closure of note |
| `mcp__uw-pp__oi_smart_positioning` | symbol=SNOW, top_n=20, min_oi_change=500 | Same 7 contracts with directional inference |
| `mcp__uw-pp__oi_position_rolls` | symbol=SNOW, threshold=500, near_dte_max=30 | rolls_detected=0 |
| `mcp__uw-pp__oi_pin_risk` | top_n=25, dte_max=7, max_distance_pct=5 | SNOW not in top 25 |
| `mcp__uw-pp__oi_opex_concentration` | top_n=20, min_concentration_pct=40 | SNOW not in top 20 (diversified expiry) |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** **range-bound short-strangle** ($150-$180) with overlay of two near-term directional bull bets ($160 5/29, $145 6/26 from phase-1). Net mildly bullish in 1-2 weeks (160C buyer + put writes); range-capped above $180.
- **Conviction:** 3/5. The structure is institutional and coherent (range trade), but the directional overlay is only ~$1M premium on top of $2M+ of premium-collection trades. Not a strong one-way conviction.
- **Three pin/cliff strikes for phase-9:**
  1. **$180 = "dealer headwind ceiling"** — 4,886 OI 6/18 180C mostly bid-side built, dealers long the calls and will hedge by selling stock as spot approaches $180. This is a **realistic near-term ceiling**.
  2. **$200 = "tail-strike ceiling"** — 4,404 OI 6/18 200C + 4,635 OI 5/29 200C, both bid-side built. Second-line resistance; the 6/18 200C ask-side sweep ($1.51M phase-1) is the contrarian directional buyer pressing against these writers.
  3. **$150 = "absorbed support"** — 5/22 150P writes (+930 OI bullish) + 5-day DP cluster $150.74-$152.66 ($59M absorbed) = highest-conviction support in the chain. Thesis-broken if violated on volume.
- **Open questions:**
  - **Citation flag:** Phase-1 145C Jun-26 ($2.10M premium, vol/OI 314.67) does not produce a top-7 OI buildup — investigate whether this was sweep-on-existing-OI vs new-money. [Resolve in phase 10.]
  - Is the 6/26 210C fresh buy (+788 OI, $3.08 avg) the same actor as the 6/26 145C buy from phase-1? If so, the trader is constructing a **145/210 call spread** for 6/26 — long $1.10M ITM, short $244k OTM = net debit ~$0.85M, max value $65/spread ($6.5M max) if SNOW > $210 by 6/26.
  - Why are dealers willing to absorb both $180 and $200 strike writes simultaneously? Cross-check phase-4 GEX/vanna structure.
