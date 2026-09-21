# Phase 4 — Dealer Structure & Gamma

**Ticker:** MSTR
**As-of date:** 2026-05-19 (effective)
**Generated:** 2026-05-20T00:20:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md

## Summary

The dealer-structure tape resolves several of the open questions from phases 1–3
and reveals the single loudest signal in the workup so far: a **binary-event
IV spike on the 2026-06-18 expiry at 143.0% IV vs ~75–78% for its neighbors**
(May 22 weekly is also elevated at 93.2% because of OPEX). The 45-DTE
**Zero Gamma Level is $174.79 with spot at $165.76** — i.e. dealers are in a
**short-gamma regime** at the 45-day window (trend amplification) and the
flip level aligns almost exactly with the **phase-2 institutional cost-basis
ceiling ($174–$179)**, the highest-confluence trigger of the workup. Counter-
intuitively, the **OPEX-week (May 22) gamma surface is POSITIVE** with ZGL
$169.66 and a stack of dealer-long-gamma "support walls" at $170, $180, $182.5,
$190 — meaning Friday's expiry pins price into the $170–$180 corridor while
the *underlying* 45-day picture is structurally fragile. Net-net: **boring and
mean-reverting through May 22, then directional-fragile with a known binary
event around June 18**. Term skew at 25Δ reads COMPLACENT (skew ratio 0.974)
while tail wings are panicked — classic pre-event setup.

## Key signals

- **June 18 2026 expiry IV = 143.0%** vs ~75–78% for surrounding monthlies — a true **binary-event IV cluster** [STRUCT:iv_term_structure]
- **45-DTE Zero Gamma Level = $174.79**, spot $165.76 — short-gamma regime (-9 points below flip) [STRUCT:gex]
- **Today's (May 22) ZGL = $169.66**, with positive dealer gamma — intraday MEAN-REVERTING regime [STRUCT:today_gamma_flip]
- **Today's largest GEX wall: $180 strike with +$15.07B GEX (support_wall)** — the magnetic strike through Friday [STRUCT:today_gamma_flip]
- **Net DEX = +$230B** — public net call-long; dealers must BUY underlying as hedge → MECHANICAL BID [STRUCT:dex]
- **Term skew 25Δ at 30 DTE: COMPLACENT (skew_ratio 0.974)** — but phase-1 wing puts at 5–10Δ are panicked (200%+ IV). Tail-panic-with-ATM-calm is the standard pre-event signature.

## Detailed findings

### GEX (per-strike + ZGL)

- **Total absolute GEX (45-DTE):** $26,643,912,302 — institutional-grade depth.
- **Regime tag:** NEGATIVE — "Dealers net short gamma — expect trend acceleration and increased volatility"
- **Zero Gamma Level:** **$174.79**
- **Spot:** $165.76 → spot is **5.5% BELOW ZGL** → confirmed short-gamma regime.

Per-strike GEX (excerpt, all strikes ≤ $97 — i.e. OTM puts dominate this region; all NEGATIVE GEX):

| Strike | Net GEX | Note |
|---:|---:|---|
| 8 | -29,166 | Wing tail |
| 31 | **-331,417** | Phase-1 IV outlier strike (June 18 expiry) |
| 32 | -385,211 | June 18 wing |
| 33 | **-803,777** | LARGEST per-strike GEX in the negative wing |
| 34 | -367,100 | June 18 wing |
| 40 | **-838,719** | Second largest negative cluster |
| 48 | -203,182 |  |
| 49 | -287,600 |  |
| 50 | -182,716 |  |
| 77 | -114,573 |  |
| 90 | -449,728 |  |
| 95 | **-856,041** | Largest single-strike negative GEX of the chain |

Read: The negative-GEX mass is concentrated **far below spot at the $31–$50 and $90–$95 strikes** — exactly the strikes phase-1 flagged as IV outliers. These are the **catastrophe-tail puts**. Dealers are SHORT these puts (because retail/inst bought them), so as spot moves toward them, dealers must SELL the underlying to remain delta-hedged. This is the mechanical "trend-amplifies-down" tail behavior.

There is **no positive GEX cluster reported in the per-strike list** for strikes ≤ $97 (all returned strikes are negative). The positive GEX must therefore live at strikes ABOVE spot ($170, $180, $190 calls — confirmed by `today_gamma_flip` data) — but those weren't paged into the per-strike list returned. The structural picture: positive-gamma call walls ABOVE, negative-gamma put wings BELOW, ZGL straddling the institutional cost-basis ceiling.

### DEX (net dealer delta)

- `call_dex` = **+$424.48B**
- `put_dex` = **-$194.02B**
- `net_dex` = **+$230.46B** (POSITIVE)
- Interpretation per tool: "Public is net call-long → dealers net short calls → dealer hedge is to **BUY underlying**."

Implication: There is a **structural delta bid** under MSTR from dealer hedging — every $1 spot move *up* forces more dealer buying (positive gamma feedback in the call-heavy zone). Every $1 spot move *down* forces dealer SELLING in the short-gamma wings. **The hedge book is asymmetric**: supportive in the short-term, accelerative-on-the-downside in the tail.

### Vanna + charm

- `net_vanna` = **-386,899** (slightly negative)
- `call_vanna` = -1,217,068
- `put_vanna` = +830,169
- `net_charm` = **+750,139,428** (positive)

Interpretation per tool: "Public net vanna negative (call-heavy book). **Falling IV → call delta drops → dealers (short calls) cut long-underlying hedge → SELLING pressure**. Rising IV reverses."

This is the **vol-crush risk after May 22 OPEX**: if 5/22 expires and IV collapses (front-month IV is 93.2%; would crash toward 75% baseline), dealers will *sell* underlying to rebalance the hedge. **The post-OPEX week (May 26-29) carries a mechanical sell flow** unless a positive catalyst sustains IV.

`net_charm` positive supports the OPEX-week pin behavior: as time decays, dealer hedge naturally tightens toward the gamma centers ($170, $180).

### IV term structure

| Expiry | DTE | Avg IV | Note |
|---|---:|---:|---|
| 2026-05-22 | 3 | **93.2%** | OPEX week — typical front-month elevation |
| 2026-05-29 | 10 | 77.1% | Normalizes |
| 2026-06-05 | 17 | 78.3% | Stable |
| 2026-06-12 | 24 | 75.2% | Lowest of the cluster |
| **2026-06-18** | **30** | **143.0%** | **BINARY-EVENT SPIKE — 1.9x neighbors** |
| 2026-06-26 | 37 | 78.7% | Normalizes again |
| 2026-07-17 | 59 | 73.0% | Settled |
| 2026-08-21 | 94 | 78.3% |  |
| 2026-09-18 | 122 | 82.7% |  |
| 2026-10-16 | 150 | 77.7% |  |
| 2026-11-20 | 185 | 79.3% |  |
| 2026-12-18 | 213 | 79.7% |  |
| 2027-01-15 | 241 | 84.6% |  |
| 2028-12-15 | 942 | 85.0% | LEAP baseline |

`structure` label: **BACKWARDATION**. `kink_expiry`: null (no single kink identified, but the June 18 expiry IS a kink at 143% — the tool may have flagged it as part of overall backwardation rather than a discrete kink).

Read: **MSTR has a known binary catalyst at the 2026-06-18 expiry.** Candidates:
- **June FOMC**: typically June 17-18 — the IV cluster strongly suggests this (BTC, MSTR's reference asset, is rate-sensitive).
- **MSTR quarterly earnings**: typically late July/Aug — does NOT match June 18.
- **BTC-specific quarterly expiry**: CME BTC futures monthly settles 4th-last business day; June quarterly is significant.
- Phase-6 (macro) MUST resolve which catalyst this is.

### Term skew (25Δ at 30 DTE)

- `call_25d_iv` = **71.83%**
- `put_25d_iv` = **70.00%**
- `skew` = -0.0184 (NEGATIVE — calls slightly richer than puts)
- `skew_ratio` = **0.974** (PUT IV / CALL IV)
- `interpretation` = **COMPLACENT**

Reading: **At 25Δ (close to ATM), the put side is NOT pricing extra fear.** This contradicts phase-1's wing-put-buying signal but is internally consistent: the panic is in the FAR-OTM tail (5-10Δ wings), not at 25Δ. **Implication**: traders are *not* pricing a near-the-money crash, they ARE pricing a tail blow-up. This is a low-vol-of-vol-but-high-skew-tail regime — the classic "binary event in 30 days" structure.

### Front-end IV ratio

- `near_iv` (9 DTE = 2026-05-29) = 77.14%
- `far_iv` (29 DTE = 2026-06-18) = **143.01%**
- `ratio` = **0.539**
- `regime` = "CONTANGO"

The tool labels this CONTANGO because near IV < far IV; **but** in MSTR's context this is not contango in the conventional sense (back-month >> front-month due to broad uncertainty) — it is **single-expiry catalyst-pricing**: the back-end IV is elevated because of the discrete June 18 event, not because of a smooth term structure. **This is a binary-event signal, not a vol-of-vol regime.**

### Today's gamma flip (May 22 expiry, 3 DTE)

- `today_total_gex` = +$26.61B (POSITIVE for May 22 expiry alone)
- `today_zero_gamma` = **$169.66**
- `atm_flip_strike` = $129 (deep below spot)
- Regime: **POSITIVE — long-gamma intraday → mean-reverting price**

Key walls:

| Strike | GEX ($B) | Role | Comment |
|---:|---:|---|---|
| **$180** | **+15.07** | support_wall | MAGNET — largest GEX node, matches phase-3 OI wall (34,457) |
| $170 | +4.76 | support_wall | Today's hottest new OI strike ($170C +8,654, phase 3) |
| $182.5 | +2.51 | support_wall |  |
| $190 | +2.48 | support_wall | Phase-3 noted 37,952 OI |
| $160 | **-1.79** | resistance_wall | Below-spot dealer-short-gamma — downside acceleration |

Read for the May 22 OPEX week:
- Spot $165.77 is BELOW the day's ZGL ($169.66) and BELOW all four support walls ($170/$180/$182.5/$190).
- **The mechanical magnet is therefore UPSIDE toward $170, then $180**. The $160 resistance wall is a *downside* breakdown level — if spot pierces $160, dealers must sell.
- The $180 strike is the largest single GEX node in the entire chain — it WILL behave as a pin/magnet on Friday's settle if spot is anywhere in the $170–$185 corridor.

## Cross-phase synthesis

The gamma map answers three open questions from earlier phases:

1. **Phase-1 question: "Is dealer positioning net delta or delta-neutral?"** Answer: **Net positive delta from public** (DEX +$230B), so dealer hedge is to *buy* underlying. Dealers are NOT short-delta; they are **short-vol short-gamma** in the wings, with mechanical underlying buying in the call zone.

2. **Phase-2 question: "Is the $174-179 institutional cost-basis a real resistance?"** Answer: **YES — and it is ALSO the 45-DTE ZGL.** Crossing $174.79 mechanically transitions dealers from short-gamma to long-gamma AND clears the dark-pool overhead supply. Single highest-leverage level in the entire workup.

3. **Phase-3 question: "Is the $170C +8,654 OI a naked long-call speculation?"** Answer: It sits **inside the long-gamma OPEX-week corridor**. The $180 call wall caps gains from $170C if held to Friday — so the trade looks like a **directional speculation against a known pin**, betting on a $170→$180 move BY EXPIRATION. Holders of $170C have a 3-day window to capture the move before the pin captures them.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__options_structure_gex` | `{symbol:MSTR, date:2026-05-19, dte-max:45, include-zero-gamma:true}` | Regime NEGATIVE; ZGL $174.79; total |GEX| $26.6B |
| `mcp__uw-pp__options_structure_dex` | `{symbol:MSTR, date:2026-05-19, dte-max:45}` | net_dex +$230B; dealer hedge BUYS underlying |
| `mcp__uw-pp__options_structure_vanna_charm` | `{symbol:MSTR, date:2026-05-19, dte-max:45}` | net_vanna -386k; net_charm +750M |
| `mcp__uw-pp__options_structure_iv_term_structure` | `{symbol:MSTR, date:2026-05-19}` | BACKWARDATION; June 18 IV spike 143% |
| `mcp__uw-pp__options_structure_term_skew` | `{symbol:MSTR, date:2026-05-19, dte-target:30}` | COMPLACENT; 25Δ skew_ratio 0.974 |
| `mcp__uw-pp__options_structure_front_end_iv_ratio` | `{symbol:MSTR, date:2026-05-19, near-dte:7, far-dte:30}` | ratio 0.539; CONTANGO label |
| `mcp__uw-pp__options_structure_today_gamma_flip` | `{symbol:MSTR, date:2026-05-19}` | POSITIVE for 5/22; ZGL $169.66; $180 mega wall |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** **two-regime split.**
  - **Near-term (≤ 3 DTE / May 22 OPEX week):** dealer-long-gamma, MEAN-REVERTING, magnet at $170 / $180.
  - **Medium-term (3 – 30 DTE):** dealer-short-gamma below $174.79, **binary-event IV cluster at June 18 expiry**, downside-fragile.
- **Conviction:** **4.5/5** — the term-structure kink is unmistakable; ZGL placement matches phase-2 supply zone; DEX/GEX numbers are deep enough to be reliable on MSTR.
- **Three structural levels phase-9 must use:**
  1. **$174.79 — 45-DTE Zero Gamma Level** ≈ institutional cost-basis ceiling (phase 2). **The single most important level in the workup.** Above = long-gamma regime + clears overhead supply. Below = short-gamma + buyers-still-underwater regime.
  2. **$169.66 — today's (5/22) Zero Gamma Level** & **$180 mega-wall**. Together these define the OPEX-week corridor [pin window].
  3. **$160 — resistance wall (today's gamma flip)** — downside breakdown trigger. Below $160 + below $163 (phase-2 support) = mechanical acceleration zone.
- **Open questions:**
  - **What is the 2026-06-18 catalyst?** Phase-6 (macro) MUST identify. Strong prior: June FOMC meeting (Jun 17-18 historically).
  - The vanna-charm post-OPEX SELL pressure (-vanna means falling IV → dealer sells) is a specific risk to size around — phase-9 must consider whether to enter BEFORE or AFTER 5/22 settle.
  - Does the historical signal-backtest (phase 5) show that prior MSTR setups with backwardation + tail-put outliers + buy-tier DP buying have a directional resolution?
