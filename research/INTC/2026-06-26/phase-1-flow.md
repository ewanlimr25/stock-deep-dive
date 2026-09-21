# Phase 1 — Options Flow

**Ticker:** INTC
**As-of date:** 2026-06-26
**Generated:** 2026-06-27T09:55:13-0400
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md

## Summary

Net directional bias is **BEARISH** once the tape is read correctly. The headline
"call premium" ($494.5M calls vs $71.6M puts) is **deep-ITM delta-one / financing
flow** — strikes 77–89 trading at ≈intrinsic value with garbage IV and delta ≈0.99 —
not bullish conviction. Strip that out and the genuine directional layer is protective
**puts**: the single largest premium print of the day is a 12-month ATM put (`$130
Jun-2027, $5.83M`), backed by a Sep `$110` put ($2.91M). The whole-tape classifier
agrees: `bearish_premium $234.3M > bullish_premium $183.4M`, derived **net_flow
−$50.9M**. Most importantly, this is **not a one-day event** — `sweep-persistence`
flags INTC with a **5-of-5-session bearish sweep campaign, consistency_score 1.0,
$925.2M cumulative sweep premium**.

## Key signals

- **5-session bearish sweep campaign**, consistency_score **1.0**, sessions_in_top
  **5/5**, total_sweep_premium **$925.2M**, dominant_direction **bearish**
  [FLOW:sweep_persistence].
- **Whole-tape net_flow −$50.9M** (bearish_premium $234.3M − bullish_premium $183.4M);
  P/C ratio 0.582 [FLOW:insights_deep_dive].
- **Biggest single print = 12-month ATM PUT** `$130 Jun-2027 $5.83M` (delta −0.33,
  vega 0.46), plus Sep `$110` put $2.91M — protective/bearish [FLOW:top_premium_trades].
- **Headline call sweeps are FINANCING, not bullish**: $109.4M ask-side + $152.0M
  bid-side, ~all deep-ITM calls (strikes 77–89) at intrinsic, delta ≈0.99, vega ≈0,
  avg_iv 11–14 (garbage) [FLOW:sweeps][FLOW:unusual_volume].
- Minor genuine bullish offset: Sep/Jul `$160` OTM calls (~$5.4M, delta 0.24–0.39)
  [FLOW:top_premium_trades] — small upside speculation against the bearish core.

## Detailed findings

### Whole-tape aggregate (the truth set — read top-N against this)

From `insights deep-dive .uw_screener` [FLOW:insights_deep_dive]:

| Field | Value |
|---|---|
| `call_premium` | $494.5M |
| `put_premium` | $71.6M |
| `bullish_premium` | $183.4M |
| `bearish_premium` | $234.3M |
| **derived `net_flow` (bullish − bearish)** | **−$50.9M (bearish)** |
| `call_volume` / `put_volume` | 384,599 / 223,790 |
| `put_call_ratio` | 0.582 |
| `iv_rank` | 94.1 |

The 7:1 call-over-put *premium* skew contradicts the −$50.9M net_flow only on the
surface: the call premium is dominated by deep-ITM financing prints (next section) that
the bull/bear classifier correctly does NOT count as bullish intent. Per phase-0.5,
this is a `GENUINELY_UNUSUAL` (bearish-skewed) tape; the BUSY_NAME cap is not triggered.

### Sweeps (ask vs bid) — dominated by deep-ITM financing, NOT directional

| Side | Total prem | Calls | Puts |
|---|---|---|---|
| Ask | $113.2M | $109.4M (21 sweeps) | $3.8M (4) |
| Bid | $152.9M | $152.0M (24 sweeps) | $0.9M (1) |

Top sweeps both sides are **adjacent deep-ITM call strikes 88/89 for the same Jul-02
expiry**, on BOTH ask ($88 $57.0M) and bid ($89 $55.3M, $88 $21.8M) — avg prices ≈
intrinsic (e.g. $88c avg $41.01 vs intrinsic $128.67−88 = $40.67). Two-sided deep-ITM
flow at adjacent strikes/one expiry = a **box/roll/financing or stock-replacement
structure**, carrying ~zero directional or vol information. Excluded from the
directional read.

### New positioning (unusual vol, vol/OI ≥ 3)

The vol/OI≥3 "new positions" are the same deep-ITM financing calls (`$88 Jul-02`
$104.1M vol 25,401 OI 33; `$89 Jul-02` $101.5M OI 3 vol/oi 8,467; 0DTE 77–80 calls) —
all with avg_iv 1.5–14 (undefined, deep-ITM). The **only genuine new directional
position** in the list is **put `$130 Jun-2027` $5.83M, vol 1,530, avg_iv 0.82 (82%,
sane)** — a long-dated ATM put. Bearish/protective.

### Largest premium prints (single-trade)

| # | Type | Strike | Expiry | Premium | Side | Greeks | Read |
|---|---|---|---|---|---|---|---|
| 1 | put | 130 | 2027-06-17 | $5.83M | no_side | δ−0.33 ν0.46 | **Bearish (12-mo ATM)** |
| 2 | put | 110 | 2026-09-18 | $2.91M | no_side | δ−0.27 | **Bearish (3-mo OTM)** |
| 3 | call | 160 | 2026-09-18 | $2.72M | mid | δ0.39 | Bullish (OTM upside) |
| 4 | call | 160 | 2026-07-24 | $2.72M | no_side | δ0.24 | Bullish (OTM upside) |
| 5–6 | call | 79/80 | 2026-06-26 | $2.46/2.41M | bid | δ0.99 ν~0 | Financing (0DTE deep-ITM) |
| 7 | call | 100 | 2028-01-21 | $2.39M | ask | δ0.80 | Bullish-ish LEAP (stock-repl) |
| 10 | call | 134 | 2026-07-02 | $1.74M | bid | — | Slightly-OTM call **sold** (bearish-ish) |

Genuine directional dollars: **~$8.7M puts (bearish) vs ~$7.5M OTM/LEAP calls
(bullish)** — net bearish, with the bearish leg longer-dated and the protective put the
single biggest print.

### IV outliers + Greeks

IV-outliers are entirely the deep-ITM 0DTE financing calls (avg_iv 3.9–9.5 = 390–950%,
undefined) — no actionable vol signal; ignore for direction. Greek-screener top-by-
premium confirms the structure: the two genuine high-premium directional names carry
real negative delta (puts −0.33/−0.27) and the deep-ITM calls carry δ≈0.99 / ν≈0
(financing).

### Smart-money / sweep-ratio (market-wide context)

INTC does **not** appear in the market-wide top-10 `smart-money-flow` (bullish or
bearish) per-contract lists, nor in the top-15 `sweep-ratio` — consistent with
phase-0.5 (the signal is in directional *premium skew*, not a single contract topping
the tape). The persistence signal (below) is where INTC stands out.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `insights deep-dive --symbol INTC --date 2026-06-26` | net_flow −$50.9M ← `.uw_screener.bullish_premium − .bearish_premium`; call/put prem 494.5/71.6M; pc 0.582 | whole-tape |
| `options-flow sweeps --side ask --min-premium 100000` | calls $109.4M vs puts $3.8M ← `group_by(.option_type)`; top $88c Jul-02 $57.0M avg 41.01 | top-25 |
| `options-flow sweeps --side bid …` | calls $152.0M; top $89c Jul-02 $55.3M avg 39.99 | top-25 |
| `options-flow unusual-volume --min-vol-oi-ratio 3` | $88c Jul-02 $104.1M voloi 770; put $130 Jun-2027 $5.83M avg_iv 0.82 ← `.results[]` | top-25 |
| `options-flow top-premium-trades --top-n 25` | put $130 2027 $5.83M δ−0.33; put $110 Sep $2.91M ← `.results[].premium,.delta` | top-25 |
| `options-flow iv-outliers --top-n 15` | all deep-ITM 0DTE calls, avg_iv 3.9–9.5 (undefined) | top-15 |
| `options-flow greek-screener --sort-by premium` | put $130 δ−0.33 ν0.46; 0DTE calls δ0.99 ν~0 ← `.results[].delta,.vega` | top-15 |
| `hot-chains smart-money-flow --direction bullish/bearish` | INTC rows = 0 (not in market-wide top-10) | top-10 ×2 |
| `hot-chains sweep-persistence --symbol INTC --days 5` | **bearish, consistency 1.0, 5/5 sessions, $925.2M** ← `.results[0]` | 5-day |
| `hot-chains sweep-ratio --min-sweep-ratio 0.3` | INTC rows = 0 | top-15 |

## Tool errors

- `hot-chains sweep-persistence … --date 2026-06-26` → `unknown flag: --date` (trailing
  tool, latest-anchored). Re-run without `--date`; latest = as-of 2026-06-26, so the
  read is valid for this date. No value transcribed from the failed call.

## DATA NOTE / CORRECTION

None — all values round-tripped through `jq` on validated JSON on first read.

## Verdict for downstream phases

- **Bias from this phase:** **bearish** (moderate). The cleanest, longest-dated, and
  most persistent flow is bearish; the bullish-looking premium is financing.
- **Conviction:** **3 / 5**. Lifted by the 5/5-session persistence (consistency 1.0)
  and the protective-put leadership; held back because the magnitude is partly
  financing-obscured and it's a direction/premium signal, not a volume surge
  (phase-0.5: vol-vs-avg NOT elevated).
- **Three things later phases should remember:**
  1. **Headline call premium ($494.5M) is deep-ITM delta-one FINANCING (strikes 77–89,
     delta ≈0.99, garbage IV) — NOT bullish.** Any downstream phase reading "huge call
     flow = bullish" is wrong here.
  2. **5-session BEARISH sweep persistence — consistency_score 1.0, sessions_in_top
     5/5, $925.2M** [FLOW:sweep_persistence]. The strongest single edge in this phase.
  3. **Biggest genuine new position = 12-month ATM PUT ($130 Jun-2027, $5.83M)** + Sep
     $110 put; net_flow −$50.9M. Bearish/protective core.
- **Open questions:**
  - Is the **dark pool** confirming distribution at/under $128.67 (phase-2)?
  - Does the **OI** put buildup at 130/135 Jul-17 (phase-0.5 carry) corroborate into
    OPEX (phase-3)? Where is the gamma/zero-gamma flip (phase-4)?
  - What event is the deep-ITM call financing tied to (dividend/roll)? Advisory only.
