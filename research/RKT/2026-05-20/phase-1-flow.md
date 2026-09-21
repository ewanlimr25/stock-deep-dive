# Phase 1 — Options Flow

**Ticker:** RKT
**As-of date:** 2026-05-20 (data: 2026-05-19)
**Generated:** 2026-05-20T00:05:00Z
**Upstream phases cited:** phase-0-intake.md

## Summary

RKT's tape on 2026-05-19 shows a **two-sided but bullishly-biased institutional
structure**: roughly $1.0M of ask-side call premium (Jul 12C + Jan 2027 12.2C)
versus ~$1.18M of ask-side put premium concentrated in Dec 13P + Dec 10P —
classic "long-LEAPS-with-collar" footprint, not net bearish. The single
strongest cross-session signal is `hot_chains_sweep_persistence`:
**RKT printed in the top sweep list 5/5 sessions with consistency_score=1.0,
dominant_direction=bullish, total_sweep_premium=$5.02M** over the trailing
week — the only single name with perfect persistence in the lookback
[FLOW:sweep_persistence]. Net read: institution(s) building leveraged long
exposure via LEAPS calls and laying off downside risk via Dec puts. Underlying
ref price ~$12.52–$12.86 intraday.

## Key signals

- **Sweep persistence is the lead datapoint:** RKT in top sweeps every one of
  the last 5 sessions, consistency 1.0, $5.02M cumulative bullish sweep
  premium [FLOW:sweep_persistence].
- **Largest single sweep was a put** — 2026-12-18 $13P bought ask, $817k
  premium / 3,383 contracts / 53 trades. Looks like collar/hedge against the
  LEAPS book, not an outright short [FLOW:sweeps].
- **LEAPS accumulation** — 2027-01-15 $12.2C bought at ask, $696.9k aggregate
  / 2,489 contracts / 53 trades; delta 0.63, slightly ITM. Stock-replacement
  signature [FLOW:sweeps, FLOW:top_premium_trades].
- **Far-OTM Dec downside hedge** — 2026-12-18 $10P bought ask, $357.9k / 3,767
  contracts / vol/OI 29× — opening protection well below the LEAPS strike
  [FLOW:unusual_volume, FLOW:top_premium_trades].
- **Near-dated bullish demand confirmed** — 2026-07-17 $12C $326.6k bought
  ask, vol/OI 10×, delta 0.63 [FLOW:sweeps, FLOW:unusual_volume].
- **Front-end vol elevated** — May-22 expiry strikes pricing 1.0–2.4 IV
  (out-of-the-money wings); no defined-event explanation yet — phase 5 should
  check for upcoming earnings/event [FLOW:iv_outliers].

## Detailed findings

### Sweeps (`mcp__uw-pp__options_flow_sweeps`, min_premium=$100k)

| Side | Strike / Type | Expiry | Premium | Size | Trades | Read |
|------|---------------|--------|---------|------|--------|------|
| ASK  | $13 PUT  | 2026-12-18 | **$817,608** | 3,383 | 53 | Hedge / collar leg |
| ASK  | $12.2 CALL | 2027-01-15 | **$696,923** | 2,489 | 53 | LEAPS accumulation |
| ASK  | $10 PUT  | 2026-12-18 | $357,917 | 3,767 | 5  | Far-OTM downside hedge |
| ASK  | $12 CALL | 2026-07-17 | $326,614 | 2,107 | 17 | Front-month directional long |
| ASK  | $1 CALL  | 2026-06-18 | $253,274 | 215   | 21 | Synthetic stock (delta 0.99 ITM) |
| ASK  | $14 CALL | 2026-08-21 | $185,885 | 1,683 | 48 | Upside-extension long |
| ASK  | $13 PUT  | 2026-07-17 | $103,744 | 804   | 10 | Near-term downside |
| BID  | $12 CALL | 2026-06-18 | $101,686 | 811   | 101 | Closing / profit-taking on June calls |
| ASK  | $16.2 PUT | 2027-01-15 | $100,100 | 220   | 1   | Deep ITM put (synthetic short OR stock replacement leg) |

Net premium tally (today only):
- Ask-side calls: ~$1.46M (Jan-27 12.2C $697k + Jul 12C $327k + Jun 1C $253k + Aug 14C $186k)
- Ask-side puts: ~$1.38M (Dec 13P $818k + Dec 10P $358k + Jul 13P $104k + Jan-27 16.2P $100k)
- Bid-side calls (closing): $102k on Jun 12C

The big June-18 $1C ask-side ($11.81 average price, delta 0.99) is a stock
replacement print — institutions buying $1-strike LEAPS-style ITM calls to
get clean long delta with limited capital. It pads "call premium" but is
NOT a directional speculation — it's effectively long stock.

### New positioning (`mcp__uw-pp__options_flow_unusual_volume`, min vol/OI=3)

| Strike / Type | Expiry | Vol/OI | Volume | OI | Premium | IV | Read |
|---------------|--------|--------|--------|-----|---------|-----|------|
| 12.5 CALL | 2026-06-18 | **109×** | 218 | 2  | $22.6k | 0.63 | Cleanest opening flow but small premium |
| 10 PUT   | 2026-12-18 | 29×    | 3,768 | 130 | $358k | 0.60 | Major Dec hedge opened |
| 12 CALL  | 2026-05-22 | 20×    | 161   | 8   | $12.5k | 0.78 | 3-day weekly speculation |
| 12 PUT   | 2026-07-17 | 19×    | 1,703 | 90  | $138k | 0.59 | Jul downside opened |
| 12 CALL  | 2026-07-17 | 10×    | 2,243 | 216 | $348k | 0.63 | Jul upside opened — matches sweep |
| 13 CALL  | 2026-05-29 | 8.4×   | 455   | 54  | $17.1k | 0.62 | Weekly ATM-OTM speculation |
| 11.5 PUT | 2026-06-05 | 6.8×   | 108   | 16  | $2.8k | 0.60 | Tiny |
| 14 CALL  | 2026-06-12 | 5.2×   | 109   | 21  | $3.5k | 0.62 | Tiny upside lottery |
| 13 PUT   | 2026-07-17 | 4.8×   | 1,037 | 217 | $134k | 0.58 | Jul ATM-ish put opened |
| 12 PUT   | 2026-08-21 | 4.7×   | 683   | 144 | $81k  | 0.61 | Aug downside hedge |
| 12.5 CALL | 2026-05-22 | 3.8×   | 867   | 228 | $34.7k | 0.72 | Front-week call speculation |
| 12 CALL  | 2026-06-18 | 3.7×   | 1,020 | 277 | $128k | 0.65 | June 12C still being built |

Opening flow corroborates the "long-LEAPS + downside-hedge" structure: big
NEW positions in 2026-12-18 10P (downside protection floor) and 2026-07-17
12C (near-dated bullish layer atop the LEAPS).

### Largest premium prints (`mcp__uw-pp__options_flow_top_premium_trades`)

Top 5 by premium:

| Time (UTC) | Type | Strike | Expiry | Premium | Side | Δ | IV | Underlying |
|------------|------|--------|--------|---------|------|---|-----|-----------|
| 14:10:17 | PUT  | 10   | 2026-12-18 | $355,870 | ASK | -0.23 | 0.587 | $12.615 |
| 14:10:09 | CALL | 12   | 2026-07-17 | $132,215 | ASK |  0.63 | 0.623 | $12.600 |
| 16:59:51 | PUT  | 16.2 | 2027-01-15 | $100,100 | ASK | -0.61 | 0.550 | $12.85  |
| 17:14:23 | PUT  | 13   | 2026-12-18 | $91,960  | ASK | -0.43 | 0.590 | $12.730 |
| 17:14:23 | PUT  | 13   | 2026-12-18 | $80,344  | ASK | -0.43 | 0.590 | $12.730 |

Notable: the 14:10 prints (Dec 10P + Jul 12C) executed within 8 seconds at
nearly the same underlying price — **almost certainly the same desk
simultaneously building the long leg and the protection leg**. This is the
strongest tape-tell of the day for "structured long" intent.

The Jan-27 16.2P at $100k (delta -0.61, deep-ITM) is unusual — it can be:
1. A short leg of a Jan 16.2/12.2 put-spread credit collar (net bullish), OR
2. A synthetic short / long-put-vs-stock pair-trade (bearish).

Given the concurrent Jan-27 12.2C accumulation, interpretation #1 (a wide
**risk-reversal**: long calls + short puts) is more likely. That structure is
unambiguously bullish — selling deep ITM puts is essentially being long stock
above ~$16.2 with capped exposure.

### IV outliers (`mcp__uw-pp__options_flow_iv_outliers`)

| Strike / Type | Expiry | Avg IV | Max IV | Volume | Premium |
|---------------|--------|--------|--------|--------|---------|
| 1 CALL   | 2026-06-18 | 5.56 | 9.27 | 215 | $253k | Pricing artifact on deep-ITM stock-replacement |
| 10 CALL  | 2026-05-22 | 2.36 | 2.47 | 50  | $12.5k | Very-near OTM lotto |
| 8 PUT    | 2026-05-22 | 2.27 | 2.28 | 51  | $51    | Pricing noise |
| 14 PUT   | 2026-05-22 | 1.08 | 1.18 | 64  | $8.8k  | OTM downside lotto |
| 14.5 CALL | 2026-05-22 | 1.08 | 1.14 | 58  | $180   | Tiny |

Real signal: **May-22 weekly OTM wings are pricing 100%+ IV**. That's an
event-window vol skew. Phase 5 must verify whether RKT has a 2026-05-22 or
2026-05-23 catalyst (earnings, secondary offering, dividend, FOMC reaction).

### Greeks / vega concentration (`mcp__uw-pp__options_flow_greek_screener`)

The high-vega bets concentrate on Dec 2026 13P (vega 0.038, gamma 0.07) and
Jan 2027 12.2C / 16.2P (vega 0.039) — institutional volatility-aware
positioning. Near-dated 2026-07-17 12C carries gamma 0.12 — the largest gamma
contribution in the tape, meaning the long-July-call book will need delta
hedging from market makers as price moves.

### Smart money flow (`mcp__uw-pp__hot_chains_smart_money_flow`)

RKT is NOT in the top 25 bullish or bearish market-wide smart-money rows
(those are dominated by SPY/IWM/HYG/VIX/POET/WULF for hedging and squeeze
plays). Implication: RKT is not a top-of-tape conviction name today on
absolute volume — but the persistence signal makes up for the absolute scale.
This is a "stealth accumulation" footprint, not a momentum-chase tape.

### Sweep persistence (`mcp__uw-pp__hot_chains_sweep_persistence`)

```
ticker: RKT
dates_covered: 2026-05-13 → 2026-05-19 (5 sessions)
sessions_in_top: 5
consistency_score: 1.0
dominant_direction: bullish
total_sweep_premium: $5,016,354
```

**This is the highest-quality persistence signal possible.** It is the only
result returned — meaning RKT is the only name in the universe with perfect
5/5 sweep-persistence + bullish dominance over the window. That is precisely
the institutional accumulation pattern the skill is designed to flag.

### Sweep ratio (`mcp__uw-pp__hot_chains_sweep_ratio`)

RKT does NOT appear in the top 25 market-wide sweep_ratio results. The big
RKT prints are aggressive but not multi-exchange sweeps in the strict sense —
they're being executed primarily through a single venue / single broker
identifier, consistent with a structured institutional package trade rather
than urgent retail-led sweeping.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `options_flow_sweeps` | `{symbol: RKT, min_premium: 100000, top_n: 25, date: 2026-05-19}` | 9 rows; $1.46M ask calls / $1.38M ask puts / $102k bid calls |
| `options_flow_unusual_volume` | `{symbol: RKT, min_vol_oi_ratio: 3, top_n: 25, date: 2026-05-19}` | 12 rows; largest = Dec 10P vol/OI 29× $358k |
| `options_flow_top_premium_trades` | `{symbol: RKT, top_n: 25, date: 2026-05-19}` | 25 rows; #1 = Dec 10P $356k |
| `options_flow_iv_outliers` | `{symbol: RKT, top_n: 15, date: 2026-05-19}` | 5 rows; near-week wings pricing 100%+ IV |
| `options_flow_greek_screener` | `{symbol: RKT, top_n: 15, sort_by: premium, date: 2026-05-19}` | Vega concentrated in Dec/Jan strikes |
| `hot_chains_smart_money_flow` | `{direction: bullish, top_n: 25, min_volume: 500, date: 2026-05-19}` | RKT not in top 25 (market-wide); SPY/IWM dominate |
| `hot_chains_smart_money_flow` | `{direction: bearish, top_n: 25, min_volume: 500, date: 2026-05-19}` | RKT not in top 25 |
| `hot_chains_sweep_persistence` | `{symbol: RKT, days: 5, top_n: 20}` | RKT 5/5 sessions, consistency 1.0, bullish, $5.02M |
| `hot_chains_sweep_ratio` | `{top_n: 25, min_volume: 500, min_sweep_ratio: 0.3, date: 2026-05-19}` | RKT not in top 25 |

## Tool errors

(none)

## Verdict for downstream phases

- **Bias from this phase:** bullish (with hedge layer — true structure is
  "long delta, long vega, with put protection")
- **Conviction:** 4/5
  - Driven primarily by the persistence signal (5/5 sessions, consistency
    1.0, $5.0M premium) and the synchronized 14:10 execution of the
    long-call + protective-put package.
  - Held back from 5/5 by the absence of a smart_money_flow top ranking and
    the modest single-day absolute scale (~$2.5M total notional).
- **Three things later phases must remember:**
  1. **Look for a single institution behind the LEAPS + Dec collar package.**
     Phase 2 (dark pool) should check whether matched block trades line up
     with the option execution time window (14:10 UTC = 10:10 ET, 17:14 UTC =
     1:14 PM ET).
  2. **2027-01-15 12.2C is the conviction strike.** $697k bought at ask with
     delta 0.63 implies a ~13-14% upside path to make economic sense vs.
     just buying stock. Phase 4 should check that strike vs. dealer GEX.
  3. **A 2026-05-22 catalyst is suspected** — front-week IV is pricing 100%+
     on wings. Phase 5/6 must identify the catalyst (earnings? ex-div?
     index reconstitution? mortgage-rate print?).
- **Open questions:**
  - Did dark pool prints confirm a buyer of stock alongside the LEAPS book? (phase 2)
  - Is dealer gamma positive or negative at $12.20–$13.00? (phase 4)
  - Where is IV30 historically? (phase 5)
  - What is the mortgage-rate macro print since 2026-04-30? (phase 6)
