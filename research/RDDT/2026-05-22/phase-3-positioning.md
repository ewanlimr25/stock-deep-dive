# Phase 3 — Open Interest & Positioning

**Ticker:** RDDT
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T00:00:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md

## Summary

Positioning reframes the divergence. Fresh OI building is **very light** — only
**two** contracts cleared the +500 threshold, **both calls, and `oi_smart_positioning`
infers BOTH as bearish (written/sold)**: the 155C 0DTE (+589, bid-heavy net_ask_bid
−48) and the **190C 6/18 (+514, bid-heavy net_ask_bid −169)**. The day's closing
activity is in **upside calls** — July 170C (−409) and July 200C (−90) reduced.
There are **no position rolls, no pin risk, and no OPEX concentration cliff** for
RDDT. Most importantly, the phase-1 "put buying" (130P 12/18 $1.13M) **did NOT build
≥500 OI** — consistent with it being the *paired two-way* print phase-1 saw (ask
$541k + bid $541k), i.e. a spread/roll, not clean directional put accumulation.
**Synthesis:** phase-1 (calls sold + puts bought) + phase-2 (block dip-buying at
141) + phase-3 (calls *written*, July upside *closed*, no put OI build) cohere into
one story — **institutional overwriting / upside-capping on an accumulated dip**,
not aggressive bearish positioning. The bearish options "footprint" is largely
**premium selling (call writing)**, which caps upside but is neutral-to-mildly
constructive on spot.

## Key signals

- Only 2 contracts with OI Δ ≥ 500, **both calls inferred BEARISH (written)**:
  155C 0DTE +589 and **190C 6/18 +514** (bid-heavy) [OI:biggest_increases]
  [OI:smart_positioning]
- Upside calls being **closed**: 170C 7/17 −409 (OI 1085→676), 200C 7/17 −90
  [OI:decrease_with_volume]
- **No directional put OI build** — the 130P 12/18 / 115P 11/20 phase-1 prints did
  not clear +500 OI → confirms two-way/spread, not put accumulation
  [OI:biggest_increases]
- **No pin risk** (RDDT absent from `oi_pin_risk` dte≤7) and **no OPEX cliff**
  (absent from `oi_opex_concentration` ≥40%) [OI:pin_risk] [OI:opex_concentration]
- Largest *standing* put OI: **120P 6/18 = 5,678 contracts** (downside ~15% OTM) —
  a pre-existing structural floor position [OI:decrease_with_volume]

## Detailed findings

### Largest OI increases — [OI:biggest_increases] + [OI:smart_positioning]

| Strike/Exp | Type | OI Δ | prev ask/bid vol | inferred | read |
|------------|------|------|------------------|----------|------|
| 155C 5/22 (0DTE) | call | +589 (995→1584) | 735 / 783 | **bearish** | 0DTE call written, expires today |
| 190C 6/18 (27DTE) | call | +514 (962→1476) | 282 / 451 | **bearish** | **call written** — caps upside at 190 over next month |

Only these two cleared +500. Both are call *writes* (bid-heavy, inferred bearish).
The 190C 6/18 is the meaningful one: someone is selling upside 34% OTM into June —
either overwriting a long stock position (covered call, ties to phase-2 buying) or
a standalone premium sale betting RDDT stays sub-190.

### Closing / roll activity — [OI:decrease_with_volume] + [OI:position_rolls]

- **170C 7/17 −409** (OI 1085→676, vol 464, avg $8.68) — closing/reducing July
  upside calls; the most material non-0DTE decrease.
- **200C 7/17 −90** — further July upside reduction.
- Remaining decreases are 0DTE (160C −212, 145P −208, 187.5C −207, 170C −141)
  expiring naturally today — not signal.
- **`oi_position_rolls`: 0 rolls detected** (single-day) — no clean near→far roll.

Theme: **upside call exposure is being trimmed/closed** (July 170/200C) and
**new upside written** (June 190C) — both point to capping/monetizing the upside
after the $132→$172 run, not to fresh downside conviction.

### Smart positioning (inferred direction)

Both qualifying OI builds inferred **bearish** via ask/bid skew — but the mechanism
is *call writing* (negative net_ask_bid on calls), which the tool labels "bearish."
Note the nuance: written calls are bearish-on-upside / theta-harvesting, distinct
from *bought puts* (directional downside). No bought-put OI build appeared.

### Pin risk — [OI:pin_risk]

**RDDT absent** from the dte≤7 pin-risk ranking (today 5/22 is a weekly expiry; the
board is HYG/SPY/TLT/QQQ/NVDA/AAPL etc.). RDDT's near-spot 0DTE OI mass is too small
to rank → **no meaningful pin for this expiry.** Next monthly OPEX = 2026-06-19.

### OPEX concentration — [OI:opex_concentration]

**RDDT absent** from the ≥40%-concentration list (all entries are tiny 100%-single-
expiry names). RDDT's total OI (447,744 from phase-0.5) is **spread across expiries
— no single OPEX cliff.** Largest standing single-strike OI seen incidentally:
120P 6/18 = 5,678 contracts (structural downside floor ~15% OTM).

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `oi_biggest_increases` | symbol=RDDT, ≥500, top20 | only 2: 155C 0DTE +589, 190C 6/18 +514 (both calls) |
| `oi_decrease_with_volume` | symbol=RDDT, min_vol100, top15 | 170C 7/17 −409, 200C 7/17 −90; rest 0DTE |
| `oi_smart_positioning` | symbol=RDDT, ≥500, top20 | both builds inferred bearish (call writes) |
| `oi_position_rolls` | symbol=RDDT, thr500, near≤30 | 0 rolls |
| `oi_pin_risk` | dte≤7, ≤5%, top25 | RDDT absent — no pin |
| `oi_opex_concentration` | ≥40%, top20 | RDDT absent — no cliff |

## Tool errors

None.

## Verdict for downstream

- **Positioning bias:** mildly bearish-on-upside via **call writing / upside
  trimming** — NOT directional downside loading. Reconciles phase-1 (bearish flow)
  with phase-2 (dip accumulation): the consistent reading is **overwriting an
  accumulated position**, capping upside, harvesting the rich long-dated vol.
- **Conviction:** 2/5 — fresh directional OI is genuinely *light* (only 2 contracts
  >500). The signal is more "stance" than "conviction bet."
- **Three pin/cliff strikes for phase-9:**
  1. **190** — June 190C now written (1,476 OI); a soft upside cap / where call
     writers sit.
  2. **120** — standing 120P 6/18 OI 5,678; structural downside floor ~15% below.
  3. No pin strike this expiry — phase-9 should NOT rely on a 5/22 or 5/29 pin.
- **Open questions:**
  - Is the 190C 6/18 write **covered** (against phase-2 accumulated stock) or naked
    bearish? If covered → the net stance is constructive-with-a-cap, not bearish.
    → phase-4 dealer positioning (DEX/GEX) + phase-8b debate.
  - With light OI and no puts being loaded, is the "bearish flow" really just
    profit-taking on the $172 high rather than a new short thesis? → phase-5 (does
    bearish flow on RDDT historically precede declines?), phase-8b.
