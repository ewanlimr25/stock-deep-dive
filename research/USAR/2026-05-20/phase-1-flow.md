# Phase 1 — Options Flow

**Ticker:** USAR
**As-of date:** 2026-05-20 (effective UW data date: 2026-05-19)
**Generated:** 2026-05-20T09:45:00-04:00
**Upstream phases cited:** phase-0-intake.md

## Summary

USAR's tape on 2026-05-19 is a **conviction tape with crossed signals**: $349k
ask-side put sweeps (6/18 $18P) and a $305k 9/18 $14P print (deep OTM tail
hedge) cohabit with a stack of unusual-volume **calls** in 5/22, 6/5, 6/18 and
7/17 expiries (vol/OI 3.3x–73.7x). Underlying ~$20.40, **sector Basic Materials**.
The single most important standalone signal is from `sweep_persistence`:
USAR has been in the **top-sweep table for 5 of 5 sessions** with cumulative
**$15.49M** sweep premium and `consistency_score=1.0`, dominant direction
"mixed". This is not a one-day flare; this is a multi-week institutional
campaign, but the directional vote remains split.

## Key signals

- **5/5 sessions in top sweep table**, $15.49M cumulative premium,
  consistency=1.0, dominant_direction=mixed
  [FLOW:hot_chains_sweep_persistence]
- **6/18 $18 PUT ask-side sweep: $349,878** premium, 2,807 contracts, 64
  trades — single biggest sweep, BEARISH near-the-money (delta -0.28, IV
  1.01) [FLOW:options_flow_sweeps]
- **9/18 $14 PUT $305,660** premium at MID, 2,108 size — deep-OTM tail hedge,
  delta -0.17, IV 0.99 [FLOW:top_premium_trades]
- **7/17 $19 CALL vol 221 / OI 3 (vol/OI = 73.7x)**, IV 0.99 — fresh
  bullish open position [FLOW:unusual_volume]
- **5/22 expiry call stack**: $20C vol 1486 / OI 241 ($145k), $21C vol 1800 /
  OI 388 ($109k); IV outliers up to **241% on 5/22 $30C** — lottery-style
  bullish positioning 3 days from expiry [FLOW:unusual_volume + iv_outliers]
- **Underlying ~$20.40 intraday range $19.60–$20.75**. Sector tag: **Basic
  Materials**. [FLOW:top_premium_trades]
- **Not in market-wide smart_money_flow top-25** (bullish or bearish) —
  the conviction reads big *relative to USAR's own ADV*, but not on the
  market-wide leaderboard, where ETFs (HYG, IEF, SPY, IWM) and single names
  like POET/WULF dominate. [FLOW:hot_chains_smart_money_flow]

## Detailed findings

### Sweeps (ask vs bid, premium, persistence)

Three sweeps cleared the $100k aggregated-premium threshold:

| Side | Strike | Expiry | DTE | Type | Premium | Size | Trades | Avg Px |
|------|--------|--------|-----|------|---------|------|--------|--------|
| ask  | 18     | 2026-06-18 | 30 | put | $349,878 | 2,807 | 64 | $1.32 |
| mid  | 14     | 2026-09-18 | 122 | put | $318,206 | 2,190 | 6 | $1.52 |
| bid  | 47     | 2028-01-21 | 612 | call | $107,665 | 194 | 2 | $5.53 |

Interpretation:
- The **$18P ask-side sweep** is unambiguous: paying offer, broken into 64
  prints (avg ~44 contracts/print), at delta -0.28 it's an effective
  hedge/directional bet that USAR closes the next ~30 sessions below ~$18
  (-12% from spot). [FLOW:options_flow_sweeps]
- The **$14P at MID** could be either side; given size (2,190) it's most
  likely an opening trade. At delta -0.17 and 122 DTE, this is **tail-hedge
  geometry** — paying ~$1.50 to own a -17% lottery for a -30%+ move.
- The **$47C 2028 LEAP at BID** sold (or sold-to-close) reads as someone
  taking profit / scaling out of way-OTM upside, NOT new bullish opening.
  Tag: stale-position dressing, not flow.

Persistence (`hot_chains_sweep_persistence`, days=5):

> USAR — sessions_in_top: **5**, consistency_score: **1.0**,
> dominant_direction: **mixed**, total_sweep_premium: **$15,492,949**.

Reading: this name has been in the institutional crosshairs for an entire
week. Mixed direction tells us the campaign is not unidirectional — there is
both substantial put and call sweep volume across the window. That matches
today's snapshot.

### New positioning (unusual vol, vol/OI ratio)

All seven entries above the 3.0 vol/OI threshold are **CALLS**:

| Strike | Expiry | DTE | OI | Vol | Vol/OI | Premium | Avg IV |
|--------|--------|-----|----|----|--------|---------|--------|
| 19 C   | 2026-07-17 | 59 | 3 | 221 | **73.7x** | $80,046 | 0.99 |
| 20 C   | 2026-05-22 | 3  | 241 | 1,486 | 6.2x | $144,616 | 1.26 |
| 22 C   | 2026-06-05 | 17 | 79 | 374 | 4.7x | $33,973 | 1.04 |
| 21 C   | 2026-05-22 | 3  | 388 | 1,800 | 4.6x | $108,508 | 1.27 |
| 20.5 C | 2026-05-22 | 3  | 65 | 273 | 4.2x | $19,115 | 1.27 |
| 30 C   | 2026-06-26 | 38 | 79 | 273 | 3.5x | $13,614 | 1.04 |
| 20.5 C | 2026-05-29 | 10 | 32 | 106 | 3.3x | $12,433 | 1.05 |

Note the curious asymmetry: **the bearish premium is in puts seen by
`options_flow_sweeps`** (high contract count, mid-OI strikes), while **the
bullish premium is in calls seen by `options_flow_unusual_volume`** (low-OI
strikes getting new opens). This is consistent with a market in which an
institutional player(s) is **buying downside puts AT premium aggregator,
while retail/momentum buyers are opening near-dated calls** for a binary
event. They may be the same population (a hedged bull), or two different
populations sizing opposite bets.

### Largest premium prints (table: time, strike, expiry, premium, side)

Top 10 single-trade prints (from `options_flow_top_premium_trades`):

| Time (UTC) | Strike/Exp/Type | Premium | Px | Δ | IV | Side | Size |
|-----------|-----------------|---------|------|------|-----|------|------|
| 17:35:34 | $14P 2026-09-18 | $305,660 | 1.45 | -0.17 | 0.99 | mid | 2,108 |
| 17:35:34 | $18P 2026-06-18 | $255,068 | 1.21 | -0.28 | 1.01 | ask | 2,108 |
| 16:25:38 | $47C 2028-01-21 | $107,115 | 5.55 | +0.50 | 1.02 | bid | 193 |
| 18:14:48 | $25C 2027-01-15 | $51,500  | 5.15 | +0.57 | 1.00 | ask | 100 |
| 13:38:23 | $60P 2027-01-15 | $43,626  | 39.66 | -0.92 | 0.78 | bid | 11 |
| 18:23:18 | $30C 2028-01-21 | $39,000  | 7.80 | +0.64 | 0.99 | bid | 50 |
| 19:20:01 | $50P 2028-01-21 | $33,500  | 33.50 | -0.59 | 0.88 | ask | 10 |
| 19:48:28 | $26P 2026-06-05 | $30,400  | 6.08 | -0.93 | 0.77 | ask | 50 |
| 19:48:28 | $26P 2026-05-22 | $29,500  | 5.90 | -0.92 | **1.91** | mid | 50 |
| 19:20:01 | $45P 2028-01-21 | $29,100  | 29.10 | -0.55 | 0.89 | mid | 10 |

**Pattern lock**: the **two largest prints execute at the same second
(17:35:34Z)**, both for **size 2,108**, and constitute the only $250k+ tape
prints of the day. This is a single trader executing a **put structure**,
not two random buys. The most natural read is a **diagonal/calendar put
spread**: short 6/18 $18P (delta -0.28, ask) hedged with long 9/18 $14P
(delta -0.17, mid). Net synthetic: this is a **bearish directional structure
that profits from a slow grind to the $14–18 zone while collecting decay**.
That is far more sophisticated than a simple put buy and revises the read
on the $349k "ask-side put sweep" — it may be **the short leg of a
sophisticated spread**, not an outright bearish bet. Phase 7
(`insights_deep_dive`) and phase 4 (skew) should be cross-referenced before
accepting either interpretation.

The deep-ITM put prints ($45P/$50P/$60P 2028-01-21) are **synthetic-stock
unwinds** (delta-replacement plays). They are not directional bets — when
combined with the matching LEAP call activity, the trader is closing out a
synthetic long stock position. Tag as **portfolio noise, not signal**.

### IV outliers + Greeks

Concentration of IV outliers is overwhelmingly **2026-05-22 expiry**
(3 DTE):

- **$30C 5/22**: avg IV 1.97, max IV **2.42** (242%) — pure lottery
- **$26P 5/22**: avg IV 1.80, max **2.20** — deep ITM lottery (delta -0.92)
- **$28C 5/22**: avg IV 1.83, max 2.38
- **$27C 5/22**: avg IV 1.73, max 1.99
- **$26C 5/22**: avg IV 1.54, max 1.79
- **$24C 5/22**: 525 volume at avg IV 1.44

A 30%+ implied move in 3 sessions on a $20 stock implies the market is
pricing a **binary catalyst** between 5/19 close and 5/22 close. That could
be: earnings, FDA/regulator decision, sector news (Basic Materials), or a
known event-date. **Phase 7 `insights_earnings_play` must check.**

Greek screener (sorted by premium) corroborates the sweeps and adds no
new contracts; the highest-vega prints are the 2028 LEAPs (vega ~0.10), but
their size (10–50 contracts) limits vol-bet interpretation.

### Smart money flow

USAR does **not appear** in the top-25 bullish OR bearish market-wide
`smart_money_flow` rankings on 2026-05-19. Market-wide bullish leadership is
ETFs (HYG, IEF, LQD bullish-call sweeps — bond rally hedges), index puts
(SPY, IWM), and single names POET, WULF, AMZN. Market-wide bearish
leadership is VIX 6/17 calls (massive bid-side hits = vol-supply tape) and
HYG protective puts.

**Read for USAR**: the macro-flow tape is **vol-supply / bonds-grinding** —
risk-on rotation under the surface — which is mildly supportive of bullish
small-cap calls. But USAR's flow is far below the market-wide threshold, so
this is at best supporting context.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__options_flow_sweeps` | symbol=USAR, min-premium=100000, top-n=25, date=2026-05-19 | 3 sweeps, $776k total premium; biggest = $18P 6/18 ask $349k |
| `mcp__uw-pp__options_flow_unusual_volume` | symbol=USAR, min-vol-oi-ratio=3, top-n=25, date=2026-05-19 | 7 contracts, ALL calls; 7/17 $19C 73.7x vol/OI |
| `mcp__uw-pp__options_flow_top_premium_trades` | symbol=USAR, top-n=25, date=2026-05-19 | 25 rows; top 2 = paired 17:35:34Z $14P/$18P size 2108 each |
| `mcp__uw-pp__options_flow_iv_outliers` | symbol=USAR, top-n=15, date=2026-05-19 | 15 rows, 13 in 5/22 expiry, max IV 2.42 on $30C |
| `mcp__uw-pp__options_flow_greek_screener` | symbol=USAR, top-n=15, sort=premium, date=2026-05-19 | mirrors top_premium_trades; vega max 0.10 on 2028 LEAPs |
| `mcp__uw-pp__hot_chains_smart_money_flow` | direction=bullish, top-n=25, min-vol=100, date=2026-05-19 | USAR absent; market-wide ETF-heavy |
| `mcp__uw-pp__hot_chains_smart_money_flow` | direction=bearish, top-n=25, min-vol=100, date=2026-05-19 | USAR absent; VIX & HYG dominate |
| `mcp__uw-pp__hot_chains_sweep_persistence` | symbol=USAR, days=5, top-n=20 | **5/5 sessions, $15.49M cumulative, consistency=1.0, mixed dir** |
| `mcp__uw-pp__hot_chains_sweep_ratio` | top-n=25, min-vol=100, min-sweep-ratio=0.3, date=2026-05-19 | USAR absent in top-25 |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** **MIXED with bearish lean** (institutional
  premium tilts to puts at $18 strike; bullish flow is retail-flavored 5/22
  lotto + thin 7/17 $19C; net $-weighted sentiment ~55/45 bearish).
- **Conviction:** **3/5** — the persistence score is high, but the mixed
  direction caps conviction.
- **Three things later phases must remember:**
  1. **5/22 expiry has implied move ≥30%**, max IV 242% on $30C — a
     **near-dated catalyst window** is being priced. Phase 7 must
     identify what (earnings most likely).
  2. **The "$18P/$14P at 17:35:34Z size 2108" pair is one structured trade,
     not two**; do not double-count as bearish premium. The diagonal-spread
     reading reduces the standalone-bearish weight of the $349k ask sweep
     bucket.
  3. **USAR has been in top sweep table 5/5 sessions, $15.5M cumulative.**
     This is a multi-week institutional campaign, not a one-day flare.
     Whatever the audit concludes, the underlying setup deserves attention.
- **Open questions:**
  - Is there an earnings or regulatory date 2026-05-22 +/-? (Phase 7
    `insights_earnings_play` will answer.)
  - Is dark pool tape confirming the institutional thesis on either side?
    (Phase 2 must check for $20.40 area block prints and overnight tape.)
  - What is the gamma flip price? At spot $20.40 with this much 5/22 OTM
    call interest, dealers may be short gamma — a positive feedback loop
    could ignite if spot pops above $21. (Phase 4 GEX must check.)
  - What is USAR's actual business? "Basic Materials" tag is broad — phase
    6/8 fundamental view needs to land specifics.
