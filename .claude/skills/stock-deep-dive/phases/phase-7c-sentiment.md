# Phase 7c — Sentiment, Positioning & Short Interest (second filter)

## Goal

Phase 7b filters the flow by the *quality of the business*. This phase filters it
by the *crowd*: news-flow tone, analyst-revision momentum, retail-vs-institutional
positioning, and short interest / borrow. A flow-confirmed long into a euphoric,
crowded, heavily-owned-by-retail name is a fade setup, not a continuation; a
bearish thesis on a name with 25% short interest and a hard-to-borrow tag is a
squeeze risk, not a clean short. Like 7b, this is a **downside-only filter** — it
can confirm or cut conviction, never add it. Emit `phase-7c-sentiment.md`.

> Added in the 2026-05-25 audit (`docs/audit/2026-05-25/06`, item N3) to cover the
> goal's explicit "tie into fundamental **and sentiment** analysis." Reuses the 7b
> free-data discipline: curl + jq, `.env` key, graceful skip, never pay.

## Data sources (priority order; all free; skip gracefully)

### Preflight

```bash
set -a; [ -f .env ] && . ./.env; set +a   # FINNHUB_API_KEY (same key as 7b)
test -n "$FINNHUB_API_KEY" && echo "finnhub key set" || echo "NO FINNHUB KEY"
fz --version >/dev/null 2>&1 && echo "fz ok" || echo "NO fz — SI via WebSearch"
case "<SYMBOL>" in *.*) echo "non-US — news/revisions limited" ;; *) echo "US ok" ;; esac
```

If `FINNHUB_API_KEY` is unset, run the WebSearch paths only (news) and mark the
Finnhub paths skipped. Short interest is `fz`-primary (source #4) — if `fz` is
unavailable (`fz_available=no` from phase-0), the short-interest leg falls back to
WebSearch. Never abort.

### Look-ahead guard (MANDATORY for as-of runs)

Filter every news item / revision / estimate to `<= as-of date`. Drop anything
dated after the as-of. Quoting a post-as-of headline is look-ahead contamination.

### Sources

| # | Source | How | Extract |
|---|--------|-----|---------|
| 1 | **News-flow sentiment** | `curl -sS "https://finnhub.io/api/v1/company-news?symbol=<SYMBOL>&from=<as-of-14d>&to=<as-of>&token=$FINNHUB_API_KEY" \| jq '[.[] \| {datetime,headline,source}]'` (free). Fallback: WebSearch `"<SYMBOL>" news <month> <year>` | Net tone (bullish/bearish/mixed) of the trailing 14d; did the tape *lead* or *lag* the news? |
| 2 | **Analyst-revision momentum** | `curl -sS "https://finnhub.io/api/v1/stock/recommendation?symbol=<SYMBOL>&token=$FINNHUB_API_KEY" \| jq '.'` (free). **Cross-source (D6):** `fz quote <SYMBOL> --agent \| jq -c '{recom:.fundamentals.Recom, target:.fundamentals."Target Price"}'` — `Recom` 1=strong-buy…5=strong-sell + price target. | Direction of the last 2–3 months: are strongBuy/buy counts rising or falling? Revisions trend; static ratings lag. Flag any **divergence** between the Finnhub recommendation trend and the `fz` `Recom`/target — vendor disagreement is itself information. Tag `[SENT:recom fz]`. |
| 3 | **Retail vs institutional** | From phase-1 (lit tape) + phase-2 (dark pool): small-lot ask-side call buying (retail euphoria) vs dark-pool block accumulation/distribution (institutional). Optionally `lib/duckdb-cuts.md §A` for a lit small-lot vs block premium split. | Are retail and institutions on the *same* side? Divergence = fade-the-crowd flag. |
| 4 | **Short interest & borrow** (N4, D1) | **Primary (`fz`, deterministic):** `fz quote <SYMBOL> --agent \| jq -c '{short_float:.fundamentals."Short Float", days_to_cover:.fundamentals."Short Ratio", float:.fundamentals."Shs Float"}'` → % float short, days-to-cover, float in one point-in-time call. **Keep WebSearch for borrow-fee / HTB only** (`fz` has no borrow field): `"<SYMBOL>" borrow fee hard to borrow <month> <year>`. Fallback if `fz` absent: WebSearch the full SI figure (Fintel/Ortex/exchange). | % float short, days-to-cover (tag `[SENT:short_float fz semi-monthly]` — Finviz SI is the exchange semi-monthly settlement, ~2-week lag), borrow fee / HTB (WebSearch). Reframes the directional thesis. See `lib/fz-recipes.md §1`. |
| 5 | **Positioning extremes** | Reuse phase-5 `historical_pc_ratio_zscore` + phase-0.5 `iv_rank`. | P/C z-score \|z\|>2 or IV-rank extreme = contrarian trigger. |

`<as-of-14d>` = as-of minus 14 calendar days; default to today (US/Eastern) if no
as-of.

## Output sections

1. **Summary** — one paragraph: does the crowd's positioning confirm or contradict
   the phase-1→7 flow bias, and is the name crowded / squeezable?
2. **Key signals** — top-5 with `[SENT:<source>]` citations.
3. **Detailed findings**
   - ### News flow (14d tone; lead/lag vs price)
   - ### Analyst-revision momentum (direction, not level) — note any
     Finnhub-vs-`fz` `Recom`/target divergence (D6)
   - ### Retail vs institutional (lit small-lot vs dark-pool blocks)
   - ### Short interest & borrow (%float, days-to-cover from `fz` — point-in-time
     & semi-monthly-tagged; HTB/borrow-fee from WebSearch)
   - ### Positioning extremes (P/C z-score, IV-rank percentile)
4. **Divergences** — explicit list where the crowd and the flow disagree.
5. **Source calls** — audit (which ran, which skipped/404'd).
6. **Source errors** — verbatim (including any skip line).
7. **Verdict for downstream** — the **positioning gate**:
   ```
   sentiment_signal:  BULLISH | BEARISH | NEUTRAL
   crowd_state:       CROWDED_LONG | CROWDED_SHORT | BALANCED | NA
   short_interest:    <%float short or "n/a"> [fz, semi-monthly] ; days_to_cover: <x or n/a> ; borrow: EASY | HTB | n/a [WebSearch]
   tier_adjustment:   CONFIRM | CAUTION | VETO | NA
   divergences:       [<=3 one-line, e.g. "retail call euphoria vs DP distribution">]
   key_risks:         [<=3 one-line positioning risks for phase-9]
   ```

## Tier-adjustment rubric (the gate logic — downside-only)

Compare the **flow bias** (plurality of phases 1–7) against the crowd:

| Condition vs flow bias | `tier_adjustment` | Phase-9 effect |
|---|---|---|
| Crowd/positioning confirms, not crowded | `CONFIRM` | no-op |
| One contrary axis (e.g. crowded long into a bullish thesis, OR adverse revision trend) | `CAUTION` | cut one size step |
| Crowded the same way as the thesis **and** a hard squeeze/short-interest mismatch (e.g. heavily-shorted name on a fresh short thesis; or extreme retail euphoria + DP distribution on a long) | `VETO` | directional → watch-only / 0%; defined-risk carry only |
| No usable data (no key / non-US / nothing found) | `NA` | no-op; phase-9 notes the blind spot |

A `VETO` here means *the crowd is already positioned your way and the smart money
isn't* (long), or *the squeeze risk dominates the edge* (short). Symmetric to 7b.

## Interpretation heuristics

- **Retail call euphoria + dark-pool distribution (phase-2) + bullish flow** →
  classic distribution-into-strength; the lit flow is exit liquidity. CAUTION→VETO.
- **High short interest + HTB + bullish flow + dark-pool accumulation** → squeeze
  fuel; this *supports* a long but you do not size it up here (filters never add) —
  note it as a tailwind for phase-9 to weigh, and a hazard for any short.
- **Deteriorating analyst revisions + bullish flow** → flow front-running a
  downgrade cycle, or a contrarian bounce — pair with 7b earnings trend.
- **\|P/C z-score\| > 2** is a genuine sentiment extreme → contrarian setups live here.
- **Absence of news/short data is not bullish** — it is a blind spot. Mark `NA`,
  don't infer.

## Common pitfalls

- Never let 7c *raise* conviction. Confirming sentiment is already partly priced in
  the flow; the gate is a downside filter (same rule as 7b/8b).
- News recency: a 3-week-old bullish article is not today's sentiment — weight by date.
- Short-interest data is often 2 weeks lagged (bi-monthly exchange reporting) — note
  the as-of of the SI figure.
- A single bullish headline is not a tone; require a balance across the 14d window.
- For ETFs / non-US: expect `NA`. Don't fabricate a crowd read from missing data.
