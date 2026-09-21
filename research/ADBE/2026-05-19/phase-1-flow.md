# Phase 1 — Options Flow

**Ticker:** ADBE
**As-of date:** 2026-05-19
**Generated:** 2026-05-19T20:00:00Z
**Upstream phases cited:** phase-0-intake.md

## Summary

ADBE traded $48.0M of sweep premium across five consecutive sessions with a
"mixed" dominant direction `[FLOW:sweep_persistence]` — very persistent
activity but not directionally clean, the classic signature of pre-event
positioning. On 2026-05-19 spot oscillated **$252.11 → $264.06** before
closing near the low ~$252 `[FLOW:top_premium_trades]`. The aggregate
ask-side tape is **bearish-tilted: ~$4.0M ask-side puts bought vs ~$3.8M
ask-side calls bought**, with the heaviest concentration in pre-earnings
**weekly and front-month puts** (May-22 $260P $1.02M, Jun-05 $267.5P
$1.03M-1.37M) `[FLOW:sweeps] [FLOW:unusual_volume]`. Counter-flow shows
long-dated put **selling** in 2027 expirations ($260P Mar-27 $1.03M bid;
$315P Jan-27 $0.67M bid) — institutions monetizing elevated longer-dated IV
while traders pay up for near-dated protection.

## Key signals

- **Sweep persistence top 5/5 sessions, $48.0M aggregate, mixed direction**
  `[FLOW:sweep_persistence]` — ADBE is on every desk's screen this week.
- **Largest single ask-side sweep = bullish 247.5C 2026-05-22 weekly, $1.39M
  / 1,027 contracts / 133 prints** — deep ITM call, looks like delta-1
  proxy or short-cover replacement `[FLOW:sweeps]`.
- **Three largest near-term puts BOUGHT on ASK** total $3.05M:
  Jun-05 $267.5P $1.03M, May-22 $260P $1.02M, Jun-05 $267.5P 2nd line
  $0.66M — all OTM/ATM, all weekly/front-month: **pre-earnings hedge stack**
  `[FLOW:sweeps] [FLOW:top_premium_trades]`.
- **2027 LEAP put SELLING:** $1.03M 2027-03-19 $260P on the **bid** and
  $0.67M 2027-01-15 $315P on the **bid** — institutions short put / cash-
  secured-put behaviour collecting elevated long-dated premium
  `[FLOW:top_premium_trades]`.
- **Net delta of top-25 premium trades = slightly negative** (heavy
  short-dated negative-delta puts outweigh the bid-side put sells which
  carry low gamma exposure for the seller) — short-term bearish skew, longer-
  term mildly bullish `[FLOW:greek_screener]`.
- **IV regime:** near-dated ADBE IV 44-62%, LEAP IV 40-47% — front-end
  premium ~15-20 vol-points above LEAPs, consistent with the next ~30-day
  earnings event being priced in `[FLOW:top_premium_trades]`.

## Detailed findings

### Sweeps — ask vs bid concentration

Top-25 sweeps by aggregated premium, splitting by side (own analysis from
`options_flow_sweeps`):

| Side / type | Ask premium ($M) | Bid premium ($M) | Direction interpretation |
|-------------|------------------|------------------|--------------------------|
| Calls ask (bullish open) | ~3.78 | — | Bullish — payers |
| Calls bid (bearish open / call sells) | — | ~1.79 | Mildly bearish |
| Puts ask (bearish / hedge open) | ~4.00 | — | Bearish / hedge |
| Puts bid (bullish — put sells) | — | ~3.05 | Mildly bullish |

Read: **ASK-side flow tilts bearish** (puts > calls by $0.22M) but the bid
side shows institutions WRITING long-dated puts — a barbell consistent with
"hedge the event, harvest the term-structure premium." Six-month and out
puts (Sep-18 $300P/$320P, Jan-27 $315P, Mar-27 $260P) all show meaningful
bid-side prints, while every front-week put strike shows ask-side
aggression. Net read: **front-end hedging dominates short-term direction**;
LEAP positioning is constructive.

**Notable single sweep:** 2026-05-22 **$247.5 CALL**, ask-side, $1.39M /
1,027 contracts / 133 prints at avg $13.58 (~$253 spot implies this is
~$5.50 ITM, delta ~0.81). At 133 prints this is repeated small-lot
aggression — likely retail / short-cover or systematic replacement, not a
single institutional ticket.

### New positioning (unusual vol / vol_oi_ratio ≥ 3)

| Contract | Type | Vol/OI | Volume | Premium | IV | Read |
|----------|------|--------|--------|---------|----|----- |
| 2026-05-22 $262.5P | put | **65.5** | 131 | $89k | 56% | New OTM put — speculative downside |
| 2026-05-29 $265P | put | **59.5** | 238 | $332k | 45% | New ATM put |
| 2026-05-29 $257.5P | put | 29.0 | 145 | $126k | 44% | New OTM put |
| 2026-06-05 $267.5P | put | **22.0** | 902 | **$1.37M** | 43% | Biggest new-position open of the day — pre-earnings hedge |
| 2026-06-12 $265P | put | 13.1 | 105 | $181k | 54% | New near-ATM put |
| 2026-06-05 $310C | call | 8.3 | 216 | $14k | 47% | Tiny premium, cheap upside lottery |
| 2026-05-22 $265P | put | 6.2 | 309 | $338k | 56% | New ATM put |
| 2027-01-15 $325C | call | 4.5 | 150 | $271k | 48% | LEAP OTM upside bet |
| 2026-05-29 $305C | call | 4.4 | 212 | $7k | 51% | OTM cheap upside |
| 2027-03-19 $260P | put | 4.4 | 500 | **$2.07M** | 41% | Largest single OI build — LEAP put (bid-side = selling, see top trades) |
| 2026-06-18 $265P | put | 4.1 | 224 | $382k | 52% | New near-ATM Jun put |
| 2026-05-29 $257.5C | call | 3.4 | 288 | $305k | 48% | New ATM call |

**Unusual-volume read: 9 of 12 new-position lines are PUTS.** New downside
positioning is the dominant story. Of the new-put openings, $2.4M is in
weekly/front-month strikes (May-22 → Jun-18) while only the $2.07M 2027
$260P is the long-dated OI build — and the largest LEAP-put open is on the
**bid** (option writers, see § Largest premium prints).

### Largest premium prints (top 12 by $premium)

| Time (UTC) | Expiry | Strike | Type | Side | Premium ($) | Size | Δ | IV | Spot |
|------------|--------|--------|------|------|-------------|------|---|----|------|
| 17:24:58 | 2027-03-19 | 260 | P | **bid** | 1,027,500 | 250 | -0.46 | 0.40 | 252.11 |
| 17:16:06 | 2026-05-22 | 260 | P | **ask** | 966,600 | 1,080 | -0.69 | 0.54 | 253.50 |
| 16:26:46 | 2026-06-05 | 267.5 | P | **ask** | 663,000 | 390 | -0.67 | 0.43 | 255.35 |
| 17:22:49 | 2027-01-15 | 350 | C | bid | 630,000 | 500 | 0.26 | 0.47 | 252.60 |
| 17:18:40 | 2027-03-19 | 260 | P | **ask** | 519,125 | 125 | -0.45 | 0.41 | 253.03 |
| 17:18:40 | 2027-03-19 | 260 | P | **ask** | 519,125 | 125 | -0.45 | 0.41 | 253.03 |
| 13:45:55 | 2028-01-21 | 250 | C | bid | 453,000 | 60 | 0.66 | 0.53 | 262.49 |
| 13:45:13 | 2026-07-17 | 230 | C | **ask** | 440,000 | 110 | 0.77 | 0.51 | 261.77 |
| 14:44:55 | 2026-09-18 | 300 | P | bid | 425,085 | 85 | -0.66 | 0.42 | 262.47 |
| 14:23:04 | 2028-01-21 | 165 | P | bid | 352,500 | 250 | -0.14 | 0.45 | 264.06 |
| 17:46:13 | 2027-01-15 | 315 | P | bid | 311,346 | 42 | -0.68 | 0.41 | 255.51 |
| 17:46:13 | 2026-09-18 | 320 | P | ask | 300,468 | 42 | -0.78 | 0.43 | 255.51 |

**Read:** the **biggest single ticket of the day is a long-dated 2027 put
SOLD on the bid for $1.03M** — a fund collecting >$41 of premium per share
against the $260 strike (downside breakeven ~$219 vs spot $252 ≈ -13%).
That seller is short ~17 delta of synthetic long exposure to ADBE through
March 2027. Within 8 minutes the SAME 2027-03-19 $260P strike printed
**$519k ASK twice** — at least two-sided activity. Same buyer/seller
matching is possible (calendar roll, ratio book).

**Pre-earnings weekly puts dominate the front end:** $1.6M of ask-side
weekly/front-month puts (May-22 $260P + Jun-05 $267.5P) — these are
classic "buy-side hedge into June earnings" tickets.

### IV outliers + Greeks

- `options_flow_iv_outliers` with default `min-iv=1.0` returned **0 results**
  for ADBE — no triple-digit IV contracts on the tape. Largest IV in the
  premium-greek screen is the May-22 $247.5C at **0.616 IV** (a near-dated
  ITM call that screens IV-high because of pin sensitivity, not vol bid).
- Total **vega** exposure of top-15 premium trades = +0.91 + 0.91 + 0.91 + …
  dominated by the 2027-03-19 $260P trades (vega 0.91 × 250 contracts × 2
  legs ≈ 455 vega units) and the 2027-01-15 $350C (vega 0.66 × 500 = 330
  vega units). Net **long vega is on the LEAP / call side**, consistent
  with funds short long-dated puts (short vega) and long long-dated
  speculative calls (long vega) — a vol-curve flattener.
- Gamma is concentrated in the weekly puts (May-22 $260P gamma 0.028 × 1,080
  = ~30 gamma), which is the hedge dealer pin risk for the next 3 sessions.

### Smart-money flow (market-wide, ADBE filter)

Both calls ranked top-25 by net bullish/bearish ask-bid imbalance — **ADBE
appears in neither list**. The most aggressive macro flow today is in
SPY/IWM/VIX puts and IEF/HYG/LQD bond hedges. **ADBE-specific imbalance is
below the macro-level threshold of $300+ contracts net flow**, so the tape
is institutional but distributed, not concentrated in one ticker bet
`[FLOW:smart_money_flow]`.

### Multi-day persistence

- ADBE: **5 of 5 most-recent sessions in top sweep universe**, $48.0M total
  premium, `dominant_direction=mixed` `[FLOW:sweep_persistence]`. Five-bagger
  persistence is rare; combined with the mixed-direction tag this confirms a
  **catalyst-driven** book (earnings ≈ mid-June 2026 historically) where
  buyers and sellers are both engaged.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__options_flow_sweeps` | symbol=ADBE, min-premium=100000, top-n=25, date=2026-05-19 | 25 sweeps, total $14.4M premium |
| `mcp__uw-pp__options_flow_unusual_volume` | symbol=ADBE, min-vol-oi-ratio=3, top-n=25, date=2026-05-19 | 12 rows, 9 puts / 3 calls |
| `mcp__uw-pp__options_flow_top_premium_trades` | symbol=ADBE, top-n=25, date=2026-05-19 | 25 prints, ranges $171k–$1.03M |
| `mcp__uw-pp__options_flow_iv_outliers` | symbol=ADBE, top-n=15, date=2026-05-19 | empty (min-iv default 1.0) |
| `mcp__uw-pp__options_flow_greek_screener` | symbol=ADBE, top-n=15, sort-by=premium, date=2026-05-19 | 15 rows, vega concentrated in LEAPs |
| `mcp__uw-pp__hot_chains_smart_money_flow` | direction=bullish, top-n=25, min-volume=300, date=2026-05-19 | market-wide list, ADBE absent |
| `mcp__uw-pp__hot_chains_smart_money_flow` | direction=bearish, top-n=25, min-volume=300, date=2026-05-19 | market-wide list, ADBE absent |
| `mcp__uw-pp__hot_chains_sweep_persistence` | symbol=ADBE, days=5, top-n=20 | ADBE 5/5 sessions, $48.0M, mixed |
| `mcp__uw-pp__hot_chains_sweep_ratio` | top-n=25, min-volume=300, min-sweep-ratio=0.3, date=2026-05-19 | market-wide, ADBE not present |

## Tool errors

None. (Phase-0 fallback from 2026-05-20 → 2026-05-19 noted in phase 0.)

## Verdict for downstream phases

- **Bias from this phase:** **mixed with short-term bearish hedge tilt**.
  Front-end puts are being bought aggressively (event hedge), LEAP puts
  are being SOLD (premium harvest). Net delta of premium tape mildly
  negative; net vega mildly positive on the long-dated side.
- **Conviction:** **3/5** — tape is extremely active and persistent (5/5
  sessions in top sweep universe) but lacks one-sided directional skew.
- **Three things later phases should remember:**
  1. **Earnings event is the catalyst** — every front-end put strike
     (May-22, May-29, Jun-05, Jun-12, Jun-18) shows fresh ATM/OTM put
     opening. Phase 6 should confirm ADBE earnings date; phase 9 should
     timestamp the trade plan relative to that date.
  2. **Largest single ticket of the day = bid-side LEAP put = institution
     SHORT $260 March-27 puts for $1.03M premium** — a structural bullish-
     to-neutral conviction trade (~$219 breakeven, -13% from spot) that
     conflicts with the bearish front-end stack. The audit phase should
     flag this.
  3. **Spot reference $252.11 (last large print) with intraday high $264.06
     — ~$12 range / ~5%.** Front-end IV ~50%, LEAP IV ~41% (vol-curve
     contango ~9 vol-points), which is rich vs typical ADBE non-event IV
     (historical ~28-35%) — phase 5 should confirm IV percentile.
- **Open questions:**
  - Is the front-end put hoarding earnings hedge vs directional? — phase 4
    (term structure) and phase 5 (IV percentile vs realized) settle it.
  - Are dealers short or long gamma at $250/$260? — phase 4 GEX answers.
  - Is dark pool absorbing or distributing in the $250-265 zone? — phase 2.
  - Did the LEAP put seller leave footprints in OI? — phase 3 OI deltas.
