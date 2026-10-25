---
name: filing-deadlines
description: Calculates every statutory deadline for a UK limited company — Companies House accounts and confirmation statements, Corporation Tax registration, payment and CT600 filing, s455 repayment, R&D notification, VAT, PAYE and director Self Assessment. Use when the user asks "when are my accounts due", "what are my deadlines", "when do I pay corporation tax", "build my compliance calendar", or gives an incorporation date or year end.
---

# Filing deadlines

1. Collect: company name/number (optional), incorporation date, current accounting reference date (and whether it was changed with AA01), date trading started, date of last confirmation statement if filed early, VAT stagger (if registered), whether running payroll.
   - If the user gives a company number, suggest they check the dates shown on the Companies House register (find-and-update.company-information.service.gov.uk) — it shows "next accounts due" and "next statement due" — and use those as the source of truth.
2. Run:
   ```bash
   python3 ${CLAUDE_PLUGIN_ROOT}/skills/filing-deadlines/scripts/deadlines.py --incorporated YYYY-MM-DD [--ard YYYY-MM-DD] [--trading-start YYYY-MM-DD] [--last-cs YYYY-MM-DD] [--years 3]
   ```
   Add `--json` for structured output.
3. Present a single chronological table: date, regulator (Companies House / HMRC), obligation, and consequence if missed (use penalty figures from `${CLAUDE_PLUGIN_ROOT}/skills/uk-company-tax-expert/references/rates-2026-27.md`).
4. Add recurring items the script does not compute:
   - VAT: return + payment 1 month and 7 days after each VAT quarter end.
   - PAYE: FPS on/before each payday; pay HMRC by the 22nd; EPS by the 19th; P60 by 31 May; P11D/P11D(b) by 6 July; Class 1A by 22 July.
   - Directors' Self Assessment: 31 January and 31 July.
   - Identity verification: each director's personal code with the next confirmation statement; PSC verification windows (see `companies-house.md` §4).
5. Highlight the first period trap: a first period of more than 12 months produces **two** CT accounting periods and two CT600s, with two payment dates.
6. Note that Companies House deadlines do not move for weekends or bank holidays; pay HMRC early enough for the money to clear.
7. Offer to turn the list into a calendar file (.ics) the user can import — generate it with Python if asked.

Rules reference: `${CLAUDE_PLUGIN_ROOT}/skills/uk-company-tax-expert/references/deadlines-calendar.md`.
