# Phase 4 — Dealer Structure & Gamma

**Ticker:** BL
**As-of date:** 2026-05-19
**Generated:** 2026-05-19T00:00:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md

## Summary

Dealer structure is **almost entirely concentrated at one strike**:
**$27.5 carries `net_gex=193,037,548.78` out of total `194,349,985` (≈99.3%)**
[STRUCT:options_structure_gex]. Net dealer delta (DEX) is unambiguously
positioned to **BUY underlying as price rises**: `net_dex=6,337,156,590` with
`call_dex=6,337,500,481` and `put_dex=-343,891` —
`"Public is net call-long → dealers net short calls → dealer hedge is to BUY
underlying"` [STRUCT:options_structure_dex]. Term structure is **CONTANGO**
(74.2% Jun → 78.7% Dec) with **no front-end event spike**
[STRUCT:options_structure_iv_term_structure,
options_structure_front_end_iv_ratio]; 30-DTE skew is **NORMAL**
(`skew=0.0589`, `skew_ratio=1.078`) — no tail-hedging panic
[STRUCT:options_structure_term_skew]. Vanna is **negative**
(`net_vanna=-750878`) because the book is call-heavy: **falling IV =
de-hedge selling pressure; rising IV = re-hedge buying pressure**
[STRUCT:options_structure_vanna_charm]. Today's intraday gamma map shows
`atm_flip_strike=27.5`, `today_zero_gamma=25.7`, spot **above** flip → a
support-wall stack at $30 ($57.9k), $32.5 ($986.3k), and $37.5 ($40.6k);
$25 is the only resistance wall and it's tiny (-$675)
[STRUCT:options_structure_today_gamma_flip].

**Known conflict** (flagged for phase-10 audit): the GEX tool labels the
regime "POSITIVE / Dealers net long gamma — expect mean-reversion" while the
DEX tool says dealers are net short calls and must buy the rally. These two
interpretations are operationally contradictory. Resolution: the DEX
read-out is the more direct dealer-position signal (it's derived from raw
delta × OI), while the GEX label uses a sign convention that does not
specify whether `net_gex` is reported from the public side or the dealer
side. Given (a) phase-3 OI confirms the public newly bought 13,016 Dec
$27.5C contracts ask-side, and (b) net_dex aligns with that direction, the
**dealer-short-gamma / dealer-must-buy** read is the operative one for trade
construction. The GEX label is recorded as-given and flagged.

**Net read: short-gamma squeeze setup at $27.5, with $32.5 as the next
gamma-magnet ceiling.** Conviction 4/5 (capped because of the
above-mentioned label conflict).

## Key signals

- **GEX concentration:** strike $27.5 net_gex = `193,037,548.78` out of
  total `194,349,985` ≈ **99.3% of total GEX in one strike**
  [STRUCT:options_structure_gex]. Implication: any move that pushes spot
  toward or through $27.5 forces a non-linear dealer re-hedge.
- **Dealer delta direction:** `net_dex=6,337,156,590` (positive), dealer
  hedge **= BUY underlying** [STRUCT:options_structure_dex].
- **Term structure CONTANGO**: June 74.2% < July 76.9% < Nov 77.3% < Dec
  78.7% — **smooth upward slope, no front-end backwardation kink** ⇒ no
  imminent (≤30 DTE) earnings or binary event priced
  [STRUCT:options_structure_iv_term_structure].
- **30-DTE skew NORMAL:** put 25Δ IV 81.85% vs call 25Δ IV 75.96%; `skew=0.059`,
  `skew_ratio=1.078` [STRUCT:options_structure_term_skew]. Slightly put-rich
  but unremarkable for a small-cap — no tail panic.
- **Today's gamma walls:** support stack $30 / $32.5 / $37.5 (positive GEX
  $57.9k / $986.3k / $40.6k); resistance wall at $25 (-$675)
  [STRUCT:options_structure_today_gamma_flip]. **$32.5 is the dominant
  intraday gravity strike — phase 9 should view this as the first target.**

## Detailed findings

### GEX (per strike, ZGL, total) [STRUCT:options_structure_gex]

| Strike | Net GEX | Note |
|--------|---------|------|
| 22.5 | −25,103.55 | tiny, below ZGL |
| 25.0 | −675.18 | ZGL boundary |
| **27.5** | **193,037,548.78** | **dominant concentration (LEAP-flow driven)** |
| 30.0 | 57,936.35 | small wall |
| 32.5 | 987,461.67 | **second-largest** |
| 37.5 | 292,817.06 | upside |

- `total_gex`: **$194,349,985**
- `zero_gamma_level`: **$25.00**
- `underlying_price`: **$29.85**
- `regime` (as labeled by tool): "POSITIVE", `regime_description`:
  `"Dealers net long gamma — expect mean-reversion and reduced volatility"`
- `note` (from tool itself): `"GEX most meaningful for index products
  (SPY, QQQ) and large-cap single stocks with deep OI."` — single-name
  caveat acknowledged.

**Critical observation**: 99.3% of total GEX is at the single strike
($27.5) where phase-3 documented +13,016 OI today. The GEX number for that
strike effectively *is* the new public position. **Whether the regime label
("dealers net long") is meaningful depends on the tool's sign convention,
which is ambiguous against the DEX read-out below.**

### DEX (net dealer delta) [STRUCT:options_structure_dex]

- `call_dex` = **6,337,500,481**
- `put_dex` = −343,891 (negligible)
- `net_dex` = **6,337,156,590**
- `spot` = **$29.85**
- Tool interpretation (verbatim): *"Public is net call-long → dealers net
  short calls → dealer hedge is to BUY underlying."*

**Mechanics:** delta-weighted public exposure is ~$6.34B notional long-side
on the calls. Translating: with spot $29.85 and 100x multiplier, the
call_dex implies a delta×OI sum of about `6.34B / (29.85×100) ≈ 2.12M`
share-equivalent of *positive* delta held by the public. Dealers carry the
mirror **negative-2.12M share-equivalent delta**, which they hedge with
underlying longs. As spot rises:
- Delta of the Dec $27.5C rises from 0.67 (current) to ~0.85 at spot $32.5.
- That alone forces dealer share-buying of ~`(0.85−0.67) × 16,178 × 100 ≈
  291,000 shares` from spot $29.85 → $32.5. **For BL with ~500k share ADV,
  this is ~half a day's volume of pure mechanical buying.**

### Vanna + charm [STRUCT:options_structure_vanna_charm]

| Quantity | Value |
|----------|-------|
| `call_vanna` | −750,909 |
| `put_vanna` | +31 |
| `net_vanna` | **−750,878** |
| `net_charm` | +420,927 |

Vanna interpretation (verbatim from tool): *"Public net vanna negative
(call-heavy book). Falling IV → call delta drops → dealers (short calls) cut
long-underlying hedge → SELLING pressure. Rising IV reverses."*

**Implication for the bull thesis:** today's flow paid up to ~80% IV. If
realized vol prints in line and the dealer book stays short-vega, **IV
should not collapse easily** (sellers don't want to feed cheap calls into
this demand). Positive net_charm (+$420k) is the time-decay tailwind for
dealers — over the next week or two, charm flow gently *supports* the
underlying (long-dated calls' delta drifts higher with time → dealers
re-buy stock to stay hedged). **Vanna + charm net = mildly bullish drift
unless IV craters.**

### IV term structure [STRUCT:options_structure_iv_term_structure]

| Expiry | Avg IV | Contracts |
|--------|--------|-----------|
| 2026-06-18 (30 DTE) | 0.7417 (**74.2%**) | 63 |
| 2026-07-17 (60 DTE) | 0.7690 (76.9%) | 2 |
| 2026-11-20 (185 DTE) | 0.7732 (77.3%) | 15 |
| 2026-12-18 (**213 DTE**) | **0.7868 (78.7%)** | 210 |

- `structure`: **CONTANGO**
- `kink_expiry`: **null** (no event spike)

**Read:** A clean upward slope from 74% to 79% over June → Dec. No isolated
"earnings hump" at any expiry. This is consistent with phase-5's likely
finding that BL has an event (or earnings) somewhere in the Aug-Dec window
that the buyer is positioning for — not a binary front-month catalyst. Note
the Dec expiry has **210 contracts** vs June's 63 and Nov's 15: the chain is
already concentrated in Dec, supporting phase-3's "this is *the* expiry"
thesis.

### Term skew [STRUCT:options_structure_term_skew]

- `dte_target` = 30, `dte_actual` = 30
- `put_25d_iv` = 0.8185 (81.85%)
- `call_25d_iv` = 0.7596 (75.96%)
- `skew` = 0.0589
- `skew_ratio` = **1.078**
- Interpretation (tool): **NORMAL**

**Read:** mild put richness (5.9 vol-points), typical for a small-cap
software name. No `TAIL_HEDGING` regime (which would require ratio ≥ ~1.15).
**The bull thesis is not contradicted by skew** — the market is not pricing
in unusual downside.

### Front-end IV ratio
[STRUCT:options_structure_front_end_iv_ratio]

- `near_dte` (requested 7, `near_dte_actual` 30) — note: BL has no
  contracts in the ≤7-day window, so the tool snapped to the nearest expiry
  (June 18, 30 DTE).
- `near_iv` = 0.7417, `far_iv` = 0.7417, `ratio` = **1.00**
- Regime: **FLAT**

**Read:** With near_dte snapped to 30 (no true near-term contracts), the
"flat" regime is mechanically true but not informative. The deeper signal
from term-structure above already covers this — **no event stress in the
front month**.

### Today's gamma flip [STRUCT:options_structure_today_gamma_flip]

| Field | Value |
|-------|-------|
| `today_expiry` | 2026-06-18 |
| `atm_flip_strike` | **27.5** |
| `today_zero_gamma` | **25.70** |
| `spot` | 30.01 |
| `today_total_gex` | $1,086,564 |
| `regime` | POSITIVE |

**Key walls (intraday) — verbatim:**

| Strike | Net GEX | Role |
|--------|---------|------|
| 32.5 | **986,306** | support_wall |
| 30.0 | 57,936 | support_wall |
| 37.5 | 40,592 | support_wall |
| 27.5 | 2,405 | support_wall |
| 25.0 | −675 | resistance_wall |

**Read:** Spot ($30.01) sits **between two support walls** ($30 and $32.5).
$32.5 is the dominant gamma magnet — if BL trades up, this is the first
mechanically-hard ceiling/target. $25 is the only resistance wall and it's
tiny — the path down is **unsupported** below $25.70 (today's flip). This
matches phase-2's institutional floor at $24.90–25.81: that floor is *price*
support; below it, gamma offers no second line of defense.

## Cross-phase confluence

| Phase 4 datapoint | Echo from prior phases |
|-------------------|------------------------|
| $27.5 = 99.3% of total GEX | Phase 1: $4.14M ask-side sweeps on Dec $27.5C; Phase 3: +13,016 OI at Dec $27.5C |
| $32.5 dominant intraday support wall ($986k) | Phase 3: OTM ladder seeded at $30/$32.5/$35/$37.5; Phase 2: institutional accumulation continued up to $30.50 |
| Dealer hedge = BUY underlying | Phase 2: 89-100% buy_ratio in DP today; the institution may itself be *one of the dealer hedgers* OR the trigger that makes the broader dealer cohort hedge |
| Today_zero_gamma = $25.70 | Phase 2: institutional floor cluster at $24.90-25.81 — gamma support and institutional support **stack** here |
| NORMAL skew + CONTANGO + no front-end stress | No imminent (≤30d) binary event — supports buyer's choice of 213-DTE expiry over weekly |

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `options_structure_gex` | `{symbol:BL, dte-max:365, include-zero-gamma:true, date:2026-05-19}` | Total GEX $194M, ZGL $25, $27.5 = 99.3% concentration |
| `options_structure_dex` | `{symbol:BL, dte-max:365, date:2026-05-19}` | net_dex +$6.34B → dealers BUY underlying as spot rises |
| `options_structure_vanna_charm` | `{symbol:BL, dte-max:365, date:2026-05-19}` | net_vanna −$750k, net_charm +$421k |
| `options_structure_iv_term_structure` | `{symbol:BL, date:2026-05-19}` | CONTANGO, no kink |
| `options_structure_term_skew` | `{symbol:BL, dte-target:30, date:2026-05-19}` | NORMAL, ratio 1.078 |
| `options_structure_front_end_iv_ratio` | `{symbol:BL, near-dte:7, far-dte:30, date:2026-05-19}` | FLAT (snapped to 30 DTE — no true near-term) |
| `options_structure_today_gamma_flip` | `{symbol:BL, date:2026-05-19}` | atm_flip $27.5, today_zero_gamma $25.70, $32.5 dominant support wall |

## Tool errors

None.

## Verdict for downstream phases

- **Dealer regime:** Operationally **SHORT GAMMA at $27.5** with
  dealer-hedge=BUY-underlying. (Tool's "POSITIVE" label conflicts with this
  — flagged.)
- **Conviction:** **4 / 5** (downrated from 5 only due to the GEX-label
  vs DEX-direction conflict, which a careful PM must resolve. Phase 10 must
  audit.)
- **Three structural levels for phase 9 (entry/stop/target reference):**
  1. **$25.70** — today's intraday zero-gamma flip. **Hard floor**: below
     this, dealers move from "buy support" to "neutral or sell." Combined
     with the $24.90–25.81 institutional cluster from phase-2, this is the
     phase-9 **stop band**. A close < $24.85 invalidates the thesis.
  2. **$30.00** — current spot zone, primary support wall.
  3. **$32.50** — **dominant gamma magnet** ($986k support wall, second-
     largest GEX). Phase 9 **first target**. A breakout above $32.50 forces
     mechanical dealer buying into the $37.5 wall and the OTM seeded
     strikes from phase-3.
- **Three things later phases should remember:**
  1. **Dealer hedge is one-directional bullish** while spot ≥ $25.70 and
     the $27.5 OI stays intact. Phase-5 must confirm whether IV (78-79%) is
     a multi-month/yearly high — if so, the buyer is paying for the squeeze,
     not getting it cheap.
  2. **No event stress in the near term** (NORMAL skew, CONTANGO, FLAT
     front-end). Phase-5 / phase-7 should find the catalyst in the **back-
     half of the year** (Aug-Dec), since the buyer chose Dec expiry and the
     term-structure slope is gentle.
  3. **GEX label conflict** between "POSITIVE / mean-reversion" and DEX
     "dealer-short / buy-rallies" must be flagged in **phase-10 audit**.
- **Open questions:**
  - **What is the catalyst** that explains why the buyer chose Dec 18, 2026?
    BL's Q3 earnings (typically Nov), an investor day, sector M&A, or a
    contract win? → phase 5 (`historical_*`) + phase 6 + phase 7
    (`insights_earnings_play`).
  - Where does **IV percentile** sit historically — is 79% a 95th-percentile
    extreme or a 50th-percentile normal? → phase 5 (`historical_iv_percentile_zscore`).
  - Has the OI trend been **monotonically building** for the last 2-3 weeks
    (smart-money accumulation phase) or is today a one-day spike? → phase 5
    (`historical_oi_trend`).
