# Phase 3 — Open Interest & Positioning

**Ticker:** OKLO
**As-of date:** 2026-07-17
**Generated:** 2026-07-18T00:00:00Z
**Upstream phases cited:** phase-0.5-context.md, phase-1-flow.md, phase-2-dark-pool.md

## Summary

Positioning has **two layers that point opposite ways**. Near-term flow is **bearish /
protective**: fresh OI is put-dominated — a new **$33 put (07-24) +6,518 contracts** leads,
plus $25 (08-21) and $40 puts, and smart-positioning tags **5 of 7 fresh rows bearish**. A
**put roll is confirmed** (near −5,421 → far +4,430, roll_size 4,430): the deep-ITM $50–60
puts that Phase 1 flagged are **closing at today's OPEX and rolling out**, i.e. the desk is
*maintaining* downside/short-delta structure, not abandoning it. Underneath, the **far-dated
LEAPs are heavily call-skewed** (Dec-26 68K call OI, Jan-27 64K, Jan-28 51K) — a structural
long-term-bull base that is **not** changing. No pin risk / OPEX concentration at OKLO
despite today being July monthly OPEX.

## Key signals

- **Fresh $33 put wall (07-24): oi_diff +6,518, vol 6,617** — the single largest new
  position, clean bearish/hedge ~20% below spot [OI:biggest_increases]
- **Put roll confirmed**: `near_oi_change −5,421 → far_oi_change +4,430`, put, balance 0.817
  — downside structure rolled forward, not closed [OI:position_rolls]
- **Smart-positioning net bearish**: 5/7 rows bearish incl. the $33p (+6,518) and $25p
  (+1,159) [OI:smart_positioning]
- **Deep-ITM puts closing at OPEX**: $55p −4,303 (vol 15,000), $50p −3,725, $60p −2,988 —
  the phase-1 "deep-ITM put" prints were 07-17 expiries rolling off [OI:decrease_with_volume]
- **Structural LEAP call base intact**: Dec-26 68,383 / Jan-27 63,527 / Jan-28 51,220 call
  OI — long-dated upside ownership unchanged [OI:term_structure]

## Detailed findings

### OI walls by strike (≤30 DTE, spot $41.11) — [OI:oi_by_strike]

| Strike | call_oi | put_oi | net_oi | role | dist% |
|---|---|---|---|---|---|
| 50 | 6,585 | 1,700 | +4,885 | **call_wall_resistance** | +21.6% |
| 45 | 2,225 | 5,780 | −3,555 | put_heavy | +9.5% |
| **40** | 691 | 6,221 | −5,530 | **put_wall_support** | −2.7% |
| **35** | 288 | 12,227 | −11,939 | **put_wall_support** | −14.9% |
| 33 | 0 | 6,782 | −6,782 | put_wall_support | −19.7% |
| 30 | 0 | 8,965 | −8,965 | put_wall_support | −27.0% |
| 60/70/80 | 8K/8K/10K | low | + | call_wall_resistance | +46/70/95% |

Structure: **no near-term call OI between spot and $50** — the first overhead call wall is
**$50 (+21.6%)**. Downside is layered with put walls at **$40 (support at spot), $35
(heaviest, 12,227), $33, $30**. Puts define the near-term map; calls are all far OTM.

### OI term structure (OPEX cliff) — [OI:term_structure], total OI 548,875

| Expiry | call_oi | put_oi | % of total OI |
|---|---|---|---|
| **2026-07-17 (today, OPEX)** | 65,131 | 41,318 | **19.4%** (expires today → rolls off) |
| 2027-01-15 (LEAP) | 63,527 | 28,934 | 16.9% |
| 2026-12-18 (LEAP) | 68,383 | 9,724 | 14.2% (call-skewed) |
| 2026-08-21 (1st post-ER monthly) | 32,717 | 29,614 | 11.4% (balanced) |
| 2028-01-21 (LEAP) | 51,220 | 8,909 | 11.0% (call-skewed) |
| 2026-09-18 | 20,135 | 22,833 | 7.8% (put-skewed) |

The gravity well is **today's OPEX (19.4%)** which expires tonight. Post-OPEX the tradeable
cliffs are **2026-08-21** (first monthly after the 08-10 earnings, balanced) and the
call-heavy LEAPs. Cross-check phase-4 max-pain and phase-6 catalyst calendar.

### Largest OI increases (fresh positions) — [OI:biggest_increases]

| Contract | Side/Exp | OI Δ | Vol | Read |
|---|---|---|---|---|
| OKLO260724P00033000 | $33 put 07-24 | **+6,518** | 6,617 | big fresh bearish/hedge |
| OKLO260821P00025000 | $25 put 08-21 | +1,159 | 1,460 | post-ER crash hedge |
| OKLO260918P00040000 | $40 put 09-18 | +770 | 835 | ATM put |
| OKLO260821P00040000 | $40 put 08-21 | +530 | 1,294 | ATM put (post-ER) |
| OKLO260717C00048/44000 | $48/$44 calls 0DTE | +1,074/+933 | — | 0DTE noise |

Fresh OI is **put-heavy** across four distinct put strikes/expiries; the only call adds are
0DTE (expiring, noise).

### Closing / roll activity — [OI:decrease_with_volume / position_rolls]

Decreases concentrate in **07-17 deep-ITM puts** ($55 −4,303 / $50 −3,725 / $60 −2,988,
each on 7K–15K volume) — the phase-1 "deep-ITM put" prints were this OPEX expiring/closing.
**1 put roll detected** (near −5,421 → far +4,430): the position is rolled forward, not
liquidated → sustained downside/protective posture (matches phase-1's 5-day bearish
persistence).

### Smart positioning — [OI:smart_positioning]

7 rows, **5 bearish** (incl. the two largest: $33p +6,518, $25p +1,159) and the 0DTE
calls tagged bearish (written/sold). Only $40p 09-18 (+770) tagged bullish (put selling).
Net inferred direction: **bearish**.

### Pin risk / OPEX concentration — [OI:pin_risk / opex_concentration]

OKLO is **outside** both the market-wide pin-risk top-40 (≤7 DTE, ≤5% distance) and the
opex-concentration top-40 (≥40%). Despite today being July OPEX, OKLO's near-spot OI is
not concentrated enough to pin — the call OI is far OTM and the put OI is spread across
$30–$45. **No pin commentary applies.**

## Tool calls (audit trail)

| Command | Key value(s) ← `jq` path | Rows |
|---|---|---|
| `oi oi-by-strike --dte-max 30` | $40 put_wall_support net −5,530 ← `.results[]` | 12 |
| `oi term-structure` | 07-17 = 19.4% of OI ← `.term_structure[].pct_of_total_oi` | 16 exp |
| `oi biggest-increases --min-oi-change 500` | $33p +6,518 ← `.results[0].oi_diff_plain` | 7 |
| `oi decrease-with-volume` | $55p −4,303 ← `.results[0]` | 8 |
| `oi smart-positioning` | 5/7 bearish ← `.results[].inferred_direction` | 7 |
| `oi position-rolls --threshold 500` | put roll 4,430 ← `.results[0]` | 1 |
| `oi pin-risk / opex-concentration` | OKLO outside top-40 ← filtered | 0 (OKLO) |

## Tool errors

`term-structure` `put_call_ratio` is `null` per row — used null-safe jq
(`(.pct_of_total_oi // 0)`); P/C derived from call_oi/put_oi where needed. Not fatal.

## DATA NOTE / CORRECTION

First read stood. Far-dated call walls ($90/$200 in the all-expiry view) are LEAP strikes
— excluded from the near-term (≤30 DTE) tradeable wall map above, per skill guidance.

## Verdict for downstream

- **Positioning bias:** near-term **puts being built + rolled forward = bearish/protective**;
  long-term LEAP call base = structurally bullish but static. Net for a swing horizon: **bearish-lean**.
- **Conviction:** 3 / 5 (fresh $33p + confirmed roll + bearish smart-positioning is a
  reasonably clean, corroborated read; tempered by phase-0.5 "normal day").
- **Largest OI build as % of float:** $33p +6,518 ≈ 651,800 share-equiv ≈ **~0.37%** of
  ~174M shares-out proxy (true float n/a) — **moderate, not structural** for this name; advisory.
- **Three pin/cliff strikes for phase-9:**
  1. **Put wall support $40** (net −5,530, at spot −2.7%) — first downside shelf.
  2. **Heavy put wall $35** (put_oi 12,227) + fresh **$33** — the real downside magnet.
  3. **Call wall resistance $50** (+21.6%) — first overhead; nothing between spot and $50.
- **Open questions:** Is the $33/$25 put build a hedge against the LEAP-call long base
  (collar) or a standalone bearish view? Does phase-4 GEX/max-pain confirm $40–$41 as the
  gamma pivot and $50 as the call-wall ceiling? Does phase-5 show OKLO tends to drift or
  gap around 08-10 earnings (relevant to the $25/$40 post-ER put hedges)?
