# Phase 7 — UW Insights Confluence

**Ticker:** HOOD
**As-of date:** 2026-05-27
**Generated:** 2026-05-28T14:03:50Z
**Upstream phases cited:** phase-0.5-context.md, phase-1-flow.md, phase-2-dark-pool.md, phase-4-structure.md, phase-5-historical.md, phase-6-macro.md

## Summary

UW's composite instrumentation reads **nominally bullish** — signal-confluence
**5/6**, conviction-matrix **DIRECTIONAL_LONG**, institutional-accumulation
**ACCUMULATION**, price-vs-flow **bullish DIVERGENCE** — which, taken at face value,
is a strong stack. **But this is a textbook composite-over-count, and phases 1/2/4/6
supply specific contrary evidence that every contributing factor is weak or an
artifact.** The conviction-matrix's own **confidence is just 17.5%**; the "ACCUMULATION"
is the **closing-auction cluster** phase-2 dismantled (intraday DP was 40.8% above mid =
distributive); the "bullish_flow" is **+$1.07M net** with call-buying ≈ call-selling
(phase-1 aggressor split); "oi_building" is **two-sided premium-selling** (phase-3); and
the only unambiguously-valid factor, **low_iv_cheap_options**, is a *structure-selection*
input, not a direction. The composite even prints **volume_ratio 0.67** (below average) —
self-evidence of phase-0.5's `BUSY_NAME_NORMAL_DAY`. **Verdict: the UW baseline is
weak-bullish/score-5 on paper but MIXED on decomposition — phase-9 should treat the
nominal bullish stack as largely artifact and lean on phases 1/2/4/6.**

## Key signals

- signal-confluence **score 5/6** (bullish_flow, low_pcr, dp_accumulation, oi_building,
  low_iv_cheap_options) — but it also prints **volume_ratio 0.67** [INSIGHT:signal_confluence].
- conviction-matrix **DIRECTIONAL_LONG @ only 17.5% confidence**; DP buy_ratio 0.631
  (whole-day) just clears the 0.6 bull threshold [INSIGHT:conviction_matrix].
- institutional-accumulation **ACCUMULATION, buy/sell 1.71** — but its top level is
  **76.23 / $61.2M / 29 trades = the 16:00 ET closing cluster** [INSIGHT:institutional_accumulation].
- price-vs-flow **DIVERGENCE = true**: "price down 10.4%, flow bullish (+$1.07M)"
  [INSIGHT:price_vs_flow] — marginal bullish side, fights phase-4 short-γ + phase-6 macro.
- **No bearish confluence**; **earnings-play out-of-window** (HOOD ER 2026-07-29 > 30d).

## Detailed findings

### Deep-dive snapshot + whole-tape directional aggregates

From `uw insights deep-dive` `uw_screener` (carried from phase-0.5/1):
- call_premium **$42.55M** vs put_premium **$11.75M** (P/C 0.36); **bullish $24.11M vs
  bearish $23.04M → net +$1.07M**; IV rank 23.2; IV30d 0.588; implied_move **3.29% /
  $2.51**; total OI 1,846,299; dark-pool premium **$273.67M**. Reconciles exactly with
  phase-1 (the 3.6× call/put premium is *not* directional — phase-1 aggressor split).

### Signal confluence [INSIGHT:signal_confluence]

HOOD scores **5/6** bullish (rare/high per the rubric), factors: `bullish_flow`,
`low_pcr`, `dp_accumulation`, `oi_building`, `low_iv_cheap_options`; net_flow +$1.07M,
PCR 0.36, **volume_ratio 0.67**, IV rank 23.2. **Factor-by-factor reconciliation:**

| Factor | UW says | Decomposed reality | Verdict |
|--------|---------|--------------------|---------|
| bullish_flow | bullish | net +$1.07M trivial; call ask$17.6M≈bid$18.9M (ph-1) | **weak** |
| low_pcr | bullish | PCR 0.36 is sold-call-heavy, not buy (ph-1); z NORMAL (ph-5) | **artifact** |
| dp_accumulation | accum. | closing auction; intraday 40.8% abv mid (ph-2) | **artifact** |
| oi_building | bullish | two-sided premium-selling/range (ph-3) | **artifact** |
| low_iv_cheap_options | bullish | TRUE — IV %ile 15.6 (ph-5) | **valid (structure, not direction)** |

The score of 5 is **four correlated naive signals + one valid-but-non-directional**.
Treat as **≈1.5 effective**, not 5.

### Conviction matrix [INSIGHT:conviction_matrix]

scenario **DIRECTIONAL_LONG**, **confidence_pct 17.5%** (very low). dark_pool buy_ratio
0.631 (whole-day; > 0.6 bull threshold by a hair), options_flow call_ask 67,731 /
call_bid 56,676 / put_ask 17,797 / put_bid 29,873 (the same near-balanced split phase-1
flagged). The label is the optimistic read of marginal inputs; the 17.5% confidence is
the tool itself signaling "barely."

### Price vs flow [INSIGHT:price_vs_flow]

**DIVERGENCE = true**: price −10.39% over the window (period_high 93.32, low 69.93,
start 86.85 → end 77.83) while net flow is +$1.07M bullish. Classic bullish-flow /
falling-price divergence — but (a) the bullish side is **+$1.07M (trivial)** and (b)
per the heuristic it must be paired with phase-4: dealer regime is **short-γ below the
78 ceiling with vanna selling on falling IV**, which does **not** support the divergence
resolving up. Early/weak reversal hint at best; phase-6 macro (hawkish) argues the other
way.

### Analyst vs flow [INSIGHT:analyst_vs_flow]

Returned **options-flow side only** (flow_sentiment bullish, +$1.07M) — **no analyst
consensus populated** (yfinance analyst block empty). No Wall-Street-vs-trader
comparison available this run; defer the analyst read to phase-7b/7c.

### Institutional accumulation [INSIGHT:institutional_accumulation]

signal **"ACCUMULATION — dark pool buy volume significantly exceeds sell volume"**,
buy/sell **1.71** (buy 2,284,387 vs sell 1,335,889), vwap 75.59, price_30d −10.36%.
**Top level: 76.23 / $61.19M / 802,714 sh / 29 trades** — this is exactly the **16:00 ET
closing-auction cluster** (+ the double-counted mega) phase-2 isolated. So the
"ACCUMULATION" verdict is **built on closing-cross mechanics**; phase-2's intraday
decomposition (40.8% above mid → net offered) is the truer directional read. **This tool
DISAGREES with phase-2 and phase-2 is right.**

### Earnings play

HOOD **absent** at `--days-until-earnings 30` — ER 2026-07-29 is ~63 days out, **out of
window** (not an error). No pre-earnings IV/OI setup applies.

## Tool calls (audit trail)

| Command | Result summary |
|---------|----------------|
| `uw insights conviction-matrix --symbol HOOD --date 2026-05-27` | DIRECTIONAL_LONG, **17.5% conf** |
| `uw insights price-vs-flow --symbol HOOD --lookback-days 30` | DIVERGENCE true (px −10.4%, flow +$1.07M) |
| `uw insights analyst-vs-flow --symbol HOOD` | flow bullish; no analyst consensus returned |
| `uw insights institutional-accumulation --symbol HOOD` | ACCUMULATION 1.71 — top level = closing cluster |
| `uw insights signal-confluence --direction bullish --min-score 1 --top-n 50` | HOOD **score 5/6**, vol_ratio 0.67 |
| `uw insights signal-confluence --direction bearish --min-score 1 --top-n 50` | HOOD absent (no bearish confluence) |
| `uw insights earnings-play --days-until-earnings 30` | HOOD absent (out of window) |

## Tool errors

None. (analyst-vs-flow returned no analyst block — empty yfinance consensus, not an
error; deferred to 7b/7c.)

## Cross-check vs phases 1–5

| UW insight | Phase agreement? | Notes |
|------------|------------------|-------|
| signal_confluence (5/6 bullish) | **DISAGREES with ph-1/2/3/5** | 4 of 5 factors are artifact/weak on decomposition; only low_iv valid (non-directional) |
| conviction_matrix (DIRECTIONAL_LONG) | partial — agrees with ph-1's *slight* + but **17.5% conf**; ph-4 structure neutral-to-bearish | marginal label on marginal inputs |
| institutional_accumulation (ACCUMULATION) | **DISAGREES with ph-2** | tool uses whole-day DP incl. closing auction; ph-2 intraday = distribution. **Ph-2 correct.** |
| price_vs_flow (bullish divergence) | agrees flow is +; **ph-4 + ph-6 argue against resolving up** | early/weak reversal hint only |

## Verdict for downstream

- **UW composite bias (BASELINE):** **nominally bullish (confluence 5/6,
  DIRECTIONAL_LONG, ACCUMULATION, bullish divergence)** — but it is the *naive
  whole-tape* read and is **specifically contradicted** by phases 1 (balanced aggressor
  split), 2 (closing-auction artifact), 4 (short-γ cap + vanna selling), and 6 (hawkish
  macro headwind). On the merits, the real read is **MIXED / weak-bullish at low
  confidence.**
- **Conviction:** **2/5** in the bullish baseline (the composite over-counts; effective
  signal ≈1.5/6). The one durable takeaway is **low_iv / cheap options** — a structure
  input, not a direction.
- **Phase 9 guidance:** do **not** anchor on the 5/6 confluence or the ACCUMULATION
  label. Treat the nominal bullish stack as largely artifact; weight the decomposed
  evidence (balanced flow, distributive intraday DP, capped short-γ structure, hawkish
  macro). If anything is actionable long, it is *small, defined-risk, and cheap-IV-aware*,
  not a conviction directional long.
- **Open questions:**
  - Will phase-7b/7c (fundamentals + sentiment/SI) confirm the macro headwind and the
    crypto-revenue drag, or surface a fundamental floor that supports the bullish
    divergence?
  - The bullish divergence (flow up, price down) — does phase-8b's bear case explain it
    as trapped/wrong flow, or a genuine early-accumulation tell?
