# Phase 1 — Options Flow

**Ticker:** BBAI
**As-of date:** 2026-05-29
**Generated:** 2026-05-31 (re-verified against validated JSON)
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md

> **## DATA NOTE.** Figures below are from JSON-validated `uw` output captured via
> scripted gather (each file checked to be real JSON before parsing). Earlier
> ad-hoc drafts of this file contained mis-extracted numbers during a harness
> output-delay window and have been replaced. The read is **net-bearish/divergent**.

## Summary

BBAI closed +6% (~$5.05) but the option tape is **net-bearish by premium and
clearly divergent**. Whole-tape `net_call_premium` is **−$999,867**,
`net_put_premium −$243,572`, and `bearish_premium $6,066,639` > `bullish_premium
$5,310,344`, even though volume is enormous (`call_volume` 259,763, P/C 0.113;
98.6th self-pctile, phase-0.5). The tell is the **side split: both the top-20
premium prints AND the 20 sweeps lean to the BID** — top prints bid $663,554 vs
ask $290,374; sweeps bid $2,542,445 vs ask $2,302,287 — i.e. **calls are being
sold/written, not bought**, with fresh put buying on the side. This is a
distribution/blow-off signature into the rally, not accumulation.

## Key signals

- Whole-tape premium **net-negative**: `net_call_premium −$999,867`,
  `net_put_premium −$243,572`; `bearish_premium $6.07M` > `bullish_premium $5.31M`
  [FLOW:insights_deep_dive]
- **Sweeps (20, all calls, $5,060,621) lean bid**: bid $2,542,445 > ask $2,302,287
  (mid $215,889) → net call *selling* even in the aggressive tape [FLOW:sweeps]
- **Top-20 premium prints lean bid**: call $1,115,958 / put $37,260; bid $663,554 >
  ask $290,374; largest is **call $8 2026-12-18 $343,000 at the BID** (3,500) [FLOW:top_premium_trades]
- Fresh **put buying**: `put $5 2026-06-12 vol 4,262 / OI 280 / vol-OI 15.2 /
  $166,066` (the day's biggest unusual-vol line) [FLOW:unusual_volume]
- DTE mix **BALANCED** (`dte-volume-share`: weeklies 18.7%, monthlies 23.3%, LEAPs
  11.5%); IV high but mid-rank (`iv30d` 102.7%, `iv_rank` 34.39) [FLOW:dte_volume_share]

## Detailed findings

### Whole-tape aggregate (read top-N against this)

| Field | Value |
|-------|-------|
| `call_premium` / `put_premium` | $11,866,705 / $1,082,369 |
| `bullish_premium` / `bearish_premium` | $5,310,344 / **$6,066,639** |
| `net_call_premium` | **−$999,867** (1.4th self-pctile) |
| `net_put_premium` | **−$243,572** |
| `call_volume` / `put_volume` | 259,763 / 29,441 (P/C 0.113) |
| `iv30d` / `iv_rank` / `implied_move` | 102.7% / 34.39 / 6.79% |
| `total_open_interest` / `next_earnings` | 945,694 / 2026-08-10 |

→ Call-heavy by **volume**, but net-negative by **premium** = the signature of
**calls being written/sold** faster than bought. Bearish premium leads.

### Sweeps (`uw options-flow sweeps`, n=20)

- All calls; `total $5,060,621`. Side: **bid $2,542,445 > ask $2,302,287** (mid
  $215,889) → net lean to selling. Largest lines: $5 2028 $442,556 (bid), $5 7/17
  $372,091 (bid), $8 12/18 $359,617 (bid), $5 1/15 $359,038 (bid) — the four
  biggest sweeps are **bid-side calls** (far-dated $5 + the Dec-$8). Ask-side
  sweeps appear at $5 1/15 ($340k), $5 9/18 ($294k), $7 7/17 ($281k).
- Read: there IS aggressive two-way call activity, but the dollar weight is on the
  **bid** → consistent with the negative net call premium (selling/writing).

### Largest premium prints (`uw options-flow top-premium-trades`, n=20)

| type | strike | expiry | premium | side | size |
|------|--------|--------|---------|------|------|
| call | 8 | 2026-12-18 | $343,000 | **bid** | 3,500 |
| call | 7 | 2027-01-15 | $118,125 | mid | 945 |
| call | 7 | 2027-01-15 | $50,850 | bid | 450 |
| call | 5 | 2026-07-17 | $47,725 | bid | 575 |
| call | 5 | 2026-09-18 | $46,500 | ask | 375 |
| call | 6 | 2026-09-18 | $41,760 | ask | 480 |
| call | 5 | 2026-06-12 | $40,877 | bid | 997 |
| put | 5 | 2026-07-17 | $37,260 | bid | 460 |

- Aggregate: call $1,115,958 / put $37,260; **bid $663,554 > ask $290,374** (mid
  $199,290). The biggest dollars are **calls sold at the bid** (led by the $343k
  Dec-$8) → call writing / distribution.

### New positioning / unusual volume (`uw options-flow unusual-volume`)

| type | strike | expiry | OI | vol | vol/OI | premium |
|------|--------|--------|----|-----|--------|---------|
| put | 5.5 | 2026-06-18 | 8 | 372 | 46.5 | $29,056 |
| call | 6.5 | 2026-07-10 | 22 | 468 | 21.3 | $15,728 |
| **put** | **5** | **2026-06-12** | 280 | 4,262 | 15.2 | **$166,066** |
| put | 5 | 2026-05-29 (0DTE) | 353 | 2,495 | 7.1 | $23,362 |
| put | 5 | 2026-06-26 | 36 | 307 | 8.5 | $17,399 |

→ Biggest unusual line is a **$5 put (6/12, $166k)** — fresh downside positioning
at spot. Two-sided footprint, not cleanly bullish.

### Expiry / DTE distribution

- `dte-volume-share`: regime **BALANCED** — weeklies 18.7%, monthlies 23.3%, LEAPs
  11.5%. `expiry-heatmap` premium leaders: **2027-01-15 $2.38M** (98% call), 7/17
  $1.85M, 2028-01-21 $1.78M, 9/18 $1.57M, 6/18 $1.37M — call-dominated across the
  curve, with heavy LEAP premium (ties to phase-3's Jan-2027 OI cliff).

## Tool calls (audit trail)

| Command | Result |
|---------|--------|
| `uw insights deep-dive --symbol BBAI --date 2026-05-29` | net_call_prem −$999,867; bear>bull; PCR 0.113 |
| `uw options-flow sweeps --symbol BBAI --date 2026-05-29` | 20, all calls $5.06M; bid $2.54M > ask $2.30M |
| `uw options-flow top-premium-trades --symbol BBAI --date 2026-05-29 --top-n 20` | call $1.12M; bid $664k > ask $290k; top $343k Dec-$8 bid |
| `uw options-flow unusual-volume --symbol BBAI --date 2026-05-29` | $5 6/12 put $166k top |
| `uw options-flow {expiry-heatmap,dte-volume-share} --symbol BBAI` | LEAP+monthly call-heavy; regime BALANCED |
| screener parquet (signed nets) | net_call_prem −$999,867 / net_put_prem −$243,572 |

## Tool errors

- `uw options-flow hottest-chains` does not exist (correct leaves: sweeps,
  top-premium-trades, unusual-volume, expiry-heatmap, dte-volume-share, …). No
  fabricated values remain in this version.

## Verdict for downstream phases

- **Bias from this phase:** **bearish/divergent** (distribution into the rally)
- **Conviction:** 3/5 — net call premium clearly negative on record volume, **both
  sweeps and top prints lean to the bid (selling)**, fresh $5 put buying; capped at
  `+` by phase-0.5.
- **Three things later phases should remember:**
  1. **Price-up / flow-soft divergence**: +6% close but `net_call_premium
     −$999,867` and bearish > bullish premium — the rally is flow-*unconfirmed*.
  2. Calls are being **written/sold** (bid-leaning sweeps AND top prints, incl
     $343k Dec-$8) — pair this with phase-2 dark-pool buying: the combination reads
     like **accumulation-with-call-overwrite (buy-write)** or distribution; phase-8b
     must adjudicate.
  3. Fresh **$5 put buying ($166k)** + heavy 0DTE churn (5/29 expiry) + rich IV
     (iv30d 102.7%) → respect downside and discount the headline volume.
- **Open questions:** Are dealers long or short gamma at $5 (phase-4 GEX)? Does the
  dark-pool large-tier buying (phase-2) + call selling = a buy-write program? Does
  26% short float (phase-0/7c) still make a $5-break squeeze possible?
