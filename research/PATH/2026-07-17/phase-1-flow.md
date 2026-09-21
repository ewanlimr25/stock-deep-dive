# Phase 1 — Options Flow

**Ticker:** PATH · **As-of:** 2026-07-17 · **Version:** v1
Cites: phase-0.5-context.md `[CTX:] unusual_verdict = QUIET`; phase-0-intake.md
(options anchor 2026-07-17).

## Summary

Today's PATH options tape is **near-balanced with a mild bullish undertone**, and
must be read through phase-0.5's `QUIET` verdict — this is a low-tradeability day,
not a signal day. Whole-tape aggregate: call premium $2.35M vs put premium $2.53M,
bullish $2.17M vs bearish $1.98M → **derived net_flow +$0.18M** (marginally
bullish), P/C 0.55 with call volume (27.0k) ~1.8× put volume (14.9k) — cheap OTM
call lottery tickets against slightly heavier put *premium*. The single largest
structure of the day — a **two-sided Sep-18 $13 put** (~$1.06M ask + ~$1.02M bid,
nearly symmetric, ≈40% of the day's total premium) — is **not directional** (a
roll / spread-leg / two-way market-making print, not a conviction bet). The one
genuinely bullish tell is **multi-day**: `sweep-persistence` shows PATH in the top
sweep tape **5 of 5 sessions, consistency 1.0, dominant bullish, $6.19M cumulative**,
and today's real directional prints are **deep-ITM long-dated LEAP calls**
(stock-replacement).

## Key signals

- **5-day bullish sweep campaign** — `sessions_in_top=5, consistency_score=1.0,
  dominant_direction=bullish, total_sweep_premium=$6.19M` `[FLOW:sweep_persistence]`.
  The strongest single item in this phase; the slow bid the daily tape hides.
- **Two-sided Sep-18 $13P — NON-directional** — ask $1.06M (5,366 ct / 570 trades /
  avg $1.98) vs bid $1.02M (5,174 ct / 555 trades / avg $1.97). Near-perfect
  symmetry = roll/spread/MM, ≈40% of day premium; **do not read as bearish**
  `[FLOW:sweeps]`.
- **Deep-ITM LEAP calls = bullish stock-replacement** — Dec'28 $3C $100k (δ0.96),
  Jan'28 $3C $95.5k (δ0.97), Mar'27 $8C $51.5k (δ0.85), Jan'28 $8C $45.4k (δ0.84).
  Small size, high delta, long dated = patient synthetic-long `[FLOW:greek_screener]`.
- **Whole-tape near-balanced** — net_flow +$0.18M, put premium > call premium,
  P/C 0.55 `[FLOW:insights_deep_dive]`. Magnitude tiny vs tape leaders (NVDA +$82M).
- **No smart-money-flow rows** for PATH either direction at min-volume 500
  `[FLOW:smart_money_flow]` — the name is below the cross-sectional smart-money bar.

## Detailed findings

### Whole-tape aggregate `[FLOW:insights_deep_dive]`
| Field | Value |
|---|---|
| call_premium | $2,347,678 |
| put_premium | $2,533,829 |
| bullish_premium | $2,166,017 |
| bearish_premium | $1,984,094 |
| **net_flow (derived bull−bear)** | **+$181,923** (marginally bullish) |
| call_volume / put_volume | 27,044 / 14,947 |
| put_call_ratio | 0.553 |
| iv_rank | 44.5 · iv30d 67.5% |
Read the top-N below *against* this: net_flow is small and put premium slightly
exceeds call premium, so the tape is **not** cleanly bullish on the day —
the bullish read is the 5-day persistence, not today's dollars.

### Sweeps (ask vs bid) `[FLOW:sweeps]`
Only ONE contract clears the $100k sweep bar, and it prints on **both** sides:
| Side | Contract | Premium | Size | Trades | Avg px |
|---|---|---|---|---|---|
| ask | PATH 2026-09-18 $13 PUT | $1,064,182 | 5,366 | 570 | $1.98 |
| bid | PATH 2026-09-18 $13 PUT | $1,021,114 | 5,174 | 555 | $1.97 |
Near-identical size/price both sides → two-way flow (roll or spread), **not a
directional bearish put buy**. This strike sits just above spot (~$12.14) and
expires two weeks after the 2026-09-03 earnings — earnings-cycle put real estate.

### New positioning (unusual vol/OI) `[FLOW:unusual_volume]`
9 rows, all small: Jul-31 $18C (vol 150/OI 1, $330 — lottery), Aug-28 $11C
(135/1), Jul-24 $12.5P (401/42, vol/OI 9.5 — the only mid-size new put),
Aug-28 $15C (264/37). Nothing institutional-sized; consistent with QUIET.

### Largest premium prints `[FLOW:top_premium_trades]`
| Type | Strike | Expiry | Premium | Side |
|---|---|---|---|---|
| call | $3 | 2028-12-15 | $100,000 | mid |
| call | $3 | 2028-01-21 | $95,500 | mid |
| call | $8 | 2027-03-19 | $51,500 | ask |
| call | $8 | 2028-01-21 | $45,360 | ask |
| put | $12 | 2028-12-15 | $43,000 | bid |
| call | $12 | 2027-01-15 | $31,080 | ask |
The premium leaderboard is **long-dated low-strike CALLS** (bullish
stock-replacement), sides mixed but the ask-side $8C prints are genuine buys.
The lone put (Dec'28 $12P bid $43k, δ−0.25) is a small long-term hedge.

### IV outliers + Greeks `[FLOW:iv_outliers, greek_screener]`
IV-outlier rows are **all 0DTE** (2026-07-17 expiry) low-strike calls — expiring-day
pin noise, IV null; **discount entirely**. Greek-screener premium leaders are the
LEAP calls above: Dec'28 $3C (δ0.96/γ0.005), Jan'28 $3C (δ0.97), $8C 2027/2028
(δ0.84–0.85) — high-delta synthetic longs — plus Dec'28 $12P (δ−0.25) and
Jan'27 $12C (δ0.64).

## Tool calls
| Tool | Args | Result |
|---|---|---|
| options-flow sweeps | --symbol PATH --side ask --min-premium 100000 --date 2026-07-17 | 1 row (Sep13P) |
| options-flow sweeps | --symbol PATH --side bid --min-premium 100000 --date 2026-07-17 | 1 row (Sep13P) |
| options-flow unusual-volume | --symbol PATH --min-vol-oi-ratio 3 --date 2026-07-17 | 9 rows, all small |
| options-flow top-premium-trades | --symbol PATH --top-n 25 --date 2026-07-17 | LEAP calls lead |
| options-flow iv-outliers | --symbol PATH --top-n 15 --date 2026-07-17 | all 0DTE noise |
| options-flow greek-screener | --symbol PATH --sort-by premium --date 2026-07-17 | LEAP calls δ0.84–0.97 |
| hot-chains smart-money-flow | --direction bullish/bearish --min-volume 500 --date 2026-07-17 | no PATH rows |
| hot-chains sweep-persistence | --days 5 --symbol PATH (trailing, anchors 2026-07-17) | 5/5, bullish, $6.19M |

## Tool errors
- `hot-chains sweep-persistence … --date 2026-07-17` → `Error: unknown flag: --date`.
  This trailing-window tool takes no `--date`; re-ran without it. Latest available
  date == as-of (2026-07-17, phase-0), so the trailing window is reproducible.

## Verdict for downstream

- **Net bias: mildly bullish** — driven by the 5-day persistence campaign
  (bullish, consistency 1.0) + deep-ITM LEAP call accumulation, NOT by today's
  balanced dollars. Today alone reads neutral.
- **Conviction: 2 / 5** — the persistence is genuine but the daily tape is QUIET
  (phase-0.5), magnitude tiny vs the universe, and the biggest single print is
  explicitly non-directional. Real but slow; short-term tradeability low.
- **Three datapoints later phases must remember:**
  1. **$6.19M / 5-of-5-session bullish sweep persistence, consistency 1.0** — the
     slow accumulation signal; corroborate against dark pool (phase 2) and OI (phase 3).
  2. **Sep-18 $13P two-sided ~$2.09M** is a roll/MM, **not** a bearish bet — do not
     let phase-8 bears cite it as put buying.
  3. **Directional intent = long-dated low-strike CALLS (δ0.84–0.97)**; positioning
     is patient/institutional, not a fast momentum sweep.
- **Open questions:** Is the $267M dark-pool block (phase-0.5) confirming this slow
  bullish bid — accumulation, or distribution at $12? Does OI (phase-3) show the
  Sep $13P as opening (new hedge) or closing (roll)? Does the Nov-16C OI build
  (+4,255, phase-0.5) belong to the same LEAP-call buyer?
