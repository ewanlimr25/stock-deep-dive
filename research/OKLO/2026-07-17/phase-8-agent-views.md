# Phase 8 — Multi-Agent Analyst Desk (parallel)

**Ticker:** OKLO
**As-of date:** 2026-07-17
**Generated:** 2026-07-18T00:00:00Z
**Upstream phases cited:** phase-1 through phase-7c (all packed to each agent)

## Summary

**Unanimous 5-of-5 SHORT** — but a *low-conviction, defined-risk* short. Average conviction
**2.2 / 5**; horizons cluster **1-4 weeks**. Notably even the **contrarian-scanner returned
SHORT** (conviction 3, its highest of the desk): it found the only genuinely crowded trade is
the short *itself*, and the trend + fundamentals are the right side, so the fade is not to buy
OKLO but to respect that size must be capped. **Every one of the five agents named the same
top risk** — the crowded short (19.3% float) into a cash-rich balance sheet at the 52-week
low, still-bullish analysts ($55 PT), positive vanna, and the 08-10 earnings binary — a
squeeze toward the $47–50 max-pain zone. The desk consensus: **short, half-size, spreads only,
exit/hedge before 08-10 earnings.**

## Agent verdicts table

| Agent | bias | conviction | horizon | one_line_take |
|---|---|---|---|---|
| accumulation-hunter | SHORT | 2 | 1-4w | No mega prints, block tier sold, outside DP top-30 — overhead supply & dip-buy noise, not a floor. |
| contrarian-scanner | SHORT | 3 | 1-4w | Not a fade — the crowd (bearish sweeps, put-building, neg GEX) is aligned with a real de-rating; the only crowded trade is the short, which caps size not direction. |
| sweep-tracker | SHORT | 2 | 1-5d | Five straight sessions of bearish sweep persistence + put-rolling say fade rips toward $45-46; short-gamma cuts both ways — size small. |
| earnings-scout | SHORT | 2 | 1-4w | Sell vol via defined-risk put spread; rich IV vs a real downtrend, but 19%-float short into binary earnings is squeeze-primed. |
| risk-monitor | SHORT | 2 | 1-4w | Bearish five phases deep, but a lonely crowded gamma-amplified trade in a half-size regime — spreads only, exit before 08-10. |

**Tally:** SHORT 5 / LONG 0 / NEUTRAL 0 / RANGE 0. Conviction: one 3, four 2s → avg **2.2**.

## Per-agent details

### accumulation-hunter — SHORT, conv 2, 1-4w
- support $39.53–$40.00 (52w low / block-print floor); resistance $45.50–$46.20 (DP shelf);
  invalidation: daily close above $46.20 (shelf reclaimed) or a vanna-IV-crush break of $47–50.
- top_signal: "No genuine accumulation fingerprint — large-tier DP buy_ratio only 0.611
  (suggestive band), the sole block-tier print was a *sell*, OKLO outside DP ticker-summary
  top-30, and the heaviest 5-day prints ($46.24=$17.2M, $45.81=$11.4M) are overhead supply,
  not a defended floor [phase-2]."
- top_risk: crowded short into cash-rich 52w-low + 08-10 binary + primed vanna-squeeze; a
  stop-run through $46 is a real tail.

### contrarian-scanner — SHORT, conv 3, 1-4w
- support $39.8–$40.0; resistance $45.5–$46.2 (max-pain $47–50 above); invalidation: close
  above $46.2 or a post-OPEX IV crush firing the vanna squeeze toward $47–50.
- top_signal: "5-day bearish sweep-persistence ($41.0M, consistency 1) corroborated by the
  confirmed put roll (near −5,421 → far +4,430) and FULLY_NEGATIVE GEX on the $35/$33 walls —
  three independent lanes agree the put-buying is reinforced, not unwound [phase-1/3/4]."
- top_risk: cash-rich (current ratio 59.9), analysts 20-buy/1-sell $55 PT, COMPLACENT skew +
  positive vanna → post-OPEX IV crush or 08-10 earnings could squeeze toward $47–50.

### sweep-tracker — SHORT, conv 2, 1-5d
- support $40 → $35 (heaviest put wall + most-negative GEX, dealer-amplified break);
  resistance $45.5–$46.2; invalidation: daily close above $42.20 with sweep-persistence
  flipping bullish / consistency dropping.
- top_signal: "sweep-persistence bearish-dominant all 5/5 sessions (consistency 1, $41.0M),
  corroborated by the put roll and negative DEX −167M (dealers sell to hedge) [phase-1/3/4]."
- top_risk: today's tape genuinely mixed (net +$398K, BUSY_NAME_NORMAL_DAY) + COMPLACENT skew
  + FULLY_NEGATIVE GEX → live squeeze to $47–50 if IV crushes post-OPEX (vanna +1,942).

### earnings-scout — SHORT, conv 2, 1-4w (SELL VOL / defined-risk)
- support $35 (put wall + most-neg GEX); resistance $47–50 (max-pain + $50 call wall);
  invalidation: close above $47 max-pain magnet, or an SI print showing further build.
- top_signal: "fresh $33p +6,518 OI + confirmed put roll atop 5-day bearish sweeps ($41.0M)
  and −37% trend with bearish_flow backtest 100% (n=10, avg −5.22%) [phase-1/3/5]."
- top_risk: crowded short (19.29%, DTC 2.6) vs net-bullish analysts ($55 PT) into 08-10;
  cash-rich removes the floor-to-zero; positive vanna + max-pain $47–50 is a live squeeze.
- **Structure guidance:** put debit spread (e.g. ~$35/$28) expiring shortly after 08-10;
  avoid naked short/long-put (VRP +0.28 overpays) and avoid short strangles/condors (real
  ±25% IV move + FULLY_NEGATIVE GEX = amplification, not mean-reversion). Half size.

### risk-monitor — SHORT, conv 2, 1-4w (spreads only, exit before 08-10)
- support $35 (dealer-amplified); resistance $47–50 (squeeze ceiling); invalidation: daily
  close above $46 (reclaims 07-16 gap) OR IV30d crushing below ~75% (fires vanna buy-back).
- top_signal: "FULLY_NEGATIVE GEX (−8.99M, no ZGL) stacked on $35/$33 walls — short-gamma,
  mechanically amplifies any break lower, held every session through the −37% downtrend
  [phase-4/5]."
- top_risk: crowded 19.3%-float short, cash-rich no-solvency, 52w low, 08-10 binary, bullish
  analysts — defined-risk works, a naked short is a squeeze waiting to happen.
- **Correlation note:** no concurrent blueprints for 2026-07-17 → correlation gate genuinely
  empty; but beta 1.22 + FULLY_NEGATIVE gamma mean OKLO will co-move hard with any high-beta /
  risk-off name added to the book same-day — re-check correlation when positions are added.

## Disagreements

**None on direction** — 5-of-5 SHORT. The only spread is conviction (contrarian 3 vs four 2s)
and horizon (sweep-tracker 1-5d vs the rest 1-4w). The contrarian's *higher* conviction is
itself notable: the agent whose job is to fade the consensus concluded the consensus is right
and the crowd is only crowded on the short side.

## Tool errors

None. All five agent types available and returned. No `MISSING:` lines.

## Verdict for downstream

- **Plurality bias:** **SHORT, 5 of 5** (unanimous).
- **Average conviction:** **2.2 / 5** across all five non-MISSING agents (one 3, four 2s) —
  unanimous but deliberately restrained.
- **Three highest-quality signals across the desk:**
  1. 5-day bearish sweep-persistence, $41.0M, consistency 1, 5/5 sessions [phase-1
     sweep_persistence] — cited by 3 of 5 as the durable anchor.
  2. FULLY_NEGATIVE GEX stacked on the $35/$33 put walls + negative DEX −167M (dealers sell to
     hedge) [phase-4] — the mechanical amplification of any break lower.
  3. Confirmed put roll (near −5,421 → far +4,430) + fresh $33p +6,518 OI [phase-3] — downside
     structure maintained, not unwound, corroborating the −37% trend and de-rating.
- **Open questions surfaced by agents:** (1) does a post-OPEX IV crush fire the vanna squeeze
  up before the trend resumes down? (2) how to be short the downtrend while capped against the
  19%-float squeeze and the 08-10 earnings gap — every agent converges on **defined-risk put
  spread, half-size, exit/hedge before earnings**. This is the exact tension the phase-8b
  debate must resolve.
