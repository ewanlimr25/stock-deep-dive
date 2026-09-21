# Phase 1 — Options Flow

**Ticker:** NBIS (Nebius Group NV)
**As-of date:** 2026-06-17
**Generated:** 2026-06-18T00:28:36Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md

## Summary

The tape is **net bullish but heavily two-sided**, and the bullish read strengthens as you move
from premium to delta-notional. On premium the day nets only **+$18.0M** (bullish $295.3M vs
bearish $277.3M ex-0/1DTE — exactly reconciling the screener `net_flow`), but on **delta-notional
the tape is ~1.76:1 bullish (+$0.469bn vs −$0.267bn)** because the bullish exposure is concentrated
in **high-delta LEAP calls (LEAP call/put premium 4.6:1, $238.0M vs $51.8M)** while the bearish side
is lower-delta OTM puts. This is backed by a **5-of-5-session bullish sweep campaign (consistency
score 1, $722.4M total sweep premium, Jun 11–17)** — the strongest single signal in the phase. The
qualifier (carried from phase-0.5): it is NOT a clean one-sided ask-side blast — there is real fresh
put buying ($95.5M ask-side, incl. a $17.3M Sept $250 put) and ~$182M of LEAP call *selling* on the
bid (overwriting), and IV rank 91 makes all of it expensive.

## Key signals

- **Whole-tape net:** call premium $514.1M vs put premium $189.4M (2.7×), but directional `net_flow`
  only **+$18.0M** (bullish $329.1M − bearish $311.1M) — two-sided. P/C 0.846. [FLOW:insights_deep_dive]
- **Delta-notional is the cleaner bull read:** +$0.469bn bullish vs −$0.267bn bearish (ex-0/1DTE) →
  net **+$0.20bn**, ~1.76:1, concentrated in deep-ITM LEAP calls. [FLOW:duckdb_aggressor DUCKDB]
- **Persistent bullish sweep campaign:** NBIS in top sweeps **all 5/5 sessions**, dominant_direction
  bullish, consistency_score 1, total_sweep_premium **$722.4M**. [FLOW:sweep_persistence]
- **Biggest single print:** $180 CALL exp **2028-12-15**, premium **$19.86M**, delta 0.874 — deep-ITM
  long-dated stock-replacement (bullish, slow). [FLOW:greek_screener / top_premium_trades]
- **Counter-tape:** fresh new positioning (vol/OI≥3) is PUT-heavy — deep-ITM $400 puts (Aug $12.7M,
  Sep $10.4M), near-ATM $290 hedges, an 11,343-lot $170 tail put — real downside hedging. [FLOW:unusual_volume]

## Detailed findings

### Whole-tape aggregate (read everything below against this) [FLOW:insights_deep_dive]

| Field | Value |
|-------|-------|
| call_premium | $514,133,070 |
| put_premium | $189,438,807 (calls 2.7× puts on premium) |
| bullish_premium | $329,134,229 |
| bearish_premium | $311,125,142 |
| **derived net_flow** | **+$18,009,087** (bull − bear; +2.8% of gross — two-sided) |
| call_volume / put_volume | 140,521 / 118,813 |
| put_call_ratio | 0.846 (call-heavy) |
| iv_rank / iv30d | 91.3 / 113.1% |
| implied_move | 13.66 pts = 4.86% |

The 2.7× call-vs-put *premium* overstates direction: the buy/sell-classified net is only +$18M, i.e.
much of the call premium is being SOLD (overwriting), not bought. The directional truth is in the
aggressor + delta-notional split below.

### DuckDB aggressor & delta-notional split (ex-0/1DTE pin noise) [FLOW:… DUCKDB]

| Type | side | premium | delta-notional |
|------|------|---------|----------------|
| call | ask (buy) | $221.67M | +$0.661bn |
| call | bid (sell) | $181.84M | +$0.530bn |
| put | ask (buy) | $95.51M | −$0.263bn |
| put | bid (sell) | $73.67M | −$0.192bn |

- Net call buying (ask−bid) = **+$39.8M** premium; net put buying = **+$21.8M** premium → both sides
  are being bought, but calls more. Classified bullish_dn **+$0.469bn** vs bearish_dn **−$0.267bn**.
- **DTE buckets (premium):** LEAP call $238.0M / put $51.8M (**4.6:1**); 8-45DTE $127.2M / $62.5M
  (2.0:1); 46-180DTE $88.1M / $61.7M (1.4:1); 0-1DTE $60.9M / $13.5M (pin noise, discounted).
  Calls dominate every tenor; dominance is largest and most institutional in LEAPs.

### Sweeps (ask vs bid) [FLOW:sweeps]

Top-25 each side. Ask-side (aggressive buying): 17 calls $101.3M / 8 puts $55.8M. Bid-side (selling):
17 calls $86.7M / 8 puts $42.0M. **Net ask-side aggression is nearly equal in calls (+$14.6M) and
puts (+$13.9M)** — the single largest ask-side sweep is a **$250 PUT (exp 2026-09-18) at $17.3M**
(downside positioning). Large bid-side LEAP call writes appear ($350c 2028 $14.1M, $400c 2028 $12.7M
sold) = overwriting/financing. Verdict: aggressive on BOTH sides — not a one-way sweep.

### New positioning — unusual volume (vol/OI ≥ 3) [FLOW:unusual_volume]

8 of the top 10 fresh positions are PUTS:

| Type | Strike | Expiry | Premium | vol/OI | avg_iv |
|------|--------|--------|---------|--------|--------|
| put | $400 | 2026-08-21 | $12.68M | 233 | 115% |
| put | $290 | 2026-06-26 | $4.18M | 168 | 116% |
| put | $290 | 2026-06-18 | $2.36M | 73 | 142% |
| put | $170 | 2026-07-02 | $1.63M (11,343 lots) | 70 | 154% |
| put | $400 | 2026-09-18 | $10.35M | 47 | 113% |
| call | $292.5 | 2026-06-26 | $1.05M | 43 | 113% |

Deep-ITM $400 puts (Aug+Sep ≈ $23M) are ambiguous (synthetic short vs sold-to-open financing); the
near-ATM $290/$282.5/$277.5 puts and the $170 tail put read as hedges. Net: fresh PUT demand is real
but, per the aggressor split, smaller in aggregate than the call buying.

### Largest premium prints [FLOW:top_premium_trades]

| Type | Strike | Expiry | Premium | side |
|------|--------|--------|---------|------|
| call | $180 | 2028-12-15 | $19.86M | no_side (deep-ITM LEAP, delta 0.87) |
| call | $240 | 2026-06-26 | $10.07M | ask (deep-ITM, delta 0.80) |
| call | $410 | 2026-09-18 | $7.20M + $5.97M | ask (OTM upside) |
| put | $250 | 2026-09-18 | $5.95M | ask (downside) |
| call | $285 | 2026-07-02 | $4.97M | bid (ATM call SOLD) |
| put | $290 | 2026-06-26 | $2.94M | ask (hedge) |
| put | $310 | 2027-03-19 | $2.92M | ask (long-dated downside) |

### IV outliers + Greeks [FLOW:iv_outliers / greek_screener]

IV outliers are all 0DTE (exp 2026-06-18) with absurd IVs (596–951%) — pin noise, discounted; only
the deep-ITM 0DTE $150/$155 calls ($1.6M/$1.2M) carry size. Greek-screener (by premium) confirms the
bullish delta footprint sits in the $180 2028 call (delta 0.874, $19.9M ≈ $17.4M delta-notional) and
$240 6-26 call (delta 0.80, $10.1M); puts carry smaller delta (−0.31 to −0.47). avg IV on the active
front strikes ≈ 113–116%.

### Smart-money-flow / sweep-ratio (market-wide) [FLOW:smart_money_flow / sweep_ratio]

NBIS is **not** in the market-wide smart-money-flow top-10 (bullish or bearish) or the sweep-ratio
top-15 — those lists are dominated by cheap, ultra-high-volume contracts (AAL, XLE). Recorded as
"not in market-wide top-N"; not re-run with looser thresholds (per composition guidance).

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← path | Rows |
|------------------|--------------------|------|
| `uw insights deep-dive --symbol NBIS --date 2026-06-17` | call_prem $514.1M, put_prem $189.4M, net_flow +$18.0M, P/C 0.846, iv_rank 91.3 ← `.uw_screener` | 1 |
| `uw options-flow sweeps --symbol NBIS --side ask --min-premium 100000 --top-n 25` | 17c $101.3M / 8p $55.8M; top=$250P Sep $17.3M ← `.results` | 25 |
| `uw options-flow sweeps --symbol NBIS --side bid …` | 17c $86.7M / 8p $42.0M ← `.results` | 25 |
| `uw options-flow unusual-volume --symbol NBIS --min-vol-oi-ratio 3 --top-n 25` | 8/10 puts; $400P Aug $12.7M, $400P Sep $10.4M ← `.results` | 25 |
| `uw options-flow top-premium-trades --symbol NBIS --top-n 25` | $180C 2028 $19.86M no_side ← `.results` | 25 |
| `uw options-flow iv-outliers --symbol NBIS --top-n 15` | all 0DTE 596–951% IV (noise) ← `.results` | 15 |
| `uw options-flow greek-screener --symbol NBIS --sort-by premium --top-n 15` | $180C 2028 delta 0.874 ← `.results` | 15 |
| `uw hot-chains sweep-persistence --days 5 --symbol NBIS` | 5/5 sessions, bullish, consistency 1, $722.4M ← `.results[0]` | 1 |
| `uw hot-chains smart-money-flow --direction bullish/bearish --top-n 10 --min-volume 500` | no NBIS rows ← `.results[]\|select(startswith NBIS)` | 0 |
| `uw hot-chains sweep-ratio --top-n 15 --min-volume 500 --min-sweep-ratio 0.3` | no NBIS rows | 0 |
| DuckDB §A aggressor+delta-notional (bot-eod 2026-06-17, ex-0/1DTE) | bull_dn +$0.469bn / bear_dn −$0.267bn; LEAP c/p 4.6:1; bull_prem $295.3M − bear_prem $277.3M = +$18.0M (cross-validates net_flow) | full tape |

## Tool errors

None. (`yahoo_fundamentals` 401 inside deep-dive already logged in phase-0.5; not a flow field.)

## DATA NOTE / CORRECTION

First sweep read mis-applied `avg_iv`/`vol`/`oi` jq paths that don't exist on the `sweeps` schema
(only avg_price, total_premium, total_size, trade_count, side) → re-extracted with the correct keys;
no number was transcribed from the failed read. Premium net (+$18.0M) independently reconciled
between the screener (`net_flow`) and the DuckDB parquet (bull_prem−bear_prem) — exact match.

## Verdict for downstream phases

- **Bias from this phase:** **bullish-leaning, two-sided** (premium net thin +$18M; delta-notional
  net clearly bullish +$0.20bn / 1.76:1, LEAP-call-led; counterweighted by real put hedging).
- **Conviction:** **3/5.** Upgraders: 5/5 persistent bullish sweep campaign (consistency 1, $722M),
  LEAP call dominance 4.6:1, delta-notional 1.76:1. Downgraders: net premium only 2.8% of gross,
  $95.5M fresh ask-side put buying + $182M LEAP call selling, IV rank 91 (expensive), and phase-0.5's
  cap (vol only 1.43×, "do not escalate to ++ on size alone").
- **Three things later phases must remember:**
  1. Bullish footprint is **tenor-broad and LEAP-led** (4.6:1) + a **5-day persistent sweep campaign**
     — this is conviction positioning, not a 0DTE blip; but it's slow (LEAP) so short-term tradeability is moderate.
  2. There is a **real downside hedge layer**: $95.5M ask-side puts incl. $250 Sep ($17.3M), deep-ITM
     $400 puts (~$23M), $170 tail put (11.3k lots). Phase-2 (dark pool) and phase-3 (OI walls) should test whether this is hedging vs genuine bearish conviction.
  3. ~$182M of **LEAP call SELLING** on the bid (overwriting/financing) means part of the call premium
     is supply, not demand — keep the net read at +$18M premium / +$0.20bn delta-notional, not the $514M call gross.
- **Open questions:** Is the dark pool confirming accumulation under this bid (phase-2)? Where are the
  OI walls relative to the $400 put / $410 call / $180 LEAP strikes (phase-3)? Is dealer gamma
  positive (pinning) or negative (accelerant) around spot $280.91 (phase-4)?
