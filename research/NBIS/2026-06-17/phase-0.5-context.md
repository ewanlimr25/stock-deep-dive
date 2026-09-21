# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** NBIS (Nebius Group NV)
**As-of date:** 2026-06-17
**Generated:** 2026-06-18T00:23:50Z
**Upstream phases cited:** phase-0-intake.md

## Summary

NBIS is having a genuinely big options day on the SIZE axis — today is its **largest
total-premium day in the 48-session local window (self-pctile 100.0)** and it sits at the
**99.7th universe percentile on total premium / 99.6th on net-directional premium** (CLI rank
**#20** of 60 on net bullish flow). But two qualifiers temper the headline: (1) the net
direction is small relative to gross — bullish premium $329.1M vs bearish $311.1M nets only
**+$18.0M** (net/gross ≈ 2.8%), i.e. heavily two-sided, and (2) option volume is **1.43× its
own 30-day average (81st pctile)** — elevated but NOT a ≥2× blowout, which is why NBIS is
absent from the CLI `volume-vs-average --min-ratio 2` top-80. IV rank 91.3 (96.6 pctile)
means the record premium is partly an IV-inflation artifact, not pure incremental positioning.
Net verdict: **GENUINELY_UNUSUAL on premium/IV/net-direction rank, but the directional
conviction is thinner than the premium headline** — phases 1–2 should resist maxing confluence
on raw dollar size alone.

## Universe ranking (today, 2026-06-17)

- **Net bullish premium:** NBIS rank **#20 of 60** (net_flow +$18,009,087). Single-name
  leaders (ex-ETF): BABA (+$285.2M), HOOD (+$71.7M). Index/ETF leaders set aside per pitfall:
  SPX (+$1.75B), GLD (+$238M), IBIT (+$78M).
- **Net bearish premium:** NBIS **outside top-60** (it is a net-bullish name today ✓).
  Notably the bearish leaders are mega-cap tech — **META −$447.9M, MSFT −$197.9M, AMZN
  −$134.9M, NDX −$118.7M** (plus SPY −$604.8M). The large-cap AI complex is being SOLD on net
  premium today while NBIS and BABA are bought → possible rotation into secondary AI-infra
  names; flagged for phase-6.
- **Volume-vs-average:** NBIS **outside CLI top-80** (filter ≥2×). True ratio computed from
  parquet: **1.43× 30-day option average (81st universe pctile)** — elevated, not extreme.
- **IV-rank-high:** NBIS **outside CLI top-60** in absolute rank, but iv_rank 91.3 = **96.6
  universe percentile** — very high vol, just not the single most extreme names.

## Sector read

- UW screener tagged NBIS sector = **"Communication Services"**, which conflicts with `fz`
  (**Technology / Software-Infrastructure**) and the company's actual AI-cloud business. Per the
  known data-source workaround, **the UW sector field is broken — trust `fz`: NBIS is
  Technology / AI-infrastructure.** (yahoo_fundamentals cross-check returned HTTP 401.)
- Cross-sectional tech read is **split / rotational:** mega-cap tech (META, MSFT, AMZN) shows
  net-bearish premium today while secondary/high-beta AI names (NBIS, BABA, HOOD) are
  net-bullish. This is the strongest cross-sectional nuance for phase-6 to resolve: is the bid
  in NBIS genuine AI-infra leadership, or rotation/chase out of the crowded mega-caps?

## Self-history (parquet present, N=48 sessions, gap-aware)

- **self_pctile_total = 100.0** — today is the single biggest total-premium day for NBIS in
  the entire 48-session local window. (Caveat: IV rank 91 inflates premium; size partly = price.)
- **self_pctile_net_dir = 87.2** — net bullish direction is high vs its own history but not a
  record (12 of the last 48 sessions printed equal-or-stronger net direction... no: 87th pctile
  ⇒ ~6 sessions stronger). N=48 spans 2026-03-13→06-17 with the 03-28→04-24 gap (`§ gap`).

## Source

CLI rankings (`uw screener` + `uw insights deep-dive`) **+ DuckDB §C** exact percentiles
(local parquet present for 2026-06-17). "Outside top-N" recorded for vol-vs-avg and IV-rank
as information, not error. DuckDB recipe note: the canned `vol_x` divides option contracts by
*stock* avg volume; I recomputed the proper **option-vol ÷ 30-day option-avg = 1.43×** for the
volume read (the percentile-recipe figure 96.2 measures options-intensity vs share volume, a
different metric — not used for the unusualness verdict).

## Verdict for downstream

```
universe_pctile_total_prem:  99.7                         [CTX:universe_pctile DUCKDB]
universe_rank_net_dir:       #20 of 60 (99.6 pctile)      [CTX]
sector_leadership:           Tech/AI-infra SPLIT — mega-cap tech net-bearish, secondary AI (NBIS/BABA) net-bullish → rotation, resolve in phase-6
iv_rank:                     91.3                          [CTX]  (96.6 universe pctile)
implied_move_pct:            4.86%                         [CTX]  (13.66 pts; feeds phase-9 N4)
self_pctile_net_dir:         87.2  (N=48, gap-aware)       [CTX:self_pctile DUCKDB]
self_pctile_total_prem:      100.0 (N=48)                  [CTX:self_pctile DUCKDB]
unusual_verdict:             GENUINELY_UNUSUAL (size/IV/net-rank) — BUT directional conviction CAPPED: opt vol only 1.43× avg (not ≥2×), net/gross 2.8% (two-sided), premium partly IV-inflated
```

**Calibration guidance for phases 1–2:** treat the flow as real and worth reading closely
(record premium day, top-decile net rank), but do NOT escalate confluence to `++` on dollar
size alone — the ≥2× volume criterion fails (1.43×) and the net is two-sided. The unusualness
is most defensible on premium *size* and *IV*, least on *directional volume*.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` / SQL path | Rows used |
|------------------|--------------------------------|-----------|
| `uw screener bullish-bearish --direction bullish --top-n 60 --date 2026-06-17` | NBIS rank #20; net_flow +$18.0M; bull $329.1M / bear $311.1M ← `.results[]\|select(.ticker=="NBIS")` | top-60 |
| `uw screener bullish-bearish --direction bearish --top-n 60 --date 2026-06-17` | NBIS outside top-60; leaders META/MSFT/AMZN net-bearish ← `.results[]` | top-60 |
| `uw screener volume-vs-average --min-volume-ratio 2 --top-n 80 --date 2026-06-17` | NBIS outside top-80 ← `index("NBIS")` | top-80 |
| `uw screener iv-rank --mode high --top-n 60 --date 2026-06-17` | NBIS outside top-60 ← `index("NBIS")` | top-60 |
| `uw insights deep-dive --symbol NBIS --date 2026-06-17` | call_prem $514.1M, put_prem $189.4M, P/C 0.846, iv_rank 91.3, iv30d 113%, implied_move 4.86%, OI 1.13M, next_earn 2026-08-06 ← `.uw_screener` | 1 |
| DuckDB §C universe pctiles | total_prem 99.7, net_dir 99.6, iv_rank 96.6 ← `PERCENT_RANK()` over screener-2026-06-17 (n=4,755 optionable) | universe |
| DuckDB §C self-history | self net_dir 87.2, self total 100.0, N=48 ← `PERCENT_RANK()` over 48 screener files | 48 |
| DuckDB (proper option-vol ratio) | opt_vol 259,334 / avg30 181,494 = **1.43×** (81 pctile) | NBIS |

## Tool errors

`uw insights deep-dive` → `.yahoo_fundamentals` returned `{"error":"yahoo quoteSummary NBIS: HTTP 401"}` — yahoo sector/fundamental cross-check unavailable (paid/blocked). Non-fatal; `fz` supplies sector. No CLI command errored.

## DATA NOTE / CORRECTION

Initial CLI-only read suggested "volume not unusual" (outside top-80 vol list). Corrected with
DuckDB: option volume **is** elevated (1.43× 30-day avg, 81st pctile) — just below the CLI's 2×
filter, not "not unusual." The verdict uses the precise 1.43× figure. Also corrected the §C
canned `vol_x` (0.02, which mis-divides option vol by share vol) → recomputed proper 1.43×.

## Verdict for downstream phases

- **Bias from this phase:** neutral (context only — sets no directional bias per skill rule).
- **Conviction:** n/a (context phase).
- **Three things later phases should remember:**
  1. Record self-premium day (100 pctile) + top-decile universe rank, BUT net is two-sided (+$18M / $640M gross) and volume only 1.43× — read direction conservatively.
  2. Mega-cap tech net-bearish while NBIS/BABA net-bullish → rotation vs leadership question for phase-6; if it's chase-rotation, conviction should fade.
  3. IV rank 91.3 / IV30d 113% — premium is expensive and the "record premium" is partly IV-inflated; phase-4/9 structures must respect rich vol.
- **Open questions:** Is the +$18M net the residue of aggressive directional buying or balanced dealer/overwrite flow? (phase-1 aggressor split.) Does the dark pool confirm accumulation under the options bid? (phase-2.)
