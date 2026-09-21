# Phase 7 — UW Insights Confluence

**Ticker:** GOOG
**As-of date:** 2026-06-22
**Generated:** 2026-06-22
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md (mega buy 0.764), phase-5-historical.md, phase-6-macro.md

## Summary

UW's own composite math returns a **decisively MIXED, no-directional-edge verdict** —
and it agrees with the run. GOOG appears in **neither the bullish nor the bearish
`signal-confluence` list** (low confluence both ways); the **`conviction-matrix` is
`MIXED` at just 6.2% confidence** (overall dark-pool buy_ratio 0.562, between the 0.4/0.6
thresholds); **`price-vs-flow` shows NO divergence** (bearish flow + falling price are
*aligned* — no reversal signal); and **`institutional-accumulation` reads `NEUTRAL —
balanced dark pool activity`**. That NEUTRAL is the important cross-check: it confirms
phase-2's accumulation was **narrow** (the mega-tier 0.764 was 14 trades; the *whole*
book is balanced at 0.562). The deep-dive snapshot is unchanged from phase-1 (net_flow
−$23.0M artifact, call:put 4:1, IV rank 39.8, implied move 2.63%). `analyst-vs-flow`
returned only the flow side (yfinance analyst consensus empty this run — deferred to
phase-7b/7c), and **GOOG did not qualify for `earnings-play`** despite the 7/22 date.
**Baseline for phase-9: low-conviction MIXED** — the constructive micro-signals do not
aggregate to a directional edge, and they sit under the phase-6 macro headwind.

## Key signals

- **`conviction-matrix` = MIXED, confidence 6.2%** (DP buy 0.562; calls lean sold,
  puts lean bought) `[INSIGHT:conviction_matrix]`
- **GOOG absent from BOTH bullish and bearish `signal-confluence`** lists → no
  directional confluence either way `[INSIGHT:signal_confluence]`
- **`institutional-accumulation` = NEUTRAL** (balanced DP) — tempers phase-2's narrow
  mega-tier accumulation `[INSIGHT:institutional_accumulation]`
- **`price-vs-flow` = no divergence**, flow bearish + price falling (aligned, no
  reversal) `[INSIGHT:price_vs_flow]`
- Deep-dive snapshot: net_flow **−$23.0M** (artifact), call/put **$335.6M/$83.6M**,
  P/C 0.388, IV rank 39.8, implied move **2.63%**, OI 1.60M, earnings 7/22
  `[INSIGHT:deep_dive]`

## Detailed findings

### Deep-dive snapshot `[INSIGHT:deep_dive]`

| Field | Value | (whole-tape; reconciles with phase-1 / phase-0.5) |
|-------|-------|---|
| bullish_premium / bearish_premium | $182.2M / $205.2M | net_flow **−$23.04M** (LEAP-roll artifact per phase-1) |
| call_premium / put_premium | $335.6M / $83.6M | 4.0:1 call-heavy |
| put_call_ratio | 0.388 | call-heavy by volume |
| iv_rank / iv30d | 39.78 / 32.76% | mid (phase-5: 85.7th 1-yr pctile) |
| implied_move / perc | $9.18 / **2.63%** | phase-9 N4 sizes to this |
| total_open_interest | 1,601,618 | OI building 30 sessions (phase-5) |
| next_earnings_date | 2026-07-22 | ~30 days out |

### Signal confluence `[INSIGHT:signal_confluence]`

GOOG is in **neither** the bullish (`--direction bullish --min-score 1`) **nor** the
bearish list — its directional confluence score is below the floor on both sides. No
multi-factor stack is firing either way. (Consistent with phases 1–4 being individually
mild and partly offsetting.)

### Conviction matrix `[INSIGHT:conviction_matrix]`

`scenario` = **MIXED**; `confidence_pct` = **6.2**. Components:
- `dark_pool`: buy_ratio **0.562** (buy 3.32M / sell 2.59M, 6,373 trades) — between the
  `bear 0.4` / `bull 0.6` thresholds → no DP bias.
- `options_flow`: call_bid 124,948 > call_ask 85,982 (calls lean **sold**); put_ask
  42,148 > put_bid 38,654 (puts lean **bought**) — a mild bearish aggressor lean.
- `explanation`: *"Balanced dark pool activity — no clear bias."*

Not DIRECTIONAL_LONG, not HEDGED_LONG, not DIRECTIONAL_SHORT — genuinely **MIXED**.

### Price vs flow `[INSIGHT:price_vs_flow]`

`divergence` = **false**; `flow_direction` = bearish. Bearish (net-aggressor) flow +
falling price = **aligned, no divergence → no reversal signal**. (Caveat: the "bearish"
flow is the phase-1 LEAP-roll artifact; the *absence* of a bullish-flow-vs-falling-price
divergence means there's no contrarian long trigger here.)

### Analyst vs flow `[INSIGHT:analyst_vs_flow]`

Returned **only the options_flow side** (net_flow −$23.0M, flow_sentiment bearish); the
**yfinance analyst consensus came back empty** this run (no rating/target). Deferred to
phase-7b (fz/Finnhub analyst cross-source) and phase-7c (revisions). No agreement read
possible from this tool today.

### Institutional accumulation `[INSIGHT:institutional_accumulation]`

`signal` = **"NEUTRAL — balanced dark pool activity."** The whole-book DP is balanced —
**this is the composite tempering phase-2**: the mega-tier 0.764 was a narrow, 14-trade
signal; aggregated across all tiers the institutional footprint is neutral, not
accumulation.

### Earnings play

**GOOG not in the `earnings-play` list** (`--days-until-earnings 30`). Earnings is 7/22
(≈30d) but the IV-rank + OI-buildup profile didn't flag a setup — consistent with the
fresh call OI expiring (6/26–7/10) *before* earnings, i.e. a pre-earnings bounce bet, not
an earnings-vol play (phase-6).

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← path | Rows |
|------------------|--------------------|------|
| `uw insights conviction-matrix --symbol GOOG --date 2026-06-22 --json` | scenario MIXED, confidence 6.2, DP buy 0.562 ← `.scenario`/`.confidence_pct` | 1 |
| `uw insights signal-confluence --direction bullish --min-score 1 --top-n 20 --json` | GOOG absent ← `index("GOOG")==null` | 20 |
| `uw insights signal-confluence --direction bearish --min-score 1 --top-n 20 --json` | GOOG absent | 20 |
| `uw insights price-vs-flow --symbol GOOG --lookback-days 30 --json` | divergence false, flow bearish ← `.divergence` | 1 |
| `uw insights institutional-accumulation --symbol GOOG --json` | "NEUTRAL — balanced dark pool" ← `.signal` | 1 |
| `uw insights analyst-vs-flow --symbol GOOG --json` | flow −23.0M; **analyst side empty** ← `.options_flow` | 1 |
| `uw insights earnings-play --days-until-earnings 30 --json` | GOOG absent | list |
| `uw insights deep-dive --symbol GOOG --date 2026-06-22 --json` (phase-1) | net_flow −23.0M, IV rank 39.78 ← `.uw_screener` | 1 |

## Tool errors

- `uw insights analyst-vs-flow` returned only `symbol` + `options_flow` (no analyst
  consensus block) — not an error, the yfinance analyst side was empty this run. Recorded;
  analyst data sourced in phase-7b/7c instead.

## Cross-check vs phases 1–5

| UW insight | Phase agreement? | Notes |
|------------|------------------|-------|
| signal_confluence (absent both) | **phases 1–4 AGREE** | Individually mild/offsetting → no aggregate directional confluence. Consistent. |
| conviction_matrix (MIXED, 6.2%) | **phase 1 AGREES** | Phase-1 read MIXED/mild-bullish; composite confirms no clean direction. |
| institutional_accumulation (NEUTRAL) | **phase 2 — partial** | Phase-2 mega 0.764 was narrow; whole-book 0.562 is neutral. Composite **tempers** phase-2's accumulation conviction. |
| price_vs_flow (no divergence) | **phase 5 AGREES** | Falling price + bearish-tagged flow aligned; no reversal trigger. |

## Verdict for downstream

- **UW composite bias:** **MIXED / NEUTRAL — no directional edge.** Both the
  confluence scorer and the conviction matrix decline to call a direction; DP is balanced
  whole-book; no price-vs-flow reversal.
- **Conviction:** **2 / 5** in any *directional* read (high confidence that the verdict
  itself is MIXED). The constructive micro-signals (narrow DP accumulation, upside call
  OI) are **real but sub-threshold** — they do not aggregate to an edge on UW's own math.
- **Phase 9 guidance:** treat **MIXED/low-conviction as the BASELINE**. Only override
  toward a directional trade with *specific* contrary evidence from phases 1–4/8 — and
  remember phase-5 (edge-neutral, IV rich) and phase-6 (macro HEADWIND) both push the
  same way. A high-conviction directional blueprint is **not** supported; if anything is
  actionable it is small, defined-risk, and tactical.
- **Open questions:** Does the fundamentals veto (phase-7b) confirm the capex/FCF/AI-moat
  damage from phase-6, turning "MIXED" into a fundamental *caution*? Does sentiment/
  positioning (phase-7c — short interest, revisions, the empty analyst consensus) add a
  downside gate? The debate (phase-8b) should test whether the narrow mega-tier DP buy is
  a credible bull foothold or noise inside a NEUTRAL book.
