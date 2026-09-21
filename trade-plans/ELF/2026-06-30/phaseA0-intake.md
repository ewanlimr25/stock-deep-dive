# Phase A0 — Intake & Reuse Detection — ELF

**Ticker:** ELF (US-listed equity, NYSE — e.l.f. Beauty) · **As-of:** 2026-06-30 (US/Eastern) · **Version:** v1

## Inputs
- Ticker validated: `ELF` matches `^[A-Z][A-Z0-9.]{0,5}$`.
- As-of date: 2026-06-30 (default = today). All look-backs `<= as_of`.
- Book risk overrides: none → defaults (fraction 0.25, cap 5%).
- Output dir: `trade-plans/ELF/2026-06-30/` (newly created; no prior files → v1).

## Reused deep dive
- **Path:** `research/ELF/2026-06-30/` — has `decision.json` + full phase set.
- **Age:** **0 days** (same-day; generated 2026-07-01T01:16Z UTC = evening 06-30 ET) → freshest possible. L-0003 staleness cut does **not** apply.
- **flow_source = `deep_dive`.** Full flow / dark-pool / OI / dealer-structure / historical / macro / fundamentals / sentiment / debate substrate reused. No live re-pull needed.

### Deep-dive headline (from decision.json)
- **Bias:** **LONG** · **conviction 0.55** · horizon 1–4w · spot_ref **$74.00**.
- **final_size_pct = 0.6%** → **a real (small) defined-risk long** — NOT watch-only. First of this session's three tickers with a non-zero size.
- **Thesis core:** insider- & OI-confirmed **turnaround** — **25 consecutive OI-build days (+127,955)** [HIST:oi-trend], **June MSPR +44.1** (insiders buying) [FUND:insider-sentiment], a **$45 Jan-2028 delta-0.85 LEAP** [FLOW:sweeps] — that has run **+34.9%/30d into a long-gamma dealer cap** (ZGL $59.97, gamma walls **$70 (+1.03M) / $75 (+681k)**, max-pain $59–63 **below** spot) [STRUCT:gex]. Desk 2 LONG-mild / 2 RANGE + disconfirmed debate → **small defined-risk DIP-BUY at $70 / $64–65 with a capped $75–80 target — NOT a chase of $74.**
- **Levels:** support 70, resistance 75, gamma_flip (ZGL) **59.97**, largest_pin 60.
- **Entries (deep dive):** primary **$70** (pullback to largest gamma strike / DP cluster — dealers buy dips in long-gamma); aggressive **$75** (decisive close above the $75 wall + fresh OI → squeeze-through, 12.7% short is fuel); fade **$64.5** (rejection at $75 back to shelf, or a flush into the 5-day institutional shelf that holds).
- **Sizing:** p 0.625 (n=8, backtest), payoff_b 1.67, raw_kelly 0.40, **final_size_pct 0.6%**.
- **IV rank 46.8**; **VRP +0.081 → mild PREMIUM_SELLING**; expected move ±3.52% / ±$2.61 to Jul-31.
- **Gates:** fundamentals **CONFIRM**, sentiment **CAUTION**, crowd **BALANCED**, rotation **neutral**, debate **DISCONFIRMED** (bull 0.65 = bear 0.65).
- **Catalysts:** June ISM/jobs (early Jul) · June CPI (mid-Jul) · haircare rollout ramp (TikTok Shop → Target, soft +) · **ELF Q1 FY2027 earnings Aug-5** (Jul-31 structures expire before it).
- **Recommended structures:** (1) call debit **72/78 Jul-31** (debit ~$2.0, BE $74) — straddles the $75 wall, caps at $78, **expires pre-earnings**; (2) put credit **65/60 Jul-31** (credit ~$1.4, BE $63.6) — sells the $64–65 shelf into VRP +0.081 + long-gamma buffer.

### Setup character (vs the prior two tickers)
Unlike INTC (DIVERGENT/VETO/0%) and ENVX (DIVERGENT/negative-edge/0%), ELF is **CONFLUENT bullish** — flow (OI build + insider + LEAP) and chart (above sma20/50, MACD bullish) agree on direction — but **both flag the same caution: extended/overbought into a long-gamma cap**. So the edge is real but the *entry* is bad at $74; the plan is a **dip-buy, not a chase**, with the aggressive $75 breakout gated to confirmation.

## Reasoning ledger (loaded `trade-plans/_eval/reasoning-ledger.md`)
- **L-0001 — don't size a breakout at full until the break holds** · **ACTIVE** · `pattern:triangle/flag, setup:chart-leads`. → **LIKELY APPLIES** to the aggressive **$75 squeeze-through** entry: require a decisive close above the $75 wall on >1.2× volume with fresh OI before adding; no anticipatory size. Confirm after A2 pattern read.
- **L-0002 — DIVERGENT is not a directional trade** · ACTIVE. → **does NOT apply** (this is CONFLUENT, not divergent) — but the *extended/overbought* condition is the analog caution; enforce dip-buy entry, not chase.
- **L-0003 — stale flow decays** · ACTIVE. → **does NOT apply** (deep dive 0 days old).
- **L-0004 — bearish-sweep/short-gamma/VETO trap** · CANDIDATE. → does NOT apply (long, long-gamma, no veto).
- `ledger_lessons_applied` (carry to A4): **L-0001** (breakout confirmation on the $75 add); dip-buy discipline (L-0002 analog); L-0003/L-0004 n/a.

## Chart source probe (smoke test)
- `chart_engine.py --ticker ELF --date 2026-06-30` → **`available: true`**, **source = `yfinance`** (373 daily sessions). B1 is **not** a gap.
- Spot $74.00 (chart) = $74.00 (deep dive) — identical.
- Snapshot: ma_stack **mixed** (spot 74 > sma20 60.9 > sma50 59.77, but **< sma200 84.05**), dist +23.81% to sma50 / **−11.96% to sma200**, RSI14 **72.7 (overbought)**, MACD hist +1.373 (bullish), ATR14 3.85 (5.49%), BB 47.26–74.53 (**spot pressing the upper band**), 52w range **$49.50–$146.67** (halved from the high, bouncing hard off the low). → chart is **bullish-momentum but stretched/overbought below the 200-day**.
- No tool errors.

## Verdict for downstream
- `deep_dive_reused`: **research/ELF/2026-06-30** (age **0 days**, freshest)
- `flow_source`: **deep_dive**
- `chart_source`: **yfinance** (373 sessions)
- `ledger_lessons`: **L-0001** (apply to the $75 breakout add); L-0002/L-0003/L-0004 n/a (with the extended-entry caution as the L-0002 analog)
- Setup signature: **CONFLUENT LONG (OI build + insider + LEAP ∥ bullish momentum) but EXTENDED/OVERBOUGHT into a long-gamma $75 cap** with max-pain below spot → **small defined-risk DIP-BUY at $70/$64–65, capped $75–80 target, breakout-add gated to a confirmed $75 close.** Expect A1 → SUFFICIENT; A3 → LONG, conviction 0.55, size ~0.6% (dip-buy), two structures pre-earnings.
