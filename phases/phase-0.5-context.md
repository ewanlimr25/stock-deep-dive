# Phase 0.5 — Cross-Sectional & Self-History Context

## Goal

Before reading the single name's tape in detail, answer the question every desk
asks first: **is this flow actually unusual — for this name, and versus the rest
of the market today — or is it a busy name having a normal day?** A 99th-percentile
*size* day on a perpetually-active mega-cap is not the same signal as the same
dollars on a name that never trades options. Seed every downstream phase with that
context so conviction is calibrated to genuine unusualness, not raw magnitude.
Emit `phase-0.5-context.md`.

> **Why this phase exists (audit 2026-05-25, `docs/audit/2026-05-25/06`).** The skill
> read a single name in isolation and could mistake "big flow on a name that always
> has big flow" for a signal. The ranking below is one `uw screener` call the skill
> previously never made for the single name. (Worked example: AAPL 2026-05-20 ranked
> ~17th on net bullish flow behind AMD/MU/SNDK/INTC — semis led the tape, AAPL was not
> a top directional name — a fact invisible to a single-name-only read.)

## Tools (`uw` CLI — primary path)

The `uw screener` commands are MARKET-WIDE rankings sourced from the same screener
data `uw insights deep-dive` returns per-name. Call with a generous `--top-n` so
`<SYMBOL>` falls inside the returned list; if it does not, the name is outside the
top of that metric (record "outside top-N on <metric>"). All commands take `--json`.

| Command | What it answers |
|---------|-----------------|
| `uw screener bullish-bearish --direction bullish --top-n 50 [--date D] --json` | Where `<SYMBOL>` ranks on net bullish premium today; which names lead |
| `uw screener bullish-bearish --direction bearish --top-n 50 [--date D] --json` | Same for net bearish premium |
| `uw screener volume-vs-average --min-volume-ratio 2 --top-n 50 [--date D] --json` | Is today's option volume unusual vs the name's 30-day average |
| `uw screener iv-rank --mode high\|low --top-n 50 [--date D] --json` | Where the name's IV rank sits in the universe |
| `uw insights deep-dive --symbol <SYMBOL> [--date D] --json` | The name's own `uw_screener` block — bullish/bearish/call/put premium, `put_call_ratio`, `iv_rank`, `implied_move`/`implied_move_perc` (the absolute numbers behind the rank). **`net_flow` is NOT in this block** — read it from `screener bullish-bearish` `.results[]` (row where `ticker == <SYMBOL>`) or derive `bullish_premium − bearish_premium` |

## Optional precise percentile (DuckDB escape hatch — `lib/duckdb-cuts.md` §C)

The CLI returns *ranked top-N*, not an exact percentile or a self-history series.
If the local screener parquet for the as-of date exists
(`~/Documents/Stocks/Stock Screener/stock-screener-<DATE>.parquet`; `STOCKS_DIR`
overridable), run `lib/duckdb-cuts.md §C` for:
- the name's **exact universe percentile** (total premium, net-directional premium,
  IV rank, volume-vs-average) across all ~6,171 names, and
- its **self-history percentile** (today vs the name's own ≤31-session distribution).

This is purely additive — it sharpens the verdict. If the parquet is absent (live
run beyond the snapshot, or `STOCKS_DIR` unset), skip it and rank from the CLI
lists alone; say so in the `## Source` line.

## Output sections

1. **Summary** — one paragraph: is the flow genuinely unusual, and how does the name
   rank against the universe + its sector today.
2. **Universe ranking** — the name's rank on net bullish/bearish premium and
   volume-vs-average; name the 3–5 leaders (sector-leadership read).
3. **Sector read** — which sector leads today's directional tape; is `<SYMBOL>`'s
   sector in or out of favour (hands the macro phase a head start).
4. **Self-history** (if parquet present) — today's premium / net-direction /
   P-C / IV rank percentile vs the name's own recent sessions.
5. **Source** — CLI-only or CLI+DuckDB; note any "outside top-N" metrics.
6. **Verdict for downstream** — the `[CTX:]` block (phases 1, 5, 9 read it verbatim):
   ```
   universe_pctile_total_prem:  <0–100 or null>   # null if CLI-rank-only
   universe_rank_net_dir:       <integer rank, or "outside top-50">
   sector_leadership:           <SECTOR is leading | lagging | mid-pack today>
   iv_rank:                     <0–100>            # from insights_deep_dive
   implied_move_pct:            <%>                # feeds phase-9 expected-move (N4)
   self_pctile_net_dir:         <0–100 or null>    # null if parquet absent
   unusual_verdict:  GENUINELY_UNUSUAL | BUSY_NAME_NORMAL_DAY | QUIET
   ```

## Interpretation heuristics

- **GENUINELY_UNUSUAL** = top-decile (or rank ≤ ~25) on net-directional premium
  *and* volume-vs-average ≥ 2 *and* (if available) self_pctile_net_dir ≥ 80. The
  flow is unusual both cross-sectionally and for the name.
- **BUSY_NAME_NORMAL_DAY** = high *absolute* premium but mid-pack universe rank
  and/or self_pctile < 60. Big numbers, normal day. **Phases 1–2 confluence is
  capped at `+` (not `++`) when this fires** (`rubrics/confluence-scoring.md`).
- **QUIET** = thin on both axes — flag low tradeability; downstream conviction
  should stay low regardless of how clean a single print looks.
- A name leading its sector while the sector leads the tape is the strongest
  cross-sectional confirmation; the reverse (name strong, sector being sold) is a
  yellow flag for phase-6 to resolve.

## Common pitfalls

- Index/sector ETFs (SPY, QQQ, SPXW) dominate every premium ranking — when
  `<SYMBOL>` is a single name, read its rank *among single names*, mentally setting
  the ETFs aside.
- `net_flow` in `screener_bullish_bearish` is bullish−bearish premium; do not
  confuse it with `net_call_premium`.
- "Outside top-50" is information, not an error — it means the name is not among
  the day's leaders on that metric; record it and move on.
- This phase establishes *context only* — it sets no directional bias. The bias is
  the plurality of phases 1–8.
