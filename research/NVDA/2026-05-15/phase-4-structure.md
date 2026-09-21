# Phase 4 — Dealer Structure & Gamma

**Ticker:** NVDA
**As-of date:** 2026-05-15
**Spot reference:** $227.54 (per `options_structure_gex`)
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md,
phase-3-positioning.md
**Generated:** 2026-05-17T17:11Z

## Summary

Dealer regime is firmly **POSITIVE GAMMA** with the Zero Gamma Level at
**$72.29** (45-DTE basis) and the today-only ZGL at **$218.30**. Spot at
$227.54 sits ~$9 / +4.2% above today's ZGL — that's the **mean-reversion
shelf** below which short-gamma chaos starts. **The single largest gamma
wall is $230** with **$7.69 trillion in GEX** `[STRUCT:today_gamma_flip]` —
this is the magnetic strike for the 0DTE chain and it cleanly explains
phase-2's intra-day mean-reversion around the same level. DEX is heavily
positive ($25.8T), meaning dealers are net **short calls** and hedge by
BUYING underlying on rallies — a structural intraday bid. The biggest
warning: **front-end IV ratio is 1.41 (BACKWARDATION)**, with 05-22 IV at
**74.0% vs 32-day IV at 52.5%** — this is event-stress in the 5–7 day
window, almost certainly an **NVDA earnings print on the 05-22 chain**.
Phase 6 must confirm the earnings date. Term skew is COMPLACENT (calls
slightly richer than puts), which is unusual and tells us option buyers
are paying up for upside relative to downside.

## Key signals

- **GEX regime: POSITIVE**, total GEX $1.10T (45-DTE), ZGL $72.29
  `[STRUCT:gex]`. Spot $155 above ZGL — extreme positive gamma; expect
  suppressed realized vol and intraday mean reversion.
- **DEX +$25.85T**, public net-call-long, dealer hedge **BUYS underlying**
  `[STRUCT:dex]`. Structural bid through the next 45 DTE.
- **Today's largest gamma wall: $230 strike, $7.69T GEX**
  `[STRUCT:today_gamma_flip]`. Spot (228.93 late-day per phase-1) is
  magnetically attracted to $230.
- **Front-end IV ratio: 1.41 — BACKWARDATION** (near IV 74.0% vs far IV
  52.5%) `[STRUCT:front_end_iv_ratio]`. Event stress in the 5–7d window.
- **Term skew at 30D: COMPLACENT** (call_25d 49.2%, put_25d 47.3%, skew
  -0.02) `[STRUCT:term_skew]`. Calls richer than puts — upside-chasing
  premium, NOT tail-hedging panic.

## Detailed findings

### GEX (45-DTE basis)

| Field | Value |
|-------|-------|
| Regime | **POSITIVE** (dealers long gamma) |
| Total GEX | $1.10T |
| Zero Gamma Level | $72.29 |
| Underlying price | $227.54 |
| Spot above ZGL by | +$155.25 (+214%) |

Top positive gamma strikes (call walls dealers must hedge against, i.e.,
where dealers SELL as price approaches):

| Strike | Net GEX | Role |
|--------|---------|------|
| $90  | $527B | call wall (deep ITM dealer short calls, irrelevant to near-term spot) |
| $80  | $393B | same |
| $96  | $94B  | same |
| $60  | $30B  | same |
| $50  | $23.5B | same |

Top negative gamma strikes (put walls dealers must hedge against, BUY as
price approaches):

| Strike | Net GEX | Role |
|--------|---------|------|
| $115 | -$16.0T | put wall |
| $120 | -$7.4T  | put wall |
| $100 | -$1.06T | put wall |
| $110 | -$744B  | put wall |
| $95  | -$339B  | put wall |

Note: all the near-spot GEX action is on the 0DTE chain — see "Today's
gamma flip" below for the strikes that actually matter for the next 24h.

### DEX (net dealer delta exposure, 45-DTE)

| Field | Value |
|-------|-------|
| Net DEX | $25.85T (positive — public long calls) |
| Call DEX | $28.80T |
| Put DEX | -$2.95T |
| Spot | $227.51 |

Reading: public is overwhelmingly long calls; dealers are short those
calls; dealer hedge is to BUY underlying. This produces a **structural
intraday bid**. Combined with the positive-gamma mean-reversion, NVDA
should be very hard to break to the downside unless ZGL is taken out.

### Vanna + Charm (45-DTE, excludes 0DTE)

| Field | Value |
|-------|-------|
| Net vanna | -141.9M (call-heavy book) |
| Net charm | +9.50B |
| Call vanna | -155.0M |
| Put vanna | +13.1M |

**Vanna interpretation:** with negative net vanna, *falling IV* would
cause dealers (short calls) to cut their long-underlying hedge → SELLING
pressure. *Rising IV* reverses → BUYING pressure. With phase-4 backwardation
showing event stress, post-earnings IV crush on 05-22+ could create a
vanna-driven selling pulse if dealers under-hedge into the event.

**Charm interpretation:** positive net charm = passage of time supports
the existing dealer long-hedge. Over the next few sessions (before any
event), decay is on the bullish/dealer-bid side.

### IV term structure (CONTANGO overall, but front-end spike)

| Expiry | DTE | Avg IV | Read |
|--------|-----|--------|------|
| 2026-05-15 | 0  | **6.3%** | Collapsed (OPEX day) |
| 2026-05-18 | 3  | 39.9% | Normalizing |
| **2026-05-22** | **7** | **74.0%** | **EVENT IV — almost certainly earnings on this chain** |
| 2026-05-26 | 11 | 61.1% | Post-event |
| 2026-05-29 | 14 | 61.0% | Post-event |
| 2026-06-05 | 21 | 55.9% | |
| 2026-06-12 | 28 | 52.4% | |
| 2026-06-18 | 34 | 52.5% | Monthly OPEX |
| 2026-07-17 | 63 | 47.2% | |
| 2026-09-18 | 126 | 48.2% | |
| 2026-12-18 | 217 | 55.6% | (Q4 earnings re-acceleration) |
| 2027-01-15 | 245 | 48.7% | |
| 2028-12-15 | 945 | 50.1% | LEAP baseline |

Overall classification: CONTANGO (back > near in the smoothed average),
but the **05-22 spike is a binary event marker** that phase-6 needs to
confirm — NVDA earnings calendar should put a release on or just before
2026-05-22. Front-end IV ratio confirms with a hard BACKWARDATION 1.41.

### Term skew (30D)

| Field | Value |
|-------|-------|
| 25Δ Call IV | 49.24% |
| 25Δ Put IV | 47.26% |
| Skew | -0.0199 (calls > puts) |
| Regime | **COMPLACENT** |

Reading: in normal markets put skew is positive (puts richer than calls
because tail hedging demand outweighs upside-chasing). Here the call IV is
RICHER — option buyers are paying up for upside (consistent with phase-1
LEAP buys and phase-3 250C 05-22 buyer demand) and *not* paying up for
downside protection. This is a complacent / one-way-bullish positioning
posture that is itself a small contrarian flag — when everyone is positioned
upside, an unexpected catalyst can produce outsized downside.

### Today's gamma flip (0DTE)

| Field | Value |
|-------|-------|
| Spot | $227.56 |
| Today ZGL | **$218.30** |
| ATM flip strike | $155 (far below spot — irrelevant) |
| Today total GEX | $10.52T |
| Regime | POSITIVE |

Today's support walls (in order):

| Strike | GEX | Role |
|--------|-----|------|
| **$230** | **$7.69T** | **Primary gamma wall — strongest magnet** |
| $227.5 | $1.59T | Secondary |
| $235 | $441B | Above-spot wall |
| $225 | $430B | Below-spot wall |
| $232.5 | $371B | Above-spot wall |

Confirmation of phase-3 pin analysis: the $230 strike is where dealer
hedging is most concentrated. Spot closed at $228.93 — pulled toward $230
from below. This is the single most important level for the next session
(though it's a 0DTE wall, fresh OI on the next chain will redistribute).

## Tool calls (audit trail)

| Tool | Args | Result |
|------|------|--------|
| `mcp__uw-pp__options_structure_gex` | `symbol=NVDA, date=2026-05-15, dte-max=45` | regime POSITIVE, ZGL $72.29 |
| `mcp__uw-pp__options_structure_dex` | `symbol=NVDA, date=2026-05-15, dte-max=45` | net_dex +$25.85T |
| `mcp__uw-pp__options_structure_vanna_charm` | `symbol=NVDA, date=2026-05-15, dte-max=45` | vanna -141.9M, charm +9.5B |
| `mcp__uw-pp__options_structure_iv_term_structure` | `symbol=NVDA, date=2026-05-15` | CONTANGO overall, 05-22 spike |
| `mcp__uw-pp__options_structure_term_skew` | `symbol=NVDA, dte-target=30, date=2026-05-15` | COMPLACENT, skew -0.02 |
| `mcp__uw-pp__options_structure_front_end_iv_ratio` | `symbol=NVDA, near-dte=7, far-dte=30, date=2026-05-15` | BACKWARDATION ratio 1.41 |
| `mcp__uw-pp__options_structure_today_gamma_flip` | `symbol=NVDA, date=2026-05-15` | Today ZGL $218.30, wall $230 |

## Tool errors

None.

## Verdict for downstream phases

- **Dealer regime:** **POSITIVE GAMMA / LONG-GAMMA** (mean-reverting,
  suppressed vol intraday). Spot well above ZGL.
- **Conviction:** 4/5 — clean structural read.
- **Three structural levels for phase-9:**
  1. **$230 — primary gamma wall** (today's 0DTE; expect magnetism on
     next session as well unless fresh OI redistributes far above).
  2. **$218.30 — Today ZGL** — breaking below would flip dealer regime
     to short-gamma and accelerate any sell-off. Use as **secondary stop
     trigger**.
  3. **$72.29 — 45-DTE ZGL** — the structural floor of the long-gamma
     regime; only relevant if NVDA crashes 60%+ (catastrophe stop).
- **Open questions for downstream phases:**
  - **Phase-6 MUST confirm NVDA earnings date**: the 05-22 IV at 74%
     vs everything else at 50–55% is unambiguously an event marker.
     Likely earnings 2026-05-21 (after close) or 2026-05-22 (before open).
  - Phase-5 `historical_iv_percentile_zscore` should tell us if this 74%
    front IV is HIGH or LOW vs NVDA's earnings history.
  - Phase-7 `insights_earnings_play` will run automatically if earnings
    are within 30 days, and will quantify the IV-rank + OI-buildup
    pre-earnings setup.
  - Skew is COMPLACENT — should phase-9 prefer a defined-risk structure
    (debit spread) over naked long calls to limit IV-crush losses if
    earnings disappoint?
