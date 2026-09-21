# Phase 1 — Options Flow

**Ticker:** RDDT
**As-of date:** 2026-05-20 (data anchor 2026-05-18; see phase-0-intake.md)
**Generated:** 2026-05-19T00:10:00-04:00
**Upstream phases cited:** phase-0-intake.md

## Summary

RDDT's options tape on 2026-05-18 is **bullishly biased with high
persistence**: `hot_chains_sweep_persistence` returns RDDT with
`sessions_in_top=5/5`, `consistency_score=1.0`, `dominant_direction=bullish`,
and `total_sweep_premium=$24.91M` across the 5-session window
(2026-05-13 → 2026-05-19). Single-day ask-side call sweeps cluster at the
$160 and $170 strikes in the front-end (5/22, 5/29, 6/05) and at $170/$180
in 8/21. Bearish prints exist but are smaller and read as hedging or
put-writing (bid-side 8/21 175P) rather than directional shorts.
Underlying tape price oscillated $157.0 – $160.6 intraday on 2026-05-18.

## Key signals

- RDDT in TOP sweep tickers on **5 of 5** recent sessions, $24.91M cumulative
  bullish sweep premium, consistency 1.0 [FLOW:hot_chains_sweep_persistence].
- Front-end call ladder ask-side sweeps: 5/22 160C $292k, 5/22 165C $187k,
  5/22 170C $251k, 5/29 160C $317k (vol/OI 3.48), 6/05 160C ask+bid
  ~$326k combined [FLOW:options_flow_sweeps + unusual_volume].
- Aug-21 two-sided commitment: 170C ask-side $356k + 175P **bid-side**
  $395k (put-sale = bullish commitment to own at ~$143.60 breakeven)
  [FLOW:options_flow_sweeps].
- Largest single print: 10/16 **110C** mid-side, premium $229,000, delta
  0.84, size 40 (deep-ITM long call ≈ stock surrogate) [FLOW:top_premium_trades].
- IV outliers are tiny weekly 5/22 wing-strike calls (230C IV 173%, 192.5C
  IV 129%) — lottery-ticket speculation, not directional conviction
  [FLOW:options_flow_iv_outliers].

## Detailed findings

### Sweeps — ask vs bid concentration

Top aggressive sweeps by premium ($100k+ floor), `date=2026-05-18`:

| Side | OT | Expiry | Strike | Trades | Size | Premium |
|------|----|--------|--------|--------|------|---------|
| bid  | put  | 2026-08-21 | 175 | 5   | 125  | $395,350 |
| ask  | put  | 2026-06-18 | 140 | 110 | 898  | $380,384 |
| ask  | call | 2026-08-21 | 170 | 6   | 184  | $355,935 |
| ask  | call | 2026-05-29 | 160 | 71  | 536  | $316,679 |
| ask  | call | 2026-05-22 | 160 | 163 | 771  | $291,808 |
| ask  | call | 2026-05-22 | 170 | 262 | 1632 | $250,536 |
| ask  | put  | 2028-06-16 | 120 | 35  | 77   | $245,518 |
| bid  | call | 2026-05-22 | 160 | 153 | 610  | $240,984 |
| bid  | call | 2026-06-05 | 160 | 11  | 248  | $230,586 |
| mid  | call | 2026-10-16 | 110 | 1   | 40   | $229,000 |
| bid  | call | 2026-07-17 | 170 | 24  | 198  | $226,753 |
| ask  | call | 2026-08-21 | 180 | 14  | 135  | $210,541 |
| bid  | call | 2026-08-21 | 170 | 11  | 107  | $203,569 |

Read: ask-side calls dominate gross premium across the front-end and 8/21.
Two notable contrarian prints: (a) 8/21 175P **bid-side $395k** — read as
put-write (synthetic-long bullish, breakeven ~$143.60); (b) 6/18 **140P
ask-side $380k** — OTM put buying = downside hedge or contained bearish bet
(140 is ~12% below spot). Net call-vs-put ask-side premium ≈
**call $1.96M vs put $0.78M ≈ 2.5:1 bullish**, ignoring the put-write.

### New positioning (vol >> OI)

| Expiry | OT | Strike | OI | Vol | Vol/OI | Premium | IV |
|--------|----|--------|----|----|--------|---------|-----|
| 2026-11-20 | put  | 105 | 1  | 141 | 141.0 | $107,811 | 71.7% |
| 2026-08-21 | put  | 90  | 73 | 334 | 4.58  | $43,194  | 74.1% |
| 2026-05-29 | call | 160 | 164| 571 | 3.48  | $339,080 | 66.4% |
| 2026-08-21 | put  | 175 | 41 | 127 | 3.10  | $401,595 | 66.1% |

Read: most fresh-positioning premium is in the 5/29 160C ($339k) and the
8/21 175P ($401k). The 11/20 105P is a tiny but structurally interesting
deep-OTM tail bet (~30% below spot). The 8/21 90P is a far-OTM disaster
hedge — $43k, not material.

### Largest premium prints (top 10 by $)

| Time (UTC) | Expiry | OT | Strike | Side | Size | Premium | Delta | Underlying |
|---|---|---|---|---|---|---|---|---|
| 19:52:46 | 2026-10-16 | call | 110 | mid | 40  | $229,000 | 0.84 | 158.95 |
| 17:29:43 | 2026-08-21 | put  | 175 | bid | 50  | $157,000 | -0.55| 158.40 |
| 16:55:51 | 2026-08-21 | put  | 175 | bid | 46  | $146,280 | -0.56| 157.61 |
| 14:17:42 | 2026-08-21 | call | 170 | ask | 75  | $145,125 | 0.51 | 160.50 |
| 14:17:42 | 2026-08-21 | call | 170 | ask | 75  | $145,125 | 0.51 | 160.50 |
| 13:30:03 | 2026-10-16 | call | 155 | ask | 50  | $144,250 | 0.61 | 158.55 |
| 14:17:46 | 2026-08-21 | call | 170 | bid | 70  | $135,450 | 0.51 | 160.30 |
| 14:17:46 | 2026-06-05 | call | 160 | bid | 100 | $95,700  | 0.53 | 160.30 |
| 14:24:58 | 2026-06-05 | call | 160 | bid | 100 | $95,200  | 0.54 | 160.46 |
| 13:58:15 | 2026-07-17 | call | 175 | bid | 100 | $94,000  | 0.39 | 158.10 |

Read: late-day 10/16 110C $229k mid-print at delta 0.84 is the single biggest
bet — high-delta long call ≈ stock surrogate with ~$110 effective entry.
13:30 and 14:17 are two timestamps where multiple large bullish lots cross
simultaneously, suggesting a coordinated institutional sweep.

### IV outliers + Greeks

- IV outliers are confined to tiny 5/22 wing calls (230C IV 173%, $662
  premium; 192.5C IV 129%, $3k premium). These are lottery-ticket tape
  noise, **not** a vol-spike signal.
- Greek screener (sort by premium) confirms long-call concentration: top
  positive-delta prints sit at 0.50–0.84 delta (directional), with gamma
  highest on 6/05 160C (0.017) — short-dated ATM = squeeze fuel if spot
  pushes through 160. Highest vega in 11/20 180C (0.45) — vol-sensitive
  long-dated upside.

### Smart-money flow (market-wide, RDDT-filtered)

- `hot_chains_smart_money_flow direction=bullish top_n=50 min_volume=500`:
  RDDT does NOT appear in the top-50 (dominated by VIX, SPXW, SPY, IWM,
  NVDA, TSLA mass-volume names). This is a normalization-of-scale issue,
  not absence of bullish flow.
- `hot_chains_sweep_ratio top_n=50 min_volume=500 min_sweep_ratio=0.3`:
  RDDT does NOT appear in the top-50. Same scale issue.
- The persistence tool (which is symbol-aware) is the dispositive read.

### Sweep persistence (5-session)

```
ticker: RDDT
sessions_in_top: 5
consistency_score: 1.0
dominant_direction: bullish
total_sweep_premium: $24,910,332
dates_covered: 2026-05-13, 2026-05-14, 2026-05-15, 2026-05-18, 2026-05-19
```

Read: RDDT was a top sweep ticker every single trading session over the
window, with cumulative bullish sweep premium near **$25M**. This is rare
and is the highest-quality flow signal in the dataset.

Note: `dates_covered` extends to 2026-05-19, which is one session past the
2026-05-18 parquet cutoff used everywhere else. Persistence tool reads
from a different live source; flagging the date discrepancy here for the
audit phase.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__options_flow_sweeps` | symbol=RDDT, date=2026-05-18, min_premium=100000, top_n=25 | 25 rows; ask-side call dominance |
| `mcp__uw-pp__options_flow_unusual_volume` | symbol=RDDT, date=2026-05-18, min_vol_oi_ratio=3, top_n=25 | 4 rows |
| `mcp__uw-pp__options_flow_top_premium_trades` | symbol=RDDT, date=2026-05-18, top_n=25 | 25 rows; 10/16 110C top print |
| `mcp__uw-pp__options_flow_iv_outliers` | symbol=RDDT, date=2026-05-18, top_n=15 | 2 rows (wing-strike weeklies) |
| `mcp__uw-pp__options_flow_greek_screener` | symbol=RDDT, date=2026-05-18, top_n=15, sort_by=premium | 15 rows; confirms directional long-call cluster |
| `mcp__uw-pp__hot_chains_smart_money_flow` | direction=bullish, date=2026-05-18, top_n=50, min_volume=500 | RDDT absent (mass-volume dominated) |
| `mcp__uw-pp__hot_chains_smart_money_flow` | direction=bearish, date=2026-05-18, top_n=50, min_volume=500 | RDDT absent |
| `mcp__uw-pp__hot_chains_sweep_persistence` | symbol=RDDT, days=5, top_n=20 | RDDT 5/5 sessions, $24.9M, bullish |
| `mcp__uw-pp__hot_chains_sweep_ratio` | date=2026-05-18, top_n=50, min_volume=500, min_sweep_ratio=0.3 | RDDT absent (scale) |

## Tool errors

None on Phase 1 calls.

## Verdict for downstream phases

- **Bias from this phase:** bullish
- **Conviction:** 4 / 5 (persistence + size + multi-strike confirmation)
- **Three things later phases should remember:**
  1. RDDT consistency_score 1.0, 5/5 sessions, $24.91M bullish sweep premium
     [FLOW:hot_chains_sweep_persistence]. This is the single strongest
     signal in the workup so far.
  2. Front-end call gamma magnet at **$160** spans 5/22, 5/29, 6/05 with
     ~$850k+ ask-side call sweep premium; spot already sitting on the
     magnet (158.4–160.6 intraday 5/18).
  3. Aug-21 two-sided bullish commitment: 170C ask + 175P bid-side =
     >$1M premium net-bullish; long-vol upside + put-write downside
     cushion to ~$143.60.
- **Open questions:**
  - Does dark pool tape confirm accumulation under the bullish sweep flow,
    or is the spot held up by retail demand alone? (phase 2)
  - Is there an earnings/catalyst inside the 8/21 window that explains the
    long-dated bullish commitment? (phase 6)
  - Does positioning OI show that the 160C call ladder is fresh sell-side
    supply being absorbed, or is the dealer short calls into a squeeze
    setup? (phase 3 + 4)
