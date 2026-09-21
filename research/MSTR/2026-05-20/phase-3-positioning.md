# Phase 3 — Open Interest & Positioning

**Ticker:** MSTR
**As-of date:** 2026-05-19 (effective)
**Generated:** 2026-05-20T00:15:00Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md

## Summary

MSTR is **3 days from monthly OPEX (Fri 2026-05-22)** and the day's OI tape is
dominated by aggressive *new call positioning at and just above spot*: the
single biggest OI change on the entire chain is the **$170 5/22 call +8,654
contracts of new OI** (current OI 9,457, from 803). The wider OI map shows
heavy call walls at **$180 (34,457 OI) and $190 (37,952 OI)** for 5/22 — a
classic dealer-short-OTM-call structure that should act as gamma resistance.
Put-side, the data is *bullish-leaning*: at the $160P, $175P, and $152.5P
strikes the net flow is **sell-to-open puts** (inferred bullish), while the
$150P and $147P strikes show **buy-to-open** (inferred bearish hedge). Net OI
bias by direction count: **12 bullish vs 8 bearish** strikes among the top-20
OI changes — a moderate, not extreme, bullish positioning skew. MSTR does
**NOT** appear in market-wide `oi_pin_risk` despite being in OPEX week — its
OI is too dispersed across strikes for a clean pin signal.

## Key signals

- **OPEX-week hot strike: $170C 5/22 OI +8,654 (now 9,457)** — clearest single bullish OI signal [OI:biggest_increases, OI:smart_positioning → bullish]
- **Call walls 5/22: $180C (34,457 OI) + $190C (37,952 OI)** — dealer-short OTM call structure, upside gamma resistance [OI:biggest_increases]
- **Put-selling at $160/$175/$152.5** strikes — bullish smart-positioning inference (net bid-side puts = sold to open) [OI:smart_positioning]
- **Bullish-leaning at-the-money call adds**: $165C +2,940, $167.5C +766, $170C +8,654 all infer BULLISH
- **Bearish hedge accumulation**: $150P 5/22 +2,196 ($807k aggregate premium prior); $147P +807; $135P +883 — concentrated 8–15% below spot
- **No pin risk and no same-day position rolls detected** — institutions are not rolling near-DTE structures to longer expiries today

## Detailed findings

### Largest OI increases (top 12 by |OI Δ|)

| Rank | Contract | DTE | OI Δ | Curr OI | Prev ask vol | Prev bid vol | Inferred dir | Read |
|---:|---|---:|---:|---:|---:|---:|---|---|
| 1 | **MSTR 2026-05-22 $170 C** | 3 | **+8,654** | 9,457 | 7,969 | 6,835 | **bullish** | Hot OPEX-week ATM call |
| 2 | MSTR 2026-07-17 $10 P | 59 | +4,980 | 9,930 | 20 | 5,010 | bullish | Far OTM puts sold (~$0.01 avg) = naked premium harvest, bullish bias |
| 3 | MSTR 2026-05-22 $177.5 C | 3 | +3,612 | 5,132 | 2,166 | 2,328 | bearish | Slight bid-side = call-overwrite likely |
| 4 | MSTR 2026-05-22 $165 C | 3 | +2,940 | 3,541 | 5,272 | 2,373 | **bullish** | At-the-money OPEX call buying |
| 5 | MSTR 2026-05-22 $172.5 C | 3 | +2,560 | 2,847 | 656 | 3,002 | bearish | Bid-heavy = call selling / covered |
| 6 | MSTR 2026-05-22 $150 P | 3 | +2,196 | 6,545 | 4,020 | 1,352 | **bearish** | ASK-side put buying = 9% downside hedge |
| 7 | MSTR 2026-05-22 $180 C | 3 | +1,902 | **34,457** | 4,021 | 4,484 | bearish | Mild bid lean — call wall growing slightly |
| 8 | MSTR 2026-05-22 $175 C | 3 | +1,790 | 4,450 | 3,011 | 2,421 | bullish | Slight ask lean — speculation through wall |
| 9 | MSTR 2026-06-18 $175 P | 30 | +1,562 | 3,212 | 246 | 1,517 | **bullish** | Heavy bid = puts SOLD = bullish income |
| 10 | MSTR 2026-05-22 $190 C | 3 | +1,412 | **37,952** | 3,687 | 2,911 | bullish | Ask-side wing call lottery |
| 11 | MSTR 2026-05-29 $152.5 P | 10 | +1,304 | 1,628 | 101 | 1,440 | **bullish** | Bid-heavy = puts SOLD |
| 12 | MSTR 2026-06-18 $35 P | 30 | +672 | 1,249 | 156 | 593 | bullish | Far OTM puts sold (premium harvest) |

Direction count among the **top 20** OI increases:
- **Bullish (12):** $170C, $10P (sold), $165C, $175C, $175P (sold), $190C, $152.5P (sold), $180C 6/5, $167.5C, $160P (sold), $170C 5/29, $35P (sold)
- **Bearish (8):** $177.5C, $172.5C, $150P, $180C, $135P, $125P, $147P, $182.5C

Premium-weighted bias (using `prev_total_premium` proxy):
- Bullish premium proxy: $170C $5.91M + $165C $4.42M + $175C $1.46M + $167.5C $2.05M + $190C $0.47M + $160P (sold) $2.82M + $175P (sold) $3.39M = ~**$20.5M**
- Bearish premium proxy: $177.5C $0.99M + $172.5C $1.03M + $150P $0.81M + $180C $1.53M + $182.5C $0.26M + $147P $0.10M = ~**$4.7M**

Premium-weighted ratio ~ **4:1 in favor of bullish positioning** at the top of the OI change list.

### Closing / roll activity (top 8 by |OI Δ| < 0)

| Contract | DTE | OI Δ | Notes |
|---|---:|---:|---|
| MSTR 2026-05-22 $192.5 C | 3 | -2,092 | OTM call expiring — closed/decayed |
| MSTR 2026-05-22 $185 C | 3 | -1,325 | OTM call closing |
| MSTR 2026-05-22 $120 P | 3 | -917 | Deep OTM put closing (expired-worthless candidate) |
| MSTR 2026-05-22 $212.5 C | 3 | -632 | Wing call closing |
| MSTR 2026-05-22 $115 P | 3 | -614 | Deep OTM put closing |
| MSTR 2026-06-18 $500 C | 30 | -552 | Far-OTM 6/18 lottery call closing |
| MSTR 2026-05-22 $200 C | 3 | -424 | 21% OTM call decay |
| MSTR 2026-05-22 $225 C | 3 | -378 | 36% OTM call closing |

Pattern: **OTM call OI above $185 is shrinking** as we approach OPEX (5/22) while OI in the **$165–$182.5 band is growing**. This is consistent with a *contraction toward the money* — speculators rotating out of dead wings into more realistic strikes. The expanding ATM strikes are the real OPEX-week story.

**Position rolls:** `oi_position_rolls` returned **0 detected rolls** at the 500-contract threshold with `near_dte_max=30`. There is no clear institutional same-day roll signature today. This means the OI buildup at the May 22 expiry is **new positioning**, not legacy positions being rolled in from earlier expiries.

### Smart positioning summary (direction inference)

Aggregating the 20 reports by direction:
- **Bullish strikes** dominate at the 5/22, 5/29 expiries, especially in the **$165–$175 call** band and **$152.5–$175 put-selling** band.
- **Bearish strikes** cluster in the **$135–$150 put-buying** band and the **$172.5–$180 call-selling/overwriting** band.

Interpretation: The market is "long a $165–$170 → $180 call spread structure" with some downside hedging out to $150. **No bearish-conviction signal** — the bearish prints look like *limit-the-upside* (call selling) or *insurance* (put buying 8–10% OTM) rather than directional short.

### Pin risk (OPEX week)

MSTR is NOT in the top-25 `oi_pin_risk` despite being 3 DTE to OPEX. The top pins this week are:
- SPY @ $710 (pin_score 1,854,488)
- HYG @ $78 (pin_score 1,512,476)
- QQQ @ $680
- IWM @ $270
- TLT @ $86
- XLF @ $51
- NVDA @ $220
- AAPL @ $300
- AMZN @ $250
- MSFT @ $420
- TSLA @ $400
- IBIT @ $45 (BTC ETF — 3.51% from spot)

Even though MSTR has large absolute OI (34k+ at $180C, 38k+ at $190C), the OI is dispersed across many strikes and the Ni–Pearson–Poteshman score doesn't flag a dominant magnet. Implication: **no strong pin on Friday's close**; spot can move freely within the $160–$185 band based on news/BTC/macro, NOT toward a single magnet strike.

### OPEX concentration

MSTR did not appear in the top-25 `oi_opex_concentration` list — that screen is dominated by small-cap tickers (MRTN, YCL, PVLA, MAX, RAIL, GBTG...) with 100% OI in one expiry. MSTR's options market is too liquid and diversified across expiries to register on the concentration screen.

### Notable: IBIT pin proximity

`oi_pin_risk` flagged **IBIT (iShares Bitcoin Trust ETF)** at spot $43.48 vs pin strike $45 (3.51% above) for tomorrow's expiry (DTE 1). Because MSTR's thesis is BTC-reflexivity, **IBIT's potential pin at $45 = BTC ~ $107k/$108k** is relevant macro pin risk for MSTR's underlying. Phase-6 should evaluate.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__oi_biggest_increases` | `{symbol:MSTR, date:2026-05-19, top-n:20, min-oi-change:500}` | 20 contracts, top $170C +8,654 |
| `mcp__uw-pp__oi_decrease_with_volume` | `{symbol:MSTR, date:2026-05-19, top-n:15, min-volume:100}` | 15 contracts, top $192.5C -2,092 |
| `mcp__uw-pp__oi_smart_positioning` | `{symbol:MSTR, date:2026-05-19, top-n:20, min-oi-change:500}` | 12 bullish, 8 bearish |
| `mcp__uw-pp__oi_position_rolls` | `{symbol:MSTR, date:2026-05-19, threshold:500, near-dte-max:30}` | 0 rolls detected |
| `mcp__uw-pp__oi_pin_risk` | `{date:2026-05-19, top-n:25, dte-max:7, max-distance-pct:5}` | MSTR not in top-25 (dispersed OI) |
| `mcp__uw-pp__oi_opex_concentration` | `{date:2026-05-19, top-n:25, min-concentration-pct:40}` | MSTR not in top-25 |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** **bullish-leaning OPEX-week positioning**. 12 vs 8 bullish-vs-bearish direction-count among top 20 OI changes; ~4:1 premium-weighted bullish:bearish.
- **Conviction:** **3.5/5** — the $170C +8,654 single-strike print is a real signal, but the call walls at $180 and $190 cap upside; positioning could be tactical OPEX-week bias, not multi-week thesis.
- **Three pin/cliff strikes phase-9 must use:**
  1. **$170 (5/22 weekly):** Day's hottest new OI; +8,654 contracts. **Magnet to spot through Friday.**
  2. **$180 (5/22 weekly):** 34,457 OI **call wall** — upside resistance and dealer-short-gamma cluster (phase 4 to confirm gamma sign).
  3. **$150 (5/22 weekly):** Building put wall (+2,196 OI today, total 6,545); downside hedge level matching ~9% OTM and below all the dark-pool clusters in phase-2.
- **Open questions:**
  - Is the $170C +8,654 OI build a *naked-long-call* speculation, or part of a **call-spread/diagonal** structure (with $180C overwrite)? Phase-7 (insights composite) and phase-4 (dealer gamma) will help confirm.
  - Are the $150P / $147P put buyers the SAME desks as the IV-outlier wing-tail buyers in phase-1 (June $31–$49 puts)? If yes, this is a coordinated multi-strike tail-hedge campaign — phase-7 should test.
  - The $190 5/22 call OI of 37,952 is HUGE. Is this stale or recent? It only added 1,412 today, so most is legacy — but it's still a relevant gamma node phase-4 must price.
