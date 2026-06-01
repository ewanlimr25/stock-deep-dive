# Phase 1 — Options Flow

## Goal

Read today's options tape for `<SYMBOL>`: who's buying what, how aggressively,
and at what conviction. Emit `phase-1-flow.md`.

## Tools (call all; surface errors verbatim, do not skip)

All ticker-scoped (pass `--symbol <SYMBOL>` and `--date <AS-OF>` if not today).
Cap `--top-n` at 25 to keep output readable. All commands take `--json`.
For the two ask/bid sweep reads, call `uw options-flow sweeps` once per `--side`.

| Command | What it answers |
|---------|-----------------|
| `uw options-flow sweeps --symbol <S> --side ask\|bid --min-premium 100000 --top-n 25 --json` | Aggressive ask/bid-side sweeps (run both sides) |
| `uw options-flow unusual-volume --symbol <S> --min-vol-oi-ratio 3 --top-n 25 --json` | New positions opening (vol >> OI) |
| `uw options-flow top-premium-trades --symbol <S> --top-n 25 --json` | Largest single-trade premium bets |
| `uw options-flow iv-outliers --symbol <S> --top-n 15 --json` | Unusually high-IV contracts |
| `uw options-flow greek-screener --symbol <S> --top-n 15 --sort-by premium --json` | Delta/gamma/vega-filtered tape |
| `uw hot-chains smart-money-flow --direction bullish\|bearish --top-n 10 --min-volume 500 --json` | Ask vs bid imbalance (run both directions) |
| `uw hot-chains sweep-persistence --days 5 --top-n 20 --symbol <S> --json` | Multi-day sweep campaigns |
| `uw hot-chains sweep-ratio --top-n 15 --min-volume 500 --min-sweep-ratio 0.3 --json` | Aggressive-sweep ratio |
| `uw insights deep-dive --symbol <SYMBOL> [--date D] --json` | **Whole-tape aggregate** — the `uw_screener` block: `call_premium`, `put_premium`, `bullish_premium`, `bearish_premium`, `put_call_ratio`, `call_volume`, `put_volume`, `implied_move`/`implied_move_perc`, `iv_rank`. **No `net_flow` field here — derive `net_flow = bullish_premium − bearish_premium`** (or read the real `net_flow` from `screener bullish-bearish` `.results[]`). The block carries `call_volume`/`put_volume`, **not** ask/bid volume — for ask-vs-bid use the `sweeps` / `smart-money-flow` tools above |

## Whole-tape aggregate first (do NOT read direction off top-N alone)

The ranked tools above return the **top-N prints — the tip of the iceberg** (audit
2026-05-25 `§3`: the top-25 AAPL prints were only ~30% of the day's premium, and
read "clean bullish" while the whole tape was near-balanced). **Before interpreting
the top prints, state the whole-tape aggregate** from `insights_deep_dive`'s
`uw_screener` block (the same screener data phase-7 / phase-0.5 use):
- call vs put premium, `bullish_premium` vs `bearish_premium`, **derived
  `net_flow = bullish_premium − bearish_premium`** (the block has no `net_flow` key),
  `call_volume` vs `put_volume`, P/C ratio (`put_call_ratio`). Ask-vs-bid is
  per-contract in `sweeps`/`smart-money-flow`, not in this whole-tape block.

Then read the top-N prints *against* that aggregate: a single huge ask-side LEAP on
top of a near-balanced tape is one print, not a one-sided tape — say so. Carry
`[CTX:]` from phase-0.5: if `unusual_verdict = BUSY_NAME_NORMAL_DAY`, discount the
magnitude and cap this phase's downstream conviction (phases 1–2 capped at `+`,
`rubrics/confluence-scoring.md`).

> When the CLI top-N view and the aggregate disagree and you need the directional
> read **stripped of 0DTE pin noise** or in **delta-notional** terms, that exact cut
> is the DuckDB escape hatch `lib/duckdb-cuts.md §A` (tag `[FLOW:… DUCKDB]`). Optional;
> only when the snapshot exists and the standard view is ambiguous.

## Composition guidance

- `uw hot-chains` commands are MARKET-WIDE; filter the returned rows to
  `<SYMBOL>` after the call. If a command exposes a `--symbol` filter (e.g.
  `sweep-persistence`), use it.
- If `uw hot-chains smart-money-flow` returns no rows for `<SYMBOL>`, note "no
  smart-money flow detected on this date" — do NOT call it again with looser
  thresholds.

## Output sections (follow templates/phase-N-template.md)

1. **Summary** — 3 sentences: net bias, premium magnitude, persistence.
2. **Key signals** — bulleted top-5 with `[FLOW:<tool>]` citations.
3. **Detailed findings**
   - ### Whole-tape aggregate (call vs put premium, bullish vs bearish premium,
     derived net_flow, call vs put volume, P/C) — `[FLOW:insights_deep_dive]`; the top-N
     below is read against this
   - ### Sweeps (ask vs bid, premium, persistence)
   - ### New positioning (unusual vol, vol/OI ratio)
   - ### Largest premium prints (table: time, strike, expiry, premium, side)
   - ### IV outliers + Greeks
4. **Tool calls** — audit table with every tool + args summary.
5. **Tool errors** — verbatim.
6. **Verdict for downstream**
   - Net bias (bullish / bearish / mixed)
   - Conviction 1–5 based on premium magnitude + persistence
   - Three datapoints later phases must remember
   - Open questions (e.g. "is dark pool confirming this premium?")

## Interpretation heuristics

- **Bullish flow signature:** ask-side calls + ratio ≥ 0.6 in smart_money_flow
  + sweeps persisting ≥ 2 sessions in sweep_persistence.
- **Bearish flow signature:** bid-side puts + smart_money ratio ≤ 0.4 + IV
  outliers concentrated in OTM puts.
- **Hedging signature:** premium > $1M concentrated in single ATM put strikes
  near earnings/ex-div — call it out as "hedging, not directional intent".

## Common pitfalls

- 0DTE-heavy flow inflates premium counts; tag and discount.
- LEAP-heavy flow (>180 DTE) is institutional but slow — note conviction but
  short-term tradeability is low.
- Sector ETFs (SPY, QQQ) have so much flow that ranking by premium alone
  buries signal — also sort by sweep_ratio.
