# Phase 7c — Sentiment, Positioning & Short Interest

**Ticker:** MU
**As-of date:** 2026-07-28
**Generated:** 2026-07-28T23:02:00-04:00
**Upstream phases cited:** `phase-1-flow.md`, `phase-2-dark-pool.md`, `phase-5-historical.md` (P/C z-score), `phase-6-macro.md` (CXMT), `phase-7b-fundamentals.md` (analyst counts, MSPR)

## Summary

**The news layer supplies the proximate trigger that phase-6's structural CXMT story only half
explained: SK Hynix reported overnight, and its RECORD profit MISSED elevated expectations.**
Headlines on 2026-07-28 include *"SK Hynix's Record Profit Misses Investors' Lofty AI
Expectations"*, *"SK Hynix Stock Drops on Disappointing Earnings"*, *"SK Hynix, Samsung Drag
Down KOSPI as China Chip Fears Spread"*, *"The Korean Stock Market Crashes Overnight"* and
*"Nasdaq-100 slides into correction as global chip and memory stocks sell off"*. **A record
quarter that disappoints is the canonical cycle-top signature**, and it corroborates phase-7b's
peak-cycle read (`peNormalizedAnnual` 108.93 vs `peTTM` 18.43) far more directly than the CXMT
narrative alone.

**The crowd is positioned LONG and the smart money is not.** Analysts are **91.1% buy-or-better
(51 of 56, one sell, zero strong-sells)** and have *added* coverage through the entire -32%
drawdown; retail is publicly anchored on a rebound — *"MU Stock Loses Some Steam After Korea
Chip Selloff — But Retail Is Eyeing Clean Rebound Above $1,000"* (7/24) — while the stock trades
at $820.53; and phase-7b showed insiders selling (MSPR -100 in four of ten months). Against
that, phase-2 measured regular-hours dark-pool **distribution** (mega buy_ratio 0.227).

**But the classic "retail euphoria" fade does NOT fire, and this phase declines to claim it.**
The lit small-lot tape shows retail was **defensive, not euphoric**: trades ≤5 contracts **net
SOLD $34.3M of calls and net BOUGHT $19.7M of puts.** The $120M of net premium selling
identified in phase-1 is **overwhelmingly institutional** — the 51–500 and >500 contract buckets
account for **-$111.4M of the -$120.1M total.**

**There is no squeeze risk in either direction.** Short interest is **3.21% of shares out
(36.21M shares)** with **days-to-cover 1.0** and a **borrow fee of just 0.27–0.40%** with ~10M
shares available — **MU is easy to borrow, not HTB.** No positioning extreme exists either:
P/C z-score **-1.239** (`extreme = NORMAL`, |z| < 2) and IV rank 83.48 sits at only the **43rd
percentile of MU's own history**.

**Gate: `CAUTION`.** One axis genuinely contradicts the neutral-to-bearish flow bias — **analyst
revision momentum is stable-to-improving** (strong-buys 17 → 18, coverage 52 → 56, zero
downgrades through a 32% decline), reinforced by retail's defensive rather than euphoric options
posture. Cut one size step.

## Key signals

- **SK Hynix record profit MISSED expectations overnight → KOSPI crash → global memory
  selloff.** [SENT:company_news 2026-07-28]
- **Analysts 91.1% buy-or-better (51/56), one sell, zero strong-sells — crowded long.**
  [SENT:recommendation]
- **Retail narrative anchored on a "$1,000 rebound" while price is $820.53.**
  [SENT:company_news 2026-07-24]
- **Retail options flow was DEFENSIVE: ≤5-lot net -$34.3M calls, +$19.7M puts.**
  [SENT:retail_vs_inst DUCKDB]
- **Institutions did the premium selling: 51–500 and >500 lots = -$111.4M of the -$120.1M net.**
  [SENT:retail_vs_inst DUCKDB]
- **Short interest 3.21% / 36.21M sh, days-to-cover 1.0, borrow 0.27–0.40% → EASY.**
  [SENT:short_float fz semi-monthly] [SENT:borrow WebSearch:fintel.io]
- **No positioning extreme: P/C z = -1.239 (`NORMAL`); IV rank at 43rd self-percentile.**
  [SENT:pc_zscore] [SENT:iv_rank]

## Detailed findings

### News flow

`curl .../company-news?symbol=MU&from=2026-07-14&to=2026-07-28` returned **245 articles**, but
**the earliest is dated 2026-07-23** — the free tier delivered a **6-day window, not the
requested 14** (recorded under Source errors). **Look-ahead guard applied: no article is dated
after 2026-07-28.**

**Article volume by date — a 10× escalation:**

| date | articles | MU close | change |
|---|---:|---:|---:|
| 2026-07-23 | 9 | 990.21 | +3.20% |
| 2026-07-24 | 54 | 920.95 | -6.99% |
| 2026-07-25 | 10 | — | weekend |
| 2026-07-26 | 14 | — | weekend |
| 2026-07-27 | 64 | 900.20 | -2.25% |
| **2026-07-28** | **94** | **820.53** | **-8.85%** |

**The narrative arc, dated:**

- **2026-07-23 — unambiguously BULLISH.** *"Micron gains as Musk thanks it for 'significant'
  memory chip allocation"*, *"Why Micron Stock Popped Today"*, *"Micron, SK Hynix Stocks Rise
  After Google Earnings"*, *"S&P 500 Q2 Earnings: Stripping Out the Outsized Impact of Alphabet
  and Micron"*. MU closed **+3.20%** at 990.21. *(This is the same session phase-5 flagged as
  the GEX regime flip.)*
- **2026-07-24 — the turn.** *"AI Memory Stocks Lead Chip Selloff"*, *"SK Hynix and Micron Sink
  6%, SanDisk Drops 9% as Korea Chip Selloff Hits U.S. Memory Stocks"*, *"Micron (MU) Down 18.4%
  Since Last Earnings Report: Can It Rebound?"*. **Note the bullish counter-current already
  present**: *"Micron Is A Strong Buy Again Because Of Kimi K3"*, *"Micron Boosts HBM4 Ramp-Up"*,
  *"MU, SKHY, STX, WDC And Other Memory Stocks Tumble — Evercore's Daryanani Believes
  Supply-Demand Imbalance Is Going To Get Bigger In 2027"*.
- **2026-07-28 — capitulation-grade volume and the proximate trigger.**
  *"SK Hynix's Record Profit Misses Investors' Lofty AI Expectations"*, *"SK Hynix Stock Drops
  on Disappointing Earnings"*, *"SK Hynix's Worst Month Since 2008"*, *"The Korean Stock Market
  Crashes Overnight"*, *"SK Hynix, Samsung Drag Down KOSPI as China Chip Fears Spread"*,
  *"Nasdaq-100 slides into correction as global chip and memory stocks sell off"*, *"U.S. chip
  stocks extend losses on AI financing, China competition fears"*, *"SNDK Stock Plunges Over 30%
  In 3 Days"*, *"Why Micron Stock Just Dropped Again"*.

**Lead/lag: the news LED the tape by roughly one session, then coincided with it.** The Korea
selloff was already a headline on 7/24; the SK Hynix print landed overnight into 7/28 and MU
gapped **-6.73%** (phase-5 `fz Gap`) before falling further intraday to close -8.85%. **This was
not a stealth repricing — it was a well-telegraphed, heavily-covered event.**

**Two observations that matter downstream:**
1. **"Record profit misses lofty expectations" is a cycle-top tell, not a demand failure.**
   SK Hynix earned a *record*. The stock fell because expectations exceeded even that. This is
   the sentiment-layer expression of phase-7b's `peNormalizedAnnual` 108.93 finding and
   phase-6's "shortage, not oversupply" counter-fact — **the industry's results are excellent
   and the market is de-rating them anyway.**
2. **Note the macro cross-current the same day:** *"Stock Market Today: Dow Leaps 650 Points"*,
   *"Dow Gains 500 Points"*, *"Equities Mostly Rise Intraday as Fed Meeting Begins"* alongside
   *"Nasdaq-100 Hits Correction Territory"*. **Dow +650 while NDX entered correction** — a
   violent intra-market rotation, exactly matching phase-0.5 (SPY +0.24%, NVDA +0.25%,
   SNDK -14.25%) and `fz` breadth (70.97% of the S&P green).

### Analyst-revision momentum

From `/stock/recommendation` (the direction, not the level — level was covered in phase-7b):

| Period | Strong Buy | Buy | Hold | Sell | Strong Sell | Total |
|---|---:|---:|---:|---:|---:|---:|
| 2026-04-01 | 17 | 31 | 3 | 1 | 0 | 52 |
| 2026-05-01 | 17 | 32 | 3 | 1 | 0 | 53 |
| 2026-06-01 | 18 | 33 | 3 | 1 | 0 | 55 |
| **2026-07-01** | **18** | **33** | **4** | **1** | **0** | **56** |

**Revision momentum is stable-to-improving, and this is the phase's key contrary finding.**
Over four months: strong-buys **+1**, buys **+2**, holds **+1**, sells **unchanged at 1**,
strong-sells **unchanged at 0**, total coverage **+4 (52 → 56)**. **Not a single downgrade to
sell occurred while MU fell 32% from its peak.**

Per the interpretation heuristic, *deteriorating* analyst revisions alongside a bearish setup
would confirm the thesis. **The opposite is observed** — the sell side is adding coverage and
upgrading marginally into the drawdown. **This is a genuine contrary axis for the
neutral-to-bearish flow bias.**

Read the other way, it is also the crowding risk: **91.1% buy-rated with one sell means the
downgrade pipeline is nearly full and the upgrade pipeline nearly empty.** Both readings are
true; they operate on different horizons (revisions are a lagging confirm, crowding is a
forward risk).

**Cross-source (D6) — NOT AVAILABLE.** `fz quote MU --agent` remains degraded to 14 fields
(`phase-0-intake.md`) and **carries no `Recom` or `Target Price`**, and Finnhub
`/stock/price-target` is paid-tier. **No independent vendor cross-check of the consensus was
possible; no divergence can be reported either way.** Recorded as a blind spot, not as agreement.

### Retail vs institutional

Lit-tape premium by trade size (`lib/duckdb-cuts.md §A`; ask = bought, bid = sold):

| bucket | type | trades | contracts | bought | sold | **net bought** |
|---|---|---:|---:|---:|---:|---:|
| **retail (≤5)** | call | 115,617 | 175,542 | $270.1M | $304.4M | **-$34.3M** |
| **retail (≤5)** | put | 97,580 | 145,728 | $332.2M | $312.6M | **+$19.7M** |
| small (6–50) | call | 11,439 | 158,613 | $297.3M | $281.1M | +$16.2M |
| small (6–50) | put | 8,579 | 123,047 | $303.4M | $313.6M | -$10.2M |
| **mid (51–500)** | call | 537 | 59,753 | $77.3M | $105.5M | **-$28.2M** |
| **mid (51–500)** | put | 554 | 59,638 | $68.7M | $134.1M | **-$65.4M** |
| block (>500) | call | 1 | 599 | $0.5M | $0.0M | +$0.5M |
| **block (>500)** | put | 12 | 13,664 | $5.5M | $23.9M | **-$18.3M** |

**Two findings, and the first overturns the expected setup:**

1. **Retail was DEFENSIVE, not euphoric.** The ≤5-contract bucket **net sold $34.3M of calls and
   net bought $19.7M of puts** — a net -$14.6M premium position leaning *bearish*. **The
   textbook "retail call euphoria + dark-pool distribution" fade signature from the
   interpretation heuristics does NOT fire, and this phase does not claim it.**
2. **Institutions did essentially all of the premium selling.** The mid (51–500) and block
   (>500) buckets net **-$111.4M** of the **-$120.1M** total net premium sold measured in
   phase-1 — **92.8% of it.** Combined with phase-2's regular-hours dark-pool distribution
   (mega buy_ratio 0.227) and phase-3's institutional put-writing campaign at 750/800, **the
   institutional footprint is coherent: sell premium, distribute stock, underwrite the
   downside at 750–800.**

**Reconciling the apparent contradiction with the news:** the 7/24 headline says retail is
"eyeing a clean rebound above $1,000" — a *narrative about retail equity sentiment*. The
options tape says retail small-lots hedged. **These are different populations and different
instruments; both are reported, neither is suppressed.** The honest conclusion is that
**retail sentiment is bullish in commentary but retail's actual options positioning was not**,
which materially weakens any fade-the-retail argument.

### Short interest & borrow

| metric | value | as-of / source |
|---|---:|---|
| **Short float** | **3.22%** | `fz`, semi-monthly settlement |
| **Short interest (shares)** | **36.21M** (≈3.21% of shares out) | latest, WebSearch:fintel.io |
| Prior FINRA settlement | 32M shares (2.80% of out) | **2026-06-30** |
| **Days to cover** | **0.69** (`fz Short Ratio`) / **1.0** (WebSearch, on 60.3M ADV) | — |
| **Borrow fee** | **0.27% – 0.40%** | 2026-07-13, WebSearch:fintel.io / shortinteresttracker.com |
| Shares available to short | ~10M | 2026-07-13 |
| **HTB status** | **EASY — not hard to borrow** | — |

`[SENT:short_float fz semi-monthly]` `[SENT:borrow WebSearch:fintel.io]`

**There is no squeeze dynamic in MU in either direction.**
- **For a bearish thesis:** shorting is cheap (0.27–0.40%) and unconstrained (~10M shares
  available). **The squeeze-risk VETO condition in the rubric does not trigger.**
- **For a bullish thesis:** at 3.2% of float with **~1 day to cover**, there is **no short base
  to squeeze.** Any "shorts will fuel the bounce" argument is unavailable on this name.
- Short interest is **rising modestly** — 32M (6/30 settlement) → 36.21M latest, i.e. **+13%**,
  or 2.80% → 3.21% of shares out. Directionally consistent with the bearish tape, but the
  absolute level remains low.
- Peer context (phase-7b): MU's 3.22% sits below WDC (6.81%) and SNDK (5.38%).

**Staleness note:** the `fz` figure is the exchange semi-monthly settlement (~2-week lag) and
the 32M FINRA print is dated **2026-06-30**, i.e. **before the entire -32% drawdown.** The 36.21M
"latest" figure post-dates it but its exact settlement date was not confirmed. **The true
current short interest after this week's decline is unobservable from free sources.**

### Positioning extremes

| metric | value | extreme? |
|---|---:|---|
| P/C ratio z-score (20d) | **-1.239** (`extreme = NORMAL`) | **No** — \|z\| < 2 |
| current P/C vs 20d mean | 0.8671 vs 1.0271 (σ 0.1291) | call-heavy vs recent norm, not extreme |
| IV rank | 83.4835 | **No** — 90th universe %ile but **43rd self-percentile** |
| IV percentile (`iv-percentile-zscore`) | **48.65**, z +0.365, `NORMAL` | **No** |

**No contrarian trigger exists on any positioning axis.** The heuristic requires |P/C z| > 2;
MU is at -1.24. IV is at its own median. Per phase-5, **realised vol (109.12%) exceeds implied
(96.04%)** — the crowd is, if anything, *under*-hedged relative to how the stock is moving,
which is the opposite of a sentiment extreme.

## Divergences

1. **Crowd is long, institutions are distributing.** Analysts 91.1% buy-or-better with zero
   downgrades through a -32% decline, retail narrative anchored on a "$1,000 rebound", and
   insiders selling (7b: MSPR -100 in four of ten months) — while phase-2 measured
   regular-hours dark-pool distribution (mega buy_ratio **0.227**) and phase-7c measures
   institutions selling 92.8% of the day's net premium.
2. **Retail commentary is bullish but retail options positioning is defensive.** ≤5-lot flow net
   sold $34.3M of calls and net bought $19.7M of puts. **The two retail signals disagree**, so
   neither a euphoria-fade nor a retail-capitulation read is supportable.
3. **Analyst revisions are improving while price and flow deteriorate.** Coverage 52 → 56 and
   strong-buys 17 → 18 across four months in which MU fell 32%. **This is the one axis that
   contradicts the neutral-to-bearish flow bias** and is the basis for `CAUTION` rather than
   `CONFIRM`.
4. *(Noted, not counted — it is a within-industry rather than crowd-vs-flow divergence)*
   **Record fundamentals, falling prices.** SK Hynix printed a record profit and fell; MU has
   4/4 beats, +166.98% revenue growth and 76.6% gross margin (7b) and is -32.4% from its peak.

## Source calls (audit trail)

| Source / command | Result | Key value(s) |
|---|---|---|
| `curl .../company-news?symbol=MU&from=2026-07-14&to=2026-07-28` | **OK (245 articles) — but window truncated to 2026-07-23→07-28** | 94 articles on 7/28; "SK Hynix's Record Profit Misses Investors' Lofty AI Expectations"; "Retail Is Eyeing Clean Rebound Above $1,000" (7/24) ← `.[].headline`, `.[].datetime` |
| `curl .../stock/recommendation?symbol=MU` | **OK** | 2026-04→07: strongBuy 17→**18**, buy 31→**33**, hold 3→**4**, sell **1→1**, strongSell **0→0**; total 52→**56** |
| `fz quote MU --agent` (`Recom`, `Target Price`) | **DEGRADED — fields absent** | 14-field payload; **no cross-source check possible** |
| `curl .../stock/price-target` (phase-7b) | **PAID** | `{"error":"You don't have access to this resource."}` |
| DuckDB §A small-lot split (`bot-eod-report-2026-07-28.parquet`) | **OK** | retail ≤5: calls **-$34.3M**, puts **+$19.7M**; mid+block: **-$111.4M** of -$120.1M total |
| `fz screen --view ownership` (phase-0/7b carry) | **OK** | Short Float **3.22%**, Short Ratio **0.69**, Float 1.12B, Inst Own 78.11% |
| WebSearch — borrow / SI | **OK** | borrow **0.27–0.40%** (2026-07-13), ~10M shares available, SI **36.21M / 3.21%**, FINRA 32M @ 2026-06-30, **days-to-cover 1.0**, **not HTB** |
| `uw historical pc-ratio-zscore` (phase-5 carry) | **OK** | z = **-1.239**, `extreme = NORMAL` |
| `uw historical iv-percentile-zscore` (phase-5 carry) | **OK** | `iv_percentile` **48.65**, `regime = NORMAL` |

## Source errors

1. **Finnhub `company-news` returned a truncated window.** Requested `from=2026-07-14`; the
   earliest article returned is dated **2026-07-23** — a **6-day** window rather than the
   specified 14. The tone assessment therefore covers 7/23–7/28 only, and **no claim is made
   about 7/14–7/22 sentiment.** This biases the window toward the selloff itself; the pre-event
   baseline is not observed.
2. **`fz quote MU` degraded to 14 of 84 fields** (carried from `phase-0-intake.md`), so the
   D6 analyst cross-source (`Recom` 1–5 scale + `Target Price`) **could not be run.** Combined
   with Finnhub `/stock/price-target` being paid-tier, **the analyst dimension rests on a single
   vendor with no cross-check.**
3. **Short-interest staleness:** the `fz` short float is the exchange semi-monthly settlement
   (~2-week lag) and the corroborating FINRA figure settles **2026-06-30**, before the drawdown.
   **Post-selloff short interest is unobservable from free sources.**

## DATA NOTE / CORRECTION

- **The expected "retail euphoria" setup was tested and REJECTED on the data.** The
  interpretation heuristics anticipate *"retail call euphoria + dark-pool distribution +
  bullish flow → CAUTION→VETO"*. The lit small-lot cut shows the opposite (retail net sold
  calls, net bought puts), so **that heuristic is explicitly not invoked** despite the bullish
  retail *narrative* in the news. Both signals are reported and the conflict is left standing
  rather than resolved in favour of the tidier story.
- **Two days-to-cover figures appear and are both quoted:** `fz Short Ratio` **0.69** and the
  WebSearch-derived **1.0** (36.21M / 60.3M ADV). They differ because of the ADV denominator
  and settlement date, not because either is wrong. **Both are ≪ 2 days; the conclusion (no
  squeeze) is insensitive to the difference.**
- No value in this file was transcribed from an unparsed read; every Finnhub payload
  round-tripped through `jq` and the DuckDB cut was computed on validated parquet.

## Verdict for downstream

```
sentiment_signal:  BEARISH
crowd_state:       CROWDED_LONG
short_interest:    3.21% of shares out (36.21M sh) [fz 3.22%, semi-monthly] ;
                   days_to_cover: 0.69 (fz) / 1.0 (ADV-derived) ;
                   borrow: EASY (0.27-0.40%, ~10M shares available) [WebSearch:fintel.io]
tier_adjustment:   CAUTION
divergences:
  - "Analysts 91.1% buy-or-better with ZERO downgrades through a -32% drawdown, while
     institutions distribute (DP mega buy_ratio 0.227 regular-hours) and insiders sell."
  - "Retail commentary anchored on a '$1,000 rebound' but retail OPTIONS flow was defensive
     (<=5-lot: -$34.3M calls, +$19.7M puts) — the two retail signals disagree."
  - "SK Hynix printed a RECORD profit and the stock fell; MU has 4/4 beats and 76.6% GM and is
     -32.4% from its peak. Results are excellent and the market is de-rating them."
key_risks:
  - "Crowded long with an empty downgrade pipeline: 51 of 56 analysts at buy-or-better and only
     one sell rating, with the stock 34.62% below its 52w high — downgrade risk is asymmetric."
  - "No squeeze fuel in either direction: 3.2% short float, ~1 day to cover, 0.27-0.40% borrow.
     A bounce cannot be short-covering-driven, and a short cannot be squeezed out."
  - "Post-drawdown short interest is unobservable (FINRA settles 2026-06-30, pre-selloff);
     the crowd read could shift materially on the next settlement."
```

**How the gate was computed.** The flow bias from phases 1–7 is **NEUTRAL-TO-BEARISH**. Testing
the crowd against it:

| axis | finding | vs neutral-to-bearish bias |
|---|---|---|
| News tone | overwhelmingly negative, escalating 9 → 94 articles/day; SK Hynix miss as trigger | **CONFIRMS** |
| Crowd positioning | **CROWDED_LONG** — analysts 91.1% buy, retail narrative at "$1,000", insiders selling | **CONFIRMS** (supply overhead; crowd is offside) |
| Short interest / borrow | 3.21%, DTC ~1.0, borrow 0.27–0.40%, **not HTB** | **CONFIRMS** (no squeeze hazard to a short) |
| Retail vs institutional | institutions sold 92.8% of net premium and distributed in the DP | **CONFIRMS** |
| **Analyst revision momentum** | **stable-to-improving: strong-buys 17→18, coverage 52→56, zero downgrades through -32%** | **CONTRADICTS** |
| Retail options posture | ≤5-lot net **bought puts**, sold calls — defensive, not euphoric | **weakly contradicts** (removes the fade-the-crowd catalyst) |
| Positioning extremes | P/C z -1.239 (`NORMAL`), IV rank at 43rd self-%ile | **NEUTRAL** (no contrarian trigger) |

**One clear contrary axis (analyst revision momentum), reinforced by a second weak one (retail's
defensive options posture) → `tier_adjustment = CAUTION` → phase-9 cuts one size step.**

**Why not `CONFIRM`:** the rubric's `CONFIRM` requires the crowd to confirm **and** the name not
to be crowded. MU is **crowded long**, and analyst revisions are moving *against* the bearish
thesis.

**Why not `VETO`:** the rubric's `VETO` requires the crowd to be *crowded the same way as the
thesis* plus a squeeze/short-interest mismatch. **Neither holds.** The crowd is long while the
flow bias is bearish (opposite, not aligned), and borrow is easy at 0.27–0.40% with ~1 day to
cover — **there is no squeeze hazard.** *(Note: for a hypothetical **long** thesis this phase
would read `VETO` — crowded long + institutional distribution + insider selling is the classic
distribution-into-strength stack.)*

**Interaction with phase-7b that phase-9 must reconcile:** 7b returned **`VETO` on the
directional short** (fundamentals contradict on 2 of 3 axes); 7c returns **`CAUTION`** on the
same bearish lean. **Neither gate can raise conviction — both are downside-only.** Taken
together they permit **no directional short** (7b) and, by their own logic, would penalise a
long even harder (7c would `VETO` it). **The two gates jointly point at a non-directional or
watch-only conclusion, which phase-9 must confront rather than average away.**

- **Two items for phase-8b's debate:** (1) *Does "record profit misses expectations" mark the
  top, or the maximum-pessimism entry?* Both readings are consistent with every fact in this
  phase. (2) *Does a 91.1% buy-rated consensus with one sell make MU more dangerous (downgrade
  pipeline) or more supported (no capitulation from the sell side)?*
- **One item for phase-9's calendar:** short interest re-settles semi-monthly; the next print
  will be the first to include the drawdown. **The current SI read is pre-selloff and should be
  treated as stale.**
