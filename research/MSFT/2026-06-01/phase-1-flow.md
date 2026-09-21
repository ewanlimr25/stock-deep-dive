# Phase 1 — Options Flow

**Ticker:** MSFT
**As-of date:** 2026-06-01
**Generated:** 2026-06-02T10:58:05Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md

## Summary

The MSFT tape is **net bullish but two-way and normal-magnitude.** Calls dominate
overwhelmingly (P/C 0.256; gross call premium $1.39B vs put $265M; ask-side call
sweeps $274.6M vs essentially zero put buying), yet the *directional* net is
modest — whole-tape `bullish_premium $795.5M` vs `bearish_premium $714.3M` =
**derived net_flow +$81.2M** — because heavy **call writing/overwriting** runs
alongside the buying (bid-side call sweeps $207.97M; the 5-day sweep campaign is
flagged `dominant_direction: mixed`). The most directionally meaningful prints are
a **deep-ITM stock-replacement 410C Jul-17 ($21.2M, delta 0.82)** and a fresh
**480C Jul-2 new position ($21.0M, vol/OI 82)**; much of the rest of the
"unusual volume" is **0DTE pin churn** around 460–465 to discount. Per
phase-0.5 `[CTX: BUSY_NAME_NORMAL_DAY]`, magnitude is discounted and this phase's
downstream confluence is **capped at `+`**.

## Key signals

- Whole-tape **derived net_flow = +$81.2M bullish** (bull $795.5M − bear $714.3M),
  modest vs $1.06B+ directional premium — a *tilt*, not a one-way tape
  `[FLOW:insights_deep_dive]`.
- **Ask-side sweeps are 100% calls: $274.6M** (254,748 contracts, 34,957 trades),
  zero put buying above $100k — but $208.0M of **bid-side call selling** offsets it
  (net call sweeps ≈ +$66.7M) `[FLOW:sweeps]`.
- Largest single prints: **call|ask $90.2M vs call|bid $30.6M vs put $2.6M** — top
  prints lean far more bullish than the whole tape (tip-of-iceberg caveat)
  `[FLOW:top_premium_trades]`.
- **5-day sweep persistence: consistency 1.0, in top-sweeps 5/5 sessions, $2.57B
  total — but `dominant_direction: mixed`** (persistent attention, unclear
  direction) `[FLOW:sweep_persistence]`.
- MSFT is **absent from every market-wide imbalance screen** (smart-money-flow
  bullish & bearish top-10; sweep-ratio top-15) — no single contract is a
  market-leading anomaly, confirming the busy-but-normal read `[FLOW:smart_money_flow]`.

## Detailed findings

### Whole-tape aggregate (read the top-N below against this) `[FLOW:insights_deep_dive]`

From `uw insights deep-dive --symbol MSFT --date 2026-06-01` `.uw_screener`
(same block phase-0.5 used; spot = **$459.77** from top-premium-trades):

| Field | Value |
|-------|-------|
| `call_premium` | $1,392.6M |
| `put_premium` | $264.6M |
| `bullish_premium` | $795.5M |
| `bearish_premium` | $714.3M |
| **derived `net_flow` (bull − bear)** | **+$81.2M** |
| `call_volume` / `put_volume` | 1,292,095 / 331,153 |
| `put_call_ratio` | 0.256 |
| `implied_move` / `implied_move_perc` | 15.36 / **3.33%** |
| `iv_rank` | 73.07 |

The $1.39B gross call premium vs only +$81.2M net directional is the headline:
this is a heavily-trafficked call tape with large two-way (buying *and* writing),
not clean accumulation. Top-N below skews more bullish than this aggregate — by
design it is the iceberg tip.

### Sweeps (ask vs bid) `[FLOW:sweeps]`

| Side | Calls | Puts |
|------|-------|------|
| **Ask (aggressive buying)** | **$274.6M** / 254,748 ctr / 34,957 trades | $0 (none ≥ $100k) |
| **Bid (aggressive selling)** | $208.0M / 223,939 ctr / 36,142 trades | $7.6M / 474 ctr |

Net call sweeps ≈ **+$66.7M** (ask − bid). Top ask-side call sweeps:
500C Aug-21 $53.6M · 450C Jul-17 $26.2M · 450C Jun-18 $16.3M · 480C Jul-2 $15.5M ·
420C Jul-17 $15.0M · 430C Sep-18 $14.3M. The 500C Aug-21 also tops the *bid* side
($20.8M) — same strike bought and sold → genuine two-way, net long.

### New positioning (unusual vol, vol/OI ≥ 3) `[FLOW:unusual_volume]`

By type: **calls $54.3M (7 contracts), puts $19.4M (18 contracts).** Genuinely new
directional position = **480C Jul-2: $21.0M, vol 18,245 vs OI 222 (vol/OI 82).**
Everything else large is **0DTE** (exp 2026-06-01): 465C ($14.0M, v/oi 164), 462.5C
($13.1M, v/oi 343), 460P ($5.2M, v/oi 8257), 467.5C, 465P — pin/gamma churn around
spot, **discounted as non-directional**. The 18 "put" rows are dominated by these
0DTE/near-dated 460–465 puts, not fresh bearish positioning.

### Largest premium prints `[FLOW:top_premium_trades]`

| Time(ET) | Strike | Expiry | Type | Side | Prem | Size | Δ | IV |
|----------|--------|--------|------|------|------|------|---|----|
| 16:07:49 | 410 | 2026-07-17 | call | no_side | $21.2M | 3750 | 0.82 | 38% |
| 19:20:51 | 450 | 2026-07-17 | call | **ask** | $17.9M | 6000 | 0.62 | 35% |
| 17:42:24 | 430 | 2026-09-18 | call | **ask** | $13.2M | 2500 | 0.66 | 38% |
| 19:20:51 | 500 | 2026-08-21 | call | **ask** | $11.1M | 6000 | 0.36 | 37% |
| 13:31:04 | 500 | 2026-08-21 | call | **ask** | $10.5M | 6000 | 0.36 | 36% |
| 16:07:49 | 455 | 2026-07-17 | call | no_side | $9.3M | 3750 | 0.56 | 34% |
| 13:40:47 | 500 | 2026-08-21 | call | **ask** | $9.3M | 5000 | 0.36 | 38% |
| 17:42:24 | 460 | 2026-09-18 | call | bid | $9.0M | 2500 | 0.54 | 36% |

Reads as **bullish call accumulation across the curve**: a deep-ITM stock-
replacement (410C Δ0.82) + ATM directional (450/455C Jul) + OTM upside lottos
(500C Aug Δ0.36, repeated). Aug-21 500C is the most-repeated upside bet.

### IV outliers + Greeks `[FLOW:iv_outliers]` `[FLOW:greek_screener]`

IV-outliers (6 rows) are **all 0DTE / deep-ITM artifacts** (avg_iv 120–224% on
exp-2026-06-01 contracts and a 175C deep-ITM) — **no directional signal**, low
premium. Greek-screener (top-by-premium) just re-lists the call buying above;
delta is being accumulated long via the 410C (Δ0.82) stock-replacement and ATM
Jul calls; gammas small (~0.004–0.007), vega per-contract ~1 (not a vol play).

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|------------------|--------------------------|-----------|
| `uw insights deep-dive --symbol MSFT --date 2026-06-01 --json` | net_flow=+$81.2M ← `.uw_screener.bullish_premium - .bearish_premium`; P/C=0.256 ← `.uw_screener.put_call_ratio` | whole-tape |
| `uw options-flow sweeps --symbol MSFT --side ask --min-premium 100000 --top-n 25 --date 2026-06-01 --json` | call ask=$274.6M ← `.results\|group_by(.option_type)\|map(sum total_premium)` | top-25 |
| `uw options-flow sweeps --symbol MSFT --side bid … --json` | call bid=$208.0M, put bid=$7.6M ← same | top-25 |
| `uw options-flow unusual-volume --symbol MSFT --min-vol-oi-ratio 3 --top-n 25 --date 2026-06-01 --json` | 480C Jul-2 $21.0M v/oi 82 ← `.results\|sort_by(.total_premium)` | top-25 |
| `uw options-flow top-premium-trades --symbol MSFT --top-n 25 --date 2026-06-01 --json` | call\|ask $90.2M, spot=$459.77 ← `.results\|group_by(type+side)`, `.results[0].underlying_price` | top-25 |
| `uw options-flow iv-outliers --symbol MSFT --top-n 15 --date 2026-06-01 --json` | all 0DTE/ITM artifacts ← `.results` | 6 |
| `uw options-flow greek-screener --symbol MSFT --top-n 15 --sort-by premium --date 2026-06-01 --json` | 410C Δ0.82 stock-replacement ← `.results\|sort_by(.premium)` | top-8 |
| `uw hot-chains sweep-persistence --days 5 --top-n 20 --symbol MSFT --json` | consistency 1.0, 5/5 sessions, $2.57B, dir=mixed ← `.results[0]` | 1 |
| `uw hot-chains smart-money-flow --direction bullish\|bearish --top-n 10 --min-volume 500 --date 2026-06-01 --json` | no MSFT contracts ← `[.results[]\|select(.option_symbol\|test("^MSFT"))]` = [] | top-10 ea |
| `uw hot-chains sweep-ratio --top-n 15 --min-volume 500 --min-sweep-ratio 0.3 --date 2026-06-01 --json` | no MSFT contracts ← same | top-15 |

## Tool errors

- `uw hot-chains sweep-persistence … --date 2026-06-01` → **`Error: unknown flag:
  --date`**. `sweep-persistence` is a **trailing tool** with no as-of flag; it
  anchors to the latest available date. Because as-of 2026-06-01 **is** the latest
  data date (phase-0), the no-`--date` call returned `dates_covered:
  [2026-06-01, 05-29, 05-28, 05-27, 05-26]` — correct and reproducible *for this
  run only*. Re-ran without `--date`; value used is valid.

## DATA NOTE / CORRECTION

- **Field:** smart-money-flow / sweep-ratio MSFT membership. **First read:** filtered
  on `.ticker`/`.underlying_symbol` → all-null (wrong key). **Corrected:** these tools
  key rows on `.option_symbol`; re-filtered with `select(.option_symbol|test("^MSFT"))`
  → confirmed **[] (MSFT absent from all three top-N)**. No numeric value was
  transcribed from the wrong read.

## Verdict for downstream phases

- **Net bias:** **bullish (tilt), two-way tape** — calls dominate decisively but the
  directional net is modest and writing/selling is heavy.
- **Conviction: 3/5** (moderate). Capped, not raised: magnitude is normal for the
  name (`[CTX: BUSY_NAME_NORMAL_DAY]`), direction is clean but the 5-day campaign is
  `mixed` and no contract leads any market imbalance screen.
- **Three datapoints later phases must remember:**
  1. **net_flow +$81.2M** bullish but only ~+0.6% of the $1.39B gross call tape — a
     tilt overlaid on large two-way call activity (writing + buying).
  2. **Strike map:** spot **$459.77**; aggressive call buying clusters **450–500**
     (Jun–Sep), anchored by **500C Aug-21** (most-repeated) and a **410C Jul-17
     stock-replacement (Δ0.82)** + fresh **480C Jul-2**. 0DTE pin churn at 460–465.
  3. **Persistence high, direction mixed** (sweep-persistence 5/5, $2.57B, mixed) —
     attention is real and sticky; conviction in *direction* is not.
- **Open questions:** Is dark pool (phase-2) confirming accumulation under this call
  buying, or is the underlying being distributed while calls are bought? Do the OI
  walls (phase-3) sit at 450/460/500 — confirming the strike map — and is the
  bid-side call selling dealer-driven (phase-4 GEX)?
