# Phase 4 — Dealer Structure & Gamma

**Ticker:** DOCN
**As-of date:** 2026-07-17
**Generated:** 2026-07-20T01:40:00Z
**Upstream phases cited:** phase-0.5-context.md, phase-1-flow.md, phase-3-positioning.md

## Summary

DOCN is in a **long-gamma (POSITIVE) dealer regime** — ZGL $70.14 sits far below
$119.31 spot, so dealers dampen moves (sell rallies / buy dips), suppressing
realized vol and reinforcing a range. The **near-expiry max-pain magnet is $120**
(7/24 and 8/7 both pin there, ≈spot) — opex gravity agrees with phase-3's $120
put_heavy battleground and $115/$128 walls. The IV term structure shows the
**classic pre-earnings hump: IV peaks at the 8/7 expiry (117.9%)**, the first
tenor after **8/4 earnings**, then declines — the overall "BACKWARDATION" label is
driven by the 0DTE 446% spike. The standout risk: a **call-heavy book at IV rank
99** means **post-earnings vol crush → vanna selling pressure** on the way down.
Net: **range-bound / vol-suppressed into earnings, with a vanna downside tail after.**

## Key signals

- **GEX regime POSITIVE** ("dealers net long gamma — mean-reversion, reduced
  vol"), **ZGL $70.14** vs spot $119.31 `[STRUCT:gex]` — range-supportive.
- **Max-pain magnet $120** (7/24 dist +0.9%, pc_oi 1.98; 8/7 dist +0.9%) — opex
  gravity ≈ spot `[STRUCT:max_pain]`; 7/17 pins $128 (call wall).
- **IV term structure humps at 8/7 = 117.9%** (post-earnings tenor), vs 7/24
  101.6% and 1/15 96.0% `[STRUCT:iv_term_structure]` — vol priced for 8/4 earnings.
- **Vanna risk:** public net vanna negative (call-heavy book) → **falling IV ⇒
  dealers SELL underlying** `[STRUCT:vanna_charm]`. With IV rank 99, post-earnings
  crush is a mechanical downside pressure.
- **DEX net −$4.4M**: public mildly net put-long → dealer hedge is to SELL
  underlying `[STRUCT:dex]` (small). **Skew NORMAL** (put/call 25Δ ratio 1.059) —
  no panic tail-hedging `[STRUCT:term_skew]`.

## Detailed findings

### GEX `[STRUCT:gex]`

- **regime: POSITIVE** — "Dealers net long gamma — expect mean-reversion and
  reduced volatility."
- **zero_gamma_level: $70.14** (spot $119.31 far above → deep long-gamma).
- total_gex field reads −1,673,663 (per-strike concentration is negative around the
  $100 strike, −103,731); the **tool's `regime` label (POSITIVE) is authoritative**
  per skill guidance — quoted verbatim, not re-derived. Spot ≫ ZGL confirms the
  long-gamma, range-suppressing read.

### DEX `[STRUCT:dex]`

- net_dex **−$4,401,071** (call_dex +$69.2M, put_dex −$73.6M).
- Interpretation (verbatim): "Public is net put-long → dealers net short puts →
  dealer hedge is to SELL underlying." Magnitude is modest — a mild, not dominant,
  downward hedging bias.

### Vanna + charm `[STRUCT:vanna_charm]`

- net_vanna **−260** (call-heavy book), net_charm +4,598.
- Interpretation (verbatim): "Public net vanna negative (call-heavy book). Falling
  IV → call delta drops → dealers (short calls) cut long-underlying hedge → SELLING
  pressure. Rising IV reverses." **This is the key structural risk**: at IV rank 99,
  the likely next move in IV is *down* (post-8/4 crush) → vanna adds sell pressure.

### IV term structure `[STRUCT:iv_term_structure]` (structure label: BACKWARDATION)

| Expiry | DTE | avg IV | note |
|--------|-----|--------|------|
| 2026-07-17 | 0 | **446.2%** | 0DTE expiry noise → drives the "backwardation" label |
| 2026-07-24 | 5 | 101.6% | front |
| 2026-07-31 | 12 | 105.7% | |
| **2026-08-07** | 19 | **117.9%** | **peak — first expiry after 8/4 earnings** |
| 2026-08-14 | 26 | 114.1% | |
| 2026-08-21 | 33 | 110.8% | monthly OPEX |
| 2026-09-18 | 61 | 105.5% | |
| 2026-10-16 | 90 | 100.5% | |
| 2027-01-15 | 180 | 96.0% | back |

Excluding 0DTE, this is a **pre-earnings vol hump** peaking at 8/7 (117.9%),
declining into the back months — vol is priced for the 8/4 event. `front-end-iv-ratio`
(5d 101.6% vs 33d 110.8%, ratio 0.917) reads **CONTANGO** because the earnings
premium sits at the far end of that window. Both labels reconcile to: **earnings
vol bump at the 8/7–8/21 tenor.**

### Term skew `[STRUCT:term_skew]`

- put_25d_iv 1.147 vs call_25d_iv 1.082, skew 0.064, **skew_ratio 1.059**,
  interpretation **NORMAL** (dte_actual 33). Mild, ordinary put richness — no
  tail-hedge panic, no call-chase euphoria.

### Front-end IV ratio `[STRUCT:front_end_iv_ratio]`

- near 5d 101.6% / far 33d 110.8% → **ratio 0.917, regime CONTANGO** (earnings
  premium at the far tenor). Event stress is present but *dated to 8/4*, not now.

### Today's gamma flip

- **Skipped** — `today-gamma-flip` is 0DTE intraday-only; this is an as-of
  (after-hours) historical run. Not meaningful; not called.

### Max pain (opex gravity) `[STRUCT:max_pain]` (dte ≤ 30; static-OI caveat)

| Expiry | max_pain | dist% | put_call_oi_ratio |
|--------|----------|-------|-------------------|
| 2026-07-17 | $128 | +7.6 | 0.417 (call-heavy) |
| **2026-07-24** | **$120** | **+0.9** | 1.978 (put-heavy) |
| 2026-07-31 | $130 | +9.3 | 10.05 (very put-heavy) |
| 2026-08-07 | **$120** | +0.9 | 0.694 |
| 2026-08-14 | $125 | +5.1 | 0.514 |

**Near-expiry magnet = $120** (≈spot). The chain wants to pin price near $120 into
late July / early August — consistent with the long-gamma regime and phase-3 walls.
(8/21 earnings expiry is just outside dte-max 30; phase-9 should treat $120 as the
pre-earnings pin and expect it to loosen once the 8/4 event injects realized vol.)

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | |
|------------------|--------------------------|--|
| `options-structure gex --dte-max 45` | regime POSITIVE, ZGL 70.14 ← `.regime`, `.zero_gamma_level` | spot 119.31 |
| `options-structure dex --dte-max 45` | net_dex −4.4M ← `.net_dex` | |
| `options-structure vanna-charm --dte-max 45` | net_vanna −260, "falling IV→SELL" ← `.net_vanna`,`.vanna_interpretation` | |
| `options-structure iv-term-structure` | 8/7 IV 117.9% ← `.term_structure[] .avg_iv` | BACKWARDATION |
| `options-structure term-skew --dte-target 30` | skew_ratio 1.059, NORMAL ← `.skew_ratio`,`.interpretation` | |
| `options-structure front-end-iv-ratio 7/30` | ratio 0.917, CONTANGO ← `.ratio`,`.regime` | |
| `options-structure max-pain --dte-max 30` | 7/24 pin $120 ← `.results[] .max_pain` | |

## Tool errors

(none — all seven calls returned valid JSON. `today-gamma-flip` intentionally not
called: 0DTE intraday-only, not meaningful on an after-hours as-of run.)

## DATA NOTE / CORRECTION

- `iv-term-structure` "BACKWARDATION" label is driven by the 0DTE 446% row; the
  tradeable curve (≥5DTE) is a pre-earnings hump peaking 8/7. Both the term and
  front-end labels are reported verbatim and reconciled, not re-derived.
- GEX `total_gex` sign is negative while `regime`=POSITIVE; per skill guidance the
  `regime`/`zero_gamma_level` labels are quoted authoritatively (spot ≫ ZGL ⇒ long
  gamma), not recomputed from the raw sum.

## Verdict for downstream phases

- **Dealer regime:** **Long-gamma (POSITIVE)** — range-bound, vol-suppressed,
  mean-reverting into 8/4 earnings. Mild dealer *sell* hedge (DEX) + vanna sell
  risk on any IV decline.
- **Conviction:** **3/5** (clear regime + clear $120 pin + clear earnings vol hump).
- **Structural levels for phase-9:**
  1. **Max-pain pin $120** (near-expiry magnet, ≈spot) — the gravity center.
  2. **ZGL $70.14** (far below — confirms long gamma; not a tradeable level).
  3. Regime-consistent range **$115 support ↔ $128 call wall** (agrees w/ phase-3).
- **Key structural risk to carry:** **call-heavy book + IV rank 99 → post-earnings
  vol crush = vanna SELLING pressure.** Any long-vol or long-delta thesis must
  respect the 8/4 event and the mechanical downside after it.
- **Open questions:** Does phase-5 history show DOCN mean-reverting inside a range in
  long-gamma regimes? What is the empirical earnings move vs the priced ~implied
  hump (phase-5/7c)? Is 8/4 earnings the dominant catalyst on the phase-6 calendar?
