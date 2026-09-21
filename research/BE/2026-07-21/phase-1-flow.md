# Phase 1 — Options Flow

**Ticker:** BE
**As-of date:** 2026-07-21
**Generated:** 2026-07-22T08:05:00Z
**Upstream phases cited:** phase-0.5-context.md, phase-0-intake.md

## Summary

BE's tape is **net bullish (+$25.5M directional premium) but the bullishness is
built from put-SELLING, not call-buying** — resolving the phase-0.5 divergence
(P/C volume 2.05 yet net premium bullish). The aggressive directional conviction
sits in **~$29.5M of Jan-2027 LEAP calls** (350/480/500 strikes, multi-leg),
while the earnings-window expression is **~$25.7M of net put-writing** at
197.5–230 (harvesting 98.8-rank IV, building a floor) plus a cheap deep-OTM tail
lottery. Flow is a **persistent 5/5-session campaign** ($648M 5-day sweep
premium) and institutional-sized (single $17M LEAP block, $12M put-write block),
so it is real positioning, not thin-tape noise — but the near-term stance reads
more "sell the elevated vol / hold the line into earnings" than "chase a
breakout."

## Key signals

- **Whole-tape net_flow +$25,457,620** (bullish 117.0M − bearish 91.5M); net call
  premium only +$4.8M (call 127.2M vs put 122.4M) `[FLOW:insights_deep_dive]`
- **Puts net SOLD ~$25.7M** on sweeps: ask-side (bought) $18.3M vs bid-side (sold)
  **$44.0M** — dominant action is put-writing at 197.5/215/230 `[FLOW:sweeps]`
- **$29.5M Jan-2027 LEAP calls** — 350C $17.2M (Δ0.51), 480C $7.8M, 500C $4.5M,
  all `no_side` multi-leg → bullish call ladder/spread `[FLOW:top_premium_trades]`
- **5/5 sessions in top-sweep names**, consistency_score 1.0, 5-day sweep premium
  **$648.3M**, dominant_direction *mixed* `[FLOW:sweep_persistence]`
- **Tail-hedge lottery:** 110P 7/24 = 18,478 contracts for only $160k (vol/OI
  50.6); deep-OTM puts 105–115 carry 280–308% IV `[FLOW:iv_outliers]`

## Detailed findings

### Whole-tape aggregate (read the top-N below against this) `[FLOW:insights_deep_dive]`

| Field | Value |
|-------|-------|
| `call_premium` | $127,219,013 |
| `put_premium` | $122,382,167 |
| net call premium | **+$4,836,846** (mild) |
| `bullish_premium` | $117,000,142 |
| `bearish_premium` | $91,542,522 |
| derived **`net_flow`** | **+$25,457,620** (bullish) |
| `call_volume` / `put_volume` | 51,463 / 105,286 |
| `put_call_ratio` | 2.0459 |
| `iv_rank` | 98.78 · `implied_move_perc` 10.6% |

Reconciliation of the P/C-2.05-vs-bullish divergence (phase-0.5 open question):
put volume is 2× call volume **because puts are being written** — the sweep tape
below shows $44.0M puts hit the bid (sold) vs $18.3M lifted the ask (bought). Net
premium is bullish primarily via that put-selling, not via call demand (net call
premium only +$4.8M).

### Sweeps — ask (bought) vs bid (sold) `[FLOW:sweeps]`

| Type | Ask/bought | Bid/sold | Net |
|------|-----------|----------|-----|
| Calls | $12.37M (5,568) | $13.74M (4,121) | ≈ −$1.4M (balanced) |
| Puts | $18.30M (17,460) | **$44.02M (18,122)** | **−$25.7M sold (bullish)** |

Largest bid-side (sold) puts: **197.5P 7/31 $12.3M**, 230P 8/14 $8.9M, 215P 7/31
$5.8M — a put-write campaign establishing a floor ~197.5–215 through the earnings
window. Also $300 calls **sold** (Sep $2.78M, Aug $2.77M) → mild upside
call-writing near $300. Top ask-side (bought) prints are near-dated puts
(197.5/215/165/210), i.e. two-sided put churn — consistent with the *mixed*
persistence tag.

### New positioning (vol/OI ≥ 3) `[FLOW:unusual_volume]`

| Contract | vol | OI | vol/OI | premium |
|----------|-----|----|--------|---------|
| **350C 2027-01-15** | 3,314 | 672 | 4.9 | **$17.54M** (LEAP call accumulation) |
| 110P 2026-07-24 | 18,478 | 365 | **50.6** | $0.16M (cheap tail lottery) |
| 230P 2026-08-14 | 1,989 | 73 | 27.2 | $9.47M (post-ER put write) |
| 215P 2026-07-31 | 2,424 | 411 | 5.9 | $8.02M (put write) |
| 185P 2026-07-24 | 5,171 | 1,018 | 5.1 | $1.37M |

New-money opening is put-heavy in the earnings window (all written per sweeps),
with the one large *call* opener being the 350 LEAP.

### Largest premium prints `[FLOW:top_premium_trades]` / Greeks `[FLOW:greek_screener]`

| Type | Strike | Expiry | Premium | Side | Δ | IV |
|------|--------|--------|---------|------|---|----|
| call | 350 | 2027-01-15 | **$17.23M** | no_side | 0.51 | 133% |
| call | 480 | 2027-01-15 | $7.79M | no_side | 0.36 | 130% |
| call | 500 | 2027-01-15 | $4.53M | no_side | 0.35 | 129% |
| put | 230 | 2026-08-14 | $1.25M | bid (sold) | −0.45 | 183% |
| put | 190/200 | 2026-07-31 | $1.03M/$1.01M | bid (sold) | −0.27/−0.31 | 265%/263% |
| call | 210 | 2026-08-21 | $0.98M | bid (sold) | 0.64 | 178% |

The three `no_side` LEAP calls ($29.5M total) are the dominant premium event — a
long-dated bullish ladder (long 350 financed partly by writing 480/500, net ~$4.9M
debit if a spread; outright it is ~$29.5M of upside conviction targeting +55–120%
by Jan-2027). LEAP-heavy → strong institutional conviction but **low short-term
tradeability** (>170 DTE); it does not drive the earnings-window trade.

### IV outliers `[FLOW:iv_outliers]`

Highest IV is concentrated in deep-OTM near-dated **puts** (105/110/115 strikes,
7/24–7/31, IV 280–308%) — the crash-hedge/lottery tier, cheap in dollars. One
365C 7/24 at 211%. This is wing demand (tail protection), not directional ATM
conviction.

### Smart-money-flow `[FLOW:smart_money_flow]`

BE did **not** appear in the market-wide bullish or bearish top-10 on this date —
consistent with phase-0.5's finding that BE's turnover (1.2× avg) is not
extreme; its signal is in the directional *lean*, not raw volume. No additional
ask/bid imbalance signal beyond the sweep read above.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|------------------|--------------------------|-----------|
| `insights deep-dive --symbol BE --date 2026-07-21` | net_flow=+$25.46M ← `.uw_screener.bullish_premium − .uw_screener.bearish_premium`; net call prem +$4.84M ← `call_premium − put_premium`; P/C 2.046 ← `.put_call_ratio` | whole-tape |
| `options-flow sweeps --symbol BE --side ask --min-premium 100000` | put bought $18.30M, call bought $12.37M ← `group_by(option_type)｜sum(.total_premium)` | top-25 |
| `options-flow sweeps --symbol BE --side bid --min-premium 100000` | put sold **$44.02M**, call sold $13.74M ← same | top-25 |
| `options-flow unusual-volume --symbol BE --min-vol-oi-ratio 3` | 350C 27' vol/OI 4.9 $17.54M; 110P 50.6 ← `.results[].vol_oi_ratio` | 13 rows |
| `options-flow top-premium-trades --symbol BE` | 350C 27' $17.23M no_side ← `.results｜sort_by(-.premium)` | top-25 |
| `options-flow iv-outliers --symbol BE` | 110P IV 3.084 ← `.results[].avg_iv` | 15 |
| `options-flow greek-screener --symbol BE --sort-by premium` | 350C Δ0.51 vega0.63 ← `.results[].delta/.vega` | 15 |
| `hot-chains sweep-persistence --days 5 --symbol BE` | sessions_in_top 5, consistency 1.0, 5d prem $648.3M, mixed ← `.results[]｜select(.ticker=="BE")` | 1 |
| `hot-chains smart-money-flow --direction bullish/bearish` | BE not in top-10 either dir | 10+10 |

## Tool errors

- `hot-chains sweep-persistence … --date 2026-07-21` → `unknown flag: --date`. Re-run
  without `--date`; as-of (2026-07-21) equals the latest available date so the
  trailing-window read is point-in-time-correct here (per uw-cli-parity note).

## DATA NOTE / CORRECTION

- First sweep jq assumed fields `total_volume`/`open_interest`/`avg_iv`; the actual
  sweep schema is `total_size`/`trade_count` (no OI/IV). Re-read with correct paths;
  all sweep premium figures above are from validated `.total_premium` sums.
- top-premium schema is `premium`/`side`/`size` (not `total_premium`/`total_volume`).
  Re-read; LEAP-call premiums confirmed via `.results｜sort_by(-.premium)`.

## Verdict for downstream phases

- **Bias from this phase:** **bullish**, but *put-write/LEAP-driven*, not a call-chase.
- **Conviction:** **3.5 / 5** — real institutional positioning (5-session campaign,
  $17M+$12M blocks) and record self-pctile directional lean, but the near-term
  expression is income/floor + it's only 1.2× volume, so not a max-conviction breakout.
- **Three things later phases must remember:**
  1. Bullishness = **put-selling** (net −$25.7M puts) + **$29.5M Jan-2027 LEAP
     calls**; near-term is "sell rich IV / hold ≥197.5–215," not chase.
  2. Key strikes: **put floor 197.5–230** (written), **upside caps 300 (written)
     / LEAP targets 350/480/500**; earnings 2026-07-28 anchors all near-dated flow.
  3. 5/5-session persistent sweep campaign, $648M 5-day, **mixed** direction —
     two-sided (write puts + buy LEAP calls), not clean one-way.
- **Open questions:** Is the **dark pool** confirming accumulation at these levels
  (phase 2 — DP total_premium was $794.9M, avg 222.4)? Where are the **OI walls /
  max-pain** that the put-writers are leaning on (phases 3–4)? Is the LEAP block a
  spread or outright (affects how bullish to read it)?
