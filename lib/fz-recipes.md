# `fz` Recipe Library — Finviz CLI augments (free, deterministic, EOD)

**Status: opt-in supplement, MCP-primary.** `fz` (`finviz-pp-cli`, a Go binary at
`~/.local/bin/fz`) supplies the **fundamentals / short-interest / float / peer / breadth**
data the `uw-pp` MCP does **not** carry. It is the same class of tool as this skill's existing
`curl`/Finnhub calls — a Bash CLI, no MCP, no new dependency. It is a *supplement* to the phases the
MCP can't serve, **never** a new primary substrate.

`fz` **cannot** replace, compete with, or duplicate any `uw`/MCP tool: it has **no** options flow,
greeks, dark pool, IV term structure, GEX/DEX, or OI. It touches **none of the microstructure phases
1–5** as a primary source — only as advisory price-context color in 5/9. It lives in **7b** (quality),
**7c** (sentiment/SI), **6** (macro overlay), **2/3** (float-normalize, advisory), and **0** (float
snapshot + as-of drift).

## House rules for every `fz` datapoint

- **Downside-only.** An `fz` contribution can only *cut* size or veto (7b/7c gates) or add advisory
  color (2/3/5/6/9). It **never** touches the Kelly `p` (phase-5 backtest win-rate) and never inflates
  conviction.
- **Citation discipline.** Tag every `fz` datapoint with a trailing ` fz` qualifier inside the phase's
  normal tag (parallel to the ` DUCKDB` qualifier — see `rubrics/citation-conventions.md`):
  `[SENT:short_float fz]`, `[FUND:peer_pe fz]`, `[MACRO:sector_breadth fz EOD]`,
  `[DP:block_pct_float fz]`. **Short interest is the semi-monthly settlement figure (~2-week lag)** —
  tag it `[SENT:short_float fz semi-monthly]` so the staleness is on the record.
- **Graceful skip.** If `fz` is absent or errors, the phase proceeds on its current source (WebSearch
  for SI, Finnhub for peers) and notes the skip — identical to the Finnhub-403 / non-US-ticker
  behavior. Never abort the run.

## Invocation basics (verified 2026-05-27)

- Add **`--agent`** to any command = `--json --compact --no-input --no-color --yes` (the agent-safe
  defaults). Always use it.
- **`--select a,b`** projects fields, comma-separated. Default rate limit **2 req/s**. Reads persist to
  local SQLite (`~/.local/share/finviz-pp-cli/data.db`) which powers `quote-drift`.
- **Exit codes drive graceful-skip:** `0` ok · `2` usage · `3` not-found · `5` api · `7` rate-limited ·
  `10` config. Treat any non-zero as "skip this `fz` lane, fall back to the phase's current source."
- **No auth** except the bulk `export` command (which the skill does not use).

### Field-projection syntax — READ THIS (label spaces & quoting are sharp edges)

Single-ticker `fz quote <T>` nests the 84-field grid under **`.fundamentals`**. Two working ways to
project; one trap:

```bash
# WORKS — unquoted dotted paths, comma-separated (spaces in labels are fine UNQUOTED):
fz quote AAPL --agent --select 'fundamentals.Short Float,fundamentals.Short Ratio,fundamentals.Shs Float'
#   → {"fundamentals":{"Short Float":"0.92%","Short Ratio":"3.05","Shs Float":"14.67B"}}

# TRAP — inner double-quotes around a key return an EMPTY object:
fz quote AAPL --agent --select 'fundamentals."Short Float"'      # → {"fundamentals":{}}

# ROBUST (recommended for the phase patches) — full quote piped to jq:
fz quote AAPL --agent | jq -c '{short_float:.fundamentals."Short Float", days_to_cover:.fundamentals."Short Ratio", float:.fundamentals."Shs Float", recom:.fundamentals.Recom, target:.fundamentals."Target Price"}'
#   → {"short_float":"0.92%","days_to_cover":"3.05","float":"14.67B","recom":"1.98","target":"316.07"}
```

---

## §1 — Single-ticker quote → SI / float / analyst / technicals (phase-7c, 7b, 2/3, 5/9)

```bash
fz quote <T> --agent | jq -c '{
  short_float:.fundamentals."Short Float",        # phase-7c — replaces WebSearch SI leg (semi-monthly)
  days_to_cover:.fundamentals."Short Ratio",      # phase-7c
  float:.fundamentals."Shs Float",                # phase-0 carry → phase-2/3 % of float
  shs_out:.fundamentals."Shs Outstand",
  inst_own:.fundamentals."Inst Own", inst_trans:.fundamentals."Inst Trans",
  insider_own:.fundamentals."Insider Own", insider_trans:.fundamentals."Insider Trans",
  recom:.fundamentals.Recom,                      # analyst 1=strong-buy … 5=strong-sell (cross-source vs Finnhub)
  target:.fundamentals."Target Price",
  rsi:.fundamentals."RSI (14)",                   # phase-5/9 advisory
  sma50:.fundamentals.SMA50, sma200:.fundamentals.SMA200,
  perf_ytd:.fundamentals."Perf YTD",
  high52:.fundamentals."52W High", low52:.fundamentals."52W Low",  # NOTE: "<value> <pct>%" combined string
  earnings:.fundamentals.Earnings
}'
```

- **`Recom`/`Target`/earnings/EPS-surprise overlap Finnhub** — use as a **cross-source check**, not
  net-new. Net-new vs the rest of the flow: `Shs Float` (no other phase has float) and the SI fields
  when the Finnhub key is unset.
- **`Short Float` is semi-monthly** (exchange settlement, ~2-week lag) → squeeze *context*, not a live
  borrow signal. `fz` has **no borrow-fee / HTB field** → phase-7c keeps WebSearch for that one leg.
- `52W High`/`52W Low` come back as a combined `"<level> <pct>%"` string (e.g. `"311.82 -0.31%"`) —
  split on whitespace if you need the level vs the % separately.

## §2 — Peer breadth (phase-7b) — `--tickers` is SHALLOW; use `screen --view` for depth

> **CORRECTION to audit `02`/D3.** `fz quote --tickers` does **NOT** return the 84-field grid per
> peer. It returns a **flat 9-field overview** only — `Ticker, Company, Sector, Market Cap, P/E,
> Price, Volume, Perf Week, Perf YTD`, with **no `.fundamentals` nesting and no SI/float/margins**.
> A `--select 'fundamentals.…'` against `--tickers` therefore returns empty objects. (Verified
> 2026-05-27.) For the deep peer comparison (SI / float / margins / growth) use `fz screen --view`.

**(a) Quick known-peer overview** (when Finnhub `/stock/peers` gave you an explicit list) — one call,
overview fields only:
```bash
fz quote --tickers <T>,<peer1>,<peer2>,... --agent | jq -c '.[] | {t:.Ticker, pe:."P/E", mcap:."Market Cap", perf_ytd:."Perf YTD"}'
```

**(b) Deep peer breadth** — the real relative-value comparison incl. SI + float, via a
sector/industry screen (flat output; `--select` takes **bare** field names, no `fundamentals.` prefix):
```bash
# Ownership view → Float, Short Float, Short Ratio, Inst/Insider Own & Trans, Outstanding:
fz screen --filter sec_<sector>,ind_<industry> --view ownership --agent \
  --select 'Ticker,Float,Short Float,Short Ratio,Inst Own,Insider Trans'

# Valuation view → P/E, Forward P/E, PEG, P/B, P/S, P/FCF, EPS Next Y, EPS Next 5Y, Sales Past 5Y:
fz screen --filter sec_<sector>,ind_<industry> --view valuation --agent \
  --select 'Ticker,P/E,Forward P/E,PEG,EPS Next Y,Sales Past 5Y'
```

> **Screen field labels differ from quote labels** — use the right label per command:
> `Forward P/E` (screen) vs `Fwd P/E` (quote) · `EPS Next Y` (screen) vs `EPS next Y` (quote) ·
> `Float` (screen ownership) vs `Shs Float` (quote) · `Outstanding` (screen) vs `Shs Outstand` (quote).

Raw Finviz filter codes (verified): `sec_technology`, `ind_consumerelectronics`, `cap_midover`,
`cap_largeover`, `idx_sp500`, `fa_pe_u20`, `sh_short_o15`/`sh_short_o20` (squeeze lane), `sh_price_o5`,
`earningsdate_thisweek`, `ta_*` signals. Views: `overview|valuation|ownership|performance|technical|financial`.

## §3 — Insider clusters (phase-7b) — distinct-buyer count, net-new vs MSPR

```bash
fz insider-clusters --days 30 --min-buyers 2 --side buy --agent
#   → [{"DistinctOwners":2,"Side":"buy","Ticker":"WHF","Transactions":3}, ...]
```

A **count of distinct insiders** acting the same way — the conviction Finnhub's blended monthly MSPR
ratio averages away. Scope to the name (grep the `Ticker`) to populate
`insider_cluster: {present, distinct_buyers, side}`. Run the `--side sell` variant too: an insider
*selling* cluster into bullish flow sharpens a 7b VETO (distribution signature).

## §4 — Macro breadth & group valuation (phase-6, advisory)

```bash
fz breadth --group sector --agent     # advancers/decliners/pct_green/top_mover, timestamped
fz groups --by sector --view valuation --agent   # per-sector P/E, Fwd P/E, PEG, EPS growth, Change, Volume
```

Free, logged breadth + valuation overlay complementing the UW `options_flow_sector_flow*` read.
Advisory only; tag `[MACRO:sector_breadth fz EOD]`.

## §5 — As-of re-run drift (phase-0, needs a prior snapshot)

```bash
fz quote-drift <T> --since <prior_run_date> --agent   # which of the 84 fields moved between snapshots
```

Requires a prior `fz quote <T>` snapshot in the local store (limit #6). On a first run there is no
history → skip and note it. Use it on a same-name `-vK` re-run to auto-list moved fundamentals
(target cut, short-float spike, guidance re-rate) into the intake delta. The phase-0 snapshot in §6
below is what seeds this for the *next* run.

## §6 — Phase-0 health probe + float snapshot (run once at intake)

```bash
fz --version 2>/dev/null && fz doctor --agent >/dev/null 2>&1 && FZ=yes || FZ=no
[ "$FZ" = yes ] && fz quote <T> --agent | jq -c '{float:.fundamentals."Shs Float", shs_out:.fundamentals."Shs Outstand", short_float:.fundamentals."Short Float", captured:now}'
echo "fz_available=$FZ"
```

Records `fz_available` (yes/no) and **snapshots `Shs Float` once** so phase-2/3 can express order size
as % of float and the snapshot seeds next run's `quote-drift`. On `fz_available=no`, every `fz` lane
degrades to its current source (WebSearch SI, Finnhub peers) — never abort.

## What `fz` is NOT (scope discipline — do not over-adopt)

1. **No microstructure** — no flow/greeks/dark-pool/GEX/DEX/OI. Touches none of phases 1–5 as a source.
2. **EOD/delayed**, not intraday tick (only `fz prices` has intraday). Fine for slow SI/float/fundamentals.
3. **Short interest = semi-monthly settlement (~2-week lag)** — squeeze context, not live borrow.
4. **No borrow-fee / HTB field** — phase-7c keeps WebSearch for borrow cost / HTB.
5. **`Recom`/`Target`/earnings/EPS-surprise overlap Finnhub** — cross-source check, not net-new.
6. **`quote-drift`/`screen-diff` need a prior snapshot** — run `fz quote`/`sync` first.
