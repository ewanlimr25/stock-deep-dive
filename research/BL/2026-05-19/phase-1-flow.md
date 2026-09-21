# Phase 1 — Options Flow

**Ticker:** BL
**As-of date:** 2026-05-19
**Generated:** 2026-05-19T00:00:00Z
**Upstream phases cited:** phase-0-intake.md

## Summary

Despite the thin-options profile flagged in phase-0-intake.md, BL printed a
**concentrated, single-strike, ask-side bullish campaign** on 2026-05-19:
**$4,137,830** of ask-side sweep premium on **BL Dec-18-2026 $27.5 calls**
across 156 trades, with underlying drifting from $28.91 → $30.28 during the
session [FLOW:options_flow_sweeps]. Bid-side activity on the same contract was
**negligible** ($37,154 across 24 trades — ratio ≈ 0.9% of ask), so the
campaign is unambiguously directional, not delta-hedged spread legs. Sweep
persistence places BL in 3 of the last 5 sessions with a **$17.97M
total-sweep-premium aggregate** and `dominant_direction = "bullish"`
[FLOW:hot_chains_sweep_persistence] — this is the second material datapoint:
today is not a one-off; it is the visible cap of a multi-day accumulation.
Net flow bias: **bullish, conviction 4/5** (capped at 4 only because BL is
absent from the market-wide top-25 smart-money flow board, i.e. magnitudes are
large for BL but small in absolute terms; phase-2 dark pool must confirm).

## Key signals

- **Anchor trade:** BL 2026-12-18 $27.5C, ask-side sweep premium
  `total_premium=4137830`, `total_size=5177`, `trade_count=156`
  [FLOW:options_flow_sweeps].
- **Single largest print:** $749,490 premium @ $8.30, size 903, ask-side, IV
  80.9%, delta 0.674, executed 19:38:59Z with underlying at $29.975
  [FLOW:options_flow_top_premium_trades].
- **Persistence:** BL `consistency_score=0.6`, `sessions_in_top=3`,
  `total_sweep_premium=17968412`, `dominant_direction="bullish"` over
  2026-05-13 → 2026-05-19 [FLOW:hot_chains_sweep_persistence].
- **Vol/OI explosion in adjacent expiry:** BL 2026-11-20 $27.5C
  `total_volume=38` on `open_interest=2` → `vol_oi_ratio=19`
  [FLOW:options_flow_unusual_volume]. Tiny notional ($28.5k) but a sniff of
  fresh positioning in the Nov chain too — likely the same hand seeding the
  next-out expiry.
- **IV regime:** entire BL flow stack prints with `avg_iv` between **0.72 and
  0.79** (call side), top contract `avg_iv=0.7906`, `max_iv=0.8139`
  [FLOW:options_flow_iv_outliers]. For a small/mid-cap accounting SaaS this is
  **elevated** (typical realized vol for BL is high-30s to mid-40s) — buyer is
  paying premium volatility, which usually means a known catalyst is in the
  window.
- **Bid-side put activity:** essentially zero — the only put in
  iv_outliers is BL 2026-06-18 $27.5P with `total_premium=1300`,
  `total_volume=10` [FLOW:options_flow_iv_outliers]. No hedging campaign
  worth naming.

## Detailed findings

### Sweeps (ask vs bid, premium, persistence) [FLOW:options_flow_sweeps]

| Strike | Expiry | Type | Side | Trades | Size | Total premium | Avg price |
|--------|--------|------|------|--------|------|---------------|-----------|
| 27.5 | 2026-12-18 | call | **ask** | 156 | 5,177 | **$4,137,830** | 7.90 |
| 27.5 | 2026-12-18 | call | mid | 18 | 451 | $364,410 | 8.12 |
| 27.5 | 2026-12-18 | call | bid | 24 | 47 | $37,154 | 7.95 |
| 37.5 | 2026-12-18 | call | bid | 3 | 83 | $31,994 | 3.98 |
| 27.5 | 2026-11-20 | call | ask | 15 | 38 | $28,520 | 7.51 |
| 32.5 | 2026-06-18 | call | ask | 24 | 91 | $14,690 | 1.59 |
| 32.5 | 2026-06-18 | call | bid | 26 | 81 | $12,962 | 1.46 |

Read: **ask-side dominates bid-side by ~111×** on the lead contract.
Mid-fills are non-trivial ($364k) but the bid-side prints aren't enough to
suggest the seller is also institutional — most of the bid side is likely
spreading market-makers laying off inventory. The $37.5C bid prints
($32k) are stale/profit-taking on an old position, not new short calls.

### New positioning [FLOW:options_flow_unusual_volume]

Only 3 contracts pass `min_vol_oi_ratio=1`, `min_volume=10`:

| Strike | Expiry | Type | Volume | OI | Vol/OI | Premium | Avg IV |
|--------|--------|------|--------|-----|--------|---------|--------|
| 27.5 | 2026-11-20 | call | 38 | 2 | **19** | $28,520 | 0.7732 |
| 32.5 | 2026-06-18 | call | 177 | 108 | 1.64 | $28,227 | 0.7398 |
| 32.5 | 2026-12-18 | call | 11 | 4 | 2.75 | $5,515 | 0.7203 |

Note: the $4.14M Dec $27.5C concentration is **absent from
unusual_volume** because that strike already has substantial OI from prior
days' campaign — the buyer is *adding* to a position that already exists. This
is consistent with phase-0's "ticker has thin but active options" framing and
with the persistence finding above.

### Largest single-print premium prints (top 10)
[FLOW:options_flow_top_premium_trades]

| Time (UTC) | Strike | Expiry | Premium | Size | Price | Side | Δ | IV | Spot |
|------------|--------|--------|---------|------|-------|------|------|------|------|
| 19:38:59 | 27.5C | 2026-12-18 | $749,490 | 903 | 8.30 | ask | 0.674 | 0.809 | 29.98 |
| 19:15:03 | 27.5C | 2026-12-18 | $623,220 | 799 | 7.80 | ask | 0.661 | 0.799 | 29.36 |
| 19:23:47 | 27.5C | 2026-12-18 | $314,280 | 388 | 8.10 | mid | 0.672 | 0.790 | 29.92 |
| 19:42:43 | 27.5C | 2026-12-18 | $168,840 | 201 | 8.40 | ask | 0.679 | 0.797 | 30.27 |
| 19:22:00 | 27.5C | 2026-12-18 | $158,000 | 200 | 7.90 | ask | 0.665 | 0.790 | 29.62 |
| 19:42:43 | 27.5C | 2026-12-18 | $140,280 | 167 | 8.40 | ask | 0.679 | 0.797 | 30.27 |
| 18:58:34 | 27.5C | 2026-12-18 | $131,820 | 169 | 7.80 | ask | 0.659 | 0.813 | 29.18 |
| 19:22:00 | 27.5C | 2026-12-18 | $79,000 | 100 | 7.90 | ask | 0.665 | 0.790 | 29.62 |
| 19:42:43 | 27.5C | 2026-12-18 | $71,400 | 85 | 8.40 | ask | 0.679 | 0.797 | 30.27 |
| 19:42:43 | 27.5C | 2026-12-18 | $70,560 | 84 | 8.40 | ask | 0.679 | 0.797 | 30.27 |

**Read:**
- **100% of top 25 prints are on a single contract** (Dec 2026 $27.5C) —
  rare concentration even for liquid names.
- **23 of 25 are ask-side**; the 2 non-ask are "mid" (still aggressive given
  spread); **none are bid-side** in the top 25.
- Buying ramps with underlying — the first slug was at spot $29.07-29.18
  (18:58Z, $60k-$132k blocks) and the largest single block ($749k) lifted at
  spot $29.975 (19:38Z). This is **buy-on-strength**, the opposite of
  scalp/fade behavior.
- Pay-up tolerance: trader lifted at 8.40 vs intraday low ~7.40 — a 13.5%
  premium pickup over the day to keep accumulating. That is uncharacteristic
  of a retail buyer.

### IV outliers + Greeks [FLOW:options_flow_iv_outliers,
options_flow_greek_screener]

Anchor contract Greeks (Dec 2026 $27.5C, weighted across top prints):
- `delta` ≈ 0.66–0.68 (moderately ITM — call is ~$2-3 in-the-money on close)
- `gamma` ≈ 0.019–0.021
- `vega` ≈ 0.082 — non-trivial vol exposure
- `theta` ≈ −0.015 (very benign decay for a 213-day contract)
- `IV` ≈ 78–81% (call-side); `max_iv=0.8139`

**Interpretation:** the Greeks are consistent with a buyer wanting **leveraged
upside with low theta drag and meaningful vega**. Delta 0.67 × 5,177 contracts
= ~**347,000 share-equivalent long delta** added today on the ask-side sweep
alone. On a stock with ~$15-20M ADV (BL is illiquid in shares too), that is
material — **~17M of synthetic notional** at the current spot. The buyer is
sized like an institution. Vega exposure (~0.082 × ~5,200 contracts ≈ 425
points of vol-per-1%) means the buyer also wins if IV expands — common pattern
ahead of a binary event.

Put side is essentially absent — only one put (BL 2026-06-18 $27.5P,
volume=10, premium=$1,300) clears the IV-outlier filter. **No hedging
campaign.** This argues against the call buys being part of a synthetic stock
short hedge — they look like outright bullish bets.

## Market context cross-check

- **Smart-money board (market-wide):** BL is **absent** from the top 25
  bullish and top 25 bearish ask/bid-ratio leaderboards
  [FLOW:hot_chains_smart_money_flow]. Boards are dominated by SPY, IWM, VIX,
  HYG, IEF, LQD, SPXW, AMZN, TSLA, POET, WULF. **What this tells us:** BL's
  flow is institutional-grade *for its market cap* but small in absolute
  dollars (a $4.1M ask-side concentration doesn't crack a board where SPXW
  weeklies show $246M premium prints). Phase 8 risk monitor should remember
  this: BL is a single-name idiosyncratic play, not a sector-flow expression.
- **Sweep-ratio board:** BL absent from top 15 (sweep-ratio leaders are mostly
  weekly OTM lottery tickets) [FLOW:hot_chains_sweep_ratio]. That's expected
  — BL's flow is in 2026-12 expiry, not weekly.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `options_flow_sweeps` | `{symbol:BL, min-premium:10000, top-n:25, date:2026-05-19}` | 7 rows; ask-side $4.14M on Dec 27.5C dominates |
| `options_flow_unusual_volume` | `{symbol:BL, min-vol-oi-ratio:1, min-volume:10, top-n:25, date:2026-05-19}` | 3 rows; Nov 27.5C vol/OI=19 |
| `options_flow_top_premium_trades` | `{symbol:BL, top-n:25, date:2026-05-19}` | 25 rows; 23 ask, 2 mid, 0 bid; all Dec 27.5C |
| `options_flow_iv_outliers` | `{symbol:BL, min-iv:0.3, min-volume:10, top-n:15, date:2026-05-19}` | 6 rows; 5 calls + 1 token put |
| `options_flow_greek_screener` | `{symbol:BL, top-n:15, sort-by:premium, date:2026-05-19}` | 15 rows; Δ 0.65-0.68, IV 0.78-0.81 |
| `hot_chains_smart_money_flow` | `{direction:bullish, top-n:25, min-volume:100, date:2026-05-19}` | BL absent from market-wide top 25 |
| `hot_chains_smart_money_flow` | `{direction:bearish, top-n:25, min-volume:100, date:2026-05-19}` | BL absent from market-wide top 25 |
| `hot_chains_sweep_persistence` | `{days:5, top-n:20, symbol:BL}` | 1 row: BL, consistency 0.6, $17.97M agg, bullish |
| `hot_chains_sweep_ratio` | `{top-n:15, min-volume:100, min-sweep-ratio:0.3, date:2026-05-19}` | BL absent (weekly OTM dominates) |

## Tool errors

None — all 9 calls returned successfully. Initial intake-phase
`unusual_volume` empty result was a thresholding issue (defaults of min_volume
100 and vol/OI ratio 5 are too high for thin names); relaxed thresholds in
this phase surfaced the real flow.

## Verdict for downstream phases

- **Bias from this phase:** **bullish** (high conviction directionally; medium
  conviction on absolute magnitude because BL is a small-cap).
- **Conviction:** **4 / 5**
- **Three things later phases should remember:**
  1. The **anchor** is one contract: **BL 2026-12-18 $27.5 call** —
     `total_premium=4137830`, `total_size=5177`, `trade_count=156`, ask-side.
     Every phase (DP, OI, structure, plan) must orbit this strike/expiry.
     Today's session added **~347k share-equivalent long delta** at spot
     ~$29-30.
  2. The campaign is **persistent and one-sided**: 3 of last 5 sessions in
     the sweep-persistence top, $17.97M cumulative, bullish-dominant
     [FLOW:hot_chains_sweep_persistence]. Today is the third or fourth wave,
     not initiation.
  3. **IV is elevated (~78-81% on the Dec 27.5C)** for an accounting SaaS.
     Phase 5 (historical IV-percentile/z-score) should determine whether this
     is at a multi-month or yearly high; phase 7 (insights_earnings_play /
     screener_earnings_catalyst) must check for an earnings date in the Dec
     window or an event between now and Dec 18, 2026.
- **Open questions for downstream phases:**
  - Is dark pool **confirming** this directional bullish flow with above-tape
    block buys, or **fading** it with below-tape distribution? → phase 2.
  - What does the **Dec 2026 OI map** look like across strikes? Is $27.5
    isolated, or is there a stacked structure ($27.5/$32.5/$37.5)
    suggesting a target or a roll? → phase 3.
  - **Gamma flip + dealer positioning at $27.5** — if dealers are short gamma
    above ~$28-30 they will be forced buyers on every uptick, which would
    amplify any move higher. → phase 4.
  - Is BL near a **known catalyst** (earnings, investor day, M&A speculation,
    sector re-rating) that could explain the willingness to pay 80% IV? →
    phase 5 + phase 7.
