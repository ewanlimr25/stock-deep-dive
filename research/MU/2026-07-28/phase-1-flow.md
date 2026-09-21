# Phase 1 — Options Flow

**Ticker:** MU
**As-of date:** 2026-07-28
**Generated:** 2026-07-28T21:22:00-04:00
**Upstream phases cited:** `phase-0-intake.md`, `phase-0.5-context.md`

## Summary

The MU options tape is **near-perfectly balanced and directionally inert**: $3.025B of premium
resolves to a net of **+$28.6M — a 1.0% tilt on $2.83B of two-way flow** — and the net customer
**delta** exposure across the entire tape is **-$178M (-$41M ex-0DTE) against a $926.7B market
cap**, i.e. statistically zero. Critically, the headline "+$1.43B bullish premium" is an
artifact of UW's definition: it is **ask-side calls ($645.2M) + bid-side puts ($784.2M)**, and
**puts sold is the larger half**. Read on the aggressor axis instead, MU customers were **net
SELLERS of $120M of premium** — calls net sold -$45.8M, puts net sold -$74.3M. The marginal
options participant on an -8.85% day was a **premium harvester, not a dip-buyer**. The one
genuinely coherent institutional footprint is a **~$28.4M systematic sale of the 750–800 put
strip across six tenors (Sep-26 → Jun-27) in the final 16 minutes**, paired with short-dated
ATM call buying — a "willing to own it 8–20% lower, want near-term convexity" posture — but
low volume/OI ratios (0.05–0.51) leave it **genuinely ambiguous whether that is opening short
puts (bullish) or monetizing protective puts after a -32% drawdown (neutral de-risking)**.
Phase 3 must resolve it. Per `phase-0.5-context.md` (`unusual_verdict = BUSY_NAME_NORMAL_DAY`,
option volume **0.84×** its own 30-day average), this phase's conviction is **capped at `+`**.

## Key signals

- **Net flow is noise.** `bullish_premium` $1,429,357,672 vs `bearish_premium` $1,400,800,551
  → derived `net_flow = +$28,557,121`, **+1.0% of gross**. [FLOW:insights_deep_dive]
- **Calls were net SOLD.** Ask-side calls $645.19M vs bid-side calls $690.95M = **-$45.76M**.
  There was no call-buying panic on the dip. [FLOW:aggressor_split DUCKDB]
- **Puts were net SOLD, and by more.** Ask-side puts $709.85M vs bid-side puts $784.17M =
  **-$74.32M**. Total net premium **sold: -$120.1M**. [FLOW:aggressor_split DUCKDB]
- **Net customer delta ≈ 0.** -$178M all-tape, **-$41M ex-0DTE**, on a $926.7B cap
  (0.004% of cap). The options market expressed **no directional view** on MU today.
  [FLOW:delta_notional DUCKDB]
- **Closing put-strip sale:** ~$28.4M of 750/800-strike puts hit the bid across Sep-26,
  Oct-26, Nov-26, Dec-26, Feb-27 and Jun-27 between **15:44–15:50 ET**, driving **+$130M of
  positive net customer delta in the last 16 minutes**. [FLOW:top_premium_trades]
- **Sweep persistence is activity, not direction:** MU in the top sweep cohort **5 of 5
  sessions**, `consistency_score = 1`, `total_sweep_premium = $4.333B` — but
  **`dominant_direction = "mixed"`**. [FLOW:sweep_persistence]
- **No smart-money flow detected for MU** on this date — zero MU rows in either the bullish or
  bearish `smart-money-flow` top-10. [FLOW:smart_money_flow]

## Detailed findings

### Whole-tape aggregate (read the top-N against THIS)

From `uw insights deep-dive --symbol MU` `.uw_screener`:

| Field | Value |
|---|---:|
| `call_premium` | $1,424,250,544 |
| `put_premium` | **$1,601,190,867** |
| `bullish_premium` | $1,429,357,672 |
| `bearish_premium` | $1,400,800,551 |
| **derived `net_flow`** (bull − bear) | **+$28,557,121** |
| `call_volume` | 394,507 |
| `put_volume` | 342,077 |
| `put_call_ratio` | 0.8671 |
| `total_open_interest` | 3,326,277 |
| `iv30d` / `volatility` | 0.9604 / 1.2857 |
| `iv_rank` | 83.4835 |
| `implied_move` / `implied_move_perc` | 64.79 pts / **7.90%** |
| `next_earnings_date` | 2026-09-22 |

Two things immediately conflict with a naive bullish read:
1. **Put premium ($1.601B) exceeds call premium ($1.424B) by $177M**, even though `put_volume`
   (342,077) is *below* `call_volume` (394,507) and P/C = 0.867. Puts are carrying more dollars
   per contract — a downside-skew/higher-strike-value tape.
2. `net_flow` is **+1.0% of gross**. On a name whose daily implied move is 7.90%, a 1% premium
   tilt is not a signal.

**Reverse-engineering UW's definition (audit-grade).** The DuckDB aggressor split reconciles to
UW's aggregate **to the dollar**, which pins the definition:

```
bullish_premium = ask-side CALLS + bid-side PUTS  =  645.19 + 784.17  = $1,429.36M  ✓ (UW: 1,429,357,672)
bearish_premium = ask-side PUTS  + bid-side CALLS =  709.85 + 690.95  = $1,400.80M  ✓ (UW: 1,400,800,551)
```

**This matters enormously here.** 54.9% of MU's "bullish premium" is *puts being sold*, not
calls being bought. A reader who takes "+$1.43B bullish" at face value would conclude
institutions were buying the dip. They were not — they were **selling premium into it**.

**Full-tape aggressor split** (`canceled=false`, all expiries) — the authoritative directional read:

| type | side | trades | contracts | premium | delta-notional |
|---|---|---:|---:|---:|---:|
| call | ask *(bought)* | 53,281 | 170,280 | **$645.19M** | +$3.963B |
| call | bid *(sold)* | 63,447 | 193,977 | **$690.95M** | +$4.233B |
| call | mid | 10,862 | 30,244 | $88.11M | +$0.507B |
| put | ask *(bought)* | 48,224 | 148,765 | **$709.85M** | -$3.370B |
| put | bid *(sold)* | 49,814 | 167,982 | **$784.17M** | -$3.462B |
| put | mid | 8,687 | 25,330 | $107.17M | -$0.405B |

- **Calls: net -$45.76M sold** (and 23,697 more contracts sold than bought).
- **Puts: net -$74.32M sold** (19,217 more contracts sold than bought).
- **Customers net sold $120.08M of option premium.**
- **Net customer delta** = (ask-side Δ) − (bid-side Δ) = (+0.593B) − (+0.771B) = **-$178M**.
  Ex-0DTE: (+0.272B) − (+0.313B) = **-$41M**. Against a $926.7B cap this is **zero**.
  [FLOW:delta_notional DUCKDB]

### Tenor structure — where the selling actually is

Premium by DTE bucket (ask = bought by customer, bid = sold):

| DTE bucket | type | bought | sold | **net** |
|---|---|---:|---:|---:|
| 0–1DTE | call | $83.9M | $91.0M | -$7.1M |
| 0–1DTE | put | $82.2M | $79.2M | +$3.0M |
| 2–7DTE | call | $70.5M | $66.5M | +$4.0M |
| 2–7DTE | put | $103.2M | $118.7M | -$15.5M |
| 8–45DTE | call | $82.1M | $85.5M | -$3.4M |
| 8–45DTE | put | $150.9M | $140.1M | **+$10.9M** |
| **46–180DTE** | **call** | $156.5M | $208.4M | **-$51.9M** |
| 46–180DTE | put | $159.3M | $163.9M | -$4.7M |
| **LEAP (>180DTE)** | call | $252.2M | $239.6M | +$12.6M |
| **LEAP (>180DTE)** | **put** | $214.2M | $282.2M | **-$68.1M** |

- **0–1DTE is only $336.3M — ~12% of two-sided premium.** Unlike most event-day tapes, 0DTE is
  *not* inflating this read. The signal (such as it is) lives in real tenor.
- **The two dominant imbalances are both SALES:** LEAP puts **-$68.1M** and 46–180DTE calls
  **-$51.9M**. Selling long-dated downside *and* medium-dated upside = **short-vol / range-bound
  income posture**, not a directional bet.
- The only net *buying* of size is **8–45DTE puts, +$10.9M** — modest near-term protection.

**Moneyness of the LEAP put selling** (spot 820.53):

| moneyness | trades | contracts | bought | sold | net |
|---|---:|---:|---:|---:|---:|
| <60% (deep OTM) | 1,816 | 4,555 | $8.5M | $5.0M | +$3.5M |
| 60–90% OTM | 791 | 3,579 | $15.7M | $30.7M | **-$15.0M** |
| **ATM ±10%** | 582 | 4,514 | $26.7M | $68.9M | **-$42.2M** |
| 110–160% ITM | 532 | 1,892 | $32.7M | $45.0M | -$12.3M |
| >160% deep ITM | 766 | 2,507 | $130.6M | $132.7M | -$2.1M |

- The core is **ATM LEAP puts sold, -$42.2M**, plus **-$15.0M** of 60–90% OTM. Someone is
  selling long-dated downside on MU around and below spot.
- **The >160% deep-ITM bucket ($130.6M bought / $132.7M sold) is balanced to ~1.6%** — these are
  the 1700/1750/1800/2000/2390/2480/2500-strike Dec-2028 puts seen in the sweep and top-premium
  lists. **Balanced two-way = structural/financing (box- or combo-style), NOT directional.**
  They inflate every premium-ranked view of MU today and must be excluded from any directional
  read. *(At 2.4y tenor and ~100% IV these strikes carry deltas of only ~-0.42, so they are far
  less "deep" in probability terms than in strike terms.)*

**Moneyness of the 46–180DTE call selling:**

| moneyness | trades | contracts | bought | sold | net |
|---|---:|---:|---:|---:|---:|
| ITM | 1,932 | 7,242 | $66.4M | $91.5M | **-$25.1M** |
| 0–20% OTM | 2,652 | 7,743 | $33.1M | $48.7M | **-$15.6M** |
| 20–50% OTM | 4,182 | 14,708 | $43.9M | $54.3M | -$10.4M |
| >50% OTM | 4,165 | 12,913 | $13.1M | $13.9M | -$0.8M |

Selling is **monotonic in moneyness** — heaviest where the premium is (ITM/near-money). That is
the signature of **systematic overwriting against stock**, not of directional bearish bets.

### Sweeps (ask vs bid)

`uw options-flow sweeps --min-premium 100000 --top-n 25` per side (top-25 each, so these are
tips of the iceberg — read against the aggregate above):

| side | calls | puts |
|---|---:|---:|
| **ask** (aggressive buys) | n=12, **$103.71M** | n=13, **$139.63M** |
| **bid** (aggressive sells) | n=9, **$85.29M** | n=16, **$192.47M** |

- Largest ask-side sweeps: **800P Aug-21 $15.98M**, 1700P Sep-18 $15.12M, 800P Jul-31 $13.99M,
  800P Jul-29 $13.36M, 1800P Dec-2028 $12.95M, 820C Jul-29 $11.80M.
- Largest bid-side sweeps: **2500P Dec-2028 $19.95M**, 2000P Dec-2028 $17.68M, 2480P Dec-2028
  $15.95M, 780P Jun-27 $15.16M, 800P Jul-31 $14.88M, 820C Jul-29 $13.84M.
- **Both sweep lists are dominated by the same deep-ITM Dec-2028 put complex** and by the 800
  strike traded on *both* sides across Jul-29/Jul-31/Aug-21. This is two-way market-making
  around a level, not a one-sided campaign.

### New positioning (unusual volume, vol/OI)

`uw options-flow unusual-volume --min-vol-oi-ratio 3 --top-n 25`:

| type | strike | expiry | premium | volume | OI | vol/OI | avg IV |
|---|---:|---|---:|---:|---:|---:|---:|
| call | 820 | 2026-07-29 | $26.59M | 11,401 | 12 | **950.08** | 1.436 |
| call | 825 | 2026-07-29 | $21.21M | 9,533 | 13 | 733.31 | 1.411 |
| call | 830 | 2026-07-29 | $15.78M | 8,297 | 46 | 180.37 | 1.406 |
| call | 815 | 2026-07-29 | $14.06M | 5,649 | 18 | 313.83 | 1.463 |
| call | 835 | 2026-07-29 | $4.12M | 2,288 | 8 | 286.00 | 1.415 |
| call | 790 | 2026-07-29 | $3.12M | 887 | 3 | 295.67 | 1.554 |
| call | 785 | 2026-08-05 | $1.94M | 294 | 1 | 294.00 | 1.100 |
| put | 1080 | 2027-02-19 | $4.37M | 115 | 1 | 115.00 | 0.872 |
| call | 2180 | 2027-03-19 | $1.81M | 567 | 5 | 113.40 | 0.870 |
| call | 2370 | 2026-07-31 | **$1,089** | 497 | 2 | 248.50 | 3.579 |

- **The entire top of the vol/OI list is the 1DTE ATM call ladder (785–835 strikes, Jul-29)** at
  **IV 140–155%**. Nine-hundred-times-OI on a 1-day option is **event-day gamma trading around
  the close**, not position-building. Tag and discount per the 0DTE pitfall.
- Note the 820C/Jul-29 chain nets out: it appears in the ask sweeps at $11.80M **and** the bid
  sweeps at $13.84M — traded aggressively **both ways**.
- The 2370C/2380C Jul-31 rows at **$1,089 / $689 total premium** and **IV 358%/357%** are
  worthless-lottery noise; ignore.
- From `insights_deep_dive.uw_top_oi_changes`: **55P Aug-07 +24,412 OI at $0.01**, 500P Jul-31
  +11,767 at $0.27, 95P Jul-31 +4,352 at $0.01. These are **penny crash-tail lotteries** — 24k
  contracts of the 55 put cost roughly $24k total. Real, but economically trivial; note as tail
  hedging appetite, not as a directional signal.

### Largest premium prints

`uw options-flow top-premium-trades --top-n 25` (fields are `premium`/`size`/`side`, **not**
`total_premium`/`total_size` — see DATA NOTE):

| time (ET) | type | strike | expiry | premium | size | price | side | IV | Δ |
|---|---|---:|---|---:|---:|---:|---|---:|---:|
| 12:56:24 | put | 820 | 2027-03-19 | **$10.20M** | 500 | 204.00 | **bid** | 0.86 | -0.347 |
| 15:46:49 | put | 800 | 2026-10-16 | $7.70M | 630 | 122.25 | **bid** | 0.91 | -0.385 |
| 10:40:00 | call | 1000 | 2027-01-15 | $6.45M | 480 | 134.36 | **bid** | 0.87 | +0.490 |
| 15:46:28 | put | 800 | 2026-09-18 | $5.32M | 540 | 98.50 | **bid** | 0.91 | -0.397 |
| 10:40:00 | call | 1100 | 2027-01-15 | $5.26M | 480 | 109.56 | **bid** | 0.87 | +0.425 |
| 15:48:19 | put | 750 | 2027-06-17 | $5.16M | 270 | 191.00 | **bid** | 0.84 | -0.288 |
| 11:13:16 | call | 500 | 2028-12-15 | $5.15M | 100 | 515.42 | ask | 0.85 | +0.865 |
| 11:13:16 | call | 600 | 2028-12-15 | $4.77M | 100 | 476.58 | bid | 0.84 | +0.832 |
| 11:03:35 | put | 830 | 2026-07-31 | $4.28M | 951 | 45.00 | **bid** | 1.28 | -0.532 |
| 11:43:50 | call | 1100 | 2027-09-17 | $4.17M | 187 | 222.95 | mid | 0.84 | +0.572 |
| 12:02:30 | put | 2500 | 2028-12-15 | $4.15M | 24 | 1729.72 | bid | 1.05 | -0.424 |
| 10:24:42 | put | 900 | 2026-10-16 | $4.13M | 210 | 196.45 | **bid** | 0.92 | -0.518 |
| 15:47:38 | put | 750 | 2027-02-19 | $4.10M | 270 | 152.00 | **bid** | 0.85 | -0.309 |
| 11:13:16 | call | 2400 | 2028-12-15 | $3.74M | 200 | 186.78 | bid | 0.82 | +0.442 |
| 15:49:40 | put | 830 | 2026-07-31 | $3.67M | 1,000 | 36.70 | **bid** | 1.23 | -0.477 |
| 11:13:16 | call | 1200 | 2028-12-15 | $3.30M | 100 | 329.72 | ask | 0.83 | +0.663 |
| 15:47:12 | put | 800 | 2026-11-20 | $3.20M | 225 | 142.30 | **bid** | 0.88 | -0.371 |
| 14:47:12 | put | 800 | 2026-07-31 | $3.01M | 913 | 33.00 | ask | 1.32 | -0.429 |

**Side × type totals across the top-25: `bid_put` n=15 $67.04M · `bid_call` n=4 $20.21M ·
`ask_put` n=3 $8.73M · `ask_call` n=2 $8.45M · `mid_call` n=1 $4.17M.** The largest prints of
the day were overwhelmingly **puts hitting the bid** — $67.0M sold vs $8.7M bought, a **7.7:1
sell/buy ratio** in the top-25.

**The 15:44–15:50 ET closing cluster** (chains >$1.5M in that window):

| type | strike | expiry | side | contracts | premium | Δ |
|---|---:|---|---|---:|---:|---:|
| put | 800 | 2026-10-16 | bid | 631 | $7.71M | -0.384 |
| put | 800 | 2026-09-18 | bid | 541 | $5.33M | -0.395 |
| put | 750 | 2027-06-17 | bid | 270 | $5.16M | -0.288 |
| **call** | **830** | **2026-07-31** | **ask** | 1,273 | **$4.32M** | +0.487 |
| put | 750 | 2027-02-19 | bid | 270 | $4.10M | -0.309 |
| put | 800 | 2026-11-20 | bid | 225 | $3.20M | -0.371 |
| put | 750 | 2026-12-18 | bid | 225 | $2.88M | -0.319 |
| **call** | **950** | **2028-12-15** | **ask** | 75 | **$2.88M** | +0.728 |

**≈$28.4M of 750/800 puts sold across six consecutive expiries (Sep-26 → Jun-27) inside six
minutes, alongside ATM/ITM call buying.** The minute-by-minute net customer delta confirms the
impact: **+$57.2M (15:44), +$37.9M (15:46), +$22.5M (15:47), +$6.4M (15:48), +$8.8M (15:49)** —
roughly **+$130M of positive delta added into the closing bell of an -8.85% session**, against a
full-day net of only -$178M. **Someone leaned long into the close.**

**But is it opening or closing?** Volume against start-of-day OI on that strip:

| strike | expiry | SOD OI | day contracts | vol/OI | sold | bought |
|---:|---|---:|---:|---:|---:|---:|
| 800 | 2026-09-18 | 4,687 | 1,192 | 0.25 | $7.70M | $3.84M |
| 800 | 2026-10-16 | 2,371 | 1,198 | 0.51 | $9.63M | $4.59M |
| 750 | 2026-09-18 | 3,439 | 425 | 0.12 | $1.50M | $1.44M |
| 800 | 2026-11-20 | 1,567 | 348 | 0.22 | $3.88M | $1.06M |
| 750 | 2026-12-18 | 1,433 | 290 | 0.20 | $3.54M | $0.15M |
| 750 | 2027-02-19 | 391 | 286 | 0.73 | $4.15M | $0.20M |
| 750 | 2027-06-17 | 1,452 | 482 | 0.33 | $7.01M | $1.97M |
| 800 | 2027-06-17 | 2,460 | 161 | 0.07 | $3.13M | $0.46M |
| 800 | 2027-02-19 | 45 | 163 | **3.62** | $0.91M | $2.11M |

**Every strike except 800P/Feb-27 traded well below its existing OI (0.07–0.73×).** There is
ample pre-existing open interest to close against, so the tape **cannot distinguish**:
- **(A) opening short puts** — a bullish "I'll own MU at 750–800" income trade, or
- **(B) closing long protective puts** — monetizing hedges after a -32% drawdown, which is
  *de-risking*, directionally neutral, and would actually mean a large holder just **removed its
  downside protection**.

These readings have opposite implications for phase 9. **→ Phase 3 (`uw oi`) must check whether
OI at 750/800 across Sep-26→Jun-27 rose or fell.**

### IV outliers + Greeks

`uw options-flow iv-outliers --top-n 15` returns **only worthless deep-OTM puts**:

| type | strike | expiry | avg IV | premium | volume |
|---|---:|---|---:|---:|---:|
| put | 105 | 2026-07-31 | **7.337** (734%) | $136 | 102 |
| put | 140 | 2026-07-31 | 6.384 | $757 | 108 |
| put | 160 | 2026-07-31 | 6.008 | $557 | 93 |
| put | 150 | 2026-07-31 | 5.828 | $141 | 64 |
| put | 170 | 2026-07-31 | 5.721 | $743 | 151 |
| put | 60 | 2026-08-07 | 5.385 | $475 | 61 |
| put | 5 | 2026-10-16 | 4.204 | $570 | 82 |

Premiums of **$136–$757** — these are pricing artifacts on unquotable strikes, **not signal**.
The genuine IV information is elsewhere: **front-week ATM IV is 140–155%** (the Jul-29 ladder)
versus **`iv30d` = 96.0%** and **LEAP IV ≈ 82–86%** — a steeply backwardated term structure
pricing near-term event risk and long-run mean reversion. Per `phase-0.5-context.md`, IV rank
83.48 is the **43rd percentile of MU's own history** — vol did *not* spike on this -8.85% day.

`greek-screener --sort-by premium --top-n 15` returns the same prints as top-premium (fields
`delta`/`gamma`/`premium` singular). Deltas on the largest prints cluster **-0.29 to -0.53 on
puts** and **+0.42 to +0.87 on calls** — i.e. the size is being done in **meaningful-delta,
near-the-money contracts**, not lottery tickets. The Dec-2028 complex prints at Δ +0.865 (500C),
+0.832 (600C), +0.663 (1200C), +0.442 (2400C), -0.424 (2500P) — consistent with a multi-leg
structure executed at a single timestamp (11:13:16), reinforcing the "financing/structural, not
directional" read.

### Persistence, smart money, sweep ratio

- **`sweep-persistence --days 5 --symbol MU`**: `sessions_in_top = 5` of 5 (dates covered
  2026-07-22…07-28), `consistency_score = 1`, `total_sweep_premium = $4,333,000,908`,
  **`dominant_direction = "mixed"`**. MU sweeps *every* session — maximal persistence of
  **activity** with **zero persistence of direction**. Per the phase heuristic, the bullish
  signature requires sweeps persisting ≥2 sessions **in one direction**; that condition **fails**.
- **`smart-money-flow` (bullish and bearish, top-10, min-volume 500)**: **no MU rows in either
  direction.** Recorded as "no smart-money flow detected on this date"; per composition
  guidance, not re-run with looser thresholds. *(Sector aside: `DRAM260821C00060000` appears in
  the bullish list — ask 36,880 vs bid 17,908, ratio 2.06, $8.09M — so there was net bullish
  call buying on a DRAM-complex ETF even though MU itself showed none. One chain; noted, not
  weighted.)*
- **`sweep-ratio --min-sweep-ratio 0.3 --top-n 15`**: exactly one MU chain —
  **`MU260918C00740000`, sweep_ratio 0.9116, premium $8.39M, volume 543**. **This is a trap:**
  the parquet side-split shows **498 contracts SOLD on the bid ($7.70M) vs 39 bought on the ask
  ($0.60M)** — 92.8% of the premium was **sell**-side. An ITM Sep call being aggressively
  *written*, i.e. overwriting. A high sweep ratio measures **aggression, not direction**.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|------------------|--------------------------|-----------|
| `uw insights deep-dive --symbol MU --date 2026-07-28 --json` | bullish=1,429,357,672; bearish=1,400,800,551; **derived net_flow=+28,557,121**; call_prem=1,424,250,544; put_prem=1,601,190,867; call_vol=394,507; put_vol=342,077; pcr=0.8671; iv_rank=83.4835; implied_move_perc=0.07904 ← `.uw_screener.*` | whole-tape |
| ″ | top OI changes: 55P +24,412 @0.01; 500P +11,767 @0.268 ← `.uw_top_oi_changes[]` | top-5 |
| `uw options-flow sweeps --symbol MU --side ask --min-premium 100000 --top-n 25 --date …` | call n=12 $103.71M; put n=13 $139.63M ← `group_by(.option_type)`, `.total_premium` | top-25 |
| `uw options-flow sweeps --symbol MU --side bid …` | call n=9 $85.29M; put n=16 $192.47M | top-25 |
| `uw options-flow unusual-volume --symbol MU --min-vol-oi-ratio 3 --top-n 25 …` | 820C 7/29 vol_oi=950.08 prem=26,588,476 oi=12 iv=1.436 ← `.results[]` | top-25 |
| `uw options-flow top-premium-trades --symbol MU --top-n 25 …` | bid_put n=15 $67.04M vs ask_put n=3 $8.73M ← `group_by(.side+"_"+.option_type)`, `.premium` | top-25 |
| `uw options-flow iv-outliers --symbol MU --top-n 15 …` | 105P 7/31 avg_iv=7.337 prem=$136 ← `.results[]` | top-15 |
| `uw options-flow greek-screener --symbol MU --top-n 15 --sort-by premium …` | Δ 500C Dec-28=+0.865; 2500P Dec-28=-0.424 ← `.results[].delta` | top-15 |
| `uw hot-chains smart-money-flow --direction bullish\|bearish --top-n 10 --min-volume 500 …` | **0 MU rows both directions** ← `[.results[]\|select(.option_symbol\|test("^MU"))]\|length` | top-10 ×2 |
| `uw hot-chains sweep-persistence --days 5 --top-n 20 --symbol MU --json` | sessions_in_top=5; consistency=1; **dominant_direction="mixed"**; sweep_prem=$4,333,000,908 ← `.results[0]` | 1 row |
| `uw hot-chains sweep-ratio --top-n 15 --min-volume 500 --min-sweep-ratio 0.3 …` | MU260918C00740000 ratio=0.9116 prem=$8,391,941 ← `.results[]` | top-15 |
| DuckDB §A aggressor + delta-notional (`bot-eod-report-2026-07-28.parquet`, 234,323 MU rows) | call ask/bid $645.19M/$690.95M; put ask/bid $709.85M/$784.17M; net cust Δ **-$178M** all / **-$41M** ex-0DTE | full tape |
| DuckDB §A DTE×type×side | LEAP put net **-$68.1M**; 46–180DTE call net **-$51.9M**; 0–1DTE = $336.3M (~12%) | full tape |
| DuckDB moneyness cuts | LEAP put ATM±10% net **-$42.2M**; >160% ITM balanced ($130.6M/$132.7M) | full tape |
| DuckDB closing-cluster + per-minute Δ | 15:44–15:50 ET ≈$28.4M puts sold across 6 tenors; +$130M cust Δ in last 16 min | full tape |
| DuckDB vol-vs-SOD-OI on 750/800 strip | vol/OI 0.07–0.73 (ex 800P Feb-27 3.62) → open-vs-close **ambiguous** | 11 chains |
| DuckDB side split `MU260918C00740000` | bid 498 ct/$7.70M vs ask 39 ct/$0.60M → **sold** | 1 chain |

## Tool errors

1. **`uw hot-chains sweep-persistence --days 5 --top-n 20 --symbol MU --date 2026-07-28 --json`**
   → exited 1, verbatim:
   ```
   Error: unknown flag: --date
   error: unknown flag: --date
   ```
   **Resolution:** `sweep-persistence` is a *trailing* tool and takes no `--date`; it anchors to
   the latest available date. Re-run **without** `--date`, and its returned
   `dates_covered = ["2026-07-28","2026-07-27","2026-07-24","2026-07-23","2026-07-22"]` confirms
   the window terminates exactly on our as-of date, so the read is point-in-time correct for
   this run. *(Would NOT be reproducible for a historical as-of date.)*
2. `uw insights deep-dive --symbol MU` again returned
   `"yahoo_fundamentals":{"error":"yahoo quoteSummary MU: HTTP 401"}` — carried over from
   phase-0.5, non-blocking, no phase-1 value depends on it.

## DATA NOTE / CORRECTION

Two field-path errors were made and corrected **before** any number was written here:

1. **`top-premium-trades` / `greek-screener` use singular `premium`, `size`, `delta`** — not
   `total_premium` / `total_size`. The first read with `.total_premium` returned `null` for
   every row. Re-read against `.premium` / `.size` / `.side`; all values in the "Largest premium
   prints" table trace to those paths. **No null was transcribed as a number.**
2. **`options-flow sweeps` has no `total_volume`, `open_interest` or `avg_iv`** — its schema is
   `avg_price, expiry, option_type, side, strike, total_premium, total_size, trade_count,
   underlying_symbol`. The first read requested `.total_volume` and got `null`; the sweeps
   section here quotes only `total_premium` (a field that exists). Volume/OI figures in this
   file come from `unusual-volume` and the parquet, never from `sweeps`.

Additionally, `hot-chains smart-money-flow` carries **no `underlying_symbol`/`ticker` field** —
the ticker is embedded in `option_symbol` (e.g. `SOFI260731C00018500`). The MU filter was
re-run as `select(.option_symbol|test("^MU"))`; the "0 MU rows" finding is from that corrected
path, not from the failed `.underlying_symbol` filter.

All DuckDB figures reconcile to the UW aggregate to the dollar (bullish/bearish premium
identity shown above), which is the strongest available cross-validation that the escape-hatch
numbers and the CLI numbers describe the same tape.

## Verdict for downstream phases

- **Bias from this phase:** **MIXED — leaning short-vol / range-bound, NOT directional.** The
  premium sign says "+bullish"; the aggressor axis says "customers sold $120M of premium and
  ended the day with ≈zero net delta." The honest read is **no directional signal**, with a
  modest, genuine tilt toward *selling volatility* in both wings.
- **Conviction: 2 / 5.** Capped at `+` by `phase-0.5`'s `BUSY_NAME_NORMAL_DAY` verdict
  (option volume 0.84× its own average). The bullish-flow *signature* from the rubric requires
  ask-side calls + smart-money ratio ≥0.6 + directionally persistent sweeps: MU fails **all
  three** (calls net sold; no smart-money rows at all; persistence `mixed`).
- **Three datapoints later phases must remember:**
  1. **`bullish_premium` = ask-calls + bid-puts, and bid-puts ($784.17M) is the larger half.**
     MU's "+$1.43B bullish" is **more put-selling than call-buying** — calls were net **sold**
     -$45.76M. Never cite MU's bullish premium as evidence of dip-buying in phases 7–9.
  2. **Net customer delta ≈ -$41M ex-0DTE on a $926.7B cap.** The options market took no side.
     Any downstream thesis claiming "options flow confirms X" must reconcile with this.
  3. **≈$28.4M of 750/800 puts sold across Sep-26→Jun-27 in the last 16 minutes** (+$130M
     customer delta into the bell), **plus -$51.9M of 46–180DTE calls sold (heaviest ITM)**.
     The 750–800 zone is where a large participant is transacting downside. Phases 3/4 should
     treat **750–800 as the structurally important shelf**, and phase 9 should note it is
     ~2.5–8.6% below spot.
- **Open questions:**
  - **THE decisive one — is the 750/800 put-strip sale OPENING or CLOSING?** Vol/OI of 0.07–0.73
    makes the tape agnostic. Opening = bullish (institution underwriting the dip at 750–800);
    closing = neutral-to-negative (a hedged holder just *removed* protection after -32%).
    **→ phase 3 (`uw oi`, OI change at 750/800 across Sep-26→Jun-27).**
  - Is the dark pool confirming any accumulation, or is it distributive? MU printed **$12.93B /
    15.79M shares (1.41% of the 1.12B float) at avg $817.22, below the $820.53 close** —
    **→ phase 2.**
  - **Why did IV rank *fall* to the 43rd self-percentile on an -8.85% day, and who is selling
    ATM LEAP puts at 82–86% IV?** Is dealer positioning long-gamma enough to damp realized
    vol? **→ phase 4 (GEX/DEX, max-pain).**
  - The 46–180DTE ITM call selling (-$25.1M) looks like overwriting against stock. Does phase-2
    dark-pool or phase-3 OI show the underlying long it would be written against?
