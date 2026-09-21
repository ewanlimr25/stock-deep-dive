# Phase 4 — Dealer Structure & Gamma

**Ticker:** IREN
**As-of date:** 2026-06-05
**Generated:** 2026-06-07T01:10Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md

## Summary

Dealers are **short gamma in a deep pit exactly where spot sits**: every strike
from 44 to 59 carries negative net GEX (54: **−$30.7M**, 55: −$15.9M, 50:
−$7.4M), positive gamma only appears at 60+ (70: +$3.6M), and total_gex =
**−$64.79M** with spot 54.23 [STRUCT:gex]. The practical flip sits at
**~59.5–60** (sign change between 59 and 60 on the per-strike surface) — note
the tool's own `regime: "POSITIVE"` label and `zero_gamma_level: 5.12`
contradict its negative total and surface; flagged below, the per-strike signs
are the tradeable read. Dealer delta hedging adds pressure: net DEX −$253.6M,
"dealer hedge is to SELL underlying" [STRUCT:dex]. The front end is stressed —
6d IV 130.2% vs 34d 110.1% (ratio 1.182, regime **BACKWARDATION**)
[STRUCT:front_end_iv_ratio] — yet 30d skew is **inverted ("COMPLACENT"): 25Δ
calls 113.5% vs puts 107.1%** — the market still pays up for upside, no crash
panic [STRUCT:term_skew]. This regime explains today's −9% flush + V-recovery
(phase-1 underlying path): short gamma amplifies both directions. Max pain:
06/18 monthly magnet at **55** (+1.1% from spot), agreeing with phase-3's 55
put-heavy battleground; 06/12 max pain 61 [STRUCT:max_pain].

## Key signals

- **Short-gamma pit 44–59, deepest at 54/55** (−$30.7M/−$15.9M net_gex);
  positive gamma starts at 60 — moves inside 48–59 get amplified, 60+ gets
  pinned [STRUCT:gex per_strike].
- **Net DEX −$253,615,527** (call_dex +$501.0M, put_dex −$754.6M): "Public is
  net put-long → dealers net short puts → dealer hedge is to SELL underlying"
  (verbatim interpretation) [STRUCT:dex].
- **Front-end backwardation: ratio 1.182** (near 6d 130.2% / far 34d 110.1%)
  — event-stress pricing in the 06/12 week, consistent with the fresh 50P/55P
  hedge builds (phase-3-positioning.md §Largest OI increases) [STRUCT:front_end_iv_ratio].
- **Inverted 30d skew, "COMPLACENT"**: skew −0.0637 (ratio 0.944) — 25Δ calls
  RICHER than puts after a −18% week; upside speculation intact, tail-hedge
  demand muted [STRUCT:term_skew].
- **Max pain 06/18 = 55** (distance +1.14%, P/C OI 0.859, 315,927 OI) — the
  monthly magnet sits at the phase-1 short-strangle strike and phase-3 ATM
  put-heavy battleground; 06/12 max pain = 61 (+12.2%, P/C OI 3.431 pulling it
  above spot) [STRUCT:max_pain].

## Detailed findings

### GEX [STRUCT:gex] (dte≤45)

- `total_gex` = **−$64,788,860**; underlying 54.23; 50 strikes returned
  (per-strike sum −$69.96M ≈ total).
- Tool labels: `regime: "POSITIVE"` / "Dealers net long gamma — expect
  mean-reversion and reduced volatility"; `zero_gamma_level: 5.12`. **Internal
  contradiction flagged**: a −$64.8M total with an all-negative 44–59 surface
  is short gamma at spot by the tool's own numbers; the 5.12 ZGL is a
  degenerate lowest-crossing artifact (label likely derives from spot > ZGL).
  Quoted verbatim per guidance; per-strike signs used for the level map only.
- Surface (near spot): 48 −$0.96M · 50 −$7.41M · 52 −$4.71M · 53 −$2.84M ·
  **54 −$30.72M** · **55 −$15.94M** · 56 −$2.89M · 57/58/59 ≈ −$1.1–1.3M each ·
  **60 +$2.39M** · 64 +$1.11M · 65 +$1.75M · **70 +$3.59M**.
- Tradeable flip band: **59.5–60** (first persistent sign change; ±2% coarse
  per pitfalls). Below ~59.5 dealers amplify; above 60 they dampen.

### DEX [STRUCT:dex] (dte≤45)

call_dex +$500,956,765 · put_dex −$754,572,292 · **net_dex −$253,615,527**.
Verbatim: "Public is net put-long → dealers net short puts → dealer hedge is
to SELL underlying." Mechanical sell-pressure overhang while the front-week
put wall (phase-3) stays open.

### Vanna + charm [STRUCT:vanna_charm] (dte≤45)

net_vanna −31 (call_vanna −4,855 vs put_vanna +4,824 — offsetting), net_charm
−133,630. Verbatim: "Public net vanna negative (call-heavy book). Falling IV →
call delta drops → dealers (short calls) cut long-underlying hedge → SELLING
pressure. Rising IV reverses." With front-end IV at 130% post-flush, **vol
crush on a calm-down would mechanically pressure the stock** (vanna), while
charm decay into 06/12 bleeds the put hedges' delta support. No squeeze setup:
vanna is net ~zero, not positive.

### IV term structure [STRUCT:iv_term_structure]

Label: `structure: "CONTANGO"`, `kink_expiry: null`. Rows (avg_iv): 06/12
**130.2%** → 06/18 121.3% → 06/26 113.5% → 07/02 111.3% → 07/10 110.1% →
07/17 113.5% → 08/21 113.9% → 09/18 115.6%. **Label/data tension flagged**:
the listed front end (06/12 → 07/10) is downward-sloping = backwardation; the
"CONTANGO" label appears anchored on the expired 06/05 row (20.7%, dte −1, a
post-expiry artifact). The minimum of the curve is 07/10 (110.1%) with a
gentle rise after — net shape: **stressed-front backwardation flattening into
a mild long-dated contango**.

### Term skew (30d target, 26d actual) [STRUCT:term_skew]

put_25d_iv 1.0713 vs call_25d_iv 1.135 → skew **−0.0637**, skew_ratio 0.944,
interpretation verbatim: **"COMPLACENT"**. Calls over puts after a −18% week =
speculative upside demand persists (consistent with phase-3's 110C LEAP builds
and phase-1's $339.9M bullish sweep persistence).

### Front-end IV ratio [STRUCT:front_end_iv_ratio]

near_iv 1.302 (6d) / far_iv 1.1013 (34d) → **ratio 1.182, regime
"BACKWARDATION"**. Event-stress: the market prices the next 1–2 weeks as the
risk window (no earnings until 2026-08-27 per phase-0.5 — this is positioning/
news stress, not earnings).

### Today's gamma flip

Skipped — `today-gamma-flip` is 0DTE-intraday only and this is an EOD as-of
run (per phase guidance).

### Max pain [STRUCT:max_pain] (dte≤30; static-OI caveat quoted: "assumes
settlement at each candidate strike with current open interest unchanged")

| Expiry | DTE | max_pain | dist % | P/C OI | total OI |
|---|---|---|---|---|---|
| 2026-06-05 | 0 | 62 | +14.0 | 1.256 | 305,132 (expired tonight) |
| 2026-06-12 | 7 | **61** | +12.2 | 3.431 | 172,842 |
| **2026-06-18** | 13 | **55** | **+1.1** | 0.859 | 315,927 |
| 2026-06-26 | 21 | 59 | +8.5 | 1.565 | 28,330 |
| 2026-07-02 | 27 | 61 | +12.2 | 2.312 | 16,728 |

The tradeable magnet is **06/18 @ 55** (largest near OI, 1.1% away) —
reinforcing the 55 pin thesis (phase-3 battleground + phase-1 strangle). The
06/12 61 magnet is soft (P/C 3.43 = put-OI-dragged, and spot is 12% below);
read it as "the put side, not price, is expected to expire worthless," i.e.
put writers win if the stock merely stops falling.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw options-structure gex --symbol IREN --dte-max 45 --date 2026-06-05 --json` | total_gex=−64,788,860 ← `.total_gex`; 54 strike −30,715,711 ← `.per_strike[]\|select(.strike==54).net_gex`; regime label + ZGL=5.12 verbatim | 50 strikes |
| `uw options-structure dex --symbol IREN --dte-max 45 --date 2026-06-05 --json` | net_dex=−253,615,527 ← `.net_dex`; interpretation verbatim | aggregate |
| `uw options-structure vanna-charm --symbol IREN --dte-max 45 --date 2026-06-05 --json` | net_vanna=−31, net_charm=−133,630 ← `.net_vanna/.net_charm` | aggregate |
| `uw options-structure iv-term-structure --symbol IREN --date 2026-06-05 --json` | structure="CONTANGO" ← `.structure`; 06/12 avg_iv=1.302 ← `.term_structure[1].avg_iv` | 19 expiries |
| `uw options-structure term-skew --symbol IREN --dte-target 30 --date 2026-06-05 --json` | skew=−0.0637, interpretation="COMPLACENT" ← `.skew/.interpretation` | 1 |
| `uw options-structure front-end-iv-ratio --symbol IREN --near-dte 7 --far-dte 30 --date 2026-06-05 --json` | ratio=1.182, regime="BACKWARDATION" ← `.ratio/.regime` | 1 |
| `uw options-structure max-pain --symbol IREN --dte-max 30 --date 2026-06-05 --json` | 06/18 max_pain_strike=55, distance_pct=1.14 ← `.results[2]` | 5 expiries |

## Tool errors

(none — two label/data inconsistencies documented, not tool failures:
`gex.regime="POSITIVE"`+`zero_gamma_level=5.12` vs `total_gex=−64.79M`;
`iv-term-structure.structure="CONTANGO"` vs backwarded 06/12→07/10 front end
anchored by an expired-row artifact.)

## Verdict for downstream phases

- **Dealer regime:** **SHORT GAMMA at spot** (44–59 negative pit, total
  −$64.8M, net DEX −$253.6M sell-hedge) flipping LONG above ~60. Moves are
  amplified inside 48–59; rallies stall into 60–65 positive gamma + the
  phase-2 61–62 DP shelf.
- **Conviction:** 4/5 on the regime read (surface is one-sided and deep;
  docked one for the tool's self-contradictory labels).
- **Three structural levels for phase-9:**
  1. **~59.5–60 = gamma flip + first positive-GEX strike + 06/12 max-pain 61
     just above** — the regime-change line; longs get dealer help only above it.
  2. **54–55 = deepest negative GEX (−$46.7M combined) + 06/18 max-pain 55**
     — the violent-chop zone / OPEX magnet; expect pinning INTO 06/18 only if
     spot first stabilizes ≥55.
  3. **50 = put wall (phase-3) + −$7.4M GEX** — below it the surface thins
     (next support 45/40), and short-gamma acceleration plus the uncharted DP
     map below 54 (phase-2) makes 50-break the air-pocket scenario.
  Plus the **06/18 max-pain 55** as the opex pin magnet.
- **Open questions:** Does the macro regime (phase-6) support a vol crush
  (vanna selling pressure but also strangle-seller win) or renewed stress
  (short-gamma downside chase)? Historical: how often has IREN V-recovered
  from short-gamma flushes (phase-5 win-rate)?
