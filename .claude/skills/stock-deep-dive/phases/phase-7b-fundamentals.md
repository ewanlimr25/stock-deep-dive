# Phase 7b — Deep Fundamentals & Quality Veto (FINNHUB)

## Goal

Phase 7's `insights_deep_dive` gives only a shallow snapshot (PE / short% /
IV-rank). This phase pulls **real fundamentals** — balance sheet, cash flow,
income trend, multi-quarter earnings-surprise history, peer comps, and insider
sentiment (MSPR) — and uses them to **filter the flow by the quality of the
underlying**. A flow-confirmed long on a name with serial earnings misses and
deteriorating FCF deserves a fundamental veto. Emit `phase-7b-fundamentals.md`.

Ported from `claude-trading-agents` (`dataflows/fetch_finnhub_*.py`,
`prompts/fundamentals-analyst.md`). This skill runs no Python — it calls the
same free Finnhub REST endpoints directly with `curl` + `jq` (the same pattern
phase-6 uses for FRED).

## Data source — Finnhub free tier (conditional on key)

All endpoints are free-tier (`https://finnhub.io/api/v1`, 60 req/min). The key
comes from the `FINNHUB_API_KEY` env var.

### Preflight (run first)

```bash
set -a; [ -f .env ] && . ./.env; set +a   # auto-load repo-local FINNHUB_API_KEY
# 1. Key present?
test -n "$FINNHUB_API_KEY" && echo "key set" || echo "NO KEY"
# 2. US ticker? Finnhub free tier is US-equity-focused; a "." suffix
#    (e.g. .TO/.L/.HK) is not covered.
case "<SYMBOL>" in *.*) echo "non-US — skip" ;; *) echo "US ok" ;; esac
# 3. fz present? (peer-breadth + insider-cluster + analyst cross-source augments)
fz --version >/dev/null 2>&1 && echo "fz ok" || echo "NO fz — Finnhub peers only"
```

**Graceful skip.** If `FINNHUB_API_KEY` is unset (neither env var nor repo
`.env`) OR the ticker is non-US, do NOT abort the run. Write this line under
`## Tool / source errors` and emit a minimal verdict with
`tier_adjustment = NA`:

> Finnhub fundamentals skipped — `<FINNHUB_API_KEY unset | non-US ticker>`.
> Quality veto unavailable; phase-9 proceeds on flow + UW insights only. To
> enable, register a free key at https://finnhub.io/register and put it in
> `~/.zshrc` or the repo-root `.env`.

### Look-ahead guard (MANDATORY for as-of runs)

Every record with a date/period field MUST be filtered to `<= as-of date`.
Finnhub has been observed returning rows past the requested window. When an
as-of date is supplied, drop any `period`/`year-month` later than it — quoting
a future earnings print is look-ahead contamination.

### Endpoints (run in parallel — read-only fetches only, no MD write in the batch; SKILL.md rule 0)

Each endpoint may independently 403 → mark "paid, skipped". **But the harness is
fail-fast:** if one curl errors, its sibling calls are CANCELLED (`Cancelled: parallel
tool call …`), which is NOT a 403 — do not mark a cancelled endpoint "paid, skipped";
re-run it individually before recording it unavailable. Read every endpoint's output
*before* writing `phase-7b-fundamentals.md`.

| # | Endpoint | curl | What to extract |
|---|----------|------|-----------------|
| 1 | Key metrics | `curl -sS "https://finnhub.io/api/v1/stock/metric?symbol=<SYMBOL>&metric=all&token=$FINNHUB_API_KEY" \| jq '.metric'` | PE (TTM + normalized), P/B, P/S, PEG, current ratio, LT-debt/equity, ROE, ROA, gross/operating/net margin (TTM), revenue & EPS growth TTM YoY, beta, 52w hi/lo |
| 2 | Earnings surprises | `curl -sS "https://finnhub.io/api/v1/stock/earnings?symbol=<SYMBOL>&limit=8&token=$FINNHUB_API_KEY" \| jq '.'` | Last 8 quarters: actual vs estimate EPS, surprise, surprise %. Filter `period <= as-of`. Compute beat-rate. |
| 3 | Forward EPS consensus | `curl -sS "https://finnhub.io/api/v1/stock/eps-estimate?symbol=<SYMBOL>&freq=quarterly&token=$FINNHUB_API_KEY" \| jq '.data'` | Next ≤4 quarters: epsAvg/High/Low + #analysts. Keep only `period > as-of`. |
| 4 | Forward revenue consensus | `curl -sS "https://finnhub.io/api/v1/stock/revenue-estimate?symbol=<SYMBOL>&freq=quarterly&token=$FINNHUB_API_KEY" \| jq '.data'` | Next ≤4 quarters revenue avg/high/low + #analysts. Keep only `period > as-of`. |
| 5 | Peers | `curl -sS "https://finnhub.io/api/v1/stock/peers?symbol=<SYMBOL>&token=$FINNHUB_API_KEY" \| jq '.'` | Peer ticker **list** (drop self) — anchor for the peer-breadth comparison in #5b. |
| 5b | **Peer-breadth (`fz`, D3)** | With the #5 list: `fz quote --tickers <SYMBOL>,<peer1>,<peer2>,... --agent \| jq -c '.[] \| {t:.Ticker, pe:."P/E", mcap:."Market Cap", perf_ytd:."Perf YTD"}'` (overview, one call). For **depth incl. SI + float**, screen the sector/industry: `fz screen --filter sec_<sector>,ind_<industry> --view ownership --agent --select 'Ticker,Float,Short Float,Short Ratio,Inst Own'` and `--view valuation --select 'Ticker,P/E,Forward P/E,PEG,EPS Next Y'`. | A peer *comparison*, not just a list — P/E / growth / **SI / float** side-by-side (Finnhub peer metrics lack SI + float). **NOTE:** `--tickers` returns only a flat 9-field overview (no `.fundamentals`, no SI/float) — use `fz screen --view` for the deep cut. See `lib/fz-recipes.md §2`. Tag `[FUND:peer_pe fz]`. |
| 6 | Insider sentiment (MSPR) | `curl -sS "https://finnhub.io/api/v1/stock/insider-sentiment?symbol=<SYMBOL>&from=<as-of-365d>&to=<as-of>&token=$FINNHUB_API_KEY" \| jq '.data'` | Monthly Share Purchase Ratio per month (blended ratio). |
| 6b | **Insider clusters (`fz`, D5)** | `fz insider-clusters --days 30 --min-buyers 2 --side buy --agent` (and `--side sell`); grep the result for `<SYMBOL>`. | **Distinct-buyer count** for the name — the conviction MSPR averages away. Populate `insider_cluster: {present, distinct_buyers, side}` — the distinct-buyer count field is `DistinctOwners` (with `Side`, `Transactions`): `jq '.[] | select(.Ticker=="<SYMBOL>") | {DistinctOwners, Side}'`. A *sell* cluster into bullish flow sharpens a VETO. See `lib/fz-recipes.md §3`. Tag `[FUND:insider_cluster fz]`. |
| 6c | **Analyst cross-source (`fz`, D6)** | `fz quote <SYMBOL> --agent \| jq -c '{recom:.fundamentals.Recom, target:.fundamentals."Target Price"}'` | `Recom` 1=strong-buy…5=strong-sell + target, as an independent cross-check vs Finnhub. Flag divergence; overlaps Finnhub (cross-check, not net-new). Tag `[FUND:recom fz]`. |
| 7 | Statements (best-effort) | `curl -sS "https://finnhub.io/api/v1/stock/financials-reported?symbol=<SYMBOL>&freq=quarterly&token=$FINNHUB_API_KEY" \| jq '.data[0].report \| keys'` | Balance sheet / cash flow / income line items if free on this key; many accounts get 403 here — mark "paid, skipped" and lean on the metric + growth fields from #1. |

`<as-of-365d>` = the as-of date minus 365 calendar days. If no as-of date, use
today (US/Eastern) for `to` and today−365 for `from`.

### MSPR scale

MSPR (Monthly Share Purchase Ratio) ranges −100 (most bearish) to +100 (most
bullish). `|MSPR| > 30` is a strong signal; sustained multi-month trends
predict 30–90 day moves. Absence of insider activity is itself a weak signal —
note it, don't treat it as bullish.

## Output sections

1. **Summary** — one paragraph: is the underlying business *quality* consistent
   with the directional flow thesis from phases 1–7, or does it contradict it?
2. **Key signals** — top-5 with `[FUND:<metric>]` citations.
3. **Detailed findings**
   - ### Valuation (PE / fwd PE / PEG / P/B / P/S vs the named peers)
   - ### Growth profile (revenue & EPS trajectory, margin expansion/compression)
   - ### Earnings-surprise history (8-quarter beat/miss table + beat-rate)

     | Period | Actual EPS | Estimate | Surprise | Surprise % |
     |--------|-----------:|---------:|---------:|-----------:|

   - ### Forward consensus (next ≤4 quarters EPS + revenue, trend up/down)
   - ### Balance-sheet health (debt/equity, current ratio, liquidity) — or
     "statements paid-tier, using metric proxies"
   - ### Cash-flow quality (FCF, capex intensity, buyback/dividend) — proxy
     from margins/ROE if statements are paid
   - ### Insider signal (MSPR table, last ≤12 months, trend; + `fz`
     distinct-buyer cluster count and side if present)
   - ### Peers — relative-value **comparison** (not just a list): a small table of
     the named peers' P/E / fwd P/E / growth + (from `fz screen`) **SI / float**,
     with one line placing `<SYMBOL>` in the group. Note if the peer list was thin
     and a sector/industry screen was used instead.

     | Ticker | P/E | Fwd P/E | EPS next Y | Short Float | Float |
     |--------|----:|--------:|-----------:|------------:|------:|
4. **Red flags** — declining margins, rising debt, negative FCF, serial
   misses, deteriorating consensus, insider selling (MSPR persistently < −30).
5. **Tool / source calls** — audit trail (which endpoints ran, which 403'd).
6. **Tool / source errors** — verbatim (including the skip line if no key).
7. **Verdict for downstream** — the **quality gate**:
   ```
   fundamental_signal:  BULLISH | BEARISH | NEUTRAL
   tier_adjustment:     CONFIRM | CAUTION | VETO | NA
   contradiction_count: <0–3>   # of {earnings_trend, insider_MSPR, growth/margins}
                                 # that contradict the phase-1→7 flow bias
   insider_cluster:     {present: <y/n>, distinct_buyers: <int or n/a>, side: <buy/sell/n/a>}  # fz, D5
   key_risks:           [<≤3 one-line fundamental risks for phase-9 to carry>]
   ```

## Tier-adjustment rubric (the veto logic)

Compare the **flow bias** (plurality of phases 1–7) against three fundamental
axes: (a) **earnings_trend** — beat-rate and forward-consensus direction;
(b) **insider_MSPR** — sign and magnitude of recent months; (c) **growth/margins**
— revenue/EPS growth and margin trend. Count how many *contradict* the flow bias.

| Contradictions vs flow bias | `tier_adjustment` | Phase-9 effect |
|---|---|---|
| 0 (all confirm, or fundamentals strongly support) | `CONFIRM` | no-op |
| 1 | `CAUTION` | cut one size step |
| ≥ 2 | `VETO` | directional trade → watch-only / 0%; carry-only defined-risk allowed |
| no usable data (no key / non-US / all 403) | `NA` | no-op; phase-9 notes the blind spot |

A `VETO` means: the flow says long but the business is deteriorating on ≥2
axes → read the bullish flow as smart-money **distribution into strength**, not
a new long. (Symmetric for a short thesis into an *improving* underlying.)

## Interpretation heuristics

- **Serial misses + falling forward EPS + bullish flow** → classic
  distribution setup. VETO the directional long; the flow is exit liquidity.
- **MSPR > +30 sustained 3+ months + bullish flow + accumulation (phase-2)** →
  triple-confirmed; this is the strongest quality stack the skill can produce.
- **`fz` insider buy-cluster (≥2 distinct officers) corroborating a positive MSPR**
  → sharpens CONFIRM (clustered opportunistic insider buying has documented
  predictive content). A **sell**-cluster into bullish flow is the distribution
  signature — sharpens VETO. Downside-only: the cluster never *raises* conviction,
  it only strengthens the existing CONFIRM or sharpens the VETO on the
  `insider_MSPR` axis.
- **Cheap multiple alone is not CONFIRM** — value traps miss for years. Require
  a growth or insider co-signal before upgrading.
- **Non-US ticker / ETF** → expect NA; fundamentals don't apply to an ETF.
  Don't fabricate a veto from missing data.

## Common pitfalls

- Finnhub `/stock/metric` ratios are TTM-*current*, not strictly point-in-time;
  for historical as-of runs, cross-reference the price series at the as-of date
  and flag the caveat rather than quoting a contaminated PE as historical.
- `financials-reported` is frequently paid-tier — do not abort; proxy from the
  metric + growth fields and label the gap.
- A single bad quarter is not a trend — require ≥2 of the 3 axes to contradict
  before a VETO.
- Never let phase-7b *raise* conviction — it can only confirm or cut. Upside
  fundamentals are already partly priced in the flow; the gate is a downside
  filter.
