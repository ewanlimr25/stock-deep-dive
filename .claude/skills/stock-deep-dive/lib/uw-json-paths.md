# uw / fz JSON path map (validated 2026-06-01 @ data date 2026-05-29)

Authoritative wrapper-key + field-path map for the tools the phases read. Cite
this instead of re-discovering shape at runtime. Every number a phase writes must
trace to a `jq` path here (SKILL.md Orchestration rule 0 — JSON-validity gate).
Validated against live output in `docs/audit/2026-06-01/03-evidence-appendix.md`.

> Two phantom-field traps this map exists to prevent:
> - `insights deep-dive .uw_screener` has **NO `net_flow`** and **NO ask/bid
>   volume** → derive `net_flow = bullish_premium − bearish_premium`
>   (validated `exact_match=true` vs the real `net_flow` field).
> - `dark-pool block-stratified` has **NO `sell_ratio`**; only `buy_ratio`, nested
>   per tier → derive `sell_ratio = 1 − buy_ratio`.

## screener
```
bullish-bearish   {direction, results[], source}
  results[]       ticker, net_flow, bullish_premium, bearish_premium, call_volume,
                  put_volume, iv_rank, put_call_ratio, close, sector, full_name
                  # net_flow == bullish_premium − bearish_premium (exact)
volume-vs-average {results[]: ticker, ...}
iv-rank           {results[]: ticker, ...}        # --mode high|low
```

## insights
```
deep-dive         {symbol, uw_screener{}, uw_dark_pool{}, uw_top_oi_changes, yahoo_fundamentals}
  .uw_screener    call_premium, put_premium, bullish_premium, bearish_premium,
                  call_volume, put_volume, put_call_ratio, iv_rank, iv30d,
                  implied_move, implied_move_perc, total_open_interest, volatility,
                  next_earnings_date
                  ✗ NO net_flow · NO ask/bid volume → net_flow := bullish−bearish
signal-confluence {results[]: ticker, score, factors, net_flow, iv_rank,
                  put_call_ratio, volume_ratio, ...}              # market-wide
conviction-matrix {scenario, confidence_pct, dark_pool, options_flow, thresholds}
price-vs-flow     {divergence, divergence_signal, flow_direction, net_premium_flow,
                  bullish_premium, bearish_premium, put_call_ratio, ...}
institutional-accumulation {signal, buy_sell_ratio, buy_side_volume, sell_side_volume,
                  total_dp_premium, vwap, top_price_levels, ...}
analyst-vs-flow   {symbol, options_flow, ...}     # analyst block can be empty/thin
```

## options-flow
```
sweeps            {results[]: ...}                # --side ask|bid
unusual-volume    {results[]: ...}                # --min-vol-oi-ratio
sector-flow       {results[]: sector, net_flow, total_premium_call, total_premium_put,
                  total_volume_call, total_volume_put}
sector-flow-persistence {results[]: sector, net_flow_by_day, persistence_score, trend}
```

## dark-pool
```
largest           {results[]: executed_at, price, size, premium, nbbo_ask, nbbo_bid,
                  nbbo_mid, trade_vs_mid, ticker}
block-stratified  {caveat, results[], source}
  results[]       ticker, highest_tier, total_premium_all_tiers,
                  mega{buy_ratio, buy_volume, sell_volume, total_premium, trade_count},
                  large{…}, block{…}, retail{…}
                  ✗ NO sell_ratio → sell_ratio := 1 − buy_ratio
ticker-summary    {results[]: ticker, total_premium, total_shares, avg_price,
                  max_single_trade, trade_count}
price-levels      {dates_covered, results[]: price_level, total_premium, total_shares,
                  trade_count}                    # --days latest-anchored
```

## oi
```
oi-by-strike      {symbol, spot, caveat, dte_max, results[], source}
  results[]       strike, call_oi, put_oi, net_oi, total_oi, role, distance_pct
                  role ∈ call_wall_resistance | put_wall_support | call_heavy | put_heavy
term-structure    {symbol, total_oi, expiry_count, term_structure[], source}
  term_structure[] expiry, dte, call_oi, put_oi, total_oi, put_call_oi_ratio,
                  pct_of_total_oi, contract_count
biggest-increases {results[]: option_symbol, underlying_symbol, strike, dte, curr_oi,
                  last_oi, oi_change(ratio), oi_diff_plain(Δ), volume, ...}
                  # side & expiry ⊂ option_symbol (OPRA); no separate columns
```

## options-structure
```
gex               {zero_gamma_level, total_gex, regime, regime_description,
                  underlying_price, per_strike[], dte_max, note}
max-pain          {symbol, spot, caveat, dte_max, results[], source}
  results[]       expiry, dte, max_pain_strike, distance_pct, put_call_oi_ratio,
                  call_oi, put_oi, total_oi   # pain_curve only with --expiry
term-skew         {interpretation, skew_ratio, skew, call_25d_iv, put_25d_iv,
                  dte_actual, dte_target}      # --dte-target default 365
iv-term-structure {structure, kink_expiry, expiry_count, term_structure[]}
```

## historical (trailing tools take NO --date — latest-anchored)
```
signal-backtest   TOP-LEVEL: win_rate, total_signals, avg_move_pct, results[]
                  empty → {note:"no backtest results", total_signals:0}
                  # market-wide (no --symbol): p is a signal-class base rate
vrp               {vrp, iv30d, realised_vol, regime, interpretation}
iv-percentile-zscore {iv_percentile, iv_zscore, current_iv30d, dates_used, regime}
                  # dates_used = actual N (gap-aware)
trend             {daily_data[], days_analyzed, date_range, bullish_days, bearish_days,
                  price_change, iv_rank_change, flow_direction_latest}
```

## risk
```
market-regime         {regime, spy, market_breadth, sector_rotation, trend, trading_guidance}
portfolio-correlation {high_correlations, ticker_details, sector_breakdown,
                  sector_concentration, tickers_analyzed, warnings}   # no --date
```

## fz
```
quote <S> --agent          {ticker, company, sector, industry, fundamentals{84 fields}}
  .fundamentals            Shs Float, Shs Outstand, Short Float, Short Ratio, RSI (14),
                           SMA20/50/200, Perf YTD, 52W High, 52W Low, Recom, Target Price,
                           P/E, Forward P/E, Market Cap, …
quote --tickers a,b --agent [ {Ticker, Company, P/E, Market Cap, Price, Perf Week,
                           Perf YTD, EPS (ttm), Sector} ]     # flat, NO .fundamentals
screen --view ownership    columns: Ticker, Float, Short Float, Short Ratio, Inst Own,
                           Insider Own, Market Cap, Outstanding, …   # --select works
insider-clusters --agent   [ {Ticker, DistinctOwners, Side, Transactions} ]
breadth --group sector     single object: advancers, decliners, pct_green, top_mover, …
groups --by sector --view valuation  [ {Name, P/E, Fwd P/E, PEG, EPS past 5Y, Change, …} ×11 ]
```
