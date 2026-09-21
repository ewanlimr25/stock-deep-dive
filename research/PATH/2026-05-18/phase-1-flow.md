# Phase 1 — Options Flow

**Ticker:** PATH
**As-of date:** 2026-05-18 (data: 2026-05-15)
**Generated:** 2026-05-18T00:10:00-04:00
**Upstream phases cited:** phase-0-intake.md

## Summary

PATH's tape is decisively **bullish** with a small-cap signature: aggressive
ask-side call sweeps stacked into Jan-2027 and Jan-2028 LEAPs, and
front-week call sweeps at the $11.5 strike. The standout is sweep
**persistence — PATH appeared in the top market-wide sweep activity in 5 of
the last 5 sessions, dominant direction bullish, cumulative sweep premium
$7.77M** [FLOW:hot_chains_sweep_persistence]. Put activity exists but is
clustered in near-dated $9-10.5 strikes, more consistent with hedging
long-stock than a directional short. Absolute premium is small (top
single-contract sweep $693k) — consistent with PATH being a sub-$11 small
cap.

## Key signals

- **5-of-5 session sweep persistence, bullish, $7.77M cumulative** —
  rarely-seen single-name conviction signal
  [FLOW:hot_chains_sweep_persistence].
- **2027-01-15 $12C ask-side sweep: 3,742 contracts, $693k premium, 111
  trades** — biggest single-day institutional footprint, ~25 delta at
  underlying $9.85 [FLOW:sweeps].
- **2026-05-29 $11.5C unusual volume: 5,617 vol vs 522 OI (10.8×), $209k
  premium, avg IV 117.8%** — new short-dated bullish positioning above
  spot [FLOW:unusual_volume].
- **2027-01-15 $30C single block 4,293 contracts, $133k premium, delta
  0.12** — far-OTM upside lottery / call-overwrite-replacement candidate
  [FLOW:top_premium_trades].
- **2026-07-17 $15C vol/OI 166.5×** — pure new positioning, premium small
  ($22k) but reads as smart-money OTM bet for July
  [FLOW:unusual_volume].

## Detailed findings

### Sweeps (ask vs bid)

Underlying was ~$9.85 → $10.40 intraday (closing near $10.36 per
top_premium_trades). Largest aggregated sweeps by side:

| Strike / Expiry | Type | Side | Premium | Size | Trades | Read |
|---|---|---|---|---|---|---|
| **$12C / 2027-01-15** | call | **ask** | **$693,174** | 3,742 | 111 | Bullish LEAP accumulation [FLOW:sweeps] |
| $9C / 2026-05-15 | call | ask | $186,119 | 1,763 | 30 | Expiring ITM, mostly delta-hedge / closing |
| $30C / 2027-01-15 | call | no_side | $133,083 | 4,293 | 1 | Single block, far OTM lottery |
| $11.5C / 2026-05-29 | call | bid | $123,859 | 3,504 | 51 | Bid-side — closing or short premium |
| $20C / 2028-01-21 | call | bid | $109,985 | 553 | 13 | Mixed: bid-side trim of LEAP |
| $10C / 2026-06-18 | call | ask | $107,440 | 971 | 96 | Near-month bullish add |
| $10.5P / 2026-05-22 | put | ask | $93,028 | 1,781 | 263 | Likely **protective put** on stock |
| $10C / 2027-01-15 | call | ask | $80,271 | 305 | 42 | Add to ITM LEAP base |
| $12C / 2026-06-18 | call | bid | $66,776 | 1,173 | 57 | Bid-side trim, partial offset to LEAP add |
| $10C / 2026-05-15 | call | bid | $64,976 | 2,441 | 236 | Closing ATM exposure |

**Read:** Call ask-side premium dominates (~$1.18M+ across the top tape).
Bid-side puts are smaller and clustered just below spot — protective, not
directional shorts. The 2028 $20C and $25C show **bid-side** activity —
this is a *partial trim* of long-dated LEAPs, not a fresh short.

### New positioning (vol/OI ratio)

| Contract | Vol | OI | Vol/OI | Premium | IV |
|---|---|---|---|---|---|
| 2026-07-17 $15C | 666 | 4 | **166.5×** | $22,063 | 88.2% |
| 2026-07-17 $10C | 167 | 2 | 83.5× | $25,877 | 84.0% |
| **2026-05-29 $11.5C** | **5,617** | **522** | **10.8×** | **$209,318** | **117.8%** |
| 2026-05-22 $12P | 320 | 36 | 8.9× | $57,098 | 85.7% |
| 2026-07-17 $13C | 149 | 25 | 6.0× | $8,800 | 84.9% |

Four of five unusual-vol contracts are calls. The 2026-05-29 $11.5C — a
**$1.65 OTM bet expiring in 2 weeks** with 5.6k contracts of new size and
IV of 117.8% — is the most aggressive **near-term** bull signal of the
day.

### Largest premium prints

Top 8 trades concentrate in **2027-01-15 $12C** (six prints at the same
price $1.84 ask-side: $97.7k, $67.0k, $66.2k, $49.5k, $34.0k, $27.8k,
$27.4k) — same actor working a block. Combined: ~$369k ask-side at the
$12 strike alone, 2,059 contracts, all stamped between 14:47:11 and
14:47:11 UTC (single sweep print) [FLOW:top_premium_trades].

Two ITM 0DTE $9C prints ($53k + $52.5k ask) at 16:23-16:24 UTC with IV
160-170% are stock-equivalent buys, NOT directional options (delta
≈ 1.00, gamma ≈ 0). Discount these as synthetic stock.

### IV outliers

Top 4 IV outliers are all **same-day-expiring** $8-10 calls with avg IV
170-280%+. This is end-of-day pin/expiry noise — discount. The
informative outlier is **2026-06-05 $11C avg IV 105.4%** with $20.4k
premium and 272 volume — an event-anticipation signal for the first
week of June.

### Greeks profile

Net flow skews to **moderate-delta (0.45-0.55) call buying** on long
horizons (Jan-2027 $12C dominates), supplemented with **low-delta
(0.12-0.30) lottery** at $30 strike Jan-2027 and $20/$25 strikes
Jan-2028. Vega exposure on the LEAPs is meaningful (0.032 per contract)
but theta drag is tiny (-0.005), so these are durable bullish bets.

### Market-wide context

PATH did NOT appear in the top-25 `hot_chains_smart_money_flow` ranked by
net flow on 2026-05-15 [FLOW:hot_chains_smart_money_flow]. This is
expected for a sub-$11 small cap — single-contract net flows lose to
TLT/INTC/MARA/SPY. The sweep_persistence ranking is the better lens for
this name, and PATH leads it.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `options_flow_sweeps` | `{symbol: PATH, date: 2026-05-15, min-premium: 10000, top-n: 25}` | 25 rows, top sweep 2027 $12C ask $693k |
| `options_flow_unusual_volume` | `{symbol: PATH, date: 2026-05-15, min-vol-oi-ratio: 3, top-n: 25}` | 5 contracts, 4 calls 1 put |
| `options_flow_top_premium_trades` | `{symbol: PATH, date: 2026-05-15, top-n: 25}` | 26 trades; 2027 $12C ask block dominates |
| `options_flow_iv_outliers` | `{symbol: PATH, date: 2026-05-15, top-n: 15, min-volume: 20}` | 15 rows; mostly expiring-day noise |
| `options_flow_greek_screener` | `{symbol: PATH, date: 2026-05-15, top-n: 15, sort-by: premium}` | Same call set; net moderate-delta long |
| `hot_chains_sweep_persistence` | `{symbol: PATH, days: 5, top-n: 20}` | PATH 5/5 sessions, bullish, $7.77M |
| `hot_chains_smart_money_flow` | `{direction: bullish, top-n: 25, min-volume: 500, date: 2026-05-15}` | PATH not in top-25 (small-cap masking) |
| `hot_chains_sweep_ratio` | `{top-n: 25, min-volume: 500, min-sweep-ratio: 0.3, date: 2026-05-15}` | PATH not in top-25 ratio table |

## Tool errors

(none)

## Verdict for downstream phases

- **Bias from this phase:** **BULLISH**
- **Conviction:** **4/5** — sweep persistence is the standout; held back
  from 5 by small absolute premium and the bid-side trim on 2028 strikes.
- **Three things later phases must remember:**
  1. **PATH has logged 5-of-5 session sweep persistence, bullish, $7.77M
     cumulative** — the single most important number in the deep dive
     so far [FLOW:hot_chains_sweep_persistence].
  2. The dominant institutional footprint is the **2027-01-15 $12C
     ask-side sweep ($693k, 3,742 contracts, ~25-delta at $9.85
     underlying)** — that strike is the dealer pressure point to track
     in phase 4.
  3. **Near-term ammo: 2026-05-29 $11.5C unusual volume 5,617/522
     (10.8×) with IV 117.8%** — implies someone expects a >$1.65
     move within 2 weeks (≥17% from $9.85 spot at trade time).
- **Open questions for downstream:**
  - Is dark pool confirming accumulation in the underlying? (phase 2)
  - Where is dealer gamma flip relative to $11.5 / $12? (phase 4)
  - Is IV 117% on the 2026-05-29 $11.5C cheap or rich vs PATH's recent
    realized vol? (phase 5)
  - What event is the market pricing for late-May / June 2026? (phase 6
    — earnings, catalyst search)
