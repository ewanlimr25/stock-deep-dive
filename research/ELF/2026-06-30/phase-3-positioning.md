# Phase 3 — Open Interest & Positioning

**Ticker:** ELF
**As-of date:** 2026-06-30
**Generated:** 2026-07-01T00:26:59Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-0.5-context.md

## Summary

The ELF option chain is **structurally very call-heavy** — every OI wall near and
above spot is a call wall ($75, $80, $90, $100), with put walls only far below
($45–55, ≥25% OTM). That is a bullish *standing* posture. **But today's incremental
positioning was thin and churny**: despite the biggest premium day in 56 sessions
(phase-0.5) and ~20.5k contracts traded (phase-1), **only one strike added ≥500 net
OI** — the **$70 Jul-10 call, +1,466 (smart-positioning flags it bullish)**. The
marquee $75 Aug line (4,497 volume, phase-1) did **not** stick as OI, and the day's
decreases are all calls being *closed* — confirming phase-1's "two-way churn, not
clean accumulation" read. So: bullish chain skew, but the loud flow largely did not
convert to new held positions. The immediate structure is **spot $74 pinned just
under the $75 call wall (+1.33%)**, with $80 the next resistance and the Jul-17
monthly the nearest OI cliff (17.9% of total OI).

## Key signals

- **$75 = call-wall resistance at +1.33% above spot** (call_oi 4,979 vs put 178, net_oi +4,801) — immediate ceiling / pin [OI:oi-by-strike]
- **$80 = next call-wall resistance (+8.09%)** (call_oi 5,528, net_oi +5,335) [OI:oi-by-strike]
- **Only +1,466 net OI added all day** (the $70 Jul-10 call) — the loud tape did **not** stick as OI [OI:biggest-increases][OI:smart-positioning]
- **All OI decreases are calls closing** ($66 Jul-02 −558, Nov $80/$110 far-OTM) — no put-hedge build, no rolls [OI:decrease-with-volume][OI:position-rolls]
- **Nearest OPEX cliff = Jul-17 (17.9% of total OI)**; structural gravity well = Jan-2027 (32.7%) [OI:term-structure]

## Detailed findings

### OI walls by strike `[OI:oi-by-strike]` (spot $74.00)

**Tradeable horizon (DTE ≤ 30):**

| Strike | call_oi | put_oi | net_oi | role | dist |
|---|---|---|---|---|---|
| **$75** | 1,975 | 13 | **+1,962** | **call_wall_resistance** | **+1.33%** |
| $80 | 1,216 | 0 | +1,216 | call_wall_resistance | +8.09% |
| $70 | 3,306 | 0 | +3,306 | call_heavy | −5.42% |
| $66 | 1,096 | 35 | +1,061 | call_heavy | −10.83% |
| $65 | 1,216 | 447 | +769 | call_heavy | −12.18% |
| $50 | 0 | 3,123 | −3,123 | put_wall_support | −32.45% |

**All-expiry aggregate** (adds the LEAP/structural strikes): $80 (net +5,335) and $75
(net +4,801) are the dominant call walls; $70 call-heavy (net +4,913); put support
only at $50/$55 (net −6,514 / −4,586) but **25–32% OTM** — effectively no put wall
near spot. Read: dealers are structurally **short upside calls** into $75/$80 — a
move through $75 forces call-delta hedging (buying), a mild tailwind; but it is also
the level where long-call holders take profit → **$75 is a genuine two-sided
battleground/pin, not pure resistance** (net_oi is call-dominated, but phase-1 showed
the $75 line traded two-way).

### OI term structure `[OI:term-structure]` (total OI 63,673 across 13 expiries)

| Expiry | DTE | call_oi | put_oi | P/C | % of total OI |
|---|---|---|---|---|---|
| **2027-01-15** | 199 | 11,272 | 9,535 | 0.85 | **32.68%** ← structural gravity well (LEAP) |
| **2026-07-17** | 17 | 6,859 | 4,532 | 0.66 | **17.89%** ← nearest tradeable OPEX cliff |
| **2026-08-21** | 52 | 6,648 | 3,294 | 0.50 | **15.61%** ← holds phase-1's $75 call buying |
| 2028-01-21 | 570 | 4,004 | 1,911 | 0.48 | 9.29% ← the phase-1 $45 LEAP block |
| 2026-07-02 | 2 | 3,823 | 917 | 0.24 | 7.44% (front weekly, call-skewed) |
| 2026-11-20 | 143 | 3,193 | 1,202 | 0.38 | 6.90% |
| others | | | | | <5% each |

Cross-check the **Jul-17 (17.9%)** cliff against phase-4 max-pain; the **Jan-2027
(32.7%)** LEAP fraction is where the deepest positioning lives but is 199 days out.

### Largest OI increases `[OI:biggest-increases]` (min +500)

| Contract (OPRA-parsed) | Strike / Expiry / Side | OI Δ | Vol | oi_change |
|---|---|---|---|---|
| ELF260710C00070000 | $70 / 2026-07-10 / **Call** | **+1,466** | 1,786 | +12.9% |

**Only one strike** crossed +500 net OI — a $70 call for the Jul-10 weekly. Everything
else (incl. the $75 Aug 4,497-vol line) netted <500 OI change → **intraday round-trip
churn, not retained positioning**.

### Closing / roll activity `[OI:decrease-with-volume][OI:position-rolls]`

All decreases are **calls being closed**: $66 Jul-02 (−558), $80 Nov (−400), $110 Nov
(−399), $55 Jan-2028 (−157), $80 Jul-17 (−22), $69 Jul-02 (−2). No puts closing; **no
position-rolls detected (0 rows)**. Read: front-weekly and far-OTM call profit-taking
into the rally, no defensive rotation.

### Smart positioning `[OI:smart-positioning]`

Single inferred position: **$70 Jul-10 call, inferred_direction = bullish** (net_ask_bid
positive) — the same build as above. No bearish inferred positions.

### Pin risk / OPEX concentration (market-wide, filtered) `[OI:pin-risk][OI:opex-concentration]`

- **pin-risk (dte ≤ 7, ≤5% distance): ELF absent** from the top-25. The nearest weekly
  is Jul-02 (dte 2) but ELF's $75 wall (+1.33%) didn't rank as a market-wide pin
  candidate — recorded, not an error.
- **opex-concentration (min 40%): ELF absent** — its largest single-expiry share is
  Jan-2027 at 32.7%, below the 40% bar, so it correctly doesn't qualify.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw oi oi-by-strike --symbol ELF --dte-max 30 --top-n 10 --date 2026-06-30` | $75 net_oi +1,962 role call_wall_resistance ← `.results[]` | top-10 |
| `uw oi oi-by-strike --symbol ELF --top-n 10 --date 2026-06-30` (all-expiry) | $80 net_oi +5,335; $75 +4,801 | top-10 |
| `uw oi term-structure --symbol ELF --date 2026-06-30` | Jul-17 17.89% ← `.term_structure[].pct_of_total_oi`; total_oi 63,673 | 13 expiries |
| `uw oi biggest-increases --symbol ELF --top-n 20 --min-oi-change 500 --date 2026-06-30` | $70 Jul-10 +1,466 ← `.results[0].oi_diff_plain` (parsed `option_symbol`) | 1 |
| `uw oi decrease-with-volume --symbol ELF --top-n 15 --min-volume 100 --date 2026-06-30` | $66 Jul-02 −558 ← `.results[].oi_diff_plain` | 6 |
| `uw oi smart-positioning --symbol ELF --top-n 20 --min-oi-change 500 --date 2026-06-30` | $70 Jul-10 bullish ← `.results[0].inferred_direction` | 1 |
| `uw oi position-rolls --symbol ELF --threshold 500 --near-dte-max 30 --date 2026-06-30` | 0 rows | 0 |
| `uw oi pin-risk --top-n 25 --dte-max 7 --max-distance-pct 5 --date 2026-06-30` | ELF absent ← `index("ELF")==null` | 0 |
| `uw oi opex-concentration --top-n 20 --min-concentration-pct 40 --date 2026-06-30` | ELF absent | 0 |

## Tool errors

- `uw oi term-structure` output is keyed `.term_structure` (not `.results`); an initial
  `.results[]` jq raised "Cannot iterate over null" — corrected to `.term_structure[]`,
  re-read, values below are from the valid parse. Not a tool error (the JSON was valid).

## DATA NOTE / CORRECTION

- **term-structure jq path:** first attempted `.results[]` → null-iterate error; the
  correct path is `.term_structure[]`. All term-structure numbers above are from the
  corrected read (`total_oi 63,673`, Jul-17 17.89%, etc.). No numbers were transcribed
  from the errored attempt.

## Verdict for downstream phases

- **Positioning bias:** **BULLISH SKEW (structural), LOW incremental conviction.** The
  standing chain is call-dominated (walls $75/$80/$90/$100; no near put wall), but
  **today's flow barely added OI** — only +1,466 (a single $70 Jul-10 call) stuck, and
  calls were net *closing* elsewhere. The loud tape (phase-1) was churn, not
  accumulation. This **tempers** the phase-1 bullish flow.
- **Conviction:** **2 / 5** — structural call skew is mildly bullish, but the absence of
  net new held OI on the biggest premium day is a real yellow flag against chasing.
- **Largest OI build as % of float (advisory):** float unavailable (`fz` degraded,
  phase-0). Using shares-out ≈ 59.5M: +1,466 contracts ≈ 146,600 sh ≈ **~0.25% of
  shares out** — negligible; **not a structural build for this name**. Reinforces
  "churn, not accumulation."
- **Three pin/cliff strikes for phase-9** (sourced from `oi-by-strike` roles +
  `term-structure` cliff, not hand-picked):
  1. **$75 — call_wall_resistance (+1.33%)**: the immediate ceiling/pin just above the
     $74 spot; a decisive close above it (with the Jul-17 cliff) is the bull trigger.
  2. **$80 — call_wall_resistance (+8.09%)**: the upside target/next magnet.
  3. **$70 — call_heavy (−5.42%)**: nearest support battleground (and today's only real
     OI build); aligns with phase-2's $69.91 DP cluster → shared support ~$70.
- **Open questions:**
  - Is the $75/$80 call OI **speculative long** (dealers short, supportive gamma into a
    breakout) or **covered writing** against the phase-2 accumulation (a ceiling)?
    Phase-4 (max-pain/GEX) should resolve dealer sign.
  - With **no put wall near spot**, downside is structurally unprotected — does phase-4
    max-pain sit below spot (a drag) or at $75 (a pull-up)?
  - Does the churn (loud volume, no OI retention) argue the +17% run (phase-2) is
    **late-stage** rather than fresh accumulation? (phase-5 historical / phase-8.)
