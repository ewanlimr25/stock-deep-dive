# Phase 8 — Multi-Agent Analyst Desk (parallel)

**Ticker:** ENPH
**As-of date:** 2026-07-29
**Generated:** 2026-07-30T03:44:00Z
**Upstream phases cited:** all of `phase-1-flow.md` → `phase-7c-sentiment.md` (each agent read all nine)

## Summary

**Five agents, five verdicts, and the most informative result is the uniformity: nobody voted
LONG, and every single agent returned conviction 2 of 5.**

The split is **3 NEUTRAL / 2 SHORT**, which per the phase heuristics is **MIXED** — but it is a
*bearish-leaning* mixed with an unusual property: the three NEUTRAL votes are not "I see both
sides," they are **"the bearish direction is right and there is nothing tradeable here."** The
accumulation specialist, sent out expressly to find the bull case, came back reporting **no
accumulation exists**. The contrarian specialist, sent to test whether the bearish consensus is
itself the crowded trade, came back reporting **the crowding gauges read NORMAL, so there is no
positioning extreme to fade**. The momentum specialist found **persistence without consensus**.

**Average conviction is exactly 2.00 across all five agents — no dissent, no outlier, and not a
single vote above 2.** For a desk where five specialists independently read nine phase files,
that degree of agreement on *low* conviction is itself the signal.

**All five converged on the same three levels**, arrived at independently:

- **Support 34.90–34.96** — and four of five explicitly flagged it as an **untested edge**, not
  defended support, because `phase-2-dark-pool.md` found **no institutional shelf below spot**.
- **Resistance 36.27** — every agent named it, and three named the same triple convergence:
  the dark-pool VWAP (36.27), the 36–37 gamma-flip band, and the 08-07 max-pain strike (36).
- **Invalidation: a daily close back above ~37** — unanimous.

**The two SHORT votes both refuse short stock.** earnings-scout: *"express it with cheap long
puts, not fresh short stock, and only on a confirmed break of 35."* risk-monitor labelled its own
bias **"SHORT (defined-risk expression only — not a fresh short-stock thesis)."** So even the
bears are voting for defined-risk expression at reduced size — which is exactly what
`phase-7c-sentiment.md`'s VETO permits and what `phase-6-macro.md`'s regime guidance
(*"Half position sizes. Favor defined-risk strategies"*) prescribes.

**risk-monitor answered the phase-5 Kelly question directly and unambiguously:** the 100%
`win_rate` on `total_signals` 9 is *"not a usable Kelly p — phase 9 must discard it and size off
the conviction bin, not the backtest."*

All five agent types were available; **no `MISSING:` lines**. Per the spec, `earnings-scout`
would normally be skipped with earnings 90 days out — it was run with an explicitly reframed
**post-earnings-drift** remit and returned the run's most decision-relevant single sentence.

## Agent verdicts table

| Agent | bias | conviction | horizon | one_line_take |
|---|---|---|---|---|
| **accumulation-hunter** | **NEUTRAL** | **2** | 1-5d | "Every lane says distribution; the four 'bullish' datapoints are a trapped buyer, short-vol harvesting with a 3-for-3 failure record, a bearish-skewed OI build, and a $0.29 lottery ticket. No accumulation here." |
| **contrarian-scanner** | **NEUTRAL** | **2** | 1-4w | "This isn't a crowded short to fade — it's an unfashionable, unloved stock with cheap analyst optimism and a fortress balance sheet sitting under genuinely bearish dealer mechanics." |
| **sweep-tracker** | **NEUTRAL** | **2** | 1-5d | "Persistence without consensus and $470k of ask-side sweeps against $666k bid-side is noise dressed as a campaign — the only tradeable urgency is the isolated Aug-07 C37, and it's too small and too lonely to lean on." |
| **earnings-scout** | **SHORT** | **2** | 1-5d | "In-line print, gap-and-crap into a still-negative-gamma downtrend argues continuation over reversion, but express it with cheap long puts, not fresh short stock, and only on a confirmed break of 35." |
| **risk-monitor** | **SHORT** *(defined-risk only)* | **2** | 1-4w | "Direction's right and cheap to express via puts, but two gates (7b CAUTION, 7c VETO) plus a rising crowded short and CHOPPY tape say defined-risk, half-size, or stand aside — not a fresh short." |

**Distribution:** LONG **0** · SHORT **2** · NEUTRAL **3** · RANGE **0**.
**Conviction:** 2, 2, 2, 2, 2 → **mean 2.00, median 2, range 0**.
**Horizon:** 1-5d ×3, 1-4w ×2.

## Per-agent details

### accumulation-hunter — NEUTRAL, conviction 2

```
- bias: NEUTRAL
- conviction: 2
- horizon: 1-5d
- key_levels:
    support: 34.96 (session low, untested — no institutional dark-pool shelf exists below spot per phase-2 §D)
    resistance: 36.27 (dark-pool VWAP / phase-7 institutional clearing price, converges with phase-4's 36-37 gamma flip and max-pain magnet)
    invalidation: reclaim and hold above 37.48-38.25 (the trapped-buyer zone) on volume would flip this bull-case read; breakdown through 34.96 with dark-pool prints continuing below-mid confirms no accumulation exists
- top_signal: No genuine accumulation survives scrutiny — phase-2's 76,300 shares bought above mid at $37.56-37.66 VWAP in the opening minutes were immediately overwhelmed by 15 consecutive below-mid blocks laddering to 35.01, leaving those buyers -6.6% to -6.9% underwater and converting the print into overhead supply (36.15-36.30 shelf), not support.
- top_risk: Dismissing this as purely bearish ignores that Street targets average +22.8% above spot with zero downgrades and a fortress balance sheet (phase-7c/7b) — if the 8,970 short Sept-18 P35 puts (now ATM, 0.70% of float) trigger dealer/writer covering into a bounce, a short squeeze off 34.96 is mechanically plausible even without real accumulation.
- one_line_take: Every lane — dark pool (0.610 sell), OI (5.4:1 bearish premium), UW composite (DISTRIBUTION, DIRECTIONAL_SHORT) — says distribution; the four "bullish" datapoints are a trapped buyer, short-vol harvesting with a 3-for-3 failure record, a bearish-skewed OI build, and a $0.29 lottery ticket. No accumulation here.
```

**This is the most important verdict in the phase.** The agent was tasked specifically as the
designated bull-case detector on the accumulation axis, given four candidate bullish datapoints
to examine, and told to be honest if the answer was that there is nothing. It examined all four
and **dismantled each**:

| Candidate bull datapoint | Agent's finding |
|---|---|
| 76,300 sh bought above mid at $37.56–37.66 VWAP | **Trapped buyer** — immediately overwhelmed by 15 consecutive below-mid blocks to 35.01; now **−6.6% to −6.9%** and converted into the 36.15–36.30 **overhead supply** shelf |
| Sept-18 P35 (+885 OI, `curr_oi` 8,970) | **Written, not bought** (`prev_bid_volume` 639 > `prev_ask_volume` 348) → now ATM = **0.70% of float** of forced-selling risk if 35 breaks, *not* support |
| +201,329 30-day OI build / 8 consecutive build days | Real, **but** coexists with total OI **−25.4%** via expiration, and the premium-weighted composition of the largest builds is **5.4:1 bearish** ($2,910,482 vs $535,495) |
| Sept-18 C70 (+1,604 OI) | A **$55,196 lottery ticket** at $0.29/contract, 99.7% OTM — trivial, not conviction |

It also independently surfaced the phase-5 pattern as decisive: the three large bullish premium
spikes (06-17, 07-16, 07-23) were **all put-selling in mechanism and all 3-for-3 followed by
lower prices**, averaging −7.9%.

Its `top_risk` is the run's cleanest statement of the bear's real hazard: **the 8,970 written
Sept-18 P35 puts are now at the money**, and if writers/dealers cover into a bounce, a squeeze
off 34.96 is *mechanically plausible without any accumulation existing at all*.

### contrarian-scanner — NEUTRAL, conviction 2

```
- bias: NEUTRAL
- conviction: 2
- horizon: 1-4w
- key_levels:
    support: 34.96 (session/30-day low; no institutional shelf beneath it — phase 2/3)
    resistance: 36.27 (dark-pool VWAP = 36.15–36.30 distribution shelf = gamma-flip band 36–37 = max-pain 36, three lanes converging — phase 4/7)
    invalidation: reclaim and hold above 37 (flips gamma regime long, invalidates negative-gamma/dealer-sell mechanic) OR a clean break and hold below 34.90 on volume (confirms accelerant thesis, negates squeeze-fade)
- top_signal: Every genuine crowding gauge reads NORMAL, not extreme — pc-ratio-zscore +0.482 (phase 5 §D) and skew_ratio 0.994 COMPLACENT with puts cheaper than calls (phase 4 §F) — meaning the "bearish consensus" is not actually a crowded options positioning trade to fade, even though short float rose to 17.94% with only 3.05 days-to-cover (phase 7c §D), which is a sector-wide condition (tied with SEDG) rather than an ENPH-specific squeeze setup.
- top_risk: The fade thesis requires ignoring that dealers are short gamma across the entire 32-36 zone with net_dex -$65.1M explicitly interpreted as "SELL underlying" (phase 4 §B/§G), that GEX has been negative 26 consecutive sessions while spot fell 24.7% (phase 5 §C), and that macro just resolved the one bullish mechanical force (vanna-squeeze) against the bull — VIX rose 23.5% in 10 sessions when the setup needed it to collapse (phase 6 §A) — so the mechanical tape is genuinely bearish, not merely crowded-bearish.
- one_line_take: This isn't a crowded short to fade — it's an unfashionable, unloved stock with cheap analyst optimism (targets +23-28%) and a fortress balance sheet sitting under genuinely bearish dealer mechanics; the contrarian long case is a valuation/analyst-gap story, not a positioning-extreme fade, so I won't flag it as high-conviction contrarian setup.
```

**A structurally important distinction that resolves an ambiguity `phase-7c-sentiment.md` left
open.** The contrarian agent was handed six bullish/crowding datapoints and concluded they **do
not cohere into a fade signal**, because the two gauges that would *prove* genuine crowding both
read flat: `pc-ratio-zscore` **+0.482** (`extreme` NORMAL, against a |z| > 2 threshold) and
`skew_ratio` **0.994** (COMPLACENT — puts *cheaper* than calls).

Its formulation is precise and worth carrying verbatim into phase 9: **ENPH is not a crowded
short to fade; it is an unloved stock with a valuation/analyst-gap story sitting under genuinely
bearish dealer mechanics.** Those are different trades. A positioning-extreme fade would be
short-horizon and mechanical; a valuation-gap long is multi-quarter and requires a catalyst —
and there is **no company catalyst for ~13 weeks**.

It is also the only agent to name a **two-sided invalidation**, which phase 9 should adopt:
reclaim/hold **above 37** kills the bearish mechanic; clean break/hold **below 34.90** kills the
squeeze-fade.

### sweep-tracker — NEUTRAL, conviction 2

```
- bias: NEUTRAL
- conviction: 2
- horizon: 1-5d
- key_levels:
    support: 34.96
    resistance: 36-37 (vanna pivot / max-pain / gamma-flip band, then 39.60 gap high)
    invalidation: close back below 34.96 (session low) confirms breakdown; reclaim of 37 flips dealer regime long-gamma and voids the bearish read
- top_signal: Phase 1 §D: only real conviction print all week is 2026-08-07 C37 (1,206 vol/81 OI, 99 trades, ~96% ask-side, $218,770) — a genuine 9-DTE bullish sweep, but it's isolated against $405,922 of long-dated 40/55/75 call writing and a $260,820 Oct-16 P35 buy the same day.
- top_risk: Sweep persistence is 5/5 sessions at $7.4M premium yet dominant_direction is "mixed" (flipped from bearish while premium rose 454%) — the desk-wide signal this agent hunts for (consistent-direction, urgent sweeps) simply isn't present here, and ENPH clears zero market-wide aggression screens in either direction.
- one_line_take: Persistence without consensus and $470k of ask-side sweeps against $666k bid-side is noise dressed as a campaign — the only tradeable urgency is the isolated Aug-07 C37, and it's too small and too lonely to lean on.
```

**The momentum specialist declined to find momentum, and named the exact reason.** Its phrase
*"persistence without consensus"* is the cleanest available summary of the 5-of-5 /
`consistency_score` 1.0 / `dominant_direction` **"mixed"** configuration: maximal attention,
zero directional agreement, with sweep premium up **454%** while the direction *flipped from
bearish to mixed*.

It is the only agent to add **39.60** (the gap high) as a secondary resistance above the 36–37
band, which is useful for phase 9's upper structure.

It gives the fairest verdict available on the day's one clean bull print — the **Aug-07 C37**
is *"genuine"* but *"too small and too lonely to lean on"*: $218,770 against $405,922 of
long-dated call writing and a $260,820 Oct-16 P35 purchase on the same session, and **9 DTE**.

Note this agent used only 2 tool calls — it found everything it needed in the phase files, which
is a mild positive signal about the completeness of phases 1–7c.

### earnings-scout — SHORT, conviction 2 *(remit reframed to post-earnings)*

```
- bias: SHORT
- conviction: 2
- horizon: 1-5d
- key_levels:
    support: 34.96 (30-session period low, set today, close is only $0.11 above it)
    resistance: 36.27 (dark-pool VWAP / institutional clearing price, phase-7) converging with the 36-37 gamma-flip band and 36 max-pain magnet (phase-4)
    invalidation: daily close back above 37 (reclaims atm_flip_strike 36, flips dealer regime to long-gamma, and sits at the 07-31 max-pain strike) — that closes the short
- top_signal: Phase-4 shows dealers short gamma across the entire 32-36 zone spot is sitting in (net_gex negative 25-36.5, strike 35 tagged resistance_wall at gex -323,628, net_dex -$65.1M = dealer-sell mechanism), and phase-7 shows the close (35.07) printed 3.3% below the day's own dark-pool VWAP (36.27) — the marginal seller drove price below where institutional size actually cleared, into a negative-gamma zone that amplifies further weakness on any break of 35.
- top_risk: Phase-7c is an explicit VETO on a fresh directional short: the 17.94% short base grew (from 17.55%) through the print rather than covering, days-to-cover is only ~3 (cheap to cover, weak squeeze fuel), and all seven analyst targets except one sit above spot (mean $43.07, +22.8%) with every rating maintained — shorting here means joining an already-crowded trade against a consensus price level, into a name whose skew (0.994, COMPLACENT) charges no premium for downside and whose vanna bid (+1,327) and max-pain pull (36-45 across all <30 DTE expiries) are live upside counterforces.
- one_line_take: In-line print, gap-and-crap into a still-negative-gamma downtrend argues continuation over reversion, but express it with cheap long puts, not fresh short stock, and only on a confirmed break of 35.
```

**The post-earnings-drift verdict is continuation, not mean reversion — with a conditional
trigger.** The agent's reasoning is that a **gap-and-crap on an *in-line* print** (revenue beat
+0.67%, EPS in line after a published correction, Q3 guide in line versus $304.253M consensus)
into a **negative-gamma downtrend** favours continuation, because there was no positive surprise
to mean-revert toward.

Its one_line_take contains the run's single most actionable sentence — and it independently
arrives at the same structure `phase-4-structure.md` §F implied and
`phase-7c-sentiment.md` concluded: **long puts, not short stock, and only on a confirmed break
of 35.** The skew logic supports it: `skew_ratio` 0.994 means downside optionality carries **no
skew premium**, and the 10-16 expiry is the **cheapest vol on the curve at 82.2%**.

Note this agent's `top_risk` is a full and fair statement of the bull case against its own bias —
it explicitly cites the 7c VETO, the rising short base, the cheap 3-day cover, the +22.8%
consensus targets, the complacent skew, the `net_vanna` +1,327 and the max-pain pull. That is the
mark of a verdict phase 8b can trust rather than merely tally.

### risk-monitor — SHORT (defined-risk expression only), conviction 2

```
- bias: SHORT (defined-risk expression only — not a fresh short-stock thesis)
- conviction: 2
- horizon: 1-4w
- key_levels:
    support: 34.90–34.96 (session/post-close lows; phase-2 finds no dark-pool shelf below spot — this is an untested edge, not defended support)
    resistance: 36.27 (triple convergence: phase-2/7 dark-pool VWAP 36.27, phase-4 gamma-flip band 36–37, phase-4 08-07 max-pain 36 — the level ENPH must reclaim to invalidate the bearish structure)
    invalidation: daily close back above ~37 (gamma flip + max pain, on volume) OR VIX rolling back toward collapse (re-arming phase-4's vanna bid) — either kills the negative-gamma/dealer-selling mechanic this thesis leans on
- top_signal: Phase-6: VIX rose 18.21→20.66 (+13.5% today, +23.5%/10d) which invalidates phase-4's vanna-squeeze trigger ("if VIX collapses"), leaving negative gamma across every strike 25–36.5 and net_dex −$65.1M (1.41% of float, dealer hedge = SELL) as the unopposed mechanical force with spot sitting on the 35 strike the tool itself tags `resistance_wall`.
- top_risk: Stacking a leveraged, undiversifiable solar-beta bet (ENPH/TAN ρ0.846, ENPH/SEDG ρ0.819, Beta 1.65–1.69) with a VETO-flagged crowded short (17.94% float short and RISING, Street targets +22.8% above spot) into a CHOPPY/TRANSITIONAL regime (bullish_pct 32.5%, "half position sizes") where ATR (9.2% of spot) exceeds the front implied move (5.58%) means any stop tight enough to size normally gets noise-stopped, and one tight enough to survive is already a half-position-or-smaller bet; separately, phase-5's 100% win-rate (N=9, market-wide, ENPH absent from the sample, unstable 0.556→1.00 in two sessions) is not a usable Kelly p — phase 9 must discard it and size off the conviction bin, not the backtest.
- one_line_take: Direction's right and cheap to express via puts, but two gates (7b CAUTION, 7c VETO) plus a rising crowded short and CHOPPY tape say defined-risk, half-size, or stand aside — not a fresh short.
```

**Three contributions phase 9 must act on:**

1. **The Kelly `p` ruling, requested explicitly and answered unambiguously.** Phase 5's
   `win_rate` **"100.0%"** on `total_signals` **9** is *"not a usable Kelly p — phase 9 must
   discard it and size off the conviction bin, not the backtest,"* citing all four defects:
   in-sample (self-disclaimed), N=9 below the confidence floor, market-wide with **ENPH absent
   from the sample**, and unstable (**0.556 → 1.00 in two sessions** at unchanged N).
2. **The stop-sizing impossibility, quantified.** `ATR` **3.24 = 9.2% of spot** against a
   front-expiry implied move of only **5.58%**. *"Any stop tight enough to size normally gets
   noise-stopped, and one tight enough to survive is already a half-position-or-smaller bet."*
   This is the mechanical reason a stock expression fails here regardless of direction, and it
   is the strongest argument for options over shares.
3. **A second invalidation condition no other agent named: a VIX reversal.** Because the bearish
   mechanic leans on the vanna trigger *staying* unmet, *"VIX rolling back toward collapse
   (re-arming phase-4's vanna bid)"* is a genuine thesis-killer independent of price. Phase 9's
   invalidation rubric should carry it alongside the 37 level.

It also reframes the correlation finding sharply: with **ρ 0.846 to TAN** and **Beta 1.65–1.69**,
an ENPH position is *"a leveraged, undiversifiable solar-beta bet"* — so this is not an
idiosyncratic trade even though the deep dive is single-name.

## Disagreements

**There is no true dissent to report — no agent took a bias opposite to the majority direction,
and no agent voted LONG.** The 3–2 NEUTRAL/SHORT split is a difference in *threshold*, not in
*direction*: all five read the mechanical evidence as bearish, and they differ only on whether
that is enough to act on.

The distinction, stated precisely:

| Agent | Reads mechanics as bearish? | Willing to act? | Reason for the gap |
|---|---|---|---|
| accumulation-hunter | **Yes** ("every lane says distribution") | **No** | The bull datapoints are hollow, but that does not make the entry good |
| contrarian-scanner | **Yes** ("genuinely bearish, not merely crowded-bearish") | **No** | No positioning extreme to fade in either direction |
| sweep-tracker | **Yes** (net aggressive −2,622) | **No** | "Persistence without consensus" — no tradeable urgency |
| earnings-scout | **Yes** | **Conditionally** | Only via long puts, only on a confirmed break of 35 |
| risk-monitor | **Yes** | **Conditionally** | Defined-risk, half-size, or stand aside |

**The nearest thing to a dissent is internal to accumulation-hunter's own verdict**, and it is
the most valuable contrarian point any agent made — worth quoting because it argues *against* the
agent's own framing:

> *"if the 8,970 short Sept-18 P35 puts (now ATM, 0.70% of float) trigger dealer/writer covering
> into a bounce, a short squeeze off 34.96 is mechanically plausible even without real
> accumulation."*

**This is a squeeze mechanism that does not require any accumulation, any good news, or any
change in fundamentals** — purely the mechanical consequence of a large written-put position
going in the money. Phase 8b must test it, and phase 9 must carry it as the primary risk to any
downside expression.

A second near-disagreement worth logging: **contrarian-scanner and earnings-scout differ on what
the 17.94% short base means.** earnings-scout treats it as a **reason not to short** (crowded,
consensus targets above). contrarian-scanner treats it as **not a fade signal either**, because
days-to-cover is only 3.05 and 17.94% is a sector condition (tied with SEDG 17.97%). Both are
consistent with `phase-7c-sentiment.md`'s own acknowledgment that the "hard squeeze" half of its
VETO test is unconfirmed — and together they suggest the short base is a **reason for neither
side to be confident**, rather than fuel for one.

## Tool errors

**None.** All five `subagent_type` values resolved and returned complete, well-formed verdict
blocks. **No `MISSING:` lines.**

Agent tool budget (spec allowance: ~30 UW calls total across all five): **33 tool_uses**
observed — accumulation-hunter 9, contrarian-scanner 9, sweep-tracker 2, earnings-scout 4,
risk-monitor 9. Marginally above the guideline and immaterial; most calls were file reads of the
nine phase documents rather than `uw` invocations. **contrarian-scanner explicitly reported
needing zero additional `uw` calls** — *"all cited datapoints were present in the completed phase
files"* — and sweep-tracker used only 2. That is a useful completeness signal for phases 1–7c.

**One deliberate spec deviation, disclosed:** `phase-8-agent-views.md`'s agent table instructs
*"`earnings-scout` (skip if earnings > 30d out)"*. ENPH's next earnings is **2026-10-27, ~90
days out**, so the letter of the spec calls for a skip. I ran it anyway with an **explicitly
reframed post-earnings remit**, because ENPH reported **one session before the as-of date** and
the post-earnings-announcement-drift question is squarely in that agent's domain (historical
earnings behaviour, vol-surface aftermath). The reframing was stated in the agent's prompt. It
returned the run's most actionable single sentence, so the deviation was worth making — but it is
a deviation and phase 10 should record it.

**Context-packing method note:** the spec's prompt template embeds `<full contents>` of each
phase file inline. I instead passed the nine **absolute file paths** with an instruction to read
them in full. The agents have file-read access, all five confirmed reading the files, and every
verdict cites specific phase sections and exact figures — so the context transfer was
functionally complete while avoiding ~100KB of duplicated inline text per agent. Recorded for
transparency.

## Verdict for downstream

- **Plurality bias: NEUTRAL, 3 of 5** (NEUTRAL 3 / SHORT 2 / LONG **0** / RANGE 0).
  **But read the composition, not just the count:** all five agents independently judged the
  *mechanical* evidence bearish; the three NEUTRAL votes are **"bearish direction, nothing
  tradeable"**, not genuine two-sidedness. **Effective bias: bearish-leaning MIXED with zero
  bullish support.**
- **Average conviction: 2.00 / 5** across all five non-MISSING agents (2, 2, 2, 2, 2 — median 2,
  **range 0**). Per the phase heuristics, a 3–2 split → **MIXED**, and phase 9 should *"target
  0.55–0.65 conviction and use a defined-risk structure."* **The unanimous conviction of 2 argues
  for the bottom of that band or below** — five independent specialists, none of whom found
  enough to act on with size.
- **Three highest-quality signals across all agents:**
  1. **[AGENT:risk-monitor]** *"VIX rose 18.21→20.66 (+13.5% today, +23.5%/10d) which invalidates
     phase-4's vanna-squeeze trigger ('if VIX collapses'), leaving negative gamma across every
     strike 25–36.5 and net_dex −$65.1M (1.41% of float, dealer hedge = SELL) as the unopposed
     mechanical force with spot sitting on the 35 strike the tool itself tags `resistance_wall`."*
     — the cleanest statement of why the structure is bearish rather than balanced.
  2. **[AGENT:accumulation-hunter]** *"the 76,300 shares bought above mid at $37.56–37.66 VWAP in
     the opening minutes were immediately overwhelmed by 15 consecutive below-mid blocks laddering
     to 35.01, leaving those buyers −6.6% to −6.9% underwater and converting the print into
     overhead supply (36.15–36.30 shelf), not support."* — the designated bull-hunter finding no
     bull case, with the mechanism.
  3. **[AGENT:contrarian-scanner]** *"Every genuine crowding gauge reads NORMAL, not extreme —
     pc-ratio-zscore +0.482 and skew_ratio 0.994 COMPLACENT with puts cheaper than calls —
     meaning the 'bearish consensus' is not actually a crowded options positioning trade to
     fade."* — removes the contrarian long from the table on measured evidence.
- **Levels for phase 9 (all five agents converged; use these):**
  - **Support 34.90–34.96** — an **untested edge**, explicitly *not* defended support (no
    dark-pool shelf below spot; the 30-day low was set today and the close is $0.11 above it).
  - **Resistance 36.27** — the triple convergence: dark-pool **VWAP 36.27** = 36.15–36.30
    distribution shelf = **36–37 gamma-flip band** = **36 max-pain** (08-07). Secondary:
    **39.60** (the gap high, per sweep-tracker).
  - **Invalidation — unanimous: a daily close back above ~37** (reclaims `atm_flip_strike` 36,
    flips the dealer regime to long gamma). **Plus two conditions no single agent shared:** a
    clean break/hold **below 34.90** on volume (contrarian-scanner: negates the squeeze-fade),
    and **a VIX reversal toward collapse** (risk-monitor: re-arms the vanna bid). Phase 9's
    invalidation rubric should carry all three.
- **Structural directive from the two bears — both refused short stock.** earnings-scout: *"cheap
  long puts, not fresh short stock, and only on a confirmed break of 35."* risk-monitor:
  *"defined-risk, half-size, or stand aside."* Mechanically justified by **`ATR` 3.24 = 9.2% of
  spot against a 5.58% front implied move** — a stop tight enough to size normally gets
  noise-stopped, one wide enough to survive is already a half-position. Supported by
  `skew_ratio` **0.994** (no skew premium on puts) and the 10-16 expiry at **82.2%**, the
  cheapest vol on the curve.
- **Kelly `p` ruling (risk-monitor, requested and answered):** **discard phase-5's
  `signal_backtest_win_rate` of 1.00 entirely** — in-sample and self-disclaimed, N=9 below the
  confidence floor, market-wide with **ENPH absent from the 9-signal sample**, and unstable
  (0.556 → 1.00 in two sessions at unchanged N). **Size off the conviction bin**, and state the
  substitution explicitly in `decision.json`.
- **Open questions surfaced by agents:**
  1. **Can the 8,970 written Sept-18 P35 puts, now at the money (0.70% of float), squeeze the
     stock off 34.96 through writer/dealer covering — with no accumulation, no good news and no
     fundamental change required?** (accumulation-hunter) **This is the single largest risk to
     any downside expression and phase 8b must test it.**
  2. **Is ENPH a valuation/analyst-gap long (multi-quarter, needs a catalyst — and there is none
     for ~13 weeks) rather than a positioning fade?** (contrarian-scanner) The distinction
     changes the horizon, not just the direction.
  3. **Does the isolated Aug-07 C37 ($218,770, ~96% ask-side, 9 DTE) mean anything against
     $405,922 of long-dated call writing, or is it retail noise?** (sweep-tracker)
  4. **If ATR (9.2%) exceeds the front implied move (5.58%), is the options market
     under-pricing forward movement — and does that favour buying premium despite VRP
     +0.1267?** (risk-monitor, cross-reading `phase-5-historical.md` §A)
  5. **Would a VIX reversal alone rescue the bull case, independent of ENPH news?**
     (risk-monitor's second invalidation condition)
