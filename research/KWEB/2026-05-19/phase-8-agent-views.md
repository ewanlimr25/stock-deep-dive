# Phase 8 — Multi-Agent Analyst Desk

**Ticker:** KWEB
**As-of date:** 2026-05-19
**Generated:** 2026-05-20T00:00:00Z
**Upstream phases cited:** all of phases 1–7

## Summary

Four sub-agents returned (earnings-scout intentionally skipped — KWEB
is an ETF without scheduled earnings). The bench splits **2 LONG / 2
RANGE / 0 SHORT / 0 NEUTRAL** with **average conviction 2.75 / 5**.
The two longs (sweep-tracker conv 4, contrarian-scanner conv 3)
emphasize *the tariff truce headline lighting a fuse on
already-bullish-unwound positioning*. The two range votes
(accumulation-hunter conv 2, risk-monitor conv 2) emphasize
*managed-range institutional behaviour + sector outflows preventing
breakout*. There is **no SHORT vote** anywhere on the desk — the
bearish 5-day sweep persistence is not endorsed as a directional
short by any of the four agents on a forward-looking basis.

## Agent verdicts table

| Agent | bias | conviction | horizon | one_line_take |
|-------|------|-----------|---------|---------------|
| accumulation-hunter | **RANGE** | 2 | 1-4w | "Two institutions disagree at $28 — one underwriting the floor via puts, another distributing size into the close; net read is a managed range, not stealth accumulation." |
| contrarian-scanner | **LONG** | 3 | 1-5d | "Fade the panic-sellers, not the dreamers — 28P sold-to-open + tariff truce + IV at 0th percentile = crowd just dumped calls at the bottom of a positive-gamma envelope." |
| sweep-tracker | **LONG** | 4 | 1-5d | "Tape rotated from chronic bearish to bullish-unwind into the close; tariff headline lights the fuse — expect a Monday gap pinned to the $29 dealer magnet, with $30 as the stretch target." |
| risk-monitor | **RANGE** | 2 | 1-4w | "Five conflicting signals plus correlated sector outflows means this is a defined-risk, half-size premium play — not a directional bet; size 0.5R max, prefer May 22 IV-rich credit structure over debit chase." |
| earnings-scout | MISSING (skipped — ETF, no scheduled earnings) | — | — | — |

## Per-agent details

### accumulation-hunter [AGENT:accumulation-hunter]

```
VERDICT
- bias: RANGE
- conviction: 2
- horizon: 1-4w
- key_levels:
    support: 28.00
    resistance: 30.46
    invalidation: close below 27.85 on >1.5x ADV, OR mega-tier DP prints flip to buy-side above $30.46
- top_signal: Phase 3 KWEB 260529 28P +11,461 OI sold-to-open ($665K premium, prev bid_vol 6,300 vs ask 621) is a textbook institutional floor underwrite at $28, while Phase 2 mega-tier DP prints ($25.87M, 0.000 buy_ratio, both inside last 6 hours and one at 19:56:41Z = closing-print distribution) cap the upside — these are not the same actor and the tape is being warehoused, not accumulated.
- top_risk: The 28P put-write is a synthetic long that becomes real accumulation if the May 20 tariff-truce headline triggers a gap-up through $30.46, forcing the mega-tier sellers to cover and converting the range into a breakout.
```

### contrarian-scanner [AGENT:contrarian-scanner]

```
VERDICT
- bias: LONG
- conviction: 3
- horizon: 1-5d
- key_levels:
    support: 28.06
    resistance: 30.00
    invalidation: close below 27.00 (short-gamma cliff -$7.10B activates downside cascade)
- top_signal: Phase 1 call ask/bid 24,148/77,729 (ratio 0.31) plus 33C Jun OI -35,485 = mass call overwriting/liquidation INTO a US-China tariff truce extension catalyst (phase 6) — bears positioned for downside the news just removed.
- top_risk: COMPLACENT reverse skew (calls 33.74% IV vs puts 30.71%) means downside is genuinely under-priced; if 28.06 DP support cracks, dealer long-stock hedge unwinds violently toward 27 short-gamma cliff.
```

### sweep-tracker [AGENT:sweep-tracker]

```
VERDICT
- bias: LONG
- conviction: 4
- horizon: 1-5d
- key_levels:
    support: 28.00 (intraday hold) / 27.00 (short-gamma cliff, invalidation level)
    resistance: 29.00 (massive +$17.79B GEX magnet) then 30.00 (+$10.75B)
    invalidation: sustained close below $27.00 — breaks into negative GEX cliff and flips dealer flow to accelerant
- top_signal: Phase 1 tape shows ask-side deep-ITM 0.95-delta synthetic long ($631.5K Jun 20C) plus bid-side 2027 27P liquidation ($330K) — that is bullish unwind footwork landing the session before the tariff-truce headline hit the wire.
- top_risk: The 5-day persistence read is BEARISH with $94.9M cumulative premium and today's bid-side overwriting of Jul 30C / Aug-Sep 35C suggests funds are capping upside above $30, so a gap-up could stall fast at the $29 GEX wall.
```

### risk-monitor [AGENT:risk-monitor]

```
VERDICT
- bias: RANGE
- conviction: 2
- horizon: 1-4w
- key_levels:
    support: 27.00
    resistance: 30.00
    invalidation: close below 27.00 (short-gamma cliff confirms breakdown) OR close above 30.50 on expanding call premium
- top_signal: Phase 4 dealer regime is POSITIVE GEX with $29 magnet at +$17.79B and ZGL $23.81 — range-suppression dominates absent a catalyst that breaks the +$10.75B $30 wall.
- top_risk: KWEB's two parent buckets (Comm Services -$84M, Consumer Cyclical -$27M per Phase 6) are both bleeding institutional capital while regime is TRANSITIONAL — even a bullish tariff truce headline may fail to ignite a breakout because the sector flow tailwind isn't there to absorb dealer-suppression.
```

### earnings-scout [AGENT:earnings-scout] — MISSING

Skipped intentionally: KWEB is an ETF with no scheduled earnings event.
Phase 6's catalyst calendar already covers the near-term binaries
(May 22 expiry / tariff truce confirmation, June FOMC, June 18 OPEX).

## Disagreements

- **Sweep-tracker (LONG conv 4) vs risk-monitor (RANGE conv 2)** —
  largest gap. Sweep-tracker reads today's tape rotation (deep-ITM 20C
  ask buy + Jan'27 27P bid close) as bullish footwork landing the
  session before the truce headline, projecting a Monday $29 magnet
  pin. Risk-monitor counters that **sector outflows from Comm Services
  and Consumer Cyclical (KWEB's parent buckets) will starve any
  breakout of fuel even with the truce news**. Both can be right at
  different horizons: sweep-tracker's 1-5d window may print the gap;
  risk-monitor's 1-4w window may see it fade.
- **Accumulation-hunter "managed range, not stealth accumulation"** is
  the most surgical observation in the set — explicitly says the
  28-floor underwriter and the mega-tier seller are NOT the same
  actor; the tape is being *warehoused* between two desks. This is
  the cleanest framing of the range thesis.

## Tool errors

`MISSING: earnings-scout` — skipped (KWEB is an ETF, no earnings).
Not a failure.

## Verdict for downstream phases

- **Plurality bias:** **2 LONG / 2 RANGE / 0 SHORT / 0 NEUTRAL** — no
  bearish directional vote, but split between mildly-bullish and
  managed-range readings.
- **Average conviction across 4 non-MISSING agents:** **2.75 / 5**.
- **Consensus invalidation:** **close below $27.00** (3 of 4 explicit;
  4th cites $27.85). The negative-GEX cliff at $27 [STRUCT:gex] is the
  hard line for ALL constructive scenarios.
- **Consensus support / resistance band:** support **$27.00-$28.00**;
  resistance **$29.00 → $30.00 → $30.46**.
- **Three highest-quality signals across all agents:**
  1. **Phase 3 28P sold-to-open** (cited by 2 of 4 — accumulation-hunter, contrarian-scanner): floor defense at $28.
  2. **Phase 7 conviction matrix call ask/bid 0.31 + Phase 3 33C OI −35,485** (cited by contrarian-scanner): mass call overwriting *just before* the bullish truce news.
  3. **Phase 4 $29 GEX wall +$17.79B + ZGL $23.81** (cited by sweep-tracker and risk-monitor): positive-gamma magnet to $29 within a 16% suppression envelope.
- **Open questions surfaced by agents:**
  - **Will sector flow (Comm Services / Consumer Cyclical) reverse to
    confirm a tariff-driven KWEB breakout?** Risk-monitor flags this
    as the structural drag that could neutralize a positive headline.
    Phase 9 should set a *sector-flow* trigger condition as part of
    the trade plan (e.g., scale up only if Comm Services flow flips
    positive within 2 sessions).
  - **Is the 28-floor underwriter and the mega-tier 19:56Z seller the
    same actor (delta-neutralizing a short stock with a sold put) or
    two distinct actors (one accumulating, one distributing)?**
    Accumulation-hunter argues two distinct desks. Phase 9 sizing
    should not assume the same balance-sheet logic for both flows.
  - **If May 22 expiry IV settles back to ~33% on confirmed truce,
    does the put-write structure (sold 28P) start paying-down
    immediately, or is the gamma exposure too thin to capture?**
    Phase 9 should consider whether a *short May 22 vol* trade can
    co-exist with the put-write or whether it doubles short-gamma
    exposure.
