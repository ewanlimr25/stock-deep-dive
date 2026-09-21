# Phase 2 — Dark Pool & Block Prints

**Ticker:** OKLO
**As-of date:** 2026-07-17
**Generated:** 2026-07-18T00:00:00Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md, phase-1-flow.md

## Summary

Dark-pool activity is **mixed / mild-distribution-into-support**. Today's large-tier
prints ($28.4M premium) lean 61% buy — some dip-buying at ~$41 — but the single
block-tier print ($1.03M) was a **sell** and there are **no mega-tier blocks**. The more
telling read is the 5-day price-level map: the heaviest institutional clusters sit
**above spot at $45.5–$46.2 (~$40M combined)** while price has since fallen to **$41.11**
— overhead supply consistent with phase-1's 5-session bearish sweep campaign. OKLO is
**outside the dark-pool ticker-summary top-30**, so none of this is unusual size for the
tape. Block sizes (≤25K shares ≈ 0.014% of ~174M shares out) are **small for the name** —
low conviction on the individual prints.

## Key signals

- **5-day DP supply overhead**: heaviest clusters at **$46.24 ($17.2M / 373K sh)** and
  **$45.81 ($11.4M)** — well above the $41.11 spot; price fell away from them [DP:price_levels]
- **Large tier mildly buy**: `large.buy_ratio=0.611` on $28.4M premium (suggestive dip-buy,
  not high-confidence) [DP:block_stratified]
- **Block tier sold**: the one ≥$1M block was `buy_ratio=0` (a sell), $1.03M [DP:block_stratified]
- **No mega prints; OKLO outside DP ticker-summary top-30** — not an unusual DP day [DP:ticker_summary]
- **After-hours block**: $41.11 × 24,000 = $986K at 21:54 (closing-cross-type print) [DP:extended_hours]

## Detailed findings

### Largest blocks — [DP:largest]

| Price | Size | Premium | Time | NBBO | Read |
|---|---|---|---|---|---|
| 41.21 | 25,000 | $1,030,250 | 14:27 | 41.21/41.26 | at bid → sell lean |
| 39.98 | 24,997 | $999,380 | 13:45 | 39.98/40.04 | at bid → sell lean |
| 42.20 | 23,538 | $993,303 | 16:59 | 42.18/42.19 | above ask → buy |
| 41.11 | 24,000 | $986,640 | 21:54 (AH) | 40.99/41.25 | mid/AH cross → neutral |
| 41.80 | 21,600 | $902,880 | 15:56 | 41.48/41.50 | above ask → buy |
| 41.56 | 21,600 | $897,696 | 15:57 | 41.40/41.48 | above ask → buy |

Prints span **$39.8–$42.3**, straddling spot. NBBO context is genuinely mixed —
sells at the lower blocks (39.98, 41.21), buys at 41.6–42.2. No one-sided footprint.
Largest single block = 0.014% of ~174M shares out → **not a conviction-size print**.

### Tier breakdown — [DP:block_stratified]

| Tier (boundary) | buy_ratio | derived sell | total_premium |
|---|---|---|---|
| large (≥$100K) | **0.611** | 0.389 | $28,423,209 |
| block (≥$1M) | **0.000** | 1.000 | $1,030,250 |
| mega (≥$10M) | — | — | $0 (none) |
| retail (<$100K) | — | — | $0 |

Read: broad large-tier flow is a mild **buy (0.611, in the 0.55–0.7 "suggestive only"
band)** — retail-adjacent dip-buying at $41 — but the one true block-size print was a
sell and there is **no mega-tier conviction**. Net: balanced-to-mild-distribution.

### Price levels (5-day clusters, 07-13→07-17) — [DP:price_levels]

| price_level | total_premium | shares | zone |
|---|---|---|---|
| **46.24** | $17,244,534 | 372,935 | **overhead resistance** |
| **45.81** | $11,431,747 | — | overhead resistance |
| 45.69 / 45.55 / 45.60 | $6.5M / $3.4M / $2.0M | — | overhead resistance |
| **41.81 / 41.80 / 41.56** | $6.7M / $2.2M / $2.6M | — | **near-spot pivot** |

Two zones: a **heavy supply shelf at $45.5–$46.2 (~$40M+ combined)** now above spot, and a
**moderate $41.5–$41.8 pivot** at spot. The stock traded up into the $45–46 shelf earlier
in the window and has since fallen to $41.11 — those upper prints are now resistance and,
given the concurrent bearish sweeps (phase-1), read as distribution near the highs.

### Extended-hours — [DP:extended_hours]

14 prints; largest = $41.11 × 24,000 ($986K, 21:54 after-hours cross) and $40.9999 ×
14,800 ($607K, 11:42 pre-market). These are near-spot and look like closing-cross /
liquidity prints rather than directional accumulation — de-rate. No pre-catalyst
hedging spike (earnings not until 2026-08-10).

## Tool calls (audit trail)

| Command | Key value(s) ← `jq` path | Rows |
|---|---|---|
| `dark-pool largest --sort-by premium --top-n 25` | top block $1.03M @41.21 at bid ← `.results[0]` | 25 |
| `dark-pool block-stratified --min-tier large` | large.buy 0.611 / block.buy 0.0 ← `.results[0].large.buy_ratio` | tiers |
| `dark-pool price-levels --days 5` | $46.24 = $17.2M ← `.results[0].price_level/total_premium` | 15 |
| `dark-pool extended-hours --top-n 15` | $986K AH @41.11 ← `.results[0]` | 14 |
| `dark-pool ticker-summary --top-n 30` | OKLO outside top-30 ← filtered `.results[]` | 0 (OKLO) |

## Tool errors

None. All reads round-tripped through `jq`.

## DATA NOTE / CORRECTION

`price-levels` `price` field is `null`; correct field is **`price_level`** (re-queried,
no value transcribed before correction). `Shs Float` unavailable from `fz` this run
(phase-0) → %-of-float uses shares-outstanding proxy (~174M = MktCap $7.15B / $41.11),
flagged advisory, not float-exact.

## Verdict for downstream

- **Bias:** MIXED — mild-distribution / balanced. Overhead supply + bearish sweeps vs a
  weak large-tier dip-buy at spot.
- **Conviction:** 2 / 5 (small block sizes, no mega prints, OKLO not a DP leader).
- **Largest block as % of float:** **~0.014%** of shares-outstanding proxy (~174M;
  true float n/a) — **not meaningful size for this name**; advisory only.
- **Three S/R levels for phase-9:**
  1. **Resistance $45.5–$46.2** — heavy 5-day DP supply shelf (~$40M), now overhead.
  2. **Pivot/near-support $41.5–$41.8** — moderate DP cluster at spot.
  3. **Lower support $39.8–$40.0** — today's block prints ($39.98, $39.79).
- **Open questions:** Does OI (phase-3) show fresh put OI building at $39–$40 (confirming
  the phase-1 $30/$65 puts) and call walls near $45–46 (matching the DP supply shelf)? Is
  the $45–46 shelf distribution (bearish) or a re-accumulation base institutions defend?
