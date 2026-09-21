# Phase 1 — Options Flow

**Ticker:** MU
**As-of date:** 2026-06-23
**Generated:** 2026-06-23
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md

## Summary

MU's tape is a **two-sided pre-earnings vol book with only a thin net-bearish
aggressor lean** — net_flow = **−$145.2M** (bullish_premium $1.886B − bearish_premium
$2.031B), just ~3.7% of the $3.92B directional premium, with PCR a balanced **1.013**.
Read against that aggregate the *aggressive* tape actually tilts **bullish**: top-25
ask-side call sweeps ($331.6M) outweigh bid-side call sweeps ($255.2M) by +$76.4M,
and the largest structural prints are long-dated **call buying** (1500/950/2220 LEAPs)
plus **put selling** (900/1000/1300) — both bullish-classified. The net-bearish tag is
driven by premium-harvesting (call overwriting into 107% IV) below the top prints,
plus one clear directional hedge: a **$10.2M 1000-strike put bought, expiry 2026-06-26**
(3 days out, straddling tomorrow's postmarket print). **Honest read: MIXED direction;
the dominant signal is the volatility event, not a side.**

## Key signals

- Whole-tape net_flow **−$145.2M** (bull $1.886B − bear $2.031B), PCR **1.013**, but
  call_premium **$2.646B** ≫ put_premium **$1.490B** — heavy call activity, much of it sold `[FLOW:insights_deep_dive]`
- Aggressive sweeps tilt **bullish**: ask calls **$331.6M** vs bid calls **$255.2M** (+$76.4M); puts balanced (ask $174.3M ≈ bid $175.6M) `[FLOW:sweeps]`
- Largest print: **1500c 2027-12-17 ask $30.8M** (Δ0.63 LEAP) — structural long-term bullish bet; 2228 more in 950c/2220c LEAPs `[FLOW:top_premium_trades]`
- Clearest directional/event bet: **1000p 2026-06-26 ask $10.2M** — near-dated put *bought* into the print (the earnings hedge / bearish event lean) `[FLOW:top_premium_trades]`
- MU a top-sweep name **5/5 of last 5 sessions**, $7.81B 5-day sweep premium, but **dominant_direction = "mixed"** — a week-long two-sided build into the catalyst `[FLOW:sweep_persistence]`

## Detailed findings

### Whole-tape aggregate (the truth; top-N read against it) — `[FLOW:insights_deep_dive]`

| Field (`jq` path) | Value |
|---|---|
| `call_premium` | $2,646,549,704 |
| `put_premium` | $1,489,528,173 |
| `bullish_premium` | $1,885,931,042 |
| `bearish_premium` | $2,031,172,720 |
| **derived net_flow** (`bullish_premium − bearish_premium`) | **−$145,241,678** |
| `put_call_ratio` | 1.0130 |
| `call_volume` / `put_volume` | 314,668 / 318,751 |
| `iv_rank` / `iv30d` | 100 / 1.072 (107%) |
| `implied_move` / `implied_move_perc` | 114.72 / **10.91%** |
| `total_open_interest` | 3,285,355 |

The net-bearish lean is thin (≈3.7% of directional premium) and contradicted by the
aggressive sweep tape — it reflects **call overwriting / premium harvesting into 107%
IV**, not a conviction short. Carry-forward from phase-0.5: `unusual_verdict =
GENUINELY_UNUSUAL` (event-driven), so no busy-name confluence cap, but treat direction
as *positioning into a binary*.

### Sweeps (ask vs bid; top-25 each side) — `[FLOW:sweeps]`

| Side | Calls | Puts |
|---|---|---|
| **Ask** (aggressive buy) | $331.6M (16 prints) | $174.3M (9) |
| **Bid** (aggressive sell) | $255.2M (16 prints) | $175.6M (9) |
| **Net (ask−bid)** | **+$76.4M call buying** | **−$1.3M (balanced)** |

Aggressive flow leans bullish on calls, neutral on puts — the opposite tilt to the
whole-tape net, confirming the bearish aggregate is non-sweep (overwriting) flow.
Largest single ask sweep: **1500c 2027-12-17, $97.6M total_size 2535** (a LEAP — slow,
institutional, low short-term tradeability per pitfalls).

### New positioning & largest premium prints — `[FLOW:top_premium_trades]`

| Type | Strike | Expiry | Premium | Side | Read |
|---|---|---|---|---|---|
| call | 1500 | 2027-12-17 | $30.8M | ask | LEAP call buy (bullish, structural) |
| put | 1300 | 2026-07-10 | $18.1M | bid | deep-ITM put sold (Δ−0.72; roll/synthetic-long) |
| call | 1500 | 2027-12-17 | $15.0M | ask | more LEAP call buying |
| put | 900 | 2026-10-16 | $13.7M | bid | OTM put sold (bullish/income, willing buyer −14%) |
| put | 1300 | 2026-07-10 | $12.1M | bid | deep-ITM put sold |
| put | 900 | 2026-12-18 | $10.5M | bid | OTM put sold (bullish) |
| **put** | **1000** | **2026-06-26** | **$10.2M** | **ask** | **near-dated put BOUGHT — the earnings hedge / bearish event bet** |
| call | 950 | 2027-01-15 | $9.4M | ask | ITM LEAP call buy (bullish) |
| call | 950 | 2027-01-15 | $8.4M | ask | more |
| call | 2220 | 2028-12-15 | $8.1M | ask | deep-OTM 2028 lotto call (bullish tail) |
| put | 1000 | 2027-01-15 | $7.1M | bid | LEAP put sold (bullish) |
| put | 900 | 2026-09-18 | $7.0M | bid | OTM put sold (bullish) |

Structural skew of the *named* prints is **bullish** (long-dated call buying + put
selling). The lone clean bearish/hedge directional print is the $10.2M 2026-06-26 1000p.

### IV outliers + Greeks — `[FLOW:iv_outliers]` / `[FLOW:greek_screener]`

- IV outliers are all **deep-OTM 2026-06-26 puts** (the post-earnings Friday) at
  **avg_iv 657% → max 774%** on trivial premium ($1.7k) — the market is pricing a fat
  left tail into the print, but at lotto size (not a directional signal, just tail pricing).
- Greek tape underlying_price = **$1070.68** intraday (vs $1051.77 screener close);
  the 1500c LEAP carries Δ0.63 / vega 4.91 — genuine directional delta, not a pure vol play.

### Smart-money-flow & sweep-ratio

- MU appears in **neither** the bullish nor bearish market-wide smart-money top-10
  (dominated by NFLX/others) — "no smart-money-flow row for MU in top-10 on this date";
  not loosening thresholds per guidance. `[FLOW:smart_money_flow]`
- MU not in the sweep-ratio top-15 (penny-name artifacts); not meaningful. `[FLOW:sweep_ratio]`

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `insights deep-dive --symbol MU --date 2026-06-23` | net_flow=−$145.2M ← `.uw_screener.bullish_premium-.uw_screener.bearish_premium`; PCR 1.013 ← `.uw_screener.put_call_ratio` | whole-tape |
| `options-flow sweeps --side ask --min-premium 100000 --top-n 25` | call $331.6M, put $174.3M ← `.results\|group_by(.option_type)\|map(.total_premium\|add)` | top-25 |
| `options-flow sweeps --side bid …` | call $255.2M, put $175.6M ← same | top-25 |
| `options-flow top-premium-trades --top-n 25` | 1500c $30.8M ask; 1000p 2026-06-26 $10.2M ask ← `.results[].total_premium/.side/.strike/.expiry` | top-25 |
| `options-flow unusual-volume --min-vol-oi-ratio 3 --top-n 25` | 25 new-position rows (vol≫OI) | top-25 |
| `options-flow iv-outliers --top-n 15` | avg_iv 6.57 / max 7.74 on 2026-06-26 puts ← `.results[].avg_iv/.max_iv` | top-15 |
| `options-flow greek-screener --sort-by premium --top-n 15` | 1500c Δ0.633 vega 4.91 ← `.results[0]`; underlying $1070.68 | top-15 |
| `hot-chains smart-money-flow --direction bullish/bearish --top-n 10` | MU absent from both top-10 | market-wide |
| `hot-chains sweep-persistence --days 5 --symbol MU` | 5/5 sessions, $7.81B, dominant_direction "mixed" ← `.results[0]` | 5-day |
| `hot-chains sweep-ratio --top-n 15` | MU absent (penny artifacts) | market-wide |

## Tool errors

- `hot-chains sweep-persistence … --date 2026-06-23` → `Error: unknown flag: --date`.
  This is a **trailing tool** (anchors to latest available date). Re-ran without `--date`;
  `dates_covered` = [2026-06-23 … 2026-06-16], so the anchor IS the as-of date — valid
  and reproducible for this run. (Recorded per `uw-cli-leaves` memory.)

## DATA NOTE / CORRECTION

(none — sweep-persistence re-run was a flag fix, not a value correction; all numbers
round-tripped through `jq` on validated JSON.)

## Verdict for downstream phases

- **Net bias:** **MIXED** (thin bearish net-aggressor −$145.2M / ~3.7%, but aggressive
  sweeps + structural prints lean bullish; the real signal is the **vol event**, not a side).
- **Conviction (directional):** **2/5** — direction is genuinely unresolved; the binary
  earnings event dominates. (Conviction that *this is a major vol event* is 5/5.)
- **Three things later phases must remember:**
  1. Earnings **2026-06-24 postmarket**, implied move **±10.91% (±$114.7)**, IV rank 100 / IV30d 107% — any plan must price the gap and the post-print IV crush.
  2. Flow is two-sided: aggressive call buying + LEAP call buys + put selling (bullish) vs call overwriting + a $10.2M near-dated put hedge (bearish) → net only −$145M. Don't over-read the "#1 bearish" tag as conviction short.
  3. MU = top-sweep name 5/5 sessions, $7.81B 5d, **mixed** — a built-up two-sided positioning book, not a fresh one-directional campaign.
- **Open questions:** Is the dark pool (phase 2) confirming accumulation or distribution under this two-sided tape? Does dealer positioning (phase 3/4) show where the gamma/pin sits for the post-earnings move? These resolve whether the thin bearish lean is hedging (most likely) or genuine.
