# Phase 4 — Dealer Structure & Gamma

**Ticker:** ENPH
**As-of date:** 2026-05-19 (effective UW date 2026-05-15)
**Generated:** 2026-05-19T00:00:00-04:00
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md

## Summary

Dealers are in a **strongly positive-gamma regime** with **total GEX ~$4.42B
and the per-strike gamma profile dominated by a single $50 wall worth
~$2.78B in net_gex** [STRUCT:gex] — the heaviest gamma node on the chain by
two orders of magnitude. Zero-gamma level is **$15.01**, well below the
$51.37 reference spot, so dealers are unambiguously long-gamma and will
sell rallies / buy dips → suppressed realized vol, mean-reversion bias
intraday. **DEX is +$92.3B, public is net call-long, so dealers are
net short calls and will MECHANICALLY BUY underlying as spot rises**
[STRUCT:dex] — a positive feedback loop for the bull thesis. The single
biggest **structural flag is the front-end IV term structure**:
**5/22 expiry IV averages 121% versus 96% at the next monthly (6/18)**, a
**front-end IV ratio of 1.057 = BACKWARDATION** [STRUCT:front_end_iv_ratio]
[STRUCT:iv_term_structure]. That **121% near-week IV spike strongly implies
a binary catalyst within the 5/15→5/22 window** — phase-6 must investigate
(likely earnings, possibly tariff/IRA policy event, possibly analyst day).
**25-delta skew is INVERTED (calls richer than puts, skew = −0.10,
COMPLACENT regime)** [STRUCT:term_skew] — extremely unusual for an equity
and consistent with **chase-style upside demand** rather than tail-hedging.

## Key signals

- **Total GEX +$4,424,496,657 (POSITIVE regime), ZGL $15.01, spot $51.37**
  [STRUCT:gex] — long-gamma, mean-reverting, intraday vol suppressed.
- **$50 strike GEX +$2,782,892,560** [STRUCT:gex] — by far the largest
  gamma wall on the chain, the dealer hedging pivot. Spot above $50 keeps
  the bullish dealer-hedging tailwind live.
- **Net DEX +$92.3B, call-heavy public → dealer hedge is to BUY underlying
  on rallies** [STRUCT:dex] — mechanical tailwind for trending up.
- **5/22 expiry IV 121.3% vs 6/18 IV 96.2% → front_end_iv_ratio 1.057
  BACKWARDATION** [STRUCT:front_end_iv_ratio][STRUCT:iv_term_structure] —
  **CATALYST EVENT EXPECTED IN THE 5/15→5/22 WINDOW**.
- **25Δ skew −0.10 (calls richer than puts, COMPLACENT)**
  [STRUCT:term_skew] — chase-style upside premium demand, atypical for
  equities, consistent with phase-1 ask-side call sweeping.

## Detailed findings

### GEX (total + per-strike top 10 + zero gamma level)

- **Regime:** POSITIVE — "Dealers net long gamma — expect mean-reversion
  and reduced volatility."
- **Total GEX:** +$4,424,496,657
- **Zero gamma level (ZGL):** $15.01
- **Underlying reference price:** $51.37 (close 2026-05-15)
- **Spot vs ZGL:** $51.37 / $15.01 = spot is **3.4× above ZGL** — deeply
  inside long-gamma territory.

Top gamma walls (net_gex by strike, positive = support / negative = short-
gamma / momentum activator):

| Strike | net_gex ($) | Role |
|---|---|---|
| **50** | **+2,782,892,560** | **Dominant call-wall / support pivot** |
| 45 | +82,248,733 | Secondary call-wall / floor |
| 46 | +7,377,279 | Tertiary support |
| 49 | +2,788,272 | At-spot support cluster |
| 48 | +1,405,198 | Support cluster |
| 42 | +1,044,650 | Lower-zone support |
| 48.5 | +735,490 | Cluster |
| 47 | +712,256 | Cluster |
| 43 | +575,469 | Lower support |
| 41 | +352,666 | Lower support |
| **30** | **−18,190,140** | **Short-gamma trap below** |
| **35** | **−9,825,466** | **Short-gamma trap below** |
| 40 | −1,809,017 | Short-gamma transition zone |
| 25 | −814,082 | Deep short-gamma |
| 29 | −186,663 | Deep short-gamma |

**Reading:**
- $50 is the most important price in this dataset. Holding $50 = positive
  dealer hedge feedback for the bull case.
- A break below ~$40 transitions dealers into short-gamma territory; below
  $35 the regime fully flips and momentum amplifies downside.
- Above $50, every dollar higher creates more dealer call-short delta to
  hedge → buying pressure increases.

### DEX (net dealer delta)

- **call_dex:** +$94,428,071,716
- **put_dex:** −$2,132,843,128
- **net_dex:** **+$92,295,228,588**
- Interpretation: "Public is net call-long → dealers net short calls →
  dealer hedge is to BUY underlying."

**Reading:** the public's call book is essentially the entire delta
exposure on this chain. Put-side delta is negligible (~2% of call delta).
Dealers must **systematically buy stock as ENPH rises** — and conversely
sell as it falls (mean-revert). This is the structural reason for the
positive-gamma squeeze potential in a bull trend.

### Vanna + charm (squeeze regime detection)

- **net_vanna:** **−2,161,896**
  - call_vanna −2,204,305 / put_vanna +42,409
- **net_charm:** **+28,487,647**

Vanna interpretation (verbatim from tool): "Public net vanna negative
(call-heavy book). Falling IV → call delta drops → dealers (short calls)
cut long-underlying hedge → SELLING pressure. Rising IV reverses."

**Reading:**
- **If IV expands** (e.g., into the 5/22 event): dealers must buy more
  underlying to maintain hedge → **vanna-driven up squeeze**.
- **If IV collapses post-event** (typical earnings vol-crush): dealers
  cut their long-stock hedge → **mechanical selling pressure**.
- **Charm is positive and large (~$28.5M)**: time decay favors dealer
  positioning, supporting drift higher into expiry baseline as long as
  spot stays above $50 wall.

This is a **two-edged structural setup**:
1. Pre-event: rising IV + ask-side call buying = vanna squeeze risk to
   upside (good for bulls).
2. Post-event: IV crush = mechanical dealer unwind = pullback risk
   regardless of direction of the catalyst.

### IV term structure (regime + slope)

`options_structure_iv_term_structure` (16 expiries):

| Expiry | DTE | Avg IV % | Note |
|---|---|---|---|
| 2026-05-15 | 0 | 29.2% | Expiring (mechanical) |
| **2026-05-22** | **7** | **121.3%** | **EVENT SPIKE — catalyst window** |
| 2026-05-29 | 14 | 101.6% | Decaying from event |
| 2026-06-05 | 21 | 102.5% | |
| 2026-06-12 | 28 | 93.4% | |
| **2026-06-18** | **34** | **96.2%** | Monthly OPEX (heavy OI) |
| 2026-06-26 | 42 | 91.9% | |
| 2026-07-17 | 63 | 87.7% | |
| 2026-08-21 | 98 | 93.2% | |
| 2026-09-18 | 126 | 88.7% | |
| 2026-11-20 | 189 | 85.9% | |
| 2026-12-18 | 217 | 81.3% | |
| 2027-01-15 | 245 | 84.5% | LEAP campaign tier |
| 2027-06-17 | 398 | 82.8% | Phase-1 combo expiry |
| 2028-01-21 | 615 | 81.3% | LEAP |
| 2028-12-15 | 944 | 79.9% | LEAP |

**Structure label:** "CONTANGO" (back-month 79.9% < non-event nearby term
~96%) — but the **5/22 121% spike is a clear earnings-style kink** that
the tool's kink detector missed (kink_expiry: null). **Treat the chain as
KINKED-AT-5/22**.

Phase-6 must confirm what's on the calendar for 2026-05-18 → 2026-05-22.
(Possible candidates: Q1 2026 earnings if pushed late; IRA / residential-
solar policy announcement; tariff decision; analyst day. Investigate.)

### Term skew (25Δ put vs call IV at DTE 30)

- **call_25d_iv:** 0.9914 (99.1%)
- **put_25d_iv:** 0.8908 (89.1%)
- **skew:** **−0.1005** (calls richer than puts by ~10 IV points)
- **skew_ratio:** 0.899
- **interpretation:** **COMPLACENT**

This is a **highly unusual reading** for an equity (normal equity skew is
puts > calls by 2–8 IV points). Inverted call-rich skew on ENPH means:
- The marginal demand is for upside calls, not downside puts.
- Tail-hedging by long holders is minimal — they're either underhedged
  or have rotated hedges into the LEAP put leg (Jun-2027 $45P).
- Combined with positive-gamma regime and ask-side call sweeping
  (phase-1), this signals **trend-chase positioning** with the underlying.

### Front-end IV ratio (event-stress signal)

- **near_iv:** 1.0162 (DTE ~10, average of 5/22 and 5/29)
- **far_iv:** 0.9616 (DTE 30, the 6/18 monthly)
- **ratio:** **1.057** → **BACKWARDATION**

Confirms the term-structure event spike. **Backwardation with positive
gamma + call-rich skew + ask-side flow is the signature of "expecting a
binary upside catalyst" — the market is paying up for short-dated calls
and accepting normal-priced puts because the consensus directional bias
is to the upside through the catalyst window.**

### Today's gamma flip (0DTE 5/15)

`options_structure_today_gamma_flip` (today_expiry=2026-05-15):

- regime: POSITIVE
- today_total_gex: $10,366,083,305
- **today_zero_gamma: $29.53** (well below spot $51.18)
- atm_flip_strike: $19 (mechanical extreme — discount)

Today's walls (0DTE only):

| Role | Strike | gex ($) |
|---|---|---|
| **support_wall** | **50** | **9,312,858,413** |
| support_wall | 55 | 908,026,011 |
| support_wall | 45 | 93,859,677 |
| support_wall | 40 | 33,155,167 |
| support_wall | 42 | 3,732,143 |

**Note:** the tool returned only support walls and no resistance walls,
meaning upside hedging was unconstrained by 0DTE OI for 5/15. Consistent
with the late-session rally to $53.50.

This 0DTE snapshot is now expired (the data is end-of-Friday). For the
next session (Monday 5/18 / Tuesday 5/19), the **same $50 wall persists
via the 6/18 expiry which holds 26,273 contracts** [OI:biggest_increases].

### Cross-check vs phases 1–3

| Phase-1/2/3 claim | Phase-4 confirms? |
|---|---|
| Bullish ask-side sweeps in $50–$65 calls | **Confirmed**: skew inverted (call-rich), DEX call-heavy, positive gamma at $50. |
| Dark pool accumulation $48–$54 | **Confirmed**: $50 = massive gamma wall = dealer hedging center inside the DP cluster. |
| OI roll-up Jun $45→$50/$55 | **Confirmed**: $50 wall is the largest single-strike GEX in the dataset. |
| Long-dated bullish combo Jun-2027 70C/45P | **Implicit confirm**: positive charm + negative call-vanna → dealers benefit from time + suffer if IV rises — the LEAP combo benefits from BOTH directions of that asymmetry. |

## Tool calls (audit trail)

| Tool | Args | Result summary |
|---|---|---|
| `mcp__uw-pp__options_structure_gex` | symbol=ENPH, date=2026-05-15, dte_max=45 | Total GEX +$4.42B, $50 wall +$2.78B, ZGL $15.01, POSITIVE |
| `mcp__uw-pp__options_structure_dex` | symbol=ENPH, date=2026-05-15, dte_max=45 | Net DEX +$92.3B, dealers hedge BUY on rallies |
| `mcp__uw-pp__options_structure_vanna_charm` | symbol=ENPH, date=2026-05-15, dte_max=45 | net_vanna −2.16M / net_charm +28.5M |
| `mcp__uw-pp__options_structure_iv_term_structure` | symbol=ENPH, date=2026-05-15 | 16 expiries; 5/22 IV 121% spike (catalyst); CONTANGO label with KINK |
| `mcp__uw-pp__options_structure_term_skew` | symbol=ENPH, date=2026-05-15, dte_target=30 | Skew −0.10, COMPLACENT (calls richer) |
| `mcp__uw-pp__options_structure_front_end_iv_ratio` | symbol=ENPH, date=2026-05-15, near_dte=7, far_dte=30 | ratio 1.057, BACKWARDATION |
| `mcp__uw-pp__options_structure_today_gamma_flip` | symbol=ENPH, date=2026-05-15 | $50 dominant 0DTE support wall; today_zero_gamma $29.53 |

## Tool errors

None.

## Verdict for downstream phases

- **Dealer regime:** **LONG-GAMMA, BULLISH BIASED** — call-heavy public,
  inverted skew, dealers mechanically buy on rallies, $50 wall holds.
- **Conviction:** **4 / 5** — would be 5/5 absent the post-event vol-crush
  unwind risk.
- **Three structural levels for phase-9:**
  1. **$50 — primary support pivot** (gamma wall $2.78B; spot above
     $50 keeps the bullish dealer-feedback live; lose $50 and the squeeze
     fades).
  2. **$45 — secondary support** (gamma wall $82M; loss of $45 starts
     the transition toward short-gamma territory below $40).
  3. **$40 — short-gamma activation line** (below $40 dealers go net
     short gamma; momentum amplifies, downside accelerates).
  - Bonus: **ZGL $15** is the deep bear cliff but not actionable.
- **Critical flag for phase-6 and phase-9:**
  - **5/22 expiry IV 121.3% = binary catalyst within 7 days.** Phase-6
    MUST identify what the market is pricing. Phase-9 must NOT pick an
    expiry that prices through the event without intentional vol-play
    consideration. Recommended: structure trades either (a) before the
    event with short-dated debit calls that capture the IV expansion +
    vanna squeeze, or (b) after the event with longer-dated structures
    that miss the IV crush.
- **Open questions:**
  - What is the 5/22 catalyst? (phase-6)
  - Is the inverted skew a sign of overcrowded long positioning?
    (phase-5 P/C z-score + phase-7 conviction matrix + phase-8
    contrarian-scanner).
