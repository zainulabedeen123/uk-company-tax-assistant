# Corporation Tax (HMRC)

Legislation: Corporation Tax Act 2009 (CTA 2009), Corporation Tax Act 2010 (CTA 2010), Capital Allowances Act 2001 (CAA 2001), Finance Act 1998 Sch 18 (returns, penalties, enquiries), TMA 1970. Manuals: Company Taxation Manual (CTM), Capital Allowances Manual (CA), Corporate Intangibles R&D Manual (CIRD). Figures: `rates-2026-27.md`.

## 1. Who pays and registration

- UK-resident companies pay Corporation Tax on worldwide profits (subject to the branch exemption election); non-resident companies on UK permanent establishment profits and UK property income.
- After incorporation HMRC sends the **Unique Taxpayer Reference (UTR)** (10 digits) to the registered office, usually within ~14 days.
- **Register for Corporation Tax within 3 months of starting to do business** (trading, buying/selling, advertising, renting property, employing). Failure to notify chargeability within 12 months of the period end: penalty under FA 2008 Sch 41.
- Dormant from incorporation: tell HMRC; no return unless a notice to file is issued.

## 2. Accounting periods for Corporation Tax

- A CT accounting period can never exceed **12 months** (CTA 2009 s10).
- It starts when the company comes within the charge (starts trading/acquires a source of income) and ends at the earliest of: 12 months after start; the end of the company's period of account; starting/ceasing to trade; becoming/ceasing to be UK resident; entering administration/winding up.
- If statutory accounts cover more than 12 months (e.g. first period of 13 months), there are **two CT periods**: the first 12 months and the remainder → **two CT600s**, two payment dates, two filing dates (both returns' filing deadline is 12 months after the end of the *period of account*, capped at 30 months from its start). Trading profits are time-apportioned; capital allowances computed per CT period; chargeable gains and some items allocated to the period in which they arise.
- Pre-trading company with no income: may have no CT accounting period yet.

## 3. Payment and filing deadlines

| Obligation | Deadline |
|---|---|
| Pay Corporation Tax (augmented profits ≤ £1.5m) | 9 months and 1 day after the end of the CT accounting period |
| Large companies (> £1.5m) | Quarterly instalments: months 7, 10, 13, 16 from start of a 12-month period (not required in first year of being large if profits ≤ £10m and not large in previous 12 months) |
| Very large (> £20m) | Months 3, 6, 9, 12 |
| File CT600 (with accounts + computations, iXBRL) | 12 months after the end of the period of account |
| Amend a return | Within 12 months after the filing deadline |
| HMRC enquiry window | 12 months from the date the return was delivered (if on time) for single companies/small groups; otherwise to the quarter day after 12 months from delivery |
| Overpayment relief claim | 4 years from end of the accounting period |
| Keep records | 6 years from end of the accounting period (longer if enquiry open) |

Pay using the 17-character payment reference (UTR + accounting period code + "A001…"). HMRC charges late payment interest from the day after the due date.

## 4. How to file the CT600 (from 1 April 2026)

- HMRC's free "File your accounts and Company Tax Return" service (CATO) **closed 31 March 2026**. CT600s must be filed using **HMRC-recognised commercial software** (or by an agent). Many low-cost options exist; HMRC lists recognised software on GOV.UK ("Find software for filing Company Tax Returns").
- Return pack: CT600 form + statutory accounts in iXBRL + tax computation in iXBRL. Dormant/very small companies still need iXBRL accounts.
- Supplementary pages (attach when relevant):
  - CT600A — loans to participators (s455) and relief for repayment
  - CT600B — controlled foreign companies
  - CT600C — group and consortium relief
  - CT600D — insurance
  - CT600E — charities and CASCs
  - CT600F — tonnage tax
  - CT600G — Northern Ireland trading
  - CT600H — cross-border royalties
  - CT600I — supplementary charge (ring fence trades)
  - CT600J — disclosure of tax avoidance schemes
  - CT600K — restitution tax
  - CT600L — research and development
  - CT600M — freeports and investment zones
  - CT600N — residential property developer tax
  - CT600P — Pillar 2 / Multinational top-up tax (large groups)
- The return includes a declaration by an authorised person; the company is responsible even if an agent files.

## 5. Computing taxable total profits (TTP)

Start with profit before tax per accounts, then:

**Add back (disallowable):**
- Depreciation, amortisation of non-qualifying assets, loss on disposal of fixed assets (replaced by capital allowances / chargeable gains).
- Client/customer entertaining and gifts (except gifts ≤ £50 per person per year carrying a conspicuous advert, not food/drink/tobacco/vouchers). Staff entertaining is allowable.
- Fines and penalties, late-filing penalties, HMRC penalties (late payment *interest* is deductible).
- Expenditure not wholly and exclusively for the trade (CTA 2009 s54); capital expenditure (s53).
- Political donations; most legal costs of capital nature; general provisions (specific provisions allowable).
- Remuneration not paid within 9 months of the period end (deduct in the period paid — s1288).
- Employer pension contributions are deductible only when paid (no accrual).
- Charitable donations are not trading deductions — deduct as qualifying charitable donations (QCDs) from total profits.
- Car leasing: 15% disallowance for cars with CO2 > 50g/km.

**Deduct:**
- Capital allowances (section 6).
- Income not taxable as trading income (e.g. dividends received — generally exempt for companies under CTA 2009 Part 9A; bank interest is taxed as non-trading loan relationship income instead).
- R&D enhanced deduction (ERIS) where applicable.

**Then:**
TTP = trading profits + non-trading loan relationship credits (interest) + property income + chargeable gains (with indexation frozen at Dec 2017) + other income − losses relieved − qualifying charitable donations − group relief.

## 6. Rates and marginal relief

1. Count **associated companies**: companies under common control (50% test, CTA 2010 s25), at any time in the accounting period. Ignore dormant companies and passive holding companies. Since April 2023 attribution of rights from relatives/associates applies only where there is substantial commercial interdependence.
2. Divide the £50,000 and £250,000 limits by (1 + associated companies); pro-rate for a short period (days/365).
3. **Augmented profits** = TTP + exempt distributions received from non-group companies (franked investment income).
4. If augmented profits ≤ lower limit → 19% on TTP. If ≥ upper limit → 25% on TTP.
5. Between the limits → 25% on TTP minus marginal relief:
   **MR = 3/200 × (U − A) × N / A**, where U = upper limit, A = augmented profits, N = TTP.
6. Periods straddling 1 April use each financial year's rates for the time-apportioned profits (rates unchanged FY2023–FY2026, so straddles only matter if future rates change).

Worked example: 12-month period, no associates, TTP = augmented = £100,000. Tax at 25% = £25,000. MR = 3/200 × (250,000 − 100,000) × 100,000/100,000 = £2,250. CT = £22,750 (effective 22.75%). Use `corporation-tax-calculator`.

## 7. Capital allowances (CAA 2001)

- **Plant and machinery** — equipment, computers, vans, furniture, integral features (special rate), long-life assets (special rate), cars (special rules).
- Priority order for a typical small company: AIA (£1m) first; full expensing (100%, new and unused, main-rate assets, companies only); 50% FYA for special-rate new assets; new 40% FYA (from 1 Jan 2026) for main-rate assets not otherwise covered (e.g. second-hand excluded — check; leased assets included); balance into pools.
- Writing-down allowances: main pool 14% (from 1 April 2026; hybrid for straddling periods), special rate pool 6%. Short periods: WDA pro-rated (AIA limit pro-rated too).
- Cars never qualify for AIA or full expensing. New zero-emission cars: 100% FYA (check expiry). Others: main pool (≤50g/km) or special rate pool (>50g/km).
- Disposals: under full expensing a disposal creates a balancing charge equal to the proceeds (50% for 50% FYA assets). Under AIA/pool, proceeds deducted from the pool (capped at cost).
- **Structures and Buildings Allowance** (SBA): 3% a year straight-line on construction/renovation costs of non-residential structures (not land).
- **Intangible fixed assets** (CTA 2009 Part 8): amortisation per accounts generally deductible, or elect 4% fixed rate. Goodwill: relief at 6.5% where acquired with qualifying IP (post-April 2019 rules).

## 8. Losses

- **Trading losses (CTA 2010 s37 / s45A)**: set against total profits of the same period; carry back 12 months against total profits (36 months on cessation — terminal loss relief); carry forward against total profits (losses arising from 1 April 2017), subject to the £5m deductions allowance per group/company. Pre-April 2017 losses carry forward only against profits of the same trade.
- Claims for current-year / carry-back relief: within 2 years of the end of the loss-making period.
- Group relief (CTA 2010 Part 5): 75% group; consortium relief.
- Non-trading loan relationship deficits, property losses, capital losses (capital losses only against chargeable gains, carried forward indefinitely).
- Loss buying restrictions on change of ownership (CTA 2010 Part 14) — escalate.

## 9. Research and development

- Merged R&D Expenditure Credit scheme for periods beginning on/after 1 April 2024 (20% taxable credit). ERIS for loss-making R&D-intensive SMEs (≥30% intensity): 86% extra deduction + 14.5% payable credit.
- Qualifying costs: staff costs, EPWs, software, data and cloud computing, consumables, clinical trial volunteers, subcontracted R&D (restrictions on overseas costs since April 2024).
- Pre-notification within 6 months of period end if first claim or no claim in previous 3 years; Additional Information Form (AIF) before the CT600; CT600L page. Claims must be made within 2 years of period end.
- Must meet the DSIT guidelines definition (seeking an advance in science or technology through resolution of scientific/technological uncertainty). Compliance risk is high — escalate for significant claims.

## 10. Close companies

Most owner-managed companies are close (controlled by 5 or fewer participators or by directors). Consequences: s455 on loans to participators (see director-pay-dividends.md); benefits to non-employee participators treated as distributions; close investment-holding companies always pay the main rate.

## 11. Penalties and compliance

- Late filing: fixed and tax-geared (see rates file). Reasonable excuse appeals: file the return first; appeal within 30 days of the penalty notice.
- Inaccuracy penalties (FA 2007 Sch 24): careless 0–30%, deliberate 20–70%, deliberate and concealed 30–100% of potential lost revenue; reduced for disclosure (unprompted vs prompted).
- Failure to notify: Sch 41, similar percentages.
- Senior Accounting Officer rules for companies with turnover > £200m or balance sheet > £2bn.
- HMRC compliance checks: respond by deadlines, keep records; escalate.

## 12. Other company-level taxes to flag

- Stamp duty on share transfers: 0.5% (rounded up to £5) where consideration > £1,000.
- SDLT/LBTT/LTT on property purchases; ATED for residential property > £500,000 held by companies.
- Business rates (local authority), Construction Industry Scheme (CIS) for construction contractors/subcontractors, Plastic Packaging Tax, Digital Services Tax, Pillar 2 (groups ≥ €750m).
