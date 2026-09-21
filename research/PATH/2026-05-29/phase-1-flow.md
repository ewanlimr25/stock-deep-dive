# Phase 1 — Options Flow

**Ticker:** PATH · **As-of:** 2026-05-29 · **Generated:** 2026-05-29
**Upstream:** phase-0.5-context.md (`unusual_verdict=BUSY_NAME_NORMAL_DAY`,
sector software LEADING, self total-prem pctile 97.1) · phase-0-intake.md
(price $11.72, short float 31.15%)

## Summary

PATH's tape is **gross call-heavy but net near-balanced** — and the gross is
inflated by 0DTE pin/lottery strikes, exactly as phase-0.5 warned. Whole-tape
aggregate `[FLOW:insights_deep_dive]`: call premium **$9.47M** vs put **$2.29M**
(P/C ratio **0.35**), but the directional split is bullish $5.31M vs bearish
$5.08M — effectively flat with a faint bullish lean. The one genuinely
*directional* footprint is **LEAP call accumulation** — Jan-2028 $12/$10/$20/$17
calls bought on the ask — set against **near-dated June/Aug put buying**
(downside hedges) and some call *selling* on bids. Net read: a beaten-down,
heavily-shorted ($11.72, −41% from 52w high, +12.9% on the month, 31% short
float) software name attracting speculative long-dated upside bets into a
recovery, but with no clean, persistent, one-sided institutional campaign today.

## Key signals

- **LEAP call accumulation, ask-side** — Jan-2028 $12C (+$229K ask), $10C
  (+$196K ask), 2027 $20C (+$156K ask); a buyer paid $3.65 for the 2028 $12C
  (delta 0.65, IV 0.78) `[FLOW:top-premium-trades]`. Slow, institutional,
  long-horizon bullish — *not* short-term tradeable.
- **Near-dated put buying (downside hedge / bearish lean)** — June 12P/11P/10P/
  9.5P/9P and a cluster of Aug $11P prints opening (vol≫OI), e.g. June-05 12P
  vol 1,383 / OI 110 (voi 12.6), June-12 11P voi 7.4 `[FLOW:unusual-volume]`.
  Protection or tactical bearish bets under spot.
- **Call selling present** — the single largest sweep is a **bid-side** Aug $14C
  ($327K) and the largest top-premium print is a bid-side 2028 $12C; calls trade
  on *both* sides → no clean ask-side conviction `[FLOW:sweeps]`.
- **0DTE dominates the OI build** — top OI changes are all same-day 12C/12.5C/13C
  (`uw insights` top_oi_changes) — pin/lottery, discount per phase-0.5.
- **No smart-money flow, no multi-day campaign** — PATH absent from
  `smart-money-flow` (both directions, top-60) and `sweep-persistence` (5d)
  returned empty → today's heat is a one-day event, not a building campaign
  `[FLOW:smart-money-flow][FLOW:sweep-persistence]`.

## Detailed findings

### Whole-tape aggregate `[FLOW:insights_deep_dive]`
| Metric | Value |
|---|---|
| Call premium | $9.47M |
| Put premium | $2.29M |
| P/C ratio | 0.35 (call-tilted gross) |
| Bullish vs bearish premium | $5.31M vs $5.08M (≈ flat) |
| Call vol / Put vol | 191,734 / 66,363 |
| IV rank | 43.3 |
| Implied move (daily) | 1.63% |
| Next earnings | 2026-09-03 (no near-term catalyst) |

Read against the top-N: the call-heavy gross is **not** a clean directional tape.
Net bullish−bearish is essentially flat; the call premium is split between
ask-side LEAP buying and bid-side call selling, with 0DTE inflating volume.

### Sweeps (ask vs bid)
- **Ask-side (lifting offers):** all calls — 2028 $12C $229K, 0DTE $11.5C $202K,
  2028 $10C $196K, 2027 $20C $156K, June $12C $150K, Aug $14C $139K.
- **Bid-side (hitting bids):** also all calls — Aug $14C **$327K** (largest of
  either side), June $12C $213K, 2028 $12C $180K, 2028 $10C $169K.
- Verdict: calls heavily traded but on **both sides** — net call conviction is
  muddy, not the clean ask-side signature the bullish rubric requires.

### New positioning (vol ≫ OI)
Mix of fresh June/Aug **puts** (8.5–12 strikes, below/near spot) opening
alongside June 13.5C (vol 6,654 / OI 478). The put openings cluster under spot →
hedging or tactical downside, not the bullish side of the book.

### Largest premium prints (table)
| Time (ET) | Strike | Type | Expiry | Premium | Side | Note |
|---|---|---|---|---|---|---|
| 13:36 | 12 | call | 2028-01-21 | $96.7K | bid | LEAP, delta 0.65, sold |
| — | 12 | call | 2028-01-21 | — | ask | LEAP accumulation |
| — | 14 | call | 2026-07-17 | — | bid | call sold |
| — | 11 | put | 2026-08-21 | — | ask | downside (multiple prints) |

### IV outliers + Greeks
IV rank 43.3 — middling, not a vol-event setup. 30d IV ≈ 0.65 (high in absolute
terms for a low-priced name, normal post-de-rate software). No earnings until
Sep — IV is not catalyst-pumped.

## Tool calls
| Tool | Args | Result |
|---|---|---|
| `options-flow sweeps` | `--symbol PATH --side ask\|bid --min-premium 100000` | calls both sides |
| `options-flow unusual-volume` | `--min-vol-oi-ratio 3 --top-n 25` | mixed calls/puts, 0DTE-heavy |
| `options-flow top-premium-trades` | `--top-n 25` | LEAP calls + Aug puts |
| `insights deep-dive` | `--symbol PATH` | whole-tape aggregate |
| `hot-chains smart-money-flow` | bullish/bearish top-60 | PATH absent |
| `hot-chains sweep-persistence` | `--days 5 --symbol PATH` | empty (no campaign) |

## Tool errors
(none — `yahoo_fundamentals` returned HTTP 401 inside `insights deep-dive`, an
optional sub-field, not a UW error; price/perf sourced from `fz` instead.)

## Verdict for downstream

- **Net bias:** MIXED with a faint bullish lean. Gross call-heavy, net flat;
  directional conviction is LEAP-only (slow) plus offsetting near-term puts.
- **Conviction: 2 / 5** — high activity, low *directional* clarity. Phase-0.5
  caps phases 1–2 confluence at `+` (BUSY_NAME_NORMAL_DAY); this tape does not
  even reach the top of `+`.
- **Three datapoints later phases must remember:**
  1. P/C 0.35 / call prem $9.47M is **gross**; net bullish−bearish ≈ flat
     ($5.31M vs $5.08M). Do not read the call premium as a bullish signal.
  2. The only persistent directional intent is **2028 LEAP call accumulation**
     ($12/$10/$20C ask-side) — institutional, slow, *not* short-term.
  3. **No earnings until 2026-09-03** — any near-term thesis is technical /
     squeeze / momentum, not catalyst-driven.
- **Open questions for downstream:**
  - Is the dark pool (phase-2) confirming accumulation under $11.72, or is the
    LEAP call buying unsupported by tape? (31% short float makes the
    cover-vs-distribute question central.)
  - Does dealer positioning (phase-3/4) show a gamma squeeze setup that would
    make the call buying self-fulfilling?
