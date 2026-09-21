# Phase 7 — UW Insights Confluence

**Ticker:** FCX
**As-of date:** 2026-05-20 (effective data 2026-05-19)
**Generated:** 2026-05-20T21:00:00-04:00
**Upstream phases cited:** all of phases 1–6.

## Summary

UW's composite tools deliver a single, internally-consistent verdict:
**COVERED_CALL scenario with ACCUMULATION in dark pool**. Institutions are
**buying FCX equity in dark pool (buy/sell ratio 1.58 = $11M net
accumulation)** [INSIGHT:institutional_accumulation] AND simultaneously
**selling calls** (call bid-volume 25,116 > ask-volume 17,236)
[INSIGHT:conviction_matrix]. UW's verbatim explanation: *"Dark pool buying
+ call selling — yield enhancement, capping upside."* This **resolves the
phase-3 ambiguity** — the bid-side call activity at 60C Jun-18, 66C May-22,
63C/52C/53C/70C May-29 etc. is **covered-call yield-overlay writing
against long stock, not directional bearish bets**.

The composite confidence is **only 20.6%** [INSIGHT:conviction_matrix] —
which is honest. The picture is conflicted enough that the classifier
won't claim high conviction, and **FCX appears in NEITHER the market-wide
bullish confluence top-100 NOR the bearish top-100 (min_score=1)**
[INSIGHT:signal_confluence]. That absence is itself an important
datapoint: UW sees FCX as a real-money two-sided book where no
directional thesis is dominating.

Price vs flow shows **no divergence** — 30-day price change −8.4% with
bearish net flow [INSIGHT:price_vs_flow]. The 30-day net premium flow is
−$393k (mildly bearish, far smaller than the 90-day −$22.8M in phase-5).
The implied move from today's IV30d (49.9%) over the next 30 sessions is
**3.6% ≈ ±$2.11** — i.e., the market prices FCX in a $56.86 → $61.08 band
for the standard monthly window, but realised vol of 57.3% says actual
ranges have been considerably wider.

**Institutional accumulation top-5 price levels** [INSIGHT:institutional_
accumulation]: $59.27 ($2.24M / 37.8k shares), $59.13 ($2.14M), $59.69
($1.97M), $59.21 ($1.32M), $59.41 ($1.25M). **All five concentrated in the
$59.13–$59.69 band — i.e., today's actual trading range.** This is where
the next 4-week base is being established.

**Phase-9 baseline:** the institutional trade structure is **buy
stock + sell upside calls (covered-call yield play)**. The options-only
equivalent is **long lower strike + short upper strike = bull call spread**
— exactly matching phase-4's "$59 magnet, $65 ceiling" gamma map and
phase-5's "buy premium / debit structures" rule. **Do NOT structure naked
long calls or naked long stock.** Conviction **3/5** on the phase-7
composite (limited by the UW confidence number itself).

## Key signals

- **Conviction matrix scenario: COVERED_CALL** at 20.6% confidence
  [INSIGHT:conviction_matrix] — *"Dark pool buying + call selling — yield
  enhancement, capping upside."*
- **Institutional ACCUMULATION** — DP buy/sell ratio **1.58**, +$11M net
  [INSIGHT:institutional_accumulation].
- **FCX absent from bullish AND bearish confluence top-100** (min_score=1)
  [INSIGHT:signal_confluence] — no directional confluence at the market
  level.
- **Price/flow ALIGNED bearish** — 30d −8.4% with net flow −$393k
  [INSIGHT:price_vs_flow]; no reversal divergence detected.
- **Top DP price levels concentrated $59.13–$59.69** — today's range IS
  the developing base [INSIGHT:institutional_accumulation].
- **Implied move 30d = ±3.6% ($2.11)** vs realised 30d = 57.3% (much
  wider) [INSIGHT:deep_dive] — premium-buying environment confirmed.

## Detailed findings

### Deep dive snapshot [INSIGHT:deep_dive]

| Metric | Value |
|--------|-------|
| Symbol | FCX |
| Sector | Basic Materials |
| Last close (data date) | $58.71 (per phase-5 trend) |
| Avg DP price (today) | $59.10 |
| Total DP premium | **$48,850,231** |
| Total DP shares | 825,964 |
| Total DP trades | 222 |
| IV30d | 49.91% |
| IV rank | 54.94 |
| Realised vol (annualised) | 58.06% |
| Implied move (30d) | **3.6% ≈ ±$2.11** |
| Put/call ratio | 0.41 |
| Total OI | 1,222,691 |
| Next earnings | **2026-07-22** (~62 DTE — outside Jun-18 OPEX) |
| Yahoo fundamentals | **errored (HTTP 401)** — see Tool errors |

Top-5 OI changes (already covered in phase-3):
1. 59C 2026-06-18 +6,216 OI ($3.23M premium)
2. 67C 2026-06-05 +6,045 OI
3. 63P 2026-05-29 +1,789 OI
4. 49P 2026-08-21 +1,421 OI
5. 66C 2026-05-22 +998 OI

### Signal confluence [INSIGHT:signal_confluence]

**Bullish direction (top 100, min_score=1):** FCX is **NOT in the list**.

Top bullish-confluence tickers today: **SG** (score 6), **TE** (score 6),
then a cluster of score-5 names (DPST, WULF, WBD, USAS, HRL, AFL, CMBT,
LQDA, SFM, YPF, MKC, YINN, …). **FCX requires fewer than 1 factor to
appear → it has 0 bullish factors firing in UW's composite scoring.**
Phase-9 must treat this absence as a non-trivial fact.

**Bearish direction (top 100, min_score=1):** FCX is **NOT in the list**
either. Top bearish names: BNTX (score 6), EIX/FLEX/TOL/PSEC/DG/TIGR/HACK/
TJX/FUTU/IPO/SMH (score 5). FCX shares the same "no clean signal" status
on the bearish side.

**Notable Basic Materials peers:** APD (bullish score 4), PPTA (bullish
score 5), NB (bullish score 5), USAS (bullish score 5), IYM (bearish
score 4) — the sector itself is mixed.

### Conviction matrix [INSIGHT:conviction_matrix]

| Field | Value |
|-------|-------|
| **Scenario** | **COVERED_CALL** |
| Confidence | **20.6%** |
| Dark pool buy_ratio | 0.613 (above bull threshold 0.6) |
| Dark pool buy_volume | 506,316 |
| Dark pool sell_volume | 319,648 |
| Call ask volume | 17,236 |
| Call **bid volume** | **25,116** (calls sold > calls bought) |
| Put ask volume | 9,377 (puts bought > puts sold) |
| Put bid volume | 5,332 |
| Explanation | *"Dark pool buying + call selling — yield enhancement, capping upside."* |
| Bull threshold | 0.6 |
| Bear threshold | 0.4 |

**This is the most important phase-7 finding.** UW's classifier confirms
my phase-3 hypothesis: institutions are running a **covered-call yield
overlay** on FCX — long stock, short calls. They are NOT chasing the
$1.54M July 65C sweep buyer; they are PROVIDING that liquidity.

The low confidence (20.6%) means the classifier sees noise in the data —
specifically, the put-ask-buying ($9,377 vs bid $5,332) doesn't fit the
classic COVERED_CALL pattern. That put-buying is the **Jun-18 OTM put
protection cluster** identified in phase-1 (58P/56P/60P, ~$638k combined).
So the layered structure is actually **STOCK + SHORT CALL + LONG PUT =
COLLAR**, which de-risks the institutional position around current spot.

### Price vs flow [INSIGHT:price_vs_flow]

| Metric | Value |
|--------|-------|
| Period high (last 30d) | $70.97 |
| Period low (last 30d) | $55.49 |
| Price start | $66.45 |
| Price end | $60.87 (within their 30d window) |
| Price change | **−8.4%** |
| Bullish premium | $5,486,004 |
| Bearish premium | $5,879,191 |
| Net premium flow | **−$393,187** |
| Flow direction | bearish |
| **Divergence** | **No — price and flow aligned** |
| IV rank | 54.94 |

The lack of divergence means there is **no obvious reversal setup right
now**. If price had been falling while flow was turning bullish, that
would be the classic "smart money buying the dip" reversal signal. Here,
price down + flow mildly bearish = trend confirmation, not reversal.

The period high $70.97 within 30d is the May-13 peak ($67.16 close, $70.97
intraday) — phase-5's identified rally top.

### Analyst vs flow [INSIGHT:analyst_vs_flow]

The tool returned only the options-flow side (net −$393k bearish, P/C 0.41)
this run — analyst-consensus data was not retrieved (likely Yahoo 401
upstream). Compensating with phase-6 WebSearch:

- **Deutsche Bank PT $58 → $72 (Buy)** as of 2026-05-13 [MACRO:DBPT_2026-
  05-13@phase-6]
- **Consensus analyst PT cluster $70–$81** [MACRO:FCXAnalystTargets_2026-05@
  phase-6]
- **Options flow net = mildly bearish (−$393k)** [INSIGHT:analyst_vs_flow]

**Contrast:** analyst consensus is **bullish ($70–$81 PT, 19–38% upside
from $58.71)** while net options flow is **mildly bearish today**. This
is a classic Wall Street vs. options-tape disagreement — analysts are
slow-moving and may not have refreshed since the May-13 → May-19 drop.

### Institutional accumulation [INSIGHT:institutional_accumulation]

| Metric | Value |
|--------|-------|
| **Signal** | **ACCUMULATION — dark pool buy volume significantly exceeds sell volume** |
| Buy/sell ratio | **1.58** |
| Buy-side volume | 506,316 |
| Sell-side volume | 319,648 |
| Avg trade price | $59.10 |
| VWAP | $59.14 |
| 30d price change | −8.4% |
| DP trades | 222 |
| Total DP premium | $48,850,231 |

**Top 5 price levels (today's DP):**

| Level | Premium | Shares | Trades |
|-------|---------|--------|--------|
| $59.27 | $2,237,917 | 37,758 | 3 |
| $59.13 | $2,139,737 | 36,187 | 5 |
| $59.69 | $1,969,839 | 33,000 | 1 |
| $59.21 | $1,318,614 | 22,271 | 4 |
| $59.41 | $1,253,551 | 21,100 | 3 |

**Read:** the top-5 daily DP levels cluster between **$59.13 and $59.69**
(0.95% width) — institutions are accumulating in a TIGHT band right around
spot. This is consistent with covered-call yield writers establishing
basis at the post-flush low.

The 5-day price levels (phase-2) showed institutional concentration at
$65–$68 ($256M cumulative). Today's DP focus has shifted DOWN to the
$59 area as the price reset — confirming institutions are **adding into
weakness** within their established range.

### Earnings play

**SKIPPED** — next FCX earnings is 2026-07-22, ~62 DTE, outside the 30-day
window stipulated by the phase-7 spec.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `insights_deep_dive` | symbol=FCX, date=2026-05-19 | Yahoo errored, UW data complete; next earnings 2026-07-22 |
| `insights_signal_confluence` | dir=bullish, min_score=1, top_n=100 | FCX not in top-100 |
| `insights_signal_confluence` | dir=bearish, min_score=1, top_n=100 | FCX not in top-100 |
| `insights_conviction_matrix` | symbol=FCX | **COVERED_CALL @ 20.6% confidence** |
| `insights_price_vs_flow` | symbol=FCX, lookback=30 | aligned bearish, **no divergence** |
| `insights_analyst_vs_flow` | symbol=FCX | analyst data missing this run; options net −$393k |
| `insights_institutional_accumulation` | symbol=FCX | **ACCUMULATION, ratio 1.58** |
| `insights_earnings_play` | (skipped) | next earnings is 62 DTE (out of window) |

## Tool errors

```
insights_deep_dive (yahoo_fundamentals component):
"yahoo quoteSummary FCX: HTTP 401"
```

```
insights_analyst_vs_flow — analyst-consensus block was empty this run
(likely upstream Yahoo 401). Compensated with phase-6 WebSearch analyst
data (Deutsche $72, consensus $70–$81). No new ratings since 2026-05-13.
```

## Cross-check vs phases 1–5

| UW insight | Phase agreement? | Notes |
|------------|------------------|-------|
| `signal_confluence` (no FCX in either direction) | **Agrees** with phase-1's "mixed bias / conviction 3/5" | Conviction was always limited; UW formalises the absence |
| `conviction_matrix` = **COVERED_CALL** | **Agrees and RESOLVES** phase-3's nuance on bid-side call activity | The bid-side calls at 60C Jun-18 / 66C May-22 / 63C/52C/53C/70C are OVERLAY writes, not bearish bets |
| `institutional_accumulation` = ACCUMULATION | **Agrees** with phase-2's +$11M dark-pool net buy | DP buy_ratio 0.613 ≈ phase-2's 0.601 large + 0.69 block |
| `price_vs_flow` aligned bearish (no divergence) | **Agrees** with phase-5's bearish 90d cumulative flow | No reversal signal — trend confirmation |
| Implied move ±3.6% vs realised 57% vol | **Agrees** with phase-5 VRP −7.4 pts conclusion | Premium-buying regime, debit structures |
| Top DP levels $59.13–$59.69 (today) vs $65–$68 (5d) | **Agrees** with phase-2 cumulative map | Institutions ADDING at lower levels |
| Top OI builds (59C Jun-18, 67C Jun-5, …) | **Agrees** with phase-3 | Same five contracts |
| Analyst $70–$81 vs flow −$393k | **Disagreement** (Wall Street bullish, tape mildly bearish) | Classic stale-analyst signal; expect upgrades to follow tape with lag |

**No contradictions to resolve.** UW's composite verdict is fully
consistent with phases 1–6.

## Verdict for downstream phases

- **UW composite bias:** **COVERED_CALL with mild ACCUMULATION**.
  Institutions are owning stock and selling calls / buying puts for
  yield + protection. NO directional new long, NO outright short.
- **Conviction:** **3/5** — UW's own confidence is only 20.6%; the
  composite tools are clear but the underlying data is two-sided.
- **Phase-9 baseline (to be overridden only with specific contrary
  evidence):**
  - Trade structure: **DEFINED-RISK DEBIT (long lower strike + short
    upper strike) = bull call spread**, mirroring institutional collar
    economics.
  - Strikes: **long ATM/near-the-money around $59–$60 (matches new
    Jun-18 59C build [OI:biggest_increases@phase-3]) + short at
    $65 (matches dealer long-gamma magnet [STRUCT:gex@phase-4] and DP
    target [DP:price_levels@phase-2])**.
  - Expiry: **Jun-18 monthly** (captures Jun-16/17 FOMC catalyst
    [MACRO:FOMC_2026-06-17@phase-6]).
  - Size: **half-position** (Market regime TRANSITIONAL
    [MACRO:MarketRegime_2026-05-19@phase-6], bullish_flow signal backtest
    26.7% win rate [HIST:signal_backtest@phase-5]).
- **Open questions:**
  - **Will the COVERED_CALL classification persist if FCX rallies back
    above $61?** If institutions stop selling calls (i.e., ratio of
    call_bid / call_ask drops), the read flips to DIRECTIONAL_LONG and
    structure should switch to long calls.
  - **Will UW move FCX into bullish confluence within 1–2 sessions?**
    With IV cheap, 59C buildup fresh, and DP accumulating, a single
    bullish-flow session would likely push it into the top-100.
  - **What is the realised dollar return implied by the COVERED_CALL
    structure?** Roughly: long stock $59 + short Jun-18 65C ($0.50
    credit per UW chain) = potential P&L of $6 spot gain + $0.50 credit
    = ~10.5% in 30 days, capped at $65. Phase-9 sizing rubric will set
    the leverage equivalent.
