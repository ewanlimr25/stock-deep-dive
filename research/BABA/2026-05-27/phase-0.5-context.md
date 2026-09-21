# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** BABA
**As-of date:** 2026-05-27
**Generated:** 2026-05-28T02:55:00Z
**Upstream phases cited:** phase-0-intake.md

## Summary

BABA's options tape today is **not genuinely unusual — it is a busy mega-cap
having a light, slightly-bearish day inside a clean two-week downtrend.**
Cross-sectionally BABA sits at the **97.3rd percentile of the ~6,100-name
optionable universe on total option premium** `[CTX:universe_pctile_total_prem
DUCKDB]` — but that is just its mega-cap baseline. Versus its *own* recent
history, today is a **bottom-6% premium session** (`self_pctile_total 6.3`,
$23.2M vs a $50–196M range earlier in May) `[CTX:self_pctile DUCKDB]`, and net
flow is **bottom-2% of the universe on net-directional premium** (structurally
net-put/sell-call heavy) yet only mid-low (40.6 pctile) for the name itself.
BABA does **not** appear on the bullish top-200 and ranks a modest **78/200 on
net-bearish premium** (net −$1.76M). Verdict: **BUSY_NAME_NORMAL_DAY** — phases
1–2 confluence is capped at `+` (not `++`) per `rubrics/confluence-scoring.md`.

## Universe ranking (BABA vs the tape, 2026-05-27)

| Metric | BABA | Read |
|--------|------|------|
| Net-bullish premium rank | **outside top-200** | not a directional buy leader `[CTX:universe_rank_net_dir]` |
| Net-bearish premium rank | **78 / 200** (net −$1.76M) | mild, mid-pack bearish lean |
| Universe pctile — total premium | **97.3** | mega-cap baseline, not a signal `[CTX:universe_pctile_total_prem DUCKDB]` |
| Universe pctile — net-directional | **1.6** | structurally net-put/sell-call heavy vs universe `[CTX:universe_pctile_net_dir DUCKDB]` |
| Universe pctile — IV rank | **20.1** | low-vol regime `[CTX:universe_pctile_iv DUCKDB]` |
| Universe pctile — vol-vs-avg | **93.3** (raw ratio ambiguous) | NOT in the ≥2x-volume screener → option volume *not* unusual vs its own 30-day; treat as inconclusive |

Today's directional **leaders** (single names, ETFs set aside): bullish — META
(+$61.7M), TSLA (+$54.8M), ASTS (+$32.5M), APP (+$29.1M), AAPL (+$17.4M); bearish
— **MU (−$124.3M), AMD (−$85.5M), NVDA (−$66.3M), SNDK, ARM** (semis sold hard).

## Sector read

BABA = Chinese-ADR Consumer Cyclical (e-commerce). The most relevant cross-read
is its closest US-listed peer **PDD, which ranks 13th on the net-bearish list
(−$21.5M)** today — Chinese e-commerce is seeing real bearish premium, not just
BABA. Broad tape is a **semis-down / mega-cap-tech-up** split (MU/AMD/NVDA sold;
META/AAPL/AMZN/GOOGL bid). BABA's own sub-group (China ADRs) is **lagging /
mixed-to-bearish** — a yellow flag for phase-6 to resolve against the macro
(China stimulus / tariff) backdrop. `[CTX:sector_leadership]`

## Self-history (BABA today vs its own 33 available sessions)

`sessions_in_window = 33` — **mind the gap** (`lib/duckdb-cuts.md §gap`): the local
window spans 2026-03-13→03-27 then 2026-04-27→05-27, a ~1-month hole, so these are
33 *available* sessions, not a contiguous calendar window.

- `self_pctile_net_dir`: **40.6** — today's net direction is mid-low for BABA
  (slightly below its own median; the name runs persistently net-bearish).
- `self_pctile_total`: **6.3** — today is a **very light premium day** for BABA.
- Trailing 12-session trail (DuckDB):

  | date | net_dir $M | tot_prem $M | px | iv_rank |
  |------|-----------|------------|-----|---------|
  | 05-27 | −1.76 | 23.2 | 127.76 | 21.2 |
  | 05-26 | −2.56 | 23.0 | 129.64 | 39.0 |
  | 05-22 | −0.79 | 48.5 | 130.00 | 29.9 |
  | 05-21 | −0.36 | 62.1 | 131.47 | 34.0 |
  | 05-20 | −4.05 | 23.9 | 134.47 | 40.8 |
  | 05-19 | +1.33 | 41.3 | 135.68 | 41.2 |
  | 05-18 | −4.75 | 39.6 | 133.26 | 42.8 |
  | 05-15 | −10.27 | 84.4 | 132.57 | 40.3 |
  | 05-14 | −10.87 | 115.0 | 141.12 | 49.2 |
  | 05-13 | **+14.23** | **196.3** | **145.81** | 83.0 |
  | 05-12 | −2.35 | 75.5 | 134.78 | 68.3 |
  | 05-11 | −6.54 | 55.9 | 137.30 | 63.4 |

  **Pattern:** BABA topped near $145.81 on 05-13 (the one big +net_dir / high-IV
  day) and has bled ~12% to $127.76 over two weeks with **persistently negative
  net_dir** and **IV rank collapsing 83 → 21** — an orderly, vol-down distribution,
  not a panic. `[CTX:self_history DUCKDB]`

## Source

CLI (`uw screener` ×3, `uw insights deep-dive`) **+ DuckDB escape hatch §C**
(exact universe + self-history percentiles; local snapshot for 2026-05-27 present).
"Outside top-200" recorded for net-bullish premium. vol-vs-average flagged
inconclusive (high percentile but absent from the ≥2x screener).

## Verdict for downstream

```
universe_pctile_total_prem:  97.3        # mega-cap baseline, NOT a signal
universe_rank_net_dir:       outside top-200 bullish / 78 of 200 bearish (net −$1.76M)
universe_pctile_net_dir:     1.6         # structurally net-put/sell-call heavy
sector_leadership:           CHINA-ADR / Consumer-Cyclical lagging (peer PDD −$21.5M, rank 13 bearish)
iv_rank:                     21.2        # low-vol regime
implied_move_pct:            2.16        # feeds phase-9 expected-move (N4)
self_pctile_net_dir:         40.6        # mid-low for the name
self_pctile_total:           6.3         # LIGHT premium day for BABA
unusual_verdict:             BUSY_NAME_NORMAL_DAY
```

- **Bias from this phase:** neutral (context only — sets no directional bias).
- **Three things later phases must remember:**
  1. Today is a **light, normal-to-quiet day** for BABA, not an unusual-flow
     event — cap phases 1–2 confluence at `+`, keep conviction calibrated.
  2. BABA is in a clean **~12% two-week downtrend ($146→$128) with IV crushed
     (83→21)** — phase-5/phase-9 must frame any long as a counter-trend / falling-
     knife and any short as trend-continuation into low vol.
  3. The **China-ADR peer group is lagging** (PDD −$21.5M bearish) — phase-6 must
     resolve the China macro (stimulus/tariff) backdrop before sizing.
- **Open questions:** Is the persistent negative net_dir real put-buying or
  call-selling (overwriting)? Phase-1/phase-4 must split gross call premium
  ($17.2M) from net-aggressive direction. Why is IV rank so low into a downtrend —
  complacency or genuine low realized vol? (phase-5).
