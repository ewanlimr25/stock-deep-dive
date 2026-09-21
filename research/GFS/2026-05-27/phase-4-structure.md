# Phase 4 — Dealer Structure & Gamma

**Ticker:** GFS
**As-of date:** 2026-05-27
**Generated:** 2026-05-28T00:00:00Z
**Upstream phases cited:** phase-0.5-context.md, phase-2-dark-pool.md, phase-3-positioning.md

## Summary

The dealer structure is **cautionary/bearish-leaning and internally consistent: a
hard ceiling above, amplified downside below, and a complacent vol market that is
not pricing the risk.** Dealers are **net short gamma** (total_gex +1.05M but
**regime NEGATIVE**) with spot **$81.04 below the Zero-Gamma Level $86.37** → a
trend-acceleration / vol-expansion regime (this *is* why GFS just printed +35% then
−9.7%). Positive-gamma walls cluster at **$85/$90/$95/$100** — exactly where phase-3
call-writing and phase-2's $91–92 dark-pool supply sit — so the **upside is triple-
capped**. Below spot, **negative gamma at $60–$75** means a break of support gets
*accelerated*. Term structure is in **BACKWARDATION** (front-month June IV 90.6% >
back) despite **no earnings until Aug-4** — pure momentum-unwind stress that can
vol-crush. And skew is **COMPLACENT / reversed**: 25Δ calls (94.8% IV) are richer
than 25Δ puts (84.0%), so the market is *not* paying up for downside — puts are
relatively cheap, and vanna says a fall in this elevated IV mechanically forces
dealer selling.

## Key signals

- **Short-gamma regime**, spot $81.04 **< ZGL $86.37** → downside acceleration
  `[STRUCT:gex]`.
- **Positive-gamma ceiling** $90 (+434,875), $100 (+423,356), $85 (+193,880),
  $80 (+181,287) — dealers dampen/sell rallies here `[STRUCT:gex]`.
- **Negative-gamma floor zone** $65 (−277,375), $70 (−94,120), $75 (−41,041) —
  drops amplified into this band `[STRUCT:gex]`.
- **BACKWARDATION** w/ no earnings: June 90.6% → Jul 85.0% → Oct 81.6% → Jan'27
  80.4% → Jan'28 76.2% → front-month vol-crush risk `[STRUCT:iv_term_structure]`.
- **COMPLACENT reverse skew**: 25Δ call IV 94.8% > 25Δ put IV 84.0% (skew −0.108,
  ratio 0.886) — downside under-priced, puts cheap `[STRUCT:term_skew]`.
- **Vanna selling pressure if IV falls**: public call-heavy book; IV ↓ → dealers
  (short calls) cut long hedge → mechanical SELLING `[STRUCT:vanna_charm]`.
- DEX: public net call-long → dealers net short calls → structural buy-hedge bias
  (net_dex +$37.9M) — the one offsetting positive `[STRUCT:dex]`.

## Detailed findings

### GEX `[STRUCT:gex]`

- total_gex **+1,050,287**, **regime NEGATIVE** (dealers net short gamma), spot
  **$81.04**, **ZGL $86.37**. (Tool note: GEX coarse on non-index single names —
  treat ZGL as a ±2% band, ~$84.7–$88.1.)
- Per-strike (largest |GEX|):

| strike | net_gex | vs spot | role |
|------:|--------:|--------|------|
| 90 | **+434,875** | +11% | positive-γ wall (dampen) |
| 100 | +423,356 | +23% | positive-γ wall |
| 65 | **−277,375** | −20% | negative-γ (accelerate down) |
| 85 | +193,880 | +5% | positive-γ wall (nearest ceiling) |
| 80 | +181,287 | −1% | positive-γ (near spot) |
| 95 | +129,948 | +17% | positive-γ |
| 120 | +122,541 | +48% | positive-γ (written-call strike, phase-3) |
| 70 | −94,120 | −14% | negative-γ |

Above spot is positive-γ (dealers sell rallies); below ~$78 turns negative-γ
(dealers sell dips). **The regime flips long-gamma only above ~$86.37.** Reclaiming
$86–87 would *calm* the tape; failing there keeps it whippy/downward.

### DEX `[STRUCT:dex]`

net_dex **+$37.9M** (call_dex +$59.7M, put_dex −$21.7M). Public net call-long →
dealers net short calls → dealer hedge is to **buy** underlying as it rises. This is
the single offsetting bullish mechanic (dealers chase up), but it is overwhelmed
below ZGL by the negative-gamma sell-the-dip dynamic.

### Vanna / charm `[STRUCT:vanna_charm]`

net_vanna **−404** (call-heavy book), net_charm +9,580. Interpretation:
**falling IV → call deltas drop → dealers (short calls) cut their long-underlying
hedge → selling pressure.** Given IV rank 79 / 92.5 pctile (phase-0.5) and no
catalyst to defend it, the *likely* path is IV down → this vanna flow is a
**bearish mechanical tailwind**.

### IV term structure `[STRUCT:iv_term_structure]`

**BACKWARDATION**, 5 expiries: Jun-18 (21d) 90.6% · Jul-17 (50d) 85.0% · Oct-16
(141d) 81.6% · Jan-15-27 (232d) 80.4% · Jan-21-28 (603d) 76.2%. Front-month richest
with **no earnings until 2026-08-04** → this is momentum-unwind stress, not event
premium; it can normalize fast and crush front-month long-vol.

### Term skew `[STRUCT:term_skew]`

**COMPLACENT**: call_25d_iv 0.9479 vs put_25d_iv 0.8401, skew −0.1078, ratio 0.886.
Calls richer than puts (reverse of normal equity skew) = residual speculative call
demand, downside under-hedged. **Puts are cheap here** — favorable for buying
downside or financing it.

### Front-end IV ratio `[STRUCT:front_end_iv_ratio]`

regime **FLAT** (ratio 1.0) — but degenerate: no ≤7-DTE expiry exists; both near and
far resolved to the same 21-DTE June expiry. **Low information; do not weight.**

### Today's gamma flip

**Skipped** — `today-gamma-flip` is 0DTE/intraday; this is an EOD/as-of historical
run (2026-05-27), so it carries no signal. Noted, not called.

## Tool calls (audit trail)

| Command | Result |
|---------|--------|
| `uw options-structure gex --dte-max 45` | NEGATIVE, ZGL $86.37 > spot $81.04; walls $85–100 |
| `uw options-structure dex --dte-max 45` | net_dex +$37.9M, dealers short calls |
| `uw options-structure vanna-charm --dte-max 45` | net_vanna −404; IV↓ → dealer selling |
| `uw options-structure iv-term-structure` | BACKWARDATION (front 90.6%) |
| `uw options-structure term-skew --dte-target 30` | COMPLACENT, calls richer (ratio 0.886) |
| `uw options-structure front-end-iv-ratio` | FLAT (degenerate, no 7-DTE) |
| `uw options-structure today-gamma-flip` | skipped (0DTE intraday; EOD run) |

## Tool errors

None.

## Verdict for downstream

- **Dealer regime:** **SHORT GAMMA (negative), spot below ZGL $86.37** —
  trend-amplifying, vol-expanding. Structurally **bearish-leaning** for the near
  term: capped upside ($85–92 wall stack), accelerated downside (<$78 → $65–70).
- **Conviction:** **4/5** — multiple independent structural signals align (gamma
  walls + complacent skew + backwardation + vanna), and they corroborate phases
  1–3. The only caveat is GEX coarseness on a non-index name.
- **Three structural levels for phase-9:**
  1. **ZGL $86.37 (±2%, ~$84.7–88.1)** — the regime pivot. Below = whippy/down;
     reclaim = calm. Coincides with phase-2/3 resistance.
  2. **$90 positive-GEX wall (+434,875)** — the upper dampener / phase-2 supply edge.
  3. **$65 negative-GEX node (−277,375)** — the downside acceleration magnet if
     $78/$70 support fails.
- **Open questions:** Will IV actually compress (triggering vanna selling) or does a
  catalyst re-rate it? (phase-6 macro / phase-7b). Does the historical base-rate
  (phase-5) say post-parabolic short-gamma names mean-revert down or consolidate?
  Is the complacent skew a genuine fade signal or just thin-name noise (phase-8b)?
