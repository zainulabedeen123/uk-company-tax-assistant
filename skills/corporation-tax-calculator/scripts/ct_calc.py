#!/usr/bin/env python3
"""UK Corporation Tax calculator with marginal relief (FY2023 onwards).

Usage:
  python3 ct_calc.py --profits 120000 [--fii 0] [--associates 0]
                     [--start 2026-01-01 --end 2026-12-31] [--json]

--profits     Taxable total profits (TTP) for the CT accounting period (after capital
              allowances, losses and adjustments).
--fii         Exempt distributions received from non-group companies (added to get
              augmented profits).
--associates  Number of associated companies (excluding this one).
--start/--end CT accounting period (max 12 months). Default: 12-month period.

Formula: MR = fraction x (U - A) x N / A  (CTA 2010 s18B), limits divided by
(1 + associates) and pro-rated by days/365 for each financial year slice.
"""
import argparse
import json
from datetime import date, timedelta

# Financial year (starting 1 April of the given year): rates. Add future years here
# once confirmed by Finance Act. FY2026 verified 25 Oct 2026.
FY = {
    2023: dict(small=0.19, main=0.25, lower=50000, upper=250000, fraction=3 / 200),
    2024: dict(small=0.19, main=0.25, lower=50000, upper=250000, fraction=3 / 200),
    2025: dict(small=0.19, main=0.25, lower=50000, upper=250000, fraction=3 / 200),
    2026: dict(small=0.19, main=0.25, lower=50000, upper=250000, fraction=3 / 200),
}


def fy_of(d):
    return d.year if d >= date(d.year, 4, 1) else d.year - 1


def slices(start, end):
    s = start
    while s <= end:
        fy = fy_of(s)
        fy_end = date(fy + 1, 3, 31)
        e = min(end, fy_end)
        yield fy, s, e
        s = e + timedelta(days=1)


def calc(profits, fii=0.0, associates=0, start=None, end=None):
    if start is None:
        end = end or date(2027, 3, 31)
        start = date(end.year - 1, end.month, end.day) + timedelta(days=1)
    total_days = (end - start).days + 1
    if total_days > 366:
        raise SystemExit("A CT accounting period cannot exceed 12 months - split it first.")
    augmented = profits + fii
    out = {"taxable_total_profits": profits, "augmented_profits": augmented,
           "associated_companies": associates, "period": f"{start} to {end}",
           "days": total_days, "slices": []}
    total_tax = 0.0
    for fy, s, e in slices(start, end):
        if fy not in FY:
            raise SystemExit(f"Rates for FY{fy} not loaded - confirm them (Budget) and add to FY table.")
        r = FY[fy]
        days = (e - s).days + 1
        share = days / total_days
        n = profits * share
        a = augmented * share
        divisor = 1 + associates
        lower = r["lower"] / divisor * days / 365
        upper = r["upper"] / divisor * days / 365
        if a <= lower:
            tax, band, mr = n * r["small"], "small profits rate", 0.0
        elif a >= upper:
            tax, band, mr = n * r["main"], "main rate", 0.0
        else:
            mr = r["fraction"] * (upper - a) * (n / a if a else 0)
            tax, band = n * r["main"] - mr, "main rate less marginal relief"
        total_tax += tax
        out["slices"].append({"financial_year": f"FY{fy}", "from": str(s), "to": str(e), "days": days,
                              "profits": round(n, 2), "lower_limit": round(lower, 2),
                              "upper_limit": round(upper, 2), "band": band,
                              "marginal_relief": round(mr, 2), "tax": round(tax, 2)})
    out["corporation_tax"] = round(total_tax, 2)
    out["effective_rate_pct"] = round(100 * total_tax / profits, 2) if profits else 0
    out["profit_after_tax"] = round(profits - total_tax, 2)
    out["payment_due"] = str(_add9m1d(end))
    return out


def _add9m1d(d):
    import calendar
    y, m = divmod(d.month - 1 + 9, 12)
    y += d.year
    m += 1
    last = calendar.monthrange(y, m)[1]
    month_end = d.day == calendar.monthrange(d.year, d.month)[1]
    day = last if month_end else min(d.day, last)
    return date(y, m, day) + timedelta(days=1)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--profits", type=float, required=True)
    p.add_argument("--fii", type=float, default=0)
    p.add_argument("--associates", type=int, default=0)
    p.add_argument("--start")
    p.add_argument("--end")
    p.add_argument("--json", action="store_true")
    a = p.parse_args()
    s = date.fromisoformat(a.start) if a.start else None
    e = date.fromisoformat(a.end) if a.end else None
    if (s is None) != (e is None):
        raise SystemExit("Give both --start and --end, or neither.")
    r = calc(a.profits, a.fii, a.associates, s, e)
    if a.json:
        print(json.dumps(r, indent=2))
        return
    print(f"Period {r['period']} ({r['days']} days); TTP £{r['taxable_total_profits']:,.2f}; "
          f"augmented £{r['augmented_profits']:,.2f}; associated companies {r['associated_companies']}")
    for sl in r["slices"]:
        print(f"  {sl['financial_year']} {sl['from']}..{sl['to']}: profits £{sl['profits']:,.2f}, limits "
              f"£{sl['lower_limit']:,.2f}/£{sl['upper_limit']:,.2f} -> {sl['band']}; "
              f"MR £{sl['marginal_relief']:,.2f}; tax £{sl['tax']:,.2f}")
    print(f"Corporation Tax: £{r['corporation_tax']:,.2f} (effective {r['effective_rate_pct']}%)")
    print(f"Profit after tax: £{r['profit_after_tax']:,.2f}; payment due {r['payment_due']}")


if __name__ == "__main__":
    main()
