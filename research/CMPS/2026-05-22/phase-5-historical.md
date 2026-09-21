# Phase 5 — Historical Context & VRP

**Ticker:** CMPS
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T00:00:00Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md, phase-3-positioning.md, phase-4-structure.md

## Summary

The single most important historical fact: **options are cheap relative to how much
CMPS actually moves.** VRP is **−0.7132** — implied vol 75% vs **realized vol 146%** —
a deep **PREMIUM-BUYING** regime. This *favors long-premium / debit structures* and is
a yellow flag on phase-3's put-*selling* leg (selling cheap vol), while validating the
institutional Jul $12 call *buying* (buying cheap vol). Second: **a major catalyst is
hidden in the data gap** — spot ran from $5.37 (3/27) to **$8.93 (4/27)** across the
21-session hole, then ground to $11.85; the GEX series confirms a regime change from
negative-gamma chop at $5 to **sustained POSITIVE gamma for ~1 month while the stock
trended UP +33%** (so positive gamma here has *not* meant range-bound — phase-4's pin
read must be tempered). Premium flow over the available window is **MIXED** (net
+$555k, balanced), the recent 8-session run was bullish-flow-driven, and today's
bearish print is a 1-day flip. P/C and IV are unremarkable (no extreme). The
name-specific dark-pool-accumulation backtest has **n=0** (no usable edge measurement);
the bullish_flow backtest reads 87.5% but is market-wide and regime-contaminated.

## Key signals

- **VRP −0.7132**: IV30d 75.0% vs realized 146.3% → **PREMIUM-BUYING**, favour debit/long options `[HIST:vrp]`.
- **Catalyst in the gap**: $5.37 (3/27) → $8.93 (4/27), +66% over the 21-session hole → unknown event re-rated the name `[HIST:gex_time_series]` `[HIST:trend]`.
- **Sustained POSITIVE gamma ~1 month, stock grinding UP** $8.93→$11.85 (+33%) — positive gamma ≠ stuck for this name `[HIST:gex_time_series]`.
- **IV percentile 36.67** (over the **30 sessions actually available**, not 252), z −0.17, regime NORMAL; iv_rank 12.25 — low-to-mid, cheap vs realized `[HIST:iv_percentile_zscore]`.
- **Premium flow MIXED**: 31-session net +$555,180 (bullish $8.56M vs bearish $8.01M) — balanced, no stealth one-way build `[HIST:cumulative_premium_flow]`.
- **dark_pool_accumulation backtest n=0** (no edge measurement); **bullish_flow 87.5% / n=16** market-wide proxy only `[HIST:signal_backtest]`.

## Detailed findings

### IV regime (percentile + z-score + VRP) `[HIST:iv_percentile_zscore]` `[HIST:vrp]`

- `iv_percentile 36.67`, `iv_zscore −0.17`, regime **NORMAL** — but computed over
  `dates_used 30` (only ~30 sessions exist locally, not the requested 252). So this is a
  ~6-week percentile, not a 1-year one — **interpret as "middling for the recent window,"
  not a true 1y rank.** The screener `iv_rank 12.25` (phase-0.5) is the more bearish-on-vol read.
- **VRP −0.7132** (IV30d 0.7495 − realized 1.4627): realized vol (146%) is ~2× implied
  (75%). **Vol is cheap vs how the stock moves → PREMIUM_BUYING.** The realized window
  captures the explosive $5→$12 run, so it's elevated by a real trend, not noise. Net:
  the edge is in *owning* optionality, not selling it.

### Cumulative premium flow (window = 31 available sessions, gap-aware) `[HIST:cumulative_premium_flow]`

`cumulative_bullish $8,563,421 · cumulative_bearish $8,008,241 · net +$555,180 · MIXED`.
Requested days=90 but only **31 sessions exist** (2026-03-13…05-22, the 03-28→04-24 hole
excluded — never read this as a contiguous 90 days). Net flow is mildly bullish but
essentially **balanced** — no stealth one-directional institutional accumulation
signature. Consistent with a volatile, two-sided, headline-driven biotech.

### P/C ratio z-score `[HIST:pc_ratio_zscore]`

`current_pc 0.129 · mean 0.268 · std 0.251 · z −0.553 · NORMAL`. Today is more
call-heavy than the 20-day norm but only −0.55σ — **no sentiment extreme**, no
contrarian trigger.

### GEX time series — regime stability (30 sessions, gap-aware) `[HIST:gex_time_series]`

Trajectory (abbreviated):

| date | spot | regime | total_gex | ZGL |
|------|------|--------|-----------|-----|
| 03-16→03-23 | $5.3–6.3 | NEGATIVE / FULLY_NEG | −0.5M to −2.8M | ~5 / null |
| 03-24→03-27 | $5.2–5.6 | POSITIVE | +0.37–0.52M | 2–4 |
| **[GAP 03-28→04-24]** | — | — | — | — |
| 04-27 | **$8.93** | POSITIVE | +0.28M | 4.07 |
| 05-01→05-06 | $9.0–9.7 | POSITIVE | +1.0–1.9M | 4–6 |
| 05-07 / 05-12 | $9.4 / $9.38 | NEGATIVE (brief) | +1.6M / +2.0M | 9.73 |
| 05-13→05-20 | $10.1–10.85 | POSITIVE/FULLY_POS | +3.4–5.7M | 1–4 / null |
| 05-21 | $11.53 | POSITIVE | +2.19M | 2.01 |
| **05-22** | **$11.85** | POSITIVE | +1.63M | **9.02** |

Reads: (1) **Pre-gap the name was a negative-gamma $5 chop-stock; post-gap it is a
positive-gamma uptrend** — a structural character change tied to the gap catalyst.
(2) Two brief NEGATIVE flips (05-07, 05-12) where spot dipped under a momentarily-high
ZGL (~9.73) **both resolved UP** (05-08, 05-13 rally to $10.85) — vol-expansion episodes
that broke higher, not lower. (3) total_GEX peaked $5.7M (05-15) and has since *halved*
to $1.63M as OI rolled — the pin is real but **loosening**, and the month-long record
shows price can **trend up inside positive gamma**. ZGL $9.02 is the highest sustained
floor, tracking the rising stock.

### OI trend & multi-day table `[HIST:trend]`

- 30-session split: **15 bullish / 15 bearish** flow days — genuinely two-sided.
- The run that matters: 05-12 close **$9.37** → 05-22 **$11.81** (**+26%**), predominantly
  bullish-flow days; **05-21 was the strongest** (+$553k net, $2.1M call premium); **05-22
  (today) is the first bearish flip** (−$276k) — a 1-day event, not yet a trend.
- IV rank stayed **low throughout (6–18)** even as the stock rallied — cheap vol is the
  name's persistent state, reinforcing the VRP premium-buying read.
- `total_open_interest` peaked **132,273 (05-15)** and has fallen to **89,658 (05-22)** —
  OI *contracting* off the mid-May peak (expiry/closing), consistent with phase-3's roll.

### Signal backtest (current signal's historical edge) `[HIST:signal_backtest]`

- **`dark_pool_accumulation`** (the cleanest phase-2 signal): `{"note":"no backtest
  results","total_signals":0}` → **no name-specific edge measurement available.**
- **`bullish_flow`** (proxy for the reconciled bullish thesis): `win_rate 87.5%`,
  `total_signals 16`, avg +9.83% / 10d. **Heavy caveats:** this is a **market-wide**
  backtest of the last ~4 days' bullish_flow signals (MCHP, MU ×3, AMD ×2, SNDK ×2,
  PANW…), **not CMPS-specific**, and the window was a strong semis-momentum tape — so
  87.5% reflects a **favourable recent regime**, not CMPS's idiosyncratic edge. n=16 over
  4 days = small and autocorrelated. Treat as a soft regime tailwind, not a Kelly p for CMPS.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `historical_iv_percentile_zscore` | symbol=CMPS, lookback=252 | pctile 36.67 (30 dates), z −0.17, NORMAL |
| `historical_vrp` | symbol=CMPS, realised=30 | VRP −0.7132, IV 75% vs RV 146%, PREMIUM_BUYING |
| `historical_cumulative_premium_flow` | symbol=CMPS, days=90 | net +$555k over 31 sessions, MIXED |
| `historical_pc_ratio_zscore` | symbol=CMPS, lookback=20 | z −0.553, NORMAL |
| `historical_gex_time_series` | symbol=CMPS, days=30 | POSITIVE ~1mo, uptrend; brief neg flips 05-07/12 |
| `historical_trend` | symbol=CMPS, days=30 | 15/15 days; +26% run 05-12→22; today 1st bearish flip |
| `historical_signal_backtest` | dark_pool_accumulation, 10d | n=0 (no results) |
| `historical_signal_backtest` | bullish_flow, 10d | 87.5%, n=16 (market-wide, regime-contaminated) |

## Tool errors

_None._ Data-quality caveats (not errors): (1) IV percentile computed over 30 sessions,
not 252 — the local window is short. (2) The 90-day premium-flow and 30-day series both
**span the 03-28→04-24 gap**; session counts (31, 30) are *available* sessions, not
calendar days — no annualization performed across the hole.

## Verdict for downstream phases

- **Volatility regime: CHEAP** (VRP −0.71; realized 146% ≫ implied 75%). **Premium-BUYING
  environment → favour DEBIT/long-premium structures; penalize premium-selling.** This
  is the dominant sizing/structure input and *aligns with* the institutional Jul $12 call
  buying (phase-3) while *cautioning against* the Jun $11 put-write leg.
- **Premium-buying vs selling:** decisively **buying.** A long-call or call-debit-spread
  expresses the reconciled bullish thesis *and* harvests the cheap-vol edge; an overwrite
  would give away mispriced optionality.
- **Conviction that today's signal is HISTORICALLY EDGE-POSITIVE: 3/5.** The cheap-vol +
  positive-gamma-uptrend + slight-net-bullish-flow backdrop is constructive and the
  bullish_flow regime proxy is supportive, but (a) the name-specific DP-accumulation
  backtest is empty (n=0), (b) flow is genuinely two-sided (15/15), and (c) the gap
  catalyst is unidentified — so this is a "plausible, vol-supported edge," not a
  measured one.
- **Three specific data points:** IV percentile **36.67** (30-session) / VRP **−0.7132**
  (premium-buying) / bullish_flow win-rate **87.5% (n=16, market-wide proxy)**.
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:              bullish_flow   # CMPS-specific dark_pool_accumulation = n=0; this is a market-wide proxy
  signal_backtest_win_rate:  0.875
  win_rate_n:                16
  win_rate_source:           backtest        # CAVEAT: market-wide & regime-contaminated; apply N-conditional cap, lean to conviction bin
  vrp:                       -0.7132         # premium-buying — favour debit; not in template but decisive for structure choice
  ```
- **Open questions for phases 6–7c:**
  - **What was the 03-28→04-24 gap catalyst** that doubled the stock ($5.37→$8.93)? Clinical
    readout? Partnership? Financing? This defines the *base* of the current move. (phase-6/7)
  - Does the **Nov '26 IV bump** (phase-4) correspond to a scheduled H2 readout — the next
    binary that would resolve the cheap-vol/premium-buying setup explosively? (phase-6/7c)
  - With realized 146%, is a **defined-risk debit** (call spread) the right way to own the
    cheap vol without paying for 146%-realized tails, or does the binary risk argue for
    a long single call (max-loss = premium)? (phase-9 structure)
