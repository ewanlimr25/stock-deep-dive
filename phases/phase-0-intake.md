# Phase 0 — Intake

## Goal

Validate inputs, prepare the immutable output directory, and write
`phase-0-intake.md` recording the run metadata.

## Steps

1. **Parse ticker.** Uppercase, alphanumeric, 1–5 chars (US-listed equity or
   ETF). Reject if invalid; ask the user to re-supply.

2. **Resolve as-of date.** Default = today (US/Eastern). If user supplied a
   date, normalize to `YYYY-MM-DD` and remember to pass `date=<as-of>` to
   every UW tool downstream.

3. **Create directory.** `research/<SYMBOL>/<YYYY-MM-DD>/` (mkdir -p).

4. **Check for existing run.** If any `phase-*.md` already exists in that
   directory:
   - Determine the next version suffix (`-v2`, `-v3`, ...).
   - All subsequent phases in this run will write `phase-N-<topic>-vK.md`
     where K is the new version.
   - The intake file itself becomes `phase-0-intake-vK.md` and must include a
     "Prior version(s)" section listing earlier files in the same dir.

5. **Smoke-test UW MCP availability.** Call
   `mcp__uw-pp__historical_available_dates` (no args). If it errors, write the
   error to phase-0 under `## Tool errors` and ABORT the run — without UW data
   the rest of the skill is useless.

6. **Confirm ticker has options.** Call
   `mcp__uw-pp__options_flow_unusual_volume` with `symbol=<TICKER>` and
   `top_n=1`. If empty AND the ticker is a known equity, note "thin options
   activity" in phase-0 and proceed. If the tool errors with "no such
   symbol", abort.

7. **Probe the local snapshot (for the DuckDB escape hatch + gap-awareness).**
   The `uw-pp` MCP reads parquet files under `~/Documents/Stocks`
   (`STOCKS_DIR`, overridable in `.env`). The escape hatch (`lib/duckdb-cuts.md`),
   phase-0.5 self-history, and phase-5 gap-handling need to know which dates are
   present locally. Run once and record the result:
   ```bash
   set -a; [ -f .env ] && . ./.env; set +a
   STOCKS_DIR="${STOCKS_DIR:-$HOME/Documents/Stocks}"
   python3 -c "import duckdb" 2>/dev/null && DUCK=yes || DUCK=no
   ls "$STOCKS_DIR/Stock Screener/" 2>/dev/null \
     | sed -E 's/.*screener-([0-9-]+)\.parquet/\1/' | sort
   echo "DUCKDB=$DUCK  STOCKS_DIR=$STOCKS_DIR"
   ```
   Record `local_data_available` (yes/no), `duckdb_available`, and the **full list
   of available local dates** in phase-0. Flag the known non-contiguous gap if the
   list shows it. This is informational only — the MCP remains the primary path;
   the local list just tells later phases when the escape hatch and self-history
   are usable. Never abort on a missing snapshot.

8. **Write `phase-0-intake.md`** using the template at
   `templates/phase-N-template.md`. The summary section should list:
   - Resolved ticker + as-of date
   - Output directory absolute path
   - Versioning decision (v1 / v2 / ...)
   - UW MCP availability check result
   - Options activity check result
   - Local-data availability + DuckDB present + available local dates (+ gap flag)

## Output template (specific to phase 0)

```markdown
# Phase 0 — Intake

**Ticker:** <SYMBOL>
**As-of date:** <YYYY-MM-DD>
**Output dir:** <absolute path>
**Version:** v1 (or vK with reference to prior versions)
**Generated:** <ISO-8601>

## Summary

Ticker validated. Output directory created. UW MCP reachable.
Proceeding to phase 1.

## UW availability

- `historical_available_dates`: <ok / error text>
- Latest available options date: <date>
- Latest available darkpool date: <date>

## Ticker sanity

- Options activity (unusual_volume top 1): <option_symbol or "empty">

## Local data (escape hatch / gap-awareness)

- `local_data_available`: <yes/no> · `duckdb_available`: <yes/no>
- `STOCKS_DIR`: <path>
- Available local dates: <list> (gap flagged: <yes/no>)
- Note: MCP is primary; local DuckDB is opt-in for cuts the MCP can't express
  (`lib/duckdb-cuts.md`).

## Prior versions

<empty for v1>

## Tool errors

<empty if all green>
```

## Validation checklist

- [ ] Output dir exists and is empty (or contains only prior-version files)
- [ ] `phase-0-intake.md` (or `-vK.md`) written
- [ ] Either UW MCP confirmed working OR run aborted with clear error
