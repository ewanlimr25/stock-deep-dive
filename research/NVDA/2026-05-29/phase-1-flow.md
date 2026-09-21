# Phase 1 — Options Flow

**Ticker:** NVDA
**As-of date:** 2026-05-29
**Generated:** 2026-05-30T13:10Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md

## Summary

The tape is **call-skewed by volume/premium but aggressor-balanced and
low-conviction**, and it sits inside a bearish intraday tell: the largest prints
executed at underlying **~215–217 (the intraday high) yet NVDA closed at 211.14**
— buyers paid up for calls and the stock then **faded ~2–3% into the close**.
Whole-tape aggregate: call premium $1.04B vs put $277M (3.8:1), but
aggressor-adjusted it is nearly flat — **bullish premium $596M vs bearish $579M,
net only +$17.3M**. Sweeps confirm the balance: ask-side call sweeps $174M vs
bid-side $168M (**net +$6M**), and *puts were swept more aggressively on the ask*
(put ask−bid +$11.1M). The genuine bullish thread is real fresh call sweeping/OI
in **215–230 (Jun-5 → Jun-26)**, but it is heavily **0DTE/near-dated** and was
sold into. Against the phase-0.5 `[CTX:]` verdict (**BUSY_NAME_NORMAL_DAY**,
downtrend −10.4%/10d, NVDA 15th in its own leading sector) this is a
**fade-able bounce attempt, not conviction accumulation**. Net bias: **mixed /
weak-bullish, conviction 2/5** (capped at `+`).

## Key signals

- [FLOW:insights_deep_dive] Whole-tape: call_premium **$1.043B** vs put_premium
  **$277M**, but **bullish_premium $596M vs bearish_premium $579M = net
  +$17.3M** (aggressor-balanced). P/C ratio **0.424**.
- [FLOW:insights_deep_dive] Aggressor volume: **call ask/bid 1.03**, **put
  ask/bid 1.15** — puts bid slightly *harder* than calls on a −1.45% day.
- [FLOW:sweeps] Sweeps near-balanced: **ask call sweeps $173.8M vs bid call
  sweeps $167.8M (net +$6.0M)**; put sweeps ask $25.7M vs bid $14.5M (**put
  ask−bid +$11.1M** — aggressive put buying present).
- [FLOW:top-premium-trades] Top-25 prints **call-dominated $61M call vs $8M put**
  but aggressor-split (call ask $21.3M ≈ call bid $22.1M). Biggest: **230C Jun-26
  $9.4M ask** (underlying 215.48 at execution). Many 215C Jun-18 prints at mid.
- [FLOW:top-premium-trades] **Intraday fade tell:** top prints' `underlying_price`
  ≈ **215–217** vs **211.14 close** — calls bought near the highs, stock sold off
  ~2–3% into the close. The bullish bets are already offside on the day.

## Detailed findings

### Whole-tape aggregate (read top-N against this)

| metric | value | read |
|--------|-------|------|
| call_premium | $1,043.3M | call-skewed by premium |
| put_premium | $277.0M | — |
| bullish_premium | $596.1M | **near-balanced** vs bearish |
| bearish_premium | $578.7M | — |
| **net_flow (bull−bear)** | **+$17.3M** | mildly bullish, weak |
| put_call_ratio | 0.424 | structurally call-skewed (NVDA norm) |
| call ask/bid vol | 1,386,014 / 1,344,743 = **1.03** | calls barely net-bought |
| put ask/bid vol | 621,308 / 542,530 = **1.15** | **puts bid harder** |
| iv_rank | 40.65 | middling |

The "$1B call premium" headline is the trap the audit warns about: once adjusted
for aggressor side, bullish and bearish premium are within 3% of each other.
This is a balanced tape with a call *tilt*, not one-sided accumulation.

### Sweeps (ask vs bid)

| side | call sweep prem | put sweep prem |
|------|-----------------|----------------|
| ask (aggressive buy) | $173.8M | $25.7M |
| bid (aggressive sell) | $167.8M | $14.5M |
| **net (ask−bid)** | **+$6.0M calls** | **+$11.1M puts** |

Largest ask-side call sweeps: 215C 0DTE $22.7M (151K size, 20.6K trades — pure
expiry churn), 215C Jul-17 $20.6M, 230C Jun-26 $17.0M, 217.5C 0DTE $12.7M. Bid
side mirrors it (215C 0DTE $19.6M, 215C Jun-18 $19.6M). **Net sweep edge is
trivially positive on calls and meaningfully positive on puts** — i.e. the most
aggressive money is split, with a notable aggressive-put-buying undercurrent.
Most call sweep volume is 0DTE/near-dated expiry noise; discount it.

### New positioning (OI build, vol/OI) — `[FLOW:insights_deep_dive top_oi_changes]`

Fresh OI in near-dated slightly-OTM calls: **225C Jun-5 +20,337**, 217.5C Jun-5
+18,483 — a ~1-week directional bet above the (intraday) spot. Heavy 0DTE churn
at 215C/217.5C (May-29 expiry, vol 302K/163K) is pin/expiry noise — discounted.
(Cross-confirmed in phase-3 §OI changes, where the day's *largest single* build
was actually the 200P Jun-30 +33,653 — a downside hedge.)

### Largest premium prints (top-12, deduped, with aggressor side)

| type | strike | expiry | prem | side | size | underlying@exec | mny |
|------|--------|--------|------|------|------|-----------------|-----|
| call | 230 | 2026-06-26 | $9.4M | **ask** | 22,996 | 215.48 | OTM |
| call | 215 | 2026-06-18 | $5.0M | mid | 5,895 | 215.76 | OTM |
| call | 215 | 2026-06-18 | $4.9M | mid | 5,787 | 215.82 | OTM |
| call | 215 | 2026-06-18 | $4.8M | bid | 5,788 | 215.69 | OTM |
| call | 300 | 2028-12-15 | $4.4M | no_side | 1,000 | 216.87 | OTM (LEAP) |
| call | 215 | 2026-06-18 | $4.0M | bid | 4,961 | 215.14 | OTM |
| put | 250 | 2026-12-18 | $3.5M | ask | 750 | 216.87 | ITM |
| call | 195 | 2026-06-12 | $2.8M | bid | 1,315 | 215.89 | ITM |
| call | 195 | 2026-05-29 | $2.8M | ask | 1,315 | 215.89 | ITM |
| call | 450 | 2028-12-15 | $2.2M | no_side | 1,000 | 216.87 | OTM (LEAP) |

Call-dominated, but the aggressor mix is muddy (ask $21.3M ≈ bid $22.1M ≈ mid
$9.9M). The one unambiguous large *ask* bet is the 230C Jun-26 ($9.4M). Two
2028 LEAP calls (300C/450C, no_side, 1,000 lots each) are slow institutional
positioning, not near-term tradeable. Every print executed with underlying at
215–217 — all bought *above* the 211.14 close.

## Tool calls (audit trail)

| Command | Result |
|---------|--------|
| `uw insights deep-dive --symbol NVDA --date 2026-05-29 --json` | whole-tape aggregate + top OI changes |
| `uw options-flow sweeps --symbol NVDA --side ask --min-premium 100000 --top-n 25 --date 2026-05-29 --json` | 25 ask sweeps, $174M call |
| `uw options-flow sweeps --symbol NVDA --side bid --min-premium 100000 --top-n 25 --date 2026-05-29 --json` | 25 bid sweeps, $168M call |
| `uw options-flow top-premium-trades --symbol NVDA --top-n 25 --date 2026-05-29 --json` | 25 prints, call-dominated, underlying 215–217 |

## Tool errors

(none — all flow tools returned data.)

## Verdict for downstream phases

- **Net bias:** MIXED, weak-bullish (net_flow +$17.3M, call-tilted but
  aggressor-balanced; bullish bets faded into the close).
- **Conviction:** 2/5 (capped at `+` by phase-0.5 BUSY_NAME_NORMAL_DAY; weak edge,
  sweeps balanced, aggressive put-buying undercurrent, calls sold into).
- **Three datapoints later phases must remember:**
  1. Net flow is only **+$17.3M** with bullish/bearish premium near-balanced
     ($596M vs $579M) — the "$1B call premium" headline is misleading.
  2. **Calls were bought at 215–217 and the stock closed 211.14** — the bullish
     prints are already offside; intraday fade is a bearish tell.
  3. Bullish thread = fresh **215–230 Jun-5/Jun-26 calls**, but 0DTE-heavy and
     aggressor-balanced; there is a real **aggressive-put-buying undercurrent**
     (put ask−bid +$11.1M) and the day's largest OI build was a put (phase-3).
- **Open questions:** Is dark pool confirming accumulation into the dip or
  distribution (phase-2)? Does dealer gamma cap the 215–230 call zone or fuel it
  (phase-4)? The flow/price divergence from phase-0.5 deepened — calls bid, price
  faded.
