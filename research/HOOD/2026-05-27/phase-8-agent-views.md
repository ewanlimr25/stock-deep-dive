# Phase 8 — Multi-Agent Analyst Desk

**Ticker:** HOOD
**As-of date:** 2026-05-27
**Generated:** 2026-05-28T14:03:50Z
**Upstream phases cited:** phase-1 … phase-7c (full chain packed to each agent)

## Summary

Four specialist agents ran in parallel (earnings-scout **skipped** — ER 2026-07-29 is
>30d out). **Unanimous: no directional long.** Two voted **RANGE**, two **NEUTRAL**, and
every one converges on the same structure — **capped at 78–80, slippery support
75.76→73.64→70, fade strength rather than chase, and any exposure must be small /
defined-risk.** Directional conviction is low (~2.5/5); the *risk-avoidance* conviction is
high (risk-monitor: 4/5 to REDUCE/avoid). The single most important new finding:
risk-monitor independently computed that **HOOD sits in a 0.84–0.94 high-beta cluster
(SOFI 0.94, COIN/IBKR 0.87–0.88, NVDA 0.84)** and AAPL is 0.736 to NVDA — so HOOD-long
beside the concurrent AAPL/2026-05-27 blueprint is **one undiversified tech-beta bet**,
into the regime's largest sector outflow (Tech −$433M), at beta 2.27.

## Agent verdicts table

| Agent | bias | conviction | horizon | one_line_take |
|-------|------|-----------|---------|---------------|
| accumulation-hunter | NEUTRAL (range, lean distributive) | 2 | 1-5d | No quiet hand — the "accumulation" is auction plumbing + a double-counted print; institutions feed stock into retail strength. |
| contrarian-scanner | RANGE (short-the-pop) | 3 | 1-5d | Good news sold into the 78–80 cap by distributing institutions — fade the pop, not a blowoff; small/defined-risk. |
| sweep-tracker | RANGE | 2 | 1-5d | No tape to chase — calls are written, the one urgent near-dated sweep is a put; trade the 78 flip / 73.5 fail, don't anticipate. |
| risk-monitor | NEUTRAL (lean range-to-bearish) | 4 (to REDUCE) | 1-4w | REDUCE/avoid — one leveraged tech-beta bet wearing two tickers, into half-size regime with CPI+FOMC binaries. |
| earnings-scout | — | — | — | **SKIPPED** (earnings 2026-07-29 > 30d out) |

## Per-agent details

### accumulation-hunter — NEUTRAL (lean distributive), conviction 2, 1-5d
- support: 75.76 (dominant 5d DP cluster) → 73.64 shelf → 70–72 put-write floor
- resistance: 78 (OI pin) → 80 (written-call wall, hard cap)
- invalidation: sustained *intraday* (not closing-auction) DP buying reclaiming/holding >78
  on rising volume, OR a de-duped large-tier block buy at buy_ratio >0.60
- top_signal: "Phase-2 session split is decisive — the off-exchange 'buy' is entirely the
  16:00 closing cross (94.8% above mid on $62M) while the regular session was net offered
  (40.8% above mid on $208M), and the $48M 'mega' is one $24M block double-counted at
  0.041% of float."
- top_risk: "Persistent MOC buying clustering at 75.76–76.23 over consecutive days (a
  known passive-accumulation venue) would flip this to genuine accumulation."

### contrarian-scanner — RANGE (short-the-pop), conviction 3, 1-5d
- support: 75.76 → 73.64 → 70
- resistance: 78–80 positive-gamma wall (sell zone); ZGL 77.85 is the line
- invalidation: sustained intraday reclaim & hold >78 = gamma flip to long-γ, removes the
  cap and flips vanna supportive → kills the fade
- top_signal: "phase-2 dark pool — the AI-launch +2.9% pop was sold into, intraday DP net
  offered (40.8% above mid on $208M) with the only 'buying' being the de-duped closing
  auction, and phase-7c shows institutional blocks net call-SELLING ($6.81M bid vs $4.95M
  ask) into retail/analyst length = distribution-into-strength."
- top_risk: "No true positioning extreme to fade (P/C z −1.05 NORMAL, IV rank 23) and a
  +$168M DEX buy-hedge plus a real catalyst (AI-agent trading + SpaceX IPO) could carry a
  reclaim above 78, flipping vanna supportive and squeezing the fade."

### sweep-tracker — RANGE, conviction 2, 1-5d
- support: 73.64 (DP cluster / lower edge of slippery 70–75)
- resistance: 77.85–78.00 (ZGL + OI pin @78)
- invalidation: sustained 30-min hold >78.00 on rising volume → LONG; sustained break
  <73.50 → SHORT
- top_signal: "sweep-persistence 5/5 sessions but dominant_direction MIXED (consistency 1,
  $82.3M), and aggressor-weighted sweeps are BID-heavy $8.15M>$6.09M with the marquee
  Aug-90C $2.75M SOLD — premium overwriting, not momentum." (Live re-run also flagged the
  one urgent near-dated sweep is a **74P 5/29 buy**, $1.09M / 12,205 contracts.)
- top_risk: "A real ask-side near-term call sweep stack appearing >78 (the gamma flip)
  could ignite a short-gamma squeeze and turn this dead RANGE into a fast LONG breakout."

### risk-monitor — NEUTRAL (lean range-to-bearish), conviction 4 (to REDUCE), 1-4w
- support: 75.00 (slippery negative-γ edge) → 73.64 DP shelf → 70 put-floor
- resistance: 77.85 ZGL / 78–80 positive-γ wall
- invalidation: risk-on needs a daily close >78 that holds (flips long-γ) AND regime off
  TRANSITIONAL AND a non-hawkish CPI/FOMC; for the bear/range, two daily closes back >78
- top_signal: "Independently computed from local screener closes, HOOD sits in a 0.84–0.94
  high-beta cluster (SOFI 0.94, COIN/IBKR 0.87–0.88, NVDA 0.84) and Technology is the
  single largest net-directional outflow at −$433.5M [market-regime 2026-05-27]."
- top_risk: "HOOD-long beside the concurrent AAPL/2026-05-27 book is one undiversified
  tech-beta bet (both hang off NVDA: HOOD 0.84, AAPL 0.736), and at beta 2.27 a routine
  −2% SPY day drags HOOD to ~72.8 through the 73.64 shelf in a short-gamma regime that
  amplifies it." (beta stress: −3% CPI/FOMC shock → ~71.)

## Disagreements

No directional disagreement — **0 LONG, 0 SHORT, 2 RANGE, 2 NEUTRAL.** The only nuance:
contrarian-scanner carries an explicit *short-the-pop* tilt (conviction 3) while
accumulation-hunter and sweep-tracker stay flat-RANGE and risk-monitor frames it as
*avoid/reduce*. All four agree on the levels and that the bullish case requires a
**sustained intraday hold >78** to even start.

## Tool errors

- `earnings-scout`: **SKIPPED** (out of window; ER 2026-07-29 > 30d). Per phase rule.
- No agent errors; agents re-ran `uw hot-chains sweep-persistence`, `uw options-flow
  sweeps`, `uw risk market-regime` and local correlation/beta compute — all confirmed the
  digest. (UW `portfolio-correlation` remains broken; risk-monitor computed clusters from
  local screener close.)

## Verdict for downstream

- **Plurality bias:** **RANGE / NEUTRAL** (2 RANGE, 2 NEUTRAL; **0 directional long/short**).
- **Average conviction (4 agents):** **2.75/5** directional — but note risk-monitor's 4 is
  conviction to *reduce/avoid*, so the directional edge is genuinely ~2/5 and the
  risk-avoidance signal is the strong one.
- **Three highest-quality signals across agents:**
  1. **Closing-auction artifact** — "buy" is the 16:00 cross (94.8% abv mid) vs regular
     session offered (40.8%); $48M mega = a double-counted single $24M block
     [DP:session_split DUCKDB][DP:dedup DUCKDB] (accumulation-hunter + contrarian).
  2. **Distribution-into-strength** — institutional blocks net call-SELLING ($6.81M bid vs
     $4.95M ask) + insider selling into the AI-news/analyst bid [SENT:retail_vs_inst DUCKDB]
     (contrarian + sweep-tracker).
  3. **Correlated tech-beta cluster** — HOOD 0.84–0.94 with SOFI/COIN/IBKR/NVDA; HOOD+AAPL
     = one bet into Tech's −$433M outflow at beta 2.27 [MACRO:portfolio_correlation DUCKDB]
     (risk-monitor).
- **Open questions surfaced:**
  - Would consecutive-day closing-auction (MOC) buying at 75.76–76.23 reveal genuine
    passive accumulation (flip the distributive read)? — needs forward sessions.
  - Does a sustained *intraday* reclaim >78 flip vanna supportive and squeeze the fade
    (the one path to LONG)? This is the binary phase-8b should pressure-test.
