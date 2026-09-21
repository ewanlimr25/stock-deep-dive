# Phase 10 — Audit & Confidence Score

**Ticker:** XOM
**As-of date (user request):** 2026-05-20
**Effective data date:** 2026-05-18
**Generated:** 2026-05-19T00:00:00Z
**Audit target:** phase-9-trade-plan.md
**Dominant thesis (from phase 9):** LONG (defined-risk, range-bounded into $165 dealer pin)

## Summary

**Raw score: +29 → Confluence score: 63 / 100 → Recommended bin: 0.65.**
**Phase-9 actual bin: 0.65 — MATCH.**

The run is **internally consistent and ready for action** under the
defined-risk structure phase-9 specified, with two important caveats:
(a) three upstream phases (2 dark pool, 5 historical, 7 insights) actively
contradict the LONG thesis, so the conviction is correctly bounded at 0.65
not higher, and (b) two of four active phase-8 agents (accumulation-hunter
and contrarian-scanner) rejected the LONG framing, meaning the trade must
be entered with the post-OPEX-dip timing discipline phase-9 specified, NOT
chased here at $160.49. Contradictions are documented and have explicit
resolutions baked into phase-9's invalidation rubric and sizing haircut.

## Confluence scorecard

| Phase | Score | Justification (quoted datapoint) |
|-------|-------|----------------------------------|
| 1 — flow | **+** | "Net premium flow +$306,031 [FLOW:top_premium_trades] with paired ask/bid calendar-roll sweeps (Dec'26 150C bid + Mar'27 155C ask, four 400-lot blocks in 3 minutes)." Mildly supports LONG but the paired sweeps are not directional — net positive but tempered. |
| 2 — dark pool | **-** | "**Mega-tier dark-pool buy_ratio 0.049** across 6 trades, $206.6M premium, 5 of 6 prints below NBBO mid [DP:block_stratified]." Stock-side institutional distribution is the strongest single contradiction to a LONG entry at $160.49. |
| 3 — OI | **++** | "**Jun'26 165C +8,150 OI Δ (last 10,036 → 18,186, +81%)** [OI:biggest_increases]; net OI Δ today +34,856 contracts [HIST:oi_trend]." Strongest single bullish signal in the run. |
| 4 — structure | **++** | "**Total net GEX +$23.2B with $9.75B at the $165 strike and $6.66B at $160** [STRUCT:gex], ZGL $55.03 → dealer long-gamma regime mean-reverts spot toward $160-$165." Dealer mechanics directly support the range-bounded LONG. |
| 5 — historical | **-** | "**`bullish_flow` 20-day backtest: 0.0% win rate across 12 signals, avg -3.39%** [HIST:signal_backtest]; 90-day cumulative premium flow -$6.3M net MIXED [HIST:cumulative_premium_flow]." Macro environment for bullish-flow signals is hostile. |
| 6 — macro | **++** | "**Strait of Hormuz closure, 10.5 mmb/d of Middle East production shut in April** [MACRO:Strait_of_Hormuz_2026-04_to_2026-05]; **Energy sector inflow $+9.1M vs Tech outflow -$299.8M today** (300:1 rotation) [MACRO:MarketRegime_2026-05-18]." Clean, large tailwind. |
| 7 — insights | **-** | "**`insights_conviction_matrix` = DISTRIBUTION** (confidence 15.78%, dp buy_ratio 0.342) [INSIGHT:conviction_matrix]; **XOM absent from top-50 bullish `signal_confluence`** [INSIGHT:signal_confluence]." Composite signals tilt against the LONG framing. |
| **8 — agents (-2 net)** | **-** (agent-weight ±2 each) | Vote: 1 LONG (risk-monitor +2), 1 RANGE (sweep-tracker 0, compatible with range-bounded LONG), 2 NEUTRAL (accumulation-hunter -2 "Not accumulation"; contrarian-scanner -2 "Fade rips"), 1 MISSING (earnings-scout 0). Phase-8 net = **-2**. |

**Raw score:** +7 −7 +15 +15 −7 +15 −7 (phases 1-7 = +31) + (−2 phase-8) = **+29**
**Confluence_score:** (29 + 115) / 230 × 100 = **63 / 100**
**Recommended bin (per `rubrics/confluence-scoring.md` 50–64 band):** **0.65**
**Phase-9 actual bin:** **0.65** → **MATCH**

## Contradictions

- **phase-2 (dark pool):** Mega-tier DP `buy_ratio 0.049` means 95% of
  $206.6M in mega-tier prints was sell-classified, with 5 of 6 mega prints
  below NBBO mid (top print $79.7M @ $159.44 vs NBBO mid $160.21). This
  contradicts the LONG entry at $160.49 — institutions are *distributing*
  at the trade's intended entry level. **Suggested resolution: tighten
  invalidation (already done — phase-9 specifies "DISTRIBUTION persists for
  3 consecutive sessions" as a signal-based invalidation trigger).**
  Phase-9 also defers entry to the post-OPEX dip ($157.50), below today's
  distribution zone — this is the right tactical response.

- **phase-5 (historical):** `historical_signal_backtest(bullish_flow, 20d)`
  returned a 0.0% win rate across 12 market-wide signals with avg -3.39%
  20-day forward return. The macro environment for "bullish flow" signals
  is hostile in the last 20 trading days. **Suggested resolution:
  downgrade conviction (already done — phase-9 chose 0.65, not 0.75,
  explicitly citing this backtest as a drag in §"Why this bin").** The
  backtest universe is tech-heavy and XOM-vs-tech is the actual rotation
  axis (phase-6's $9.1M energy in / $299.8M tech out resolves the apparent
  contradiction).

- **phase-7 (insights):** UW's composite `signal_confluence` (bullish,
  min_score=1, top-n=50) returned XOM ABSENT — XOM's composite is below
  the top-50 cutoff, likely scoring 3 of 6 factors (fails `dp_accumulation`
  and `low_iv_cheap_options`). The `conviction_matrix` returned
  DISTRIBUTION (15.78% confidence), and aggregate call_bid 36,074 >
  call_ask 29,426. **Suggested resolution: wait for confirmation (already
  done — phase-9's monitoring checklist explicitly says to "check XOM
  appearance in `signal_confluence` (bullish, min_score=3); if XOM enters
  the top-50, conviction confirms and consider scaling").** Sizing
  haircut from 5% cap to 2.5% final also responds to this contradiction.

- **phase-8 agents (-2 net):** accumulation-hunter (NEUTRAL, "Not
  accumulation — this is hedged profit-taking") and contrarian-scanner
  (NEUTRAL/lean-fade, "Crowd is right on macro, wrong on entry — fade
  rips") both argue against entering LONG at current spot. **Suggested
  resolution: the trade plan ALREADY embeds both objections — entry is
  deferred to $157.50 post-OPEX-dip (lower than both agents' fade
  zones), sizing is halved to 2.5% per risk-monitor's "size half"
  recommendation, and the structure is defined-risk debit + credit spread
  rather than naked long calls.** The contradictions are absorbed by the
  trade construction, not ignored.

## Citation failures

Spot-checked 3 citations from phase-9's thesis paragraph:

1. **`[STRUCT:gex]` → "+$9.75B at the $165 strike":** Opens
   phase-4-structure.md §"Key signals" bullet 2 — "**The $165 strike is the
   single largest gamma magnet at $9.75B net GEX**". Also resolved in the
   §"GEX (DTE ≤ 45)" table, rank 1, "$165 / +$9,749,363,698". **✓ RESOLVED.**

2. **`[OI:biggest_increases]` → "+8,150 OI Δ added today on Jun'26 165C":**
   Opens phase-3-positioning.md §"Key signals" bullet 1 — "**Jun'26 165C:
   +8,150 OI (10,036 → 18,186, +81% in one day).** Volume 12,397 with
   prev_ask 6,293 / prev_bid 5,806 (net +487 ask-favored)." Also resolved
   in §"Largest OI increases" table rank 1. **✓ RESOLVED.**

3. **`[MACRO:Strait_of_Hormuz_2026-04_to_2026-05]` → "Strait of Hormuz
   closure / Iran conflict shutting in 10.5 mmb/d":** Opens
   phase-6-macro.md §"Key signals" bullet 1 — "**Strait of Hormuz
   effectively closed through late May 2026** — Iraq, Saudi Arabia, Kuwait,
   UAE, Qatar, Bahrain shut in 10.5 mmb/d in April combined. Brent $110,
   WTI $103." Also resolved in §"Sector overlay — energy specifics" first
   bullet and the tailwind/headwind table. **✓ RESOLVED.**

All 3 spot-checked citations resolve to actual content in the cited phase
MDs. No citation failures.

## Sanity checks

- [✓] All `phase-*.md` files (phase-0 through phase-9, 10 files) present
      in `/Users/ewan/Development/stock-deep-dive/research/XOM/2026-05-20/`
- [✓] Phase-9 cites ≥3 distinct upstream datapoints (6 cited:
      `[STRUCT:gex]`, `[OI:biggest_increases]`,
      `[MACRO:Strait_of_Hormuz_2026-04_to_2026-05]`,
      `[DP:block_stratified]`, `[MACRO:MarketRegime_2026-05-18]`,
      `[AGENT:risk-monitor]`)
- [✓] Phase-9 conviction bin is **0.65** (one of {0.55, 0.65, 0.75, 0.85,
      0.95})
- [✓] Phase-9 includes ≥1 directional structure (Jun'26 160/170 bull call
      spread) AND ≥1 defined-risk alternative (Jun'26 152.50/145 put credit
      spread)
- [✓] Sizing math fully shown: Kelly inputs (p=0.65, b=1.50, fraction=0.25),
      raw_kelly = 41.67%, suggested = 10.4%, capped at 5.00%, final 2.50%
      with downward-deviation reason explicitly stated
- [✓] Disclaimer line present at top of phase-9
- [✓] Invalidation rubric covers all 3 categories (price / signal / macro)
      with falsifiable triggers
- [✓] Catalyst calendar covers next 30 days
- [✓] Post-trade monitoring checklist has ≥4 items (8 items present)
- [✓] Phase-9 conviction bin (0.65) matches phase-10 recommended bin (0.65)
      — no deviation note required

## Confluence breakdown by axis

| Axis | Contribution | Net |
|------|--------------|-----|
| **Today's tape** (phases 1-2) | +7 (flow) − 7 (DP) | **0** (mixed) |
| **Positioning + dealer** (phases 3-4) | +15 +15 | **+30** (strongest stack) |
| **Historical context** (phase 5) | −7 | **-7** (caution) |
| **Macro + insights** (phases 6-7) | +15 − 7 | **+8** (tailwind tempered by composite) |
| **Multi-agent desk** (phase 8) | −2 | **-2** (mild dissent) |
| **TOTAL** | | **+29** |

The structural backbone (phases 3 + 4) is what carries this thesis. Take
those away and the score collapses to −1 (negative). The trade is therefore
**a structural / dealer-mechanics trade** with macro tailwind support, NOT
a sentiment / momentum / flow trade. Phase-9's chosen Jun'26 expiry and
$160/$170 call spread strike selection align directly with that — same
expiry where the OI sits, same strike clusters where the GEX walls are.

## Final auditor note

The run is **internally consistent and ready for action**. Three phases
contradict the LONG thesis (phase-2 DP distribution, phase-5 historical
backtest, phase-7 insights), but phase-9 absorbed each contradiction with a
specific mitigation: post-OPEX-dip entry (not chasing current spot),
sizing halved from 5% cap to 2.5%, defined-risk debit/credit spreads
instead of naked premium, and explicit signal-based invalidation
triggers. The Strait of Hormuz reopening remains the single largest
unhedged tail risk — phase-9's macro-based invalidation is correct to
specify "close trade on credible reopening headline regardless of price
action." No revision required.

**Run status: PASS. Phase-9 trade blueprint is consistent, falsifiable,
and conviction-appropriate. Confluence score 63/100 = 0.65 bin.**
