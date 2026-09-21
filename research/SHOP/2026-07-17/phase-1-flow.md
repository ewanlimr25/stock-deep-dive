# Phase 1 — Options Flow

**Ticker:** SHOP
**As-of date:** 2026-07-17
**Generated:** 2026-07-19 (run) · as-of 2026-07-17
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md

## Summary

SHOP's tape is **genuinely two-sided with a slight short-dated bearish tilt**, not
a clean directional flow. Whole-tape aggregate is **mildly net-bearish**
(bullish_premium $7.28M < bearish_premium $8.36M → **net_flow −$1.08M**) even though
**call premium dominates** ($11.09M call vs $6.35M put). Among the top-25 prints
buyers were put-heavy ($1.87M puts bought vs $1.31M calls bought), led by an
aggressive near-ATM **$121 Jul-24 put bought for $702K** — but that is offset by a
larger-size **$116 Jul-24 put sold for $613K** (put-writing at support) and a
bullish deep-ITM **$95 Jan-2027 call bought (~$483K, Δ0.8)**. Consistent with
phase-0.5's `BUSY_NAME_NORMAL_DAY` — persistent sweep name (5/5 sessions in top
sweeps) but `dominant_direction = mixed`. Downstream conviction capped at `+`.

## Key signals

- **Whole-tape net_flow −$1.08M** (bullish $7.28M − bearish $8.36M); P/C 0.919;
  call premium 1.75× put premium. `[FLOW:insights_deep_dive]`
- **Largest aggressive print: $121 Jul-24 PUT bought, $702K, 2,600 ct, Δ−0.37,
  ASK** — near-ATM short-dated put buying (bearish/protective). `[FLOW:top_premium_trades]`
- **Counter-print: $116 Jul-24 PUT sold, $613K, 5,200 ct, Δ−0.20, BID** — largest
  size of the day, put-writing defining **support at 116**. `[FLOW:top_premium_trades]`
- **Deep-ITM LEAP: $95 Jan-2027 CALL bought ~$483K (2 prints, Δ0.79–0.80), ASK** —
  bullish stock-replacement; vs **$150 Dec-18 PUT bought ~$710K (Δ−0.60), ASK**
  (bearish/deep-ITM). Two-sided institutional. `[FLOW:sweeps ask]`
- **Sweep-persistence: 5/5 sessions in top sweeps, consistency 1.0, total sweep
  premium $17.44M, `dominant_direction = mixed`.** `[FLOW:sweep_persistence]`

## Detailed findings

### Whole-tape aggregate (read the top-N against this) `[FLOW:insights_deep_dive]`

| Field (`.uw_screener`) | Value |
|---|---|
| call_premium | $11,090,325 |
| put_premium | $6,352,131 |
| bullish_premium | $7,276,693 |
| bearish_premium | $8,357,131 |
| **net_flow (derived bull−bear)** | **−$1,080,438** |
| put_call_ratio | 0.9185 |
| call_volume / put_volume | 30,886 / 28,370 |
| iv_rank / iv30d | 85.6 / 0.753 |

Reading: **call premium leads but the aggressor classification is net-bearish** —
the classic "calls sold / puts hit" ambiguity. Net_flow is only −$1.08M (32nd
self-percentile per phase-0.5) → a *mildly* bearish normal day, not a spike.

### Sweeps (ask vs bid) `[FLOW:sweeps]`

- **Ask-side (buyer-initiated) sweeps ≥$100K: $3.91M** — near-even split (puts
  ~$1.95M, calls ~$1.96M). Top: $150 Dec put $721K, $121 Jul-24 put $705K, $95
  Jan-27 call $558K, $130 Jul-24 call $494K.
- **Bid-side (seller-initiated) sweeps ≥$100K: $3.03M** — puts ~$1.35M, calls
  ~$1.68M. Top: $116 Jul-24 put $620K, $125 Sep put $298K.
- Within top-25 prints: ASK $3.18M vs BID $1.50M (buyers 2.1× sellers), but ASK is
  **put-heavy** ($1.87M vs $1.31M) → aggressive buyers slightly favour puts.

### New positioning (unusual vol, vol/OI) `[FLOW:unusual_volume]`

| Contract | Vol | OI | Vol/OI | Prem | Read |
|---|---|---|---|---|---|
| $116 Jul-24 PUT | 5,334 | 54 | 99 | $632K | New, **sold-to-open** (support write at 116) |
| $121 Jul-24 PUT | 2,636 | 140 | 19 | $713K | New, **bought-to-open** (ATM bearish/hedge) |
| $115 Jul-31 PUT | 1,025 | 211 | 5 | $237K | New put |
| $146–$148 Jul-24 CALLs | ~550 ea | 1–3 | 184–572 | ~$16K ea | Tiny OTM **lotto calls** (retail-ish) |

Dominant new flow = the dueling $116 (sold) / $121 (bought) Jul-24 puts. Jul-24 is
**pre-earnings** (next_earnings 2026-08-05), so these are near-term directional/
protective, **not** earnings-vol plays.

### IV outliers + Greeks `[FLOW:iv_outliers]`

IV-outlier list is **0DTE noise** — every top row is the Jul-17 (same-day) expiry
(call $115 IV 4.64, put $114 IV 1.77, etc.) with tiny premium; **discount as
expiring gamma noise.** iv_rank 85.6 elevated but no clean directional IV skew signal.

### Smart-money-flow (market-wide) `[FLOW:smart_money_flow]`

SHOP appears in **neither** the bullish nor bearish market-wide top-40 — no
standout aggressive ask/bid imbalance vs the universe. Consistent with phase-0.5's
"outside top-60." No smart-money flow detected in the top-40 on this date.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw insights deep-dive --symbol SHOP --date 2026-07-17` | net_flow=−$1.08M ← `.uw_screener.bullish_premium − .uw_screener.bearish_premium`; P/C 0.9185 ← `.put_call_ratio` | whole-tape |
| `uw options-flow sweeps --symbol SHOP --side ask --min-premium 100000 --top-n 25` | ask_sum $3.91M ← `[.results[].total_premium]\|add` | 12 |
| `uw options-flow sweeps --symbol SHOP --side bid …` | bid_sum $3.03M | 14 |
| `uw options-flow top-premium-trades --symbol SHOP --top-n 25` | $121 put ASK $702K ← `.results[]{side,premium,strike}` | 25 |
| `uw options-flow unusual-volume --symbol SHOP --min-vol-oi-ratio 3 --top-n 25` | $116 put vol 5334/oi 54 ← `.results[]{vol_oi_ratio}` | 15 |
| `uw options-flow iv-outliers --symbol SHOP --top-n 15` | all 0DTE Jul-17 ← `.results[].expiry` | 15 |
| `uw options-flow greek-screener --symbol SHOP --sort-by premium` | $121 put Δ−0.37 ← `.results[].delta` | 15 |
| `uw hot-chains smart-money-flow --direction bullish\|bearish --min-volume 500` | SHOP absent ← `select(.option_symbol\|startswith("SHOP"))` = 0 | 40 ea |
| `uw hot-chains sweep-persistence --days 5 --symbol SHOP` | 5/5 sessions, mixed ← `.results[0]{sessions_in_top,dominant_direction}` | 1 |

## Tool errors

- `uw hot-chains sweep-persistence … --date 2026-07-17` → `unknown flag: --date`.
  Re-ran without `--date` (trailing tool, anchors to latest = 2026-07-17). Value used.

## DATA NOTE / CORRECTION

First `jq` on `top-premium-trades`/`greek-screener` used field `total_premium`
(absent → $0). Re-read against the correct field `premium` (+ `side`). All top-print
premium/side numbers above trace to `.results[].premium` / `.results[].side`.

## Verdict for downstream phases

- **Bias from this phase:** MIXED, slight bearish tilt on the short-dated aggressor side.
- **Conviction:** 2/5 (two-sided; capped at `+` by phase-0.5 `BUSY_NAME_NORMAL_DAY`).
- **Three things later phases should remember:**
  1. net_flow **−$1.08M** (bullish $7.28M < bearish $8.36M) yet **call premium
     $11.09M >> put premium $6.35M** — aggressor-bearish, premium-call-heavy.
  2. The two decisive new positions are dueling Jul-24 puts: **$121 bought $702K
     (bearish)** vs **$116 sold $613K (support write)** → the market is pricing a
     **116–121 battle zone** into next week.
  3. Persistent sweep name (**5/5 sessions**) but `dominant_direction = mixed`;
     bullish counterweight is the deep-ITM **$95 Jan-27 call** LEAP.
- **Open questions:** Is the $121-put buying protective (dealer/hedge) or
  directional? Is dark pool confirming distribution near 123–125 (phase-2)? Where
  are the OI walls relative to the 116/121/130 strikes (phase-3)?
