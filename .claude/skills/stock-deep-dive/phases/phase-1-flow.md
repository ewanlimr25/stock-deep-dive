# Phase 1 — Options Flow

## Goal

Read today's options tape for `<SYMBOL>`: who's buying what, how aggressively,
and at what conviction. Emit `phase-1-flow.md`.

## Tools (call all; surface errors verbatim, do not skip)

All ticker-scoped (pass `symbol=<SYMBOL>` and `date=<AS-OF>` if not today).
Cap `top_n` at 25 to keep output readable.

| Tool | Args | What it answers |
|------|------|-----------------|
| `mcp__uw-pp__options_flow_sweeps` | symbol, side (both), min_premium=100000, top_n=25 | Aggressive ask/bid-side sweeps |
| `mcp__uw-pp__options_flow_unusual_volume` | symbol, min_vol_oi_ratio=3, top_n=25 | New positions opening (vol >> OI) |
| `mcp__uw-pp__options_flow_top_premium_trades` | symbol, top_n=25 | Largest single-trade premium bets |
| `mcp__uw-pp__options_flow_iv_outliers` | symbol, top_n=15 | Unusually high-IV contracts |
| `mcp__uw-pp__options_flow_greek_screener` | symbol, top_n=15, sort_by=premium | Delta/gamma/vega-filtered tape |
| `mcp__uw-pp__hot_chains_smart_money_flow` | direction=both, top_n=10, min_volume=500 | Ask vs bid imbalance |
| `mcp__uw-pp__hot_chains_sweep_persistence` | days=5, top_n=20, symbol | Multi-day sweep campaigns |
| `mcp__uw-pp__hot_chains_sweep_ratio` | top_n=15, min_volume=500, min_sweep_ratio=0.3 | Aggressive-sweep ratio |

## Composition guidance

- `hot_chains_*` tools are MARKET-WIDE; filter the returned rows to
  `<SYMBOL>` after the call. If a tool exposes a `symbol` filter (e.g.
  `sweep_persistence`), use it.
- If `smart_money_flow` returns no rows for `<SYMBOL>`, note "no smart-money
  flow detected on this date" — do NOT call it again with looser thresholds.

## Output sections (follow templates/phase-N-template.md)

1. **Summary** — 3 sentences: net bias, premium magnitude, persistence.
2. **Key signals** — bulleted top-5 with `[FLOW:<tool>]` citations.
3. **Detailed findings**
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
