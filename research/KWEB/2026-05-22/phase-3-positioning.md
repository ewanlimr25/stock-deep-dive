# Phase 3 — Open Interest & Positioning

**Ticker:** KWEB
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T00:00:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md

## Summary

OI positioning **adjudicates the phase-1 (bullish flow) vs phase-2 (DP
distribution) conflict toward a two-sided, range-bound read with a capped
upside**. There *is* genuine fresh bullish call buying — Dec-18 **30C +9,992** and
May-29 **28.5C +9,388** (net ask +10,158) — but phase-1 overstated the "bull
campaign": it is **matched by heavy call *writing* at 29.5–32** (Jun-26 30C sold
net −4,922, Jul-17 32C −3,569, Jun-05 29.5C −3,558, Jun-18 29C −1,594) and by
**fresh downside put buying at 25–26** (Jul 25P +7,116, Jul 26P +3,293). Offsetting
that, big June **31C/30.5C call walls were reduced** (−13,668 / −9,730) and large
**downside puts were closed/rolled** (Jun 35P −5,889, 34P −2,439; one detected
**put roll**: −20,964 near vs +9,600 far). Net: bulls own 28–30 calls, sellers cap
30–32, hedgers hold 25–26 puts. KWEB is **NOT** in the OPEX-week (05-29) pin list —
no near-term gamma pin. The OI mass sits in the **June monthly (06-18)** call walls.

## Key signals

- Largest fresh build: Dec-18 **30C +9,992 OI** (curr 15,260; $2.1M prev prem),
  inferred **bullish** `[OI:biggest_increases]` `[OI:smart_positioning]`.
- Strongest ask-side build: May-29 **28.5C +9,388** (net_ask_bid **+10,158**) —
  aggressive near-term upside bet on +6% by next Friday `[OI:smart_positioning]`.
- **Call writing caps upside:** Jun-26 30C (net **−4,922** bid), Jul-17 32C
  (**−3,569**), Jun-05 29.5C (**−3,558**), Jun-18 29C (−1,594) — sellers at 29.5–32
  `[OI:smart_positioning]`.
- **Downside put builds:** Jul-17 **25P +7,116** (ask) and **26P +3,293** (ask) —
  fresh bearish/hedge demand at 25–26 `[OI:biggest_increases]` `[OI:smart_positioning]`.
- June call walls reduced + downside puts closed: Jun-18 **31C −13,668**, 30.5C
  −9,730, **35P −5,889** ($8.4M prev prem), 34P −2,439 `[OI:decrease_with_volume]`;
  one **put roll** −20,964 near / +9,600 far `[OI:position_rolls]`.

## Detailed findings

### Largest OI increases `[OI:biggest_increases]` (spot $26.91)

| Strike/Expiry | Type | OI Δ | DTE | Inferred | Note |
|---------------|------|------|-----|----------|------|
| Dec-18 30C | call | +9,992 | 210 | bullish | largest; LEAP-ish upside |
| May-29 28.5C | call | +9,388 | 7 | **bullish (ask +10,158)** | near-term bull bet |
| Jun-05 29.5C | call | +7,172 | 14 | **bearish (bid −3,558)** | **sold** calls |
| Jul-17 25P | put | +7,116 | 56 | bearish (ask +1,430) | downside hedge |
| Jul-17 28C | call | +5,819 | 56 | bullish (≈flat) | |
| Jun-26 30C | call | +4,898 | 35 | **bearish (bid −4,922)** | **sold** calls (covered/cap) |
| Jul-17 26P | put | +3,293 | 56 | bearish (ask +803) | downside hedge |
| Nov-20 32C | call | +2,457 | 182 | bullish | far upside |
| Jul-17 32C | call | +1,138 | 56 | **bearish (bid −3,569)** | **sold** calls |
| Jun-18 25.5P | put | +1,743 | 27 | bullish (bid, **sold** put) | willing to own |

**Read:** call demand is concentrated at **28–30** (bull), but **30–32 is being
written** (cap), and **25–26 puts are being bought** (hedge). Mixed, with upside
contained near 30–32 and the June call walls above.

### Closing / roll activity `[OI:decrease_with_volume]` `[OI:position_rolls]`

- **Jun-18 31C −13,668** (curr OI still 151,062) and **30.5C −9,730** — the big
  June call walls being trimmed (upside conviction *reduced*, not added).
- **Jun-18 35P −5,889** (prev prem $8.4M) and **34P −2,439** ($2.6M) — large
  in/near-the-money downside puts **closed** → protection coming off (mildly bullish,
  but these are the deep-ITM "structural" puts phase-1 flagged).
- May-29 27P −2,719 closed (bullish, near puts gone).
- **Position roll (1):** put roll, near −20,964 / far +9,600, balance 0.458 — a
  large near-term put position retired, partly extended. Net **near-term downside
  protection reduced**.

### Smart positioning (inferred) `[OI:smart_positioning]`

Tally of the top builds: ~6 bullish (call buys + put sells: Dec 30C, May 28.5C,
Jul 28C, May 29C, Nov 32C, Jun 25.5P-sold, Dec 26P-sold) vs ~6 bearish (call
writes + put buys: Jun-05 29.5C, Jun-26 30C, Jul 32C, Jun-18 29C, Jul 25P, Jul
26P). **Genuinely balanced** — not the clean bull tape phase-1 reported. The single
most aggressive print is bullish (May 28.5C, +10,158 ask), but the aggregate is a
two-way book.

### Pin risk (OPEX week 05-29) `[OI:pin_risk]`

**KWEB absent** from the dte_max=7 pin list — no strong near-term gamma pin. Notable
China/EM peers *do* pin this week: **FXI** (spot 35.51, pin 37, score 303k) and
**EEM** (spot 65.89, pin 65, score 305k) — phase-6 should note EM/China OPEX
mechanics, but KWEB itself is unpinned near-term.

### OPEX concentration / call walls `[OI:opex_concentration]` `[OI:decrease_with_volume]`

KWEB absent from the ≥40%-concentration list (OI is spread, not single-expiry). The
**OI mass is the June 06-18 monthly**: standing OI **31C 151,062, 30C 97,085, 35C
~71–73k, 29C 43,307**. These 30–31 call walls (≈+11–15% above spot) are the
structural upside magnets/resistance — and they were being *reduced* today.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `oi_biggest_increases` | KWEB, top20, min500 | Dec 30C +9,992; May 28.5C +9,388; Jul 25P +7,116 |
| `oi_decrease_with_volume` | KWEB, top15, min100 | Jun 31C −13,668; 35P −5,889 closed |
| `oi_smart_positioning` | KWEB, top20, min500 | ~balanced bull/bear; call writing 29.5–32 |
| `oi_position_rolls` | KWEB, thr500, near≤30 | 1 put roll: −20,964 near / +9,600 far |
| `oi_pin_risk` | top25, dte≤7, ≤5% | **KWEB absent**; FXI/EEM pin this week |
| `oi_opex_concentration` | top20, ≥40% | KWEB absent; OI mass = June 06-18 calls |

## Tool errors

(none)

## Verdict for downstream phases

- **Positioning bias:** **MIXED / range-bound, capped upside** — fresh 28–30 call
  buying (bull) offset by 30–32 call writing (cap) and 25–26 put buying (hedge);
  June 31C/30.5C walls trimmed; downside protection partly closed/rolled. This
  **partially confirms phase-1's bullishness but caps it**, and **softens phase-2's
  distribution** (protection is coming off, not piling on).
- **Conviction:** **3/5** — clean, high-volume OI data, but the read is genuinely
  two-sided; do not let phase-1's headline overstate one-way conviction.
- **Three pin/cliff strikes for phase-9:**
  1. **$30–31 (June 06-18 call walls: 31C 151k, 30C 97k OI)** — structural upside
     resistance/magnet; coincides with phase-1's 30–31 call buys and sits *above*
     phase-2's $28 DP supply. Reclaiming $28 then pushing to 30 is the bull path.
  2. **$25–26 (Jul 25P 13.1k / 26P 13.0k OI)** — downside hedge floor; a break of
     phase-2's $26.36 pre-mkt low exposes this zone.
  3. **No 05-29 weekly pin** — near-term price is *not* gamma-pinned; it can trend
     to the June walls rather than stick.
- **Open questions:**
  1. Is the 28–30 call buying **speculative or covered**? The simultaneous 30–32
     call *writing* suggests a chunk is overwriting/spreads, not naked long upside.
  2. Does dealer GEX/gamma flip (phase-4) reinforce the "unpinned, can trend" read,
     and where is the gamma flip relative to $26.91 and the $28 supply?
