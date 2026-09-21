# Phase 1 — Options Flow

**Ticker:** GFS
**As-of date:** 2026-05-27
**Generated:** 2026-05-28T00:00:00Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md

## Summary

The tape is **near-balanced with a slight call-writing / profit-taking lean** — not
directional accumulation. Whole-tape directional premium is **$4.5M bullish vs $4.8M
bearish** (net ≈ −$0.3M), and the ex-0/1DTE aggressor split shows **more call
selling than buying** (5,885 contracts hit the bid vs 4,171 lifted the ask;
$3.92M bid-call vs $3.73M ask-call). Net **delta-notional footprint is negligible
(±$15–17M)** — there is no real directional weight behind the day's top-5%-of-universe
premium. 5-day sweep persistence flags GFS in the top sweep cohort all 5 sessions but
with `dominant_direction = "mixed"`. This **confirms phase-0.5's BUSY_NAME_NORMAL_DAY
/ post-parabolic churn** read; conviction here is capped at `+`.

## Key signals

- Whole-tape: **bullish $4.5M vs bearish $4.8M premium, net_flow ≈ −$0.3M**, P/C
  0.33, call_prem $8.37M vs put_prem $1.93M `[FLOW:insights_deep_dive]`.
- Ex-0/1DTE aggressor: **call SELLING > call BUYING** — bid-calls 5,885 ct / $3.92M
  vs ask-calls 4,171 ct / $3.73M; delta-notional +$0.017bn vs +$0.015bn (a wash)
  `[FLOW:aggressor_ex0dte DUCKDB]`.
- Largest unusual-volume print: **$120 Jul call, vol 1,308 / OI 150 (vol/OI 8.72),
  opening — but traded on the BID** (1,283-lot bid sweep $256k) = **sold-to-open
  far-OTM calls** (price $81), an income/capped-upside tell `[FLOW:unusual_volume]`,
  `[FLOW:sweeps]`.
- Sweep persistence 5/5 sessions, consistency 1.0, **direction "mixed"**, total
  sweep premium $12.5M `[FLOW:sweep_persistence]`.
- Net delta-notional ≈ +$0.012bn total (calls) net of negligible put delta — **no
  directional footprint** `[FLOW:delta_notional DUCKDB]`.

## Detailed findings

### Whole-tape aggregate (read the top-N against this) `[FLOW:insights_deep_dive]`

| Metric | Value |
|--------|------:|
| bullish_premium | $4,500,876 |
| bearish_premium | $4,798,574 |
| net_flow | ≈ −$297,698 (slight bear) |
| call_premium | $8,370,861 |
| put_premium | $1,934,809 |
| call_volume / put_volume | 10,958 / 3,666 |
| put_call_ratio | 0.33 |

Call premium dwarfs put premium, but that is **gross** — the aggressor split below
shows roughly half those calls were *sold*, so the high call_premium is two-way churn,
not one-sided buying.

### Ex-0/1DTE aggressor + delta-notional `[FLOW:aggressor_ex0dte DUCKDB]`

| type | side | trades | contracts | prem $M | delta-notional $bn |
|------|------|------:|----------:|--------:|-------------------:|
| call | ask (buy) | 1,006 | 4,171 | 3.73 | +0.015 |
| call | bid (sell) | 1,148 | 5,885 | **3.92** | +0.017 |
| call | mid | 281 | 902 | 0.72 | +0.003 |
| put | ask (buy) | 320 | 1,433 | 0.88 | −0.003 |
| put | bid (sell) | 308 | 1,795 | 0.77 | −0.003 |
| put | mid | 138 | 438 | 0.28 | −0.001 |

Bullish (ask-call + bid-put) **$4.5M** vs bearish (bid-call + ask-put) **$4.8M** —
matches the screener block to the dollar. **Call selling marginally dominates.**

### DTE distribution `[FLOW:aggressor_ex0dte DUCKDB]`

| bucket | call $M | put $M |
|--------|--------:|-------:|
| 8–45DTE | 2.36 | 0.70 |
| 46–180DTE | 3.15 | 0.70 |
| LEAP (>180DTE) | 2.86 | 0.53 |

Premium is spread evenly across near, mid, and LEAP tenors — no concentration that
would mark a single dated catalyst bet. LEAP calls $2.86M is the one slow-money
positive, but it is part of the same two-way churn (LEAP calls also showed bid-side
selling above).

### Sweeps (ask vs bid) `[FLOW:sweeps]`

- **Ask-side (aggressive buy):** 12 sweeps, ~$2.32M, **all calls** except 2 small
  puts. Top: $100 LEAP-2028 ($378k), $85 Jun ($363k), $85 Jul ($306k), $80
  LEAP-2027 ($283k), $90 Jun ($247k).
- **Bid-side (aggressive sell):** 12 sweeps, ~$2.30M, **all calls**. Top: $80 Jun
  ($374k), $90 Jun ($286k), **$120 Jul ($256k, 1,283 lots)**, $90 Oct ($251k),
  $100 Oct ($201k).
- Symmetric call sweeping on both sides → churn, not a one-way campaign.

### Largest premium prints (top-25 split) `[FLOW:top_premium_trades]`

ask-calls $1,140,281 · bid-calls $950,154 · ask-puts $194,920 · bid-puts $0.
Bullish (ask-call + bid-put) $1.14M vs bearish (bid-call + ask-put) $1.145M — a
dead heat among the largest prints too. Notable single prints: $80 Jun call $269k
(bid, d0.58), $90 Oct call $237k (bid), $100 LEAP-2028 call $217k (ask, d0.60).

### IV outliers + Greeks `[FLOW:iv_outliers]`, `[FLOW:greek_screener]`

- IV-outliers: 1 row — $120 Jun call, avg_iv 1.05 (far-OTM lottery line).
- Greek screener (by premium) is dominated by 0.50–0.64 delta calls in the
  $80–$100 strikes — at-the-money exposure consistent with the spot churn, not deep
  OTM directional bets.

## Tool calls (audit trail)

| Command | Result |
|---------|--------|
| `uw options-flow sweeps --side ask … --date 2026-05-27` | 12 sweeps, ~$2.32M, ~all calls |
| `uw options-flow sweeps --side bid … --date 2026-05-27` | 12 sweeps, ~$2.30M, all calls |
| `uw options-flow unusual-volume --min-vol-oi-ratio 3` | 1 row: $120 Jul call vol/OI 8.72 (sold) |
| `uw options-flow top-premium-trades --top-n 25` | 25 prints; ask-call $1.14M ≈ bid-call $0.95M+ask-put $0.19M |
| `uw options-flow iv-outliers --top-n 15` | 1 row ($120 Jun, avg_iv 1.05) |
| `uw options-flow greek-screener --sort-by premium` | ATM 0.5–0.64Δ calls dominate |
| `uw hot-chains smart-money-flow --direction bullish/bearish` | **no GFS rows** (not a directional leader) |
| `uw hot-chains sweep-persistence --days 5 --symbol GFS` | 5/5 sessions, consistency 1.0, **mixed**, $12.5M |
| `uw hot-chains sweep-ratio` | **GFS outside top-50** |
| `uw insights deep-dive --symbol GFS --date 2026-05-27` | whole-tape aggregate (above) |
| DuckDB §A aggressor+delta-notional (ex-0/1DTE) | call-sell > call-buy; net delta ≈ 0 |

## Tool errors

- `uw hot-chains sweep-persistence … --date 2026-05-27` → `Error: unknown flag:
  --date`. Re-ran **without** `--date` (trailing tool anchors to latest; latest ==
  as-of 2026-05-27, so the read is valid for this run). Flagged per memory
  [[uw-cli-mcp-parity]] that trailing tools are not as-of reproducible in general.
- `uw options-flow iv-outliers` returned `implied_volatility/iv/premium/volume` as
  null (only `avg_iv` populated) — single far-OTM row, low information.

## Verdict for downstream

- **Net bias from this phase:** **MIXED, slight bearish lean** (call-writing into
  the spike). Not bullish accumulation.
- **Conviction:** **2/5** — high activity, no directional edge; delta-notional flat.
- **Three things later phases must remember:**
  1. **Call selling > call buying** ex-0/1DTE (5,885 vs 4,171 contracts). The
     headline "$8.4M call premium" is two-way churn, ~half of it sold.
  2. **The opening $120 Jul call block was SOLD** (call writing far above a $81
     spot) — a ceiling vote, not a moonshot bet.
  3. **No net delta-notional** (±$15M) and **mixed** 5-day sweep direction →
     phase-2/dark-pool must carry the directional weight if any exists; flow alone
     does not.
- **Open questions:** Is the $202.7M dark pool (phase-0.5) accumulation or
  distribution into the parabola? (phase-2). Does dealer positioning/GEX (phase-4)
  explain the call writing — are dealers long gamma capping the move?
