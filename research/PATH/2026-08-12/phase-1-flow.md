# Phase 1 — Options Flow

**Ticker:** PATH
**As-of date:** 2026-08-12
**Generated:** 2026-08-13T01:35:00Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md

## Summary

The whole-tape aggregate is essentially flat: derived `net_flow = bullish_premium
($1,440,177) − bearish_premium ($1,484,555) = −$44,378` against $3.33M gross
premium — noise-level. The single largest theme in today's tape (and the prior
4 sessions) is a **2028-12-15 $10/$12 put LEAP chain** carrying $8.47M of
cumulative sweep premium over 5 straight sessions — but `hot-chains
sweep-persistence` itself tags its `dominant_direction` as **"mixed"**
(`consistency_score=1`, meaning it appears every day, but not one-sided). Ask-
and bid-side sweep sizes on that exact chain are almost perfectly balanced
today (1,148 ask-side vs. 1,150 bid-side contracts). No smart-money-flow or
sweep-ratio presence market-wide for PATH today. Combined with phase-0.5's
`BUSY_NAME_NORMAL_DAY` verdict, this phase's net bias is **mixed/neutral** at
**low conviction (2/5)**.

## Key signals

- Whole-tape derived net_flow ≈ −$44,378 on $3.33M gross premium — flat
  [FLOW:insights_deep_dive]
- 2028-12-15 $10/$12 put LEAP chain: $8.47M cumulative sweep premium over 5
  sessions, `dominant_direction=mixed`, `consistency_score=1`
  [FLOW:sweep_persistence]
- Today's ask-side vs bid-side sweep contracts on that same chain: 1,148 vs
  1,150 — near-perfectly offsetting [FLOW:sweeps]
- Top-25 largest single prints sum to only $683,581 — ~20.5% of the $3.33M
  whole-tape gross premium; the "top prints" are the tip of a much larger,
  balanced iceberg [FLOW:top_premium_trades]
- Zero PATH rows in market-wide `smart-money-flow` (bullish or bearish, top-10
  each) and zero rows in market-wide `sweep-ratio` (top-15) — no smart-money
  flag on PATH today [FLOW:smart_money_flow, FLOW:sweep_ratio]

## Detailed findings

### Whole-tape aggregate (read first, per skill rule — top-N is the tip of the iceberg)

From `uw insights deep-dive --symbol PATH --date 2026-08-12` (same call as
phase-0.5, `uw_screener` block):

| Metric | Value |
|---|---|
| `call_premium` | $2,254,097 |
| `put_premium` | $1,074,984 |
| `bullish_premium` | $1,440,177 |
| `bearish_premium` | $1,484,555 |
| **derived `net_flow`** (`bullish_premium − bearish_premium`) | **−$44,378** |
| `call_volume` | 17,375 |
| `put_volume` | 8,250 |
| `put_call_ratio` | 0.4748 |

Call volume is ~2.1× put volume, but put premium is ~48% of call premium — puts
are carrying disproportionately more premium per contract than calls, which is
consistent with the expensive, longer-dated LEAP puts driving the put side (see
below) versus cheaper, more numerous near-term calls. Net directional premium
is a rounding error against the gross flow — **this is a flat tape**, matching
phase-0.5's `unusual_verdict=BUSY_NAME_NORMAL_DAY` and its `self_pctile_net_dir
=47.1` read.

### Sweeps (ask vs bid)

`uw options-flow sweeps --side ask --min-premium 100000 --top-n 25`: **2 rows**,
both puts, both 2028-12-15 expiry:

| Strike | Premium | Size | Trades | Avg price |
|---|---|---|---|---|
| $10 | $197,418 | 788 | 16 | $2.51 |
| $12 | $128,722 | 360 | 12 | $3.58 |

`uw options-flow sweeps --side bid --min-premium 100000 --top-n 25`: **3 rows**:

| Type | Strike | Expiry | Premium | Size | Trades | Avg price |
|---|---|---|---|---|---|---|
| put | $12 | 2028-12-15 | $206,126 | 576 | 23 | $3.57 |
| put | $10 | 2028-12-15 | $143,185 | 574 | 25 | $2.49 |
| call | $5.50 | 2026-09-04 | $128,333 | 131 | 96 | $9.82 (deep ITM) |

Ask-side put sweep contracts (788+360=1,148) vs bid-side put sweep contracts
(574+576=1,150) on the identical $10/$12 LEAP chain — this is two aggressive
flows nearly cancelling each other in size, on the same two strikes, same
expiry, same day. Read as **spread construction, MM inventory turnover, or a
large position being rolled/adjusted** — not a fresh one-directional bet. The
lone bid-side call sweep ($5.50 strike, 96 trades in one line, deep ITM,
avg price $9.82 vs spot $15.26 → ~$9.76 intrinsic) looks like a
stock-replacement position being sold/closed, immaterial in size.

### New positioning (unusual volume, vol/OI ≥ 3)

`uw options-flow unusual-volume --min-vol-oi-ratio 3 --top-n 25`: only **3
rows**, all small (`total_premium` $10K–$18K):

| Type | Strike | Expiry | Vol | OI | Vol/OI | Avg IV |
|---|---|---|---|---|---|---|
| put | $14.5 | 2026-08-28 | 418 | 24 | 17.4 | 0.601 |
| call | $20 | 2026-09-11 | 750 | 133 | 5.6 | 0.835 |
| put | $15 | 2026-08-28 | 155 | 32 | 4.8 | 0.602 |

Genuinely new near-term positioning is thin and dollar-small — none of it
overlaps with the LEAP chain (which has ample OI already, so it isn't showing
as a vol/OI spike). Not enough size here to change the read.

### Largest premium prints (top 5 of 25)

| Time (UTC) | Type | Strike | Expiry | Premium | Side | Delta | Underlying |
|---|---|---|---|---|---|---|---|
| 14:30:48 | call | $12 | 2028-12-15 | $54,600 | ask | 0.80 | $15.12 |
| 14:57:16 | call | $18 | 2026-12-18 | $51,072 | bid | 0.44 | $15.04 |
| 14:08:59 | put | $10 | 2028-12-15 | $37,944 | bid | -0.15 | $15.235 |
| 15:19:40 | put | $12 | 2028-12-15 | $35,900 | bid | -0.20 | $15.055 |
| 13:52:31 | put | $12 | 2028-12-15 | $35,800 | bid | -0.20 | $15.175 |

Top-25 split: **calls $335,627 (12 trades) vs puts $347,954 (13 trades)** —
essentially balanced. By side: **ask $313,533 vs bid $284,213 vs mid $85,835**
— also balanced, no clean aggressor skew. **All $347,954 of put premium in the
top-25 sits in the single 2028-12-15 $10/$12 chain** (breakdown: $10-ask
$112,000/5 trades, $10-bid $62,793/2, $12-ask $101,461/4, $12-bid $71,700/2) —
confirming this one LEAP chain is effectively the entire put story today.

### IV outliers + Greeks

`uw options-flow iv-outliers --top-n 15`: only 4 rows, all **deep-ITM, very
short-dated calls** (strikes $5.50–$12 against a $15.26 spot, expiries
2026-08-14/08-21/09-04 — 2–23 DTE) showing implausibly high `avg_iv` (1.66–6.56)
and `max_iv` up to 7.50. This pattern (deep ITM, near-expiry, extreme IV) is a
classic **parity/thin-quote artifact**, not a genuine volatility signal — flag
as a data-quality caveat, not a real vol edge, and exclude from conviction
scoring.

Greek screener (top by premium) is dominated by the same 2028-12-15 chain
already covered above; deltas on the puts cluster at −0.15 to −0.20 (modestly
OTM, consistent with hedge/collar legs rather than aggressive directional
bets), gammas/vegas are unremarkable for 2+ year LEAPs.

### Market-wide cross-checks

- `uw hot-chains smart-money-flow --direction bullish/bearish --top-n 10`:
  **zero PATH rows either direction** → no smart-money flow detected on this
  date (per skill rule, not re-queried with looser thresholds).
- `uw hot-chains sweep-ratio --top-n 15 --min-sweep-ratio 0.3`: **zero PATH
  rows** — PATH does not crack the market's most aggressive-sweep-ratio names
  today.
- `uw hot-chains sweep-persistence --days 5 --symbol PATH`: PATH appears in
  top sweep activity **all 5 of the last 5 sessions** (`sessions_in_top=5`,
  `consistency_score=1`) with `total_sweep_premium=$8,471,362` — the chain is
  a real, sustained institutional presence, but the tool's own
  `dominant_direction=mixed` label confirms it is not one-sided.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw options-flow sweeps --symbol PATH --side ask --min-premium 100000 --top-n 25 --date 2026-08-12 --json` | 2 rows, `.results[]` | all |
| `uw options-flow sweeps --symbol PATH --side bid --min-premium 100000 --top-n 25 --date 2026-08-12 --json` | 3 rows, `.results[]` | all |
| `uw options-flow unusual-volume --symbol PATH --min-vol-oi-ratio 3 --top-n 25 --date 2026-08-12 --json` | 3 rows, `.results[]` | all |
| `uw options-flow top-premium-trades --symbol PATH --top-n 25 --date 2026-08-12 --json` | 25 rows; call_prem=$335,627 ← `[.results[]\|select(.option_type=="call")\|.premium]\|add`; put_prem=$347,954 (same for puts) | all 25 |
| `uw options-flow iv-outliers --symbol PATH --top-n 15 --date 2026-08-12 --json` | 4 rows, `.results[]` | all |
| `uw options-flow greek-screener --symbol PATH --top-n 15 --sort-by premium --date 2026-08-12 --json` | 15 rows, `.results[]` | all |
| `uw hot-chains smart-money-flow --direction bullish --top-n 10 --min-volume 500 --date 2026-08-12 --json` | PATH absent ← `.results[]\|select(.option_symbol\|test("^PATH"))` | top-10 |
| `uw hot-chains smart-money-flow --direction bearish --top-n 10 --min-volume 500 --date 2026-08-12 --json` | PATH absent (same filter) | top-10 |
| `uw hot-chains sweep-persistence --days 5 --top-n 20 --symbol PATH --json` (no `--date`; trailing tool anchors to latest date, which is the as-of date here) | `sessions_in_top=5, consistency_score=1, dominant_direction="mixed", total_sweep_premium=8471362` ← `.results[0]` | 1 (symbol-filtered) |
| `uw hot-chains sweep-ratio --top-n 15 --min-volume 500 --min-sweep-ratio 0.3 --date 2026-08-12 --json` | PATH absent ← `.results[]\|select(.option_symbol\|test("^PATH"))` | top-15 |
| `uw insights deep-dive --symbol PATH --date 2026-08-12 --json` | `.uw_screener` block (reused from phase-0.5) | whole name |

## Tool errors

- `uw hot-chains sweep-persistence --days 5 --top-n 20 --symbol PATH --date 2026-08-12 --json` → `Error: unknown flag: --date` / `error: unknown flag: --date`. This tool has no `--date` flag (trailing tool, anchors to latest available date per `uw CLI ≡ MCP parity` note — the latest date is the as-of date 2026-08-12 here, so no reproducibility gap for this run). Re-ran without `--date`; succeeded.

## DATA NOTE / CORRECTION

<none — first read stood>

## Verdict for downstream phases

- **Bias from this phase:** mixed / neutral (whole-tape net_flow ≈ flat,
  largest persistent chain is explicitly two-sided)
- **Conviction:** 2/5 (capped low per phase-0.5's `BUSY_NAME_NORMAL_DAY`;
  further capped by zero smart-money-flow presence and a two-sided dominant
  chain)
- **Three things later phases should remember:**
  1. The 2028-12-15 $10/$12 put LEAP chain is the dominant flow story
     ($8.47M/5 sessions) but is genuinely two-sided — treat as
     hedge/spread/MM-inventory activity, not a directional signal, unless
     phase-2 dark pool or phase-3 OI shows a one-sided net position building
     underneath it.
  2. Whole-tape net_flow is essentially zero (−$44,378 on $3.33M gross) —
     don't let any single top-N print read as "the tape," the top-25 is only
     ~20% of the day's gross premium.
  3. No smart-money-flow or elevated sweep-ratio anywhere in the market-wide
     screens for PATH today.
- **Open questions:** Does phase-2 dark pool activity or phase-3 OI-by-strike
  show a net change in the $10/$12 LEAP puts (i.e., is one side of the
  sweep flow actually opening while the other closes, netting to a real
  directional position despite the balanced dollar sweep totals)? Is there an
  identifiable counterparty pattern (e.g., a known collar program) behind the
  5-day persistence?
