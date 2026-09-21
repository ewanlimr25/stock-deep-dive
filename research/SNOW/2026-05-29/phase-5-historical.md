# Phase 5 — Historical Context & VRP

**Ticker:** SNOW · **As-of:** 2026-05-29 · **Generated:** 2026-05-29
**Upstream:** phase-4-structure.md (long-gamma pin $250–$255) · phase-2 (mega-tier
distribution) · phase-1 (cautious) · phase-0.5 (GENUINELY_UNUSUAL)

> **Gap-aware:** local window non-contiguous (21-session hole 2026-03-28→04-24);
> "30d/90d" reads span ~34 available sessions. Trailing tools anchor to the latest
> date (2026-05-29 == as-of).

## Summary

History delivers the loudest caution flag of the run: **SNOW is parabolic and
deeply overbought.** Price ran **$168 → $255 (+52%)** over the window
`[HIST:trend]`, RSI(14) is **86.9**, price sits **+53.8% above its 20-day SMA**,
**+63.8% above the 50-day**, and **−9% from the 52-week high** ($280.67)
`[HIST:rsi fz][HIST:52w_proximity fz]`. VRP is **negative (−0.55)** — IV30 61% vs
a trailing **realized vol of ~116%** — but that "cheap vol" reading is an artifact
of the explosive one-time run/earnings gap, not a repeatable edge. The
bullish_flow signal backtest is **50% / n=8 — no historical edge** (identical to
the PATH read) `[HIST:signal-backtest]`. The one genuinely bullish historical fact
is **net-positive 90d premium flow** (bull $1.167B vs bear $1.085B, +$82M) — a
real sustained accumulation behind the run. But layered onto phase-2 mega-tier
distribution and the phase-4 $255 gamma pin, the technical extension says this is
**blow-off / distribution territory**: a fresh long here is chasing an RSI-87,
+54%-above-the-20d move into a wall — historically edge-negative on risk/reward.

## Key signals

- **RSI 86.9, +53.8% above SMA20, near 52w high** `[HIST:rsi fz]` — extreme
  overbought; severe mean-reversion risk for a new long.
- **+52% run in the window** ($168→$255) `[HIST:trend]` — parabolic; the move is
  largely *made*, not beginning.
- **bullish_flow backtest 50%, n=8 — no edge** `[HIST:signal-backtest]`. Kelly `p`.
- **VRP −0.55 (vol cheap vs realized 116%)** `[HIST:vrp]` — premium-buying *signal*,
  but realized is inflated by the one-time gap; discount it.
- **90d premium flow net bullish** (+$82M, $1.167B vs $1.085B)
  `[HIST:cumulative-premium-flow]` — the real sustained bid behind the run (the
  one bull counterpoint to the distribution read).

## Detailed findings

### IV regime
IV30d **61.1%**, **35.3rd percentile** (252d), z −0.74, regime **NORMAL** (n=34).
Middling — not a cheap-vol or rich-vol extreme on the 1y lens.

### VRP
IV30 **61%** vs RV30 **~116%** → VRP **−0.55**, "vol cheap vs realised — favour
premium buying." **Caveat:** RV is distorted by the +52% run/gap; forward realized
unlikely to sustain 116%. Reconcile with phase-4 front backwardation: sell the
rich 0–7DTE front, but the 30d IV is genuinely not expensive. Net: ambiguous,
don't lean hard on "cheap vol."

### P/C ratio z-score
PCR 0.398; z **null** (insufficient clean history to compute). Call-tilt is normal
for SNOW; no usable extreme read.

### Cumulative premium flow (~34 sessions)
Bull **$1.167B** vs bear **$1.085B** → net **+$82M bullish**. Sustained net-bullish
premium — the run was flow-supported, unlike PATH's balanced 90d.

### Multi-day trend (~34 sessions, spans gap)
Price **$168.02 → $255.55 (+52%)**; **14 bull / 16 bear days** (mixed daily
breadth despite the huge net move — i.e. big up-gaps, choppy in between); IV rank
**43 → 51**.

### Price context (`fz`, advisory)
- **RSI(14) 86.9** — extreme overbought (>70 = OB; 87 is rare).
- **+53.8% above SMA20, +63.8% above SMA50, +25.9% above SMA200** — vertical;
  enormous gap to any mean.
- **−9.0% from 52w high $280.67; +116% above 52w low $118.30; Perf YTD +16.5%.**
- Read: **late-stage parabolic move into resistance** — chase risk is extreme;
  the fade/range entries are the disciplined ones.

### Signal backtest
| Signal | Win rate | N |
|---|---|---|
| bullish_flow | **50.0%** | 8 |
| dark_pool_distribution | (no usable result) | — |

## Tool calls
| Tool | Args | Result |
|---|---|---|
| `historical iv-percentile-zscore` | `--lookback-days 252` | 35.3 pctile, NORMAL |
| `historical vrp` | `--realised-window-days 30` | −0.55 (RV 116% inflated) |
| `historical cumulative-premium-flow` | `--days 90` | net +$82M bullish |
| `historical pc-ratio-zscore` | `--lookback-days 20` | z null |
| `historical trend` | `--days 30` | +52% run, 14/16 days |
| `historical signal-backtest` | `bullish_flow` / `dark_pool_distribution` | 50% n=8 / n/a |
| `fz quote` | `--agent` | RSI 86.9, +54% vs SMA20, near 52w high |

## Tool errors
- `pc-ratio-zscore` z-score null (insufficient clean series).
- `signal-backtest dark_pool_distribution` returned no usable win-rate; relying
  on bullish_flow 50% (n=8) as the Kelly `p`.

## Verdict for downstream

- **Volatility regime: NORMAL IV, negative VRP (premium-buying signal, but
  realized-distorted)** → for a range/fade view, **selling the rich front premium**
  (phase-4 backwardation) is the cleaner structural read than buying vol.
- **Premium environment:** net-bullish 90d (flow-supported run) — but the move is
  *made* and now meeting distribution.
- **Conviction that today's signal is HISTORICALLY EDGE-POSITIVE: 1.5 / 5** —
  50% win rate (no edge) *plus* extreme overbought extension makes a fresh long
  edge-negative on risk/reward. The edge, if any, is in fading/range, not chasing.
- **Three datapoints:** RSI **86.9** · VRP **−0.55** · signal win rate **0.50 (n=8)**.
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:               bullish_flow
  signal_backtest_win_rate:   0.50
  win_rate_n:                 8
  win_rate_source:            backtest
  ```
  Kelly `p` = 0.50, n<10 → cap 0.75 → p=0.50; near-zero Kelly, **starter at most**,
  and the RSI-87 extension argues against a long-side directional bet entirely.
- **Open questions:**
  - With the move parabolic + distribution (phase-2) + gamma pin (phase-4), is the
    only disciplined long expression a *defined-risk pullback entry*, or is the
    edge actually a **fade / premium-sale** at the $255 wall? Carry to phase-8b.
  - Does fundamental quality (phase-7b) justify the +52% re-rate, or is valuation
    now stretched (chase risk on the fundamentals too)?
