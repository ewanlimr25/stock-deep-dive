# Phase 3 — Open Interest & Positioning

**Ticker:** CMPS
**As-of date:** 2026-06-18
**Generated:** 2026-06-20
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md

## Summary

Standing positioning is **overwhelmingly call-dominated** — the opposite of today's
bearish put flow. Every meaningful expiry skews to calls (the 2026-07-17 cliff holds
31.21% of all OI at a P/C of **0.026**), and the heaviest strikes are call walls at
$13 (+3.83% from the $12.53 close), $15 and $11. **Crucially, today's P10 LEAP put
buying is NOT yet in OI** — the 2028-01-21 expiry still shows put_oi = 0 (today's
2,011 contracts settle into the 6/19 snapshot), and `biggest-increases`/`smart-
positioning` are both **empty** (no strike added ≥500 OI on 6/18). So the chain
remains structurally bullish; the bearish event is a single brand-new position
sitting on top of a call-heavy book. CMPS is **not** a pin or OPEX-concentration
candidate this week.

## Key signals

- OPEX cliff = **2026-07-17, 31.21% of total OI, P/C 0.026** (near-all calls)
  [OI:term_structure]
- Nearest call wall (DTE≤30): **$13, net_oi +12,660, +3.83%** from spot $12.53
  [OI:oi_by_strike]
- Chain is call-heavy at $11/$12/$13/$15; only real put presence is **$10
  put_wall_support** (net_oi −2,165 in DTE≤30) [OI:oi_by_strike]
- **No settled OI build** on 6/18: `biggest-increases` empty, `smart-positioning`
  empty, `position-rolls` n=0 — today's put flow settles 6/19 [OI:biggest_increases]
- Jan-2028 expiry **put_oi = 0** → confirms the P10 LEAP put is a brand-new opening
  position (corroborates phase-1 vol/OI 13.97) [OI:term_structure]
- CMPS **absent** from pin-risk (n=25) and opex-concentration (n=20) lists
  [OI:pin_risk, OI:opex_concentration]

## Detailed findings

### OI walls by strike (`[OI:oi_by_strike]`, spot = $12.53 close)

**DTE ≤ 30 (tradeable-horizon wall map — what phase-9 sizes against):**

| Strike | call_oi | put_oi | net_oi | role | dist % |
|--------|---------|--------|--------|------|--------|
| **$13** | 13,270 | 610 | +12,660 | call_wall_resistance | **+3.83%** |
| $12 | 9,897 | 1,073 | +8,824 | call_heavy | −4.15% |
| $11 | 10,423 | 3,324 | +7,099 | call_heavy | −12.14% |
| $15 | 6,655 | 0 | +6,655 | call_wall_resistance | +19.81% |
| **$10** | 765 | 2,930 | **−2,165** | **put_wall_support** | −20.13% |
| $14 | 1,534 | 238 | +1,296 | call_wall_resistance | +11.82% |

All-expiry aggregate adds far-dated call walls ($15 net +15,321; $13 net +13,968;
$11 net +13,732) — the book is bullish at essentially every strike. The $10
put_wall_support is the only structural downside marker, and it's −20% away.

### OI term structure (`[OI:term_structure]`, total_oi across 6 expiries)

| Expiry | DTE | call_oi | put_oi | P/C | % of total OI |
|--------|-----|---------|--------|-----|---------------|
| 2026-06-18 | 0 | 15,476 | 7,450 | 0.481 | 24.65% |
| **2026-07-17** | 29 | 28,304 | 725 | **0.026** | **31.21%** ← cliff |
| 2026-08-21 | 64 | 19,919 | 1,827 | 0.092 | 23.38% |
| 2026-11-20 | 155 | 413 | 123 | 0.298 | 0.58% |
| 2027-01-15 | 211 | 13,914 | 0 | 0.000 | 14.96% |
| **2028-01-21** | 582 | 4,872 | **0** | 0.000 | 5.24% |

The **2026-07-17 expiry is the gravity well** (31.21%, almost pure calls) — feed to
phase-4 max-pain cross-check and phase-6 catalyst calendar. The 2028-01-21 put_oi=0
is the tell that today's LEAP puts are net-new.

### Largest OI increases / closing / rolls

- `biggest-increases` (min Δ 500): **empty** — no strike added ≥500 settled OI on
  6/18. [OI:biggest_increases]
- `decrease-with-volume`: 1 tiny row — CMPS260618**P12** oi_diff −33 on vol 125
  (0DTE put closing into expiry). Immaterial. [OI:decrease_with_volume]
- `position-rolls` (thr 500, near-DTE≤30): **n=0** — no near→far rolls.
- `smart-positioning`: **empty** — no inferred directional OI build today.

### Pin risk / OPEX concentration

- `pin-risk` (DTE≤7, ≤5% from spot): 25 market-wide rows, **CMPS not among them**.
- `opex-concentration` (≥40%): 20 market-wide rows, **CMPS not among them**.
- → No mechanical pin pressure on CMPS this week; price action is fundamentally
  driven, not dealer-pinned.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|------------------|--------------------------|-----------|
| `uw oi oi-by-strike --symbol CMPS --dte-max 30` | $13 call wall net_oi +12,660 @ +3.83% ← `.results[]`; $10 put support net −2,165 | 10 |
| `uw oi oi-by-strike --symbol CMPS` (all-exp) | $11 call_heavy 17,056; $15 wall net +15,321 ← `.results[]` | 10 |
| `uw oi term-structure --symbol CMPS` | Jul-17 31.21% P/C 0.026 ← `.term_structure[]`; 2028 put_oi=0 | 6 |
| `uw oi biggest-increases --min-oi-change 500` | results = [] ← `.results\|length` | 0 |
| `uw oi decrease-with-volume --min-volume 100` | P12 0DTE −33 ← `.results[0]` | 1 |
| `uw oi smart-positioning --min-oi-change 500` | results = [] | 0 |
| `uw oi position-rolls --threshold 500` | n=0 | 0 |
| `uw oi pin-risk` / `opex-concentration` | CMPS absent (0 matches) ← `test("CMPS")` | 25 / 20 |

## Tool errors

<none — `term_structure` array is under `.term_structure`, not `.results`; read
correctly on second pass (see DATA NOTE).>

## DATA NOTE / CORRECTION

- `uw oi term-structure` nests its array under `.term_structure`, **not** `.results`
  (first jq path `.results` errored on null). Re-read against `.term_structure[]` —
  all values above trace to that path.
- Spot reference reconciled: phase-1/2 intraday prints used underlying $12.03
  (~10:30 ET), but CMPS **closed $12.53** (prev_close $11.94, **+4.94%**). `oi-by-
  strike` `distance_pct` is computed off the ~$12.52 close, so **phase-9 uses $12.53
  as spot**. The bearish P10 puts were bought *into a +5% up day* — material context.

## Verdict for downstream phases

- **Positioning bias:** **Bullish (standing OI) vs bearish (today's flow) — a
  conflict.** The book is call-dominated at every expiry; the bearish signal is one
  brand-new LEAP put position not yet in OI. Structure says the crowd is long calls.
- **Conviction:** **2 / 5** on the bearish thesis from OI — standing positioning
  actively contradicts it; the new put build is real but tiny and unsettled.
- **Largest OI build as % of float:** no settled build today (biggest-increases
  empty). Today's P10 LEAP put flow = 2,011 contracts ≈ **0.156% of float**
  (share-equivalent); standing Jul-17 call OI 28,304 ≈ 2.20% of float. The put bet
  is *not* structural for this name. [OI:oi_pct_float fz]
- **Three pin/cliff strikes for phase-9:**
  1. **$13 call_wall_resistance** (+3.83%) — nearest overhead magnet/cap.
  2. **2026-07-17 OPEX cliff** (31.21% of OI, call-heavy) — gamma/gravity event.
  3. **$10 put_wall_support** (−20.13%, the LEAP put strike) — deep downside marker.
- **Open questions:** Will the P10 LEAP put OI actually build on 6/19+ (campaign) or
  was 6/18 a one-print spike (phase-1 said consistency 0.2)? Is the call-heavy book
  covered-call writing vs the dark-pool sellers, or genuine bullish speculation?
  Does max-pain (phase-4) gravitate toward the call-heavy $12–13 zone?
