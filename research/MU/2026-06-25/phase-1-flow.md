# Phase 1 — Options Flow

**Ticker:** MU
**As-of date:** 2026-06-25
**Generated:** 2026-06-25
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md

## Summary

MU's whole-tape aggregate is **net bullish by dollars** — call premium $5.10B vs
put premium $1.83B (calls **2.79×**), net_flow **+$279M** (bullish−bearish), the #1
single-name net-bullish reading in the universe (see phase-0.5-context.md). But the
conviction is *premium-weighted, not breadth-weighted*: contract-count P/C is a
balanced **1.026**, and the top-N prints are genuinely **two-way** — large ask-side
call buys (Oct-1300 $13.5M, a 2028 700-strike LEAP $8.3M, a $31.5M deep-ITM
synthetic long) sitting alongside real put buying (a $10.3M ask-side ATM Mar-2027
1200 put and a $20.9M 1DTE 1220 put). Sweeps lean bullish (ask $701M vs bid $559M)
but are call-dominated and heavily 1DTE (gamma/pin), and `sweep-persistence` flags
MU's 5-session campaign as **`dominant_direction: mixed`**. Net read: constructive
post-earnings continuation flow, tempered by visible two-way/hedging activity —
**bullish, conviction 3/5**, not a clean one-sided tape.

Underlying ≈ **$1,165** (print `underlying_price` 1165.04).

## Key signals

- Whole-tape **net_flow +$279M**, call premium **2.79×** put premium `[FLOW:insights_deep_dive]`
- Largest single print: **ask-side** Oct-16 **1300 call, $13.5M**, delta 0.53, IV 95% `[FLOW:top_premium_trades]`
- Counter-signal: **ask-side** Mar-2027 **1200 ATM put, $10.3M** + new **1DTE 1220 put, $20.9M** `[FLOW:top_premium_trades / unusual_volume]`
- Sweeps: ask-side $701M > bid-side $559M (**+$142M ask lean**), but call-heavy & 1DTE `[FLOW:sweeps]`
- Persistent but undirected: MU in top sweeps **5/5 sessions, consistency 1.0, dominant_direction MIXED** `[FLOW:sweep_persistence]`

## Detailed findings

### Whole-tape aggregate `[FLOW:insights_deep_dive]` (read top-N against this)

| Field | Value |
|-------|-------|
| call_premium | $5,104,692,980 |
| put_premium | $1,830,644,189 |
| call/put premium ratio | **2.79×** (dollars decisively in calls) |
| bullish_premium | $3,447,623,492 |
| bearish_premium | $3,168,616,930 |
| **net_flow (derived bull−bear)** | **+$279,006,562** |
| call_volume / put_volume | 726,812 / 745,544 |
| put_call_ratio (volume) | **1.026** (balanced by count) |
| iv_rank | 77.07 (32.7th pctile of MU's own range — IV deflating post-earnings) |
| implied_move | 47.39 abs / **3.93%** |

The dollars say bullish (calls 2.79×, net +$279M); the contract count says balanced
(P/C 1.026). Reconciliation: a smaller number of large, expensive call positions vs
a broad, balanced two-way book. This is the signature of **institutional directional
call buying on top of an otherwise balanced retail/hedging tape** — real but not a
stampede.

### Sweeps (ask vs bid) `[FLOW:sweeps]`

- **Ask-side:** 25 sweeps, **$701.2M** total premium. Top: 1200/1100/1150/1250
  calls, mostly **exp 2026-06-26 (1DTE)** + some 7-02 / 7-17.
- **Bid-side:** 25 sweeps, **$559.4M** total premium. Same strikes (1100–1250
  calls), also 1DTE-heavy.
- Net ask lean **+$142M**, but both sides are calls at ATM strikes (1100–1250 vs
  $1,165 spot) and dominated by 1DTE — this is **gamma/pin sweep churn**, not clean
  directional accumulation. Discount the magnitude; the directional content is in
  the dated prints below, not the 1DTE sweeps.

### New positioning (unusual vol, vol/OI ≥ 3) `[FLOW:unusual_volume]`

| Type | Strike | Expiry | Vol | OI | Vol/OI | Premium |
|------|--------|--------|-----|----|--------|---------|
| **put** | **1220** | **2026-06-26 (1DTE)** | 6,178 | 53 | 116.6 | **$20.9M** |
| put | 150 | 2026-07-02 | 6,015 | 2 | 3007.5 | $6.1K (lotto) |
| call | 2230 | 2026-12-18 | 126 | 1 | 126 | $1.4M (far-OTM lotto) |
| call | 2390 | 2027-06-17 | 122 | 1 | 122 | $2.4M (far-OTM lotto) |
| call | 2390 | 2027-12-17 | 104 | 1 | 104 | $2.8M (far-OTM lotto) |

The one material new position is the **$20.9M 1DTE 1220 put** — a large near-ATM
short-dated put, read as a **hedge/short-term downside bet into 6-26**, not a
structural short (1DTE). The far-OTM 2200–2400 calls are single-contract lottery
tickets — institutional optionality but negligible size.

### Largest premium prints (table) `[FLOW:top_premium_trades / greek_screener]`

| Type | Strike | Expiry | Premium | Side | Δ | Read |
|------|--------|--------|---------|------|---|------|
| call | 1300 | 2026-10-16 | $13.5M | **ask** | 0.53 | bullish open (4mo OTM) |
| call | 1250 | 2026-12-18 | $11.3M | bid | 0.60 | call sold/closed |
| **put** | **1200** | **2027-03-19** | **$10.3M** | **ask** | −0.33 | **bearish/hedge open (9mo ATM put)** |
| call | 1010 | 2027-03-19 | $9.3M | bid | 0.75 | ITM call sold/closed |
| call | 1200 | 2026-07-17 | $8.4M | bid | 0.57 | call sold/closed |
| call | 700 | 2028-12-15 | $8.3M | **ask** | 0.88 | **deep-ITM LEAP, stock-replacement long** |
| call | 900 | 2026-09-18 | $7.3M | mid | — | ITM call |
| call | 1700 | 2026-10-16 | $7.2M | bid | — | OTM call sold (upside cap/write) |

Ask-side opens are bullish (Oct-1300, 2028-700 LEAP); bid-side calls (Dec-1250,
Jul-1200, Oct-1700) are sells/closes; and the **single largest non-call print is an
ask-side ATM put** ($10.3M, Mar-2027). The tape is buying upside *and* paying up for
downside protection — consistent with longs hedging a post-earnings run rather than
fresh one-way conviction.

### IV outliers + Greeks `[FLOW:iv_outliers / greek_screener]`

- IV-outliers are dominated by **deep-ITM pricing artifacts** (5/350/505 calls show
  IV 900–1140% — meaningless for deep ITM) and **OTM 1DTE lotto puts** (tiny
  premium). No clean directional IV-skew signal — note and discount.
- The $31.5M **5-strike call, exp 7-17** is effectively a **synthetic long stock**
  (delta ≈ 1) — directionally bullish but a financing/replacement trade, not a
  speculative call.
- Greeks on the dated prints: Oct-1300 call vega 2.58, Mar-2027 put vega 3.74 — the
  big positions carry real vega; with IV deflating post-earnings, long-vega
  positions face a headwind.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|------------------|--------------------------|-----------|
| `insights deep-dive --symbol MU --date 2026-06-25` | call_prem $5.10B / put_prem $1.83B / net_flow +$279M ← `.uw_screener.{call_premium,put_premium,bullish_premium-bearish_premium}` | whole-tape |
| `options-flow sweeps --side ask --min-premium 100000 --top-n 25` | ask total $701.2M ← `[.results[].total_premium]\|add` | top-25 |
| `options-flow sweeps --side bid …` | bid total $559.4M | top-25 |
| `options-flow unusual-volume --min-vol-oi-ratio 3 --top-n 25` | 1DTE 1220 put $20.9M ← `.results[]` | top-25 |
| `options-flow top-premium-trades --top-n 25` | Oct-1300 call $13.5M ask; Mar-27 1200 put $10.3M ask ← `.results[].{premium,side}` | top-25 |
| `options-flow iv-outliers --top-n 15` | deep-ITM artifacts only | top-15 |
| `options-flow greek-screener --top-n 15 --sort-by premium` | delta/vega on dated prints | top-15 |
| `hot-chains smart-money-flow --direction bullish/bearish --min-volume 500` | **MU absent from top-10 both directions** | top-10 |
| `hot-chains sweep-persistence --days 5 --symbol MU` | 5/5 sessions, consistency 1.0, **dominant_direction MIXED**, $10.3B 5d sweep prem ← `.results[0]` | 5d |
| `hot-chains sweep-ratio --top-n 15 --min-sweep-ratio 0.3` | MU outside top-15 | top-15 |

## Tool errors

- `hot-chains sweep-persistence`: first call with `--date 2026-06-25` failed —
  `Error: unknown flag: --date`. Re-run without `--date` (trailing tool anchors to
  latest available date = 2026-06-25); succeeded. No data fabricated.

## DATA NOTE / CORRECTION

None — all values round-tripped through `jq` on validated JSON. `smart-money-flow`
keys rows by `option_symbol`, not `ticker`; MU confirmed absent from both top-10
lists (no extreme ask/bid imbalance), recorded as a real null, not an error.

## Verdict for downstream phases

- **Bias from this phase:** **bullish** (net_flow +$279M, calls 2.79× by premium,
  #1 single name universe-wide) — but **moderated** by mixed sweeps, two-way top
  prints, and material ATM/1DTE put buying.
- **Conviction:** **3 / 5** (strong dollar tilt to calls, but no clean one-sidedness;
  `dominant_direction MIXED`, smart-money imbalance absent, hedging puts present).
- **Three things later phases should remember:**
  1. Dollars are decisively in calls (2.79×, +$279M net) but **contract-count P/C is
     balanced (1.026)** — directional conviction is institutional & premium-weighted,
     not broad.
  2. There is **real two-way positioning**: a $10.3M ask-side Mar-2027 ATM put and a
     $20.9M 1DTE 1220 put against the call buying — phase-2 (dark pool) and phase-3
     (OI walls) must confirm whether the put side is hedging or a genuine short.
  3. A large slice of premium is **1DTE/0DTE gamma churn** (sweeps + 1220 put) —
     discount it; the durable positioning is the Oct-1300 call, 2028 700 LEAP, and
     Mar-2027 1200 put.
- **Open questions:** Is the dark pool absorbing/confirming the bullish premium
  (phase 2)? Where are the OI walls vs the 1100–1300 strike cluster, and is the
  Mar-2027 put a hedge against a visible long (phase 3)? Does IV deflation cap the
  value of long-vega call structures (phase 4)?
