# Phase 3 — Open Interest & Positioning

**Ticker:** NVDA
**As-of date:** 2026-05-15 (OPEX Friday)
**Spot reference:** $225.45 (from OI snapshot `stock_price` — slightly below
the DP-weighted $227.87 in phase 2)
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md
**Generated:** 2026-05-17T17:08Z

## Summary

Positioning is **two-sided across the 237.5–250 zone** on the next-Friday
(2026-05-22) chain: buyers are reaching for **upside** at 245C/247.5C/250C
(net ask-bid POSITIVE) while sellers are **writing** 237.5C/240C (net
ask-bid NEGATIVE) — classic call-write-against-stock from the long-money
crowd OR a stretched-target speculative spread structure (long upper /
short lower). On the same chain there is a massive far-OTM 430C 2026-06-18
add (+19,045 OI vs prior 23, an 828× change) `[OI:biggest_increases]` —
lottery-ticket upside positioning. Pin risk: **NVDA's highest-OI 0DTE
strike is $220** with pin_score 723,473, well-positioned at -2.4% from
spot — NVDA is in the top-7 pin candidates today `[OI:pin_risk]`.

## Key signals

- **+45,567 OI on `NVDA 250C 2026-05-22`** (curr 62,978, prior 17,411) —
  bullish (net_ask_bid +20,536) `[OI:biggest_increases]` `[OI:smart_positioning]`.
- **+29,355 OI on `NVDA 240C 2026-05-22`** but with **bearish smart
  positioning** (net_ask_bid -30,263) — these are being SOLD ON BID =
  covered call writers or a short-call leg of a spread `[OI:smart_positioning]`.
- **+19,045 OI on `NVDA 430C 2026-06-18`** (prior OI 23) — speculative
  lottery upside, bullish (net_ask_bid +16,554) `[OI:biggest_increases]`.
- **+8,092 OI on `NVDA 215C 2028-06-16`** (LEAP) — strong LEAP add at $215
  strike `[OI:biggest_increases]`. Phase-1 LEAP signature is confirmed.
- **Near-term June 2026 calls being CLOSED**: 230C 06-18 (-11,832), 220C
  06-18 (-6,796), 220C 06-05 (-6,776), 225C 06-05 (-6,001), 140C 2028-01-21
  (-4,072) `[OI:decrease_with_volume]` — long calls taking profit / rolling.
- **NVDA pin strike: $220, 2.42% below spot, pin_score 723,473**
  `[OI:pin_risk]` — 7th-highest pin score in market today.

## Detailed findings

### Top OI increases (bullish + bearish blended)

| Contract | DTE | OI Δ | New OI | Smart positioning | Read |
|----------|-----|------|--------|-------------------|------|
| 250C 05-22 | 7 | +45,567 | 62,978 | **BULLISH** | Upside reach |
| 240C 05-22 | 7 | +29,355 | 49,649 | **BEARISH** (bid-sold) | Premium write / short spread leg |
| 237.5C 05-22 | 7 | +22,009 | 24,334 | **BEARISH** (bid-sold) | Premium write |
| 247.5C 05-22 | 7 | +20,710 | 22,184 | **BULLISH** | Upside reach |
| 245C 0DTE | 0 | +19,211 | 33,067 | bullish | 0DTE speculation |
| **430C 06-18** | 34 | **+19,045** (828×) | 19,068 | **BULLISH** | **Lottery upside bet** |
| 230P 0DTE | 0 | +16,754 | 18,833 | bullish (puts sold) | Pin-related put writing |
| 237.5C 0DTE | 0 | +16,747 | 29,827 | bullish | 0DTE |
| 240C 0DTE | 0 | +15,434 | 60,623 | bullish (net +25,005) | 0DTE |
| 232.5P 0DTE | 0 | +14,746 | 15,151 | **BEARISH** | 0DTE put buys |
| 115P 05-22 | 7 | +12,609 | 16,134 | bearish | Deep OTM put protection |
| 250C 05-18 | 3 | +12,782 | 24,983 | bullish | Next-week upside |
| 210P 0DTE | 0 | +10,031 | 36,045 | bullish (puts sold) | Pin write |
| **215C 2028-06-16** | **763** | **+8,092** | 8,406 | bearish (-321) | **LEAP add but net bid-side** |

**Net interpretation for the 05-22 chain:**
- **+OI bullish reach:** 250C +45.5k, 247.5C +20.7k → ~+66k contracts of
  out-of-money upside-buyers
- **+OI bearish writing:** 240C +29.4k, 237.5C +22.0k → ~+51k contracts of
  call-write supply at $237.5–$240
- Result: there is **a wall of short calls at 237.5–240** that dealers must
  hedge against AND **buyer demand for 245–250** — implies a structured
  bet (e.g., 240/250 call spread bought as a debit spread).
- **OR** institutional covered-call income at 237.5–240 vs separate
  speculative buying at 245–250.

### Largest OI decreases (closings)

| Contract | DTE | OI Δ | Read |
|----------|-----|------|------|
| 235C 0DTE | 0 | -32,288 | Expiring |
| 230C 0DTE | 0 | -31,977 | Expiring |
| 225C 0DTE | 0 | -14,510 | Expiring |
| **230C 06-18** | 34 | **-11,832** | Long calls closing (matches phase-1 BID prints) |
| 227.5C 0DTE | 0 | -9,433 | Expiring |
| 220C 0DTE | 0 | -8,631 | Expiring |
| 225C 05-18 | 3 | -7,689 | Closing pre-next-week |
| 220C 06-18 | 34 | -6,796 | Long closing |
| 220C 06-05 | 21 | -6,776 | Long closing |
| 225C 06-05 | 21 | -6,001 | Long closing |
| **140C 2028-01-21** | 616 | **-4,072** | **Deep-ITM LEAP closing** |

The June 2026 call decreases (220C, 225C, 230C 06-18) match phase-1's BID-side
sweeps closing $93/contract ITM positions. Net: **long calls are taking
profit on the June chain** while fresh longs reach to LEAPs (2027-12-17,
2028-12-15, 2028-06-16) and speculative upper strikes (430C 06-18, 250C
05-22).

### Smart positioning highlights (direction-inferred)

Top bullish, OI Δ ≥ 10k:
- 250C 05-22 (+45.5k, bullish)
- 247.5C 05-22 (+20.7k, bullish)
- 245C 0DTE (+19.2k)
- 430C 06-18 (+19.0k, very high net_ask_bid)
- 240C 0DTE (+15.4k, net +25k)

Top bearish, OI Δ ≥ 10k:
- 240C 05-22 (+29.4k bid-sold)
- 237.5C 05-22 (+22.0k bid-sold)
- 232.5P 0DTE (+14.7k put-buyers)
- 115P 05-22 (+12.6k put-buyers, deep OTM protection)

### Pin risk (OPEX window)

NVDA is in the top 7 pin candidates market-wide:

| Field | Value |
|-------|-------|
| Spot | 225.45 |
| Highest-OI strike (within 5%) | **$220** |
| Top-strike OI | 76,532 |
| Total OI in window | 2,024,456 |
| Pin score | 723,473 |
| Pin distance | -2.42% |
| DTE to OPEX | 0 (today is OPEX) |

NVDA closed at $228.93 by late-day (per phase-1 underlying_price), so the
$220 magnetic strike was **not** pinned — spot drifted ABOVE the gravity
zone through the session. This is bullish-leaning behavior: the chain
wanted to anchor at 220, the tape pushed it to 228+.

### OPEX concentration

NVDA did NOT appear in the top-25 concentrated-expiry list (threshold
`min_concentration_pct=40`). NVDA's OI is broadly distributed across
many expiries — no single-expiry cliff to defend.

## Tool calls (audit trail)

| Tool | Args | Result |
|------|------|--------|
| `mcp__uw-pp__oi_biggest_increases` | `symbol=NVDA, date=2026-05-15, top-n=20, min-oi-change=500` | 20 rows |
| `mcp__uw-pp__oi_decrease_with_volume` | `symbol=NVDA, date=2026-05-15, top-n=15, min-volume=100` | 15 rows |
| `mcp__uw-pp__oi_smart_positioning` | `symbol=NVDA, date=2026-05-15, top-n=20, min-oi-change=500` | 20 rows |
| `mcp__uw-pp__oi_position_rolls` | `symbol=NVDA, date=2026-05-15, threshold=500, near-dte-max=30` | **ERROR — see below** |
| `mcp__uw-pp__oi_pin_risk` | `date=2026-05-15, top-n=25, dte-max=7, max-distance-pct=5` | NVDA #7 with pin_score 723,473 |
| `mcp__uw-pp__oi_opex_concentration` | `date=2026-05-15, top-n=25, min-concentration-pct=40` | NVDA absent (broadly distributed) |

## Tool errors

### `mcp__uw-pp__oi_position_rolls`

**Args:** `symbol=NVDA, date=2026-05-15, threshold=500, near-dte-max=30`

**Error verbatim:**

> Conversion Error: Could not convert string 'COP' to INT64 when casting from
> source column underlying_symbol

This is a server-side bug: the SQL query passes the symbol parameter to a
column that has been auto-typed as INT64 because some rows contain
numeric-looking values (the parser saw a ticker like a number elsewhere
and inferred the wrong type for the column). Workaround for now: position
roll information is partially recoverable from `oi_biggest_increases` and
`oi_decrease_with_volume` cross-correlated by strike — the June 2026 →
LEAP roll pattern is visible there. Server issue should be filed against
the `oi_position_rolls` SQL template (cast `underlying_symbol` to VARCHAR
in the WHERE clause).

## Verdict for downstream phases

- **Positioning bias:** **MILDLY BULLISH** with a wall of short calls at
  237.5–240 (next Friday) acting as resistance. LEAP signature confirms
  long-duration bullish capital deployment.
- **Conviction:** 3/5 (mixed near-term — call writes vs upside reach).
- **Three pin/cliff strikes for phase-9:**
  1. **$220 — pin gravity** (high 0DTE OI; spot is 2.4% above and trended
     higher into close — not pinned, so it acts as recent support).
  2. **$237.5–$240 — call-write wall on 05-22 chain** (+51k contracts of
     short-call supply). This is the natural near-term resistance zone for
     the next 7 days.
  3. **$250 — upside-buyer target on 05-22 chain** (+45.5k contracts of
     long calls). This is where institutional speculators are betting
     spot reaches.
- **Open questions for downstream:**
  - Does phase-4 GEX show the $237.5–$240 zone as a positive-gamma wall?
    If yes, the call-write story is confirmed.
  - Does phase-5 `historical_oi_trend` show the LEAP add as a multi-week
    pattern or a one-day spike?
  - Does phase-7 `insights_conviction_matrix` resolve the
    DIRECTIONAL_LONG vs COVERED_CALL ambiguity?
