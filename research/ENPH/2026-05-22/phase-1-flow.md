# Phase 1 — Options Flow

**Ticker:** ENPH
**As-of date:** 2026-05-22
**Generated:** 2026-05-25T22:43:20Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md

## Summary

The whole-tape aggregate is **genuinely call-skewed — call premium $27.64M vs put
$8.81M (3.1:1), net bullish +$5.55M, P/C 0.39** — and this is **day 5 of a persistent
sweep campaign** ($61.4M sweep premium over 5 sessions, in top sweeps every session).
But the campaign's `dominant_direction` is **"mixed," not bullish**, and the single
largest print of the day is a **$2.5M June-2027 $60 PUT** — so the flow is net-bullish
on premium yet two-sided in structure. Much of the call buying is **LEAP / deep-ITM
stock-replacement** (slow, institutional) plus one clean aggressive near-term sweep
(June $65C, ask, $1.55M); options are **extraordinarily rich (IV 79–130%, IV-rank 92)**,
so the read "is this outright-long conviction or vol-harvesting/overwriting?" is open
and handed to phases 3–4. Net bias **bullish, conviction 3/5** (capped by mixed sweep
direction + a $2.5M put + rich IV).

## Key signals

- Whole-tape **call premium 3.1× put premium**, net +$5.55M bullish [FLOW:insights_deep_dive]
- Sweep campaign **5/5 sessions, $61.4M, consistency 1.0 — but `dominant_direction=mixed`** [FLOW:sweep_persistence]
- Cleanest bullish print: **June-18 $65C, ASK side, $1.55M, 480 trades, 2401 ct** [FLOW:sweeps]
- Largest single print is bearish/hedge: **2027-06 $60P, $2.5M, 1392 ct, no_side** [FLOW:top_premium_trades]
- OTM June call OI building (70C +4,616 / 85C +2,518 / 80C +1,488) = **opening longs, not just overwriting** [FLOW:insights_deep_dive top_oi_changes]

## Detailed findings

### Whole-tape aggregate (read the top-N against THIS)

From `insights_deep_dive.uw_screener` (the entire tape, not top-N):

| Field | Value | Read |
|-------|-------|------|
| call_premium | $27,644,785 | — |
| put_premium | $8,811,335 | call/put premium **3.14:1** |
| bullish_premium | $18,086,596 | — |
| bearish_premium | $12,537,857 | **net_flow +$5,548,739** |
| put_call_ratio | 0.392 | call-heavy |
| call_volume / put_volume | 43,592 / 17,092 | 2.55:1 by volume |

The aggregate **confirms** the top-N direction (no AAPL-style top-N illusion here) —
the tape is genuinely call-skewed. The nuance is *structure/tenor*, not direction.

### Sweeps (ask vs bid, premium, tenor)

The two-sidedness lives here. Sorted by premium ([FLOW:sweeps]):

| Strike/Expiry | Type | Side | Premium | Trades | Read |
|---------------|------|------|---------|--------|------|
| $60 / 2027-06-17 | PUT | **no_side** | **$2.50M** | 1 | LEAP put block — largest print; bearish/hedge/structural |
| $65 / 2026-06-18 | CALL | **ask** | $1.55M | 480 | **Cleanest bullish** — aggressive near-term call buying |
| $50 / 2027-01-15 | CALL | bid | $1.32M | 56 | Deep-ITM LEAP call, bid — stock-replacement / possibly written |
| $100 / 2027-01-15 | PUT | bid | $0.90M | 2 | Deep-ITM LEAP put, bid (sold) — bullish-ish / structural |
| $50 / 2027-01-15 | CALL | ask | $0.85M | 47 | LEAP call buying — bullish |
| $60 / 2027-01-15 | PUT | bid | $0.70M | 184 | LEAP put, bid (sold) — bullish-ish |
| $60 / 2027-01-15 | CALL | ask | $0.67M | 26 | LEAP call buying — bullish |

Theme: **near-term clean bullish ($65C June ask) + a wall of LEAP positioning** across
2027-01, 2027-06, 2028-01 (calls bought at ask; puts mostly on bid = sold). The lone
counter is the **$2.5M 2027-06 $60P** — the day's biggest ticket, `no_side`,
delta −0.32, IV 79%. **→ phase 2 must cross-check** for near-simultaneous underlying
prints around its `executed_at` 16:26:26Z (12:26 ET) to tell married-put/collar from
outright bearish.

### New positioning (unusual vol, vol/OI)

`unusual_volume` (min vol/OI 3): the top vol/OI hits are **near-dated PUTS** —
5/29 $57P (29.7×), 2027-06 $60P (28.4×, the $2.5M block), 5/29 $63P, 5/29 $57.5P,
6/05 $55P — i.e. fresh **short-dated put positioning** alongside the calls. Fresh call
positions show at 5/29 $64C (6.1×), 6/05 $63C, 5/29 $63C, 6/26 $65C. So **both** new
puts (near-term, downside) and new calls are opening — consistent with the "mixed"
persistence tag.

OI changes (from `insights_deep_dive.top_oi_changes`) tell the cleaner directional
story — the biggest OI *builds* are **OTM June calls**: 70C +4,616, 85C +2,518,
80C +1,488 (all 27-DTE, OTM), plus 50P-Sept +1,721. OTM call OI building = **opening
long calls**, which argues the call flow is at least partly genuine direction, not
pure overwrite. (Phase 3 confirms.)

### IV outliers + Greeks

IV is uniformly extreme: near-dated contracts 90–130% IV; the 0DTE $60C printed
388% avg IV (pure pin noise — discount). Greek screener: the large call prints carry
**high delta (0.75–0.95)** — ITM/directional stock-replacement — while the lottery
calls ($170C/$175C 2027-01, delta ~0.17, ~$160K each ask) are cheap convexity bets on
a large move. Net: positioning spans deep-ITM stock-replacement → OTM lottery, i.e. a
**conviction-with-convexity** call book, financed partly by selling rich puts.

### Market-wide cross-checks

- `smart_money_flow` (bullish, market-wide top-25): **no ENPH contract present** — the
  list is SMH/GLD/TLT/index-put dominated. Not a negative; ENPH's per-contract size
  just isn't top-25 market-wide. Recorded, not re-run with looser thresholds.
- `sweep_ratio` (market-wide top-25): **no ENPH contract** — list is micro-name
  dominated. Uninformative for a liquid name.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__options_flow_sweeps` | `{symbol: ENPH, min_premium: 100000, top_n: 25, date: 2026-05-22}` | $2.5M 2027-06 60P (no_side) top; $1.55M June 65C ask = bullish |
| `mcp__uw-pp__options_flow_unusual_volume` | `{symbol: ENPH, min_vol_oi_ratio: 3, top_n: 25, date: 2026-05-22}` | fresh near-term puts (57/57.5/63) + calls (64/63) opening |
| `mcp__uw-pp__options_flow_top_premium_trades` | `{symbol: ENPH, top_n: 25, date: 2026-05-22}` | confirms $2.5M put + LEAP call ladder |
| `mcp__uw-pp__options_flow_iv_outliers` | `{symbol: ENPH, top_n: 15, date: 2026-05-22}` | IV 90–388%; options extremely rich |
| `mcp__uw-pp__options_flow_greek_screener` | `{symbol: ENPH, top_n: 15, sort_by: premium, date: 2026-05-22}` | call prints high-delta (stock-replacement) + low-delta lottery |
| `mcp__uw-pp__hot_chains_sweep_persistence` | `{symbol: ENPH, days: 5, top_n: 20}` (no date — flag rejected) | **5/5 sessions, $61.4M, consistency 1.0, dominant=MIXED** |
| `mcp__uw-pp__hot_chains_smart_money_flow` | `{direction: bullish, top_n: 25, min_volume: 500, date: 2026-05-22}` | no ENPH contract in market-wide top-25 |
| `mcp__uw-pp__hot_chains_sweep_ratio` | `{top_n: 25, min_volume: 500, min_sweep_ratio: 0.3, date: 2026-05-22}` | no ENPH contract (micro-name dominated) |

## Tool errors

- `hot_chains_sweep_persistence` with `date=2026-05-22` → `Error: unknown flag: --date`.
  Re-called **without** `date`; tool returned its own 5-session window
  (2026-05-18→05-22, ending on the as-of date) — correct for this run.

## Verdict for downstream phases

- **Bias from this phase:** **bullish, but mixed/two-sided** (net call premium 3:1,
  persistent 5 sessions; offset by a $2.5M LEAP put + "mixed" sweep direction + rich IV).
- **Conviction:** **3/5** (magnitude + persistence + cross-sectional rank support it;
  capped below 4 by two-sided structure and IV richness).
- **Three things later phases must remember:**
  1. **Net call premium 3.1:1 ($27.6M vs $8.8M), +$5.55M net, 5/5-session campaign**
     — direction is real, but the persistence tool calls it **"mixed."**
  2. **The single biggest print is a $2.5M 2027-06 $60 PUT (no_side, 12:26 ET)** —
     phase 2 must check the underlying tape around it (married-put vs outright bearish).
  3. **OTM June call OI is building (70/80/85C)** = opening longs; but IV-rank 92 means
     some flow may be financed by selling puts/overwriting — phases 3–4 resolve.
- **Open questions:**
  - Is dark pool confirming the bullish premium with accumulation, or is the $2.5M put
    a hedge against a long stock block? (→ phase 2)
  - Are the June OTM calls net-new opening interest (direction) or covered overwrite
    (income)? (→ phase 3 OI)
  - With IV-rank 92, does dealer positioning (GEX/vanna) favor a squeeze or a pin? (→ phase 4)
