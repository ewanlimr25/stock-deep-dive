# Phase 4 — Dealer Structure & Gamma

**Ticker:** FSLY
**As-of date:** 2026-05-19  (Effective data date: 2026-05-18)
**Underlying ref:** $16.53
**Generated:** 2026-05-19T00:40:00Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md

## Summary

Dealer structure is **constructive** for FSLY's bullish flow campaign,
with three reinforcing signals. (1) **Term structure is in BACKWARDATION**
(5/22 avg IV 117.7% vs 7/17 82.8%) [STRUCT:iv_term_structure] — a clear
event-premium signature in the front week. (2) **Term skew is reversed
(COMPLACENT label):** 25Δ call IV 83.4% > 25Δ put IV 79.9% at 30 DTE
[STRUCT:term_skew] — a small-cap with calls richer than puts is the
**M&A/contract-win/upside-catalyst signature**. (3) **Vanna is positive
and net charm is positive** ($16,563 / $431,948)
[STRUCT:vanna_charm] — the tool's own read is "classic vanna-squeeze
setup if VIX collapses" because dealers short puts will buy stock as IV
decays. The headline structural risk: total 45-DTE GEX is **negative
−$9.8M** [STRUCT:gex] with the deepest negative gamma well at the
**$17.5 strike (−$21.4M)** — meaning a move *through* $17.5 will
mechanically accelerate (no dealer dampening). For the 4-DTE 5/22
expiry, however, dealer gamma is **positive** with $17.5 acting as a
**support magnet** [STRUCT:today_gamma_flip] and $20 as the resistance
wall. The two horizons disagree because of WHERE on the curve the OI
sits — and that creates the *trade*: long-gamma 5/22 dynamics pull
spot toward $17.5, then short-gamma 9/18 dynamics let it overshoot if
flow stays on the ask.

## Key signals

- **BACKWARDATION with 5/22 IV at 117.7%** [STRUCT:iv_term_structure] —
  a 26-percentage-point spread vs 7/17 (82.8%) tells the market is
  pricing in a binary event inside the next 4 sessions. Likely earnings
  or known catalyst; phase-5/6 must resolve.
- **Reverse 30-DTE skew (call IV > put IV): COMPLACENT label**
  [STRUCT:term_skew] — net 25Δ skew = −0.0351, ratio = 0.958. For a
  $16-handle small-cap, this is one of the cleanest bullish
  positioning signals available.
- **Vanna-squeeze setup is live:** net vanna +16,563, net charm
  +431,948 [STRUCT:vanna_charm]. If FSLY's 100% IV deflates after the
  event, **dealers mechanically buy stock to cover short-put hedges**.
- **GEX dichotomy:** intraday/0DTE dealers are LONG gamma with $17.5
  as **support wall** ($+12.57M GEX) [STRUCT:today_gamma_flip], but
  the full 45-DTE chain has $17.5 as the deepest **NEGATIVE gamma
  pocket** ($−21.4M) [STRUCT:gex]. A clean break of $17.5 unlocks
  acceleration; failure to break holds spot in the $16-17.5 box.
- **DEX skew is bearish-structural:** net DEX −$246.4M (put_dex −$409M,
  call_dex +$163M) [STRUCT:dex] → dealers are short puts → on
  declines they'd mechanically sell. But this is the LEGACY book; new
  flow (phase 1 put-SELLING) is unwinding this position day by day,
  which is precisely the fuel for the vanna squeeze.

## Detailed findings

### GEX (45 DTE)

`options_structure_gex`, dte_max=45, spot=$16.53:

| Field | Value |
|---|---|
| total_gex | **−$9,802,481** |
| zero_gamma_level (ZGL) | $9.00 |
| Spot vs ZGL | spot $7.53 above ZGL (84% above) |
| Tool regime label | POSITIVE |
| Tool regime description | "Dealers net long gamma — expect mean-reversion and reduced volatility" |

Per-strike GEX (top 10 by |magnitude|), 45-DTE:

| Strike | Net GEX | Distance from spot | Role |
|---|---|---|---|
| 17.5 | **−$21,449,093** | +5.9% | Deepest NEG gamma — accelerator strike |
| 20.0 | +$11,685,784 | +21.0% | LONG-gamma magnet ceiling |
| 16.0 | −$8,631,194 | −3.2% | NEG gamma well below spot |
| 15.0 | −$8,243,533 | −9.3% | NEG gamma support |
| 22.5 | +$7,208,627 | +36.1% | LONG-gamma far ceiling |
| 25.0 | +$4,950,650 | +51.2% | LONG-gamma far-far ceiling |
| 19.0 | +$2,650,577 | +14.9% | LONG-gamma sub-magnet |
| 12.5 | −$2,265,601 | −24.4% | NEG gamma tail |
| 16.5 | −$2,111,639 | −0.2% | At-spot NEG gamma |
| 19.5 | +$1,965,086 | +18.0% | LONG-gamma transition |

**Interpretation tension.** The tool labels the regime POSITIVE
(because spot is well above ZGL of $9) but `total_gex` aggregates to
negative because the NEG gamma at $15-$17.5 outweighs the POS gamma
above $19. In practice the per-strike picture is what trades —
**below $18, dealers are net short gamma; from $18.5 to $25, dealers
are net long gamma.** That maps cleanly to the recent trading range
(stock fell from $19 to $16.50) and to the bullish flow campaign
(which targets $17.5-$20).

**Trade implication.** A break above $18.50 puts the stock in
long-gamma terrain where dealers dampen the move; a break above $20
puts it through the largest standing long-gamma wall (the 9/18 20C
2,890 OI from phase-3). Conversely, below $16 spot drops into
deepening NEG gamma — dealer hedging would sell into weakness.
$17.5 is the volatility-acceleration strike in both directions.

### DEX (45 DTE)

`options_structure_dex`, spot=$16.53:

| Field | Value |
|---|---|
| call_dex | +$162,998,838 |
| put_dex | −$409,374,188 |
| net_dex | **−$246,375,350** |
| Interpretation (tool) | "Public is net put-long → dealers net short puts → dealer hedge is to SELL underlying" |

This is a meaningfully bearish *structural legacy* reading — the
standing put book is ~2.5× the standing call book in delta-dollar
terms. **However**, phase-1 and phase-3 show today's flow is
*reducing* the put book (put-selling on the bid across 5/22/7/17/9/18
strikes). The dynamic: as net put OI declines and IV decays,
dealer hedge demand for underlying *shifts from selling to buying*.
This phased unwind is exactly the vanna-squeeze mechanism the next
section captures.

### Vanna + Charm

`options_structure_vanna_charm`, dte_max=45, spot=$16.53:

| Field | Value | Read |
|---|---|---|
| call_vanna | −7,437 | Modest negative |
| put_vanna | +24,000 | Dominant POSITIVE vanna in puts |
| **net_vanna** | **+16,563** | Vanna-squeeze polarity (bullish) |
| **net_charm** | **+431,948** | Time-decay benefits long-stock dealer hedge |
| Tool interpretation | "Public net vanna positive (put-heavy book). Falling IV → \|put delta\| drops → dealers (short puts) cover by BUYING underlying. Classic vanna-squeeze setup if VIX collapses." |

The vanna+charm reading is the **strongest single bullish structural
signal in phase 4**. If the event captured by the 117.7% 5/22 IV
prints and IV collapses 20-30 IV points post-event, dealers will be
mechanically forced to buy stock against their short-put book. That
is, the *resolution* of the binary event — regardless of direction
of the event itself — has a built-in bullish hedge flow embedded in
the dealer book.

### IV term structure — BACKWARDATION

`options_structure_iv_term_structure`:

| Expiry | DTE | Avg IV | Δ vs 7/17 base |
|---|---|---|---|
| 2026-05-22 | 4 | **117.7%** | **+34.9 pp** |
| 2026-05-29 | 11 | 91.0% | +8.2 pp |
| 2026-06-05 | 18 | 85.9% | +3.1 pp |
| 2026-06-12 | 25 | 86.0% | +3.2 pp |
| 2026-06-18 | 31 | 91.0% | +8.2 pp (June OPEX bump) |
| 2026-06-26 | 39 | 85.8% | +3.0 pp |
| **2026-07-17** | **60** | **82.8%** | **base** |
| 2026-09-18 | 123 | 95.5% | +12.7 pp |
| 2026-12-18 | 213 | 96.3% | +13.5 pp |
| 2027-01-15 | 241 | 94.8% | +12.0 pp |
| 2028-01-21 | 613 | 95.5% | +12.7 pp |

The 5/22 spike is the **clear event premium**. Note the *secondary*
hump at 6/18 (91% vs 86% neighbors) — that's the standard June OPEX
implied-vol bump. The trough at 7/17 (82.8%) defines the "no-event"
baseline. Back-end (9/18+) is structurally elevated at 95-97%, which
is consistent with FSLY being a high-vol single name regardless of
event horizon.

No KINK in the term structure (kink_expiry = null) — backwardation
is smooth, not binary-spiked at one expiry. This makes earnings
**slightly less likely** than a generic news/catalyst event (which
would usually concentrate IV in one expiry).

### Term skew — REVERSE / COMPLACENT

`options_structure_term_skew`, dte_target=30:

| Field | Value |
|---|---|
| put_25d_iv | 79.92% |
| call_25d_iv | **83.43%** |
| skew (call − put) | **+0.0351** in OTM-rich-side terms; tool reports −0.0351 |
| skew_ratio | 0.958 (calls > puts) |
| Tool interpretation | COMPLACENT |

**Reverse skew on a $16 small-cap is rare.** It tells us the market
is paying up for upside more than downside, *even at 30 DTE.* For
FSLY specifically, with reverse skew + the BACKWARDATION above + the
ask-side call campaign from phase-1, the structural read converges
on **"market expects a meaningful upside catalyst, soon."**

### Front-end IV ratio

`options_structure_front_end_iv_ratio`, near=7, far=30:

| Field | Value |
|---|---|
| near_iv (actual 10 DTE) | 90.98% |
| far_iv (30 DTE) | 90.99% |
| ratio | **1.000** (FLAT) |

Identical to the 4th decimal place. **The event premium is
concentrated in the front week (5/22), not the front month** —
making a *known* catalyst inside 4 days the most probable
interpretation. After 5/22 passes, the rest of May / early June IV
is at the "ambient" level.

### Today's gamma flip (4-DTE 5/22 expiry)

`options_structure_today_gamma_flip`, spot=$16.53, today_expiry=5/22:

| Field | Value |
|---|---|
| today_zero_gamma | $10.58 |
| today_total_gex | **+$7,699,324** (POSITIVE) |
| atm_flip_strike | $9 |
| Regime | POSITIVE |

| Strike | GEX | Role |
|---|---|---|
| **17.5** | **+$12,570,605** | **SUPPORT wall (magnet)** |
| 15 | −$4,415,954 | Resistance wall |
| 16 | −$3,196,647 | Resistance wall (just below spot) |
| 20 | −$2,847,570 | Resistance wall (ceiling) |
| 19 | +$2,185,208 | Support wall |

**For the next 4 trading days (through 5/22 OPEX): expected pulls.**
- Magnet: $17.5 (largest positive GEX strike).
- Friction zone: $15.5-$16.5 (negative GEX cluster below spot; choppy
  realized vol if spot stays here).
- Ceiling: $20 (negative GEX wall — dealers short calls here, will
  sell rallies).
- Hidden support: $19 (small positive GEX).

The 0DTE-frame and 45-DTE-frame agree on the *direction* (bullish to
$17.5, capped at $20) and *disagree* on the *gamma sign at the
breakout point*. That disagreement IS the trade thesis — see verdict.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|---|---|---|
| `mcp__uw-pp__options_structure_gex` | symbol=FSLY, dte_max=45, date=2026-05-18 | total_gex −$9.8M; ZGL $9; deepest neg gamma at $17.5 |
| `mcp__uw-pp__options_structure_dex` | symbol=FSLY, dte_max=45, date=2026-05-18 | net_dex −$246M; legacy put-heavy book |
| `mcp__uw-pp__options_structure_vanna_charm` | symbol=FSLY, dte_max=45, date=2026-05-18 | net_vanna +16,563; net_charm +432K; classic vanna-squeeze polarity |
| `mcp__uw-pp__options_structure_iv_term_structure` | symbol=FSLY, date=2026-05-18 | BACKWARDATION; 5/22 IV 117.7% vs 7/17 82.8% |
| `mcp__uw-pp__options_structure_term_skew` | symbol=FSLY, dte_target=30, date=2026-05-18 | REVERSE / COMPLACENT skew; call IV > put IV |
| `mcp__uw-pp__options_structure_front_end_iv_ratio` | symbol=FSLY, near_dte=7, far_dte=30, date=2026-05-18 | ratio = 1.000 FLAT (10 vs 30 DTE) |
| `mcp__uw-pp__options_structure_today_gamma_flip` | symbol=FSLY, date=2026-05-18 | POSITIVE regime; $17.5 = support wall, $20 = resistance |

## Tool errors

(none)

## Verdict for downstream phases

- **Dealer regime:** *transitional / pivoting.* Spot is in the
  short-gamma / chop zone ($16-17.5) on the 4-DTE frame but the next
  magnet pull is upward to $17.5 SUPPORT wall, and reverse skew +
  backwardation + positive vanna all point bullish.
- **Conviction:** 4 / 5 — the structural picture is internally
  consistent (term/skew/vanna all aligned bullish) and corroborates
  the flow data from phase-1.
- **Three structural levels for phase-9:**
  1. **$17.50 — pivot/magnet (both 4-DTE support wall and 45-DTE
     acceleration strike).** A close above $17.50 unlocks
     short-gamma terrain above and a fast move toward $20.
  2. **$20.00 — primary ceiling.** 45-DTE long-gamma magnet AND
     5/22 short-gamma resistance wall (different signs but same
     effective behavior: dealer-supplied supply at $20).
  3. **$15.50 / $15.00 — invalidation floor.** Negative-gamma
     pocket below spot; a break of $15.50 puts dealers into
     amplification mode to the downside.
- **Open questions:**
  - What is the 5/22 event? IV 117.7% with no kink and FLAT 10vs30
    ratio is consistent with a known calendar item rather than a
    rumor. Earnings is a candidate. → phase-6 catalyst search +
    phase-5 historical earnings IV pattern.
  - If the event has already happened (e.g. earnings in early May)
    and IV is still elevated, why? Litigation? Buyout speculation?
    → phase-7 insights composite + phase-8 analyst views.
  - Can the vanna-squeeze be timed? It triggers when IV mean-
    reverts. → phase-5 historical IV percentile / z-score will
    tell us whether 100% IV is rich or normal for FSLY.
