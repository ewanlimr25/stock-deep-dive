# Phase 7 — Composite Insights

## Summary

The composite engine reads FSLY as **MIXED/NEUTRAL — not a high-confluence name** —
with one flag worth parsing carefully:

- **`conviction-matrix`: scenario MIXED, confidence 4.7%** (near-zero, dead-center) —
  *"Balanced dark pool activity — no clear bias."* Dark-pool buy ratio 0.547 (mild),
  and the options *volume* view is balanced: call-ask 6,264 vs call-bid 5,909 (51%
  ask), put-ask 1,389 vs put-bid 1,900. **No directional conviction at the composite
  level.**
- **`institutional-accumulation`: NEUTRAL**, buy/sell ratio **1.21** — *mildly*
  positive (matches phase-2's small large-tier accumulation), but the engine calls it
  balanced, not accumulation.
- **`price-vs-flow`: DIVERGENCE = true** — but read it carefully: *"Price is down
  27.7% but options flow is bullish (net flow +$153,723)."* The engine is comparing
  **bullish current flow against the longer-window price drawdown** — i.e. a
  potential **reversal/bottoming** signal (smart-money call flow into a beaten-down
  name), *not* a fade-the-rally signal. For a +74.5% YTD name this "−27.7%" is a
  pullback-from-highs window, and bullish flow into it is the constructive reading.
- **CRM is `signal-confluence` outside top-100** → FSLY is **not** a multi-factor-
  aligned name; its signals are mild and mixed (quiet flow, bullish OI, neutral DP).

**Composite read: MIXED/NEUTRAL, faint-constructive.** The engine sees no strong bias
either way — balanced DP, balanced option volume, but a *bullish-flow-into-a-pullback*
divergence that leans mildly constructive. This is consistent with the dive so far:
**armed squeeze structure (phase-3) + cheap vol (phase-5), but no flow ignition
(phase-1) and dampening gamma (phase-4)** → the synthesis is "potential, not yet
kinetic." No phase contradicts a *small* long; nothing supports a *large* one.

## Conviction matrix (`uw insights conviction-matrix`) `[INSIGHT:conviction-matrix]`

| Field | Value |
|-------|-------|
| **Scenario** | **MIXED** |
| Confidence | **4.7%** (dead-center; bear<40 / bull>60) |
| Explanation | "Balanced dark pool activity — no clear bias" |
| DP buy ratio | 0.547 (mild) |
| Call ask / bid vol | 6,264 / 5,909 (ask share 0.51) |
| Put ask / bid vol | 1,389 / 1,900 (put selling) |

- The options *volume* view is balanced (51% call-ask) — echoing phase-1's "call-tilt
  but low aggression." Puts traded more on the bid (sold) — mildly constructive at
  the margin.

## Institutional accumulation (`uw insights institutional-accumulation`) `[INSIGHT:institutional-accumulation]`

| Field | Value |
|-------|-------|
| **Signal** | **NEUTRAL** ("balanced dark pool activity") |
| Buy/sell ratio | **1.21** (mildly positive) |

- Matches phase-2: small, mildly-accumulative DP. Not distribution (contrast CRM),
  not strong accumulation either.

## Price-vs-flow (`uw insights price-vs-flow`) `[INSIGHT:price-vs-flow]`

| Field | Value |
|-------|-------|
| Divergence | **true** |
| Signal | "Price down 27.7% but options flow bullish (net +$153,723)" |
| Flow direction | bullish |

- **Interpretation:** bullish flow against a multi-week pullback = a **potential
  reversal/bottoming** lean (constructive), not a fade. Modest net flow ($154k) keeps
  it a faint signal. The "−27.7%" is a pullback-from-highs window on a +74.5%-YTD name.

## Signal confluence (`uw insights signal-confluence`) `[INSIGHT:signal-confluence]`

- **FSLY outside top-100** — not a high-confluence name; signals are mild and mixed.

## Tool calls

```bash
uw insights conviction-matrix          --symbol FSLY --date 2026-05-29 --json
uw insights institutional-accumulation --symbol FSLY --date 2026-05-29 --json
uw insights price-vs-flow              --symbol FSLY --date 2026-05-29 --json
uw insights signal-confluence          --top-n 100 --date 2026-05-29 --json   # FSLY outside top-100
```

## Tool errors

none

## Read-through

- The engine **confirms the dive's "armed but not triggered" read** at the synthesis
  level: MIXED scenario (4.7%), neutral accumulation (1.21), balanced option volume —
  no conviction signal. The one lean is the **price-vs-flow reversal divergence**
  (bullish flow into a pullback), which is mildly constructive for a squeeze-name long.
- **What this means for sizing:** the composite gives **no permission to upsize.** It
  neither vetoes a small long (no distribution, no bearish bias) nor supports a
  conviction one (MIXED, outside confluence top-100). It hands phase-8/8b a clean
  question: **is the cheap-vol + bullish-OI-ladder + 14.6%-short structure worth a
  small optionality bet, or is the quiet/mixed flow a reason to wait?**
- **Net through phase-7:** bull case = squeeze-laddered OI (phase-3) + cheap-vs-
  realized vol + 4-day OI build (phase-5) + low-beta idiosyncrasy (phase-6) + mild DP
  accumulation (phase-2). Caution case = quiet/thin flow, no sweeps (phase-1),
  dampening positive gamma (phase-4), choppy 4/4 price action (phase-5), MIXED
  composite (phase-7). **Small, defined-risk, optionality-style long — or wait for
  volume.** Both gates (7b/7c) next.

## Citations

- `[INSIGHT:conviction-matrix]` scenario MIXED, confidence 4.7%, balanced DP (0.547), call-ask vol 0.51 — `uw insights conviction-matrix`
- `[INSIGHT:institutional-accumulation]` NEUTRAL, buy/sell 1.21 (mildly positive) — `uw insights institutional-accumulation`
- `[INSIGHT:price-vs-flow]` divergence true — bullish flow into a −27.7% pullback (reversal lean) — `uw insights price-vs-flow`
- `[INSIGHT:signal-confluence]` FSLY outside top-100 (mild/mixed signals) — `uw insights signal-confluence`

## Upstream references

- phase-2-dark-pool.md §Summary — "net neutral-to-mildly-accumulative"; phase-7's
  conviction-matrix (balanced, 0.547) and institutional-accumulation (NEUTRAL, 1.21)
  independently confirm the mild-positive-but-not-strong DP read.
- phase-4-structure.md §Summary — "bullish bias / neutral mechanics"; phase-7's MIXED
  composite mirrors it — the structure leans bullish but nothing has triggered.

## Next phase

- phase-7b-fundamentals.md (quality veto: is Fastly's fundamental picture sound enough
  to support a squeeze-optionality long, or does an unprofitable small-cap cut it?)
