# Phase 8 — Multi-Agent Analyst Desk

**Ticker:** ENPH
**As-of date:** 2026-07-27
**Generated:** 2026-07-27T22:30:00-04:00
**Upstream phases cited:** `phase-0.5-context.md`, `phase-1-flow.md`, `phase-2-dark-pool.md`, `phase-3-positioning.md`, `phase-4-structure.md`, `phase-5-historical.md`, `phase-6-macro.md`, `phase-7-insights.md`, `phase-7b-fundamentals.md`, `phase-7c-sentiment.md`

## Summary

**Five agents ran; all five returned; not one is SHORT.** That is the headline.
Every phase from 1 through 7 carried a bearish flow bias, and the desk — given
that same evidence — declined to short it. The verdict is **4× NEUTRAL, 1× LONG,
0× SHORT**, average conviction **2.2 / 5**.

**The single most valuable output is a fact the previous four phases could not
obtain.** Phases 4, 5, 6 and 7b each deferred the question *"how large were ENPH's
actual earnings-day moves?"* — Finnhub carries no price reaction, the local
74-session snapshot contains no prior ENPH earnings date, and the estimate
endpoints are paid. **`earnings-scout` recovered two of the last four via
WebSearch, and I verified the larger one independently:**

- **2026-02-04 (Q4'25): +39%** — *"Strong Guidance Ignites Vicious Short Squeeze"*
- **2026-04-28 (Q1'26): −9.1%**

**Against tomorrow's 12.25% implied move, those are 3.2× and 0.74× — a mean
absolute reaction of ~24%, roughly 2× what the market is charging.** This inverts
the naive read of "170% IV = expensive". It also means the February setup —
guidance beat detonating a crowded short base — is **structurally available
again**, with short interest at 17.55% **and rising** (`phase-7c-sentiment.md`).

The agents converge tightly on levels: **$35.00 support** (3 of 5) with a
**$36.21–36.70** secondary shelf, and **$42.50 resistance** (4 of 5) — the
five-method confluence already established in phases 3/4/5/7b. Every agent
independently flags that **no stop inside ±12.25% survives the gap**.

## Agent verdicts table

| Agent | bias | conviction | horizon | one_line_take |
|---|---|---|---|---|
| **accumulation-hunter** | **NEUTRAL** | 2 | 1-5d | *"Every 'accumulation' print in this tape is a closing auction, a floor cross, or a placeholder empty bucket — nobody institutional is quietly building ENPH into earnings, they're selling wings and going home."* |
| **contrarian-scanner** | **LONG** | 3 | 1-5d | *"No options-tape extreme to fade — the crowd is short the stock, not the options, and it's adding into an armed vanna squeeze with two gates vetoing a fresh short; trade the squeeze with cheap calls into $42.50, size small, let flat skew buy your tail insurance rather than sell it."* |
| **sweep-tracker** | **NEUTRAL** | 1 | intraday | *"Real 5-day bearish sweep campaign, but too small to trade and dwarfed by tomorrow's ±12.25% binary — direction is right, size is irrelevant, stand aside until the print clears."* |
| **earnings-scout** | **NEUTRAL** | **4** | 1-5d | *"170% IV is arithmetic, not richness — history says ENPH gaps 2-3x the priced move either way; buy the front-week straddle/strangle, don't sell it, and don't fade the tape into a fundamentals+positioning double-veto."* |
| **risk-monitor** | **NEUTRAL** | 1 | 1-5d | *"No-touch on stock size: dual VETO plus FULLY_NEGATIVE gamma into stacked binaries means the only defensible expression is small defined-risk long optionality, not directional stock."* |

**Distribution:** NEUTRAL 4 · LONG 1 · SHORT **0** · RANGE 0.
**Average conviction: 2.2 / 5** (2, 3, 1, 4, 1).

⚠️ **Read "NEUTRAL" carefully — it does not mean "no view" here.** Three of the
four NEUTRAL agents are *direction*-neutral while holding a definite view on
*volatility* or *sizing*. `earnings-scout` is NEUTRAL on direction at
**conviction 4** — the highest in the desk — because its call is explicitly
**long volatility, both ways**. Collapsing these to "the desk has no opinion"
would misread the phase.

## Per-agent details

### accumulation-hunter — NEUTRAL (2)

```
- bias: NEUTRAL
- conviction: 2
- horizon: 1-5d
- key_levels:
    support: $36.70 (phase-2 most-transacted DP level, 9 trades; also recent swing-low
             close and near the 30d low $36.21 from phase-7 price-vs-flow)
    resistance: $40.55-$40.67 (phase-2 genuine multi-trade DP supply cluster) /
                $42.50 (phase-3 only genuine near-term OI call wall, zero puts, 3,735)
    invalidation: 2026-07-28 postmarket print — implied move ±12.25% ($33.36-$42.66)
                  dwarfs every level above; no dealer gamma structure holds price inside
                  it (phase-3: earnings expiry 6.98% of OI, ~2,000 contracts inside the
                  move, ENPH absent from pin-risk)
- top_signal: No accumulation signal survives — phase-7's DuckDB reclassification
  reproduces UW's own institutional-accumulation buy/sell volumes exactly
  (216,974/99,381, buy_ratio 0.686) and then shows 129,000 of those "buy" shares are the
  single 16:00:30 closing-auction cross; stripping it drops buy_ratio to 0.450 (55% sell),
  corroborated by phase-2's independent NBBO aggressor split (hit% 20.3 > lift% 15.2,
  4-of-6 sessions) and the block-stratified large tier (0.555, n=36).
- top_risk: The one print that looked like genuine footprint — the 800-lot Nov-20 $35 put
  + 28,800-share dark-pool hedge phase-2 flagged as "customer bought puts" — is confirmed
  a floor-cross delta-neutral package by phase-3 (OI moved only 407→412, {futures_floor}/
  slft), so even the strongest single-print evidence is a wash.
```

**Assessment:** it was asked to *test* phases 2/3/7's conclusions rather than
restate them, and it did — independently reproducing the reclassification
arithmetic and confirming both corrections. **No dissent; both corrections hold.**

### contrarian-scanner — LONG (3) — the sole dissent

```
- bias: LONG
- conviction: 3
- horizon: 1-5d
- key_levels:
    support: 36.70 (most-transacted DP level / recent swing-low close;
             secondary $35 put wall)
    resistance: 42.50 (largest positive gamma +703,006 = only genuine near-term call
                wall = SMA20 ≈$42.76 = $42.00 median analyst target)
    invalidation: close below $35.00 (put_wall_support, −7.92%) on volume — that level
                  breaking confirms the crowd short is right, not crowded
- top_signal: phase-4's net_vanna=+913 with front-week IV certain to crush 170%→~90%
  post-print forces the short-put dealer book to BUY as soon as the event clears, and it
  is arming into a short base that phase-7c shows is RISING (15.09M→16.79M shares,
  17.55-17.94% of float) rather than covering — the crowd is adding to the short at the
  exact moment the dealer mechanics flip bullish.
- top_risk: FULLY_NEGATIVE gamma and net_dex=−$40.3M mean if ENPH gaps down, dealers sell
  into the move and the vanna bid is overwhelmed — the squeeze mechanic is conditional on
  the stock holding/rallying, not a floor; a genuine miss (25D repeal, −20.6% revenue,
  gross margin 47%→35%) breaks $35 and the fade fails outright.
```

**Assessment:** the strongest *reasoned* case in the desk, and it states its own
kill condition precisely. It correctly identifies that there is **no options-tape
extreme to fade** (P/C z −0.037, IV 54.8th self-percentile) and relocates the
crowding to the **stock's short base** — then argues the squeeze mechanics, not
sentiment, are the trade. Crucially it **does not dispute the bearish
fundamentals**; it argues they are already in the price and that the *mechanics*
into the event are asymmetric. Its conviction of 3 (not 4 or 5) reflects honest
acknowledgement that the vanna bid is conditional.

### sweep-tracker — NEUTRAL (1)

```
- bias: NEUTRAL
- conviction: 1
- horizon: intraday
- key_levels:
    support: $35 (put_wall_support, net_gex −502,635)
    resistance: $40 (max-pain magnet in 8/15 expiries, also most negative gamma strike)
    invalidation: any position must close before the 2026-07-28 postmarket print —
                  earnings gap invalidates all pre-event technicals
- top_signal: phase-1 sweep-persistence shows consistency_score=1,
  dominant_direction="bearish", sessions_in_top=5 of 5, total_sweep_premium=$1,335,255 —
  a genuine 5-day directional campaign, not noise.
- top_risk: the campaign is $1.34M against a $5.01B cap (0.027% of market cap) on option
  volume at the 16.4th percentile of ENPH's own history, absent from smart-money-flow and
  sweep-ratio top lists, and the 2026-07-31 expiry prices a flat two-sided 170% IV
  (skew_ratio 1.001) ahead of a ±12.25% binary — any pre-earnings momentum read is erased.
```

**Assessment:** the most self-refuting verdict on the desk, in the best sense.
The sweep specialist confirms its own signal is **real** (5/5, consistency 1.0)
and then **disqualifies it on magnitude** — 0.027% of market cap. This is the
honest answer to the question it was asked and it is the reason phase-1's
conviction was capped at 3/5 with "high-confidence direction, near-zero force."

### earnings-scout — NEUTRAL (4) — highest conviction

```
- bias: NEUTRAL
- conviction: 4
- horizon: 1-5d
- key_levels:
    support: $35.00 (phase-3 put_wall_support, 4,217 puts vs 10 calls ≤30DTE;
             phase-4's second-most-negative GEX strike)
    resistance: $42.50 (five-method confluence)
    invalidation: IV crushes 170%→~90% on the 2026-07-31 expiry with spot pinned near $38
                  (no realized move) — long premium bleeds out with nothing to show;
                  alternatively a close outside $33.36–$42.66 hands the move to
                  FULLY_NEGATIVE gamma with no dealer brake
- top_signal: WebSearch confirms ENPH's last two earnings prints moved +39% (2026-02-04,
  guidance-beat short squeeze) and −9.1% (2026-04-28) — both outside tomorrow's 12.25%
  implied move; phase-5 independently shows implied/ATR=1.46x and implied/RV=2.9x on a
  name that already prints unprompted 5-7% days, so the front week is fairly priced to
  cheap, not the "170% IV" giveaway it looks like.
- top_risk: The earnings expiry holds only 6.98% of OI / ~2,000 contracts inside the
  implied move and ENPH is absent from pin-risk, inside a FULLY_NEGATIVE regime with
  zero_gamma_level=null — no dealer brake — and FOMC lands 2026-07-29 14:00 ET while ENPH
  is still digesting its own gap, doubling path risk before the IV crush completes.
- historical_earnings_moves: 2026-02-04 +39% (Q4'25 beat + guidance raise, short-squeeze),
  2026-04-28 −9.1% (Q1'26, closed $31.19) — via WebSearch (trefis.com, yahoo, investing).
  Only 2 of the last 4 were recoverable; Oct-2025 and Feb-2025 remain unmeasured.
```

**Assessment: the most valuable contribution of the phase**, and the only agent
that added genuinely new primary data. See §Verification below — I confirmed the
+39% independently rather than accepting it. Its `invalidation` is unusually
well-specified: it names the *failure mode of its own trade* (IV crush with no
realized move), which is precisely the risk of buying a 170% front week.

### risk-monitor — NEUTRAL (1)

```
- bias: NEUTRAL
- conviction: 1
- horizon: 1-5d
- key_levels:
    support: $35.00 (put_wall_support / 2nd-most-negative GEX strike, net_gex −502,635;
             floor zone extends to $36.21–36.70 where the 30d low, the most-transacted DP
             print and phase-2 distribution all cluster)
    resistance: $42.50 (five-method confluence + the vanna squeeze's natural ceiling)
    invalidation: no position should be sized ahead of the 2026-07-28 postmarket print —
                  any pre-print stop sits inside the ±12.25% implied move and will be
                  gapped through, not triggered by thesis. Reassess only once price settles
                  post-FOMC (2026-07-29) relative to $33.36–$42.66; a close outside that
                  range with confirming flow is the earliest legitimate re-entry.
- top_signal: Phase-4's FULLY_NEGATIVE gamma (net_dex −$40.3M ≈0.83% of float,
  zero_gamma_level=null, confirmed by phase-5's 24-session/−28.8% out-of-sample GEX track
  record) guarantees mechanical amplification of whichever way the gap breaks, while
  phase-7b (2/3 axes contradict) and phase-7c (CROWDED_SHORT 17.55% and rising into an
  armed vanna squeeze) independently VETO sizing the bearish thesis.
- top_risk: Two binaries in 48 hours — earnings 2026-07-28 postmarket then FOMC 2026-07-29
  14:00 ET while ENPH trades its own gap — over a surface with no gamma brake and no OI pin
  (max-pain's $41 magnet backed by only 16,897 contracts); any stop inside ±12.25% is taken
  out by path, not by being wrong.
```

**Assessment:** re-ran `uw risk portfolio-correlation --symbols ENPH
--lookback-days 30` and `ls -d research/*/2026-07-27/` and **independently
confirmed ENPH is the sole blueprint for the date** — `tickers_analyzed = 1`,
`high_correlations = null`. **The correlation gate does not bind.** Its conviction
of 1 is a statement that *no directional position is defensible*, not that it
lacks a view.

## Verification of the new primary data

`earnings-scout`'s historical-earnings figures are the only genuinely new primary
data introduced in phase 8, and they materially change the vol conclusion — so I
verified the larger claim independently rather than taking it at face value:

**Confirmed.** WebSearch returns Trefis (2026-02-05): *"Enphase Stock (+39%):
Strong Guidance Ignites Vicious Short Squeeze"*; Finviz: *"Enphase (ENPH) Jumps
38.6% on Strong Profits"*; Simply Wall St: *"Why Enphase Energy (ENPH) Is Up 34.9%
After Q4 Earnings."* The mechanism is documented: **Q4'25 adjusted EPS $0.71 vs
~$0.52 consensus**, and **Q1'26 revenue guidance of $270–300M against ~$263.3M
expected**, with management confirming channel inventory normalised and US
sell-through up 21% sequentially. Roth, TD Cowen, Oppenheimer, Susquehanna,
Morgan Stanley, Goldman, JPMorgan, Mizuho and Citi all raised targets; RBC and BMO
upgraded.

Two notes on precision: the reported move ranges **+34.9% to +39%** depending on
the measurement window, and the $0.52 consensus cited by Trefis differs from
Finnhub's `estimate = 0.5933` for that quarter (`phase-7b-fundamentals.md`) —
different consensus vendors. **Both agree it was a beat; the magnitude of the
*reaction* is not in dispute.**

**Implication, stated plainly:**

| Print | Move | vs 12.25% implied |
|---|---|---|
| 2026-02-04 (Q4'25) | **+39%** | **3.18×** |
| 2026-04-28 (Q1'26) | **−9.1%** | 0.74× |
| **Mean absolute** | **~24.1%** | **~1.97×** |
| 2025-10 (Q3'25) | **not recoverable** | — |
| 2025-02 (Q4'24) | **not recoverable** | — |

⚠️ **n = 2. This is a suggestive sample, not an established distribution**, and
the two recovered prints may be selection-biased toward the memorable ones.
Treated as strong evidence, not proof.

**The February template is live again.** That move was *"guidance ignites vicious
short squeeze"* — and today ENPH carries **17.55% short float that is rising**
(`phase-7c-sentiment.md`), an **armed positive-vanna dealer book**
(`phase-4-structure.md`), **no pin**, and **flat 25Δ skew** meaning upside
convexity is priced identically to downside. **The same mechanism, the same
setup.** That is the strongest single argument in the run against a directional
short, and it is now evidenced rather than asserted.

## Disagreements

**One agent takes the opposite bias from the plurality: `contrarian-scanner`
(LONG vs 4× NEUTRAL).**

Per the phase-8 heuristic — *"4-of-5 with one strong dissent: read the dissent's
top_signal carefully — often it's the missing piece"* — the dissent's signal:

> *"phase-4's `net_vanna = +913` with front-week IV certain to crush 170%→~90%
> post-print forces the short-put dealer book to BUY as soon as the event clears,
> and it is arming into a short base that phase-7c shows is RISING
> (15.09M→16.79M shares) rather than covering — the crowd is adding to the short
> at the exact moment the dealer mechanics flip bullish."*

**This is not really a contradiction of the other four — it is a sharper reading
of the same mechanics.** `earnings-scout` (conviction 4) independently supplies
the historical evidence that makes it credible (+39% on exactly this setup in
February), and `risk-monitor` explicitly endorses *"small defined-risk long
optionality"* as the only defensible expression. The genuine gap between them is
**directional commitment**: `contrarian-scanner` wants **cheap calls into
$42.50**; `earnings-scout` wants a **two-sided straddle/strangle** because it
respects the −9.1% precedent equally.

**Note what is absent: no agent argues the bear case as a trade.** Even
`sweep-tracker`, whose entire mandate is the bearish sweep campaign, concludes
*"direction is right, size is irrelevant."* Phases 1–7 produced a bearish bias;
the desk unanimously declines to express it.

**Sub-disagreement on levels:** `sweep-tracker` and `accumulation-hunter` place
first resistance at **$40 / $40.55–40.67** (max-pain magnet and dark-pool supply)
rather than **$42.50**. Both are right at different horizons — $40 is the nearer
mechanical magnet, $42.50 the structural wall. Phase-9 should carry **both**.

## Tool errors

**No `MISSING:` lines — all five `subagent_type` values resolved and all five
returned complete, well-formed verdicts.**

Agent tool usage stayed within the ~30-call phase budget: 4 + 9 + 2 + 11 + 8 = 34
tool calls total, of which a substantial share were file reads of the phase MDs
rather than `uw` calls. `earnings-scout` and `contrarian-scanner` used the most
(11 and 9) and were the two that produced new information.

One agent (`risk-monitor`) appended a trailing prose line after its verdict block
listing the files it read, contrary to the "no closing remarks" instruction.
Cosmetic; the verdict block itself is complete and correctly formatted. Its extra
work — re-running `portfolio-correlation` — was useful and is reported above.

## DATA NOTE / CORRECTION

- **`historical_earnings_moves` is new primary data**, sourced by `earnings-scout`
  via WebSearch and **independently re-verified** by the orchestrator (Trefis /
  Finviz / Simply Wall St). It is **not** derived from any phase 1–7 artifact.
  **n = 2 of 4**; the October-2025 and February-2025 reactions remain unmeasured.
- **The reported February move spans +34.9% to +39%** by source and measurement
  window. **+39%** is used (Trefis headline, corroborated by Finviz's +38.6%),
  with the range disclosed.
- **The `+39%` datapoint resolves an open question carried by four phases**
  (4, 5, 6, 7b) and **shifts the vol verdict from "fairly priced" to "fairly
  priced-to-cheap."** Phase-5's preliminary read (implied/ATR 1.46×,
  implied/RV 2.9× → *"fairly priced, arguably slightly cheap"*) is **strengthened,
  not corrected** — the direction of the update was already right.
- **No agent verdict was edited.** All five blocks are reproduced verbatim from
  their returned output.
- **No prior phase number is corrected by this phase.**

## Verdict for downstream

- **Plurality bias: NEUTRAL, 4 of 5** (accumulation-hunter, sweep-tracker,
  earnings-scout, risk-monitor). **1 LONG** (contrarian-scanner). **0 SHORT.**
- **Average conviction across all five (none MISSING): 2.2 / 5.**
- Per the phase-8 heuristic this is neither a 5-of-5 alignment nor a 3-2 split.
  It is **4-1 with a strong dissent whose signal is corroborated by the
  highest-conviction agent** — so the dissent must be weighted well above its
  single vote. **The operative desk conclusion is: direction-neutral, long
  volatility, with an upside skew to the tail risk — not short.**

- **Three highest-quality signals across all agents:**
  1. **[AGENT:earnings-scout]** *"ENPH's last two earnings prints moved +39%
     (2026-02-04, guidance-beat short squeeze) and −9.1% (2026-04-28) — both
     outside tomorrow's 12.25% implied move."* **Independently verified.** Mean
     absolute ≈24% ≈ **2× the priced move**. **The single most decision-relevant
     fact produced in the entire run**, and the one that phases 4–7b could not
     obtain. *(n=2 — suggestive, not conclusive.)*
  2. **[AGENT:contrarian-scanner]** *"`net_vanna = +913` … arming into a short
     base that is RISING (15.09M→16.79M shares) rather than covering — the crowd
     is adding to the short at the exact moment the dealer mechanics flip
     bullish."* Ties phase-4's mechanics to phase-7c's positioning and to the
     documented February precedent. **This is the bull case, and it is mechanical
     rather than fundamental.**
  3. **[AGENT:risk-monitor]** *"Any stop inside the ±12.25% implied move is taken
     out by path, not by being wrong"* — with two binaries stacked in 48 hours
     (earnings 07-28 postmarket, FOMC 07-29 14:00 ET) over a surface with
     `zero_gamma_level = null` and no OI pin. **This governs structure selection
     in phase-9 more than any directional view.**

- **Consensus levels for phase-9** (agent convergence, cross-checked upstream):
  - **Support $35.00** — 3 of 5 agents (`put_wall_support`, 4,217 puts vs 10 calls
    ≤30DTE; `net_gex −502,635`). Secondary shelf **$36.21–36.70** (30d low,
    most-transacted DP level at 9 trades, recent swing-low close) — 2 of 5.
  - **Resistance $42.50** — 4 of 5 agents. **Now a six-method confluence**:
    only genuine near-term call wall (3,735 calls / 0 puts) + largest positive
    gamma (+703,006) + SMA20 ≈$42.76 + $42.00 median analyst target + vanna-squeeze
    ceiling + agent consensus. **Nearer magnet $40.00–40.67** (max-pain in 8 of 15
    expiries; DP supply cluster) — 2 of 5.
  - **Priced range: $33.36 – $42.66** (±12.25%). Note **$42.50 sits just inside the
    upper bound and $35.00 comfortably inside the lower** — the implied move
    contains both consensus levels, which is exactly why every agent says stops
    will be gapped.

- **Open questions surfaced by agents:**
  - **Two of the last four earnings reactions remain unmeasured** (Oct-2025,
    Feb-2025). With n=2 the "2× the implied move" claim is suggestive, not
    established. → **phase-8b should stress this**
  - Is the correct expression **directional upside** (contrarian-scanner: cheap
    calls into $42.50) or **two-sided long vol** (earnings-scout: straddle/
    strangle)? The −9.1% April precedent argues for two-sided; the rising short
    base and flat skew argue for a call-tilted structure. → **phase-8b / phase-9**
  - `earnings-scout`'s own invalidation — **IV crushes 170%→~90% with spot pinned
    near $38** — is the specific way a long-vol trade loses. How probable is a
    sub-4% move on a name with an 8.4% ATR and no pin? → **phase-9 (structure)**
  - Nearest resistance: **$40 (max-pain magnet)** or **$42.50 (structural wall)**?
    Agents split 2–4. → **phase-9 (target laddering)**
