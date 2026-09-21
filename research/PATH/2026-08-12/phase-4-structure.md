# Phase 4 — Dealer Structure & Gamma

**Ticker:** PATH
**As-of date:** 2026-08-12
**Generated:** 2026-08-13T02:05:00Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-3-positioning.md

## Summary

Dealers are **net long gamma** (`regime=POSITIVE`) both broadly (≤45 DTE) and
at the nearest expiry — the tool's own label, quoted verbatim both times —
which mechanically favors mean-reversion and suppressed realized vol, not a
directional edge. `dex` confirms the public is net call-long (matching phase-3's
call-heavy OI book), so **dealers must buy the underlying to hedge their short
calls** — a structural, price-agnostic tailwind that stays live as long as the
call skew persists. Term skew is `COMPLACENT` (calls slightly richer than
puts, no tail-hedge fear priced in). The broad `iv-term-structure` calls the
curve `BACKWARDATION`, but that label is driven by a heavily-contaminated
2-DTE read (`avg_iv=206.9%`, the same deep-ITM parity artifacts phase-1 flagged
in `iv-outliers`) — the cleaner near-tradable window (9 DTE vs 30 DTE) is
`CONTANGO` per `front-end-iv-ratio`, the more normal shape. Max pain sits
**below spot at every near-term expiry** (−1.5% to −27.8%), a mechanical OPEX
headwind if OI stays static, most pronounced at the largest near-dated expiry
(2026-08-21, 98,917 contracts, max pain $11). Net: **neutral-to-mildly-bullish
dealer mechanics** (long-gamma range compression + call-hedge buying pressure)
partially offset by a soft downward OPEX pull. Low-moderate conviction.

## Key signals

- Dealer regime **POSITIVE** (long gamma) both broad (≤45 DTE) and nearest-
  expiry — mean-reversion/vol-suppression bias [STRUCT:gex, STRUCT:today_gamma_flip]
- `net_dex=+$143.5M`: "Public is net call-long → dealers net short calls →
  dealer hedge is to BUY underlying" [STRUCT:dex]
- Term skew `COMPLACENT` (`call_25d_iv=0.812` vs `put_25d_iv=0.760`,
  `skew=-0.052`) — no crash-fear premium [STRUCT:term_skew]
- `iv-term-structure=BACKWARDATION` but driven by a contaminated 2-DTE read
  (206.9% avg IV); the cleaner `front-end-iv-ratio` (9 vs 30 DTE) reads
  `CONTANGO` (ratio 0.802) [STRUCT:iv_term_structure, STRUCT:front_end_iv_ratio]
- Max pain below spot at all 5 near-term expiries, most extreme at the
  largest-OI 2026-08-21 expiry: **$11 (−27.77%)** [STRUCT:max_pain]

## Detailed findings

### GEX (total, per-strike top, zero gamma level)

`uw options-structure gex --dte-max 45`: `regime=POSITIVE`,
`regime_description="Dealers net long gamma — expect mean-reversion and
reduced volatility"`, `total_gex=$26,010,804`, `zero_gamma_level=$8.64`
(spot $15.23). Per-strike GEX is overwhelmingly positive; the top-10 strikes
by |net_gex| are all positive except one negative pocket:

| Strike | Net GEX |
|---|---|
| $15 (ATM) | +$9,899,956 |
| $18 | +$3,087,283 |
| $16 | +$2,955,359 |
| $14 | +$2,361,188 |
| $16.50 | +$1,973,524 |
| $15.50 | +$1,748,256 |
| $17 | +$1,321,157 |
| $12 | +$948,847 |
| **$9** | **−$112,361** (the one significant negative pocket) |

The lone meaningful negative-gamma strike ($9) is the same level phase-3
flagged as the only real put wall (`put_wall_support`, −40.91% from spot) —
the ZGL of $8.64 sits just below it, i.e., spot would need to fall ~43% before
the dealer book flips short-gamma. **Common-pitfall caveat applies**: on a
name this size, treat the ZGL as directional information (very far below
spot, book solidly positive-gamma) rather than a precise tradeable line.

### DEX (net dealer delta / hedging direction)

`uw options-structure dex --dte-max 45`: `call_dex=$152,684,358`,
`put_dex=−$9,183,240`, `net_dex=+$143,501,118`. Interpretation (quoted
verbatim): *"Public is net call-long → dealers net short calls → dealer hedge
is to BUY underlying."* This is a structural, mechanical bullish flow — not
contingent on today's tape — that persists as long as the call-heavy OI book
(phase-3) stays in place.

### Vanna + charm

`uw options-structure vanna-charm --dte-max 45`: `net_vanna=−6,786`
(`call_vanna=−7,353`, `put_vanna=+567`), `net_charm=+251,613`.
Interpretation (quoted verbatim): *"Public net vanna negative (call-heavy
book). Falling IV → call delta drops → dealers (short calls) cut long-
underlying hedge → SELLING pressure. Rising IV reverses."* This is the mirror
image of the DEX read: the same short-call dealer book that creates buying
pressure today is IV-sensitive — a vol crush would create incremental
mechanical selling, a vol pop would reinforce the buying pressure. No squeeze
setup (`net_vanna` is negative, not the positive-vanna + negative-delta
combination the interpretation heuristics call a squeeze).

### IV term structure

`uw options-structure iv-term-structure`: `structure=BACKWARDATION`,
`kink_expiry=null`. Per-expiry `avg_iv` (front six):

| Expiry | DTE | avg IV |
|---|---|---|
| 2026-08-14 | 2 | **206.9%** |
| 2026-08-21 | 9 | 80.2% |
| 2026-08-28 | 16 | 63.8% |
| 2026-09-04 | 23 | **146.4%** |
| 2026-09-11 | 30 | 100.0% |
| 2026-09-18 | 37 | 78.2% |

The 2-DTE (206.9%) and 23-DTE (146.4%) readings are driven by the same
deep-ITM, thin-quote contracts phase-1's `iv-outliers` flagged as parity
artifacts (2026-08-14 $6.50/$7 calls; 2026-09-04 $5.50 call) — a handful of
illiquid strikes skewing the per-expiry average, not genuine event-driven
richness. **Excluding those two contaminated points, the curve is closer to
flat-to-mild-contango** (63.8% → 78.2% → 100.0% across 16/37/30 DTE), which
`front-end-iv-ratio` corroborates directly.

### Term skew

`uw options-structure term-skew --dte-target 30`: `call_25d_iv=0.8121`,
`put_25d_iv=0.7600`, `skew=-0.0521`, `skew_ratio=0.936`,
`interpretation=COMPLACENT`. Calls are modestly richer than puts at 30 DTE —
consistent with the call-heavy OI book and the absence of tail-hedge demand.

### Front-end IV ratio (event stress)

`uw options-structure front-end-iv-ratio --near-dte 7 --far-dte 30`:
`near_iv=0.8024` (9 DTE actual), `far_iv=1.00` (30 DTE), `ratio=0.802`,
`regime=CONTANGO`. **This is the cleaner, uncontaminated read** — no acute
event-stress signal in the near-dated, liquid part of the curve.

### Today's gamma flip (nearest-expiry / EOD snapshot)

`uw options-structure today-gamma-flip` (nearest expiry 2026-08-14, EOD
snapshot — this run is as-of a completed session, not a live intraday read):
`regime=POSITIVE`, `today_total_gex=$5,608,837`, `today_zero_gamma=$13.80`,
`atm_flip_strike=$6.50`, spot $15.24.

| Strike | GEX | Role |
|---|---|---|
| $15 | +$1,576,674 | support_wall |
| $16.50 | +$1,556,223 | support_wall |
| $15.50 | +$1,406,174 | support_wall |
| $16 | +$1,220,994 | support_wall |
| $14 | **−$472,454** | resistance_wall |

The nearest-expiry ZGL ($13.80, −9.5% from spot) is far more relevant than the
broad 45-DTE ZGL ($8.64) for near-term price behavior — confirms the positive-
gamma regime holds down to a meaningful, in-range level. The $14 negative-gamma
pocket (labeled `resistance_wall` by the tool despite sitting below spot — a
level that, if broken, dealers would need to sell into rather than defend) is
the one soft spot in an otherwise supportive nearest-expiry gamma map.

### Max pain (opex-gravity magnet)

`uw options-structure max-pain --dte-max 30`:

| Expiry | DTE | Max pain | Distance from spot | Total OI | P/C OI ratio |
|---|---|---|---|---|---|
| 2026-08-14 | 2 | $14 | −8.08% | 28,136 | 0.443 |
| **2026-08-21** | 9 | **$11** | **−27.77%** | **98,917** | 0.253 |
| 2026-08-28 | 16 | $12 | −21.21% | 12,040 | 0.129 |
| 2026-09-04 | 23 | $14 | −8.08% | 8,393 | 0.316 |
| 2026-09-11 | 30 | $15 | −1.51% | 2,381 | 0.038 |

Every near-term max-pain strike sits below spot — mechanical consequence of
the heavy call skew (phase-3): the more call-heavy an expiry's OI, the further
below spot its pain point pulls (compare 2026-09-11's P/C=0.038 → pain only
−1.51% since total OI is tiny, vs. 2026-08-21's P/C=0.253 on 98,917 contracts
→ pain −27.77%, the deepest pull and the largest near-dated book by far).
**Caveat (the tool's own):** "Single-day OI snapshot... assumes settlement
with current OI unchanged to expiry" — this migrates as OI builds/closes
between now and each expiry; the 2026-08-21 pull is the one worth tracking
since it sits on this week's OPEX and the largest OI base.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw options-structure gex --symbol PATH --dte-max 45 --date 2026-08-12 --json` | `regime=POSITIVE, zero_gamma_level=8.64, total_gex=26010804` ← top-level keys | per-strike table |
| `uw options-structure dex --symbol PATH --dte-max 45 --date 2026-08-12 --json` | `net_dex=143501118` ← `.net_dex` | 1 |
| `uw options-structure vanna-charm --symbol PATH --dte-max 45 --date 2026-08-12 --json` | `net_vanna=-6786, net_charm=251613` ← top-level | 1 |
| `uw options-structure iv-term-structure --symbol PATH --date 2026-08-12 --json` | `structure=BACKWARDATION` ← `.structure`; per-expiry `.term_structure[]` | 15 |
| `uw options-structure term-skew --symbol PATH --dte-target 30 --date 2026-08-12 --json` | `interpretation=COMPLACENT, skew=-0.0521` ← top-level | 1 |
| `uw options-structure front-end-iv-ratio --symbol PATH --near-dte 7 --far-dte 30 --date 2026-08-12 --json` | `regime=CONTANGO, ratio=0.802` ← top-level | 1 |
| `uw options-structure today-gamma-flip --symbol PATH --date 2026-08-12 --json` | `regime=POSITIVE, today_zero_gamma=13.8` ← top-level; `.key_walls[]` | 5 |
| `uw options-structure max-pain --symbol PATH --dte-max 30 --date 2026-08-12 --json` | 5 rows ← `.results[]` | 5 |

## Tool errors

<none>

## DATA NOTE / CORRECTION

<none — first read stood. The BACKWARDATION vs CONTANGO tension between
`iv-term-structure` and `front-end-iv-ratio` is a genuine data-quality nuance
(contaminated front-dated contracts), not a tool error — both fields are
quoted verbatim; the write-up above explains the discrepancy rather than
silently picking one.>

## Verdict for downstream phases

- **Dealer regime:** Long gamma (POSITIVE), both broad and nearest-expiry —
  mean-reversion / vol-suppression bias. Combined with `dex`, the mechanical
  flow is mildly bullish (dealers must buy stock to hedge short calls); term
  skew shows no fear premium.
- **Conviction:** 2/5 — the long-gamma regime itself is directionally neutral
  (it dampens moves either way), and the one directional mechanical signal
  (DEX buy-hedge pressure) is offset by max pain's downward OPEX pull at the
  largest near-dated expiry.
- **Three structural levels for phase-9 (+ opex magnet):**
  1. **Nearest-expiry ZGL: $13.80** (−9.5%) — the meaningful gamma-flip line;
     the broad 45-DTE ZGL ($8.64) is too far out-of-range to be tradeable.
  2. **Largest GEX strike: $15.00** (ATM, +$9.9M net GEX) — the dominant
     dealer-hedging pivot.
  3. **Vanna pivot:** qualitative, not a strike — negative net vanna means a
     **vol crush would add selling pressure**, a **vol pop would reinforce
     buying pressure**; watch IV direction, not just level.
  4. **Near-expiry max-pain magnet: $11.00** (2026-08-21, −27.77%, 98,917
     contracts — the largest near-dated OI book) — the OPEX gravity well to
     watch this week; $14.00 (2-DTE, −8.08%) is the more immediate one.
- **Open questions:** Does phase-5's historical/technical read show PATH
  respecting the $13.80–$14.00 zone as support on past pullbacks (would
  corroborate the gamma-wall + max-pain confluence there)? Will the
  2026-08-21 OI book (P/C=0.253, currently pulling pain to $11) actually hold
  its call skew into expiry, or is that likely to unwind the way today's
  call OI already started unwinding (phase-3)?
