# Phase 1 — Options Flow

**Ticker:** SNOW
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T15:20:00Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md

## Summary

SNOW's tape is **gross call-heavy but net directionally flat** — and *that gap is
the signal.* Whole-tape call premium ($34.6M) dwarfs put premium ($7.6M), but the
aggressor classification is balanced-to-slightly-bearish (bullish $19.0M vs bearish
$19.9M premium, net_flow −$0.9M) [FLOW:insights_deep_dive]. The DuckDB aggressor cut
stripped of 0DTE confirms it: calls are **bought and sold almost equally** (ask
$13.62M / 12,349 ct vs bid $12.61M / 11,432 ct), and the **signed delta-notional in
the 2–7DTE earnings week is net BEARISH (−$15M)** [FLOW:delta_notional DUCKDB]. This
is two-sided earnings positioning / call-overwriting, **not** one-directional
accumulation. Persistent — SNOW is in the top sweep cohort 5/5 sessions — but
`dominant_direction = mixed` over $89.7M of 5-day sweep premium
[FLOW:sweep_persistence]. Honoring phase-0.5's `BUSY_NAME_NORMAL_DAY`, this phase's
directional conviction is capped at `+`.

## Key signals

- **Gross/net divergence:** call premium $34.6M vs put $7.6M (P/C vol 0.37), yet
  bullish−bearish premium = **−$0.9M** [FLOW:insights_deep_dive]. Heavy call
  *volume*, no net long-delta.
- **Ex-0DTE delta-notional ≈ flat**, with the **earnings week (2–7DTE) net bearish
  −$15M** and 8–45DTE only +$11M [FLOW:delta_notional DUCKDB] — the upside calls are
  being overwritten/sold against.
- **Single largest print is bearish:** 2027-06-17 **155P, $1.07M, ask-side**, delta
  −0.31, IV 0.597 [FLOW:top_premium_trades] — a long-dated protective/short bet, the
  biggest dollar conviction trade on the tape.
- **Sweeps are two-sided:** biggest call sweep is **bid-side** 5/29 160C ($1.60M,
  call-selling) vs ask-side 5/29 175C ($1.20M, call-buying) [FLOW:sweeps] — no clean
  aggressor.
- **Persistence without direction:** 5/5 sessions in top sweeps, consistency 1.0,
  $89.7M, `dominant_direction = mixed` [FLOW:sweep_persistence].

## Detailed findings

### Whole-tape aggregate (read the top-N against this)

From `insights_deep_dive.uw_screener` [FLOW:insights_deep_dive]:
- `call_premium` $34,572,339 · `put_premium` $7,624,904 (gross call-skew, P/C vol 0.37)
- `bullish_premium` $19,007,739 · `bearish_premium` $19,910,145 → **net_flow ≈ −$0.9M**
- `call_volume` 42,680 · `put_volume` 15,765
- The gross call-skew says "calls are where the action is"; the near-equal
  bullish/bearish premium says "but it's two-sided." The top-N prints below are the
  tip of the iceberg — do not read them as the whole tape.

### Aggressor & delta-notional, ex-0DTE (DuckDB §A)

| type | side | trades | contracts | prem $M | |
|------|------|--------|-----------|---------|---|
| call | ask | 4,266 | 12,349 | 13.62 | buying |
| call | bid | 3,357 | 11,432 | 12.61 | selling |
| put | ask | 1,460 | 5,257 | 4.01 | buying |
| put | bid | 1,854 | 5,895 | 3.05 | selling |

Calls net only +917 contracts bought-on-ask; puts net bought on ask. Signed
delta-notional by tenor [FLOW:delta_notional DUCKDB]:

| DTE bucket | signed Δ-notional $bn | read |
|------------|----------------------|------|
| 0–1DTE | +0.005 | pin noise |
| **2–7DTE (earnings wk)** | **−0.015** | **net bearish into print** |
| 8–45DTE | +0.011 | mild bullish |
| 46–180DTE | +0.004 | mild bullish |
| LEAP | −0.001 | flat (the 2027 155P) |
| **Total ex-0DTE** | **≈ −0.001 (flat)** | no net directional conviction |

### Premium by DTE bucket (full tape)

0-1DTE call $5.79M / put $0.13M (pure 0DTE call churn) · 2-7DTE call $10.73M / put
$1.83M · 8-45DTE call $9.26M / put $2.25M · 46-180DTE call $4.89M / put $1.33M ·
LEAP call $3.90M / put $2.09M. Call premium concentrates in the 2–7DTE (earnings)
and 8–45DTE tenors — but per the delta-notional table that 2–7DTE call premium is
net *sold*, not accumulated.

### Sweeps (two-sided)

Largest aggregated sweeps [FLOW:sweeps]: 5/29 160C **bid** $1.60M (918) · 5/29 175C
**ask** $1.20M (1,165) · 2027-06-17 155P **ask** $1.07M (340) · 5/29 170C **bid**
$1.02M (856) · 6/18 200C **ask** $0.97M (1,476) · 6/18 170P **bid** $0.82M · 5/22
160C bid $0.78M (0DTE) · 6/26 125C bid $0.74M (deep-ITM, Δ0.91 — stock-replacement/
buy-write). Upside-call buying (5/29 175C/180C/182.5C/190C, 6/18 180C/200C ask) is
real but matched by call-selling (5/29 160C/170C bid) and put-buying.

### New positioning (vol/OI ≥ 3)

[FLOW:unusual_volume] 6/26 125C vol/OI 250 (the deep-ITM print, 1 OI) · 5/29 182.5C
vol/OI 8.9 ($0.93M, 998 trades — genuine fresh OTM earnings-call build) · 6/18 205C
vol/OI 11.6 · 2027-06-17 155P vol/OI 6.2 (the bearish LEAP put) · 5/29 150P vol/OI
3.1 ($0.35M put build) · 2027-03 135P vol/OI 3.9. Fresh OTM upside calls (182.5C,
205C 5/29–6/18) **and** fresh downside puts (155P 2027, 150P 5/29, 135P 2027) —
both tails being bought for the event.

### IV outliers & Greeks

[FLOW:iv_outliers] dominated by 5/22 **0DTE** strikes with max_iv 7–183 (expiry-day
IV blow-up artifacts — discard as pin noise). Greek screener [FLOW:greek_screener]
top by premium = the 2027 155P (vega 0.63, the only large long-vega bearish print)
and the 6/26 125C (Δ0.91 deep-ITM). No high-gamma directional cluster beyond 0DTE.

### Smart-money & sweep-ratio leaderboards

SNOW appears in **neither** the market-wide bullish nor bearish
`smart_money_flow` top-20 (those are SMH/GLD/SPY/NVDA/IGV index & mega-cap
contracts) — **no dominant single-contract smart-money imbalance for SNOW on this
date** [FLOW:smart_money_flow]. SNOW also outside the `sweep_ratio` top-15 (micro-cap
high-ratio names) [FLOW:sweep_ratio].

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `insights_deep_dive` | symbol=SNOW, date=2026-05-22 | whole-tape: call $34.6M/put $7.6M, net_flow −$0.9M |
| `options_flow_sweeps` | symbol=SNOW, min_premium=100k, top_n=25 | two-sided; biggest = bid 5/29 160C $1.6M |
| `options_flow_unusual_volume` | symbol=SNOW, min_vol_oi=3, top_n=25 | fresh OTM calls (182.5C/205C) AND puts (155P/150P) |
| `options_flow_top_premium_trades` | symbol=SNOW, top_n=25 | #1 = 2027 155P ask $1.07M (bearish) |
| `options_flow_iv_outliers` | symbol=SNOW, top_n=15 | all 0DTE 5/22 artifacts — discarded |
| `options_flow_greek_screener` | symbol=SNOW, top_n=15, sort=premium | 155P (long vega) + 125C deep-ITM lead |
| `hot_chains_smart_money_flow` | dir=bullish/bearish, min_vol=500 | SNOW absent both lists |
| `hot_chains_sweep_persistence` | days=5, symbol=SNOW | 5/5 sessions, consistency 1.0, $89.7M, **mixed** |
| `hot_chains_sweep_ratio` | min_vol=500, min_ratio=0.3 | SNOW absent (micro-caps dominate) |
| DuckDB §A | aggressor ex-0DTE + delta-notional by DTE | net Δ-notional ≈ flat; 2–7DTE net bearish |

## Tool errors

(none — `yahoo_fundamentals` returned HTTP 401 inside `insights_deep_dive`, an
optional sub-block; the `uw_screener` block used here is intact. Noted for phase-7b
to source fundamentals from Finnhub/WebSearch instead.)

## Verdict for downstream phases

- **Net bias from this phase:** **MIXED** (gross call-skew, net delta-flat; earnings
  week net slightly bearish on signed delta).
- **Conviction:** **2/5** (capped at `+` per phase-0.5 `BUSY_NAME_NORMAL_DAY`; the
  flow is persistent but two-sided — no directional edge to lean on).
- **Three things later phases must remember:**
  1. **Do not read $34.6M call premium as bullish.** Ex-0DTE, calls are sold ≈ as
     much as bought; net delta-notional ≈ flat and the earnings-week tenor is net
     bearish −$15M [FLOW:delta_notional DUCKDB]. This is overwriting/two-sided
     event positioning.
  2. **Both tails are being bought for 5/27 earnings** — fresh OTM calls (5/29
     182.5C, 6/18 205C) *and* fresh puts (2027 155P $1.07M, 5/29 150P). The market
     is positioning for a *move*, not a direction.
  3. **The single biggest-conviction print is bearish** (2027 155P, $1.07M ask) —
     phase-2/3 should check whether dark-pool / OI corroborates any downside lean.
- **Open questions:**
  - Is the dark pool accumulating or distributing at $171–172? → phase-2.
  - Does OI confirm the 5/29 OTM call build is *opening* (new longs) vs the call
    selling closing? → phase-3.
  - Where is dealer gamma pinning into the event, and what's the real earnings
    expected move? → phase-4.
