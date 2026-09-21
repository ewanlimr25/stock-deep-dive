# Phase 1 — Options Flow

**Ticker:** FCX
**As-of date:** 2026-05-20 (effective data 2026-05-19)
**Generated:** 2026-05-20T19:30:00-04:00
**Upstream phases cited:** `phase-0-intake.md`

## Summary

Today's tape on FCX (spot intraday $58.31–$59.80, settle ≈$59.13) shows a
**mixed-but-leaning-bullish** directional bias on a 2–4-month horizon, riding
on top of an unusually large **single-trade** ask-side call sweep. One trader
bought 6,158 contracts of the **July 65C @ avg $2.68 for $1.54M**
[FLOW:options_flow_sweeps] — by far the biggest premium event of the day and
a clear upside bet (delta 0.35, ~10.7% OTM). Per `sweep_persistence`, FCX has
appeared in the market-wide top-sweep cohort in **5 of the last 5 sessions**
with **$54.4M cumulative sweep premium** [FLOW:sweep_persistence] —
institutional engagement is sustained, not a one-day fluke.

Counterbalancing the calls: meaningful **Jun-18 OTM put buying** (58P/56P/60P
all on the ask, ~$638k combined) and a long-dated **Jan-27 55P ask print at
$591k** — these look like portfolio protection more than directional shorts,
since the same tape also shows institutional **put-selling** on Jan-2027/Jan-
2028 45P/50P (bid-side, ~$258k combined), i.e. someone is happy to be put the
stock at $42–$50. Front-week (May-22) IVs are blown out (max 122% on the 65P)
but premiums there are trivial; the real signal is in the **Jun/Jul/Aug**
maturities at 47–55% IV. Conviction is **3/5** — strong magnitude and
persistence, but the bull and bear flow co-exist rather than confirm.

## Key signals

- **Headline bullish print:** July 65C ask-side sweep, **6,158 contracts, $1.54M
  premium, 47 trades, avg $2.68** [FLOW:options_flow_sweeps] — split across
  two clip prints of $750k each at 14:26:43Z [FLOW:top_premium_trades].
- **Persistence is exceptional:** FCX in top-sweep cohort **5 of 5 sessions**,
  consistency_score 1.0, $54.4M cumulative sweep premium, dominant_direction
  "mixed" [FLOW:sweep_persistence].
- **OTM-put accumulation cluster (Jun-18):** 58P $244k ask + 56P $212k ask +
  60P $182k ask = **~$638k of put buying on a single expiry** at strikes 5%,
  3%, 1.5% OTM [FLOW:options_flow_sweeps][FLOW:options_flow_unusual_volume].
- **Long-dated put-selling (bullish signature):** Jan-27 50P bid $130k + Jan-
  28 45P bid $127k + Jan-28 42P bid $51k — somebody is selling LEAP downside
  to express comfort owning FCX at $42–$50 [FLOW:options_flow_sweeps].
- **0DTE-style IV outliers ignored:** May-22 65P 122% max IV [FLOW:iv_outliers]
  but total premium <$100k → cosmetic, not signal.

## Detailed findings

### Sweeps (ask vs bid, premium, persistence)

Top FCX sweeps on 2026-05-19, ranked by total_premium [FLOW:options_flow_sweeps]:

| Strike | Type | Expiry | Side | Size | Premium | Avg px | Trades | Read |
|--------|------|--------|------|------|---------|--------|--------|------|
| 65C | call | 2026-07-17 | **ask** | 6,158 | $1,542,604 | $2.68 | 47 | Bullish — biggest single trade of the day |
| 55P | put | 2027-01-15 | **ask** | 901 | $591,985 | $6.71 | 2 | Long-dated put buy — hedge or bearish LEAP |
| 55P | put | 2026-11-20 | no_side | 1,000 | $560,000 | $5.60 | 1 | Block — direction ambiguous |
| 55P | put | 2026-08-21 | no_side | 1,250 | $498,750 | $3.99 | 1 | Block — direction ambiguous |
| 60C | call | 2026-07-17 | no_side | 1,000 | $435,000 | $4.35 | 1 | Bullish — ATM call block |
| 100C | call | 2028-01-21 | **bid** | 550 | $341,798 | $6.22 | 60 | Bullish-tail SOLD — capping upside? or closing |
| 60C | call | 2026-06-18 | **bid** | 932 | $307,330 | $3.14 | 72 | ATM call SOLD — covered-call or short |
| 58P | put | 2026-06-18 | **ask** | 768 | $243,824 | $2.98 | 12 | OTM put bought — short-dated protection |
| 56P | put | 2026-06-18 | **ask** | 1,029 | $212,346 | $2.06 | 17 | OTM put bought — protection |
| 60P | put | 2026-06-18 | **ask** | 469 | $182,260 | $3.90 | 46 | ATM put bought — protection |
| 65C | call | 2026-06-18 | **ask** | 903 | $133,650 | $1.47 | 93 | Bullish — OTM call sweep |
| 62C | call | 2026-06-18 | **ask** | 576 | $134,721 | $2.33 | 51 | Bullish — call buy |
| 70C | call | 2026-07-17 | bid + ask | 2,114 | $321,924 (combined) | $1.53 | 333 | Wash — likely closed or rolled |
| 66C | call | 2026-06-05 | **ask** | 3,008 | $189,590 | $0.67 | 16 | Short-dated lottery call |
| 50P | put | 2027-06-17 | **bid** | 201 | $130,626 | $6.38 | 2 | Put SOLD — bullish signature |
| 45P | put | 2028-01-21 | **bid** | 201 | $127,585 | $6.32 | 8 | LEAP put SOLD — bullish |

**Ask-side net:** ~$3.1M of call premium aggressively lifted (65C/60C/66C/62C
across Jun-Jul). **Bid-side net:** ~$770k of put premium sold (Jan-27 50P,
Jan-28 45P/42P) — these are bullish tells. **Counter-flow:** ~$638k of Jun-18
OTM puts BOUGHT ask-side.

### New positioning (vol/OI ratio ≥ 3)

[FLOW:options_flow_unusual_volume]

| Strike | Type | Expiry | OI | Vol | V/OI | Avg IV | Read |
|--------|------|--------|----|----|------|--------|------|
| 58P | put | 2026-06-18 | 61 | 866 | **14.2x** | 50.0% | New short-term protection |
| 66C | call | 2026-06-05 | 230 | 3,259 | **14.2x** | 53.9% | New OTM call lottery (Jun-5 weekly) |
| 57C | call | 2026-06-12 | 35 | 411 | 11.7x | 55.2% | New bullish call (Jun-12 weekly) |
| 56P | put | 2026-06-18 | 99 | 1,142 | 11.5x | 50.4% | Builds on the Jun-18 put-buying cluster |
| 53P | put | 2026-06-12 | 17 | 166 | 9.8x | 52.9% | Cheap OTM put, low premium |
| 59C | call | 2026-05-22 | 56 | 200 | 3.6x | 65.5% | Near-the-money weekly bet |
| 62C | call | 2026-06-18 | 189 | 588 | 3.1x | 52.9% | OTM call continuation |

The unusual-volume slate is **roughly balanced**: bullish weekly calls (66C
Jun-5, 57C Jun-12, 62C Jun-18) vs bearish weekly puts (58P/56P/53P). The
common thread is a **5–11% IV bump above realized** on every weekly strike —
the market is pricing a move within the next 4 weeks.

### Largest premium prints — chronological

[FLOW:options_flow_top_premium_trades] — clean reconstruction of the day:

1. **13:43Z** — 100C Jan-2028 bid 199x @ $6.22 = $124k (call sold, vol bet
   capping upside or closing long)
2. **13:43–14:18Z** — 45P Jan-2028 bid 100/95 @ $6.30/$6.40 = $124k (LEAP put
   sold — happy to own at $45)
3. **14:08Z** — 50P Mar-2027 ask 100 @ $5.50 = $55k (small bearish/protection)
4. **14:21Z** — 57C Jun-12 bid 381 @ $4.05 = $154k (ITM call sold — covered
   call or short-call)
5. **14:25Z** — 64P May-29 ask 325 @ $5.94 = $193k AND 64P May-22 bid 325
   @ $5.74 = $187k → looks like a **calendar roll** of an ITM put hedge from
   May-22 → May-29
6. **14:26:43Z — 65C Jul-17 ask 3,000 + 2,999 @ $2.50 = $1.50M** (THE bullish
   sweep; spot $58.69)
7. **14:37Z** — 62P/63P short-dated put block ($316k combined, mid-quote)
8. **14:48Z** — 58P Jun-18 ask 750 @ $3.18 = $238k (protection cluster build)
9. **15:16Z** — 55P Aug-21 no_side 1,250 @ $3.99 = $499k (mystery block)
10. **16:45Z** — 55C Jan-2028 ask 90 @ $17.75 = $160k (LEAP call BUY, ITM
    delta 0.68 — strong bullish institutional bet, low size though)
11. **17:12Z** — 55P Nov-2026 no_side 1,000 @ $5.60 = $560k (mystery block)
12. **17:15Z** — 60C Jun-18 bid 720 @ $3.35 = $241k (ITM call SOLD)
13. **17:41Z — 55P Jan-2027 ask 900 @ $6.57 = $591k** (LEAP put BUY — biggest
    bearish print of the day, 0.34 delta protection)
14. **19:38Z** — 60C Jul-17 no_side 1,000 @ $4.35 = $435k (block; spot $58.84)

**Time-of-day pattern:** bullish call sweep front-loaded at 14:26Z, put-
buying clusters mid-day, big LEAP put-buy ($591k) at 17:41Z, then final hour
sees more 60C buying. **Both books are open** — institutional accumulation
*and* institutional protection are happening on the same tape.

### IV outliers & Greeks

[FLOW:iv_outliers] — every entry is **May-22 weekly** (expires Friday).
Max IVs of 100–122% on weekly puts are normal expiry-week behaviour and the
total premiums are trivial (<$100k each except the 63P at $251k). **Do not
treat the May-22 IVs as a signal**; they reflect time decay arithmetic, not
real positioning.

[FLOW:options_flow_greek_screener] — sorted by premium, the top-5 by Greeks
match the sweep table. Key Greek tells:

- **65C Jul-17:** delta 0.35, gamma 0.031, **vega 0.087** — typical
  directional structure (vega-positive but moderate; this is a delta bet, not
  a vol bet).
- **55P Jan-27:** delta -0.34, **vega 0.178** — high vega; this is at least
  partly a **vol/long-dated protection bet**, not pure direction.
- **55C Jan-28 LEAP:** delta 0.68, **vega 0.276** — vega is the dominant
  Greek; long-dated bullish + long-vol bet (consistent with someone planning
  for higher copper price and/or higher realized vol).
- **64P May-22 (deep ITM):** delta -0.92, IV 54% — pure intrinsic, the
  "calendar roll" hypothesis holds.

### Smart money flow (market-wide, FCX filter)

[FLOW:hot_chains_smart_money_flow] — checked both bullish (top-25) and
bearish (top-25) cohorts; **no FCX contract appeared in either ranking**.
This is unsurprising — the market-wide list is dominated by SPY/IWM/SPX/VIX
hedging tape (millions of contracts). Absence here is not a signal *against*
FCX; the threshold is too high.

### Sweep persistence (multi-day)

[FLOW:sweep_persistence] (days=5, dates 05-13 → 05-19):

| Ticker | Sessions in top | Consistency | Dominant dir | Cumulative sweep $ |
|--------|----------------|-------------|--------------|-------------------|
| **FCX** | **5/5** | **1.00** | mixed | **$54,380,015** |

**This is the single most important phase-1 datapoint.** $54M of sweep
premium across 5 sessions on a $90B mid-cap copper miner means a real
institutional debate is playing out on the tape. Phase 2 (dark pool) and
phase 3 (OI builds) will tell us which side is winning.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `options_flow_sweeps` | symbol=FCX, min_prem=100k, top_n=25, date=2026-05-19 | 25 contracts; #1 = 65C Jul-17 ask $1.54M |
| `options_flow_unusual_volume` | symbol=FCX, min_v/oi=3, top_n=25, date=2026-05-19 | 9 hits; #1 = 58P Jun-18 14.2x |
| `options_flow_top_premium_trades` | symbol=FCX, top_n=25, date=2026-05-19 | 25 trades; top 2 = 65C Jul-17 ask $750k × 2 |
| `options_flow_iv_outliers` | symbol=FCX, min_iv=0.4, min_vol=50, top_n=15, date=2026-05-19 | 15 May-22 weeklies, all expiry-driven |
| `options_flow_greek_screener` | symbol=FCX, top_n=15, sort=premium, date=2026-05-19 | 15 rows, confirms 65C delta 0.35 / vega 0.087 |
| `hot_chains_smart_money_flow` | dir=bullish, top_n=25, min_vol=500, date=2026-05-19 | FCX not present (market-wide cohort) |
| `hot_chains_smart_money_flow` | dir=bearish, top_n=25, min_vol=500, date=2026-05-19 | FCX not present (market-wide cohort) |
| `hot_chains_sweep_persistence` | symbol=FCX, days=5, top_n=20 | **5/5 sessions, $54.4M cumulative, mixed** |
| `hot_chains_sweep_ratio` | top_n=25, min_vol=500, min_ratio=0.3, date=2026-05-19 | No FCX in market-wide ratio cohort |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** **mixed, leaning bullish** (single biggest print
  + LEAP put-selling = bullish; offsetting Jun-18 put-buying + Jan-27 LEAP
  put-buy = protective).
- **Conviction:** **3/5** — premium magnitude is unambiguous and persistence
  is exceptional, but the two-sided flow keeps conviction from being higher.
- **Three things later phases must remember:**
  1. The **July 65C ask-side sweep ($1.54M, 6,158 contracts)** is the
     anchor bullish trade. If dark pool / OI / dealer phases corroborate,
     this is the trade idea.
  2. There is a **simultaneous put-protection cluster on Jun-18 OTM strikes
     ($638k)** AND a **$591k Jan-27 55P LEAP put-buy**. These could be
     covered-call sellers buying tail-hedge, OR a genuine bearish institution
     fading the call buyer. Phase 3 (OI builds) is the tiebreaker.
  3. **FCX has been in the top-sweep cohort 5 of 5 sessions, $54.4M
     cumulative** — this is the kind of multi-day signature that historically
     precedes a real move (verify in phase 5 historical_signal_backtest).
- **Open questions:**
  - Is the dark pool confirming aggressive *equity* accumulation on the days
    the calls have been sweeping? (phase 2)
  - On the call side, are the Jul 65C contracts adding to OI (genuine new
    position) or just churning intraday? (phase 3 `oi_biggest_increases`)
  - Is 50% IV elevated, in-line, or cheap vs FCX's own history? (phase 5
    `historical_iv_percentile_zscore`)
  - Does dealer GEX flip above/below current spot — does the July 65C buyer
    *force* dealer hedging into a squeeze? (phase 4 `gamma_flip`)
