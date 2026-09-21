# Phase 4 — Dealer Structure & Gamma

**Ticker:** ADBE
**As-of date:** 2026-05-29
**Generated:** 2026-05-30T20:00:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md

## Summary

ADBE is in a **long-gamma / positive-GEX regime**: total GEX **+$26.6M** with the
**Zero Gamma Level at 140**, far below spot (~257–259) [STRUCT:gex]. Spot trades
well *above* ZGL, so dealers are net long gamma and **sell rallies / buy dips →
suppressed realized vol, mean-reversion, and a pull toward the OI pin**. That pin
sits **below spot**: max pain is **245 for the 6/5 weekly and 250 for the 6/12
(post-earnings) expiry** [STRUCT:max_pain]. DEX is strongly positive (**+$401M**;
public net call-long → dealers short calls → **dealer hedge is to BUY the
underlying**) [STRUCT:dex] — a mild mechanical bid that *supports* spot near-term
even as the gamma/pin structure caps upside at the 260 wall. The vol surface is an
**earnings kink**: front weekly 6/5 IV 47.5% (expires *before* the print) vs the
**6/12 earnings expiry at 71.4%** [STRUCT:iv_term_structure] — the tool labels the
overall curve CONTANGO because the pre-earnings weekly is cheap, but the tradeable
signal is the earnings vol bubble. 30-day skew is mildly **COMPLACENT** (25Δ call
IV 59.7% > put IV 57.4%, skew_ratio 0.961) — slight *call* richness, no fear bid.

## Key signals

- **Long-gamma regime:** total GEX **+$26.6M**, ZGL **140** ≪ spot → dealers damp
  moves, mean-reversion + pin pull [STRUCT:gex].
- **Pin magnets below spot:** max pain **245** (6/5, P/C OI 0.62) and **250**
  (6/12 earnings, P/C OI **1.29** — put-heavy), distance −5.45% / −3.52%
  [STRUCT:max_pain].
- **DEX +$401M, dealers must BUY underlying** (public call-long) — supportive
  near-term hedging bid [STRUCT:dex].
- **Earnings vol kink:** 6/5 IV 47.5% (pre-print) vs 6/12 IV **71.4%** (earnings)
  → buying the 6/12 expiry pays a steep event premium [STRUCT:iv_term_structure].
- **Skew COMPLACENT:** 25Δ call IV 59.7% > put IV 57.4% (skew_ratio 0.961) — no
  downside fear premium; slight upside-call lean [STRUCT:term_skew].

## Detailed findings

### GEX — `[STRUCT:gex]`

- **Total GEX: +$26,642,775 (POSITIVE)** → **long-gamma regime.**
- **Zero Gamma Level: 140** — far below spot (~257). Spot is deep in positive-gamma
  territory; the whole tradeable range is long-gamma, so dealer hedging is
  **stabilizing** (sell strength / buy weakness).
- Per-strike resolution is **coarse for a single name** (the tool itself warns GEX
  is most meaningful for index products); the largest |GEX| nodes in the captured
  window sit at **200 (−$354k)** and **210 (−$343k)** (OTM, below spot). Treat ZGL
  140 as a ±2% band and the regime sign (positive/long-gamma) as the durable read,
  not the exact node.

### DEX — `[STRUCT:dex]`

- **Net DEX +$401,490,348** (call_dex +$845M, put_dex −$444M). Public is net
  call-long → dealers are net short calls → **dealer delta hedge is to BUY the
  underlying.** Near-term mechanical support for spot, reinforcing the
  long-gamma "buy dips" behavior.

### Vanna + charm — `[STRUCT:vanna_charm]`

- net_vanna **−1,041** (small, call-heavy book), net_charm **+31,068**,
  `squeeze_signal: null`. **No vanna squeeze.** The flagged risk is the *unwind*:
  on a **post-earnings IV crush**, falling IV drops call deltas → dealers (short
  calls) cut their long-underlying hedge → **mechanical selling pressure** after
  6/11. A headwind for any naked long held through the print.

### IV term structure — `[STRUCT:iv_term_structure]`

| Expiry | DTE | avg IV |
|--------|-----|--------|
| 2026-06-05 | 6 | 47.5% (pre-earnings weekly — cheap) |
| **2026-06-12** | **13** | **71.4%** (first post-earnings — event bubble) |
| 2026-06-18 | 19 | 67.5% |
| 2026-06-26 | 27 | 59.6% |
| 2026-07-02 | 33 | 58.0% |
| 2026-08-21 | ~84 | ~51% |

Tool label: **CONTANGO** (front weekly < back) and `kink_expiry: null`, but the
**13-DTE 6/12 spike to 71.4%** is the true structure — a classic earnings kink.
front-end-iv-ratio 0.797 (6d 47.5% / 27d 59.6%) = CONTANGO, an artifact of the
6/5 weekly expiring before the print. **Implication:** sell the rich 6/12 vol or
spread it; do not buy the 6/12 expiry outright.

### Term skew — `[STRUCT:term_skew]`

25Δ call IV **59.7%** vs 25Δ put IV **57.4%**, skew **−0.0231**, skew_ratio
**0.961**, interpretation **COMPLACENT**. Calls are *richer* than puts — no
tail-hedging bid, mild upside-call demand. Consistent with phase-1's call-tilted
tape, but "complacent" is also a yellow flag: little downside protection is being
priced into a name that reports in ~2 weeks.

### Front-end IV ratio — `[STRUCT:front_end_iv_ratio]`

ratio **0.797**, regime **CONTANGO** (near 6d 47.5% < far 27d 59.6%). Reflects the
cheap pre-earnings weekly, not calm — the event premium lives in 6/12+.

### Max pain (opex gravity) — `[STRUCT:max_pain]`

| Expiry | Max pain | Dist % | P/C OI ratio |
|--------|----------|--------|--------------|
| 2026-05-29 (0DTE) | 245 | −5.45 | 0.62 |
| 2026-06-05 (7) | **245** | −5.45 | 0.76 |
| 2026-06-12 (earnings) | **250** | −3.52 | **1.29** |
| 2026-06-18 (monthly) | 250 | −3.52 | 1.04 |
| 2026-06-26 | 240 | −7.38 | 0.70 |

Every near-expiry max-pain strike sits **below spot (245–250)** — in a long-gamma
regime that is a **downward pin pull** toward 250 into the 6/12 earnings expiry,
where the P/C OI ratio (1.29) is the most put-heavy. This **disagrees with the
bullish flow tape** and agrees with phase-3's call-writing read: the chain's
gravity is *down* to 250, not up through the 260 wall.

### Today's gamma flip

After-hours run (as-of EOD), so `today-gamma-flip` (0DTE intraday) is not
meaningful — skipped per phase instructions.

## Tool calls (audit trail)

| Command | Result summary |
|---------|----------------|
| `uw options-structure gex --symbol ADBE --dte-max 45 --date 2026-05-29` | total GEX +$26.6M, ZGL 140, POSITIVE/long-gamma |
| `uw options-structure dex --symbol ADBE --dte-max 45 --date 2026-05-29` | net DEX +$401M; dealers buy underlying |
| `uw options-structure vanna-charm --symbol ADBE --dte-max 45 --date 2026-05-29` | net_vanna −1,041; no squeeze; IV-crush unwind = sell pressure |
| `uw options-structure iv-term-structure --symbol ADBE --date 2026-05-29` | CONTANGO label; real story = 6/12 earnings kink 71.4% |
| `uw options-structure term-skew --symbol ADBE --dte-target 30 --date 2026-05-29` | skew_ratio 0.961, COMPLACENT (calls richer) |
| `uw options-structure front-end-iv-ratio --symbol ADBE --near-dte 7 --far-dte 30 --date 2026-05-29` | ratio 0.797, CONTANGO |
| `uw options-structure max-pain --symbol ADBE --dte-max 30 --date 2026-05-29` | pins 245 (6/5) / 250 (6/12, P/C OI 1.29) — below spot |

## Tool errors

None. (GEX per-strike resolution is coarse for single names — flagged in findings,
not an error.)

## Verdict for downstream phases

- **Dealer regime:** **LONG GAMMA (positive GEX, ZGL 140 ≪ spot)** → vol
  suppression, mean-reversion, pin pull. DEX +$401M adds a near-term supportive
  hedging bid, but the pin pull is **down toward 245–250**, not up.
- **Conviction:** **3 / 5** on the structural read (regime is clear; per-strike GEX
  is coarse).
- **Structural levels for phase-9:**
  1. **Near-expiry max-pain 245 (6/5) / 250 (6/12)** — the opex-gravity magnets,
     below spot [STRUCT:max_pain].
  2. **ZGL 140** (regime boundary; coarse — treat as "spot is far above flip, solid
     long-gamma") [STRUCT:gex].
  3. **260 call wall** (from phase-3 `oi-by-strike`) reinforced here as the upside
     cap the long-gamma regime defends [OI:oi_by_strike].
- **The structural read is a brake on the bullish flow:** long gamma + max-pain
  below spot + complacent skew + an earnings IV kink = **range/pin into the print,
  not a breakout** — favor defined-risk and selling rich 6/12 vol over buying it.
- **Open questions:** Does the DEX buy-hedge bid hold spot at 259–260 into 6/5, or
  does the 250 max-pain win? Will the post-earnings vanna/charm IV-crush unwind add
  selling on 6/12? Is the cumulative 90d premium flow (phase-5) actually building a
  directional long, or churning?
