# Phase 4 — Dealer Structure & Gamma

**Ticker:** SMH
**As-of date:** 2026-05-28
**Generated:** 2026-05-29T12:40:00Z
**Upstream phases cited:** phase-1-flow.md, phase-3-positioning.md, phase-2-dark-pool.md

## Summary

The dealer structure is a **"pinned-with-a-trapdoor"** setup. Spatially, dealers are
**long gamma at and above spot** (positive GEX $595–650, epicenter +$7.4M at 600)
which **pins/mean-reverts SMH around $600–620** and caps rallies, but **short gamma
below ~$585 with a major short-gamma well at $550 (−$16.0M net GEX)** `[STRUCT:gex]`
— exactly where the phase-1/phase-3 put hedges (550P $24M, 530P roll) are stacked. Net
total GEX is **−$26.5M (net short gamma)**, the put-heavy book's footprint. Offsetting
the downside-gamma risk, **DEX is +$3.95bn — dealers are net short calls and hedge by
BUYING dips** (a supportive bid) `[STRUCT:dex]`. IV is in **BACKWARDATION** with a
**front-end ratio of 1.556 (7d IV 84% vs 30d IV 54%)** — strong near-term event stress
priced into the ~June 4–5 window `[STRUCT:front_end_iv]` — yet the **30-DTE 25Δ skew is
NORMAL (1.039)** `[STRUCT:term_skew]`, i.e. the hedging is **orderly, not panic**. The
**ZGL (269.92) is a coarse/broken artifact** for this ETF; discount the tool's
"POSITIVE regime" label and read the per-strike shape + negative total GEX instead.

## Key signals

- **Short-gamma well at $550: net GEX −$16.0M** — the single largest strike, a
  downside accelerant; the put hedges sit right on it `[STRUCT:gex]`.
- **Long-gamma cushion $595–650** (600 +$7.4M, 620 +$5.0M, 605 +$3.8M, 595 +$3.4M)
  → near-term pin/mean-reversion around $600–620, rallies sold by dealers `[STRUCT:gex]`.
- **Net total GEX −$26.5M** = net short gamma (put-heavy book) → vol-expansion risk if
  spot leaves the long-gamma zone `[STRUCT:gex]`.
- **DEX +$3.95bn** → dealers net short calls, **hedge by buying dips** (supportive,
  partially offsets the downside trapdoor) `[STRUCT:dex]`.
- **Front-end IV ratio 1.556** (7d 84% vs 30d 54%), **BACKWARDATION** → near-term
  catalyst priced ~June 4–5; but **30D skew NORMAL (1.039)** = orderly protection
  `[STRUCT:front_end_iv][STRUCT:term_skew]`.

## Detailed findings

### GEX (dte≤45) `[STRUCT:gex]`

- total_gex **−26,465,241** (net short gamma); underlying_price 600.38; ZGL 269.92
  (**unreliable** — far below spot, an artifact; the per-strike flip is ~$585–595).
- Tool regime label "POSITIVE / dealers net long gamma" is derived from the broken
  ZGL — **discounted**. The per-strike data is the truth:

| Above spot (long γ) | net GEX | | Below spot (short γ) | net GEX |
|---|---|---|---|---|
| 600 | +7.38M | | **550** | **−15.98M** |
| 620 | +5.03M | | 540 | −2.13M |
| 605 | +3.84M | | 585 | −1.72M |
| 595 | +3.39M | | 575 | −1.60M |
| 610 | +3.19M | | 545 | −1.36M |
| 650 | +2.18M | | 577.5 | −1.36M |
| 625 | +1.87M | | 560 | −1.23M |

The flip from long→short gamma is around **$585–595**. Below it, dealer hedging
**amplifies** moves; the −$16M at 550 is the accelerant strike.

### DEX (dte≤45) `[STRUCT:dex]`

net_dex **+$3,952,471,499**. Public is net **call**-long (standing OI), so dealers
are net short calls → dealer hedge is to **BUY underlying** on dips. Supportive bid;
this is the standing book (upside held), distinct from today's put-heavy *flow*. It
cushions the downside trapdoor unless a catalyst overwhelms it.

### Vanna + charm (dte≤45) `[STRUCT:vanna_charm]`

net_vanna **−6,343** (small), net_charm **−1,397,247**. No squeeze signal. Coarse
closed-form approximations; not a material driver here. No vanna-squeeze setup.

### IV term structure & front-end `[STRUCT:iv_term_structure][STRUCT:front_end_iv]`

- Structure: **BACKWARDATION** (front > back).
- Front-end ratio **1.556**: near_iv (7d) **0.8426** vs far_iv (30d) **0.5414**.
- 7-DTE IV at **84%** is elevated → a near-term event (~June 4–5) is being priced.
  ETFs have no earnings, so this is **macro/positioning-driven** (hand to phase-6:
  what's on the calendar that week?).

### Term skew (30-DTE 25Δ) `[STRUCT:term_skew]`

skew_ratio **1.039** (put 25Δ IV 0.4799 vs call 0.462), interpretation **NORMAL**.
Despite heavy put *buying*, the 30D skew is barely elevated → **orderly hedging, not
fear-driven tail panic**. (Panic would show a steepening 25Δ put skew.)

### Today's gamma flip (0DTE)

**Skipped** — `today-gamma-flip` is 0DTE/intraday-only; this is an after-hours as-of
run (2026-05-28 EOD), so it has no meaningful read.

## Tool calls (audit trail)

| Command | Result summary |
|---------|----------------|
| `uw options-structure gex --symbol SMH --dte-max 45` | total −26.5M; 550 −16M well; 595–650 long-γ cushion |
| `uw options-structure dex --symbol SMH --dte-max 45` | +$3.95bn; dealers buy dips |
| `uw options-structure vanna-charm --symbol SMH --dte-max 45` | vanna −6,343, charm −1.4M; no squeeze |
| `uw options-structure iv-term-structure --symbol SMH` | BACKWARDATION |
| `uw options-structure front-end-iv-ratio --symbol SMH --near-dte 7 --far-dte 30` | 1.556 (84% vs 54%) |
| `uw options-structure term-skew --symbol SMH --dte-target 30` | 1.039 NORMAL |
| `uw options-structure today-gamma-flip` | skipped (0DTE/intraday, after-hours run) |

## Tool errors

- GEX `zero_gamma_level` = 269.92 is a coarse/unreliable artifact for this ETF
  (per the tool's own "most meaningful for index products / deep-OI" note). Not a
  hard error; flagged and worked around using per-strike GEX + total_gex.
- `iv-term-structure` `term_structure` rows returned `None`/`None` (dte/iv null);
  only the `structure` headline (BACKWARDATION) is usable. Front-end ratio tool
  supplied the actual near/far IV values.

## Verdict for downstream

- **Dealer regime:** **Transitional / net short gamma.** Long gamma at-and-above spot
  ($595–650) → near-term **pin around $600–620, capped rallies**; short gamma below
  ~$585 with a **−$16M well at $550** → downside **amplification** if the flip breaks.
  DEX (+$3.95bn, buy-the-dip) cushions but does not eliminate the trapdoor.
- **Conviction:** **3/5** (per-strike shape and total GEX are clear; the broken ZGL
  and coarse vanna/charm reduce confidence in the precise flip level).
- **Three structural levels for phase-9:**
  1. **$585–595** — the gamma flip zone; above = dealer-stabilized, below = amplified.
     The key line that turns the put hedges "live."
  2. **$550** — short-gamma epicenter (−$16M); a downside accelerant and the marquee
     hedge strike. A break of $585 likely gravitates here fast.
  3. **$600 / $620** — long-gamma pins / upside cap (rallies sold by dealers); $612.30
     52-wk high sits inside this cap.
- **Open questions:** What is the ~June 4–5 catalyst the 84% front-end IV is pricing
  (phase-6 macro calendar)? Given DEX buy-the-dip support *and* a short-gamma well at
  550, the market is set up to **pin near $600 into the catalyst, then move violently
  if $585 breaks** — does phase-5 history show how SMH resolves backwardation +
  short-gamma setups (mean-revert vs trend)?
