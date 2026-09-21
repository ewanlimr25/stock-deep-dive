# Phase 2 — Dark Pool & Block Prints

**Ticker:** PATH
**As-of date:** 2026-06-05
**Generated:** 2026-06-06T10:25:00-04:00
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md, phase-1-flow.md

## Summary

Off-exchange tape leans **mildly accumulative but unconvincing**: large-tier
buy_ratio **0.638** (suggestive band, not high-confidence) on $55.56M / 484
trades, the day's single biggest block (135,000 sh @ $11.41, $1.54M) printed
**at the ask**, but the mega tier is empty, PATH is nowhere in the market-wide
DP top-30, and a §B timestamp join shows **no stock-side confirmation** of
phase-1's key Sep $10C sweep. All 5-day institutional price clusters sit
*above* spot ($11.83–$12.97) — that is overhead supply from the faded
earnings pop, not institutions paying up. Phase-0.5 cap (`+`) applies.

## Key signals

- Large-tier (484 trades): buy_volume 3,160,389 vs sell_volume 1,791,352 →
  **buy_ratio 0.638** (derived sell_ratio 0.362), $55,557,866 premium
  [DP:block_stratified]
- Biggest block: **135,000 sh @ $11.41 = $1,540,350** at 13:54:01Z (09:54 ET),
  printed AT the ask (NBBO 11.40/11.41) → buy; it is the *only* block-tier
  print (block buy_ratio 1.0) [DP:largest][DP:block_stratified]
- **Mega tier: zero trades** — no >$5M conviction prints [DP:block_stratified]
- 5-day price-level map is all overhead: **$12.86–$12.97 shelf ≈ $82M / ~6.3M
  sh**, $12.72 $21.0M in just 6 prints (avg ~275k sh), $12.00–$12.06 ~$26.7M,
  $11.83–$11.84 ~$18.4M [DP:price_levels]
- §B join: ±5 min around the 10:28:31 ET Sep $10C sweep → 16,792 sh **hit**
  (sell) @ $11.30 at 10:26:43, two ~9k mid prints after — **no DP buy
  confirmation of the option print** [DP:ts_confirm DUCKDB]

## Detailed findings

### Largest blocks (top-25, `--sort-by premium`)

| Time (Z) | Price | Size | Premium | NBBO | Read | % float |
|---|---|---|---|---|---|---|
| 13:54:01 | 11.41 | 135,000 | $1,540,350 | 11.40/11.41 | at-ask buy | 0.033% |
| 15:36:37 | 11.111 | 72,509 | $805,647 | 11.11/11.12 | near-bid | 0.018% |
| 16:25:00 | 11.12 | 52,748 | $586,558 | 11.13/11.14 | below-bid sell | 0.013% |
| 13:55:36 | 11.475 | 47,794 | $548,436 | 11.46/11.48 | mid | 0.012% |
| 15:36:37 | 11.11 | 47,537 | $528,136 | 11.11/11.12 | at-bid sell | 0.012% |
| 19:41:11 | 11.23 | 45,101 | $506,484 | 11.23/11.24 | at-bid | 0.011% |

(% of float vs Shs Float 412.34M, phase-0-intake.md §Finviz
[DP:block_pct_float fz].) Intraday tape readable off the prints: open prints
$11.61–$11.73 (12:43–13:40Z), morning buy block at $11.41–$11.47, midday flush
to **$11.11–$11.14** (15:35–16:25Z, mixed-to-sell prints ≈$2.9M), recovery to
$11.18–$11.30 afternoon, close prints $11.23–$11.24. Net path: lower-high day
consistent with phase-0's drift (close 11.24 vs prev 11.67).

### Tier breakdown (`block-stratified`, buy fraction = `.results[].<tier>.buy_ratio`)

| Tier | trades | buy_vol | sell_vol | buy_ratio | derived sell_ratio | premium |
|---|---|---|---|---|---|---|
| mega | 0 | 0 | 0 | 0.5 (degenerate) | — | $0 |
| block | 1 | 135,000 | 0 | **1.0** | 0.0 | $1,540,350 |
| large | 484 | 3,160,389 | 1,791,352 | **0.638** | 0.362 | $55,557,866 |

0.638 sits in the 0.55–0.70 "suggestive only" band (NBBO classification is
probabilistic). Day's large-tier DP volume = 4,951,741 sh ≈ **1.20% of float**
— routine institutional turnover for this name, not a footprint
[DP:block_pct_float fz].

### Price levels (5-day, `--days 5`; window = 06-01→06-05, anchors to latest
date = as-of here, per phase-0 available-dates — no slide)

All 15 levels ≥ $11.83, i.e. **100% of 5-day institutional volume memory is
above spot $11.24** — the 06-01 earnings session (close 13.10, phase-0 drift)
built the $12.7–$13.0 shelf, since abandoned. Reading: heavy **overhead
supply / trapped longs**, not "institutions paying up" — the
clusters-above-spot accumulation heuristic does not apply on a falling tape.
Support below spot has no 5-day DP memory; the only intraday reference is
today's $11.11–$11.14 print zone.

### Extended-hours activity

5 prints: 12:43/13:00Z premarket (8,936 @ 11.6296; 10,248 @ 11.61 — small,
unremarkable) and 20:00:24–25Z = the 16:00 ET closing cross (23,025 + 11,826 +
9,199 @ $11.24 ≈ $495k) — **closing-auction mechanics, not directional intent**
[DP:extended_hours]. Nothing pre-catalyst-shaped.

### Market-wide context

PATH absent from `ticker-summary` top-30 (leaders QQQ $21.4B, SPY $20.9B, MU
$15.5B) — consistent with phase-0.5 `BUSY_NAME_NORMAL_DAY`.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw dark-pool largest --symbol PATH --top-n 25 --sort-by premium --date 2026-06-05 --json` | 135,000 @ 11.41 $1,540,350 ← `.results[0]{size,price,premium}` | 25 |
| `uw dark-pool block-stratified --symbol PATH --top-n 30 --min-tier large --date 2026-06-05 --json` | large.buy_ratio 0.638 ← `.results[].large.buy_ratio`; sell_ratio derived 1−0.638 | 1 ticker row |
| `uw dark-pool extended-hours --symbol PATH --top-n 15 --date 2026-06-05 --json` | closing-cross 23,025 @ 11.24 ← `.results[]{size,price}` | 5 |
| `uw dark-pool price-levels --symbol PATH --top-n 15 --days 5 --date 2026-06-05 --json` | 12.72 → $21,016,200/6 trades ← `.results[]{price_level,total_premium,trade_count}` | 15 |
| `uw dark-pool ticker-summary --top-n 30 --date 2026-06-05 --json` | PATH absent ← `select(.ticker=="PATH")` | top-30 |
| DuckDB §B ±5min join @ 10:28:31 ET | 16,792 sh `hit` @ 11.30 | 3 rows |

## Tool errors

None — all five CLI calls and the DuckDB join returned valid JSON/frames.

## DATA NOTE / CORRECTION

None — first reads stood.

## Verdict for downstream phases

- **Accumulation / Distribution / Mixed:** **Mixed, mild accumulation tilt**
  (large-tier 0.638 suggestive; single at-ask block buy; but zero mega tier,
  no sweep confirmation, falling price path)
- **Conviction:** 2/5 (and phase-0.5 caps phases 1–2 confluence at `+`)
- **Largest block as % of float:** 0.033% (135k / 412.34M) — *not meaningful
  size for this name*; day's whole large-tier was 1.20% of float. Advisory:
  nothing here is a conviction footprint.
- **Three S/R levels for phase-9:**
  1. **$11.11–$11.14** — today's institutional flush zone (intraday support;
     break = no DP memory below)
  2. **$11.83–$12.06** — first overhead supply band ($18.4M + $26.7M clusters)
  3. **$12.72–$12.97** — the earnings-day shelf (~$103M incl. 12.72) — major
     resistance / target ceiling
- **Open questions:** Did the Sep $10C/$15C volume become new OI (phase 3)?
  Is the 0.638 large-tier buy tilt just HTB/borrow mechanics from the deep-ITM
  call structure phase-1 flagged (phase 3 OI + phase 7c borrow data)?
