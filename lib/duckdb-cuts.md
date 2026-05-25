# DuckDB Escape Hatch — cuts the MCP can't express

**Status: opt-in augmentation, not a default path.** The `uw-pp` MCP server reads
the same `~/Documents/Stocks` parquet files these recipes query (proven 2026-05-25 —
its output names the source file; see `docs/audit/2026-05-25/06`). So for anything
the MCP already returns, **use the MCP** — it is the curated, point-in-time-correct
layer. Reach for DuckDB **only** for the three query shapes the MCP's fixed tool
vocabulary genuinely cannot express:

- **§A** custom aggregations / slices the MCP doesn't pre-bucket (e.g. aggressor
  split excluding 0DTE, net delta-notional by strike);
- **§B** cross-dataset joins on a key the MCP doesn't join (option print ↔ dark-pool
  print on timestamp proximity);
- **§C** one-shot full-universe / long self-history percentiles.

When you use a recipe here, tag the resulting datapoint `[… DUCKDB]` (e.g.
`[CTX:self_pctile DUCKDB]`) so `/deep-dive-calibration` can attribute it to the
escape hatch, not to an MCP tool.

## Preconditions

```bash
set -a; [ -f .env ] && . ./.env; set +a
STOCKS_DIR="${STOCKS_DIR:-$HOME/Documents/Stocks}"
ASOF="<YYYY-MM-DD>"
python3 -c "import duckdb" 2>/dev/null && echo "duckdb ok" || echo "NO duckdb — skip escape hatch"
test -f "$STOCKS_DIR/Stock Screener/stock-screener-$ASOF.parquet" \
  && echo "snapshot present for $ASOF" || echo "no local snapshot for $ASOF — MCP only"
```

If DuckDB is absent or the snapshot for the as-of date is missing, **skip silently
and rely on the MCP** — these cuts are augmentations, never required. Every query:
`con.execute("SET threads TO 4;")`; filter `WHERE canceled=false` on tape/DP;
timestamps are tz-aware US-Eastern (compare to `TIMESTAMP '… -04:00'`/`-05:00`).
**Push aggregation into the query — return only summaries**, never raw rows, so the
model never ingests the 10.9M-row tape.

Path map (datasets, glob): All Options `All Options/bot-eod-report-<DATE>.parquet`,
Dark pool `Dark pool/dp-eod-report-<DATE>.parquet`, OI changes
`OI changes/chain-oi-changes-<DATE>.parquet`, Stock Screener
`Stock Screener/stock-screener-<DATE>.parquet`.

---

## §A — Custom aggregations the MCP doesn't pre-bucket

Use when the standard top-N / fixed-`dte_max` views are ambiguous — e.g. you need
the directional read **stripped of 0DTE pin noise**, or **delta-notional** (true
directional footprint) rather than premium.

```python
import duckdb
con = duckdb.connect(); con.execute("SET threads TO 4;")
SD="<STOCKS_DIR>"; ASOF="<YYYY-MM-DD>"; SYM="<SYMBOL>"
F=f"{SD}/All Options/bot-eod-report-{ASOF}.parquet"

# Aggressor premium AND delta-notional split, EXCLUDING 0–1DTE (the cut the MCP lacks)
print(con.execute(f"""
SELECT option_type, side, COUNT(*) trades, SUM(size) contracts,
       ROUND(SUM(premium)/1e6,2) prem_m,
       ROUND(SUM(delta*size*100*underlying_price)/1e9,2) delta_notional_bn
FROM read_parquet('{F}')
WHERE underlying_symbol='{SYM}' AND canceled=false AND expiry > DATE '{ASOF}' + 1
GROUP BY 1,2 ORDER BY 1,2""").df().to_string(index=False))

# Premium by DTE bucket × type (separate gamma/pin mechanics from directional tenor)
print(con.execute(f"""
SELECT CASE WHEN expiry<=DATE '{ASOF}'+1 THEN '0-1DTE'
            WHEN expiry<=DATE '{ASOF}'+7 THEN '2-7DTE'
            WHEN expiry<=DATE '{ASOF}'+45 THEN '8-45DTE'
            WHEN expiry<=DATE '{ASOF}'+180 THEN '46-180DTE' ELSE 'LEAP' END dte_bucket,
       option_type, ROUND(SUM(premium)/1e6,2) prem_m
FROM read_parquet('{F}') WHERE underlying_symbol='{SYM}' AND canceled=false
GROUP BY 1,2 ORDER BY 1,2""").df().to_string(index=False))
```

Tag: `[FLOW:aggressor_ex0dte DUCKDB]`, `[FLOW:delta_notional DUCKDB]`. These augment
phase-1 (or phase-7c §3 retail-vs-institutional small-lot split) when the MCP's
top-N view over- or under-states direction.

## §B — Cross-dataset timestamp join (option print ↔ dark-pool print)

Use to confirm a single high-conviction option print with near-simultaneous
underlying activity — there is no MCP tool that joins two tapes on time.

```python
DP=f"{SD}/Dark pool/dp-eod-report-{ASOF}.parquet"
# Dark-pool prints within ±5 min of a specific option-print time (ET)
T="<HH:MM:SS>"   # e.g. the largest sweep's executed_at, ET
print(con.execute(f"""
SELECT executed_at, size, ROUND(premium/1e6,2) prem_m, ROUND(price,2) price,
       CASE WHEN price>=nbbo_ask THEN 'lift' WHEN price<=nbbo_bid THEN 'hit'
            WHEN price>(nbbo_bid+nbbo_ask)/2 THEN 'abv_mid' ELSE 'blw_mid' END aggressor
FROM read_parquet('{DP}')
WHERE ticker='{SYM}' AND canceled=false
  AND executed_at BETWEEN TIMESTAMP '{ASOF} {T}-04:00' - INTERVAL 5 MINUTE
                      AND TIMESTAMP '{ASOF} {T}-04:00' + INTERVAL 5 MINUTE
ORDER BY premium DESC LIMIT 10""").df().to_string(index=False))
```

Tag: `[DP:ts_confirm DUCKDB]`. Augments phase-2's verdict for the single most
important print phase-1 flagged.

## §C — Full-universe & long self-history percentiles

Use for phase-0.5 context when an **exact** percentile is wanted (the MCP returns
ranked top-N, not a percentile for an arbitrary name) or a **self-history** read
across the local window (the MCP would need one call per day).

```python
import glob
SCR=f"{SD}/Stock Screener/stock-screener-{ASOF}.parquet"
# Exact percentile across the whole optionable universe today
print(con.execute(f"""
WITH u AS (
  SELECT ticker, call_premium+put_premium tot,
         net_call_premium-net_put_premium net_dir, iv_rank,
         (call_volume+put_volume)::DOUBLE/NULLIF(avg30_volume,0) vol_x
  FROM read_parquet('{SCR}') WHERE call_volume+put_volume>0)
SELECT ROUND(100*PERCENT_RANK() OVER(ORDER BY tot),1)     pctile_total_prem,
       ROUND(100*PERCENT_RANK() OVER(ORDER BY net_dir),1) pctile_net_dir,
       ROUND(100*PERCENT_RANK() OVER(ORDER BY iv_rank),1) pctile_iv_rank,
       ROUND(100*PERCENT_RANK() OVER(ORDER BY vol_x),1)   pctile_vol_vs_avg
FROM u QUALIFY ticker='{SYM}'""").df().to_string(index=False))

# Self-history: today vs the name's own ≤31-session distribution
files=sorted(glob.glob(f"{SD}/Stock Screener/stock-screener-*.parquet"))
flist=",".join(f"'{f}'" for f in files)
print(con.execute(f"""
WITH h AS (SELECT date, net_call_premium-net_put_premium net_dir,
                  call_premium+put_premium tot
           FROM read_parquet([{flist}]) WHERE ticker='{SYM}')
SELECT ROUND(100*PERCENT_RANK() OVER(ORDER BY net_dir),1) self_pctile_net_dir,
       ROUND(100*PERCENT_RANK() OVER(ORDER BY tot),1)     self_pctile_total,
       COUNT(*) OVER () AS sessions_in_window
FROM h QUALIFY date=DATE '{ASOF}'""").df().to_string(index=False))
```

Tag: `[CTX:universe_pctile DUCKDB]`, `[CTX:self_pctile DUCKDB]`. **Mind the data
gap** (`§ gap`): `sessions_in_window` is the true N — a self-history percentile
computed across the 2026-03-28→04-24 hole is over ≤31 *available* sessions, not a
contiguous calendar window. State the N.

## § gap — the non-contiguous window (applies to any local lookback)

The local snapshots are **not contiguous**: 2026-03-13…03-27 then 2026-04-27…05-22
(21-session hole 2026-03-28→04-24). Never annualize or compute a "30-day" trend
across the hole; report the actual session count. The MCP's `historical_*` tools
sit on the same files — if a lookback there looks suspiciously smooth across late
March/April, suspect the gap and cross-check the available dates:

```bash
ls "$STOCKS_DIR/Stock Screener/" | sed -E 's/.*screener-([0-9-]+)\.parquet/\1/' | sort
```
