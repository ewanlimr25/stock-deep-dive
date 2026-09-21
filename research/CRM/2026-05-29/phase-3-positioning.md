# Phase 3 — Positioning (Open Interest)

## Summary

OI **corroborates the bullish options flow's geometry** while quietly flagging
real downside hedging. The dominant structure:

- **$200 = the call wall (resistance / upside magnet)**: 66,706 call OI, net
  **+58,153**, **+4.71%** above spot — the single heaviest wall and the *exact*
  strike phase-1 sweeps targeted. A secondary call wall at **$195** (net +24,417,
  +2.09%).
- **Put-wall support sits well below**: $170 (put OI 37,099, −11%), $160 (34,450,
  −16%), $175 (25,701, −8.4%). The nearest meaningful support shelf is **$185**
  (slightly put-heavy, −3.15%). There is **no put wall between spot and $185** — air
  pocket just under the close.
- **Fresh OI is call-led**: biggest OI increases are 190C (+2,481), 195C (+952/+584),
  200C (+503) — but the **#2 increase is the 160P 7/17 (+1,407)**, a deliberate
  deep-OTM downside hedge that matches phase-1's 190P Sep prints.
- **6/18 monthly dominates** at **24.86% of all OI** (209,850 contracts, DTE 20) —
  the gravity expiry. Today's 0DTE (5/29) was 13.77%. Pin-risk ranks CRM #66
  (dte_to_opex 0 for the weekly), nearest high-OI strike **$200**.

**Positioning read: BULLISH-leaning geometry (call wall at $200 = clear target),
but with a defined downside-hedge tail and an air pocket to $185.** Conviction
MODERATE. The OI map says "upside capped/targeted at $195–$200, support not until
$185, tail hedges at $160–$170."

## OI walls (`uw oi oi-by-strike`, all expiries) `[OI:oi-by-strike]`

| Strike | Role | Call OI | Put OI | Net OI | Dist % |
|--------|------|---------|--------|--------|--------|
| **200** | **call wall / resistance** | 66,706 | 8,553 | **+58,153** | **+4.71** |
| 180 | call-heavy | 33,345 | 23,835 | +9,510 | −5.76 |
| 190 | call-heavy | 30,882 | 25,288 | +5,594 | −0.53 |
| **170** | **put wall / support** | 11,028 | 37,099 | −26,071 | −11.0 |
| **160** | **put wall / support** | 13,116 | 34,450 | −21,334 | −16.2 |
| 185 | put-wall support | 20,316 | 22,437 | −2,121 | −3.15 |
| **195** | **call wall / resistance** | 31,597 | 7,180 | **+24,417** | +2.09 |
| 175 | put-wall support | 11,866 | 25,701 | −13,835 | −8.38 |

- Above spot: strong net-call walls at **195 (+24.4k) and 200 (+58.2k)** → the
  $195–$200 zone is where dealers are short calls / where price is "pulled and
  capped." Below spot: the first real put support is **$185** (barely net-put),
  then a gap to the **$170/$160 put walls**. The structure is **top-heavy with
  calls, with sparse near-support** — bullish bias but a thin floor.

## Term structure (`uw oi term-structure`) `[OI:term-structure]`

| Expiry | DTE | Total OI | % of total | Call OI | Put OI | P/C OI |
|--------|-----|----------|-----------|---------|--------|--------|
| 2026-05-29 | 0 | 116,200 | 13.77 | 60,827 | 55,373 | 0.91 |
| 2026-06-05 | 7 | 29,457 | 3.49 | 19,198 | 10,259 | 0.53 |
| **2026-06-18** | 20 | **209,850** | **24.86** | 123,555 | 86,295 | 0.70 |
| 2026-07-17 | 49 | 83,011 | 9.83 | 46,415 | 36,596 | 0.79 |

- **6/18 is the dominant OPEX** (almost a quarter of all OI; call-heavy P/C 0.70).
  The front weeklies (6/5: P/C 0.53) are the most call-skewed — consistent with the
  fresh weekly-call buying in phase-1. Call OI > put OI at every meaningful tenor.

## Fresh OI (`uw oi biggest-increases`) `[OI:biggest-increases]`

- Top increases: **190C 6/5 (+2,481)**, 195C/195C, **200C 6/18 (+503)** — fresh
  upside. The standout non-call: **160P 7/17 (+1,407)** — the day's #2 OI build is a
  deep-OTM (−16%) put, a tail hedge being put on even as calls dominate.

## Smart positioning (`uw oi smart-positioning`) `[OI:smart-positioning]`

- The leaf infers **"bearish"** on the top contracts via net ask−bid: 190C 6/5 had
  prev bid-vol (2,590) > ask-vol (1,829) → net_ask_bid −761, i.e. **the prior day's
  190C traded more on the bid** (selling/writing). This is a yellow flag: some of
  the call OI may be **call-writing**, not pure long-call accumulation — and it
  echoes phase-1's 44% bid-side sweeps. Read as *mixed*, not clean long.

## Pin risk (`uw oi pin-risk`) `[OI:pin-risk]`

- CRM #66 of 80; dte_to_opex 0 (weekly), **nearest high-OI strike $200**, pin
  distance +4.71%, pin score 75,724. Not an acute pin (price is 4.7% under the
  high-OI strike), but $200 is the magnet if price grinds up into 6/18.

## Tool calls

```bash
uw oi oi-by-strike       --symbol CRM --date 2026-05-29 --json
uw oi term-structure     --symbol CRM --date 2026-05-29 --json
uw oi biggest-increases  --symbol CRM --date 2026-05-29 --json
uw oi smart-positioning  --symbol CRM --date 2026-05-29 --json
uw oi pin-risk           --top-n 80   --date 2026-05-29 --json   # market-wide; CRM #66
```

## Tool errors

- `uw oi opex-concentration` rejects `--symbol` (market-wide); covered by
  `term-structure` (6/18 = 24.86% of OI). Not blocking.

## Read-through

- OI **confirms the bullish flow's target architecture**: the $200 call wall is the
  heaviest in the chain and is exactly where phase-1's sweeps and fresh OI cluster.
  Upside objective $195→$200 is well-defined.
- But OI also **echoes phase-2's caution from a different angle**: (a) the
  smart-positioning leaf flags the marquee 190C as prior-day *bid*-traded
  (possible writing), (b) a deliberate **160P hedge** is among the largest fresh
  builds, and (c) **there's no put-wall support between spot and $185** — if the
  pop fails, little structural cushion until $185, then a gap to $170.
- **Net across phases 1–3:** options *positioning* is bullish and targets $200, but
  it is **not unhedged euphoria** (call-writing signature + tail puts), and it sits
  on a **thin near-term floor** — which is exactly the vulnerability phase-2's
  institutional selling would exploit. Phase-4's dealer gamma will determine whether
  $200 acts as a magnet (positive gamma above the flip) or whether the air pocket to
  $185 is the more dangerous side.

## Citations

- `[OI:oi-by-strike]` $200 call wall net +58,153 (+4.71%); first support $185, gap to $170/$160 — `uw oi oi-by-strike`
- `[OI:term-structure]` 6/18 = 24.86% of OI (209,850); call OI > put at every tenor — `uw oi term-structure`
- `[OI:biggest-increases]` 190C +2,481 / 200C +503 vs 160P +1,407 hedge — `uw oi biggest-increases`
- `[OI:smart-positioning]` 190C 6/5 prior-day bid>ask (net −761) → possible call-writing — `uw oi smart-positioning`

## Upstream references

- phase-1-flow.md §Sweeps — "the $200 strike is the clear magnet"; phase-3 confirms
  $200 is the heaviest call wall in the chain (net +58,153 OI).
- phase-2-dark-pool.md §Read-through — "no accumulation shelf below spot"; phase-3
  independently finds no put-wall support until $185 → the thin-floor vulnerability
  is corroborated from the OI side.

## Next phase

- phase-4-structure.md (GEX / zero-gamma flip / max-pain / skew — does dealer
  positioning make $200 a magnet and $185 a trapdoor, and where is opex gravity vs
  the $191 close?)
