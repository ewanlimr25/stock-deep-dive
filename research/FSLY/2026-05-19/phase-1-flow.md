# Phase 1 — Options Flow

**Ticker:** FSLY
**As-of date:** 2026-05-19  (Effective data date: 2026-05-18)
**Underlying ref print:** $16.48 – $16.69 intraday on 2026-05-18
**Generated:** 2026-05-19T00:10:00Z
**Upstream phases cited:** phase-0-intake.md

## Summary

Today's tape on FSLY is dominated by **call premium** with one anomalously
large bid-side block at the Jan'27 $20 strike. Excluding that single $205K
print (which looks like a write, not a buy), the rest of the chain shows a
clear **ask-side accumulation of Sep'26 $17.5 calls** ($255,633 aggregated
sweep premium, 774 contracts, avg $3.31) plus a smaller but real
**bid-side put-selling stream** at $15/$17.5 strikes — both reads are
bullish. Critically, FSLY has appeared in UW's top-sweep universe **all 5
of the last 5 sessions (consistency_score = 1.0, $642,945 in 5-day sweep
premium)** [FLOW:hot_chains_sweep_persistence] — this is a campaign, not a
one-day blip.

## Key signals

- **Sep'26 $17.5 call ask-sweep campaign:** $255,633 aggregated, 774
  contracts, avg fill $3.31, 23 trades [FLOW:options_flow_sweeps] — the
  cleanest bullish print on the tape, slightly OTM (~6% above spot $16.5).
- **5-of-5-session sweep persistence:** FSLY made UW's top-sweep list every
  trading day from 2026-05-12 to 2026-05-18, total $642,945 5-day sweep
  premium, consistency_score 1.0 [FLOW:hot_chains_sweep_persistence].
- **Largest single trade is BID-side** Jan'27 $20C, $205K premium, 500
  contracts at $4.10, delta 0.57, IV 96.5%, executed 13:33:09Z
  [FLOW:options_flow_top_premium_trades] — this is a **call write** (or
  covered-call / collar leg), NOT bullish buying. Tagging as institutional
  premium-selling at the $20 strike — a soft resistance flag for upside.
- **Put-selling on the bid at $15 / $17.5:** $25,318 Jul'26 $15P bid-side,
  $18,692 Jun'26 $15P bid-side, $16,315 Jul'26 $17.5P bid-side
  [FLOW:options_flow_sweeps] — income/bullish "ok to own here" behaviour.
- **Vol/OI explosion in near-dated calls:** 5/22 $16.5C vol/OI = 38.25x;
  7/17 $17.5C vol/OI = 37.75x; 9/18 $17.5C vol/OI = 3.42x on 783 vol
  [FLOW:options_flow_unusual_volume] — fresh upside positioning across the
  curve (weekly, monthly, quarterly).
- **Single 5/22 $21.5P @ IV 170% bought mid for $9,595** (delta −0.92, size
  19) [FLOW:options_flow_greek_screener] — deep ITM put, looks like a
  **synthetic short stock** leg or far-OTM tail hedge. Notable but small.
- **Sub-threshold for market-wide smart-money lists:** FSLY does not appear
  in `hot_chains_smart_money_flow` top-25 in either direction because the
  list is saturated by VIX/SPX/large-caps. Not a "no flow" finding — the
  per-symbol calls above are the source of truth.

## Detailed findings

### Sweeps — ask vs bid breakdown

Aggregated sweep premium (`options_flow_sweeps`, date=2026-05-18,
min_premium=10,000):

| Contract | Side | Premium | Size | Trades | Avg fill | Read |
|---|---|---|---|---|---|---|
| FSLY 2026-09-18 C 17.5 | **ASK** | $255,633 | 774 | 23 | $3.31 | Bullish accumulation |
| FSLY 2027-01-15 C 20 | bid | $211,407 | 516 | 8 | $4.02 | Call write / covered-call |
| FSLY 2027-01-15 C 12.5 | bid | $66,000 | 100 | 3 | $6.60 | Deep-ITM call sale (likely rolled) |
| FSLY 2028-01-21 C 45 | bid | $54,330 | 147 | 8 | $3.68 | OTM LEAP write |
| FSLY 2028-01-21 C 45 | **ASK** | $49,930 | 135 | 4 | $3.65 | OTM LEAP buy (opposite of above) |
| FSLY 2026-07-17 P 15 | bid | $25,318 | 188 | 34 | $1.34 | Put write (bullish income) |
| FSLY 2026-06-12 P 15 | bid | $18,692 | 267 | 5 | $0.70 | Put write |
| FSLY 2026-06-18 P 17.5 | **ASK** | $17,732 | 85 | 12 | $2.18 | ATM put buy (hedge / bearish) |
| FSLY 2026-07-17 P 17.5 | bid | $16,315 | 61 | 6 | $2.67 | Put write |
| FSLY 2026-07-17 P 17.5 | **ASK** | $13,443 | 50 | 12 | $2.66 | ATM put buy |
| FSLY 2026-09-18 C 20 | **ASK** | $12,672 | 52 | 3 | $2.49 | OTM call buy |
| FSLY 2026-07-17 C 17.5 | bid | $11,454 | 62 | 18 | $1.85 | Call write |
| FSLY 2027-01-15 C 20 | **ASK** | $10,919 | 27 | 5 | $4.12 | LEAP call buy |
| FSLY 2026-05-22 C 15 | bid | $10,821 | 61 | 7 | $1.68 | ITM call sale |

**Net interpretation.** The $211K Jan'27 $20C bid-side block + $66K Jan'27
$12.5C bid-side + $54K Jan'28 $45C bid-side together look like a **single
institutional overwriter** or **call spread seller** at the long end —
this is *neutral-to-mildly-bearish into 2027*. Against that, the Sep'26
$17.5C ask-side campaign + put-selling at $15/$17.5 is *bullish in the 4-9
month window*. The two stories are not contradictory if you read them as
**bullish bias near-term, capped enthusiasm into 2027** — a real-money
"own it but sell the $20 strike" overwrite posture. That is precisely
what disciplined accumulation looks like.

### New positioning (unusual vol / OI ratios)

`options_flow_unusual_volume`, top 6, min_vol_oi_ratio = 3:

| Contract | OI | Vol | Vol/OI | Premium | IV | Read |
|---|---|---|---|---|---|---|
| 2026-05-22 C 16.5 | 4 | 153 | **38.25x** | $10,650 | 102% | Lottery upside |
| 2026-07-17 C 17.5 | 4 | 151 | **37.75x** | $28,194 | 85% | New upside |
| 2026-07-17 P 17.5 | 17 | 137 | 8.06x | $36,718 | 80% | New ATM put |
| 2026-07-17 P 15 | 44 | 242 | 5.50x | $32,513 | 79% | New OTM put |
| 2026-05-22 C 17 | 94 | 359 | 3.82x | $18,370 | 100% | New short-dated upside |
| 2026-09-18 C 17.5 | 229 | 783 | 3.42x | $258,658 | 96% | The campaign target |

The **Jul'26 17.5C/17.5P pair both opening** with similar vol/OI is a
**Jul'26 17.5 straddle/strangle** signature — someone is buying volatility
into mid-July, *not* taking a direction view. With near-dated IV already
at ~80-100%, this is a high-conviction "FSLY will move" bet rather than
"FSLY will move up."

### Largest premium prints

`options_flow_top_premium_trades`, top 10 by $ premium:

| # | Time (Z) | Contract | Side | Premium | Size | Δ | IV |
|---|---|---|---|---|---|---|---|
| 1 | 13:33:09 | 2027-01-15 C 20 | **bid** | $205,000 | 500 | 0.57 | 96.5% |
| 2 | 19:22:44 | 2026-09-18 C 17.5 | **ask** | $61,710 | 187 | 0.57 | 96.9% |
| 3 | 19:22:44 | 2026-09-18 C 17.5 | **ask** | $58,410 | 177 | 0.57 | 96.9% |
| 4 | 16:36:37 | 2027-01-15 C 12.5 | **bid** | $52,140 | 79 | 0.77 | 94.4% |
| 5 | 16:24:19 | 2028-01-21 C 45 | **ask** | $37,000 | 100 | 0.43 | 97.1% |
| 6 | 16:25:40 | 2028-01-21 C 45 | **bid** | $33,300 | 90 | 0.43 | 97.1% |
| 7 | 19:22:44 | 2026-09-18 C 17.5 | **ask** | $32,010 | 97 | 0.57 | 96.9% |
| 8 | 19:22:44 | 2026-09-18 C 17.5 | **ask** | $21,450 | 65 | 0.57 | 96.9% |
| 9 | 19:22:44 | 2026-09-18 C 17.5 | **ask** | $16,830 | 51 | 0.57 | 96.9% |
| 10 | 15:55:14 | 2028-01-21 C 45 | **ask** | $12,210 | 33 | 0.43 | 97.1% |

The 19:22:44 cluster (#2, #3, #7, #8, #9) on Sep'26 $17.5C is **a single
sweep broken into ~5 prints in 0 seconds** — classic "fill at the ask
across the book" pattern, ~$190K of fresh ask-side call demand in one
shot. This is the headline bullish print of the day.

The $37K/$33,300 Jan'28 $45C pair (rows 5 & 6) one minute apart on opposite
sides looks like a **cross / agency match** — net zero direction.

### IV outliers + Greeks

`options_flow_iv_outliers`, top 7 by max_iv (min_vol=20):

| Contract | Avg IV | Max IV | Vol | Premium |
|---|---|---|---|---|
| 2026-06-18 P 12.5 | 96% | **210%** | 61 | $1,764 |
| 2026-05-22 P 22 | 159% | 176% | 30 | $16,275 |
| 2026-06-18 C 45 | 156% | 170% | 116 | $680 |
| 2026-05-22 C 22 | 151% | 155% | 30 | $94 |
| 2026-06-18 P 17.5 | 82% | 155% | 135 | $28,019 |
| 2026-06-18 C 40 | 138% | 139% | 134 | $670 |
| 2026-05-22 C 21 | 132% | 137% | 43 | $139 |

Two structural takeaways:

1. **Wings are massively bid.** OTM call IV at $22/$40/$45 strikes is
   running 130-170%; OTM put IV at $12.5 is hitting 210% briefly. The
   skew is **two-sided** — the market is paying up for tails in both
   directions. This is the IV signature of either **upcoming earnings**
   or a **known binary catalyst** (M&A, lawsuit, contract win).
2. **ATM 5/22 IV at 100% on the 17C with 359 vol** confirms the
   near-dated lottery thesis: 4 days from snapshot, IV at the money is
   ~100%. The June 17.5P at IV 82% (max 155%) backs this up.

The single Greek-screener standout is the **5/22 21.5P at $5.05 mid, IV
170%, size 19** — at delta −0.92 this is functionally short stock with
limited downside; equivalent of "I want to be short $32K of FSLY through
Friday but cap my loss at $9,500." A trader with a very specific 4-day
view.

### Multi-day persistence

`hot_chains_sweep_persistence`, days=5, symbol=FSLY:

| Field | Value |
|---|---|
| sessions_in_top | **5 / 5** |
| consistency_score | **1.0** |
| dominant_direction | mixed |
| total_sweep_premium (5d) | $642,945 |
| dates_covered | 2026-05-12 → 2026-05-18 |

A consistency score of 1.0 across 5 sessions for a $16-handle small-cap
is unusual and is the single highest-quality "this is real" signal in
phase 1.

### Market-wide smart-money flow

FSLY does not surface in the top-25 of either `hot_chains_smart_money_flow`
direction (the list is anchored by VIX/SPX/IWM/large-caps). Per skill
guidance, this is **not** a "no flow" result — it just means FSLY's
absolute notional is below the market-wide cut. The per-symbol calls
above (sweeps, unusual vol, top premium) are the authoritative read.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|---|---|---|
| `mcp__uw-pp__options_flow_sweeps` | symbol=FSLY, min_premium=10000, top_n=25, date=2026-05-18 | 14 sweeps; ask-side Sep'26 17.5C is the largest at $255K |
| `mcp__uw-pp__options_flow_unusual_volume` | symbol=FSLY, min_vol_oi_ratio=3, top_n=25, date=2026-05-18 | 6 rows; call/put mix; near-dated lottery 5/22 16.5C at 38x vol/OI |
| `mcp__uw-pp__options_flow_top_premium_trades` | symbol=FSLY, top_n=25, date=2026-05-18 | $205K bid-side Jan'27 20C is largest; rest dominated by ask-side Sep'26 17.5C cluster |
| `mcp__uw-pp__options_flow_iv_outliers` | symbol=FSLY, top_n=15, date=2026-05-18, min_iv=0.5, min_volume=20 | Wings bid 130-210% IV; ATM ~100% 4 days out |
| `mcp__uw-pp__options_flow_greek_screener` | symbol=FSLY, top_n=15, sort_by=premium, date=2026-05-18 | Confirms call dominance; one −0.92 delta 5/22 21.5P standout |
| `mcp__uw-pp__hot_chains_sweep_persistence` | symbol=FSLY, days=5, top_n=20 | 5/5 sessions, consistency 1.0, $642,945 5d premium |
| `mcp__uw-pp__hot_chains_smart_money_flow` | direction=bullish, top_n=25, min_volume=100, date=2026-05-18 | FSLY absent (sub-threshold) |
| `mcp__uw-pp__hot_chains_smart_money_flow` | direction=bearish, top_n=25, min_volume=100, date=2026-05-18 | FSLY absent (sub-threshold) |

## Tool errors

(none)

## Verdict for downstream phases

- **Bias from this phase:** bullish (with caveats)
- **Conviction:** 3.5 / 5 — high *persistence*, moderate *magnitude*. The
  campaign is real (5/5 sessions, $643K) but absolute premium is small by
  institutional standards.
- **Three datapoints later phases must remember:**
  1. **Sep'26 $17.5C is the campaign strike.** Ask-side aggregated $255K
     on 2026-05-18, OI 229 → vol 783 same day, max-pain candidate for
     phase 3.
  2. **A $205K bid-side Jan'27 $20C block** caps the upside narrative —
     someone is writing the $20 strike at scale. Phase 3 OI work must
     check whether the $20 strike has unusual OI buildup that confirms
     this is overwriting volume.
  3. **IV term structure is hot on both wings**, ATM 100% on the front
     week — strong signal for either earnings or a binary catalyst.
     Phase 5 (historical IV) and phase 6 (catalyst calendar) must
     resolve which.
- **Open questions:**
  - Is dark pool tape *confirming* the bullish call campaign (price
    above VWAP, large block bids), or *fading* it (block sells)?
    → phase 2.
  - Is FSLY pinned to a known earnings date inside the 5/22 → 7/17
    options window? → phase 5/6.
  - The Jul'26 17.5C/17.5P pair opening together — is this a long
    straddle (volatility bet) or short straddle (premium-collection)?
    Phase 3 OI changes will disambiguate.
