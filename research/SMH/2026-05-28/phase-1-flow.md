# Phase 1 — Options Flow

**Ticker:** SMH
**As-of date:** 2026-05-28
**Generated:** 2026-05-29T12:10:00Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md

## Summary

The whole-tape aggregate is **net bearish/put-skewed** — put premium $131.5M vs
call premium $86.7M, bullish $76.2M vs bearish $97.2M, **net flow −$21.0M**, P/C
ratio **7.26** `[FLOW:insights_deep_dive]`. But the *structure* of that skew is
hedging, not conviction-short: the bearish weight is concentrated in **near-term
(8–45 DTE) puts ($82.9M vs $28.8M calls, ~3:1)**, while the **46–180 DTE and LEAP
buckets are balanced-to-call-favored**, and the net options delta-notional is only
**≈ −$0.38bn** against a $68B AUM ETF `[FLOW:delta_notional DUCKDB]`. The marquee
print is the **550P 06-05 (8DTE) at $24.08M ask** — an ~8%-OTM near-term tail hedge
(delta −0.137). Per phase-0.5's `[CTX:]`, this is a **BUSY_NAME_NORMAL_DAY on size**
(total premium only 51.5 self-pctile) with a genuinely-unusual *directional skew*, so
magnitude conviction is capped at `+`.

## Key signals

- **Marquee:** 550P 06-05 (8DTE) **$24.08M ask-side** sweep vs $10.88M bid (net
  ~$13M aggressive put BUYING), delta −0.137 — near-term tail hedge `[FLOW:sweeps]`.
- **Likely collar:** 635C 09-18 **$7.36M** + 575P 09-18 **$6.89M** (same expiry,
  near-equal premium, both opening) — long downside put / short upside call,
  classic hedge-into-strength `[FLOW:top_premium_trades]`.
- **June put accumulation:** 565P 06-26 $6.9M (vol/OI 49.9), 530P 06-26 $3.4M
  (vol/OI 21.7), 590P 06-12 $2.3M — all new positions opening `[FLOW:unusual_volume]`.
- **Net put buying:** puts $59.2M bought (ask) vs $40.6M sold (bid); calls net
  slightly *sold* ($31.0M ask vs $33.5M bid = overwriting) `[FLOW:aggressor_ex0dte DUCKDB]`.
- **Persistent but mixed:** SMH a top-sweep name **5 of last 5 sessions**, $561.5M
  total sweep premium, **dominant_direction = mixed**, consistency_score 1
  `[FLOW:sweep_persistence]`. No smart-money-flow signal either direction.

## Detailed findings

### Whole-tape aggregate (read top-N against this)

| Field | Value |
|-------|-------|
| call_premium | $86.7M |
| put_premium | **$131.5M** |
| bullish_premium | $76.2M |
| bearish_premium | $97.2M |
| **net_flow** | **−$21.0M** |
| call_volume / put_volume | 48,362 / 351,344 |
| **put_call_ratio** | **7.26** |
| IV rank / IV30d | 84.6 / 0.462 |

Source: `uw insights deep-dive` `uw_screener` block `[FLOW:insights_deep_dive]`.
The tape is genuinely put-skewed (not a top-N artifact) — confirmed by the DuckDB
aggressor split below.

### Aggressor & delta-notional split (ex-0DTE) `[FLOW:aggressor_ex0dte DUCKDB]`

| Type | Side | Prem $M | Δ-notional $bn |
|------|------|---------|----------------|
| call | ask (bought) | 31.03 | +0.244 |
| call | bid (sold) | 33.51 | +0.268 |
| put | **ask (bought)** | **59.22** | **−0.923** |
| put | bid (sold) | 40.61 | −0.572 |

Net customer delta-notional ≈ **−$0.38bn** (net short via options) — modest for a
$68B ETF. Calls net *sold* (overwriting); puts net *bought*. Reads as a collar/hedge
overlay, not a directional short.

### Premium by DTE bucket × type `[FLOW:delta_notional DUCKDB]`

| DTE bucket | call $M | put $M | read |
|-----------|---------|--------|------|
| 0–1DTE | 4.67 | 5.52 | pin noise |
| **2–7DTE / 8–45DTE** | 28.75 | **82.93** | **near-term puts dominate ~3:1 (June protection)** |
| 46–180DTE | 37.17 | 31.63 | balanced, slight call lean (collar + 500P 07-17) |
| LEAP | 16.14 | 11.48 | slight call lean — structural upside intact |

The bearish/hedge weight is **all in the front (June) tenor**; medium/long tenor is
balanced-to-bullish. Holders keep upside, buy near-term insurance.

### Sweeps (ask vs bid)

Ask-side dominated by puts: **550P 06-05 $24.08M**, 565P 06-26 $3.35M, 560P 12-18
$2.56M, 590P 06-12 $2.16M, 530P 06-26 $1.80M; upside calls smaller (655C 06-26
$2.04M, 580C 06-26 $1.69M, 600C 09-18 $1.17M). Bid-side: 550P 06-05 $10.88M (offsets
the ask) plus calls being sold (640C 07-17 $2.61M, 570C 06-26 $1.95M, 580C 06-18
$1.72M) `[FLOW:sweeps]`.

### New positioning (vol/OI ≥ 3)

Opening puts dominate: 565P 06-26 (vol 3,740 / OI 75, **vol/OI 49.9**), 530P 06-26
(vol 3,758 / OI 173, 21.7), 560P 12-18 (26.2), 480P 12-18 (22.0), 575P 09-18 (7.5,
$6.9M). One sizeable opening call: 655C 06-26 ($2.04M, vol/OI 20.5) `[FLOW:unusual_volume]`.
(Dozens of 0DTE 255–422 strike puts at IV 2–3.5 are penny tail/pin noise — ignored.)

### Largest premium prints

| Type | Strike | Expiry | Prem | Side |
|------|--------|--------|------|------|
| call | 635 | 2026-09-18 | $7.36M | no_side |
| put | 575 | 2026-09-18 | $6.89M | no_side |
| put | 500 | 2026-07-17 | $3.56M | no_side |
| call | 760 | 2026-07-17 | $3.12M | no_side |
| call | 640 | 2026-07-17 | $2.58M | bid (sold) |
| put | 590 | 2026-06-12 | $2.06M | ask (bought) |
| call | 570 | 2026-06-26 | $1.93M | bid (sold) |

The 635C/575P 09-18 pair (near-equal premium, same expiry, both opening per
unusual-volume) is the collar; the rest is June put buying + call overwriting.

### IV outliers + Greeks

IV outliers are all worthless deep-OTM 0DTE puts (255–422 strikes, IV 2.0–3.5, ~$0
premium) — pin noise, no signal `[FLOW:iv_outliers]`. Greek screener: 550P 06-05
delta −0.137 (tail hedge), 575P 09-18 delta −0.383, 635C 09-18 delta +0.468,
590P 06-12 delta −0.407 `[FLOW:greek_screener]`.

## Tool calls (audit trail)

| Command | Result summary |
|---------|----------------|
| `uw insights deep-dive --symbol SMH --date 2026-05-28` | aggregate: put-skew, net −$21M, P/C 7.26 |
| `uw options-flow sweeps --symbol SMH --side ask/bid --min-premium 100000` | 550P 06-05 $24M ask dominant |
| `uw options-flow unusual-volume --symbol SMH --min-vol-oi-ratio 3` | opening puts: 565P/530P 06-26, 575P 09-18 |
| `uw options-flow top-premium-trades --symbol SMH` | 635C/575P 09-18 collar, June puts |
| `uw options-flow iv-outliers --symbol SMH` | only 0DTE pin-noise puts |
| `uw options-flow greek-screener --symbol SMH --sort-by premium` | 550P 06-05 Δ−0.137 tail hedge |
| `uw hot-chains smart-money-flow --direction bullish/bearish` | no SMH rows either direction |
| `uw hot-chains sweep-persistence --days 5 --symbol SMH` | 5/5 sessions, $561.5M, **mixed** |
| `uw hot-chains sweep-ratio --min-sweep-ratio 0.3` | SMH outside top-50 |
| DuckDB §A (aggressor ex-0DTE + DTE buckets) | net put buying, Δ−0.38bn, June puts 3:1 |

## Tool errors

- `uw hot-chains sweep-persistence … --date 2026-05-28` → `Error: unknown flag:
  --date`. Re-run without `--date`; it anchors to the latest available date, which
  IS the as-of (2026-05-28), so the result is reproducible for this run.

## Verdict for downstream

- **Net bias from this phase:** bearish/hedged (near-term), but the *intent* reads
  **protective hedging into strength**, not directional conviction short.
- **Conviction:** **2/5** on a directional-bearish read (capped by the phase-0.5
  BUSY_NAME size flag + mixed sweep direction + modest −$0.38bn net delta). The
  *hedging* read itself is higher-conviction (3–4/5).
- **Three things later phases must remember:**
  1. The bearish skew is **concentrated in 8–45 DTE (June) puts ($82.9M, 3:1 over
     calls)**; 46–180D and LEAP are balanced-to-call-favored — protection tenor,
     not a structural short.
  2. **550P 06-05 $24M (net ~$13M bought, Δ−0.137)** is the single most important
     print — an 8-DTE tail hedge. Phase-3 OI shows the 530P 06-05 +50,795 OI build;
     resolve whether this is one desk's basket hedge or broad protection.
  3. Calls net *sold* (overwriting) + puts net *bought* + likely **635C/575P 09-18
     collar** = classic collar overlay; net options delta only −$0.38bn.
- **Open questions:** Is dark pool (phase-2) showing accumulation or distribution at
  ~$599? Does OI (phase-3) confirm the 530P/550P/565P puts are *opening* (hedge
  build) vs closing? Does structure (phase-4) GEX put the dealer short gamma below
  spot (which would amplify any down-move the hedgers are protecting against)?
