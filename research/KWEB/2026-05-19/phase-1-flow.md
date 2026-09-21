# Phase 1 — Options Flow

**Ticker:** KWEB
**As-of date:** 2026-05-19 (effective; user-requested 2026-05-20 unavailable)
**Generated:** 2026-05-20T00:00:00Z
**Upstream phases cited:** phase-0-intake.md

## Summary

KWEB tape is genuinely two-way today, but the multi-session backdrop is
unambiguously bearish: KWEB sat in the top-sweep cohort **5 of 5 sessions**
with a `dominant_direction` of **bearish** and aggregate sweep premium
**$94.9M** [FLOW:sweep_persistence]. Today's single largest prints are a
near-ATM **Dec '26 29-strike straddle (~$1.75M, equal-size puts + calls
struck @ ATM 29 timestamped 14:56:16Z)** — a long-volatility / event play,
not a directional bet [FLOW:top_premium_trades]. The mid-price tape skews
**bid-side on upside calls (Jul 30C $499K, Sep 35C $429K, Aug 35C $314K
all on bid)** consistent with overwriting or long-call dumping, even as a
**Jun '26 20-strike deep-ITM call sweep on the ASK ($631.5K, delta 0.95)**
adds synthetic long exposure [FLOW:sweeps].

## Key signals

- **5-day sweep persistence: dominant_direction = bearish, $94.9M total**
  [FLOW:sweep_persistence] — strongest single signal; weight it heavily.
- **Long-straddle print** Dec '26 29P $897K + Dec '26 29C $858K at the
  same second, equal 3,000 size, opposite deltas (-0.50 / +0.52)
  [FLOW:top_premium_trades] → directional-neutral, vol-long event play.
- **Jun '26 30.5C: vol 18,231 vs OI 56 → vol/OI 326×**, $656K premium
  [FLOW:unusual_volume] but executed `side=mid` ($583.7K) — opening, not
  aggressive; flagged but ambiguous.
- **Bid-side selling of upside calls** Jul 30C ($499K), Sep 35C ($429K),
  Aug 35C ($314K) [FLOW:sweeps] — overwriting / long-call liquidation.
- **Closing/sold Jan '27 27P on bid, $330K, delta -0.37** + bid-side Nov
  30P ($128K) [FLOW:top_premium_trades] — partial offset to the bearish
  persistence; *some* downside puts being sold-to-close.
- **Smart-money bearish list** contains `KWEB260529C00032000`
  (24,594 net bid-side, $74K premium) [FLOW:smart_money_flow:bearish] —
  small but it is the *only* KWEB contract in either smart-money list.

## Detailed findings

### Sweeps — aggressor side mix

Top KWEB sweeps by aggregated premium [FLOW:sweeps]:

| # | Expiry | Strike / Type | Side | Premium | Size | Read |
|---|--------|---------------|------|---------|------|------|
| 1 | 2026-12-18 | 29P | no_side | $897,000 | 3,000 | Long-straddle leg (paired with #2) |
| 2 | 2026-12-18 | 29C | no_side | $858,000 | 3,000 | Long-straddle leg (paired with #1) |
| 3 | 2026-06-18 | 20C | **ask** | $631,500 | 750 | Deep-ITM synthetic long, delta 0.95 |
| 4 | 2026-06-18 | 30.5C | mid | $583,704 | 16,214 | Opening, aggressor unclear |
| 5 | 2026-07-17 | 30C | **bid** | $499,664 | 5,397 | Call overwrite / long-call dump |
| 6 | 2026-09-18 | 35C | **bid** | $429,706 | 7,674 | Far-OTM call sale |
| 7 | 2026-05-29 | 29C | no_side | $409,500 | 11,700 | Near-ATM May-end, tied |
| 8 | 2027-01-15 | 27P | **bid** | $330,000 | 1,500 | Put liquidation (bullish unwind) |
| 9 | 2026-08-21 | 35C | **bid** | $314,771 | 8,735 | Far-OTM call sale |
| 10 | 2026-06-18 | 29C | **ask** | $276,541 | 3,580 | Front-month long-call buy |

Ask-side notional ≈ **$1.04M**; bid-side notional ≈ **$1.69M**; no-side
(tied / multi-leg) ≈ **$2.17M**. **Bid > ask**, but bid-side is dominated
by upside-call selling (Jul/Aug/Sep 30–35Cs) and put closes (Jan'27 27P)
— this is not a clean bear signature, it's an *overwriting / unwind*
signature on top of a bearish multi-day persistence base.

### New positioning — unusual volume [FLOW:unusual_volume]

Only four contracts cleared the 3× vol/OI floor; all in the front
2026-Jun expiry except the May 29C:

| Expiry | Strike | Type | Volume | OI | Vol/OI | Premium |
|--------|--------|------|--------|-----|--------|---------|
| 2026-06-18 | 30.5 | C | 18,231 | 56 | **326×** | $656,297 |
| 2026-06-18 | 27.5 | P | 161 | 8 | 20× | $9,118 |
| 2026-06-18 | 29.5 | C | 606 | 81 | 7× | $36,692 |
| 2026-05-29 | 29 | C | 16,016 | 3,985 | 4× | $571,575 |

The 30.5C surge is the day's headline new position. Aggressor on it is
`side=mid`, so this is more likely **complex / spread / institutional
two-sided print** than an outright directional buy.

### Largest single-trade prints [FLOW:top_premium_trades]

| Time (UTC) | Contract | Side | Delta | Premium | Notes |
|------------|----------|------|-------|---------|-------|
| 14:56:16 | Dec'26 29P | no_side | -0.496 | $897,000 | Straddle leg |
| 14:56:16 | Dec'26 29C | no_side | +0.522 | $858,000 | Straddle leg |
| 14:36:28 | Jun'26 20C | ask | +0.947 | $631,500 | Synthetic long (deep ITM) |
| 19:00:26 | Jun'26 30.5C | mid | +0.238 | $583,704 | Opening, ambiguous |
| 15:50:37 | May'26 29C | no_side | +0.339 | $350,000 | Front-week directional bid |
| 19:10:44 | Jan'27 27P | **bid** | -0.370 | $330,000 | Put sale / close |
| 18:22:09 | Nov'26 30P | **bid** | -0.558 | $128,975 | Put sale / close |
| 14:05:36 | Sep'26 35C | **bid** | +0.188 | $115,920 | Far-OTM call sale |

### IV outliers & Greeks [FLOW:iv_outliers / greek_screener]

- `iv_outliers` returned **empty** at the default `min-iv=1.0` floor —
  KWEB IV sits comfortably in the **29–37% band** across the term
  structure; no fat-tail single-name vol blowout signature.
- `greek_screener` (sort=premium) returns the same top-15 as
  `top_premium_trades`. Highest-gamma row is May'26 29C @ 0.229 — front-
  expiry pin candidate (see phase 3/4). Highest-vega rows are the Jan'27
  27P (0.087) and 30P (0.092), aligning with the bid-side put-vega
  liquidation noted above.

### Smart-money flow (market-wide context) [FLOW:smart_money_flow]

KWEB appears in **bearish** list only, single row:

- `KWEB260529C00032000`: bid_side_volume 24,663 vs ask 69, net flow
  −24,594, premium $74,077. Reads as **call writing / closing long calls
  at the 32 strike one week out** — small notional but it's the only
  KWEB contract that crossed the market-wide smart-money filter.

KWEB is absent from the **bullish** smart-money list; the broader market
list is dominated by IWM/SPY puts and VIX calls — the macro tape is
risk-off (relevant to phase 6).

### Sweep persistence over 5 sessions [FLOW:sweep_persistence]

| Ticker | Sessions in top | Consistency | Dominant dir | Total premium |
|--------|----------------|-------------|--------------|---------------|
| KWEB | **5 / 5** | **1.00** | **bearish** | **$94,897,773** |

This is the singular most important Phase-1 datapoint. KWEB sweep
aggressors have been bearish-tilted *every* session in the lookback,
totalling ~$95M of sweep premium. Today's mixed tape does NOT cancel
this — it reads as a partial reversal / two-way day on top of a
multi-day bearish trend. Downstream phases must validate or refute this
against dark pool prints (phase 2) and OI structure (phase 3).

### Sweep ratio (market-wide) [FLOW:sweep_ratio]

KWEB is absent from the top-25 sweep-ratio leaders. China-adjacent
appearance: **FXI 2026-05-22 36P, sweep_ratio 0.88, sweep_vol 1,611**
($29K premium) — a *small* directional bearish China-broad sweep, but
not at KWEB-specific notional.

## Tool calls (audit trail)

| Tool | Args | Result |
|------|------|--------|
| `options_flow_sweeps` | `{symbol: KWEB, min-premium: 100000, top-n: 25, date: 2026-05-19}` | 25 rows |
| `options_flow_unusual_volume` | `{symbol: KWEB, min-vol-oi-ratio: 3, top-n: 25, date: 2026-05-19}` | 4 rows |
| `options_flow_top_premium_trades` | `{symbol: KWEB, top-n: 25, date: 2026-05-19}` | 25 rows |
| `options_flow_iv_outliers` | `{symbol: KWEB, top-n: 15, date: 2026-05-19}` | **0 rows** |
| `options_flow_greek_screener` | `{symbol: KWEB, top-n: 15, sort-by: premium, date: 2026-05-19}` | 15 rows |
| `hot_chains_smart_money_flow` | `{direction: bullish, top-n: 25, min-volume: 500, date: 2026-05-19}` | 25 rows; 0 KWEB |
| `hot_chains_smart_money_flow` | `{direction: bearish, top-n: 25, min-volume: 500, date: 2026-05-19}` | 25 rows; 1 KWEB (260529 C32) |
| `hot_chains_sweep_persistence` | `{symbol: KWEB, days: 5, top-n: 20}` | 1 row (KWEB 5/5 bearish $94.9M) |
| `hot_chains_sweep_ratio` | `{top-n: 25, min-volume: 500, min-sweep-ratio: 0.3, date: 2026-05-19}` | 25 rows; 0 KWEB |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** mixed-leaning bearish (persistence > today's
  tape).
- **Conviction:** 3 / 5. The 5-day persistence is loud and singular, but
  today's tape includes a long-volatility straddle, a deep-ITM synthetic
  long, and Jan'27 put closes — none of which fit a clean bear-trend
  thesis. The aggressor mix today is dominated by upside-call selling
  (overwriting), which is *not* the same as buying downside.
- **Three things later phases should remember:**
  1. **KWEB has been a top-sweep ticker for 5 consecutive sessions, dominant_direction=bearish, $94.9M cumulative** — the dark-pool phase MUST check whether large block prints are confirming distribution or absorbing the bearish sweep flow.
  2. **A near-ATM Dec '26 29-strike straddle (~$1.75M combined) was bought as one paired trade today** — phases 4/5 should check what catalyst sits inside that 7-month window (China policy meetings, Hang Seng / CSI300 events, possible US-listing rule changes).
  3. **Front-month dealer-gamma flag**: Jun '26 30.5C with vol/OI 326× and gamma 0.114, *plus* May 29C with gamma 0.229. These two contracts dominate dealer near-money inventory and should drive phase-4 gamma analysis.
- **Open questions:**
  - Is the bid-side selling of upside calls (Jul 30C, Aug/Sep 35C) an *overwriting program by a holder* (bullish-supportive — implies they still own the underlying) or a *long-call liquidation* (bearish — closing prior bullish bets)? Dark-pool absorption pattern in phase 2 should help distinguish.
  - Is the $94.9M 5-day sweep premium concentrated in puts (clear bear) or in OTM-call sales (overwriting, neutral-to-bullish)? Persistence tool doesn't break that out; phase 3 OI delta-vs-volume + phase 7 `insights_*` need to answer.
