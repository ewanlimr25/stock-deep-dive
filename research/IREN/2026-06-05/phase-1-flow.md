# Phase 1 — Options Flow

**Ticker:** IREN
**As-of date:** 2026-06-05
**Generated:** 2026-06-07T00:52Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md

## Summary

Today's IREN tape is **net bearish, driven by selling in the long-dated call
complex rather than aggressive put buying** — whole-tape net_flow −$18.83M
(derived: bullish_premium $72.37M − bearish_premium $91.21M), confirming the
phase-0.5 `[CTX:]` verdict (GENUINELY_UNUSUAL bearish, 0.0 self-history pctile,
see phase-0.5-context.md §Verdict). Ex-0-1DTE, calls were net SOLD −$24.3M
(ask $36.50M vs bid $60.77M) and net aggressor delta-notional was ≈ **−$98M**
[FLOW:aggressor_ex0dte DUCKDB] — yet this lands against a 5/5-session
**bullish** sweep-persistence campaign totaling $339.9M [FLOW:sweep_persistence],
so the day reads as **profit-taking/de-risking inside an ongoing bullish
campaign**, on a session where the stock flushed 55.94 → 51.57 intraday and
V-recovered to close 54.35.

## Key signals

- **Bid-side sweep premium 2× ask-side**: $49.80M (n=25) vs $24.59M (n=25) —
  premium is being *collected from* sellers hitting bids, led by Jan-2027 call
  selling: 70C $6.05M, 45C $3.49M, 110C $2.90M, 100C $2.20M [FLOW:sweeps side=bid].
- **Largest print of the day is bullish-unsigned**: 110C 21-Jan-2028, 4,000
  contracts @ $18.70 = **$7.48M**, side `no_side` (cross/mid), delta 0.573 →
  ≈ $12.6M delta-notional, 14:11:40Z @ underlying 55.20 [FLOW:top_premium_trades].
- **Roll, not exit, in Jan-27**: 45C SOLD $3.31M (bid) + 75C BOUGHT $1.95M (ask),
  identical timestamp 14:17:35Z and identical size 1,413 — a roll UP that locks
  gains but keeps upside [FLOW:top_premium_trades].
- **Vol-selling pin bet**: 55P 06/12 bid 6,759× ($3.16M) + 56C 06/12 bid 6,759×
  ($1.51M), same stamp 19:27:57Z — a ~$4.7M short strangle at 55/56 for next
  week [FLOW:top_premium_trades].
- **5-day sweep persistence is BULLISH**: sessions_in_top 5/5,
  dominant_direction "bullish", consistency_score 1.0, total_sweep_premium
  $339,924,997 [FLOW:sweep_persistence] — today's bearish skew is one session
  against that backdrop.

## Detailed findings

### Whole-tape aggregate (read top-N against this)

[FLOW:insights_deep_dive], jq `.uw_screener`:
| Field | Value |
|---|---|
| call_premium / put_premium | $124,223,791 / $70,031,179 |
| bullish_premium / bearish_premium | $72,372,345 / $91,205,132 |
| **derived net_flow** (bullish − bearish) | **−$18,832,787** |
| call_volume / put_volume | 270,818 / 247,561 |
| put_call_ratio | 0.91 |
| iv_rank / implied_move_perc | 48.17 / 0.963% |

Call premium exceeds put premium 1.8:1 yet the tape is net *bearish* — the
calls are trading at the **bid**. The top-N below is the tip (top-25 premium
prints = $45.2M of a ~$194M premium day); direction comes from the aggregate +
the §A aggressor cut.

### Aggressor split ex-0-1DTE (DuckDB §A — strips expiry-day noise)

[FLOW:aggressor_ex0dte DUCKDB]:
| type | side | trades | contracts | prem $M | δ-notional $bn |
|---|---|---|---|---|---|
| call | ask | 9,072 | 55,071 | 36.50 | +0.112 |
| call | bid | 14,951 | 104,546 | 60.77 | −0.200 |
| call | mid | 3,124 | 28,174 | 12.71 | +0.046 |
| call | no_side | 3 | 7,200 | 11.09 | +0.022 |
| put | ask | 12,405 | 112,539 | 24.46 | −0.106 |
| put | bid | 7,311 | 58,430 | 21.31 | +0.096 |
| put | mid | 2,316 | 12,692 | 5.59 | −0.019 |

Net calls −$24.3M (sold); net puts +$3.2M (bought). **Net signed aggressor
delta-notional ≈ −$98M** (ask−bid legs). The bearish read survives the 0DTE
strip — it is not pin noise.

### Premium by DTE bucket [FLOW:dte_buckets DUCKDB]

| bucket | call $M | put $M |
|---|---|---|
| 0-1DTE | 3.15 | 18.68 |
| 2-7DTE | 7.66 | 18.96 |
| 8-45DTE | 20.06 | 14.85 |
| 46-180DTE | 22.41 | 12.44 |
| **LEAP** | **70.94** | 5.10 |

The action is in LEAPs (37% of all premium) — and per the sweeps split, that
LEAP call premium trades net at the bid. Front end (≤7DTE) is put-dominated.

### Sweeps (ask vs bid)

- **Ask-side (n=25, Σ$24.59M)** [FLOW:sweeps side=ask]: bullish LEAP buying —
  110C 06/17/2027 $2.38M (1,766×, 153 trades), 75C 01/2027 $2.23M, 70C 01/2027
  $1.94M, 50C 09/2028 $0.95M — but also front-end put BUYING: 53P 06/12 $1.43M,
  45P 06/12 $1.30M (15,703 contracts, 1,586 trades — small-lot heavy), 48P
  06/12 $1.26M, 50P 08/21 $0.92M.
- **Bid-side (n=25, Σ$49.80M)** [FLOW:sweeps side=bid]: Jan-27 call selling
  (70C $6.05M/4,229×, 45C $3.49M, 110C $2.90M, 100C $2.20M), 70C 12/18 $2.17M,
  plus 0DTE deep-ITM put closes (65P $5.60M, 62P $4.40M @ 18:41Z, both 4,043×,
  underlying 51.57 — mechanical position closes on expiry day, discounted) and
  put selling 55P 06/12 $3.55M, 50P 08/21 $3.07M.

### New positioning (vol/OI ≥ 3) [FLOW:unusual_volume]

- 56C 06/12: vol 8,227 vs OI 238 (vol/OI 34.6), $1.92M — fresh next-week call
  positioning at 56 (note: also the short-strangle strike).
- 35C 07/02: vol 100 vs OI 1, $212k in a SINGLE print — deep-ITM call
  (≈$21 ITM), stock-replacement-style.
- 0DTE call churn at 53–58 strikes (vol/OI 12–26) — expiry-day scalping, low signal.
- 140C 01/2028: vol 120 vs OI 10, $175k — small far-OTM LEAP call spec.

### Largest premium prints [FLOW:top_premium_trades] (n=25, Σ$45.22M)

| Time (Z) | Contract | Prem | Size | Side | Underlying |
|---|---|---|---|---|---|
| 14:11:40 | 110C 01/21/28 | $7.48M | 4,000 | no_side | 55.20 |
| 18:41:33 | 65P 06/05 (0DTE) | $5.41M | 4,043 | bid | 51.57 |
| 18:41:33 | 62P 06/05 (0DTE) | $4.19M | 4,043 | bid | 51.57 |
| 14:17:35 | 45C 01/15/27 | $3.31M | 1,413 | bid | 55.94 |
| 19:27:57 | 55P 06/12 | $3.16M | 6,759 | bid | 52.92 |
| 15:02:51 | 60C 10/16 | $2.80M | 2,000 | no_side | 55.40 |
| 14:17:35 | 75C 01/15/27 | $1.95M | 1,413 | ask | 55.94 |
| 14:10:33 | 56P 06/12 | $1.55M | 4,043 | bid | 55.77 |
| 19:27:57 | 56C 06/12 | $1.51M | 6,759 | bid | 52.92 |
| 15:26–19:44 | 70C 01/15/27 ×3 | $1.32–1.42M | 907–994 | bid | 54.65→53.75 |

Underlying path embedded in the prints: 55.94 (14:17Z) → 51.57 (18:41Z) →
53.75 (19:44Z), close 54.35 — a −7.8% flush and V-recovery.

### IV outliers + Greeks

[FLOW:iv_outliers]: no signal — top outliers are stale-quote artifacts on
0DTE/far-OTM strikes (e.g. 34C 0DTE max_iv 52.4 on $107k premium; 10P/12P
06/18 with $56–151 premium). Discarded.
[FLOW:greek_screener]: the $7.48M 110C 01/28 carries vega 0.276/contract →
≈ $110k vega (long vol if bought); the 0DTE put closes carry near-zero vega.
Front 06/12 prints carry heavy theta (55P theta −0.245/d).

### Smart-money / sweep-ratio (market-wide screens)

No IREN rows in `smart-money-flow` top-10 (either direction; leaders GLD, STM,
IWM, MARA chains) nor in `sweep-ratio` top-15 — **no smart-money ask/bid
imbalance detected on this date at standard thresholds** [FLOW:smart_money_flow].
Not re-run with looser thresholds per composition guidance.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw options-flow sweeps --symbol IREN --side ask --min-premium 100000 --top-n 25 --date 2026-06-05 --json` | Σ$24,592,242 ← `[.results[].total_premium]\|add`; top rows `.results[:10]` | top-25 |
| `uw options-flow sweeps --symbol IREN --side bid …` | Σ$49,796,248; 70C 01/27 bid $6,047,426 ← `.results[0].total_premium` | top-25 |
| `uw options-flow unusual-volume --symbol IREN --min-vol-oi-ratio 3 --top-n 25 --date 2026-06-05 --json` | 56C 06/12 vol_oi_ratio 34.57 ← `.results[2].vol_oi_ratio` | top-25 |
| `uw options-flow top-premium-trades --symbol IREN --top-n 25 --date 2026-06-05 --json` | $7,480,000 110C 01/28 ← `.results[0].premium`; Σ$45,216,713 | top-25 |
| `uw options-flow iv-outliers --symbol IREN --top-n 15 --date 2026-06-05 --json` | stale-quote noise ← `.results[:8]` | top-15 |
| `uw options-flow greek-screener --symbol IREN --top-n 15 --sort-by premium --date 2026-06-05 --json` | 110C vega 0.2765 ← `.results[0].vega` | top-15 |
| `uw hot-chains smart-money-flow --direction bullish/bearish --top-n 10 --min-volume 500 --date 2026-06-05 --json` | IREN absent ← `select(.option_symbol\|startswith("IREN"))` → `[]` | top-10 ×2 |
| `uw hot-chains sweep-persistence --days 5 --top-n 20 --symbol IREN --json` (no `--date`; trailing window ends at latest=as-of) | sessions_in_top=5, dominant_direction="bullish", total_sweep_premium=$339,924,997 ← `.results[0]` | 1 row |
| `uw hot-chains sweep-ratio --top-n 15 --min-volume 500 --min-sweep-ratio 0.3 --date 2026-06-05 --json` | IREN absent | top-15 |
| `uw insights deep-dive --symbol IREN --date 2026-06-05 --json` | bullish 72,372,345 / bearish 91,205,132 → net −18,832,787 ← `.uw_screener` | whole-tape |
| DuckDB §A aggressor ex-0-1DTE | call bid $60.77M vs ask $36.50M; δ-notional net ≈ −$0.098bn | whole-tape |
| DuckDB §A DTE buckets | LEAP calls $70.94M | whole-tape |

## Tool errors

- `uw hot-chains sweep-persistence --days 5 --top-n 20 --symbol IREN --date 2026-06-05 --json` →
  `Error: unknown flag: --date`. Re-run without `--date`; safe here because the
  latest available dataset date equals the as-of date (phase-0-intake.md §UW
  availability), so the trailing 5-day window ends 2026-06-05 as intended.

## DATA NOTE / CORRECTION

First jq pass on `smart-money-flow`/`sweep-ratio` guessed wrong field names
(`.underlying_symbol // .ticker`) and returned nulls; schema inspected
(`.results[0]|keys` → `option_symbol`) and re-filtered before any conclusion
was drawn. No numbers from the bad pass were used.

## Verdict for downstream phases

- **Bias from this phase:** **bearish (today's tape)** — but explicitly
  *profit-taking-shaped* inside a 5-session bullish sweep campaign, not fresh
  aggressive shorting. Put buying is modest (+$3.2M net ex-0DTE); the bearish
  premium is dominated by long-dated call selling at the bid.
- **Conviction:** 3/5 (large magnitude + extreme-for-name direction per
  `[CTX:]`, tempered by two-sidedness: $7.48M unsigned LEAP buy, the 45C→75C
  roll-up, and the bullish 5-day persistence).
- **Three things later phases should remember:**
  1. Net aggressor delta-notional ex-0-1DTE ≈ **−$98M**; net call premium
     ex-0DTE **−$24.3M** — the bearish flow is *call selling at the bid in
     Jan-27 LEAPs*, not put accumulation [FLOW:aggressor_ex0dte DUCKDB].
  2. The day's biggest print, **$7.48M 110C 01/2028 (4,000×, no_side)**, plus a
     same-second 45C→75C Jan-27 roll-up — sophisticated money kept/extended
     upside even while the complex de-grossed [FLOW:top_premium_trades].
  3. **Sweep-persistence 5/5 sessions dominant-bullish, $339.9M** — today is
     the first bearish tape in an ongoing bullish campaign; one day ≠ trend
     change [FLOW:sweep_persistence]. Also: ~$4.7M short strangle at 55/56
     exp 06/12 — someone is selling the move, pinning 55–56.
- **Open questions:** Is dark pool confirming distribution (phase 2)? Did OI at
  Jan-27 70C/100C/110C actually *fall* (closing sales = profit-taking) or rise
  (opening overwrites)? — phase 3's oi-by-strike answers this. Where do the
  gamma walls sit relative to the 55–56 pin (phase 4)?
