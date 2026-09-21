# Phase 4 — Dealer Structure & Gamma

**Ticker:** MU
**As-of date:** 2026-06-23
**Generated:** 2026-06-23
**Upstream phases cited:** phase-1-flow.md, phase-3-positioning.md

## Summary

The dealer structure is **built for a big directional move, not a pin** — and it is
**directionally symmetric** (it favors magnitude, not a side). GEX regime is
**NEGATIVE (dealers net short gamma)** with the **Zero Gamma Level at 1495.2, far above
spot $1053.58** — across any realistic post-earnings range MU is short-gamma, so dealer
hedging **amplifies** the move rather than damping it. IV is in **BACKWARDATION** with a
front-end IV ratio of **1.252** (near 143.5% vs far 114.7%) — textbook event stress that
will crush post-print. Yet the **25Δ skew is COMPLACENT** (put IV 110.9% ≈ call IV 110.4%,
ratio 1.005) — the surface prices a *symmetric* ±10.9% move with no downside-fear premium.
The static-OI **max-pain anchor for the 2026-06-26 expiry is $1050 (−0.13%, dead at spot)**,
matching phase-3's ATM pivot — but it is a *pre-event* magnet the print will blow through.
The one directional asymmetry: **negative vanna on a call-heavy book** means the post-print
IV crush mechanically forces dealers to **unwind their long-underlying hedge → selling
pressure**, a structural headwind to any post-earnings rally.

## Key signals

- **Short-gamma regime**: GEX NEGATIVE, ZGL **1495.2** ≫ spot **1053.58** → moves amplify, no pin holds post-print `[STRUCT:gex]`
- **IV BACKWARDATION** + front-end IV ratio **1.252** (near_iv 1.4352 / far_iv 1.1466) → event stress, post-print crush `[STRUCT:iv_term_structure]` `[STRUCT:front_end_iv_ratio]`
- **Skew COMPLACENT**, skew_ratio **1.005** (put 1.1092 ≈ call 1.1037) → symmetric expected move, no panic-hedge premium `[STRUCT:term_skew]`
- **Max-pain 06-26 = $1050** (−0.13%), PCR_oi 2.125 — pre-event anchor at spot; later expiries pull lower (1015 → 1000 → 790) `[STRUCT:max_pain]`
- **DEX**: dealers net-short calls → hedge is **BUY underlying** (current bid); **vanna negative** → IV crush unwinds that hedge → post-print **selling** pressure `[STRUCT:dex]` `[STRUCT:vanna_charm]`

## Detailed findings

### GEX — `[STRUCT:gex]`

- `regime` = **NEGATIVE**; `regime_description` = "Dealers net short gamma — expect trend
  acceleration and increased volatility."
- `zero_gamma_level` = **1495.2** (≈ +42% above spot $1053.58) — gamma only flips positive
  up at the 1500 LEAP-call wall; everywhere tradeable, MU is short-gamma.
- Heaviest negative GEX per-strike near spot: **950 (−778,404)**, 960 (−226,502), 940
  (−221,536) — a downside acceleration shelf; a break under $1000 toward $950 is where
  short-gamma hedging chases hardest.

### DEX — `[STRUCT:dex]`

- `net_dex` = +11.57B; interpretation: "Public is net call-long → dealers net short calls
  → dealer hedge is to BUY underlying." A current structural **bid** (corroborates phase-2
  accumulation) — but it is delta that **decays as the post-print IV crush cuts call delta**.

### Vanna + charm — `[STRUCT:vanna_charm]`

- `net_vanna` = −3,221, `net_charm` = +53,620, no squeeze signal.
- `vanna_interpretation`: "Public net vanna negative (call-heavy book). **Falling IV → call
  delta drops → dealers (short calls) cut long-underlying hedge → SELLING pressure.** Rising
  IV reverses." → The post-earnings IV collapse is a **mechanical selling headwind** to a
  relief rally; a positive surprise must overcome it. (Closed-form, coarse — directional read,
  not a level.)

### IV term structure — `[STRUCT:iv_term_structure]`

- `structure` = **BACKWARDATION** (front-month IV > back) — event stress; will normalize
  within 24h of the print, so do not trade the backwardation itself post-event.

### Term skew — `[STRUCT:term_skew]`

- `interpretation` = **COMPLACENT**; `skew_ratio` = 1.005; put_iv 1.1092 ≈ call_iv 1.1037.
  The market is *not* paying up for downside — symmetric move priced. Mildly notable: no
  crowded put-fear to fade, and no skew signal telegraphing the direction.

### Front-end IV ratio — `[STRUCT:front_end_iv_ratio]`

- `ratio` = **1.252**, near_iv 1.4352 (143.5%) / far_iv 1.1466 (114.7%) — front-week IV 25%
  rich to the 30-day → a binary event is priced into the front week (the 06-26 expiry).

### Max pain (opex-gravity) — `[STRUCT:max_pain]`

| Expiry | DTE | max_pain | dist% | PCR_oi | read |
|---|---|---|---|---|---|
| **2026-06-26** | 3 | **$1050** | −0.13% | 2.125 | pre-event pin **at spot** (= phase-3 ATM pivot) |
| 2026-07-02 | 9 | $1015 | −3.46% | 1.791 | mild downward pull |
| 2026-07-10 | 17 | $1000 | −4.89% | 5.056 | put-heavy gravity → $1000 |
| 2026-07-17 | 24 | $790 | −24.86% | 1.879 | far-dated, **static-OI artifact** — indicative only |

Static-OI caveat (tool's own): "Max pain assumes settlement with current OI unchanged."
The $1050 06-26 anchor is the tradeable magnet; the progressively lower later strikes are
the put-heavy OI's downward bias, soft and migrating. **Read with GEX: max pain pins $1050
*pre*-event; short gamma means the ±10.9% print blows through it and the resulting trend
amplifies.**

### Today's gamma flip

Not run — `today-gamma-flip` is 0DTE/intraday and this is an as-of (after-hours,
non-live) run. Noted and skipped per phase guidance.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Notes |
|---|---|---|
| `options-structure gex --symbol MU --dte-max 45` | regime NEGATIVE, ZGL 1495.2 ← `.regime,.zero_gamma_level`; 950 GEX −778k ← `.per_strike` | spot 1053.58 |
| `options-structure dex --symbol MU --dte-max 45` | net_dex +11.57B, "BUY underlying" ← `.regime` | — |
| `options-structure vanna-charm --symbol MU --dte-max 45` | net_vanna −3,221; IV-crush→selling ← `.vanna_interpretation` | no squeeze |
| `options-structure iv-term-structure --symbol MU` | BACKWARDATION ← `.structure` | — |
| `options-structure term-skew --symbol MU --dte-target 30` | COMPLACENT, ratio 1.005 ← `.interpretation,.skew_ratio` | — |
| `options-structure front-end-iv-ratio --symbol MU --near-dte 7 --far-dte 30` | 1.252 ← `.ratio` | near 1.4352 |
| `options-structure max-pain --symbol MU --dte-max 30` | 06-26 $1050 −0.13% ← `.results[0].max_pain_strike` | static-OI |

## Tool errors

(none — `iv-term-structure` exposes `.term_structure` rows without an `iv` scalar at the
summary level; the regime label `.structure` is the field of record and parsed cleanly.)

## DATA NOTE / CORRECTION

(none — all regime labels quoted verbatim from the tools' own fields per guidance;
no hand-derived regimes.)

## Verdict for downstream phases

- **Dealer regime:** **SHORT GAMMA / event-stressed** — directionally **symmetric**
  (complacent skew), built to **amplify** the post-print move. Mild directional asymmetry:
  post-print IV crush + negative vanna → mechanical **selling** headwind to a rally.
- **Conviction:** **4/5** on the regime (clear short-gamma + backwardation + 1.25 front-end);
  **0/5 directional** (structure favors magnitude, not a side).
- **Three structural levels for phase-9 (+ the max-pain magnet):**
  1. **Max-pain pin $1050 (06-26)** — pre-event gravity at spot; the post-print move is
     measured *from* here (±10.9% ⇒ ~$937 / ~$1165).
  2. **Negative-GEX acceleration shelf ~$950–1000** — short-gamma chases hardest if price
     breaks the $1000 put-wall to the downside.
  3. **ZGL $1495.2** — gamma stays negative below it (i.e. in every realistic range);
     a move would have to clear the 1500 call wall to enter long-gamma/pinning territory.
- **Open questions:** Does the historical earnings record (phase-5) show MU's realized
  post-print move runs *with* the short-gamma amplification, and at what hit-rate/direction?
  Does macro/sector (phase-6) bias the symmetric structure to a side (semis being sold —
  phase-0.5)? The structure is a coiled spring; phases 5–6 must supply the directional lean.
