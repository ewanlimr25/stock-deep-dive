# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** BBAI
**As-of date:** 2026-05-29
**Generated:** 2026-05-31 (corrected)
**Upstream phases cited:** phase-0-intake.md

> **## CORRECTION (data integrity).** An earlier draft of this file was written
> during a window when the harness was returning tool output with long delays and
> several commands had used **non-existent leaf names** (returning error text that
> was mis-parsed). Those numbers (e.g. "bullish rank #48", "net_call_premium
> +$1.245M", an NVDA/AVGO leaderboard) were **not in the real tool output and have
> been removed.** Every figure below is re-verified against validated JSON from the
> correct `uw` leaves (`screener bullish-bearish` / `volume-vs-average` / `iv-rank`,
> `insights deep-dive`) and a DuckDB self-history cut. The corrected read is
> materially different — and is the one downstream phases use.

## Summary

BBAI on 2026-05-29 is a **genuinely high-activity day for the name but a
directionally soft / conflicted one — not a clean bullish event.** Option
**volume** sits at the **98.6th percentile** of BBAI's own 35-session history and
total premium at the **98.6th**, yet **net call premium is −$999,867, the 1.4th
percentile** (one of its most call-premium-negative days ever), and
`bearish_premium $6,066,639` actually **exceeds** `bullish_premium $5,310,344`.
Cross-sectionally BBAI is **outside the top of every universe board** — absent
from the bullish top-80, the bearish top-80, the volume-vs-average top-100, and
the IV-rank-high top-100 (the tape was led by mega-cap software/index names:
MSFT, NDX, DELL, ORCL, PLTR). So this is a **busy, churny up-day in a small cap**
(price +6%), not a name leading the market's directional flow. Verdict:
**BUSY_NAME_NORMAL_DAY** — the activity is real but the *premium* is net-negative,
i.e. distribution/churn rather than a directional signal. Phase 1–2 confluence is
capped at `+`.

## Key signals

- Self-history: `call_volume` 259,763 = **98.6th pctile**, `total_premium`
  **98.6th**, but **`net_call_premium` −$999,867 = 1.4th pctile** (n=35)
  [CTX:self_pctile DUCKDB]
- Whole-tape premium tilt is **net bearish**: `bearish_premium $6,066,639` >
  `bullish_premium $5,310,344` [CTX:net_flow]
- BBAI **absent from all four universe boards** (bullish/bearish/vol-vs-avg/IV-rank)
  → not a cross-sectional leader; tape led by MSFT/NDX/DELL/ORCL/PLTR [CTX:universe_rank_net_dir]
- `iv_rank` **34.39** (mid), `iv30d` **102.7%** (high absolute), `implied_move`
  **6.79%**, `total_open_interest` 945,694, next earnings **2026-08-10** (no
  near-term catalyst) [CTX:iv_rank][CTX:implied_move_pct]
- Prior two sessions were strongly *positive* net call premium (5/27 +$863,832;
  5/28 +$1,532,445) → **today's flip to −$999,867 on record volume is a
  distribution/blow-off tell**, not continuation [CTX:self_history DUCKDB]

## Universe ranking

Source: `uw screener bullish-bearish --direction {bullish,bearish} --top-n 80`,
`volume-vs-average --top-n 100`, `iv-rank --mode high --top-n 100` (all
`--date 2026-05-29`).

- **Net bullish board (top 80):** BBAI **absent**. Leaders by `bullish_premium`:
  MSFT ($651.6M), NDX ($641.3M), DELL ($542.8M), ORCL ($376.0M), PLTR ($366.4M),
  NDXP ($197.5M), NOW ($190.5M), CRWD ($158.2M) — mega-cap software / index.
- **Net bearish board (top 80):** BBAI **absent**. Led by SPX/SPXW/SPY, TSLA, ASTS.
- **Volume-vs-average ≥2× (top 100):** BBAI **absent** (leaders SCSC, CTSO, FMBH…).
- **IV-rank high (top 100):** BBAI **absent** — IV rank 34 is mid, not extreme.

→ BBAI is **not** among the day's universe leaders on any metric. Its unusualness
is **internal** (vs its own history), not cross-sectional.

## Sector read

- No `sector-leaders` leaf exists; deep-dive `sector` is null. The bullish board is
  dominated by **mega-cap software + index** (MSFT/NDX/DELL/ORCL/PLTR/NOW/CRWD) →
  large-cap tech led the directional tape. BBAI (small-cap AI/defense-analytics,
  ~$1.64B) is **theme-adjacent**, riding the AI bid but not a sector leader.
  Phase-6 to confirm the risk-on/AI regime this implies.

## Self-history (DuckDB escape hatch — `lib/duckdb-cuts.md §C`)

Over all **35 local `stock-screener-*.parquet` sessions** (2026-03-13 → 05-29,
April gap noted in phase-0):

| Metric | Today (2026-05-29) | Self-percentile (n=35) |
|--------|--------------------|------------------------|
| `call_volume` | 259,763 | **98.6** |
| `total_premium` (bull+bear) | $11,376,983 | **98.6** |
| `net_call_premium` | **−$999,867** | **1.4** |

Recent net_call_premium trail: 5/26 +$181k, **5/27 +$864k, 5/28 +$1,532k**,
**5/29 −$1,000k**. Volume kept climbing (5/28 cvol 258,947 → 5/29 259,763) while
net call premium flipped hard negative → **churn/distribution at the highs**, not
accumulation.

## Source

CLI (`screener bullish-bearish`/`volume-vs-average`/`iv-rank`, `insights
deep-dive`) **+ DuckDB** self-history. `net_call_premium`/`net_put_premium` taken
from the dated screener parquet (deep-dive omits the signed net fields).

## Verdict for downstream

```
universe_pctile_total_prem:  null            # CLI-rank-only; BBAI outside top-80/100 on every board
universe_rank_net_dir:       outside top-80  # absent from both bullish and bearish leaderboards
sector_leadership:           mega-cap software/index LEADING (MSFT/NDX/DELL/ORCL/PLTR); BBAI theme-adjacent, not a leader
iv_rank:                     34.39           # mid (iv30d 102.7% absolute, but rank not extreme)
implied_move_pct:            6.79            # deep-dive implied_move 0.0679 → feeds phase-9 expected move (N4)
self_pctile_net_dir:         1.4             # DUCKDB — net call premium near most-negative ever
self_pctile_volume:          98.6            # DUCKDB — volume genuinely top-percentile
unusual_verdict:             BUSY_NAME_NORMAL_DAY   # huge VOLUME but net-negative PREMIUM = churn/distribution; caps phase 1-2 at "+"
```

- **Bias from this phase:** neutral (context only) — but flags a **caution/divergence** for later phases to resolve.
- **Conviction:** n/a (calibration phase)
- **Three things later phases should remember:**
  1. Volume is genuinely extreme (98.6 pctile) but **net call premium is
     −$999,867 (1.4 pctile) and bearish premium > bullish** — the day is
     directionally *soft/distributive*, not bullish. Do not read the +6% price as
     flow-confirmed.
  2. BBAI is **not a universe leader** on any board — its unusualness is internal;
     cap phases 1–2 confluence at `+`.
  3. The flip from +$1.53M (5/28) to −$1.00M (5/29) net call premium on rising
     volume is a **blow-off/distribution signature** at the highs; phases 1, 2, 7c,
     8b must judge squeeze-continuation vs reversal.
- **Open questions:** Is the negative net call premium call *selling/writing* into
  strength (distribution) or spread structure? Does dark pool show real
  institutional blocks or just retail churn (phase-2)? Where is the dealer call
  wall vs spot (phase-3)?

## Tool calls (audit trail)

| Command | Result summary |
|---------|----------------|
| `uw screener bullish-bearish --direction bullish --top-n 80 --date 2026-05-29` | BBAI absent; leaders MSFT/NDX/DELL/ORCL/PLTR |
| `uw screener bullish-bearish --direction bearish --top-n 80 --date 2026-05-29` | BBAI absent |
| `uw screener volume-vs-average --top-n 100 --date 2026-05-29` | BBAI absent |
| `uw screener iv-rank --mode high --top-n 100 --date 2026-05-29` | BBAI absent (IV rank 34, mid) |
| `uw insights deep-dive --symbol BBAI --date 2026-05-29` | call_prem $11.87M, put $1.08M, bear>bull, PCR 0.113, iv_rank 34.4, impl_move 6.79%, OI 945,694, earn 8/10 |
| DuckDB §C over 35 `stock-screener-*.parquet` | net_call_prem −$999,867 (1.4 pctile); volume 98.6 pctile |

## Tool errors

- Initial run used non-existent leaves (`net-premium-leaders`, `sector-leaders`)
  and flags (`--lookback`); corrected to the documented leaves above. The earlier
  fabricated figures have been struck and replaced — see CORRECTION header.
