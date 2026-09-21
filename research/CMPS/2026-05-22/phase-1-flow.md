# Phase 1 — Options Flow

**Ticker:** CMPS
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T00:00:00Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md

## Summary

Today's tape is **call distribution, not call accumulation.** Gross call premium
($1.33M) dwarfs put premium ($0.10M), which superficially screams bullish — but the
aggressor split is the opposite: **bid-side call premium ($580.8k) is ~2× ask-side
($291.9k)**, i.e. calls are being net **SOLD** (`net_call_premium −$288.9k`,
`net_flow −$275.6k`). The marquee print phase-0 flagged — the Jul $13 call at vol/OI
12.78, $735k premium — is **1,632 contracts hit on the bid (sold) vs only 629 lifted
on the ask (bought)**, plus a 1,000-lot mid/no_side block. Same signature at Jun $11
(1,173 sold vs 164 bought). After a +26% eight-session run (phase-0.5), this reads as
**profit-taking / covered-call overwriting capping upside**, not bullish initiation —
a soft-bearish-to-mixed tape. Puts are negligible and slightly net-sold, so this is
*not* aggressive downside positioning either.

## Key signals

- Whole-tape aggressor split: **bid-side calls $580.8k vs ask-side $291.9k (~2:1 SOLD)**, 3,398 contracts sold vs 1,591 bought `[FLOW:aggressor_ex0dte DUCKDB]`.
- Marquee Jul $13 call: $735k premium, **vol/OI 12.78**, but 1,632 sold (bid) / 629 bought (ask) + 1,000-lot mid block → net **call selling** `[FLOW:unusual_volume]` `[FLOW:sweeps]`.
- Whole-tape: `bullish_premium $330k` vs `bearish_premium $606k`, `net_flow −$275.6k`; P/C ratio **0.129** (call-heavy by volume but bid-driven) `[FLOW:insights_deep_dive]`.
- Sweep persistence: CMPS in top sweeps **4 of 5 sessions** ($840.8k total), `dominant_direction = MIXED` — a real multi-day campaign that flipped bullish→bearish into today `[FLOW:sweep_persistence]`.
- All flow is **8–180 DTE** (Jun/Jul/Aug + a few LEAPs); **zero 0DTE** — the aggregate is clean, no pin-noise inflation `[FLOW:dte_bucket DUCKDB]`.

## Detailed findings

### Whole-tape aggregate (read top-N against this) `[FLOW:insights_deep_dive]`

| Field | Value |
|-------|-------|
| call_premium | $1,326,507 |
| put_premium | $100,519 |
| bullish_premium | $330,105 |
| bearish_premium | $605,686 |
| **net_flow (bull−bear)** | **−$275,581** |
| net_call_premium | −$288,917 |
| net_put_premium | −$13,335 |
| call_volume / put_volume | 7,809 / 1,007 |
| put_call_ratio | 0.129 |

The gross call premium is real, but the *aggressor* classification (which side took
liquidity) is net bearish. High call volume + negative net_call_premium = calls
sold-into. Carrying phase-0.5: `unusual_verdict = GENUINELY_UNUSUAL (bearish-tilted)`,
86.7th-pctile premium but bottom-5% net-direction — so this is a genuine signal day,
and the signal is **distribution**.

### Whole-tape aggressor split (DuckDB §A) `[FLOW:aggressor_ex0dte DUCKDB]`

Premium and contracts by option_type × aggressor side (ex 0–1DTE; there is none here):

| type | side | trades | contracts | premium |
|------|------|--------|-----------|---------|
| call | ask (bought) | 244 | 1,591 | $291.9k |
| call | **bid (sold)** | 222 | **3,398** | **$580.8k** |
| call | mid | 221 | 1,820 | $303.8k |
| call | no_side (block) | 1 | 1,000 | $150.0k |
| put | ask (bought) | 23 | 176 | $24.9k |
| put | bid (sold) | 28 | 424 | $38.2k |
| put | mid | 18 | 407 | $37.5k |

**Call bid:ask premium ≈ 2:1 in favour of selling.** Puts are immaterial (~$100k
total, marginally net-sold). This is the cleanest single read of the day: the move is
in calls, and the calls are being sold.

### New positioning (unusual vol, vol/OI) `[FLOW:unusual_volume]` + OI changes `[OI:deep_dive]`

- Only one contract clears vol/OI ≥ 3: **Jul $13 call**, vol 4,894 / OI 383 = **12.78×**, $735k premium, avg IV 103%. New activity — but per the sweep/aggressor split, predominantly sold-to (bid 1,632 vs ask 629).
- `insights_deep_dive` top OI *increases* (yesterday→today) are **puts**, small premium:
  Jun $10 put +2,191 OI (avg $0.32), Jun $11 put +2,139 OI (avg $0.70), then Jul $12
  call +1,962 OI (avg $1.54). → fresh **downside** OI building at $10/$11 (protective
  or initiating; cheap), alongside the $12–13 call churn. Phase 3 must confirm whether
  the $13-call OI itself rose (sold-to-open overwrite) or fell (longs closing).

### Largest premium prints `[FLOW:top_premium_trades]`

| time (Z) | contract | premium | side | read |
|----------|----------|---------|------|------|
| 15:46 | Jul $13 C ×1,000 @1.50 | $150.0k | no_side | mid block / cross — ambiguous |
| 14:11 | Jun $11 C ×500 @1.55 | $77.5k | **bid** | sold |
| 15:25 | Jul $13 C ×503 @1.50 | $75.5k | **bid** | sold |
| 15:00 | Jun $11 C ×436 @1.55 | $67.6k | **bid** | sold |
| 15:25 | Jul $13 C ×266 @1.50 | $39.9k | **bid** | sold |
| 13:30 | Jan'28 $7 C ×48 @6.87 | $33.0k | bid | deep-ITM LEAP, sold (tiny) |
| 14:08 | Aug $9 C ×69 @4.12 | $28.4k | **ask** | bought (only sizable ask print) |

Five of the top seven prints are **bid-side call sales**. The lone meaningful ask-side
buy is a tiny 69-lot Aug $9 call. The 1,000-lot mid block is the only large ambiguous
print — consistent with a negotiated overwrite/roll rather than a directional buy.

### IV outliers + Greeks `[FLOW:iv_outliers]` `[FLOW:greek_screener]`

- Highest IV sits in the **far-OTM wings**: Aug $7 call 123%, Aug $7 put 120%, Aug $6
  put 119% — classic binary-biotech tails. The traded Jul $13 call avg IV 103% (max
  132%) is elevated vs the ~75% ATM IV30d but is the contract being *sold* — i.e.
  someone is **selling rich vol**, consistent with the cheap headline IV rank (12.25).
- Greeks: Jul $13 call δ≈0.49 (slightly OTM, high-IV-fattened), Jun $11 call δ≈0.68–0.70.
  Flow is near-the-money, moderate gamma (0.08–0.14), low vega per contract — a
  directional/income tenor, not a vega/vol-event bet.

### Market-wide context

- CMPS does **not** appear in `hot_chains_smart_money_flow` top-25 (either direction) —
  the list is dominated by index/mega-cap (SMH, GLD, SPY, NVDA, TSLA). No smart-money
  flow detected for CMPS at the market-wide top-N on this date.
- CMPS not in `hot_chains_sweep_ratio` top-25 (dominated by sub-$0.50 contracts). Not a
  pure-sweep name today; the campaign is the multi-session one above.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__insights_deep_dive` | symbol=CMPS, date=2026-05-22 | Whole-tape: net_flow −$275.6k, call/put prem $1.33M/$0.10M |
| `mcp__uw-pp__options_flow_sweeps` | symbol=CMPS, min_premium=50k, top_n=25 | Jul $13 call bid $245k > ask $95k; Jun $11 bid $182k |
| `mcp__uw-pp__options_flow_unusual_volume` | symbol=CMPS, min_vol_oi=3 | 1 hit: Jul $13 call 12.78× |
| `mcp__uw-pp__options_flow_top_premium_trades` | symbol=CMPS, top_n=25 | 5 of top 7 = bid-side call sales |
| `mcp__uw-pp__options_flow_iv_outliers` | symbol=CMPS, top_n=15 | Wings 119–123% IV; Jul $13 call 103% |
| `mcp__uw-pp__options_flow_greek_screener` | symbol=CMPS, sort_by=premium | δ≈0.49–0.70, NTM, low vega |
| `mcp__uw-pp__hot_chains_sweep_persistence` | symbol=CMPS, days=5 | 4/5 sessions, $840.8k, MIXED direction |
| `mcp__uw-pp__hot_chains_smart_money_flow` | both, top_n=25, min_vol=500 | CMPS absent (small-cap) |
| `mcp__uw-pp__hot_chains_sweep_ratio` | top_n=25, min_sweep=0.3 | CMPS absent |
| DuckDB §A | All Options 2026-05-22 | Aggressor split: call bid $580.8k vs ask $291.9k |

## Tool errors

_None._ (Market-wide tools returning no CMPS rows is expected, not an error — noted inline.)

## Verdict for downstream phases

- **Net bias from this phase:** **bearish-to-mixed (soft bearish).** The directional
  intent is call selling/distribution after a hot run; it is not aggressive bearish
  initiation (puts are immaterial). Read it as "upside being capped / longs taking
  profit," a ceiling signal more than a floor-breaking one.
- **Conviction:** **3/5.** The aggressor split is clean and two-source-confirmed
  (MCP screener net_flow + DuckDB bid/ask split agree), but the *character* (passive
  bid-side selling + a mid block) is overwriting/profit-taking, which is lower-conviction
  bearish than ask-side put sweeps would be.
- **Three things later phases must remember:**
  1. The high call volume is **net SOLD** — bid-side call premium $580.8k vs ask $291.9k
     (~2:1). Do **not** carry "big call flow = bullish" forward. `net_flow −$275.6k`.
  2. The Jul $13 call (12.78× vol/OI, the headline) and Jun $11 call are the *sold*
     contracts; fresh **put** OI is building at Jun $10/$11 (cheap, possibly protective).
  3. There IS a 4/5-session sweep campaign ($840.8k) but it is **MIXED** and flipped
     bullish→bearish into today — momentum is rolling over, not extending.
- **Open questions for phases 2–4:**
  - Is the **dark pool** confirming distribution (sellers ≥ buyers at ~$12)? (phase 2)
  - Did the **$13-call OI rise** (sold-to-open overwrite/short) or **fall** (prior longs
    closing)? That distinguishes "income/cap" from "bullish thesis exited." (phase 3)
  - Where is **dealer gamma/GEX** — does call selling to dealers make them long gamma
    (mean-reverting, pins the move) above $11–12? (phase 4)
