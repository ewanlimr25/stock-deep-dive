# Phase 3 — Open Interest & Positioning

**Ticker:** KWEB
**As-of date:** 2026-05-19
**Generated:** 2026-05-20T00:00:00Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md

## Summary

OI tells a more nuanced story than phase 1's bearish sweep persistence
[FLOW:sweep_persistence] or phase 2's mega-tier distribution
[DP:block_stratified]. The dominant OI moves describe an institutional
**range-defining premium-harvest** structure: a major **put SELL-to-open
at the 28 strike, May-29 expiry (OI +11,461, vol 11,585 on prev_bid_vol
6,300 vs prev_ask_vol 621)** [OI:biggest_increases / smart_positioning],
paired with **upside call OI being closed (Jun 33C −35,485)**
[OI:decrease_with_volume] and **upside call OI being written (Jun 30C
net ask-bid −6,018; Sep 35C −2,977; Jun 50C −355)**
[OI:smart_positioning]. A single same-day **call-roll** is detected:
near (≤30 DTE) call OI −14,284 vs far call OI +9,329 (roll_size 9,329,
balance 0.653) [OI:position_rolls]. Conclusion: institutions are
**capping upside at $30 and defending the $28 floor for May expiry** —
the bearish sweep tape from phase 1 partially resolves to call-
overwriting + roll-out, not unhedged shorting. Pin/cliff windows: KWEB
is **30 DTE from next OPEX (Jun 18)** so it does NOT appear in the
within-14-day pin risk list [OI:pin_risk]; OPEX concentration is well
spread (no 40%+ single-expiry cliff) [OI:opex_concentration].

## Key signals

- **28P (May 29 expiry, DTE 10): OI +11,461 (5.4×), $665K premium, prev
  bid_vol 6,300 vs ask_vol 621 → put SELL-to-open**
  [OI:smart_positioning] — *inferred_direction = bullish*. Strongest
  single new opening in the chain. Defines a hard $28 floor over the
  next 10 calendar days.
- **Jun 33C: OI −35,485** (from 147,098 to 111,613), volume 44,677
  [OI:decrease_with_volume] — **largest single OI move in the dataset**,
  closing of prior upside long-call position.
- **Jun 30C: OI +824 but net ask−bid −6,018, prev premium $757,679**
  [OI:smart_positioning] — heavy call writing at the $30 ceiling
  (consistent with phase-1 Jul 30C / Aug 35C / Sep 35C bid-side sweeps).
- **Position roll detected (calls only)**: near OI Δ −14,284, far OI Δ
  +9,329, roll_size 9,329, balance 0.653 [OI:position_rolls] — partial
  roll-out, not full liquidation. About 35% of near-term call OI
  retired permanently; 65% pushed to longer dated expiries.
- **Jan'27 15P: OI +6,929, prev ask_vol 6,734 vs bid_vol 923 → tail-
  risk put BUYING far OTM** [OI:smart_positioning] — structural tail
  hedge ~47% below spot, not directional intent.

## Detailed findings

### Largest OI increases [OI:biggest_increases / smart_positioning]

| Contract | DTE | Strike Δ% | Prev OI | Curr OI | OI Δ | Prev ask_vol | Prev bid_vol | Net ask−bid | Inferred dir |
|----------|-----|-----------|---------|---------|------|--------------|--------------|-------------|--------------|
| KWEB 260529 28P | 10 | -1.0% | 2,104 | 13,565 | **+11,461** | 621 | 6,300 | **-5,679** | bullish (put sell-to-open) |
| KWEB 260529 30.5C | 10 | +7.8% | 11,414 | 18,863 | +7,449 | 59 | 9 | +50 | bullish (call buy, low vol) |
| KWEB 270617 15P | 394 | -47% | 18,177 | 25,106 | +6,929 | 6,734 | 923 | +5,811 | bearish-tail (long-dated OTM put buy) |
| KWEB 260529 29.5C | 10 | +4.3% | 15,170 | 21,178 | +6,008 | 400 | 4,676 | **-4,276** | bearish (call write) |
| KWEB 260618 29C | 30 | +2.5% | 37,949 | 40,874 | +2,925 | 3,988 | 5,084 | -1,096 | bearish-lean |
| KWEB 260918 32C | 122 | +13% | 6,256 | 8,445 | +2,189 | 1,332 | 828 | +504 | bullish (call buy) |
| KWEB 260717 30C | 59 | +6.1% | 21,253 | 22,622 | +1,369 | 1,377 | 956 | +421 | bullish-lean |
| KWEB 270115 30C | 241 | +6.1% | 15,802 | 16,890 | +1,088 | 616 | 792 | -176 | bearish-lean |
| KWEB 260618 28C | 30 | -1.0% | 2,652 | 3,736 | +1,084 | 150 | 1,132 | -982 | bearish (ITM call write) |
| KWEB 260918 24P | 122 | -15% | 6,687 | 7,738 | +1,051 | 0 | 51 | -51 | bullish (put sell, small) |
| KWEB 260522 26.5P | 3 | -6.3% | 207 | 1,230 | +1,023 | 2 | 1,043 | -1,041 | bullish (near-zero-DTE put write) |
| KWEB 260918 29P | 122 | +2.5% | 20,030 | 20,972 | +942 | 714 | 228 | +486 | bearish (put buy at ATM) |
| KWEB 260918 35C | 122 | +24% | 19,665 | 20,583 | +918 | 13 | 2,990 | **-2,977** | bearish (far OTM call write) |
| KWEB 260618 30C | 30 | +6.1% | 97,738 | 98,562 | +824 | 4,319 | 10,337 | **-6,018** | bearish (call write at ceiling) |
| KWEB 260618 32C | 30 | +13% | 106,511 | 107,327 | +816 | 295 | 1,960 | -1,665 | bearish (call write) |
| KWEB 260612 32C | 24 | +13% | 676 | 1,471 | +795 | 864 | 12 | +852 | bullish (call buy) |
| KWEB 260618 50C | 30 | +77% | 34,206 | 34,856 | +650 | 197 | 552 | -355 | bearish (lottery write) |
| KWEB 260522 30C | 3 | +6.1% | 23,663 | 24,309 | +646 | 138 | 576 | -438 | bearish (call write) |
| KWEB 260717 35C | 59 | +24% | 60,258 | 60,893 | +635 | 895 | 532 | +363 | bullish-lean (lottery buy) |
| KWEB 260918 30C | 122 | +6.1% | 20,364 | 20,933 | +569 | 1,089 | 71 | +1,018 | bullish (call buy) |

**Tally:**
- Net bullish-inferred OI Δ: 11,461 + 7,449 + 2,189 + 1,369 + 1,084 + 1,023 + 795 + 635 + 569 = **+26,574**
- Net bearish-inferred OI Δ: 6,929 + 6,008 + 2,925 + 1,088 + 1,084 + 942 + 918 + 824 + 816 + 650 + 646 = **+22,830**
- Roughly balanced, but the **single largest opening (28P sold-to-open) is bullish-floor-defining**, and the **single largest CLOSE (Jun 33C, see below) is bearish-cap-removing**.

### Closing / roll activity [OI:decrease_with_volume / position_rolls]

| Contract | Curr OI | Prev OI | OI Δ | Volume | Notes |
|----------|---------|---------|------|--------|-------|
| KWEB 260618 33C | 111,613 | 147,098 | **−35,485** | 44,677 | Largest single close; OTM call unwind |
| KWEB 260618 35C | 79,347 | 82,337 | −2,990 | 4,451 | Continuing call unwind further OTM |
| KWEB 260618 31C | 167,252 | 168,050 | −798 | 4,237 | Modest unwind |
| KWEB 260821 41C | 5,991 | 6,685 | −694 | 1,227 | Slow unwind in Aug |
| KWEB 270115 33C | 11,635 | 12,041 | −406 | 4,317 | Modest Jan'27 |
| KWEB 260918 34C | 50,642 | 50,962 | −320 | 2,033 | Modest Sep |
| KWEB 260618 29P | 14,523 | 14,806 | −283 | 635 | Slight ATM put close |
| KWEB 261120 29P | 2,092 | 2,299 | −207 | 276 | Nov 29P close |
| KWEB 260529 32C | 53,595 | 53,797 | −202 | 243 | Weekly close |
| KWEB 261120 28P | 3,852 | 4,027 | −175 | 371 | Nov 28P close |

**Position roll detection** [OI:position_rolls] returns ONE roll —
**calls, near (≤30 DTE) Δ −14,284, far Δ +9,329, balance 0.653**. This
tells us ~65% of near-term call OI that left the chain was rolled
further out (likely from Jun 33C → Sep/Jan calls); the remaining ~35%
was a net liquidation.

### Smart positioning summary [OI:smart_positioning]

Top 20 OI changes with inferred direction:

- **Bullish-inferred contracts (9):** 28P 260529 (+11,461), 30.5C 260529
  (+7,449), 32C 260918 (+2,189), 30C 260717 (+1,369), 24P 260918
  (+1,051), 26.5P 260522 (+1,023), 32C 260612 (+795), 35C 260717
  (+635), 30C 260918 (+569).
- **Bearish-inferred contracts (11):** 15P 270617 (+6,929, tail), 29.5C
  260529 (+6,008), 29C 260618 (+2,925), 30C 270115 (+1,088), 28C 260618
  (+1,084), 29P 260918 (+942), 35C 260918 (+918), 30C 260618 (+824),
  32C 260618 (+816), 50C 260618 (+650), 30C 260522 (+646), 32C 260618
  (+816).

**Critically:** of the 11 "bearish" contracts, **9 are call sells** (bid-
heavy call OI opens = call writing, NOT directional shorting). Only
**Jan'27 15P (tail hedge), Sep'26 29P (ATM put buy), and a small May
22 30C (3 DTE)** are bona-fide bearish opens. Strip out the call-writes
and the OI-led bias **flips to BULLISH-skewed range-defining**.

### Pin risk [OI:pin_risk]

KWEB is **NOT in the top 25 within-14-day pin-risk list**. Next OPEX
(Jun 18) is 30 DTE — outside the rubric's default 7-day window. Note:
the May-29 weekly expiry (DTE 10) is technically within 14 days but
KWEB's strike-cluster mass is too diffuse to outscore SPY/IWM/QQQ/HYG.

For reference: tickers WITH ETF-relevant pin scores nearby —
- **HYG (high-yield) pin_score 1,512,476 at $78 strike** (junk-bond
  proxy, market risk-off mirror)
- **EEM (broad emerging) pin_score 399,754 at $65** (KWEB's parent
  EM index)
- **FXI (China large-cap) pin_score 322,681 at $37, dte 3** — direct
  China-proxy pin
These are macro context for phase 6.

### OPEX concentration [OI:opex_concentration]

KWEB is **NOT in the top 30 most-concentrated list** (which is dominated
by small-caps with 100% single-expiry concentration). KWEB's OI is
**broadly spread** across 2026-05-22, 2026-05-29, 2026-06-12, 2026-06-
18, 2026-07-17, 2026-08-21, 2026-09-18, 2026-11-20, 2027-01-15, 2027-
06-17, which means no single OPEX cliff dominates dealer positioning —
this matters for phase 4 (dealer gamma will spread its sensitivity
across expiries rather than pinning one).

## Tool calls (audit trail)

| Tool | Args | Result |
|------|------|--------|
| `oi_biggest_increases` | `{symbol: KWEB, top-n: 20, min-oi-change: 500, date: 2026-05-19}` | 20 rows |
| `oi_decrease_with_volume` | `{symbol: KWEB, top-n: 15, min-volume: 100, date: 2026-05-19}` | 15 rows |
| `oi_smart_positioning` | `{symbol: KWEB, top-n: 20, min-oi-change: 500, date: 2026-05-19}` | 20 rows |
| `oi_position_rolls` | `{symbol: KWEB, threshold: 500, near-dte-max: 30, date: 2026-05-19}` | 1 row |
| `oi_pin_risk` | `{top-n: 25, dte-max: 14, max-distance-pct: 5, date: 2026-05-19}` | 25 rows; KWEB absent |
| `oi_opex_concentration` | `{top-n: 30, min-concentration-pct: 40, date: 2026-05-19}` | 30 rows; KWEB absent |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** **range-defining premium-sale structure**;
  net mildly bullish on the floor (28P sold-to-open) and bearish-
  capping on the upside ($30 / $33 calls). NOT a unidirectional setup.
- **Conviction:** 3 / 5 — strongest single signal (28P short, 11,461 OI
  +5×) is genuinely directional-bullish at the $28 level; the 33C
  closing is genuinely directional-bearish at the upside. Together
  they describe a range trade, not a trend.
- **Three pin/cliff strikes for phase 9:**
  1. **$28.00** — institutional put-write floor (May 29 expiry; 28P
     short OI 13,565). If spot breaks $28 ahead of 5/29 with no
     covering bid, that's a thesis-broken event for the floor.
  2. **$30.00** — call-write ceiling (Jun 30C OI 98,562, net ask−bid
     −6,018 today; May 30.5C OI 18,863). Strong dealer cap.
  3. **$33.00** — former cap, now neutralized by the −35,485 OI close
     today. Bears removing upside hedges suggests they NO LONGER expect
     a print there in June — but this also REMOVES dealer short-gamma
     overhang at $33, freeing the path up if a catalyst arrives.
- **Open questions:**
  - **Reconciliation with phase 1**: Phase-1 sweep persistence
    ($94.9M bearish over 5 days) was almost certainly dominated by
    bid-side call selling (overwriting) and put-writing (premium sale)
    — both of which print as "bearish" in raw sweep tape but are
    actually **range-defining / mildly bullish** structurally. Phase 10
    audit must explicitly flag this and decide whether to weight
    persistence as bear-signal (raw) or range-signal (parsed).
  - **Reconciliation with phase 2**: Two mega DP prints at -$25.87M
    total cannot be explained by call-overwriting alone (those would
    NOT cause big block stock sales). The mega DP sells imply at least
    SOME actual underlying-share liquidation, not just options writing.
    Phase 7 / 8 must reconcile whether this is one fund de-risking
    spot exposure while another fund opens the put-write floor.
  - Is the +6,929 OI Jan'27 15P a tail-hedge from a *long-stock* holder
    (bullish underlying conviction + cheap insurance) or a directional
    catastrophe bet? The OI smart-positioning labels it bearish; we
    weight it as **structural tail hedge, NOT bearish flow**.
