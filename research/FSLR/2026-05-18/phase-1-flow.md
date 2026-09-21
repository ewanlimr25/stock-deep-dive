# Phase 1 — Options Flow

**Ticker:** FSLR
**As-of date:** 2026-05-18 (data anchor: 2026-05-15)
**Generated:** 2026-05-18T00:05:00Z
**Upstream phases cited:** phase-0-intake.md

## Summary

FSLR (spot ≈ $236.0) printed mixed-but-net-constructive flow on 2026-05-15:
~$3.0M of ask-side bullish call premium opens (highlighted by a $1.39M
single-print Mar-2027 280C at $34.75 ask, vol/OI = 10× on 48 OI) was paid for
alongside ~$1.27M of ask-side OTM put protection (220–230 strikes, May
expiries). Bid-side call activity ($1.6M on Jun-2026 250C, $496K on Jul-2026
270C, $378K on Jan-2028 400C) is large enough that some institutional desks
appear to be writing/closing rather than chasing — net flow tone is therefore
**mixed-bullish, conviction 3/5**, anchored by a credible long-dated ATM
LEAPS open. FSLR has been in the top sweep universe **5 of 5 sessions**
(persistence score 1.0, dominant direction "mixed", aggregate sweep premium
$35.4M) — institutions are working both sides, not panicking.

## Key signals

- $1.668M aggressed Mar-2027 280C **opens** at ask ($34.75 avg, Δ≈0.48,
  IV 57.5%, vol/OI = 10×) — biggest single conviction print of the day
  [FLOW:options_flow_sweeps][FLOW:options_flow_unusual_volume].
- Jun-2026 250C is being traded on **both sides** at the $10.20 print —
  $1.60M ask vs $1.62M bid — pointing to two-sided institutional repositioning
  rather than one-sided accumulation [FLOW:options_flow_sweeps].
- $580.9K ask-side May-2026 230P sweep + $519.7K ask-side May-2026 220P sweep
  + $171.6K ask-side Dec-2026 195P sweep = **$1.27M of put protection** being
  paid up for, dominantly short-dated [FLOW:options_flow_sweeps].
- FSLR sits in the **top sweep universe 5/5 days** with
  `consistency_score=1, total_sweep_premium=$35.37M`, but
  `dominant_direction="mixed"` — persistent two-way conviction
  [FLOW:hot_chains_sweep_persistence].
- No FSLR contract appears in the market-wide top-25 smart-money lists (bull
  or bear) — sized vs the SPY/IWM/SMH whales but is not a top tape mover
  [FLOW:hot_chains_smart_money_flow].

## Detailed findings

### Sweeps (ask vs bid, premium, persistence)

Top FSLR sweeps on 2026-05-15 (date=2026-05-15, min-premium=$100K):

| Side | Strike/Type | Expiry | Premium | Size | Trades | Avg px | Read |
|------|-------------|--------|---------|------|--------|--------|------|
| ASK | 280 C | 2027-03-19 | $1.668M | 480 | 2 | $34.75 | **Long-dated near-ATM call open, conviction print** |
| BID | 250 C | 2026-06-18 | $1.618M | 1,601 | 73 | $9.59 | Sellers/closers active on Jun call |
| ASK | 250 C | 2026-06-18 | $1.597M | 1,574 | 52 | $9.69 | Bullish buyers offsetting bid pressure |
| ASK | 230 P | 2026-05-22 | $580.9K | 1,285 | 37 | $4.82 | Short-dated hedge / bearish |
| MID | 250 C | 2026-06-18 | $528.0K | 518 | 6 | $9.71 | More 250C churn |
| ASK | 220 P | 2026-05-29 | $519.7K | 1,505 | 18 | $3.54 | Tail hedge |
| BID | 270 C | 2026-07-17 | $495.8K | 512 | 9 | $9.12 | Call seller/closer |
| BID | 400 C | 2028-01-21 | $378.1K | 138 | 2 | $27.40 | LEAP unwind, not new open |
| BID | 200 C | 2026-05-15 (0DTE) | $310.7K | 90 | 8 | $32.82 | ITM 0DTE close (Δ=0.90) |
| ASK | 155 C | 2027-03-19 | $309.3K | 32 | 8 | $96.65 | Deep-ITM LEAP open (synthetic long stock) |
| ASK | 240 C | 2026-05-29 | $266.0K | 361 | 43 | $7.52 | Near-money bullish |
| ASK | 240 C | 2026-06-18 | $218.5K | 177 | 40 | $12.71 | Same idea, longer dated |
| ASK | 185 C | 2026-12-18 | $183.9K | 26 | 6 | $70.73 | Deep ITM Dec call open |
| ASK | 195 P | 2026-12-18 | $171.6K | 92 | 21 | $18.66 | Year-end downside hedge |

**Net premium tally (FSLR-only sweeps ≥ $100K):**
- Ask calls: 1,668 + 1,597 + 309 + 266 + 218.5 + 183.9 + 156.2 + 134.7 + 125 + 105.1 + 100.2 ≈ **$4.864M**
- Bid calls: 1,618 + 495.8 + 378.1 + 310.7 + 149.6 + 141.7 + 135.2 ≈ **$3.229M**
- Mid calls: $528K
- Ask puts: 580.9 + 519.7 + 171.6 ≈ **$1.272M**
- Bid puts: $118K

→ Call ask − call bid = **+$1.63M net call buying**.
→ Put ask − put bid = **+$1.15M net put buying** (hedge layer).

The dollar-weighted call bias is positive but the put hedge is unusually
heavy for FSLR's size; consistent with "lift into resistance, buy crash
insurance" institutional behaviour.

### New positioning (unusual vol, vol/OI ratio)

Top unusual-volume contracts:

| Type | Strike | Expiry | OI | Vol | vol/OI | Premium | IV | Read |
|------|--------|--------|----|-----|--------|---------|-----|------|
| Call | 280 | 2027-03-19 | 48 | 480 | **10.0×** | $1.668M | 57.4% | Opening — same as top sweep |
| Put | 220 | 2026-05-29 | 192 | 1,513 | **7.88×** | $523.5K | 53.7% | Opening — fresh hedge |
| Call | 232.5 | 2026-05-15 (0DTE) | 92 | 329 | 3.58× | $53.4K | 8.6% | Day-trader pin chase |
| Call | 255 | 2026-05-22 | 63 | 201 | 3.19× | $18.4K | 58.9% | Small lottery ticket |
| Put | 220 | 2026-05-22 | 67 | 203 | 3.03× | $40.2K | 55.9% | Hedge extension |

Two largest *new* positions are diametric: long-dated ATM-ish call vs
near-dated 220-strike put. This is the smoking gun for the "two-sided
institutional" thesis.

### Largest premium prints

Single trades ≥ $100K, sorted by premium (full timestamps preserved):

| Time (UTC) | Type | Strike | Expiry | Premium | Side | Δ | IV | UL price |
|------------|------|--------|--------|---------|------|----|----|----------|
| 19:30:52 | Call | 280 | 2027-03-19 | **$1,390K** | ASK | 0.479 | 57.5% | 236.26 |
| 18:55:27 | Call | 250 | 2026-06-18 | $612K | BID | 0.397 | 55.1% | 235.87 |
| 18:22:41 | Call | 250 | 2026-06-18 | $609K | ASK | 0.398 | 54.9% | 236.02 |
| 18:40:01 | Call | 250 | 2026-06-18 | $563K | ASK | 0.395 | 55.6% | 235.54 |
| 18:22:41 | Call | 250 | 2026-06-18 | $521K | MID | 0.398 | 54.9% | 235.99 |
| 18:56:18 | Call | 270 | 2026-07-17 | $485K | BID | 0.315 | 54.8% | 235.63 |
| 19:23:24 | Put  | 220 | 2026-05-29 | $404K | ASK | −0.229 | 53.1% | 236.35 |
| 19:02:08 | Call | 250 | 2026-06-18 | $349K | BID | 0.397 | 55.3% | 235.78 |
| 19:32:43 | Call | 280 | 2027-03-19 | $278K | ASK | 0.479 | 57.4% | 236.39 |
| 15:20:05 | Call | 400 | 2028-01-21 | $241K | BID | 0.347 | 55.3% | 231.72 |

Note the 19:30:52 print on the Mar-2027 280C — late-session, paid the ask,
single-print 400 lots. That is the high-conviction signature of the tape.

### IV outliers + Greeks

`options_flow_iv_outliers` returned **0 rows** for FSLR (min-iv default 1.0
i.e. 100%) — no triple-digit-IV speculation on the name, consistent with a
$236, $25B large-cap solar manufacturer whose ATM IV sits in the **mid-50s%**.

Greek screener (sorted by premium) shows:
- The Mar-2027 280C had **Δ=0.479, γ=0.0032, ν=0.865, θ=−0.081**.
  High vega, low gamma → this is structurally a **vol-and-direction** bet,
  not a delta-1 punt.
- The Jun-2026 250C cluster had **Δ≈0.395–0.398, γ≈0.0097, ν≈0.278**.
  Near-the-money, moderate gamma, modest vega — a directional 5-week play.
- The May-2026 230P had **Δ=−0.367, γ=0.022, ν=0.123, θ=−0.46** — pure
  short-dated short-delta hedge, decaying fast (highest theta in the deck).

### Multi-day persistence

`hot_chains_sweep_persistence` (5-day, symbol=FSLR):

| Field | Value |
|-------|-------|
| sessions_in_top | 5 of 5 |
| consistency_score | 1.0 |
| dominant_direction | mixed |
| total_sweep_premium (5d) | $35,370,060 |

FSLR has been a daily-sweep regular all week — the flow is not a one-day
anomaly, it is a sustained two-way institutional engagement. Mixed direction
across 5 sessions is the strongest evidence we have that today's tape is
**positioning, not directional liquidation**.

### Market-wide smart money context

Neither the bullish nor bearish smart-money top-25 contains a single FSLR
strike. The biggest tape directional bets on 2026-05-15 are
- Bullish: PEP Sep-2026 155C ($24.0M premium, ratio 35.9), IWM Jun-2026 270P
  bull-rolls, MARA short-dated calls.
- Bearish: IWM May-2026 270P/260P ($17.9M and $4.7M bid), SMH May-2026 500P
  ($48.8M bid), XLI Jun-2026 145P.

Macro tone (per the market-wide table) is risk-off — small caps and chips
being hedged hard. FSLR-specific tape is **constructive vs that backdrop**.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__options_flow_sweeps` | `{symbol: FSLR, min-premium: 100000, top-n: 25, date: 2026-05-15}` | 23 rows; biggest = Mar-2027 280C ask $1.668M |
| `mcp__uw-pp__options_flow_unusual_volume` | `{symbol: FSLR, min-vol-oi-ratio: 3, top-n: 25, date: 2026-05-15}` | 5 rows; top vol/OI = 10× on Mar-2027 280C |
| `mcp__uw-pp__options_flow_top_premium_trades` | `{symbol: FSLR, top-n: 25, date: 2026-05-15}` | 26 rows; largest single = $1.39M |
| `mcp__uw-pp__options_flow_iv_outliers` | `{symbol: FSLR, top-n: 15, date: 2026-05-15}` | empty (no IV ≥ 100%) |
| `mcp__uw-pp__options_flow_greek_screener` | `{symbol: FSLR, top-n: 15, sort-by: premium, date: 2026-05-15}` | 15 rows mirroring top-premium with Greeks |
| `mcp__uw-pp__hot_chains_smart_money_flow` | `{direction: bullish, top-n: 25, min-volume: 500, date: 2026-05-15}` | No FSLR rows |
| `mcp__uw-pp__hot_chains_smart_money_flow` | `{direction: bearish, top-n: 25, min-volume: 500, date: 2026-05-15}` | No FSLR rows |
| `mcp__uw-pp__hot_chains_sweep_persistence` | `{symbol: FSLR, days: 5, top-n: 25}` | 1 row, consistency=1, mixed, $35.37M 5d |
| `mcp__uw-pp__hot_chains_sweep_ratio` | `{top-n: 25, min-volume: 500, min-sweep-ratio: 0.3, date: 2026-05-15}` | Market-wide; no FSLR row (sweep ratio < 0.3 on FSLR contracts) |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** mixed-bullish.
- **Conviction:** 3/5. Net call buying is real and led by a long-dated ATM
  LEAP open, but the matching put hedge layer and two-sided 250C tape stop
  this from being a 4–5 directional flow read.
- **Three things later phases should remember:**
  1. The cornerstone print is **Mar-2027 280C @ $34.75 ask, $1.39M, Δ=0.48,
     IV 57.5%, vol/OI = 10×** (executed 19:30:52 UTC). Any thesis must
     reconcile to this.
  2. Hedge layer is **220–230 May-2026 puts (≈$1.1M)** + Dec-2026 195P
     ($172K). Institutions want crash insurance through summer.
  3. FSLR has been **in the top sweep universe every day of the week**
     ($35.4M 5d sweep premium, mixed direction) — this is a sustained
     campaign, not a one-day blip.
- **Open questions for downstream:**
  - Is the 280C buyer the same flow as institutional dark-pool accumulation?
    (→ phase-2 dark pool)
  - Where does dealer gamma sit relative to spot $236? (→ phase-4 structure)
  - Is IV rank elevated or depressed for this name historically? (→ phase-5
    historical)
  - Earnings catalyst in window? Mar-2027 LEAP would imply view past several
    earnings cycles. (→ phase-6 macro / earnings calendar)
