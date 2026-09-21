# Phase 1 — Options Flow

**Ticker:** GOOG · **As-of:** 2026-07-23 · **Spot:** $318.34
**Generated:** 2026-07-24T01:18:35Z
**Upstream:** phase-0.5-context.md (`[CTX:] unusual_verdict=GENUINELY_UNUSUAL`, net-dir
universe pctile 0.0, self-history net-dir pctile 1.4 over 72 sessions)

## Summary

The dollar-weighted tape is **bearish**: put premium ($406.6M) is ~1.9× call
premium ($215.9M), net flow −$49.4M, and the **top-25 single-premium prints are
100% puts** ($170.2M, zero calls), led by a 480-strike LEAP put (exp 2027-01-15,
$29.9M). Aggressive ask-side sweeps are put-dominated 10:1 by premium ($124.3M
puts vs $12.3M calls). The one countervailing layer is a wall of **0DTE/1DTE call
scalps** (325C/320C/322.5C exp 07-24, vol 16k–17k on OI <100) — that is where the
"22 calls vs 3 puts" new-position count comes from, but it is cheap retail
lottery, not premium. Net: institutional/premium money leans short via deep-ITM
puts; retail scalps lean long intraday. Conviction moderate, not maximal, because
much of the deep-ITM put premium prints on the **bid** side (could be writing/
rolling, not fresh shorts) and 5-session sweep persistence reads "mixed."

## Key signals

- **Whole-tape aggregate is net bearish:** bullish $258.7M − bearish $308.0M =
  **net −$49.4M**; put premium $406.6M > call premium $215.9M; P/C 0.713 by
  volume. GOOG #6 net-bearish in the universe. `[FLOW:insights_deep_dive]`
- **Top-25 premium prints are entirely puts** — $170.2M, 0 calls. Largest: 480P
  2027-01-15 $29.9M (bid). `[FLOW:top_premium_trades]`
- **Ask-side sweeps put-heavy 10:1 by premium:** 19 put sweeps $124.3M vs 6 call
  sweeps $12.3M; top ask sweep 400P 2026-08-21 $28.3M. `[FLOW:sweeps]`
- **Big puts are deep-ITM, delta −0.84 to −0.96** (480P, 410P, 400P, 395P) —
  short-stock-like exposure, capital-intensive/institutional. `[FLOW:greek_screener]`
- **Persistent campaign, mixed direction:** GOOG in top-sweeps **5/5 sessions**,
  $437.7M cumulative sweep premium, `dominant_direction = mixed`. `[FLOW:sweep_persistence]`

## Detailed findings

### Whole-tape aggregate (read the top-N against this) — `[FLOW:insights_deep_dive]`
| Metric | Value |
|---|---|
| call_premium | $215.9M |
| put_premium | $406.6M |
| bullish_premium | $258.7M |
| bearish_premium | $308.0M |
| **net_flow (derived)** | **−$49.4M** |
| call_volume / put_volume | 327,406 / 233,311 |
| put_call_ratio (vol) | 0.713 |
| iv30d / iv_rank | 0.324 / 38.3 |
| implied_move | 1.57% ($4.99) |

Premium/volume divergence: more call *contracts* (0DTE scalps drive it) but put
*premium* nearly doubles call premium. Dollars are bearish; contracts are noisy.

### Sweeps (ask vs bid) — `[FLOW:sweeps]`
- **ASK (aggressive buyers):** 19 puts $124.3M · 6 calls $12.3M. All top ask
  sweeps are ITM puts (strike > $318.34 spot): 400P/375P/395P/345P/410P.
- **BID (aggressive sellers/hitters):** 18 puts $111.8M · 7 calls $16.0M.
- Net ask−bid put premium ≈ +$12.5M (modestly more aggressive put *buying* than
  selling). Puts dominate both sides → this is a **put-centric tape**, direction
  slightly net-buy. Ambiguity: heavy two-sided put flow ⇒ some is rolling/writing.

### New positioning (vol >> OI) — `[FLOW:unusual_volume]`
22 calls / 3 puts by count, but the calls are near-dated scalps:
| Type | Strike | Exp | vol/OI | vol | OI | prem |
|---|---|---|---|---|---|---|
| call | 325 | 07-24 (1DTE) | 331.7 | 16,254 | 49 | $2.39M |
| call | 320 | 07-24 (1DTE) | 174.5 | 17,446 | 100 | $5.40M |
| call | 322.5 | 07-24 | 126.0 | 7,056 | 56 | $1.74M |
| call | 317.5 | 07-24 | 110.6 | 3,649 | 33 | $1.44M |
| **put** | **300** | **2027-02-19 (LEAP)** | 85.0 | 425 | 5 | $0.91M |
| **put** | **362.5** | **2026-08-07 (ITM)** | 241.0 | 241 | 1 | $1.05M |

The genuinely *new* directional opens of size are the calls (0DTE lottery) plus a
fresh 300 LEAP put and a 362.5 ITM put — small but bearish-tenor.

### Largest premium prints — `[FLOW:top_premium_trades]` (all puts)
| Type | Strike | Exp | Premium | Side |
|---|---|---|---|---|
| put | 480 | 2027-01-15 (LEAP) | $29.93M | bid |
| put | 410 | 2026-08-21 | $12.97M | bid |
| put | 400 | 2026-08-21 | $12.36M | ask |
| put | 395 | 2026-08-21 | $11.08M | ask |
| put | 380 | 2026-07-24 | $11.00M | bid |
| put | 410 | 2026-08-21 | $9.74M | ask |
| put | 350 | 2026-07-24 | $9.57M | bid |
| put | 345 | 2026-07-24 | $8.32M | ask |

### IV outliers + Greeks — `[FLOW:iv_outliers]` `[FLOW:greek_screener]`
- IV outliers: 13 puts / 2 calls; all outlier puts are **1DTE deep-ITM** (400P/
  395P/390P exp 07-24) with IV 1.8–2.7 — a deep-ITM near-expiry **pricing
  artifact** (wide spreads), not a clean directional vol bid. Discount as pin/
  mechanical.
- Greeks: the premium puts carry delta −0.837 (480P) to −0.962 (410P) — deep-ITM,
  short-stock-equivalent. gamma small (deep ITM). This is directional-delta
  positioning, not a vol trade.

## Tool calls
| Tool | Args | Rows | jq path |
|---|---|---|---|
| insights deep-dive | --symbol GOOG --date 2026-07-23 | 1 | `.uw_screener.{call_premium,put_premium,bullish_premium,bearish_premium,put_call_ratio,call_volume,put_volume,iv_rank,implied_move_perc}` |
| options-flow sweeps | --side ask --min-premium 100000 --top-n 25 | 25 | `.results[]│group_by(.option_type)` |
| options-flow sweeps | --side bid --min-premium 100000 --top-n 25 | 25 | same |
| options-flow unusual-volume | --min-vol-oi-ratio 3 --top-n 25 | 25 | `.results[].{option_type,strike,expiry,vol_oi_ratio,total_volume,open_interest,total_premium}` |
| options-flow top-premium-trades | --top-n 25 | 25 | `.results[].{option_type,strike,expiry,premium,side}` |
| options-flow iv-outliers | --top-n 15 | 15 | `.results[]│group_by(.option_type)` |
| options-flow greek-screener | --top-n 15 --sort-by premium | 15 | `.results[].{option_type,strike,premium,delta,gamma}` |
| hot-chains sweep-persistence | --days 5 --top-n 20 --symbol GOOG | 1 | `.results[0].{sessions_in_top,dominant_direction,total_sweep_premium}` |
| hot-chains smart-money-flow | --direction bullish/bearish --top-n 25 --min-volume 500 | GOOG absent | market-wide list; GOOG not ranked |
| hot-chains sweep-ratio | --top-n 25 --min-sweep-ratio 0.3 | 25 | GOOG not in top rows |

## Tool errors
- `hot-chains sweep-persistence` rejects `--date` (unknown flag) — re-ran without
  it (command anchors to latest = 2026-07-23). No data lost.
- `hot-chains smart-money-flow` returned **no GOOG row** either direction on this
  date (GOOG outside the market-wide top-25). Per rule, not re-run with looser
  thresholds. Recorded "no smart-money-flow ranked for GOOG."

## Verdict for downstream

- **Net bias: BEARISH** (dollar/premium/delta-weighted). Put premium ~1.9× call
  premium, top-25 prints 100% puts, ask-side put sweeps 10:1, and phase-0.5 pins
  GOOG as the single most net-bearish name in the universe. The 0DTE call-scalp
  layer is real but is intraday lottery noise, not premium conviction.
- **Conviction: 3 / 5 (moderate bearish).** Held below 4 because (a) large
  deep-ITM puts print on both ask *and* bid — meaningful put *writing/rolling* is
  plausible, not only fresh shorts; (b) 5-session sweep persistence is "mixed";
  (c) the highest-IV puts are 1DTE deep-ITM artifacts, not a directional vol bid.
- **Three datapoints to remember:**
  1. net_flow −$49.4M; put premium $406.6M vs call premium $215.9M; universe
     net-dir pctile 0.0.
  2. Top-25 premium prints = 100% puts ($170.2M); largest 480P 2027-01-15 LEAP
     $29.9M (bid); deep-ITM put deltas −0.84 to −0.96.
  3. Ask-side put-sweep premium $124.3M vs call-sweep $12.3M; new-position count
     is 0DTE call scalps (325C/320C exp 07-24), not premium.
- **Open questions:**
  - Is the deep-ITM put flow fresh directional shorting or writing/rolling? →
    phase-3 OI-change (put OI building?), phase-4 structure/GEX.
  - Is dark pool confirming distribution (bearish) or absorbing (support)? → phase-2.
  - Where are the dealer gamma walls relative to the 380–410 put strikes? → phase-3/4.
