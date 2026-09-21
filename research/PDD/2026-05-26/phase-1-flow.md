# Phase 1 — Options Flow

**Ticker:** PDD
**As-of date:** 2026-05-26
**Generated:** 2026-05-26T20:22:00Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md

## Summary

Today's PDD tape is **two-sided pre-earnings positioning with only a mild bullish
lean, not directional accumulation.** By premium it is call-heavy (calls $18.99M vs
puts $12.27M, 61/39) and P/C volume is 0.44, but bullish vs bearish premium is
near-balanced ($13.23M vs $12.11M, net **+$1.12M**) — the call-heavy *volume* is
dominated by cheap earnings-lottery weeklies, not high-delta directional conviction.
The single **largest dollar print on the whole tape is a downside bet/hedge** — a
$1.945M Jan-2027 110-put — and the most-active contract (5/29 105C, 30,626 contracts,
IV 101.8%) straddles earnings and trades heavily on *both* ask and bid. Carrying
phase-0.5's `BUSY_NAME_NORMAL_DAY` [CTX:unusual_verdict] and the 5/5-session-but-MIXED
sweep persistence, this phase is **mixed/mildly-bullish, low conviction**.

## Key signals

- Whole-tape near-balanced: bullish $13.23M vs bearish $12.11M premium, **net
  +$1.12M**, P/C 0.44 [FLOW:insights_deep_dive]. Call-heavy volume, balanced direction.
- Largest single print = **downside**: 2027-01-15 **110P $1.945M**, 1,000×, delta −0.60,
  IV 0.369 (low — a LEAP hedge/roll, paired same-timestamp with a 9/18 90P $540K)
  [FLOW:top_premium_trades].
- Dominant fresh position = **earnings lottery**: 2026-05-29 **105C** 30,626 contracts
  vs OI 1,338 (vol/OI 22.9), $3.25M, IV **101.8%** — expires 2 days post-print
  [FLOW:unusual_volume]. Traded two-sided (ask $1.90M / bid $1.14M) [FLOW:sweeps].
- Genuine ask-side OTM **call** buying spread across tenors: 97C/100C 5/29, 100C/105C
  6/26, 120C 9/18 ($606K), 130C 9/18 ($375K), 130C 1/15 ($241K) [FLOW:sweeps] — slow
  upside bets beyond the event.
- Sweep persistence: PDD in top sweeps **5/5 sessions, consistency 1.0**,
  $31.08M total — but **dominant_direction = "mixed"** [FLOW:sweep_persistence]. Lots
  of attention, no directional conviction.

## Detailed findings

### Whole-tape aggregate (read top-N against this) — `[FLOW:insights_deep_dive]`

| Field | Value | Read |
|-------|-------|------|
| call_premium | $18,999,334 | calls 61% of premium |
| put_premium | $12,271,307 | |
| bullish_premium | $13,226,742 | near-balanced… |
| bearish_premium | $12,110,864 | …net only **+$1.12M** |
| net_flow | +$1.12M | mild bull tilt |
| put_call_ratio | 0.44 | call-heavy by volume |
| call_volume / put_volume | 90,588 / 39,696 | volume skew driven by cheap weeklies |

The call-heavy *volume* overstates bullishness: the volume concentrates in sub-$1.30
earnings-lottery weeklies (5/29 105C at $1.06). Premium-weighted direction is
essentially flat. **Top-N below is one slice of a balanced tape, not a one-way tape.**

### Sweeps (ask vs bid) — `[FLOW:sweeps]`

- **Two-sided weekly:** 5/29 105C ask $1.90M (17,506×) **and** bid $1.14M (11,244×) →
  net only +6,262 contracts ask-side; heavily intermediated/gamma into the print.
- **Ask-side call buying (bullish):** 120C 9/18 $606K, 100C 6/26 $538K, 105C 6/26 $470K,
  97C 5/29 $450K, 130C 9/18 $375K, 130C 1/15 $241K.
- **Put activity (bearish/hedge):** 95P 6/18 ask $642K (bought), 95P 6/18 no_side $756K,
  90P 7/17 mid $401K, 90P 9/18 ask $339K, 110P 1/15 $1.945M no_side.
- **Bid-side (selling/closing):** 104C 6/05 bid $1.0M, 100C 8/21 bid $651K, 85C 9/18
  bid $516K (deep-ITM, possible stock replacement).

### New positioning (unusual vol / vol-OI) — `[FLOW:unusual_volume]`

- 5/29 105C: 30,626 vol / OI 1,338 (22.9×), $3.25M, IV 101.8% — the position of the day.
- 6/05 104C: 5,956 / OI 33 (180×), $1.15M.
- 6/26 100C (18×), 6/18 107C (12.9×), 9/18 85C (12×) — call-side dominates fresh OI.
- Put unusual-vol is **cheap OTM crash protection**: 5/29 70P (5,156×, $15K), 80P, 83P,
  85P; plus 6/18 96P/97P near-money. Lottery-priced, low dollar weight.

### Largest premium prints — `[FLOW:top_premium_trades]`

| Time (UTC) | Contract | Premium | Side | Δ | Note |
|-----------|----------|---------|------|---|------|
| 15:16:03 | 2027-01-15 110P | $1.945M | no_side | −0.60 | LEAP put, IV 0.37; paired w/ 90P 9/18 |
| 15:16:03 | 2026-09-18 90P | $540K | no_side | −0.32 | paired downside |
| 19:00:06 | 2026-09-18 85C | $512K | bid | +0.74 | deep-ITM call (stock replacement?) |
| 19:16:16 | 2026-06-18 100C | $454K | no_side | +0.44 | **same-stamp as 95P below → strangle/RR** |
| 19:16:16 | 2026-06-18 95P | $415K | no_side | −0.39 | paired w/ 100C 6/18 |
| 15:55:18 | 2026-06-05 104C | $147K×4 | bid | +0.30 | repeated OTM call |

Several top prints are **same-timestamp multi-leg structures** (110P+90P; 100C+95P
6/18 ≈ a strangle/risk-reversal), i.e. volatility/combo trades, not clean directional
bets — reinforcing the two-sided read.

### IV outliers + Greeks — `[FLOW:iv_outliers]` / `[FLOW:greek_screener]`

- **Every IV outlier is the 2026-05-29 (post-earnings) weekly**, IV **100%–189%** (130C
  189%, 70P 151%, 120C 140%). This tenor is the pure earnings-event vol and faces
  **severe IV crush** after the 5/27 print.
- Greek screener top dollar = the 110P LEAP (vega 0.30 — vol-sensitive) and the 5/29
  105C (vega 0.027, theta −0.49 — pure gamma/event lottery, near-zero vega protection).

### Market-wide cross-checks

- `smart_money_flow` (bullish & bearish, min_vol 500): **PDD appears in neither
  top-20** [FLOW:smart_money_flow]. No PDD contract shows an extreme ask/bid imbalance
  worth ranking market-wide (lists led by SPY/NVDA/VIX/IWM/F/WULF). → no smart-money
  one-way signal on this date.
- `sweep_ratio` (≥0.3, min_vol 500): **PDD absent** from top-25 [FLOW:sweep_ratio] —
  its sweeps are not among the most aggressive single-sweep contracts (list led by QQQ
  puts). Consistent with mixed/intermediated flow.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `options_flow_sweeps` | symbol=PDD, min_prem=100k, top25 | Two-sided 105C; ask OTM calls 97-130; puts 90-95-110 |
| `options_flow_top_premium_trades` | symbol=PDD, top25 | #1 = 110P LEAP $1.945M; several multi-leg combos |
| `options_flow_unusual_volume` | symbol=PDD, min_vol_oi=3, top25 | 5/29 105C 30.6k vol/OI 22.9; call-dominated |
| `options_flow_iv_outliers` | symbol=PDD, top15 | All 5/29; IV 100-189% (event vol) |
| `options_flow_greek_screener` | symbol=PDD, top15, by premium | 110P (vega 0.30) + 5/29 105C (theta −0.49) lead |
| `hot_chains_sweep_persistence` | symbol=PDD, days5, top20 | 5/5 sessions, consistency 1.0, **mixed**, $31.08M |
| `hot_chains_smart_money_flow` | dir=bullish & bearish, min_vol500 | PDD in neither top-20 |
| `hot_chains_sweep_ratio` | top25, min_vol500, ratio≥0.3 | PDD absent from top-25 |
| `insights_deep_dive` | symbol=PDD (whole-tape) | net_flow +$1.12M, P/C 0.44, calls 61% prem |

## Tool errors

None.

## Verdict for downstream phases

- **Net bias:** MIXED / mildly bullish. Call-heavy volume + ask-side OTM call buying
  give a slight upside lean; but premium-weighted direction is flat, the biggest single
  print is a put, and 5-day sweep direction is "mixed".
- **Conviction:** **2/5.** Capped by phase-0.5 `BUSY_NAME_NORMAL_DAY` → phases 1–2
  confluence ceiling `+` (`rubrics/confluence-scoring.md`). This is earnings vol/lottery
  positioning, not accumulation.
- **Three datapoints later phases must remember:**
  1. The flow is an **earnings event book**: dominant contract is the 5/29 105C at IV
     101.8% (expires 2 days post-print) — long premium will be crushed; phase-9 must
     not recommend naked long options through the event.
  2. **Largest dollar conviction is downside/hedge** (110P LEAP $1.945M) — the upside is
     expressed in cheap, low-delta OTM calls. Net directional dollars are roughly flat.
  3. Spot intraday $97.2–$97.8, **close $96.58**; the action clusters 95P–105C, i.e.
     the market is pricing a move *within* the ±5.69% implied band [CTX:implied_move_pct].
- **Open questions:** Is dark pool accumulating under the print (phase-2), or is the
  underlying being distributed? Does dealer positioning (phase-3/4) pin spot near
  100/105 or leave it free to move on the print?
