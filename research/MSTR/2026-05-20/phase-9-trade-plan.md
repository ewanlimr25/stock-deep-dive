# Phase 9 — Trade Blueprint

**Ticker:** MSTR (Strategy Inc. — MicroStrategy)
**As-of date:** 2026-05-19 (effective; user requested 2026-05-20)
**PM voice:** desk PM running an institutional book
**Spot reference:** $165.76 close ($164.74 last print, $165.78 DEX spot)
([phase-4-structure.md §GEX])
**Upstream phases cited:** phase-1 through phase-8

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (3 sentences)

The June 18 2026 expiry is pricing **143.0% IV vs ~75–78% for neighbouring
monthlies** — a binary-event IV cluster perfectly aligned with the **June
16–17 FOMC meeting + SEP/dot-plot** [STRUCT:iv_term_structure]; this is the
only place real edge exists in MSTR right now. The macro backdrop is
**HEADWIND** — April CPI printed **+3.8% YoY (hottest since May 2023, up
from +3.3%)** on 2026-05-12, killing the dovish-cut narrative going into a
meeting CME FedWatch reads at **65% hold / 33% cut** [MACRO:CPI_2026-04
WebSearch:bls.gov] — while structural risk from Saylor's 2026-05-05
"potential to sell BTC" admission has already compressed MSTR's mNAV
premium and driven a 16% drawdown. The play is a **two-stage trade**:
harvest theta into the 5/22 OPEX pin (call wall at $180 with +$15.07B GEX),
then carry a long-premium bear-put-debit-spread targeting **MSTR $160 → $140
into the 6/18 FOMC expiry**, sized at 0.5× normal because **IBIT/MSTR
correlation = 0.864** makes MSTR one position in a BTC-proxy cluster, not
four [AGENT:risk-monitor].

## Bias + conviction + horizon

- **Directional bias:** **RANGE through 5/22, then SHORT-leaning via long put spread into 6/18 FOMC**
- **Conviction (M-01 bin):** **0.75** (high edge)
- **Time horizon:** **1–4 weeks (5/22 OPEX → 6/18 FOMC expiry)**
- **Why this bin** (one sentence): Phase-10 confluence rubric scores this setup ≈ **75–80** because every phase scores positive for the *event-vol / range-then-event* thesis (phase-4 +15 IV term structure, phase-5 +7 IV cheap + VRP −4.3%, phase-6 +15 macro headwind, phase-7 +15 conviction_matrix MIXED, phase-8 +8 from 4 NEUTRAL agents) — strong but not a slam-dunk because the directional asymmetry (vs vol asymmetry) is genuinely two-sided.

### Conviction deviation

None. 0.75 maps directly to the 65–79 confluence band (see phase 10).

## Entry zones

| Entry type | Price | Trigger condition | Source |
|---|---|---|---|
| **Primary** | **MSTR $163 – $168** (current corridor) | Spot in the $163.30 – $168 zone with no break of $163 floor; intraday confirmation of dealer-long-gamma pin via $170C OI magnet [OI:biggest_increases] | [DP:price_levels] $166.63 cluster $243.6M premium; [STRUCT:today_gamma_flip] ZGL $169.66 |
| **Aggressive** | **$160 – $162 retest** | Tag of $160 resistance_wall with intraday bounce; opens better risk/reward on long-vol leg | [STRUCT:today_gamma_flip] $160 = -$1.79B GEX resistance_wall |
| **Fade (LONG flip)** | **$174.79+ reclaim on volume** | Spot closes > $174.79 with ≥ $50M premium → flips 45-DTE gamma regime POSITIVE and clears $174–$179 institutional supply zone; **cancel bear put spread, switch to long call-spread or short put-spread** | [STRUCT:gex] ZGL $174.79 = [DP:price_levels] $174.55–$178.03 cluster ceiling |

## Levels to watch

| Type | Level | Source |
|---|---|---|
| Primary support / institutional anchor | **$166.63** | [DP:price_levels] $243.6M / 1.46M shares / 40 trades — heaviest 5-session cluster |
| Secondary support | **$163.30 – $164.50** | [DP:largest] extended-hours bid + intraday low band |
| Breakdown trigger | **$160** | [STRUCT:today_gamma_flip] resistance_wall −$1.79B GEX; close below = mechanical-acceleration zone |
| Today's gamma flip (5/22 expiry only) | **$169.66** | [STRUCT:today_gamma_flip] today_zero_gamma |
| Largest pin / call wall | **$180** | [STRUCT:today_gamma_flip] +$15.07B GEX support_wall; [OI:biggest_increases] 34,457 OI |
| Second pin / call wall | **$190** | [OI:biggest_increases] 37,952 OI (largest absolute OI in the chain) |
| 45-DTE Zero Gamma Level / regime gate | **$174.79** | [STRUCT:gex] = [DP:price_levels] $178 institutional cost-basis ceiling — single highest-leverage level |
| Hot OPEX-week strike | **$170** | [OI:biggest_increases] $170C 5/22 +8,654 OI (now 9,457) — day's hottest new position |
| Put wall (downside cap) | **$150** | [OI:biggest_increases] $150P 5/22 +2,196 OI (now 6,545) |

## Invalidation

- **Price-based:**
  - **Two daily closes below $160** (loss of 5/22 resistance_wall + below phase-2 $163 floor) → **HARD STOP both legs**. Mechanical-acceleration zone confirmed.
  - **Single daily close above $174.79 on > $50M premium** (45-DTE ZGL reclaim) → **CLOSE the bear put spread, flip thesis bullish**. Dealer regime mechanically flips to long-gamma.
- **Signal-based:**
  - **`oi_smart_positioning` direction-count flips to ≥ 60% bearish** (currently 12 bullish / 8 bearish per [OI:smart_positioning]) → tighten stop on bear put to "any 2-session bounce." This would mean the speculative bull lean has unwound.
  - **`historical_cumulative_premium_flow` runs net-bullish for 3 consecutive sessions** (currently mixed, slight +$215M over 90d, [HIST:cumulative_premium_flow]) → take profit on bear put spread regardless of price.
  - **Block-tier DP buy_ratio falls below 0.50** ([DP:block_stratified] currently 0.754) → close iron condor at break-even, hold bear put spread but tighten stop.
- **Macro-based:**
  - **Strategy / Saylor announces actual BTC SALES** before 6/18 → -20% MSTR gap risk; **EXIT both legs immediately at open**, do not negotiate. ([MACRO:MSTR_news_2026-05-05])
  - **June 16-17 FOMC delivers a 25bp CUT + dovish guidance** → bear put spread expires worthless; **plan for this scenario by exiting bear leg at intrinsic−$1 the morning of 6/17** before FOMC if no further weakness has materialized.
  - **May CPI on 2026-06-11 prints +4.0% YoY or worse** → ADD 25% to bear put spread size (still within cap).

**Exit on invalidation:** Hard stops on directional debit; iron condor → close at $0.50 over net credit if breached either wing (defined max loss already small).

## Sizing (% of risk, NOT dollars)

**Risk-monitor explicit cap from phase-8: 0.5× normal sizing + IBIT/MSTR correlation 0.864.**

For the **primary directional structure (bear put debit spread, see below)**:

- p (conviction bin) = **0.75**
- Entry debit (estimated) = ~**$6.00** per spread
- Stop = full debit loss = $6.00
- Target = max profit $14.00 (width $20 − debit $6)
- b (payoff ratio) = |target − entry| / |entry − stop| = $14 / $6 = **2.33**
- raw_kelly = (0.75 × 2.33 − 0.25) / 2.33 = (1.7475 − 0.25) / 2.33 = **64.27%**
- × fraction 0.25 = **16.07%**
- Cap at cap_pct = 5% → **5.0%**
- **Apply risk-monitor 0.5× cluster correlation haircut** → **2.5%**
- **Final size: 2.5% of book risk** (net debit ≤ 2.5% of book).

For the **defined-risk iron condor on 5/22 (see below)**:

- p = 0.75
- Net credit estimate = $2.00; max loss = $3.00 per wing
- b = $2 / $3 = **0.67**
- raw_kelly = (0.75 × 0.67 − 0.25) / 0.67 = (0.5025 − 0.25) / 0.67 = **37.69%**
- × fraction 0.25 = **9.42%**
- Cap at 5% → **5.0%**
- 0.5× correlation haircut → **2.5%**
- **Final size: 2.5% of book risk** (max loss ≤ 2.5% of book).

**Combined max book risk: ≤ 5.0%** if both legs held simultaneously.

## Option structures

### Directional (primary) — MSTR Jun 18 2026 $160/$140 BEAR PUT DEBIT SPREAD

- **Structure:** Long 1× MSTR 2026-06-18 $160 Put **/** Short 1× MSTR 2026-06-18 $140 Put
- **Strikes:** 160 / 140 (width $20)
- **Expiry:** 2026-06-18 (target the FOMC binary expiry, capture 143% IV [STRUCT:iv_term_structure])
- **Debit (estimated):** ~$6.00 per spread (160P leg ~$15, 140P leg ~$9)
- **Breakeven at expiry:** $160 − $6 = **$154**
- **Max profit at expiry:** $20 − $6 = **$14** (if MSTR < $140 at 6/18 close)
- **Max loss:** $6 (full debit)
- **Why this structure:** IV30 at 33rd percentile and VRP −4.34% [HIST:iv_percentile_zscore, HIST:vrp] favor LONG-premium structures; the 6/18 expiry holds the entire 143% IV cluster but the wing-OTM puts at $140 still trade rich enough to materially cheapen the spread (CASE: net debit ≈ 30% of width = good vertical pricing). Long $160P aligns with $160 resistance_wall break-trigger [STRUCT:today_gamma_flip]; short $140P caps risk below phase-3's $147P/$150P put-buying wall and well below the $150P put-build floor [OI:biggest_increases].

### Defined-risk alternative — MSTR May 22 2026 $155/$160/$180/$185 IRON CONDOR

- **Structure:** Short 1× MSTR 2026-05-22 $160 Put **/** Long 1× MSTR 2026-05-22 $155 Put **AND** Short 1× MSTR 2026-05-22 $180 Call **/** Long 1× MSTR 2026-05-22 $185 Call
- **Strikes:** 155 / 160 / 180 / 185 (each wing width $5)
- **Expiry:** 2026-05-22 (3 DTE — the gamma-pin OPEX week)
- **Credit (estimated):** ~$2.00 per condor (put wing $1.00 credit, call wing $1.00 credit)
- **Breakeven (expiry):** $158 to $182 (credit-adjusted body)
- **Max profit:** $2.00 (if MSTR closes between $160 and $180 at 5/22)
- **Max loss:** $5 − $2 = **$3.00 per wing breached**
- **Why this structure:** Today's (5/22) gamma surface is POSITIVE with the **$180 strike as the largest GEX node in the entire chain (+$15.07B)** [STRUCT:today_gamma_flip] and the $170/$180 call walls anchoring upside, $160 anchoring downside [OI:biggest_increases]. Phase-3 shows **no OPEX pin score** for MSTR [OI:pin_risk] *but* the OI dispersion across $165–$190 creates a soft pin in the $170–$180 corridor that the iron-condor body monetizes. Phase-1 sweep persistence is MIXED — high churn but no clean directional lean [FLOW:sweep_persistence] — exactly the condition where defined-range theta harvest wins. **NOTE:** This trade carries vanna-charm SELL pressure risk the week of 5/26 [STRUCT:vanna_charm], but exits at 5/22 expiry, so that risk doesn't apply to this structure.

## Macro overlay

### Tailwinds (limited)

- Technology-sector options inflow **+$44M today** in UW regime read [MACRO:MarketRegime_2026-05-19 UW]
- BTC ETF inflows **~$700M weekly**, cumulative $56.5B since inception [MACRO:BTC_ETF_2026-05 WebSearch:intellectia.ai]
- MSTR's **843,738 BTC holdings at avg cost $66,384** are ~21% above breakeven vs current BTC $80k [MACRO:MSTR_holdings_2026-05-18 WebSearch:bitbo.io]
- SPY still in UPTREND vs 20-SMA and 50-SMA (−2.11% from 90d high) [MACRO:SPY_trend UW]

### Headwinds (dominant)

- **April CPI +3.8% YoY** (up from +3.3%, hottest since May 2023) [MACRO:CPI_2026-04 WebSearch:bls.gov]
- **Core CPI +2.8% YoY** — well above Fed 2% target [MACRO:CPI_2026-04 WebSearch:bls.gov]
- **June FOMC: 65% hold / 33% cut** per CME FedWatch — hawkish-hold risk priced [MACRO:FOMC_2026-06-17 WebSearch:cmegroup.com]
- **Market regime TRANSITIONAL — "reduce position size, wait for clarity"** [MACRO:MarketRegime_2026-05-19 UW]
- **SPY 9 of last 10 days bearish-flow**; market breadth 34.7% bullish [MACRO:SPY_trend UW]
- **Saylor's 2026-05-05 sell-admission** — structural mNAV premium compression [MACRO:MSTR_news_2026-05-05 WebSearch:strategy.com]
- **Strategy Q1 2026 loss −$12.5B + debt-wall watch** [MACRO:MSTR_news_2026-05-05 WebSearch:beincrypto.com]
- **Energy CPI component +17.9% YoY** on Middle East geopolitical risk → broader risk-off [MACRO:CPI_2026-04 WebSearch:bls.gov]

### Net: **HEADWIND** (8 headwind, 4 tailwind, 4 binary/neutral; 65% probability of June hold = binary lean hawkish).

## Catalyst calendar (next 30 days)

| Date | Event | Impact direction |
|---|---|---|
| 2026-05-22 (Fri) | **MSTR monthly OPEX** (front-month IV 93.2%) | + (mean-revert pin; iron condor wins if stays in $160-$180) |
| 2026-05-26 (Tue) | Memorial Day; post-OPEX session | − (vanna-charm SELL pressure risk per [STRUCT:vanna_charm]) |
| 2026-05-29 (Fri) | Weekly expiry | minor |
| 2026-06-05 (Fri) | Weekly expiry + NFP probable | binary (NFP could shift cut odds) |
| 2026-06-11 (Thu)* | **May CPI release** (est) | **HIGH** (sets FOMC tone; print > +4.0% YoY = strong bear put spread tailwind) |
| **2026-06-16/17 (Tue/Wed)** | **FOMC + SEP/dot plot** | **CRITICAL BINARY** (hawkish hold = bear put pays; dovish/cut = bear put expires worthless) |
| **2026-06-18 (Thu)** | **MSTR June monthly OPEX** (IV 143%) | **EXPIRY EVENT** — bear put spread settles |

*Estimated date — typical mid-month BLS release; user/desk to confirm calendar.

## Post-trade monitoring checklist

- [ ] **Daily**: Refresh `mcp__uw-pp__options_structure_gex` for MSTR — flag if ZGL crosses $174.79 in either direction or if total GEX swings > ±25% (regime instability indicator per [HIST:gex_time_series] 8 flips in 28 sessions).
- [ ] **Daily**: Refresh `mcp__uw-pp__dark_pool_block_stratified symbol=MSTR` — exit signal if block-tier buy_ratio drops below 0.50 OR a **mega-tier (≥$10M)** print appears (would change accumulation read).
- [ ] **Daily**: Check `mcp__uw-pp__options_structure_iv_term_structure symbol=MSTR` — if 6/18 IV collapses below 100% without an FOMC event having passed, the binary thesis is being unwound by the market and bear put spread should be trimmed.
- [ ] **Twice-daily**: BTC spot vs $76k support and $80k psychological line; **IBIT** intraday for MSTR-proxy confirmation (correlation 0.864 per [AGENT:risk-monitor]).
- [ ] **News watch**: Strategy / Saylor announcements — any BTC SALE confirmation = immediate exit-at-open both legs (no negotiation).
- [ ] **Macro releases**: May CPI ~2026-06-11; NFP first week of June; FOMC 6/16-17. Add structured size on hot CPI confirmation, halt new size on dovish surprise.
- [ ] **Re-run the skill on 2026-06-12**: a -v2 deep dive after May CPI prints; this re-validates the thesis going into FOMC week.

## Citations summary (M-04 requirement: ≥ 3 distinct upstream datapoints)

1. **[STRUCT:iv_term_structure]** — *MSTR 2026-06-18 expiry avg_iv = 143.0% vs neighbors at 75–78%* — phase-4-structure.md §IV term structure. Drives the entire trade design.
2. **[MACRO:CPI_2026-04 WebSearch:bls.gov]** — *April 2026 headline CPI +3.8% YoY, core +2.8%, released 2026-05-12* — phase-6-macro.md §Inflation. Defines the macro headwind that selects directional lean.
3. **[AGENT:risk-monitor]** — *fresh `risk_portfolio_correlation` pull: IBIT/MSTR 0.864, COIN/MSTR 0.803* — phase-8-agent-views.md §risk-monitor. Drives the 0.5× sizing haircut.
4. **[DP:price_levels]** — *$166.63 5-session cluster $243.6M premium / 1.46M shares / 40 trades* — phase-2-dark-pool.md §Price levels. Defines support anchor and primary entry zone.
5. **[HIST:iv_percentile_zscore] + [HIST:vrp]** — *IV30 33rd percentile / z-score −0.41, VRP −4.34%* — phase-5-historical.md §IV regime. Validates LONG-premium structure choice over short-premium.
6. **[STRUCT:today_gamma_flip]** — *$180 strike = +$15.07B GEX support_wall (largest in chain); $160 = −$1.79B resistance_wall* — phase-4-structure.md §Today's gamma flip. Defines iron-condor wing placement.

— *End phase-9 trade blueprint —*
