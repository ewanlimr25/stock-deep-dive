# Phase 1 — Options Flow

**Ticker:** ADBE
**As-of date:** 2026-05-29
**Generated:** 2026-05-30T19:52:00Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md

## Summary

ADBE's whole-tape options flow on 2026-05-29 is **net bullish, call-dominated,
moderate conviction**: call premium **$46.62M vs put premium $20.43M** (2.3×),
`bullish_premium` **$36.93M** vs `bearish_premium` **$24.65M** (net **+$12.27M**),
P/C ratio **0.468** [FLOW:insights_deep_dive]. The aggressive tape leans the same
way — ask-side near-term call buying clustered at 245–260 (June expiries,
including the post-earnings 2026-06-12) plus two marquee bullish structures: a
deep-ITM **150 call** July buy (Δ0.97 — stock replacement, ~$2.95M across prints)
and **long-dated put selling** (Jan-2028 280-put bid $1.03M). The tempering
counterweights: meaningful **bid-side call selling** at 250–300 (capping
upside / covered writing) and a maxed **IV rank 100** that makes every long
premium expensive into the 2026-06-11 earnings. No multi-session sweep campaign
detected (sweep-persistence empty; ADBE absent from the smart-money top-10).

## Key signals

- Whole-tape **net +$12.27M bullish**, call premium **2.3×** put premium, P/C
  **0.468** — genuinely call-tilted, and per phase-0.5 this is ADBE's **most
  net-bullish day in 35 sessions** (`self_pctile_net_dir` 100) [FLOW:insights_deep_dive] [CTX:self_pctile DUCKDB].
- Largest **ask-side (bullish) sweep:** **150 call 2026-07-17 $2.15M**, Δ0.97 —
  a deep-ITM stock-replacement long, not a lottery [FLOW:sweeps] [FLOW:greek_screener].
- Fresh near-money call buildup into earnings: **257.5 call 2026-06-05 vol
  1,226 / OI 154 (7.96×) $0.78M** and **255 call 2026-06-12 vol 745 / OI 166
  (4.49×) $1.12M premium** [FLOW:unusual_volume].
- Largest single print is **bullish-income**: **280 put 2028-01-21 sold (bid)
  $1.03M** (Δ−0.46) — long-dated put writing [FLOW:top_premium_trades].
- **Counterweight:** ask-side **put** structures too — 260/300 put 2028 bought
  (~$1.6M) and bid-side 250 call 6/18 $0.96M *sold* — two-sided long-dated
  positioning caps the directional read at moderate [FLOW:sweeps].

## Detailed findings

### Whole-tape aggregate (read the top-N against this) — `[FLOW:insights_deep_dive]`

| Field | Value |
|-------|-------|
| call_premium | **$46,620,744** |
| put_premium | **$20,427,106** |
| bullish_premium | **$36,928,159** |
| bearish_premium | **$24,654,697** |
| net_flow | **+$12,273,462** (bullish) |
| put_call_ratio | **0.468** |
| call_volume / put_volume | 55,718 / 26,069 |
| iv30d / iv_rank | 0.596 / **100** |
| total_open_interest | 637,730 |

The tape is **genuinely call-tilted** (calls 2.3× puts on premium, P/C 0.47), and
phase-0.5 confirms the net-directional figure is 99.6th-pctile cross-sectionally
and 100th self-history — so the top-N prints below are read as **confirming a real
directional tape**, not as isolated prints on a balanced book. Turnover is
normal-to-elevated (81,787 contracts; 96th-pctile activity but no volume
blow-off, phase-0.5) so this is conviction-rich, not a volume event.

### Sweeps (ask = aggressive buy, bid = aggressive sell)

**Ask-side (bullish) — top prints:**

| Type | Strike | Expiry | Premium | Read |
|------|--------|--------|---------|------|
| call | 150 | 2026-07-17 | **$2,147,937** | deep-ITM Δ0.97 stock replacement (bullish) |
| call | 250 | 2026-06-18 | $1,113,489 | near-money June call buy |
| put | 260 | 2028-01-21 | $828,497 | LEAP put buy (hedge/structure) |
| put | 300 | 2028-01-21 | $809,000 | LEAP put buy (hedge/structure) |
| call | 255 | 2026-06-12 | $650,629 | **post-earnings expiry** call buy |
| call | 255 | 2026-05-29 | $469,640 | 0DTE — discount |
| call | 247.5/245/250/260 | 2026-06-05/06-12 | $0.28–0.34M ea. | near-money June call cluster |

**Bid-side (aggressive sells) — top prints:**

| Type | Strike | Expiry | Premium | Read |
|------|--------|--------|---------|------|
| put | 250 | 2026-08-21 | $1,282,497 | **put writing** (bullish-income) |
| put | 280 | 2028-01-21 | $1,030,500 | LEAP put writing (bullish-income) |
| call | 250 | 2026-06-18 | $962,147 | **call selling** (caps upside / covered) |
| put | 250 | 2028-01-21 | $842,180 | LEAP put writing |
| call | 210/300 | 2027-06-17/2028 | $0.66–0.70M | LEAP call selling |

Net sweep read: ask-side calls + put *writing* on the bid both lean bullish; the
offsetting signals are call selling at 250 June and some LEAP put buying. The
near-term, tradeable-horizon flow (June expiries) is **net bullish**; the
long-dated book is **two-sided structuring** (not a clean directional add).

### New positioning (unusual vol, vol/OI ≥ 3) — `[FLOW:unusual_volume]`

| Type | Strike | Expiry | Vol | OI | Vol/OI | Premium |
|------|--------|--------|-----|----|--------|---------|
| call | 257.5 | 2026-06-05 | 1,226 | 154 | 7.96 | $775,459 |
| call | 255 | **2026-06-12** | 745 | 166 | 4.49 | **$1,115,202** |
| call | 252.5 | 2026-06-05 | 403 | 114 | 3.54 | $297,715 |
| call | 257.5 | 2026-06-18 | 132 | 36 | 3.67 | $152,571 |
| put | 252.5 | 2026-05-29 | 777 | 83 | 9.36 | $167,289 (0DTE) |
| put | 250/247.5 | 2026-06-05 | 510/352 | 99/65 | 5.15/5.42 | $0.11–0.19M |

Fresh opening is **call-led at 252.5–257.5**, concentrated in the **June 5 and
June 12** expiries — i.e. positioning **straddling the 2026-06-11 earnings**
(6/12 is the first post-print expiry). Some protective put opening at 247.5–252.5
(near-money downside) accompanies it — consistent with hedged longs, not naked
bears.

### Largest premium prints — `[FLOW:top_premium_trades]`

The single biggest is a **sold** Jan-2028 280 put ($1.03M, bid). The next tier is
the deep-ITM 150-call July buying ($0.98M + $0.82M, ask). The blend — long-dated
put *writing* + deep-ITM call *buying* — is a **synthetic-long / bullish-carry**
signature from a sophisticated participant, set against some LEAP put buying that
looks like tail hedging on an existing position.

### IV outliers + Greeks

`iv-outliers` returned **no rows** at the default threshold (consistent with a
name whose whole surface is already rich — IV rank 100 — so no single contract is
an outlier *relative to the rest of ADBE's chain*). `greek-screener` (sorted by
premium) is dominated by the same prints: the 2028 280 put (Δ−0.46, sold), the
deep-ITM 150 calls (Δ0.97, bought), and a 210 2027 call (Δ0.71). Near-money June
calls carry the highest gamma (250 6/18 Δ0.57 γ0.010).

## Tool calls (audit trail)

| Command | Result summary |
|---------|----------------|
| `uw options-flow sweeps --symbol ADBE --side ask --min-premium 100000 --top-n 25 --date 2026-05-29` | 25 rows; top = 150C 7/17 $2.15M ask |
| `uw options-flow sweeps --symbol ADBE --side bid --min-premium 100000 --top-n 25 --date 2026-05-29` | 25 rows; top = 250P 8/21 $1.28M bid (put writing) |
| `uw options-flow unusual-volume --symbol ADBE --min-vol-oi-ratio 3 --top-n 25 --date 2026-05-29` | call-led fresh opens at 252.5–257.5, June 5/12 expiries |
| `uw options-flow top-premium-trades --symbol ADBE --top-n 25 --date 2026-05-29` | top = 280P 2028 sold $1.03M; 150C 7/17 bought |
| `uw options-flow iv-outliers --symbol ADBE --top-n 15 --date 2026-05-29` | **no rows** (whole surface already rich) |
| `uw options-flow greek-screener --symbol ADBE --top-n 15 --sort-by premium --date 2026-05-29` | mirrors top-premium; near-money June calls highest γ |
| `uw hot-chains smart-money-flow --direction bullish/bearish --top-n 10 --min-volume 500 --date 2026-05-29` | **no ADBE row** (top-10 = SPX/index) — no smart-money flag this date |
| `uw hot-chains sweep-persistence --days 5 --top-n 20 --symbol ADBE` | empty for ADBE (and `--date` unsupported — see Tool errors) |
| `uw hot-chains sweep-ratio --top-n 15 --min-volume 500 --min-sweep-ratio 0.3 --date 2026-05-29` | no ADBE rows in top-15 |

## Tool errors

- `uw hot-chains sweep-persistence --days 5 --top-n 20 --symbol ADBE --date 2026-05-29`
  → `Error: unknown flag: --date`. Re-ran **without** `--date`; the command
  anchors to the latest available session (2026-05-29 = latest local) so the read
  is still as-of-correct, but it is **not** as-of-reproducible on a later re-run.
  Result for ADBE: empty (no recurring multi-session sweep campaign).
- `uw options-flow dte-volume-share` / `expiry-heatmap` (optional supplemental)
  were attempted but their stdout buffered and did not return this session; they
  are not required phase-1 inputs and are omitted (the whole-tape aggregate and
  unusual-volume already give the DTE/expiry concentration: June 5/12).

## Verdict for downstream phases

- **Net bias:** **BULLISH** (whole-tape net +$12.27M, calls 2.3× puts on premium,
  ask-side near-term call buying + put writing).
- **Conviction:** **3 / 5.** The direction is real and unusually one-sided for the
  name (self_pctile 100), but conviction is held to moderate by: (a) IV rank 100
  making longs expensive, (b) the binary 2026-06-11 earnings inside the active
  expiries, (c) two-sided long-dated structuring + bid-side June call selling, and
  (d) no smart-money/sweep-persistence confirmation.
- **Three datapoints later phases must remember:**
  1. Whole-tape net **+$12.27M** bullish, call premium **$46.6M** vs put **$20.4M**,
     P/C **0.468** [FLOW:insights_deep_dive].
  2. Marquee bullish structure = **150C 7/17 bought (Δ0.97) + LEAP puts written** —
     a synthetic-long/carry signature, plus fresh **255C 6/12** (post-earnings)
     buying [FLOW:sweeps][FLOW:unusual_volume].
  3. **IV rank 100** + earnings **2026-06-11** → premium is expensive; favor
     spreads/defined-risk over naked long calls.
- **Open questions:** Is the dark pool (phase-2) confirming accumulation under
  this call bid, or distributing into it? Is the 150C-buy/LEAP-put-write a single
  desk's synthetic long or unrelated prints? Does dealer positioning (phase-4)
  put spot above or below the gamma flip (trend vs mean-revert into earnings)?
