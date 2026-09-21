# Phase 1 — Options Flow

**Ticker:** KWEB
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T00:00:00Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md

## Summary

Today's KWEB tape is **call-skewed and bullishly positioned**: net directional
premium +$2.65M with a put/call ratio of just **0.25** by volume, and the largest
new-money prints are **ask-side call buying clustered at the 30–31 strikes** across
Aug/Sep/Dec (spot $26.91 — i.e. bets on a +12–15% move), reinforced by a deep-ITM
**31P block sold on the bid (~$2.08M)** that is bullish/synthetic-long in intent.
**BUT** the 5-day `sweep_persistence` scan labels KWEB **bearish on all 5/5
sessions** ($21.0M total sweep premium, consistency 1.0) — a direct conflict with
today's read that phases 2–3 must adjudicate. Net bias **bullish, moderate
conviction**: the directional skew is genuinely unusual (phase-0.5: 99.1 universe
pctile, 2nd consecutive bullish-skew day into the price low) but on **normal
volume**, **multi-month (slow) tenor**, and against a bearish 5-day sweep label.

## Key signals

- Whole-tape call-skew: call premium **$9.50M** vs put **$6.83M**; bullish
  **$8.35M** vs bearish **$5.70M**; net_flow **+$2.65M**; P/C **0.25** by volume
  `[FLOW:insights_deep_dive]`.
- Upside call accumulation at 30–31: Sep-18 **31C ask ~$917K** (5775+4533 ct, Δ0.28),
  Dec-18 **31C ~$972K** (no_side 4000+4000 ct), Aug-21 **30C ask $762K**
  `[FLOW:top_premium_trades]` `[FLOW:sweeps]`; Dec-18 **30C OI +9,992** (vol 10,391)
  `[FLOW:insights_deep_dive]`.
- Bullish put-selling: Jul-17 **31P (deep ITM, Δ-0.93) sold on the bid, ~$2.08M /
  5,000 ct** `[FLOW:sweeps]` `[FLOW:top_premium_trades]` — collecting downside premium.
- **Conflict flag:** 5-day `sweep_persistence` → KWEB **bearish, 5/5 sessions,
  $21.0M, consistency 1.0** `[FLOW:sweep_persistence]`. Likely a window artifact
  (05-15→05-20 was bearish before 05-21/22 flipped bullish) and/or naive
  put-volume=bearish labeling that ignores bid-side (selling) execution — but
  unresolved here.
- No KWEB rows in the market-wide `smart_money_flow` or `sweep_ratio` top-20/25 →
  consistent with phase-0.5's **normal-volume** read (not a universe-leading chain).

## Detailed findings

### Whole-tape aggregate (read top-N against this) `[FLOW:insights_deep_dive]`

| Field | Value |
|-------|-------|
| call_premium | $9,500,888 |
| put_premium | $6,832,122 |
| bullish_premium | $8,349,064 |
| bearish_premium | $5,702,082 |
| net_flow | **+$2,646,982** (bullish) |
| call_volume / put_volume | 196,609 / 49,267 |
| put_call_ratio | **0.2506** (heavily call-tilted) |
| total_open_interest | 3,902,955 |

The tape is genuinely call-tilted on *both* premium and volume — not a single LEAP
masking a balanced book. This corroborates phase-0.5's 99.1-pctile net-directional
read `[CTX:universe_pctile DUCKDB]`.

### Sweeps (ask vs bid) `[FLOW:sweeps]`

| Contract | Side | Premium | Size | Read |
|----------|------|---------|------|------|
| Jul-17 **31P** | **bid** | $2,075,000 | 5,000 | sell ITM put → bullish/synthetic-long (or closing) |
| Sep-18 **31C** | **ask** | $1,010,453 | 11,355 | buy upside calls → bullish |
| Aug-21 **30C** | **ask** | $762,020 | 8,868 | buy upside calls → bullish |
| Dec-18 31C | no_side | $640,000 | 4,000 | upside calls (auction/mid) → bullish |
| Jun-18 **40P** | ask | $473,600 | 320 | deep-ITM (IV 1.72) → **structural/roll, not directional** |
| Sep-18 36C | **bid** | $317,352 | 11,334 | **sell** far-OTM calls → caps upside / covered |
| Jun-18 35P | ask | $313,600 | 320 | deep-ITM (IV 1.39) → **structural/roll** |
| Jan-15-27 27P | ask | $284,842 | 1,038 | buy ATM put (LEAP) → small downside hedge |

Weight of aggressive flow is **bullish** (buy 30/31 calls + sell 31 puts), with a
minority of upside-capping (sell 36C) and a small ATM put hedge.

### New positioning (unusual vol, vol/OI ≥3) `[FLOW:unusual_volume]`

Predominantly **call openings at 26–30** (Jun-12 30C vol 5,439; Jun-18 27.5C; May-29
27.5C; Jul-17 27C) plus a **2028-01 64C LEAP (vol 900)** — a long-dated upside
lottery. A handful of small near-dated put opens (May-29 25P, Jun-05 26P). Net: new
money opens **calls**, confirming the skew.

### OI build (from `insights_deep_dive` top OI changes) `[FLOW:insights_deep_dive]`

- Dec-18 **30C +9,992** (vol 10,391, avg $2.02) — the largest, bullish, multi-month.
- May-29 28.5C +9,388 · Jun-05 29.5C +7,172 — near-term upside.
- Jul-17 **25P +7,116** (avg $0.41) — the one notable **downside** build (hedge/bear).
- Jul-17 28C +5,819 — upside.

Call OI builds dominate; the lone material put build is the Jul 25P.

### IV outliers + Greeks `[FLOW:iv_outliers]` `[FLOW:greek_screener]`

Only two IV outliers, both **deep-ITM June puts** (40P IV 1.72, 35P IV 1.39) — these
are stale/structural prints (delta-one / roll), **not** genuine vol bets; discount
them directionally. The largest-delta directional print is the Δ-0.93 Jul 31P sold
on the bid (already noted bullish). Real new vol/vega is in the 30–31 calls (Δ0.27–0.36).

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `insights_deep_dive` | symbol=KWEB, date=2026-05-22 | whole-tape: net +$2.65M, P/C 0.25 |
| `options_flow_sweeps` | KWEB, min_prem=100k, top25 | bullish: buy 30/31C, sell 31P |
| `options_flow_unusual_volume` | KWEB, min_vol_oi=3, top25 | call openings at 26–30 |
| `options_flow_top_premium_trades` | KWEB, top25 | 31P bid $830k; Sep/Dec 31C ask |
| `options_flow_iv_outliers` | KWEB, top15 | only 2 deep-ITM June puts (structural) |
| `options_flow_greek_screener` | KWEB, top15, premium | confirms 30/31C directional Δ |
| `hot_chains_smart_money_flow` | bullish, minvol500, top20 | **no KWEB rows** (market-wide) |
| `hot_chains_sweep_persistence` | KWEB, days=5 | **KWEB bearish 5/5, $21.0M, consistency 1.0** |
| `hot_chains_sweep_ratio` | top25, minvol500, ratio0.3 | no KWEB rows; FXI 38C (China) present |

## Tool errors

`hot_chains_sweep_persistence` with `date=2026-05-22` → `Error: unknown flag:
--date`. The tool has no date arg; re-ran without it (scans the latest 5 sessions
ending 2026-05-22, which equals the as-of). Resolved.

## Verdict for downstream phases

- **Bias from this phase:** **bullish** (call-skewed tape; upside accumulation at
  30–31; ITM put selling) — but flagged against a bearish 5-day sweep label.
- **Conviction:** **3/5** — genuine directional skew (phase-0.5 top-1% universe)
  but normal volume, multi-month/slow tenor, and an unresolved bearish sweep-persistence read.
- **Three things later phases must remember:**
  1. **Upside positioning is at 30–31 (Aug/Sep/Dec), +12–15% above spot $26.91** —
     this is a *patient, multi-month* call campaign, not a same-week momentum chase.
  2. **The Jul-17 31P "block" is sold on the BID (bullish), not bought** — do not
     mis-read it as a bearish put buy. Counterweighted by the Jul-17 **25P OI +7,116** (a real downside build).
  3. **`sweep_persistence` says bearish 5/5 sessions ($21.0M)** — phase-2 (dark
     pool) and phase-3 (OI) must adjudicate whether aggressive sweeps are quietly
     bearish under a bullish premium veneer, or whether the label is a window/classification artifact.
- **Open questions:** Is dark pool *accumulating* (confirming the bullish call
  campaign) or *distributing* into the price low? Does dealer GEX/positioning (phase-3/4)
  pin price near 27 or enable the 30–31 target?
