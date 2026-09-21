# Phase 2 — Dark Pool & Block Prints

**Ticker:** ELF
**As-of date:** 2026-06-30
**Generated:** 2026-07-01T00:24:19Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md

## Summary

Institutional dark-pool activity is **mild-to-moderate accumulation, aligned with an
extended rally** — but the headline number is a trap. The single largest print,
**3,242,478 shares / $241.2M at $74.39, executed 20:04 UTC (16:04 ET, post-close on
quarter-end June 30)**, is a **closing-cross / index-rebalance block** (extended-hours,
one trade, quarter-end) and is **de-rated to non-directional** per the phase's own
pitfall guidance. Stripping it, the genuine read is the **large tier: buy_ratio 0.61
across 115 trades** ($25.95M) plus **block tier 0.584** — suggestive net buying, not a
high-confidence (>0.7) signal. Critically, ELF has **rallied +17% in six sessions**
($63.18 → $74.00, +5.9% on 06-30 into the close), and the 5-day dark-pool price-level
clusters ($64–65, $67, $70) map precisely onto that run's consolidation steps —
institutions bought *into* the move. The picture: real accumulation confirming
phase-1's bullish flow, but on a **now-extended** breakout.

## Key signals

- **Large-tier buy_ratio 0.61** (buy 217,950 / sell 139,063 sh, 115 trades, $25.95M) — suggestive accumulation, the most robust DP signal [DP:block-stratified `.results[].large.buy_ratio`]
- **$241.2M / 3.24M-sh single print @ $74.39, 16:04 ET post-close, quarter-end** — flagged as **rebalance cross, de-rated to non-directional** [DP:largest][DP:extended-hours]
- **5-day price-level clusters at $64–65 / $67.4 / $69.91** = the rally's institutional cost/support ladder [DP:price-levels]
- **$74 cluster (7 prints, $6.76M) sits exactly at spot** — the immediate battleground/pin [DP:price-levels]
- **After-hours prints at $73.02–$73.54 (19:22–19:23 ET), below the $74 close** — mild post-market give-back [DP:extended-hours]

## Detailed findings

### Largest blocks `[DP:largest]`

| Time (ET) | Price | Size (sh) | Premium | NBBO | vs mid | Read |
|---|---|---|---|---|---|---|
| 16:04 | $74.39 | 3,242,478 | **$241.2M** | 73.50/74.45 | above | **quarter-end close cross — rebalance, de-rate** |
| 16:00 | $74.00 | 61,900 | $4.58M | 73.50/74.45 | above | close print |
| 16:06 | $73.41 | 54,645 | $4.01M | 73.65/74.40 | below | close-adjacent sell |
| 14:10 | $73.76 | 14,739 | $1.09M | 73.68/73.78 | above | intraday buy |
| 19:23 | $73.02 | 12,875 | $0.94M | 73.43/73.89 | below | after-hours sell |
| 12:35 | $73.41 | 11,814 | $0.87M | 73.37/73.40 | above | intraday buy |
| 12:05 | $72.75 | 10,000 | $0.73M | 72.67/72.76 | above | intraday buy |
| 11:15 | $71.79 | 10,000 | $0.72M | 71.62/71.78 | above | intraday buy |

Top-25 total = **$263.1M / 3.54M sh**; the one rebalance print is **92%** of it. The
*organic* intraday prints (excluding the close cross) are mostly **above mid** —
consistent with buyers paying up into the rally.

### Tier breakdown `[DP:block-stratified]`

| Tier | buy_ratio | sell_ratio (1−buy) | buy_vol | sell_vol | premium | trades |
|---|---|---|---|---|---|---|
| mega | **1.00** | 0.00 | 3,242,478 | 0 | $241.2M | **1** ← the rebalance cross; ignore as signal |
| block | 0.584 | 0.416 | 76,639 | 54,645 | $9.68M | 3 |
| **large** | **0.61** | 0.39 | 217,950 | 139,063 | $25.95M | **115** ← the real read |
| — | | | | | | |

The mega tier's perfect 1.0 is an artifact of the single cross. The **decision-grade
signal is large-tier 0.61 over 115 trades** — net buying, in the "suggestive" band
(0.55–0.70), not "high-confidence" (>0.70). Direction: accumulation, moderate.

### Price levels — 5-day clusters `[DP:price-levels]`

(Window anchors to latest date = 2026-06-30; spans ~06-24→06-30 per phase-0 dates.)

| Level | Premium | Prints | Note |
|---|---|---|---|
| $74.39 | $241.2M | 1 | rebalance cross — not a cluster |
| **$74.00** | $6.76M | 7 | **at spot — immediate battleground** |
| $73.41 | $5.03M | 3 | near spot |
| **$69.91** | $2.96M | 8 | = 06-29 close → **first support** |
| $67.43 | $3.47M | 5 | = 06-26 close → support |
| **$64.26–$64.69** | ~$7.8M | 3–4 each | = 06-24/25 consolidation → **major lower shelf** |

Clusters sit **below** the $74 spot because ELF *ran up through them* — the ladder is
now support, and institutions are in-the-money on it (bullish, they'll defend).

### Extended-hours `[DP:extended-hours]`

Dominated by the **quarter-end close** (16:00–16:09 ET: the $241M cross + ~$5.7M of
$74 prints). Genuine after-hours (19:22–19:23 ET) shows two small sells at
$73.02/$73.54 — a **mild give-back below the $74 close**, worth watching but tiny
($1.07M combined) next to the day's tape. No overnight news-driven block to attribute
(hand to phase-6).

### Cross-market rank `[DP:ticker-summary]`

ELF is **outside the DP ticker-summary top-30** (`index("ELF") == null`) — its
dark-pool footprint isn't market-leading in absolute terms (mega-caps print larger
daily), consistent with phase-0.5 (98th percentile, not top-50 absolute). Recorded,
not an error.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw dark-pool largest --symbol ELF --top-n 25 --sort-by premium --date 2026-06-30` | $241.2M cross ← `.results[0].premium`; total $263.1M ← `[.results[].premium]\|add` | top-25 |
| `uw dark-pool block-stratified --symbol ELF --top-n 30 --min-tier large --date 2026-06-30` | large buy_ratio 0.61 ← `.results[].large.buy_ratio`; sell derived 1−0.61 | 3 tiers |
| `uw dark-pool price-levels --symbol ELF --top-n 15 --days 5` | $74 cluster 7 prints ← `.results[].trade_count`; $64–65 shelf | top-15 |
| `uw dark-pool extended-hours --symbol ELF --top-n 15 --date 2026-06-30` | $241M @ 16:04 ET post-close ← `.results[0].executed_at` | 10 |
| `uw dark-pool ticker-summary --top-n 30 --date 2026-06-30` | ELF absent ← `index("ELF")==null` | 0 |

## Tool errors

_None — all five reads returned exit 0 and valid JSON._

## DATA NOTE / CORRECTION

_None — first reads stood. `size` is null in `price-levels` (that tool returns
`total_shares`/`total_premium`/`trade_count`, no per-level size); premiums used
directly._

## Verdict for downstream phases

- **Net institutional bias:** **MILD-TO-MODERATE ACCUMULATION**, confirming phase-1's
  bullish tilt — but the headline $241M print is a **quarter-end rebalance cross,
  de-rated to non-directional**. Do not treat it as accumulation.
- **Conviction:** **3 / 5** — large-tier 0.61 (115 trades) + above-mid intraday buys +
  the confirming 6-session rally support the accumulation read; held at 3 (not higher)
  because the signal is "suggestive" (0.55–0.70), not high-confidence, once the
  rebalance print is stripped.
- **Largest block as % of float (advisory):** float unavailable this run (`fz` grid
  degraded, phase-0). Using shares-outstanding ≈ **59.5M** (mkt cap $4.40B / $74): the
  $241M cross ≈ 3.24M sh ≈ **~5.4% of shares out in one print** — implausibly large for
  organic accumulation, **reinforcing the rebalance-cross reading**. The organic
  large-tier buy volume (217,950 sh ≈ ~0.37% of shares out) is the real, modest footprint.
- **Three S/R levels for phase-9:**
  1. **$74.00** — spot / immediate pivot (7-print DP cluster, at the 06-30 close & near intraday high $74.36).
  2. **$69.91–$70** — first support (8-print cluster = prior-day close); logical stop reference for a momentum long.
  3. **$64–65** — major lower institutional shelf (5-day accumulation zone); thesis-defining support — a break below invalidates the breakout.
- **Open questions:**
  - Does **phase-3 OI** show the $74/$75 strikes as a pin (gamma wall) given the DP $74 cluster + phase-1 $75 Aug call concentration?
  - Is the **+17% six-session run** overbought (phase-5 historical / phase-8 contrarian) — chase risk into an extended move?
  - No news attributed to the after-hours softness — phase-6 to check for an overnight catalyst.
