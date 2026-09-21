# Phase 4 — Dealer Structure & Gamma

**Ticker:** INTC
**As-of date:** 2026-06-15
**Generated:** 2026-06-16T01:24:55Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md

## Summary

The dealer structure is **positive-gamma / mean-reverting and built to cap the
rally at $130** — it argues against chasing INTC higher from here. `gex` returns
**regime POSITIVE — "Dealers net long gamma — expect mean-reversion and reduced
volatility"** (total_gex +$74.4M), with the **largest gamma pin at $130 (+$15.3M
net_gex)**, exactly the phase-3 call wall and only +1.7% above spot [STRUCT:gex].
`dex` shows dealers **net short calls → hedge by BUYING underlying** (net_dex
+$9.83B) — a dip-bid mechanic that supports weakness [STRUCT:dex]. Term skew is
**COMPLACENT** (25Δ call IV 93.0% > put 87.9%, skew_ratio 0.945) — upside calls
richer than downside puts, i.e. real call demand but little hedging [STRUCT:term_skew].
Max-pain (ex the legacy-distorted 06-18) clusters at **$110–112** (06-26/07-02/07-10)
— a downward OI gravity ~12–14% below spot [STRUCT:max_pain]. Net: spot is **wedged
between a $130 gamma/call-wall cap and a $110–120 dip-bid floor**, in a vol-suppressing
positive-gamma regime — a range/fade-rip-buy-dip backdrop, not a breakout-chase one.
Conviction 4.

## Key signals

- **GEX regime POSITIVE** (dealers long gamma, mean-reversion, reduced vol);
  total_gex **+$74,405,438**; spot $127.92 [STRUCT:gex].
- **Largest gamma pin $130 (+$15.3M net_gex)**, then $150 (+$13.4M), $140 (+$10.0M),
  $120 (+$7.6M) — gamma stacked on the call-OI strikes; $130 = +1.7% above spot [STRUCT:gex].
- **DEX +$9.83B, dealers net short calls → BUY underlying to hedge** — supportive
  dip-bid [STRUCT:dex].
- **Term skew COMPLACENT** — call 25Δ IV 0.930 > put 25Δ IV 0.879, skew −0.0513;
  upside demand, downside under-hedged (contrarian flag for phase-7c) [STRUCT:term_skew].
- **Max-pain $110–112** for 06-26/07-02/07-10 (06-18 reads $60 = legacy-OI artifact,
  flagged) — OI gravity below spot [STRUCT:max_pain].
- **Vanna net −15,098: falling IV → dealer SELLING pressure** (headwind if IV
  compresses post-OPEX); no squeeze setup [STRUCT:vanna_charm].

## Detailed findings

### GEX (regime + per-strike)

- `zero_gamma_level` reported **$13.44** — a **legacy-OI artifact**: INTC's run from
  the sub-$50 era left enormous deep-ITM call OI ($25–$70 strikes) that drags the
  ZGL calc far below spot. The **regime sign is the reliable read: POSITIVE**, and
  spot ($127.92) sits far above any real flip — dealers are long gamma. Treat ZGL as
  "well below spot," not a tradeable level.
- Per-strike net_gex (top, near spot): **$130 +15.3M · $150 +13.4M · $140 +10.0M ·
  $120 +7.6M · $135 +5.6M · $125 +4.8M**. Positive gamma is concentrated at the
  call strikes — **$130 is the dominant pin** (dealers sell into it, buy below).

### DEX (net dealer delta)

net_dex **+$9,833,697,701** (call_dex +$10.31B, put_dex −$0.47B). Public is net
call-long → **dealers net short calls → dealer hedge is to BUY underlying** — a
mechanical bid, strongest on dips. In positive gamma this is the "buy-the-dip" leg;
the "sell-the-rally" leg caps moves into $130.

### Vanna + charm

net_vanna **−15,098** (negative, call-heavy book), net_charm +1,048,420. Tool read:
"Falling IV → call delta drops → dealers (short calls) cut long-underlying hedge →
**SELLING pressure**." With IV rank 82 and earnings 5+ weeks out (07-23), post-OPEX
IV compression is plausible → a **mild mechanical headwind**. Not a squeeze (squeeze
needs positive vanna).

### IV term structure & front-end ratio

- `iv-term-structure` **structure = BACKWARDATION** (front > back) across 18 expiries.
- `front-end-iv-ratio` regime **FLAT**, ratio 1.047 (near 11-DTE IV 0.974 vs far
  32-DTE 0.930). So the backwardation is **mild** — a modest OPEX-week front-vol
  premium, **not acute event stress** (consistent with earnings being far off, 07-23).

### Term skew (25Δ)

call_25d_iv **0.930** vs put_25d_iv **0.879**, skew −0.0513, skew_ratio 0.945,
interpretation **COMPLACENT**. This is a **reverse/call skew** — upside is bid
richer than downside. Bullish in that it reflects genuine call demand (ties to
phases 1/3), but "COMPLACENT" = thin downside hedging → a **contrarian yellow flag**:
crowded upside, little protection. Hand to phase-7c.

### Today's gamma flip

**Skipped** — `today-gamma-flip` is 0DTE intraday-only; this run is on the
end-of-day 2026-06-15 snapshot (after-hours), so an intraday 0DTE flip read is not
meaningful. The 45-DTE `gex` regime above is the authoritative structural read.

### Max pain (per-expiry, dte ≤ 30; spot $127.82)

| Expiry | DTE | max_pain | dist | PCR | note |
|--------|-----|----------|------|-----|------|
| 2026-06-18 | 3 | $60 | −53.1% | 0.57 | **legacy-OI artifact — disregard** |
| 2026-06-26 | 11 | **$112** | −12.4% | 0.60 | realistic gravity |
| 2026-07-02 | 17 | **$110** | −13.9% | 0.57 | realistic gravity |
| 2026-07-10 | 25 | **$111** | −13.2% | 0.92 | realistic gravity |

The $60 06-18 figure is distorted by the same deep-ITM legacy call OI that broke the
ZGL — **disregard it**. The clean signal: the chain's OI gravity sits at **~$110–112**,
12–14% below spot. In positive gamma this is a *soft* pull (the tool's own caveat:
static-OI estimate), but it is a real downside counterweight to the bullish flow and
agrees with phase-3's $110 put-wall.

## Tool calls (audit trail)

| Command (`--symbol INTC --date 2026-06-15`) | Key value(s) ← `jq` path | Rows |
|------|------|------|
| `options-structure gex --dte-max 45` | regime POSITIVE, total +$74.4M, $130 +15.3M ← `.regime`,`.per_strike[].net_gex` | 18 |
| `options-structure dex --dte-max 45` | net_dex +$9.83B, dealers buy underlying ← `.net_dex`,`.interpretation` | — |
| `options-structure vanna-charm --dte-max 45` | net_vanna −15,098, falling-IV→selling ← `.net_vanna` | — |
| `options-structure iv-term-structure` | BACKWARDATION ← `.structure` | 18 |
| `options-structure term-skew --dte-target 30` | COMPLACENT, ratio 0.945 ← `.interpretation`,`.skew_ratio` | — |
| `options-structure front-end-iv-ratio --near-dte 7 --far-dte 30` | FLAT, ratio 1.047 ← `.regime` | — |
| `options-structure max-pain --dte-max 30` | $110–112 (06-18 $60 artifact) ← `.results[].max_pain_strike` | 4 |

## Tool errors

None (data). Note: initial `per_strike` extraction used the wrong field (`gex`);
the correct field is `net_gex` — re-extracted cleanly (see DATA NOTE). `today-gamma-flip`
intentionally not called (0DTE intraday-only, after-hours run).

## DATA NOTE / CORRECTION

- **GEX per-strike field:** first `jq` used `.gex` (null) → error. Corrected to
  `.net_gex`; top pin = $130 (+15,325,541). No wrong value was written.
- **Legacy-OI artifacts flagged, not transcribed as signal:** ZGL $13.44 and 06-18
  max-pain $60 are both distorted by deep-ITM call OI from INTC's sub-$50 era. The
  regime label (POSITIVE) and the clean max-pain cluster ($110–112) are the reliable reads.

## Verdict for downstream phases

- **Dealer regime:** **POSITIVE GAMMA (long-gamma) — mean-reverting, vol-suppressing.**
  Spot wedged under the $130 gamma/call-wall cap with a dealer dip-bid below.
- **Conviction:** **4/5** — the positive-gamma label is high-confidence for a deep-OI
  large-cap (the tool's own note flags GEX as most meaningful exactly here).
- **Three structural levels for phase-9:**
  1. **$130 — dominant gamma pin (+$15.3M) + call wall** (+1.7%): the near-term cap /
     mean-reversion magnet. Breakout needs a catalyst to overwhelm it.
  2. **$150 — second gamma peak + upper call wall** (+17.4%): upside target/ceiling.
  3. **Near-expiry max-pain $110–112** (−12–14%): downside OI gravity / dip-bid zone
     (with phase-3's $110 put-wall). ZGL is artifact-low (no real flip near spot).
- **Open questions:**
  - The structure caps momentum at $130 — does the multi-day bullish flow/accumulation
    have a *catalyst* to break it, or is this a range until earnings (07-23)? → **phases 5–7**.
  - Is the COMPLACENT call-skew a crowded-upside contrarian risk? → **phase-7c**.
  - Will post-OPEX IV compression trigger the vanna selling headwind? → **phases 7c/9 sizing**.
