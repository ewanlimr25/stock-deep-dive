# Phase 3 — Open Interest & Positioning

**Ticker:** CMPS
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T00:00:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md

## Summary

**This phase materially revises the phase-1 "soft-bearish" read toward net-bullish
positioning.** What *stuck as overnight OI* (vs the intraday aggressor tape phase-1
saw) is a coherent bullish structure: a **call roll-up-and-out** (near-term OI −682,
far-term **+3,820**), with the Jun $11 call (OI **−753**) as the *closing* leg and the
Jul $12 call (OI **+1,962, ask-side bought**) as the *opening* leg. The marquee Jul $13
call that dominated phase-1's volume (4,894 contracts) added only **+324 OI** — i.e. it
was mostly intraday churn / a facilitated cross, **not** a big sold-to-open overwrite.
On the put side, a **bull-put-spread + tail hedge**: Jun $11 put **sold** (+2,139 OI,
bid-side = income/willing to own at $11) financed against a Jun $10 put **bought**
(+2,191 OI, ask-side = $10 downside protection). Reconciled with phase-2's dark-pool
buying (`buy_ratio 0.839`), the institutional read is **constructive**: accumulate
shares, roll long calls up and out, write puts for income, hedge the tail below $10.
Conviction tempered by modest sizes (1,500–2,200 contracts) and the explicit $10 hedge.

## Key signals

- **Call roll-up-and-out**: near OI −682 / far OI **+3,820**, roll_size 682, balance_ratio 0.179 `[OI:position_rolls]` — bullish continuation.
- **Jul $12 call OI +1,962** (curr 4,361), prev ask-vol 2,219 vs bid 316 → **bought-to-open**, inferred bullish `[OI:smart_positioning]`.
- **Jun $11 call OI −753** (curr 10,553, still the largest single strike), vol 2,761 → near-term longs **closing** (the roll's near leg) `[OI:decrease_with_volume]`.
- **Jun $11 put OI +2,139** sold (bid-vol 2,198 vs ask 78) → put-writing, inferred bullish `[OI:smart_positioning]`.
- **Jun $10 put OI +2,191** bought (ask-vol 322 vs bid 140) → genuine **$10 tail hedge**, inferred bearish `[OI:smart_positioning]` `[OI:biggest_increases]`.
- Jul $13 call OI only **+324** despite 4,894 vol → churn, not position-building (corrects phase-1) `[OI:biggest_increases]`.

## Detailed findings

### Largest OI increases (05-21 → 05-22) `[OI:biggest_increases]` `[OI:smart_positioning]`

| contract | DTE | OI Δ | curr OI | avg px | prev ask/bid vol | inferred | read |
|----------|-----|------|---------|--------|------------------|----------|------|
| Jun $10 **put** | 27 | **+2,191** | 2,619 | $0.32 | 322 / 140 (ask) | bearish | **bought** — $10 tail hedge |
| Jun $11 **put** | 27 | **+2,139** | 2,587 | $0.70 | 78 / 2,198 (bid) | bullish | **sold** — put write / own at $11 |
| Jul $12 **call** | 56 | **+1,962** | 4,361 | $1.54 | 2,219 / 316 (ask) | bullish | **bought** — call accumulation |
| Jan'27 $5 put | 238 | +388 | 425 | $0.49 | 400 / 0 (ask) | bearish | bought — cheap deep tail |
| Jan'27 $9 call | 238 | +363 | 610 | $4.68 | 0 / 410 (bid) | bearish | ITM call sold (small) |
| Jul $13 call | 56 | +324 | 383 | $1.40 | 249 / 144 | bullish | small — churn, see note |
| Aug $16 call | 91 | +307 | 377 | $1.14 | 5 / 110 (bid) | bearish | far-OTM call sold (small) |

The **net-bullish** OI builds (Jul $12 calls bought +1,962; Jun $11 puts sold +2,139)
outweigh the **hedge** builds (Jun $10 puts bought +2,191; small Jan'27 $5 puts). The
$11-put-sold / $10-put-bought pair is a textbook **bull put spread** (net credit,
bullish, max loss below $10) — or two players, but the strikes/DTE alignment favours a
single structured trade.

### Closing / roll activity `[OI:decrease_with_volume]` `[OI:position_rolls]`

- **Jun $11 call OI −753** (curr 10,553), vol 2,761 — the day's only large *decrease*.
  This is the **near leg of the roll**: longs closing Jun $11 calls (shows as bid-side
  "selling" in phase-1) while opening Jul $12 calls. **This reframes phase-1's bid-side
  call premium as roll/closing flow, not bearish initiation.**
- `oi_position_rolls`: **1 roll**, call type, near_oi_change −682, far_oi_change
  **+3,820**, roll_size 682, balance_ratio 0.179. Calls migrating Jun → Jul/Aug. A
  **bullish roll-up-and-out** — maintaining/extending upside exposure after the +26% run.
- Other decreases are immaterial (Jun $8 put −197, Jun $8 call −179, Jan'27 $10 call −84).

### Smart positioning (inferred) `[OI:smart_positioning]`

Net of the inferred-direction tags: **bullish** legs (Jul $12 call +1,962 bought; Jun
$11 put +2,139 sold) dominate the conviction-sized builds; **bearish** tags are the $10
put hedge (+2,191) and small far-OTM/LEAP odds-and-ends. Note the tool's "bearish" tag
on the Jun $10 *bought put* is correct (long puts = downside bet/hedge) — but in context
it is **protection wrapped around a bullish core**, not a standalone bear thesis.

### Pin risk

**N/A.** Nearest monthly OPEX is Jun 18 = **27 DTE**; `oi_pin_risk` (dte_max 7) would
return empty. No OPEX-week pin to model as of 2026-05-22. Re-check inside the week of
Jun 15.

### OPEX concentration `[OI:opex_concentration]`

CMPS does **not** appear in the market-wide top-20 at the ≥40% single-expiry threshold
(list is all 100%-concentration micro-names — PMCB, SABS, PLBY, etc.). CMPS's total OI
(89,658) is **spread across expiries**, with the Jun 18 and Jul 17 monthlies carrying
the bulk — no single-expiry cliff risk. Largest single strike open: **Jun $11 call
10,553 OI** (even after −753), then Jan'27 $10 call 6,551, Jul $12 call 4,361.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__oi_biggest_increases` | symbol=CMPS, min_oi_change=300 | Jun $10P +2,191, Jun $11P +2,139, Jul $12C +1,962 |
| `mcp__uw-pp__oi_decrease_with_volume` | symbol=CMPS, min_volume=100 | Jun $11C −753 (roll near leg); rest immaterial |
| `mcp__uw-pp__oi_smart_positioning` | symbol=CMPS, min_oi_change=300 | Bullish: Jul $12C, Jun $11P-sold; hedge: Jun $10P |
| `mcp__uw-pp__oi_position_rolls` | symbol=CMPS, threshold=300, near_dte=30 | 1 call roll: near −682 / far +3,820 (up-and-out) |
| `mcp__uw-pp__oi_opex_concentration` | top_n=20, min_conc=40 | CMPS absent — OI spread, no cliff |
| `mcp__uw-pp__oi_pin_risk` | — | Skipped: 27 DTE to OPEX, would be empty (N/A) |

## Tool errors

_None._

## Verdict for downstream phases

- **Positioning bias:** **net BULLISH (constructive), with an explicit $10 tail hedge.**
  Long calls rolled up-and-out (Jun $11 → Jul $12), Jul $12 calls accumulated, Jun $11
  puts written (income / willing to own), Jun $10 puts bought for protection. This is the
  *reconciling* layer: phase-1's "call selling" was largely the **closing/near leg of a
  bullish roll** + intraday $13 churn, not distribution. Aligns with phase-2 DP buying.
- **Conviction:** **3.5/5.** Coherent, multi-leg, institutionally-shaped bullish
  structure confirmed across three OI tools — but sizes are modest (1,500–2,200 contracts
  per leg) and the genuine $10 put hedge signals the positioners are **not complacent**
  about downside. Not a max-conviction directional bet; a managed bullish-with-protection
  stance.
- **Three pin/cliff strikes for phase-9:**
  1. **$12 (Jul) — bullish magnet/target**: the accumulated long-call strike (+1,962 OI);
     where the roll positioned for upside.
  2. **$11 — soft support / "willing-to-own" line**: largest single OI (Jun $11 call
     10,553) + the written Jun $11 put — a level the structure is comfortable holding.
  3. **$10 — hedged downside / invalidation reference**: the bought Jun $10 put strike;
     below it the bull-put-spread max-loss and the DP support ($10.56–$10.86, phase-2)
     converge → a natural stop zone.
- **Open questions for phases 4–6:**
  - Does **dealer GEX/gamma** (phase-4) confirm a long-gamma pin in the $11–12 zone that
    would make this structure's range-thesis self-fulfilling?
  - Is the **$10 put hedge** sized to a known **catalyst** (clinical readout / data) before
    Jun 18? Next earnings is 2026-07-30 (phase-0.5) — so the Jun hedge points at a
    *non-earnings* event. Phase-6/7c must hunt the catalyst calendar.
  - Confirm the bull-put-spread vs two-player interpretation isn't masking a naked short
    put (different risk). Phase-4 structure + phase-7b balance-sheet (cash runway) inform this.
