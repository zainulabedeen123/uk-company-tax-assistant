# Building a compliance calendar for a UK private limited company

Run `${CLAUDE_PLUGIN_ROOT}/skills/filing-deadlines/scripts/deadlines.py` for exact dates. Rules it implements:

## Companies House
| Item | Rule |
|---|---|
| First ARD | Last day of the month of the first anniversary of incorporation |
| First accounts | If first period > 12 months: 21 months after incorporation (or 3 months after ARD if later). Otherwise 9 months after ARD |
| Subsequent accounts | 9 months after ARD (last day of month if ARD is a month end) |
| Confirmation statement | Review period ends on the anniversary of incorporation (or of last confirmation date); file within 14 days after |
| Identity verification (existing directors) | With first confirmation statement on/after 18 Nov 2025; transition ends 18 Nov 2026 |
| Event filings | 14 days (officers, PSCs), 1 month (SH01), 15 days (resolutions), 21 days (charges) |

## HMRC — Corporation Tax
| Item | Rule |
|---|---|
| Register for CT | Within 3 months of starting business activity |
| CT accounting periods | Max 12 months — a 13+ month first period splits into two |
| Pay CT | 9 months + 1 day after each CT period end |
| File CT600 | 12 months after period-of-account end |
| s455 repayment window | 9 months + 1 day after period end |
| R&D claim notification | 6 months after period end (first-time claimants) |

## HMRC — VAT (if registered)
Return and payment: 1 month + 7 days after each VAT quarter end.

## HMRC — PAYE (if employer)
FPS on/before each payday; pay by 22nd of following tax month; EPS by 19th; P60 by 31 May; P11D/P11D(b) by 6 July; Class 1A by 22 July.

## Directors — Self Assessment
5 Oct (register), 31 Oct (paper), 31 Jan (online return + balancing payment + 1st POA), 31 Jul (2nd POA).

## Other
Auto-enrolment declaration (5 months after duties start), re-enrolment every 3 years; ICO data protection fee annually if processing personal data (most companies); business rates; insurance (employer's liability compulsory once employing).
