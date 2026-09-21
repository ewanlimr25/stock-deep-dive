# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** ENPH
**As-of date:** 2026-05-22
**Generated:** 2026-05-25T22:43:20Z
**Upstream phases cited:** phase-0-intake.md

## Summary

ENPH's flow today is **genuinely unusual on the directional axis** — not a busy
name having a normal day. Across the full optionable universe (4,532 names) it sits
in the **99.5th percentile on net-directional premium** (≈ rank 23, top-25 directional
name on the whole tape), 97.8th on total premium, and 97.1st on IV rank. Against its
own ≤31-session history it is 93.3rd percentile on net-direction and 90th on total
premium. Critically the bullish skew is **persistent, not a spike**: net-directional
premium has been positive ~5 of the last 6 sessions ($5.55M today, +7.45M on 5/21,
+5.35M on 5/20, +5.55M on 5/15) — sustained call-side accumulation rather than a
one-day event. The one yellow flag: ENPH is bid while its closest solar/clean-energy
peer **FSLR is being SOLD** (net_flow −$5.77M, bearish top-30) and **BE** also bearish
(−$3.53M) — so this looks idiosyncratic to ENPH, not a sector-wide solar bid. Phase 6
should resolve that. Verdict: **GENUINELY_UNUSUAL** (directional), with softer volume
confirmation (self vol-vs-avg only 70th pctile — accumulation, not an explosive spike).

## Key signals

- Universe net-directional premium **99.5th pctile** of 4,532 names [CTX:universe_pctile DUCKDB]
- Universe total premium **97.8th pctile**, IV rank **97.1st pctile** [CTX:universe_pctile DUCKDB]
- Self-history net-direction **93.3rd pctile**, total **90.0th** (31 sessions, gap-aware) [CTX:self_pctile DUCKDB]
- Net bullish flow positive 5 of last 6 sessions — **persistent accumulation** [CTX:self_history DUCKDB]
- Peer divergence: ENPH bid, **FSLR sold (−$5.77M)**, BE sold (−$3.53M) [CTX:screener_bullish_bearish]

## Detailed findings

### Universe ranking (cross-sectional, MCP + DuckDB)

`screener_bullish_bearish` (bullish, top-50) lists ENPH with **net_flow +$5,548,739**
(bullish_premium $18.09M − bearish_premium $12.54M), P/C 0.392 (call-heavy). In the
raw list it appears ~32nd, but that list is front-loaded with indices/ETFs
(SPX, SPXW, NDX, NDXP, GLD, IGV, VIX, XSP, SOXL). The exact DuckDB universe percentile
strips that distortion:

| Metric | Universe pctile (of 4,532) | Read |
|--------|---------------------------|------|
| total premium | **97.8** | top 2.2% |
| net-directional premium | **99.5** (≈ rank 23) | top 0.5% — a genuine leader |
| IV rank | **97.1** | top 3% — options very expensive |
| vol-vs-avg | 93.3 | elevated (noisy metric; see below) |

The day's directional tape is **led by Technology/semis** — DELL (+$32.7M), IBM
(+$32.6M), ADBE, NOW, PANW, QCOM, INTC, ALAB, CRDO, MU, ARM. On the bearish side,
single-name leaders are MSTR (−$120.7M), NVDA (−$97.0M), SNDK (−$48.1M), GOOGL.

### Sector read

UW tags ENPH "Technology," but its true peer group is **solar / clean-energy**, and
that group is **NOT** in favour today: **FSLR** (First Solar) is in the bearish top-30
at **−$5.77M**, **BE** (Bloom Energy) at **−$3.53M**. ENPH being bid while First Solar
is offered is a **relative-value / idiosyncratic** signature, not a sector bid →
**peer group LAGGING; ENPH is the outlier.** Hand-off to phase 6: is there an
ENPH-specific catalyst, or is the bullish flow a single desk's view that the broader
solar tape doesn't share?

### Self-history (DuckDB §C, gap-aware)

31 available sessions (non-contiguous — 2026-03-28→04-24 hole; this is the true N,
not a calendar month). Today vs ENPH's own distribution:

| Metric | Self pctile | 
|--------|-------------|
| net-directional premium | **93.3** |
| total premium | **90.0** |
| vol-vs-avg | 70.0 |

Recent net-directional trail ($M): 5/22 **+5.55**, 5/21 +7.45, 5/20 +5.35, 5/19 +2.06,
5/18 −5.53, 5/15 +5.55, 5/14 +3.63, 5/13 +0.73. IV rank has climbed 45→92 over the
same window — rising vol *and* rising bullish flow together.

> **Caveat:** raw `vol_x` = (option vol)/(avg30 *share* volume) ≈ 0.01 (unit mismatch,
> option contracts vs share volume) — read only the **percentile** (cross-sectionally
> comparable), not the raw ratio. ENPH was **outside top-50** on
> `screener_volume_vs_average`, but that list is dominated by micro-float names with
> 20–1000× ratios, so it is uninformative for a liquid name. Net: volume is elevated
> (self 70th pctile) but this is sustained accumulation, not a fresh volume explosion.

### Implied move (flag for phase 4)

`insights_deep_dive` returns `implied_move` 0.2957 and `implied_move_perc` 0.0046
(0.46%). The 0.46% reads as a daily/near-term figure that is **inconsistent** with
iv30d ≈ 101% and IV-rank 92 — phase 4 must derive the expected move directly from the
term structure / straddle and **not trust 0.46%**. Next earnings **2026-07-28** (well
beyond any near-dated structure — no earnings event inside a <60-DTE trade).

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__insights_deep_dive` | `{symbol: ENPH, date: 2026-05-22}` | net_flow +5.55M, iv_rank 92.1, P/C 0.39, DP 74.7M/1.18M sh @ 63.38 |
| `mcp__uw-pp__screener_bullish_bearish` | `{direction: bullish, top_n: 50, date: 2026-05-22}` | ENPH net_flow +5.55M; tech/semis lead |
| `mcp__uw-pp__screener_bullish_bearish` | `{direction: bearish, top_n: 50, date: 2026-05-22}` | FSLR −5.77M, BE −3.53M (solar peers sold); MSTR/NVDA lead bearish |
| `mcp__uw-pp__screener_volume_vs_average` | `{min_volume_ratio: 2, top_n: 50, date: 2026-05-22}` | ENPH outside top-50 (list is micro-float dominated; uninformative) |
| DuckDB §C | universe + self-history percentiles, `stock-screener-2026-05-22.parquet` | net_dir 99.5/93.3 pctile; total 97.8/90.0; iv_rank 97.1 |

## Tool errors

`insights_deep_dive` → `yahoo_fundamentals` returned `HTTP 401` (yfinance auth) — the
UW screener/DP/OI blocks are intact; fundamentals will be sourced in phase 7b
(Finnhub). Not fatal.

## Verdict for downstream — [CTX:] block

```
universe_pctile_total_prem:  97.8
universe_rank_net_dir:       ~23 of 4532  (99.5 pctile)
sector_leadership:           Tech/semis LEADING tape; ENPH's true peer group
                             (solar: FSLR, BE) LAGGING — ENPH is the bullish outlier
iv_rank:                     92.06
implied_move_pct:            UNRELIABLE from screener (0.46%); derive in phase-4
self_pctile_net_dir:         93.3   (sessions_in_window=31, gap-aware)
unusual_verdict:             GENUINELY_UNUSUAL  (directional; vol confirmation moderate)
```

- **Bias from this phase:** neutral (context only — sets no directional bias).
- **Conviction:** n/a (context phase).
- **Three things later phases should remember:**
  1. The bullish flow is **genuinely unusual cross-sectionally (99.5 pctile) AND
     persistent (5 of 6 sessions)** — phases 1–2 confluence is NOT capped at `+`
     (the BUSY_NAME cap does not fire).
  2. IV rank is **92–97 pctile — options are very expensive**; any long-premium
     structure fights a steep VRP headwind (phase 4/7c must address).
  3. **Peer divergence is the key tension:** ENPH bid while FSLR/BE sold. Treat the
     thesis as idiosyncratic-to-ENPH until phase 6 confirms a catalyst.
- **Open questions:** Why is ENPH the solar outlier? Is the call accumulation
  directional conviction or covered-call/vol-selling supply (which would explain high
  IV rank + call premium)? → phases 1, 3, 4 must distinguish.
```
