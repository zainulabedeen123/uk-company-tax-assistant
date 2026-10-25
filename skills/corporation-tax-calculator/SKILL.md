---
name: corporation-tax-calculator
description: Computes a UK company's Corporation Tax liability from its accounts — adjusting profit for disallowables, capital allowances, losses and charitable donations, then applying the 19%/25% rates with marginal relief, associated companies and short periods. Use when the user asks "how much corporation tax do I owe", "calculate my CT", "marginal relief", "what is my tax bill", or shares a profit figure or P&L.
---

# Corporation Tax calculator

## Step 1 — Gather facts
- CT accounting period dates (max 12 months; split longer periods first using `filing-deadlines`).
- Profit before tax from the accounts (or the P&L / trial balance).
- Number of associated companies (companies under common control at any time in the period; ignore dormant and passive holding companies).
- Dividends received from other companies (exempt distributions → augmented profits).
- Fixed asset additions/disposals in the period, depreciation charged, brought-forward losses, any capital allowance pool balances b/f.

## Step 2 — Build the tax computation
Use `${CLAUDE_PLUGIN_ROOT}/skills/uk-company-tax-expert/references/corporation-tax.md` §5–§8. Lay it out as:

```
Profit before tax (per accounts)                    X
Add: depreciation / amortisation (non-qualifying)   X
Add: client entertaining                            X
Add: fines and penalties                            X
Add: other disallowables (explain each)             X
Less: non-trading income included above            (X)
Less: capital allowances (show AIA / FE / FYA / WDA)(X)
= Trading profit                                    X
Add: non-trading loan relationship credits          X
Add: property income / chargeable gains             X
Less: losses brought forward / current-year relief (X)
Less: qualifying charitable donations              (X)
= Taxable total profits (TTP)                       X
```

Ask about any line that is unclear rather than guessing. Explain each adjustment in one line.

## Step 3 — Compute the tax
```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/corporation-tax-calculator/scripts/ct_calc.py --profits <TTP> [--fii <exempt dividends>] [--associates <n>] [--start YYYY-MM-DD --end YYYY-MM-DD]
```
The script slices periods across financial years, pro-rates the limits, divides them by (1 + associates) and applies marginal relief. If it reports that a financial year's rates are not loaded, confirm the rates (run `check-tax-updates`) and add them to the `FY` table at the top of the script.

## Step 4 — Report
- Tax payable, effective rate, marginal rate band, payment deadline (9 months + 1 day) and the CT600 filing deadline.
- Quarterly instalments warning if augmented profits exceed £1.5m (divided by 1 + associates).
- s455 if the director's loan account is overdrawn at the year end and not repaid within 9 months + 1 day (add to the bill; CT600A).
- Planning points to raise, not to push: timing of capital purchases (AIA/full expensing), employer pension contributions (deductible when paid), R&D eligibility, use of losses. Flag professional advice for anything complex.
- Cite GOV.UK "Corporation Tax rates and allowances" and "Marginal Relief for Corporation Tax".
