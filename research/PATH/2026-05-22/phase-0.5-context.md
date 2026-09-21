# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** PATH (UiPath Inc.)
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T00:00:00Z
**Upstream phases cited:** phase-0-intake.md

## Summary

PATH's options activity is **elevated but event-driven, not directional**. It sits in
the **93rd percentile of the optionable universe by total premium** and **96th
percentile by IV rank** — yet its **net-directional premium is the bottom 4% of the
universe** (a mild *bearish* tilt) and option volume is only **1.2× its own 30-day
average**. The driver is the **2026-05-28 earnings report (6 days out)**: IV30d ≈ 99%,
IV rank 84, implied move ≈ 11.8%. So the premium is large because options are
*expensive* (earnings vol ramp), not because conviction money is piling in directionally.
**Correction to phase-0:** PATH trades ≈ **$10.95** (dark-pool avg), not $17 — the
2026-05-29 $17 call flagged at intake is a deep-OTM (+55%) earnings lottery, not a
spot-level signal. Verdict: **BUSY_NAME_NORMAL_DAY (event-driven)** — downstream
conviction must be calibrated to *earnings vol*, not to a directional flow signal.

## Key signals

- Universe percentile (all optionable names, today): **total premium 93.2, IV rank 95.7,
  net-direction 3.9, volume-vs-avg 84.9** [CTX:universe_pctile DUCKDB]
- Net-directional premium **−$398,934** today (call premium $3.42M vs put premium
  $1.54M, but bearish_premium $2.05M > bullish_premium $1.65M) [CTX:net_flow]
- IV30d **98.7%**, IV rank **84.0**, implied move **≈11.8%**, earnings **2026-05-28**
  [CTX:implied_move_pct] · [CTX:iv_rank]
- Spot ≈ **$10.95** (dark-pool avg price) — reconciles the $8.5–$11.5 OI-change strikes,
  not the $17 lottery call [CTX:spot]
- Self-history (31 sessions): today's net-direction is only the **23rd percentile** of
  PATH's own recent range (bottom quartile = relatively bearish *for the name*), while
  total premium is 80th and IV rank 93rd pctile [CTX:self_pctile DUCKDB]

## Detailed findings

### Universe ranking (single-name read, ETFs set aside)

PATH is **outside the top 50** on both `screener_bullish_bearish` directions:
- Net-bullish leaders (single names): AAPL (+$81M), TSLA (+$53M), DELL (+$33M),
  IBM (+$33M), ASTS (+$28M), RKLB (+$27M), ADBE (+$23M). PATH not present.
- Net-bearish leaders: MSTR (−$121M), NVDA (−$97M), SNDK (−$48M), GOOGL (−$36M),
  SMH (−$33M), META (−$23M). PATH not present (its −$0.4M net is far too small to rank).

The exact DuckDB percentile resolves what "outside top-50" hides: PATH's total premium
is genuinely top-decile (93.2) — it's an *active* options name today — but its
**net-directional premium ranks in the bottom 4% (pctile 3.9)** of the universe, i.e.
among the more net-bearish-tilted names by premium. Volume-vs-avg pctile 84.9 looks high
only because most names trade below their average; the raw multiple is just **1.2×**.

### Sector read

PATH is **Technology / application software** (RPA + agentic automation). Today's tape:
- **Software sub-sector mildly bid:** IGV (software ETF) net-bullish **+$16.2M**
  (rank ~12), ADBE +$23M, NOW +$13M, PANW +$13M, INTU +$7.9M, MDB net-bearish −$2.6M.
- **Semis being sold:** SMH −$33M, NVDA −$97M, AMD −$8.8M, AVGO −$7.5M, SOXX put-heavy.
- Read: the *application-software* pocket PATH lives in is **in mild favour**, semis are
  out of favour. This is a faint sector tailwind, but PATH itself is **not** participating
  as a leader — it's idling into its own event. Hands phase-6 a starting point: software
  ≠ semis today.

### Self-history (DuckDB §C, N=31 sessions, gap-aware)

`sessions_in_window = 31` spanning 2026-03-13→05-22 with the known 03-28→04-24 hole — so
this is 31 *available* sessions, not a contiguous calendar window.
- **self_pctile_net_dir 23.3** — today's directional premium is in the bottom quartile of
  the name's own recent range. The last two sessions (05-21 −$185K, 05-22 −$399K) both
  printed net-bearish; the bullish impulse of 05-14/05-15 (+$559K / +$1.13M) has faded.
- **self_pctile_total 80.0** + **self_pctile_iv_rank 93.3** — premium and IV are near
  their own recent highs: the classic pre-earnings vol build, confirming the event read.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__insights_deep_dive` | `{symbol: PATH, date: 2026-05-22}` | IV rank 84, iv30d 98.7%, implied move 11.8%, earnings 2026-05-28, net premium −$399K, DP avg $10.95 |
| `mcp__uw-pp__screener_bullish_bearish` | `{direction: bullish, top_n: 50}` | PATH outside top-50; leaders AAPL/TSLA/DELL/IBM |
| `mcp__uw-pp__screener_bullish_bearish` | `{direction: bearish, top_n: 50}` | PATH outside top-50; leaders MSTR/NVDA/SNDK |
| `mcp__uw-pp__screener_volume_vs_average` | `{min_volume_ratio: 2, top_n: 50}` | PATH outside top-50 (micro-cap names dominate ratio list) |
| `mcp__uw-pp__screener_iv_rank` | `{mode: high, top_n: 50}` | PATH outside top-50 (list is the iv_rank=100 club; PATH = 84) |
| DuckDB §C | universe + self-history percentiles | universe: tot 93.2 / net_dir 3.9 / iv 95.7 / vol 84.9; self: net_dir 23.3 / tot 80.0 / iv 93.3 / N=31 |

## Tool errors

`yahoo_fundamentals` inside `insights_deep_dive` returned `HTTP 401` (yfinance auth) —
non-fatal; fundamentals are covered by phase-7b (Finnhub). No UW tool errored.

## Verdict for downstream

```
universe_pctile_total_prem:  93.2
universe_rank_net_dir:       outside top-50 (universe pctile 3.9 — net-bearish-tilted)
sector_leadership:           application-software mildly LEADING (IGV +$16M); semis lagging; PATH itself outside top-50
iv_rank:                     84.0
implied_move_pct:            ~11.8%   (earnings 2026-05-28, 6 days out)
self_pctile_net_dir:         23.3     (bottom quartile for the name — mild bearish tilt)
unusual_verdict:             BUSY_NAME_NORMAL_DAY   (event-driven pre-earnings IV ramp, NOT directional conviction)
```

- **Bias from this phase:** neutral (context only — sets no directional bias by design).
- **Conviction:** n/a (context phase).
- **Three things later phases should remember:**
  1. **The catalyst is everything.** Earnings 2026-05-28 (between as-of and the typical
     1-month horizon). Any blueprint is fundamentally an *event* trade — size and
     structure must respect the ~11.8% implied move. Phases 1–2 confluence is **capped at
     `+` (not `++`)** per the BUSY_NAME_NORMAL_DAY rule (`rubrics/confluence-scoring.md`).
  2. **Premium is high because of IV, not volume.** Volume is only 1.2× average; the
     top-decile premium rank is an IV artifact. Don't read "high premium" as accumulation.
  3. **Directional tilt is weak-bearish, and fading.** Net-direction bottom-4% of
     universe, bottom-quartile for the name, last two sessions net-negative. Spot ≈ $11.
- **Open questions:** Is the put-premium tilt protective hedging into earnings or genuine
  bearish positioning? (phase-1 aggressor split + phase-3 OI to resolve.) What does the
  Street expect from the 05-28 print? (phase-7b/7c.)
