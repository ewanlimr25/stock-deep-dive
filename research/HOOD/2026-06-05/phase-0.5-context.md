# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** HOOD
**As-of date:** 2026-06-05
**Generated:** 2026-06-07T12:08:00-04:00
**Upstream phases cited:** phase-0-intake.md

## Summary

HOOD's flow on 2026-06-05 is **genuinely unusual in direction, not in size — and
the direction is BEARISH**. The name printed $113.5M total options premium
(98.8th universe percentile, but only 74.4th vs its own 40-session history —
busy is HOOD's normal), yet its **net-directional flow sits at the 0.6th
percentile of the entire optionable universe** (−$13.58M net) and at the
**7.7th percentile of its own self-history** — one of HOOD's most net-bearish
flow days in the local 40-session window. It ranks #33 on the market-wide net
bearish premium list while being absent from the bullish top-50. The
volume-vs-average ≥2× leg of the unusualness test FAILS (not on the ≥2× screen),
so the unusualness lives entirely in the *direction* of premium, not its
quantity. Sector backdrop: Technology is the day's sold sector (22 of the
bearish top-50 vs 12 of the bullish); Financial Services is mildly net-favoured
(4 bullish vs 2 bearish leaders) — **HOOD is one of only two financials on the
bearish leaders list**, a name-vs-sector divergence phase 6 must resolve.

## Universe ranking

| Metric | HOOD result | Leaders (ETFs/indices set aside) |
|---|---|---|
| Net bullish premium (top-50) | **outside top-50** | SPX +$2.40B, NDXP +$73.8M, IWM +$55.2M, STM +$53.4M (Tech), NDX +$43.5M |
| Net bearish premium (top-50) | **rank 33**, `net_flow` = −$13,575,317 | SPXW −$2.09B, QQQ −$116.9M, SNDK −$114.3M (Tech), SOXL −$85.6M, NVDA −$81.4M (Tech) |
| Volume-vs-average ≥2× (top-50) | **outside top-50** (option volume < 2× its 30-day avg) | degenerate low-base names (FCPT 5309×, IMCR 732×) — not informative leaders |
| IV-rank high (top-50) | **outside top-50** | MU 100, AIS 100, MRVL 100 |

Exact universe percentiles (DuckDB §C, full optionable universe with volume>0,
2026-06-05 snapshot) `[CTX:universe_pctile DUCKDB]`:

- `pctile_total_prem` = **98.8** (size: always-busy name)
- `pctile_net_dir` = **0.6** (direction: extreme bearish tail of the universe)
- `pctile_iv_rank` = **58.5** (vol pricing: mid-pack)
- `pctile_vol_vs_avg` = **96.4** — ⚠ unit caveat: the §C recipe's `vol_x`
  divides option *contracts* by `avg30_volume` (share volume), so it is valid
  only as a cross-sectional proxy (same distortion every name); HOOD's raw
  `vol_x` = 0.02 is unitless noise. The authoritative ≥2× option-volume gate is
  the `volume-vs-average` screen above, which HOOD **fails**.

## Sector read

Bearish top-50 sector mix: Technology 22, (ETF/index null 16), Industrials 4,
Communication Services 3, Consumer Cyclical 3, **Financial Services 2**.
Bullish top-50: (null 17), Technology 12, Consumer Cyclical 5, **Financial
Services 4**, Healthcare 4. → Tech is today's sold sector; Financials lean
mildly net-bid. HOOD (Financial Services) being sold against a mildly-bid
sector is idiosyncratic, not a sector trade. `[CTX:sector_leadership]`

## Self-history (40 sessions, non-contiguous window)

`[CTX:self_pctile DUCKDB]` — sessions_in_window = **40** (2026-03-13→06-05 with
the known 2026-03-30→04-24 hole; percentile over available sessions only):

- `self_pctile_net_dir` = **7.7** — bottom ~8% of HOOD's own net-directional
  flow distribution (extreme bearish for the name)
- `self_pctile_total` = **74.4** — active but unexceptional size for the name

## HOOD absolute numbers (insights deep-dive `.uw_screener`)

- `bullish_premium` $44,036,989 · `bearish_premium` $57,612,306 →
  derived `net_flow` = **−$13,575,317** (matches screener bearish row rank 33
  exactly — phantom-field guard respected: no `net_flow` field in this block)
- `call_premium` $81,433,934 · `put_premium` $32,060,841 ·
  `call_volume` 393,858 · `put_volume` 156,714 · `put_call_ratio` **0.40**
  — ⚠ call-heavy *volume* with net-bearish *premium aggression*: consistent
  with call selling / bearish call-side prints, for phase 1 to decompose
- `iv_rank` **49.59** · `iv30d` 0.7185 · `implied_move` $0.5998 ·
  `implied_move_perc` **0.727%** · `total_open_interest` 2,139,203
- `next_earnings_date` 2026-07-29 (UW field can be stale — phase 7b/7c re-check)

## Source

CLI (`uw screener` ×4, `uw insights deep-dive`) + DuckDB §C escape hatch
(universe + self-history percentiles). Outside-top-N metrics: bullish top-50,
volume-vs-average ≥2×, iv-rank top-50 — all recorded above.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw screener bullish-bearish --direction bullish --top-n 50 --date 2026-06-05 --json` | HOOD absent ← `.results[] \| select(.ticker=="HOOD")` (empty) | top-50 |
| `uw screener bullish-bearish --direction bearish --top-n 50 --date 2026-06-05 --json` | rank 33, net_flow −13,575,317 ← `.results \| to_entries[] \| select(.value.ticker=="HOOD")` | top-50 |
| `uw screener volume-vs-average --min-volume-ratio 2 --top-n 50 --date 2026-06-05 --json` | HOOD absent ← same selector (empty) | top-50 |
| `uw screener iv-rank --mode high --top-n 50 --date 2026-06-05 --json` | HOOD absent ← same selector (empty) | top-50 |
| `uw insights deep-dive --symbol HOOD --date 2026-06-05 --json` | bullish 44,036,989 / bearish 57,612,306 / pcr 0.4 / iv_rank 49.5939 / implied_move_perc 0.00727 ← `.uw_screener.*` | per-name block |
| DuckDB §C universe percentile (screener parquet 2026-06-05) | 98.8 / 0.6 / 58.5 / 96.4 ← `PERCENT_RANK()` | full universe |
| DuckDB §C self-history (40 screener parquets) | 7.7 / 74.4 / N=40 ← `PERCENT_RANK()` | self-history |
| DuckDB HOOD vol_x check | tot_vol 550,572 · avg30_volume 2.59e7 (shares) · vol_x 0.02 | 1 row |
| `uw screener bullish-bearish` ×2 sector group-by | Tech 22/50 bearish vs 12/50 bullish; FinSvcs 4 bull / 2 bear ← `group_by(.sector)` | top-50 ×2 |

## Tool errors

(none)

## DATA NOTE / CORRECTION

- `pctile_vol_vs_avg` (96.4) carries the §C unit caveat documented above — kept
  as cross-sectional proxy only; the binary ≥2× gate is taken from the
  `volume-vs-average` screen (HOOD fails it).
- **Corrected during phase 1** (see phase-1-flow.md §DATA NOTE): the UW
  screener row for HOOD carries `sector`="Technology", so the sector group-by
  above counted HOOD itself inside "Technology 22/50 bearish". The line "HOOD
  is one of only two financials on the bearish leaders list" used Finviz's
  taxonomy (HOOD = Financial) against UW's counts — invalid mix. Corrected
  read: under UW taxonomy HOOD trades with the day's sold Tech/fintech cohort
  (weakens the "idiosyncratic vs sector" claim); under Finviz taxonomy
  (authoritative for sector per data-source conventions, UW sector field
  known-unreliable) HOOD is a Financial being sold on a mildly-bid Financials
  day. Phase 6 must resolve which cohort HOOD actually traded with (e.g.
  fintech peers COIN/SOFI direction).

## Verdict for downstream phases

- **Bias from this phase:** none set (context only) — but the context is a
  bearish-direction extreme
- **Conviction:** n/a (context phase)

```
[CTX:]
universe_pctile_total_prem:  98.8        # DUCKDB
universe_rank_net_dir:       33 (bearish list; outside bullish top-50)
universe_pctile_net_dir:     0.6         # DUCKDB — extreme bearish tail
sector_leadership:           Financial Services is mid-pack/mildly bid today; Technology is the sold sector — HOOD bearish flow is idiosyncratic vs its sector
iv_rank:                     49.59
implied_move_pct:            0.727
self_pctile_net_dir:         7.7         # DUCKDB, N=40 (gap-aware)
unusual_verdict:  GENUINELY_UNUSUAL      # in DIRECTION (bearish), NOT in size:
                                         # vol-vs-avg ≥2× leg FAILS, total prem is
                                         # the name's norm (self 74.4) — do not
                                         # award size-based confluence in 1–2
```

- **Three things later phases should remember:**
  1. The unusualness is **direction-only**: net flow −$13.58M = 0.6th universe
     pctile / 7.7th self-pctile, while size is HOOD-normal. Size-based ++ in
     phases 1–2 is not licensed; direction-based evidence is.
  2. `put_call_ratio` 0.40 (call-heavy volume) with net-bearish premium ⇒ the
     bearish premium likely sits in *sold calls or bearish call-side prints* —
     phase 1 must decompose side/aggressor before calling direction.
  3. HOOD is being sold on a day its sector (Financials) is mildly bid and the
     tape's selling is concentrated in Tech — idiosyncratic, not sector beta;
     phase 6 should check whether a HOOD-specific catalyst/news explains it.
- **Open questions:** what instrument(s) carry the −$13.6M net (puts bought vs
  calls sold, tenor, strikes)? Is there dark-pool confirmation of distribution?
  Any name-specific news on/before 2026-06-05?
