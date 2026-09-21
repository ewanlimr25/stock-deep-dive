# Phase 1 — Options Flow

**Ticker:** NVDA
**As-of date:** 2026-05-27
**Generated:** 2026-05-28T02:20:00Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md

## Summary

NVDA's tape is **net bearish despite enormous gross call premium**. The whole-tape
aggregate is net-bearish (`net_flow = -$66.25M`, bullish $575M vs bearish $641M),
**bid-side sweep premium ($215.9M) exceeds ask-side ($155.9M)**, and the single
largest prints are **LEAP calls sold on the bid** ($37.8M Jun-2028 $210C, $20.8M
Dec-2027 $210C). Most decisively, the 5-session sweep-persistence read tags NVDA
`dominant_direction = bearish` with a **perfect consistency_score of 1 (5/5 sessions
in the bearish top, $4.55B cumulative)** — this is a sustained distribution campaign,
not a one-day blip. Per phase-0.5 this is a `BUSY_NAME_NORMAL_DAY` so magnitude is
discounted, but the *direction* is unambiguous and persistent.

## Key signals

- **Net flow bearish:** `net_flow = -$66.25M`, bullish $575.07M < bearish $641.32M
  [FLOW:insights_deep_dive]; NVDA = universe rank #4 net-bearish (phase-0.5).
- **Bid-side selling > ask-side buying:** bid-sweep premium $215.9M vs ask-sweep
  $155.9M [FLOW:sweeps] — net premium is being *hit*, not *lifted*.
- **LEAP calls being written/sold:** largest bid prints = Jun-2028 $210C $37.84M,
  Dec-2027 $210C $20.83M [FLOW:sweeps] — long-dated call supply.
- **5-session bearish persistence:** `dominant_direction=bearish`,
  `consistency_score=1`, `sessions_in_top=5`, `$4.55B` [FLOW:sweep_persistence].
- **No clean bullish smart-money:** NVDA outside top-50 on `smart_money_flow`
  (both directions) and outside top-50 on `sweep_ratio` [FLOW:smart_money_flow].

## Detailed findings

### Whole-tape aggregate (read top-N against this) — [FLOW:insights_deep_dive]

| Field | Value |
|-------|-------|
| `call_premium` | $1,482,343,454 |
| `put_premium` | $342,603,767 |
| `bullish_premium` | $575,068,095 |
| `bearish_premium` | $641,319,214 |
| **`net_flow` (bull−bear)** | **−$66,251,119 (net bearish)** |
| `put_call_ratio` | 0.396 (call-heavy by gross premium/volume) |
| `total_open_interest` | 15,940,062 |
| `iv_rank` / `iv30d` | 30.5 / 0.375 |
| `implied_move` | $4.12 (1.94%) |

The interpretation that matters: gross *call* premium is 4× gross *put* premium,
which a top-N-only read would call "wildly bullish." But the **net directional**
figure is negative and the sweep tape (below) shows the calls are predominantly
**sold on the bid**. Big call *volume*, bearish call *direction*.

### Sweeps (ask vs bid) — [FLOW:sweeps]

- **Ask-side (buying):** 25 sweeps, $155.9M total. Top: Jul-17 $215C $11.21M,
  Sep-18 $225C $10.62M, 0DTE $210C $9.18M.
- **Bid-side (selling):** 25 sweeps, **$215.9M total (38% larger)**. Top:
  **Jun-2028 $210C $37.84M, Dec-2027 $210C $20.83M**, Jun-05 $215C $12.22M,
  Jun-2027 $200C $12.05M. The two biggest single prints on the day are long-dated
  ITM/ATM calls being *sold* — consistent with institutional long unwinds or
  covered-call/overwrite supply.

### New positioning (unusual vol, vol/OI≥3) — [FLOW:unusual_volume]

Dominated by **0DTE pin activity**: $212.5C 0DTE (vol 351,362 / OI 4,130,
vol/OI 85), $207.5C 0DTE (vol 15,759). These are gamma/pin mechanics around the
$210 level, not directional tenor — tag and discount (common pitfall #1).

### Largest premium prints + Greeks — [FLOW:greek_screener]

The largest *premium* prints are **deep-ITM, high-delta calls**: Sep-18 $190C
(Δ0.714, $202.2M), Jun-18 $170C (Δ0.963, $187.1M + $52.2M). Delta near 1.0 = stock
proxies; combined with bid-side execution this reads as **long-exposure reduction /
stock-replacement unwind**, not fresh bullish bets. Largest put: Jun-2028 $235P
(Δ−0.46, $4.37M, mid).

### IV outliers — [FLOW:iv_outliers]

Scattered low-strike/short-dated names, no concentrated OTM-put fear cluster. IV
rank 30.5 (phase-0.5) — vol is cheap and was sold down from ~76 in mid-May.

## Tool calls (audit trail)

| Command | Result summary |
|---------|----------------|
| `uw insights deep-dive --symbol NVDA --date 2026-05-27` | net_flow −$66.25M, P/C 0.396 |
| `uw options-flow sweeps --side ask … ` | 25 rows, $155.9M (calls) |
| `uw options-flow sweeps --side bid … ` | 25 rows, $215.9M (LEAP calls sold) |
| `uw options-flow top-premium-trades …` | premium field returned 0; side field shows mostly bid-side calls |
| `uw options-flow unusual-volume --min-vol-oi-ratio 3 …` | 0DTE pin at $212.5/$207.5 |
| `uw options-flow iv-outliers …` | no OTM-put fear cluster |
| `uw options-flow greek-screener --sort-by premium …` | deep-ITM Δ0.7–0.96 calls largest |
| `uw hot-chains smart-money-flow --direction bullish\|bearish …` | NVDA outside top-50 both |
| `uw hot-chains sweep-persistence --days 5 --symbol NVDA` | **bearish, score 1, 5/5, $4.55B** |
| `uw hot-chains sweep-ratio …` | NVDA outside top-50 |

## Tool errors

- `uw hot-chains sweep-persistence … --date 2026-05-27` → `Error: unknown flag:
  --date`. Re-ran without `--date`; per the uw CLI it anchors to the latest
  available date (= 2026-05-27 here), so the result is as-of-correct for this run.
- `uw options-flow top-premium-trades` returned `total_premium = 0.00` for all rows
  (field-population issue on that leaf); the `side` field still resolved (mostly
  `bid` on calls), consistent with the sweeps read. Not used for magnitude.

## Verdict for downstream

- **Net bias:** **BEARISH** (net_flow negative, bid-side > ask-side, 5-session
  bearish persistence, deep-ITM call selling).
- **Conviction:** **4/5** on direction (the 5/5 persistence + universe rank #4 +
  bid-side dominance is unusually consistent), but **magnitude discounted to `+`**
  per phase-0.5 busy-name cap; IV is low (30.5) so options are not pricing stress.
- **Three datapoints later phases must remember:**
  1. `net_flow = -$66.25M`; bid-sweep $215.9M > ask-sweep $155.9M — calls are
     being *sold*, not bought.
  2. `sweep_persistence`: NVDA bearish 5/5 sessions, $4.55B — a multi-day campaign,
     the strongest single signal in this phase.
  3. The $210 strike is the gravitational center (0DTE pin + the two largest LEAP
     prints both $210C) — phases 3/4 should check OI/GEX there.
- **Open questions:**
  - Is dark pool (phase-2) confirming distribution at/above $210, or absorbing it?
  - Are the bid-side LEAP calls *closing* longs (OI falling) or *opening* short
    call positions (OI rising)? Phase-3 OI-change resolves this.
