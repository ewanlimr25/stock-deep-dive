# Phase 1 — Options Flow

**Ticker:** OKLO
**As-of date:** 2026-07-17
**Generated:** 2026-07-18T00:00:00Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md

## Summary

Today's OKLO tape is **mixed but leans cautious**: the whole-tape aggregate is barely
net-bullish (+$397,772) yet **put premium ($13.41M) is 2.1× call premium ($6.34M)**, and
the biggest prints are deep-ITM put rolls plus a fresh downside put. The single most
durable signal is the **5-day sweep-persistence: OKLO is `bearish`-dominant, in the top
sweep names all 5 sessions (consistency_score 1), $41.0M cumulative sweep premium**
[FLOW:sweep_persistence]. Front-week ATM $41.5 calls opened big (vol/OI 19.4) but trade
on the **bid** (being sold), while a far-OTM Jan-2027 $110 LEAP call ($0.55M, delta 0.16)
is the only clean bullish footprint. Per phase-0.5 this is a `BUSY_NAME_NORMAL_DAY` —
magnitude discounted, conviction capped at `+`.

## Key signals

- **5-session bearish sweep campaign**: `dominant_direction=bearish`, `sessions_in_top=5/5`,
  `consistency_score=1`, `total_sweep_premium=$41,004,637` (dates 07-13→07-17) [FLOW:sweep_persistence]
- **Put premium 2.1× call premium**: put_premium $13,408,062 vs call_premium $6,344,472,
  even as net_flow (bull−bear) is only +$397,772 [FLOW:insights_deep_dive]
- **ATM front call being sold**: $41.5c exp 2026-07-24 opened new (vol 2428 / OI 125,
  vol/OI 19.4) but $512K crossed on the **bid** → call writing / distribution [FLOW:sweeps_bid]
- **Fresh downside put**: $30p exp 2026-11-20, vol 1110 / OI 264 (vol/OI 4.2), $366K new —
  a directional/hedge bet on a ~27% drawdown [FLOW:unusual_volume]
- **Lone bullish print**: $110c exp 2027-01-15 LEAP, $550K, size 1350, delta 0.16 — far-OTM
  moonshot, slow and low-probability [FLOW:top_premium_trades]

## Detailed findings

### Whole-tape aggregate (read the top-N against this) — [FLOW:insights_deep_dive]

| Field | Value |
|---|---|
| bullish_premium | $8,702,389 |
| bearish_premium | $8,304,617 |
| **net_flow (derived bull−bear)** | **+$397,772** (barely bullish) |
| call_premium | $6,344,472 |
| put_premium | $13,408,062 (**2.11× call premium**) |
| call_volume | 28,491 |
| put_volume | 20,838 |
| put_call_ratio | 0.731 (more call *volume*, but puts far more $) |
| iv_rank | 32.7 · iv30d 97.5% |

Interpretation: aggressor-based net direction is a coin-flip (+$398K on ~$19.8M total),
but the **money is in puts** — the put premium is concentrated in large deep-ITM strikes
(delta ≈ −1). Volume skews to calls (cheap front-week), premium skews to puts (big ITM).

### Sweeps (ask vs bid) — [FLOW:sweeps_ask / sweeps_bid]

- **Ask-side (aggressive buys), 10 prints:** dominated by deep-ITM puts — $65p 08-14 $790K,
  $70p 10-16 $415K, $120p 10-16 $382K, $30p 11-20 $362K, plus $22.5c 12-18 $280K.
  Put-heavy aggressive buying.
- **Bid-side (aggressive sells), 14 prints:** $120p 10-16 **$1.27M** (deep-ITM put sold),
  $65p 07-31 $786K, **$41.5c 07-24 $512K (ATM call sold)**, $47c 2027-01-15 $185K (OTM call written).
- **Read:** the deep-ITM put strikes (65/120) appear on **both** sides (e.g. $120p 10-16 ask
  $382K + bid $1.27M; $65p ask $395K×2 vs $65p 07-31 bid $392K×2) → **rolling large put
  positions out in time**, i.e. maintaining short-delta / protective structure, not fresh
  clean shorts. The clean fresh directional adds are the $30p (bearish/hedge) and the ATM
  call *selling*.

### New positioning (unusual vol, vol/OI ≥ 3) — [FLOW:unusual_volume]

| Type | Strike | Exp | Vol | OI | vol/OI | Prem | IV |
|---|---|---|---|---|---|---|---|
| call | 41.5 | 07-24 | 2428 | 125 | 19.4 | $519K | 91% |
| put | 65 | 08-14 | 338 | 47 | 7.2 | $790K | 83% |
| put | 30 | 11-20 | 1110 | 264 | 4.2 | $366K | 94% |
| call | 42 (0DTE) | 07-17 | 1651 | 206 | 8.0 | $46K | 140% |
| call | 43/43.5/44 | 07-24/31 | small | | 3–6 | <$65K | ~92% |

Biggest *new* positions: the ATM $41.5c (sold on the bid) and the deep-ITM $65p / OTM $30p.
Small front-week upside calls (43–44) are cheap lottery adds.

### Largest premium prints — [FLOW:top_premium_trades]

Puts = **$4.23M (19 trades)** vs calls **$1.28M (6 trades)**. Deltas on the top puts are
−0.9 to −1 (deep ITM, K=65/85/100/120 vs spot ~$41). Side split near-balanced: ask $1.73M /
bid $1.99M / mid $1.24M. Largest single: **$85p 0DTE, delta −1, $663K, side mid, size 150**
(gamma 0 / vega 0 → synthetic-stock replacement or a close, not a vol view).

### IV outliers + Greeks — [FLOW:iv_outliers / greek_screener]

All 15 IV-outlier rows are **0DTE (exp 2026-07-17) with IVs 300–1000%+** — near-expiry pin
artifacts, **discarded** as noise per skill guidance. Greek-screener top rows are the same
deep-ITM 0DTE puts (delta −1, gamma/vega ≈ 0). No clean high-vega directional vol bet.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `insights deep-dive --symbol OKLO --date 2026-07-17` | net_flow +$397,772 ← `.uw_screener.bullish_premium − .bearish_premium`; put_prem 13.41M ← `.uw_screener.put_premium` | whole-tape |
| `options-flow sweeps --side ask --min-premium 100000 --top-n 25` | 10 prints, put-heavy ← `.results[]` | top-10 |
| `options-flow sweeps --side bid` | $41.5c 07-24 $512K on bid ← `.results[]` | top-14 |
| `options-flow unusual-volume --min-vol-oi-ratio 3` | $41.5c vol/OI 19.4 ← `.results[0].vol_oi_ratio` | top-10 |
| `options-flow top-premium-trades --top-n 25` | put $4.23M vs call $1.28M ← `.results|group_by(.option_type)` | top-25 |
| `options-flow iv-outliers --top-n 15` | all 0DTE noise ← `.results[].expiry` | 15 (discarded) |
| `options-flow greek-screener --sort-by premium` | $85p delta −1 $663K ← `.results[0]` | top-15 |
| `hot-chains sweep-persistence --days 5 --symbol OKLO` | bearish, 5/5, $41.0M ← `.results[0]` | 1 (OKLO) |
| `hot-chains smart-money-flow --direction bullish/bearish --min-volume 500` | OKLO outside top-30 both dirs ← filtered `.results[]` | 0 rows OKLO |
| `hot-chains sweep-ratio --min-sweep-ratio 0.3` | OKLO outside top-30 ← filtered | 0 rows OKLO |

## Tool errors

- `hot-chains sweep-persistence --date 2026-07-17` → `Error: unknown flag: --date`. Re-run
  without `--date`; the tool anchors to the latest available date, which IS 2026-07-17
  (dates_covered = 07-13…07-17), so the read is as-of-consistent for this run.

## DATA NOTE / CORRECTION

First read stood after the `--date` flag was dropped on sweep-persistence. All numbers
round-tripped through `jq` on validated JSON.

## Verdict for downstream

- **Net bias:** MIXED, leaning **bearish/cautious**. The 5-day bearish sweep persistence
  + 2.1× put-premium skew + ATM-call *selling* outweigh the marginal +$398K net-directional
  and the lone far-OTM LEAP call.
- **Conviction:** 2 / 5 (signal exists but muddied — much of the put premium is *rolls/hedges*,
  today is a `BUSY_NAME_NORMAL_DAY`, and net-directional is a coin-flip).
- **Three datapoints later phases must remember:**
  1. **5-session bearish sweep campaign, $41.0M, consistency 1** — the most durable flow read.
  2. Put premium **2.1× call premium** with the biggest puts deep-ITM (delta ≈ −1) and
     appearing on both sides → large **put-position rolling** (short-delta/protective).
  3. The big new front-week ATM $41.5 call is being **sold on the bid**, not bought — the
     one loud "bullish" number is actually distribution.
- **Open questions:** Is the dark pool confirming distribution (phase 2)? Are the deep-ITM
  puts hedging a large long (dealer/holder) or a genuine synthetic short? Does OI (phase 3)
  show the $30 / $65 puts building as fresh open interest vs. closing?
