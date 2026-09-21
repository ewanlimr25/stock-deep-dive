# Phase 7 — UW Insights Confluence

**Ticker:** BABA · **As-of:** 2026-07-23 · **Spot:** ~$114
**Generated:** 2026-07-24
**Upstream:** phases 1–6. Reconciles the composite against the hand-built read.

## Summary

UW's composite engine says **MIXED — no clear directional bias.** The **conviction matrix is
MIXED at 2.8% confidence** (*"Balanced dark pool activity — no clear bias"*), **BABA scores below
1 on BOTH the bullish and bearish signal-confluence screens** (no coherent directional stack), and
**institutional accumulation is NEUTRAL** (DP buy/sell ratio 1.12 — balanced). The only directional
tilt is a **marginally bearish options flow** (net −$1.68M, price −1.14% over 30d, **aligned — no
divergence**). Crucially, the flow sub-block confirms the phases 1/3 read that **the call premium is
net SOLD, not bought**: call_bid volume 49,758 > call_ask 36,425 (net call *selling*), matching the
covered-call/overwriting interpretation. The composite baseline for phase-9 is therefore **MIXED
with a slight bearish/range tilt — a defined-risk / range structure, not a strong directional bet** —
which agrees with the phase-6 regime guidance (*iron condors in range*) and the phase-5 range-fade lean.

## Key signals

- **Conviction matrix MIXED (2.8%)** — *"balanced dark pool, no clear bias"* `[INSIGHT:conviction_matrix]`
- **Signal confluence < 1 both directions** — no directional stack for BABA `[INSIGHT:signal_confluence]`
- **Institutional accumulation NEUTRAL** — DP buy/sell 1.12, balanced `[INSIGHT:institutional_accumulation]`
- **Net call SELLING** — call_bid 49,758 > call_ask 36,425 → confirms overwriting `[INSIGHT:conviction_matrix.options_flow]`
- **Price vs flow ALIGNED (no divergence)** — flow bearish, price −1.14%, no reversal signal `[INSIGHT:price_vs_flow]`

## Detailed findings

### Deep-dive snapshot (whole-tape aggregates, reconciled) `[INSIGHT:deep_dive]`

From the phase-0.5/phase-1 `uw_screener` block: call premium **$39.24M** vs put **$26.01M**;
**bullish $23.50M vs bearish $25.18M → net_flow −$1.68M (bearish)**; PCR **0.372**; iv_rank **61.16**;
**implied_move ±1.56% / ~$1.78** (phase-9 N4 sizes to this); total OI 2,036,525. Consistent with
phase-1's aggregate and phase-0.5's `[CTX:]` (universe net-dir pctile 1.5, self 43.7).

### Signal confluence `[INSIGHT:signal_confluence]`

BABA is **absent from both the bullish and bearish screens even at `--min-score 1`** → its directional
confluence score is **< 1** on either side. UW's confluence engine sees **no directional edge** — the
strongest possible statement of "this is a range/mixed name today," not a ≥5 high-conviction stack.

### Conviction matrix `[INSIGHT:conviction_matrix]`

**scenario = MIXED, confidence 2.8%.** Options-flow sub: call_ask 36,425 / **call_bid 49,758** (net
call *selling*), put_ask 14,370 / put_bid 18,620 (net put selling too). Dark-pool sub: buy_ratio
**0.528** (balanced). Explanation: *"Balanced dark pool activity — no clear bias."* The net call
selling is the key corroboration of phases 1/3: the call-heavy premium is **written, not bought** →
range/overwrite, not bullish conviction.

### Price vs flow `[INSIGHT:price_vs_flow]`

**divergence = false** (*"Price and flow are aligned"*). flow_direction **bearish**, price_change
**−1.14%** (115.38 → 114.06 over 30d), net_premium −$1.68M. **No reversal signal** — the mild bearish
flow simply confirms the mild down-drift; nothing to fade contrarian-wise.

### Analyst vs flow `[INSIGHT:analyst_vs_flow]`

Tool returned **only the options-flow side** (flow_sentiment **bearish**, net −$1.68M) — **no analyst
consensus block** for this ADR (yfinance analyst data sparse for BABA). Defer the Street-consensus
read to **phase-7b/7c** (Finnhub + WebSearch). Options-trader signal = bearish; no analyst side to
agree/disagree with here.

### Institutional accumulation `[INSIGHT:institutional_accumulation]`

**signal = NEUTRAL** ("balanced dark pool activity"). buy_side_volume 563,297 vs sell_side 504,218,
**buy/sell ratio 1.12** (mildly more buying), total DP premium $122.0M, 30d price −1.14%. Net: **DP is
balanced-to-slightly-accumulative in aggregate** — this **tempers phase-2's "mild distribution"** read
(which leaned on the block tier + the seller-initiated largest print). Honest reconciliation: **DP is
NEUTRAL/balanced**, with a distributive *block* tier inside an otherwise balanced whole.

### Earnings play

**Skipped** — BABA's next earnings date is **unverified** (phase-6: UW says 2026-09-04, but the June
quarter historically prints mid-August). Running `earnings-play` against an unconfirmed date would be
misleading; phase-7b must pin the date first. If earnings is mid-Aug (~3 weeks), it is in-window and
phase-9 should treat the Aug expiry as event-laden.

## Tool calls (audit)

| Datapoint | Command | jq path |
|-----------|---------|---------|
| scenario | `uw insights conviction-matrix --symbol BABA --date 2026-07-23` | `.{scenario,confidence_pct,options_flow,dark_pool}` |
| divergence | `uw insights price-vs-flow --symbol BABA --lookback-days 30` | `.{divergence,flow_direction,price_change_pct,net_premium_flow}` |
| analyst | `uw insights analyst-vs-flow --symbol BABA` | `.options_flow` (no analyst block) |
| accumulation | `uw insights institutional-accumulation --symbol BABA` | `.{signal,buy_sell_ratio,buy_side_volume,sell_side_volume}` |
| confluence | `uw insights signal-confluence --direction bullish\|bearish --min-score 1 --top-n 50` | `[.results[]\|select(.ticker=="BABA")]` → none |

## Tool errors

None. `analyst-vs-flow` legitimately carries no analyst block for this ADR (not an error — a data
gap; deferred to 7b/7c).

## Cross-check vs phases 1–5

| UW insight | Phase agreement? | Notes |
|------------|------------------|-------|
| signal_confluence (<1 both dirs) | **agrees** with phase-0.5 BUSY_NAME_NORMAL_DAY + phase-1 conviction 2/5 | no directional stack — range name |
| conviction_matrix (MIXED) | **agrees** with phases 1/3/4 | net call selling confirms overwriting; range/capped |
| institutional_accumulation (NEUTRAL) | **tempers** phase-2 (mild distribution) | aggregate DP balanced (1.12); distribution was block-tier-only |
| price_vs_flow (aligned, no divergence) | **agrees** with phase-5 (mild bearish drift, flat price) | no reversal to fade |

## Verdict for downstream

- **UW composite bias: MIXED, slight bearish/range tilt.** No directional confluence; the actionable
  read is **defined-risk / range**, not a strong directional bet.
- **Conviction: 2/5** on any directional thesis (the composite explicitly finds no edge); **3/5** that
  the *right structure is range/defined-risk* rather than directional.
- **Phase-9 baseline:** treat this MIXED/range read as the anchor. Only override toward a directional
  short if phases 7c (positioning) + 8/8b (desk + debate) add specific bearish conviction beyond the
  mild flow tilt. The net-call-selling + short-gamma + adverse-rotation stack supports **fading rallies
  toward $119–120**, not chasing a breakdown.
- **Open questions:** Does phase-7b confirm the fundamental drag (operating loss, AI capex) as a
  *quality* cut, and pin the earnings date? Does phase-7c's short-interest / positioning read add a
  squeeze risk that would penalize a short? Does the desk (phase-8) converge on range-fade or split?
