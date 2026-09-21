# Phase 1 — Options Flow

**Ticker:** MSTR
**As-of date:** 2026-05-19 (effective; requested 2026-05-20 — see phase-0-intake.md)
**Generated:** 2026-05-20T00:05:00Z
**Upstream phases cited:** phase-0-intake.md

## Summary

MSTR's tape is **mixed-but-defensive-leaning** on 2026-05-19: the largest single
trades are deep-ITM put buys (synthetic shorts) plus ask-side LEAP call buys at
$135 strike, while traders are simultaneously *selling* near-the-money May/June
puts on the bid (bullish income). Sweep activity is enormous — MSTR has placed
in the top of `hot_chains_sweep_persistence` for **5 consecutive sessions** with
$465.79M cumulative sweep premium — but with `dominant_direction = mixed`.
Wing-of-the-distribution IV outliers (June $31–$49 puts at 2.0–2.5 IV) signal
ongoing tail-hedge buying consistent with binary BTC-reflexivity risk.

## Key signals

- Sweep persistence: **5/5 sessions in top, $465.79M cumulative sweep premium**, direction = mixed [FLOW:hot_chains_sweep_persistence]
- Largest single trade: **$1.329M bid-side put on 2026-05-22 $182.5 strike** (delta −0.88, IV 88.5%) — selling deep ITM puts = bullish/unwind hedge [FLOW:top_premium_trades]
- Largest ask-side put: **$1.165M on 2027-01-15 $180P @ $46.6** (delta −0.44, vega 0.53) — long-vol hedge or synthetic short [FLOW:top_premium_trades]
- Bullish LEAP call buying: **$2.18M ask-side on 2028-12-15 $135C, 228 contracts** [FLOW:options_flow_sweeps]
- Catastrophic-tail IV outliers: **June 18 $31–$49 puts trading 1.9–2.5 IV** on 5,000+ aggregate contracts — classic blow-up insurance [FLOW:iv_outliers]
- Underlying reference price across trades: **~$164.5 – $167.8** (intraday range)

## Detailed findings

### Sweeps (ask vs bid, premium)

Top 8 sweeps by aggregated premium:

| Rank | Expiry | Type | Strike | Side | Premium ($) | Contracts | Avg $ | Read |
|------|--------|------|--------|------|------|-----------|------|------|
| 1 | 2028-12-15 | C | 120 | **bid** | 2,319,123 | 230 | 100.73 | Deep-ITM LEAP calls sold (delta-1 short or unwind) |
| 2 | 2028-12-15 | C | 135 | **ask** | 2,177,165 | 228 | 95.49 | LEAP call BUY (bullish, vega 1.01) |
| 3 | 2026-09-18 | C | 230 | **bid** | 1,993,921 | 1770 | 11.24 | Sept OTM calls SOLD on bid (call-overwrite or bearish) |
| 4 | 2028-12-15 | C | 120 | mid | 1,710,200 | 170 | 100.60 | Pair to #1 — likely diagonal/roll |
| 5 | 2028-12-15 | C | 135 | mid | 1,696,340 | 178 | 95.30 | Pair to #2 |
| 6 | 2026-10-16 | C | 245 | **ask** | 1,434,833 | 1215 | 11.94 | October OTM call BUY (bullish vega) |
| 7 | 2026-08-21 | P | 400 | **ask** | 1,401,990 | 60 | 233.66 | Deep-ITM put BUY ≈ **synthetic short** |
| 8 | 2028-12-15 | C | 275 | **bid** | 1,394,292 | 225 | 61.34 | OTM LEAP calls SOLD (bearish or premium harvest) |

Read: the $120/$135 LEAP pair (#1+#2) looks like a $120↔$135 *diagonal up-roll* — selling deep-ITM 120s, buying 135s — which is a *moderately* bullish/delta-trim hedge restructure, NOT a directional new bull bet. Combined with the bid-side $230 Sept calls and $275 LEAP calls being sold, the call-side flow looks more like **monetizing existing long calls** than fresh bullish initiation. The ask-side $245 Oct call sweep ($1.43M, 1,215 contracts) is the cleanest bullish print of the day.

### New positioning (unusual vol, vol/OI)

| Strike / Type | Expiry | Vol/OI | Volume | OI | Premium | Side cue |
|---------------|--------|--------|--------|-----|---------|----------|
| 192.5 C | 2026-06-18 | 108 | 324 | 3 | $155k | New OTM call positions |
| 80 P | 2027-09-17 | 18.5 | 500 | 27 | $625k | New long-dated **bearish tail hedge** |
| **245 C** | 2026-10-16 | 16.3 | 2,002 | 123 | **$2,362,035** | Largest new bullish call position [FLOW:unusual_volume] |
| 152.5 P | 2026-06-18 | 16.2 | 243 | 15 | $169k | OTM put open |
| 167.5 P | 2026-06-26 | 13.8 | 124 | 9 | $189k | ATM put open |
| 240 P | 2026-10-16 | 5.4 | 103 | 19 | $870k | Deep-ITM put = **synthetic short** |
| 240 C | 2026-10-16 | 3.2 | 573 | 180 | $721k | Companion bullish call |

Read: $245C and $240C October opening are the structural new-bull positions ($3.1M combined). They are partially offset by the $240P October synthetic-short ($870k). Net delta exposure on Oct 2026 wing is positive but the dispersion suggests **vol-trading / dispersion** more than pure direction.

### Largest premium prints (table)

Top 5 in dollar terms (all printed during 2026-05-19 RTH):

| Time (UTC) | Type | Strike | Expiry | Side | Premium ($) | Delta | IV |
|-----------:|------|-------:|--------|------|------------:|------:|-----:|
| 15:50:53 | P | 182.5 | 2026-05-22 | bid | 1,329,475 | -0.881 | 88.5% |
| 13:43:24 | P | 250 | 2028-06-16 | bid | 1,234,000 | -0.480 | 66.0% |
| 15:36:42 | P | 180 | 2027-01-15 | **ask** | 1,165,000 | -0.441 | 71.0% |
| 13:43:24 | P | 250 | 2027-01-15 | **ask** | 984,000 | -0.680 | 67.8% |
| 15:51:30 | P | 340 | 2026-06-26 | **ask** | 962,060 | -0.981 | 100.2% |

Read: The two **bid-side** put prints (#1, #2) imply someone *closing or selling* deep-ITM puts — bullish or risk-off-unwind. The three **ask-side** put prints (#3, #4, #5) are mid-delta long puts and one near-delta-1 put (#5) — classic mix of long downside protection and synthetic short. **The ask-side put premium ($3.1M) exceeds the bid-side put premium ($2.56M)**, so on a net basis, the largest-trade tape skews bearish/protective.

### IV outliers + Greeks

- The IV outlier list is dominated by **deep OTM June 2026 puts** at strikes $31–$49 with IV **1.9–2.5** and ~5,000 cumulative volume. These are *catastrophic tail* puts (current spot ≈ $165, so $40 strike is ~76% OTM). Buyers paying 200%+ IV on tail puts is a **strong "blow-up insurance"** signature [FLOW:iv_outliers].
- Highest absolute IV in the top-25 sweeps: **2026-06-26 $340P at 100.2% IV** (delta −0.98, vega 0.025) — deep-ITM put used as efficient short delta vehicle (vol payoff minimized intentionally).
- Greeks profile of top premium: heavy **negative delta** concentration (puts dominate). Bullish ask-side delta concentrated only in:
  - 2027-06-17 $165 C ($550k bid — note: BID side, so actually *sold*)
  - 2027-01 $200 C ($817k bid — *sold*)
  - 2028-12 $135/$120 LEAP diagonal — the ONE genuinely long-call new exposure is the $135 LEAP buy.
- 2028-12-15 $275C bought $752k on bid (size 121) — call delta +0.62 — looks like a long LEAP call closing (bid = trader sold to MM).

### Smart money flow (market-wide context)

MSTR did NOT appear in the top 25 bullish or bearish `hot_chains_smart_money_flow` rows. The market-wide tape on 2026-05-19 was dominated by:
- SPY 5/19 expiry zero-DTE balanced flow
- IWM / SPY June puts being **bought aggressively** (broad index-hedging)
- VIX June/Aug $65 calls being SOLD aggressively (net bearish-vol — VIX-call supply)
- HYG and LQD puts/calls — credit-spread hedging at scale
- WULF, POET, BMNR speculative single-name tape

The macro tape on 2026-05-19 thus reads as **broad equity-hedging / vol-supply** — consistent with the MSTR tail-put buying we see. Note: VIX call selling = market believes the spike is contained, *not* a fresh hedging wave. So if MSTR tail puts are part of broader risk-off, they are running ahead of broader risk indicators.

### Sweep persistence (5-session)

Only ticker returned (filtered to MSTR): MSTR — 5 sessions in top, total $465,791,828 sweep premium, **consistency score = 1.0**, `dominant_direction = mixed` [FLOW:sweep_persistence]. This is institutional-grade conviction *on activity*, but the mixed direction means we cannot infer a clean long/short bias from persistence alone.

### Sweep ratio (market-wide)

MSTR contracts did NOT appear in the top 25 sweep-ratio leaders. The screen was dominated by sub-$1 cheap-vol-lottery tickers (BMNR, RGTI, RLMD, IONQ) — these are unrelated to MSTR's thesis, so this tool produced no actionable MSTR-specific signal today.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__options_flow_sweeps` | `{symbol:MSTR, date:2026-05-19, min-premium:100000, top-n:25}` | 25 sweeps, $35M total premium |
| `mcp__uw-pp__options_flow_unusual_volume` | `{symbol:MSTR, date:2026-05-19, min-vol-oi-ratio:3, top-n:25}` | 13 contracts with vol/OI ≥ 3 |
| `mcp__uw-pp__options_flow_top_premium_trades` | `{symbol:MSTR, date:2026-05-19, top-n:25}` | 25 trades, top $1.329M |
| `mcp__uw-pp__options_flow_iv_outliers` | `{symbol:MSTR, date:2026-05-19, top-n:15}` | 15 wing-OTM put outliers |
| `mcp__uw-pp__options_flow_greek_screener` | `{symbol:MSTR, date:2026-05-19, top-n:15, sort-by:premium}` | 15 Greek-tagged trades |
| `mcp__uw-pp__hot_chains_smart_money_flow` | `{date:2026-05-19, direction:bullish, top-n:25, min-volume:500}` | MSTR not in top-25 (market-wide) |
| `mcp__uw-pp__hot_chains_smart_money_flow` | `{date:2026-05-19, direction:bearish, top-n:25, min-volume:500}` | MSTR not in top-25 (market-wide) |
| `mcp__uw-pp__hot_chains_sweep_persistence` | `{symbol:MSTR, days:5, top-n:20}` | 1 hit: MSTR, $465.79M, consistency 1.0, mixed |
| `mcp__uw-pp__hot_chains_sweep_ratio` | `{date:2026-05-19, top-n:25, min-volume:500, min-sweep-ratio:0.3}` | MSTR not in top-25 |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** **mixed with bearish/defensive tilt** — net ask-side put premium > net ask-side call premium; tail-put IV outliers active; bullish print of the day ($245C Oct) is real but smaller than aggregate put-protection spend.
- **Conviction:** 4/5 on the *activity* (5-session sweep persistence is hard to fake); 2/5 on the *direction* (mixed). Net: 3/5.
- **Three things later phases should remember:**
  1. **$465.79M of 5-day sweep premium** with mixed direction — phase-3 (OI) and phase-4 (dealer structure) must determine whether the institutional positioning has *net* delta or is delta-neutral.
  2. The October 2026 expiry is the *new-bull* expression ($245C and $240C with combined $3.08M premium opening) — phase-3 should track this expiry's OI buildup.
  3. **Wing puts ($31–$49 strike June expiry at 200%+ IV)** are being bought in size — this is tail-of-distribution insurance; phase-6 (macro) should check if this aligns with a stress regime.
- **Open questions:**
  - Is the dark-pool tape confirming net accumulation or distribution at $160–$170 spot? (phase 2)
  - Where is the gamma-flip relative to spot? The deep-ITM put buys at $250–$400 strikes are essentially short-delta and dealers must be long them — does dealer positioning lean negative-gamma into a downside break? (phase 4)
  - Is the LEAP diagonal ($120↔$135) coordinated with a known institutional unwind, or is it idiosyncratic? (phase 8 sub-agents)
