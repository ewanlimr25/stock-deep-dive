# Phase 1 — Options Flow

**Ticker:** HOOD
**As-of date:** 2026-05-27
**Generated:** 2026-05-28T14:03:50Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md

## Summary

HOOD's tape on 2026-05-27 is **near-balanced with only a trivial bullish lean
(+$1.06M net directional)**, despite a headline call/put premium ratio of 3.6×.
That headline is a trap: the aggressor split (DuckDB §A, ex-0DTE) shows call premium
is almost evenly divided between buying ($17.6M ask) and selling/overwriting ($18.9M
bid), so the heavy call premium does **not** equal heavy call *buying*. The single
genuine standout is an ask-side **Dec-18 $75 call for $1.82M** (delta 0.61) — one
clean bullish print sitting on top of an otherwise two-sided tape. Consistent with
phase-0.5's `BUSY_NAME_NORMAL_DAY` verdict, conviction here is **low and capped at
`+`**.

## Key signals

- Whole-tape aggregate: call premium $42.6M vs put $11.7M, but **bullish $24.1M vs
  bearish $23.0M (net +$1.07M)**, P/C 0.36 [FLOW:insights_deep_dive].
- Aggressor split ex-0DTE: **call ask $17.6M ≈ call bid $18.9M** — call buying ≈ call
  selling; net directional reconstructs to +$1.06M [FLOW:aggressor_ex0dte DUCKDB].
- Largest clean buy: **Dec-18 $75C, $1.82M, ask-side, delta 0.61, vol 1,181** @15:30
  [FLOW:top_premium_trades] — a real ~7-month bullish bet.
- Largest single print is bid/no-side, not buying: **Aug-21 $90C $2.75M bid** (likely
  call writing) and **Jun-18 $80C $1.17M no-side vol 4,000** (block/spread leg)
  [FLOW:sweeps][FLOW:top_premium_trades].
- 5-day sweep persistence: HOOD in top sweep names **all 5 sessions** but
  **dominant_direction = mixed**, $82.3M total sweep premium [FLOW:sweep_persistence]
  — persistent activity, no persistent direction.

## Detailed findings

### Whole-tape aggregate (read everything below against this)

`uw insights deep-dive` `uw_screener` block [FLOW:insights_deep_dive]:
- call_premium **$42.55M**, put_premium **$11.75M** (ratio 3.6×)
- bullish_premium **$24.11M**, bearish_premium **$23.04M** → **net_flow +$1.07M**
- put_call_ratio **0.36**, call_volume 146,185, put_volume 52,995
- total_open_interest 1,846,299, IV30d 0.588, IV rank 23.2

The 3.6× call/put premium ratio looks bullish in isolation, but bullish vs bearish
premium is essentially flat. Reason (next subsection): much of the call premium is
sold, not bought.

### Aggressor split — the directional resolution (DuckDB §A, ex 0–1DTE)

[FLOW:aggressor_ex0dte DUCKDB] / [FLOW:delta_notional DUCKDB]:

| Type | Side | Trades | Contracts | Premium | Δ-notional |
|------|------|--------|-----------|---------|------------|
| call | ask  | 13,520 | 67,731 | **$17.61M** | +$0.160bn |
| call | bid  | 11,024 | 56,676 | **$18.88M** | +$0.142bn |
| call | mid  | 3,591  | 17,778 | $4.89M  | +$0.040bn |
| call | no_side | 1 | 4,000 | $1.17M | +$0.012bn |
| put  | ask  | 3,944  | 17,797 | $4.16M  | −$0.038bn |
| put  | bid  | 4,876  | 29,873 | **$6.49M** | −$0.071bn |
| put  | mid  | 1,317  | 5,325  | $1.09M  | −$0.010bn |

- **Bullish** (ask calls + bid puts) = $17.61M + $6.49M = **$24.10M**
- **Bearish** (bid calls + ask puts) = $18.88M + $4.16M = **$23.04M**
- **Net ≈ +$1.06M** — reconstructs the screener's +$1.07M almost exactly.

Takeaway: call buying ($17.6M) and call selling/overwriting ($18.9M) roughly cancel.
The only modest net positive comes from put *selling* ($6.5M bid puts vs $4.2M ask
puts), i.e. people collecting put premium — a mild, low-conviction bullish tilt.

### Sweeps (ask vs bid)

Both ask and bid sweep lists are **call-dominated** [FLOW:sweeps]:
- Ask side top: Dec-18 75C $2.50M, Jun-05 80C $0.60M, Jun-18 80C $0.58M, May-29 75C
  $0.57M — short-to-medium dated upside *buying*.
- Bid side top: **Aug-21 90C $2.75M** (OTM, bid → likely written/overwrite), May-29
  74P $1.09M (bid put → sold), Dec-18 75C $0.93M.
The two-sided call sweeping (buy near + write far-OTM upside) is a hallmark of
overwriting/spreading, not clean accumulation.

### New positioning (unusual vol, vol/OI ≥ 3)

[FLOW:unusual_volume] — concentrated in the **2026-07-02 expiry** (a cluster of puts
*and* calls each opening fresh, vol/OI 4–43, small premium) plus one large near-dated
position: **2026-05-29 (2DTE) $74P, vol 15,853 / OI 4,115, $1.42M, IV 0.707**
(elevated vs the ~0.57 chain). In top-premium this 74P prints repeatedly **bid-side**
($152K × n, vol 1,713) → consistent with **put selling** at a slightly-OTM 2DTE
strike (price 76.23), i.e. premium harvest, not a bearish bet. The 7/02 two-sided
cluster reads as straddle/strangle positioning around an event window, not direction.

### Largest premium prints (table)

| Time (UTC) | Type | Strike | Expiry | Premium | Side | IV | Read |
|-----------|------|--------|--------|---------|------|----|----|
| 15:30 | call | 75 | 2026-12-18 | $1.82M | **ask** | 0.68 | clean bullish buy (Δ0.61) |
| 18:36 | call | 80 | 2026-06-18 | $1.17M | no_side | 0.61 | block/spread leg (vol 4,000) |
| 15:14 | call | 75 | 2026-12-18 | $0.69M | mid | 0.68 | same name, mid |
| 17:49 | call | 90 | 2026-08-21 | $0.37M | bid | 0.65 | OTM call written |
| 14:50 | call | 75 | 2026-12-18 | $0.35M | bid | 0.68 | Dec 75C also being sold |
| 14:31 | call | 130 | 2028-01-21 | $0.34M | bid | 0.69 | far-OTM LEAP, bid (written) |

Note even the Dec-18 75C shows up on **both ask ($1.82M) and bid ($0.35M)** — some
of the day's marquee call line is being two-way traded, reinforcing the balanced read.

### IV outliers + Greeks

[FLOW:iv_outliers] returned only structural rows (IV/vol fields null in this cut) —
outliers sit in far wings (100C/185C, 55–61P 5/29) typical of low-liquidity strikes,
no actionable signal. [FLOW:greek_screener] (sorted by premium) confirms the premium
stack is **all calls**, deltas 0.34–0.77 (the Dec 75C at Δ0.61, the Jun 80C at
Δ0.40) — directional-delta exposure exists but is offset by the bid-side writing
above.

### Smart-money flow

[FLOW:smart_money_flow] returned **no HOOD rows** in either direction at min-volume
500 — HOOD is not among the day's ask/bid-imbalance leaders. Consistent with
phase-0.5 (rank 114 net bullish, below-average volume). Not re-run with looser
thresholds (per phase guidance).

## Tool calls (audit trail)

| Command | Result summary |
|---------|----------------|
| `uw insights deep-dive --symbol HOOD --date 2026-05-27 --json` | net_flow +$1.07M, call/put prem $42.6M/$11.7M, P/C 0.36 |
| `uw options-flow sweeps --symbol HOOD --side ask --min-premium 100000 --top-n 25 --date 2026-05-27` | call-dominated; top Dec-18 75C $2.50M |
| `uw options-flow sweeps --symbol HOOD --side bid ...` | call-dominated; top Aug-21 90C $2.75M (written) |
| `uw options-flow unusual-volume --symbol HOOD --min-vol-oi-ratio 3 --top-n 25 --date 2026-05-27` | 7/02 two-sided cluster + 5/29 74P 15.9k vol $1.42M IV0.71 |
| `uw options-flow top-premium-trades --symbol HOOD --top-n 25 --date 2026-05-27` | top print Dec-18 75C $1.82M ask |
| `uw options-flow iv-outliers --symbol HOOD --top-n 15 --date 2026-05-27` | wing strikes only, no signal |
| `uw options-flow greek-screener --symbol HOOD --top-n 15 --sort-by premium --date 2026-05-27` | premium stack all calls, Δ0.34–0.77 |
| `uw hot-chains smart-money-flow --direction bullish\|bearish --top-n 50 --min-volume 500 --date 2026-05-27` | no HOOD rows either side |
| `uw hot-chains sweep-persistence --days 5 --top-n 20 --symbol HOOD` | 5/5 sessions, dominant_direction=mixed, $82.3M |
| `uw hot-chains sweep-ratio --top-n 100 --min-volume 500 --min-sweep-ratio 0.3 --date 2026-05-27` | no HOOD rows |
| DuckDB §A aggressor split (ex-0DTE) | call ask $17.6M ≈ bid $18.9M; net +$1.06M |

## Tool errors

- `uw hot-chains sweep-persistence ... --date 2026-05-27` → `unknown flag: --date`.
  Re-run without `--date` (trailing tool anchors to latest available = 2026-05-27).
- `uw options-flow iv-outliers` returned null IV/volume fields in the parsed cut
  (structural rows only) — no usable IV outlier data this date.

## Verdict for downstream

- **Net bias from this phase:** **MIXED / slight bullish** (net +$1.06M is trivial;
  the only real edge is mild put-selling).
- **Conviction:** **2/5** (capped at `+` per phase-0.5 `BUSY_NAME_NORMAL_DAY`).
- **Three things later phases must remember:**
  1. The 3.6× call/put *premium* ratio is **not** directional — call buying ≈ call
     selling (ask $17.6M ≈ bid $18.9M). Do not treat heavy call premium as bullish.
  2. One genuine bullish print exists: **Dec-18 $75C $1.82M ask @15:30** (delta 0.61,
     IV 0.68) — phase-2 should check for dark-pool confirmation near 15:30Z; phase-3/4
     should watch 75/80 call strikes for OI build.
  3. Fresh two-sided positioning is clustering in **2026-07-02** (event-window
     straddle/strangle) — note earnings is 2026-07-29, so 7/02 is *not* an earnings
     play; it may front-run a catalyst. Mild **put-selling** (5/29 74P) is the bullish
     tilt.
- **Open questions:**
  - Is the $273.7M dark-pool premium (phase-0.5) confirming accumulation, or is it
    two-sided like the options tape? (phase-2)
  - Where is dealer gamma — does the 75/80 call wall pin price or fuel a squeeze?
    (phase-3/4)
