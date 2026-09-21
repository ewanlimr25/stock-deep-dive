# Phase 8 — Multi-Agent Analyst Desk

**Ticker:** IREN
**As-of date:** 2026-06-05
**Generated:** 2026-06-07T02:05Z
**Upstream phases cited:** phases 1–7c (full packed context delivered to each agent)

## Summary

Four desk agents ran in parallel (earnings-scout deliberately skipped —
next earnings 2026-08-27, 83 days out, beyond the 30d gate). Verdict
distribution: **NEUTRAL ×3, RANGE ×1**; zero LONG, zero SHORT. Average
conviction **2.25/5**. The desk is unanimous that there is **no clean
directional trade at spot 54.35** — and unanimous on the battlefield map:
all four independently chose **support 50 / resistance 60** with the same
mechanics (06/12 put wall + GEX shelf below; gamma flip + DP shelf above).
The only directional lean comes from the contrarian-scanner (RANGE, 3/5,
fade-the-fresh-put-crowd toward the 55 pin with defined risk). The
sweep-tracker contributed the phase's one piece of new tape work: **today's
bid-side LEAP call selling was a one-day spike** (06/04 bid sweeps ≈$1.4M vs
today's $6.05M) and the rolling sweep-persistence read is STILL
dominant-bullish — "campaign paused, not broken."

## Agent verdicts table

| Agent | bias | conviction | horizon | one_line_take |
|-------|------|-----------|---------|---------------|
| accumulation-hunter | NEUTRAL | 2 | 1-4w | "No quiet accumulation here — the back-month LEAP buyers want the 2027/28 AI story, but the near-term tape is hedges chasing price down and dealers harvesting 130% vol, not size stepping in front of a bounce." |
| contrarian-scanner | RANGE | 3 | 1-5d | "The fresh put ladder is bagholders' insurance bought at the top of IV, not smart money's conviction; fade the panic toward the 55 pin, but only with defined risk and a hard BTC stop." |
| sweep-tracker | NEUTRAL | 2 | 1-5d | "Campaign paused not broken — one-day LEAP profit-take into a short-gamma flush that V-recovered; no follow-through short signature, but no urgency to chase either side until 55/50 resolves." |
| earnings-scout | SKIPPED | — | — | earnings 2026-08-27 > 30d out (phase gate) |
| risk-monitor | NEUTRAL | 2 | 1-5d | "No sizeable directional IREN bet survives this regime — short gamma plus two binaries plus a BTC-beta-4.28 driver means defined-risk only; correlation to the rest of the book is contained (no IREN pair ≥0.70), so IREN's danger is self-inflicted volatility, not portfolio contagion." |

## Per-agent details

### accumulation-hunter [AGENT:accumulation-hunter]
- bias NEUTRAL · conviction 2 · horizon 1-4w
- support 50 (06/12 put wall + −$7.4M GEX; below 50 the 5-day DP map is
  uncharted air-pocket) · resistance 60 (gamma flip + 61–62 DP shelf; then
  65.3–67.6 $450M overhead) · invalidation: long dies on daily close <50 with
  BTC <$58k; short dies on reclaim/hold >60.
- top_signal: "The only true accumulation fingerprint is the deep-OTM LEAP
  build confirmed OPENING in phase-3 (110C 09/2028 +4,018 and 110C 06/2027
  +3,044 bought at ask, plus the $7.48M 110C '28 cross) — patient upside added
  through the crash, but it is back-month only and sits under a front-week
  hedging tape."
- top_risk: "dip-buying" is mostly mechanics — mega-tier EMPTY,
  institutional_accumulation NEUTRAL (1.19), the 30-day OI build is a put
  ladder chasing price DOWN, and blocks sold premium both sides.

### contrarian-scanner [AGENT:contrarian-scanner]
- bias RANGE · conviction 3 · horizon 1-5d
- support 50 · resistance 60 · invalidation: **BTC closes <$56k OR spot
  closes <50** — either validates the put ladder as trend, fade is wrong.
- top_signal: "the crowd is FRESHLY/reactively short — retail bought 06/12
  puts at 130% front IV and the hedge ladder followed price down one
  strike/day (phase-5), while blocks sold the 55/56 strangle both ways and
  smart money kept opening 110C '27/'28 LEAPs (phase-3) — the bearish
  positioning is rented, not structural (borrow EASY, DTC 1.20)."
- Signal alignment audit (their own count): put-extreme ✓(partial),
  screener-vs-flow divergences ✓(strong), regime/mechanics ✓; price-vs-flow
  and OI-unwind tools did NOT fire → conviction capped at 3.
- top_risk: BTC keeps falling → short-gamma accelerates through 50; the
  "reactive hedge" becomes a correct trend, not a fade.

### sweep-tracker [AGENT:sweep-tracker]
- bias NEUTRAL · conviction 2 · horizon 1-5d
- support 50 · resistance 60 (then 65.3–66.6) · invalidation: hold-and-close
  >55 with bid-side LEAP selling NOT recurring 06/08-09 → flips back to
  LONG-continuation; close <50 on rising volume → flips SHORT.
- top_signal (new tape work): "sweep-persistence is still 5/5-session
  dominant-bullish at $339.9M (3-day re-check confirms bullish, consistency
  1.0, $211.9M), and my own tape check shows today's $6.05M bid-side Jan-27
  call selling was a one-day spike (06/04 bid sweeps were only ~$1.4M) —
  today is profit-taking inside an intact bullish campaign, not a campaign
  reversal." Also: relative volume 1.50× (63.7M vs 42.5M avg) — participation
  without a 3×+ climactic blowoff; the V-recovery close = absorbed
  capitulation.
- top_risk: short-gamma pit + BTC leg-down gets dealer-amplified through 50
  before the LEAP buyers' thesis matters.

### earnings-scout
SKIPPED — next earnings 2026-08-27 (83 days; phase gate is 30d). Not a
MISSING-agent error; deliberate per the phase table.

### risk-monitor [AGENT:risk-monitor]
- bias NEUTRAL · conviction 2 · horizon 1-5d
- support 50 · resistance 60 · invalidation: **BTC reclaiming >$65k flips the
  whole thesis bullish** (crowded put ladder unwinds into beta 4.28);
  sustained close <50 opens the air-pocket. "Spot 54.35 sits in the deepest
  short-gamma pit (54 = −$30.7M GEX) — no edge either way at spot."
- Fresh re-reads confirmed phase-6 bit-for-bit: regime TRANSITIONAL ("half
  position sizes"), breadth 29.4%, Tech −$807.6M; correlation matrix: **no
  IREN pair ≥0.70**, only IREN/RKT 0.608 soft-watch; the CRM/NOW/PATH 0.76–0.86
  software cluster does NOT include IREN.
- top_risk: "CPI (06/10) and FOMC+SEP (06/16-17) detonate inside a
  short-gamma pit (GEX −$64.8M, RV 113.7% > IV 109%) on top of the crowded
  06/12 put-ladder expiry — either a BTC bounce force-unwinds the rented put
  crowding violently upward, or a BTC break <$60k accelerates through the
  uncharted sub-50 air-pocket."

## Disagreements

No agent took an opposite *bias* from the majority (no LONG, no SHORT). The
one tilt: contrarian-scanner's RANGE carries a fade-toward-55-pin long lean
vs the three flat NEUTRALs — its top_signal (rented, reactive put crowding vs
block vol-selling) is quoted above and is the strongest argument for the
mean-reversion side of the book. Per the 3-2-split heuristic (here 3-1):
treat as **MIXED → phase-9 targets 0.55–0.65 conviction ceiling and a
defined-risk structure**.

## Tool errors

None. All four launched agents returned structured verdicts within budget
(9–13 tool uses each). earnings-scout: deliberate skip (not MISSING).

## Verdict for downstream phases

- **Plurality bias:** NEUTRAL (3 of 4) + RANGE (1) — effectively
  **NEUTRAL/RANGE, no directional mandate**.
- **Average conviction:** 2.25 / 5.
- **Three highest-quality signals across agents:**
  1. [AGENT:sweep-tracker] Today's bid-side LEAP selling was a ONE-DAY spike
     (06/04 ≈$1.4M vs 06/05 $6.05M); rolling persistence still dominant-bullish
     → "paused, not broken."
  2. [AGENT:contrarian-scanner] The bearish positioning is rented — retail
     puts bought at 130% IV, ladder reactive one-strike-per-day, blocks
     selling the 55/56 strangle, borrow EASY — fade-able with defined risk.
  3. [AGENT:risk-monitor] Both binaries (CPI 06/10, FOMC 06/16-17) land
     inside the short-gamma pit on the put-ladder expiry — whipsaw window;
     regime guidance "half position sizes" is a direct sizing instruction.
- **Unanimous level map:** support **50**, resistance **60**, pin **55** —
  identical across all four agents.
- **Open questions surfaced:** Does bid-side LEAP selling recur 06/08-09
  (sweep-tracker's flip condition)? Does BTC hold $56–60k through CPI
  (contrarian + risk-monitor invalidation hinge)? Below 50, where is the next
  real support given the uncharted DP map (accumulation-hunter's air-pocket)?
