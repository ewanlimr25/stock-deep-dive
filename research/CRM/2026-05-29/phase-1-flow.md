# Phase 1 — Options Flow

## Summary

The options tape is **decisively call-dominant and directional-long**, confirming
the self-history extreme from phase-0.5. Sweeps are **100% calls (20 of 20
contracts, zero put sweeps)**, $26.3M total sweep premium, **56% on the ask**
($14.3M ask vs $11.1M bid). Call premium dominates **every** expiry — e.g. 7/17
$18.1M call vs $4.7M put; 6/18 $13.8M vs $3.0M; 6/5 $12.7M vs $2.0M. DTE is
**BALANCED** (weeklies 19% / monthlies 19% / LEAPs 5% / **0DTE 0%**) — this is
*term-structure* positioning across June→2027, **not** a 0DTE gamma scramble.

Two honest caveats keep this from being a clean "++": (1) a meaningful share of
the call sweeps printed on the **bid** ($11.1M, 44%) — consistent with some
profit-taking / call-writing into the +8.5% pop, not purely fresh aggressive
buying; (2) the largest *single* premium trade was a **230C Sep bid** ($0.65M) and
a **190P Sep** appears in the top bets — minor, but the book is not 100% one-way.

**Directional read: BULLISH, conviction MODERATE-HIGH.** The call dominance is
real, fresh (phase-0.5: net-call premium 100th self-pctile), and spread across the
curve. The ask/bid split (56/44) and IV-crush context (options got cheaper into the
move) temper it from a stampede to a strong-but-qualified long signal.

## Sweeps (`uw options-flow sweeps`) — ask=bullish / bid=bearish `[FLOW:sweeps]`

- **20 sweep contracts, 100% calls, 0 put sweeps.** Total sweep premium **$26.3M**.
- **Call ask $14.28M (12 contracts) vs call bid $11.10M (7) + mid $0.90M (1)** →
  ask share **0.56**.
- Largest sweeps:

| Strike | Type | Expiry | Side | Premium | Size | Avg px |
|--------|------|--------|------|---------|------|--------|
| 200 | call | 2026-06-18 | bid | $2.17M | 4,674 | 4.61 |
| 200 | call | 2026-07-17 | **ask** | $2.11M | 2,531 | 8.29 |
| 180 | call | 2026-07-17 | bid | $1.88M | 1,011 | 17.71 (ITM) |
| 185 | call | 2026-07-17 | bid | $1.70M | 1,260 | 14.35 (ITM) |
| 200 | call | 2026-06-18 | **ask** | $1.59M | 3,409 | 4.56 |
| 200 | call | 2026-07-17 | bid | $1.51M | 1,774 | 8.55 |
| 190 | call | 2026-06-05 | **ask** | $1.46M | 3,088 | 4.69 |
| 175 | call | 2027-01-15 | bid | $1.43M | 383 | 37.08 (deep ITM) |

- The **$200 strike (6/18 + 7/17)** is the clear magnet — that's **+4.7% above
  spot** ($191.10), a logical upside target for the position. Heavy ask-side buying
  of the 6/18 200C and 6/5 190C = fresh upside bets; the ITM 180/185/175C bids look
  like rolling/locking gains or covered structures.

## Top-premium single trades (`uw options-flow top-premium-trades`) `[FLOW:top-premium-trades]`

- 10 of the top 12 single bets are **calls**. Mix of ask (220C '27, 200C Aug, 175C
  Jun, 185C '27) and bid sides; two **190P Sep** prints ($0.38M each) are the only
  puts — modest downside hedging at-the-money.
- Notable: **220C Jan-2027 ask** (×2) and **200C Aug ask** — longer-dated upside
  conviction layered on top of the front-month flow.

## Expiry concentration (`uw options-flow expiry-heatmap`) `[FLOW:expiry-heatmap]`

| Expiry | Call prem | Put prem | Call/Put prem |
|--------|-----------|----------|---------------|
| 2026-07-17 | $18.12M | $4.70M | 3.85 |
| 2026-06-18 | $13.78M | $2.97M | 4.64 |
| 2026-06-05 | $12.70M | $2.03M | 6.27 |
| 2026-08-21 | $6.85M | $3.70M | 1.85 |
| 2027-01-15 | $8.30M | $2.00M | 4.15 |
| 2026-05-29 (0DTE) | $9.15M | $0.91M | 10.06 |

- **Call premium leads at every single expiry**; the front weeklies (6/5, 6/18) and
  the 7/17 monthly carry the most. The 8/21 expiry is the least call-skewed (1.85) —
  the one tenor with meaningful two-way interest.

## DTE regime (`uw options-flow dte-volume-share`) `[FLOW:dte-volume-share]`

- regime_hint **BALANCED** — 0DTE **0%**, weeklies 19.0%, monthlies 19.4%,
  LEAPs 5.1%. Not a same-day gamma event; positioning is spread along the curve →
  **swing/positioning flow, not intraday churn.**

## Tool calls

```bash
uw options-flow sweeps              --symbol CRM --date 2026-05-29 --json
uw options-flow top-premium-trades  --symbol CRM --date 2026-05-29 --top-n 12 --json
uw options-flow expiry-heatmap      --symbol CRM --date 2026-05-29 --json
uw options-flow dte-volume-share    --symbol CRM --date 2026-05-29 --json
uw hot-chains smart-money-flow / most-active   # market-wide; CRM outside top-80 (see Read-through)
```

## Tool errors

- `uw hot-chains *` take no `--symbol` (market-wide rankings). CRM does **not**
  appear in the bullish smart-money-flow top-80 — consistent with phase-0.5's
  cross-sectional read (CRM is a sector laggard by raw volume; the mega-caps
  dominate the universe-level chain rankings). Not an error; recorded.

## Read-through

- This is the phase that **converts phase-0.5's "unusual" into "unusual *and*
  bullish."** Zero put sweeps, call premium leading every expiry, fresh ask-side
  buying of the 6/18 200C / 6/5 190C, and longer-dated 220C '27 upside bets — the
  flow is unambiguously positioned for **continuation higher**, with $200 (+4.7%)
  the visible target strike.
- **But not a stampede.** 44% of sweep premium hit the bid (some selling/writing
  into strength), the single largest trade was a 230C *bid*, and 190P hedges appear
  — so there is two-way activity under the call-dominant surface. Combined with the
  IV-crush backdrop (phase-0.5: IV rank 35th self-pctile — vol got *cheaper* into
  the move), the cleanest interpretation is **directional-long repositioning the day
  after a catalyst**, with some early profit-taking, rather than a euphoric chase.
- Hands to phase-3/4: the **$200 call magnet** and the spread-along-the-curve DTE
  profile should show up as call-OI building at 200 and a dealer-gamma map that
  matters more for June/July than for 0DTE.

## Citations

- `[FLOW:sweeps]` 20/20 call sweeps, $26.3M, ask 0.56 ($14.3M/$11.1M), $200 magnet — `uw options-flow sweeps`
- `[FLOW:expiry-heatmap]` call premium leads every expiry (7/17 $18.1M vs $4.7M) — `uw options-flow expiry-heatmap`
- `[FLOW:dte-volume-share]` BALANCED, 0DTE 0%, weeklies/monthlies ~19% — `uw options-flow dte-volume-share`
- `[FLOW:top-premium-trades]` 10/12 top single bets calls; only puts = 190P Sep — `uw options-flow top-premium-trades`

## Upstream references

- phase-0.5-context.md §Self-history — "net-call premium 100th self-pctile, P/C 0th";
  phase-1 confirms the *mechanism*: 100% call sweeps, call premium leading every expiry.
- phase-0-intake.md §Key datapoints — "P/C 0.235, call premium $94.5M vs put $24.9M";
  phase-1 resolves that aggregate into ask-side, curve-spread, $200-targeted call buying.

## Next phase

- phase-2-dark-pool.md (does the $1.45B dark-pool cash tape from phase-0.5 confirm
  institutional accumulation at/around $190, or is it distribution into the pop?)
