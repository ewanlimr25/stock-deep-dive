# Phase 9 — Trade Blueprint

**Ticker:** ELF
**As-of date:** 2026-06-30
**PM voice:** desk PM running an institutional book
**Spot reference:** $74.00 (phase-1-flow.md §whole-tape; screener close)
**Upstream phases cited:** phase-0.5 through phase-8b

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

ELF is a genuine, insider- and OI-confirmed turnaround — 25 consecutive OI-build days
(+127,955) [HIST:oi-trend], insiders flipped to buying (June MSPR +44.1) [FUND:insider-sentiment],
and a $45 Jan-2028 delta-0.85 LEAP bought on the ask ($1.9M) [FLOW:sweeps] — but it has
already run +34.9%/30d into a **long-gamma dealer cap** (ZGL $59.97, gamma walls
$70/$75 bracketing spot, max-pain $59–63 *below* spot) [STRUCT:gex][STRUCT:max-pain]. The
desk (phase-8: 2 LONG-mild / 2 RANGE / 0 SHORT) and the debate (disconfirmed, 0.65/0.65)
[DEBATE:] converge on one trade: **a small, defined-risk dip-buy at $70/$64–65 with a
capped $75–80 target — not a chase of $74.** The edge is real but thin (bullish_flow
backtest 62.5%, n=8) [HIST:signal-backtest] and heavily gated.

## Bias + conviction + horizon

- **Directional bias:** LONG (mild — a range-aware dip-buy; no phase is bearish/short)
- **Conviction (M-01 bin):** **0.55**
- **Time horizon:** 1-4w
- **Why this bin:** phase-10 confluence ≈ 48 (band 30–49) and the phase-8b debate
  disconfirmed the trade (bear residual ≥ bull), which down-shifts the bin to the floor —
  a slight edge, not a conviction long.

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| Primary | **$70** | pullback to the largest gamma strike / DP cluster, holding above-mid (dealers buy dips in long-gamma) | [STRUCT:gex $70 +1.03M] / [DP:price_levels $69.91] |
| Aggressive | **>$75** | decisive daily close back above the $75 call/gamma wall **with fresh OI expansion** (squeeze-through the cap — the 12.7% short is fuel) | [OI:oi-by-strike call_wall_resistance] / [SENT:short_float] |
| Fade (plan B) | **$64–65** | rejection at $75 back toward the shelf, OR a flush into the 5-day institutional shelf that holds — the best-value dip-buy | [DP:price_levels $64–65] |

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Support | **$70**, then **$64–65** shelf | [STRUCT:gex] / [DP:price_levels] |
| Resistance | **$75** (call/gamma wall), then **$80** | [OI:oi-by-strike] / [STRUCT:gex] |
| Gamma flip (ZGL) | **$59.97** (below → short-gamma, trend amplification) | [STRUCT:gex] |
| Largest pin (max-pain) | **$60** (Jul-17) / $61 (Jul-02) — downward gravity; tradeable pin zone is $70–75 | [STRUCT:max-pain] |

*Price-context color (advisory):* the `fz` RSI/52-week read was unavailable this run
(degraded grid, phase-0), but the UW proxy is clear — **+34.9%/30d, still ~51% below the
52-wk high $150.99** [HIST:trend][FUND:metric]: extended near-term → **prefer the $70 /
$64–65 dip entries over chasing $74**. (Narrative only; not in the Kelly `p`.)

## Invalidation

- **Price-based:** two daily closes below **$70** [DP/STRUCT support] → first invalidation
  (tranche 50%); two daily closes below the **$64–65 shelf** [DP:price_levels] → thesis
  broken (exit remaining); intraday break of **ZGL $59.97** with no reclaim → hard stop
  (dealers flip short-gamma → amplified downdraft) [STRUCT:gex].
- **Signal-based:** cumulative premium flow turns **net-bearish 3 consecutive sessions**
  (it is already 90d net-bearish −$9.5M — a resumption confirms distribution)
  [HIST:cumulative-premium-flow]; OR `institutional-accumulation` flips to distribution
  [INSIGHT:institutional-accumulation]; OR `conviction-matrix` flips DIRECTIONAL_LONG →
  HEDGED_LONG [INSIGHT:conviction-matrix].
- **Macro-based:** a **hawkish CPI surprise** (~mid-July) above consensus (Fed dots
  already point to a hike) [MACRO:CPIAUCSL / FOMC]; OR UW `market-regime` flips
  TRANSITIONAL → RISK-OFF [MACRO:MarketRegime]; OR the **July haircare sell-through
  disappoints** / a negative ELF-specific headline (the idiosyncratic catalyst fails)
  [MACRO:ELF_catalyst].
- **Exit rule:** **tranche exit** — 50% on the $70 break, 50% on the $64–65 break; the put
  credit spread → close/roll if $65 is tested.

## Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** p_raw = **0.625** (n=8, source=backtest) → N-cap (n<10) = 0.75
  → **capped p = 0.625** [HIST:signal-backtest]. (Market-wide bullish_flow base rate, not
  ELF-specific; small N.)
- **Kelly inputs:** b = **1.67** (entry $70, target $80, stop $64), fraction = 0.25, cap_pct = 5.
- **Raw Kelly:** 0.40 → ×0.25×100 = **10%** → capped at cap_pct 5%. **Win-rate map ceiling:**
  p 0.625 ∈ [0.50,0.70] → **half = 2.5%** (take the smaller of Kelly-cap and map → 2.5%).
- **Risk gates:**
  - Fundamentals (phase-7b): **CONFIRM** (0 contradictions) → no-op.
  - Sentiment/crowd (phase-7c): **CAUTION** (BALANCED; analyst revisions flattening, rally
    partly short-covering) → **cut one step: 2.5% → starter ~1.25%**.
  - Correlation cluster (phase-6): **none** (ELF only blueprint for the date) → no-op.
  - Sector rotation (phase-6): **neutral** (Consumer Defensive laggard but persistent inflow) → no-op.
  - Debate (phase-8b): bull_residual **0.65** vs bear_residual **0.65** → **disconfirmed →
    down-shift bin (→0.55) AND cut one step: ~1.25% → ~0.6%**.
  - Context (phase-0.5): **GENUINELY_UNUSUAL** → no-op (edge already in p); macro regime
    "half size" reinforces the small footprint.
- **Final size:** **~0.6% of book risk** (a minimal, defined-risk starter). Two gates fired
  (7c CAUTION + 8b disconfirmed) — this is a dip-buy *alert* sized as a token starter, not a
  size-now position.
- **Deviation reason:** none (upward deviation forbidden — two gates fired).

## Option structures

Both use the **Jul-31 expiry (dte 31)** — deliberately **before the 2026-08-05 earnings**
[MACRO:catalyst] to avoid the binary IV crush, and the premium-selling vol regime (VRP
+0.081) [HIST:vrp] favors the credit leg. Front-expiry implied move is **±3.52% / ±$2.61**
[CTX:implied_move]; the Jul-31 one-month expected move is far larger (IV30 ~0.67), so the
$75–78 targets sit inside ~1 monthly sigma.

### Directional (primary)

- **Structure:** call debit spread (bullish, defined risk)
- **Strike(s) / expiry:** **buy $72 call / sell $78 call, 2026-07-31**
- **Debit/credit:** ~$2.0 debit (illustrative)
- **Breakeven:** ~$74.0
- **Max loss:** ~$2.0 (the debit) — this IS the defined risk; size premium ≤ 0.6% of book
- **Why this structure:** straddles the $75 gamma/call wall (the pin magnet) [STRUCT:gex],
  caps at $78 (short of the $80 wall) so it doesn't pay for upside the long-gamma cap
  blocks, and expires pre-earnings to dodge IV crush. *For a patient institutional mirror
  of the smart-money LEAP, the $45 Jan-2028 deep-ITM call [FLOW:sweeps] is the alternative
  — but it is a 1-3m+ book position, not this 1-4w structure.*

### Defined-risk alternative

- **Structure:** put credit spread (bullish-neutral; sells rich premium into the shelf)
- **Strike(s) / expiry:** **sell $65 put / buy $60 put, 2026-07-31**
- **Debit/credit:** ~$1.4 credit (illustrative)
- **Breakeven:** ~$63.6
- **Max loss:** ~$3.6 (width $5 − credit) — size max-loss ≤ 0.6% of book
- **Why:** monetizes "the $64–65 institutional shelf holds" [DP:price_levels] + the
  premium-selling regime (VRP +0.081) [HIST:vrp] + the long-gamma buffer [STRUCT:gex];
  breakeven $63.6 sits just below the shelf, and it profits from the pin/consolidation the
  desk expects rather than requiring a breakout the $75 wall blocks.

## Macro overlay (cite phase-6)

- **Tailwinds:** solid labor (unemployment 4.3%, payrolls +172k) [MACRO:UNRATE/PAYEMS];
  ISM Mfg 54.0 / Services 54.5 (activity expanding) [MACRO:ISM]; Consumer Defensive
  persistent sector INFLOW (persistence 1.0) [MACRO:sector_flow_persistence]; idiosyncratic
  catalyst — rhode +80%, haircare launch, RJ Strong Buy $85 PT [MACRO:ELF_catalyst].
- **Headwinds:** FOMC dots moved UP to 3.8% end-26 — **hike signaled** [MACRO:FOMC];
  hot inflation (headline CPI +4.2%, core PCE +3.4%) [MACRO:CPIAUCSL/PCEPILFE]; regime
  **TRANSITIONAL — half size, defined-risk** [MACRO:MarketRegime]; richly valued sector
  (PEG 2.89) [MACRO:group_valuation].
- **Net:** **mixed / mild headwind** — macro says size down and use defined risk; ELF's
  driver is idiosyncratic, so macro is a backdrop caution, not the thesis.

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|------|-------|------------------|
| Early Jul 2026 | June ISM Mfg/Services + June jobs report | ? |
| ~Mid-Jul 2026 | June CPI release (Fed-relevant) | ? |
| Jul 2026 (ongoing) | Haircare rollout ramp (TikTok Shop → Target) — idiosyncratic soft catalyst | + |
| Late Jul 2026 | Next FOMC meeting (hawkish-leaning) | ? |
| 2026-08-05 | **ELF Q1 FY2027 earnings** (binary; Jul-31 structures expire before it) | ? |

## Post-trade monitoring checklist

- [ ] **OI retention:** does the $75 Aug / $70 line finally *stick* as OI (accumulation
      confirmed) or keep churning (phase-3 `biggest-increases` daily)?
- [ ] **DP flips:** re-check dark-pool large-tier buy_ratio daily — a drop below 0.50
      (distribution) is a signal-invalidation [DP:block-stratified].
- [ ] **GEX/ZGL:** re-run phase-4 GEX daily — a slide of the ZGL toward spot, or spot losing
      $70 toward $60, warns of the short-gamma flip [STRUCT:gex].
- [ ] **Cumulative premium flow:** watch for 3 consecutive net-bearish sessions (already 90d
      net-bearish) [HIST:cumulative-premium-flow].
- [ ] **Short interest / squeeze:** next semi-monthly SI print — a further drop confirms
      covering is spent; a rise = fresh shorts (fade fuel) [SENT:short_float].
- [ ] **Catalyst:** July haircare sell-through headlines + the June CPI print vs consensus.

## Citations summary

1. `[HIST:oi-trend]` OI BUILDING 25 consecutive days, +127,955 net — phase-5-historical.md §OI trend
2. `[STRUCT:gex]` POSITIVE/long-gamma, ZGL $59.97, gamma walls $70 (+1.03M)/$75 (+681k) — phase-4-structure.md §GEX
3. `[HIST:signal-backtest]` bullish_flow win_rate 0.625 (n=8) — phase-5-historical.md §Signal backtest
4. `[FUND:insider-sentiment]` June MSPR +44.1 (insiders buying) — phase-7b-fundamentals.md §Insider signal
5. `[DEBATE:]` disconfirmed, bull 0.65 / bear 0.65 — phase-8b-debate.md §Disconfirmation verdict
