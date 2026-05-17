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

### Priority 2 — FRED (free tier ONLY)

Use WebFetch on FRED public series endpoints. Free series include:
- `CPIAUCSL` — CPI, all urban consumers
- `PCEPI` / `PCEPILFE` — PCE / Core PCE
- `PAYEMS` — Total nonfarm payrolls
- `UNRATE` — Unemployment rate
- `DFF` — Federal funds effective rate
- `T10Y2Y` — 10y-2y spread
- `DGS10`, `DGS2` — 10y / 2y treasury yields
- `DTWEXBGS` — Broad dollar index
- `SOFR` — Secured overnight financing rate

If a series requires a key or paid endpoint, DO NOT call it — fall through to
priority 3 and tag the source.

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
