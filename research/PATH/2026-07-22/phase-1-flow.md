# Phase 1 — Options Flow

**Ticker:** PATH · **As-of:** 2026-07-22 · **Underlying:** $10.53 · **Generated:** 2026-07-22
**Upstream:** phase-0.5-context.md `[CTX:]` (unusual_verdict = GENUINELY_UNUSUAL, bearish tilt; net-dir 1.4 pctile; iv_rank 45.6; implied_move 4.70%)

## Summary

PATH's tape is **genuinely unusual but internally conflicted.** The whole-tape
aggregate is **net-bearish** — bullish premium $1.66M vs bearish $3.26M (derived
net_flow **−$1.60M**), with gross call premium ($4.16M) net-*sold* — yet
`sweep-persistence` shows a **5-session bullish sweep campaign** (consistency 1.0,
$6.71M, top-of-list all 5 days). The single largest flow today is **$893k of Dec-18
$12 calls hit on the BID** (5,546 contracts, delta ~0.51) — call writing or
long-call profit-taking — sitting on top of **$276k of near-ATM $10.5 puts bought**
(7/31) and a wall of cheap 7/24 OTM call lottos priced at **100–176% IV vs a 30-day
IV of 67.5%**, i.e. the market is pricing a **near-term catalyst around 2026-07-24**
(UW's stated 2026-09-03 earnings date looks stale — flag for phase 6/7b).

## Key signals

- **5-day bullish sweep campaign, consistency 1.0** — PATH top of the sweep-persistence list all 5 sessions, $6.71M total, dominant_direction bullish `[FLOW:sweep_persistence]`. The structural undercurrent.
- **Net-bearish aggregate today** — bull $1.66M < bear $3.26M, net_flow −$1.60M; net-directional premium in the 1.4 universe percentile `[FLOW:insights_deep_dive]` (carried from `[CTX:]`).
- **Largest print = call SELLING** — $893k Dec-18 $12 calls on the bid (5,546 ct @ $1.66, delta 0.51); top-25 prints are $1.07M bid-side vs $0.27M ask-side `[FLOW:top_premium_trades]` `[FLOW:sweeps]`.
- **Biggest NEW position = near-ATM puts** — $10.5 put 7/31 opened vol 7,206 / OI 329 (vol/OI 21.9), $276k, IV 72% `[FLOW:unusual_volume]`.
- **Near-term event kink** — 7/24 front-expiry IV 100–176% (call 14 7/24 = 176%, call 11.5 7/24 = 104% on 4,272 vol) vs 30-day IV 67.5% `[FLOW:iv_outliers]`.
- **No PATH rows in market-wide smart-money-flow top-10** (bull or bear) — "no smart-money flow detected for PATH on this date" (thresholds NOT loosened, per skill rule).

## Detailed findings

### Whole-tape aggregate `[FLOW:insights_deep_dive]`

| Metric | Value |
|---|---|
| call_premium / put_premium | $4.16M / $1.29M |
| bullish_premium / bearish_premium | $1.66M / $3.26M |
| **derived net_flow (bull − bear)** | **−$1.60M (net bearish)** |
| call_volume / put_volume | 67,418 / 28,230 |
| put_call_ratio | 0.419 |
| iv_rank / iv30d | 45.6 / 67.5% |
| implied_move_perc | 4.70% |
| total_open_interest | 663,367 |

Read: **gross call premium dominates but is net-SOLD** — the aggressor split is
bearish. The top-N below is read against this, not in place of it. Because
`[CTX:] unusual_verdict = GENUINELY_UNUSUAL` (not BUSY_NAME_NORMAL_DAY), the phase-1/2
confluence is **not** magnitude-capped — the direction is the real signal.

### Sweeps (ask vs bid) `[FLOW:sweeps]`

Ask-side (aggressive buyers), total ~$0.38M:
| side | type | strike | expiry | prem | size | avg px |
|---|---|---|---|---|---|---|
| ask | put | 10.5 | 2026-07-31 | $144,878 | 3,770 | 0.37 |
| ask | call | 11 | 2026-07-24 | $124,274 | 7,512 | 0.17 |
| ask | call | 13 | 2026-09-18 | $112,429 | 1,708 | 0.68 |

Bid-side (aggressive sellers / hit-bid), total ~$1.15M:
| side | type | strike | expiry | prem | size | avg px |
|---|---|---|---|---|---|---|
| **bid** | **call** | **12** | **2026-12-18** | **$893,213** | **5,546** | **1.66** |
| bid | call | 17 | 2027-01-15 | $131,980 | 1,685 | 0.79 |
| bid | put | 10.5 | 2026-07-31 | $126,957 | 3,339 | 0.38 |

The Dec-$12 call sale dwarfs everything. Note both sides of the 10.5 put (7/31)
traded — net a modest bid/ask wash on that strike; the *unusual-volume* opener below
shows it opened net long puts on the day.

### New positioning (unusual vol, vol/OI ≥ 3) `[FLOW:unusual_volume]`

| type | strike | expiry | vol | OI | vol/OI | prem | IV |
|---|---|---|---|---|---|---|---|
| put | 10.5 | 2026-07-31 | 7,206 | 329 | 21.9 | **$275,610** | 72% |
| call | 11 | 2026-07-24 | 12,086 | 1,174 | 10.3 | $211,005 | 99% |
| call | 11.5 | 2026-07-24 | 5,701 | 378 | 15.1 | $67,499 | 102% |
| call | 11.5 | 2026-08-07 | 1,088 | 53 | 20.5 | $53,306 | 74% |
| call | 10.5 | 2026-07-31 | 903 | 83 | 10.9 | $47,009 | 73% |
| put | 10 | 2026-07-31 | 1,147 | 191 | 6.0 | $25,075 | 70% |
| put | 9.5 | 2026-08-21 | 501 | 1 | 501 | $17,243 | 67% |
| put | 8.5 | 2026-08-28 | 416 | 3 | 138.7 | $6,680 | 69% |

The **single biggest new-money commitment is near-ATM downside** ($276k of 10.5 puts,
9 DTE). Call openers are mostly **cheap 7/24 lottos** (11/11.5 strikes at ~$0.17–0.55,
99–102% IV) — event speculation, low per-contract conviction, small premium. A
scattering of cheap OTM crash puts (9.5, 8.5) rounds out the downside tail.

### Largest premium prints `[FLOW:top_premium_trades]`

Top-25 by premium: **calls $1.36M vs puts $0.07M**, but by aggressor **bid $1.07M (13
prints) vs ask $0.27M (9) / mid $0.09M (3)**. The five largest are the Dec-$12 call
decomposition ($324k/$161k/$161k/$159k/$70k, all bid) executed ~19:08Z. A $53k Jan-2028
$5 LEAP call (delta 0.91, mid) is a small deep-ITM stock-replacement bullish tag.

### IV outliers + Greeks `[FLOW:iv_outliers]` `[FLOW:greek_screener]`

Front-expiry **2026-07-24** is a clear term-structure event kink: call 14 = 176% IV,
call 13.5 = 157%, call 13 = 134% (vol 1,698), call 11.5 = 104% (vol 4,272), put 12 =
126%, put 11.5 = 107% — all vs 30-day IV 67.5%. Greeks confirm the Dec-$12 call
(delta 0.51, gamma 0.076, vega 0.027) as the premium center of gravity, being sold.

## Tool calls (audit)

| Datapoint | Command | jq path |
|---|---|---|
| whole-tape aggregate | `uw insights deep-dive --symbol PATH --date 2026-07-22 --json` | `.uw_screener.{call_premium,put_premium,bullish_premium,bearish_premium,put_call_ratio,call_volume,put_volume,iv_rank,implied_move_perc}` |
| ask sweeps | `uw options-flow sweeps --symbol PATH --side ask --min-premium 100000 --top-n 25 --date 2026-07-22 --json` | `.results[].{side,option_type,strike,expiry,total_premium,total_size,avg_price}` |
| bid sweeps | `… --side bid …` | same |
| new positioning | `uw options-flow unusual-volume --symbol PATH --min-vol-oi-ratio 3 --top-n 25 --date 2026-07-22 --json` | `.results[].{option_type,strike,expiry,total_volume,open_interest,vol_oi_ratio,total_premium,avg_iv}` |
| premium prints | `uw options-flow top-premium-trades --symbol PATH --top-n 25 --date 2026-07-22 --json` | `.results[].{option_type,strike,expiry,premium,side,delta,underlying_price}` |
| IV outliers | `uw options-flow iv-outliers --symbol PATH --top-n 15 --date 2026-07-22 --json` | `.results[].{strike,expiry,avg_iv,max_iv}` |
| greeks | `uw options-flow greek-screener --symbol PATH --top-n 15 --sort-by premium --date 2026-07-22 --json` | `.results[].{delta,gamma,vega,premium}` |
| smart-money (mkt-wide) | `uw hot-chains smart-money-flow --direction bullish\|bearish --top-n 10 --min-volume 500 --date 2026-07-22 --json` | filter `.results[] .underlying_symbol=="PATH"` → none |
| sweep persistence | `uw hot-chains sweep-persistence --days 5 --top-n 20 --symbol PATH --json` (no `--date`; anchors to latest = 2026-07-22) | `.[]|select(.ticker=="PATH")` |

## Tool errors

- `uw hot-chains sweep-persistence … --date 2026-07-22` → `Error: unknown flag: --date`. Re-ran WITHOUT `--date` (trailing tool anchors to the latest available date, which equals the as-of 2026-07-22). Result used.

## Verdict for downstream

- **Net bias: MIXED — today's aggressor is net-BEARISH, but it overlays a live 5-day BULLISH sweep campaign; most coherent read is profit-taking / hedging into a near-term event, not fresh bearish initiation.**
- **Conviction: 2/5** on the bearish today-read (mechanically driven by one $893k call sale + near-ATM put hedges; conflicts with the persistent bullish sweeps). Higher-confidence fact is the **near-term catalyst ~7/24**.
- **Three datapoints later phases MUST remember:**
  1. **5-day bullish sweep persistence: $6.71M, consistency 1.0, dominant bullish** — structural undercurrent that argues against reading today as a clean short.
  2. **Near-term catalyst ~2026-07-24** — front-expiry IV 100–176% vs 30-day 67.5%; UW `next_earnings_date 2026-09-03` is almost certainly STALE. Resolve the real event date in phase 6/7b before sizing anything with a >2-day horizon.
  3. **Today's dominant flow = $893k Dec-$12 calls SOLD + $276k near-ATM 10.5 puts BOUGHT** — net-bearish aggressor at spot $10.53; whether the Dec calls are being CLOSED (from the campaign) or WRITTEN is an OI question for phase 3.
- **Open questions:**
  - Is dark pool confirming accumulation or distribution under this options tape? (phase 2)
  - What is the real 7/24 catalyst — earnings, analyst/investor day, or lockup/index event? (phase 6/7b)
  - Are the Dec-$12 calls being closed (bullish-campaign unwind) or freshly overwritten? (phase 3 OI Δ)
