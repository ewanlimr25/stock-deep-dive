# Phase 2 — Dark Pool & Block Prints

**Ticker:** FSLR
**As-of date:** 2026-07-31
**Generated:** 2026-07-31
**Upstream phases cited:** `phase-0-intake.md`, `phase-0.5-context.md`, `phase-1-flow.md`

## Summary

**Genuine regular-session accumulation, mechanically distorted at both ends of
the report.** FSLR printed **416,193 shares / $88.27M across 250 dark-pool
trades** — 13.8% of the day's 3,014,081-share volume and **0.410% of the
101.48M float**. Decomposed by session the picture is unambiguous: the
**regular session (09:30–15:55) is 73.1% buy on $59.16M**, while the closing
auction is **6.8% buy** and post-market **0% buy**.

Two artifacts had to be stripped before that read was trustworthy, and both
cut against the tools' raw output:

1. **`block-stratified` reports a mega tier of 2 trades / 144,400 shares /
   $30.75M with `buy_ratio = 1.0`. One of those two prints is
   `canceled = True`.** The real mega tier is **one** print, 72,200 shares,
   $15.38M. `uw dark-pool largest` lists the cancelled print too. The tools do
   not filter cancellations.
2. **That surviving 72,200-share print is not accumulation — it is an options
   delta hedge.** It is flagged `qualified_contingent_trade`, it landed **49.0
   seconds** after the 1,900-lot Aug-21 $230 call cross from
   `phase-1-flow.md`, and 72,200 ÷ (1,900 × 100) = **delta 0.3800** against the
   option's reported delta of **0.3760** — a **101.1%** hedge match.

That second finding is the most valuable result in this phase, because it runs
in the *opposite* direction to its effect on size. It removes 72,200 shares
from the accumulation column (regular-session buy falls to **63.2%**), but it
**independently confirms phase-1's contested read**: the dealer bought stock
*above the ask* to hedge, which means the dealer is **short** the calls — so
the customer **bought** them. Phase 1's single largest open question is closed
by a different dataset.

## Key signals

- **Regular session 73.1% buy on 278,276 shares / $59.16M** — and **63.2%**
  after removing the hedge print; the highest of the last five sessions
  `[DP:session_split DUCKDB]`
- **Five-day regime flip**: regular-session buy% ran 44.5 → 36.8 → **28.4**
  (07-29) → 64.2 → **73.1**. Institutions distributed *into* the pre-earnings
  run-up and have bought since the print `[DP:session_split DUCKDB]`
- **The 72,200-share mega print is a QCT delta hedge for the Aug-21 $230 call
  block** — 49.0s lag, 101.1% size match, the day's only non-cancelled QCT.
  Confirms the customer was the call **buyer** `[DP:ts_confirm DUCKDB]`
- **`block-stratified` mega tier double-counts a cancelled trade** (2 prints /
  144,400 sh / $30.75M reported vs 1 / 72,200 / $15.38M real)
  `[DP:block_stratified]`
- **Largest genuine directional block: 28,000 shares at $214.00 ($5.99M,
  14:13 ET)** — above spot, no hedge partner `[DP:largest]`
- **Largest print = 0.0711% of float; whole dark-pool day = 0.410% of float**
  — modest for a 101.48M-float name `[DP:block_pct_float fz]`
- **Off-hours "93–100% sell" is a classification artifact**, not distribution
  — closing crosses print at 211.03 against a stale wide NBBO of [210, 213]
  (mid 211.50), so every one mechanically classifies as a sell
  `[DP:extended_hours]`

## Detailed findings

### Largest blocks

Times converted to **ET**. `Float %` uses `Shs Float = 101.48M` from
`phase-0-intake.md`.

| # | Time (ET) | Price | Size | Premium | NBBO | vs mid | Float % | Read |
|--:|-----------|------:|-----:|--------:|------|--------|--------:|------|
| 1 | 12:12:35 | 212.9695 | **72,200** | $15,376,398 | 212.18 / 212.54 | **+0.61 above ask** | 0.0711% | **QCT — delta hedge, not a view** |
| — | ~~12:13:12~~ | ~~212.9695~~ | ~~72,200~~ | ~~$15,376,398~~ | 212.08 / 212.54 | — | — | **`canceled = True` — excluded** |
| 2 | 16:00:07 | 211.03 | 35,724 | $7,538,836 | 210.00 / 213.00 | −0.47 | 0.0352% | Closing cross (artifact) |
| 3 | 14:13:24 | 214.00 | **28,000** | $5,992,000 | 213.46 / 214.04 | +0.25 | 0.0276% | **Genuine buy above spot** |
| 4 | 17:13:28 | 211.03 | 23,138 | $4,882,812 | 210.20 / 212.99 | −0.57 | 0.0228% | Post-market cross |
| 5 | 17:13:28 | 211.03 | 13,500 | $2,848,905 | 210.20 / 212.99 | −0.57 | 0.0133% | Post-market cross |
| 6 | 16:00:26 | 211.03 | 13,100 | $2,764,493 | 210.00 / 213.00 | −0.47 | 0.0129% | Closing cross |
| 7 | 15:29:19 | 212.00 | 11,602 | $2,459,624 | 211.88 / 212.03 | +0.045 | 0.0114% | Genuine, near-mid |
| 8 | 16:00:36 | 211.03 | 5,610 | $1,183,878 | 210.00 / 213.00 | −0.47 | 0.0055% | Closing cross |
| 9 | 09:34:03 | 214.39 | 5,000 | $1,071,950 | 213.41 / 214.39 | **at ask** | 0.0049% | Genuine buy, opening |
| 10 | 16:07:24 | 211.03 | 4,743 | $1,000,915 | 211.08 / 215.00 | below bid | 0.0047% | Post-close cross |

Genuine intraday directional blocks (rows 3, 7, 9 plus the sub-$1M tail) are
**buys at or above the offer**: 28,000 @ 214.00, 11,602 @ 212.00, 5,000 @
214.39, 2,500 @ 215.59, 2,078 @ 213.44, 1,905 @ 214.225, 1,880 @ 214.55. The
only meaningful intraday **sells** are 2,775 @ 210.83 (09:32), 2,100 @ 208.629
(09:47) and 2,000 @ 207.3775 (10:04) — **early-session supply that was
absorbed**, since the stock traded to 215.59 afterwards.

### Tier breakdown

`uw dark-pool block-stratified --min-tier large` returns one row for FSLR with
tiers nested (there is **no `sell_ratio`** field — derived as `1 − buy_ratio`):

| Tier | Trades | Buy vol | Sell vol | `buy_ratio` | Derived sell | Premium |
|------|-------:|--------:|---------:|------------:|-------------:|--------:|
| mega | 2 ⚠ | 144,400 | 0 | **1.000** | 0.000 | $30,752,796 ⚠ |
| block | 9 | 44,602 | 95,815 | **0.318** | 0.682 | $29,743,413 |
| large | 240 | 98,009 | 105,567 | **0.481** | 0.519 | $43,151,790 |
| retail | 0 | 0 | 0 | 0.500 | — | $0 |
| **all tiers** | | | | | | **$103,647,999** |

⚠ **The mega row is wrong.** Corrected to one print: 72,200 shares, $15.38M.
`total_premium_all_tiers` overstates by exactly $15,376,398 — the true
non-cancelled total is **$88,271,601**, which matches the raw-parquet total of
$88.27M across 250 prints.

Taken at face value the tiers read *bearish* — block tier 68.2% sell, large
tier balanced. **That reading is entirely a session artifact.** Cross-cut by
session:

| Tier | Session | Prints | Shares | Premium | Class |
|------|---------|-------:|-------:|--------:|-------|
| mega | regular | 1 | 72,200 | $15.38M | buy *(hedge)* |
| block | regular | 2 | 39,602 | $8.45M | **buy** |
| block | close auction | 2 | 48,824 | $10.30M | sell |
| block | post-market | 2 | 36,638 | $7.73M | sell |

Every block-tier "sell" happened **at or after the closing cross**. In the
regular session the block tier is **100% buy**. `block_ratio = 0.318` is
measuring the closing auction, not institutional intent.

### Session decomposition — the honest read

| Session (ET) | Prints | Shares | Premium | Buy % of classified | Mid shares |
|--------------|-------:|-------:|--------:|--------------------:|-----------:|
| Pre-market (<09:30) | 3 | 2,485 | $0.53M | 100.0 | 0 |
| **Regular (09:30–15:55)** | **206** | **278,276** | **$59.16M** | **73.1** | 9,522 |
| Close auction (15:55–16:05) | 37 | 93,564 | $19.75M | **6.8** | 0 |
| Post-market (>16:05) | 4 | 41,868 | $8.84M | **0.0** | 0 |

Regular-session detail: **buy 100 prints / 196,445 sh / $41.82M** vs **sell 95
prints / 72,309 sh / $15.32M** vs mid 11 / 9,522 / $2.02M.

**Excluding the 72,200-share hedge**: buy 99 prints / **124,245 sh / $26.44M**
vs sell 95 / 72,309 / $15.32M → **63.2% buy**, net **+51,936 shares
(+$11.12M, +0.0512% of float)** genuinely accumulated in the regular session.

**Why the off-hours numbers must be discarded.** The closing-cross prints
execute at the official close of **211.03** while the recorded NBBO is a stale,
wide **[210.00, 213.00]** — mid **211.50**. Since 211.03 < 211.50, the
NBBO-midpoint classifier marks every single one a *sell*. The same mechanism
produces the 17:13 ET prints (NBBO [210.20, 212.99], mid 211.595). This is the
documented closing-auction artifact, and here it fires in the direction of a
**false bearish** signal. Per the standing pitfall that ratios below 0.55 are
only suggestive, and given the mechanical cause, **the 6.8% / 0.0% figures
carry no directional information.**

### Five-day regime — the strongest signal in this phase

| Date | DP shares | DP premium | Regular-session shares | **Regular buy %** | Off-hours buy % |
|------|----------:|-----------:|-----------------------:|------------------:|----------------:|
| 2026-07-27 | 342,434 | $70.17M | 89,693 | 44.5 | 81.3 |
| 2026-07-28 | 367,467 | $74.01M | 137,771 | 36.8 | 86.3 |
| 2026-07-29 | 179,986 | $36.08M | 99,491 | **28.4** | 98.9 |
| 2026-07-30 | 315,789 | $64.94M | 104,547 | 64.2 | 38.2 |
| **2026-07-31** | **416,193** | **$88.27M** | **278,276** | **73.1** | 6.4 |

Read the **regular-session** column only (the off-hours column inverts because
of the classifier artifact above, and its perfect anti-correlation is itself
evidence the two columns are measuring different things).

**Institutions sold into the pre-earnings run-up (44.5 → 36.8 → 28.4) and have
bought since the print (64.2 → 73.1).** Today is simultaneously the **largest
dark-pool day of the week** ($88.27M, 2.7× the prior day's regular-session
share count) and the **most buy-skewed**. That is a genuine, clean regime
change — and unlike phase 1's evidence, it does **not** hinge on a single
print.

### Price levels (5-day: 2026-07-27 → 07-31)

| Price | Premium | Prints | Interpretation |
|------:|--------:|-------:|----------------|
| 205.83 | $51,439,181 | 21 | = 07-27 close — **auction cross** |
| 202.59 | $45,940,524 | 17 | = 07-28 close — **auction cross** |
| 206.01 | $39,156,733 | 27 | = 07-30 close — **auction cross** |
| **212.97** | $30,854,595 | 3 | Today's hedge print ⚠ *(includes the cancelled duplicate)* |
| 211.03 | $26,294,971 | 29 | = 07-31 close — **auction cross** |
| 199.24 | $15,343,472 | 14 | = 07-29 close — **auction cross** |
| **214.00** | $6,395,390 | 4 | **Genuine intraday institutional level** |
| 201.49 | $5,688,839 | 3 | Intraday |
| 198.50 | $3,453,900 | 1 | Single print |
| 204.61 | $3,211,728 | 3 | Intraday |
| **212.00** | $2,598,484 | 2 | **Genuine intraday level** |
| 205.00 | $2,451,800 | 4 | Round-number intraday |
| 200.00 | $2,402,000 | 8 | Round-number intraday |

**Six of the top seven clusters are daily closing prices.** Cross-checked
against `phase-0.5-context.md`'s session table: 205.83 = 07-27 close, 202.59 =
07-28, 199.24 = 07-29, 206.01 = 07-30, 211.03 = 07-31 — exact matches. As
"institutional support/resistance" these are **weak evidence of intent**,
though they do mark where real shares changed hands.

The **212.97 row is inflated** — $30.85M over "3 prints" is 144,875 shares,
i.e. the 72,200 hedge counted twice plus a 475-share tail. The genuine figure
is $15.38M.

**Clusters within 1% of the 211.03 spot** (209.9–213.1): 211.03 ($26.29M,
auction), 212.00 ($2.60M, genuine), 212.97 ($15.38M corrected, hedge). The
genuine, non-mechanical institutional levels are **212.00 and 214.00 above**,
and **205.00 / 204.61 / 201.49 below**.

### Extended-hours activity

15 prints returned; **14 of them print at exactly 211.03**, the closing price.
The largest: 35,724 sh ($7.54M) at 16:00:07, 23,138 sh ($4.88M) and 13,500 sh
($2.85M) both at 17:13:28, 13,100 sh ($2.76M) at 16:00:26. Only one print
deviates: 1,727 sh at 213.00 (16:03:58).

The 16:00:0x–16:00:4x cluster is the **closing auction**; the 17:13:28 pair
(36,638 sh, $7.73M) is genuine post-market. Per the standing pitfall, prints
of this shape are **index rebalancing / ETF creation-redemption**, not
directional intent — note that **2026-07-31 is a month-end**, when index
tracking funds rebalance mechanically. FSLR is an **S&P 500 member**
(`phase-0-intake.md`). **Conviction from all off-hours activity is de-rated to
zero**, and no overnight-news attribution is claimed; phase 6 should confirm
there was no post-close headline.

### Cross-dataset confirmation (escape hatch §B)

Joining every option print ≥$700K to every dark-pool print ≥10,000 shares
within a ±120-second window returns **exactly one match**:

| Option leg | DP leg | Lag | Match |
|------------|--------|----:|------:|
| 12:11:46.663 ET · Aug-21 $230 C · 1,900 lots · δ 0.3760 · 71,437 δ-shares | 12:12:35.673 ET · 72,200 sh @ 212.9695 · `qualified_contingent_trade` | **49.0 s** | **101.1%** |

Implied hedge delta = 72,200 ÷ 190,000 = **0.3800** vs the option's 0.3760.
A QCT is *by definition* a stock trade contingent on a derivative leg, and this
is the **only non-cancelled QCT FSLR printed all day**.

**Inference chain:** the stock leg printed at **212.9695 against an ask of
212.54** — the hedger paid up, aggressively. A dealer buys stock to hedge a
**short** call. Therefore the dealer is short 1,900 Aug-21 $230 calls, and the
**customer is long** them. `phase-1-flow.md` flagged this print's initiator as
unprovable and warned that reversing it would swing net customer delta from
**+$10.73M to roughly −$4.5M**. **It is now established from an independent
dataset.** Phase 1's mildly-bullish bias stands, and phase 8b's bear case can
no longer attack the tape on this ground.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` / SQL path | Rows used |
|------------------|--------------------------------|-----------|
| `uw dark-pool largest --symbol FSLR --top-n 25 --sort-by premium --date 2026-07-31 --json` | top premium=15376397.9, size=72200, price=212.9695, nbbo_ask=212.54, trade_vs_mid=0.6095 ← `.results[0]`; **rows 1 & 2 are the same print, one cancelled** | 25 |
| `uw dark-pool block-stratified --symbol FSLR --top-n 30 --min-tier large --date 2026-07-31 --json` | mega.buy_ratio=1, mega.trade_count=2 ⚠, block.buy_ratio=0.318, large.buy_ratio=0.481, total_premium_all_tiers=103647999.45 ← `.results[0].{mega,block,large}` (**no `sell_ratio` — derived 1−buy_ratio**) | 1 |
| `uw dark-pool extended-hours --symbol FSLR --top-n 15 --date 2026-07-31 --json` | 14/15 at price=211.03; largest size=35724, premium=7538835.72, nbbo=[210,213] ← `.results[]` | 15 |
| `uw dark-pool price-levels --symbol FSLR --top-n 15 --days 5 --json` | 205.83 → total_premium=51439181.13, trade_count=21 ← `.results[0]`; `dates_covered`=[07-31,07-30,07-29,07-28,07-27] ← `.dates_covered` | 15 |
| `uw dark-pool ticker-summary --top-n 30 --date 2026-07-31 --json` | FSLR = null ← `[.results[].ticker]\|index("FSLR")`; SPY premium=1.697e10 ← `.results[0]` | 30 (market-wide) |
| DuckDB session split on `Dark pool/dp-eod-report-2026-07-31.parquet` | regular 278,276 sh / $59.16M / 73.1% buy; close-auction 93,564 / 6.8%; postmkt 41,868 / 0.0% | 250 |
| DuckDB tier × session | block: regular 39,602 buy vs close 48,824 + post 36,638 sell | 250 |
| DuckDB cancelled-flag audit | `canceled=True` → 1 print / 72,200 sh / $15.38M; `False` → 250 / 416,193 / $88.27M | 251 |
| DuckDB §B option↔DP 120 s join | lag_s=49.0, hedge_match_pct=101.1, trade_code=`qualified_contingent_trade` | 1 match |
| DuckDB 5-day regular-session buy% | 44.5 / 36.8 / 28.4 / 64.2 / **73.1** | 5 files |
| DuckDB regular session ex-hedge | buy 124,245 sh / $26.44M vs sell 72,309 / $15.32M → 63.2% | 205 |

## Tool errors

No command errored — all five exited 0 and every payload parsed.

**Three data-quality defects were found in otherwise-successful output**, all
material enough that downstream phases must not quote these tools raw:

1. **`block-stratified` and `largest` include cancelled trades.** The mega
   tier reports 2 trades / 144,400 sh / $30,752,796 with `buy_ratio = 1.0`;
   the second print (12:13:12.242 ET) has `canceled = True` in the source
   parquet. Corrected: 1 print / 72,200 sh / $15,376,398.
   `total_premium_all_tiers` is overstated by $15,376,398 (17.4%).
2. **`price-levels` inherits the same cancellation** — the 212.97 level shows
   $30,854,595 across "3 prints"; the true figure is ~$15.48M.
3. **`price-levels` is dominated by closing-auction crosses**, not
   institutional intent: six of its top seven levels are the five sessions'
   exact closing prices. Usable as volume-at-price, **not** as a
   support/resistance intent signal without this filter.

Note also that `price-levels` does not accept `--date` for its window anchor —
it anchors `--days 5` to the latest available date. Verified safe here:
returned `dates_covered` ends at 2026-07-31 = the as-of date
(`phase-0-intake.md`). **This would silently return the wrong window on a
historical as-of run** — the same defect recorded for `sweep-persistence` in
`phase-1-flow.md`.

## DATA NOTE / CORRECTION

Nothing was mis-transcribed, but three first-pass readings were overturned
before writing, each by the raw parquet:

1. **"Mega tier is 100% buy on $30.8M"** → half of it is a cancelled
   duplicate. Real: $15.38M.
2. **"Block tier is 68.2% sell — distribution"** → every block-tier sell is a
   closing-auction or post-market cross. In the regular session the block tier
   is **100% buy**.
3. **"72,200-share mega buy = institutional accumulation"** → it is a QCT
   **delta hedge** for the phase-1 option block. Removed from the accumulation
   count (73.1% → 63.2% regular-session buy), while *confirming* phase-1's
   directional read.

The memory-flagged closing-auction artifact fired here in the **opposite
direction** to the documented case: there, stripping post-close crosses turned
an apparent 0.803 buy-ratio bearish; here, stripping them turns an apparent
0.318 buy-ratio **bullish**. The lesson generalises as "always decompose by
session," not "crosses are always bullish."

## Verdict for downstream phases

- **Bias from this phase:** **ACCUMULATION** — in the regular session only.
- **Conviction: 3 / 5.** Higher than phase 1's 2/5 because this signal does
  **not** rest on a single ambiguous print: it is 99 buy prints across
  124,245 shares, plus a five-session trend (28.4% → 73.1%) that reverses
  exactly at the earnings date. Held below 4 because (a) the *headline* size
  is inflated by a hedge that carries no view, (b) net genuine accumulation is
  only **+51,936 shares = 0.0512% of float**, small in absolute terms, and (c)
  a single day's regime flip on a post-earnings session can be
  position-squaring rather than fresh conviction.
- **Largest block as % of float:** **0.0711%** (72,200 sh ÷ 101.48M) — and it
  is a hedge, not a position. The largest *genuine directional* block is
  28,000 sh @ $214.00 = **0.0276% of float**. The entire dark-pool day is
  **0.410% of float**. **For a 101.48M-float S&P 500 name these are ordinary
  sizes** — meaningful in aggregate and direction, not in individual heft. No
  single print here is large enough to move the name on its own.
- **Three S/R levels for phase-9:**
  1. **$214.00 — near resistance / first upside reference.** 28,000 sh
     ($5.99M) at 14:13 ET plus 5,000 @ 214.39, 1,905 @ 214.225, 1,880 @
     214.55 — $6.40M across 4 prints at the level, all bought at/above the
     offer. Today's high-water institutional zone; also the intraday high
     region the stock faded from.
  2. **$212.00–212.97 — immediate overhead supply / pivot.** 11,602 sh at
     212.00 and the 72,200-share hedge at 212.9695. Spot closed *below* this
     at 211.03. First test on any continuation.
  3. **$205.83–206.01 — primary support shelf.** The heaviest multi-day
     volume zone ($90.6M across 48 prints, though auction-driven), coincident
     with the 07-27 and 07-30 closes. Secondary support **$202.59**
     ($45.94M), then **$199.24** ($15.34M). A close below 205.83 would break
     the post-earnings structure.
- **Open questions:**
  - **Does the regular-session buying persist on 08-03?** One post-earnings
    session is a data point; two is a trend. This is the cheapest, highest-value
    follow-up in the whole run.
  - **Who supplied the 28,000 shares at $214.00** — and is the seller the same
    desk that trimmed LEAP delta in `phase-1-flow.md`? Both are consistent
    with one holder taking profit into strength while another initiates.
  - **Is the 17:13 ET post-market block (36,638 sh, $7.73M) month-end index
    rebalancing?** FSLR is an S&P 500 member and 07-31 is a month-end.
    Phase 6 should confirm; if it is mechanical, it further supports
    discarding the off-hours read.
  - **Does the 72,200-share dealer hedge create a gamma floor?** The dealer is
    short 1,900 Aug-21 $230 calls and long 72,200 shares. If FSLR rallies
    toward 230 the dealer must buy more stock; if it falls, sell. → **phase 4
    must price this**, since it is now a *known* dealer position rather than an
    inferred one.
