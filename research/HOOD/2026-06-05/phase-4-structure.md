# Phase 4 — Dealer Structure & Gamma

**Ticker:** HOOD
**As-of date:** 2026-06-05
**Generated:** 2026-06-07T12:42:00-04:00
**Upstream phases cited:** phase-1-flow.md, phase-3-positioning.md

## Summary

HOOD closed the week in a **short-gamma regime**: the tool labels `regime` =
"NEGATIVE — Dealers net short gamma — expect trend acceleration and increased
volatility", with `zero_gamma_level` **87.45** vs underlying 81.81 — spot is
~6.5% *below* the flip, so dealers amplify moves in both directions. The
vol surface is two-faced: 30-day skew is **COMPLACENT** (25Δ puts at 67.4% IV
vs calls 71.7% — calls *richer* than puts, no downside fear priced) while the
front end is in **BACKWARDATION** (5-DTE IV 77.7% vs 33-DTE 70.0%, ratio 1.11)
— near-term movement priced without an earnings event (next: 2026-07-29).
Max-pain gravity splits the next two expiries: Jun-12 magnet **83** (+0.6%
above spot) but the heavy Jun-18 OPEX (21.39% of OI, phase-3) magnet sits at
**80** (−3.0%) — the chain's biggest expiry pulls price *down* into June 18.

## Key signals

- **Short gamma**: `regime`="NEGATIVE", `zero_gamma_level`=87.45, underlying
  81.81 → spot 6.5% below ZGL; moves get amplified, not damped [STRUCT:gex]
- **Largest positive GEX strike = 90** (net_gex +9.16M; then 100 +5.62M, 85
  +4.81M, 95 +4.51M) — same 85/90/95/100 geography as phase-3's call walls;
  **negative GEX pockets at 82 (−2.06M) and 75 (−2.13M)** — air pockets where
  dealer hedging chases price [STRUCT:gex]
- **DEX**: call_dex +$1.175B vs put_dex −$0.685B → net_dex +$490M;
  `interpretation` verbatim: "Public is net call-long → dealers net short calls
  → dealer hedge is to BUY underlying" — but the mirror is mechanical *selling*
  if calls are unwound or IV falls [STRUCT:dex]
- **Vanna**: net_vanna −5,953; verbatim: "Falling IV → call delta drops →
  dealers (short calls) cut long-underlying hedge → SELLING pressure. Rising IV
  reverses." Charm +308,333 — time-decay flows lean supportive into expiry
  [STRUCT:vanna_charm]
- **Jun-18 max-pain 80** (−3.0% from spot 82.47, P/C OI 0.536, total_oi
  391,214) vs Jun-12 max-pain 83 (+0.6%) [STRUCT:max_pain]
- **Skew COMPLACENT**: skew −0.0429, skew_ratio 0.94 — put protection is
  *cheap* relative to calls [STRUCT:term_skew]

## Detailed findings

### GEX [STRUCT:gex] (dte ≤45)

- `total_gex` 32,578,652 · `zero_gamma_level` **87.45** · underlying 81.81 ·
  `regime` **NEGATIVE** (label quoted verbatim, not re-derived)
- Top |net_gex| strikes: 90 (+9.16M), 100 (+5.62M), 85 (+4.81M), 95 (+4.51M),
  86 (+3.53M), 80 (+2.86M), 105 (+2.62M), **75 (−2.13M)**, **82 (−2.06M)**,
  83 (+1.98M)
- Read: positive-gamma shelf 83–90 above spot (dealers pin/resist there);
  negative pockets at 82 and 75 — below 82 dealer hedging *adds* to downside
  until the 80 strike's +2.86M, then 75 is another air pocket. Tool's own
  note: GEX most meaningful for deep-OI large caps — HOOD qualifies
  (2.1M total OI), treat ZGL as ±2% band per rubric.
- ⚠ underlying_price quoted by gex/dex/vanna = 81.81/81.80 (intraday parquet
  last) vs official close 82.47 — levels read against both.

### DEX [STRUCT:dex]

`call_dex` +1,175,292,384 · `put_dex` −685,261,891 · `net_dex` +490,030,493
(Σ delta×OI×100×spot). Public net call-long → dealers short calls → dealers
hold a long-stock hedge. Mechanical risks: (a) falling IV or (b) call OI
unwind ⇒ dealers shed that long hedge = downside accelerant — this is the
structural mirror of phase-1's call-selling tape.

### Vanna + charm [STRUCT:vanna_charm] (dte ≥1 filtered)

`net_vanna` −5,953 (call_vanna −12,128 / put_vanna +6,175) · `net_charm`
+308,333. Verbatim interpretation quoted in Key signals. No squeeze setup:
the classic vanna squeeze needs positive vanna + negative dealer delta; here
the geometry is the *reverse* — IV decline is a sell-flow trigger, IV spike a
buy-flow trigger. Charm positive: as Jun-18 OPEX decays, dealer re-hedging
leans mildly supportive *if* spot holds near the call-heavy strikes.

### IV term structure [STRUCT:iv_term_structure]

`structure` = **CONTANGO** (kink_expiry null, 21 expiries) — but the curve is
humped at the front: Jun-12 77.7% / Jun-18 78.3% / Jun-26 75.6% / Jul-02 71.5%
/ Jul-10 70.0%, then **Aug-21 75.7%** (the 2026-07-29 earnings bump — Jul-24
70.5% is the last pre-earnings expiry) settling ~74–76% long-dated. The 0DTE
row (8.6%) is an expired-contract artifact, ignored.

### Term skew [STRUCT:term_skew] (dte_target 30 → actual 33)

`put_25d_iv` 0.6744 < `call_25d_iv` 0.7174 → `skew` −0.0429, `skew_ratio` 0.94,
`interpretation` = **COMPLACENT**. Calls are the bid side of the vol surface —
speculative upside demand, zero tail-hedging premium. Notable *against*
phase-1's bearish tape: whoever is selling stock/calls is NOT paying up for
puts.

### Front-end IV ratio [STRUCT:front_end_iv_ratio]

near (5 DTE) 0.7772 / far (33 DTE) 0.6999 → `ratio` **1.11**, `regime` =
**BACKWARDATION**. Event-stress pricing with no earnings inside the window —
the market prices continued near-term realized movement (consistent with the
short-gamma regime), not a discrete catalyst.

### Today's gamma flip

Skipped — 0DTE intraday tool; this is an as-of (T+2) run, not a live session.

### Max pain [STRUCT:max_pain] (dte ≤30; static-OI caveat quoted: "assumes
settlement at each candidate strike with current open interest unchanged")

| Expiry | DTE | max_pain_strike | distance_pct | P/C OI | total_oi |
|---|---|---|---|---|---|
| 2026-06-05 | 0 | 83 | +0.64% | 0.402 | 271,016 (expired) |
| 2026-06-12 | 7 | **83** | +0.64% | 0.451 | 95,898 |
| **2026-06-18** | 13 | **80** | **−3.0%** | 0.536 | **391,214** |
| 2026-06-26 | 21 | 80 | −3.0% | 0.456 | 28,054 |
| 2026-07-02 | 27 | 85 | +3.07% | 0.469 | 19,469 |

Cross-check vs phase-3: Jun-18 = the 21.39% OPEX cliff ✓; magnet 80 sits in
phase-3's two-sided 80 battleground, below the 83–90 positive-GEX shelf.
Near-term gravity: flat-to-+0.6% into Jun-12, then **down-3% into Jun-18**.
Far max pain is indicative only (static-OI softness).

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw options-structure gex --symbol HOOD --dte-max 45 --date 2026-06-05 --json` | ZGL 87.45, regime NEGATIVE ← `.zero_gamma_level, .regime`; strikes ← `.per_strike \| sort_by(-(.net_gex\|fabs))[:10]` | 50 strikes |
| `uw options-structure dex --symbol HOOD --dte-max 45 --date 2026-06-05 --json` | net_dex +490,030,493 ← `.net_dex`; verbatim `.interpretation` | summary |
| `uw options-structure vanna-charm --symbol HOOD --dte-max 45 --date 2026-06-05 --json` | net_vanna −5,953 / net_charm +308,333 ← `.net_vanna, .net_charm`, `.vanna_interpretation` | summary |
| `uw options-structure iv-term-structure --symbol HOOD --date 2026-06-05 --json` | CONTANGO ← `.structure`; hump ← `.term_structure[].avg_iv` | 21 expiries |
| `uw options-structure term-skew --symbol HOOD --dte-target 30 --date 2026-06-05 --json` | COMPLACENT, ratio 0.94 ← `.interpretation, .skew_ratio, .put_25d_iv, .call_25d_iv` | summary |
| `uw options-structure front-end-iv-ratio --symbol HOOD --near-dte 7 --far-dte 30 --date 2026-06-05 --json` | BACKWARDATION 1.11 ← `.regime, .ratio, .near_iv, .far_iv` | summary |
| `uw options-structure max-pain --symbol HOOD --dte-max 30 --date 2026-06-05 --json` | table ← `.results[] \| {expiry, max_pain_strike, distance_pct, put_call_oi_ratio}` | 5 expiries |
| `uw options-structure today-gamma-flip` | SKIPPED — intraday/0DTE-only, as-of run | — |

## Tool errors

(none)

## DATA NOTE / CORRECTION

gex/dex/vanna tools quote underlying 81.81/81.80 (parquet intraday last);
max-pain and screener quote close 82.47. Distances stated against the source
quoted in each section; the discrepancy (~0.8%) is inside the ZGL ±2% band and
does not change any regime call.

## Verdict for downstream phases

- **Dealer regime:** **short gamma** (spot ~6.5% below ZGL 87.45) — moves
  amplify; combined with net-long dealer stock hedge (+$490M DEX) whose unwind
  triggers are falling IV or call-OI liquidation. Fragile-to-downside
  structure despite complacent skew.
- **Conviction:** 4 (regime labels are tool-native and mutually consistent;
  softened only by the GEX large-cap caveat and the 81.81-vs-82.47 price gap)
- **Structural levels for phase-9:**
  1. **ZGL 87.45** (±2% band) — above it, regime flips to mean-reversion;
     natural thesis-invalidation line
  2. **Largest GEX strike 90** (+9.16M, with the 85/86 shelf first) — dealer
     resistance; matches phase-3 call walls
  3. **Negative-GEX air pockets 82 → 80 → 75** — below 82 hedging accelerates
     toward the Jun-18 max-pain magnet **80**, then 75 (put wall + −2.13M GEX)
  4. **Jun-18 max-pain 80** — the OPEX-gravity target 13 days out
- **Open questions:** Does realized vol (phase 5) confirm the backwardation's
  implied movement? Is the complacent skew a contrarian red flag if phase 6's
  regime is risk-off? What catalyst (phase 6 news) breaks the 80–87 dealer
  range, given short gamma cuts both ways?
