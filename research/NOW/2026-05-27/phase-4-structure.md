# Phase 4 — Dealer Structure & Gamma

**Ticker:** NOW
**As-of date:** 2026-05-27
**Generated:** 2026-05-28T12:36:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md

## Summary

Structure is **constructive-but-conditional — a coiled spring needing a spark.**
Spot $102.75 sits **below the Zero-Gamma Level $104.62 → dealers are SHORT gamma**
(trend-amplifying: they buy rallies / sell dips). DEX confirms dealers are **net
short calls (net DEX +$409M public-long) → their hedge is to BUY underlying** — a
mechanical bid under the stock right now. The dominant gamma wall is **$110
(+7.4M)**, converging with phase-1/3's call activity. The catch: **negative net
vanna** means a decline in the elevated IV (rank 63, no catalyst until earnings
7/22) forces dealer *selling*, and the **COMPLACENT skew** (25Δ calls richer than
puts) flags crowded call positioning. Net: clearing $103.30→$104.62 unlocks a
dealer chase toward $110; absent a spark, IV bleed + charm are a slow headwind.

## Key signals

- **ZGL $104.62 vs spot $102.75** → **SHORT-gamma regime** (trend-amplifying below) `[STRUCT:gex]`
- Largest gamma wall **$110 (+7.4M GEX)**, then $105 (+4.8M), $112 (+4.7M), $106 (+3.2M) — upside magnet cluster `[STRUCT:gex]`
- **DEX net +$409M public-long → dealers short calls → BUY-underlying hedge** (supportive bid) `[STRUCT:dex]`
- **Net vanna −3,544 (call-heavy)** → falling IV ⇒ dealer SELLING; IV elevated w/ no catalyst = headwind risk `[STRUCT:vanna_charm]`
- **Skew COMPLACENT** — put 25Δ IV 0.578 < call 25Δ IV 0.637 (ratio 0.907) → crowded-call footprint / low hedging `[STRUCT:term_skew]`

## Detailed findings

### GEX `[STRUCT:gex]`

- `total_gex` +29,526,962; `regime` **NEGATIVE**; `zero_gamma_level` **104.62**; spot **102.75**.
- Spot is **~$1.87 below ZGL** → short-gamma. Trend-amplifying: a push up gets chased, a drop gets sold into. Flipping long-gamma (vol suppression) needs spot > $104.62.
- **Per-strike walls:** $110 **+7.40M** (dominant) · $105 +4.78M · $112 +4.73M · $106 +3.21M · $100 +3.15M · $120 +2.49M · $115 +1.93M · **$90 −1.85M** (only negative wall, puts) · $130 +1.60M · $102 +1.36M.
- Path read: from $102.75 (amplifying) through the $103.30 DP supply (phase-2) to the $104.62 flip, then into the $105/$106/**$110** positive-gamma cluster which magnetizes/caps. **$110 is the convergent upside target** (gamma wall + call OI).

### DEX `[STRUCT:dex]`

| field | value |
|-------|-------|
| call_dex | +$842.2M |
| put_dex | −$433.6M |
| net_dex | **+$408.7M** |
| interpretation | "Public net call-long → dealers net short calls → dealer hedge is to BUY underlying." |

A real, mechanical **buy-side hedge bid** under spot today — corroborates phase-1's call demand and partly offsets phase-2's soft dark pool.

### Vanna + charm `[STRUCT:vanna_charm]`

- `net_vanna` **−3,544** (call-heavy book); `net_charm` +526,762.
- Vanna read: **falling IV → call deltas drop → dealers (short calls) cut their long-underlying hedge → SELLING pressure** (rising IV reverses to buying). With IV rank 63 (84th pctile) and **no earnings until 7/22**, IV mean-reversion lower is the base case → **vanna is a headwind**.
- Charm +ve: OTM call delta decays with time → mild dealer de-hedging (selling) into expiry — standard for a call-heavy book, reinforces the slow-bleed risk absent a catalyst.

### IV term structure & front-end `[STRUCT:iv_term_structure]` `[STRUCT:front_end_iv_ratio]`

- **BACKWARDATION** — near 8DTE IV 0.689 > far 29DTE IV 0.617, ratio **1.117**.
- **Not earnings-driven** (next earnings 7/22, 51 DTE; none just passed). Near-term stress is either macro/event (phase-6 to source) or **0DTE/weekly churn** inflating the front (phase-1 IV outliers were all 5/29). Treat as front-end nervousness, not a clean catalyst signal.

### Term skew `[STRUCT:term_skew]`

- 25Δ put IV **0.578** vs 25Δ call IV **0.637**; skew **−0.059**, ratio 0.907 → **COMPLACENT**.
- Calls richer than puts = the bullish call demand (phase-1) has bid call IV above put IV, and **little downside is being hedged**. Two faces: (a) confirms the bullish positioning footprint; (b) **contrarian flag** — crowded calls + low put protection is the complacency that precedes pullbacks. Hand to phase-7c / contrarian agent.

### Today's gamma flip

Skipped — `today-gamma-flip` is 0DTE intraday-only and this is an after-hours/EOD
as-of run (2026-05-27 snapshot). Not meaningful post-close.

## Tool calls (audit trail)

| Command | Result summary |
|---------|----------------|
| `uw options-structure gex --symbol NOW --dte-max 45` | ZGL 104.62, regime NEGATIVE, wall $110 +7.4M |
| `uw options-structure dex --symbol NOW --dte-max 45` | net +$409M, dealers short calls → buy hedge |
| `uw options-structure vanna-charm --symbol NOW --dte-max 45` | net vanna −3,544 (IV-fall = selling) |
| `uw options-structure iv-term-structure --symbol NOW` | BACKWARDATION |
| `uw options-structure term-skew --symbol NOW --dte-target 30` | COMPLACENT (calls > puts, ratio 0.907) |
| `uw options-structure front-end-iv-ratio --symbol NOW --near-dte 7 --far-dte 30` | ratio 1.117, backwardation |
| `uw options-structure today-gamma-flip` | skipped (0DTE intraday-only, EOD run) |

## Tool errors

None.

## Verdict for downstream

- **Dealer regime:** **SHORT GAMMA / transitional** (spot $102.75, ZGL $104.62 — only ~1.8% below the flip). Trend-amplifying with a supportive dealer buy-hedge bid (short calls).
- **Conviction:** **3/5** — the short-gamma + dealer-short-call setup is a genuine squeeze trigger above $104.62, but negative vanna (IV-bleed selling) + complacent skew are real counterweights, and there's no catalyst until 7/22 to spark it.
- **Three structural levels for phase-9:**
  1. **ZGL $104.62** — gamma flip / squeeze trigger. Above: dealers chase (long-gamma stabilizes higher); below: short-gamma amplifies both ways. **The pivot.**
  2. **$110 gamma wall (+7.4M)** — convergent upside target/magnet & cap (matches phase-1/3 call strikes).
  3. **$90 (−1.85M, only negative wall)** — downside-acceleration zone if support fails (below phase-2's $99.69).
- **Open questions:**
  1. What is the **non-earnings backwardation** sourcing from — a macro/sector event on the near calendar (phase-6), or just 0DTE inflation?
  2. Does the **complacent skew + crowded calls** trip the phase-7c positioning gate / contrarian agent (phase-8)? It is the cleanest contrarian flag in the chain so far.
