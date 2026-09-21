# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** RKT
**As-of date:** 2026-07-17
**Generated:** 2026-07-19T19:20:00-04:00
**Upstream phases cited:** phase-0-intake.md

## Summary

RKT is a **perennially-active options name having a below-average day by its own
standards, while sitting at a genuine cross-sectional bearish extreme.** Total
premium ($2.17M) ranks 91.7th pctile and total volume 96.9th pctile across the
6,298-name universe — but those numbers reflect RKT's chronic activity, not a
spike: today's premium is only the **16th self-percentile** and volume the **20th
self-percentile** versus RKT's own last 25 sessions (call volume 23,879 vs its own
30-day avg 43,885 = 0.54×). Directionally, however, RKT's net-directional premium
(−$364,914) sits at the **4.1 universe percentile** (259th-most-bearish single name
of 6,298), and its sector — **Financial Services — is the single most net-bearish
sector on the tape today (−$57.2M)**. So the bearish tilt is cross-sectionally
coherent (weak name inside a sold sector), but today's *magnitude* is unremarkable
for RKT. **Verdict: BUSY_NAME_NORMAL_DAY** → phases 1–2 confluence capped at `+`.

## Universe ranking (6,298 names)

| Metric (as-of 2026-07-17) | RKT value | Universe pctile / rank |
|---|---|---|
| Total premium (call+put) | $2,168,923 | **91.7 pctile** |
| Total volume (call+put contracts) | 35,863 | **96.9 pctile** |
| Net-directional premium (bull−bear) | **−$364,914** | **4.1 pctile** · rank 6,040/6,298 (i.e. 259th-most-bearish) |
| Net-delta flow (net_call+net_put prem) | −$97,736 | 7.2 pctile |
| IV rank | 51.7 | mid |

- Directional **leaders** today are all index/semis, not comparables: net-bullish =
  SPX, NDX, SPXW, **NVDA (+$81.6M)**, CDNS, GLD; net-bearish = SPY, QQQ, **SMH,
  SLV, MU, SOXX**. RKT is nowhere near the single-name directional leaders in size —
  it's simply on the bearish side of a broad, index/semis-driven tape.

## Sector read

Financial Services net-directional premium = **−$57.2M**, the **most net-bearish of
all 11 sectors** today (n=557 names). The bullish end was Technology (+$98.6M),
Energy (+$30.1M), Communication Services (+$29.7M). **RKT is a bearish-flow name
inside the tape's most-sold sector** → this is the *coherent* configuration (name
weak + sector weak), not the yellow-flag divergence. Hands phase-6 a head start:
Financials/rate-sensitive mortgage names are out of favour today.

## Self-history (25 sessions, 2026-06-11 → 2026-07-17; local parquet present)

| Metric | Today | Self-pctile |
|---|---|---|
| Total premium | $2,168,923 | **16** |
| Net-directional premium | −$364,914 | 36 |
| Net-delta flow | −$97,736 | 52 |
| Total volume | 35,863 | **20** |

**Trend context (this is where the signal lives, not in today's single print):**
the last five sessions show persistent, escalating bearish net-directional flow —
07-14 +$24k → **07-15 −$1.46M → 07-16 −$3.02M** (vol 107,438, net-delta −$3.70M) →
07-17 −$0.36M. Price path: peaked $15.85 (07-01), troughed $13.91 (07-13), bounced
to $14.90 (07-16), closed **$14.54 (07-17, −2.4% on the day)**. The standout is
**07-16: ~$3M net-bearish premium into a price *rise* to $14.90** — bearish flow
sold into strength, and price rolled the next session. Today merely continues that
bearish lean at smaller size.

## Source

CLI + **DuckDB escape hatch** (`lib/duckdb-cuts.md §C`): exact universe percentiles
(N=6,298) and 25-session self-history computed from
`~/Documents/Stocks/Stock Screener/stock-screener-*.parquet`. Yahoo price block in
`insights deep-dive` returned HTTP 401 (paid) → spot/close sourced from the screener
parquet (`close=14.54`) instead. No "outside top-N" metrics — RKT is inside every
ranking. IV rank / earnings date from `uw_screener` block.

## Verdict for downstream — `[CTX:]` block

```
universe_pctile_total_prem:  91.7
universe_rank_net_dir:       6040 of 6298   # bearish end; = 259th-most-bearish name
sector_leadership:           Financial Services LEADING BEARISH (−$57.2M, most-sold sector)
iv_rank:                     51.7
implied_move_pct:            0.63%           # implied_move_perc from uw_screener (1-day)
self_pctile_net_dir:         36
unusual_verdict:             BUSY_NAME_NORMAL_DAY
```

Interpretation notes for later phases:
- **Confluence cap:** BUSY_NAME_NORMAL_DAY → phases 1–2 confluence capped at `+`
  (not `++`) per `rubrics/confluence-scoring.md`. Today's magnitude is below RKT's
  own median even though cross-sectional pctiles look large.
- **Directional prior is bearish but low-conviction on today alone** — the durable
  signal is the multi-day bearish escalation (07-15/07-16), not the 07-17 print.
- **Earnings 2026-07-30 (~9 trading days out)** — any swing structure must price the
  event; the persistent bearish flow may be positioning into that print.
- **Dual-class scale note (from phase-0):** UW screener marketcap = $14.6B (Class-A
  public float, ~1.0B shares at $14.54); fz all-class Market Cap = $41.14B. Use the
  $14.6B tradeable-float figure for liquidity/positioning; the $41B for enterprise scale.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← path | Rows used |
|---|---|---|
| `uw insights deep-dive --symbol RKT --date 2026-07-17 --json` | bull_prem 758,711 / bear_prem 1,123,625 / net_call_prem −231,325 / net_put_prem +133,589 / iv_rank 51.7 / earnings 2026-07-30 ← `.uw_screener` | 1 |
| DuckDB §C on `stock-screener-2026-07-17.parquet` | universe N=6,298; RKT total_prem pctile 91.7, net_dir pctile 4.1, vol pctile 96.9 | full universe |
| DuckDB self-history, 25× `stock-screener-*.parquet` | today premium self-pctile 16, vol self-pctile 20, net_dir self-pctile 36; close 14.54 | 25 sessions |
| DuckDB sector aggregate | Financial Services net-dir −$57.2M (most bearish of 11) | 6,298 rows grouped |

## Tool errors

`uw insights deep-dive` → `yahoo_fundamentals: {"error":"yahoo quoteSummary RKT:
HTTP 401"}` (paid endpoint). Non-fatal per orchestration rule 4 — spot/close sourced
from the screener parquet instead (`close=14.54`, `prev_close=14.90`). All other reads
round-tripped through `jq`/DuckDB.

## DATA NOTE / CORRECTION

Universe/self percentiles use the DuckDB escape hatch because the CLI returns only
ranked top-N, not exact percentiles or a self-history series — tagged `[… DUCKDB]`
downstream. High universe pctiles (91.7/96.9) were NOT read as "unusual": the
self-history (16/20) corrects that to a below-average day for the name — recorded
explicitly so phases 1–2 don't over-weight the cross-sectional magnitude.

## Verdict for downstream phases

- **Bias from this phase:** context only (no bias set) — but flags a **coherent
  bearish cross-sectional configuration** for phases 1/6/9 to weigh.
- **Conviction:** n/a (context)
- **Three things later phases should remember:**
  1. **BUSY_NAME_NORMAL_DAY** — cap phase 1–2 confluence at `+`; today is below
     RKT's own median activity despite top-decile universe pctiles.
  2. **Bearish is the coherent read** — RKT net-dir at 4.1 universe pctile *and*
     Financial Services is the most-sold sector; multi-day flow escalated bearish
     (07-16 −$3.0M into strength). Not a divergence — a confirmation.
  3. **Earnings 2026-07-30** and **IV rank 51.7** (mid) — event risk ~9 sessions
     out; not a cheap- or rich-vol extreme.
- **Open questions:** does the detailed flow (phase 1) show the bearish premium as
  aggressive put-buying / call-selling vs. hedging? Is the dark pool (phase 2)
  accumulating into this weakness or confirming distribution? Resolve before sizing.
