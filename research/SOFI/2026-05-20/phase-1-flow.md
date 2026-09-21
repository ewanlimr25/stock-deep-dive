# Phase 1 — Options Flow

**Ticker:** SOFI
**As-of date (requested):** 2026-05-20
**Effective data date:** 2026-05-19
**Generated:** 2026-05-20T00:00:00Z
**Upstream phases cited:** phase-0-intake.md

## Summary

SOFI tape on 2026-05-19 shows **persistent, two-way institutional flow with a
mixed-but-net-bullish-long-dated tilt**. The single largest premium trade is an
$816k mid-side block on the **Jan-2027 15C** (delta 0.62, 2,366 contracts) —
institutional ATM call accumulation. Bullish flow extends into **Jun-2028 13/15C
LEAPs** and **Jan-2028 15/18C LEAPs**, all bought on a mix of ask/mid/bid.
Counter-signal: a $669k ask-side block of **Jun-2028 15P** (1,404 contracts at
$4.78) — either a 2y bearish hedge or outright bearish LEAP. Near-dated tape
(May-22 expiry, 3 trading days out) is dominated by aggressive ATM 15C/15.5C
churn — both ask-side AND bid-side prints, suggesting active **dealer-vs-retail
gamma battle** at spot ($15.27) into May opex. Sweep persistence over the last
5 sessions classifies SOFI as a **persistent, $67M-premium sweep target with
mixed dominant direction** — this is a name institutions are repeatedly
positioning in.

## Key signals

- **Largest single print: Jan-2027 15C, $816,270 mid-side, 2,366 size, delta
  0.62, IV 68.2%** — institutional ATM call accumulation. [FLOW:top_premium_trades]
- **Bullish LEAP campaign: Jan-2027/Jan-2028/Jun-2028 15/18/20/13C aggregate
  >$3.5M in ask/mid sweep premium** [FLOW:sweeps], including $873k Jan-2027 15C
  mid sweep (41 trades) and $580k May-2022 15C ask sweep (13,326 size).
- **Counter-signal: Jun-2028 15P ask-side, $669k, 1,404 size, IV 53%** —
  long-dated put buying that does NOT square with the long-dated call accumulation.
  [FLOW:sweeps]
- **Single $516k Jul-2026 16P block (3,000 size, no_side)** — likely an
  opening cash-secured put SOLD (price = $1.72, delta -0.54). If sold, that is
  bullish income/bottom-fishing intent. [FLOW:top_premium_trades]
- **Sweep persistence (5/5 sessions in top, $66.99M total sweep premium, mixed
  direction)** — SOFI is one of the most consistently swept tickers in the tape.
  [FLOW:sweep_persistence]
- **Speculative 0DTE lottery flow** at $1/2/3/4/5 strikes May-22 expiry, IV
  9–18× normal — discount as retail/gamma-scalping noise, not directional
  signal. [FLOW:iv_outliers]
- **No SOFI appearance in market-wide top-30 bullish or bearish smart_money_flow**
  — meaning the absolute size of SOFI flow is below SPY/IWM/VIX/POET, but the
  *ratio* signals on persistence and vol/OI remain strong.
  [FLOW:smart_money_flow]

## Detailed findings

### Sweeps (ask vs bid, premium, persistence)

Sweep tape on 2026-05-19, ranked by aggregate premium, filtered to top 25 with
≥$100k premium:

| Expiry | Strike | Type | Side | Premium | Size | Trades | Avg Px |
|---|---|---|---|---|---|---|---|
| 2027-01-15 | 15 | call | mid | $873,015 | 2,530 | 41 | $3.44 |
| 2028-06-16 | 15 | put | ask | $669,263 | 1,404 | 202 | $4.78 |
| 2026-05-22 | 15 | call | ask | $579,792 | 13,326 | 686 | $0.47 |
| 2027-01-15 | 20 | call | bid | $523,986 | 2,838 | 260 | $1.84 |
| 2026-07-17 | 16 | put | no_side | $516,000 | 3,000 | 1 | $1.72 |
| 2028-06-16 | 20 | call | bid | $447,832 | 944 | 167 | $4.75 |
| 2027-01-15 | 20 | call | ask | $386,838 | 2,092 | 142 | $1.85 |
| 2028-06-16 | 15 | call | bid | $357,322 | 574 | 122 | $6.24 |
| 2028-06-16 | 20 | call | mid | $354,335 | 746 | 35 | $4.75 |
| 2026-09-18 | 2 | call | bid | $351,614 | 266 | 146 | $13.22 |
| 2026-08-21 | 16 | call | ask | $343,329 | 2,008 | 145 | $1.69 |
| 2028-06-16 | 15 | call | ask | $319,766 | 506 | 63 | $6.27 |
| 2028-01-21 | 18 | call | ask | $282,237 | 605 | 52 | $4.68 |
| 2026-05-22 | 15.5 | call | bid | $278,242 | 10,888 | 1,124 | $0.25 |
| 2026-05-22 | 15 | call | bid | $261,548 | 5,481 | 610 | $0.47 |
| 2028-01-21 | 15 | call | ask | $251,960 | 449 | 74 | $5.63 |
| 2028-06-16 | 15 | put | bid | $249,247 | 523 | 94 | $4.74 |
| 2026-05-22 | 15.5 | call | ask | $239,229 | 9,519 | 971 | $0.26 |
| 2026-05-29 | 15 | put | ask | $233,753 | 5,591 | 359 | $0.45 |
| 2027-06-17 | 20 | call | ask | $219,841 | 764 | 59 | $2.89 |
| 2028-06-16 | 15 | put | mid | $216,565 | 453 | 41 | $4.76 |
| 2028-06-16 | 13 | call | bid | $206,598 | 293 | 53 | $6.98 |
| 2026-09-18 | 2 | call | mid | $201,180 | 152 | 76 | $13.24 |
| 2026-05-22 | 15 | put | bid | $195,177 | 7,091 | 995 | $0.28 |
| 2028-01-21 | 20 | call | bid | $190,670 | 467 | 105 | $4.09 |

**Net read:**
- Bullish ask/mid-side call sweep premium aggregate (LEAP & multi-month):
  $873k + $580k + $354k + $343k + $319k + $282k + $251k + $239k + $219k =
  **~$3.46M** spread across Jan-2027 15C, May-22 15C, Jun-2028 20C, Aug-21 16C,
  Jun-2028 15C, Jan-2028 18C, May-22 15.5C, Jun-2027 20C.
- Bid-side call sweep premium ("call selling") aggregate: $523k + $447k + $357k
  + $190k = **~$1.52M** in Jan-2027 20C, Jun-2028 20C, Jun-2028 15C, Jan-2028 20C.
  This is either covered-call writing against existing long stock OR profit-taking
  on rolled positions.
- Put sweep premium: $669k Jun-2028 15P ask (BEARISH or hedge), $249k Jun-2028
  15P bid (put-selling = bullish), $233k May-29 15P ask (BEARISH 10-day put buy),
  $216k Jun-2028 15P mid, $195k May-22 15P bid (put selling = bullish).
- **The "$2 Sep-2026 call" $351k bid + $201k mid prints at $13.22-$13.24 price**
  represent **deep ITM call selling** (delta ~0.99) — synthetic long stock
  unwind OR call-write selling. Functionally short-stock-equivalent.

### New positioning (unusual vol vs OI)

Contracts with new positions opening (vol/OI ≥ 3):

| Expiry | Strike | Type | OI | Volume | vol/OI | Premium | Avg IV |
|---|---|---|---|---|---|---|---|
| 2026-06-05 | 12.5 | C | 2 | 336 | 168× | $96,742 | 65% |
| 2026-06-05 | 9 | C | 2 | 220 | 110× | $140,105 | 143% |
| 2026-06-05 | 8 | C | 3 | 292 | 97× | $214,396 | 172% |
| 2026-05-22 | 15 | C | 2,041 | 19,655 | 9.6× | $884,021 | 70% |
| 2026-05-22 | 4 | C | 22 | 181 | 8.2× | $202,321 | 988% |
| 2026-05-29 | 9 | C | 20 | 158 | 7.9× | $99,857 | 172% |
| 2026-05-22 | 1 | C | 28 | 161 | 5.8× | $225,952 | 1668% |
| 2026-05-22 | 5 | C | 21 | 116 | 5.5× | $118,772 | 660% |
| 2026-06-18 | 15.5 | C | 439 | 2,285 | 5.2× | $199,763 | 58% |

The deep ITM (June-2026 8/9/12.5C) buys + the May-22 ATM 15C activity at 9.6×
vol/OI are the institutionally interesting new positions; the rest is 0DTE
lottery noise.

### Largest premium prints (single-trade snapshot)

Spot range during 2026-05-19: **$15.05 – $15.39** (intraday).

Top 10 single trades by premium:

| Time (UTC) | Expiry | Strike | Type | Side | Premium | Size | Δ | IV |
|---|---|---|---|---|---|---|---|---|
| 19:53 | 2027-01-15 | 15 | C | mid | $816,270 | 2,366 | 0.62 | 68% |
| 17:33 | 2026-07-17 | 16 | P | no_side | $516,000 | 3,000 | -0.54 | 54% |
| 14:05 | 2028-06-16 | 25 | P | mid | $119,000 | 100 | -0.60 | 53% |
| 19:37 | 2028-01-21 | 18 | C | ask | $115,320 | 248 | 0.61 | 71% |
| 17:10 | 2027-01-15 | 20 | C | ask | $113,400 | 600 | 0.42 | 67% |
| 14:08 | 2028-06-16 | 3 | C | bid | $111,360 | 87 | 0.97 | 105% |
| 16:30 | 2027-06-17 | 20 | C | ask | $105,616 | 368 | 0.49 | 70% |
| 19:48 | 2028-01-21 | 15 | C | ask | $84,750 | 150 | 0.69 | 73% |
| 19:43 | 2027-01-15 | 20 | C | bid | $84,600 | 450 | 0.41 | 67% |
| 13:48 | 2028-06-16 | 15 | C | bid | $82,399 | 131 | 0.71 | 73% |

**The 19:53 close-of-day Jan-2027 15C mid block** is the headline trade —
delta 0.62 means it has stock-equivalent exposure of ~1,467 shares per
contract block, so $816k buys ~1,466 deltas (~22,400 shares-equivalent). For
context, SOFI's late-day spot was ~$15.27; a 22.4k-share equivalent at ~$15
is ~$340k of cash-equivalent stock — but the $816k spent on calls buys the
**convexity** that a stock buyer doesn't get. This is institutional behavior.

### IV outliers + Greeks

May-22 expiry (3 DTE) shows IV blow-outs at $1/$2/$3/$4/$5 strikes (deep ITM
calls trading near intrinsic) with IVs 6.6× → 16.7×. This is mechanical
behavior of the IV model on deep ITM contracts whose price is near intrinsic
and tiny extrinsic is rounded — **disregard as IV signal**.

Greek-screener (sorted by premium): the same Jan-2027 15C mid block dominates
(delta 0.62, gamma 0.045, theta -$0.0067/day, vega $0.047). The Jul-2026 16P
block (-0.54 delta, gamma 0.121, theta -$0.011, vega $0.024) has high gamma
and low vega → **near-money, short-dated directional structure**, consistent
with either "sell puts to collect premium ahead of Jul expiry" or "buy puts
as 60-day directional bearish bet." The single-line, no_side execution
profile favors the SOLD interpretation (block trade, single counterparty,
bid/ask cross).

### Smart-money flow (market-wide context)

SOFI does NOT appear in the top-30 bullish OR bearish hot_chains_smart_money_flow
on 2026-05-19. The market-wide tape on this date is dominated by:
- **Bearish:** VIX upside-call SELLING (200k+ contracts), HYG put buying,
  IWM/SPY downside put buying ($35M+ premiums each).
- **Bullish:** IEF put-selling, WULF/POET upside calls, SPX deep-OTM call buying.

Implication for SOFI: macro-tape positioning is broadly **defensive equity
hedging + rate-curve flattening (Treasury ETF put-selling/call-buying)**, not
risk-on euphoria. SOFI long-dated call accumulation is happening *against* a
broadly defensive macro tape — that strengthens the signal that the accumulation
is conviction-driven rather than beta-chasing.

### Sweep ratio (cross-ticker context)

No SOFI contracts appear in the top-30 sweep_ratio table on 2026-05-19; SOFI
sweeps are spread across many strikes/expiries rather than concentrated in a
single contract with extreme sweep_volume/volume ratio. Consistent with the
"persistent two-way" pattern from sweep_persistence.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|---|---|---|
| `options_flow_sweeps` | symbol=SOFI, min-premium=100000, top-n=25, date=2026-05-19 | 25 rows, mix of long-dated calls + counter-signal LEAP puts |
| `options_flow_unusual_volume` | symbol=SOFI, min-vol-oi-ratio=3, top-n=25, date=2026-05-19 | 9 rows; institutional new positions in Jun-2026 8/9/12.5C + May-22 15C |
| `options_flow_top_premium_trades` | symbol=SOFI, top-n=25, date=2026-05-19 | $816k Jan-2027 15C mid is largest; $516k Jul-2026 16P block second |
| `options_flow_iv_outliers` | symbol=SOFI, top-n=15, date=2026-05-19 | All outliers are mechanical (deep ITM May-22 calls); no signal |
| `options_flow_greek_screener` | symbol=SOFI, top-n=15, sort-by=premium, date=2026-05-19 | Confirms 0.62-delta Jan-27 15C is dominant by premium; Jul-26 16P high-gamma |
| `hot_chains_smart_money_flow` | direction=bullish, top-n=30, min-volume=500, date=2026-05-19 | SOFI absent from top-30 bullish |
| `hot_chains_smart_money_flow` | direction=bearish, top-n=30, min-volume=500, date=2026-05-19 | SOFI absent from top-30 bearish |
| `hot_chains_sweep_persistence` | symbol=SOFI, days=5, top-n=20 | SOFI in top sweeps **5/5 sessions**, mixed direction, $66.99M total |
| `hot_chains_sweep_ratio` | top-n=30, min-volume=500, min-sweep-ratio=0.3, date=2026-05-19 | SOFI absent from top-30 sweep-ratio table |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** mixed, leaning bullish-multi-month.
- **Conviction:** **3 / 5** — premium magnitude is real (>$3.5M ask/mid-side
  bullish call premium, 5/5 session sweep persistence), but ≥$900k of
  same-day put-side flow (Jun-2028 15P ask + May-29 15P ask + Jul-2026 16P
  uncertain-side) prevents conviction from going higher without dark pool /
  OI confirmation.
- **Three things later phases must remember:**
  1. **Spot reference: $15.27** (closing area on 2026-05-19). All strike
     analysis downstream should anchor here.
  2. **Key strike: $15** — Jan-2027 / Jan-2028 / Jun-2028 15C all bought; also
     Jun-2028 15P bought; May-22 15C/15.5C are the active near-term battleground.
     The $15 level is where dealer gamma and institutional positioning converge.
  3. **Counter-signal flagged: Jun-2028 15P ask-side $669k** is the largest
     non-bullish print. Phase 3 (OI) and phase 4 (dealer GEX) must clarify
     whether this is a hedge against a long stock position or a standalone
     bearish LEAP.
- **Open questions:**
  - Is dark pool accumulating SOFI at $15 to support the long-dated 15C bets?
    (phase 2 must answer)
  - What does OI at $15 / $16 / $18 / $20 look like vs. trading volume — is
    this new positioning or rolls? (phase 3)
  - Where is gamma flip / vanna concentration relative to $15.27? (phase 4)
  - Is the Jul-2026 16P "$516k single block" a sold put (bullish) or bought
    put (bearish)? Cross-reference dark pool size on 2026-05-19 17:33 UTC.
