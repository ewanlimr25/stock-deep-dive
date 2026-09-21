# Phase 7 — UW Insights Confluence

**Ticker:** SNOW
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T16:32:00Z
**Upstream phases cited:** phase-0.5-context.md, phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-5-historical.md

## Summary

UW's composite engines are **unanimous and confirm the upstream read: this is a
MIXED, no-directional-edge, rallied-into-earnings setup with a bearish flow
divergence as the one caution flag.** `conviction_matrix` = **MIXED** (DP buy_ratio
0.486, confidence 1.43%) [INSIGHT:conviction_matrix]; `institutional_accumulation` =
**NEUTRAL** (buy/sell 0.94) [INSIGHT:institutional_accumulation]; SNOW is **absent
from the bullish `signal_confluence` top-30 even at min_score=1**
[INSIGHT:signal_confluence] — its high IV, balanced DP, and net-bearish premium fail
the bullish-confluence factors. The standout: `price_vs_flow` flags a **DIVERGENCE —
"price up 31.7% but options flow is bearish (net −$902K)"** [INSIGHT:price_vs_flow],
a leading-reversal yellow flag that SNOW rallied into the print without net-bullish
flow confirmation. Whole-tape directional aggregates (call $34.6M / put $7.6M but
bullish $19.0M / bearish $19.9M, net −$0.9M) match phase-1 exactly. **Baseline for
phase-9: event-driven MIXED, lean defined-risk, treat the long side with caution.**

## Key signals

- **Conviction matrix MIXED** (DP 0.486 balanced; call ask 20,697 / bid 18,378; put
  ask 6,312 / bid 7,875 = puts net sold) [INSIGHT:conviction_matrix].
- **Bullish confluence: SNOW not ranked** (top-30 are low-IV micro-caps with
  dp_accumulation + cheap options — the opposite of SNOW's profile)
  [INSIGHT:signal_confluence].
- **Price-vs-flow DIVERGENCE:** +31.7% price vs net-bearish flow — leading-reversal
  caution into earnings [INSIGHT:price_vs_flow].
- **Institutional NEUTRAL** (buy/sell 0.94, +31.7% 30d, balanced DP) — no
  accumulation despite the rally [INSIGHT:institutional_accumulation].
- **Peer read:** NTAP (data-infra comp, concurrent blueprint) reports 2026-05-28,
  implied move ~10.6%, IV rank 100, P/C 0.178 [INSIGHT:earnings_play] — same-week
  data-infrastructure earnings cohort.

## Detailed findings

### Deep-dive snapshot (whole-tape aggregates)

From `insights_deep_dive` (phase-0.5) + this phase's tools: spot ~$172.2, mcap
$57.2B, IV rank 86.76, total DP premium $151.5M / 881k sh / VWAP $171.89, next
earnings **2026-05-27 postmarket**. **Directional aggregates (whole tape):**
`call_premium` $34.57M vs `put_premium` $7.62M (gross call-skew); **`bullish_premium`
$19.01M vs `bearish_premium` $19.91M → `net_flow` −$0.90M** (net bearish); P/C 0.369.
`implied_move_perc` 0.40% from the screener is **unusable for the event** — use the
phase-4 straddle-derived **±13.3%** (N4). These reconcile exactly with phase-1's
aggregate and phase-0.5's `[CTX:universe_pctile_net_dir 2.3]`.

### Signal confluence [INSIGHT:signal_confluence]

Bullish, min_score=1, top-30 returned — **SNOW absent.** The list is micro/small-caps
(QSI, SKYT, TE, ACHR, F…) whose factors are `bullish_flow + low_pcr + volume_spike +
dp_accumulation + oi_building + low_iv_cheap_options`. SNOW fails most: IV is *high*
not cheap, DP is *balanced* not accumulating, net flow is *bearish*. **UW's own
confluence engine does not rate SNOW as a bullish setup** — strong corroboration of
the no-edge read.

### Conviction matrix [INSIGHT:conviction_matrix]

`scenario` **MIXED**, confidence 1.43%. DP buy_ratio 0.486 (balanced). Options flow:
call ask 20,697 vs bid 18,378 (mild net call-buy), put ask 6,312 vs bid 7,875 (puts
net *sold*). "Balanced dark pool activity — no clear bias." Directly confirms
phases 1–3 (capped/two-sided).

### Price vs flow [INSIGHT:price_vs_flow]

**`divergence` = true.** "Price is up 31.7% but options flow is bearish (net flow
−$902,406)." 30d range $133.02–$181.27, price_start $135.47 → end $178.36.
Interpretation: SNOW rallied hard into earnings but the net options tape did **not**
confirm with bullish premium — a classic leading-reversal / exhaustion caution. Per
the heuristic, pair with phase-4: dealer long-gamma is *pinning* pre-event, so the
divergence won't resolve until the 5/27 catalyst — but it raises the bar for the
long side and increases downside asymmetry on a disappointing print.

### Analyst vs flow [INSIGHT:analyst_vs_flow]

Tool returned the options-flow block only (flow_sentiment **bearish**, net −$902K);
**no analyst consensus** (yahoo 401, consistent with phase-1's note). Wall-Street
consensus to be sourced in phase-7b/7c via Finnhub/WebSearch (pre-5/22 only). So no
analyst-vs-flow agreement read available from this tool.

### Institutional accumulation [INSIGHT:institutional_accumulation]

`signal` **NEUTRAL — balanced dark pool activity.** buy_sell_ratio 0.94 (buy 428k /
sell 453k), 343 trades, VWAP $171.89, price_30d +31.66%. Top level $172.2 ($36.7M /
213k sh). Confirms phase-2: balanced/mechanical, no accumulation footprint behind the
rally.

### Earnings play [INSIGHT:earnings_play]

SNOW not in the top-20 (sorted by IV rank; the list is saturated with IV-rank=100
names and SNOW is 86.76) — but SNOW unambiguously IS an earnings play (5 days out).
Useful cohort read: same-week reporters include **NTAP 5/28 (impl move 10.6%, IVR
100)**, **HPQ 5/27 (0.9%)**, **OKTA 5/28 (0.4%)**, **PANW 6/2 (0.3%)**. NTAP is the
closest comp (data infrastructure) and reports one day after SNOW — a potential
read-through both ways.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `insights_signal_confluence` | bullish, min_score=1, top_n=30 | SNOW absent (not a bullish-confluence name) |
| `insights_conviction_matrix` | symbol=SNOW | MIXED, DP 0.486, conf 1.43% |
| `insights_price_vs_flow` | symbol=SNOW, lookback=30 | DIVERGENCE: +31.7% price vs bearish flow |
| `insights_analyst_vs_flow` | symbol=SNOW | flow bearish; analyst consensus unavailable (yahoo) |
| `insights_institutional_accumulation` | symbol=SNOW | NEUTRAL, buy/sell 0.94 |
| `insights_earnings_play` | days≤14, min_ivr=40 | SNOW below IVR cutoff; NTAP/HPQ/OKTA cohort |

## Tool errors

(none fatal. `analyst_vs_flow` omitted the analyst-consensus block — yahoo
quoteSummary 401, same as phase-1. Sourced elsewhere in 7b/7c.)

## Cross-check vs phases 1–5

| UW insight | Phase agreement? | Notes |
|------------|------------------|-------|
| `signal_confluence` (SNOW absent) | **agrees** phases 0.5/1/5 | not a bullish-confluence name; no edge |
| `conviction_matrix` MIXED | **agrees** phases 1/3 | two-sided; capped 185/200 spread is the only structure |
| `institutional_accumulation` NEUTRAL | **agrees** phase 2 | balanced/mechanical DP, no accumulation |
| `price_vs_flow` DIVERGENCE (bearish) | **adds** caution | new flag: +32% rally without bullish-flow confirmation |
| whole-tape net_flow −$0.9M | **agrees** phases 0.5/1 | matches `[CTX:net_dir 2.3 pctile]` & phase-1 |

No contradictions — the UW composite is internally consistent with the desk read.

## Verdict for downstream phases

- **UW composite bias:** **MIXED / NEUTRAL** with a **bearish price-vs-flow
  divergence** (caution on the long side). No bullish confluence; no accumulation.
- **Conviction:** **4/5 that the setup is genuinely MIXED** (i.e., high confidence
  there is *no* clean directional edge) — the engines unanimously agree.
- **Phase-9 baseline:** treat SNOW as an **event-driven, defined-risk** situation,
  not a directional conviction trade. The only directional structure on the tape is
  the phase-3 capped 185/200 bull call spread; UW does not corroborate it as bullish
  confluence, so size it as a low-conviction, defined-risk event expression — and
  weigh the divergence flag against any naked-long lean. Override this MIXED baseline
  only with specific contrary evidence from phases 7b/7c/8.
- **Open questions:**
  - Do fundamentals justify the +32% run-up into the print, or is it priced for
    perfection (raising miss-asymmetry)? → phase-7b.
  - What is sell-side consensus / recent revisions and short interest into the
    event? → phase-7b/7c (pre-5/22 only).
  - Does the NTAP/data-infra cohort offer a directional read-through? → phase-8.
