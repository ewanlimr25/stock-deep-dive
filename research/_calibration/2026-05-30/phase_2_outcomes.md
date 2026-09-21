# Phase 2 — Outcome Resolution (2026-05-30)

## Path-aware win threshold (verbatim)
> ≥ +1R move in the **bias direction** within the window **without** a −1R drawdown
> first, where R = the blueprint's defined risk (`|entry − stop|`, else
> `max_loss`-implied move, else `0.5 × ATR(14)`). A +2R that came only after a −1.2R
> drawdown is a LOSS. For NEUTRAL/RANGE: WIN if spot stayed inside the structure's
> profit zone through expiry/window end.

## The binding constraint: windows have not elapsed
Latest `uw` data = **2026-05-29**; the corpus spans **2026-05-22 → 05-29**. Forward
trading sessions available (05-25 was Memorial Day, market closed):

| Blueprint date | Fwd sessions through 05-29 |
|---|---|
| 05-22 | 4 (26,27,28,29) |
| 05-26 | 3 (27,28,29) |
| 05-27 | 2 (28,29) |
| 05-28 | 1 (29) |
| 05-29 | 0 |

Required windows: **1-5d = 3D AND 10D**, **1-4w = 10D AND 21D**. **No blueprint has
10 forward sessions**, so the 10D leg — and therefore a clean price-window resolution
— is unavailable for **all 18**. Data is only ~1 trading day older than the youngest
blueprint. `uw historical trend` also returns **close only** (no intraday OHLC), so
even where sessions exist, intra-day MAE cannot be measured; resolution below is
close-based and limited to terminal/decisive conditions.

## Counts
| Outcome | N |
|---|---|
| **WIN** | 0 |
| **LOSS** | 4 |
| **INCONCLUSIVE (window_not_elapsed)** | 14 |

**Resolvable N = 4** (all via terminal conditions, not the price window) — **below the
floor of 8.** Per Step 0.3 the calibration math (Phases 3–6) is aborted; the four are
recorded as a flagged *early read*, not a calibration.

## The 4 decisively-resolved (terminal conditions only — all verified against fresh closes)
| Blueprint | Outcome | Size | Basis |
|---|---|---|---|
| **SNOW/05-22** | **LOSS** | 1.0 | Earnings gap 172→255 (+48%); blew through 195/205 IC call wing AND 149–195 cone; IC + put-debit **expired 05-29** at max loss. |
| **HOOD/05-27** | **LOSS** | 0.5 | Plan's own kill "two daily closes >78" met (84.84, 94.30); 94.30 ≫ 82.5 → bear-call-spread at max loss. |
| **RDDT/05-22** | **LOSS** | 0.0 | Plan's own kill ">147 = bear break voided" met (144.66/**154.19/167.69/176.00**); fade lean ran **+24%** against. VETO'd to size 0. |
| **PDD/05-26** | **LOSS** | 0.0 | Earnings gap **DOWN** 96.58→86.61→**84.44**; 84.44 < 85 long-put strike → put-skewed IC at **max loss** (plan's own "5/27 gap beyond 90/104 = defined max loss" triggered). VETO'd to size 0. |

**Early read (do NOT treat as signal — N=4, and the subset is adversely selected):**
4 LOSS / 0 WIN. **Critical caveat:** RANGE/NEUTRAL premium-selling blueprints only
resolve *this fast* when something violent breaks the range (two earnings gaps —
SNOW, PDD; two sharp trend breaks — HOOD, RDDT). The early-resolving subset is
therefore **structurally biased toward losers**; the 14 INCONCLUSIVE blueprints that
are quietly pinning could well be the winners. Do **not** read "4/4 loss" as "the skill
loses." Two observations that survive the caveat: (1) of the 2 trades that carried
real size, **both lost** (SNOW 1.0, HOOD 0.5); (2) the fundamentals **VETO floored
RDDT and PDD to 0 — and both went on to lose**, i.e. on this tiny sample the VETO
*avoided* losers rather than over-cutting. Re-test at N≥8 / ≥5-fired before acting.

## INCONCLUSIVE (14) — all `window_not_elapsed`
AAPL, BABA, CMPS, ENPH, GFS, KWEB, NOW, NTAP, NVDA/05-27, NVDA/05-29, PATH/05-22,
PATH/05-29, SMH, SNOW/05-29. GFS additionally never triggered its short entry (85.5;
max close 84.5). None had their structure expire or their kill level confirmed within
the elapsed sessions.

## Earliest meaningful re-run (window seasoning)
- **1-5d cohort** (RDDT, SNOW/05-22, PDD, GFS, HOOD, NVDA/05-29) clears its 10D leg
  ≈ **2026-06-05 → 2026-06-12**.
- **1-4w cohort** (12 blueprints) clears 10D ≈ **2026-06-05 → 2026-06-12** and the
  full 21D leg ≈ **2026-06-22 → 2026-06-29**.
- First run that can plausibly clear **N≥8 resolvable: ~2026-06-12**; a full-corpus
  calibration: **late June 2026**.
