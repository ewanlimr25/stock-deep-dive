# Phase 4 — Dealer Structure & Gamma

**Ticker:** HOOD
**As-of date:** 2026-05-27
**Generated:** 2026-05-28T14:03:50Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md

## Summary

Dealers are **net short gamma** with spot 76.2 sitting **below the Zero Gamma Level
77.85** — the regime is amplification, not pinning, *below* the flip. But the gamma
map is asymmetric: there is a **hard positive-gamma cap at 78–80** (+$13.3M @80,
+$12.2M @78 — dealers sell rallies into it) and **slippery negative-gamma support at
70–75** (−$3.0M @70, dealers sell into dips). Net mechanical read: **range-bound and
capped above, with downside that accelerates if 75 breaks.** Layered on top is a
**vanna selling headwind** — the book is call-heavy and IV rank is low (23) in mild
backwardation, so as front-month IV bleeds, dealers (short calls) cut long-underlying
hedges → mechanical selling, exactly the pressure behind the recent 80.78→76.23 fade.
Skew is NORMAL (1.034), so no tail-hedge panic. **Verdict: SHORT-γ below 77.85,
capped at 78–80; mildly bearish/range mechanical lean while IV falls.**

## Key signals

- **GEX regime NEGATIVE:** total_gex +$39.1M but spot 76.2 < **ZGL 77.85** → dealers
  net short gamma, "expect trend acceleration and increased volatility" [STRUCT:gex].
- **Positive-gamma wall 78–80** (net_gex +$12.2M/+$13.3M) = resistance/pin cap;
  **negative-gamma 70–75** (−$3.0M @70) = slippery support [STRUCT:gex].
- **DEX net +$168.2M**, dealers net short calls → standing **buy-hedge** (supportive)
  *while IV is stable* [STRUCT:dex].
- **Vanna headwind:** net_vanna −1,942 (call-heavy book); falling IV → dealers cut long
  hedge → **selling pressure** [STRUCT:vanna_charm] — matches the price fade.
- **Term structure BACKWARDATION** (front 5/29 IV 76.5% vs 8DTE 64.5%, ratio 1.052);
  skew **NORMAL** 1.034 — front elevation is 2DTE/OPEX, not earnings (next ER 7/29)
  [STRUCT:iv_term_structure][STRUCT:term_skew][STRUCT:front_end_iv_ratio].

## Detailed findings

### GEX (gamma exposure) [STRUCT:gex]

- total_gex **+$39.08M**, **ZGL 77.85**, spot 76.20, regime **NEGATIVE** ("Dealers net
  short gamma — expect trend acceleration and increased volatility").
- Positive-gamma strikes (stabilizing / resistance walls, dealers sell rallies):

  | Strike | net_gex |
  |--------|---------|
  | **80** | +$13.25M |
  | **78** | +$12.24M |
  | 77 | +$5.08M |
  | 79 | +$4.75M |
  | 76 | +$4.56M |
  | 83 | +$4.12M |

- Negative-gamma strikes (amplifying / slippery support, dealers sell dips):

  | Strike | net_gex |
  |--------|---------|
  | **70** | −$3.01M |
  | 65 | −$2.53M |
  | 72 | −$2.36M |
  | 74 | −$2.26M |
  | 75 | −$2.13M |
  | 73 | −$1.85M |

The structure is a **bowl**: positive gamma stacked 76–80 (cap), negative gamma 65–75
(slippery floor). Spot 76.2 sits just inside the lower edge of the positive band. To
flip into a stabilizing long-gamma regime, price must clear **77.85–78**; lose **75**
and dealer hedging amplifies the move toward 73–70. (GEX caveat: "most meaningful for
index/large-cap with deep OI" — HOOD qualifies but treat ZGL as a ±2% band, ~76.3–79.4.)

### DEX (dealer delta) [STRUCT:dex]

net_dex **+$168.2M** (call_dex +$644.1M, put_dex −$475.9M). Interpretation: public net
call-long → dealers net short calls → **dealer hedge is to BUY underlying**. This is a
standing supportive bid — but it is conditional on IV/delta stability; the vanna line
below shows what happens when IV falls.

### Vanna + charm [STRUCT:vanna_charm]

net_vanna **−1,942** (call-heavy book), net_charm **+717,347**, call_vanna −7,569,
put_vanna +5,627. Tool interpretation: "Public net vanna negative... Falling IV → call
delta drops → dealers (short calls) cut long-underlying hedge → **SELLING pressure**.
Rising IV reverses." With IV rank at 23 and front-month in backwardation (front IV
likely to bleed post-5/29 OPEX), the near-term vanna flow is a **headwind**. This is
the mechanical engine behind the 80.78→76.23 drift on declining IV.

### IV term structure [STRUCT:iv_term_structure]

**BACKWARDATION.** Front-loaded: 5/29 (1DTE) 76.5%, 6/05 (8DTE) 64.5%, 6/12 63.5%,
6/18 65.0%, 6/26 61.3%, 7/02 60.6%, then LEAPs rising back to 66–70%. The 5/29 spike is
**2DTE OPEX gamma/weekly effect, not an earnings event** (next ER 2026-07-29). The
2–6 week belly (60–63%) is the cheapest part of the curve.

### Term skew & front-end IV [STRUCT:term_skew][STRUCT:front_end_iv_ratio]

- term-skew ratio **1.034 → NORMAL** (25Δ puts only ~3% richer than calls). No
  steepening, no tail-hedge demand — consistent with phase-3's put-*selling*.
- front-end-iv-ratio **1.052 (BACKWARDATION)**, near(8d) 0.645 / far(29d) 0.613 — mild
  event/OPEX stress, nothing extreme.

### Today's gamma flip

**Skipped** — `today-gamma-flip` is 0DTE intraday-only; this is an EOD/after-hours
as-of run (2026-05-27 close). Not meaningful post-session.

## Tool calls (audit trail)

| Command | Result summary |
|---------|----------------|
| `uw options-structure gex --symbol HOOD --dte-max 45 --date 2026-05-27` | total +$39.1M, ZGL 77.85, spot 76.2, NEGATIVE; walls 78/80 (+), 70 (−) |
| `uw options-structure dex --symbol HOOD --dte-max 45 --date 2026-05-27` | net_dex +$168.2M, dealers buy-hedge |
| `uw options-structure vanna-charm --symbol HOOD --dte-max 45 --date 2026-05-27` | net_vanna −1,942; falling IV → selling pressure |
| `uw options-structure iv-term-structure --symbol HOOD --date 2026-05-27` | BACKWARDATION, front 5/29 76.5% |
| `uw options-structure term-skew --symbol HOOD --dte-target 30 --date 2026-05-27` | ratio 1.034 NORMAL |
| `uw options-structure front-end-iv-ratio --symbol HOOD --near-dte 7 --far-dte 30 --date 2026-05-27` | 1.052 BACKWARDATION |
| `uw options-structure today-gamma-flip` | skipped (0DTE intraday only) |

## Tool errors

None. (per-strike GEX field is `net_gex`, not `gex`; term-skew `put_iv`/`call_iv` null
in this build but `skew_ratio`+`interpretation` resolve the read.)

## Verdict for downstream

- **Dealer regime:** **SHORT GAMMA / transitional** — spot 76.2 below ZGL 77.85;
  amplification below the flip, hard positive-gamma cap 78–80, slippery support 70–75.
  Mechanical lean **mildly bearish/range** while IV declines (vanna selling).
- **Conviction:** **3/5** (GEX/DEX/vanna agree on a coherent, capped-range mechanical
  picture — higher conviction than the noisy flow/DP phases).
- **Three structural levels for phase-9:**
  1. **ZGL 77.85 (≈78)** — gamma flip / regime pivot. Reclaim & hold above ≈78 = flip
     to long-gamma, removes the cap → bullish trigger. This is *the* level.
  2. **78–80 positive-gamma wall** — resistance/pin cap (aligns with phase-3 written-80
     wall + pin@78). Upside is heavily dealer-supplied here.
  3. **75 → 70 negative-gamma zone** — lose 75 and hedging accelerates downside toward
     73.64 (phase-2 DP shelf) / 70 (put-selling floor + largest negative GEX).
- **Open questions:**
  - Does macro/regime (phase-6) favor a vol expansion that would break the 78 cap
    upward, or continued vol compression that keeps the vanna selling on?
  - The DEX buy-hedge vs the vanna sell-hedge partly offset — net near-term is the
    vanna headwind while IV falls; would a catalyst (phase-6/7c) reverse IV and flip
    vanna supportive?
