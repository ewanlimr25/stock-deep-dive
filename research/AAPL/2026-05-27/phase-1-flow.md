# Phase 1 — Options Flow

**Ticker:** AAPL
**As-of date:** 2026-05-27
**Generated:** 2026-05-28T02:56:00Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md

## Summary

The headline reads bullish — call premium is **11.5x put premium** ($742M vs
$65M) and AAPL ranks 9th in the universe on net bullish flow — but the read
**dissolves on inspection**. Bullish vs bearish premium is near-balanced
($198M vs $180.5M, net only **+$17.4M**), call ask-side volume fraction is just
**0.53** (below the 0.6 bullish-signature bar), and the single largest position
(7/2 310C, $27.7M, vol/OI 85) is split **~50/50 ask vs bid** — spread/two-way,
not clean accumulation. Sweep-persistence confirms AAPL is in the top sweep names
**5/5 sessions but `dominant_direction = mixed`**. **Net: a mildly bullish lean
on a busy mega-cap having a normal two-way day — low directional conviction**,
consistent with phase-0.5's `BUSY_NAME_NORMAL_DAY`.

## Key signals

- Whole-tape net flow **+$17.4M bullish** but bullish/bearish premium near-balanced
  ($197.95M / $180.54M); call ask-frac **0.53**, put ask-frac 0.47 `[FLOW:insights_deep_dive]`
- Largest new position: **7/2 310C, $27.7M premium, vol 28,454 vs OI 334 (vol/OI 85)** —
  but ask-side $13.9M ≈ bid-side $13.6M → two-way/spread, not directional `[FLOW:sweeps]` `[FLOW:unusual_volume]`
- Sweep persistence: AAPL in top sweeps **5/5 sessions, dominant_direction = MIXED**,
  $1.155B 5-day sweep premium `[FLOW:sweep_persistence]`
- Largest-premium contracts by greeks: deep-ITM **9/18 calls (delta 0.62–0.84,
  stock-replacement)** + long-dated **12/2027 puts (340P/265P, high vega — protective)** `[FLOW:greek_screener]`
- **No AAPL rows in smart-money-flow top-50 (either direction)** and not in
  sweep-ratio top-50 → no concentrated smart-money imbalance `[FLOW:smart_money_flow]`

## Detailed findings

### Whole-tape aggregate (read top-N against this)

| Field | Value |
|-------|-------|
| call_premium | $741.92M |
| put_premium | $64.77M |
| **bullish_premium** | **$197.95M** |
| **bearish_premium** | **$180.54M** |
| **net_flow (bull−bear)** | **+$17.42M** |
| put_call_ratio | 0.373 |
| call_volume / put_volume | 853,971 / 318,504 |
| call ask-side fraction | **0.53** (369,047 ask / 326,708 bid) `[FLOW:insights_deep_dive DUCKDB]` |
| put ask-side fraction | 0.47 (134,930 ask / 152,161 bid) |

The 11.5x call/put **premium** ratio is a busy-name artifact: when you net
aggressor direction, the tape is near-balanced (+$17.4M, ~9% bull tilt) and the
ask/bid volume split is barely bullish (0.53). This is precisely the phase-0.5
`BUSY_NAME_NORMAL_DAY` signature — **the top-N prints below must not be read as a
one-sided bullish tape.**

### Sweeps (ask vs bid — the mirror is the story)

| Strike/Type | Expiry | Ask-side $ | Bid-side $ |
|-------------|--------|-----------|-----------|
| 310 C | 2026-07-02 | $13.95M | $13.65M |
| 310 C | 2026-06-18 | $5.28M | $7.30M |
| 312.5 C | 2026-05-29 | $4.47M | $4.71M |
| 312.5 C | 2026-05-27 (0DTE) | $5.10M | $3.53M |
| 300 C | 2026-06-18 | $10.23M (ask only top) | — |

The top ask-side and top bid-side prints are the **same 7/2 310 strike at nearly
identical size** — calls bought and sold in the same line. This is market-making /
vertical-spread footprint, not one-directional conviction. A clean 300C 6/18
$10.2M ask-side print exists, but it sits atop a balanced book.

### New positioning (unusual vol, vol/OI ≥ 3)

- **7/2 310C — vol 28,454, OI 334, vol/OI 85, $27.7M** → genuinely new, the day's
  largest fresh line (but two-way per above).
- **5/27 312.5P (0DTE) — vol 30,548, OI 265, $3.8M** → 0DTE pin noise, discount.
- A ladder of tiny 0DTE deep-ITM calls (235C/255C/245C/240C, vol/OI 60–196) — pin/
  expiry mechanics, immaterial premium.

### Largest premium prints + Greeks

Greek screener (by premium) is dominated by:
- **Deep-ITM 9/18 calls**: 260C (Δ0.84), 285C (Δ0.72), 300C (Δ0.62) — high-delta
  **stock-replacement / synthetic long** structures (institutional, slow, not a
  short-term catalyst bet). Top-premium-trades tagged these `no_side` (complex/mid).
- **Long-dated 12/2027 puts**: 340P (Δ−0.57, vega 1.53), 265P (Δ−0.24, vega 1.22) —
  high-vega LEAP puts, read as **protective/collar legs**, not directional bearish
  intent (phase-3/4 to confirm against OI).

### IV outliers

Nothing material — top IV contract is a 5/29 260C at IV 1.41 on $848k premium; the
rest are <$1k premium dust. **No IV-driven directional signal.**

## Tool calls (audit trail)

| Command | Result summary |
|---------|----------------|
| `uw insights deep-dive --symbol AAPL --date 2026-05-27` | whole-tape aggregate (net +$17.4M, P/C 0.373) |
| `uw options-flow sweeps --side ask --min-premium 100000` | 25 rows, call-led but mirrored on bid |
| `uw options-flow sweeps --side bid --min-premium 100000` | 25 rows, calls also sold (310C 7/2 $13.6M) |
| `uw options-flow unusual-volume --min-vol-oi-ratio 3` | 7/2 310C new (vol/OI 85, $27.7M) standout |
| `uw options-flow top-premium-trades --top-n 15` | 9/18 calls + 12/2027 protective puts |
| `uw options-flow iv-outliers --top-n 10` | no material signal |
| `uw options-flow greek-screener --sort-by premium` | deep-ITM stock-replacement calls; LEAP puts |
| `uw hot-chains sweep-persistence --days 5 --symbol AAPL` | 5/5 sessions, dominant_direction MIXED, $1.155B |
| `uw hot-chains smart-money-flow --direction bullish/bearish` | **no AAPL rows in top-50** |
| `uw hot-chains sweep-ratio --top-n 50` | no AAPL rows in top-50 |
| DuckDB §A (ask/bid volume split) | call ask-frac 0.53, put ask-frac 0.47 |

## Tool errors

- `uw hot-chains sweep-persistence … --date 2026-05-27` → `Error: unknown flag:
  --date`. **Cause:** sweep-persistence is a trailing multi-day tool that anchors
  to the latest available date (per memory `uw-cli-mcp-parity`). Re-run **without
  `--date`** succeeded; as-of (2026-05-27) == latest, so the result is valid for
  this run. Not as-of-reproducible on a backdated run.

## Verdict for downstream

- **Bias from this phase:** mixed / mildly-bullish (net +$17.4M, ~9% tilt; heavily
  qualified by two-way structure).
- **Conviction:** **2/5** — the bullish headline is a premium-ratio artifact; net
  direction and ask/bid split are weak, the marquee print is two-way, and
  persistence is explicitly "mixed."
- **Three things later phases must remember:**
  1. Net directional flow is only **+$17.4M** (call ask-frac 0.53) — *not* a
     conviction bullish tape despite the 11.5x call/put premium ratio.
  2. The **7/2 310C ($27.7M, vol/OI 85)** is the one fresh institutional line to
     track — but it printed ~50/50 ask/bid (spread, not accumulation).
  3. Long-dated 12/2027 **protective puts** (340P/265P) present — phase-3/4 must
     check whether these are hedges/collars against the deep-ITM call longs.
- **Open questions for downstream:**
  - Is dark pool (phase-2) confirming accumulation, or is the underlying also
    two-way? (If DP is balanced too → no real positioning.)
  - Does OI (phase-3) show the 7/2 310C and 9/18 calls as *building* longs or as
    spread legs?
  - Phase-0.5 cap stands: **phases 1–2 confluence capped at `+`** given
    `BUSY_NAME_NORMAL_DAY`.
