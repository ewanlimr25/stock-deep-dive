# Phase 7c — Sentiment, Positioning & Short Interest

**Ticker:** FSLR
**As-of date:** 2026-07-31
**Generated:** 2026-07-31
**Upstream phases cited:** `phase-0-intake.md`, `phase-1-flow.md`, `phase-2-dark-pool.md`, `phase-5-historical.md`, `phase-6-macro.md`, `phase-7-insights.md`, `phase-7b-fundamentals.md`

## Summary

**The sell side responded to a 37% EPS beat by cutting price targets across
every rating tier — that is the dominant sentiment fact of the day, and it is
adverse.** On 2026-07-31, **Wells Fargo maintained Overweight but lowered its
target to $300**, **Truist reiterated Hold and lowered to $229**, and
**Bernstein maintained Underperform and lowered to $197**. Ratings unchanged,
targets down, unanimously. The mechanism is visible in the headlines: EPS beat
big ($3.92 vs $2.86) but **sales of $1.056B missed the $1.062B estimate**, and
**FY guidance of $4.900–5.200B was affirmed against a $5.118B consensus** — a
midpoint below the street.

**The crowd, however, is not crowded.** The lit tape decomposed by trade size
shows **retail (≤5 lots) buying puts more aggressively than calls** —
put ask/bid premium **1.43** versus call ask/bid **1.12** — which is hedging,
not euphoria. There is no retail-euphoria-into-distribution setup here, which
is what would have escalated this gate toward VETO.

The most interesting structure is a **three-way split by participant size**:
retail is two-sided (ask/bid 1.26), **mid-size institutional flow (101–500
lots) is the most aggressively bullish cohort on the tape at ask/bid 3.22 with
76.3% of its premium in ask-side calls**, and the **largest blocks (>500 lots)
are net sellers at ask/bid 0.69** — the LEAP roll from `phase-1-flow.md`. The
biggest and second-biggest players are on opposite sides.

Short interest is **9.75% of float with 4.09 days to cover** — elevated in
absolute terms but, per `phase-7b-fundamentals.md`, **the third-lowest in the
solar group** (ENPH 17.89%, SEDG 17.97%, ARRY 20.39%, RUN 28.65%, CSIQ
34.53%). For a long thesis that is squeeze fuel; per the downside-only rule it
is noted, not sized on.

**Verdict: `sentiment_signal = BEARISH`, `crowd_state = BALANCED`,
`tier_adjustment = CAUTION`** — one contrary axis (adverse revision momentum),
one size step cut.

## Key signals

- **Three price-target cuts on 2026-07-31, all rating tiers**: WF $300
  (Overweight), Truist $229 (Hold), Bernstein $197 (Underperform)
  `[SENT:revision_trend]`
- **Guidance $4.900–5.200B vs $5.118B consensus** — midpoint below the street
  `[SENT:news_flow]`
- **Sales $1.056B missed the $1.062B estimate** despite the EPS beat
  `[SENT:news_flow]`
- **Retail bought puts harder than calls**: put ask/bid **1.43** vs call
  **1.12** — hedging, not euphoria `[SENT:retail_vs_inst DUCKDB]`
- **Mid-size (101–500 lot) flow is the most bullish cohort**: ask/bid **3.22**,
  76.3% of premium in ask-side calls `[SENT:retail_vs_inst DUCKDB]`
- **Largest blocks (>500 lots) net sellers**: ask/bid **0.69**
  `[SENT:retail_vs_inst DUCKDB]`
- **Short float 9.75%, days-to-cover 4.09** — third-lowest among solar peers
  `[SENT:short_float fz semi-monthly]`
- **Analyst ratings essentially static** (buy-side 30/48 = 62.5% since April)
  but strongSell doubled 1 → 2 `[SENT:recom]`
- **No positioning extreme**: P/C z-score −0.825 (`extreme: NORMAL`); IV rank
  81.94 but only the 39.4th self-percentile `[SENT:pc_zscore]`
- **Bernstein's $197 target sits 6.7% BELOW spot** — a credible bear anchor
  `[SENT:revision_trend]`

## Detailed findings

### News flow (14-day tone)

41 items returned for 2026-07-17 → 2026-07-31. All quoted items are dated
**≤ 2026-07-31** (look-ahead guard applied). The window is dominated by the
2026-07-30 print and its 2026-07-31 reaction.

**Analyst reactions, 2026-07-31 — the decisive cluster:**

| Firm | Rating action | Price target | vs spot 211.03 |
|------|---------------|-------------:|---------------:|
| Wells Fargo | **Maintains Overweight** | **$300** (lowered) | +42.2% |
| Truist Securities | **Reiterates Hold** | **$229** (lowered) | +8.5% |
| Bernstein | **Maintains Underperform** | **$197** (lowered) | **−6.7%** |

**Every firm that published lowered its target. None raised. None upgraded.**

**Results coverage, 2026-07-30 → 07-31:**

- *"First Solar Q2 EPS $3.92 Beats $2.86 Estimate, Sales $1.056B **Miss**
  $1.062B Estimate"* (Benzinga)
- *"First Solar Affirms FY2026 Sales Guidance of $4.900B-$5.200B **vs $5.118B
  Est**"* (Benzinga)
- *"First Solar (NASDAQ:FSLR) **Misses** Q2 CY2026 Revenue Estimates"* (Yahoo)
- *"First Solar (NASDAQ:FSLR) **Surges After-Hours** as Q2 Earnings Beat
  **Offsets** Revenue Miss"* (ChartMill)
- *"First Solar's Q2 Earnings Beat Estimates, **Revenues Decrease Y/Y**"* (Yahoo)
- *"First Solar Inc (FSLR) (Q2 2026) Earnings Call Highlights: **Record Sales
  and 100 GW Milestone**"* (Yahoo)
- *"FSLR Q2 Earnings Call Highlights **Domestic Solar Push**"* (Yahoo)
- *"First Solar Stock Edges Higher After Q2 **Profit Surge**"* (Benzinga)

**Tone: genuinely mixed, tilting negative on the forward look.** The bullish
items are backward-looking (profit surge, record sales, 100 GW milestone); the
bearish items are forward-looking (revenue miss, guidance below consensus,
three target cuts). Sector context is unhelpful too — *"Enphase Energy Q2
Earnings Match Estimates, Revenues Decline Y/Y"* (2026-07-29).

**Did the tape lead or lag the news?** It **lagged, then partly faded.** The
stock rose **+3.40% on 07-30** (the print landed AMC, so that move preceded
the news) and gapped **+3.29% on 07-31**, but faded **−0.82% from the open** to
close +2.44% — and `phase-5-historical.md` showed the intraday high of
**217.1274** stopped **0.17% short of the 217.50 gamma wall**. **Price
reacted to the beat and then met a structural ceiling as the target cuts
published.**

### Analyst-revision momentum

Finnhub `/stock/recommendation` — **note every row predates the earnings and
the target cuts**:

| Period | Strong Buy | Buy | Hold | Sell | Strong Sell | Total | Buy-side % |
|--------|-----------:|----:|-----:|-----:|------------:|------:|-----------:|
| **2026-07-01** | 6 | 24 | 15 | 1 | **2** | 48 | 62.5% |
| 2026-06-01 | 6 | 24 | 15 | 1 | 1 | 47 | 63.8% |
| 2026-05-01 | 6 | 23 | 17 | 1 | 1 | 48 | 60.4% |
| 2026-04-01 | 7 | 23 | 17 | 1 | 1 | 49 | 61.2% |

**Ratings are static.** Buy-side (SB+B) held at 30/29/30/30 across four
months — 62.5% currently. The only drift is at the extremes: **strongBuy 7 → 6
and strongSell 1 → 2** since April, with holds migrating out (17 → 15). A
mild barbelling, not a downgrade cycle.

**But the trend data is stale for this decision.** The latest period is
**2026-07-01 — four weeks before the print and thirty days before the target
cuts.** The three revisions on 2026-07-31 are **not** in this table.

**The direction of travel, which is what this axis measures, is adverse.**
Targets were cut by an Overweight, a Hold and an Underperform on the same day,
following a large EPS beat. Per the phase-7c heuristic — *"deteriorating
analyst revisions + bullish flow → flow front-running a downgrade cycle, or a
contrarian bounce"* — this is the contrary axis, and it should be read
alongside `phase-7b-fundamentals.md`'s finding that **revenue decelerated to
−4% YoY** and the FY guide implies a demanding **33–48% H2 acceleration**. The
analysts are marking down the forward model even as the current quarter beats.

**Target dispersion is itself a signal:** $197 to $300 is a **52% spread**
around a $211.03 spot. There is no analyst consensus on this name.

**Cross-source divergence check (D6): not performable.** `fz quote FSLR` is
degraded to a 14-field subset with no `Recom` or `Target Price`
(`phase-0-intake.md`), and `uw insights analyst-vs-flow` returned no analyst
leg at all (Yahoo HTTP 401, `phase-7-insights.md`). **Two of three intended
analyst sources failed**; the WebSearch/Finnhub news path above is the only
one that produced data.

### Retail vs institutional

Lit option tape decomposed by trade size (DuckDB, `canceled = false`):

| Bucket | Trades | Contracts | Premium ($M) | % premium in ask-side calls | **Ask/bid premium ratio** |
|--------|-------:|----------:|-------------:|----------------------------:|--------------------------:|
| **Retail (≤5 lots)** | 5,280 | 8,278 | **8.247** | 27.3% | **1.26** |
| Small (6–25) | 753 | 8,157 | 6.257 | 21.9% | 0.97 |
| Mid (26–100) | 81 | 3,702 | 2.062 | 32.3% | 0.91 |
| **Large (101–500)** | 20 | 3,867 | 1.425 | **76.3%** | **3.22** |
| **Block (>500)** | 6 | 7,020 | **8.674** | 32.2% | **0.69** |

**Retail direction detail (≤5 lots):**

| Type | Side | Trades | Contracts | Premium |
|------|------|-------:|----------:|--------:|
| call | ask | 1,505 | 2,429 | $2,252,520 |
| call | bid | 1,444 | 2,306 | $2,004,340 |
| call | mid | 199 | 307 | $214,271 |
| **put** | **ask** | 1,069 | 1,598 | **$2,140,751** |
| **put** | **bid** | 946 | 1,464 | $1,495,220 |
| put | mid | 117 | 174 | $139,630 |

Retail call ask/bid = **1.12**; retail **put ask/bid = 1.43**.

**Three findings, in order of importance:**

1. **There is no retail euphoria.** Retail is a large presence — 5,280 trades
   and **$8.25M, 31% of the day's $26.66M premium** — but it bought **puts
   more aggressively than calls** (1.43 vs 1.12). The classic
   distribution-into-strength setup (retail call euphoria absorbing
   institutional supply) **is not present**, and its absence is what keeps
   this gate at CAUTION rather than VETO.
2. **Mid-size institutional flow is the most bullish cohort on the tape.**
   The 101–500 lot bucket has an ask/bid premium ratio of **3.22** with
   **76.3% of its premium in ask-side calls** — three times more aggressive
   than any other bucket. This is where `phase-1-flow.md`'s $230/$210/$245/$250
   call buying lives.
3. **The largest blocks are on the other side.** Six trades >500 lots carry
   **$8.67M — the largest premium of any bucket — at ask/bid 0.69**, i.e. net
   selling. This is the LEAP roll (Package B sold $4.07M at mid-market) plus
   the 1,900-lot Aug-21 $230 cross.

**Read: retail is hedged and two-sided; mid-size institutions are buying
upside; the very largest players are trimming.** Retail and institutions are
**not** on opposite sides in the way that generates a fade signal — the real
divergence is *within* the institutional cohort, by size.

### Short interest & borrow

| Metric | Value | Source |
|--------|------:|--------|
| **Short float** | **9.75%** | `fz` (semi-monthly settlement, ~2-week lag) |
| **Days to cover** | **4.09** | `fz` |
| Shares float | 101.48M | `fz` |
| Implied shares short | ≈ **9.89M** | derived |
| Institutional ownership | 92.82% | `fz` |
| Insider ownership | 5.55% | `fz` |
| **Borrow fee / HTB** | **n/a** | not retrievable free |

**Peer context** (`phase-7b-fundamentals.md`): FSLR's 9.75% is the
**third-lowest** in the solar industry — ENPH 17.89%, SEDG 17.97%, ARRY
20.39%, RUN 28.65%, CSIQ 34.53%; only NXT (4.82%), JKS (6.81%) and SHLS
(8.83%) are lower. **The sector is heavily shorted as a theme and FSLR carries
materially less of that positioning than its peers.**

**Historical trajectory** (WebSearch, corroborating the level): short interest
ran ~9.22% of float in early 2025 (6.56M → 7.53M shares) and ~10.12% (10.26M
shares) as of September 2025. **Today's 9.75% is in line with a stable
one-to-two-year range** — no fresh short build, no capitulation.

**Borrow: could not be determined.** Fintel, Ortex and MarketBeat all gate
current borrow-fee and HTB data behind paid tiers. Per the standing rule,
**no paid source was used and no value is inferred.** Recorded as `n/a`.

*(Judgment, explicitly not a datapoint: a $22.68B S&P 500 constituent with a
101.48M float and 92.82% institutional ownership is very unlikely to be hard
to borrow. This is stated as reasoning, not measurement, and phase 9 should
not treat borrow as confirmed easy.)*

**Directional framing.** 4.09 days-to-cover means covering the full short
interest would take roughly four average sessions. Against
`phase-4-structure.md`'s finding that dealers are **short gamma below the
215.03 ZGL**, this **cuts both ways and phase 9 must carry both**:

- **Upside:** a break above the **217.50** gamma wall would force dealer
  buying *and* short covering into a 4-day-to-cover position — the strongest
  mechanical squeeze setup available in this name.
- **Downside:** the same short-gamma regime means a break below **200**
  (net_gex −465,782) accelerates *downward*, and 9.89M shares short do not
  help on the way down.

### Positioning extremes

| Measure | Value | Threshold | Extreme? |
|---------|------:|-----------|:--------:|
| P/C ratio z-score (20d) | **−0.825** | \|z\| > 2 | **No** |
| P/C `extreme` label | **NORMAL** | — | **No** |
| IV rank (universe) | 81.94 (92.8 pctile) | — | High |
| IV rank (self, N=67) | **39.4** | — | **No** |
| IV percentile (N=77) | 71.43, regime **NORMAL** | — | No |

**No sentiment extreme exists on any measure.** Today's P/C of 0.2791 is the
most call-skewed reading of the month, yet z = −0.825 because the series'
standard deviation (0.8305) is 86% of its mean (0.9642)
(`phase-5-historical.md`). The IV picture is the same story from two angles:
**high versus the universe (92.8th percentile), unremarkable versus FSLR's own
history (39.4th self-percentile)** — a name that habitually runs high vol,
now post-crush.

**There is no contrarian trigger here.** Phase 9 should not build a
mean-reversion or squeeze thesis on sentiment positioning; the squeeze case,
if any, rests on the **structural** gamma/short-interest interaction above,
not on crowd extremes.

## Divergences

1. **Sell side vs the print.** Three firms cut price targets on 2026-07-31 —
   across Overweight, Hold *and* Underperform — the day after a **+37.1% EPS
   beat**. The beat was driven by items analysts are not capitalizing (the
   **$89M IEEPA tariff benefit**, higher 45X mix — `phase-6-macro.md`) while
   the **revenue miss** and **below-consensus guidance** hit their forward
   models.
2. **Retail hedges while mid-size institutions buy upside.** Retail put ask/bid
   **1.43** exceeds its call ask/bid **1.12**, while the 101–500 lot cohort
   runs **3.22** ask/bid with 76.3% of premium in ask-side calls. The two
   cohorts are positioned in opposite directions.
3. **Institutions disagree with each other by size.** The 101–500 lot bucket
   is the most bullish on the tape (ask/bid 3.22); the >500 lot bucket carries
   the **largest premium of any bucket ($8.67M) at ask/bid 0.69** — net
   selling. Combined with `phase-2-dark-pool.md`'s regular-session
   accumulation (73.1% buy) against phase-1's **$1.374M-credit LEAP trim**,
   **one institutional cohort is initiating while another is monetizing.**

## Source calls (audit trail)

| Source / command | Result | Key value(s) ← path |
|------------------|--------|---------------------|
| Preflight: `FINNHUB_API_KEY`, `fz`, US ticker | all ok | key set; `fz` present; FSLR US |
| `/company-news?symbol=FSLR&from=2026-07-17&to=2026-07-31` | **ok** (41 items) | WF $300 / Truist $229 / Bernstein $197 headlines, all dated 2026-07-31 ← `.[].headline`, `.[].datetime` |
| `/stock/recommendation?symbol=FSLR` | **ok** (4 periods) | 2026-07-01: SB=6 B=24 H=15 S=1 SS=2 ← `.[0]`; latest period **predates earnings** |
| `fz screen --tickers FSLR --view ownership --json` (phase 0) | ok | Short Float=9.75%, Short Ratio=4.09, Float=101.48M, Inst Own=92.82% ← `.[0]` |
| `fz screen --filter ind_solar --view ownership` (phase 7b) | ok | peer SI: ENPH 17.89%, SEDG 17.97%, RUN 28.65%, CSIQ 34.53% |
| `fz quote FSLR --agent` → `Recom` / `Target Price` | **unavailable** | degraded to 14 fields; neither key present |
| DuckDB §A size-bucket split on `bot-eod-report-2026-07-31.parquet` | ok | retail ask/bid=1.26, put ask/bid=1.43 vs call 1.12; large(101-500) ask/bid=3.22; block(>500) ask/bid=0.69 | 6,140 prints |
| WebSearch — FSLR short interest / borrow / HTB | **partial** | SI level corroborated (~9.22% early-2025, ~10.12% Sep-2025); **borrow fee & HTB behind paid tiers → `n/a`** |
| Reused: `historical pc-ratio-zscore` (phase 5) | ok | zscore=−0.825, extreme="NORMAL" |
| Reused: `iv_rank` (phase 0.5) | ok | 81.94 universe / 39.4 self-percentile |

**Look-ahead guard applied:** the news window was bounded `to=2026-07-31`;
every headline quoted is dated 2026-07-29, 07-30 or 07-31. No post-as-of item
was used.

## Source errors

1. **Borrow fee / hard-to-borrow status unavailable.** Fintel, Ortex,
   MarketBeat and Benzinga all gate live borrow data behind subscriptions.
   Per the never-pay rule this is recorded as **`borrow: n/a`** and not
   inferred. **This is a genuine blind spot**, not a neutral reading.

2. **The `fz` analyst cross-source (D6) could not run.** `fz quote FSLR`
   returns only 14 fundamental fields — `Recom` and `Target Price` are absent
   (documented in `phase-0-intake.md`). **No vendor-divergence check was
   possible.**

3. **Carried from `phase-7-insights.md`:** `uw insights analyst-vs-flow`
   returned no analyst leg (`yahoo quoteSummary FSLR: HTTP 401`). **Two of the
   three intended analyst sources failed** — only the Finnhub
   recommendation-trend table and the WebSearch news path produced data.

4. **The Finnhub recommendation trend is stale for this decision.** Its most
   recent period is **2026-07-01**, four weeks before the earnings print and
   thirty days before the target cuts. The static ratings it shows should
   **not** be read as evidence that revisions are stable — the three cuts of
   2026-07-31 postdate the entire table.

5. **Short interest is the semi-monthly exchange settlement figure with an
   approximately two-week lag** (`fz`/Finviz). The 9.75% therefore reflects
   positioning around mid-July and **does not include any short covering or
   building around the 2026-07-30 earnings event.**

## DATA NOTE / CORRECTION

No correction to prior phases. One reconciliation worth recording:
`phase-7b-fundamentals.md` cited Q2 sales of **$1.06B** (rounded, from the
company release) while this phase quotes **$1.056B against a $1.062B
estimate** (Benzinga's precise figures). These are the same number at
different precision — and the precise version reveals a **revenue miss** that
the rounded figure obscures. Phase 10 should not flag this as a
contradiction, but phase 9 should use the precise version: **Q2 was an EPS
beat and a revenue miss.**

## Verdict for downstream

```
sentiment_signal:  BEARISH
crowd_state:       BALANCED
short_interest:    9.75% of float [fz, semi-monthly] ; days_to_cover: 4.09 ; borrow: n/a [WebSearch — paid-gated]
tier_adjustment:   CAUTION
divergences:
  - Three price targets cut (WF $300 / Truist $229 / Bernstein $197) the day after a +37.1% EPS beat
  - Retail bought puts harder than calls (put ask/bid 1.43 vs call 1.12) while 101-500 lot flow ran 3.22 ask/bid in calls
  - Largest blocks (>500 lots, $8.67M) net sellers at ask/bid 0.69 while mid-size institutions aggressively bought upside
key_risks:
  - FY guide $4.900-5.200B midpoint is BELOW the $5.118B consensus; sales $1.056B missed $1.062B
  - Bernstein's $197 Underperform target sits 6.7% BELOW spot - a credible bear anchor under the trade
  - 9.75% short float / 4.09 days-to-cover is squeeze fuel above 217.50 but an accelerant below 200,
    given dealers are short gamma beneath the 215.03 ZGL
```

**Axis-by-axis against the phase-1→7 flow bias** (plurality: *mildly bullish /
balanced-constructive*):

| Axis | Reading | Contrary to bullish bias? |
|------|---------|---------------------------|
| **News tone (14d)** | Mixed, tilting negative on the forward look: EPS beat, revenue miss, guidance below consensus. | Contrary — **same event as revisions below; counted once** |
| **Analyst revisions** | Three targets cut across all rating tiers on 2026-07-31; strongSell 1 → 2 since April; 52% target dispersion. | **YES — the one contrary axis** |
| **Retail vs institutional** | Retail two-sided and put-leaning (1.43 vs 1.12) — **no euphoria**; mid-size institutions aggressively long calls. | No — no fade setup |
| **Short interest / borrow** | 9.75% float, 4.09 DTC, third-lowest among solar peers; borrow unknown. | No — squeeze fuel *for* a long |
| **Positioning extremes** | P/C z −0.825 (`NORMAL`); IV rank 39.4 self-percentile. **No extreme on any measure.** | No |

**`tier_adjustment = CAUTION` → phase 9 cuts one size step.**

**Why not VETO:** the rubric requires the crowd to be *"crowded the same way
as the thesis AND a hard squeeze/short-interest mismatch."* Neither holds.
Retail is **hedging, not euphoric** — the single most important negative
finding that did *not* appear. And 9.75% short interest on a long thesis is
**fuel, not mismatch**; the squeeze-risk clause applies to *short* theses.

**Why not CONFIRM:** analyst revision momentum is unambiguously adverse —
three cuts, zero raises, on a large beat — and it is corroborated by
`phase-7b-fundamentals.md`'s independent findings (revenue −4% YoY, a guide
requiring 33–48% H2 acceleration). The sell side is marking down the forward
model, and per the phase-7c heuristic that pattern means the flow is either
front-running a downgrade cycle or catching a contrarian bounce.

**Per the downside-only rule, this gate cannot raise conviction.** The absence
of retail euphoria and the presence of squeeze fuel are recorded as
*context for phase 9 to weigh*, explicitly **not** as grounds to size up.

**Note for phase 9 on gate stacking:** this CAUTION is **independent** of
`phase-7b-fundamentals.md`'s CAUTION — 7b's contradiction is *insider selling*,
7c's is *analyst revisions*. They are different axes with different evidence,
so **both cuts apply**. Phase 9 should apply **two size steps down** from the
baseline, plus `phase-6-macro.md`'s "half position sizes" regime guidance,
before any further adjustment.
