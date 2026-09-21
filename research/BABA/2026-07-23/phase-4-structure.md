# Phase 4 — Dealer Structure & Gamma

**Ticker:** BABA · **As-of:** 2026-07-23 · **Spot:** ~$114 (GEX snapshot $113.52; OI $114.05; last print $114.99)
**Generated:** 2026-07-24
**Upstream:** phase-3-positioning.md ($120 call wall, $115 ATM battleground, open Q:
"does max-pain sit near $115 and is $120 a hard cap?"); phase-2 overhead supply $116.85–118.22.

## Summary

BABA is in a **SHORT-GAMMA regime** — GEX is **NEGATIVE**, spot (~$113.5) sits **below the
Zero-Gamma Level of $119.71**, so dealers **buy rallies and sell dips → moves get amplified,
realized vol expands** (tool: *"trend acceleration and increased volatility"*). Near-term this
is partly offset: **net DEX is +$228M** (public net call-long → dealers short calls → hedge is
to **buy** underlying, a mechanical bid) and **max pain pins at $114 (0DTE) / $115 (Aug monthly)**
— right at spot, matching phase-3's $115 battleground. The gamma map is stark: **+$8.56M positive
gamma at $120** (a stabilizing ceiling that coincides with the $120 call wall + DP overhead
supply) vs **−$3.63M negative gamma at $112** (a downside accelerant just under spot). Skew is
**COMPLACENT** (calls richer than puts, ratio 0.924 — no downside fear priced), and **vanna says
falling IV → mechanical dealer selling** (call-heavy book). Net structural picture: **pinned
~$114–115 near-term, capped hard at $119–120, but asymmetrically exposed to a downside
acceleration if $112 breaks** — consistent with phases 1–3's mild-bearish, range-capped read.

## Key signals

- **Short-gamma regime:** GEX NEGATIVE, spot ~$113.5 < ZGL **$119.71** → vol amplification
  `[STRUCT:gex]`
- **$120 = +$8.56M positive-gamma ceiling** (largest strike); **$112 = −$3.63M accelerant**
  below spot `[STRUCT:gex]`
- **Max pain $114 (0DTE) / $115 (2026-08-21)** — OI pin at spot, agrees with phase-3
  `[STRUCT:max_pain]`
- **COMPLACENT skew** — 25Δ put IV 45.5% < call IV 49.3% (ratio 0.924); no downside hedge
  bid `[STRUCT:term_skew]`
- **Vanna sell-risk on falling IV** — call-heavy book, net_vanna −2,116; DEX +$228M dealer bid
  is the offsetting support `[STRUCT:vanna_charm]` / `[STRUCT:dex]`

## Detailed findings

### GEX `[STRUCT:gex]`

- **regime = NEGATIVE** (*"Dealers net short gamma — expect trend acceleration and increased
  volatility"*), **ZGL = $119.71**, spot $113.52, total_gex $20.7M.
- Per-strike (net_gex): **$120 +8.56M** (dominant positive wall) · $125 +3.85M · **$112 −3.63M**
  · $130 +3.19M · $122 +2.41M · $119 +2.29M.
- Structure: positive gamma stacks $119–130 (above spot → stabilizing/capping); the lone large
  negative-gamma strike is **$112, just below spot → break-accelerant**. The $119.71 ZGL is the
  flip: below it (where price is) vol amplifies; reclaim $120 and dealers flip long-gamma (cap).

### DEX `[STRUCT:dex]`

net_dex **+$228.1M** (call_dex +$646.7M, put_dex −$418.6M). *"Public net call-long → dealers net
short calls → dealer hedge is to BUY underlying."* A mechanical bid supports near-term — **but in
a short-gamma regime that bid inverts on the way down** (dealers sell dips), so it is a fair-weather
support, not a floor.

### Vanna + charm `[STRUCT:vanna_charm]`

net_vanna **−2,116**, net_charm +440,714. *"Call-heavy book. Falling IV → call delta drops →
dealers (short calls) cut long-underlying hedge → SELLING pressure. Rising IV reverses."* With no
catalyst until 2026-09-04 earnings and IV rank 61, an IV bleed is plausible → **latent mechanical
selling pressure.** Bearish-leaning drift risk.

### IV term structure `[STRUCT:iv_term_structure]` + front-end ratio `[STRUCT:front_end_iv_ratio]`

- Term structure labelled **BACKWARDATION** (18 expiries, no kink), **but** front-end-IV-ratio is
  **FLAT** (near 49.16% vs far 49.75%, ratio 0.988). Net: **very mild** front-end richness — a
  small near-term stress premium (China/tariff headline risk), not an earnings-imminent spike
  (earnings 43 DTE). Don't over-weight.

### Term skew `[STRUCT:term_skew]`

25Δ **put IV 45.54% < call IV 49.26%**, skew −0.0372, ratio 0.924, interpretation **COMPLACENT**.
This is **reverse (call) skew** — the chain pays up for calls, not puts. Consistent with the
call-heavy premium/OI, but a **contrarian yellow flag**: with no downside protection bid, a
negative China/tariff/regulatory surprise is under-hedged and could move violently in the
short-gamma regime.

### Today's gamma flip

**Skipped** — `today-gamma-flip` is 0DTE/intraday-only; this run is after-hours (as-of 2026-07-23,
generated 2026-07-24). Not meaningful post-session.

### Max pain `[STRUCT:max_pain]`

| Expiry | Max-pain strike | dist from spot | P/C OI |
|--------|-----------------|----------------|--------|
| 2026-07-24 (0DTE) | **$114** | −0.0% | 0.289 |
| 2026-07-31 | $113 | −0.9% | 0.409 |
| 2026-08-07 | $112 | −1.8% | 0.148 |
| 2026-08-14 | $118 | +3.5% | 0.376 |
| **2026-08-21** (monthly) | **$115** | +0.8% | 0.416 |

Near-term OI gravity is **$113–115, right at spot** — the Aug-monthly magnet $115 matches
phase-3's $115 ATM battleground and OPEX cliff. Static-OI caveat applies; in short gamma the pin
is **weak** — a catalyst can override it and the move will travel.

## Tool calls (audit)

| Datapoint | Command | jq path |
|-----------|---------|---------|
| GEX regime/ZGL | `uw options-structure gex --symbol BABA --dte-max 45 --date 2026-07-23` | `.{regime,zero_gamma_level,underlying_price,total_gex}`, `.per_strike[].net_gex` |
| DEX | `uw options-structure dex --symbol BABA --dte-max 45 --date 2026-07-23` | `.{net_dex,call_dex,put_dex,interpretation}` |
| vanna/charm | `uw options-structure vanna-charm --symbol BABA --dte-max 45 --date 2026-07-23` | `.{net_vanna,net_charm,vanna_interpretation}` |
| IV term / FEIR | `uw options-structure iv-term-structure` / `front-end-iv-ratio --near-dte 7 --far-dte 30` | `.structure`, `.{near_iv,far_iv,ratio,regime}` |
| skew | `uw options-structure term-skew --symbol BABA --dte-target 30 --date 2026-07-23` | `.{put_25d_iv,call_25d_iv,skew_ratio,interpretation}` |
| max pain | `uw options-structure max-pain --symbol BABA --dte-max 30 --date 2026-07-23` | `.results[].{expiry,max_pain_strike,distance_pct,put_call_oi_ratio}` |

## Tool errors

None. (GEX per-strike field is `net_gex` not `gex`; max-pain strike is `max_pain_strike` — both
re-parsed cleanly on validated JSON. Spot differs slightly across tools — GEX/close $113.52 vs
last print $114.99 — intraday-vs-close snapshotting; treated as ~$114 band.)

## Verdict for downstream

- **Dealer regime: SHORT GAMMA (negative GEX), spot below ZGL $119.71.** Trend-amplifying, vol
  expanding — the dominant structural fact. Near-term pinned $113–115 by max-pain + a positive
  DEX dealer bid, but that support inverts on a break.
- **Conviction: 3/5** — the short-gamma regime and complacent skew are clear; the near-term pin
  + positive DEX temper the immediacy (the regime bites most on a catalyst break).
- **Three structural levels for phase-9 (+ max-pain magnet):**
  1. **ZGL $119.71** = gamma flip; with the **$120 +$8.56M gamma wall**, DP overhead supply, and
     $120 OI call wall → **hard ceiling $119–120** (reclaim flips dealers long-gamma).
  2. **$112 negative-gamma accelerant** — a break below the $112–113 shelf lets the short-gamma
     regime chase price lower (align with phase-2 $113 block floor).
  3. **Max-pain magnet $114 (0DTE) / $115 (Aug monthly)** — the near-term OI pin at spot.
- **Open questions:** With complacent skew + short gamma, is the risk/reward a **downside**
  break of $112 (asymmetric, under-hedged) vs a capped $120 upside? Does historical (phase-5)
  show BABA's edge after a mild-bearish-flow + short-gamma setup? Does macro (phase-6) carry a
  China/tariff catalyst that the complacent skew is under-pricing?
