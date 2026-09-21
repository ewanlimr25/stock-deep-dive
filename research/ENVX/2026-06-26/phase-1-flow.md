# Phase 1 — Options Flow

**Ticker:** ENVX
**As-of date:** 2026-06-26
**Generated:** 2026-06-27T14:47:39Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md

## Summary

Net bias is **bullish, but narrowly** — the entire directional signal is one coherent
campaign: an **ask-side sweep into the $6 call expiring 2026-10-16** (~112 DTE),
$871,964 premium / 6,738 contracts / 101 trades, lifting offers at ~$1.29 (84.2% of
the $6-strike premium was ask-side; ask:bid = 5.31×; delta ~0.6 → ~404K share-equiv of
upside). The whole tape is decisively call-skewed — call premium $1.81M vs put $0.34M,
PCR 0.198 — but **derived net_flow is only +$441,792** (`bullish_premium $1.12M −
bearish_premium $0.68M`), modest in absolute dollars because $0.68M of bearish premium
comes from bid-side call selling. Persistence is real (5/5 recent sessions in the sweep
top-list) but **mixed direction across the campaign** — today is the cleanly-bullish day.
Read this as a **single-strike directional bet on an ENVX recovery above $6 by October**,
not a broad tape stampede; conviction in the idea, caution on the scale.

## Key signals

- **$6C 2026-10-16 ask-side sweep: $871,964 / 6,738 contracts / 101 trades, avg $1.287**,
  84.2% ask-side `[FLOW:sweeps]` — the position of the day.
- Whole-tape: call $1,814,638 vs put $342,822 premium; **net_flow +$441,792**; PCR 0.198
  `[FLOW:insights_deep_dive]` — call-skewed but modest net dollars.
- Sweep-persistence: `consistency_score 1.0`, `sessions_in_top 5/5`,
  `total_sweep_premium $1,576,720`, **`dominant_direction "mixed"`** `[FLOW:sweep_persistence]`
  — persistent multi-day sweeping, not cleanly one-way until today.
- The $6 Oct call is the single highest-volume contract on the tape (vol 4,958)
  `[FLOW:iv_outliers]`; greek-screener's top-15 by premium are ~14 $6-Oct calls,
  delta ~0.6 / gamma ~0.11 `[FLOW:greek_screener]`.
- ENVX absent from market-wide smart-money-flow top-10 (bullish or bearish) and from
  sweep-ratio top-15 `[FLOW:smart_money_flow, sweep_ratio]` — small name, signal is
  name-specific not universe-leading (consistent with phase-0.5 "outside top-50 by $").

## Detailed findings

### Whole-tape aggregate (read the top-N against this) — `[FLOW:insights_deep_dive]`

| Field | Value |
|-------|-------|
| `call_premium` | $1,814,638 |
| `put_premium` | $342,822 |
| `bullish_premium` | $1,120,154 |
| `bearish_premium` | $678,362 |
| **derived `net_flow` (bull−bear)** | **+$441,792** (bullish) |
| `call_volume` / `put_volume` | 15,394 / 3,043 |
| `put_call_ratio` | 0.1977 (very call-heavy) |
| `iv_rank` | 42.51 · `iv30d` 87.9% |
| `implied_move_perc` | 2.42% |

Read: heavy call *volume/premium* skew, but the **net directional dollars are small**
(+$442K) because a chunk of call flow is bid-side (sold/closed), which UW books as
bearish premium. Phase-0.5 framed this exactly: 95.8th-%ile net-direction but 0.94×
normal *volume* — a directional skew, not a participation surge. Don't over-weight the
raw $1.81M call number.

### Sweeps (ask vs bid) — `[FLOW:sweeps]`

| Side | Strike / Expiry | Premium | Contracts | Trades | Avg px |
|------|-----------------|---------|-----------|--------|--------|
| **ASK** | $6 C 2026-10-16 | **$871,964** | 6,738 | 101 | $1.287 |
| BID | $6 C 2026-10-16 | $164,234 | 1,306 | 20 | $1.261 |

Same strike, same expiry, both sides — but **ask dominates 5.31× / 84.2% of premium**.
Net of the bid-side closing/selling, this is aggressive accumulation of the $6 Oct call.
Delta ~0.6 on the ask leg → ~404,280 share-equivalent of long-delta upside exposure for
~$872K. This is the institutional footprint of the day.

### New positioning (unusual vol, vol/OI ≥ 3) — `[FLOW:unusual_volume]`

| Contract | Vol | OI | vol/OI | Premium |
|----------|-----|----|--------|---------|
| $2.5 C 2026-06-26 (0DTE) | 364 | 16 | 22.75 | $123,250 |
| $2 C 2026-06-26 (0DTE) | 368 | 17 | 21.64 | $142,788 |
| $6 C 2026-07-24 | 108 | 11 | 9.81 | $5,590 |

The two 0DTE prints are **deep-ITM ($2/$2.5 strike vs $5.88 spot) with garbage IV**
(printed implied vol 2,500–8,700%); these are stock-replacement / pin mechanics, **not
directional vol bets — discounted as noise.** Only the $6 Jul-24 call is a genuine new
opening, and it is tiny ($5.6K).

### Largest premium prints — `[FLOW:top_premium_trades]`

Top 25 by premium are dominated by **$6 C 2026-10-16** at sizes 250–500, mostly
ask/mid, IV ~96–105%, delta ~0.60, executed in a tight 19:40–19:55 UTC window — a
single coordinated sweep program. The only non-$6-Oct prints of note: the 0DTE $2/$2.5
deep-ITM calls (noise, above) and one $12 P 2026-08-21 (48 ct, $29K, deep-ITM put,
negligible). No meaningful bearish print.

### IV outliers + Greeks — `[FLOW:iv_outliers, greek_screener]`

IV-outlier list is topped by the noise 0DTE deep-ITM calls (meaningless IV); the only
*size* outlier is **$6 C 2026-10-16, vol 4,958** — the day's biggest contract. Greeks on
the $6 Oct call: delta ~0.60, gamma ~0.11–0.12, vega ~0.0126, IV ~100% — a clean
moderately-OTM directional call (strike $6 vs spot $5.95), not a vol/gamma scalp.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|------------------|--------------------------|-----------|
| `uw insights deep-dive --symbol ENVX --date 2026-06-26 --json` | net_flow=+$441,792 ← `.uw_screener.bullish_premium - .uw_screener.bearish_premium`; PCR 0.198 ← `.uw_screener.put_call_ratio` | whole-tape |
| `uw options-flow sweeps --symbol ENVX --side ask --min-premium 100000 --top-n 25 --date 2026-06-26` | $871,964 / 6,738 ct ← `.results[0].total_premium,.total_size` | 1 |
| `uw options-flow sweeps … --side bid …` | $164,234 / 1,306 ct ← `.results[0]` | 1 |
| `uw options-flow unusual-volume --symbol ENVX --min-vol-oi-ratio 3 --top-n 25 …` | 0DTE $2.5/$2 calls voloi 22.75/21.64 ← `.results[].vol_oi_ratio` | 3 |
| `uw options-flow top-premium-trades --symbol ENVX --top-n 25 …` | top prints all $6 C 2026-10-16 ← `.results[]|sort_by(-.premium)` | 25 |
| `uw options-flow iv-outliers --symbol ENVX --top-n 15 …` | $6 Oct call vol 4,958 ← `.results[]` | 15 |
| `uw options-flow greek-screener --symbol ENVX --top-n 15 --sort-by premium …` | $6 Oct call delta ~0.60 ← `.results[].delta` | 15 |
| `uw hot-chains smart-money-flow --direction bullish/bearish --top-n 10 --min-volume 500 …` | no ENVX rows ← `select(.ticker=="ENVX")` empty | 0 (of 10) |
| `uw hot-chains sweep-persistence --days 5 --top-n 20 --symbol ENVX --json` (no `--date` — trailing tool, anchors latest=2026-06-26) | consistency 1.0, 5/5 sessions, $1,576,720, "mixed" ← `.results[0]` | 1 |
| `uw hot-chains sweep-ratio --top-n 15 --min-volume 500 --min-sweep-ratio 0.3 …` | no ENVX rows | 0 (of 15) |

## Tool errors

- `uw hot-chains sweep-persistence … --date 2026-06-26` → `Error: unknown flag: --date`.
  Re-run without `--date` (trailing-window tool anchors to the latest available date =
  2026-06-26 = our as-of). Value used is from the corrected call.

## DATA NOTE / CORRECTION

- First `jq` on the ask/bid sweeps multiplied a null `avg_iv` and errored; the sweeps
  payload carries no `avg_iv` field (only `avg_price`). Re-read with the correct schema
  (`total_premium`, `total_size`, `trade_count`, `avg_price`) — values above are from the
  corrected read. No number was transcribed from the errored buffer.

## Verdict for downstream phases

- **Net bias:** bullish (single-campaign), **conviction 3/5.** Real ask-side directional
  accumulation, but concentrated in ONE strike/expiry, modest absolute net dollars
  (+$442K), counter-trend (phase-0.5: ENVX −20.67%/month, 26% short float), and the
  multi-day sweep picture is "mixed."
- **Three datapoints later phases must remember:**
  1. **$6 C 2026-10-16 ask-side sweep — $871,964 / 6,738 ct / 84.2% ask / delta-0.6.**
     The whole bull thesis lives or dies on this strike. Phase-3/4 must check OI build
     and dealer gamma at $6.
  2. **net_flow only +$441,792** despite PCR 0.198 — call-skewed but small net dollars;
     don't inflate conviction off the headline call premium.
  3. **Persistence 5/5 sessions but `dominant_direction "mixed"`** — sweepers have been
     active all week but not one-directional; today is the bullish print. Watch whether
     it persists or fades.
- **Open questions:** Is dark pool (phase-2) confirming accumulation under $6, or is the
  $6 call a standalone bet? Is the $6 strike a building OI wall / dealer pin (phase-3/4)?
  Given 26% short float, is this recovery-bet flow or squeeze-positioning (phase-7c/8b)?
