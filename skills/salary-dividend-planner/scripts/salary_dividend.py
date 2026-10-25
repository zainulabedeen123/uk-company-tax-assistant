#!/usr/bin/env python3
"""Director salary vs dividend comparison for UK tax year 2026/27.

Usage:
  python3 salary_dividend.py --profit 80000 [--ea] [--other-income 0] [--scottish]
                             [--associates 0] [--salaries 0,5000,6708,12570]
                             [--dividend all|<amount>] [--json]

--profit        Company profit for a 12-month CT period BEFORE the director's salary and
                employer NIC (and before Corporation Tax).
--ea            Company can claim Employment Allowance (NOT a single-director company
                whose director is the only employee paid above £5,000).
--other-income  Director's other non-savings income (e.g. another job, rental profit)
                taxed before this salary. NIC on other income is not modelled.
--scottish      Apply Scottish income tax bands to salary/other income (dividends use UK bands).
--dividend      'all' = distribute all post-tax profit; or a fixed gross amount.

Assumptions: one director-shareholder owning 100%, 12-month period inside FY2026,
no pension contributions, no student loan, no HICBC. Outputs are estimates.
"""
import argparse
import json

PA, BRB, ADD_T, TAPER_T = 12570, 37700, 125140, 100000
LEL, PT, UEL, ST = 6708, 12570, 50270, 5000
EMP_NIC, EE_NIC, EE_NIC_UP, EA = 0.15, 0.08, 0.02, 10500
DIV_ALLOW = 500
DIV_RATES = (0.1075, 0.3575, 0.3935)
RUK_BANDS = [(BRB, 0.20), (ADD_T - PA - BRB, 0.40), (float("inf"), 0.45)]  # above PA (full PA case)
SCOT_BANDS = [(3967, 0.19), (16956 - 3967, 0.20), (31092 - 16956, 0.21), (62430 - 31092, 0.42),
              (125140 - 62430, 0.45), (float("inf"), 0.48)]


def ct(profit, associates=0):
    if profit <= 0:
        return 0.0
    lower, upper = 50000 / (1 + associates), 250000 / (1 + associates)
    if profit <= lower:
        return profit * 0.19
    if profit >= upper:
        return profit * 0.25
    return profit * 0.25 - 3 / 200 * (upper - profit)


def personal_allowance(ani):
    return max(0.0, PA - max(0.0, ani - TAPER_T) / 2)


def income_tax(non_savings, dividends, scottish=False):
    ani = non_savings + dividends
    pa = personal_allowance(ani)
    ns_taxable = max(0.0, non_savings - pa)
    pa_left = max(0.0, pa - non_savings)
    div_taxable = max(0.0, dividends - pa_left)

    # non-savings tax
    bands = SCOT_BANDS if scottish else RUK_BANDS
    tax_ns, rem = 0.0, ns_taxable
    for width, rate in bands:
        take = min(rem, width)
        tax_ns += take * rate
        rem -= take
        if rem <= 0:
            break

    # dividends always use UK bands; basic band extended? (no Gift Aid/pension modelled)
    # When PA is tapered the additional-rate threshold is still £125,140 of total income.
    basic_limit = BRB
    higher_limit = ADD_T - pa  # taxable-income point where additional rate starts
    # Scottish taxpayers: dividend rates still follow UK bands, positioned after taxable NS income.
    pos = ns_taxable
    tax_div = 0.0
    allowance_left = DIV_ALLOW
    rem = div_taxable
    while rem > 1e-9:
        if pos < basic_limit:
            room, rate = basic_limit - pos, DIV_RATES[0]
        elif pos < higher_limit:
            room, rate = higher_limit - pos, DIV_RATES[1]
        else:
            room, rate = float("inf"), DIV_RATES[2]
        take = min(rem, room)
        free = min(take, allowance_left)
        allowance_left -= free
        tax_div += (take - free) * rate
        pos += take
        rem -= take
    return tax_ns, tax_div, pa


def employee_nic(salary):
    return max(0.0, min(salary, UEL) - PT) * EE_NIC + max(0.0, salary - UEL) * EE_NIC_UP


def scenario(profit, salary, ea, other, scottish, associates, dividend):
    er_nic_gross = max(0.0, salary - ST) * EMP_NIC
    er_nic = max(0.0, er_nic_gross - EA) if ea else er_nic_gross
    taxable = profit - salary - er_nic
    corp_tax = ct(taxable, associates)
    post_tax = taxable - corp_tax
    div = max(0.0, post_tax) if dividend == "all" else min(float(dividend), max(0.0, post_tax))
    ee = employee_nic(salary)
    t_ns, t_div, pa = income_tax(other + salary, div, scottish)
    # attribute non-savings tax to salary only (exclude tax on other income alone)
    t_other_only, _, _ = income_tax(other, 0, scottish)
    tax_on_salary = t_ns - t_other_only
    take_home = salary - ee - tax_on_salary + div - t_div
    total_tax = er_nic + corp_tax + ee + tax_on_salary + t_div
    return {
        "salary": round(salary, 2), "employer_nic": round(er_nic, 2),
        "corporation_tax": round(corp_tax, 2), "dividends": round(div, 2),
        "retained_in_company": round(post_tax - div, 2),
        "employee_nic": round(ee, 2), "income_tax_on_salary": round(tax_on_salary, 2),
        "dividend_tax": round(t_div, 2), "personal_allowance_used": round(pa, 2),
        "total_tax_and_nic": round(total_tax, 2), "director_take_home": round(take_home, 2),
        "state_pension_qualifying_year": salary >= LEL,
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--profit", type=float, required=True)
    p.add_argument("--ea", action="store_true")
    p.add_argument("--other-income", type=float, default=0)
    p.add_argument("--scottish", action="store_true")
    p.add_argument("--associates", type=int, default=0)
    p.add_argument("--salaries", default="0,5000,6708,12570")
    p.add_argument("--dividend", default="all")
    p.add_argument("--json", action="store_true")
    a = p.parse_args()
    sals = [float(x) for x in a.salaries.split(",")]
    res = [scenario(a.profit, s, a.ea, a.other_income, a.scottish, a.associates, a.dividend) for s in sals]
    if a.json:
        print(json.dumps(res, indent=2))
        return
    print(f"Profit before director pay £{a.profit:,.0f}; Employment Allowance: {'yes' if a.ea else 'no'}; "
          f"other income £{a.other_income:,.0f}; {'Scottish' if a.scottish else 'rUK'} taxpayer; tax year 2026/27\n")
    hdr = ["Salary", "Er NIC", "Corp tax", "Dividends", "Ee NIC", "IT salary", "Div tax", "Total tax", "Take-home", "SP year"]
    print(" | ".join(f"{h:>10}" for h in hdr))
    best = max(res, key=lambda r: r["director_take_home"] + r["retained_in_company"])
    for r in res:
        row = [r["salary"], r["employer_nic"], r["corporation_tax"], r["dividends"], r["employee_nic"],
               r["income_tax_on_salary"], r["dividend_tax"], r["total_tax_and_nic"], r["director_take_home"]]
        print(" | ".join(f"{v:>10,.0f}" for v in row) + f" | {'yes' if r['state_pension_qualifying_year'] else 'no':>10}"
              + ("   <- lowest total tax" if r is best else ""))
    print("\nEstimates only. Check distributable reserves before paying dividends.")


if __name__ == "__main__":
    main()
