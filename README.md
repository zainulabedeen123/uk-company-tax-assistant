# UK Company Tax Assistant

A Cowork plugin that helps founders and directors of UK private limited companies understand and meet their **Companies House** and **HMRC** obligations, from working out taxes to step-by-step filing.

> Companies House handles company-law filings (accounts, confirmation statements, officer/PSC changes, identity verification). HMRC handles tax (Corporation Tax/CT600, VAT, PAYE, Self Assessment). This plugin covers both.

## Install

- **Claude Code:** `/plugin install uk-company-tax-assistant --marketplace zainulabedeen123/uk-company-tax-assistant`
- **claude.ai / Cowork:** add it from the plugin directory once listed.

## Skills

| Skill | What it does |
|---|---|
| `uk-company-tax-expert` | Core knowledge base (rates, rules, forms, sources) used for any UK company tax/compliance question |
| `filing-deadlines` | Calculates every deadline from incorporation date / year end (script) |
| `corporation-tax-calculator` | Builds the tax computation and applies 19%/25% + marginal relief, associates, short periods (script) |
| `salary-dividend-planner` | Compares salary/dividend mixes for 2026/27 and drafts dividend minutes and vouchers (script) |
| `file-annual-accounts` | Prepare, approve and file micro/small/dormant accounts at Companies House |
| `file-confirmation-statement` | Confirmation statement, identity verification, director/PSC/share/address changes |
| `file-company-tax-return` | Register for CT, prepare and file the CT600 via recognised software, pay HMRC |
| `vat-and-payroll` | VAT registration, schemes, MTD returns; PAYE set-up, RTI, Employment Allowance, P11D, pensions |
| `compliance-health-check` | Full company check with a prioritised action list |
| `check-tax-updates` | Checks GOV.UK for changes since the figures were verified (e.g. Budget announcements) |

## Accuracy and currency

- Figures verified against GOV.UK on **25 October 2026** for tax year 2026/27 and Corporation Tax FY2026.
- The Autumn Budget was scheduled for **28 October 2026** — run `check-tax-updates` before relying on figures for 2027/28 onwards. Items marked **[verify]** in the rates file were not confirmed against a primary source.
- Calculators: Python 3 standard library only. Update the `FY` table in `ct_calc.py` and the constants in `salary_dividend.py` when rates change.

## Limits

- Information and guidance, not regulated tax or legal advice. The plugin flags situations that need an accountant (groups, audits, share schemes, exits, HMRC enquiries, IR35 disputes, large R&D claims).
- It cannot press "submit" for you: filings require your own Companies House / HMRC sign-in. It never asks for passwords or authentication codes.
- Since 1 April 2026 the CT600 must be filed through HMRC-recognised commercial software (the free HMRC service closed). From April 2028 Companies House accounts must also be filed via software.

## What the plugin runs, sends and fetches

- **Runs:** three small Python 3 scripts (standard library only) inside the plugin folder — `deadlines.py`, `ct_calc.py`, `salary_dividend.py`. They do arithmetic on the numbers you give and print results. They read no files, write no files, and make no network requests.
- **Sends:** nothing. The plugin has no MCP servers, hooks, connectors, telemetry or external endpoints, and stores no data.
- **Fetches:** when asked to check for rule changes, Claude uses its normal web search/fetch tools to read public pages on GOV.UK, legislation.gov.uk, Companies House and the Bank of England.
- **Credentials:** never requested. You sign in to Companies House and HMRC yourself.

## No setup required

No connectors or API keys are needed.

## Licence

MIT — see `LICENSE`.
