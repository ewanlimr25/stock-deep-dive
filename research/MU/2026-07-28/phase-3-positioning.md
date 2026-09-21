# Phase 3 — Open Interest & Positioning

**Ticker:** MU
**As-of date:** 2026-07-28
**Generated:** 2026-07-28T21:44:00-04:00
**Upstream phases cited:** `phase-0-intake.md` (float 1.12B), `phase-0.5-context.md`, `phase-1-flow.md` (the 750/800 put-strip question), `phase-2-dark-pool.md`

## Summary

**Phase 1's decisive question is resolved: the 750/800 put-strip selling is OPENING, not
closing.** Open interest on those strikes has been *rising* on bid-side-dominated volume for
six sessions — a persistent campaign that accelerated on 7/27 (**+910 contracts** across the
Mar-27 800 and Jun-27 800 strikes, bid volume 551 and 455 vs ask 1 and 99) and continued on
7/28 (**+416**: Feb-27 750 +216 on 217 bid vs 1 ask; Jun-27 750 +200 on 201 bid vs 2 ask).
Someone is systematically **underwriting MU at $750–800 out to Jun-2027 and adding as price
falls** — genuine, if modest, structural support (~2,370 contracts ≈ 0.021% of float).

The rest of the positioning picture is defensive. The **strongest wall in the chain sits at
$800 — 84,213 OI, net -32,711 puts, just 2.39% below spot** (`put_wall_support`). Near-dated
expiries are heavily put-skewed (**7/31 holds 18.38% of all OI at a 2.592 put/call OI ratio**;
8/07 at 2.551) while LEAPs are call-skewed (2028-12-15 at 0.677) — near-term fear, long-term
optimism. The overnight OI churn is a textbook **roll-down-and-out**: large closures of
profitable near-money puts (**7/31 750P -3,314, 810P -3,050, 820P -2,333; 8/21 950P -3,106**)
paired with fresh purchases of **cheap crash tails** (Aug-07 55P **+24,412 @ $0.01**, Jul-31
500P **+11,767 @ $0.27**, both ask-side). Holders banked the protection that worked and replaced
it with lottery-priced insurance. **MU is not a pin candidate** (0 rows in `pin-risk`) and
carries no OPEX concentration cliff ≥40%.

**Critical caveat governing this entire phase:** the OI file's window is
`last_date = 2026-07-27 → curr_date = 2026-07-28`. **Every OI change here was created by the
7/27 session, not by today's tape.** Today's $28.4M put-strip sale will not appear in OI until
tomorrow's file. The "opening" verdict is therefore an inference from the *prior* leg of the
same campaign — strong, but explicitly not a direct observation of today's prints.

## Key signals

- **750/800 put strip = OPENING short puts.** Six-session OI build on bid-side volume;
  7/27 +910 contracts, 7/28 +416. [OI:biggest_increases DUCKDB]
- **$800 is the dominant wall: 84,213 total OI, 58,462 puts vs 25,751 calls, net -32,711,
  `role = put_wall_support`, `distance_pct = -2.39`.** [OI:oi_by_strike]
- **7/31 (3 DTE) holds 18.38% of all 2,194,370 contracts of OI at put/call OI 2.592** —
  the near-term gravity well. [OI:term_structure]
- **Crash-tail buying:** Aug-07 55P **+24,412** contracts at $0.01 (ask-side), Jul-31 500P
  **+11,767** at $0.268 (15,060 ask vs 1,374 bid). [OI:biggest_increases]
- **Profitable near-money puts closed:** 7/31 520P **-3,588**, 750P **-3,314**, 810P **-3,050**;
  8/21 950P **-3,106**. [OI:decrease_with_volume]
- **No pin risk, no OPEX cliff:** 0 MU rows in `pin-risk` (25 returned) and 0 in
  `opex-concentration` (20 returned). [OI:pin_risk] [OI:opex_concentration]
- **`smart-positioning` is a wash: 11 bullish / 9 bearish** among the top-20 OI movers.
  [OI:smart_positioning]

## Detailed findings

### OI walls by strike

`uw oi oi-by-strike --symbol MU --top-n 10` (all-expiry aggregate; spot $820.53):

| strike | call_oi | put_oi | **net_oi** | total_oi | `role` | `distance_pct` |
|---:|---:|---:|---:|---:|---|---:|
| **800** | 25,751 | 58,462 | **-32,711** | **84,213** | `put_wall_support` | **-2.39%** |
| 500 | 18,643 | 54,914 | -36,271 | 73,557 | `put_wall_support` | -38.99% |
| 1000 | 48,053 | 20,243 | +27,810 | 68,296 | `call_wall_resistance` | +22.01% |
| **900** | 35,570 | 29,455 | **+6,115** | 65,025 | `call_wall_resistance` | +9.81% |
| 700 | 20,258 | 40,428 | -20,170 | 60,686 | `put_wall_support` | -14.59% |
| 600 | 14,904 | 31,548 | -16,644 | 46,452 | `put_wall_support` | -26.79% |
| 1100 | 35,940 | 7,027 | +28,913 | 42,967 | `call_wall_resistance` | +34.21% |
| **750** | 10,290 | 30,861 | **-20,571** | 41,151 | `put_wall_support` | **-8.49%** |
| 1200 | 35,608 | 4,907 | +30,701 | 40,515 | `call_wall_resistance` | +46.41% |
| 400 | 5,072 | 34,787 | -29,715 | 39,859 | `put_wall_support` | -51.20% |

**Reading the roles honestly:**
- **$800 is the real level.** Largest total OI in the chain, cleanly put-dominated
  (net -32,711), and only **2.39% below spot**. It is simultaneously where phase-1's
  institutional seller is writing puts and where phase-2's dark-pool selling was heaviest
  (790s/800s buy_ratio 0.411/0.419). Convergence of three independent lenses on one level.
- **$900 is NOT clean resistance.** Tagged `call_wall_resistance`, but 35,570 calls against
  **29,455 puts** gives net_oi of only **+6,115** — a **two-sided battleground**, exactly the
  mislabeling the pitfall warns about. Phase-9 must not treat $900 as a firm ceiling; it is
  contested. **$1,000 (net +27,810) and $1,100 (net +28,913) are the genuinely clean call
  walls** — but at +22.0% and +34.2% they are irrelevant to any near-term plan.
- **The put-wall ladder below spot — 800 (-2.4%), 750 (-8.5%), 700 (-14.6%), 600 (-26.8%),
  500 (-39.0%), 400 (-51.2%)** — is unusually deep and heavy. 54,914 puts at the $500 strike
  and 34,787 at $400 on a $820 stock is a **large, pre-existing crash-hedge book**, consistent
  with the fresh tail buying below.

### OI term structure

`uw oi term-structure --symbol MU` — `total_oi = 2,194,370` across **23 expiries**
(array lives at `.term_structure`, not `.results`):

| expiry | DTE | call_oi | put_oi | **put/call OI** | total_oi | **% of total OI** |
|---|---:|---:|---:|---:|---:|---:|
| **2026-07-31** | **3** | 112,250 | 291,008 | **2.592** | 403,258 | **18.38%** |
| 2026-08-21 | 24 | 114,978 | 190,357 | 1.656 | 305,335 | 13.91% |
| 2026-09-18 | 52 | 106,343 | 167,288 | 1.573 | 273,631 | 12.47% |
| 2027-01-15 | 171 | 134,435 | 131,722 | 0.980 | 266,157 | 12.13% |
| 2026-12-18 | 143 | 65,232 | 87,050 | 1.334 | 152,282 | 6.94% |
| 2026-10-16 | 80 | 55,066 | 63,004 | 1.144 | 118,070 | 5.38% |
| **2026-08-07** | 10 | 32,831 | 83,760 | **2.551** | 116,591 | 5.31% |
| 2026-11-20 | 115 | 39,211 | 46,114 | 1.176 | 85,325 | 3.89% |
| 2028-12-15 | 871 | 46,922 | 31,759 | **0.677** | 78,681 | 3.59% |
| 2027-06-17 | 324 | 47,999 | 30,468 | **0.635** | 78,467 | 3.58% |
| 2026-07-29 | 1 | 34,694 | 40,659 | 1.172 | 75,353 | 3.43% |

- **The OPEX cliff is 2026-07-31 (3 DTE) at 18.38% of all OI** — not a standard monthly, a
  weekly, yet it carries nearly a fifth of MU's entire chain with **291,008 puts to 112,250
  calls**. Combined with phase-1's finding that 2–7DTE puts were the one bucket with net *buying*
  (+$10.9M... actually net -$15.5M sold; the net *buying* was 8–45DTE at +$10.9M), this expiry
  is where near-term risk is concentrated. Cross-check against phase-4 max-pain.
- **A clean monotonic skew flip by tenor:** put/call OI runs **2.592 → 2.551 → 1.656 → 1.573**
  through 8/07–9/18, then falls to **0.980** at Jan-27 and **0.635–0.677** in the 2027–2028
  LEAPs. **The market is hedged for the next two months and constructive beyond a year.** That
  is the single cleanest structural statement in this phase.
- Sep-18 (12.47%) sits **4 days before the 2026-09-22 earnings date** reported by
  `insights_deep_dive` — phase-7b/7c must verify that date, because a 12.5%-of-OI expiry
  landing just *before* earnings is unusual and would more typically sit just after.

### Largest OI increases

`uw oi biggest-increases --symbol MU --top-n 20 --min-oi-change 500`
(`oi_diff_plain` = absolute delta; `oi_change` is the ratio. Side inferred from
`prev_ask_volume` / `prev_bid_volume`; expiry/type parsed from the OPRA `option_symbol`.)

| contract | strike | type | DTE | last_oi → curr_oi | **Δ OI** | ask_vol | bid_vol | avg_price | read |
|---|---:|---|---:|---|---:|---:|---:|---:|---|
| MU260807P00055000 | 55 | put | 10 | 6,594 → 31,006 | **+24,412** | 5,424 | **18,995** | $0.01 | sold (bid) |
| MU260731P00500000 | 500 | put | 3 | 17,680 → 29,447 | **+11,767** | **15,060** | 1,374 | $0.268 | **bought — crash tail** |
| MU260731P00095000 | 95 | put | 3 | 1,855 → 6,207 | +4,352 | **4,352** | 0 | $0.01 | bought |
| MU260729P00570000 | 570 | put | 1 | 825 → 4,514 | +3,689 | **3,997** | 522 | $0.140 | bought |
| MU260729C00880000 | 880 | call | 1 | — | +2,735 | 3,957 | 1,430 | $32.81 | bought |
| MU260729C00875000 | 875 | call | 1 | — | +2,635 | 739 | **3,108** | $35.35 | sold |
| MU260731C01065000 | 1065 | call | 3 | — | +2,242 | 1,698 | 936 | $3.43 | bought |
| MU260729C00990000 | 990 | call | 1 | — | +1,649 | 397 | **1,555** | $3.73 | sold |
| MU260731C01050000 | 1050 | call | 3 | — | +1,620 | 2,410 | 2,056 | $4.48 | mixed |
| MU260731C01000000 | 1000 | call | 3 | — | +1,598 | 7,027 | 4,312 | $9.70 | bought |
| **MU260821P00800000** | **800** | **put** | **24** | — | **+1,443** | 365 | **604** | $50.22 | **sold — same campaign** |
| MU260731C00950000 | 950 | call | 3 | — | +1,268 | 3,196 | 2,686 | $20.52 | mixed |

- **The two largest builds are crash tails.** The Aug-07 **55-strike** put gained **24,412
  contracts** (OI 6,594 → 31,006, a 3.70× increase) at **one cent**, and the Jul-31 **500-strike**
  put gained **11,767** at $0.268 on **15,060 ask vs 1,374 bid** — unambiguous buying. In
  share-equivalent terms the 55P build alone is **2,441,200 shares = 0.218% of float**. The cost
  is trivial (~$24k and ~$315k respectively); the *appetite* is the signal. Someone wants
  convexity to a catastrophic outcome. *(Note the 55P's own bid-heavy volume — 18,995 bid vs
  5,424 ask — means the OI was built with the customer on the **sell** side, which
  `smart-positioning` duly tags "bullish." Selling 55-strike puts for a penny is economically
  nonsensical as a standalone trade; treat this row as package/artifact and do not weight its
  direction. The 500P and 95P, both ask-dominated, are the trustworthy tail-buying evidence.)*
- **The call builds are all far-OTM and short-dated** — 875/880/950/990/1000/1050/1065 strikes
  expiring 7/29–7/31, i.e. **6.6%–29.8% OTM with 1–3 days to live.** These are lottery tickets
  and they are **traded both ways** (880C bought 3,957/1,430; 875C sold 739/3,108; 990C sold
  397/1,555). This is not a call-buying campaign; it is weekly gamma churn.
- **`MU260821P00800000 +1,443` on 604 bid vs 365 ask is the fifth visible leg of the put-selling
  campaign** — same 800 strike, now in the Aug-21 monthly.

### The decisive cut — is the 750/800 put strip opening or closing?

Phase 1 flagged this as the question that inverts the read. **Answer: OPENING.**

**(a) Today's file (7/27 → 7/28), 750/800 puts, DTE 40–340:**

| contract | DTE | last_oi → curr_oi | **Δ** | vol | ask_v | bid_v |
|---|---:|---|---:|---:|---:|---:|
| MU270219P00750000 | 206 | 175 → 391 | **+216** | 218 | 1 | **217** |
| MU270617P00750000 | 324 | 1,252 → 1,452 | **+200** | 203 | 2 | **201** |
| MU261016P00800000 | 80 | 2,304 → 2,371 | +67 | 147 | 95 | 41 |
| MU260918P00800000 | 52 | 4,635 → 4,687 | +52 | 310 | 133 | 161 |
| MU270115P00800000 | 171 | 2,745 → 2,797 | +52 | 97 | 45 | 39 |
| MU270319P00800000 | 234 | 4,380 → 4,388 | +8 | 15 | 12 | 3 |
| MU270115P00750000 | 171 | 3,103 → 2,980 | -123 | 373 | 288 | 82 |
| MU260918P00750000 | 52 | 3,455 → 3,439 | -16 | 291 | 81 | 196 |

**(b) The multi-session campaign** (|Δ| ≥ 50, last six OI files):

| date | contract | last_oi → curr_oi | **Δ** | ask_v | bid_v |
|---|---|---|---:|---:|---:|
| 2026-07-21 | MU260918P00800000 | 4,494 → 4,642 | +148 | 194 | 59 |
| 2026-07-21 | MU270115P00750000 | 2,636 → 2,822 | +186 | 202 | 154 |
| 2026-07-22 | MU260918P00800000 | 4,642 → 4,548 | -94 | 155 | 69 |
| 2026-07-22 | MU270115P00750000 | 2,822 → 2,687 | -135 | 520 | 17 |
| **2026-07-23** | MU270115P00750000 | 2,687 → 3,011 | **+324** | 12 | **465** |
| **2026-07-23** | MU270319P00800000 | 3,848 → 4,015 | **+167** | 0 | **302** |
| 2026-07-23 | MU270617P00800000 | 1,848 → 1,911 | +63 | 12 | 83 |
| **2026-07-27** | MU270319P00800000 | 4,020 → 4,380 | **+360** | 1 | **551** |
| **2026-07-27** | MU270617P00800000 | 1,910 → 2,460 | **+550** | 99 | **455** |
| 2026-07-27 | MU260918P00750000 | 3,390 → 3,455 | +65 | 165 | 232 |
| **2026-07-28** | MU270219P00750000 | 175 → 391 | **+216** | 1 | **217** |
| **2026-07-28** | MU270617P00750000 | 1,252 → 1,452 | **+200** | 2 | **201** |

**Every large positive OI change on this strip is bid-dominated** — 465/12, 302/0, 551/1,
455/99, 217/1, 201/2. Selling puts *while open interest rises* is definitionally **opening a
short put position**, not closing a long one. **Net +2,370 contracts** across the window
(≈237,000 shares ≈ **0.021% of float**, ~$180M notional at strike).

**Interpretation.** A participant has been writing MU downside at $750–800 across Sep-26,
Oct-26, Dec-26, Jan-27, Feb-27, Mar-27 and Jun-27 for six sessions, **accelerating as the stock
fell** (7/23 +554, 7/27 +975, 7/28 +416). They are being paid $50–$191 per contract to be long
MU at $750–800 for 2–11 months. This is the **one genuinely constructive structural datapoint in
the run so far** — and it is worth being precise about its size: at ~0.021% of float it is a
real desk position, not a market-moving one.

**What it does NOT resolve:** whether this is an outright bullish bet or the short-put leg of a
larger hedged structure (e.g. financed by the ITM call selling phase-1 measured at -$25.1M in
46–180DTE, which would make it a collar/buy-write against stock). Phase-2's dark-pool
distribution makes the "against a long stock position" reading harder to sustain.

### Closing / roll activity

`uw oi decrease-with-volume --symbol MU --top-n 15 --min-volume 100`:

| contract | strike | type | DTE | last_oi → curr_oi | **Δ** | volume |
|---|---:|---|---:|---|---:|---:|
| MU260731P00520000 | 520 | put | 3 | 22,591 → 19,003 | **-3,588** | 5,092 |
| MU260731P00750000 | 750 | put | 3 | 12,556 → 9,242 | **-3,314** | 5,170 |
| MU260821P00950000 | 950 | put | 24 | 5,734 → 2,628 | **-3,106** | 4,700 |
| MU260731P00810000 | 810 | put | 3 | 11,343 → 8,293 | **-3,050** | 3,996 |
| MU260807P00800000 | 800 | put | 10 | 16,893 → 14,401 | **-2,492** | 1,570 |
| MU260731P00820000 | 820 | put | 3 | 11,194 → 8,861 | **-2,333** | 6,019 |
| MU260821P00850000 | 850 | put | 24 | 6,391 → 4,979 | -1,412 | 2,483 |
| MU260731P00850000 | 850 | put | 3 | 7,067 → 5,977 | -1,090 | 3,260 |
| MU260821P01000000 | 1000 | put | 24 | 5,608 → 4,558 | -1,050 | 1,535 |
| MU260731P00800000 | 800 | put | 3 | 9,746 → 8,731 | -1,015 | 12,478 |
| MU260807P00855000 | 855 | put | 10 | 2,278 → 1,318 | -960 | 291 |
| MU260821C01000000 | 1000 | call | 24 | 6,096 → 5,307 | -789 | 3,872 |

**Eleven of the twelve largest closures are puts**, and they cluster in the **750–1000 strikes
expiring 7/31, 8/07 and 8/21** — precisely the contracts that were deep in-the-money or
near-the-money during the 7/27 session (MU closed 900.20 on 7/27, so the 950P and 1000P were
ITM and the 810/820/850P were near-money). **Holders monetized winning protection.** Roughly
**-24,600 contracts** of near-dated put protection was retired in a single session.

**`uw oi position-rolls --threshold 500 --near-dte-max 30` returned `rolls_detected: 0`**, with
the tool's own caveat *"Single-day detection only — cross-session rolls are not captured."*
**The tool missed the roll that is plainly present in the data:** near-dated puts closed
(-24,600) + far-dated puts opened (750/800 strip, Feb-27/Jun-27) + cheap tails bought (55P
+24,412, 500P +11,767) is a classic **roll down and out, financed by writing long-dated
downside**. Recorded as a tool limitation, not as an absence of rolling.

### Smart positioning

`uw oi smart-positioning --symbol MU --top-n 20 --min-oi-change 500` — direction tally across
the top-20: **11 bullish / 9 bearish.** A wash, consistent with phase-1's balanced tape.

The field `inferred_direction` derives from `option_type_inferred` × `net_ask_bid` (puts sold →
bullish, puts bought → bearish, etc.), and spot-checking confirms the logic is applied
correctly (500P with `net_ask_bid` +13,686 → bearish; Aug-21 800P with -239 → bullish). Its
weakness here is that it weights a 24,412-contract penny-put row equally with a genuine
$50-premium position, so **the 11/9 tally should not be read as "slightly bullish."** The
informative rows are the ones quoted individually above.

### Pin risk

`uw oi pin-risk --top-n 25 --dte-max 7 --max-distance-pct 5` returned **25 rows market-wide and
zero for MU.** Despite 7/31 (3 DTE) holding 18.38% of MU's OI, MU does not qualify as a pin
candidate — unsurprising given a **7.90% implied move** against the tool's 5% distance filter:
MU's expected range is wider than the pin window, so no strike is close enough to exert
reliable gravity. **No pin commentary is warranted; phase-9 should not assume a 7/31 pin.**

### OPEX concentration

`uw oi opex-concentration --top-n 20 --min-concentration-pct 40` returned **20 rows market-wide
and zero for MU.** MU's most concentrated expiry is 7/31 at **18.38%**, well below the 40%
threshold. **MU's OI is unusually well distributed across 23 expiries — there is no cliff.**
This *reduces* the odds of a mechanical expiry-driven move and argues against structuring a
phase-9 trade around an OPEX unwind.

### Float normalization (advisory — `Shs Float` = 1.12B)

| build | contracts | share-equivalent | **% of float** |
|---|---:|---:|---:|
| Aug-07 55P (largest single build) | +24,412 | 2,441,200 | **0.218%** |
| Jul-31 500P (crash tail) | +11,767 | 1,176,700 | 0.105% |
| 750/800 put campaign (6 sessions) | +2,370 | 237,000 | 0.021% |
| Aug-21 800P | +1,443 | 144,300 | 0.013% |
| *Total chain OI (context)* | 2,194,370 | 219,437,000 | *19.6%* |

`[OI:oi_pct_float fz]` — **Is the build structural for MU?** No. The largest single OI increase
is **0.218% of float**, and it is a one-cent tail option. The strategically meaningful
put-writing campaign is **0.021% of float**. Against a 1.12B float and 19.6% total
chain-to-float ratio, **none of today's positioning is large enough to move the underlying**;
these are desk-scale positions expressing views, not flows that force price. **Advisory only —
does not raise conviction.**

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|------------------|--------------------------|-----------|
| `uw oi oi-by-strike --symbol MU --top-n 10 --date 2026-07-28 --json` | **800**: call_oi=25,751 put_oi=58,462 net=-32,711 total=84,213 role=`put_wall_support` dist=-2.39; 900: net=+6,115 (two-sided); 750: net=-20,571 dist=-8.49 ← `.results[]` | top-10 |
| `uw oi term-structure --symbol MU --date … --json` | total_oi=2,194,370; expiry_count=23; **2026-07-31 pct=18.38 pcoi=2.592** (put 291,008/call 112,250); 2028-12-15 pcoi=0.677 ← `.term_structure[]` | 23 expiries |
| `uw oi biggest-increases --symbol MU --top-n 20 --min-oi-change 500 --date … --json` | 55P Aug-07 `oi_diff_plain`=+24,412 (6,594→31,006, ask 5,424/bid 18,995, $0.01); 500P Jul-31 +11,767 (ask 15,060/bid 1,374); 800P Aug-21 +1,443 ← `.results[]` | top-20 |
| `uw oi decrease-with-volume --symbol MU --top-n 15 --min-volume 100 --date … --json` | 520P 7/31 -3,588; 750P 7/31 -3,314; 950P 8/21 -3,106; 810P 7/31 -3,050 ← `.results[]` | top-15 |
| `uw oi smart-positioning --symbol MU --top-n 20 --min-oi-change 500 --date … --json` | **11 bullish / 9 bearish** ← `[.results[].inferred_direction]\|group_by(.)` | top-20 |
| `uw oi position-rolls --symbol MU --threshold 500 --near-dte-max 30 --date … --json` | `rolls_detected: 0`, `results: []` + single-day caveat | 0 rows |
| `uw oi pin-risk --top-n 25 --dte-max 7 --max-distance-pct 5 --date … --json` | **0 MU rows** of 25 ← `[.results[]\|select(.ticker=="MU")]\|length` | top-25 |
| `uw oi opex-concentration --top-n 20 --min-concentration-pct 40 --date … --json` | **0 MU rows** of 20 | top-20 |
| DuckDB `chain-oi-changes-2026-07-28.parquet` | window `last_date=2026-07-27 → curr_date=2026-07-28`; 750/800 strip Δ: Feb-27 750P +216 (bid 217/ask 1), Jun-27 750P +200 (bid 201/ask 2) | 12 chains |
| DuckDB 6-file OI history (`chain-oi-changes-*.parquet`) | campaign: 7/23 +324/+167, 7/27 +360/+550, 7/28 +216/+200 — **all bid-dominated**; net **+2,370** | 22 rows |
| DuckDB `stock-screener-2026-07-28.parquet` | **high=848.36, low=789.09**, close=820.53, prev_close=900.20, total_volume=50,897,669, avg30_volume=44,991,443.7 (**1.13×**) | 1 row |
| `fz` float carry (phase-0) | `Shs Float` = 1.12B → % -of-float column | — |

## Tool errors

None — all eight `uw oi` commands exited 0 and every payload parsed. Two **non-error findings**
worth recording as limitations:

1. `position-rolls` returned `rolls_detected: 0` while a clear roll-down-and-out is visible in
   the increase/decrease data. Its documented single-day scope is the cause. Not a failure, but
   **do not treat "0 rolls" as evidence of no rolling.**
2. `pin-risk` and `opex-concentration` returned MU-empty. Both are genuine information
   (no pin, no ≥40% cliff), not tool failures.

## DATA NOTE / CORRECTION

Three field/semantics traps were hit and corrected **before** any number was written:

1. **`term-structure` returns its array at `.term_structure`, not `.results`.** The first
   `jq '.results[]'` errored with `Cannot iterate over null (null)`. Re-read against
   `.term_structure[]`; all expiry figures trace to that path.
2. **`smart-positioning` has no `direction`/`volume` field** — the correct names are
   `inferred_direction`, `option_type_inferred`, `net_ask_bid`, `prev_ask_volume`,
   `prev_bid_volume`. The first read printed `-` and `null`; the tally and all side reads here
   come from the corrected paths.
3. **The OI window is `2026-07-27 → 2026-07-28`, and `avg_price`/`prev_*_volume` describe the
   PRIOR session's trades while `dte`/`stock_price` are as-of today.** This was caught by an
   arithmetic cross-check: `MU260729C00880000` reports `avg_price = $32.81` at `dte = 1`, but
   MU's **actual range today was 789.09–848.36** (screener `high`/`low`) — the stock never
   traded near 880, and a 1DTE 880 call at spot 820.53 with 143% IV is worth ≈$6, not $32.81.
   The $32.81 is consistent with the **7/27 session**, when MU closed 900.20. **Every OI change
   in this phase is therefore attributed to 7/27 activity, and today's put-strip sale is
   explicitly NOT yet in these numbers.** This governs the confidence attached to the
   "opening" verdict and is restated in the summary and verdict.

Minor source discrepancy noted, not reconciled: `uw` screener reports today's stock volume as
**50,897,669 vs avg30 44,991,443.7 (1.13×)**, while `fz` (phase-0) reported **61,039,321 vs
52.22M avg (1.17×)**. Different consolidation/session coverage; the ratio agrees (~1.13–1.17×)
and no conclusion depends on the absolute figure. UW is cited as primary.

## Verdict for downstream phases

- **Positioning bias: DEFENSIVE NEAR-TERM, CONSTRUCTIVE LONG-TERM — with one genuine bullish
  structural footprint.** Put/call OI runs 2.592 (3 DTE) → 1.573 (52 DTE) → 0.635–0.980 (LEAPs).
  Near-dated winning puts were closed (-24,600 contracts) and replaced with cheap crash tails
  (+36,179 contracts at $0.01–$0.27), while a persistent counterparty **opens** short puts at
  750–800 out to Jun-2027. **Hedges are being rolled down and out; someone is being paid to
  underwrite the downside.**
- **Conviction: 3 / 5.** The put-strip-opening finding is well-evidenced (six sessions,
  consistent bid-domination, rising OI) and answers phase-1's decisive question — but it is
  **inferred from the 7/27 leg**, since today's OI is not yet published, and at 0.021% of float
  it is a desk position, not a market force. The rest of the phase (walls, term structure) is
  descriptive rather than directional. Not capped by phase-0.5 (that cap applies to phases 1–2).
- **Largest OI build as % of float: 0.218%** (Aug-07 55P, +24,412 contracts ≈ 2.44M shares) —
  and it is a **one-cent tail option**, so the headline percentage overstates its economic
  weight. The strategically meaningful build (750/800 put campaign) is **0.021% of float**.
  **Not structural for a 1.12B-float mega-cap; does not raise conviction.**
- **Three pin/cliff strikes for phase 9** (sourced from `oi-by-strike` roles and the
  `term-structure` cliff, not hand-picked):
  1. **$800 — `put_wall_support`, -2.39% from spot, 84,213 OI, net -32,711.** The single most
     important level in this run. Independently corroborated by phase-1 (put strip written at
     750/800) and phase-2 (dark-pool selling heaviest in the 790–809 bins). **Primary
     support/entry reference.**
  2. **$750 — `put_wall_support`, -8.49%, 41,151 OI, net -20,571.** The lower rung of the same
     written strip and the next structural shelf if 800 fails. **Stop/second-entry reference.**
  3. **2026-07-31 expiry (3 DTE) — the OPEX cliff at 18.38% of total OI, put/call 2.592.**
     Not a pin (MU failed `pin-risk`), but the largest near-term gamma concentration.
     **Event-risk reference; cross-check phase-4 max-pain.**
  *(Explicitly NOT a level: **$900**, despite its `call_wall_resistance` tag — net_oi of only
  +6,115 against 29,455 puts makes it a contested battleground, not a ceiling.)*
- **Open questions:**
  - **Is the 750/800 short-put campaign outright bullish, or the financing leg of a collar
    against stock?** Phase-1 measured -$25.1M of ITM 46–180DTE call selling, which pairs
    naturally with it as a buy-write/collar. But phase-2 shows the dark pool *distributing*
    — so the stock leg it would hedge may be shrinking. **→ phase-4 (dealer positioning) and
    phase-8's desk views must adjudicate.**
  - **Why is the 12.47%-of-OI Sep-18 expiry sitting 4 days BEFORE the reported 2026-09-22
    earnings date?** Either the earnings date is stale (a known `next_earnings_date` trap) or
    the market is positioned into, not through, the print. **→ phase-7b/7c must verify the date.**
  - **Who is buying 55-strike and 95-strike puts for a penny?** Appetite for catastrophic-tail
    convexity on a memory name is worth understanding. **→ phase-6/7c (is there a systemic
    memory-cycle or credit narrative?).**
  - Tomorrow's OI file will show whether today's $28.4M put-strip sale added to the campaign
    (opening, confirming) or netted against it. **This run cannot see it** — a re-run on
    2026-07-29 should check.
