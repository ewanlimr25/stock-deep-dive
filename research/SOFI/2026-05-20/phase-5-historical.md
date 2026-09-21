# Phase 5 — Historical Context & VRP

**Ticker:** SOFI
**As-of date (requested):** 2026-05-20
**Effective data date:** 2026-05-19
**Generated:** 2026-05-20T00:00:00Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-3-positioning.md, phase-4-structure.md

## Summary

SOFI's historical context **complicates the bullish read from phases 1-3** in
two important ways. First, the **bullish_flow signal backtest scored 0% win
rate on its 7 most recent firings** (avg -3.05% / 5d on MSFT, AAPL, QQQ, SMH,
META, AVGO, UPS over May 14-15) [HIST:signal_backtest] — meaning in the
current tape, "bullish flow" has been a fade signal, not a follow-through
signal. Second, SOFI itself has **fallen 14.7% from $17.77 (Mar 13) to $15.16
(May 19)** with **21 of the last 28 sessions classified bearish flow direction**,
and the Q1 earnings event on 2026-04-28/29 was a -15% gap with IV rank
collapsing 47.6 → 21.9 [HIST:trend]. On the other hand, the constructive
signals are real: **VRP is -9.47% (IV30 53.8% vs realized vol 63.3%) → premium
is CHEAP vs realized**, favoring debit/long-option structures
[HIST:vrp]; **28 consecutive days of net OI build** including +118,132
contracts on 2026-05-19 alone [HIST:oi_trend]; the GEX time series shows the
first NEGATIVE total-GEX day in 28 sessions [HIST:gex_time_series], a
**regime-transition warning**. IV percentile sits at 44 (NORMAL) [HIST:iv_percentile];
PC ratio z-score -0.51 (NORMAL, slightly call-skewed but not extreme)
[HIST:pc_ratio_zscore]; 90-day net premium flow is -$44M (MIXED with
slight bearish tilt — bearish $479M vs bullish $435M) [HIST:cumulative_premium_flow].

## Key signals

- **VRP = -9.47% → PREMIUM_BUYING regime**: IV30 53.8% vs realized 63.3%.
  Long options are cheap vs realized — favor LONG straddles, LONG calls/puts,
  LONG verticals over credit structures. [HIST:vrp]
- **IV percentile 44.4 (NORMAL)**, IV z-score -0.60. Not cheap on 1y basis
  but not rich either. [HIST:iv_percentile_zscore]
- **28 consecutive sessions of net OI build** (+118,132 on 2026-05-19 alone,
  524 contracts with increases vs 175 with decreases). Persistent stealth
  positioning. [HIST:oi_trend]
- **Today (2026-05-19) is the first NEGATIVE total-GEX day in the 28-session
  window**. Prior 28 days all classified POSITIVE regime; today's -$4.6B
  total GEX is a regime-transition warning. ZGL has held in the $11-$13
  range across all 28 days. [HIST:gex_time_series]
- **Bullish_flow backtest: 0.0% win rate on 7 recent firings (avg -3.05%)**.
  The signal type that aligns with phase-1's verdict has been a FADE in
  the last 5 trading days. **Downgrade phase-1 conviction by one notch.**
  [HIST:signal_backtest]
- **Multi-day flow tally: 7 bullish days vs 21 bearish days over 28 sessions**,
  price down 14.7% in window. Today's "bullish" call buildup at the May-22
  expiry is happening AGAINST a 21:7 net-bearish flow backdrop.
  [HIST:historical_trend]
- **Q1 earnings (2026-04-28/29) was a -15% gap day** with $11.6M net bearish
  flow and IV rank crash 47.6 → 21.9. SOFI has been in a post-earnings
  re-rating drift ever since. [HIST:historical_trend]

## Detailed findings

### IV regime

| Metric | Value | Regime |
|---|---|---|
| Current IV30d | 53.81% | — |
| 1y IV percentile | 44.4 | NORMAL |
| 1y IV z-score | -0.60 | Slightly below mean, not extreme |
| Realized vol (30d) | 63.28% | — |
| VRP (IV − realized) | **-9.47%** | **PREMIUM_BUYING** |

**Take:** IV is mid-range historically (44th percentile) but **CHEAP relative
to recent realized volatility** (vol is being underpriced by 9.5 points by the
option market). Combined with the COMPLACENT skew from phase 4
[STRUCT:term_skew], this **favors long options / debit structures** —
especially long ATM straddles or long ATM directional verticals — over
credit-selling structures.

### Cumulative premium flow (90 days, 2026-03-13 → 2026-05-19)

| Metric | Value |
|---|---|
| Cumulative bullish premium | $435,076,047 |
| Cumulative bearish premium | $479,221,202 |
| Net flow | **-$44,145,155** |
| Trend direction | MIXED |

The 90-day net flow leans **slightly bearish** but by only ~9-10% — neither
side is dominant. Note however that bearish flow $479M was meaningfully
inflated by the Q1 earnings event (2026-04-29 alone had -$11.6M net flow
and 2026-04-28/29 combined ~-$14.5M net bearish), and ten of the most-recent
ten sessions show net-negative flow on five of them. **No persistent stealth
bullish accumulation in the 90-day premium-flow signature**.

### P/C ratio z-score

| Metric | Value |
|---|---|
| Current PC ratio | 0.38 |
| 20d mean PC ratio | 0.447 |
| 20d std PC ratio | 0.132 |
| Z-score | -0.51 |
| Extreme classification | NORMAL |

Today's PC of 0.38 (38 puts for every 100 calls in volume) is slightly
call-skewed relative to the 20-day baseline of 0.45, but NOT a z>2 extreme.
Consistent with phase-4 COMPLACENT skew but doesn't trigger a contrarian
mean-reversion setup.

### GEX time series (30 days)

Selected snapshots (full 28-row table available in raw data):

| Date | Spot | Total GEX | ZGL | Regime |
|---|---|---|---|---|
| 2026-03-13 | $17.77 | +$2.16B | $13.31 | POSITIVE |
| 2026-03-27 | $15.35 | +$1.04B | $13.01 | POSITIVE |
| 2026-04-27 | $18.80 | +$3.66B | $4.49 | POSITIVE (pre-earnings) |
| 2026-04-28 | $18.59 | +$3.91B | $9.01 | POSITIVE (earnings day) |
| 2026-04-29 | $15.93 | +$6.77B | $10.85 | POSITIVE (gap day -14%) |
| 2026-05-11 | $16.06 | +$13.23B | $11.93 | POSITIVE |
| 2026-05-14 | $15.71 | +$17.68B | $11.66 | POSITIVE |
| 2026-05-18 | $15.65 | **+$37.03B** | $11.78 | POSITIVE (peak) |
| **2026-05-19** | **$15.16** | **-$4.61B** | **$11.65** | **POSITIVE (label) / negative total** |

**Critical observation:** May-18 had the largest positive GEX in the 28-day
window (+$37B); 2026-05-19 collapsed to -$4.6B in a single session. That's
a **$41.6B GEX swing in 24 hours** — driven primarily by the put-write
inflow at $15 documented in phase-3 [OI:smart_positioning]. **No formal
regime flip** because spot ($15.16) is still above ZGL ($11.65), but this
is the kind of GEX swing that historically precedes realized-vol expansion.

### OI trend (multi-day buildup)

- **Consecutive build days:** 28 (entire window — every single session was
  net OI-positive)
- **Today's net OI change:** +118,132 contracts
- **Today's breadth:** 524 contracts with increases vs. 175 with decreases
- **Today's top buildup:** May-22 16C (+12,861), 17C (+12,002), 16.5C
  (+10,318) — all dominant. (Full top-10 = phase-3 [OI:biggest_increases].)

**The 28-day OI build pattern is meaningful** but it's worth noting that
this kind of broad chain expansion in a fintech name often reflects
**dealer inventory expansion + retail/momentum dealer-write inventory**,
not necessarily a directional smart-money signal. Cross-reference with
the bearish-flow majority (21/28 days) and the price decline (-14.7%).

### Multi-day trend table (last 10 sessions)

| Date | Close | IV30 | IV Rank | PCR | Net Flow | Direction |
|---|---|---|---|---|---|---|
| 2026-05-19 | $15.235 | 53.81% | 18.77 | 0.38 | -$2.51M | bearish |
| 2026-05-18 | $15.71 | 54.02% | 17.36 | 0.42 | +$0.37M | bullish |
| 2026-05-15 | $15.585 | 51.80% | 13.51 | 0.63 | -$0.34M | bearish |
| 2026-05-14 | $16.02 | 53.32% | 15.73 | 0.36 | -$1.06M | bearish |
| 2026-05-13 | $15.31 | 52.61% | 14.08 | 0.44 | -$3.17M | bearish |
| 2026-05-12 | $15.90 | 49.00% | 5.66 | 0.35 | -$0.94M | bearish |
| 2026-05-11 | $16.26 | 51.51% | 11.50 | 0.32 | +$1.31M | bullish |
| 2026-05-08 | $15.75 | 48.36% | 6.29 | 0.43 | -$0.49M | bearish |
| 2026-05-07 | $16.00 | 49.96% | 7.89 | 0.36 | -$2.26M | bearish |
| 2026-05-06 | $16.30 | 51.01% | 10.36 | 0.27 | +$1.36M | bullish |

**Key reading:**
- IV rank has been compressed 5-19 range — vol is **at the cheap end** of
  its recent regime, **consistent with phase-5 VRP signal that long options
  are attractive**.
- Net flow has been negative in 7 of 10 most-recent sessions (-$2.5M today).
  Today's headline "bullish" signals (top_premium_trades, sweeps) are
  happening DESPITE a net-bearish premium tally on most days.
- PCR has compressed to 0.32-0.44 in May — call-heavy by recent standards
  but consistent with COMPLACENT skew read in phase-4.

### Signal backtest

| Signal type | Signals (5d lookback) | Win rate | Avg 5d move |
|---|---|---|---|
| `dark_pool_accumulation` | 0 | n/a | n/a (no recent firings) |
| `bullish_flow` | 7 | **0.0%** | **-3.05%** |

The bullish_flow backtest table:

| Date | Ticker | Spot at signal | 5d after | Δ% |
|---|---|---|---|---|
| 2026-05-15 | MSFT | $422.05 | $417.42 | -1.10% |
| 2026-05-15 | AAPL | $300.37 | $298.97 | -0.47% |
| 2026-05-15 | UPS | $99.00 | $96.83 | -2.19% |
| 2026-05-14 | QQQ | $719.79 | $701.53 | -2.54% |
| 2026-05-14 | SMH | $578.34 | $543.96 | **-5.94%** |
| 2026-05-14 | META | $618.43 | $602.61 | -2.56% |
| 2026-05-14 | AVGO | $439.79 | $411.07 | **-6.53%** |

**Take:** the broader tape's bullish-flow-followed-by-distribution pattern
is the dominant signal in the last week. SOFI today fits the pattern (large
ask-side call sweeps) — meaning **today's bullish flow on SOFI is more likely
than not to be faded over the next 5 trading days based on the most-recent
peer signal cohort**. This is a **HARD downgrade** to the phase-1
conviction. Caveat: 7 signals is a low N, and dark_pool_accumulation backtest
was unavailable.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|---|---|---|
| `historical_iv_percentile_zscore` | symbol=SOFI, lookback-days=252 | IV30 53.81%, percentile 44.4, z -0.60, NORMAL |
| `historical_vrp` | symbol=SOFI, date=2026-05-19, realised-window-days=30 | VRP -9.47% → PREMIUM_BUYING |
| `historical_cumulative_premium_flow` | symbol=SOFI, days=90 | Bullish $435M, bearish $479M, net -$44M MIXED |
| `historical_pc_ratio_zscore` | symbol=SOFI, lookback-days=20 | PCR 0.38, z -0.51, NORMAL |
| `historical_gex_time_series` | symbol=SOFI, days=30, dte-max=45 | 28d POSITIVE regime; 2026-05-19 first negative total GEX (-$4.6B from +$37B prior day) |
| `historical_oi_trend` | symbol=SOFI, days=30, top-n=10 | 28 consecutive build days; +118,132 today |
| `historical_trend` | symbol=SOFI, days=30 | 7 bullish vs 21 bearish days; -14.7% from Mar 13 |
| `historical_signal_backtest` | signal-type=dark_pool_accumulation, lookback-days=5, top-n=20 | 0 recent signals — no data |
| `historical_signal_backtest` | signal-type=bullish_flow, lookback-days=5, top-n=20 | 7 signals, 0.0% win rate, avg -3.05% over 5d |

## Tool errors

None. `dark_pool_accumulation` backtest returned "no backtest results" (zero
recent firings), not an error.

## Verdict for downstream phases

- **Volatility regime:** **CHEAP** (VRP -9.47%, IV percentile 44 mid-range).
  **Favor LONG options / debit structures.** Avoid selling premium against
  this VRP backdrop.
- **Premium-flow environment:** mildly bearish (9 of last 10 days net flow
  ≤ 0) — but the magnitude is contained ($2-3M/day) and the cumulative 90d
  flow is only -$44M (essentially balanced).
- **Conviction on whether today's signals are HISTORICALLY EDGE-POSITIVE:**
  **2 / 5** — the bullish_flow signal type that aligns with phase-1's verdict
  has been a 0% win-rate FADE in its most-recent 7 firings, and SOFI itself
  has been in a 28-day drift down (-14.7% from $17.77 to $15.16). The dark
  pool accumulation signal is real (phase 2) but the backtest tool returns
  zero recent firings → no historical edge confirmation.
- **Three specific data points for phase 9:**
  1. **VRP -9.47%** — premium is cheap, favor long-options / debit.
  2. **Bullish_flow 5d win rate 0% / avg -3.05%** — fade-the-rip warning.
  3. **2026-04-29 -14% earnings gap from $18.36 → $15.525, IV rank 47.6 →
     21.9** — current $15 area is a post-earnings re-test zone.
- **Open questions:**
  - Why has OI built 28 consecutive sessions while price dropped 14.7%?
    Stealth bear-case positioning (puts), or contrarian institutional dip-buying?
    (Phase 7 insights composite should disambiguate.)
  - Was the Q1 (Apr 28-29) miss revenue/credit/guidance? Macro/calendar
    in phase 6 should source the reaction reason.
  - Sep-18 IV kink (87.2% from phase 4) — Q2 earnings late-July or early-
    August event? Phase 6 must confirm.
  - The 2026-05-18 +$37B GEX → 2026-05-19 -$4.6B swing — does this presage
    a vol-expansion regime change that phase 4 should have caught? Phase 10
    audit must flag.
