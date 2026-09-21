# Phase 9 — Trade Plan (PM Synthesis)

**Ticker:** FSLY (Fastly Inc) · **As-of:** 2026-05-29 · **Spot ref:** $17.77
**Bias:** LONG (starter / optionality) · **Conviction bin:** 0.55 · **Horizon:** 1–3 months

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis

Own a **small, defined-risk, cheap-convexity starter** on an armed-but-not-yet-
triggered squeeze — the real trade is the ignition, not the setup. FSLY's OI is
call-skewed (P/C OI **0.53**) and laddered **$20/$22.5/$25** above spot $17.77, with
**all** fresh OI on calls and a **4-day consecutive build** accelerating to **+6,062
contracts** on 5/29 `[OI:oi-by-strike]` `[HIST:oi-trend]` — quiet positioning over a
**14.6% short float** `[SENT:short_float fz semi-monthly]`, with institutions adding
(Inst Trans +17.5%, DP large-tier buy_ratio 0.85) `[SENT:retail_vs_inst fz]`
`[DP:block-stratified]` and a credible turnaround under it (4/4 accelerating beats
crossing into profit, D/E 0.41) `[FUND:earnings_surprise]`. Crucially the upside is
**cheap to own**: VRP **−0.566** (PREMIUM_BUYING, realized vol 144% vs IV30d 88%)
`[HIST:vrp]` — a rare green light to *buy* premium on a high-IV name.

But it is **not a trade yet**: phase-1 found **zero sweeps** on the +4.9% day, FSLY is
absent from the sweep-ratio scanner, volume was **9th self-percentile** `[FLOW:sweeps]`
`[CTX:self_pctile_volume]`, dealers are in **positive gamma pinning $17.5**
`[STRUCT:gex]`, days-to-cover is a low **1.74** (weak squeeze reflexivity), and the
next catalyst (earnings 8/05) is **>2 months out**. The phase-8b debate **disconfirmed**
(bull 0.55 / bear 0.55): the structure is real, the timing is a hope. So this is a
**starter-size optionality bet** — buy cheap convexity, risk only the small debit, and
**add only on the ignition**: a volume/sweep break through **$18.5–$19**. Hard stop on
a close below **$16** (where gamma flips negative and the floor becomes a trapdoor).

## Entries

| Type | Price | Trigger | Source |
|------|-------|---------|--------|
| **Primary (starter)** | **$17.5** | tag of the gamma node / 6-18 max-pain / dark-pool shelf $17.49–$17.58 (dealer-pinned support) | `[STRUCT:gex]` / `[DP:price-levels]` |
| **Add (the real trade)** | **$18.5–$19.0** | **volume/sweep ignition** through the pin — flips the desk's stand-aside agents LONG | `[FLOW:sweeps]` (absence today = wait) |
| Fade (counter) | $20.0 | rejection at the $20 call wall without volume → trim the starter | `[OI:oi-by-strike]` |

## Levels

| Level | Price | Role |
|-------|-------|------|
| Resistance (target 2) | **$22.5** | second call wall (+27%) — squeeze extension |
| Resistance (target 1) | **$20.0** | dominant call wall (net +14,840 OI, +12.9%) |
| Ignition trigger | $18.5–$19 | volume/sweep break that converts starter → position |
| Pin / support | **$17.5** | +$2.24M gamma node + 6/18 max-pain + DP shelf |
| **Hard floor / stop** | **$16.0** | gamma flips negative (−$1.6M node) + first OI put wall → trapdoor |

## Invalidation

- **Price:** a **close below $16** (unanimous desk + debate) — gamma turns negative
  and accelerates downside; the squeeze thesis is dead. `[STRUCT:gex]`
- **Signal:** the **OI build reverses** (call OI bleeding instead of building) or DP
  large-tier flips to selling — the quiet accumulation was a head-fake. `[HIST:oi-trend]`
- **Time/thesis:** **no ignition by mid-July** (volume stays sub-average, no sweeps,
  price pinned) → the cheap convexity decays; let the starter expire/close, don't add.
  `[FLOW:sweeps]`

## Sizing

| Input | Value | Source / note |
|-------|-------|---------------|
| `p_raw` | 0.60 | phase-5 `bullish_flow` 5d win-rate `[HIST:signal-backtest]` |
| `win_rate_n` | 70 | N≥20 → cap 0.90 |
| `p` (capped) | **0.60** | min(0.60, 0.90); universe-pooled/in-sample |
| Payoff `b` | **1.26** | (target $20 − entry $17.77) / (entry $17.77 − stop $16) |
| `raw_kelly` | **0.283** | (0.60·1.26 − 0.40)/1.26 |
| suggested (pre-gate) | min(0.283·0.25·100, 5) = 1.77% → win-rate-map ceiling **2.5%** → 1.77% | Kelly × fraction |
| **Gates applied** | **debate cut + QUIET cap** (see below) | |
| **`final_size_pct`** | **0.5% (starter)** | debate disconfirmed → cut one step + bin downshift; phase-0.5 QUIET → starter cap |

**Risk gates (each can only cut):**
1. **Fundamentals (7b): CONFIRM** → no-op (caveat: unprofitable, caps not cuts).
2. **Sentiment/crowd (7c): NO-CUT, BALANCED** → no-op.
3. **Correlation cluster: CLEAN** — FSLY idiosyncratic (beta 0.37, *negatively*
   correlated FSLY/DDOG −0.634); **no cluster to cut against** (a diversifier). → no-op.
4. **Sector rotation: NEUTRAL** (Tech inflow is generic; FSLY doesn't participate) → no-op.
5. **Debate disconfirmation: TRUE** (bull 0.55 = bear 0.55) → **down-shift bin to 0.55
   + cut one size step.** This is the binding gate.

**Context modifier (0.5):** `BUSY_NAME_NORMAL_DAY` leaning **QUIET** (volume 9th
self-pctile) → **caps directional size at STARTER** regardless of Kelly. Binding.

→ Net: pre-gate 1.77% → debate cut + QUIET starter-cap → **final 0.5% (starter)**.

## Structures (sized so max-loss ≤ 0.5% of book risk)

| # | Kind | Type | Strikes | Expiry | Debit/Credit | Breakeven | Max loss | Note |
|---|------|------|---------|--------|--------------|-----------|----------|------|
| 1 | directional | **call debit spread** | **20/22.5** | 2026-07-17 | ~$0.55 debit | ~$20.55 | $0.55 (per spread) | the cheap-convexity expression — anchored to the $20/$22.5 call ladder; VRP says it's cheap-vs-realized; max-loss = debit, neutralizes the $16 trapdoor |
| 2 | defined_risk | **17.5/15 put credit spread** | **17.5/15** | 2026-07-17 | ~$0.70 credit | ~$16.80 | $1.80 (width−credit) | sells the gamma-pin/DP-shelf support; profits if $17.5 holds; **only if comfortable with the $16-stop overlap** — the 15 strike sits below the trapdoor, so this is an aggressive financing leg, mark accordingly |

- **Preferred expression:** the **20/22.5 July call debit spread** as a *starter* —
  defined-risk, cheap-convexity, max-loss = the small debit. **Add a second tranche
  only on the $18.5–$19 volume/sweep ignition.** The put credit spread is an optional
  financing overlay but its short-15 leg sits below the $16 stop — use only if you
  accept assignment risk there; most will skip it.
- **Why a starter, not a position:** debate disconfirmed + QUIET context + no catalyst
  = this earns a toe-hold, not size. The real trade is the ignition. `[STRUCT:gex]`

## Expected move

- Screener daily implied move **2.46%** (~$0.44) `[CTX:implied_move]`.
- July (7/17, 49 DTE) expected move ≈ **±32%** (from iv30d 0.88) — the $20/$22.5
  spread (+12.9%/+27%) sits inside the July expected move, i.e. the squeeze target is
  reachable within normal vol *if* it moves; the problem is direction/ignition, not range.

## Macro

- **Net: neutral-to-mild-tailwind (non-decisive).**
- Tailwinds: `[MACRO:sector_flow_persistence]` Tech #1 inflow (persistence 1.0) —
  generic; `[MACRO:market-regime]` SPY uptrend.
- Headwinds/neutral: `[MACRO:market-regime]` breadth 36.3% (narrow, "half-size");
  `[MACRO:portfolio_correlation]` FSLY idiosyncratic/low-beta → no sector *push* either.

## Catalysts

| Date | Event | Impact |
|------|-------|--------|
| ~2026-07-17 | July OPEX (call-ladder gravity) | ? |
| 2026-08-05 | Next earnings (beyond a tactical horizon; no isolable event-vol expiry) | ? |

## Key risks

1. **No catalyst / no ignition** — zero sweeps, earnings >2mo, positive gamma pins
   $17.5; the most likely path is a chop that decays the premium. `[FLOW:sweeps]`/`[STRUCT:gex]`
2. **Unprofitable small-cap, no earnings floor** — op margin −16%; if momentum fails
   there's nothing valuation-wise to catch it. `[FUND:operatingMargin fz]`
3. **Weak squeeze reflexivity** — 14.6% SI but only 1.74 days-to-cover; shorts cover
   fast, so the short base won't force a reflexive spark on its own. `[SENT:short_float fz semi-monthly]`
4. **Sub-scale accumulation + insiders selling** — DP $10.5M (FSLY absent from
   top-200 DP names); Insider Trans −19.4% into the +74.5% YTD run. `[DP:block-stratified]`/`[SENT:retail_vs_inst fz]`

## Citations (≥3 distinct upstream datapoints)

- `[OI:oi-by-strike]` $20 call wall net +14,840 (+12.9%), ladder 20/22.5/25; P/C OI 0.53
- `[HIST:vrp]` VRP −0.566 PREMIUM_BUYING (RV 144% >> IV 88%) — cheap-vs-realized
- `[HIST:oi-trend]` 4 consecutive OI-build days, +6,062 on 5/29, all call-led
- `[FLOW:sweeps]` 0 sweeps on a +4.9% day — armed but un-ignited
- `[STRUCT:gex]` positive gamma pins $17.5 (+$2.24M node); flips negative below $16
- `[SENT:short_float fz semi-monthly]` 14.6% SI / 1.74 days-to-cover (low)
- `[FUND:earnings_surprise]` 4/4 beats crossing into profit (+112%, +58%)

## Upstream references

- phase-8b-debate.md §Disconfirmation — bull 0.55 = bear 0.55, **disconfirmed**; this
  plan inherits the "starter-only, wait-biased, ignition-is-the-trade" verdict and
  applies the debate size-cut + bin downshift.
- phase-8-agent-views.md §Verdict — 2 LONG / 2 NEUTRAL / 1 RANGE / 0 SHORT, avg conv
  2.0; plan = starter long at 0.55, defined-risk call spread, add on ignition.
- phase-0.5-context.md §Verdict — QUIET (volume 9th pctile) → starter size cap applied.

## Next phase

- decision.json (written alongside) → phase-10-audit.md (confluence score + contradiction sweep)
