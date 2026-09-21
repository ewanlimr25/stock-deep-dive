# Phase 1 — Options Flow

**Ticker:** SMR
**As-of date:** 2026-06-16
**Generated:** 2026-06-17T11:51:06Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md

## Summary

The tape is **call-heavy by gross volume/premium but net-bearish by aggressor** —
a classic overwrite/sell signature on a heavily-shorted $9.9 name, not directional
upside buying. Whole-tape net flow is **−$159,229** (bearish_premium $1.985M >
bullish_premium $1.826M) despite calls being 2.0× puts by premium and 3.8× by
volume. The single strongest read is **a persistent multi-day BEARISH sweep
campaign** (`sweep-persistence`: 5/5 sessions, consistency 1.0, $9.18M). There were
**zero aggressive ask-side sweeps ≥$100k**; the only large sweeps were bid-side
(sellers). Per phase-0.5 this is a **BUSY_NAME_NORMAL_DAY** → conviction capped at
`+`.

## Key signals

- **Persistent bearish sweep campaign:** SMR in the top sweep list **5/5 sessions
  (06-10→06-16), `dominant_direction=bearish`, `consistency_score=1`,
  `total_sweep_premium=$9,177,230`** [FLOW:sweep_persistence].
- **Net-bearish whole-tape aggregate:** `net_flow = bullish − bearish = 1,825,992
  − 1,985,221 = −$159,229` [FLOW:insights_deep_dive], even though
  `put_call_ratio=0.2626` (call-heavy).
- **No ask-side aggression:** `sweeps --side ask --min-premium 100000` returned
  **empty**; bid-side returned 3 prints — a LEAP C10 sold ($136k), Nov C20 sold
  ($120k), Jul P11.5 sold ($109k) [FLOW:sweeps]. Aggressor = sellers.
- **New positions are short-dated synthetic-stock calls:** C5.5 & C6 exp 06-18
  (2-DTE, delta ~0.95) at vol/OI 184 and 17.4 — deep-ITM, ambiguous (2-day punt or
  stock replacement) [FLOW:unusual_volume].
- **Not a smart-money leader:** SMR absent from both bullish & bearish
  `smart-money-flow` top-10 (dominated by SPY/VIX/XLB) → "no smart-money flow
  detected for SMR on this date" [FLOW:smart_money_flow].

## Detailed findings

### Whole-tape aggregate (read top-N against this) — [FLOW:insights_deep_dive]

| Field | Value |
|-------|-------|
| `call_premium` | $3,144,320 |
| `put_premium` | $1,542,990 |
| `bullish_premium` | $1,825,992 |
| `bearish_premium` | $1,985,221 |
| **derived `net_flow`** (bull − bear) | **−$159,229 (net bearish)** |
| `call_volume` / `put_volume` | 47,662 / 12,518 (calls 3.8×) |
| `put_call_ratio` | 0.2626 (call-heavy) |
| `iv_rank` / `iv30d` | 26.68 / 92.2% |

**Read:** gross flow is call-dominated, but the *directional aggressor* read is
marginally **net-bearish**. On a name with 18.12% short float (phase-0), call-heavy
volume + bid-side aggression + net-bearish premium is the **call-overwriting /
premium-selling** signature, not bullish accumulation. The few deep-ITM short calls
are delta-1 proxies, not OTM upside bets.

### Sweeps (ask vs bid) — [FLOW:sweeps]

- **Ask side ≥$100k: EMPTY** — no one lifting offers aggressively.
- **Bid side ≥$100k (sellers):**

| Contract | Side | Premium | Size | Avg px | Read |
|----------|------|---------|------|--------|------|
| C10 exp **2028-01-21** (LEAP) | bid | $136,386 | 256 | $5.35 | LEAP call sold |
| C20 exp 2026-11-20 | bid | $119,781 | 1,242 | $0.99 | OTM call sold |
| P11.5 exp 2026-07-02 | bid | $108,866 | 611 | $1.79 | put sold |

Bid-side calls sold (caps upside / monetizes the LEAP) + bid-side put sold (mildly
bullish/premium harvest) = **mixed but seller-controlled**, no directional buyer.

### Multi-day persistence — [FLOW:sweep_persistence]

`{dominant_direction: bearish, sessions_in_top: 5/5, consistency_score: 1,
total_sweep_premium: 9,177,230}` over `[06-16, 06-15, 06-12, 06-11, 06-10]`. This is
the cleanest signal in the phase: **a week-long, every-session bearish sweep
campaign** — structural, not a one-day blip. SMR not in `sweep-ratio` top-15.

### New positioning (vol/OI ≥3) — [FLOW:unusual_volume]

| Contract | Vol | OI | vol/OI | Premium | Note |
|----------|-----|-----|--------|---------|------|
| C5.5 exp 06-18 | 368 | 2 | 184 | $170,359 | deep-ITM, 2-DTE (Δ0.97) |
| C6 exp 06-18 | 366 | 21 | 17.4 | $151,373 | deep-ITM, 2-DTE (Δ0.96) |
| C9 exp 07-02 | 248 | 48 | 5.2 | $35,506 | near-ATM |

Deep-ITM 2-DTE calls behave like synthetic long stock for two days — directionally
ambiguous (could be a short-term long punt or a stock-replacement/hedge). Large
*OTM* short-dated call **volume** also present (C12 06-18 vol 4,565; C10.5 vol
3,031; C15 vol 1,004) — lottery-ticket OTM calls **or** call writing into the 06-18
expiry; the net-bearish aggregate argues writing.

### Largest premium prints (top, single-trade) — [FLOW:top_premium_trades]

Fragmented and mixed-side; largest single print only **$84k** (vs $4.69M day
total). C5.5/C6 06-18 deep-ITM (mid/ask), C20 2027-01-15 LEAP call (mid, $70k), **P20
2028-01-21 LEAP put bought ask ($49.8k)** — small bearish LEAP, C15 07-17 OTM call
bought ask ($46.5k, size 1,722). No dominant directional print; underlying_price on
prints $9.93–$10.65 (spot ≈ $9.9–10.0, consistent with fz $9.89).

### IV outliers + Greeks — [FLOW:iv_outliers] / [FLOW:greek_screener]

IV outliers are almost all **06-18 (2-DTE)** contracts — high IV is mechanical at 2
DTE, not a vol-event tell. Greek-screener's top-premium names are the deep-ITM 06-18
calls (Δ0.94–0.97, i.e. synthetic stock). No large vega/gamma directional structure
stands out.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|------------------|--------------------------|-----------|
| `uw insights deep-dive --symbol SMR --date 2026-06-16` | net_flow=−159,229 ← `.uw_screener.bullish_premium-.bearish_premium`; pcr=0.2626 | uw_screener |
| `uw options-flow sweeps --symbol SMR --side ask --min-premium 100000 --top-n 25 --date …` | `.results==[]` (empty) | top-25 |
| `uw options-flow sweeps --symbol SMR --side bid --min-premium 100000 --top-n 25 --date …` | 3 bid prints ← `.results[].total_premium` ($136k/$120k/$109k) | top-3 |
| `uw options-flow unusual-volume --symbol SMR --min-vol-oi-ratio 3 --top-n 25 --date …` | C5.5 vol/oi=184 ← `.results[0].vol_oi_ratio` | 3 rows |
| `uw options-flow top-premium-trades --symbol SMR --top-n 25 --date …` | max single prem=$84,165 ← `.results[0].premium`; underlying_price 9.93–10.65 | top-25 |
| `uw options-flow iv-outliers --symbol SMR --top-n 15 --date …` | all 06-18 short-dated ← `.results[].expiry` | top-15 |
| `uw options-flow greek-screener --symbol SMR --top-n 15 --sort-by premium --date …` | deep-ITM Δ0.94–0.97 ← `.results[].delta` | top-15 |
| `uw hot-chains smart-money-flow --direction bullish\|bearish --top-n 10 --min-volume 500 --date …` | SMR absent (`test("SMR")` len 0) | top-10 ea |
| `uw hot-chains sweep-persistence --days 5 --top-n 20 --symbol SMR` (no `--date`) | bearish 5/5, $9,177,230 ← `.results[0]` | 1 row |
| `uw hot-chains sweep-ratio --top-n 15 --min-volume 500 --min-sweep-ratio 0.3 --date …` | SMR absent | top-15 |

## Tool errors

- `uw hot-chains sweep-persistence … --date 2026-06-16` → `Error: unknown flag:
  --date`. Re-run without `--date` (trailing tool, anchors to latest =
  2026-06-16, our as-of). Succeeded; `dates_covered` confirms it ends 06-16.

## DATA NOTE / CORRECTION

`insights deep-dive` `uw_screener` block has **no `net_flow` key** — derived as
`bullish_premium − bearish_premium = −159,229` per the field-path trap. No value
here was transcribed from an unparsed buffer; all reads jq-validated.

## Verdict for downstream phases

- **Bias from this phase:** **bearish-lean / mixed** (net-bearish aggregate +
  persistent bearish sweep campaign; gross call volume is overwrite, not upside)
- **Conviction:** **2/5** (real week-long bearish campaign, but today is a
  normal/quiet day for SMR per phase-0.5 self-pctile 37; magnitude discounted,
  capped at `+`)
- **Three things later phases should remember:**
  1. **Persistent bearish sweep campaign**: 5/5 sessions, $9.18M, consistency 1.0
     — structural bearish flow over the full week, not a one-day read.
  2. **No ask-side aggression at all** (≥$100k empty); bid-side selling dominates →
     the call-heavy gross volume is **writing/overwriting**, not accumulation.
  3. Net-bearish whole-tape (−$159k) despite P/C 0.26 — interpret call volume on
     this 18%-short name as premium-selling against the short base.
- **Open questions:** Is dark pool (phase-2) confirming distribution/short-side, or
  is there quiet accumulation under the bearish options tape? Are the OI walls
  (phase-3) consistent with call-writing into 06-18? Does the 2028 LEAP put + LEAP
  call-selling signal a longer-horizon bearish lean?
