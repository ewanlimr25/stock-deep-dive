# Phase 6 — Macro Overlay

## Goal

Layer the macro regime and most recent macro prints over the ticker's setup.
Tag each datapoint as tailwind / headwind / neutral for the symbol's sector.
Emit `phase-6-macro.md`.

## Data sources (in priority order)

### Priority 1 — UW MCP (always run)

| Tool | Args | What it gives |
|------|------|---------------|
| `mcp__uw-pp__risk_market_regime` | (date if as-of) | SPY trend, VIX, breadth → regime label |
| `mcp__uw-pp__historical_trend` | symbol=SPY, days=10 | SPY recent action context |
| `mcp__uw-pp__historical_trend` | symbol=VIX or use regime VIX field | Vol context |

### Priority 2 — FRED (registered-but-free API, conditional on key)

**Reality check:** FRED's public chart-CSV endpoints
(`fred.stlouisfed.org/graph/fredgraph.csv?id=<ID>`,
`fred.stlouisfed.org/data/<ID>`, `fred.stlouisfed.org/series/<ID>`) are
**actively blocked** at the CDN layer for both `WebFetch` and `curl`
requests (verified 2026-05 — both return HTTP 403 / connection reset).
Do NOT attempt the chart-CSV path.

Two paths that DO work:

#### Path A — FRED JSON API with a free API key (preferred when available)

If the env var `FRED_API_KEY` is set, call the official JSON API. The key
is free (no paid tier needed) — register once at
https://fred.stlouisfed.org/docs/api/api_key.html and `export
FRED_API_KEY=…` in `~/.zshrc`.

Use the Bash tool (NOT WebFetch — the API uses a different host that is
not blocked):

```bash
curl -sSL "https://api.stlouisfed.org/fred/series/observations?series_id=CPIAUCSL&api_key=$FRED_API_KEY&file_type=json&sort_order=desc&limit=14" \
  | jq '.observations[] | {date, value}'
```

Run these series in parallel (independent calls; ~12 series total):

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

If `FRED_API_KEY` is unset (`echo $FRED_API_KEY` is empty), write the
following line in the `## Tool / source errors` section of phase-6 and
proceed entirely with WebSearch (priority 3):

> FRED skipped — no `FRED_API_KEY` env var set. Public CSV endpoint is
> blocked at CDN. To enable automated rate / inflation / labor pulls, the
> user can register a free key at
> https://fred.stlouisfed.org/docs/api/api_key.html and export it in
> their shell rc.

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
4. **Tailwind / Headwind table**

   | Datapoint | Latest value | Release date | Source | Impact on \<SECTOR\> |
   |-----------|--------------|--------------|--------|---------------------|
   | CPI YoY   | ...          | ...          | FRED/WebSearch | tailwind / headwind / neutral |
   | ...       | ...          | ...          | ...    | ...                 |

5. **Catalyst calendar (next 30d)**

   | Date | Event | Likely impact |
   |------|-------|---------------|
   | ...  | FOMC  | ?             |
   | ...  | CPI release | ?       |

6. **Tool / source errors** — verbatim.
7. **Verdict for downstream**
   - Net macro bias for `<SYMBOL>` (tailwind / headwind / neutral)
   - Conviction 1–5
   - Top 2 datapoints phase-9 must cite in its macro overlay
   - Top 2 catalysts phase-9 must put in the calendar

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
