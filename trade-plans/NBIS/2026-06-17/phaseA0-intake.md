# Phase A0 — Intake & Reuse Detection — NBIS 2026-06-17

- **Ticker / as-of:** NBIS / 2026-06-17 · version v1
- **Output dir:** trade-plans/NBIS/2026-06-17/
- **Deep dive reused:** research/NBIS/2026-06-17/ (decision.json present) — **age 0 days (same session)**, not stale.
  - Carried forward: bias LONG, conviction 0.55, horizon 1-5d, spot 280.91, sizing {p 0.375, b 1.73, raw_kelly 0.014, final 0.3%}, gates {fund CAUTION, sent CAUTION, crowd CROWDED_LONG, debate disconfirmed}, levels {support 267.5, resistance 300, largest_pin 267.5, gamma_flip 34.64 ⚠}, expected_move 4.86%/$13.66, context {GENUINELY_UNUSUAL, iv_rank 91.3}, catalysts (OPEX 6/18, NDX 6/22, CPI 7/15, ER 8/6).
- **Flow source:** `deep_dive` (no live re-pull needed; deep dive is same-session).
- **Chart source probe:** `chart_engine.py --ticker NBIS --date 2026-06-17` → `available: true`, source `yfinance`, 372 sessions. OK.
- **Ledger loaded:** trade-plans/_eval/reasoning-ledger.md — L-0001 (event/chart-leads sizing) is in scope for this momentum-into-catalyst setup; applied in A3/A4.

## Tool errors

None. One **data-quality flag** to carry to A1: reused `gamma_flip = 34.64` is implausible for a $280 underlying (likely a different scale) — do not trust it; re-source the ZGL.

## Verdict for downstream

deep_dive_reused = research/NBIS/2026-06-17/ (age 0) · flow_source = deep_dive · chart_source = yfinance · ledger lessons in scope: L-0001.
