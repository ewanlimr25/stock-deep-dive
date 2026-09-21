# Phase 7 — UW Insights Confluence

**Ticker:** BE
**As-of date:** 2026-07-21
**Generated:** 2026-07-22T08:38:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-5-historical.md, phase-0.5-context.md

## Summary

The composite instrumentation reads BE as **CONTESTED / MIXED — not the clean
bullish stack the flow lean implied.** The dark-pool-and-volume-weighted tools
lean mildly *bearish* (conviction-matrix **DIRECTIONAL_SHORT at just 15.4%
confidence**; institutional-accumulation **DISTRIBUTION**, buy/sell 0.58),
corroborating phase-2's dark-pool yellow flag. The reversal lens leans *bullish*
(**price-vs-flow DIVERGENCE**: price −10.8% but flow +$25.5M bullish),
corroborating phase-5's bounce-off-197. Tellingly, **BE ranks in neither the
bullish nor the bearish signal-confluence top-40** — it is a middling name on the
composite score, not a standout on either side. The reconciliation that matters:
the composite's bearish tag is **volume-weighted** (raw put volume + DP sell
classification), whereas phase-1's bullish read is **premium-weighted** (puts net
*sold* $25.7M, LEAP calls bought) — the cheap 110P lottery (18k contracts, $160k)
inflates put *volume* without being bearish *money*. Baseline for phase 9:
**mildly bullish reversal thesis with a real institutional-distribution overhang —
size it as contested, not conviction.**

## Key signals

- **Conviction-matrix: DIRECTIONAL_SHORT, confidence only 15.4%** — "dark pool selling + put buying, institutional bear bet" `[INSIGHT:conviction_matrix]`
- **Institutional-accumulation: DISTRIBUTION** (buy/sell 0.58, buyVol 1.30M vs sellVol 2.25M) — agrees w/ phase-2 `[INSIGHT:institutional_accumulation]`
- **Price-vs-flow: DIVERGENCE (bullish)** — price −10.8%, flow +$25.5M → reversal signal, agrees w/ phase-5 `[INSIGHT:price_vs_flow]`
- **BE absent from BOTH bullish and bearish signal-confluence top-40** — middling composite score `[INSIGHT:signal_confluence]`
- **Analyst-vs-flow: flow bullish** (net +$25.5M); analyst consensus data absent (yfinance) `[INSIGHT:analyst_vs_flow]`

## Detailed findings

### Deep-dive snapshot (whole-tape aggregates) `[INSIGHT:deep_dive]`

Re-stated from phase-0.5/phase-1 `uw_screener` block (same source): `bullish_premium`
$117.0M vs `bearish_premium` $91.5M → **net_flow +$25,457,620**; `call_premium`
$127.2M vs `put_premium` $122.4M (net call +$4.8M); `put_call_ratio` **2.046**;
`iv_rank` **98.78**; `implied_move`/`implied_move_perc` **$23.89 / 10.6%**;
DP `total_premium` $794.9M @ avg 222.41. Consistent with phases 1 & 0.5.

### Signal confluence `[INSIGHT:signal_confluence]`

Market-wide, `--min-score 1`, top-40, both directions: **BE is in neither list**
(tickers_found 40 each). BE's composite confluence score is below the cohort on
*both* sides → the instrumentation does not see a strong one-way signal here. This
is the single most important phase-7 datapoint: it caps how confidently phase-9
can call this directional.

### Conviction matrix `[INSIGHT:conviction_matrix]`

`scenario` **DIRECTIONAL_SHORT**, `confidence_pct` **15.4%** (thresholds bull 0.6 /
bear 0.4). options_flow volume split: put_ask 51,109 / put_bid 46,995 (puts
slightly ask-side by *volume*), call_ask 20,641 / call_bid 20,821 (balanced);
dp buy_ratio 0.367. `explanation`: *"Dark pool selling + put buying — institutional
bear bet."* **Flagged disagreement:** this is a *low-confidence* (15.4%) tag built
on **volume**, not premium. Phase-1's premium-weighted sweeps show puts net
**sold** $25.7M and LEAP calls bought — the opposite directional inference. The
15.4% confidence itself signals the tool is unsure; I down-weight the SHORT label
but carry the underlying DP-distribution concern (it echoes phase-2).

### Price vs flow `[INSIGHT:price_vs_flow]`

`divergence` **true**, `divergence_signal`: *"Price is down 10.8% but options flow
is bullish (net $25,457,620)"*, `flow_direction` bullish, iv_rank 98.78, period
high 351.28 / low 194.6. A **bullish reversal divergence** — the leading-reversal
heuristic — which aligns with phase-5's +14.8% bounce off the 197 floor. Per the
pitfall, such divergences are often early; pair with phase-4 (short-gamma amplifies
whichever way the earnings break resolves it).

### Analyst vs flow `[INSIGHT:analyst_vs_flow]`

Returned only the `options_flow` side (flow_sentiment **bullish**, net +$25.5M);
the analyst-consensus half is **absent** (yfinance analyst data not returned).
Cannot score Wall-Street-vs-trader agreement here — phase-7b/WebSearch carry the
analyst view (consensus is constructive on the AI-power growth, per phase-6).

### Institutional accumulation `[INSIGHT:institutional_accumulation]`

`signal` **DISTRIBUTION** — "dark pool sell volume significantly exceeds buy
volume"; buy_sell_ratio 0.58, buy_side_volume 1,300,308 vs sell_side_volume
2,245,895 over 1,964 trades; 30d price −10.77%, avg trade price 222.41. **Agrees
with phase-2's mega-tier sell**, though phase-2 attributed the bulk to post-close
crossing prints (non-directional). Net: a genuine distribution *overhang* on the
DP tape — the clearest bearish counterweight in the whole run.

### Earnings play `[INSIGHT:earnings_play]`

BE **not among the top-10** earnings-play setups returned (despite IV rank 98.8) —
its two-sided flow (written puts + LEAP calls) does not read as a clean long-vol or
directional earnings setup on the tool's ranking. Earnings context is fully covered
by phase-6 (7/28 AMC, +106.5% rev guide) and phase-4 (backwardation, ±10.6% move).

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Notes |
|------------------|--------------------------|-------|
| `insights conviction-matrix --symbol BE` | DIRECTIONAL_SHORT 15.4% ← `.scenario/.confidence_pct` | low-conf; volume-based |
| `insights price-vs-flow --symbol BE --lookback-days 30` | DIVERGENCE bullish ← `.divergence/.divergence_signal` | reversal |
| `insights analyst-vs-flow --symbol BE` | flow bullish ← `.options_flow.flow_sentiment` | analyst side absent |
| `insights institutional-accumulation --symbol BE` | DISTRIBUTION 0.58 ← `.signal/.buy_sell_ratio` | agrees phase-2 |
| `insights earnings-play --days-until-earnings 30` | BE not in top-10 ← `.results｜select(.symbol=="BE")` empty | out of top ranking |
| `insights signal-confluence --direction bullish/bearish --min-score 1 --top-n 40` | BE in neither list | middling |

## Tool errors

<none — all reads valid JSON. `analyst-vs-flow` returned no analyst-consensus
block (yfinance data absent); `earnings-play`/`signal-confluence` are market-wide
rankings where BE simply did not appear (recorded, not errors).>

## Cross-check vs phases 1–5

| UW insight | Phase agreement? | Notes |
|------------|------------------|-------|
| signal_confluence (absent both sides) | **partial** | Middling composite — tempers phase-0.5's "GENUINELY_UNUSUAL" (that was net-dir premium; composite doesn't rank it a standout) |
| conviction_matrix (DIRECTIONAL_SHORT, 15.4%) | **disagrees w/ phase-1** | Volume-weighted & low-confidence; phase-1 premium-weighted is bullish (puts *sold*). Carry the DP concern, down-weight the SHORT label |
| institutional_accumulation (DISTRIBUTION) | **agrees w/ phase-2** | Confirms the DP-tape distribution overhang (phase-2 tied bulk to post-close crosses) |
| price_vs_flow (bullish divergence) | **agrees w/ phase-5** | Confirms bounce-off-197 reversal read |

## Verdict for downstream phases

- **UW composite bias:** **MIXED / CONTESTED**, tilting *mildly bullish* only via
  the reversal-divergence + premium-weighted flow, against a real **DP distribution
  overhang** and a middling confluence score.
- **Conviction:** **2.5 / 5** — the instrumentation is split; this is the phase
  that says "don't treat the bullish flow as a clean signal."
- **Phase-9 baseline:** treat BE as a **contested reversal-off-197 into earnings**,
  NOT a high-conviction directional long. The premium-selling edge (phase-5 VRP)
  and put-write floor are the strongest legs; the DP distribution + short-gamma
  downside (phase-4) + middling confluence are the counterweights. Override toward
  more-bullish ONLY if phases 7b/7c/8 add fundamental/positioning support.
- **Open questions:** Do fundamentals (phase-7b) justify the +106% revenue guide
  and the bounce, or is the −35% drawdown warranted (which would validate the DP
  distribution)? Does short interest / sentiment (phase-7c) show a squeeze setup
  that explains the bounce? Can the desk agents (phase-8) reconcile premium-weighted
  bullish flow vs volume/DP-weighted distribution?
