# Phase 1 — Options Flow

**Ticker:** BILI
**As-of date:** 2026-05-20 (data date 2026-05-19)
**Generated:** 2026-05-20T09:35:00-04:00
**Upstream phases cited:** phase-0-intake.md

## Summary

Tape skews **moderately bullish on premium magnitude** but **mixed on direction**.
The largest single signature is a $235k institutional ask-side sweep of Jan-2027
$25 calls (1067 contracts, 41 prints). Counter-pressure comes from a clean
141-contract 22.5 put diagonal roll (May 22 → June 5) and a small LEAP-put
program (Jan-2028 $25/$32 puts) — both bearish but materially smaller premium.
BILI has appeared in the top sweep-persistence cohort for **5 of 5 recent
sessions** ($2.28M cumulative sweep premium), confirming continuous institutional
engagement rather than one-off interest.

## Key signals

- Net call premium dominance: Jan-2027 $25C **$235,084 ask-side sweep**, 1067
  contracts, delta 0.41, IV 0.595, vega 0.063 [FLOW:options_flow_sweeps].
- Largest single print: Jan-2027 $25C **$76,340 ask** at 18:28:07Z, underlying
  $19.88 [FLOW:top_premium_trades].
- Bearish counter: 22.5 strike put **diagonal roll** at 18:02:59Z — 141c sold
  at bid 5/22 ($42,300) + 141c bought at ask 6/5 ($44,415), same trader
  signature [FLOW:top_premium_trades].
- New positioning: June 18 $19.5C **vol/OI 4.35x, $36,855 ask-side** —
  opening directional bet [FLOW:unusual_volume].
- Persistence: BILI in top sweep cohort 5/5 sessions, consistency_score 1.0,
  $2,276,116 5-day sweep premium [FLOW:sweep_persistence].

## Detailed findings

### Spot anchor

Underlying prices stamped across the day on the top-premium tape range
**$18.685 (13:30Z open print) → $19.945 (19:46Z late-day print)**, with cluster
at $19.88 on the big 18:28Z Jan-2027 $25C sweep. **Working EOD spot: ~$19.94**.

### Sweeps — ask vs bid breakdown [FLOW:options_flow_sweeps]

Top sweep rows (filtered to BILI):

| Strike / Expiry | Type | Side | Premium | Size | Trades | Avg Price |
|---|---|---|---|---|---|---|
| **$25 / 2027-01-15** | **call** | **ask** | **$235,084** | **1067** | **41** | $2.21 |
| $22.5 / 2026-06-05 | put | ask | $52,582 | 167 | 3 | $3.15 |
| $22.5 / 2026-05-22 | put | bid | $50,947 | 170 | 5 | $2.96 |
| $19.5 / 2026-05-22 | call | ask | $29,923 | 527 | 70 | $0.53 |
| $30 / 2027-01-15 | call | bid | $27,764 | 214 | 27 | $1.31 |
| $32 / 2028-01-21 | put | ask | $22,425 | 15 | 1 | $14.95 |
| $20 / 2026-05-22 | call | ask | $20,635 | 575 | 80 | $0.37 |
| $30 / 2027-01-15 | call | mid | $19,650 | 145 | 11 | $1.34 |
| $19 / 2026-05-22 | call | ask | $18,725 | 237 | 42 | $0.81 |
| $19.5 / 2026-06-18 | call | ask | $18,280 | 154 | 14 | $1.10 |

**Net ask-call vs bid-call premium (BILI rows above):** ask-side calls ~$320k,
bid-side calls ~$58k → **5.5x ask/bid ratio in calls** = aggressive buying.
**Net ask-put vs bid-put premium:** ask-side puts $52k + LEAP puts $36k =
$88k; bid-side puts $51k. Roughly balanced in puts.

### New positioning [FLOW:unusual_volume]

Only **two** contracts cleared the vol/OI ≥ 3x threshold:

| Contract | Vol | OI | Vol/OI | Premium | Avg IV | Read |
|---|---|---|---|---|---|---|
| 2026-05-22 $18.5 PUT | 604 | 119 | 5.08x | $14,346 | 79.0% | Small-lot weekly hedge |
| 2026-06-18 $19.5 CALL | 296 | 68 | 4.35x | $36,855 | 55.2% | **Opening monthly long calls** |

The June 18 $19.5C is the most actionable opening signal — at ATM 30 DTE, this
is a directional intent print, not a hedge.

### Largest premium prints [FLOW:top_premium_trades]

Re-stacked by signature:

**Bullish bloc (Jan-2027 $25 calls — all ask, all 18:28:07Z):**
- 347c @ $2.20 = $76,340 (delta 0.41, IV 0.595)
- 134c @ $2.20 = $29,480
- 114c @ $2.20 = $25,080
- 105c @ $2.20 = $23,100
- 105c @ $2.20 = $23,100
- 44c @ $2.20 = $9,680
- 34c @ $2.20 = $7,480
- → 8 prints totaling **883 contracts / $217,260** at a single timestamp.
  This is a worked institutional buy program at one print or one broker
  splitting size across exchanges. Underlying was $19.88.

**Bearish bloc (22.5 put roll, 18:02:59Z):**
- Sell 141c 5/22 $22.5P @ $3.00 bid = $42,300 received (IV 151%, delta -0.81 — deep ITM)
- Buy 141c 6/5 $22.5P @ $3.15 ask = $44,415 paid (IV 76%, delta -0.76)
- **Net cost ~$2,115** to extend a bearish position by 14 days. Notional
  exposure preserved (~141 × 100 × delta 0.76 ≈ 10,716 share-equivalent short
  delta). This is a clear **stay-bearish roll**, not a fresh open.

**LEAP put bloc (13:30:15Z–13:30:25Z, single trader):**
- Buy 15c 2028-01-21 $32P @ $14.95 ask = $22,425 (IV 50%, delta -0.69 — deep ITM)
- Buy 15c 2028-01-21 $25P @ $9.30 ask = $13,950 (IV 52%, delta -0.53)
- Combined **$36,375 long premium on 20-month puts** — long vega bet (vega
  0.085 × 30 contracts), small notional, behaves like a long-dated structural
  short / vol-up hedge.

**Retail-flavored bullish bloc (5/22 weekly calls, scattered):**
- $19.5 / $20 / $19 / $18 / $17.5 strikes, ~$50k aggregate ask-side, small
  premium per print → end-of-week lottery / gamma-buying.

### IV outliers + Greeks [FLOW:iv_outliers,greek_screener]

Only **3 contracts** cleared the IV ≥ 100% screen:

| Contract | Vol | Premium | Max IV | Read |
|---|---|---|---|---|
| 2026-05-22 $26.5C | 162 | $162 | 170% | Far-OTM lottery — ignore |
| 2026-05-22 $26C | 168 | $170 | 162% | Far-OTM lottery — ignore |
| 2026-05-22 $22.5P | 170 | $50,947 | 156% | The deep-ITM put leg of the roll |

The $22.5P 5/22 IV at 156% is **synthetic** — for a 3-day deep-ITM put it
mostly reflects extrinsic decay pricing of intrinsic value. Do not treat as
a real vol signal. Front-week realized-IV stress should be sourced from phase 4
term structure rather than this row.

### Smart-money flow market-wide [FLOW:smart_money_flow]

BILI **did not** appear in the top-25 market-wide bullish or bearish
smart_money_flow rows (which were dominated by IEF, TSLA, HYG, SPY, IWM, WULF,
VIX). Interpretation: BILI's flow is too small in absolute volume terms to
crack the index/ETF-dominated cross-sectional leaderboard, but its relative
positioning (5/5 persistence) and per-ticker premium structure are still
informative. **No market-wide smart-money confirmation either direction.**

### Multileg [FLOW:multileg]

BILI did not appear in the top-25 market-wide multileg list. None of the
22.5 put roll prints were tagged as a single combo by the multileg classifier
(though timestamp identity 18:02:59Z makes the human read clearly a roll).
**No detected complex spread positioning in BILI today.**

### Sweep persistence [FLOW:sweep_persistence]

```
ticker  sessions_in_top  consistency_score  dominant_direction  5-day premium
BILI    5/5              1.00               mixed               $2,276,116
```

**This is the cleanest single bullish-engagement datapoint:** for 5 consecutive
sessions (2026-05-13 → 2026-05-19) BILI has been in the top sweep cohort. The
"mixed" direction tag means the consistency is in *activity*, not in *one-way
bias*, which aligns with what we see today: bullish call sweeps + bearish put
rolls coexisting.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|---|---|---|
| `options_flow_sweeps` | symbol=BILI, date=2026-05-19, min-premium=10000, top-n=25 | 22 BILI sweep rows |
| `options_flow_unusual_volume` | symbol=BILI, date=2026-05-19, min-vol-oi-ratio=3, top-n=25 | 2 contracts (5/22 $18.5P, 6/18 $19.5C) |
| `options_flow_top_premium_trades` | symbol=BILI, date=2026-05-19, top-n=25 | 25 BILI prints, top = $76,340 Jan-27 $25C |
| `options_flow_iv_outliers` | symbol=BILI, date=2026-05-19, top-n=15 | 3 IV outliers (2 far-OTM calls, 1 deep-ITM put) |
| `options_flow_greek_screener` | symbol=BILI, date=2026-05-19, sort=premium, top-n=15 | Confirms Jan-27 $25C delta 0.41 / vega 0.063 |
| `hot_chains_smart_money_flow` | direction=bullish/bearish, date=2026-05-19 | No BILI rows market-wide |
| `hot_chains_sweep_persistence` | symbol=BILI, days=5 | 5/5 sessions, score 1.0, $2.28M |
| `hot_chains_multileg` | date=2026-05-19, top-n=25 | No BILI rows |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** **mixed-bullish** (calls dominate by 5.5x ask/bid
  premium but bearish hedges are well-organized and persistent).
- **Conviction:** **3 / 5** — institutional engagement is real (5/5
  persistence, $217k single-timestamp Jan-2027 $25C sweep), but the bearish
  put roll plus LEAP puts means flow is not unanimously long. Not a "stuff
  the boat with calls" tape.
- **Three things later phases must remember:**
  1. Working spot **~$19.94** as of EOD 2026-05-19.
  2. **Jan-2027 $25 strike** is the institutional bullish anchor (883
     contracts / $217k single-print sweep). Phase 3 should check whether this
     shows up as OI build tomorrow; phase 4 should see this as net negative
     dealer-call inventory at that strike.
  3. **141-contract 22.5 put position is alive** and was rolled May 22 → June
     5. Phase 4 should expect dealer net-positive put inventory at $22.5
     (gamma support / dealers short downside).
- **Open questions:**
  - Is dark pool confirming the bullish premium with above-average ticker
    block volume? → phase 2.
  - Where does Jan-2027 $25 strike currently sit on the OI ladder vs other
    strikes? → phase 3.
  - Is realized IV consistent with the 56-79% IV being paid in the front
    months, or is vol being purchased rich? → phase 4 + phase 5.
  - What macro / earnings catalyst is the Jan-2027 expiry pricing for?
    (BILI fiscal-year reports typically in late-Feb/early-March.) → phase 6
    + phase 7.
