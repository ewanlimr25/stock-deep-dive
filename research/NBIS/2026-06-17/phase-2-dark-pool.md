# Phase 2 — Dark Pool & Block Prints

**Ticker:** NBIS (Nebius Group NV)
**As-of date:** 2026-06-17
**Generated:** 2026-06-18T00:31:43Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md, phase-1-flow.md

## Summary

The dark pool **does not confirm** phase-1's net-bullish options flow — at best it's neutral, and the
**mega tier (≥$10M blocks) reads as distribution: buy_ratio 0.064 (sell ≈ 0.936), $158.5M across 8
blocks, sell_volume 526k vs buy 36k.** The broader **large tier ($925.3M, 4,634 trades) is balanced-
to-mildly-accumulative (buy_ratio 0.536)** and the block tier is dead-even (0.492). Average dark
print price **$284.01 sits above the $280.91 close**, i.e. institutions transacted into intraday
strength ($283–286) and the stock faded to close — a mild distribution tell. **Two important
caveats lower the conviction**: (1) the two largest "blocks" (124k + 122k sh at exactly $280.91) are
**closing-auction / after-hours prints** whose sell-classification is partly an NBBO artifact
(price vs a drifted after-hours quote ~$284), and (2) every print is **modest as % of float** (largest
block 0.06%, total dark 2.47% of the 202M float) — no float-dominating dump. Net read: **MIXED,
leaning mild distribution at the top tier; no accumulation signature underneath the bullish options.**

## Key signals

- **Mega tier 93.6% sell** (buy_ratio 0.064; sell_vol 526,251 vs buy 36,200; $158.5M, 8 blocks) →
  high-confidence distribution *band*, but see closing-cross caveat. [DP:block_stratified]
- **Large tier mildly accumulative** (buy_ratio 0.536; $925.3M; 4,634 trades) — the broad
  institutional read is roughly balanced. [DP:block_stratified]
- **avg dark price $284.01 > $280.91 close** — transacted above where it closed (faded). [DP:ticker_summary]
- **NBIS only rank #23** in today's dark-pool universe ($1.41B total premium) — active but not a leader. [DP:ticker_summary]
- **5-day price clusters mostly below spot** ($260.07 $362.8M, $232.36 $165.4M) — these are the
  uptrend's footprint / support, not fresh distribution. [DP:price_levels]

## Detailed findings

### Largest blocks (spot/close $280.91; times in ET) [DP:largest]

| Time ET | Price | Size | Premium | % float | vs_mid | Note |
|---------|-------|------|---------|---------|--------|------|
| 16:51 | $280.91 | 124,241 | $34.9M | 0.062% | −3.65* | after-close print (*NBBO drifted) |
| 16:01 | $280.91 | 122,100 | $34.3M | 0.060% | −0.59 | closing auction |
| 13:09 | $285.64 | 76,100 | $21.74M | 0.038% | −0.17 | INTRADAY, above close (mild sell) |
| 12:11 | $283.01 | 70,400 | $19.92M | 0.035% | −0.01 | INTRADAY, above close (neutral) |
| 16:54 | $280.91 | 59,410 | $16.69M | 0.029% | −3.61* | after-close |
| 16:01 | $280.91 | 37,000 ×2 | $10.39M ea | 0.018% | −0.59 | closing auction |

Of the 8 mega blocks (≥$10M), only **2 are genuine intraday** ($285.64, $283.01) — both *above* the
close and classified neutral-to-mild-sell; the other 6 are at/after the close (auction/AH), where
the sell-side NBBO classification is unreliable. Largest single trade $34.9M = **0.062% of float**.

### Tier breakdown (buy/sell per tier; sell = 1 − buy_ratio) [DP:block_stratified]

| Tier (boundary) | buy_ratio | sell (derived) | buy_vol | sell_vol | total_prem | trades |
|-----------------|-----------|----------------|---------|----------|------------|--------|
| **mega (≥$10M)** | **0.064** | **0.936** | 36,200 | 526,251 | $158.5M | 8 |
| block (≥$1M) | 0.492 | 0.508 | 571,704 | 589,174 | $328.0M | 126 |
| large (≥$100k) | 0.536 | 0.464 | 1,746,592 | 1,511,179 | $925.3M | 4,634 |
| retail (<$100k) | — | — | 0 | 0 | $0 | 0 |
| **all tiers** | | | | | **$1.412B** | |

Heuristic application: mega buy_ratio 0.064 ≤ 0.45 ⇒ **DISTRIBUTION at the mega tier** (>0.7 sell is
"high-confidence" — but discounted here for the closing-cross artifact). large tier 0.536 buy is in
the 0.45–0.55 "suggestive only" band → effectively neutral. No accumulation signature.

### Price levels (5-day clusters; window 2026-06-11→06-17) [DP:price_levels]

| Price | Premium | Shares | Read vs spot $280.91 |
|-------|---------|--------|----------------------|
| $260.07 | $362.8M | 1,395,015 | −7.4% — largest cluster (support / uptrend footprint) |
| $232.36 | $165.4M | 711,629 | −17.3% — deeper support |
| **$280.91** | $165.2M | 587,968 | at spot — current battleground |
| $285.64 / $286 | $23.0M / $12.8M | — | +1.7%/+1.8% — overhead supply |
| $270 / $271 | $17.0M / $13.9M | — | −3.5%/−3.6% — minor support |

The below-spot weighting reflects the 12-day rally (price climbed from ~$232 into ~$281), not active
distribution — these are accumulation/transaction levels from the way up, now acting as support.

### Extended-hours activity [DP:extended_hours]

15 prints, all clustered 16:01–16:54 ET at $280.91–$284.48 (closing-cross + immediate after-hours),
vs_mid 0 (auction prints). No surprise overnight catalyst-driven block; consistent with the closing-
auction interpretation. No directional extended-hours signal to attribute to news (cross-check phase-6).

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← path | Rows |
|------------------|--------------------|------|
| `uw dark-pool ticker-summary --top-n 30 --date 2026-06-17` | NBIS rank #23; tot_prem $1.412B; avg_price $284.01; shares 4.98M; max trade $34.9M ← `.results[]\|select NBIS` | 30 |
| `uw dark-pool largest --symbol NBIS --top-n 25 --sort-by premium --date 2026-06-17` | top block 124,241 sh $34.9M @$280.91; 2 intraday mega @$285.64/$283.01 ← `.results` | 25 |
| `uw dark-pool block-stratified --symbol NBIS --top-n 30 --min-tier large --date 2026-06-17` | mega buy_ratio 0.064, large 0.536, block 0.492 ← `.results[0].<tier>.buy_ratio` | 1 |
| `uw dark-pool price-levels --symbol NBIS --top-n 15 --days 5 --date 2026-06-17` | clusters $260.07 $362.8M, $232.36, $280.91 ← `.results` | 15 |
| `uw dark-pool extended-hours --symbol NBIS --top-n 15 --date 2026-06-17` | all closing-cross/AH @ $280.91 ← `.results` | 15 |
| `fz` float (phase-0) | Shs Float 202.00M → block %-float ← computed | — |

## Tool errors

None.

## DATA NOTE / CORRECTION

The raw mega-tier sell_ratio (0.936) overstates active distribution: 6 of 8 mega blocks are
closing-auction / after-hours prints at the $280.91 close, where NBBO-based buy/sell classification is
unreliable (the displayed NBBO ~$284 is a drifted after-hours quote). Conviction de-rated accordingly.
The 2 *intraday* mega blocks ($285.64, $283.01) are the cleaner read and lean neutral-to-mild-sell,
above the close. No value re-read; this is an interpretation caveat, not a transcription fix.

## Verdict for downstream phases

- **Institutional bias:** **MIXED → mild DISTRIBUTION at the mega tier** (no accumulation). Diverges
  from phase-1's bullish options flow.
- **Conviction:** **2/5.** The mega-sell signal is real (0.064 buy_ratio) and avg price > close
  supports it, but it's de-rated by (a) the closing-cross classification artifact on 6 of 8 mega
  blocks and (b) modest %-of-float (largest 0.06%, total 2.47%). Large tier is neutral (0.536).
- **Largest block as % of float (advisory):** $34.9M block = **0.062% of the 202M float**; total dark
  2.47% of float. Sizes are NOT meaningful enough for this large-float name to call it a decisive
  institutional event — color, not conviction. [DP:block_pct_float fz]
- **Three S/R levels for phase-9:**
  1. **$260.07** — largest 5-day cluster ($362.8M), primary support ~7.4% below spot.
  2. **$285.64–$286** — overhead supply (intraday mega blocks sold here), first resistance.
  3. **$232.36** — deeper support ($165M) if the rally unwinds.
- **Open questions:** Is the mega-tier selling outright distribution, or **stock→call rotation**
  (selling shares while buying the $180/$240 deep-ITM LEAP calls seen in phase-1 = capital-efficient
  re-leveraging)? Where are the OI walls vs the $260/$286 dark-pool levels and the $400 put strikes
  (phase-3)? Does dealer gamma pin spot at $280–281 (phase-4)?
