---
name: vat-and-payroll
description: Step-by-step help with a UK company's VAT and PAYE obligations — whether and when to register for VAT, choosing VAT schemes (Flat Rate, cash, annual), Making Tax Digital returns, VAT penalties, setting up payroll, running RTI submissions, director NIC, Employment Allowance, P11D benefits and workplace pensions. Use when the user asks "do I need to register for VAT", "file my VAT return", "flat rate scheme", "set up payroll for my company", "pay myself through PAYE", "P11D", or "Employment Allowance".
---

# VAT and payroll

References: `${CLAUDE_PLUGIN_ROOT}/skills/uk-company-tax-expert/references/vat.md`, `paye-payroll.md`, `rates-2026-27.md`.

## VAT

### Do I need to register?
1. Ask for taxable turnover month by month for the last 12 months and the expected next 30 days. Exclude exempt and outside-scope income (e.g. most supplies of services to overseas business customers).
2. Test the rolling 12-month figure each month-end against £90,000 and the forward-looking 30-day test. Give the exact registration deadline and effective date.
3. If below the threshold, explain voluntary registration pros/cons (B2B customers can reclaim; B2C prices rise).

### Registering
HMRC online VAT registration via the business tax account; choose schemes at the same time if wanted. Keep invoices from the effective date showing VAT; reclaim pre-registration VAT (goods 4 years, services 6 months).

### Choosing a scheme
Model the Flat Rate Scheme against standard accounting with the user's figures — check the limited cost trader test (goods < 2% of turnover or < £1,000/year → 16.5%). Explain cash accounting and annual accounting eligibility.

### Filing a VAT return (MTD)
1. Use MTD-compatible software (or bridging software from a spreadsheet); authorise it with HMRC.
2. Reconcile sales and purchases for the quarter; check invoices are valid; exclude blocked input VAT (entertaining, private use, cars).
3. Complete boxes 1–9 (see `vat.md` §4); check reverse-charge and postponed import VAT entries.
4. Submit and pay by 1 month + 7 days after the period end.
5. Errors under the threshold go on the next return; larger ones on VAT652.

## Payroll (PAYE)

### Set up
1. Register as an employer (before the first payday; up to 2 months early).
2. Choose HMRC-recognised payroll software (free options exist for small employers).
3. Collect employee details (starter checklist / P45), set the director's NIC calculation method (annual or alternative arrangements).

### Each pay period
Run payroll → send FPS on or before payday → pay employees → pay HMRC by the 22nd of the next tax month (quarterly if average monthly liability < £1,500) → send EPS by the 19th when needed (Employment Allowance claim, no payment periods).

### Year end and benefits
P60s by 31 May; P11D/P11D(b) by 6 July (unless payrolling benefits); Class 1A by 22 July.

### Employment Allowance
Claim via EPS if eligible (£10,500 in 2026/27). Explain the single-director exclusion clearly.

### Workplace pension
Assess staff; enrol eligible jobholders; declaration of compliance to The Pensions Regulator within 5 months. Director-only companies: confirm exemption with TPR.
