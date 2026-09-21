# Phase 1 — Options Flow

**Ticker:** SNOW
**As-of date:** 2026-05-16 (data date: 2026-05-15)
**Generated:** 2026-05-17T00:00:00Z
**Upstream phases cited:** phase-0-intake.md

## Summary

SNOW options tape on 2026-05-15 was **net bullish with active two-way LEAP positioning**. The session saw $5+ intraday spot rally ($153.55 → $159.18) accompanied by aggressive ask-side ITM call buying (Jun-26-26 $145C, $2.10M premium, vol/OI 314.67) and far-OTM call sweeps (Jun-18 $200C, $1.51M premium, 3,342 contracts). LEAP activity is structurally bullish (Dec-28 $260/$280 call spread bought for net ~$220k debit on 538 spreads) but offset by a smaller Jan-28 $270/$320 bear call spread credit ($140k). The 5-day sweep_persistence score of 1.0 with "mixed" direction confirms SNOW is on every sweep desk's radar but conviction is split between near-term bulls and long-dated neutrals.

## Key signals

- **Single largest premium print:** SNOW Jun-26-26 $145C ask, 467 contracts @ $23.60, **$1,102,120 premium**, delta 0.67, IV 80.9% — clear directional ITM call buy [FLOW:top_premium_trades].
- **Highest vol/OI ratio:** SNOW Jun-26-26 $145C **vol/OI = 314.67** on aggregated 944 contracts (OI=3), $2.10M total premium — confirmed brand-new opening position [FLOW:unusual_volume].
- **OTM upside lottery:** Jun-18-26 $200C ask-side sweep, 3,342 contracts (avg $4.52), **$1,514,023 premium** — 33 mins to spot from $158 to $200 = 27% OTM upside bet [FLOW:sweeps].
- **LEAP bull call spread:** Dec-15-28 $260C ask (538 ct, $2,288,374) + Dec-15-28 $280C bid (538 ct, $2,069,109) — matched 11 trades each side = single actor buying 260/280 call spread for ~$219k net debit on 538 spreads, max payoff $20/spread (≈$1.08M max value) [FLOW:sweeps].
- **Persistent presence on sweep tape:** SNOW appeared in top sweeps **all 5 of last 5 sessions** (consistency_score=1.00), total 5-day sweep premium **$57,302,192**, dominant_direction "mixed" [FLOW:sweep_persistence].

## Detailed findings

### Spot context (extracted from trade timestamps)

The trade tape shows SNOW rallied intraday from $153.55 (13:57Z) to $159.18 (17:24Z) and closed around $157.88-$158.05 (19:52Z). Intraday range ≈ $5.63 (3.6%). All subsequent analysis assumes spot ≈ $158 at close.

| Timestamp (UTC) | Spot |
|---|---|
| 13:57 | $153.55 |
| 14:37 | $155.45 |
| 15:10 | $157.63 |
| 15:20 | $158.18 |
| 16:16 | $157.83 |
| 16:55 | $158.99 |
| 17:24 | $159.18 |
| 19:52 | $157.88 |

### Sweeps (ask vs bid)

Top sweeps (premium ≥ $100k) ranked by total premium [FLOW:sweeps]:

| Expiry | Strike | Type | Side | Size | Premium | Avg Price | Trades |
|---|---|---|---|---|---|---|---|
| 2028-12-15 | 260 | call | **ask** | 538 | $2,288,374 | $42.44 | 11 |
| 2028-12-15 | 280 | call | bid | 538 | $2,069,109 | $38.65 | 11 |
| 2026-06-18 | 160 | call | bid | 1,118 | $1,711,229 | $15.22 | 215 |
| 2026-06-18 | 200 | call | **ask** | 3,342 | $1,514,023 | $4.52 | 418 |
| 2026-06-26 | 145 | call | **ask** | 556 | $1,289,020 | $22.30 | 2 |
| 2026-05-15 | 155 | call | **ask** | 4,639 | $1,190,657 | $2.67 | 1,816 |
| 2026-05-29 | 155 | call | bid | 847 | $1,170,911 | $13.78 | 188 |
| 2026-05-29 | 150 | call | bid | 536 | $16,487 | $16.49 | 74 |
| 2026-05-29 | 155 | call | **ask** | 628 | $871,943 | $13.80 | 137 |
| 2026-05-15 | 155 | call | bid | 3,873 | $845,492 | $2.14 | 1,043 |
| 2026-06-26 | 145 | call | bid | 387 | $812,860 | $21.18 | 8 |
| 2026-05-22 | 160 | call | bid | 1,507 | $716,805 | $4.91 | 739 |
| 2028-01-21 | 270 | call | bid | 212 | $568,699 | $26.50 | 5 |
| 2026-05-22 | 160 | call | **ask** | 1,127 | $550,730 | $4.99 | 516 |
| 2026-08-21 | 145 | **put** | bid | 347 | $527,584 | $15.22 | 43 |
| 2026-06-18 | 145 | call | **ask** | 208 | $488,682 | $22.17 | 19 |
| 2028-01-21 | 320 | call | **ask** | 202 | $400,909 | $19.65 | 3 |

**Ask vs bid premium tally (calls only, top 25):**
- Total ask-side call premium: ~**$8.5M**
- Total bid-side call premium: ~**$8.4M**
- Near-parity, but **timing and structure favor the ask side** — the largest single ask-side block ($1.10M 145C Jun-26 at 15:10) coincides with the start of the intraday rally, and ITM buys (delta > 0.6) skew ask-side.

**Pairing detection:**
- Dec-15-28 260C ask (538 ct) + 280C bid (538 ct) = 1× 260/280 bull call spread buy at net debit ~$3.79/share. Max value $20, breakeven $263.79 (delta-equivalent of "SNOW > $264 by Dec 2028").
- Jan-21-28 270C bid (212 ct) + 320C ask (202 ct) = ~1× 270/320 bear call spread sold at net credit ~$7/share. Max risk $43/share, betting SNOW < $270 by Jan 2028.
- These are clearly **two different actors** with opposite long-dated views.

**Put activity:** Only one meaningful put sweep — Aug-21-26 $145P **bid**, 347 contracts @ $15.22, $527,584 premium. **Bid-side put = put SELLING = bullish** (collecting premium on the assumption SNOW > $145 by Aug). One $260P ask Jun-18 at $105.97 (37 ct, $392k) is deep ITM and likely a synthetic/combo leg, not a directional bet.

### New positioning (unusual volume)

[FLOW:unusual_volume] confirmed new-opening contracts:

| Expiry | Strike | Type | OI | Volume | Vol/OI | Premium | Avg IV |
|---|---|---|---|---|---|---|---|
| 2026-06-26 | 145 | call | 3 | 944 | **314.67** | $2,104,220 | 80.8% |
| 2026-06-26 | 100 | call | 1 | 100 | 100 | $608,250 | 119.7% |
| 2028-12-15 | 260 | call | 11 | 539 | 49 | $2,292,574 | 66.2% |
| 2026-05-22 | 157.5 | put | 10 | 134 | 13.4 | $74,851 | 67.5% |
| 2026-05-29 | 162.5 | call | 12 | 107 | 8.9 | $118,636 | 106.1% |
| 2028-12-15 | 280 | call | 79 | 538 | 6.8 | $2,069,109 | 65.4% |

The Jun-26-26 100C with vol/OI=100 at IV 120% deserves attention — 50 contracts traded at $60/contract bid for $300k, delta 0.93. This is buying deep-ITM 100C as a synthetic stock substitute with leverage. Spot $158 means $100C is $58 intrinsic + premium = high-delta stock proxy. Combined with the 145C buy and put selling, the actor profile is **bullish-leveraged**.

### Largest premium prints (single trades)

[FLOW:top_premium_trades]:

| Time (UTC) | Expiry | Strike | Type | Side | Size | Premium | Δ | IV | Spot |
|---|---|---|---|---|---|---|---|---|---|
| 15:10 | 2026-06-26 | 145C | call | **ask** | 467 | $1,102,120 | 0.67 | 0.81 | 157.63 |
| 13:57 | 2026-06-26 | 145C | call | bid | 285 | $598,500 | 0.64 | 0.81 | 153.55 |
| 19:39 | 2028-01-21 | 270C | call | bid | 200 | $537,000 | 0.42 | 0.65 | 158.05 |
| 16:16 | 2028-12-15 | 260C | call | **ask** | 108 | $462,780 | 0.53 | 0.67 | 157.83 |
| 16:16 | 2028-12-15 | 280C | call | bid | 108 | $408,780 | 0.49 | 0.65 | 157.83 |
| 19:39 | 2028-01-21 | 320C | call | **ask** | 200 | $397,000 | 0.34 | 0.64 | 158.05 |
| 16:55 | 2026-06-18 | 145C | call | **ask** | 140 | $332,500 | 0.69 | 0.85 | 158.99 |
| 15:20 | 2026-09-18 | 155C | call | **ask** | 111 | $318,570 | 0.60 | 0.74 | 158.18 |

The single highest-conviction print of the day is the **15:10Z $145C ask block** at spot $157.63. The trader paid up $23.60 for an ITM call worth ~$12.63 intrinsic + ~$10.97 extrinsic — implying they want **delta + vega + some time premium** until Jun 26. This is not a hedge; it is a leveraged directional bet that SNOW continues higher into June.

### IV outliers

[FLOW:iv_outliers] is dominated by 5/15 0DTE expiry contracts with vol-of-vol blowups (max_iv 170%, etc.) — these are gamma-scalping/pinning artifacts and not signal. The only non-0DTE outlier worth noting is the 2026-06-26 $100C at IV 119.7% (driven by deep-ITM premium structure, not informational).

### Smart money flow (market-wide)

[FLOW:smart_money_flow] top 25 bullish and bearish — **SNOW does not appear in either list**. The bullish list is dominated by TLT puts, F calls, NU puts, INTC puts, PEP calls; the bearish list is dominated by IWM/SMH puts and SPY 0DTE calls. This means SNOW's directional volume on 5/15 was not extreme enough relative to market to crack the top 25 in absolute net-flow contract count, but as the sweep_persistence tool shows, SNOW IS active on the sweep-premium dimension — a different cut.

### Greek screener (premium-sorted)

[FLOW:greek_screener] top trades restate the top_premium_trades data with Greeks. Key takeaways:
- The two LEAP $260C asks have **vega 1.01** — heavily vega-sensitive, so the trader is also betting on IV expansion.
- The 145C Jun-26 ask has **gamma 0.0084** — modest, expected for ITM.
- The OTM 200C Jun-18 lottery has **delta 0.22** — large notional but cheap per-contract exposure.

### Sweep persistence (5-day)

[FLOW:sweep_persistence]:

```
ticker: SNOW
sessions_in_top: 5 / 5
consistency_score: 1.00
total_sweep_premium: $57,302,192
dominant_direction: mixed
```

SNOW has been on the institutional sweep radar **every single trading day** of the last 5 sessions, with $57M in cumulative sweep premium. The "mixed" direction tag confirms what the 5/15 tape also shows: two-way conviction. This is institutional positioning, not retail FOMO.

### Sweep ratio (market-wide)

SNOW does not appear in the top 15 single-day sweep_ratio list [FLOW:sweep_ratio]. The list is dominated by small-cap names (DJT, AMD, AAPL LEAPs, BCS, QQQ 0DTE). SNOW's sweeps are large-premium but not extreme-sweep-share contracts.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__options_flow_sweeps` | symbol=SNOW, min_premium=100k, top_n=25, date=2026-05-15 | 25 contracts; near-parity ask/bid call premium |
| `mcp__uw-pp__options_flow_unusual_volume` | symbol=SNOW, min_vol_oi_ratio=3, top_n=25 | 16 contracts; top vol/OI 314.67 on 145C Jun-26 |
| `mcp__uw-pp__options_flow_top_premium_trades` | symbol=SNOW, top_n=25 | Largest = $1.10M 145C ask 15:10Z |
| `mcp__uw-pp__options_flow_iv_outliers` | symbol=SNOW, top_n=15 | Mostly 0DTE gamma artifacts; one informational 100C |
| `mcp__uw-pp__options_flow_greek_screener` | symbol=SNOW, top_n=15, sort_by=premium | Confirms vega-heavy LEAP positioning |
| `mcp__uw-pp__hot_chains_smart_money_flow` | direction=bullish, top_n=25, min_volume=500 | SNOW not in top 25 |
| `mcp__uw-pp__hot_chains_smart_money_flow` | direction=bearish, top_n=25, min_volume=500 | SNOW not in top 25 |
| `mcp__uw-pp__hot_chains_sweep_persistence` | symbol=SNOW, days=5, top_n=20 | 5/5 sessions, $57.3M sweep premium, mixed |
| `mcp__uw-pp__hot_chains_sweep_ratio` | top_n=15, min_volume=500, min_sweep_ratio=0.3 | SNOW not in top 15 |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** **bullish** (near-term 1-6 weeks), **mixed** (LEAP horizon).
- **Conviction:** 4/5 — premium magnitude is large ($2M+ single-strike concentration on 145C Jun-26), the buyer paid ask intraday during a rally, persistence is 5/5, but the LEAP tape shows two-way action that bars a 5/5.
- **Three things later phases should remember:**
  1. **$145 strike Jun-26-26 calls** are the highest-conviction near-term institutional bet ($2.10M premium, vol/OI 314.67, ask-side block at 15:10Z). Phase 3 should look for matching OI buildup; phase 4 should check $145 as a gamma/dealer wall.
  2. **Spot closed near $158** with a strong intraday rally from $153.55 — momentum is up but the move is ~1 day old. Phase 2 should check whether dark pool flow was simultaneously absorbing or distributing.
  3. **5-day sweep premium $57.3M with mixed direction** — SNOW is institutional consensus *interest*, not institutional consensus *direction*. Phase 7's `insights_signal_confluence` should weight this against agreement signals.
- **Open questions:**
  - Is there a known catalyst (earnings, analyst day, product event) driving the 6-week $145C buy? Phase 6 macro overlay and phase 7 earnings_play tools need to check.
  - Is the LEAP $260/$280 call spread a long-term conviction trade or a hedge against an even-larger short position elsewhere?
  - Why is the 5-day direction "mixed" if today was clearly net bullish? Did prior sessions skew bearish?
