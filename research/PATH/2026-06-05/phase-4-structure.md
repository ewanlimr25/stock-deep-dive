# Phase 4 — Dealer Structure & Gamma

**Ticker:** PATH
**As-of date:** 2026-06-05
**Generated:** 2026-06-06T10:45:00-04:00
**Upstream phases cited:** phase-0.5-context.md, phase-1-flow.md, phase-3-positioning.md

## Summary

Dealers are **net long gamma** (≤45DTE total_gex **+$4,446,767**, regime
`POSITIVE`: "Dealers net long gamma — expect mean-reversion and reduced
volatility", ZGL **7.57** far below spot 11.25) — but the surface is lumpy:
the **$11 strike carries −$7.52M net GEX** (the one destabilizing strike,
exactly phase-3's put-wall/battleground) with stabilizing positive-GEX bands
at $12 (+$4.09M) and $13 (+$4.64M). Skew is **inverted/"COMPLACENT"** (25Δ
calls 72.1% vs puts 60.7% — upside is what's bid, consistent with a 31%
short-float squeeze-option market). Max pain pins the front expiries at
**$11–$12**. The headline front-end `BACKWARDATION` (ratio 1.797) is
**artifact-suspect** — the 06/12 expiry's avg_iv 162.1% is polluted by the
deep-ITM HTB lines phase-1 flagged.

## Key signals

- Total GEX +$4,446,767, regime `POSITIVE`, `zero_gamma_level` **7.57** vs
  spot 11.25 → long-gamma, mean-reversion regime [STRUCT:gex]
- Per-strike GEX: **$11 = −$7,522,428** (negative-gamma pocket at spot);
  $12 +$4,092,079 / $13 +$4,637,229 overhead dampeners [STRUCT:gex]
- DEX: call_dex $43,686,381 / put_dex −$22,952,199 → net_dex **+$20,734,182**;
  tool verbatim: "Public is net call-long → dealers net short calls → dealer
  hedge is to BUY underlying." [STRUCT:dex]
- Term skew (26 DTE actual): put_25d_iv 0.6071 vs call_25d_iv 0.7206 → skew
  **−0.1135**, skew_ratio 0.842, interpretation **`COMPLACENT`** — calls
  richer than puts (inverted) [STRUCT:term_skew]
- Max pain: 06/12 → **$12** (+6.81%, P/C OI 1.144); 06/18 (the 15.9% OPEX
  cliff, phase-3) → **$11** (−2.09%, P/C 0.356) [STRUCT:max_pain]

## Detailed findings

### GEX

Regime `POSITIVE` (+$4.45M ≤45DTE), ZGL 7.57 (treat as ±2% band; tool notes
GEX is coarse on non-mega-cap names). Top strikes by |net_gex|:

| strike | net_gex | character |
|---|---|---|
| 11 | −7,522,428 | destabilizing magnet AT spot |
| 13 | +4,637,229 | dampener |
| 12 | +4,092,079 | dampener |
| 14 | +2,219,318 | dampener |
| 15 | +1,907,753 | dampener |
| 10 | −1,702,250 | destabilizing below |

Read: range-stabilizing book overhead ($12–$15), negative pocket at $11/$10 —
a decisive break under $11 puts spot into accelerating territory (dealers add
to the move), while rallies into 12–13 get sold by hedgers. Mirrors phase-3's
$11 put-wall battleground (net_oi −12,197) and $12/$13 call walls.

### DEX

net_dex +$20.73M (call-skewed public book). Dealer inverse hedge = structural
**buy-underlying** bias — a modest mechanical tailwind while the call-long
public book persists [STRUCT:dex].

### Vanna + charm

net_vanna **−1,831** (call_vanna −3,213 / put_vanna +1,382), net_charm
+93,016. Tool verbatim: "Public net vanna negative (call-heavy book). Falling
IV → call delta drops → dealers (short calls) cut long-underlying hedge →
SELLING pressure. Rising IV reverses." [STRUCT:vanna_charm]
**No squeeze setup**: the classic vanna-squeeze needs positive vanna +
falling IV; here IV *decline* produces dealer selling — i.e. post-earnings
vol crush is a mild *headwind* via hedge unwind.

### IV term structure

`structure: CONTANGO` [STRUCT:iv_term_structure]. Per-expiry avg_iv: 06/18
77.7% → Sep/LEAPs lower (front > back only at the 06/12 node). The **06/12
avg_iv 162.1%** (1,437 contracts) is distorted by the deep-ITM $5/$5.5/$6
weeklies whose quoted IVs print 540–570% (phase-1-flow.md §IV outliers) —
not a real event hump.

### Term skew

COMPLACENT / inverted: calls 11.35 vol pts richer than puts at 25Δ
(skew_ratio 0.842, dte_actual 26). Upside-chasing demand + cheap downside —
typical of crowded-short names where the feared move is *up*. Cross-ref
phase-7c short-interest gate.

### Front-end IV ratio

near_iv (6 DTE) 1.6209 vs far_iv (26 DTE) 0.9019 → ratio **1.797**, regime
`BACKWARDATION` [STRUCT:front_end_iv_ratio]. **Flagged artifact-suspect**:
same 06/12 contamination as above; phase-0.5's whole-name iv30d was 64.7%
with iv_rank 40 — no event before earnings 2026-09-03. Do not trade this
"stress" signal.

### Today's gamma flip (0DTE book, as-of session)

Retrospective EOD read of the 06/05 0DTE book (expired same day —
informational only): regime `NEGATIVE`, today_total_gex −3,180,919,
today_zero_gamma 9.56, atm_flip 7.5; key wall $11 gex −5,695,983
(`resistance_wall`) [STRUCT:today_gamma_flip]. Confirms the $11 strike was
the 0DTE battleground into the close (spot closed 11.24).

### Max pain (≤30DTE; tool caveat verbatim: "Single-day OI snapshot. Max pain
assumes settlement at each candidate strike with current open interest
unchanged to expiry.")

| expiry | max_pain | dist % | put_call_oi_ratio |
|---|---|---|---|
| 2026-06-12 | **12.0** | +6.81 | 1.144 |
| 2026-06-18 | **11.0** | −2.09 | 0.356 |
| 2026-06-26 | 11.5 | +2.36 | 1.471 |
| 2026-07-02 | 11.0 | −2.09 | 0.336 |

Near-term gravity: **$11–$12**. The Jun-18 OPEX cliff (15.9% of chain OI,
phase-3-positioning.md §term structure) pins at $11 — chain gravity is *at or
slightly below* spot into the monthly, then $12 pull on the 06/12 weekly.
Consistent with the oi-by-strike walls; no disagreement to resolve.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw options-structure gex --symbol PATH --dte-max 45 --date 2026-06-05 --json` | regime POSITIVE, ZGL 7.57, total +4,446,767 ← `.regime/.zero_gamma_level/.total_gex`; strikes ← `.per_strike[].net_gex` | full surface |
| `uw options-structure dex --symbol PATH --dte-max 45 --date 2026-06-05 --json` | net_dex +20,734,182 ← `.net_dex`; interpretation verbatim | aggregate |
| `uw options-structure vanna-charm --symbol PATH --dte-max 45 --date 2026-06-05 --json` | net_vanna −1,831; charm +93,016 ← `.net_vanna/.net_charm` | aggregate |
| `uw options-structure iv-term-structure --symbol PATH --date 2026-06-05 --json` | CONTANGO ← `.structure`; 06/12 avg_iv 1.6209 ← `.term_structure[].avg_iv` | 15 expiries |
| `uw options-structure term-skew --symbol PATH --dte-target 30 --date 2026-06-05 --json` | COMPLACENT, skew −0.1135 ← `.interpretation/.skew` | 26 DTE |
| `uw options-structure front-end-iv-ratio --symbol PATH --near-dte 7 --far-dte 30 --date 2026-06-05 --json` | ratio 1.797 BACKWARDATION ← `.ratio/.regime` | 2 nodes |
| `uw options-structure today-gamma-flip --symbol PATH --date 2026-06-05 --json` | 0DTE gex −3,180,919, zg 9.56 ← `.today_total_gex/.today_zero_gamma` | 0DTE book |
| `uw options-structure max-pain --symbol PATH --dte-max 30 --date 2026-06-05 --json` | 06/18 mp 11.0 ← `.results[]{max_pain,distance_pct}` | 5 expiries |

## Tool errors

None fatal. First GEX jq assumed `.gex` per-strike key and a non-null `total`
(`jq: error … null (null) number required`) — no values transcribed; re-ran
with `del(.per_strike)` probe then `.net_gex`. First iv-term-structure jq
guessed `.atm_iv // .iv` (nulls) — rows actually carry `avg_iv`; re-read.

## DATA NOTE / CORRECTION

- GEX per-strike field is `net_gex` (not `gex`); top-strike table re-verified
  against `sort_by(-(.net_gex*.net_gex))`.
- iv-term-structure per-row field is `avg_iv`; 06/12 = 1.6209 re-verified.

## Verdict for downstream phases

- **Dealer regime:** **long gamma** (total +$4.45M, spot 11.25 ≫ ZGL 7.57) —
  mean-reversion/range regime, with one destabilizing negative-GEX pocket at
  $11/$10 and dealer buy-underlying delta bias (+$20.7M net DEX)
- **Conviction:** 3/5 (signals internally consistent; GEX coarse on this name,
  front-end vol metrics contaminated)
- **Structural levels for phase-9:**
  1. **ZGL 7.57** (deep-crash reference only; ±2% band) — the operative
     trigger is the **$11 negative-GEX strike**: below it dealers amplify
  2. **$12–$13 positive-GEX dampener band** (+$4.1M/+$4.6M) = sold-rally zone,
     matches phase-3 call walls and phase-2 $11.83–$12.06 DP supply
  3. **Max-pain magnets: 06/12 → $12; 06/18 OPEX cliff → $11** — chain
     gravity says spot oscillates $11–$12 into Jun OPEX
- **Open questions:** Is the inverted skew (calls 11 pts over puts) crowded
  squeeze speculation or informed positioning (phase 7c SI/borrow read)? Does
  vol crush continue (vanna says crush = mechanical selling pressure)?
