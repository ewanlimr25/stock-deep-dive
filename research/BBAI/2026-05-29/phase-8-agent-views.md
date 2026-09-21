# Phase 8 — Multi-Agent Analyst Desk

**Ticker:** BBAI
**As-of date:** 2026-05-29
**Generated:** 2026-05-31
**Upstream phases cited:** phase-1 … phase-7c (all)

## Summary

Five specialist desk agents ran in parallel against the on-disk phases 0.5–7c.
**None went long.** The plurality is **NEUTRAL / range / sell-vol (4 of 5)** with
one **defined-risk SHORT** (contrarian-scanner); **average conviction 2.4/5** (low).
The desk converges hard on a single expression: **a defined-risk premium-selling
structure pinned to the $5 long-gamma level** (iron condor ≈ short $4.5P/$5.5–6C, or
a $5.5/$6.5 call-credit spread into 6/18 OPEX), **half-size or less** per the
"reduce size" regime — explicitly **no naked short** and **no directional long**.
The **unanimous top risk is the 26.37% short-float squeeze** through the $5.50 call
wall on a fresh defense-contract headline.

## Agent verdicts table

| Agent | bias | conviction | horizon | one_line_take |
|-------|------|-----------|---------|---------------|
| accumulation-hunter | NEUTRAL | 2 | 1-4w | "Buy-lean is sub-threshold (0.55/1.22), the only block was a sell — not accumulation; fade, don't chase." |
| contrarian-scanner | SHORT (defined-risk) | 3 | 1-5d/1-4w | "Price +31% on net-negative premium into a complacent-skew long-gamma $5 pin — sell the call skew." |
| sweep-tracker | AVOID | 2 | 1-5d | "Sweeps lean bid (call writing), premium net-negative — no momentum-long; if anything fade to $5." |
| earnings-scout | SELL VOL / NEUTRAL | 3 | 1-4w | "No catalyst till 8/10, IV rich (VRP +0.28), $5 gamma pin — harvest premium, keep wings for the squeeze." |
| risk-monitor | NEUTRAL | 2 | 1-4w | "TRANSITIONAL regime says reduce size; no backtest edge, conflicting signals — watch-only / half-unit defined-risk." |

**Distribution:** LONG 0 · SHORT 1 · NEUTRAL/RANGE/SELL-VOL 4. Avg conviction **2.4/5**.

## Per-agent details

### accumulation-hunter — NEUTRAL (2)
- top_signal: institutional-accumulation fires **NEUTRAL, buy_sell_ratio 1.22 / buy_ratio 0.55** (sub-0.6 threshold); large tier $43.29M buy_ratio 0.581 **but the only block print was a $2.44M SELL**, mega/retail $0 [phase-2/7].
- top_risk: thin downside air-pocket — first real put support only at $3.5/$3 (−31%/−41%); a failed $5 pin can gap fast.
- levels: support $5.00 · resistance $5.50 · invalidation DP buy_ratio >0.60 + net call premium positive.

### contrarian-scanner — SHORT, defined-risk (3)
- top_signal: **price +30.9% but net options premium −$999,867** (price-vs-flow DIVERGENCE) + **skew COMPLACENT 0.815** + long-gamma **$5 pin (+$82.0M GEX)**, max-pain $4 [phase-7/4].
- trade: **$5.50/$6.50 call-credit spread into 6/18**, or iron condor centered $5 (short $4.5P/$5.5C); small size.
- top_risk: 26.37% short float (~133.8M sh, ~3 DTC) + contract catalysts → covering squeeze to max loss.
- levels: support $5.00 · resistance $5.50 · invalidation daily close >$5.50 on positive net call premium.

### sweep-tracker — AVOID (2)
- top_signal: sweeps (20, all calls $5.06M) **lean bid $2.54M > ask $2.30M** = call writing; net_call_premium −$999,867; long-gamma $5 pin caps squeeze [phase-1/4].
- top_risk: a clean break/hold above $5.50 could force a gamma-flip squeeze (bid-selling may be buy-write, not pure distribution).
- levels: support $5.00 · resistance $5.50 · invalidation net premium flips positive with ask-side near-dated buying above $5.

### earnings-scout — SELL VOL / NEUTRAL (3)
- top_signal: **no earnings until 8/10** (no near catalyst) + **VRP +0.28 PREMIUM_SELLING** (IV 102.7% vs realized 74.6%), IV 79th pctile, complacent skew, $5 gamma pin [phase-5/4/6].
- trade: **short ~30-DTE iron condor / strangle centered $5** (short $4.5P/$6C, wings $4/$6.5) into 6/18; small.
- top_risk: gap above $5.5/$6 wall outruns the pin — wings are load-bearing, not decoration.
- levels: support $5.00 · resistance $5.50–$6.00 · invalidation realized vol → implied on a fresh catalyst.

### risk-monitor — NEUTRAL / watch-only (2)
- top_signal: **regime TRANSITIONAL — "reduce position size," breadth 36.3%** [phase-6]; signal-backtest 50% n≈8 (no edge); conviction-matrix MIXED 5%; quality caps long (P/S 18.95, −226.7% margin) [phase-5/7/7b].
- trade: defined-risk premium-sell pinned to $5 at **≤½ unit**, or watch-only into 6/18 OPEX + June FOMC/CPI.
- top_risk: **6/18 monthly OPEX is the un-pin event** — the +$82M $5 gamma rolls off as max-pain sits at $4 and 26% SI can ignite.
- levels: support $5.00 · resistance $5.50 · invalidation close >$5.50 + rising borrow fee.

## Disagreements

- The lone directional dissent is **contrarian-scanner (SHORT)** — but it expresses the
  short as a *defined-risk credit spread*, not a naked short, so it is operationally
  consistent with the four NEUTRAL/sell-vol agents (all want a defined-risk,
  premium-selling, $5-pinned structure). **There is no genuine bull dissent** — a
  notable absence the phase-8b debate must stress-test (is the desk too one-sided
  given 26% SI + live catalysts?).

## Tool errors

- None blocking. All five `subagent_type`s were available (no `MISSING:` lines).
  Agents noted the prompt's illustrative filenames mapped to the actual on-disk
  artifacts (phase-2/3/4/5/6/7/7b/7c); they used the real files.

## Verdict for downstream

- **Plurality bias:** NEUTRAL / range / sell-vol (**4 of 5**; 1 defined-risk short; **0 long**).
- **Average conviction:** **2.4 / 5** (low).
- **Three highest-quality signals across agents:**
  1. Price-vs-flow **DIVERGENCE**: +30.9% price vs net_call_premium −$999,867 [phase-7/1].
  2. **Long-gamma $5 pin** (+$82.0M GEX, ZGL $2.64) + **COMPLACENT skew 0.815** + max-pain $4 → upside capped, mean-reversion to $5 [phase-4].
  3. **VRP +0.28 PREMIUM_SELLING** + **no catalyst until 8/10** + **TRANSITIONAL "reduce size" regime** → sell premium, small [phase-5/6].
- **Convergent expression:** defined-risk, premium-selling, $5-pinned (iron condor or
  call-credit spread into 6/18), **half-size**; no naked short, no directional long.
- **Open questions (for phase-8b):** Is the desk too uniformly bearish/fade given
  **26.37% short float + ~3 DTC + live defense catalysts** (squeeze tail)? Is the
  bid-side call selling **distribution** or **buy-write on top of dark-pool
  accumulation** (sweep-tracker's caveat)? What happens at the **6/18 OPEX un-pin**?
