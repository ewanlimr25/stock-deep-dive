# Phase 1 — Options Flow

**Ticker:** AAPL
**As-of date:** 2026-05-20
**Generated:** 2026-05-20T20:30:00Z
**Upstream phases cited:** phase-0-intake.md

## Summary

AAPL spot anchored around **$299–$302** on 2026-05-20 (`underlying_price` field
from top trades spans 299.09–302.08). Today's single dominant print is a
**$51.6M ask-side sweep of the 2028-01-21 $300 call** (10,115 contracts,
delta 0.59) — an institutional LEAP-length, ATM bullish bet. That print is
partially offset by two large **bid-side** deep-ITM call prints (the
2026-12-18 $200C and 2026-06-18 $190C, both delta ≥ 0.91), which read as
unwinds/rolls of long-stock-replacement positions taken much lower. Critically,
5-day sweep persistence flags AAPL in the **top sweep ticker every session
with `dominant_direction = bearish`** and **$1.054B aggregate sweep premium**,
so today's bullish LEAP is a counter-trend, not a continuation, of the
prevailing 1-week tape.

## Key signals

- **Largest single trade: $51.6M ask-side 300C 2028-01-21 LEAP**, delta 0.586,
  IV 33.2%, gamma 0.003, vega 1.51 — long-dated ATM directional [FLOW:top_premium_trades].
- **Bid-side rolls of ITM 2026 calls:** 200C 12/18/26 for $29.5M (delta 0.91)
  + 190C 6/18/26 for $24.7M (delta 0.96) [FLOW:top_premium_trades]. These
  likely close stock-replacement bullish exposure taken lower, NOT new bearish
  bets — but they do remove a chunk of friendly gamma above spot.
- **5-day sweep persistence: AAPL top ticker, 5/5 sessions, dominant_direction
  bearish, $1.054B aggregate** [FLOW:sweep_persistence]. Multi-day
  institutional bearish flow that today's bullish LEAP does not erase.
- **0DTE expiry pin around $300/$302.5:** 300C 5/20 vol/OI 13.4 ($16.16M
  premium, 132k contracts) + 302.5C 5/20 vol/OI 24.0 ($8.66M, 220k) +
  300P 5/20 vol/OI 27.7 ($4M, 59k) [FLOW:unusual_volume]. Pure gamma /
  expiration mechanics, not directional intent.
- **Fresh small upside spec:** 282.5C 5/27 vol/OI 225.75 ($3.17M),
  270C 2/19/27 vol/OI 28.0 ($2M), 245C 1/15/27 vol/OI 51 ($690k)
  [FLOW:unusual_volume]. Brand-new low-base call positions opening across
  multiple expiries — consistent with the LEAP buyer above.
- **No AAPL rows in `hot_chains_smart_money_flow` (bullish OR bearish, both
  directions filtered to volume ≥ 500)** — index/sector ETFs and NVDA
  dominated the market-wide ask/bid imbalance leaderboard today. AAPL flow
  is large in absolute dollars but not the most lopsided ratio-wise.

## Detailed findings

### Sweeps (ask vs bid)

Ranked by `total_premium` from `options_flow_sweeps` (date=2026-05-20,
min-premium=$100k, top-n=25). All AAPL.

| Rank | Strike/Type | Expiry | Side | Total premium | Size | Trades | avg_price |
|------|-------------|--------|------|---------------|------|--------|-----------|
| 1 | 300 C | 2028-01-21 | **ask** | **$54.11M** | 10,608 | 49 | $51.43 |
| 2 | 200 C | 2026-12-18 | bid | $29.50M | 2,838 | 2 | $105.53 |
| 3 | 190 C | 2026-06-18 | bid | $24.73M | 2,275 | 1 | $108.70 |
| 4 | 300 C | 2026-05-20 (0DTE) | ask | $8.09M | 62,329 | 10,240 | $1.32 |
| 5 | 300 C | 2026-05-20 (0DTE) | bid | $6.64M | 55,954 | 9,172 | $1.23 |
| 6 | 300 C | 2026-05-22 | ask | $5.19M | 17,926 | 3,475 | $2.98 |
| 7 | 302.5 C | 2026-05-20 (0DTE) | ask | $4.33M | 106,398 | 14,237 | $0.46 |
| 8 | 300 P | 2026-08-21 | bid | $3.95M | 3,080 | 136 | $13.10 |
| 9 | 300 C | 2026-05-22 | bid | $3.76M | 13,812 | 2,887 | $2.81 |
| 10 | 300 C | 2027-01-15 | ask | $3.74M | 1,254 | 635 | $29.78 |

**Interpretation.** Excluding 0DTE noise (rows 4–7, 9), the directional
read is:

- Bullish ask-side: $54.1M LEAP 300C 2028, $3.74M LEAP 300C Jan-27,
  $3.12M 300C Jun-26, plus ladders out to 305C 5/29 ($2.40M) and
  297.5C 5/22 ($2.29M). Total ≈ **$70M ask-side calls long-tenor**.
- Bid-side that LOOKS bearish but probably isn't: $29.5M 200C 12/26 +
  $24.7M 190C 6/26 = $54.2M deep-ITM call closes at avg prices > $100
  (delta 0.91+). Treat as **stock-replacement unwind**, not new shorts.
- Genuine bearish prints: $3.95M 300P 8/21 bid + $2.57M 300P 1/15/27 bid +
  $1.92M 0DTE 300P bid. ≈ **$8.4M bearish premium** — small vs LEAP buying.

### New positioning (unusual_volume, vol/OI ≥ 3)

Filtering out 0DTE pin trades, the directional new positions are:

| Strike | Type | Expiry | vol/OI | Total premium | Note |
|--------|------|--------|--------|---------------|------|
| 282.5 | C | 2026-05-27 | **225.75** | $3.17M | Fresh weekly upside [FLOW:unusual_volume] |
| 270 | C | 2027-02-19 | 28.0 | $2.01M | Fresh LEAP-ish bullish [FLOW:unusual_volume] |
| 245 | C | 2027-01-15 | 51.0 | $690k | Deep ITM Jan-27 [FLOW:unusual_volume] |
| 322.5 | C | 2026-06-05 | 16.25 | $6.9k | Cheap upside lotto [FLOW:unusual_volume] |
| 312.5 | C | 2026-06-05 | 7.5 | $61.6k | Upside lotto |
| 370 | C | 2026-07-17 | 6.4 | $48.6k | Far-OTM upside |
| 365 | C | 2027-01-15 | 6.0 | $291k | Far-OTM Jan-27 |
| 285 | P | 2026-06-03 | 11.4 | $19.2k | Small downside hedge |
| 307.5 | P | 2026-05-26 | 59.5 | $85.3k | Very small upside hedge from a vol seller |

Bullish-new-positioning premium dominates ≈ **30:1** vs bearish-new-positioning
once 0DTE is removed.

### Largest premium prints (top 5)

| Time (UTC) | Type | Strike | Expiry | Side | Premium | Δ | IV | Underlying |
|------------|------|--------|--------|------|---------|---|-----|-----------|
| 16:00:43 | C | 300 | 2028-01-21 | ask | $51.59M | 0.586 | 33.2% | 299.09 |
| 16:00:43 | C | 200 | 2026-12-18 | bid | $29.47M | 0.915 | 44.1% | 299.09 |
| 16:00:43 | C | 190 | 2026-06-18 | bid | $24.73M | 0.963 | 97.5% | 299.09 |
| 17:18:39 | C | 315 | 2026-08-21 | ask | $0.99M | 0.389 | 25.9% | 300.86 |
| 17:27:31 | C | 275 | 2026-07-17 | ask | $0.94M | 0.792 | 30.2% | 300.94 |

Three of the top three crossed at **16:00:43 UTC** (12:00:43 ET) on the same
print — strongly suggests a **single coordinated package**: BUY 10,115 LEAP
300C 2028 (ASK), SELL 2,835 deep-ITM 200C 12/26 (BID), SELL 2,275 deep-ITM
190C 6/26 (BID). Net delta ≈ +5,932 (10,115 × 0.59) − 2,593 (2,835 × 0.91) −
2,191 (2,275 × 0.96) = **+1,148 deltas** still net long, but with significant
duration extension (Jun-26/Dec-26 → Jan-28) and theta reduction.

### IV outliers + Greeks

- 250C 5/22/26 avg IV **137%** (max 187%) — deep-OTM call lotto, $1.37M
  premium across 272 contracts, IV likely model artifact (low time value).
  Not directional signal [FLOW:iv_outliers].
- 0DTE 300C IV 114% max 148% — expiration mechanics, ignore.

`greek_screener` (sorted by premium) shows the same top three as
`top_premium_trades` plus a $742.5k **bid-side** 290P 2028-01-21 LEAP
($742.5k, delta −0.39, vega 1.49) — this is the only non-trivial LONG-DATED
PUT activity and is on the BID, i.e. **someone selling 2028 puts** = bullish
(collecting premium that AAPL stays above $290 through Jan-28). Reinforces
the LEAP-buyer thesis.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__options_flow_sweeps` | `{symbol: AAPL, min-premium: 100000, top-n: 25, date: 2026-05-20}` | 25 rows; #1 = $54.1M LEAP 300C 2028 ask |
| `mcp__uw-pp__options_flow_unusual_volume` | `{symbol: AAPL, min-vol-oi-ratio: 3, top-n: 25, date: 2026-05-20}` | 25 rows; bullish-new dominates |
| `mcp__uw-pp__options_flow_top_premium_trades` | `{symbol: AAPL, top-n: 25, date: 2026-05-20}` | 25 rows; top 3 are a coordinated package at 16:00:43 UTC |
| `mcp__uw-pp__options_flow_iv_outliers` | `{symbol: AAPL, top-n: 15, date: 2026-05-20}` | Only 2 rows (250C 5/22 137% IV, 300C 0DTE 114% IV) — both expiration artifacts |
| `mcp__uw-pp__options_flow_greek_screener` | `{symbol: AAPL, top-n: 15, sort-by: premium, date: 2026-05-20}` | Confirms top trades + 2028 290P bid-side ($742k, vol-selling) |
| `mcp__uw-pp__hot_chains_smart_money_flow` | `{direction: bullish, top-n: 10, min-volume: 500, date: 2026-05-20}` | No AAPL rows; VIX/NVDA/XLE/SPY dominate |
| `mcp__uw-pp__hot_chains_smart_money_flow` | `{direction: bearish, top-n: 10, min-volume: 500, date: 2026-05-20}` | No AAPL rows |
| `mcp__uw-pp__hot_chains_sweep_persistence` | `{symbol: AAPL, days: 5, top-n: 20}` | **AAPL 5/5 sessions, dominant_direction=bearish, $1.054B aggregate** |
| `mcp__uw-pp__hot_chains_sweep_ratio` | `{top-n: 15, min-volume: 500, min-sweep-ratio: 0.3, date: 2026-05-20}` | No AAPL rows; small-cap names dominate |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** mixed → modestly bullish for today's tape, but
  **bearish on the 5-day persistence overlay**.
- **Conviction:** 3 / 5. Today's $54M LEAP is high quality (institutional
  ask-side LEAP buy), but it directly contradicts the 5-day persistence
  flag and the two large bid-side deep-ITM call exits.
- **Three things later phases should remember:**
  1. Today's single dominant trade is a **$54.1M ask-side 300C 2028-01-21
     LEAP sweep** at delta 0.59 — looks like a roll from 2026 ITM calls.
  2. **5-day sweep persistence = $1.054B with `dominant_direction =
     bearish`** — this is the structural counter-signal phase 9 must
     reconcile with today's bullish LEAP.
  3. **Spot ≈ $300, key strike = $300, max OI building at 300/302.5** —
     phase 4 GEX must check whether $300 is the gamma flip / pin level.
- **Open questions:**
  - Is the $54M LEAP package a NEW long or a ROLL of an older position
    (the bid-side 190C 6/26 + 200C 12/26 closes suggest roll)? Phase 3 OI
    should show whether 2028 300C OI jumped by ~10k contracts post-2026-05-20.
  - Is dark pool confirming size on the underlying around the LEAP print
    timestamp (16:00:43 UTC = 12:00:43 ET)? Phase 2.
  - Does the 5-day bearish sweep persistence concentrate in puts or in
    bid-side calls? Phase 5 historical_cumulative_premium_flow.
