# Phase 1 — Options Flow

**Ticker:** NVO
**As-of date:** 2026-05-20
**Generated:** 2026-05-20T20:30:00-04:00
**Upstream phases cited:** phase-0-intake.md

## Summary

Today's NVO tape is **decisively bullish for the first time in a week**: a
$1.0M ask-side sweep on Jan 2028 $45 calls (30 trades, 950 contracts,
delta ~0.62) anchors a broader pattern of LEAP call accumulation and put
selling at $45. This contradicts the 5-day sweep persistence label of
"bearish, $9.68M total" — the read is that the multi-day put bid was
absorbed today by a real institutional LEAP buyer. Spot drifted +1.5%
intraday (44.54 → 45.24) while the big tickets hit at $44.83, suggesting
the size was absorbed without leaving offers.

## Key signals

- $1,007,176 ask-side sweep, NVO 2028-01-21 $45C, 30 trades / 950 size, avg fill $10.64 [FLOW:sweeps]
- Two single prints at 14:41 ($402,800) and 14:43 ($337,600) on the same Jan 2028 $45C ask-side — likely the same desk legging into ~$740k of directional LEAP exposure [FLOW:top_premium_trades]
- 5-day sweep persistence ranks NVO with `dominant_direction = bearish`, `total_sweep_premium = $9,681,175`, sessions_in_top = 5/5, consistency = 1.0 — every session this week showed top-table NVO bearish sweeps, until today's flip [FLOW:sweep_persistence]
- $153k Jan 2028 $45P **bid-side** (put sale, bullish) + $30.6k Jan 2028 $45P bid-side = a put-writer is monetizing the same level the call buyer is loading [FLOW:sweeps]
- Bearish counter-flow concentrated in **Dec 2026 $45P** ($120,752 ask + $103,785 mid = ~$224k buying ATM puts that expire just after the U.S. compounded-tirzepatide cliff window) [FLOW:sweeps]
- IV outliers returned empty; smart_money_flow market-wide top-25 contained zero NVO rows in either direction — flow is meaningful but not extreme by ticker rank [FLOW:iv_outliers, FLOW:smart_money_flow]

## Detailed findings

### Sweeps — ask vs bid, premium

| Contract | Side | Premium | Size | Trades | Avg fill | Direction |
|----------|------|---------|------|--------|----------|-----------|
| 2028-01-21 $45C | ask | **$1,007,176** | 950 | 30 | $10.64 | bullish LEAP |
| 2026-05-22 $42C | ask | $219,997 | 762 | 15 | $2.92 | bullish (2DTE deep ITM) |
| 2026-06-18 $45C | no_side | $188,000 | 1,000 | 1 | $1.88 | block, mid-market |
| 2028-01-21 $50C | ask | $176,065 | 204 | 17 | $8.69 | bullish LEAP |
| 2026-07-17 $45C | ask | $173,361 | 594 | 243 | $2.93 | bullish, persistence |
| 2028-01-21 $45P | bid | $153,159 | 170 | 12 | $9.02 | **put sale = bullish** |
| 2026-12-18 $45P | ask | $120,752 | 221 | 76 | $5.42 | bearish |
| 2027-01-15 $50C | ask | $114,694 | 256 | 42 | $4.49 | bullish LEAP |
| 2026-12-18 $45P | mid | $103,785 | 190 | 34 | $5.45 | mixed bearish |

**Net call premium (ask-side bullish only):** $1,007k + $220k + $176k + $173k +
$115k = **$1,691,876** in unambiguously bullish call sweeps.
**Net put premium (ask-side, bearish only):** $120,752.
Bullish premium dollars dominate today's tape 14×.

### New positioning — unusual volume (vol/OI ≥ 3)

| Contract | Vol/OI | Volume | OI | Avg IV |
|----------|--------|--------|-----|--------|
| 2026-06-18 $37P | **88.5×** | 3,010 | 34 | 0.461 |
| 2026-06-05 $42.5P | 8.2× | 246 | 30 | 0.366 |
| 2026-06-18 $51C | 4.5× | 147 | 33 | 0.399 |
| 2026-05-22 $48.5C | 3.96× | 999 | 252 | 0.568 |
| 2026-06-18 $46C | 3.28× | 508 | 155 | 0.392 |

The $37P 06/18 outlier resolves via top_premium_trades: a **single 3,000-lot
print at $0.19 with side = no_side, delta −0.068** [FLOW:top_premium_trades].
That is a deep OTM tail with $57k notional — consistent with a short put leg
of a put-credit spread or a cheap tail purchase, not a directional fear bet.

### Largest premium prints (top 5)

| Time (UTC) | Strike/Expiry | Side | Premium | Size | Δ | IV | Spot |
|-----------:|--------------|------|--------:|-----:|----|-----|------|
| 14:41:27 | 2028-01 $45C | ask | $402,800 | 380 | 0.62 | 0.464 | 44.835 |
| 14:43:42 | 2028-01 $45C | ask | $337,600 | 320 | 0.62 | 0.462 | 44.83 |
| 17:08:51 | 2026-06 $45C | no_side | $188,000 | 1,000 | 0.50 | 0.394 | 44.78 |
| 13:32:16 | 2028-01 $50C | ask | $85,400 | 100 | 0.54 | 0.455 | 44.615 |
| 14:51:32 | 2028-01 $45P | bid | $62,100 | 69 | −0.40 | 0.394 | 44.83 |

Spot drifted $44.54 → $45.24 across the session — the LEAP buyer paid
$10.55–10.64 and sat through a +1.5% afternoon rally that improved their
mark.

### IV outliers + Greeks

- `iv_outliers(min_iv=1.0)` returned **0 rows** — NVO IVs at 39–55% are
  elevated for healthcare but not abnormal. No vol blow-off.
- Greek screener confirms the $1.0M LEAP sweep has **delta 0.62, gamma 0.014,
  vega 0.221** — high vega, modest gamma → buyer is paying for forward
  delta + vol expansion, not gamma scalp. Consistent with a multi-quarter
  thematic re-rating bet (e.g. GLP-1 franchise re-acceleration).

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `options_flow_sweeps` | `{symbol: NVO, date: 2026-05-20, min_premium: 100000, top_n: 25}` | 9 rows, $1.0M LEAP call ask dominates |
| `options_flow_unusual_volume` | `{symbol: NVO, date: 2026-05-20, min_vol_oi_ratio: 3, top_n: 25}` | 5 rows; top is 88.5× $37P block |
| `options_flow_top_premium_trades` | `{symbol: NVO, date: 2026-05-20, top_n: 25}` | 25 rows; top 2 are same-strike Jan 2028 $45C buys 2 min apart |
| `options_flow_iv_outliers` | `{symbol: NVO, date: 2026-05-20, top_n: 15}` | 0 rows (no extreme IV) |
| `options_flow_greek_screener` | `{symbol: NVO, date: 2026-05-20, sort: premium, top_n: 15}` | LEAP $45C has δ0.62 γ0.014 ν0.221 |
| `hot_chains_smart_money_flow` | `{direction: bullish, min_volume: 500, top_n: 25}` | No NVO in market-wide top 25 |
| `hot_chains_smart_money_flow` | `{direction: bearish, min_volume: 500, top_n: 25}` | No NVO in market-wide top 25 |
| `hot_chains_sweep_persistence` | `{symbol: NVO, days: 5, top_n: 25}` | NVO 5/5 sessions, dominant_direction=bearish, $9.68M total |
| `hot_chains_sweep_ratio` | `{date: 2026-05-20, min_volume: 500, min_sweep_ratio: 0.3}` | No NVO contracts in top 25 (sweep ratio dispersed) |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** **bullish today, bearish 5-day trailing → potential inflection day**
- **Conviction:** 4/5 on today's print (single-day signal is unambiguous in premium dollars and Greek profile); 2/5 confidence the 1-day flip is sustainable without confirmation from dark pool and OI.
- **Three things later phases must remember:**
  1. A single (or coordinated) institutional desk bought ~$1.0M of Jan 2028 $45C ask-side and sold the matching $45P bid-side — a **synthetic long structure** around the $45 line. Look in phase 3 OI for an unusual OI build at Jan 2028 $45 strike.
  2. NVO was the **#1 bearish-persistence ticker for 5 sessions running** with $9.68M total sweep premium until today. Phase 2 dark pool must answer: did dealers/shorts cover today, or did a new buyer simply step in front?
  3. Dec 2026 $45P retains a $224k aggregate bid that is fundamentally **on the opposite side** of the LEAP synthetic — the bearish thesis hasn't been fully discharged, just outweighed. The $45 strike is the disputed line.
- **Open questions:**
  - Is the LEAP buyer hedging an underlying short, or initiating? Phase 2 + Phase 3 (OI delta on 2028-01 $45 strike) will tell.
  - Are dealers short gamma at $45 (which would force buying on rallies)? Phase 4 GEX.
  - Is implied vol elevated relative to realized? Phase 5 VRP.
