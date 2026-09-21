# Phase 1 — Options Flow

**Ticker:** BABA
**As-of date:** 2026-05-27
**Generated:** 2026-05-28T03:05:00Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md

## Summary

Today's BABA tape is **mixed and light, leaning mildly bearish/range-bound**.
Gross call premium ($17.2M) dwarfs put premium ($6.1M), but the net-aggressive
read is the opposite of directional buying: customers **sold** more calls than
they bought ($8.77M bid vs $6.13M ask, ex-0/1DTE) **and** sold more puts than
they bought ($3.21M vs $2.33M) — **two-sided premium selling into a collapsing IV
(rank 83→21)**, i.e. vol-selling/overwriting, not conviction. The one durable
directional signal is **5-session bearish sweep persistence** (consistency 1.0,
all 5 sessions in top, $43.1M, dominant direction bearish) `[FLOW:sweep_persistence]`.
Against that trend sits a small, patient contrarian bull quietly lifting a
**deep-OTM C210 Dec-2028 LEAP** repeatedly on the ask `[FLOW:top_premium_trades]`.
Carrying phase-0.5 `unusual_verdict = BUSY_NAME_NORMAL_DAY` → conviction capped.

## Key signals

- **5-day bearish sweep campaign:** consistency 1.0, 5/5 sessions in top,
  $43.14M total sweep premium, `dominant_direction = bearish` `[FLOW:sweep_persistence]`.
- **Net-aggressive flow is premium-selling, not buying:** calls net sold
  ($8.77M bid > $6.13M ask), puts net sold ($3.21M bid > $2.33M ask), ex-0/1DTE
  `[FLOW:aggressor_ex0dte DUCKDB]`.
- **Whole-tape `net_flow` −$1.76M** (bearish_premium $11.1M > bullish_premium
  $9.35M); P/C ratio 0.385; call_premium $17.2M vs put_premium $6.05M
  `[FLOW:insights_deep_dive]`.
- **Biggest single prints split both ways:** ask-side deep-ITM C105 6/18 buy
  $774K + repeated C210 Dec-2028 LEAP buys (bullish), vs bid-side P125 6/18 sold
  $791K + heavy call selling (C135/C130 6/18) `[FLOW:sweeps]`.
- **No smart-money concentration:** BABA absent from both bullish and bearish
  `smart_money_flow` top-50, and absent from the `sweep_ratio` and ≥2x-volume
  leaders `[FLOW:smart_money_flow]`.

## Detailed findings

### Whole-tape aggregate (read top-N against this) `[FLOW:insights_deep_dive]`

| Field | Value |
|-------|-------|
| call_premium | $17,158,096 |
| put_premium | $6,052,197 |
| bullish_premium | $9,347,073 |
| bearish_premium | $11,107,627 |
| **net_flow** | **−$1,760,554** (bearish) |
| put_call_ratio | 0.385 |
| call_volume / put_volume | 52,544 / 20,219 |
| total_open_interest | 1,756,723 |
| iv30d / iv_rank | 0.372 / **21.2** |
| implied_move | 2.76 (**2.16%**) |

Gross is call-tilted, but `net_flow` is bearish and — critically — the DuckDB
aggressor split below shows the gross call volume is being **sold**, not bought.

### Net-aggressive split, ex-0/1DTE (DuckDB §A) `[FLOW:aggressor_ex0dte DUCKDB]`

| type | side | trades | prem $M | Δ-notional $bn |
|------|------|-------:|--------:|---------------:|
| call | ask (buy) | 4,071 | 6.13 | +0.061 |
| call | **bid (sell)** | 5,615 | **8.77** | +0.089 |
| call | mid | 1,317 | 1.65 | +0.016 |
| put | ask (buy) | 2,013 | 2.33 | −0.030 |
| put | **bid (sell)** | 2,224 | **3.21** | −0.046 |
| put | mid | 594 | 0.51 | −0.007 |

Both legs net-sold → **two-sided premium selling / vol monetization** into the
IV collapse. Net delta-notional +$0.087bn (mildly long-delta footprint, small).

### Premium by DTE bucket (DuckDB §A) `[FLOW:delta_notional DUCKDB]`

| bucket | call $M | put $M |
|--------|--------:|-------:|
| 2–7DTE | 1.16 | 1.44 |
| 8–45DTE | 5.11 | 2.79 |
| 46–180DTE | 4.33 | 1.29 |
| **LEAP (>180D)** | **6.55** | 0.53 |

LEAP calls are the single biggest premium bucket — the C210 Dec-2028 accumulation.
Put activity is concentrated short (2–7DTE puts ≈ calls) — near-dated hedging /
pin, not a structural bearish bet.

### Sweeps (ask vs bid) `[FLOW:sweeps]`

- **Ask-side (aggressive buys):** 13 sweeps, $3.51M. Led by C105 6/18 $774K
  (deep-ITM stock-replacement, bullish), C210 Dec-2028 LEAP $763K, C135 6/18
  $426K, C150 Jan-2027 $191K, C100 Aug-2026 $183K. Some put buys (P125/P135/P127).
- **Bid-side (aggressive sells):** 25 sweeps, $5.42M. Led by **P125 6/18 sold
  $791K** (bullish — downside puts monetized/closed), then heavy call selling:
  C135 6/18 $533K, C130 6/18 $353K, C125 LEAP $331K, C155 Jan-2027 $292K.
- More premium hit the bid ($5.42M) than the ask ($3.51M) → seller-initiated tilt.
- *Note:* `executed_at` / `total_volume` returned null in the sweeps view; sizing
  read from premium only.

### New positioning — unusual vol (vol/OI ≥ 3) `[FLOW:unusual_volume]`

C116 & C115 6/5 (vol 232, OI 1, vol/OI 232 — brand-new near-dated call lotto),
C134 7/2 (vol 390, OI 11), **C210 Dec-2028 (vol 400, OI 20 — the LEAP opening)**,
C128 6/5 (vol 173). Net: new positioning is short-dated call lotto + the one
LEAP — modest, not a large opening campaign.

### Top premium trades `[FLOW:top_premium_trades]`

C140 Aug-2026 $596K (no_side / spread leg), **C210 Dec-2028 repeated ask buys**
($190K, $190K, $96K×3), C100 Aug-2026 $168K ask, C130 Mar-2027 $133K bid (sold),
C134 7/2 $127K bid (sold), C105 6/18 $111K ask. Calls dominate the premium
leaderboard; ask = ITM/LEAP buying, bid = call overwriting.

### IV outliers `[FLOW:iv_outliers]`

Far-OTM 2-DTE calls only: C180 5/29 IV 163%, C165 IV 129%, C160 IV 118% — tiny
premium ($61–211), pin-lottery noise. No structural IV signal.

## Tool calls (audit trail)

| Command | Result summary |
|---------|----------------|
| `uw options-flow sweeps --symbol BABA --side ask --min-premium 100000` | 13 sweeps, $3.51M, ITM-call + LEAP buying |
| `uw options-flow sweeps --symbol BABA --side bid --min-premium 100000` | 25 sweeps, $5.42M, P125 sold + call overwriting |
| `uw options-flow unusual-volume --symbol BABA --min-vol-oi-ratio 3` | short-dated call lotto + C210 LEAP open |
| `uw options-flow top-premium-trades --symbol BABA` | calls dominate; C210 Dec-2028 repeated ask buys |
| `uw options-flow iv-outliers --symbol BABA` | far-OTM weekly call noise only |
| `uw hot-chains smart-money-flow --direction bullish/bearish` | BABA absent both lists |
| `uw hot-chains sweep-persistence --days 5 --symbol BABA` | **consistency 1.0, 5/5, $43.1M, bearish** |
| `uw hot-chains sweep-ratio` | BABA not a leader |
| `uw insights deep-dive --symbol BABA` | whole-tape aggregate (table above) |
| DuckDB §A (`bot-eod-report-2026-05-27.parquet`) | aggressor + delta-notional + DTE split |

## Tool errors

- `uw hot-chains sweep-persistence --date 2026-05-27` → `unknown flag: --date`.
  Re-ran without `--date`; it anchors to the latest available date (2026-05-27 =
  as-of), so the result is date-correct. (Consistent with the known trailing-tool
  behavior in memory `uw-cli-mcp-parity`.)

## Verdict for downstream

- **Net bias:** mixed, **leaning mildly bearish / range-bound**. The directional
  edge is small; the dominant character is two-sided premium selling into IV
  collapse plus a persistent (if modest) 5-day bearish sweep campaign.
- **Conviction:** **2 / 5.** Light, two-sided, no smart-money concentration; only
  the 5-day sweep persistence carries weight. Per phase-0.5 `BUSY_NAME_NORMAL_DAY`,
  phases 1–2 confluence capped at `+`.
- **Three things later phases must remember:**
  1. **5-session bearish sweep persistence** (consistency 1.0, $43.1M) is the
     single most reliable flow signal here — it aligns with the ~12% downtrend.
  2. Net-aggressive flow is **premium-selling on both sides** (calls sold > bought,
     puts sold > bought) — a vol-monetization regime, *not* directional accumulation.
     Any bullish call-volume headline is mostly **call overwriting**.
  3. A patient contrarian is **accumulating the deep-OTM C210 Dec-2028 LEAP** on
     the ask — a small long-horizon bullish footprint to watch, not a tradeable
     short-term signal.
- **Open questions:** Is the dark pool confirming distribution or accumulation at
  $127–128 (phase-2)? Is the call selling covered overwriting (neutral) or naked
  (bearish)? Does dealer positioning (phase-3/4) pin price in the $125–135 zone
  consistent with the put-selling at P125?
