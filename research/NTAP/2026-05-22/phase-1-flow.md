# Phase 1 — Options Flow

**Ticker:** NTAP
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T00:00:00Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md

## Summary

NTAP's tape is **call-heavy by volume but net-flat-to-slightly-bearish by
aggressor footprint** — the opposite of the headline. The whole-tape aggregate is
balanced (`bullish_premium $4.95M ≈ bearish_premium $5.00M`, net_flow −$48.5K), and
the §A aggressor split (ex-0DTE) shows **net call SELLING (−$0.356M) and net put
SELLING (−$0.308M)**, net delta-notional ≈ −$4M. The single largest event of the
day is a **145C 6/18 sold on the bid — $2.86M / 4,851 contracts** (one print
$1.80M / 2,998 ctr at 16:17). This is **premium harvesting into IV rank 100 ahead
of the 2026-05-28 earnings**, not directional accumulation — exactly the
event/vol-not-direction read phase-0.5 flagged (`[CTX] net-dir bottom decile`).

## Key signals

- **Largest print is a call SALE, not a buy:** 145C 6/18 **bid-side** $2.86M /
  4,851 ctr / 189 trades; biggest single ticket $1.80M bid at 16:17 [FLOW:sweeps], [FLOW:top_premium_trades]
- **Whole-tape net is flat:** call prem $9.35M vs put prem $1.49M, but
  bullish $4.95M ≈ bearish $5.00M, net_flow −$48.5K [FLOW:insights_deep_dive]
- **Aggressor footprint net-negative:** net call buy −$0.356M, net put buy
  −$0.308M, net delta-notional ≈ −$4M (ex-0DTE) [FLOW:aggressor_ex0dte DUCKDB]
- **Headline 551× vol/OI is a far-OTM lotto:** 185C 6/18 (strike +34% vs spot),
  avg price ~$0.86, $284K — cheap convexity punt, not conviction [FLOW:unusual_volume]
- **Small genuine bull tells:** LEAP calls bought on ask — 180C 1/15/27 $293K,
  160C 1/15/27 $159K; $1.51M total LEAP calls [FLOW:sweeps], [FLOW:delta_notional DUCKDB]
- **Two-sided new money:** fresh 130P 6/18 (492× vol/OI, $735K) + 135P 6/18
  alongside the call lottos — straddle/strangle-shaped, not one-way [FLOW:unusual_volume]

## Detailed findings

### Whole-tape aggregate (read the top-N against this) — `[FLOW:insights_deep_dive]`

| Field | Value | Read |
|-------|-------|------|
| call_premium | $9,346,981 | Call-heavy by gross premium |
| put_premium | $1,488,717 | — |
| bullish_premium | $4,950,598 | ≈ bearish |
| bearish_premium | $4,999,135 | **slightly > bullish** |
| net_flow | **−$48,537** | **flat / marginally bearish** |
| put_call_ratio | 0.178 | call-heavy by volume only |
| call_volume / put_volume | 16,077 / 2,867 | — |

The gross call premium is large, but `bullish ≈ bearish` because the marquee call
flow is **sold on the bid**. Volume-heavy ≠ direction. Carrying phase-0.5
`[CTX] unusual_verdict = GENUINELY_UNUSUAL (EVENT/VOL — NOT DIRECTIONAL)` →
**phases 1–2 directional confluence capped at `+`** (`rubrics/confluence-scoring.md`).

### Aggressor & delta-notional split (DuckDB §A, ex-0DTE) — `[FLOW:aggressor_ex0dte DUCKDB]`

| Type | Ask (buy) $M | Bid (sell) $M | Net buy $M | Net Δ-notional $bn |
|------|-------------|---------------|-----------|---------------------|
| Calls | 4.089 | 4.445 | **−0.356** | −0.0077 |
| Puts | 0.554 | 0.861 | **−0.308** | +0.0037 |

Net call selling + net put selling = **premium harvesting**. Combined net
delta-notional ≈ −$4M (marginally short delta). The standard MCP top-N view and
this aggregate **agree** — the day is directionally flat.

### Sweeps (ask vs bid) — `[FLOW:sweeps]`

| Strike/Exp | Type | Side | Premium | Size | Read |
|-----------|------|------|---------|------|------|
| 145C 6/18 | call | **bid** | **$2,858,466** | 4,851 | **dominant — call SALE/overwrite** |
| 130P 6/18 | put | bid | $673,921 | 1,350 | put selling (mild bull / income) |
| 135C 6/18 | call | ask | $562,064 | 680 | buy |
| 145C 6/18 | call | ask | $555,382 | 1,224 | buy (small lots, 396 trades) |
| 135C 9/18 | call | bid | $373,099 | 254 | sale |
| 180C 1/15/27 | call | ask | $293,600 | 367 | **LEAP buy (bull)** |
| 140C / 125C / 150C 6/18 | call | ask | $263K / $262K / $142K | — | buys |
| 185C 6/18 | call | ask | $166,995 | 1,983 | lotto buy |
| 160C 1/15/27 | call | ask | $159,054 | 148 | LEAP buy |

Ask-side call buying (~$2.6M across many strikes) ≈ offset by the single $2.86M
145C bid-side sale. Net: a wash leaning to the sell side.

### New positioning (vol ≫ OI) — `[FLOW:unusual_volume]`

- **185C 6/18** vol 3,307 / OI 6 = **551×**, $284K, IV 68.8% — far-OTM lotto (+34%)
- **130P 6/18** vol 1,477 / OI 3 = **492×**, $735K — fresh downside bet/hedge
- **175C 6/18** 276× — far-OTM lotto
- **180C 1/15/27** 63× $301K — LEAP call accumulation
- **135P 6/18** 62× $195K — fresh puts
- **145C 6/18** vol 6,231 / OI 1,597 = 3.9× $3.49M — heavy but **distributed (sold)**

New money is genuinely **two-sided** (OTM call lottos + LEAP calls + fresh puts) —
the footprint of pre-earnings convexity positioning, not directional entry.

### DTE distribution (DuckDB §A) — `[FLOW:delta_notional DUCKDB]`

| DTE bucket | Calls $M | Puts $M | Note |
|-----------|----------|---------|------|
| 8–45DTE (6/18 monthly) | 6.261 | 1.051 | first expiry *after* the 5/28 print — the battleground |
| 46–180DTE (9/18) | 1.578 | 0.230 | — |
| LEAP (1/15/27, 3/19/27) | 1.508 | 0.208 | small genuine longer-term bull tilt |

No meaningful 0DTE noise. Flow is concentrated in the post-earnings 6/18 expiry.

### IV outliers + Greeks — `[FLOW:iv_outliers]`, `[FLOW:greek_screener]`

- `iv_outliers` (min_iv=1.0): **empty** — no NTAP contract exceeds 100% IV. IV is
  elevated (rank 100) but absolute IV30d ≈ 57.5%, far-OTM 185C ≈ 68.8% — rich, not
  extreme.
- Greek screener (by premium) is dominated by the 145C 6/18 bid prints (Δ≈0.41,
  vega≈0.15). LEAP/9-18 calls carry higher vega (0.30–0.42) — the genuine
  long-vol/long-delta positioning sits in the longer tenors, modest size.

### Sweep persistence — `[FLOW:sweep_persistence]`

NTAP in top sweeps **3 of last 5 sessions**, consistency 0.6, `dominant_direction
"bullish"`, total_sweep_premium $5.08M. **Tension to carry:** the weekly sweep
campaign leans bullish/persistent, yet *today's* marquee print is a large call
**sale**. Reads as a multi-day bullish lean now meeting pre-earnings call
overwriting / profit-taking into rich IV.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__insights_deep_dive` | symbol=NTAP, date=2026-05-22 | whole-tape: net_flow −$48.5K, P/C 0.178 |
| `mcp__uw-pp__options_flow_sweeps` | symbol=NTAP, min_premium=100k, top_n=25 | top print 145C 6/18 BID $2.86M |
| `mcp__uw-pp__options_flow_top_premium_trades` | symbol=NTAP, top_n=25 | biggest ticket 145C bid $1.80M @16:17 |
| `mcp__uw-pp__options_flow_unusual_volume` | symbol=NTAP, min_vol_oi=3, top_n=25 | 185C 551×, 130P 492× (two-sided) |
| `mcp__uw-pp__options_flow_iv_outliers` | symbol=NTAP, top_n=15 | empty (no contract >100% IV) |
| `mcp__uw-pp__options_flow_greek_screener` | symbol=NTAP, top_n=15, sort=premium | dominated by 145C bid prints |
| `mcp__uw-pp__hot_chains_sweep_persistence` | symbol=NTAP, days=5, top_n=20 | 3/5 sessions, bullish, $5.08M |
| DuckDB §A | aggressor + delta-notional, ex-0DTE | net call −$0.356M, net put −$0.308M |

## Tool errors

None. (`iv_outliers` returned empty results — not an error; no contract exceeds the
100% IV floor.)

## Verdict for downstream phases

- **Net bias from this phase:** **MIXED, marginally NOT-bullish.** Call-heavy
  volume masks a net-flat aggressor footprint with the day's biggest print a call
  *sale*. Genuine directional conviction is low.
- **Conviction (direction):** **2/5.** (Conviction that this is *event/vol
  positioning*: high.)
- **Three things later phases must remember:**
  1. The marquee flow is a **145C 6/18 overwrite (bid-side $2.86M / 4,851 ctr)** —
     read any "huge call volume" claim against this. Net call & put buying both
     **negative** (DuckDB §A).
  2. New money is **two-sided** (185C/175C lottos + LEAP 180C/160C buys + fresh
     130P/135P) — straddle-shaped around the **5/28 print**, 6/18 is the
     battleground expiry.
  3. Small but real **longer-term bull tell**: $1.51M LEAP calls bought on ask
     (180C/160C 1/15/27). The only clean directional conviction is slow and small.
- **Open questions:** Is the dark pool (phase 2) confirming accumulation under the
  flat tape, or is it also two-sided? Is the 130P buying a hedge against a held
  long, or a standalone bear bet? Does dealer positioning (phase 4) show the 145C
  overwrite as a known supply wall?
