# Phase 1 — Options Flow

**Ticker:** PATH (UiPath Inc.)
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T00:00:00Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md

## Summary

PATH's tape is **mixed-to-mildly-bearish with a hedging signature into the 05-28
earnings event**, not a directional accumulation. The whole-tape aggregate is net-bearish
(net_flow **−$399K**) even though call *volume* dwarfs put volume (P/C 0.31) — because the
call volume is short-dated 05-29 lottery tickets and bid-side (sold) calls, while the
largest, most capital-committed prints are **puts**. The single biggest print of the day
is a **$525,780 2027-03-19 $10 put**, and PATH has now appeared in the top sweep tape
**every one of the last 5 sessions with a bearish dominant direction** (consistency 1.0,
$6.01M). Per phase-0.5 (`unusual_verdict = BUSY_NAME_NORMAL_DAY`), magnitude is discounted
and this phase's downstream conviction is **capped at `+`**.

## Key signals

- **5-session bearish sweep persistence:** PATH in top sweeps all 5 sessions, `consistency_score=1.0`, `dominant_direction=bearish`, `total_sweep_premium=$6,011,150` [FLOW:sweep_persistence]
- **Largest print = a put:** $525,780 2027-03-19 **$10 put**, size 2286, IV 74.6%, delta −0.315, `side=no_side`, ≈10% of the day's total premium in one ticket [FLOW:top_premium_trades]
- **ATM June put hedging cluster:** 2026-06-18 $11 puts traded ~1,347 contracts in a 16:47 block (mid-heavy), + a $207,675 mid-side $11 June put sweep — protective positioning straddling spot ($10.99) into earnings [FLOW:sweeps]
- **Whole-tape:** call_premium $3.42M vs put_premium $1.54M but **bullish $1.65M < bearish $2.05M** → net_flow −$399K; call_volume 53,118 vs put_volume 16,464 [FLOW:insights_deep_dive]
- **Calls are lottery/sold:** ask-side calls concentrate in 0DTE $10 (pin) and 05-29 OTM (13/12/11.5); the larger-size call prints (Aug $12, 2028 $10/$20) are **bid-side** = written, not bought [FLOW:sweeps]

## Detailed findings

### Whole-tape aggregate (read the top-N against this)

From `insights_deep_dive.uw_screener` (the same screener data phase-0.5 used):
| Metric | Value |
|--------|-------|
| call_premium | $3,417,150 |
| put_premium | $1,540,712 |
| bullish_premium | $1,649,236 |
| bearish_premium | $2,048,170 |
| **net_flow** | **−$398,934 (bearish)** |
| call_volume / put_volume | 53,118 / 16,464 (P/C 0.31) |
| total_open_interest | 689,415 |

The tape is **call-heavy by volume but net-bearish by premium**. The resolution: the call
volume is dominated by cheap short-dated 05-29 lottery contracts and bid-side (sold) call
writing, so it carries little directional premium; the put side carries the capital. This
is the classic pre-earnings *hedging / mild-bearish* fingerprint, consistent with
phase-0.5's net-direction bottom-4%-of-universe read. **Spot ≈ $10.99** (confirmed from
print `underlying_price`).

### Sweeps (ask vs bid, premium, persistence)

| Strike / Expiry | Type | Side | Premium | Size | Read |
|---|---|---|---|---|---|
| $10 2027-03-19 | put | no_side | $525,780 | 2286 | Dominant print; long-dated, slightly-OTM, unclassified aggressor |
| $11 2026-06-18 | put | mid | $207,675 | 1790 | ATM post-earnings put — hedge |
| $10 2026-05-22 | call | ask | $142,685 | 1553 | **0DTE** — pin/gamma at $10, discount |
| $12 2026-08-21 | call | bid | $131,597 | 1002 | Call **written** (sold) |
| $10 2028-01-21 | call | bid | $118,936 | 249 | LEAP call **written** |
| $11.5 2026-05-29 | call | bid | $104,458 | 1817 | Earnings-week call, bid-side |
| $11 2026-06-18 | put | bid | $94,092 | 816 | More June put |
| $15 2027-01-15 | call | ask | $75,878 | 447 | One genuine OTM long call (bought ask) |

**Persistence (the strongest single read):** `sweep_persistence` over 2026-05-18→05-22
returns PATH alone with `sessions_in_top=5`, `consistency_score=1.0`,
`dominant_direction=bearish`, `total_sweep_premium=$6,011,150`. A 5-day bearish sweep
campaign is a real, repeated footprint — not a one-day artifact — and it corroborates the
fading net-direction trail in phase-0.5 (05-21 −$185K, 05-22 −$399K).

### New positioning (unusual vol, vol/OI ratio)

Only 4 contracts clear vol/OI ≥ 3: the 05-29 $17 call (lottery, vol 801/OI 82), the
**2027-03-19 $10 put (vol 2289 / OI 343, $526K premium)** — i.e. the dominant print is a
genuinely *new* position, not OI recycling — plus a 07-17 $16 call (493) and 06-05 $13.5
call (121). New money is opening the long-dated $10 put; the rest is small lottery.

### Largest premium prints + Greeks

The $526K 2027 $10 put dominates vega-notional (vega 0.0355 × 2286). The 2028 $20 LEAP
calls ($58K+$44K, mid/bid) and 2028 $30 ITM put ($60K ask, delta −0.83 — possible
synthetic-short leg) are the long-dated structural prints. Near-money gamma sits in the
06-18 $11 puts (gamma 0.136). Nothing here reads as aggressive directional **call buying**;
the conviction capital is in puts and vol.

### IV outliers + smart-money

05-29 weekly calls print IV 130–155% (earnings vol ramp); June $11 puts ~97%; 0DTE $10
calls show a nonsensical max_iv (24.8 — expiry-day blowup, ignored). Market-wide
`smart_money_flow direction=bullish` top-10 is SMH/GLD/TSLA/TLT/ACHR — **no PATH bullish
smart-money flow detected** in the top rows, consistent with PATH not being a bullish
leader today.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__insights_deep_dive` | `{symbol: PATH, date: 2026-05-22}` | Whole-tape: net_flow −$399K, P/C 0.31, call prem $3.42M / put prem $1.54M |
| `mcp__uw-pp__options_flow_sweeps` | `{symbol: PATH, min_premium: 25000, top_n: 25}` | Largest = $526K 2027 $10 put; ATM June puts; calls bid-side/0DTE |
| `mcp__uw-pp__options_flow_top_premium_trades` | `{symbol: PATH, top_n: 25}` | #1 = $525,780 2027 $10 put; puts dominate top capital |
| `mcp__uw-pp__options_flow_unusual_volume` | `{symbol: PATH, min_vol_oi_ratio: 3, top_n: 25}` | New money in 2027 $10 put (vol 2289/OI 343); rest lottery |
| `mcp__uw-pp__options_flow_iv_outliers` | `{symbol: PATH, top_n: 15}` | 05-29 calls IV 130–155%; June $11 puts ~97% — earnings ramp |
| `mcp__uw-pp__options_flow_greek_screener` | `{symbol: PATH, top_n: 15, sort_by: premium}` | Vega concentrated in long-dated $10 put + 2028 LEAPs |
| `mcp__uw-pp__hot_chains_smart_money_flow` | `{direction: bullish, min_volume: 300, top_n: 10}` | Market-wide; **no PATH** in top bullish rows |
| `mcp__uw-pp__hot_chains_sweep_persistence` | `{symbol: PATH, days: 5, top_n: 20}` | PATH 5/5 sessions, consistency 1.0, **bearish**, $6.01M |

## Tool errors

None. (`smart_money_flow` returned no PATH rows — recorded as a finding, not an error; not re-run at looser thresholds per phase guidance.)

## Verdict for downstream

- **Net bias from this phase:** **mildly bearish / hedging-dominant** (mixed, with the
  capital-committed prints and the 5-day sweep campaign both leaning bearish).
- **Conviction:** **2/5** — capped by phase-0.5 BUSY_NAME_NORMAL_DAY; much of the put flow
  is plausibly pre-earnings hedging rather than outright directional conviction, and the
  largest print is `no_side` (unclassified). The *persistence* of the bearish sweeps is
  what keeps this from being neutral.
- **Three things later phases must remember:**
  1. **5-session bearish sweep persistence** (consistency 1.0, $6.01M) — the most durable
     flow signal; this is a campaign, not a print.
  2. **The conviction capital is in puts:** $526K 2027 $10 put (largest print, new money)
     + ATM June $11 put hedging cluster; calls are 05-29 lottery or bid-side/written.
  3. **Net_flow −$399K bearish despite P/C 0.31** — do not misread call-heavy *volume* as
     bullish; it's cheap short-dated/sold call activity.
- **Open questions:**
  - Is the dark pool **confirming distribution** (bearish) or **absorbing supply**
    (accumulation under the tape)? → phase-2.
  - Is the long-dated $10 put an outright bearish bet or a **hedge against a long /
    spread leg**? → phase-3 OI + phase-2 DP.
  - All of this is into a 6-day-out earnings print — how much is *event hedging* vs
    *thesis*? → phase-7b/7c.
