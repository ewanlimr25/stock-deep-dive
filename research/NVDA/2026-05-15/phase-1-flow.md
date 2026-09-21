# Phase 1 — Options Flow

**Ticker:** NVDA
**As-of date:** 2026-05-15 (OPEX Friday — heavy 0DTE pin activity expected)
**Spot reference:** ~$228 (from top_premium_trades `underlying_price`)
**Upstream phases cited:** phase-0-intake.md
**Generated:** 2026-05-17T17:02Z

## Summary

NVDA tape is **mildly bullish with strong LEAP accumulation** but the
near-term picture is dominated by **OPEX-week pin behavior around the
227.5–230 zone**. Net premium leans long (call premium > put premium on the
top 25), with two clean signatures: (1) institutional LEAP call buying in
Dec-2027 / Jan-2028 / Dec-2028 expirations, and (2) what looks like an
options-overlay manager closing 11/2026 puts and Jan-2028 puts on the bid
(i.e., taking off protection — bullish meta-signal). 0DTE flow is high-vol /
low-conviction and should not drive directional thesis.

## Key signals

- **Largest sweep:** `NVDA 217.5C 0DTE` — **$37.06M premium, ASK side, 39,381
  contracts, 329 trades** `[FLOW:options_flow_sweeps]`. Avg price $10.39 →
  this is synthetic long stock for the day (delta ~0.88), not directional
  speculation. Discount.
- **LEAP accumulation:** `NVDA 230C 2027-12-17` **$11.65M block (2,000
  contracts, no_side)** + `NVDA 240C 2027-01-15` **$12.3M mid + bid**
  `[FLOW:top_premium_trades]`. Delta 0.5–0.65, vega 1.09 → genuine
  long-duration bullish positioning.
- **Far OTM long-tail upside bet:** `NVDA 400C 2028-12-15` $6.65M, 2,000
  contracts, no_side, delta 0.38 `[FLOW:top_premium_trades]`. Asymmetric bet
  on multi-year rally.
- **Put-protection closing:** `NVDA 220P 2028-01-21` $3.26M **BID side** +
  `NVDA 230P 2028-01-21` $2.79M BID + `NVDA 210P 2027-06-17` $2.88M BID
  `[FLOW:options_flow_sweeps]`. Reads as institutions REMOVING long-dated
  protection — bullish meta-signal.
- **Persistent activity:** `hot_chains_sweep_persistence` shows NVDA in top
  sweep tickers **5/5 sessions** with **$8.31B cumulative sweep premium**,
  but `dominant_direction: mixed` `[FLOW:hot_chains_sweep_persistence]`.
  High attention, no clean directional consensus from sweeps alone.

## Detailed findings

### Sweeps (ask vs bid, premium, persistence)

Top 5 by premium:

| # | Contract | Side | Premium | Size | Trades | Avg price | Read |
|---|----------|------|---------|------|--------|-----------|------|
| 1 | 217.5C 2026-05-15 (0DTE) | ask | $37.06M | 39,381 | 329 | $10.39 | Synthetic long stock, ITM at expiry — flat directional signal |
| 2 | 185C 2026-06-05 | bid | $26.67M | 6,050 | 43 | $43.99 | Deep ITM, BID side → closing institutional long call |
| 3 | 225C 2026-05-15 (0DTE) | bid | $20.30M | 70,329 | 5,851 | $2.91 | 0DTE pin / closing |
| 4 | 135C 2026-06-18 | bid | $19.38M | 2,072 | 6 | $93.83 | Deep ITM ($228 spot, $135 strike) closing |
| 5 | 135C 0DTE | ask | $19.16M | 2,059 | 11 | $93.01 | Mirror — synthetic stock OR re-opening at near-term |

**Net read:** the BID-side ITM calls are closing long positions (taking
profit); the LEAP rows further down are net buying. Mixed near-term, bullish
long-term.

Persistence: `sweep_persistence` confirms NVDA in top 5/5 sessions with
$8.31B total premium → high institutional attention, mixed direction.

### New positioning (unusual vol, vol/OI ratio)

| Contract | vol/OI | Volume | Premium | Type | Read |
|----------|--------|--------|---------|------|------|
| 227.5C 2026-05-18 | 24.2 | 79,851 | $24.45M | call | Fresh ATM next-week call buildup |
| 230C 2026-05-15 (0DTE) | 9.4 | 562,974 | $38.74M | call | OPEX-day speculation / hedge |
| 227.5C 2026-05-15 (0DTE) | 11.3 | 248,144 | $36.21M | call | Same |
| 225P 2026-05-15 (0DTE) | 14.9 | 250,985 | $20.86M | put | OPEX-day pin behavior |
| 145C 2026-05-22 | 50.3 | 1,207 | $10.01M | call | Deep ITM next-week call, unusual |

Reading the chain: 0DTE and next-Friday strikes 225–232.5 are hot. Next-week
(05-22) calls at 230 ASK $14.4M `[FLOW:options_flow_sweeps]` look like fresh
short-term bullish positioning beyond the OPEX noise.

### Largest premium prints (table)

| Time (UTC) | Contract | Side | Premium | Size | Delta | Read |
|------------|----------|------|---------|------|-------|------|
| 15:38 | 135C 2026-06-18 | bid | $16.51M | 1,764 | 0.96 | Closing deep ITM |
| 15:38 | 135C 0DTE | ask | $16.42M | 1,764 | 0.99 | Roll? Same size, same time → roll from June to 0DTE |
| 19:17 | 230C 2027-12-17 | no_side | $11.65M | 2,000 | 0.63 | **LEAP accumulation** |
| 13:35 | 217.5C 0DTE | ask | $10.27M | 10,000 | 0.88 | Synthetic stock |
| 14:52 | 230P 2026-11-20 | no_side | $8.81M | 3,000 | -0.46 | Six-month put — protection or directional bear |
| 19:17 | 400C 2028-12-15 | no_side | $6.65M | 2,000 | 0.38 | **LEAP upside lottery** |
| 14:59 | 250C 2026-09-18 | no_side | $3.27M | 2,000 | 0.41 | Sep call buildup |

### IV outliers + Greeks

Top IV outliers are all 0DTE calls (15.97 max IV) — these are end-of-day
0DTE artifacts (last hour, deep OTM going to zero), not signal. Filter and
ignore.

Greek screener confirms the LEAP names carry the meaningful vega:
- `230C 2027-12-17` vega 1.09 — directional vol exposure
- `400C 2028-12-15` vega 1.40 — convex upside
- `220P 2028-01-21` vega 1.12 — long-dated put (being CLOSED on bid)

### Smart money flow

Filtered to NVDA from the market-wide list: only
`NVDA260515C00217500` appeared (ask_bid_ratio 6.30, net_flow +33,130,
premium $46.2M `[FLOW:hot_chains_smart_money_flow]`). Confirms bullish
ask-side bias on the 217.5C — but that contract is 0DTE synthetic stock, so
the smart-money read is muted.

### Sweep ratio

Only one NVDA hit: `NVDA 320C 2026-06-18` sweep_ratio 0.795, premium $107k,
1,801 sweep volume `[FLOW:hot_chains_sweep_ratio]`. Tiny size but bullish
OTM positioning — speculative call buyer reaching for upside.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__options_flow_sweeps` | `symbol=NVDA, date=2026-05-15, min-premium=100000, top-n=25` | 25 rows, $37M top sweep |
| `mcp__uw-pp__options_flow_unusual_volume` | `symbol=NVDA, date=2026-05-15, min-vol-oi-ratio=3, top-n=25` | 25 rows, 562k vol on 0DTE 230C |
| `mcp__uw-pp__options_flow_top_premium_trades` | `symbol=NVDA, date=2026-05-15, top-n=25` | 25 rows, top $16.5M (135C BID close) |
| `mcp__uw-pp__options_flow_iv_outliers` | `symbol=NVDA, date=2026-05-15, top-n=15` | 15 rows, all 0DTE artifacts |
| `mcp__uw-pp__options_flow_greek_screener` | `symbol=NVDA, date=2026-05-15, top-n=15, sort-by=premium` | 15 rows |
| `mcp__uw-pp__hot_chains_smart_money_flow` | `direction=bullish, top-n=15, min-volume=500` | 1 NVDA row (217.5C 0DTE) |
| `mcp__uw-pp__hot_chains_sweep_persistence` | `symbol=NVDA, days=5, top-n=20` | NVDA in top 5/5 sessions, $8.31B premium, mixed direction |
| `mcp__uw-pp__hot_chains_sweep_ratio` | `top-n=25, min-volume=500, min-sweep-ratio=0.3` | 1 NVDA row (320C 06-18) |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** cautiously bullish (LEAP signature dominates;
  near-term pin clouds the picture)
- **Conviction:** 3/5 (high attention, mixed directional reads)
- **Three things later phases must remember:**
  1. **Spot ~$228** with **massive 0DTE pin at 227.5–230** — phase-3 should
     confirm pin in OI; phase-4 should expect ZGL near here.
  2. **LEAP call buying** at 230 / 240 / 400 strikes in Dec 2027 – Dec 2028
     — this is structural bullish; phase-5 cumulative_premium_flow should
     confirm.
  3. **Protective puts being CLOSED** (220P/230P 2028, 210P 2027) on the bid
     — this is an institutional risk-on tilt; phase-7 conviction_matrix
     should reflect (expect DIRECTIONAL_LONG or HEDGED_LONG).
- **Open questions:**
  - Is the 230P 2026-11-20 ($8.8M, 3,000 size, no_side) new protection or
    closing? Phase-3 `oi_smart_positioning` may resolve.
  - Is the bullish ask-side flow on 217.5C 0DTE confirmed by dark pool
    accumulation at this level? Phase-2 should answer.
  - Does phase-4 vanna_charm show a squeeze setup that would extend the
    bullish LEAP thesis intraday?
