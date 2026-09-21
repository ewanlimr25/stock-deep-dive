# Phase 3 — Open Interest & Positioning

**Ticker:** PDD
**As-of date:** 2026-05-26
**Generated:** 2026-05-26T20:30:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-0.5-context.md

## Summary

Positioning is **hedged/defensive, not directionally bullish — and it diverges from
the dark-pool bid.** Of the 8 fresh OI builds ≥500, `oi_smart_positioning` infers
**7 as "bearish"**: the far-OTM calls (6/18 110C, 9/18 130C, 1/15 150C) all built on
the **bid** (call *writing* / overwriting), and the near puts (5/29 90P, 5/29 92P,
6/26 94P) built on the **ask** (downside bets/hedges) [OI:smart_positioning]. Read
*together with* phase-2's 100%-buy block tape, the most coherent interpretation is a
**collar / buy-write on accumulated stock** — long shares, short upside calls, long
downside puts — i.e. risk-managed long exposure into the print, **not** clean bullish
conviction. The single biggest OI change is a **−5,989 unwind of the 6/18 125C**
(de-risking) [OI:decrease_with_volume]. Critically, **PDD is absent from the pin-risk
list** — it is *not* gamma-pinned this week and is free to move on the 5/27 print
[OI:pin_risk]. No same-day rolls detected.

## Key signals

- **7 of 8 fresh OI builds inferred bearish** [OI:smart_positioning]: upside calls
  written on bid (110C net_ask_bid −1,477; 130C −800; 150C −530), puts bought on ask
  (90P net +495, 92P +345).
- **Biggest call OI build is bid-side, i.e. written:** 6/18 110C +1,585 (→13,565),
  prev_ask 298 vs prev_bid 1,775 [OI:biggest_increases] — supply of upside, not demand.
- **Fresh put accumulation just below spot:** 6/26 94P +1,008 (54→1,062, **18.7×**),
  avg $4.62 [OI:biggest_increases] — protection/bet at the $94.5 DP support shelf.
- **−5,989 unwind of 6/18 125C** on 7,023 volume — largest single OI move, de-risking
  far-OTM call longs ahead of earnings [OI:decrease_with_volume].
- **No pin:** PDD does not appear in the OPEX-week `oi_pin_risk` top-25 (led by HYG,
  SPY, TLT) [OI:pin_risk]; no single-expiry OI cliff in `oi_opex_concentration` either.
  → spot is unconstrained by dealer gamma into the print.

## Detailed findings

### Largest OI increases — `[OI:biggest_increases]` (ref stock_price $96.68)

| Strike/Exp | Type | DTE | OI Δ | Curr OI | Vol | avg$ | prev ask/bid | Inferred |
|-----------|------|-----|------|---------|-----|------|--------------|----------|
| 110C 6/18 | call | 23 | +1,585 | 13,565 | 2,140 | 0.68 | 298 / **1,775** | bearish (written) |
| 94P 6/26 | put | 31 | +1,008 | 1,062 | 1,008 | 4.62 | 507 / 500 | bearish (bought) |
| 99C 6/18 | call | 23 | +582 | 583 | 597 | 2.78 | 117 / **479** | bearish (written) |
| 130C 9/18 | call | 115 | +557 | 5,163 | 924 | 1.42 | 62 / **862** | bearish (written) |
| 150C 1/15 | call | 234 | +536 | 7,208 | 584 | 1.83 | 27 / **557** | bearish (written) |
| 95C 5/29 | call | 3 | +533 | 2,067 | 1,218 | 2.73 | 621 / 586 | **bullish** (net +35) |
| 90P 5/29 | put | 3 | +526 | 2,193 | 1,211 | 1.34 | **811** / 316 | bearish (bought ask) |
| 92P 5/29 | put | 3 | +505 | 1,088 | 1,105 | 2.03 | **681** / 336 | bearish (bought ask) |

The only "bullish" build is the 3-DTE 5/29 95C, and only marginally (net +35). Every
OTM call build above spot is **bid-side = supply**; every near put build is **ask-side
= demand for protection**. This is the OI fingerprint of a **collar/overwrite**, not
accumulation.

### Closing / roll activity — `[OI:decrease_with_volume]` / `[OI:position_rolls]`

- **6/18 125C: −5,989** (13,379→7,390), vol 7,023, avg $0.156 — the day's largest OI
  change; far-OTM call longs unwound/covered into earnings (de-risking).
- Minor: 9/18 125P −244, 6/18 105P −126, 7/17 130C −47. Nothing else material.
- **`oi_position_rolls`: 0 rolls detected** (single-day; near_dte_max 30, threshold 500).

### Smart positioning (inferred direction) — `[OI:smart_positioning]`

Net read: **mildly bearish / hedged.** 7 bearish vs 1 bullish among the builds. Caveat
(phase-3 heuristic + tool note): inference is OPRA-parse + ask/bid based. The bid-side
upside-call writing **coinciding with phase-2 dark-pool stock buying** is the textbook
**covered-call/buy-write signature** — so "bearish" here likely means "capping upside
on a long," not outright bearish. The ask-side put buying is genuine downside demand.

### Pin risk — `[OI:pin_risk]` (dte_max 7)

**PDD absent from top-25.** The 5/29 weekly (3 DTE) does not carry enough concentrated
near-money OI to pin. Monthly OPEX (6/19) is 24 days out. → **no gamma pin into the
print; spot can travel the full implied ±5.69%** [CTX:implied_move_pct]. Pin candidates
this week are HYG/SPY/TLT/QQQ, not PDD.

### OPEX concentration — `[OI:opex_concentration]`

PDD absent (list is micro-caps at 100% single-expiry). PDD's OI is **spread across
expiries** (5/29, 6/5, 6/18, 6/26, 7/17, 8/21, 9/18, 1/15/27). The heaviest standing-OI
expiry is the **6/18 monthly** (95P 19,729; 115C 14,892; 160C 10,907; 125C 7,390 post-
unwind) — the structural OI anchor, but not a near-term cliff.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `oi_biggest_increases` | symbol=PDD, top20, min_chg500 | 8 builds; calls written bid-side, puts bought ask-side |
| `oi_decrease_with_volume` | symbol=PDD, top15, min_vol100 | 6/18 125C −5,989 (de-risk); rest minor |
| `oi_smart_positioning` | symbol=PDD, top20, min_chg500 | 7 bearish / 1 bullish (hedged/overwrite read) |
| `oi_position_rolls` | symbol=PDD, thr500, near_dte30 | 0 rolls |
| `oi_pin_risk` | top25, dte_max7, dist5% | PDD absent → no pin |
| `oi_opex_concentration` | top20, min_conc40% | PDD absent → no single-expiry cliff |

## Tool errors

None.

## Verdict for downstream phases

- **Positioning bias:** **HEDGED / DEFENSIVE, mildly bearish-tilted.** Upside calls
  written, downside puts bought, biggest call line de-risked. Diverges from phase-2's
  dark-pool stock bid — the reconciliation is a **collar/buy-write** (risk-managed long),
  not bullish accumulation. **Flag for phase-10: DP-accumulation vs OI-hedging divergence.**
- **Conviction:** **2/5** (the positioning is real but its *direction* is ambiguous —
  hedged long vs bearish — and resolves toward "defensive," low directional signal).
- **Three pin/cliff strikes for phase-9:**
  1. **94–95** — fresh put OI (94P 6/26, 90/92P 5/29) + huge 6/18 95P (19,729 OI) +
     phase-2 $94.52 DP support. The downside hedge wall / first support.
  2. **No gamma pin** — spot is *free to move* the full implied ±5.69% on the print; do
     not assume a pin holds it near 97/100.
  3. **110 / 125–130** — written-call supply (110C 13,565 OI, 130C builds) caps upside;
     overhead resistance from dealer/overwriter short-call hedging on a rally.
- **Open questions:** Is the call-writing covered (buy-write on the phase-2 stock) or
  naked bearish? Phase-4 dealer GEX/DEX will say whether dealers are long or short gamma
  here, and phase-7c short interest will say if puts are hedges vs a squeeze setup.
