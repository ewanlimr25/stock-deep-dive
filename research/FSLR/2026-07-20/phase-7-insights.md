# Phase 7 — UW Insights Confluence

**Ticker:** FSLR · **As-of:** 2026-07-20 · **Version:** v1 · **Generated:** 2026-07-20
**Cites:** phase-1-flow.md (net_flow −$3.8M, short-vol); phase-2-dark-pool.md (mild
accumulation, neutral); phase-5-historical.md (−26.4% downtrend); phase-4 (short γ).

## Summary

UW's composite tools return a **MIXED, low-confluence verdict** — the bearish tape
is real and *aligned with the downtrend*, but it does **not** stack into a clean
directional signal on this instrumentation. The conviction matrix reads **MIXED
(confidence 7.5%)**; price-vs-flow shows **no divergence** ("price and flow are
aligned," both bearish, price −26.4% and sitting near the period low $203.77);
institutional-accumulation is **NEUTRAL** (dark-pool buy/sell 1.35). Critically,
**FSLR appears in neither the bullish nor the bearish `signal-confluence` top-40**
— its bearish flow is *not* joined by the put-heavy PCR, volume spike, or dark-pool
distribution that a high-score bearish name (e.g. INFY, score 6) carries. The one
genuine cross-signal is **analyst-vs-flow divergence**: options flow is bearish
while Street consensus (phase-6) is *Moderate Buy*. Net: the composite gives phase-9
a **muddy baseline — mild bearish tactical drift on top of a downtrend, with no
confirming confluence and a bullish analyst/mild-accumulation counterweight.**

## Key signals

- **[INSIGHT:conviction_matrix]** **MIXED** (confidence 7.5%): DP buy_ratio 0.575
  (between bear 0.4 / bull 0.6 thresholds), calls sold on bid (call_bid_vol 18,864
  ≫ call_ask 3,207) → "balanced, no clear bias."
- **[INSIGHT:price_vs_flow]** **No divergence** — flow bearish, price −26.4%,
  aligned = **trend continuation**, not a reversal; price near period low $203.77.
- **[INSIGHT:signal_confluence]** FSLR **absent from both** bullish and bearish
  top-40 (min-score 1) → no clean confluence stack either direction.
- **[INSIGHT:institutional_accumulation]** **NEUTRAL** — buy/sell 1.35 (55,337 /
  40,969), top level $205.31 ($6.2M, 25 trades). Mild-buy but labeled balanced.
- **[INSIGHT:analyst_vs_flow]** flow **bearish** (net −$3.8M) vs Street **Moderate
  Buy** (phase-6) → **analyst/flow divergence** (a caution for the short).

## Detailed findings

### Deep-dive snapshot `[INSIGHT:deep_dive]`
Whole-tape (uw_screener) — reconciles with phase-1/0.5:
- bullish_prem $11.89M vs bearish_prem $15.69M → **derived net_flow −$3.80M**
- call_prem $17.23M vs put_prem $12.55M; P/C (prem) 0.418
- **implied_move ±$10.89 / ±5.31%** (phase-9 N4 sizes to this)
- IV rank **99.1**; total OI 541,050
- *Yahoo fundamentals block empty this run* (PE/mcap/short% null) → those come from
  **phase-7b** (Finnhub/fz), not here.

### Signal confluence `[INSIGHT:signal_confluence]`
FSLR **not in bearish top-40 nor bullish top-40** (score < 1 both sides). A clean
bearish name this session (INFY, score 6) carries `bearish_flow + high_pcr +
volume_spike + dp_distribution + oi_building_puts + high_iv_sell_premium`. FSLR has
only **bearish_flow + oi_building_puts (partial) + high_iv**; it **lacks** high_pcr
(PCR call-heavy 0.42), volume_spike (vva 0.69, below avg), and dp_distribution (DP
neutral). That gap is *why* the setup is MIXED, not a screaming short.

### Conviction matrix `[INSIGHT:conviction_matrix]`
Scenario **MIXED**, confidence 7.5%. DP buy_ratio 0.575, 83 trades. Options: calls
overwhelmingly sold on bid, puts modestly sold on bid → short-vol signature, no
clean directional conviction. Explanation: "Balanced dark pool activity — no clear
bias."

### Price vs flow `[INSIGHT:price_vs_flow]`
**divergence = false** ("Price and flow are aligned"). flow bearish, price
$279.01 → $205.31 (−26.4%), period high $306.55 / low $203.77 → price pinned near
the LOW. This is **bearish trend continuation** confirmation, not the bullish-
reversal divergence that would fire if flow were bullish into a falling price.

### Analyst vs flow `[INSIGHT:analyst_vs_flow]`
Tool returned only the options side (flow_sentiment **bearish**, net −$3.8M);
the analyst/yfinance leg was empty this run. Cross-referencing phase-6's WebSearch
consensus (**Moderate Buy**, 17 Strong Buy / 10 Hold / 3 Strong Sell, target
implied upside), **the Street is bullish while options flow is bearish** → a
divergence that phase-8b must weigh (analysts slow vs flow fast, or flow wrong).

### Institutional accumulation `[INSIGHT:institutional_accumulation]`
Signal **NEUTRAL** ("balanced dark pool activity"), buy/sell ratio **1.35**,
buy-side vol 55,337 / sell-side 40,969, avg price $206.67, 83 DP trades. Top
levels: $205.31 ($6.2M, 25 trades), $208.43, $204.66. Mild buy-tilt but not a
distribution signal → **corroborates phase-2's "mild accumulation / tension"**.

### Earnings play `[INSIGHT:earnings_play]`
FSLR **not in the earnings-play top-10** (all top-10 carry IV rank exactly 100;
FSLR's 99.1 sits just below the cutoff). Earnings *is* in-window (07-30, phase-6),
so the setup qualifies conceptually — it's simply edged out of the top-10 by names
at IVR 100. Treat as: high-IV pre-earnings name, not a top-ranked earnings-vol play.

## Tool calls
| Tool | Args | Result |
|------|------|--------|
| insights conviction-matrix | FSLR, date 07-20 | MIXED, conf 7.5% |
| insights price-vs-flow | FSLR, 30d | no divergence, aligned bearish |
| insights analyst-vs-flow | FSLR | flow bearish; analyst leg empty |
| insights institutional-accumulation | FSLR | NEUTRAL, buy/sell 1.35 |
| insights earnings-play | 30d (market) | FSLR outside top-10 (IVR cutoff) |
| insights signal-confluence | bearish, min-score 1, top 40 | **FSLR absent** |
| insights signal-confluence | bullish, min-score 1, top 40 | **FSLR absent** |
| insights deep-dive | FSLR (uw_screener) | net_flow −$3.8M, IVR 99.1 |

## Tool errors
None. `deep-dive` `yahoo_fundamentals` block returned empty (PE/mcap/short% null) —
not a tool error; those metrics are sourced in phase-7b. All reads parsed via `jq`.

## Cross-check vs phases 1–5

| UW insight | Phase agreement? | Notes |
|------------|------------------|-------|
| signal_confluence (absent both sides) | **weaker than phase-1** | Phase-1 called bearish (3/5); composite doesn't stack it → confirms "modest, not screaming." |
| conviction_matrix MIXED | **agrees phase-2** | Matches the flow-vs-DP tension. |
| price_vs_flow aligned bearish | **agrees phase-5** | Confirms downtrend continuation. |
| institutional_accumulation NEUTRAL | **agrees phase-2** | Mild-buy / balanced, not distribution. |
| analyst_vs_flow divergence | **new** | Street bullish vs flow bearish — feed to 7b/8b. |

## Verdict for downstream

- **UW composite bias:** **MIXED, mildly bearish tactically.** The bearish flow is
  aligned with a −26% downtrend and short-gamma structure, but it is **not
  confirmed** by DP (neutral/mild-buy), PCR (call-heavy), volume (below avg), or a
  confluence score — and it runs *against* bullish Street consensus.
- **Conviction: 2.5/5** — deliberately low; this phase is the honest "the composite
  does not see a clean edge here" checkpoint.
- **Phase-9 baseline:** treat FSLR as a **low-confluence, mild-bearish-drift** name,
  NOT a high-conviction short. Any directional sizing must lean on the phase-4
  short-gamma structure + phase-5 trend/backtest, and must respect (a) the neutral-
  to-accumulative DP floor at $205, and (b) the bullish analyst / policy-tailwind
  counterweight. Only override this MIXED baseline with the specific edges phases
  4/5/8 supply.
- **Open questions:**
  - Is the analyst-vs-flow divergence "flow is early/right" (short pays) or "flow is
    vol-selling noise while fundamentals hold" (analysts right)? → phase-7b/8b.
  - Does earnings (07-30) resolve the MIXED tape into a clean move, and which way,
    given price already sits at the period low ($203.77)?
  - Can a MIXED composite + a 90% (N=10) bearish backtest coexist — is the edge in
    the *structure/trend*, not the *flow confluence*?
