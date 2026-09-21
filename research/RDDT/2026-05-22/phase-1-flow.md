# Phase 1 — Options Flow

**Ticker:** RDDT
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T00:00:00Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md

## Summary

Net bias is **bearish**, and — critically — the bearishness survives stripping
0DTE noise. The whole-tape aggregate is net-bearish (`net_flow −$6.98M`,
bearish_premium $21.0M vs bullish $14.1M), and the DuckDB ex-0DTE cut confirms it:
dated-option premium is **$12.19M bullish vs $19.54M bearish** while 0DTE is
roughly balanced ($1.87M vs $1.50M). The mechanism is two-sided and coherent:
**net call selling** ($13.10M sold on the bid vs $7.61M bought on the ask, ex-0DTE)
**plus net put buying** ($6.44M bought vs $4.58M sold). The one major caveat is a
timeframe divergence — the **5-day sweep campaign is dominant-bullish** ($30.3M,
RDDT in top sweeps 5/5 sessions) — so today's bearish tape reads as a *fade /
unwind of the prior bullish campaign* coinciding with phase-0.5's "most net-bearish
day in the window." Conviction is tempered by modest absolute dollars and the
cheap IV (rank 18.7).

## Key signals

- Whole-tape **net_flow −$6.98M**, bearish $21.0M > bullish $14.1M, P/C 0.92 —
  the most net-bearish session in RDDT's 31-day window (carry from
  phase-0.5-context.md §self-history) [FLOW:insights_deep_dive]
- Ex-0DTE aggressor split: **calls net SOLD $5.5M** (bid $13.1M − ask $7.6M),
  **puts net BOUGHT $1.9M** (ask $6.4M − bid $4.6M) → coherent bearish two-sided
  flow, not pin artifact `[FLOW:aggressor_ex0dte DUCKDB]`
- Largest prints are **bid-side call sales across tenors**: 100C Sep'18 bid $0.97M
  (Δ0.84, deep ITM), 120C Jun'18 bid $0.52M, 130C/200C/280C LEAPs bid — monetizing
  /writing the $132→$172 run-up [FLOW:top_premium_trades] [FLOW:sweeps]
- Near-dated **put buying in the swing window**: 8–45DTE puts $4.31M > calls
  $3.41M; 135P 6/26 ask $0.34M, 140P 6/18 ask $0.31M, 165P 6/18 ask, 200P 6/18 ask
  [FLOW:sweeps] [FLOW:dte_bucket DUCKDB]
- **Divergence:** 5-day sweep persistence = BULLISH, consistency 1.0, 5/5
  sessions, $30.3M — trailing campaign contradicts today's bearish flip
  [FLOW:sweep_persistence]

## Detailed findings

### Whole-tape aggregate (read top-N against this) — [FLOW:insights_deep_dive]

| Field | Value |
|-------|-------|
| call_premium | $22,935,424 |
| put_premium | $15,138,064 |
| bullish_premium | $14,065,953 |
| bearish_premium | $21,041,632 |
| **net_flow** | **−$6,975,679** |
| call_volume / put_volume | 34,915 / 31,972 |
| put_call_ratio | 0.9157 |
| iv_rank | 18.73 (cheap) |

Note the apparent paradox — *more* premium sits in calls ($22.9M) than puts
($15.1M), yet the tape is net **bearish**. The aggressor split resolves it: the
call premium is dominated by **sellers** (bid-side), so heavy call volume here is
distribution/writing, not accumulation.

### Aggressor & delta-notional split, ex-0DTE — `[FLOW:aggressor_ex0dte DUCKDB]`

| type | side | prem $M | Δ-notional $bn |
|------|------|---------|----------------|
| call | ask (bought) | 7.61 | +0.042 |
| call | **bid (sold)** | **13.10** | +0.068 |
| put | **ask (bought)** | **6.44** | −0.040 |
| put | bid (sold) | 4.58 | −0.027 |

Net customer delta ≈ **−$39M notional (modestly net short)**. Both legs lean
bearish: calls net sold, puts net bought. Net premium ex-0DTE: **bullish $12.19M
vs bearish $19.54M** → the bearish tilt is genuine directional flow, not 0DTE pin.

### Premium by DTE bucket — `[FLOW:dte_bucket DUCKDB]`

| bucket | call $M | put $M | read |
|--------|---------|--------|------|
| 0–1DTE | 0.83 | 2.76 | pin noise; put-heavy but tiny premium |
| 2–7DTE | 2.79 | 2.49 | balanced near-week |
| **8–45DTE** | 3.41 | **4.31** | **put-heavy in the actionable swing window** |
| 46–180DTE | 5.66 | 1.90 | call-heavy — but the Sep 100C ITM was *sold* |
| LEAP | **10.25** | 3.68 | biggest bucket, but bid-side (calls *sold*) |

The LEAP call bucket is the largest by premium but is dominated by **bid-side
sales** (130C Jan'28, 200C Jun'28, 280C Jan'28 — see sweeps) — i.e. long-dated
upside being *monetized/written*, consistent with the net-bearish aggregate.

### Sweeps (ask vs bid) — [FLOW:sweeps]

Top sweeps by premium are overwhelmingly **bid-side calls** (selling):
100C 9/18 bid $0.97M, 130C '28 bid $0.67M, 200C 6/16'28 bid $0.66M, 120C 6/18 bid
$0.53M, 280C '28 bid $0.48M. Bid-side put: 150P 0DTE $0.70M (0DTE, discount).
Ask-side (buying) sweeps are smaller and split: 240C 6/16'28 ask $0.64M (lone
LEAP-call *buy*), plus ask-side near-dated put buys — 135P 6/26 $0.34M, 140P 6/18
$0.31M, 145P 0DTE $0.26M. **Read: institutional call-writing/closing > buying;
genuine but moderate near-dated put accumulation.**

### New positioning (unusual vol, vol/OI ≥3) — [FLOW:unusual_volume]

Dominated by **near-dated calls** at 128–149 strikes (5/29) and 0DTE — 142C 5/29
vol/OI 152.6, 143C 73, 128C/129C 5/29 ~25–36×. High *volume*, but the sweeps show
much of the 5/29 call activity (128C 5/29 bid $0.29M, 129C 5/29) is **bid-side**.
Two larger put prints stand out as genuine downside opens: **130P 12/18 $1.13M
(vol/OI 6.5)** and **115P 11/20 $0.71M (vol/OI 3.6, 410 trades)** — dated OTM put
accumulation. → phase-3 must check whether these are OI-building.

### IV outliers + Greeks — [FLOW:iv_outliers] [FLOW:greek_screener]

All IV outliers are **0DTE (5/22)** contracts showing absurd avg_iv (8–10) / max_iv
(up to 92) — pure 0DTE pin/expiry artifacts; **discount entirely**. The only
non-0DTE high-IV note: LEAP calls priced ~0.76–0.77 IV (Sep/Jan'28 100–130C), i.e.
long-dated vol is the richest part of the surface — yet another reason those LEAP
calls are being *sold*. Greek screener confirms the biggest delta-notional prints
are the deep-ITM Sep 100C (Δ0.84) sold and the Dec 130P (Δ−0.33) two-way.

### Market-wide context

RDDT does **not** appear in either the bullish or bearish `smart_money_flow`
top-25 (those are SMH/GLD/NVDA/SPY/TSLA-dominated) — RDDT's flow is real but
**mid-size**, not a market-leading footprint. Consistent with phase-0.5's "~15th
single-name on net bearish, modest absolute dollars."

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `insights_deep_dive` | symbol=RDDT, date=5/22 | net_flow −$6.98M, bearish>bullish |
| `options_flow_sweeps` | symbol=RDDT, min_prem=100k, top25 | top sweeps bid-side calls (selling) |
| `options_flow_top_premium_trades` | symbol=RDDT, top25 | 100C Sep bid $0.97M largest |
| `options_flow_unusual_volume` | symbol=RDDT, vol/OI≥3, top25 | near-dated calls + 130P/115P put opens |
| `options_flow_iv_outliers` | symbol=RDDT, top15 | all 0DTE pin artifacts — discount |
| `options_flow_greek_screener` | symbol=RDDT, top15, by premium | Sep100C Δ0.84 sold dominates Δ-notional |
| `hot_chains_smart_money_flow` | bullish & bearish, top25 | RDDT absent (mid-size flow) |
| `hot_chains_sweep_persistence` | symbol=RDDT, 5d | BULLISH, 5/5 sessions, $30.3M |
| `[DUCKDB]` §A | aggressor ex-0DTE, dte buckets | calls net sold, puts net bought |

## Tool errors

None. (`smart_money_flow` returned no RDDT rows — recorded as "mid-size flow, not
a market-wide leader," not re-run with looser thresholds per phase guidance.)

## Verdict for downstream

- **Net bias:** bearish (genuine directional, ex-0DTE confirmed)
- **Conviction:** 3/5 — coherent two-sided bearish flow (calls sold + puts bought)
  and the most net-bearish day in the window, but modest absolute dollars (~$7M
  net), cheap IV, and a **conflicting 5-day bullish sweep campaign** cap conviction.
- **Three datapoints later phases must remember:**
  1. Bearish is real ex-0DTE: dated bullish $12.19M vs bearish $19.54M; mechanism
     = call selling + put buying; customer net delta ≈ −$39M.
  2. **Timeframe conflict:** trailing 5-day sweeps were dominant-BULLISH ($30.3M,
     5/5) — today is a bearish *flip/unwind*. Phase-3/5 must judge whether the
     bullish campaign's OI is now being closed.
  3. Dated OTM put opens to watch: **130P 12/18 $1.13M** and **115P 11/20 $0.71M**;
     LEAP calls (130C/200C/280C) being **sold**, not bought.
- **Open questions:**
  - Is dark pool confirming distribution (sells above/below spot)? → phase-2
  - Are the bid-side LEAP/ITM call sales *closing* existing OI (profit-taking) or
    *opening* new short-call writes? → phase-3 (oi_position_rolls, oi_decrease)
  - Does the 130P/115P put buildup show in OI increases? → phase-3
