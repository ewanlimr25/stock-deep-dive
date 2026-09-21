# Phase 3 — Open Interest & Positioning

**Ticker:** RDDT
**As-of date:** 2026-05-20 (data anchor 2026-05-18)
**Generated:** 2026-05-19T00:30:00-04:00
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md

## Summary

OI changes confirm the front-end call buildup from phase-1 is leaving
durable open interest behind: the **5/22 160C added +1,292 OI** (OI now
3,592) and the **6/18 160C added +643 OI** (now 1,693). The 6/18 160C
print signature (bid-side dominance, net_ask_bid -787) reads as
**covered-call writing** — institutions that just accumulated stock in
phase-2 are harvesting premium against it at $160. The most aggressive %
buildup is **5/22 167.5C +246%** (OI 307 → 1,062) with net_ask_bid +384,
inferred bullish — speculative upside chase. **Only 4 RDDT contracts
breached the +500-OI threshold**, meaning most of phase-1's $25M
sweep premium was day-trading flow that did NOT leave durable positioning
behind — a critical de-rating nuance for the audit. No position rolls
detected. RDDT not in the market-wide pin-risk top-40 or OPEX
concentration top-100 — chain is healthy/distributed, no acute pin
mechanic. Stock_price snapshot on the OI feed: $159.04.

## Key signals

- **5/22 160C OI 2,300 → 3,592 (+56%)**, vol 1,510 — 85% of session
  volume created new positions; this is the front-week gamma magnet
  [OI:biggest_increases].
- **6/18 160C OI 1,050 → 1,693 (+61%)**, **net_ask_bid -787**, inferred
  direction = bearish (call write) — covered-call signature versus
  accumulated stock [OI:smart_positioning].
- **5/22 167.5C OI 307 → 1,062 (+246%)**, net_ask_bid +384, bullish:
  speculative upside chase one step above the 160 magnet
  [OI:smart_positioning].
- **6/18 95P OI +502, bid-side dominant** — put-writer commitment to
  absorb stock at $95 (-40% from spot); small ($5k premium) but
  symbolically bullish [OI:smart_positioning].
- Only **4 contracts** cleared the +500-OI threshold — phase-1's $25M
  bullish sweep premium was substantially intraday-only / non-positional;
  conviction adjustment recommended for phase-9 [OI:biggest_increases].

## Detailed findings

### Largest OI increases

| Expiry | DTE | OT | Strike | Last OI | Curr OI | Δ OI | %Δ | Volume | Stock |
|--------|-----|----|--------|---------|---------|------|-----|--------|-------|
| 2026-05-22 | 4  | call | 160   | 2,300 | 3,592 | +1,292 | +56%  | 1,510 | 159.04 |
| 2026-05-22 | 4  | call | 167.5 |   307 | 1,062 |   +755 | +246% | 1,076 | 159.04 |
| 2026-06-18 | 31 | call | 160   | 1,050 | 1,693 |   +643 | +61%  |   992 | 159.04 |
| 2026-06-18 | 31 | put  | 95    |   164 |   666 |   +502 | +306% |   544 | 159.04 |

Read: front-week call ladder is the only material OI buildup. The $160
strike is now the largest single-strike OI cluster in both the 5/22 and
6/18 expiries — **this is where dealer-hedging gamma will concentrate**
(phase-4 must confirm). The 95P buildup is tiny but is a "what-if-it-
crashes" tail-write that pays $5k premium for $9.5M of notional
commitment — institutional, not retail.

### Closing / roll activity

| Expiry | DTE | OT | Strike | Last OI | Curr OI | Δ OI | Vol | Read |
|--------|-----|----|--------|---------|---------|------|-----|------|
| 2026-07-17 | 60 | call | 175 | 1,163 | 966 | -197 | 254 | profit-take / roll-down |
| 2026-06-18 | 31 | call | 180 | 2,293 | 2,214 | -79  | 232 | minor close |
| 2026-06-18 | 31 | call | 170 | 1,876 | 1,829 | -47  | 190 | minor close |
| 2026-05-22 | 4  | call | 155 |   436 |   426 | -10  | 274 | churn (vol 274 vs Δ -10) |

Read: nothing material being closed. The 7/17 175C is the only notable
position trimming — read as someone taking small profits on an out-of-
the-money long call after the persistence-bullish run. Position-rolls
tool returned 0 hits at threshold 500, so there is no
near-DTE → far-DTE roll signature on a single-day basis.

### Smart positioning (inferred direction)

| Expiry | Strike | OT | Δ OI | net_ask_bid | Inferred |
|--------|--------|----|------|-------------|----------|
| 2026-05-22 | 160   | call | +1,292 | -32   | bearish (near-balanced) |
| 2026-05-22 | 167.5 | call |   +755 | +384  | **bullish** |
| 2026-06-18 | 160   | call |   +643 | -787  | **bearish (call writer)** |
| 2026-06-18 | 95    | put  |   +502 | -515  | **bullish (put writer)** |

Read: tool's "bearish" inference on the 5/22 160C is near-noise
(net_ask_bid -32 against 1,510 volume), but the **6/18 160C bid-side
dominance is clean** — this is a call-write, not a long-call open.
Combined with phase-2's institutional accumulation, the natural read is:
institutions are running a **covered-call strategy at 160 for June**,
extracting ~$10 of premium per contract while owning the stock around
$157-$160. This caps June upside FROM THE WRITER'S BOOK at ~$170
breakeven but does not cap broader spot upside — and on a 6/18 close
above $160, the calls will be assigned and the institutions will be
flat at higher prices with the premium booked.

### Pin risk

`oi_pin_risk dte_max=7 max_distance_pct=5 top_n=40` does not contain
RDDT. Market-wide top is HYG, SPY, TLT, QQQ, IWM, XLF, NVDA, SLV, EEM,
AAPL — all ETFs and mega-caps. RDDT's chain is too thin (in absolute
OI) to compete with those names on the gamma-weighted pin score, but
the **self-built $160 OI cluster** (5/22 OI 3,592 + 6/18 OI 1,693 +
prior phase-1 ladder at 5/29 160C) functions as a local pin/magnet for
the front weeklies. Phase-4 will confirm whether dealer GEX agrees.

### OPEX concentration

`oi_opex_concentration min_concentration_pct=40 top_n=100` does not
contain RDDT. RDDT's chain has OI distributed across multiple expiries
— healthy/liquid, not a single-expiry cliff trap.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__oi_biggest_increases` | symbol=RDDT, date=2026-05-18, top_n=20, min_oi_change=500 | 4 rows |
| `mcp__uw-pp__oi_decrease_with_volume` | symbol=RDDT, date=2026-05-18, top_n=15, min_volume=100 | 4 rows, all minor |
| `mcp__uw-pp__oi_smart_positioning` | symbol=RDDT, date=2026-05-18, top_n=20, min_oi_change=500 | 4 rows (same set as increases) |
| `mcp__uw-pp__oi_position_rolls` | symbol=RDDT, date=2026-05-18, threshold=500, near_dte_max=30 | 0 rolls |
| `mcp__uw-pp__oi_pin_risk` | date=2026-05-18, top_n=40, dte_max=7, max_distance_pct=5 | RDDT absent |
| `mcp__uw-pp__oi_opex_concentration` | date=2026-05-18, top_n=100, min_concentration_pct=40 | RDDT absent |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** mixed-bullish (call buildup is real but
  partly covered-call write; absolute scale modest)
- **Conviction:** 3 / 5 (real positioning but only 4 contracts cleared
  threshold; majority of phase-1 flow was non-positional)
- **Three pin/cliff strikes for phase-9:**
  1. **$160** — self-built front-end OI cluster: 5/22 OI 3,592 + 6/18
     OI 1,693. Local pin/magnet for the next two weeklies. Spot is
     literally sitting on this strike. Breakout above with momentum
     could force short-call hedging and a gamma squeeze; rejection at
     160 confirms pin behavior.
  2. **$167.50** — first upside resistance (5/22 OI 1,062, +246% in one
     session). If price clears 160, the next OI sponge.
  3. **$95** — symbolic floor where put-writer accepted the risk of
     long-stock assignment; far below spot but signals institutional
     view of "no scenario worse than -40%".
- **Open questions:**
  - Does phase-4 GEX confirm $160 as a dealer-positive-gamma magnet (so
    spot pins) or dealer-negative-gamma (so any break is amplified)?
  - Does phase-4 vanna/charm show dealer flows that would force buying
    on any spot strength through 160?
  - Is the apparent disconnect between $25M of bullish sweep premium
    (phase-1) and only 4 new OI lines a sign that most flow was hedge-
    fund day-trading or that opt-flow / OI snapshots are misaligned?
    (audit phase to reconcile.)
