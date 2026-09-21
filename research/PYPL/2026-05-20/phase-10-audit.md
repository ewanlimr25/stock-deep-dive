# Phase 10 — Audit & Confidence Score

**Ticker:** PYPL
**As-of date:** 2026-05-19 (effective); user-requested 2026-05-20
**Generated:** 2026-05-20T01:45:00-04:00
**Phase 9 dominant bias being audited:** **RANGE (with mild LONG kicker), conviction 0.65, horizon 1–5d primary / 1–4w kicker**

## Summary

- **Raw confluence score: +37**
- **Normalized confluence_score: 66 / 100**
- **Recommended conviction bin (per rubric 65–79 band): 0.75**
- **Phase-9 actual bin: 0.65 (one bin BELOW recommendation)** — phase-9
  is **conservatively sized**, which is permitted by the rubric without a
  deviation note (smaller is always allowed). The conservative bin is
  justified by: (a) 1-1-1-1 agent split with mean conviction only 2.75/5
  [AGENT:phase-8], (b) two `-` contradiction phases, (c) TRANSITIONAL
  market regime requires defined-risk + half-size per
  [MACRO:MarketRegime_2026-05-19].
- **Contradictions: 2 phases (phase 5 historical, phase 6 macro)** — both
  attack the LONG-kicker specifically, not the RANGE primary. Phase 9
  has already addressed these via tighter invalidation and downward
  sizing deviation on the kicker.
- **Citation spot-check: 3/3 PASS.**
- **Sanity checks: 6/6 PASS.**
- **Verdict: run is internally consistent; phase 9 is ready for action
  as written.** No revision required.

## Confluence scorecard

| Phase | Score | Justification (quote a datapoint) |
|-------|-------|-----------------------------------|
| 1 — flow | **+** (+7) | "hot_chains_sweep_persistence shows PYPL in top sweep activity 5/5 of last 5 sessions … dominant_direction MIXED, consistency_score 1.0" [FLOW:hot_chains_sweep_persistence] — institutional engagement with mixed direction directly supports a RANGE thesis. |
| 2 — dark pool | **+** (+7) | "Mega-tier (≥$10M) buy_ratio = 1.0 on $29.64M / 2 trades" [DP:dark_pool_block_stratified] — supports the LONG kicker portion but not the RANGE primary; partial alignment only, so `+` not `++`. |
| 3 — OI positioning | **++** (+15) | "PYPL 2026-06-18 $50C OI +1,352 → 23,713, prev bid_vol 2,287 vs ask 725 (3.2:1 bid)" [OI:oi_biggest_increases] — the $50 call wall is the natural profit cap of the call-debit kicker AND informs the IC's call-side strike avoidance; foundational structural data for both structures. |
| 4 — dealer structure | **++** (+15) | "Total GEX = +$2.187B; ZGL = $37.06; spot $44.22 — local SHORT-gamma trough $40–$45 contains spot; $44 = −$755M, $46 = +$640M support_wall, $50 = +$1.6B mega-wall" [STRUCT:gex / today_gamma_flip] — every strike of both option structures references this map directly. Plus INVERTED 30D skew (call IV 34.0% > put IV 33.2%) [STRUCT:term_skew] justifies the call-debit-spread edge. |
| 5 — historical | **−** (−7) | "bullish_flow signal (10-day forward): 15 signals, win_rate 26.7%, avg move −1.10%" [HIST:historical_signal_backtest] — direct historical contradiction to the LONG kicker. Also: "20 of 28 trailing days were bearish flow" [HIST:historical_trend]. Phase 9 mitigated this via downward sizing on the kicker. |
| 6 — macro | **−** (−7) | "Financial Services sector dollar flow −$48,789,451 today (5/19) — top-3 SECTOR OUTFLOW" [MACRO:MarketRegime_2026-05-19] and "April CPI +3.8% YoY (vs 3.3% prior, hottest since May 2023)" [MACRO:CPIAUCSL_2026-04] — both oppose any directional long; partially compatible with defined-risk RANGE only. |
| 7 — insights | **+** (+7) | "conviction_matrix scenario = DIRECTIONAL_LONG, confidence 27.4%, dark_pool buy_ratio 0.735; institutional_accumulation = ACCUMULATION 2.77× buy/sell" [INSIGHT:conviction_matrix / institutional_accumulation] — clean composite bull labels, but absence from bullish_signal_confluence top 100 caps the score at `+` not `++`. |
| 8 — agents | **0** (raw 0) | 4 agents: accumulation-hunter LONG −2 (not RANGE), contrarian-scanner SHORT −2 (not RANGE), sweep-tracker RANGE +2 (match), risk-monitor NEUTRAL +2 (defined-risk compatible). Net **0**. Convergent S/R $42.50–$46.00 directly informs the IC strike placement. |

**Raw score arithmetic:**
```
phase 1: +7
phase 2: +7
phase 3: +15
phase 4: +15
phase 5: -7
phase 6: -7
phase 7: +7
phase 8: 0
───────────
raw:    +37

confluence_score = round((37 + 115) / 230 × 100) = round(66.087) = 66
```

**Confluence_score: 66 / 100** → rubric band 65–79 → recommended bin **0.75**.

**Phase-9 actual bin: 0.65 (one bin below recommendation — conservative)**.
Per the sizing rubric, "phase-9 may set `final_size_pct < suggested_size_pct`
without explanation". The conservative bin is appropriate given the agent
desk split and the TRANSITIONAL regime.

## Contradictions

- **phase-5 (historical):** market-wide `bullish_flow` 10-day win rate is
  only **26.7%** [HIST:historical_signal_backtest] over the most recent
  window, while `bearish_flow` win rate is **71.4%** — current setups
  with bullish features are losing 3:1. Conflict: phase-9's LONG kicker
  acts on a bullish setup that historically loses.
  **Resolution applied in phase-9:** (a) LONG kicker sized DOWN to 2%
  of book (vs 5% Kelly cap), (b) signal-based invalidation if
  `consecutive_build_days` resets, (c) tight $43.40 price stop. ✓

- **phase-6 (macro):** Financial Services is a sector OUTFLOW today
  (−$48.8M, top-3 outflow) [MACRO:MarketRegime_2026-05-19], April CPI is
  re-accelerating (+3.8% YoY, hottest since 2023-05), TRANSITIONAL regime
  mandates half-size. Conflict: directional LONG on a single name in a
  sector-outflow regime fights two tailwinds.
  **Resolution applied in phase-9:** (a) LONG kicker capped at 2%
  (already addressed), (b) macro-based invalidation lists hawkish FOMC
  AND hot CPI as exits, (c) post-trade monitoring requires weekly
  Fin Svc sector flow review with 3-week persistence trigger. ✓

## Citation spot-check

3 citations sampled from phase-9's `## Citations summary`:

1. **[DP:dark_pool_block_stratified]** — "mega-tier `buy_ratio = 1.0` on
   $29,639,716 across 2 trades" — `grep` of phase-2-dark-pool.md §"Tier
   breakdown":
   ```
   mega   (≥$10M):   2 trades   |  $29,639,716 | buy_ratio 1.000  |  100% BUY
   ```
   **RESOLVES ✓** (premium matches to the dollar; trade count matches; ratio matches).

2. **[OI:oi_biggest_increases]** — "PYPL 2026-06-18 $50C OI +1,352 →
   23,713, prev bid_vol 2,287 vs ask 725 (3.2:1 bid)" — `grep` of
   phase-3-positioning.md §"Largest OI increases" row 5:
   ```
   | **50**   | **2026-06-18** | **30** | **C** | **+1,352** | **23,713** | **725 / 2,287**  | **bearish** (overwrite) | **Jun $50 overwrite — KEY CAP** |
   ```
   **RESOLVES ✓** (strike $50, expiry 6/18, OI delta +1,352, total OI
   23,713, ask 725 / bid 2,287 = 3.15:1 — phase-9's "3.2:1" is a rounding,
   still accurate).

3. **[STRUCT:iv_term_structure]** — "5/22 expiry avg_iv 47.0% vs 5/29
   34.4%" — `grep` of phase-4-structure.md §"IV term structure":
   ```
   | 2026-05-22 | 3 | **47.0%** | 2,130 | **Weekly spike** ... |
   | 2026-05-29 | 10 | 34.4% | 631 | Normalized |
   ```
   **RESOLVES ✓** (both IV values match exactly).

## Citation failures

None. All 3 spot-checked citations resolve cleanly to the cited phase MD.

## Sanity checks

| Check | Status | Notes |
|-------|--------|-------|
| All `phase-*.md` files present (0–10) | ✓ | `ls`: phase-0 through phase-9 verified at write time; phase-10 self-emitting now. |
| Phase-9 cites ≥3 distinct upstream datapoints in thesis | ✓ | Thesis paragraph cites [DP:dark_pool_block_stratified], [HIST:historical_oi_trend via AGENT:accumulation-hunter], [OI:oi_biggest_increases], [MACRO:MarketRegime_2026-05-19], [AGENT:risk-monitor] = 5 distinct tags. |
| Conviction bin ∈ {0.55, 0.65, 0.75, 0.85, 0.95} | ✓ | Phase-9 set to 0.65. |
| ≥1 directional + ≥1 defined-risk structure | ✓ | Directional: 7/17 Bull Call Debit Spread (long $44C / short $50C). Defined-risk: 5/22 Iron Condor (long $42.50P / short $43.50P + short $45.50C / long $46.50C). |
| Sizing math shown explicitly | ✓ | Both structures show Kelly inputs (p, b, fraction), raw Kelly %, capped final %, and deviation reason for the LONG kicker. |
| Disclaimer at top of phase-9 | ✓ | "For research and educational use only. Not financial advice. Sizing and structures are illustrative." |

## Open items / known gaps surfaced during audit

- **Phase 5 `historical_oi_trend` data was deferred to a disk file and not
  read inline** due to token-limit truncation. Phase 8's accumulation-hunter
  later surfaced the key fact (10 consecutive build days, +290,842 OI,
  BUILDING trend). Phase 9 cites it via [HIST:historical_oi_trend via
  AGENT:accumulation-hunter]. The audit trail is preserved but a
  re-runner who wants direct verification must `jq` the file at
  `/Users/ewan/.claude/projects/-Users-ewan-Development-stock-deep-dive/5e26e164-2811-4f94-b6bd-bbe50209ec09/tool-results/mcp-uw-pp-historical_oi_trend-1779307151611.txt`.
- **Yahoo `quoteSummary` returned HTTP 401** in both phase-7
  `insights_deep_dive.yahoo_fundamentals` and (implicitly)
  `insights_analyst_vs_flow`. No P/E, market cap, or short interest from
  this lens. Phase 6 covered fundamentals via WebSearch instead. Not
  blocking, but a re-runner should verify Yahoo auth before relying on
  those insight tools.
- **Effective data date is 2026-05-19, NOT 2026-05-20 as requested.**
  Documented in phase-0-intake.md. No data exists for 2026-05-20 yet —
  the parquet files have a T+1 cadence. Phase-9's monitoring checklist
  treats 2026-05-20 as the EXECUTION day (the day after the data
  observation), which is the correct PM-voice framing.

## Final auditor note

The run is **internally consistent and ready for action as written**.
The two contradiction phases (5 historical, 6 macro) have been
mechanically addressed in phase 9 via downward sizing on the LONG kicker
and tight, falsifiable invalidation conditions. Phase 9's conservative
0.65 bin (vs the 66/100 score's recommended 0.75) reflects honest
respect for the 1-1-1-1 desk split rather than a sizing error; if the
desk were to come back to 4-of-4 long with confluence ≥ 75, the kicker
could be re-sized up to the 5% cap.

**Final confluence_score: 66 / 100. RANGE primary + bounded LONG kicker
is the right shape of trade for this signal stack.**
