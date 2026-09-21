# Phase 1 — Options Flow

**Ticker:** GOOG
**As-of date:** 2026-06-22
**Generated:** 2026-06-22
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md

## Summary

GOOG's tape is **overwhelmingly call-premium dominated** ($335.6M call vs $83.6M
put, 4.0:1) and call-heavy by volume (P/C 0.388), yet the whole-tape *bullish/bearish*
classification reads modestly **net-bearish at −$23.0M** — a number phase-0.5 flagged
as a universe/self extreme. **Phase 1 resolves that tension: the net-bearish sign is a
classification artifact, not bearish accumulation.** The single largest print is a
**$54.0M deep-ITM 2027-06-17 $250 call SOLD at bid** (Δ0.87), part of a multi-leg
deep-ITM LEAP-call **roll** ($66M of 200/230 calls *bought* at ask vs the $54M 250
*sold*) — quasi-stock, two-sided, and the bid-side sale alone inflates `bearish_premium`.
Stripped to genuine directional flow, **every DTE bucket is call-heavy** and the
**fresh short-dated positioning is clearly bullish-leaning** (near-money 6/26–7/10 call
buying), with only modest LEAP-put hedging. Net read: **MIXED, mild short-term bullish
lean, low conviction** — magnitude is mega-cap-normal (phase-0.5: 1.62× vol, IV rank 40,
not a vol event), the headline prints are a delta-1 roll not a directional bet, and GOOG
is absent from the day's top-10 smart-money imbalance.

## Key signals

- Whole-tape: **call $335.6M vs put $83.6M (4.0:1)**; net_flow **−$23.0M** (bull
  $182.2M − bear $205.2M) — net-bearish sign driven by a LEAP roll, not puts
  `[FLOW:insights_deep_dive]`
- Top print **$54.0M 2027 $250 CALL sold at bid (Δ0.87)** + $66M of 200/230 calls
  bought at ask = **deep-ITM LEAP roll**, quasi-stock `[FLOW:top_premium_trades]`
- **Every DTE bucket call-heavy** — LEAP call $205.2M / put $27.5M; 2-7DTE call
  $25.3M / put $12.2M `[FLOW:dte_bucket DUCKDB]`
- Fresh new positioning (vol/OI≥3) is **near-money calls for 6/26–7/10** (345C
  vol 6,256; 355C vol 6,027; 347.5C vol 5,284) — short-term bullish `[FLOW:unusual_volume]`
- Sweeps **balanced** (ask $94.6M vs bid $99.3M) but **persistent 5/5 sessions,
  $302M, dominant_direction = MIXED** `[FLOW:sweep_persistence]`; GOOG **absent**
  from top-10 smart-money-flow both directions `[FLOW:smart_money_flow]`

## Detailed findings

### Whole-tape aggregate (read top-N against this) `[FLOW:insights_deep_dive]`

| Field | Value |
|-------|-------|
| call_premium | **$335.6M** |
| put_premium | **$83.6M** (call:put = 4.0:1) |
| bullish_premium | $182.2M |
| bearish_premium | $205.2M |
| **net_flow (derived = bull − bear)** | **−$23.04M** |
| call_volume / put_volume | 233,514 / 90,607 |
| put_call_ratio | **0.388** (call-heavy by volume) |
| iv_rank / iv30d | 39.78 / 32.76% |
| implied_move | $9.18 (**2.63%**); next earnings **2026-07-22** (~1mo out — these weeklies are NOT earnings plays) |

**Reconciliation (critical).** call premium is 4× put premium, yet bullish < bearish.
That is only possible because a large slug of the call premium is **call *selling*** —
specifically the $54.0M bid-side 2027 $250 call. The DuckDB aggressor/delta-notional
cut (below) confirms net customer delta is ~flat-to-slightly-short *only because* of
that LEAP-roll sale; it is **not** put accumulation. Phase-0.5's "net-dir bearish
extreme" (0.2 univ / 10.2 self pctile) should be **down-weighted to a mechanical
artifact** by all downstream phases.

### Sweeps (ask vs bid, persistence)

- **ask-side sweep premium $94.62M vs bid-side $99.28M** — near-balanced (slightly
  bid/seller-initiated), no clean directional aggression `[FLOW:sweeps]`.
- Both sides are **call-led**; the biggest sweep lines are the same deep-ITM 2027
  calls (250-bid $54M, 230-ask $38.6M, 200-ask $27.4M).
- `sweep_persistence`: GOOG in top sweep names **5/5 sessions**, `consistency_score
  1.0`, **`total_sweep_premium $301.99M`**, **`dominant_direction "mixed"`** — a real
  multi-day campaign, but two-sided (consistent with rolling, not accumulating)
  `[FLOW:sweep_persistence]`.
- `sweep_ratio` top-15: **GOOG absent**. `smart_money_flow` top-10 bullish AND
  bearish: **GOOG absent both** — no single GOOG contract showed a top-tier ask/bid
  imbalance today `[FLOW:smart_money_flow]`.

### New positioning (unusual vol, vol/OI ≥ 3) — short-term BULLISH `[FLOW:unusual_volume]`

Fresh opening interest is **overwhelmingly near-money CALLS expiring this week (6/26)
and next (7/2, 7/10)**:

| Contract | vol | OI | vol/OI | prem | IV |
|----------|-----|----|--------|------|----|
| 345C 6/26 | 6,256 | 266 | 23.5 | $3.66M | 41.3% |
| 355C 6/26 | 6,027 | 347 | 17.4 | $1.99M | 40.1% |
| 347.5C 6/26 | 5,284 | 73 | 72.4 | $2.79M | 40.1% |
| 342.5C 6/26 | 3,268 | 57 | 57.3 | $2.24M | 41.9% |
| 352.5C 6/26 | 3,018 | 54 | 53.9 | $1.15M | 40.2% |
| 355C 7/10 | 1,971 | 141 | 14.0 | $1.58M | 33.0% |
| 340C 6/26 | 1,701 | 85 | 20.0 | $1.58M | 41.7% |

Puts in the vol/OI≥3 list are small and scattered (317.5P 6/26 $21K; 332.5P 6/26
$172K; 315P 7/31 $119K) — **no fresh put accumulation of size**. Short-dated IVs ~40%
(elevated vs 32.8% iv30d, typical near-dated skew), but `iv-outliers` returned **empty**
— no genuine IV dislocation `[FLOW:iv_outliers]`.

### Largest premium prints (the LEAP roll) `[FLOW:top_premium_trades]` / `[FLOW:greek_screener]`

| Type | Strike | Expiry | Premium | Side | Δ | Read |
|------|--------|--------|---------|------|---|------|
| call | 250 | 2027-06-17 | **$54.0M** | **bid (sold)** | 0.866 | roll: close/sell hi-Δ |
| call | 230 | 2027-06-17 | $38.6M | ask (bought) | 0.900 | roll: open lower strike |
| call | 200 | 2027-06-17 | $19.1M | ask (bought) | 0.940 | roll: open deeper |
| call | 200 | 2027-06-17 | $8.2M | ask (bought) | 0.940 | roll: open deeper |
| put | 350 | 2028-01-21 | $5.67M | no_side | −0.366 | LEAP put hedge |
| put | 400 | 2027-12-17 | $1.38M | bid | −0.471 | LEAP put |
| call | 345 | 2027-01-15 | $1.28M | bid | 0.591 | — |

Top-4 = the 2027-06-17 deep-ITM call complex (Δ 0.87–0.94 → behaves like stock).
$66M *bought* at 200/230 vs $54M *sold* at 250 = net long lower-strike LEAP call delta,
i.e. a **roll down/adjustment of a synthetic-stock position**, not a fresh directional
conviction bet. The handful of LEAP puts ($5.67M Jan-28 350P + smaller) is modest
downside hedging.

### Aggressor & delta-notional split, **excluding 0–1DTE** (DuckDB §A)

```
type  side  trades  prem_m  delta_notional_bn
call  ask   16634   143.80   +0.97
call  bid   25080   172.10   +1.39   ← incl. the $54M 250-call SALE (the roll)
put   ask   12796    33.14   -0.42
put   bid   10095    38.40   -0.39
```
Signed by aggressor, net customer delta ≈ **−0.42bn (calls) − 0.03bn (puts) ≈ −0.45bn**
— a *mild* net-short tilt that is **entirely attributable to the deep-ITM 250-call sale**
in the call-bid bucket. Premium by DTE confirms call dominance in **every** tenor
(LEAP 205/27, 46-180DTE 67/25, 8-45DTE 38/19, 2-7DTE 25/12 call/put $M)
`[FLOW:delta_notional DUCKDB]`, `[FLOW:dte_bucket DUCKDB]`.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← path | Rows |
|------------------|--------------------|------|
| `uw insights deep-dive --symbol GOOG --date 2026-06-22 --json` | call_prem 335.6M, put_prem 83.6M, net_flow −23.04M ← `.uw_screener.bullish_premium-.bearish_premium` | 1 |
| `uw options-flow sweeps --symbol GOOG --side ask --min-premium 100000 --top-n 25 --json` | ask sum $94.62M ← `[.results[].total_premium]\|add` | 25 |
| `uw options-flow sweeps --symbol GOOG --side bid …` | bid sum $99.28M | 25 |
| `uw options-flow unusual-volume --symbol GOOG --min-vol-oi-ratio 3 --top-n 25 --json` | near-money 6/26 calls top of list ← `.results[]` | 25 |
| `uw options-flow top-premium-trades --symbol GOOG --top-n 25 --json` | 250C 2027 $54M side=bid ← `.results[0]` | 25 |
| `uw options-flow iv-outliers --symbol GOOG --top-n 15 --json` | **empty** | 0 |
| `uw options-flow greek-screener --symbol GOOG --top-n 15 --sort-by premium --json` | 250C Δ0.866 ← `.results[0].delta` | 15 |
| `uw hot-chains smart-money-flow --direction bullish/bearish --top-n 10 --min-volume 500 --json` | GOOG absent both ← `select(option_symbol\|test("GOOG"))` | 10+10 |
| `uw hot-chains sweep-persistence --days 5 --top-n 20 --symbol GOOG --json` | $301.99M, 5/5 sessions, mixed ← `.results[]` | 1 |
| `uw hot-chains sweep-ratio --top-n 15 --min-volume 500 --min-sweep-ratio 0.3 --json` | GOOG absent | 15 |
| DuckDB §A (`bot-eod-report-2026-06-22.parquet`) | delta-notional & DTE-bucket split | whole tape |

## Tool errors

- `uw hot-chains sweep-persistence … --date 2026-06-22` → `unknown flag: --date`
  (trailing/multi-day tool — anchors to latest available date, **not** as-of
  reproducible). Re-run **without** `--date` succeeded; the 5-session window ends at
  the latest local date (2026-06-22), so it is as-of-aligned here. No other errors.

## DATA NOTE / CORRECTION

No value was mis-read. Note of *interpretation*, not correction: phase-0.5 reported
net_flow −$23.0M as a directional "bearish extreme" (it is, by the screener's
classification). Phase 1 establishes that sign is **mechanically produced by a $54M
deep-ITM LEAP-call sale (a roll)**, so downstream phases must treat the net-bearish
premium as an **artifact**, not as evidence of bearish positioning.

## Verdict for downstream phases

- **Bias from this phase:** **MIXED**, mild **short-term bullish** lean (fresh
  near-money 6/26–7/10 call buying; calls dominate every tenor). The net-bearish
  *premium* is a LEAP-roll artifact, not bearish intent — **do not** carry it as a
  bearish signal.
- **Conviction:** **2 / 5.** Premium magnitude is real but mega-cap-normal (phase-0.5:
  not a vol event); headline prints are a delta-1 roll, not directional; sweeps
  balanced & "mixed"; GOOG absent from smart-money top-10. Genuine fresh directional
  conviction is modest.
- **Three things later phases must remember:**
  1. **The −$23M net-bearish premium is an artifact** of a $54M deep-ITM 2027 250-call
     sale (LEAP roll). True directional flow is **call-dominated** in every tenor.
  2. **Fresh short-dated positioning is bullish** — heavy near-money call opening for
     6/26–7/10 (345C/347.5C/352.5C/355C), no fresh put accumulation. A 1–3-week
     momentum/upside bet, not earnings (7/22).
  3. **Institutional LEAP presence is large but two-sided** ($302M 5-session sweep
     campaign, "mixed") — a position being *managed/rolled*, with modest LEAP-put
     hedging on top. Quasi-stock delta, slow, low short-term tradeability on its own.
- **Open questions:** Is the dark pool (phase 2) confirming accumulation under the
  call-heavy tape, or distribution? Does OI (phase 3) show the 200/230 2027 calls as
  genuinely *new* (roll-open) vs the 250 closing? Where are the dealer gamma walls
  (phase 3/4) relative to the 6/26 345–355 call cluster?
