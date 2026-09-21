# Phase 4 — Dealer Structure & Gamma

**Ticker:** BE
**As-of date:** 2026-07-21
**Generated:** 2026-07-22T08:20:00Z
**Upstream phases cited:** phase-3-positioning.md, phase-1-flow.md, phase-0.5-context.md

## Summary

Dealers are in a **fully short-gamma, trend-amplifying regime** (GEX
FULLY_NEGATIVE, total −3.51M, no zero-gamma crossing) heading into earnings
(2026-07-28) — moves will be amplified, not dampened. The gamma surface is
**asymmetric to the downside**: the deepest negative GEX sits at **197.5**
(−4.84M — a trapdoor that a break below ~215 would accelerate toward), while only
modest positive gamma caps the upside at **250**. Right now dealers are **net
short calls and must BUY underlying to hedge** (DEX +$444M) — a mechanical bid
supporting spot pre-print. The catch is the **post-earnings vanna/charm
headwind**: with IV rank 98.8 and backwardation (front/far IV ratio 1.41), the
IV crush after the print mechanically forces **dealer selling** (net_vanna −1,302,
net_charm −285k). Max pain pulls to **215 into the 7/24 weekly** (down 5%), then
flips **up to 240 for 7/31** (post-earnings). Net: a coiled, event-stressed,
short-gamma name where the bullish put-write lean is structurally exposed if the
print misses.

## Key signals

- **GEX FULLY_NEGATIVE, total −3,513,440, ZGL null** — short-gamma amplification `[STRUCT:gex]`
- **Worst negative GEX at 197.5 (−4.84M); positive-gamma cap at 250 (+656k)** — asymmetric downside `[STRUCT:gex]`
- **DEX net +$444.3M, dealers short calls → BUY-to-hedge** (pre-print bid) `[STRUCT:dex]`
- **Vanna/charm negative → post-earnings IV crush = dealer SELLING pressure** `[STRUCT:vanna_charm]`
- **BACKWARDATION, front/far IV ratio 1.408 (near 2.59 / far 1.84); skew TAIL_HEDGING (put25Δ 1.83 vs call 1.65)** `[STRUCT:iv_term_structure / front_end_iv_ratio / term_skew]`
- **Max pain 7/24 → 215 (−5.05%), 7/31 → 240 (+5.99%), 8/14 → 225** `[STRUCT:max_pain]`

## Detailed findings

### GEX `[STRUCT:gex]`

- `regime` = **FULLY_NEGATIVE**; `regime_description` = "All strikes have negative
  net GEX — strong gamma amplification"; `total_gex` = **−3,513,440**;
  `zero_gamma_level` = **null** (no crossing — spot 226.02 is in a wholly
  short-gamma book).
- Per-strike net_gex — **most negative (accelerants):** 197.5 (−4.84M), 165
  (−1.17M), 200 (−0.74M), 180 (−0.72M) — all *below* spot → a downside break is
  amplified toward the 197.5 put wall. **Most positive (dampers):** 250 (+0.66M),
  275 (+0.45M), 280 (+0.39M), 260 (+0.38M) — a mild upside brake at 250–280.
- Read: short-gamma into a binary event = expect the ~10.6% implied move to be
  *realized or exceeded*, and any directional break to run.

### DEX `[STRUCT:dex]`

`net_dex` = **+$444,306,542** (call_dex +$1.543B, put_dex −$1.099B).
Interpretation (verbatim): *"Public is net call-long → dealers net short calls →
dealer hedge is to BUY underlying."* A mechanical bid under spot pre-earnings —
supportive now, but it is a *hedge*, not conviction, and unwinds with IV.

### Vanna + charm `[STRUCT:vanna_charm]`

`net_vanna` −1,302, `net_charm` −284,819. Interpretation (verbatim): *"Public net
vanna negative (call-heavy book). Falling IV → call delta drops → dealers (short
calls) cut long hedge → SELLING pressure. Rising IV reverses."* **This is the
post-earnings risk**: the inevitable IV crush from 98.8 rank turns dealer hedging
into a *seller* — a headwind that can blunt or reverse a modest positive earnings
reaction (the classic "good print, sell the vol" fade).

### IV term structure `[STRUCT:iv_term_structure]`

`structure` = **BACKWARDATION** (front-month IV > back). Classic single-name event
stress ahead of the 7/28 print. Normalizes within ~24h post-earnings — do not
trade the backwardation itself once the event passes (pitfall).

### Term skew `[STRUCT:term_skew]`

put25Δ IV **1.8263** vs call25Δ IV **1.6482**; skew +0.178, ratio **1.108**;
`interpretation` = **TAIL_HEDGING**. Puts ~11% richer than calls — a moderate
downside-protection bid (consistent with phase-1's deep-OTM put lottery), not an
extreme panic skew.

### Front-end IV ratio `[STRUCT:front_end_iv_ratio]`

near (7d) IV **2.5866** vs far (30d) IV **1.8374**, ratio **1.408**, `regime`
BACKWARDATION — front-end carries a large event premium that will deflate through
7/28. Selling that front-end vol (which the phase-1 put-writers are doing) is the
positioned trade.

### Today's gamma flip

**Skipped** — this is an after-hours / as-of (2026-07-21) run, not intraday;
`today-gamma-flip` (0DTE-only, intraday) is not meaningful here.

### Max pain `[STRUCT:max_pain]` (spot 226.44; caveat: static-OI estimate)

| Expiry | DTE | max_pain_strike | distance | P/C OI |
|--------|-----|-----------------|----------|--------|
| **2026-07-24** | 3 | **215** | −5.05% | 3.218 (put-heavy pre-ER) |
| 2026-07-31 | 10 | **240** | +5.99% | 1.373 (post-ER upward) |
| 2026-08-07 | 17 | 215 | −5.05% | 0.218 |
| 2026-08-14 | 24 | 225 | −0.64% | 0.316 |

Pre-earnings gravity pulls **down to 215** (agrees with phase-3's put-heavy 7/24
cliff and the 215 DP level); post-earnings the pin flips **up to 240**. The 8/14
magnet settles at spot (225). Near-expiry (215) is the tradeable magnet; far
strikes are softer.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Notes |
|------------------|--------------------------|-------|
| `options-structure gex --symbol BE --dte-max 45` | regime FULLY_NEGATIVE, total −3.51M, ZGL null ← `.regime/.total_gex/.zero_gamma_level`; 197.5 net_gex −4.84M ← `.per_strike[]` | short-gamma |
| `options-structure dex --symbol BE --dte-max 45` | net_dex +444.3M ← `.net_dex/.interpretation` | dealer buy-hedge |
| `options-structure vanna-charm --symbol BE --dte-max 45` | net_vanna −1302 ← `.net_vanna/.vanna_interpretation` | post-ER sell risk |
| `options-structure iv-term-structure --symbol BE` | BACKWARDATION ← `.structure` | event stress |
| `options-structure term-skew --symbol BE --dte-target 30` | ratio 1.108 TAIL_HEDGING ← `.skew_ratio/.interpretation` | puts +11% |
| `options-structure front-end-iv-ratio --near-dte 7 --far-dte 30` | ratio 1.408 ← `.ratio/.regime` | front vol rich |
| `options-structure max-pain --symbol BE --dte-max 30` | 7/24 → 215 ← `.results[]｜.max_pain_strike/.distance_pct` | pin magnet |

## Tool errors

<none — all seven reads valid JSON. `today-gamma-flip` deliberately skipped
(after-hours run). `iv-term-structure` per-row `dte`/`iv` returned null in the
summary view; the regime label `.structure`=BACKWARDATION is the authoritative
field and was read verbatim per the phase spec (do not re-derive).>

## DATA NOTE / CORRECTION

- max-pain strike field is `max_pain_strike` (not `max_pain`/`strike`); first jq
  read null, re-read against `.max_pain_strike` → 215/240/215/225. All pin strikes
  above trace to that path.
- GEX per-strike field is `net_gex` (not `gex`); re-read via `.per_strike[].net_gex`.

## Verdict for downstream phases

- **Dealer regime:** **SHORT-GAMMA (trend-amplifying)** with a *mechanical dealer
  buy-hedge now* (DEX +444M) but a *post-earnings vanna/charm SELL headwind* as IV
  crushes. Asymmetric **downside** gamma (worst at 197.5).
- **Conviction:** **4 / 5** — the structure signals are clean and mutually
  consistent (negative GEX + backwardation + tail skew all say "big event move,
  amplified, downside trapdoor").
- **Three structural levels for phase-9 (+ pin magnet):**
  1. **ZGL:** none (fully short-gamma) — treat the *whole* zone as amplifying.
  2. **Largest negative-GEX strike 197.5** — downside accelerant / floor magnet.
  3. **Largest positive-GEX strike 250** — upside damper / resistance.
  4. **Near-expiry max pain 215** (7/24 pre-earnings magnet); post-ER flips to 240.
- **Open questions:** Does the historical earnings-move (phase-5) exceed the 10.6%
  implied move — i.e. is short-gamma amplification likely to overshoot? Is the
  post-earnings vanna sell strong enough to fade a positive reaction (phases 8b/9)?
  How does the mechanical dealer buy-hedge interact with the phase-2 closing-cross
  overhang?
