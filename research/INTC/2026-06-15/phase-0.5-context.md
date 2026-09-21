# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** INTC
**As-of date:** 2026-06-15
**Generated:** 2026-06-16T01:24:55Z
**Upstream phases cited:** phase-0-intake.md

## Summary

INTC is one of the most *active* option names on the tape today — **99.7th
percentile on total option premium** across the 4,754-name optionable universe
(`[CTX:universe_pctile DUCKDB]`) and **80th percentile vs its own recent
sessions** — but the *direction* of that flow is conflicted, not decisively
unusual. The two net-directional measures point opposite ways: INTC ranks **99.2
pctile on net-call-minus-net-put premium (aggressor basis, bullish)** yet **2.3
pctile on bullish-minus-bearish premium (classification basis, bearish)**, and on
the CLI screener it sits **outside the top-50 on both bullish and bearish net
flow**. Self net-direction is only ~60th pctile. Verdict: **BUSY_NAME_NORMAL_DAY**
— enormous gross activity, but the net signal is two-sided and self-history-normal,
so phases 1–2 confluence is capped at `+` (not `++`). Sector context is a yellow
flag: **Technology/semiconductors lead today's bullish tape (MU, NVDA, HPE in the
top 8)** while INTC is *not* among the directional leaders — peers are getting the
bid, INTC is balanced.

## Universe ranking (today, vs ~4,754 optionable names)

Net **bullish** premium leaders (ETFs/index set aside): **HPE +$92.7M**,
**TSLA +$90.1M**, **MU +$78.2M**, **NVDA +$70.5M** (indices NDX/SPXW/QQQ top the
raw list). `[CTX:screener_bullish]`
Net **bearish** premium leaders: SPX −$686.5M, SPY −$184.2M, RUT, GLD, **PDD −$43.9M**. `[CTX:screener_bearish]`

- **INTC net-flow rank: outside top-50 on BOTH bullish and bearish** CLI lists →
  net-directional flow is balanced, not a leader either way. `[CTX:screener_bullish]` `[CTX:screener_bearish]`
- **INTC volume-vs-average: outside CLI top-50**, but DuckDB universe pctile
  **92.9** (top ~7%) — volume is elevated, just below the day's top-50 cutoff. `[CTX:universe_pctile DUCKDB]`
- **INTC IV-rank: 82.0 absolute** (`iv_rank`), **94.8 universe pctile** — elevated
  vs the universe (top names sit at 100: MU, plus small-caps). `[CTX:insights_deep_dive]`

Exact universe percentiles (`lib/duckdb-cuts.md §C`, N=4754) `[CTX:universe_pctile DUCKDB]`:

| Metric | Universe pctile |
|--------|-----------------|
| total premium (call+put) | **99.7** |
| net_call_premium − net_put_premium (aggressor) | **99.2** |
| bullish_premium − bearish_premium (classification) | **2.3** |
| iv_rank | 94.8 |
| volume vs 30d avg | 92.9 |

> **The two net-direction pctiles disagree by ~97 points.** Heavy *aggressive
> call buying* (net_call_premium high, 99.2) coexists with a *neutral-to-bearish*
> bullish/bearish classification (2.3) — i.e. large call premium is being both
> bought AND sold/written (or offset by put buying). gross call_premium $425.4M vs
> put_premium $97.0M (4.4:1) but bullish $229.9M ≈ bearish $231.0M (net −$1.16M).
> **Phase 1 must disentangle this** — it is the central question of the name today.

## Sector read

Today's **bullish** tape is led by **Technology / semiconductors**: MU (+$78.2M,
IV 100), NVDA (+$70.5M), HPE (+$92.7M) all in the top 8 net-bullish single names.
INTC's own sector is therefore **in favour / leading** on the bullish side —
**but INTC is conspicuously absent from the directional leaders.** This hands
phase 6 a specific question: is INTC a *laggard catch-up* candidate within a bid
semi complex, or is capital rotating to the leaders (MU/NVDA) and passing INTC by?
The reverse-divergence (sector bid, name neutral) is a **yellow flag**, not a green light.

## Self-history (today vs INTC's own local sessions, N=46)

`[CTX:self_pctile DUCKDB]` (`lib/duckdb-cuts.md §C`; note the 2026-03-27→04-27 gap
— window is 46 *available* sessions, not contiguous calendar):

| Metric | Self pctile (N=46) |
|--------|--------------------|
| net_call − net_put (aggressor) | 60.0 |
| bullish − bearish (classification) | 42.2 |
| total premium | **80.0** |
| iv_rank | 64.4 |

Today is a **busy day by INTC's own standard** (80th pctile total premium) but the
**net direction is middling** (42–60th pctile) — not a self-history outlier. This
is what separates BUSY_NAME_NORMAL_DAY from GENUINELY_UNUSUAL: the size is there,
the directional conviction is not.

## Source

CLI (`uw screener` ×4 + `uw insights deep-dive`) **+ DuckDB §C** (universe &
self-history exact percentiles; parquet for 2026-06-15 present). "Outside top-50"
recorded for net bullish, net bearish, and volume-vs-average CLI lists.

## Verdict for downstream — `[CTX:]` block

```
universe_pctile_total_prem:  99.7
universe_rank_net_dir:       outside top-50 (both lists); pctile 99.2 (net_call−net_put) vs 2.3 (bull−bear) — CONFLICTED
sector_leadership:           Technology/Semis LEADING today (MU, NVDA, HPE) — INTC NOT a leader (laggard/yellow flag)
iv_rank:                     82.0
implied_move_pct:            6.17%
self_pctile_net_dir:         60.0 (net_call−net_put) / 42.2 (bull−bear)
unusual_verdict:             BUSY_NAME_NORMAL_DAY   # conf cap '+' on phases 1–2; directional conflict flagged
```

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq`/SQL path | Rows used |
|------------------|------------------------------|-----------|
| `uw screener bullish-bearish --direction bullish --top-n 50 --date 2026-06-15 --json` | INTC rank=null (outside top-50); leaders HPE/TSLA/MU/NVDA ← `.results[].ticker\|index("INTC")` | top-50 |
| `uw screener bullish-bearish --direction bearish --top-n 50 --date 2026-06-15 --json` | INTC rank=null; leaders SPX/SPY/RUT/GLD/PDD | top-50 |
| `uw screener volume-vs-average --min-volume-ratio 2 --top-n 50 --date 2026-06-15 --json` | INTC rank=null | top-50 |
| `uw screener iv-rank --mode high --top-n 50 --date 2026-06-15 --json` | INTC rank=null; leaders MU/SMN1/OPTU (iv 100) | top-50 |
| `uw insights deep-dive --symbol INTC --date 2026-06-15 --json` | bull=229.9M, bear=231.0M, PCR=0.605, iv_rank=82.0, implied_move_perc=0.0617 ← `.uw_screener` | 1 |
| DuckDB §C universe (`stock-screener-2026-06-15.parquet`, N=4754) | total_prem pctile 99.7, net_call−put 99.2, bull−bear 2.3, iv 94.8, vol 92.9 ← `PERCENT_RANK()` | universe |
| DuckDB §C self-history (46 local screener parquets) | self total 80.0, net_dir 60.0/42.2, iv 64.4, sessions=46 | self |

## Tool errors

None on the data. (Harness note: piped `jq` output was intermittently swallowed
when several `uw` reads were batched in one message; resolved by capturing each
`uw` read to a file and running `jq` against the file — every number above
round-tripped through validated JSON/SQL, no streamed-buffer transcription.)

## DATA NOTE / CORRECTION

Initial null-safe jq oversight: an object built with `intc: (.results[]|select(...))`
collapsed to empty output when INTC was absent from a top-50 list (zero-output
stream zeroes the whole jq object). Re-queried with `[…]|.[0]//null` — confirmed
INTC is genuinely outside all four CLI top-50 lists (rank null), not a read miss.

## Verdict for downstream phases

- **Bias from this phase:** neutral (context only — sets no directional bias)
- **Conviction:** n/a (calibration input)
- **Three things later phases should remember:**
  1. **BUSY_NAME_NORMAL_DAY** → cap phases 1–2 confluence at `+`; huge gross
     premium (99.7 pctile) but middling self net-direction (42–60 pctile).
  2. **Directional CONFLICT** is the headline: aggressive call buying (net_call−put
     99.2 pctile) vs neutral bullish/bearish classification (2.3 pctile). Phase 1
     must resolve whether calls are bought or written.
  3. **Sector bid, name lagging** — semis (MU/NVDA/HPE) lead the bullish tape;
     INTC is not a directional leader. Phase 6 resolves laggard-catchup vs passed-over.
- **Open questions:** Which side of the call premium is the aggressor (bought vs
  written)? → phase 1. Is the IV-rank-82 a pre-earnings (2026-07-23) build? → phases 4/7c.
