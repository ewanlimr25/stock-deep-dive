# Phase 3 — Open Interest & Positioning

**Ticker:** ENPH
**As-of date:** 2026-05-22
**Generated:** 2026-05-25T22:43:20Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md

## Summary

OI **resolves phase-1's open question**: the June OTM call buildup is **genuine
opening long interest, not covered overwrite**. The standout is **June-18 $70C: OI
+4,616 (1,941→6,557) on prev ask-volume 5,400 vs bid 275** — overwhelmingly ask-driven
= speculative bullish call accumulation, joined by 85C (+2,518) and 95C (+1,340), both
ask-led. Simultaneously the ITM **June $60C is being closed (−1,968)** while the $70C
is opened → an implied **bullish strike-roll up (60→70)**. The offsets are real but
secondary: a **long-dated put hedge is building (Sept $50P +1,721; plus phase-1's
2027-06 $60P)**, and there's mild call *writing* at $80C (bid-led) and July $70C. Net
positioning: **speculative bullish call buildup in June, financed partly by put-selling
(60P/55P bid-led), hedged by a few long-dated puts.** **No near-term pin risk** (ENPH
absent from the OPEX-week pin list; next monthly 6/18 is 27 DTE). Bias **bullish,
conviction 4/5.**

## Key signals

- **June $70C OI +4,616, ask 5,400 vs bid 275 → opening long calls (not overwrite)** [OI:biggest_increases]
- `oi_smart_positioning` infers **bullish** on 70C/85C/95C June (the OI leaders) [OI:smart_positioning]
- ITM **June $60C −1,968** closed while 70C opened → **bullish strike-roll up** [OI:decrease_with_volume]
- **Long-dated put hedge building: Sept $50P +1,721** (prev premium $1.13M) [OI:biggest_increases]
- **No pin risk** — ENPH not in OPEX-week pin list; next monthly OPEX 6/18 (27 DTE) [OI:pin_risk]

## Detailed findings

### Largest OI increases (fresh conviction)

| Strike / Expiry | DTE | OI Δ | prev ask vs bid vol | Inferred | Read |
|-----------------|-----|------|---------------------|----------|------|
| **$70C / 06-18** | 27 | **+4,616** | 5,400 / 275 | **bullish** | flagship opening long call (OTM) |
| $85C / 06-18 | 27 | +2,518 | 2,360 / 601 | bullish | OTM lottery, ask-led |
| **$50P / 09-18** | 119 | +1,721 | 8 / 5 | bearish* | **long-dated put hedge** ($1.13M) |
| $65C / 05-22 (0DTE) | 0 | +1,622 | 3,353 / 1,373 | bullish | expired today — pin noise |
| $80C / 06-18 | 27 | +1,488 | 885 / 1,792 | bearish* | **bid-led = call writing at $80** |
| $95C / 06-18 | 27 | +1,340 | 3,450 / 1,726 | bullish | OTM lottery, ask-led |
| $60P / 06-18 | 27 | +1,145 | 113 / 1,129 | bullish | **bid-led = put selling (bullish)** |
| $55P / 05-22 (0DTE) | 0 | +1,128 | 472 / 985 | bullish | put selling (0DTE) |
| $65C / 05-29 | 7 | +744 | 460 / 739 | bearish* | mild bid-lean |
| $70C / 07-17 | 56 | +715 | 411 / 676 | bearish* | mild call writing at $70 |
| $170C / 2027-01 | 238 | +519 | 511 / 27 | bullish | LEAP lottery (phase-1) |

The OI leaders (70C/85C/95C June) are **ask-driven opening longs** → the call premium
in phase-1 is **directional, not overwrite**. The "bearish" tags on 80C and 50P reflect
*writing* / *hedge* mechanics, not a bearish directional crowd.

### Closing / roll activity

| Strike / Expiry | OI Δ | Volume | Read |
|-----------------|------|--------|------|
| $60C / 06-18 | **−1,968** | 6,837 | ITM call closed → **rolled up to 70C** (bullish) |
| $60C / 05-22 (0DTE) | −1,098 | 11,295 | 0DTE expiry |
| $55C / 05-22 (0DTE) | −827 | 2,670 | 0DTE expiry |
| $50C / 06-18 | −417 | 1,158 | trim of largest standing OI (25,713) |

`oi_position_rolls` detected **0 rolls** — but it only catches near→far *expiry* rolls;
the 60C→70C move is a **same-expiry strike-roll** (both 06-18), which the tool misses.
Flagging it manually: closing ITM 60C + opening OTM 70C in the same expiry = raising the
strike = **bullish roll-up**.

### Smart positioning (inferred direction)

`oi_smart_positioning` net read: bullish dominates the high-OI-change contracts
(70C/85C/95C/170C June+LEAP calls all ask-led bullish; 60P/55P bid-led = bullish put
selling). Bearish tags are confined to (a) the **50P-Sept hedge** and (b) **call
writing** at 80C/70C-July — i.e. premium-supply mechanics, not a downside directional
push. The genuine speculative direction is **bullish.**

### Pin risk

**None applicable.** ENPH is **not** in `oi_pin_risk` (dte_max=7). The pin list is all
`dte_to_opex=0` names with an expiry *today* (SPY, NVDA, AAPL, HYG, TLT…). ENPH's
0DTE 5/22 strikes expired today; its next monthly OPEX (6/18) is 27 DTE out — beyond
the pin window. No OPEX-week pin commentary for this run.

### OPEX concentration

ENPH **outside** `oi_opex_concentration` (≥40% threshold) — the list is 100%-concentration
micro-names. ENPH's OI is spread across strikes/expiries; the single largest standing
contract is **June $50C (OI 25,713)** — a deep-ITM structural block — and June 18 holds
the bulk of fresh activity. No single-expiry cliff risk.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__oi_biggest_increases` | `{symbol: ENPH, top_n: 20, min_oi_change: 500, date: 2026-05-22}` | 70C June +4,616 (ask-led) leads; 85C/95C bullish; 50P-Sept hedge |
| `mcp__uw-pp__oi_decrease_with_volume` | `{symbol: ENPH, top_n: 15, min_volume: 100, date: 2026-05-22}` | 60C June −1,968 (roll-up); 0DTE expiries |
| `mcp__uw-pp__oi_smart_positioning` | `{symbol: ENPH, top_n: 20, min_oi_change: 500, date: 2026-05-22}` | bullish on call leaders; bearish only on hedge/writes |
| `mcp__uw-pp__oi_position_rolls` | `{symbol: ENPH, threshold: 500, near_dte_max: 30, date: 2026-05-22}` | 0 rolls (same-expiry strike-roll not captured) |
| `mcp__uw-pp__oi_pin_risk` | `{top_n: 25, dte_max: 7, max_distance_pct: 5, date: 2026-05-22}` | ENPH absent — no near-term pin |
| `mcp__uw-pp__oi_opex_concentration` | `{top_n: 20, min_concentration_pct: 40, date: 2026-05-22}` | ENPH absent — OI not concentrated |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** **Bullish** — speculative opening long-call buildup (June
  70/85/95C, ask-driven), implied bullish strike-roll 60→70C, financed by put-selling;
  offset only by a contained long-dated put hedge and minor call writing.
- **Conviction:** **4/5** (the 70C +4,616 ask-led opening is unambiguous direction;
  de-rated from 5 by the visible hedge/writing supply and that the biggest builds are
  OTM lottery strikes 85/95C, which is convexity-seeking, not high-probability).
- **Three pin/cliff strikes for phase-9:**
  1. **$70 (June 18)** — the bull magnet: heaviest fresh OI build (+4,616); upside target/strike for structures.
  2. **$60** — the floor: ITM 60C closed/rolled + 60P being *written* → institutions defend the $60 area (aligns with phase-2 support $61–62).
  3. **$50 (June 18, OI 25,713)** — deep structural OI block (aligns with phase-2's $53/$49 shelves) — disaster reference.
- **Open questions:**
  - Is the 50P-Sept + 2027-06 60P hedge protecting these very call/stock longs, or an
    independent bear? (→ phase 8b)
  - With dealers likely **short the heavily-bought 70/85/95C**, does gamma set up a
    squeeze on a move toward $70? (→ phase 4 GEX/vanna)
