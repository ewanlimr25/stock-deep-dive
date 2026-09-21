# Phase 7 — UW Insights Confluence

**Ticker:** RDDT
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T00:00:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md,
phase-3-positioning.md, phase-5-historical.md, phase-6-macro.md

## Summary

UW's composite layer **refuses to score RDDT as a clean directional short — the
baseline is MIXED / low-conviction.** The conviction matrix returns **MIXED**
(confidence 6.88%): options flow confirms calls-sold / puts-bought, but dark pool
is balanced (buy_ratio 0.569). Institutional accumulation = **NEUTRAL** (buy/sell
1.32, "balanced"). Price-vs-flow shows **no divergence** — the bearish flow is
*aligned* with the −7.3% 30-day price slide, i.e. trend-confirming, not a reversal
tell. Most decisively, **RDDT does not appear in the bearish signal-confluence
top-30 even at min_score 1** — because it is missing the corroborating bearish
factors the composite wants: *no dp_distribution* (DP is mildly buying), *no
oi_building_puts* (calls are being written instead, phase-3), and *no high-IV
premium* (IV rank 18.7 is LOW). RDDT is **flow-bearish but confluence-weak.** The
one crisp, actionable output: with **LOW_IV + BEARISH_FLOW**, the UW playbook
prescribes a **Long Put / Put Debit Spread, 45–60 DTE** — exactly the cheap-vol,
premium-buying expression phases 4–5 pointed to. Phase-9 baseline: low-conviction,
mildly-bearish, debit-structured if traded at all.

## Key signals

- `conviction_matrix` **MIXED**, confidence **6.88%** — calls sold (ask 13,733 <
  bid 18,424) + puts bought (ask 15,946 > bid 12,777), DP balanced 0.569
  [INSIGHT:conviction_matrix]
- **RDDT ABSENT from bearish signal_confluence top-30** (min_score 1) — fails
  dp_distribution / oi_building_puts / high_iv confirmation [INSIGHT:signal_confluence]
- `institutional_accumulation` **NEUTRAL** (buy/sell 1.32, balanced) — tempers
  phase-2's block-tier accumulation [INSIGHT:institutional_accumulation]
- `price_vs_flow` **no divergence** — bearish flow aligned with −7.3% slide
  (trend-confirming, not reversal) [INSIGHT:price_vs_flow]
- `playbook` → **Long Put / Put Debit Spread, 45–60 DTE** (LOW_IV + BEARISH_FLOW)
  [INSIGHT:playbook_suggest_strategy]

## Detailed findings

### Deep dive snapshot (whole-tape aggregates) — [INSIGHT:insights_deep_dive]

(from phase-0.5 call; Yahoo fundamentals 401'd — no PE/short% from this tool, use
phase-7b/6 instead.)
- `bullish_premium` $14.07M vs **`bearish_premium` $21.04M**; `net_flow` **−$6.98M**
- `call_premium` $22.94M vs `put_premium` $15.14M (more call premium, but call-*sold*)
- `put_call_ratio` 0.9157; `iv_rank` 18.73; `total_open_interest` 447,744
- **`implied_move_perc` 0.00563 (0.56%)** — phase-9 N4 input (appears 1-session;
  IV-derived 5/29 weekly ≈ ±8%, 30d ≈ ±17.8%); `next_earnings` 2026-07-30
- Reconciles with phase-1 aggregate and phase-0.5 `[CTX]` (universe net-dir pctile
  0.5, self 0.0).

### Signal confluence — [INSIGHT:signal_confluence]

**RDDT not present** in the bearish top-30 (scores 4–5), which is led by FLO, FUTU,
OCS, EWY, BLDP, SMH (score 5). The 6 confluence factors are `bearish_flow`,
`high_pcr`, `volume_spike`, `dp_distribution`, `oi_building_puts`,
`high_iv_sell_premium`. RDDT has at most `bearish_flow` (+ borderline
`volume_spike`) but **lacks**:
- `dp_distribution` — DP is mild *buy* (phase-2), not distribution;
- `oi_building_puts` — phase-3 showed *calls being written*, no put OI build;
- `high_iv_sell_premium` — IV rank 18.7 is LOW, nothing rich to sell.
→ The composite ranks RDDT a **weak** bearish setup. This is the single strongest
internal confirmation that the "bearish" read is thin / not a high-conviction short.

### Conviction matrix — [INSIGHT:conviction_matrix]

Scenario **MIXED** (confidence 6.88%). DP buy_ratio 0.569 ("balanced — no clear
bias", between 0.4/0.6 thresholds). Options: call_ask 13,733 < call_bid 18,424
(net call selling); put_ask 15,946 > put_bid 12,777 (net put buying). The matrix
sees the same calls-sold/puts-bought tape as phase-1 but, with balanced DP, will
not classify it DIRECTIONAL_SHORT — it's MIXED. (Note: this all-tier DP 0.569
matches phase-2's *large*-tier 0.526; the 0.735 buy was only the 11-trade block tier.)

### Price vs flow — [INSIGHT:price_vs_flow]

**divergence: false** — "Price and flow are aligned." 30d: price_start 154.54 →
price_end 143.23 (−7.32%), period high 177.13 / low 139.55; flow bearish, P/C 0.92.
Bearish flow is **confirming** the downtrend, not diverging from it → **no reversal
signal here.** (This mildly counters the phase-5 "fade" thesis: flow and price agree.)

### Analyst vs flow — [INSIGHT:analyst_vs_flow]

Tool returned **only the flow side** (bearish, net −$6.98M, P/C 0.92) — analyst
consensus absent (Yahoo 401, consistent with deep_dive). Using phase-6 WebSearch for
the analyst side: **street bullish (avg PT ~$225, "Buy") vs flow bearish →
CONTRADICTION.** Wall Street and the options tape disagree — the defining tension of
this dive (see phase-6, phase-8b).

### Institutional accumulation — [INSIGHT:institutional_accumulation]

Signal **NEUTRAL** — "balanced dark pool activity." buy_sell_ratio 1.32 (buy 657k /
sell 498k), avg trade $142.58, VWAP $142.40, price −7.32% 30d. Top levels 141.7
($14.6M), 141.67 ($10.5M) — the phase-2 support zone. **Tempers phase-2:** whole-DP
is balanced/mild-buy, not decisive accumulation.

### Earnings play

**Skipped** — earnings 2026-07-30 is outside the 30-day window (phase-6 calendar).

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `insights_conviction_matrix` | symbol=RDDT | MIXED, 6.88%, DP 0.569 |
| `insights_price_vs_flow` | symbol=RDDT, 30d | no divergence, aligned bearish |
| `insights_institutional_accumulation` | symbol=RDDT | NEUTRAL, buy/sell 1.32 |
| `insights_analyst_vs_flow` | symbol=RDDT | flow only (bearish); analyst absent |
| `insights_signal_confluence` | bearish, min1, top30 | **RDDT absent** — weak bearish confluence |
| `playbook_suggest_strategy` | symbol=RDDT | Long Put / Put Debit Spread, 45–60 DTE |

## Tool errors

`insights_analyst_vs_flow` / `insights_deep_dive` Yahoo fundamentals 401 (analyst &
PE absent) — substituted phase-6 WebSearch analyst data. Not fatal.

## Cross-check vs phases 1–5

| UW insight | Phase agreement? | Notes |
|------------|------------------|-------|
| signal_confluence (RDDT absent) | **agrees** phase-3 (no put build) & phase-5 (weak edge) | confirms bearish-but-thin |
| conviction_matrix (MIXED) | **agrees** the phase-1-vs-phase-2 divergence | not directional short |
| institutional_accumulation (NEUTRAL) | **tempers** phase-2 (mild accum → neutral) | block-tier buy was the only strong skew |
| price_vs_flow (aligned) | **agrees** phase-1 bearish + downtrend | but counters phase-5 "fade" — flow confirms price |

## Verdict for downstream

- **UW composite bias:** **MIXED / mildly bearish, low conviction.** Flow is
  bearish and trend-aligned, but the multi-factor bearish confluence FAILS (DP not
  distributing, puts not building, IV low) → not a clean short.
- **Conviction:** 2/5.
- **Phase-9 baseline:** treat as **MIXED-bearish, low-conviction**; if the desk
  expresses the bearish lean, the instrument is a **Long Put / Put Debit Spread,
  45–60 DTE** (UW playbook; aligns with phase-4 cheap-puts + phase-5 premium-buying).
  Override only with specific contrary evidence from phases 7b/7c/8/8b.
- **Open questions:**
  - Reconcile the analyst-vs-flow contradiction (street $225 vs bearish tape): is
    the fundamental Meta-Forum threat (phase-6) bad enough to vindicate the flow over
    the street? → phase-7b fundamentals, phase-8b debate.
  - Does the NEUTRAL institutional read mean the phase-2 dip-buying was just
    liquidity provision absorbing the options selling, not conviction? → phase-8b.
