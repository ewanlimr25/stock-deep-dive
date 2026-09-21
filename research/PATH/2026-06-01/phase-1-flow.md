# Phase 1 — Options Flow

**Ticker:** PATH (UiPath Inc.)
**As-of date:** 2026-06-01
**Generated:** 2026-06-01T20:11:00-04:00
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md

## Summary

PATH's tape is genuinely **two-sided**, not the clean bullish read its 100th-percentile
net number (phase-0.5) implied. By aggregate the day tilts mildly bullish — call
premium $14.0M vs put $3.54M, direction-aware net **+$2.18M** (bullish $8.63M − bearish
$6.45M), P/C 0.26 — but the single **largest, newest, most-aggressive print on the
whole tape is bearish**: a $2.31M at-the-money Sep-18 **$13 put**, volume 10,328 against
OI 372 (27.8× → a brand-new position), lifted ask-side. That one put is ~36% of the
day's entire bearish premium. The bullish counterweight is real but diffuse (ask-side
calls spread Jun→Jan-2028, plus deep-ITM $5/$5.5 stock-replacement calls), and the
5-day sweep campaign that flags PATH is explicitly `dominant_direction: "mixed"`. Net
read: **mixed, mild bullish lean, low directional conviction** — the flow looks more
like a long-with-protection / two-camp fight than one-way accumulation.

## Key signals

- Whole-tape net directional **+$2.18M** bullish, call-heavy P/C **0.259** (call vol
  151,351 vs put 39,188) [FLOW:insights_deep_dive]
- **Largest single conviction print is a bearish/protective ATM put:** Sep-18 $13 put,
  **$2.31M**, vol 10,328 / OI 372 = **27.8× (new)**, ask-side, delta −0.42 vega 0.028
  [FLOW:unusual_volume][FLOW:greek_screener]
- Top ask-side sweep is that **$13 Sep put for $1.29M** — biggest aggressor print of
  the day is to the downside [FLOW:sweeps ask]
- Bullish side is **diffuse**: ask-side call sweeps $12 '27 ($398K), $13 Jun-5 ($294K),
  $13 Jul-17 ($290K), $12 Jun-18 ($286K), $15 Aug-21 ($280K), $12 Jan-2028 LEAP ($217K)
  [FLOW:sweeps ask]
- **5-day persistence flags PATH** (sessions_in_top 5, $39.3M total sweep premium) but
  `dominant_direction: "mixed"` — a two-sided multi-day campaign [FLOW:sweep_persistence]

## Detailed findings

### Whole-tape aggregate (read the top-N against this) `[FLOW:insights_deep_dive]`

| Field | Value |
|-------|-------|
| call_premium | $14,008,670 |
| put_premium | $3,541,576 |
| bullish_premium | $8,630,001 |
| bearish_premium | $6,453,667 |
| **net_flow (derived = bull − bear)** | **+$2,176,334** (mild bullish) |
| call_volume / put_volume | 151,351 / 39,188 |
| put_call_ratio | 0.259 (call-heavy) |
| iv_rank / iv30d | 53.3 / 72.3% |
| implied_move_perc | 6.32% |

Critical nuance: call **premium** ($14M) dwarfs put premium, but direction-aware
**bullish** premium ($8.63M) only modestly beats bearish ($6.45M). So much of the call
premium is not aggressively bullish (sold calls / two-way), and a single ATM put
($2.31M) supplies a third of the bearish side. The tape is far more balanced than the
raw call/put premium split suggests.

### Sweeps (ask vs bid) `[FLOW:sweeps]`

- **Ask-side (aggressor = buyer):** 24 prints, $5.63M total. Top print is **bearish**:
  $13 Sep-18 **put $1,287,710**. Remainder are calls across the curve: $12 '27 $398K,
  $13 Jun-5 $294K, $13 Jul-17 $290K, $12 Jun-18 $286K, $15 Aug-21 $280K, $15 '27 $247K,
  $12 Jan-2028 $217K, $15 Dec-18 $212K, $5 Jun-5 $200K (deep-ITM).
- **Bid-side:** 13 prints, $2.70M total. Again topped by the **$13 Sep-18 put $845K**
  (so that put traded heavily on both sides — net ask-skew = put accumulation), then
  bid-side calls ($15 '27 $215K, $5 Jun-5 $199K, $13 Jun-5 $186K).
- Read: the marquee aggressive flow is the ATM Sep put (bought, ~$1.3M ask vs $0.85M
  bid → net buyer). Call buying is broad but no single call rivals that put's size.

### New positioning (unusual vol, vol/OI ≥ 3) `[FLOW:unusual_volume]`

| Type | Strike | Expiry | vol/OI | Vol | OI | Premium |
|------|-------|--------|--------|-----|-----|---------|
| **put** | **13** | **2026-09-18** | **27.8** | **10,328** | 372 | **$2,311,083** |
| put | 12.5 | 2026-06-05 | 66.1 | 3,898 | 59 | $133,017 |
| call | 5 | 2026-06-05 | 4.85 | 504 | 104 | $398,590 (deep-ITM) |
| call | 14 | 2026-06-12 | 4.57 | 1,610 | 352 | $60,929 |
| call | 5.5 | 2026-06-05 | 167 | 501 | 3 | $371,476 (deep-ITM) |

The dominant **new** position by premium is unambiguously the ATM Sep $13 put. The
other large "new" prints are deep-ITM ultra-short $5/$5.5 calls (delta ~0.97–0.99 →
stock substitutes / assignment mechanics, not directional conviction).

### Largest premium prints `[FLOW:top_premium_trades]`

Top-25 single trades: call $1.62M vs put $431K. Largest: $5 Jun-5 call $197K (ask,
delta 0.97 — ITM), $5.5 Jun-5 call $185K (mid), **$13 Sep-18 put $127K (ask)**, $10
Jun-5 call $109K (mid), **$13 Sep-18 put $93.5K (ask)**. The Sep $13 put recurs as the
only repeated large directional name.

### IV outliers + Greeks `[FLOW:iv_outliers][FLOW:greek_screener]`

- IV-outlier list is entirely **deep-ITM ultra-short calls** ($5/$5.5/$7/$10 Jun-5)
  showing IV 130–630% — pricing artifacts of deep-ITM near-expiry, **not signal**.
  Discard (pitfall: deep-ITM/0DTE noise).
- Greeks: the only meaningful vega/gamma sits in the **$13 Sep put** (δ −0.42, γ 0.070,
  ν 0.028) and longer-dated calls ($15 Dec δ 0.51, $12 '27 δ 0.67). The ITM Jun calls
  are δ≈0.97–0.99 stock-equivalents.

### Persistence & market-wide context

- `sweep-persistence --days 5`: **PATH present** — consistency_score 1, sessions_in_top
  5, total_sweep_premium **$39.26M**, but `dominant_direction: **mixed**`
  [FLOW:sweep_persistence]. A real multi-day campaign, but two-sided.
- `smart-money-flow` (bullish & bearish, market-wide): **PATH absent** from both top-10s
  → no market-scale smart-money signal on this date (consistent with small absolute $).
- `sweep-ratio` (≥0.3, market-wide top-15): PATH absent.

## Tool calls (audit trail)

| Command | Key value(s) ← `jq` path | Rows |
|---------|--------------------------|------|
| `insights deep-dive --symbol PATH --date 2026-06-01` | net=+2.18M ← `.uw_screener.bullish_premium-.bearish_premium`; P/C 0.259 ← `.uw_screener.put_call_ratio` | whole-tape |
| `options-flow sweeps --side ask --min-premium 100000` | top print $13 Sep put $1.29M ← `.results[0]` (sorted) | top-24 |
| `options-flow sweeps --side bid` | $13 Sep put $845K ← `.results[0]` | top-13 |
| `options-flow unusual-volume --min-vol-oi-ratio 3` | $13 Sep put voi 27.8, $2.31M ← `.results[]` | top-13 |
| `options-flow top-premium-trades --top-n 25` | call $1.62M / put $431K ← `.results|map(...)` | top-25 |
| `options-flow iv-outliers` / `greek-screener` | deep-ITM IV artifacts; put δ −0.42 ← `.results[].delta` | top-15 |
| `hot-chains sweep-persistence --days 5 --symbol PATH` | dominant_direction "mixed", $39.3M ← `.results[0]` | 1 |
| `hot-chains smart-money-flow bull/bear`, `sweep-ratio` | PATH absent ← `.results[]|select(...)` | market-wide |

## Tool errors

<none — all reads parsed clean through `jq`>

## Verdict for downstream phases

- **Net bias:** **mixed**, mild bullish lean on aggregate net premium (+$2.18M), but
  materially offset by the day's single biggest conviction print being a bearish/
  protective ATM Sep $13 put.
- **Conviction:** **2/5** — the tape is genuinely two-sided; no clean one-way signal.
  (Phase-0.5 said GENUINELY_UNUSUAL by magnitude, but composition is mixed → do not
  let later phases inflate this to a directional ++.)
- **Three things later phases must remember:**
  1. Net directional only +$2.18M despite $14M call premium — most call premium is not
     aggressively bullish; the day is near-balanced direction-aware.
  2. The **$2.31M new ATM Sep-18 $13 put** (vol 10,328/OI 372) is the dominant single
     position — bearish bet **or** protective hedge on accumulated long stock. Resolving
     which is the central question for phase 2 (dark pool) and phase 3 (OI).
  3. 5-day sweep campaign is real but `mixed`; deep-ITM $5/$5.5 calls are stock-
     replacement noise, not conviction — strip them when judging direction.
- **Open questions:** Is the Sep $13 put a hedge against dark-pool accumulation
  (→ phase-2) or a standalone short thesis? On a 31%-short-float name (phase-0), is the
  ITM/LEAP call buying squeeze-positioning or just delta-1 substitution?
