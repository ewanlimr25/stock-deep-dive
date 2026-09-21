# Phase 7 — UW Insights Confluence

**Ticker:** SMR
**As-of date:** 2026-06-16
**Generated:** 2026-06-17T12:09:26Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-5-historical.md

## Summary

UW's composite tools **agree with phases 1–2 and confirm a low-confidence bearish
read.** The conviction matrix classifies SMR **DIRECTIONAL_SHORT** ("Dark pool
selling + put buying — institutional bear bet") but at only **13.7% confidence**;
institutional-accumulation returns **DISTRIBUTION** (dark-pool sell >> buy);
price-vs-flow shows bearish flow and falling price **aligned (no reversal
divergence)**; and SMR is **absent from both bullish and bearish signal-confluence
lists** (score < 1 either way → not a cross-sectional confluence name, consistent
with phase-0.5's BUSY_NAME_NORMAL_DAY). The whole-tape aggregate is net-bearish
(net_flow −$159,229) on a call-heavy gross book. **Baseline for phase-9: bearish /
DIRECTIONAL_SHORT, low conviction.**

## Key signals

- **Conviction matrix = DIRECTIONAL_SHORT, 13.7% confidence:** "Dark pool selling +
  put buying — institutional bear bet" [INSIGHT:conviction_matrix].
- **Institutional = DISTRIBUTION:** buy_sell_ratio 0.384 (buy 535,114 / sell
  857,492), vwap $10.14 — "sell volume significantly exceeds buy volume"
  [INSIGHT:institutional_accumulation].
- **Price-vs-flow ALIGNED (no reversal):** flow bearish, net −$159,229, "Price and
  flow are aligned" [INSIGHT:price_vs_flow].
- **No signal confluence either direction:** SMR not in bullish or bearish lists at
  `--min-score 1` → no strong cross-sectional stack [INSIGHT:signal_confluence].
- **Whole-tape net-bearish on call-heavy book:** bull 1,825,992 / bear 1,985,221 →
  derived net_flow −159,229; P/C 0.2626; implied_move 5.68% [INSIGHT:deep_dive].

## Detailed findings

### Deep dive snapshot — [INSIGHT:deep_dive]

| Metric | Value |
|--------|-------|
| `bullish_premium` / `bearish_premium` | 1,825,992 / 1,985,221 |
| **derived `net_flow`** (bull − bear) | **−159,229 (net bearish)** |
| `call_premium` / `put_premium` | 3,144,320 / 1,542,990 |
| `put_call_ratio` | 0.2626 (call-heavy) |
| `implied_move` / `implied_move_perc` | 0.561 / **5.68%** (phase-9 N4) |
| `iv_rank` / `iv30d` | 26.68 / 92.2% |
| dark-pool premium / shares / trades | $14.12M / 1,392,606 / 80 (avg $10.18) |
| next earnings | 2026-08-06 (outside 30d) |

Reconciles with phase-1 aggregate and phase-0.5 `[CTX:]` (universe net-dir 8.1
pctile, BUSY_NAME_NORMAL_DAY).

### Signal confluence — [INSIGHT:signal_confluence]

SMR **absent from both** bearish and bullish lists at `--min-score 1` (score < 1).
Not a confluence-stack name in either direction — the bearish lean is real but
weak and not cross-sectionally reinforced.

### Conviction matrix — [INSIGHT:conviction_matrix]

`scenario=DIRECTIONAL_SHORT`, `confidence_pct=13.7`, thresholds bear 0.4 / bull
0.6. `dark_pool.buy_ratio=0.384` (= phase-2). `options_flow`: call_ask 17,932 vs
call_bid 22,004 (calls net **sold** on bid), put_ask 5,546 vs put_bid 5,102 (puts
~balanced). Verdict text: "Dark pool selling + put buying — institutional bear
bet." Low confidence is the headline caveat.

### Price vs flow — [INSIGHT:price_vs_flow]

`divergence=false` ("Price and flow are aligned"), `flow_direction=bearish`,
`net_premium_flow=−159,229`. **Period range = $9.12–$14.30** (this is the **30-day**
hi/lo — it reconciles the phase-6 web-article "52W range" confusion; the true 52W
is fz's $8.85–$57.42). No reversal signal → bearish flow confirms the downtrend.
(`price_end=0` / `price_change_pct=−100` are buggy fields — see Tool errors.)

### Analyst vs flow — [INSIGHT:analyst_vs_flow]

Returned **flow side only** (`flow_sentiment=bearish`, net −159,229) — **no analyst
consensus** (yfinance gap). External read from phase-6: **BofA Neutral, $12 PT** —
non-bullish, roughly aligned with the bearish-to-neutral flow. No clean Wall-St-vs-
flow conflict to resolve.

### Institutional accumulation — [INSIGHT:institutional_accumulation]

`signal=DISTRIBUTION`, buy 535,114 / sell 857,492 (ratio 0.384), total DP $14.12M,
vwap $10.14, avg $10.18. Top levels $9.89 ($2.61M) / $9.90 / $10.02 / $10.14 /
$10.08 — **matches phase-2 price-levels.** (`price_30d_change_pct=−100` is the same
buggy field.)

### Earnings play

**Skipped** — next earnings ~2026-08-06 is outside the 30-day window (phase-6).

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows |
|------------------|--------------------------|------|
| `uw insights deep-dive --symbol SMR --date 2026-06-16` | net_flow −159,229 ← `.uw_screener` | 1 |
| `uw insights signal-confluence --direction bearish\|bullish --min-score 1 --top-n 20` | SMR absent ← filter | top-20 ea |
| `uw insights conviction-matrix --symbol SMR --date …` | DIRECTIONAL_SHORT 13.7% ← `.scenario/.confidence_pct` | 1 |
| `uw insights price-vs-flow --symbol SMR --lookback-days 30` | divergence=false ← `.divergence` | 30d |
| `uw insights analyst-vs-flow --symbol SMR` | flow bearish; no analyst ← `.options_flow` | 1 |
| `uw insights institutional-accumulation --symbol SMR` | DISTRIBUTION 0.384 ← `.signal/.buy_sell_ratio` | 1 |

## Tool errors

- `price-vs-flow` and `institutional-accumulation` return **`price_end=0` /
  `price_change_pct=−100` / `price_30d_change_pct=−100`** — a **buggy field**
  (price_end clamped to 0 → spurious −100%). The real 30d move is +11.87→9.89
  (≈−16.8%, from phase-5). The −100% is **ignored**; all other fields parse and are
  used.
- `analyst-vs-flow` returned no analyst-consensus block (yfinance gap) — not fatal;
  used BofA Neutral $12 (phase-6) as the external analyst read.

## Cross-check vs phases 1–5

| UW insight | Phase agreement? | Notes |
|------------|------------------|-------|
| signal_confluence (absent both) | phases 0.5/1 **agree** | Not a confluence name; bearish lean is weak |
| conviction_matrix DIRECTIONAL_SHORT (13.7%) | phase-1 (bearish flow) **agrees** | Low confidence matches "capped at +" |
| institutional_accumulation DISTRIBUTION | phase-2 (DP buy_ratio 0.384) **agrees** | Identical numbers |
| price_vs_flow aligned (bearish) | phase-5 downtrend **agrees** | No reversal divergence |
| analyst_vs_flow (flow bearish) | phase-6 BofA Neutral **roughly agrees** | No Wall-St-vs-flow conflict |

**Fully internally consistent** — every composite tool corroborates the
bearish/distribution stack, all at *low* confidence. No phase contradicts.

## DATA NOTE / CORRECTION

The web "52W range $9.12–$14.30" (phase-6) is resolved here as the UW **30-day**
period hi/lo, not 52-week. True 52W = fz $8.85–$57.42 (phase-5). No conflict
remains; price levels in this blueprint use UW/`fz`.

## Verdict for downstream phases

- **UW composite bias:** **bearish / DIRECTIONAL_SHORT** (distribution + bearish
  flow + aligned price-flow).
- **Conviction:** **2/5** — the matrix's own confidence is **13.7%**; everything
  aligns but nothing is strong, and no signal-confluence stack.
- **Phase-9 treatment:** **this is the BASELINE — bearish but low-conviction.**
  Override only with specific contrary evidence; the strongest such evidence so far
  is the squeeze setup (18% short float, premium-buying regime, FOMC + Japan-pledge
  catalysts) that phases 7c/8b must weigh.
- **Open questions:** Do fundamentals (phase-7b) confirm the falling-knife or flag
  a value/cash floor? Is the short crowded/expensive enough (phase-7c) that the
  low-confidence short is asymmetric-risk into the 06-17 FOMC + Japan catalyst?
