# Phase 4 — Dealer Structure & Gamma

**Ticker:** RDDT
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T00:00:00Z
**Upstream phases cited:** phase-0.5-context.md, phase-1-flow.md, phase-3-positioning.md

## Summary

Mechanically, RDDT is set up to **amplify, not dampen, its next move — with a
downside lean but a coiled vanna offset.** Dealers are **fully short gamma**
(total GEX **−$11.66M**, regime FULLY_NEGATIVE, no zero-gamma flip anywhere in the
45-DTE window) and spot **$141.71 sits in the densest negative-GEX zone** (142
−$3.30M, 140 −$2.35M, 145 −$1.87M, 141 −$1.20M, 143 −$1.09M). In short gamma,
dealers **sell dips and buy rallies → trend amplification + expanded realized
vol**. DEX confirms the downside tilt: **net −$209M** (public is net put-long,
dealers are short those puts, hedge = SELL underlying), so a decline begets more
dealer selling. The offset: **net vanna +961 (positive)** — with IV already cheap
(rank 18.7), *if* IV bleeds further while spot stabilizes, dealers short puts
mechanically **buy** the underlying (vanna-squeeze fuel). Term structure shows **no
genuine event stress** (the "BACKWARDATION" label is a 0DTE 201%-IV artifact;
ex-0DTE the curve is mild contango and the front-end ratio is FLAT 1.011), and
30-DTE skew is **COMPLACENT** — calls are *richer* than puts (skew_ratio 0.982),
so no downside fear is priced and **puts are cheap**. Net: a short-gamma,
net-short-dealer-delta tape that accelerates a break of the 140 floor, but with a
cheap-put/positive-vanna coil that can snap back up if the selling stops.

## Key signals

- **FULLY_NEGATIVE GEX, total −$11.66M, no ZGL** → short-gamma = moves amplified,
  vol expands [STRUCT:gex]
- Spot 141.71 pinned in the **140–145 negative-gamma cluster** (142 strike
  −$3.30M is the most intense) — the mechanical battle zone [STRUCT:gex]
  [STRUCT:today_gamma_flip]
- **DEX −$209M** (put_dex −$324M vs call_dex +$116M) → dealers net short underlying
  hedge; declines self-reinforce [STRUCT:dex]
- **Net vanna +961 (positive)** → falling-IV + stable-spot = mechanical dealer
  BUYING; coiled squeeze setup [STRUCT:vanna_charm]
- **Skew COMPLACENT** (25Δ put IV 63.0% < call IV 64.2%) → no downside fear priced;
  **puts cheap** → favours debit put structures for downside [STRUCT:term_skew]

## Detailed findings

### GEX — [STRUCT:gex]

- **Total net GEX −$11,655,250; regime FULLY_NEGATIVE; zero_gamma_level = null**
  (no flip in 45 DTE — spot is deep in short-gamma territory).
- Most negative strikes (gamma battle zone): **142 (−3.30M)**, 140 (−2.35M),
  145 (−1.87M), 141 (−1.20M), 143 (−1.09M), 135 (−0.85M), 120 (−0.79M),
  130 (−0.62M), 137 (−0.60M), 131 (−0.57M).
- First **positive-GEX** strikes above: **150 (+0.62M)** and **160 (+0.88M)** →
  above ~150 dealers flip toward long gamma (dampening). **150 is a structural
  stabilization ceiling.**
- Interpretation: with spot at 141.71 inside the heaviest negative cluster, a
  decisive break **below 140** hands dealers more selling (downside acceleration);
  a reclaim **above 150** would mute amplification.

### DEX — [STRUCT:dex]

`net_dex −$208,798,613` (put_dex −$324.3M, call_dex +$115.5M). Public is net
**put-long**; dealers are net short puts; the hedge is to **SELL underlying**, and
that selling **grows as spot falls** (short-put delta lengthens). This is the
mechanical engine behind phase-0.5's accelerating net-bearish sessions. Ties to
phase-3: the public put-length is *standing* OI (e.g. 120P 6/18 5,678 contracts),
not today's flow — today's flow was call-writing, not new puts.

### Vanna + charm — [STRUCT:vanna_charm]

`net_vanna +961` (put_vanna +1,791, call_vanna −831), `net_charm +5,649`. Put-heavy
book ⇒ positive public vanna. **Falling IV → |put delta| shrinks → dealers (short
puts) buy back underlying.** With IV rank already at 18.7, this is the bullish
mechanical offset to the short-gamma downside engine: if the selloff stalls and the
already-cheap IV bleeds further, dealer vanna hedging becomes a **mechanical bid**.
Positive charm adds a small same-direction (time-decay) dealer-buy drift. **Coiled
both ways; the resolution depends on whether 140 holds.**

### IV term structure — [STRUCT:iv_term_structure]

Labelled **BACKWARDATION**, but this is a **0DTE artifact**: the 2026-05-22 expiry
prints avg IV **201.4%** (expiring-today blow-up). Ex-0DTE the curve is *upward*:
5/29 61.7% → 6/18 65.5% → 7/17 66.1% → 8/21 71.6% → 2028 ~73% (mild **contango**).
`kink_expiry: null`. **No genuine front-month event stress** — consistent with
earnings not until **2026-07-30**. Discount the backwardation flag.

### Front-end IV ratio — [STRUCT:front_end_iv_ratio]

near (10DTE) 64.3% / far (31DTE) 63.6% → **ratio 1.011 = FLAT**. Confirms no
event-stress; no catalyst priced into the front. The down-move is a price event,
not a vol event.

### Term skew (30DTE) — [STRUCT:term_skew]

25Δ put IV **63.02%** vs 25Δ call IV **64.15%** → skew −0.0113, skew_ratio 0.982 →
**COMPLACENT** (calls richer than puts). Two reads, both useful: (1) contrarian —
the market prices **no** downside fear despite an 18% drawdown and the most bearish
flow day in the window, a mild "too-calm" yellow flag; (2) actionable — **puts are
cheap relative to calls**, so any downside expression in phase-9 should be a
*debit* put structure (or put spread), not a credit one.

### Today's gamma flip (0DTE / EOD snapshot) — [STRUCT:today_gamma_flip]

Run is EOD (not intraday) — treat as snapshot. regime NEGATIVE, today_total_gex
−$9.28M, `atm_flip_strike 103` (far below spot — only a crash flips today's book
positive). "Walls" (all negative GEX in short-gamma) cluster at **142 (−3.21M),
140, 145, 141, 143** — the same 140–145 battle zone. No 0DTE pin (consistent with
phase-3 `oi_pin_risk` absence).

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `options_structure_gex` | symbol=RDDT, dte≤45 | FULLY_NEGATIVE, −$11.66M, no ZGL |
| `options_structure_dex` | symbol=RDDT, dte≤45 | net −$209M, dealers sell into declines |
| `options_structure_vanna_charm` | symbol=RDDT, dte≤45 | vanna +961, coiled squeeze if IV falls |
| `options_structure_iv_term_structure` | symbol=RDDT | "backwardation" = 0DTE artifact; ex-0DTE contango |
| `options_structure_term_skew` | symbol=RDDT, dte30 | COMPLACENT, calls richer (puts cheap) |
| `options_structure_front_end_iv_ratio` | near7/far30 | FLAT 1.011 — no event stress |
| `options_structure_today_gamma_flip` | symbol=RDDT | NEGATIVE, walls 140–145, flip 103 |

## Tool errors

None.

## Verdict for downstream

- **Dealer regime:** **SHORT GAMMA** (fully negative, no flip) + **net short
  dealer delta** (DEX −$209M) = downside-amplifying. Offset by **positive vanna**
  (cheap-IV squeeze coil). Transitional-bearish-with-a-spring.
- **Conviction:** 4/5 that the regime is short-gamma/amplifying (total GEX strongly
  negative, unambiguous). Lower conviction on *direction* — the vanna coil is real.
- **Three structural levels for phase-9:**
  1. **140** — lower edge of the negative-gamma cluster; **break = downside
     acceleration** (dealer selling). Primary stop/invalidation reference.
  2. **142** — most-negative GEX strike; spot sits here = max-amplification pivot.
  3. **150** — first positive-GEX shelf; reclaim mutes amplification = upside
     stabilization target / where a bounce meets long-gamma resistance (also the
     phase-2 5/21 DP level).
- **Open questions:**
  - Does phase-5 history show RDDT short-gamma + net-bearish-flow days resolving
    *down* (amplification wins) or *up* (vanna/dip-buy wins)? This is the crux.
  - Is the complacent skew (no put bid) a reliable contrarian "too calm" tell here,
    or just RDDT's structural call-demand signature? → phase-7c sentiment.
  - The cheap-put + short-gamma combo argues a **debit put spread** expresses the
    downside cleanly if the thesis is bearish — flag for phase-9 structure choice.
