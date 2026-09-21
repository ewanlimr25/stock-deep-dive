# Phase 3 — Open Interest & Positioning

**Ticker:** PATH (UiPath Inc.)
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T00:00:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md

## Summary

The OI buildup **reconciles the phase-1 (bearish options) vs phase-2 (DP accumulation)
contradiction**: it is a **two-sided premium-selling / buy-write-collar regime around an
accumulated long**, not directional bearishness. New OI is dominated by **downside put
writing** (5/29 $8.5 +962, $9 +589, $9.5 +347 — all bid-side/sold = "bullish" inference)
and **upside call writing** (6/18 $10 +562 sold, $143K premium; 5/29 $13.5 +358 sold;
0DTE $10.5/$11.5 sold). The phase-1 "bearish premium" is largely **call overwriting**, and
the day's biggest print — the $526K 2027 $10 put — most plausibly the **protective leg of a
collar** on the dark-pool long, not a standalone bear bet. Net posture: **long stock +
sell elevated earnings IV both sides** = neutral-to-mildly-bullish with defined downside
and capped upside. No rolls; PATH outside the market-wide pin/OPEX-concentration leaders.

## Key signals

- **Downside puts being written:** 5/29 $8.5 put OI +962 (1914→2876), $9 +589, $9.5 +347 — all bid-side (sold), `inferred_direction=bullish` [OI:smart_positioning]
- **Upside calls being written:** 6/18 $10 call OI +562, net_ask_bid **−910** (sold), prev_premium $143K [OI:smart_positioning]; 5/29 $13.5 +358 sold [OI:biggest_increases]
- **Standing structural OI:** 2027-01-15 $15 call OI **33,865** (large LEAP); 6/18 $12 call OI 8,801; 5/29 $10 put OI 5,643; 6/18 $10 call OI 5,287 [OI:decrease_with_volume / biggest_increases]
- **No rolls detected** (single-day) and **no closing flush** — largest decrease is just 0DTE $10.5 put −147 (expiry) [OI:position_rolls / decrease_with_volume]
- **PATH not in pin-risk or OPEX-concentration leaders** — its OI is too small vs SPY/HYG/QQQ and is *spread* across 5/29→2028, not cliff-concentrated [OI:pin_risk / opex_concentration]

## Detailed findings

### Largest OI increases (new positions)

| Strike / Expiry | Type | DTE | OI Δ | net_ask_bid | Inferred | Read |
|---|---|---|---|---|---|---|
| $8.5 2026-05-29 | put | 7 | +962 | −38 | bullish | Downside put **written** (income / willing buyer) |
| $10.5 2026-05-22 | call | 0 | +810 | −921 | bearish | 0DTE call **written** (pin) |
| $9 2026-05-29 | put | 7 | +589 | −239 | bullish | Downside put **written** |
| $11 2026-05-22 | call | 0 | +579 | +341 | bullish | 0DTE call bought (pin/gamma) |
| $11.5 2026-05-22 | call | 0 | +579 | −760 | bearish | 0DTE call **written** |
| **$10 2026-06-18** | **call** | 27 | **+562** | **−910** | bearish | **Post-earnings call overwriting**, $143K prem |
| $10.5 2026-05-29 | call | 7 | +556 | +206 | bullish | Earnings-week call bought |
| $13.5 2026-05-29 | call | 7 | +358 | −394 | bearish | OTM call **written** |
| $9.5 2026-05-29 | put | 7 | +347 | −244 | bullish | Downside put **written** |
| $10 2026-05-29 | put | 7 | +327 | +113 | bearish | ATM put bought (hedge) |

**Pattern:** of the 10 largest OI increases, **6 are bid-side (written)** — 3 downside puts
sold + 3 upside/0DTE calls sold. Only the 0DTE $11 call and 5/29 $10.5 call are net-bought
(lottery), plus one ATM 5/29 $10 put bought (hedge). This is the fingerprint of a
**vol-seller / range-harvesting** desk, not a directional bear.

### Closing / roll activity

`position_rolls` → **0 rolls** (single-day detection). `decrease_with_volume` shows only
trivial reductions (0DTE $10.5 put −147 expiring; 6/18 $12 call −58; 2028 $17 call −49) —
**no meaningful position is being closed**. The book is being *added to*, not unwound.

### Smart positioning (inferred direction)

The directional inference is deliberately **muddy** — 4 "bullish" (puts sold + 1 call
bought) vs 4 "bearish" (calls sold + 1 put bought) — precisely because this is a two-sided
premium structure, not a one-way bet. Read mechanically: **puts sold below + calls sold
above = short strangle / collar overlay** on the (phase-2) long. The largest single
directional inference is the 6/18 $10 call written (net_ask_bid −910) — overwriting the
near-term upside into earnings.

### Pin risk (OPEX week)

`oi_pin_risk` (dte_max 7) is led by HYG, SPY, TLT, QQQ, XLF, NVDA — all 0DTE 5/22 monthly
names. **PATH does not rank** (its window OI is far below the ETF/mega-cap leaders). So
no *market-structural* pin on PATH; but internally, PATH's own 5/29 (post-earnings) chain
has a **put shelf at $8.5–$10** (OI: $10 = 5,643; building at 8.5/9/9.5) and **call mass at
$10.5–$13.5** — a self-contained range bracket around the event.

### OPEX concentration

PATH not in the ≥40%-concentration list (all entries are micro-caps at 100%). PATH's OI is
**distributed** across 5/29 (event week), 6/18 (8,801 at $12 call), 7/17, and big LEAPs
(2027 $15 call 33,865; 2028 $17). Distributed OI = lower single-expiry cliff risk, but the
2027 $15 call is a notable long-term ceiling of standing interest.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__oi_biggest_increases` | `{symbol: PATH, min_oi_change: 300, top_n: 20}` | 10 increases; 6 bid-side written (downside puts + upside calls) |
| `mcp__uw-pp__oi_decrease_with_volume` | `{symbol: PATH, min_volume: 100, top_n: 15}` | Only trivial decreases; no position closed |
| `mcp__uw-pp__oi_smart_positioning` | `{symbol: PATH, min_oi_change: 300, top_n: 20}` | 4 bullish / 4 bearish — two-sided premium selling |
| `mcp__uw-pp__oi_position_rolls` | `{symbol: PATH, threshold: 300, near_dte_max: 30}` | 0 rolls |
| `mcp__uw-pp__oi_pin_risk` | `{dte_max: 7, max_distance_pct: 8, top_n: 25}` | PATH absent; ETFs/mega-caps lead |
| `mcp__uw-pp__oi_opex_concentration` | `{min_concentration_pct: 40, top_n: 20}` | PATH absent; OI distributed 5/29→2028 |

## Tool errors

None.

## Verdict for downstream

- **Positioning bias:** **buy-write / collar around an accumulated long** — neutral-to-
  mildly-bullish, downside defined, **upside capped** by call overwriting ($12–$13.5).
  This **resolves the phase-1↔phase-2 contradiction**: the bearish-tagged options premium
  is overwriting against the dark-pool long, not a directional short.
- **Conviction:** **3/5** — the structure is coherent and the book is being added to (no
  unwind), but the directional *edge* is small by design (vol sellers profit from
  rangebound + IV crush, not from a move).
- **Three pin/cliff strikes for phase-9:**
  1. **$10** — strongest magnet/support: 5/29 put wall ($10 OI 5,643 + 8.5/9/9.5 written),
     6/18 $10 call OI 5,287, aligns with DP support shelf $10.38–$10.65 (phase-2). Key
     downside pin.
  2. **$11** — spot battleground: 0DTE $11 call OI 7,545 / $11.5 OI 9,915; = DP $11 ceiling
     (phase-2).
  3. **$12** — upside cap: 6/18 $12 call OI 8,801 + active overwriting → where rallies meet
     written-call supply. (2027 $15 call OI 33,865 = far ceiling.)
- **Open questions:**
  - Is the call writing **covered** (institutions long per phase-2 → confirms long thesis,
    capped upside) or naked? → phase-4 GEX/dealer positioning.
  - Is the 2027 $10 put the **protective leg of a collar** or a standalone long-term bear?
    The buy-write context argues collar. → phase-4 + phase-7.
  - Does the $10 put-wall + DP support stack into a hard floor that survives a soft
    earnings print? → phase-4 gamma, phase-5 historical earnings reaction.
