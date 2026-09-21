# Phase 1 — Options Flow

**Ticker:** NOW
**As-of date:** 2026-05-27
**Generated:** 2026-05-28T12:18:00Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md

## Summary

The NOW tape is **decisively call-tilted and bullish across the entire term
structure** — whole-tape call premium $59.4M vs put $17.2M (~3.4:1; P/C 0.284),
and stripped of 0–1DTE pin noise the net **delta-notional is +$0.36bn long**
(`[FLOW:delta_notional DUCKDB]`). Ask-side sweeps are a uniform wall of calls
from 5/29 through Jan-2028 LEAPs, and the largest premium *bucket* is LEAP calls
($19.5M). The one genuine counter-signal: the three biggest *single* prints are
long-dated puts (100P Jun-27 $3.2M, 100P Sep-26 $1.8M, 90P Jan-27 $1.5M, all
`no_side`) — but they total only ~$6.6M and −$0.02bn delta, so they do **not**
flip the net-bullish read; they are the key ambiguity for phases 2–3 to resolve.

## Key signals

- Whole-tape call premium **$59.4M** vs put **$17.2M**, net_flow **+$5.0M**, P/C **0.284** `[FLOW:insights_deep_dive]`
- Net **delta-notional +$0.36bn** ex-0DTE (calls +$0.46bn / puts −$0.10bn) `[FLOW:delta_notional DUCKDB]`
- Ask-side sweeps: **25 of 25 are calls** — top 105C 5/29 $1.15M, 110C 6/18 $771k, 100C Jan-28 LEAP $679k `[FLOW:sweeps ask]`
- **Calls dominate every DTE bucket** — LEAP $19.5M, 46–180DTE $16.5M, 8–45DTE $15.0M, 2–7DTE $8.4M (puts ≤$7.5M in each) `[FLOW:dte_bucket DUCKDB]`
- Counter-signal: 3 largest single prints are long-dated puts ($6.6M, `no_side`) — ambiguous hedge vs CSP `[FLOW:top_premium_trades]`

## Detailed findings

### Whole-tape aggregate (read everything below against this) `[FLOW:insights_deep_dive]`

| Field | Value |
|-------|-------|
| call_premium | $59,404,332 |
| put_premium | $17,222,133 |
| bullish_premium | $31,983,917 |
| bearish_premium | $26,968,958 |
| net_flow (bull−bear) | +$5,014,959 |
| put_call_ratio | 0.284 |
| call_volume / put_volume | 127,501 / 36,202 |

Call premium is 3.4:1 over puts and net_flow is positive. Per phase-0.5
`[CTX:]`, this is the **99.4th universe percentile on net-direction** and **81st
self-percentile** — genuinely unusual *directionally*, but volume is 0.9× average
(`vol_confirmed=NO`), so this is steady accumulation, not a catalyst blowout.

### Aggressor & delta-notional, ex-0DTE (DuckDB §A — resolves the top-N tension)

| type | side | trades | prem $M | delta-notional $bn |
|------|------|--------|---------|--------------------|
| call | ask | 15,062 | 26.52 | +0.21 |
| call | bid | 11,928 | 23.00 | +0.18 |
| call | mid | 5,206 | 9.89 | +0.07 |
| put | ask | 3,561 | 3.97 | −0.03 |
| put | bid | 4,021 | 5.47 | −0.04 |
| put | mid | 1,689 | 1.24 | −0.01 |
| put | no_side | 3 | 6.55 | −0.02 |

`[FLOW:aggressor_ex0dte DUCKDB]` Net delta-notional **+$0.36bn long**. Ask-side
calls ($26.5M) lead bid-side ($23.0M) by only ~$3.5M — aggressive buying but with
meaningful two-way (some call writing/closing on the bid), so not a one-sided
stampede. The 3 `no_side` put blocks = the $6.55M long-dated puts below.

### Sweeps (ask vs bid) `[FLOW:sweeps]`

- **Ask-side (25/25 calls):** 105C 5/29 $1.15M · 110C 6/18 $771k · 110C 7/17 $760k
  · **100C Jan-2028 LEAP $679k** · 110C 12/18 $644k · 100C Jan-2027 $636k · 120C 7/17 $594k …
  A continuous call wall across near-term + LEAP tenors.
- **Bid-side (also call-led):** 100C 7/17 $1.5M · 150C Jan-28 $1.2M · 105C 5/29 $697k
  · 110C 6/18 $690k · then **90P Jan-27 $540k** (lone put). Bid-side calls =
  likely some writing/rolling; the lone bid put is small.

### Largest premium prints (top-N — the tip of the iceberg) `[FLOW:top_premium_trades]`

| type | strike | expiry | premium | side |
|------|--------|--------|---------|------|
| put | 100 | 2027-06-17 | **$3,210,000** | no_side |
| put | 100 | 2026-09-18 | $1,816,500 | no_side |
| put | 90 | 2027-01-15 | $1,525,000 | no_side |
| call | 100 | 2026-07-17 | $904,800 | bid |
| call | 150 | 2028-01-21 | $689,500 | bid |
| call | 120 | 2026-09-18 | $350,260 | bid |
| call | 186/190 | 2028-01-21 | $175k/$169k | bid/ask |

**Interpretation:** the three largest prints are long-dated, $90–100-strike puts
(ATM-to-OTM on a $102 stock) executed `no_side` (block/floor — aggressor
unknown). On a 3.4:1 call-heavy tape these are either (a) **protective puts /
collar** against a long position, or (b) **cash-secured put sales** (a holder
happy to own NOW at $90–100, i.e. *bullish* income). They are NOT large enough in
delta (−$0.02bn) to flip the net-long read. Disambiguating them is the #1 job for
phase-2 (dark-pool accumulation?) and phase-3 (is the OI on those strikes growing,
and is there matching stock?). Note the far-OTM upside LEAP calls (186C/190C Jan-28)
— small, but a lottery-ticket bullish tail.

### New positioning, IV outliers, smart-money

- **Unusual volume (vol≫OI):** mostly small puts (88P 7/2 vol684/OI10 $134k; 101P
  5/29 vol2881/OI623 $446k) + a tiny 284C Jun-27 LEAP — no large new directional
  open here. `[FLOW:unusual_volume]`
- **IV outliers:** all clustered in 5/29 (0DTE) contracts, both calls and puts at
  IV 1.0–1.6 — **0DTE pin noise; discounted.** `[FLOW:iv_outliers]`
- **Smart-money-flow:** NOW is **outside the top-50** both bullish and bearish — no
  ask/bid imbalance flag from this market-wide tool. `[FLOW:smart_money_flow]`
- **Sweep-persistence (5d):** NOW **appears** on the persistence list (1 row), but
  the CLI returned no detail fields — note presence (some multi-day sweep
  campaign), no quantified count. `[FLOW:sweep_persistence]`

## Tool calls (audit trail)

| Command | Result summary |
|---------|----------------|
| `uw insights deep-dive --symbol NOW --date 2026-05-27` | whole-tape: call $59.4M / put $17.2M, P/C 0.284 |
| `uw options-flow sweeps --symbol NOW --side ask --min-premium 100000` | 25 rows, all calls, top 105C 5/29 $1.15M |
| `uw options-flow sweeps --symbol NOW --side bid` | 25 rows, call-led, 1 put (90P Jan27) |
| `uw options-flow top-premium-trades --symbol NOW` | top 3 prints = long-dated puts (no_side) |
| `uw options-flow unusual-volume --symbol NOW --min-vol-oi-ratio 3` | 5 rows, small puts + tiny LEAP call |
| `uw options-flow iv-outliers --symbol NOW` | all 0DTE 5/29 — pin noise |
| `uw hot-chains smart-money-flow --direction bullish\|bearish` | NOW outside top-50 both sides |
| `uw hot-chains sweep-persistence --days 5 --symbol NOW` | NOW present (1 row, no detail) |
| DuckDB §A aggressor + delta-notional + DTE buckets | net delta-notional +$0.36bn; calls lead every bucket |

## Tool errors

None — all calls returned. (`yahoo_fundamentals` in deep-dive returned HTTP 401,
irrelevant to flow; fundamentals handled in phase-7b.)

## Verdict for downstream

- **Net bias:** **BULLISH** (call premium 3.4:1, net delta-notional +$0.36bn, ask-side call wall across all tenors).
- **Conviction:** **4/5** — bias is unambiguous and structurally consistent across the curve; held below 5 by (a) no volume confirmation (0.9× avg), (b) ask-call only modestly over bid-call, (c) unresolved big put blocks.
- **Three things later phases must remember:**
  1. **+$0.36bn net delta-notional, 3.4:1 call premium across EVERY tenor** (LEAP bucket largest, $19.5M calls) — structural bullish positioning, not a 0DTE blip.
  2. **The 3 largest single prints are long-dated $90–100 puts ($6.6M, `no_side`)** — hedge vs cash-secured-put sale is unresolved; phases 2–3 must disambiguate. They do NOT flip the net read.
  3. **No volume catalyst** (0.9× avg) + two-way call flow → bullish but **low near-term urgency / longer-fuse** setup. The LEAP weighting reinforces a slow-burn institutional thesis.
- **Open questions:** Is the dark pool confirming accumulation under the call buying (phase 2)? Are the put-block strikes ($90/$100) showing growing OI with matching stock = collar, or naked sales (phase 3)? Is the ask-side call wall opening fresh OI or rolling (phase 3)?
