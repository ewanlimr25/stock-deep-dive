# Phase 3 — Positioning (Open Interest)

## Summary

OI is **structurally call-skewed and laddered for upside** — the clearest bullish
signal in the dive so far, and it dovetails with the 14.6% short float into a
**squeeze-target geometry**:

- **Call OI dominates**: total OI 114,155 contracts (~11.4M shares = **7.9% of the
  145.2M float**), split **74,588 call / 39,567 put → P/C OI 0.53**. Calls outnumber
  puts ~1.9:1.
- **Stacked call walls above spot**: **$20 is the dominant call wall** (call OI
  20,279, net **+14,840**, **+12.87%**), then **$22.5** (net +11,058, +27%) and
  **$25** (net +4,013, +41%) — a classic squeeze ladder of resistance/target strikes.
- **Put support is far below**: first real put wall at **$16** (put OI 5,242, −9.7%),
  then $15 / $12.5 / $10. The near-money $17.5 is mildly call-heavy. So the
  **downside OI floor (~$16) is ~10% away** — wide, typical of a volatile small-cap.
- **Fresh OI is all upside calls**: biggest builds **20C 7/17 (+1,775), 30C 7/17
  (+1,233), 17C 0DTE (+1,154), 45C 6/18 (+239)** — the squeeze-lottery footprint from
  phase-0.5/1, now confirmed as genuine new OI.
- **6/18 monthly dominates** at **34.47% of OI** (39,345 contracts) — the gravity
  expiry; today's 0DTE was 13%.

**Positioning read: BULLISH-skewed, squeeze-laddered, conviction MODERATE** (the
structure is genuinely call-heavy and asymmetric, the strongest phase so far — but
the absolute OI is small-cap-sized and the bullish strikes are far OTM). The geometry
hands phase-9 a clean asymmetric-upside thesis: **spot $17.77 → $20 call wall (+12.9%)
→ $22.5 (+27%)**, with downside structurally cushioned only ~10% lower at $16.

## OI walls (`uw oi oi-by-strike`) `[OI:oi-by-strike]`

| Strike | Role | Call OI | Put OI | Net OI | Dist % |
|--------|------|---------|--------|--------|--------|
| **20** | **call wall / resistance** | 20,279 | 5,439 | **+14,840** | **+12.87** |
| 17.5 | call-heavy | 11,605 | 8,694 | +2,911 | −1.24 |
| **22.5** | **call wall / resistance** | 11,061 | 3 | **+11,058** | +26.98 |
| 25 | call wall / resistance | 6,203 | 2,190 | +4,013 | +41.08 |
| 17 | call-heavy | 2,818 | 1,252 | +1,566 | −4.06 |
| **16** | **put wall / support** | 391 | 5,242 | −4,851 | −9.71 |
| 15 | put wall / support | 1,926 | 3,332 | −1,406 | −15.35 |
| 10 | put wall / support | 890 | 5,915 | −5,025 | −43.57 |

- **Above spot:** a call ladder at 20 / 22.5 / 25 — net long-call walls stacked as
  squeeze targets. **Below spot:** first support $16 (−9.7%), thin until then. The
  book is **top-heavy with calls on a wide base** — bullish-asymmetric.

## Term structure (`uw oi term-structure`) `[OI:term-structure]`

| Expiry | DTE | Total OI | % of total | Call | Put | P/C |
|--------|-----|----------|-----------|------|-----|-----|
| 2026-05-29 | 0 | 14,829 | 12.99 | 8,005 | 6,824 | 0.85 |
| 2026-06-05 | 7 | 4,506 | 3.95 | 2,916 | 1,590 | 0.55 |
| **2026-06-18** | 20 | **39,345** | **34.47** | 24,565 | 14,780 | 0.60 |
| 2026-07-17 | 49 | (LEAP/monthly builds) | — | call-led | — | <0.6 |

- **6/18 dominates** (34.5% of OI, call-heavy P/C 0.60). Call OI > put OI at every
  near tenor. The 7/17 monthly carries the fresh 20C/30C squeeze builds.

## Fresh OI (`uw oi biggest-increases`) `[OI:biggest-increases]`

- **All top builds are calls:** 20C 7/17 (+1,775), 30C 7/17 (+1,233), 17C 0DTE
  (+1,154), 17.5C '26-09 (+532), **45C 6/18 (+239)**, 22.5C 6/18 (+125). The deep-OTM
  30C (+69%) and 45C (+153%) are **squeeze-lottery** positions — cheap convexity bets
  on a short-driven spike. No put builds in the top list.

## Pin risk (`uw oi pin-risk`) `[OI:pin-risk]`

- FSLY **outside top-100** — spot $17.77 is too far below its high-OI strike ($20,
  +12.9%) for an acute OPEX pin. No pinning constraint; $20 is a *magnet/target*, not
  a pin.

## Squeeze context (advisory) `[OI: fz]`

- Total OI ~11.4M shares = **7.9% of the 145.2M float**; **short interest 14.64% of
  float (intake)**. Call OI laddered at 20/22.5/25 above a heavily-shorted float is
  the textbook **gamma-squeeze fuel** setup — *if* price gets moving, dealer call
  hedging + short covering can compound. Today it is potential, not kinetic (phase-1:
  no sweeps, light volume).

## Tool calls

```bash
uw oi oi-by-strike      --symbol FSLY --date 2026-05-29 --json
uw oi term-structure    --symbol FSLY --date 2026-05-29 --json
uw oi biggest-increases --symbol FSLY --date 2026-05-29 --json
uw oi pin-risk          --top-n 100   --date 2026-05-29 --json   # FSLY outside top-100
```

## Tool errors

none

## Read-through

- Phase-3 is the **first phase to give a real bullish signal**, and it's a coherent
  one: call OI outnumbers puts ~1.9:1, stacked into a **$20 → $22.5 → $25 squeeze
  ladder** above a 14.6%-shorted float, with all fresh OI on the call side. This is
  exactly the positioning that precedes a short-driven spike in a name like FSLY.
- **But it is potential energy, not kinetic.** Phases 0.5/1 showed the *flow* was
  quiet (volume 9th pctile, no sweeps) and phase-2's accumulation was small. So the
  squeeze is *armed* (OI structure + short base) but **not yet triggered** (no
  volume/sweep ignition). The bullish OI skew is also concentrated **far OTM** ($20 is
  +12.9%, $22.5 +27%) — the market is positioned for a *big* move or nothing, with
  little near-money conviction.
- **Phase-9 geometry:** spot $17.77; upside targets **$20 (call wall, +12.9%)** then
  **$22.5 (+27%)**; downside first OI support **$16 (−9.7%)** reinforced by the
  phase-2 dark-pool shelf ~$17.5. Phase-4 (gamma) will say whether dealers amplify or
  dampen — critical for whether the squeeze ladder can actually fire.

## Citations

- `[OI:oi-by-strike]` $20 call wall net +14,840 (+12.9%), stacked 22.5/25; first put support $16 (−9.7%) — `uw oi oi-by-strike`
- `[OI:term-structure]` call OI 74.6k vs put 39.6k (P/C 0.53); 6/18 = 34.5% of OI — `uw oi term-structure`
- `[OI:biggest-increases]` all top builds calls — 20C/30C 7/17, 45C 6/18 (squeeze-lottery) — `uw oi biggest-increases`
- `[OI: fz]` total OI 7.9% of float vs 14.6% short float — gamma-squeeze fuel — `uw oi term-structure` + `fz`

## Upstream references

- phase-1-flow.md §Read-through — "squeeze-lottery positioning, fresh deep-OTM calls";
  phase-3 confirms those as real OI builds (20C/30C 7/17, 45C 6/18) and a 20/22.5/25
  call ladder.
- phase-0-intake.md §Finviz — "short float 14.64%"; phase-3 quantifies the squeeze
  fuel: call OI laddered above a 14.6%-shorted float.

## Next phase

- phase-4-structure.md (GEX / max-pain / skew / DEX — does dealer gamma make the $20
  ladder a squeeze accelerant or a wall, and is the IV (high) priced for the move?)
