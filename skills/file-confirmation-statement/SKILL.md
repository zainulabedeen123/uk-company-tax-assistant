---
name: file-confirmation-statement
description: Walks a director through filing the Companies House confirmation statement (CS01), including director identity verification personal codes, PSC verification, SIC codes, shareholders, statement of capital, registered email and lawful purpose statement, plus event filings for director, PSC, share and address changes. Use when the user says "file my confirmation statement", "annual return", "verify my identity for Companies House", "add/remove a director", "change registered office", "issue new shares", or "update PSC".
---

# Confirmation statement and company changes

Reference: `${CLAUDE_PLUGIN_ROOT}/skills/uk-company-tax-expert/references/companies-house.md` §3–§5; fees in `rates-2026-27.md`.

## 1. Before starting
- Confirm the confirmation date and deadline (14 days after the review period ends) on the Companies House register.
- **Identity verification**: every director needs a Companies House personal code (verify via GOV.UK One Login, or through an authorised agent/ACSP). Confirmation statements filed on or after 18 November 2025 require codes for all directors, and the 12-month transition for existing directors ends 18 November 2026. PSCs verify separately in their own 14-day window. Guide the user through verification first if needed:
  1. Go to GOV.UK "Verify your identity for Companies House".
  2. Sign in/create a GOV.UK One Login.
  3. Verify with photo ID (e.g. passport, photocard driving licence) via the GOV.UK ID Check app or the online route; if unable to verify digitally, use an authorised agent (ACSP).
  4. Receive the personal code; keep it safe and give it to whoever files.
- Have ready: company authentication code (or One Login access to the company), registered email address, current shareholders and shareholdings, SIC codes, £50 fee (card / PayPal).

## 2. File any changes first (event-driven filings)
Changes in the period must be filed on their own forms (they cannot all be made in the CS01): new/removed directors (AP01/TM01), director detail changes (CH01), registered office (AD01), PSC changes (PSC01–PSC09), new share allotments (SH01 — within one month). New directors must give their personal code on AP01.

## 3. Complete the confirmation statement (online)
1. Sign in to the Companies House service and choose "File a confirmation statement".
2. Check each section: registered office; registered email address (provide if missing); SIC codes (up to 4; update if business changed); statement of capital (only changes via SH01 etc.); shareholders (update names/holdings for transfers in the period); PSCs; officers; register locations.
3. Provide each director's personal code / confirm verification.
4. Confirm the **lawful purpose statement**.
5. Pay £50 (first statement in the 12-month payment period; further statements in the same period are free).
6. Submit; keep the confirmation email; check the filing history.

## 4. Afterwards
- Diary the next confirmation date (12 months on).
- Remind PSCs of their verification window if not done.
- Update the company's own statutory registers (members, directors, PSC) if kept.

## Penalties to explain
No automatic fine, but failing to file is a criminal offence for the company and each officer and leads to strike-off action. Acting as an unverified director is an offence.
