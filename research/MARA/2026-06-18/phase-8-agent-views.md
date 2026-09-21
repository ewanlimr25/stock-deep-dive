# Phase 8 — Multi-Agent Analyst Desk

**Ticker:** MARA
**As-of date:** 2026-06-18
**Generated:** 2026-06-19
**Upstream phases cited:** phases 1–7c (all packed into each agent's context)

## Summary

**Unanimous: 4 of 4 agents return RANGE** (earnings-scout skipped — earnings 8/4 is
47 DTE > 30d). Conviction 2 / 3 / 2 / 3 → **average 2.5**. Every agent independently
converges on the same structure: a **gamma-pinned $14 ↔ $14.5 range, capped at
$15/$16, supported at $14.00/$12.00**, with the **26.5% short float as the dominant
*up-tail* risk** (a BTC bounce squeezes through the call walls and hurts any
short-premium structure). No agent sees a chasable directional trade. The desk frame
is the macro-regime frame: **defined-risk, half-size, sell premium into the pin.**

## Agent verdicts table

| Agent | bias | conviction | horizon | one_line_take |
|-------|------|-----------|---------|---------------|
| accumulation-hunter | RANGE | 2 | 1-4w | "Dealer/income plumbing — a buy-write pinned to $14, not quiet accumulation. No standing position built. Fade extremes, don't chase." |
| contrarian-scanner | RANGE | 3 | 1-5d | "The crowd to fade isn't the shorts — it's retail buying cheap calls while smart money writes them; sell that euphoria into the $14 pin, defined-risk under $15." |
| sweep-tracker | RANGE | 2 | 1-5d | "No chasable momentum — the loud '$13M calls' is selling that didn't stick as OI; premium-harvest into a $14–14.5 pin, not a sweep campaign." |
| risk-monitor | RANGE | 3 | 1-4w | "Gamma-pinned range until BTC moves; sell premium small and defined-risk — β 5.35 and 26.5% short float mean both tails are fat, and the up-tail hurts a short." |
| earnings-scout | — | — | — | **MISSING/SKIPPED** — earnings 2026-08-04 (47 DTE) > 30d window |

## Per-agent details

### accumulation-hunter — RANGE, conviction 2, horizon 1-4w
- support **$14.00** (DP band $13.99–14.08 ~$29M; max-pain $14) · resistance **$14.50**
  (overwrite/wall) → **$15.00** (dominant wall, +5.3%)
- invalidation: clean daily close > $15.00 on **rising real-volume + OI build (not
  churn)** flips buy-write→markup; close < $13.83 voids the $14 shelf.
- top_signal: "The 'accumulation' is overwhelmingly a single 1.25M-share block (0.335%
  float) crossed at 21:48 UTC exactly at the $14.22 close on MARA's 6/18 annual-meeting
  day — MOC/index mechanics; strip it and the large tier is only 52.8% buy with the
  block tier net-selling (31.2%)." `[DP:block-stratified]`
- top_risk: 26.49% short float + Street $17.70 → a real-volume break above $14.5/$15
  could ignite a squeeze that overruns the buy-write cap.

### contrarian-scanner — RANGE, conviction 3, horizon 1-5d
- support **$14.00** (VWAP $14.09 / max-pain $14; deeper $12) · resistance **$14.50**
  (short-call cap / peak GEX) → **$15.50** (long leg) / **$16.00** (wall)
- invalidation: BTC breaks $65.2k 50d MA / $66k resistance (rips through walls + igns
  the short squeeze); OR sustained spot close > $15.00.
- top_signal: "Retail-vs-smart-money split — `conviction-matrix` call_ask_volume
  211,500 > call_bid_volume 108,210 (retail buying cheap calls by count) while phase-1
  dollar-weighted flow is net call SELLING −$2.15M — the classic fade-the-retail-
  euphoria signature into a long-gamma pin." `[SENT:retail_vs_inst]`
- top_risk: 26.5% short float is squeeze fuel — a BTC move > $66k could detonate the
  short crowd, blowing through any undefined short-call cap.

### sweep-tracker — RANGE, conviction 2, horizon 1-5d
- support **$14.00** · resistance **$14.50** · invalidation: sustained acceptance
  > $15.50 on rising call-OI (dealers flip short gamma) OR break < $14.00 on expanding
  put-side aggressor flow.
- top_signal: "The day's signature sweep ($14.5C 6/26, 63,005 volume, $2.66M sold)
  lifted OI only **+514 (0.01% of float)** — intraday churn, not a standing short;
  sweep-persistence MIXED, sweep-ratio outside top-15." `[OI:biggest-increases]`
- top_risk: a crowded-short BTC-proxy where long-gamma dealers pin $14–14.5 — a BTC
  pop / squeeze rips through $14.5/$15.5 fast and credit-spread sellers become forced
  buyers above the cap.

### risk-monitor — RANGE, conviction 3, horizon 1-4w
- support **$14.00** (max-pain magnet + DP floor; then $12) · resistance **$14.50**
  (triple-confluence: overwrite + call wall + peak GEX +$36.4M) → **$15.50/$16.00**
- invalidation: BTC clean break of $66k (melt-up through walls via 26.5% short) OR
  break of $65.2k MA toward $60k (β 5.35 risk-off cascade) — either resolves the range.
- top_signal: "`gex-time-series` shows POSITIVE/long-gamma **every session for 30
  days** (`regime_flip_dates: null`, ZGL $5.26 vs spot $14.22) — the pin is
  **structural**, not a one-day artifact; holds absent a BTC catalyst." `[HIST:gex-time-series]`
- top_risk: the whole thesis is **one undiversified BTC bet** (fresh corr MARA/CLSK
  0.818 HIGH, complex 0.72–0.84) levered β 5.35 to a sub-MA BTC — a clean BTC break
  either way overwhelms the local pin; the 26.5% short makes the **up-break the more
  violent tail**.
- Risk notes: fresh `portfolio-correlation` re-confirmed the cluster; **no concurrent
  blueprint** fires the cross-book gate (MARA-only, advisory). Flagged a real **6/17
  FOMC risk-off pulse** (Tech/Comm/Consumer-Cyclical net flow flipped negative one day,
  recovered 6/18) — the complex absorbed the hawkish shock → supports range over cascade.

## Disagreements

**None on bias** — 4/4 RANGE. The only nuance is *which crowd to fade*: contrarian-
scanner sharpens it to **fade retail call euphoria** (not the shorts), while
accumulation-hunter/sweep-tracker frame it as **premium-harvest into the pin** — the
same trade from two angles. No agent dissents toward LONG or SHORT.

## Tool errors

- `MISSING: earnings-scout` — deliberately skipped (earnings 2026-08-04 = 47 DTE,
  beyond the 30-day pre-earnings window per the phase-8 agent table).

## Verdict for downstream phases

- **Plurality bias:** **RANGE — 4 of 4** (unanimous; earnings-scout n/a).
- **Average conviction:** **2.5** across the four non-MISSING agents.
- **Three highest-quality signals across agents:**
  1. The 1.25M DP "accumulation" block is **MOC/index mechanics on annual-meeting day**;
     stripped, the large tier is only 52.8% buy and the block tier *sells* → not
     accumulation `[DP:block-stratified]` (accumulation-hunter).
  2. The dominant $14.5C 6/26 sweep ($2.66M, 63k vol) **lifted OI only +514** → intraday
     churn, not a standing short; the real fade is **retail call euphoria** vs
     smart-money premium-selling `[OI:biggest-increases / SENT:retail_vs_inst]`
     (sweep-tracker + contrarian).
  3. **30d GEX zero regime flips** (ZGL $5.26) → **structural long-gamma pin**; the
     range holds absent a BTC catalyst `[HIST:gex-time-series]` (risk-monitor).
- **Open questions surfaced:**
  - Does the pin hold into **6/26 OPEX**, or does a **BTC break of $65.2k/$66k**
    (either direction) resolve the range first? (all four)
  - Is the **up-tail (26.5% short squeeze through $14.5/$15)** the dominant risk to a
    short-premium structure — i.e. must any bearish/range expression be strictly
    **defined-risk**? (accumulation-hunter, contrarian, risk-monitor — yes.)
