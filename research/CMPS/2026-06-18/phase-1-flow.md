# Phase 1 — Options Flow

**Ticker:** CMPS
**As-of date:** 2026-06-18
**Generated:** 2026-06-20
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md

## Summary

CMPS's tape is **net bearish, and the bearishness is essentially one position.** The
whole-tape aggregate is put-heavy (put premium $737,595 vs call $250,780; net_flow
= bullish $179,048 − bearish $774,197 = **−$595,149**; P/C 1.36). The top-25 prints
capture $800,936 of premium and **85% of it ($677,400) is ask-side put buying**,
almost all of it concentrated in the **Jan-2028 $10 LEAP put bought on the ask** —
~$647K across four prints in a 30-minute window (10:04–10:33 ET), brand-new
(vol/OI ≈ 14, OI was 144). Net delta-notional across the top-25 is **−$411,388**.
This is an aggressive, single-session bearish/protective LEAP initiation on a small
name — not a multi-day campaign (sweep-persistence consistency 0.2, sessions_in_top 1).

## Key signals

- Net flow **−$595,149** bearish, P/C **1.36**, put premium 2.9× call premium
  [FLOW:insights_deep_dive]
- Single dominant print: **Jan-2028 $10 PUT, ask-side, ~$647K / ~1,839 contracts**,
  delta −0.24, IV ~85%, bought 10:04–10:33 ET [FLOW:top_premium_trades]
- Top-25 split: **put/ask $677,400** ≫ put/bid $47,430 ≈ call/ask $52,186 > call/bid
  $23,920 — overwhelmingly ask-side puts [FLOW:greek_screener]
- New positioning: P10 LEAP vol/OI **13.97** (2011 vol on 144 OI) — opening, not
  closing [FLOW:unusual_volume]
- **No multi-day persistence** (consistency 0.2, 1 session) and **no smart-money
  rows** for CMPS in either direction — too small for the market-wide top-N
  [FLOW:sweep_persistence, FLOW:smart_money_flow]

## Detailed findings

### Whole-tape aggregate (`[FLOW:insights_deep_dive]`, underlying $12.03)

| Field | Value |
|-------|-------|
| call_premium | $250,780 |
| put_premium | $737,595 |
| bullish_premium | $179,048 |
| bearish_premium | $774,197 |
| **net_flow (derived bull−bear)** | **−$595,149** |
| put_call_ratio | 1.3641 |
| call_volume / put_volume | 1,648 / 2,248 |
| iv_rank | 20.35 (LOW; universe pctile 21.2) |
| iv30d | 0.9379 (93.8% — high absolute, typical biotech) |
| implied_move_perc | 4.14% |

The top-25 puts ($677K ask + $47K bid = $724K) ≈ the entire whole-tape put premium
($737,595), so here the **top-N IS the tape** — this is a concentrated event, not the
"tip of the iceberg" case. Reconciles with phase-0.5: self_pctile_net_dir **0.0**
(most bearish day for CMPS in 49 sessions). [CTX:self_pctile DUCKDB]

### Sweeps (ask vs bid)

- **Ask-side:** 1 sweep — Jan-2028 $10 PUT, $667,944. [FLOW:sweeps ask]
- **Bid-side:** none (n=0). [FLOW:sweeps bid]
- All aggression is on the ask, all of it in the P10 LEAP. Ask-side **puts** =
  buyer paying up for downside → bearish/protective intent, not passive hedging.

### New positioning (unusual vol, vol/OI)

- Only one contract clears vol/OI ≥ 3: **Jan-2028 $10 PUT**, vol 2,011 / OI 144 =
  **13.97×** → unambiguously a new (opening) position. [FLOW:unusual_volume]

### Largest premium prints (top by premium)

| Time (ET) | Type | Strike | Expiry | Side | Premium | Size | Delta | IV |
|-----------|------|--------|--------|------|---------|------|-------|-----|
| 10:33 | PUT | 10 | 2028-01-21 | ask | $252,700 | 722 | −0.24 | 85% |
| 10:04 | PUT | 10 | 2028-01-21 | ask | $157,500 | 450 | −0.24 | 85% |
| 10:07 | PUT | 10 | 2028-01-21 | ask | $131,950 | 377 | −0.23 | 85% |
| 10:04 | PUT | 10 | 2028-01-21 | ask | $104,400 | 290 | −0.23 | 87% |
| 10:33 | PUT | 10 | 2028-01-21 | bid | $35,350 | 101 | −0.24 | 85% |
| 15:57 | CALL | 7 | 2026-06-18 | ask | $18,530 | 34 | 1.00 | 1586% |

(`executed_at` is UTC in raw JSON; converted to ET above. The 0DTE $7 calls at
15:57 ET with 940–1586% IV are expiring-day pin noise — discounted.)

### IV outliers + Greeks

- IV outliers are dominated by the 0DTE $7 call (IV 1155%) — pin noise; the rest are
  Aug-2026 contracts ~100–110%. [FLOW:iv_outliers]
- Greeks on the P10 LEAP: delta ≈ −0.24, gamma ≈ 0.024, **vega ≈ 0, theta ≈ 0** in
  the screener rounding — deep-OTM long-dated convexity, low per-contract delta.
  [FLOW:greek_screener]

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|------------------|--------------------------|-----------|
| `uw insights deep-dive --symbol CMPS --date 2026-06-18` | put_prem=$737,595, call_prem=$250,780, net_flow=−$595,149 ← `.uw_screener.bullish_premium-.bearish_premium`; P/C=1.364 ← `.uw_screener.put_call_ratio` | whole-tape |
| `uw options-flow sweeps --side ask --min-premium 100000` | 1 row, P10 LEAP $667,944 ← `.results[0].total_premium` | top-25 |
| `uw options-flow sweeps --side bid --min-premium 100000` | n=0 ← `.results\|length` | — |
| `uw options-flow unusual-volume --min-vol-oi-ratio 3` | P10 LEAP vol/OI=13.97 ← `.results[0].vol_oi_ratio` | top-25 |
| `uw options-flow top-premium-trades --top-n 25` | put/ask=$677,400 ← `group_by(option_type+side)\|map(premium)\|add`; net Δ-notional=−$411,388 ← `Σ(delta*size*100*underlying_price)` | top-25 |
| `uw options-flow iv-outliers --top-n 15` | 0DTE $7C IV=1155% (noise) ← `.results[].implied_volatility` | 4 rows |
| `uw options-flow greek-screener --sort-by premium` | put/ask size=1,951 vs call/ask 88 ← `group_by\|map(size)\|add` | 15 rows |
| `uw hot-chains sweep-persistence --days 5 --symbol CMPS` | consistency=0.2, sessions_in_top=1, prem=$706,934, dominant_direction="bullish" (MISLABEL) ← `.results[]` | 1 row |
| `uw hot-chains smart-money-flow --direction bullish/bearish` | no CMPS rows | — |
| `uw hot-chains sweep-ratio --min-sweep-ratio 0.3` | no CMPS rows | — |

## Tool errors

- `uw hot-chains sweep-persistence … --date 2026-06-18` → `Error: unknown flag: --date`.
  Re-ran without `--date` (trailing tool anchors to latest available date = 2026-06-18,
  which equals the as-of, so the result is correct for this run). Recorded per the
  known "trailing tools not as-of-flagged" caveat.

## DATA NOTE / CORRECTION

- `sweep_persistence.dominant_direction = "bullish"` **contradicts the contract-level
  reality** (ask-side PUT buying, net delta-notional −$411K). The tool appears to
  tag ask-side aggression as "bullish" without distinguishing puts. Trusting the
  contract-level read (bearish); flagged for phase-10 contradiction audit.

## Verdict for downstream phases

- **Bias from this phase:** **bearish** (single-position-driven).
- **Conviction:** **3 / 5** — direction is genuinely unusual (most-bearish self-history
  day, aggressive ask-side, new position) but it is *one* LEAP print on a small name,
  small in absolute $ (~$647K), with no multi-day persistence and a plausible
  hedge interpretation. Concentrated ≠ broad conviction.
- **Three things later phases must remember:**
  1. The whole bearish skew = **one Jan-2028 $10 LEAP put, ask-side, ~$647K**,
     delta −0.24, opening (vol/OI 14). Everything else is noise.
  2. It is **not persistent** (1 session, consistency 0.2) — treat as an event, not
     a campaign; re-check tomorrow's tape for follow-through.
  3. Could be **directional bearish OR a tail hedge** on a binary biotech — phase-2
     (dark pool) and phase-3 (OI) must resolve whether common is being sold under it.
- **Open questions:** Is dark pool confirming distribution (phase-2)? Is the P10 LEAP
  OI actually building or was today a one-print spike (phase-3)? Is there a known
  catalyst (trial readout / financing) behind a 19-month OTM put (phase-7b/7c)?
