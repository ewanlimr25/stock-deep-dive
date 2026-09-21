# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** HOOD
**As-of date:** 2026-06-15
**Generated:** 2026-06-16T11:45:00Z
**Upstream phases cited:** phase-0-intake.md

## Summary

HOOD's tape on 2026-06-15 is **genuinely unusual, not a busy name's normal day**.
By the full optionable universe (N=4,754 names) it sits in the **99.4th percentile
on total option premium ($233.1M) and the 99.5th percentile on net-directional
premium (+$8.68M net bullish)** — and against its *own* 46-session history this is
the 93.3rd-percentile day for total premium and the 84.4th-percentile day for net
bullish direction `[CTX:self_pctile DUCKDB]`. The directional tilt is decisively
call-side: net call premium **+$10.06M** vs net put premium **+$1.38M**, call
volume 353,167 vs put volume 122,323 (PCR 0.346). The one caveat: among the day's
*largest* directional names HOOD ranks only **32nd** (the leaderboard is dominated
by index ETFs + semis printing $25–278M net), so the raw net dollars are modest in
absolute leader terms even as the name is top-decile both cross-sectionally and vs
itself. Context only — sets no bias.

## Key signals

- Universe percentiles today (N=4,754): total prem **99.4**, net-dir **99.5**,
  vol-vs-avg **96.4**, iv-rank **40.8** `[CTX:universe_pctile DUCKDB]`.
- Self-history (46 sessions): net-dir **84.4 pctile**, total prem **93.3 pctile**
  — among the name's own busiest & most bullish recent days `[CTX:self_pctile DUCKDB]`.
- Net flow **+$8.68M** ranks **32nd** on the day's net-bullish leaderboard
  `[CTX:screener_bullish_bearish]` — top-0.5% of all names, mid-pack among the day's giants.
- Call-tilt: net call prem +$10.06M vs net put +$1.38M; PCR 0.346; call vol 353k vs put 122k.
- IV rank **32.4** (mid/low, 40.8 universe pctile); implied move **±4.65% ($4.55)** on $98.12.

## Detailed findings

### Universe ranking (`uw screener`, as-of 2026-06-15)

- **Net bullish premium:** HOOD ranks **32 / top-50**. Leaderboard (net_flow, ETFs
  to set aside): NDX $278M, SPXW $139M, **HPE $92M**, **TSLA $90M**, **MU $78M**,
  **NVDA $70M**, NDXP $64M, QQQ $41M, **CRM $35M**, **AMD $34M**, **AVGO $32M**,
  **MRVL $26M** `[CTX:screener_bullish_bearish]`. Single-name leaders are semis +
  mega-cap tech; HOOD is well behind them in absolute net dollars.
- **Net bearish premium:** HOOD **outside top-50** (not a top name being sold).
- **Volume-vs-average (≥2× screen):** HOOD **outside top-50** of the ≥2× screen,
  yet 96.4th universe pctile on the parquet's vol ratio. ⚠️ The parquet
  `avg30_volume` field is *share* volume, so an absolute "options-vol ≥2×" read is
  not computable from it; treat the 96.4 pctile as a *relative* elevation signal, not
  a literal ≥2× confirmation.
- **IV-rank (high screen):** HOOD **outside top-50** — IV is not elevated (rank 32.4).

### Sector read

Technology dominates today's bullish tape — **17 of the top-50** net-bullish names
are UW-sector "Technology" (semis HPE/MU/NVDA/AMD/AVGO/MRVL/CRM leading), plus ~14
index ETFs ("n/a" sector). UW classifies **HOOD itself as "Technology"**, so on UW's
taxonomy the name's sector *is leading* the directional tape today — a cross-sectional
tailwind. (Caveat for phase-6: HOOD is economically a fintech/Financial Services
broker; Finviz classifies it Financials. The "tech leadership = HOOD tailwind" read
holds only under UW's taxonomy — phase-6 should resolve whether the fintech/broker
cohort, not semis, is the right comp.)

### Self-history (DuckDB §C, 46 sessions present locally)

- `self_pctile_net_dir` = **84.4** — today is more net-bullish than ~84% of HOOD's
  own recent sessions.
- `self_pctile_total` = **93.3** — today is among the name's busiest premium days.
- `sessions_in_window` = **46** (true N; recent window contiguous trading days).

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq`/SQL path | Rows used |
|------------------|------------------------------|-----------|
| `uw screener bullish-bearish --direction bullish --top-n 50 --date 2026-06-15 --json` | HOOD rank=32 ← `[.results[].ticker]\|index("HOOD")+1`; net_flow=+$8.68M ← `.results[]\|select(.ticker=="HOOD").net_flow` | top-50 |
| `uw screener bullish-bearish --direction bearish --top-n 50 …` | HOOD outside top-50 | top-50 |
| `uw screener volume-vs-average --min-volume-ratio 2 --top-n 50 …` | HOOD outside top-50 | top-50 |
| `uw screener iv-rank --mode high --top-n 50 …` | HOOD outside top-50 | top-50 |
| `uw insights deep-dive --symbol HOOD --date 2026-06-15 --json` | call_prem=$197.9M, put_prem=$35.2M, PCR=0.346, iv_rank=32.4, implied_move_perc=4.65% ← `.uw_screener.*` | 1 name |
| DuckDB §C `stock-screener-2026-06-15.parquet` (+46-file glob) | universe pctile total=99.4/net_dir=99.5/iv=40.8/vol=96.4 (N=4754); self net_dir=84.4/total=93.3 (N=46); net_call=$10.06M, net_put=$1.38M | universe + self |

## Tool errors

(none — initial DuckDB run hit a `close` reserved-word parser error; re-run with
`"close"` quoted succeeded. No value transcribed from the failed run.)

## DATA NOTE / CORRECTION

- `avg30_volume` in the screener parquet is the underlying's *share* avg volume, not
  options volume; the raw vol_x (0.02) is therefore apples-to-oranges. The 96.4th
  *percentile* (same field across all names) remains a valid relative rank and is what
  is reported. The absolute "≥2× options volume" GENUINELY_UNUSUAL sub-criterion could
  not be literally verified from this field.

## Verdict for downstream phases

```
universe_pctile_total_prem:  99.4
universe_rank_net_dir:       32          # of top-50 leaderboard; = 99.5 universe pctile
sector_leadership:           Technology is LEADING today (UW taxonomy; HOOD tagged Technology) — but verify fintech-broker comp in phase-6
iv_rank:                     32.4        # 40.8 universe pctile — mid/low
implied_move_pct:            4.65        # ±$4.55 on $98.12 close — feeds phase-9 N4
self_pctile_net_dir:         84.4
unusual_verdict:             GENUINELY_UNUSUAL
```

- **Bias from this phase:** neutral (context only — no directional bias set here).
- **Conviction:** n/a (context phase).
- **Three things later phases should remember:**
  1. The flow is genuinely top-decile (99.4/99.5 universe, 84.4/93.3 self) — but the
     *net dollars* ($8.68M) are modest vs the day's giants; do **not** let raw
     magnitude alone drive ++ confluence. Gross premium $233M is two-sided.
  2. Directional tilt is decisively **call-side** (net call $10.06M vs net put $1.38M,
     PCR 0.346) — the bullish read is in the call/put skew, not the net-premium size.
  3. IV rank is mid/low (32.4) — premium-selling structures less attractive; cheap
     optionality for premium buyers. Implied move ±4.65%.
- **Open questions:** Is HOOD's true comp the leading semis/tech cohort (UW taxonomy)
  or the fintech-broker complex (phase-6 to resolve)? Is the $96 put with vol/OI 242
  (phase-0) a hedge or a directional bet (phase-1 to resolve)?
```
