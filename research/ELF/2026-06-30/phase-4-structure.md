# Phase 4 — Dealer Structure & Gamma

**Ticker:** ELF
**As-of date:** 2026-06-30
**Generated:** 2026-07-01T00:29:45Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md

## Summary

The dealer structure is a **mean-reversion headwind against the bullish flow, not a
continuation tailwind.** GEX regime is **POSITIVE / long-gamma** (`zero_gamma_level
$59.97`, spot $74 well above) — dealers sell rallies and buy dips, suppressing
realized vol. The two largest positive-gamma walls, **$70 (+1.03M) and $75 (+681k),
straddle the $74 spot**, so dealer hedging pins price into the $70–75 zone with $80
the next magnet up. Meanwhile **max-pain sits $59–63 across every near expiry, 15–20%
below spot** — the call-heavy OI is now deep ITM, so the option structure exerts a
mild *downward/consolidation* gravity, not an upward pin. IV term structure is
mildly **BACKWARDATION** (ratio 1.072) but earnings is 2026-08-05, so that front-IV
elevation is the +17% realized-vol run, not an event. Skew is **NORMAL** (puts only
mildly richer). Net: after an extended six-session rally, the structure favors the
$75 wall capping and $70–72 pinning — **don't chase; fade-into-strength / long-dated
is the structurally-sane expression.**

## Key signals

- **GEX regime POSITIVE (long gamma)**, ZGL $59.97, total_gex +2.89M — mean-reversion, suppressed vol [STRUCT:gex]
- **Largest gamma walls $70 (+1,030,467) and $75 (+681,186) bracket spot $74** → $70–75 pin zone; $80 (+333,643) next [STRUCT:gex]
- **Max-pain $59–63 on all near expiries (15–20% below spot)** — downward/consolidation gravity, no upside pin [STRUCT:max-pain]
- **IV term structure BACKWARDATION (ratio 1.072)** — but earnings is Aug-05, so momentum-driven, not event stress [STRUCT:iv-term-structure][STRUCT:front-end-iv-ratio]
- **Skew NORMAL** (put_25Δ 0.685 vs call_25Δ 0.630, skew_ratio 1.087) — no tail-hedging panic [STRUCT:term-skew]

## Detailed findings

### GEX `[STRUCT:gex]`

- `regime` = **POSITIVE**; `regime_description` = "Dealers net long gamma — expect
  mean-reversion and reduced volatility."
- `zero_gamma_level` = **$59.97** (~$60). Spot $74 is **+23% above ZGL** → firmly
  long-gamma. A regime flip to short-gamma (trend amplification) would require a break
  under ~$60 — a distant, thesis-breaking level.
- `total_gex` = +2,892,849.
- Per-strike (near spot): **$70 = +1,030,467** (dominant), **$75 = +681,186**, **$80 =
  +333,643**, then $65 +116k, $60 +129k, $85 +76k. Minor negative pockets at $64
  (−22.7k) / $66 (−45k). The gamma is stacked at $70/$75 → those are the dealer
  hedging magnets bracketing the $74 spot.

### DEX `[STRUCT:dex]`

- `net_dex` = **+72,622,466** (call_dex +76.13M, put_dex −3.50M). Delta exposure is
  overwhelmingly call-driven — consistent with the phase-3 call-heavy chain. Large
  positive dealer delta means hedging flow leans to selling into strength (reinforces
  the long-gamma mean-reversion read).

### Vanna / charm `[STRUCT:vanna-charm]`

- No squeeze signature flagged; in a long-gamma, normal-skew, declining-front-IV
  context there is no positive-vanna + negative-dealer-delta squeeze setup. (The
  bullish mechanical bid case — the classic vanna squeeze — does **not** apply here;
  dealers are long gamma, not short.)

### IV term structure `[STRUCT:iv-term-structure]`

- `structure` = **BACKWARDATION** (front IV > back IV). Per-strike dte/iv rows returned
  null in this build, but the label is authoritative and corroborated by front-end-iv-ratio.
- Interpretation: front elevated by the **realized-vol spike from the +17% run**, not
  earnings (next earnings 2026-08-05, phase-0.5 — beyond the Jul front). Watch phase-6/7c
  for any July catalyst; absent one, this normalizes as the move settles.

### Term skew `[STRUCT:term-skew]`

- `interpretation` = **NORMAL**. `put_25d_iv` 0.6847 vs `call_25d_iv` 0.6298, `skew`
  0.0549, `skew_ratio` 1.087. Puts modestly richer (ordinary equity skew) — **no
  tail-hedging demand spike**, no risk-off signature.

### Front-end IV ratio `[STRUCT:front-end-iv-ratio]`

- `ratio` = **1.072** (near_iv 0.684 @ dte 10 vs far_iv 0.638 @ dte 31), `regime` =
  **BACKWARDATION**. Mild front-end stress — consistent with the momentum read above.

### Today's gamma flip `[STRUCT:today-gamma-flip]`

- EOD/as-of run: tool returned `spot 73.94` only (zgl/flip null) — it is an
  **intraday-0DTE** tool with no live session to read. **Noted and skipped** per phase
  guidance. Use the GEX ZGL ($59.97) as the regime boundary instead.

### Max pain `[STRUCT:max-pain]` (spot $74; static-OI estimate per tool caveat)

| Expiry | DTE | max_pain | distance | P/C OI |
|---|---|---|---|---|
| 2026-07-02 | 2 | **$61** | −17.6% | 0.24 |
| 2026-07-10 | 10 | **$63** | −14.9% | 0.14 |
| **2026-07-17** | 17 | **$60** | −18.9% | 0.66 |
| 2026-07-24 | 24 | $59 | −20.3% | 0.37 |

Every near-expiry max-pain is **$59–63, 15–20% below spot**. The chain's call-heavy OI
is deep ITM after the run, so the theoretical pain-minimizing strike lags far below —
a **downward/consolidation gravity**, not an upside pull. Per the tool's caveat this
is static-OI and softens with distance; treat it as "the rally is ahead of its OI, and
the structure won't pull price *up*" rather than a hard $60 target. The **Jul-17
max-pain $60** vs phase-3's Jul-17 OPEX cliff (17.9% of OI) and $75 call wall: they
agree the heavy OI is below spot and now ITM — no upside magnet exists near $74.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw options-structure gex --symbol ELF --dte-max 45 --date 2026-06-30` | regime POSITIVE, ZGL 59.97 ← `.regime`,`.zero_gamma_level`; $70 +1.03M ← `.per_strike[]` | all strikes |
| `uw options-structure dex --symbol ELF --dte-max 45 --date 2026-06-30` | net_dex +72.6M ← `.net_dex` | agg |
| `uw options-structure vanna-charm --symbol ELF --dte-max 45 --date 2026-06-30` | no squeeze signature | agg |
| `uw options-structure iv-term-structure --symbol ELF --date 2026-06-30` | BACKWARDATION ← `.structure` | term |
| `uw options-structure term-skew --symbol ELF --dte-target 30 --date 2026-06-30` | NORMAL, skew_ratio 1.087 ← `.interpretation`,`.skew_ratio` | agg |
| `uw options-structure front-end-iv-ratio --symbol ELF --near-dte 7 --far-dte 30 --date 2026-06-30` | ratio 1.072 BACKWARDATION ← `.ratio`,`.regime` | agg |
| `uw options-structure today-gamma-flip --symbol ELF --date 2026-06-30` | spot 73.94, flip null (intraday tool) ← `.spot` | n/a |
| `uw options-structure max-pain --symbol ELF --dte-max 30 --date 2026-06-30` | Jul-17 $60 −18.9% ← `.results[].max_pain_strike`,`.distance_pct` | 4 expiries |

## Tool errors

_None — all eight reads returned exit 0 and valid JSON. `today-gamma-flip` returned a
sparse (intraday) payload — handled per phase guidance, not an error._

## DATA NOTE / CORRECTION

- `iv-term-structure` per-row `dte`/`iv` came back null in this build; the `structure`
  label (BACKWARDATION) is authoritative and corroborated by `front-end-iv-ratio`
  (near 0.684 > far 0.638). No per-row numbers were transcribed from the null rows.

## Verdict for downstream phases

- **Dealer regime:** **LONG GAMMA** (POSITIVE GEX, ZGL $59.97, spot +23% above) →
  mean-reversion, suppressed realized vol. This is a **structural headwind against
  chasing the +17% run**: dealers sell into strength, and max-pain sits well below spot.
- **Conviction:** **3 / 5** — the GEX regime, ZGL, and $70/$75 gamma walls are clean,
  high-quality reads; the mean-reversion implication is well-supported.
- **Three structural levels for phase-9** (+ near-expiry max-pain magnet):
  1. **$70 — largest GEX strike (+1.03M) / primary dealer pin** (aligns with phase-2 DP
     $69.91 cluster + phase-3 $70 call-heavy) → strongest support magnet.
  2. **$75 — GEX wall (+681k) = phase-3 call wall** → near-term ceiling; a *sustained*
     break above (dealer buy-to-hedge) opens $80.
  3. **$80 — GEX wall (+334k)** → next upside magnet / target.
  - **ZGL $59.97** = regime-flip line (short-gamma below → trend amplification; a
    thesis-breaking break).
  - **Near-expiry max-pain $60–61** = downward gravity reference (indicative only).
- **Open questions:**
  - Long-gamma pin vs bullish flow: does phase-5 show ELF *continues* after +17%/6-session
    runs, or mean-reverts (the structure votes mean-revert)?
  - Front-end backwardation with no earnings until Aug-05 — is there a **July catalyst**
    (phase-6/7c) or is it pure momentum vol?
  - The $75 gamma wall + max-pain-below-spot cap near-term upside — this is a **downside
    temper on phase-1's conviction**; phase-9 should size for consolidation, not breakout.
