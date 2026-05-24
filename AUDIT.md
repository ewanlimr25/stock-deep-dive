# stock-deep-dive — Capability Audit
_Audited: 2026-05-23 · Perspective: options trader / hedge fund PM / MM_

Rubric — **Impact:** CRITICAL/HIGH/MEDIUM/LOW/NICE · **Effort:** S(<1d)/M(1–3d)/L(1wk+) · **Edge:** A=alpha R=risk O=operational. Siblings: `claude-trading-agents`, `uw-daily-analysis` (both `/Users/ewan/Development/`).

## 1. What this repo does well
- **Most thorough single-name workup of the three.** 10 sequential phases (`phases/phase-0`…`phase-10`) walk flow → dark pool → OI → dealer structure → historical IV/VRP → macro → UW insights → 5-agent desk → trade blueprint → audit. Nothing in the set goes this deep on one ticker.
- **Only macro-aware repo.** Phase 6 pulls **hard FRED data** (CPI/PCE/NFP/Fed funds/10y-2y/2s10s) with WebSearch fallback — free, and a capability both siblings lack entirely.
- **Disciplined artifact hygiene.** Immutable, versioned outputs (`research/<T>/<date>/`, `-v2`/`-v3`, never overwrite) + verbatim tool-error surfacing. Reproducible and auditable per ticker-date.
- **Explicit invalidation framework.** `rubrics/invalidation-rubric.md` defines price/signal/macro kill-triggers — the trade has a written exit before it's entered.
- **Normalized 0–100 confluence score + contradiction log** (`rubrics/confluence-scoring.md`) — quantifies cross-phase agreement and *logs* disagreement rather than burying it.

## 2. Adopt from sibling repos
| From | Capability | Why it matters here | Impact | Effort | Edge |
|------|-----------|---------------------|--------|--------|------|
| uw-daily | Outcome-driven calibration (`/calibration-audit`: path-aware ±1R resolution, Brier, tool attribution) | **Phase 10 audits internal consistency, never whether the trade made money.** The entire confluence-score → conviction-bin apparatus is unfalsifiable without an outcome loop — you cannot allocate capital to a "score 85" blueprint you've never verified beats a "score 60" one | CRITICAL | M | A·O |
| uw-daily | Wire `historical_signal_backtest` win-rate into the Phase-9 sizing `p` | **Phase 5 already fetches the win-rate**; Phase 9's Kelly uses the conviction *bin* as `p` instead. The empirical edge is sitting one phase upstream, unused. Near-free fix, directly improves size calibration | HIGH | S | A·R |
| claude-trading-agents (**FINNHUB**) | Deep fundamentals as a Phase 7b: balance sheet / cash flow / income, earnings-surprise history, peer comps, insider MSPR | Phase 7 only has shallow UW `insights_deep_dive` (PE/short%/IV-rank). A flow-confirmed long on a name with serial misses + deteriorating FCF deserves a fundamental veto — *filter the flow by quality of the underlying* | HIGH | M | A·R |
| uw-daily | Call the `uw-pp` tools the phases never invoke — `risk_portfolio_correlation`, `options_flow_sector_flow_persistence` (uw-daily already uses both on the same server) | Phase 6 has `market_regime` but the phases never invoke portfolio correlation or sector rotation, though `uw-pp` already exposes both. Concurrent deep dives could be one correlated bet with no flag. This is a prompt gap, not a data gap — the tools are one call away | MEDIUM | S | R |
| claude-trading-agents | Bull/bear debate between Phase 8 and Phase 9 (1–2 rounds) | The Phase-8 desk is **additive** — 5 agents each return a verdict that adds to confluence; none rebuts the others. A bear case stress-tests before the blueprint is written | MEDIUM | M | R |
| claude-trading-agents | Pydantic `decision.json` beside `phase-9-trade-plan.md` | Output is markdown only; a structured envelope makes blueprints machine-resolvable by the outcome loop above | MEDIUM | M | O |

### Status — all six adopted (2026-05-23)

| Capability | Landed in |
|------------|-----------|
| Outcome-driven calibration | **`commands/deep-dive-calibration.md`** — 7-phase propose-only audit; resolves `research/*/decision.json` to WIN/LOSS path-aware ±1R, Brier by confluence band (incl. `conviction` vs `kelly_p`), phase+tool attribution, gate-efficacy. Referenced from SKILL.md + README. |
| Backtest win-rate → sizing `p` | `rubrics/sizing-rubric.md` §"Choosing the Kelly `p`" (uw-daily N-cap + sizing map + SHORT floor); `phases/phase-5-historical.md` emits the sizing handoff block; `phases/phase-9-trade-plan.md` step 1 reads it. |
| Deep fundamentals (FINNHUB) | **`phases/phase-7b-fundamentals.md`** — statements / 8-q surprise / peers / MSPR via free Finnhub REST (curl+jq, `.env` key, graceful skip). `tier_adjustment` CONFIRM/CAUTION/VETO/NA is a phase-9 sizing gate. New `[FUND:]` tag. |
| Uncalled `uw-pp` tools | `phases/phase-6-macro.md` now invokes `options_flow_sector_flow(_persistence)` + `risk_portfolio_correlation`; phase-9 applies the rotation + correlation-cluster gates; phase-8 risk-monitor reads them. |
| Bull/bear debate | **`phases/phase-8b-debate.md`** — 1–2 rounds, sycophancy guard + residual bins; phase-9 debate-disconfirmation gate; −5 confluence penalty in `rubrics/confluence-scoring.md`. |
| Structured `decision.json` | `schemas/decision.schema.json` + stdlib `schemas/validate_decision.py` + `templates/decision-template.json`; phase-9 emits & validates, phase-10 backfills the score. |

## 3. Shared infrastructure to extract
- **No UW infra gap — both UW repos already share `uw-pp`.** This repo and `uw-daily` consume the *same* consolidated server (`mcp__uw-pp__*`, ~58 tools), which replaced the legacy 11-server split for speed/token savings. The sector-rotation and portfolio-correlation tools this repo appears to "lack" are **already exposed by `uw-pp`** — the `phases/` prompts simply never call them. The fix is a prompt change (invoke the tools), not an infra/server change. The genuinely sharable cross-repo assets are *prompts and rubrics*, not servers.
- **FRED macro block is this repo's exportable asset.** `phases/phase-6-macro.md` is self-contained (free key + `curl` + WebSearch fallback). Package it as the canonical macro overlay both siblings copy. Because the siblings differ in language (one Python, one markdown), share it as a **documented phase/rubric**, not a code module.
- **Sizing/conviction rubrics are triplicated.** `rubrics/sizing-rubric.md` (fractional Kelly 0.25, cap 5%) + `confluence-scoring.md` bins {0.55…0.95} mirror `claude-trading-agents/kelly.py`. They cannot share a package (this repo runs no code). Adopt `uw-daily`'s win-rate-cap table as the **canonical sizing rubric** and copy it — keep one source-of-truth document, three copies.
- **Net-new shared gap: a market/holiday calendar** for DTE, expected-move √t, and OPEX-window math. None of the three has one; matters for every dated structure here.

## 4. Missing capabilities the trader desk would want
**CRITICAL — No outcome feedback.** Detailed in §2. A research workflow that never marks its own blueprints to market is a hypothesis generator, not an edge. This is the gap that most undermines trusting the output with capital.

**HIGH — Realized win-rate fetched but unused at sizing.** §2. The cheapest high-impact fix in the entire three-repo set: the data is already in the Phase-5 file.

**HIGH — Thin fundamentals.** §2. Only UW `insights_deep_dive`; no statements, no earnings-surprise history, no peer relative-value.

**MEDIUM — Short interest + borrow rate.** Squeeze/HTB context absent — material for interpreting a bullish-flow long thesis on a heavily-shorted name.

**MEDIUM — Expected-move calc around the catalyst.** Phase 6 lists the catalyst calendar; the blueprint never computes the straddle-implied move, so entry/structure aren't sized to the event's priced range. The IV data (Phase 4/5) is on hand to do it.

**MEDIUM — No candidate generation.** Requires a user-supplied ticker; `uw-daily`'s screener fleet could feed it (natural pipeline: daily scan → deep dive on the conviction names).

**Out-of-scope:** execution/slippage — this produces a blueprint a human trades. Correctly omitted.

**Rejected framing:** "adopt UW flow" is not a gap — this repo **already** has UW flow/dark-pool/gamma via `uw-pp`, the same consolidated server `uw-daily` uses. Its real gap is *unused* `uw-pp` tools (sector rotation, portfolio correlation — available but never called) plus the absent calibration loop, not flow or server access.

## 5. Top 3 actions (P&L-weighted)
1. **Wire Phase-5 backtest win-rate into Phase-9 sizing.** [HIGH·S·A·R] Replace conviction-bin-as-`p` in `rubrics/sizing-rubric.md` / `phases/phase-9-trade-plan.md` with the `historical_signal_backtest` rate already fetched in Phase 5, applying uw-daily's sample-size cap. *Edge:* immediate sizing-calibration improvement at near-zero cost — the data round-trip is already paid for. **Do this first.**
2. **Build `/deep-dive-calibration`.** [CRITICAL·M·A·O] Port `uw-daily/.claude/commands/calibration-audit.md`: resolve past `research/*/phase-9` blueprints to WIN/LOSS (path-aware ±1R), Brier-score by confluence band, attribute hit-rate to phases/tools. *Edge:* converts an unvalidated scoring system into a measured one — the precondition for trusting any of the above with size. *Sketch:* mirror the 7-phase audit; reuse this repo's invalidation rubric as the win/loss definition.
3. **Add deep fundamentals as Phase 7b (FINNHUB).** [HIGH·M·A·R] Pull statements + earnings-surprise + MSPR via `claude-trading-agents/dataflows/fetch_finnhub_*.py`; let it veto flow-confirmed theses on broken underlyings. *Edge:* filters the flow by quality of the business — avoids the long-thesis-into-a-deteriorating-balance-sheet trap that pure-flow depth can't see.
