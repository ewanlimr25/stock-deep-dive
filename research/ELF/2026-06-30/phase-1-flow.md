# Phase 1 — Options Flow

**Ticker:** ELF
**As-of date:** 2026-06-30
**Generated:** 2026-07-01T00:21:15Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md

## Summary

The ELF tape is **bullishly tilted but not one-directional**. The whole-tape
aggregate is heavily call-skewed (P/C ratio **0.184**, call premium $13.3M vs put
$1.2M) yet the *directional* edge is only modest — **net_flow +$1.22M** bullish
(bullish $5.97M vs bearish $4.75M, a 56/44 split), because a large share of the
call premium is being *written* against, not just bought. The two highest-conviction
signals are unambiguously bullish, though: a **$45 Jan-2028 deep-ITM LEAP block
bought on the ask for $1.90M** (delta 0.85 — a leveraged stock-replacement long),
and **5-of-5-session bullish sweep persistence (consistency_score 1.0)** — a
multi-day campaign, not a one-day print. The marquee front-month line ($75 Aug call,
$3.5M of new positioning) is heavily two-way, which is what caps the directional
conviction. Carrying phase-0.5: `unusual_verdict = GENUINELY_UNUSUAL` → no confluence
cap; this is ELF's biggest premium day in 56 sessions.

## Key signals

- **Net_flow +$1,220,344 bullish** (derived: bullish_premium $5,972,371 − bearish_premium $4,752,027) [FLOW:insights_deep_dive]
- **P/C ratio 0.184** — call premium $13.32M vs put premium $1.21M (very call-heavy tape) [FLOW:insights_deep_dive]
- **$45 Jan-2028 LEAP bought ask, $1.90M, delta 0.85** — leveraged long / stock-replacement, highest-conviction print [FLOW:sweeps ask][FLOW:top-premium-trades]
- **Sweep-persistence: 5/5 sessions bullish, consistency 1.0** — a sustained bullish campaign, not a one-off [FLOW:sweep-persistence]
- **$75 Aug call: 4,497 vol vs 1,230 OI (vol/OI 3.66), $3.54M new** — biggest new line, but two-way (bought AND sold) [FLOW:unusual-volume][FLOW:sweeps]

## Detailed findings

### Whole-tape aggregate `[FLOW:insights_deep_dive]` (read the top-N below against this)

Underlying **close $74.00**, intraday $71.22–$74.36 (closed near the high).

| Field (`uw_screener`) | Value |
|---|---|
| call_premium | $13,319,462 |
| put_premium | $1,210,166 |
| bullish_premium | $5,972,371 |
| bearish_premium | $4,752,027 |
| **net_flow (derived = bull − bear)** | **+$1,220,344** |
| call_volume / put_volume | 17,351 / 3,194 |
| put_call_ratio | 0.184 |
| iv_rank | 46.83 |
| implied_move / implied_move_perc | 2.606 / **3.52%** |
| volatility (IV30d) | 0.701 / 0.670 |

Read: the tape is ~92% call *premium*, but only **+$1.22M net directional** — the
gap says heavy call-*writing* (or spread-selling) is offsetting the call-buying. So
"call-heavy" ≠ "clean long". The directional edge (56/44) is real but modest; the
conviction lives in the *composition* (below), not the raw call skew.

### Sweeps — ask vs bid `[FLOW:sweeps]`

- **Ask-side (aggressive buyers): $3.35M total, 97% calls** ($3.245M calls / $0.103M puts).
  - **$45 call 2028-01-21 — $1,904,448** (size 502, 4 trades, avg $38.86, delta 0.85): deep-ITM LEAP, a leveraged long. The single most conviction-bearing print on the tape.
  - $75 call 2026-08-21 — $991,255 (size 1,184, 68 trades, ATM).
  - $90 call 2026-09-18 — $190,563; $58 call 2026-07-31 — $158,950.
  - Only put bought on ask: $70 put 2026-08-21 — $103,423 (small; possible collar/hedge against the LEAP).
- **Bid-side (aggressive sellers): $2.81M total, 90% calls** ($2.54M calls / $0.27M puts).
  - **$75 call 2026-08-21 — $1,114,622 sold** (size 1,413) — nearly mirrors the ask-side $75 Aug buying → this line is a wash / spread, not clean accumulation.
  - $57 call 2026-07-31 — $541,595 sold; plus $55/$60/$64 Jul calls sold.
  - $55 put 2026-10-16 — $128,370 sold (bullish: put-writing).
- **Net sweep read:** calls ask $3.245M − bid $2.54M = **+$0.70M net call buying**;
  puts net sold (bullish). Direction bullish, magnitude modest — the ask-side is
  dominated by the one LEAP block.

### New positioning — unusual volume (vol/OI ≥ 3) `[FLOW:unusual-volume]`

Overwhelmingly **new call positioning**, concentrated Jul-31 and Aug-21:

| Contract | Vol | OI | vol/OI | Premium |
|---|---|---|---|---|
| $75 call 2026-08-21 | 4,497 | 1,230 | 3.66 | **$3,537,077** |
| $58 call 2026-07-31 | 598 | 2 | 299 | $961,252 |
| $63 call 2026-07-31 | 246 | 9 | 27.3 | $288,852 |
| $64 call 2026-07-31 | 244 | 52 | 4.7 | $266,266 |
| $55 call 2026-07-31 | 102 | 9 | 11.3 | $181,077 |
| $60 call 2026-07-31 | 114 | 38 | 3.0 | $158,487 |
| $55 put 2026-10-16 | 389 | 63 | 6.2 | $128,370 |
| $90 call 2026-09-18 | 397 | 64 | 6.2 | $191,543 |

The $58 Jul call opened from OI=2 → a genuinely fresh position. Nearly all fresh
positioning is calls; the only notable new put is the $55 Oct (and it was *sold*,
per bid sweeps — bullish).

### Largest premium prints `[FLOW:top-premium-trades]`

Side split of the top-25 prints: **ask $2.87M (9) · mid $1.91M (10) · bid $1.45M (6)**
→ **net ask − bid = +$1.42M** aggressive buying, but ~$1.9M sits at *mid* (spreads /
negotiated), reinforcing "call-heavy churn with a bullish tilt". Focal lines: the
$45 Jan-2028 LEAP ($1.13M + $764K, both ask) and the $75 Aug call (bid $783K + mid
$765K + ask $174K×4 — classic two-way).

### IV outliers + Greeks `[FLOW:iv-outliers][FLOW:greek-screener]`

- **IV outliers:** only three contracts flagged — all **0–2 DTE (2026-07-02) puts
  with iv=null** ($53/$57/$58). This is 0DTE pin noise, not a vol signal — **discounted**.
- **Greeks:** top-by-premium is the same two lines — $45 LEAP (delta 0.85, vega 0.21,
  low gamma 0.0035 — long-dated) and $75 Aug (delta ~0.52, high gamma ~0.018 — ATM
  front-month). No OTM-put gamma cluster → no bearish greek signature.

### Market-wide context reads

- **smart-money-flow:** ELF is **absent from both bullish and bearish top-10**
  (min-volume 500). No market-leading ask/bid imbalance detected on this date — do
  not loosen thresholds (per phase rule). Consistent with phase-0.5: ELF is 98th
  *percentile* but not a top-50 *absolute* name.
- **sweep-ratio:** ELF **outside top-15** (its absolute sweep ratio is not
  market-leading) — recorded, not an error.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw insights deep-dive --symbol ELF --date 2026-06-30 --json` | net_flow=+$1,220,344 ← `.uw_screener.bullish_premium − .uw_screener.bearish_premium`; P/C=0.184 ← `.uw_screener.put_call_ratio` | whole-tape |
| `uw options-flow sweeps --symbol ELF --side ask --min-premium 100000 --top-n 25` | ask calls $3.245M ← `[.results[]\|select(.option_type=="call").total_premium]\|add`; LEAP $1,904,448 ← `.results[0].total_premium` | top-5 |
| `uw options-flow sweeps --symbol ELF --side bid --min-premium 100000 --top-n 25` | bid calls $2.54M; $75 Aug sold $1,114,622 ← `.results[0].total_premium` | top-10 |
| `uw options-flow unusual-volume --symbol ELF --min-vol-oi-ratio 3 --top-n 25` | $75 Aug 4497/1230 $3,537,077 ← `.results[]\|select(.strike==75…)` | top-15 |
| `uw options-flow top-premium-trades --symbol ELF --top-n 25` | ask $2.87M / mid $1.91M / bid $1.45M ← `group_by(.side)`; undp close 74.0 ← `.results[].underlying_price` | top-25 |
| `uw options-flow iv-outliers --symbol ELF --top-n 15` | 3 rows, all 0-2DTE puts iv=null ← `.results[].iv` | 3 |
| `uw options-flow greek-screener --symbol ELF --top-n 15 --sort-by premium` | $45 LEAP delta 0.85 ← `.results[0].delta` | top-12 |
| `uw hot-chains sweep-persistence --days 5 --top-n 20 --symbol ELF` | 5/5 sessions bullish, consistency 1.0, $688,379 ← `.results[]\|select(.ticker=="ELF")` | 1 |
| `uw hot-chains smart-money-flow --direction bullish/bearish --top-n 10 --min-volume 500` | ELF absent both ← `index("ELF")==null` | 0 |
| `uw hot-chains sweep-ratio --top-n 15 --min-volume 500 --min-sweep-ratio 0.3` | ELF outside top-15 | 0 |

## Tool errors

- `uw hot-chains sweep-persistence … --date 2026-06-30` → `Error: unknown flag: --date`.
  Re-ran without `--date` (trailing multi-day tool anchors to the latest date =
  2026-06-30, our as-of); result valid. No other errors.

## DATA NOTE / CORRECTION

_None — all values round-tripped through `jq`/DuckDB on first read._

## Verdict for downstream phases

- **Net bias:** **BULLISH** (call-heavy, net-bullish flow + persistent bullish sweeps + a
  leveraged LEAP long), tempered — the directional edge is only 56/44 and the biggest
  new line ($75 Aug) is two-way.
- **Conviction:** **3 / 5** — lifted from 2 by (a) 5/5-session bullish persistence
  (consistency 1.0) and (b) the $1.9M deep-ITM LEAP; held below 4 by the two-way
  front-month churn and modest net directional edge.
- **Three things later phases should remember:**
  1. The cleanest bullish signal is **structural/long-dated** (a $45 Jan-2028 delta-0.85
     LEAP + 5-session sweep persistence), **not** front-month momentum — the $75 Aug
     line is a wash. Tradeable thesis is "leveraged long into a slow grind," not "chase
     a breakout."
  2. Positioning is **call-concentrated at $55–$75, Jul-31/Aug-21**; ELF closed **$74**,
     so the $75 Aug call is ATM — watch it as the pin/magnet (hand to phase-3/4).
  3. This is a **flow event, not a vol event** (IV rank 46.8, IV outliers are 0DTE noise) —
     favor directional/delta structures over vega. No bearish greek signature.
- **Open questions:**
  - Is **dark pool** (phase-2) confirming accumulation under this call-buying, or is the
    equity being distributed while calls churn?
  - Does **OI / positioning** (phase-3) show the $75 Aug and $45 LEAP as genuinely *held*
    open interest building, or intraday round-trips?
  - Next earnings 2026-08-05 (phase-0.5) sits just after Aug-21 expiry — is the Aug call
    buying an earnings-anticipation play? (cross-check phase-7c/earnings.)
