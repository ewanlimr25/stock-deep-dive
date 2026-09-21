# Phase 3 — Open Interest & Positioning

**Ticker:** IREN
**As-of date:** 2026-06-05
**Generated:** 2026-06-07T01:05Z
**Upstream phases cited:** phase-0-intake.md (float 324.15M), phase-1-flow.md, phase-2-dark-pool.md

## Summary

Positioning shows a **fresh, aggressive front-week put build against a standing
long-dated call mountain**. The single largest OI event is the **06/12 50P:
+29,735 contracts (1,601 → 31,336), bought 81% at the ask** — a ~0.92%-of-float
share-equivalent hedge/short placed right at the −8% strike during the flush
[OI:biggest_increases]. The whole front week is now put-skewed (06/12 P/C OI
ratio **3.43**) while the structural OI lives in calls: Jan-2027 holds **19.67%
of all 1.91M OI** (256,672 calls vs 118,623 puts) and the all-expiry 110 strike
carries 155k call OI [OI:term_structure, OI:oi_by_strike]. Critically, the
far-LEAP buying phase-1 flagged **confirmed as opening**: 110C 09/2028 OI
+4,018 and 110C 06/2027 +3,044 (ask-side) — institutions added 2027/2028 upside
even as the front of the book hedged. Phase-1's open question (are the Jan-27
bid-side call sales closes?) is NOT yet answerable — today's selling prints in
tomorrow's OI; no Jan-27 decreases appear in today's data.

## Key signals

- **50P 06/12 +29,735 OI** (vol 33,555; prev_ask_volume 22,718 vs bid 5,342 →
  bought at ask; avg $0.776, $2.60M premium) — biggest build on the chain,
  bearish/protective [OI:biggest_increases].
- **55P 06/12 +8,285** (→38,746 total; ask 8,461 vs bid 1,516) + **30P 06/12
  +7,505** (ask 8,024 vs 286; $0.049 disaster puts) — layered front-week put
  buying [OI:biggest_increases].
- **64C 06/12 +7,051** (266→7,317; ask 7,111 vs bid 376; $2.29M) — a real
  bullish recovery bet at +18% OTM, the counter-flow [OI:biggest_increases].
- **LEAP 110C builds opened**: 09/15/2028 +4,018 (→16,370; $10.97M traded
  mid/cross) and 06/17/2027 +3,044 (→21,616; ask 3,058 vs bid 34)
  [OI:smart_positioning inferred bullish on the 06/27 line].
- **Put SELLING at 60P 06/12 (+2,298, bid 2,345 vs ask 757) and 42P 08/21
  (+2,002, bid 2,000 vs ask 2)** — premium sellers fading further downside
  [OI:biggest_increases].

## Detailed findings

### OI walls by strike — all-expiry [OI:oi_by_strike]

| Strike | call_oi | put_oi | net_oi | role | dist % |
|---|---|---|---|---|---|
| 110 | 155,304 | 1,266 | +154,038 | call_wall_resistance | +102.3 |
| 50 | 66,971 | 76,679 | −9,708 | put_wall_support | −8.1 |
| 60 | 82,336 | 57,508 | +24,828 | call_wall_resistance | +10.3 |
| 70 | 120,397 | 7,822 | +112,575 | call_wall_resistance | +28.7 |
| 65 | 104,465 | 21,598 | +82,867 | call_wall_resistance | +19.5 |
| 55 | 34,672 | 71,294 | −36,622 | **put_heavy (ATM battleground)** | +1.1 |
| 30 | 19,366 | 71,501 | −52,135 | put_wall_support | −44.8 |
| 40 | 23,355 | 61,411 | −38,056 | put_wall_support | −26.4 |
| 80 | 77,231 | 3,429 | +73,802 | call_wall_resistance | +47.1 |
| 100 | 67,681 | 556 | +67,125 | call_wall_resistance | +83.9 |

Note: 50 all-expiry is two-sided (67k calls vs 77k puts) — the clean put wall
is in the ≤30DTE cut below. 110/100/80/70 are the LEAP call mountain.

### OI walls — ≤30DTE (the tradeable map) [OI:oi_by_strike --dte-max 30]

| Strike | call_oi | put_oi | net_oi | role | dist % |
|---|---|---|---|---|---|
| **50** | 8,952 | **54,682** | −45,730 | put_wall_support | −8.1 |
| **55** | 10,493 | **51,891** | −41,398 | put_heavy (ATM) | +1.1 |
| 70 | 43,614 | 4,173 | +39,441 | call_wall_resistance | +28.7 |
| **60** | 27,719 | 14,050 | +13,669 | call_wall_resistance | +10.3 |
| 40 | 5,030 | 36,625 | −31,595 | put_wall_support | −26.4 |
| 75 | 32,908 | 0 | +32,908 | call_wall_resistance | +37.9 |
| 38 | 364 | 32,301 | −31,937 | put_wall_support | −30.1 |
| **65** | 22,860 | 8,144 | +14,716 | call_wall_resistance | +19.5 |
| 30 | 1,680 | 28,739 | −27,059 | put_wall_support | −44.8 |
| 45 | 289 | 26,617 | −26,328 | put_wall_support | −17.3 |

Near-term structure: put support ladder 50 → 45 → 40 → 38 → 30 below spot
(54.38); call resistance 60 → 65 → 70 → 75 above. Spot sits just under the
55 put-heavy battleground.

### OI term structure [OI:term_structure] (total_oi 1,908,361; 19 expiries)

| Expiry | DTE | call_oi | put_oi | P/C | % of total |
|---|---|---|---|---|---|
| **2027-01-15** | 224 | 256,672 | 118,623 | 0.462 | **19.67 ← cliff** |
| 2026-06-18 | 13 | 169,988 | 145,939 | 0.859 | 16.55 |
| 2026-06-05 (today) | 0 | 135,273 | 169,859 | 1.256 | 15.99 (rolls off tonight) |
| 2026-06-12 | 7 | 39,007 | 133,835 | **3.431** | 9.06 |
| 2026-09-18 | 105 | 117,636 | 37,927 | 0.322 | 8.15 |
| 2026-07-17 | 42 | 66,691 | 37,616 | 0.564 | 5.47 |
| 2028-01-21 | 595 | 66,076 | 32,231 | 0.488 | 5.15 |
| 2026-08-21 | 77 | 51,158 | 31,911 | 0.624 | 4.35 |

Reads: (1) the structural gravity well is **Jan-2027, call-heavy** — the LEAP
complex phase-1 saw churning; (2) the **front week 06/12 is the most
put-skewed expiry on the board (P/C 3.43)** — that's where today's hedges went;
(3) June monthly OPEX (06/18) holds 16.55% with balanced P/C 0.86 — the
near-term pin battleground; (4) ~16% of all OI expires TODAY — tomorrow's
chain will look structurally different.

### Largest OI increases [OI:biggest_increases] (top rows; side from prev ask/bid vol)

| Contract | OI Δ | curr_oi | side read | premium |
|---|---|---|---|---|
| 50P 06/12 | **+29,735** | 31,336 | ASK 81% → bought | $2.60M |
| 71C 06/05 (0DTE) | +14,537 | 20,186 | bid-lean → sold/expired worthless | $0.27M |
| 55P 06/12 | +8,285 | 38,746 | ASK 85% → bought | $1.95M |
| 30P 06/12 | +7,505 | 8,448 | ASK 97% → bought (disaster hedge) | $0.04M |
| 64C 06/12 | +7,051 | 7,317 | ASK 95% → bought | $2.29M |
| 110C 09/15/28 | +4,018 | 16,370 | mid/cross (ask 59/bid 79) | $10.97M |
| 62C 06/05 (0DTE) | +3,588 | 5,623 | balanced | $1.57M |
| 110C 06/17/27 | +3,044 | 21,616 | ASK 99% → bought | $5.28M |
| 60P 06/12 | +2,298 | 3,748 | BID 76% → SOLD | $1.17M |
| 42P 08/21 | +2,002 | 2,900 | BID 99.9% → SOLD | $0.67M |

### Closing / roll activity

[OI:decrease_with_volume]: dominated by today's expiry rolling off (52P 06/05
−21,130; 80C 06/05 −11,227; 70C/75C/67C/81C 0DTE decreases). Non-expiry
closes are small: 80C 07/17 −1,301; 40P 06/18 −894; 48P 06/18 −649; 75C 06/18
−624. **No decreases in Jan-27 70C/100C/110C** — today's bid-side LEAP selling
(phase-1-flow.md §Sweeps) is not yet visible in OI (prints tonight/tomorrow).
[OI:position_rolls]: **0 rolls detected** (threshold 500, near-DTE ≤30).

### Smart positioning [OI:smart_positioning]

Inferred: bearish on the 50P/55P/30P builds (ask-side puts), bearish on 71C
0DTE (sold), bullish on 64C 06/12 + 110C 06/17/27 (ask-side calls), bullish on
60P 06/12 + 42P 08/21 (bid-side puts = sold). Net: **front-week bearish tilt,
back-month bullish tilt.**

### Pin risk / OPEX concentration

IREN absent from market-wide `pin-risk` top-25 (dte≤7, ≤5% distance) and
`opex-concentration` top-20 (≥40% concentration) [OI:pin_risk,
OI:opex_concentration] — no single-expiry pin dominance vs the rest of the
tape; consistent with OI spread across 06/12, 06/18 and Jan-27.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw oi biggest-increases --symbol IREN --top-n 20 --min-oi-change 500 --date 2026-06-05 --json` | 50P 06/12 oi_diff_plain=+29,735, prev_ask_volume=22,718 ← `.results[0]` | top-20 |
| `uw oi decrease-with-volume --symbol IREN --top-n 15 --min-volume 100 --date 2026-06-05 --json` | 52P 0DTE −21,130 ← `.results[0].oi_diff_plain` | top-15 |
| `uw oi smart-positioning --symbol IREN --top-n 20 --min-oi-change 500 --date 2026-06-05 --json` | inferred_direction per row ← `.results[:10]` | top-20 |
| `uw oi position-rolls --symbol IREN --threshold 500 --near-dte-max 30 --date 2026-06-05 --json` | n=0 ← `.results\|length` | 0 |
| `uw oi oi-by-strike --symbol IREN --top-n 10 --date 2026-06-05 --json` | 110: call_oi=155,304, role=call_wall_resistance ← `.results[0]` | 10 strikes |
| `uw oi oi-by-strike --symbol IREN --top-n 10 --dte-max 30 --date 2026-06-05 --json` | 50: put_oi=54,682, net_oi=−45,730 ← `.results[0]` | 10 strikes |
| `uw oi term-structure --symbol IREN --date 2026-06-05 --json` | 2027-01-15 pct_of_total_oi=19.67; 06/12 put_call_oi_ratio=3.431 ← `.term_structure[]` | 19 expiries |
| `uw oi pin-risk --top-n 25 --dte-max 7 --max-distance-pct 5 --date 2026-06-05 --json` | IREN absent ← ticker filter | top-25 |
| `uw oi opex-concentration --top-n 20 --min-concentration-pct 40 --date 2026-06-05 --json` | IREN absent ← ticker filter | top-20 |
| float normalization (fz, phase-0) | 29,735×100/324.15M = 0.92% | derived |

## Tool errors

(none — see DATA NOTE for a jq-path correction)

## DATA NOTE / CORRECTION

First `term-structure` read used `.results` and returned `n=0/null`; the
payload actually nests under **`.term_structure[]`** (top-level keys:
`expiry_count, source, symbol, term_structure, total_oi`). Re-read with the
correct path; all term-structure numbers above trace to `.term_structure[]`.
No values from the empty first read were used.

## Verdict for downstream phases

- **Positioning bias:** **Hedged-bearish front / structurally-bullish back.**
  Fresh front-week put walls (50P/55P/30P bought at ask) layered under spot;
  far-LEAP call builds (110C '27/'28) confirmed OPENING; premium sellers
  shorting 60P/42P against the panic. This is "protect the book, keep the
  upside" positioning, consistent with phase-1's profit-taking-not-exit read.
- **Conviction:** 3/5 (the 50P build is unambiguous and huge; direction split
  across tenors caps it).
- **Largest OI build as % of float:** 50P 06/12 +29,735 ≈ 2.97M share-equiv ≈
  **0.92% of float** (324.15M, fz) — structural for a one-week hedge; this is
  a real institutional protection trade, not retail noise [OI:oi_pct_float fz].
- **Three pin/cliff strikes for phase-9:**
  1. **50 (06/12 put wall, −8.1%)** — dealer-support shelf + the big hedge
     strike; first downside reference.
  2. **55 (put_heavy ATM battleground) / 56** — pin zone for 06/12 (phase-1's
     short strangle sits exactly here); break-and-hold above 55 negates the
     front-week put pressure.
  3. **60 (call wall, +10.3%) then 65 (+19.5%)** — near-term resistance
     stack; aligns with phase-2's 61.0–61.9 DP shelf (see phase-2-dark-pool.md
     §Price levels).
  Cliff: **2026-06-18 monthly OPEX (16.55% of OI)** is the near-term gravity
  date; structural cliff 2027-01-15 (19.67%).
- **Open questions:** Did today's Jan-27 call selling CLOSE existing OI (shows
  in 06/08 OI as decreases) or open covered/overwrites? Is the 50P build a
  fund hedging a long stock book (benign) or outright short delta (hostile)?
  Phase-4 GEX will say which way dealers are positioned around 50–55.
