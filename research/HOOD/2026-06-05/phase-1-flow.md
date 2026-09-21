# Phase 1 — Options Flow

**Ticker:** HOOD
**As-of date:** 2026-06-05
**Generated:** 2026-06-07T12:20:00-04:00
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md

## Summary

HOOD's 2026-06-05 options tape is **bearish by decomposition, not by put
volume**: whole-tape net flow is −$13.58M (bearish 0.6th universe percentile per
phase-0.5-context.md `[CTX:]`), and the bearishness is carried by **calls sold
into the bid** (−$11.23M net call aggressor premium ex-0DTE) plus **puts bought
at the ask** (+$3.02M net) — both legs point the same way. The single loudest
signal is persistence: HOOD has been a top-sweeper **5 of the last 5 sessions
with dominant_direction "bearish", consistency_score 1.0, and $317.8M total
sweep premium** [FLOW:sweep_persistence]. Magnitude caveat: the net imbalance is
only ~12% of a $113.5M tape, the stock already fell intraday (prints show
underlying 85.76→79.70 before closing 82.47, −~4% from the morning high), and
phase-0.5 licenses direction-based — not size-based — confluence.

## Key signals

- **5/5-session bearish sweep campaign**: `sessions_in_top`=5,
  `dominant_direction`="bearish", `consistency_score`=1.0,
  `total_sweep_premium`=$317,794,122 [FLOW:sweep_persistence] (trailing tool,
  latest-anchored = as-of here)
- **Calls net-sold ex-0DTE**: ask $27.76M vs bid $38.99M → −$11.23M; contracts
  86,759 ask vs 122,921 bid [FLOW:aggressor_ex0dte DUCKDB]
- **Puts net-bought ex-0DTE**: ask $12.87M vs bid $9.85M → +$3.02M; net
  delta-notional all legs ≈ **−$0.09B** [FLOW:delta_notional DUCKDB]
- **Whole-tape**: bullish_premium $44.04M vs bearish_premium $57.61M → derived
  net_flow **−$13,575,317**; P/C volume ratio 0.40 (call-heavy volume, bearish
  premium — the call volume is two-way, the aggression is one-way)
  [FLOW:insights_deep_dive]
- **Largest bearish put prints at ask**: Sep-18 70P $1.20M swept at ask
  (OTM, ~15% below spot); Sep-18 100P $0.66M at ask (deep ITM, delta −0.61,
  stock-short proxy); Jun-12 75P $0.58M [FLOW:sweeps ask]
- **No HOOD contract in market-wide smart-money top-10 (either direction) or
  sweep-ratio top-15** — no single chain qualified; the bearishness is spread
  across strikes, not one conviction print [FLOW:smart_money_flow, sweep_ratio]

## Detailed findings

### Whole-tape aggregate (read top-N against this) [FLOW:insights_deep_dive]

| Field | Value |
|---|---|
| `call_premium` / `put_premium` | $81,433,934 / $32,060,841 |
| `bullish_premium` / `bearish_premium` | $44,036,989 / $57,612,306 |
| derived `net_flow` (bullish−bearish; no net_flow key in block) | **−$13,575,317** |
| `call_volume` / `put_volume` / `put_call_ratio` | 393,858 / 156,714 / 0.40 |
| `iv_rank` / `implied_move_perc` | 49.59 / 0.727% |

[CTX:] carry-over: unusual_verdict = GENUINELY_UNUSUAL **in direction only**
(vol-vs-avg ≥2× failed; self total-premium pctile 74.4) — size-based `++` is
not licensed for phases 1–2; direction-based evidence is.

### DTE composition (0DTE noise is small) [FLOW:dte_buckets DUCKDB]

| DTE bucket | Call prem $M | Put prem $M |
|---|---|---|
| 0–1DTE | 7.20 | 6.29 |
| 2–7DTE | 15.53 | 6.28 |
| 8–45DTE | **24.10** | 8.20 |
| 46–180DTE | 11.77 | 7.00 |
| LEAP | **22.83** | 4.29 |

0–1DTE is only $13.5M of the $113.5M tape — the direction read is not pin
noise. Action concentrates in 8–45DTE (the sold June/July calls) and LEAPs.

### Sweeps (≥$100k aggregated lines, top-25 per side) [FLOW:sweeps]

- **Ask side** (n=25): $15.43M total — calls $11.83M (20 lines) vs puts $3.60M
  (5 lines). Largest: Jun-18 90C $1.31M; Sep-18 70P $1.20M; Jun-12 90C $1.02M;
  Jun-12 88C $0.81M; Jun-12 70C $0.78M (deep ITM); 0DTE Jun-05 84P $0.70M;
  Sep-18 100P $0.66M (ITM). LEAP call buying present: 2027-06 80C $0.55M,
  2027-03 60C $0.49M, 2027-01 100C $0.43M.
- **Bid side** (n=25): $19.30M total — **calls $18.47M (24 of 25 lines)** vs
  puts $0.83M (1 line). Largest sold calls: 2027-06 100C $1.14M; Jun-18 90C
  $1.13M; Jul-17 100C $1.07M; Jun-12 85C $1.05M; Jun-12 87C $1.04M; 2027-01 80C
  $0.99M. Call selling spans weeklies → LEAPs.
- Net top-25 sweep read: calls −$6.64M, puts +$2.77M — same sign as the
  whole-tape §A cut. The 85–90 strikes (Jun-12/Jun-18) traded heavily on BOTH
  sides; the bid side is bigger nearly everywhere.

### New positioning (vol/OI ≥3, n=19) [FLOW:unusual_volume]

- Jun-12 90C: vol 18,126 vs OI 5,339 (3.4×), $2.08M premium — biggest new-money
  chain; two-way per sweeps (both ask $1.02M and bid $0.86M lines exist).
- Jun-12 86C $1.38M (5.0×), Jun-12 84C $1.13M (4.7×), Jun-12 82C $1.03M (4.2×).
- **Jun-12 55P: vol 16,035 vs OI 1,641 (9.8×) but only $48,200 premium** —
  teenies (avg ~$0.03); disaster-lottery or spread leg, not conviction.
- Jun-12 75P $0.71M (5.0×) — real new put money 9% below spot.
- Jul-10 85C $0.84M (10.5×, OI 150) — new ATM call money mid-July.

### Largest premium prints (top single trades) [FLOW:top_premium_trades]

| Time (UTC) | Contract | Premium | Side | Note |
|---|---|---|---|---|
| 15:44 | Jun-12 87C | $599,690 | bid | sold, 3,295×, und 83.10 |
| 14:04 | Jun-12 86C | $572,000 | bid | sold, 2,200×, und 84.26 |
| 19:13 | Jul-17 75P | $470,000 | mid | 1,000×, und 80.75 — ambiguous |
| 17:52 | 2027-03 60C | $466,590 | ask | bought, Δ0.78 deep-ITM LEAP |
| 19:55 | 2027-06 100C | $466,250 | bid | sold OTM LEAP, und 82.24 |
| 13:46 | Sep-18 100P | $440,200 | ask | bought, Δ−0.61 ITM put |
| 19:26 | 0DTE 87P | $385,206 | bid | Δ−0.97 — EOD close-out |
| 17:56 | Jul-10 85C | $365,044 | bid | sold (row duplicated in feed ×2) |

Underlying fell through the prints: 85.76 (14:19) → 83.10 (15:44) → 80.40
(17:52) → 79.70 (18:46), close 82.47 [FLOW:screener.close]. Call sellers were
selling into weakness all day, not just at the high. Data quirk: two rows
(Jul-10 85C, Jun-12 70C) appear twice verbatim in top-premium-trades — treated
as one print each for narrative (totals unaffected: aggregates come from §A).

### IV outliers + Greeks [FLOW:iv_outliers, greek_screener]

- IV outliers are NOT concentrated in OTM puts: the list is mostly 0DTE strikes
  and far-OTM lottery calls (120–170 strikes, ≤$8k premium each) — noise.
- Substantive entries: Jun-12 55P (16,035 vol, avg IV 1.34 — the teenies
  above); deep-ITM 55C Jun-18/Jun-26 ($384k/$327k, IV ~1.2, ~130 contracts) —
  stock-replacement-style ITM call buys, modestly bullish.
- Greek-screener top-8 = the same prints as top-premium-trades (premium-sorted);
  largest vega print: 2027-06 100C sold (vega 0.33/contract).

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw options-flow sweeps --symbol HOOD --side ask --min-premium 100000 --top-n 25 --date 2026-06-05 --json` | $15.43M total ← `[.results[].total_premium]\|add`; call/put split via `select(.option_type)` | top-25 |
| same, `--side bid` | $19.30M; calls $18.47M (24/25) ← same paths | top-25 |
| `uw options-flow unusual-volume --symbol HOOD --min-vol-oi-ratio 3 --top-n 25 --date 2026-06-05 --json` | 19 rows; Jun-12 90C vol 18,126/OI 5,339 ← `.results[]` | 19 |
| `uw options-flow top-premium-trades --symbol HOOD --top-n 25 --date 2026-06-05 --json` | table above ← `.results[]` (premium, side, executed_at) | top-25 |
| `uw options-flow iv-outliers --symbol HOOD --top-n 15 --date 2026-06-05 --json` | mostly lottery noise ← `.results[]` | 15 |
| `uw options-flow greek-screener --symbol HOOD --top-n 15 --sort-by premium --date 2026-06-05 --json` | vega/delta on top prints ← `.results[:8]` | 8 |
| `uw hot-chains smart-money-flow --direction bullish|bearish --top-n 10 --min-volume 500 --date 2026-06-05 --json` | no HOOD rows ← `select(.option_symbol\|startswith("HOOD"))` (empty) | top-10 ×2 |
| `uw hot-chains sweep-persistence --days 5 --top-n 20 --symbol HOOD --json` | 5/5 bearish, $317,794,122, consistency 1.0 ← `.results[0]` | 1 |
| `uw hot-chains sweep-ratio --top-n 15 --min-volume 500 --min-sweep-ratio 0.3 --date 2026-06-05 --json` | no HOOD rows ← same OPRA selector (empty) | top-15 |
| `uw insights deep-dive --symbol HOOD --date 2026-06-05 --json` | aggregate table ← `.uw_screener.*`; net_flow derived | block |
| DuckDB §A (bot-eod-report-2026-06-05.parquet) | aggressor ×6 + DTE×type ← SQL above | whole tape |
| `uw screener bullish-bearish --direction bearish …` (HOOD row) | close 82.47 ← `.results[] \| select(.ticker=="HOOD") \| .close` | 1 |

## Tool errors

(none — first smart-money/sweep-ratio jq used wrong field names
(`underlying_symbol`/`ticker` absent in hot-chains rows); re-probed and
re-filtered on `option_symbol` OPRA prefix before recording the empty result.)

## DATA NOTE / CORRECTION

- **Sector taxonomy conflict**: UW screener tags HOOD `sector`="Technology";
  Finviz (`fz`) classifies HOOD as Financial (brokers). Phase-0.5's sector
  group-by used UW's field, so HOOD itself sat inside the "Technology 22/50
  bearish" count — its "one of only two financials being sold" line is corrected
  in phase-0.5's DATA NOTE. Known caveat: UW's sector field is unreliable.
- Duplicate rows in top-premium-trades (Jul-10 85C, Jun-12 70C) noted above.

## Verdict for downstream phases

- **Bias from this phase:** **bearish** (decomposed: call supply + put demand,
  both aggressor-confirmed, 5-session persistence)
- **Conviction:** 4 (persistence + two-leg alignment; capped from 5 because net
  imbalance is ~12% of tape, no single smart-money conviction print, and the
  move already ran −4% intraday)
- **Three datapoints later phases must remember:**
  1. `sweep_persistence`: 5/5 sessions bearish-dominant, $317.8M cumulative
     sweep premium, consistency 1.0 — this is a *campaign*, not one day.
  2. Ex-0DTE aggressor split: calls −$11.23M / puts +$3.02M / net delta-notional
     ≈ −$90M `[FLOW:… DUCKDB]` — the P/C 0.40 is two-way volume, not bullishness.
  3. Strike geography: heavy two-way 85–90 calls Jun-12/Jun-18 (sold harder than
     bought), put demand at 75 (Jun-12, Jul-17) and Sep 70/100 — watch 75–80 as
     the put shelf and 85–90 as the call ceiling for phases 3/4.
- **Open questions:** Is dark pool confirming distribution (phase 2)? Are the
  85–90 sold calls building OI walls (phase 3)? What news made HOOD fall ~4%
  intraday on the day (phase 6)?
