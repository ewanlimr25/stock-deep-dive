# Phase 3 — Open Interest & Positioning

**Ticker:** SMH
**As-of date:** 2026-05-28
**Generated:** 2026-05-29T12:30:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-0.5-context.md

## Summary

Positioning is a **large, broad protective put build**: net put OI grew **+86,442**
contracts today vs net call OI **+10,858** — an **~8:1 put-to-call OI build**, with
puts dominating *every* tenor bucket (0-8DTE 15:1, 9-30DTE 3:1, 31-90DTE 13:1, 90+DTE
3:1) `[OI:biggest_increases DUCKDB]`. The single dominant build, **530P 06-05
+50,795** (vol 53,530, avg $2.75, ~12% OTM), is **largely a ROLL** of a standing
hedge: the **530-strike dte1 (05-29) position fell −40,726** the same session
`[OI:decrease_with_volume]`, so ~40k of the 50.8k is an existing protective put
rolled forward one week, not a fresh directional short. `smart-positioning`
classifies the meaningful builds **bearish** (530, 475, 550, 545, 410 — all puts)
`[OI:smart_positioning]`, but in context (phase-1 collar + phase-2 basket-hold) this
is **hedge maintenance into strength**, not conviction shorting. No pin/cliff risk
this week (SMH absent from both pin-risk and opex-concentration).

## Key signals

- **Net put OI +86,442 vs call +10,858 (~8:1)** — systematic put accumulation
  `[OI:biggest_increases DUCKDB]`.
- **530P 06-05 +50,795** is the marquee build but **~40,726 is a roll** from the
  expiring 530P 05-29 (−40,726) — a standing 12%-OTM hedge rolled forward
  `[OI:decrease_with_volume]`.
- **Multi-tenor put floor:** 475P 08-21 +7,983, 475P 07-17 +4,159, 530 08-21 +4,015,
  500P 07-17 +3,325, 550P 06-18 +2,715, 545P 06-26 +2,004, 520P 09-18 +1,348 — a
  laddered downside hedge stack `[OI:biggest_increases]`.
- **Modest call retention:** call OI +10,858 (spread, no single large speculative
  call strike) — upside kept small but present `[OI:biggest_increases DUCKDB]`.
- **No pin/cliff this week** — SMH absent from pin-risk (dte≤7) and
  opex-concentration (≥40%); OI is spread across strikes `[OI:pin_risk][OI:opex_concentration]`.

## Detailed findings

### Net OI change by type (SMH, parsed from OPRA symbol) `[OI:* DUCKDB]`

| Type | Strikes | Net OI Δ | Volume |
|------|---------|----------|--------|
| Calls | 746 | **+10,858** | 40,568 |
| Puts | 807 | **+86,442** | 301,295 |

### OI build by DTE bucket × type (builds only, oi_diff>0) `[OI:* DUCKDB]`

| Bucket | Call build | Put build | put:call |
|--------|-----------|-----------|----------|
| 0–8DTE | +6,202 | **+96,656** | ~15:1 |
| 9–30DTE | +5,707 | +16,791 | ~3:1 |
| 31–90DTE | +1,950 | **+25,313** | ~13:1 |
| 90+DTE | +3,084 | +10,399 | ~3:1 |

Puts dominate at every tenor. The 0-8DTE bucket is inflated by the 530P roll; the
**31-90DTE +25,313 put build** (July-August 475/500/530 strikes) is the cleaner
"new protection" signal — institutions extending the hedge stack into Q3.

### Largest OI increases

| Strike | DTE | OI Δ | Vol | Avg px | read |
|--------|-----|------|-----|--------|------|
| 530P | 8 (06-05) | +50,795 | 53,530 | $2.75 | dominant — mostly **roll** from 530P 05-29 |
| 475P | 85 (08-21) | +7,983 | 8,015 | $13.26 | Q3 downside floor |
| 405P | 8 (06-05) | +4,650 | 5,501 | $0.28 | cheap convex tail |
| 475P | 50 (07-17) | +4,159 | 7,294 | $6.33 | July hedge |
| 530P | 85 (08-21) | +4,015 | 4,041 | $26.97 | Q3 hedge |
| 500P | 50 (07-17) | +3,325 | 5,372 | $10.65 | matches phase-1 500P 07-17 $3.56M |
| 550P | 21 (06-18) | +2,715 | 3,272 | $11.74 | June monthly hedge |
| 545P | 29 (06-26) | +2,004 | 2,011 | $12.84 | late-June hedge |
| 520P | 113 (09-18) | +1,348 | 1,450 | $29.36 | aligns w/ 575P/635C 09-18 collar expiry |

(0DTE 400/405 penny puts +5,249/+6,330 are pin noise.)

### Closing / roll activity

| Strike | DTE | OI Δ | Vol | read |
|--------|-----|------|-----|------|
| 530 | 1 (05-29) | **−40,726** | 55,337 | **rolled → 530P 06-05** (the hedge moves forward) |
| 760C | 50 (07-17) | −3,356 | 209 | phase-1 760C $3.12M closed |
| 540 | 21 | −3,575 | 1,240 | June position trimmed |
| 475 | 21 | −1,838 | 5,122 | June hedge rolled to July (475P 07-17 +4,159) |
| 545 | 21 | −1,817 | 2,430 | rolled to 545P 06-26 |

The signature is **rolling protective puts forward and out** — near-DTE closes (530,
475, 545 dte1/dte21) re-opening as 06-05/06-26/07-17 builds. `position-rolls` returned
0 rows (its strike-match heuristic didn't span the dte1→dte8 530 boundary), but the
paired OI deltas make the roll unmistakable `[OI:position_rolls]` (tool empty — manual inference).

### Smart positioning (inferred direction)

Meaningful builds classified **bearish**: 530 dte8 (+50,795), 475 dte85 (+7,983),
530 dte85 (+4,015), 550 dte21 (+2,715), 545 dte29 (+2,004), 410 dte15 (+1,999). The
"bullish"-tagged rows are mostly 0DTE penny strikes (400/405/402.5) = noise, plus
small 500/520 builds (likely put-selling/financing) `[OI:smart_positioning]`.

### Pin risk / OPEX concentration

SMH appears in **neither** pin-risk (dte≤7, max 5% distance) nor opex-concentration
(≥40%). Nearest weekly OPEX is 06-05 (8 DTE, just outside the window); monthly is
06-19 (22 DTE). OI is spread across many strikes — **no single-strike cliff or pin
mechanic to trade around this week** `[OI:pin_risk][OI:opex_concentration]`.

## Tool calls (audit trail)

| Command | Result summary |
|---------|----------------|
| `uw oi biggest-increases --symbol SMH --min-oi-change 500` | 530P 06-05 +50,795 dominant; laddered put builds |
| `uw oi decrease-with-volume --symbol SMH --min-volume 100` | 530 dte1 −40,726 (the roll); 760C closed |
| `uw oi smart-positioning --symbol SMH` | meaningful builds bearish (puts) |
| `uw oi position-rolls --symbol SMH --near-dte-max 30` | 0 rows (missed the dte1→dte8 530 roll) |
| `uw oi pin-risk --dte-max 7` | SMH absent |
| `uw oi opex-concentration --min-concentration-pct 40` | SMH absent |
| DuckDB (OI Δ by type/tenor, OPRA-parsed) | puts +86,442 vs calls +10,858 (~8:1) |

## Tool errors

(none — `position-rolls` returned empty, not an error.)

## Verdict for downstream

- **Positioning bias:** **Puts being built (protective hedges), heavily** — net put
  OI +86,442 vs call +10,858 (~8:1), laddered across all tenors. The dominant near
  strike is a **rolled** hedge (530P 05-29→06-05), so this is **hedge maintenance
  into strength, not a fresh directional short**. Reads consistent with phase-1
  (collar + put buying) and phase-2 (basket held, not dumped).
- **Conviction:** **4/5 that this is protective positioning**; **2/5 that it implies
  a directional-bearish view** (the roll character + modest −$0.38bn net delta).
- **Largest OI build as % of float:** **n/a** — SMH is an ETF (no float). For scale,
  +86,442 net put OI ≈ 8.64M share-equivalents notionally hedged — meaningful but
  small vs SMH's ~114M shares outstanding / $68B AUM.
- **Three pin/cliff strikes for phase-9:**
  1. **530** — the hedge line; heaviest put OI build and the rolled-hedge strike.
     If spot breaks toward it, dealer short-gamma below could accelerate (resolve in
     phase-4 GEX).
  2. **475** — laddered Q3 downside floor (08-21/07-17 builds); aligns with deeper
     protection, well below the $567.88 DP shelf.
  3. **565 / 550** — mid put strikes (565P 06-26, 550P 06-05/06-18); 550 is the
     marquee phase-1 sweep strike.
- **Open questions:** Does phase-4 GEX show dealers **short gamma below ~$565–575**?
  If so, the put hedges sit exactly where a down-move would be amplified — raising
  the value of the protection and the risk if spot breaks the $567.88 shelf. Is the
  modest call retention (+10,858) enough to call the structure a true collar vs a
  pure put overlay?
