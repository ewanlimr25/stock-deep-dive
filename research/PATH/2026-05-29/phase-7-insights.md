# Phase 7 — UW Insights Confluence

**Ticker:** PATH · **As-of:** 2026-05-29 · **Generated:** 2026-05-29
**Upstream:** phases 1–6. Reconciles the composite tools against the bottom-up
read (gross-bullish / net-mixed, BUSY_NAME_NORMAL_DAY, no flow edge).

## Summary

UW's composite tools **split exactly along the gross-vs-net fault line this run
has flagged from the start.** The factor-checklist `signal-confluence` scores
PATH **5 of 6 bullish** (bullish_flow, low_pcr, volume_spike, dp_accumulation,
oi_building) — a rare, high-looking stack. But the *net-balance*
`conviction-matrix` returns **MIXED at just 6.7% confidence** ("balanced dark
pool activity — no clear bias"): the order book shows calls only mildly bought
(ask 90,850 vs bid 83,148), puts net *sold* (ask 22,015 vs bid 38,899), and DP
buy_ratio 0.567 — none of it clearing the 0.6 bull threshold.
`institutional-accumulation` agrees: **NEUTRAL**. The one clean constructive read
is `price-vs-flow`: **no divergence, price and flow aligned bullish** (price
+12.6% over the window, 10.41→11.72, net premium +$232K). So the composite
baseline is **tentatively bullish but shallow** — the bullish *factors are
present* (which is why confluence lights up) but the *conviction behind them is
thin* (which is why the net-balance tool says MIXED). This is a textbook
BUSY_NAME_NORMAL_DAY signature, and phase-5's 50% win rate says the bullish stack
has **no proven historical edge** on this name.

## Key signals

- **`signal-confluence` = 5/6 BULLISH** — factors: bullish_flow, low_pcr,
  volume_spike, dp_accumulation, oi_building `[INSIGHT:signal-confluence]`. High
  on factor *presence*; read against the net-balance caveat below.
- **`conviction-matrix` = MIXED, 6.7% confidence** — "balanced dark pool, no
  clear bias"; puts net sold, calls only mildly bought, DP buy_ratio 0.567
  `[INSIGHT:conviction-matrix]`. The honest net read.
- **`price-vs-flow` = ALIGNED, no divergence, bullish** — price +12.58%
  (10.41→11.72, hi 12.09 / lo 9.20), net premium +$232,542
  `[INSIGHT:price-vs-flow]`. No reversal signal; momentum and flow agree.
- **`institutional-accumulation` = NEUTRAL** — balanced DP
  `[INSIGHT:institutional-accumulation]`. Confirms phase-2's "block-tier buy but
  balanced large-tier" → not a clean accumulation flag.
- **`analyst-vs-flow`** — flow_sentiment bullish (net +$232K) but **no analyst
  consensus** returned (yfinance blank) `[INSIGHT:analyst-vs-flow]`; Street view
  deferred to phase-7b/7c.

## Detailed findings

### Deep dive snapshot
- Whole-tape `uw_screener` aggregates (reconciles with phase-1):
  bullish premium **$5.31M** vs bearish **$5.08M** → net **+$232,542** (faint
  bullish); call premium $9.47M vs put $2.29M; **P/C 0.346**; IV rank 43.3;
  **implied move 1.63%/day**; next earnings **2026-09-03**.
- DP total premium $74.5M / 433 trades (phase-2); short float 31.15% (phase-0).
- Matches phase-0.5 `[CTX:]`: 95th universe pctile total premium, but net-dir
  only moderately elevated.

### Signal confluence
Score **5/6**, factors `["bullish_flow","low_pcr","volume_spike",
"dp_accumulation","oi_building"]`. Missing factor presumably the net-aggressor /
sweep-persistence leg (phase-1 found no multi-day campaign). **Caveat:** this
tool rewards factor *presence*, not depth — every factor here is real but
shallow (gross call tilt, 0DTE-inflated volume, block-only DP buy, speculative
OI). Do **not** treat 5/6 as high conviction given the net-balance disagreement.

### Conviction matrix
**MIXED**, confidence **6.7%**. DP buy_ratio 0.567 (below 0.6 bull threshold);
options: call ask/bid 90,850/83,148 (mild buy), put ask/bid 22,015/38,899 (net
put *selling* = mild bullish). Net of everything: no clear bias. This is the
tool most aligned with the bottom-up read.

### Price vs flow
**No divergence** — "price and flow are aligned" (bullish). Price +12.58% over
the lookback, period high 12.09 (just under the $12 gamma wall / DP supply), low
9.20. Constructive: no leading-reversal warning.

### Analyst vs flow
Flow bullish; analyst consensus unavailable (deferred to phase-7b/7c Finnhub /
fz cross-source). No agreement read possible here.

### Institutional accumulation
**NEUTRAL** (balanced DP). Consistent with phase-2.

### Earnings play
Out of window — earnings 2026-09-03 (>30d). Tool skipped.

## Tool calls
| Tool | Args | Result |
|---|---|---|
| `insights conviction-matrix` | `--symbol PATH` | MIXED, 6.7% |
| `insights price-vs-flow` | `--lookback-days 30` | aligned bullish, no divergence |
| `insights analyst-vs-flow` | `--symbol PATH` | flow bullish, no consensus |
| `insights institutional-accumulation` | `--symbol PATH` | NEUTRAL |
| `insights signal-confluence` | `--direction bullish --min-score 1 --top-n 100` | PATH 5/6 |

## Tool errors
(none — `analyst-vs-flow` consensus blank is a yfinance gap, not an error.)

## Cross-check vs phases 1–6
| UW insight | Phase agreement? | Notes |
|---|---|---|
| signal-confluence 5/6 | **partial / overstated** | Agrees with phase-1 gross call tilt; *over*states vs phase-1 conviction 2/5 and phase-5 no-edge. Factor-presence, not depth. |
| conviction-matrix MIXED | **agrees** phases 1, 5, 0.5 | Matches the net-mixed read and BUSY_NAME_NORMAL_DAY. |
| institutional-accumulation NEUTRAL | **agrees** phase-2 | Block-buy but balanced large tier → net neutral. |
| price-vs-flow aligned bullish | **agrees** phase-5 momentum | Recovery + bullish flow, no reversal. |

## Verdict for downstream

- **UW composite bias: WEAKLY BULLISH / MIXED.** Bullish factors are present and
  price-flow is aligned, but the net-balance composite is MIXED (6.7%) and
  accumulation is NEUTRAL. The 5/6 confluence is a *breadth-of-factors* score,
  not a depth-of-conviction score — do not over-weight it.
- **Conviction: 2.5 / 5.**
- **Baseline for phase-9:** treat the setup as a **low-conviction tactical
  bullish lean**, capped by phase-0.5 (`+`), phase-5 (50% win rate / no edge),
  and the phase-4 $12 gamma cap. Override toward bullish ONLY if phase-7c shows
  short-interest squeeze fuel loading; override toward neutral/short if phase-7b
  fundamentals veto or phase-7c shows SI unwinding.
- **Open questions:**
  - Does the 31% short float (the non-flow edge phase-5 flagged) convert the
    weak bullish lean into a squeeze setup? → phase-7c.
  - Is the fundamental quality of PATH strong enough to support owning it, or is
    this a falling-knife recovery bounce? → phase-7b.
