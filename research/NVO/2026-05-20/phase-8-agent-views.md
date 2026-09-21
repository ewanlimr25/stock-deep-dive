# Phase 8 — Multi-Agent Analyst Desk

**Ticker:** NVO
**As-of date:** 2026-05-20
**Generated:** 2026-05-20T22:25:00-04:00
**Upstream phases cited:** phase-1 through phase-7

## Summary

Three of four agents return **LONG**, one returns **NEUTRAL**. Average
conviction across the four = **3.25/5**, with the long-biased trio
averaging **3.67/5** and the contrarian neutral at 2/5. Every agent
identifies the **same support ($44.15) and the same invalidation
($44.00 close)**, which is unusual cross-perspective agreement on
levels. Resistance varies — accumulation-hunter and contrarian see
$45.80 as the immediate ceiling; sweep-tracker and risk-monitor extend
to $50 as the real magnet. Universal top-risk: the **July 1, 2026 LLY
Medicare GLP-1 Bridge** launch excludes NVO — a known unhedged
competitive event 6 weeks out.

`earnings-scout` was skipped per phase-8 spec: NVO Q2 earnings are
2026-08-05, 77 days out, well outside the 14-day pre-earnings window.

## Agent verdicts table

| Agent | bias | conviction | horizon | one_line_take |
|-------|:----:|:----------:|---------|---------------|
| accumulation-hunter | **LONG** | **4** | 1-4w | Institutional fingerprints are everywhere — mega DP block, LEAP synthetic, 29-day OI build, GEX flip — this is textbook quiet accumulation pre-move; size the long. |
| contrarian-scanner | NEUTRAL | 2 | 1-5d | Crowd is complacent into a 7/1 Medicare headwind, but smart money is on the same side as the crowd here — no clean fade, just a tactical mean-revert toward $44 if $45.80 ceiling rejects. |
| sweep-tracker | **LONG** | **4** | 1-4w | Synthetic-long LEAP whale, dark-pool $26.9M mega-buy and POS-GEX flip in 7th-pctile IV — cheap upside convexity, ride $45 to $50. |
| risk-monitor | **LONG** | 3 | 1-4w | Real institutional accumulation but size at half-Kelly — TRANSITIONAL regime plus 1-day flip following a 5-day bearish streak demands confirmation before pyramiding; cut on $44 close. |
| earnings-scout | n/a | n/a | n/a | SKIPPED: NVO Q2 earnings 77 DTE (> 30d) — out of window |

## Per-agent details

### accumulation-hunter
```
VERDICT
- bias: LONG
- conviction: 4
- horizon: 1-4w
- key_levels:
    support: 44.15
    resistance: 45.80
    invalidation: sustained close below 44.00 (flips dealers into the $44 short-gamma pocket, opens $40 magnet)
- top_signal: Phase 2's $26.94M mega dark-pool print at $45.07 with mega-tier buy_ratio 1.0 and block-tier 0.893, occurring on the same session as Phase 1's $1.0M ask-side LEAP sweep on the 2028-01 $45 calls and Phase 3's 29-consecutive-day OI build (+628k contracts) — three independent accumulation footprints converging on one strike.
- top_risk: A vanna-driven IV crush into 6/18 OPEX could force dealers to unwind their long-stock hedge, and the 7/1 LLY Medicare Bridge launch is an unhedged competitive event sitting just past horizon.
- one_line_take: Institutional fingerprints are everywhere — mega DP block, LEAP synthetic, 29-day OI build, GEX flip — this is textbook quiet accumulation pre-move; size the long.
```

### contrarian-scanner
```
VERDICT
- bias: NEUTRAL
- conviction: 2
- horizon: 1-5d
- key_levels:
    support: 44.15
    resistance: 45.80
    invalidation: sustained close above 45.80 on >1.5× avg volume invalidates fade; conversely loss of 44 flips to short-gamma trapdoor
- top_signal: Phase 7 confluence screener excluded NVO from bullish top 50 despite five aligning factors, and Phase 4 term skew at 0.998 (COMPLACENT) with PCR 0.33 shows tail risk is unpriced exactly as LLY's 7/1 Medicare Bridge looms — the crowd is leaning long into a known competitive cliff.
- top_risk: A genuine institutional LEAP synthetic (Phase 1 $1.0M Jan 2028 $45C ask + matched $45P bid-sale, Phase 2 $26.9M mega DP print, Phase 3 $42.5P put-write floor) is multi-signal accumulation — fading this is fading real smart money, not retail euphoria.
- one_line_take: Crowd is complacent into a 7/1 Medicare headwind, but smart money is on the same side as the crowd here — no clean fade, just a tactical mean-revert toward $44 if $45.80 ceiling rejects.
```

### sweep-tracker
```
VERDICT
- bias: LONG
- conviction: 4
- horizon: 1-4w
- key_levels:
    support: 44.15
    resistance: 50.00
    invalidation: sustained close below 44 (loss of $45 wall, opens short-gamma trap-door toward $40)
- top_signal: Phase 1 $1.0M ask-side sweep on Jan 2028 $45C (30 trades, δ0.62) plus phase-5 GEX flip POSITIVE with −$17.30 ZGL collapse mirrors the April 28 analog that ran +8% in 5 sessions.
- top_risk: July 1 LLY Medicare GLP-1 Bridge launch (phase 6) excludes NVO — competitive headwind that could cap the move and re-bid downside skew before the bullish setup matures.
- one_line_take: Synthetic-long LEAP whale, dark-pool $26.9M mega-buy and POS-GEX flip in 7th-pctile IV — cheap upside convexity, ride $45 to $50.
```

### risk-monitor
```
VERDICT
- bias: LONG
- conviction: 3
- horizon: 1-4w
- key_levels:
    support: 44.15
    resistance: 50.00
    invalidation: sustained close below 44.00 (flips into -$93M short-gamma pocket; opens path to -$107M trap-door at $40)
- top_signal: Phase 5 GEX regime flipped POSITIVE today with ZGL collapsing -$17.30 (from $44.74 to $27.44) — the biggest 1-day structural reset in the 29-session series, mirroring the April 28 analog that ran +8% in five sessions, confirmed by Phase 2's $26.94M mega-block buy at $45.07 and Phase 1's $1.0M Jan 2028 $45C ask sweep.
- top_risk: 5-day sweep persistence was BEARISH ($9.68M, 5/5 sessions) flipping only today — a single-day reversal inside a TRANSITIONAL regime (39.5% breadth, hot 3.8% CPI) is unconfirmed; July 1 LLY Medicare Bridge is an unhedged competitive cliff and negative vanna means any IV crush turns dealer flow into mechanical selling.
- one_line_take: Real institutional accumulation but size at half-Kelly — TRANSITIONAL regime plus 1-day flip following a 5-day bearish streak demands confirmation before pyramiding; cut on $44 close.
```

### earnings-scout
**MISSING / SKIPPED** — NVO Q2 2026 earnings on 2026-08-05 is 77 days
out, beyond the 14-day pre-earnings window. Per phase-8 spec, skip
rather than force the call.

## Disagreements

**Only one dissent (contrarian-scanner, NEUTRAL 2).** Its top_signal is
notable because it overlaps with two of phase-7's caveats:
1. NVO missing from bullish_signal_confluence top 50
2. COMPLACENT skew (0.998) ahead of a known competitive cliff (LLY Medicare Bridge)

Importantly, the contrarian-scanner does NOT recommend SHORT. The
agent's own one-line take concedes: "smart money is on the same side as
the crowd here — no clean fade." The fade case exists in theory
(complacency + LLY catalyst) but is undermined by the institutional
footprint. **This counts as confirmation of the LONG thesis with an
explicit risk callout, not a true bear dissent.**

**Resistance split:**
- $45.80 (accumulation-hunter, contrarian-scanner) — phase-2's
  institutional 5-day price-level ceiling
- $50.00 (sweep-tracker, risk-monitor) — phase-4's $825M GEX call wall

Phase 9 should treat $45.80 as the **first take-profit zone (T1)** and
$50.00 as the **structural target (T2)**.

## Tool errors

- `earnings-scout`: SKIPPED, not error (earnings out of window).

## Verdict for downstream phases

- **Plurality bias: LONG (3/4 = 75%)**; neutral dissent (1/4) does not propose SHORT.
- **Average conviction (non-MISSING agents) = (4+2+4+3)/4 = 3.25/5**
- **Three highest-quality signals across all agents:**
  1. **Phase 2's $26.94M mega DP print at $45.07 with mega-tier buy_ratio 1.0** [DP:dark_pool_largest, DP:block_stratified] — cited by accumulation-hunter, contrarian-scanner (acknowledged), risk-monitor.
  2. **Phase 1's $1.0M ask-side LEAP sweep on 2028-01-21 $45C (30 trades, δ0.62)** [FLOW:sweeps] — cited by all 4 agents.
  3. **Phase 5's POSITIVE GEX flip with ZGL collapse −$17.30, mirroring the April 28 analog (+8% in 5 sessions)** [HIST:gex_time_series] — cited by sweep-tracker, risk-monitor.

- **Open questions surfaced by agents:**
  - Vanna-driven IV crush risk into 6/18 OPEX → would force dealer-hedge unwind (accumulation-hunter).
  - LLY Medicare Bridge competitive cliff (7/1) lies just past the 1-4w horizon → does phase 9 cap horizon at 6 weeks or take the LEAP-scale view (multi-quarter)?
  - Today's flip is a **1-day reversal of a 5-day bearish persistence streak** — needs Monday confirmation; risk-monitor flags this as the dominant unresolved factor.
  - Negative net vanna (phase-4) → "IV crush turns dealer flow into mechanical selling"; this is a non-obvious second-order risk.
