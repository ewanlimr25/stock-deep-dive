# Phase 7c — Sentiment, Positioning & Short Interest

**Ticker:** SWKS
**As-of date:** 2026-07-31
**Generated:** 2026-08-02
**Upstream phases cited:** `phase-0-intake.md`, `phase-0.5-context.md`, `phase-1-flow.md`, `phase-2-dark-pool.md`, `phase-5-historical.md`, `phase-6-macro.md`, `phase-7-insights.md`, `phase-7b-fundamentals.md`

## Summary

**The crowd is short, and the sell side is cutting — but the short is mechanical,
not opinionated, and that distinction reverses the usual playbook.** SWKS carries
**21.93% of float short (≈32.9M shares, 5.77 days to cover)**, roughly **5× the
17-peer median** and **2.2× the next-highest name** — but `phase-6-macro.md` and
`phase-7b-fundamentals.md` together establish this is almost certainly the
**merger-arb hedge** (long QRVO / short 0.960 SWKS), corroborated by QRVO's own
elevated 8.02% and by both names sitting at ~5.4–5.8 days-to-cover against a cohort
at 1–3. **That matters enormously for how it unwinds: on deal completion the arb
retires its short by delivering the SWKS shares it receives — no market buying, no
squeeze. On a deal BREAK it must buy ≈32.9M shares in the open market — a violent
squeeze that arrives attached to the fundamentally worst outcome.** Sentiment
elsewhere is uniformly negative: **7 of 8 firms cut price targets on 2026-07-29**
(mean of the new targets **$66.00**, Mizuho as low as **$52** at Underperform),
KeyBanc downgraded on 2026-07-14, BofA cut on merger-execution concerns, and
Finnhub's recommendation trend shows **Sells rising 1 → 3 since April with coverage
shrinking 33 → 31**. Critically, **there is no retail euphoria to fade** — even
sub-10-lot retail trades were **79.2% call-selling on the bid**. **One contrary axis
(adverse revisions) ⇒ `tier_adjustment: CAUTION`.**

## Key signals

- **★ Short float 21.93%, Short Ratio 5.77, Float 149.81M ⇒ ≈32.85M shares short.**
  Peer cohort median ~4.3%; next-highest ALGM 10.05%; merger partner QRVO 8.02%.
  `[SENT:short_float fz semi-monthly]`
- **★ Analyst revision cluster on 2026-07-29: 7 of 8 firms LOWERED targets, 1
  raised, 0 upgrades, every rating Neutral/Hold or worse.** New targets: Mizuho
  **$52 (Underperform)**, Citigroup $64, TD Cowen $65, JP Morgan $65, RBC $70,
  Stifel $70, UBS $70 *(raised)*, Morgan Stanley $72. **Mean $66.00, median
  $67.50.** `[SENT:news_flow finnhub]`
- **Recommendation trend is deteriorating slowly:** Sell count **1 → 2 → 3 → 3**
  (Apr → Jul), Hold **22 → 18**, Buy flat at 8, Strong Buy flat at 2, **total
  coverage 33 → 31**. `[SENT:recom finnhub]`
- **★ NO retail euphoria.** Sub-10-lot ("retail") trades were **79.2% of call
  contracts on the bid** (397 bid vs 104 ask) and only 38.7% of put contracts on
  the ask. Retail is **selling calls alongside institutions** — the classic
  fade-the-crowd divergence is **absent**. `[SENT:retail_vs_inst DUCKDB]`
- **Zero call blocks.** The only >500-lot trades on the entire tape were the
  **2,662-contract bid-side and 666-contract mid 52.5 put sale**. `[SENT:retail_vs_inst DUCKDB]`
- **P/C z-score +2.557 = `BEARISH_EXTREME`**, but manufactured by put *selling*
  (put ask-share 0.088); IV rank 52.9 = **29.9th self-percentile**.
  `[SENT:positioning_extremes]`

## Detailed findings

### News flow (14 days: 2026-07-17 → 2026-07-31)

`/company-news?symbol=SWKS&from=2026-07-17&to=2026-07-31` returned **43 items**.
**Look-ahead guard: every `datetime` falls inside the window and ≤ the as-of date —
0 items dropped.**

**Tone by sub-period:**

| Window | Items | Tone |
|---|---|---|
| 2026-07-17 → 07-27 (pre-print) | 11 | **Constructive/anticipatory** — "Will Skyworks Beat Estimates Again", "Expected to Beat Earnings Estimates: Can the Stock Move Higher?", "2 Radio Frequency Stocks to Watch From a Prospering Industry", a NetSync product launch for AI data centers (07-23), and SeekingAlpha's **"Skyworks Q3 Preview: The Correction Helps Long-Term Investors Accumulate More"** (07-24) |
| 2026-07-28 (print day) | 13 | **Mixed → negative.** Beat headlines ("Q3 Adj. EPS $1.08 Beats $1.01 Estimate, Sales $934.800M Beat $920.280M") sit next to "**Sees Q4 Adj EPS $1.27 vs $1.28 Est**", "**Posts EPS Beat, Suspends Dividend Amid Qorvo Merger Plans**", and two "Exceeds Expectations **But Stock Drops**" pieces. Also: combined-company leadership named (Philip Carter CFO, Reza Kasnavi COO/CTO) |
| **2026-07-29 (reaction day)** | **15** | **Decisively negative — the PT-cut cluster** (table below), plus "These Analysts Revise Their Forecasts On Skyworks Solutions Following Q3 Earnings". Sole positive: "Skyworks' Qorvo Deal Seen as Favorable Amid Steady Core Trends, RBC Says" |
| 2026-07-30 → 07-31 | 4 | **Neutral/flat** — "Stock Trades Near Fair Value Despite Rich Earnings", "1 Value Stock with Exciting Potential and 2 We Turn Down", and a **Qualcomm**-focused piece |

**Did the tape lead or lag the news?** It **led**. `phase-5-historical.md` shows
SWKS fell **−14.03% over the 30 sessions to 2026-07-31** (72.45 → 62.28) with a
**$56.91 low on 2026-07-16** — *before* the pre-print window even opened — while the
news tone in that window was still constructive ("Expected to Beat", "Prospering
Industry"). The negative headlines arrived on **2026-07-29, after** the −5.40%
reaction. **News is a lagging confirmation here, not a driver**, which is exactly
why `phase-2-dark-pool.md` could find institutions absorbing **+341,637 net shares
on the reaction day itself**: the informed side was positioned before the
commentary turned.

One item deserves a flag: the 2026-07-30 Benzinga piece **"Wall Street's Most
Accurate Analysts Spotlight On 3 Tech Stocks Delivering High-Dividend Yields"**
appeared **two days after SWKS eliminated its dividend**. Screens and syndicated
lists are still classifying SWKS as an income name. That is precisely the
mis-classified holder base `phase-7b-fundamentals.md` flagged as **forced sellers on
mandate rather than on view**, and it is not yet fully worked through.

### Analyst-revision momentum

**★ The 2026-07-29 post-earnings revision cluster** (all from Finnhub company-news,
all dated ≤ as-of):

| Firm | Rating action | New PT | vs spot $62.28 | Direction |
|---|---|---|---|---|
| **Mizuho** | Maintains **Underperform** | **$52** | **−16.5%** | **LOWERED** |
| Citigroup | Maintains Neutral | $64 | +2.8% | **LOWERED** |
| JP Morgan | Maintains Neutral | $65 | +4.4% | **LOWERED** |
| TD Cowen | Maintains Hold | $65 | +4.4% | **LOWERED** |
| RBC Capital | Maintains Sector Perform | $70 | +12.4% | **LOWERED** |
| Stifel | Maintains Hold | $70 | +12.4% | **LOWERED** |
| **UBS** | Maintains Neutral | $70 | +12.4% | **RAISED** |
| Morgan Stanley | Maintains Equal-Weight | $72 | +15.6% | **LOWERED** |
| **Mean of the eight** | — | **$66.00** | **+5.97%** | — |
| **Median of the eight** | — | **$67.50** | **+8.38%** | — |

Plus, outside the cluster:
- **KeyBanc: Overweight → Sector Weight, 2026-07-14, no PT** — the only *rating*
  downgrade, on "new content gains likely offset by a contracting smartphone
  market" and single-customer reliance (`phase-7b-fundamentals.md`).
- **BofA: PT cut on merger-execution concerns** (Investing.com; specific target not
  recovered).

**Not one of the eleven firms carries a Buy.** The best rating in the entire
post-print set is Neutral/Equal-Weight/Sector Perform.

**Finnhub `/stock/recommendation`** (monthly snapshots; all periods ≤ as-of):

| Period | Strong Buy | Buy | Hold | Sell | Strong Sell | Total | Bull share |
|---|---|---|---|---|---|---|---|
| 2026-04-01 | 2 | 8 | **22** | **1** | 0 | 33 | 30.3% |
| 2026-05-01 | 2 | 9 | 20 | 2 | 0 | 33 | 33.3% |
| 2026-06-01 | 2 | 8 | 19 | **3** | 0 | 32 | 31.3% |
| **2026-07-01** | **2** | **8** | **18** | **3** | 0 | **31** | 32.3% |

**Direction, not level:** Sells **tripled** (1 → 3) since April, Holds fell
**22 → 18**, Buys and Strong Buys are **flat**, and **coverage is shrinking (33 →
31)**. Nothing is improving. Note this snapshot is dated **2026-07-01** — it
**predates both the 2026-07-14 KeyBanc downgrade and the entire 2026-07-29 cut
cluster**, so the true as-of state is **worse than the table shows**.

**Vendor divergence (D6), reported not resolved:**

| Source | Consensus | Avg PT | Coverage |
|---|---|---|---|
| Finnhub `/stock/recommendation` (2026-07-01) | 2 SB / 8 B / 18 H / 3 S | — | 31 |
| WebSearch aggregate ("late July", `phase-7b-fundamentals.md`) | 1 SB / 4 B / 16 H / 3 S = **Hold** | **$74.72** | 24 |
| **The 2026-07-29 cut cluster (this phase)** | **0 Buy of 8** | **$66.00** | 8 |
| `fz quote` `Recom` / `Target Price` | **null / null** | — | — |

**★ Correction to `phase-7b-fundamentals.md`: the $74.72 average price target is
stale.** It is a "late July" aggregate that has not absorbed the 2026-07-29
revisions. **The post-print mean of the eight firms that actually re-marked is
$66.00 (+5.97%), median $67.50 (+8.38%)** — a ~12% reduction in the implied upside.
Phase 9 should use **$66–67.50**, not $74.72, as the sell-side anchor.

`fz`'s `Recom`/`Target Price` are **null** — the persistent 14/84-field quote
degradation from `phase-0-intake.md`. The D6 cross-source could not be run from
`fz`; Finnhub's recommendation series plus the primary Benzinga revision items were
used instead and are labelled as such.

### Retail vs institutional

Lit-tape decomposition by trade size (DuckDB, `bot-eod-report-2026-07-31.parquet`,
471 SWKS trades):

| Size bucket | Type | Side | Trades | Contracts | Premium |
|---|---|---|---|---|---|
| **retail (≤10)** | call | ask | 54 | 104 | $44,235 |
| **retail (≤10)** | call | **bid** | **171** | **397** | **$130,566** |
| retail (≤10) | call | mid | 33 | 68 | $21,990 |
| **retail (≤10)** | put | ask | 52 | 129 | $65,347 |
| **retail (≤10)** | put | **bid** | 94 | 204 | $62,373 |
| retail (≤10) | put | mid | 27 | 61 | $28,485 |
| mid (11–100) | call | ask | 1 | 68 | $30,532 |
| **mid (11–100)** | call | **bid** | 16 | **414** | $115,100 |
| mid (11–100) | call | mid | 1 | 29 | $38,280 |
| mid (11–100) | put | ask | 8 | 183 | $22,050 |
| **mid (11–100)** | put | **bid** | 11 | **379** | $66,775 |
| mid (11–100) | put | mid | 2 | 100 | $32,500 |
| **block (>500)** | **put** | **bid** | **1** | **2,662** | **$173,030** |
| **block (>500)** | put | mid | 1 | 666 | $46,620 |
| large (101–500) | — | — | **0** | 0 | $0 |

**Four findings, and the first is decisive:**

1. **★ There is no retail call euphoria.** Retail-lot call contracts traded
   **79.2% on the bid** (397 of 501 ask+bid) for $130,566 sold vs $44,235 bought.
   The fade-the-crowd setup this phase exists to detect — small-lot ask-side call
   buying into institutional distribution — is **categorically absent**. Retail is
   doing the **same thing** as institutions: **selling calls**.
2. **Retail is the only cohort with any net put buying**, and even that is modest:
   129 ask vs 204 bid contracts (38.7% ask-share), $65,347 bought vs $62,373 sold.
   Retail is mildly hedging; nobody else is.
3. **Zero call blocks.** Every trade above 500 contracts on the entire board was the
   **52.5 put sale** (2,662 bid + 666 mid). Institutional size expressed itself
   **once**, and it was **short puts**.
4. **Retail dominates trade count, not dollars:** 431 of 471 trades (91.5%) were
   sub-10-lot, but they carried only **$352,996 of the $877,883 tape (40.2%)**.

**Verdict: retail and institutions are on the SAME side.** There is **no
divergence to fade**. That removes the phase's primary fade trigger and is, on its
own, a mild point in favour of taking the tape at face value rather than as
distribution.

### Short interest & borrow

| Metric | Value | Source |
|---|---|---|
| **Short Float** | **21.93%** | `fz screen --view ownership` `[SENT:short_float fz semi-monthly]` |
| **Short Ratio (days to cover)** | **5.77** | `fz` |
| **Float** | **149.81M** | `fz` |
| **⇒ Shares short (derived)** | **≈32.85M** | 0.2193 × 149.81M |
| Institutional ownership | **112.87%** | `fz` — >100% is itself a lending/shorting signature |
| **Borrow fee / HTB status** | **n/a** | WebSearch returned no borrow-rate or HTB data |

**Semi-monthly caveat:** Finviz short interest is the **exchange semi-monthly
settlement figure with roughly a two-week lag**. The 21.93% therefore reflects a
settlement date around **mid-July 2026**, i.e. **before** the 2026-07-28 earnings
print, the dividend elimination and the SAMR Phase III disclosure. It is a
positioning *level*, not a post-event reading.

**Peer context** (`phase-7b-fundamentals.md`, 17 names):

| Rank | Ticker | Short Float | Short Ratio |
|---|---|---|---|
| **1** | **SWKS** | **21.93%** | **5.77** |
| 2 | ALGM | 10.05% | 4.18 |
| 3 | SLAB | 9.10% | 6.82 |
| **4** | **QRVO** *(merger partner)* | **8.02%** | **5.39** |
| 5 | SMTC | 7.03% | 1.84 |
| … | cohort median | ~4.3% | ~2.1 |
| 17 | AVGO | 1.47% | 2.65 |

**★ This short interest is mechanical, not opinionated — and the unwind asymmetry
is the opposite of the textbook.** The evidence that it is the merger-arb hedge
(long QRVO / short 0.960 SWKS, per `phase-6-macro.md`):

- **SWKS and QRVO are ranked 1st and 4th** on short float in a 17-name cohort, and
  are the **only two names** with days-to-cover in the 5.4–5.8 band while the rest
  sit at 1–3.
- **The magnitudes reconcile.** 32.85M SWKS shares short ÷ the 0.960 exchange ratio
  = **34.2M QRVO-share-equivalents = 39.3% of QRVO's 87.13M float** — a plausible
  arb participation rate, and *not* an implausible one in either direction.
- The arb short appeared alongside a deal announced with a **Goldman Sachs bridge
  commitment dated 2025-10-27** (SWKS 10-Q), i.e. the position has had ~9 months to
  build.

**Why this inverts the standard squeeze logic — the single most important
mechanical point in this run:**

| Scenario | What the arb does with its ≈32.9M-share short | Effect on SWKS |
|---|---|---|
| **Deal CLOSES** (SAMR clears) | Receives 0.960 SWKS per QRVO share held and **delivers those shares against the short**. No open-market purchase. | **No squeeze.** But the persistent supply **stops** — a removal of overhang, not a buy-side event. Mildly positive, gradual. |
| **Deal BREAKS** (SAMR blocks/over-conditions) | The hedge has no delivery to net against — it must **buy ≈32.9M shares in the open market** (5.77 days of average volume) while dumping QRVO. | **Violent squeeze UP — arriving attached to the worst fundamental outcome** ($2B of debt raised for nothing, $500M+ synergies gone). |

**Consequence: the 21.93% short is NOT conventional squeeze fuel for a long
thesis.** The phase's own heuristic ("*high short interest + bullish flow +
dark-pool accumulation → squeeze fuel*") applies only in its **hazard** form: it
makes a **short thesis dangerous** without making a **long thesis safer**. And it
means the two outcomes of the binary are **not cleanly directional** — a fact phase
8b must debate and phase 9 must size around.

**Borrow is genuinely unknown.** No fee or HTB tag was recoverable. Per the phase's
pitfall — *absence of short data is not bullish; mark it, don't infer* — borrow is
recorded as **n/a**, not as EASY. The observable proxies (21.93% of float out on
loan, 112.87% institutional ownership) are consistent with tight borrow but do not
establish it.

### Positioning extremes

| Metric | Value | Reading |
|---|---|---|
| **P/C ratio z-score** (20d) | **+2.557**, `extreme: "BEARISH_EXTREME"` | \|z\| > 2 ⇒ **contrarian trigger fires** |
| P/C ratio (level) | 4.0593 vs 20d mean 1.0798 | 97.4th self-percentile |
| IV rank | 52.90 | 61.6th universe pctile, **29.9th SELF pctile** |
| IV percentile (77 sessions) | 40.26, z −0.219, `regime: NORMAL` | Not an extreme |

**The P/C extreme is real as a statistic and inverted as a sentiment read** — the
third phase in a row to reach this conclusion independently
(`phase-1-flow.md`, `phase-5-historical.md`, `phase-7-insights.md`). The 4,384 puts
were **88.9% sold on the bid**, and 3,333 of them were one **opening short-put
block**. A `BEARISH_EXTREME` built from put *selling* is not bearish crowd
positioning; **the contrarian trade the trigger points at is already the position
on the tape.**

**IV rank is the more useful extreme**: at the **29.9th percentile of SWKS's own
history**, options are cheap for this name — which, with
`phase-5-historical.md`'s finding that realized vol has crossed **above** implied on
the trailing 5–10 sessions, is the one positioning fact that genuinely favours a
structure rather than a direction.

## Divergences

1. **★ Analyst targets vs the dark pool.** Seven of eight firms cut targets on
   2026-07-29 (mean $66.00) — on the **same session** the dark pool absorbed
   **+341,637 net shares (+$21.16M)** at a 0.634 buy ratio, followed by **+232,129
   (+$14.21M)** at 0.751 the next day (`phase-2-dark-pool.md`). **The sell side
   marked down what somebody else was buying, in size, that day.**
2. **★ 21.93% short float vs a "no directional view" options tape.** The largest
   short position in its peer group coexists with a tape that is **net short
   premium on both legs** (`net_call_premium` −$170,899, `net_put_premium`
   −$214,781) and **25Δ skew at a NORMAL 1.042** (`phase-4-structure.md`). A
   genuine bearish crowd would bid puts; this one does not. **Confirms the short is
   a hedge, not a view.**
3. **News tone vs price timing.** Headlines turned decisively negative on
   2026-07-29 *after* a 30-session −14.03% decline that bottomed on **2026-07-16**.
   The commentary is **lagging**, not leading.
4. **Syndicated "high-dividend-yield" coverage vs the eliminated dividend.** A
   2026-07-30 piece still listed SWKS among high-yield tech names, two days after
   the dividend was killed. **The income holder base has not finished repricing.**
5. **NOT a divergence — and this matters:** retail and institutions are on the
   **same side** (retail sold 79.2% of its call contracts on the bid). The
   classic euphoria-fade signal is **absent**.

## Source calls (audit trail)

| # | Source / command | Result ← path | Status |
|---|---|---|---|
| — | Preflight | `FINNHUB_API_KEY` **set** (repo `.env`); `fz --version` **ok**; SWKS **US, no dot suffix** | pass |
| 1 | `curl .../company-news?symbol=SWKS&from=2026-07-17&to=2026-07-31` | **43 items**; all `datetime` within window ⇒ **look-ahead guard: 0 dropped**. Captured the 8-firm PT cluster (2026-07-29), the dividend-suspension headline (2026-07-28), the beat headlines, and the combined-company leadership announcement ← `[.[] \| {datetime,headline,source}]` | **200** |
| 2 | `curl .../stock/recommendation?symbol=SWKS` | 4 monthly rows, **all ≤ as-of**: 2026-07-01 {SB 2, B 8, H 18, S 3, SS 0}; 2026-06-01 {2,8,19,3,0}; 2026-05-01 {2,9,20,2,0}; 2026-04-01 {2,8,**22**,**1**,0} ← `.[]` | **200** |
| 2b | `fz quote SWKS \| jq '{recom, target}'` | **`{"recom":null,"target":null}`** — 14/84-field degradation (`phase-0-intake.md`). D6 cross-source **unavailable from `fz`** `[SENT:recom fz]` | **degraded** |
| 3 | DuckDB `bot-eod-report-2026-07-31.parquet`, `underlying_symbol='SWKS'`, bucketed by `size` | retail(≤10) call ask 104ct/$44,235 vs **bid 397ct/$130,566**; retail put ask 129ct/$65,347 vs bid 204ct/$62,373; mid(11–100) call bid 414ct; **block(>500) = put only, 2,662 bid + 666 mid**; large(101–500) = **0 trades**; 471 trades total `[SENT:retail_vs_inst DUCKDB]` | **ok** |
| 4 | `fz screen --tickers SWKS,… --view ownership` (via `phase-7b-fundamentals.md` §5b) | **Short Float 21.93%**, **Short Ratio 5.77**, **Float 149.81M**, Inst Own 112.87%; QRVO 8.02% / 5.39 / 87.13M `[SENT:short_float fz semi-monthly]` | **ok** |
| 4b | WebSearch — borrow fee / HTB | **No borrow-rate or HTB data returned.** Recovered instead: Goldman Sachs **Bridge Commitment Letter, 2025-10-27, up to $3,050.0M** of senior unsecured bridge term loans (SWKS 10-Q); BofA PT cut on merger-execution concerns `[SENT:borrow WebSearch:sec.gov, investing.com]` | **partial** |
| 5 | Reuse of `phase-5-historical.md` + `phase-0.5-context.md` | `pc-ratio-zscore` **+2.557**, `extreme: BEARISH_EXTREME`, mean 1.0798, std 1.1652; `iv_rank` 52.8977 (**29.9th self-pctile**); `iv_percentile` 40.26, z −0.219 | **ok** |

## Source errors

- `fz quote SWKS` → `Recom` and `Target Price` both **null**. The D6 analyst
  cross-source **could not be run from `fz`**; substituted with Finnhub's
  recommendation series and primary Benzinga revision items, both labelled by
  source. **No `fz` analyst value was inferred.**
- **WebSearch returned no borrow-fee or hard-to-borrow data** for SWKS. Recorded as
  **`borrow: n/a`**. Per the phase pitfall, this is a **blind spot, not an
  EASY-borrow finding**, and no HTB status was inferred from the 21.93% short float.
- **Short-interest recency caveat (not an error):** the `fz`/Finviz figure is the
  **exchange semi-monthly settlement, ~2 weeks lagged** ⇒ it reflects roughly
  mid-July 2026 and **predates the 2026-07-28 print, the dividend elimination and
  the SAMR Phase III disclosure**. Tagged `[SENT:short_float fz semi-monthly]`
  at every use.
- **Finnhub `/stock/recommendation` is dated 2026-07-01** — it predates the
  2026-07-14 KeyBanc downgrade and the 2026-07-29 cut cluster. Reported as
  returned, with the staleness stated inline; **the true as-of picture is worse.**
- No paid endpoint was called. No source was retried after a failure.

## DATA NOTE / CORRECTION

1. **★ Correcting `phase-7b-fundamentals.md`'s price target.** Phase 7b carried a
   WebSearch consensus average of **$74.72** described as "late July." The Finnhub
   news feed shows that figure **predates the 2026-07-29 revision cluster**, in
   which **7 of 8 firms cut**. **Corrected sell-side anchor: mean $66.00 / median
   $67.50** across the eight firms that actually re-marked after the print — a
   ~12% reduction in implied upside (from +20.0% to **+5.97% / +8.38%**). Verified
   by enumerating all eight named PTs from individual dated headlines rather than
   an aggregate. Phase 9 must use **$66.00–67.50**.
2. **The 21.93% short float is interpreted, and the interpretation is labelled as
   such.** It is **observed** that SWKS and QRVO rank 1st and 4th on short float
   with near-identical days-to-cover (5.77 / 5.39) against a cohort at 1–3, and
   that 32.85M ÷ 0.960 = 39.3% of QRVO's float. It is **inferred** — not observed —
   that these are the same arbitrageurs. Short-interest data identifies no holder.
   The inference is strong and internally consistent, but phase 8b should test it.
3. **Shares short (≈32.85M) is derived** as 0.2193 × 149.81M float. Both inputs are
   from the same `fz` ownership row.
4. **Mean/median of the PT cluster are computed** over the eight firms with a
   published new target (52, 64, 65, 65, 70, 70, 70, 72). KeyBanc (no PT) and BofA
   (PT not recovered) are **excluded from the arithmetic** and noted separately —
   both are cuts, so their exclusion makes the $66.00 mean, if anything,
   **generous**.
5. **The retail/institutional split uses a size proxy**, not an account-type flag.
   ≤10 contracts is a conventional retail proxy and is stated as such; the parquet
   carries no customer-type field. The conclusion (retail selling calls on the bid)
   rests on a 397-vs-104 contract split that is large enough to survive reasonable
   boundary changes.

## Verdict for downstream

```
sentiment_signal:  BEARISH
crowd_state:       CROWDED_SHORT
short_interest:    21.93% of float [fz, semi-monthly, ~mid-July settlement] ;
                   days_to_cover: 5.77 ; shares short ~32.85M ; borrow: n/a [WebSearch — no data]
tier_adjustment:   CAUTION
divergences:
  - "7 of 8 analysts CUT targets on 2026-07-29 (mean $66.00) on the very session the
     dark pool absorbed +341,637 net shares at a 0.634 buy ratio — the sell side
     marked down what somebody else was buying in size."
  - "21.93% short float (5x peer median) coexists with a tape that is net SHORT
     premium on both legs and 25-delta skew at a NORMAL 1.042 — a real bearish crowd
     would bid puts. Confirms the short is a merger-arb HEDGE, not a view."
  - "NOT a divergence, and it matters: retail sold 79.2% of its call contracts on
     the bid — same side as institutions. No euphoria to fade."
key_risks:
  - "Deteriorating revisions with no offset: 0 Buy ratings among 11 post-print
     firms; Sells 1->3 since April; coverage shrinking 33->31; Mizuho Underperform
     at $52 (-16.5%), which sits $0.07 above the 52-week low and $0.50 below the
     sold 52.5 put strike."
  - "The 21.93% short is NOT squeeze fuel for a long. On deal CLOSE the arb delivers
     received shares — no market buying. Only a deal BREAK forces ~32.9M shares of
     open-market covering, and that arrives with $2B of stranded debt and no
     synergies. The binary is not cleanly directional in either leg."
  - "The income-holder base has not finished repricing the dividend elimination —
     syndicated coverage was still listing SWKS as a high-yield tech name on
     2026-07-30. Expect continued mandate-driven, price-insensitive supply."
```

**Gate reasoning.** The flow bias from phases 1–7 is **MIXED with a mild
constructive tilt** (phase 2's two-session +573,766-share absorption is the
strongest single signal; phases 1, 3, 5, 7 are thin-to-neutral; phase 6 is a
headwind). Scored against the crowd:

| Axis | Reading | Contrary to the flow bias? |
|---|---|---|
| **News tone (14d)** | Constructive pre-print → **decisively negative post-print**; but **lagging** a decline that bottomed 2026-07-16 | Partially — discounted for lag |
| **Analyst revisions** | **7 of 8 PT cuts**, 0 Buys among 11 firms, Sells 1→3, coverage 33→31 | **YES — one clear contrary axis** |
| **Retail vs institutional** | **Same side** (retail 79.2% call-selling on the bid); no euphoria | **NO — no fade signal** |
| **Short interest** | **21.93%, CROWDED_SHORT** — crowded **opposite** to the flow tilt | **NO** — not the VETO condition |
| **Positioning extremes** | P/C z **+2.557** but built from put *selling*; IV rank at **29.9th self-pctile** | **NO** — inverted / structure-relevant |

**⇒ Exactly one contrary axis (adverse revision momentum) ⇒ `tier_adjustment:
CAUTION` ⇒ phase 9 cuts one size step.**

`VETO` is **not** warranted: the rubric's VETO requires the crowd to be **crowded
the same way as the thesis** plus a squeeze/SI mismatch. Here the crowd is
**crowded the opposite way** (short) from a mildly constructive tilt, and there is
**no retail euphoria** — the two conditions that would trigger a
distribution-into-strength veto are both absent. `CONFIRM` is equally unwarranted
given the revision cluster.

**Explicitly per the phase constraint — this gate can only cut, never raise.** The
genuinely supportive findings (no euphoria to fade, a crowd positioned against the
tilt, IV cheap at the 29.9th self-percentile) are **recorded but add no
conviction**.

**★ Two hand-offs to phases 8, 8b and 9:**

1. **The squeeze asymmetry is inverted, and this is the run's most
   counter-intuitive mechanical fact.** ≈32.9M shares short (5.77 days of volume)
   that **retire without market buying if the deal closes** but must be **bought in
   the open market if it breaks**. Phase 9 must not treat 21.93% short interest as
   a bullish catalyst, and must not construct any short exposure that would be run
   over by a break-driven cover. Combined with `phase-4-structure.md`'s **short
   gamma at spot (62.5, −448,437)**, a break-driven cover would be **mechanically
   amplified** by dealer hedging — the fattest tail in this blueprint.
2. **The sell-side anchor is $66.00–67.50, not $74.72.** Set by the eight firms
   that re-marked after the print. Note that **Mizuho's $52 Underperform target
   sits within $0.07 of the 52-week low ($51.93) and $0.50 below the strike where
   3,333 puts were sold** (`phase-1-flow.md`) — the most bearish house on the
   street and the largest opening options position on the board are underwriting
   **the same level from opposite sides**. Phase 8b should make that the crux of
   the debate.
