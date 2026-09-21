# Phase A0 — Intake & Reuse Detection — ENVX

**Ticker:** ENVX (US-listed equity, NASDAQ — Enovix) · **As-of:** 2026-06-27 (US/Eastern) · **Version:** v1

## Inputs
- Ticker validated: `ENVX` matches `^[A-Z][A-Z0-9.]{0,5}$`.
- As-of date: 2026-06-27 (default = today). All look-backs `<= as_of`.
- Book risk overrides: none → defaults (fraction 0.25, cap 5%).
- Output dir: `trade-plans/ENVX/2026-06-27/` (newly created; no prior files → v1).

## Reused deep dive
- **Path:** `research/ENVX/2026-06-26/` — has `decision.json`.
- **Age:** 1 calendar day (0 trading days) vs as_of → **NOT stale**. L-0003 staleness cut does **not** apply.
- **flow_source = `deep_dive`.** Full flow / dark-pool / OI / dealer-structure / historical / macro / fundamentals / sentiment / debate substrate reused. No live re-pull needed.

### Deep-dive headline (from decision.json)
- **Bias:** **RANGE** · **conviction 0.55** · horizon 1–4w · spot_ref **$5.95**.
- **final_size_pct = 0.0** → **watch, not a trade**; directional risk skipped, only token defined-risk debit carry permitted.
- **Thesis core:** a single ask-side campaign bought **$871,964 of $6-strike October calls (84% ask)** [FLOW:sweeps] into a **26%-short-float, HTB, covering name** [SENT:short_float] — latent squeeze fuel — **but the empirical edge is negative**: bullish_flow backtest wins **20% (n=5)** [HIST], **raw_kelly −0.143**, dealers **long-gamma 30/30 sessions** with **July max-pain pinned $6.00** [STRUCT:max_pain], desk went **0-for-4 directional**, debate **DISCONFIRMED** (bear 0.75 ≥ bull 0.55).
- **Levels:** support 5.50 (= gamma_flip), resistance 6.33, largest_pin 6.00.
- **IV rank 42.5**; **VRP −0.17 → PREMIUM_BUYING** (cheap vol favors *buying* debit legs, not selling). Front-expiry expected move only **±2.42% / ±$0.14** (near-term priced move is tiny — the squeeze isn't priced).
- **Catalysts:** July OPEX Jul-17 ($6 max-pain magnet) · **ENVX Q2 earnings ~Aug-12** (UW shows 07-30 — flagged likely stale; this is the squeeze trigger).
- **Gates:** fundamentals CONFIRM, sentiment CONFIRM, **crowd CROWDED_SHORT** (squeeze fuel), rotation **adverse** (Industrials −$61.6M out), debate DISCONFIRMED.
- **Recommended structures (carry-only, defined-risk debit):** (1) call debit 6/8 **Oct-16** (debit ~$0.80, BE $6.80) — squeeze lottery held *through* Aug-12 earnings; (2) put debit 5.5/4.5 Oct-16 (debit ~$0.40, BE $5.10) — trend-continuation hedge toward the 52w low. Together = cheap long-optionality on a violent range break (exploits PREMIUM_BUYING).

### Key structural contrast vs a normal fade
Unlike a pre-earnings name, ENVX's edge (if any) is a **squeeze that needs the Aug-12 catalyst**, so the sanctioned structures are **long-dated Oct-16 debits held *through* earnings** — max-loss = premium, so an earnings gap cannot exceed it. "Don't hold through earnings" does **not** apply here; the defined-risk debit is the mechanism that makes holding through the binary acceptable.

## Reasoning ledger (loaded `trade-plans/_eval/reasoning-ledger.md`)
- **L-0002 — DIVERGENT flow↔chart is not a directional trade** · **ACTIVE** · `setup:divergent`. → **APPLIES.** Bullish $6-Oct call flow vs. a full bearish downtrend (price below all SMAs, MACD bearish). Default RANGE / defined-risk only; log divergence as a top reason_against. Thread into A3.
- **L-0004 — bearish-sweep short in short-gamma + bullish catalyst + VETO = trap** · **CANDIDATE** · `structure:short-gamma`. → **does NOT match** (this is a *bullish* sweep in a *long-gamma* name). Mirror-image cautionary read instead: a lone bullish sweep into a long-gamma $6 pin with no catalyst until ~Aug-12 is a **trap for the bull** — the pin caps the very breakout the $6 calls need. Carry as context, not a binding rule.
- **L-0001 — don't size a breakout at full until the break holds** · ACTIVE · `pattern:triangle/flag`. → evaluate after A2.
- **L-0003 — stale flow decays** · ACTIVE. → **does NOT apply** (deep dive 1 day old).
- `ledger_lessons_applied` (carry to A4): **L-0002**; L-0004 mirror-cautionary; L-0001 pending A2; L-0003 n/a.

## Chart source probe (smoke test)
- `chart_engine.py --ticker ENVX --date 2026-06-27` → **`available: true`**, **source = `yfinance`** (373 daily sessions). B1 is **not** a gap.
- Spot $5.95 (chart) = $5.95 (deep dive) — identical.
- Snapshot: ma_stack **mixed/bearish** (spot 5.95 < sma20 7.08, sma50 6.83, sma200 7.72), RSI14 40.21, MACD hist −0.158 (bearish), ATR14 0.56 (**10.49%** — very volatile, typical of a $6 name), 52w range $4.84–$15.93 (spot near the low). → chart is structurally **bearish/down-trending**.
- No tool errors.

## Verdict for downstream
- `deep_dive_reused`: **research/ENVX/2026-06-26** (age **1 day**, fresh)
- `flow_source`: **deep_dive**
- `chart_source`: **yfinance** (373 sessions)
- `ledger_lessons`: **L-0002** (ACTIVE, apply); L-0004 (mirror-cautionary); L-0001 pending A2; L-0003 n/a
- Setup signature: **DIVERGENT (bullish lone-sweep ⟂ bearish downtrend) + negative empirical edge + long-gamma $6 pin + CROWDED_SHORT squeeze fuel + cheap VRP (PREMIUM_BUYING) + squeeze needs Aug-12.** Expect A1 → likely SUFFICIENT/USABLE; A3 → **RANGE**, conviction floor 0.55, **directional size 0%**, expressed only as cheap two-way long-optionality debits.
