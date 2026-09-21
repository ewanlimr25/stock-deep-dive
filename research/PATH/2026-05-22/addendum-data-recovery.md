# Addendum — Data Recovery (post-run backfill)

**Ticker:** PATH (UiPath Inc.)
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T00:00:00Z
**Status:** Supplementary to the immutable phase chain (phase-0 … phase-10). This file
backfills three datapoints the original run flagged as unavailable. It **does not** overwrite
any phase MD or `decision.json`. Net effect on the blueprint: **none** — the recovered points
roughly offset and reinforce the existing NEUTRAL/mild-long, defined-risk, starter-size,
conviction-0.55 conclusion.

## What was unavailable in the original run

| Gap | Original phase | Original disposition |
|-----|----------------|----------------------|
| Finnhub forward EPS/revenue consensus | phase-7b §Forward consensus | 403 paid-tier → "key blind spot" |
| Finnhub MSPR (insider sentiment) | phase-7b §Insider signal | empty `{"data":[]}` → "NA / unobserved" |
| UW `risk_portfolio_correlation` coefficients | phase-6 §Cross-name correlation | "Unknown" sectors, `high_correlations: null` → "no usable coefficients" |

---

## 1. Forward consensus — recovered via WebSearch (Yahoo locked, Finnhub paid)

**Root cause.** Finnhub `eps-estimate`, `revenue-estimate`, `price-target`, and
`revenue-breakdown` are **confirmed premium-tier (HTTP 403 "You don't have access to this
resource")** on the free key — not a transient error. Yahoo Finance `quoteSummary`
(earningsTrend/financialData) returned **all `null`** — the same crumb/cookie auth wall that
401'd `insights_deep_dive` and the UW correlation tool. WebSearch is the working free path
(consistent with the skill's phase-6/7c WebSearch fallback discipline).

**Recovered (filtered to ≤ as-of; the 05-28 print had not occurred):**

| Q1 FY27 (reports 2026-05-28) | Value | Source |
|---|---|---|
| Consensus EPS | **~$0.15–0.16** | WebSearch (American Banking News / TipRanks) |
| Consensus revenue | **~$397.5M** | WebSearch |
| Company Q1 guide (prior) | $395–400M (in line / slightly above cons) | WebSearch |
| Company **FY27 revenue guide** | **$1.754–1.759B vs consensus $1.74B** → guided **above** | WebSearch |

**Read:** mildly **constructive** [SENT:forward_consensus WebSearch]. Management set a
full-year revenue bar **above** the Street — a beatable/raised setup the original run could
not see. This slightly strengthens the long-lean and partially offsets the insider finding (§2).
Recency caveat: figures reflect ~May 2026 reporting (pre-print); analyst numbers ~static in
the 4 days between as-of (05-22) and retrieval.

**Persistent free alternative (optional):** Financial Modeling Prep or Alpha Vantage free
tiers carry analyst estimates but each needs a separately-registered free key (none present
in `.env`, which holds only `FINNHUB_API_KEY` + `FRED_API_KEY`). WebSearch suffices for a
single-name overlay; register an FMP key only if a programmatic estimates feed is wanted.

## 2. Insider signal — recovered via `insider-transactions` (MSPR aggregate is empty)

**Root cause.** Finnhub `insider-sentiment` (the computed MSPR) returns `{"data":[]}` for
PATH — Finnhub simply does not publish an MSPR series for this name (the endpoint is
free/accessible, just empty). But **`insider-transactions` is free and fully populated** — the
raw Form-4 tape. Aggregating it by transaction code (≤ 2026-05-22, trailing 12 months) gives a
proper insider read the MSPR aggregate would have summarized:

| Code | Meaning | n | Net shares |
|---|---|---|---|
| **S** | open-market **sell** | 129 | **−7,207,693** |
| J | other disposition (footnoted) | 7 | −9,615,297 |
| A | grant / award | 14 | +1,324,322 (routine comp) |
| F | tax-withholding on vesting | 17 | −586,371 (routine) |
| **P** | open-market **buy** | **0** | **0** |
| C / M | conversion / option-exercise | 6 | 0 |

**Read:** mildly **BEARISH** [SENT:insider_transactions]. Insiders are **net open-market
sellers (129 sells, −7.2M shares) with zero open-market buys**; a large −9.6M "J" disposition
adds to the supply. **Caveat:** for a post-IPO, stock-comp-heavy software name this is largely
routine 10b5-1 / VC-distribution selling, not a discretionary bearish cluster — a **soft
caution**, not a veto-grade contradiction.

**Effect on the phase-7b gate (illustrative, not applied to the immutable file):** this moves
the insider axis from `NA` to a **mild bearish contradiction**, which would take
`contradiction_count` from 0→1 and `tier_adjustment` from CONFIRM→**CAUTION** (cut one size
step). **But** §1's "FY guide above consensus" is a mild bullish offset on the earnings_trend
axis, and the trade was **already** cut to **starter (1.25%)** by the phase-8b debate gate — so
the practical sizing outcome is unchanged. Net of §1+§2: the two new fundamental signals
roughly cancel; conviction stays 0.55, structure stays defined-risk.

## 3. Correlation matrix — recovered from local prices (UW tool's lookup is broken)

**Root cause.** UW `risk_portfolio_correlation(PATH,ENPH,NTAP,SYM)` returned all sectors
`"Unknown"` and `high_correlations: null`. This is a **tool-side limitation**: it relies on a
**yfinance-based sector/price lookup** (the same Yahoo wall as §1), **not** missing data — the
local `stock-screener-2026-05-22.parquet` carries both `sector` (PATH/ENPH/NTAP = Technology,
SYM = Industrials) and `close`. Computed directly from local screener `close` series (30
return observations across the 31 available, gap-aware sessions):

**30-session daily-return correlation matrix** [CTX:price_corr DUCKDB]:

|       | ENPH | NTAP | PATH | SYM  |
|-------|------|------|------|------|
| ENPH  | 1.00 | 0.23 | 0.02 | −0.01|
| NTAP  | 0.23 | 1.00 | −0.01| 0.37 |
| PATH  | 0.02 | −0.01| 1.00 | −0.17|
| SYM   | −0.01| 0.37 | −0.17| 1.00 |

| Pair | corr | Verdict |
|---|---|---|
| PATH~ENPH | **+0.02** | no cluster |
| PATH~NTAP | **−0.01** | no cluster |
| PATH~SYM | **−0.17** | no cluster |

**Read:** **PATH is idiosyncratic** vs the concurrent book — no pair ≥0.70 (cluster) or
0.60–0.70 (soft-watch). Notably the phase-6 qualitative **"PATH/SYM automation soft-watch" is
NOT supported** by price action (they are slightly *negatively* correlated, −0.17). The
correlation gate is now a **measured** no-op, upgrading phase-6's "no usable coefficients."
**Unchanged operational note:** NTAP reports the **same evening (05-28)** as PATH — that is
*event-date* clustering (two positions resolving on one print), distinct from the ~0 price
correlation, and remains a desk-awareness item.

## Net effect on the blueprint

- **Forward consensus (§1):** mildly bullish (FY guide above Street). ↑ long-lean slightly.
- **Insider selling (§2):** mildly bearish (net sellers, no buys). ↓ long-lean slightly.
- **Correlation (§3):** confirmed no cluster (measured). → correlation gate stays a no-op.

**Conclusion: no change.** §1 and §2 offset; §3 confirms an existing no-op. The blueprint's
**NEUTRAL/mild-long, defined-risk (06-18 iron condor primary), starter size 1.25%, conviction
0.55** stands. If anything, the recovered insider-selling and the now-visible "guide above
consensus" both argue for **keeping it defined-risk** rather than a naked directional bet —
the same posture the chain already chose.

## Calibration-loop flags (for `/deep-dive-calibration`)

1. **phase-7b:** Finnhub forward estimates are paid-tier; route consensus via WebSearch and
   MSPR via `insider-transactions` (code-filtered), not `insider-sentiment`.
2. **phase-6:** `risk_portfolio_correlation` is unreliable (yfinance sector/price lookup
   fails); compute correlation from the local screener `close` series (DuckDB) instead.
3. **phase-0:** do not infer spot from an unusual-volume strike (the $17 lottery-call error,
   corrected in phase-0.5).

## Source calls (audit)

| Source | Status | Result |
|--------|--------|--------|
| Finnhub `eps/revenue-estimate`, `price-target`, `revenue-breakdown` | ❌ 403 | paid-tier (confirmed) |
| Yahoo `quoteSummary` earningsTrend/financialData | ❌ null | crumb/cookie auth wall |
| WebSearch (forward consensus) | ✅ | Q1 cons EPS ~$0.15–0.16, rev ~$397.5M; FY guide $1.754–1.759B > $1.74B cons |
| Finnhub `insider-sentiment` (MSPR) | ✅ empty | no MSPR series for PATH |
| Finnhub `insider-transactions` | ✅ | 129 S (−7.2M), 0 P; net open-market seller |
| DuckDB local screener `close` correlation | ✅ | PATH~{ENPH +0.02, NTAP −0.01, SYM −0.17} |

Sources: [American Banking News — PATH consensus](https://www.americanbankingnews.com/2026/05/21/uipath-path-expected-to-announce-earnings-on-thursday.html), [TipRanks — PATH earnings](https://www.tipranks.com/stocks/path/earnings)
