# Phase 4 — Dealer Structure & Gamma

**Ticker:** SNOW
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T15:55:00Z
**Upstream phases cited:** phase-2-dark-pool.md, phase-3-positioning.md, phase-0.5-context.md

## Summary

The structure is textbook **pre-earnings long-gamma pin sitting on top of a priced
binary**. Dealers are net **long gamma** (total GEX **+40.7M**, regime POSITIVE,
spot $172.16 far above ZGL $78.8), with a **dominant +$23.8M gamma wall at $172.5**
that mechanically pins price near spot *until* the 5/27 event [STRUCT:gex]
[STRUCT:today_gamma_flip]. Above, gamma walls at **$185** (matches the phase-3 185C
long OI) and **$200** (matches the 200C call-writing cap) are the upside steps
[STRUCT:gex]. The term structure is **steep earnings backwardation** — 5/29 IV
122.9% vs 6/18 84.5% vs back-end ~65%, front/far ratio **1.29** [STRUCT:iv_term_structure]
[STRUCT:front_end_iv_ratio]. The **5/29 ATM straddle ($23.35) implies a ≈ ±13.3%
earnings move** (range ~$149–$195) [STRUCT:gex DUCKDB] — the number phase-0.5 flagged
the screener couldn't give. Two forward-looking warnings: net **vanna is negative
(−2,294)**, so the post-earnings IV crush will force **mechanical dealer SELLING**
[STRUCT:vanna_charm]; and 30-day skew is **COMPLACENT** (calls richer than puts,
ratio 0.99) — upside calls are expensive and there is little put-protection bid
[STRUCT:term_skew].

## Key signals

- **Long-gamma pin at $172.5:** +$23.8M net GEX, the dominant wall = price magnet
  into earnings; expect chop/mean-reversion $170–175 pre-event [STRUCT:gex].
- **Earnings expected move ≈ ±13.3% (±$23):** 5/29 ATM straddle 172.5C $11.42 +
  172.5P $11.93 = $23.35 on spot ~$172 → post-print range **~$149–$195**
  [STRUCT:gex DUCKDB].
- **Steep backwardation, ratio 1.29:** 5/29 IV 122.9% → 6/18 84.5% → LEAP ~65%; the
  front is pricing a large event, vol is rich [STRUCT:iv_term_structure].
- **Negative net vanna (−2,294):** post-earnings IV crush → dealers cut long hedge →
  **mechanical selling pressure** after the print [STRUCT:vanna_charm]. Long-premium /
  long-stock holders face a vol-crush + vanna-unwind double headwind.
- **COMPLACENT skew:** 25Δ call IV 79.3% ≥ put IV 78.6% (skew −0.0077) — call-demand
  tilt, no tail-hedge bid [STRUCT:term_skew]; consistent with phase-1/3 upside-call
  buying but means downside is *under*-protected if the print disappoints.

## Detailed findings

### GEX (DTE ≤ 45) [STRUCT:gex]

- `total_gex` **+40,693,652** · `regime` **POSITIVE** (dealers long gamma →
  mean-reversion, suppressed realized vol) · `zero_gamma_level` 78.8 · spot $172.16.
- Top positive walls: **$172.5 +$23.78M** (dominant pin) · $185 +$1.67M · $175
  +$1.33M · $180 +$1.43M · $200 +$2.40M · $170 +$4.71M · $190 +$0.87M · $210 +$0.61M.
- Negative GEX below: $140 −$0.49M, $145 −$0.10M, $135 −$0.14M (deep-OTM put mass —
  source of the low ZGL; small in dollar terms).
- The +$23.8M concentration at $172.5 is why ZGL ($78.8) is academic pre-earnings:
  the *practical* pin is $172.5. **The 5/27 binary overrides the pin** — once OI
  expires/crushes through earnings, the long-gamma magnet dissolves.

### DEX [STRUCT:dex]

`net_dex` +691.7M (call_dex +886M, put_dex −195M). Public is net call-long → dealers
net short calls → standing hedge is to **BUY underlying** (mild supportive bid in
normal tape). Note this is the *pre-earnings* hedge; the vanna mechanic below
reverses it post-print.

### Vanna + charm [STRUCT:vanna_charm]

`net_vanna` **−2,294** (call-heavy book), `net_charm` +116,920. Interpretation:
**falling IV → call delta drops → dealers (short calls) cut their long-underlying
hedge → SELLING pressure.** Earnings 5/27 guarantees a large IV drop on 5/28–5/29
(122.9% → realized), so the vanna unwind is a **mechanical post-earnings headwind** —
critical for any structure held through the print. No bullish vanna-squeeze setup
here (that needs *rising* IV).

### IV term structure & front-end ratio [STRUCT:iv_term_structure][STRUCT:front_end_iv_ratio]

**BACKWARDATION**, monotonic from the front: 5/22 198.2% (0DTE artifact) · **5/29
122.9%** · 6/5 102.9% · 6/12 90.8% · **6/18 84.5%** · 6/26 79.8% · 7/17 71.4% · LEAP
62–68%. Front/far ratio **1.29** (near 10DTE 102.9% vs far 31DTE 79.8%) = event
stress. `kink_expiry` null (smooth decay, not a single isolated kink — the whole
front curve is bid for the event). Long premium in 5/29 pays ~123% IV that collapses
to the ~65% baseline within days of the print.

### Term skew (31 DTE) [STRUCT:term_skew]

`call_25d_iv` 0.7934 vs `put_25d_iv` 0.7857 → skew **−0.0077**, ratio 0.99,
**COMPLACENT**. Calls marginally richer than puts — a call-demand skew (consistent
with the 185C/upside buying), and notably *no* put-protection premium. Downside is
cheap to hedge but no one is — if earnings disappoints, the lack of a put bid means
skew can snap and the move down can overshoot.

### Today's gamma flip (EOD 5/22 snapshot) [STRUCT:today_gamma_flip]

Regime POSITIVE, today_total_gex +31.3M, today_zero_gamma 78.8. Key 0DTE walls:
**172.5 (support_wall, GEX 23.7M)**, 170, 175, 167.5, 160. (After-hours snapshot for
the 5/22 expiry — confirms the $172.5 pin held into the Friday close.)

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `options_structure_gex` | symbol=SNOW, dte_max=45 | +40.7M, POSITIVE, ZGL 78.8, $172.5 +$23.8M wall |
| `options_structure_dex` | symbol=SNOW, dte_max=45 | net_dex +691.7M; dealers buy underlying (pre-event hedge) |
| `options_structure_vanna_charm` | symbol=SNOW, dte_max=45 | net_vanna −2,294 → post-crush dealer selling |
| `options_structure_iv_term_structure` | symbol=SNOW | BACKWARDATION; 5/29 122.9% → LEAP ~65% |
| `options_structure_term_skew` | symbol=SNOW, dte_target=30 | COMPLACENT, call≥put IV, ratio 0.99 |
| `options_structure_front_end_iv_ratio` | symbol=SNOW, near=7 far=30 | ratio 1.29, BACKWARDATION |
| `options_structure_today_gamma_flip` | symbol=SNOW | $172.5 support wall, POSITIVE |
| DuckDB (ATM straddle) | 5/29 & 6/18 near-ATM VWAP | 5/29 ATM straddle $23.35 → ±13.3% earnings move |

## Tool errors

(none)

## Verdict for downstream phases

- **Dealer regime:** **LONG GAMMA (pinned at $172.5) pre-earnings → discontinuity at
  5/27.** Pre-event: suppressed vol, mean-reversion, $170–175 chop. Through-event:
  pin dissolves, expected ±13.3% move, and the **negative-vanna IV-crush mechanic
  adds dealer selling** on the other side.
- **Conviction:** **4/5** on the structural read (clean long-gamma, clean
  backwardation, clean vanna mechanic — all corroborate each other and phases 2–3).
- **Three structural levels for phase-9:**
  1. **$172.5 — gamma pin / pivot** (+$23.8M wall = pre-earnings magnet; also the
     phase-2 DP spot node). The fulcrum the trade is built around.
  2. **$185 — upside gamma wall & first earnings target** (+$1.67M GEX, the phase-3
     185C long-OI strike; +7.5%, inside the +13% expected move).
  3. **$200 — upside cap** (+$2.40M GEX, the phase-3 200C writing wall; +16%, just
     beyond the expected move) // downside: **$150 ≈ −13%** is the straddle-implied
     floor, coinciding with the phase-2 $163–167 shelf just above it.
- **Open questions:**
  - Does SNOW's *historical* earnings move match the priced ±13%? (over/under-priced
    vol → sell vs buy the event) → phase-5 + phase-7b earnings history.
  - Is the macro/sector regime calm enough for the long-gamma pin to hold into the
    print? → phase-6.
  - Given rich front IV (123%) + negative vanna, is long premium even the right
    vehicle, or is a defined-risk spread / premium-selling structure better? →
    phase-9 strategy selection.
