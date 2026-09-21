# Phase 1 — Options Flow

**Ticker:** SNOW · **As-of:** 2026-05-29 · **Generated:** 2026-05-29
**Upstream:** phase-0.5-context.md (GENUINELY_UNUSUAL magnitude, but direction
split — on the net-bearish board despite huge call premium) · phase-0
(post-earnings T+2, +6.84%, $255.55)

## Summary

The headline is a trap: SNOW's **$232.6M call premium vs $28.3M put**
`[FLOW:insights_deep_dive]` looks wildly bullish, but the composition reads as
**post-earnings distribution and hedging, not fresh continuation buying.** The
gross call figure is inflated by **deep-ITM 0DTE calls** ($175/$182.5/$200C
expiring today, far below spot $255.55) — closing/exercise flow as the gap-up ran
through strikes — and the **single largest sweep of the entire tape is a $14.0M
*bid-side* 0DTE $185C (call SELLING)** `[FLOW:sweeps]`. The genuine *new*
positioning (vol≫OI) skews to **near-the-money puts** — 252.5P / 250P / 247.5P /
255P `[FLOW:unusual-volume]` — i.e. traders buying protection or fading the
+6.84% rip. This is exactly why phase-0.5 found SNOW on the **net-bearish board
(rank 38)** despite record call premium. There are real upside bets (June $300C,
Aug $250C, a 2027 $320C/$220P LEAP combo) but they are dwarfed by the ITM-closing
and put-hedging flow. Net: **mixed, leaning cautious** — the desk is taking
profits / hedging the post-earnings gap, not pressing it.

## Key signals

- **Largest sweep = $14.0M bid-side 0DTE $185C — call SELLING** `[FLOW:sweeps]`.
  Deep ITM, expiring today: closing winners / writing into the pop, not buying.
- **Gross call premium is ITM-0DTE-inflated** — top ask sweeps are $175/$182.5/
  $200C 0DTE (spot $255) `[FLOW:sweeps]`; these are exercise/close mechanics from
  the gap-up, not directional new longs. Discount the $232M headline.
- **New positioning skews to near-the-money PUTS** — 252.5P (voi 275), 247.5P
  (voi 87), 250P (voi 23), 255P (voi 56) `[FLOW:unusual-volume]` — hedging/fading
  the rip is the freshest directional intent.
- **Net bull/bear slightly bearish** — bullish $113.8M vs bearish $118.2M
  `[FLOW:insights_deep_dive]`; the call premium does NOT translate to net-bullish
  classification.
- **Some genuine upside tail bets** — June $300C (vol 2,337/OI 104), Aug $250C
  bid $3M, a 2027 $320C + $220P block combo `[FLOW:top-premium-trades]` — real
  but secondary to the hedging/closing flow.
- **No smart-money-flow campaign** — SNOW absent from `smart-money-flow` both
  directions `[FLOW:smart-money-flow]`.

## Detailed findings

### Whole-tape aggregate `[FLOW:insights_deep_dive]`
| Metric | Value |
|---|---|
| Call premium | $232.6M (ITM-0DTE-inflated) |
| Put premium | $28.3M |
| P/C ratio | 0.40 (call-tilted gross) |
| Bullish vs bearish premium | $113.8M vs $118.2M (**net slightly bearish**) |
| IV rank | 51.5 |
| Implied move (daily) | 0.55% (post-earnings IV crush) |
| Next earnings | 2026-08-26 (earnings just passed 2026-05-27) |

### Sweeps
- **Ask-side:** $175/$200/$182.5/$172.5/$180C 0DTE (deep ITM — closing), plus
  $200C June/Aug, $230C June, and a $230P 2027 LEAP ($1.46M).
- **Bid-side (selling):** $185C 0DTE **$14.0M** (largest), $180C July $6.4M,
  $185C June $5.9M, $200C June $4.0M, $250C Aug $3.0M — heavy call *supply*.
- Verdict: calls traded massively on BOTH sides; the bid-side selling +
  ITM-0DTE closing dominate — **not a clean ask-side bullish signature**.

### New positioning (vol ≫ OI)
Skewed to **puts at/just-under spot** (252.5/250/247.5/255 strikes, 0DTE & Jun-05)
= protection/fade of the gap. A handful of OTM upside calls ($300C Jun-12, $262.5C
Jun-05) and deep-OTM crash puts ($130/$160/$120P July).

### Largest premium prints
| Strike | Type | Expiry | Premium | Side | Read |
|---|---|---|---|---|---|
| 185 | call | 0DTE | $14.0M | **bid** | ITM call sold/closed |
| 180 | call | Jul-17 | $5.4M | bid | call sold |
| 200 | call | 0DTE | $4.3M | ask | ITM close (buy-to-cover?) |
| 320 | call | 2027 | $3.07M | block | LEAP upside (combo) |
| 220 | put | 2027 | $3.0M | block | LEAP downside (combo) |

### IV outliers + Greeks
IV rank 51.5; implied move only **0.55%/day** — post-earnings **IV crush** has
already deflated front vol (the event is behind us). Not a vol-event setup.

## Tool calls
| Tool | Args | Result |
|---|---|---|
| `options-flow sweeps` | ask/bid `--min-premium 250000` | calls both sides; $14M bid-side call sale |
| `options-flow unusual-volume` | `--min-vol-oi-ratio 3` | new positions skew puts |
| `options-flow top-premium-trades` | `--top-n 12` | ITM 0DTE call closing + LEAP combo |
| `hot-chains smart-money-flow` | bull/bear top-60 | SNOW absent |

## Tool errors
(none)

## Verdict for downstream

- **Net bias: MIXED, leaning CAUTIOUS** (post-earnings distribution/hedging). The
  gross call premium is ITM-0DTE/close-inflated; new directional intent is
  put-hedging the +6.84% gap, and the bull/bear net is slightly bearish.
- **Conviction: 2 / 5.** Magnitude is GENUINELY_UNUSUAL (phase-0.5, no cap) but
  the *direction* reads fade/consolidate, not continuation.
- **Three datapoints later phases must remember:**
  1. The $232M call premium is **misleading** — ITM-0DTE closing + a $14M
     bid-side call sale; net bull/bear is slightly *bearish*.
  2. Freshest new positioning = **near-the-money put buying** (hedging the gap).
  3. **Earnings already passed (5/27 beat)** — IV crushed, no near-term catalyst;
     any thesis is post-earnings drift, not event-driven.
- **Open questions:**
  - Is the dark pool (phase-2) accumulating the post-earnings level (institutions
    buying the breakout) or distributing into it? This resolves continuation-vs-fade.
  - Does dealer structure (phase-4) pin SNOW near $255, or is there a gamma
    breakout setup? The huge ITM call flow suggests heavy dealer hedging.
