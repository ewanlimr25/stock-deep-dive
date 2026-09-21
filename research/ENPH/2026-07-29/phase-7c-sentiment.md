# Phase 7c — Sentiment, Positioning & Short Interest

**Ticker:** ENPH
**As-of date:** 2026-07-29
**Generated:** 2026-07-30T03:26:00Z
**Upstream phases cited:** `phase-0-intake.md`, `phase-0.5-context.md`, `phase-1-flow.md`, `phase-2-dark-pool.md`, `phase-3-positioning.md`, `phase-4-structure.md`, `phase-5-historical.md`, `phase-6-macro.md`, `phase-7-insights.md`, `phase-7b-fundamentals.md`

## Summary

**The crowd is already short, it added into the print, and Wall Street's price targets sit
23–28% above spot. This is a bad place to initiate a fresh short even though the direction is
right — `tier_adjustment` VETO.**

**Short interest rose through the binary event.** `Short Float` is **17.94%** of the 127.77M
float [`fz`, semi-monthly settlement], **up from 17.55%** at the 07-27 run — the short base did
not cover into the print, it **grew**. A fresh directional short here means joining a trade
that already owns ~18% of the float, which is precisely the archetype the gate's VETO rubric
names ("heavily-shorted name on a fresh short thesis").

**News tone is decisively negative on direction — and this phase repairs two gaps
`phase-7b-fundamentals.md` had to declare unmeasured.** The 14-day Finnhub news feed (18 items,
**zero look-ahead** after correcting my first threshold — see `## Source errors`) contains a
**complete analyst sweep on 2026-07-29: six price-target CUTS and zero raises.** Mizuho → $45,
BMO → **$37**, Wells Fargo → $44, Oppenheimer → $56, RBC → $47, plus TD Cowen → $48 on 07-20,
and **GLJ Research reiterating SELL at $24.47**. Negative revision momentum, unambiguous.

**But the same sweep is the strongest argument against shorting:** every one of those brokers
**maintained** its rating (3 Outperform/Overweight, 2 Neutral/Market Perform, 1 Hold, 1 Sell),
and the seven targets **average $43.07 / median $45 — 22.8% / 28.3% ABOVE the 35.07 close.**
The lowest non-Sell target, BMO's $37, is still **+5.5%**. Only GLJ's $24.47 sits below spot.

**And `/stock/recommendation` — the free endpoint, which works where
`recommendation-trends` 404'd — supplies the ratings trend 7b could not get:**
holds **19 → 18 → 21**, sells **5 → 6 → 4**, buys flat at 12, strongBuy flat at 4;
bullish share **40% → 40% → 39%**. A slow drift toward HOLD, not a downgrade cycle.

**The Q2 "beat" was corrected to in-line — this settles the ambiguity 7b flagged.** Benzinga
published *"Q2 Adj. EPS $0.47 Beats $0.46 Estimate"* at 16:07 on 07-28, then issued
**"CORRECTION: Enphase Energy Q2 Adj. EPS $0.46, Inline"** at 17:34, and ChartMill reported
*"Posts In-Line Q2 Earnings."* Finnhub's 0.46 vs 0.4678 was right. **Q2 was a revenue beat
(+0.67%) with EPS in line** — and the Q3 guide of $290–320M straddles the **$304.253M**
consensus, i.e. **also in line**, not above.

**Retail and institutions are on opposite sides, and institutions are short.** Retail bought
cheap near-dated calls — the Aug-07 C37 at **$218,770 across 99 trades (~12 contracts/ticket),
~96% ask-side** — plus a far-OTM 07-31 put ladder at ~$0.04/contract. Institutions bought size
puts in single tickets: **Oct-16 P35, $196,240 in ONE trade (446 contracts)** and the
**$2,837,716 Jan-2028 P30** at 92% ask-side, while distributing stock off-exchange
(`sell_ratio` 0.610). For a bearish thesis this divergence **confirms** — you are aligned with
the institutions.

**No positioning extreme exists to trade against.** `pc-ratio-zscore` **+0.482, `extreme`
NORMAL** (nowhere near |z| > 2) and `iv_rank` 47.05 is at ENPH's **15.6th** self percentile —
low, not extreme-high. **Borrow fee / HTB status could not be obtained** (Fintel/ORTEX are the
sources; no values returned) → **borrow: n/a**, a blind spot, not a benign reading.

## Key signals

- **`Short Float` 17.94% of float, UP from 17.55%** — the short base **added** through the
  print [SENT:short_float fz semi-monthly]
- **Six analyst price-target CUTS on 2026-07-29, zero raises**; GLJ reiterates **Sell $24.47**
  [SENT:company_news]
- **Yet all 7 ratings MAINTAINED and targets average $43.07 / median $45 = +22.8% / +28.3%
  above spot** [SENT:company_news]
- **"CORRECTION: Q2 Adj. EPS $0.46, Inline"** — the beat was retracted; Q3 guide midpoint
  $305M vs **$304.253M** consensus = in line [SENT:company_news]
- **Ratings drift to HOLD: hold 19 → 18 → 21, sell 5 → 6 → 4, bull share 40% → 39%**
  [SENT:recommendation]
- **`Short Ratio` 3.05 days** (`fz`) / **2.63 days** on 6.38M avg volume [WebSearch] — **cheap
  to cover, weak squeeze fuel** [SENT:short_ratio fz]
- **Retail vs institutional DIVERGENCE:** retail 99-ticket call buying ($218,770) vs
  institutional single-ticket put buying ($196,240 in 1 trade; $2.84M Jan-2028 P30)
  [SENT:retail_vs_inst]
- **`pc-ratio-zscore` +0.482, `extreme` NORMAL**; `iv_rank` 47.05 = 15.6th self percentile —
  **no contrarian trigger** [SENT:positioning_extremes]
- **17.94% is 5th of 18 solar names and tied with SEDG's 17.97%** — a sector condition, not an
  ENPH-specific setup [SENT:peer_si fz]
- **Borrow fee / HTB: NOT OBTAINABLE** → blind spot [SENT:borrow_unavailable]

## Detailed findings

### A — News flow (14-day tone; lead/lag vs price)

`curl .../company-news?symbol=ENPH&from=2026-07-15&to=2026-07-29` → **18 items**.
**Look-ahead guard: 0 items dated after the as-of.** Max `datetime` = 1785331681; the correct
end-of-day-ET boundary is 1785383999 (my first threshold was wrong — see `## Source errors`).

| Date · time | Source | Headline |
|---|---|---|
| 07-16 06:05 | SeekingAlpha | *Enphase: Rough Short-Term, But Tailwinds Ahead* |
| **07-20 10:10** | Benzinga | **TD Cowen Maintains Hold — LOWERS PT to $48** |
| 07-22 10:15 | Benzinga | *Here's How Much $100 Invested In ENPH 10 Years Ago Would Be Worth Today* |
| 07-27 13:35 | Benzinga | *7 Information Technology Stocks Whale Activity In Today's Session* |
| **07-28 10:21** | Benzinga | **GLJ Research Maintains SELL — Raises PT to $24.47** |
| 07-28 16:07 | Benzinga | *Q2 Adj. EPS $0.47 **Beats** $0.46 Est, Sales $291.854M Beat $289.917M Est* |
| 07-28 16:10 | Benzinga | **Sees Q3 Sales $290.000M–$320.000M vs $304.253M Est** |
| 07-28 16:48 | Benzinga | *Stock Rises on Q2 Earnings Beat as Company Accelerates AI Data Center Strategy* |
| **07-28 17:34** | Benzinga | **CORRECTION: Q2 Adj. EPS $0.46, *Inline*, Sales $291.854M Beat** |
| 07-28 20:43 | ChartMill | *Posts **In-Line** Q2 Earnings, Stock Rebounds* |
| 07-29 02:13 | SeekingAlpha | *Q2 2026 Earnings Call Transcript* |
| **07-29 09:07** | Benzinga | **Mizuho Maintains Neutral — LOWERS PT to $45** |
| **07-29 10:42** | Benzinga | **BMO Capital Maintains Market Perform — LOWERS PT to $37** |
| **07-29 10:45** | Benzinga | **GLJ Research Reiterates SELL — Maintains $24.47 PT** |
| **07-29 12:08** | Benzinga | **Wells Fargo Maintains Overweight — LOWERS PT to $44** |
| **07-29 12:29** | Benzinga | **Oppenheimer Maintains Outperform — LOWERS PT to $56** |
| 07-29 12:34 | Benzinga | *Trump Bans Chinese Humanoid Robots; SK Hynix Volatility; Fed Decision Looms* |
| **07-29 13:28** | Benzinga | **RBC Capital Maintains Outperform — LOWERS PT to $47** |

**Tone verdict: BEARISH on direction, BULLISH on level — and the two must be reported
separately.**

**Direction (what the spec says to weight):** **six price-target cuts on 07-29 alone, and zero
raises.** GLJ's 07-28 "raise" to $24.47 is a **Sell** target **30% below spot** and is not a
bullish revision. Adding TD Cowen's 07-20 cut to $48, **seven of seven revisions in the window
were downward or reiterated-bearish.** This is unambiguous negative revision momentum and it
**confirms** the phases 1–7 bearish bias.

**Level (the counterweight):** every broker **maintained** its rating and the targets are far
above spot:

| Broker | Rating (maintained) | New PT | vs 35.07 close |
|---|---|---:|---:|
| Oppenheimer | Outperform | **$56** | **+59.7%** |
| TD Cowen | Hold | $48 | +36.9% |
| RBC Capital | Outperform | $47 | +34.0% |
| Mizuho | Neutral | $45 | +28.3% |
| Wells Fargo | Overweight | $44 | +25.5% |
| BMO Capital | Market Perform | **$37** | **+5.5%** |
| GLJ Research | **Sell** | **$24.47** | **−30.2%** |
| **Mean / Median** | | **$43.07 / $45** | **+22.8% / +28.3%** |

**Only one of seven targets sits below spot.** Even the most conservative non-Sell house (BMO,
$37) implies upside. **Shorting into a consensus that sees 23–28% upside is an uncomfortable
trade** — the sell-side is cutting *toward* the price, not below it.

**Lead/lag against price — a genuinely useful sequencing read.** The earnings headline at
**16:07** on 07-28 is consistent with the documented **postmarket** release
(`phase-0-intake.md`), which implies these timestamps are **Eastern**, not UTC. Under that
reading the six PT cuts landed between **09:07 and 13:28 ET on 07-29 — during the intraday
collapse** that `phase-1-flow.md` §C measured (high 39.60 at the open → close 35.07, **−11.44%
from the high**, closing $0.11 off the low). Sequence:

1. **07-28 postmarket:** results out; initial "beat" headline; *"Stock Rises"* — the after-hours
   read was **positive**.
2. **07-28 17:34:** the **CORRECTION** downgrades the print from "beat" to "in line."
3. **07-29 open:** ENPH still **gapped +7.08%** (`fz` `Gap`, `phase-5-historical.md` §G).
4. **07-29 09:07 → 13:28:** six PT cuts roll in; the stock bleeds all session to close on the
   low.

**So the news did not lead the reversal — the reversal ran alongside and after it.** The gap up
happened *after* the correction was public, and the decline coincided with the target cuts.
That argues the selling was **positioning-driven, not headline-driven** — consistent with
`phase-2-dark-pool.md`'s distribution (gap **bought** above mid at a $37.56 VWAP in the first
11 minutes, then 15 consecutive below-mid blocks) and with `phase-7-insights.md`'s finding that
price closed **3.3% below the dark-pool VWAP of 36.27**.

> **Timezone caveat, stated rather than assumed.** `jq strftime` renders UTC by default. If the
> feed's `datetime` is genuinely UTC, the six cuts would be **pre-market** (05:07–09:28 ET)
> rather than intraday. I judge ET far more likely because a 16:07 earnings headline matches a
> postmarket release while 12:07 ET does not. **The ordering of events is identical under either
> reading, and so is the conclusion** — the cuts were public before or during the decline, and
> the gap up occurred after the correction. Only the intraday attribution shifts.

One further sentiment datapoint, undated in results and therefore not weighted: a Seeking Alpha
piece titled *"Enphase Energy: A Top Short Squeeze Idea For 2026"* exists. A public
retail-facing squeeze narrative on a name that is 17.94% short is itself crowding information —
it means the squeeze thesis is **known and shared**, which cuts against its payoff.

### B — Analyst-revision momentum

`curl .../stock/recommendation?symbol=ENPH` — **this free endpoint works**, where
`phase-7b-fundamentals.md` §G found `/stock/recommendation-trends` **404s**. It repairs part of
7b's declared blind spot. **Look-ahead guard: 0 rows with `period` > 2026-07-29.**

| Period | strongBuy | buy | hold | sell | strongSell | Total | Bullish share |
|---|---:|---:|---:|---:|---:|---:|---:|
| **2026-07-01** | 4 | 12 | **21** | **4** | 0 | 41 | **39.0%** |
| 2026-06-01 | 4 | 12 | 18 | 6 | 0 | 40 | 40.0% |
| 2026-05-01 | 4 | 12 | 19 | 5 | 0 | 40 | 40.0% |
| 2026-04-01 | 4 | 11 | 19 | 7 | 0 | 41 | 36.6% |

**Direction: a slow drift toward HOLD — deteriorating, but mildly.**
`hold` rose **19 → 18 → 21** (+3 from June, the largest single move in the table), while
`buy` (12) and `strongBuy` (4) have been **frozen for four months** and `sell` eased
**6 → 4**. Bullish share is flat-to-down: 36.6% → 40.0% → 40.0% → **39.0%**.

**Two honest readings, and I will not collapse them:**
- **Confirming the bearish bias:** conviction is draining into the middle. Nobody has upgraded
  in four months; the marginal analyst moves to HOLD. With **21 of 41 holds (51%)**, the
  modal Street view is "no opinion."
- **Tempering it:** this is **not** a downgrade cycle. `sell` count actually *fell* (6 → 4) and
  `strongSell` is **zero across all four months**. If the sell-side were capitulating you would
  see buys converting to sells; instead you see one new hold.

**Cross-source check (D6) — cannot be performed.** `fz quote`'s `Recom` and `Target Price` are
both **`null`** (leaf degraded to 14/84 fields, `phase-0-intake.md`), so the Finnhub-vs-`fz`
divergence test the spec requests is unavailable. **However**, the news feed (§A) provides an
independent, higher-quality substitute: seven **named brokers with dated, specific targets**,
which is strictly better than a single blended `Recom` scalar. Recorded as: **cross-source
check unavailable via `fz`, superseded by the named-broker sweep in §A.**

> **Net effect on 7b's blind spot.** `phase-7b-fundamentals.md` §G declared the analyst leg
> **UNMEASURED** after four dead routes. Two of those routes are now recovered here — the
> **ratings distribution and trend** (`/stock/recommendation`) and **seven dated price targets**
> (news feed). **The analyst leg is no longer a blind spot**; it reads *negative on revision
> direction, bullish on absolute level*. Phase 8/8b/9 should use this and disregard 7b's
> UNMEASURED flag, which was correct at the time it was written.

### C — Retail vs institutional

No new tooling required — the split is legible in phases 1–3 by **ticket size**, and the
divergence is stark.

**Retail-signature flow — small tickets, cheap contracts, ask-side, near-dated calls:**

| Contract | Premium | Volume | Trades | Contracts/ticket | Read |
|---|---:|---:|---:|---:|---|
| **2026-08-07 C37** | **$218,770** | 1,206 | **99** | **12.2** | +5.5% OTM, **9 DTE**, ~96% ask-side |
| 2026-07-31 P28–P32 ladder | **$7,702** | 1,933 | — | — | **~$0.04/contract** — lottery tickets |
| 2026-09-04 P25 | $61,546 | 1,845 | 34 | 54 | 28.7% OTM at **$0.33** avg |
| 2026-08-14 C36 | $28,231 | 111 | 14 | 7.9 | `vol_oi_ratio` 27.75, 87% IV |

**Institutional-signature flow — single large tickets, at-the-money or long-dated puts:**

| Contract | Premium | Size | Trades | Read |
|---|---:|---:|---:|---|
| **2026-10-16 P35** | **$196,240** | 446 | **1** | ATM, 79 DTE, `delta` −0.368, ask side |
| **2028-01-21 P30** | **$2,837,716** | 2,000 OI added | cluster of 5 tickets ≥96 | **92% ask-side**, `dte` 541, opened **pre-print** |
| 2026-09-18 C70 (sold) | $55,196 | 1,604 OI | — | far-tail call **written** |
| Sep C40 / Jan-27 C55 / Jan-28 C75 (sold) | **$405,922** | — | — | long-dated call **supply** |

**Verdict: clear DIVERGENCE — and it confirms the bearish thesis.**

- **Retail is bullish and short-dated.** The single cleanest bullish expression of the day is a
  **9-DTE, +5.5%-OTM call bought across 99 small tickets**. That is a retail/momentum signature,
  and it needs a move within two weeks or it expires worthless.
- **Institutions are bearish and long-dated.** The two largest committed positions in the run
  are **puts bought in single tickets** — $196,240 in one print, and **$2.84M of 18-month
  $30 puts opened hours before the earnings release**. Simultaneously $405,922 of long-dated
  **calls were written**.
- **Institutions were also net sellers of the stock itself** — `phase-2-dark-pool.md` large-tier
  `sell_ratio` **0.610** across 188 trades, price closing **3.3% below** the dark-pool VWAP of
  36.27.
- **Even the company is not buying:** `Repurchases of common stock` = **$0**
  (`phase-7b-fundamentals.md` §F).

Per the spec's heuristic, retail euphoria + dark-pool distribution is the distribution-into-
strength signature that would VETO a *long*. **Here the thesis is short, so this axis CONFIRMS**
— the lit retail call flow is the exit liquidity, not the signal.

### D — Short interest and borrow

**Primary (`fz`, point-in-time)** — via `fz screen --tickers ENPH --view ownership --agent`,
the validated substitute for the degraded `fz quote` leaf (`phase-0-intake.md`):

| Field | Value |
|---|---|
| **`Short Float`** | **17.94%** [fz, semi-monthly settlement — ~2-week lag] |
| **`Short Ratio` (days to cover)** | **3.05** |
| `Float` | 127.77M |
| `Inst Own` | 101.05% |
| `Insider Own` | 3.06% |

**Cross-source (WebSearch, prior settlement):** short interest **rose from 15.09M to 16.79M
shares = 17.55% of float**, with **2.63 days to cover** on 6.38M average daily volume
[Fintel/Benzinga]. That 17.55% matches the figure carried from the 07-27 run exactly.

**The trend is the signal: 17.55% → 17.94%. The short base ADDED through a binary event.**
At 17.94% of a 127.77M float, roughly **22.9M shares** are short. Shorts did not take profits
into an earnings print after a 30% decline — they pressed. **That is what makes this a crowded
trade rather than a contrarian one.**

**Three facts that materially temper the squeeze risk — all must be carried:**

1. **This is a sector condition, not an ENPH setup.** Per `phase-7b-fundamentals.md` §H, ENPH's
   17.94% is **5th of 18 solar names** and **statistically tied with SEDG's 17.97%**, far below
   **CSIQ 34.53%**, **RUN 28.65%** and ARRY 20.39%. Being shorted like your closest comparable
   is not a distinguishing characteristic.
2. **The short base is cheap to cover: 3.05 days** (`fz`) / **2.63 days** (WebSearch), versus
   RUN 6.57, CSIQ 5.65, ARRY 5.04, FSLR 4.06. **A ~3-day cover is weak squeeze fuel** — a
   violent short squeeze normally requires high days-to-cover *and* borrow scarcity.
3. **The squeeze thesis is publicly known** — a Seeking Alpha article titled *"A Top Short
   Squeeze Idea For 2026"* exists (§A). A shared squeeze narrative is a poorer squeeze.

**Borrow fee / HTB status: NOT OBTAINABLE → `borrow: n/a`.** WebSearch identified Fintel and
ORTEX as the tracking sources but **returned no current rate or HTB flag**. Per the spec's
pitfall, **absence of borrow data is a blind spot, not an "easy borrow" reading.** I will not
infer HTB status from the elevated short float — that is exactly the inference the spec
forbids. Consequence: the "hard" half of the VETO test (§ gate) is **unconfirmed**, and §Verdict
states how that affects the call.

### E — Positioning extremes

Reused from upstream, per the spec:

| Measure | Value | Trigger? |
|---|---|---|
| `pc-ratio-zscore` `zscore` | **+0.482** (`extreme` **NORMAL**) | **No** — spec threshold is \|z\| > 2 |
| `current_pc_ratio` / mean / std | 0.726 / 0.5607 / 0.3429 | — |
| `iv_rank` | **47.05** = **15.6th self percentile** | **No** — low, not extreme-high |
| `iv_percentile` (75 sessions) | **28**, `iv_zscore` −0.658, `regime` NORMAL | No |
| P/C self percentile (65 sessions) | 87.5th | Elevated by rank only |

**No positioning extreme exists in either direction, so no contrarian trigger is available.**
`|z|` of 0.48 is a quarter of the threshold. As `phase-5-historical.md` §D established, the P/C
distribution is strongly right-skewed (`std` 0.3429 on a `mean` of 0.5607, CV 0.61), so the
87.5th self-percentile rank and the NORMAL z-score are both true and neither is an extreme.

**Directionally important for this thesis:** `iv_rank` at the **15.6th** self percentile is the
*opposite* of the crowded-fear reading a short would want. Combined with
`phase-4-structure.md`'s `skew_ratio` **0.994** (25Δ puts *cheaper* than 25Δ calls,
`interpretation` **COMPLACENT**), **the options market is not braced for downside at all.** That
cuts two ways: cheap protection for a bear, but also no capitulation to sell into.

## Divergences

1. **Analyst revision DIRECTION (6 cuts, 0 raises) vs analyst LEVEL (mean PT $43.07 = +22.8%
   above spot, all ratings maintained, 0 strongSell).** The sell-side is cutting targets *toward*
   the price while continuing to recommend the stock. Direction confirms the bearish thesis;
   level contradicts shorting it here.
2. **Retail bullish and short-dated (Aug-07 C37: $218,770 / 99 tickets / ~96% ask-side) vs
   institutional bearish and long-dated ($196,240 ATM put in one ticket; $2.84M Jan-2028 P30 at
   92% ask-side; $405,922 of long-dated calls written; DP `sell_ratio` 0.610).** Confirms the
   thesis — retail is the exit liquidity.
3. **Short base 17.94% and RISING (from 17.55%) vs a fresh short thesis.** The crowd is already
   positioned the way this run's evidence points, and it added into the event. This is the
   crowding conflict that drives the gate.

*Secondary, noted but not counted:* `iv_rank` at the 15.6th self percentile and
`skew_ratio` 0.994 (COMPLACENT) sit oddly beside a 17.94% short base — a heavily-shorted name
whose options market charges no downside premium. Consistent if the shorts are expressed in
**stock** rather than options, which the 3.05-day cover and the absence of a put-skew bid both
support.

## Source calls (audit trail)

| # | Source / command | Result | Key value(s) ← path |
|---|---|---|---|
| 0 | Preflight: `test -n "$FINNHUB_API_KEY"`; `fz --version`; ticker pattern | **key set · fz ok · US ok** | `.env`-sourced |
| 1 | `curl .../company-news?symbol=ENPH&from=2026-07-15&to=2026-07-29` | **OK — 18 items** | 6 PT cuts on 07-29 (Mizuho $45, BMO $37, WF $44, Oppenheimer $56, RBC $47, GLJ Sell $24.47) + TD Cowen $48 on 07-20; **"CORRECTION: Q2 Adj. EPS $0.46, Inline"**; "Q3 Sales $290.000M–$320.000M vs **$304.253M Est**" ← `.[].headline` / `.datetime` / `.source`. Look-ahead: `max(.datetime)`=1785331681 < boundary 1785383999 → **0 items after as-of** |
| 2 | `curl .../stock/recommendation?symbol=ENPH` | **OK — free endpoint works** | 2026-07-01 `hold`=**21** / `sell`=**4** / `buy`=12 / `strongBuy`=4 / `strongSell`=0; 06-01 18/6; 05-01 19/5; 04-01 19/7 ← `.[]`. Look-ahead: 0 rows `period` > as-of |
| 2b | `fz quote ENPH --agent` → `.fundamentals.Recom` / `."Target Price"` | **DEGRADED** | both **`null`** — cross-source test unavailable; superseded by the named-broker sweep in §A |
| 3 | Retail-vs-institutional — reused from `phase-1-flow.md` §D–F, `phase-2-dark-pool.md` §A–B, `phase-3-positioning.md` §C | **OK** | Retail: Aug-07 C37 $218,770 / 1,206 vol / **99 trades**; 07-31 P28–P32 $7,702 / 1,933 contracts. Institutional: Oct-16 P35 **$196,240 in 1 trade**; Jan-2028 P30 **$2,837,716** at `prev_ask_volume` 2,908 vs `prev_bid_volume` 253; DP large `sell_ratio` **0.610** |
| 4 | `fz screen --tickers ENPH --view ownership --agent` (from `phase-0-intake.md`) | **OK** | `Short Float`=**17.94%**, `Short Ratio`=**3.05**, `Float`=127.77M, `Inst Own`=101.05%, `Insider Own`=3.06% |
| 4b | WebSearch: *"ENPH Enphase borrow fee hard to borrow short interest July 2026"* | **PARTIAL** | SI rose **15.09M → 16.79M = 17.55% of float**, **2.63 days** to cover on 6.38M avg vol [Fintel/Benzinga]. **Borrow fee / HTB: NOT RETURNED** → `borrow: n/a` |
| 4c | Peer SI context — `fz screen --filter ind_solar --view ownership` (from `phase-7b-fundamentals.md` §H) | **OK** | ENPH 17.94% is **5th of 18**; SEDG **17.97%**, CSIQ 34.53%, RUN 28.65%, ARRY 20.39%, FSLR 9.75% |
| 5 | Positioning extremes — reused from `phase-5-historical.md` §A/§D, `phase-0.5-context.md` | **OK** | `zscore`=**+0.482** / `extreme`=**NORMAL**; `iv_rank`=47.05 = **15.6th** self pctile; `iv_percentile`=28 |

Every Finnhub read was captured to a file before being queried and round-tripped through `jq`
on validated JSON. **Look-ahead guard applied to both dated series** (news `datetime`,
recommendation `period`) and verified to drop nothing. Derived values, stated inline: the
seven-target mean/median and percentage distances from the 35.07 close (§A), bullish-share
percentages (§B), contracts-per-ticket (§C), and shares-short from `Short Float` × `Float`
(§D).

## Source errors

No fatal errors. Finnhub key present, ENPH is US-listed, `fz` available → **no graceful-skip
line required and `tier_adjustment` is NOT `NA`.**

1. **My first look-ahead threshold was wrong and was caught before any value was
   transcribed.** I filtered news on `datetime > 1785283199`, believing it to be the 07-29
   end-of-day-ET boundary; it is actually **2026-07-28T23:59:59 UTC**, so the filter reported
   **8 items "after as-of."** Recomputed: the correct boundary is **1785383999**
   (2026-07-30 03:59:59 UTC = 2026-07-29 23:59:59 ET), and `max(.datetime)` = **1785331681**
   → **0 items after the as-of date.** No contaminated headline entered this file. Recorded in
   `## DATA NOTE`.
2. **`fz quote`'s `Recom` and `Target Price` are `null`** (leaf degraded to 14/84 fields,
   `phase-0-intake.md`), so the D6 Finnhub-vs-`fz` cross-source divergence test could not be
   run. Substituted with seven dated, named-broker targets from the news feed — a strictly
   richer source than a blended scalar.
3. **Borrow fee / HTB status not obtainable.** WebSearch identified Fintel and ORTEX as
   trackers but returned **no current rate and no HTB flag**. Recorded as **`borrow: n/a`** —
   a blind spot. **Not inferred from the short float**, per the spec's pitfall.
4. **News-feed timezone is not determinable from the payload.** `jq strftime` renders UTC; the
   16:07 earnings headline against a documented postmarket release implies **ET**. §A states
   the ambiguity and shows the conclusion is unchanged under either reading.
5. **Short-interest staleness, tagged as the spec requires.** `Short Float` 17.94% is the
   **exchange semi-monthly settlement figure with a ~2-week lag** — it therefore may **not yet
   reflect 07-28/07-29 activity**, including any covering into the print. Tagged
   `[SENT:short_float fz semi-monthly]` throughout. The 17.55% → 17.94% *trend* spans two
   settlements and is the more robust reading.

Not an error, recorded as a correction to an upstream inference — see `## DATA NOTE`:
`/stock/recommendation` **works** where `phase-7b-fundamentals.md` found
`/stock/recommendation-trends` returned **404**. Two of 7b's four dead analyst routes are
recovered.

## DATA NOTE / CORRECTION

No value in this file was revised after its first validated read. **Three corrections to
upstream inferences, all sourced from this phase's data:**

**(1) `phase-7b-fundamentals.md`'s "analyst leg UNMEASURED" is now partly repaired.** That
phase declared the analyst leg unmeasured after four dead routes (Finnhub estimates/target
paid, `recommendation-trends` 404, Yahoo 401, `fz` `Recom` null). **Two routes are recovered
here:** `/stock/recommendation` returns the full ratings distribution and trend (§B), and the
news feed supplies **seven dated, named-broker price targets** (§A). Verified against
`curl .../stock/recommendation?symbol=ENPH` → `.[]` and
`curl .../company-news?...` → `.[].headline`. **Phases 8/8b/9 should use this and disregard
7b's UNMEASURED flag** — which was correct when written, before this endpoint was tried.
Reading: **negative on revision direction (6 cuts, 0 raises), bullish on absolute level (mean
PT $43.07 = +22.8% above spot, 0 strongSell).**

**(2) `phase-6-macro.md`'s and `phase-7b-fundamentals.md`'s "Q2 beat / guided above" framing is
corrected.** `phase-6-macro.md` §G recorded *"Revenue $291.9M... adjusted EPS $0.47 vs $0.46 →
slight BEAT"* and *"Q3 revenue guidance $290–320M ... ABOVE"*; `phase-7b-fundamentals.md` §C
flagged the basis as genuinely ambiguous and asked phase 8 not to treat it as settled.
**The news feed settles it:**
- Benzinga's *"Q2 Adj. EPS $0.47 Beats $0.46 Estimate"* (07-28 16:07) was **retracted** by
  **"CORRECTION: Enphase Energy Q2 Adj. EPS $0.46, *Inline*"** (07-28 17:34), corroborated by
  ChartMill's *"Posts **In-Line** Q2 Earnings."* **Finnhub's 0.46 vs 0.4678 was correct.**
- The Q3 guide is **"$290.000M–$320.000M vs $304.253M Est"** — midpoint **$305M against a
  $304.253M consensus**, i.e. **IN LINE**. Phase 6's "above" was measured against the *carried
  pre-print range* ($280–310M) from the 07-27 run, not against actual consensus.
- **Corrected statement: Q2 was a small revenue beat (+0.67%) with EPS IN LINE, and Q3 guidance
  is IN LINE with consensus.** Not a beat-and-raise.
- **Downstream consequence:** `phase-6-macro.md`'s argument that *"ENPH beat its Q2 and the
  market sold it anyway — more bearish than a miss"* **weakens** — the market sold an *in-line*
  print, which is ordinary. But `phase-7b-fundamentals.md`'s earnings axis **strengthens**: an
  in-line quarter confirms the beat cushion is exhausted after +36.28% → +19.67% → +12.17% → 0.
  Phase 8 agents must use **"in line"**, not "beat."

**(3) My own first look-ahead filter on the news feed was wrong.** Threshold 1785283199 is
2026-07-28T23:59:59 UTC, not the 07-29 ET end-of-day; it falsely reported 8 look-ahead items.
Correct boundary **1785383999**; `max(.datetime)` **1785331681** → **0 items after as-of**.
Re-verified against `[.[].datetime] | max`. **No value was transcribed from the erroneous
filter** — the JSON-validity/look-ahead gate caught it before any headline was used.

## Verdict for downstream

```
sentiment_signal:  BEARISH
crowd_state:       CROWDED_SHORT
short_interest:    17.94% of float [fz, semi-monthly, ~2wk lag; up from 17.55%] ; days_to_cover: 3.05 (fz) / 2.63 (WebSearch) ; borrow: n/a [WebSearch — NOT OBTAINABLE, blind spot]
tier_adjustment:   VETO
divergences:
  - "Analyst direction (6 PT cuts, 0 raises) vs analyst level (mean PT $43.07 = +22.8% above spot, all ratings maintained, 0 strongSell)"
  - "Retail bullish/short-dated (Aug-07 C37 $218,770 across 99 tickets, ~96% ask-side) vs institutional bearish/long-dated ($196,240 ATM put in 1 ticket; $2.84M Jan-2028 P30 at 92% ask; $405,922 long-dated calls written; DP sell_ratio 0.610)"
  - "Short base 17.94% and RISING from 17.55% — the crowd is already positioned the way this run's evidence points, and it ADDED into the print"
key_risks:
  - "Fresh short joins ~22.9M shares (17.94% of float) already short, into a base that grew through the event — crowded, with the squeeze thesis publicly circulated"
  - "Street targets average $43.07 / median $45 (+22.8% / +28.3% above spot) with every rating maintained and zero strongSell — shorting into consensus upside"
  - "Borrow fee / HTB UNMEASURED, so the true cost and fragility of a short cannot be priced; combined with iv_rank at the 15.6th self percentile and skew_ratio 0.994 (COMPLACENT), the market is not braced for downside"
```

**Axis-by-axis derivation** (flow bias = **BEARISH**, plurality of phases 1–7;
`phase-7-insights.md` `scenario` DIRECTIONAL_SHORT at `confidence_pct` 24):

| Axis | Reading | vs bearish flow bias |
|---|---|---|
| News tone / revision **direction** | 6 PT cuts, 0 raises; GLJ Sell $24.47; Q2 corrected to **in line** | **CONFIRMS** |
| Analyst revision **momentum** (counts) | hold 19 → 18 → **21**; buys frozen 4 months; bull share 40% → 39%; but `sell` 6 → **4**, `strongSell` **0** | **CONFIRMS** (mildly) |
| Retail vs institutional | Retail long calls / institutions long puts + selling stock; company buyback **$0** | **CONFIRMS** |
| **Short interest / squeeze** | **17.94% and RISING**; crowd already short; squeeze narrative public | **CONTRADICTS** |
| Positioning extremes | `zscore` +0.482 NORMAL; `iv_rank` 15.6th self pctile; `skew_ratio` 0.994 COMPLACENT | **NEUTRAL** — no trigger |
| Analyst **level** | mean PT **$43.07** (+22.8%), median $45, all ratings maintained, 0 strongSell | **CONTRADICTS** |

**Why VETO and not CAUTION — and the honest case against it.**

The rubric escalates to VETO when the crowd is **crowded the same way as the thesis** *and*
there is a **squeeze / short-interest mismatch**, giving as its named example *"a heavily-shorted
name on a fresh short thesis."* **That is exactly this case, and two independent contrary axes
fire rather than one:**

1. **The crowd is already there and adding.** 17.94% of float short — roughly **22.9M shares**
   — and the base **rose from 17.55%** through a binary event rather than covering. Shorts
   pressed after a 30% decline.
2. **Wall Street is not.** Seven targets averaging **$43.07** (+22.8%), median **$45**
   (+28.3%), **every rating maintained**, **zero strongSell**. Even BMO's low non-Sell target
   of $37 is above spot.
3. **The entry is the worst point of the range.** `period_low` **34.96 was set today** and the
   close is **$0.11 above it** (`phase-7-insights.md` §D); `RSI` **31.60**; price **−30.49%
   below SMA50** (`phase-5-historical.md` §G).
4. **The name will not fund a short cheaply or safely:** fortress balance sheet (current ratio
   **3.80**, **$930.6M** liquid, ~net-cash-neutral), **~7.2% annualized FCF yield**,
   `Forward P/E` **15.82** (`phase-7b-fundamentals.md`), and **borrow cost unmeasured**.

**The counter-case, stated fairly: a CAUTION reading is defensible.** The "hard" half of the
squeeze test is **not confirmed** — days-to-cover is only **3.05 / 2.63** (cheap to cover),
17.94% is a **sector condition** (5th of 18, tied with SEDG 17.97%, far below CSIQ 34.53% and
RUN 28.65%), and **HTB status is unmeasured rather than confirmed hard**. On a strict reading of
"hard squeeze," this is a crowded-but-not-fragile short → CAUTION. **I resolve to VETO** because
(a) two contrary axes fire, not one; (b) the short base *grew* into the event, which is the
substance of crowding regardless of cover speed; (c) 7c is a **downside-only** gate where the
cautious resolution is the correct default; and (d) it is coherent with
`phase-6-macro.md`'s regime guidance of *"Half position sizes. Favor defined-risk strategies."*
**Phase 8b should test this explicitly** — if the debate concludes the 3-day cover defeats the
squeeze argument, the gate is a CAUTION and phase 9 may carry a small defined-risk directional
position rather than none.

**What VETO means mechanically** (per the rubric): a **fresh directional short is watch-only /
0%**; **carry-only defined-risk structures remain permitted**. It does **not** flip the bias —
`sentiment_signal` is **BEARISH** and the direction of every confirming axis stands. It says the
**expression and the entry are wrong**, not the direction.

**Reminder of this gate's constraint:** 7c is **downside-only — it can only confirm or cut,
never add.** Nothing here licenses a long. The bullish-level evidence (PTs +22.8%, RSI 31.60,
FCF yield) is a **reason not to be short**, not a reason to be long — and phase 4's negative
gamma below spot plus `phase-6-macro.md`'s rising VIX remain unrebutted structural bearish
mechanics.

**Combined gate state entering phase 8:** `phase-7b-fundamentals.md` **CAUTION** (1
contradiction: insider MSPR) + `phase-7c-sentiment.md` **VETO** (crowded short, adverse analyst
level). Two downside gates fired. `phase-6-macro.md` sector rotation is **adverse**
(persistence 1.0). Phase 9's directional sizing should be at or near zero before the phase-8b
debate is even considered.

## Sources

- [Fintel — ENPH short interest, short squeeze, borrow rates](https://fintel.io/ss/us/enph)
- [Benzinga — ENPH short interest](https://www.benzinga.com/quote/ENPH/short-interest)
- [ORTEX — Enphase Energy short interest](https://app.ortex.com/s/Nasdaq/ENPH/short-interest)
- [GuruFocus — ENPH short interest](https://www.gurufocus.com/term/ShortInterest/ENPH)
- [Seeking Alpha — Enphase Energy: A Top Short Squeeze Idea For 2026](https://seekingalpha.com/article/4861545-enphase-energy-a-top-short-squeeze-idea-for-2026)
