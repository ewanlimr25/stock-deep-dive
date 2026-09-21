# Phase 2 — Dark Pool & Block Prints

**Ticker:** RKT
**As-of date:** 2026-07-17
**Generated:** 2026-07-19T19:29:00-04:00
**Upstream phases cited:** phase-0.5-context.md, phase-1-flow.md

## Summary

Dark pool **diverges from the bearish options tape: the continuous institutional
flow was net-BUYING.** The large tier — the day's bulk at $191.2M across 1,426
prints — carries `buy_ratio 0.651` (buy 8.50M sh vs sell 4.55M sh), and the top-10
individual blocks mostly executed *above* NBBO mid. The two eye-catching mega prints
(2.07M sh / $30.1M and 988k sh / $14.4M, both at $14.54) net to a *sell* (mega
`buy_ratio 0.323`) — **but both are after-hours (20:03 & 20:48 UTC = post-4pm ET)
closing-facilitation prints carrying `ext_hour_sold_codes`, executed at the mark,
not aggressive distribution.** Net read: **mild accumulation** on the high-quality
continuous tape, mechanically offset by a large closing cross. Five-day price
levels define a tight **$14.30 support / $14.54 pivot / $14.90 resistance** shelf.

## Key signals

- **Large-tier `buy_ratio 0.651`** — $191.2M / 1,426 trades, buy 8.50M vs sell 4.55M sh → continuous **accumulation** `[DP:block_stratified]`
- **Mega-tier `buy_ratio 0.323`** — but only 2 prints, both **after-hours closing crosses** at $14.54 → mechanical, de-rated `[DP:block_stratified / extended_hours]`
- **Top block 2.07M sh / $30.1M @ $14.54**, tvm −0.005 (just below mid, closing print) `[DP:largest]`
- **Price-level support shelf $14.30** (3.19M sh, $45.7M, 5-day) below spot; **$14.90 resistance** (1.58M sh) above `[DP:price_levels]`
- **RKT not in dark-pool top-30 by absolute premium** (list is SPY/MU/QQQ/SNDK/NVDA, all $5B+) but its ~$238M all-tier premium is heavy for a $14.6B-float name `[DP:ticker_summary]`

## Detailed findings

### Largest blocks `[DP:largest]`

| Time (UTC) | Price | Size (sh) | Premium | trade_vs_mid | Read |
|---|---|---|---|---|---|
| 20:03:36 | 14.54 | 2,069,471 | $30,090,108 | −0.005 | AH closing cross, mild sell |
| 20:48:38 | 14.54 | 987,716 | $14,361,391 | 0.000 | AH, at mid → neutral |
| 19:45:14 | 14.535 | 180,590 | $2,624,876 | +0.020 | block-tier, **buy** (above mid) |
| 14:18:19 | 14.7901 | 48,734 | $720,781 | −0.005 | midday, ~mid |
| 13:46:51 | 14.74 | 45,000 | $663,300 | +0.005 | buy lean |
| 19:47:39 | 14.495 | 45,000 | $652,275 | 0.000 | at mid |
| 13:36:10 | 14.61 | 35,000 | $511,350 | +0.015 | buy lean |

Most continuous-session prints (rows 3–7) sit at or above NBBO mid → buy-side lean,
matching the large-tier ratio. The two AH mega prints are the only meaningful sells
and are structurally mechanical (closing facilitation at the $14.54 mark).

### Tier breakdown `[DP:block_stratified]`

| Tier | buy_ratio | derived sell_ratio | buy_vol | sell_vol | total_premium | trades |
|---|---|---|---|---|---|---|
| **large** | **0.651** | 0.349 | 8,496,882 | 4,551,285 | $191,202,656 | 1,426 |
| **mega** | **0.323** | 0.677 | 987,716 | 2,069,471 | $44,451,499 | 2 |
| block | 1.000 | 0.000 | 180,590 | 0 | $2,624,876 | 1 |
| retail | — | — | 0 | 0 | 0 | 0 |
| **all tiers** | — | — | — | — | **$238,279,031** | — |

The signal-bearing tier is **large** (1,426 trades = genuine continuous flow) at
**0.651 buy** — "suggestive" accumulation (0.55–0.70 band, not high-confidence
>0.70). The mega tier's sell tilt is 2 after-hours prints → discounted per phase-2
pitfalls (extended-hours ≠ directional intent).

### Price levels (5-day institutional S/R) `[DP:price_levels]`

| Price level | Shares | Premium | Trades |
|---|---|---|---|
| **14.54** | 3,901,769 | $56,729,178 | 71 |
| **14.30** | 3,192,863 | $45,657,154 | 36 |
| **14.60** | 2,877,518 | $42,010,132 | 91 |
| 14.77 | 1,748,000 | $25,814,321 | 162 |
| **14.90** | 1,583,037 | $23,586,622 | 34 |
| 14.76 | 1,520,831 | $22,444,520 | 170 |
| 14.62 | 1,212,535 | $17,724,646 | 134 |

Dense institutional interest **$14.30 → $14.90**, single heaviest right at spot
$14.54. The $14.30 shelf (3.19M sh) is a firm support; $14.90 (prev-session high) a
lighter resistance. This is a coiled, well-defined range — supports a mean-reversion
or range read into earnings rather than a trending break.

### Extended-hours activity `[DP:extended_hours]`

Top two AH prints ARE the two mega blocks (20:03 / 20:48 UTC, both $14.54,
`ext_hour_sold_codes` present) → closing-auction / facilitation prints, not overnight
directional accumulation. Smaller AH prints (25k @ 14.54, 24k @ 14.53) are trivial.
No pre-market catalyst-driven block detected (cross-ref phase-6).

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw dark-pool largest --symbol RKT --top-n 25 --sort-by premium` | top block 2.07M sh $30.1M @14.54 tvm −0.005 ← `.results\|sort_by(-.premium)` | 25 |
| `uw dark-pool block-stratified --symbol RKT --min-tier large` | large.buy_ratio 0.651; mega.buy_ratio 0.323 ← `.results[0].<tier>.buy_ratio` | 1 (tiered) |
| `uw dark-pool price-levels --symbol RKT --days 5` | $14.54 (3.90M sh) / $14.30 (3.19M) / $14.90 (1.58M) ← `.results[].price_level` | 15 |
| `uw dark-pool extended-hours --symbol RKT --top-n 15` | 2 mega prints AH w/ ext_hour_sold_codes ← `.results[]` | 15 |
| `uw dark-pool ticker-summary --top-n 30` | RKT not in top-30 (SPY/MU/QQQ lead) ← `.results[]` | 30 |

## Tool errors

None. `ticker-summary` jq select for RKT returned null → RKT is **outside the
top-30** absolute-premium names (an expected finding for a $14.6B-cap vs
$5B+-premium ETFs/mega-caps), not a tool error. All numeric reads round-tripped
through `jq`.

## DATA NOTE / CORRECTION

`price-levels` first jq used `.price`/`.premium` (null); correct fields are
`.price_level`/`.total_premium`/`.total_shares`/`.trade_count` — re-read and all
level premiums trace to `.total_premium`. `block-stratified` buy/sell read per the
phantom-field rule: **no `sell_ratio` field** — derived `sell_ratio = 1 − buy_ratio`
from `.results[0].<tier>.buy_ratio`.

## Verdict for downstream phases

- **Institutional bias:** **Mild ACCUMULATION** (continuous large tier 0.651,
  above-mid prints), with a mechanical mega closing SELL to net against — call it
  **accumulation-leaning MIXED**. This **partially offsets phase-1's bearish delta
  lean** → a genuine cross-lane divergence for phase-8b to adjudicate.
- **Conviction:** **2–3 / 5** — 0.651 is suggestive, not high-confidence (>0.70);
  the tape's biggest prints are AH/mechanical, which caps how much to lean on it.
- **Largest block as % of float:** **n/a** (`fz` float unavailable, phase-0) —
  advisory estimate: the 3.06M mega closing shares ≈ ~0.3% of the ~1.0B Class-A
  share count (marketcap $14.6B ÷ $14.54); modest and consistent with a mechanical
  closing cross rather than a float-moving accumulation. Tag `[DP:block_pct_float est]`.
- **Three S/R levels for phase-9:**
  1. **Support $14.30** (3.19M-sh, $45.7M shelf) — primary downside reference / stop zone.
  2. **Pivot $14.54** (3.90M-sh, heaviest cluster = spot) — the pin/mean.
  3. **Resistance $14.90** (1.58M sh, prev-session high) — first upside cap.
- **Open questions:** does OI positioning (phase-3) confirm a pin near $14.5 into
  the Jul-24 weekly / 07-30 earnings? Is the continuous dark-pool buying institutions
  accumulating stock while hedging with the phase-1 puts (long-stock + put-hedge),
  which would reconcile the divergence?
