# Phase 9 — Trade Blueprint

**Ticker:** SNOW (Snowflake Inc.)
**As-of date:** 2026-05-29
**PM voice:** desk PM running an institutional options-overlay book
**Spot reference:** $255.55 (phase-0 / fz close; +6.84% on the day)
**Upstream phases cited:** phase-0.5 through phase-8b

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

SNOW is a **best-in-class hyper-grower that has gone parabolic and euphoric** —
+52% into a clean 5/27 beat, **RSI 86.9** `[HIST:rsi fz]`, 50/58 analysts at
buy/strong-buy with PT raises flooding to $285–$325 `[SENT:recom fz]` — but the
**smart money is distributing into that euphoria**: the dark-pool **mega tier is a
net seller (buy_ratio 0.401)** placing closing blocks at the $255.55 high
`[DP:block-stratified]`, the largest options sweep is a **$14M bid-side call
sale** `[FLOW:sweeps]`, and **price-vs-flow is bearishly divergent** ("price
+77.5% but flow bearish") `[INSIGHT:price-vs-flow]`. **Dealers are long gamma and
pin the tape at $250–$255** (walls $255 +$9.1M / $250 +$7.2M) `[STRUCT:gex]`, so
the trade is a **defined-risk fade/range at the $255 wall** — sell the overpriced
upside into a name nobody can chase (RSI 87, P/S 17.6) and nobody should naked-short
(the beat + strong-buy + dealer-short-call squeeze fuel, phase-7b VETO).

## Bias + conviction + horizon

- **Directional bias:** RANGE / fade-the-$255-wall (downside-skewed, defined-risk)
- **Conviction (M-01 bin):** **0.65**
- **Time horizon:** 1–4w (June-18 expiry, ~20 DTE)
- **Why this bin:** phase-10 confluence ≈ 69 maps to the 0.75 band, but I **deviate
  down one bin to 0.65** (downward deviation, always permitted) — the phase-7b
  **VETO on the short direction** (a strong-buy hyper-grower) and the unrefuted
  phase-8b **>$262 squeeze tail** are real disconfirming evidence that keep this a
  *moderate-edge* fade, not a high-conviction one.

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| Primary | $254–$256 | sell into strength at the $255 gamma wall / MOC-distribution zone | `[STRUCT:gex]` `[DP:largest]` |
| Aggressive | $258–$262 | a failed push above the wall that *rejects* (fade the exhaustion) — but stand aside if it *holds* >$262 | `[STRUCT:gex]` |
| Fade (counter) | $248 | if $250 wall breaks and SNOW loses the pin, the range is gone — flip to stand-aside / momentum-short, do not fade-buy | `[STRUCT:gex]` |

Price-context color: **RSI 86.9, +53.8% above SMA20, near 52w high $280.67**
`[HIST:rsi fz][HIST:52w_proximity fz]` — this is the *opposite* of a chase setup;
selling premium into the wall is the disciplined expression, buying the breakout
is not.

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Resistance / pin ceiling | $255–$256 (gamma wall +$9.1M = MOC distribution) | `[STRUCT:gex]` `[DP:largest]` |
| Support / pin floor | $250 (gamma wall +$7.2M) | `[STRUCT:gex]` |
| Squeeze trigger (invalidation) | $262 then $280.67 (52w high) | `[STRUCT:dex]` `[HIST:52w_proximity fz]` |
| Lower support | $248, then $239–$244 (gap-up base) | `[DP:largest]` |
| ZGL (far below — no near-term cascade) | $149.78 | `[STRUCT:gex]` |

## Invalidation

- **Price-based:** *Fade/range invalidated* by a **sustained close above ~$262**
  (clears the $255 pin into thin gamma → dealer-short-call hedge-buying squeeze
  toward $280.67); secondary hard invalidation a close **>$280.67** (52w-high
  breakout, euphoria extends). On the downside, a close **<$248** ends the *range*
  (pin lost) — stand aside, do not fade-buy.
- **Signal-based:** dark-pool **mega tier flips to net buyer** (>0.55)
  `[DP:block-stratified]` (distribution over), OR price-vs-flow divergence
  **resolves bullish** (flow confirms the highs) `[INSIGHT:price-vs-flow]`.
- **Macro-based:** regime flips to clear **RISK_ON / breadth broadens >55%**
  `[MACRO:MarketRegime_2026-05-29 UW]` (a broad melt-up overruns single-name pins),
  or a fresh AI-capex headline re-ignites the mega-cap leadership.

## Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** p_raw = **0.50** (n=**8**, source=`backtest`,
  bullish_flow) → n<10 cap 0.75 → capped **p = 0.50** `[HIST:signal-backtest]`.
  *Caveat:* the trade is a range/fade, so the `bullish_flow` win-rate is a **loose
  proxy** — the empirical edge for *fading* a 50%-bullish-flow signal is, if
  anything, ≥0.50; I keep p=0.50 as the conservative input.
- **Kelly inputs:** for the iron-condor range expression, b = credit/(width−credit)
  = 9.25 / (15 − 9.25) = **1.61**; fraction = 0.25; cap_pct = 5.
- **Raw Kelly:** (0.50×1.61 − 0.50)/1.61 = **0.189** → ×0.25×100 = 4.74% → cap 5%.
  **Win-rate map ceiling:** p=0.50 → "0.50–0.70 = half" ⇒ ≤ **2.5%**. Take 2.5%.
- **Risk gates:**
  - Fundamentals (7b): **VETO** of the *directional short* (strong-buy hyper-grower)
    → **naked short forbidden (0%); defined-risk range/fade carry only.** Our
    structures are defined-risk → permitted, but it bars upsizing.
  - Sentiment/crowd (7c): **CAUTION** (CROWDED_LONG euphoria can persist / FOMO) →
    **cut one size step (half → starter ≈1.25%).**
  - Correlation cluster (6): SNOW vs PATH **ρ 0.478 < 0.60** → **no cluster, no cut.**
  - Sector rotation (6): Tech **rotating IN** (persistence 1/1) — *adverse to a
    fade* → **cut half a size step (≈1.25% → ~0.9%).**
  - Debate (8b): bull_residual **0.70** vs bear_residual **0.58** → **NOT
    disconfirmed → no cut** (the fade thesis cleared).
  - **Context (0.5): GENUINELY_UNUSUAL** → no cap (edge is in the data).
- **Final size:** **1.0% of book risk** (starter — 7c + adverse-rotation cuts;
  7b VETO bars any naked short and caps upsizing). Structure max-loss ≤ 1.0% of book.
- **Deviation reason:** none upward (all moves were cuts).

## Option structures

> Front-expiry implied move **0.55%/day** `[CTX:implied_move]` (post-earnings IV
> crush); the ~20-day June-18 1σ move ≈ **±$6.3** (→ ~$249–$262). Earnings are
> **behind us** (5/27) — no IV-crush risk in the window; **front IV is still rich
> (backwardation, phase-4)** so **selling premium is favoured** (aligns with the
> fade). Strikes anchored to the $255/$250 gamma walls and the $280.67 52w-high
> squeeze level.

### Directional (the fade tilt — defined risk)

- **Structure:** bear call spread (call credit), **$265 / $280, June-18-2026**
- **Strikes / expiry:** sell $265C ($9.70), buy $280C ($5.21) — short strike above
  the $255 pin; long wing at the **$280.67 52w-high squeeze level** (phase-8b
  invalidation) `[STRUCT:gex][HIST:52w_proximity fz]`
- **Credit:** ≈ **$4.49** · **Breakeven:** $269.49 · **Max loss:** $10.51 (if
  SNOW > $280)
- **Why:** monetizes the distribution + pin + euphoria fade; profits unless SNOW
  squeezes >$269.49 (well above the $255 wall). Cheap-to-carry expression of "sell
  the rip" with hard-capped risk at the breakout level. (Lower reward/risk than the
  condor, but cleaner downside-skew.)

### Defined-risk alternative (the regime-prescribed range — primary recommendation)

- **Structure:** **iron condor, sell $265C / sell $240P, buy $280C / buy $225P,
  June-18-2026**
- **Strikes / expiry:** call side $265/$280 (+$4.49), put side $240/$225 (+$4.76);
  shorts bracket the $250–$255 pin with buffer, wings at the squeeze level ($280)
  and below the $239–$244 base ($225) `[STRUCT:gex][DP:largest]`
- **Net credit:** ≈ **$9.25** · **Breakevens:** **$230.75 / $274.25** · **Max
  loss:** $5.75 (one side, $15 width − credit)
- **Why:** this is the **regime-prescribed expression** ("iron condors in range,"
  `[MACRO:MarketRegime_2026-05-29 UW]`), monetizes the rich front IV (phase-4
  backwardation), and profits across the **$240–$265 pin zone** the whole desk
  converged on — comfortably containing the ±$6.3 1σ move. **Size so max loss
  ≤ 1.0% of book.** Preferred over the naked-short-vetoed directional bet.

## Macro overlay (cite phase-6)

- **Tailwinds (for the underlying, *headwinds* for the fade):** Tech sector flow
  leadership, persistence 1/1 `[MACRO:SectorFlowPersistence_2026-05-29 UW]`
  (SNOW a beneficiary — this is why the fade is defined-risk, not naked); easing
  cycle `[MACRO:DFF_2026-05-28 FRED]`.
- **Headwinds:** regime **TRANSITIONAL "half size, iron condors in range"** + weak
  breadth 36% `[MACRO:MarketRegime_2026-05-29 UW]`; nosebleed valuation P/S 17.6 /
  fwd PE 97 `[FUND:peer_pe fz]`.
- **Net:** mixed — sector tailwind for the name, but the regime + valuation + pin
  favour the defined-risk range/fade.

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|------|-------|------------------|
| 2026-05-27 (PASSED) | Q1 FY2027 earnings — **beat, AI growth** | + (in the tape; IV crushed) |
| ~mid-Jun | May CPI release | ? (sector rate beta) |
| ~early-Jun | May NFP | ? (sector rate beta) |
| 2026-08-26 | next SNOW earnings (**outside window**) | n/a |

No idiosyncratic SNOW catalyst before June-18 expiry — the fade/range is pure
post-earnings digestion, no event gap risk to the structures.

## Post-trade monitoring checklist

- [ ] Re-check **dark-pool mega-tier buy_ratio** daily — a flip to net buyer
      (>0.55) means distribution is over; close the fade.
- [ ] Watch **$262 and $280.67** — a sustained close above $262 is the squeeze
      invalidation (dealer short-call hedge-buying); cut/cover the call side.
- [ ] Re-check **GEX/pin** on the phase-4 refresh — if the $255 wall erodes and
      gamma thins, the pin (and the trade) is weakening.
- [ ] Track **price-vs-flow divergence** — if it resolves bullish (flow confirms
      the highs), the fade thesis is broken.
- [ ] Monitor **breadth / regime** — a broad RISK_ON melt-up overruns single-name
      pins; reduce the short-call side.

## Citations summary

1. `[DP:block-stratified]` — dark-pool **mega tier net seller, buy_ratio 0.401**
   (516K sold vs 345K bought) — phase-2-dark-pool.md §Tier breakdown.
2. `[STRUCT:gex]` — **long gamma +$35.2M, walls $255 (+$9.1M) / $250 (+$7.2M),
   pinned** — phase-4-structure.md §GEX.
3. `[INSIGHT:price-vs-flow]` — **bearish divergence, "price +77.5% but flow
   bearish"** — phase-7-insights.md §Price vs flow.
4. `[HIST:rsi fz]` — **RSI 86.9, +53.8% above SMA20** (parabolic) —
   phase-5-historical.md §Price context.
5. `[SENT:recom fz]` — **Recom 1.40 strong-buy, PT flood $285–$325** (crowded-long
   euphoria) — phase-7c-sentiment.md.
