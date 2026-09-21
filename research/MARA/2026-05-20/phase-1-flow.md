# Phase 1 — Options Flow

**Ticker:** MARA
**As-of date:** 2026-05-19 (data EOD; trade date 2026-05-20)
**Generated:** 2026-05-20T00:05:00-04:00
**Upstream phases cited:** phase-0-intake.md

## Summary

Net options flow on MARA leans **modestly bullish** with **mixed** tactical
texture. Six sweeps ≥$100K aggregated to $1.018M of premium, split roughly
60/40 in favor of bullish prints (put-writing at 10P/Sep and 11.5P/May, plus
ask-side call buying in 12C/Jun and 12.5C/May 0DTE) versus call-writing at
13C/Jun. Persistence is the standout: MARA shows up in the top-sweep list in
**5/5** of the last five sessions with cumulative $30.1M sweep premium —
institutional flow has been on this name for a week, not just today.

## Key signals

- 5/5-session sweep persistence, $30.15M aggregate sweep premium, "mixed"
  dominant direction [FLOW:hot_chains_sweep_persistence]
- Largest single sweep is a $367,990 **bid-side put** at 10P 2026-09-18 →
  put-writing = bullish bias on the 4-month horizon [FLOW:options_flow_sweeps]
- Largest single premium trade is a $172,684 **bid-side call** at 13C
  2026-06-18 (size 1,877) → call-writing capping near-term upside at $13
  [FLOW:options_flow_top_premium_trades]
- Most aggressive opening bullish print: 12C 2026-06-18 **ask-side** $147,130
  (size 1,404, 82 trades) [FLOW:options_flow_sweeps]
- Unusual-vol top-of-list: 14.5C 2026-06-18 with vol/OI **15.9x** on 223
  contracts — small premium ($9.7K) but cleanest "new position opening" tape
  [FLOW:options_flow_unusual_volume]
- 0DTE (2026-05-22 expiry) tape is two-sided: $128K bid-side 12C + $107K
  ask-side 12.5C + $114K bid-side 11.5P — gamma scalp / pinning setup, not a
  directional bet [FLOW:options_flow_sweeps]

**Spot anchor:** underlying_price prints intraday ranged $11.56 → $12.48
across the day, closing zone ~$12.30-$12.44 (multiple late-session prints at
$12.40+). This is the spot to use for downstream ITM/OTM tagging.

## Detailed findings

### Sweeps (≥$100K aggregated premium)

| Rank | Strike/Expiry | Type | Side | Premium | Size | Trades | Interpretation |
|------|---------------|------|------|---------|------|--------|----------------|
| 1 | 10P / 2026-09-18 | put | **bid** | $367,990 | 2,957 | 71 | Put-writing → **bullish** (4mo) |
| 2 | 13C / 2026-06-18 | call | **bid** | $251,702 | 2,791 | 107 | Call-writing → **bearish/cap** (1mo) |
| 3 | 12C / 2026-06-18 | call | **ask** | $147,130 | 1,404 | 82 | Long call → **bullish** (1mo) |
| 4 | 12C / 2026-05-22 | call | **bid** | $128,734 | 2,542 | 307 | 0DTE call-write / gamma scalp |
| 5 | 11.5P / 2026-05-22 | put | **bid** | $114,130 | 3,416 | 156 | 0DTE put-write → bullish/pin |
| 6 | 12.5C / 2026-05-22 | call | **ask** | $107,987 | 3,056 | 360 | 0DTE long call → bullish |

**Net premium balance** (bullish ask-call + bid-put vs bearish bid-call +
ask-put within these six prints):
- Bullish: $367,990 + $147,130 + $114,130 + $107,987 = **$737,237**
- Bearish: $251,702 + $128,734 = **$380,436**
- Net bullish: +$356,801 (~66/34 split)

Caveat: the 13C call-write is large ($251K, 2,791 contracts) and at a strike
just $0.70 above spot — could be covered-call writing by holders, not an
outright bearish directional view. Treat as "capping near-term upside to $13"
rather than "shorting MARA".

### New positioning (unusual vol/OI)

Only two contracts cross the vol/OI ≥ 3 threshold for MARA:

| Strike/Expiry | Type | Vol | OI | Vol/OI | Premium | Avg IV |
|---------------|------|-----|----|--------|---------|--------|
| 14.5C / 2026-06-18 | call | 223 | 14 | **15.93** | $9,691 | 88.9% |
| 10.5P / 2026-06-18 | put | 371 | 107 | 3.47 | $19,239 | 81.3% |

Premium is small (combined $29K) but the 14.5C is unambiguously new-position
opening at an OTM strike +$2 above spot. The 10.5P is also new — could be
hedge or downside speculation. Mixed but with a bullish-skew upside-call
opener.

### Largest premium prints (top 5)

| Time | Strike/Expiry | Type | Side | Premium | Δ | IV | Spot |
|------|---------------|------|------|---------|---|----|------|
| 18:02 | 13C / 2026-06-18 | call | bid | $172,684 | 0.46 | 85% | $12.31 |
| 18:04 | 10P / 2026-09-18 | put | bid | $97,539 | -0.25 | 86% | $12.27 |
| 15:07 | 25C / 2027-06-17 | call | bid | $85,120 | 0.35 | 86% | $11.69 |
| 14:53 | 10C / 2026-06-18 | call | **ask** | $61,060 | 0.77 | 88% | $11.71 |
| 19:39 | 15C / 2027-01-15 | call | **ask** | $41,040 | 0.54 | 88% | $12.44 |

The 25C 2027-06-17 bid-side print is a **LEAP closing trade**. Combined with
the 13C call-write, this reads as a holder *trimming long call exposure
into upside and capping at $13* — neutral-to-bullish hold rather than
adding length. Counterbalanced by the 10C/Jun ITM ask-buy (delta 0.77, near
stock-replacement) — different counterparty going *long* synthetic exposure.

### IV outliers + Greek context

Top IV outliers are almost entirely **0DTE 2026-05-22** strikes with absurd
IV reads (2C and 3C show IV >10.0 — these are deep-ITM, low-extrinsic
contracts where the implied vol number is mathematically blown out; ignore
the IV print, look at the volume). Material outliers worth flagging:

- 11.5C/May-22 — vol 1,066, avg IV 109% (0DTE gamma)
- 14C/May-22 — put vol 204, avg IV 116%
- 6P/Jun-18 — vol 1,503 at 134% IV — far-OTM crash hedge appearing in 1,503
  contracts is *unusual for a $12 stock* and worth re-checking in phase 2 for
  dark-pool corroboration

Greek screener confirms the picture: top weighted print by gamma is the
0DTE 11.5P (gamma 0.359), so a meaningful chunk of today's premium is
short-dated gamma — dealer hedging activity, not directional.

### Multi-session persistence

`hot_chains_sweep_persistence(symbol=MARA, days=5)` returns:

```
consistency_score: 1 (max)
sessions_in_top: 5/5
total_sweep_premium: $30,149,457
dominant_direction: mixed
```

This is the single strongest signal in phase 1: **MARA has been in the top
sweep list every session for the last week with $30M of cumulative sweep
premium**. "Mixed" direction tempers conviction on direction but elevates
conviction on *something is happening here*.

### Smart-money flow (market-wide)

MARA does NOT appear in the top-25 market-wide bullish or bearish
smart_money_flow tables. Largest bullish ticker imbalance is in fixed-income
ETFs (IEF, HYG, LQD) and SPY/IWM hedges; largest bearish in VIX call
write-backs and HYG put sells. Crypto-miner peers WULF appears prominently
(WULF 27C bearish $76K bid-side net, WULF 23C bullish $38K ask-side net) —
**mixed signal in the crypto-miner cohort**, not a uniform sector buy. Worth
remembering in phase 6 (macro/regime).

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__options_flow_sweeps` | `{symbol: MARA, date: 2026-05-19, min_premium: 100000, top_n: 25}` | 6 sweeps ≥ $100K |
| `mcp__uw-pp__options_flow_unusual_volume` | `{symbol: MARA, date: 2026-05-19, min_vol_oi_ratio: 3, top_n: 25}` | 2 contracts (14.5C vol/OI 15.9) |
| `mcp__uw-pp__options_flow_top_premium_trades` | `{symbol: MARA, date: 2026-05-19, top_n: 25}` | 25 rows; top is 13C/Jun bid $173K |
| `mcp__uw-pp__options_flow_iv_outliers` | `{symbol: MARA, date: 2026-05-19, top_n: 15}` | 15 rows; mostly 0DTE noise + 6P/Jun crash hedge |
| `mcp__uw-pp__options_flow_greek_screener` | `{symbol: MARA, date: 2026-05-19, sort_by: premium, top_n: 15}` | Matches top_premium; 0DTE gamma dominant |
| `mcp__uw-pp__hot_chains_smart_money_flow` | `{date: 2026-05-19, direction: bullish, top_n: 25, min_volume: 500}` | MARA absent from market-wide top-25 |
| `mcp__uw-pp__hot_chains_smart_money_flow` | `{date: 2026-05-19, direction: bearish, top_n: 25, min_volume: 500}` | MARA absent |
| `mcp__uw-pp__hot_chains_sweep_persistence` | `{symbol: MARA, days: 5, top_n: 25}` | MARA 5/5 sessions, $30.1M, mixed |
| `mcp__uw-pp__hot_chains_sweep_ratio` | `{date: 2026-05-19, min_volume: 500, min_sweep_ratio: 0.3, top_n: 25}` | MARA absent from market-wide top-25 high-sweep-ratio |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** modestly bullish, mixed near-term
- **Conviction:** 3/5 — persistence is 5/5 (strong), but the same-day
  ask/bid split is 66/34 (not overwhelming) and includes large call-writing
- **Three things later phases must remember:**
  1. **Spot ≈ $12.30-$12.44 on 2026-05-19 close.** Use this for all
     ITM/OTM tagging in phase 4 (GEX, gamma flip) and phase 9 (strike
     selection).
  2. **Persistence is the headline.** Phase 7 (insights) and phase 10
     (audit) should weight 5/5 sweep-persistence as the most reliable signal
     here, more than today's same-day flow imbalance.
  3. **Two-sided structure:** holders are call-writing at $13 (cap) while
     new buyers are taking the $12C/Jun ask and writing $10P/Sep. The trade
     range implied by the tape is roughly **$10 floor (puts written) → $13
     ceiling (calls written)**, with someone betting on a break above $14.50
     by Jun OPEX. Phase 4 should check if dealer gamma supports that range.
- **Open questions:**
  - Is dark-pool buying confirming the $10P put-write (i.e., are holders also
    accumulating shares at the same level)?
  - Does the OI map (phase 3) show the 13C call-write as a *new* short
    position or a *roll* from a closed lower-strike position?
  - Where is the gamma flip relative to $12.30 spot? (phase 4)
