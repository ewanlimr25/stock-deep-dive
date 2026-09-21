# Phase 1 — Options Flow

**Ticker:** MARA
**As-of date:** 2026-06-18
**Generated:** 2026-06-19
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md

## Summary

The headline "$12.9M call premium / PCR 0.13" reads bullish but **inverts on
inspection: the dominant flow is call *selling*, not buying.** Whole-tape net
aggressor flow is **net bearish −$1.61M** (`bullish_premium $5.72M − bearish_premium
$7.32M`), and the single biggest structure of the day is a **short-$14.5C /
long-$15.5C 6/26 call credit spread** executed in size (~$2.5M credit collected on
the short leg, both new OI). There is **no meaningful downside put buying** — the
bearish expression is "capped upside / premium harvest," not a directional short or
crash hedge. Net bias **mildly bearish-to-neutral**; conviction capped per
`[CTX:] = BUSY_NAME_NORMAL_DAY` (phases 1–2 → `+`, not `++`).

## Key signals

- Net aggressor flow **−$1.61M** (net bearish) despite call-heavy *volume*
  (PCR 0.128) — calls being sold, not bought `[FLOW:insights_deep_dive]`.
- **$14.5C 6/26 sold $2.66M** on the bid (63,005 vol / 2,111 OI = **30× vol/OI**,
  new position; ask_bid_ratio 0.03) — the day's signature print `[FLOW:smart-money-flow]`.
- **$15.5C 6/26 bought $1.2M** on the ask (63,413 vol / 4,002 OI = 16×, new) — the
  long leg of the spread `[FLOW:unusual-volume]`.
- Bid call premium **$4.43M** ≫ ask call premium **$2.28M** → net call *selling*
  ≈ −$2.15M `[FLOW:sweeps]`.
- 5-day sweep persistence: **consistency 1.0, 5/5 sessions, direction MIXED**,
  $44.1M premium — busy but **non-directional** `[FLOW:sweep-persistence]`.

## Detailed findings

### Whole-tape aggregate `[FLOW:insights_deep_dive]` (read top-N against this)

| Field | Value |
|-------|-------|
| `call_premium` | $12,926,879 |
| `put_premium` | $2,231,047 |
| `bullish_premium` | $5,715,408 |
| `bearish_premium` | $7,321,224 |
| **derived `net_flow` = bull − bear** | **−$1,605,816 (net bearish)** |
| `call_volume` / `put_volume` | 344,323 / 43,946 |
| `put_call_ratio` | 0.1276 (extreme call-heavy by *volume*) |
| `iv_rank` / `iv30d` | 30.30 / 0.7969 (79.7%) |
| `implied_move_perc` | 0.01456 (~1.46%) |

**The tell:** gross call dominance (volume + premium) coexists with *negative net
aggressor flow*. That only happens when calls are being **written/sold**. The top-N
prints below explain exactly how.

### Sweeps (ask = lift/buy, bid = hit/sell)

- **ASK (buying), 9 prints, all calls, $2.28M:** $15.5C 6/26 $894k (47k ctr, avg
  $0.19), $15C 9/18 $373k, $13C LEAP 6/2027 $220k, $14C 0DTE $161k, scattered 0DTE.
- **BID (selling), 13 prints, $4.43M call + $0.35M put:** **$14.5C 6/26 $2,561,412
  (60,897 ctr)** dominates; then $13C 0DTE $513k, $13C LEAP $336k, $13.5C 0DTE $245k.
  Puts on the bid are tiny ($10.5P 7/24 $110k, $20P 12/18 $112k) = **put writing**.
- **Net call aggressor = ask $2.28M − bid $4.43M = −$2.15M (net call selling).**

### New positioning (unusual volume, vol/OI ≥ 3) — the structure

| Contract | Vol | OI | Vol/OI | Premium | Net side | Role |
|----------|-----|----|----|---------|----------|------|
| **$14.5C 6/26** | 63,005 | 2,111 | **30×** | $2.66M | **SOLD** (bid) | short leg (Δ≈0.40) |
| **$15.5C 6/26** | 63,413 | 4,002 | 16× | $1.20M | **BOUGHT** (ask) | long leg (Δ≈0.21) |
| $10.5P 7/24 | 5,008 | 32 | 157× | $0.11M | SOLD (bid) | put write |
| $6.5C / $7.5C 0DTE | small | — | — | — | mixed | ITM/expiry noise |

Comparable sizes on the two 6/26 legs (~47–61k) → a **bear/neutral call credit
spread** (short $14.5 / long $15.5), net credit, max profit if MARA ≤ $14.5 at 6/26,
defined risk above $15.5. Spot $14.22, so the **short strike sits just +2% OTM** and
the long cap +9%. Plus opportunistic put-writing. Read: **capped-upside, range-bound,
premium-harvest** — not bullish accumulation, not a downside short.

### Largest premium prints `[FLOW:top-premium-trades]`

| Type | Strike | Expiry | Premium | Side |
|------|--------|--------|---------|------|
| call | $14.5 | 6/26 | $630,000 | **bid (sell)** |
| call | $14.5 | 6/26 | $612,950 | **bid (sell)** |
| call | $14.5 | 6/26 | $569,310 | **bid (sell)** |
| call | $13 | 0DTE | $421,464 | bid (Δ0.98, ITM) |
| call | $14.5 | 6/26 | $397,277 | **bid (sell)** |
| call | $15.5 | 6/26 | $285,000 | ask (buy) |
| call | $15.5 | 6/26 | $284,050 | ask (buy) |
| call | $15.5 | 6/26 | $257,545 | mid |

Five of the top eight are $14.5C 6/26 **sells**; the offset is $15.5C 6/26 **buys**.

### IV outliers + Greeks

- IV outliers are **entirely 0DTE (6/18)** contracts with avg_iv 130–630% — pure
  expiry-day gamma noise. **Tagged and discounted**; no directional content.
- Greeks confirm legs: $14.5C 6/26 Δ≈0.39–0.40 / γ≈0.24 (short), $15.5C 6/26 Δ≈0.21
  / γ≈0.17 (long). The 0DTE $13C (Δ0.98) / $6C (Δ0.97) are deep-ITM expiry mechanics.
- `sweep-ratio`: MARA **outside top-15** (leaders IREN, SMCI, NVDA, TSLA…) — its
  sweeps aren't unusually aggressive vs the universe.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|------------------|--------------------------|-----------|
| `insights deep-dive --symbol MARA --date 2026-06-18` | net_flow −1,605,816 ← `.uw_screener.bullish_premium − .bearish_premium`; pcr 0.1276; call/put prem 12.93M/2.23M | whole-tape |
| `options-flow sweeps --side ask --min-premium 100000 --top-n 25` | ask calls $2.28M ← `.results\|group_by(.option_type)` | 9 |
| `options-flow sweeps --side bid --min-premium 100000 --top-n 25` | bid calls $4.43M / puts $0.35M ← same | 13 |
| `options-flow unusual-volume --min-vol-oi-ratio 3 --top-n 25` | $14.5C 30× $2.66M; $15.5C 16× $1.2M ← `.results[]` | 6 |
| `options-flow top-premium-trades --top-n 25` | 5/8 top = $14.5C 6/26 bid ← `.results[].side` | 25 |
| `options-flow iv-outliers --top-n 15` | all 0DTE noise ← `.results[].expiry` | 15 |
| `options-flow greek-screener --top-n 15 --sort-by premium` | $14.5C Δ0.40 / $15.5C Δ0.21 ← `.results[].delta` | 15 |
| `hot-chains smart-money-flow --direction bullish\|bearish --min-volume 500` | MARA $14.5C 6/26 in BEAR list: net_flow −59,288, ask_bid 0.03 ← `select(option_symbol\|startswith("MARA"))` | top-10 ea |
| `hot-chains sweep-persistence --days 5 --symbol MARA` | consistency 1.0, 5/5 sessions, **mixed**, $44.1M ← `.results[]` | 1 |
| `hot-chains sweep-ratio --top-n 15 --min-sweep-ratio 0.3` | MARA outside top-15 ← ticker scan | 15 |

## Tool errors

- `hot-chains sweep-persistence … --date 2026-06-18` → `Error: unknown flag: --date`
  (trailing tool, latest-anchored). **Re-ran without `--date`** (latest = 2026-06-18,
  the as-of) → valid. Recorded per `[[uw-cli-mcp-parity]]` (trailing tools anchor to
  latest, not as-of-parameterized).

## DATA NOTE / CORRECTION

First `jq` on sweeps referenced phantom fields (`vol_oi_ratio`/`open_interest` — not
in the sweeps schema, which is `avg_price, expiry, option_type, side, strike,
total_premium, total_size, trade_count, underlying_symbol`). Re-extracted against the
real keys; no number transcribed from the failed read.

## Verdict for downstream phases

- **Bias from this phase:** mildly **bearish / neutral** (capped-upside; NOT a
  directional short — bearish lean is via call-*selling*, not put-buying).
- **Conviction:** **2/5** — the structure is real and sizeable (~$2.5M credit) but
  it expresses *range-bound/capped upside*, not strong direction; and `[CTX:]` says
  this is a **busy name's normal day** (self-pctile total 58th), so magnitude is
  discounted and confluence is capped at `+`.
- **Three things later phases must remember:**
  1. The "$13M call premium" is **call SELLING** — net_flow **−$1.61M**; the
     defining trade is a **short-$14.5C / long-$15.5C 6/26 credit spread** capping
     upside ~+2% over spot **$14.22**.
  2. **Zero downside put buying** — no crash hedge, no directional short. Low
     bearish conviction; the flow says "won't rip above $14.5 this week."
  3. **$14.5** is the flow-defined upside cap / pin candidate (short-call strike,
     6/26 weekly OPEX). $15.5 is the hard ceiling of the spread.
- **Open questions:**
  - Is the $14.5C selling **covered** (overwriting against held stock → neutral) or
    **naked** (bearish)? → Phase-2 dark pool: are institutions accumulating shares
    underneath (covered-write) or distributing?
  - Does dealer positioning (phase-3 OI walls / phase-4 GEX, max-pain) reinforce
    **$14.5** as a near-term pin into 6/26 OPEX?
