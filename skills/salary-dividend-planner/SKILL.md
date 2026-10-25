---
name: salary-dividend-planner
description: Works out the most tax-efficient mix of director salary and dividends for a UK owner-managed company for 2026/27, including employer and employee NIC, Employment Allowance, Corporation Tax, dividend tax and the Personal Allowance taper, and produces dividend paperwork. Use when the user asks "how should I pay myself", "salary vs dividends", "optimal director salary", "how much dividend can I take", or needs a dividend voucher or board minute.
---

# Salary and dividend planner

## Step 1 — Facts that change the answer
Ask for (skip what's already known): expected company profit before director pay; number of directors/employees on payroll (Employment Allowance eligibility — a company whose only employee paid above £5,000 is a director cannot claim); director's other income; Scottish taxpayer?; shareholders and percentages; distributable reserves brought forward; whether a state pension qualifying year matters; Child Benefit in household (HICBC from £60,000); pension contribution plans.

## Step 2 — Model it
```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/salary-dividend-planner/scripts/salary_dividend.py --profit <amount> [--ea] [--other-income <amount>] [--scottish] [--associates <n>] [--salaries 0,5000,6708,12570] [--dividend all|<amount>]
```
The script assumes one 100% director-shareholder and a 12-month period in FY2026. For multiple shareholders, run it per person with their share of the dividend (`--dividend <amount>`) and compute company-level CT once.

## Step 3 — Explain the result
- Show the comparison table and the recommended salary with the reasoning (CT saving on salary vs NIC cost, qualifying year).
- Flag thresholds: £50,270 (higher rate), £100,000–£125,140 (60% effective band from Personal Allowance taper), £60,000–£80,000 (HICBC). Suggest employer pension contributions as an alternative to dividends that would push income into these bands.
- Remind: dividends need distributable profits after providing for Corporation Tax; salary must go through payroll (RTI).

## Step 4 — Paperwork (if asked)
Draft in plain text or a document:
1. **Board minute — interim dividend**: company name and number, date, directors present, statement that the board reviewed management accounts dated [x] showing distributable reserves of £[x], resolution to pay an interim dividend of £[x] per [class] share on [date] to shareholders on the register at [date], signed by the chair.
2. **Dividend voucher** per shareholder: company name and number, registered office, date of payment, shareholder name and address, share class and number held, dividend per share, total amount, signed by a director.
3. For a **final dividend**: directors' recommendation + ordinary resolution of members (written resolution under CA 2006 s288 is fine).
Do not backdate documents.

References: `${CLAUDE_PLUGIN_ROOT}/skills/uk-company-tax-expert/references/director-pay-dividends.md`, `rates-2026-27.md`.
