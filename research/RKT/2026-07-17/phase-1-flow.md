# Phase 1 — Options Flow

**Ticker:** RKT
**As-of date:** 2026-07-17
**Generated:** 2026-07-19T19:24:00-04:00
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md

## Summary

Today's RKT tape is **mildly bearish in delta with a loud long-volatility overlay**.
The whole-tape aggregate is net-bearish — `net_flow = bullish − bearish =
−$364,914`, calls **net sold** (`net_call_premium −231,325`) while puts are **net
bought** (`net_put_premium +133,589`) — but the single largest structure in the
top prints is a **983-lot ATM straddle for the Jul-24 weekly** ($14.5 call + $14.5
put, both lifted at the ask), i.e. a big-move/long-vol bet into the **2026-07-30
earnings**, which is direction-neutral. Per phase-0.5 this is a
**BUSY_NAME_NORMAL_DAY** (today's premium is only the 16th self-percentile), so the
bearish delta lean is real but low-magnitude; the durable bearish signal remains
the multi-day escalation (07-16 −$3.0M net-dir), not this session's tape.

## Key signals

- **Whole-tape net-directional −$364,914** (bull $758,711 vs bear $1,123,625) — bearish tilt `[FLOW:insights_deep_dive]`
- **Calls net SOLD / puts net BOUGHT:** `net_call_premium −231,325`, `net_put_premium +133,589` — a bearish-delta signature `[FLOW:insights_deep_dive]`
- **983-lot long ATM straddle, Jul-24 exp:** $14.5C ask $50,133 + $14.5P ask $44,235 (same 983 size, gamma ≈0.33 each) — long-vol into earnings, direction-neutral `[FLOW:top_premium_trades / greek_screener]`
- **New positioning is put-led:** largest vol>>OI opener is Jul-24 $14.5 **put** (2,547 vol / 315 OI, voi 8.1, $114,649) vs Jul-24 $14.5 call (1,944 / 281) `[FLOW:unusual_volume]`
- **Upside calls being *sold*:** Jan-15 $21.2 calls hit the **bid** ($20,976×2), Oct $19C sold on bid $125,193 — capped-upside / overwrite tone `[FLOW:sweeps_bid / top_premium_trades]`

## Detailed findings

### Whole-tape aggregate (the truth the top-N is read against) `[FLOW:insights_deep_dive]`

| Field (`uw_screener`) | Value |
|---|---|
| call_premium | $1,563,016 |
| put_premium | $605,907 |
| bullish_premium | $758,711 |
| bearish_premium | $1,123,625 |
| **net_flow (bull − bear, derived)** | **−$364,914** (bearish) |
| net_call_premium | **−$231,325** (calls net sold) |
| net_put_premium | **+$133,589** (puts net bought) |
| call_volume / put_volume | 23,879 / 11,984 |
| put_call_ratio | 0.502 |
| iv_rank / iv30d | 51.7 / 0.694 |

Read: more *call dollars* changed hands than put dollars (call_premium ≫ put_premium),
but on a delta-adjusted, aggressor-side basis the tape is **bearish** — calls were
sold into and puts were bought. This is the classic "call selling + put buying"
bearish-delta configuration, consistent with phase-0.5's coherent bearish read
(RKT net-dir 4.1 universe pctile; Financial Services the most-sold sector −$57.2M).

### Sweeps (ask vs bid) `[FLOW:sweeps]`

Minimal aggressive-sweep activity (thin name):
- **Ask (aggressive buy):** Oct-16 **$18 call** $144,857 — the one bullish sweep.
- **Bid (aggressive sell):** Oct-16 **$19 call** $125,193; Jan-15 **$21.2 call** $114,924 — upside calls being **sold**.

Net sweep read: the aggressive prints are *call-selling on the upside* ($19C, $21.2C
sold) against a single $18C buy — no clean bullish-sweep signature; if anything a
cap-the-upside tone. No multi-day sweep persistence (below).

### New positioning (unusual vol, vol/OI ≥ 3) `[FLOW:unusual_volume]`

| Exp | Strike | Type | Vol | OI | Vol/OI | Prem | IV |
|---|---|---|---|---|---|---|---|
| 07-24 | 14.5 | **put** | 2,547 | 315 | 8.1 | $114,649 | 0.60 |
| 07-24 | 14.5 | call | 1,944 | 281 | 6.9 | $99,671 | 0.60 |
| 08-14 | 15.0 | put | 322 | 12 | 26.8 | $44,540 | 0.71 |
| 08-14 | 13.5 | put | 230 | 32 | 7.2 | $13,624 | 0.71 |

New positioning clusters at the **Jul-24 $14.5 ATM weekly** — puts opened heavier
than calls (2,547 vs 1,944), reinforcing the straddle/put-lean read. The Aug OTM
puts ($15, $13.5) are small downside adds.

### Largest premium prints (top of 25) `[FLOW:top_premium_trades]`

| Exp | Strike | Type | Side | Prem | Size | Δ | IV |
|---|---|---|---|---|---|---|---|
| 07-24 | 14.5 | call | **ask** | $50,133 | 983 | +0.54 | 0.59 |
| 07-24 | 14.5 | put | **ask** | $44,235 | 983 | −0.46 | 0.60 |
| 01-15 | 21.2 | call | bid | $20,976 | 228 | +0.28 | 0.61 |
| 01-15 | 21.2 | call | bid | $20,976 | 228 | +0.28 | 0.61 |
| 07-24 | 15.5 | call | mid | $15,728 | 983 | +0.24 | 0.59 |
| 07-24 | 14.5 | put | mid | $15,660 | 348 | −0.46 | 0.61 |
| 12-18 | 11.0 | put | ask | $15,610 | 223 | −0.17 | 0.65 |
| 08-21 | 15.0 | call | ask | $14,175 | 135 | +0.49 | 0.70 |
| 07-24 | 13.5 | put | ask | $13,762 | 983 | −0.19 | 0.65 |

Premium-weighted side totals (top-25): **call ask $97,827 / bid $89,905** (balanced),
**put ask $99,142 / bid $6,900** (puts overwhelmingly *bought*). The repeated 983-size
across the 07-24 $14.5C, $14.5P, $15.5C and $13.5P is one coordinated **long
straddle + call/put wings** → a long-gamma, big-move bet on the Jul-24 weekly. The
Dec $11 put ask ($15,610) is a cheap OTM downside tail.

### IV outliers + Greeks `[FLOW:iv_outliers / greek_screener]`

- **IV outliers are all 0DTE (07-17-expiry) artifacts** — deep-ITM $10–14 calls
  showing IV "1267%/1252%/337%" are pin/expiry noise, **not** signal. Tagged and
  discarded per phase-1 pitfalls.
- Greek screener confirms the 07-24 $14.5 straddle as the dominant Greek exposure
  (Δ +0.54 call / −0.46 put, **gamma ≈0.33 each** = ATM long-gamma). Longer-dated
  Jan $21.2 calls (Δ0.28, higher vega 0.035) are the *sold* upside leg.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw insights deep-dive --symbol RKT --date 2026-07-17 --json` | net_flow −$364,914 (`.uw_screener.bullish_premium−.bearish_premium`); net_call_prem −231,325; net_put_prem +133,589 | 1 (whole-tape) |
| `uw options-flow sweeps --side ask --min-premium 100000 --top-n 25` | 1 row: Oct $18C ask $144,857 ← `.results[]` | 1 |
| `uw options-flow sweeps --side bid --min-premium 100000 --top-n 25` | Oct $19C $125,193; Jan $21.2C $114,924 (calls sold) ← `.results[]` | 2 |
| `uw options-flow unusual-volume --min-vol-oi-ratio 3 --top-n 25` | Jul-24 $14.5P vol 2547/oi 315 $114,649 ← `.results[]` | 4 |
| `uw options-flow top-premium-trades --top-n 25` | 983-lot Jul-24 $14.5 straddle; put ask $99,142 vs bid $6,900 ← `.results[]` | 25 |
| `uw options-flow iv-outliers --top-n 15` | all 0DTE 07-17 pin artifacts ← `.results[]` | 13 (discarded) |
| `uw options-flow greek-screener --sort-by premium --top-n 15` | Jul-24 $14.5 straddle gamma 0.33 ← `.results[]` | 15 |
| `uw hot-chains smart-money-flow --direction bull/bear --min-volume 500` | RKT not in market top-10 either side | 0 RKT |
| `uw hot-chains sweep-persistence --days 5 --symbol RKT` | empty (no multi-day RKT campaign) | 0 |
| `uw hot-chains sweep-ratio --min-sweep-ratio 0.3` | RKT not present | 0 RKT |

## Tool errors

None. `sweep-persistence`, `sweep-ratio`, and `smart-money-flow` returned no RKT
rows — that is a *finding* (thin/normal day), not an error; recorded as such.

## DATA NOTE / CORRECTION

First `jq` on `top-premium-trades`/`greek-screener` used `.total_premium`/`.side`
paths that returned null — those tools nest premium under `.premium`, size under
`.size`. Re-read against `.premium`/`.size`/`.side`; all top-print premiums above
trace to `.premium`. `unusual-volume`/`iv-outliers`/`sweeps` use `.total_premium`
(confirmed non-null). No value was transcribed from an unparsed buffer.

## Verdict for downstream phases

- **Net bias:** **mildly bearish** (delta) with a **direction-neutral long-vol
  overlay** into earnings. Not a clean directional conviction day.
- **Conviction:** **2 / 5** — bearish tilt is genuine but small (net-dir −$365k,
  16th self-pctile), capped at `+` by BUSY_NAME_NORMAL_DAY; the straddle dilutes
  directionality. The stronger bearish evidence is the multi-day escalation
  (phase-0.5), not today's prints.
- **Three datapoints later phases must remember:**
  1. Whole-tape is **calls-sold / puts-bought** (net_call −231k, net_put +134k) →
     bearish delta; net_flow −$364,914.
  2. A **983-lot ATM straddle for Jul-24** dominates the top prints → the market is
     paying up for a **big move into the 07-30 earnings**; sizing must respect event vol.
  3. **Upside is being sold** (Jan $21.2C, Oct $19C on the bid) → limited appetite
     to chase RKT above ~$19–21 near-term.
- **Open questions:** is the dark pool (phase-2) accumulating into this weakness or
  confirming distribution? Do OI walls (phase-3) sit below spot (bearish pin) or
  above (support)? Does term structure show the Jul-24/Jul-31 vol kink the straddle
  implies?
