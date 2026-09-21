# Phase 7 — Composite Insights

## Summary

The composite engine **independently reproduces the dive's central divergence — and
weights it toward caution.** Two synthesis tools land on **DISTRIBUTION**:

- **`conviction-matrix`: scenario DISTRIBUTION, confidence 32.9%** (below the 0.40
  bear threshold). Explanation: *"Dark pool selling with mixed options activity."*
  Note the options side is **"mixed," not bullish** by the matrix's lens: call-ask
  vol 104,899 vs call-bid 96,442 (only 52% ask) and put-ask 21,369 vs put-bid
  25,113 — i.e. once you net ask-vs-bid *volume* (not premium), the call buying is
  far less one-sided than phase-1's premium view suggested.
- **`institutional-accumulation`: signal DISTRIBUTION**, buy/sell ratio **0.21**
  (1.30M buy vs 6.32M sell shares), avg price $190.15, concentrated at the $191.10
  level — a verbatim restatement of phase-2.

Counterweighting them, `price-vs-flow` finds **no reversal divergence** ("price and
flow are aligned," both bullish; period +4.92%), and `analyst-vs-flow` shows flow
sentiment bullish. CRM is **outside the top-80 on `signal-confluence`** — i.e. it is
*not* a clean multi-factor-aligned name; the factors conflict, which is precisely why
it doesn't rank.

**Composite read: CONFLICTED, engine-tilted BEARISH/DISTRIBUTION.** The machine
synthesis says the dominant, highest-conviction tape (institutional dark-pool
selling) outweighs the call-premium flow — confidence 32.9% sits in the
bearish-of-neutral zone. This is the **strongest formal articulation yet** of why
this setup is "tactical long at best, not a conviction buy," and it sets up phases
7b/7c/8b to stress-test the long thesis hard.

## Conviction matrix (`uw insights conviction-matrix`) `[INSIGHT:conviction-matrix]`

| Field | Value |
|-------|-------|
| **Scenario** | **DISTRIBUTION** |
| Confidence | **32.9%** (bear<40 / bull>60) |
| Explanation | "Dark pool selling with mixed options activity" |
| Dark-pool buy ratio | 0.171 (1.30M buy / 6.32M sell) |
| Options: call ask / bid vol | 104,899 / 96,442 (ask share 0.52) |
| Options: put ask / bid vol | 21,369 / 25,113 |

- **Key nuance vs phase-1:** by *premium*, sweeps were 56% ask and 100% call (phase-1).
  By *total call volume* ask/bid, it's only 52% ask — so the aggressive-buy edge is
  real but thinner than the premium view implied. The matrix treats the options side
  as "mixed," letting the dark-pool selling dominate → DISTRIBUTION.

## Institutional accumulation (`uw insights institutional-accumulation`) `[INSIGHT:institutional-accumulation]`

| Field | Value |
|-------|-------|
| **Signal** | **DISTRIBUTION** ("sell volume significantly exceeds buy") |
| Buy/sell ratio | **0.21** |
| Buy / sell volume | 1.30M / 6.32M shares |
| Avg trade price | $190.15 |
| Top level | $191.10 ($908M, 4.75M sh) |

## Price-vs-flow (`uw insights price-vs-flow`) `[INSIGHT:price-vs-flow]`

| Field | Value |
|-------|-------|
| Divergence | **false** — "price and flow are aligned" |
| Flow direction | bullish |
| Period change | +4.92% (start $182.14 → end $191.10; hi $194.14 / lo $164.33) |

- No *reversal* signal: price rose with bullish flow. This is the one composite that
  supports continuation — it argues the call flow is *confirming* price, not fading it.

## Signal confluence / analyst-vs-flow `[INSIGHT:signal-confluence]`

- **CRM outside top-80 on `signal-confluence`** — the bullish/bearish factors do
  **not** align cleanly, so CRM is not a high-confluence name. (A conflicted setup,
  by construction, won't rank.)
- `analyst-vs-flow`: flow sentiment **bullish** (analyst recommendation block not
  populated for CRM here → analyst leg deferred to phase-7b/7c).

## Tool calls

```bash
uw insights conviction-matrix          --symbol CRM --date 2026-05-29 --json
uw insights institutional-accumulation --symbol CRM --date 2026-05-29 --json
uw insights price-vs-flow              --symbol CRM --date 2026-05-29 --json
uw insights analyst-vs-flow            --symbol CRM --date 2026-05-29 --json
uw insights signal-confluence          --top-n 80 --date 2026-05-29 --json   # CRM outside top-80
```

## Tool errors

- `analyst-vs-flow` returned only the flow block for CRM (no analyst recommendations
  populated) — analyst sentiment is picked up via `fz`/WebSearch in phase-7b/7c.
  Not blocking.

## Read-through

- **The composite engine is the tie-breaker's first vote, and it votes caution.**
  Two of five synthesis tools say **DISTRIBUTION** outright; the matrix confidence
  (32.9%) sits in bearish-of-neutral territory; and CRM **fails to make the
  signal-confluence board** because its factors genuinely conflict. The one bullish
  composite (`price-vs-flow`) only certifies that the call flow isn't *fading* price —
  not that it overrides the institutional selling.
- **What changed my weighting:** the matrix's *volume* view of options (52% call-ask,
  not the 56%/100% premium view) shows the aggressive-buying edge is **thinner than
  phase-1 alone implied.** A few large premium sweeps drove the bullish premium
  number; the broad call *volume* was closer to balanced. That makes the dark-pool
  distribution the higher-conviction tape, exactly as the engine concludes.
- **Net through phase-7:** bull case = real call flow + sector inflow + positive
  gamma + 60–73% historical follow-through (phases 1/4/5/6). Bear case =
  institutional distribution + thin near-support + conflicted confluence (phases
  2/3/7). The engine sides with the bear/caution read at the *synthesis* level while
  acknowledging near-term continuation is mechanically possible. **This frames the
  trade as a small, defined-risk, tactical-continuation long that must survive the
  7b/7c/8b downside gates — with a live "fade/avoid" alternative if those gates
  bite.**

## Citations

- `[INSIGHT:conviction-matrix]` scenario DISTRIBUTION, confidence 32.9%, "mixed options" (call-ask vol share 0.52) — `uw insights conviction-matrix`
- `[INSIGHT:institutional-accumulation]` DISTRIBUTION, buy/sell 0.21 (1.30M/6.32M sh) — `uw insights institutional-accumulation`
- `[INSIGHT:price-vs-flow]` divergence false, price & flow aligned bullish, +4.92% — `uw insights price-vs-flow`
- `[INSIGHT:signal-confluence]` CRM outside top-80 (factors conflict) — `uw insights signal-confluence`

## Upstream references

- phase-2-dark-pool.md §Summary — "mega-tier buy ratio 0.017, distribution";
  phase-7's conviction-matrix and institutional-accumulation both independently
  return DISTRIBUTION, confirming phase-2 is the engine's dominant signal.
- phase-1-flow.md §Sweeps — "56% ask, 100% call sweeps"; phase-7's volume view
  (52% call-ask) shows that edge is **thinner** than the premium view, downgrading
  the flow from "bullish" to "mixed" at the composite level.

## Next phase

- phase-7b-fundamentals.md (quality veto: is Salesforce's fundamental picture sound
  enough to support a catch-up long, or does it cut conviction further?)
