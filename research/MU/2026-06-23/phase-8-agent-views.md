# Phase 8 — Multi-Agent Analyst Desk (parallel)

**Ticker:** MU
**As-of date:** 2026-06-23
**Generated:** 2026-06-23
**Upstream phases cited:** phase-1 through phase-7c (full chain packed into each agent)

## Summary

Five specialists, **unanimous that there is no directional edge** — 4 NEUTRAL + 1 RANGE,
**average conviction 2.4/5**. Not one agent will take a directional long or short into the
binary; all converge on **"trade the vol event / defined-risk structure, not the side."** The
highest-conviction view is **earnings-scout (RANGE, 4/5): IV rank 100 + backwardation into a
100%-beat-rate name is RICH premium → a short-vol, defined-risk iron condor around max-pain
$1050, half-size.** The risk-monitor supplies the binding constraint: short-gamma (ZGL 1495 ≫
spot) means the post-print move *amplifies* and the implied ±10.9% is "a floor, not a ceiling,"
so **defined wings and NO naked short premium, half a unit.** The two reconcile on a
**defined-risk condor/fly** (wings cap the amplification breach). The three other desks
independently dismantle any directional thesis: accumulation-hunter shows the marquee $553M
"mega-buy" is a **post-close mechanical print** (institutional-accumulation NEUTRAL, VWAP above
close — no stealth bid); contrarian-scanner finds **no fadeable extreme** (P/C z 0.78, SI 3.35%);
sweep-tracker shows the "bullish" sweep tilt is **2027 LEAP duration**, orthogonal to tomorrow,
with the only near-dated print a **put hedge**.

## Agent verdicts table

| Agent | bias | conviction | horizon | one_line_take |
|---|---|---|---|---|
| accumulation-hunter | NEUTRAL | 2 | 1-5d | No stealth bid — the "mega buy" is a closing-cross print; vol event in an accumulation costume. |
| contrarian-scanner | NEUTRAL | 2 | 1-5d | No crowd to fade — book balanced, P/C & SI not extreme; won't bet a contrarian thesis the night before a vol bomb. |
| sweep-tracker | NEUTRAL | 2 | 1-5d | Sweep tape is two-sided theater — LEAP duration masquerading as conviction, one real near-dated print and it's a put hedge. |
| earnings-scout | RANGE | 4 | 1-5d | IV 100 into a 4-for-4 beater is rich premium — sell the crush with a defined-risk condor outside the band, not a naked straddle. |
| risk-monitor | NEUTRAL | 2 | intraday–1-5d | Half a unit, defined-risk only; you can't hedge a beta-2.16 binary gap — trade the structure, not the direction. |

## Per-agent details

### accumulation-hunter — NEUTRAL / 2 / 1-5d
- key_levels: support 1043.19 (then 1020.76, put-wall 1000); resistance 1133.99 (then call-wall 1200); invalidation: a long-accumulation read only validates if MU re-prints mega-tier buys **intraday** at/above $1058 with buy_ratio >0.8 and VWAP crosses back under spot.
- top_signal: Phase-2's mega-tier buy (0.859) is an **artifact** — the lone $553M / 522,285-sh block executed 2026-06-23T20:08:20Z (**post-close**, $1058.88 vs $1057.93 ask); $601M of top prints after-hours vs only $158M intraday; institutional-accumulation NEUTRAL (buy/sell 1.21, VWAP $1076.66 > $1051.77 close).
- top_risk: Short-gamma (Phase-4) + bullish fundamental veto (7b) + a binary print means one positive-guide gap can run MU back over the $1133 shelf and brutalize a fade.

### contrarian-scanner — NEUTRAL / 2 / 1-5d
- key_levels: support 1043; resistance 1134; invalidation: break <$1000 flips bearish-confirmed, sustained close >$1134 flips bullish-confirmed.
- top_signal: **No fadeable crowd extreme** — P/C z 0.78 and SI 3.35% both non-extreme, PCR 1.013 two-sided; no one-sided crowd to lean against the day before earnings.
- top_risk: A directional fade is a coin-flip on a ±10.91% binary gap; any edge is dwarfed by event variance + post-print IV crush.

### sweep-tracker — NEUTRAL / 2 / 1-5d
- key_levels: support 1043 (then 1020, put-wall 1000); resistance 1134 (then 1200); invalidation: post-print sweep regime — sustained ask-side call sweeps holding >$1134 flips LONG; sustained bid-side put sweeps breaking <$1020 flips SHORT.
- top_signal: Phase-1 — the only clean **near-dated** aggressive sweep is the lone $10.2M 1000p bought 3 days out (a **hedge**); the +$76.4M "bullish" tilt is **2027-12-17 LEAP buying** that doesn't speak to tomorrow.
- top_risk: Negative GEX + ZGL ≫ spot → the post-print move amplifies; NEUTRAL gets run over fast, and 88.9% bearish_flow (n=9) + the −12% break argue the break is down.

### earnings-scout — RANGE / 4 / 1-5d  *(highest conviction)*
- key_levels: support 1043 (then 1020, put-wall 1000); resistance 1134 (then call-wall 1200); invalidation: gap settles **outside** the ±10.9% band ($937–$1166) and holds → directional follow-through, condor breached.
- top_signal: IV rank 100 / IV30d 107% + front-end backwardation 1.252 against a **100% beat-rate base (7b)** → premium is **RICH** vs the actual outcome distribution; the edge is **short-vol, not long-vol**.
- top_risk: Negative GEX / ZGL 1495 ≫ spot + negative vanna → the move amplifies; a beat-gap-up or knife-catch gap-down can blow through a condor's short strikes before IV crush bails you out.
- **Proposed structure:** short iron condor centered on max-pain $1050, short strikes at/just outside the implied-move band (~937P / ~1166C), long wings for defined risk, **half size**. Do NOT buy vol (VRP −0.098 is parabola-distorted; realized collapses post-print).

### risk-monitor — NEUTRAL / 2 / intraday–1-5d
- key_levels: support 1043 (then 1020, put-wall 1000); resistance 1134 (then call-wall 1200); invalidation: any MU risk sized above **half** the regime-normal unit, OR any **naked** short-premium structure.
- top_signal: Phase-4 — GEX flipped to NEGATIVE/short-gamma, ZGL 1495 ≫ $1051.77, COMPLACENT-symmetric skew → the post-print move is **dealer-amplified, not pinned**; implied ±10.91% is a **floor, not a ceiling**.
- top_risk: Holding directional MU into an IV-100 binary at beta 2.16 in a TRANSITIONAL "half-size" regime while semis lead the bearish tape — a gap through 1043/1000 is a single-event correlated semis drawdown.
- **Sizing constraints phase-9 MUST honor:** (1) max risk = **0.5× normal unit, hard cap**; (2) **defined-risk only** — no naked short options (short-gamma + ZGL≫spot amplification + negative-vanna IV-crush dealer selling); (3) bullish fundamentals VETO a directional short, complacent skew + IV-100 argue against paying rich premium for one direction → a **defined-risk symmetric structure** (condor/fly around $1050, or a defined strangle if buying the move) is the only regime-consistent expression; (4) honor the 06-26 OPEX cliff (19.4% OI, PCR 2.13) if held past the print. No cross-name cluster (no concurrent blueprints), **but MU is not diversifiable from the semis complex** — it is the lead bearish name.

## Disagreements

No **bias** disagreement (RANGE ≈ NEUTRAL directionally — all five reject a side). The live
debate is **structural**, and it is the key input to phase-8b:
- **earnings-scout (sell vol, conv 4)** vs **risk-monitor (don't sell naked, conv 2)** — harvest
  the rich IV crush with a condor, *or* respect the short-gamma amplification that can breach it.
  They reconcile on a **defined-risk** condor/fly (wings satisfy risk-monitor; short strikes
  outside the band satisfy the breach concern), half-size. Phase-8b should stress-test whether
  the move exceeding ±10.9% is likely enough to favor *buying* a defined strangle over *selling*
  the condor.

## Tool errors

None. All five agent types available (no `MISSING:` lines). Sub-agents made minimal extra CLI
calls (accumulation-hunter 24 confirming the block timing; risk-monitor 2 fresh regime reads;
others 0–2) — well within the ~30-call phase budget.

## Verdict for downstream

- **Plurality bias:** **NEUTRAL / RANGE — 5 of 5 reject a directional side.** The trade is the
  vol event, not a long or short.
- **Average conviction (non-MISSING):** **2.4/5** (directional); the *one* high-conviction view
  (earnings-scout, 4/5) is a **short-vol / RANGE** call, not directional.
- **Three highest-quality signals across agents:**
  1. **Premium is RICH**: IV rank 100 + backwardation 1.252 into a 100%-beat-rate name → short-vol edge (earnings-scout) `[STRUCT:front_end_iv_ratio]` `[FUND:earnings_surprise]`
  2. **The "accumulation" is a mirage**: $553M block is a post-close mechanical print; institutional-accumulation NEUTRAL, VWAP $1076.66 > close (accumulation-hunter) `[DP:largest]` `[INSIGHT:institutional_accumulation]`
  3. **The move amplifies**: short-gamma, ZGL 1495 ≫ spot → implied ±10.9% is a floor not a ceiling (risk-monitor, sweep-tracker) `[STRUCT:gex]`
- **Open questions for phase-8b/9:** Sell the crush (condor) or buy the move (defined strangle)?
  The desk says defined-risk + half-size either way; phase-8b must adjudicate which side of vol
  the edge sits on, given (a) IV 100 rich vs (b) realized has *exceeded* implied and short-gamma
  can push the move past ±10.9%.
