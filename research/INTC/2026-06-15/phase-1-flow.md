# Phase 1 — Options Flow

**Ticker:** INTC
**As-of date:** 2026-06-15
**Generated:** 2026-06-16T01:24:55Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md

## Summary

The phase-0.5 directional conflict resolves into a **two-sided, net-neutral call
tape with one persistent bullish thread underneath.** Gross call premium ($425.4M)
swamps puts ($97.0M) 4.4:1, but bullish-classified ($229.9M) ≈ bearish-classified
($231.0M) — **derived net_flow = −$1.16M, essentially flat** [FLOW:insights_deep_dive].
The reason is symmetric call flow: aggressive ask-side call sweeps total **$80.6M**
against bid-side call sweeps of **$79.6M** — calls are being bought and sold/written
in nearly equal size [FLOW:sweeps]. The lone durable directional signal is
**5-session bullish sweep persistence: $1.23B total, consistency 1.0, INTC in the
top sweeps 5/5 sessions** [FLOW:sweep_persistence] — plus deep-ITM C90 Jul17 call
accumulation and net put-writing. Net bias: **mildly bullish, low conviction** —
the multi-day persistence and put-selling tilt up, but today is two-way OPEX-week
churn, not a clean one-way grab. Conviction capped at `+` per phase-0.5
BUSY_NAME_NORMAL_DAY.

## Key signals

- **5-day bullish sweep persistence — $1,231,820,756, consistency_score 1.0,
  sessions_in_top 5/5, dominant_direction bullish** [FLOW:sweep_persistence]. The
  single strongest, most repeatable bullish element.
- **Ask-side call sweeps $80.6M vs bid-side call sweeps $79.6M** — net call sweep
  only **+$1.0M**; the "aggressive call buying" (phase-0.5 net_call−put 99.2 pctile)
  is ~94% offset by call selling [FLOW:sweeps].
- **Puts net SOLD: ask-put $5.2M vs bid-put $13.2M (~−$8M net put writing)** —
  mildly bullish positioning [FLOW:sweeps].
- **Deep-ITM C90 Jul17 accumulation on ask** — $18.3M sweep (4,598 ct, avg $40.24,
  delta 0.91) + ≥5 repeated ~$2M ask prints; a high-delta stock-substitute long
  [FLOW:sweeps][FLOW:top_premium_trades].
- **Counter-thread: deep-ITM calls SOLD on bid** — C125 Jan27 $6.2M (delta .65),
  C85 Dec18 $3.7M (delta .83), C75 Jun18 $3.7M (delta .97) — profit-taking / rolling
  of an existing bullish delta book, not fresh shorting [FLOW:top_premium_trades].
- **No smart-money-flow imbalance for INTC** — absent from both bullish and bearish
  `smart-money-flow` top-10 (leaders WULF/SMH/QQQ/SPY) and absent from `sweep-ratio`
  top-15 [FLOW:smart_money_flow][FLOW:sweep_ratio].

## Detailed findings

### Whole-tape aggregate (read top-N against this) — `[FLOW:insights_deep_dive]`

| Field (`uw_screener`) | Value |
|---|---|
| call_premium | $425,398,661 |
| put_premium | $96,976,370 |
| bullish_premium | $229,872,054 |
| bearish_premium | $231,034,898 |
| **net_flow (derived = bull − bear)** | **−$1,162,844** (flat) |
| call_volume / put_volume | 444,046 / 268,691 |
| put_call_ratio | 0.605 |
| iv_rank | 82.02 |
| implied_move_perc | 6.17% |
| total_open_interest | 5,936,185 |

Gross call dominance (4.4:1 premium, PCR 0.605) but **flat net classification** =
two-way call book. This is the phase-0.5 conflict (net_call−put 99.2 pctile vs
bull−bear 2.3 pctile) explained: calls churned on both sides.

### Sweeps (ask vs bid)

| Side | Total prem | Calls | Puts | Read |
|------|-----------|-------|------|------|
| **Ask** (lifting offers) | $85.8M | **$80.6M** | $5.2M | aggressive call buying |
| **Bid** (hitting bids) | $92.8M | **$79.6M** | $13.2M | call selling + put selling |

Net: **calls ~flat (+$1.0M ask), puts net sold (~−$8M)**. Top ask call sweeps:
C90 Jul17 $18.3M · C130 Jun18 $7.25M · C150 Jul17 $5.08M · C115 Jun18 $4.80M.
Top bid call sweeps (writes/closes): C125 Jan27 $8.0M · C130 Jun18 $7.99M · C110
Jun18 $6.50M. The **C130 Jun18 strike appears large on both sides** ($7.25M ask /
$7.99M bid) — classic two-way / spread, not directional.

### New positioning (unusual vol, vol/OI ≥ 3)

OPEX-week front-dated churn dominates. Notable new positions (Jun18 = front weekly):
- Calls: C131 Jun18 (vol 6,744 / OI 688, v/oi 10, $3.15M), C137 Jun18 (v/oi 17,
  $1.95M), C148 Jun18 (v/oi 90, $0.92M), C75 Jun27 LEAP (v/oi 17, $1.65M)
- Puts: **ATM cluster P127/P128/P129 Jun18** (v/oi 21/47/49, ~$4.2M combined) — sits
  right on spot ($127.86); reads as 3-DTE gamma/pin positioning, not directional.

### Largest premium prints (single trades)

| Type | Strike | Exp | Premium | Size | Side | Δ | Read |
|------|--------|-----|---------|------|------|---|------|
| put | 95 | 2026-09-18 | $6.70M | 9,500 | no_side | −0.19 | OTM put — hedge/bet, neutral aggressor |
| call | 125 | 2027-01-15 | $6.18M | 1,765 | **bid** | 0.65 | ITM LEAP call SOLD |
| call | 85 | 2026-12-18 | $3.74M | 695 | **bid** | 0.83 | deep-ITM call SOLD |
| call | 75 | 2026-06-18 | $3.71M | 695 | **bid** | 0.97 | stock-sub call SOLD |
| put | 80 | 2026-10-16 | $3.29M | 7,075 | **bid** | −0.12 | OTM put SOLD (bullish write) |
| call | 90 | 2026-07-17 | ~$2.0M ×5 | 500 ea | **ask** | 0.91 | deep-ITM call BOUGHT (repeated) |

The book is **high-delta calls being repositioned** (bought at C90 Jul17, sold at
C75/C85/C125 longer/lower) + **OTM puts mostly written** (P80 Oct16 sold). One large
P95 Sep18 hedge stands apart. Net intent: maintain/roll a bullish delta long, sell
downside premium — constructive but not aggressive.

### IV outliers + Greeks

IV outliers are **deep-ITM / deep-OTM near-dated artifacts** (C30 Jun18 avg_iv 6.38 /
max 9.30; P15, C40–C43 Jun18) — unstable IV calc on 3-DTE wings, **not informative**
[FLOW:iv_outliers]. Greek screener confirms the premium leaders: the tape's vega is
concentrated in the C125 Jan27 LEAP (vega 0.36) and the directional delta in the
C90 Jul17 / C75–C85 ITM calls (delta 0.83–0.97) [FLOW:greek_screener].

## Tool calls (audit trail)

| Command (+ args, `--date 2026-06-15`) | Key value(s) ← `jq` path | Rows |
|------|------|------|
| `options-flow sweeps --side ask --min-premium 100000 --top-n 25` | ask total $85.8M, calls $80.6M ← `[.results[].total_premium]\|add` | 25 |
| `options-flow sweeps --side bid --min-premium 100000 --top-n 25` | bid total $92.8M, calls $79.6M, puts $13.2M | 25 |
| `options-flow unusual-volume --min-vol-oi-ratio 3 --top-n 25` | P127/8/9 Jun18 ATM cluster ← `.results[]` | 25 |
| `options-flow top-premium-trades --top-n 25` | P95 Sep18 $6.70M no_side; C90 Jul17 ask cluster ← sort_by(-.premium) | 25 |
| `options-flow iv-outliers --top-n 15` | C30 Jun18 avg_iv 6.38 (artifact) ← `.results[0]` | 15 |
| `options-flow greek-screener --top-n 15 --sort-by premium` | C125 Jan27 vega 0.36; C90 Jul17 Δ0.91 | 15 |
| `hot-chains smart-money-flow --direction bullish/bearish --top-n 10 --min-volume 500` | INTC ABSENT both ← `select(option_symbol\|startswith("INTC"))` = [] | 10+10 |
| `hot-chains sweep-persistence --symbol INTC --days 5 --top-n 20` (no --date) | $1.23B, consistency 1.0, 5/5, bullish ← `.results[0]` | 1 |
| `hot-chains sweep-ratio --top-n 15 --min-volume 500 --min-sweep-ratio 0.3` | INTC absent | 15 |
| `insights deep-dive --symbol INTC` | aggregate block above ← `.uw_screener` | 1 |

## Tool errors

- `hot-chains sweep-persistence` rejects `--date` (`Error: unknown flag: --date`) —
  it is a trailing/latest-anchored tool; latest = 2026-06-15 = as-of, so the read
  is reproducible. Re-run without the flag succeeded (matches the known "trailing
  tools anchor to latest date" behavior).

## DATA NOTE / CORRECTION

None on values. (Harness: all `uw` reads captured to files then `jq`'d against the
files — every number round-tripped through validated JSON, no streamed-buffer
transcription. Batched-stdout swallow seen in phase 0.5 avoided by file capture.)

## Verdict for downstream phases

- **Net bias:** mixed-to-mildly-**bullish** (persistence + put-writing tilt up;
  today's net classification flat).
- **Conviction:** **3/5** — the 5-day bullish sweep persistence (consistency 1.0)
  is a real multi-session footprint, but it rests on a two-way OPEX-week tape with
  ITM-call profit-taking, and phase-0.5 caps phases 1–2 at `+`. Not a clean
  directional day.
- **Three datapoints later phases must remember:**
  1. **5-session bullish sweep persistence $1.23B, consistency 1.0** — the bull case's backbone.
  2. **Today's net_flow is FLAT (−$1.16M)** despite 4.4:1 gross call premium — two-way call churn; don't mistake gross call premium for direction.
  3. **Puts net written (~−$8M), big P95 Sep18 hedge aside** — positioning leans bullish, downside premium being sold.
- **Open questions:**
  - Is dark pool confirming accumulation under this call flow, or is the underlying being distributed? → **phase 2**.
  - Where does the deep-ITM C90/upside-C150 call OI sit vs walls, and is the ATM Jun18 put cluster a dealer pin? → **phases 3–4**.
  - IV rank 82 + earnings 2026-07-23 — is the elevated IV a pre-earnings vol build (affects structure/sizing)? → **phases 4/7c**.
