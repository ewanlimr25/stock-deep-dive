# Phase 4 — Dealer Structure & Gamma

**Ticker:** CRM
**As-of date:** 2026-06-05
**Generated:** 2026-06-06T16:18:00-04:00
**Upstream:** phase-3-positioning.md (call-supply 190–220, put walls 185/180,
6/18 OPEX cliff 25.13%; open question: "where does dealer gamma flip?"),
phase-2-dark-pool.md (overhead DP shelves 189/201/210; spot 185.66 close)

## Summary

Dealers are in a **negative-gamma regime at and below spot with long-gamma
pockets overhead** — the most explosive-to-the-downside configuration on the
board. The tool's headline regime is `FULLY_NEGATIVE` ("strong gamma
amplification", total GEX −3.33M), driven by a dominant **−$13.34M GEX at the
185 strike** (exactly spot); but the per-strike cross-check shows *positive*
GEX at 195/200/210/220 — dealers are long the calls the street sold (phase-3's
overwrites), so rallies into 195–200 get dampened while breaks below 185 get
amplified. Net DEX says the dealer hedge is to **SELL underlying** (net −$67.2M
public delta). Skew is **COMPLACENT** (25Δ calls *richer* than puts, ratio
0.943) and the front-end is **backwardated** (7d/30d IV 1.111) with no earnings
until 9/02 — the market is paying up for near-dated movement while ignoring
tail risk. The one upward force: **max pain sits ABOVE spot** at every near
expiry (6/12 → 192.5, 6/18 → 190), giving OPEX gravity a +2.3–3.6% pull.

## Key signals

- **GEX regime `FULLY_NEGATIVE` — "All strikes have negative net GEX — strong
  gamma amplification"; total −3,333,998; `zero_gamma_level: null`.**
  Cross-check tension (surfaced, not hidden): per-strike shows positive GEX at
  195 (+3.86M), 200 (+6.72M), 210 (+2.46M), 220 (+2.64M) vs deeply negative
  185 (−13.34M), 182.5 (−1.94M), 170 (−2.17M), 165 (−2.11M). Functional flip
  zone ≈ **190–195**: short-gamma below, long-gamma pockets above.
  `[STRUCT:gex]`
- **DEX: dealer hedge = SELL.** call_dex +$1.082B, put_dex −$1.149B, net
  **−$67.18M**; tool interpretation verbatim: "Public is net put-long → dealers
  net short puts → dealer hedge is to SELL underlying." `[STRUCT:dex]`
- **Skew COMPLACENT:** 25Δ call IV 0.4619 > 25Δ put IV 0.4354 (skew −0.0265,
  ratio 0.943, dte_actual 34) — upside still bid, zero tail-hedge demand after
  a −11% four-day fade. `[STRUCT:term_skew]`
- **Front-end BACKWARDATION without an event:** near IV (6 DTE) 0.5173 vs far
  (26 DTE) 0.4656, ratio **1.111** — stress premium in next week's options;
  next earnings 2026-09-02 (phase-0.5), so this is fade-vol, not event-vol.
  `[STRUCT:front_end_iv_ratio]`
- **Max pain pulls UP:** 6/12 → **192.5** (+3.63%), 6/18 (monthly cliff) →
  **190** (+2.29%), 6/26 → 185, 7/02 → 190. Static-OI caveat quoted below.
  `[STRUCT:max_pain]`

## Detailed findings

### GEX `[STRUCT:gex --dte-max 45]`

Total GEX **−3,333,998**; regime `FULLY_NEGATIVE`; ZGL null (tool found no
crossing). Largest per-strike magnitudes:

| Strike | GEX | Side of spot |
|---|---|---|
| **185** | **−13,339,085** | at spot (−0.41%) |
| 200 | +6,724,586 | +7.67% |
| 195 | +3,862,496 | +4.98% |
| 220 | +2,644,563 | +18.44% |
| 210 | +2,459,156 | +13.05% |
| 170 | −2,166,847 | −8.48% |
| 165 | −2,108,869 | −11.1% |
| 182.5 | −1,937,243 | −1.7% |

Read with phase-3: the positive pockets are exactly the strikes where fresh OI
was *sold* (dealers long those calls → long gamma there); the negative mass at
185/182.5/170/165 is the put OI dealers are short. **Below 185 every move gets
amplified by dealer hedging; the regime label's "all strikes negative" wording
overstates — the per-strike table is the operative map.**

### DEX `[STRUCT:dex --dte-max 45]`

net_dex −$67,184,938 (call +1,082,153,810 / put −1,149,338,748), spot field
186.15 (parquet EOD spot; close 185.66). Interpretation verbatim: "Public is
net put-long → dealers net short puts → dealer hedge is to SELL underlying."

### Vanna + charm `[STRUCT:vanna_charm --dte-max 45]`

net_vanna −1,832 (call_vanna −9,465, put_vanna +7,632); net_charm +88,195.
Tool interpretation verbatim: "Public net vanna negative (call-heavy book).
Falling IV → call delta drops → dealers (short calls) cut long-underlying
hedge → SELLING pressure. Rising IV reverses." With IV30d at 0.450 (iv_rank 60,
phase-0.5) and the post-event fade, the base case is IV *bleed* → **vanna flow
is a daily mechanical seller** as long as price chops/declines. No squeeze
setup (needs positive vanna + falling IV + negative dealer delta).

### IV term structure `[STRUCT:iv_term_structure]`

`structure: CONTANGO`. Curve (avg_iv by expiry): 6/12 51.7% → 6/18 49.6% →
6/26 47.7% → 7/02 46.6% → 7/10 45.3% → 7/17 45.9% → 7/24 45.3% (0DTE 6/05 row
7.6% is an expiry-day artifact, ignored). Smooth decay — contango overall with
an elevated front week, which is what the 7v30 ratio picks up as
backwardation. Kinked-front contango, normalizing by July.

### Term skew `[STRUCT:term_skew --dte-target 30]`

25Δ put 0.4354 vs 25Δ call 0.4619 → skew −0.0265, skew_ratio 0.943,
`interpretation: COMPLACENT` (dte_actual 34). Calls richer than puts after a
−11% fade = the chain still prices upside chase, not crash protection.

### Front-end IV ratio `[STRUCT:front_end_iv_ratio --near-dte 7 --far-dte 30]`

near_iv 0.5173 (6 DTE) / far_iv 0.4656 (26 DTE) = **1.111 → BACKWARDATION**.
No earnings inside the window (next 2026-09-02) — this is realized-vol chasing
(ATR expansion 8.27→9.60, phase-0 drift), not event pricing. Pitfall rule
checked: earnings were 5/28, >24h before as-of, so the backwardation is not a
normalizing post-print artifact — it has persisted through four fade sessions.

### Today's gamma flip

Skipped — `today-gamma-flip` is 0DTE/intraday-only and this run executes
after the session (as-of EOD snapshot). Noted per phase guidance.

### Max pain `[STRUCT:max_pain --dte-max 30]`

Tool caveat verbatim: "Single-day OI snapshot. Max pain assumes settlement at
each candidate strike with current open interest unchanged to expiry."

| Expiry | Max pain | Dist from spot | put_call_oi_ratio |
|---|---|---|---|
| 2026-06-05 (expired) | 190 | +2.29% | 0.337 |
| **2026-06-12** | **192.5** | **+3.63%** | 0.483 |
| **2026-06-18** (OPEX cliff) | **190** | **+2.29%** | 0.494 |
| 2026-06-26 | 185 | −0.41% | 0.513 |
| 2026-07-02 | 190 | +2.29% | 0.873 |

Agrees with phase-3's wall map (190 battleground, 195/200 walls above): the
chain's pin gravity for the next two weeks is **190 ± 2.5** — above spot.
Tension to resolve downstream: max-pain pull UP vs short-gamma amplification
DOWN below 185. The 6/26+7/02 rows show the magnet decaying toward spot
(185–190) as the cliff passes.

## Tool calls

| Command | jq path | Status |
|---|---|---|
| `uw options-structure gex --symbol CRM --dte-max 45 --date 2026-06-05 --json` | `.regime/.regime_description/.zero_gamma_level/.total_gex/.per_strike[]` | ok |
| `uw options-structure dex --symbol CRM --dte-max 45 --date 2026-06-05 --json` | `.net_dex/.call_dex/.put_dex/.interpretation` | ok |
| `uw options-structure vanna-charm --symbol CRM --dte-max 45 --date 2026-06-05 --json` | `.net_vanna/.net_charm/.vanna_interpretation` | ok |
| `uw options-structure iv-term-structure --symbol CRM --date 2026-06-05 --json` | `.structure/.term_structure[] {expiry,dte_approx,avg_iv}` (first pass mis-pathed `.atm_iv` → nulls; re-ran with `.avg_iv`) | ok |
| `uw options-structure term-skew --symbol CRM --dte-target 30 --date 2026-06-05 --json` | `.skew/.skew_ratio/.interpretation` | ok |
| `uw options-structure front-end-iv-ratio --symbol CRM --near-dte 7 --far-dte 30 --date 2026-06-05 --json` | `.ratio/.regime/.near_iv/.far_iv` | ok |
| `uw options-structure today-gamma-flip` | — | skipped (intraday-only; run is post-session) |
| `uw options-structure max-pain --symbol CRM --dte-max 30 --date 2026-06-05 --json` | `.rows[] {expiry,max_pain,distance_pct,put_call_oi_ratio}` + `.caveat` | ok n=5 |

## Tool errors

None fatal. Two extraction notes: (1) GEX `regime_description` ("All strikes
have negative net GEX") is contradicted by its own `per_strike` payload
(positive GEX at 195/200/210/220) — both quoted above, per-strike treated as
operative; (2) iv-term-structure rows first extracted with wrong field names
(nulls), re-pulled with `.avg_iv` — all quoted values round-tripped through jq
on the corrected pass.

## Verdict for downstream

- **Dealer regime: SHORT GAMMA at/below spot (amplification), long-gamma
  pockets 195–220 (dampening). Transitional band 190–195.** Dealer delta hedge
  pressure: SELL. Vanna: mechanical seller while IV bleeds.
- **Conviction: 4/5** on the regime map (large, unambiguous per-strike masses);
  3/5 on the net-direction implication (max-pain pull conflicts).
- **Structural levels for phase-9:**
  1. **185 = the gamma trigger** (−$13.3M GEX, largest mass on the board, at
     spot). Below it dealers chase price down; phase-2 shows a DP air pocket
     to ~176 underneath.
  2. **195–200 = dealer long-gamma + call-wall + DP-shelf confluence**
     (+$3.9M/+$6.7M GEX, net OI +8.9k/+22.0k ≤30DTE, $415M DP at 201) — the
     rally-sale zone.
  3. **Max-pain magnet 190–192.5 into 6/12 and 6/18 OPEX** (+2.3–3.6% above
     spot) — the opex-gravity counterweight; decays to 185–190 by 6/26–7/02.
- **Open questions:** Historically, when CRM sits short-gamma below max-pain
  into a monthly OPEX, does the magnet or the amplification win (phase 5
  analogs)? Is the complacent skew + backwardated front-end a repeatable
  pre-breakdown signature for this name (phase 5)? Does the macro tape
  (phase 6) supply the IV direction that decides the vanna flow's sign?
