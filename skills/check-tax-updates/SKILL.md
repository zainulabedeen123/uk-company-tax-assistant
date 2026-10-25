---
name: check-tax-updates
description: Checks GOV.UK, HMRC and Companies House for changes to UK company tax rates, thresholds, fees, deadlines and filing rules since this plugin's figures were verified (25 October 2026), including Budget announcements. Use when the user asks "has anything changed", "latest rates", "what did the Budget change", "is this still current", when a question concerns a tax year after 2026/27, or before relying on any figure marked [verify].
---

# Check for tax and filing rule updates

The plugin's figures were verified on **25 October 2026** (`${CLAUDE_PLUGIN_ROOT}/skills/uk-company-tax-expert/references/rates-2026-27.md`). The **Autumn Budget was scheduled for 28 October 2026**; anything announced there applies mostly from April 2027.

## Steps
1. Identify what the user needs (a specific rate, a deadline rule, or a general update).
2. Search the web, restricted to authoritative domains where possible: `gov.uk`, `legislation.gov.uk`, `companieshouse.blog.gov.uk`, `changestoukcompanylaw.campaign.gov.uk`, `bankofengland.co.uk` (Bank Rate → HMRC interest). Useful queries:
   - "Budget 2026 overview of tax legislation and rates annex A"
   - "Corporation Tax rates and allowances" (HMRC publication)
   - "Rates and thresholds for employers 2027 to 2028"
   - "Companies House fees" / "Companies House changes accounts filing"
   - "HMRC interest rates for late and early payments"
   - "VAT registration threshold"
3. Fetch the primary page and read the relevant table. Prefer GOV.UK over commentary; if only secondary sources exist, say so.
4. Report: what changed, effective date, old vs new value, source link, and whether it is enacted (Finance Act) or only announced.
5. If the update affects a calculator, tell the user which value in which script needs updating (`ct_calc.py` FY table; `salary_dividend.py` constants) and offer to produce an updated plugin version. Do not silently assume unconfirmed rates.
6. Distinguish devolved differences (Scottish income tax set by the Scottish Budget, usually December–February).
