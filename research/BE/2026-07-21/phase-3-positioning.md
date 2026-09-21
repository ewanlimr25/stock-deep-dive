# Phase 3 — Open Interest & Positioning

**Ticker:** BE
**As-of date:** 2026-07-21
**Generated:** 2026-07-22T08:15:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-0.5-context.md

## Summary

OI confirms the phase-1 structure with a **bullish long-term / range-defined
near-term** shape. The single strongest structural level is the **197.5 put wall
(net −31,125 OI ≤30DTE)** — now corroborated by three independent lanes (phase-1
put-write sweeps, phase-2 DP price-level $214.9M, phase-3 OI). Long-dated
conviction is a **Jan-2027 LEAP call ladder (310/430/510, +4,790 OI on 310C)**,
partly **funded by rolling near-dated calls out** (closing Aug/Sep 250–360 calls).
Near-term is capped by a **250 call wall** with spot pinned at the **225
call_heavy battleground (−0.6% from spot)**. Two OPEX gravity wells straddle
earnings (2026-07-28): the **7/24 weekly (3 DTE, put-heavy P/C 3.22, 21.1% of
OI)** for the pre-print pin and the **8/21 monthly (31 DTE, call-heavy, 21.6% —
the largest cliff)** where the post-earnings move will concentrate.

## Key signals

- **Put wall 197.5: net −31,125 OI (≤30DTE), 12.8% below spot** — dominant support `[OI:oi_by_strike]`
- **LEAP call ladder Jan-2027: 310C +4,790 OI** (biggest single build), 430C +1,800,
  510C +1,046 — bullish long-term accumulation `[OI:biggest_increases]`
- **Roll-up-and-out:** closing 8/21 300C (−1,157), 8/7 250C (−938), 9/18 360C
  (−682), 8/21 330C (−592) → opening Jan-2027 LEAPs `[OI:decrease_with_volume]`
- **250 call wall (10.4% OTM, net +4,671 ≤30DTE)** near-term resistance; **225 =
  call_heavy at spot** (net +4,273, dist −0.6%) — the battleground `[OI:oi_by_strike]`
- **OPEX cliffs: 8/21 21.62% (call-heavy) > 7/24 21.14% (put-heavy P/C 3.22)**;
  earnings 7/28 sits between them `[OI:term_structure]`

## Detailed findings

### OI walls by strike — tradeable horizon (≤30 DTE) `[OI:oi_by_strike]`

| Strike | call_oi | put_oi | net_oi | role | dist% |
|--------|---------|--------|--------|------|-------|
| **197.5** | 1,761 | 32,886 | **−31,125** | put_wall_support | −12.8 |
| 165 | 4 | 18,860 | −18,856 | put_wall_support | −27.1 |
| 200 | 1,521 | 6,855 | −5,334 | put_wall_support | −11.7 |
| 210 | 1,660 | 6,692 | −5,032 | put_wall_support | −7.3 |
| 180 | 186 | 7,575 | −7,389 | put_wall_support | −20.5 |
| **225** | 5,603 | 1,330 | +4,273 | **call_heavy (@spot)** | −0.6 |
| **250** | 6,194 | 1,523 | +4,671 | call_wall_resistance | +10.4 |
| 400 | 9,258 | 0 | +9,258 | call_wall_resistance | +76.7 (LEAP) |

All-expiry aggregate adds the LEAP resistance stack: **330 (net +36,528, the
largest wall overall, +45.7%)**, 350 (+26,179), 300 (+19,769) — these are the
Jan-2027 LEAP targets, not near-term caps. Near-term tradeable map: **support
197.5/210, spot pivot 225, resistance 250.**

### OI term structure — OPEX cliffs `[OI:term_structure]` (total_oi 769,142, 16 expiries)

| Expiry | DTE | call_oi | put_oi | P/C | % of total OI |
|--------|-----|---------|--------|-----|---------------|
| **2026-08-21** | 31 | 93,945 | 72,362 | 0.77 | **21.62%** (largest — post-ER monthly) |
| **2026-07-24** | 3 | 38,554 | 124,048 | **3.22** | **21.14%** (pre-ER weekly, put-heavy) |
| 2026-09-18 | 59 | 65,791 | 39,871 | 0.61 | 13.74% |
| 2027-01-15 | 178 | 32,895 | 68,190 | 2.07 | 13.14% (LEAP zone) |
| 2026-07-31 | 10 | 34,951 | 47,976 | 1.37 | 10.78% |

Earnings 2026-07-28 lands between the 7/24 (put-heavy pin) and 8/21 (call-heavy
gravity) cliffs — the post-print repricing concentrates into 8/21.

### Largest OI increases `[OI:biggest_increases]` (option_symbol parsed)

| Contract | Expiry / type / strike | OI Δ | vol | Read |
|----------|------------------------|------|-----|------|
| BE270115C00310000 | 2027-01-15 C 310 | **+4,790** | 5,023 | LEAP call (bullish, phase-1 block) |
| BE260821P00210000 | 2026-08-21 P 210 | +2,912 | 3,165 | post-ER put (written per phase-1) |
| BE260821P00040000 | 2026-08-21 P 40 | +2,792 | 3,169 | deep tail put (lottery/structured) |
| BE260724P00170000 | 2026-07-24 P 170 | +1,979 | 2,841 | near put |
| BE260724C00250000 | 2026-07-24 C 250 | +1,883 | 2,735 | 250 call wall (written) |
| BE270115C00430000 | 2027-01-15 C 430 | +1,800 | 1,800 | LEAP ladder rung |
| BE270115C00510000 | 2027-01-15 C 510 | +1,046 | 1,286 | LEAP ladder rung |

### Closing / roll activity `[OI:decrease_with_volume]`

Calls closing across the Aug/Sep 250–360 band (8/21 300C −1,157, 8/7 250C −938,
9/18 360C −682, 8/21 330C −592, 8/14 235C −744) while Jan-2027 LEAP calls open →
a **roll-up-and-out** of the bullish call exposure into 2027. Near put 7/24 165P
closing (−1,157) = pre-earnings de-hedging at that strike.

### Smart positioning `[OI:smart_positioning]`

Per-contract inferred_direction is **two-sided and noisy** (tags 310C LEAP
`bullish`, 250C write `bearish`, 40P write `bullish`) — consistent with the
mixed/two-sided campaign (long LEAP calls, written near puts + 250 calls), not a
clean one-way signal. Do not over-read the per-row tags.

### Pin risk / OPEX concentration `[OI:pin_risk / opex_concentration]`

Both market-wide screens returned **no BE row** (BE outside the top on the pin /
concentration metrics). The term-structure above is the OPEX-cliff read instead;
the 7/24 weekly is the mechanical pin candidate (3 DTE, put-heavy) but BE's own
turnover isn't extreme enough to rank market-wide.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows |
|------------------|--------------------------|------|
| `oi oi-by-strike --symbol BE --dte-max 30` | 197.5 net_oi −31,125 ← `.results[]｜.net_oi/.role` | 10 |
| `oi oi-by-strike --symbol BE` (all-exp) | 330 net +36,528 ← same | 10 |
| `oi term-structure --symbol BE` | 8/21 21.62%, 7/24 21.14% P/C 3.22 ← `.term_structure[]｜.pct_of_total_oi/.put_call_oi_ratio` | 16 exp |
| `oi biggest-increases --symbol BE --min-oi-change 500` | 310C 27' +4,790 ← `.results[]｜.oi_diff_plain` + parse `.option_symbol` | 20 |
| `oi decrease-with-volume --symbol BE --min-volume 100` | 8/21 300C −1,157 ← `.oi_diff_plain` | 15 |
| `oi smart-positioning --symbol BE` | mixed per-row `inferred_direction` | 20 |
| `oi pin-risk --dte-max 7` / `oi opex-concentration` | no BE row ← `select(.ticker=="BE")` empty | — |

## Tool errors

<none — all reads valid JSON. term-structure results live under `.term_structure`
(not `.results`); pin-risk/opex-concentration are market-wide and returned no BE row
(recorded, not an error).>

## DATA NOTE / CORRECTION

- `oi term-structure` first jq (`.results`) returned length 0; the array is
  `.term_structure`. Re-read against the correct path — all cliff percentages
  above trace to `.term_structure[].pct_of_total_oi`.
- `biggest-increases`/`decrease-with-volume` carry no side/expiry columns; both
  parsed from `.option_symbol` (OPRA) per the phase spec, not inferred from net_oi.

## Verdict for downstream phases

- **Positioning bias:** **bullish long-term (LEAP call ladder + roll-up-and-out),
  range-defined near-term** — put-write floor 197.5, call resistance 250, spot
  battleground 225. Two-sided, structured; not an aggressive one-way breakout.
- **Conviction:** **3 / 5** — the LEAP accumulation and 197.5 floor are strong and
  triple-confirmed, but the near-term is a written-premium range, not a directional
  thrust; smart-positioning tags are mixed.
- **Largest OI build as % of float:** **n/a** — no `Shs Float` from phase-0.
  310C build 4,790 contracts ≈ 479k share-equiv; on ~230M shares out (phase-7b to
  confirm) ≈ 0.2% — structural-leaning but not float-dominating. Advisory only.
- **Three pin/cliff strikes for phase-9:** **put_wall_support 197.5** (floor/stop
  reference), **call_wall_resistance 250** (near-term upside cap), **OPEX gravity
  8/21 monthly** (post-earnings move concentrates here); the 7/24 weekly is the
  pre-print pin candidate.
- **Open questions:** Is the 250-call OI covered writing against the DP holdings
  (phase-2 large-tier buy 0.561) or naked resistance? Does phase-4 max-pain
  gravitate to 225–230 into 7/24 / 8/21? The LEAP ladder — long 310 vs short
  430/510 (call spread) or outright — determines how far the bullish target reaches.
