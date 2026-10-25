---
name: file-company-tax-return
description: Guides a director through registering for Corporation Tax and preparing, filing and paying the Company Tax Return (CT600) with HMRC — computations, iXBRL accounts, supplementary pages such as CT600A for director's loans, recognised software after the HMRC free service closed, payment references, amendments, dormant companies and late-filing penalties. Use when the user says "file my CT600", "file my company tax return", "register for corporation tax", "pay corporation tax", "HMRC penalty", or "my company is dormant for tax".
---

# Company Tax Return (CT600)

Reference: `${CLAUDE_PLUGIN_ROOT}/skills/uk-company-tax-expert/references/corporation-tax.md`; figures in `rates-2026-27.md`.

## 0. Registration (if not yet done)
- Must register within 3 months of starting to do business. Needs the company UTR (posted to the registered office after incorporation), company number, date trading started, SIC/activity, accounting period end.
- Register via the HMRC business tax account (Government Gateway user ID — the user signs in themselves; never ask for credentials).
- Dormant: tell HMRC the company is dormant instead; no CT600 unless HMRC sends a notice to file.

## 1. Check the periods
Use `filing-deadlines`. If the accounts cover more than 12 months, prepare **two** returns (first 12 months + remainder). Confirm any "notice to deliver" HMRC issued.

## 2. Prepare the figures
1. Final statutory accounts (approved). 
2. Tax computation (`corporation-tax-calculator`): adjustments, capital allowances, losses, marginal relief.
3. Supplementary pages needed? Most common for small companies:
   - **CT600A** if the director's loan account was overdrawn at the period end (loans to participators) — report loans, repayments within 9 months, s455 due, and relief claims.
   - **CT600L** for R&D (plus the Additional Information Form submitted beforehand and pre-notification where required).
   - CT600C for group relief; CT600E for charities; CT600J if a disclosed avoidance scheme.
4. Associated companies count and the "small company" questions on the return.

## 3. Choose filing software (HMRC free service closed 31 March 2026)
- Use HMRC-recognised commercial software (GOV.UK: "Find software for filing Company Tax Returns"). Many low-cost packages produce the CT600, iXBRL-tagged accounts and computations together; some also file accounts with Companies House.
- Selection checklist: supports the company's accounts type (micro/small/dormant), supplementary pages needed (e.g. CT600A, CT600L), iXBRL tagging of accounts and computations, Companies House filing, price.
- An agent (accountant) can file instead; authorise them through HMRC agent services.

## 4. File the return
In the software:
1. Enter company details: name, number, UTR, period dates, return type (company/amended).
2. Enter or import accounts (iXBRL) and computation figures; check the CT600 boxes for turnover, trading profits, capital allowances, losses, TTP, associated companies, tax chargeable, marginal relief, tax payable, s455 (from CT600A).
3. Attach supplementary pages.
4. Declaration by an authorised person (director/company secretary).
5. Submit; save the HMRC submission receipt (IRmark). Check the business tax account shows the return.

## 5. Pay
- Due 9 months and 1 day after the CT period end (earlier quarterly instalments for large companies).
- Use the 17-character Corporation Tax payment reference for the specific period (shown in the business tax account / payslip). Methods: Faster Payments/CHAPS/Bacs to HMRC's bank details on GOV.UK "Pay Corporation Tax", Direct Debit (set up in advance), online by debit or corporate credit card (personal credit cards not accepted), bank online.
- If paying late: interest at Bank Rate + 4% runs from the due date. If unable to pay, contact HMRC for a Time to Pay arrangement before the deadline.

## 6. After filing
- Amend within 12 months of the filing deadline if an error is found (file an amended CT600).
- Enquiry window generally 12 months from filing.
- Keep records 6 years.
- Penalties if late: £200 / further £200 at 3 months (third successive late return: £1,000 each); 10% of unpaid tax at 6 and 12 months. Appeal only with reasonable excuse after filing the return.
