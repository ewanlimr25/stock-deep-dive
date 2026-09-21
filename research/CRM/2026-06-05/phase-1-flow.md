# Phase 1 — Options Flow

**Ticker:** CRM
**As-of date:** 2026-06-05
**Generated:** 2026-06-06T15:58:00-04:00
**Upstream:** phase-0-intake.md (spot 185.66 close), phase-0.5-context.md (`[CTX:] unusual_verdict = BUSY_NAME_NORMAL_DAY` → this phase's confluence contribution capped at `+`)

## Summary

CRM's 2026-06-05 options tape is **direction-flat in aggregate with a structurally
bullish long-dated standout print stack and a contradicting 5-day bearish sweep
campaign**. Whole-tape: derived net_flow +$1.28M on $44.8M bullish+bearish premium
(noise-level), P/C 0.57, and the DuckDB aggressor cut puts customer net delta
ex-0/1DTE at ≈ **−$7M** — flat. The single most important print is a 975-contract
Jan-2027 195 **risk reversal** (sell put / buy call, ≈+$18.6M bullish delta
notional), set against persistent bearish sweeps (5/5 sessions, $211M) and
LEAP call *selling* — read: institutions are two-way, with one large player
positioning for upside above 195 into 2027 while shorter-tape pressure stays
bearish. Conviction is LOW (2/5); phase-0.5 already caps this phase at `+`.

## Key signals

- **Jan-2027 195 risk reversal, 975×975, 17:30:25Z, spot 186.71** — 195P sold at
  bid ($2.87M, Δ −0.483) + 195C bought at ask ($2.49M, Δ +0.535), same second,
  same size → synthetic long ≈ +99k shares (≈ +$18.6M delta notional) for a small
  net credit (~$0.38M). Single largest directional intent on the tape.
  `[FLOW:top_premium_trades]` `[FLOW:greek_screener]`
- **5-day bearish sweep persistence:** dominant_direction `bearish`, 5/5
  sessions_in_top, consistency_score 1.0, $211.13M total sweep premium —
  the multi-day aggressive tape leans SHORT. `[FLOW:sweep_persistence]` (trailing
  window anchored at latest=2026-06-05)
- **Whole-tape flat:** bullish_premium $23.02M vs bearish_premium $21.74M →
  derived net_flow **+$1.28M**; call vol 50,764 vs put vol 28,811 (P/C 0.57);
  customer net delta ex-0/1DTE ≈ −$7M. `[FLOW:insights_deep_dive]`
  `[FLOW:delta_notional DUCKDB]`
- **Fresh weekly upside opening:** Jun-12 187.5C (vol 939, OI 159, ratio 5.9,
  $404k) and Jun-12 190C (vol 2,388, OI 477, ratio 5.0, $819k) — new positions
  for next week, straddling the 6/11 ex-div. `[FLOW:unusual_volume]`
- **LEAP call supply:** Jan-2028 200C sold at bid $2.05M (473×), Jan-2028 150C
  sold at bid $705–830k (Δ 0.75), Aug-21 230C 500× at bid $225k — overwriting /
  upside-trimming against the RR's upside bet. `[FLOW:sweeps side=bid]`

## Detailed findings

### Whole-tape aggregate (read the top-N against this)

`[FLOW:insights_deep_dive .uw_screener]` (same call/block as phase-0.5):
call_premium $26.64M vs put_premium $21.02M; bullish $23.02M vs bearish $21.74M
→ **derived net_flow = +$1.28M** (no `net_flow` key in this block); call_volume
50,764 vs put_volume 28,811 (put_call_ratio 0.57); iv_rank 60.0; iv30d 0.450;
implied_move 0.56%/day. Top-25 prints below are the iceberg-tip of a ~$48M
two-sided tape — they must NOT be read as the tape's direction.

`[FLOW:aggressor_ex0dte DUCKDB]` (ex-0/1DTE, customer-perspective):

| Type | Ask (bought) | Bid (sold) | Net prem | Customer Δ-notional |
|---|---|---|---|---|
| Calls | $10.90M / 15,994 ct | $12.99M / 20,846 ct | −$2.09M (net sold) | +78M (ask) / −102M (bid) |
| Puts | $7.43M / 9,533 ct | $11.05M / 10,806 ct | −$3.62M (net sold) | −56M (ask) / +73M (bid) |

**Customer net delta ≈ −$7M — flat.** Both calls and puts are net *sold*: an
income/overwriting tape, not a directional one. DTE mix: LEAP call $11.59M vs
LEAP put $6.04M (long-dated is where the call premium lives); 8–45DTE balanced
(5.76 vs 5.81); 0-1DTE trivial (~$2.6M total — no pin-noise inflation today).

### Sweeps (ask vs bid)

Ask-side (≥$100k, top 25, n=25): biggest are **Jan-2027 195C $2.50M** (977),
Jul-17 190P $1.18M (907 — puts *bought*, bearish), Aug-21 195C $782k, Aug-21
190P $711k, Jul-17 195C $637k, Jan-2028 165P $577k. Mixed both ways.
Bid-side (n=25): **Jan-2027 195P $2.87M** (975 — puts *sold*, bullish leg of the
RR), Jan-2028 200C $2.05M (calls sold), Aug-21 190P $1.16M (puts sold),
Jan-2028 165P $835k (puts sold), Jan-2028 150C $830k (calls sold).
`[FLOW:sweeps]` Persistence: bearish-dominant 5/5 sessions, $211.13M
(`[FLOW:sweep_persistence]`). Market-wide sweep-ratio top-15: CRM absent.
Smart-money-flow top-10 bullish/bearish: **CRM absent both directions** — no
smart-money flow detected on this date (thresholds not loosened per skill rule).

### New positioning (vol ≫ OI)

n=5 rows ≥3× vol/OI `[FLOW:unusual_volume]`: Jun-12 190C (2,388 vol / 477 OI,
5.0×, $819k, IV 0.473); Jun-12 187.5C (939/159, 5.9×, $404k); Jun-12 177.5P
(665/191, 3.5×, $109k); Jul-02 145P (101/13, 7.8×, $2k — noise); 0DTE 192.5C
(3,378/899, 3.8× — expired worthless, spot closed 185.66). Fresh money is
buying *next week's* upside calls just above spot, into the 6/11 ex-div.

### Largest premium prints

| Time (UTC) | Type | Strike | Expiry | Premium | Side | Spot |
|---|---|---|---|---|---|---|
| 17:30:25 | put | 195 | 2027-01-15 | $2,871,375 | bid (sold) | 186.71 |
| 17:30:25 | call | 195 | 2027-01-15 | $2,491,125 | ask (bought) | 186.71 |
| 19:35:57 | call | 150 | 2028-01-21 | $705,240 | bid (sold) | 186.20 |
| 16:11:11 | put | 210 | 2026-06-12 | $283,360 | bid (sold, Δ −0.913 ITM) | 185.33 |
| 13:54:50 | call | 120 | 2026-07-24 | $277,600 | ask (bought) | 188.66 |
| 13:54:50 | call | 120 | 2026-07-17 | $276,600 | bid (sold) | 188.66 |
| 15:55:05 | put | 190 | 2026-07-17 | $260,000 | bid (sold) | 185.53 |
| 13:49:32 | call | 230 | 2026-08-21 | $225,000 | bid (sold) | 189.96 |

Structural reads: rows 1–2 = the bullish risk reversal; rows 5–6 = deep-ITM 120C
calendar roll (stock-replacement rolled Jul-17→Jul-24, Δ 0.97 — neutral,
maintenance); row 4 = deep-ITM put sale (bullish-leaning); rows 3/8 = upside call
supply. `[FLOW:top_premium_trades]`

### IV outliers + Greeks

IV outliers: n=1 — 0DTE 180C at IV 1.18 ($31k, 57 vol) — expiry-day noise, no
vol-event signal. `[FLOW:iv_outliers]` Greek screener (sorted by premium)
confirms the RR legs (Δ −0.483/+0.535, vega 0.58 — vega-neutral-ish combo) and
shows the Jan-2028 200C sale carried the tape's largest vega (0.92/contract)
— long-dated vol *supply*. `[FLOW:greek_screener]`

## Tool calls

| Command | jq path | Status |
|---|---|---|
| `uw options-flow sweeps --symbol CRM --side ask --min-premium 100000 --top-n 25 --date 2026-06-05 --json` | `.results[] {option_type,strike,expiry,total_premium,total_size,side}` | ok n=25 |
| `uw options-flow sweeps --side bid …` | same | ok n=25 |
| `uw options-flow unusual-volume --symbol CRM --min-vol-oi-ratio 3 --top-n 25 --date 2026-06-05 --json` | `.results[] {total_volume,open_interest,vol_oi_ratio,total_premium,avg_iv}` | ok n=5 |
| `uw options-flow top-premium-trades --symbol CRM --top-n 25 --date 2026-06-05 --json` | `.results[] {executed_at,premium,side,underlying_price}` | ok n=25 |
| `uw options-flow iv-outliers --symbol CRM --top-n 15 --date 2026-06-05 --json` | `.results[]` | ok n=1 |
| `uw options-flow greek-screener --symbol CRM --top-n 15 --sort-by premium --date 2026-06-05 --json` | `.results[] {premium,side,delta,vega,size}` (first attempt mis-pathed `avg_*` → nulls; re-ran with correct paths) | ok n=15 |
| `uw hot-chains smart-money-flow --direction bullish/bearish --top-n 10 --min-volume 500 --date 2026-06-05 --json` | filter ticker==CRM | ok — CRM absent both |
| `uw hot-chains sweep-persistence --days 5 --top-n 20 --symbol CRM --json` | `.results[0]` | ok (see Tool errors: no `--date` flag) |
| `uw hot-chains sweep-ratio --top-n 15 --min-volume 500 --min-sweep-ratio 0.3 --date 2026-06-05 --json` | filter ticker==CRM | ok — CRM absent |
| DuckDB §A aggressor/delta-notional + DTE buckets | `lib/duckdb-cuts.md §A` | ok |

## Tool errors

- `uw hot-chains sweep-persistence --days 5 --top-n 20 --symbol CRM --date 2026-06-05 --json` →
  `Error: unknown flag: --date`. Re-ran without `--date`; the trailing window
  anchors to the latest available session, which IS 2026-06-05 (phase-0 UW
  availability), so the 5-day window is point-in-time correct for this run.

## Verdict for downstream

- **Net bias: MIXED** (aggregate flat; one large long-dated bullish structure vs
  5-day bearish sweep persistence and LEAP call supply)
- **Conviction: 2/5** — magnitude is normal-for-the-name (`[CTX:]` cap applies),
  aggregate delta ≈ flat; the RR is one player, not a tape.
- **Three datapoints to remember:**
  1. Jan-2027 195 risk reversal 975× (sell 195P $2.87M bid / buy 195C $2.49M ask,
     17:30:25Z) ≈ +$18.6M bullish delta into 2027 — strongest single intent.
  2. Bearish sweep persistence 5/5 sessions, $211.13M, consistency 1.0 — the
     aggressive short-tape has NOT capitulated post-earnings.
  3. Customer net delta ex-0/1DTE ≈ −$7M on ~$45M premium; both calls AND puts
     net sold `[FLOW:aggressor_ex0dte DUCKDB]` — income tape, not directional.
- **Open questions:** Is dark pool accumulating or distributing under this flat
  options tape (phase 2)? Are the Jan-2028 call sales overwrites against
  existing long OI or naked vol supply (phase 3 OI by strike)? Does 190–195
  show up as a dealer gamma wall pinning next week's 187.5/190 weekly buyers
  (phase 4)?
