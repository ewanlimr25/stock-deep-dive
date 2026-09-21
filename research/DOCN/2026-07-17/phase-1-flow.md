# Phase 1 — Options Flow

**Ticker:** DOCN
**As-of date:** 2026-07-17
**Generated:** 2026-07-20T01:12:00Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md

## Summary

DOCN's tape on 2026-07-17 is **two-sided and hedging-heavy**, not a directional
one-way bet — exactly what phase-0.5's `BUSY_NAME_NORMAL_DAY` verdict predicts.
The whole-tape aggregate is near-balanced (net **+$154K** bullish, P/C **0.86**),
and DOCN appears in **none** of the market-wide smart-money-flow (bull or bear) or
sweep-ratio leaderboards. The single largest print is one genuinely bullish bet —
a **$180C Nov-20 for $985K at the ask** — sitting on top of an otherwise balanced,
protection-flecked tape; multi-day sweep persistence is **"mixed"** (4/5 sessions,
consistency 0.8). Net bias: **mixed with a mild bullish tilt**, low conviction.

## Key signals

- Whole-tape near-balanced: bullish $2.886M vs bearish $2.732M → **net +$154K**,
  P/C **0.864** `[FLOW:insights_deep_dive]` — cap conviction per `[CTX:]`.
- Standout bullish print: **$180C 2026-11-20, $985,005 at ask**, 795 contracts,
  1 trade, IV≈100%, delta 0.35 `[FLOW:top_premium_trades]` — one print, not a tape.
- **Phase-0 flag resolved:** the $123C 7/24 (vol/oi 230.5) is **sold at the bid**
  ($259.5K, 459 contracts) — **call-writing/closing, NOT aggressive buying**
  `[FLOW:sweeps bid]`. The near-dated "spike" is not directional demand.
- Downside protection is real: **$175P Oct-16 $726K ask** (deep-ITM) + **$100P
  Sep-18 $468K ask** (OTM) bought `[FLOW:sweeps ask]` — hedging/bearish offset.
- **$115P Aug-21 sold at bid $461–496K** (340–365 contracts) `[FLOW:sweeps bid]`
  — put-writing (mildly bullish / willing-to-own at 115).

## Detailed findings

### Whole-tape aggregate (read the top-N against this) `[FLOW:insights_deep_dive]`

| Field | Value |
|-------|-------|
| call_premium | $3.006M |
| put_premium | $2.998M |
| bullish_premium | $2.886M |
| bearish_premium | $2.732M |
| **derived net_flow (bull−bear)** | **+$154,130** (≈53% bullish — balanced) |
| call_volume / put_volume | 2,957 / 2,555 |
| **put_call_ratio** | **0.864** (mild call lean) |
| iv_rank | 99.12 · iv30d ≈114% |
| implied_move / _perc | 2.14 / **1.80%** (near-dated) |

Directional edge from the aggregate is negligible. The tape's magnitude is
below DOCN's own median (self_pctile_total 31.3, `[CTX:self_pctile DUCKDB]`).

### Sweeps (ask vs bid)

**ASK side (aggressive buying):**
| Contract | Prem | Size | Trades | Read |
|----------|------|------|--------|------|
| $180C Nov-20 | $985,005 | 795 | 1 | **bullish** (biggest print, 4mo) |
| $175P Oct-16 | $725,880 | 115 | 1 | deep-ITM put buy — bearish/synthetic-short |
| $100P Sep-18 | $468,180 | 426 | 42 | OTM put buy — downside hedge/bearish |
| $130P 7/17 (0DTE) | $410,567 | 346 | 30 | **0DTE pin noise — discount** |
| $135C Dec-2027 | $131,370 | 29 | 1 | LEAP call — slow bullish |
| $200C Jan-2027 | $131,230 | 98 | 94 | far-OTM upside lotto — bullish |

**BID side (aggressive selling):**
| Contract | Prem | Size | Read |
|----------|------|------|------|
| $115P Aug-21 | $460,700–495,875 | 340–365 | **put-writing — mild bullish** |
| $123C 7/24 | $259,520 | 459 | call-writing/closing (phase-0 flag) |
| $130P 7/17 (0DTE) | $131,413 | 77 | 0DTE noise |
| $150C Jan-2027 | $119,470 | 51 | call sold — capping upside |
| $140C Aug-21 | $103,050 | 111 | call sold |

Net of sweeps: bullish (180C/200C ask + 115P bid-writing) vs bearish/hedge
(175P/100P ask). **Genuinely two-sided.**

### New positioning (unusual vol, vol/OI ≥ 3) `[FLOW:unusual_volume]`

- $123C 7/24: vol 461 / OI 2 (voi 230.5) — but **bid-side** (writing), not new longs.
- $116P 7/24: vol 196 / OI 2 (voi 98).
- $123C 7/31: vol 104 / OI 12 (voi 8.7).
- **$115P Aug-21: vol 365 / OI 61 (voi 5.98)** — real new positioning, sold at bid.
- **$100P Sep-18: vol 426 / OI 104 (voi 4.1)** — real new OTM put buying.

### Largest premium prints + timing `[FLOW:top_premium_trades]`

The two biggest ($180C Nov + $175P Oct) both stamped **16:58:10 @ undl 119.17** —
a paired late-session institutional structure (OTM call + deep-ITM put), net a
small long-delta, long-vega position at ~100% IV. The $115P Aug-21 bid-side sale
printed later (19:34:45 @ 119.44). Underlying traded **~$117–119.4** across the tape.

### IV outliers + Greeks `[FLOW:iv_outliers][FLOW:greek_screener]`

- 0DTE 7/17 puts dominate the IV-outlier list (125P IV 486%, 130P IV 324%,
  115P IV 226%) — **expiry pin mechanics, discard as directional signal.**
- Real elevated-IV new-tenor names: 80P Aug-21 (118%), 220C Aug-21 (112%),
  140C Aug-21 (110%), 115P Aug-21 (109%), 180C Aug-21 (109%).
- IV is uniformly ~100–120% across live tenors — consistent with **iv_rank 99**;
  this is a **vol-elevated, pre-earnings tape**.

### Persistence & smart-money membership

- `sweep-persistence` (5d): DOCN in **4/5 sessions**, consistency **0.8**,
  dominant_direction **"mixed"**, total_sweep_premium $2.07M `[FLOW:sweep_persistence]`.
- `smart-money-flow` bullish & bearish top-10: **DOCN absent both** — not a
  smart-money leader on this date `[FLOW:smart_money_flow]`.
- `sweep-ratio` top-15: **DOCN absent** `[FLOW:sweep_ratio]`.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|------------------|--------------------------|-----------|
| `insights deep-dive --symbol DOCN --date 2026-07-17` | net_flow=+$154,130 ← `.uw_screener.bullish_premium-.bearish_premium`; P/C 0.864 ← `.uw_screener.put_call_ratio` | whole-tape |
| `options-flow sweeps --side ask --min-premium 100000` | $180C Nov $985,005 ← `.results[0].total_premium` | top-6 |
| `options-flow sweeps --side bid --min-premium 100000` | $115P Aug $495,875 bid ← `.results[0]`; $123C 7/24 $259,520 bid ← `.results[1]` | top-5 |
| `options-flow unusual-volume --min-vol-oi-ratio 3` | 115P Aug voi 5.98 ← `.results[3].vol_oi_ratio` | top-5 |
| `options-flow top-premium-trades --top-n 25` | 180C/175P both @16:58:10 ← `.results[0..1].executed_at` | top-8 |
| `options-flow iv-outliers --top-n 15` | 0DTE 125P IV 486% ← `.results[0].implied_volatility` | top-8 |
| `options-flow greek-screener --sort-by premium` | 180C delta 0.35 ← `.results[0].delta` | top-8 |
| `hot-chains sweep-persistence --days 5 --symbol DOCN` | mixed, 4/5, 0.8 ← `.results[0]` | 1 |
| `hot-chains smart-money-flow --direction bull/bear` | DOCN absent ← filter `.ticker=="DOCN"` | 0 |
| `hot-chains sweep-ratio --top-n 15` | DOCN absent | 0 |

## Tool errors

- `hot-chains sweep-persistence … --date 2026-07-17` → `Error: unknown flag: --date`.
  Re-run without `--date`; latest available == as-of (2026-07-17) so as-of-safe
  (dates_covered = 2026-07-13…07-17). No number transcribed from the failed call.

## DATA NOTE / CORRECTION

- Phase-0 intake read the $123C 7/24 (vol/oi 230.5) as a live "call spike."
  Phase-1 sweeps resolve it as **bid-side ($259,520 sold, 459 contracts) —
  call-writing/closing, not directional buying.** Corrected here.
- `top-premium-trades` premium/size fields are `.premium`/`.size` (not
  `total_premium`/`total_size` as in `sweeps`); values re-read against the
  correct paths before transcription.

## Verdict for downstream phases

- **Bias from this phase:** **mixed, mild bullish tilt** (biggest single print
  $180C ask + 115P put-writing vs offsetting deep-ITM/OTM put buying)
- **Conviction:** **2/5** (balanced aggregate, `BUSY_NAME_NORMAL_DAY` cap, not on
  any smart-money leaderboard, sweep persistence "mixed")
- **Three things later phases should remember:**
  1. Tape is **two-sided/hedging-heavy** — no clean directional flow edge; the one
     bullish standout ($180C Nov $985K) is a single print, not a tape.
  2. IV is pinned at **~100% / rank 99** across all live tenors → this is a
     **vol / pre-earnings (Aug-4) setup**, not a flow-momentum setup.
  3. Real new positioning is in **Aug-21 & Sep-18 puts** (115P written at bid,
     100P bought at ask) — phase-3 must check whether these become OI walls.
- **Open questions:** Is the $45.8M dark-pool print (phase-0.5) confirming a
  directional accumulation the balanced options tape hides? (phase-2). Are the
  180C/200C upside calls building OI or one-and-done? (phase-3).
