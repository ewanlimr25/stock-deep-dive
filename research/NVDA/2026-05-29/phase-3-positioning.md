# Phase 3 — Open Interest & Positioning

**Ticker:** NVDA
**As-of date:** 2026-05-29
**Generated:** 2026-05-30T13:40Z
**Upstream phases cited:** phase-0.5-context.md, phase-1-flow.md, phase-2-dark-pool.md

## Summary

OI changes are **near-balanced and, on the aggressor-inferred read, slightly
bearish** — they do *not* corroborate a clean bull case. `smart-positioning`
nets **bullish OI +82,762 vs bearish +92,138** (net −9,376, mildly bearish). The
biggest raw OI builds are slightly-OTM near-dated calls (225C +20,337, 217.5C
+18,483, both 7-DTE; plus 0DTE 215C/217.5C/220C), **but the model infers the two
largest 217.5C/215C builds as BEARISH** (net_ask_bid −17,164 / −12,815 = sold on
the bid → **call writing, not buying**). Genuinely bullish-inferred builds are
smaller (220C 0DTE +16,219 ask-side, 225C 7-DTE +20,337, 250C 112-DTE +5,582).
Meanwhile fresh **downside put building** appears at 95P/110P (7-DTE, deep OTM
crash hedges), 200P (49-DTE), and the decrease tape shows **upside calls being
closed** (225C −11,830, 230C, 232.5C). Float-normalized, even the largest build
(225C) is **0.0087% of float** — a rounding error on NVDA. Net: positioning is
two-sided with a bearish lean once aggressor side is applied, and it aligns with
the phase-2 distribution read far better than with the phase-1 call headline.
**Bias: mixed-to-slightly-bearish. Conviction 3/5.**

## Key signals

- [OI:smart-positioning] Net inferred OI: **bullish +82,762 vs bearish +92,138**
  → **net −9,376 (slightly bearish)**.
- [OI:smart-positioning] The two largest call builds are inferred **BEARISH**:
  217.5C 7-DTE +18,483 (**net_ask_bid −17,164**) and 215C 0DTE +17,220
  (net_ask_bid −12,815) — sold on the bid ⇒ **call writing / overwriting**, not
  bullish accumulation.
- [OI:biggest-increases] Largest raw builds (all near-dated, slightly OTM calls):
  **225C 7-DTE +20,337**, 217.5C 7-DTE +18,483, 215C 0DTE +17,220, 217.5C 0DTE
  +16,650, 220C 0DTE +16,219. Plus downside puts: **95P/110P 7-DTE +9,612/+8,159**
  (deep-OTM crash hedges), 200P 49-DTE +7,497.
- [OI:decrease-with-volume] **Upside calls being closed:** 225C 14-DTE **−11,830**,
  232.5C 0DTE −6,757, 230C 0DTE −4,153, 230C 20-DTE −2,294, 260C 28-DTE −2,134 —
  net unwinding of higher call strikes.
- [OI:oi_pct_float fz] Largest build (225C +20,337) = **0.0087% of the 23.27B
  float** (share-equiv). Every build is a float rounding-error — none structural.

## Detailed findings

### Largest OI increases (biggest-increases)

| type | strike | DTE | OI Δ | volume | avg px | vs spot |
|------|--------|-----|------|--------|--------|---------|
| call | 225 | 7 | +20,337 | 37,672 | 1.50 | OTM |
| call | 217.5 | 7 | +18,483 | 24,622 | 3.33 | OTM |
| call | 215 | 0 | +17,220 | 302,268 | 1.42 | OTM (0DTE) |
| call | 217.5 | 0 | +16,650 | 162,588 | 0.75 | OTM (0DTE) |
| call | 220 | 0 | +16,219 | 209,037 | 0.39 | OTM (0DTE) |
| put | 95 | 7 | +9,612 | 9,627 | 0.01 | deep-OTM hedge |
| put | 110 | 7 | +8,159 | 11,790 | 0.01 | deep-OTM hedge |
| call | 210 | 3 | +8,039 | 12,721 | 5.14 | ~ATM |
| put | 200 | 49 | +7,497 | 10,243 | 5.79 | OTM hedge |
| put | 197.5 | 0 | +5,871 | 13,690 | 0.06 | OTM (0DTE) |
| call | 250 | 112 | +5,582 | 10,588 | 9.04 | far-OTM |

The headline call builds are dominated by **0DTE expiry noise** (215/217.5/220C,
May-29) and two 7-DTE strikes (225C/217.5C). The 95P/110P 7-DTE penny builds
(avg px $0.01) are cheap tail/crash hedges — bearish-flavored but lottery-priced.

### Smart positioning (inferred direction)

| inferred | type | strike | DTE | OI Δ | net_ask_bid | read |
|----------|------|--------|-----|------|-------------|------|
| bullish | call | 225 | 7 | +20,337 | +3,115 | mild ask-side call buy |
| **bearish** | call | 217.5 | 7 | +18,483 | **−17,164** | **call writing (sold)** |
| **bearish** | call | 215 | 0 | +17,220 | **−12,815** | **call writing (sold)** |
| bullish | call | 217.5 | 0 | +16,650 | +916 | ~balanced |
| bullish | call | 220 | 0 | +16,219 | +18,944 | ask-side buy (0DTE) |
| bearish | put | 95 | 7 | +9,612 | +8,411 | crash hedge |
| bearish | call | 210 | 3 | +8,039 | −5,056 | ~ATM call sold |

The model's net is **slightly bearish (−9,376)**. The critical nuance vs phase-1:
the big 217.5C/215C builds that *look* bullish by raw OI are **inferred as sold
(written)**, consistent with the phase-2 distribution — institutions appear to be
**overwriting calls against stock they're selling**, the classic top-of-range
behavior, not buying upside.

### Closing / roll activity (decrease-with-volume)

Net **closing of upside calls**: 225C 14-DTE −11,830, 232.5C 0DTE −6,757, 230C
0DTE −4,153 / 20-DTE −2,294, 260C 28-DTE −2,134. The 0DTE decreases are expiry
settlement; the 14-DTE 225C −11,830 and 20-DTE 230C / 28-DTE 260C closings are
**genuine unwinding of higher-strike upside bets** — bearish at the margin (longs
ringing the register on the bounce, or rolled down). No clean near→far roll
signature detected.

### Pin risk / OPEX concentration

Not separately pulled as primary; nearest monthly OPEX is 2026-06-18 (>14 days
out as-of), so pin-risk would be empty/low-signal. The downside reference levels
come from phase-4's gamma surface and this phase's put builds (195 negative-gamma
strike, 200P 49-DTE build), NOT from a max-pain calculation — max pain was not
computed this run (no `uw options-structure` max-pain leaf exists).

### Map vs flow & dark pool

This phase **reconciles the phase-1/phase-2 tension toward the bearish side**:
phase-1's call-tilted headline is undercut here because the largest call builds
are *written* (sold), not bought — which fits phase-2's institutional
distribution (sell stock, write calls against it). The only unambiguously
bullish-inferred builds are small (220C 0DTE +18,944 ask, 225C 7-DTE +3,115).

## Tool calls (audit trail)

| Command | Result |
|---------|--------|
| `uw oi biggest-increases --symbol NVDA --date 2026-05-29 --top-n 20 --min-oi-change 500 --json` | 225C/217.5C/215C builds + 95P/110P hedges |
| `uw oi smart-positioning --symbol NVDA --date 2026-05-29 --top-n 20 --min-oi-change 500 --json` | net inferred −9,376 (slightly bearish); 217.5C/215C written |
| `uw oi decrease-with-volume --symbol NVDA --date 2026-05-29 --top-n 15 --min-volume 100 --json` | upside calls closing (225C −11,830) |

## Tool errors

(none — all three OI tools returned data. `oi-by-strike`/`term-structure`/
`gamma-exposure` are NOT valid `uw oi` leaves; the valid leaves are
biggest-increases / smart-positioning / decrease-with-volume / position-rolls /
pin-risk / opex-concentration.)

## Verdict for downstream phases

- **Bias from this phase:** MIXED-to-slightly-BEARISH (net inferred OI −9,376;
  big call builds are *written*, upside calls closing, downside puts opening).
- **Conviction:** 3/5.
- **Largest OI build as % of float:** 225C +20,337 = **0.0087% of float** —
  non-structural; this is short-dated speculative/hedging flow, not a position.
- **Three pin/cliff strikes for phase-9 reference:**
  1. **215–217.5** — heaviest 0DTE/7-DTE call OI, but *written* (resistance/cap).
  2. **225** — largest 7-DTE build (bull target) but 14-DTE OI being closed (cap).
  3. **200** — put-build strike (49-DTE) + phase-4 negative-gamma level (downside ref; not a max-pain figure).
- **Open questions:** Does dealer gamma (phase-4) confirm 215–220 as a written-call
  resistance cap? Is the 95P/110P tail-hedge buildup a sign of rising crash fear
  (phase-7c sentiment)?
