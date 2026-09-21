# Phase 1 — Options Flow

**Ticker:** FSLR · **As-of:** 2026-07-20 · **Underlying:** $210.56 · **Version:** v1
**Generated:** 2026-07-20
**Cites:** phase-0.5-context.md (`[CTX:] unusual_verdict=BUSY_NAME_NORMAL_DAY`,
net_dir self-pctile 15.5, IV rank 99.1); phase-0-intake.md (as-of, options active).

## Summary

FSLR's tape is **net bearish with a heavy short-volatility overlay** into the
2026-07-30 earnings. Whole-tape net directional premium is **−$3.80M**
(bullish $11.89M vs bearish $15.69M) and there is a **5-session persistent
*bearish* sweep campaign** (consistency score **1.0**, in the top-sweep list all
5 sessions, $16.3M cumulative) — the single strongest flow signal today. But the
largest individual prints are **premium-harvesting**: ~$10M of OTM calls and
~$6M of OTM puts **sold on the bid** into 99th-percentile IV rank (Sep 330C/350C
sold in 4,000-lot clips, Sep 260C/280C sold), i.e. straddle/strangle-selling and
call-overwriting, not directional buying. Per `[CTX:]` BUSY_NAME_NORMAL_DAY, this
phase's downstream conviction is **capped at `+`**.

## Key signals

- **[FLOW:sweep_persistence]** 5/5 sessions in top sweeps, **dominant_direction =
  bearish**, consistency **1.0**, $16.3M cumulative — a genuine multi-day bearish
  campaign, not a one-day print.
- **[FLOW:unusual_volume]** All three new-position (vol/OI ≥3) prints are **puts
  opening** — notably **165P Aug-21, vol 2,359 / OI 233 (29×… 10.1× vol/OI),
  $863k** — fresh bearish/hedge positioning.
- **[FLOW:top_premium_trades]** Largest prints are **bid-side call *selling***:
  Sep 260C ($2.91M), 280C ($2.80M), Jun-27 340C ($2.00M), Sep 350C ($0.94M) —
  ~$10.1M calls sold on the bid vs only $1.5M bought on the ask. Overwriting /
  short-vol into IV rank 99.
- **[FLOW:sweeps ask]** The largest *aggressive buyer-initiated* print is a put:
  **210P Jul-31 (ATM), $1.01M, 731 lots** — a directional/hedge put bought into
  earnings; call ask-buying ($2.09M) barely edges put ask-buying ($1.80M).
- **[FLOW:insights_deep_dive]** Whole-tape **net_flow = −$3.80M** (derived
  bull−bear); P/C prem-ratio 0.42 (call-heavy by premium — but that call premium
  is being *sold*, see above), IV rank **99.1**, implied move **±5.31%**.

## Detailed findings

### Whole-tape aggregate — `[FLOW:insights_deep_dive]`
| Field | Value |
|-------|-------|
| Call premium | $17.23M |
| Put premium | $12.55M |
| Bullish premium | $11.89M |
| Bearish premium | $15.69M |
| **Derived net_flow (bull−bear)** | **−$3.80M (bearish)** |
| Call vol / Put vol | 23,422 / 9,795 |
| P/C ratio (prem-wt) | 0.418 |
| IV rank / IV30d | 99.1 / 76.4% |
| Implied move | ±$10.89 (±5.31%) |
| Total OI | 541,050 |

Read the top-N below *against* this: the call-heavy premium headline is misleading
— the big calls are being **sold**, so the true directional balance is the
net_flow (−$3.8M) plus the persistent bearish sweeps.

### Sweeps (ask vs bid)
- **Ask (buyer-initiated):** call $2.09M / put $1.80M (10 rows). Top: **210P
  Jul-31 $1.01M** (ATM put buy), 260C Sep $0.88M, 185P Jan-27 $0.46M.
- **Bid (seller-initiated):** call $11.05M / put $7.50M (18 rows). Top: 260C Sep
  $2.93M (3,028 lots), 280C Sep $2.82M (4,026 lots), 170P Jan-28 $2.51M, 340C
  Jun-27 $2.00M, 330C/350C Sep ($0.98M/$0.94M, ~4,000 lots each). → dominant
  activity is **selling far-OTM calls** and some OTM puts = short-vol.

### New positioning (unusual vol, vol/OI ≥ 3) — `[FLOW:unusual_volume]`
| Type | Strike | Exp | Vol/OI | vol/OI× | Prem | IV |
|------|--------|-----|--------|---------|------|-----|
| Put | 175 | 2026-07-24 | 755/26 | 29.0 | $15k | 86% |
| **Put** | **165** | **2026-08-21** | **2,359/233** | **10.1** | **$863k** | 77% |
| Put | 140 | 2026-09-18 | 158/44 | 3.6 | $35k | 74% |

All fresh positioning is **puts** → bearish/hedge new interest.

### Largest premium prints (top 8) — `[FLOW:top_premium_trades]`
| Type | Strike | Exp | Side | Prem | Δ |
|------|--------|-----|------|------|---|
| C | 260 | 2026-09-18 | bid | $2.91M | 0.29 |
| C | 280 | 2026-09-18 | bid | $2.80M | 0.22 |
| C | 340 | 2027-06-17 | bid | $2.00M | 0.33 |
| P | 170 | 2028-01-21 | bid | $1.96M | −0.24 |
| P | 210 | 2026-09-18 | bid | $1.44M | −0.46 |
| C | 350 | 2026-09-18 | bid | $0.94M | 0.08 |
| C | 260 | 2026-09-18 | ask | $0.85M | 0.27 |
| C | 330 | 2026-09-18 | bid | $0.76M | 0.09 |

By side×type: **bid-call $10.12M** (9), bid-put $4.75M (6), ask-call $1.52M (5),
mid-call $1.23M (4), ask-put $0.09M (1). Bid-side call selling dominates.

### IV outliers + Greeks
- `iv-outliers`: **0 rows** — no single contract flagged as an IV outlier
  (consistent with IV being uniformly elevated across the surface, not spiked in
  one line; IV rank 99 is a whole-surface earnings phenomenon).
- `greek-screener`: largest premium concentrated in low-Δ OTM Sep calls
  (Δ0.08–0.33) and mid-Δ puts (210P Δ−0.46) — the gamma/vega per line is small;
  no single dominant directional delta bet.

## Tool calls
| Tool | Args | Result |
|------|------|--------|
| options-flow sweeps (ask) | FSLR, min-prem 100k, top 25, date 07-20 | 10 rows |
| options-flow sweeps (bid) | FSLR, min-prem 100k, top 25, date 07-20 | 18 rows |
| options-flow unusual-volume | FSLR, min-vol-oi 3, top 25 | 3 rows (all puts) |
| options-flow top-premium-trades | FSLR, top 25 | 25 rows |
| options-flow iv-outliers | FSLR, top 15 | 0 rows |
| options-flow greek-screener | FSLR, sort premium, top 15 | 15 rows |
| hot-chains smart-money-flow | bullish/bearish, top 10, min-vol 500 | FSLR outside both top-10 |
| hot-chains sweep-persistence | FSLR, 5 days, top 20 | **1 row: bearish, consistency 1.0, 5/5 sessions, $16.3M** |
| hot-chains sweep-ratio | top 15, min-vol 500, ratio 0.3 | FSLR not in list |
| insights deep-dive | FSLR (whole-tape aggregate) | uw_screener block above |

## Tool errors
`hot-chains sweep-persistence` rejected `--date` ("unknown flag"). This tool
anchors to the latest available date, which **is** the as-of (2026-07-20, per
phase-0 available-dates) — re-ran without the flag; result is as-of-correct.
All other reads round-tripped through `jq` cleanly.

## Verdict for downstream

- **Net bias:** **BEARISH** (net_flow −$3.8M + 5-session persistent bearish sweep
  campaign + all new positioning in puts), with a **dominant short-volatility
  overlay** (call/put selling into IV rank 99 ahead of 7/30 earnings). The
  bullish-by-premium headline is an artifact of large calls being *sold*.
- **Conviction: 3/5** — the persistence signal is real and directional, but
  magnitude is modest, much of the tape is non-directional vol-harvest, and
  `[CTX:]` BUSY_NAME_NORMAL_DAY **caps phases 1–2 confluence at `+`**.
- **Three datapoints later phases must remember:**
  1. 5-session persistent **bearish** sweep campaign, consistency 1.0, $16.3M.
  2. Massive OTM-call **selling** (Sep 330C/350C in 4,000-lots) + put selling =
     short-vol / earnings premium harvest — dealers likely getting **long** these
     options (watch phase-3/4 for the dealer-positioning implication).
  3. IV rank **99.1** with earnings **2026-07-30** (10 sessions out) — any
     directional plan must respect the post-earnings **IV crush**.
- **Open questions for later phases:**
  - Is dark pool (phase-2) confirming distribution/accumulation under this bearish
    tape, or is the price being defended?
  - Where are the OI walls / max-pain (phase-3/4) — do the sold Sep 260/280/330
    calls define a dealer-long ceiling?
  - Does the 5-day bearish sweep campaign show up as a phase-5 signal with a
    measurable win-rate?
