# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** ENPH
**As-of date:** 2026-07-29
**Generated:** 2026-07-30T01:02:00Z
**Upstream phases cited:** `phase-0-intake.md`

## Summary

**The earnings event passed with a whimper, and that is the finding.** ENPH is D+1 after
its Q2 2026 print (postmarket 2026-07-28, confirmed by `next_earnings_date` rolling to
`2026-10-27` [CTX:insights_deep_dive]) — the one session all year where you would expect
unusual option activity. Instead ENPH traded **1.178× its own 30-day average option
volume** and posted total option premium at only the **26.6th percentile of its own 65
contiguous sessions** [CTX:self_pctile DUCKDB]. Absolute activity looks impressive
cross-sectionally (93.8th universe percentile on total premium, 95.7th on option volume,
out of 4,570 optionable names) purely because ENPH is a structurally busy name — the
classic magnitude-vs-unusualness trap this phase exists to catch.

Direction is mildly bearish and **trivially sized**: `net_flow` = `bullish_premium` −
`bearish_premium` = 2,153,830 − 2,633,643 = **−$479,813** on a $4.80B cap. That is
**5.8× too small** to enter the day's bearish top-50 (rank-50 cutoff `net_flow`
−$2,762,256, NEE) and ranks ENPH **477th of 538** Technology names on net flow. The
bearish tilt is real but weightless — an identical structural read to the 2026-07-27
pre-event run (`net_flow` −$258,731, [CTX] verdict BUSY_NAME_NORMAL_DAY), which is
notable: **the binary event did not change the character of the tape.**

Two genuinely informative context facts do emerge. First, **vol has collapsed**:
`iv30d` 0.905 → **0.797** in one session, `iv_rank` 63.3 → **47.05** — the **15.6th
percentile of ENPH's own 65-session IV-rank range** — while the forward implied move fell
from the pre-print **12.25%** to **5.58%**. Second, **today's −3.44% is sector beta, not
an ENPH verdict**: 15 of 16 names in the solar/clean-energy complex are red, with SHLS
−7.03%, FLNC −5.78% and ARRY −5.69% all *worse* than ENPH. Phase 0.5 sets no directional
bias; it hands downstream the instruction that neither the decline nor the flow is
idiosyncratically unusual, and that ENPH vol is now cheap both absolutely and relative to
its own sector.

## Key signals

- Net directional premium **−$479,813** (`bullish_premium − bearish_premium`), i.e.
  bearish tilt but **outside top-50 both directions** — vs a bearish rank-50 cutoff of
  −$2,762,256 [CTX:screener_bullish_bearish]
- Option volume **31,326** vs 30-day average **26,588.5** → **vol_x 1.178** — only 18%
  above normal, on the day after earnings [CTX:vol_vs_avg DUCKDB]
- Total premium at the **93.8th universe percentile** but the **26.6th self percentile**
  — the exact BUSY_NAME_NORMAL_DAY signature [CTX:universe_pctile DUCKDB]
- **IV crush confirmed:** `iv30d` 0.905 → 0.797 (−10.8pp, 1 session); `iv_rank` 47.05 =
  **self 15.6th percentile**; forward `implied_move_perc` **5.58%** vs 12.25% pre-print
  [CTX:insights_deep_dive]
- Put/call ratio **0.7259** = ENPH's own **87.5th percentile** — the *one* metric elevated
  vs self; puts are relatively crowded even as total activity is unremarkable
  [CTX:self_pctile DUCKDB]
- ENPH −3.44% is **5th-worst of 16** in the solar complex (15/16 red) → decline is
  sector-wide de-rating, not an idiosyncratic earnings verdict [CTX:peer_complex DUCKDB]
- ENPH `iv_rank` 47.1 is the **2nd-lowest** in that complex (FSLR 91.1, TAN 98.1,
  ICLN 100.0, SEDG 78.4) — ENPH vol is cheap relative to its own sector

## Detailed findings

### A — Universe ranking (`uw screener` CLI + exact DuckDB percentiles)

ENPH appears in **neither** the bullish nor the bearish top-50 for 2026-07-29.

| Metric | ENPH value | Universe standing | Cutoff / leaders |
|---|---|---|---|
| Net directional premium | **−$479,813** | **outside top-50 both directions**; exact pctile **4.7** (n=4,570) | bearish #50 = NEE −$2,762,256; bullish #50 = GM +$2,613,558 |
| Total premium (`call_premium + put_premium`) | $5,258,451 | **93.8th pctile** | rank 95 / 538 within Technology |
| Option volume (`call_volume + put_volume`) | **31,326** | **95.7th pctile** | — |
| Volume vs 30-day average | **vol_x 1.178** | **72.2nd pctile** | outside the `--min-volume-ratio 2` top-50 (cutoff 20.79×) |
| `iv_rank` | **47.05** | **49.8th pctile** (median) | outside iv-rank-high top-50 (all 50 at 100.0) |

> **Reading the 4.7 net-dir percentile correctly.** A 4.7th percentile sounds extreme, but
> PERCENT_RANK is rank-based, not magnitude-based: most of the 4,570 names cluster at
> ≈0 net flow, so any negative print lands in the bottom decile. The magnitude test is
> the one that binds — **−$479,813 is 5.8× below the bearish top-50 threshold**. Both
> facts are true and must be reported together: *directionally* bearish-tilted,
> *economically* weightless. Downstream phases must not cite "bottom 5% of the universe"
> as evidence of heavy bearish flow.

> **ETF caveat applied.** The bullish leaderboard is ETF/index-heavy (SPY #2, SMH #6,
> SPXW #9, NDXP #11, NDX #13, QQQ #16, VIX #18, XSP #23, DIA #28, VOO #46, VIXW #47);
> the bearish list likewise (SPX #1, GLD #4, SOXL #7, SOXX #10, IWM #18, TLT #20,
> TQQQ #21). Among **single names**, the day's bullish leaders were **SNDK #1, ASML #3,
> GOOGL #4, MSFT #5, GEV #7, AMD #8** and the bearish leaders **NVDA #2, MU #3, AMZN #5,
> TSM #6, INTC #8, BE #9** — a semiconductor-dominated tape on both sides.

> **The volume-vs-average leaderboard is a low-base artifact and was discarded.** #1 NWS
> shows `volume_ratio` 523.2 on `avg_total_volume` **5.13 contracts** and
> `total_volume` 2,686; the top-50 is almost entirely micro-liquidity tickers and bond
> ETFs (LQDH, ANGL, SYLD, JNK, XBIL, SPBO). For a name with a 26,588-contract 30-day
> average, that list is uninformative — hence the exact DuckDB `vol_x` above.

### B — Sector read

Universe-wide sector aggregation for 2026-07-29 (n = 3,363 optionable names with a sector
label; `SUM(bullish_premium − bearish_premium)` and `%` of constituents closing green):

| Sector | n | Net flow ($M) | % green | Avg chg % |
|---|---|---|---|---|
| Communication Services | 159 | **+75.85** | 53.5 | −0.26 |
| **Technology (ENPH)** | 538 | **+55.96** | **34.4** | **−2.20** |
| Utilities | 90 | +30.66 | **8.9** | −2.31 |
| Healthcare | 612 | +5.35 | 32.2 | −1.05 |
| Real Estate | 173 | −0.64 | 31.8 | −0.52 |
| Energy | 197 | −12.30 | **58.9** | **+0.76** |
| Consumer Defensive | 136 | −12.99 | 58.8 | +0.33 |
| Basic Materials | 207 | −10.26 | 23.2 | −1.70 |
| Financial Services | 431 | −46.09 | 24.4 | −1.56 |
| Industrials | 476 | **−67.98** | **14.5** | **−3.60** |
| Consumer Cyclical | 344 | **−98.01** | 34.0 | −1.07 |

**Verdict: ENPH's sector is mid-pack on premium but broadly sold on price.** Technology
carries the 2nd-largest net bullish premium (+$55.96M) yet only **34.4% of its members
closed green** and the average member fell **−2.20%** — premium is concentrated in a
handful of mega-cap winners (SNDK, ASML, GOOGL, MSFT, AMD) while the breadth underneath
is poor. This is a **risk-off, narrow tape** on an FOMC day: only Energy (+0.76%) and
Consumer Defensive (+0.33%) posted positive average change; Industrials was worst
(−3.60%, 14.5% green). Phase 6 inherits this as a head start and should resolve whether
the FOMC statement (14:00 ET today) drove it.

**The sub-sector cut is the one that matters for ENPH.** ENPH's Finviz industry is
**Solar** (`fz` sector Technology / industry Solar, `phase-0-intake.md`), and the solar /
clean-energy complex was uniformly liquidated:

| Ticker | Px | Chg % | Net flow ($M) | Opt vol | P/C | IV rank | % from 52W high |
|---|---|---|---|---|---|---|---|
| SHLS | 7.94 | **−7.03** | −0.003 | 1,162 | 0.689 | 78.8 | −39.8 |
| FLNC | 11.89 | −5.78 | −0.213 | 4,395 | 0.260 | 82.2 | −64.5 |
| ARRY | 4.81 | −5.69 | −0.000 | 2,933 | 0.362 | 77.6 | −60.7 |
| GEV | 900.28 | −4.57 | **+32.604** | 23,250 | 1.368 | 65.7 | −24.7 |
| **ENPH** | **35.07** | **−3.44** | **−0.480** | **31,326** | **0.726** | **47.1** | **−52.4** |
| PLUG | 1.90 | −3.06 | +1.486 | 50,091 | 2.455 | 35.2 | −58.5 |
| TAN (ETF) | 47.68 | −2.89 | +0.162 | 752 | 1.657 | 98.1 | −36.9 |
| NXT | 92.67 | −2.81 | −0.249 | 1,101 | 0.787 | 84.8 | −43.2 |
| NRG | 124.23 | −2.61 | +3.345 | 24,678 | 0.025 | 100.0 | −34.6 |
| SEDG | 39.04 | −2.57 | +0.461 | 7,229 | 0.522 | 78.4 | −52.0 |
| JKS | 14.58 | −2.34 | −0.002 | 100 | 1.000 | 1.2 | −54.3 |
| ICLN (ETF) | 16.87 | −1.92 | −0.002 | 420 | 1.010 | 100.0 | −29.1 |
| BE | 163.75 | −1.85 | **−28.203** | 253,397 | 1.315 | 67.1 | −53.4 |
| RUN | 9.47 | −1.66 | +0.733 | 21,860 | 0.215 | 71.4 | −57.8 |
| FSLR | 199.24 | −1.65 | −0.853 | 7,490 | 0.354 | 91.1 | −37.9 |
| CSIQ | 13.72 | **+0.48** | −0.012 | 2,613 | 0.206 | 71.4 | −60.3 |

Four things downstream must carry from this table:

1. **ENPH's −3.44% is mid-pack (5th worst of 16) in a complex where 15/16 fell.** The
   post-earnings decline is **not separable from sector beta** on this session. Any phase
   that reads today's price action as the market's verdict on the Q2 print is
   over-attributing. Phase 5 and phase 7b must control for this.
2. **Capital is rotating to grid/power-generation, not to distributed solar.** GEV
   (+$32.6M, universe bullish **#7**), NRG (+$3.3M, **#40**) and PWR (+$4.9M, **#29**)
   all drew net bullish premium; every pure-play solar name drew ≈0 or negative. The
   electrification bid is real but it is landing upstream of ENPH.
3. **Within residential solar, ENPH is the flow laggard.** RUN (+$0.73M), SEDG (+$0.46M)
   and PLUG (+$1.49M) saw net *buying*; ENPH (−$0.48M) and FSLR (−$0.85M) saw net
   selling. ENPH did not attract the dip-buying its closest comparables did — a yellow
   flag for phase 6 to reconcile, and a direct contradiction of any "washed-out, everyone
   is buying the bottom" narrative.
4. **ENPH vol is the cheapest in the complex.** `iv_rank` 47.1 vs SEDG 78.4, ARRY 77.6,
   SHLS 78.8, FLNC 82.2, NXT 84.8, FSLR 91.1, TAN 98.1, ICLN 100.0, NRG 100.0. Only JKS
   (1.2, illiquid — 100 contracts) and PLUG (35.2) are lower. ENPH has already paid its
   event premium; its peers have not. Phase 4 owns whether that is an opportunity or a
   correctly-priced absence of catalyst.

### C — Self-history (65 contiguous local sessions, 2026-04-27 → 2026-07-29)

Windowed to the contiguous block per the `phase-0-intake.md` gap flag (the
2026-03-27 → 2026-04-27 hole is excluded; **N = 65**, not a 65-calendar-day window).

| Metric | Today | Self percentile |
|---|---|---|
| Net flow (`bullish − bearish`) | −$479,813 | **32.8** |
| Net directional (`net_call_prem − net_put_prem`) | −$479,813 | **34.4** |
| Total premium | $5,258,451 | **26.6** |
| Option volume | 31,326 | **56.3** |
| Put/call ratio | 0.7259 | **87.5** |
| `iv_rank` | 47.05 | **15.6** |
| Total open interest | 381,215 | **26.6** |

**The headline is the 26.6th-percentile premium on an earnings-reaction day.** ENPH's own
distribution says today was a *below-median* premium session and a barely-above-median
volume session. Whatever repositioning the Q2 print triggered, it did not show up as
option urgency. The `net_dir` self percentile of **34.4** is mildly bearish-of-median and
nowhere near the ≥80 threshold that would support GENUINELY_UNUSUAL.

Two exceptions cut in opposite directions and both belong downstream:
- **P/C 87.5th percentile** — puts are unusually prominent *for this name* even though
  total activity is not. Phases 1/3/7c must determine whether that is fresh bearish
  initiation or post-event hedge retention.
- **IV rank 15.6th percentile** — realized vol expectations are at the bottom of ENPH's
  own recent range. Phase 4 must decide whether cheap vol here is opportunity or
  correctly-priced quiet.

**Trailing 8-session tape (context for phase 1 and phase 5):**

| Date | Close | Chg % | Net flow | Opt vol | P/C | IV rank | `iv30d` | Total OI |
|---|---|---|---|---|---|---|---|---|
| 2026-07-29 | **35.07** | **−3.44** | −479,813 | 31,326 | 0.726 | **47.1** | **0.797** | 381,215 |
| 2026-07-28 | 36.32 | −4.45 | −3,162,110 | 39,644 | 0.680 | 63.3 | 0.905 | 363,227 |
| 2026-07-27 | 38.01 | +3.57 | −258,731 | 14,999 | 0.547 | 69.8 | 0.922 | 355,935 |
| 2026-07-24 | 36.70 | −5.63 | −346,714 | 14,957 | 0.622 | 66.8 | 0.924 | 362,593 |
| 2026-07-23 | 38.89 | −1.74 | **+5,904,530** | 22,722 | 0.947 | 65.2 | 0.927 | 361,654 |
| 2026-07-22 | 39.58 | −0.90 | −215,563 | 10,828 | 0.405 | 75.0 | 0.987 | 359,659 |
| 2026-07-21 | 39.94 | +1.22 | +50,235 | 10,148 | 0.546 | 79.5 | 1.004 | 356,978 |
| 2026-07-20 | 39.46 | −5.08 | −518,325 | 18,719 | 0.633 | 82.1 | 1.017 | 348,684 |

Observations for downstream:
- **The selling front-ran the print.** ENPH fell −4.45% on 07-28 *before* the postmarket
  release and carried the single largest bearish net flow of the window on that day
  (−$3,162,110, ~6.6× today's). The heaviest bearish premium was **pre-**event.
- **The reaction itself was −3.44% against a ±12.25% pre-print implied move** — roughly
  **28% of the priced move**. Vol sellers won the event decisively; this is the mechanical
  driver of the `iv30d` 0.905 → 0.797 collapse. Phase 4 must not read the low post-event
  IV rank as complacency without accounting for this.
- **`iv30d` has fallen monotonically for 8 straight sessions** (1.017 → 0.797, −22pp) —
  the crush began well before the print and the event merely completed it.
- **Cumulative 07-20 → 07-29: 39.46 → 35.07 = −11.1%**, with 6 of 8 sessions red. The
  drawdown is a trend, not a gap.
- **Open interest built +17,988 (+4.95%) today**: calls +9,120 (221,652 from 212,532),
  puts +8,868 (159,563 from 150,695); OI put/call **0.72**. The build is almost perfectly
  balanced — no directional OI signature. Phase 3 owns strike placement.
- One genuinely bullish outlier remains unexplained: **07-23 net flow +$5,904,530 on a
  −1.74% day** — the largest directional print of the window, on a red candle. Phase 1
  should determine whether that position is still alive after the event.

### D — Cross-check vs the 2026-07-27 run

| Field | 2026-07-27 | 2026-07-29 | Change |
|---|---|---|---|
| Spot | 38.01 | **35.07** | **−7.74%** |
| `net_flow` | −$258,731 | −$479,813 | still trivially bearish |
| `iv_rank` | 69.81 | **47.05** | **−22.8pp** |
| `implied_move_perc` | 12.25% | **5.58%** | **−6.67pp** |
| `self_pctile_net_dir` | 37.0 | 34.4 | flat |
| `unusual_verdict` | BUSY_NAME_NORMAL_DAY | **BUSY_NAME_NORMAL_DAY** | unchanged |
| Short float (`fz`) | 17.55% | **17.94%** | **+0.39pp** |

**The interpretation:** a binary catalyst fired and the *character* of the option tape is
unchanged — same verdict, same trivial net flow, same mid-pack self percentile. What
changed is entirely in the vol surface (rank −22.8pp, implied move −6.67pp) and the
price (−7.74%). The prior run's `spot_reference` 38.01 and stated support **35.00** are
now directly in play: **spot 35.07 is 0.2% above that support and sits on the 2026-08-21
$35 put wall (3,734 contracts)**. Phases 3 and 4 must re-derive both, not inherit them.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` / SQL path | Rows used |
|---|---|---|
| `uw insights deep-dive --symbol ENPH --date 2026-07-29 --json` | `bullish_premium`=2153830, `bearish_premium`=2633643, `iv_rank`=47.0523, `implied_move_perc`=0.05585, `iv30d`=0.79698, `put_call_ratio`=0.72595, `total_open_interest`=381215, `next_earnings_date`=2026-10-27 ← `.uw_screener` | 1 |
| `uw screener bullish-bearish --direction bullish --top-n 50 --date 2026-07-29 --json` | ENPH absent ← `[.results[]\|select(.ticker=="ENPH")]\|.[0]//null` → `null`; cutoff GM `net_flow`=2613558 ← `.results[49]` | 50 |
| `uw screener bullish-bearish --direction bearish --top-n 50 --date 2026-07-29 --json` | ENPH absent ← same null-safe select; cutoff NEE `net_flow`=−2762256 ← `.results[49]`; BE `net_flow`=−28202872 (rank 9) | 50 |
| `uw screener volume-vs-average --min-volume-ratio 2 --top-n 50 --date 2026-07-29 --json` | ENPH absent; leaderboard is a low-base artifact (NWS `volume_ratio`=523.24 on `avg_total_volume`=5.1334) ← `.results[0]`; cutoff SNN 20.79 ← `.results[49]` | 50 |
| `uw screener iv-rank --mode high --top-n 50 --date 2026-07-29 --json` | ENPH absent; all top-50 at `iv_rank`=100 ← `.results[0:5]` | 50 |
| DuckDB `stock-screener-2026-07-29.parquet` — universe percentiles | `universe_n`=4570, `pctile_total_prem`=93.8, `pctile_net_flow`=4.7, `pctile_net_dir`=4.7, `pctile_iv_rank`=49.8, `pctile_vol_vs_avg`=72.2, `pctile_optvol`=95.7, `vol_x`=1.178 ← `PERCENT_RANK() … QUALIFY ticker='ENPH'` | 4,570 |
| DuckDB — ENPH raw row | `close`=35.07, `prev_close`=36.32, `total_volume`=8670939, `avg30_volume`=5127857.95, `call_volume`=18150, `put_volume`=13176, `avg_30_day_call_volume`=18586.57, `avg_30_day_put_volume`=8001.97, `week_52_high`=73.74, `week_52_low`=25.775, `marketcap`=4799493615 | 1 |
| DuckDB — self-history, 65 contiguous files ≥ 2026-04-27 | `sessions_in_window`=65, `self_pctile_net_flow`=32.8, `self_pctile_net_dir`=34.4, `self_pctile_total`=26.6, `self_pctile_optvol`=56.3, `self_pctile_pcr`=87.5, `self_pctile_ivrank`=15.6, `self_pctile_oi`=26.6 | 65 |
| DuckDB — trailing 8-session tape | 07-28 `net_flow`=−3162110; 07-23 `net_flow`=+5904530; `iv30d` 1.017→0.797 | 8 |
| DuckDB — sector aggregation | Technology `net_flow_musd`=+55.96, `pct_green`=34.4, `avg_chg_pct`=−2.20; Industrials −67.98 / 14.5%; Consumer Cyclical −98.01 | 3,363 |
| DuckDB — solar peer complex (18 tickers requested, 16 present) | SHLS −7.03%, FLNC −5.78%, ARRY −5.69%, ENPH −3.44%, CSIQ +0.48%; BE `net_flow`=−28.203M; ENPH `pct_from_52wh`=−52.4 | 16 |
| DuckDB — Technology sector rank | `tech_n`=538, `rank_most_bearish`=62, `rank_net_flow_desc`=477, `rank_total_prem`=95 | 538 |
| DuckDB — OI deltas | `d_coi`=+9120, `d_poi`=+8868, `oi_pcr`=0.72 ← `call_open_interest − prev_call_oi` | 1 |
| `jq … research/ENPH/2026-07-27/decision.json` | prior `iv_rank`=69.81, `expected_move.front_expiry_pct`=12.25, `spot_reference`=38.01 | 1 |

All five `uw` reads round-tripped through `jq` on validated JSON; every ENPH-row select
used the null-safe `[…]|.[0]//null` form per `memory/batched-stdout-swallow.md`, and each
read was captured to a file before being queried. `net_flow` was **derived**
(`bullish_premium − bearish_premium`) for the single name because
`insights deep-dive`'s `uw_screener` block does not carry a `net_flow` field
(`lib/uw-json-paths.md` phantom-field trap); the derived value was independently
reproduced by DuckDB as `net_call_premium − net_put_premium` = −479,813 — **the two
methods agree exactly**, which is a useful validation of the derivation rule.

## Tool errors

None. All five `uw screener`/`insights` calls returned exit 0 with parseable JSON; all
DuckDB queries succeeded.

Two non-blocking notes:
1. One DuckDB query initially failed with `ParserException: syntax error at or near
   "close"` (bare `close` used as a column alias, which collides with a DuckDB keyword).
   Re-run with explicit `AS px` aliasing; **no value was transcribed from the failed
   query.**
2. The `lib/duckdb-cuts.md §C` snippet references a column `avg30_volume` for the
   option-volume ratio. In `stock-screener-*.parquet` that column is **stock** volume;
   the option-volume average lives in `avg_30_day_call_volume` + `avg_30_day_put_volume`.
   `vol_x` above uses the option columns (1.178). Using `avg30_volume` would have
   produced a meaningless equity-vs-option ratio. **Propose-only** doc fix, per the audit
   convention.

## DATA NOTE / CORRECTION

First read stood for every reported value. No number in this file was revised after its
initial validated read. The two items above are a rejected query (nothing transcribed)
and a library documentation discrepancy (correct columns used), not corrections to data.

## Verdict for downstream phases

```
universe_pctile_total_prem:  93.8            # DUCKDB, n=4,570 optionable names
universe_rank_net_dir:       outside top-50  # both directions; exact pctile 4.7, magnitude −$479,813 vs −$2,762,256 cutoff
sector_leadership:           Technology mid-pack on premium (+$55.96M, 2nd) but LAGGING on price (34.4% green, avg −2.20%); Solar sub-complex uniformly lagging (15/16 red); grid/power (GEV/PWR/NRG) is the sector bid, not distributed solar
iv_rank:                     47.05           # self 15.6th pctile — bottom of its own range
implied_move_pct:            5.58            # front expiry; was 12.25 pre-print
self_pctile_net_dir:         34.4            # N=65 contiguous sessions (2026-04-27..2026-07-29)
unusual_verdict:             BUSY_NAME_NORMAL_DAY
```

**Confluence cap triggered.** BUSY_NAME_NORMAL_DAY fired on both legs of the test — high
absolute premium (universe 93.8) with a mid-pack universe rank *and* self percentiles
below 60 (`net_dir` 34.4, `total` 26.6). Per `rubrics/confluence-scoring.md`,
**phases 1–2 confluence is capped at `+`, not `++`.** GENUINELY_UNUSUAL was tested and
failed decisively: `vol_x` 1.178 against a ≥2 requirement, and `self_pctile_net_dir` 34.4
against a ≥80 requirement. QUIET was also rejected — 95.7th-percentile option volume is
not thin.

- **Bias from this phase:** **neutral by construction.** Phase 0.5 sets context, not
  direction. The observed bearish *tilt* is recorded as too small to weigh.
- **Conviction:** n/a (context phase)
- **Three things later phases should remember:**
  1. **An earnings event fired and the tape did not care.** Option premium sits at the
     **26.6th self percentile** with `vol_x` **1.178** on D+1. Treat every "big flow"
     claim about ENPH today with suspicion — verify magnitude against the −$479,813 net
     and the $2.76M top-50 cutoff before assigning weight. Phases 1–2 are capped at `+`.
  2. **Vol did all the work, price did some, flow did none.** `iv_rank` 69.81 → **47.05**
     (self 15.6th pctile), implied move 12.25% → **5.58%**, `iv30d` down 8 consecutive
     sessions (1.017 → 0.797), realized reaction **−3.44% ≈ 28% of the priced ±12.25%**.
     ENPH is now the 2nd-cheapest vol in a solar complex sitting at 78–100 IV rank.
     Phase 4 owns this; it is the single largest structural change since 07-27.
  3. **Today's −3.44% is sector beta, not an earnings verdict.** 15 of 16 solar names
     fell; SHLS/FLNC/ARRY fell harder. Meanwhile RUN/SEDG/PLUG attracted net *buying*
     and ENPH did not — ENPH is the flow laggard within its own sub-sector while capital
     rotates upstream to GEV/PWR/NRG. Do not let phase 5/7b attribute the full decline to
     the Q2 print, and do not let any phase claim washed-out dip-buying.
- **Open questions phase 0.5 cannot answer:**
  - What is inside the **P/C 87.5th-percentile** put activity — fresh bearish initiation
    or retained post-event hedges? (→ 1, 3, 7c)
  - Is the **07-23 +$5,904,530** bullish position (largest of the window, printed on a
    red candle) still alive after the event? (→ 1, 3)
  - Is ENPH's sector-cheapest `iv_rank` 47.1 an opportunity or the correct price for a
    name with no catalyst until **2026-10-27**? (→ 4, 9)
  - Does **spot 35.07** hold as dealer-supported support on the 08-21 $35 put wall, or
    fail once the 07-31 gamma island rolls off? (→ 3, 4)
  - Was the broad risk-off (only 2 of 11 sectors green on average change) FOMC-driven?
    (→ 6)
