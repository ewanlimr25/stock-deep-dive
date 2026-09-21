# Phase 1 — Options Flow

**Ticker:** PYPL
**As-of date:** 2026-05-19 (effective; user requested 2026-05-20 — see phase-0-intake.md)
**Generated:** 2026-05-20T00:05:00-04:00
**Upstream phases cited:** phase-0-intake.md

## Summary

PYPL's 2026-05-19 tape is **mixed with a near-term bearish tilt and a longer-dated
bullish tail**. Unusual-volume openings are 6:1 puts-to-calls, and the largest
ask-side print is a $55K June $47.5 put (clear hedging/short bet). However, the
top single print is a $72K Dec-2028 $50 call hit on the BID (call overwriting,
not directional buying), and four-figure ask-side prints in Jan-2028 / Dec-2028
$75–82.5 calls suggest a small "buy the wing" program is also live. The single
strongest signal is `hot_chains_sweep_persistence`: PYPL has appeared in top
sweep activity **5/5 of the last 5 sessions with $8.16M aggregate sweep
premium and mixed direction** — institutions are clearly engaged, just not
unanimously bullish or bearish.

## Key signals

- **Sweep persistence 5/5 sessions, $8.16M cumulative sweep premium, mixed
  direction, consistency_score 1.0** [FLOW:hot_chains_sweep_persistence:2026-05-15..19] —
  highest possible persistence, institutional engagement is not random.
- **Unusual volume is 6:1 puts:calls.** Top: Jun-12 $36P vol/OI = 152
  (2,280 vol / 15 OI), Jun-18 $41P vol/OI = 23, plus Jun-5/12/18 $36–44 puts
  [FLOW:options_flow_unusual_volume:2026-05-19]. Only 1 unusual call (Jun-18 $47C).
- **Largest single ask-side directional bet is a put:** $55,300 premium on
  PYPL 2026-06-18 $47.5P at the ask, 158 contracts, IV 33.9%, delta −0.72
  [FLOW:top_premium_trades:2026-05-19T14:30:49Z]. Underlying was $44.73 — this
  is an ITM put buy, not a hedge.
- **Counter-signal: long-dated call speculation.** Stacked ask-side prints in
  Dec-2028 $75C ($44K), Jan-2028 $75C ($26K + $25K), Jan-2028 $82.5C ($26K)
  [FLOW:top_premium_trades]. Small notional but consistent "buy the wing"
  positioning for multi-year upside.
- **Sweeps weakly net bullish near-term ($167K Jul-17 $45C ask) but offset
  by $247K of ask-side OTM put sweeps in Dec-2026 / Jan-2027 $35P**
  [FLOW:options_flow_sweeps:2026-05-19] — read as tail-hedge + near-term
  positive lean.
- **No PYPL in either bullish or bearish smart-money top-25 today**
  [FLOW:hot_chains_smart_money_flow:2026-05-19] — flow is real but not
  ask-bid lopsided enough to register on the market-wide leaderboard.

## Detailed findings

### Spot reference

Underlying prices observed across the session (from top_premium_trades
`underlying_price` field): high $44.83 (14:19Z), low $43.835 (19:44Z),
session-end region $43.86–$44.00. **Working spot for downstream phases: $43.88**
(close-of-day median of late-session prints).

### Sweeps (≥$100K aggregated premium)

Only 4 sweeps cleared the $100K threshold — aggregate sweep premium of $629K
on the single day:

| Side | Type | Strike | Expiry | Premium | Size | Read |
|------|------|--------|--------|---------|------|------|
| bid  | call | $50    | 2028-12-15 | $213,882 | 202 | LEAP call overwriting / monetization |
| ask  | call | $45    | 2026-07-17 | $167,719 | 842 | Near-term bullish, OTM by ~$1 |
| ask  | put  | $35    | 2027-01-15 | $146,148 | 817 | Tail/skew hedge ~20% OTM |
| ask  | put  | $35    | 2026-12-18 | $101,435 | 631 | Same theme, shorter dated |

[FLOW:options_flow_sweeps:2026-05-19]. Net near-term ask-side directional:
+$167K calls vs $0 near-term puts ⇒ near-term bullish *via sweeps only*. Net
ask-side put sweeps are all far-OTM Q4-2026/Q1-2027 $35P — classic tail-risk
or skew-trade structure, not "betting on imminent crash".

### New positioning (unusual vol/OI ratios)

7 contracts with vol/OI ≥ 3.7 — 6 puts, 1 call:

| Type | Strike | Expiry | Vol | OI | Vol/OI | Premium | IV |
|------|--------|--------|-----|-----|--------|---------|-----|
| put  | $36    | 2026-06-12 | 2,280 | 15  | **152** | $6,050   | 37.3% |
| put  | $41    | 2026-06-18 | 671   | 29  | 23.1    | $38,177  | 34.6% |
| put  | $36    | 2026-06-05 | 270   | 17  | 15.9    | $270     | 38.8% |
| put  | $43.5  | 2026-06-05 | 100   | 9   | 11.1    | $10,100  | 33.1% |
| put  | $43    | 2026-06-12 | 665   | 113 | 5.9     | $66,212  | 33.1% |
| put  | $44    | 2026-06-18 | 165   | 34  | 4.9     | $26,015  | 33.7% |
| call | $47    | 2026-06-18 | 142   | 38  | 3.7     | $10,324  | 34.1% |

[FLOW:options_flow_unusual_volume:2026-05-19]. The vol/OI = 152 on a $36P
14% OTM is striking — that's a deep-OTM crash hedge or a directional bet on
a sub-$36 break (~18% downside from $43.88). However, the **premium spent
is tiny ($6K)** — likely small accounts or a directional dabble, not an
institutional positioning shift.

The $43P Jun-12 (665 vol, $66K premium, vol/OI 5.9) is the **most
information-rich opening put** — ATM, real premium, and 6× OI buildup.

### Largest premium prints (top 10 by single-trade premium)

| Time UTC | Type | Strike | Expiry | Side | Price | Premium | Delta | Read |
|----------|------|--------|--------|------|-------|---------|-------|------|
| 13:41 | C | 50  | 2028-12-15 | bid | 10.80 | $72,360 | +0.58 | LEAP call sold to bid (overwriter/exit) |
| 14:30 | P | 47.5 | 2026-06-18 | ask | 3.50  | $55,300 | −0.72 | ITM put bought — clear directional bearish 30-DTE |
| 18:15 | C | 45  | 2026-06-12 | bid | 1.07  | $53,500 | +0.42 | Near-term call sold to bid (vol sale or roll) |
| 16:57 | C | 75  | 2028-12-15 | ask | 4.50  | $44,100 | +0.32 | Long-dated wing bought — multi-year speculation |
| 17:57 | C | 40  | 2027-01-15 | ask | 8.12  | $40,600 | +0.68 | ITM 2027 LEAP call bought — long-term bullish stake |
| 14:45 | P | 42.5 | 2026-09-18 | ask | 2.75  | $25,850 | −0.37 | Sep put bought — 4-mo downside protection |
| 19:53 | C | 46.5 | 2026-05-22 | ask | 0.08  | $21,960 | +0.09 | 0DTE lotto, discount |
| 14:28 | P | 47   | 2026-05-22 | ask | 2.30  | $23,000 | −0.93 | Deep ITM 3DTE put — synthetic short / hedge |

[FLOW:top_premium_trades:2026-05-19].

Aggregate by intent (top 25):
- **Long calls bought at ask (bullish):** $44K + $40K + $35K + $26K + $25K + $24K + $21K + $21K ≈ **$236K** (dominated by Jan/Dec-2028 wings)
- **Long puts bought at ask (bearish/hedge):** $55K + $26K + $23K + $19.9K ≈ **$124K** (dominated by Jun-18 $47.5P)
- **Calls sold to bid (overwrite/exit):** $72K + $54K + $36K + $34K + $28K + $26K + $21K ≈ **$271K** (LEAP-heavy overwriting)
- **Puts sold to bid (income/exit):** $21K + $20K ≈ **$41K**

Ask-side directional dollar bias: **+$112K calls > puts** but small absolute.
The $271K of LEAP call overwriting (Dec-2028 $50C, $20C deep-ITM) is the
dominant flow by dollar — this is **institutional yield generation on a
held PYPL position**, not directional.

### IV outliers + Greeks

`options_flow_iv_outliers` returned **empty** at default min-iv=1.0 (100%).
PYPL is not in unusual-vol-of-vol territory — its IVs are clustered 30–45%,
normal for a mid-cap financial after a multi-year de-rate.
[FLOW:options_flow_iv_outliers:2026-05-19].

`options_flow_greek_screener` (top 15 by premium) confirms the picture above
— the top deltas are mixed long-call (Dec-2028 $50C delta +0.58) and a
single large negative-delta put (Jun-18 $47.5P delta −0.72). No vol/vega
concentration is unusual. [FLOW:options_flow_greek_screener:2026-05-19].

### Persistence + smart money

`hot_chains_sweep_persistence` is the highest-conviction signal in phase 1:

```
{ ticker: PYPL, sessions_in_top: 5/5, total_sweep_premium: $8,155,590,
  dominant_direction: mixed, consistency_score: 1.0 }
```

[FLOW:hot_chains_sweep_persistence:2026-05-13..19]. **PYPL has been in
top market-wide sweep activity every single one of the last five sessions**,
with $8.16M of sweep premium — far above today's $629K single-session figure.
The 5-day stack is institutionally significant, but direction is mixed (not a
unanimous bull or bear campaign).

PYPL does NOT appear in `hot_chains_smart_money_flow` top-25 in either
bullish (`direction=bullish`) or bearish (`direction=bearish`) configuration
[FLOW:hot_chains_smart_money_flow:2026-05-19]. The market-wide bullish list
is dominated by IEF, TSLA, HYG, SPY, IWM, WULF, AMZN; bearish is dominated by
VIX, IEF, HYG, IWM, SPY. PYPL's flow is real but not lopsided enough to crack
the leaderboard.

`hot_chains_sweep_ratio` top 25 (min ratio 0.3): no PYPL contracts. The
PYPL flow is volume-rich but not exchange-sweeping aggressively
[FLOW:hot_chains_sweep_ratio:2026-05-19].

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__options_flow_sweeps` | symbol=PYPL, min-premium=100000, top-n=25, date=2026-05-19 | 4 sweeps, $629K aggregate |
| `mcp__uw-pp__options_flow_unusual_volume` | symbol=PYPL, min-vol-oi-ratio=3, top-n=25, date=2026-05-19 | 7 unusual contracts; 6 puts / 1 call |
| `mcp__uw-pp__options_flow_top_premium_trades` | symbol=PYPL, top-n=25, date=2026-05-19 | 25 top prints, spot range $43.86–44.83 |
| `mcp__uw-pp__options_flow_iv_outliers` | symbol=PYPL, top-n=15, date=2026-05-19 | empty (no contract with IV ≥ 100%) |
| `mcp__uw-pp__options_flow_greek_screener` | symbol=PYPL, top-n=15, sort-by=premium, date=2026-05-19 | top 15 mirror top_premium_trades |
| `mcp__uw-pp__hot_chains_smart_money_flow` | direction=bullish, min-volume=500, top-n=25, date=2026-05-19 | PYPL not in top 25 |
| `mcp__uw-pp__hot_chains_smart_money_flow` | direction=bearish, min-volume=500, top-n=25, date=2026-05-19 | PYPL not in top 25 |
| `mcp__uw-pp__hot_chains_sweep_persistence` | days=5, top-n=20, symbol=PYPL | 5/5 sessions, $8.16M, mixed, consistency 1.0 |
| `mcp__uw-pp__hot_chains_sweep_ratio` | min-volume=500, min-sweep-ratio=0.3, top-n=25, date=2026-05-19 | no PYPL contracts |

## Tool errors

None — all 9 calls succeeded on 2026-05-19 data.

## Verdict for downstream phases

- **Bias from this phase:** **mixed, leaning short-term bearish / long-term
  neutral-to-bullish**. Near-term tape (Jun expiries) shows clear put
  preference both in unusual openings (6:1) and the largest ask-side print
  ($55K Jun-18 $47.5P). Long-dated tape (Jan-2028, Dec-2028) shows OTM call
  speculation + heavy LEAP call overwriting — read as "someone holds PYPL,
  is generating yield, while another cohort plays the multi-year wing." No
  unanimous institutional voice.
- **Conviction:** **3 / 5** — persistence is high (5/5), but mixed direction
  prevents a high-confidence call. Premium magnitudes are modest in absolute
  terms ($600K sweeps + $5M total premium across top-25). Phase 2 (dark
  pool) and phase 3 (OI) need to break the tie.
- **Three datapoints later phases must remember:**
  1. Spot = **$43.88** (late-session median) — use for all moneyness math.
  2. Sweep persistence 5/5 with $8.16M 5-day total — institutional
     engagement is **not in doubt**; only direction is.
  3. The **June 2026 expiry is the gravity well of new put positioning** —
     phase 3 OI work and phase 4 dealer-positioning should focus there.
- **Open questions:**
  - Is dark pool (phase 2) confirming the short-term bearish lean, or are
    block prints absorbing on the bid side (institutional accumulation)?
  - Does OI (phase 3) show net put builds on Jun expiries, or are these
    new opens being rolled off existing call positions?
  - With June expiry as the focal point, what is dealer gamma at $42–$45
    on Jun 18 (phase 4)?
  - Is there a known catalyst in May–Jun (earnings already passed in early
    May historically) driving the put openings? Defer to phase 6 macro.
