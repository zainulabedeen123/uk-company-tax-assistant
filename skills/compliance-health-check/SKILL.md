---
name: compliance-health-check
description: Runs a full compliance and tax health check for a UK limited company across Companies House and HMRC — filings due or overdue, identity verification, registers, director's loan account, dividends, VAT and payroll status, records — and produces a prioritised action list. Use when the user asks "is my company compliant", "check my company", "what have I missed", "annual company checklist", or is taking over an existing company.
---

# Company compliance health check

Work through each area, asking only what is not already known. Use the Companies House register (public) for filing status: the user can share the company number, and the register page shows accounts/confirmation statement due dates, officers, PSCs and filing history. Search or fetch the register page if web tools are available.

## Checklist

### Companies House
- [ ] Accounts filed for the last period? Next due date? (`filing-deadlines`)
- [ ] Confirmation statement up to date?
- [ ] Every director verified and personal code linked (12-month transition ends 18 Nov 2026)? PSCs verified in their windows?
- [ ] Registered office is an appropriate address; registered email address provided.
- [ ] Officers, PSCs, share capital on the register match reality (any unfiled AP01/TM01/PSC/SH01)?
- [ ] Statutory registers and minutes kept; articles up to date.
- [ ] Charges registered within 21 days.

### Corporation Tax
- [ ] Registered for CT; UTR known.
- [ ] Last CT600 filed on time; CT paid on time; any penalties/interest outstanding?
- [ ] Next CT payment and filing dates.
- [ ] First-period split into two returns handled?
- [ ] Capital allowances claimed; losses tracked.

### Director's loan and dividends
- [ ] Director's loan account balance at the last year end — overdrawn? repaid within 9 months + 1 day? s455/CT600A dealt with?
- [ ] Loans over £10,000 → P11D benefit?
- [ ] Every dividend supported by distributable reserves, minutes and vouchers; paid pro rata.

### VAT
- [ ] Rolling 12-month taxable turnover vs £90,000; registered if required.
- [ ] MTD-compatible software; returns and payments on time; penalty points?

### PAYE and pensions
- [ ] Payroll registered if anyone is paid ≥ LEL; FPS on time; HMRC paid by the 22nd.
- [ ] Employment Allowance claimed if eligible (not single-director-only).
- [ ] P11Ds filed by 6 July; Class 1A paid by 22 July.
- [ ] Auto-enrolment duties met or exemption confirmed.

### Directors personally
- [ ] Self Assessment registered and filed by 31 January; payments on account.

### Records and other
- [ ] Bookkeeping current; records kept 6 years.
- [ ] ICO data protection fee paid (if processing personal data); employer's liability insurance (if employees).

## Output
Produce a table: area | status (OK / action needed / overdue / unknown) | what to do | deadline | consequence. Order by urgency (overdue first, then by deadline). Offer to start the most urgent workflow skill. Note items needing professional advice.
