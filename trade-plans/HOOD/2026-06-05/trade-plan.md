# Trade Plan — HOOD

**As-of date:** 2026-06-05
**Spot reference:** 82.47 (chart.json, yfinance)
**Voice:** desk PM running an institutional book
**Built from:** research/HOOD/2026-06-05/ (deep dive, age 0d) + chart engine (yfinance)

> *For research and educational use only. Not financial advice. Sizing,
> structures, targets and dates are illustrative.*

## 0. Information completeness (gap audit)

- **Verdict:** USABLE_WITH_GAPS — completeness 94%
- **Have:** flow, dark pool, OI + max-pain, dealer GEX/ZGL, historical win-rate, macro, fundamentals (VETO), sentiment, debate, chart + patterns, events.
- **Missing / how to source:**
  | Item | Severity | How to source |
  |------|----------|---------------|
  | Confirmation the short is real (close below 80 pin) | important | wait for 6/18 OPEX; re-pull `uw oi term-structure` + price |
  | Timing/likelihood of the SpaceX-IPO-access headline | **critical** | WebSearch + `finnhub_enrich.py` news monitor — this is the thesis-killer |

## 1. Direction & conviction

- **Bias:** SHORT — but **WATCH-ONLY** (0% directional)
- **Conviction:** 0.65 on the flow read, **cut to watch-only** by the fundamentals VETO + DIVERGENT flow/chart
- **Horizon:** 1-4w
- **Flow↔chart agreement:** DIVERGENT — bearish flow vs a bullish double bottom / range. Per the rubric, divergence ⇒ not a directional trade.

### Thesis

Flow and dealer structure are bearish — a 5-session $317.8M bearish sweep
[FLOW:sweep_persistence] into a short-gamma book (spot 6.5% below the 87.45 ZGL
[STRUCT:gex]) with 6/18 max-pain at 80 [STRUCT:max_pain] — but the chart will not
confirm (a medium double bottom, RSI 51 [CHART:double]) and fundamentals VETO the
direction, so this is watch-only with a defined-risk carry only.

### Why it should work (the short case)

- 5-session bearish sweep campaign $317.8M, consistency 1.0 [FLOW:sweep_persistence].
- Short-gamma book: spot 82.47 is 6.5% below the 87.45 ZGL [STRUCT:gex]; 6/18 max-pain gravity at the 80 pin (21.4% of OI) [STRUCT:max_pain].
- Price below the falling 200-day 103.29 [CHART:sma200].

### Why it may fail (and why this is watch-only)

- **FUNDAMENTALS VETO** — business quality contradicts the short; the bearish flow may be hedging [FUND:tier_adjustment].
- **Bear's strongest point:** a SpaceX-IPO-access headline gaps HOOD above 85 [SENT:company_news][DEBATE:strongest_bear_point] — the catalyst that breaks the short.
- **Short-gamma cuts both ways:** a reclaim-and-hold of the 87.45 ZGL flips dealers to buyers / squeeze [STRUCT:gex].
- **Chart won't confirm:** medium double bottom + range, RSI 51 [CHART:market_structure] — flow and chart DIVERGENT.

## 2. Levels to watch

| Level | Role | Source |
|-------|------|--------|
| 85.00 | stop | [OI:oi_by_strike] |
| 87.45 | gamma flip / ZGL | [STRUCT:gex] |
| 80.00 | target / pin | [STRUCT:max_pain] |
| 77.50 | target (1 ATR ext) | [CHART:atr14] |

## 3. Patterns forming (chart)

| Pattern | Direction | Confidence | Note |
|---------|-----------|-----------|------|
| double bottom | bullish | medium | argues AGAINST the short |
| symmetrical triangle | neutral | low | coiling; trade the break |

## 4. Upcoming events

| Date | Event | Impact |
|------|-------|--------|
| 2026-06-17 | FOMC (hawkish risk) | ? |
| 2026-06-18 | June OPEX / max-pain 80 | ? |
| undated | SpaceX-IPO-access headline (live) | + |

## 5. Invalidation

- **Price:** two daily closes above 85.00, or a reclaim-and-hold of the 87.45 ZGL — hard stop.
- **Signal:** net flow bullish ≥ +$5M for 2 sessions, or DP block buy_ratio ≥ 0.60, or conviction-matrix → DIRECTIONAL_LONG.
- **Macro:** dovish FOMC, or a confirmed SpaceX-IPO-access headline above 85.

## 6. Sizing

- Kelly p_raw 0.875 → capped 0.75 (n=8); b 1.0; raw Kelly 0.5 → fractional ceiling 5%.
- **Risk gates:** fundamentals **VETO** → directional **0%**; sentiment CAUTION; debate not disconfirmed; flow/chart DIVERGENT.
- **Final size: 0% directional** (watch-only). Defined-risk carry only at ≤0.3%.

## 7. Plan A — pure stock (short)

- **Direction:** short — **WATCH-ONLY, no size.**
- **Entry:** none now. Would only consider on a daily close below the 80 pin with flow still bearish AND the SpaceX-IPO risk resolved.
- **Stop:** 85.05 · **Targets:** 80.0 (pin) / 77.5 · **R:R to T1:** ~0.96 · **Size:** 0%.
- **One-liner:** Bearish flow but vetoed + a live bullish catalyst above 85 — do not short into that.

## 8. Plan B — options (target date + price)

### B1 — directional (vetoed, carry only)

- Bear put debit spread 84/80 exp 2026-06-18 · target_date 6/18 · target_price 80 · debit 2.2 · BE 81.8 · max loss 2.2 · **size 0% (VETO)**.

### B2 — defined-risk

- Call credit spread 86/90 exp 2026-06-18 · target_date 6/18 · target_price 80 · credit 1.4 · BE 87.4 · max loss 2.6 · size starter 0.3%. Short strike at the call wall; max loss if the ZGL-reclaim/SpaceX squeeze fires.

## 9. Monitoring checklist

- [ ] Watch for any SpaceX-IPO-access headline — instant invalidation above 85.
- [ ] Watch the 87.45 ZGL — a reclaim flips short-gamma to a squeeze.
- [ ] 6/18 OPEX: does price pin to 80 or break the call wall?
- [ ] Net flow / DP block buy_ratio for a bullish flip.

## 10. Reasoning-ledger lessons applied

- **L-0002** — DIVERGENT flow↔chart ⇒ not a directional trade; watch-only / defined-risk fade only.

## Citations

1. [FLOW:sweep_persistence] HOOD bearish sweeps 5/5 sessions, $317.8M — research/HOOD/2026-06-05/phase-1-flow.md
2. [STRUCT:gex] spot 82.47 is 6.5% below the 87.45 ZGL — research/HOOD/2026-06-05/phase-4-structure.md
3. [CHART:double] medium double bottom + range, RSI 51 — chart.json
4. [FUND:tier_adjustment] fundamentals VETO — research/HOOD/2026-06-05/phase-7b-fundamentals.md
