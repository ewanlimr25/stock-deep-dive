# Phase 1 — Options Flow

**Ticker:** BABA · **As-of:** 2026-07-23 · **Underlying:** $114.99 (from top-premium block)
**Generated:** 2026-07-24
**Upstream:** phase-0.5-context.md — `[CTX: unusual_verdict = BUSY_NAME_NORMAL_DAY]`,
net-dir universe pctile 1.5 (bearish extreme), self_pctile_net_dir 43.7.

## Summary

The BABA tape is **two-sided with a persistent bearish lean.** Raw premium is
call-heavy (call $39.24M vs put $26.01M, PCR 0.372 by volume) but the *directional*
read is marginally **net bearish** — bullish premium $23.50M < bearish premium $25.18M
(**net_flow −$1.68M**), meaning much of the call premium is non-aggressive (ITM blocks /
spreads / writes), not conviction upside buying. The single cleanest directional signal
is **sweep-persistence: BABA sat in the top sweep names 5/5 sessions with consistency
1.0, dominant_direction BEARISH, $76.53M total sweep premium** — a genuine multi-session
bearish campaign into the 2026-07-23 print. Per the phase-0.5 BUSY_NAME_NORMAL_DAY
verdict, magnitude is discounted and this phase's downstream conviction is **capped at
`+`** (`rubrics/confluence-scoring.md`).

## Key signals

- **5-session bearish sweep campaign** — `consistency_score 1.0`, `sessions_in_top 5`,
  `total_sweep_premium $76.53M`, `dominant_direction bearish` `[FLOW:sweep_persistence]`
- **Net directional premium marginally bearish** — bull $23.50M vs bear $25.18M
  (net −$1.68M) despite call-heavy raw premium `[FLOW:insights_deep_dive]`
- **Top ask-side sweep is a long-dated bearish/protective put** — 2028-12-15 **105 PUT**,
  $2.85M, 1,315 ctr, avg $21.66 `[FLOW:sweeps ask]`
- **Near-term new positioning skews to puts** — PUT 106 (exp 07-31, 2,660 vol, vol/OI
  26×), PUT 112 (vol/OI 46.6×), PUT 101 alongside some CALL 99/101/102 `[FLOW:unusual_volume]`
- **All IV outliers are 0DTE OTM puts** (129/130/128 exp 07-24, IV 113–196%) — pin
  noise, discounted, but directionally all puts `[FLOW:iv_outliers]`

## Detailed findings

### Whole-tape aggregate (the anchor — top-N read against this) `[FLOW:insights_deep_dive]`

| Metric | Value |
|--------|-------|
| call premium | $39.24M |
| put premium | $26.01M |
| **bullish premium** | **$23.50M** |
| **bearish premium** | **$25.18M** |
| **derived net_flow (bull−bear)** | **−$1.68M (net bearish)** |
| call volume / put volume | 103,588 / 38,575 |
| put/call ratio | 0.372 (call-heavy by volume) |
| iv_rank / iv30d | 61.16 / 47.2% |

Read: call *volume* and call *premium* dominate, but net *directional* premium is
marginally bearish. The gap = call premium that is not aggressive upside buying (ITM
blocks, spreads, overwrites). Do **not** call this a bullish tape off the call-premium
headline (audit 2026-05-25 §3 lesson). Universe net-dir percentile 1.5 (phase-0.5) —
cross-sectionally BABA is at the bearish extreme today.

### Sweeps (ask vs bid) `[FLOW:sweeps]`

- **Ask-side (aggressive buying), top-25:** call $8.59M / put $6.01M.
- **Bid-side (aggressive selling), top-25:** call $8.95M / put $6.19M.
- Roughly balanced, marginally more bid-side (selling). **Largest single sweep = ask-side
  2028-12-15 105 PUT, $2.85M** — a long-dated protective/bearish structure.
- **Persistence:** BABA 5/5 sessions in top sweep names, consistency 1.0,
  **dominant_direction bearish**, $76.53M cumulative `[FLOW:sweep_persistence]`.
- `smart-money-flow`: **no BABA rows in top-10 either direction** — not a market-wide
  smart-money leader on 2026-07-23 (do not re-run looser).

### New positioning (unusual vol, vol/OI ≥ 3) `[FLOW:unusual_volume]`

| Type | Strike | Expiry | Vol | OI | vol/OI | Premium |
|------|--------|--------|-----|----|--------|---------|
| PUT | 112 | 2026-08-21 | 326 | 7 | 46.6× | $147k |
| PUT | 106 | 2026-07-31 | 2,660 | 102 | 26.1× | $143k |
| CALL | 99 | 2026-08-14 | 130 | 5 | 26.0× | $200k |
| CALL | 101 | 2026-08-14 | 250 | 12 | 20.8× | $358k |
| PUT | 101 | 2026-08-21 | 621 | 37 | 16.8× | $73k |
| CALL | 113 | 2026-08-28 | 146 | 9 | 16.2× | $115k |

Genuinely mixed new positioning — highest-volume new put is the near-dated **106
(2,660 ctr)**; calls cluster at 99–102 (Aug). Two-sided, near-term put-skewed.

### Largest premium prints `[FLOW:top_premium_trades]` / `[FLOW:greek_screener]`

| Type | Strike | Expiry | Premium | Δ | Side |
|------|--------|--------|---------|---|------|
| CALL | 105 | 2026-12-18 | $2.96M | 0.69 | no_side (block) |
| CALL | 105 | 2026-11-20 | $1.73M | 0.69 | no_side (block) |
| CALL | 140 | 2027-01-15 | $1.44M | 0.34 | no_side (block) |
| PUT | 105 | 2026-12-18 | $1.12M | −0.30 | no_side (block) |
| CALL | 115 | 2026-10-16 | $0.79M | 0.56 | ask |
| PUT | 115 | 2026-10-16 | $0.75M | −0.44 | ask |

The four largest are `no_side` blocks (ambiguous — could be call spreads, ITM
call rolls, or a risk-reversal: note the paired 105 Dec call **and** put). The ask-side
**115 Oct call + put** reads as a **long-straddle / vol buy around the $115 level** (spot
$114.99). Only genuinely aggressive *directional* upside print is the OTM **140 Jan-27
LEAP call** ($1.44M, Δ0.34).

### IV outliers + Greeks `[FLOW:iv_outliers]`

All top outliers are **0DTE (exp 2026-07-24) OTM puts** — 129 (IV 196%), 130 (146%),
128 (176%), 126 (113%). Classic 0DTE pin/hedge noise — **discounted**; directionally all
puts, consistent with the mild bearish lean but not a standalone signal. Greek screener
top prints match the premium table (biggest gamma on the ATM 115 Oct).

## Tool calls (audit)

| Datapoint | Command | jq path |
|-----------|---------|---------|
| whole-tape aggregate | `uw insights deep-dive --symbol BABA --date 2026-07-23` | `.uw_screener.{call_premium,put_premium,bullish_premium,bearish_premium,put_call_ratio}` |
| ask/bid sweeps | `uw options-flow sweeps --symbol BABA --side ask\|bid --min-premium 100000 --top-n 25 --date 2026-07-23` | `.results[].{option_type,total_premium,strike,expiry}` |
| new positioning | `uw options-flow unusual-volume --symbol BABA --min-vol-oi-ratio 3 --top-n 25 --date 2026-07-23` | `.results[].{strike,vol_oi_ratio,total_volume,open_interest}` |
| top premium | `uw options-flow top-premium-trades --symbol BABA --top-n 25 --date 2026-07-23` | `.results[].{option_type,strike,premium,side,delta}` |
| IV outliers | `uw options-flow iv-outliers --symbol BABA --top-n 15 --date 2026-07-23` | `.results[].{strike,avg_iv,expiry}` |
| sweep persistence | `uw hot-chains sweep-persistence --days 5 --top-n 20 --symbol BABA` (no --date; trailing→latest 2026-07-23) | `.results[0].{consistency_score,dominant_direction,total_sweep_premium}` |
| smart-money-flow | `uw hot-chains smart-money-flow --direction bullish\|bearish --top-n 10 --min-volume 500 --date 2026-07-23` | `.results[] \| select(.option_symbol\|startswith("BABA"))` → none |

## Tool errors

- `sweep-persistence` rejects `--date` (`unknown flag: --date`) — re-ran without it; this
  trailing tool anchors to the latest available date (= 2026-07-23 = as-of), so the
  5-session window ends at the as-of date. Recorded per `[[uw-cli-mcp-parity]]`.
- Initial `iv-outliers` jq used `.implied_volatility`; the field is `.avg_iv`/`.max_iv` —
  re-parsed cleanly. No number transcribed from the errored buffer.

## Verdict for downstream

- **Net bias:** **MIXED, bearish-leaning.** Directional premium marginally bearish
  (−$1.68M); the one clean thread is the 5-session bearish sweep persistence ($76.5M).
  Call-premium headline is NOT bullish confirmation (non-aggressive blocks).
- **Conviction: 2/5** — two-sided tape on a BUSY_NAME_NORMAL_DAY; the bearish signal is
  persistent but modest, offset by real two-sided call blocks and a $115 straddle.
  Downstream confluence capped at `+`.
- **Three datapoints later phases must remember:**
  1. **5-session bearish sweep persistence** — consistency 1.0, $76.53M, dominant bearish.
  2. **Net directional premium −$1.68M** (bull $23.50M < bear $25.18M) despite call-heavy
     raw premium — the call premium is not aggressive directional buying.
  3. **Spot $114.99**; the $105 and $115 strikes are the battleground (105 = big Dec call
     blocks + 2028 put; 115 = Oct straddle). Near-term new positioning put-skewed (106/112/101).
- **Open questions:** Is the dark pool confirming distribution (bearish) or absorbing
  (accumulation)? Where are the OI walls — does 105 support / 115–120 cap the tape?
  Is IV rank 61 rich enough that premium-selling structures beat directional?
