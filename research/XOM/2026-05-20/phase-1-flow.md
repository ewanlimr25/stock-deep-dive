# Phase 1 — Options Flow

**Ticker:** XOM
**As-of date (user request):** 2026-05-20
**Effective data date:** 2026-05-18
**Generated:** 2026-05-19T00:00:00Z
**Upstream phases cited:** phase-0-intake.md

## Summary

XOM tape on 2026-05-18 shows heavy institutional activity (≥$10M premium across
top trades) but **directionally mixed** — the dominant footprint is a calendar
roll of large call positions from Dec'26 → Mar'27 with simultaneous downside
hedging via Dec'26 160P (ask, $1.1M) and a 2028 $120 LEAP put. Underlying ranged
$155.85 → $161.10 intraday with IV ~30–33% (no IV outliers). Sweep persistence
flags XOM as a top sweep ticker in **5 of last 5 sessions** ($73M cumulative)
but with `dominant_direction = "mixed"` — confirming sustained interest but no
clean directional consensus. *(see phase-0-intake.md §UW availability for the
2026-05-18 data anchor.)*

## Key signals

- **Calendar roll bullish duration extension:** four ~400-lot blocks executed
  within 3 minutes (15:16–15:19) — buy 400 Mar'27 155C @ $20.66 (ask, $826k,
  Δ 0.60) and sell 400 Dec'26 150C @ $20.52 (bid, $820k, Δ 0.65). Net keeps
  bullish delta but pushes duration 3M further out at near-identical premium.
  [FLOW:top_premium_trades]
- **Significant new put hedge layer:** Dec'26 160P opened ask-side, 414
  contracts, $612k premium, Δ -0.45, IV 30.3%; `vol_oi_ratio = 6.37` confirms
  new position (OI was 118, volume 752). [FLOW:unusual_volume]
  [FLOW:top_premium_trades]
- **2028 LEAP tail hedge:** single trade of 500 contracts XOM 2028-01-21 120P
  @ $7.10 (bid, $355k premium, IV 30.4%, Δ -0.17). Deep OTM, 20-month dated —
  long-dated tail risk hedge, not directional. [FLOW:top_premium_trades]
- **Persistent multi-session sweep activity:** XOM is the only ticker shown
  in `hot_chains_sweep_persistence` for the 5-day window, sessions_in_top = 5,
  consistency_score = 1.0, cumulative sweep premium **$73.0M**, but
  `dominant_direction = "mixed"`. [FLOW:hot_chains_sweep_persistence]
- **No "smart money" tilt:** XOM does not appear in either bullish or bearish
  top-25 smart_money_flow lists — i.e. its ask/bid imbalance is below the
  market's most aggressive directional names. [FLOW:hot_chains_smart_money_flow]

## Detailed findings

### Sweeps (ask vs bid, premium, persistence)

Top 5 sweeps by premium (date 2026-05-18):

| Rank | Expiry | Type | Strike | Side | Premium | Size | Trades | Avg Px | Read |
|------|--------|------|--------|------|---------|------|--------|--------|------|
| 1 | 2026-12-18 | Call | 150 | bid | $1,848,340 | 901 | 4 | 20.49 | Sell deep-ITM calls (close longs or write) |
| 2 | 2026-12-18 | Put  | 160 | ask | $1,109,173 | 750 | 7 | 14.76 | Buy slightly-ITM puts (hedge or bear) |
| 3 | 2027-03-19 | Call | 155 | ask | $1,054,672 | 510 | 9 | 21.47 | Buy ITM calls 10M out (bullish duration) |
| 4 | 2026-06-18 | Call | 160 | ask | $982,647 | 1,558 | 224 | 6.04 | Aggressive 1M ATM call buying |
| 5 | 2027-03-19 | Call | 155 | bid | $864,735 | 421 | 6 | 21.02 | Closing leg of #3 (paired) |

Pattern: the Dec'26 150C bid + Mar'27 155C ask + Dec'26 160P ask combination is
the signature of a **bullish roll with downside protection** — close existing
Dec'26 long calls into strength, roll into Mar'27 ITM calls, layer a Dec'26
ITM put as hedge against the now-extended duration.

The Jun'26 160C activity (#4) is more aggressive day-to-day positioning:
$983k ask-side vs $727k bid-side (rows 4 and 6 in the JSON), net ~$256k bullish
delta in the 1M ATM zone with 224 trades each — likely market-maker churn or
multi-account institution accumulating size.

Mid-tier sweeps include $510k bid-side put @ Sep'26 160P (407 size, 7 trades),
suggesting further put-protection layering on slightly-OTM expiries, not a
short put. Plus $312k bid-side put @ Oct'26 155P (317 size) — same theme.

### New positioning (unusual vol, vol/OI ratio)

7 contracts cleared `min_vol_oi_ratio = 3` for XOM. **6 of 7 are puts.**

| Expiry | Type | Strike | OI | Volume | Vol/OI | Premium | Avg IV |
|--------|------|--------|------|--------|--------|---------|--------|
| 2026-08-21 | Call | 185 | 6 | 171 | 28.5 | $55,968 | 32.8% |
| 2026-05-22 | Put | 160 | 77 | 494 | 6.42 | $120,485 | 38.0% |
| 2026-12-18 | Put | 160 | 118 | 752 | 6.37 | **$1,112,064** | 30.2% |
| 2026-05-29 | Put | 160 | 29 | 148 | 5.10 | $49,996 | 32.9% |
| 2026-05-22 | Put | 152.5 | 209 | 828 | 3.96 | $55,077 | 39.3% |
| 2026-08-21 | Put | 150 | 34 | 122 | 3.59 | $67,413 | 31.7% |
| 2026-08-21 | Call | 160 | 56 | 178 | 3.18 | $176,503 | 33.0% |

The dollar-weighted center of new positioning is the Dec'26 160P
($1.1M, 89% of put-side premium in this table). All other entries are <$200k.

### Largest premium prints

Top 5 by raw single-trade premium:

1. 2026-05-18T15:19:11Z — Mar'27 155C ask, 400 ct, $826,400, Δ 0.60, IV 31.8%
2. 2026-05-18T15:16:10Z — Dec'26 150C bid, 400 ct, $820,800, Δ 0.65, IV 32.2%
3. 2026-05-18T15:19:11Z — Dec'26 150C bid, 400 ct, $820,400, Δ 0.65, IV 32.2%
4. 2026-05-18T15:16:10Z — Mar'27 155C bid, 400 ct, $819,600, Δ 0.60, IV 31.5%
5. 2026-05-18T15:42:58Z — Dec'26 160P ask, 414 ct, $612,306, Δ -0.45, IV 30.3%

The four call legs (#1-4) executed in two paired sequences 3 minutes apart,
each pair = sell Dec'26 150C @ bid + buy Mar'27 155C @ ask, with net delta
near-flat per pair (+0.60 - 0.65 = -0.05 per share, but the longer duration
gives more vega and theta). Reading: same actor, calendar roll of ~800
contracts, $3.3M turnover. The put leg #5 (~25 minutes later) layered downside.

Additional notable prints:
- 2026-05-18T17:58:59Z — Jun'26 185C bid, 9000 ct, $477,000, Δ 0.08 (cheap OTM
  call write — could be income overlay against an existing long position).
- 2026-05-18T15:27:48Z — Jun'27 95C mid, 45 ct, $297,000 (deep-ITM long-dated
  call, $66 price, Δ 0.95 — synthetic-stock substitute, conviction-long).
- 2026-05-18T19:36:11Z — 2028-01-21 120P bid, 500 ct, $355,000, Δ -0.17 (LEAP
  tail hedge, IV 30.4%).

### IV outliers + Greeks

`options_flow_iv_outliers` returned **no rows** for XOM at the default
`min_iv = 1.0` threshold. Top of book IV across XOM contracts ranges 30%–58%,
with the few higher reads (49% on deep-ITM Jun'26 130C; 58% on deep-ITM
Jun'26 110C) explained by their depth (low extrinsic share, IV noisy). **No
elevated IV regime** at the ATM strikes — the Mar'27 155C and Dec'26 150C/160P
sit at 30–32% IV, consistent with normal large-cap energy vol.

Greek screener (sorted by premium) confirms:
- Highest vega trades concentrated in the Dec'26 / Mar'27 ATM blocks (vega
  0.45–0.56). These are vol-positive prints — long-dated buyers picking up vega.
- Highest gamma is the Sep'26 160P (γ 0.0154) and the Dec'26 160P (γ 0.0107) —
  both puts, modest pin-risk contribution near $160.
- Theta-burdened: same Dec'26 / Mar'27 calls (θ -0.030 to -0.035/day) — these
  are not cheap to hold; the actor is paying decay for duration.

### Smart-money cross-check

XOM is **absent** from both `hot_chains_smart_money_flow` lists (bullish and
bearish, top-25 each, min_volume=500). The top of both lists is dominated by
VIX/SPY/IWM/NVDA/SPXW macro hedging activity. Read: XOM's ask/bid
imbalance, while elevated, doesn't crack the most extreme top-25 of the tape.
The action is institutional but not panicked or euphoric — consistent with the
"roll + hedge" interpretation.

### Sweep ratio cross-check

`hot_chains_sweep_ratio` top-25 (date 2026-05-18) does **not** contain XOM —
suggests XOM sweeps are large in absolute size (hence appearing in
`sweep_persistence`) but mixed with non-sweep flow, so the ratio is below the
top-25 cutoff. Confirms institutional but not stampeding behavior.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__options_flow_sweeps` | symbol=XOM, min-premium=100000, top-n=25, date=2026-05-18 | 25 rows, top 5 dominated by Dec'26 150C / Mar'27 155C / Dec'26 160P / Jun'26 160C |
| `mcp__uw-pp__options_flow_unusual_volume` | symbol=XOM, min-vol-oi-ratio=3, top-n=25, date=2026-05-18 | 7 rows, 6 puts; Dec'26 160P dominates at $1.11M |
| `mcp__uw-pp__options_flow_top_premium_trades` | symbol=XOM, top-n=25, date=2026-05-18 | 26 rows; biggest 5 = 4 calls + 1 put block |
| `mcp__uw-pp__options_flow_iv_outliers` | symbol=XOM, top-n=15, date=2026-05-18 | empty (no contracts cleared min-iv=1.0) |
| `mcp__uw-pp__options_flow_greek_screener` | symbol=XOM, sort-by=premium, top-n=15, date=2026-05-18 | confirms top-premium-trades; highest vega in Dec'26/Mar'27 calls |
| `mcp__uw-pp__hot_chains_smart_money_flow` | direction=bullish, min-volume=500, top-n=25, date=2026-05-18 | XOM absent (top-25 dominated by VIX/SPY/NVDA macro hedges) |
| `mcp__uw-pp__hot_chains_smart_money_flow` | direction=bearish, min-volume=500, top-n=25, date=2026-05-18 | XOM absent |
| `mcp__uw-pp__hot_chains_sweep_persistence` | symbol=XOM, days=5, top-n=25 | XOM only result: 5/5 sessions, $73.0M total, direction=mixed |
| `mcp__uw-pp__hot_chains_sweep_ratio` | min-volume=500, min-sweep-ratio=0.3, top-n=25, date=2026-05-18 | XOM absent from top-25 |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** mixed-with-slight-bullish (duration extension + ITM
  call exposure rolled out 3 months; puts are protective hedge layers, not
  aggressive shorts).
- **Conviction:** 3/5 (high activity + multi-session persistence, but mixed
  direction and no smart-money-flow ranking).
- **Three things later phases must remember:**
  1. The Dec'26 → Mar'27 call calendar roll is the **biggest single
     institutional signature** on the tape. Watch for confirmation in OI
     changes (phase 3) and dealer GEX shift (phase 4) — if dealer short-gamma
     migrates further out the curve, the roll is real positioning, not a hedge
     unwind.
  2. **6 of 7 vol/OI ≥ 3 contracts are puts**, with the Dec'26 160P
     ($1.11M, IV 30.2%) being the dominant new position. Phase 3 should check
     if put OI increased materially at the 155/160 strikes; phase 4 should
     check if put-side DEX rose.
  3. XOM is a **5-of-5-session sweep-persistence top ticker** at $73M
     cumulative — but `direction=mixed`. Phase 5 must check whether 30-day
     premium-flow cumulation is bullish or bearish; phase 7 should pull
     `insights_signal_confluence` for a multi-signal verdict.
- **Open questions:**
  - Are the Dec'26 150C bid-side blocks closing existing longs, or **opening
    short calls** (covered or naked)? OI delta in phase 3 will resolve this.
  - Is the Dec'26 160P actually a HEDGE against existing long stock/calls, or
    a **directional bearish bet**? Dark pool activity (phase 2) and OI changes
    (phase 3) on Dec'26 160P will clarify.
  - Why is XOM under sustained 5-day sweep pressure ($73M) without showing in
    smart-money-flow imbalance lists? Phase 7 `insights_deep_dive` should
    surface the catalyst (earnings? CapEx headlines? oil tape?).
