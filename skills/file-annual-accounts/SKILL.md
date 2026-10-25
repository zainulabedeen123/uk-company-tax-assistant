---
name: file-annual-accounts
description: Guides a director step by step through preparing, approving and filing a UK private company's annual accounts at Companies House — choosing micro-entity, small, filleted or dormant accounts, the mandatory balance-sheet statements, the filing method and deadline. Use when the user says "file my accounts", "prepare my company accounts", "dormant accounts", "micro-entity accounts", "my accounts are late", or "can I get an extension".
---

# File annual accounts with Companies House

Reference: `${CLAUDE_PLUGIN_ROOT}/skills/uk-company-tax-expert/references/companies-house.md` §2.

## 1. Establish the basics
- Company number, period end date, deadline (run `filing-deadlines` or read it from the register), whether already late.
- Activity in the period: dormant (no significant accounting transactions)? trading?
- Size test (2 of 3, see `rates-2026-27.md`): turnover, balance sheet total (gross assets), average employees.
- Any members holding ≥10% asking for an audit? Any reason audit exemption is excluded?

## 2. Choose the accounts type
| Situation | Accounts | Standard |
|---|---|---|
| No significant transactions | Dormant accounts | — |
| Micro-entity | Micro-entity accounts (balance sheet + limited notes; P&L prepared but need not be filed) | FRS 105 |
| Small | Small company accounts; may file filleted (balance sheet + notes) | FRS 102 Section 1A |
| Medium/large | Full accounts + strategic report + audit | FRS 102 / IFRS |

Explain that the **full** accounts (including P&L) must still be prepared, approved, sent to members (s423) and used for the CT600 — filleting only affects the public copy. From April 2028 small and micro companies must file a P&L (with an opt-out from publication) and must file via software.

## 3. Prepare the accounts
Walk the user through (for micro/small):
1. Close the books: bank reconciliation, sales/purchase ledgers, accruals and prepayments, depreciation, stock, director's loan account balance, Corporation Tax provision for the year (use `corporation-tax-calculator`), dividends paid.
2. Profit and loss account: turnover, cost of sales, other income, staff costs, depreciation, other charges, tax, profit for the year.
3. Balance sheet: fixed assets; current assets (stock, debtors, cash); creditors due within one year (including CT and VAT owed, director's loan if credit); net current assets; creditors after more than one year; provisions; net assets; capital and reserves (called-up share capital, profit and loss reserve).
4. Notes (micro minimum): advances/credits to directors and guarantees (s413), financial commitments and contingencies, average number of employees. Small (FRS 102 1A): accounting policies, average employees, fixed assets, debtors/creditors analysis, related parties where material, going concern, etc.
5. Mandatory statements above the director's signature on the balance sheet:
   - "For the year ending [date] the company was entitled to exemption from audit under section 477 of the Companies Act 2006 relating to small companies." (dormant: section 480)
   - "The members have not required the company to obtain an audit in accordance with section 476."
   - "The directors acknowledge their responsibilities for complying with the requirements of the Act with respect to accounting records and the preparation of accounts."
   - "These accounts have been prepared in accordance with the provisions applicable to companies subject to the small companies regime." (micro: "…in accordance with the micro-entity provisions.")
   - If filleted: "The company has elected not to file the profit and loss account / directors' report" statement (s444(5A)).
6. Board approval: date of approval, printed name and signature of a director on the balance sheet.

Offer to draft the accounts as a document/spreadsheet from the user's figures. State clearly that the user must check figures against their records; an accountant review is wise for a first set.

## 4. File
- **Method today**: Companies House online service ("File your accounts" / WebFiling — needs the company authentication code, or GOV.UK One Login access) for micro, small (filleted), dormant accounts; or commercial software (iXBRL). Note: HMRC's joint accounts-and-CT600 service closed on 31 March 2026, so the CT600 is filed separately through commercial software (`file-company-tax-return`).
- Online accounts filing is free. Usually accepted within 24–48 hours; check the email confirmation and the filing history.
- If rejected, read the rejection reason (common: wrong period dates, missing statements, unsigned/undated, figures not matching) and refile before the deadline.

## 5. Late or about to be late
- Apply for an extension **before** the deadline only with a genuine reason outside the company's control.
- If already late: file immediately (penalty increases with time — see rates file); explain appeal limits honestly.
- Persistent non-filing → strike-off and prosecution risk.

## 6. After filing
Remind: CT600 deadline (12 months after period end) and CT payment (9 months + 1 day), share accounts with members, keep records 6 years.
