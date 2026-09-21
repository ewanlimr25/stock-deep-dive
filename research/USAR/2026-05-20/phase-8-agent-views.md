# Phase 8 — Multi-Agent Analyst Desk

**Ticker:** USAR (USA Rare Earth, Inc.)
**As-of date:** 2026-05-20 (effective UW data date: 2026-05-19)
**Generated:** 2026-05-20T11:30:00-04:00
**Upstream phases cited:** phase-1 through phase-7

## Summary

Four specialist sub-agents ran in parallel on the packed phases 1–7
brief. The fifth — **earnings-scout — was SKIPPED** because USAR's
next earnings (2026-08-10, per phase 7 deep_dive) is 81 days away,
outside the 30-day window the phase spec calls out. Net verdict:

- **Plurality: split 2 LONG / 2 NEUTRAL / 0 SHORT**.
- **Average conviction: 2.25 / 5** (low).
- **All four agents converge** on three numbers: support $19.46,
  near-term resistance $21, medium resistance $25 (or $25.42).
  Invalidation = **close below $19.46** (every agent's primary line).
- The dissent is not directional but **structural** — sweep-tracker
  reads the headline 6/18 $18P sweep as a structured put spread
  (neutralizing its bearish signal), while accumulation-hunter and
  contrarian-scanner read the DP buying as a real bid that wins.
- **risk-monitor mandates 25–33% of normal sleeve, defined-risk only**
  — anchored to the negative-gamma + FOMC-OPEX collision risk in mid-
  June. This sizing guidance is the most important single take from
  the parallel run, given the phase-6 TRANSITIONAL regime.

## Agent verdicts table

| Agent | Bias | Conviction | Horizon | One-line take |
|-------|------|-----------|---------|---------------|
| accumulation-hunter | LONG | 2 | 1-4w | Footprint is accumulation-shaped but stacked under a $25 supply shelf — somebody's building a position, but they're buying from a bigger seller. |
| contrarian-scanner | LONG | 3 | 1-5d | Retail is panic-buying $17.50 puts after a 29% bleed while institutions quietly accumulate at NBBO ask and sell 2028 $40 puts — fade the panic, not the trend. |
| sweep-tracker | NEUTRAL | 2 | 1-5d | Tape is loud but structured — 5/5 sessions of sweeps net to spread complexes, not a momentum push; fade the headline, trade the $19-$21 range until a leg breaks. |
| risk-monitor | NEUTRAL | 2 | 1-5d | Trade is UNFIT at normal size; cap at 25-33% sleeve, defined-risk only, no naked premium short into negative-gamma FOMC-OPEX collision. |
| earnings-scout | SKIPPED | — | — | Next earnings 2026-08-10 (81 days) — out of 30-day window per phase spec. |

## Per-agent details

### accumulation-hunter

```
VERDICT
- bias: LONG
- conviction: 2
- horizon: 1-4w
- key_levels:
    support: 19.46
    resistance: 25.42
    invalidation: Daily close below $19.00 with DP buy_ratio flipping
                  <0.45 and no new sub-$19.46 large-tier accumulation print
- top_signal: Phase 2 large-tier dark-pool buy_ratio 0.623 with a
              $505,960 print @ $19.46 at NBBO ask, reinforced by Phase 7
              institutional_accumulation B/S 1.65 at VWAP $20.07 — a real
              bid is being worked, not unwound.
- top_risk:   The $24.18-$25.95 5-day DP cluster ($10.1M concentrated at
              $25.42) looks more like distribution overhead than
              accumulation, meaning today's lower-band buying may simply
              be late longs absorbing earlier institutional supply
              rather than fresh smart-money entry.
- one_line_take: Footprint is accumulation-shaped but stacked under a
              $25 supply shelf — somebody's building a position, but
              they're buying from a bigger seller.
```

### contrarian-scanner

```
VERDICT
- bias: LONG
- conviction: 3
- horizon: 1-5d
- key_levels:
    support: 19.46
    resistance: 25.00
    invalidation: close below 19.46 with DP buy_ratio flipping <0.50
- top_signal: Phase 7 price-vs-flow divergence (price +31.5% / flow
              -$814k) combined with Phase 2 DP buy_ratio 0.623 and Phase
              1 2028 $40P sold all-bid $682k = retail puts crowded short
              into institutional accumulation.
- top_risk:   Phase 6 China export-ban suspension is a real fundamental
              headwind that can override positioning; if $19.46 DP floor
              breaks, the absence of dark pool support below opens a
              vacuum to $17.50 (the strike crowded put-buyers just
              opened +1,253 OI on).
- one_line_take: Retail is panic-buying $17.50 puts after a 29% bleed
              while institutions quietly accumulate at NBBO ask and sell
              2028 $40 puts — fade the panic, not the trend.
```

### sweep-tracker

```
VERDICT
- bias: NEUTRAL
- conviction: 2
- horizon: 1-5d
- key_levels:
    support: 19.00
    resistance: 21.00
    invalidation: sustained break <18.50 on expanding volume OR reclaim
                  >21.50 with call sweeps flipping ask-side
- top_signal: Phase 1's headline 6/18 $18P ask sweep ($349,878) is
              paired 17:35:34Z with the 9/18 $14P mid print at identical
              2,108 size — a diagonal put spread, not a clean directional
              short.
- top_risk:   If the $14P leg is the short and $18P is the long, this is
              actually a bearish debit diagonal targeting a slide into
              June OPEX, and dealer negative GEX below $20 would
              accelerate it.
- one_line_take: Tape is loud but structured — 5/5 sessions of sweeps
              net to spread complexes, not a momentum push; fade the
              headline, trade the $19-$21 range until a leg breaks.
```

### risk-monitor

```
VERDICT
- bias: NEUTRAL
- conviction: 2
- horizon: 1-5d
- key_levels:
    support: 19.46
    resistance: 21.00
    invalidation: close below 19.46 on volume OR breach of 18.00 intraday
- top_signal: Phase 4 negative GEX regime with spot $20.02 vs ZGL $24.98
              (-19.8%) inside $14-$21 amplification corridor confirms
              moves get magnified, not dampened.
- top_risk:   Phase 2 shows zero dark-pool support below $19.46 while
              Phase 5 -29%/11-session drawdown plus 5/22 IV 145% on
              3DTE sets up gap-down cascade into 16,949 OI $21P pin
              during FOMC week.
- one_line_take: Trade is UNFIT at normal size; cap at 25-33% sleeve,
              defined-risk only, no naked premium short into negative-
              gamma FOMC-OPEX collision.
```

### earnings-scout (skipped)

`MISSING: earnings-scout` — per phase 7 `insights_deep_dive`, USAR's
next earnings is **2026-08-10**, 81 days from today. The phase spec
says "skip if earnings > 30d out". No verdict produced; sizing impact
neutral.

## Disagreements

There is **no opposite-direction dissent** — no agent went SHORT. The
disagreement is **LONG vs NEUTRAL**, structured as:

- LONG side (accumulation-hunter + contrarian-scanner): the DP and OI
  footprint represent a real institutional bid that should be faded-
  against (i.e., bought into).
- NEUTRAL side (sweep-tracker + risk-monitor): the same footprint is
  ambiguous — sweep-tracker says the headline sweep is a spread (not
  outright); risk-monitor says the regime doesn't allow conviction
  sizing even if directionally right.

**Critical disagreement on the paired $18P/$14P trade**: sweep-tracker
explicitly identifies this as a *diagonal put spread* and notes:

> "If the $14P leg is the short and $18P is the long, this is actually
> a **bearish debit diagonal** targeting a slide into June OPEX."

That contradicts the phase-1 reading where the more natural "long $18P
ask / short $14P mid" was assumed (which would be bullish if exited
quickly, OR a hedged-long sleeve). The $14P is at the mid (could be
either side) so neither phase 1 nor sweep-tracker can definitively
resolve it.

**Reconciliation for phase 9:** since we can't tell which leg is short
and the spread itself is delta-negative either way (both legs are puts
with negative deltas), treat the entire paired trade as a **bearish
overlay** for sizing purposes but **not** as a fresh outright bear bet.
This is consistent with the "hedged-long" interpretation across phases
2-7.

## Tool errors

- `MISSING: earnings-scout` — intentional skip per phase spec (earnings
  > 30d). No subagent invoked.
- No other agent errors. All four returned structured verdicts within
  expected schema.

## Verdict for downstream phases

- **Plurality bias:** **LONG (2) vs NEUTRAL (2) vs SHORT (0)** —
  effective tilt is **LONG-LEANING with strong neutrality**.
- **Average conviction:** **2.25 / 5** across four non-MISSING agents.
- **Three highest-quality signals across all agents (with tag):**
  1. **[ACC-HUNTER + INSIGHT]** Large-tier DP buy_ratio 0.623 + B/S
     1.65 with the $505,960 print @ $19.46 at NBBO ask "a real bid is
     being worked, not unwound."
  2. **[CONTRARIAN + FLOW]** Price-vs-flow divergence (+31.5% / flow
     -$814k) + 2028 $40P sold all-bid $682k = retail crowded short
     into institutional accumulation = textbook **bottom-divergence
     setup**.
  3. **[SWEEP + STRUCT]** The 17:35:34Z paired prints (size 2,108
     identical) are ONE structured trade, not two — reduces standalone
     bearish weight of the $349k ask sweep and tilts the spread-net
     toward "hedged" rather than "outright bear".
- **Open questions:**
  - Is the 17:35:34Z diagonal long-$18P/short-$14P or short-$18P/long-
    $14P? Determining this would resolve whether the institutional
    side is **hedged long** (PM hedging existing stock) vs **structured
    bear** (PM expressing a directional view via diagonal).
  - Will dealers defend $19 (the negative-gamma accelerator edge) or
    let the move cascade to $17.50 (the put-wall floor)? Risk-monitor
    flags this; phase 9 sizing should presume "defend $19" as base case
    but plan for "lose $19" tail scenario.
  - Is risk-monitor's "25-33% normal sleeve" the right size or is even
    that too generous given the FOMC-OPEX collision in 4 weeks? Phase
    9 sizing rubric will resolve.
