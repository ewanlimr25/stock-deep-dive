# Phase 1 — Options Flow

**Ticker:** BABA
**As-of date:** 2026-05-20 (data: 2026-05-19)
**Generated:** 2026-05-20T00:05:00Z
**Upstream phases cited:** phase-0-intake.md
**Spot reference:** $135.56 (`underlying_price` field on Mar27 $145C print, 16:04:32Z)

## Summary

BABA's tape on 2026-05-19 is **net bullish but two-sided** — aggressive ASK-side
call sweeps total ~$5.7M across Jan/Mar 2027 LEAPs, Jun18 OTM calls, and
upside Jul17 $140C, while a paired Mar 2027 $145C/$130P print
($1.89M + $1.58M, same timestamp, same 1000-lot size) reads as a bullish
LEAP risk reversal. New positioning is dominated by Jun18 $137–$141C strikes
(vol/OI 100×+) and the May29 $124C (vol/OI 23×, $2.49M premium). BABA has been
in the top sweep table 5/5 sessions with **$217M cumulative sweep premium** —
this is institutional-grade campaign, not retail noise.

## Key signals

- LEAP risk reversal opened on the close: **Mar 2027 $145C +$1.89M ASK-equivalent**
  paired with **Mar 2027 $130P +$1.58M**, both 1000-lots, same trade timestamp
  16:04:32Z — bullish synthetic [FLOW:top_premium_trades].
- Jan 2027 $150C: $2.43M total premium on the ASK side across 40 trades,
  1626 contracts — directional LEAP campaign [FLOW:sweeps].
- Jun18 $140C: $1.09M no-side block (2500 lots, $4.35) with gamma 0.025 and
  delta 0.41 — sized for a gamma squeeze if spot pushes through $140
  [FLOW:greek_screener].
- BABA is in the top sweep table for **5 of last 5 sessions**, consistency_score
  = 1.0, cumulative sweep premium **$217.1M** [FLOW:sweep_persistence].
- New-money concentration: Jun18 $139C vol/OI **202×**, $138C **102×**, $137C
  **18×** — institutional ladder of slightly-OTM Jun upside [FLOW:unusual_volume].
- Tail-risk hedge: Jan 2027 $120P, $1.26M premium, 1300 lots — paired against
  the LEAP calls, this is portfolio-style downside protection, not a directional
  short [FLOW:top_premium_trades].

## Detailed findings

### Sweeps — ask-side vs bid-side breakdown

Premium-weighted (sweeps ≥ $100K, BABA only):

| Side | Bullish flag | Premium | Notable strikes |
|------|--------------|---------|------------------|
| ASK calls | bullish | **$5.69M** | Jan27 $150C ($2.43M), Jun18 $120C ($704K), May29 $124C ($730K), Jul17 $140C ($614K), Jan28 $200C ($493K), May22 $140C ($394K), Jun18 $145C ($323K) |
| BID calls | closing / short-call | **$3.43M** | May29 $124C ($1.34M, deep ITM at $135.5 spot → likely closing winners), May29 $123C ($602K), Jan27 $130C ($609K), Jan27 $120C ($445K), Aug21 $120C ($400K) |
| ASK puts | bearish / hedge | **$368K** | Jun18 $130P ($368K) |
| BID puts | closing or short-put | **$651K** | Jun5 $135P ($324K), Jan27 $135P ($328K) — selling puts at-the-money = bullish |
| `no_side` blocks | structure | **$5.82M** | Mar27 $145C ($1.89M) + Mar27 $130P ($1.58M) + Jan27 $120P ($1.26M) + Jun18 $140C ($1.09M) |

Net ASK-call premium ($5.69M) exceeds BID-call premium ($3.43M) by **+$2.26M**,
and most of the BID-call premium is concentrated in the deep-ITM May29 $123/$124C
strikes (intrinsic ≈ $11+) where BID-side reads as **profit-taking on existing
longs**, not opening shorts. Net bias from the sweep tape: **bullish**.

[FLOW:sweeps]

### Mar 2027 LEAP risk reversal (paired prints)

| Field | $145C | $130P |
|------|-------|-------|
| `executed_at` | 2026-05-19T16:04:32Z | 2026-05-19T16:04:32Z |
| `size` | 1000 | 1000 |
| `premium` | $1,890,000 | $1,580,000 |
| `delta` | +0.521 | −0.381 |
| `gamma` | 0.0070 | 0.0080 |
| `vega` | 0.493 | 0.472 |
| `IV` | 0.458 | 0.387 |

Net debit $310K (call premium − put premium). Combined delta = **+0.90** per
spread, vega-neutral. Interpretation: **bullish LEAP risk reversal** — long
upside above $145 with $130 as the short-put pin. If interpreted as a collar
against an existing long-stock book, the structure is still net bullish (long
$130P floor, short $145C cap), but the LEAP duration argues for synthetic-long
campaign. [FLOW:top_premium_trades] [FLOW:greek_screener]

### New positioning (vol/OI ≥ 3×) — Jun18 dominates

| Strike | Type | Expiry | Vol | OI | Vol/OI | Total prem |
|--------|------|--------|-----|----|----:|----:|
| 139 | C | 2026-06-18 | 404 | 2 | **202** | $195K |
| 136 | P | 2026-06-18 | 122 | 1 | **122** | $81K |
| 138 | C | 2026-06-18 | 305 | 3 | **102** | $156K |
| 132 | P | 2026-06-18 | 113 | 3 | 38 | $53K |
| 124 | C | 2026-05-29 | 1907 | 80 | **24** | **$2.49M** |
| 145 | C | 2027-03-19 | 1000 | 49 | 20 | $1.89M |
| 137 | C | 2026-06-18 | 238 | 13 | 18 | $131K |

The Jun18 cluster is **slightly OTM** (spot $135.56 → strikes $137–$141) and
represents fresh openings, not roll activity. The May29 $124C $2.49M is the
single largest new-money line — deep ITM, very high delta, reads as an
**institutional surrogate for stock** (synthetic long with leverage) ahead of
the May29 expiry. [FLOW:unusual_volume]

### IV outliers

All IV outliers ≥ 100% are clustered in May22 (3-day expiry) **far-OTM lottery
calls** ($162.5C / $167.5C / $170C / $172.5C / $185C / $200C). These are
0DTE/3DTE lottery flow — premium amounts are trivial ($85–$3K) and should be
**discounted as signal**. [FLOW:iv_outliers]

### Market-wide smart-money flow context

BABA does NOT appear in the market-wide top-25 bullish or bearish smart-money
flow tables — the top is monopolized by SPY/IWM/HYG/VIX index products and a
few single names (TSLA, AMZN, POET, WULF). The only China-adjacent line in the
top-25 bearish list is **KWEB May29 $32C bid-side $74K premium, 24k contracts
sold-to-close** (KWEB at much lower notional), which is mildly cautionary for
the China-tech complex but is dwarfed by direct BABA bullish flow.
[FLOW:smart_money_flow]

### Sweep persistence (5 sessions: 2026-05-13 → 2026-05-19)

| Field | Value |
|------|------|
| `ticker` | BABA |
| `sessions_in_top` | **5 / 5** |
| `consistency_score` | **1.0** |
| `dominant_direction` | mixed |
| `total_sweep_premium` | **$217,119,527** |

5/5 sessions with $217M in sweeps is **institutional campaign territory** —
this is not one fat-finger print. The "mixed" direction flag reflects that
both calls and puts are sweeping, but today's tape skew (ASK calls > BID puts,
plus bullish risk reversal) confirms the campaign is **net long-biased**.
[FLOW:sweep_persistence]

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `options_flow_sweeps` | symbol=BABA, min_premium=100K, top_n=25, date=2026-05-19 | 25 rows; ASK calls $5.69M vs BID puts negligible |
| `options_flow_unusual_volume` | symbol=BABA, min_vol_oi_ratio=3, top_n=25 | 14 rows; Jun18 ATM/OTM call cluster dominant |
| `options_flow_top_premium_trades` | symbol=BABA, top_n=25 | 26 rows; Mar27 risk reversal + Jan27 $120P hedge headline |
| `options_flow_iv_outliers` | symbol=BABA, top_n=15 | 6 rows; all May22 OTM lottery — discard as noise |
| `options_flow_greek_screener` | symbol=BABA, sort=premium, top_n=15 | 15 rows; Mar27 risk reversal Greeks confirm structure |
| `hot_chains_smart_money_flow` | direction=bullish, top_n=25 | market-wide; no BABA hit |
| `hot_chains_smart_money_flow` | direction=bearish, top_n=25 | market-wide; KWEB May29 $32C bid only (peripheral) |
| `hot_chains_sweep_persistence` | symbol=BABA, days=5 | 5/5 sessions, score 1.0, $217M cumulative |
| `hot_chains_sweep_ratio` | top_n=25, min_volume=500 | market-wide; no BABA contracts in top 25 |
| `hot_chains_multileg` | top_n=25, min_ratio=0.3 | market-wide; BABA Mar27 pair not flagged (single-leg parquet) |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** **bullish** (with paired hedging in Jan 2027 $120P).
- **Conviction:** **4 / 5** — high persistence, sized premium, multi-DTE
  structure, no contradicting bearish ask-side flow.
- **Three things later phases must remember:**
  1. 5-day sweep premium = **$217M** with consistency score 1.0 — phase 2
     (dark pool) must check whether tape buying is being absorbed at the bid
     or sourced internally; phase 3 (OI) must confirm Jun18 OTM call OI is
     building, not rolling.
  2. **Mar 2027 risk reversal:** $145C long / $130P short paired prints —
     phase 4 (dealer structure) must check whether dealers are short calls
     above $145 (positive vanna) or short puts below $130 (long gamma).
  3. **Spot anchor:** $135.56 at close. Key option-flow strikes from the
     phase: 119 (gamma squeeze trigger), 124 (deep-ITM new-money pivot),
     140 (Jun18 $1.09M block + Jul17 $140C ask), 145 (LEAP risk reversal
     ceiling), 150 (Jan27 LEAP target), 120/130 (downside hedge floors).
- **Open questions:**
  - Is the Jan 2027 $120P hedge sized to existing BABA long stock, or is it
    standalone? Phase 2 (dark pool absorbing on tape buys) can hint at this.
  - Does dealer GEX flip support a $140 magnet (phase 4)?
  - Is BABA's IV percentile rich or cheap for this magnitude of sweep
    campaign? (phase 5)
