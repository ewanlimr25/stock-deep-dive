# Phase 1 — Options Flow

**Ticker:** NOW
**As-of date:** 2026-07-17
**Generated:** 2026-07-19 (run) for as-of 2026-07-17
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md

## Summary

The tape is **mixed / mildly bullish but low-conviction — classic pre-earnings vol
positioning, not directional intent.** The whole-tape aggregate is call-heavy
(call $22.67M vs put $18.04M, P/C 0.632) and net-bullish by a thin +$2.21M, and
ask-side sweeps are call-led ($6.2M). But the **largest single prints lean put-side**
($4.70M put vs $2.91M call in the top-25), dominated by **Jan-2027 104 & 72 puts
sold at the bid** — most consistent with premium-writing into **IV rank 96.9** ahead
of **earnings 2026-07-22**, and the Greek-weighted tape is essentially flat
(−$89k net delta-notional). Per phase-0.5 this is a **BUSY_NAME_NORMAL_DAY**
(volume 0.59× average), so magnitude is discounted and this phase is capped at `+`.

## Key signals

- Whole-tape mildly bullish: **net_flow = +$2.21M** (bullish $18.75M − bearish
  $16.54M), **P/C 0.632**, call-heavy `[FLOW:insights_deep_dive]`.
- Largest prints are **bid-side puts**: top-25 put premium $4.70M > call $2.91M;
  **put-bid $3.67M** vs call-ask $0.58M — Jan-2027 104P ($942k+$626k) & 72P ($942k)
  sold at bid `[FLOW:top_premium_trades]`.
- Ask-side call sweeps present but modest: **$6.2M / 25 prints**, spread across
  90/101/105/113/115/120 strikes `[FLOW:sweeps ask]`.
- **Delta-neutral aggressive tape:** net_delta_notional **−$89k** on the top-15
  greek-sorted prints `[FLOW:greek_screener]`.
- **Persistent but non-directional:** NOW in sweep-persistence top all **5/5
  sessions**, $106.2M 5-day sweep premium, **dominant_direction = "mixed"**
  `[FLOW:sweep_persistence]`. **No** smart-money-flow signal (absent from bullish
  AND bearish top-10) `[FLOW:smart_money_flow]`.

## Detailed findings

### Whole-tape aggregate (read the top-N against this) `[FLOW:insights_deep_dive]`

| Field | Value |
|---|---|
| call_premium | $22.67M |
| put_premium | $18.04M |
| bullish_premium | $18.75M |
| bearish_premium | $16.54M |
| **net_flow (derived)** | **+$2.21M** (bullish − bearish) |
| put_call_ratio | 0.632 (call-heavy) |
| call_volume / put_volume | 63,857 / 40,365 |
| iv_rank / iv30d | 96.9 / 0.759 |
| total_open_interest | 1,514,177 |
| next_earnings_date | 2026-07-22 (5 days out) |

Read: call-heavy and thinly net-bullish, but the magnitude is modest for a top-1%
absolute-premium name (phase-0.5: 17.6th self-pctile total premium) — so the whole
tape is *quietly* bull-leaning, not a directional surge.

### Sweeps (ask vs bid) `[FLOW:sweeps]`

- **Ask-side (buyer-initiated):** 25 prints, **$6.21M**, **call-dominated** — top:
  101C 0DTE $448k, 105C 7/24 $424k, 90C 0DTE $392k, 120C 10/16 $338k, 90C Jan-27 $296k,
  115C 8/21 $288k. Genuine call buying, but fragmented across strikes/expiries.
- **Bid-side (seller-initiated):** 25 prints, **$8.97M**, **put-dominated** — top:
  104P Jan-27 **$1.64M**, 72P Jan-27 **$1.07M**, 105P 9/18 $591k, 100C 2028 $447k,
  115P 10/16 $427k. The Jan-2027 puts hit the bid = **written/sold** → premium
  collection into elevated IV (neutral-to-bullish), *or* long-put liquidation.
  Ambiguous; delta-weighted read (below) resolves it as roughly flat.

### New positioning (unusual vol/OI ≥3) `[FLOW:unusual_volume]`

8 rows, **mixed and 0DTE-heavy**: 103P 0DTE (vol 5,295, $176k) & 104C 0DTE
(vol 2,936, $174k) are pin/expiry noise; 113C 8/14 (vol/oi 13.4, tiny $62k), 198C
9/18 (far-OTM lotto, $31k), 83P 7/24, 105P 8/28, 107P 8/7. No single new-position
theme — puts and calls both represented. Discount the 0DTE rows.

### Largest premium prints (top-25) `[FLOW:top_premium_trades]`

| type | strike | expiry | premium | side | delta |
|---|---|---|---|---|---|
| put | 104 | 2027-01-15 | $942,300 | bid | −0.41 |
| put | 72 | 2027-01-15 | $942,084 | bid | −0.15 |
| put | 100 | 2026-07-31 | $636,000 | no_side | −0.39 |
| put | 104 | 2027-01-15 | $626,400 | bid | −0.41 |
| call | 135 | 2026-09-18 | $480,000 | no_side | +0.21 |
| call | 100 | 2028-01-21 | $343,300 | bid | +0.69 |

Split: call $2.91M vs **put $4.70M**; **put-bid $3.67M** is the single biggest bucket.
Theme = large Jan-2027 put selling at the bid (write premium into IV rank 96.9).

### IV outliers + Greeks

- **IV outliers = 0DTE pin noise:** top rows are 2026-07-17 OTM calls with avg_iv
  20.9 / 5.3 (i.e. 2090% / 530% — meaningless expiry-day marks). Discard `[FLOW:iv_outliers]`.
- **Greeks:** net_delta_notional **−$89k** on $6.2M top-15 premium — the aggressive
  tape is **delta-neutral with a faint negative tilt**, consistent with vol/premium
  positioning rather than a directional bet `[FLOW:greek_screener]`.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows |
|---|---|---|
| `uw insights deep-dive --symbol NOW --date 2026-07-17` | net_flow=+$2.21M, P/C=0.632, call$22.67M/put$18.04M ← `.uw_screener.*` | whole-tape |
| `uw options-flow sweeps --side ask --min-premium 100000 --top-n 25` | sum $6.21M, call-led ← `.results[].total_premium` | 25 |
| `uw options-flow sweeps --side bid --min-premium 100000 --top-n 25` | sum $8.97M, put-led (104P Jan27 $1.64M) ← `.results[]` | 25 |
| `uw options-flow unusual-volume --min-vol-oi-ratio 3 --top-n 25` | 8 mixed rows, 0DTE-heavy ← `.results[]` | 8 |
| `uw options-flow top-premium-trades --top-n 25` | put $4.70M > call $2.91M; put-bid $3.67M ← `.results[].premium/.side/.option_type` | 25 |
| `uw options-flow greek-screener --sort-by premium --top-n 15` | net_delta_notional −$89k ← `Σ .delta*.premium` | 15 |
| `uw options-flow iv-outliers --top-n 15` | all 0DTE pin noise ← `.results[].avg_iv` | 15 |
| `uw hot-chains sweep-persistence --days 5 --symbol NOW` | 5/5 sessions, $106.2M, dir="mixed" ← `.results[].dominant_direction` | 1 |
| `uw hot-chains smart-money-flow --direction bullish/bearish` | NOW absent both ← filter `.ticker=="NOW"` | 0 |
| `uw hot-chains sweep-ratio --min-sweep-ratio 0.3` | NOW absent ← filter | 0 |

## Tool errors

- `uw hot-chains sweep-persistence … --date 2026-07-17` → `unknown flag: --date`
  (this leaf has no `--date`; it is a trailing 5-day window anchored to latest).
  Re-run **without** `--date` succeeded. Per known behavior, this is a trailing
  (not as-of-reproducible) window — noted so phase 5/9 don't treat it as strictly
  as-of.

## DATA NOTE / CORRECTION

`top-premium-trades` / `greek-screener` use field `premium` (not `total_premium`)
and `side` (`ask`/`bid`/`no_side`); first jq assumed `total_premium` and returned
$0 sums. Corrected to `.premium` before any value was transcribed — no wrong number
persisted.

## Verdict for downstream

- **Net bias:** **mixed, faintly bullish** (call-heavy whole tape + call ask-sweeps,
  offset by large bid-side put writing and flat delta). Treat as **pre-earnings vol
  positioning**, not directional conviction.
- **Conviction:** **2 / 5** (persistent flow but non-directional; busy-name normal
  day; volume 0.59× avg).
- **Three datapoints later phases must remember:**
  1. **Delta-neutral aggressive tape (−$89k net delta), P/C 0.632** — no directional
     bet is being expressed with size; the theme is IV/premium, not price.
  2. **Largest prints = Jan-2027 104/72 puts SOLD at bid ($3.67M put-bid bucket)** —
     premium-writing into IV rank 96.9; watch if phase-3 OI confirms these as new
     short-put positions (bullish/neutral) vs opening hedges (bearish).
  3. **5-day sweeps persistent (5/5, $106M) but "mixed"** — flow is habitual for
     NOW, not a fresh directional campaign.
- **Open questions:** Is dark pool (phase-2) confirming any directional lean, or is
  it also balanced/quiet? Do the Jan-27 bid-side puts show up as OI *builds* (writes)
  or OI *reductions* (closes) in phase-3? What's the earnings straddle-implied move
  (phase-4/9), given IV rank 96.9?
