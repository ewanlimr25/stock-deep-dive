# Phase 6 — Macro Overlay

## Goal

Layer the macro regime and most recent macro prints over the ticker's setup.
Tag each datapoint as tailwind / headwind / neutral for the symbol's sector.
Emit `phase-6-macro.md`.

## Data sources (in priority order)

### Priority 1 — `uw` CLI (always run)

All take `--json`; pass `--date <AS-OF>` where the flag exists if not today.

| Command | What it gives |
|---------|---------------|
| `uw risk market-regime [--date D] --json` | SPY trend, VIX, breadth → regime label |
| `uw historical trend --symbol SPY --days 10 --json` | SPY recent action context |
| `uw historical trend --symbol VIX --days 10 --json` (or use the regime VIX field) | Vol context |
| `uw options-flow sector-flow [--date D] --json` | Premium by sector × call/put — which sectors smart money is leaning into today |
| `uw options-flow sector-flow-persistence --days 5 --json` | Per-sector net flow + persistence score (sign consistency over 5 sessions) — is the rotation *durable* or a one-day blip? |
| `uw risk portfolio-correlation --symbols <SYMBOL>,<other1>,… --lookback-days 30 --json` | Pairwise price correlation — flags when this deep dive is the same bet as another |

These last three were previously never invoked even though the `uw` engine exposes
them (AUDIT.md §2). Sector rotation contextualises a single-name flow signal
(a bullish-flow long into a sector smart money is *leaving* is weaker); the
correlation matrix prevents concurrent deep dives from becoming one
undiversified position with no flag.

**Building the correlation symbol set.** List sibling research dirs for the
same as-of date — `ls research/*/<YYYY-MM-DD>/` (Bash) — collect those tickers,
and pass `--symbols <SYMBOL>,<other1>,<other2>,…` to `uw risk portfolio-correlation`
with `--lookback-days 30`. If `<SYMBOL>` is the only blueprint for the date, note
"no concurrent positions to correlate against" and skip the gate (but still
report the tool was run with the single symbol or skipped).

### Priority 1b — `fz` sector breadth + group valuation (free, optional; D7)

A free, deterministic, logged breadth + valuation overlay that **complements** the
UW flow-based sector read (it does not replace it). Run if `fz_available=yes`
(phase-0); skip silently otherwise (`lib/fz-recipes.md §4`):

```bash
fz breadth --group sector --agent   # advancers/decliners/pct_green/top_mover, timestamped
fz groups --by sector --view valuation --agent   # per-sector P/E, Fwd P/E, PEG, EPS growth, Change
```

Use it to cross-check the UW `sector_flow` direction (is `<SYMBOL>`'s sector green
on breadth and where does its P/E sit vs peers?). **Advisory only** — it never sets
the macro bias or sizes. Tag `[MACRO:sector_breadth fz EOD]`,
`[MACRO:group_valuation fz EOD]`.

### Priority 2 — FRED (registered-but-free API, conditional on key)

**Reality check:** FRED's public chart-CSV endpoints
(`fred.stlouisfed.org/graph/fredgraph.csv?id=<ID>`,
`fred.stlouisfed.org/data/<ID>`, `fred.stlouisfed.org/series/<ID>`) are
**actively blocked** at the CDN layer for both `WebFetch` and `curl`
requests (verified 2026-05 — both return HTTP 403 / connection reset).
Do NOT attempt the chart-CSV path.

Two paths that DO work:

#### Path A — FRED JSON API with a free API key (preferred when available)

The key is free (no paid tier needed) — register once at
https://fred.stlouisfed.org/docs/api/api_key.html. Provide it either by
`export FRED_API_KEY=…` in `~/.zshrc`, OR (preferred for this skill) by
putting `FRED_API_KEY=…` in a gitignored `.env` at the repo root — the recipe
below auto-sources it so no shell-rc change is needed.

Use the Bash tool (NOT WebFetch — the API uses a different host that is
not blocked). Source `.env` first so a repo-local key is picked up:

```bash
set -a; [ -f .env ] && . ./.env; set +a   # auto-load repo-local FRED_API_KEY
curl -sSL "https://api.stlouisfed.org/fred/series/observations?series_id=CPIAUCSL&api_key=$FRED_API_KEY&file_type=json&sort_order=desc&limit=14" \
  | jq '.observations[] | {date, value}'
```

Run these series in parallel (independent **read-only** calls; ~12 series total).
These are data fetches only — no MD write in the batch (SKILL.md rule 0). Note the
harness is fail-fast: if one curl errors, its siblings are CANCELLED, not 403'd — a
`Cancelled:` result is NOT a "paid, skipped" endpoint, so re-run the cancelled series
(individually if needed) before recording any as unavailable.

| Series | What to extract |
|--------|-----------------|
| `CPIAUCSL` — CPI all urban | Last 3 monthly + YoY % vs 12mo ago |
| `CPILFESL` — Core CPI | Same |
| `PCEPI` — PCE | Last 3 monthly + YoY |
| `PCEPILFE` — Core PCE | Same |
| `PAYEMS` — Total nonfarm payrolls | Last 3 monthly + MoM Δ (thousands) |
| `UNRATE` — Unemployment rate | Last 3 monthly |
| `DFF` — Federal funds effective | Latest daily |
| `DGS10` — 10y treasury yield | Latest + 30d-ago |
| `DGS2` — 2y treasury yield | Latest + 30d-ago |
| `T10Y2Y` — 10y minus 2y spread | Latest + sign (inverted / normal) |
| `DTWEXBGS` — Broad USD index | Latest + 30d-ago |
| `SOFR` — Secured overnight | Latest daily |

Tag values as `[MACRO:<SERIES_ID>_<release-date> FRED]`, e.g.
`[MACRO:CPIAUCSL_2026-04 FRED]`.

#### Path B — Key not set: skip FRED, go straight to priority 3

If `FRED_API_KEY` is still unset after sourcing `.env`
(`set -a; [ -f .env ] && . ./.env; set +a; echo $FRED_API_KEY` is empty),
write the following line in the `## Tool / source errors` section of phase-6
and proceed entirely with WebSearch (priority 3):

> FRED skipped — no `FRED_API_KEY` (neither env var nor repo `.env`). Public
> CSV endpoint is blocked at CDN. To enable automated rate / inflation / labor
> pulls, register a free key at
> https://fred.stlouisfed.org/docs/api/api_key.html and put it in `~/.zshrc`
> or the repo-root `.env`.

WebSearch + WebFetch on reporter coverage of BLS / Fed / Treasury
releases is sufficient for a single-ticker macro overlay; precise series
values are only needed for production / multi-ticker dashboards.

### Priority 3 — WebSearch + WebFetch fallback

Use for:
- Latest **FOMC statement** (search: `"FOMC statement" <month> <year>`)
- **Dot plot** if recent SEP release
- **ISM Manufacturing PMI** + **ISM Services PMI** latest print
- **U-Michigan Consumer Sentiment** latest
- **Conference Board Consumer Confidence** latest
- Any sector-specific catalyst (chip export rules for semis, drug approval
  calendar for biotech, OPEC for energy, etc.)

## Output sections

1. **Summary** — regime label + dominant macro narrative for the sector.
2. **Key signals** — top-5 with `[MACRO:<series_or_event>]` citations.
3. **Detailed findings**
   - ### Market regime (UW: SPY + VIX + breadth)
   - ### Inflation (CPI, PCE — last 3 prints + YoY)
   - ### Labor (NFP, unemployment — last 2 prints)
   - ### Rates (FOMC last statement, dot plot, SOFR, 10y/2y, 2s10s)
   - ### Activity (ISM Mfg PMI, ISM Services PMI)
   - ### Consumer (U-Mich, Conference Board)
   - ### Sector overlay (specific catalysts for `<SYMBOL>`'s sector)
   - ### Sector rotation (`uw options-flow sector-flow` + `sector-flow-persistence`)
     - `<SYMBOL>`'s sector net flow today + 5-session persistence score.
     - Verdict: is smart money rotating INTO or OUT OF this sector, and is the
       rotation persistent (high sign-consistency) or noise? Tag the direction
       relative to the trade thesis: `aligned` / `adverse` / `neutral`.
     - **`fz` breadth cross-check (D7, advisory):** the sector's breadth
       (advancers/decliners, pct_green) and group P/E from `fz` — does the
       price-breadth read corroborate the UW flow rotation? Note agreement or
       divergence; this colors, never overrides, the rotation verdict.
   - ### Cross-name correlation (`uw risk portfolio-correlation`)
     - Concurrent blueprints correlated against (list tickers + date).
     - Pairwise correlation table; flag any pair ≥ 0.70 as a **cluster**
       (phase-9 cuts size), 0.60–0.70 as **soft-watch** (surface only).
4. **Tailwind / Headwind table**

   | Datapoint | Latest value | Release date | Source | Impact on \<SECTOR\> |
   |-----------|--------------|--------------|--------|---------------------|
   | CPI YoY   | ...          | ...          | FRED/WebSearch | tailwind / headwind / neutral |
   | ...       | ...          | ...          | ...    | ...                 |

5. **Catalyst calendar (next 30d)**

   Record the **front-expiry expected (implied) move** at the top of this section
   from the screener `implied_move` / `implied_move_perc` (already surfaced in
   phase-0.5 `[CTX:implied_move_pct]` and phase-7's `uw_screener` block) — e.g.
   "front-expiry implied move ±3.8% / $3.78 [CTX:implied_move]". Phase-9 sizes its
   structures to this priced range (N4); each binary below should be read against it.

   | Date | Event | Likely impact | vs expected move |
   |------|-------|---------------|------------------|
   | ...  | FOMC  | ?             | inside / exceeds ±X% |
   | ...  | CPI release | ?       | ...              |

6. **Tool / source errors** — verbatim.
7. **Verdict for downstream**
   - Net macro bias for `<SYMBOL>` (tailwind / headwind / neutral)
   - Conviction 1–5
   - Top 2 datapoints phase-9 must cite in its macro overlay
   - Top 2 catalysts phase-9 must put in the calendar
   - **Sector-rotation verdict:** `aligned` / `adverse` / `neutral` +
     persistence score (phase-9 sizing gate input).
   - **Correlation verdict:** any cluster (≥0.70) or soft-watch (0.60–0.70)
     pair, named with the coefficient (phase-9 sizing gate input). State
     "no concurrent positions" if `<SYMBOL>` is the only blueprint for the date.

## Source tagging convention

Every macro datapoint MUST carry:
- The series ID or event name
- The release date (NOT today's date)
- The source: `UW`, `FRED`, or `WebSearch:<domain>`

Examples:
- `[MACRO:CPIAUCSL_2026-04 FRED]`
- `[MACRO:FOMC_2026-05-07 WebSearch:federalreserve.gov]`
- `[MACRO:MarketRegime_2026-05-17 UW]`

## Common pitfalls

- WebSearch results may be from older articles — always confirm release date.
- FRED series can revise; the most recent print may be marked "preliminary".
- Sector impact is judgmental — if uncertain, mark neutral and justify in
  the body.
- The skill should NEVER pay for data. If a source asks for a subscription,
  note it as "paid source skipped" and use WebSearch instead.
