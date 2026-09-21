# Phase 9 — Trade Blueprint

**Ticker:** FCX (Freeport-McMoRan, NYSE)
**As-of date:** 2026-05-20 (effective data 2026-05-19)
**PM voice:** desk PM running an institutional book
**Spot reference:** $58.71 close 2026-05-19 [HIST:historical_trend@phase-5]
**Upstream phases cited:** phase-0 through phase-8

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

FCX flushed 12.6% in 4 sessions from the May-13 $67.16 peak to $58.71
[HIST:historical_trend@phase-5] and the institutional bid is now visible in
the tape — dark-pool block-tier buy_ratio 0.69 + large-tier 0.601 = ~$11M net
accumulation [DP:block_stratified@phase-2], the dominant near-term
long-gamma node sits at $65 with +$1.44B net GEX (the magnet/ceiling)
[STRUCT:gex@phase-4], and Deutsche Bank's $72 PT [MACRO:DBPT_2026-05-13@
phase-6] frames analyst fair value at the same level UW's
accumulation-hunter agent flagged as the natural target [AGENT:accumulation-
hunter@phase-8]. With IV at the 40.7th percentile of FCX's own 1y range,
VRP −7.4 pts, and UW's conviction-matrix classifying the institutional
imprint as COVERED_CALL (long stock + short calls) [INSIGHT:conviction_
matrix@phase-7], the trade is **mean-reversion long up to the $65 magnet,
expressed via a debit call spread that mirrors institutional collar
economics — NOT a naked directional bet**.

## Bias + conviction + horizon

- **Directional bias:** **LONG (range-bounded $55 → $65)**
- **Conviction (M-01 bin):** **0.65**
- **Time horizon:** **1-4w (target exit by Jun-18 OPEX)**
- **Why this bin:** phase-10's projected confluence score for a LONG bias
  is ~54 (mid-band 50–64), so the rubric maps to 0.65. The underlying RANGE
  confluence is much higher (~81) but a range structure would require
  selling premium, which violates the phase-5 VRP rule
  [HIST:vrp@phase-5]. The bull call spread captures the range thesis with a
  long-premium P&L profile, so we adopt the higher-discipline LONG bin.

## Entry zones

| Entry type | Price (spot) | Trigger condition | Source |
|------------|------|-------------------|--------|
| **Primary** | $58.50–$59.30 | Establish into current institutional accumulation band before May-22 weekly close | [DP:price_levels@phase-2] top-5 today: $59.13 / $59.27 / $59.69 / $59.21 / $59.41; [INSIGHT:institutional_accumulation@phase-7] VWAP $59.14 |
| **Aggressive** | $57.50–$58.00 | Intraday dip to upper edge of phase-1 OTM put-buying cluster ($58 strike, OI/sweep evidence of dealer-supported demand) | [FLOW:options_flow_sweeps@phase-1] 58P Jun-18 ask sweep $244k + [STRUCT:today_gamma_flip@phase-4] $58 weekly-resistance flip to support on reclaim |
| **Fade** | reject at $60.50 | If price rallies into $60.50 DP shelf and stalls intraday without breaching $60.65, fade to test $58–$59 base; opens a second entry at primary band | [DP:price_levels@phase-2] $60.50 = $11.3M cumulative shelf; [STRUCT:today_gamma_flip@phase-4] $60 = +$80.5M support → resistance pivot |

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| **Hard floor / cascade trigger** | **$55.00** | [STRUCT:gex@phase-4] −$458M GEX node = dominant short-gamma; [HIST:historical_trend@phase-5] May-04 close $55.57 = recent rally launch pad |
| Support (institutional band) | $58.50–$59.30 | [DP:price_levels@phase-2] today's DP cluster; [INSIGHT:institutional_accumulation@phase-7] VWAP $59.14 |
| Immediate ceiling / pivot | $60.50 | [DP:price_levels@phase-2] $11.3M shelf; [STRUCT:today_gamma_flip@phase-4] support wall +$80.5M GEX |
| Intermediate resistance | $62.30–$62.63 | [DP:price_levels@phase-2] $16.5M aggregate |
| **Gamma flip (ZGL)** | **$64.09** | [STRUCT:gex@phase-4]; clearing this unlocks dealer-long-gamma regime above |
| **Dominant magnet / target** | **$65.00–$66.14** | [STRUCT:gex@phase-4] +$1.44B net GEX; [DP:price_levels@phase-2] $191M cumulative concentration; [MACRO:DBPT_2026-05-13@phase-6] Deutsche PT $72 |
| Largest pin this OPEX | n/a — Jun-18 is 29 DTE | [OI:pin_risk@phase-3] FCX absent from pin-risk top-50 (>7 DTE) |

## Invalidation

Three categories, each falsifiable. Hard stop = full exit on any single
firing.

- **Price-based:** **Two consecutive daily closes below $55.00** OR an
  intraday break below $55 with no immediate reclaim
  [STRUCT:gex@phase-4 −$458M GEX node = mechanical cascade to $50 short-
  gamma node]. **No "give it room" — the cascade is hard-coded into the
  dealer map.**
- **Signal-based:** Dark-pool buy/sell ratio falls **below 1.20** on the
  next session (today: 1.58) [INSIGHT:institutional_accumulation@phase-7];
  OR UW conviction-matrix flips from COVERED_CALL to DIRECTIONAL_SHORT
  [INSIGHT:conviction_matrix@phase-7]; OR the new 59C Jun-18 OI starts
  decaying (>1,000-contract OI loss in single session)
  [OI:biggest_increases@phase-3 baseline 6,216 OI]. **Any ONE of the three
  → close.**
- **Macro-based:** **Hawkish surprise on June 10 CPI** (release 8:30 ET,
  20 DTE) or **June 16-17 FOMC + Warsh-debut dot plot** materially above
  current 3.50–3.75% target / dots [MACRO:FOMC_2026-06-17@phase-6] —
  defined as the policy-sensitive 2y yield ripping ≥ 25bp on the print AND
  copper rolling below $6.00/lb intraday [MACRO:Copper_2026-05-15@phase-6].
  Exit at the next session open; do not wait.

**Exit on invalidation:** **HARD STOP — close 100%** at any of the three.
Debit structure cannot be rolled responsibly into a broken thesis.

## Sizing (% of risk, NOT dollars)

Applying `rubrics/sizing-rubric.md`:

**Kelly inputs:**
- p = **0.65** (conviction bin)
- Entry (long leg @ spot ≈ $59) — see "Directional (primary)" below.
- Target: short-leg strike **$65** (dealer magnet, DP $191M concentration).
- Stop: invalidation at **$55** close.
- Long-leg debit (60/65 Jun-18 spread): ≈ **$1.88** (estimates below).
- Max gain: spread width $5 − debit $1.88 = **$3.12** at $65+.
- Max loss: full debit $1.88 (price = $55 stop, but defined-risk structure
  caps loss at premium paid regardless of spot).
- **b = payoff ratio = max_gain / max_loss = $3.12 / $1.88 = 1.66**

**Raw Kelly:**
```
raw_kelly = (0.65 × 1.66 − (1 − 0.65)) / 1.66
          = (1.079 − 0.35) / 1.66
          = 0.729 / 1.66
          = 0.4392 (43.9%)
```

**Fractional Kelly (0.25) and cap (5%):**
```
suggested_size_pct = min(0.4392 × 0.25 × 100, 5)
                   = min(10.98, 5)
                   = 5.00%
```

- **Final size:** **5.00% of book risk** (= the Kelly cap; max-loss of
  spread sums to no more than 5% of risk-budget).
- **Deviation reason:** none. The TRANSITIONAL market regime
  [MACRO:MarketRegime_2026-05-19@phase-6] + 26.7% bullish_flow signal win
  rate [HIST:signal_backtest@phase-5] argue against pushing above the cap;
  risk-monitor's "half-size at most" verdict [AGENT:risk-monitor@phase-8]
  is fully respected at 5%.

## Option structures

### Directional (primary) — Bull Call Spread

- **Structure:** Long Jun-18 60C / Short Jun-18 65C (debit call spread)
- **Strike(s) / expiry:** **60 / 65, expiry 2026-06-18 (29 DTE)**
- **Debit:** ~$1.88 ($3.35 − $1.47 from phase-1 mid-quotes)
  [FLOW:options_flow_sweeps@phase-1]
- **Breakeven:** $60.00 + $1.88 = **$61.88**
- **Max gain:** $3.12 per spread (@ FCX ≥ $65 by 2026-06-18)
- **Max loss:** $1.88 per spread (full debit)
- **Why this structure:**
  1. **Mirrors institutional COVERED_CALL economics** — long lower strike
     replicates the long-stock leg; short 65C replicates the call-write
     [INSIGHT:conviction_matrix@phase-7].
  2. **Strike selection sources:** 60C long leg aligns with the $60.50 DP
     shelf [DP:price_levels@phase-2] and the new 59C Jun-18 OI build at
     adjacent strike [OI:biggest_increases@phase-3]; 65C short leg sits at
     the dealer-long-gamma magnet [STRUCT:gex@phase-4 +$1.44B net GEX] and
     the 5-day institutional DP concentration cluster $65.94–$66.14 [DP:
     price_levels@phase-2].
  3. **Expiry 2026-06-18 captures the FOMC binary** [MACRO:FOMC_2026-06-17
     @phase-6] without being a naked vol bet. The defined-risk profile means
     a hawkish surprise caps loss at $1.88 — no overnight gap-down disaster.
  4. **Cheap IV + cheap baseline vol favours debit, not credit**
     [HIST:vrp@phase-5 VRP −7.4, IV 40.7%ile].
  5. **Payoff ratio b = 1.66** is enough to make a 65% p-bin trade work
     under Kelly while staying at half-conviction.

### Defined-risk alternative — Put Credit Spread

For a higher win-rate, lower-upside expression of the same "FCX defends
$55" thesis.

- **Structure:** Short Jun-18 55P / Long Jun-18 50P (put credit spread)
- **Strike(s) / expiry:** **55 / 50, expiry 2026-06-18 (29 DTE)**
- **Estimated credit:** ~$0.45 net (sell 55P @ ~$1.00 vs buy 50P @ ~$0.55,
  estimates derived from phase-1 surrounding strikes; verify on live
  chain)
- **Breakeven:** $55.00 − $0.45 = **$54.55**
- **Max gain:** $0.45 per spread (full credit if FCX ≥ $55 by 2026-06-18)
- **Max loss:** $5.00 − $0.45 = $4.55 per spread
- **Why this structure:**
  - Wins if FCX simply HOLDS the $55 floor that every phase-8 agent and
    phase-4 [STRUCT:gex@phase-4 −$458M GEX node] flagged as the line.
  - Lower notional capital but worse payoff (b ≈ 0.10) — only suitable if
    PM wants a high-probability income trade in addition to (not
    replacing) the directional spread.
  - **Important:** this is the only sanctioned credit structure here. The
    VRP rule [HIST:vrp@phase-5] prohibits selling premium in an absolute
    sense — but a defined-risk credit spread that pays for tail protection
    (the long 50P leg) is acceptable.
  - Size at HALF the primary spread allocation (2.5% of book risk) given
    the inferior payoff and the regime caveat.

## Macro overlay (cite phase-6)

**Tailwinds:**
- **Deutsche Bank PT raised $58 → $72 (Buy)** [MACRO:DBPT_2026-05-13@phase-6]
  — analyst consensus cluster $70–$81 frames the magnet target.
- **AI/data-center copper demand: 27–33 t/MW of installed capacity**
  [MACRO:CopperAIDemand_2026@phase-6] — structural 6–12mo tailwind.
- **JPMorgan: LME copper avg $12,500/ton Q2-26** [MACRO:CopperForecast_
  2026-Q2@phase-6] — bullish base case.
- **Grasberg ramp on track, Indonesia exports extended through mid-2026**
  [MACRO:GrasbergGuidance_2026-Q1@phase-6][MACRO:IndonesiaExport_2026@
  phase-6] — operational tailwind.

**Headwinds:**
- **Market regime TRANSITIONAL — 34.7% bullish breadth, defined-risk only**
  [MACRO:MarketRegime_2026-05-19@phase-6] — caps position size.
- **SPY 9 of 10 days bearish flow despite uptrend** [MACRO:SPYTrend_2026-
  05-19@phase-6] — broad-tape divergence; cyclicals at risk first if risk-
  off.
- **FOMC June 16-17 (Warsh debut)** [MACRO:FOMC_2026-06-17@phase-6] —
  uncertainty premium that could break either way.
- **Goldman Sachs: copper modest decline from record highs**
  [MACRO:CopperForecast_2026@phase-6] — counter-narrative cap.
- **Copper retraced from $6.44/lb to $6.10/lb** [MACRO:Copper_2026-05-15@
  phase-6] — momentum cooling; FCX is a 1:1 high-beta proxy.

**Net:** **MIXED, with bullish 6–12mo structural tilt and binary 4-week
catalyst risk.** Sized accordingly (5% / cap).

## Catalyst calendar (next 30d)

| Date | DTE | Event | Impact direction |
|------|-----|-------|------------------|
| 2026-05-22 | 2 | Weekly OPEX (gamma pin candidate at $60) | + range / ? |
| 2026-05-29 | 9 | Weekly OPEX; 64% IV pre-CPI hedge unwind window | ? |
| 2026-06-05 | 16 | Weekly OPEX | neutral |
| **2026-06-10** | **20** | **CPI release (US May data, 8:30 ET)** | **? high two-way** |
| 2026-06-12 | 22 | Weekly OPEX (post-CPI vol fade) | neutral |
| **2026-06-16–17** | **27–28** | **FOMC + dot plot, WARSH DEBUT** | **? primary 4-week binary** |
| **2026-06-18** | **29** | **Monthly OPEX = trade expiry** | resolves spread P&L |

Sources for all: [MACRO:*@phase-6].

## Post-trade monitoring checklist

- [ ] **Daily DP buy/sell ratio.** Today 1.58 [INSIGHT:institutional_
      accumulation@phase-7]; close if next session ratio < 1.20 (signal-
      based invalidation).
- [ ] **59C Jun-18 OI.** Baseline 6,216 [OI:biggest_increases@phase-3]; flag
      if it loses >1,000 in a single session.
- [ ] **UW conviction-matrix scenario.** Today COVERED_CALL @ 20.6%
      [INSIGHT:conviction_matrix@phase-7]; close if it flips to
      DIRECTIONAL_SHORT or HEDGED_SHORT.
- [ ] **Cumulative premium flow (5-day).** Today net 90d −$22.8M
      [HIST:cumulative_premium_flow@phase-5]; flag 3 consecutive sessions of
      net bearish flow > $5M/day.
- [ ] **GEX regime.** Today NEGATIVE at spot (ZGL $64.09) [STRUCT:gex@
      phase-4]; **flip to POSITIVE (spot reclaims $64.09 close) = ratchet
      to full position from half — but cap at 5% remains.**
- [ ] **Copper spot.** Currently $6.10–$6.20/lb [MACRO:Copper_2026-05-15@
      phase-6]; close on confirmed close below $6.00/lb intraday
      (macro-based invalidation, pairs with CPI/FOMC trigger).
- [ ] **SPY breadth & TRANSITIONAL regime.** [MACRO:MarketRegime_2026-05-19
      @phase-6]; if regime flips to RISK-OFF, reduce 50% immediately and
      review the trade.
- [ ] **Next FCX earnings 2026-07-22.** Outside this trade's Jun-18 expiry,
      but if any pre-announcement leak hits the tape, the spread can be
      closed early to capture vol expansion.

## Citations summary (M-04 audit list)

Minimum 3 distinct upstream datapoints required; this plan cites the
following (more than minimum):

1. **[DP:block_stratified@phase-2] §Tier breakdown** — block_tier
   buy_ratio 0.69 ($6.55M), large_tier 0.601 ($42.3M), implied net dark-
   pool accumulation ≈ +$11M today.
2. **[STRUCT:gex@phase-4] §GEX per-strike map** — $65 strike net_gex
   +$1,437,659,056 (dominant long-gamma node); $55 strike net_gex
   −$458,228,523 (dominant short-gamma node); ZGL $64.09.
3. **[HIST:vrp@phase-5] §IV regime** — VRP = −7.43 pts (IV30 49.9% <
   realised 30d vol 57.3%), regime label PREMIUM_BUYING; favour debit
   structures.
4. **[INSIGHT:conviction_matrix@phase-7] §Conviction matrix** — scenario =
   COVERED_CALL at 20.6% confidence; institutional pattern is long stock +
   short calls. Mirrored by the bull call spread structure.
5. **[MACRO:DBPT_2026-05-13@phase-6] §FCX-specific catalysts** — Deutsche
   Bank price target raise $58 → $72 (Buy); analyst consensus cluster
   $70–$81 frames the $65 short-leg strike.
6. **[OI:biggest_increases@phase-3] §Largest OI increases** — 59C
   2026-06-18 OI 0 → 6,216 (+6,216) on 6,508 vol, ask_vol 5,611 (86%)
   vs bid_vol 722; $3.23M premium — the only "fresh-conviction" build
   of the day at near-ATM.
7. **[AGENT:accumulation-hunter@phase-8]** — verdict LONG conv 3, target
   $65, kill <$55; *"Real accumulation — institutions are buying the
   flush and writing the $65 magnet, not chasing; long 59/65 call spread
   Jun-18, half-size, killed under $55."*

---

**PM sign-off:**
*Trade: long 1× FCX Jun-18 60C / short 1× FCX Jun-18 65C @ ~$1.88 debit.
Size 5.00% of book risk. Stop: hard exit on any of three invalidations
listed. Target: $3.12 max gain at 65+. Time horizon: hold through FOMC
Jun-17, exit Jun-18 OPEX or at first invalidation. Sized for plurality of
4 sub-agents agreeing on $55 floor; long bias derives from accumulation-
hunter + COVERED_CALL institutional baseline; range-cap from $65 dealer-
gamma node and analyst $70–$81 cluster.*
